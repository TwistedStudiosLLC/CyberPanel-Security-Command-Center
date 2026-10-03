"""Regression tests for findings of the second adversarial review."""

import sqlite3
import unittest

from k4core.core import Outcome
from k4core.inputs import ApprovalVerificationResult
from k4core.model import (
    ApprovalRequired,
    CapExact,
    DecisionStatus,
    Grant,
    Permission,
    TargetSystem,
    Tier,
)
from k4core.policy import LocalSettings, PolicyInputs

from .support import CoreTestCase, baseline, plan, request, step, verified


class SeparationOfDutiesTierTests(CoreTestCase):
    def test_sod_uses_action_or_plan_tier(
        self,
    ):  # §17.8 SoD "per tier"; §17.10 Action-or-Plan tier
        self.seed_principal(
            "req", "requester", roles=("scc.administrator", "scc.approver")
        )
        anchors = self.establish(("req", "anc-req"))
        pol = PolicyInputs(
            baseline(),
            LocalSettings(revision=2, separation_of_duties_tiers=frozenset({Tier.R4})),
        )
        res = self.commit(
            verified("requester", self.clock),
            plan(step(clock=self.clock)),
            req=request("jailcfg"),
            anchors=anchors,
            pol=pol,
        )
        self.assertEqual(res.status, DecisionStatus.AWAITING_APPROVAL)
        out = self.core.submit_approval(
            ApprovalVerificationResult(
                "e1", res.authorization_ref, "s1", True, True, "anc-req"
            ),
            self.decls,
            self.inv,
            pol,
            anchors,
        )
        self.assertEqual(out.reason, "separation_of_duties")
        self.assertEqual(
            self.store.latest_status(res.authorization_ref),
            DecisionStatus.AWAITING_APPROVAL,
        )


class MalformedEnvelopeTests(CoreTestCase):
    def test_non_proposal_envelope_refused_with_no_effect(self):
        self.seed_principal("p1", "alice", roles=("scc.operator",))
        auth = verified("alice", self.clock)
        for bad in (None, object(), (step(clock=self.clock),)):
            res = self.commit(auth, bad)
            self.assertEqual(
                (res.outcome, res.reason),
                (Outcome.MALFORMED, "plan_envelope_malformed"),
            )
        self.assertEqual(self.audit(), [])


class CorruptRowTests(CoreTestCase):
    def test_corrupt_binding_row_is_step1_b2(self):
        self.seed_principal("p1", "alice", roles=("scc.operator",))
        conn = sqlite3.connect(self.path)
        with conn:
            conn.execute("UPDATE bindings SET status='GARBLED'")
        conn.close()
        res = self.intent(verified("alice", self.clock))
        self.assertEqual(
            (res.outcome, res.reason), (Outcome.UNAUTHENTICATED, "binding")
        )
        self.assertEqual(len(self.audit("B2")), 1)

    def test_corrupt_membership_row_denies(self):
        self.seed_principal("p1", "alice", roles=("scc.operator",))
        conn = sqlite3.connect(self.path)
        with conn:
            conn.execute("UPDATE role_memberships SET state='GARBLED'")
        conn.close()
        res = self.intent(verified("alice", self.clock))
        self.assertEqual(
            (res.outcome, res.reason), (Outcome.FORBIDDEN, "k7_unavailable")
        )
        self.assertEqual(self.audit("A1")[0]["decision"], "denied")


class AnchorReadFailureTests(CoreTestCase):
    def test_reported_read_failure_invalidates_earlier_read(self):
        self.seed_principal("adm", "admin", roles=("scc.administrator",))
        anchors = self.establish(("adm", "anc"))
        self.core.anchor_read_failed()
        res = self.intent(
            verified("admin", self.clock), req=request("install"), anchors=anchors
        )
        self.assertEqual(res.reason, "k11_anchors_unestablished")


class GrantsUsedAcrossFullEvaluationTests(CoreTestCase):
    def test_step4_grant_counts_as_used(
        self,
    ):  # owner reading: every matched Grant is used
        self.seed_principal("p1", "alice")
        # The Action's own Grant (step 4) carries APPROVAL_REQUIRED; the Plan's step is covered by another Grant.
        self.seed_grant(
            Grant(
                "g-action",
                "principal",
                "p1",
                Permission.REQUEST,
                CapExact("fail2ban", "status"),
                TargetSystem("S1"),
                Tier.R4,
                (ApprovalRequired(),),
            )
        )
        self.seed_grant(
            Grant(
                "g-plan",
                "principal",
                "p1",
                Permission.REQUEST,
                CapExact("fail2ban", "ban"),
                TargetSystem("S1"),
                Tier.R4,
            )
        )
        res = self.commit(
            verified("alice", self.clock),
            plan(step(clock=self.clock)),
            req=request("status"),
        )
        self.assertEqual(res.matched_grants, ("g-action", "g-plan"))
        self.assertEqual(res.status, DecisionStatus.AWAITING_APPROVAL)
        self.assertEqual(
            self.store.decision(res.authorization_ref)["grants_used"],
            ["g-action", "g-plan"],
        )

    def test_a2_denial_records_action_or_plan_tier(self):
        self.seed_principal("adm", "admin", roles=("scc.administrator",))
        anchors = self.establish(("adm", "anc"))
        self.commit(
            verified("admin", self.clock, age=400),
            plan(step(clock=self.clock)),
            req=request("install"),
            anchors=anchors,
        )
        self.assertEqual(self.audit("A2")[0]["effective_tier"], "R4")


