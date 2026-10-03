"""K4 authorization-and-audit core: locked §17.22 steps 1–10, the §21 records DEC-089 authorizes, R4a and R5a, and
the K4 side of the §22 bootstrap act.

Every authorization outcome is computed here from abstract facts (DEC-089 D89-3 … D89-5); no input carries a decision.
Nothing here runs host commands, constructs K6 (P6) requests, verifies signatures or implements P2, K5, K6, K8, K9 or
K11 (DEC-029; DEC-089 D89-16).
"""

from __future__ import annotations

import uuid
from collections.abc import Callable, Mapping
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from enum import Enum
from typing import Any

from . import audit
from .inputs import (
    ActionRequest,
    AdmissibilityInput,
    ApprovalVerificationResult,
    AuthenticationFailure,
    AuthenticationResult,
    CapabilityDeclaration,
    ExecutionDeclaration,
    InventoryResolution,
    K11AnchorRead,
    K11Declarations,
    PlanProposal,
    PlanStep,
    ResolvedTarget,
    RootDetermination,
    VerifiedAuthentication,
)
from .model import (
    ADMINISTRATOR_ROLE,
    OP_CLASSES,
    PLATFORM_ADMIN,
    SELECTOR_CLASSES,
    ApprovalRequired,
    AuthFresh,
    Binding,
    BindingStatus,
    CapabilityRef,
    CapAll,
    CapCategory,
    CapExact,
    CapIntegration,
    Condition,
    DecisionStatus,
    Grant,
    Permission,
    PlanMaxAge,
    PlatformRole,
    PrincipalState,
    RecordState,
    TargetAny,
    TargetCategory,
    TargetComponent,
    TargetManagementIn,
    TargetScc,
    TargetSystem,
    Tier,
)
from .policy import (
    APPROVAL,
    REAUTH,
    EffectivePolicy,
    PolicyInputs,
    PolicyUnavailable,
    resolve_policy,
)
from .serialization import (
    EncodingError,
    canonical_json,
    encode_condition,
    sha256_hex,
    to_iso,
)
from .store import K7Store, K7Unavailable

ACTOR_HUMAN = "HUMAN"
ACTOR_LOCAL_ROOT_OPERATOR = "Local Root Operator"
BOOTSTRAP_AUTHORITY = "Local Root Operator bootstrap authority (A-07)"
B1_DENIAL_CONDITION = "audit_write_failure_denial"
P11_FIELDS = frozenset(
    {"platform_adapter_id", "platform_instance_id", "platform_subject_id"}
)


class Outcome(str, Enum):
    """Result categories, named after the P2/K3 §P.5 error model (implementation representation)."""

    OK = "OK"
    UNAUTHENTICATED = "UNAUTHENTICATED"
    FORBIDDEN = "FORBIDDEN"
    INADMISSIBLE = "INADMISSIBLE"
    UNAVAILABLE = "UNAVAILABLE"
    MALFORMED = "MALFORMED"


class UnsupportedInSlice(Exception):
    """The request needs semantics outside DEC-089 (stop rule, D89-19). No state or audit effect occurs."""


class AnchorsNotEstablished(Exception):
    """The B3 records of an anchor read could not be made durable; the read must not be relied on (§21.12)."""


@dataclass(frozen=True)
class EstablishedAnchors:
    """An anchor read whose observed changes are durably recorded as B3. Only K4Core creates these.

    Only the most recent read is usable: a failed or newer read makes every earlier object stale, so K4 never falls
    back to a previously observed anchor set (§21.12; §21.15).
    """

    anchors: frozenset[tuple[str, str]]  # (named_principal, anchor_digest)
    _issuer: object = field(repr=False, compare=False)

    def principal_for(self, anchor_digest: str | None) -> str | None:
        """The Principal the anchor names, or None if absent or ambiguous (fail closed)."""
        named = {p for p, digest in self.anchors if digest == anchor_digest}
        return next(iter(named)) if len(named) == 1 else None


@dataclass
class Result:
    outcome: Outcome
    reason: str
    trace: list[str]
    principal_id: str | None = None
    effective_tier: Tier | None = None
    matched_grants: tuple[str, ...] = ()
    authorization_ref: str | None = None
    status: DecisionStatus | None = None
    plan_digest: str | None = None
    audit_ids: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return self.outcome is Outcome.OK


@dataclass
class _Target:
    ref: str
    resolved: ResolvedTarget


@dataclass
class _Ctx:
    """Evaluation state of one request; it is never persisted and is not a cache (§17.17)."""

    now: datetime
    trace: list[str]
    auth: VerifiedAuthentication | None = None
    principal_id: str | None = None
    binding: Binding | None = None
    policy: EffectivePolicy | None = None
    conditions: list[dict] = field(default_factory=list)
    matched: dict[str, Grant] = field(default_factory=dict)
    roles_used: set[str] = field(default_factory=set)
    admissibility: list[dict] = field(default_factory=list)
    intent_targets: list[str] = field(default_factory=list)


