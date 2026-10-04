"""K4 side of the §22 bootstrap act (DEC-089 D89-15; DEC-086)."""

import sqlite3
import unittest

from k4core.core import Outcome
from k4core.inputs import RootDetermination
from k4core.model import BindingStatus, PrincipalState, RecordState

from .support import (
    ADAPTER,
    INSTANCE,
    CoreTestCase,
    FaultyStore,
    plan,
    request,
    step,
    verified,
)

ROOT = RootDetermination(True, "peer-root-ref-1")
P11 = {
    "platform_adapter_id": ADAPTER,
    "platform_instance_id": INSTANCE,
    "platform_subject_id": "admin",
}


class BootstrapTests(CoreTestCase):
    def test_first_bootstrap_creates_principal_membership_and_two_a6(self):
        res = self.core.bootstrap(dict(P11), ROOT)
        self.assertEqual(res.outcome, Outcome.OK, res)
        pid = res.principal_id
        self.assertEqual(self.store.principal(pid).state, PrincipalState.ACTIVE)
        b = self.store.binding_of(pid)
        self.assertEqual(b.status, BindingStatus.UNCONFIRMED)
        m = self.store.memberships_of(pid)
        self.assertEqual(
            [(x.role_id, x.state, x.valid_until) for x in m],
            [("scc.administrator", RecordState.ACTIVE, None)],
        )
        self.assertEqual(self.store.direct_grants_of(pid), [])  # no Grants
        a6 = self.audit("A6")
        self.assertEqual(len(a6), 2)  # one per bootstrap mutation (§22.7.2)
        for r in a6:
            self.assertEqual(r["actor_type"], "Local Root Operator")
            self.assertEqual(
                r["authority_basis"], "Local Root Operator bootstrap authority (A-07)"
            )
            self.assertEqual(r["lro_auth_ref"], "peer-root-ref-1")
            self.assertNotIn("principal_id", r)  # not set for the Actor (§22.7.1)
            self.assertIn(f"principal:{pid}", r["targets"])

    def test_non_root_rejected(self):
        res = self.core.bootstrap(dict(P11), RootDetermination(False, "peer-1000"))
        self.assertEqual(res.reason, "caller_not_root")
        self.assertEqual(self.audit(), [])

    def test_malformed_p11_rejected(self):
        for bad in (
            {},
            {**P11, "role": "scc.administrator"},
            {**P11, "platform_subject_id": ""},
            "admin",
            {**P11, "platform_instance_id": 5},
        ):
            self.assertEqual(
                self.core.bootstrap(bad, ROOT).outcome, Outcome.MALFORMED, bad
            )
        self.assertFalse(self.store.any_administrator_membership_record())

    def test_root_determination_is_not_p11_content(self):
        res = self.core.bootstrap(
            {**P11, "caller_is_root": True}, RootDetermination(False, "x")
        )
        self.assertEqual(res.reason, "caller_not_root")

    def test_replay_rejected(self):
        self.assertEqual(self.core.bootstrap(dict(P11), ROOT).outcome, Outcome.OK)
        again = self.core.bootstrap({**P11, "platform_subject_id": "second"}, ROOT)
        self.assertEqual(again.reason, "bootstrap_unavailable_administrator_exists")
        self.assertEqual(len(self.audit("A6")), 2)

    def test_refused_while_any_administrator_record_exists_in_any_state(self):
        self.seed_principal("old", "old-admin")
        self.seed_membership("old", "scc.administrator", state=RecordState.REVOKED)
        self.assertEqual(
            self.core.bootstrap(dict(P11), ROOT).reason,
            "bootstrap_unavailable_administrator_exists",
        )

    def test_grants_nothing_else_and_admin_acts_only_after_verified_assertion(self):
        res = self.core.bootstrap(dict(P11), ROOT)
        conn = sqlite3.connect(self.path)
        self.assertEqual(conn.execute("SELECT COUNT(*) FROM grants").fetchone()[0], 0)
        self.assertEqual(
            conn.execute("SELECT COUNT(*) FROM role_memberships").fetchone()[0], 1
        )
        conn.close()
        # Without PLATFORM_ADMIN the bootstrapped Principal still cannot act (§22.4.2; A-04).
        denied = self.intent(verified("admin", self.clock, role="PLATFORM_USER"))
        self.assertEqual(denied.outcome, Outcome.FORBIDDEN)
        ok = self.intent(verified("admin", self.clock))
        self.assertEqual((ok.outcome, ok.principal_id), (Outcome.OK, res.principal_id))
        self.assertEqual(
            self.store.binding_of(res.principal_id).status, BindingStatus.CONFIRMED
        )


class BootstrapAtomicityTests(CoreTestCase):
    store_class = FaultyStore

    def test_nothing_committed_if_any_a6_fails(self):  # §22.4.4; R4a
        self.store.fail_audit = True
        res = self.core.bootstrap(dict(P11), ROOT)
        self.assertEqual(res.outcome, Outcome.UNAVAILABLE)
        self.assertFalse(self.store.any_administrator_membership_record())
        conn = sqlite3.connect(self.path)
        self.assertEqual(
            conn.execute("SELECT COUNT(*) FROM principals").fetchone()[0], 0
        )
        conn.close()
        self.store.fail_audit = False
        self.assertEqual(self.core.bootstrap(dict(P11), ROOT).outcome, Outcome.OK)


class NoAdministrationPathTests(CoreTestCase):
    def test_store_exposes_no_administration_mutation(self):
        from k4core.store import Transaction

        names = {n for n in dir(Transaction) if not n.startswith("_")}
        self.assertEqual(
            names,
            {
                "append_audit",
                "record_binding_confirmation",
                "create_bootstrap_principal",
                "store_plan",
                "create_decision",
                "append_status",
                "record_approval",
            },
        )

    def test_scc_request_evaluated_but_not_applied(self):
        res = self.core.bootstrap(dict(P11), ROOT)
        anchors = self.establish((res.principal_id, "anc-admin"))
        before = sqlite3.connect(self.path)
        counts = [
            before.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]
            for t in ("principals", "grants", "role_memberships")
        ]
        before.close()
        out = self.intent(
            verified("admin", self.clock),
            req=request("scc.enroll", targets=("scc",)),
            anchors=anchors,
        )
        self.assertEqual(out.outcome, Outcome.OK)
        after = sqlite3.connect(self.path)
        self.assertEqual(
            counts,
            [
                after.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]
                for t in ("principals", "grants", "role_memberships")
            ],
        )
        after.close()

    def test_status_writes_limited_to_slice(self):
        from k4core.model import DecisionStatus

        self.core.bootstrap(dict(P11), ROOT)
        res = self.commit(
            verified("admin", self.clock), plan(step(clock=self.clock)), req=request()
        )
        self.assertEqual(res.outcome, Outcome.OK, res)
        with self.assertRaises(ValueError), self.store.transaction() as tx:
            tx.append_status(
                res.authorization_ref, DecisionStatus.CONSUMED, self.clock.now
            )


if __name__ == "__main__":
    unittest.main()
