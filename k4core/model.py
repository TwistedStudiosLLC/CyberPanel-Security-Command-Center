"""Locked §17 vocabulary used by the K4 core.

These enumerations transcribe locked state and selector vocabularies; they add no values (§17.1.4, §17.4.1, §17.5.3,
§17.7, §17.19).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum, IntEnum

SCC_NAMESPACE = "scc."
PLATFORM_ADMIN = "PLATFORM_ADMIN"
ADMINISTRATOR_ROLE = "scc.administrator"


class Tier(IntEnum):
    """Risk Tiers R0–R4 (§17.5.3)."""

    R0 = 0
    R1 = 1
    R2 = 2
    R3 = 3
    R4 = 4


class Permission(str, Enum):
    """The closed HUMAN Permission verbs (§17 Terms)."""

    VIEW = "view"
    REQUEST = "request"
    APPROVE = "approve"
    CANCEL = "cancel"


class PrincipalState(str, Enum):
    ACTIVE = "ACTIVE"
    SUSPENDED = "SUSPENDED"
    DISABLED = "DISABLED"
    REVOKED = "REVOKED"


class BindingStatus(str, Enum):
    CONFIRMED = "CONFIRMED"
    UNCONFIRMED = "UNCONFIRMED"
    LOST = "LOST"


class RecordState(str, Enum):
    """Grant and Role Membership state (§17.4.1; §19 lifecycle table)."""

    ACTIVE = "ACTIVE"
    REVOKED = "REVOKED"


class DecisionStatus(str, Enum):
    """Decision status records (§17.19). This slice writes only AWAITING_APPROVAL, AUTHORIZED and INVALIDATED."""

    AWAITING_APPROVAL = "AWAITING_APPROVAL"
    AUTHORIZED = "AUTHORIZED"
    CONSUMED = "CONSUMED"
    EXPIRED = "EXPIRED"
    REVOKED = "REVOKED"
    INVALIDATED = "INVALIDATED"


WRITABLE_DECISION_STATUSES = frozenset(
    {
        DecisionStatus.AWAITING_APPROVAL,
        DecisionStatus.AUTHORIZED,
        DecisionStatus.INVALIDATED,
    }
)

OP_CLASSES = frozenset({"read", "write"})
SELECTOR_CLASSES = frozenset({"read", "write", "any"})


@dataclass(frozen=True)
class CapabilityRef:
    """An Integration capability (`integration_id`, `capability_id`) or a reserved `scc.*` capability.

    Reserved `scc.*` capabilities have no Integration; their ``integration_id`` is None.
    """

    integration_id: str | None
    capability_id: str

    @property
    def is_reserved(self) -> bool:
        return self.integration_id is None and self.capability_id.startswith(
            SCC_NAMESPACE
        )

    @property
    def key(self) -> str:
        return (
            self.capability_id
            if self.integration_id is None
            else f"{self.integration_id}/{self.capability_id}"
        )


# --- Grant selectors (§17.4.1, closed) --------------------------------------------------------------------------


@dataclass(frozen=True)
class CapExact:
    integration_id: str | None
    capability_id: str


@dataclass(frozen=True)
class CapIntegration:
    integration_id: str
    cls: str


@dataclass(frozen=True)
class CapCategory:
    category: str
    cls: str


@dataclass(frozen=True)
class CapAll:
    cls: str


CapabilitySelector = CapExact | CapIntegration | CapCategory | CapAll


@dataclass(frozen=True)
class TargetAny:
    pass


@dataclass(frozen=True)
class TargetSystem:
    system_id: str


@dataclass(frozen=True)
class TargetCategory:
    category: str


@dataclass(frozen=True)
class TargetComponent:
    system_id: str
    component_id: str


@dataclass(frozen=True)
class TargetScc:
    pass


TargetSelector = TargetAny | TargetSystem | TargetCategory | TargetComponent | TargetScc

# --- Conditions (§17.7, closed) -----------------------------------------------------------------------------------


@dataclass(frozen=True)
class AuthFresh:
    max_age_seconds: int


@dataclass(frozen=True)
class PlatformRole:
    role: str


@dataclass(frozen=True)
class PlanMaxAge:
    max_age_seconds: int


@dataclass(frozen=True)
class ApprovalRequired:
    pass


@dataclass(frozen=True)
class TargetManagementIn:
    states: frozenset[str]


Condition = (
    AuthFresh | PlatformRole | PlanMaxAge | ApprovalRequired | TargetManagementIn
)


@dataclass(frozen=True)
class Grant:
    """A Grant (§17.4.1). ``subject_kind`` is "principal" (HUMAN only) or "role" (built-in role_id)."""

    grant_id: str
    subject_kind: str
    subject_id: str
    permission: Permission
    capability_selector: CapabilitySelector
    target_selector: TargetSelector
    max_tier: Tier
    conditions: tuple[Condition, ...] = ()
    valid_from: datetime | None = None
    valid_until: datetime | None = None
    state: RecordState = RecordState.ACTIVE

    def in_validity(self, now: datetime) -> bool:
        if self.valid_from is not None and now < self.valid_from:
            return False
        return self.valid_until is None or now < self.valid_until


@dataclass(frozen=True)
class RoleMembership:
    membership_id: str
    principal_id: str
    role_id: str
    state: RecordState
    valid_from: datetime | None = None
    valid_until: datetime | None = None

    def effective(self, now: datetime) -> bool:
        if self.state is not RecordState.ACTIVE:
            return False
        if self.valid_from is not None and now < self.valid_from:
            return False
        return self.valid_until is None or now < self.valid_until


@dataclass(frozen=True)
class Principal:
    principal_id: str
    state: PrincipalState


@dataclass(frozen=True)
class Binding:
    principal_id: str
    platform_adapter_id: str
    platform_instance_id: str
    platform_subject_id: str
    status: BindingStatus
    status_since: datetime
    latest_confirmed_role: str | None = None


@dataclass(frozen=True)
class GrantSpec:
    """A built-in Role's Grant as defined by the release baseline (§17.3; §17.20)."""

    permission: Permission
    capability_selector: CapabilitySelector
    target_selector: TargetSelector
    max_tier: Tier
    conditions: tuple[Condition, ...] = field(default_factory=tuple)
