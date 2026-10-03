"""§17.22 Phases II–III (steps 5–9): Plan validation, K11 coverage, plan_digest, Plan tier, Plan Authorization,
REAUTH, Decision creation, INVALIDATED (§17.11; DEC-089 Q4), approval requirement (§17.8; D89-22)."""

import unittest
from dataclasses import replace
from datetime import timedelta

from k4core.core import Outcome, UnsupportedInSlice
from k4core.model import (
    ApprovalRequired,
    CapExact,
    DecisionStatus,
    Grant,
    Permission,
    PlanMaxAge,
    TargetSystem,
    Tier,
)
from k4core.policy import LocalSettings, PolicyInputs

from .support import CoreTestCase, baseline, plan, request, step, verified


def direct(gid, pid, cap_id="ban", sys="S1", tier=Tier.R4, conditions=(), **kw):
    return Grant(
        gid,
        "principal",
        pid,
        Permission.REQUEST,
        CapExact("fail2ban", cap_id),
        TargetSystem(sys),
        tier,
        tuple(conditions),
        **kw,
    )


class PlanValidationTests(CoreTestCase):
    def setUp(self):
        super().setUp()
        self.seed_principal("p1", "alice", roles=("scc.operator",))
        self.auth = verified("alice", self.clock)

    def test_valid_plan_authorized_without_approval(self):
        res = self.commit(self.auth, plan(step(clock=self.clock)))
        self.assertEqual(
            (res.outcome, res.status), (Outcome.OK, DecisionStatus.AUTHORIZED), res
        )
        self.assertEqual(
            self.store.statuses(res.authorization_ref), [DecisionStatus.AUTHORIZED]
        )
        a2 = self.audit("A2")[0]
        self.assertEqual(a2["authorization_ref"], res.authorization_ref)
        self.assertEqual(a2["plan_digest"], res.plan_digest)
        self.assertEqual(
            len(self.audit("A1")), 1
        )  # plan commit re-runs steps 1–4 (§17.13.1)

    def test_trace_runs_steps_in_order(self):
        res = self.commit(self.auth, plan(step(clock=self.clock)))
        order = [s for s in res.trace if s.startswith("step")]
        expected = [
            "step1:authenticate",
            "step1:authenticated",
            "step2:identify",
            "step3:admissibility",
            "step4:intent_authorization",
            "step5:plan_validation",
            "step6:plan_tier",
            "step7:plan_authorization",
            "step8:step_up",
            "step9:create_decision",
        ]
        self.assertEqual(order, expected)

    def test_malformed_plans(self):
        cases = [
            plan(),
            plan(step(step_id="", clock=self.clock)),
            plan(step(clock=self.clock), step(clock=self.clock)),  # duplicate step_id
            plan(step(op="nodot", clock=self.clock)),
            plan(step(op_class="exec", clock=self.clock)),
            plan(step(params={"x": float("nan")}, clock=self.clock)),
        ]
        for i, p in enumerate(cases):
            res = self.commit(self.auth, replace(p, plan_ref=f"plan-m{i}"))
            self.assertEqual(
                (res.outcome, res.reason), (Outcome.FORBIDDEN, "plan_malformed"), i
            )
        self.assertEqual(len(self.audit("A2")), len(cases))
        self.assertTrue(all(r["decision"] == "denied" for r in self.audit("A2")))

    def test_a2_denial_records_resolved_targets(self):
        self.commit(self.auth, plan())
        self.assertEqual(self.audit("A2")[0]["targets"], ["system:S1"])

    def test_insufficient_k11_coverage(self):
        cases = [
            step(resources=("svc:sshd",), clock=self.clock),  # resource not in scope
            step(
                op="service.restart", clock=self.clock
            ),  # operation not in scope entry
            step(op_major=2, clock=self.clock),  # major version
            step(op_class="read", clock=self.clock),  # class mismatch
            step(declaration_digest="stale", clock=self.clock),
            step(handle_refs=("cred:x",), clock=self.clock),
        ]
        for i, s in enumerate(cases):
            res = self.commit(self.auth, plan(s, plan_ref=f"p-{i}"))
            self.assertEqual(res.reason, "k11_coverage_insufficient", i)
        self.assertEqual(self.store.decisions_for_plan("p-0"), [])

    def test_scope_mismatch_between_step_and_capability(self):
        # The 'status' scope entry does not cover a WRITE op for 'ban'.
        res = self.commit(
            self.auth,
            plan(step(capability_id="status", op="service.control", clock=self.clock)),
        )
        self.assertEqual(res.reason, "k11_coverage_insufficient")

    def test_deterministic_digest(self):
        p = plan(step(clock=self.clock, params={"b": 1, "a": [1, 2]}))
        d1 = self.commit(self.auth, p).plan_digest
        same = plan(step(clock=self.clock, params={"a": [1, 2], "b": 1}))
        res = self.commit(self.auth, same)
        self.assertEqual(res.plan_digest, d1)
        self.assertEqual(res.reason, "plan_already_decided")  # A-24
        other = plan(step(clock=self.clock, params={"a": [2, 1], "b": 1}))
        self.assertNotEqual(
            self.core.commit_plan(
                request(),
                self.auth,
                self.decls,
                self.inv,
                self.adm,
                self.pol,
                None,
                replace(other, plan_ref="plan-9"),
            ).plan_digest,
            d1,
        )

    def test_plan_content_not_in_audit(self):  # §21.20
        self.commit(
            self.auth, plan(step(clock=self.clock, params={"ip": "198.51.100.99"}))
        )
        self.assertNotIn("198.51.100.99", str(self.store.audit_records()))

    def test_every_pair_must_be_covered(self):
        p = plan(
            step("s1", clock=self.clock),
            step("s2", targets=("sys-2",), clock=self.clock),
        )
        self.assertEqual(self.commit(self.auth, p).outcome, Outcome.OK)
        self.seed_principal("p2", "bob")
        self.seed_grant(direct("g1", "p2", sys="S1"))
        res = self.commit(verified("bob", self.clock), replace(p, plan_ref="plan-2"))
        self.assertEqual(res.reason, "plan_not_covered")  # A-25: whole Plan or nothing

    def test_plan_tier_is_highest_step(self):
        self.seed_principal("p2", "root-admin", roles=("scc.administrator",))
        anchors = self.establish(("p2", "anc"))
        p = plan(
            step("s1", clock=self.clock),
            step(
                "s2",
                capability_id="install",
                op="package.install",
                resources=("pkg:fail2ban",),
                clock=self.clock,
            ),
        )
        res = self.commit(verified("root-admin", self.clock), p, anchors=anchors)
        self.assertEqual(res.effective_tier, Tier.R4)
        self.assertEqual(res.status, DecisionStatus.AWAITING_APPROVAL)

    def test_reserved_capability_plans_are_outside_slice(self):
        self.seed_principal("p2", "root-admin", roles=("scc.administrator",))
        before = self.store.audit_records()
        with self.assertRaises(UnsupportedInSlice):
            self.commit(
                verified("root-admin", self.clock),
                plan(step(clock=self.clock)),
                req=request("scc.enroll", targets=("scc",)),
            )
        self.assertEqual(self.store.audit_records(), before)


