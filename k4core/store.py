"""K7 authorization store (SD-K7) for the data classes this slice touches: DC-07 … DC-11.

Representation (DEC-089 D89-17; implementation-level, not architecture): SQLite with ``synchronous=FULL``. A committed
transaction is the durability point for "durably recorded" (§21.11), and one transaction is the atomic unit for R4a
(DEC-034). The store exposes no Grant, Role Membership, Principal-state or DC-08 write: those paths are outside this
slice (DEC-089 D89-10, D89-11).
"""

from __future__ import annotations

import json
import sqlite3
from collections.abc import Callable, Iterator
from contextlib import contextmanager
from datetime import datetime
from typing import Any

from .model import (
    WRITABLE_DECISION_STATUSES,
    Binding,
    BindingStatus,
    DecisionStatus,
    Grant,
    Principal,
    PrincipalState,
    RecordState,
    RoleMembership,
    Tier,
)
from .serialization import decode_grant, from_iso, to_iso

FORMAT_VERSION = "k4core-k7/1"

_SCHEMA = """
CREATE TABLE IF NOT EXISTS meta (key TEXT PRIMARY KEY, value TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS principals (
    principal_id TEXT PRIMARY KEY, state TEXT NOT NULL, created_at TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS bindings (
    principal_id TEXT PRIMARY KEY REFERENCES principals(principal_id),
    platform_adapter_id TEXT NOT NULL, platform_instance_id TEXT NOT NULL, platform_subject_id TEXT NOT NULL,
    status TEXT NOT NULL, status_since TEXT NOT NULL, latest_confirmed_role TEXT,
    UNIQUE (platform_adapter_id, platform_instance_id, platform_subject_id));
CREATE TABLE IF NOT EXISTS role_memberships (
    membership_id TEXT PRIMARY KEY, principal_id TEXT NOT NULL REFERENCES principals(principal_id),
    role_id TEXT NOT NULL, state TEXT NOT NULL, valid_from TEXT, valid_until TEXT);
CREATE TABLE IF NOT EXISTS grants (grant_id TEXT PRIMARY KEY, subject_kind TEXT NOT NULL, subject_id TEXT NOT NULL,
    body TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS plans (
    plan_ref TEXT NOT NULL, plan_digest TEXT NOT NULL, content TEXT NOT NULL, stored_at TEXT NOT NULL,
    PRIMARY KEY (plan_ref, plan_digest));
CREATE TABLE IF NOT EXISTS decisions (
    authorization_ref TEXT PRIMARY KEY, plan_ref TEXT NOT NULL, plan_digest TEXT NOT NULL, body TEXT NOT NULL,
    created_at TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS decision_status (
    status_seq INTEGER PRIMARY KEY AUTOINCREMENT,
    authorization_ref TEXT NOT NULL REFERENCES decisions(authorization_ref), status TEXT NOT NULL, at TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS approval_records (
    approval_id TEXT PRIMARY KEY, authorization_ref TEXT NOT NULL REFERENCES decisions(authorization_ref),
    step_id TEXT NOT NULL, evidence_ref TEXT NOT NULL, approver_principal_id TEXT NOT NULL, recorded_at TEXT NOT NULL,
    UNIQUE (authorization_ref, step_id));
CREATE TABLE IF NOT EXISTS audit (
    audit_seq INTEGER PRIMARY KEY AUTOINCREMENT, audit_id TEXT NOT NULL UNIQUE, record TEXT NOT NULL);
CREATE TRIGGER IF NOT EXISTS audit_no_update BEFORE UPDATE ON audit BEGIN SELECT RAISE(ABORT, 'append-only'); END;
CREATE TRIGGER IF NOT EXISTS audit_no_delete BEFORE DELETE ON audit BEGIN SELECT RAISE(ABORT, 'append-only'); END;
CREATE TRIGGER IF NOT EXISTS decisions_no_update BEFORE UPDATE ON decisions
    BEGIN SELECT RAISE(ABORT, 'immutable'); END;
CREATE TRIGGER IF NOT EXISTS status_no_update BEFORE UPDATE ON decision_status
    BEGIN SELECT RAISE(ABORT, 'append-only'); END;
CREATE TRIGGER IF NOT EXISTS status_no_delete BEFORE DELETE ON decision_status
    BEGIN SELECT RAISE(ABORT, 'append-only'); END;
"""


class K7Unavailable(Exception):
    """K7 could not be read, or a write could not be durably committed."""


class UnsupportedFormat(Exception):
    """SD-K7 content carries a format version this component cannot safely interpret (S19-15)."""


