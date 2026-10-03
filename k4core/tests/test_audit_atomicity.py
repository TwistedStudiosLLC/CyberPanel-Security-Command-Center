"""§21 audit infrastructure and failure behaviour: identity, sequence, timestamp vs recorded_at, required and
prohibited fields, durable recording, §21.12, B1, B3 reliance, R4a and R5a."""

import sqlite3
import unittest

from k4core import audit
from k4core.core import AnchorsNotEstablished, Outcome
from k4core.inputs import AnchorChange, AuthenticationFailure
from k4core.model import DecisionStatus
from k4core.store import K7Store, UnsupportedFormat

from .support import (
    CoreTestCase,
    FaultyStore,
    added,
    anchor_read,
    plan,
    request,
    step,
    verified,
)


class AuditInfrastructureTests(CoreTestCase):
    def setUp(self):
        super().setUp()
        self.seed_principal("p1", "alice", roles=("scc.operator",))

    def test_identity_unique_and_sequence_monotonic(self):
        for _ in range(5):
            self.intent(verified("alice", self.clock))
            self.intent(AuthenticationFailure("audience"))
        recs = self.audit()
        self.assertEqual(len({r["audit_id"] for r in recs}), len(recs))
        seqs = [r["audit_seq"] for r in recs]
        self.assertEqual(seqs, sorted(seqs))
        self.assertEqual(len(set(seqs)), len(seqs))

    def test_timestamp_and_recorded_at_are_distinct_fields(self):
        self.intent(verified("alice", self.clock))
        rec = self.audit("A1")[0]
        self.assertIn("timestamp", rec)
        self.assertIn("recorded_at", rec)

    def test_sequence_is_recording_order_not_event_order(self):
        # A B1 written later for an earlier unrecorded denial carries the earlier event time but a later position.
        faulty_path = self.path
        self.store.close()
        store = FaultyStore(faulty_path, self.clock)
        from k4core.core import K4Core

        core = K4Core(store, self.clock)
        store.fail_audit = True
        t_denial = self.clock.now
        core.evaluate_intent(
            request("nope"),
            verified("alice", self.clock),
            self.decls,
            self.inv,
            self.adm,
            self.pol,
            None,
        )
        store.fail_audit = False
        self.clock.advance(60)
        core.evaluate_intent(
            request(),
            verified("alice", self.clock),
            self.decls,
            self.inv,
            self.adm,
            self.pol,
            None,
        )
        recs = store.audit_records()
        b1 = next(r for r in recs if r["event_kind"] == "B1")
        a1 = [r for r in recs if r["event_kind"] == "A1"][-1]
        self.assertEqual(b1["timestamp"], t_denial.isoformat())
        self.assertLess(b1["audit_seq"], a1["audit_seq"])
        self.assertEqual(b1["recorded_at"], self.clock.now.isoformat())
        self.store = store

    def test_records_survive_reopen(self):  # durable recording (§21.11)
        self.intent(verified("alice", self.clock))
        self.store.close()
        self.store = K7Store(self.path, self.clock)
        self.assertEqual(len(self.audit("A1")), 1)

    def test_audit_is_append_only(self):
        self.intent(verified("alice", self.clock))
        conn = sqlite3.connect(self.path)
        with self.assertRaises(sqlite3.DatabaseError):
            conn.execute("UPDATE audit SET record='{}'")
        with self.assertRaises(sqlite3.DatabaseError):
            conn.execute("DELETE FROM audit")
        conn.close()

    def test_required_fields(self):
        self.intent(verified("alice", self.clock))
        self.intent(AuthenticationFailure("signature"))
        for rec in self.audit():
            missing = audit.REQUIRED[rec["event_kind"]] - set(rec)
            self.assertFalse(missing, rec)
            self.assertIn("audit_seq", rec)
            self.assertIn("recorded_at", rec)

    def test_contract_rejects_unlisted_or_forbidden_fields(self):
        t = self.clock.now
        with self.assertRaises(audit.AuditContractError):
            audit.draft("B2", t, failure_reason="signature", raw_assertion="eyJ...")
        with self.assertRaises(audit.AuditContractError):
            audit.draft(
                "B2", t, failure_reason="signature", claimed_assertion_id="not-marked"
            )
        with self.assertRaises(audit.AuditContractError):
            audit.draft(
                "B1", t, condition_kind="x", count=1, principal_id="p1"
            )  # denial B1 carries nothing else
        with self.assertRaises(audit.AuditContractError):
            audit.draft(
                "A1",
                t,
                actor_type="HUMAN",
                authority_basis={},
                decision="d",
                reason_code="r",
                capability="c",
                action="a",
                targets=[],
                job_id="j",
            )  # Job state out of slice
        for kind in ("A3", "A5", "A7", "B4"):
            with self.assertRaises(audit.AuditContractError):
                audit.draft(kind, t)

    def test_no_raw_credential_material_in_audit(self):
        self.intent(verified("alice", self.clock, assertion_id="asr-1"))
        self.intent(
            AuthenticationFailure("signature", claimed_assertion_id="claimed-2")
        )
        text = str(self.store.audit_records())
        self.assertNotIn("password", text)  # method claims are not recorded as content
        self.assertNotIn("alice", text)  # platform subject is not recorded
        self.assertNotIn("platform_subject", text)

    def test_unsupported_format_version_not_interpreted(self):  # S19-15
        self.store.close()
        conn = sqlite3.connect(self.path)
        with conn:
            conn.execute("UPDATE meta SET value='other/9' WHERE key='format_version'")
        conn.close()
        with self.assertRaises(UnsupportedFormat):
            K7Store(self.path, self.clock)
        self.store = K7Store.__new__(
            K7Store
        )  # tearDown closes this placeholder; the refused store closed itself
        self.store._conn = sqlite3.connect(":memory:")


