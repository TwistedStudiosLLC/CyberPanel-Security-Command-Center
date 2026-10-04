"""DEC-090 D90-7 corrections: Q2 K11 flag (D90-3), Q3 future times (D90-4), Q4 Role-subject Grants (D90-5),
Q5 plan_ref and invalidation (D90-6)."""

import sqlite3
import unittest
from dataclasses import fields, replace
from datetime import timedelta
from unittest import mock

from k4core.core import Outcome
from k4core.inputs import ApprovalVerificationResult, PlanProposal
from k4core.model import (
    ApprovalRequired,
    AuthFresh,
    CapExact,
    DecisionStatus,
    Grant,
    Permission,
    PlanMaxAge,
    TargetSystem,
    Tier,
)
from k4core.policy import LocalSettings, PolicyInputs

from .support import CoreTestCase, baseline, declarations, plan, request, step, verified

TINY = timedelta(microseconds=1)


def flagged_ban_declarations():
    """The R2 'ban' capability's scope entry carries the K11 approval_required flag."""
    decls = declarations()
    d = decls.declarations[0]
    entries = tuple(
        replace(e, approval_required=True) if e.capability_id == "ban" else e
        for e in d.scope_entries
    )
    return replace(decls, declarations=(replace(d, scope_entries=entries),))


def grant(gid, pid, cap_id="ban", tier=Tier.R4, conditions=(), perm=Permission.REQUEST):
    return Grant(
        gid,
        "principal",
        pid,
        perm,
        CapExact("fail2ban", cap_id),
        TargetSystem("S1"),
        tier,
        tuple(conditions),
    )


# =================================================================================================================
# Q2 — the K11 flag is not a K4 Plan-level trigger; flagged + no trigger is refused (option C)
# =================================================================================================================


class K11FlagTests(CoreTestCase):
    def setUp(self):
        super().setUp()
        self.flagged = flagged_ban_declarations()

    def test_flagged_below_r4_without_trigger_is_refused_with_a2(self):
        self.seed_principal("p1", "alice", roles=("scc.operator",))
        res = self.commit(
            verified("alice", self.clock),
            plan(step(clock=self.clock)),
            decls=self.flagged,
        )
        self.assertEqual(
            (res.outcome, res.reason),
            (Outcome.FORBIDDEN, "k11_flag_without_k4_approval_requirement"),
        )
        a2 = self.audit("A2")[-1]
        self.assertEqual(
            (a2["decision"], a2["reason_code"]),
            ("denied", "k11_flag_without_k4_approval_requirement"),
        )
        self.assertEqual(self.decision_rows(), [])

    def test_flag_alone_never_adds_plan_wide_approval(self):
        # Without the flag, the same Plan is AUTHORIZED with no approval; with it, it is refused, never
        # AWAITING_APPROVAL.
        self.seed_principal("p1", "alice", roles=("scc.operator",))
        auth = verified("alice", self.clock)
        self.assertEqual(
            self.commit(auth, plan(step(clock=self.clock))).status,
            DecisionStatus.AUTHORIZED,
        )
        flagged = self.commit(auth, plan(step(clock=self.clock)), decls=self.flagged)
        self.assertIsNone(flagged.status)
        self.assertNotIn("AWAITING_APPROVAL", str(self.audit("A2")[-1]))

    def test_flagged_with_r4_action_uses_existing_approval_path(self):
        self.seed_principal("adm", "admin", roles=("scc.administrator",))
        anchors = self.establish(("adm", "anc"))
        res = self.commit(
            verified("admin", self.clock),
            plan(step(clock=self.clock)),
            req=request("install"),
            anchors=anchors,
            decls=self.flagged,
        )
        self.assertEqual(res.status, DecisionStatus.AWAITING_APPROVAL)

    def test_flagged_with_approval_required_grant_uses_existing_approval_path(self):
        self.seed_principal("p1", "alice")
        self.seed_grant(grant("g1", "p1", conditions=(ApprovalRequired(),)))
        res = self.commit(
            verified("alice", self.clock),
            plan(step(clock=self.clock)),
            decls=self.flagged,
        )
        self.assertEqual(res.status, DecisionStatus.AWAITING_APPROVAL)

    def test_flagged_with_local_setting_uses_existing_approval_path(self):
        self.seed_principal("p1", "alice", roles=("scc.operator",))
        pol = PolicyInputs(
            baseline(),
            LocalSettings(revision=2, approval_required_tiers=frozenset({Tier.R2})),
        )
        res = self.commit(
            verified("alice", self.clock),
            plan(step(clock=self.clock)),
            decls=self.flagged,
            pol=pol,
        )
        self.assertEqual(res.status, DecisionStatus.AWAITING_APPROVAL)

    def test_scope_entry_flag_defaults_to_false(self):
        from k4core.inputs import ScopeEntry

        self.assertFalse(
            ScopeEntry(
                "c", "service.control", 1, "write", frozenset()
            ).approval_required
        )

    def test_any_flagged_covering_entry_counts(self):
        decls = declarations()
        d = decls.declarations[0]
        extra = replace(
            next(e for e in d.scope_entries if e.capability_id == "ban"),
            approval_required=True,
        )
        decls = replace(
            decls, declarations=(replace(d, scope_entries=d.scope_entries + (extra,)),)
        )
        self.seed_principal("p1", "alice", roles=("scc.operator",))
        res = self.commit(
            verified("alice", self.clock), plan(step(clock=self.clock)), decls=decls
        )
        self.assertEqual(res.reason, "k11_flag_without_k4_approval_requirement")


