"""Abstract inputs to the K4 authorization core (DEC-089 D89-3, D89-4, D89-5; Q2, Q3, Q6).

Each type represents facts produced by a component this slice does not implement. The types carry facts only, never
an authorization outcome; K4 evaluates the locked rules over them. Their representation is an implementation choice
(DEC-089 D89-17); their meaning is the locked text's. Wrong types are rejected at construction, before K4 sees them;
a Plan proposal is the exception, because step 5 is where K4 validates it.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any

from .model import CapabilityRef, Permission, Tier


def _require(condition: bool, message: str) -> None:
    """Boundary type check: a malformed abstract input is rejected before it reaches K4."""
    if not condition:
        raise TypeError(message)


def _nonempty_str(value: object) -> bool:
    if not isinstance(value, str) or not value:
        return False
    try:
        value.encode("utf-8")
    except UnicodeError:
        return False
    return True


def _opt_str(value: object) -> bool:
    return value is None or _nonempty_str(value)


def _aware(value: object) -> bool:
    return (
        isinstance(value, datetime)
        and value.tzinfo is not None
        and value.utcoffset() is not None
    )


def _str_tuple(value: object) -> bool:
    return isinstance(value, tuple) and all(_nonempty_str(v) for v in value)


def _str_frozenset(value: object) -> bool:
    return isinstance(value, frozenset) and all(_nonempty_str(v) for v in value)


def _tuple_of(value: object, kind: type) -> bool:
    return isinstance(value, tuple) and all(isinstance(v, kind) for v in value)


# ---------------------------------------------------------------------------
# Authentication boundary (§17.22 step 1; §17 Terms; P2/K3 §P.3.2; DEC-089 D89-4, Q1)
# ---------------------------------------------------------------------------

# The §17.22 step-1 assertion checks. A failure result names exactly one of them.
ASSERTION_CHECKS = frozenset({"signature", "audience", "freshness", "single_use"})


@dataclass(frozen=True)
class VerifiedAuthentication:
    """Authentication Context taken from a verified K2 assertion (§17 Terms), plus the P2/K3 §P.3.2 role fact.

    Verification itself is outside this slice (OD19-01; DEC-079 D79-8).
    """

    assertion_id: str
    platform_adapter_id: str
    platform_instance_id: str
    platform_subject_id: str
    auth_time: datetime
    method_claims: tuple[str, ...] = ()
    platform_role: str | None = None

    def __post_init__(self) -> None:
        for name in (
            "assertion_id",
            "platform_adapter_id",
            "platform_instance_id",
            "platform_subject_id",
        ):
            _require(
                _nonempty_str(getattr(self, name)), f"{name} must be a non-empty string"
            )
        _require(_aware(self.auth_time), "auth_time must be a timezone-aware datetime")
        _require(
            _str_tuple(self.method_claims), "method_claims must be a tuple of strings"
        )
        _require(_opt_str(self.platform_role), "platform_role malformed")


@dataclass(frozen=True)
class AuthenticationFailure:
    """A failed §17.22 step-1 assertion check, supplied through the abstract boundary (DEC-089 D89-4)."""

    failed_check: str
    claimed_assertion_id: str | None = None

    def __post_init__(self) -> None:
        _require(_opt_str(self.claimed_assertion_id), "claimed_assertion_id malformed")
        if self.failed_check not in ASSERTION_CHECKS:
            raise ValueError(
                "failed_check must be one of the §17.22 step-1 assertion checks"
            )


AuthenticationResult = VerifiedAuthentication | AuthenticationFailure

# ---------------------------------------------------------------------------
# K11 approver anchors (§17.9; §21.15; DEC-089 D89-3)
# ---------------------------------------------------------------------------

CHANGE_KINDS = frozenset({"added", "revoked", "removed", "modified"})


@dataclass(frozen=True)
class AnchorEntry:
    named_principal: str
    anchor_digest: str

    def __post_init__(self) -> None:
        _require(
            _nonempty_str(self.named_principal),
            "named_principal must be a non-empty string",
        )
        _require(
            _nonempty_str(self.anchor_digest),
            "anchor_digest must be a non-empty string",
        )


@dataclass(frozen=True)
class AnchorChange:
    """A change K4 observed in the read that carries it. K4 supplies the observation time (§21.7)."""

    named_principal: str
    anchor_digest: str
    change_kind: str

    def __post_init__(self) -> None:
        _require(
            _nonempty_str(self.named_principal),
            "named_principal must be a non-empty string",
        )
        _require(
            _nonempty_str(self.anchor_digest),
            "anchor_digest must be a non-empty string",
        )
        if self.change_kind not in CHANGE_KINDS:
            raise ValueError(
                "change_kind must be added, revoked, removed or modified (§21.15)"
            )


@dataclass(frozen=True)
class K11AnchorRead:
    """One K4 read of the authoritative K11 approver anchor set, with the changes observed in that read."""

    anchors: tuple[AnchorEntry, ...]
    changes: tuple[AnchorChange, ...] = ()

    def __post_init__(self) -> None:
        _require(
            _tuple_of(self.anchors, AnchorEntry),
            "anchors must be a tuple of AnchorEntry",
        )
        _require(
            _tuple_of(self.changes, AnchorChange),
            "changes must be a tuple of AnchorChange",
        )


# ---------------------------------------------------------------------------
# K11 capability and scope declarations (§15.7; §16.2.2; DEC-089 D89-5(a))
# ---------------------------------------------------------------------------

OP_CLASS_VALUES = ("read", "write")


@dataclass(frozen=True)
class CapabilityDeclaration:
    capability_id: str
    category: str
    op_class: str  # "read" | "write"
    declared_tier: Tier

    def __post_init__(self) -> None:
        _require(_nonempty_str(self.capability_id), "capability_id malformed")
        _require(_nonempty_str(self.category), "category malformed")
        _require(self.op_class in OP_CLASS_VALUES, "op_class must be read or write")
        _require(isinstance(self.declared_tier, Tier), "declared_tier must be a Tier")


@dataclass(frozen=True)
class ScopeEntry:
    capability_id: str
    op_id: str  # "<family>.<verb>" (§16.1)
    op_major: int
    op_class: str  # "read" | "write"
    resources: frozenset[str]
    handles: frozenset[str] = frozenset()
    executable_semantics: bool = False
    approval_required: bool = False

    def __post_init__(self) -> None:
        _require(_nonempty_str(self.capability_id), "capability_id malformed")
        _require(
            _nonempty_str(self.op_id)
            and self.op_id.count(".") == 1
            and all(self.op_id.split(".")),
            "op_id must be <family>.<verb>",
        )
        _require(
            isinstance(self.op_major, int)
            and not isinstance(self.op_major, bool)
            and self.op_major >= 0,
            "op_major malformed",
        )
        _require(self.op_class in OP_CLASS_VALUES, "op_class must be read or write")
        _require(
            _str_frozenset(self.resources), "resources must be a frozenset of strings"
        )
        _require(_str_frozenset(self.handles), "handles must be a frozenset of strings")
        _require(
            isinstance(self.executable_semantics, bool),
            "executable_semantics must be a bool",
        )
        _require(
            isinstance(self.approval_required, bool), "approval_required must be a bool"
        )

    @property
    def family(self) -> str:
        return self.op_id.split(".", 1)[0]


@dataclass(frozen=True)
class ExecutionDeclaration:
    declaration_id: str  # the integration_id for Integration declarations (§16.2.2)
    declaration_digest: str
    capabilities: tuple[CapabilityDeclaration, ...]
    scope_entries: tuple[ScopeEntry, ...]

    def __post_init__(self) -> None:
        _require(_nonempty_str(self.declaration_id), "declaration_id malformed")
        _require(_nonempty_str(self.declaration_digest), "declaration_digest malformed")
        _require(
            _tuple_of(self.capabilities, CapabilityDeclaration),
            "capabilities malformed",
        )
        _require(_tuple_of(self.scope_entries, ScopeEntry), "scope_entries malformed")


@dataclass(frozen=True)
class K11Declarations:
    declarations: tuple[ExecutionDeclaration, ...]

    def __post_init__(self) -> None:
        _require(
            _tuple_of(self.declarations, ExecutionDeclaration), "declarations malformed"
        )

    def find(self, integration_id: str) -> ExecutionDeclaration | None:
        for d in self.declarations:
            if d.declaration_id == integration_id:
                return d
        return None


# ---------------------------------------------------------------------------
# Inventory target resolution (§17.6; DEC-089 Q2) and admissibility facts (§17.22 step 3; D89-5(b))
# ---------------------------------------------------------------------------

TARGET_KINDS = frozenset({"system", "component", "scc"})


@dataclass(frozen=True)
class ResolvedTarget:
    kind: str
    system_id: str | None = None
    component_id: str | None = None
    category: str | None = None
    management_state: str | None = None

    def __post_init__(self) -> None:
        if self.kind not in TARGET_KINDS:
            raise ValueError("target kind must be system, component or scc (§17.6)")
        for name in ("system_id", "component_id", "category", "management_state"):
            _require(_opt_str(getattr(self, name)), f"{name} malformed")
        if self.kind in ("system", "component"):
            _require(self.system_id is not None, "system_id required")
        if self.kind == "component":
            _require(self.component_id is not None, "component_id required")

    @property
    def key(self) -> str:
        if self.kind == "scc":
            return "scc"
        if self.kind == "system":
            return f"system:{self.system_id}"
        return f"component:{self.system_id}/{self.component_id}"


@dataclass(frozen=True)
class InventoryResolution:
    """Inventory facts resolving requested target references to SCC domain targets at authorization time."""

    targets: Mapping[str, ResolvedTarget]

    def __post_init__(self) -> None:
        _require(
            isinstance(self.targets, Mapping)
            and all(
                _nonempty_str(k) and isinstance(v, ResolvedTarget)
                for k, v in self.targets.items()
            ),
            "targets must map reference strings to ResolvedTarget",
        )


@dataclass(frozen=True)
class AdmissibilityFacts:
    integration_valid: bool
    capability_available: bool
    compatibility_permits: bool
    management_permits: bool

    def __post_init__(self) -> None:
        for name in (
            "integration_valid",
            "capability_available",
            "compatibility_permits",
            "management_permits",
        ):
            _require(isinstance(getattr(self, name), bool), f"{name} must be a bool")

    def holds(self) -> bool:
        return (
            self.integration_valid
            and self.capability_available
            and self.compatibility_permits
            and self.management_permits
        )


@dataclass(frozen=True)
class AdmissibilityInput:
    """Step-3 facts keyed by (capability key, target key)."""

    facts: Mapping[tuple[str, str], AdmissibilityFacts]

    def __post_init__(self) -> None:
        _require(
            isinstance(self.facts, Mapping)
            and all(
                isinstance(k, tuple)
                and len(k) == 2
                and all(_nonempty_str(x) for x in k)
                and isinstance(v, AdmissibilityFacts)
                for k, v in self.facts.items()
            ),
            "facts must map (capability key, target key) to AdmissibilityFacts",
        )


# ---------------------------------------------------------------------------
# Plan proposal (§17.22 step 5; §16.3; DEC-089 D89-5(c)). Validated by K4 at step 5, not here.
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class PlanStep:
    """One K6 request of the Plan, with the (capability, target) pair it realizes (§17.11; §16.3 fields)."""

    step_id: str
    integration_id: str
    capability_id: str
    target_refs: tuple[str, ...]
    op_id: str
    op_major: int
    op_class: str
    declaration_digest: str
    resource_refs: tuple[str, ...] = ()
    selectors: Mapping[str, Any] = field(default_factory=dict)
    params: Mapping[str, Any] = field(default_factory=dict)
    handle_refs: tuple[str, ...] = ()
    expected_state: Any = None
    deadline: datetime | None = None

    @property
    def capability(self) -> CapabilityRef:
        return CapabilityRef(self.integration_id, self.capability_id)


@dataclass(frozen=True)
class PlanProposal:
    plan_ref: str
    steps: tuple[PlanStep, ...]
    newest_input_observation_at: datetime | None = None


# ---------------------------------------------------------------------------
# Action request (the requested invocation evaluated at Phase I)
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class ActionRequest:
    capability: CapabilityRef
    action: str
    target_refs: tuple[str, ...]
    permission: Permission = Permission.REQUEST

    def __post_init__(self) -> None:
        _require(
            isinstance(self.capability, CapabilityRef),
            "capability must be a CapabilityRef",
        )
        _require(
            _nonempty_str(self.capability.capability_id), "capability_id malformed"
        )
        _require(_opt_str(self.capability.integration_id), "integration_id malformed")
        _require(_nonempty_str(self.action), "action must be a non-empty string")
        _require(_str_tuple(self.target_refs), "target_refs must be a tuple of strings")
        _require(isinstance(self.permission, Permission), "permission malformed")


# ---------------------------------------------------------------------------
# Approval-evidence verification result (§17.22 step 10; §16.5; DEC-089 D89-3, Q6)
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class ApprovalVerificationResult:
    """Result of verifying one approval-evidence item, produced outside K4 (no K6 cryptography here).

    ``verifying_anchor_digest`` identifies the anchor whose key verified the signature; K4 checks it against the
    established anchor set and the Principal it names.
    """

    evidence_ref: str
    authorization_ref: str
    step_id: str
    signature_valid: bool
    digest_matches: bool
    verifying_anchor_digest: str | None

    def __post_init__(self) -> None:
        for name in ("evidence_ref", "authorization_ref", "step_id"):
            _require(
                _nonempty_str(getattr(self, name)), f"{name} must be a non-empty string"
            )
        _require(
            isinstance(self.signature_valid, bool), "signature_valid must be a bool"
        )
        _require(isinstance(self.digest_matches, bool), "digest_matches must be a bool")
        _require(
            _opt_str(self.verifying_anchor_digest), "verifying_anchor_digest malformed"
        )


# ---------------------------------------------------------------------------
# P11 bootstrap input (§22.5, §22.6; DEC-089 D89-15)
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class RootDetermination:
    """The OS-enforced peer-identity determination for the P11 channel (§22.5.1). Not P11 request content."""

    caller_is_root: bool
    determination_ref: str

    def __post_init__(self) -> None:
        _require(isinstance(self.caller_is_root, bool), "caller_is_root must be a bool")
        _require(
            _nonempty_str(self.determination_ref),
            "determination_ref must be a non-empty string",
        )
