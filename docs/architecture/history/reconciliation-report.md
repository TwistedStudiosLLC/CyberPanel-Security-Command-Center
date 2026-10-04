> **Document status:** HISTORICAL — NON-NORMATIVE
> **Authority category:** 5 — Historical / forensic material (see [Authority Hierarchy](../README.md#authority-hierarchy))
> **What this is:** The architecture reconciliation report. The owner accepted it as the architectural understanding
> at that time, subject to the owner decisions that followed.
> **This document is not current authority.** Its decisions do not independently establish current architecture
> (DEC-030, Q5). The owner's decisions on its items are recorded in the
> [decision log](../decisions/decision-log.md): D-1 → DEC-014, D-3 → DEC-015, D-4 → DEC-016, D-5 → DEC-017,
> D-6 → DEC-018, D-7 → DEC-019, D-8 → DEC-020, D-9 → DEC-021, D-10 → DEC-022; the D-2 presentation question →
> DEC-027 (D-15). The proposed document set in §E was refined by the Phase A.5 plan and DEC-030.
> **Transcription notes:** Reproduced verbatim. Removed process-wrapper text only: the closing line ("I've stopped
> here. Before creating any architecture document, I need your decisions on D-1, D-3, D-4 and D-10. D-2 and D-5 can
> wait for the CyberPanel K2 gate.").

# SCC Architecture Reconciliation Report

I made no changes. The repository was re-checked: `main` at `d7b1b9f`, with `LICENSE` as the only file. Because the repository holds no architecture, **every architecture item below comes from this conversation's working context**, and I've labelled each one with the gate or decision it comes from.

**Status labels used below**

| Label | Meaning |
|---|---|
| CURRENT/LOCKED | The owner locked it explicitly |
| CURRENT | Accepted and still in force, but never formally locked |
| OPEN | Undecided or not yet designed |
| HISTORICAL | Kept as record only; not in force |
| SUPERSEDED | Replaced by a later approved decision |
| UNKNOWN | Status can't be determined from what exists |

---

## A. Current Architecture I Now Understand

1. **SCC is a separate security and control system** with its own processes, data and authority. A parent platform connects to it through a platform-specific **K2** (§15.3, §15.5, your §3–4).
2. **Topology** (§15.3, §15.16):
   - Parent Platform (K1) → K2 → K3 → K4 → K6 → Host.
   - Around that chain: K5 (unprivileged workers), K7 (SCC-owned persistence), K8 (executor journal), K9 (host-local operator interface), K10 (host service manager), K11 (root-owned install and trust tree).
3. **Separation of duties.**
   - Authentication: K1/K2.
   - Authorization: K4 only (§17.2, T-15, A-08).
   - Execution enforcement: K6 only (§16.5, X-17).
   - Both sides refuse to widen each other: Principal → Capability → Target cannot expand Execution Declaration → Operation → Resource, and the reverse holds too (§17.4.2, A-10, X-06).
4. **Execution** happens only through §16. That means:
   - a closed vocabulary of Operations;
   - one request → one declared Operation (X-05);
   - K11 declarations;
   - approved executable and endpoint identity (X-34, X-35);
   - K8 write-ahead journaling;
   - no generic command execution in any form (X-02, X-03, X-11).
5. **Authorization** follows §17:
   - HUMAN Principals exist only through explicit enrollment. SYSTEM has Fixed System Authority, which is not a Permission (§17.1.1, A-05).
   - Built-in Roles plus direct Grants.
   - Risk tiers R0–R4, with REAUTH and APPROVAL as step-up.
   - Decisions are bound to `plan_digest`.
   - Revalidation happens before every WRITE.
   - Everything fails closed.
6. **Strategy is one panel at a time** (your message, §11–12). SCC Core stays provider-neutral. Platform knowledge lives only in that platform's K2 and in its Platform Services declaration or worker (T-27). CyberPanel is the first panel.
7. **The host is outside SCC's trust boundary.** A compromised root-equivalent host, which includes the parent platform, is a host compromise (§15.15, your §6 and §22).

## B. Locked / Current Components

| Item | Status | Source |
|---|---|---|
| §15 Runtime Topology & Trust Boundaries (K0–K11, T-01…T-31) | **CURRENT/LOCKED** | Approved at the §16 gate; restated as locked at the §17 and §18 gates |
| §16 Privileged Execution Contract, revised (X-01…X-39) | **CURRENT/LOCKED** | §16 revision gate; restated as locked at §17 |
| — Decision A: Core Discovery Declaration (X-36, X-37, X-39) | CURRENT/LOCKED | Owner, §16 revision gate |
| — Decision B: one request → one declared Operation (X-05, X-38) | CURRENT/LOCKED | Owner, §16 revision gate |
| — Decision C: Approved Executable Identity (X-34) | CURRENT/LOCKED | Owner, §16 revision gate |
| — CF-3: interpreted programs allowed only when both the program and its interpreter are identity-bound | CURRENT/LOCKED | Owner, §17 kickoff |
| — CF-5: Platform Services has its own declaration kind | CURRENT/LOCKED | Owner, §17 kickoff |
| §17 Authorization Model, final (A-01…A-36) | **CURRENT/LOCKED** | §17 finalization gate; restated as locked at §18 |
| — §17 owner decisions: (1) self-approval allowed by default; (2) package WRITE is R4; (3) explicit enrollment; (4) `PLATFORM_ADMIN` only in v1 | CURRENT/LOCKED | Owner, §17 finalization |
| Product name "Security Command Center (SCC)" | CURRENT | Your message §1 |
| One-panel-at-a-time strategy | CURRENT (owner position) | Your message §11–12. **Not yet recorded as a formal decision** (see D-4) |
| Development order, steps 1–11 | CURRENT (owner position) | Your message §18 |

## C. Superseded Architecture I Found (working context)

| # | Item | Where it appeared | Classification | Superseded by |
|---|---|---|---|---|
| C-1 | "Execution occurs through the Integration" | Baseline §6 | SUPERSEDED | §15.8, §16 (X-11, T-05, T-06) |
| C-2 | "Integration isolation is mandatory" with no boundary defined | Baseline §2, §14 | SUPERSEDED | §15.8 (K5, launcher-bound identity) |
| C-3 | "Privileged work through a controlled worker/mechanism" (vague) | Baseline §9 | SUPERSEDED | §15.9, §16 |
| C-4 | A single "Platform Adapter" component | Baseline §11, §13.55.5 | SUPERSEDED | §15.3 split (K2 Bridge, Presentation Adapter, Platform Services) |
| C-5 | A universal Parent Theme / Presentation Contract shared by CyberPanel, cPanel and DirectAdmin | Baseline §13.55 | HISTORICAL as a universal design; the per-platform principle is OPEN | Your message §5, §11–12 |
| C-6 | "Externally supplied / locally developed Integrations" | Baseline §14 | SUPERSEDED for v1 | T-22 |
| C-7 | Integration metadata field "supported CyberPanel versions" | Baseline §2, §14 | SUPERSEDED | T-27 / audit HIGH-11. The replacement field is OPEN. |
| C-8 | A recovery mode that includes a web UI | Baseline §12, §13 | SUPERSEDED | T-29, A-07. The recovery gate is OPEN. |
| C-9 | First §16 candidate: "at most one invocation"; Platform Services filed under Integration Declarations | §16 first candidate | SUPERSEDED | Revised §16 (X-05, CF-5) |
| C-10 | §17 candidate text, before the SYSTEM-cancel clarification | §17 candidate | SUPERSEDED | Final §17 (A-05) |
| C-11 | My Phase A STOP-2 option (b): "a time-limited §15 deviation letting K3/K4 run inside CyberPanel" | Phase A report | **SUPERSEDED / REJECTED** | Your message §2, §4 |
| C-12 | "System Control Contract" as the product name | Your earlier implementation brief | SUPERSEDED | Your message §1 |
| C-13 | Implementation brief framing: SCC Principal, authorization and UI delivered as a CyberPanel Django integration | Earlier implementation brief | SUPERSEDED | Your message §4, §18 |
| C-14 | Forensic Architectural Audit (§1–§20) | First turn | HISTORICAL | Its CHANGE-001…004 were absorbed into §15–§17. For the rest, see D-7. |
| C-15 | §18 candidate, §18 forensic review, §18 owner-decision gate | §18 turns | HISTORICAL / OPEN (see D-3) | — |
| — | Baseline principles: discovery first, unknown is valid, no score, detection ≠ Integration ≠ management, and similar | Baseline §1–§10 | **UNKNOWN** (see D-1) | — |

The repository itself contains no terminology to audit, because it holds nothing but `LICENSE`.

## D. Ambiguities and Contradictions

**D-1. Status of the baseline §1–§14.**
- The §15 gate called §1–§14 "the principles/domain baseline".
- Your message calls "superseded §11–§14 concepts" non-authoritative, but says nothing about §1–§10.
- **Decision needed:** do the baseline principles (§1–§10, and the parts of §11–§14 not listed in C) count as CURRENT, with the superseded items annotated? Or is the whole baseline HISTORICAL, with only §15–§17 authoritative?

**D-2. Where the CyberPanel presentation surface sits (contradiction with locked §15).**
- §15.6 puts the **Presentation Adapter in K3** and has **K3 serve the SCC UI assets**.
- Your message §4–5 puts a native CyberPanel route in **K2** as its "integration surface".
- If K3 serves executable UI content into CyberPanel's origin, the forensic finding TF-18-02 applies: a compromised K3 could reach root-equivalent power, which breaks §15.6's own stated bound.
- **A consistent option that needs a §15 amendment:** K2 renders natively, and K3 returns *data only*, which K2 presents as inert (SR-01). That keeps §15.6's bound on K3 true, but moves the Presentation Adapter from K3 to K2. I'm not choosing this; the decision belongs to the CyberPanel K2 gate plus a §15 amendment.

**D-3. What happens to §18 under the new strategy.**
- §18 is CONDITIONAL, and ODF-18-01 to ODF-18-09 are undecided.
- Your message moves ODF-18-01 to the CyberPanel K2 gate, but that hasn't been recorded as a decision.
- **Still needed:** a recorded disposition. For example: "ODF-18-01 is deferred to each platform's K2 gate, and SCC Core makes no universal claim about presentation origin."
- ODF-18-02 to ODF-18-09 are independent of the UI strategy. They are still open.

**D-4. The one-panel-at-a-time strategy isn't written into any gate text.**
- It affects how §15.18 OQ-1, the §15.6 Presentation Adapter placement, and baseline §11/§13.55 should be read.
- It needs a formal decision record.

**D-5. CyberPanel's registration mechanism vs T-24.**
- T-24 says SCC must not require modifying CyberPanel's core files, and must use only supported extension mechanisms.
- CyberPanel's only supported mechanism, its own plugin installer, edits `settings.py`, `urls.py` and `baseTemplate/index.html`. I verified this in upstream `stable`, 3.0 build 7.
- §11 permits guarded exceptions for *Actions*, not for SCC's own installation.
- **Needs an interpretation at the K2 gate or a T-24 amendment.** Your §21 treats the installer as K2 deployment only, which is consistent with the rest of the architecture but doesn't resolve T-24's literal wording.

**D-6. Wording in your message that needs precision (not contradictions):**
- **§3 "K5 unprivileged discovery/integration workers."** Under §15.7 and X-39, *generic* discovery logic belongs to K4. K5 runs only product-specific detection plus the Platform Services worker.
- **§4 "K2 … communicate with SCC Core."** Under §15.6 and §15.10, K2 talks to **K3** only (P2) and never to K4 directly.
- **§4 "K2 may authenticate the platform user."** Under §15.5 and §17.2, **K1** authenticates. K2 reads the platform session and issues the assertion. This matters because K2 must not contain an authentication system of its own.

**D-7. Forensic-audit changes that §15–§17 didn't absorb are still OPEN, not current:**
- ownership and management vocabulary (CHANGE-005/006);
- Job states (CHANGE-007 / §16 Q-6);
- lock domains (CHANGE-009);
- Component/Target model (CHANGE-010, which §17 selectors partly depend on: `COMPONENT(...)` "where the domain model defines it");
- absence lifecycle (CHANGE-012);
- event model (CHANGE-022).

**D-8. §20 is missing from your remaining-work list.** Your message §13 lists §19, §21 and §22. §20 (Reconciliation / Desired State / Drift) was proposed by the audit and hasn't been designed. It isn't needed for the identity slice, but it is needed before any reconciliation capability.

**D-9. The first administrator can't be bootstrapped with §17 alone.** A-07 requires the Local Root Operator (K9) to create the first `scc.administrator`. That needs §22 mechanics, and possibly the recovery gate, before even the identity slice can be completed.

**D-10. Whether the verbatim texts are authoritative.** The locked texts exist as my outputs in this conversation. Before committing them, the owner should confirm those exact texts are the approved versions:
- the original §15 candidate, which was approved unchanged;
- the revised §16;
- the final §17.

## E. Required Architecture Document Set

This is a proposal for layout only. Nothing gets created until you say so, and no content gets invented.

| Path (proposed) | Category | Contents |
|---|---|---|
| `docs/architecture/README.md` | Index | Status legend (A/B/C/D) and the status of every section and decision |
| `docs/architecture/current/15-runtime-topology.md` | **A — LOCKED** | §15 verbatim |
| `docs/architecture/current/16-privileged-execution.md` | **A — LOCKED** | Revised §16 verbatim |
| `docs/architecture/current/17-authorization.md` | **A — LOCKED** | Final §17 verbatim |
| `docs/architecture/current/glossary.md` | A | Terms defined in §15–§17 only |
| `docs/architecture/baseline/01-14-principles.md` | A or D, **pending D-1** | Baseline, with each superseded item from section C annotated in place |
| `docs/architecture/decisions/` (one record per decision) | **B** | Decisions A/B/C; CF-3; CF-5; §17 owner decisions 1–4; the one-panel-at-a-time strategy (D-4); product name; development order |
| `docs/architecture/open/18-threat-model/` | **C** | §18 candidate, marked CONDITIONAL, plus the owner-decision record with ODF-18-01…09 marked PENDING |
| `docs/architecture/open/register.md` | C | Every open question (§15 OQ, §16 Q, §17 P, §18 TQ/ODF, D-7 items), each with its owning gate |
| `docs/architecture/open/19…22-*.md` | C | Stubs stating **"NOT DESIGNED — gate pending"** and nothing more |
| `docs/architecture/history/` | **D** | The forensic audit, the §18 forensic review, superseded candidates (C-9, C-10), and a superseded-concepts register (section C of this report) |
| `docs/platforms/cyberpanel/reconnaissance.md` | C | Upstream facts I verified (A.2 of the Phase A report), each marked "upstream stable 3.0.7, not verified on the live host" |

**Rule:** every file must start with a status header stating its category and source gate, so historical material can never be mistaken for normative text.

## F. Dependency Order, §15 Through Implementation

1. §15, §16 and §17 are locked. **Commit them** (your steps 1–3), after D-10 is confirmed.
2. **Record decisions:** D-1 (baseline status), D-3 (§18 disposition), D-4 (strategy).
3. **§19 Persistence / Secrets / Data Lifecycle.** Inputs:
   - K7 ownership (T-23);
   - Principal, Grant and Decision records (§17);
   - credential store (§16.9, Q-2);
   - K8 retention (Q-2);
   - SR-12…SR-17 from §18, if adopted.
4. **§21 Audit / Events.** Inputs: A-35 and §17.18 fields, the separation of K8 from K4 audit (§16.10), CHANGE-022, and TQ-04.
5. **§22 Lifecycle / Recovery.** Inputs:
   - bootstrap of the first administrator (A-07, D-9);
   - approver anchors (§17.9, P-1);
   - K2 key provisioning (§15.14);
   - K11 install and release validation;
   - rollback protection (SR-15).

   Recovery authority (P-5, §16 Q-4) may be a separate gate.
6. **CyberPanel K2 gate.** Covers:
   - the P2 protocol and assertion format;
   - subject stability (P-6);
   - presentation placement (D-2) and ODF-18-01 for CyberPanel;
   - the T-24 interpretation (D-5);
   - an installer that is idempotent, reversible and version-aware.

   **Observation, not a decision:** K3's external API *is* the P2 protocol. So the P2 protocol contract, though not the CyberPanel installer, probably has to be designed before K3 can be implemented (your step 7). You may want to split this gate so the protocol part comes first.
7. **Minimum SCC Core implementation:**
   - K3;
   - K4 identity and authorization: enrollment, Roles, Grants, fail-closed;
   - K7 as §19 defines it;
   - audit as §21 defines it;
   - K10 service definitions.

   No K5 or K6 is needed for the identity slice.
8. K2 CyberPanel implementation, then identity binding, then the presentation surface (your steps 8–10).
9. **§20 Reconciliation, and the open D-7 items** before any capability that needs them.
10. **K5, K6, K8 and capabilities**, only once those sections allow them (your step 11).

## G. The CyberPanel-Specific K2 Boundary

**K2 may** (sources: §15.6, your message §4):
- register navigation;
- render the CyberPanel-native surface (placement pending D-2);
- read CyberPanel's authenticated session;
- issue the short-lived, audience-bound identity assertion (T-20: the signing key exists only in K2);
- relay requests to K3 over P2 (§15.10).

**K2 must not** (sources: §15.6, T-03, T-13, A-03, A-08, your message §4):
- authenticate users itself (K1 does, D-6);
- call K4, K5 or K6 directly;
- hold Principals, Grants, Roles, policy, Decisions or audit;
- evaluate authorization;
- treat CyberPanel ACLs, roles, `is_staff` or `is_superuser` as SCC authority (`PLATFORM_ADMIN` may only *restrict*, A-04);
- execute host operations;
- store SCC data in CyberPanel's database (T-23);
- carry product-specific SCC logic.

**Platform facts** (verified in upstream `stable` 3.0.7; live host not verified):
- identity comes from the `Administrator` model in `loginSystem` together with `request.session['userID']`;
- `httpProc` is CyberPanel's ACL gate, not SCC authorization;
- `X_FRAME_OPTIONS = 'SAMEORIGIN'`;
- the plugin installer edits core files and is lost on upgrade (D-5);
- static files go to two different destinations.

**Open at the K2 gate:**
- which identity field is canonical and whether it's stable (P-6, TQ-03);
- presentation placement (D-2);
- T-24 (D-5);
- whether assertions are bound to requests (ODF-18-06);
- how to re-register after a CyberPanel upgrade (§15.14).

## H. Must Not Be Implemented Yet

| Item | Blocked by |
|---|---|
| Any K7 schema or storage | §19 |
| Any audit or event format | §21 |
| Installer, bootstrap, anchor provisioning, recovery | §22 / recovery gate |
| K3 API or K2↔K3 protocol | K2 gate (the P2 contract) |
| K4 identity or authorization code | §19, §21, and the first-administrator bootstrap (D-9) |
| CyberPanel K2 plugin, route or template | K2 gate; D-2; D-5 |
| K5 workers, Integrations, Platform Services | Later gates; the D-7 domain model |
| K6, K8, K11 declarations, any Operation | §16 is locked, but it depends on §19, §21 and §22 and is outside the first slice |
| Approval tooling | §22, P-1, ODF-18-08 |
| Reconciliation or drift handling | §20 |
| Any `execute` / `run` / `shell` / `subprocess` / `exec_as_root` helper | Forbidden permanently (X-02, X-03, X-11) |
| Any capability with host effects (firewall, packages, services, files, DNS, mail, remediation) | Gates plus K6 |
| Any universal presentation or origin mechanism in SCC Core | Your message §11–12, T-27 |