class Transaction:
    """Writes inside one atomic K7 commit. Only the mutations this slice authorizes are exposed."""

    def __init__(self, store: K7Store, cur: sqlite3.Cursor) -> None:
        self._store = store
        self._cur = cur

    # --- DC-11 audit ------------------------------------------------------------------------------------------
    def append_audit(self, record: dict[str, Any]) -> int:
        record = dict(record)
        record["recorded_at"] = to_iso(self._store.clock())
        return self._store._insert_audit(self._cur, record)

    # --- DC-07 -------------------------------------------------------------------------------------------------
    def record_binding_confirmation(
        self, principal_id: str, at: datetime, platform_role: str | None
    ) -> None:
        """DEC-089 Q1: Binding CONFIRMED and the latest confirmed platform role, from a verified context."""
        self._cur.execute(
            "UPDATE bindings SET status = ?, status_since = ?, latest_confirmed_role = ? WHERE principal_id = ?",
            (BindingStatus.CONFIRMED.value, to_iso(at), platform_role, principal_id),
        )
        if self._cur.rowcount != 1:
            raise K7Unavailable("binding not found for confirmation")

    def create_bootstrap_principal(
        self,
        principal_id: str,
        binding: tuple[str, str, str],
        membership_id: str,
        at: datetime,
    ) -> None:
        """§22.4.2: one HUMAN Principal (ACTIVE, no Grants), its Binding UNCONFIRMED(since), one ACTIVE membership."""
        self._cur.execute(
            "INSERT INTO principals (principal_id, state, created_at) VALUES (?, ?, ?)",
            (principal_id, PrincipalState.ACTIVE.value, to_iso(at)),
        )
        self._cur.execute(
            "INSERT INTO bindings (principal_id, platform_adapter_id, platform_instance_id, platform_subject_id,"
            " status, status_since, latest_confirmed_role) VALUES (?, ?, ?, ?, ?, ?, NULL)",
            (principal_id, *binding, BindingStatus.UNCONFIRMED.value, to_iso(at)),
        )
        self._cur.execute(
            "INSERT INTO role_memberships (membership_id, principal_id, role_id, state, valid_from, valid_until)"
            " VALUES (?, ?, 'scc.administrator', ?, NULL, NULL)",
            (membership_id, principal_id, RecordState.ACTIVE.value),
        )

    # --- DC-09 / DC-10 -----------------------------------------------------------------------------------------
    def store_plan(
        self, plan_ref: str, plan_digest: str, content: str, at: datetime
    ) -> None:
        self._cur.execute(
            "INSERT OR IGNORE INTO plans (plan_ref, plan_digest, content, stored_at) VALUES (?, ?, ?, ?)",
            (plan_ref, plan_digest, content, to_iso(at)),
        )

    def create_decision(
        self,
        authorization_ref: str,
        plan_ref: str,
        plan_digest: str,
        body: dict,
        at: datetime,
    ) -> None:
        self._cur.execute(
            "INSERT INTO decisions (authorization_ref, plan_ref, plan_digest, body, created_at) VALUES (?, ?, ?, ?, ?)",
            (
                authorization_ref,
                plan_ref,
                plan_digest,
                json.dumps(body, sort_keys=True),
                to_iso(at),
            ),
        )

    def append_status(
        self, authorization_ref: str, status: DecisionStatus, at: datetime
    ) -> None:
        if status not in WRITABLE_DECISION_STATUSES:
            raise ValueError(
                "this slice does not write that Decision status (DEC-089 D89-10, D89-12)"
            )
        self._cur.execute(
            "INSERT INTO decision_status (authorization_ref, status, at) VALUES (?, ?, ?)",
            (authorization_ref, status.value, to_iso(at)),
        )

    def record_approval(
        self,
        approval_id: str,
        authorization_ref: str,
        step_id: str,
        evidence_ref: str,
        approver: str,
        at: datetime,
    ) -> None:
        self._cur.execute(
            "INSERT INTO approval_records (approval_id, authorization_ref, step_id, evidence_ref,"
            " approver_principal_id, recorded_at) VALUES (?, ?, ?, ?, ?, ?)",
            (
                approval_id,
                authorization_ref,
                step_id,
                evidence_ref,
                approver,
                to_iso(at),
            ),
        )


