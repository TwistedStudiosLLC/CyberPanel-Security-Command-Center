"""§17.22 Phase I (steps 1–4): authentication boundary, binding, platform role, capability, targets, admissibility,
Grant matching, risk tier."""

import unittest
from datetime import timedelta

from k4core.core import Outcome
from k4core.inputs import AdmissibilityFacts, AdmissibilityInput, AuthenticationFailure
from k4core.model import (
    AuthFresh,
    BindingStatus,
    CapCategory,
    CapExact,
    CapIntegration,
    Grant,
    Permission,
    PlatformRole,
    PrincipalState,
    RecordState,
    TargetCategory,
    TargetManagementIn,
    TargetSystem,
    Tier,
)
from k4core.policy import LocalSettings, PolicyInputs

from .support import CoreTestCase, admissible, baseline, policy, request, verified


def direct(
    gid, pid, sel, tsel, tier=Tier.R4, perm=Permission.REQUEST, conditions=(), **kw
):
    return Grant(gid, "principal", pid, perm, sel, tsel, tier, tuple(conditions), **kw)


class AuthenticationTests(CoreTestCase):
    def test_valid_context_confirms_binding_and_records_role(self):
        self.seed_principal(
            "p1",
            "alice",
            status=BindingStatus.UNCONFIRMED,
            role=None,
            roles=("scc.operator",),
        )
        res = self.intent(verified("alice", self.clock))
        self.assertEqual(res.outcome, Outcome.OK, res)
        b = self.store.binding_of("p1")
        self.assertEqual(b.status, BindingStatus.CONFIRMED)  # DEC-089 Q1
        self.assertEqual(b.latest_confirmed_role, "PLATFORM_ADMIN")

    def test_assertion_failure_is_b2_not_a1(self):
        res = self.intent(
            AuthenticationFailure("signature", claimed_assertion_id="claimed-1")
        )
        self.assertEqual(res.outcome, Outcome.UNAUTHENTICATED)
        b2 = self.audit("B2")
        self.assertEqual(len(b2), 1)
        self.assertEqual(b2[0]["failure_reason"], "signature")
        self.assertEqual(
            b2[0]["claimed_assertion_id"], {"value": "claimed-1", "verified": False}
        )
        self.assertNotIn("principal_id", b2[0])
        self.assertEqual(self.audit("A1"), [])

    def test_each_assertion_check_is_a_failure_reason(self):
        for check in ("signature", "audience", "freshness", "single_use"):
            self.intent(AuthenticationFailure(check))
        self.assertEqual(
            [r["failure_reason"] for r in self.audit("B2")],
            ["signature", "audience", "freshness", "single_use"],
        )

    def test_failure_result_cannot_invent_a_check(self):
        with self.assertRaises(ValueError):
            AuthenticationFailure("password_wrong")

    def test_unenrolled_identity_has_no_authority(self):  # A-03
        res = self.intent(verified("mallory", self.clock))
        self.assertEqual(res.outcome, Outcome.UNAUTHENTICATED)
        self.assertEqual(self.audit("B2")[0]["failure_reason"], "binding")
        self.assertNotIn("principal_id", self.audit("B2")[0])

    def test_lost_binding_denied(self):
        self.seed_principal(
            "p1", "alice", status=BindingStatus.LOST, roles=("scc.operator",)
        )
        res = self.intent(verified("alice", self.clock))
        self.assertEqual(res.outcome, Outcome.UNAUTHENTICATED)
        rec = self.audit("B2")[0]
        self.assertEqual(rec["failure_reason"], "binding")
        self.assertEqual(
            rec["principal_id"], "p1"
        )  # resolved Principal of a verified assertion (§21.14)

    def test_non_active_principal_denied(self):
        for i, state in enumerate(
            (PrincipalState.SUSPENDED, PrincipalState.DISABLED, PrincipalState.REVOKED)
        ):
            self.seed_principal(
                f"p{i}", f"user{i}", state=state, roles=("scc.operator",)
            )
            res = self.intent(verified(f"user{i}", self.clock))
            self.assertEqual(res.outcome, Outcome.UNAUTHENTICATED, state)
        self.assertEqual(
            {r["failure_reason"] for r in self.audit("B2")}, {"principal_state"}
        )
        # No confirmation is written for a failed step 1.
        self.assertEqual(self.store.binding_of("p0").status, BindingStatus.CONFIRMED)

    def test_platform_admin_is_implicit_condition_and_denial_is_authorization(self):
        self.seed_principal("p1", "alice", roles=("scc.operator",))
        res = self.intent(verified("alice", self.clock, role="PLATFORM_USER"))
        self.assertEqual(res.outcome, Outcome.FORBIDDEN)
        self.assertEqual(res.reason, "no_matching_grant")
        self.assertEqual(self.audit("B2"), [])  # DEC-089 Q1: not B2
        a1 = self.audit("A1")[0]
        implicit = [c for c in a1["conditions"] if c["implicit"]]
        self.assertTrue(implicit and all(c["value"] is False for c in implicit))
        self.assertEqual(
            self.store.binding_of("p1").latest_confirmed_role, "PLATFORM_USER"
        )

    def test_missing_role_fact_counts_false(self):
        self.seed_principal("p1", "alice", roles=("scc.operator",))
        self.assertEqual(
            self.intent(verified("alice", self.clock, role=None)).outcome,
            Outcome.FORBIDDEN,
        )

    def test_other_platform_role_condition_cannot_be_evaluated_in_v1(self):
        self.seed_principal("p1", "alice")
        self.seed_grant(
            direct(
                "g1",
                "p1",
                CapExact("fail2ban", "ban"),
                TargetSystem("S1"),
                conditions=[PlatformRole("PLATFORM_RESELLER")],
            )
        )
        self.assertEqual(
            self.intent(verified("alice", self.clock)).outcome, Outcome.FORBIDDEN
        )


