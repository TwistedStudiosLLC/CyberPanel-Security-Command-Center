# SCC Architecture Index & Authority Hierarchy

> **Document status:** CURRENT — architecture index (normative for authority and status)
> **Establishes:** the authority hierarchy (DEC-023 / D-11), the baseline override rule (DEC-014 / D-1), and
> the current status of every architecture section.
> **Rule:** If a document's own header or text claims a status that differs from this index, **this index
> and the decision log control.**

---

## Authority Hierarchy

The following hierarchy is recorded verbatim from owner decision D-11 (DEC-023):

```text
The hierarchy is:

    1. Locked architecture
       §15, §16, §17

    2. Explicit owner decisions
       decisions that constrain implementation

    3. Current foundational principles
       original §1–§14 material that remains compatible

    4. Conditional/open architecture
       §18, §19, §20, §21, §22 and other explicitly open gates

    5. Historical / forensic material
       previous candidates, audits, rejected alternatives

When documents conflict, the higher authoritative category wins.

A historical document must never silently override a locked
architecture document.
```

### Baseline override rule (DEC-014 / D-1)

```text
    Earlier principle
        +
    later locked architecture
        =
    later locked architecture controls
```

The original §1–§14 baseline is **FOUNDATIONAL / CURRENT WITH OVERRIDES**. It is neither wholly authoritative
nor wholly obsolete. Statements in the baseline that carry no annotation are CURRENT FOUNDATIONAL PRINCIPLES,
subject to this override rule. Annotated statements carry one of:

| Annotation class | Meaning (per D-1) |
|---|---|
| CURRENT FOUNDATIONAL PRINCIPLE / CURRENT-REFINED | Still valid and compatible with §15–§17 (refined where noted) |
| SUPERSEDED | Replaced by a later architectural decision |
| HISTORICAL | Retained for architectural history but no longer normative |
| OPEN | Not yet resolved by a later gate |

---

## Document Map and Status

### Category 1 — Locked architecture

| Document | Status | Source |
|---|---|---|
| [`current/15-runtime-topology.md`](current/15-runtime-topology.md) | **LOCKED** | §15 approved text (DEC-001, DEC-022) |
| [`current/16-privileged-execution.md`](current/16-privileged-execution.md) | **LOCKED** | §16 revised text with Decisions A/B/C, X-01…X-39 (DEC-007, DEC-022) |
| [`current/17-authorization.md`](current/17-authorization.md) | **LOCKED** | §17 final text with A-01…A-36 (DEC-012, DEC-022) |

The locked documents contain no inline commentary. Their terminology is defined in their own Terms sections
(§16 Terms, §17 Terms) and in the §15.3 component catalogue. **No separate glossary exists**, so that no second
set of definitions can compete with the locked text.

### Category 2 — Owner decisions

| Document | Status |
|---|---|
| [`decisions/decision-log.md`](decisions/decision-log.md) | **CURRENT — OWNER DECISIONS** (DEC-001 … DEC-030) |

### Category 3 — Foundational principles

| Document | Status |
|---|---|
| [`baseline/foundational-01-14.md`](baseline/foundational-01-14.md) | **FOUNDATIONAL / CURRENT WITH OVERRIDES** (original text + delimited annotations ANN-01…ANN-32) |

### Category 4 — Conditional / open architecture

| Document | Status |
|---|---|
| [`open/18-threat-model/README.md`](open/18-threat-model/README.md) | **CONDITIONAL — THREAT MODEL / FORENSIC ARCHITECTURE — NOT FULLY LOCKED** (current §18 status summary) |
| [`open/18-threat-model/18-candidate.md`](open/18-threat-model/18-candidate.md) | CONDITIONAL — candidate text — NOT CURRENT AUTHORITY |
| [`open/18-threat-model/18-owner-decision-gate.md`](open/18-threat-model/18-owner-decision-gate.md) | OPEN — decision record (ODF-18-01 dispositioned by DEC-015; ODF-18-02…09 OPEN) |
| [`open/register.md`](open/register.md) | OPEN QUESTIONS REGISTER |
| [`open/19-persistence-secrets-data-lifecycle.md`](open/19-persistence-secrets-data-lifecycle.md) | CANDIDATE — OWNER REVIEW REQUIRED — NOT LOCKED |
| [`open/20-reconciliation-desired-state-drift.md`](open/20-reconciliation-desired-state-drift.md) | NOT DESIGNED — GATE PENDING |
| [`open/21-audit-events.md`](open/21-audit-events.md) | NOT DESIGNED — GATE PENDING |
| [`open/22-lifecycle-recovery.md`](open/22-lifecycle-recovery.md) | NOT DESIGNED — GATE PENDING |
| [`open/p2-protocol.md`](open/p2-protocol.md) | NOT DESIGNED — GATE PENDING |
| [`../platforms/cyberpanel/k2-gate.md`](../platforms/cyberpanel/k2-gate.md) | OPEN — CyberPanel K2 gate |

### Category 5 — Historical / forensic material

| Document | Status |
|---|---|
| [`open/18-threat-model/18-gate-review.md`](open/18-threat-model/18-gate-review.md) | HISTORICAL / FORENSIC — **not** current §18 authority |
| [`history/forensic-audit.md`](history/forensic-audit.md) | HISTORICAL / FORENSIC |
| [`history/phase-a-report.md`](history/phase-a-report.md) | HISTORICAL |
| [`history/reconciliation-report.md`](history/reconciliation-report.md) | HISTORICAL |
| [`history/superseded-register.md`](history/superseded-register.md) | HISTORICAL INDEX — NON-NORMATIVE |