class K4Core:
    def __init__(self, store: K7Store, clock: Callable[[], datetime]) -> None:
        self._store = store
        self._clock = clock
        self._current_read: object | None = None
        self._pending_denials = 0
        self._pending_since: datetime | None = None

    # =============================================================================================================
    # Audit writing, R4a and R5a
    # =============================================================================================================

    def _note_unrecorded_denial(self, at: datetime) -> None:
        """§21.12 denial row: the denial stays a refusal; a B1 is written when possible; nothing is late-recorded."""
        if self._pending_denials == 0:
            self._pending_since = at
        self._pending_denials += 1

    def _flush_pending_b1(self) -> None:
        if not self._pending_denials:
            return
        assert self._pending_since is not None
        record = audit.draft(
            "B1",
            self._pending_since,
            condition_kind=B1_DENIAL_CONDITION,
            count=self._pending_denials,
        )
        try:
            with self._store.transaction() as tx:
                tx.append_audit(record.fields)
        except K7Unavailable:
            return
        self._pending_denials = 0
        self._pending_since = None

    def _record(
        self,
        drafts: list[audit.AuditDraft],
        mutate: Callable[[Any], None] | None,
        denial: bool,
    ) -> bool:
        """Write the records, with any mutation, in one atomic commit (R4a). Returns False if not durable."""
        try:
            with self._store.transaction() as tx:
                if mutate is not None:
                    mutate(tx)
                for d in drafts:
                    tx.append_audit(d.fields)
        except K7Unavailable:
            if denial:
                for d in drafts:
                    self._note_unrecorded_denial(
                        datetime.fromisoformat(d.fields["timestamp"])
                    )
            return False
        return True

    # =============================================================================================================
    # K11 anchors (§17.9; §21.15; DEC-089 D89-3)
    # =============================================================================================================

    def observe_anchor_read(self, read: K11AnchorRead) -> EstablishedAnchors:
        """Record a B3 for each observed change; the read becomes usable only once all are durable (§21.12)."""
        self._flush_pending_b1()
        self._current_read = (
            None  # an earlier read is never relied on once a new read begins
        )
        observed_at = (
            self._clock()
        )  # §21.7: K4's time of observation during its K11 read
        drafts = [
            audit.draft(
                "B3",
                observed_at,
                named_principal=c.named_principal,
                anchor_digest=c.anchor_digest,
                observed_at=to_iso(observed_at),
                change_kind=c.change_kind,
                observer=audit.OBSERVED_BY_K4,
            )
            for c in read.changes
        ]
        if drafts and not self._record(drafts, None, denial=False):
            raise AnchorsNotEstablished(
                "B3 records not durable; the changed anchor set is not established"
            )
        token = object()
        self._current_read = token
        return EstablishedAnchors(
            frozenset((a.named_principal, a.anchor_digest) for a in read.anchors),
            token,
        )

    def anchor_read_failed(self) -> None:
        """Report that a K11 anchor read failed. No earlier read is relied on afterwards (§21.12; §17.16)."""
        self._current_read = None

    def _anchors_ok(self, anchors: EstablishedAnchors | None) -> bool:
        return (
            anchors is not None
            and self._current_read is not None
            and anchors._issuer is self._current_read
        )

    # =============================================================================================================
    # Phase I — steps 1–4
    # =============================================================================================================

    def evaluate_intent(
        self,
        request: ActionRequest,
        authentication: AuthenticationResult,
        declarations: K11Declarations,
        inventory: InventoryResolution,
        admissibility: AdmissibilityInput,
        policy: PolicyInputs,
        anchors: EstablishedAnchors | None,
    ) -> Result:
        """Intent Authorization: §17.22 steps 1–4, recorded as A1 (or B2 for a step-1 failure)."""
        if request.permission not in (Permission.REQUEST, Permission.VIEW):
            # approve is step 10; cancel is Phase IV (outside this slice, DEC-089 D89-2).
            raise UnsupportedInSlice("Intent Authorization evaluates request or view")
        self._flush_pending_b1()
        ctx = _Ctx(now=self._clock(), trace=[])
        return self._phase_one(
            ctx,
            request,
            authentication,
            declarations,
            inventory,
            admissibility,
            policy,
            anchors,
        )[0]

    def _phase_one(
        self,
        ctx: _Ctx,
        request: ActionRequest,
        authentication: AuthenticationResult,
        declarations: K11Declarations,
        inventory: InventoryResolution,
        admissibility: AdmissibilityInput,
        policy: PolicyInputs,
        anchors: EstablishedAnchors | None,
    ) -> tuple[Result, list[_Target], Tier | None, CapabilityDeclaration | None]:
        # ---- Step 1: Authenticate ----------------------------------------------------------------------------
        failure = self._step1_authenticate(ctx, authentication)
        if isinstance(failure, Result):
            return failure, [], None, None
        if failure is not None:
            # Step 1 passed, but the DEC-089 Q1 confirmation could not be recorded, so the Binding's latest
            # confirmed platform role cannot be positively established for §17.7 (§17.16: denied).
            ctx.trace.append("step2:k7_unavailable")
            return (
                self._deny_a1(ctx, request, [], None, Outcome.FORBIDDEN, failure),
                [],
                None,
                None,
            )

        # ---- Step 2: Identify capability, Action and targets -------------------------------------------------
        ctx.trace.append("step2:identify")
        try:
            ctx.policy = resolve_policy(policy)
        except PolicyUnavailable:
            return (
                self._deny_a1(
                    ctx, request, [], None, Outcome.FORBIDDEN, "policy_unavailable"
                ),
                [],
                None,
                None,
            )
        cap_decl, decl = self._identify_capability(request.capability, declarations)
        if not request.capability.is_reserved and cap_decl is None:
            return (
                self._deny_a1(
                    ctx,
                    request,
                    [],
                    None,
                    Outcome.FORBIDDEN,
                    "capability_not_identified",
                ),
                [],
                None,
                None,
            )
        targets = self._resolve_targets(
            request.target_refs, inventory, request.capability.is_reserved
        )
        if targets is None:
            return (
                self._deny_a1(
                    ctx, request, [], None, Outcome.FORBIDDEN, "target_not_resolved"
                ),
                [],
                None,
                None,
            )
        tier = self._effective_tier(request.capability, cap_decl, decl, ctx.policy)
        ctx.intent_targets = [t.resolved.key for t in targets]

        # ---- Step 3: Admissibility (recorded separately; not authorization) -----------------------------------
        ctx.trace.append("step3:admissibility")
        if not self._admissible(ctx, request.capability, targets, admissibility):
            return (
                self._deny_a1(
                    ctx, request, targets, tier, Outcome.INADMISSIBLE, "inadmissible"
                ),
                targets,
                tier,
                cap_decl,
            )

        # ---- Step 4: Intent Authorization ---------------------------------------------------------------------
        ctx.trace.append("step4:intent_authorization")
        if tier == Tier.R4 and not self._anchors_ok(anchors):
            # §17.16: K11 anchors unreadable → R4 denied.
            return (
                self._deny_a1(
                    ctx,
                    request,
                    targets,
                    tier,
                    Outcome.FORBIDDEN,
                    "k11_anchors_unestablished",
                ),
                targets,
                tier,
                cap_decl,
            )
        try:
            for t in targets:
                matched = self._matching_grants(
                    ctx,
                    request.permission,
                    request.capability,
                    cap_decl,
                    t,
                    tier,
                    None,
                    False,
                )
                if not matched:
                    return (
                        self._deny_a1(
                            ctx,
                            request,
                            targets,
                            tier,
                            Outcome.FORBIDDEN,
                            "no_matching_grant",
                        ),
                        targets,
                        tier,
                        cap_decl,
                    )
        except K7Unavailable:
            return (
                self._deny_a1(
                    ctx, request, targets, tier, Outcome.FORBIDDEN, "k7_unavailable"
                ),
                targets,
                tier,
                cap_decl,
            )
        result = Result(
            Outcome.OK,
            "intent_authorized",
            ctx.trace,
            ctx.principal_id,
            tier,
            tuple(sorted(ctx.matched)),
        )
        if request.permission is Permission.VIEW and tier == Tier.R0:
            ctx.trace.append("audit:r0_view_not_recorded")  # §17.18; §21.16
            return result, targets, tier, cap_decl
        record = self._a1(ctx, request, targets, tier, "permitted", "intent_authorized")
        if not self._record([record], None, denial=False):
            # R5a: the decision does not proceed without its durable record.
            return (
                Result(
                    Outcome.UNAVAILABLE,
                    "audit_unavailable",
                    ctx.trace,
                    ctx.principal_id,
                    tier,
                ),
                targets,
                tier,
                cap_decl,
            )
        result.audit_ids.append(record.fields["audit_id"])
        return result, targets, tier, cap_decl

    def _step1_authenticate(
        self, ctx: _Ctx, authentication: AuthenticationResult
    ) -> Result | str | None:
        """None on success; a B2 Result on any step-1 failure (§21.6, §21.14), including Binding or Principal
        state that cannot be read; or "k7_unavailable" when step 1 passed but its Q1 confirmation was not recorded.
        """
        ctx.trace.append("step1:authenticate")
        if isinstance(authentication, AuthenticationFailure):
            claimed = None
            if authentication.claimed_assertion_id is not None:
                claimed = {
                    "value": authentication.claimed_assertion_id,
                    "verified": False,
                }
            return self._b2(ctx, authentication.failed_check, None, claimed)
        if not isinstance(authentication, VerifiedAuthentication):
            raise TypeError(
                "authentication must come from the abstract authentication boundary"
            )
        ctx.auth = authentication
        try:
            binding = self._store.find_binding(
                authentication.platform_adapter_id,
                authentication.platform_instance_id,
                authentication.platform_subject_id,
            )
        except K7Unavailable:
            return self._b2(ctx, "binding", None, None)
        if binding is None:
            return self._b2(ctx, "binding", None, None)  # A-03: no enrolled Principal
        try:
            principal = self._store.principal(binding.principal_id)
        except K7Unavailable:
            return self._b2(ctx, "principal_state", binding.principal_id, None)
        if binding.status is BindingStatus.LOST:
            return self._b2(ctx, "binding", binding.principal_id, None)
        if principal is None or principal.state is not PrincipalState.ACTIVE:
            return self._b2(ctx, "principal_state", binding.principal_id, None)
        # §17.1.4: an interactive request is confirmed by its own verified assertion. DEC-089 Q1: record it.
        try:
            with self._store.transaction() as tx:
                tx.record_binding_confirmation(
                    binding.principal_id, ctx.now, authentication.platform_role
                )
            ctx.binding = self._store.binding_of(binding.principal_id)
        except K7Unavailable:
            ctx.principal_id = binding.principal_id
            ctx.trace.append("step1:authenticated")
            return "k7_unavailable"
        ctx.principal_id = binding.principal_id
        ctx.trace.append("step1:authenticated")
        return None

    def _b2(
        self,
        ctx: _Ctx,
        failure_reason: str,
        principal_id: str | None,
        claimed: dict | None,
    ) -> Result:
        ctx.trace.append(f"step1:failed:{failure_reason}")
        record = audit.draft(
            "B2",
            ctx.now,
            failure_reason=failure_reason,
            principal_id=principal_id,
            claimed_assertion_id=claimed,
        )
        recorded = self._record([record], None, denial=True)
        res = Result(Outcome.UNAUTHENTICATED, failure_reason, ctx.trace, principal_id)
        if recorded:
            res.audit_ids.append(record.fields["audit_id"])
        return res

    # ---- step 2 helpers -----------------------------------------------------------------------------------------

    @staticmethod
    def _identify_capability(
        cap: CapabilityRef, declarations: K11Declarations
    ) -> tuple[CapabilityDeclaration | None, ExecutionDeclaration | None]:
        if cap.is_reserved or cap.integration_id is None:
            return None, None
        decl = declarations.find(cap.integration_id)
        if decl is None:
            return None, None
        for c in decl.capabilities:
            if c.capability_id == cap.capability_id:
                return c, decl
        return None, decl

    @staticmethod
    def _resolve_targets(
        refs: tuple[str, ...], inventory: InventoryResolution, reserved: bool
    ) -> list[_Target] | None:
        if not refs:
            return None
        out = []
        for ref in refs:
            resolved = inventory.targets.get(ref)
            if resolved is None:
                return None
            # §17.4.1/§17.6: the SCC target is for reserved scc.* capabilities only.
            if (resolved.kind == "scc") != reserved:
                return None
            out.append(_Target(ref, resolved))
        return out

    @staticmethod
    def _effective_tier(
        cap: CapabilityRef,
        cap_decl: CapabilityDeclaration | None,
        decl: ExecutionDeclaration | None,
        policy: EffectivePolicy,
    ) -> Tier:
        """§17.5.3 / A-16: highest of declared tier, K11-derived tier (criteria a, b) and any local raise."""
        if cap.is_reserved:
            return Tier.R4  # criterion (d)
        assert cap_decl is not None and decl is not None
        tier = cap_decl.declared_tier
        for e in decl.scope_entries:
            if e.capability_id != cap.capability_id or e.op_class != "write":
                continue
            if e.executable_semantics or e.family == "package":  # criteria (a), (b)
                tier = Tier.R4
        raise_to = policy.tier_raise(cap.key)
        if raise_to is not None and raise_to > tier:
            tier = raise_to
        return tier

    # ---- step 3 helper -------------------------------------------------------------------------------------------

    @staticmethod
    def _admissible(
        ctx: _Ctx,
        cap: CapabilityRef,
        targets: list[_Target],
        admissibility: AdmissibilityInput,
    ) -> bool:
        ok = True
        for t in targets:
            facts = admissibility.facts.get((cap.key, t.resolved.key))
            if facts is None:
                ctx.admissibility.append(
                    {"target": t.resolved.key, "result": "not_established"}
                )
                ok = False
                continue
            entry = {
                "target": t.resolved.key,
                "integration_valid": facts.integration_valid,
                "capability_available": facts.capability_available,
                "compatibility_permits": facts.compatibility_permits,
                "management_permits": facts.management_permits,
                "result": "admissible" if facts.holds() else "inadmissible",
            }
            ctx.admissibility.append(entry)
            ok = ok and facts.holds()
        return ok

    # ---- step 4 / 7 / 10 helper: Grant matching (§17.4.2; §17.7) -------------------------------------------------

    def _effective_grants(
        self, principal_id: str, policy: EffectivePolicy, now: datetime
    ) -> list[tuple[Grant, str | None]]:
        grants: list[tuple[Grant, str | None]] = [
            (g, None) for g in self._store.direct_grants_of(principal_id)
        ]
        for m in self._store.memberships_of(principal_id):
            if not m.effective(now):
                continue
            for i, spec in enumerate(policy.role_grants(m.role_id)):
                grants.append(
                    (
                        Grant(
                            grant_id=f"role:{m.role_id}:{i}",
                            subject_kind="role",
                            subject_id=m.role_id,
                            permission=spec.permission,
                            capability_selector=spec.capability_selector,
                            target_selector=spec.target_selector,
                            max_tier=spec.max_tier,
                            conditions=spec.conditions,
                        ),
                        m.role_id,
                    )
                )
        return grants

    def _matching_grants(
        self,
        ctx: _Ctx,
        permission: Permission,
        cap: CapabilityRef,
        cap_decl: CapabilityDeclaration | None,
        target: _Target,
        tier: Tier,
        plan_observed_at: datetime | None,
        at_decision: bool,
        principal_id: str | None = None,
        binding: Binding | None = None,
        auth: VerifiedAuthentication | None | bool = True,
    ) -> list[Grant]:
        """Every effective Grant meeting all §17.4.2 criteria. K4 records every Grant that matched."""
        assert ctx.policy is not None
        pid = principal_id or ctx.principal_id
        assert pid is not None
        bnd = binding if principal_id is not None else ctx.binding
        context = ctx.auth if auth is True else (auth or None)
        matched = []
        for grant, role in self._effective_grants(pid, ctx.policy, ctx.now):
            if grant.state is not RecordState.ACTIVE or not grant.in_validity(ctx.now):
                continue
            if grant.permission is not permission:
                continue
            if not _capability_matches(grant, cap, cap_decl):
                continue
            if not _target_matches(grant, target.resolved):
                continue
            if tier > grant.max_tier:
                continue
            conditions = tuple(grant.conditions) + (
                PlatformRole(PLATFORM_ADMIN),
            )  # v1 implicit (§17.7; A-04)
            all_hold = True
            for cond in conditions:
                value = _evaluate_condition(
                    cond,
                    ctx.now,
                    context,
                    bnd,
                    target.resolved,
                    plan_observed_at,
                    at_decision,
                )
                ctx.conditions.append(
                    {
                        "grant_id": grant.grant_id,
                        "target": target.resolved.key,
                        "condition": encode_condition(cond),
                        "implicit": cond == PlatformRole(PLATFORM_ADMIN)
                        and cond not in grant.conditions,
                        "value": value,
                    }
                )
                if value is False:
                    all_hold = False
            if all_hold:
                matched.append(grant)
                if principal_id is None:
                    ctx.matched[grant.grant_id] = grant
                    if role is not None:
                        ctx.roles_used.add(role)
        return matched

    # ---- A1 ---------------------------------------------------------------------------------------------------

    def _a1(
        self,
        ctx: _Ctx,
        request: ActionRequest,
        targets: list[_Target],
        tier: Tier | None,
        decision: str,
        reason: str,
    ) -> audit.AuditDraft:
        policy = ctx.policy
        return audit.draft(
            "A1",
            ctx.now,
            actor_type=ACTOR_HUMAN,
            principal_id=ctx.principal_id,
            auth_context_ref=ctx.auth.assertion_id if ctx.auth else None,
            authority_basis=self._authority_basis(ctx),
            capability=request.capability.key,
            action=request.action,
            targets=[t.resolved.key for t in targets] or list(request.target_refs),
            admissibility_result=list(ctx.admissibility) or None,
            conditions=list(ctx.conditions) or None,
            effective_tier=tier.name if tier is not None else None,
            step_up=sorted(policy.step_up(tier))
            if (policy and tier is not None)
            else None,
            policy_revisions=policy.revisions if policy else None,
            revocation_state={
                gid: g.state.value for gid, g in sorted(ctx.matched.items())
            }
            or None,
            decision=decision,
            reason_code=reason,
        )

    @staticmethod
    def _authority_basis(ctx: _Ctx) -> dict:
        if not ctx.matched:
            return {"grants": [], "roles": [], "no_matching_grant": True}
        return {"grants": sorted(ctx.matched), "roles": sorted(ctx.roles_used)}

    def _deny_a1(
        self,
        ctx: _Ctx,
        request: ActionRequest,
        targets: list[_Target],
        tier: Tier | None,
        outcome: Outcome,
        reason: str,
    ) -> Result:
        ctx.trace.append(f"deny:{reason}")
        decision = "inadmissible" if outcome is Outcome.INADMISSIBLE else "denied"
        res = Result(outcome, reason, ctx.trace, ctx.principal_id, tier)
        if request.permission is Permission.VIEW and tier == Tier.R0:
            ctx.trace.append("audit:r0_view_not_recorded")
            return res
        record = self._a1(ctx, request, targets, tier, decision, reason)
        if self._record([record], None, denial=True):
            res.audit_ids.append(record.fields["audit_id"])
        return res

    # =============================================================================================================
    # Phases II–III — steps 5–9 (Plan commit runs the full evaluation, steps 1–9: §17.13.1)
    # =============================================================================================================

    def commit_plan(
        self,
        request: ActionRequest,
        authentication: AuthenticationResult,
        declarations: K11Declarations,
        inventory: InventoryResolution,
        admissibility: AdmissibilityInput,
        policy: PolicyInputs,
        anchors: EstablishedAnchors | None,
        plan: PlanProposal,
    ) -> Result:
        if request.capability.is_reserved:
            # Approval semantics for K4-internal Actions are open (Q19-04; DEC-089 D89-11, D89-19, D89-20).
            raise UnsupportedInSlice(
                "Plans for reserved scc.* capabilities are outside this slice"
            )
        if request.permission is not Permission.REQUEST:
            raise ValueError("a Plan realizes a requested Action")
        if (
            not isinstance(plan, PlanProposal)
            or not isinstance(plan.plan_ref, str)
            or not plan.plan_ref
        ):
            # No plan_ref exists to record an A2 against; the envelope is refused by schema validation with no
            # state or audit effect (§15.10 P3; P2/K3 §P.5 MALFORMED).
            return Result(Outcome.MALFORMED, "plan_envelope_malformed", [])
        self._flush_pending_b1()
        ctx = _Ctx(now=self._clock(), trace=[])
        intent, _targets, action_tier, _cap_decl = self._phase_one(
            ctx,
            request,
            authentication,
            declarations,
            inventory,
            admissibility,
            policy,
            anchors,
        )
        if not intent.ok:
            return intent
        a1_ids = list(intent.audit_ids)
        assert ctx.policy is not None
        pol = ctx.policy

        # ---- Step 5: K5 proposes; K4 validates structure and K11 coverage, computes plan_digest -----------------
        ctx.trace.append("step5:plan_validation")
        digest = None
        content = ""
        try:
            steps_info, reason = self._validate_plan(plan, declarations, inventory, pol)
            if steps_info is not None:
                content = canonical_json(_plan_content(plan))
                digest = sha256_hex(content)
        except (EncodingError, TypeError, ValueError, AttributeError, RecursionError):
            steps_info, reason = None, "plan_malformed"
        if steps_info is None or digest is None:
            return self._deny_a2(
                ctx, request, plan, None, [], None, reason or "plan_malformed", a1_ids
            )

        # ---- Step 6: Plan tier --------------------------------------------------------------------------------
        ctx.trace.append("step6:plan_tier")
        plan_tier = max(info["tier"] for info in steps_info.values())
        # §17.10 trigger and §17.8 requirement: "the effective tier of the Action or Plan".
        assert action_tier is not None
        step_up_tier = max(action_tier, plan_tier)
        all_targets = sorted(
            {t.resolved.key for info in steps_info.values() for t in info["targets"]}
        )

        # ---- Step 7: Plan Authorization over every (capability, target) pair, and PLAN_MAX_AGE -----------------
        ctx.trace.append("step7:plan_authorization")
        # Plan commit is the full steps 1-9 evaluation (§17.13.1). Grants matched at step 4 stay in ctx.matched:
        # every matched Grant is a Grant used (owner reading), for approval, expires_at and the Decision record.
        if step_up_tier == Tier.R4 and not self._anchors_ok(anchors):
            return self._deny_a2(
                ctx,
                request,
                plan,
                digest,
                all_targets,
                step_up_tier,
                "k11_anchors_unestablished",
                a1_ids,
            )
        try:
            for info in steps_info.values():
                for t in info["targets"]:
                    matched = self._matching_grants(
                        ctx,
                        Permission.REQUEST,
                        info["cap"],
                        info["cap_decl"],
                        t,
                        info["tier"],
                        plan.newest_input_observation_at,
                        True,
                    )
                    if not matched:
                        return self._deny_a2(
                            ctx,
                            request,
                            plan,
                            digest,
                            all_targets,
                            step_up_tier,
                            "plan_not_covered",
                            a1_ids,
                        )
        except K7Unavailable:
            return self._deny_a2(
                ctx,
                request,
                plan,
                digest,
                all_targets,
                step_up_tier,
                "k7_unavailable",
                a1_ids,
            )
        # Every matched Grant is used, including those matched at step 4, so each PLAN_MAX_AGE condition of a used
        # Grant is evaluated at Decision time (§17.11; §17.22 step 7; owner reading "used = matched").
        for g in list(ctx.matched.values()):
            for c in g.conditions:
                if not isinstance(c, PlanMaxAge):
                    continue
                obs = plan.newest_input_observation_at
                fresh = obs is not None and ctx.now - obs <= timedelta(
                    seconds=c.max_age_seconds
                )
                ctx.conditions.append(
                    {
                        "grant_id": g.grant_id,
                        "condition": encode_condition(c),
                        "at_decision": True,
                        "value": bool(fresh),
                    }
                )
                if not fresh:
                    return self._deny_a2(
                        ctx,
                        request,
                        plan,
                        digest,
                        all_targets,
                        step_up_tier,
                        "plan_max_age",
                        a1_ids,
                    )
        policy_plan_age = pol.plan_max_age
        if policy_plan_age is not None:
            obs = plan.newest_input_observation_at
            fresh = obs is not None and ctx.now - obs <= timedelta(
                seconds=policy_plan_age
            )
            ctx.conditions.append(
                {
                    "policy": "PLAN_MAX_AGE",
                    "max_age_seconds": policy_plan_age,
                    "value": bool(fresh),
                }
            )
            if not fresh:
                return self._deny_a2(
                    ctx,
                    request,
                    plan,
                    digest,
                    all_targets,
                    step_up_tier,
                    "plan_max_age",
                    a1_ids,
                )

        # ---- Step 8: Step-up (REAUTH) ---------------------------------------------------------------------------
        ctx.trace.append("step8:step_up")
        step_up = set(pol.step_up(step_up_tier))
        if REAUTH in step_up:
            max_age = pol.reauth_max_age(step_up_tier)
            assert ctx.auth is not None
            fresh = max_age is not None and ctx.now - ctx.auth.auth_time <= timedelta(
                seconds=max_age
            )
            ctx.conditions.append(
                {
                    "step_up": "AUTH_FRESH",
                    "max_age_seconds": max_age,
                    "value": bool(fresh),
                }
            )
            if not fresh:
                reason = (
                    "reauth_required" if max_age is not None else "policy_unavailable"
                )
                return self._deny_a2(
                    ctx,
                    request,
                    plan,
                    digest,
                    all_targets,
                    step_up_tier,
                    reason,
                    a1_ids,
                )

        # §17.8: approval is required for effective tier R4 or any matched Grant carrying APPROVAL_REQUIRED.
        if any(
            isinstance(c, ApprovalRequired)
            for g in ctx.matched.values()
            for c in g.conditions
        ):
            step_up.add(APPROVAL)
        # D89-22: the K11 per-scope-entry approval_required flag remains an additional input/condition.
        if any(info["k11_approval_flag"] for info in steps_info.values()):
            step_up.add(APPROVAL)
        approval_required = APPROVAL in step_up
        # D89-22: when the Plan requires approval, every K6 request in it is approval-requiring.
        approval_steps = sorted(steps_info) if approval_required else []
        # §17.22 step 5 / A-21: approval-requiring requests must be fully determined.
        for sid in approval_steps:
            step = steps_info[sid]["step"]
            if step.expected_state is None or step.deadline is None:
                return self._deny_a2(
                    ctx,
                    request,
                    plan,
                    digest,
                    all_targets,
                    step_up_tier,
                    "approval_request_not_fully_determined",
                    a1_ids,
                )

        # ---- Step 9: Create the Authorization Decision ---------------------------------------------------------
        ctx.trace.append("step9:create_decision")
        expiry_bounds = []
        if pol.decision_max_age is None:
            return self._deny_a2(
                ctx,
                request,
                plan,
                digest,
                all_targets,
                step_up_tier,
                "policy_unavailable",
                a1_ids,
            )
        obs = plan.newest_input_observation_at
        plan_ages = [
            c.max_age_seconds
            for g in ctx.matched.values()
            for c in g.conditions
            if isinstance(c, PlanMaxAge)
        ]
        if policy_plan_age is not None:
            plan_ages.append(policy_plan_age)
        try:
            expiry_bounds.append(ctx.now + timedelta(seconds=pol.decision_max_age))
            if obs is not None:
                expiry_bounds.extend(obs + timedelta(seconds=a) for a in plan_ages)
        except OverflowError:
            # A bound K4 cannot represent cannot be positively established (§17.16): denied.
            return self._deny_a2(
                ctx,
                request,
                plan,
                digest,
                all_targets,
                step_up_tier,
                "policy_unavailable",
                a1_ids,
            )
        expiry_bounds.extend(
            g.valid_until for g in ctx.matched.values() if g.valid_until is not None
        )
        expires_at = min(expiry_bounds)

        authorization_ref = uuid.uuid4().hex
        status = (
            DecisionStatus.AWAITING_APPROVAL
            if approval_required
            else DecisionStatus.AUTHORIZED
        )
        assert ctx.auth is not None
        body = {
            "authorization_ref": authorization_ref,
            "principal_id": ctx.principal_id,
            "auth_context_ref": ctx.auth.assertion_id,
            # §17.2: method claims are recorded; they satisfy only REAUTH freshness, never APPROVAL (A-18).
            "authentication_context": {
                "assertion_id": ctx.auth.assertion_id,
                "auth_time": to_iso(ctx.auth.auth_time),
                "method_claims": list(ctx.auth.method_claims),
            },
            "capability_set": sorted({info["cap"].key for info in steps_info.values()}),
            "action": request.action,
            "action_capability": request.capability.key,
            "target_set": all_targets,
            "plan_ref": plan.plan_ref,
            "plan_digest": digest,
            "policy_revisions": pol.revisions,
            "grants_used": sorted(ctx.matched),
            "step_up": sorted(step_up),
            "plan_tier": plan_tier.name,
            "step_up_tier": step_up_tier.name,
            "approval_steps": approval_steps,
            "steps": {
                sid: {
                    "capability": info["cap"].key,
                    "integration_id": info["cap"].integration_id,
                    "capability_id": info["cap"].capability_id,
                    "target_refs": [t.ref for t in info["targets"]],
                    "targets": [t.resolved.key for t in info["targets"]],
                }
                for sid, info in steps_info.items()
            },
            "expires_at": to_iso(expires_at),
            "created_at": to_iso(ctx.now),
        }
        record = self._a2(
            ctx,
            request,
            plan.plan_ref,
            digest,
            all_targets,
            step_up_tier,
            status.value,
            "plan_authorized",
            authorization_ref,
            sorted(step_up),
        )

        def mutate(tx: Any) -> None:
            # Read under the commit's write lock, so the A-24 check and invalidation cannot race.
            if any(
                d == digest for _, d in self._store.decisions_for_plan(plan.plan_ref)
            ):
                raise _PlanAlreadyDecided  # A-24: exactly one Decision per plan_digest
            prior_open = self._open_decisions(plan.plan_ref)
            for ref, _d in prior_open:
                tx.append_status(ref, DecisionStatus.INVALIDATED, ctx.now)  # §17.11; Q4
            tx.store_plan(plan.plan_ref, digest, content, ctx.now)
            tx.create_decision(authorization_ref, plan.plan_ref, digest, body, ctx.now)
            tx.append_status(authorization_ref, status, ctx.now)

        try:
            recorded = self._record([record], mutate, denial=False)
        except _PlanAlreadyDecided:
            return self._deny_a2(
                ctx,
                request,
                plan,
                digest,
                all_targets,
                step_up_tier,
                "plan_already_decided",
                a1_ids,
            )
        if not recorded:
            ctx.trace.append("r5a:not_recorded")
            return Result(
                Outcome.UNAVAILABLE,
                "audit_unavailable",
                ctx.trace,
                ctx.principal_id,
                step_up_tier,
                plan_digest=digest,
                audit_ids=a1_ids,
            )
        return Result(
            Outcome.OK,
            "plan_authorized",
            ctx.trace,
            ctx.principal_id,
            step_up_tier,
            tuple(sorted(ctx.matched)),
            authorization_ref,
            status,
            digest,
            a1_ids + [record.fields["audit_id"]],
        )

    def _validate_plan(
        self,
        plan: PlanProposal,
        declarations: K11Declarations,
        inventory: InventoryResolution,
        pol: EffectivePolicy,
    ) -> tuple[dict[str, dict] | None, str | None]:
        if (
            not isinstance(plan, PlanProposal)
            or not isinstance(plan.plan_ref, str)
            or not plan.plan_ref
        ):
            return None, "plan_malformed"
        if not isinstance(plan.steps, tuple) or not plan.steps:
            return None, "plan_malformed"
        if plan.newest_input_observation_at is not None and not _aware(
            plan.newest_input_observation_at
        ):
            return None, "plan_malformed"
        info: dict[str, dict] = {}
        for step in plan.steps:
            if (
                not isinstance(step, PlanStep)
                or not isinstance(step.step_id, str)
                or not step.step_id
            ):
                return None, "plan_malformed"
            if step.step_id in info:
                return None, "plan_malformed"
            if (
                not isinstance(step.integration_id, str)
                or not isinstance(step.capability_id, str)
                or step.op_class not in OP_CLASSES
                or not isinstance(step.op_major, int)
                or isinstance(step.op_major, bool)
                or step.op_major < 0
                or not isinstance(step.op_id, str)
                or step.op_id.count(".") != 1
                or not all(step.op_id.split("."))
                or (step.deadline is not None and not _aware(step.deadline))
                or not _str_tuple(step.target_refs)
                or not _str_tuple(step.resource_refs)
                or not _str_tuple(step.handle_refs)
                or not isinstance(step.params, Mapping)
                or not isinstance(step.selectors, Mapping)
                or not isinstance(step.declaration_digest, str)
            ):
                return None, "plan_malformed"
            cap = step.capability
            if cap.capability_id.startswith("scc."):
                return None, "plan_malformed"
            cap_decl, decl = self._identify_capability(cap, declarations)
            if cap_decl is None or decl is None:
                return None, "k11_coverage_insufficient"
            if step.declaration_digest != decl.declaration_digest:
                return None, "k11_coverage_insufficient"
            covering = [
                e
                for e in decl.scope_entries
                if e.capability_id == step.capability_id
                and e.op_id == step.op_id
                and e.op_major == step.op_major
                and e.op_class == step.op_class
                and set(step.resource_refs) <= e.resources
                and set(step.handle_refs) <= e.handles
            ]
            if not covering:
                return (
                    None,
                    "k11_coverage_insufficient",
                )  # §17.6: rejected during K4 validation
            targets = self._resolve_targets(step.target_refs, inventory, False)
            if targets is None:
                return None, "target_not_resolved"
            info[step.step_id] = {
                "step": step,
                "cap": cap,
                "cap_decl": cap_decl,
                "decl": decl,
                "targets": targets,
                "tier": self._effective_tier(cap, cap_decl, decl, pol),
                "k11_approval_flag": any(e.approval_required for e in covering),
            }
        return info, None

    def _a2(
        self,
        ctx: _Ctx,
        request: ActionRequest,
        plan_ref: str,
        digest: str | None,
        targets: list[str],
        tier: Tier | None,
        decision: str,
        reason: str,
        authorization_ref: str | None,
        step_up: list[str] | None,
    ) -> audit.AuditDraft:
        assert ctx.auth is not None and ctx.policy is not None
        return audit.draft(
            "A2",
            ctx.now,
            actor_type=ACTOR_HUMAN,
            principal_id=ctx.principal_id,
            auth_context_ref=ctx.auth.assertion_id,
            authority_basis=self._authority_basis(ctx),
            capability=request.capability.key,
            action=request.action,
            targets=targets or ctx.intent_targets or list(request.target_refs),
            admissibility_result=list(ctx.admissibility) or None,
            conditions=list(ctx.conditions) or None,
            effective_tier=tier.name if tier is not None else None,
            step_up=step_up
            if step_up is not None
            else (sorted(ctx.policy.step_up(tier)) if tier is not None else None),
            plan_ref=plan_ref,
            plan_digest=digest,
            authorization_ref=authorization_ref,
            policy_revisions=ctx.policy.revisions,
            revocation_state={
                gid: g.state.value for gid, g in sorted(ctx.matched.items())
            }
            or None,
            decision=decision,
            reason_code=reason,
        )

    def _deny_a2(
        self,
        ctx: _Ctx,
        request: ActionRequest,
        plan: PlanProposal,
        digest: str | None,
        targets: list[str],
        tier: Tier | None,
        reason: str,
        a1_ids: list[str],
    ) -> Result:
        ctx.trace.append(f"deny:{reason}")
        record = self._a2(
            ctx,
            request,
            plan.plan_ref,
            digest,
            targets,
            tier,
            "denied",
            reason,
            None,
            None,
        )

        def mutate(tx: Any) -> None:
            # Read under the commit's write lock. A read failure fails the whole commit: the denial stays a
            # refusal (§21.12) and no partial state is committed.
            for ref, d in self._open_decisions(plan.plan_ref):
                if d != digest:
                    tx.append_status(
                        ref, DecisionStatus.INVALIDATED, ctx.now
                    )  # §17.11; Q4

        res = Result(
            Outcome.FORBIDDEN,
            reason,
            ctx.trace,
            ctx.principal_id,
            tier,
            plan_digest=digest,
            audit_ids=list(a1_ids),
        )
        if self._record([record], mutate if digest is not None else None, denial=True):
            res.audit_ids.append(record.fields["audit_id"])
        return res

    def _open_decisions(self, plan_ref: str) -> list[tuple[str, str]]:
        """Decisions bound to plan_ref that are not yet INVALIDATED, as (authorization_ref, plan_digest)."""
        return [
            (ref, d)
            for ref, d in self._store.decisions_for_plan(plan_ref)
            if self._store.latest_status(ref) is not DecisionStatus.INVALIDATED
        ]

    # =============================================================================================================
    # Phase III — step 10: Approvals
    # =============================================================================================================

    def submit_approval(
        self,
        evidence: ApprovalVerificationResult,
        declarations: K11Declarations,
        inventory: InventoryResolution,
        policy: PolicyInputs,
        anchors: EstablishedAnchors | None,
    ) -> Result:
        self._flush_pending_b1()
        ctx = _Ctx(now=self._clock(), trace=["step10:approval"])
        ref = evidence.authorization_ref
        try:
            decision = self._store.decision(ref)
            status = self._store.latest_status(ref) if decision else None
            approved = self._store.approved_steps(ref) if decision else set()
        except K7Unavailable:
            return Result(Outcome.UNAVAILABLE, "k7_unavailable", ctx.trace)

        approver: str | None = None
        reason: str | None = None
        step_info = None
        if decision is None:
            reason = "decision_unknown"
        elif status is not DecisionStatus.AWAITING_APPROVAL:
            reason = "decision_not_awaiting_approval"
        elif evidence.step_id not in decision["approval_steps"]:
            reason = "request_not_approval_requiring"
        elif evidence.step_id in approved:
            reason = "request_already_approved"
        elif not self._anchors_ok(anchors):
            reason = "k11_anchors_unestablished"  # §17.16: approvals refused
        else:
            assert anchors is not None
            step_info = decision["steps"][evidence.step_id]
            try:
                ctx.policy = resolve_policy(policy)
            except PolicyUnavailable:
                reason = "policy_unavailable"
            if reason is None:
                # The anchor whose key verified the signature, and the Principal it names (§17.9; A-20).
                named = anchors.principal_for(evidence.verifying_anchor_digest)
                if not evidence.signature_valid or named is None:
                    reason = "signature_not_verified_against_anchor"
                elif not evidence.digest_matches:
                    reason = "digest_mismatch"
                else:
                    approver = named
                    reason = self._approver_check(
                        ctx, approver, step_info, decision, declarations, inventory
                    )

        accepted = reason is None
        ctx.trace.append("step10:accepted" if accepted else f"step10:rejected:{reason}")
        outcome = {"all_done": False}

        def a4(accept: bool, why: str | None) -> audit.AuditDraft:
            return audit.draft(
                "A4",
                ctx.now,
                actor_type=ACTOR_HUMAN,
                principal_id=approver,
                authority_basis=self._authority_basis(ctx),
                approval_refs=[
                    {
                        "evidence_ref": evidence.evidence_ref,
                        "step_id": evidence.step_id,
                        "signature_valid": evidence.signature_valid,
                        "digest_matches": evidence.digest_matches,
                        "anchor_digest": evidence.verifying_anchor_digest,
                    }
                ],
                authorization_ref=ref,
                plan_ref=decision["plan_ref"] if decision else None,
                plan_digest=decision["plan_digest"] if decision else None,
                capability=step_info["capability"] if step_info else None,
                targets=step_info["targets"] if step_info else None,
                revocation_state={
                    gid: g.state.value for gid, g in sorted(ctx.matched.items())
                }
                or None,
                decision="accepted" if accept else "rejected",
                reason_code="approval_accepted" if accept else why,
            )

        record = a4(accepted, reason)

        def mutate(tx: Any) -> None:
            assert approver is not None and decision is not None
            # Re-read under the commit's write lock so concurrent approvals cannot race.
            if self._store.latest_status(ref) is not DecisionStatus.AWAITING_APPROVAL:
                raise _ApprovalStateChanged
            done = self._store.approved_steps(ref)
            if evidence.step_id in done:
                raise _ApprovalStateChanged
            tx.record_approval(
                uuid.uuid4().hex,
                ref,
                evidence.step_id,
                evidence.evidence_ref,
                approver,
                ctx.now,
            )
            if set(decision["approval_steps"]) <= done | {evidence.step_id}:
                tx.append_status(ref, DecisionStatus.AUTHORIZED, ctx.now)
                outcome["all_done"] = True

        try:
            recorded = self._record(
                [record], mutate if accepted else None, denial=False
            )
        except _ApprovalStateChanged:
            accepted, reason = False, "approval_state_changed"
            ctx.trace.append(f"step10:rejected:{reason}")
            record = a4(False, reason)
            recorded = self._record([record], None, denial=False)
        all_done = outcome["all_done"]
        if not recorded:
            return Result(
                Outcome.UNAVAILABLE,
                "audit_unavailable",
                ctx.trace,
                approver,
                authorization_ref=ref,
            )
        res = Result(
            Outcome.OK if accepted else Outcome.FORBIDDEN,
            "approval_accepted" if accepted else str(reason),
            ctx.trace,
            approver,
            authorization_ref=ref,
            status=DecisionStatus.AUTHORIZED if all_done else status,
            audit_ids=[record.fields["audit_id"]],
        )
        return res

    def _approver_check(
        self,
        ctx: _Ctx,
        approver: str,
        step_info: dict,
        decision: dict,
        declarations: K11Declarations,
        inventory: InventoryResolution,
    ) -> str | None:
        """§17.8 "Who may approve" and the step-10 checks other than the abstract signature/digest result."""
        assert ctx.policy is not None
        try:
            principal = self._store.principal(approver)
            binding = self._store.binding_of(approver)
        except K7Unavailable:
            return "k7_unavailable"
        if principal is None or principal.state is not PrincipalState.ACTIVE:
            return "approver_not_active"
        if binding is None or binding.status is not BindingStatus.CONFIRMED:
            return "approver_binding_not_confirmed"
        cap = CapabilityRef(step_info["integration_id"], step_info["capability_id"])
        cap_decl, decl = self._identify_capability(cap, declarations)
        if cap_decl is None or decl is None:
            return "capability_not_identified"
        targets = self._resolve_targets(
            tuple(step_info["target_refs"]), inventory, False
        )
        if targets is None:
            return "target_not_resolved"
        tier = self._effective_tier(cap, cap_decl, decl, ctx.policy)
        try:
            for t in targets:
                matched = self._matching_grants(
                    ctx,
                    Permission.APPROVE,
                    cap,
                    cap_decl,
                    t,
                    tier,
                    None,
                    False,
                    principal_id=approver,
                    binding=binding,
                    auth=False,
                )
                if not matched:
                    return "approver_lacks_approve_grant"
                for g in matched:
                    ctx.matched[g.grant_id] = g
        except K7Unavailable:
            return "k7_unavailable"
        if (
            ctx.policy.separation_of_duties(Tier[decision["step_up_tier"]])
            and approver == decision["principal_id"]
        ):
            return "separation_of_duties"
        return None

    # =============================================================================================================
    # Bootstrap — K4 side of the §22 bootstrap act (DEC-089 D89-15)
    # =============================================================================================================

    def bootstrap(self, p11_request: object, root: RootDetermination) -> Result:
        self._flush_pending_b1()
        now = self._clock()
        trace = ["bootstrap"]
        if not isinstance(root, RootDetermination) or not root.caller_is_root:
            return Result(Outcome.FORBIDDEN, "caller_not_root", trace)  # §22.5.1
        if (
            not isinstance(p11_request, Mapping)
            or set(p11_request) != P11_FIELDS
            or not all(_p11_value(p11_request[k]) for k in P11_FIELDS)
        ):
            return Result(
                Outcome.MALFORMED, "p11_request_malformed", trace
            )  # §22.6 validation
        try:
            if self._store.any_administrator_membership_record():
                return Result(
                    Outcome.FORBIDDEN,
                    "bootstrap_unavailable_administrator_exists",
                    trace,
                )  # §22.3.2
        except K7Unavailable:
            return Result(Outcome.UNAVAILABLE, "k7_unavailable", trace)
        principal_id = uuid.uuid4().hex
        membership_id = uuid.uuid4().hex
        binding = (
            p11_request["platform_adapter_id"],
            p11_request["platform_instance_id"],
            p11_request["platform_subject_id"],
        )
        common = {
            "actor_type": ACTOR_LOCAL_ROOT_OPERATOR,
            "authority_basis": BOOTSTRAP_AUTHORITY,
            "lro_auth_ref": root.determination_ref,
            "decision": "applied",
        }
        records = [
            audit.draft(
                "A6",
                now,
                targets=[f"principal:{principal_id}"],
                reason_code="bootstrap_principal_creation",
                **common,
            ),
            audit.draft(
                "A6",
                now,
                targets=[f"principal:{principal_id}", f"role:{ADMINISTRATOR_ROLE}"],
                reason_code="bootstrap_administrator_membership",
                **common,
            ),
        ]

        def mutate(tx: Any) -> None:
            if self._store.any_administrator_membership_record():
                raise _BootstrapUnavailable  # §22.3.2, re-checked under the write lock
            tx.create_bootstrap_principal(principal_id, binding, membership_id, now)

        try:
            committed = self._record(records, mutate, denial=False)
        except _BootstrapUnavailable:
            return Result(
                Outcome.FORBIDDEN, "bootstrap_unavailable_administrator_exists", trace
            )
        if not committed:
            return Result(
                Outcome.UNAVAILABLE, "bootstrap_not_committed", trace
            )  # §22.4.4: nothing committed
        return Result(
            Outcome.OK,
            "bootstrap_committed",
            trace,
            principal_id,
            audit_ids=[r.fields["audit_id"] for r in records],
        )


