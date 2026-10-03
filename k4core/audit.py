"""§21 audit-record contract for the event kinds DEC-089 authorizes (A1, A2, A4, A6, B1, B2, B3).

Records contain only §21.7 fields (§21.7 last paragraph; §21.20). A3, A5, A7 and B4 are not produced by this slice
(DEC-089 D89-13).
"""

from __future__ import annotations

import uuid
from dataclasses import dataclass
from datetime import datetime
from typing import Any

from .serialization import to_iso

CLASS_A = "A"
CLASS_B = "B"

AUTHORIZED_KINDS = {
    "A1": CLASS_A,
    "A2": CLASS_A,
    "A4": CLASS_A,
    "A6": CLASS_A,
    "B1": CLASS_B,
    "B2": CLASS_B,
    "B3": CLASS_B,
}

# §21.7: the complete record field set. No other field is part of the contract.
CONTRACT_FIELDS = frozenset(
    {
        "audit_id",
        "audit_seq",
        "record_class",
        "event_kind",
        "timestamp",
        "recorded_at",
        "late_recorded",
        "refers_to",
        "actor_type",
        "principal_id",
        "auth_context_ref",
        "lro_auth_ref",
        "authority_basis",
        "capability",
        "action",
        "targets",
        "admissibility_result",
        "conditions",
        "effective_tier",
        "step_up",
        "approval_refs",
        "plan_ref",
        "plan_digest",
        "authorization_ref",
        "decision",
        "reason_code",
        "policy_revisions",
        "revalidation_results",
        "revocation_state",
        "job_id",
        "k6_request_ids",
        "k8_ref",
        "k6_reported_outcome",
        "p3_request_id",
        "condition_kind",
        "count",
        "failure_reason",
        "claimed_assertion_id",
        "named_principal",
        "anchor_digest",
        "observed_at",
        "change_kind",
        "observer",
    }
)

# Fields this slice never sets: their producers or kinds are outside it (DEC-089 D89-13, D89-14).
NOT_PRODUCED = frozenset(
    {
        "late_recorded",
        "refers_to",
        "revalidation_results",
        "job_id",
        "k6_request_ids",
        "k8_ref",
        "k6_reported_outcome",
        "p3_request_id",
    }
)

_COMMON = {"audit_id", "record_class", "event_kind", "timestamp"}
_CLASS_A_REQUIRED = _COMMON | {
    "actor_type",
    "authority_basis",
    "decision",
    "reason_code",
}

REQUIRED = {
    "A1": _CLASS_A_REQUIRED | {"capability", "action", "targets"},
    "A2": _CLASS_A_REQUIRED | {"capability", "action", "targets", "plan_ref"},
    "A4": _CLASS_A_REQUIRED | {"approval_refs", "authorization_ref"},
    "A6": _CLASS_A_REQUIRED | {"lro_auth_ref", "targets"},
    "B1": _COMMON | {"condition_kind", "count"},
    "B2": _COMMON | {"failure_reason"},
    "B3": _COMMON
    | {"named_principal", "anchor_digest", "observed_at", "change_kind", "observer"},
}

ALLOWED = {
    "A1": REQUIRED["A1"]
    | {
        "principal_id",
        "auth_context_ref",
        "admissibility_result",
        "conditions",
        "effective_tier",
        "step_up",
        "policy_revisions",
        "revocation_state",
    },
    "A2": REQUIRED["A2"]
    | {
        "principal_id",
        "auth_context_ref",
        "admissibility_result",
        "conditions",
        "effective_tier",
        "step_up",
        "approval_refs",
        "plan_digest",
        "authorization_ref",
        "policy_revisions",
        "revocation_state",
    },
    "A4": REQUIRED["A4"]
    | {
        "principal_id",
        "plan_ref",
        "plan_digest",
        "capability",
        "action",
        "targets",
        "revocation_state",
    },
    "A6": REQUIRED["A6"] | {"revocation_state"},
    # Denial B1 (§21.12): condition_kind, timestamp, count and its own identity, sequence and recording fields only.
    "B1": REQUIRED["B1"],
    "B2": REQUIRED["B2"] | {"principal_id", "claimed_assertion_id"},
    "B3": REQUIRED["B3"],
}

OBSERVED_BY_K4 = "observed by K4"


class AuditContractError(ValueError):
    """A record would violate the §21 contract; it is never written."""


@dataclass(frozen=True)
class AuditDraft:
    fields: dict[str, Any]


def draft(event_kind: str, timestamp: datetime, **fields: Any) -> AuditDraft:
    if event_kind not in AUTHORIZED_KINDS:
        raise AuditContractError(
            f"event kind {event_kind} is not produced by this slice"
        )
    record = {
        "audit_id": uuid.uuid4().hex,
        "record_class": AUTHORIZED_KINDS[event_kind],
        "event_kind": event_kind,
        "timestamp": to_iso(timestamp),
    }
    for key, value in fields.items():
        if value is not None:
            record[key] = value
    validate(record)
    return AuditDraft(record)


def validate(record: dict[str, Any]) -> None:
    kind = record.get("event_kind")
    if kind not in AUTHORIZED_KINDS:
        raise AuditContractError("unknown event kind")
    keys = set(record) - {"audit_seq", "recorded_at"}
    unknown = keys - CONTRACT_FIELDS
    if unknown:
        raise AuditContractError(
            f"fields outside the §21.7 contract: {sorted(unknown)}"
        )
    produced_elsewhere = keys & NOT_PRODUCED
    if produced_elsewhere:
        raise AuditContractError(
            f"fields not produced by this slice: {sorted(produced_elsewhere)}"
        )
    missing = REQUIRED[kind] - keys
    if missing:
        raise AuditContractError(f"{kind} missing required fields: {sorted(missing)}")
    extra = keys - ALLOWED[kind]
    if extra:
        raise AuditContractError(f"{kind} may not carry: {sorted(extra)}")
    if kind == "B2" and "claimed_assertion_id" in record:
        claimed = record["claimed_assertion_id"]
        if not (
            isinstance(claimed, dict)
            and claimed.get("verified") is False
            and set(claimed) == {"value", "verified"}
        ):
            raise AuditContractError(
                "claimed_assertion_id must be marked unverified (§21.14)"
            )
