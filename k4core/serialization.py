"""Deterministic encodings (implementation-level representation; DEC-089 D89-17)."""

from __future__ import annotations

import hashlib
import json
import math
from collections.abc import Mapping
from datetime import datetime, timedelta, timezone
from typing import Any

from .model import (
    ApprovalRequired,
    AuthFresh,
    CapAll,
    CapCategory,
    CapExact,
    CapIntegration,
    Condition,
    Grant,
    Permission,
    PlanMaxAge,
    PlatformRole,
    RecordState,
    TargetAny,
    TargetCategory,
    TargetComponent,
    TargetManagementIn,
    TargetScc,
    TargetSystem,
    Tier,
)


class EncodingError(ValueError):
    """Content cannot be encoded deterministically."""


def require_aware(dt: datetime) -> datetime:
    if dt.tzinfo is None or dt.utcoffset() is None:
        raise EncodingError("timestamps must be timezone-aware")
    return dt


def to_iso(dt: datetime | None) -> str | None:
    if dt is None:
        return None
    return require_aware(dt).astimezone(timezone.utc).isoformat()


def from_iso(value: str | None) -> datetime | None:
    """Decode a stored timestamp; stored timestamps are always timezone-aware."""
    if value is None:
        return None
    if not isinstance(value, str):
        raise TypeError("timestamp must be a string")
    dt = datetime.fromisoformat(value)
    if dt.tzinfo is None or dt.utcoffset() is None:
        raise ValueError("stored timestamp is not timezone-aware")
    return dt


def checked_age(value: object) -> int:
    """A maximum age in seconds: a non-negative int representable as a timedelta."""
    if not isinstance(value, int) or isinstance(value, bool) or value < 0:
        raise ValueError("maximum age must be a non-negative integer")
    timedelta(seconds=value)  # raises OverflowError if not representable
    return value


def _str(value: object) -> str:
    if not isinstance(value, str) or not value:
        raise ValueError("expected a non-empty string")
    return value


def _opt_str(value: object) -> str | None:
    return None if value is None else _str(value)


def _canonical_value(value: Any) -> Any:
    if value is None or isinstance(value, (bool, str)):
        return value
    if isinstance(value, int):
        return value
    if isinstance(value, float):
        if math.isnan(value) or math.isinf(value):
            raise EncodingError("non-finite numbers have no canonical encoding")
        return value
    if isinstance(value, datetime):
        return {"$datetime": to_iso(value)}
    if isinstance(value, (list, tuple)):
        return [_canonical_value(v) for v in value]
    if isinstance(value, (set, frozenset)):
        items = [_canonical_value(v) for v in value]
        return {"$set": sorted(items, key=lambda v: json.dumps(v, sort_keys=True))}
    if isinstance(value, Mapping):
        out = {}
        for k, v in value.items():
            if not isinstance(k, str):
                raise EncodingError("mapping keys must be strings")
            out[k] = _canonical_value(v)
        return out
    raise EncodingError(f"unsupported value type {type(value).__name__}")


def canonical_json(value: Any) -> str:
    return json.dumps(
        _canonical_value(value),
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    )


