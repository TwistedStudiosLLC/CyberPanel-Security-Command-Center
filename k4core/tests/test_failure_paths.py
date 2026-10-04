"""Failure paths and edge cases: anchor staleness, K4-clock B3 times, step-1 K7 failures, Action-vs-Plan tier,
K11 approval_required flag, malformed Plan input types, R4a/R5a for A4, K7 failures at commit and step 10,
unreadable Grant rows, §21.7 field sets per kind."""

import sqlite3
import unittest
from dataclasses import replace
from datetime import timedelta

from k4core.core import AnchorsNotEstablished, Outcome, UnsupportedInSlice
from k4core.inputs import ApprovalVerificationResult, RootDetermination
from k4core.model import (
    BindingStatus,
    CapExact,
    DecisionStatus,
    Grant,
    Permission,
    PrincipalState,
    TargetSystem,
    Tier,
)

from .support import (
    ADAPTER,
    INSTANCE,
    CoreTestCase,
    FaultyStore,
    added,
    anchor_read,
    plan,
    request,
    step,
    verified,
)

INSTALL_STEP = {
    "capability_id": "install",
    "op": "package.install",
    "resources": ("pkg:fail2ban",),
}

# §21.7 field sets, transcribed independently of k4core.audit.
COMMON = {
    "audit_id",
    "audit_seq",
    "record_class",
    "event_kind",
    "timestamp",
    "recorded_at",
}
EXPECTED_REQUIRED = {
    "A1": COMMON
    | {
        "actor_type",
        "authority_basis",
        "decision",
        "reason_code",
        "capability",
        "action",
        "targets",
    },
    "A2": COMMON
    | {
        "actor_type",
        "authority_basis",
        "decision",
        "reason_code",
        "capability",
        "action",
        "targets",
        "plan_ref",
    },
    "A4": COMMON
    | {
        "actor_type",
        "authority_basis",
        "decision",
        "reason_code",
        "approval_refs",
        "authorization_ref",
    },
    "A6": COMMON
    | {
        "actor_type",
        "authority_basis",
        "decision",
        "reason_code",
        "lro_auth_ref",
        "targets",
    },
    "B1": COMMON | {"condition_kind", "count"},
    "B2": COMMON | {"failure_reason"},
    "B3": COMMON
    | {"named_principal", "anchor_digest", "observed_at", "change_kind", "observer"},
}


class AnchorRelianceTests(CoreTestCase):
    store_class = FaultyStore

    def setUp(self):
        super().setUp()
        self.seed_principal("adm", "admin", roles=("scc.administrator",))
        self.auth = verified("admin", self.clock)

    def test_old_read_not_usable_after_a_failed_newer_read(self):  # §21.12 B3 row
        old = self.establish(("adm", "anc-1"))
        self.assertEqual(
            self.intent(self.auth, req=request("install"), anchors=old).outcome,
            Outcome.OK,
        )
        self.store.fail_audit_kinds = frozenset({"B3"})
        with self.assertRaises(AnchorsNotEstablished):
            self.core.observe_anchor_read(
                anchor_read(("adm", "anc-2"), changes=[added("adm", "anc-2")])
            )
        self.store.fail_audit_kinds = frozenset()
        res = self.intent(self.auth, req=request("install"), anchors=old)
        self.assertEqual(res.reason, "k11_anchors_unestablished")

    def test_old_read_not_usable_after_a_newer_successful_read(self):
        old = self.establish(("adm", "anc-1"))
        self.establish(("adm", "anc-2"))
        self.assertEqual(
            self.intent(self.auth, req=request("install"), anchors=old).reason,
            "k11_anchors_unestablished",
        )

    def test_b3_times_come_from_k4_clock(
        self,
    ):  # §21.7: K4 clock; K4's observation time
        self.clock.advance(3600)
        self.core.observe_anchor_read(
            anchor_read(("adm", "anc-1"), changes=[added("adm", "anc-1")])
        )
        b3 = self.audit("B3")[0]
        self.assertEqual(b3["timestamp"], self.clock.now.isoformat())
        self.assertEqual(b3["observed_at"], self.clock.now.isoformat())


class Step1K7FailureTests(CoreTestCase):
    store_class = FaultyStore

    def setUp(self):
        super().setUp()
        self.seed_principal("p1", "alice", roles=("scc.operator",))

    def test_unreadable_binding_is_step1_failure_b2_not_a1(self):  # §21.6; §21.14
        self.store.fail_reads = True  # reads fail; the B2 write itself still succeeds
        res = self.intent(verified("alice", self.clock))
        self.assertEqual(
            (res.outcome, res.reason), (Outcome.UNAUTHENTICATED, "binding")
        )
        self.store.fail_reads = False
        self.assertEqual([r["failure_reason"] for r in self.audit("B2")], ["binding"])
        self.assertEqual(self.audit("A1"), [])

    def test_confirmation_write_failure_after_step1_denies_without_b2(self):
        original = self.store.transaction

        def failing():
            raise __import__("k4core").K7Unavailable("simulated")

        self.store.transaction = failing
        res = self.intent(verified("alice", self.clock))
        self.store.transaction = original
        self.assertEqual(
            (res.outcome, res.reason), (Outcome.FORBIDDEN, "k7_unavailable")
        )
        self.assertIn("step1:authenticated", res.trace)
        self.assertEqual(self.audit("B2"), [])


