> **Document status:** LOCKED
> **Authority category:** 1 — Locked architecture (see [Authority Hierarchy](../README.md#authority-hierarchy))
> **Source:** §16 revised text containing Decisions A, B and C and X-01…X-39 — DEC-002, DEC-003, DEC-004, DEC-005, DEC-006, DEC-007, DEC-022 (D-10)
> **Normative:** Yes
> **Findings against this text:** none recorded inline (DEC-030, Q2). See [Known Findings Against Locked Text](../README.md#known-findings-against-locked-text): KF-04 to KF-09.
> **Transcription notes:** Normative text reproduced verbatim, including the revision summary. Removed process-wrapper
> text only: the opening italic line ("This is candidate architecture text for architecture-owner approval. … I have
> not modified or created any files.") and the closing line ("Stopping here. I won't start §17 until you give
> explicit approval."). The consistency findings CF-3 and CF-5 in §16.16 were subsequently approved by the owner
> (DEC-005, DEC-006). The Gate Assessment is retained as part of the approved text; its permissions for §17 are
> historical (§17 is complete and locked).

# SCC §16 — Privileged Execution Contract (Revision for Lock)

**What changed in this revision**
- **Decision A (Core Discovery Declaration):** §16.2, §16.3, §16.4, §16.7, and invariants X-36, X-37 and X-39.
- **Decision B (one request, one declared Operation):** §16.1.2, §16.6.1, §16.8, §16.10, invariant X-05 (replaced) and X-38.
- **Decision C (profile executable identity):** §16.1.1, §16.2, §16.4, and invariants X-03 (amended) and X-34.
- **Consistency fixes:** §16.16 lists five findings (CF-1 to CF-5). Each is resolved inside §16, and none changes §15 or an owner decision. Two of them (CF-3 and CF-5) need you to look at them explicitly.

---

## Terms

- **Operation:** a named, versioned primitive implemented in K6 and defined in the K11 Operation Catalogue.
- **Internal step:** a mechanical step of an Operation, fixed by that Operation's catalogue definition (e.g., stage, validate, commit, postcondition). An internal step is **not** an Operation and can never be requested on its own.
- **Profile:** a K11-declared instance of a Tier-2 primitive (`tool.invoke` or `endpoint.call`), or a validator used as an internal step of `file.replace`.
- **Approved Executable Identity:** the K11-declared binding between a profile and the specific executable it may run. It does not refer to the path alone (§16.2.3).
- **Execution Declaration:** a signed K11 unit that grants scope to one requester identity. It comes in three kinds:
  - **Integration Declaration**
  - **Platform Services Declaration**
  - **Core Discovery Declaration**
- **Core Discovery Declaration:** the READ-only Execution Declaration used by K4's own generic, product-neutral discovery logic. **It is not an Integration** in the SCC domain model.
- **Scope entry:** a grant inside an Execution Declaration. It binds a capability (or, for Core Discovery, a discovery function) to specific Operations, resources, parameter bounds and credential handles.
- **Resource:** a K11-declared, named host object. Requests refer to it by ID and never by raw host path or name.
- **Internal binding:** a value K6 supplies to an internal step, for example the location of staged content. It is never supplied by the request.

---

## 16.1 Closed Operation Vocabulary

### 16.1.1 What replaces "run a command"

K6 accepts only **Operations**. The vocabulary has two tiers, and **both are closed at K11 load time**.

- **Tier 1: built-in primitives.** Fixed code in K6 with fixed semantics, as listed in §16.1.3.
- **Tier 2: declared profiles.** These are instances of exactly two Tier-1 primitives, `tool.invoke` and `endpoint.call`. Each profile is data in a signed K11 Execution Declaration.

**A tool profile's declared execution boundary is the full set of the following items. All of them are fixed by K11, and none can be changed by a request:**

| Element | Rule |
|---|---|
| **Path** | Absolute. The executable and every path component are root-owned and not group- or world-writable. |
| **Approved Executable Identity** | The executable found at the path must match the declared identity (§16.2.3). K6 must execute the same object it verified. |
| **Interpreter identity** (only if the executable is an interpreted program) | Declared and verified in the same way (see CF-3). |
| **Argument template** | Fixed. Every variable slot is typed (§16.1.5). |
| **Environment** | Fixed and minimal. Nothing is inherited. |
| **Working directory** | Fixed. |
| **Stdin policy** | None, or one bounded `blob` slot. |
| **run_as** | Fixed identity (§16.13). |
| **Output bound and timeout** | Fixed maxima. |
| **Class** | READ or WRITE. |

An **endpoint profile** has the equivalent boundary:
- the endpoint address (a unix socket path, a loopback address, or a D-Bus destination/interface/method);
- the **expected endpoint owner identity** (CF-4);
- a fixed request template with typed slots;
- output bound, timeout and class.

**Why a profile does not amount to arbitrary execution:**
- the executable is bound by identity, not just by path;
- no slot accepts free text, a script, a module name, interpreter options, or anything that reaches a shell;
- general-purpose executors are refused at load time (§16.2.2);
- no profile can be added at runtime.

### 16.1.2 Operation definition model (in K11)

| Attribute | Meaning |
|---|---|
| `op_id` | Stable name, `<family>.<verb>`. |
| `op_version` | `major.minor`. A major change means a semantic change. Requests name an exact major version. |
| `class` | `READ` or `WRITE`. |
| `family` | See §16.1.3. |
| `param_schema` | Typed request parameters only (§16.1.5). |
| `param_bounds` | Global maxima. Scope entries may narrow them, never widen them. |
| `internal_steps` | **The fixed, ordered list of mechanical steps that implement the Operation.** The only control flow allowed is abort-on-failure. For each step it records: the step name, whether the step may cause a host effect, the declared profile role it uses (if any), the internal bindings it receives, and how failure at that step maps to an outcome (§16.6.2). |
| `result_schema` | Structured result, output framing and truncation flag. |
| `refusal_codes` | The subset of §16.4.2 this Operation can produce. |
| `max_duration` | Hard ceiling for the whole Operation, all internal steps included. |
| `output_limit` | Maximum bytes returned. Truncation is always flagged. |
| `effect_model` | `NONE` (reads), `ATOMIC`, `NON_ATOMIC` or `IRREVERSIBLE`. |
| `preconditions` | Checks K6 can perform itself (e.g., expected prior digest). |
| `postcondition` | Optional. If present, it is an internal step. |
| `cancellation` | `BEFORE_INVOKE_ONLY` or `SAFE_ABORT` (with the step boundaries at which abort is safe). |
| `idempotency_class` | `NATURAL`, `CONDITIONAL` (via precondition digest) or `NONE`. |
| `retry_class` | `SAFE`, `AFTER_RECONCILE` or `NEVER_AUTOMATIC`. |
| `grant_mode` | `SCOPED` (needs a scope entry), or `CALLER` (executor family only; see CF-1). |

### 16.1.3 Families (the Tier-1 set)

| Family | Operations | Class |
|---|---|---|
| `host` | `host.facts`, `host.package_inventory`, `host.service_inventory`, `host.process_inventory` (bounded fields), `host.socket_inventory` | READ |
| `file` | `file.stat`, `file.read`, `file.list` (declared directories only), `file.digest` | READ |
| `file` | `file.replace` (internal steps: stage → declared validator → atomic commit where supported → postcondition; the pre-image is retained where declared), `file.restore_preimage` | WRITE |
| `log` | `log.read_range` | READ |
| `service` | `service.query` | READ |
| `service` | `service.control` (enum: start, stop, restart, reload, enable, disable; the scope entry lists which values are allowed) | WRITE |
| `package` | `package.query` | READ |
| `package` | `package.install`, `package.remove`, `package.upgrade` (only from allowlisted sources, only packages named in scope, exact version/artifact identity) | WRITE |
| `tool` | `tool.invoke` (class taken from the profile) | READ or WRITE |
| `endpoint` | `endpoint.call` (class taken from the profile) | READ or WRITE |
| `executor` | `executor.status`, `executor.request_status`, `executor.declarations`. These touch no host state. `grant_mode = CALLER`. | READ |

There is no operation for deleting files, changing permissions, appending or patching files, creating directories, running database queries, making general HTTP requests, network access outside allowlisted package sources and declared loopback/unix/D-Bus endpoints, or signalling processes other than through `service.control`. Any new primitive requires a new SCC release.

**Validators are not Operations.** A validator profile is used only as a declared internal step of `file.replace`.

### 16.1.4 Classes

- **READ:** no intended host effect. It may still be sensitive (§16.7).
- **WRITE:** has an intended host effect. It requires the authorization interface fields (§16.5) and a write-ahead intent record (§16.8).
- The class is fixed by K11, on the Operation or on the profile. A class stated in a request is compared against K11 and never trusted.

### 16.1.5 Parameter and slot types

**Request parameter types (the complete set):** `enum`, `int` (bounded), `string` (bounded, anchored declared pattern), `duration`, `ip`/`cidr` (declared restrictions), `resource_ref`, `selector` (a name matching a declared pattern inside a declared resource), `blob` (bounded), `handle_ref`, `digest`.

**Profile slot types:** any of the request types above, plus **internal binding types**. An internal binding (e.g., `staged_object`) is filled only by K6 during an internal step. It is never accepted from a request (CF-2).

**There is no `path`, `command`, `url`, `script`, `module` or `query` type.**

---

## 16.2 K11 Operation Declarations

### 16.2.1 Loading

K6 loads K11 at start, and again on an explicit root-initiated reload through K10. Each Execution Declaration is signature-checked against the K11 trust anchors and checked against the Global Execution Policy. **A declaration that fails is excluded on its own; the others still load** (§14).

### 16.2.2 Structure

| K11 part | Contents | Scope | Mutable at runtime? | Narrowable by K4? |
|---|---|---|---|---|
| **Operation Catalogue** | All Tier-1 definitions (§16.1.2), including `internal_steps` | Global | No | K4 may choose not to use an Operation. K6 still enforces the catalogue. |
| **Global Execution Policy** | See the list below this table. | Global | No | No |
| **Trust Anchors** | SCC release signing keys. **Approver anchor set:** reserved and empty until §17 populates it through lifecycle. | Global | No | No |
| **Integration Declarations** | `declaration_id` (which is the `integration_id`), version, digest, signature; capabilities; resources; profiles (with executable identities); handles; scope entries | Per Integration | No | By non-use only |
| **Platform Services Declaration(s)** | Same structure. Represents the Platform Adapter's Platform Services worker (K5). **Not an Integration** (CF-5). | Per Platform Adapter | No | By non-use only |
| **Core Discovery Declaration** | Reserved `declaration_id`; READ-only scope entries for K4's generic discovery (§16.2.4) | Core | No | By non-use only |
| **Scope entries** (in any Execution Declaration) | Capability or discovery function → Operation and major version → resources → narrowed bounds → allowed enum values → handles → exposure mode (reads) → `executable_semantics` flag (writes) → declared validator profile (required when `executable_semantics` is set) → `approval_required` flag (reserved for §17) | Per declaration | No | By non-use only |
| **Host Restriction Overlay** | Root-authored, **narrowing-only** restrictions for this host. It can exclude families, declarations, scope entries or classes, but cannot add anything. It is not an authorization engine: it holds no principals, roles or per-user rules. | Host-local | Only by root through K9/lifecycle | It is itself a narrowing that K6 enforces |

The **Global Execution Policy** contains:
- the deny rule for profile executables (see below);
- the rule that every profile slot is typed;
- path rules;
- the rule that **every tool profile must declare an Approved Executable Identity**;
- the rule that **every endpoint profile must declare its expected owner identity**;
- the reserved-namespace rule (§16.2.4);
- the allowlist of package sources;
- K6 concurrency ceilings.

The **deny rule** refuses any profile executable that:
- is a general-purpose shell, an interpreter invoked directly, or an exec-wrapper; or
- has any slot able to supply code, a script path, a module name, or interpreter options.

**General rules**
- K4 **may narrow** by not sending requests. It **must not widen**. K6 never accepts scope, capability, class, identity or step selection from a request, and never reads any of these from K4.
- Narrowing that must survive a compromised K4 belongs in the Host Restriction Overlay.
- **Configuration-as-code rule:** a WRITE scope entry targeting content whose format can cause the Security System to execute commands must be flagged `executable_semantics`, and must declare a validator profile. Scope should be designed to avoid such content where possible.

### 16.2.3 Approved Executable Identity (Decision C)

A tool profile, including a validator profile, **must** declare the identity of the approved executable. K6 **must not** execute whatever happens to exist at the declared path. The profile declares one of these identity modes:

| Mode | Binding | Availability |
|---|---|---|
| **`DIGEST_PINNED`** | A signed set of one or more approved content digests for the executable (and for the interpreter, if one applies) | Always available |
| **`PACKAGE_ATTESTED`** | The executable must belong to a declared package, installed from an allowlisted source. The package must be within a declared version range. The file on disk must match the digest recorded by the host package system, and the package system must itself provide verifiable provenance for that record. | Only on Host Environments whose package system provides verifiable provenance (a Host Environment compatibility fact, §12). Otherwise `DIGEST_PINNED` is required. |

**Identity rules**
- K6 verifies identity at invocation time and **must execute the same object it verified**, so an attacker cannot swap the file between the check and the execution. The mechanism is an implementation detail; the rule is architectural.
- A mismatch refuses the request with `EXECUTABLE_IDENTITY_MISMATCH`. The journal marks the event as integrity-relevant.
- **Consequence to accept explicitly:** an external upgrade of a Security System can change a `DIGEST_PINNED` executable. The affected profiles then refuse until the declarations are updated. The capability becomes *unavailable*, never absent (T-28), and compatibility becomes unknown (§12). How declarations are refreshed is Q-7.
- **Limit:** identity binding defends against substitution by non-root actors and against accidental drift. It cannot defend against local root, which is outside SCC's boundary (§15.15).
- The digest algorithm and encoding are implementation details.

### 16.2.4 Core Discovery Declaration (Decision A)

**Purpose.** K4 owns generic, product-neutral discovery logic (§15.7). T-07 routes every host observation through K6, and K6 grants only through K11 Execution Declarations. The Core Discovery Declaration is therefore the K11 identity under which K4's own discovery reads are scoped.

**Terminology.** Core Discovery is **not** an Integration. It has no Integration Registry entry, no capabilities in the §2/§14 sense, no health, and no management or ownership semantics. Its reserved identifier appears in the request field `integration_id` only because that field identifies an **Execution Declaration** (§16.3).

**Constraints.** The Core Discovery Declaration:
- is signed and validated like every other Execution Declaration;
- uses an identifier in the **reserved SCC namespace**, which no Integration or Platform Services declaration may use (K6 refuses to load a declaration that claims it);
- contains **READ entries only**;
- includes only the product-neutral `host` family: `host.facts`, `host.package_inventory`, `host.service_inventory`, `host.process_inventory`, `host.socket_inventory`;
- contains **no** `file`, `log`, `service`, `package`, `tool` or `endpoint` entries, **no** product- or platform-specific resources, and **no** credential handles. Product-specific detection is Integration detection (§14);
- sets `host.process_inventory` exposure to `METADATA_ONLY` (executable identity, name, owner; no argument vectors, no environment) because argument vectors can carry secrets;
- is subject to all K6 validation and to the Host Restriction Overlay. If the overlay narrows it, generic observation shrinks, and affected state goes stale rather than absent.

K6 **must refuse to load** a Core Discovery Declaration that violates any of these constraints. K6 does not repair it or partially load it.

---

## 16.3 Request Contract (P6: K4 → K6)

| Field | Created by | May modify | Verified by K6 how | Security-relevant | Trusted by K6? |
|---|---|---|---|---|---|
| `request_id` | K4 | Nobody | Uniqueness against K8 (§16.11) | Yes (replay) | Identifier only |
| `idempotency_key` | K4 | No | Against K8 history | Yes | Identifier only |
| `reconciled_after` | K4 | No | Must reference an existing terminal journal record for the same key | Yes | Recorded; K6 cannot verify that K4 actually reconciled |
| `job_id` | K4 | No | Present for WRITE | Correlation | **No**; recorded as claimed |
| `correlation_id`, `plan_ref`, `plan_digest` | K4 | No | Well-formed | Correlation (the plan digest is bound into approval evidence if present) | **No**; recorded |
| `integration_id` — **the Execution Declaration identifier**: an Integration ID, a Platform Services declaration ID, or the reserved Core Discovery ID | K4 (from the K5 launcher binding, or its own identity for Core Discovery) | No | Must be a loaded, valid declaration | Yes | **Partially.** K6 cannot verify which requester originated the request. It enforces only that declaration's scope. |
| `capability_id` (for Core Discovery: the discovery function ID declared in its scope entry) | K4 | No | Must exist in that declaration | Yes | No, checked |
| `op_id`, `op_version` | K4 | No | In the catalogue; version supported | Yes | No, checked |
| `op_class` | K4 | No | Must equal the K11 class | Yes | **No**; mismatch refused |
| `declaration_digest` | K4 | No | Must equal the loaded digest | Yes | No, checked |
| `resource_refs`, `selectors` | Proposed by K5 (or by K4 for discovery), validated by K4 | No | Resolved only through K11 | Yes | **No** |
| `params` | Same as above | No | Full schema and bounds check | Yes | **No** |
| `expected_state` | K4, from the Plan | No | Compared with the host just before the effect-bearing step | Yes (TOCTOU) | Used as the expectation only |
| `handle_refs` | K4 | No | Declared in the scope entry used | Yes | No, checked |
| `authorization_ref` | K4 | No | Present and well-formed for WRITE | Yes | **No**; recorded |
| `principal_claim` | K4 | No | Well-formed | Accountability | **No**; never used in a K6 decision |
| `approval_evidence` | Approver (§17), carried by K4 | Nobody (signed) | Cryptographic verification (§16.5) | Yes | Verified, not trusted |
| `issued_at` | K4 | No | Within the acceptance window by K6's clock | Yes | Bounded |
| `deadline` | K4 | No | Not passed; K6 uses the earlier of this and `max_duration` | Yes | Bounded |
| `output_limit` | K4 | No | Not above the catalogue or scope bound | Resource | Bounded |

**There is no request field for choosing a validator, an internal step, an executable, an identity mode, a staging location or an interpreter.** Any such field in a request is malformed.

**K6 must not trust merely because K4 supplied:** anything except that the channel peer is C. This specifically includes:
- `integration_id` as proof of origin, including use of the reserved Core Discovery ID;
- `job_id`, `authorization_ref`, `principal_claim`;
- `plan_ref`/`plan_digest`, unless covered by verified evidence;
- `op_class`, `reconciled_after`;
- every parameter, resource reference and expected-state value.

---

## 16.4 Request Validation

### 16.4.1 Validation layers (in order; the first failure refuses)

| # | Layer | Check | Refusal code |
|---|---|---|---|
| 0 | Journal availability | K8 is writable | `UNAVAILABLE_JOURNAL` |
| 1 | Transport peer | OS-enforced peer identity is C | Connection rejected (`CONNECTION_REJECTED`, journaled with rate limiting) |
| 2 | Message schema | Envelope well-formed; size within bound; no forbidden fields (§16.3) | `MALFORMED` |
| — | *The request is journaled as RECEIVED (content digest) at this point* | | |
| 3 | Replay / duplicate | Unseen `request_id`, or an identical duplicate; `issued_at` within the window | `REPLAY` / duplicate path (§16.11) |
| 4 | Deadline | Not passed | `STALE_DEADLINE` |
| 5 | Declaration currency | Digest equals the loaded declaration | `STALE_DECLARATION` |
| 6 | Operation existence | In the catalogue | `UNSUPPORTED_OPERATION` |
| 7 | Operation version | Major version supported | `UNSUPPORTED_VERSION` |
| 8 | Operation class | Request class equals the K11 class | `CLASS_MISMATCH` |
| 9 | Declaration identity | Loaded and valid | `UNKNOWN_INTEGRATION` (applies to every declaration kind) |
| 10 | K11 scope | For `SCOPED` operations, a scope entry exists for (declaration, capability or function, operation, resources); for `CALLER` operations, the caller is C (CF-1); the Host Restriction Overlay does not exclude it | `OUT_OF_SCOPE` / `RESTRICTED_BY_HOST_POLICY` |
| 11 | Parameter schema | Types match | `INVALID_PARAMETER` |
| 12 | Parameter bounds | Narrowest of catalogue, scope and overlay; enum value allowed | `PARAMETER_OUT_OF_BOUNDS` |
| 13 | Resource limits | Output and blob sizes; concurrency ceiling; no other WRITE in flight on the same resolved resource | `RESOURCE_LIMIT` / `RESOURCE_BUSY` |
| 14 | Authorization interface | WRITE has `authorization_ref` and `job_id` | `AUTHORIZATION_REFERENCE_MISSING` |
| 15 | Approval evidence | Where required: verified (§16.5) | `APPROVAL_EVIDENCE_MISSING` / `APPROVAL_EVIDENCE_INVALID` |
| 16 | Idempotency | §16.11 | `IDEMPOTENCY_CONFLICT` / `ALREADY_COMPLETED` |
| 17 | Credential handles | Declared in the entry, provisioned, resolvable | `CREDENTIAL_UNAVAILABLE` |
| 18 | Resource resolution | Inside the declared root; no escape through symlinks or special files | `RESOURCE_RESOLUTION_FAILED` |
| 18a | **Executable / endpoint identity** | Every profile the Operation will use, including a `file.replace` validator, passes path rules and its Approved Executable Identity (or, for endpoints, the expected owner identity). Re-verified and bound at the internal step that uses it. | `EXECUTABLE_IDENTITY_MISMATCH` / `ENDPOINT_IDENTITY_MISMATCH` |
| 19 | Execution preconditions | Operation preconditions and `expected_state` hold, checked as close to the effect-bearing step as the mechanism allows | `PRECONDITION_FAILED` |
| — | *The request is journaled as ACCEPTED at this point* | | |

### 16.4.2 Canonical distinctions

| Category | Meaning | Refusal codes / outcome | Effect certainty |
|---|---|---|---|
| **Malformed** | Could not be parsed, or carries forbidden fields | `MALFORMED` | None |
| **Unauthorized** (in the K6 interface sense; *not* a K6 authorization decision) | Missing authorization-interface field, or missing/invalid approval evidence | `AUTHORIZATION_REFERENCE_MISSING`, `APPROVAL_EVIDENCE_*` | None |
| **Unsupported** | Operation or version unknown | `UNSUPPORTED_*` | None |
| **Out-of-scope** | No K11 grant; restricted by the overlay; or the host object is not the one K11 approved | `OUT_OF_SCOPE`, `RESTRICTED_BY_HOST_POLICY`, `EXECUTABLE_IDENTITY_MISMATCH`, `ENDPOINT_IDENTITY_MISMATCH` | None |
| **Invalid parameter** | Schema or bounds violation | `INVALID_PARAMETER`, `PARAMETER_OUT_OF_BOUNDS` | None |
| **Stale** | Deadline passed, or declaration mismatch | `STALE_*` | None |
| **Duplicate** | Same `request_id`, identical content | Prior record returned | n/a |
| **Replay** | Same `request_id` with different content, outside the window, or a reused nonce | `REPLAY` | None |
| **Unavailable** | Journal, resource busy, credential, resolution, or executor degraded | `UNAVAILABLE_*`, `RESOURCE_*`, `CREDENTIAL_UNAVAILABLE`, `RESOURCE_RESOLUTION_FAILED` | None |
| **Execution failure** | Executed, with positive evidence of no effect | FAILED | None evidenced |
| **Verification failure** | Executed, but the postcondition did not hold | UNKNOWN (with `verification = FAILED`) | Unknown |
| **Outcome unknown** | Effect cannot be established | UNKNOWN | Unknown |

All pre-acceptance categories produce **REFUSED**, which guarantees no host effect.

---

## 16.5 Authorization vs Execution

K6 receives three things from K4's decision: `authorization_ref`, `job_id` and `principal_claim`. All three are opaque, asserted by K4, and recorded. Where K11 requires it, K6 also receives `approval_evidence`.

| Responsibility | Owner |
|---|---|
| Whether the principal may act; risk; confirmation; Plan validity; locks across Security Systems; sequencing; revalidation; cancellation policy | **K4 only** |
| Presence of the authorization reference (WRITE); recording claimed values | K6 records |
| Catalogue, class, internal steps, declaration and scope, overlay, parameters, bounds, resolution, executable and endpoint identity, preconditions, deadline, replay, idempotency, credential binding, per-resource write exclusion, journal-before-report | **K6 enforces independently** |
| Approval evidence where K11 requires it | **K6 verifies cryptographically** |

**Residual risk (stated, not eliminated).** Where no approval evidence is required, a compromised K4 can execute **any Operation granted by any loaded Execution Declaration**, under any claimed Job or principal. K8 records all of it. This includes `executable_semantics` writes that pass their validator.

The Core Discovery Declaration adds **no** WRITE exposure. Misuse of it by K4 is limited to product-neutral inventory reads, with process arguments and environment withheld.

**Approval evidence interface** (unchanged; activation belongs to §17):
- **Form:** a signature by a key anchored in the K11 Approver anchor set.
- **What it signs:** a canonical digest of `integration_id`, `capability_id`, `op_id@major`, canonical parameters, resource references and selectors, `expected_state`, `plan_digest`, `deadline` and a single-use nonce.
- **K6 verifies:** that the anchor is present and not revoked, that the signature is valid, that the digest matches the request exactly, that the evidence has not expired, and that the nonce has not been used before (checked against K8).
- **K6 does not interpret** who the approver is or what policy applies.
- **Activation:** until §17 populates the anchors and flags scope entries, no Operation requires evidence.
- A deterministic canonical encoding per Operation version is an implementation specification.

---

## 16.6 Execution Semantics

### 16.6.1 One request → one declared Operation (Decision B)

- An **accepted** request executes **exactly one** declared Operation: the one it names. A refused request executes none.
- An Operation runs its `internal_steps` **exactly as its catalogue definition specifies**:
  - in the declared order;
  - using only the profiles the matching scope entry declares for those steps;
  - with internal bindings supplied only by K6;
  - with abort-on-failure as the only deviation.
- K6 **does not**:
  - chain Operations;
  - derive further Operations from results;
  - schedule Operations as a consequence of execution;
  - invoke any undeclared Operation or profile;
  - let a request add, remove, reorder or select internal steps.
- **Example: `file.replace`.** Its internal steps are stage → validator → atomic commit → postcondition. These are one Operation. The validator is fixed by the scope entry at K11 load time, verified by executable identity, and run as an internal step. It is never a separately requested or dynamically selected Operation.
- **Per-Operation contract.** Each definition states:
  - preconditions and internal steps;
  - which steps may cause a host effect;
  - the timeout, which covers all steps;
  - cancellation points;
  - interruption and partial-effect behaviour (from `effect_model`, per step);
  - postcondition;
  - retry and idempotency classes.

### 16.6.2 Result model

Three axes, plus a derived outcome:
- **Termination cause:** `NOT_STARTED`, `COMPLETED`, `ERROR`, `TIMED_OUT`, `INTERRUPTED`, `CANCELLED`. The journal also records **the internal step at which it occurred**.
- **Effect certainty:** `NONE_GUARANTEED`, `NONE_EVIDENCED`, `COMPLETE`, `PARTIAL`, `UNKNOWN`.
- **K6 verification:** `NOT_DEFINED`, `VERIFIED`, `FAILED`, `UNAVAILABLE`.

**Canonical outcome** (exactly one per request):

| Outcome | Definition |
|---|---|
| **REFUSED** | Not executed; `NONE_GUARANTEED`. |
| **SUCCESS** | All internal steps completed as defined. If a postcondition is defined, it was `VERIFIED`. If none is defined, verification is `NOT_DEFINED` and K4 still performs Job-level verification (§8). |
| **FAILED** | Executed, with **positive evidence** that the intended effect did not occur. Examples: failure at a step declared not to cause an effect (a staging or validator failure, with the staged content discarded); defined no-effect error semantics; an `ATOMIC` postcondition that shows the pre-state. |
| **PARTIAL** | Evidence that some but not all intended effects occurred. |
| **UNKNOWN** | The effect cannot be established. |

`TIMEOUT` and `INTERRUPTED` are **causes**. Each resolves to FAILED, PARTIAL or UNKNOWN according to the evidence and the step at which it occurred. An error exit at an effect-bearing step without defined no-effect semantics resolves to UNKNOWN.

### 16.6.3 Cancellation and rollback

- **Before any effect-bearing step:** the request becomes REFUSED(`CANCELLED`) if it was never accepted, or FAILED/`NONE_EVIDENCED` if only non-effect steps (such as staging) had run.
- **At a declared `SAFE_ABORT` boundary:** K6 aborts, and the outcome follows the evidence.
- **Otherwise:** the cancel request is journaled and execution continues.
- **K6 never rolls back on its own initiative.** Compensation, such as `file.restore_preimage`, is a separate, fully validated request. Discarding staged content after a validator rejects it is not rollback, because nothing was committed.

---

## 16.7 Read Operations

- **Freshness:** every read observes the host at request time. K6 keeps no cache. Each result carries `observed_at` (K6 clock) and a journal reference.
- **Normalisation boundary:** K6 performs mechanical framing only. Semantic interpretation belongs to K5, or to K4 for generic discovery.
- **Bounds:** the output limit is the minimum of the catalogue, scope and request limits. Truncation is always flagged.
- **Exposure modes:** `FULL`, `REDACTED`, `DIGEST_ONLY`, `METADATA_ONLY`.
  - Credential-bearing resources must not be `FULL`.
  - `host.process_inventory` under the Core Discovery Declaration is `METADATA_ONLY`.
  - Resolved credential values are exact-match scrubbed from all output.
- **Provenance:** Operation and version, declaration ID, resource reference, resolved object identity, `observed_at`, journal sequence.
- **Untrusted data:** K6 never follows references found in observed data, and never turns observed data into new requests.
- **Journaling:** metadata and a content digest only, never content.
- **If K8 is unavailable, K6 refuses all new requests, including READ** (§16.10.4).

---

## 16.8 Write Operations

Sequence for a WRITE:

1. Validation (§16.4).
2. **Write-ahead intent:** `EFFECT_ATTEMPT_STARTED` is journaled with the pre-state observation *before the first effect-bearing internal step*.
3. Internal steps execute in their declared order. Each is journaled as `OPERATION_STEP` (§16.10).
4. The termination cause and the step reached are captured.
5. The postcondition step runs, where defined.
6. The result is journaled.
7. K6 replies.

**`file.replace` as one declared Operation**
- **Stage:** content is written to a K6-internal staging location that no requester can address. This step has no effect on the target.
- **Validate:** runs the scope entry's declared validator profile, identity-verified, READ class, with `run_as` unprivileged unless root is declared, no handles, and the staged object supplied as an internal binding. This step is mandatory for `executable_semantics` entries.
- **Commit:** atomic where the filesystem supports it. This is the effect-bearing step. The pre-image is retained where declared.
- **Postcondition:** a digest comparison of the target against the staged content.
- **Failure mapping:**
  - failure at stage or validate → FAILED, `NONE_EVIDENCED`;
  - failure during commit → decided by evidence;
  - postcondition failure → UNKNOWN (with `verification = FAILED`), unless atomicity evidence shows the pre-state (FAILED).

**General write rules**
- A failed verification never implies that the effect did not occur.
- There is no automatic retry and no automatic rollback.
- At most one WRITE is in flight per resolved resource.

---

## 16.9 Credential Handles

| Question | Rule |
|---|---|
| Who defines a handle | An Execution Declaration in K11: `handle_id`, class, and the scope entries allowed to use it. The Core Discovery Declaration may declare **none**, and validator profiles use **none**. |
| Where the credential exists | Only in K6's root-only credential storage (its design belongs to §19) |
| Who may reference it | Only a request using a scope entry that lists the handle, within that declaration. Handles cannot be referenced by free name or across declarations. |
| Scope binding | Bound to specific scope entries, and so to specific Operations and resources |
| Provisioning | §19 / §22. No request field carries credential material into K6. |
| Invalid or unprovisioned | REFUSED(`CREDENTIAL_UNAVAILABLE`) |
| Endpoint safety | K6 sends a credential to an endpoint only after the endpoint's owner identity has been verified (CF-4) |
| Logging and redaction | K8 records the handle ID and whether it resolved, never the value. Output is exact-match scrubbed. Credential material never appears in results or errors. |

---

## 16.10 K8 Executor Journal

### 16.10.1 Minimum event types

- **Executor lifecycle:** `EXECUTOR_STARTED` (with the loaded catalogue and declaration digests), `EXECUTOR_STOPPING`.
- **Declaration loading:** `DECLARATIONS_LOADED` / `DECLARATION_REJECTED` (including reserved-namespace violations and Core Discovery constraint violations).
- **Connections and requests:** `CONNECTION_REJECTED`, `REQUEST_RECEIVED`, `REQUEST_REFUSED`, `REQUEST_ACCEPTED`.
- **Execution:** `EFFECT_ATTEMPT_STARTED`, **`OPERATION_STEP`** (step name, the executable identity verified for any profile used, and the step result), `EFFECT_ATTEMPT_ENDED`, `POSTCONDITION_EVALUATED`, `CANCEL_REQUESTED`, `RESULT_RECORDED`.
- **Recovery:** `INTERRUPTION_DETECTED`, `OUTCOME_UNKNOWN_DECLARED`, `JOURNAL_FAILURE_RECOVERED`.

**Internal steps are events of the same request.** They never appear as separate requests.

### 16.10.2 Minimum record fields

- `journal_seq`, `event_type`, `k6_time`
- `request_id`, `idempotency_key`, `job_id` (as claimed)
- `integration_id`, i.e. the declaration ID, plus the **declaration kind** (Integration / Platform Services / Core Discovery)
- `capability_id`, `op_id@version`, class
- the internal step (where applicable)
- resource references and their resolved identities
- the executable or endpoint identity verified
- a canonical parameter digest, plus the non-sensitive parameter values
- `authorization_ref` and `principal_claim` (as claimed)
- approval-evidence ID and its verification result
- `declaration_digest`
- the refusal code, or: termination cause, effect certainty, verification and outcome
- pre-state and post-state digests
- handle IDs

### 16.10.3 Relationships

- `request_id` → many journal events.
- `job_id` → many requests (as K4 claims them).
- K4 audit references `journal_seq`.
- **K8 records what K6 received and did. K4's audit records what SCC decided and why.**

### 16.10.4 Journal-before-report and journal failure

- K6 returns no result before its terminal event is durable in K8.
- **If K8 is unwritable, K6 refuses all new requests, READ and WRITE.**
- A WRITE already past its intent record runs through its remaining internal steps, holds its result, and retries the journal. If K6 dies first, the request becomes UNKNOWN on restart.
- There is no unjournaled mode and no bypass.

---

## 16.11 Duplicate / Replay / Idempotency

| Case | Behaviour |
|---|---|
| New `request_id` within the acceptance window | Normal processing |
| Same `request_id`, identical content | **DUPLICATE:** returns the recorded outcome, or `IN_PROGRESS`, or UNKNOWN. Never re-executed. |
| Same `request_id`, different content | **REPLAY:** refused |
| Outside the acceptance window | **REPLAY/STALE:** refused. K8 retention must cover at least the window (retention itself belongs to §19). |
| Approval nonce already used | **REPLAY:** refused |
| Same `idempotency_key`, prior outcome SUCCESS | REFUSED(`ALREADY_COMPLETED`) |
| Same key, prior outcome FAILED or REFUSED | Allowed |
| Same key, prior outcome UNKNOWN or PARTIAL | Refused unless `reconciled_after` references the prior terminal record |
| `retry_class = NEVER_AUTOMATIC` | Always requires `reconciled_after` |
| After a K6 restart | State is rebuilt from K8. Dangling intents become UNKNOWN **before** any new request is accepted. |
| Lost response | Never treated as "did not happen". K4 resends the identical request, or calls `executor.request_status`. |

---

## 16.12 Interruption and Partial Effects

| Event | Outcome |
|---|---|
| Crash before `REQUEST_ACCEPTED` | REFUSED (`EXECUTOR_INTERRUPTED_BEFORE_EFFECT`), established at restart |
| Crash after acceptance, before any effect-bearing step (e.g., during staging or validation) | FAILED, `NONE_EVIDENCED`. The journal shows no `EFFECT_ATTEMPT_STARTED`, and staged content is discarded at restart. |
| Crash after `EFFECT_ATTEMPT_STARTED`, before the result | **UNKNOWN** |
| Tool killed, or timeout after an effect-bearing step began | UNKNOWN; or FAILED (`ATOMIC` and the pre-state is observed); or SUCCESS (postcondition verified) |
| Host-side partial completion | PARTIAL where evidence shows a subset; otherwise UNKNOWN |
| Postcondition impossible to evaluate | UNKNOWN if a postcondition is defined; SUCCESS with `NOT_DEFINED` if none is defined |

Atomicity is claimed only where `effect_model = ATOMIC` and the host mechanism actually provides it.

**K4's obligations on UNKNOWN:**
- mark the Job step uncertain;
- never report success or failure;
- never resubmit automatically;
- reconcile through K6 reads;
- surface the uncertainty to the user;
- resubmit only under §16.11 with `reconciled_after`.

---

## 16.13 Privilege Reduction / Executor Splitting

The evaluation from the prior candidate stands unchanged:
- **A:** one root K6.
- **B:** split read and write executors. Rejected: the benefit is small, and credentials would be duplicated in a second root process.
- **C:** distribution-specific privilege systems. Rejected: they require host-policy changes and hurt portability.
- **D:** process hardening.
- **E:** per-profile `run_as`.

**v1 posture: A + E + D.** B and C are not adopted.

Changes in this revision:
- **E** now also covers validator profiles: they run unprivileged unless root is explicitly declared.
- **Decision C adds a security benefit to A without cost to posture.** Tool invocations are bound to approved executable identities, which removes executable substitution by non-root actors as a path to root execution through K6.
- **B should be revisited** if non-built-in Integrations are ever proposed, or if K6's read-side parsing grows.

---

## 16.14 Normative Invariants

Numbering is kept. X-03 is amended, X-05 is replaced, and X-34 to X-39 are new.

**Vocabulary**
- **X-01** K6 MUST refuse any `op_id`/major version not in the loaded Operation Catalogue.
- **X-02** K6 MUST NOT accept request parameters of any type outside §16.1.5. There MUST be no path, command, URL, script, module or query type. Internal binding types MUST NOT be accepted from requests.
- **X-03** *(amended)* `tool.invoke`, `endpoint.call` and `file.replace` validator steps MUST execute only K11-declared profiles whose every variable slot is typed. K6 MUST NOT invoke a shell. K6 MUST refuse at load time any profile whose executable is a general-purpose shell, a directly invoked interpreter or an exec-wrapper, and any profile whose slots could supply code, a script path, a module name or interpreter options.
- **X-04** The set of Operations, profiles and internal step definitions MUST be fixed at K11 load. No request may add, alter or extend them.
- **X-05** *(replaced)* Each accepted request MUST execute exactly one declared Operation, the one it names, and a refused request MUST execute none. K6 MUST NOT dynamically chain Operations, derive additional Operations from execution results, or schedule additional Operations as a consequence of execution. An Operation MAY contain only the internal mechanical steps explicitly defined in its Operation Catalogue definition, executed in their declared order with abort-on-failure as the only deviation. No request field may add, remove, reorder or select those steps or the profiles they use.

**Scope and declarations**
- **X-06** K6 MUST derive class, scope, capability or function binding, bounds, exposure modes, handle bindings, internal steps, validator selection and executable identities only from K11 and the Host Restriction Overlay. Request-supplied equivalents may only be compared against K11 and refused on mismatch.
- **X-07** K6 MUST refuse a request whose `declaration_digest` differs from the loaded declaration.
- **X-08** K6 MUST exclude an Execution Declaration that fails signature or policy validation, without affecting other declarations.
- **X-09** The Host Restriction Overlay MUST be narrowing-only, MUST NOT contain principals, roles or per-user rules, and MUST NOT be writable by W, C or I.
- **X-10** A WRITE scope entry with `executable_semantics` MUST declare a validator profile, and K6 MUST run it as a declared internal step before commit.

**Validation and authorization interface**
- **X-11** K6 MUST authenticate the P6 caller as C through OS-enforced peer identity before processing.
- **X-12** K6 MUST validate every parameter against the narrowest of catalogue, scope and overlay bounds.
- **X-13** K6 MUST resolve host objects only through declared resources, and refuse any resolution that escapes the declared root.
- **X-14** K6 MUST check `expected_state` against the host immediately before the effect-bearing step, and refuse on mismatch.
- **X-15** K6 MUST refuse a WRITE lacking `authorization_ref` and `job_id`, and MUST NOT use `authorization_ref` or `principal_claim` for any decision beyond checking presence.
- **X-16** Where K11 requires approval evidence, K6 MUST verify signature, anchor, digest binding, expiry and nonce single use.
- **X-17** K6 MUST NOT make or evaluate authorization policy.

**Execution and outcome**
- **X-18** K6 MUST report exactly one canonical outcome per request: REFUSED, SUCCESS, FAILED, PARTIAL or UNKNOWN.
- **X-19** K6 MUST NOT report FAILED without positive evidence of no effect, and MUST report UNKNOWN when the effect cannot be established.
- **X-20** K6 MUST NOT report SUCCESS for an Operation with a defined postcondition unless that postcondition was verified.
- **X-21** K6 MUST NOT retry, roll back or compensate on its own initiative.
- **X-22** At most one WRITE MAY be in flight per resolved resource.

**Reads and data**
- **X-23** K6 MUST NOT interpret observed output as instructions, or follow references found in it.
- **X-24** K6 MUST apply declared exposure modes, MUST NOT return `FULL` content from credential-bearing resources, and MUST scrub resolved credential values from all output.
- **X-25** K6 MUST NOT cache observations, and every read MUST carry `observed_at`.

**Credentials**
- **X-26** K6 MUST resolve credentials only through handles bound to the scope entry in use, and MUST NOT return, log or journal credential values.

**Journal**
- **X-27** K6 MUST journal RECEIVED after schema validation, a terminal event for every request, every internal step of an accepted Operation, and a write-ahead intent before the first effect-bearing step of every WRITE.
- **X-28** K6 MUST NOT report any result before its terminal event is durable in K8.
- **X-29** If K8 is unwritable, K6 MUST refuse all new requests (READ and WRITE), and MUST NOT offer any unjournaled mode.
- **X-30** On start, K6 MUST convert every dangling intent into an UNKNOWN outcome before accepting new requests.

**Replay and idempotency**
- **X-31** K6 MUST reject a reused `request_id` with different content, and any request outside the window. It MUST answer an identical duplicate from K8 without re-executing.
- **X-32** K6 MUST refuse re-execution under an idempotency key whose prior outcome was SUCCESS, and MUST require `reconciled_after` where the prior outcome was UNKNOWN or PARTIAL.

**Privilege and identity**
- **X-33** Profile invocations, validators included, MUST run as the profile's declared `run_as`. `root` MUST be explicitly declared.
- **X-34** *(new, Decision C)* Every tool profile MUST declare an Approved Executable Identity (`DIGEST_PINNED` or `PACKAGE_ATTESTED`), plus an interpreter identity where the executable is interpreted. K6 MUST verify these identities before execution, MUST execute the same object it verified, and MUST refuse on mismatch with `EXECUTABLE_IDENTITY_MISMATCH`. A path alone MUST NOT be sufficient.
- **X-35** *(new, CF-4)* Every endpoint profile MUST declare an expected endpoint owner identity. K6 MUST verify it before sending any request or credential, and refuse on mismatch with `ENDPOINT_IDENTITY_MISMATCH`.

**Core Discovery (Decision A)**
- **X-36** The Core Discovery Declaration MUST be signed. It MUST contain only READ scope entries over the `host` family, MUST NOT contain file, log, service, package, tool or endpoint entries, product- or platform-specific resources, or credential handles, and MUST declare `METADATA_ONLY` exposure for process inventory. K6 MUST refuse to load a Core Discovery Declaration that violates this.
- **X-37** The reserved SCC declaration namespace MUST be usable only by the Core Discovery Declaration and the SCC-shipped Platform Services declarations. K6 MUST refuse to load any Integration Declaration that claims it.
- **X-38** *(new, Decision B)* A validator profile MUST be referenced only by a scope entry as an internal step of `file.replace`. It MUST NOT be requestable as an Operation, MUST be READ class, MUST NOT use credential handles, and MUST receive the staged object only as an internal binding.
- **X-39** *(K4 obligation)* K4 MUST use the Core Discovery Declaration identifier only for its own generic discovery requests, and MUST NOT use it for requests originating from any K5 worker. K6 cannot verify this; the resulting exposure is bounded by X-36.

**Required coverage from the brief:**

| Requirement | Invariants |
|---|---|
| One request → one declared Operation | X-05 |
| No dynamic chaining | X-05, X-38 |
| Executable identity binding | X-34 (endpoints: X-35) |
| Core Discovery Declaration | X-36, X-37, X-39 |
| K11-only scope authority | X-06, X-09 |

---

## 16.15 Open Questions

Former C-1 is removed because it has been decided. Q-1 to Q-6 are kept, with wording adjusted where needed. Q-7 is new.

| # | Question | Why not §16 | Owner | Blocks implementation? | Affects §15? |
|---|---|---|---|---|---|
| Q-1 | Which scope entries require approval evidence (e.g., `executable_semantics` writes, package installs); who holds approver keys; anchor provisioning and revocation. *The Core Discovery Declaration is READ-only and never carries `approval_required`.* | Approval model | §17 (anchors: §22) | Blocks enabling WRITE entries that §17 designates high-risk, not READ or core K6 | No |
| Q-2 | Credential storage, provisioning and rotation; pre-image retention; K8 retention (at least the replay window) | Data lifecycle | §19 | Blocks credential provisioning only | No |
| Q-3 | K8 tamper-evidence; comparing K8 with K4 audit; off-host export | Threat model and integrity | §18 / §19 | No | No |
| Q-4 | Whether K9 may call K6 directly, and under which identity rules | Recovery authority | Recovery gate | No | T-29 (already deferred) |
| Q-5 | Who edits the Host Restriction Overlay and the package-source allowlist | Lifecycle and recovery | §22 / recovery gate | No (defaults: empty overlay; allowlist shipped with the release) | No |
| Q-6 | Job states that consume K6 outcomes | Job model (CHANGE-007) | §8 amendment | Blocks K4 Job implementation, not K6 | No |
| Q-7 | How and by whom Execution Declarations are refreshed when an external Security System upgrade changes a `DIGEST_PINNED` identity; which Host Environments qualify for `PACKAGE_ATTESTED` | Lifecycle and compatibility | §22 (refresh) / §12 Host Environment (qualification) | No: `DIGEST_PINNED` is always available, and a mismatch degrades safely | No |

---

## 16.16 Gate Assessment

### Internal consistency audit

| Check | Result |
|---|---|
| One Operation vs. internal Operation mechanics | Resolved by X-05 and `internal_steps`. One correction to the brief's proposed wording: "exactly one" applies to **accepted** requests, because refused requests execute nothing. Without that qualification, X-05 would contradict REFUSED. |
| Profiles vs. closed vocabulary | Consistent. Profiles are closed at load (X-04) and identity-bound (X-34). |
| Validator profiles vs. no dynamic chaining | Consistent via X-38. See **CF-2**. |
| K11 vs. request-supplied scope | Consistent (X-06, extended to steps, validators and identities). |
| Core Discovery vs. Integration terminology | Consistent via §16.2.4 and the `integration_id` field semantics. See **CF-5**. |
| Approval evidence vs. §17 ownership | Consistent. The interface is unchanged; activation belongs to §17. |
| K4 authority vs. K6 enforcement | Consistent. X-39 adds a K4 obligation and no K6 policy. |
| K8 journal-before-report; K8 failure | Consistent. Steps journaled under X-27; X-28 and X-29 unchanged. |
| UNKNOWN/PARTIAL semantics | Consistent. Step-aware mapping added (§16.6.2, §16.12); no new outcomes. |
| Retry/idempotency | Unchanged. |
| Credential handles | Consistent. Core Discovery and validators hold none; endpoint identity is checked before credentials are sent (CF-4). |
| `executable_semantics` | Consistent. The validator is now an identity-bound internal step. |
| Resource confinement | Consistent. Staging is K6-internal and not addressable by requests. |
| Profile executable identity | Added (X-34). See **CF-3**. |

**Consistency findings, all resolved within §16:**
- **CF-1: grant for the executor family.** The prior candidate did not say which grant authorises `executor.*`. Resolution: `grant_mode = CALLER`. These operations are available to authenticated C with no scope entry, are READ, touch no host state, and are journaled.
- **CF-2: validator input vs. "no path type".** A validator needs the staged content's location, but requests have no path type. Resolution: internal binding slot types, filled by K6 only (§16.1.5, X-02, X-38).
- **CF-3: "no interpreter" vs. realistic executables. Needs your review.** Some Security System CLIs are interpreted programs; the Fail2Ban client is typically a Python program (verify per distribution). The prior deny rule targeted *general-purpose* executors. Resolution adopted: the profile executable must not *be* a shell, interpreter or exec-wrapper, and no slot may supply code or interpreter options. An interpreted program is permitted only when **both** the program and its interpreter are identity-bound (X-03, X-34).
  - **For you to decide:** if "no interpreter" was meant to prohibit interpreted programs entirely, those Integrations must use endpoint profiles (sockets or D-Bus) where available, or cannot be supported. Nothing in §15 depends on this choice.
- **CF-4: endpoint identity.** Decision C covered executables. The equivalent gap exists for endpoints: without it, a spoofed socket or bus name could receive credentials. Resolution: X-35.
- **CF-5: Platform Services terminology. Needs your review.** The prior candidate filed the Platform Services worker's scope under "Integration Declarations". Under §15 it is part of the Platform Adapter, not an Integration: the same terminology issue that Decision A addressed for Core Discovery. Resolution: a separate "Platform Services Declaration" kind, with the ID in the `integration_id` field and the declaration kind recorded in K8. Renaming the field to `declaration_id` is an optional editorial change and is not applied here.

### §15 compatibility (T-01 to T-31)

| Invariant | Status | Note |
|---|---|---|
| T-01 | Preserved | Profile `run_as` identities belong to invoked host tools, not SCC runtime components. |
| T-02 / T-07 | Preserved | K6 remains the sole host-access point. Core Discovery reads go through K6. |
| T-03 | Preserved | No K3 path. |
| T-04 | Preserved | K4 performs no host operation; it requests them through the Core Discovery Declaration. |
| T-05 / T-06 | Preserved | Generic discovery stays in K4, product logic stays in K5, and K6 loads no Integration code. |
| T-08 | Preserved | X-11. |
| T-09 | Preserved | K11 is authoritative, now also for steps, validators and executable identities (X-06). |
| T-10 | Preserved | X-12 to X-14, X-34, X-35. |
| T-11 | Preserved | X-05: internal steps are fixed parts of one declared Operation, not K6-initiated Operations. |
| T-12 | Preserved | Strengthened by step journaling (X-27). |
| T-13 / T-14 | Untouched | |
| T-15 | Preserved | X-17. |
| T-16 / T-17 | Preserved | Scope is K11-bound. K4 cannot widen. Core Discovery use is limited by X-39 and bounded by X-36. |
| T-18 / T-19 | Preserved | Credentials stay in K6. Core Discovery and validators hold none. |
| T-20 | Untouched | |
| T-21 | Preserved | Profile executables are Security System software, not SCC runtime code. Their identity is now bound in K11. |
| T-22 | Preserved | No non-built-in load path. The reserved namespace is protected (X-37). |
| T-23 to T-27 | Untouched / preserved | The Core Discovery Declaration contains no product- or platform-specific resources (T-27). |
| T-28 | Preserved | Identity mismatch, overlay narrowing and K8 failure lead to stale or unavailable state, never absent. |
| T-29 | Preserved | No bypass mode. |
| T-30 / T-31 | Untouched | |

### Disposition

**PASS — READY FOR §17**, once you approve, with CF-3 and CF-5 noted for your review. Neither is a conflict with §15.

### Locked

- Two-tier closed vocabulary. Parameter types and internal binding types.
- **One request → one declared Operation with fixed internal steps** (X-05, X-38).
- K11 structure: Operation Catalogue, Global Execution Policy, Trust Anchors, and three Execution Declaration kinds (Integration, Platform Services, Core Discovery), plus scope entries and the narrowing-only overlay.
- **Core Discovery Declaration** (X-36, X-37, X-39).
- **Approved Executable Identity** (X-34) and endpoint owner identity (X-35).
- Configuration-as-code protection.
- Request contract and the trust classification of each field.
- Validation order and refusal taxonomy.
- Result model (three axes plus outcome) with step-aware mapping.
- Read exposure modes and the no-interpretation rule.
- Write-ahead journaling, journal-before-report, and refusal of all new requests while K8 is unavailable.
- Replay and idempotency semantics.
- Credential handles.
- The approval-evidence interface (inactive until §17).
- Privilege posture A + E + D.

### Remaining open

Q-1 to Q-7.

### Conflicts

None.

### What §17 may and may not do

**§17 may define:**
- principals, roles and grants;
- authorization policy and approval policy;
- approver authority, including population and revocation policy for the K11 Approver anchor set (provisioning mechanics belong to §22);
- which scope entries or classes set `approval_required`;
- how K4 produces `authorization_ref`;
- revalidation semantics.

**§17 must not:**
- redefine K6's Operation vocabulary or internal steps;
- redefine K6's physical scope enforcement or identity binding;
- bypass K11;
- give the Core Discovery Declaration any WRITE or approval semantics;
- turn K6 into an authorization engine;
- change the §16 approval-evidence interface without an explicit §16 amendment.