class StepOrderingTests(CoreTestCase):
    def setUp(self):
        super().setUp()
        self.seed_principal("p1", "alice", roles=("scc.operator",))

    def test_trace_follows_locked_sequence(self):
        res = self.intent(verified("alice", self.clock))
        self.assertEqual(
            res.trace[:4],
            [
                "step1:authenticate",
                "step1:authenticated",
                "step2:identify",
                "step3:admissibility",
            ],
        )
        self.assertIn("step4:intent_authorization", res.trace)

    def test_inadmissible_stops_before_authorization(self):
        res = self.intent(verified("alice", self.clock), adm=admissible(holds=False))
        self.assertEqual(res.outcome, Outcome.INADMISSIBLE)
        self.assertNotIn("step4:intent_authorization", res.trace)
        a1 = self.audit("A1")[0]
        self.assertEqual(a1["decision"], "inadmissible")
        self.assertEqual(a1["admissibility_result"][0]["result"], "inadmissible")
        self.assertNotIn("conditions", a1)  # authorization was not evaluated (A-09)

    def test_admissibility_recorded_separately_from_authorization(self):
        res = self.intent(verified("alice", self.clock))
        a1 = self.audit("A1")[0]
        self.assertEqual(res.outcome, Outcome.OK)
        self.assertEqual(a1["admissibility_result"][0]["result"], "admissible")
        self.assertEqual(a1["decision"], "permitted")


class CapabilityTests(CoreTestCase):
    def setUp(self):
        super().setUp()
        self.seed_principal("p1", "alice", roles=("scc.operator",))
        self.auth = verified("alice", self.clock)

    def test_valid_capability(self):
        self.assertEqual(self.intent(self.auth).outcome, Outcome.OK)

    def test_unknown_capability_refused(self):
        res = self.intent(self.auth, req=request("does-not-exist"))
        self.assertEqual(
            (res.outcome, res.reason), (Outcome.FORBIDDEN, "capability_not_identified")
        )
        self.assertEqual(self.audit("A1")[0]["decision"], "denied")

    def test_each_admissibility_fact_is_required(self):
        for i, field in enumerate(
            (
                "integration_valid",
                "capability_available",
                "compatibility_permits",
                "management_permits",
            )
        ):
            values = {
                f: True
                for f in (
                    "integration_valid",
                    "capability_available",
                    "compatibility_permits",
                    "management_permits",
                )
            }
            values[field] = False
            adm = AdmissibilityInput(
                {("fail2ban/ban", "system:S1"): AdmissibilityFacts(**values)}
            )
            self.assertEqual(
                self.intent(self.auth, adm=adm).outcome, Outcome.INADMISSIBLE, field
            )

    def test_missing_admissibility_facts_refused(self):
        self.assertEqual(
            self.intent(self.auth, adm=AdmissibilityInput({})).outcome,
            Outcome.INADMISSIBLE,
        )

    def test_tier_derived_from_k11_cannot_be_lowered(self):
        # 'install' is declared R2 but uses a package-family WRITE scope entry (criterion b) → R4.
        res = self.intent(self.auth, req=request("install"))
        self.assertEqual(res.effective_tier, Tier.R4)
        # 'jailcfg' uses an executable_semantics WRITE entry (criterion a) → R4.
        self.assertEqual(
            self.intent(self.auth, req=request("jailcfg")).effective_tier, Tier.R4
        )

    def test_local_policy_raises_but_never_lowers(self):
        pol = PolicyInputs(
            baseline(), LocalSettings(revision=4, tier_raises={"fail2ban/ban": Tier.R3})
        )
        res = self.intent(self.auth, pol=pol)
        self.assertEqual(res.effective_tier, Tier.R3)
        self.assertEqual(res.outcome, Outcome.FORBIDDEN)  # operator max_tier R2
        pol = PolicyInputs(
            baseline(),
            LocalSettings(revision=4, tier_raises={"fail2ban/install": Tier.R1}),
        )
        self.assertEqual(
            self.intent(self.auth, req=request("install"), pol=pol).effective_tier,
            Tier.R4,
        )

    def test_r4_denied_when_anchors_not_established(self):
        self.seed_principal("p2", "root-admin", roles=("scc.administrator",))
        auth = verified("root-admin", self.clock)
        res = self.intent(auth, req=request("install"))
        self.assertEqual(res.reason, "k11_anchors_unestablished")
        anchors = self.establish(("p2", "anc-1"))
        self.assertEqual(
            self.intent(auth, req=request("install"), anchors=anchors).outcome,
            Outcome.OK,
        )

    def test_grant_cannot_widen_k11_scope_selectors(self):
        self.seed_principal("p3", "carol")
        self.seed_grant(
            direct(
                "g-int-read",
                "p3",
                CapIntegration("fail2ban", "read"),
                TargetSystem("S1"),
            )
        )
        auth = verified("carol", self.clock)
        self.assertEqual(
            self.intent(auth, req=request("ban")).outcome, Outcome.FORBIDDEN
        )  # write capability
        self.assertEqual(self.intent(auth, req=request("status")).outcome, Outcome.OK)