### Evidence (non-normative)

| Document | Status |
|---|---|
| [`../platforms/cyberpanel/reconnaissance.md`](../platforms/cyberpanel/reconnaissance.md) | EVIDENCE — NON-NORMATIVE (platform facts, not SCC architecture) |

---

## Section Status

| Section | Title | Status | Where |
|---|---|---|---|
| §1–§14 | Original baseline | FOUNDATIONAL / CURRENT WITH OVERRIDES | `baseline/` |
| §15 | Runtime Topology & Trust Boundaries | **LOCKED** | `current/` |
| §16 | Privileged Execution Contract | **LOCKED** | `current/` |
| §17 | Authorization Model | **LOCKED** | `current/` |
| §18 | Threat Model | **CONDITIONAL — NOT FULLY LOCKED** | `open/18-threat-model/` |
| §19 | Persistence, Secrets & Data Lifecycle | CANDIDATE — OWNER REVIEW REQUIRED — NOT LOCKED | `open/` |
| §20 | Reconciliation / Desired State / Drift | NOT DESIGNED — GATE PENDING | `open/` |
| §21 | Audit / Events | NOT DESIGNED — GATE PENDING | `open/` |
| §22 | Lifecycle / Recovery | NOT DESIGNED — GATE PENDING | `open/` |
| P2 | K2 ↔ K3 protocol | NOT DESIGNED — GATE PENDING | `open/p2-protocol.md` |
| CyberPanel K2 | CyberPanel platform gate | OPEN | `platforms/cyberpanel/k2-gate.md` |

---

## Dependency Order

Architecture gates (DEC-024 / D-12):

```text
    §19
      ↓
    §21
      ↓
    §22
```

§20 proceeds according to its own dependencies. It is required before capabilities that rely on
reconciliation/drift. It does not block the initial identity slice unless an actual dependency is demonstrated.

Implementation phases (DEC-025 / D-13):

```text
PHASE 1   Commit architecture source-of-truth.
PHASE 2   Design §19.
PHASE 3   Design §21.
PHASE 4   Design §22 / recovery/lifecycle as required.
PHASE 5   Establish the K3/P2 service boundary.
PHASE 6   Implement the minimum SCC Core required by the locked
          contracts and completed persistence/audit/lifecycle gates.
PHASE 7   CyberPanel K2 gate.
PHASE 8   CyberPanel K2 implementation.
PHASE 9   Identity binding.
PHASE 10  CyberPanel presentation integration.
PHASE 11  Capability implementation.
```

Prohibited implementation at this stage: see DEC-029 (D-17). No generic `execute` / `run` / `shell` /
`subprocess` / `exec_as_root` abstraction may ever be created (§16 X-02, X-03, X-11).

---

## Known Findings Against Locked Text

The locked documents are **not** edited to record findings (DEC-030, Q2). The following findings concern
locked text. Each one is **open**. None of them modifies the locked text unless a future gate explicitly
authorizes an amendment.

| ID | Locked text concerned | Finding | Source | Status / owner |
|---|---|---|---|---|
| KF-01 | §15.6 compromised-K3 bound; §15.18 OQ-1 ("Both satisfy §15") | The bound can be false under same-origin presentation | §18 gate review TF-18-02 | OPEN — CyberPanel K2 gate (DEC-015, DEC-027) |
| KF-02 | §15.6 Presentation Adapter placed in K3; K3 serves UI assets | Tension with a CyberPanel-native K2 presentation surface | Reconciliation D-2; D-15 | OPEN — CyberPanel K2 gate (DEC-027) |
| KF-03 | §15 T-24 (no parent-platform core-file modification) | The upstream CyberPanel plugin installer edits core files | Phase A STOP-3; reconciliation D-5 | OPEN — CyberPanel K2 gate (DEC-017); T-24 **not** amended |
| KF-04 | §16.5 approval digest (no instance identity) | Cross-instance approval replay | §18 gate review TF-18-03 | OPEN — ODF-18-02 |
| KF-05 | §16.2 / A-23 `approval_required` authoring rule | Omission not mechanically detected at K6 | TF-18-04 | OPEN — ODF-18-03 |
| KF-06 | §16.1.5 `handle_ref` permitted in argument slots | Credential exposure via process arguments (Host-Environment dependent) | TF-18-06 | OPEN — ODF-18-04 |
| KF-07 | §16 X-13 (resource resolution; no ownership check) | WRITE resources under non-root-writable paths | TF-18-05 | OPEN — ODF-18-05 |
| KF-08 | §15.4 item 6 / §16.1.3 (no general egress) | Off-host audit export has no mechanism in locked text | §18 owner-decision gate §8 | OPEN — ODF-18-07 |
| KF-09 | §16.2 `executable_semantics` definition ("the Security System") | Platform-configuration writes fall outside the definition | TF-18-10 | OPEN — ODF-18-09 |
| KF-10 | §17.21 statement on compromised K1/K2 | Holds only for the SCC-interface path; K1/K2 are root-equivalent | §18 gate review CF-18-07 | OPEN — §18 (conditional) |

Full question inventory: [`open/register.md`](open/register.md).

---

## Status Header Convention

Every document in `docs/` begins with a status header in a blockquote that states: document status, authority
category, source, whether the content is normative, and any transcription notes. The status header is
**non-normative front matter**. In locked documents it adds no architectural content.