# =================================================================================================================
# Pure helpers
# =================================================================================================================


def _p11_value(value: object) -> bool:
    if not isinstance(value, str) or not value:
        return False
    try:
        value.encode("utf-8")
    except UnicodeError:
        return False
    return True


class _BootstrapUnavailable(Exception):
    """Raised inside the commit when an `scc.administrator` membership record appeared concurrently."""


class _ApprovalStateChanged(Exception):
    """Raised inside the commit to roll it back when the Decision or step changed concurrently."""


class _PlanAlreadyDecided(Exception):
    """Raised inside the commit to roll it back when a Decision for this plan_digest exists (A-24)."""


def _aware(value: object) -> bool:
    return (
        isinstance(value, datetime)
        and value.tzinfo is not None
        and value.utcoffset() is not None
    )


def _str_tuple(value: object) -> bool:
    return isinstance(value, tuple) and all(isinstance(v, str) for v in value)


def _plan_content(plan: PlanProposal) -> dict:
    return {
        "plan_ref": plan.plan_ref,
        "newest_input_observation_at": plan.newest_input_observation_at,
        "steps": [
            {
                "step_id": s.step_id,
                "integration_id": s.integration_id,
                "capability_id": s.capability_id,
                "target_refs": list(s.target_refs),
                "op_id": s.op_id,
                "op_major": s.op_major,
                "op_class": s.op_class,
                "declaration_digest": s.declaration_digest,
                "resource_refs": list(s.resource_refs),
                "selectors": dict(s.selectors),
                "params": dict(s.params),
                "handle_refs": list(s.handle_refs),
                "expected_state": s.expected_state,
                "deadline": s.deadline,
            }
            for s in plan.steps
        ],
    }


