"""§17.22 step 10: approvals over the abstract verification result (DEC-089 D89-3, Q6), §17.8 approver
requirements, anchor naming (§17.9; A-20), separation of duties, D89-22."""

import unittest

from k4core.core import Outcome
from k4core.inputs import ApprovalVerificationResult
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
from k4core.policy import LocalSettings, PolicyInputs

from .support import CoreTestCase, baseline, plan, request, step, verified


class ApprovalTests(CoreTestCase):
    def setUp(self):
        super().setUp()
        self.seed_principal("req", "requester", roles=("scc.administrator",))
        self.seed_principal("apr", "approver", roles=("scc.approver",))
        self.anchors = self.establish(("apr", "anc-apr"), ("req", "anc-req"))
        p = plan(
            step(
                "s1",
                capability_id="install",
                op="package.install",
                resources=("pkg:fail2ban",),
                clock=self.clock,
            ),
            step("s2", clock=self.clock),
        )
        res = self.commit(
            verified("requester", self.clock),
            p,
            req=request("install"),
            anchors=self.anchors,
        )
        assert res.status is DecisionStatus.AWAITING_APPROVAL, res
        self.ref = res.authorization_ref

    def evidence(
        self,
        step_id="s1",
        anchor="anc-apr",
        sig=True,
        digest=True,
        ref=None,
        evidence_ref=None,
    ):
        return ApprovalVerificationResult(
            evidence_ref or f"ev-{step_id}-{anchor}",
            ref or self.ref,
            step_id,
            sig,
            digest,
            anchor,
        )

    def submit(self, ev, anchors="default", pol=None):
        return self.core.submit_approval(
            ev,
            self.decls,
            self.inv,
            pol or self.pol,
            self.anchors if anchors == "default" else anchors,
        )

    def test_every_request_needs_approval_and_authorized_when_all_present(
        self,
    ):  # D89-22
        self.assertEqual(self.store.decision(self.ref)["approval_steps"], ["s1", "s2"])
        r1 = self.submit(self.evidence("s1"))
        self.assertEqual(
            (r1.outcome, r1.status), (Outcome.OK, DecisionStatus.AWAITING_APPROVAL)
        )
        r2 = self.submit(self.evidence("s2"))
        self.assertEqual(
            (r2.outcome, r2.status), (Outcome.OK, DecisionStatus.AUTHORIZED)
        )
        self.assertEqual(
            self.store.statuses(self.ref),
            [DecisionStatus.AWAITING_APPROVAL, DecisionStatus.AUTHORIZED],
        )
        a4 = self.audit("A4")
        self.assertEqual([r["decision"] for r in a4], ["accepted", "accepted"])
        self.assertEqual(a4[0]["principal_id"], "apr")

    def test_signature_failure_rejected(self):
        res = self.submit(self.evidence(sig=False))
        self.assertEqual(
            (res.outcome, res.reason),
            (Outcome.FORBIDDEN, "signature_not_verified_against_anchor"),
        )
        self.assertEqual(self.audit("A4")[0]["decision"], "rejected")
        self.assertNotIn(
            "principal_id", self.audit("A4")[0]
        )  # no attribution without verification
        self.assertEqual(self.store.approved_steps(self.ref), set())

    def test_digest_mismatch_rejected(self):
        self.assertEqual(
            self.submit(self.evidence(digest=False)).reason, "digest_mismatch"
        )

    def test_unknown_anchor_rejected(self):
        self.assertEqual(
            self.submit(self.evidence(anchor="anc-unknown")).reason,
            "signature_not_verified_against_anchor",
        )

    def test_anchor_without_approve_grant_rejected(
        self,
    ):  # A-20: anchor alone does not suffice
        self.seed_principal("x", "xavier")
        anchors = self.establish(("x", "anc-x"))
        res = self.submit(self.evidence(anchor="anc-x"), anchors=anchors)
        self.assertEqual(res.reason, "approver_lacks_approve_grant")

    def test_approve_grant_without_anchor_rejected(
        self,
    ):  # A-20: Grant alone does not suffice
        self.seed_principal("y", "yolanda", roles=("scc.approver",))
        self.assertEqual(
            self.submit(self.evidence(anchor="anc-y")).reason,
            "signature_not_verified_against_anchor",
        )

    def test_approver_must_be_active(self):
        self.seed_principal(
            "s", "sam", state=PrincipalState.SUSPENDED, roles=("scc.approver",)
        )
        anchors = self.establish(("s", "anc-s"))
        self.assertEqual(
            self.submit(self.evidence(anchor="anc-s"), anchors=anchors).reason,
            "approver_not_active",
        )

    def test_approver_binding_must_be_confirmed(self):
        self.seed_principal(
            "u", "uma", status=BindingStatus.UNCONFIRMED, roles=("scc.approver",)
        )
        anchors = self.establish(("u", "anc-u"))
        self.assertEqual(
            self.submit(self.evidence(anchor="anc-u"), anchors=anchors).reason,
            "approver_binding_not_confirmed",
        )

    def test_approver_platform_admin_implicit(self):
        self.seed_principal("v", "vic", role="PLATFORM_USER", roles=("scc.approver",))
        anchors = self.establish(("v", "anc-v"))
        self.assertEqual(
            self.submit(self.evidence(anchor="anc-v"), anchors=anchors).reason,
            "approver_lacks_approve_grant",
        )

    def test_approve_grant_tier_must_cover(self):
        self.seed_principal("w", "wes")
        self.seed_grant(
            Grant(
                "gw",
                "principal",
                "w",
                Permission.APPROVE,
                CapExact("fail2ban", "install"),
                TargetSystem("S1"),
                Tier.R3,
            )
        )
        anchors = self.establish(("w", "anc-w"))
        self.assertEqual(
            self.submit(self.evidence(anchor="anc-w"), anchors=anchors).reason,
            "approver_lacks_approve_grant",
        )

    def test_self_approval_permitted_by_default(self):
        self.seed_membership("req", "scc.approver")
        self.assertEqual(
            self.submit(self.evidence(anchor="anc-req")).outcome, Outcome.OK
        )

    def test_separation_of_duties_when_enabled(self):
        self.seed_membership("req", "scc.approver")
        pol = PolicyInputs(
            baseline(),
            LocalSettings(revision=9, separation_of_duties_tiers=frozenset({Tier.R4})),
        )
        self.assertEqual(
            self.submit(self.evidence(anchor="anc-req"), pol=pol).reason,
            "separation_of_duties",
        )
        self.assertEqual(
            self.submit(self.evidence(anchor="anc-apr"), pol=pol).outcome, Outcome.OK
        )

    def test_anchors_not_established_refused(self):
        self.assertEqual(
            self.submit(self.evidence(), anchors=None).reason,
            "k11_anchors_unestablished",
        )

    def test_duplicate_and_unknown_requests_rejected(self):
        self.submit(self.evidence("s1"))
        self.assertEqual(
            self.submit(self.evidence("s1", evidence_ref="again")).reason,
            "request_already_approved",
        )
        self.assertEqual(
            self.submit(self.evidence("s9")).reason, "request_not_approval_requiring"
        )
        self.assertEqual(
            self.submit(self.evidence(ref="nope")).reason, "decision_unknown"
        )

    def test_authorized_decision_accepts_no_further_approval(self):
        self.submit(self.evidence("s1"))
        self.submit(self.evidence("s2"))
        self.assertEqual(
            self.submit(self.evidence("s1", evidence_ref="late")).reason,
            "decision_not_awaiting_approval",
        )

    def test_a4_carries_references_not_evidence_content(self):
        self.submit(self.evidence("s1"))
        a4 = self.audit("A4")[0]
        self.assertEqual(a4["approval_refs"][0]["evidence_ref"], "ev-s1-anc-apr")
        self.assertEqual(a4["authorization_ref"], self.ref)
        self.assertNotIn("policy_revisions", a4)


if __name__ == "__main__":
    unittest.main()