class DecodableButInvalidRowTests(CoreTestCase):
    """Rows that parse but violate the stored-state contract deny (§17.16); they never crash K4."""

    def _exec(self, sql, args=()):
        conn = sqlite3.connect(self.path)
        with conn:
            conn.execute(sql, args)
        conn.close()

    def _grant_body(self, **overrides):
        import json

        body = {
            "grant_id": "g1",
            "subject_kind": "principal",
            "subject_id": "p1",
            "permission": "request",
            "capability_selector": {
                "type": "EXACT",
                "integration_id": "fail2ban",
                "capability_id": "ban",
            },
            "target_selector": {"type": "T_SYSTEM", "system_id": "S1"},
            "max_tier": 4,
            "conditions": [],
            "valid_from": None,
            "valid_until": None,
            "state": "ACTIVE",
        }
        body.update(overrides)
        return json.dumps(body)

    def test_corrupt_grant_variants_deny(self):
        self.seed_principal("p1", "alice")
        variants = [
            {"valid_until": "2030-01-01T00:00:00"},  # naive timestamp
            {
                "capability_selector": {"type": "ALL", "cls": ["any"]}
            },  # class not in the closed set
            {"grant_id": ["x"]},
            {
                "conditions": [{"type": "AUTH_FRESH", "max_age_seconds": 10**20}]
            },  # not representable
            {"conditions": [{"type": "AUTH_FRESH", "max_age_seconds": -1}]},
        ]
        for i, v in enumerate(variants):
            self._exec("DELETE FROM grants")
            self._exec(
                "INSERT INTO grants VALUES ('g1', 'principal', 'p1', ?)",
                (self._grant_body(**v),),
            )
            res = self.intent(verified("alice", self.clock))
            self.assertEqual(
                (res.outcome, res.reason), (Outcome.FORBIDDEN, "k7_unavailable"), i
            )

    def test_naive_membership_validity_denies(self):
        self.seed_principal("p1", "alice", roles=("scc.operator",))
        self._exec("UPDATE role_memberships SET valid_until='2030-01-01T00:00:00'")
        self.assertEqual(
            self.intent(verified("alice", self.clock)).reason, "k7_unavailable"
        )

    def test_corrupt_decision_body_at_step10_is_unavailable(self):
        self.seed_principal("req", "requester", roles=("scc.administrator",))
        self.seed_principal("apr", "approver", roles=("scc.approver",))
        anchors = self.establish(("apr", "anc"))
        res = self.commit(
            verified("requester", self.clock),
            plan(step(clock=self.clock)),
            req=request("install"),
            anchors=anchors,
        )
        conn = sqlite3.connect(self.path)
        with conn:
            conn.execute("DROP TRIGGER decisions_no_update")
            conn.execute("UPDATE decisions SET body='[1, 2]'")
        conn.close()
        out = self.core.submit_approval(
            ApprovalVerificationResult(
                "e", res.authorization_ref, "s1", True, True, "anc"
            ),
            self.decls,
            self.inv,
            self.pol,
            anchors,
        )
        self.assertEqual(out.outcome, Outcome.UNAVAILABLE)


class StepFourPlanMaxAgeTests(CoreTestCase):
    def test_plan_max_age_on_a_step4_grant_is_evaluated_at_decision_time(self):
        from datetime import timedelta

        from k4core.model import PlanMaxAge

        self.seed_principal("p1", "alice")
        self.seed_grant(
            Grant(
                "g-action",
                "principal",
                "p1",
                Permission.REQUEST,
                CapExact("fail2ban", "status"),
                TargetSystem("S1"),
                Tier.R4,
                (PlanMaxAge(60),),
            )
        )
        self.seed_grant(
            Grant(
                "g-plan",
                "principal",
                "p1",
                Permission.REQUEST,
                CapExact("fail2ban", "ban"),
                TargetSystem("S1"),
                Tier.R4,
            )
        )
        auth = verified("alice", self.clock)
        stale = plan(
            step(clock=self.clock), observed_at=self.clock.now - timedelta(seconds=600)
        )
        self.assertEqual(
            self.commit(auth, stale, req=request("status")).reason, "plan_max_age"
        )
        missing = plan(step(clock=self.clock))
        self.assertEqual(
            self.commit(auth, missing, req=request("status")).reason, "plan_max_age"
        )
        fresh = plan(
            step(clock=self.clock),
            observed_at=self.clock.now - timedelta(seconds=30),
        )
        res = self.commit(auth, fresh, req=request("status"))
        self.assertEqual(res.outcome, Outcome.OK)
        self.assertGreater(
            self.store.decision(res.authorization_ref)["expires_at"],
            self.clock.now.isoformat(),
        )


