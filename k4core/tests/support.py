"""Test fixtures. Abstract inputs here are external facts only; none encodes an authorization outcome.

K7 seeding writes rows directly because this slice has no Grant, Principal or Role Membership mutation path
(DEC-089 D89-10, D89-11). Seeding is test-only and is not reachable from k4core.
"""

from __future__ import annotations

import json
import sqlite3
import tempfile
import unittest
from datetime import datetime, timedelta, timezone

from k4core.core import K4Core
from k4core.inputs import (
    ActionRequest,
    AdmissibilityFacts,
    AdmissibilityInput,
    AnchorChange,
    AnchorEntry,
    CapabilityDeclaration,
    ExecutionDeclaration,
    InventoryResolution,
    K11AnchorRead,
    K11Declarations,
    PlanProposal,
    PlanStep,
    ResolvedTarget,
    ScopeEntry,
    VerifiedAuthentication,
)
from k4core.model import (
    PLATFORM_ADMIN,
    BindingStatus,
    CapabilityRef,
    CapAll,
    Grant,
    GrantSpec,
    Permission,
    PrincipalState,
    RecordState,
    TargetAny,
    TargetScc,
    Tier,
)
from k4core.policy import APPROVAL, REAUTH, LocalSettings, PolicyInputs, ReleaseBaseline
from k4core.serialization import encode_grant, to_iso
from k4core.store import K7Store

T0 = datetime(2026, 10, 3, 12, 0, 0, tzinfo=timezone.utc)
ADAPTER, INSTANCE = "cyberpanel", "host-1"
DECL_DIGEST = "decl-digest-1"


class FakeClock:
    def __init__(self, now: datetime = T0) -> None:
        self.now = now

    def __call__(self) -> datetime:
        return self.now

    def advance(self, seconds: int) -> None:
        self.now = self.now + timedelta(seconds=seconds)


class FaultyStore(K7Store):
    """K7 whose audit writes or reads can be made to fail, to exercise R4a, R5a and §21.12."""

    fail_audit = False
    fail_reads = False
    fail_audit_kinds: frozenset[str] = frozenset()

    def _insert_audit(self, cur, record):
        if self.fail_audit or record["event_kind"] in self.fail_audit_kinds:
            raise sqlite3.OperationalError("simulated durable-write failure")
        return super()._insert_audit(cur, record)

    def _query(self, sql, args=()):
        if self.fail_reads:
            from k4core.store import K7Unavailable

            raise K7Unavailable("simulated read failure")
        return super()._query(sql, args)


def baseline(**overrides) -> ReleaseBaseline:
    roles = {
        "scc.viewer": (
            GrantSpec(Permission.VIEW, CapAll("any"), TargetAny(), Tier.R0),
        ),
        "scc.operator": (
            GrantSpec(Permission.REQUEST, CapAll("any"), TargetAny(), Tier.R2),
            GrantSpec(Permission.VIEW, CapAll("any"), TargetAny(), Tier.R1),
        ),
        "scc.administrator": (
            GrantSpec(Permission.REQUEST, CapAll("any"), TargetAny(), Tier.R4),
            GrantSpec(Permission.VIEW, CapAll("any"), TargetAny(), Tier.R1),
        ),
        "scc.approver": (
            GrantSpec(Permission.APPROVE, CapAll("any"), TargetAny(), Tier.R4),
        ),
    }
    values = {
        "policy_id": "scc-release-baseline",
        "revision": 7,
        "role_grants": roles,
        "default_step_up": {
            Tier.R2: frozenset({REAUTH}),
            Tier.R3: frozenset({REAUTH}),
            Tier.R4: frozenset({REAUTH, APPROVAL}),
        },
        "reauth_max_age_seconds": {Tier.R2: 900, Tier.R3: 900, Tier.R4: 300},
        "decision_max_age_seconds": 3600,
        "plan_max_age_seconds": None,
    }
    values.update(overrides)
    return ReleaseBaseline(**values)


def policy(base=None, local=None) -> PolicyInputs:
    return PolicyInputs(base or baseline(), local or LocalSettings(revision=3))