# =================================================================================================================
# Q3 — a time later than K4's clock, by any amount, is not fresh; equal to the clock is fresh
# =================================================================================================================


class FutureTimeTests(CoreTestCase):
    def setUp(self):
        super().setUp()
        self.seed_principal("p1", "alice")

    def auth_at(self, offset):
        a = verified("alice", self.clock)
        return replace(a, auth_time=self.clock.now + offset)

    def test_auth_fresh_condition(self):
        self.seed_grant(grant("g1", "p1", conditions=(AuthFresh(60),)))
        self.assertEqual(self.intent(self.auth_at(timedelta(0))).outcome, Outcome.OK)
        self.assertEqual(self.intent(self.auth_at(TINY)).outcome, Outcome.FORBIDDEN)
        self.assertEqual(
            self.intent(self.auth_at(timedelta(days=365))).outcome, Outcome.FORBIDDEN
        )

    def test_reauth(self):
        self.seed_grant(grant("g1", "p1"))
        self.assertEqual(
            self.commit(
                self.auth_at(timedelta(0)), plan(step(clock=self.clock))
            ).outcome,
            Outcome.OK,
        )
        res = self.commit(self.auth_at(TINY), plan(step(clock=self.clock)))
        self.assertEqual(res.reason, "reauth_required")

    def test_plan_max_age_condition(self):
        self.seed_grant(grant("g1", "p1", conditions=(PlanMaxAge(300),)))
        auth = verified("alice", self.clock)
        ok = self.commit(auth, plan(step(clock=self.clock), observed_at=self.clock.now))
        self.assertEqual(ok.outcome, Outcome.OK)
        res = self.commit(
            auth, plan(step(clock=self.clock), observed_at=self.clock.now + TINY)
        )
        self.assertEqual(res.reason, "plan_not_covered")

    def test_plan_max_age_on_step4_grant(self):
        self.seed_grant(
            grant("g-action", "p1", cap_id="status", conditions=(PlanMaxAge(300),))
        )
        self.seed_grant(grant("g-plan", "p1"))
        auth = verified("alice", self.clock)
        res = self.commit(
            auth,
            plan(step(clock=self.clock), observed_at=self.clock.now + TINY),
            req=request("status"),
        )
        self.assertEqual(res.reason, "plan_max_age")

    def test_policy_plan_maximum_age(self):
        self.seed_grant(grant("g1", "p1"))
        pol = PolicyInputs(
            baseline(plan_max_age_seconds=600), LocalSettings(revision=1)
        )
        auth = verified("alice", self.clock)
        ok = self.commit(
            auth, plan(step(clock=self.clock), observed_at=self.clock.now), pol=pol
        )
        self.assertEqual(ok.outcome, Outcome.OK)
        res = self.commit(
            auth,
            plan(step(clock=self.clock), observed_at=self.clock.now + TINY),
            pol=pol,
        )
        self.assertEqual(res.reason, "plan_max_age")

    def test_no_tolerance_even_for_large_max_age(self):
        self.seed_grant(grant("g1", "p1", conditions=(AuthFresh(10**9),)))
        self.assertEqual(self.intent(self.auth_at(TINY)).outcome, Outcome.FORBIDDEN)


