> **Document status:** HISTORICAL INDEX — NON-NORMATIVE
> **Authority category:** 5 — Historical / forensic material (see [Authority Hierarchy](../README.md#authority-hierarchy))
> **What this is:** An index of superseded, rejected and never-approved architecture material, with the current
> source that replaced it. It exists so that superseded material cannot be mistaken for current architecture.
> **Normative:** No. The "Replaced by" column points to the controlling source; read that source.

# Superseded & Non-Authoritative Material Register

## 1. Superseded concepts

Entries C-1 … C-15 originate in the [reconciliation report](reconciliation-report.md) §C. The "Current pointer"
column adds the decision-log entries recorded afterwards.

| ID | Item | Where it appeared | Classification | Replaced by / current pointer |
|---|---|---|---|---|
| C-1 | "Execution occurs through the Integration" | Baseline §6 | SUPERSEDED | §15.8; §16 (T-05, T-06, X-11); baseline ANN-10 |
| C-2 | "Integration isolation is mandatory" with no boundary defined | Baseline §2, §14 | SUPERSEDED | §15.8; baseline ANN-04 |
| C-3 | "Privileged work through a controlled worker/mechanism" | Baseline §9 | SUPERSEDED | §15.9; §16; baseline ANN-15 |
| C-4 | A single "Platform Adapter" component | Baseline §11, §13.55.5 | SUPERSEDED | §15.3 split (K2, Presentation Adapter, Platform Services); baseline ANN-21 |
| C-5 | A universal Parent Theme / Presentation Contract across platforms | Baseline §13.55 | HISTORICAL (as a universal design); per-platform question OPEN | DEC-015, DEC-016, DEC-027; baseline ANN-24 |
| C-6 | "Externally supplied / locally developed Integrations" | Baseline §14 | SUPERSEDED (for v1) | T-22; baseline ANN-26 |
| C-7 | Integration metadata field "supported CyberPanel versions" | Baseline §2, §14 | SUPERSEDED; replacement OPEN | T-27; DEC-016; baseline ANN-03, ANN-29 |
| C-8 | A recovery mode that includes a web UI | Baseline §12, §13 | SUPERSEDED; recovery OPEN | T-29; A-07; DEC-021; baseline ANN-22 |
| C-9 | First §16 candidate wording (see NA-2) | §16 first candidate | SUPERSEDED — NEVER APPROVED | Locked §16 (X-05, CF-5) |
| C-10 | Pre-clarification §17 candidate (see NA-3) | §17 candidate | SUPERSEDED — NEVER APPROVED | Locked §17 (A-05) |
| C-11 | Phase A STOP-2 option (b): a time-limited §15 deviation letting K3/K4 run inside CyberPanel | [Phase A report](phase-a-report.md) | **REJECTED** | DEC-016, DEC-018; §15 T-01, T-04 |
| C-12 | "System Control Contract" as the product name | Superseded implementation brief (IB-1) | SUPERSEDED | DEC-013 |
| C-13 | SCC Principal, authorization and UI delivered as a CyberPanel Django integration | Superseded implementation brief (IB-1) | SUPERSEDED | DEC-016, DEC-018, DEC-025, DEC-027, DEC-028 |
| C-14 | Forensic Architectural Audit | [`forensic-audit.md`](forensic-audit.md) | HISTORICAL | §15–§17; unabsorbed changes indexed in [`../open/register.md`](../open/register.md) §7 |
| C-15 | §18 candidate, §18 gate review, §18 owner-decision gate | [`../open/18-threat-model/`](../open/18-threat-model/README.md) | Candidate: CONDITIONAL. Gate review: HISTORICAL. Owner-decision gate: OPEN. | DEC-015 |

## 2. Never-approved candidate texts (register entries only)

Per DEC-030 (Q7), these texts are **not** reproduced in the repository. They are **NEVER APPROVED /
NON-AUTHORITATIVE**. The locked documents are the only authoritative versions (DEC-022).

| ID | Candidate | Status | Main differences from the locked text | Authoritative version |
|---|---|---|---|---|
| NA-1 | §15: no separate never-approved candidate text exists. The single §15 text was approved unchanged (DEC-001). The *starting-hypothesis diagram* in the §15 gate brief (CyberPanel → SCC Web / Platform Adapter → SCC Core → Integration Host / Privileged Executor → Host) was an input, not a candidate. | NEVER APPROVED / NON-AUTHORITATIVE (the hypothesis diagram) | §15.3.1 records seven defects (H-1 … H-7) in that hypothesis | [`../current/15-runtime-topology.md`](../current/15-runtime-topology.md) |
| NA-2 | First §16 candidate | **NEVER APPROVED / NON-AUTHORITATIVE** | "One request produces at most one invocation" (replaced by X-05, DEC-003); profile deny rule based on a binary's documented purpose without Approved Executable Identity (replaced by X-03, X-34, DEC-004); Core Discovery's declaration left as clarification C-1 (decided by DEC-002); Platform Services filed under Integration Declarations (replaced by CF-5, DEC-006) | [`../current/16-privileged-execution.md`](../current/16-privileged-execution.md) |
| NA-3 | Pre-clarification §17 candidate | **NEVER APPROVED / NON-AUTHORITATIVE** | SYSTEM's revocation-triggered cancellation was not distinguished from the HUMAN `cancel` Permission (replaced by the Fixed System Authority clarification, A-05) | [`../current/17-authorization.md`](../current/17-authorization.md) |

## 3. Superseded implementation brief (summary only)

Per DEC-030 (Q6), the brief is summarized here and **not** copied.

| ID | Summary | Status | Replaced by |
|---|---|---|---|
| IB-1 | The first CyberPanel implementation brief. It referred to SCC as "System Control Contract". It asked for a first vertical slice delivered as a CyberPanel-native Django route and SCC-owned UI inside CyberPanel, with CyberPanel identity mapped to an SCC Principal and SCC authorization established through the CyberPanel integration, plus tests, CI, an installer and a pull request. It also set rules that remain consistent with current architecture (no generic shell or command execution, no privileged operations in the first slice, GitHub as source of truth). | **SUPERSEDED** | The architecture reconciliation message and DEC-013, DEC-016, DEC-018, DEC-025, DEC-027, DEC-028. Rules that remain valid are carried by the locked sections and DEC-029, not by the brief. |

## 4. Baseline annotations

Superseded, historical and open statements inside the original §1–§14 are annotated in place in
[`../baseline/foundational-01-14.md`](../baseline/foundational-01-14.md) (ANN-01 … ANN-32; index at the end of that
document).