class StepUpTests(CoreTestCase):
    def setUp(self):
        super().setUp()
        self.seed_principal("p1", "alice", roles=("scc.operator",))

    def test_reauth_within_tier_age(self):
        self.assertEqual(
            self.commit(
                verified("alice", self.clock, age=899), plan(step(clock=self.clock))
            ).outcome,
            Outcome.OK,
        )

    def test_reauth_failure_denies_whole_plan(self):
        res = self.commit(
            verified("alice", self.clock, age=901), plan(step(clock=self.clock))
        )
        self.assertEqual(
            (res.outcome, res.reason), (Outcome.FORBIDDEN, "reauth_required")
        )
        self.assertEqual(self.audit("A2")[0]["reason_code"], "reauth_required")

    def test_local_settings_shorten_reauth_age(self):
        pol = PolicyInputs(
            baseline(), LocalSettings(revision=5, reauth_max_age_seconds={Tier.R2: 60})
        )
        res = self.commit(
            verified("alice", self.clock, age=120),
            plan(step(clock=self.clock)),
            pol=pol,
        )
        self.assertEqual(res.reason, "reauth_required")

    def test_unconfigured_reauth_age_denies(self):
        pol = PolicyInputs(
            baseline(reauth_max_age_seconds={}), LocalSettings(revision=1)
        )
        self.assertEqual(
            self.commit(
                verified("alice", self.clock), plan(step(clock=self.clock)), pol=pol
            ).reason,
            "policy_unavailable",
        )

    def test_method_claims_never_satisfy_approval(self):  # A-18
        self.seed_principal("p2", "root-admin", roles=("scc.administrator",))
        anchors = self.establish(("p2", "anc"))
        p = plan(
            step(
                capability_id="install",
                op="package.install",
                resources=("pkg:fail2ban",),
                clock=self.clock,
            )
        )
        res = self.commit(
            verified("root-admin", self.clock),
            p,
            req=request("install"),
            anchors=anchors,
        )
        self.assertEqual(res.status, DecisionStatus.AWAITING_APPROVAL)