# =================================================================================================================
# Q4 — a Role-subject Grant row for a held Role fails closed; never ignored
# =================================================================================================================


class RoleSubjectGrantTests(CoreTestCase):
    def role_row(self, role, cap_id="status", tier=Tier.R0):
        self.seed_grant(
            Grant(
                f"rg-{role}",
                "role",
                role,
                Permission.REQUEST,
                CapExact("fail2ban", cap_id),
                TargetSystem("S1"),
                tier,
            )
        )

    def test_step4_denied_a1(self):
        self.seed_principal("p1", "alice", roles=("scc.operator",))
        self.role_row(
            "scc.operator"
        )  # would not even match the request: still fails closed
        res = self.intent(verified("alice", self.clock))
        self.assertEqual(
            (res.outcome, res.reason),
            (Outcome.FORBIDDEN, "role_subject_grant_unsupported"),
        )
        self.assertEqual(
            self.audit("A1")[-1]["reason_code"], "role_subject_grant_unsupported"
        )

    def test_not_silently_ignored(self):
        # The direct Grant alone would authorize; the encountered Role-subject row must still deny.
        self.seed_principal("p1", "alice", roles=("scc.viewer",))
        self.seed_grant(grant("g1", "p1"))
        self.assertEqual(self.intent(verified("alice", self.clock)).outcome, Outcome.OK)
        self.role_row("scc.viewer")
        self.assertEqual(
            self.intent(verified("alice", self.clock)).reason,
            "role_subject_grant_unsupported",
        )

    def test_step7_denied_a2(self):
        self.seed_principal("p1", "alice", roles=("scc.operator",))
        auth = verified("alice", self.clock)
        original = self.store.role_subject_grant_exists
        calls = {"n": 0}

        def appears_after_step4(role_id):
            calls["n"] += 1
            return (
                calls["n"] > 1 and original(role_id) is False
            )  # the row appears once step 4 has passed

        self.store.role_subject_grant_exists = appears_after_step4
        res = self.commit(auth, plan(step(clock=self.clock)))
        self.store.role_subject_grant_exists = original
        self.assertEqual(res.reason, "role_subject_grant_unsupported")
        self.assertEqual(
            self.audit("A2")[-1]["reason_code"], "role_subject_grant_unsupported"
        )
        self.assertEqual(self.decision_rows(), [])

    def test_step10_rejected_a4(self):
        self.seed_principal("req", "requester", roles=("scc.administrator",))
        self.seed_principal("apr", "approver", roles=("scc.approver",))
        anchors = self.establish(("apr", "anc"))
        res = self.commit(
            verified("requester", self.clock),
            plan(step(clock=self.clock)),
            req=request("install"),
            anchors=anchors,
        )
        self.role_row("scc.approver")
        out = self.core.submit_approval(
            ApprovalVerificationResult(
                "e", res.authorization_ref, "s1", True, True, "anc"
            ),
            self.decls,
            self.inv,
            self.pol,
            anchors,
        )
        self.assertEqual(
            (out.outcome, out.reason),
            (Outcome.FORBIDDEN, "role_subject_grant_unsupported"),
        )
        a4 = self.audit("A4")[-1]
        self.assertEqual(
            (a4["decision"], a4["reason_code"]),
            ("rejected", "role_subject_grant_unsupported"),
        )

    def test_row_for_role_not_held_has_no_effect(self):
        self.seed_principal("p1", "alice", roles=("scc.operator",))
        self.role_row("scc.administrator")
        self.assertEqual(self.intent(verified("alice", self.clock)).outcome, Outcome.OK)

    def test_revoked_row_still_counts_as_encountered(self):
        self.seed_principal("p1", "alice", roles=("scc.operator",))
        from k4core.model import RecordState

        self.seed_grant(
            Grant(
                "rg",
                "role",
                "scc.operator",
                Permission.REQUEST,
                CapExact("fail2ban", "ban"),
                TargetSystem("S1"),
                Tier.R4,
                state=RecordState.REVOKED,
            )
        )
        self.assertEqual(
            self.intent(verified("alice", self.clock)).reason,
            "role_subject_grant_unsupported",
        )


# =================================================================================================================
# Q5 — K4-generated plan_ref; every commit is a new Plan; no invalidation; one Decision per digest
# =================================================================================================================