def sha256_hex(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


# --- Grants -----------------------------------------------------------------------------------------------------

_CAP = {
    "EXACT": CapExact,
    "INTEGRATION": CapIntegration,
    "CATEGORY": CapCategory,
    "ALL": CapAll,
}
_TGT = {
    "ANY": TargetAny,
    "SYSTEM": TargetSystem,
    "CATEGORY": TargetCategory,
    "COMPONENT": TargetComponent,
    "SCC": TargetScc,
}


def encode_selector(sel: Any) -> dict:
    for name, cls in {**_CAP, **{"T_" + k: v for k, v in _TGT.items()}}.items():
        if type(sel) is cls:
            return {"type": name, **sel.__dict__}
    raise EncodingError("unknown selector")


_SELECTOR_FIELDS = {
    "EXACT": {"integration_id": _opt_str, "capability_id": _str},
    "INTEGRATION": {"integration_id": _str, "cls": _str},
    "CATEGORY": {"category": _str, "cls": _str},
    "ALL": {"cls": _str},
    "ANY": {},
    "SYSTEM": {"system_id": _str},
    "COMPONENT": {"system_id": _str, "component_id": _str},
    "SCC": {},
}
_TARGET_CATEGORY = {"category": _str}
_CLASSES = frozenset({"read", "write", "any"})


def _decode_selector(d: dict, table: dict, prefix: str = "") -> Any:
    if not isinstance(d, dict) or not isinstance(d.get("type"), str):
        raise TypeError("selector malformed")
    d = dict(d)
    name = d.pop("type")
    if not name.startswith(prefix) or name[len(prefix) :] not in table:
        raise ValueError("unknown selector")
    key = name[len(prefix) :]
    fields = (
        _TARGET_CATEGORY if (prefix and key == "CATEGORY") else _SELECTOR_FIELDS[key]
    )
    if set(d) != set(fields):
        raise ValueError("selector fields malformed")
    values = {k: check(d[k]) for k, check in fields.items()}
    if "cls" in values and values["cls"] not in _CLASSES:
        raise ValueError("selector class outside the closed set")
    return table[key](**values)


def encode_condition(c: Condition) -> dict:
    if isinstance(c, AuthFresh):
        return {"type": "AUTH_FRESH", "max_age_seconds": c.max_age_seconds}
    if isinstance(c, PlatformRole):
        return {"type": "PLATFORM_ROLE", "role": c.role}
    if isinstance(c, PlanMaxAge):
        return {"type": "PLAN_MAX_AGE", "max_age_seconds": c.max_age_seconds}
    if isinstance(c, ApprovalRequired):
        return {"type": "APPROVAL_REQUIRED"}
    if isinstance(c, TargetManagementIn):
        return {"type": "TARGET_MANAGEMENT_IN", "states": sorted(c.states)}
    raise EncodingError("condition outside the closed vocabulary (§17.7)")


def decode_condition(d: dict) -> Condition:
    if not isinstance(d, dict):
        raise TypeError("condition malformed")
    t = d["type"]
    if t == "AUTH_FRESH":
        return AuthFresh(checked_age(d["max_age_seconds"]))
    if t == "PLATFORM_ROLE":
        return PlatformRole(_str(d["role"]))
    if t == "PLAN_MAX_AGE":
        return PlanMaxAge(checked_age(d["max_age_seconds"]))
    if t == "APPROVAL_REQUIRED":
        return ApprovalRequired()
    if t == "TARGET_MANAGEMENT_IN":
        if not isinstance(d["states"], list):
            raise ValueError("states malformed")
        return TargetManagementIn(frozenset(_str(s) for s in d["states"]))
    raise EncodingError("condition outside the closed vocabulary (§17.7)")


def encode_grant(g: Grant) -> dict:
    return {
        "grant_id": g.grant_id,
        "subject_kind": g.subject_kind,
        "subject_id": g.subject_id,
        "permission": g.permission.value,
        "capability_selector": encode_selector(g.capability_selector),
        "target_selector": encode_selector(g.target_selector),
        "max_tier": int(g.max_tier),
        "conditions": [encode_condition(c) for c in g.conditions],
        "valid_from": to_iso(g.valid_from),
        "valid_until": to_iso(g.valid_until),
        "state": g.state.value,
    }


def decode_grant(d: dict) -> Grant:
    if not isinstance(d, dict):
        raise TypeError("grant malformed")
    if d["subject_kind"] not in ("principal", "role"):
        raise ValueError("grant subject kind malformed")
    if not isinstance(d["conditions"], list):
        raise TypeError("grant conditions malformed")
    return Grant(
        grant_id=_str(d["grant_id"]),
        subject_kind=d["subject_kind"],
        subject_id=_str(d["subject_id"]),
        permission=Permission(d["permission"]),
        capability_selector=_decode_selector(d["capability_selector"], _CAP),
        target_selector=_decode_selector(d["target_selector"], _TGT, "T_"),
        max_tier=Tier(d["max_tier"]),
        conditions=tuple(decode_condition(c) for c in d["conditions"]),
        valid_from=from_iso(d["valid_from"]),
        valid_until=from_iso(d["valid_until"]),
        state=RecordState(d["state"]),
    )