def declarations() -> K11Declarations:
    caps = (
        CapabilityDeclaration("ban", "intrusion", "write", Tier.R2),
        CapabilityDeclaration("status", "intrusion", "read", Tier.R0),
        CapabilityDeclaration("logs", "intrusion", "read", Tier.R1),
        CapabilityDeclaration("jailcfg", "intrusion", "write", Tier.R3),
        CapabilityDeclaration("install", "intrusion", "write", Tier.R2),
    )
    entries = (
        ScopeEntry("ban", "service.control", 1, "write", frozenset({"svc:fail2ban"})),
        ScopeEntry("status", "service.status", 1, "read", frozenset({"svc:fail2ban"})),
        ScopeEntry("logs", "log.read", 1, "read", frozenset({"log:fail2ban"})),
        ScopeEntry(
            "jailcfg",
            "file.replace",
            1,
            "write",
            frozenset({"cfg:jail"}),
            executable_semantics=True,
            approval_required=True,
        ),
        ScopeEntry(
            "install",
            "package.install",
            1,
            "write",
            frozenset({"pkg:fail2ban"}),
            approval_required=True,
        ),
    )
    return K11Declarations(
        (ExecutionDeclaration("fail2ban", DECL_DIGEST, caps, entries),)
    )


def inventory() -> InventoryResolution:
    return InventoryResolution(
        {
            "sys-1": ResolvedTarget("system", "S1", None, "intrusion", "MANAGED"),
            "sys-2": ResolvedTarget("system", "S2", None, "intrusion", "OBSERVED"),
            "scc": ResolvedTarget("scc"),
        }
    )


def admissible(*pairs, holds=True) -> AdmissibilityInput:
    facts = AdmissibilityFacts(holds, holds, holds, holds)
    keys = pairs or [
        (f"fail2ban/{c}", t)
        for c in ("ban", "status", "logs", "jailcfg", "install")
        for t in ("system:S1", "system:S2")
    ] + [("scc.enroll", "scc")]
    return AdmissibilityInput({k: facts for k in keys})


def cap(capability_id: str) -> CapabilityRef:
    if capability_id.startswith("scc."):
        return CapabilityRef(None, capability_id)
    return CapabilityRef("fail2ban", capability_id)


def request(
    capability_id="ban",
    targets=("sys-1",),
    permission=Permission.REQUEST,
    action="ban-ip",
) -> ActionRequest:
    return ActionRequest(cap(capability_id), action, tuple(targets), permission)


def verified(
    subject: str, clock: FakeClock, role=PLATFORM_ADMIN, age=0, assertion_id=None
) -> VerifiedAuthentication:
    return VerifiedAuthentication(
        assertion_id=assertion_id or f"asr-{subject}-{clock.now.timestamp()}",
        platform_adapter_id=ADAPTER,
        platform_instance_id=INSTANCE,
        platform_subject_id=subject,
        auth_time=clock.now - timedelta(seconds=age),
        method_claims=("password",),
        platform_role=role,
    )


def step(
    step_id="s1",
    capability_id="ban",
    targets=("sys-1",),
    op="service.control",
    op_class="write",
    resources=("svc:fail2ban",),
    expected_state="running",
    deadline=None,
    clock=None,
    **kw,
) -> PlanStep:
    return PlanStep(
        step_id=step_id,
        integration_id=kw.pop("integration_id", "fail2ban"),
        capability_id=capability_id,
        target_refs=tuple(targets),
        op_id=op,
        op_major=kw.pop("op_major", 1),
        op_class=op_class,
        declaration_digest=kw.pop("declaration_digest", DECL_DIGEST),
        resource_refs=tuple(resources),
        params=kw.pop("params", {"ip": "203.0.113.7"}),
        expected_state=expected_state,
        deadline=deadline
        if deadline is not None
        else (clock.now + timedelta(minutes=30) if clock else None),
        **kw,
    )


def plan(*steps, observed_at=None) -> PlanProposal:
    """A Plan proposal. It carries no plan_ref: K4 generates one per commit (DEC-090 D90-6)."""
    return PlanProposal(tuple(steps), observed_at)


