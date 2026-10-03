> **Document status:** CURRENT — OWNER DECISIONS
> **Authority category:** 2 — Explicit owner decisions (see [Authority Hierarchy](../README.md#authority-hierarchy))
> **Source:** Owner messages in the SCC architecture sessions, recorded 2026-09-23. Each entry names its source message.
> **Normative:** Yes. Owner wording is reproduced verbatim inside fenced `text` blocks. Text outside those blocks
> (titles, status, cross-references) is an index added for navigation and is not owner wording. Entries record owner
> decisions. They do not themselves amend or lock §15–§17 (DEC-064).
> **Numbering note:** D-2 was not issued as an owner decision. The reconciliation item D-2 (presentation placement)
> was addressed by owner decision D-15. DEC-030 records the Phase A.5 confirmation and was added after the
> Phase A.5 plan listed DEC-001 … DEC-029. DEC-031 … DEC-064 record the §19 owner disposition review and its
> change-set reconciliation. DEC-065 records the §19 pre-lock corrections. DEC-066 records K11-held SCC data
> ownership under R1/R4. DEC-067 records the F19-06 known-findings index treatment.
> DEC-068 records the procedural framework of the §16 Amendment Gate.
> DEC-069 convenes the §16 Amendment Gate for OD19-04 and the interpretation of F19-05.
> DEC-070 records the OD19-04 / F19-05 gate outcome.
> DEC-071 … DEC-080 record the §21, §22 and P2/K3 gate structures, the ODF-18-07 disposition, the F19-05 index
> treatment, the §19 locked form and lock, the recovery-gate identity, the §22 post-lock route and the development
> path.
> DEC-081 records the §19.3 post-lock authority statement.
> DEC-082 records the §21 Audit Events owner dispositions.
> DEC-083 and DEC-084 assign the K8 tamper-evidence mechanism and K8 credential-bearing digest handling to the §16
> Amendment Gate.
> DEC-085 records the §21 candidate-review dispositions and locks §21.
> DEC-086 records the §22 candidate dispositions and locks §22.
> DEC-087 assigns P3 request-ID semantics to the §16 Amendment Gate. DEC-088 records the P2/K3 dispositions and locks
> the P2/K3 gate.
> DEC-089 authorizes the first Phase 6 implementation slice: the abstract K4 authorization-and-audit core.
> DEC-090 records owner interpretations of five Phase 6 authorization semantics questions.
> DEC-091 routes the K4-side aspects of three open P2 verification questions to the §17/K4 Architecture Gate.

# SCC Decision Log

| ID | Title | Status |
|---|---|---|
| DEC-001 | §15 approved / locked | LOCKED |
| DEC-002 | §16 Decision A — Core Discovery Declaration | LOCKED |
| DEC-003 | §16 Decision B — One request → one declared Operation | LOCKED |
| DEC-004 | §16 Decision C — Profile executable identity | LOCKED |
| DEC-005 | CF-3 — Interpreted programs require interpreter identity binding | LOCKED |
| DEC-006 | CF-5 — Platform Services has its own Execution Declaration kind | LOCKED |
| DEC-007 | §16 locked | LOCKED |
| DEC-008 | §17 Owner Decision 1 — Self-approval permitted by default | LOCKED |
| DEC-009 | §17 Owner Decision 2 — Package-family WRITE is R4 | LOCKED |
| DEC-010 | §17 Owner Decision 3 — Explicit enrollment | LOCKED |
| DEC-011 | §17 Owner Decision 4 — v1 restricted to PLATFORM_ADMIN | LOCKED |
| DEC-012 | §17 locked | LOCKED |
| DEC-013 | Product identity — Security Command Center | CURRENT |
| DEC-014 | D-1 — Status of the §1–§14 baseline | CURRENT |
| DEC-015 | D-3 — §18 disposition (ODF-18-01 → per-platform K2 gate) | CURRENT |
| DEC-016 | D-4 — One panel at a time | **LOCKED** (project/architecture strategy) |
| DEC-017 | D-5 — CyberPanel installation deferred to the K2 gate | CURRENT (deferral) |
| DEC-018 | D-6 — K2 identity precision | CURRENT |
| DEC-019 | D-7 — K5 precision | CURRENT |
| DEC-020 | D-8 — §20 added to the roadmap | CURRENT |
| DEC-021 | D-9 — Bootstrap dependency | CURRENT |
| DEC-022 | D-10 — Approval of the §15–§17 texts | CURRENT |
| DEC-023 | D-11 — Architecture authority hierarchy | CURRENT |
| DEC-024 | D-12 — §19 through §22 not designed; order | CURRENT |
| DEC-025 | D-13 — Implementation order | CURRENT |
| DEC-026 | D-14 — K3 / P2 clarification | CURRENT |
| DEC-027 | D-15 — K2 presentation question | CURRENT (question OPEN) |
| DEC-028 | D-16 — First implementation boundary | CURRENT |
| DEC-029 | D-17 — No premature execution | CURRENT |
| DEC-030 | Phase A.5 confirmation — repository documentation rules | CURRENT |
| DEC-031 | PD19-01 — One authoritative owner and storage domain per data class | CURRENT (revised) |
| DEC-032 | PD19-02 — SD-K6P storage areas | CURRENT (accepted) |
| DEC-033 | PD19-03 — Credential secret material only in SD-K6P / K6 | CURRENT (accepted as locked-derived; clarification C-03a/C-03b) |
| DEC-034 | PD19-04 — Authorization/audit atomicity and integrity | CURRENT (revised) |
| DEC-035 | PD19-05 — Audit fail-closed | CURRENT (revised) |
| DEC-036 | PD19-06 — C-writable configuration | CURRENT (revised) |
| DEC-037 | PD19-07 — Integration-specific configuration | CURRENT (revised) |
| DEC-038 | PD19-08 — Revoked-Principal tombstones | CURRENT (revised) |
| DEC-039 | PD19-09 — Retention of referenced authorization records | CURRENT (revised) |
| DEC-040 | PD19-10 — Backup/export encryption; no root-protection claim | CURRENT (revised) |
| DEC-041 | PD19-11 — K8 and pre-image retention | CURRENT (revised) |
| DEC-042 | PD19-12 — Deletion model (A) and credential-bearing-content authoring rule (B) | CURRENT (revised) |
| DEC-043 | PD19-13 — Material SCC components must not persist | CURRENT (revised) |
| DEC-044 | PD19-14 — SCC session tokens | CURRENT (revised) |
| DEC-045 | PD19-15 — No bootstrap or recovery secret | CURRENT (revised) |
| DEC-046 | PD19-16 — Credential-handle lifecycle | CURRENT (revised) |
| DEC-047 | PD19-17 — Backup/restore implications | CURRENT (revised) |
| DEC-048 | PD19-18 — K8 loss or reinitialization | CURRENT (revised) |
| DEC-049 | PD19-19 — Format versioning, migration and downgrade | CURRENT (revised) |
| DEC-050 | PD19-20 — §20 dependency finding | CURRENT (revised) |
| DEC-051 | OD19-01 — Assertion verification material | CURRENT (deferral — question OPEN) |
| DEC-052 | OD19-02 — At-rest encryption | CURRENT (deferral — question OPEN) |
| DEC-053 | OD19-03 — Approval validity horizon; R03e correction | CURRENT (deferral — question OPEN) |
| DEC-054 | OD19-04 — Credential-bearing file content | CURRENT (deferral — question OPEN) |
| DEC-055 | OD19-05 — K4 visibility of credential-handle state | CURRENT (deferral — question OPEN) |
| DEC-056 | OD19-06 — DC-05 retention | CURRENT (deferral — question OPEN) |
| DEC-057 | OD19-07 — Pre-image retention bounds | CURRENT (deferral — question OPEN) |
| DEC-058 | F19-05 — Credential-bearing `file.replace` content | CURRENT (finding deferred — OD19-04 / §16 Amendment Gate) |
| DEC-059 | F19-06 — Approval horizon; approval evidence after K8 loss | CURRENT (finding deferred — OD19-03 / §22 / §16 Amendment Gate) |
| DEC-060 | F19-07 — K4 visibility of credential-handle state | CURRENT (rejected as a finding against locked text) |
| DEC-061 | F19-08 — Generated credentials | CURRENT (finding split — provisioning half governed by DEC-046; output half deferred — §16 Amendment Gate) |
| DEC-062 | F19-09 — K7 restore and post-backup authorization changes | CURRENT (finding deferred — §22 / recovery gate; TQ-08; ODF-18-07) |
| DEC-063 | Post-lock §19 resolution route | CURRENT (adopted) |
| DEC-064 | §19 Change-Set Reconciliation Decisions | CURRENT (adopted) |
| DEC-065 | §19 Pre-Lock Corrections (J-1 … J-12) | CURRENT (adopted) |
| DEC-066 | K11-held SCC data ownership under R1/R4 | CURRENT (adopted — DC-01/DC-02 owner OPEN) |
| DEC-067 | F19-06 — Known-findings index treatment | CURRENT (adopted — F19-06 indexed as KF-11 and OPEN; OD19-03 OPEN) |
| DEC-068 | §16 Amendment Gate — Procedural framework | CURRENT (adopted — procedural; gate NOT SCHEDULED) |
| DEC-069 | §16 Amendment Gate — Convening for OD19-04 / F19-05 | CURRENT (adopted — gate OPEN; OD19-04 and F19-05 interpretation admitted, undecided) |
| DEC-070 | §16 Amendment Gate — OD19-04 / F19-05 Disposition | CURRENT (adopted — OD19-04 Path A; F19-05 enforcement gap; gate NOT SCHEDULED) |
| DEC-071 | §21 Scope and Gate Structure | CURRENT (adopted — §21 scope and gate structure; §21 NOT DESIGNED; not locked) |
| DEC-072 | ODF-18-07 Disposition | CURRENT (adopted — ODF-18-07 Option B, mechanism (iii); KF-08 OPEN) |
| DEC-073 | F19-05 Index Treatment | CURRENT (adopted — F19-05 indexed as KF-12; OPEN — enforcement gap, category (ii)) |
| DEC-074 | §19 Locked Form | CURRENT (adopted — §19 locked in its existing form) |
| DEC-075 | §19 Lock | CURRENT (adopted — §19 LOCKED) |
| DEC-076 | §22 Scope and Gate Structure | CURRENT (adopted — §22 scope and gate structure; §22 NOT DESIGNED; not locked) |
| DEC-077 | Recovery Gate Identity | CURRENT (adopted — recovery gate = §22 gate) |
| DEC-078 | §22 Post-Lock Route | CURRENT (adopted — §22 post-lock route; applies after §22 lock) |
| DEC-079 | Development Path and Phase-6 Entry Criteria | CURRENT (adopted — Phase-6 entry criteria; no implementation authority) |
| DEC-080 | P2/K3 Gate Structure | CURRENT (adopted — P2/K3 gate structure; not locked) |
| DEC-081 | §19.3 Post-Lock Authority Statement | CURRENT (adopted — one-time explicit owner amendment of §19.3; DEC-023 hierarchy governs locked §19) |
| DEC-082 | §21 Audit Events Owner Dispositions | CURRENT (adopted — §21 owner dispositions; §21 not written, not locked) |
| DEC-083 | Assignment of the K8 tamper-evidence mechanism to the §16 Amendment Gate | CURRENT (adopted — item assigned, scope A1; gate NOT SCHEDULED; undecided) |
| DEC-084 | Assignment of K8 credential-bearing digest handling to the §16 Amendment Gate | CURRENT (adopted — item assigned, scope B2; D70-D3(4) "additional" reading closed; gate NOT SCHEDULED; undecided) |
| DEC-085 | §21 Audit Events Lock | CURRENT (adopted — §21 LOCKED; Category 1 from DEC-085) |
| DEC-086 | §22 Lifecycle / Recovery Lock | CURRENT (adopted — §22 LOCKED; bootstrap scope; Category 1 from DEC-086) |
| DEC-087 | Assignment of P3 request-ID semantics to the §16 Amendment Gate | CURRENT (adopted — item assigned; gate NOT SCHEDULED; undecided) |
| DEC-088 | P2/K3 Gate Lock | CURRENT (adopted — P2/K3 LOCKED; Phase 5 complete; Category 1 from DEC-088) |
| DEC-089 | Phase 6 Implementation Authorization: K4 Authorization and Audit Core | CURRENT (adopted — first Phase 6 implementation slice authorized; no amendment; DEC-029 standing) |
| DEC-090 | Phase 6 Authorization Semantics Clarification | CURRENT (adopted — owner interpretations for the Phase 6 K4 core; no amendment; corrections documented, not implemented) |
| DEC-091 | Routing of Open P2 Verification Questions | CURRENT (adopted — routing only; K4-side items assigned to the §17/K4 Architecture Gate; no technical answer; no amendment) |

---

## DEC-001 — §15 approved / locked

- **Status:** LOCKED
- **Source:** §16 gate kickoff message; restated in the §17 gate kickoff and the §18 gate kickoff.
- **Constrains:** [`../current/15-runtime-topology.md`](../current/15-runtime-topology.md)

```text
§15 — Runtime Topology & Trust Boundaries has now been reviewed and is approved to proceed to §16.
```

```text
§15 — Runtime Topology & Trust Boundaries
is LOCKED.
```

---

## DEC-002 — §16 Decision A — Core Discovery Declaration

- **Status:** LOCKED
- **Source:** §16 revision / lock gate message.
- **Constrains:** §16.2.4, X-36, X-37, X-39.

```text
------------------------------------------------------------
DECISION A — CORE DISCOVERY DECLARATION
------------------------------------------------------------

C-1 IS APPROVED.

K4 owns generic, product-neutral discovery logic.

§15 requires all host observation to pass through K6.

Therefore K4 requires a narrow K11 READ-only execution declaration
through which Core Discovery may request the generic discovery
operations it is authorized to use.

Use a dedicated:

CORE DISCOVERY DECLARATION

This declaration MUST:

- be signed
- be loaded and validated by K6 exactly like other K11 execution
  declarations
- be READ-only
- be tightly scoped
- expose only the generic discovery operations actually required by K4
- be subject to the same K11 bounds and K6 validation
- never grant WRITE capability
- never permit K4 to widen its own authority
- remain subject to the Host Restriction Overlay

IMPORTANT TERMINOLOGY RULE:

Do NOT silently redefine Core Discovery as an actual SCC Integration.

Core Discovery belongs to K4.

The declaration exists because K6's execution model requires a
K11-declared scope/declaration identity.

If the existing request contract requires an integration_id field,
define a reserved identifier for Core Discovery and explicitly state
that this identifier represents a K11 execution declaration for Core
Discovery, NOT an Integration in the SCC domain model.

Do NOT move generic discovery logic into K5.

Do NOT alter §15 to make K5 responsible for generic discovery.

Preserve:

K4 = generic discovery logic
K5 = product-specific Integration logic
K6 = physical host observation/execution
```

---

## DEC-003 — §16 Decision B — One request → one declared Operation

- **Status:** LOCKED
- **Source:** §16 revision / lock gate message.
- **Constrains:** §16.6.1, X-05 (final wording in §16), X-38.

```text
------------------------------------------------------------
DECISION B — ONE OPERATION, NOT ONE RAW INVOCATION
------------------------------------------------------------

The existing §16 wording:

"One request produces at most one invocation."

is too literal because operations such as:

file.replace

may have explicitly defined internal mechanical stages:

- stage content
- run validator profile
- commit atomically
- evaluate postcondition

These are part of ONE declared Operation.

They must not be interpreted as dynamically chained Operations.

REVISE §16.6.1 and X-05 accordingly.

The canonical rule is:

ONE REQUEST → ONE DECLARED OPERATION.

K6 MUST NOT:

- dynamically chain Operations
- derive additional Operations from results
- schedule additional Operations as a consequence of execution
- invoke an undeclared Operation
- turn one request into an arbitrary sequence of Operation requests

However:

A declared Operation MAY contain explicitly defined internal
mechanical steps necessary to implement that Operation's semantics.

For example:

file.replace

may internally perform:

1. staging
2. declared validator execution
3. atomic commit
4. postcondition evaluation

provided those steps are part of the canonical Operation definition.

The validator profile MUST NOT become a dynamically selected Operation.

It is part of the declared semantics of file.replace.

REPLACE THE EXISTING X-05 WITH A FORMAL INVARIANT EQUIVALENT TO:

X-05 — One request MUST invoke exactly one declared Operation.
K6 MUST NOT dynamically chain Operations, derive additional Operations
from execution results, or schedule additional Operations as a consequence
of execution. An Operation MAY contain only the explicitly defined
internal mechanical steps necessary to implement its declared semantics.

Use the exact final wording only after checking it against the rest of
§16.
```

---

## DEC-004 — §16 Decision C — Profile executable identity

- **Status:** LOCKED
- **Source:** §16 revision / lock gate message.
- **Constrains:** §16.1.1, §16.2.3, X-03, X-34.

```text
------------------------------------------------------------
DECISION C — PROFILE EXECUTABLE IDENTITY
------------------------------------------------------------

The existing Tier-2 profile design is retained.

Profiles remain necessary because real Security System interfaces may
include:

- product CLIs
- local sockets
- D-Bus
- other bounded local endpoints

K6 remains the generic enforcement engine.

However, "the documented purpose of a binary" is not itself sufficient
as an executable security boundary.

Strengthen the K11 profile identity model.

A profile MUST identify the approved executable itself, not merely its
path.

At minimum, determine an architecture-level identity mechanism such
as:

- approved executable digest
- immutable executable identity
- equivalent release-approved host identity

The exact cryptographic/hash implementation may remain an implementation
detail unless §16 genuinely requires it.

The important invariant is:

K6 MUST NOT trust merely:

"/some/path/program"

and execute whatever happens to exist there.

The signed K11 declaration must bind the profile to the approved
executable identity.

Preserve all existing profile restrictions:

- absolute executable path
- root-owned executable and path components
- no group/world-writable executable path
- fixed argv/request template
- every variable slot typed
- fixed environment
- fixed working directory
- fixed stdin policy
- fixed run_as
- output bound
- timeout
- READ/WRITE class
- no shell
- no interpreter
- no arbitrary command execution
- no runtime profile creation

The final architecture must make clear that:

PATH + EXECUTABLE IDENTITY + TEMPLATE + ENVIRONMENT + CWD + STDIN +
RUN_AS

form the declared execution boundary.
```

---

## DEC-005 — CF-3 — Interpreted programs require interpreter identity binding

- **Status:** LOCKED
- **Source:** §17 gate kickoff message ("The architecture-owner explicitly approved:").
- **Constrains:** §16.16 CF-3, X-03, X-34.

```text
- CF-3: interpreted Security System programs are permitted only when
  both the executable and its interpreter are identity-bound by K11.
```

---

## DEC-006 — CF-5 — Platform Services has its own Execution Declaration kind

- **Status:** LOCKED
- **Source:** §17 gate kickoff message.
- **Constrains:** §16.2.2, §16.16 CF-5.

```text
- CF-5: Platform Services has its own Execution Declaration kind.
- Core Discovery has its own Execution Declaration kind.
```

---

## DEC-007 — §16 locked

- **Status:** LOCKED
- **Source:** §17 gate kickoff message; restated in the §18 gate kickoff.
- **Constrains:** [`../current/16-privileged-execution.md`](../current/16-privileged-execution.md)

```text
§16 — Privileged Execution Contract
is LOCKED.
```

```text
The architecture-owner explicitly approved:

- CF-3: interpreted Security System programs are permitted only when
  both the executable and its interpreter are identity-bound by K11.
- CF-5: Platform Services has its own Execution Declaration kind.
- Core Discovery has its own Execution Declaration kind.
- One accepted request executes exactly one declared Operation.
- Operations may contain fixed internal mechanical steps.
- K6 never dynamically chains Operations.
- Approved Executable Identity is mandatory for tool profiles.
- Endpoint owner identity is mandatory for endpoint profiles.
- K4 remains the authorization decision point.
- K6 remains the physical enforcement point.
- K6 is NOT an authorization engine.

DO NOT reopen these decisions.
```

---

## DEC-008 — §17 Owner Decision 1 — Self-approval permitted by default

- **Status:** LOCKED
- **Source:** §17 finalization / owner-approval gate message.
- **Constrains:** §17.8, §17 Gate Assessment owner review item 1.

```text
### Owner Decision 1
Self-approval is permitted by default in v1.

Do NOT convert this into mandatory two-person approval.

Do NOT imply that self-approval is equivalent to separation of duties.

Retain the distinction that the security value of approval comes from the independent anchored signing key.
```

---

## DEC-009 — §17 Owner Decision 2 — Package-family WRITE is R4

- **Status:** LOCKED
- **Source:** §17 finalization / owner-approval gate message.
- **Constrains:** §17.5.3 criterion (b).

```text
### Owner Decision 2
Package-family WRITE capabilities are R4.

Therefore package installation, removal, and upgrade require an approver anchor and approval under the R4 model.

Do NOT downgrade this.
```

---

## DEC-010 — §17 Owner Decision 3 — Explicit enrollment

- **Status:** LOCKED
- **Source:** §17 finalization / owner-approval gate message.
- **Constrains:** §17.1.5, A-03.

```text
### Owner Decision 3
Every platform administrator must be explicitly enrolled.

A platform identity being PLATFORM_ADMIN does NOT itself grant SCC authority.

Do NOT introduce automatic enrollment or automatic Grants.
```

---

## DEC-011 — §17 Owner Decision 4 — v1 restricted to PLATFORM_ADMIN

- **Status:** LOCKED
- **Source:** §17 finalization / owner-approval gate message.
- **Constrains:** §17.1.5, A-04.

```text
### Owner Decision 4
v1 is restricted to PLATFORM_ADMIN.

Do NOT introduce reseller, user, or multi-tenant platform authorization.

These remain future work.
```

---

## DEC-012 — §17 locked

- **Status:** LOCKED
- **Source:** §18 gate kickoff message.
- **Constrains:** [`../current/17-authorization.md`](../current/17-authorization.md)

```text
The following architecture gates are LOCKED and MUST be treated as authoritative:

- §15 — Runtime Topology & Trust Boundaries
- §16 — Privileged Execution Contract
- §17 — Authorization Model

§17 has passed its architecture gate:

    §17 — PASS — READY FOR §18
```

---

## DEC-013 — Product identity — Security Command Center

- **Status:** CURRENT
- **Source:** Architecture reconciliation message, section 1.

```text
The product is:

    Security Command Center (SCC)

Use:

    SCC
    SCC Core
    CyberPanel Integration
    K2
    K3
    K4
    K5
    K6
    K7
    K8
    K9
    K10
    K11

Do NOT rename the product to "System Control Contract."

"Contract" refers to an architectural contract/specification where
appropriate.
```

---

## DEC-014 — D-1 — Status of the §1–§14 baseline

- **Status:** CURRENT
- **Source:** Owner decisions message (D-1).
- **Constrains:** [`../baseline/foundational-01-14.md`](../baseline/foundational-01-14.md), the architecture index.

```text
D-1 — STATUS OF THE §1–§14 BASELINE

DECISION:

The original §1–§14 material is NOT to be discarded wholesale.

The foundational/domain principles from the original baseline remain
part of the SCC architectural lineage and remain CURRENT where they
do not conflict with later locked architecture.

However:

    §15
    §16
    §17

are the controlling normative architecture wherever an earlier
baseline statement conflicts with them.

Therefore the baseline shall be treated as:

    FOUNDATIONAL / CURRENT WITH OVERRIDES

rather than simply CURRENT or HISTORICAL.

The repository representation must make the hierarchy explicit.

Use this rule:

    Earlier principle
        +
    later locked architecture
        =
    later locked architecture controls

Do not silently rewrite the historical baseline.

Instead, preserve the original principle and annotate any part
that has been superseded.

The following distinctions are required:

    CURRENT FOUNDATIONAL PRINCIPLE
        still valid and compatible with §15–§17

    SUPERSEDED PRINCIPLE
        replaced by a later architectural decision

    HISTORICAL PROPOSAL
        retained for architectural history but no longer normative

    OPEN
        not yet resolved by a later gate

This means the original discovery/unknown/detection/integration/
management/ownership/health/compatibility/authorization principles
should remain available as foundational material where compatible.

The repository MUST NOT represent the entire original §1–§14 as
either wholly authoritative or wholly obsolete.
```

---

## DEC-015 — D-3 — §18 disposition

- **Status:** CURRENT
- **Source:** Owner decisions message (D-3).
- **Constrains:** [`../open/18-threat-model/README.md`](../open/18-threat-model/README.md), ODF-18-01 … ODF-18-09.

```text
D-3 — §18 DISPOSITION

DECISION:

§18 remains a real architectural section and remains CONDITIONAL.

It is NOT deleted.

It is NOT promoted to fully locked architecture.

It is NOT allowed to block the one-panel-at-a-time strategy.

ODF-18-01 is hereby DISPOSITIONED as follows:

    The universal presentation/origin question is deferred to the
    Platform/K2 gate for each concrete platform.

SCC Core MUST NOT make a universal presentation-origin claim that
assumes all control panels expose the same extension architecture.

The architectural rule becomes:

    SCC Core defines security/domain/process invariants.

    Each platform integration must establish its own conforming
    presentation/security boundary against the actual platform.

For CyberPanel specifically:

    ODF-18-01 -> CyberPanel K2 / Platform Adapter gate.

Do not resolve ODF-18-01 by weakening §15.

Do not resolve it by placing SCC authorization inside CyberPanel.

Do not resolve it by putting SCC Core into the CyberPanel Django
process.

Do not resolve it by inventing a universal iframe/cross-origin
architecture.

The CyberPanel gate must determine the conforming presentation
arrangement while preserving the SCC Core trust boundaries.

ODF-18-02 through ODF-18-09 remain OPEN unless already explicitly
resolved elsewhere.

Do not silently decide them.

The §18 repository document must therefore be marked:

    CONDITIONAL
    THREAT MODEL / FORENSIC ARCHITECTURE
    NOT FULLY LOCKED

Historical §18 forensic material must remain distinguishable from
current decisions.
```

---

## DEC-016 — D-4 — One panel at a time

- **Status:** **LOCKED** as a project/architecture strategy
- **Source:** Owner decisions message (D-4).

```text
D-4 — ONE-PANEL-AT-A-TIME STRATEGY

DECISION:

LOCKED AS A PROJECT/ARCHITECTURE STRATEGY.

SCC Core is provider-neutral.

Platform integration is platform-specific.

The project will implement and validate one platform at a time.

The first platform is:

    CyberPanel

This means:

    SCC Core
        remains provider-neutral

    CyberPanel K2
        contains CyberPanel-specific knowledge

    future cPanel K2
        may contain cPanel-specific knowledge

    future Plesk K2
        may contain Plesk-specific knowledge

Do NOT put platform conditionals into SCC Core.

Do NOT design future platforms speculatively when doing the
CyberPanel implementation.

Do NOT require a universal presentation implementation before a
specific platform can proceed.

This decision DOES NOT relax the SCC process/trust boundaries.

It only determines where platform-specific questions are resolved.

Record this as an explicit architecture decision.
```

---

## DEC-017 — D-5 — CyberPanel installation deferred to the K2 gate

- **Status:** CURRENT (a deferral; the underlying question is OPEN)
- **Source:** Owner decisions message (D-5).
- **Related:** KF-03 in the architecture index; [`../../platforms/cyberpanel/k2-gate.md`](../../platforms/cyberpanel/k2-gate.md).

```text
D-5 — CYBERPANEL INSTALLATION

Do NOT resolve D-5 yet.

It belongs to the CyberPanel K2 gate.

The upstream CyberPanel installer behavior is evidence about the
platform, not an SCC architectural decision.

The K2 gate must determine how SCC can be installed/re-registered
while preserving:

    idempotence
    reversibility
    upgrade behavior
    version awareness
    SCC process separation
    SCC data ownership

Do not amend T-24 merely because the upstream CyberPanel installer
is poorly behaved.

First determine whether a conforming K2 deployment mechanism can
be built around the actual CyberPanel extension model.

If not, then the contradiction must be brought back as an explicit
architecture decision.
```

---

## DEC-018 — D-6 — K2 identity precision

- **Status:** CURRENT
- **Source:** Owner decisions message (D-6).

```text
D-6 — K2 IDENTITY PRECISION

Your correction in D-6 is accepted.

Use the following precise model:

    K1
        authenticates the user as the parent platform.

    K2
        consumes the authenticated platform session/context and
        produces the SCC-facing identity assertion.

    K3
        is the SCC service boundary.

    K4
        is the SCC authorization/domain boundary.

K2 does NOT implement a second authentication system.

K2 does NOT directly call K4.

K2 communicates with K3 through the defined P2 boundary.

Preserve this distinction in all future documentation.
```

---

## DEC-019 — D-7 — K5 precision

- **Status:** CURRENT
- **Source:** Owner decisions message (D-7).

```text
D-7 — K5 PRECISION

Your correction is accepted.

Do not describe K5 generically as "discovery."

Generic SCC discovery belongs to K4 through the reserved
Core Discovery Declaration.

K5 is for:

    product-specific detection
    Integration workers
    Platform Services worker behavior

where permitted by the architecture.

K5 remains unprivileged.
```

---

## DEC-020 — D-8 — §20 added to the roadmap

- **Status:** CURRENT
- **Source:** Owner decisions message (D-8).
- **Related:** [`../open/20-reconciliation-desired-state-drift.md`](../open/20-reconciliation-desired-state-drift.md)

```text
D-8 — §20

Accepted.

§20 must be added to the architecture roadmap.

It is:

    OPEN / NOT YET DESIGNED

and concerns:

    Reconciliation
    Desired State
    Drift

Do not invent §20 content.

It does not block the initial identity slice unless a later
capability requires reconciliation semantics.
```

---

## DEC-021 — D-9 — Bootstrap dependency

- **Status:** CURRENT
- **Source:** Owner decisions message (D-9).
- **Related:** §17 A-07; [`../open/22-lifecycle-recovery.md`](../open/22-lifecycle-recovery.md)

```text
D-9 — BOOTSTRAP

Accepted.

The first administrator bootstrap is a real dependency.

A-07 requires the Local Root Operator / K9 recovery/bootstrap
boundary.

Therefore bootstrap mechanics cannot be casually implemented in
K2 or K4.

The exact bootstrap/recovery mechanism belongs to the appropriate
lifecycle/recovery architecture gate.

Do not invent a temporary web bootstrap simply because it is
convenient.
```

---

## DEC-022 — D-10 — Approval of the §15–§17 texts

- **Status:** CURRENT
- **Source:** Owner decisions message (D-10).

```text
D-10 — APPROVAL OF §15–§17 TEXTS

CONFIRMED.

Use the following as the authoritative architecture documents:

    §15 — the approved Runtime Topology & Trust Boundaries text

    §16 — the revised/locked Privileged Execution Contract
           containing Decisions A, B and C and X-01…X-39

    §17 — the final canonical Authorization Model containing
           the SYSTEM revocation-triggered cancellation clarification
           and A-01…A-36

These are the authoritative versions.

Do NOT substitute earlier candidates.

Do NOT merge earlier and later versions.

Do NOT silently rewrite them while committing them.

If formatting changes are required for repository presentation,
preserve the normative text and semantics exactly.
```

---

## DEC-023 — D-11 — Architecture authority hierarchy

- **Status:** CURRENT
- **Source:** Owner decisions message (D-11).
- **Related:** [`../README.md#authority-hierarchy`](../README.md#authority-hierarchy)

```text
D-11 — IMPORTANT ARCHITECTURE HIERARCHY

Add an explicit hierarchy to the architecture README.

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

---

## DEC-024 — D-12 — §19 through §22 not designed; order

- **Status:** CURRENT
- **Source:** Owner decisions message (D-12).

```text
D-12 — §19 THROUGH §22

The following are NOT designed yet:

    §19 Persistence, Secrets & Data Lifecycle
    §20 Reconciliation / Desired State / Drift
    §21 Audit / Events
    §22 Lifecycle / Recovery

Do not create fake specifications for these.

Repository stubs may identify them as:

    NOT DESIGNED
    GATE PENDING

but must not invent normative behavior.

Their dependency order should be preserved.

The current intended order is:

    §19
      ↓
    §21
      ↓
    §22

with §20 proceeding according to its own dependencies and becoming
required before capabilities that rely on reconciliation/drift.

Do not imply that §20 must be completed before the identity slice
unless an actual dependency is demonstrated.
```

---

## DEC-025 — D-13 — Implementation order

- **Status:** CURRENT
- **Source:** Owner decisions message (D-13).

```text
D-13 — IMPLEMENTATION ORDER

The implementation strategy is now:

PHASE 1
    Commit architecture source-of-truth.

PHASE 2
    Design §19.

PHASE 3
    Design §21.

PHASE 4
    Design §22 / recovery/lifecycle as required.

PHASE 5
    Establish the K3/P2 service boundary.

PHASE 6
    Implement the minimum SCC Core required by the locked
    contracts and completed persistence/audit/lifecycle gates.

PHASE 7
    CyberPanel K2 gate.

PHASE 8
    CyberPanel K2 implementation.

PHASE 9
    Identity binding.

PHASE 10
    CyberPanel presentation integration.

PHASE 11
    Capability implementation.

This is an architectural dependency order, not a requirement that
every possible future SCC feature be completed before a working
CyberPanel UI can ever exist.

At every stage, only implement what its governing contract permits.
```

---

## DEC-026 — D-14 — K3 / P2 clarification

- **Status:** CURRENT
- **Source:** Owner decisions message (D-14).
- **Related:** [`../open/p2-protocol.md`](../open/p2-protocol.md)

```text
D-14 — K3 / P2 CLARIFICATION

Your observation is accepted.

The P2 protocol is a real dependency for the K2 -> SCC boundary.

However, do not invent its final contract yet.

The P2 protocol should be designed as the appropriate architecture
gate before K3/K2 implementation.

The current architecture only establishes that:

    K2 talks to K3

and:

    K2 does not talk directly to K4/K5/K6.

The exact protocol:

    message format
    assertion format
    freshness
    replay resistance
    request binding
    error model
    transport
    endpoint exposure
    key provisioning

must be formally specified before implementation.
```

---

## DEC-027 — D-15 — K2 presentation question

- **Status:** CURRENT (records an OPEN question and an implementation prohibition)
- **Source:** Owner decisions message (D-15).
- **Related:** KF-01, KF-02; [`../../platforms/cyberpanel/k2-gate.md`](../../platforms/cyberpanel/k2-gate.md)

```text
D-15 — K2 PRESENTATION QUESTION

Your D-2 observation is correct.

There is a genuine architectural question concerning the exact
placement of the CyberPanel presentation surface.

Do NOT resolve it by assumption.

Record it as an OPEN CyberPanel K2 gate question.

The question is:

    Which portion of the CyberPanel-native presentation surface
    may execute inside K2, and what exact data/protocol boundary
    separates it from K3/K4, while preserving the §15 trust
    invariants and the §18 threat requirements?

The K2 gate must answer this.

Until then:

    do not implement the CyberPanel route
    do not implement the CyberPanel template
    do not implement the UI bridge
```

---

## DEC-028 — D-16 — First implementation boundary

- **Status:** CURRENT
- **Source:** Owner decisions message (D-16).

```text
D-16 — CURRENT FIRST IMPLEMENTATION BOUNDARY

The first eventual implementation target is NOT:

    "CyberPanel plugin"

It is:

    "SCC Core + CyberPanel K2 integration"

with explicit boundaries between them.

The first useful vertical slice will eventually establish:

    CyberPanel authenticated identity
            ↓
    K2 assertion
            ↓
    K3
            ↓
    K4 Principal resolution
            ↓
    authorization decision
            ↓
    response

before any host-changing capability is introduced.

No K6 operation is needed for that initial identity/authorization
slice.
```

---

## DEC-029 — D-17 — No premature execution

- **Status:** CURRENT
- **Source:** Owner decisions message (D-17).

```text
D-17 — NO PREMATURE EXECUTION

The following remain prohibited from implementation at this stage:

    shell execution
    generic command execution
    subprocess helpers
    arbitrary host writes
    firewall changes
    package management
    service management
    DNS changes
    mail changes
    filesystem remediation
    arbitrary plugin execution
    privileged CyberPanel operations

Do not create placeholder functions that secretly establish
these paths.
```

---

## DEC-030 — Phase A.5 confirmation — repository documentation rules

- **Status:** CURRENT
- **Source:** Phase A.5 owner confirmation message.
- **Constrains:** every document in `docs/`.

```text
Q1 — CONFIRMED
Use the proposed inline annotations in the foundational §1–§14 document.

The original §1–§14 source text must remain unchanged. Every annotation must be visibly delimited and clearly distinguishable from the original text.

Q2 — CONFIRMED
Do NOT place inline findings, conflict notes, or architectural commentary inside the locked §15, §16, or §17 documents.

Those documents remain clean normative specifications.

Known findings against them belong in the architecture index/open register.

Q3 — CONFIRMED
Remove only conversational/process wrapper text when creating standalone documents.

Do not remove, rewrite, renumber, or normalize substantive architectural content.

Formatting-only Markdown repairs remain permitted as specified in the plan.

Q4 — CONFIRMED
Use one consolidated decision log:

docs/architecture/decisions/decision-log.md

Do not split decisions into individual files.

Owner decision wording should be preserved verbatim where the plan specifies verbatim owner wording.

Q5 — CONFIRMED
Include both the Phase A report and reconciliation report as historical material.

They are historical/forensic artifacts, not current authority.

Their decisions do not independently establish current architecture.

Q6 — CONFIRMED
The superseded implementation brief gets a summary entry in the superseded register only.

Do not copy it verbatim into history.

Q7 — CONFIRMED
Never-approved §15 and §16 candidate texts, and the pre-clarification §17 candidate, receive register entries only.

Do not create competing historical copies.

Mark them clearly as NEVER APPROVED / NON-AUTHORITATIVE.

Q8 — CONFIRMED WITH ONE AMENDMENT

Use ANN-01 through ANN-32 as proposed EXCEPT ANN-25.

ANN-25 must be classified:

OPEN — CyberPanel K2 gate

Do not classify T-24 as currently resolved.

The actual CyberPanel installation/registration mechanism remains unresolved and is deferred to the CyberPanel K2 gate under D-5 / D-15.

All other ANN-01 through ANN-32 classifications are approved as proposed.

Q9 — CONFIRMED
Create the branch:

docs/architecture-source-of-truth

from:

main @ d7b1b9f

Do not commit directly to main.

ADDITIONAL §18 RULE

For:

docs/architecture/open/18-threat-model/18-gate-review.md

retain the historical forensic gate review, but add a clear non-normative header stating that it records the historical review of the §18 candidate and is NOT the current §18 authority.

In particular, the historical "PASS — READY FOR §19" wording must not be allowed to function as current authority.

Current §18 status is established by the architecture index, decision log, and open register.

ADDITIONAL EXECUTION RULES

1. Do not implement code.
2. Do not create schemas.
3. Do not create CI.
4. Do not create an installer.
5. Do not create .github/ content.
6. Do not modify CyberPanel.
7. Do not resolve open architecture questions by inference.
8. Do not silently reconcile contradictory historical material.
9. Do not rewrite locked §15–§17.
10. Do not invent §19–§22 behavior.
11. Do not invent the P2 protocol.
12. Do not resolve CyberPanel K2 presentation placement.
13. Do not resolve T-24 / CyberPanel installation until the CyberPanel K2 gate.
14. Preserve source IDs and numbering.
15. Preserve historical material as historical material.
16. The architecture index and decision log establish current authority according to D-11.
17. The repository must make it difficult for a future implementer to mistake historical, candidate, conditional, or open material for locked architecture.
```

> **Excerpt note (index text, not owner wording):** The Q9 owner text also lists the eight commit categories and
> the instruction to push the branch, open a PR and not merge. Those are process instructions for this repository
> bootstrap and are omitted from the excerpt above. The excerpt otherwise reproduces the owner's Q1–Q9 text, the
> ANN-25 amendment, the additional §18 rule and the execution rules.

---

## DEC-031 — PD19-01 — One authoritative owner and storage domain per data class

- **Status:** CURRENT (revised)
- **Source:** §19 owner disposition review; owner message for PD19-01 (2026-09-23).
- **Related:** §19.6, §19.8, §19.20 (S19-01, S19-02)
- **Requirement IDs (index, not owner wording):** R1 = the first quoted paragraph after "The owner-approved direction is:";
  R2 = the second quoted paragraph;
  R3 = the "ALSO NOTE" paragraph ("Therefore, do not make PD19-01 depend on the final wording of PD19-02 more than necessary.");
  R4 = the "TERMINOLOGY CLARIFICATION" paragraph (meaning of "owner" in §19).

```text
Continue the §19 OWNER DISPOSITION REVIEW.

The owner has now reviewed PD19-01.

OWNER DECISION — PD19-01
------------------------

Disposition:

REVISE

The owner accepts the underlying architectural principle, but does NOT accept the current wording unchanged.

The revision must preserve these two concepts:

1. Each SCC data class has exactly one authoritative owner and one authoritative storage domain.

2. The authoritative SCC storage domains remain distinct according to their defined trust and access boundaries and must not be consolidated or exposed to another component merely for implementation convenience.

The revised wording must also explicitly avoid an unintended interpretation that a data value may exist in only one physical location.

The owner-approved direction is:

> Each SCC data class has exactly one authoritative owner and one authoritative storage domain. This does not prohibit transient, derived, or explicitly permitted non-authoritative copies, provided those copies do not become an alternate authoritative source or weaken the access boundary of the authoritative domain.

And:

> The authoritative SCC storage domains identified by §19 must remain distinct according to their defined trust and access boundaries; they must not be consolidated or exposed to another component merely for implementation convenience.

ALSO NOTE
---------

PD19-01 should establish the general separation/ownership principle.

PD19-02 separately establishes the specific proposed name and internal organization of the K6 privileged storage domain (`SD-K6P`).

Therefore, do not make PD19-01 depend on the final wording of PD19-02 more than necessary.

TERMINOLOGY CLARIFICATION
-------------------------

When eventually incorporated into §19, the term "owner" should be explicitly distinguished from the baseline's Security System/business "Ownership" concept.

For §19, "owner" means the SCC component responsible for the authoritative persistence of the data class.

Do not make this change yet; merely carry it forward as part of the approved revision requirements.
```

> **Transcription note (PD19-01):** The closing "NEXT DECISION / Proceed to:" block, which requested the next
> review item and its format, is omitted as process-wrapper text.

> **Transcription note (session process):** The following review-session process lines are omitted; they
> governed only the review session and are not owner decisions: "IMPORTANT:"; "These are the owner's intended revision points, NOT authorization to edit the repository yet."; "Do NOT modify §19."; "Do NOT commit."; "Do NOT push."; "Do NOT update the decision log."; "Do NOT update the architecture index."; "Record this only in the working owner-disposition state for this review.".

---

## DEC-032 — PD19-02 — SD-K6P storage areas

- **Status:** CURRENT (accepted)
- **Source:** §19 owner disposition review; owner message for PD19-02 (2026-09-23).
- **Related:** §19.6 (SD-K6P); §19.7 (DC-13, DC-14)

```text
PD19-02 — ACCEPT

Accepted scope:
- SD-K6P is established as the named K6 privileged storage domain.
- CS (Credential Store), PI (Pre-image Store), and ST (Staging Area) are internal storage areas within K6's existing privileged domain.
- SD-K6P is NOT a new runtime component and does not add a K12 to the §15 component catalogue.
- DC-13 credential material and DC-14 credential metadata are authoritative within the Credential Store, subject to the unresolved K4 visibility question in OD19-05 / F19-07.

Carry forward these explicit non-decisions:
- OD19-02 at-rest encryption remains OPEN.
- OD19-05 / F19-07 K4 provisioning-state visibility remains OPEN.
- PD19-11 retention remains independently pending.
- PD19-12 credential-bearing file content remains independently pending.
- §22 provisioning, rotation, destruction, backup and uninstall mechanics remain DEFERRED.
```

> **Transcription note:** Process-wrapper lines ("No files changed", "No commit/push", "No decision-log update",
> "Proceed to …") are omitted (DEC-030 Q3). The text is otherwise verbatim.

> **Transcription note (session process):** The following review-session process lines are omitted; they
> governed only the review session and are not owner decisions: "Record this in the working owner-disposition state only."; "Do not edit any files, commit, push, or update the decision log.".

---

## DEC-033 — PD19-03 — Credential secret material only in SD-K6P / K6

- **Status:** CURRENT (accepted as locked-derived; clarification C-03a/C-03b)
- **Source:** §19 owner disposition review; owner message for PD19-03 (2026-09-23).
- **Related:** §19.20 (S19-03)
- **Requirement IDs (index, not owner wording):** C-03a = the first quoted paragraph (scope of S19-03); C-03b = the
  second quoted paragraph (F19-05 remains unresolved).

```text
PD19-03 — ACCEPT AS LOCKED-DERIVED, WITH CLARIFICATION

The owner confirms that the core credential-custody rule is already LOCKED by T-18, §15.12 and §16.9. PD19-03 does not create new authority and does not require a new owner decision to establish the underlying K6-only rule.

Carry forward this clarification for the eventual §19 wording:

> S19-03 applies only to credential secret material whose authoritative custody is assigned to K6 by the locked architecture—specifically Security System, parent-platform administrative/API, and endpoint credentials. It does not govern secrets explicitly assigned by higher authority to K2, off-host approvers, release owners, or other domains.

Also carry forward:

> F19-05 remains an unresolved finding. S19-03 does not itself authorize or solve any path by which credential material could transiently or durably appear outside K6.

Do not treat PD19-03 as resolving F19-05.

The transformed-credential issue identified from the conditional §18 material also remains unresolved and must not be silently solved by PD19-03.
```

> **Transcription note:** Process-wrapper lines ("No files changed", "No commit/push", "No decision-log update",
> "Proceed to …") are omitted (DEC-030 Q3). The text is otherwise verbatim.

> **Transcription note (session process):** The following review-session process lines are omitted; they
> governed only the review session and are not owner decisions: "Record this in the working owner-disposition state only."; "Do not edit files."; "Do not commit."; "Do not push."; "Do not update the decision log.".

---

## DEC-034 — PD19-04 — Authorization/audit atomicity and integrity

- **Status:** CURRENT (revised)
- **Source:** §19 owner disposition review; owner message for PD19-04 (2026-09-23).
- **Related:** §19.8, §19.15, §19.20 (S19-06)

```text
PD19-04 — REVISE

R4a — Authorization atomicity:

"For every K4 authorization state mutation for which §17 requires an audit record, the authorization mutation and its required audit record MUST become durable atomically: either both are committed or neither is committed."

R4b — Authorization-state integrity:

"K4 MUST NOT rely on authorization state that it cannot establish as valid. The mechanism for detecting corruption or loss of integrity is owned by the appropriate later architecture/implementation gate."

Carry forward these explicit boundaries:

- This does NOT make K7 and K8 a distributed atomic store.
- This does NOT define §21 audit format.
- This does NOT define tamper-evidence.
- This does NOT establish a universal fail-closed rule for ordinary domain-state corruption.
- Existing §15–§17 fail-closed rules remain authoritative.
```

> **Transcription note:** Process-wrapper lines ("No files changed", "No commit/push", "No decision-log update",
> "Proceed to …") are omitted (DEC-030 Q3). The text is otherwise verbatim.

> **Transcription note (session process):** The following review-session process lines are omitted; they
> governed only the review session and are not owner decisions: "Record in the working owner-disposition state only. No files changed."; "Do not edit files."; "Do not commit."; "Do not push."; "Do not update the decision log.".

---

## DEC-035 — PD19-05 — Audit fail-closed

- **Status:** CURRENT (revised)
- **Source:** §19 owner disposition review; owner message for PD19-05 (2026-09-23).
- **Related:** §19.15; §19.25 (criterion 4)

```text
PD19-05 — Owner disposition
REVISE
The core policy is sound as a separate decision from R4a: R4a guarantees atomicity for audited authorization state mutations, while PD19-05 closes the remaining gap for audited authorization events/decisions that do not themselves mutate authorization state, including the revalidation-before-K6-request case.
The important issue is the SYSTEM revocation-triggered cancellation exception. A-05 is locked and says that cancellation is a Fixed System Authority and does not depend on K7 authorization state. We should not silently create a new dependency on K7 merely because the cancellation must also be audited.
I would therefore revise the policy to distinguish whether the action itself requires authorization-state persistence from whether an audit record is required.
R5a — General audit fail-closed
A K4 action or authorization decision that requires an audit record MUST NOT be allowed to proceed when that required audit record cannot be durably recorded, unless a higher-authority locked rule explicitly requires the action to proceed independently of K7 authorization state.
This preserves the intended fail-closed rule while acknowledging that a higher-authority SYSTEM safety action can exist.
R5b — SYSTEM revocation cancellation
The exception should be narrowly tied to the already-locked A-05 authority, rather than creating a general audit bypass:
A SYSTEM revocation-triggered cancellation governed by A-05 MUST proceed according to its locked Fixed System Authority semantics and MUST NOT become dependent on K7 authorization state merely because its audit record cannot be durably written. Failure to record the required audit event does not invalidate or delay the cancellation.
That leaves the accountability problem visible rather than pretending it doesn't exist. The audit failure should be surfaced as an operational/audit condition for later §21/§22 treatment, but the cancellation itself must not wait for K7.
Denials
I would not create a special exception for denied authorization decisions.
A denied decision is still an authorization decision that §17 requires to be recorded. If the audit cannot be durably recorded, PD19-05 means the decision cannot complete normally. Since the result is already refusal, there is no safety expansion from this rule; the unresolved issue is how the failed audit attempt is represented/recovered, which belongs with the later audit/recovery design.
SYSTEM observation
No special exception is needed.
PD19-05 applies to actions/decisions that require an audit record. It should not be interpreted as imposing an audit-write dependency on ordinary SYSTEM observation that §17.16 expressly permits to continue when K7 is unavailable.
Durability definition
Leave “durably recorded” as a dependency for §21/implementation rather than deciding the storage mechanism here.
Availability consequence
Record it explicitly as a consequence, not as a reason to weaken the rule:
Audit-storage failure may cause refusal of all operations requiring durable audit until audit availability is restored. No bypass is created by this decision.
That is important because otherwise a later implementation could interpret audit exhaustion as permission to continue without auditing.
Owner decision
PD19-05 — REVISE
Carry forward:
R5a
A K4 action or authorization decision that requires an audit record MUST NOT be allowed to proceed when that required audit record cannot be durably recorded, unless a higher-authority locked rule explicitly requires the action to proceed independently of K7 authorization state.
R5b
A SYSTEM revocation-triggered cancellation governed by A-05 MUST proceed according to its locked Fixed System Authority semantics and MUST NOT become dependent on K7 authorization state merely because its audit record cannot be durably written. Failure to record the required audit event does not invalidate or delay the cancellation.
Also carry forward:

* No audit bypass is created.
* Denied authorization decisions remain subject to the audit requirement.
* Ordinary SYSTEM observation is not made dependent on K7 merely because PD19-05 exists.
* “Durably recorded” remains for §21/implementation to define.
* Audit-storage failure may therefore make audited operations unavailable until recovery.
* §21 still owns audit format, retention/capacity details and tamper-evidence.
* §22 owns recovery behavior.
* K8's separate fail-closed rule remains unaffected.
* Do not amend §17 or §15 from this decision unless a genuine contradiction is later demonstrated.
```

> **Transcription note:** Process-wrapper lines ("No files changed", "No commit/push", "No decision-log update",
> "Proceed to …") are omitted (DEC-030 Q3). The text is otherwise verbatim.

---

## DEC-036 — PD19-06 — C-writable configuration

- **Status:** CURRENT (revised)
- **Source:** §19 owner disposition review; owner message for PD19-06 (2026-09-23).
- **Related:** §19.7 (DC-03), §19.20 (S19-12)

```text
PD19-06 — Owner disposition
REVISE
The underlying security boundary is already substantially established by the locked architecture. The new decision should be the general configuration-classification rule, but it must explicitly avoid redefining §17 authorization state.
The biggest issue is the phrase “security-relevant configuration.” As written, it can collide with §17.20 and potentially with other future configuration categories. The clean boundary is:

* Authorization state remains governed by §17 and is not “configuration” for purposes of S19-12.
* Configuration that can widen execution authority remains outside C's writable domain.
* Configuration that can narrow security behavior may be C-writable if its own governing contract permits it.
* Non-security operational tuning may be C-writable.
* “Tuning” does not automatically mean “non-security”; the effect of the particular setting has to be classified.

I would therefore make the owner decision:
R6a — Configuration boundary
For S19-12, “configuration” does not include Principal enrollment, Role Memberships, Grants, Authorization Decisions, or other authorization state governed by §17. Those remain governed by §17 and its locked authorization model.
This is important because otherwise PD19-06 could accidentally override §17's explicit C/K7 model.
R6b — Widening prohibition
Configuration writable by C MUST NOT widen SCC authority or execution capability. Configuration that can widen authority or execution MUST be outside C's writable domain and governed by its applicable higher-authority control.
This captures the actual locked architectural principle without claiming that all security-relevant configuration must be root-only.
R6c — Permitted C-writable configuration
C-writable configuration MAY narrow security behavior or tune behavior that does not widen authority or execution, provided the applicable configuration contract permits the change.
That wording avoids the ambiguity in the current “narrow or tune non-security behaviour” sentence and accommodates §17.20's narrowing-only authorization policy.
Freshness/scheduling examples
I would not classify those examples globally here.
The fact that a freshness threshold or scheduling cadence can affect security-relevant behavior doesn't mean PD19-06 needs to decide its classification now. The governing contract for each configuration class should establish whether a value can:

* widen authority/execution,
* narrow behavior,
* or merely tune non-authoritative operational behavior.

That prevents §19 from silently making future §20/§21/§22 design decisions.
Compromised K4 / denial of service
No change is needed to address this separately.
The proposal does not promise that C-writable configuration is harmless. It establishes a boundary against authority/execution widening. A compromised K4 may still be able to cause availability or operational effects through configuration that is legitimately C-writable. That consequence should remain explicit rather than being treated as a violation of PD19-06.
PD19-07 dependency
PD19-07 should subsequently be evaluated against R6a–R6c. In particular, don't pre-approve “Integration configuration is C-writable” merely because it doesn't widen K6's physical authority. Its semantic effect still needs to be classified when PD19-07 is reviewed.
Owner decision
PD19-06 — REVISE
Carry forward:
R6a
For S19-12, “configuration” does not include Principal enrollment, Role Memberships, Grants, Authorization Decisions, or other authorization state governed by §17. Those remain governed by §17 and its locked authorization model.
R6b
Configuration writable by C MUST NOT widen SCC authority or execution capability. Configuration that can widen authority or execution MUST be outside C's writable domain and governed by its applicable higher-authority control.
R6c
C-writable configuration MAY narrow security behavior or tune behavior that does not widen authority or execution, provided the applicable configuration contract permits the change.
Also carry forward:

* Do not classify freshness thresholds or scheduling cadence globally in §19.
* Do not redefine §17.20.
* “Configuration” and “authorization state” remain distinct concepts.
* PD19-07 must be reviewed independently.
* A compromised K4 may still cause availability/operational effects through legitimately C-writable configuration; PD19-06 is an authority/execution-widening boundary, not a universal availability guarantee.
```

> **Transcription note:** Process-wrapper lines ("No files changed", "No commit/push", "No decision-log update",
> "Proceed to …") are omitted (DEC-030 Q3). The text is otherwise verbatim.

---

## DEC-037 — PD19-07 — Integration-specific configuration

- **Status:** CURRENT (revised)
- **Source:** §19 owner disposition review; owner message for PD19-07 (2026-09-23).
- **Related:** §19.5.1, §19.5.3 (D19-02), §19.7 (DC-06), §19.8

```text
PD19-07 — Owner disposition
REVISE
The proposed persistence boundary is workable, but accepting it as written would prematurely decide several things that §19 has not yet established—especially the write path, authorization of configuration changes, and the relationship to §20 desired state.
The important distinction is:
K4 may be the authoritative persistence owner without the Integration being the authority that is permitted to change that persistent state.
That distinction should be explicit.
R7a — Ownership and namespace
Accept the basic data-class decision:
Integration-specific configuration is an SCC data class whose authoritative owner is K4 and whose authoritative storage domain is SD-K7. It is namespaced by `integration_id`. K4 MUST NOT provide one Integration with another Integration's configuration.
This establishes storage ownership without implying that the Integration itself owns the authorization to modify it.
R7b — No credential material
Carry forward the existing locked-derived boundary:
Integration-specific configuration MUST NOT contain credential secret material whose authoritative custody is assigned to K6.
That is consistent with C-03a and should not be treated as a new credential-storage decision.
R7c — Write path remains open
This is the biggest unresolved part.
Do not accept “writers: C” as meaning that arbitrary C-side code may persist configuration.
Instead:
The mechanism by which Integration-specific configuration is created or changed is not established by PD19-07. Any write path MUST be authorized by the applicable SCC architecture and capability/authorization contract; K5 MUST NOT acquire an implicit write path merely by producing P5 output.
That directly addresses the concern about an untrusted Integration effectively gaining durable state through K4.
In particular, K5 output does not become an implicit configuration-write channel.
R7d — Configuration changes must have a governing contract
PD19-06 already requires C-writable configuration to remain within its permitted security boundary. PD19-07 should therefore not invent the actual semantics.
The permitted contents and security effect of Integration-specific configuration MUST be defined by the governing Integration/configuration contract. PD19-07 does not itself authorize configuration to widen authority or execution, and configuration changes remain subject to R6b/R6c.
This leaves open whether a future Integration's configuration is merely operational tuning, narrowing policy, or something else.
It also means we should not yet assign a §17 risk tier or audit requirement to configuration changes globally. Those depend on the eventual write/action contract.
R7e — K5 isolation
The namespacing rule should not be described as worker isolation.
Per-`integration_id` namespacing is a K4 persistence and delivery boundary. It is not an assertion that K5 workers are mutually isolated from one another.
That preserves the distinction the candidate correctly identifies: all K5 workers currently operate under the shared Integration identity model.
R7f — Platform Services
Do not silently include Platform Services in DC-06.
The candidate correctly identifies that Platform Services has a declaration identity relationship but is not an Integration. That means the scope needs to remain explicit:
PD19-07 applies to Integration-specific configuration. It does not by itself establish a storage class or configuration model for Platform Services. Platform Services configuration requires separate treatment if needed.
This avoids accidentally binding the future CyberPanel Platform Services worker to an Integration persistence model.
R7g — §20 boundary
Leave the desired-state boundary open:
PD19-07 does not decide whether a particular Integration configuration represents desired state under §20. Where an Integration configuration expresses desired Security System state, the §20 architecture governs that aspect once designed.
That prevents §19 from preempting the still-open reconciliation architecture.
Baseline §14
The proposed interpretation is acceptable as a candidate resolution, but I would not yet lock the exact baseline annotation.
Once the §19 contract is finalized, the baseline can be annotated to say, in substance, that “within the Integration boundary” is a logical ownership/scope statement, while authoritative durable persistence is provided by K4/SD-K7 under the §19 model.
That should happen as part of the final §19 change set rather than being invented now.
Owner decision
PD19-07 — REVISE
Carry forward:
R7a
Integration-specific configuration is an SCC data class whose authoritative owner is K4 and whose authoritative storage domain is SD-K7. It is namespaced by `integration_id`. K4 MUST NOT provide one Integration with another Integration's configuration.
R7b
Integration-specific configuration MUST NOT contain credential secret material whose authoritative custody is assigned to K6.
R7c
The mechanism by which Integration-specific configuration is created or changed is not established by PD19-07. Any write path MUST be authorized by the applicable SCC architecture and capability/authorization contract; K5 MUST NOT acquire an implicit write path merely by producing P5 output.
R7d
The permitted contents and security effect of Integration-specific configuration MUST be defined by the governing Integration/configuration contract. PD19-07 does not itself authorize configuration to widen authority or execution, and configuration changes remain subject to R6b/R6c.
R7e
Per-`integration_id` namespacing is a K4 persistence and delivery boundary. It is not an assertion that K5 workers are mutually isolated from one another.
R7f
PD19-07 applies to Integration-specific configuration. It does not by itself establish a storage class or configuration model for Platform Services.
R7g
PD19-07 does not decide whether a particular Integration configuration represents desired state under §20. Where an Integration configuration expresses desired Security System state, the §20 architecture governs that aspect once designed.
Also carry forward:

* Do not assign a global §17 risk tier to Integration configuration changes yet.
* Do not globally decide their audit requirement yet.
* Do not treat “writers: C” as authorization for arbitrary persistence.
* Do not create a K5 → K4 configuration-write channel through P5 implicitly.
* Baseline §14 annotation is deferred until the final §19 edit.
```

> **Transcription note:** Process-wrapper lines ("No files changed", "No commit/push", "No decision-log update",
> "Proceed to …") are omitted (DEC-030 Q3). The text is otherwise verbatim.

---

## DEC-038 — PD19-08 — Revoked-Principal tombstones

- **Status:** CURRENT (revised)
- **Source:** §19 owner disposition review; owner message for PD19-08 (2026-09-23).
- **Related:** §19.11.1, §19.12, §19.16, §19.20 (S19-08)

```text
PD19-08 — Owner disposition
REVISE
The locked requirement is non-reuse of `principal_id`. PD19-08 should establish the persistence mechanism needed to support that requirement, but it should not prematurely lock an instance-lifetime model, retain unnecessary identity data indefinitely, or claim that tombstones alone solve backup/restore.
The cleanest approach is to separate the identifier invariant from the retention mechanism.
R8a — Tombstone purpose and minimum content
Accept the tombstone concept, but make its purpose explicit:
A revoked Principal MUST have a retained tombstone sufficient to establish that its `principal_id` existed and MUST NOT be reused within the applicable SCC instance. The tombstone MUST contain no more identity information than is necessary to enforce that invariant and support required historical references.
This avoids automatically retaining `platform_subject_id`, display name, or other binding information forever.
The existing definition of tombstone as a retained minimal record proving that an identifier existed is therefore preserved, but “minimal” becomes a normative minimization requirement.
R8b — Non-reuse remains the authoritative invariant
PD19-08 does not redefine §17.1.4. The authoritative requirement remains that a `principal_id` is never reused. The tombstone is one persistence mechanism supporting that requirement, not the source of the requirement.
That distinction matters for restore.
R8c — Backup/restore is unresolved
The restore problem is real and should remain open.
A K7 rollback can remove tombstones created after the backup. Therefore:
PD19-08 does not establish that a K7 backup restore by itself preserves the `principal_id` non-reuse invariant. Backup/restore preservation of identifier non-reuse remains an open §22/implementation requirement.
We should not choose an ID-generation mechanism here merely to compensate for the restore issue.
R8d — “Life of the instance” is not locked yet
I would not accept “life of the instance” as the final retention boundary because the candidate itself acknowledges that the instance lifecycle is not yet defined.
Instead:
Revoked-Principal tombstones MUST NOT be removed by ordinary retention while the corresponding `principal_id` remains subject to the §17 non-reuse invariant. The precise instance lifecycle, uninstall/reinstall semantics, and final disposition of the tombstone are deferred to §22.
That preserves the actual security requirement without pretending §22 has already defined what an “instance” is.
R8e — No need to expand this decision to other IDs
Do not generalize PD19-08 to `grant_id`, Decision IDs, `authorization_ref`, `request_id`, etc.
Those identifiers have different lifecycle and replay requirements. The candidate already treats some of them differently, and there is no source-supported reason in this decision to create a universal identifier-nonreuse rule.
If a later gate determines that another identifier requires non-reuse, it can establish that separately.
R8f — Growth
No special architecture is needed here.
The retention requirement is intentionally durable, but the architecture should account for its storage implications later. We don't need to invent a tombstone compaction or archival mechanism now, particularly because deleting the tombstone could undermine the invariant.
Owner decision
PD19-08 — REVISE
Carry forward:
R8a
A revoked Principal MUST have a retained tombstone sufficient to establish that its `principal_id` existed and MUST NOT be reused within the applicable SCC instance. The tombstone MUST contain no more identity information than is necessary to enforce that invariant and support required historical references.
R8b
PD19-08 does not redefine §17.1.4. The authoritative requirement remains that a `principal_id` is never reused. The tombstone is one persistence mechanism supporting that requirement, not the source of the requirement.
R8c
PD19-08 does not establish that a K7 backup restore by itself preserves the `principal_id` non-reuse invariant. Backup/restore preservation of identifier non-reuse remains an open §22/implementation requirement.
R8d
Revoked-Principal tombstones MUST NOT be removed by ordinary retention while the corresponding `principal_id` remains subject to the §17 non-reuse invariant. The precise instance lifecycle, uninstall/reinstall semantics, and final disposition of the tombstone are deferred to §22.
R8e
PD19-08 does not establish identifier-nonreuse requirements for other identifier classes.
Also carry forward:

* Do not retain `platform_subject_id` or display information indefinitely merely because it is available.
* Do not select an ID-generation algorithm here.
* Do not resolve backup/restore mechanics here.
* Do not define “life of the instance” here.
* Do not create a universal identifier-retention rule.
* PD19-12 must remain coordinated with this decision.
```

> **Transcription note:** Process-wrapper lines ("No files changed", "No commit/push", "No decision-log update",
> "Proceed to …") are omitted (DEC-030 Q3). The text is otherwise verbatim.

---

## DEC-039 — PD19-09 — Retention of referenced authorization records

- **Status:** CURRENT (revised)
- **Source:** §19 owner disposition review; owner message for PD19-09 (2026-09-23).
- **Related:** §19.11.1, §19.12

```text
PD19-09 — Owner disposition
REVISE
The underlying principle is useful: authoritative records cannot be deleted while authoritative references still depend on them. But the candidate currently mixes direct references, transitive dependencies, K8 journal references, and off-host copies without defining which ones create an authoritative retention obligation.
I would keep the decision deliberately narrow.
R9a — Referential retention
An authoritative SD-K7 record MUST NOT be removed while an authoritative SCC record in SD-K7 requires that record to remain resolvable.
This gives us the invariant without prematurely defining every possible reference relationship.
For the specific authorization records named by PD19-09:
Revoked Grants, revoked Role Memberships, applicable policy revisions, Authorization Decisions, Decision status records, and Approval Records MUST remain resolvable for as long as required by an authoritative SCC record that depends on them.
R9b — Transitive dependencies
I would make the transitive relationship explicit rather than leaving “referenced” ambiguous:
Where an authoritative retained record depends on another authoritative record through a chain of authorization references, the dependency remains a retention obligation for the underlying record.
For example:
`Audit record → Authorization Decision → Grant`
means the Grant cannot disappear merely because the audit record does not directly contain the Grant as its own independent retention relationship.
This is a retention dependency, not a claim that every reference is semantically identical.
R9c — K8 is not silently added to the K7 retention rule
The K8 issue should remain open rather than treating every `authorization_ref` in K8 as an SD-K7 retention obligation.
The important distinction is that K8 is a separate authoritative domain under §16. Therefore:
PD19-09 does not by itself establish that a K8 reference creates an SD-K7 retention obligation. The consistency and retention relationship between K8 journal records and K7 authorization records remains subject to the §16/K8 and later recovery/retention design.
That prevents §19 from silently modifying §16.
The unresolved question is real: if K8 retains an `authorization_ref` beyond K7's retention, what does that reference mean? But that should be resolved deliberately.
R9d — Retention floor, not deletion command
PD19-09 should establish a minimum retention condition, not a deletion schedule:
PD19-09 establishes a retention floor. Once its retention dependencies no longer exist, removal is neither required nor automatically authorized by PD19-09; subsequent disposition remains governed by §21, §22, and PD19-12 as applicable.
This is important because otherwise “retained while referenced” could accidentally become “delete immediately when unreferenced.”
R9e — Job lifetime
The candidate's “at least the life of the referencing Job” should be retained, but expressed as a minimum dependency:
An Authorization Decision and the authorization records required to support an active Job MUST remain resolvable for the life of that Job.
That aligns with the existing §17 Job → Decision relationship without deciding what happens afterward.
R9f — Baseline policy revisions
Do not solve K11 baseline revision retention inside PD19-09.
This is a genuine upgrade/lifecycle dependency. If a retained Decision identifies a release-supplied policy revision that is no longer present after an upgrade, the architecture needs to determine how that historical revision remains interpretable.
Therefore:
PD19-09 does not establish retention mechanics for release-supplied baseline policy revisions in K11. Preservation and historical resolvability of those revisions across upgrade remains a §22 concern.
This keeps SD-K7 retention from implicitly forcing K11 storage behavior.
R9g — Off-host exports
Likewise, don't let a possible future audit export mechanism silently create indefinite local retention:
PD19-09 governs authoritative SCC records and references within their authoritative storage domains. It does not establish retention obligations for off-host audit exports or other non-authoritative copies.
That belongs with §21 / ODF-18-07 if and when those are designed.
R9h — Approval Records vs evidence
Keep these separate.
PD19-09 can establish retention for the K4 Approval Record in K7. It should not decide retention of the underlying approval evidence in K8.
Retention of Approval Records in SD-K7 does not establish retention requirements for approval evidence held in K8. Those remain governed by the applicable K8 lifecycle and recovery rules.
Owner decision
PD19-09 — REVISE
Carry forward:
R9a
An authoritative SD-K7 record MUST NOT be removed while an authoritative SCC record in SD-K7 requires that record to remain resolvable.
For the covered authorization records:
Revoked Grants, revoked Role Memberships, applicable policy revisions, Authorization Decisions, Decision status records, and Approval Records MUST remain resolvable for as long as required by an authoritative SCC record that depends on them.
R9b
Where an authoritative retained record depends on another authoritative record through a chain of authorization references, the dependency remains a retention obligation for the underlying record.
R9c
PD19-09 does not by itself establish that a K8 reference creates an SD-K7 retention obligation. The consistency and retention relationship between K8 journal records and K7 authorization records remains subject to the §16/K8 and later recovery/retention design.
R9d
PD19-09 establishes a retention floor. Once its retention dependencies no longer exist, removal is neither required nor automatically authorized by PD19-09; subsequent disposition remains governed by §21, §22, and PD19-12 as applicable.
R9e
An Authorization Decision and the authorization records required to support an active Job MUST remain resolvable for the life of that Job.
R9f
PD19-09 does not establish retention mechanics for release-supplied baseline policy revisions in K11. Preservation and historical resolvability of those revisions across upgrade remains a §22 concern.
R9g
PD19-09 governs authoritative SCC records and references within their authoritative storage domains. It does not establish retention obligations for off-host audit exports or other non-authoritative copies.
R9h
Retention of Approval Records in SD-K7 does not establish retention requirements for approval evidence held in K8. Those remain governed by the applicable K8 lifecycle and recovery rules.
Also carry forward:

* “Referenced” is now understood as an authoritative retention dependency, including transitive dependencies.
* K8 is not silently folded into SD-K7 retention.
* Baseline K11 revision preservation remains a §22 issue.
* Off-host audit retention remains §21/ODF-18-07.
* Approval Records and approval evidence remain distinct.
* No immediate deletion rule is created.
```

> **Transcription note:** Process-wrapper lines ("No files changed", "No commit/push", "No decision-log update",
> "Proceed to …") are omitted (DEC-030 Q3). The text is otherwise verbatim.

---

## DEC-040 — PD19-10 — Backup/export encryption; no root-protection claim

- **Status:** CURRENT (revised)
- **Source:** §19 owner disposition review; owner message for PD19-10 (2026-09-23).
- **Related:** §19.9, §19.10, §19.15, §19.16, §19.20 (S19-09, S19-10); Q19-01

```text
PD19-10 — Owner disposition
REVISE
There are two separate issues here that should not be collapsed:

1. What SCC requires when it deliberately creates a backup/export containing secret material.
2. What “credentials exist only within K6” means when ciphertext is copied outside K6.

The first can be established now. The second needs precise wording so PD19-10 does not accidentally contradict the locked credential-custody rule.
R10a — Secret-bearing SCC backups/exports
Accept the core confidentiality rule, but scope it to SCC-controlled backup/export artifacts:
When SCC deliberately creates a backup or export containing secret material, the secret-bearing artifact MUST be encrypted with a key that is not stored with that artifact.
This does not regulate arbitrary host-level snapshots or backups that SCC does not control.
That distinction is important because SCC cannot make a guarantee about a provider's or Local Root Operator's independent whole-host backup merely by declaring this rule.
R10b — K6 credential custody requires clarification
I would not accept the candidate's “SD-K6P material, if ever backed up” wording yet.
The locked architecture says credential material exists only in K6's root-only credential storage, and C-03b specifically preserves the unresolved transformed/copy issue.
We therefore need to carry this as an unresolved interpretation:
PD19-10 does not, by itself, authorize creation of a backup copy of K6-custodied credential secret material outside K6. Whether encrypted ciphertext representing such material may be retained outside K6 without violating the locked K6-only custody invariant remains unresolved.
That avoids making a new exception to §16 by implication.
In other words, do not infer from “encrypt it if backed up” that backing it up has been authorized.
R10c — Separate K6 backup question
The candidate's distinction between SD-K7 and SD-K6P should remain, but the actual K6 backup policy belongs in the recovery design:
PD19-10 does not require SD-K6P to be backed up. Any decision to back up K6 privileged storage, and the resulting custody semantics, remains subject to §22 and the locked K6 credential-custody constraints.
This preserves the possibility that the eventual recovery architecture determines that certain K6 material is never backed up.
R10d — “Secret material” definition
I would not narrow S19-09 to only C-03a's K6 credentials.
The candidate deliberately uses the broader term “secret material,” and PD19-10 should cover any SCC secret material that legitimately exists in a storage domain and is deliberately exported.
However, that does not create permission for additional secret classes to exist.
So:
“Secret material” in PD19-10 means secret material that SCC is otherwise authorized to hold under the governing architecture. PD19-10 does not authorize creation or storage of new secret classes.
That preserves the distinction between the general export protection rule and C-03a's narrower K6 custody rule.
R10e — Separately held key
Keep the requirement:
The encryption key protecting a secret-bearing SCC backup/export MUST NOT be stored with the artifact it protects.
But leave key custody, location, algorithms, recovery and rotation to §22/OD19-02 as appropriate.
No decision is needed here about whether the key is off-host, root-controlled, externally held, etc.
R10f — Claims restriction
Accept the encryption portion:
SCC MUST NOT claim that on-host at-rest encryption protects SCC data against a root-equivalent compromise.
This follows the locked boundary that root is outside the SCC trust boundary.
But split the erasure statement out of PD19-10. The second half of S19-10 belongs to PD19-12 and should not be accepted as part of this decision.
R10g — At-rest key failure
I would leave the proposed failure rule open.
The candidate says:
“At-rest key material unavailable (if adopted) → ... fail closed”
But OD19-02 has not decided whether host at-rest encryption exists, what it protects, or what its key hierarchy is.
Therefore:
PD19-10 does not establish a general fail-closed rule for unavailable at-rest encryption keys. Any such behavior remains contingent on OD19-02 and the affected storage domain's lifecycle/recovery design.
That prevents us from locking behavior around a technology/design that has not yet been selected.
Owner decision
PD19-10 — REVISE
Carry forward:
R10a
When SCC deliberately creates a backup or export containing secret material, the secret-bearing artifact MUST be encrypted with a key that is not stored with that artifact.
R10b
PD19-10 does not, by itself, authorize creation of a backup copy of K6-custodied credential secret material outside K6. Whether encrypted ciphertext representing such material may be retained outside K6 without violating the locked K6-only custody invariant remains unresolved.
R10c
PD19-10 does not require SD-K6P to be backed up. Any decision to back up K6 privileged storage, and the resulting custody semantics, remains subject to §22 and the locked K6 credential-custody constraints.
R10d
“Secret material” in PD19-10 means secret material that SCC is otherwise authorized to hold under the governing architecture. PD19-10 does not authorize creation or storage of new secret classes.
R10e
The encryption key protecting a secret-bearing SCC backup/export MUST NOT be stored with the artifact it protects.
R10f
SCC MUST NOT claim that on-host at-rest encryption protects SCC data against a root-equivalent compromise.
R10g
PD19-10 does not establish a general fail-closed rule for unavailable at-rest encryption keys. Any such behavior remains contingent on OD19-02 and the affected storage domain's lifecycle/recovery design.
Also carry forward:

* SCC-controlled backup/export is distinct from arbitrary host/provider backups.
* No authorization is created for credential material to leave K6 merely because encryption is proposed.
* No decision yet on whether encrypted K6 credential ciphertext can exist outside K6.
* Key custody/location/algorithm/recovery remain open.
* The physical-erasure claim belongs to PD19-12, not PD19-10.
```

> **Transcription note:** Process-wrapper lines ("No files changed", "No commit/push", "No decision-log update",
> "Proceed to …") are omitted (DEC-030 Q3). The text is otherwise verbatim.

---

## DEC-041 — PD19-11 — K8 and pre-image retention

- **Status:** CURRENT (revised)
- **Source:** §19 owner disposition review; owner message for PD19-11 (2026-09-23).
- **Related:** §19.12, §19.20 (S19-07); §19.25 (criterion 4); Q19-02

```text
PD19-11 — Owner disposition
REVISE
This one needs more separation than the candidate currently provides. Several pieces are genuinely locked-derived, but there are three distinct retention problems:

1. Replay/idempotency/nonce safety records
2. K7 → K8 audit-reference retention
3. Pre-image retention

The biggest issue is the candidate's grouping of `request_id` and idempotency records under one retention period. The source analysis correctly identifies that the locked replay window does not establish an expiration for X-32's successful-idempotency protection.
R11a — Separate request/replay records from idempotency records
Do not accept the current combined row.
K8 records required to enforce the §16 replay-acceptance window MUST be retained for at least that window. This requirement does not by itself establish a retention period for idempotency records governed by X-32.
And separately:
An idempotency record required to establish that a prior request with the same idempotency key completed SUCCESSFULLY MUST remain available for as long as necessary to enforce X-32. The retention period and any permitted idempotency-key reuse semantics remain open.
This avoids silently inventing either indefinite retention or an expiration rule.
The important point is that X-32 is the authority, not the §16.11 replay window.
R11b — Approval nonce retention remains bounded by the evidence deadline
Keep the locked-derived rule:
A used approval nonce MUST remain recorded in K8 for at least the period necessary to enforce its single-use property through the deadline of the approval evidence to which it belongs.
But the maximum horizon remains OD19-03 / F19-06.
Do not solve that horizon in PD19-11.
R11c — UNKNOWN/PARTIAL/dangling outcomes
Accept this as locked-derived:
K8 records required to prevent unsafe re-execution or establish reconciliation of UNKNOWN or PARTIAL outcomes MUST remain available until the applicable reconciliation requirement has been satisfied.
That preserves X-30/X-32 without inventing a general retention period after reconciliation.
R11d — K7 audit → K8 retention
I would accept the principle conditionally, but explicitly recognize the cross-domain dependency.
The rule can be:
Where an authoritative K4 audit record in SD-K7 contains a `journal_seq` reference that requires the corresponding K8 journal record to remain resolvable, that K8 record MUST be retained for at least as long as the authoritative audit record requires the reference to remain resolvable.
This is deliberately narrower than “all K7 references bind K8.”
It also does not contradict R9c. R9c said that a K8 reference does not automatically create an SD-K7 retention obligation. PD19-11 establishes the reverse relationship because the architecture explicitly places the audit reference in K7 and requires that reference to remain meaningful.
That asymmetry should be recorded, not silently normalized.
R11e — Pressure rule
I would accept the no-eviction safety property, with its scope made explicit:
K8 MUST NOT evict records whose retention is required to enforce replay protection, idempotency safety, approval-nonce single use, unresolved-outcome reconciliation, or an authoritative K7 audit reference. If K8 cannot preserve those required records, K6 MUST refuse new requests in accordance with X-29.
This does not say every K8 record is permanently retained.
Records outside the protected classes may have lifecycle/eviction rules later.
Also explicitly preserve the availability consequence:
K8 capacity exhaustion may therefore prevent new K6 requests until sufficient protected capacity is restored; PD19-11 creates no bypass or unjournaled mode.
That follows the existing X-29 boundary rather than introducing a new one.
R11f — Pre-images remain separate
Do not accept the current pre-image rule as a complete decision.
The principle can be retained:
Pre-image retention MUST be bounded rather than indefinite, and the applicable retention MUST be declared for the relevant scope entry.
But the proposed global maximum in the K11 Global Execution Policy should remain open pending OD19-07 / §16 review.
Also, PD19-11 should not decide what happens when a pre-image expires.
The later design needs to establish whether expiration affects:

* `file.restore_preimage`;
* compensation/recovery expectations;
* credential-bearing staged/pre-image material;
* PD19-16 credential lifecycle.

Those are separate questions.
R11g — Credential-bearing pre-images
Carry forward the interaction with C-03a:
A pre-image containing credential secret material remains subject to the applicable K6 credential-custody and destruction requirements. PD19-11 does not authorize retention of credential material beyond those requirements.
This doesn't decide the unresolved “ciphertext outside K6” issue from PD19-10.
Owner decision
PD19-11 — REVISE
Carry forward:
R11a
K8 records required to enforce the §16 replay-acceptance window MUST be retained for at least that window. This requirement does not by itself establish a retention period for idempotency records governed by X-32.
An idempotency record required to establish that a prior request with the same idempotency key completed SUCCESSFULLY MUST remain available for as long as necessary to enforce X-32. The retention period and any permitted idempotency-key reuse semantics remain open.
R11b
A used approval nonce MUST remain recorded in K8 for at least the period necessary to enforce its single-use property through the deadline of the approval evidence to which it belongs.
R11c
K8 records required to prevent unsafe re-execution or establish reconciliation of UNKNOWN or PARTIAL outcomes MUST remain available until the applicable reconciliation requirement has been satisfied.
R11d
Where an authoritative K4 audit record in SD-K7 contains a `journal_seq` reference that requires the corresponding K8 journal record to remain resolvable, that K8 record MUST be retained for at least as long as the authoritative audit record requires the reference to remain resolvable.
R11e
K8 MUST NOT evict records whose retention is required to enforce replay protection, idempotency safety, approval-nonce single use, unresolved-outcome reconciliation, or an authoritative K7 audit reference. If K8 cannot preserve those required records, K6 MUST refuse new requests in accordance with X-29.
R11f
Pre-image retention MUST be bounded rather than indefinite, and the applicable retention MUST be declared for the relevant scope entry.
R11g
A pre-image containing credential secret material remains subject to the applicable K6 credential-custody and destruction requirements. PD19-11 does not authorize retention of credential material beyond those requirements.
Also carry forward:

* Do not combine replay-window retention with idempotency retention.
* Do not decide idempotency-key reuse semantics here.
* OD19-03 remains responsible for the approval-horizon problem.
* The K7 → K8 retention dependency is intentionally asymmetric with R9c; document that rather than assuming symmetry.
* Ordinary/unprotected K8 records may have separate lifecycle rules.
* Do not yet put the pre-image global maximum into K11 without resolving OD19-07 / §16 implications.
* Do not decide pre-image expiration/restore semantics here.
* No bypass or unjournaled K6 mode is created.
```

> **Transcription note:** Process-wrapper lines ("No files changed", "No commit/push", "No decision-log update",
> "Proceed to …") are omitted (DEC-030 Q3). The text is otherwise verbatim.

---

## DEC-042 — PD19-12 — Deletion model (A) and credential-bearing-content authoring rule (B)

- **Status:** CURRENT (revised)
- **Source:** §19 owner disposition review; one owner message containing PD19-12(A) and PD19-12(B) (2026-09-23).
- **Related:** §19.11.1, §19.13, §19.13.1, §19.16, §19.20 (S19-10)

```text
PD19-12(A) — Deletion/destruction model
Owner decision: REVISE
The candidate is combining several lifecycle decisions that should remain distinct. In particular, R8d, R9d, R11f, and PD19-16 have already deliberately left parts of this open.
R12A-1 — No physical-erasure claim
Accept:
SCC MUST NOT claim that SCC-controlled deletion guarantees physical erasure of data from storage media, filesystem journals, backups outside SCC's control, or storage controlled by root or another external party.
This is a claims boundary, not a guarantee about what SCC can or cannot make locally unusable.
R12A-2 — Append-only records
Revise the candidate's “removed only by §21 retention expiry” language so it does not conflict with R9d or the later §22 removal model:
Append-only records MUST NOT be edited in place. Their authoritative removal, if permitted, MUST occur only through an explicitly defined retention or lifecycle disposition that preserves the applicable architectural invariants. PD19-12 does not itself authorize removal merely because a retention period has elapsed.
This preserves the distinction between:

* immutability/append-only semantics;
* a retention floor;
* actual deletion authorization;
* SCC instance removal/recovery.

That is consistent with R9d.
R12A-3 — Principals
Do not retain the absolute phrase “Principals are never deleted.”
Revise it to preserve R8d:
A Principal is never deleted in a manner that violates the §17 `principal_id` non-reuse invariant. A revoked Principal's required tombstone remains subject to R8d; final disposition of the Principal record and tombstone is deferred to §22.
This avoids creating a conflict between PD19-12 and the already accepted R8d.
R12A-4 — Credential destruction
Do not lock the candidate's complete destruction state machine here.
The candidate is correct that credential destruction must make the handle unusable before reporting successful destruction, but that is already tightly coupled to PD19-16.
Therefore:
Credential destruction MUST NOT be reported complete until the credential handle is no longer resolvable for credential use. Detailed destruction, DESTROYING-state, retry, idempotency, and recovery semantics remain subject to PD19-16 and §22.
This establishes the important safety ordering without prematurely duplicating PD19-16.
R12A-5 — Pre-images
Do not accept “destroyed at the end of declared retention” as a complete rule yet.
R11f deliberately left expiration semantics open.
Instead:
Pre-image retention MUST remain bounded as established by PD19-11. What occurs when that retention period expires, including destruction and its effect on `file.restore_preimage`, remains subject to the later pre-image lifecycle/recovery design.
This prevents PD19-12 from silently deciding a question that PD19-11 explicitly left open.
R12A-6 — SCC removal
Accept the deferral:
SCC instance removal and the disposition of SCC state, including retained authorization records, tombstones, K8 data, credentials, pre-images, and other persistent material, are deferred to §22.
That is the correct place for the complete uninstall/recovery lifecycle.
A7 — Append-only compromise boundary
No new claim is needed here. The wording should not imply that “append-only” is an enforcement guarantee against root or a compromised K4. The existing trust-boundary limitations remain authoritative.
PD19-12(A) disposition
REVISE
Carry forward:
R12A-1
SCC MUST NOT claim that SCC-controlled deletion guarantees physical erasure of data from storage media, filesystem journals, backups outside SCC's control, or storage controlled by root or another external party.
R12A-2
Append-only records MUST NOT be edited in place. Their authoritative removal, if permitted, MUST occur only through an explicitly defined retention or lifecycle disposition that preserves the applicable architectural invariants. PD19-12 does not itself authorize removal merely because a retention period has elapsed.
R12A-3
A Principal is never deleted in a manner that violates the §17 `principal_id` non-reuse invariant. A revoked Principal's required tombstone remains subject to R8d; final disposition of the Principal record and tombstone is deferred to §22.
R12A-4
Credential destruction MUST NOT be reported complete until the credential handle is no longer resolvable for credential use. Detailed destruction, DESTROYING-state, retry, idempotency, and recovery semantics remain subject to PD19-16 and §22.
R12A-5
Pre-image retention MUST remain bounded as established by PD19-11. What occurs when that retention period expires, including destruction and its effect on `file.restore_preimage`, remains subject to the later pre-image lifecycle/recovery design.
R12A-6
SCC instance removal and the disposition of SCC state, including retained authorization records, tombstones, K8 data, credentials, pre-images, and other persistent material, are deferred to §22.
PD19-12(B) — Credential-bearing-content authoring rule
Owner decision: REVISE
I would adopt the interim prohibition, but tighten its scope and its lifetime.
The important thing is that B is an authoring/release constraint, not a solution to F19-05. The candidate itself correctly identifies that it cannot prevent credential material from being placed into an incorrectly classified arbitrary `blob`.
R12B-1 — Interim authoring prohibition
Until OD19-04 is resolved, a K11 WRITE scope entry MUST NOT target a resource declared by the applicable execution contract to contain credential-bearing content.
This is narrower and more precise than simply saying “credential-bearing content,” because §16 already has the concept of a resource declared to contain credentials.
R12B-2 — No false claim of complete prevention
Explicitly preserve:
This authoring restriction does not establish that arbitrary `blob` content cannot contain credential material and does not resolve F19-05.
That is important. Otherwise someone could later interpret the release rule as proving that credentials can never pass through K4/K7.
R12B-3 — Misclassification
Do not create a new runtime detection mechanism here.
PD19-12(B) does not establish runtime inspection or classification of arbitrary `blob` content. Enforcement is through release-authoring/validation controls consistent with A-23 unless a later architecture explicitly provides another mechanism.
R12B-4 — Lifetime
Do not make the prohibition's future status depend on the outcome being “a §16 amendment.”
Instead:
The prohibition remains in force until OD19-04 establishes an authoritative disposition for credential-bearing WRITE content. Its eventual replacement, narrowing, or continuation must follow that disposition.
That handles both possible outcomes.
If OD19-04 ultimately concludes that no safe §16 path should exist, the prohibition can remain. If it authorizes a safe handle-based mechanism, the rule can be revised accordingly.
R12B-5 — Functional consequences
No special exception should be created for TLS/private-key deployment or Integration configuration.
If a capability needs to write credential-bearing content, that capability remains unavailable under the interim authoring rule until an authoritative path exists.
That is a consequence of the rule, not a reason to weaken it.
PD19-12(B) disposition
REVISE
Carry forward:
R12B-1
Until OD19-04 is resolved, a K11 WRITE scope entry MUST NOT target a resource declared by the applicable execution contract to contain credential-bearing content.
R12B-2
This authoring restriction does not establish that arbitrary `blob` content cannot contain credential material and does not resolve F19-05.
R12B-3
PD19-12(B) does not establish runtime inspection or classification of arbitrary `blob` content. Enforcement is through release-authoring/validation controls consistent with A-23 unless a later architecture explicitly provides another mechanism.
R12B-4
The prohibition remains in force until OD19-04 establishes an authoritative disposition for credential-bearing WRITE content. Its eventual replacement, narrowing, or continuation must follow that disposition.
R12B-5
A capability requiring credential-bearing WRITE content remains unavailable under the interim authoring rule until an authoritative path exists.
Also carry forward:

* B does not solve F19-05.
* B does not authorize credentials to leave K6.
* B does not create runtime credential detection.
* The §16 credential-bearing-resource classification should be reused rather than inventing a competing definition.
* No §16 amendment is made by PD19-12.
```

> **Transcription note:** Process-wrapper lines ("No files changed", "No commit/push", "No decision-log update",
> "Proceed to …") are omitted (DEC-030 Q3). The text is otherwise verbatim.

---

## DEC-043 — PD19-13 — Material SCC components must not persist

- **Status:** CURRENT (revised)
- **Source:** §19 owner disposition review; owner message for PD19-13 (2026-09-23).
- **Related:** §19.9, §19.20 (S19-04)

```text
PD19-13 — Owner disposition
REVISE
The three categories should remain together as a single prohibition, but the scope of “SCC component” and the distinction between persistent custody and transient exposure need to be made explicit.
The source material supports a stronger distinction than the candidate currently makes:

* platform session material is allowed to transit K2/K3 under the locked §15.12 rules;
* approver private keys are intended to remain outside SCC and only signatures enter the SCC authorization flow;
* release signing private keys are outside the K11 trust-anchor model.

I would therefore revise as follows.
R13a — SCC component scope
For this decision:
“SCC component” includes K2 through K8 and K11, and any SCC-supplied runtime or service that is part of the SCC trust architecture. It does not include the Browser/K0 or an external operator-controlled approval/signing environment merely because SCC interacts with it.
This makes K2 unambiguously covered.
That matters because otherwise PD19-13 would leave a potentially important ambiguity in the CyberPanel K2 gate.
R13b — Parent-platform session
The platform-session prohibition should preserve the exact locked transient exception:
The parent-platform session MUST NOT be persisted by an SCC component. K2/K3 may process or relay the session only as permitted by §15.12; K3 MUST strip it and MUST NOT persist, log, or forward it.
This does not prohibit the transient handling already authorized by §15.12.
It also does not decide whether K2 may retain some derived, non-bearer identity information; that remains governed by the K2 architecture and P2.
R13c — Approver private keys
Use a stronger rule than merely “must not persist”:
Approver private keys MUST NOT enter or be persisted by an SCC component. SCC receives only the resulting approval signature and associated verification evidence required by §17.
That matches the candidate's own “Never enters SCC; only signatures do” distinction and avoids creating a loophole where an SCC component could transiently process the private key without persisting it.
It does not prohibit an external approval tool from holding the key.
R13d — Release signing private keys
Similarly:
Release signing private keys MUST NOT enter or be persisted by an SCC component. SCC receives and relies only on the corresponding public release trust anchors and signed release artifacts.
This establishes the custody boundary without choosing where the private keys actually live.
R13e — Approval/signing tools
Do not classify the external approval tool as an SCC component merely because SCC ships, invokes, or interoperates with it.
The important boundary is whether the tool is actually part of the SCC trust/runtime architecture.
Therefore:
Operator-controlled approval/signing environments outside the SCC component boundary are not subject to PD19-13's SCC persistence prohibition, but their key-custody requirements remain governed by §17, §22, and the applicable key-custody decision.
This preserves the possibility described by ODF-18-08 without deciding that custody model now.
R13f — No complete-secret inventory
Do not turn S19-04 into a universal “these are the only secrets SCC cannot persist” rule.
The candidate already identifies other separately governed material, including K2 assertion-signing material and SCC bearer/session material.
PD19-13 is limited to the three named material classes and does not supersede more restrictive custody rules elsewhere in the architecture.
That prevents an accidental implication that anything not listed here is automatically permitted.
R13g — No custody decision
PD19-13 should not select:

* off-host vs host-local approval key custody;
* release-signing infrastructure;
* K2 assertion-key custody;
* P2 session/assertion mechanics.

Those remain separate architecture questions.
Owner decision
PD19-13 — REVISE
Carry forward:
R13a
“SCC component” includes K2 through K8 and K11, and any SCC-supplied runtime or service that is part of the SCC trust architecture. It does not include the Browser/K0 or an external operator-controlled approval/signing environment merely because SCC interacts with it.
R13b
The parent-platform session MUST NOT be persisted by an SCC component. K2/K3 may process or relay the session only as permitted by §15.12; K3 MUST strip it and MUST NOT persist, log, or forward it.
R13c
Approver private keys MUST NOT enter or be persisted by an SCC component. SCC receives only the resulting approval signature and associated verification evidence required by §17.
R13d
Release signing private keys MUST NOT enter or be persisted by an SCC component. SCC receives and relies only on the corresponding public release trust anchors and signed release artifacts.
R13e
Operator-controlled approval/signing environments outside the SCC component boundary are not subject to PD19-13's SCC persistence prohibition, but their key-custody requirements remain governed by §17, §22, and the applicable key-custody decision.
R13f
PD19-13 is limited to the three named material classes and does not supersede more restrictive custody rules elsewhere in the architecture.
Also carry forward:

* K2 is explicitly within scope.
* Transient parent-session handling remains governed by locked §15.12.
* Approver/release private keys have a stronger “must not enter” boundary than merely “must not persist.”
* No custody model is selected here.
* No implication that unlisted secrets are automatically permissible.
```

> **Transcription note:** Process-wrapper lines ("No files changed", "No commit/push", "No decision-log update",
> "Proceed to …") are omitted (DEC-030 Q3). The text is otherwise verbatim.

---

## DEC-044 — PD19-14 — SCC session tokens

- **Status:** CURRENT (revised)
- **Source:** §19 owner disposition review; owner message for PD19-14 (2026-09-23).
- **Related:** §19.9, §19.19, §19.20 (S19-14)

```text
PD19-14 — Owner disposition
REVISE
The core rule is appropriate, but it needs to be expressed as a property of persisted authentication material, not merely as “the string isn't stored in plaintext.” Otherwise reversible encryption or encoding could technically satisfy the wording while leaving K4 holding recoverable bearer credentials.
The other important point is to keep SCC session tokens distinct from K2 identity assertions. P2 should not be pre-decided by PD19-14.
R14a — Scope
Keep the candidate's narrow scope:
PD19-14 applies to SCC session tokens issued or accepted as SCC bearer credentials. It does not, by itself, classify K2 identity assertions, approval evidence, or other authentication material. Those remain governed by their respective architecture.
This avoids silently expanding the decision to assertions.
If the later P2 or K2 architecture determines that a particular assertion is itself a persisted bearer credential, it can establish the appropriate rule there.
R14b — Persistence property
Replace “not plaintext” with the actual security property:
An SCC session token MUST NOT be persisted in a form from which the token can be recovered for direct bearer use.
That is substantially clearer.
A one-way verifier/hash-like representation could satisfy it; reversible encoding would not. Encryption could only satisfy it if the resulting architecture genuinely prevents the persisted material from functioning as a recoverable bearer token under the applicable threat model—but we should not make an encryption design decision here.
R14c — No P2 session design
Preserve the deferral:
PD19-14 does not select stateful versus stateless sessions, token format, session lifetime, invalidation semantics, or the form of K4 validation state. Those remain P2 decisions.
This is important because P2 may determine whether there is durable validation state at all.
R14d — No new session-key custody decision
The candidate correctly identifies a possible gap if P2 chooses self-contained MAC/signing tokens.
Do not solve it here.
If P2 requires a persistent secret key for session validation or token issuance, that key constitutes a separately governed secret class whose custody must be established by the applicable architecture gate. PD19-14 does not authorize or define that custody.
That is preferable to treating the key as implicitly permitted or prohibited.
R14e — Logging
I would not expand the rule into a general logging policy here.
The existing architecture already constrains K3/K5 logging, and §21 will define audit/logging semantics. PD19-14's core decision is about persistence of usable SCC session tokens.
However, the final wording should not be interpreted as permission to put a recoverable session token into K4 audit simply because audit is not technically “session storage.” Existing credential/audit constraints remain applicable.
R14f — K4 validation state
We can explicitly distinguish validation state from the token:
K4 may retain session validation state only in a form permitted by P2 and consistent with R14b; PD19-14 does not require durable session state.
Owner decision
PD19-14 — REVISE
Carry forward:
R14a
PD19-14 applies to SCC session tokens issued or accepted as SCC bearer credentials. It does not, by itself, classify K2 identity assertions, approval evidence, or other authentication material. Those remain governed by their respective architecture.
R14b
An SCC session token MUST NOT be persisted in a form from which the token can be recovered for direct bearer use.
R14c
PD19-14 does not select stateful versus stateless sessions, token format, session lifetime, invalidation semantics, or the form of K4 validation state. Those remain P2 decisions.
R14d
If P2 requires a persistent secret key for session validation or token issuance, that key constitutes a separately governed secret class whose custody must be established by the applicable architecture gate. PD19-14 does not authorize or define that custody.
R14e
PD19-14 does not establish a general logging or audit-format rule. Existing credential-handling constraints and the later §21 audit design remain applicable.
R14f
K4 may retain session validation state only in a form permitted by P2 and consistent with R14b; PD19-14 does not require durable session state.
Also carry forward:

* “Plaintext” is replaced by the stronger non-recoverable-for-direct-bearer-use property.
* Do not decide whether SCC sessions are stateful/stateless.
* Do not classify K2 assertions under PD19-14.
* Do not implicitly authorize a session-signing/MAC key.
```

> **Transcription note:** Process-wrapper lines ("No files changed", "No commit/push", "No decision-log update",
> "Proceed to …") are omitted (DEC-030 Q3). The text is otherwise verbatim.

---

## DEC-045 — PD19-15 — No bootstrap or recovery secret

- **Status:** CURRENT (revised)
- **Source:** §19 owner disposition review; owner message for PD19-15 (2026-09-23).
- **Related:** §19.9, §19.16, §19.20 (S19-05)

```text
PD19-15 — Owner disposition
REVISE
The core decision is sound, but the phrase “no bootstrap or recovery secret” is too broad. It could accidentally prohibit operational secrets that are provisioned or regenerated during a recovery operation without themselves granting recovery authority.
The key distinction should be:
A secret used to perform or support recovery is not necessarily a recovery secret. A recovery secret is one whose possession itself confers bootstrap or recovery authority.
That distinction also prevents PD19-15 from colliding with PD19-10 backup-key questions, PD19-16 operational credentials, or the K2 signing-key reprovisioning path.
R15a — Define the prohibited secret by function
I would revise S19-05 to:
SCC MUST NOT create, persist, or rely upon a secret whose possession itself confers bootstrap or recovery authority. Bootstrap and recovery authority remains OS root acting host-locally through K9, subject to the recovery gate.
This is materially better than “SCC MUST NOT create or hold any bootstrap or recovery secret,” because it identifies what makes a secret prohibited: it is an alternative authority mechanism.
R15b — Operational secrets are not recovery authority
Explicitly preserve the distinction:
PD19-15 does not prohibit provisioning, rotation, replacement, or temporary handling of operational secrets that are otherwise authorized by the architecture, including Security System credentials or K2 operational signing material, provided those secrets do not themselves confer bootstrap or recovery authority.
This does not authorize those secrets; their individual custody rules still apply.
R15c — Backup encryption keys
Do not decide this here.
The backup-encryption key required by R10a/R10e could be generated or held as part of a future recovery architecture, but PD19-15 should not classify it as a recovery secret merely because it is needed to restore encrypted material.
Therefore:
PD19-15 does not determine whether a backup-encryption or restore key is a “recovery secret.” Its custody and authority properties must be established by the applicable §22/OD19-02 design.
The functional test from R15a should ultimately determine the classification.
R15d — K9 authority remains open
Do not expand “authority is OS root through K9” into a complete K9 capability definition.
PD19-15 does not define the scope or operations of K9. Bootstrap and recovery authority remains host-local and K9's exact authority remains subject to the recovery gate.
That preserves T-29 and the existing open questions.
R15e — Initial provisioning
Likewise, root provisioning of operational credentials should not be confused with bootstrap authority.
The first-admin membership remains governed by A-07. PD19-15 does not prohibit the Local Root Operator from provisioning operational credentials into K6 where §22/PD19-16 authorizes that operation.
Owner decision
PD19-15 — REVISE
Carry forward:
R15a
SCC MUST NOT create, persist, or rely upon a secret whose possession itself confers bootstrap or recovery authority. Bootstrap and recovery authority remains OS root acting host-locally through K9, subject to the recovery gate.
R15b
PD19-15 does not prohibit provisioning, rotation, replacement, or temporary handling of operational secrets that are otherwise authorized by the architecture, including Security System credentials or K2 operational signing material, provided those secrets do not themselves confer bootstrap or recovery authority.
R15c
PD19-15 does not determine whether a backup-encryption or restore key is a “recovery secret.” Its custody and authority properties must be established by the applicable §22/OD19-02 design.
R15d
PD19-15 does not define the scope or operations of K9. Bootstrap and recovery authority remains host-local and K9's exact authority remains subject to the recovery gate.
R15e
Root provisioning of operational credentials is not, by itself, a bootstrap or recovery-secret mechanism. Such provisioning remains subject to the applicable architecture and PD19-16.
Also carry forward:

* A-07 remains authoritative for first-admin bootstrap.
* T-29 remains authoritative for host-local recovery.
* No web bootstrap or alternate recovery authority is created.
* No backup-key custody decision is made.
* No §22 recovery mechanism is designed here.
* “Recovery secret” is defined by the authority it confers, not merely by whether it is used during recovery.
```

> **Transcription note:** Process-wrapper lines ("No files changed", "No commit/push", "No decision-log update",
> "Proceed to …") are omitted (DEC-030 Q3). The text is otherwise verbatim.

---

## DEC-046 — PD19-16 — Credential-handle lifecycle

- **Status:** CURRENT (revised)
- **Source:** §19 owner disposition review; owner message for PD19-16 (2026-09-23).
- **Related:** §19.7, §19.11.2, §19.12, §19.14, §19.15, §19.16

```text
PD19-16 — Owner disposition
REVISE
This is a substantial architectural decision, not merely a lifecycle description. The proposed state model is useful, but several terms currently imply mechanics or behaviors that have not actually been established. In particular, ORPHANED, ROTATING, “reported,” “committed,” and stale-credential detection need tighter boundaries.
The most important correction is that the lifecycle should distinguish authoritative persisted credential state from derived state. `DECLARED` and `UNPROVISIONED` are not equivalent persisted states.
R16a — State model and derived states
Carry forward the state model, but explicitly distinguish declaration-derived conditions:
The credential-handle lifecycle consists of the following architectural states or conditions: DECLARED, UNPROVISIONED, PROVISIONED, ROTATING, REVOKED, DESTROYING, DESTROYED, and ORPHANED. `DECLARED` is established by the presence of a valid loaded K11 Execution Declaration; `UNPROVISIONED` is established when a declared handle has no provisioned credential material. These conditions need not have independent persisted records. The authoritative representation and transition mechanics remain subject to §22.
This avoids creating a false requirement that every state must be a database row.
R16b — Resolvability
Keep the refusal rule explicit:
A credential handle resolves for credential use only while its authoritative lifecycle state is PROVISIONED or ROTATING and all applicable §16 resolution conditions are satisfied. Handles in DECLARED/UNPROVISIONED, REVOKED, DESTROYING, DESTROYED, or ORPHANED conditions MUST NOT resolve for credential use. An unavailable or invalid handle MUST produce `CREDENTIAL_UNAVAILABLE` through the applicable §16 refusal path.
This preserves the locked §16 behavior without pretending PD19-16 owns the refusal mechanism.
R16c — Root authority in v1
Accept the v1 policy, but keep mechanics out:
In v1, credential provisioning, rotation, revocation, and destruction are Local Root Operator acts performed through the authorized host-local lifecycle mechanism. They are not K6 request operations and no request field may carry credential material into K6. The mechanics, authentication of the Local Root Operator, and exact K9 operations remain subject to §22.
I would explicitly include revocation here because the candidate already treats it as a lifecycle transition and otherwise the authority statement is incomplete.
This does not mean K6 is prohibited from mechanically using or refusing a credential after K4 authorization; it means credential lifecycle administration is not exposed as an ordinary K6 Operation.
R16d — Rotation safety
The important invariant can be locked without defining the commit mechanics:
During rotation, the last committed credential version MUST remain the version resolvable for credential use until the new version has been authoritatively committed. An interrupted or failed rotation MUST NOT leave the handle without a previously committed usable version unless the credential has independently been revoked or otherwise made unavailable by an authoritative lifecycle transition. The mechanics of testing, committing, and retiring credential versions remain subject to §22.
This resolves the current ambiguity around “committed” without deciding how root and K6 interact during rotation.
R16e — Revocation and destruction
We should not invent a retention period for revoked credentials.
Revocation makes the credential handle unusable for credential resolution but does not, by itself, establish an immediate destruction requirement. Credential material associated with a revoked handle MUST remain subject to the applicable destruction lifecycle and MUST NOT remain usable through that handle. Destruction, retention bounds, and any required transition through DESTROYING remain subject to PD19-12, PD19-16, and §22.
This deliberately leaves the “why/how long” question open rather than creating an arbitrary retention rule.
R16f — Orphaned credentials
This needs a particularly careful rule because of the upgrade/rollback concern:
Credential material whose handle is no longer referenced by any currently loaded K11 Execution Declaration is ORPHANED and MUST NOT resolve for credential use. An ORPHANED credential MUST NOT be automatically destroyed solely because its declaration is absent. Destruction of orphaned material requires an explicit authorized Local Root Operator lifecycle action. Whether a later declaration using the same `handle_id` may re-adopt existing orphaned material, or instead requires fresh provisioning, remains a §22 lifecycle decision.
This preserves the candidate's rollback concern without silently deciding reactivation semantics.
R16g — Stale credential handling
The candidate should not establish that K6 itself determines that a credential is stale.
PD19-16 does not establish a general mechanism by which K6 interprets an endpoint or tool response as evidence that a credential is stale. K6 MAY record the mechanical outcome of a credential-dependent Operation as permitted by §16/K8. Any semantic determination that a credential is stale, expired, rejected, or otherwise requires rotation MUST be made by the component and contract authorized to make that determination. PD19-16 does not authorize automatic rotation.
That keeps K6 within its locked mechanical-enforcement role and avoids creating a hidden semantic authority.
R16h — Reporting
Remove the unqualified word “reported.”
PD19-16 does not establish a reporting channel for orphaned credentials or stale-credential conditions. Any reporting, surfacing, or operator notification mechanism remains subject to the applicable §21, §22, capability, or integration design.
This directly addresses F19-07 rather than pretending K4 can currently inspect SD-K6P.
R16i — Product-side revocation
Preserve the important boundary:
Revocation or destruction of an SCC credential handle does not, by itself, revoke or destroy the corresponding credential at the external Security System or endpoint. External credential revocation or destruction occurs only where an applicable declared Operation or other authorized Integration mechanism exists. PD19-16 does not create such an Operation.
This should be documented as a known lifecycle boundary/residual condition, not treated as an implementation defect.
R16j — SCC-generated credentials
Keep F19-08 unresolved:
PD19-16 does not establish an SCC-generated or Integration-generated credential provisioning path. Credential material generated by SCC or an Integration MUST NOT enter the K6 credential lifecycle unless an applicable higher-authority architecture establishes an authorized provisioning path consistent with §16.9 and the credential-custody rules.
That prevents PD19-16 from accidentally solving F19-08 by implication.
Important consequence: K11 declaration churn
I would make this explicit in the working review:
The lifecycle definition must not imply that removal of a K11 declaration automatically destroys its credential material.
The proposed ORPHANED state is useful precisely because K11 is release-controlled while K6 credential material has a different lifecycle. But whether a later declaration with the same `handle_id` can reclaim an orphan is a real §22 decision, not something we should settle now.
Owner decision
PD19-16 — REVISE
Carry forward:
R16a
The credential-handle lifecycle consists of the following architectural states or conditions: DECLARED, UNPROVISIONED, PROVISIONED, ROTATING, REVOKED, DESTROYING, DESTROYED, and ORPHANED. `DECLARED` is established by the presence of a valid loaded K11 Execution Declaration; `UNPROVISIONED` is established when a declared handle has no provisioned credential material. These conditions need not have independent persisted records. The authoritative representation and transition mechanics remain subject to §22.
R16b
A credential handle resolves for credential use only while its authoritative lifecycle state is PROVISIONED or ROTATING and all applicable §16 resolution conditions are satisfied. Handles in DECLARED/UNPROVISIONED, REVOKED, DESTROYING, DESTROYED, or ORPHANED conditions MUST NOT resolve for credential use. An unavailable or invalid handle MUST produce `CREDENTIAL_UNAVAILABLE` through the applicable §16 refusal path.
R16c
In v1, credential provisioning, rotation, revocation, and destruction are Local Root Operator acts performed through the authorized host-local lifecycle mechanism. They are not K6 request operations and no request field may carry credential material into K6. The mechanics, authentication of the Local Root Operator, and exact K9 operations remain subject to §22.
R16d
During rotation, the last committed credential version MUST remain the version resolvable for credential use until the new version has been authoritatively committed. An interrupted or failed rotation MUST NOT leave the handle without a previously committed usable version unless the credential has independently been revoked or otherwise made unavailable by an authoritative lifecycle transition. The mechanics of testing, committing, and retiring credential versions remain subject to §22.
R16e
Revocation makes the credential handle unusable for credential resolution but does not, by itself, establish an immediate destruction requirement. Credential material associated with a revoked handle MUST remain subject to the applicable destruction lifecycle and MUST NOT remain usable through that handle. Destruction, retention bounds, and any required transition through DESTROYING remain subject to PD19-12, PD19-16, and §22.
R16f
Credential material whose handle is no longer referenced by any currently loaded K11 Execution Declaration is ORPHANED and MUST NOT resolve for credential use. An ORPHANED credential MUST NOT be automatically destroyed solely because its declaration is absent. Destruction of orphaned material requires an explicit authorized Local Root Operator lifecycle action. Whether a later declaration using the same `handle_id` may re-adopt existing orphaned material, or instead requires fresh provisioning, remains a §22 lifecycle decision.
R16g
PD19-16 does not establish a general mechanism by which K6 interprets an endpoint or tool response as evidence that a credential is stale. K6 MAY record the mechanical outcome of a credential-dependent Operation as permitted by §16/K8. Any semantic determination that a credential is stale, expired, rejected, or otherwise requires rotation MUST be made by the component and contract authorized to make that determination. PD19-16 does not authorize automatic rotation.
R16h
PD19-16 does not establish a reporting channel for orphaned credentials or stale-credential conditions. Any reporting, surfacing, or operator notification mechanism remains subject to the applicable §21, §22, capability, or integration design.
R16i
Revocation or destruction of an SCC credential handle does not, by itself, revoke or destroy the corresponding credential at the external Security System or endpoint. External credential revocation or destruction occurs only where an applicable declared Operation or other authorized Integration mechanism exists. PD19-16 does not create such an Operation.
R16j
PD19-16 does not establish an SCC-generated or Integration-generated credential provisioning path. Credential material generated by SCC or an Integration MUST NOT enter the K6 credential lifecycle unless an applicable higher-authority architecture establishes an authorized provisioning path consistent with §16.9 and the credential-custody rules.
Review notes to carry forward

* `DECLARED` and `UNPROVISIONED` are lifecycle conditions, not necessarily persisted records.
* `ROTATING` has a safety invariant, but its mechanics remain §22.
* No automatic credential rotation.
* No implicit K6 semantic interpretation of endpoint/tool failures.
* No undefined “reported” channel.
* ORPHANED material is unusable and not automatically destroyed.
* Re-adoption of an orphan after a K11 rollback/re-release remains open.
* Revocation does not imply external product-side credential revocation.
* No new credential-generation/provisioning path is created.
* OD19-02 remains open for at-rest protection.
* R12A-4 remains authoritative for destruction completion: destruction cannot be reported complete while the handle remains resolvable.
```

> **Transcription note:** Process-wrapper lines ("No files changed", "No commit/push", "No decision-log update",
> "Proceed to …") are omitted (DEC-030 Q3). The text is otherwise verbatim.

---

## DEC-047 — PD19-17 — Backup/restore implications

- **Status:** CURRENT (revised)
- **Source:** §19 owner disposition review; owner message for PD19-17 (2026-09-23).
- **Related:** §19.15, §19.16, §19.17, §19.20 (S19-11)

```text
PD19-17 — Owner disposition
REVISE
The prior review stands. The candidate still needs to be tightened around the distinction between restoring storage and restoring authoritative security state.
The critical point is that a K7 restore can resurrect authorization state that was subsequently revoked. Merely invalidating non-terminal Decisions does not prevent new authorization decisions from being made against that stale restored state. So the recovery invariant must be stronger, while the actual reconciliation mechanism remains §22.
R17a — Backup scope
SCC-controlled backups MUST be scoped to their authoritative storage domain. A backup of SD-K7 MUST NOT include SD-K6P material. PD19-17 does not authorize backup, export, or retention of SD-K6P credential material outside K6; any such operation remains subject to R10b/R10c and the later §22/OD19-02 custody decision.
R17b — Restore authority
Restoration of SCC authoritative state is a Local Root Operator act through the authorized host-local recovery mechanism. Restore MUST NOT be reachable through K3 or any web-facing SCC path, and MUST NOT bypass applicable authorization, audit, or recovery controls.
R17c — K7 restore enters recovery/reconciliation
Restoring SD-K7 from an earlier backup point MUST place SCC into a recovery/reconciliation condition before ordinary authorization-dependent work may resume. The restored K7 state MUST be treated as potentially stale with respect to events occurring after the backup point. The exact recovery state and transition mechanics remain subject to §22.
R17d — Non-terminal Decisions
Do not establish a new §17 trigger for `INVALIDATED` here.
Non-terminal Decisions existing at the restored backup point MUST NOT resume execution solely because they are present in the restored K7 state. They MUST be reconciled or otherwise dispositioned by the recovery procedure before further execution. PD19-17 does not establish a new §17 Decision-status transition or expand the existing semantics of `INVALIDATED`.
R17e — Jobs
Jobs that are non-terminal at the restored backup point MUST be held from further execution until their authorization and execution state have been reconciled against the surviving authoritative evidence, including K8 where applicable. Restore MUST NOT cause an uncertain or previously in-flight Job to be silently re-executed.
R17f — Post-backup authorization changes
This is the major correction to the candidate's “disclose the residual risk” approach:
A K7 restore MUST treat authorization changes occurring after the backup point—including Principal revocations, Role Membership revocations, Grant revocations, and applicable policy or authorization-state changes—as potentially absent from restored K7. SCC MUST NOT represent restored authorization state as current merely because it was present in the backup. The recovery procedure MUST establish the disposition of post-backup authorization changes before ordinary authorization-dependent operation resumes. The mechanism for obtaining and reconciling those changes remains subject to §22 and applicable off-host evidence.
This means disclosure can be part of the recovery record, but disclosure alone is not sufficient to permit normal authorization to resume.
R17g — Audit continuity
A K7 restore MAY remove authoritative audit records created after the backup point while K8 may retain journal records from that period. Recovery MUST NOT silently treat such surviving K8 references as nonexistent merely because their referenced K7 records were lost. The consistency, reconciliation, and retention relationship between K7 audit records and K8 journal records remains subject to §21, §22, and the applicable §16/K8 rules.
R17h — K8 restore
Restoring an older SD-K8 state MUST NOT silently replace a newer K8 journal state. Any operation that intentionally replaces, reinitializes, or discards K8 state MUST be explicitly recognized as a K8 recovery/reinitialization event and governed by the applicable §16 and §22 recovery rules.
R17i — Session state
A K7 restore MUST NOT assume that restored SCC session validation state remains valid merely because it is present in the backup. Session validity and invalidation after restore remain subject to P2 and §22.
R17j — Principal-ID non-reuse
A K7 restore MUST NOT be treated as preserving the §17 Principal-ID non-reuse invariant by virtue of the restored K7 state alone. The recovery mechanism MUST preserve the applicable principal non-reuse invariant, consistent with R8c and §17.1.4. The mechanism remains subject to §22.
R17k — Host/external state
Restoring SD-K7 does not restore or roll back host state, Platform Services state, or other external state. State represented in restored K7 that depends on observations of such external state MUST be treated as potentially stale and reconciled according to the applicable architecture. PD19-17 does not design §20 reconciliation.
R17l — Partial/mixed-domain restore
Recovery MUST NOT assume that independently restored storage domains form a mutually consistent SCC state merely because each restored domain is individually valid. Mixed-version or partial restoration of K7, K8, K11H, or other authoritative domains MUST be explicitly detected or dispositioned by the applicable recovery design before dependent operations resume.
Important review notes

* Do not accept the candidate's blanket `non-terminal Decision → INVALIDATED` rule. That would establish a new §17 semantic trigger.
* Do not accept “disclose lost revocations” as the complete safety response. Restored authorization state itself must be reconciled before authorization-dependent operation resumes.
* K7 restoration does not restore the complete SCC security state.
* K8 may contain surviving evidence whose K7 references have disappeared; that discrepancy must not be silently discarded.
* P2 remains authoritative for session semantics.
* R8c remains authoritative regarding Principal-ID non-reuse.
* Host state and external Security System state are not rolled back by K7 restore.
* Mixed/partial domain restoration must be addressed explicitly by §22.
* Backup frequency, storage location, retention mechanics, and procedures remain deferred.
* SD-K6P backup remains unresolved and unauthorized by PD19-10.
```

> **Transcription note:** Process-wrapper lines ("No files changed", "No commit/push", "No decision-log update",
> "Proceed to …") are omitted (DEC-030 Q3). The text is otherwise verbatim.

---

## DEC-048 — PD19-18 — K8 loss or reinitialization

- **Status:** CURRENT (revised)
- **Source:** §19 owner disposition review; owner message for PD19-18 (2026-09-23).
- **Related:** §19.12, §19.15, §19.16, §19.21.2, §19.22

```text
PD19-18 — Owner disposition
REVISE
This needs to be treated as a K8-lifetime/recovery boundary, not merely a timestamp rule.
The candidate's `issued_at` cutoff is useful, but by itself it does not restore replay, nonce, idempotency, or UNKNOWN/PARTIAL safety. More importantly, we should not allow K8 disappearance to become an implicit reset mechanism.
I would not lock the proposed approval blackout yet. OD19-03 is still unresolved, and the current approval evidence does not contain an issuance timestamp that K6 could independently compare against a reinitialization time.
R18a — K8 lifetime / no implicit reset
K8 loss, removal, replacement, or reinitialization MUST NOT be treated as an implicit reset of replay, nonce, idempotency, approval, or execution-history protections. A new K8 lifetime MUST be explicitly recognized by the authorized recovery/reinitialization mechanism before K6 may resume normal request acceptance. The absence of K8 alone MUST NOT authorize creation of a fresh K8 lifetime.
This directly addresses the first problem.
A missing K8 should not mean “new installation.”
R18b — Recovery/reinitialization authority
K8 reinitialization is a Local Root Operator recovery/reinitialization act subject to §22. K6 MUST NOT autonomously declare K8 reinitialized merely because its journal is absent, empty, truncated, or otherwise unavailable.
This is important because otherwise deleting K8 could become a replay-reset primitive.
R18c — New K8 lifetime identity
We need a lifetime identity rather than relying solely on `journal_seq`.
Each K8 lifetime MUST have an identity distinct from the journal sequence values within that lifetime. A `journal_seq` value MUST NOT by itself identify a journal record across K8 lifetimes. Cross-lifetime references MUST identify the applicable K8 lifetime as well as the journal position, or use an equivalent mechanism that prevents ambiguity.
This resolves the collision problem identified in item 7.
It also strengthens R11d/R17g: a K7 audit record referring to an old K8 record cannot accidentally resolve to a new record having the same sequence number.
R18d — Acceptance after K8 loss
I would not yet accept the candidate's exact `issued_at` rule as a permanent §19 rule, because it may require a §16 amendment and depends on how the new K8 lifetime is represented.
Instead:
Following an authorized K8 reinitialization, K6 MUST NOT accept a request in a manner that could rely upon replay, nonce-use, idempotency, approval, or execution-history evidence from a prior K8 lifetime unless the applicable recovery design explicitly establishes that evidence as valid and available. The exact K6 acceptance/refusal conditions and any required §16 amendment remain subject to the §22 recovery design and applicable §16 gate.
This establishes the safety property without prematurely modifying §16.
R18e — Idempotency
This needs its own explicit protection:
A K8 lifetime change MUST NOT cause an idempotency key previously associated with a SUCCESS outcome in an earlier K8 lifetime to become automatically eligible for re-execution. Recovery MUST establish the disposition of affected idempotency keys before an operation relying on their prior history may be accepted. The retention and key-reuse semantics remain subject to R11a and the applicable §16/§22 design.
This directly addresses the candidate's biggest omission: a fresh `request_id` plus an old idempotency key could otherwise execute an operation again.
R18f — UNKNOWN / PARTIAL outcomes
A K8 lifetime change MUST NOT cause an UNKNOWN or PARTIAL outcome from a prior K8 lifetime to become silently re-executable merely because its terminal reconciliation evidence is no longer present. Affected Jobs and idempotency keys MUST remain held or otherwise dispositioned until the applicable recovery/reconciliation procedure establishes a safe disposition. The exact reconciliation mechanism remains subject to §22 and the applicable §16 rules.
This prevents the loss of K8 from turning UNKNOWN/PARTIAL into an accidental permission to retry.
R18g — Approval evidence
Do not lock the proposed blanket blackout yet.
PD19-18 does not establish a post-reinitialization approval-evidence blackout period. Approval evidence after K8 loss or reinitialization remains subject to §17, the applicable approval-evidence rules, OD19-03, and the §22 recovery design. Any rule requiring elapsed time after reinitialization MUST have an authoritative horizon and an enforceable basis in the applicable architecture.
This is the cleanest way to handle F19-06/OD19-03.
R18h — Approval evidence cannot be classified by an unavailable timestamp
PD19-18 does not assume that K6 can determine when approval evidence was created unless that information is actually represented in the authoritative approval evidence and validation contract. A reinitialization rule MUST NOT rely on an approval-issuance timestamp that the locked approval model does not provide.
This is important. We should not manufacture a timestamp semantics that §17 doesn't contain.
R18i — K8 reinitialization time
The new K8 needs durable knowledge of its own lifetime boundary.
An authorized K8 reinitialization MUST establish durable evidence of the new K8 lifetime and its creation/reinitialization boundary before K6 resumes request acceptance under that lifetime. The exact representation and recovery behavior remain subject to §22 and §21.
That avoids saying “store the timestamp in this exact table/record” prematurely.
R18j — Older K8 restore
An older K8 isn't the same as a blank K8, but it is still a new lifetime for purposes of post-backup history.
Restoring an older K8 copy creates a new current K8 lifetime; the restored records retain only the history contained in that copy. The restored journal MUST NOT be treated as containing the records or replay/idempotency state that existed after its backup point. Recovery MUST establish which surviving records are authoritative for the new lifetime before dependent requests resume.
This is consistent with R17h.
R18k — Clock dependency
Do not create a clock-integrity architecture here, but explicitly don't hide the dependency:
Any K8-reinitialization rule based on elapsed time MUST use the authoritative time source and clock-integrity assumptions established by the applicable architecture. PD19-18 does not establish a new clock-trust model.
R18l — Tampering/truncation
PD19-18 does not establish whether an unexpected K8 truncation, deletion, or tampering event can be distinguished from ordinary K8 loss. Such detection and tamper-evidence requirements remain subject to §16.15, §18, §19, and the applicable later gate. An intentionally or unexpectedly damaged K8 MUST NOT be treated as a benign replay-history reset merely because the resulting store is readable.
That keeps the §18/§19 tamper-evidence question open.
Owner decision
PD19-18 — REVISE
Carry forward:
R18a
K8 loss, removal, replacement, or reinitialization MUST NOT be treated as an implicit reset of replay, nonce, idempotency, approval, or execution-history protections. A new K8 lifetime MUST be explicitly recognized by the authorized recovery/reinitialization mechanism before K6 may resume normal request acceptance. The absence of K8 alone MUST NOT authorize creation of a fresh K8 lifetime.
R18b
K8 reinitialization is a Local Root Operator recovery/reinitialization act subject to §22. K6 MUST NOT autonomously declare K8 reinitialized merely because its journal is absent, empty, truncated, or otherwise unavailable.
R18c
Each K8 lifetime MUST have an identity distinct from the journal sequence values within that lifetime. A `journal_seq` value MUST NOT by itself identify a journal record across K8 lifetimes. Cross-lifetime references MUST identify the applicable K8 lifetime as well as the journal position, or use an equivalent mechanism that prevents ambiguity.
R18d
Following an authorized K8 reinitialization, K6 MUST NOT accept a request in a manner that could rely upon replay, nonce-use, idempotency, approval, or execution-history evidence from a prior K8 lifetime unless the applicable recovery design explicitly establishes that evidence as valid and available. The exact K6 acceptance/refusal conditions and any required §16 amendment remain subject to the §22 recovery design and applicable §16 gate.
R18e
A K8 lifetime change MUST NOT cause an idempotency key previously associated with a SUCCESS outcome in an earlier K8 lifetime to become automatically eligible for re-execution. Recovery MUST establish the disposition of affected idempotency keys before an operation relying on their prior history may be accepted. The retention and key-reuse semantics remain subject to R11a and the applicable §16/§22 design.
R18f
A K8 lifetime change MUST NOT cause an UNKNOWN or PARTIAL outcome from a prior K8 lifetime to become silently re-executable merely because its terminal reconciliation evidence is no longer present. Affected Jobs and idempotency keys MUST remain held or otherwise dispositioned until the applicable recovery/reconciliation procedure establishes a safe disposition. The exact reconciliation mechanism remains subject to §22 and the applicable §16 rules.
R18g
PD19-18 does not establish a post-reinitialization approval-evidence blackout period. Approval evidence after K8 loss or reinitialization remains subject to §17, the applicable approval-evidence rules, OD19-03, and the §22 recovery design. Any rule requiring elapsed time after reinitialization MUST have an authoritative horizon and an enforceable basis in the applicable architecture.
R18h
PD19-18 does not assume that K6 can determine when approval evidence was created unless that information is actually represented in the authoritative approval evidence and validation contract. A reinitialization rule MUST NOT rely on an approval-issuance timestamp that the locked approval model does not provide.
R18i
An authorized K8 reinitialization MUST establish durable evidence of the new K8 lifetime and its creation/reinitialization boundary before K6 resumes request acceptance under that lifetime. The exact representation and recovery behavior remain subject to §22 and §21.
R18j
Restoring an older K8 copy creates a new current K8 lifetime; the restored records retain only the history contained in that copy. The restored journal MUST NOT be treated as containing the records or replay/idempotency state that existed after its backup point. Recovery MUST establish which surviving records are authoritative for the new lifetime before dependent requests resume.
R18k
Any K8-reinitialization rule based on elapsed time MUST use the authoritative time source and clock-integrity assumptions established by the applicable architecture. PD19-18 does not establish a new clock-trust model.
R18l
PD19-18 does not establish whether an unexpected K8 truncation, deletion, or tampering event can be distinguished from ordinary K8 loss. Such detection and tamper-evidence requirements remain subject to §16.15, §18, §19, and the applicable later gate. An intentionally or unexpectedly damaged K8 MUST NOT be treated as a benign replay-history reset merely because the resulting store is readable.
Review notes

* Reject the candidate's simple `issued_at > reinitialization time` rule for now; it may require a §16 amendment and does not solve idempotency or UNKNOWN/PARTIAL safety.
* Reject the blanket approval blackout until OD19-03 and the approval-evidence model establish an enforceable basis.
* K8 disappearance cannot become an implicit replay-reset mechanism.
* K8 lifetime identity must be distinct from `journal_seq`.
* An older K8 restore is a new current lifetime, not a continuation of the old one.
* Loss of K8 history does not authorize re-execution.
* UNKNOWN/PARTIAL outcomes require explicit recovery disposition.
* K8 reinitialization must be explicitly authorized and durably identified before normal acceptance resumes.
* Tamper/truncation detection remains open.
* Clock-trust semantics remain open.
```

> **Transcription note:** Process-wrapper lines ("No files changed", "No commit/push", "No decision-log update",
> "Proceed to …") are omitted (DEC-030 Q3). The text is otherwise verbatim.

---

## DEC-049 — PD19-19 — Format versioning, migration and downgrade

- **Status:** CURRENT (revised)
- **Source:** §19 owner disposition review; owner message for PD19-19 (2026-09-23).
- **Related:** §19.15, §19.16, §19.18, §19.20 (S19-15), §19.21.2

```text
PD19-19 — Owner disposition
REVISE
The candidate has several good invariants, but it currently overreaches into §16 behavior, §22 lifecycle policy, and K11H/K11R upgrade semantics. We should lock the format-versioning principle without prematurely deciding who migrates which store, how downgrade works, or whether a particular domain is migration-compatible.
The most important distinction is:
A stored format version identifies how content is represented; it does not by itself establish the migration mechanism, compatibility window, or lifecycle policy.
R19a — Versioned authoritative formats
Authoritative persistent content in SD-K7 and SD-K8 MUST carry sufficient format-version information to determine whether the currently executing SCC component can safely interpret that content. The format-version mechanism MUST NOT rely solely on an implicit software-release version.
This accepts the genuinely new architectural requirement without dictating a schema.
R19b — Unknown or unsupported formats
The candidate's fail-closed intent is appropriate, but the exact component behavior should stay within the relevant gate:
SCC MUST NOT interpret authoritative persistent content whose format is unrecognised or unsupported by the executing component. The affected component MUST fail closed with respect to operations that depend upon that content. The exact refusal behavior and any required §16 amendment for K6 remain subject to the applicable implementation/recovery gate.
This avoids silently amending §16 with a new refusal condition here.
R19c — Partial migrations
Distinguish a known format from an incomplete migration:
SCC MUST NOT operate on authoritative persistent content known or determined to be in a partially migrated or otherwise indeterminate format state. Migration MUST NOT be reported as successful unless the applicable postconditions establishing the target format have been satisfied.
This works with the baseline requirement that migration failure cannot be reported as success, without claiming that a version field alone detects interrupted migration.
R19d — Deterministic/versioned migrations
Carry forward the baseline rather than restating only part of it:
Migrations of authoritative SCC persistent content MUST be versioned and deterministic, and MUST preserve the applicable baseline requirements for recoverability where practical, idempotence where practical, preservation of configuration unless explicitly migrated, and accounting for active Jobs before upgrades.
This keeps those foundational requirements authoritative rather than accidentally creating a shorter §19 substitute.
R19e — Append-only records
We need to prevent a migration from silently turning append-only history into mutable history:
A format migration MUST NOT edit an append-only record in place in a manner that violates R12A-2. Migration of append-only K7 audit records or K8 journal records MUST preserve their applicable append-only semantics. The exact representation of migrated or multi-version records remains subject to §21/§22 and the applicable storage design.
This intentionally does not decide whether migration means rewriting, versioned coexistence, translation-on-read, or another mechanism.
R19f — K8 forward interpretability
I would narrow the candidate's “later K6 versions” promise. It is too broad as an architectural guarantee.
K8 records required by the retention and recovery rules MUST remain interpretable by the K6 versions that are authorized to consume them for their retained lifetime, or an explicitly authorized migration/compatibility mechanism MUST preserve their required semantics. PD19-19 does not require indefinite backward compatibility across arbitrary future K6 versions.
That is much more defensible and ties compatibility to the actual retention obligation.
R19g — K7 audit history
Likewise, preserve the existing baseline without promising a particular migration mechanism:
Format migration or upgrade MUST preserve required K7 audit history and its required historical resolvability. PD19-19 does not select the representation or migration mechanism by which that preservation is achieved.
This works with R9/R17 without redefining §21.
R19h — Downgrade
Do not accept the candidate's “downgrade is restore-only” rule as a §19 decision.
The correct carry-forward is:
PD19-19 does not establish a general downgrade policy. Downgrade, including any downgrade performed by restoring prior authoritative state, remains governed by CHANGE-025, TQ-06, §22, and the applicable recovery rules. Any downgrade mechanism MUST satisfy the applicable PD19-17 and PD19-18 consequences when it restores or replaces K7/K8 state.
This preserves the important consequence without stealing CHANGE-025 from §22.
R19i — K7/K8 downgrade interaction
Because the candidate correctly spotted the K7/K8 asymmetry:
A downgrade or rollback MUST account for the compatibility and lifetime state of both SD-K7 and SD-K8. Restoring or replacing one domain MUST NOT be treated as sufficient merely because the other domain remains readable. Any resulting mixed-version or mixed-lifetime condition MUST be explicitly detected or dispositioned under the applicable recovery design.
This directly incorporates R17l and R18j.
R19j — K11R/K11H
The candidate should not lock the proposed “K11H survives unless root changes it” wording.
PD19-19 does not establish the upgrade or migration semantics of SD-K11R or SD-K11H. K11R release content remains governed by its release/installation lifecycle; K11H remains subject to its authoritative configuration and migration rules. Any upgrade that changes K11H content or format MUST preserve the applicable baseline configuration-preservation requirements unless an explicit migration is authorized. Detailed K11R/K11H upgrade, rollback, and migration behavior remains subject to §22 and the applicable §18 decisions.
This fixes the conflict with the baseline without inventing a K11H migration mechanism.
R19k — Other storage domains
Don't silently imply that SD-K6P or SD-K2 have no format-version requirements.
PD19-19's explicit K7/K8 format-version requirement does not establish format, migration, or compatibility rules for SD-K6P, SD-K11H, SD-K11R, SD-K2, or other storage domains. Their applicable format and lifecycle requirements remain governed by their respective architecture and later gates.
This prevents §19 from accidentally becoming incomplete normative authority for domains it hasn't designed.
R19l — Migration authority/mechanics
Leave the actor question to §22:
PD19-19 does not establish which SCC component or host-local mechanism performs K7, K8, K11H, or other domain migrations. Migration authority, sequencing, authorization, interruption handling, and recovery mechanics remain subject to §22 and the applicable component architecture.
This is particularly important because C cannot acquire authority merely because it performs migration.
R19m — Upgrade consequences already locked elsewhere
We should not duplicate the detailed K11 declaration/approval behavior:
PD19-19 does not alter the locked upgrade-sensitive validation rules of §16 or §17. Changes to K11 declarations, declaration digests, Operation major versions, Plans, Decisions, or approval evidence continue to have the effects already established by those sections.
That means the existing `STALE_DECLARATION` and `op_id@major` binding behavior remains authoritative without us creating another upgrade model.
Owner decision
PD19-19 — REVISE
Carry forward:
R19a
Authoritative persistent content in SD-K7 and SD-K8 MUST carry sufficient format-version information to determine whether the currently executing SCC component can safely interpret that content. The format-version mechanism MUST NOT rely solely on an implicit software-release version.
R19b
SCC MUST NOT interpret authoritative persistent content whose format is unrecognised or unsupported by the executing component. The affected component MUST fail closed with respect to operations that depend upon that content. The exact refusal behavior and any required §16 amendment for K6 remain subject to the applicable implementation/recovery gate.
R19c
SCC MUST NOT operate on authoritative persistent content known or determined to be in a partially migrated or otherwise indeterminate format state. Migration MUST NOT be reported as successful unless the applicable postconditions establishing the target format have been satisfied.
R19d
Migrations of authoritative SCC persistent content MUST be versioned and deterministic, and MUST preserve the applicable baseline requirements for recoverability where practical, idempotence where practical, preservation of configuration unless explicitly migrated, and accounting for active Jobs before upgrades.
R19e
A format migration MUST NOT edit an append-only record in place in a manner that violates R12A-2. Migration of append-only K7 audit records or K8 journal records MUST preserve their applicable append-only semantics. The exact representation of migrated or multi-version records remains subject to §21/§22 and the applicable storage design.
R19f
K8 records required by the retention and recovery rules MUST remain interpretable by the K6 versions that are authorized to consume them for their retained lifetime, or an explicitly authorized migration/compatibility mechanism MUST preserve their required semantics. PD19-19 does not require indefinite backward compatibility across arbitrary future K6 versions.
R19g
Format migration or upgrade MUST preserve required K7 audit history and its required historical resolvability. PD19-19 does not select the representation or migration mechanism by which that preservation is achieved.
R19h
PD19-19 does not establish a general downgrade policy. Downgrade, including any downgrade performed by restoring prior authoritative state, remains governed by CHANGE-025, TQ-06, §22, and the applicable recovery rules. Any downgrade mechanism MUST satisfy the applicable PD19-17 and PD19-18 consequences when it restores or replaces K7/K8 state.
R19i
A downgrade or rollback MUST account for the compatibility and lifetime state of both SD-K7 and SD-K8. Restoring or replacing one domain MUST NOT be treated as sufficient merely because the other domain remains readable. Any resulting mixed-version or mixed-lifetime condition MUST be explicitly detected or dispositioned under the applicable recovery design.
R19j
PD19-19 does not establish the upgrade or migration semantics of SD-K11R or SD-K11H. K11R release content remains governed by its release/installation lifecycle; K11H remains subject to its authoritative configuration and migration rules. Any upgrade that changes K11H content or format MUST preserve the applicable baseline configuration-preservation requirements unless an explicit migration is authorized. Detailed K11R/K11H upgrade, rollback, and migration behavior remains subject to §22 and the applicable §18 decisions.
R19k
PD19-19's explicit K7/K8 format-version requirement does not establish format, migration, or compatibility rules for SD-K6P, SD-K11H, SD-K11R, SD-K2, or other storage domains. Their applicable format and lifecycle requirements remain governed by their respective architecture and later gates.
R19l
PD19-19 does not establish which SCC component or host-local mechanism performs K7, K8, K11H, or other domain migrations. Migration authority, sequencing, authorization, interruption handling, and recovery mechanics remain subject to §22 and the applicable component architecture.
R19m
PD19-19 does not alter the locked upgrade-sensitive validation rules of §16 or §17. Changes to K11 declarations, declaration digests, Operation major versions, Plans, Decisions, or approval evidence continue to have the effects already established by those sections.
Review notes

* Accept the format-versioning principle for K7/K8.
* Fail closed on unknown/unsupported content, but don't silently amend §16 here.
* Keep partially migrated distinct from unknown version.
* Preserve the full baseline migration requirements; don't accidentally narrow §12 by omission.
* Don't promise indefinite K8 backward compatibility.
* Don't establish “restore-only” downgrade policy here; CHANGE-025/TQ-06/§22 own that decision.
* Downgrade must account for both K7 and K8, including K8 lifetime implications from R18.
* Don't lock the proposed K11H survival rule.
* Don't create format policies for SD-K6P/SD-K2/etc. by implication.
* Migration authority and mechanics remain open.
* Existing §16/§17 upgrade consequences remain authoritative and should not be duplicated or altered.
```

> **Transcription note:** Process-wrapper lines ("No files changed", "No commit/push", "No decision-log update",
> "Proceed to …") are omitted (DEC-030 Q3). The text is otherwise verbatim.

---

## DEC-050 — PD19-20 — §20 dependency finding

- **Status:** CURRENT (revised)
- **Source:** §19 owner disposition review; owner message for PD19-20 (2026-09-23).
- **Related:** §19.21.1 (Q19-03), §19.22

```text
PD19-20 — Owner disposition
REVISE
The first half is essentially a finding, not a new architectural decision. The second half — assigning future §20 data classes to SD-K7 — should not be accepted because §20 has deliberately not been designed.
The useful result here is to preserve the dependency finding while making its scope precise and keeping §20's eventual storage/domain decisions open.
R20a — Bounded dependency finding
The §19 design review has identified no demonstrated dependency on §20 for the currently defined identity-related architecture and persistence requirements. This finding applies only to the explicitly defined identity slice and does not establish that the minimum SCC Core, later capabilities, or other architecture are independent of §20. Any actual dependency discovered during later design supersedes this finding for the affected scope.
This avoids the undefined blanket term “identity slice” while preserving the actual finding.
I would not put “§20 adds data classes to SD-K7” into the normative §19 candidate.
R20b — No pre-allocation of §20 storage
PD19-20 does not assign a storage domain to §20 data classes. §20 MUST determine the authoritative owner and storage domain of each reconciliation, desired-state, and drift data class when §20 is designed, subject to PD19-01 and the higher-authority architecture.
This is the important correction.
It preserves R1/R2 without pre-deciding the answer.
R20c — Recovery reconciliation is not automatically §20 reconciliation
This distinction should be explicit because otherwise R17/R18 create an accidental dependency:
The reconciliation required by R17e, R17f, R17k, R18f, and §15.13 for recovery, execution safety, or disposition of uncertain state is not, by that requirement alone, §20 reconciliation. PD19-20 does not classify recovery/reconciliation mechanics as §20 functionality.
This prevents “reconciliation” from becoming an accidental dependency label.
R20d — K4 reconciliation in §17.13.2
Likewise, don't silently equate every K4 reconciliation mechanism with §20:
The §17.13.2 reference to K4 reconciliation under §20 remains authoritative for the reconciliation mechanism expressly assigned to §20. It does not reclassify K8 execution-state reconciliation, recovery reconciliation, or other mechanisms already assigned elsewhere in the architecture.
That preserves the locked §17 text without rewriting it.
R20e — Integration desired state
R7g already handles this correctly. Don't duplicate it or predefine the relationship.
Where Integration-specific configuration expresses desired Security System state, R7g remains authoritative for the §20 aspect of that state. PD19-20 does not determine whether such configuration and any future §20 desired-state representation are the same data class, separate data classes, or related records. PD19-01 governs each class once defined.
This is important because otherwise R7g + PD19-20 could accidentally create two competing “authoritative” homes.
R20f — Observed state vs drift
The candidate correctly noticed the DC-04 boundary problem. We should preserve the distinction without designing §20:
PD19-20 does not move DC-04 or redefine observed domain state. DC-04 remains the §19-defined observed-state data class. Whether §20 introduces separate drift records, derives drift from observed state and desired state, or uses another representation remains open to §20.
This keeps §19 from pre-solving §20.
R20g — No §20 implementation dependency from this finding
Given D-8/D-12, I would explicitly state:
PD19-20 does not require completion or implementation of §20 before the currently defined identity slice may proceed, except where a later architecture or capability demonstrates an actual §20 dependency.
This is consistent with the existing owner decisions rather than creating a new dependency rule.
Owner decision
PD19-20 — REVISE
Carry forward:
R20a
The §19 design review has identified no demonstrated dependency on §20 for the currently defined identity-related architecture and persistence requirements. This finding applies only to the explicitly defined identity slice and does not establish that the minimum SCC Core, later capabilities, or other architecture are independent of §20. Any actual dependency discovered during later design supersedes this finding for the affected scope.
R20b
PD19-20 does not assign a storage domain to §20 data classes. §20 MUST determine the authoritative owner and storage domain of each reconciliation, desired-state, and drift data class when §20 is designed, subject to PD19-01 and the higher-authority architecture.
R20c
The reconciliation required by R17e, R17f, R17k, R18f, and §15.13 for recovery, execution safety, or disposition of uncertain state is not, by that requirement alone, §20 reconciliation. PD19-20 does not classify recovery/reconciliation mechanics as §20 functionality.
R20d
The §17.13.2 reference to K4 reconciliation under §20 remains authoritative for the reconciliation mechanism expressly assigned to §20. It does not reclassify K8 execution-state reconciliation, recovery reconciliation, or other mechanisms already assigned elsewhere in the architecture.
R20e
Where Integration-specific configuration expresses desired Security System state, R7g remains authoritative for the §20 aspect of that state. PD19-20 does not determine whether such configuration and any future §20 desired-state representation are the same data class, separate data classes, or related records. PD19-01 governs each class once defined.
R20f
PD19-20 does not move DC-04 or redefine observed domain state. DC-04 remains the §19-defined observed-state data class. Whether §20 introduces separate drift records, derives drift from observed state and desired state, or uses another representation remains open to §20.
R20g
PD19-20 does not require completion or implementation of §20 before the currently defined identity slice may proceed, except where a later architecture or capability demonstrates an actual §20 dependency.
Review notes

* Preserve the “no demonstrated §20 dependency” finding, but keep its scope bounded.
* Do not assign future §20 data classes to SD-K7.
* §20 remains NOT DESIGNED.
* R7g remains authoritative for Integration configuration that expresses desired state.
* DC-04 remains a §19 observed-state class; don't prematurely turn it into a §20 drift record.
* “Reconciliation” in recovery/execution safety does not automatically mean §20 reconciliation.
* §17.13.2's explicit §20 reconciliation reference remains untouched.
* The identity slice remains free of a demonstrated §20 dependency; this does not certify the entire minimum Core or future capabilities as §20-independent.
```

> **Transcription note:** Process-wrapper lines ("No files changed", "No commit/push", "No decision-log update",
> "Proceed to …") are omitted (DEC-030 Q3). The text is otherwise verbatim.

---

## DEC-051 — OD19-01 — Assertion verification material

- **Status:** CURRENT (deferral — question OPEN)
- **Source:** §19 owner disposition review; owner message for OD19-01 (2026-09-23).
- **Related:** §19.5.3 (D19-04), §19.7 (DC-18), §19.9, §19.14, §19.21

```text
OD19-01 — Owner disposition
DEFER / KEEP OPEN
I would not choose (a) or (b) yet. The analysis correctly identifies that the placement decision crosses multiple gates, and there is a real architectural ambiguity in the locked §15.12 wording that should not be silently resolved from §19.
The important thing is to make the deferral precise enough that §19 itself remains internally valid under R1.
R01a — Keep DC-18 unresolved, but without two authoritative homes
The authoritative storage domain and owner of DC-18 (K2 identity-assertion verification material) remain OPEN pending OD19-01. Until resolved, §19 MUST NOT assign DC-18 to SD-K7, SD-K11H, or any other storage domain as its authoritative home. The eventual assignment MUST satisfy R1 and the applicable higher-authority constraints.
This fixes the immediate R1 problem.
The current `SD-K7 or SD-K11H` wording should therefore not survive as normative candidate text.
R01b — Named owning decision path
The candidate should not leave the eventual owner as the vague “P2 / §22.”
OD19-01 MUST be resolved through coordination of P2, §22/recovery, and the applicable CyberPanel K2 gate. P2 determines the assertion/verification semantics; §22 determines provisioning and recovery mechanics; the K2 gate determines platform-specific installation and presentation constraints. The authoritative storage-domain decision remains a §19 architecture decision constrained by those results.
This preserves the separation of responsibilities rather than pretending one gate owns everything.
R01c — Do not reinterpret §15.12
I would explicitly avoid deciding whether “only in K4” means physical storage location versus functional custody:
OD19-01 MUST NOT reinterpret or silently amend the locked §15.12 statement that verification material exists “only in K4.” Whether the eventual storage domain is consistent with that statement must be established by the OD19-01 resolution and, if necessary, an explicit higher-authority architecture amendment.
This is particularly important because option (b) could otherwise be accepted merely by treating “only in K4” as “only used by K4.”
We should not make that semantic move ourselves.
R01d — Integrity boundary
The analysis correctly identifies that this is a trust-anchor integrity question, not a confidentiality question.
OD19-01 MUST account for the fact that assertion verification material is security-sensitive because modification changes which K2 signing authority K4 accepts. The selected storage domain and provisioning path MUST therefore preserve the applicable authority and integrity boundaries.
This does not select K7 or K11H.
R01e — R6b interaction remains conditional
Don't yet conclude that C cannot write DC-18; that depends on the final classification and placement.
Whether R6b applies to DC-18's authoritative write path remains unresolved until the authoritative storage domain, ownership, and configuration classification are established. No placement option may be accepted on the assumption that C-writability is permissible where the material would widen authority.
That keeps R6b intact without prematurely deciding the classification.
R01f — Restore implications
The K7 option has a serious consequence that should remain visible:
If OD19-01 ultimately assigns DC-18 to SD-K7, the resolution MUST explicitly address the consequences of R17 K7 restore semantics for assertion-verification material, including key rollover and post-backup key changes. A K7 restore MUST NOT silently cause K4 to accept an obsolete assertion-verification authority merely because that material was present in the restored backup.
This doesn't prohibit K7 storage; it says the consequence must be solved if that option is selected.
R01g — K11H implications
Likewise, don't prejudge option (b):
If OD19-01 ultimately assigns DC-18 to SD-K11H, the resolution MUST establish how provisioning, rollover, upgrade, rollback, and K11H integrity interact with §15.12, §15.14, T-21, R19j, and the applicable §22/K2 gate.
R01h — Key rollover
The candidate correctly notes that rollover may require multiple simultaneously valid verification materials.
OD19-01 MUST permit the P2-defined assertion-verification rollover model, including any required overlap period, without violating R1. Multiple active values of one data class do not constitute multiple authoritative storage domains. Their lifecycle and validity semantics remain subject to P2 and §22.
This avoids incorrectly treating “one authoritative data class” as “exactly one value.”
Owner decision
OD19-01 — KEEP OPEN / DEFER
I would record it as an OPEN decision, not as an accepted placement choice.
Carry forward:
R01a
The authoritative storage domain and owner of DC-18 (K2 identity-assertion verification material) remain OPEN pending OD19-01. Until resolved, §19 MUST NOT assign DC-18 to SD-K7, SD-K11H, or any other storage domain as its authoritative home. The eventual assignment MUST satisfy R1 and the applicable higher-authority constraints.
R01b
OD19-01 MUST be resolved through coordination of P2, §22/recovery, and the applicable CyberPanel K2 gate. P2 determines the assertion/verification semantics; §22 determines provisioning and recovery mechanics; the K2 gate determines platform-specific installation and presentation constraints. The authoritative storage-domain decision remains a §19 architecture decision constrained by those results.
R01c
OD19-01 MUST NOT reinterpret or silently amend the locked §15.12 statement that verification material exists “only in K4.” Whether the eventual storage domain is consistent with that statement must be established by the OD19-01 resolution and, if necessary, an explicit higher-authority architecture amendment.
R01d
OD19-01 MUST account for the fact that assertion verification material is security-sensitive because modification changes which K2 signing authority K4 accepts. The selected storage domain and provisioning path MUST therefore preserve the applicable authority and integrity boundaries.
R01e
Whether R6b applies to DC-18's authoritative write path remains unresolved until the authoritative storage domain, ownership, and configuration classification are established. No placement option may be accepted on the assumption that C-writability is permissible where the material would widen authority.
R01f
If OD19-01 ultimately assigns DC-18 to SD-K7, the resolution MUST explicitly address the consequences of R17 K7 restore semantics for assertion-verification material, including key rollover and post-backup key changes. A K7 restore MUST NOT silently cause K4 to accept an obsolete assertion-verification authority merely because that material was present in the restored backup.
R01g
If OD19-01 ultimately assigns DC-18 to SD-K11H, the resolution MUST establish how provisioning, rollover, upgrade, rollback, and K11H integrity interact with §15.12, §15.14, T-21, R19j, and the applicable §22/K2 gate.
R01h
OD19-01 MUST permit the P2-defined assertion-verification rollover model, including any required overlap period, without violating R1. Multiple active values of one data class do not constitute multiple authoritative storage domains. Their lifecycle and validity semantics remain subject to P2 and §22.
Additional review notes

* Do not select SD-K7 or SD-K11H yet.
* Do not reinterpret “only in K4” to make one option fit.
* The final §19 candidate must not contain `SD-K7 or SD-K11H` as an authoritative-domain statement.
* This does not block locking §19, provided DC-18 is explicitly marked OPEN and assigned to OD19-01 rather than given a provisional authoritative home.
* It does block P2 completion and identity-assertion implementation, as the analysis correctly notes.
* K2 signing-key material and verification material remain distinct: R15b permits operational signing-key provisioning but does not decide verification-material custody.
* Key rollover may require multiple simultaneously valid verification values without violating R1.
```

> **Transcription note:** Process-wrapper lines ("No files changed", "No commit/push", "No decision-log update",
> "Proceed to …") are omitted (DEC-030 Q3). The text is otherwise verbatim.

---

## DEC-052 — OD19-02 — At-rest encryption

- **Status:** CURRENT (deferral — question OPEN)
- **Source:** §19 owner disposition review; owner message for OD19-02 (2026-09-23).
- **Related:** §19.9, §19.15, §19.16, §19.21; Q19-01

```text
OD19-02 — Owner disposition
DEFER / KEEP OPEN
I would not choose Required, Optional, or Not Required yet.
The analysis correctly shows that this question crosses storage protection, key custody, availability/recovery, and the unresolved K6-only credential-custody issue. More importantly, choosing “Optional” now would create two security postures that §19 would then have to specify everywhere; choosing “Required” would create a new key-custody and recovery dependency before §22 has designed it.
There is also an important scope correction: the question should not silently be limited to K7/K6P if §19 is going to establish a general at-rest policy. But I would not expand the policy to K8/K11H/K2 by deciding they must use encryption. Their inclusion should remain part of OD19-02's scope determination.
R02a — Keep the policy question open
OD19-02 remains OPEN. §19 does not presently establish whether SCC-controlled at-rest encryption within any storage domain is required, optional, or not required. Until OD19-02 is resolved, §19 MUST NOT represent on-host encryption as an established security requirement or as an established absence of such a requirement.
This preserves the three-way decision without prematurely choosing one.
R02b — No root-protection claim
This part is already strongly supported by R10f and should remain explicit:
Any SCC-controlled at-rest encryption MUST NOT be represented as protecting SCC data against a root-equivalent or kernel-level compromise of the host. Such encryption may address offline-media or comparable threats only to the extent established by the eventual design.
That prevents the architecture from making a false security claim regardless of the eventual choice.
R02c — Scope of OD19-02
I would expand the question's review scope, but not prescribe encryption for the omitted domains:
OD19-02 MUST determine which SCC-controlled storage domains and data classes, if any, are subject to an SCC at-rest-encryption requirement. The review MUST explicitly consider at least SD-K7, SD-K8, and SD-K6P, and MUST record the disposition of SD-K11H and SD-K2 rather than leaving their treatment implicit.
This is better than simply saying “OD19-02 applies to all domains,” because that would itself prejudge the answer.
R02d — Key custody is a separate decision
If OD19-02 adopts SCC-controlled at-rest encryption for a storage domain, the corresponding encryption key material becomes a separately governed secret/data class subject to R1. OD19-02 does not itself establish the key's provisioning, custody, rotation, backup, recovery, or destruction mechanics; those remain subject to §22.
This prevents encryption from silently creating an unmanaged secret class.
R02e — Availability and fail-closed behavior
Preserve R10g:
OD19-02 does not establish a general fail-closed rule for unavailable at-rest-encryption keys. Any requirement to refuse reads, writes, startup, restore, or other operations when an encryption key is unavailable MUST be established by the applicable storage-domain lifecycle and recovery design.
That is important because “required encryption” does not automatically mean “component refuses to start if the key is unavailable.”
R02f — Host-provided encryption
Don't decide whether full-disk/host encryption satisfies an eventual SCC requirement yet:
OD19-02 does not, by itself, determine whether host-provided encryption satisfies any SCC at-rest-encryption requirement. If host-provided protection is proposed as satisfying an SCC requirement, the applicable threat model, trust boundary, evidence, and control ownership MUST be established by the relevant architecture.
This keeps the SCC architecture from assuming that a host feature is equivalent to an SCC control.
R02g — Backup/export encryption remains distinct
PD19-10/R10a/R10e remain applicable to SCC-controlled backups and exports containing secret material. OD19-02 does not replace or weaken those requirements, and encryption of an in-host storage domain MUST NOT be treated as authorization to create an external backup or export of K6-custodied credential material.
This is particularly important given the unresolved R10b question.
R02h — K6 credential ciphertext question remains explicitly open
I would add this to the OD19-02 record:
OD19-02 MUST NOT resolve R10b by implication. Whether ciphertext representing K6-custodied credential material may exist outside SD-K6P remains separately OPEN unless and until an authoritative decision establishes that such ciphertext is compatible with the locked K6-only custody requirements.
This preserves your observation about §15.12 and T-18 exactly where it belongs.
R02i — Crypto-erasure
Don't introduce it accidentally:
OD19-02 does not establish a claim of crypto-erasure. Any future claim that destruction of an encryption key constitutes an acceptable disposition of protected data must be separately established against the applicable retention, destruction, recovery, and threat-model requirements.
That keeps R12A-1 intact without declaring crypto-erasure either valid or invalid.
Owner decision
OD19-02 — DEFER / KEEP OPEN
Carry forward:
R02a
OD19-02 remains OPEN. §19 does not presently establish whether SCC-controlled at-rest encryption within any storage domain is required, optional, or not required. Until OD19-02 is resolved, §19 MUST NOT represent on-host encryption as an established security requirement or as an established absence of such a requirement.
R02b
Any SCC-controlled at-rest encryption MUST NOT be represented as protecting SCC data against a root-equivalent or kernel-level compromise of the host. Such encryption may address offline-media or comparable threats only to the extent established by the eventual design.
R02c
OD19-02 MUST determine which SCC-controlled storage domains and data classes, if any, are subject to an SCC at-rest-encryption requirement. The review MUST explicitly consider at least SD-K7, SD-K8, and SD-K6P, and MUST record the disposition of SD-K11H and SD-K2 rather than leaving their treatment implicit.
R02d
If OD19-02 adopts SCC-controlled at-rest encryption for a storage domain, the corresponding encryption key material becomes a separately governed secret/data class subject to R1. OD19-02 does not itself establish the key's provisioning, custody, rotation, backup, recovery, or destruction mechanics; those remain subject to §22.
R02e
OD19-02 does not establish a general fail-closed rule for unavailable at-rest-encryption keys. Any requirement to refuse reads, writes, startup, restore, or other operations when an encryption key is unavailable MUST be established by the applicable storage-domain lifecycle and recovery design.
R02f
OD19-02 does not, by itself, determine whether host-provided encryption satisfies any SCC at-rest-encryption requirement. If host-provided protection is proposed as satisfying an SCC requirement, the applicable threat model, trust boundary, evidence, and control ownership MUST be established by the relevant architecture.
R02g
PD19-10/R10a/R10e remain applicable to SCC-controlled backups and exports containing secret material. OD19-02 does not replace or weaken those requirements, and encryption of an in-host storage domain MUST NOT be treated as authorization to create an external backup or export of K6-custodied credential material.
R02h
OD19-02 MUST NOT resolve R10b by implication. Whether ciphertext representing K6-custodied credential material may exist outside SD-K6P remains separately OPEN unless and until an authoritative decision establishes that such ciphertext is compatible with the locked K6-only custody requirements.
R02i
OD19-02 does not establish a claim of crypto-erasure. Any future claim that destruction of an encryption key constitutes an acceptable disposition of protected data must be separately established against the applicable retention, destruction, recovery, and threat-model requirements.
Review notes

* No choice yet among Required / Optional / Not Required.
* OD19-02's scope should explicitly consider K7, K8, K6P, K11H, and K2, without prejudging the result.
* At-rest encryption is an offline/media-threat control, not a root-compromise control.
* Any encryption key becomes its own governed data/secret class under R1.
* Key provisioning/custody/recovery remains §22 territory.
* Host-provided encryption is not automatically equivalent to an SCC control.
* R10b — whether K6 credential ciphertext can exist outside K6 — remains separately open.
* Backup/export rules under R10a/R10e remain independent.
* No crypto-erasure claim is established.
* Conditional §19 rows remain explicitly conditional/open.
```

> **Transcription note:** Process-wrapper lines ("No files changed", "No commit/push", "No decision-log update",
> "Proceed to …") are omitted (DEC-030 Q3). The text is otherwise verbatim.

---

## DEC-053 — OD19-03 — Approval validity horizon; R03e correction

- **Status:** CURRENT (deferral — question OPEN)
- **Source:** §19 owner disposition review; owner message for OD19-03, and the owner's R03e wording confirmation (2026-09-23).
- **Related:** §19.12, §19.21, §19.21.2; Q19-04

```text
OD19-03 — Owner disposition
DEFER / KEEP OPEN
I would not choose (a), (b), or (c) yet.
The important change from the original candidate is that R11b has removed the need for a global horizon merely to make nonce retention safe. Each used nonce is retained through the deadline of its own approval evidence. Therefore OD19-03 is now primarily a question of whether the architecture wants to impose a maximum approval validity window, and, separately, whether such a horizon is needed by some future recovery design.
I would also keep the two possible enforcement locations separate. A tool-enforced horizon and a K6-enforced horizon are materially different authority models.
R03a — Keep the existence of a horizon open
OD19-03 remains OPEN as to whether SCC imposes a maximum approval-validity horizon and, if so, what value and enforcement authority establish it. §19 MUST NOT assume a finite approval horizon until OD19-03 is resolved.
This prevents the existing open question from accidentally becoming a hidden requirement.
R03b — Do not use horizon as a nonce-retention prerequisite
R11b is already sufficient:
Approval nonce retention MUST continue to be governed by R11b independently of whether OD19-03 establishes a maximum approval-validity horizon. The absence of a global horizon MUST NOT permit premature eviction of a nonce required by R11b.
This is important because option (c) does not create a safety violation merely because retention can become unbounded.
R03c — Separate approval validity from Operation duration
The distinction in the candidate should be preserved:
OD19-03 does not redefine `max_duration`, the Operation execution ceiling, or the relationship between `deadline` and `max_duration` established by §16. A maximum approval-validity horizon, if adopted, is a separate constraint on approval evidence.
R03d — Enforcement authority remains open
Don't choose the approval tool or K6 yet:
If a maximum approval-validity horizon is adopted, OD19-03 MUST establish its authoritative enforcement point. Enforcement solely by the approval tool, enforcement by K6, or a combination of controls are distinct architectural choices and MUST NOT be treated as equivalent.
This preserves option (a) vs (b).
R03e — K6 enforcement would require §16 treatment
If the owner eventually chooses a K6-enforced value:
If K6 is required to enforce an approval-validity horizon, the applicable §16 Global Execution Policy, validation sequence, refusal behavior, and authoritative value MUST be established explicitly before implementation. PD19-03 does not amend §16 by implication.
This directly captures the candidate's possible §16 amendment.
R03f — Approval-tool-only enforcement
Likewise:
If the approval tool is the sole enforcement point, the authoritative tool contract MUST establish the maximum permitted `deadline` and its enforcement. K6 MUST NOT be assumed to enforce a horizon that is not represented in its authoritative validation contract.
That prevents the architecture from claiming K6 can enforce something it cannot currently know.
R03g — K8 loss/reinitialization
R18g should remain conditional:
OD19-03 does not establish a post-K8-reinitialization elapsed-time rule. Any such rule remains unavailable unless OD19-03 establishes an authoritative horizon and the applicable §16/§22 design provides an enforceable basis for it.
This preserves R18g–R18k.
R03h — No horizon value implied
OD19-03 does not establish or imply a numeric approval-validity horizon. No particular duration, including a default or maximum value, is authorized by this decision.
Worth stating explicitly because otherwise a future implementation could invent a convenient number.
R03i — K4-internal Actions
I would not expand OD19-03 to solve the K4-internal approval question. But the scope gap should be recorded:
OD19-03 concerns approval evidence subject to the §16/K8 approval-nonce lifecycle. It does not establish nonce-use, replay, retention, or validity semantics for K4-internal Actions that do not enter the K6/K8 request path. Those semantics remain open to the applicable §17/K4 architecture.
This prevents us from accidentally implying that R11b governs K4-internal Actions.
R03j — Unbounded option
I would not reject option (c). It has consequences, but those consequences are architectural facts rather than a reason to decide the question prematurely:
An absence of a global approval-validity horizon remains an admissible unresolved design outcome. If OD19-03 ultimately selects an unbounded model, K8 capacity and retention design MUST account for potentially unbounded approval-nonce retention, subject to R11e and the applicable §21/§22 lifecycle controls.
That keeps the option alive without endorsing it.
Owner decision
OD19-03 — DEFER / KEEP OPEN
Carry forward:
R03a
OD19-03 remains OPEN as to whether SCC imposes a maximum approval-validity horizon and, if so, what value and enforcement authority establish it. §19 MUST NOT assume a finite approval horizon until OD19-03 is resolved.
R03b
Approval nonce retention MUST continue to be governed by R11b independently of whether OD19-03 establishes a maximum approval-validity horizon. The absence of a global horizon MUST NOT permit premature eviction of a nonce required by R11b.
R03c
OD19-03 does not redefine `max_duration`, the Operation execution ceiling, or the relationship between `deadline` and `max_duration` established by §16. A maximum approval-validity horizon, if adopted, is a separate constraint on approval evidence.
R03d
If a maximum approval-validity horizon is adopted, OD19-03 MUST establish its authoritative enforcement point. Enforcement solely by the approval tool, enforcement by K6, or a combination of controls are distinct architectural choices and MUST NOT be treated as equivalent.
R03e
If K6 is required to enforce an approval-validity horizon, the applicable §16 Global Execution Policy, validation sequence, refusal behavior, and authoritative value MUST be established explicitly before implementation. PD19-03 does not amend §16 by implication.
R03f
If the approval tool is the sole enforcement point, the authoritative tool contract MUST establish the maximum permitted `deadline` and its enforcement. K6 MUST NOT be assumed to enforce a horizon that is not represented in its authoritative validation contract.
R03g
OD19-03 does not establish a post-K8-reinitialization elapsed-time rule. Any such rule remains unavailable unless OD19-03 establishes an authoritative horizon and the applicable §16/§22 design provides an enforceable basis for it.
R03h
OD19-03 does not establish or imply a numeric approval-validity horizon. No particular duration, including a default or maximum value, is authorized by this decision.
R03i
OD19-03 concerns approval evidence subject to the §16/K8 approval-nonce lifecycle. It does not establish nonce-use, replay, retention, or validity semantics for K4-internal Actions that do not enter the K6/K8 request path. Those semantics remain open to the applicable §17/K4 architecture.
R03j
An absence of a global approval-validity horizon remains an admissible unresolved design outcome. If OD19-03 ultimately selects an unbounded model, K8 capacity and retention design MUST account for potentially unbounded approval-nonce retention, subject to R11e and the applicable §21/§22 lifecycle controls.
Review notes

* No choice among finite horizon / tool-only / K6-enforced / unbounded is made yet.
* R11b independently handles nonce retention; the horizon is no longer necessary to make that rule valid.
* Do not invent a numeric horizon.
* A K6-enforced horizon would require explicit §16 treatment.
* A tool-only horizon would need to live in the approval-tool contract; K6 cannot enforce information it does not possess.
* R18's post-K8-reinitialization elapsed-time rule remains conditional and unresolved.
* K4-internal Actions are outside the K6/K8 nonce-retention scope and remain a separate open question.
* If ultimately unbounded, K8 capacity becomes an explicit §21/§22 concern.
```

> **Transcription note:** Process-wrapper lines ("No files changed", "No commit/push", "No decision-log update",
> "Proceed to …") are omitted (DEC-030 Q3). The text is otherwise verbatim.

R03e wording confirmation (first part of a combined owner message; its second part is recorded in DEC-054). The
recorded wording of R03e is the corrected one ("OD19-03 does not amend §16 by implication"):

```text
R03e wording confirmation
Yes — that was a typo. `PD19-03` should be `OD19-03`.
The intended wording is:
If K6 is required to enforce an approval-validity horizon, the applicable §16 Global Execution Policy, validation sequence, refusal behavior, and authoritative value MUST be established explicitly before implementation. OD19-03 does not amend §16 by implication.
Please carry that correction into the final change set. It does not change the substance of R03e.
```

---

## DEC-054 — OD19-04 — Credential-bearing file content

- **Status:** CURRENT (deferral — question OPEN)
- **Source:** §19 owner disposition review; owner message for OD19-04 (second part of the combined message whose first part is in DEC-053) (2026-09-23).
- **Related:** §19.13.1, §19.21, §19.21.2

```text
OD19-04 — Owner disposition
DEFER / KEEP OPEN
I would not make the authoring prohibition permanent yet, and I would not authorize the §16 credential-composition path yet.
The existing interim rule in R12B-1 through R12B-5 is sufficient to keep §19 internally consistent while preserving both architectural possibilities for later consideration.
The important point is that option (2) is substantially more than "add handle substitution to `file.replace`." It would require resolving the consequences you identified around validators, staged content, digest/postcondition handling, journaling/scrubbing, templates, and pre-images. Those questions belong to the §16 gate rather than being solved implicitly inside §19.
R04a — Keep the direction open
OD19-04 remains OPEN as to whether credential-bearing file content is permanently prohibited from `file.replace` or whether a future §16 amendment may establish an authorized handle-based content-composition path. Until resolved, R12B-1 through R12B-5 remain the governing interim rule.
R04b — Preserve the interim prohibition
Until OD19-04 is resolved, a K11 WRITE scope entry MUST NOT target a resource declared by the applicable execution contract to contain credential-bearing content. The interim prohibition remains fully effective and is not weakened by the existence of the unresolved §16 alternative.
This preserves R12B-1 rather than silently turning "OPEN" into permission.
R04c — No credential composition by implication
Nothing in OD19-04 authorizes K6 to compose credential-bearing file content, substitute credential handles into arbitrary `blob` content, or otherwise place resolved credential material into staged file content. Such behavior requires an explicit higher-authority §16 amendment.
This is particularly important because §16.9 currently says no request field carries credential material into K6.
R04d — Future §16 path must resolve the complete safety surface
If the owner later chooses the composition route:
A future §16 amendment permitting credential-bearing `file.replace` content MUST explicitly resolve, at minimum, the interaction with X-38 validator restrictions, staged-content custody, §16.8 postcondition/digest handling, X-24/X-26 output and journal scrubbing, TH-31 transformed-credential exposure, template/source provenance, and pre-image custody and destruction.
This avoids approving an incomplete mechanism merely because the basic handle substitution concept works.
R04e — No capability availability change
Until an authoritative §16 amendment establishes an authorized credential-bearing `file.replace` path, capabilities requiring such content remain unavailable under R12B-5. OD19-04 does not itself authorize those capabilities.
R04f — Do not close F19-05 prematurely
F19-05 remains OPEN while OD19-04 remains unresolved. The interim authoring restriction mitigates the identified declared-resource path but does not establish that arbitrary `blob` content is mechanically free of credential material, consistent with R12B-2 and the applicable §18 findings.
That distinction matters: the authoring restriction is not being represented as a complete runtime classification mechanism.
R04g — §22 remains downstream
OD19-04 does not establish credential lifecycle, pre-image destruction, or recovery mechanics. Those remain governed by PD19-11, PD19-12, PD19-16, and the applicable §22 design.
Owner decision
OD19-04 — DEFER / KEEP OPEN
Carry forward:
R04a
OD19-04 remains OPEN as to whether credential-bearing file content is permanently prohibited from `file.replace` or whether a future §16 amendment may establish an authorized handle-based content-composition path. Until resolved, R12B-1 through R12B-5 remain the governing interim rule.
R04b
Until OD19-04 is resolved, a K11 WRITE scope entry MUST NOT target a resource declared by the applicable execution contract to contain credential-bearing content. The interim prohibition remains fully effective and is not weakened by the existence of the unresolved §16 alternative.
R04c
Nothing in OD19-04 authorizes K6 to compose credential-bearing file content, substitute credential handles into arbitrary `blob` content, or otherwise place resolved credential material into staged file content. Such behavior requires an explicit higher-authority §16 amendment.
R04d
A future §16 amendment permitting credential-bearing `file.replace` content MUST explicitly resolve, at minimum, the interaction with X-38 validator restrictions, staged-content custody, §16.8 postcondition/digest handling, X-24/X-26 output and journal scrubbing, TH-31 transformed-credential exposure, template/source provenance, and pre-image custody and destruction.
R04e
Until an authoritative §16 amendment establishes an authorized credential-bearing `file.replace` path, capabilities requiring such content remain unavailable under R12B-5. OD19-04 does not itself authorize those capabilities.
R04f
F19-05 remains OPEN while OD19-04 remains unresolved. The interim authoring restriction mitigates the identified declared-resource path but does not establish that arbitrary `blob` content is mechanically free of credential material, consistent with R12B-2 and the applicable §18 findings.
R04g
OD19-04 does not establish credential lifecycle, pre-image destruction, or recovery mechanics. Those remain governed by PD19-11, PD19-12, PD19-16, and the applicable §22 design.
Change-set notes

* §19.14 should continue to show the OD19-04-dependent interim rule rather than implying permanent prohibition.
* §19.21 OD19-04 should remain explicitly OPEN.
* Do not amend §16 now.
* Do not close F19-05.
* Do not add a new runtime credential-composition mechanism.
* The eventual §16 gate must address the entire safety surface, not merely handle substitution.

The already-identified R10b, R11a, R20a, and the new K4-internal approval semantics item should remain tracked for IDs in the final change set.
```

> **Transcription note:** Process-wrapper lines ("No files changed", "No commit/push", "No decision-log update",
> "Proceed to …") are omitted (DEC-030 Q3). The text is otherwise verbatim.

---

## DEC-055 — OD19-05 — K4 visibility of credential-handle state

- **Status:** CURRENT (deferral — question OPEN)
- **Source:** §19 owner disposition review; owner message for OD19-05 (2026-09-23).
- **Related:** §19.7 (DC-14), §19.16, §19.21, §19.21.2

```text
OD19-05 — Owner disposition
DEFER / KEEP OPEN
I would not select (a), (b), or (c) at this stage.
The key distinction is that credential enforcement remains entirely K6-owned regardless of what K4 can see. OD19-05 is about advisory visibility for planning and presentation, not authorization or credential resolution.
Option (c) should remain an interim consequence, not be recorded as the architectural selection. K4 will necessarily discover an unusable handle through the locked stage-17 `CREDENTIAL_UNAVAILABLE` path if no earlier visibility mechanism exists, but that does not mean the architecture has affirmatively chosen refusal-only discovery.
R05a — Keep K4 visibility open
OD19-05 remains OPEN as to how K4 obtains credential-handle provisioning and usability metadata. Until resolved, §19 MUST NOT establish a K4-readable authoritative or non-authoritative representation of DC-14 outside its authoritative SD-K6P / CS domain.
This preserves the single-owner rule from R1.
R05b — Visibility cannot become authority
Any mechanism established to expose credential-handle metadata to K4 MUST NOT transfer credential custody, credential resolution authority, or lifecycle authority from K6 to K4. K6 remains the sole authority for credential resolution and enforcement under §16 and R16b.
This is the central architectural boundary.
R05c — No second authoritative representation
A non-authoritative representation of DC-14, if later established, MUST remain explicitly derived from the authoritative CS state and MUST NOT become an alternate source of truth. Its creation, refresh, invalidation, and divergence behavior MUST be defined by the applicable architecture.
This is particularly important if option (b) is eventually considered.
R05d — Option (a) requires §16 treatment
If K4 is given credential-handle metadata through an executor-family Operation, the applicable §16 gate MUST explicitly define whether the metadata is provided by an existing executor Operation or a new Operation, the exposed fields, freshness semantics, refusal behavior, journaling requirements, and the boundary between advisory visibility and K6 enforcement.
Don't assume this necessarily requires a new Operation; the existing executor family may or may not be extensible in a conforming way. That belongs to the §16 gate.
R05e — Option (b) requires lifecycle consistency
If a non-authoritative provisioning record is introduced through K9 or another §22 mechanism, §22 MUST establish its storage domain, ownership, update ordering, interruption behavior, recovery behavior, and relationship to the authoritative CS state. A provisioning record MUST NOT be treated as authoritative merely because it is newer or easier for K4 to read.
This captures the interrupted-provisioning and rotation concerns without choosing a storage domain.
R05f — Refusal-only remains the interim consequence
Until OD19-05 is resolved, K4 MUST NOT assume that a declared credential handle is provisioned or usable merely because the handle is present in an applicable declaration. K6 remains the authoritative enforcement point and MUST return `CREDENTIAL_UNAVAILABLE` when the locked stage-17 conditions are not satisfied. The absence of an earlier K4 visibility mechanism MUST NOT be treated as an architectural selection of refusal-only discovery.
This is the important distinction between what happens today and what we have decided the architecture should permanently do.
R05g — Visibility does not authorize capability use
Credential-handle visibility metadata MUST NOT itself authorize planning, approval, execution, or credential resolution. Any future capability-availability indication derived from such metadata MUST remain advisory and MUST NOT weaken the applicable §17 authorization or §16 K6 enforcement checks.
This prevents "provisioned" from becoming a hidden authorization signal.
R05h — Do not overdefine DC-14 fields yet
OD19-05 does not establish that K4 may receive material version, provisioning timestamps, rotation timestamps, orphaned state, stale state, or other DC-14 metadata. The minimum metadata exposed to K4 remains OPEN and MUST be established by the applicable §16/§22 design.
That keeps the candidate from prematurely exposing sensitive lifecycle information.
R05i — R16h remains independent
OD19-05 does not establish the reporting mechanism contemplated by R16h. A future handle-status mechanism MAY satisfy some reporting requirements for orphaned or stale credentials, but such use is not established by OD19-05 and MUST remain subject to the applicable contract.
Owner decision
OD19-05 — DEFER / KEEP OPEN
Carry forward:
R05a
OD19-05 remains OPEN as to how K4 obtains credential-handle provisioning and usability metadata. Until resolved, §19 MUST NOT establish a K4-readable authoritative or non-authoritative representation of DC-14 outside its authoritative SD-K6P / CS domain.
R05b
Any mechanism established to expose credential-handle metadata to K4 MUST NOT transfer credential custody, credential resolution authority, or lifecycle authority from K6 to K4. K6 remains the sole authority for credential resolution and enforcement under §16 and R16b.
R05c
A non-authoritative representation of DC-14, if later established, MUST remain explicitly derived from the authoritative CS state and MUST NOT become an alternate source of truth. Its creation, refresh, invalidation, and divergence behavior MUST be defined by the applicable architecture.
R05d
If K4 is given credential-handle metadata through an executor-family Operation, the applicable §16 gate MUST explicitly define whether the metadata is provided by an existing executor Operation or a new Operation, the exposed fields, freshness semantics, refusal behavior, journaling requirements, and the boundary between advisory visibility and K6 enforcement.
R05e
If a non-authoritative provisioning record is introduced through K9 or another §22 mechanism, §22 MUST establish its storage domain, ownership, update ordering, interruption behavior, recovery behavior, and relationship to the authoritative CS state. A provisioning record MUST NOT be treated as authoritative merely because it is newer or easier for K4 to read.
R05f
Until OD19-05 is resolved, K4 MUST NOT assume that a declared credential handle is provisioned or usable merely because the handle is present in an applicable declaration. K6 remains the authoritative enforcement point and MUST return `CREDENTIAL_UNAVAILABLE` when the locked stage-17 conditions are not satisfied. The absence of an earlier K4 visibility mechanism MUST NOT be treated as an architectural selection of refusal-only discovery.
R05g
Credential-handle visibility metadata MUST NOT itself authorize planning, approval, execution, or credential resolution. Any future capability-availability indication derived from such metadata MUST remain advisory and MUST NOT weaken the applicable §17 authorization or §16 K6 enforcement checks.
R05h
OD19-05 does not establish that K4 may receive material version, provisioning timestamps, rotation timestamps, orphaned state, stale state, or other DC-14 metadata. The minimum metadata exposed to K4 remains OPEN and MUST be established by the applicable §16/§22 design.
R05i
OD19-05 does not establish the reporting mechanism contemplated by R16h. A future handle-status mechanism MAY satisfy some reporting requirements for orphaned or stale credentials, but such use is not established by OD19-05 and MUST remain subject to the applicable contract.
Change-set notes

* §19 DC-14 keeps “K4 visibility OPEN (OD19-05)”.
* No K4-readable copy of DC-14 is created or authorized now.
* No new executor Operation is created.
* No K9/K7/K11H provisioning-status record is selected.
* Refusal at K6 remains the current enforcement consequence, not a permanent architectural selection.
* F19-07 remains open.
* R16h remains independently open.

The four pending ID items remain unchanged:

* R10b — K6 credential ciphertext outside K6
* R11a — idempotency retention/key reuse
* R20a — identity-slice definition
* R03i — K4-internal Action approval semantics
```

> **Transcription note:** Process-wrapper lines ("No files changed", "No commit/push", "No decision-log update",
> "Proceed to …") are omitted (DEC-030 Q3). The text is otherwise verbatim.

---

## DEC-056 — OD19-06 — DC-05 retention

- **Status:** CURRENT (deferral — question OPEN)
- **Source:** §19 owner disposition review; owner message for OD19-06 (2026-09-23).
- **Related:** §19.5.1, §19.7 (DC-05), §19.12, §19.21

```text
OD19-06 — Owner disposition
DEFER / KEEP OPEN
I would keep OD19-06 open. The important issue here is ownership of the retention decision, because §15 explicitly places retention in §19, while the current candidate points toward “§21 / owner.” I would not silently transfer the authority to §21.
The cleanest treatment is:

* §19 owns the retention policy for DC-05.
* §21 may establish retention requirements arising from audit/event dependencies and the records that reference DC-05.
* §19 must incorporate those requirements as constraints when the OD19-06 period is eventually resolved.
* The actual period/value remains open.

That preserves the locked §15 scope while recognizing that §21 can create a retention floor through authoritative audit relationships.
R06a — §19 retains ownership
OD19-06 remains OPEN as to the retention period and retention basis for DC-05 observation evidence and health history. The retention policy for this §19 data class remains a §19 concern under the locked §15 scope; §21 may establish retention requirements arising from audit/event dependencies that constrain the §19 retention decision.
This avoids allowing the candidate's “§21 / owner” wording to override §15.
R06b — Scope the question to DC-05
For purposes of OD19-06, “health history / evidence history” means DC-05 observation evidence and health history. It does not establish retention policy for K8 approval evidence, K8 execution evidence, K7 Approval Records, or other evidence classes governed by their applicable architecture.
This resolves the terminology ambiguity without creating new policy.
R06c — Existing retention floor remains authoritative
Any retention period established under OD19-06 MUST satisfy the retention floor established by R9a and R9b. A DC-05 record MUST remain resolvable for as long as an authoritative SCC record requires that record to remain resolvable. OD19-06 does not establish a shorter independent period that overrides those dependencies.
R06d — No default retention value
Until OD19-06 is resolved, §19 MUST NOT imply that DC-05 history is retained indefinitely, retained for a fixed default period, or discarded as soon as it is no longer needed for current-value derivation.
This is important because DC-05 history cannot necessarily be reconstructed from the current observation.
R06e — No automatic deletion once dependencies end
Expiration of an OD19-06 retention period, once established, MUST NOT by itself authorize deletion of a DC-05 record where another applicable lifecycle, audit, recovery, or architectural requirement requires its continued retention. Consistent with R9d, the retention period establishes neither an unconditional deletion command nor a physical-erasure guarantee.
R06f — Capacity is a design constraint, not the retention policy
K7 capacity limits and the refusal behavior established by LC-08 MUST be accounted for in the eventual DC-05 retention design, but capacity exhaustion MUST NOT itself establish the retention period or authorize deletion contrary to the applicable retention floor.
This keeps us from accidentally deriving policy from available disk space.
R06g — Configurability remains open
OD19-06 does not establish whether the eventual DC-05 retention period is fixed, scope-specific, or configurable. If retention is made C-writable, the applicable configuration contract MUST establish the permitted range and security effect; R6b and R6c continue to govern the authority of C-writable configuration.
I would not decide here whether reducing forensic history is a security-sensitive configuration.
R06h — Sensitivity classification remains separate
OD19-06 does not resolve CHANGE-023 or establish a general sensitivity classification for DC-05 content. Retention requirements MUST remain compatible with whatever sensitivity and exposure classification is subsequently established for the affected content.
This keeps the two questions coordinated without prematurely merging them.
R06i — §21 dependency
Before OD19-06 is finally resolved, §21 MUST identify any authoritative audit or event records whose retention or historical resolvability creates a dependency on DC-05. Those dependencies become constraints on the §19 retention decision under R9a and R9b; §21 does not thereby become the owner of the DC-05 retention policy.
R06j — §20 dependency
If §20 later establishes that historical DC-05 observations are required for reconciliation, desired-state evaluation, or drift analysis, that requirement becomes an additional dependency on DC-05 retention. OD19-06 does not pre-commit §20 to any particular historical-observation requirement.
R06k — Identity slice
OD19-06 does not define the scope of the identity slice. Whether the identity slice consumes DC-05 observation or health history remains governed by the separate R20a scope-definition item.
This keeps R20a from being accidentally resolved through OD19-06.
Owner decision
OD19-06 — DEFER / KEEP OPEN
Carry forward:
R06a
OD19-06 remains OPEN as to the retention period and retention basis for DC-05 observation evidence and health history. The retention policy for this §19 data class remains a §19 concern under the locked §15 scope; §21 may establish retention requirements arising from audit/event dependencies that constrain the §19 retention decision.
R06b
For purposes of OD19-06, “health history / evidence history” means DC-05 observation evidence and health history. It does not establish retention policy for K8 approval evidence, K8 execution evidence, K7 Approval Records, or other evidence classes governed by their applicable architecture.
R06c
Any retention period established under OD19-06 MUST satisfy the retention floor established by R9a and R9b. A DC-05 record MUST remain resolvable for as long as an authoritative SCC record requires that record to remain resolvable. OD19-06 does not establish a shorter independent period that overrides those dependencies.
R06d
Until OD19-06 is resolved, §19 MUST NOT imply that DC-05 history is retained indefinitely, retained for a fixed default period, or discarded as soon as it is no longer needed for current-value derivation.
R06e
Expiration of an OD19-06 retention period, once established, MUST NOT by itself authorize deletion of a DC-05 record where another applicable lifecycle, audit, recovery, or architectural requirement requires its continued retention. Consistent with R9d, the retention period establishes neither an unconditional deletion command nor a physical-erasure guarantee.
R06f
K7 capacity limits and the refusal behavior established by LC-08 MUST be accounted for in the eventual DC-05 retention design, but capacity exhaustion MUST NOT itself establish the retention period or authorize deletion contrary to the applicable retention floor.
R06g
OD19-06 does not establish whether the eventual DC-05 retention period is fixed, scope-specific, or configurable. If retention is made C-writable, the applicable configuration contract MUST establish the permitted range and security effect; R6b and R6c continue to govern the authority of C-writable configuration.
R06h
OD19-06 does not resolve CHANGE-023 or establish a general sensitivity classification for DC-05 content. Retention requirements MUST remain compatible with whatever sensitivity and exposure classification is subsequently established for the affected content.
R06i
Before OD19-06 is finally resolved, §21 MUST identify any authoritative audit or event records whose retention or historical resolvability creates a dependency on DC-05. Those dependencies become constraints on the §19 retention decision under R9a and R9b; §21 does not thereby become the owner of the DC-05 retention policy.
R06j
If §20 later establishes that historical DC-05 observations are required for reconciliation, desired-state evaluation, or drift analysis, that requirement becomes an additional dependency on DC-05 retention. OD19-06 does not pre-commit §20 to any particular historical-observation requirement.
R06k
OD19-06 does not define the scope of the identity slice. Whether the identity slice consumes DC-05 observation or health history remains governed by the separate R20a scope-definition item.
Change-set notes

* §19.14 continues to show Health history / evidence history — OPEN (OD19-06).
* §19.21 continues to identify OD19-06 as OPEN.
* The owner is §19, consistent with the locked §15 scope.
* §21 is a dependency/constraint source, not silently made the owner of DC-05 retention.
* No default retention period is established.
* No “retain indefinitely” behavior is implied.
* No “delete when no longer needed” behavior is implied.
* R9a/R9b remain the minimum retention floor.
* CHANGE-023 remains open.
* R20a remains separate.
```

> **Transcription note:** Process-wrapper lines ("No files changed", "No commit/push", "No decision-log update",
> "Proceed to …") are omitted (DEC-030 Q3). The text is otherwise verbatim.

---

## DEC-057 — OD19-07 — Pre-image retention bounds

- **Status:** CURRENT (deferral — question OPEN)
- **Source:** §19 owner disposition review; owner message for OD19-07 (2026-09-23).
- **Related:** §19.11.1, §19.12, §19.21, §19.21.2

```text
OD19-07 — Owner disposition
DEFER / KEEP OPEN
I would keep OD19-07 open and not yet establish the Global Execution Policy maximum.
There is an important distinction here: R11f is already an accepted owner decision requiring bounded, per-scope-entry retention, while OD19-07 determines how that requirement can actually be represented and enforced within the locked §16/K11 model. We should not silently convert the proposed Global Execution Policy maximum into architecture merely because it appears in the current candidate wording.
R07a — Preserve the already-accepted bound
R11f remains authoritative: pre-image retention MUST be bounded rather than indefinite, and the applicable retention MUST be declared for the relevant scope entry. OD19-07 does not weaken, defer, or reopen R11f.
This is important: we're deferring the representation/enforcement mechanism, not the underlying bounded-retention decision.
R07b — Global maximum remains open
OD19-07 remains OPEN as to whether a Global Execution Policy maximum is required in addition to the per-scope-entry retention declaration. No global maximum value, field, or enforcement rule is established by OD19-07.
R07c — Do not imply the current K11 structure supports R11f
Until the applicable §16 gate resolves the representation of R11f, §19 MUST NOT represent a pre-image retention declaration as an existing K11 scope-entry field. The locked §16 scope-entry structure remains authoritative until explicitly amended or clarified through its applicable gate.
This is the critical correction to the current candidate's §19.14 wording.
R07d — Possible §16 change
If the per-scope-entry retention declaration or a Global Execution Policy maximum requires a field or behavior not present in the locked §16 structures, the applicable §16 gate MUST determine whether the change is a clarification or an amendment and MUST establish the corresponding K6 load-time and runtime behavior.
Don't pre-decide that it's merely a clarification.
R07e — K11 remains authoritative
Any eventual K6-enforced pre-image retention limit MUST be derived from authoritative K11 content consistent with §16. OD19-07 does not authorize C, K9, the Host Restriction Overlay, or another component to shorten or otherwise alter a retention value established by the applicable execution declaration.
The overlay can still exclude, per the locked rule; it doesn't become a retention policy mechanism.
R07f — No global maximum by implication
The current §19 candidate MUST NOT state or imply that the Global Execution Policy already contains a pre-image retention maximum. Until OD19-07 and the applicable §16 gate are resolved, the existence and representation of such a maximum remain OPEN.
This directly addresses the current §19.14 wording.
R07g — Pre-image store exhaustion remains separate
OD19-07 does not establish behavior when the applicable pre-image storage is unavailable or exhausted. Whether `file.replace` MUST refuse, whether retention may be reduced, and what happens to `file.restore_preimage` remain separate lifecycle and execution questions subject to the applicable §16/§22 design. K8 capacity rules under R11e do not automatically apply to pre-image storage.
This avoids accidentally extending X-29's K8 rule to K6's pre-image store.
R07h — Expiry remains §22 territory
OD19-07 does not establish what occurs when a declared pre-image retention period expires. Destruction, `file.restore_preimage` availability after expiry, interrupted destruction, and recovery remain governed by R12A-5, R11g, and the applicable §22 design.
R07i — No retention value
OD19-07 does not establish or imply any numeric pre-image retention period or Global Execution Policy maximum.
Owner decision
OD19-07 — DEFER / KEEP OPEN
Carry forward:
R07a
R11f remains authoritative: pre-image retention MUST be bounded rather than indefinite, and the applicable retention MUST be declared for the relevant scope entry. OD19-07 does not weaken, defer, or reopen R11f.
R07b
OD19-07 remains OPEN as to whether a Global Execution Policy maximum is required in addition to the per-scope-entry retention declaration. No global maximum value, field, or enforcement rule is established by OD19-07.
R07c
Until the applicable §16 gate resolves the representation of R11f, §19 MUST NOT represent a pre-image retention declaration as an existing K11 scope-entry field. The locked §16 scope-entry structure remains authoritative until explicitly amended or clarified through its applicable gate.
R07d
If the per-scope-entry retention declaration or a Global Execution Policy maximum requires a field or behavior not present in the locked §16 structures, the applicable §16 gate MUST determine whether the change is a clarification or an amendment and MUST establish the corresponding K6 load-time and runtime behavior.
R07e
Any eventual K6-enforced pre-image retention limit MUST be derived from authoritative K11 content consistent with §16. OD19-07 does not authorize C, K9, the Host Restriction Overlay, or another component to shorten or otherwise alter a retention value established by the applicable execution declaration.
R07f
The current §19 candidate MUST NOT state or imply that the Global Execution Policy already contains a pre-image retention maximum. Until OD19-07 and the applicable §16 gate are resolved, the existence and representation of such a maximum remain OPEN.
R07g
OD19-07 does not establish behavior when the applicable pre-image storage is unavailable or exhausted. Whether `file.replace` MUST refuse, whether retention may be reduced, and what happens to `file.restore_preimage` remain separate lifecycle and execution questions subject to the applicable §16/§22 design. K8 capacity rules under R11e do not automatically apply to pre-image storage.
R07h
OD19-07 does not establish what occurs when a declared pre-image retention period expires. Destruction, `file.restore_preimage` availability after expiry, interrupted destruction, and recovery remain governed by R12A-5, R11g, and the applicable §22 design.
R07i
OD19-07 does not establish or imply any numeric pre-image retention period or Global Execution Policy maximum.
Change-set notes

* R11f remains locked-derived/accepted and is not reopened.
* §19.14 must not continue to state that a Global Execution Policy maximum already exists.
* §19.14 should instead distinguish:
   * bounded per-scope-entry retention — required by R11f;
   * representation/enforcement mechanism — OPEN under OD19-07;
   * Global Execution Policy maximum — OPEN.
* §19.21 OD19-07 remains explicitly OPEN.
* The §16 gate must decide whether R11f requires a new scope-entry field and whether a global maximum is appropriate.
* No numeric retention value is established.
* Pre-image-store exhaustion is not silently mapped to K8/X-29.
* Expiration/destruction remains §22 territory.
```

> **Transcription note:** Process-wrapper lines ("No files changed", "No commit/push", "No decision-log update",
> "Proceed to …") are omitted (DEC-030 Q3). The text is otherwise verbatim.

---

## DEC-058 — F19-05 — Credential-bearing `file.replace` content

- **Status:** CURRENT (finding deferred — OD19-04 / §16 Amendment Gate)
- **Source:** §19 owner disposition review; owner message for F19-05 (2026-09-23).
- **Related:** §19.5.3 (D19-05), §19.13.1, §19.19, §19.21.2; register §5A

```text
F19-05 — Owner disposition

DEFERRED TO OD19-04 / §16 GATE

The reason is straightforward: we already explicitly decided in R04f that:

“F19-05 remains OPEN while OD19-04 remains unresolved.”

So we should not classify it as acknowledged in a way that prematurely adds it to the known-findings index, and we definitely should not classify it as resolved.

The appropriate classification is deferred to another gate, specifically OD19-04 and, if the composition path remains under consideration, the §16 gate.

F05a — Preserve the finding without resolving its interpretation

F19-05 remains a known unresolved architectural finding concerning the interaction between credential-custody requirements and file.replace content handling. OD19-04 and the applicable §16 gate MUST determine whether the issue represents a prohibited path already excluded by the locked architecture, an enforcement gap, or a locked-text interaction requiring amendment or clarification.

This is better than deciding Reading 1 vs. Reading 2 now.

F05b — Preserve the identified unresolved surfaces

Resolution of F19-05 MUST account for, at minimum, credential-material entry into K4, staged-content handling, validator exposure under X-38, K8 digest/journal handling under §16.10.2 and X-26, transformed-credential exposure under TH-31, and the relationship to KF-06.

That doesn't mean all of these are defects. It means the later gate can't declare F19-05 resolved without accounting for them.

F05c — Interim rule remains operative

Until F19-05 is resolved through OD19-04 and the applicable §16 gate, R12B-1 through R12B-5 remain the governing interim restriction. F19-05 does not weaken or suspend that restriction.

F05d — No premature index classification

The §19 gate does not independently classify F19-05 as a new KF entry while OD19-04 remains open. Any addition to the known-findings index MUST follow the applicable owner decision and change-set process without modifying locked text.

That respects the DEC-030 distinction.

So what about all those questions?

You correctly spotted that we're beginning to encounter second-order questions.

But we don't need to answer them all now.

Question	Where it belongs
Does blob actually permit credential content?	§16 gate / OD19-04
How could credential material reach K4?	§16/P2/security-boundary analysis
Should K8 retain digests of credential-bearing content?	§16 / §21 as applicable
Transformed credentials / encoded forms	§18 TH-31
Relationship to KF-06	§16 gate
Permanent prohibition vs composition	OD19-04
New handle-composition mechanism	§16 amendment gate

So don't let F19-05 turn into another mini-OD. That's exactly how this process would spiral.

Owner decision

F19-05 — DEFERRED TO ANOTHER GATE

Carry forward:

F05a

F19-05 remains a known unresolved architectural finding concerning the interaction between credential-custody requirements and file.replace content handling. OD19-04 and the applicable §16 gate MUST determine whether the issue represents a prohibited path already excluded by the locked architecture, an enforcement gap, or a locked-text interaction requiring amendment or clarification.

F05b

Resolution of F19-05 MUST account for, at minimum, credential-material entry into K4, staged-content handling, validator exposure under X-38, K8 digest/journal handling under §16.10.2 and X-26, transformed-credential exposure under TH-31, and the relationship to KF-06.

F05c

Until F19-05 is resolved through OD19-04 and the applicable §16 gate, R12B-1 through R12B-5 remain the governing interim restriction. F19-05 does not weaken or suspend that restriction.

F05d

The §19 gate does not independently classify F19-05 as a new KF entry while OD19-04 remains open. Any addition to the known-findings index MUST follow the applicable owner decision and change-set process without modifying locked text.
```

> **Transcription note (session process):** The following review-session process lines are omitted; they
> governed only the review session and are not owner decisions: "No files. No commits. No decision-log change.".

---

## DEC-059 — F19-06 — Approval horizon; approval evidence after K8 loss

- **Status:** CURRENT (finding deferred — OD19-03 / §22 / §16 Amendment Gate)
- **Source:** §19 owner disposition review; owner message for F19-06 (2026-09-23).
- **Related:** §19.5.3 (D19-06); register §5A

```text
F19-06 — Owner disposition
DEFERRED TO ANOTHER GATE — OD19-03 / §22 / applicable §16 gate
I agree with the decomposition. The important thing is that F19-06 should not be treated as one unresolved defect anymore. Its three components have different statuses:

1. nonce retention → addressed by R11b + R03b;
2. whether an approval horizon should exist → OD19-03 remains open;
3. K8-loss/reinitialization behavior → requirements established by R18a/R18d, mechanism deferred to §22 / §16.

So we should not mark the entire finding "resolved," but neither should we preserve the original finding verbatim as though none of the work above happened.
F06a — Preserve the finding in decomposed form
F19-06 remains an unresolved architectural finding only with respect to the absence of an established maximum approval-validity horizon and the mechanism for satisfying approval-evidence requirements following K8 lifetime loss or reinitialization. The nonce-retention consequence identified in the original finding is governed by R11b and R03b and is no longer an unresolved retention-rule gap.
F06b — Horizon question routes to OD19-03
Whether the absence of a maximum approval-validity horizon constitutes a defect in the locked architecture remains subject to OD19-03. OD19-03 MUST determine whether a horizon exists, its authoritative enforcement point if adopted, and whether the resulting architecture requires any §16 amendment.
F06c — K8 recovery mechanism routes downstream
The mechanism by which K6 satisfies R18d for approval evidence following K8 loss or reinitialization remains subject to §22 and the applicable §16 gate. F19-06 does not itself establish a new K6 acceptance rule, blackout period, approval timestamp requirement, or recovery mechanism.
F06d — Do not resurrect the original replay claim
F19-06 MUST NOT be interpreted as authorizing replay after K8 loss. R18a and R18d remain authoritative: K8 loss or reinitialization is not an implicit reset of replay or nonce protections, and K6 MUST NOT rely on prior-lifetime evidence unless the applicable recovery design explicitly establishes that evidence as valid and available.
F06e — Anchor revocation remains existing mitigation
§17.9 anchor revocation remains an existing mechanism that invalidates outstanding approvals. F19-06 does not establish additional revocation semantics or treat anchor revocation as a substitute for the OD19-03 or K8-recovery decisions.
F06f — K4-internal approvals remain separate
F19-06 does not establish retention, replay, or validity semantics for approvals of K4-internal Actions. Those semantics remain separately routed to R03i and the applicable §17/K4 architecture.
Owner decision
F19-06 — DEFERRED TO ANOTHER GATE
Carry forward:
F06a
F19-06 remains an unresolved architectural finding only with respect to the absence of an established maximum approval-validity horizon and the mechanism for satisfying approval-evidence requirements following K8 lifetime loss or reinitialization. The nonce-retention consequence identified in the original finding is governed by R11b and R03b and is no longer an unresolved retention-rule gap.
F06b
Whether the absence of a maximum approval-validity horizon constitutes a defect in the locked architecture remains subject to OD19-03. OD19-03 MUST determine whether a horizon exists, its authoritative enforcement point if adopted, and whether the resulting architecture requires any §16 amendment.
F06c
The mechanism by which K6 satisfies R18d for approval evidence following K8 loss or reinitialization remains subject to §22 and the applicable §16 gate. F19-06 does not itself establish a new K6 acceptance rule, blackout period, approval timestamp requirement, or recovery mechanism.
F06d
F19-06 MUST NOT be interpreted as authorizing replay after K8 loss. R18a and R18d remain authoritative: K8 loss or reinitialization is not an implicit reset of replay or nonce protections, and K6 MUST NOT rely on prior-lifetime evidence unless the applicable recovery design explicitly establishes that evidence as valid and available.
F06e
§17.9 anchor revocation remains an existing mechanism that invalidates outstanding approvals. F19-06 does not establish additional revocation semantics or treat anchor revocation as a substitute for the OD19-03 or K8-recovery decisions.
F06f
F19-06 does not establish retention, replay, or validity semantics for approvals of K4-internal Actions. Those semantics remain separately routed to R03i and the applicable §17/K4 architecture.
Criterion 3
Your observation about §19.24 criterion 3 is correct. Do not solve that inside F19-06.
At the final gate-criteria reconciliation, the change set needs to reconcile criterion 3 with the fact that both F19-05 and F19-06 are being treated as findings while their actual index-entry treatment is deferred. That can be done later when we have the complete finding dispositions.
And yes — we're now doing exactly what we wanted to avoid: not reopening the same architecture questions every time a finding mentions them. F19-06 can be closed out at this level by routing its unresolved pieces to the decisions/gates that already own them.
```

> **Transcription note:** Process-wrapper lines ("No files changed", "No commit/push", "No decision-log update",
> "Proceed to …") are omitted (DEC-030 Q3). The text is otherwise verbatim.

---

## DEC-060 — F19-07 — K4 visibility of credential-handle state

- **Status:** CURRENT (rejected as a finding against locked text)
- **Source:** §19 owner disposition review; owner message for F19-07 (2026-09-23).
- **Related:** §19.5.3 (D19-07); register §5A

```text
F19-07 — Owner disposition
REJECTED AS A FINDING AGAINST LOCKED TEXT
This is the point where I would make a distinction that matters for keeping the review from expanding indefinitely:
F19-07 describes a real missing capability, but the evidence presented does not establish a defect or contradiction in locked §15–§17.
Nothing in the locked architecture requires K4 to know credential provisioning state before planning. K6's stage-17 enforcement is explicitly sufficient to prevent execution when the handle cannot resolve. The desirable earlier visibility is an unresolved architectural/product question, which is already captured by OD19-05.
So I would not carry F19-07 as another "known finding against locked text."
R07-Fa — Classification
F19-07 is rejected as a finding against locked text. The identified absence of K4 credential-handle provisioning visibility is a missing advisory capability rather than a demonstrated defect, contradiction, or violation of §15–§17.
R07-Fb — OD19-05 remains valid
Rejecting F19-07 as a finding does not resolve or close OD19-05. OD19-05 remains OPEN and continues to govern whether and how K4 may obtain advisory credential-handle provisioning and usability metadata.
R07-Fc — Enforcement remains complete
The absence of K4 advisory visibility MUST NOT weaken the locked K6 enforcement requirement. K6 remains the authoritative enforcement point and MUST apply the stage-17 credential-resolution checks and `CREDENTIAL_UNAVAILABLE` refusal semantics established by §16.
R07-Fd — Do not conflate provisioning journaling
F19-07 does not establish whether a Local Root Operator provisioning, rotation, revocation, or destruction act is recorded in K8 or elsewhere. Those lifecycle-recording questions remain subject to R16c, R16h, §21, and §22 as applicable.
R07-Fe — No criterion-3 index entry
F19-07 does not require known-finding index treatment under §19.24 criterion 3. Its rejection as a finding against locked text does not prevent the requirements of OD19-05 from being carried into the final change set.
Owner decision
F19-07 — REJECTED AS A FINDING AGAINST LOCKED TEXT
Carry forward:
R07-Fa
F19-07 is rejected as a finding against locked text. The identified absence of K4 credential-handle provisioning visibility is a missing advisory capability rather than a demonstrated defect, contradiction, or violation of §15–§17.
R07-Fb
Rejecting F19-07 as a finding does not resolve or close OD19-05. OD19-05 remains OPEN and continues to govern whether and how K4 may obtain advisory credential-handle provisioning and usability metadata.
R07-Fc
The absence of K4 advisory visibility MUST NOT weaken the locked K6 enforcement requirement. K6 remains the authoritative enforcement point and MUST apply the stage-17 credential-resolution checks and `CREDENTIAL_UNAVAILABLE` refusal semantics established by §16.
R07-Fd
F19-07 does not establish whether a Local Root Operator provisioning, rotation, revocation, or destruction act is recorded in K8 or elsewhere. Those lifecycle-recording questions remain subject to R16c, R16h, §21, and §22 as applicable.
R07-Fe
F19-07 does not require known-finding index treatment under §19.24 criterion 3. Its rejection as a finding against locked text does not prevent the requirements of OD19-05 from being carried into the final change set.
Why this is useful
This gives us a clean separation:

* F19-07: not a defect in locked architecture → closed as a finding.
* OD19-05: still open → determines whether advisory visibility should exist and how.
* §16 / §22: determine the eventual mechanism if the owner later wants that visibility.
* K6: already has authoritative enforcement; nothing needs to be invented to close a security hole.

And importantly, we don't need another finding about the fact that F19-07 isn't a finding. 😄
```

> **Transcription note:** Process-wrapper lines ("No files changed", "No commit/push", "No decision-log update",
> "Proceed to …") are omitted (DEC-030 Q3). The text is otherwise verbatim.

---

## DEC-061 — F19-08 — Generated credentials

- **Status:** CURRENT (finding split — provisioning half governed by DEC-046; output half deferred — §16 Amendment Gate)
- **Source:** §19 owner disposition review; owner message for F19-08 (2026-09-23).
- **Related:** §19.5.3 (D19-08), §19.14, §19.19, §19.21.2, §19.22; register §5A

```text
F19-08 — Owner disposition
DEFERRED TO ANOTHER GATE — §16 gate, with F19-05/OD19-04 routing for the credential-output surface
I would split the finding exactly as you did. Half 1 is no longer really an unresolved finding: R16j and R16c establish the current architectural rule and the available Local Root Operator provisioning path. The unresolved issue is half 2: what happens when a declared Operation itself produces new credential material in its output.
That distinction keeps us from reopening the already-settled provisioning rule.
F08a — Separate the two surfaces
F19-08 MUST be treated as two distinct architectural questions: (1) whether SCC or an Integration may provision generated credential material into K6 through an SCC request path, and (2) whether an Operation that creates credential material may expose that material through K6 output to K4 or another SCC component.
F08b — Provisioning path is already constrained
The first question is governed by R16j and R16c: no SCC- or Integration-generated credential provisioning path exists in v1, and credential provisioning is a Local Root Operator lifecycle act unless a higher-authority architecture establishes an authorized provisioning path consistent with §16.9 and the credential-custody rules.
So we don't need another decision on whether the current request path can carry credentials into K6. It cannot.
F08c — Generated credential output remains unresolved
The second question remains OPEN. The existing locked rules do not establish whether credential material newly created or returned by a declared Operation is classified, scrubbed, transformed, or otherwise prevented from reaching K4/K5 through the Operation result path.
This is the actual remaining architectural question.
F08d — Route the output question to the existing gate
Resolution of the generated-credential output question MUST occur through the applicable §16 gate and MUST account for the F19-05/OD19-04 analysis concerning credential-material entry into K4, together with X-24, X-26, the declared exposure modes, and the applicable K5 custody boundary.
This avoids creating another OD when the relevant work is already routed.
F08e — Do not treat R16j as solving output exposure
R16j resolves neither the classification nor the exposure handling of credential material newly produced by an Operation. The prohibition on entering the K6 credential lifecycle without an authorized provisioning path does not by itself determine whether such material may appear in an Operation result.
Important distinction: credential lifecycle custody ≠ output-data handling.
F08f — No automatic authorization
F19-08 does not authorize SCC- or Integration-generated credential provisioning, credential-bearing Operation output, or any new credential-capture mechanism. Until the applicable architecture establishes an authorized path, such functionality remains unavailable.
Owner decision
F19-08 — DEFERRED TO ANOTHER GATE
More precisely:

* Provisioning half: resolved by existing owner decisions R16j/R16c as a v1 architectural restriction.
* Generated-output half: deferred to the §16 gate, with the existing F19-05 / OD19-04 credential-entry analysis applied.
* No new OD needed.

Carry forward:
F08a
F19-08 MUST be treated as two distinct architectural questions: (1) whether SCC or an Integration may provision generated credential material into K6 through an SCC request path, and (2) whether an Operation that creates credential material may expose that material through K6 output to K4 or another SCC component.
F08b
The first question is governed by R16j and R16c: no SCC- or Integration-generated credential provisioning path exists in v1, and credential provisioning is a Local Root Operator lifecycle act unless a higher-authority architecture establishes an authorized provisioning path consistent with §16.9 and the credential-custody rules.
F08c
The second question remains OPEN. The existing locked rules do not establish whether credential material newly created or returned by a declared Operation is classified, scrubbed, transformed, or otherwise prevented from reaching K4/K5 through the Operation result path.
F08d
Resolution of the generated-credential output question MUST occur through the applicable §16 gate and MUST account for the F19-05/OD19-04 analysis concerning credential-material entry into K4, together with X-24, X-26, the declared exposure modes, and the applicable K5 custody boundary.
F08e
R16j resolves neither the classification nor the exposure handling of credential material newly produced by an Operation. The prohibition on entering the K6 credential lifecycle without an authorized provisioning path does not by itself determine whether such material may appear in an Operation result.
F08f
F19-08 does not authorize SCC- or Integration-generated credential provisioning, credential-bearing Operation output, or any new credential-capture mechanism. Until the applicable architecture establishes an authorized path, such functionality remains unavailable.
One useful cleanup
I would not call the entire F19-08 "resolved", because that would lose the output-exposure half. But I also would not leave the original sentence intact as though §16.9 alone describes the entire problem.
So the final change set should record it as a split finding with one half resolved by existing decisions and one half deferred.
```

> **Transcription note:** Process-wrapper lines ("No files changed", "No commit/push", "No decision-log update",
> "Proceed to …") are omitted (DEC-030 Q3). The text is otherwise verbatim.

---

## DEC-062 — F19-09 — K7 restore and post-backup authorization changes

- **Status:** CURRENT (finding deferred — §22 / recovery gate; TQ-08; ODF-18-07)
- **Source:** §19 owner disposition review; owner message for F19-09 (2026-09-23).
- **Related:** §19.5.3 (D19-09), §19.16, §19.22; register §5A, TQ-08

```text
F19-09 — Owner disposition
DEFERRED TO ANOTHER GATE — §22 / recovery gate, with TQ-08 and ODF-18-07
I would not acknowledge the original finding verbatim, because its statement that "no revocation record exists outside K7" is too broad. I also would not reject the underlying issue: the architecture still has an unresolved recovery problem concerning how post-backup authorization changes are established and how an unannounced rollback is detected.
So the clean classification is deferred to another gate, with the finding itself narrowed to what is actually established.
F09a — Narrow the finding
F19-09 concerns the recovery problem that an authorized restoration of SD-K7 to an earlier backup point may omit authoritative Principal, Role Membership, Grant, or other authorization-state changes made after that backup point. The finding does not assert that all revocation information exists only in K7, and does not apply to revocation or state represented authoritatively in other domains such as K11.
This fixes the overbroad original sentence.
F09b — Preserve the existing recovery requirement
R17c and R17f remain authoritative for authorized K7 restore: restored authorization state MUST NOT be treated as current merely because it was present in the backup, and post-backup authorization changes MUST be dispositioned before ordinary authorization-dependent operation resumes.
F09c — Source of post-backup evidence remains open
The authoritative source or combination of sources by which recovery establishes post-backup authorization changes remains OPEN. §22 MUST establish a sufficient recovery basis, whether through off-host evidence, another authoritative source, or another explicitly defined mechanism, before ordinary authorization-dependent operation may resume.
This deliberately does not assume ODF-18-07 will be the answer.
F09d — Authorized restore vs. undetected rollback
F19-09 distinguishes an authorized K7 restore governed by R17b–R17f from an unannounced replacement, rollback, truncation, or other alteration of K7 that K4 is not informed has occurred. The latter detection problem remains separately governed by TQ-08, §18 SR-16, ODF-18-07, and the applicable recovery/tamper-evidence design.
That distinction is important. R17 cannot magically trigger if SCC doesn't know a rollback happened.
F09e — No resurrection through recovery
Recovery design MUST NOT permit an earlier K7 state to silently resurrect authorization state that was revoked after the backup point. The exact detection, evidence, reconciliation, and disposition mechanisms remain subject to §22 and the applicable conditional §18 requirements.
F09f — Existing external evidence remains partial
The existence of K11 state, K8 journal records, or platform-side state does not by itself establish a complete source of post-backup K7 authorization changes. Those sources MAY provide evidence relevant to recovery, but their sufficiency remains subject to the applicable recovery design.
This avoids overclaiming what K8 or the platform can reconstruct.
F09g — Not a §15–§17 defect
F19-09 is not classified as a defect in locked §15–§17. The recovery requirement is established by the applicable recovery architecture and conditional §18 requirements, while the mechanisms needed to satisfy it remain open to the recovery gate.
That also keeps it out of the special criterion-3 issue that we're tracking for F19-05/F19-06.
Owner decision
F19-09 — DEFERRED TO ANOTHER GATE
Carry forward:
F09a
F19-09 concerns the recovery problem that an authorized restoration of SD-K7 to an earlier backup point may omit authoritative Principal, Role Membership, Grant, or other authorization-state changes made after that backup point. The finding does not assert that all revocation information exists only in K7, and does not apply to revocation or state represented authoritatively in other domains such as K11.
F09b
R17c and R17f remain authoritative for authorized K7 restore: restored authorization state MUST NOT be treated as current merely because it was present in the backup, and post-backup authorization changes MUST be dispositioned before ordinary authorization-dependent operation resumes.
F09c
The authoritative source or combination of sources by which recovery establishes post-backup authorization changes remains OPEN. §22 MUST establish a sufficient recovery basis, whether through off-host evidence, another authoritative source, or another explicitly defined mechanism, before ordinary authorization-dependent operation may resume.
F09d
F19-09 distinguishes an authorized K7 restore governed by R17b–R17f from an unannounced replacement, rollback, truncation, or other alteration of K7 that K4 is not informed has occurred. The latter detection problem remains separately governed by TQ-08, §18 SR-16, ODF-18-07, and the applicable recovery/tamper-evidence design.
F09e
Recovery design MUST NOT permit an earlier K7 state to silently resurrect authorization state that was revoked after the backup point. The exact detection, evidence, reconciliation, and disposition mechanisms remain subject to §22 and the applicable conditional §18 requirements.
F09f
The existence of K11 state, K8 journal records, or platform-side state does not by itself establish a complete source of post-backup K7 authorization changes. Those sources MAY provide evidence relevant to recovery, but their sufficiency remains subject to the applicable recovery design.
F09g
F19-09 is not classified as a defect in locked §15–§17. The recovery requirement is established by the applicable recovery architecture and conditional §18 requirements, while the mechanisms needed to satisfy it remain open to the recovery gate.
Change-set notes

* Replace/narrow the original D19-09 wording; do not preserve the inaccurate "no revocation record exists outside K7" formulation.
* §19 should point to §22 / recovery, TQ-08, and ODF-18-07.
* Do not create another OD for the evidence-source question; F09c routes it to the recovery gate.
* Do not treat K8, K11, or platform state as a complete substitute for missing K7 authorization history.
* No criterion-3 treatment is required merely from this finding, because it is not a finding against locked §15–§17.

And this one illustrates the progress you were talking about: we're now mostly pruning inaccurate findings and routing unresolved mechanics to the gate that already owns them. That's much cleaner than where we started.
```

> **Transcription note:** Process-wrapper lines ("No files changed", "No commit/push", "No decision-log update",
> "Proceed to …") are omitted (DEC-030 Q3). The text is otherwise verbatim.

---

## DEC-063 — Post-lock §19 resolution route

- **Status:** CURRENT (adopted)
- **Source:** Owner message "Owner decisions for Part 8", item 7 (2026-09-23).
- **Related:** §19.21, §19.26

```text
7. Post-lock resolution route

APPROVE CS-1.

This is important enough that I would absolutely not leave it as G-1.

Use:

DEC-063 — Post-lock §19 resolution route

with the CS-1 text:

When an OD19 item, Q19 item or deferred finding is resolved after §19 is locked, the resolution is recorded as a new DEC entry. That entry identifies each §19 passage it changes, and §19 is amended to match it. No other route changes locked §19 text.

This solves the problem you identified during OD19-06.

It also means the final architecture has an explicit mechanism for the inevitable situation where §21, §22, §20, P2, CyberPanel K2, or the future §16 gate resolves something that §19 currently leaves open.
```

---

## DEC-064 — §19 Change-Set Reconciliation Decisions

- **Status:** CURRENT (adopted)
- **Source:** Owner message "Owner decisions for Part 8" (items 1–6, 8–13 and the Part 7 correction) and owner message "§C-1 … §C-4" (2026-09-23).
- **Related:** §19 header, §19.12 (Plans), §19.13.1, §19.15, §19.16, §19.21, §19.21.1, §19.25; architecture index; open register (status vocabulary, §5A, §5B, §8)

```text
Owner decisions for Part 8
1. §19 status wording

APPROVE the alternative:

CANDIDATE — OWNER DISPOSITIONS RECORDED — NOT LOCKED

Reason: the review has in fact completed the owner-disposition pass. Keeping "OWNER REVIEW REQUIRED" would now be inaccurate. NOT LOCKED must remain.

Use the same status in:

§19 header
architecture index
register §5A
§8 gate table
§19.25
2. Decision-log structure

APPROVE, with one qualification:

One DEC per disposition item: DEC-031 through DEC-062.
Use the proposed status categories.
Owner wording is reproduced verbatim.
Remove only process-wrapper language as specified.
PD19-01 through PD19-16 must be extracted from the actual transcript, not reconstructed from the compacted summary.
DEC-053 must contain the corrected R03e wording using OD19-03.
No DEC entry gets LOCKED.

One additional rule:

The decision log records the owner decision; it does not itself amend or lock §15–§17.

That keeps Category 2 authority distinct from locked architecture.

3. Duplication of owner text in §19

APPROVE pointers rather than duplicating the entire owner text wherever possible.

I would not put dozens of long verbatim decision blocks throughout §19. That creates a maintenance problem and risks having two copies drift.

Instead:

§19 contains the resulting normative classification/requirement necessary for §19 itself.
Each such passage carries [DEC-0xx].
The decision log is the authoritative record of the complete owner wording.
Where a full R-text is itself the exact §19 requirement, it can be reproduced there, but this should be deliberate rather than automatic.

So Part 1's proposed extensive ⟦R...⟧ duplication should be reduced to the minimum necessary §19 text plus DEC pointers.

This also makes the authority statement cleaner.

4. Section-number corrections

APPROVE.

The corrections are valid:

Retention rows → §19.12, not §19.14.
Interim credential-bearing file.replace authoring rule → new §19.13.1.

The latter is appropriate because the rule needs an actual normative home rather than existing only indirectly in §19.23.

5. Criterion 3

CHOOSE option (iii): leave criterion 3 unsatisfied. Do not manufacture KF entries.

Do not override F05d merely to make the gate pass.

The criterion currently says:

F19-05 and F19-06 are recorded as known findings in the index, if the owner agrees they are findings.

We have agreed they are findings, but we also explicitly decided:

F19-05 is not added to the known-findings index while OD19-04 remains open.
F19-06's index treatment was deliberately left for reconciliation.

Therefore the honest state is:

Criterion 3 — NOT SATISFIED.

Do not amend criterion 3 merely to obtain a PASS.

This is exactly the kind of situation where the gate should accurately report the current architecture rather than bend its criterion.

6. Owning gates / Q19 prefix / §16 gate

This needs more care.

Q19 prefix

APPROVE Q19-01 through Q19-04.

They are clearly §19-owned open questions and the prefix distinguishes them from OD19 items.

Formal §16 gate

APPROVE registering a named future gate:

§16 Amendment Gate — NOT SCHEDULED

It should be a named architectural gate, not an implementation gate and not an assertion that §16 is being amended now.

Its purpose is simply to provide a stable owner for the already-identified possible §16 changes.

Part 5 then points to that gate.

OD19-02 / OD19-03

For these, the answer is different.

Their policy/existence decisions belong to the owner, not to a nonexistent technical gate. We should not invent a technical gate merely to satisfy criterion 5.

Therefore:

OD19-02 → §19 Owner Decision Gate
OD19-03 → §19 Owner Decision Gate
after §19 locks, resolution enters through CS-1/DEC-063.
Q19-01

Same treatment:

§19 Owner Decision Gate, coordinated with the applicable §22/credential-custody design as needed.

Q19-03

I would not invent an owner or gate for this yet. It is a scope-definition question arising from R20a.

Use:

§19 Owner Decision Gate, coordinated with §20 as applicable

That accurately preserves R20a rather than pretending §20 owns the definition.

Q19-04

The existing phrase:

"Applicable §17/K4 architecture"

is acceptable as the owning architecture, but for criterion purposes it should be named explicitly as:

§17/K4 Architecture Gate

not a new §17 amendment gate. §17 remains locked.
```

Item 7 of this message is recorded in DEC-063.

```text
8. Three pieces of candidate text without an owner disposition

These should not be silently accepted.

§19.15 orphaned-state "and marked"

REMOVE the unsupported "and marked" language.

We explicitly removed reporting/marking implications from R16h.

§19.16 item 3

APPROVE as LOCKED-DERIVED, provided the cited LC-02/LC-03 text actually supports exactly the stated restriction:

Recovery must never make K8 writable by C, or K7 readable by W or I.

This is not a new owner decision; it is a restatement of existing locked access boundaries.

§19.12 Plans row

KEEP, but mark it explicitly as a general retention rule rather than a decided Plan-specific retention period.

The proposed wording is appropriate:

Governed by the general rule in R9a (first sentence) and R9b. No Plan-specific retention has been decided.

No new decision is needed.

9. F19-07 register status

Add REJECTED (as a finding) as a legitimate status.

Do not disguise a rejected finding as ADDRESSED.

That distinction matters:

ADDRESSED = the issue was an actual tracked matter that has been resolved.
REJECTED (as a finding) = the review determined that the alleged finding is not a defect against locked architecture.

Use:

F19-07 — REJECTED (as a finding) — DEC-060; OD19-05 remains OPEN.

Update the register's status vocabulary accordingly.

10. CHANGE-015 / CHANGE-023
CHANGE-015

Default: leave unchanged.

Do not declare the CHANGE-015 item addressed merely because R5a/R5b clarify the §19 behavior. The change itself has not been formally reconciled/closed.

So Part 8's default is correct.

CHANGE-023

Leave unchanged.

The discrepancy between the register and §19.22 should remain explicitly unresolved rather than silently selecting an owner.

The change set should preserve:

register: classification OPEN — §19
§19.22: §21 / owner

and perhaps add a pointer noting the discrepancy, without deciding it.

11. ANN-33

DEFER ANN-33. Do not add it in this change set.

The baseline itself is locked/current foundational material. Although the annotation appears useful, it is not necessary to complete the §19 owner-disposition reconciliation.

More importantly, adding it introduces another baseline change into a change set whose purpose is to reconcile §19.

So:

ANN-33 remains deferred.

No baseline change.

12. Criterion-4 readings

APPROVE the explicit readings, with no change to criterion 4.

The two points should be recorded as the rationale supporting the statement:

No violation identified.

Specifically:

R5b is the owner's interpretation of the interaction between A-05 Fixed System Authority and the audit-record requirement.
R11e applies X-29's existing K8 refusal consequence to inability to preserve required records.

But do not rewrite §17 or §16 to accommodate them.

13. Git

The local branch is fine as the eventual destination, but the proposed change set must first be finalized.

One more important correction to Part 7

With the decisions above, I would update the gate evaluation as follows:

Criterion	Result
1 — All PDs dispositioned	SATISFIED
2 — Every OD decided/deferred to named gate	SATISFIED after registering/naming the owner and future technical gates above
3 — Required findings indexed	NOT SATISFIED
4 — No authority widening / §15–§17 contradiction	NO VIOLATION IDENTIFIED
5 — Every deferral has named owner	SATISFIED after the gate assignments above

Therefore §19 remains NOT LOCKABLE, solely because criterion 3 is intentionally unsatisfied.

That's a much cleaner result than leaving criteria 2 and 5 conditionally unsatisfied because we hadn't named the gates.

And crucially, we are not changing criterion 3 to make the gate pass.

Final owner disposition of the proposed change set

The resulting change set should therefore include:

DEC-031–DEC-062
DEC-063 for CS-1
CANDIDATE — OWNER DISPOSITIONS RECORDED — NOT LOCKED
reduced duplication in §19 with DEC pointers
§19.12 correction
§19.13.1 interim rule
F19-07 register status explicitly REJECTED (as a finding)
no KF additions yet
formal §16 Amendment Gate — NOT SCHEDULED
named §19 Owner Decision Gate / §17-K4 Architecture Gate as above
ANN-33 deferred
unsupported orphan "marked" language removed
Plans row retained with its stated limitation
criterion 3 remains NOT SATISFIED
criteria 2 and 5 become SATISFIED
§19 remains NOT LOCKABLE
no §16 changes
no §15–§17 changes
no implementation authorization
no commit/push/PR action

One thing I would have Claude do before application: regenerate the entire proposed change set after these decisions and run a final internal consistency check against DEC-031 through DEC-063, especially checking that no §19 passage accidentally claims that an OPEN item has already been resolved.

At that point, I would expect the next review to be a change-set verification, not another architecture-design session.
```

Second source message (§C-1 … §C-4):

```text
§C-1: APPROVE option (a). Add DEC-064 as “§19 Change-Set Reconciliation Decisions.” Do not widen DEC-063. DEC-031–062 remain the owner disposition review; DEC-063 remains the post-lock resolution route; DEC-064 records the subsequent change-set reconciliation decisions. Update the relevant DEC range references to DEC-064.

§C-2: APPROVE the narrower reading. Criterion 5 applies to explicit §19 deferrals enumerated in §19.21–§19.22. It does not require every “applicable architecture/contract/design” dependency phrase inside an owner decision to have an independently registered gate. Add that clarification to the criterion-5 evaluation. Leave CHANGE-023 unresolved.

§C-3: APPROVE option (a). Reduce the orphaned-state row to the behavior actually supported by T-28. Remove “Retained, never silently deleted.” Do not create a new owner decision for retention/disposition.

§C-4: APPROVE the proposed transcript verification procedure. Before applying anything, verify PD19-01–PD19-16 and every verbatim insertion against the actual transcript. If any discrepancy exists, stop and report it; do not silently correct or reconstruct owner wording.
```

> **Transcription note (session process):** The following review-session process lines are omitted; they
> governed only the review session and are not owner decisions: "No push, PR update, merge, or application authorization yet."; "I would authorize Claude to revise the proposed change set according to the decisions above, but not apply it yet."; "After those changes, regenerate the final change set and perform the final consistency check. Do not edit, commit, push, open/update a PR, or otherwise apply the change set yet.".

> **Index note (not owner wording):** DEC-064 records reconciliation decisions. It does not itself lock §19,
> and it does not amend or lock §15–§17.

---

## DEC-065 — §19 Pre-Lock Corrections (J-1 … J-12)

- **Status:** CURRENT (adopted)
- **Source:** Owner message approving the proposed DEC-065 owner-decision package (2026-09-24).
- **Related:** §19.2, §19.5.3, §19.6, §19.7, §19.8, §19.9, §19.10, §19.11.2, §19.21.1, §19.22, §19.23, §19.25; open register (§5A, §8, TQ-09); architecture index

```text
I have reviewed the proposed DEC-065 Owner-Decision Package.

APPROVED OWNER DISPOSITION:

Create DEC-065 and apply the following decisions exactly.

==================================================
J-1 — GATE ACCOUNTING
==================================================

D65-1 APPROVED.

The §19.22 format rows shall explicitly name the existing gates as follows:

- SD-K11R and SD-K11H format:
  §22, consistent with DEC-049 R19j.

- SD-K6P format:
  §22 for lifecycle/storage mechanics, and the §16 Amendment Gate where the proposed change affects K6 behavior or execution semantics.

- SD-K2 format:
  CyberPanel K2 gate for platform-specific K2 concerns, with P2 for assertion/protocol and signing-key format concerns where applicable.

Do not invent any new gate.

D65-2 APPROVED.

The Job-state row shall explicitly state that its owner is assigned by locked §16.15 Q-6:

  §8 amendment (CHANGE-007)

and that:

  - no §8 gate is currently scheduled;
  - this is not a §19-created deferral;
  - §19 does not reassign or redefine the ownership established by locked §16.

Under DEC-064's existing interpretation, this item is outside criterion 5's §19-deferral accounting.

Do NOT change the text of criterion 5.

==================================================
J-2 — TQ-09
==================================================

D65-3 APPROVED.

Add Q19-05 to §19.21.1.

Use this substance:

"K8 capacity isolation and volume displacement (TQ-09; SR-17, T-18-11, TF-18-09 — conditional §18). R11e prevents eviction of required records and refuses new requests. It does not establish capacity isolation or protection of unexported records."

The item remains OPEN.

Owner:
§19 Owner Decision Gate.

Important:

- Do NOT treat R11e as resolving TQ-09.
- Do NOT adopt a capacity-isolation mechanism.
- Do NOT specify quotas, partitions, filesystem layout, reservations, or other implementation.
- Do NOT assign the item to §22 merely because a future host/storage mechanism might ultimately be implemented there.
- If a future implementation decision establishes a §22 or §12 dependency, that can be recorded later through the normal decision/change route.

D65-4 APPROVED.

Also add Q19-06 for SR-14.

SR-14 is:

"K8 SHOULD retain the full approval evidence"

and is currently downstream to §19.

Q19-06 should explicitly record that the requirement remains OPEN and that DEC-039 R9h does not resolve it.

Use wording along these lines:

"Full approval-evidence retention (SR-14; conditional §18). DEC-039 R9h does not establish the full retention requirement. The retention scope, duration, and relationship to existing K7/K8 retention rules remain OPEN."

Owner:
§19 Owner Decision Gate.

Do not create a retention requirement merely by recording this question.

==================================================
CRITERION 3
==================================================

D65-5 APPROVED.

Make NO change to criterion 3.

It remains:

NOT SATISFIED.

Do not add F19-05 or F19-06 to the Known Findings table.

Do not alter the criterion merely to obtain PASS.

Do not resolve OD19-03 or OD19-04 through this change set.

Do not change DEC-058 or DEC-059.

==================================================
MINOR FINDINGS
==================================================

D65-6 APPROVED.

Correct J-3, J-4, J-5 and J-7 narrowly and only to restore fidelity to the existing decisions and locked architecture.

J-3:
Correct the DC-06 Writers/Readers wording so it does not imply that DEC-037 authorized arbitrary persistence or a finalized delivery mechanism.

Retain the actual open state of R7c/R7e.

Do not invent a write path.

J-4:
Replace the §19.8 item 3 wording that currently says:

"Any durable state an Integration needs is held by K4 in K7 (DC-06)"

with wording limited to the actual DEC-037 scope:
Integration-specific configuration/state covered by R7a/R7f.

Do not broaden DC-06 into a universal Integration persistence rule.

J-5:
Do not identify K4 as the settled owner of DC-18.

The owner remains OPEN under DEC-051 R01a.

J-7:
Correct the SD-K8 access description to acknowledge K6's required read/use relationship with K8 established by locked §16.11 and X-31.

Do not change the underlying K8 access-control model.

==================================================
J-6 — OWNER TERMINOLOGY
==================================================

D65-7 APPROVED WITH THE FOLLOWING CLARIFICATION:

Do NOT redefine DEC-031 R4.

Instead, clarify the affected §19 table cells so that "owner" is not incorrectly represented as an SCC-component owner where the referenced class is owned by a non-SCC authority.

For K11 classes and other explicitly non-SCC-owned classes, use terminology that distinguishes:

- SCC authoritative storage owner/component, from
- the external authority responsible for the corresponding class.

Do not silently change the ownership model.

Do not create a new SCC component.

Do not change K11 authority.

Do not amend §15 or §16.

If the existing table cannot express this distinction cleanly without changing the meaning of R4, STOP and report the exact ambiguity rather than inventing terminology.

==================================================
J-8 / J-9 / J-11 / J-12
==================================================

D65-8 APPROVED.

Apply the following documentation corrections:

J-8:
Change "stage 17" to "layer 17" where referring to §16.4.1 validation.

J-9:
Correct the stale §19.2 cross-reference currently pointing to §19.20.

The reference must point to the actual intended §19 content.

Do not infer new security requirements from the correction.

J-11:
Correct the D19-05 description so it does not state as settled fact that there is a conflict with T-18 when F05a leaves that interpretation open.

Preserve the actual open/disputed status.

J-12:
Update the OD19-03 subject so it reflects the current disposition without changing OD19-03's substantive status.

Do NOT alter Q-2 or OQ-5 merely for cosmetic reasons.

==================================================
J-10
==================================================

NO CHANGE REQUIRED.

Do not add TH-31 or R11g solely for traceability.

They remain represented by their existing decision-log records.

==================================================
DEC-065 RECORD
==================================================

Create DEC-065 in the decision log.

The decision must record:

- J-1 D65-1 and D65-2;
- J-2 D65-3 and D65-4;
- Criterion 3 D65-5;
- J-3/J-4/J-5/J-7 D65-6;
- J-6 D65-7;
- J-8/J-9/J-11/J-12 D65-8;
- J-10 no-change disposition.

DEC-065 must state that it is a documentation/owner-disposition decision only.

It must NOT lock §19.

It must NOT authorize implementation.

It must NOT amend §15, §16, or §17.
```

> **Transcription note (session process):** The owner message's CHANGE-SET DISCIPLINE, IMPORTANT, post-edit
> verification and report sections are omitted; they governed only this correction pass and are not owner decisions.

> **Index note (not owner wording):** DEC-065 is a documentation/owner-disposition decision. It does not lock §19, does
> not authorize implementation, and does not amend §15, §16 or §17. D65-7 was not applied to §19: its conditional STOP
> was triggered because §19.7 cannot express the distinction for DC-01 and DC-02 without changing the meaning of
> DEC-031 R1/R4 (reported to the owner).

---

## DEC-066 — K11-held SCC data ownership under R1/R4

- **Status:** CURRENT (adopted — DC-01/DC-02 owner OPEN)
- **Source:** Owner approval message for DEC-066 (2026-09-24), adopting D66-A … D66-H verbatim from the proposed DEC-066 package.
- **Related:** §19.7, §19.22, §19.23, §19.25; open register OQ-6; DEC-031 (R1, R4); DEC-065 (D65-7)

```text
I APPROVE DEC-066 EXACTLY AS DRAFTED.

Adopt D66-A through D66-H verbatim as the owner decision.

Create:

DEC-066 — K11-held SCC data ownership under R1/R4

with the exact owner wording provided in the proposed DEC-066 package.

The substantive owner decision is:

- DC-01 and DC-02 remain SCC data classes.
- Their §19/R4 owner remains OPEN.
- The unresolved ownership assignment depends on the Recovery gate / §22 determination under locked §15.18 OQ-6.
- The eventual assignment must satisfy R1 and R4.
- No owner is assigned now.
- Do not pre-decide K9, K11, K6, an SCC installer/service, another SCC component, the Local Root Operator, or an external/root-controlled mechanism as the eventual R4 owner.
- DC-01 remains authoritative in SD-K11R.
- DC-02 remains authoritative in SD-K11H.
- Root-only K11 write authority and the K11 trust boundary remain unchanged.
- "Owned by root" remains an OS/filesystem authority statement and is not the §19 R4 owner.
- DC-20 through DC-24 receive only the approved terminology clarification and are not reclassified.
- R1 and R4 remain unchanged.
- DEC-031 remains unchanged.
- §15, §16 and §17 remain unchanged.
- No implementation is authorized.
- DEC-029 remains standing.

Apply the exact §19, decision-log, README, and register changes in the proposed package:

1. §19 header/source metadata → DEC-066
2. §19.7 DC-01 owner → OPEN pending Recovery gate / §22 OQ-6
3. §19.7 DC-02 owner → OPEN pending Recovery gate / §22 OQ-6
4. §19.7 note clarifying DC-20…DC-24 owner terminology
5. §19.22 new R4-owner deferral row
6. §19.23 DEC-066 row
7. §19.25 references updated to include DEC-066 only; criterion text remains unchanged
8. README DEC range → DEC-066
9. decision-log index → DEC-066
10. decision-log DEC-066 entry → exact approved owner wording
11. register OQ-6 pointer → include the §19 DC-01/DC-02 dependency and DEC-066

DEC-065 must remain unchanged and historically accurate.

Do NOT reopen or amend DEC-065.

Do NOT change:

- R1
- R4
- DEC-031
- §15
- §16
- §17
- §18
- §19.24 criterion text
- §19.26 / CS-1
- OD19-01…OD19-07
- Q19-01…Q19-06
- F19-05…F19-09
- Known Findings
- ANN-33
- CHANGE-015
- CHANGE-023
- implementation authorization
```

Adopted decision text (D66-A … D66-H, from the proposed DEC-066 package, adopted verbatim by the approval above):

```text
DEC-066 — K11-held SCC data ownership under R1/R4

D66-A  DC-01 (SCC release content) and DC-02 (host-local root configuration) remain SCC data
       classes. Their §19 R4 owner is OPEN: the SCC component responsible for their
       authoritative persistence has not been established. The assignment depends on locked
       §15.18 OQ-6 (Recovery gate / §22: K9's authority; key (re)provisioning for K2; installer
       placement of K11) and, for the approver anchor set held in K11, on §17.9 ("The mechanics
       belong to §22").

D66-B  This OPEN status does not waive R1 or R4.

D66-C  The eventual assignment MUST identify an SCC component responsible for authoritative
       persistence, consistent with R4, or return for an explicit owner decision if the resulting
       architecture uses a mechanism that does not fit R4. This decision does not pre-decide
       whether K9, an SCC installer or service, K11, another SCC component, or an external or
       root-controlled mechanism will be responsible.

D66-D  The authoritative storage domains remain: DC-01 → SD-K11R; DC-02 → SD-K11H.

D66-E  Root-only write authority (T-21; §15.3.2 "Owned by root; not writable by W, C, I") and
       K11's trust boundary are unchanged. "Owned by root" remains an OS/filesystem authority
       statement and is not the §19 R4 owner.

D66-F  For DC-20 … DC-24, the §19.7 "Owner" entries name the external party or holding process.
       They are not R4 SCC-component ownership claims, because these classes are outside SCC
       authoritative persistence: SD-PLAT and SD-HOST are not SCC; DC-22 is held off-host or in an
       operator-managed location outside SCC components (DEC-043 R13c, R13e); DC-23 is off-host;
       DC-24 is transient. Their classifications are unchanged.

D66-G  This decision does not amend §15, §16, §17, R1, R4 or DEC-031. It supplements DEC-065
       D65-7, which remains recorded as not applied; DEC-065 is unchanged.

D66-H  This decision does not authorize implementation. DEC-029 remains standing.
```

> **Transcription note (session process):** The approval message's pre-edit checks, commit/push/PR instructions,
> post-edit verification and report sections are omitted; they governed only this change and are not owner decisions.

> **Index note (not owner wording):** DEC-066 supplements DEC-065 D65-7; DEC-065 is unchanged. DEC-066 does not lock
> §19, does not authorize implementation, and does not amend §15–§17, R1, R4 or DEC-031.

---

## DEC-067 — F19-06 — Known-findings index treatment

- **Status:** CURRENT (adopted — F19-06 indexed as KF-11 and OPEN; OD19-03 OPEN)
- **Source:** Owner decision message for F19-06 index treatment (2026-09-24): INDEX; D65-5 treatment A2 (prospective).
- **Related:** §19.24 (criterion 3), §19.5.3 (D19-06), §19.23; architecture index (KF-11); DEC-058 (F05d); DEC-059 (F06a, F06b, F06c); DEC-064 item 5; DEC-065 (D65-5)

```text
============================================================
OWNER DECISION
============================================================

F19-06 index treatment:

**INDEX F19-06.**

D65-5 treatment:

**A2 — The owner prospectively determines that the DEC-065 D65-5 instruction not to add F19-06 to the Known Findings table no longer applies to F19-06, effective from this decision.**

Do NOT reinterpret D65-5 historically.

Do NOT claim that D65-5 was originally scoped to the DEC-065 change set.

Do NOT edit DEC-065.

Do NOT use the word "supersedes" as though the repository has an established DEC-to-DEC supersession mechanism. The decision is a new, explicit prospective owner determination addressing the application of D65-5 to F19-06.

The D65-5 treatment of F19-05 remains unchanged.

All other D65-5 instructions remain unchanged.

============================================================
SCOPE OF THIS DECISION
============================================================

The decision is narrowly limited to F19-06's treatment in the Known Findings Against Locked Text index.

The decision MUST establish:

1. F19-06 is recorded in the architecture index under "Known Findings Against Locked Text."

2. The indexed finding is limited to DEC-059 F06a:
   - the absence of an established maximum approval-validity horizon; and
   - the mechanism for satisfying approval-evidence requirements following K8 lifetime loss or reinitialization.

3. The nonce-retention consequence governed by R11b and R03b is NOT part of the indexed finding.

4. The indexed finding remains OPEN.

5. Indexing F19-06 does NOT determine whether any part of the finding constitutes a defect in the locked architecture.

6. F06b remains unchanged.

7. OD19-03 remains OPEN.

8. This decision does NOT determine:
   - whether a maximum approval-validity horizon exists;
   - what its value should be;
   - its enforcement point;
   - whether its absence constitutes a defect.

9. The K8-loss/reinitialization approval-evidence mechanism remains subject to §22 and the applicable §16 gate.

10. This decision does NOT decide that mechanism.

11. This decision does NOT amend §15, §16 or §17.

12. This decision does NOT resolve the §16 Amendment Gate.

13. F19-05 remains governed by DEC-058, including F05d, and DEC-064.

14. OD19-04 remains OPEN.

15. §19.24 Criterion 3 is NOT changed.

16. Criterion 3 remains NOT SATISFIED overall because F19-05 remains unresolved/unindexed.

17. §19 remains NOT LOCKED.

18. This decision does NOT authorize implementation.

19. DEC-029 remains in force.

20. DEC-058 and DEC-059 remain unchanged.

============================================================
D65-5 — REQUIRED OWNER WORDING
============================================================

Include a decision entry substantially equivalent to:

"DEC-065 D65-5 states: 'Do not add F19-05 or F19-06 to the Known Findings table.'

The owner prospectively determines that the D65-5 instruction not to add F19-06 to the Known Findings table no longer applies to F19-06, with effect from this decision.

This determination concerns F19-06 only. The instruction's application to F19-05 is unchanged, and F19-05 remains governed by DEC-058 F05d and DEC-064. The other D65-5 instructions are unaffected.

DEC-065 is unchanged and remains the historical record of the instruction as given."

Preserve the distinction between:
- DEC-065 as the historical record;
- this new DEC as the prospective owner decision.

Do not rewrite history.

============================================================
DOCUMENTATION SAFEGUARDS
============================================================

Keep the safeguards from IDX-A1 through IDX-A9 from the previously drafted candidate decision, tightened only as necessary for consistency.

At minimum preserve these concepts:

- F19-06 is indexed.
- F19-06 remains OPEN.
- indexing does not establish defect status.
- OD19-03 remains OPEN.
- the approval-horizon question remains unresolved.
- K8-loss/reinitialization remains subject to §22 / applicable §16 gate.
- no §16 amendment.
- no §22 design decision.
- F19-05 / OD19-04 remain untouched.
- Criterion 3 remains unchanged.
- §19 remains unlocked.
- no implementation authority is created.

These are documentation safeguards.

Do not claim they are independently mandatory source requirements unless the source explicitly says so.
```

Decision text (IDX-A1 … IDX-A9 from the candidate decision drafted for owner review, tightened for consistency with
scope items 1–20 above as the owner message permits; IDX-D65 in the owner's required D65-5 wording):

```text
F19-06 — Known-findings index treatment — Owner decision: INDEX (D65-5 treatment: A2, prospective)

IDX-A1  F19-06 is recorded in the architecture index under "Known Findings Against Locked Text" as
        KF-11. The indexed finding is limited to the scope stated in DEC-059 F06a: the absence of an
        established maximum approval-validity horizon, and the mechanism for satisfying
        approval-evidence requirements following K8 lifetime loss or reinitialization. The
        nonce-retention consequence governed by R11b and R03b is not part of the indexed finding.

IDX-A2  The indexed finding remains OPEN. Recording it in the index does not close it.

IDX-A3  Recording F19-06 in the index does not determine whether any part of it constitutes a
        defect in the locked architecture. DEC-059 F06b is unchanged.

IDX-A4  OD19-03 remains OPEN. This decision does not determine whether a maximum
        approval-validity horizon exists, its value, its authoritative enforcement point, or
        whether its absence constitutes a defect.

IDX-A5  The mechanism for satisfying approval-evidence requirements following K8 loss or
        reinitialization remains subject to §22 and the applicable §16 gate (DEC-059 F06c;
        DEC-048 R18d). This decision does not decide that mechanism or any §22 design.

IDX-A6  This decision does not amend §15, §16 or §17 and does not resolve the §16 Amendment Gate.

IDX-A7  F19-05 remains governed by DEC-058 (including F05d) and DEC-064. OD19-04 remains OPEN.

IDX-A8  §19.24 criterion 3 is unchanged. Criterion 3 remains NOT SATISFIED overall because F19-05
        remains unindexed. §19 remains NOT LOCKED. DEC-058 and DEC-059 are unchanged.

IDX-A9  This decision does not authorize implementation. DEC-029 remains standing.

IDX-D65 DEC-065 D65-5 states: "Do not add F19-05 or F19-06 to the Known Findings table."
        The owner prospectively determines that the D65-5 instruction not to add F19-06 to the
        Known Findings table no longer applies to F19-06, with effect from this decision.
        This determination concerns F19-06 only. The instruction's application to F19-05 is
        unchanged, and F19-05 remains governed by DEC-058 F05d and DEC-064. The other D65-5
        instructions are unaffected.
        DEC-065 is unchanged and remains the historical record of the instruction as given.
```

> **Factual basis (not owner wording):** F19-06 is an established finding in the decomposed form of DEC-059 F06a; the
> owner agreed it is a finding and left its index treatment for reconciliation (DEC-064 item 5). §19.5.3 D19-06 records
> the locked text concerned as §16.5, X-16 and §16.11. §19.24 criterion 3 names F19-06 for recording in the index if
> the owner agrees it is a finding.

> **Change-set implications (not owner wording):** README Known Findings table: KF-11 added (KF-01 … KF-10 and the
> preamble unchanged). README decision-log range, decision-log index and header note, and a §19.23 pointer row record
> DEC-067. Not changed: §15–§17 including their front matter (the §16 pointer "KF-04 to KF-09" is not updated), the
> open register (including its §1 range "KF-01 … KF-10" and the F19-06 row), §19.5.3, §19.24, §19.25, and DEC-058,
> DEC-059, DEC-064, DEC-065 and DEC-066.

> **Transcription note (session process):** The owner message's opening process lines and its KNOWN FINDING ROW,
> DO NOT TOUCH, DECISION LOG, DEC-065/DEC-066 INTEGRITY, README / INDEX, §19 STATUS, CHANGE-SET DISCIPLINE,
> IMPLEMENTATION, VALIDATION AFTER EDITING and FINAL REPORT sections are omitted; they governed only this change and
> are not recorded as owner decisions here.

> **Index note (not owner wording):** DEC-067 addresses the application of DEC-065 D65-5 to F19-06 prospectively;
> DEC-065 is unchanged. DEC-067 does not lock §19, does not authorize implementation, does not amend §15–§17, and
> does not resolve OD19-03, OD19-04, F19-05, §22 or the §16 Amendment Gate.

---

## DEC-068 — §16 Amendment Gate — Procedural framework

- **Status:** CURRENT (adopted — procedural; gate NOT SCHEDULED)
- **Source:** Owner approval message for DEC-068 (2026-09-24), adopting D68-A … D68-N.
- **Related:** DEC-064 item 6; §19.21.2; register §5B and §8; DEC-023; DEC-030; DEC-063; DEC-054; DEC-058

```text
APPLY AUTHORIZATION — DEC-068

DEC-068 revision 2 is APPROVED FOR ADOPTION exactly as presented.

Apply DEC-068 verbatim.

Do not reinterpret, rewrite, improve, shorten, expand, or reconcile any D68 provision.

Adopt:

DEC-068 — §16 Amendment Gate — Procedural framework

with D68-A through D68-N exactly as in the approved candidate.
```

Decision text (D68-A … D68-N, adopted verbatim by the approval above):

```text
D68-A  Gate identity. The §16 Amendment Gate registered by DEC-064 item 6 is a named
       architectural gate, not an implementation gate. This decision does not re-register it
       and does not change DEC-064.

D68-B  Convening authority. The architecture owner convenes the §16 Amendment Gate. This
       decision does not define who the architecture owner is, how that authority is obtained,
       or succession.

D68-C  Initiation. The gate is convened by an owner decision recorded in the decision log that
       (1) states that the §16 Amendment Gate is convened and (2) names the registered item or
       items admitted to that convening. On that record the gate's status changes from
       NOT SCHEDULED to OPEN. No other request mechanism is established.

D68-D  Agenda. The agenda of a convening consists only of items that the current record assigns
       to the §16 Amendment Gate (§19.21.2 / register §5B, and §19.22 entries that name the
       gate) and that the convening decision admits. A convening may admit one or more such
       items. Assigning a new item to the gate requires a separate owner decision; this decision
       assigns none.

D68-E  Independent consideration. Registered items may be admitted and heard independently of
       one another, unless locked architecture or an owner decision expressly requires joint
       consideration. Batching is not required.

D68-F  OD19-04 and F19-05. OD19-04 (§19.21.2 row 6) and the interpretation of F19-05 (§19.21.2
       row 9) may be admitted and heard, as a procedural matter, independently of unrelated
       registered items. Admission does not decide OD19-04; does not choose between a permanent
       prohibition and a §16 composition path; does not decide whether any §16 amendment is
       required; does not determine F19-05's interpretation; and does not establish whether
       OD19-04's direction is chosen before or during the gate. DEC-058 F05a (interpretation
       determined through OD19-04 and the applicable §16 gate) and the content requirements of
       DEC-058 F05b and DEC-054 R04d remain in full effect.

D68-G  Decision authority. The architecture owner records the gate's outcome for each admitted
       item. This decision establishes no quorum, vote, approver role, reviewer, committee, or
       authorization through K4 or §17.

D68-H  Status handling. When every item admitted to a convening has been dispositioned by a
       recorded DEC, the gate returns from OPEN to NOT SCHEDULED, unless an owner decision
       records a further convening. No other status is established.

D68-I  Recording. Each gate outcome is recorded as a new DEC in the consolidated decision log
       (DEC-030 Q4). Recording a decision does not itself amend or lock §15–§17 (DEC-064 item 2).

D68-J  Amendment boundary. This decision does not amend §16, does not alter the locked status of
       §16, and does not authorize any §16 amendment in advance. Any amendment to locked §16
       text requires the authority and explicit authorization required by the existing
       architecture, including the requirement that a future gate explicitly authorize the
       amendment (README "Known Findings Against Locked Text"). An owner decision does not
       directly override locked §15–§17.

D68-K  Preserved decisions. DEC-029, DEC-054 (including R04c and R04d), DEC-058 (F05a–F05d),
       DEC-064, DEC-065 (including D65-5), DEC-066, DEC-067 and R12B-1 … R12B-5 are unchanged.
       F19-05 remains an OPEN finding whose status as a finding against locked text is not
       established; it remains unindexed. OD19-04 remains OPEN. §19.24 criterion 3 is unchanged
       and remains NOT SATISFIED. §19 remains NOT LOCKED.

D68-L  §18. The §18 owner-decision-gate document is non-normative and does not control this
       gate's procedure. Its recommendation to batch §18 amendments imposes no batching on the
       §16 Amendment Gate. Whether the "§16 amendment gate" anticipated by §18 is this registered
       gate is not decided here; any relationship remains informational unless separately
       established.

D68-M  No new machinery. This decision creates no role, committee, quorum, vote, approver,
       reviewer, ticketing, calendar, external approval, Principal, Grant, Permission or gate,
       and assigns nothing to K4, K9, §17 or §22.

D68-N  This decision does not convene the gate, does not authorize implementation, and does not
       amend §15, §16 or §17. DEC-029 remains standing.
```

> **Transcription note (session process):** The approval message's "Required changes", prohibitions, post-edit
> verification and commit/push instructions are omitted; they governed only this change and are not owner decisions.

> **Index note (not owner wording):** DEC-068 is procedural. It does not convene the §16 Amendment Gate
> (status remains NOT SCHEDULED), does not resolve OD19-04 or F19-05, and does not amend §15–§17.

---

## DEC-069 — §16 Amendment Gate — Convening for OD19-04 / F19-05

- **Status:** CURRENT (adopted — gate OPEN; OD19-04 and F19-05 interpretation admitted, undecided)
- **Source:** Owner approval message for DEC-069 (2026-09-24), adopting D69-A … D69-L.
- **Related:** DEC-068 (D68-B … D68-H); §19.21.2 rows 6 and 9; register §5B and §8; DEC-054; DEC-058

```text
APPLY AUTHORIZATION — DEC-069

DEC-069 is APPROVED FOR ADOPTION exactly as presented.

Adopt:

DEC-069 — §16 Amendment Gate — Convening for OD19-04 / F19-05

with D69-A through D69-L exactly as presented in the approved candidate.

Do not reinterpret, rewrite, expand, shorten, or substantively modify any D69 provision.
```

Decision text (D69-A … D69-L, adopted verbatim by the approval above):

```text
D69-A  Convening. Under DEC-068 D68-C, the architecture owner convenes the §16 Amendment Gate
       by this decision. This decision is the convening record. On its adoption the gate's
       status changes from NOT SCHEDULED to OPEN.

D69-B  Admitted items. Exactly two registered items are admitted to this convening:
       (1) OD19-04, as registered in §19.21.2 row 6 (DEC-068 D68-F); and
       (2) the interpretation of F19-05, as registered in §19.21.2 row 9.
       No other registered item is admitted. No item is assigned to the gate, and the gate's
       registered scope is unchanged.

D69-C  OD19-04. Admission does not decide OD19-04. It does not select a permanent prohibition
       or a §16 composition path; does not define the scope of a permanent prohibition; does not
       determine whether locked §16 already excludes the path; does not determine whether a §16
       amendment is required; and does not determine whether the composition route is
       ultimately selected. DEC-054 R04a … R04g are unchanged.

D69-D  F19-05. F19-05 remains OPEN and unindexed. Whether it is a finding against locked text
       remains not established. Admission does not add F19-05 to the Known Findings table and
       does not satisfy criterion 3. DEC-058 F05d and DEC-065 D65-5, as it applies to F19-05,
       remain in force. DEC-058 F05a is unchanged: F19-05's interpretation is determined through
       OD19-04 and the applicable §16 gate.

D69-E  Relationship. The two items are admitted in the same convening under DEC-068 D68-E and
       D68-F. They are not the same decision, and admission of either does not resolve the
       other. OD19-04 concerns the direction stated in DEC-054 R04a. The interpretation of
       F19-05 is a separate question, determined as DEC-058 F05a states. The index treatment of
       F19-05 is a further separate decision governed by DEC-058 F05d. This decision does not
       set an order of resolution.

D69-F  Interim rules. DEC-042 R12B-1 … R12B-5 and DEC-054 R04b and R04e remain operative. The
       interim prohibition remains in force while OD19-04 is unresolved. Capability availability
       is unchanged.

D69-G  Composition requirements. DEC-054 R04c and R04d are unchanged. Admitting or considering a
       §16 composition path does not authorize composition. If a composition path is selected,
       the separate §16 amendment must still satisfy R04d.

D69-H  Other surfaces. §22, §18, KF-06, P2 and §21 are not agenda items. DEC-054 R04g (§22
       downstream) and DEC-058 F05b (including the relationship to KF-06) are unchanged. §18
       does not control the §16 Amendment Gate (DEC-068 D68-L).

D69-I  Decision authority. DEC-068 D68-G and D68-I govern. The architecture owner records the
       outcome for each admitted item as a new DEC. This decision creates no quorum, vote,
       approver, committee, or authorization through K4 or §17.

D69-J  Gate closure. This decision does not close the gate. DEC-068 D68-H governs the return to
       NOT SCHEDULED after both admitted items have been dispositioned by recorded DECs.

D69-K  Preserved decisions. DEC-029, DEC-042 (R12B-1 … R12B-5), DEC-054, DEC-058 (F05a … F05d),
       DEC-064, DEC-065 (including D65-5), DEC-066, DEC-067 and DEC-068 are unchanged.
       §19.24 criterion 3 is unchanged and remains NOT SATISFIED. §19 remains NOT LOCKED.

D69-L  Non-effects. This decision does not amend §15, §16 or §17; does not authorize any §16
       amendment in advance; does not determine whether §15 T-18 is contradicted; does not
       classify F19-05 as a finding against locked text; does not lock §19; and does not
       authorize implementation. DEC-029 remains standing.
```

> **Transcription note (session process):** The approval message's REQUIRED CHANGES, DO NOT CHANGE, IMPORTANT
> SUBSTANTIVE BOUNDARY, VALIDATION and GIT BOUNDARY sections are omitted; they governed only this change and are not
> recorded as owner decisions here.

> **Index note (not owner wording):** DEC-069 convenes the §16 Amendment Gate (NOT SCHEDULED → OPEN) for
> OD19-04 and the interpretation of F19-05 only. It decides neither item, does not amend §15–§17, and does not
> satisfy criterion 3.

---

## DEC-070 — §16 Amendment Gate — OD19-04 / F19-05 Disposition

- **Status:** CURRENT (adopted — OD19-04 Path A; F19-05 enforcement gap; gate NOT SCHEDULED)
- **Source:** Owner DEC-070 adoption message (2026-09-28): owner rulings 1–21 and the Path A boundary. Owner
  documentation-completeness ruling (2026-09-28): recorded in D70-I3 and in D70-D3 surface (2).
- **Related:** DEC-069; DEC-068 (D68-G … D68-J); DEC-054; DEC-058; DEC-042; §19.5.3; §19.13.1; §19.19; §19.21; §19.21.2; §19.23; register §5A, §5B, §8

```text
==================================================
OWNER RULINGS TO ADOPT AS DEC-070
==================================================

Create/adopt:

DEC-070 — §16 Amendment Gate — OD19-04 / F19-05 Disposition

Status: CURRENT / ADOPTED

The owner rulings are:

1. OD19-04 = PATH A.

2. Path A uses the declaration boundary established by D70-A3:
   credential-bearing file content is scoped by the applicable execution contract's declaration of a resource as containing credential-bearing content.

3. Do NOT create a runtime "resulting-content contains credentials" test.

4. Do NOT create a K6 runtime detector or arbitrary blob-content classifier.

5. R12B-1 = CONTINUE PERMANENTLY.
   Remove only the interim lifetime condition.
   The operative permanent rule is:

   A K11 WRITE scope entry MUST NOT target a resource declared by the applicable execution contract to contain credential-bearing content.

6. R12B-2 = CONTINUE.

7. R12B-3 = CONTINUE.

8. R12B-4 = REPLACE.
   Its interim transition language is replaced by the permanent Path A disposition.

9. R12B-5 = CONTINUE.

10. F19-05 interpretation = CATEGORY (ii), enforcement gap.

11. F05c = YES / resolved for purposes of the F05c statement, BUT this must NOT be represented as resolving the downstream questions that are routed elsewhere.

    Specifically, all F05b surfaces must be ACCOUNTED FOR by the decision:

    Surface 1 — K4 entry:
      - Existing §16.9 rule remains: credential material is K6-only.
      - No request field carries credential material.
      - The remaining question of how credential material could reach K4 / any residual undeclared-blob boundary remains routed to the applicable §16/P2/security-boundary work.
      - This decision does not resolve that downstream question.

    Surface 2 — staged content:
      - Staged content remains K6-internal.
      - No credential composition path is authorized.
      - The residual undeclared-blob issue remains an architectural/enforcement question on its existing route.
      - This decision does not create a detector.

    Surface 3 — X-38 validators:
      - Validators remain READ-class, handle-free, and receive only the K6-internal staged-object binding.
      - No credential handles or credential composition are introduced.
      - No validator-based credential detector is created.

    Surface 4 — K8 digest/journal:
      - X-26 and existing §16.10.2 protections remain.
      - This decision does NOT decide whether K8 should retain additional digests or evidence concerning credential-bearing content.
      - That question remains on its existing §16 / §21 route.

    Surface 5 — TH-31:
      - Existing §18 routing remains.
      - This decision does NOT resolve TH-31.
      - It only records that the surface has an existing downstream route.

    Surface 6 — KF-06:
      - KF-06 remains distinct from the F19-05 disposition.
      - The handle_ref path is not changed by DEC-070.

    IMPORTANT:
    "Accounted for" means each surface has an identified existing rule, boundary, or downstream route.
    It does NOT mean those downstream questions have been substantively resolved.

12. §16 amendment required by Path A itself = NO.

13. No §16 amendment is made by DEC-070.

14. OD19-04 = DISPOSITIONED.

15. F19-05 interpretation = DISPOSITIONED / resolved for the F05c purpose described above.

16. The §16 Amendment Gate returns to:
    NOT SCHEDULED

    after the two admitted items have been dispositioned.

17. F19-05 remains UNINDEXED in the Known Findings index.

18. Criterion 3 remains:
    NOT SATISFIED.

19. §19 remains:
    NOT LOCKED.

20. DEC-029 remains the implementation-authority boundary.
    DEC-070 authorizes no implementation.

21. Nothing in DEC-070 authorizes:
    - K6 credential composition
    - credential handles in arbitrary blobs
    - runtime credential-content inspection
    - a generic credential detector
    - host-side replacement
    - manual production modification
    - any SCC bypass
    - any change to K2–K11 responsibility
    - any amendment to §15–§17.

==================================================
PATH-A BOUNDARY
==================================================

Use this exact conceptual boundary:

"PATH A — Credential-bearing file content, as scoped in D70-A3, is permanently prohibited from SCC's file.replace Operation (DEC-054 R04a)."

Do NOT broaden this into an unsupported claim that SCC can inspect arbitrary resulting file content and determine whether credentials are present.

The decision must preserve the distinction between:
- authoring-time declaration of credential-bearing content, and
- runtime inspection/classification of arbitrary blob content.

The latter is NOT established by the architecture.
```

Decision text (prepared from the owner rulings above and the candidate reviewed by the owner; where any
difference exists, the owner rulings govern):

```text
PURPOSE
This decision records the outcome of the §16 Amendment Gate, convened by DEC-069, for the two
admitted items only: OD19-04 (§19.21.2 row 6) and the interpretation of F19-05 (§19.21.2 row 9).
No other item is admitted or decided.

PART A — OD19-04 OUTCOME: PATH A
D70-A1  PATH A — Credential-bearing file content, as scoped in D70-A3, is permanently prohibited
        from SCC's `file.replace` Operation (DEC-054 R04a).
D70-A2  The prohibition applies to SCC's `file.replace` Operation (§16.8).
D70-A3  Path A applies to SCC's `file.replace` Operation where a K11 WRITE scope entry targets a
        resource declared by the applicable execution contract to contain credential-bearing
        content.
D70-A4  The architecture does not presently define the declaration mechanism for
        credential-bearing status or define "applicable execution contract" as a separate
        declaration term. This decision does not create such a mechanism.
D70-A5  This decision does not establish a resulting-content test for credential material.
D70-A6  This decision does not establish runtime inspection or classification of arbitrary
        `blob` content, and creates no K6 runtime detector or blob-content classifier.

PART B — LIMITS OF THE SCOPE
D70-B1  The rule does not establish that arbitrary `blob` content cannot contain credential
        material (DEC-042 R12B-2; DEC-054 R04f).
D70-B2  Path A makes the prohibition permanent. It does not make the declaration mechanism more
        precise. The boundary is an authoring-time declaration of credential-bearing content,
        not runtime inspection or classification of arbitrary `blob` content.

PART C — INTERIM RULE (R12B) DISPOSITION
D70-C1  R12B-1 — CONTINUE PERMANENTLY. Only the interim lifetime condition ("Until OD19-04 is
        resolved") is removed. The permanent rule is: A K11 WRITE scope entry MUST NOT target a
        resource declared by the applicable execution contract to contain credential-bearing
        content. Its scope is unchanged and identical to D70-A3.
D70-C2  R12B-2 — CONTINUE.
D70-C3  R12B-3 — CONTINUE. Enforcement remains through release-authoring/validation controls
        consistent with A-23. No runtime inspection, K6 credential detection or new enforcement
        mechanism is established.
D70-C4  R12B-4 — REPLACE. Its interim transition language is replaced by the permanent Path A
        disposition recorded in this decision.
D70-C5  R12B-5 — CONTINUE. Capabilities requiring credential-bearing composition or
        credential-bearing WRITE content remain unavailable unless an authoritative architecture
        record establishes otherwise.
        DEC-042 is unchanged as the historical record of R12B-1 ... R12B-5.

PART D — F19-05 INTERPRETATION
D70-D1  F19-05 interpretation: CATEGORY (ii) — ENFORCEMENT GAP (DEC-058 F05a). The prohibition
        exists (D70-A3; D70-C1), but the current architecture provides no mechanical detection
        of arbitrary credential material entering staged or `blob` content.
D70-D2  This classification creates no runtime detector, does not authorize K6 to inspect
        credentials, and does not amend §16.

D70-D3  F05b accounting (DEC-058 F05b). "Accounted for" means each surface has an identified
        existing rule, boundary, or downstream route. It does not mean that downstream questions
        have been substantively resolved.
  (1) Credential-material entry into K4. The existing §16.9 rule remains: credential material is
      K6-only, and no request field carries credential material. The remaining question of how
      credential material could reach K4, including any residual undeclared-`blob` boundary,
      remains routed to the applicable §16 / P2 / security-boundary work (DEC-058). This
      decision does not resolve that downstream question.
  (2) Staged content. Staged content remains K6-internal (§16.8). No credential composition path
      is authorized (DEC-054 R04c). The residual undeclared-`blob` issue remains an unresolved
      architectural/enforcement question. In the reviewed material, the existing architecture
      does not provide a more specific named route for it; this decision does not create or
      assign such a route. This decision creates no detector.
  (3) X-38 validators. Validators remain READ class, handle-free, and receive only the
      K6-internal staged-object binding. No credential handles or credential composition are
      introduced. No validator-based credential detector is created.
  (4) K8 digest/journal. X-26 and the existing §16.10.2 protections remain. This decision does
      not decide whether K8 should retain additional digests or evidence concerning
      credential-bearing content. That question remains on its existing §16 / §21 route
      (DEC-058).
  (5) TH-31. The existing §18 routing remains (DEC-058). This decision does not resolve TH-31;
      it records only that the surface has an existing downstream route.
  (6) KF-06. KF-06 remains distinct from the F19-05 disposition. The `handle_ref` path is not
      changed by this decision.

PART E — F05c RESOLUTION
D70-E1  OD19-04 dispositioned, F19-05 interpreted, F19-05 resolved for purposes of F05c, and any
        downstream question resolved are distinct.
D70-E2  F05c resolution status: YES — F19-05 is resolved for purposes of DEC-058 F05c because
        every F05b surface is accounted for in D70-D3. This does not resolve the downstream
        questions that D70-D3 records as remaining on their existing routes.

PART F — CAPABILITY AVAILABILITY
D70-F1  Capabilities requiring credential-bearing composition or credential-bearing WRITE content
        remain unavailable unless and until an authoritative architecture record establishes
        otherwise (DEC-054 R04e; DEC-042 R12B-5).
D70-F2  Path A creates no credential-composition mechanism (DEC-054 R04c).
D70-F3  No implementation authorization follows from this decision.

PART G — §16 AMENDMENT
D70-G1  Path A is an owner-level prohibition. Enforcement remains release-authoring/validation
        based (DEC-042 R12B-3). This decision creates no K6 write-side credential detector and no
        credential-composition path.
D70-G2  §16 amendment required by Path A itself: NO. This does not preclude a future §16
        amendment for a separately identified issue.
D70-G3  No §16 amendment is made by this decision.

PART H — HOST BOUNDARY
D70-H1  This prohibition governs SCC's `file.replace` Operation. It does not govern, authorize,
        or define actions taken on the host outside SCC's security boundary (§15.15). This
        decision establishes no SCC path, mechanism, or authority for such actions.

PART I — F19-05 INDEX TREATMENT
D70-I1  F19-05 remains unindexed in the Known Findings index. Any index treatment is a separate
        owner decision and change-set action under DEC-058 F05d and DEC-065 D65-5 (as it applies
        to F19-05).
D70-I2  §19.24 criterion 3 remains NOT SATISFIED. §19 remains NOT LOCKED.
D70-I3  F19-05 is represented as ADDRESSED in the live register because its interpretation has
        been resolved for purposes of DEC-058 F05c, while its Known Findings index treatment
        remains a separate owner decision under DEC-058 F05d. ADDRESSED therefore records that
        the substantive interpretation has been addressed; it does not imply that F19-05 has
        been entered in the Known Findings index. This provision creates no new status
        vocabulary, does not change the category (ii) interpretation (D70-D1), does not reopen
        F05d, and does not imply that the downstream questions routed to §16 / §21 or §18
        (D70-D3 surfaces (4) and (5)) have been resolved.

PART J — AUTHORITY BOUNDARY
D70-J1  Nothing in this decision authorizes K6 credential composition; credential handles in
        arbitrary `blob` content; runtime credential-content inspection; a generic credential
        detector; host-side replacement; manual production modification; any SCC bypass; any
        change to K2–K11 responsibility; or any amendment to §15, §16 or §17.
D70-J2  DEC-029 remains the implementation-authority boundary. This decision authorizes no
        implementation.
D70-J3  DEC-042, DEC-054, DEC-058, DEC-064, DEC-065, DEC-066, DEC-067, DEC-068 and DEC-069 are
        unchanged.
D70-J4  §22 (DEC-054 R04g), KF-06, P2, §21 and F19-08's output question (DEC-061 F08d) are not
        admitted and remain as recorded.

PART K — GATE STATUS
D70-K1  OD19-04: DISPOSITIONED. F19-05 interpretation: DISPOSITIONED.
D70-K2  Both admitted items are dispositioned. Under DEC-068 D68-H the §16 Amendment Gate
        returns from OPEN to NOT SCHEDULED. DEC-068 remains the governing procedure. Historical
        references in DEC-064, DEC-068, DEC-069 and their index rows are not rewritten.
D70-K3  "Dispositioned" (DEC-068 D68-H) and "resolved" (DEC-058 F05c) are not treated as
        synonymous. Gate closure does not depend on F05c.

PART L — CHANGE SET (live-record synchronization)
D70-L1  1. Register OD19-04 row: OPEN → ADDRESSED (§19.21; DEC-054; DEC-070, Path A).
        2. §19.21 OD19-04 disposition: OPEN [DEC-054] → Addressed — Path A [DEC-070].
        3. §19.13.1: interim authoring rule → permanent authoring rule [DEC-070 D70-C1].
        4. §19.5.3 D19-05: T-18 relationship recorded as enforcement gap, category (ii);
           disposition updated [DEC-070 D70-D1, D70-E2, D70-D3, D70-I1].
        5. §19.19 P6 row: credential-bearing `blob` pointer updated [DEC-070 D70-D1].
        6. §19.23: DEC-070 pointer row added; the historical F19-05 row is unchanged.
        7. Register F19-05 row: OPEN → ADDRESSED (DEC-058; DEC-070; unindexed — index
           treatment separate).
        8. Register §8 gate row: §16 Amendment Gate NOT SCHEDULED (DEC-070; DEC-068 D68-H).
        9. Register §5B introduction: gate NOT SCHEDULED (DEC-070; DEC-068 D68-H).
        10. §19.21.2 heading: NOT SCHEDULED — DEC-070. Registered item rows unchanged.
        11. README decision range: DEC-001 … DEC-070.
        12. F19-05 remains absent from the Known Findings index.
        13. §19.24 criterion 3 remains NOT SATISFIED.
        14. §19 remains NOT LOCKED.
```

> **Transcription note (session process):** The adoption message's opening repository/process lines and its LIVE
> RECORD SYNCHRONIZATION REQUIRED, DEC-070 CONTENT REQUIREMENTS, HISTORICAL-PRESERVATION RULE and VALIDATION sections
> are omitted; they governed only this change and are summarized in D70-L1.

> **Index note (not owner wording):** DEC-070 records Path A for OD19-04 and interprets F19-05 as an enforcement gap.
> It does not amend §15–§17, does not index F19-05, and does not satisfy criterion 3. The §16 Amendment Gate returns
> to NOT SCHEDULED under DEC-068 D68-H.

---

## DEC-071 — §21 Scope and Gate Structure

- **Status:** CURRENT (adopted — §21 scope and gate structure; §21 NOT DESIGNED; not locked)
- **Source:** Owner adoption authorization for DEC-071 … DEC-080 (2026-09-30), applying the owner-approved
  decision set of the adoption-preparation pass and the owner rulings of the §21, §19-lock, §22 and P2/K3
  drafting passes.
- **Related:** DEC-024; DEC-025; DEC-035; DEC-039; DEC-049; DEC-056; DEC-064; DEC-072; §17.18; A-35; §19.12; register CHANGE-022

```text
I now authorize application of that exact adoption change set, subject to the controls below.

Apply DEC-071 through DEC-080 exactly as reviewed.

Final numbering:

DEC-071 — §21 Scope and Gate Structure
DEC-072 — ODF-18-07 Disposition
DEC-073 — F19-05 Index Treatment
DEC-074 — §19 Locked Form
DEC-075 — §19 Lock
DEC-076 — §22 Scope and Gate Structure
DEC-077 — Recovery Gate Identity
DEC-078 — §22 Post-Lock Route
DEC-079 — Development Path and Phase-6 Entry Criteria
DEC-080 — P2/K3 Gate Structure

Do NOT renumber them differently.

DEC-071
--------
Title:
§21 Scope and Gate Structure

Use the previously drafted DEC-071 content.

It establishes the §21 scope and gate structure without inventing a hidden post-lock route.

Preserve the owner ruling that §21 should attempt to close all §21-owned normative matters before lock. If an item remains genuinely unresolved, return it to the owner rather than inventing a generic post-lock mechanism.

Do not create a §21 post-lock route.
```

Decision text (D71-1 … D71-10, adopted by the authorization above):

```text
D71-1  Authority. §21 is designed under DEC-025 PHASE 3, in the order fixed by DEC-024. It follows
       the §19 pattern: candidate text, owner dispositions, and a separate lock DEC. No new gate is
       created.
D71-2  Lock scope. §21 will lock:
       (a) the K4 audit-record contract for every event A-35 enumerates (Intent Authorization, Plan
           Authorization, revalidation, approval acceptance or rejection, cancellation,
           authorization-administration change), covering the §17.18 field set without redefining it;
       (b) the meaning of "durably recorded" for DEC-035 R5a;
       (c) the audit-write failure condition that DEC-035 R5b requires to be surfaced;
       (d) the architectural scope of sequencing and gap detection;
       (e) the tamper-evidence claim scope (what SCC may and must not claim), consistent with DEC-072;
       (f) the minimal event model (D71-3);
       (g) the export content under DEC-072;
       (h) K4 audit retention and capacity details within the §19 floors (D71-4).
       No tamper-evidence mechanism is selected by this decision.
D71-3  Minimal event model. §21 defines only (A) K4 audit records required by A-35 / §17.18 and
       (B) operational-condition records where an authoritative source requires one (at present:
       the DEC-035 R5b audit-write failure condition). §21 creates no general-purpose domain-event bus,
       no generic event architecture and no generic Attention-item lifecycle. CHANGE-022 is ADDRESSED
       by this scope decision: no current authoritative requirement establishes a general-purpose
       domain-event model as part of §21. This is not a finding that such a model is impossible or
       undesirable.
D71-4  Retention. K4 audit is "Defined by §21" (§19.12), and "§21 still owns audit format,
       retention/capacity details and tamper-evidence" (DEC-035). The §19 floors remain binding:
       DEC-039 R9a, R9e, R9h; DEC-049 R19g. Removal remains governed by §21, §22 and DEC-042
       (DEC-039). DEC-056 R06a applies only to DC-05. §21 performs DEC-056 R06i: it identifies audit
       or event records whose retention or resolvability depends on DC-05. Ownership of K4 audit
       retention is not transferred to §19.
D71-5  Deferrals. "Implementation" is not an architectural gate. A normative matter is either
       resolved in §21 or deferred to an established owning gate. A non-normative detail that
       cannot alter the §21 contract may remain for implementation; it is not an architectural
       deferral and does not block §21. Existing routes are preserved unchanged: DEC-046 (orphan
       reporting); DEC-058 / DEC-070 D70-D3(4) (K8 digests, §16 / §21); DEC-053 R03j (K8 capacity,
       conditional on OD19-03); DEC-044 (K3/K5 logging); §17.24 P-8 (R0 view noise, "Blocks? No").
D71-6  §22 hand-offs. Owned downstream by §22, with §21 supplying the record contract where one is
       needed: migrated audit-record representation (DEC-049 R19g); K7/K8 consistency after restore
       (DEC-047); K8 lifetime evidence (DEC-048 R18i); Local Root Operator lifecycle records
       (DEC-060; DEC-046 R16c, R16h); recovery/removal interactions (DEC-039; DEC-042 (A));
       the lifecycle of any SCC-produced export artifact (DEC-072 D72-6).
D71-7  CHANGE-023 remains explicitly unresolved (DEC-064 item 10). It is outside §21 and is not
       assigned to any owner.
D71-8  Lock criteria. §21 may be locked when:
       1. every §21-owned item is decided or explicitly deferred to a named/established gate where
          required;
       2. ODF-18-07 is dispositioned;
       3. the audit contract covers every A-35 event and every §17.18 field and introduces no
          host-execution facts;
       4. no accepted decision widens authority, transfers responsibility between K2–K11,
          contradicts §15–§17, or makes an unauthorized §15/§16 amendment;
       5. every genuine architectural deferral has an established owning route (interpreted as in
          D71-5);
       6. no implementation authority is created, and §21 lock requires a separate explicit
          owner DEC.
D71-9  Non-ownership. §21 does not own or redefine: the K8 journal (§16.10), the §17.18 fields,
       DC-05 retention, recovery, P2, K3, CyberPanel K2, the storage engine or schema, or
       implementation authority.
D71-10 Non-effects. No amendment to §15–§17. DEC-001 … DEC-070 unchanged. §21 is not locked.
       No implementation authority. DEC-029 remains standing.
```

> **Transcription note (session process):** The decision text is the reviewed draft. Its status line ("CANDIDATE —
> NOT ADOPTED") is omitted. The authorization's other sections (application rules, file requirements, prohibited
> changes, validation, commit rule) governed only this change set and are omitted.

> **Index note (not owner wording):** DEC-071 fixes the §21 scope, minimal event model and six lock criteria. It
> does not lock §21, create a §21 post-lock route, amend §15–§17 or authorize implementation.

---

## DEC-072 — ODF-18-07 Disposition

- **Status:** CURRENT (adopted — ODF-18-07 Option B, mechanism (iii); KF-08 OPEN)
- **Source:** Owner adoption authorization for DEC-071 … DEC-080 (2026-09-30), applying the owner-approved
  decision set of the adoption-preparation pass and the owner rulings of the §21, §19-lock, §22 and P2/K3
  drafting passes.
- **Related:** DEC-071; §18 owner-decision gate §8 (ODF-18-07); KF-08; §15.4 item 6; §16.1.3; register ODF-18-07

```text
I now authorize application of that exact adoption change set, subject to the controls below.

Apply DEC-071 through DEC-080 exactly as reviewed.

Final numbering:

DEC-071 — §21 Scope and Gate Structure
DEC-072 — ODF-18-07 Disposition
DEC-073 — F19-05 Index Treatment
DEC-074 — §19 Locked Form
DEC-075 — §19 Lock
DEC-076 — §22 Scope and Gate Structure
DEC-077 — Recovery Gate Identity
DEC-078 — §22 Post-Lock Route
DEC-079 — Development Path and Phase-6 Entry Criteria
DEC-080 — P2/K3 Gate Structure

Do NOT renumber them differently.

DEC-072
--------
Title:
ODF-18-07 Disposition

Use the previously drafted DEC-072 content.

The owner ruling is:

ODF-18-07 is dispositioned using mechanism (iii), host-level export outside the SCC runtime.

Do not turn this into a new SCC runtime authority.
```

Decision text (D72-1 … D72-10, adopted by the authorization above):

```text
D72-1  ODF-18-07: OPTION B — "Supported but optional". Deployments opt in.
D72-2  Mechanism (iii): "A host-level export facility administered by root outside the SCC runtime
       needs no amendment." No §15, §16 or §17 amendment.
D72-3  No K6 export Operation (mechanism (i)). No K4 egress (mechanism (ii)). §15.4 item 6, §16.1.3
       and T-31 are unchanged.
D72-4  The export facility is external, administered by root outside the SCC runtime and outside
       SCC's security boundary (§15.15). It is not an SCC component. SCC gains no authority over it.
D72-5  §21 defines the exported audit content, including the anchor-legitimacy record (source text
       of Options A/B: "§19/§21 define what is exported, and the anchor-legitimacy record is
       exported too").
D72-6  Any SCC-produced artifact the facility reads "is a §19 matter" (source). Its lifecycle follows
       the applicable §19 route and §22's downstream lifecycle/recovery treatment. This gives §19 no
       ownership of the external export mechanism.
D72-7  Security consequence (source): "SC-17 becomes conditional on export being enabled. Without
       export, RR-03 fully applies, including to attribution."
D72-8  §18 remains conditional/open. This decision does not lock §18 and does not perform the §18
       post-decision rewrites (SC-17, T-18-09 / SR-12 scoping, SC-09, SRF-18-11). They remain
       §18 follow-ups.
D72-9  KF-08 remains OPEN: locked text still provides no export mechanism, and mechanism (iii) lies
       outside the SCC runtime. Its owner pointer records this disposition.
D72-10 No implementation authority. DEC-029 remains standing.
```

> **Transcription note (session process):** The decision text is the reviewed draft. Its status line ("CANDIDATE —
> NOT ADOPTED") is omitted. The authorization's other sections (application rules, file requirements, prohibited
> changes, validation, commit rule) governed only this change set and are omitted.

> **Index note (not owner wording):** DEC-072 dispositions ODF-18-07 only. The export facility is outside SCC; KF-08
> stays OPEN; §18 is not locked.

---

## DEC-073 — F19-05 Index Treatment

- **Status:** CURRENT (adopted — F19-05 indexed as KF-12; OPEN — enforcement gap, category (ii))
- **Source:** Owner adoption authorization for DEC-071 … DEC-080 (2026-09-30), applying the owner-approved
  decision set of the adoption-preparation pass and the owner rulings of the §21, §19-lock, §22 and P2/K3
  drafting passes.
- **Related:** DEC-058 (F05d); DEC-065 (D65-5); DEC-067; DEC-070; §19.5.3 D19-05; KF-12; §19.24 criterion 3

```text
I now authorize application of that exact adoption change set, subject to the controls below.

Apply DEC-071 through DEC-080 exactly as reviewed.

Final numbering:

DEC-071 — §21 Scope and Gate Structure
DEC-072 — ODF-18-07 Disposition
DEC-073 — F19-05 Index Treatment
DEC-074 — §19 Locked Form
DEC-075 — §19 Lock
DEC-076 — §22 Scope and Gate Structure
DEC-077 — Recovery Gate Identity
DEC-078 — §22 Post-Lock Route
DEC-079 — Development Path and Phase-6 Entry Criteria
DEC-080 — P2/K3 Gate Structure

Do NOT renumber them differently.

DEC-073
--------
Title:
F19-05 Index Treatment

Use the previously drafted DEC-073 content.

Owner ruling:

F19-05 is indexed.

Use the previously selected treatment:

- Frame 2
- status:
  OPEN — enforcement gap, category (ii)

Do not reopen DEC-070's Path A decision.

Do not claim the gap has been resolved merely because it is indexed.

Do not alter §16.
```

Decision text (D73-1 … D73-5, adopted by the authorization above):

```text
D73-1  F19-05 is recorded in the architecture index under "Known Findings Against Locked Text" as
       KF-12, in the scope of §19.5.3 D19-05 as interpreted by DEC-070 (category (ii),
       enforcement gap).
D73-2  DEC-065 D65-5 states: "Do not add F19-05 or F19-06 to the Known Findings table." The owner
       prospectively determines that this instruction no longer applies to F19-05, with effect from
       this decision. The other D65-5 instructions are unaffected. DEC-065 is unchanged and remains
       the historical record of the instruction as given.
D73-3  KF-12 status: OPEN — enforcement gap, category (ii). The register's F19-05 status (ADDRESSED:
       the interpretation has been addressed, DEC-070 D70-I3) is distinct from the Known Finding's
       status (OPEN: the gap persists).
D73-4  Indexing does not change category (ii), establish a new defect category, amend §15 or §16,
       resolve the enforcement gap, or alter DEC-070. DEC-058 F05d is followed: the addition is made
       by owner decision and change set, without modifying locked text.
D73-5  No implementation authority. DEC-029 remains standing.
```

> **Transcription note (session process):** The decision text is the reviewed draft. Its status line ("CANDIDATE —
> NOT ADOPTED") is omitted. The authorization's other sections (application rules, file requirements, prohibited
> changes, validation, commit rule) governed only this change set and are omitted.

> **Index note (not owner wording):** DEC-073 indexes F19-05 as KF-12 (OPEN — enforcement gap, category (ii)).
> DEC-065 and DEC-070 are unchanged; the gap is not resolved.

---

## DEC-074 — §19 Locked Form

- **Status:** CURRENT (adopted — §19 locked in its existing form)
- **Source:** Owner adoption authorization for DEC-071 … DEC-080 (2026-09-30), applying the owner-approved
  decision set of the adoption-preparation pass and the owner rulings of the §21, §19-lock, §22 and P2/K3
  drafting passes.
- **Related:** DEC-023; DEC-030 (Q2); DEC-064 (item 3); DEC-075

```text
I now authorize application of that exact adoption change set, subject to the controls below.

Apply DEC-071 through DEC-080 exactly as reviewed.

Final numbering:

DEC-071 — §21 Scope and Gate Structure
DEC-072 — ODF-18-07 Disposition
DEC-073 — F19-05 Index Treatment
DEC-074 — §19 Locked Form
DEC-075 — §19 Lock
DEC-076 — §22 Scope and Gate Structure
DEC-077 — Recovery Gate Identity
DEC-078 — §22 Post-Lock Route
DEC-079 — Development Path and Phase-6 Entry Criteria
DEC-080 — P2/K3 Gate Structure

Do NOT renumber them differently.

DEC-074
--------
Title:
§19 Locked Form

Use the previously drafted DEC-074 content, which was formerly draft DEC-076.

The owner selected:

1-A — lock §19 in its existing form.

Important:
- do NOT clean-transcribe §19
- preserve its DEC tags
- preserve its normative classification/findings structure
- preserve its gate/lock record
- do not rewrite locked §15–§17
- DEC-030 Q2 remains specifically applicable to §15, §16 and §17
- §19 may become Category 1 prospectively once locked
```

Decision text (D74-1 … D74-5, adopted by the authorization above):

```text
D74-1  §19 may be locked in its existing form. No clean transcription is made.
D74-2  The [DEC-0xx] tags remain, as DEC-064 item 3 requires. The §19.5.3 compatibility and findings
       material remains, as analogous to the compatibility, conflict and gate material retained in
       locked §15.16/§15 Gate Assessment, §16.16 and §17's gate sections. The §19 gate and lock record
       remains.
D74-3  DEC-030 Q2 governs §15, §16 and §17 by name. README's locked-document statements are read with
       that scope. From §19's lock forward they are clarified prospectively, not rewritten.
D74-4  On §19's lock (DEC-075), §19 joins Category 1 prospectively. DEC-023 and §19's earlier
       Category 4 classification remain historical.
D74-5  Only the status, location and lock bookkeeping that DEC-075 requires changes. No authority is
       widened. No §15–§17 amendment. No implementation authority; DEC-029 stands.
```

> **Transcription note (session process):** The decision text is the reviewed draft previously labelled DEC-076,
> renumbered under the owner's numbering ruling: D76-1 … D76-5 → D74-1 … D74-5; "DEC-074" (the §19 lock) → DEC-075.
> The draft status line is omitted. The authorization's other sections (application rules, file requirements,
> prohibited changes, validation, commit rule) governed only this change set and are omitted.

> **Index note (not owner wording):** DEC-074 fixes the form in which §19 is locked. The lock itself is DEC-075.

---

## DEC-075 — §19 Lock

- **Status:** CURRENT (adopted — §19 LOCKED)
- **Source:** Owner adoption authorization for DEC-071 … DEC-080 (2026-09-30), applying the owner-approved
  decision set of the adoption-preparation pass and the owner rulings of the §21, §19-lock, §22 and P2/K3
  drafting passes.
- **Related:** DEC-063; DEC-064; DEC-067; DEC-070; DEC-073; DEC-074; §19.24; §19.25; §19.26. Adopted after DEC-073 and DEC-074.

```text
I now authorize application of that exact adoption change set, subject to the controls below.

Apply DEC-071 through DEC-080 exactly as reviewed.

Final numbering:

DEC-071 — §21 Scope and Gate Structure
DEC-072 — ODF-18-07 Disposition
DEC-073 — F19-05 Index Treatment
DEC-074 — §19 Locked Form
DEC-075 — §19 Lock
DEC-076 — §22 Scope and Gate Structure
DEC-077 — Recovery Gate Identity
DEC-078 — §22 Post-Lock Route
DEC-079 — Development Path and Phase-6 Entry Criteria
DEC-080 — P2/K3 Gate Structure

Do NOT renumber them differently.

DEC-075
--------
Title:
§19 Lock

Use the previously drafted DEC-075 content, formerly draft DEC-074.

DEC-075 is the ACTUAL §19 LOCK DECISION.

It depends on DEC-073 and DEC-074.

Once adopted, §19 becomes locked.

The repository change associated with this lock includes the approved move:

FROM:
  docs/architecture/open/19-persistence-secrets-data-lifecycle.md

TO:
  docs/architecture/current/19-persistence-secrets-data-lifecycle.md

Do NOT perform that move during this pass.

Only prepare it as part of the proposed adoption change set.

The lock must not:
- widen authority
- amend §15–§17
- create implementation authority
- transfer responsibility between K2–K11
```

Decision text (D75-1 … D75-6, adopted by the authorization above):

```text
D75-1  Evaluation. §19.24 criteria 1–5 are satisfied (1: DEC-031 … DEC-050; 2: DEC-051 … DEC-057,
       DEC-064, DEC-070; 3: DEC-067, DEC-073; 4: no violation identified; 5: DEC-064 §C-2).
D75-2  Lock. §19 is LOCKED as the persistence, secrets and data-lifecycle classification of SCC: the
       storage domains and data classes of §19.6–§19.7, the ownership and access model of
       §19.8–§19.10, and invariants S19-01 … S19-15, as established by owner decisions DEC-031 …
       DEC-067, DEC-070 and DEC-073. (DEC-068 and DEC-069 are §16 Amendment Gate procedure and
       convening; they are not §19 content.)
D75-3  Post-lock route. Items recorded as OPEN or DEFERRED in §19.21–§19.22 remain open at the gates
       named there. Their resolution after lock uses the DEC-063 procedure: a new DEC identifying
       each §19 passage it changes, and §19 amended to match. This decision applies that procedure
       to §19.21–§19.22 items beyond the OD19 items, Q19 items and deferred findings named in DEC-063.
       DEC-063 itself is not rewritten. No other route changes locked §19 text.
D75-4  Authority tier. From this decision forward, §19 is added to the locked-architecture authority
       tier (Category 1). DEC-023 remains the historical record. §19's earlier Category 4
       classification remains historical. The hierarchy is supplemented prospectively, not rewritten.
       The locked form is established by DEC-074.
D75-5  Documentation state. On adoption, §19 moves from docs/architecture/open/ to
       docs/architecture/current/ (convention: current/15-…, 16-…, 17-… hold the locked texts), and
       its status header follows the locked-document convention.
D75-6  No implementation authority. DEC-029 remains standing. §15–§17 are unchanged.
```

> **Transcription note (session process):** The decision text is the reviewed draft previously labelled DEC-074,
> renumbered under the owner's numbering ruling: D74-1 … D74-6 → D75-1 … D75-6; D75-4 cites DEC-074 as the form
> decision. The draft status line is omitted. The authorization's other sections (application rules, file
> requirements, prohibited changes, validation, commit rule) governed only this change set and are omitted.

> **Index note (not owner wording):** DEC-075 is the §19 lock. §19 moves to current/ and joins Category 1
> prospectively; DEC-023 is not rewritten. No implementation authority.

---

## DEC-076 — §22 Scope and Gate Structure

- **Status:** CURRENT (adopted — §22 scope and gate structure; §22 NOT DESIGNED; not locked)
- **Source:** Owner adoption authorization for DEC-071 … DEC-080 (2026-09-30), applying the owner-approved
  decision set of the adoption-preparation pass and the owner rulings of the §21, §19-lock, §22 and P2/K3
  drafting passes.
- **Related:** DEC-021; DEC-024; DEC-025; DEC-071 (D71-6); DEC-077; DEC-078; §17.1.5; A-07; T-23; T-29

```text
I now authorize application of that exact adoption change set, subject to the controls below.

Apply DEC-071 through DEC-080 exactly as reviewed.

Final numbering:

DEC-071 — §21 Scope and Gate Structure
DEC-072 — ODF-18-07 Disposition
DEC-073 — F19-05 Index Treatment
DEC-074 — §19 Locked Form
DEC-075 — §19 Lock
DEC-076 — §22 Scope and Gate Structure
DEC-077 — Recovery Gate Identity
DEC-078 — §22 Post-Lock Route
DEC-079 — Development Path and Phase-6 Entry Criteria
DEC-080 — P2/K3 Gate Structure

Do NOT renumber them differently.

DEC-076
--------
Title:
§22 Scope and Gate Structure

Use the previously drafted DEC-076 content, formerly draft DEC-077.

Owner ruling:

2-A — whole-section lock with explicit deferrals.

§22 owns the lifecycle/recovery/bootstrap mechanics assigned by the existing architecture and owner decisions.

Minimum pre-lock scope:

1. Local Root Operator authority for first-admin bootstrap
2. first `scc.administrator` membership mechanics
3. K9 mechanics/authentication
4. P11 K9 → K4 interface required by bootstrap
5. bootstrap audit record under §21

No temporary web bootstrap.

K11 installer placement remains outside the minimum §22 subset and remains on the OQ-6 / recovery route.

No partial §22 lock.
```

Decision text (D76-1 … D76-8, adopted by the authorization above):

```text
D76-1  Purpose. §22 designs SCC lifecycle and recovery under DEC-025 PHASE 4 ("Design §22 /
       recovery/lifecycle as required"), in the DEC-024 order.
D76-2  Ownership. §22 owns the lifecycle, recovery and bootstrap mechanics assigned to it by locked
       architecture and routed to it by owner decisions: §15.18 OQ-6; §16.15 Q-1 (anchor provisioning
       mechanics), Q-4, Q-5, Q-7 (refresh); §17.24 P-1 (mechanics), P-5; §17.1.5 bootstrap mechanics;
       DEC-021; DEC-046 R16c/R16h; the §19.22 rows naming §22; the DEC-071 D71-6 hand-offs.
       The gate identity follows DEC-077.
D76-3  Required pre-lock scope, which the Phase-6 dependency needs:
       (1) Local Root Operator authority for the first-admin bootstrap act;
       (2) mechanics establishing the first `scc.administrator` membership (A-07; §17.1.5);
       (3) K9 mechanics and Local Root Operator authentication for that act (R16c; T-29);
       (4) the P11 K9 → K4 interface as the bootstrap act requires it (K7 is accessible only to
           identity C, T-23);
       (5) the bootstrap audit record, under the contract §21 supplies.
       No temporary web bootstrap (DEC-021). The bootstrap is limited to A-07 (T-29).
D76-4  Other §22 subjects may remain open at lock if each is explicitly recorded with its owning gate,
       or as open at §22 under DEC-078.
D76-5  K11 installer placement remains on its OQ-6 route. It is not in D76-3.
D76-6  Process: candidate → owner dispositions (recorded as DEC entries in the consolidated decision
       log, DEC-030 Q4) → a separate lock DEC. There is no partial lock.
D76-7  Lock criteria. §22 may be locked when:
       1. every D76-3 item is decided;
       2. every other §22-owned item is decided, deferred to an established gate, or recorded as open
          under DEC-078;
       3. no accepted decision widens authority, transfers responsibility between K2–K11, contradicts
          §15–§17, or makes an unauthorized §15/§16/§17 amendment;
       4. no web-reachable recovery or bootstrap path is created (T-29; DEC-021);
       5. every deferral names its owning gate;
       6. no implementation authority is created, and the lock is a separate explicit owner DEC.
D76-8  §22 does not redefine K4, K6, K9, K11 or P11 behavior established by locked architecture.
       Post-lock changes use DEC-078. No §15–§17 amendment. No implementation authority. DEC-076 does
       not lock §22.
```

> **Transcription note (session process):** The decision text is the reviewed draft previously labelled DEC-077,
> renumbered under the owner's numbering ruling: D77-1 … D77-8 → D76-1 … D76-8; "DEC-077" (self) → DEC-076;
> "DEC-078" (identity) → DEC-077; "DEC-079" (route) → DEC-078. The draft status line is omitted. The authorization's
> other sections (application rules, file requirements, prohibited changes, validation, commit rule) governed only
> this change set and are omitted.

> **Index note (not owner wording):** DEC-076 fixes the §22 scope and gate structure. It does not lock §22; there is
> no partial lock.

---

## DEC-077 — Recovery Gate Identity

- **Status:** CURRENT (adopted — recovery gate = §22 gate)
- **Source:** Owner adoption authorization for DEC-071 … DEC-080 (2026-09-30), applying the owner-approved
  decision set of the adoption-preparation pass and the owner rulings of the §21, §19-lock, §22 and P2/K3
  drafting passes.
- **Related:** DEC-076; DEC-078; §15 ("§22 / recovery gate"); §16.15; §17 Local Root Operator row

```text
I now authorize application of that exact adoption change set, subject to the controls below.

Apply DEC-071 through DEC-080 exactly as reviewed.

Final numbering:

DEC-071 — §21 Scope and Gate Structure
DEC-072 — ODF-18-07 Disposition
DEC-073 — F19-05 Index Treatment
DEC-074 — §19 Locked Form
DEC-075 — §19 Lock
DEC-076 — §22 Scope and Gate Structure
DEC-077 — Recovery Gate Identity
DEC-078 — §22 Post-Lock Route
DEC-079 — Development Path and Phase-6 Entry Criteria
DEC-080 — P2/K3 Gate Structure

Do NOT renumber them differently.

DEC-077
--------
Title:
Recovery Gate Identity

Use the previously drafted DEC-077 content, formerly draft DEC-078.

Owner ruling:

The "recovery gate" referenced by locked §15–§17 and related architecture is the §22 Lifecycle / Recovery gate.

This is an identity/organizational resolution only.

It does NOT:
- give §22 authority over K4
- change K6 enforcement
- change K9 authority
- create web recovery
- amend §15–§17

MANDATORY D77-4 WORDING CHANGE

In DEC-077 D77-4, replace the phrase:

"the §22 stub statement is superseded prospectively"

with:

"the §22 stub statement is replaced prospectively by DEC-077."

Do not otherwise change the substance of D77-4.
```

Decision text (D77-1 … D77-4, adopted by the authorization above):

```text
D77-1  The "recovery gate" referenced in locked §15 (lines "(§22 / recovery gate)", K9 row, P11,
       T-29, OQ-6, the K8-unavailable row), §16.15 (Q-4, Q-5) and §17 (the Local Root Operator row,
       P-5, the T-29 note) is the §22 gate.
D77-2  This decision resolves gate identity only. Every locked reference stands unchanged:
       P11 remains K9 → K4 / K6; Local Root Operator authority remains as §17 states; bootstrap
       mechanics remain §22's (§17.1.5); R16c, T-29, Q-4, Q-5, Q-7, OQ-6 and P-5 are unchanged.
D77-3  §22's status as the recovery gate grants it no authority over K4. K4 remains the authorization
       point, K6 the execution enforcer, and K9 the host-local administrative interface. There is no
       web recovery bypass (T-29).
D77-4  The §22 stub's statement that recovery authority "may" be handled by a separate gate is
       replaced prospectively by DEC-077 for documentation purposes. No separate gate is created.
       No implementation authority.
```

> **Transcription note (session process):** The decision text is the reviewed draft previously labelled DEC-078,
> renumbered under the owner's numbering ruling: D78-1 … D78-4 → D77-1 … D77-4; in D77-4 the draft words "is
> superseded prospectively" are replaced by "is replaced prospectively by DEC-077", as the owner's mandatory wording
> change requires, with no other change. The draft status line is omitted. The authorization's other sections
> (application rules, file requirements, prohibited changes, validation, commit rule) governed only this change set
> and are omitted.

> **Index note (not owner wording):** DEC-077 resolves gate identity only; no locked reference changes and no
> authority moves.

---

## DEC-078 — §22 Post-Lock Route

- **Status:** CURRENT (adopted — §22 post-lock route; applies after §22 lock)
- **Source:** Owner adoption authorization for DEC-071 … DEC-080 (2026-09-30), applying the owner-approved
  decision set of the adoption-preparation pass and the owner rulings of the §21, §19-lock, §22 and P2/K3
  drafting passes.
- **Related:** DEC-063 (precedent only); DEC-068; DEC-076; DEC-077

```text
I now authorize application of that exact adoption change set, subject to the controls below.

Apply DEC-071 through DEC-080 exactly as reviewed.

Final numbering:

DEC-071 — §21 Scope and Gate Structure
DEC-072 — ODF-18-07 Disposition
DEC-073 — F19-05 Index Treatment
DEC-074 — §19 Locked Form
DEC-075 — §19 Lock
DEC-076 — §22 Scope and Gate Structure
DEC-077 — Recovery Gate Identity
DEC-078 — §22 Post-Lock Route
DEC-079 — Development Path and Phase-6 Entry Criteria
DEC-080 — P2/K3 Gate Structure

Do NOT renumber them differently.

DEC-078
--------
Title:
§22 Post-Lock Route

Use the previously drafted DEC-078 content, formerly draft DEC-079.

Owner ruling:

After §22 is locked, changes occur only through a new explicit DEC resolving an OPEN/DEFERRED item or a consequential change required by an adopted DEC of another gate.

Any resulting §22 amendment must match the adopted decision.

Do not create a generic architecture authority.

Do not use this route to amend §15–§17 without the proper amendment path.
```

Decision text (D78-1 … D78-4, adopted by the authorization above):

```text
D78-1  After §22 is locked, locked §22 text changes only through a new DEC that (a) resolves an item
       recorded as OPEN or DEFERRED in locked §22, or (b) records a consequential change required by
       an adopted DEC of another established gate that resolves a dependency locked §22 records.
D78-2  The DEC identifies each §22 passage it changes, and §22 is amended to match. No other route
       changes locked §22 text. Silent edits are not permitted.
D78-3  This route cannot widen authority, transfer responsibility between K2–K11, or amend §15, §16
       or §17. A change requiring such an amendment must use the applicable established amendment
       path (for §16: the §16 Amendment Gate, DEC-068). Where no amendment path is established, the
       change cannot proceed through this route.
D78-4  This route creates no general architecture-change authority. It does not apply to §19
       (DEC-063), §21 or any other section. Historical decisions are preserved.
```

> **Transcription note (session process):** The decision text is the reviewed draft previously labelled DEC-079,
> renumbered under the owner's numbering ruling: D79-1 … D79-4 → D78-1 … D78-4. The draft status line is omitted.
> The authorization's other sections (application rules, file requirements, prohibited changes, validation, commit
> rule) governed only this change set and are omitted.

> **Index note (not owner wording):** DEC-078 applies only after §22 is locked and only to §22. It is not a general
> amendment route.

---

## DEC-079 — Development Path and Phase-6 Entry Criteria

- **Status:** CURRENT (adopted — Phase-6 entry criteria; no implementation authority)
- **Source:** Owner adoption authorization for DEC-071 … DEC-080 (2026-09-30), applying the owner-approved
  decision set of the adoption-preparation pass and the owner rulings of the §21, §19-lock, §22 and P2/K3
  drafting passes.
- **Related:** DEC-024; DEC-025; DEC-029; DEC-071; DEC-075; DEC-076; DEC-077; DEC-078; DEC-080; ODF-18-06; OD19-01

```text
I now authorize application of that exact adoption change set, subject to the controls below.

Apply DEC-071 through DEC-080 exactly as reviewed.

Final numbering:

DEC-071 — §21 Scope and Gate Structure
DEC-072 — ODF-18-07 Disposition
DEC-073 — F19-05 Index Treatment
DEC-074 — §19 Locked Form
DEC-075 — §19 Lock
DEC-076 — §22 Scope and Gate Structure
DEC-077 — Recovery Gate Identity
DEC-078 — §22 Post-Lock Route
DEC-079 — Development Path and Phase-6 Entry Criteria
DEC-080 — P2/K3 Gate Structure

Do NOT renumber them differently.

DEC-079
--------
Title:
Development Path and Phase-6 Entry Criteria

Use the revised content below.

DEC-079 D79-5

Use exactly this formulation:

D79-5
PHASE 5 is complete only when the P2/K3 gate structure established by DEC-080 has been fully designed, dispositioned, and separately locked by an explicit owner DEC, with no unresolved Phase-6-blocking architectural question.

DEC-080 is NOT itself the P2/K3 lock.

The eventual P2/K3 lock MUST be a separate explicit owner DEC.
```

Decision text (D79-1 … D79-9, adopted by the authorization above):

```text
D79-1  DEC-025 PHASE 6 "completed persistence/audit/lifecycle gates" means the applicable gates are
       explicitly completed or locked by owner DEC. Drafting, design or committed documentation
       alone does not satisfy Phase-6 entry.
D79-2  The applicable gates are: §19 (locked by DEC-075); §21 (locked by its own lock DEC under
       DEC-071); §22 (locked by its own lock DEC under DEC-076, with the required pre-lock scope of
       DEC-076 D76-3 decided, and the DEC-078 route established before any §22 lock that leaves
       items open).
D79-3  The minimum lifecycle scope before Phase 6 is DEC-076 D76-3: Local Root Operator bootstrap
       authority; first `scc.administrator` membership mechanics; K9 bootstrap mechanics and
       authentication; the P11 K9 → K4 interface as the bootstrap act requires it; the bootstrap
       audit record under §21. No temporary web bootstrap (DEC-021).
D79-4  K11 installer placement is outside that scope. It remains on the OQ-6 route (recovery gate =
       §22, DEC-077). It may be required for a runnable deployment.
D79-5  PHASE 5 is complete only when the P2/K3 gate structure established by DEC-080 has been fully
       designed, dispositioned, and separately locked by an explicit owner DEC, with no unresolved
       Phase-6-blocking architectural question.
       DEC-080 is NOT itself the P2/K3 lock.
       The eventual P2/K3 lock MUST be a separate explicit owner DEC.
D79-6  ODF-18-06 (request-bound assertions) is NON-BLOCKING and belongs to the Platform Adapter
       gate. It does not block P2 lock, §21, §22 or Phase 6, and requires no §15/§16/§17 amendment.
       It is not a Phase-5 prerequisite.
D79-7  CyberPanel K2 implementation is not required to declare the platform-neutral P2/K3
       architecture complete.
D79-8  OD19-01 remains unresolved (DEC-051 R01b coordination). It blocks actual
       assertion-verification implementation, not the abstract K4 authorization-and-audit core.
D79-9  The DEC-024/DEC-025 sequencing is preserved. No implementation authority is created. DEC-029
       remains standing. §15–§17 are unchanged.
```

> **Transcription note (session process):** The decision text is the owner-supplied text of the adoption-preparation
> message, laid out in the log's indented format without changing its words. D79-5 uses the formulation given in the
> adoption authorization. The authorization's other sections (application rules, file requirements, prohibited
> changes, validation, commit rule) governed only this change set and are omitted.

> **Index note (not owner wording):** DEC-079 interprets DEC-025 Phase-6 entry. It creates no implementation
> authority; Phase 6 is not entered.

---

## DEC-080 — P2/K3 Gate Structure

- **Status:** CURRENT (adopted — P2/K3 gate structure; not locked)
- **Source:** Owner adoption authorization for DEC-071 … DEC-080 (2026-09-30), applying the owner-approved
  decision set of the adoption-preparation pass and the owner rulings of the §21, §19-lock, §22 and P2/K3
  drafting passes.
- **Related:** DEC-025 (PHASE 5); DEC-026; DEC-051; DEC-079; §15.6; §15.10; §15.12; §17.2; §17.22; CyberPanel K2 gate

```text
I now authorize application of that exact adoption change set, subject to the controls below.

Apply DEC-071 through DEC-080 exactly as reviewed.

Final numbering:

DEC-071 — §21 Scope and Gate Structure
DEC-072 — ODF-18-07 Disposition
DEC-073 — F19-05 Index Treatment
DEC-074 — §19 Locked Form
DEC-075 — §19 Lock
DEC-076 — §22 Scope and Gate Structure
DEC-077 — Recovery Gate Identity
DEC-078 — §22 Post-Lock Route
DEC-079 — Development Path and Phase-6 Entry Criteria
DEC-080 — P2/K3 Gate Structure

Do NOT renumber them differently.

DEC-080
--------
Title:
P2/K3 Gate Structure

Use the previously drafted DEC-080 content exactly in substance.
```

Decision text (D80-1 … D80-9, adopted by the authorization above):

```text
D80-1  Authority. Designed under DEC-025 PHASE 5 and DEC-026, within locked §15.6, §15.10 (P2, P3),
       §15.12, T-31, §17.2 and §17.22. No new gate beyond the P2 gate DEC-026 establishes; its scope
       is stated here.
D80-2  P2 scope (K2 → K3). The platform-neutral protocol elements of DEC-026: message format;
       assertion format and contents sufficient for the §17 Authentication Context (assertion ID,
       platform, subject, authentication time, method claims) and lifetime (§15.18 OQ-3); audience
       binding; nonce/session binding; freshness and replay resistance; request binding as locked
       §15.10 states it (not bound to request content); error model; transport (local-only);
       endpoint exposure (T-31); and the signing-/verification-key relationship and rollover model
       at protocol level (DEC-051 R01h).
       Excluded: DC-18 storage and provisioning (OD19-01), which remain in DEC-051 coordination.
D80-3  K3 service-boundary scope (P3, K3 → K4). The contract details locked text leaves open: the
       request envelope carrying an assertion or SCC session token; the limits of K3's structural
       (shape) validation, which is not a security control; relay semantics; behavior when K4 is
       unavailable (no stale state presented as current); prohibited K3 persistence, caching and
       logging (§15.6; T-19); SCC session semantics and whether session validation state is durable
       (§19.22 → P2). The request-ID semantics of state-changing requests remain §16/§17 matters
       ("details §16/§17") and are referenced, not redefined.
D80-4  Identity flow. K2 → K3 → K4. K4 verifies end-to-end and derives the Authentication Context
       (§17.2; §17.22 step 1). K3 performs no authorization and does not mint or alter identity. K2
       has no direct path to K4, K5 or K6.
D80-5  Platform neutrality. The contract accommodates both K2 relay and a platform-supported proxy
       route (§15.6: "an adapter choice"). CyberPanel K2 gate questions (K2-Q1 … K2-Q7, including
       presentation placement KF-01/KF-02, installation and re-registration, `platform_subject_id`
       stability P-6, OQ-1) are not decided here. Presentation-content design is excluded.
D80-6  Excluded items. ODF-18-06 stays with the Platform Adapter gate (NON-BLOCKING). OD19-01 stays
       with the DEC-051 coordination. CHANGE-023 stays unresolved.
D80-7  Process. Candidate (expanding open/p2-protocol.md) → owner dispositions (DEC entries, DEC-030
       Q4) → a separate lock DEC. No partial lock. No post-lock route is created now. The candidate
       closes every P2/K3-owned normative item; if one would remain open, it returns to the owner.
D80-8  Phase-5 lock criteria. The P2/K3 gate may be locked when:
       1. every D80-2 element is specified or explicitly deferred to an established gate;
       2. every D80-3 item is specified within locked §15.6/§15.10;
       3. the delivered assertion supports every §17.22 step-1 check and every §17 Authentication
          Context field;
       4. no CyberPanel-specific K2 question is decided, and both relay and proxy routes remain
          admissible;
       5. no accepted decision widens authority, transfers responsibility between K2–K11,
          contradicts §15–§17, or makes an unauthorized amendment; K3 gains no authorization,
          identity or state authority;
       6. every deferral names an established owning gate;
       7. no implementation authority is created, and the lock is a separate explicit owner DEC.
D80-9  Non-effects. No §15–§17 amendment. No implementation authority; DEC-029 stands. K2/K3
       implementation remains subject to this gate's lock (DEC-026) and, for CyberPanel, the
       CyberPanel K2 gate ("Implementation prohibition until this gate answers K2-Q1").
```

> **Transcription note (session process):** The decision text is the owner-supplied text of the adoption-preparation
> message, laid out in the log's indented format without changing its words. The authorization's other sections
> (application rules, file requirements, prohibited changes, validation, commit rule) governed only this change set
> and are omitted.

> **Index note (not owner wording):** DEC-080 is the P2/K3 gate structure, not the P2/K3 lock. The lock requires a
> separate explicit owner DEC (D79-5).

---

## DEC-081 — §19.3 Post-Lock Authority Statement

- **Status:** CURRENT (adopted — one-time explicit owner amendment of §19.3; DEC-023 hierarchy governs locked §19)
- **Source:** Owner authorization for DEC-081 (2026-09-30): ruling B(i) and confirmations 1–7, approving the
  reviewed DEC-081 draft and the exact §19.3 replacement.
- **Related:** DEC-023; DEC-063; DEC-064 (item 3); DEC-074 (D74-1); DEC-075 (D75-3, D75-4); §19.3; §19.23

```text
OWNER AUTHORIZATION

The owner has reviewed and approved DEC-081.

The owner has selected and LOCKED IN:

B(i) — DEC-023's authority hierarchy governs.

The owner has additionally confirmed:

1. DEC-081 is a ONE-TIME EXPLICIT OWNER AMENDMENT to §19.3.

2. DEC-081 does NOT create a general §19 amendment route.

3. §19.21–§19.22 items continue to use the existing DEC-075
   D75-3 / DEC-063 route.

4. A future post-lock §19 issue outside §19.21–§19.22 does NOT
   automatically acquire a route from DEC-081.

5. Such a future issue must return to the owner for an explicit
   decision.

6. DEC-081 is a procedural one-time authorization to amend §19.3.
   It is NOT an exception to the Category 1 authority hierarchy.

7. Category 2 does NOT gain authority to silently override Category 1.

EXACT §19.3 REPLACEMENT

Replace ONLY the first paragraph of §19.3 with exactly:

This document is Category 1 (locked architecture) from DEC-075 forward; its earlier Category 4 classification is
historical [DEC-075 D75-4; DEC-081]. Where it conflicts with §15, §16 or §17, those control. Otherwise the DEC-023
hierarchy governs: a decision-log entry does not supersede this text, and a change to it takes effect only when this
document is amended to match an owner decision [DEC-081]. The decision log is the authoritative record of the
complete owner wording [DEC-064]. Where this document conflicts with the foundational baseline, the baseline override
rule (DEC-014) and DEC-023 apply; conflicts are listed in §19.5.3. Historical material (forensic audit, §18 gate
review) is evidence only.

Do NOT modify the §19.3 heading.

Do NOT modify the next paragraph.

Do NOT modify §19.5.3.

Do NOT modify any other §19 text.

CRITICAL PROCEDURAL RULE

DEC-081 is a one-time explicit owner amendment.

It does NOT establish:

- a general §19 amendment procedure
- a new §19 post-lock route
- a generic architecture-change route
- an exception to DEC-023
- Category 2 override authority
- any new authority for K2–K11

D81-6 MUST remain exactly as drafted.

Do NOT add language saying that future §19 amendments may use
DEC-081.

Do NOT add a new route to the register.
```

Decision text (D81-1 … D81-10, adopted by the authorization above):

```text
D81-1  Authority and source basis. Owner ruling B(i) on the post-lock review of §19.3. Sources:
       DEC-023 ("When documents conflict, the higher authoritative category wins."); DEC-064
       item 3 ("The decision log is the authoritative record of the complete owner wording.");
       DEC-074 D74-1 (§19 locked in its existing form); DEC-075 D75-3 and D75-4.
D81-2  Problem. §19.3, locked in its existing form by DEC-074 D74-1, still states "This document is
       Category 4 (conditional/open)", states that the decision log controls where it conflicts with
       §19, and states that "this candidate does not override the baseline until locked". DEC-075
       D75-4 added §19 to Category 1. §19.3 is not an item in §19.21–§19.22, so DEC-075 D75-3 does
       not reach it.
D81-3  Category. §19 is Category 1 (locked architecture) from DEC-075 forward (DEC-075 D75-4). Its
       earlier Category 4 classification is historical.
D81-4  Precedence (owner ruling B(i)). The DEC-023 hierarchy governs locked §19. Where §19
       conflicts with §15, §16 or §17, those control. A Category 2 owner decision or decision-log
       entry does not supersede locked §19 text. The clause of §19.3 stating that the decision log
       controls where it conflicts with §19 is replaced by this provision. No §19-specific
       exception permitting Category 2 to override Category 1 is created.
D81-5  Decision log. The decision log remains the authoritative record of owner decisions, their
       complete wording and their history (DEC-064 item 3). That role does not make a decision-log
       entry a substitute for, or a direct override of, the resulting locked §19 text.
D81-6  Changes to locked §19. An owner decision that requires a change to locked §19 has
       architectural effect in §19 only when §19 is amended to match it. Items within DEC-075 D75-3
       use that route (the DEC-063 procedure). This decision creates no other route and does not
       alter DEC-063 or DEC-075 D75-3.
D81-7  Amendment made by this decision. This decision is the explicit owner decision identifying
       §19.3 and amending it to match D81-3 … D81-5. It amends §19.3's first paragraph only, as set
       out in D81-9. The statement that "this candidate does not override the baseline until
       locked" no longer applies after DEC-075 and is replaced by a reference to the baseline
       override rule (DEC-014) and DEC-023.
D81-8  Non-effects. DEC-023, DEC-064, DEC-074 and DEC-075 are unchanged and remain the historical
       record; DEC-023 is applied to §19, not rewritten, and was not written for §19. The Category 1
       and Category 2 definitions are unchanged. No amendment to §15–§17. §19.21–§19.22 and their
       routing are unchanged. §19's substantive persistence, secrets and data-lifecycle
       architecture, the §19 lock, §19.5.1 and §19.5.3 are unchanged. §18, §20, §21, §22, P2/K3
       and the CyberPanel K2 gate are unaffected. No component (K2–K11) gains or loses authority.
       This decision creates no general hierarchy rule for any other document.
D81-9  Documentation. §19.3 first paragraph replaced as follows; §19.23 gains a pointer row for
       DEC-081; the decision log gains this entry, its index row and header note; the README
       decision range becomes DEC-001 … DEC-081. No other file changes.
D81-10 No implementation authority. DEC-029 remains standing.
```

> **Transcription note (session process):** The decision text is the reviewed DEC-081 draft; its status line
> ("CANDIDATE — NOT ADOPTED") is omitted. The replacement text referred to in D81-9 is the EXACT §19.3 REPLACEMENT
> reproduced in the authorization above. The authorization's repository-state, mutation, §19.23, §19.25, decision
> log, README, files, forbidden-change, validation, commit and output sections governed only this change and are
> omitted.

> **Index note (not owner wording):** DEC-081 is a one-time explicit owner amendment of §19.3. It creates no general
> §19 amendment route and no exception to DEC-023; §19.21–§19.22 items continue to use DEC-075 D75-3 / DEC-063. It
> does not amend §15–§17 and authorizes no implementation.

---

## DEC-082 — §21 Audit Events Owner Dispositions

- **Status:** CURRENT (adopted — §21 owner dispositions; §21 not written, not locked)
- **Source:** Owner adoption authorization for DEC-082 (2026-09-30), adopting the reviewed DEC-082 Revision 3
  (with the owner's B1-A and R4 corrections) and confirming points 1–13; owner disposition responses for B1-A, R4,
  B-2, R-1, R-2, R-3 and R-5 (2026-09-30).
- **Related:** DEC-025; DEC-034; DEC-035; DEC-041; DEC-042; DEC-047; DEC-048; DEC-056; DEC-058; DEC-068 (D68-D);
  DEC-070; DEC-071; DEC-072; DEC-075 (D75-3); DEC-076; DEC-080; DEC-081; §15.10; §15.15; T-23; §17.9; §17.16;
  §17.18; §17.21; A-01; A-35; §19.21.2; §19.22

```text
OWNER RESPONSE — B1-A / R4

B1-A: APPROVE WITHOUT ENVELOPE CLAUSE

B1-B: OWNER DECISION REQUIRED
      [§16 via D68-D / §17 via new route / other]

B2: [A / B / C]

R1: [A / B]

R2-A: [YES / NO]
R2-B: [YES / NO]
R2-B-EVIDENCE: [if YES]
R2-C: [YES / NO]
R2-D: [YES / NO]
R2-E: [ACCEPT / DO NOT ACCEPT]

R3: [A / B / C]

R4: APPROVE CORRECTED WORDING
     "Any off-host survival depends on the external facility
     (DEC-072 D72-4) and cannot extend to content still on the
     host at the time of a compromise (§15.15)."

R5: [A / B / C]

OWNER RESPONSE — REMAINING DISPOSITIONS

B2:   C

R1:   B

R2-A: YES
R2-B: NO
R2-B-EVIDENCE: N/A
R2-C: NO
R2-D: NO
R2-E: ACCEPT

R3:   A

R5:   A

ADOPTION AUTHORIZATION

A.

Adopt the DEC-082 Revision 3 text I originally presented in the
previous review, with the B1-A and R4 corrections already incorporated
there.

Do NOT use the rewritten DEC-082 text from your previous message.
Discard that rewritten version entirely.

The original Revision 3 is the authoritative adoption text for this
step.

The following points are specifically confirmed:

1. D82-16 must preserve the locked §19.21.2 routing:
   - K8 lifetime identity in journal references remains a §16
     Amendment Gate item under §19.21.2 row 1.
   - K6 acceptance after K8 reinitialization remains a §16 Amendment
     Gate item under §19.21.2 row 2.
   - The K4-observation question may remain routed to §22 as specified
     in the original Revision 3, but this does not move the K8-side
     items out of their locked §16/lifecycle routing.

2. D82-6 / D82-11 must preserve the DEC-072 D72-5 relationship.
   The §21 export content includes the record identified by D72-5 as
   the anchor-legitimacy record.

   The terminology clarification in Revision 3 must NOT be interpreted
   as renaming, deleting, or superseding D72-5.

   The intended distinction is:
   - §21 defines an anchor-change observation record;
   - that record is the §21 representation supplied for the
     anchor-legitimacy record referenced by D72-5;
   - the observation does NOT assert that the observed change was
     legitimate;
   - no second anchor representation is created (05c = M);
   - preserve the relevant §17.21 / §15.15 limitations from Revision 3.

3. D82-21 must not contradict D82-13.
   D82-13's Job identity, K6 request IDs, and `p3_request_id` recording
   are deliberate §21 audit-record requirements established by the
   owner disposition.

   Therefore D82-21 must describe K4/K8 correlation as limited to the
   locked architecture while still allowing the additional §21 audit
   fields expressly established by D82-13.

4. Preserve the approved D82-4 distinction:
   - the sequence-gap claim assumes an honest K4 writer;
   - the K4/K8 cross-check detects discrepancies between K4 claims and
     K8 evidence;
   - neither protects against compromised K4 or root.

5. Preserve D82-5's status:
   The K8 tamper-evidence mechanism is NOT already assigned to §16.
   A separate owner decision is still required to make that assignment.

6. Preserve D82-8 in full:
   - explicit R0 `view` exception from §17.18;
   - denied R0 views follow the same rule;
   - R1+ are individually audited;
   - this does not amend §17;
   - this does not eliminate A-35 generally.

7. Preserve D82-9 exactly according to the approved dispositions:
   - A5 audit-write failure may use late recording;
   - denied operations remain refused;
   - denial handling gets the approved B-class condition record;
   - do NOT generalize late recording to every audit-write failure;
   - preserve the approved 08b = X and 08c = Q distinction.

8. Preserve D82-10's explicit statement:
   DEC-035 continues to govern and is not superseded.

9. Preserve D82-11's 10b = O wording:
   the anchor-change observation is observed by K4 unless independent
   evidence establishes who made the change.

10. Preserve D82-15:
    Local Root credential lifecycle returns to the owner under §22;
    there is no post-lock §21 amendment route.

11. Preserve D82-22:
    B1-B is NOT a blocker to the §21 lock.
    It affects the P2/K3 lock and Phase 6 as previously determined.
    Do not list B1-B as a §21 lock dependency.

12. Preserve D82-6's 05c = M disposition:
    no second anchor representation.

13. Preserve all citations/references present in the original
    Revision 3, including the §17.21 and §15.15 references where
    specified.

Do not reinterpret any of these points.
```

Decision text (D82-1 … D82-24, DEC-082 Revision 3, adopted by the authorization above):

```text
D82-1  Authority and scope. Owner dispositions of OQ21-01 … OQ21-18 from the §21 Gate Review
       and Owner Disposition Pass, as revised by the owner's review resolutions I-1 … I-9 and
       the owner's dispositions of findings B-1, B-2 and R-1 … R-5, under DEC-025 PHASE 3 and
       DEC-071 (D71-1 … D71-10). These dispositions are inputs to the §21 candidate. This
       decision does not write, lock or move §21, and is not the §21 lock DEC (DEC-071 D71-8
       criterion 6).
D82-2  OQ21-01 = A. "Durably recorded" (DEC-035 R5a; DEC-071 D71-2(b)) means: the audit record
       is committed to SD-K7 and survives both a K4 process restart and a host restart. This is
       the normative meaning for §21. It creates no general storage-engine specification.
D82-3  OQ21-02. (a) = A: every K4 audit record has an identity unique within the SCC instance, so
       that later records can refer to earlier records, including UNKNOWN resolution, late
       recording and B1 conditions. (b) = A: K4 audit records carry a monotonic sequence over
       audit records within the SCC instance, permitting §21 to define K4 audit sequence-gap
       detection. This provides no protection against a compromised K4. (c) is governed by D82-4.
       Continuity across K7 restoration: D82-19.
D82-4  OQ21-03 = A. SCC may claim (i) K4 audit sequence-gap detection and (ii) K4 ↔ K8
       cross-check detection, limited as follows: sequence-gap detection concerns loss
       detectable while the K4 writer is functioning honestly; the cross-check detects
       discrepancies between K4 execution claims and K8 evidence; neither claim detects arbitrary
       falsification by a compromised K4; neither provides protection against host or root
       compromise; K8 lifetime-gap representation remains outside §21 on its established
       lifecycle/recovery route; restore-related loss follows §22; retention-related
       resolvability follows the §21 retention rules (D82-7).
D82-5  OQ21-04. (a) = A: §21 defines no new on-host tamper-evidence mechanism for K4 audit and
       creates no integrity mechanism inside K7; §21 defines the scope and limitations of its
       tamper-evidence claim and the export content. (b) = X: the unresolved K8 tamper-evidence
       mechanism requires assignment to the §16 Amendment Gate by a separate owner decision under
       DEC-068 D68-D. §21 records only the dependency. This decision does not make that
       assignment (D82-20) and does not modify §16.
D82-6  OQ21-05 and findings R-1, R-3, R-4.
       (a) = A: the §21-defined export content consists of K4 audit records and the anchor-change
       observation records (D82-11). K8 journal records are not in the §21-defined export set;
       their format and authority remain governed by §16. The anchor-change observation records
       are the §21 content for the record named in DEC-072 D72-5; that name is not changed by
       this decision and does not imply that the records establish legitimacy or completeness.
       (b) = Q: the export uses an SCC-produced export artifact, which the external
       root-administered facility (DEC-072) consumes. The facility is not granted, and does not
       rely on, direct access to K7; T-23 is unchanged. The artifact is not an SCC authorization
       mechanism and confers no authority. §21 does not define the artifact's implementation.
       (R-1 = B) The artifact's permission and classification under §19 (S19-01) and its
       lifecycle follow the established §19.22 → DEC-075 D75-3 → DEC-063 route and §22 (DEC-072
       D72-6). The SCC-produced export artifact is not permitted to be produced until a D75-3
       §19 decision permits and classifies it.
       (R-3 = A) Failure to produce the artifact for an already-created K4 audit record produces
       a B-class condition record when possible. Artifact-production failure does not alter
       DEC-035 R5a or R5b, does not refuse audited operations, and creates no new fail-closed
       dependency; export remains optional (DEC-072 D72-1). Failure to create the K7 audit
       record remains governed by R5a/R5b; failure of the external facility is outside SCC
       (DEC-072 D72-4).
       (R-4) The export artifact is produced by K4 (identity C) from K7 audit records. It carries
       no greater evidentiary weight than the records it contains. It can be falsified by a
       compromised K4 or by root (§17.21; §15.15). Any off-host survival depends on the external
       facility (DEC-072 D72-4) and cannot extend to content still on the host at the time of a
       compromise (§15.15). It claims no completeness beyond what sequence-gap detection shows
       while the writer is honest (D82-4). It carries no provenance beyond its K4 production. It
       defines no cryptographic mechanism.
       (c) = M: the §17.9 anchor-change observation records are the only anchor representation in
       the export; no second, independent representation is created.
D82-7  OQ21-06. (a) = A: K4 audit has no time-based expiry in v1; audit records are retained for
       the life of the SCC instance. This is not a statement that records can never be removed:
       removal occurs only through an explicitly defined disposition consistent with DEC-042
       R12A-2, and there is no automatic time-based expiration rule. (b) = R1: while an audit
       record is authoritative and retained, its referenced K8 evidence is subject to DEC-041
       R11d and must remain resolvable for as long as the authoritative audit record requires the
       reference to remain resolvable. K8 lifetime loss, reinitialization or restoration is
       handled according to the established K8 lifecycle and §22 recovery semantics (DEC-048;
       DEC-047 R17g); a K8 lifetime ending is not itself an architectural contradiction. K8
       capacity is thereby coupled to audit retention; if K8 cannot retain required referenced
       evidence, the existing locked K6 refusal behavior applies (X-29; S19-07). (c) = U: one
       retention rule applies across the §21 audit classes; no class-specific periods in v1. No
       numerical retention period is set.
D82-8  OQ21-07. (a) = A and (b) = S. §17.18 is an explicit exception to the general A-35
       recording rule for R0 `view` decisions: R0 `view` authorization decisions are exempt from
       individual audit-record creation under §17.18. No aggregate audit record is required
       solely by §17.18. R1 and above remain individually audited. Denied R0 `view` decisions
       follow the same rule. Audit and K8-derived views remain R1 (§17.3; §17.5.3). This is an
       owner reading of locked §17.18; it does not amend §17, does not eliminate A-35 generally,
       and creates no R0 audit mechanism.
D82-9  OQ21-08. (a) = A: §21 defines the B1 audit-write-failure record contract; §22 defines the
       recovery and reconstruction procedure. (b) = X: when an A5 record could not be durably
       written, it is written late once durable recording is possible and is marked as
       late-recorded; the B1 record references the affected cancellation; this relies on D82-3(a).
       (c) = Q: if a denial's audit record fails to become durable, a B-class operational-
       condition record is written when possible; the denial remains a refusal. No authorization
       bypass is created; DEC-035 R5a, R5b and the existing fail-closed requirements are
       unchanged.
D82-10 OQ21-09 and findings B-2, R-5. SYSTEM observation authorization is an A-35 Intent
       Authorization and receives the required K4 audit record under the existing A-35 event
       model; no new event category is created. The observation data itself is not copied into
       the K4 audit record, and K4 is not made responsible for auditing observation content
       (A-35; §17.18). K8 remains the execution evidence for the resulting K6 request; if K8 is
       unavailable, the X-29 refusal behavior applies. State-changing SYSTEM cancellation remains
       A5.
       (B-2) Whether SYSTEM observation proceeds is settled by existing authority: it proceeds
       when K7 authorization data is unavailable (§17.1.1; §17.16), and DEC-035 imposes no
       audit-write dependency on ordinary SYSTEM observation. DEC-035 continues to govern and is
       not superseded. (B2 = C) When a SYSTEM observation authorization record cannot be durably
       recorded at the time, the original authorization record is written late once durable
       recording is possible and marked as late-recorded, and a B-class condition record records
       the audit-write failure and references it. If the pending record is lost before it can be
       written late, its reconstruction is a §22 recovery matter.
       (R-5 = A) The owner accepts, as a consequence of the adopted architecture, that
       individually audited SYSTEM observation authorizations (to which the §17.18 R0 `view`
       exception does not apply) grow audit volume under D82-7. Existing fail-closed behavior
       applies to audited HUMAN operations when capacity is exhausted; SYSTEM observation
       proceeds as stated above.
D82-11 OQ21-10. (a) = B: the §17.9 anchor-change observation record is a B-class record under
       DEC-071 D71-3(B) ("where an authoritative source requires one"; source: §17.9). (b) = O:
       the record is attributed as "observed by K4" unless the architecture has independent
       evidence establishing the actual changer; the change is not attributed to the Local Root
       Operator merely because only the Local Root Operator is authorized to make it. (c) = Y:
       the minimum locked fields remain the named Principal and the anchor digest (§17.9); §21
       adds observation metadata and must define at least the normative observation timestamp
       and the change kind. The record does not claim, and must not be presented as showing,
       that the change was legitimate, that it was complete, or that no unobserved change
       occurred. §17.9 is not modified.
D82-12 OQ21-11 and finding R-2. Failed authentication at K4 is a §21 B-class audit record,
       preserving baseline §10 "Failed authentication is audited". The record: (1) must not
       attribute the attempt to a Principal based solely on an unverified authentication
       assertion or claim (A-01); (2) may identify the authentication attempt and the failure
       reason; (3) must not store raw authentication assertions or bearer credentials.
       (4) Audit-noise control must not silently destroy required failed-authentication audit
       evidence, and (5) capacity protection must therefore operate without simply dropping
       required audit records. (R2-A = YES; R2-B = NO) §21 requires one audit record per
       failed-authentication attempt; aggregation of attempts is not permitted. (R2-C = NO) A
       refusal made by K4 before authentication processing, because of an audit or capacity
       admission control, is not itself an audited event. (R2-D = NO) Intake limiting before K4
       is not assigned to P2/K3 by this decision. (R2-E = ACCEPT) The owner accepts the
       availability consequence that unbounded failed-authentication volume can exhaust K4
       audit capacity, after which DEC-035 R5a can refuse audited HUMAN operations. Concrete
       parameters remain implementation-level within this contract (DEC-071 D71-5). The P2/K3
       gate remains responsible for transport and request failure semantics (DEC-080). K3 does
       not become an authorization component.
D82-13 OQ21-12 and finding B-1. (a) = A: K4 audit records the Job identity and the K6
       `request_id`(s). (b) = D: §21 defines now the correlation field `p3_request_id`: the
       request ID carried by a state-changing P3 request under §15.10, with semantics as
       established by the architecture that §15.10 designates (§16/§17). §21 records the value K4
       receives. It defines no generation, uniqueness, transport or lifecycle semantics and
       applies only to state-changing P3 requests. No post-lock §21 amendment is required for
       it. Where the P3 request-ID semantics are defined is not decided here (D82-22). The locked
       and adopted fields remain: `authorization_ref`; Plan reference; `plan_digest`; K8
       lifetime identity / `journal_seq` reference (§17.18; DEC-048 R18c).
D82-14 OQ21-13: no owner decision. Derived: §17.18 requires "Conditions evaluated, with their
       values." The field set approved by this decision introduces no DC-05 dependency (DEC-056
       R06i).
D82-15 OQ21-14 = B. Local Root Operator credential-lifecycle acts are left to §22 (DEC-076 D76-2);
       §21 defines no record contract for them in this gate. If §22 later determines that a §21
       contract is required, the matter returns to the owner; no general post-lock §21
       amendment route exists.
D82-16 OQ21-15 = B. K8 lifetime-change observation is left to §22. The §21 candidate may identify
       the dependency but defines no K4 event for it. The K8-side architecture remains on its
       established §16/lifecycle routing (§19.21.2 rows 1–2). §16 is not modified.
D82-17 OQ21-16 = A. The unresolved question of K8 digests of credential-bearing content (DEC-058;
       DEC-070 D70-D3(4)) requires assignment to the §16 Amendment Gate by a separate owner
       decision under DEC-068 D68-D. §21 records only the dependency. This decision does not make
       that assignment (D82-20) and does not modify §16.
D82-18 OQ21-17 and OQ21-18: no owner decision; not §21 questions. CHANGE-023 remains unresolved
       and outside §21 (DEC-071 D71-7). The conditional §18 rewrites (SC-17; T-18-09 / SR-12
       scoping; SC-09; SRF-18-11; SR-13, SR-14) remain §18 work (DEC-072 D72-8); no conditional
       §18 material becomes §21 authority.
D82-19 K7 restoration and audit identity. Audit record identity and sequence semantics must
       remain unambiguous across K7 restoration. A K7 restore may roll K7 state backward
       (DEC-047 R17g); §21 must not assume that restarting the sequence from the restored K7
       state preserves uniqueness or continuity, and the §21 contract must require that audit
       identity and sequence remain unambiguous across restoration. §21 does not design a K7
       lifecycle mechanism or define a restore-generation implementation; the representation of
       restore or lifecycle generations belongs to the established lifecycle/recovery
       architecture, including §22. The §21 candidate must identify this as a §22 dependency.
D82-20 §16 Amendment Gate assignments. DEC-082 does not make either §16 Amendment Gate assignment
       named in D82-5(b) (K8 tamper-evidence mechanism) and D82-17 (K8 digests of credential-
       bearing content). Separate owner decisions under DEC-068 D68-D are required. They must be
       completed before the §21 lock where DEC-071 D71-8 criterion 5 requires them as owning
       routes.
D82-21 Boundaries. §21 owns the K4 audit contract. §21 does not own K8 architecture and does not
       redefine K8 events or fields (DEC-071 D71-9). §21 defines the audit ↔ K8 correlation
       contract without merging K7 and K8 into one store (DEC-034). Recovery and lifecycle
       procedures are §22's. K8 architectural changes belong to the §16 Amendment Gate where
       explicitly assigned. P2 request and assertion semantics are P2/K3's (DEC-080). §18 remains
       conditional.
D82-22 Dependencies. D82-20 (separate §16 Amendment Gate assignments). D82-6(b) (a D75-3 §19
       decision before any export artifact is produced; §22 for lifecycle, DEC-072 D72-6).
       D82-13(b) (the location of P3 request-ID semantics under §15.10 remains an open owner
       decision; any §16 location requires a D68-D assignment, and §17 has no amendment route;
       this affects the P2/K3 lock and Phase 6, not the §21 lock). D82-9(a), D82-10, D82-15,
       D82-16, D82-19 (§22). D82-7(b) couples K8 retention and capacity to audit retention
       (DEC-041 R11d, R11e).
D82-23 Non-effects. No amendment to §15 (including T-23 and §15.10), §16, §17 (including §17.9
       and §17.18) or locked §19. DEC-001 … DEC-081, including DEC-035 and DEC-080, are
       unchanged. No component (K2–K11) gains authority; the export facility gains no SCC
       authority or K7 access. No §21 post-lock route is created. §21 is not written, locked or
       moved.
D82-24 No implementation authority. DEC-029 remains standing.
```

> **Transcription note (session process):** The decision text is the reviewed DEC-082 Revision 3 exactly as
> presented for adoption; its status line ("CANDIDATE — NOT ADOPTED") is omitted. The owner's filled-in response
> templates are reproduced as sent; option letters are defined in the preceding owner-disposition passes. The
> authorization's repository-state, procedure, do-not-modify, validation, commit and report sections governed only
> this change and are omitted. A rewritten DEC-082 text proposed during the adoption exchange was rejected by the
> owner and is not recorded here.

> **Index note (not owner wording):** DEC-082 records owner dispositions for the §21 gate. It does not write, lock or
> move §21, does not make the §16 Amendment Gate assignments named in D82-20, does not make the D75-3 §19 decision
> for the export artifact, does not amend §15–§17 or locked §19, and authorizes no implementation.

---

## DEC-083 — Assignment of the K8 tamper-evidence mechanism to the §16 Amendment Gate

- **Status:** CURRENT (adopted — item assigned, scope A1; gate NOT SCHEDULED; undecided)
- **Source:** Owner selection of Gate A = A1, Gate B = B2 and the registration instruction (2026-09-30); owner
  D84-3 choice (ii) and adoption authorization for DEC-083 and DEC-084 (2026-09-30).
- **Related:** DEC-068 (D68-C, D68-D, D68-G, D68-J); DEC-071 (D71-8, D71-9); DEC-072; DEC-082 (D82-4, D82-5, D82-20); §15.3 (K8); T-12; §16.15 Q-3; register §5B

```text
OWNER SELECTION

Gate A — K8 Tamper-Evidence Mechanism:
A1

Gate B — K8 Credential-Bearing Digest Handling:
B2

Registration:
Record each assignment in the owner decision and add a pointer in
register §5B. Do not modify locked §19.21.2.

ADOPTION AUTHORIZATION

Now adopt DEC-083 and DEC-084 exactly as drafted, with that D84-3
owner choice incorporated.
```

Decision text (D83-1 … D83-4, adopted by the authorization above):

```text
D83-1  Assignment. Under DEC-068 D68-D, the owner assigns to the §16 Amendment Gate the item
       "K8 tamper-evidence mechanism" (DEC-082 D82-5(b), D82-20).
D83-2  Scope (A1). The item covers whether any K8 tamper-evidence mechanism is adopted,
       including: that no mechanism beyond the locked K8 properties (append-only, root-owned,
       X-29) is adopted; an in-K8 integrity property maintained by K6; and K8 content made
       available for off-host evidence through the external facility of DEC-072. Any
       mechanism's claims are limited by the fact that K6 and root write K8 (§15.3; T-12).
D83-3  Registration. The item is registered by this decision and by a pointer in register §5B.
       Locked §19.21.2 is not modified.
D83-4  Non-effects. This decision does not convene the gate (D68-C), decide the item (D68-G),
       authorize any §16 amendment (D68-J), change §16.15 Q-3 or §19.21.2, assign anything to
       §21 (DEC-071 D71-9), change DEC-072 or DEC-082, or create implementation, host or K6
       authority. DEC-029 remains standing.
```

> **Transcription note (session process):** The decision text is the reviewed candidate exactly as drafted; its
> status line ("CANDIDATE — NOT ADOPTED") is omitted. The authorization's verification, preservation,
> validation, commit and report sections governed only this change and are omitted.

> **Index note (not owner wording):** DEC-083 is an assignment decision only. It does not convene the §16 Amendment
> Gate, decide the item, amend §16, modify §19.21.2 or §21, or create implementation authority.

---

## DEC-084 — Assignment of K8 credential-bearing digest handling to the §16 Amendment Gate

- **Status:** CURRENT (adopted — item assigned, scope B2; D70-D3(4) "additional" reading closed; gate NOT SCHEDULED; undecided)
- **Source:** Owner selection of Gate A = A1, Gate B = B2 and the registration instruction (2026-09-30); owner
  D84-3 choice (ii) and adoption authorization for DEC-083 and DEC-084 (2026-09-30).
- **Related:** DEC-058; DEC-068 (D68-C, D68-D, D68-G, D68-J); DEC-070 (Path A, D70-A3, D70-D3(2), D70-D3(4)); DEC-071 (D71-8, D71-9); DEC-082 (D82-17, D82-20); X-26; §16.7; §16.10.2; register §5B

```text
OWNER SELECTION

Gate A — K8 Tamper-Evidence Mechanism:
A1

Gate B — K8 Credential-Bearing Digest Handling:
B2

Registration:
Record each assignment in the owner decision and add a pointer in
register §5B. Do not modify locked §19.21.2.

OWNER CHOICE — D84-3

Choose (ii).

The owner closes the DEC-070 D70-D3(4) "additional digests or evidence"
reading as not pursued.

The reason is that the repository does not define a sufficiently
bounded substantive item for that reading: it identifies neither the
additional evidence nor its purpose. It therefore should not remain as
an unrouted §16 / §21 dependency.

This closure does NOT:

- reopen DEC-070 Path A;
- modify D70-A3;
- modify R12B-1;
- authorize content inspection;
- authorize a runtime detector or classifier;
- prohibit a future separately defined architecture question;
- decide the substantive B2 gate question;
- amend §16;
- amend §19;
- amend §21.

D84-3 should therefore state that the DEC-070 D70-D3(4)
"additional digests or evidence" reading is not pursued and is closed
by DEC-084.

ADOPTION AUTHORIZATION

Now adopt DEC-083 and DEC-084 exactly as drafted, with that D84-3
owner choice incorporated.
```

Decision text (D84-1 … D84-5, adopted by the authorization above):

```text
D84-1  Assignment. Under DEC-068 D68-D, the owner assigns to the §16 Amendment Gate the item
       "K8 digests of credential-bearing content" (DEC-058; DEC-082 D82-17, D82-20).
D84-2  Scope (B2). The item covers whether the existing K8 digests (§16.10.2 parameter and
       pre-/post-state digests; §16.7 read content digests) are retained unchanged or reduced
       for resources declared credential-bearing by the applicable execution contract.
       "Credential-bearing" has the declaration-based meaning of DEC-070 D70-A3. No content
       inspection, runtime detector or classifier is authorized (DEC-070). The undeclared-`blob`
       residual (DEC-070 D70-D3(2)) is not within this item.
D84-3  The DEC-070 D70-D3(4) "additional digests or evidence" reading is not pursued; the owner
       closes it by this decision.
D84-4  Registration. The item is registered by this decision and by a pointer in register §5B.
       Locked §19.21.2 is not modified.
D84-5  Non-effects. This decision does not convene the gate, decide the item, reopen DEC-070
       Path A, D70-A3 or R12B-1, amend X-26, §16.7 or §16.10.2, authorize any §16 amendment
       (D68-J), or create implementation authority. DEC-029 remains standing.
```

> **Transcription note (session process):** The decision text is the reviewed candidate exactly as drafted; its
> status line ("CANDIDATE — NOT ADOPTED") is omitted. D84-3 records the owner's choice (ii) in place of the bracketed alternatives of the draft. The authorization's verification, preservation,
> validation, commit and report sections governed only this change and are omitted.

> **Index note (not owner wording):** DEC-084 is an assignment decision only. It does not convene the §16 Amendment
> Gate, decide the item, amend §16, modify §19.21.2 or §21, or create implementation authority.

---

## DEC-085 — §21 Audit Events Lock

- **Status:** CURRENT (adopted — §21 LOCKED; Category 1 from DEC-085)
- **Source:** Owner dispositions of the §21 candidate review (2026-09-30, 2026-10-01): C1–C4, C6, C7 and the
  approvals F-1, F-2, §21.14, §21.15; owner choices D85-8 … D85-10 (2026-10-01); owner adoption authorization.
- **Related:** DEC-023; DEC-025; DEC-035; DEC-071 (D71-1 … D71-9); DEC-072; DEC-075 (D75-3, D75-4, D75-5); DEC-076;
  DEC-079; DEC-080; DEC-081; DEC-082; DEC-083; DEC-084; §17.9; §17.16; §17.18; §17.22; current/21-audit-events.md

```text
OWNER DISPOSITIONS — §21 CANDIDATE REVIEW (2026-09-30)

3. Apply these owner dispositions exactly
OQ-C1 — A7 scope

CLOSED — (a).

A7 K6-reported outcome records cover K6 requests issued as Job steps only.

Therefore:

§17.22 step 14 Job execution outcomes are A7.
SYSTEM observation requests do not receive an A7 merely because K4 issued a K6 request.
SYSTEM observation authorization remains A1 under §21.13.
K8 remains the execution evidence for SYSTEM observation.
Observation content is never copied into §21.
Do not create a second SYSTEM-observation outcome event.

Update all affected wording, tables, consequences, and adversarial findings so there is no remaining ambiguity.

OQ-C2 — A7 write failure

CLOSED — (a).

If K4 cannot durably record an A7 K6-reported outcome:

the Job does not proceed to its next step;
the Job does not reach a terminal state requiring that A7 record;
there is no A7 late-recording mechanism;
do not extend B1/R5b late-recording semantics to A7;
K8 remains execution evidence;
K4 does not treat the Job as having progressed past the point requiring the A7 record.

Do not broaden this into a general statement that every K6 request is audit-fail-closed.

Update §21.6, §21.11, §21.12 and all relevant dependency/adversarial material.

OQ-C3 — Bootstrap record

CLOSED — (a).

The bootstrap A6 record shall contain:

actor_type = Local Root Operator;
authority_basis = Local Root Operator bootstrap authority (A-07);
an abstract Local Root Operator authentication reference.

The authentication-reference field must be defined only at the record-contract level by §21.

Its semantics and authentication mechanics belong to §22.

Use the same architectural pattern as p3_request_id:

§21 records the reference;
§22 later defines what the reference means and how authentication works.

Do not define Local Root Operator authentication mechanics in §21.

Update §21.6, §21.7, §21.14/§21.21/§21.22 where necessary, and downstream dependency wording.

OQ-C4 — Failed authentication identification

CLOSED — (b).

B2 may contain the claimed assertion ID only, explicitly marked unverified.

It must not:

establish Principal attribution;
establish authenticity of the assertion;
establish that the claimed subject is the actor;
contain the raw assertion;
contain bearer credentials.

Do not retain the claimed platform subject.

Make the distinction explicit between:

an unverified identifier of an authentication attempt, and
a verified/resolved Principal.

Update the B2 field contract and adversarial review accordingly.

OQ-C5

There is no OQ-C5.

The anchor change_kind vocabulary is a §21-owned proposal and is approved:

added
revoked
removed
modified

Preserve the existing conservative fallback where the §22 anchor representation cannot distinguish revoked from removed.

The record must not imply:

legitimacy;
authorization;
completeness;
absence of unobserved changes.
OQ-C6 — B1 denial-record failure

CLOSED — (a).

When a denial's own audit record cannot be durably written, B1 contains only the minimal failure-condition information:

condition kind;
time;
count;

plus the fields necessary for B1's own identity/sequence/recording metadata.

Do not reproduce:

Actor;
Principal;
capability;
targets;
full authorization data;
the original denial record.

Do not turn B1 into a late-recorded denial.

Preserve the distinction between:

“the denial record could not be written”

and

“a failure-condition record documenting that write failure was written.”

Update §21.12 and all affected review material.

4. Additional approved [C21] material

The owner also approves the following:

F-1 — Reason codes

Keep decision / reason_code as recorded audit information without creating a new normative closed reason-code vocabulary in §21.

Reason-code values remain non-normative §21 detail.

Do not create a new reason-code registry.

F-2 — Audit sequence

Approved:

audit_seq is recording order, not event order.

A late-recorded record receives its sequence position when it becomes durably recorded.

timestamp and recorded_at remain distinct.

Do not infer event chronology from audit_seq.

§21.14 verified assertion / failed Principal-state check

Approved.

If the assertion itself was verified and K4 actually resolves a Principal whose Binding or Principal-state check subsequently fails, the resolved Principal may be recorded as the Principal associated with the failed check.

This does not permit Principal attribution from an unverified claim.

§21.15 anchor vocabulary

Approved as above.

OWNER DISPOSITION — OQ-C7 (2026-10-01)

OQ-C7: (a)

When a B3 anchor-change observation record cannot be durably written,
K4 does not rely on the changed anchor set, for example for approval
verification, until the observation record is durable.

This does not create a late-recording rule for B3 and does not
supersede the separately approved A5/SYSTEM late-recording behavior.

OWNER CONFIRMATION — OQ-C7 INTERPRETATION (2026-10-01)

Confirmed: the interpretation of OQ-C7(a) is correct.

The §21 candidate shall mean:

- when a B3 anchor-change observation cannot be durably recorded,
  K4 does not treat the changed anchor set as established;
- K4 MUST NOT fall back to a stale, cached, previously observed, or
  assumed anchor set;
- §17.16's K11-anchors-unreadable behavior therefore applies:
  R4 is denied;
- no B3 late-recording rule is created;
- the separately approved A5/SYSTEM-observation late-recording behavior
  remains unchanged.

This is a reliance/authorization-state rule, not a claim that the anchor
change did not occur.

OWNER CHOICES — D85-8 … D85-10 (2026-10-01)

Owner choices:

D85-8 = A
D85-9 = A
D85-10 = A

Rationale/intent:

- §21 becomes Category 1 locked architecture prospectively, following
  the DEC-075 D75-4 precedent used for §19.
- The historical Category 4 classification remains historical; DEC-023
  is not rewritten.
- §21 moves from docs/architecture/open/ to
  docs/architecture/current/.
- §21 is locked in the completed candidate form itself.
- [OD] tags are replaced with references to DEC-085.
- Only the required status/header/location/tag bookkeeping changes.
- No substantive §21 wording is to be rewritten during this transition.

ADOPTION AUTHORIZATION (2026-10-02)

Adoption authorization:

I authorize adoption of DEC-085 exactly as proposed in the reviewed
dec085-adoption.diff, using the one-commit shape.

Use the D85-8 = A, D85-9 = A, and D85-10 = A choices exactly as
specified in the proposed adoption.

The adoption is authorized only for the reviewed change set:

1. Adopt DEC-085.
2. Move §21 from:
   docs/architecture/open/21-audit-events.md
   to:
   docs/architecture/current/21-audit-events.md
3. Apply the reviewed §21 lock/status/title/tag changes exactly.
4. Apply the reviewed README bookkeeping exactly.
5. Apply the reviewed §8 register bookkeeping exactly.
6. Preserve DEC-001 through DEC-084 exactly.
7. Do not modify §15, §16, §17, locked §19, §22, §18, P2/K3,
   CyberPanel/K2 material, or any other architecture text.
8. Do not perform the separate pointer-cleanup pass mentioned in your
   notes.
9. Do not alter the §21.22 "Blocks §21 lock?" column.
10. Do not make any additional cleanup, normalization, wording,
    formatting, or reconciliation changes.

Commit shape: ONE local commit containing the complete adoption.
```

Decision text (D85-1 … D85-13, adopted by the authorization above):

```text
D85-1  Authority and scope. This decision records the owner's §21 candidate-review dispositions
       and locks §21 under DEC-071 (D71-1, D71-8). It follows the candidate → owner dispositions →
       separate lock DEC pattern. Its subject is §21 only.
D85-2  Owner dispositions (candidate review). The following are recorded as owner decisions and
       form part of the §21 authority record:
       C1 = (a)  A7 K6-reported outcome records cover K6 requests issued as Job steps only. SYSTEM
                 observation requests and SYSTEM cancellation requests do not receive A7; SYSTEM
                 observation authorization remains A1; K8 remains the execution evidence for SYSTEM
                 observation; observation content is never copied; no separate SYSTEM-observation
                 outcome event exists.
       C2 = (a)  If an A7 record cannot be durably recorded, the Job does not proceed to its next step
                 and does not reach a terminal state requiring that record, and K4 does not treat the
                 Job as having progressed past that point. There is no A7 late-recording mechanism;
                 B1 and DEC-035 R5b semantics do not extend to A7. This applies to Job-step A7 records
                 only and does not make every K6 request audit-fail-closed.
       C3 = (a)  The bootstrap A6 record contains `actor_type` = Local Root Operator, `authority_basis`
                 = Local Root Operator bootstrap authority (A-07), and `lro_auth_ref`: "the Local Root
                 Operator authentication reference for the bootstrap act, with semantics as
                 established by §22 (DEC-076 D76-3(3)). §21 records the value K4 receives. It defines
                 no authentication mechanics, format or lifecycle."
       C4 = (b)  A B2 failed-authentication record may contain the claimed assertion ID only,
                 explicitly marked unverified. It does not establish Principal attribution, the
                 authenticity of the assertion, or that a claimed subject is the Actor, and contains no
                 raw assertion, no claimed platform subject and no bearer credential.
       C6 = (a)  When a denial's own record cannot be durably written, B1 contains only condition kind,
                 time and count, with its own identity, sequence and recording fields. It does not
                 reproduce the Actor, Principal, capability, targets, authorization data or the denial
                 record, and is not a late-recorded denial.
       C7 = (a)  When a B3 anchor-change observation record cannot be durably recorded, K4 does not
                 treat the changed anchor set as established and MUST NOT fall back to a stale, cached,
                 previously observed or assumed anchor set; §17.16's K11-anchors-unreadable behaviour
                 applies (R4 is denied). No B3 late-recording rule is created; the A5 and
                 SYSTEM-observation late-recording behaviour is unchanged. This is a reliance and
                 authorization-state rule, not a claim that the anchor change did not occur.
       There is no C5.
D85-3  Approved candidate content. Also recorded as owner decisions:
       F-1    `decision` and `reason_code` are recorded; §21 creates no closed reason-code vocabulary
              or registry; reason-code values are non-normative §21 detail.
       F-2    `audit_seq` is recording order, not event order; a late-recorded record receives its
              position when it becomes durably recorded; `timestamp` and `recorded_at` are distinct;
              event chronology is not inferred from `audit_seq`.
       §21.14 Where the assertion was verified and K4 resolved a Principal whose Binding or
              Principal-state check then failed, the resolved Principal may be recorded as the
              Principal associated with the failed check. This does not permit attribution from an
              unverified claim.
       §21.15 `change_kind` is `added`, `revoked`, `removed` or `modified`; where the §22 anchor
              representation cannot distinguish `revoked` from `removed`, K4 records the state it
              observed. The record does not imply legitimacy, authorization, completeness or the
              absence of unobserved changes.
D85-4  Completed candidate. The §21 candidate text, as reviewed by the owner on 2026-10-01,
       incorporates DEC-071, DEC-072, DEC-082, DEC-083, DEC-084 and D85-2 … D85-3, and has no
       unresolved §21-owned item.
D85-5  Lock criteria (DEC-071 D71-8). (1) Every §21-owned item is decided (DEC-082; D85-2; D85-3)
       or explicitly deferred to an established gate (D85-6). (2) ODF-18-07 is dispositioned
       (DEC-072). (3) The audit contract covers every A-35 event and every §17.18 field, with
       K6-reported outcome coverage limited by C1, and introduces no host-execution facts,
       observation content or credential material. (4) No accepted decision widens authority,
       transfers responsibility between K2–K11, contradicts §15–§17 or locked §19, or makes an
       unauthorized §15/§16 amendment. (5) Every genuine architectural deferral has an established
       owning route (D85-6). (6) No implementation authority is created, and this decision is the
       separate explicit owner lock DEC.
D85-6  Dependencies and deferrals. These are established routes and do not reopen the §21
       contract: the §16 Amendment Gate assignments DEC-083 (K8 tamper-evidence mechanism) and
       DEC-084 (K8 digests of credential-bearing content), the gate being NOT SCHEDULED; locked
       §19.21.2 rows 1–2 (K8 lifetime identity; K6 acceptance after K8 reinitialization); the
       DEC-075 D75-3 §19 decision required before any export artifact is produced (DEC-082 D82-6);
       the §22 recovery and lifecycle dependencies named in §21.22 (DEC-076); and conditional §18
       material (DEC-072 D72-8). External to §21 and not §21 deferrals: P3 request-ID semantics
       (B1-B), which affect the P2/K3 lock and Phase 6; and CHANGE-023, which remains outside §21
       (DEC-071 D71-7).
D85-7  Lock. §21 becomes locked architecture upon adoption of this decision.
D85-8  Authority category. From this decision forward, §21 is added to the locked-architecture
       authority tier (Category 1), supplementing DEC-023 prospectively as DEC-075 D75-4 did for
       §19. DEC-023 remains the historical record, and §21's earlier Category 4 classification
       remains historical. The hierarchy is supplemented prospectively, not rewritten.
D85-9  Documentation state. On adoption, §21 moves from docs/architecture/open/ to
       docs/architecture/current/, and its status header follows the locked-document convention.
D85-10 Locked form. §21 is locked in its completed candidate form, retaining its [DEC-0xx] and [L]
       tags. Each [OD] tag is replaced by a reference to DEC-085, and the status header and title
       are updated; no other text changes. No clean transcription is made.
D85-11 No post-lock route. This decision creates no post-lock §21 amendment route. A future change
       to locked §21 returns to the owner for an explicit decision.
D85-12 Non-effects. This decision does not lock, amend or change §15, §16, §17, locked §19, §22,
       §18, P2/K3 or the CyberPanel K2 gate; does not convene the §16 Amendment Gate or decide the
       DEC-083 or DEC-084 items; does not make the D75-3 §19 export-artifact decision; does not
       resolve B1-B or CHANGE-023; and does not declare Phase-6 readiness (DEC-079). DEC-001 …
       DEC-084 are unchanged. No component (K2–K11) gains authority.
D85-13 No implementation authority. §21 is locked as architecture, not implemented. DEC-029
       remains standing.
```

> **Transcription note (session process):** The decision text is the reviewed DEC-085 candidate with the owner's
> choices for D85-8, D85-9 and D85-10 (all A) in place of the bracketed alternatives; its status line ("CANDIDATE —
> NOT ADOPTED") is omitted. The owner messages are reproduced from their disposition sections; their verification,
> consistency-pass, report and repository-rule sections governed only those review steps and are omitted.

> **Index note (not owner wording):** DEC-085 locks §21 and moves it to current/. It does not lock or change §15–§17,
> §19, §22, §18 or P2/K3, does not decide the DEC-083 or DEC-084 items, creates no post-lock §21 route, and authorizes
> no implementation.

---

## DEC-086 — §22 Lifecycle / Recovery Lock

- **Status:** CURRENT (adopted — §22 LOCKED; bootstrap scope; Category 1 from DEC-086)
- **Source:** Owner dispositions of the §22 candidate, including OQ22-1 = (a) and the D22-A/B/C lock choices
  (2026-10-02); owner adoption authorization.
- **Related:** DEC-021; DEC-023; DEC-034; DEC-045; DEC-075 (D75-4); DEC-076; DEC-077; DEC-078; DEC-079; DEC-080;
  DEC-085 (C3, D85-8); §15 K9 and P11 rows; T-23; T-29; §17.1.3–§17.1.5; A-07; A-15; locked §21 A6;
  current/22-lifecycle-recovery.md

```text
OWNER DISPOSITIONS — §22 CANDIDATE (2026-10-02)

Owner dispositions for the §22 candidate:

OQ22-1: (a) YES.

The bootstrap act creates the first HUMAN Principal that receives the
first `scc.administrator` membership.

The Principal creation and membership creation are part of the same
narrow bootstrap act and commit atomically with the required A6 audit
record(s).

This is a narrowly scoped bootstrap authority under §22. It does NOT
create a general Principal-management capability and does NOT grant K9
general authority over K7, K4, memberships, roles, or other state.

Approve the candidate's proposed meaning of "first":

The bootstrap is available only when K7 contains no `scc.administrator`
membership record in any state. Re-establishing administration after
all administrators are lost is recovery, not bootstrap, and remains
open under DEC-078.

Approve the candidate's proposed §22 authority boundary:

The Local Root Operator may originate exactly the first
`scc.administrator` membership and nothing else.

Approve the candidate's proposed authentication model:

- the host operating system establishes that the P11 caller is root;
- K4 verifies that root identity on the host-local channel;
- no secret or bearer credential is introduced;
- `lro_auth_ref` is K4's reference to that determination;
- `lro_auth_ref` is not itself a credential and cannot be reused as
  authority;
- §22 does not define a format for `lro_auth_ref`.

Approve the proposed K9 boundary:

K9 relays the bootstrap request and result only.
K9 holds no bootstrap authority and does not access K7.

Approve the proposed P11 contract at the architectural level:

- K9 → K4 only;
- host-local;
- authenticated as the Local Root Operator through OS-enforced root
  identity;
- A-07 authority check;
- first-bootstrap precondition;
- replay rejection through the first-bootstrap precondition;
- schema validation;
- atomic failure;
- no fallback or bypass;
- no transport, encoding, endpoint, token or credential format is
  invented here.

Approve the proposed bootstrap audit behavior:

Use the already-locked §21 A6 contract unchanged.

Each bootstrap mutation receives its required A6 record, and the state
mutation and corresponding audit record commit atomically or neither
commits.

Approve all other [C22] architectural commitments in the candidate
exactly as written.

Do NOT resolve any O-1 … O-18 items. They remain open under DEC-078.

Do NOT resolve:

- recovery after loss of all administrators;
- restore generations;
- migration;
- K11 placement;
- Local Root credential acts beyond the bootstrap authentication
  mechanics;
- anchor mechanics;
- approver key custody;
- K7 backup/restore;
- rebuilding lost records;
- K8 lifecycle;
- removal/release keys;
- pre-image visibility;
- §16 Q-4/Q-5/Q-7;
- OD19-01;
- D71-6 hand-offs;
- DC-01/DC-02 ownership;
- export lifecycle.

Those remain explicitly open under DEC-078.

Use the same precedent as DEC-075/DEC-085:

D22-A:
- add §22 to Category 1 prospectively;
- earlier Category 4 classification remains historical.

D22-B:
- move the locked document from `docs/architecture/open/` to
  `docs/architecture/current/`.

D22-C:
- retain the existing decision/lineage tags in the locked document;
- replace candidate [C22] and [OQ22-1] markers with the adopted lock
  decision reference;
- update the status/header/title as required by the established locked
  document convention;
- make no substantive text changes beyond the explicitly authorized
  disposition/tag/header bookkeeping.

ADOPTION AUTHORIZATION (2026-10-02)

Adoption authorization:

I authorize adoption of DEC-086 exactly as proposed in the reviewed
dec086-adoption.diff, using the previously approved D22-A, D22-B, and
D22-C choices.

I explicitly approve the §22.1 wording change from:

"This candidate decides only..."

to:

"§22 decides only..."

This is authorized as locked-document status wording and does not expand,
narrow, or otherwise alter the substantive scope of §22.

The adoption is authorized only for the reviewed change set:

1. Adopt DEC-086.
2. Move:
   docs/architecture/open/22-lifecycle-recovery.md
   to:
   docs/architecture/current/22-lifecycle-recovery.md
3. Apply the reviewed §22 lock/header/title changes exactly.
4. Apply OQ22-1 = (a) exactly as approved.
5. Apply the approved [C22] → [DEC-086] substitutions exactly.
6. Apply the reviewed README bookkeeping exactly.
7. Apply the reviewed §8 register bookkeeping exactly.
8. Preserve DEC-001 through DEC-085 byte-identically.
9. Preserve O-1 … O-18 as open under DEC-078.
10. Do not resolve or modify any §22 item outside the reviewed
    disposition.
11. Do not modify §15, §16, §17, §19, or §21.
12. Do not modify DEC-083, DEC-084, or the §16 Amendment Gate.
13. Do not enter Phase 6 or create implementation authority.
14. Do not introduce a web bootstrap, K2/K3 path, secret or credential
    mechanism, K6 behavior, or K8 behavior.
15. Do not fix the DEC-021 Related-link issue in this commit.

The DEC-021 link is intentionally left unchanged because DEC-001 through
DEC-085 must remain byte-identical. Its eventual correction requires a
separate explicit authorization and is not part of DEC-086.

Commit shape: ONE local commit containing the complete reviewed adoption.
```

Decision text (D86-1 … D86-13, adopted by the authorization above):

```text
D86-1  Authority and scope. This decision records the owner's dispositions of the §22 candidate and
       locks §22 under DEC-076 (D76-3, D76-6, D76-7). §22 is the recovery gate (DEC-077). Its subject
       is §22 only.
D86-2  OQ22-1 = (a). The bootstrap act creates the first HUMAN Principal that receives the first
       `scc.administrator` membership. Principal creation and membership creation are part of the
       same narrow bootstrap act and commit atomically with the required A6 audit record(s). This
       is a narrowly scoped bootstrap authority under §22. It does not create a general
       Principal-management capability and does not grant K9 general authority over K7, K4,
       memberships, roles or other state.
D86-3  Approved candidate commitments. The owner approves every [C22] commitment of the §22
       candidate as written, including:
       (a) "first": the bootstrap act is available only while K7 holds no `scc.administrator`
           membership record in any state; re-establishing administration after every
           administrator is lost is recovery (§17.24 P-5), not bootstrap, and remains open;
       (b) authority: the Local Root Operator may originate exactly the first `scc.administrator`
           membership and nothing else;
       (c) authentication: the host operating system establishes that the P11 caller is root and
           K4 verifies that root identity on the host-local channel; no secret or bearer credential
           is introduced; `lro_auth_ref` is K4's reference to that determination, is not a
           credential, cannot be reused as authority, and has no format defined by §22;
       (d) K9: relays the bootstrap request and result only, holds no bootstrap authority and does
           not access K7;
       (e) P11, at the architectural level: K9 → K4 only; host-local; authenticated as the Local
           Root Operator through OS-enforced root identity; A-07 authority check; first-bootstrap
           precondition; replay rejection through that precondition; schema validation; atomic
           failure; no fallback or bypass; no transport, encoding, endpoint, token or credential
           format;
       (f) audit: the locked §21 A6 contract unchanged; each bootstrap mutation receives its
           required A6 record, and the mutation and its record commit atomically or neither does.
D86-4  D76-3 decided. D76-3 (1) Local Root Operator bootstrap authority (§22.3); (2) first
       `scc.administrator` membership mechanics, including creation of the first HUMAN Principal
       (§22.4; D86-2); (3) K9 mechanics and Local Root Operator authentication, including the
       meaning of `lro_auth_ref` (§22.5); (4) the P11 K9 → K4 interface for bootstrap (§22.6); and
       (5) the bootstrap audit record under locked §21 A6 (§22.7) are decided.
D86-5  Open items. O-1 … O-18 of §22.8 are recorded OPEN in locked §22 and are resolved only through
       DEC-078. This decision resolves none of them.
D86-6  Lock criteria (DEC-076 D76-7). (1) Every D76-3 item is decided (D86-4). (2) Every other
       §22-owned item is recorded as open under DEC-078 (D86-5). (3) No accepted decision widens
       authority, transfers responsibility between K2–K11, contradicts §15–§17, or makes an
       unauthorized §15/§16/§17 amendment; the bootstrap authority is limited by D86-2 and D86-3(b).
       (4) No web-reachable recovery or bootstrap path is created (T-29; DEC-021). (5) Every deferral
       names its owning route (§22.8; DEC-078). (6) No implementation authority is created, and this
       decision is the separate explicit owner lock DEC.
D86-7  Lock. §22 becomes locked architecture upon adoption of this decision.
D86-8  Authority category. From this decision forward, §22 is added to the locked-architecture
       authority tier (Category 1), supplementing DEC-023 prospectively as DEC-075 D75-4 and DEC-085
       D85-8 did. DEC-023 remains the historical record, and §22's earlier Category 4 classification
       remains historical. The hierarchy is supplemented prospectively, not rewritten.
D86-9  Documentation state. On adoption, §22 moves from docs/architecture/open/ to
       docs/architecture/current/, and its status header follows the locked-document convention.
D86-10 Locked form. §22 is locked in its candidate form with the D86-2 disposition applied, retaining
       its [DEC-0xx] and [L] tags. [C22] and [OQ22-1] markers are replaced by references to DEC-086,
       the OQ22-1 alternatives are replaced by the D86-2 disposition, and the status header and title
       are updated; no other text changes.
D86-11 Phase 6 and P2/K3. Locking §22 does not constitute Phase-6 entry (DEC-079). The first
       administrator can act only after its Platform Identity Binding is confirmed by a verified
       assertion; that operational path depends on the P2/K3 gate (DEC-080; DEC-079 D79-5) and on
       OD19-01 for actual assertion verification (DEC-079 D79-8).
D86-12 Non-effects. This decision does not amend or change §15, §16, §17, locked §19 or locked §21;
       does not change the §21 A6 contract; does not convene the §16 Amendment Gate or affect DEC-083,
       DEC-084 or §19.21.2; creates no web, K2 or K3 bootstrap or recovery path, no secret or
       credential mechanism, and no K6 or K8 behavior; and gives §22 and K9 no authority over K4
       (DEC-077 D77-3). DEC-001 … DEC-085 are unchanged. Post-lock changes to §22 use DEC-078 only.
D86-13 No implementation authority. §22 is locked as architecture, not implemented. DEC-029 remains
       standing.
```

> **Transcription note (session process):** The owner's disposition message is reproduced from its disposition and
> lock-choice sections (D22-A, D22-B, D22-C correspond to D86-8, D86-9, D86-10); its list of lock-decision
> requirements, verification list and repository rules governed only the preparation step and are omitted.

> **Index note (not owner wording):** DEC-086 locks §22 with the D76-3 bootstrap scope decided and O-1 … O-18 open
> under DEC-078. It does not enter Phase 6, does not change §15–§17, §19 or §21, and authorizes no implementation.

---

## DEC-087 — Assignment of P3 request-ID semantics to the §16 Amendment Gate

- **Status:** CURRENT (adopted — item assigned; gate NOT SCHEDULED; undecided)
- **Source:** Owner dispositions of the P2/K3 candidate (2026-10-02, two messages); owner adoption authorization.
- **Related:** DEC-068 (D68-C, D68-D, D68-G, D68-J); DEC-080 (D80-3, D80-8); DEC-082 (D82-13); §15.10 P3; register §5B

```text
OWNER DISPOSITION — B1-B (2026-10-02)

### B1-B

Choose R1.

Assign:

"P3 request-ID semantics referenced by §15.10"

to the existing §16 Amendment Gate under DEC-068 D68-D.

This establishes the owning route for B1-B.

It does NOT convene the §16 Amendment Gate.
It does NOT amend §16.
It does NOT define the P3 request-ID semantics now.

The P2/K3 contract must explicitly state that the semantics remain
deferred to that established §16 Amendment Gate route.

Do not create a new §17 amendment route.

Do not use R3.

The existing locked §21 `p3_request_id` field remains unchanged.

OWNER DISPOSITION — B1-B CONFIRMED (2026-10-02)

### B1-B

Choose R1.

Assign:

"P3 request-ID semantics referenced by §15.10"

to the existing §16 Amendment Gate under DEC-068 D68-D.

Adopt DEC-087 as part of the P2/K3 lock adoption.

DEC-087:

D87-1 assigns the P3 request-ID semantics to the §16 Amendment Gate.

D87-2 registers the item.

D87-3 preserves all stated non-effects:

- does not convene the §16 gate;
- does not define P3 request-ID semantics;
- does not amend §16 or §17;
- does not create a §17 amendment route;
- does not alter locked §21 `p3_request_id`;
- does not create implementation authority;
- DEC-029 remains in force.

The existing §21 `p3_request_id` field remains unchanged.

ADOPTION AUTHORIZATION

Adoption authorization:

I authorize adoption of DEC-087 and DEC-088 exactly as proposed in the
reviewed dec087-088-adoption.diff, with the reviewed correction that the
CBOR and Ed25519 choices are attributed to DEC-088 and not to DEC-026.

I authorize ONE local commit containing both DEC-087 and DEC-088.

DEC-087 is authorized exactly as proposed:

1. Assign "P3 request-ID semantics referenced by §15.10" to the existing
   §16 Amendment Gate under DEC-068 D68-D.
2. Register the assignment through the §5B register row.
3. Do not convene the §16 Amendment Gate.
4. Do not define the P3 request-ID semantics.
5. Do not amend §16 or §17.
6. Do not create a §17 amendment route.
7. Do not modify locked §21 `p3_request_id`.
8. Do not create implementation authority.
9. DEC-029 remains in force.

DEC-088 is authorized exactly as proposed:

1. Adopt the P2/K3 gate lock.
2. Complete the DEC-079 D79-5 / Phase-5 gate.
3. Do not enter Phase 6.
4. Do not create implementation authority.

The following are explicit owner choices under DEC-088 and must NOT be
attributed to DEC-026, DEC-044, DEC-051, DEC-080, or another prior
source:

- CBOR assertion encoding;
- Ed25519 assertion signatures;
- 60-second maximum assertion lifetime;
- Unix domain socket transport with OS peer-credential verification;
- stateful K4-owned SCC sessions;
- opaque, unsigned session tokens;
- volatile K4 session validation state;
- the §15.12 interpretation permitting transient K1/K2 session-token
  transit subject to the stated non-persistence, non-logging,
  non-minting, non-altering and non-authorizing restrictions.

The §15.12 interpretation is an owner reading of locked §15 text and is
NOT an amendment or override of §15.

The role fact is approved exactly as proposed:

- adapter-normalized;
- restrictive only;
- cannot independently grant authority;
- cannot widen K11;
- cannot bypass K4;
- cannot override K7;
- K3 does not evaluate it.

B1-B remains routed to the §16 Amendment Gate by DEC-087 and is not
resolved by DEC-088.

The following remain unresolved and routed exactly as stated in the
reviewed package:

- OD19-01;
- §22 O-4;
- CyberPanel K2 gate;
- ODF-18-06;
- §16 Amendment Gate;
- DEC-083;
- DEC-084;
- §19.21.2 items.

Do not modify or reopen §15, §16, §17, §19, §21 or §22.

Do not modify DEC-001 through DEC-086.

Do not modify the three flagged stale links/references:

1. DEC-026's protected Related line referencing
   `../open/p2-protocol.md`;
2. `docs/platforms/cyberpanel/k2-gate.md`'s reference to the old P2 path;
3. the existing register pointer rows OQ-3 and D-14.

Do not modify D80-7's historical/prose reference to
`open/p2-protocol.md`.

Those are separate documentation/pointer-cleanup work and are NOT part
of DEC-087/088.

The P2/K3 document may move from:

docs/architecture/open/p2-protocol.md

to:

docs/architecture/current/p2-protocol.md

with the reviewed locked-form changes.

Preserve the reviewed candidate text exactly except for the explicitly
authorized dispositions, lock bookkeeping, marker substitutions, title
and header changes.
```

Decision text (D87-1 … D87-3, adopted by the authorization above):

```text
D87-1  Assignment. Under DEC-068 D68-D, the owner assigns to the §16 Amendment Gate the item
       "P3 request-ID semantics referenced by §15.10" (§15.10 P3: "state-changing requests carry
       request IDs (details §16/§17)"; DEC-080 D80-3; B1-B).
D87-2  Registration. The item is registered by this decision and by a pointer in register §5B.
       Locked §19.21.2 is not modified.
D87-3  Non-effects. This decision does not convene the gate, define the semantics, amend §16 or §17,
       create a §17 amendment route, change locked §21's `p3_request_id`, or create
       implementation authority. DEC-029 remains standing.
```

> **Transcription note (session process):** The owner messages are reproduced from their disposition sections; their verification, preparation and repository-rule sections governed only those review steps and are omitted.

> **Index note (not owner wording):** DEC-087 is an assignment decision only. It does not convene the §16 Amendment Gate, define P3 request-ID
> semantics, amend §16 or §17, or create implementation authority.

---

## DEC-088 — P2/K3 Gate Lock

- **Status:** CURRENT (adopted — P2/K3 LOCKED; Phase 5 complete; Category 1 from DEC-088)
- **Source:** Owner dispositions of the P2/K3 candidate (2026-10-02, two messages); owner adoption authorization.
- **Related:** DEC-023; DEC-025; DEC-026; DEC-044; DEC-051; DEC-075 (D75-4); DEC-079 (D79-5); DEC-080; DEC-085 (D85-8);
  DEC-086 (D86-8); DEC-087; §15.6; §15.10; §15.12; T-13; T-19; T-20; T-30; T-31; §17.2; §17.22; A-04; current/p2-protocol.md

```text
OWNER DISPOSITIONS — P2/K3 CANDIDATE (2026-10-02)

Owner dispositions for the P2/K3 candidate:

### B1-B

Choose R1.

Assign:

"P3 request-ID semantics referenced by §15.10"

to the existing §16 Amendment Gate under DEC-068 D68-D.

This establishes the owning route for B1-B.

It does NOT convene the §16 Amendment Gate.
It does NOT amend §16.
It does NOT define the P3 request-ID semantics now.

The P2/K3 contract must explicitly state that the semantics remain
deferred to that established §16 Amendment Gate route.

Do not create a new §17 amendment route.

Do not use R3.

The existing locked §21 `p3_request_id` field remains unchanged.

### OQ-P1

Choose (b).

The P2/K3 protocol contract must be formally specified before
implementation, including:

- assertion encoding;
- signature algorithm;
- maximum assertion lifetime;
- transport mechanism.

However, do NOT invent concrete cryptographic, encoding, lifetime or
transport values merely to satisfy this disposition.

Use only choices supported by the governing architecture and adopted
decisions.

Where the existing sources establish a concrete value, preserve it.

Where the sources do not support a concrete value, identify the exact
remaining owner decision required rather than silently inventing one.

Preserve the existing DEC-051 key relationship and all §15 constraints.

Do not introduce a new credential or secret class.

### OQ-P2

Choose (b): STATEFUL SCC SESSIONS.

The contract must establish:

- an assertion can establish a K4-owned SCC session;
- K4 owns session validation state;
- K4 owns session invalidation;
- session lifetime is bounded by K4 policy;
- K3 holds no session authority or authorization state;
- session state is not recoverable through K3;
- no persistent signing secret is introduced by the session model;
- K3 never mints or alters an assertion or session token;
- K4 remains the authorization authority.

This choice preserves the admissibility of both relay and proxy routes.

Do not introduce stateless signed-session tokens.

Do not create a new signing-secret custody mechanism.

### OQ-P3

Choose (a): the assertion carries the adapter-normalized role fact.

The role fact must remain restrictive only.

It may restrict K4 authorization based on the platform-side role state,
but it cannot grant authority independently of K4's authorization state.

Preserve A-04.

Do not make K3 an authorization layer.

Do not allow a role claim to widen K11, bypass K4 authorization,
override K7 state, or otherwise grant authority.

### Candidate approval

Approve the candidate's [CP] passages, incorporating the above
dispositions and preserving all already-locked terminology.

Do not broaden the P2/K3 scope.

Do not modify §15, §16, §17, §19, §21 or §22.

Do not resolve OD19-01.

Do not resolve §22 O-4.

Do not resolve CyberPanel K2 questions.

Do not resolve the §16 Amendment Gate itself.

Do not define B1-B semantics in the P2/K3 document.

OWNER DISPOSITIONS — P2/K3 GATE (2026-10-02)

Owner dispositions for the P2/K3 gate:

These are explicit owner architectural choices. They are NOT claims that
the existing sources independently selected these concrete values.

### B1-B

Choose R1.

Assign:

"P3 request-ID semantics referenced by §15.10"

to the existing §16 Amendment Gate under DEC-068 D68-D.

Adopt DEC-087 as part of the P2/K3 lock adoption.

DEC-087:

D87-1 assigns the P3 request-ID semantics to the §16 Amendment Gate.

D87-2 registers the item.

D87-3 preserves all stated non-effects:

- does not convene the §16 gate;
- does not define P3 request-ID semantics;
- does not amend §16 or §17;
- does not create a §17 amendment route;
- does not alter locked §21 `p3_request_id`;
- does not create implementation authority;
- DEC-029 remains in force.

The existing §21 `p3_request_id` field remains unchanged.

### OQ-P1-E — assertion encoding

Choose:

CBOR.

The P2/K3 contract shall specify CBOR as the assertion encoding.

Do not introduce additional serialization formats.

### OQ-P1-A — signature algorithm

Choose:

Ed25519.

The assertion signature shall use Ed25519.

Preserve the existing asymmetric verification requirement:
the verifier cannot mint assertions.

Do not introduce symmetric signing or verification keys.

### OQ-P1-L — maximum assertion lifetime

Choose:

60 seconds maximum.

An assertion's validity window MUST NOT exceed 60 seconds from
`issued_at` to `expires_at`.

Preserve the existing freshness checks and single-use assertion-ID
requirement.

The 60-second value is an explicit owner decision; do not claim it was
derived from an existing source.

### OQ-P1-T — transport

Choose:

Unix domain socket with OS peer-credential verification.

The P2/K3 communication path shall use a host-local Unix domain socket
and OS-established peer identity.

There shall be no externally reachable listener for this protocol.

Do not introduce TCP, HTTP listener exposure, or another external
transport.

Do not define implementation-specific socket paths in the architecture
unless an existing source requires one.

### OQ-P2 — SCC sessions

Choose (b): STATEFUL SCC SESSIONS.

K4 owns:

- session validation state;
- session invalidation;
- session lifetime;
- authorization decisions involving the session.

K3 owns none of these.

SCC session tokens are opaque references and are not signed.

Do not introduce a session signing secret.

Do not implement stateless signed sessions.

### OQ-P4 — session validation-state durability

Choose (a): VOLATILE K4 STATE.

Session validation state exists only in K4 runtime state.

K4 restart terminates all active SCC sessions.

Do not place SCC session validation state in K7.

Do not modify locked §19 DC-19.

Do not create a new recovery mechanism for sessions.

Do not make sessions recoverable across K4 restart.

This deliberately keeps session durability out of the first
implementation path.

### OQ-P5 — session token transit through K1/K2

Choose (a).

Record this as an explicit owner interpretation of the locked §15.12
impact rule, NOT as an amendment to §15.

The interpretation is:

- a stateful SCC session token may be transiently present in K1/K2 while
  passing through the existing platform path;
- K1/K2 must not persist it;
- K1/K2 must not log it;
- K1/K2 must not mint it;
- K1/K2 must not alter it;
- K1/K2 must not independently authorize with it;
- K3 may transiently relay it within its already-locked boundary;
- K4 remains the sole authority for session validation and authorization.

The fact that K1/K2 compromise is root-equivalent does not create a new
trust boundary or authorization capability.

Do not interpret this decision as granting K1/K2 any SCC authorization
authority.

Do not amend §15.

If the candidate cannot express this as an owner reading of §15.12
without modifying locked text, STOP and report the exact conflict
rather than silently changing §15.

### OQ-P3 — role fact

Choose (a).

The assertion carries the adapter-normalized role fact.

The role fact is restrictive only.

It may restrict K4 authorization but cannot:

- grant authority independently of K4;
- widen K11;
- bypass K4;
- override K7 authorization state;
- create a role;
- create a Grant;
- substitute for K4 authorization.

K3 does not evaluate the role fact.

### Approval of candidate

Approve the candidate's [CP] passages, incorporating all dispositions
above.

Preserve all locked §15–§17 terminology.

Do not modify:

- §15;
- §16;
- §17;
- §19;
- §21;
- §22.

Do not resolve:

- OD19-01;
- §22 O-4;
- CyberPanel K2 gate;
- §16 Amendment Gate itself;
- §19.21.2 K8 lifetime items;
- DEC-083;
- DEC-084.

B1-B is only ROUTED, not solved.

### Important architectural distinction

The following are explicit owner decisions and must be identified as
such in the lock decision:

- CBOR;
- Ed25519;
- 60-second assertion maximum lifetime;
- Unix domain socket transport;
- volatile K4 session state;
- the §15.12 impact-rule interpretation for transient K1/K2 session
  token transit.

Do not attribute these concrete choices to DEC-026, DEC-044, DEC-051,
DEC-080, or any other source unless that source actually states them.

### D80-8

Re-evaluate every D80-8 criterion after these dispositions.

Criterion 1 must now be satisfied.

Criterion 2 must identify DEC-087.

Criterion 3 must cover the Authentication Context and §17.22 step-1
requirements.

Criterion 4 must be satisfied by stateful sessions and the explicit
P5 interpretation.

Criterion 5 must preserve the restrictive-only role fact.

Criterion 6 must identify DEC-087 / the §16 Amendment Gate as the
established route.

Criterion 7 remains a separate P2/K3 lock decision.

### Lock boundary

Adoption of the P2/K3 lock:

- completes the DEC-079 D79-5 / Phase-5 gate;
- does NOT enter Phase 6;
- does NOT authorize implementation;
- does NOT authorize K4 code;
- does NOT resolve OD19-01;
- does NOT resolve the CyberPanel K2 gate.

ADOPTION AUTHORIZATION

Adoption authorization:

I authorize adoption of DEC-087 and DEC-088 exactly as proposed in the
reviewed dec087-088-adoption.diff, with the reviewed correction that the
CBOR and Ed25519 choices are attributed to DEC-088 and not to DEC-026.

I authorize ONE local commit containing both DEC-087 and DEC-088.

DEC-087 is authorized exactly as proposed:

1. Assign "P3 request-ID semantics referenced by §15.10" to the existing
   §16 Amendment Gate under DEC-068 D68-D.
2. Register the assignment through the §5B register row.
3. Do not convene the §16 Amendment Gate.
4. Do not define the P3 request-ID semantics.
5. Do not amend §16 or §17.
6. Do not create a §17 amendment route.
7. Do not modify locked §21 `p3_request_id`.
8. Do not create implementation authority.
9. DEC-029 remains in force.

DEC-088 is authorized exactly as proposed:

1. Adopt the P2/K3 gate lock.
2. Complete the DEC-079 D79-5 / Phase-5 gate.
3. Do not enter Phase 6.
4. Do not create implementation authority.

The following are explicit owner choices under DEC-088 and must NOT be
attributed to DEC-026, DEC-044, DEC-051, DEC-080, or another prior
source:

- CBOR assertion encoding;
- Ed25519 assertion signatures;
- 60-second maximum assertion lifetime;
- Unix domain socket transport with OS peer-credential verification;
- stateful K4-owned SCC sessions;
- opaque, unsigned session tokens;
- volatile K4 session validation state;
- the §15.12 interpretation permitting transient K1/K2 session-token
  transit subject to the stated non-persistence, non-logging,
  non-minting, non-altering and non-authorizing restrictions.

The §15.12 interpretation is an owner reading of locked §15 text and is
NOT an amendment or override of §15.

The role fact is approved exactly as proposed:

- adapter-normalized;
- restrictive only;
- cannot independently grant authority;
- cannot widen K11;
- cannot bypass K4;
- cannot override K7;
- K3 does not evaluate it.

B1-B remains routed to the §16 Amendment Gate by DEC-087 and is not
resolved by DEC-088.

The following remain unresolved and routed exactly as stated in the
reviewed package:

- OD19-01;
- §22 O-4;
- CyberPanel K2 gate;
- ODF-18-06;
- §16 Amendment Gate;
- DEC-083;
- DEC-084;
- §19.21.2 items.

Do not modify or reopen §15, §16, §17, §19, §21 or §22.

Do not modify DEC-001 through DEC-086.

Do not modify the three flagged stale links/references:

1. DEC-026's protected Related line referencing
   `../open/p2-protocol.md`;
2. `docs/platforms/cyberpanel/k2-gate.md`'s reference to the old P2 path;
3. the existing register pointer rows OQ-3 and D-14.

Do not modify D80-7's historical/prose reference to
`open/p2-protocol.md`.

Those are separate documentation/pointer-cleanup work and are NOT part
of DEC-087/088.

The P2/K3 document may move from:

docs/architecture/open/p2-protocol.md

to:

docs/architecture/current/p2-protocol.md

with the reviewed locked-form changes.

Preserve the reviewed candidate text exactly except for the explicitly
authorized dispositions, lock bookkeeping, marker substitutions, title
and header changes.
```

Decision text (D88-1 … D88-13, adopted by the authorization above):

```text
D88-1  Authority and scope. This decision records the owner's dispositions of the P2/K3 candidate and
       locks the P2/K3 gate under DEC-080 (D80-7, D80-8), completing PHASE 5 (DEC-025; DEC-079 D79-5).
       Its subject is the P2/K3 gate only.
D88-2  Explicit owner choices. The following concrete choices are owner architectural decisions made
       by this decision. They are not attributed to DEC-026, DEC-044, DEC-051, DEC-080 or any other
       source:
       (a) assertion encoding: CBOR; no other serialization format;
       (b) assertion signature algorithm: Ed25519, asymmetric, so the verifier cannot mint; no
           symmetric signing or verification keys;
       (c) maximum assertion lifetime: 60 seconds; the validity window from `issued_at` to
           `expires_at` MUST NOT exceed 60 seconds; the freshness checks and single-use
           `assertion_id` requirement are unchanged;
       (d) transport: host-local Unix domain socket with OS peer-credential verification; no
           externally reachable listener; no TCP, HTTP listener exposure or other external
           transport; no socket path is defined architecturally;
       (e) SCC sessions (OQ-P2 = b): stateful; K4 owns session validation state, invalidation,
           lifetime and every authorization decision involving a session; K3 owns none of these;
           SCC session tokens are opaque references, not signed; no session signing secret and no
           stateless signed session;
       (f) session durability (OQ-P4 = a): session validation state exists only in K4 runtime
           state; K4 restart terminates every active SCC session; session state is not placed in K7,
           is not recoverable across K4 restart, and has no recovery mechanism; locked §19 DC-19 is
           not modified;
       (g) §15.12 reading (OQ-P5 = a): an explicit owner interpretation of the locked §15.12 impact
           rule, not an amendment to §15: a stateful SCC session token may be transiently present in
           K1/K2 while passing through the existing platform path; K1/K2 must not persist, log, mint,
           alter or independently authorize with it; K3 may transiently relay it within its locked
           boundary; K4 remains the sole authority for session validation and authorization. K1/K2
           being root-equivalent creates no new trust boundary and no SCC authorization authority
           for K1/K2.
D88-3  Role fact (OQ-P3 = a). The assertion carries the adapter-normalized platform role fact. It is
       restrictive only: it may restrict K4 authorization but cannot grant authority independently
       of K4, widen K11, bypass K4, override K7 authorization state, create a role or a Grant, or
       substitute for K4 authorization (T-13; A-04; A-10). K3 does not evaluate it.
D88-4  B1-B. P3 request-ID semantics are routed to the §16 Amendment Gate by DEC-087. The P2/K3
       contract references them and does not define them. Locked §21's `p3_request_id` is unchanged.
D88-5  Candidate approval. The owner approves every [CP] passage of the P2/K3 candidate as revised by
       D88-2 … D88-4 (OQ-P1 = b; OQ-P2 = b; OQ-P3 = a).
D88-6  Lock criteria (DEC-080 D80-8). (1) Every D80-2 element is specified (D88-2; D88-3; the
       candidate) or explicitly deferred to an established gate (D88-7). (2) Every D80-3 item is
       specified within §15.6/§15.10, and request-ID semantics are referenced and routed by DEC-087.
       (3) The assertion supports every §17.22 step-1 check (signature, audience, freshness, single
       use) and carries every §17 Authentication Context field. (4) No CyberPanel-specific K2
       question is decided; stateful sessions and the D88-2(g) reading keep both relay and proxy
       routes admissible. (5) No accepted decision widens authority, transfers responsibility
       between K2–K11, contradicts §15–§17 or makes an unauthorized amendment; K3 gains no
       authorization, identity or state authority; the role fact is restrictive only. (6) Every
       deferral names an established owning gate, including the §16 Amendment Gate for request-ID
       semantics (DEC-087). (7) No implementation authority is created, and this decision is the
       separate explicit owner lock DEC.
D88-7  Open items and routes: assertion-verification material storage and provisioning (OD19-01;
       DEC-051 R01b); K2 signing-key provisioning and re-registration (locked §22 O-4); CyberPanel
       route verification including whether the platform edge can reach K3 over the Unix domain
       socket on a proxy route, presentation placement, installation and `platform_subject_id`
       stability (CyberPanel K2 gate; OQ-1; P-6; KF-01, KF-02); request-bound assertions (Platform
       Adapter gate, ODF-18-06, NON-BLOCKING); P3 request-ID semantics (§16 Amendment Gate,
       DEC-087).
D88-8  Lock. The P2/K3 gate becomes locked architecture upon adoption of this decision.
D88-9  Authority category. From this decision forward, the P2/K3 document is added to the
       locked-architecture authority tier (Category 1), supplementing DEC-023 prospectively as DEC-075
       D75-4, DEC-085 D85-8 and DEC-086 D86-8 did. DEC-023 remains the historical record, and the
       earlier Category 4 classification remains historical.
D88-10 Documentation state. On adoption, the P2/K3 document moves from docs/architecture/open/ to
       docs/architecture/current/, and its status header follows the locked-document convention.
D88-11 Locked form. The P2/K3 document is locked in its candidate form with D88-2 … D88-4 applied,
       retaining its [DEC-0xx] and [L] tags. [CP], [OD] and open-question markers are replaced by
       references to DEC-088 (DEC-087 for request-ID routing), and the status header and title are
       updated; no other text changes.
D88-12 Phase boundary. This lock completes the DEC-079 D79-5 Phase-5 requirement. It does not enter
       Phase 6, does not authorize implementation or K4 code, and does not resolve OD19-01 or the
       CyberPanel K2 gate. A separate owner decision is required to authorize any implementation
       slice.
D88-13 Non-effects. This decision does not amend or change §15 (the D88-2(g) reading is an
       interpretation, not an amendment), §16, §17, locked §19 (including DC-19), locked §21 or
       locked §22; does not convene the §16 Amendment Gate or affect DEC-083, DEC-084 or §19.21.2;
       gives K1, K2 or K3 no authorization, identity or state authority; and creates no new secret
       or credential class. DEC-001 … DEC-086 are unchanged. DEC-029 remains standing.
```

> **Transcription note (session process):** The owner messages are reproduced from their disposition sections; their verification, preparation and repository-rule sections governed only those review steps and are omitted.

> **Index note (not owner wording):** DEC-088 locks the P2/K3 gate and completes Phase 5. It does not enter Phase 6, authorize implementation,
> amend §15 (D88-2(g) is a reading), or resolve OD19-01 or the CyberPanel K2 gate.

---

## DEC-089 — Phase 6 Implementation Authorization: K4 Authorization and Audit Core

- **Status:** CURRENT (adopted — first Phase 6 implementation slice authorized; no amendment; DEC-029 standing)
- **Source:** Owner Phase 6 implementation-authorization message with D89-1 … D89-4 (2026-10-02); owner decision
  D89-5 (2026-10-02); owner rulings Q1 … Q7 and adoption instruction (2026-10-02); owner selection of
  option (a) for Q3 (2026-10-03).
- **Related:** DEC-023; DEC-025; DEC-029; DEC-034 (R4a); DEC-035 (R5a, R5b); DEC-075; DEC-079 (D79-1 … D79-5, D79-8);
  DEC-082; DEC-085; DEC-086; DEC-087; DEC-088 (D88-12); §15.7; §16.5; §17.13; §17.22; §19 DC-07 … DC-10; §21; §22.3 … §22.7

```text
OWNER SCOPE DECISIONS AND AUTHORIZATION — DEC-089 (2026-10-02)

============================================================
DEC-089 — PHASE 6 IMPLEMENTATION AUTHORIZATION
============================================================

Before drafting, incorporate the following four scope clarifications.

These are explicit owner decisions for DEC-089 because the locked architecture does not fully define these portions of the proposed first code slice.

Do not invent any additional behavior beyond these decisions.

------------------------------------------------------------
D89-1 — DC-10 / JOB STATE
------------------------------------------------------------

DC-10 contains:

"Plans and Jobs (Plan content, plan_digest, Job state)"

However, the Job state model remains OPEN under §16 Q-6.

Therefore:

DEC-089 authorizes implementation of the Plan-related portion of DC-10 only:

- Plan content
- plan_digest
- the locked Plan state necessary for the authorized §17.22 steps 1–10

DEC-089 does NOT authorize implementation, definition, persistence, mutation, or interpretation of Job state.

Job creation and Job lifecycle remain outside this implementation slice.

Do not create a substitute Job state model.

Do not infer Job semantics from §21 A7 or any other document.

------------------------------------------------------------
D89-2 — A3 REVALIDATION
------------------------------------------------------------

A3 includes revalidation points in §17.13.

For this implementation slice, A3 is limited to the revalidation behavior actually exercised by the authorized §17.22 steps 1–10.

Specifically:

- Plan commit / authorization evaluation through the locked §17.22 steps included in this slice is in scope.
- Job-start revalidation is OUT OF SCOPE.
- Before-WRITE revalidation is OUT OF SCOPE.
- Post-revocation revalidation associated with Phase IV is OUT OF SCOPE.

Do not implement Phase IV behavior.

Do not create Job-start, WRITE-time, or Phase-IV revalidation semantics.

------------------------------------------------------------
D89-3 — K11 ANCHORS AND APPROVAL SIGNATURES
------------------------------------------------------------

The locked architecture requires:

- K11 anchor reading for §17.22 step 10;
- K11 anchor observation for B3;
- approval-evidence signature verification as specified by the locked architecture.

However, K11 implementation itself is outside this first code slice.

Therefore, for DEC-089:

K11 trust/anchor data SHALL be treated as an abstract trusted input/interface to the K4 authorization core.

The implementation may consume:

- the currently authoritative K11 anchor set required by the locked step-10 contract;
- the approval-evidence verification result required by the locked architecture;

but it MUST NOT implement K11 itself.

It MUST NOT:

- create K11 storage;
- modify K11;
- provision K11;
- implement K11 installation;
- implement K11 lifecycle;
- invent anchor-management behavior;
- create a new trust store;
- create a new cryptographic authority path.

The K4 implementation must preserve the locked distinction between K4's authorization evaluation and the K11 trust/anchor mechanism.

For B3, the implementation may consume an abstract observation/input representing the K11 anchor-change observation required by §21.

It must not implement an independent K11 observer.

If the locked architecture does not specify sufficient semantics to implement one of these abstract inputs, STOP rather than inventing them.

------------------------------------------------------------
D89-4 — B2 FAILED AUTHENTICATION
------------------------------------------------------------

Actual authentication/assertion verification remains outside this slice and remains blocked by OD19-01.

Therefore B2 failed-authentication audit handling is authorized only for a failure result supplied through the abstract Authentication Context/authentication-result boundary.

The K4 core may:

- receive an authentication failure result;
- produce the locked B2 audit record;
- apply the locked B2 recording behavior.

It may NOT:

- perform actual assertion verification;
- inspect raw credentials;
- verify Ed25519 signatures;
- manage authentication keys;
- implement P2;
- implement P2 transport;
- invent authentication failure semantics.

The authentication boundary remains abstract.

============================================================
AUTHORIZED FIRST IMPLEMENTATION SLICE
============================================================

Subject to D89-1 through D89-4, DEC-089 authorizes ONLY:

1. K4 authorization evaluation

Implement:

- §17.22 Phases I–III only where they correspond to the authorized steps;
- §17.22 steps 1–10;
- abstract Authentication Context;
- the locked authorization inputs required by those steps.

Do not implement Phase IV.

2. K7 authorization state

Implement only the authorized portions of:

- DC-07
- DC-08
- DC-09
- DC-10

with DC-10 limited according to D89-1.

3. K4 audit

Implement the locked §21 contract for:

- A1
- A2
- A3
- A4
- A6
- B1
- B2
- B3

subject to the scope limitations above.

4. Audit infrastructure

Implement:

- audit identity;
- audit sequence;
- durable recording;
- recording-order semantics;
- timestamp versus recorded_at distinction;
- the locked audit failure behavior;
- the locked atomicity requirements.

5. Failure/atomicity

Implement only:

- R4a
- R5a
- R5b

6. Bootstrap

Implement only the K4-side bootstrap necessary for:

- first HUMAN Principal;
- first scc.administrator membership;
- corresponding A6 records;

using the abstract P11 input defined by locked §22.

No general Principal management.

No general K9 authority.

No general recovery implementation.

============================================================
EXPLICITLY OUT OF SCOPE
============================================================

DEC-089 does NOT authorize:

- K2 implementation;
- K3 implementation;
- P2 implementation;
- P2 assertion issuance;
- P2 assertion verification;
- CBOR implementation;
- Ed25519 implementation;
- Ed25519 key provisioning;
- P2 transport;
- Unix-domain socket implementation;
- stateful SCC session implementation;
- P3 implementation;
- P3 request-ID semantics;
- K6 implementation;
- K8 implementation;
- K5 implementation;
- CyberPanel integration;
- platform adapter implementation;
- actual platform authentication;
- credential handling;
- secret storage;
- secret provisioning;
- host filesystem operations;
- shell execution;
- subprocess execution;
- host service management;
- K11 implementation;
- K11 storage;
- K11 provisioning;
- K11 lifecycle;
- export implementation;
- off-host audit artifacts;
- recovery beyond locked bootstrap;
- installer implementation;
- migration implementation;
- OD19-01;
- §16 Amendment Gate work;
- DEC-083 implementation;
- DEC-084 implementation;
- unresolved §22 recovery items;
- Job state;
- Job lifecycle;
- Phase IV authorization/revalidation;
- WRITE-time revalidation;
- Job-start revalidation;
- post-revocation Phase-IV revalidation;
- architecture amendments.

In particular, DEC-089 must NOT be interpreted as authorizing implementation of the concrete P2/K3 protocol merely because DEC-088 selected:

- CBOR;
- Ed25519;
- 60 seconds;
- Unix-domain sockets;
- stateful sessions.

Those remain architecture decisions whose implementation is outside this slice.

============================================================
DEC-029 BOUNDARY
============================================================

DEC-089 remains strictly subordinate to DEC-029.

It authorizes implementation of locked architecture only.

It does NOT authorize:

- architectural invention;
- resolving unrelated open questions;
- silently choosing unspecified behavior;
- compatibility behavior not specified by the architecture;
- changes to locked semantics;
- architecture amendments;
- new authority paths.

If implementation later encounters a requirement that is not specified by the locked architecture or DEC-089:

STOP.

Do not invent the behavior.

============================================================
DEC-089 FORM
============================================================

Draft DEC-089 as a Category 1 owner implementation-authorization decision.

It must explicitly record:

- D89-1
- D89-2
- D89-3
- D89-4
- authorized implementation scope;
- explicit exclusions;
- dependencies;
- DEC-029 boundary;
- OD19-01 dependency;
- statement that no architecture amendment is authorized;
- statement that unresolved questions remain unresolved;
- statement that this decision authorizes the first Phase 6 implementation slice.

Do not use vague "begin implementation" language.

The decision must be mechanically understandable by a developer implementing against it.

============================================================
OWNER AUTHORIZATION
============================================================

I authorize the preparation, adversarial review, and adoption of DEC-089 exactly within the scope above.

This is authorization to adopt the DEC-089 decision.

It is NOT authorization to implement production code in this task.

STOP after the DEC-089 commit and report.

OWNER DECISION D89-5 (2026-10-02)

D89-5 — Abstract domain and planning inputs. For this implementation slice, the following are abstract inputs to the K4 authorization core. Their producers and underlying mechanisms are not implemented:

(a) K11 capability and scope declarations required by §15.7 and §17.22 steps 2 and 5. K4 consumes these with their locked meaning and may narrow but never widen the applicable capability/scope.

(b) The §17.22 step-3 admissibility facts concerning Integration validity, capability availability, compatibility, and management or ownership. These represent the applicable DC-04 domain state and are not implemented in this slice.

(c) Plan proposals supplied as the §17.22 step-5 K5 input. K5 is excluded from this slice.

K4 remains responsible for the locked validation, narrowing, coverage checks, and plan_digest computation that the architecture assigns to K4 over those supplied inputs.

No K11 implementation, K5 implementation, K6 discovery implementation, discovery subsystem, DC-04 store/registry, or replacement mechanism is authorized by this decision.

Where the locked architecture does not provide sufficient semantics for an abstract input or for a required K4 operation, implementation stops under DEC-029 rather than inventing behavior.

OWNER RULINGS Q1 … Q7 AND ADOPTION INSTRUCTION (2026-10-02)

The seven decisions are:

* Q1 — YES. K4 may record `CONFIRMED` Binding status and the latest confirmed platform role from a verified abstract Authentication Context. Do not implement `LOST`/automatic `SUSPENDED` behavior in this slice. `PLATFORM_ADMIN` is evaluated as the locked §17.7 implicit condition; failure is an authorization denial, not B2.
* Q2 — YES. Inventory target resolution is an additional abstract domain input under D89-5.
* Q3 — YES. Treat the release-baseline policy revision as an abstract input, and have bootstrap establish the starting empty local-settings revision. Do not invent another revision mechanism.
* Q4 — YES. K4 may write the locked `INVALIDATED` DC-09 status when the Plan changes, subject to the existing atomicity/audit contract.
* Q5 — OUT. `scc.*` administrative mutation/application is explicitly outside this slice. The core may evaluate such a request through steps 1–10, but does not apply the resulting administrative change to K7.
* Q6 — YES. The abstract approval-evidence verification input includes both signature verification and the required exact canonical-digest match. K4 does not construct P6 requests or implement K6 cryptography.
* Q7 — YES. DEC-089 has no Category 1 label. It is an owner decision recorded in the decision log under the DEC-023 hierarchy.

Also apply all of the mechanical fixes Claude identified:

* D89-7: locked text controls the drafted items under DEC-081 B(i).
* Quote R4a verbatim and apply it to all applicable authorization-state mutations.
* Keep OS-root determination separate from P11 request content per §22.6.
* Implementers may choose only representations for abstract inputs; they may not define their semantics.
* Add the §17.8 requirement that an approver be ACTIVE with a CONFIRMED binding.
* Make the §21 citations explicit rather than using the broad range that includes excluded §21.10.
* Cite §21.7 alongside §21.12 for the B1 field list.
* Base D89-17 on A-01/§17.2 rather than §22.4.2.
* Change the index note to “A3 not exercised.”
* Preserve the explicit consequences:
   * A3 is not exercised in this slice.
   * R5b is not triggered because A5/SYSTEM cancellation is excluded.

One thing I want kept very explicit in the resulting DEC-089:
Steps 1–10 being authorized does not mean every consequence of steps 1–10 is authorized.
The slice is authorizing the K4 evaluation machinery and the specifically enumerated state/audit effects, while excluding the downstream systems and mutation paths that remain outside it.
Proceed with those rulings, rerun the full checks and independent adversarial review, and adopt only if they pass. One local commit, no push, no merge/rebase/force-push/amend, and stop after the commit.

OWNER SELECTION FOR Q3 (2026-10-03)

Proceed with (a), finish the revised DEC-089, rerun the full mechanical suite and independent adversarial review, and only adopt if both pass.
```

Decision text (D89-6 … D89-21, adopted by the authorization above; D89-1 … D89-5 are the owner text above):

```text
D89-6  Authority and subject. This decision is the explicit owner decision that DEC-088 D88-12 requires
       before any implementation slice. It authorizes the first PHASE 6 implementation slice (DEC-025;
       DEC-079 D79-1 … D79-3, D79-5): the abstract K4 authorization-and-audit core that DEC-079 D79-8
       leaves unblocked by OD19-01. It authorizes implementation of locked architecture only. It is an
       owner decision recorded in the decision log under the DEC-023 authority hierarchy (owner ruling
       Q7); it carries no Category 1 label and reclassifies no document.
D89-7  Controlling text. The owner text above (D89-1 … D89-5, the authorized slice, the exclusions, the
       DEC-029 boundary, the rulings Q1 … Q7 and the Q3 selection) controls D89-6 … D89-21; where a
       drafted item and the owner text differ, the owner text controls. Locked §15, §16, §17, §19, §21,
       §22 and the locked P2/K3 gate control this decision (DEC-023; DEC-081 B(i)); nothing in it
       supersedes locked text.
       Q3 as adopted. The owner's later selection of option (a) (2026-10-03) replaces the second half of
       ruling Q3. The clause "have bootstrap establish the starting empty local-settings revision" is
       not adopted, because it conflicts with locked §22.3.3 ("no policy change"), §22.7.2 (one A6
       record for each bootstrap mutation: Principal creation; membership) and the §19 DC-08 writer ("C
       (R4 `scc.*` Action)"). As adopted, Q3 means: the release-baseline policy revision and the
           starting local-settings revision are abstract inputs, consumed read-only; DC-08 is not
           written in this slice; the bootstrap act is exactly as locked §22 defines it. No other
           revision mechanism is created.
D89-8  Evaluation versus consequences. Authorizing §17.22 steps 1–10 authorizes the K4 evaluation
       machinery of those steps and only the state and audit effects enumerated in D89-10, D89-13,
       D89-14 and D89-15. It does not authorize every consequence of steps 1–10. Any other state change,
       record, downstream system, mutation path or component that a step would lead to is not authorized
       by this decision.
D89-9  Authorized: K4 evaluation of locked §17.22 steps 1–10 (Phases I–III) only:
       (a) Step 1 [§17.22 step 1; §17 Terms; §17.1.4; §17.2; A-01, A-03]: K4 receives an abstract
           Authentication Context (assertion ID, platform, subject, authentication time, method claims;
           §17 Terms), together with the platform role fact that locked P2/K3 §P.3.2 carries in the same
           verified assertion, or an abstract authentication-failure result (D89-4). From a supplied
           verified Authentication Context K4 resolves the Binding, then the Principal, in K7, and
           requires the Principal ACTIVE and the Binding CONFIRMED; an interactive request is confirmed
           by its own verified assertion (§17.1.4). On any step-1 failure, deny and record B2
           (D89-13(g)). K4 may record the Binding status CONFIRMED and the latest confirmed platform
           role in DC-07 from a verified abstract Authentication Context (owner ruling Q1). §21.6
           defines no event kind for that write and this decision creates none. Binding status LOST and
           the automatic SUSPENDED that follows it are not implemented (Q1).
       (b) Steps 2 and 3 [§17.22 steps 2–3; §15.7; §17.6; A-09]: identification over the D89-5(a)
           declarations and the Inventory target resolution of §17.6, which is an additional abstract
           domain input under D89-5 (owner ruling Q2); admissibility over the D89-5(b) facts. The
           admissibility result is recorded separately from authorization; failure is an inadmissible
           refusal.
       (c) Steps 4 and 7 [§17.22 steps 4, 7; §17.4 … §17.7; §17.17; §17.20; A-10 … A-13, A-16, A-25,
           A-34]: Grant and Role coverage; conditions from the closed vocabulary (a condition that
           cannot be evaluated counts as false), including `PLATFORM_ROLE`, under which v1
           `PLATFORM_ADMIN` is always implicitly required and is evaluated against the Binding's latest
           confirmed platform role, its failure being an authorization denial and not B2 (Q1; §17.7;
           A-04); effective tier; PLAN_MAX_AGE and whole-Plan denial. Evaluation is against K7 at every
           decision point under the current policy revisions, with no decision cache, negative cache or
           distributed cache. The release-baseline policy revision and the starting local-settings
           revision are abstract inputs consumed read-only (Q3 as adopted, D89-7).
       (d) Steps 5 and 6 [§17.22 steps 5–6; §15.7; §17.11; A-21, A-24]: K4's structure validation, K11
           coverage check, narrowing and `plan_digest` computation over the D89-5(c) Plan proposal and
           the D89-5(a) declarations; Plan tier. When a Plan changes, the old Decision becomes
           INVALIDATED (§17.11; owner ruling Q4), subject to the existing atomicity and audit contract
           (Q4).
       (e) Step 8 [§17.22 step 8; §17.10; A-17, A-18]: REAUTH (AUTH_FRESH) over the authentication time
           in the supplied Authentication Context.
       (f) Step 9 [§17.22 step 9; §17.19; A-24, A-26, A-34]: creation of the immutable Authorization
           Decision, its `authorization_ref` and its AWAITING_APPROVAL or AUTHORIZED status record,
           recording the baseline and local policy revisions.
       (g) Step 10 [§17.22 step 10; §17.8; §17.9; A-19, A-20; §16.5]: K4 verifies, from K7, that the
           approver is a HUMAN Principal that is ACTIVE with a CONFIRMED binding and holds an `approve`
           Grant covering the capability, target and tier (§17.8 "Who may approve"), and applies the
           separation-of-duties policy; and that the consumed K11 anchor set contains an anchor naming
           that approver's `principal_id` (§17.9; A-20). It consumes the K11 anchor set and the
           approval-evidence verification result as abstract inputs under D89-3; that result includes
           both signature verification and the required exact canonical-digest match (owner ruling Q6).
           K4 does not construct P6 requests, does not implement K6 cryptography and does not specify
           the §16.5 canonical encoding. It records each approval and sets AUTHORIZED when all are
           present. Where approval state or K11 anchors are unreadable, R4 is denied (§17.16).
D89-10 Authorized: K7 authorization state [locked §19 DC-07 … DC-10, SD-K7, identity C only; T-23; §19
       lifecycle table], limited to these effects:
       (a) DC-07 (Principals, Platform Identity Bindings, Role Memberships, Grants, revocation records):
           read by the D89-9 evaluation; written only by the bootstrap act (D89-15) and by the Q1
           Binding-confirmation write (D89-9(a)).
       (b) DC-08 (authorization policy local settings and revisions): not written in this slice (D89-7;
           D89-11). The starting local-settings revision is an abstract input (D89-7).
       (c) DC-09: immutable Authorization Decisions; their append-only status records AWAITING_APPROVAL,
           AUTHORIZED and INVALIDATED (Q4, subject to the existing atomicity and audit contract); and
           Approval Records.
       (d) DC-10: the Plan portion only, under D89-1.
D89-11 K4-internal administration (owner ruling Q5). A `scc.*` administration request may be evaluated
       through §17.22 steps 1–10, with the records D89-13 authorizes for those steps. The application of
       the resulting administrative change to K7 — the atomic application that replaces steps 11–14 for
       K4-internal Actions (§17.22) — is outside this slice: no enrollment, Grant, Role Membership,
       revocation, Principal-state or policy local-settings change is applied. The bootstrap act
       (D89-15) is the only authorized administration mutation. The semantics of approvals for
       K4-internal Actions remain open (Q19-04; DEC-053 R03i); where step 10 for a K4-internal Action
       requires them, D89-19 applies.
D89-12 Not authorized, because each depends on a component, phase or mutation path outside this slice:
       SYSTEM observation and its authorization (§21.13; D89-5 and the owner's K6 exclusion); Binding
       status changes from Platform Services observation, Binding LOST and automatic SUSPENDED (§17.1.4;
       Q1); asynchronous-revalidation binding freshness (§17.1.4); the Decision statuses CONSUMED,
       EXPIRED and REVOKED; and scheduled Actions (§17.12; A-30).
D89-13 Authorized: K4 audit under the locked §21 contract [§21.3, §21.4, §21.5, §21.6, §21.7, §21.8,
       §21.9, §21.11, §21.12, §21.14, §21.15, §21.20; §17.18; A-35], within this slice:
       (a) A1 for §17.22 steps 1–4, including denials, inadmissible refusals and HUMAN `view` decisions
           of tier R1 and above. SYSTEM observation A1 is not exercised (D89-12).
       (b) A2 for §17.22 steps 5–9, including REAUTH failure, whole-Plan denial and creation of the
           Decision and `authorization_ref`.
       (c) A3 is not exercised. Locked §21.6 scopes A3 to Job start, before each WRITE request and after
           revocation or disablement, all excluded by D89-2. The §17.13.1 Plan-commit point (full
           evaluation, §17.22 steps 1–9) is performed as that evaluation and recorded as A1 and A2 under
           §21.6. No A3 record arises in this slice, and this decision creates no A3 semantics.
       (d) A4, one record per approval received and verified or rejected at step 10.
       (e) A6 for the bootstrap act only (D89-15; §22.7).
       (f) B1 for the §21.12 denial row only (A1–A3 denials, inadmissible refusals and failed
           authentication), with the fields §21.7 and §21.12 require. The A5 SYSTEM and
           SYSTEM-observation A1 cases of B1 are not exercised.
       (g) B2 under D89-4 and §21.14: one per failed attempt; `failure_reason` identifies the step-1
           check; `claimed_assertion_id` only as supplied through the abstract boundary and marked
           unverified; never the claimed platform subject, raw assertions or bearer credentials.
       (h) B3 under D89-3 and §21.15 from the abstract K11 anchor-change observation, including the
           §21.12 reliance rule: the changed anchor set is not treated as established until the B3
           record is durable, with no fallback to a stale, cached, previously observed or assumed anchor
           set.
       Audit infrastructure: `audit_id` (§21.4); `audit_seq` as recording order (§21.5); the distinct
       `timestamp` and `recorded_at` (§21.5); the required record fields (§21.7); conditions and
       evaluated values (§21.8); correlation through `authorization_ref`, `plan_ref` and `plan_digest`
       (§21.9), with no value created for `job_id`, `k6_request_ids`, `k8_ref` or `p3_request_id`;
           durable recording as commitment to SD-K7 surviving K4 process restart and host restart
           (§21.11); the §21.12 audit-write-failure behaviour for the records above; and the atomicity
           of D89-14. A5, A7 and B4, K8 correlation (§21.10), audit views (§21.16), any retention or
           disposition mechanism, restoration and continuity (§21.18) and export (§21.19) are not
           authorized; the §21.17 no-expiry and no-eviction constraints apply.
D89-14 Authorized: failure and atomicity rules R4a, R5a and R5b only [DEC-034; DEC-035; §21.11; §21.12]:
       (a) R4a, verbatim: "For every K4 authorization state mutation for which §17 requires an audit
           record, the authorization mutation and its required audit record MUST become durable
           atomically: either both are committed or neither is committed." It applies by its own terms
           to every authorization-state mutation authorized by this decision for which §17 requires an
           audit record, and is not limited to A6. For a class A record subject to R4a, the `audit_seq`
           position is part of the same atomic commit (§21.5).
       (b) R5a: a K4 action or authorization decision in this slice whose required audit record cannot
           be durably recorded does not proceed; no bypass. A denial remains a refusal and is not
           late-recorded (§21.12).
       (c) R5b is not triggered. It governs only the A5 SYSTEM revocation-triggered cancellation under
           A-05, which is outside this slice (D89-1, D89-2). R5b is preserved; no SYSTEM cancellation,
           A5 record or `late_recorded` path is implemented, and no other path may rely on R5b.
D89-15 Authorized: the K4 side of the locked bootstrap act only [§22.3 … §22.7; §17.1.5; A-07; DEC-086].
       K4 receives (i) an abstract P11 request whose content is the §22.4.1 Platform Identity Binding
       tuple and nothing else that confers authority (§22.6), and (ii) separately, an abstract
       channel-level determination that the operating system established the caller as root (§22.5.1),
       which is not P11 request content; from (ii) K4 forms `lro_auth_ref`
       (§22.5.2). K4 applies §22.3 (available only while K7 holds no `scc.administrator` Role Membership
           record in any state; grants nothing else); the §22.4 effects (one HUMAN Principal ACTIVE with
           no Grants, its Binding UNCONFIRMED(since), one ACTIVE `scc.administrator` membership), and no
           other mutation (§22.3.3; D89-7); §22.4 atomicity; the §22.6 validation, replay, result and
           failure rules; and the §22.7 A6 records (one per bootstrap mutation, §22.7.2). Not
           authorized: K9; the P11 transport, encoding, command syntax and endpoint (which §22.6 does
           not define); any OS peer-credential mechanism; recovery after the loss of every administrator
           (§17.24 P-5); and any alternative path to a first administrator (§22.4).
D89-16 Excluded. Everything listed under "EXPLICITLY OUT OF SCOPE" in the owner message above, and
       everything D89-1 … D89-5, Q1 … Q7 (Q3 as adopted, D89-7), D89-8, D89-11, D89-12, D89-13, D89-14
       and D89-15 exclude, is not authorized. The concrete P2/K3 choices of DEC-088 (CBOR, Ed25519, the
       60-second maximum lifetime, Unix domain socket transport, stateful K4 sessions) are not
       implemented by this decision. K1 and K9 are not implemented.
D89-17 Implementation choices. This decision does not select a programming language, storage engine,
       schema, record encoding, identifier format or repository layout (§19 and §21 define no schema or
       storage engine). For the abstract inputs, implementers choose only their representation; their
       content and meaning are only those the locked text, D89-3 … D89-5, Q1 … Q6 and D89-7 give, and
       implementers do not define them. S19-15 (format-version information for authoritative SD-K7
       content) applies to SD-K7 content written in this slice (D89-7). A choice that would require
       behaviour not specified by the locked architecture or this decision stops under DEC-029.
D89-18 Dependencies. This slice depends on locked §15, §16, §17, §19 (DEC-075), §21 (DEC-085), §22
       (DEC-086) and the locked P2/K3 gate (DEC-088). OD19-01 remains unresolved and continues to block
           actual assertion-verification implementation (DEC-079 D79-8); this slice consumes only the
           abstract authentication result (D89-4). Authorization is evaluated only for a Principal
           resolved from a K4-verified Authentication Context (A-01; §17.2); in operation that requires
           the P2/K3 implementation and OD19-01, neither of which is authorized here.
D89-19 DEC-029 boundary. This decision is subordinate to DEC-029, which remains standing. Every DEC-029
       prohibition remains in force, and no placeholder function may secretly establish any of those
       paths. This decision authorizes no architectural invention, no resolution of open questions, no
       silent choice of unspecified behaviour, no compatibility behaviour not specified by the
       architecture, no change to locked semantics and no new authority path. When implementation meets
       a requirement that neither the locked architecture nor this decision specifies, implementation
       stops and the question is reported to the owner.
D89-20 Unresolved items remain unresolved, including: the Job state model (§16 Q-6); OD19-01; the §16
       Amendment Gate items (DEC-083, DEC-084, DEC-087, §19.21.2); the open §22 items (§22.8); the
       CyberPanel K2 gate; ODF-18-06; and Q19-04 (semantics of approvals for K4-internal Actions;
       DEC-053 R03i).
D89-21 Non-effects. This decision does not amend or change §15, §16, §17, locked §19, locked §21, locked
       §22 or the locked P2/K3 gate, and authorizes no architecture amendment. DEC-001 … DEC-088 are
       unchanged. Its adoption creates no production code.
```

> **Transcription note (session process):** The first owner message is reproduced from its scope-decision, scope,
> exclusion, DEC-029, form and authorization sections; its hash-correction, source-material, adversarial-review,
> repository-rule, adoption and final-report sections governed only this change set and are omitted. D89-5 and the
> Q1 … Q7 rulings message are reproduced in full. Q1 … Q7 answer the questions raised in the pre-adoption review. The
> 2026-10-03 message selects option (a) of the second pre-adoption review: the release-baseline and starting
> local-settings revisions are abstract read-only inputs, with no DC-08 write and the bootstrap act exactly as locked
> §22 defines it (D89-7). Item numbers in the owner's Q1 … Q7 message ("D89-17" for the A-01/§17.2 basis; the
> representation-only rule) refer to the earlier draft numbering; those items are D89-18 and D89-17 here.

> **Index note (not owner wording):** DEC-089 authorizes the first Phase 6 implementation slice: the K4 evaluation of
> §17.22 steps 1–10 over abstract inputs, the enumerated DC-07 … DC-10 effects (Plans only), A1, A2, A4, A6, B1–B3
> (A3 not exercised), R4a and R5a (R5b not triggered) and the K4 side of the bootstrap act; DC-08 is not written (Q3
> as adopted). Authorizing steps 1–10 does not authorize every consequence of them (D89-8). It amends nothing and
> leaves OD19-01 blocking actual assertion verification. Under owner ruling Q7 it carries no Category 1 label.

---

## DEC-090 — Phase 6 Authorization Semantics Clarification

- **Status:** CURRENT (adopted — owner interpretations for the Phase 6 K4 core; no amendment; corrections documented, not implemented)
- **Source:** Owner DEC-090 request and authorization (2026-10-03); owner rulings on Q5 (option (a)) and Q3 ("any amount")
  (2026-10-03); owner ruling on Q2 (option C) with the adoption instruction (2026-10-03).
- **Related:** DEC-023; DEC-029; DEC-081; DEC-088; DEC-089 (D89-4, D89-5, D89-9, D89-10, D89-11, D89-17, Q4); §16.2.2; §16.3; §16.4.1;
  §16.5; X-16; §17.3; §17.4; §17.5.2; §17.7; §17.8; §17.10; §17.11; §17.14; §17.16; §17.19; §17.20; §17.22; A-13;
  A-23; A-24; A-26; §19 DC-07 … DC-10; §21.7; P2/K3 §P.4; k4core/IMPLEMENTATION_BOUNDARY.md

```text
OWNER DEC-090 REQUEST AND AUTHORIZATION (2026-10-03)

============================================================
2. PURPOSE OF DEC-090
============================================================

DEC-090 is NOT a new architecture gate.

It is a narrowly scoped owner decision addressing semantic interpretations exposed by the first K4 implementation.

The purpose is to prevent implementation-specific behavior from silently becoming architecture.

DEC-090 MUST NOT:

- amend §15;
- amend §16;
- amend §17;
- amend §19;
- amend §21;
- amend §22;
- amend P2/K3;
- reopen DEC-089 generally;
- authorize new subsystems;
- authorize new authority paths;
- authorize new implementation scope.

If any question requires amendment to locked architecture, STOP and report that it must go through the appropriate architecture gate.

============================================================
4. DEC-090 QUESTIONS
============================================================

DEC-090 must address these five semantic questions.

------------------------------------------------------------
Q1 — ACTION VS PLAN TIER
------------------------------------------------------------

Current implementation interpretation:

Where the locked architecture refers to the tier of "the Action or Plan", the applicable tier is the higher of the Action's tier and the Plan's tier for:

- step-up;
- approval requirement;
- separation-of-duties evaluation.

The implementation does NOT add an independent requirement that a Plan must "realize" or otherwise contain the Action merely because the Action supplied the tier.

Owner decision:

CONFIRM this interpretation for the current implementation.

Do not invent an additional Action-to-Plan realization rule.

If the locked text does not define such a rule, leave it undefined.

------------------------------------------------------------
Q2 — K11 approval_required FLAG
------------------------------------------------------------

Current implementation interpretation:

A Plan step covered by a K11 scope entry with:

approval_required = true

causes the Plan to require approval.

This interpretation must be examined carefully.

Do NOT assume it merely because it is convenient.

Determine from the locked text whether:

A. any applicable flagged scope entry makes the entire Plan approval-required;

B. the flag applies only to the corresponding request;

C. the locked architecture does not define the mapping.

If the mapping is genuinely undefined, DEC-090 must say so rather than invent it.

If an owner interpretation can resolve it without contradicting locked architecture, record that interpretation explicitly.

Do NOT change §17.

------------------------------------------------------------
Q3 — FUTURE AUTHENTICATION / OBSERVATION TIMES
------------------------------------------------------------

Current implementation behavior:

An authentication or observation timestamp later than K4's current clock is currently treated as fresh.

We need an explicit owner interpretation.

First verify whether locked text already defines the treatment of future timestamps.

If it does, follow the locked text.

If it does not:

Owner decision should be:

A timestamp materially in the future relative to K4's current clock does NOT satisfy freshness.

Such input must fail closed through the applicable locked denial/error path.

Do not invent a clock-skew tolerance unless the locked architecture already specifies one.

Do not create a new timestamp protocol.

The implementation must not allow an arbitrarily future timestamp to satisfy freshness.

------------------------------------------------------------
Q4 — ROLE-SUBJECT GRANTS
------------------------------------------------------------

Current implementation behavior:

Grants whose subject is a built-in Role are ignored because this Phase 6 slice has no path that creates such K7 Grant rows.

This MUST be reviewed carefully.

Do not silently turn:

"this slice cannot create Role Grants"

into:

"Role Grants in K7 are semantically ignored."

Determine whether the locked architecture explicitly specifies how existing Role-subject Grant rows are handled.

If it does, follow that rule.

If it does not:

DEC-090 should NOT invent an ignore rule.

The preferred boundary is:

- this slice does not create Role-subject Grant rows;
- if such a row is encountered and the locked architecture does not define its treatment, K4 must not silently discard it;
- implementation should fail closed / report an unsupported semantic rather than inventing behavior.

Do not modify the locked Grant model.

------------------------------------------------------------
Q5 — REUSED plan_ref / DECISION INVALIDATION
------------------------------------------------------------

Current implementation behavior:

Committing a different Plan under an existing plan_ref can invalidate an earlier Decision, even when:

- the new Plan belongs to a different Principal; and
- the new authorization is denied.

This behavior must NOT be accepted merely because it is convenient for the current SQLite implementation.

Determine exactly what §17.11, §17.19, §19, and DEC-089 establish about:

- Plan identity;
- plan_ref;
- Decision identity;
- Principal ownership;
- invalidation;
- when a Plan change occurs.

If the locked architecture does not explicitly authorize cross-Principal invalidation from a denied request:

DEC-090 must prohibit that behavior.

The implementation must NOT invalidate an existing Decision belonging to another Principal merely because a denied request reused the same plan_ref.

A denied Plan commit must not create an unrelated cross-Principal state effect.

If the architecture does not provide enough identity semantics to safely determine which prior Decision a Plan mutation relates to:

STOP and report the semantic gap rather than inventing an identity rule.

============================================================
5. EXPLICITLY OUT OF SCOPE
============================================================

DEC-090 does NOT decide:

- P2;
- P3;
- authentication protocol;
- Ed25519;
- CBOR;
- K6;
- K8;
- K11 implementation;
- K5;
- Job state;
- Phase IV;
- A3;
- A5;
- administrative mutation;
- recovery;
- CyberPanel;
- host operations;
- schema requirements beyond correcting the current implementation if required by DEC-090.

It does not authorize a new implementation slice.

============================================================
6. IMPLEMENTATION BOUNDARY
============================================================

DEC-090 must distinguish:

LOCKED ARCHITECTURE
from
OWNER INTERPRETATION
from
IMPLEMENTATION CHOICE.

Do not promote Python, SQLite, SHA-256, internal data structures, module layout, or other implementation choices into architecture.

The existing:

k4core/IMPLEMENTATION_BOUNDARY.md

may be updated later if DEC-090 is adopted, but do not modify it during the decision-drafting stage unless the adoption procedure explicitly includes the update.

============================================================
7. DEC-090 DRAFT REQUIREMENTS
============================================================

Draft DEC-090 as an owner decision.

Do NOT label it Category 1.

Under DEC-023, a decision-log entry is a Category 2 owner decision.

DEC-090 should contain:

- title;
- purpose/scope;
- source mapping;
- Q1 ruling;
- Q2 ruling;
- Q3 ruling;
- Q4 ruling;
- Q5 ruling;
- explicit non-effects;
- statement that DEC-029 remains controlling;
- statement that no locked architecture document is amended;
- statement that unresolved semantics remain unresolved where applicable.

Every substantive ruling must distinguish:

"the locked architecture requires this"

from:

"the owner is selecting this interpretation because the locked architecture leaves it open."

============================================================
8. NO CODE CHANGES YET
============================================================

Do NOT modify production code during this task.

Do NOT modify tests.

Do NOT modify schema.

Do NOT modify k4core.

Do NOT modify the implementation boundary file yet.

This task is:

inspect → draft → adversarially review → adopt DEC-090.

If a ruling requires a code correction, document the required correction in DEC-090 but do not implement it yet.

============================================================
OWNER AUTHORIZATION
============================================================

I authorize preparation, adversarial review, and adoption of DEC-090 exactly within the scope above.

I do NOT authorize implementation changes in this task.

If any of Q1–Q5 cannot be resolved without amending locked architecture, STOP and report the required architecture gate instead of inventing a resolution.

Otherwise adopt DEC-090 in one local commit and stop.

OWNER RULINGS ON Q5 AND Q3 AND ADOPTION INSTRUCTION (2026-10-03)

Proceed with Q5(a), confirm Q3's "any amount" interpretation, draft DEC-090 with the complete source mapping, run the mechanical and independent adversarial reviews, and adopt only if both pass.

No code changes in this task. One local DEC-090 commit, no push, no merge/rebase/force-push/amend.

OWNER RULING ON Q2 AND ADOPTION INSTRUCTION (2026-10-03)

C — fail closed.
For the specific unresolved case:
A Plan contains a K11-flagged scope entry, but there is no §17.8 K4 approval trigger, no applicable §17.20 local setting, and no other approval requirement.
K4 should refuse the Plan as an unsupported case rather than infer that the K6 enforcement flag itself creates a K4 approval requirement.
That keeps the layers distinct:

* K4: does not treat the K11 flag itself as a Plan-level approval trigger.
* K6: remains responsible for the locked per-request enforcement of the flag.
* K4: does not authorize a Plan whose treatment of that flagged-below-R4 case is architecturally undefined.
* Fail closed: refusal is recorded according to the already-locked audit semantics; don't invent a new approval trigger or authority path.

So the ruling should be recorded explicitly as an owner interpretation, not represented as something already established by §17.
Proceed with the scratch-draft correction, fresh 57+ mechanical checks, and independent adversarial review. If those pass, adopt DEC-090 in one local commit only. No push, merge, rebase, force-push, or implementation changes.
```

Decision text (D90-1 … D90-9, adopted by the authorization above):

```text
D90-1  Authority, subject and form. This decision is an owner decision recorded in the decision log
       under the DEC-023 authority hierarchy; it carries no Category 1 label and is not an architecture
       gate. Its subject is five semantic questions exposed by the first PHASE 6 implementation (DEC-089
       slice; commit 94bfdc1d0c3807cc49753a6d5a332659ec0599a4). Each ruling distinguishes [L] what
       locked text requires, [OI] what the owner selects because locked text leaves it open, and [U]
       what remains unresolved. Locked §15, §16, §17, §19, §21, §22 and the locked P2/K3 gate control
       this decision (DEC-023; DEC-081 B(i)).
D90-2  Q1 — Action versus Plan tier.
       [L] §17.10 trigger: "The effective tier of the Action or Plan (§17.5.3), plus any
           `APPROVAL_REQUIRED` conditions". §17.8: "Which Actions require approval: Effective tier R4,
           plus any Grant carrying `APPROVAL_REQUIRED`". §17.22 step 6: "Plan tier is the highest
           effective tier among its steps"; step 8: "Check `AUTH_FRESH` against the tier". §17.8 and
           §17.20: separation of duties is an optional, narrowing local policy that "can be enabled per
           tier".
       [OI] For step-up (whether REAUTH and APPROVAL apply, and the REAUTH maximum age), the approval
            requirement and the separation-of-duties tier, the applicable tier is the higher of the
            Action's effective tier and the Plan tier. This confirms the current implementation for
            these purposes only.
       [U] §17.5.2 defines a Plan as "The concrete, digested set of steps K4 accepts in order to realize
           the Action", but no locked rule requires K4 to verify that a Plan realizes or contains its
           Action. DEC-090 creates no such rule; the question remains undefined.
D90-3  Q2 — K11 per-scope-entry `approval_required` flag.
       [L] §16.2.2: scope entries carry an "`approval_required` flag (reserved for §17)". X-16: "Where
           K11 requires approval evidence, K6 MUST verify signature, anchor, digest binding, expiry and
           nonce single use." §16.4.1 layer 15 and §16.5: K6 verifies approval evidence where K11
           requires it, per request. §17.7: `APPROVAL_REQUIRED` "Adds APPROVAL whenever this Grant is
           used, even below R4. K4 enforces it; K6 enforces it only where K11 also flags the scope
           entry". §17.8: "Which Actions require approval: Effective tier R4, plus any Grant carrying
           `APPROVAL_REQUIRED`". §17.20: local settings may "add `APPROVAL_REQUIRED` to tiers below R4".
           §17.8 authoring rule and A-23: the flag MUST be set on scope entries used by R4 capabilities.
           Locked consequences: the flag's locked effect is per request, at K6. The K4 approval triggers
           the locked text states are effective tier R4 (§17.8; §17.10), a Grant carrying
           `APPROVAL_REQUIRED` (§17.8) and the §17.20 local setting; the flag is not among them. The
           authoring rule sets a minimum and does not limit the flag to entries used by R4 capabilities;
           §17.7 contemplates flagged entries used below R4.
       [U] Whether a Plan that uses a flagged entry, and otherwise requires no approval, requires
           approval at K4 is not defined by the locked text. That is the only case in which the flag,
           treated as a Plan-level trigger, could change whether the Plan requires approval. It remains
           unresolved; DEC-090 does not define it.
       [OI] Owner ruling (option C, 2026-10-03), an owner interpretation and not something §17
            establishes:
           (i) K4 does not treat the K11 flag itself as a Plan-level approval trigger;
           (ii) K6 remains responsible for the locked per-request enforcement of the flag;
           (iii) where a Plan contains a K11-flagged scope entry and no other approval requirement
                 applies (no §17.8 trigger, no applicable §17.20 local setting), K4 does not authorize
                 the Plan: it refuses it as an unsupported case, failing closed, and records the refusal
                 under the already-locked audit semantics for Plan Authorization (an A2 denial). No
                 approval trigger and no authority path is created.
       D89-22 (recorded only in k4core/IMPLEMENTATION_BOUNDARY.md) states that the flag "remains an
       additional locked input/condition"; the current implementation reads that as a Plan-wide K4
       trigger. DEC-090 does not adopt or ratify D89-22; D90-3 governs its flag bullet.
D90-4  Q3 — Authentication and observation times later than K4's clock.
       [L] §17.7: `AUTH_FRESH(max_age)` holds when "The Authentication Context's authentication time is
           within `max_age`"; `PLAN_MAX_AGE(max_age)` when "At Decision time, the Plan's newest input
           observation is within `max_age`". §17.10: REAUTH requires "the authentication time is within
           the tier's configured maximum age when the Decision is made". §17.16: "if authorization
           cannot be positively established, the Action is refused"; A-13: a condition that cannot be
           evaluated counts as false. No locked text defines clock skew or the treatment of an
           authentication or observation time later than K4's clock. P2/K3 §P.4.1 ("not yet valid")
           concerns the assertion's own validity window, checked in step-1 verification, which is
           abstract in this slice (DEC-089 D89-4); it does not govern authentication-time freshness.
       [OI] An authentication time or newest-observation time later than K4's current clock, by any
            amount, does not satisfy `AUTH_FRESH`, REAUTH, `PLAN_MAX_AGE` or the Plan maximum age
            applied at Decision time (§17.11; §17.19) (owner confirmation of "any amount", 2026-10-03).
            It fails closed through the existing locked paths only: a condition that does not hold (that
            Grant does not match; a denial, recorded as A1 or A2, follows where no other Grant covers,
            §17.4.2), a REAUTH failure (A2 denial) or a Plan maximum-age failure (A2 denial). No
            clock-skew tolerance, timestamp protocol or error path is created. Introducing a tolerance
            would require a further owner decision. The current implementation treats such times as
            fresh and must be corrected (D90-7(b)).
D90-5  Q4 — Grants whose subject is a built-in Role.
       [L] §17 Terms: a Grant "confers one Permission on a HUMAN Principal or a Role". §17.4.1: the
           Grant subject is "`principal_id` (HUMAN only) or a built-in `role_id`". §17.4.2: a Permission
           is held through "at least one effective Grant (direct, or through an ACTIVE Role
           Membership)". §17.3: "built-in, immutable, release-defined roles only"; a Role's "Grants are
           evaluated exactly like direct Grants". §17.20: the release baseline contains the built-in
           Roles. Locked §19 DC-07: Grants are K7 authorization state. §17.16: unavailable Grant state
           denies HUMAN Actions, and "if authorization cannot be positively established, the Action is
           refused".
       [U] The locked text does not specify how a K7 Grant row whose subject is a built-in `role_id`
           relates to that Role's release-defined bundle: it permits such a subject while describing
           Roles as immutable and release-defined. §17.4.2 counts Grants held "through an ACTIVE Role
           Membership" and §17.3 evaluates a Role's Grants "exactly like direct Grants", but neither
           says whether a K7 Grant row naming a Role adds to the release-defined Role, which §17.3 calls
           immutable. That treatment remains unresolved; DEC-090 defines no Role-Grant semantics and
           does not modify the Grant model.
       [OI] This slice creates no Role-subject Grant rows (DEC-089 D89-10, D89-11). K4 does not silently
            ignore one. Where, in an evaluation at §17.22 step 4, 7 or 10, K4 encounters any K7 Grant
            row whose subject is a Role the evaluated Principal holds through an effective Role
            Membership, whether or not that row would match, the evaluation fails closed as Grant state
            that cannot be positively established (§17.16): at steps 4 and 7 the request is denied (A1
            or A2); at step 10 the approval is rejected (A4). The current implementation's ignore rule
            is withdrawn and must be corrected (D90-7(c)).
D90-6  Q5 — `plan_ref`, Plan identity and Decision invalidation (owner selection (a), 2026-10-03).
       [L] §17.11: "The Decision is bound to `plan_digest`. The Plan refers to its Decision"; "Any
           change to the Plan changes its digest and requires a new Decision. The old Decision becomes
           `INVALIDATED`." §17.14 (Plan invalidated: "Its Decision becomes `INVALIDATED`"). A-24.
           §17.19: a Decision binds the Principal, the Authentication Context reference, the capability
           set, the Action, the target set, `plan_digest`, the policy revisions, the Grants used, the
           required step-up and `expires_at`. A-26. §16.3: `plan_ref`'s "Created by" entry is "K4".
           §21.7: `plan_ref` has origin "K4" (generated by K4). Locked §19 DC-09, DC-10. DEC-089 Q4: K4
           "may write the locked `INVALIDATED` DC-09 status when the Plan changes, subject to the
           existing atomicity/audit contract".
           Locked consequence: a Decision is bound to one Principal, one Action and one `plan_digest`.
       [U] The locked text does not define what makes a later proposal a change to an existing Plan
           rather than a new Plan, or how a proposal identifies the Plan it changes; the K5 proposal
           interface is excluded (DEC-089 D89-5). Plan-change identity remains unresolved and is routed
           to the §17/K4 Architecture Gate or a later owner decision. DEC-090 creates no Plan-identity
           rule.
       [OI] Owner rulings (Q5 option (a)):
           (i) a denied Plan commit has no invalidation effect (a standing rule);
           (ii) no Plan commit invalidates a Decision bound to another Principal (a standing rule);
           (iii) `plan_ref` is generated by K4 and is not taken from the Plan proposal. This is the
                 owner's reading of the §16.3 "Created by" entry "K4" and the §21.7 Origin "K4"; those
                 passages describe the P6 request field and the audit field and do not mention the Plan
                 proposal; (iv) until Plan-change identity is defined, K4 writes no `INVALIDATED` status
                 in this slice. No Plan change can yet be identified, so the condition "when the Plan
                 changes" (DEC-089 Q4), and the Plan-change condition of §17.11, D89-9(d) and D89-10(c),
                 cannot be established; §17.11 is not displaced and applies once identity is defined.
                 A-24 is unaffected: every authorized Plan commit creates its own new Decision bound to
                 its own `plan_digest`.
           The current implementation takes `plan_ref` from the proposal, treats a matching `plan_ref`
           as Plan identity and invalidates on denied and cross-Principal commits; it must be corrected
           (D90-7(d)).
D90-7  Required corrections (documented, not implemented). The following corrections to commit 94bfdc1
       are required by D90-3 … D90-6. They are not made by this decision and require a separate
       owner-authorized implementation task:
       (a) Q2: replace the K11-flag Plan-wide approval trigger with the D90-3(iii) refusal: a Plan that
           uses a flagged entry and otherwise requires no approval is refused (A2 denial); a Plan that
           requires approval on another ground is unaffected by the flag as a Plan-level trigger.
           DEC-090 does not decide which requests within an approval-requiring Plan are
           approval-requiring.
       (b) Q3: treat an authentication time or newest-observation time later than K4's clock as not
           fresh in `AUTH_FRESH`, REAUTH and `PLAN_MAX_AGE`, including the policy Plan maximum age.
       (c) Q4: replace the Role-subject Grant ignore rule with the D90-5 fail-closed denial at steps 4,
           7 and 10.
       (d) Q5: generate `plan_ref` in K4; stop using a proposal-supplied `plan_ref` as Plan identity;
           write no `INVALIDATED` status; ensure a denied commit has no DC-09 effect and no commit
           affects another Principal's Decision; preserve A-24, re-basing the current
           one-Decision-per-digest check, which is keyed on the proposal's `plan_ref`, once `plan_ref`
           is generated by K4. The re-based check creates no Plan-identity rule and no cross-Principal
           effect; if it cannot be keyed without one, the key choice returns to the owner.
       (e) Update k4core/IMPLEMENTATION_BOUNDARY.md and the affected tests to match.
D90-8  Locked architecture, owner interpretation and implementation choice. Python, SQLite, SHA-256, the
       K7 schema, internal data structures and module layout remain implementation choices under DEC-089
       D89-17. They are not architecture and acquire no architectural meaning from DEC-090.
D90-9  Non-effects. DEC-090 does not amend or change §15, §16, §17, locked §19, locked §21, locked §22
       or the locked P2/K3 gate, and authorizes no architecture amendment. It does not reopen DEC-089;
       DEC-089 Q4 stands. DEC-090 does not adopt or ratify D89-22, which remains recorded only in
       k4core/IMPLEMENTATION_BOUNDARY.md; D90-3 governs its flag bullet. It creates no authority path,
       no subsystem and no implementation scope, and does not itself authorize any code change. It does
       not decide P2, P3, authentication protocol, Ed25519, CBOR, K5, K6, K8, K11 implementation, Job
       state, Phase IV, A3, A5, administrative mutation, recovery, CyberPanel or host operations.
       DEC-029 remains controlling. Unresolved semantics remain unresolved: Action-to-Plan realization
       (D90-2), the K4 meaning of a flagged entry in a Plan otherwise requiring no approval and the
       request-level mapping within an approval-requiring Plan (D90-3), any clock-skew tolerance
       (D90-4), Role-subject Grant semantics (D90-5) and Plan-change identity (D90-6). No item of
       DEC-090 may be read as permission to resolve another open question. DEC-001 … DEC-089 are
       unchanged.
```

> **Transcription note (session process):** The first owner message is reproduced from its purpose, question,
> out-of-scope, implementation-boundary, draft-requirement, no-code and authorization sections; its starting-state,
> source-review, adversarial-review, adoption and final-report sections governed only this change set and are omitted.
> The second and third owner messages are reproduced in full. The second selects option (a) for Q5 and confirms the
> "any amount" reading for Q3; the third selects option C for Q2. The options were presented in the pre-adoption
> reviews of 2026-10-03.

> **Index note (not owner wording):** DEC-090 records owner interpretations for five semantic questions exposed by the
> first Phase 6 implementation, separating locked requirements from owner interpretations and open questions. It
> confirms Q1, reverses the implementation's readings on Q2 (a flagged entry in a Plan otherwise requiring no approval
> is refused) and Q4, sets future times as not fresh (Q3), and for Q5
> forbids denied and cross-Principal invalidation and suspends `INVALIDATED` writes until Plan-change identity is
> defined. It amends nothing and implements nothing; corrections are listed in D90-7.

---

## DEC-091 — Routing of Open P2 Verification Questions

- **Status:** CURRENT (adopted — routing only; K4-side items assigned to the §17/K4 Architecture Gate; no technical answer; no amendment)
- **Source:** Owner routing-decision request (2026-10-03); owner correction instruction (2026-10-03); owner adoption
  authorization of candidate v4 (2026-10-03).
- **Related:** DEC-023; DEC-051 (R01b); DEC-063; DEC-064; DEC-068 (D68-D, D68-J, D68-M); DEC-075 (D75-3); DEC-078;
  DEC-079 (D79-8); DEC-080 (D80-2, D80-5, D80-7); DEC-081; DEC-082 (D82-22); DEC-085 (D85-11); DEC-087; DEC-088
  (D88-2, D88-6); DEC-090 (D90-1, D90-6); §15.6; §15.10; §17.2; §17.22; §21.7; §21.14; P2/K3 §P.3.1, §P.4, §P.10

```text
OWNER ROUTING-DECISION REQUEST (2026-10-03)

==================================================
TASK
==================================================

DO NOT resolve the underlying technical questions yet.

Instead, prepare a narrowly scoped OWNER ROUTING DECISION that addresses only the fact that these P2-scope questions have no established route.

This is a DRAFTING TASK ONLY.

Do NOT implement anything.

Do NOT modify §15, §16, §17, §19, §21, §22 or P2/K3.

Do NOT modify code.

Do NOT commit.

Do NOT push.

Do NOT adopt the decision yet.

==================================================
DECISION SCOPE
==================================================

The draft decision may establish routing for exactly these questions:

R-1:
What concrete value represents the P2 `audience` field's "SCC instance", and how K4 obtains the expected value / how the assertion issuer obtains the corresponding value.

R-2:
What persistence/lifecycle semantics apply to the K4 assertion replay record required by §P.4.2, including behavior across K4 restart, host restart and recovery where relevant.

R-3:
How P2 rejection conditions that are explicitly named in §P.4.1 but not individually represented in the current §21 B2 `failure_reason` vocabulary are to be handled at the architecture level, specifically:
- not-yet-valid assertion;
- unknown `key_id`;
- retired `key_id`.

IMPORTANT:

R-3 is NOT necessarily a separate owner question.

First determine whether it can safely be routed together with the verification contract rather than creating unnecessary decision surface.

Do not decide its mapping.

==================================================
WHAT THE ROUTING DECISION MUST NOT DO
==================================================

It must NOT decide:

- the audience value;
- audience storage;
- audience provisioning;
- replay storage domain;
- replay persistence;
- replay restart semantics;
- recovery behavior;
- K2 implementation;
- K4 implementation;
- P2 protocol changes;
- §19 data-class assignment;
- §22 provisioning;
- CyberPanel installation mechanics.

It must NOT reopen or amend the locked P2/K3 protocol.

It must NOT add either question to OD19-01.

It must NOT declare that an existing gate owns these questions unless the existing architecture actually provides a valid route.

==================================================
SOURCE HIERARCHY
==================================================

Use:

- DEC-023 hierarchy;
- DEC-064 gate naming/provenance;
- DEC-063 / DEC-075 post-lock §19 routing;
- DEC-078 post-lock §22 routing;
- DEC-080 P2 scope;
- DEC-088 P2/K3 lock;
- §P.3.1, §P.4.1, §P.4.2, §P.4.3;
- §17.22 step 1;
- §21.7 / §21.14 B2 semantics;
- the read-only investigation just completed.

Do not infer a post-lock P2 amendment mechanism that does not exist.

==================================================
ROUTING QUESTION
==================================================

The draft must answer:

"What existing authority or gate is empowered to resolve these questions without silently changing the locked P2/K3 contract?"

If the answer is "none", the decision should explicitly establish a narrowly scoped route.

Do not choose the underlying technical answer.

==================================================
PREFERRED ROUTING SHAPE
==================================================

Draft the decision so that:

- the P2/K3 contract remains locked;
- the questions are recognized as unresolved P2-scope dependencies;
- an explicitly named owner/gate is authorized to resolve them;
- any resulting change to a locked P2/K3 passage must follow the established owner-decision / amendment hierarchy;
- §19 placement decisions remain subject to §19's existing route;
- §22 provisioning decisions remain subject to §22's existing route;
- CyberPanel-specific constraints remain subject to the K2 gate;
- no implementation authority is granted.

If no existing gate can legitimately be named, say so rather than inventing one.

OWNER CORRECTION INSTRUCTION (2026-10-03)

Required correction:

1. In D91-2(c), remove only the phrase:
   "has expired"

   R-3 must list exactly:
   - not yet valid
   - unknown `key_id`
   - retired `key_id`

2. In the R-3 [U] row in §4, remove only the phrase:
   "has expired"

   Again, R-3 must list exactly:
   - not yet valid
   - unknown `key_id`
   - retired `key_id`

Do not make any other substantive, stylistic, citation, terminology, or structural changes.

ADOPTION AUTHORIZATION (2026-10-03)

We are now adopting Candidate DEC-091 v4.

This is an OWNER DECISION ADOPTION operation.

Before editing:
1. Read the complete DEC-091 v4 scratchpad draft.
2. Confirm it is the v4 draft whose only changes from v3 were:
   - removal of "has expired" from D91-2(c);
   - removal of "has expired" from the R-3 [U] row;
   - title changed v3 → v4.
3. Confirm the prior read-only verification reported NOT READY only because of that R-3 scope defect, and that the mechanical v4 correction subsequently passed.
4. Do not reopen the architecture review.
5. Do not alter the substantive decision.

ADOPTION RULES:

- Adopt DEC-091 v4 exactly as written.
- Preserve the owner wording and structure.
- Do not rewrite, summarize, normalize, or "improve" the decision.
- Do not add technical answers for R-1, R-2, or R-3.
- Do not assign the K2 issuer-side of R-1.
- Do not amend P2/K3.
- Do not amend §15, §16, §17, §19, §21, or §22.
- Do not extend OD19-01.
- Do not create a general P2 amendment route.
- Do not create a general gate-convening procedure.
- Do not authorize implementation.

DEC-091 adoption must preserve these substantive boundaries:

R-1:
- K4-side expected `audience` value / acquisition is assigned to the §17/K4 Architecture Gate.
- K2 issuer-side `audience` remains unresolved and returns to the owner.
- No audience value is selected.

R-2:
- Replay-record persistence/survival is assigned to the §17/K4 Architecture Gate.
- No persistence mechanism, storage class, restart behavior, or recovery behavior is selected.

R-3:
- ONLY:
  - not yet valid
  - unknown `key_id`
  - retired `key_id`
- This is a classification question against the existing §17.22 step-1 / §21 `failure_reason` contract.
- No new failure reason is created.
```

Decision text (candidate DEC-091 v4, §2–§8, adopted by the authorization above):

```text
## 2. Owner question
Which existing authority, if any, may determine three matters that real K4 assertion verification needs and that
locked text does not determine at that level — the `audience` value K4 compares against (R-1), the persistence and
lifecycle of K4's assertion replay record (R-2), and the §17.22 step-1 check under which certain §P.4.1 rejections
are recorded in B2 `failure_reason` (R-3) — given that P2/K3 and §21 have no post-lock change route and no existing
gate's recorded agenda includes these matters?

## 3. Owner dispositions (draft)

D91-1  Recognition. R-1, R-2 and R-3 are matters that the locked text (P2/K3 §P.3.1, §P.4.1, §P.4.2; §17.22 step 1;
       §21.7) does not determine at the level real verification requires. This decision does not revisit the
       DEC-088 D88-6 lock evaluation or DEC-088's lock, and does not add these matters to OD19-01.
D91-2  Owner assignment. By this decision the owner extends the remit of the §17/K4 Architecture Gate — which DEC-064
       named as the owning architecture for Q19-04 only — to the following K4-side matters:
       (a) R-1, K4 side: what K4 compares an assertion's `audience` against, and how K4 obtains that expected value;
       (b) R-2: the persistence and lifecycle of the replay record K4 keeps under §P.4.2, including behaviour
           across K4 restart, host restart and restore within the validity window;
       (c) R-3: under which §17.22 step-1 check each of the §P.4.1 conditions not yet valid, and has an
           unknown or retired `key_id` is recorded in B2 `failure_reason`.
       This is an owner assignment, not a reading of DEC-064 or DEC-090. It does not convene the gate, does not make
       it a P2/K3, §17 or §21 amendment gate, transfers no responsibility between K2–K11, and decides none of (a)–(c).
D91-3  Not assigned. The issuer side of R-1 — what K2 places in `audience` and how K2 obtains it — is not assigned
       by this decision. It has no existing route and returns to the owner for an explicit decision. Anything later
       determined to be DC-18 assertion-verification material stays in OD19-01 under DEC-051 R01b; the §17/K4
       Architecture Gate does not act as the "P2" party in that coordination.
D91-4  Form of outcome. Any determination on (a)–(c) is recorded by the owner as a new DEC in the decision log,
       recording [L], [OI] and [U] determinations where locked text leaves the matter open, in the form of DEC-090
       D90-1. It does not add to, amend or supersede locked P2/K3, §17 or §21 text, and those documents are not edited.
D91-5  Locked text. No route exists to change locked P2/K3 text (DEC-080 D80-7: "No post-lock route is created
       now") or locked §21 text (DEC-085 D85-11), and this decision creates none. A determination that would require
       changing locked P2/K3 or §21 text is not made through this route and returns to the owner for an explicit
       decision. For §15 and §17 no amendment path is established (DEC-082 D82-22: "§17 has no amendment route";
       DEC-064 item 2; DEC-068 D68-J; cf. DEC-078 D78-3). A §16 change is possible only through the §16 Amendment Gate, subject to a separate assignment under
       DEC-068 D68-D.
D91-6  §19 consequences. A §19 consequence that resolves an item already recorded in §19.21–§19.22 uses DEC-075 D75-3
       and DEC-063. Any other §19 change — for example a data-class, owner or storage-domain assignment for the replay
       record or for a persisted expected `audience` value — has no existing route and returns to the owner for an
       explicit decision (DEC-081 confirmations 4–5; D81-6). This decision does not apply or extend DEC-063 or D75-3.
D91-7  §22 consequences. A §22 change required by a determination proceeds only where DEC-078 D78-1 admits it;
       otherwise it returns to the owner for an explicit decision. This decision does not extend DEC-078.
D91-8  Platform-specific aspects. A CyberPanel-specific aspect of a determination is for the CyberPanel K2 gate only
       if it falls within K2-Q1 … K2-Q7 (DEC-080 D80-5); otherwise it returns to the owner. This decision adds nothing
       to that gate's question list.
D91-9  Gate procedure. The §17/K4 Architecture Gate has no procedural framework. Convening it, admitting items
       (including Q19-04, the DEC-090 D90-6 item and D91-2 (a)–(c)) and recording outcomes require a later owner
       decision; apart from the recording form in D91-4, this decision establishes no procedure and does not apply
       DEC-068.
D91-10 Non-effects. See section 5.

## 4. Locked-source basis

R-1 `audience`
- [L] §15.10 P2 row: "audience-bound (SCC)"; §15.6: K2 may "issue a short-lived, audience-bound identity assertion";
  §17.2 and §17.22 step 1: K4 verifies "audience"; P2/K3 §P.3.1: "`audience`, identifying the SCC instance the
  assertion is for"; §P.4.1: K4 rejects an assertion that "carries the wrong `audience`".
- [L] DEC-080 D80-2: "audience binding" is P2 scope.
- [U] The concrete value; its creator, owner, storage, provisioning and lifecycle; how K4 obtains the expected value;
  how K2 obtains the value it places.
- [OI] The K4-side aspect is assigned to the §17/K4 Architecture Gate by owner assignment (D91-2(a)); the issuer side
  is not assigned (D91-3).

R-2 replay record
- [L] §17.22 step 1 "single use"; §15.10 P3: "K4 enforces assertion freshness and single use where applicable";
  §P.4.2: "K4 records `assertion_id` for the assertion's validity period and rejects any second use"; §P.4.3: "Replay
  rejection is K4's; K3 performs none and holds no replay state"; DEC-088 D88-2(c): validity window at most 60 seconds;
  single use unchanged.
- [L] DEC-080 D80-2: "freshness and replay resistance" are P2 scope.
- [U] Whether the record survives K4 restart, host restart or restore within the validity window; its §19
  classification, owner and storage domain. (§P.7.6 volatility concerns SCC sessions only.)
- [OI] Assigned to the §17/K4 Architecture Gate by owner assignment (D91-2(b)); §19 consequences per D91-6.

R-3 step-1 classification of rejections
- [L] §21.7 `failure_reason`: "The §17.22 step-1 check that failed", with §21 semantics "the checks are §17's";
  §21.14; §17.22 step 1 lists signature, audience, freshness and single use; §P.4.1 lists not yet valid, expired,
  wrong `audience`, unknown or retired `key_id`, and signature failure. P2/K3 §P.10: P2/K3 does not own "§21 audit
  records".
- [U] Under which step-1 check the §P.4.1 conditions not yet valid, and has an unknown or retired `key_id`
  are recorded.
- [OI] R-3 is a §17.22 step-1 classification question and is assigned with R-1(a) and R-2 as part of K4's step-1
  verification (D91-2(c)); if no existing check fits, D91-5 applies.

Routing
- [L] DEC-080 D80-7 "No post-lock route is created now"; DEC-085 D85-11 (no §21 route).
- [L] DEC-064: the §17/K4 Architecture Gate is named for Q19-04, "not a new §17 amendment gate. §17 remains locked";
  §19.21.1 Q19-04: "(NOT SCHEDULED). This is not a §17 amendment gate; §17 remains LOCKED."
- [L] DEC-090 D90-6 routed a §17.11 question (Plan-change identity) to "the §17/K4 Architecture Gate or a later owner
  decision".
- [L] DEC-068 D68-D: new §16 Amendment Gate items need a separate owner decision; D68-M: DEC-068 "creates no … gate,
  and assigns nothing to K4, K9, §17 or §22".
- [L] DEC-063; DEC-075 D75-3; DEC-081 confirmations 4–5 and D81-6: §19 post-lock route limited to recorded items.
- [L] DEC-078 D78-1 … D78-4: §22 post-lock route; no general authority.
- [OI] The extension of the §17/K4 Architecture Gate's remit to D91-2 (a)–(c).

## 5. Non-effects
This decision does not amend or supplement P2/K3; does not decide the `audience` value, its storage or provisioning;
does not decide replay persistence, storage domain, restart or recovery behaviour; does not decide the R-3
classification; does not amend §15, §16, §17, locked §19, locked §21 or locked §22; makes no §19 assignment and no §22
provisioning decision; does not apply or extend DEC-063, DEC-075 D75-3 or DEC-078; does not revisit DEC-088 or its lock
evaluation; adds nothing to OD19-01 or to the CyberPanel K2 gate's question list; does not convene the §17/K4
Architecture Gate or the §16 Amendment Gate and establishes no gate procedure; creates no P2/K3 amendment mechanism;
transfers no responsibility between components; authorizes no implementation; does not alter DEC-051, DEC-064 (beyond the
D91-2 owner extension of the named gate's remit), DEC-079, DEC-088, DEC-089 or DEC-090. DEC-029 remains standing.

## 6. Routing mechanics
1. A later owner decision establishes how the §17/K4 Architecture Gate is convened, admits items and records outcomes
   (D91-9). This decision does none of that.
2. Each determination on D91-2 (a)–(c) is recorded by the owner as a new DEC with [L]/[OI]/[U] determinations, without editing
   any locked document (D91-4).
3. Consequences:
   - a change to locked P2/K3 or §21 text → returns to the owner (D91-5);
   - §15 or §17 → no amendment path is established (D91-5);
   - §16 → only through the §16 Amendment Gate after a D68-D assignment (D91-5);
   - §19 → DEC-075 D75-3 / DEC-063 only for items already recorded; otherwise back to the owner (D91-6);
   - §22 → only where DEC-078 D78-1 admits it; otherwise back to the owner (D91-7);
   - CyberPanel-specific → K2 gate only within K2-Q1 … K2-Q7; otherwise back to the owner (D91-8);
   - the issuer side of R-1 → back to the owner (D91-3).
4. Implementation of real verification still requires its own owner implementation-authorization decision.

## 7. Dependencies
- OD19-01: [U] Whether any part of R-1 or R-2 is DC-18 material is not decided; anything determined to be DC-18
  material stays in OD19-01 under DEC-051 R01b (D91-3). OD19-01 independently blocks actual assertion-verification implementation
  (DEC-079 D79-8).
- §22 O-4 / O-15: unchanged; consequences per D91-7.
- CyberPanel K2 gate: per D91-8; DEC-025 sequencing unchanged.
- P2/K3: remains locked and unsupplemented (D91-4, D91-5).
- §19: per D91-6.
- §21: `failure_reason` contract unchanged; R-3 concerns classification only (D91-2(c), D91-5).

## 8. Source mapping
See section 4. Register §8 currently lists only Q19-04 for the §17/K4 Architecture Gate; if adopted, a register §8
pointer for D91-2 (cf. DEC-087 D87-2) would be the only bookkeeping beyond the decision-log entry; that is an
owner choice at adoption.
```

> **Transcription note (session process):** The owner routing-decision request is reproduced from its task, scope,
> exclusion, source-hierarchy, routing-question and preferred-shape sections; its draft-structure and process sections
> are omitted. The correction instruction is reproduced from its required-correction section and the adoption
> authorization from its opening through its adoption rules and boundaries; their edit-scope, mechanics, validation,
> commit and reporting sections governed only this change set and are omitted. The decision text is candidate v4
> reproduced verbatim from its §2 onward; the draft title line and §1 (candidate number) are drafting metadata and are
> omitted. The "(draft)" label in the §3 heading is part of the verbatim v4 text.

> **Index note (not owner wording):** DEC-091 is a routing decision. It assigns the K4-side aspects of three open P2
> verification questions (the expected `audience` value, the replay record's persistence, and the step-1
> classification of not-yet-valid and unknown or retired `key_id` rejections) to the §17/K4 Architecture Gate, leaves
> the K2 issuer side of `audience` with the owner, decides no technical answer, amends nothing and authorizes no
> implementation.