class K7Store:
    def __init__(self, path: str, clock: Callable[[], datetime]) -> None:
        self.clock = clock
        try:
            self._conn = sqlite3.connect(path, isolation_level=None)
            self._conn.execute("PRAGMA journal_mode=WAL")
            self._conn.execute("PRAGMA synchronous=FULL")
            self._conn.execute("PRAGMA foreign_keys=ON")
            existing = self._conn.execute(
                "SELECT name FROM sqlite_master WHERE type='table' AND name='meta'"
            ).fetchone()
            if existing is None:
                self._conn.execute("BEGIN IMMEDIATE")
                for stmt in _split(_SCHEMA):
                    self._conn.execute(stmt)
                self._conn.execute(
                    "INSERT INTO meta (key, value) VALUES ('format_version', ?)",
                    (FORMAT_VERSION,),
                )
                self._conn.execute("COMMIT")
            row = self._conn.execute(
                "SELECT value FROM meta WHERE key='format_version'"
            ).fetchone()
        except sqlite3.Error as exc:
            self._close_quietly()
            raise K7Unavailable(str(exc)) from exc
        if row is None or row[0] != FORMAT_VERSION:
            self._close_quietly()
            raise UnsupportedFormat(
                f"SD-K7 format version {row[0] if row else None!r} is not {FORMAT_VERSION!r}"
            )

    def _close_quietly(self) -> None:
        conn = getattr(self, "_conn", None)
        if conn is not None:
            try:
                conn.close()
            except sqlite3.Error:
                pass

    def close(self) -> None:
        self._conn.close()

    # --- transactions -------------------------------------------------------------------------------------------
    @contextmanager
    def transaction(self) -> Iterator[Transaction]:
        """One atomic, durable commit. Any failure rolls everything back and raises K7Unavailable."""
        try:
            self._conn.execute("BEGIN IMMEDIATE")
        except sqlite3.Error as exc:
            raise K7Unavailable(str(exc)) from exc
        cur = self._conn.cursor()
        try:
            yield Transaction(self, cur)
            self._conn.execute("COMMIT")
        except BaseException as exc:
            try:
                self._conn.execute("ROLLBACK")
            except sqlite3.Error:
                pass
            if isinstance(exc, (sqlite3.Error, UnicodeError)):
                raise K7Unavailable(str(exc)) from exc
            raise

    def _insert_audit(self, cur: sqlite3.Cursor, record: dict[str, Any]) -> int:
        cur.execute(
            "INSERT INTO audit (audit_id, record) VALUES (?, ?)",
            (record["audit_id"], json.dumps(record, sort_keys=True)),
        )
        seq = cur.lastrowid
        assert seq is not None
        return seq

    # --- reads ---------------------------------------------------------------------------------------------------
    def _query(self, sql: str, args: tuple = ()) -> list[tuple]:
        try:
            return self._conn.execute(sql, args).fetchall()
        except (sqlite3.Error, UnicodeError) as exc:
            raise K7Unavailable(str(exc)) from exc

    def _decode(self, fn: Callable[[], Any]) -> Any:
        """Unreadable authorization state is K7 unavailability (§17.16: denied), never a crash."""
        try:
            return fn()
        except (KeyError, ValueError, TypeError, IndexError, OverflowError) as exc:
            raise K7Unavailable(f"K7 record unreadable: {exc}") from exc

    def find_binding(self, adapter: str, instance: str, subject: str) -> Binding | None:
        rows = self._query(
            "SELECT principal_id, platform_adapter_id, platform_instance_id, platform_subject_id, status,"
            " status_since, latest_confirmed_role FROM bindings WHERE platform_adapter_id=? AND"
            " platform_instance_id=? AND platform_subject_id=?",
            (adapter, instance, subject),
        )
        return self._decode(lambda: _binding(rows[0])) if rows else None

    def binding_of(self, principal_id: str) -> Binding | None:
        rows = self._query(
            "SELECT principal_id, platform_adapter_id, platform_instance_id, platform_subject_id, status,"
            " status_since, latest_confirmed_role FROM bindings WHERE principal_id=?",
            (principal_id,),
        )
        return self._decode(lambda: _binding(rows[0])) if rows else None

    def principal(self, principal_id: str) -> Principal | None:
        rows = self._query(
            "SELECT principal_id, state FROM principals WHERE principal_id=?",
            (principal_id,),
        )
        if not rows:
            return None
        return self._decode(lambda: Principal(rows[0][0], PrincipalState(rows[0][1])))

    def memberships_of(self, principal_id: str) -> list[RoleMembership]:
        rows = self._query(
            "SELECT membership_id, principal_id, role_id, state, valid_from, valid_until FROM role_memberships"
            " WHERE principal_id=? ORDER BY membership_id",
            (principal_id,),
        )
        return self._decode(
            lambda: [
                RoleMembership(
                    r[0], r[1], r[2], RecordState(r[3]), from_iso(r[4]), from_iso(r[5])
                )
                for r in rows
            ]
        )

    def direct_grants_of(self, principal_id: str) -> list[Grant]:
        rows = self._query(
            "SELECT body FROM grants WHERE subject_kind='principal' AND subject_id=? ORDER BY grant_id",
            (principal_id,),
        )
        return [_decode_grant_row(r[0]) for r in rows]

    def any_administrator_membership_record(self) -> bool:
        """§22.3.2: any `scc.administrator` Role Membership record, in any state."""
        return bool(
            self._query(
                "SELECT 1 FROM role_memberships WHERE role_id='scc.administrator' LIMIT 1"
            )
        )

    def decision(self, authorization_ref: str) -> dict | None:
        rows = self._query(
            "SELECT body FROM decisions WHERE authorization_ref=?", (authorization_ref,)
        )
        return self._decode(lambda: _decision_body(rows[0][0])) if rows else None

    def latest_status(self, authorization_ref: str) -> DecisionStatus | None:
        rows = self._query(
            "SELECT status FROM decision_status WHERE authorization_ref=? ORDER BY status_seq DESC LIMIT 1",
            (authorization_ref,),
        )
        return self._decode(lambda: DecisionStatus(rows[0][0])) if rows else None

    def statuses(self, authorization_ref: str) -> list[DecisionStatus]:
        rows = self._query(
            "SELECT status FROM decision_status WHERE authorization_ref=? ORDER BY status_seq",
            (authorization_ref,),
        )
        return self._decode(lambda: [DecisionStatus(r[0]) for r in rows])

    def decisions_for_plan(self, plan_ref: str) -> list[tuple[str, str]]:
        return [
            (r[0], r[1])
            for r in self._query(
                "SELECT authorization_ref, plan_digest FROM decisions WHERE plan_ref=? ORDER BY created_at",
                (plan_ref,),
            )
        ]

    def approved_steps(self, authorization_ref: str) -> set[str]:
        return {
            r[0]
            for r in self._query(
                "SELECT step_id FROM approval_records WHERE authorization_ref=?",
                (authorization_ref,),
            )
        }

    def plan_content(self, plan_ref: str, plan_digest: str) -> str | None:
        rows = self._query(
            "SELECT content FROM plans WHERE plan_ref=? AND plan_digest=?",
            (plan_ref, plan_digest),
        )
        return rows[0][0] if rows else None

    def audit_records(self) -> list[dict[str, Any]]:
        out = []
        for seq, body in self._query(
            "SELECT audit_seq, record FROM audit ORDER BY audit_seq"
        ):
            rec = self._decode(lambda body=body: json.loads(body))
            rec["audit_seq"] = seq
            out.append(rec)
        return out