class ActionTierTests(CoreTestCase):
    def test_r4_action_requires_approval_even_if_plan_steps_are_lower(
        self,
    ):  # §17.8; §17.10
        self.seed_principal("adm", "admin", roles=("scc.administrator",))
        anchors = self.establish(("adm", "anc"))
        res = self.commit(
            verified("admin", self.clock),
            plan(step(clock=self.clock)),
            req=request("install"),
            anchors=anchors,
        )
        self.assertEqual(res.status, DecisionStatus.AWAITING_APPROVAL)
        self.assertEqual(
            self.store.decision(res.authorization_ref)["step_up_tier"], "R4"
        )

    def test_r4_action_reauth_uses_r4_age(self):
        self.seed_principal("adm", "admin", roles=("scc.administrator",))
        anchors = self.establish(("adm", "anc"))
        res = self.commit(
            verified("admin", self.clock, age=400),
            plan(step(clock=self.clock)),
            req=request("install"),
            anchors=anchors,
        )
        self.assertEqual(res.reason, "reauth_required")  # R4 age 300, R2 age 900


class MalformedInputTypeTests(CoreTestCase):
    def setUp(self):
        super().setUp()
        self.seed_principal("p1", "alice", roles=("scc.operator",))
        self.auth = verified("alice", self.clock)

    def test_wrong_types_are_denied_as_malformed_not_crashes(self):
        cases = [
            plan(step(clock=self.clock, deadline="tomorrow")),
            replace(
                plan(step(clock=self.clock)), newest_input_observation_at="yesterday"
            ),
            plan(step(clock=self.clock, params=5)),
            plan(step(clock=self.clock, selectors=["x"])),
            plan(
                replace(step(clock=self.clock), resource_refs=["svc:fail2ban"])
            ),  # list, not tuple
            plan(step(clock=self.clock, targets=(5,))),
            plan(step(clock=self.clock, deadline=self.clock.now.replace(tzinfo=None))),
            plan(step(clock=self.clock, params={1: "non-string key"})),
            plan(step(clock=self.clock, params={"x": object()})),
        ]
        for i, p in enumerate(cases):
            res = self.commit(self.auth, replace(p))
            self.assertEqual(
                (res.outcome, res.reason), (Outcome.FORBIDDEN, "plan_malformed"), i
            )
        self.assertEqual(len(self.audit("A2")), len(cases))

    def test_cancel_and_approve_are_not_intent_permissions(self):
        for perm in (Permission.CANCEL, Permission.APPROVE):
            with self.assertRaises(UnsupportedInSlice):
                self.intent(self.auth, req=request(permission=perm))


class CommitAndApprovalFailureTests(CoreTestCase):
    store_class = FaultyStore

    def setUp(self):
        super().setUp()
        self.seed_principal("req", "requester", roles=("scc.administrator",))
        self.seed_principal("apr", "approver", roles=("scc.approver",))
        self.anchors = self.establish(("apr", "anc-apr"))
        res = self.commit(
            verified("requester", self.clock),
            plan(step(clock=self.clock, **INSTALL_STEP)),
            req=request("install"),
            anchors=self.anchors,
        )
        self.ref = res.authorization_ref

    def ev(self):
        return ApprovalVerificationResult("ev-1", self.ref, "s1", True, True, "anc-apr")

    def submit(self):
        return self.core.submit_approval(
            self.ev(), self.decls, self.inv, self.pol, self.anchors
        )

    def test_r4a_r5a_approval_not_recorded_without_a4(self):
        self.store.fail_audit_kinds = frozenset({"A4"})
        res = self.submit()
        self.assertEqual(res.outcome, Outcome.UNAVAILABLE)
        self.assertEqual(self.store.approved_steps(self.ref), set())
        self.assertEqual(
            self.store.latest_status(self.ref), DecisionStatus.AWAITING_APPROVAL
        )
        self.store.fail_audit_kinds = frozenset()
        self.assertEqual(self.submit().status, DecisionStatus.AUTHORIZED)

    def test_k7_unavailable_at_step10(self):
        self.store.fail_reads = True
        self.assertEqual(self.submit().outcome, Outcome.UNAVAILABLE)

    def test_k7_unavailable_at_plan_commit_denies(self):
        self.store.fail_reads = True
        res = self.commit(
            verified("requester", self.clock),
            plan(step(clock=self.clock)),
        )
        self.assertNotEqual(res.outcome, Outcome.OK)


