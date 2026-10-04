"""Authorization Policy inputs (§17.20) and their evaluation.

The release baseline and the local-settings revision are abstract read-only inputs (DEC-089 D89-7, Q3 as adopted).
K4 consumes them and never writes DC-08 in this slice. An unreadable or invalid revision denies (§17.16).
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass, field
from datetime import timedelta

from .model import SELECTOR_CLASSES, GrantSpec, Permission, Tier

REAUTH = "REAUTH"
APPROVAL = "APPROVAL"
STEP_UP_KINDS = frozenset({REAUTH, APPROVAL})

# A-17: R4 requires REAUTH and APPROVAL; R2 and R3 require REAUTH. The baseline may add, never remove.
_MINIMUM_STEP_UP: Mapping[Tier, frozenset[str]] = {
    Tier.R0: frozenset(),
    Tier.R1: frozenset(),
    Tier.R2: frozenset({REAUTH}),
    Tier.R3: frozenset({REAUTH}),
    Tier.R4: frozenset({REAUTH, APPROVAL}),
}


@dataclass(frozen=True)
class ReleaseBaseline:
    """Release baseline: built-in Roles, tier criteria, default step-up, maximum ages (§17.20)."""

    policy_id: str
    revision: int
    role_grants: Mapping[str, tuple[GrantSpec, ...]]
    default_step_up: Mapping[Tier, frozenset[str]]
    reauth_max_age_seconds: Mapping[Tier, int]
    decision_max_age_seconds: int | None
    plan_max_age_seconds: int | None = None


@dataclass(frozen=True)
class LocalSettings:
    """Local settings: closed and narrowing-only (§17.20)."""

    revision: int
    tier_raises: Mapping[str, Tier] = field(default_factory=dict)
    separation_of_duties_tiers: frozenset[Tier] = frozenset()
    reauth_max_age_seconds: Mapping[Tier, int] = field(default_factory=dict)
    decision_max_age_seconds: int | None = None
    plan_max_age_seconds: int | None = None
    approval_required_tiers: frozenset[Tier] = frozenset()


@dataclass(frozen=True)
class PolicyInputs:
    """The current revisions as read. ``None`` means the revision could not be read."""

    baseline: ReleaseBaseline | None
    local: LocalSettings | None


class PolicyUnavailable(Exception):
    """The policy revision is unreadable or invalid (§17.16)."""


def _shorter(base: int | None, local: int | None) -> int | None:
    if base is None:
        return local
    if local is None:
        return base
    return min(base, local)


@dataclass(frozen=True)
class EffectivePolicy:
    baseline: ReleaseBaseline
    local: LocalSettings

    @property
    def revisions(self) -> dict[str, object]:
        return {
            "policy_id": self.baseline.policy_id,
            "baseline_revision": self.baseline.revision,
            "local_revision": self.local.revision,
        }

    def tier_raise(self, capability_key: str) -> Tier | None:
        return self.local.tier_raises.get(capability_key)

    def step_up(self, tier: Tier) -> frozenset[str]:
        kinds = set(_MINIMUM_STEP_UP[tier]) | set(
            self.baseline.default_step_up.get(tier, frozenset())
        )
        if tier in self.local.approval_required_tiers:
            kinds.add(APPROVAL)
        return frozenset(kinds)

    def reauth_max_age(self, tier: Tier) -> int | None:
        return _shorter(
            self.baseline.reauth_max_age_seconds.get(tier),
            self.local.reauth_max_age_seconds.get(tier),
        )

    @property
    def decision_max_age(self) -> int | None:
        return _shorter(
            self.baseline.decision_max_age_seconds, self.local.decision_max_age_seconds
        )

    @property
    def plan_max_age(self) -> int | None:
        return _shorter(
            self.baseline.plan_max_age_seconds, self.local.plan_max_age_seconds
        )

    def separation_of_duties(self, tier: Tier) -> bool:
        return tier in self.local.separation_of_duties_tiers

    def role_grants(self, role_id: str) -> tuple[GrantSpec, ...]:
        return tuple(self.baseline.role_grants.get(role_id, ()))


def _non_negative(value: object) -> bool:
    return isinstance(value, int) and not isinstance(value, bool) and value >= 0


def _age(value: object) -> bool:
    if not _non_negative(value):
        return False
    try:
        timedelta(seconds=value)  # type: ignore[arg-type]
    except OverflowError:
        return False
    return True


def resolve_policy(inputs: PolicyInputs) -> EffectivePolicy:
    """Validate both revisions; raise PolicyUnavailable if either is unreadable or invalid (§17.16)."""
    base, local = inputs.baseline, inputs.local
    if base is None or local is None:
        raise PolicyUnavailable("policy revision unreadable")
    if not isinstance(base.policy_id, str) or not base.policy_id:
        raise PolicyUnavailable("baseline policy_id invalid")
    for rev in (base.revision, local.revision):
        if not _non_negative(rev):
            raise PolicyUnavailable("policy revision invalid")
    for kinds in base.default_step_up.values():
        if not set(kinds) <= STEP_UP_KINDS:
            raise PolicyUnavailable("baseline step-up outside the closed set")
    ages = list(base.reauth_max_age_seconds.values()) + list(
        local.reauth_max_age_seconds.values()
    )
    ages += [
        a
        for a in (base.decision_max_age_seconds, local.decision_max_age_seconds)
        if a is not None
    ]
    ages += [
        a
        for a in (base.plan_max_age_seconds, local.plan_max_age_seconds)
        if a is not None
    ]
    if not all(_age(a) for a in ages):
        raise PolicyUnavailable("maximum age invalid")
    # Local settings may only shorten maximum ages (§17.20).
    for tier, age in local.reauth_max_age_seconds.items():
        base_age = base.reauth_max_age_seconds.get(tier)
        if base_age is not None and age > base_age:
            raise PolicyUnavailable(
                "local settings may only shorten a baseline maximum age"
            )
    for base_age, age in (
        (base.decision_max_age_seconds, local.decision_max_age_seconds),
        (base.plan_max_age_seconds, local.plan_max_age_seconds),
    ):
        if age is not None and base_age is not None and age > base_age:
            raise PolicyUnavailable(
                "local settings may only shorten a baseline maximum age"
            )
    # APPROVAL_REQUIRED may be added only to tiers below R4 (§17.20).
    if any(t >= Tier.R4 for t in local.approval_required_tiers):
        raise PolicyUnavailable("APPROVAL_REQUIRED may be added only to tiers below R4")
    if not all(isinstance(t, Tier) for t in local.tier_raises.values()):
        raise PolicyUnavailable("tier raise invalid")
    if not all(
        isinstance(t, Tier)
        for t in local.separation_of_duties_tiers | local.approval_required_tiers
    ):
        raise PolicyUnavailable("tier set invalid")
    _validate_role_grants(base.role_grants)
    return EffectivePolicy(base, local)


def _validate_role_grants(role_grants: Mapping[str, tuple[GrantSpec, ...]]) -> None:
    """Built-in Role Grants use only the closed §17.4.1 selectors and §17.7 conditions (A-12, A-13)."""
    from .serialization import (
        EncodingError,
        checked_age,
        encode_condition,
        encode_selector,
    )

    if not isinstance(role_grants, Mapping):
        raise PolicyUnavailable("role grants invalid")
    for role_id, specs in role_grants.items():
        if not isinstance(role_id, str) or not isinstance(specs, tuple):
            raise PolicyUnavailable("role grants invalid")
        for spec in specs:
            if not isinstance(spec, GrantSpec) or not isinstance(spec.max_tier, Tier):
                raise PolicyUnavailable("role grant invalid")
            if not isinstance(spec.permission, Permission) or not isinstance(
                spec.conditions, tuple
            ):
                raise PolicyUnavailable("role grant invalid")
            try:
                for sel in (spec.capability_selector, spec.target_selector):
                    encode_selector(sel)
                    cls = getattr(sel, "cls", "any")
                    if cls not in SELECTOR_CLASSES:
                        raise PolicyUnavailable("selector class outside the closed set")
                for cond in spec.conditions:
                    encode_condition(cond)
                    age = getattr(cond, "max_age_seconds", 0)
                    checked_age(age)
            except (EncodingError, ValueError, OverflowError) as exc:
                raise PolicyUnavailable(f"role grant invalid: {exc}") from exc