_DECISION_KEYS = {
    "authorization_ref": str,
    "principal_id": str,
    "plan_ref": str,
    "plan_digest": str,
    "approval_steps": list,
    "steps": dict,
    "plan_tier": str,
    "step_up_tier": str,
    "expires_at": str,
}
_STEP_KEYS = {
    "capability": str,
    "capability_id": str,
    "target_refs": list,
    "targets": list,
}


def _decision_body(raw: str) -> dict:
    """A stored Decision body with the fields K4 relies on, of the right types; else unreadable."""
    body = json.loads(raw)
    if not isinstance(body, dict):
        raise TypeError("decision body malformed")
    for key, kind in _DECISION_KEYS.items():
        if not isinstance(body.get(key), kind):
            raise TypeError(f"decision field {key} malformed")
    for tier_key in ("plan_tier", "step_up_tier"):
        if body[tier_key] not in Tier.__members__:
            raise ValueError("decision tier malformed")
    if not all(isinstance(s, str) for s in body["approval_steps"]):
        raise ValueError("approval_steps malformed")
    for sid in body["approval_steps"]:
        if sid not in body["steps"]:
            raise ValueError("approval step missing from steps")
    for sid, step in body["steps"].items():
        if not isinstance(step, dict):
            raise TypeError("step malformed")
        for key, kind in _STEP_KEYS.items():
            if not isinstance(step.get(key), kind):
                raise TypeError(f"step field {key} malformed")
        if not isinstance(step.get("integration_id"), str):
            raise TypeError("step integration_id malformed")
        if not all(isinstance(x, str) for x in step["target_refs"] + step["targets"]):
            raise ValueError("step targets malformed")
    from_iso(body["expires_at"])
    return body


def _decode_grant_row(body: str) -> Grant:
    """Unreadable Grant state is K7 unavailability (§17.16: denied), never a crash."""
    try:
        return decode_grant(json.loads(body))
    except (KeyError, ValueError, TypeError, OverflowError) as exc:
        raise K7Unavailable(f"grant record unreadable: {exc}") from exc


def _binding(r: tuple) -> Binding:
    return Binding(r[0], r[1], r[2], r[3], BindingStatus(r[4]), from_iso(r[5]), r[6])  # type: ignore[arg-type]


def _split(script: str) -> list[str]:
    """Split the schema into statements, keeping trigger bodies intact."""
    out, buf = [], []
    for line in script.strip().splitlines():
        buf.append(line)
        joined = "\n".join(buf).strip()
        if joined.endswith(";") and (
            not joined.upper().startswith("CREATE TRIGGER") or joined.endswith("END;")
        ):
            out.append(joined)
            buf = []
    return out