class BoundaryInputValidationTests(unittest.TestCase):
    def test_wrong_types_rejected_at_the_boundary(self):
        from datetime import datetime

        from k4core.inputs import (
            ActionRequest,
            RootDetermination,
            VerifiedAuthentication,
        )
        from k4core.model import CapabilityRef

        cap = CapabilityRef("fail2ban", "ban")
        bad = [
            lambda: ActionRequest(cap, None, ("sys-1",)),
            lambda: ActionRequest(cap, "a", (["sys-1"],)),
            lambda: ActionRequest(cap, "a", ["sys-1"]),
            lambda: VerifiedAuthentication(
                "a",
                "x",
                "y",
                "z",
                datetime(2026, 1, 1),  # noqa: DTZ001
            ),  # naive auth_time
            lambda: VerifiedAuthentication("a", "x", "y", "z", "now"),
            lambda: ApprovalVerificationResult("e", None, "s1", True, True, "anc"),
            lambda: ApprovalVerificationResult("e", "r", "s1", "yes", True, "anc"),
            lambda: RootDetermination("true", "ref"),
            lambda: __import__(
                "k4core.inputs", fromlist=["K11AnchorRead"]
            ).K11AnchorRead((("p", "d"),)),
        ]
        for i, make in enumerate(bad):
            with self.assertRaises(TypeError, msg=str(i)):
                make()


class LastRoundHardeningTests(CoreTestCase):
    def test_unencodable_strings_rejected_at_boundary_and_p11(self):
        from k4core.inputs import RootDetermination, VerifiedAuthentication

        lone = chr(0xD800)
        with self.assertRaises(TypeError):
            VerifiedAuthentication("a", "x", "y", lone, self.clock.now)
        with self.assertRaises(TypeError):
            ApprovalVerificationResult(lone, "r", "s", True, True, "d")
        p11 = {
            "platform_adapter_id": lone,
            "platform_instance_id": "i",
            "platform_subject_id": "s",
        }
        self.assertEqual(
            self.core.bootstrap(p11, RootDetermination(True, "r")).outcome,
            Outcome.MALFORMED,
        )

    def test_invalid_baseline_role_grant_makes_policy_unavailable(self):
        from k4core.model import AuthFresh, CapAll, GrantSpec, TargetAny

        self.seed_principal("p1", "alice", roles=("scc.operator",))
        roles = {
            "scc.operator": (
                GrantSpec(
                    Permission.REQUEST,
                    CapAll("any"),
                    TargetAny(),
                    Tier.R2,
                    (AuthFresh(10**15),),
                ),
            )
        }
        pol = PolicyInputs(baseline(role_grants=roles), LocalSettings(revision=1))
        self.assertEqual(
            self.intent(verified("alice", self.clock), pol=pol).reason,
            "policy_unavailable",
        )
        roles = {
            "scc.operator": (
                GrantSpec(
                    Permission.REQUEST, CapAll("everything"), TargetAny(), Tier.R2
                ),
            )
        }
        pol = PolicyInputs(baseline(role_grants=roles), LocalSettings(revision=1))
        self.assertEqual(
            self.intent(verified("alice", self.clock), pol=pol).reason,
            "policy_unavailable",
        )

    def test_deep_or_cyclic_params_denied_at_step5(self):
        self.seed_principal("p1", "alice", roles=("scc.operator",))
        deep: dict = {}
        cur = deep
        for _ in range(5000):
            cur["x"] = {}
            cur = cur["x"]
        cyclic: dict = {}
        cyclic["self"] = cyclic
        for i, params in enumerate((deep, cyclic)):
            res = self.commit(
                verified("alice", self.clock),
                plan(step(clock=self.clock, params=params)),
            )
            self.assertEqual(
                (res.outcome, res.reason), (Outcome.FORBIDDEN, "plan_malformed")
            )

    def test_ambiguous_anchor_digest_fails_closed(self):
        self.seed_principal("req", "requester", roles=("scc.administrator",))
        self.seed_principal("a1", "approver1", roles=("scc.approver",))
        self.seed_principal("a2", "approver2", roles=("scc.approver",))
        anchors = self.establish(("a1", "same"), ("a2", "same"), ("req", "anc-req"))
        res = self.commit(
            verified("requester", self.clock),
            plan(step(clock=self.clock)),
            req=request("install"),
            anchors=anchors,
        )
        out = self.core.submit_approval(
            ApprovalVerificationResult(
                "e", res.authorization_ref, "s1", True, True, "same"
            ),
            self.decls,
            self.inv,
            self.pol,
            anchors,
        )
        self.assertEqual(out.reason, "signature_not_verified_against_anchor")


if __name__ == "__main__":
    unittest.main()