class PlanRefAndInvalidationTests(CoreTestCase):
    def setUp(self):
        super().setUp()
        self.seed_principal("a", "alice", roles=("scc.operator",))
        self.seed_principal("b", "bob", roles=("scc.operator",))

    def statuses(self, ref):
        return self.store.statuses(ref)

    def test_proposal_carries_no_plan_ref(self):
        self.assertNotIn("plan_ref", {f.name for f in fields(PlanProposal)})

    def test_plan_ref_generated_by_k4_and_unique_per_commit(self):
        auth = verified("alice", self.clock)
        r1 = self.commit(auth, plan(step(clock=self.clock)))
        r2 = self.commit(
            auth, plan(step(clock=self.clock))
        )  # identical logical content
        rows = self.decision_rows()
        self.assertEqual(len(rows), 2)
        self.assertNotEqual(rows[0][1], rows[1][1])  # two independently created Plans
        self.assertNotEqual(r1.plan_digest, r2.plan_digest)
        self.assertEqual(
            self.store.decision(r1.authorization_ref)["plan_ref"], rows[0][1]
        )

    def test_no_invalidated_write_on_changed_content(self):
        auth = verified("alice", self.clock)
        first = self.commit(auth, plan(step(clock=self.clock)))
        self.commit(auth, plan(step(clock=self.clock, params={"ip": "192.0.2.9"})))
        self.assertEqual(
            self.statuses(first.authorization_ref), [DecisionStatus.AUTHORIZED]
        )

    def test_denied_commit_has_no_invalidation_effect(self):
        first = self.commit(verified("alice", self.clock), plan(step(clock=self.clock)))
        denied = self.commit(
            verified("alice", self.clock, age=5000), plan(step(clock=self.clock))
        )
        self.assertEqual(denied.reason, "reauth_required")
        self.assertEqual(
            self.statuses(first.authorization_ref), [DecisionStatus.AUTHORIZED]
        )

    def test_other_principals_commit_has_no_effect(self):
        first = self.commit(verified("alice", self.clock), plan(step(clock=self.clock)))
        self.commit(verified("bob", self.clock), plan(step(clock=self.clock)))
        self.commit(verified("bob", self.clock, age=5000), plan(step(clock=self.clock)))
        self.assertEqual(
            self.statuses(first.authorization_ref), [DecisionStatus.AUTHORIZED]
        )

    def test_invalidated_never_written(self):
        auth = verified("alice", self.clock)
        for i in range(3):
            self.commit(auth, plan(step(clock=self.clock, params={"ip": str(i)})))
        self.commit(
            verified("alice", self.clock, age=5000), plan(step(clock=self.clock))
        )
        conn = sqlite3.connect(self.path)
        n = conn.execute(
            "SELECT COUNT(*) FROM decision_status WHERE status='INVALIDATED'"
        ).fetchone()[0]
        conn.close()
        self.assertEqual(n, 0)

    def test_one_decision_per_digest_guard(self):  # A-24, keyed on plan_digest only
        auth = verified("alice", self.clock)
        with mock.patch.object(
            self.core, "_new_plan_ref", return_value="fixed-plan-ref"
        ):
            first = self.commit(auth, plan(step(clock=self.clock)))
            again = self.commit(auth, plan(step(clock=self.clock)))
        self.assertEqual(first.outcome, Outcome.OK)
        self.assertEqual(again.reason, "plan_already_decided")
        digests = [r[2] for r in self.decision_rows()]
        self.assertEqual(len(digests), len(set(digests)))

    def test_digest_is_deterministic_for_same_content_and_plan_ref(self):
        from k4core.core import _plan_content
        from k4core.serialization import canonical_json, sha256_hex

        p1 = plan(step(clock=self.clock, params={"b": 1, "a": [1, 2]}))
        p2 = plan(step(clock=self.clock, params={"a": [1, 2], "b": 1}))
        d = lambda p, ref: sha256_hex(canonical_json(_plan_content(p, ref)))
        self.assertEqual(d(p1, "r"), d(p2, "r"))
        self.assertNotEqual(d(p1, "r"), d(p1, "other"))

    def test_step5_denial_still_records_a2_with_k4_plan_ref(self):
        self.commit(verified("alice", self.clock), plan())
        a2 = self.audit("A2")[-1]
        self.assertEqual(a2["reason_code"], "plan_malformed")
        self.assertTrue(isinstance(a2["plan_ref"], str) and len(a2["plan_ref"]) == 32)


if __name__ == "__main__":
    unittest.main()
