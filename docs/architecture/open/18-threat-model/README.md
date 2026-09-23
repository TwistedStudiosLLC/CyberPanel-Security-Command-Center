> **Document status:** CONDITIONAL — THREAT MODEL / FORENSIC ARCHITECTURE — NOT FULLY LOCKED
> **Authority category:** 4 — Conditional/open architecture (see [Authority Hierarchy](../../README.md#authority-hierarchy))
> **Source:** DEC-015 (D-3); §18 candidate; §18 architecture gate review; §18 owner-decision gate.
> **Normative:** This summary states the **current status** of §18. It adds no threat-model content of its own.

# §18 Threat Model — Current Status

## Status

**§18 is CONDITIONAL. It is a threat model / forensic architecture section and is NOT FULLY LOCKED** (DEC-015).

- §18 is not deleted.
- §18 is not promoted to locked architecture.
- §18 does not block the one-panel-at-a-time strategy (DEC-016).

## Documents in this folder

| Document | Category | What it is | Authority |
|---|---|---|---|
| [`18-candidate.md`](18-candidate.md) | 4 — Conditional | The §18 candidate text | Conditional. Its own closing "PASS — READY FOR §19" self-assessment is **not** current authority (overridden by the gate review and DEC-015). |
| [`18-gate-review.md`](18-gate-review.md) | 5 — Historical / forensic | The forensic architecture gate review of the candidate | **Not** the current §18 authority. |
| [`18-owner-decision-gate.md`](18-owner-decision-gate.md) | 4 — Open | The owner-decision record for ODF-18-01 … ODF-18-09 | Records the questions and options. Dispositions are recorded in the decision log, not edited into this file. |

Current §18 status is established by the [architecture index](../../README.md), the
[decision log](../../decisions/decision-log.md) and the [open register](../register.md).

## Owner-decision dispositions

| ODF | Title | Current disposition | Source |
|---|---|---|---|
| ODF-18-01 | Presentation origin model | **DISPOSITIONED:** deferred to the Platform/K2 gate for each concrete platform. For CyberPanel: → CyberPanel K2 / Platform Adapter gate. SCC Core makes no universal presentation-origin claim. | DEC-015 |
| ODF-18-02 | Cross-instance approval replay | OPEN | DEC-015 |
| ODF-18-03 | K6 enforcement of R4 `approval_required` | OPEN | DEC-015 |
| ODF-18-04 | Credential-derived argument slots | OPEN | DEC-015 |
| ODF-18-05 | WRITE resource ownership | OPEN | DEC-015 |
| ODF-18-06 | Request-bound assertions | OPEN | DEC-015 |
| ODF-18-07 | Off-host audit export (option and mechanism) | OPEN | DEC-015 |
| ODF-18-08 | Minimum approval-key custody | OPEN | DEC-015 |
| ODF-18-09 | Platform-configuration writes | OPEN | DEC-015 |

## Pending work before §18 can lock

- Dispositions for ODF-18-02 … ODF-18-09.
- A canonical §18 rewrite applying the gate review's recommended corrections RC-01 … RC-21 and the recorded decision
  consequences.
- The §18 lock conditions listed in §13 of [`18-owner-decision-gate.md`](18-owner-decision-gate.md) were written
  before DEC-015. Conditions 1 and 2 (deciding ODF-18-01 and authorizing a §15 amendment) are affected by DEC-015,
  which dispositioned ODF-18-01 to the per-platform K2 gates. How the lock conditions are restated in light of
  DEC-015 has **not** been decided and is recorded as an open item in the [open register](../register.md).

> **Note (index text, not a decision):** DEC-015 states "Do not resolve ODF-18-01 by weakening §15." The
> owner-decision gate document's statement that ODF-18-01 "requires a §15 amendment" under every option was written
> before DEC-015. Whether the CyberPanel K2 gate's conforming arrangement needs any §15 text change is an open
> question for that gate (KF-01, KF-02).
