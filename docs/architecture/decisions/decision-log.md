> **Document status:** CURRENT — OWNER DECISIONS
> **Authority category:** 2 — Explicit owner decisions (see [Authority Hierarchy](../README.md#authority-hierarchy))
> **Source:** Owner messages in the SCC architecture sessions, recorded 2026-09-23. Each entry names its source message.
> **Normative:** Yes. Owner wording is reproduced verbatim inside fenced `text` blocks. Text outside those blocks
> (titles, status, cross-references) is an index added for navigation and is not owner wording.
> **Numbering note:** D-2 was not issued as an owner decision. The reconciliation item D-2 (presentation placement)
> was addressed by owner decision D-15. DEC-030 records the Phase A.5 confirmation and was added after the
> Phase A.5 plan listed DEC-001 … DEC-029.

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