class TargetTests(CoreTestCase):
    def setUp(self):
        super().setUp()
        self.seed_principal("p1", "alice")
        self.auth = verified("alice", self.clock)

    def test_valid_target_resolution(self):
        self.seed_grant(
            direct("g1", "p1", CapExact("fail2ban", "ban"), TargetSystem("S1"))
        )
        self.assertEqual(self.intent(self.auth).outcome, Outcome.OK)

    def test_missing_target(self):
        self.seed_grant(
            direct("g1", "p1", CapExact("fail2ban", "ban"), TargetSystem("S1"))
        )
        res = self.intent(self.auth, req=request(targets=("sys-404",)))
        self.assertEqual(res.reason, "target_not_resolved")

    def test_scc_target_invalid_for_integration_capability(self):
        self.seed_grant(
            direct("g1", "p1", CapExact("fail2ban", "ban"), TargetSystem("S1"))
        )
        self.assertEqual(
            self.intent(self.auth, req=request(targets=("scc",))).reason,
            "target_not_resolved",
        )

    def test_target_outside_grant(self):
        self.seed_grant(
            direct("g1", "p1", CapExact("fail2ban", "ban"), TargetSystem("S1"))
        )
        res = self.intent(self.auth, req=request(targets=("sys-1", "sys-2")))
        self.assertEqual(
            (res.outcome, res.reason), (Outcome.FORBIDDEN, "no_matching_grant")
        )

    def test_re_detected_target_stops_matching(self):  # §17.6
        self.seed_grant(
            direct("g1", "p1", CapExact("fail2ban", "ban"), TargetSystem("S1"))
        )
        from k4core.inputs import InventoryResolution, ResolvedTarget

        inv = InventoryResolution(
            {"sys-1": ResolvedTarget("system", "S1-new", None, "intrusion", "MANAGED")}
        )
        adm = admissible(("fail2ban/ban", "system:S1-new"))
        self.assertEqual(
            self.intent(self.auth, inv=inv, adm=adm).outcome, Outcome.FORBIDDEN
        )

    def test_category_and_management_conditions(self):
        self.seed_grant(
            direct(
                "g1",
                "p1",
                CapCategory("intrusion", "write"),
                TargetCategory("intrusion"),
                conditions=[TargetManagementIn(frozenset({"MANAGED"}))],
            )
        )
        self.assertEqual(self.intent(self.auth).outcome, Outcome.OK)
        self.assertEqual(
            self.intent(self.auth, req=request(targets=("sys-2",))).outcome,
            Outcome.FORBIDDEN,
        )