def _class_matches(cls: str, cap_decl: CapabilityDeclaration | None) -> bool:
    if cls not in SELECTOR_CLASSES:
        return False
    if cls == "any":
        return True
    return cap_decl is not None and cap_decl.op_class == cls


def _capability_matches(
    grant: Grant, cap: CapabilityRef, cap_decl: CapabilityDeclaration | None
) -> bool:
    sel = grant.capability_selector
    if isinstance(sel, CapExact):
        return (
            sel.integration_id == cap.integration_id
            and sel.capability_id == cap.capability_id
        )
    if isinstance(sel, CapAll):
        return _class_matches(sel.cls, cap_decl)
    if cap.is_reserved:
        return False  # reserved scc.* capabilities are matched only by EXACT or ALL (§17.4.1)
    if isinstance(sel, CapIntegration):
        return sel.integration_id == cap.integration_id and _class_matches(
            sel.cls, cap_decl
        )
    if isinstance(sel, CapCategory):
        return (
            cap_decl is not None
            and cap_decl.category == sel.category
            and _class_matches(sel.cls, cap_decl)
        )
    return False


def _target_matches(grant: Grant, target: ResolvedTarget) -> bool:
    sel = grant.target_selector
    if isinstance(sel, TargetAny):
        return True
    if isinstance(sel, TargetScc):
        return target.kind == "scc"
    if isinstance(sel, TargetSystem):
        return target.kind == "system" and target.system_id == sel.system_id
    if isinstance(sel, TargetComponent):
        return target.kind == "component" and (
            target.system_id,
            target.component_id,
        ) == (sel.system_id, sel.component_id)
    if isinstance(sel, TargetCategory):
        return (
            target.kind != "scc"
            and target.category is not None
            and target.category == sel.category
        )
    return False


def _evaluate_condition(
    cond: Condition,
    now: datetime,
    auth: VerifiedAuthentication | None,
    binding: Binding | None,
    target: ResolvedTarget,
    plan_observed_at: datetime | None,
    at_decision: bool,
) -> bool | str:
    """§17.7. A condition that cannot be evaluated counts as false (A-13)."""
    if isinstance(cond, AuthFresh):
        return auth is not None and now - auth.auth_time <= timedelta(
            seconds=cond.max_age_seconds
        )
    if isinstance(cond, PlatformRole):
        if cond.role != PLATFORM_ADMIN:
            return False  # no other adapter-normalized role is defined in v1
        return binding is not None and binding.latest_confirmed_role == PLATFORM_ADMIN
    if isinstance(cond, PlanMaxAge):
        if not at_decision:
            return (
                "not_applicable"  # applies when the Decision is made (§17.11; step 7)
            )
        return plan_observed_at is not None and now - plan_observed_at <= timedelta(
            seconds=cond.max_age_seconds
        )
    if isinstance(cond, ApprovalRequired):
        return True  # adds APPROVAL; does not restrict matching
    if isinstance(cond, TargetManagementIn):
        return (
            target.management_state is not None
            and target.management_state in cond.states
        )
    return False