class ApprovalRequirementTests(CoreTestCase):
    def setUp(self):
        super().setUp()
        self.seed_principal("p1", "alice")
        self.auth = verified("alice", self.clock)

    def decision(self, ref):
        return self.store.decision(ref)

    def test_approval_required_grant_makes_every_request_approval_requiring(
        self,
    ):  # §17.8; D89-22
        self.seed_grant(direct("g1", "p1", sys="S1", conditions=[ApprovalRequired()]))
        self.seed_grant(direct("g2", "p1", sys="S2"))
        p = plan(
            step("s1", clock=self.clock),
            step("s2", targets=("sys-2",), clock=self.clock),
        )
        res = self.commit(self.auth, p)
        self.assertEqual(res.status, DecisionStatus.AWAITING_APPROVAL)
        self.assertEqual(
            self.decision(res.authorization_ref)["approval_steps"], ["s1", "s2"]
        )

    def test_any_matched_grant_with_approval_required_counts(
        self,
    ):  # owner reading: used = matched
        self.seed_grant(direct("g1", "p1", conditions=[ApprovalRequired()]))
        self.seed_grant(direct("g2", "p1"))
        res = self.commit(self.auth, plan(step(clock=self.clock)))
        self.assertEqual(res.matched_grants, ("g1", "g2"))
        self.assertEqual(res.status, DecisionStatus.AWAITING_APPROVAL)

    def test_local_settings_add_approval_below_r4(self):
        self.seed_grant(direct("g1", "p1"))
        pol = PolicyInputs(
            baseline(),
            LocalSettings(revision=2, approval_required_tiers=frozenset({Tier.R2})),
        )
        self.assertEqual(
            self.commit(self.auth, plan(step(clock=self.clock)), pol=pol).status,
            DecisionStatus.AWAITING_APPROVAL,
        )

    def test_no_approval_plan_needs_no_determinism(self):
        self.seed_grant(direct("g1", "p1"))
        res = self.commit(self.auth, plan(step(expected_state=None, clock=None)))
        self.assertEqual(res.status, DecisionStatus.AUTHORIZED)

    def test_approval_requiring_requests_must_be_fully_determined(self):  # A-21
        self.seed_grant(direct("g1", "p1", conditions=[ApprovalRequired()]))
        res = self.commit(self.auth, plan(step(expected_state=None, clock=self.clock)))
        self.assertEqual(res.reason, "approval_request_not_fully_determined")
        res = self.commit(self.auth, plan(step(clock=None), plan_ref="p2"))
        self.assertEqual(res.reason, "approval_request_not_fully_determined")