class GrantSemanticsTests(CoreTestCase):
    def setUp(self):
        super().setUp()
        self.seed_principal("p1", "alice")
        self.auth = verified("alice", self.clock)

    def test_every_matching_grant_recorded(self):
        self.seed_grant(
            direct("g1", "p1", CapExact("fail2ban", "ban"), TargetSystem("S1"))
        )
        self.seed_grant(
            direct("g2", "p1", CapIntegration("fail2ban", "any"), TargetSystem("S1"))
        )
        res = self.intent(self.auth)
        self.assertEqual(res.matched_grants, ("g1", "g2"))
        self.assertEqual(self.audit("A1")[0]["authority_basis"]["grants"], ["g1", "g2"])

    def test_revoked_expired_or_wrong_permission_grant_does_not_match(self):
        self.seed_grant(
            direct(
                "g1",
                "p1",
                CapExact("fail2ban", "ban"),
                TargetSystem("S1"),
                state=RecordState.REVOKED,
            )
        )
        self.seed_grant(
            direct(
                "g2",
                "p1",
                CapExact("fail2ban", "ban"),
                TargetSystem("S1"),
                valid_until=self.clock.now - timedelta(seconds=1),
            )
        )
        self.seed_grant(
            direct(
                "g3",
                "p1",
                CapExact("fail2ban", "ban"),
                TargetSystem("S1"),
                perm=Permission.VIEW,
            )
        )
        self.seed_grant(
            direct(
                "g4",
                "p1",
                CapExact("fail2ban", "ban"),
                TargetSystem("S1"),
                tier=Tier.R1,
            )
        )
        self.assertEqual(self.intent(self.auth).outcome, Outcome.FORBIDDEN)

    def test_role_membership_must_be_active_and_valid(self):
        self.seed_membership("p1", "scc.operator", state=RecordState.REVOKED)
        self.assertEqual(self.intent(self.auth).outcome, Outcome.FORBIDDEN)

    def test_auth_fresh_condition(self):
        self.seed_grant(
            direct(
                "g1",
                "p1",
                CapExact("fail2ban", "ban"),
                TargetSystem("S1"),
                conditions=[AuthFresh(60)],
            )
        )
        self.assertEqual(
            self.intent(verified("alice", self.clock, age=30)).outcome, Outcome.OK
        )
        self.assertEqual(
            self.intent(verified("alice", self.clock, age=61)).outcome,
            Outcome.FORBIDDEN,
        )

    def test_r0_view_not_recorded_r1_view_recorded(self):  # §17.18; §21.16
        self.seed_membership("p1", "scc.operator")
        self.intent(self.auth, req=request("status", permission=Permission.VIEW))
        self.assertEqual(self.audit("A1"), [])
        self.intent(self.auth, req=request("logs", permission=Permission.VIEW))
        self.assertEqual(len(self.audit("A1")), 1)


class PolicyTests(CoreTestCase):
    def setUp(self):
        super().setUp()
        self.seed_principal("p1", "alice", roles=("scc.operator",))
        self.auth = verified("alice", self.clock)

    def test_unreadable_local_revision_denied(self):  # §17.16; Q3 as adopted
        res = self.intent(self.auth, pol=PolicyInputs(baseline(), None))
        self.assertEqual(
            (res.outcome, res.reason), (Outcome.FORBIDDEN, "policy_unavailable")
        )
        self.assertEqual(self.audit("A1")[0]["reason_code"], "policy_unavailable")

    def test_unreadable_baseline_denied(self):
        self.assertEqual(
            self.intent(self.auth, pol=PolicyInputs(None, LocalSettings(1))).reason,
            "policy_unavailable",
        )

    def test_invalid_local_revision_denied(self):
        bad = LocalSettings(
            revision=2, reauth_max_age_seconds={Tier.R2: 99999}
        )  # cannot lengthen
        self.assertEqual(
            self.intent(self.auth, pol=PolicyInputs(baseline(), bad)).reason,
            "policy_unavailable",
        )
        bad = LocalSettings(revision=2, approval_required_tiers=frozenset({Tier.R4}))
        self.assertEqual(
            self.intent(self.auth, pol=PolicyInputs(baseline(), bad)).reason,
            "policy_unavailable",
        )

    def test_revisions_recorded(self):
        self.intent(self.auth, pol=policy())
        self.assertEqual(
            self.audit("A1")[0]["policy_revisions"],
            {
                "policy_id": "scc-release-baseline",
                "baseline_revision": 7,
                "local_revision": 3,
            },
        )

    def test_k4_does_not_write_dc08(self):
        self.intent(self.auth)
        import sqlite3

        conn = sqlite3.connect(self.path)
        tables = {
            r[0]
            for r in conn.execute("SELECT name FROM sqlite_master WHERE type='table'")
        }
        conn.close()
        self.assertFalse(any("polic" in t or "setting" in t for t in tables))


if __name__ == "__main__":
    unittest.main()
