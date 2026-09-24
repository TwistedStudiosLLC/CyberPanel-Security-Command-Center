> **Document status:** CURRENT — OWNER DECISIONS
> **Authority category:** 2 — Explicit owner decisions (see [Authority Hierarchy](../README.md#authority-hierarchy))
> **Source:** Owner messages in the SCC architecture sessions, recorded 2026-09-23. Each entry names its source message.
> **Normative:** Yes. Owner wording is reproduced verbatim inside fenced `text` blocks. Text outside those blocks
> (titles, status, cross-references) is an index added for navigation and is not owner wording. Entries record owner
> decisions. They do not themselves amend or lock §15–§17 (DEC-064).
> **Numbering note:** D-2 was not issued as an owner decision. The reconciliation item D-2 (presentation placement)
> was addressed by owner decision D-15. DEC-030 records the Phase A.5 confirmation and was added after the
> Phase A.5 plan listed DEC-001 … DEC-029. DEC-031 … DEC-064 record the §19 owner disposition review and its
> change-set reconciliation.

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