class UnreadableStateTests(CoreTestCase):
    def test_unreadable_grant_row_denies(self):  # §17.16
        self.seed_principal("p1", "alice")
        conn = sqlite3.connect(self.path)
        with conn:
            conn.execute(
                "INSERT INTO grants VALUES ('bad', 'principal', 'p1', '{\"oops\": 1}')"
            )
        conn.close()
        res = self.intent(verified("alice", self.clock))
        self.assertEqual(
            (res.outcome, res.reason), (Outcome.FORBIDDEN, "k7_unavailable")
        )

    def test_role_subject_rows_in_k7_do_not_extend_built_in_roles(self):  # §17.3
        self.seed_principal("p1", "alice", roles=("scc.viewer",))
        self.seed_grant(
            Grant(
                "g-role",
                "role",
                "scc.viewer",
                Permission.REQUEST,
                CapExact("fail2ban", "ban"),
                TargetSystem("S1"),
                Tier.R4,
            )
        )
        self.assertEqual(
            self.intent(verified("alice", self.clock)).outcome, Outcome.FORBIDDEN
        )

    def test_bootstrap_when_k7_read_fails(self):
        self.store.close()
        store = FaultyStore(self.path, self.clock)
        from k4core.core import K4Core

        core = K4Core(store, self.clock)
        store.fail_reads = True
        p11 = {
            "platform_adapter_id": ADAPTER,
            "platform_instance_id": INSTANCE,
            "platform_subject_id": "a",
        }
        self.assertEqual(
            core.bootstrap(p11, RootDetermination(True, "r")).outcome,
            Outcome.UNAVAILABLE,
        )
        self.store = store


class FieldSetTests(CoreTestCase):
    def test_every_authorized_kind_carries_its_required_fields(self):
        root = RootDetermination(True, "root-ref")
        p11 = {
            "platform_adapter_id": ADAPTER,
            "platform_instance_id": INSTANCE,
            "platform_subject_id": "admin",
        }
        admin = self.core.bootstrap(p11, root).principal_id  # A6 x2
        self.seed_principal("apr", "approver", roles=("scc.approver",))
        anchors = self.establish((admin, "anc-a"), ("apr", "anc-p"))  # B3 x2
        auth = verified("admin", self.clock)
        res = self.commit(
            auth,
            plan(step(clock=self.clock, **INSTALL_STEP)),
            req=request("install"),
            anchors=anchors,
        )  # A1 + A2
        self.core.submit_approval(
            ApprovalVerificationResult(
                "e", res.authorization_ref, "s1", True, True, "anc-p"
            ),
            self.decls,
            self.inv,
            self.pol,
            anchors,
        )  # A4
        self.intent(
            __import__("k4core.inputs", fromlist=["x"]).AuthenticationFailure(
                "signature"
            )
        )  # B2
        kinds = {r["event_kind"] for r in self.audit()}
        self.assertEqual(kinds, {"A1", "A2", "A4", "A6", "B2", "B3"})
        for rec in self.audit():
            self.assertLessEqual(
                EXPECTED_REQUIRED[rec["event_kind"]], set(rec), rec["event_kind"]
            )

    def test_recorded_at_is_recording_time_and_timestamp_event_time(self):
        self.seed_principal(
            "p1", "alice", status=BindingStatus.UNCONFIRMED, roles=("scc.operator",)
        )
        self.intent(verified("alice", self.clock))
        rec = self.audit("A1")[0]
        self.assertEqual(rec["timestamp"], self.clock.now.isoformat())
        self.assertEqual(rec["recorded_at"], self.clock.now.isoformat())


class StepSevenPlatformRoleTests(CoreTestCase):
    def test_platform_admin_required_at_step7(self):
        self.seed_principal("p1", "alice", roles=("scc.operator",))
        res = self.commit(
            verified("alice", self.clock, role="PLATFORM_USER"),
            plan(step(clock=self.clock)),
        )
        self.assertEqual(
            res.reason, "no_matching_grant"
        )  # denied already at step 4; no Decision
        self.assertEqual(self.decision_rows(), [])

    def test_non_active_principal_writes_no_confirmation(self):
        self.seed_principal(
            "p2",
            "bob",
            state=PrincipalState.SUSPENDED,
            status=BindingStatus.UNCONFIRMED,
            roles=("scc.operator",),
        )
        self.intent(verified("bob", self.clock))
        self.assertEqual(self.store.binding_of("p2").status, BindingStatus.UNCONFIRMED)


class PolicyPlanAgeExpiryTests(CoreTestCase):
    def test_expires_at_driven_by_policy_plan_max_age(self):
        from k4core.policy import LocalSettings, PolicyInputs

        from .support import baseline

        self.seed_principal("p1", "alice", roles=("scc.operator",))
        obs = self.clock.now - timedelta(seconds=100)
        pol = PolicyInputs(
            baseline(plan_max_age_seconds=600),
            LocalSettings(revision=1, plan_max_age_seconds=300),
        )
        res = self.commit(
            verified("alice", self.clock),
            plan(step(clock=self.clock), observed_at=obs),
            pol=pol,
        )
        self.assertEqual(
            self.store.decision(res.authorization_ref)["expires_at"],
            (obs + timedelta(seconds=300)).isoformat(),
        )


if __name__ == "__main__":
    unittest.main()