def anchor_read(*pairs, changes=()) -> K11AnchorRead:
    return K11AnchorRead(tuple(AnchorEntry(p, d) for p, d in pairs), tuple(changes))


def added(principal: str, digest: str) -> AnchorChange:
    return AnchorChange(principal, digest, "added")


class CoreTestCase(unittest.TestCase):
    store_class = K7Store

    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.path = f"{self._tmp.name}/k7.sqlite"
        self.clock = FakeClock()
        self.store = self.store_class(self.path, self.clock)
        self.core = K4Core(self.store, self.clock)
        self.decls = declarations()
        self.inv = inventory()
        self.adm = admissible()
        self.pol = policy()

    def tearDown(self) -> None:
        self.store.close()
        self._tmp.cleanup()

    # --- test-only K7 seeding ---------------------------------------------------------------------------------
    def _sql(self, sql: str, args: tuple) -> None:
        conn = sqlite3.connect(self.path)
        with conn:
            conn.execute(sql, args)
        conn.close()

    def seed_principal(
        self,
        pid: str,
        subject: str,
        state=PrincipalState.ACTIVE,
        status=BindingStatus.CONFIRMED,
        role=PLATFORM_ADMIN,
        roles=(),
    ) -> str:
        self._sql(
            "INSERT INTO principals VALUES (?, ?, ?)",
            (pid, state.value, to_iso(self.clock.now)),
        )
        self._sql(
            "INSERT INTO bindings VALUES (?, ?, ?, ?, ?, ?, ?)",
            (
                pid,
                ADAPTER,
                INSTANCE,
                subject,
                status.value,
                to_iso(self.clock.now),
                role,
            ),
        )
        for r in roles:
            self.seed_membership(pid, r)
        return pid

    def seed_membership(
        self, pid: str, role: str, state=RecordState.ACTIVE, valid_until=None
    ) -> None:
        self._sql(
            "INSERT INTO role_memberships VALUES (?, ?, ?, ?, NULL, ?)",
            (f"m-{pid}-{role}", pid, role, state.value, to_iso(valid_until)),
        )

    def seed_grant(self, grant: Grant) -> None:
        self._sql(
            "INSERT INTO grants VALUES (?, ?, ?, ?)",
            (
                grant.grant_id,
                grant.subject_kind,
                grant.subject_id,
                json.dumps(encode_grant(grant)),
            ),
        )

    def establish(self, *pairs, changes=None):
        changes = changes if changes is not None else [added(p, d) for p, d in pairs]
        return self.core.observe_anchor_read(anchor_read(*pairs, changes=changes))

    def decision_rows(self) -> list[tuple[str, str, str]]:
        """(authorization_ref, plan_ref, plan_digest) of every stored Decision."""
        conn = sqlite3.connect(self.path)
        rows = conn.execute(
            "SELECT authorization_ref, plan_ref, plan_digest FROM decisions ORDER BY created_at"
        ).fetchall()
        conn.close()
        return rows

    def plan_rows(self) -> int:
        conn = sqlite3.connect(self.path)
        n = conn.execute("SELECT COUNT(*) FROM plans").fetchone()[0]
        conn.close()
        return n

    def audit(self, kind: str | None = None) -> list[dict]:
        recs = self.store.audit_records()
        return [r for r in recs if kind is None or r["event_kind"] == kind]

    def intent(self, auth, req=None, anchors=None, **kw):
        return self.core.evaluate_intent(
            req or request(),
            auth,
            kw.get("decls", self.decls),
            kw.get("inv", self.inv),
            kw.get("adm", self.adm),
            kw.get("pol", self.pol),
            anchors,
        )

    def commit(self, auth, the_plan, req=None, anchors=None, **kw):
        return self.core.commit_plan(
            req or request(),
            auth,
            kw.get("decls", self.decls),
            kw.get("inv", self.inv),
            kw.get("adm", self.adm),
            kw.get("pol", self.pol),
            anchors,
            the_plan,
        )


__all__ = [name for name in dir() if not name.startswith("_")] + ["TargetScc"]