class ExpiryAndPlanAgeTests(CoreTestCase):
    def setUp(self):
        super().setUp()
        self.seed_principal("p1", "alice")
        self.auth = verified("alice", self.clock)

    def expires(self, res):
        return self.store.decision(res.authorization_ref)["expires_at"]

    def test_configured_maximum(self):
        self.seed_grant(direct("g1", "p1"))
        res = self.commit(self.auth, plan(step(clock=self.clock)))
        self.assertEqual(
            self.expires(res), (self.clock.now + timedelta(seconds=3600)).isoformat()
        )

    def test_earliest_valid_until_among_matched_grants(self):
        soon = self.clock.now + timedelta(seconds=100)
        self.seed_grant(direct("g1", "p1"))
        self.seed_grant(direct("g2", "p1", valid_until=soon))
        res = self.commit(self.auth, plan(step(clock=self.clock)))
        self.assertEqual(self.expires(res), soon.isoformat())

    def test_plan_max_age_condition(self):
        self.seed_grant(direct("g1", "p1", conditions=[PlanMaxAge(300)]))
        obs = self.clock.now - timedelta(seconds=100)
        res = self.commit(self.auth, plan(step(clock=self.clock), observed_at=obs))
        self.assertEqual(self.expires(res), (obs + timedelta(seconds=300)).isoformat())
        stale = plan(
            step(clock=self.clock),
            plan_ref="p2",
            observed_at=self.clock.now - timedelta(seconds=301),
        )
        self.assertEqual(self.commit(self.auth, stale).reason, "plan_not_covered")
        missing = plan(step(clock=self.clock), plan_ref="p3")
        self.assertEqual(
            self.commit(self.auth, missing).reason, "plan_not_covered"
        )  # A-13

    def test_plan_max_age_not_evaluated_at_intent(self):
        self.seed_grant(direct("g1", "p1", conditions=[PlanMaxAge(300)]))
        res = self.intent(self.auth)
        self.assertEqual(res.outcome, Outcome.OK)
        cond = [
            c
            for c in self.audit("A1")[0]["conditions"]
            if c["condition"]["type"] == "PLAN_MAX_AGE"
        ]
        self.assertEqual(cond[0]["value"], "not_applicable")

    def test_policy_plan_max_age(self):
        self.seed_grant(direct("g1", "p1"))
        pol = PolicyInputs(
            baseline(plan_max_age_seconds=600), LocalSettings(revision=1)
        )
        stale = plan(
            step(clock=self.clock), observed_at=self.clock.now - timedelta(seconds=601)
        )
        self.assertEqual(self.commit(self.auth, stale, pol=pol).reason, "plan_max_age")
        self.assertEqual(
            self.commit(
                self.auth, plan(step(clock=self.clock), plan_ref="p2"), pol=pol
            ).reason,
            "plan_max_age",
        )

    def test_no_plan_max_age_source_means_no_default(self):
        self.seed_grant(direct("g1", "p1"))
        res = self.commit(
            self.auth,
            plan(
                step(clock=self.clock), observed_at=self.clock.now - timedelta(days=30)
            ),
        )
        self.assertEqual(res.outcome, Outcome.OK)
        self.assertEqual(
            self.expires(res), (self.clock.now + timedelta(seconds=3600)).isoformat()
        )


class InvalidationTests(CoreTestCase):
    def setUp(self):
        super().setUp()
        self.seed_principal("p1", "alice", roles=("scc.operator",))
        self.auth = verified("alice", self.clock)

    def test_plan_change_invalidates_old_decision_atomically_with_a2(self):
        first = self.commit(self.auth, plan(step(clock=self.clock)))
        changed = self.commit(
            self.auth, plan(step(clock=self.clock, params={"ip": "192.0.2.1"}))
        )
        self.assertEqual(changed.outcome, Outcome.OK)
        self.assertEqual(
            self.store.statuses(first.authorization_ref),
            [DecisionStatus.AUTHORIZED, DecisionStatus.INVALIDATED],
        )
        self.assertEqual(
            self.store.statuses(changed.authorization_ref), [DecisionStatus.AUTHORIZED]
        )

    def test_denied_change_still_invalidates(self):
        first = self.commit(self.auth, plan(step(clock=self.clock)))
        denied = self.commit(
            verified("alice", self.clock, age=5000),
            plan(step(clock=self.clock, params={"ip": "x"})),
        )
        self.assertEqual(denied.reason, "reauth_required")
        self.assertEqual(
            self.store.latest_status(first.authorization_ref),
            DecisionStatus.INVALIDATED,
        )

    def test_invalidated_decision_is_not_reinvalidated(self):
        first = self.commit(self.auth, plan(step(clock=self.clock)))
        self.commit(self.auth, plan(step(clock=self.clock, params={"ip": "a"})))
        self.commit(self.auth, plan(step(clock=self.clock, params={"ip": "b"})))
        self.assertEqual(
            self.store.statuses(first.authorization_ref).count(
                DecisionStatus.INVALIDATED
            ),
            1,
        )


if __name__ == "__main__":
    unittest.main()