class FailureBehaviourTests(CoreTestCase):
    store_class = FaultyStore

    def setUp(self):
        super().setUp()
        self.seed_principal("p1", "alice", roles=("scc.operator",))
        self.auth = verified("alice", self.clock)

    def test_r5a_permitted_intent_does_not_proceed_without_record(self):
        self.store.fail_audit = True
        res = self.intent(self.auth)
        self.assertEqual(
            (res.outcome, res.reason), (Outcome.UNAVAILABLE, "audit_unavailable")
        )

    def test_denial_remains_refusal_and_b1_written_later_with_count_only(self):
        self.store.fail_audit = True
        for _ in range(3):
            self.assertEqual(
                self.intent(self.auth, req=request("nope")).outcome, Outcome.FORBIDDEN
            )
        self.intent(
            AuthenticationFailure("signature")
        )  # B2 failure is a denial (§21.12)
        self.store.fail_audit = False
        self.intent(self.auth)
        b1 = self.audit("B1")
        self.assertEqual(len(b1), 1)
        self.assertEqual(b1[0]["count"], 4)
        self.assertEqual(
            set(b1[0]) - {"audit_seq", "recorded_at"},
            {
                "audit_id",
                "record_class",
                "event_kind",
                "timestamp",
                "condition_kind",
                "count",
            },
        )
        self.assertEqual(
            self.audit("A1")[0]["decision"], "permitted"
        )  # denials were not late-recorded
        self.assertEqual(self.audit("B2"), [])

    def test_r4a_decision_not_committed_without_a2(self):
        self.store.fail_audit_kinds = frozenset({"A2"})
        res = self.commit(self.auth, plan(step(clock=self.clock)))
        self.assertEqual(res.outcome, Outcome.UNAVAILABLE)
        self.assertEqual(self.store.decisions_for_plan("plan-1"), [])
        self.assertIsNone(self.store.plan_content("plan-1", res.plan_digest))

    def test_r4a_invalidation_not_committed_without_a2(self):
        first = self.commit(self.auth, plan(step(clock=self.clock)))
        self.store.fail_audit_kinds = frozenset({"A2"})
        self.commit(self.auth, plan(step(clock=self.clock, params={"ip": "changed"})))
        self.assertEqual(
            self.store.statuses(first.authorization_ref), [DecisionStatus.AUTHORIZED]
        )

    def test_k7_unavailable_denies(self):  # §17.16
        self.store.fail_reads = True
        res = self.intent(self.auth)
        self.assertNotEqual(res.outcome, Outcome.OK)


class AnchorObservationTests(CoreTestCase):
    store_class = FaultyStore

    def test_b3_per_change_with_locked_fields(self):
        self.core.observe_anchor_read(
            anchor_read(
                ("p1", "d1"),
                changes=[added("p1", "d1"), AnchorChange("p2", "d2", "revoked")],
            )
        )
        b3 = self.audit("B3")
        self.assertEqual([r["change_kind"] for r in b3], ["added", "revoked"])
        for r in b3:
            self.assertEqual(r["observer"], "observed by K4")
            self.assertEqual(
                set(r) - {"audit_seq", "recorded_at"},
                {
                    "audit_id",
                    "record_class",
                    "event_kind",
                    "timestamp",
                    "named_principal",
                    "anchor_digest",
                    "observed_at",
                    "change_kind",
                    "observer",
                },
            )

    def test_changed_set_not_relied_on_until_b3_durable(self):
        self.store.fail_audit = True
        with self.assertRaises(AnchorsNotEstablished):
            self.core.observe_anchor_read(
                anchor_read(("p1", "d1"), changes=[added("p1", "d1")])
            )
        self.assertEqual(self.audit("B3"), [])

    def test_unknown_change_kind_rejected(self):
        with self.assertRaises(ValueError):
            AnchorChange("p", "d", "legitimate")

    def test_anchors_from_another_core_not_accepted(self):
        from k4core.core import EstablishedAnchors

        forged = EstablishedAnchors(frozenset({("p1", "d1")}), object())
        self.assertFalse(self.core._anchors_ok(forged))


if __name__ == "__main__":
    unittest.main()
