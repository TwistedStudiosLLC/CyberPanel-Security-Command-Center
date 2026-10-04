> **Document status:** OPEN QUESTIONS REGISTER
> **Authority category:** 4 — Conditional/open architecture (see [Authority Hierarchy](../README.md#authority-hierarchy))
> **Source:** §15.18, §16.15, §17.24, §18 (candidate, gate review, owner-decision gate), the forensic audit change
> list, and the owner decision log.
> **Normative:** No. This register indexes open items and where they are owned. **For items addressed by later
> sections it gives pointers only; it does not restate or paraphrase the answer.** The pointed-to section controls.

# Open Questions Register

**Status values**

| Status | Meaning |
|---|---|
| OPEN | Not yet resolved. The owning gate is named. |
| DISPOSITIONED | The owner assigned the question to a named gate; the question itself is still open there. |
| PARTIAL | Part of the question is addressed by the cited section; the remainder is OPEN at the named gate. |
| ADDRESSED | Addressed by the cited section. Pointer only — read the cited section. |
| REJECTED (as a finding) | The review determined that the alleged finding is not a defect against locked architecture. Related open questions remain listed separately (DEC-064). |

---

## 1. Known findings against locked text

See [Known Findings Against Locked Text](../README.md#known-findings-against-locked-text) (KF-01 … KF-10) in the
architecture index. They are open and are not repeated here.

---

## 2. §15.18 open questions

| ID | Subject (as titled in §15.18) | Status | Pointer / owner |
|---|---|---|---|
| OQ-1 | Browser → K3 path through CyberPanel's extension mechanism | **OPEN** | CyberPanel K2 gate (DEC-015, DEC-017, DEC-027); KF-01, KF-02, KF-03 |
| OQ-2 | K6 splitting, privilege reduction, request schema, idempotency, K8 content | ADDRESSED | §16.3, §16.10, §16.11, §16.13 |
| OQ-3 | Principal model; platform role facts; revalidation; assertion format and lifetime | PARTIAL | Addressed: §17.1, §17.2, §17.13. Assertion format and lifetime: OPEN — P2 protocol gate (DEC-026) |
| OQ-4 | Approval evidence verifiable without trusting K4 | PARTIAL | Addressed: §16.5 (interface), §17.8, §17.9 (policy). Key custody: OPEN — P-1, ODF-18-08 |
| OQ-5 | Tamper evidence for K7 audit and K8; off-host export; audit fail-closed policy | **OPEN** | §19 / §21; TQ-04; ODF-18-07 |
| OQ-6 | K9 authority; K9 → K6; K2 key provisioning; K11 installer placement | **OPEN** | Recovery gate / §22; §19 DC-01/DC-02 R4 owner depends on it (DEC-066) |
| OQ-7 | Distinct OS identity per Integration | **OPEN** (deferred) | Deferred until non-built-in Integrations are proposed (§15.8, T-22) |
| OQ-8 | Hosts without per-service identity support | **OPEN** | §12 Host Environment compatibility (no gate scheduled) |

---

## 3. §16.15 open questions

| ID | Subject | Status | Pointer / owner |
|---|---|---|---|
| Q-1 | Which scope entries require approval evidence; approver keys; anchor provisioning and revocation | PARTIAL | Addressed: §17.8, §17.9, A-23. Anchor provisioning mechanics: OPEN — §22. Key custody: P-1 |
| Q-2 | Credential storage, provisioning, rotation; pre-image retention; K8 retention | **OPEN** | §19 |
| Q-3 | K8 tamper evidence; K8 ↔ K4 audit comparison; off-host export | **OPEN** | §18 / §19 / §21; TQ-04; ODF-18-07 |
| Q-4 | Whether K9 may call K6 directly | **OPEN** | Recovery gate |
| Q-5 | Who edits the Host Restriction Overlay and package-source allowlist | **OPEN** | §22 / recovery gate |
| Q-6 | Job states that consume K6 outcomes | **OPEN** | §8 amendment (forensic audit CHANGE-007); no gate scheduled |
| Q-7 | Declaration refresh after external upgrades; PACKAGE_ATTESTED qualification | **OPEN** | §22 (refresh); §12 Host Environment (qualification) |

---

## 4. §17.24 open questions

| ID | Subject | Status | Pointer / owner |
|---|---|---|---|
| P-1 | Approver key custody; approval-tool mechanics | **OPEN** | §18 (threat) / §22 (mechanics); ODF-18-08; TQ-01 |
| P-2 | Service principals / API automation | **OPEN** (deferred) | Future gate |
| P-3 | Multi-tenant platform roles | **OPEN** (deferred) | Future gate; DEC-011 |
| P-4 | K6-verifiable multi-party approval | **OPEN** (deferred) | Would require a §16 amendment |
| P-5 | K9 authority over authorization state beyond bootstrap | **OPEN** | Recovery gate; DEC-021 |
| P-6 | Per-adapter platform subject stability (CyberPanel) | **OPEN** | CyberPanel K2 gate; TQ-03 |
| P-7 | Delegation, custom Roles, authorization caching, environmental conditions | **OPEN** (deferred by decision) | §17.15, §17.17, §17.7 |
| P-8 | Audit noise control for view decisions | **OPEN** | §21 |

---

## 5. §18 items

§18 is CONDITIONAL — NOT FULLY LOCKED (DEC-015). See [`18-threat-model/README.md`](18-threat-model/README.md).

### 5.1 Owner decisions (ODF)

| ID | Subject | Status | Pointer / owner |
|---|---|---|---|
| ODF-18-01 | Presentation origin model | **DISPOSITIONED** | Per-platform K2 gate; for CyberPanel: CyberPanel K2 gate (DEC-015) |
| ODF-18-02 | Cross-instance approval replay | **OPEN** | Owner decision; possible §16 amendment (OD-1) |
| ODF-18-03 | K6 enforcement of R4 `approval_required` | **OPEN** | Owner decision; possible §16 amendment (OD-2) |
| ODF-18-04 | Credential-derived argument slots | **OPEN** | Owner decision; possible §16 amendment (OD-3) |
| ODF-18-05 | WRITE resource ownership | **OPEN** | Owner decision; possible §16 amendment (OD-5) |
| ODF-18-06 | Request-bound assertions | **OPEN** | Owner decision; Platform Adapter / P2 |
| ODF-18-07 | Off-host audit export (option and mechanism) | ADDRESSED | DEC-072 (B, iii) |
| ODF-18-08 | Minimum approval-key custody | **OPEN** | Owner decision; §22 |
| ODF-18-09 | Platform-configuration writes | **OPEN** | Owner decision; possible §16 clarification |

### 5.2 Open questions from the §18 candidate (TQ)

| ID | Subject | Status | Pointer / owner |
|---|---|---|---|
| TQ-01 | Approver key custody / approval environment | **OPEN** | §22; P-1; ODF-18-08 |
| TQ-02 | K9 recovery authority | **OPEN** | Recovery gate; P-5 |
| TQ-03 | CyberPanel subject stability | **OPEN** | CyberPanel K2 gate; P-6 |
| TQ-04 | Audit tamper evidence, sequencing, export | **OPEN** | §19 / §21 |
| TQ-05 | Request-bound assertions | **OPEN** | ODF-18-06; Platform Adapter gate |
| TQ-06 | Release-key custody and rollback protection | **OPEN** | §22; OD-4 |
| TQ-07 | Pre-image visibility for approvers of `file.replace` | **OPEN** | §22 |
| TQ-08 | K7 restore rollback detection | **OPEN** | §19 / recovery gate; F19-09 (DEC-062 F09d) |
| TQ-09 | K8 capacity isolation (and, per the gate review, volume displacement) | **OPEN** | §19; Q19-05 (DEC-065) |
| TQ-10 | Presentation isolation mechanism | **OPEN** | Per-platform K2 gate (see ODF-18-01 disposition) |

### 5.3 Other §18 open work

| ID | Subject | Status | Pointer / owner |
|---|---|---|---|
| §18-RC | Recommended corrections RC-01 … RC-21 to the candidate | **OPEN** | Canonical §18 rewrite (not scheduled); [`18-gate-review.md`](18-threat-model/18-gate-review.md) §20 |
| §18-LOCK | Restating the §18 lock conditions in light of DEC-015 | **OPEN** | Owner; [`18-owner-decision-gate.md`](18-threat-model/18-owner-decision-gate.md) §13 |

---

## 5A. §19 candidate items (pointers only)

§19 is LOCKED (DEC-075). Its open items are listed here as pointers; the §19 document is the source. Items recorded
as OPEN or DEFERRED in §19.21–§19.22 are resolved through the route in DEC-075 D75-3. See
[`19-persistence-secrets-data-lifecycle.md`](../current/19-persistence-secrets-data-lifecycle.md).

| ID | Subject | Status | Pointer / owner |
|---|---|---|---|
| OD19-01 | Placement and provisioning of assertion verification material | **OPEN** | §19.21; DEC-051; §19, coordinated with P2, §22, CyberPanel K2 gate |
| OD19-02 | At-rest encryption inside host storage domains; key hierarchy | **OPEN** | §19.21; DEC-052; §19 Owner Decision Gate; §22 |
| OD19-03 | Whether a maximum approval-validity horizon exists; its value and enforcement point | **OPEN** | §19.21; DEC-053; §19 Owner Decision Gate; §16 Amendment Gate / §22 as applicable |
| OD19-04 | Credential-bearing file content through `file.replace` (F19-05) | ADDRESSED | §19.21; DEC-054; DEC-070 (Path A) |
| OD19-05 | How K4 learns credential-handle provisioning state (F19-07) | **OPEN** | §19.21; DEC-055; §16 Amendment Gate / §22 |
| OD19-06 | Health and evidence history retention | **OPEN** | §19.21; DEC-056; **§19**; §21 and §20 dependency inputs |
| OD19-07 | Pre-image retention bounds in K11 content | **OPEN** | §19.21; DEC-057; §16 Amendment Gate; §22 |
| PD19-01 … PD19-20 | Proposed §19 decisions | ADDRESSED | DEC-031 … DEC-050 |
| F19-05 | Credential-bearing `file.replace` content | ADDRESSED | DEC-058; DEC-070 (enforcement gap, category ii); indexed as KF-12 (DEC-073) |
| F19-06 | Approval horizon; approval evidence after K8 loss | **OPEN** | DEC-059; OD19-03; §22; §16 Amendment Gate |
| F19-07 | K4 visibility of handle state | **REJECTED (as a finding)** | DEC-060; OD19-05 remains OPEN |
| F19-08 | Generated credentials: provisioning / output | PARTIAL | DEC-061; provisioning half DEC-046; output half OPEN — §16 Amendment Gate |
| F19-09 | Restore and post-backup authorization changes | **OPEN** | DEC-062; §22 / recovery gate; TQ-08; ODF-18-07 |
| Q19-01 … Q19-06 | §19 open items without an OD number | **OPEN** | §19.21.1; gates as listed there (Q19-05: TQ-09; Q19-06: SR-14 — DEC-065) |
| D19-01 … D19-09 | Disagreements and gaps found by the §19 gate | See §19.5.3 | §19.5.3 |

---

## 5B. §16 Amendment Gate items arising from §19 (pointers only)

No §16 text is changed. The §16 Amendment Gate is NOT SCHEDULED (DEC-070; DEC-068 D68-H). The §19 document is the source; see
§19.21.2 of [`19-persistence-secrets-data-lifecycle.md`](../current/19-persistence-secrets-data-lifecycle.md).

| # | Source | Item |
|---|---|---|
| 1 | DEC-048 R18c, R18i | K8 lifetime identity in journal references |
| 2 | DEC-048 R18d | K6 acceptance after K8 reinitialization |
| 3 | DEC-049 R19b | K6 refusal on unknown or unsupported K8 format |
| 4 | DEC-049 R19f | K8 interpretability across authorized K6 versions |
| 5 | DEC-053 R03e | K6-enforced approval horizon, if chosen |
| 6 | DEC-054 R04c, R04d | Credential-bearing `file.replace` composition, if chosen |
| 7 | DEC-055 R05d | Executor-family handle visibility, if chosen |
| 8 | DEC-057 R07c, R07d | Representation of R11f; optional Global Execution Policy maximum |
| 9 | DEC-058 F05a, F05b | Interpretation of F19-05 |
| 10 | DEC-061 F08c, F08d | Credential material in Operation output |
| 11 | Q19-02 | Idempotency retention and key reuse (with §22) |
| — | DEC-083 (DEC-082 D82-5(b)) | K8 tamper-evidence mechanism |
| — | DEC-084 (DEC-082 D82-17) | K8 digests of credential-bearing content (declared resources) |
| — | DEC-087 (DEC-080 D80-3; §15.10 P3) | P3 request-ID semantics |

Rows marked — are assigned by owner decision under DEC-068 D68-D and are not items of §19.21.2.

---

## 6. Open items created by owner decisions

| ID | Subject | Status | Pointer / owner |
|---|---|---|---|
| D-5 | CyberPanel installation / re-registration; T-24 | **OPEN** | CyberPanel K2 gate (DEC-017); KF-03 |
| D-9 | First-administrator bootstrap mechanics | **OPEN** | §22 / recovery gate (DEC-021); A-07 |
| D-14 | P2 protocol contract | **OPEN** | P2 protocol gate (DEC-026) |
| D-15 | CyberPanel presentation-surface placement | **OPEN** | CyberPanel K2 gate (DEC-027); KF-01, KF-02 |

---

## 7. Forensic-audit changes not fully absorbed by §15–§17

The forensic audit (historical, [`../history/forensic-audit.md`](../history/forensic-audit.md)) proposed
CHANGE-001 … CHANGE-027. Their current standing:

| Change | Subject | Status | Pointer / owner |
|---|---|---|---|
| CHANGE-001 | Runtime topology | ADDRESSED | §15 |
| CHANGE-002 | Privileged executor contract | ADDRESSED | §16 |
| CHANGE-003 | Authorization model | ADDRESSED | §17 |
| CHANGE-004 | Recovery authority | PARTIAL | §15 T-29, §17 A-07; mechanism OPEN — recovery gate |
| CHANGE-005 | Ownership / management vocabulary | **OPEN** | Unassigned — no gate currently owns it; baseline ANN-02 |
| CHANGE-006 | Association vs adoption; install → ownership | **OPEN** | Unassigned — no gate currently owns it; baseline ANN-09 |
| CHANGE-007 | Job states; every state-changing Action is a Job | PARTIAL | §17.5.2; Job states OPEN (§16 Q-6); baseline ANN-07, ANN-12 |
| CHANGE-008 | Plan binding | ADDRESSED | §17.11, A-24; §16.3 `expected_state` |
| CHANGE-009 | Lock / resource domains | PARTIAL | §16 X-22; cross-system lock domains OPEN; baseline ANN-08 |
| CHANGE-010 | Component / Target entity; System ↔ System relationships | **OPEN** | Unassigned — no gate currently owns it; §17.4 `COMPONENT` selector depends on it |
| CHANGE-011 | Reconciliation semantics | **OPEN** | §20 |
| CHANGE-012 | Absence lifecycle | **OPEN** | §20 or unassigned — no gate currently owns it |
| CHANGE-013 | Platform Services interface; generic platform compatibility | PARTIAL | §15.3, §16.2.2, DEC-006, T-27; replacement compatibility field OPEN |
| CHANGE-014 | Step-up outside the parent DOM | ADDRESSED | §17.8, §17.10, A-22 |
| CHANGE-015 | Audit tamper evidence; fail-closed audit | **OPEN** | §21; ODF-18-07 |
| CHANGE-016 | Trust anchors, signing, install sources | PARTIAL | §16.2, X-08; release-key custody and rollback OPEN — §22 |
| CHANGE-017 | Capability-level compatibility | **OPEN** | §12 compatibility (no gate scheduled) |
| CHANGE-018 | Host Environment domain | **OPEN** | §12 compatibility (no gate scheduled) |
| CHANGE-019 | Integration state vocabulary | **OPEN** | Unassigned — no gate currently owns it; baseline ANN-01 |
| CHANGE-020 | `not_applicable`; "configured"; "supported" | **OPEN** | Unassigned — no gate currently owns it |
| CHANGE-021 | Many-to-many System ↔ Integration | **OPEN** | Unassigned — no gate currently owns it; baseline ANN-05, ANN-30 |
| CHANGE-022 | Domain event model; Attention items | ADDRESSED | DEC-071 D71-3 |
| CHANGE-023 | Sensitivity classification | PARTIAL | §16.7 exposure modes; classification OPEN — §19; §19.22 attributes it to §21 / owner — discrepancy unresolved |
| CHANGE-024 | Fallback theme; status semantics; UI integrity | **OPEN** | Per-platform K2 gate; §18 SR-01 (conditional) |
| CHANGE-025 | SCC lifecycle (install, bootstrap, removal, downgrade) | **OPEN** | §22 |
| CHANGE-026 | Explicit deferrals | PARTIAL | T-22 (non-built-in Integrations excluded in v1); other deferrals OPEN |
| CHANGE-027 | Executor records before/after per step | ADDRESSED | §16.8, §16.10 |

---

## 8. Gates not yet designed

| Gate | Status | Stub |
|---|---|---|
| §19 Persistence, Secrets & Data Lifecycle | LOCKED (DEC-075) | [`19-persistence-secrets-data-lifecycle.md`](../current/19-persistence-secrets-data-lifecycle.md) |
| §20 Reconciliation / Desired State / Drift | NOT DESIGNED — GATE PENDING | [`20-reconciliation-desired-state-drift.md`](20-reconciliation-desired-state-drift.md) |
| §21 Audit / Events | LOCKED (DEC-085) | [`21-audit-events.md`](../current/21-audit-events.md) |
| §22 Lifecycle / Recovery | LOCKED (DEC-086); recovery gate = §22 (DEC-077); post-lock route DEC-078 | [`22-lifecycle-recovery.md`](../current/22-lifecycle-recovery.md) |
| P2 protocol | LOCKED (DEC-088); P3 request-ID semantics routed to the §16 Amendment Gate (DEC-087) | [`p2-protocol.md`](../current/p2-protocol.md) |
| CyberPanel K2 gate | OPEN | [`../../platforms/cyberpanel/k2-gate.md`](../../platforms/cyberpanel/k2-gate.md) |
| §16 Amendment Gate | NOT SCHEDULED (DEC-070; DEC-068 D68-H); procedure DEC-068 | §5B |
| §19 Owner Decision Gate | OPEN (DEC-064) | OD19-02, OD19-03, Q19-01, Q19-03, Q19-05, Q19-06 (§19.21, §19.21.1) |
| §17/K4 Architecture Gate | NOT SCHEDULED (DEC-092 convening concluded under D92-10) — not a §17 amendment gate; §17 remains LOCKED (DEC-064) | Q19-04 (§19.21.1) — not admitted (DEC-092); DEC-091 D91-2 (a)–(c), convened by DEC-092 |
| Unassigned domain-model items (CHANGE-005, 006, 010, 012, 019, 020, 021) | No owning gate assigned | — |
| §12 compatibility / Host Environment (CHANGE-017, 018; OQ-8; Q-7) | Not scheduled | — |
