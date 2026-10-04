> **Document status:** LOCKED
> **Authority category:** 1 — Locked architecture (see [Authority Hierarchy](../README.md#authority-hierarchy))
> **Source:** §15 approved text — DEC-001 (approved at the §16 gate; restated as locked at the §17 and §18 gates), DEC-022 (D-10)
> **Normative:** Yes
> **Findings against this text:** none recorded inline (DEC-030, Q2). See [Known Findings Against Locked Text](../README.md#known-findings-against-locked-text): KF-01, KF-02, KF-03, KF-08.
> **Transcription notes:** Normative text reproduced verbatim. Removed process-wrapper text only: the opening italic
> line ("Candidate text for architecture-owner review. It covers only this gate and does not design §16–§22. I made
> no files or repository changes.") and the closing line ("I'm stopping here. I'll wait for your review before
> starting §16."). The second opening italic line (on "(verify)" markers) is retained because it qualifies the
> text. The Gate Assessment is retained as part of the approved text; its permissions for §16 are historical
> (§16 is complete and locked).

# SCC §15 — Runtime Topology & Trust Boundaries

*Anything marked (verify) about CyberPanel internals comes from general platform knowledge, not a check of a current release. No decision below depends on those details: CyberPanel is treated as root-equivalent either way.*

---

## 15.1 Purpose

This section fixes where SCC code runs, under which OS identities, with what privilege, and which component is trusted to decide or do what. Its goal is to make the §1–§14 doctrine enforceable **by construction**, so it does not depend on developers following convention. Specifically:
- "no generic shell"
- "capability ≠ authorization"
- "the UI is not the security authority"
- "least privilege"
- "Integration isolation"
- "CyberPanel failure must not take down SCC"

It resolves audit finding CRIT-01 and provides the process boundary that CRIT-02 requires. It deliberately leaves the executor operation vocabulary (§16), the authorization model (§17), the full threat model (§18), and recovery authority (a later gate) undefined.

## 15.2 Architectural Scope

**In scope:**
- runtime components
- process and OS-identity boundaries
- privilege placement
- communication paths and trust direction
- credential placement by class
- failure isolation at component granularity
- lifecycle independence from the parent platform
- topology-level trust assumptions

**Out of scope:**
- operation vocabulary and request schemas (§16)
- principals, roles, grants, step-up mechanisms (§17)
- adversary catalogue (§18)
- storage engine, secrets store design, retention (§19)
- reconciliation semantics (§20)
- event model (§21)
- installer, bootstrap, recovery authority (§22 / recovery gate)
- IPC technology selection

**Scope rule:** everything here must remain true for any future Platform Adapter (CyberPanel, cPanel, DirectAdmin). CyberPanel appears only as the first instance of "Parent Platform".

## 15.3 Runtime Components

### 15.3.1 Evaluation of the starting hypothesis

The proposed hypothesis (CyberPanel → SCC Web/Platform Adapter → Core → Integration Host / Executor → Host) points in the right direction. It is not sufficient as written, for seven reasons:

| # | Defect in hypothesis | Consequence if copied | Correction |
|---|---|---|---|
| H-1 | "SCC Web / Platform Adapter" is one box. Some adapter code *must* run inside the parent platform (navigation, session access), and some must not. | Either all SCC web code lands in CyberPanel's process (inheriting its privilege and upgrade lifecycle), or the identity bridge is left undefined. | Split the logical Platform Adapter into three physical parts: **Platform Bridge** (in-platform), **Presentation Adapter** (in the Gateway), and **Platform Services** (in the Integration Host). |
| H-2 | Web → Core is "authenticated IPC", which implies Core trusts the Web tier's statement of *who the user is*. | A compromised Web tier can impersonate any user to Core. This is a confused deputy: the most exposed component becomes the identity authority. | Identity travels **end-to-end** from the Platform Bridge to Core as a verifiable assertion. The Gateway relays it but cannot mint it. |
| H-3 | It is silent on *observation*. Only actions visibly reach the Executor. | Integrations or Core would read the host directly: a second, unmediated host-access path, with unverifiable evidence provenance and root-only reads implemented ad hoc. | **All** host access, reads included, crosses the Executor boundary. Operations are classed read or write. |
| H-4 | Nothing says the Integration Host cannot reach the Executor or the host directly. | CRIT-02 stays open. | Integration Host has no host access and no path to the Executor. Its only channel is to Core. |
| H-5 | Nothing says the Executor trusts Core *without limit*. | A compromise of Core (a large, unprivileged, complex process) becomes arbitrary root. | The Executor takes vocabulary and per-Integration scope from **root-owned install-time declarations**, never from requests. A compromised Core is therefore bounded to declared scopes. |
| H-6 | The state store, execution record, local operator path, and service supervisor are all missing. | Engineers would co-locate SCC state with CyberPanel's database, lose any record of executed privileged effects when Core is compromised, and invent a web-based recovery path. | Add these components explicitly. |
| H-7 | Platform-specific backend knowledge (panel version, panel-managed security features, web server layout) has no home. | It leaks into Core or into every Integration (audit HIGH-11). | Platform Services runs as a worker in the Integration Host tier under Integration constraints. |

### 15.3.2 Component catalogue

"Trusted" here means **"its decisions are relied upon by other components within a stated scope"**. It does not mean "safe".

| ID | Component | Responsibility | Process boundary | OS identity | Privilege | Trusted? | Security-sensitive? | May hold credentials? | May perform privileged host ops? |
|---|---|---|---|---|---|---|---|---|---|
| K0 | **Browser** | Render UI, carry the user's session | Remote client | n/a | None | **No**, untrusted input source | Yes (attack origin) | Platform session and SCC session tokens only | No |
| K1 | **Parent Platform** (CyberPanel) | Host panel, login, navigation, parent theme | Platform's own processes | Platform's (treated as root-equivalent) | Root-equivalent (assumed) | Trusted **for identity and presentation only**; part of the host TCB | Yes | Its own credentials | Its own business, outside SCC control |
| K2 | **Platform Bridge** | The SCC-supplied extension loaded via the platform's supported extension mechanism: navigation registration, page frame in the Parent Theme, reading the platform session, issuing identity assertions, and (adapter-dependent) relaying requests to the Gateway | **Inside K1's process / trust domain** | K1's | K1's (inherited, never used by SCC) | Trusted exactly as far as K1 is: for identity | Yes | Assertion-signing key only | **No**. It has no SCC operation paths and must not call host operations on SCC's behalf |
| K3 | **SCC Gateway** (Web tier + Presentation Adapter) | Serve SCC UI assets; Presentation Adapter rendering; API shape validation; relay to Core; never decides | Separate SCC process | Dedicated unprivileged identity **W** | Unprivileged; no host access beyond its own files | **Not trusted** for identity, authorization, or state | Yes (exposed parser) | Transient relay of tokens; must not persist or log them | **No** |
| K4 | **SCC Core** | Domain authority: Registry, Inventory, compatibility evaluation, capability registration, authorization decisions, Plan validation and ownership, Job orchestration, scheduling, generic (product-neutral) discovery logic, state evaluation, audit coordination | Separate SCC process | Dedicated unprivileged identity **C** | Unprivileged. **Not root**, and no sudo or equivalent | Trusted to **decide**; not trusted to define what is physically possible | Highest non-root sensitivity | Assertion *verification* material, SCC session state, store access | **No**. Requests them from K6 |
| K5 | **Integration Host** | Runs Security Integration code and the Platform Services worker, **one worker per Integration**. Interprets observations, computes health, proposes Plans and operation requests | Separate process(es): one isolated worker per Integration, plus a supervisor | Dedicated unprivileged identity **I** | Unprivileged, no host access, no network | **Not trusted**. Output is untrusted data | Yes | **None** in plaintext (see §15.12) | **No** |
| K6 | **Privileged Executor** | The single place where host observation and host mutation physically occur. Enforces the closed vocabulary and root-owned scopes. Records what it did | Separate process, minimal code, loads no Integration code | **root** (or the narrowest identity §16 proves sufficient) | Privileged | Trusted to **enforce limits**; not trusted to decide authorization | Critical | Security System and platform credentials whose compromise would be privileged (§15.12) | **Yes, exclusively** |
| K7 | **SCC State Store** | Durable SCC data: inventory, registry state, Jobs, audit, authorization metadata, configuration | Exclusively SCC-owned (embedded or separate; engine deferred) | Accessible to **C only** | n/a | Trusted as a storage medium only | Yes | Its own access material, held by C only | n/a |
| K8 | **Executor Journal** | Append-only record, written by K6, of every request received and every physical effect attempted and observed | Root-owned storage written only by K6 | Writable by root/K6; readable by C | n/a | Trusted as evidence against Core compromise | Yes | None | n/a |
| K9 | **Local Administrative Interface** | Host-local operator tool, invoked only by OS root on the host. **Its authority is defined at the recovery gate**; this gate only fixes its topological position | Short-lived local process | Invoking identity must be root | Root (by who invokes it) | Trusted to the same degree as local root (which is outside SCC's boundary anyway, §15.15) | Yes | None persistent | Only through K6 or K4 (recovery gate decides) |
| K10 | **Host Service Manager** | Starts and supervises K3–K6 under their assigned identities; launches Integration workers with launcher-assigned identity binding | Host component | root | Host TCB | Trusted (host TCB) | Yes | None of SCC's | n/a |
| K11 | **SCC Install Tree** (static trust object, not a process) | Root-owned, non-writable-by-SCC-runtime location holding SCC code, built-in Integration code, **capability and scope declarations**, and trust anchors | Filesystem | Owned by root; not writable by W, C, I | n/a | Trusted as the source of what may exist and be done | Critical | Public trust anchors only | n/a |

### 15.3.3 Combination decisions

| Candidate merge | Decision | Reason |
|---|---|---|
| Gateway into Platform Bridge (all web code inside CyberPanel) | **Rejected** | It would tie SCC's UI and API to the platform's runtime and upgrade lifecycle (§15.14), and run SCC's exposed parser inside a root-equivalent process. Portability also suffers: each panel's in-process runtime differs. The Bridge stays deliberately thin. |
| Gateway into Core | **Rejected** | The Gateway is the component that parses attacker-controlled HTTP. Separating it means a parser compromise yields identity W, which has no store access, no authorization state, and cannot mint identity (H-2). The cost is one local hop. |
| Integration Host into Core | **Rejected** | CRIT-02. Integration code in Core's address space could forge Core decisions and read authorization data. Fault isolation (§14) also requires process separation. |
| Core into Executor | **Rejected** | That would put the largest codebase in a root process, which is precisely the failure the audit identified. |
| Separate read-class and write-class executors | **Not required at this gate. §16 is permitted to split.** | A single root process with mandatory operation classing is the minimal enforceable boundary. Splitting reduces blast radius for read bugs but doesn't remove root from reads that need it (e.g., control-socket queries). §16 decides. |
| Per-Integration workers vs. one shared Integration process | **Per-Integration isolation required** | This is needed for fault isolation, and so that Core can bind each request to an Integration identity the Integration cannot forge. |

**Additional components required beyond the five evaluated:** K2 (identity must originate inside the platform), K7 (state independence from the platform), K8 (a privileged-effect record that survives Core compromise), K9 (a non-web operator path, so recovery never needs a web bypass), K10 (process identities must be assigned by something other than the processes themselves), and K11 (the executor needs a source of limits that Core cannot write).

## 15.4 Process and Privilege Model

1. **Four distinct runtime identities:** W (Gateway), C (Core), I (Integration Host), and root (Executor). No two SCC runtime components share an identity. Distinct identities are what prevent one component from reading another's memory or files, signalling or tracing it, or impersonating it on a local channel. Names are an implementation detail; distinctness is not.
2. **Exactly one privileged SCC runtime component:** K6. K2 runs with the platform's privilege because it lives in the platform's process. SCC design must treat that privilege as the platform's and must never route SCC operations through it.
3. **Privilege flows only downward, through one boundary.** The only path from a user intent to a host effect is: Browser → K1/K2 → K3 → K4 → K6 → host. No lateral path exists, whether K3 → K6, K5 → K6, K5 → host, K2 → K6, or K4 → host.
4. **Decide vs. do:** K4 *decides* (authorization, Plan validity, Job sequencing). K6 *does* (physical effect), and *refuses* anything outside the vocabulary or declared scope regardless of K4's decision. Neither alone is sufficient for a state change:
   - K4 without K6 can change nothing on the host.
   - K6 without a K4 request initiates nothing.
5. **Observation is mediated too.** Generic discovery logic (product-neutral) lives in K4, and product-specific interpretation lives in K5. Both obtain host facts only through K6 read-class operations. This gives every piece of evidence a single provenance point, and puts root-only reads under the same controls as writes.
6. **Network posture.** No SCC process exposes an externally reachable listener. K3 is reachable only via the platform edge (§15.6). K5 has no network access. K4 and K6 have no default egress; any required egress (e.g., update retrieval) is a lifecycle concern for §22 and must be a declared K6 operation, not ambient capability.
7. **Code provenance.** K4, K5, and K6 load code only from K11. No runtime identity (W, C, I) can write to K11. Integrations are v1 built-in only, shipped in K11. Third-party code has no load path in this topology.

## 15.5 CyberPanel Boundary

**CyberPanel's roles:**

| Role | Is CyberPanel this? | Scope |
|---|---|---|
| Presentation host | **Yes** | Hosts navigation, page frame, Parent Theme |
| Identity provider | **Yes** | Authenticates the human; its session is the source of the identity assertion |
| Trusted computing base | **Yes, for identity and presentation**, and as part of the host TCB, because it is root-equivalent (verify its actual process privilege; the architecture assumes root-equivalence either way) | Whatever CyberPanel asserts about *who* the user is, SCC believes |
| Privileged execution authority for SCC | **No** | SCC never asks CyberPanel to perform SCC operations, and never runs SCC operations through CyberPanel's own command-execution facilities |
| Authorization authority for SCC | **No** | Platform role information is an *input* to §17. It is never sufficient on its own for an SCC action |
| Management authority over some Security Systems | **Possibly** (e.g., panel-managed ModSecurity/firewall settings) | This is a *domain* fact recorded in Inventory as external management (§5). It is not a topology role |

**Responsibilities:**
- **CyberPanel:** user authentication, its own session, the host page, and its own features and configuration.
- **SCC:** everything else about SCC: its own processes, data, authorization, Jobs, audit, host effects via K6, and the Bridge's correct use of platform extension points.

**If the parent panel is compromised:**
- **SCC can still guarantee:**
  - (a) No SCC operation outside the K6 vocabulary and K11 scopes is executed *by SCC*.
  - (b) Every SCC-executed privileged effect is recorded in K8 by K6, including effects requested under forged identity.
  - (c) SCC data and components do not depend on platform files for integrity.
  - (d) SCC's configuration of authorization still applies to whatever principal the platform asserts.
  - (e) Observation continues independently of panel availability.
- **SCC cannot guarantee:**
  - (a) That the asserted identity is genuine. A compromised identity provider can impersonate any user, including SCC administrators, within those users' SCC permissions.
  - (b) That UI shown in the panel page is what SCC sent, since panel scripts share the page.
  - (c) Anything about the host at all, because a root-equivalent panel can bypass SCC entirely and act on the host directly.

  The practical consequence is that §17 must provide approval factors for high-risk actions that do not travel through K1/K2 (see §15.18, OQ-4). Topologically, K9 is already such a path.

## 15.6 SCC Web / Platform Adapter Boundary

**Model: hybrid.** A thin **Platform Bridge (K2)** inside the platform and an independent **SCC Gateway (K3)** process.

- **K2 may:** register navigation through supported extension points; render the page frame that hosts SCC UI within the Parent Theme; read the platform session; issue a short-lived, audience-bound identity assertion; and, where the adapter requires, relay browser requests to K3.
- **K2 must not:** contain SCC domain logic, hold SCC authorization data, call K4 or K6 other than via K3's request path, invoke any host operation for SCC, or store SCC state.
- **K3 may:** serve SCC's UI assets from K11; run the Presentation Adapter (how SCC-defined content is expressed in the Parent Theme); validate request *shape* (a usability and robustness filter, explicitly **not** a security control); and relay requests plus the unmodified identity assertion or SCC session token to K4.
- **K3 must not:** decide authorization, mint or alter identity, cache state and present it as current when K4 is unavailable, access K7, reach K5 or K6, or persist or log platform session credentials it happens to receive.

**Why the UI cannot become the execution layer.** K3 runs as identity W. W has no path to K6 (the executor authenticates only C), no access to K7, and no host privileges. Even a fully compromised K3 can only send K4 requests K4 would accept from the authenticated user anyway. It can't forge who that user is, because assertion signing material lives only in K2.

**Browser → K3 request path.** Whether requests reach K3 by K2 relay or by a platform-supported proxy route is an adapter choice, and both satisfy this section. The constraint is that the path must not require modifying platform core files (see OQ-1).

## 15.7 SCC Core Boundary

**K4 is the sole authority for:**
- Registry state and Integration availability
- Inventory, including generic, product-neutral discovery logic
- compatibility evaluation
- capability registration (K4 *reads* capability and scope declarations from K11, and may *narrow* them but never widen them)
- authentication verification of identity assertions
- authorization decisions
- Plan validation and ownership (K5 proposes; K4 accepts, rejects, and stores)
- Job orchestration, sequencing, locking, and scheduling
- state evaluation
- audit coordination and writing SCC audit to K7

**K4 is explicitly not:**
- the physical actor on the host
- the definer of what is physically possible (K11 is)
- a trusted source of truth for what K6 actually did (K8 is the counter-record)

**K4 treats as untrusted input:**
- everything from K3 except the assertion signature it verifies itself
- everything from K5
- raw observations returned via K6, since they originate from Security Systems, which may be compromised

**Residual risk accepted at this gate:** a compromised K4 can issue any request an installed Integration's declared scope permits, under any Job, without genuine authorization. This is bounded privileged misuse, *not* arbitrary root, and K8 records it. Narrowing this further (e.g., approvals K6 can verify without trusting K4) belongs to §16/§17 and is listed in OQ-4.

## 15.8 Integration Host Boundary

**Integrations run in K5 and nowhere else.** They don't run in K3, K4, or K6. Platform Services (the Platform Adapter's host-knowledge component) also runs in K5, as its own worker, under identical constraints.

How K5 closes CRIT-02 topologically:
1. **No host access.** K5 workers can't read the host filesystem beyond their own runtime, can't spawn host tools, can't connect to Security System sockets or APIs, and have no network. The only thing an Integration can do to the world is send a message to K4.
2. **No path to K6.** K6 authenticates only identity C. Identity I can't reach it.
3. **Launcher-bound identity.** Each worker's channel to K4 is bound to exactly one Integration identity *by K10/K5's supervisor at launch*, never by the worker's own claim. K4 therefore always knows which Integration made each request and applies only that Integration's K11 scope.
4. **Declarations come from K11, not from the running code.** A worker can't declare, extend, or alter its capabilities or scope at runtime.
5. **Untrusted output.** Everything a worker returns is data: observations, interpretations, health results, Plan proposals, operation requests. K4 validates each item.

**Isolation level in v1:**
- **Fault isolation between Integrations is required.** One crash or hang must not affect others.
- **Security isolation between Integrations (distinct OS identity per Integration) is not required in v1**, because all v1 Integrations are built-in, signed, and equally trusted. It **is required before any non-built-in Integration is ever admitted.** That admission is out of scope for v1 per the constraints.

## 15.9 Privileged Executor Boundary

| Property | Rule |
|---|---|
| Process | Separate, dedicated, minimal. Loads no Integration code, no platform code, no plugins |
| OS identity | root, or a narrower identity if §16 demonstrates sufficiency |
| Who can authenticate to it | **Only identity C**, established by OS-enforced peer identity on a channel no other identity can open. K9 access is decided at the recovery gate and, if granted, is likewise OS-identity-bound (root) |
| Web tier direct access | **Never** |
| Integration direct access | **Never** |
| Is Core the only authorized caller | **Yes** for runtime (K9 pending the recovery gate) |
| What it trusts | K4's *authorization decision* for a well-formed request within bounds; K11 declarations (vocabulary membership, per-Integration scope, trust anchors); the host OS |
| What it does NOT trust | Request contents beyond schema and bounds; any scope or permission asserted *in* a request; UI or K3 validation; Integration declarations other than those read from K11 itself; K4 to be uncompromised (hence bounds plus K8); Security System output (returned as data, not interpreted into further actions) |
| What it records | Every request received, accepted or refused, and every physical effect attempted and observed, written to K8 before replying |
| What it never does | Initiate operations; interpret results into follow-up operations; decide authorization; accept operations not in the closed vocabulary; accept free-form commands |

## 15.10 IPC and Communication Boundaries

General rules for every local channel:
- It must be accessible **only** to its two endpoint identities.
- Authentication uses **OS-enforced peer identity** where available, so no transferable bearer secret exists.
- Every message is schema-bound.

IPC technology is not selected.

| # | Sender → Receiver | Purpose | Authentication | Authorization responsibility | Integrity | Confidentiality | Replay | Failure behavior |
|---|---|---|---|---|---|---|---|---|
| P1 | Browser → K1 | Login, page load | Platform's | Platform's | TLS (platform) | TLS (platform) | Platform's | Platform down → SCC UI unavailable (§15.13) |
| P2 | K2 → K3 | Relay request + identity assertion | Peer identity of the platform process; assertion signature (verified end-to-end by K4, not K3) | None at K3 | Assertion signed; channel local-only | Local-only channel; tokens not logged | Assertion short-lived, audience-bound (SCC), nonce/session-bound | K3 down → SCC pages show "SCC unavailable"; platform unaffected |
| P3 | K3 → K4 | API calls carrying assertion or SCC session token | Peer identity W **plus** end-user assertion/session validated by K4 | **K4** decides; K3's identity grants nothing on its own | Schema-validated by K4 | Local-only | K4 enforces assertion freshness and single use where applicable; state-changing requests carry request IDs (details §16/§17) | K4 down → K3 returns "unavailable" and must not serve stale state as current |
| P4 | K4 → K5 | Invoke Integration functions with supplied observations | K4 is the launcher-bound peer | None at K5 (K5 decides nothing) | Schema | Local-only; K4 passes only what the call needs | Invocation IDs | Timeout → Integration marked error; Security System remains visible |
| P5 | K5 → K4 | Results, Plan proposals, operation requests | Launcher-bound Integration identity | **K4** checks scope, class, and authorization | Schema; size- and rate-bounded by K4 | Local-only | K4 rejects requests not tied to an active invocation | Malformed or excess output → rejected and recorded; worker may be restarted |
| P6 | K4 → K6 | Structured read/write operation requests with correlation (Job, Integration identity) | Peer identity C only | K4 (decided); **K6 enforces bounds** | Schema; vocabulary membership; K11 scope | Local-only; channel inaccessible to W and I | Unique request IDs; K6 rejects duplicates (idempotency semantics §16) | K6 down → no observation, no action; Jobs held; K4 records unknown for in-flight work |
| P7 | K6 → K4 | Results, raw observations, outcome, journal reference | Peer identity root on the channel K4 opened | n/a | Schema; K4 treats observations as untrusted data | Local-only | Bound to request ID | Lost reply → outcome unknown until reconciled against K8 |
| P8 | K6 → Host/Security Systems | Physical observation and effect | n/a | Enforced by K6 bounds | n/a | n/a | n/a | Failure reported as-is; never converted to success |
| P9 | K6 → K8 | Execution record | Root-only write | n/a | Append-only (tamper-evidence mechanism §18/§19) | Root-owned; C read-only | n/a | Write failure → K6 refuses write-class operations (it can't record what it would do) |
| P10 | K4 ↔ K7 | Durable SCC state | Access restricted to identity C | K4 | Store-level | Store not readable by W or I | n/a | Store unavailable → §15.13 |
| P11 | K9 → K4 / K6 | Local operator actions | OS root, host-local only, never network-exposed | **Recovery gate** | Schema | Local | Recovery gate | Recovery gate |
| P12 | K10 → K3–K6 | Start, stop, supervise; assign identities | Host | Host | n/a | n/a | n/a | Restart per supervision policy |
| — | K4 → K1 (direct) | — | **Does not exist.** SCC reads platform state through Platform Services (K5) via K6 read ops, and changes platform state only via K6 write ops under §11's exceptional-edit rules | | | | | |
| — | K2 → K4 / K6 directly, K3 → K5 / K6, K5 → K6 / host | — | **Do not exist** | | | | | |

## 15.11 Trust-Direction Matrix

| Sender | Receiver | What receiver trusts | What receiver must NOT trust |
|---|---|---|---|
| Browser | K1/K2 | Nothing beyond the platform's authenticated session | All input, including hidden fields and UI state |
| K1 (CyberPanel) → SCC (via K2) | K3/K4 | The platform-asserted identity (who), and platform role facts as *input* to §17 | That identity implies SCC authorization; that the page context is uncompromised; platform-supplied theme data as having any meaning beyond styling (status semantics are core-owned) |
| K2 | K3 | That the request arrived on the platform channel | Assertion validity (K3 doesn't verify it; K4 does); any claim of authorization |
| K3 (Web) | K4 (Core) | That the request came from the Gateway channel; nothing else | User identity (verified independently from the assertion); UI/K3 validation; any client-provided state, confirmations, or risk labels |
| K4 | K5 | That the call came from Core | n/a (K5 has no authority to protect) |
| K5 (Integration) | K4 | The launcher-bound Integration identity of the channel | Every result, interpretation, health verdict, Plan proposal, operation request, declared capability, or scope claim in the message; volume and timing (rate-bound) |
| K4 | K6 (Executor) | That the caller is C; C's authorization decision for in-bounds requests | Vocabulary or scope expressed in the request; parameters beyond schema and bounds; UI validation; Integration declarations not read from K11; that C is uncompromised |
| K6 | K4 | That the result came from the Executor; K8 as the authoritative record of what was executed | Observation *content* (it originates from Security Systems and the host, which may be compromised) |
| SCC → K1 (CyberPanel) | K1 | n/a (the platform follows its own rules) | SCC never relies on the platform to enforce SCC authorization or to execute SCC operations |
| K9 | K4/K6 | OS-root invocation on the host | Recovery gate |
| K10 / K11 | All | Host TCB; install-time declarations and trust anchors | Nothing in K11 may be writable by W, C, or I |

## 15.12 Credential Ownership at the Topology Boundary

The rule is based on impact: **a credential may exist only in the lowest-privilege component that must use it, and never in a component whose compromise would be *less* severe than the credential's.**

| Credential class | May exist in | Must never exist in |
|---|---|---|
| Parent-platform session (e.g., CyberPanel session) | Browser, K1, K2 (read) | K4, K5, K6, K7. K3 may see it in transit on a proxied path but must strip it and never persist, log, or forward it |
| Identity-assertion signing key | K2 only | Everything else. Verification material only in K4 (asymmetric so no verifier can mint) |
| SCC session tokens | Browser, K3 (transient relay), K4 (validation state) | K5, K6 |
| SCC State Store access | K4 | K3, K5; not required by K6 |
| Executor channel authentication | None needed as a secret: OS peer identity (C) | Any transferable form |
| Integration-channel binding | K10/K5 supervisor at launch; K4 | Integration code's own control |
| Security System credentials (API keys, admin tokens, control-socket access) | **K6 only**, referenced by handle in requests | K3, K4 (handles only), K5 (handles only), K7 plaintext (storage design §19) |
| Parent-platform administrative/API credentials (root-equivalent by nature) | **K6 only**, and only where no lower-impact read path exists | All other components |
| Trust anchors (public) | K11 (read by K6/K4) | Writable by any runtime identity |
| Audit/journal integrity material | §18/§19; topology constraint: not in K3 or K5 | K3, K5 |

**Consequence:** no Integration code, no Gateway code, and no Core code ever holds a credential capable of changing a Security System. Such credentials are used only inside K6's bounded operations.

## 15.13 Failure Isolation

| Failure | Observation | Actions | Authorization | Audit | Recovery implication |
|---|---|---|---|---|---|
| **CyberPanel unavailable** | **Continues**: K4 scheduled discovery and health via K5/K6 are unaffected | No new interactive actions (no identity source). Queued Jobs whose authorization needs revalidation of platform identity status are **held, not run** | No new decisions for interactive users; existing decisions not re-validatable if they depend on the platform are treated as uncertain → deny | Continues (K7 and K8) | K9 remains available (authority per recovery gate). No web path exists or is created |
| **SCC Gateway (K3) crash** | Continues | No new interactive actions; in-flight Jobs continue under K4 | Unaffected | Unaffected | Supervisor restart; no state lost (K3 holds none) |
| **SCC Core (K4) crash** | **Stops**: inventory ages and is marked stale on restart, never absent | Stops. K6 completes or aborts only the operation currently executing, records it in K8, and accepts nothing new | Unavailable → deny | SCC audit paused; K8 still records any in-flight effect | On restart K4 must reconcile in-flight Jobs against K8; uncertain outcomes are recorded as unknown |
| **Integration Host (K5) crash** | Generic (product-neutral) discovery continues; product-specific interpretation and health unavailable. Systems remain visible with last-known state marked stale; affected Integrations show error | Actions requiring those Integrations unavailable; in-flight Jobs whose next step needs K5 held | Unaffected | Unaffected | Supervisor restart |
| **One Integration worker crash** | Only that Integration's interpretation lost; Security System remains visible | Only that Integration's capabilities unavailable | Unaffected | Unaffected; crash recorded | Restart that worker only |
| **Privileged Executor (K6) crash** | **Stops for all host facts** (a deliberate consequence of total mediation). Inventory ages → stale, never absent. SCC's own state remains viewable | Stops; in-flight → unknown | Unaffected, but nothing can execute | SCC audit continues; K8 may lack a completion record → outcome unknown | Reconcile against K8 and fresh observation on restart |
| **IPC path unavailable** | As for the unreachable receiver in the rows above | As above | Never "assumed granted" on a broken path | Loss of reply is not success | Retry policy §16; outcome unknown until reconciled |
| **State Store (K7) unavailable** | Observation may run but **cannot be recorded durably**; UI must say so | **All state-changing actions refused.** Authorization metadata unavailable → deny; audit cannot be written | Deny (fail closed) | SCC audit unavailable; K8 continues | Store repair is recovery-gate territory. **No bypass of authorization or audit to "unstick" SCC** |
| **K8 unavailable** | Read-class continues if §16 allows | Write-class refused by K6 | Unaffected | Privileged-effect record unavailable → no privileged effects | Recovery gate |

The "no state-changing actions when audit cannot be durably recorded" rows depend on audit CHANGE-015 (fail-closed audit), which is still pending approval. The topology is built to support fail-closed; the final policy is §18/§19's.

## 15.14 SCC/CyberPanel Lifecycle Independence

**Architectural requirement:** SCC's security-critical components (K3–K8, K11) and all SCC persistent state must be installed, configured, supervised, and stored **outside any path, runtime, service, or data store that the parent platform manages or is expected to overwrite, restart, or replace as part of its normal lifecycle.**

| Event | Required behavior |
|---|---|
| **CyberPanel upgrade** | SCC processes, state, keys, and code are untouched. Only K2 (the Bridge) lives in the platform's domain, so it may be disabled, removed, or made incompatible by the upgrade. That is an *external change*: the platform version change is detected (Platform Services via K6), Bridge/theme compatibility becomes unknown until assessed, and observation continues. Loss of the Bridge causes UI unavailability, never data loss or authorization change. |
| **CyberPanel restart** | Identical to "CyberPanel unavailable" for its duration. |
| **CyberPanel package replacement / reinstall** | Same as upgrade. The Bridge may need re-registration, and its assertion key re-provisioning (a K9 or lifecycle-gate operation). SCC's authorization data doesn't live in the platform, so it survives. |
| **SCC upgrade** | Must not require a CyberPanel upgrade, restart, or core-file modification. May require updating K2 through the platform's supported extension mechanism. K2↔K3 and assertion formats are versioned so compatibility is detectable (§12). |
| **SCC restart** | CyberPanel unaffected. SCC pages show "unavailable" until K3/K4 return. |
| **SCC failure** | CyberPanel unaffected. Security Systems unaffected. Nothing on the host depends on SCC being up to keep running, unless an owned system was explicitly configured that way; that dependency is §22's concern. |

**Specific dependency prohibitions:**
- SCC runtime components must not run under the parent platform's interpreter/runtime environment. CyberPanel ships its own Python environment (verify); SCC must not rely on it.
- SCC must not use the parent platform's database server instance or credentials for K7.
- SCC must not be supervised by the platform's process manager.
- SCC must not store state, keys, or code in the platform's installation tree, except the Bridge artifact placed through the supported extension mechanism.

## 15.15 Host and Root Trust Boundary

**Three isolation levels, stated separately:**

| Level | Against | Provided? |
|---|---|---|
| **Fault isolation** | Buggy Integration, crash, hang, resource exhaustion, malformed output | **Yes**: per-Integration workers, process separation of K3/K4/K5/K6, K4 bounds on K5 output |
| **Compromised-code isolation** | A compromised K3, K5 (Integration), or K4; a compromised Security System feeding hostile data | **Yes, bounded**: K3 → cannot mint identity or reach K6; K5 → cannot touch the host, K6, or credentials; K4 → limited to K11-declared vocabulary and scopes and recorded in K8; Security System output → treated as data everywhere |
| **Malicious administrator / root isolation** | Local root, a root-equivalent parent panel, or host compromise | **No.** Root controls K6, K10, K11, and the kernel. SCC can offer *tamper evidence* (§18/§19) and off-host export, never prevention |

**Inside SCC's security boundary** (SCC must defend against):
- malicious browser input
- a compromised Gateway
- a buggy or compromised built-in Integration
- a compromised Security System's outputs
- a compromised Core, bounded (as stated above)
- replay or duplication on SCC channels
- attempts to widen scope at runtime
- confused-deputy routing through the UI

**Outside SCC's security boundary** (stated as assumptions):
- local root
- the kernel
- K10 (the host service manager)
- the integrity of K11 after root-level tampering
- a root-equivalent compromised parent panel (for identity and for everything on the host)
- physical access
- malicious non-built-in Integrations, which v1 excludes entirely

## 15.16 Authoritative Architecture Diagram

```
 LEGEND   ═══ trust boundary      ─── process boundary      ──▶ request (trust flows opposite: receiver does NOT trust sender beyond §15.11)
          [W] [C] [I] [root]  = distinct OS identities       ✗ = path that must not exist

 ╔═══════════════════════════ UNTRUSTED ════════════════════════════╗
 ║  K0 Browser                                                     ║
 ╚══════════════╤═══════════════════════════════════════════════════╝
                │ P1 (platform TLS/session)
 ╔══════════════▼════════ PARENT PLATFORM TRUST DOMAIN (root-equiv., host TCB) ═════╗
 ║  K1 CyberPanel ─── identity provider · presentation host                          ║
 ║   └─ K2 Platform Bridge (SCC code in platform process)                            ║
 ║        holds: assertion SIGNING key only · no SCC logic · no host ops for SCC    ║
 ╚══════════════╤════════════════════════════════════════════════════════════════════╝
                │ P2  request + signed identity assertion (relayed, not minted, below)
 ╔══════════════▼═════════════════ SCC UNPRIVILEGED DOMAIN ══════════════════════════╗
 ║ ┌──────────────────────────────┐                                                   ║
 ║ │ K3 SCC Gateway [W]           │  untrusted for identity/authz/state              ║
 ║ │  Presentation Adapter        │  no store · no K5 · no K6                   ✗──▶ K6
 ║ └──────────────┬───────────────┘                                                   ║
 ║                │ P3  (assertion verified END-TO-END by K4)                         ║
 ║ ┌──────────────▼───────────────────────────────────────┐    P10   ┌─────────────┐ ║
 ║ │ K4 SCC Core [C]   — DECIDES, never DOES               │◀────────▶│ K7 State    │ ║
 ║ │  Registry · Inventory · generic discovery logic      │  C only  │ Store (SCC- │ ║
 ║ │  Compatibility · Capability registration (narrow-only)│          │ owned only) │ ║
 ║ │  Authorization · Plans · Jobs/locks · Scheduler       │          └─────────────┘ ║
 ║ │  Audit coordination · assertion VERIFY key            │                          ║
 ║ └───────▲──────────┬───────────────────────────┬────────┘                          ║
 ║   P5    │          │ P4                        │                                   ║
 ║ results │          ▼ invoke                    │                                   ║
 ║ ┌───────┴───────────────────────────────┐      │                                   ║
 ║ │ K5 Integration Host [I]               │      │                                   ║
 ║ │  ┌──────────┐┌──────────┐┌──────────┐ │      │                                   ║
 ║ │  │Integr. A ││Integr. B ││ Platform │ │  no host · no network · no creds          ║
 ║ │  │ worker   ││ worker   ││ Services │ │  launcher-bound identity per worker  ✗──▶ K6
 ║ │  └──────────┘└──────────┘└──────────┘ │                                    ✗──▶ host
 ║ └───────────────────────────────────────┘      │                                   ║
 ╚════════════════════════════════════════════════╪═══════════════════════════════════╝
                                                  │ P6 structured read/write requests
                                                  │    caller authenticated as [C] ONLY
 ╔════════════════════════════════════════════════▼════ PRIVILEGED DOMAIN ═══════════╗
 ║ ┌────────────────────────────────────────────────────────┐  P9   ┌──────────────┐ ║
 ║ │ K6 Privileged Executor [root] — DOES, never DECIDES     │──────▶│ K8 Executor  │ ║
 ║ │  enforces closed vocabulary + per-Integration scope     │append │ Journal      │ ║
 ║ │  read FROM K11 (never from request) · holds SS creds    │ only  │ (C: read)    │ ║
 ║ └───────────────────────────┬────────────────────────────┘       └──────────────┘ ║
 ║   K11 Install Tree (root-owned; code, declarations, trust anchors; not writable    ║
 ║       by W, C, I) ─── read by K6, K4, K5 loader                                    ║
 ╚═════════════════════════════╪══════════════════════════════════════════════════════╝
                               │ P8
 ╔═════════════════════════════▼═══════ HOST TCB (outside SCC boundary) ═════════════╗
 ║  Host OS · kernel · K10 Service Manager (starts K3–K6 under W/C/I/root)            ║
 ║  Security Systems (their OUTPUT is untrusted data to SCC)                          ║
 ║  K9 Local Administrative Interface (root, host-local; authority = recovery gate)   ║
 ╚════════════════════════════════════════════════════════════════════════════════════╝

 Only path from intent to host effect:  K0 → K1/K2 → K3 → K4 → K6 → Host
 K4 → K1 direct: none.  Platform reads/writes go K5(Platform Services) → K4 → K6.
```

## 15.17 Normative Invariants

The audit prompt suggested several example invariants. Each was validated against the rest of the architecture before being included here: two are adopted as written, and the rest are adopted in refined or split form (see the "Validation of suggested examples" table after the list).

**Process and privilege**
- **T-01** SCC runtime components K3, K4, K5, and K6 MUST each run under a distinct OS identity. No two may share one.
- **T-02** K6 MUST be the only SCC runtime component that performs privileged host operations.
- **T-03** K3 (Gateway/UI) MUST NOT perform, request directly, or have any channel to privileged host operations.
- **T-04** K4 (Core) MUST NOT run with root or equivalent privilege, and MUST NOT perform host operations directly.
- **T-05** Integration code MUST execute only in K5 and MUST NOT execute in K3, K4, K6, or the parent platform.
- **T-06** K5 MUST NOT have direct host access (filesystem beyond its runtime, process spawning of host tools, Security System sockets or APIs) and MUST NOT have network access.
- **T-07** All host observation and all host mutation by SCC MUST pass through K6, classified as read or write.

**Executor**
- **T-08** K6 MUST accept runtime requests only from identity C, authenticated by OS-enforced peer identity.
- **T-09** K6 MUST derive its operation vocabulary and every per-Integration scope from K11. It MUST NOT accept vocabulary, scope, or permission assertions contained in a request.
- **T-10** K6 MUST NOT trust UI, K3, K5, or K4 *validation* as a substitute for its own schema and bounds enforcement.
- **T-11** K6 MUST NOT load Integration or platform code, MUST NOT initiate operations, and MUST NOT accept free-form command strings.
- **T-12** K6 MUST record every received request and every attempted effect in K8 before reporting a result. If it can't write K8, it MUST refuse write-class operations.

**Identity and authorization**
- **T-13** Platform session identity MUST NOT by itself constitute authorization for any SCC action. It establishes *who*, never *may*.
- **T-14** User identity MUST be verified by K4 from an assertion that K3 cannot mint or alter. K4 MUST NOT accept K3's statement of identity.
- **T-15** Authorization decisions MUST be made only in K4. Uncertain or unavailable authorization MUST result in denial of state-changing operations.
- **T-16** Each K5 worker's Integration identity MUST be bound by its launcher, not self-declared. K4 MUST apply only that Integration's K11-declared scope.
- **T-17** K4 MAY narrow capabilities declared in K11 and MUST NOT widen them.

**Credentials**
- **T-18** Credentials capable of changing a Security System or the parent platform MUST exist only within K6.
- **T-19** K3 and K5 MUST NOT persist or log any credential. K5 MUST NOT hold any credential in usable form.
- **T-20** The identity-assertion signing key MUST exist only in K2. Only verification material may exist elsewhere.

**Code and state provenance**
- **T-21** K4, K5, and K6 MUST load code only from K11, and K11 MUST NOT be writable by W, C, or I.
- **T-22** v1 MUST NOT provide any load path for non-built-in Integration code.
- **T-23** K7 MUST be accessible only to identity C and MUST NOT be hosted in, or depend on credentials of, the parent platform's data store.

**Platform independence**
- **T-24** SCC's installation and normal operation MUST NOT require modification of parent-platform core files. Platform integration MUST use only supported extension mechanisms. This does not remove §11's exceptional, guarded, authorized, audited core-configuration *Actions*, which execute via K6 like any other write.
- **T-25** SCC security-critical components and persistent state MUST NOT reside in, run under, or be supervised by anything the parent platform's update lifecycle manages or overwrites. K2 is the sole permitted artifact in the platform's domain.
- **T-26** An SCC upgrade MUST NOT require a parent-platform upgrade, and a parent-platform upgrade MUST NOT require SCC reinstallation. It MAY require K2 re-registration.
- **T-27** SCC Core MUST remain platform-neutral. Platform-specific code MUST reside only in K2, K3's Presentation Adapter, or K5's Platform Services worker.

**Failure and recovery**
- **T-28** Loss of any component MUST NOT cause a Security System to be represented as absent. It may only cause state to become stale or unknown.
- **T-29** No failure condition MAY enable a web-reachable path that bypasses authorization or audit. Recovery authority MUST be host-local (K9), with its scope defined at the recovery gate.
- **T-30** K3 MUST NOT present cached state as current when K4 is unavailable.
- **T-31** No SCC process MAY expose a network listener reachable from outside the host.

**Validation of suggested examples:**

| Suggested example | Disposition |
|---|---|
| SCC Web must not perform privileged operations | Adopted as T-03 |
| Integration code must not possess unrestricted privilege | **Strengthened** to T-05/T-06: Integrations get *no* host access at all |
| Privileged execution behind a dedicated enforcement boundary | Adopted as T-02/T-07 |
| Executor must not trust UI validation | Adopted as T-10 |
| Executor must not trust Integration declarations alone | **Refined** to T-09: it trusts K11 declarations and nothing in a request |
| CyberPanel session must not constitute authorization | Adopted as T-13 |
| SCC must remain independently upgradeable | **Refined** to T-26, which permits K2 re-registration |
| SCC must not require CyberPanel core modification | **Refined** to T-24, which keeps §11's exceptional-edit Actions |

## 15.18 Open Questions / Deferred Decisions

Only items that genuinely can't be settled here:

- **OQ-1 (adapter verification, not blocking §16):** Can CyberPanel's supported extension mechanism route browser requests to an independent K3 process without core-file modification (relay through K2, or a supported proxy route)? Both satisfy §15. This must be verified against current CyberPanel before adapter implementation. If *neither* is possible without core edits, §11/T-24 would need an owner decision.
- **OQ-2 → §16:** Whether K6 is physically split into read-class and write-class processes; its reduced-privilege options; request schema, idempotency, and duplicate handling; K8 content.
- **OQ-3 → §17:** Principal model; how platform role facts feed SCC authorization; revalidation when the identity provider is unavailable; assertion format and lifetime.
- **OQ-4 → §17/§16:** Whether high-risk approvals must carry evidence that K6 can verify *without trusting K4*, e.g., an approval factor that doesn't transit K1/K2/K4. This is the only way to shrink the accepted "compromised Core = bounded misuse" risk (§15.7).
- **OQ-5 → §18/§19:** Tamper-evidence mechanism for K7 audit and K8; off-host export; audit fail-closed policy (depends on CHANGE-015).
- **OQ-6 → Recovery gate / §22:** K9's authority and whether it may reach K6 directly; key (re)provisioning for K2; installer placement of K11.
- **OQ-7 → §18:** Distinct OS identity per Integration. Deferred until any non-built-in Integration is proposed (excluded from v1).
- **OQ-8 → §12 Host Environment:** Hosts without a service manager able to assign per-service identities, or container/VPS environments that constrain this, must be classified as unsupported or partially supported. The topology does not relax T-01 for them.

## Gate Assessment

**PASS: ready to proceed to §16**, subject to explicit architecture-owner approval of this section.

The topology is fully decidable at this gate. No open question changes the process, identity, trust-direction, or credential-placement decisions. OQ-1 is an adapter verification with two conforming options, and all others are downstream detail.

**§16 (Privileged Execution Contract) is now permitted to define:**
1. The closed operation vocabulary K6 enforces, and the read/write (and any finer) operation classes.
2. The format and location semantics of the per-Integration scope declarations K6 reads from K11, and how K4 narrows them.
3. The P6/P7 request and response contract: schema, parameter typing and validation, correlation fields, idempotency, and duplicate/replay rejection.
4. K6's refusal semantics and the structure and write-before-reply rule for K8 records.
5. How Security System and platform credentials are referenced by handle and used inside K6.
6. Whether K6 is split into read-class and write-class processes, and any privilege reduction below full root.
7. How K6 handles interruption, partial effects, and "outcome unknown" at the operation level.
8. Whether and how approval evidence verifiable by K6 without trusting K4 fits the request contract. This is **interface only**; the approval model itself stays in §17.

**§16 is not permitted to:** alter any §15 invariant, grant K3 or K5 any path to K6, introduce free-form command operations, or define the authorization model.
