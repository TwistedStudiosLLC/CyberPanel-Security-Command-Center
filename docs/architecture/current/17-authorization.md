> **Document status:** LOCKED
> **Authority category:** 1 — Locked architecture (see [Authority Hierarchy](../README.md#authority-hierarchy))
> **Source:** §17 final canonical text, including the SYSTEM revocation-triggered cancellation clarification and A-01…A-36 — DEC-008 to DEC-012, DEC-022 (D-10)
> **Normative:** Yes
> **Findings against this text:** none recorded inline (DEC-030, Q2). See [Known Findings Against Locked Text](../README.md#known-findings-against-locked-text): KF-10.
> **Transcription notes:** Normative text reproduced verbatim. Removed process-wrapper text only: the opening italic
> line ("This is the final canonical text, submitted for owner approval. … I have not modified or created any
> files.") and the closing line ("I've stopped here and have not started §18. I'll wait for your explicit
> approval."). The Gate Assessment is retained as part of the approved text; its permission for §18 is historical.
> Current §18 status is set by the architecture index and DEC-015, not by this Gate Assessment.

# SCC §17 — Authorization Model

---

## Terms

- **Principal:** an SCC security identity that can be authorized. There are exactly two classes (§17.1).
- **Actor:** whoever caused an audited event. Every Principal is an Actor. The **Local Root Operator** (K9) is an Actor, but **not** a Principal.
- **Platform Identity Binding:** the immutable link between a HUMAN Principal and one subject of one parent-platform instance.
- **Authentication Context:** the authentication facts K4 took from a verified K2 assertion: assertion ID, platform, subject, authentication time, and any method claims the platform made.
- **Permission:** one of a closed set of **HUMAN** authority verbs (`view`, `request`, `approve`, `cancel`). A Permission is held only through a Grant. SYSTEM holds no Permissions (§17.1.1).
- **Grant:** a record that confers one Permission on a HUMAN Principal or a Role, over a capability selector and a target selector, under closed conditions.
- **Role:** a built-in, release-defined bundle of Grants. Roles do not nest.
- **Fixed System Authority:** the release-defined authority of the SYSTEM Principal (§17.1.1). It is not Grant-derived, and no Permission, Role or K7 record expresses it.
- **Risk Tier:** R0–R4. The SCC-level risk class of a capability (§17.5.3).
- **Admissibility:** domain checks that are **not** authorization: capability available, Integration valid, compatibility permits, management or ownership permits (§5, §12, §14).
- **Intent Authorization:** an early check that a Principal may *ask for* a Capability on a target. It happens before planning.
- **Plan Authorization:** the binding decision over a concrete, digested Plan. It produces the Authorization Decision.
- **Authorization Decision:** the immutable K4 record identified by `authorization_ref`.
- **Approval:** an Approver's signature, in the §16.5 format, over the exact canonical digest of one K6 request.
- **Approver:** a HUMAN Principal who holds an `approve` Grant **and** whose key is anchored in the K11 Approver anchor set.
- **Step-up:** an additional requirement triggered by Risk Tier. It is either **REAUTH** (the authentication is recent enough) or **APPROVAL**.
- **Revalidation:** re-checking an existing Authorization Decision against current authorization state.
- **Authorization Policy:** the release-defined baseline plus local settings. The local settings are closed and can only narrow. Both are versioned.

---

## 17.1 Principals

### 17.1.1 Classes

| Class | Represents | Count | May hold Grants/Roles | May request WRITE | May approve |
|---|---|---|---|---|---|
| **HUMAN** | A person, through a Platform Identity Binding | Any | Yes | Yes, through Grants | Yes, with a Grant and an anchor |
| **SYSTEM** | K4's own autonomous activity: scheduled discovery, health evaluation, reconciliation reads, and lifecycle consequences of revocation | Exactly one reserved Principal | **No.** Its authority is fixed by the release and cannot be granted or changed. | **Never** | **Never** |

**Why only two classes.** A **service** class (API tokens, automation) has no v1 use case, and adding it would open a second authentication path. It is deferred (§17.24). Everything else is either SYSTEM or not a Principal.

**SYSTEM's Fixed System Authority.** SYSTEM may:
- request READ-class discovery, health and reconciliation observations: generic discovery through the Core Discovery Declaration (§16 X-39), and Integration inspection through K5's declarations;
- cancel Jobs as a lifecycle consequence of revocation (§17.12, §17.14).

It may do nothing else. SYSTEM's authority does not depend on K7 authorization state, so observation continues when K7 authorization data is unavailable (§17.16).

**SYSTEM cancellation is not a `cancel` Permission.** The two kinds of cancellation authority are different:

```
HUMAN:   cancel ──► Permission ──► Grant required ──► evaluated by K4 against K7 authorization state
SYSTEM:  revocation-triggered cancellation ──► Fixed System Authority (release-defined)
         ──► no Permission ──► no Grant ──► no Role ──► not K7-derived
```

SYSTEM's revocation-triggered cancellation:
- is **not** the `cancel` Permission;
- does **not** arise from any Grant or Role;
- does **not** make SYSTEM a Principal with Permissions.

It exists only to carry out the consequence of a revocation (§17.14). It applies only to Jobs whose Authorization Decision, Principal or required Approval has been revoked, has expired, or has been deactivated. It follows §16 cancellation semantics exactly. It cannot be used for any other purpose, and no Grant, Role or local policy setting can extend, narrow or confer it.

### 17.1.2 Things that are not Principals

| Concept | Why it is not a Principal |
|---|---|
| Integration, Platform Services, Core Discovery | These are Execution Declaration identities (§16). They bound what *can physically* happen. They never carry *who may* cause it. |
| K4, K5 workers, K6 | Processes. Their trust is defined in §15. |
| Job, Plan | Artifacts that act on behalf of a Principal's decision |
| Session / assertion | Authentication Contexts, which prove a Principal's identity at a point in time |
| Approver key / anchor | Credentials belonging to a Principal |
| **Local Root Operator (K9)** | Host root sits outside SCC's boundary (§15.15). It is recorded as an Actor type. Its authority belongs to the recovery gate, except for the bootstrap act in §17.1.5 and root's control of K11 anchors (§17.9). |

### 17.1.3 Identity

- `principal_id`: opaque, stable and immutable. **It is the only identifier authorization uses.**
- Display identity (name, platform username): mutable and informational. It is **never** used in authorization.
- **Platform Identity Binding:** (`platform_adapter_id`, `platform_instance_id`, `platform_subject_id`). It is immutable. A HUMAN Principal has exactly one.
  - Each Platform Adapter must declare how stable its `platform_subject_id` is over time.
  - Some platforms can reuse a subject identifier, for example by deleting and re-creating the same username (to be verified for CyberPanel). On such platforms, K4 must treat observed absence of the subject as **binding lost** (§17.1.4). A new subject with the same name is a **new, unenrolled identity**. It never inherits the old Principal.

### 17.1.4 Lifecycle

**Principal states:**
- `ACTIVE`
- `SUSPENDED`: automatic and reversible; driven by the binding status below
- `DISABLED`: administrative and reversible
- `REVOKED`: terminal; the `principal_id` is never reused

**Binding status:**
- `CONFIRMED`: a verified assertion was received, or Platform Services recently observed the subject holding the required platform role
- `UNCONFIRMED(since)`
- `LOST`: the subject is absent or has been demoted below the required platform role. `LOST` automatically suspends the Principal.

**Freshness rule.** An interactive request is confirmed by its own verified assertion. For asynchronous revalidation, the binding counts as confirmed only if the last confirmation is within the policy's maximum age. Otherwise, continuing a WRITE is **held** (§15.13).

### 17.1.5 Enrollment and bootstrap

- **A verified platform identity with no enrolled Principal has no SCC authority.** K4 may record that it observed the identity. It creates no Principal and applies no default Grants.
- Enrolling a new HUMAN Principal is an R4 SCC administrative Action (§17.5.3). The Principal is created as `ACTIVE` with **no Grants**.
- **Bootstrap.** The first `scc.administrator` Role Membership can be created **only** by the Local Root Operator, through the host-local path (K9), and is audited as a bootstrap act. The mechanics belong to §22.
- **v1 platform-role restriction.** In v1, a HUMAN Principal may be enrolled, and may act, only while its platform identity holds the adapter-normalized role `PLATFORM_ADMIN`. This platform role only restricts authority; it never grants SCC authority (§15 T-13). Multi-tenant platform roles are deferred.

---

## 17.2 Authentication vs Authorization

| Question | Answered by | K4's role |
|---|---|---|
| **Who is this?** (authentication) | K1 authenticates the human. K2 issues the assertion. | K4 verifies the assertion end-to-end (§15 T-14) and resolves it through the Binding to a Principal. |
| **May they do this?** (authorization) | **K4 only** (§15 T-15) | Evaluates Grants, conditions, policy and step-up |
| **Is this request physically permitted?** (execution enforcement) | **K6** (§16) | Not K4's decision. K6 enforces it independently. |

**Rules:**
- Authorization is evaluated only for a Principal resolved from a **verified** Authentication Context, or for SYSTEM under its Fixed System Authority. There is no authorization based on an unverified claim.
- K4 trusts the platform's statement of *who* (K1 is the identity TCB, §15.5). K4 independently verifies:
  - the assertion's signature, audience, freshness and single use;
  - Binding and Principal state;
  - everything in §17.3 onward.
- The Authentication Context reference is carried into the Authorization Decision (§17.18).
- Authentication-method claims from the platform are recorded, but they **never** satisfy APPROVAL. They can satisfy only REAUTH freshness.
- **K6 authenticates only its caller (C).** It never authenticates Principals. §17 adds no authentication duty to K6 and creates no second authentication path.

---

## 17.3 Roles

**Decision:** built-in, immutable, release-defined roles only. No nesting. Direct Grants are permitted. Custom roles are deferred.

| Role | Grants (summary) |
|---|---|
| `scc.viewer` | `view`: all capabilities, any target, tier ≤ R0 |
| `scc.auditor` | `view`: tier ≤ R1, including SCC audit and K8-derived views |
| `scc.operator` | `request`: all capabilities, tier ≤ R2. `view` ≤ R1. `cancel`: any target, tier ≤ R2. |
| `scc.administrator` | `request`: all capabilities including reserved `scc.*`, tier ≤ R4. `view` ≤ R1. `cancel`: any. |
| `scc.approver` | `approve`: all capabilities, tier ≤ R4. It only takes effect together with a K11 anchor (§17.9). |

**Rules:**
- A Role is a **real security authority**, not a label. Its Grants are evaluated exactly like direct Grants.
- A Role Membership consists of (principal, role, validity, state). Roles cannot contain roles.
- Direct Grants use the same Grant semantics. They exist so authority can be narrowed, for example "operator for Fail2Ban only".
- Authority is the **union** of the Principal's direct Grants and the Grants of its ACTIVE Role Memberships. **There are no deny Grants.** Restriction comes from not granting, from conditions, and from admissibility.
- Roles apply only to HUMAN Principals. SYSTEM holds no Roles (§17.1.1).

---

## 17.4 Grants

### 17.4.1 Structure

| Field | Meaning |
|---|---|
| `grant_id` | Immutable |
| `subject` | `principal_id` (HUMAN only) or a built-in `role_id` |
| `permission` | `view` \| `request` \| `approve` \| `cancel` |
| `capability_selector` | Closed: `EXACT(integration_id, capability_id)` · `INTEGRATION(integration_id, class)` · `CATEGORY(category, class)` · `ALL(class)`, where `class` ∈ {read, write, any}. Reserved `scc.*` capabilities are matched only by `EXACT` or `ALL`. |
| `target_selector` | Closed: `ANY` · `SYSTEM(system_id)` · `CATEGORY(category)` · `COMPONENT(system_id, component_id)` (only where the domain model defines Components) · `SCC` (SCC itself, for `scc.*` capabilities) |
| `max_tier` | Highest Risk Tier covered |
| `conditions[]` | From the closed vocabulary (§17.7). All must hold. |
| `valid_from` / `valid_until` | Optional validity window |
| `state` | `ACTIVE` \| `REVOKED` (terminal) |
| `provenance` | The Actor that created it, the Authorization Decision that created it, and the policy revisions |

### 17.4.2 Semantics

Permission P is held for (principal, capability *c*, target *t*) **if and only if** at least one effective Grant (direct, or through an ACTIVE Role Membership) meets all of the following:
- its subject is ACTIVE;
- the Grant is ACTIVE and within its validity window;
- its permission is P;
- *c* is matched by its `capability_selector`;
- *t* is matched by its `target_selector`;
- tier(*c*) ≤ `max_tier`;
- every condition holds.

K4 records **every** Grant that matched.

**A Grant is not a K11 scope entry:**

| | Grant (§17) | K11 scope entry (§16) |
|---|---|---|
| Says | Principal X may cause SCC Capability Y on SCC target T | Execution Declaration Z may physically invoke Operation Q on Resource R |
| Owner / enforcer | K4 | K11 / K6 |
| Identifiers | SCC domain IDs | Operation, resource and handle IDs |
| Can it widen the other? | **No.** Holding a Grant never adds K11 scope. | **No.** K11 scope never authorizes a Principal. |

**Grants must never name** an `op_id`, profile, `resource_ref`, executable, host path or handle.

---

## 17.5 Capability Authorization

### 17.5.1 What K4 authorizes

K4 authorizes invocations of SCC-level **Capabilities on SCC targets**. It never authorizes K6 Operations directly.

### 17.5.2 Entity chain (these must not be merged)

| Entity | Definition | How authorization relates to it |
|---|---|---|
| **Capability** | A declared, supported operation of an Integration, or a reserved `scc.*` SCC capability | Grants name capabilities |
| **Action** | One requested invocation of a Capability by a Principal on a target | Intent Authorization |
| **Plan** | The concrete, digested set of steps K4 accepts in order to realize the Action | Plan Authorization, which produces the Authorization Decision |
| **Job** | The execution of exactly one authorized Plan | Consumes the Decision and revalidates it |
| **K6 Operation** | One §16 request within a Job step | Carries `authorization_ref`. K6 enforces §16 independently. |

### 17.5.3 Risk Tiers

| Tier | Meaning | Default step-up |
|---|---|---|
| **R0** Observe | Non-sensitive state and read capabilities | None |
| **R1** Sensitive observe | Evidence or diagnostics containing sensitive content; log content; SCC audit and K8 views | None (a Decision record is required) |
| **R2** Operate | Service lifecycle; bans and unbans; scans without host modification | REAUTH |
| **R3** Change | Configuration writes without `executable_semantics`; SCC-side Integration enable/disable; ownership and adoption transitions | REAUTH |
| **R4** Critical | A capability that meets any criterion below | REAUTH **and** APPROVAL |

A capability is **R4** if any of these apply:
- (a) it uses any `executable_semantics` WRITE scope entry;
- (b) it uses any package-family WRITE (install, remove or upgrade);
- (c) it changes authentication or access control for host access (SSH authentication, administrator accounts, firewall policy affecting management access);
- (d) it is a reserved `scc.*` capability: principal enrollment, Grants, Role Memberships, policy, or SCC ownership release;
- (e) the Integration declares it R4.

**Effective tier** is the highest of:
- the Integration's declared tier (signed in K11);
- the tier derived **mechanically** from criteria (a) and (b) using the K11 scope entries the capability uses;
- any tier raise set by local policy.

Tier derivation is monotonic. Local policy may raise a tier and **never lowers** one. A Plan's tier is the highest tier of any of its steps.

---

## 17.6 Resource / Target Authorization

- Authorization targets are **SCC domain objects**: Security System (`system_id`), Security System category, Component (where the domain model defines it), and SCC itself.
  - Integrations are addressed through capability selectors.
  - Ownership and management relationships are **admissibility inputs** (§5), not authorization targets.
- Targets are resolved from Inventory at authorization time. If a target's identity changes (for example, it is re-detected with a new `system_id`), Grants bound to the old identity **stop matching**. This fails closed.
- **Authorization cannot override admissibility.** Suppose a Principal holds `request` on a WRITE capability for a system whose management state doesn't permit SCC writes. The request is refused by admissibility and recorded as an admissibility refusal, not as an authorization denial.
- **K11 still applies.** A Principal authorized at SCC level can cause only what the relevant Execution Declaration physically permits.
  - If a Plan step lacks K11 scope, the Plan is rejected during K4 validation.
  - If K4 wrongly issues such a step anyway, K6 refuses it (`OUT_OF_SCOPE`).

---

## 17.7 Conditions

**Closed vocabulary.** There are no expressions, scripts or custom policy language. Conditions can **only restrict**. A condition that cannot be evaluated counts as **false**.

| Condition | Meaning |
|---|---|
| `AUTH_FRESH(max_age)` | The Authentication Context's authentication time is within `max_age` |
| `PLATFORM_ROLE(role)` | The Binding's latest confirmed platform role is at least `role`. In v1, `PLATFORM_ADMIN` is always implicitly required. |
| `PLAN_MAX_AGE(max_age)` | At Decision time, the Plan's newest input observation is within `max_age` |
| `APPROVAL_REQUIRED` | Adds APPROVAL whenever this Grant is used, even below R4. K4 enforces it; K6 enforces it only where K11 also flags the scope entry. |
| `TARGET_MANAGEMENT_IN(set)` | Narrows the Grant to targets whose management state is in `set`. It can only narrow; admissibility still applies regardless. |

Time-of-day, network-origin and other environmental conditions are deferred.

---

## 17.8 Approval Model

**Definition.** An Approval is an Approver's signature, in the §16.5 format, over the canonical digest of **one** K6 request. The digest covers:
- the declaration and capability;
- `op_id@major`;
- parameters and resources;
- `expected_state`;
- `plan_digest`;
- `deadline`;
- a nonce.

**Approval is not authorization.** Authorization is K4's policy decision that the Principal may cause the Action. Approval is **evidence independent of K4** that an anchored human agreed to *this exact* request. Approval is not a Grant and cannot be derived from one. For K6-executed requests, it is the only authorization-related control that survives a compromised K4.

| Question | Decision |
|---|---|
| Which Actions require approval | Effective tier R4, plus any Grant carrying `APPROVAL_REQUIRED` |
| K11 flags | **Authoring rule:** `approval_required` MUST be set on every scope entry whose use makes a capability R4 under criteria (a), (b) or (e), and on entries used by capabilities meeting criterion (c). This makes approval K6-verifiable wherever K6 is involved. |
| Who may approve | A HUMAN Principal that is ACTIVE with a CONFIRMED binding, holds an `approve` Grant covering the capability, target and tier, **and** has an anchor in the K11 Approver anchor set |
| Must the approver differ from the requester? | **No, by default in v1.** Self-approval is permitted by default. Self-approval is **not** separation of duties. Its security value comes from the approval being signed with an anchored key held outside K1, K2, K3 and K4, not from a second person being involved. Separation of duties is an optional, narrowing local policy that can be enabled per tier. |
| Multiple approvals | **Not verifiable by K6 in v1**, because the §16 interface carries a single evidence item. K4 policy *may* require more than one approval, but that protects only against threats other than K4. Multi-party approval that K6 can verify would need a §16 amendment and is deferred (§17.24). |
| One-time | Yes. The nonce is single-use (§16 X-16), and one Approval covers exactly one K6 request. |
| Bound to Plan / parameters / resources | Yes, all three, through the §16 digest (`plan_digest`, canonical parameters, resources, `expected_state`) |
| Expiry | The request `deadline` inside the digest. Anchor revocation also invalidates it (§17.9). |
| Revocation | By anchor revocation (effective at K6), by the approving Principal becoming non-ACTIVE (effective at K4), by Plan invalidation, or by revocation of the Decision |
| Evidence | Exactly the §16.5 interface. **No redesign.** |

**Rules:**
- **Fully determined before approval.** Every request that needs approval must be completely determined before it is approved, including `expected_state` and `deadline`. If a Plan's later approval-requiring inputs depend on runtime results, the Plan **must be split** into sequential Plans.
- **What you see is what you sign (mandatory).** The approval signing tool **must** derive what it displays from the canonical content being signed. It must never rely on narrative supplied by K4, K3, K2 or K1. It must run **outside** K1, K2, K3 and K4, and outside any browser page served through them. The mechanics belong to §22.
- **K4 pre-check.** Before accepting an Approval into the Plan, K4 checks the approver's Grant and state, and checks the signature against the K11 anchors. K6 verifies the signature again at execution.
- **Approval of K4-internal Actions.** Some R4 Actions have no host effect and never reach K6, such as Grant or policy changes. For these, only K4 verifies the Approval. This protects against a compromised K1, K2 or K3 and against hijacked sessions. It **does not** protect against a compromised K4 (§17.21).

---

## 17.9 Approver Anchor Set

| Question | Decision |
|---|---|
| Who controls it | Local root. It lives in K11, which only root can write (§15 T-21). Neither K4 nor any Principal can change it. |
| How an approver becomes trusted | Two independent conditions are both required: (1) the Local Root Operator adds an anchor entry naming the approver's `principal_id` (K6 ignores the name; K4 uses it); and (2) an SCC administrator gives that Principal an `approve` Grant or the `scc.approver` Role. Neither condition is enough alone. |
| Who adds and revokes anchors | The Local Root Operator only. The mechanics belong to §22. |
| Roles | Anchors carry no roles. Approval *authority* comes from Grants; *key trust* comes from the anchor. |
| Delegation | None (§17.15) |
| Auditing | K4 records each anchor change it observes when reading K11, including the named Principal and the anchor digest. K9 acts are audited as the Local Root Operator. |
| Key rotation (concept) | Add the new anchor, then revoke the old one. Approvals made under the old anchor become invalid once it is revoked. |
| Outstanding approvals after revocation | Invalid. K6 refuses evidence from an anchor that is revoked or absent (§16 X-16), and K4 refuses it at revalidation. The requests must be approved again. |
| Key custody | **Architectural limit:** an approver key stored on the host gives **no** protection against a compromised root-equivalent host or parent platform (§15.15). Protecting R4 against the platform requires the key to be held **off-host**. Custody mechanics belong to §18/§22. |

---

## 17.10 Step-up Authorization

| Aspect | Decision |
|---|---|
| Trigger | The effective tier of the Action or Plan (§17.5.3), plus any `APPROVAL_REQUIRED` conditions |
| Kinds | **REAUTH:** the Authentication Context is recent enough (`AUTH_FRESH`). It defends against stale or hijacked sessions, **not** against a compromised platform. **APPROVAL:** an independent signature (§17.8). |
| Both | Required together for R4 |
| Tied to the Plan | REAUTH is checked at Plan Authorization and recorded in the Decision. APPROVAL is bound per request to the digest, which includes `plan_digest`. |
| Freshness | REAUTH: the authentication time is within the tier's configured maximum age when the Decision is made. APPROVAL: the request `deadline`. |
| How it binds to the action | REAUTH through the Decision record. APPROVAL cryptographically, per request. |

There is no UI design and no assumption about a specific identity provider.

---

## 17.11 Plan Authorization

The sequence is:

1. **Intent Authorization** happens **before** planning, so unauthorized Actions never reach K5 planning or K6 observation.
2. The Plan is proposed by K5 and validated by K4, including K11 coverage.
3. **Plan Authorization** happens when the concrete Plan is committed, and produces the Authorization Decision.
4. Approvals are collected.
5. The Plan becomes executable.

**Rules:**
- The Decision is **bound to `plan_digest`**. The Plan refers to its Decision. The Decision is a separate, immutable record; the Plan does not *contain* the decision.
- **Any change to the Plan changes its digest and requires a new Decision.** The old Decision becomes `INVALIDATED`.
- **Freshness:** `PLAN_MAX_AGE` applies when the Decision is made, and the Decision has an `expires_at`. Physical freshness is enforced separately by `expected_state` at K6 (§16 X-14).
- **No partial authorization.** A Plan is authorized as a whole or not at all. Every (capability, target) pair in the Plan must be covered.
- Individual Job steps are **not separately granted**. They are **revalidated** (§17.13). Approval is per request (§17.8).

**Chain:**

```
Principal ─(verified assertion)→ Intent Authorization ─→ Plan (digest)
   ─→ Authorization Decision [authorization_ref] ─→ Approvals (per request, if required)
   ─→ Job ─→ per-request revalidation ─→ K6 request (§16) ─→ Operation
```

---

## 17.12 Job Authorization

| Question | Decision |
|---|---|
| Inherits from the Plan | A Job references exactly one Decision. Every K6 request in the Job carries that Decision's `authorization_ref`. |
| Start condition | The Decision is `AUTHORIZED` **and** every Approval the Plan requires has been recorded. Approvals are collected before the Job starts. |
| Revalidation | At Job start and before **every** WRITE K6 request (§17.13) |
| Can a Job outlive its authorization? | No new WRITE may be issued after the Decision expires or is revoked, or after the Principal stops being ACTIVE. The Job is **held or halted**, never continued. |
| Revoked while pending | The Job never starts. |
| Revoked or expired during execution | K4 issues no further requests. For a request already in flight, K4 **should** request cancellation under Fixed System Authority (§17.1.1). That cancellation follows §16 semantics: it is effective only before the effect-bearing step, or at a `SAFE_ABORT` boundary. |
| Interrupting running K6 Operations | Not by authorization. Only §16 cancellation applies. |
| Who may cancel | **HUMAN:** the initiating Principal may cancel its own active Jobs. Other HUMAN Principals need a `cancel` Permission, held through a Grant that covers the capability and target. **SYSTEM:** may cancel only as the revocation consequence above, under Fixed System Authority. This is not a `cancel` Permission and involves no Grant. Cancellation never requires step-up and is always audited, with the actor type recorded. |
| Scheduled (recurring) Actions | Allowed only for effective tier ≤ R3 with no APPROVAL requirement. **Each run** gets a new, complete Plan Authorization as the owning Principal at that moment. There is no standing authorization. If the owner becomes non-ACTIVE, the schedule stops. |

---

## 17.13 Revalidation

### 17.13.1 When revalidation happens

| Point | What is checked |
|---|---|
| Plan commit | Full evaluation (§17.22, steps 1–9) |
| Job start | Principal ACTIVE; binding confirmed within its maximum age; Decision `AUTHORIZED` and not expired; every Grant used is still ACTIVE and valid (or equivalent coverage exists under the current policy); Approvals present and their anchors not revoked |
| Before each WRITE K6 request | The same checks, under the **current** policy revision |
| After a revocation or disablement event | K4 immediately marks the affected Decisions and Jobs, which are then held or halted |
| After a long delay | Covered by the per-request check together with `expires_at` |
| After Security System changes | **Not an authorization revalidation.** The Plan is invalidated through admissibility or `expected_state`; a new Plan needs a new Decision. |

### 17.13.2 Four separate mechanisms

| Mechanism | Owner | Question it answers |
|---|---|---|
| Authorization revalidation | K4 | Is this Principal *still permitted*? |
| K6 execution preconditions | K6 (§16 X-14) | Is the host *physically* in the expected state right now? |
| K4 reconciliation | K4 (§20) | What does the host look like now, and what happened? |
| K6 postconditions | K6 (§16 X-20) | Did the Operation's declared effect verifiably hold? |

---

## 17.14 Revocation

| Revoked | Effect | Pending Plans | Queued Jobs | Running Jobs | Completed effects |
|---|---|---|---|---|---|
| Principal (DISABLED / REVOKED / SUSPENDED) | Immediate at K4 | Decisions `REVOKED` | Never start | No further requests; in-flight cancellation per §16 under Fixed System Authority | **Not reversed** |
| Role Membership / Grant | Immediate, at the next evaluation or revalidation | Revalidated; revoked if coverage is lost | Held or halted if coverage is lost | Same as queued | Not reversed |
| Approval (anchor revoked or approver non-ACTIVE) | Anchor: effective at K6 after reload. Approver: effective at K4 immediately. | Affected requests need new approval | Held until re-approved | Affected requests are not issued | Not reversed |
| Authorization Decision | Immediate | n/a | Never start | No further requests; in-flight cancellation per §16 under Fixed System Authority | Not reversed |
| Plan (invalidated) | Its Decision becomes `INVALIDATED` | n/a | Never start | n/a once running, because the Job is bound to its digest | Not reversed |
| Job (cancelled) | §16 cancellation semantics | n/a | Cancelled | Per §16 | Not reversed |

**Rules:**
- **Revocation never implies rollback.** Any compensation is a new Action with its own authorization.
- **Revocation-triggered cancellation** is carried out by SYSTEM under Fixed System Authority (§17.1.1). It is not an exercise of the `cancel` Permission and depends on no Grant.
- **Last-administrator protection:** K4 must refuse any Action that would leave no ACTIVE Principal holding `scc.administrator`. Only the Local Root Operator may produce that state.

---

## 17.15 Delegation

**Deferred for v1.**
- No Principal may delegate authority.
- Approval authority cannot be delegated; it is tied to the Principal's own anchored key.
- An administrator creating a Grant for another Principal (an R4 action) is administration, not delegation. The new Grant does not depend on the creating administrator's continued authority.
- **No self-Grants:** a Principal may not create, modify or re-enable Grants, Role Memberships or Principal state for itself.

---

## 17.16 Fail-Closed Semantics

| Unavailable | HUMAN Actions | SYSTEM observation | Approvals | Authorization administration |
|---|---|---|---|---|
| Authorization store (K7) | **Denied**, including views that require Grants | Continues under Fixed System Authority, but cannot be durably recorded (§15.13) | Refused | Refused |
| Principal, Binding, Role Membership, Grant or revocation state | Denied | Continues | Refused | Refused |
| Approval state or K11 anchors unreadable | R4 denied; lower tiers unaffected | Continues | Refused | R4 refused |
| Policy evaluation (policy revision unreadable or invalid) | Denied | Continues | Refused | Refused |
| Platform (K1) unavailable | No new interactive Actions (no identity). Jobs whose binding confirmation is older than the maximum age are **held**. | Continues | No new approvals via the platform. Off-host approval evidence is still accepted if everything else holds. | Refused (requires an interactive Principal) |
| K4 restart | Decisions persist in K7. Running Jobs are revalidated before any further request. | Resumes | Persist | n/a |

**Default posture:** if authorization cannot be positively established, the Action is **refused**. K4 never continues on stale, cached or assumed authorization state.

SYSTEM's Fixed System Authority is not K7-derived, so it is unaffected by the loss of authorization state.

---

## 17.17 Authorization Caching

**Deferred.** In v1, K4 evaluates against K7 at every decision and revalidation point. The durable Authorization Decision is a record that gets revalidated; it is not a cache. There is no decision cache, no negative cache and no distributed cache.

---

## 17.18 Audit

K4 records the following for every:
- Intent Authorization and Plan Authorization;
- revalidation;
- approval acceptance or rejection;
- cancellation (HUMAN Permission-based, or SYSTEM Fixed System Authority);
- authorization-administration change.

**Fields recorded:**
- **Actor type** (HUMAN, SYSTEM, Local Root Operator) and Principal
- Authentication Context reference
- **Grants** and **Roles** used, or the absence of any matching Grant. For SYSTEM: the fixed-authority basis instead of Grants.
- Capability, Action, and resolved targets
- **Admissibility result, recorded separately from the authorization result**
- Conditions evaluated, with their values
- Effective tier and the step-up required
- Approval evidence references and K4's verification results
- Plan reference and `plan_digest`
- `authorization_ref`
- Decision and reason code
- Timestamp
- Policy identity and revisions (release baseline and local)
- Revalidation results
- Revocation state of every referenced item

**K4 does not record** host execution facts; those belong in K8. K4 records K8 `journal_seq` references and the outcomes K6 reported, marked as reported by K6.

**View decisions:** R0 `view` decisions need not be recorded individually. R1 and above must be. Controlling audit noise belongs to §21.

---

## 17.19 authorization_ref

| Property | Decision |
|---|---|
| Identifies | Exactly one immutable Authorization Decision record in K7 |
| Mutability | The record itself never changes. Status changes are separate, append-only status records: `AWAITING_APPROVAL`, `AUTHORIZED`, `CONSUMED`, `EXPIRED`, `REVOKED`, `INVALIDATED`. |
| Binds | Principal · Authentication Context reference · capability set · Action · target set · `plan_digest` · policy revisions · Grants used · required step-up · `expires_at` |
| Expiry | `expires_at` is the earliest of: the configured maximum, the Plan maximum age, and the earliest `valid_until` among the Grants used |
| Reuse | Valid **only** for the K6 requests of the one Job that executes the bound Plan. K4 refuses any use in another Job or Plan. K6 cannot detect such reuse, because it treats the value as opaque (§17.21). |
| Revocation | Status `REVOKED` stops all further use at K4. |
| K6 | Opaque. Required to be present for WRITE, and recorded (§16 X-15). |

---

## 17.20 Policy Versioning

- **Policy identity.** There are two levels:
  - **Release baseline:** built-in Roles, tier criteria, default step-up, maximum ages. It carries a `policy_id` and revision and ships with the SCC release.
  - **Local settings:** a closed, narrowing-only set with its own revision counter. The allowed settings are: raise tiers, enable separation of duties, shorten maximum ages, and add `APPROVAL_REQUIRED` to tiers below R4. Changing local settings is an R4 `scc.*` Action.
- **Every Decision records both revisions.**
- **Effect of a change:** revalidation always evaluates under the **current** revisions.
  - A tightening applies to pending Plans and running Jobs at their next revalidation point. They are held or invalidated if they fail.
  - A loosening **never** widens an existing Decision. A Decision can only shrink.
- There is no general policy language.

---

## 17.21 Security Boundary / Compromised K4

**What a compromised K4 can do.** K4 owns K7, so a compromised K4 can:
- forge Principals, Grants, Decisions, `authorization_ref` values and K4 audit entries;
- request **every READ** permitted by any loaded Execution Declaration;
- request **every WRITE whose scope entry is not `approval_required`**. Under the §17.8 authoring rule, that means all R2–R3 host effects within declared scope;
- withhold, delay or reorder work, and misreport state to users;
- **present misleading context to approvers**. This is contained by what-you-see-is-what-you-sign, but only if the approval tool actually meets that requirement;
- change K4-internal state for R4 `scc.*` administration without approval, because approval of K4-internal Actions is verified only by K4.

**Protected by K4 only.** Ordinary SCC authorization, Grants, Roles, policy, Plan Authorization and revalidation all depend on K4 being intact.

**Protected by K11/K6 even if K4 is compromised.** A compromised K4 cannot:
- execute outside the Operation vocabulary, the physical K11 scope, or approved executable and endpoint identities;
- obtain credential values;
- perform `approval_required` WRITEs (R4 host effects: `executable_semantics` writes, package changes, changes to host access control) without a valid signature from an anchored key it does not hold;
- reuse a nonce, alter an approved request, or run one past its deadline;
- change K11, the anchors or the overlay;
- erase K8's record of what it caused.

**What §17 adds against threats other than K4:**
- A compromised K1 or K2, a hijacked session, or a compromised K3 can act only as enrolled Principals. They cannot create authority, because enrollment and Grants are held by K4 and are R4 actions.
- REAUTH limits the use of stale sessions.
- R4 host effects additionally require an off-host approval key.
- Lower-privileged insiders are bounded by their Grants.
- Revocation and disablement take effect at the next revalidation point.

**Residual risk, stated plainly:**
- **R2/R3 host effects depend on K4's integrity.**
- **R4 host protection depends on an independent approval key and an independent approval environment** outside K1, K2, K3 and K4.
- **An approver key stored on the host does not protect against a compromised root-equivalent host or parent platform.**
- **§18 must treat these points as primary threat-model inputs.**

---

## 17.22 K4 Authorization Algorithm (normative)

**Phase I — Intent**
1. **Authenticate.** Verify the K2 assertion: signature, audience, freshness, single use. Resolve the Binding, then the Principal. Require the Principal to be ACTIVE and the Binding CONFIRMED. On any failure, **deny**.
2. **Identify** the requested Capability (`integration_id`, `capability_id`, or reserved `scc.*`), the Action, and the targets (SCC domain IDs).
3. **Check admissibility** (this is not authorization): the Integration is valid, the capability is available, compatibility permits it, and management or ownership permits it. Record the result separately. On failure, **refuse as inadmissible**.
4. **Intent Authorization.** Some `request` Grant must cover (capability, target, effective tier) with all conditions true. Otherwise, **deny**.

**Phase II — Plan**
5. **Plan.** K5 proposes the Plan. K4 validates its structure and K11 coverage, and computes `plan_digest`. Every approval-requiring request must be fully determined.
6. **Plan tier** is the highest effective tier among its steps.

**Phase III — Decision**
7. **Plan Authorization.** Re-evaluate step 4 for **every** (capability, target) in the Plan under the current policy, and evaluate `PLAN_MAX_AGE`. If anything is not covered, **deny the whole Plan**.
8. **Step-up (REAUTH).** Check `AUTH_FRESH` against the tier. On failure, **deny** and require fresh authentication.
9. **Create the Authorization Decision** (immutable), which yields `authorization_ref`. Its status is `AWAITING_APPROVAL` if APPROVAL is required, otherwise `AUTHORIZED`.
10. **Approvals.** For each approval-requiring request, receive the evidence and verify:
    - the approver's Principal state and `approve` Grant;
    - the separation-of-duties policy;
    - the signature against the K11 anchor;
    - that the digest matches.

    Record each approval. When all are present, set the status to `AUTHORIZED`.

**Phase IV — Execution**
11. **Create the Job**, bound to the Plan and the Decision. Revalidate (§17.13).
12. **Before each WRITE request, revalidate.** On failure, **hold or halt** the Job and issue no request. If revocation, expiry or deactivation leaves a request in flight, SYSTEM may request its cancellation under Fixed System Authority, following §16 semantics.
13. **Issue the K6 request** with `authorization_ref`, `job_id`, `principal_claim` and, where required, `approval_evidence`, exactly as §16.3 defines.
14. **K6 enforces §16 independently.** K4 records the outcome K6 reports and the `journal_seq` reference.
15. **Complete.** When the Job reaches a terminal state, the Decision becomes `CONSUMED`.

**For K4-internal Actions** (`scc.*` administration): steps 1–10 apply. Steps 11–14 are replaced by K4 applying the change to K7 atomically together with its audit record.

---

## 17.23 Normative Invariants

**Principals and authentication**
- **A-01** Authorization MUST be evaluated only for a Principal resolved from a K4-verified Authentication Context, or for the SYSTEM Principal under its Fixed System Authority.
- **A-02** Authorization MUST use only `principal_id`, and MUST NOT use display names or platform usernames.
- **A-03** A verified platform identity without an enrolled, ACTIVE Principal MUST have no SCC authority.
- **A-04** Platform role facts MUST only restrict authority and MUST NOT confer it. In v1, `PLATFORM_ADMIN` MUST be required.
- **A-05** SYSTEM MUST NOT hold Grants or Roles, MUST NOT request WRITE-class capabilities, and MUST NOT approve. SYSTEM's revocation-triggered Job cancellation MUST be exercised only as release-defined Fixed System Authority. It MUST NOT be treated as, derived from, or expressed as the `cancel` Permission or any Grant. It MUST NOT depend on K7 authorization state. It MUST be limited to Jobs affected by revocation, expiry or deactivation, and MUST follow §16 cancellation semantics.
- **A-06** Integrations, Execution Declarations, processes, Jobs, Plans and sessions MUST NOT be Principals.
- **A-07** The first `scc.administrator` membership MUST originate only from the Local Root Operator.

**Ownership of decisions**
- **A-08** Authorization decisions MUST be made only by K4. K6 MUST NOT be given any authentication or authorization duty by §17.
- **A-09** Authorization MUST NOT override admissibility, and K4 MUST record admissibility and authorization results separately.
- **A-10** Grants MUST NOT name K6 Operations, profiles, resource references, executables, handles or host paths. Holding a Grant MUST NOT widen K11 scope.

**Grants and Roles**
- **A-11** A Permission MUST be held only when an effective, ACTIVE, in-validity Grant matches the permission, capability selector, target selector and tier, and all of its conditions hold.
- **A-12** There MUST be no deny Grants, no Role nesting and no custom Roles in v1.
- **A-13** Conditions MUST come from the closed vocabulary of §17.7. A condition that cannot be evaluated MUST count as false.
- **A-14** A Principal MUST NOT create, modify or re-enable Grants, Role Memberships or Principal state for itself.
- **A-15** K4 MUST refuse any Action that would leave no ACTIVE `scc.administrator`, except when performed by the Local Root Operator.

**Tiers and step-up**
- **A-16** A capability's effective tier MUST be at least both its declared tier and its K11-derived tier. Local policy MUST NOT lower it.
- **A-17** R4 MUST require REAUTH and APPROVAL. R2 and R3 MUST require REAUTH.
- **A-18** Authentication-method claims from the platform MUST NOT satisfy APPROVAL.

**Approval**
- **A-19** Approval MUST use the §16.5 evidence interface unchanged. One Approval MUST authorize exactly one K6 request.
- **A-20** A valid Approver MUST hold an `approve` Grant **and** a K11 anchor naming them. Neither alone MUST suffice.
- **A-21** Approval-requiring requests MUST be fully determined before they are approved.
- **A-22** The approval signing tool MUST derive its display from the canonical signed content, and MUST NOT run within K1, K2, K3, K4 or a browser page served through them.
- **A-23** K11 declarations MUST set `approval_required` on every scope entry used by an R4 capability. This is an authoring rule.

**Plans, Jobs, authorization_ref**
- **A-24** Every WRITE-bearing Plan MUST have exactly one Authorization Decision bound to its `plan_digest`. Any change to the Plan MUST require a new Decision.
- **A-25** A Plan MUST be authorized as a whole or not at all.
- **A-26** `authorization_ref` MUST identify an immutable Decision. K4 MUST accept it only for requests of the Job executing the bound Plan.
- **A-27** A Job MUST NOT start without an `AUTHORIZED` Decision and all required Approvals recorded.
- **A-28** K4 MUST revalidate at Job start and before every WRITE K6 request, under the current policy revision.
- **A-29** After revocation, expiry or Principal deactivation, K4 MUST NOT issue further WRITE requests for the affected Job. Running Operations MUST be affected only through §16 cancellation.
- **A-30** Scheduled Actions MUST be limited to tiers ≤ R3 without APPROVAL, and each run MUST be fully re-authorized.

**Revocation, failure, caching, policy**
- **A-31** Revocation MUST NOT be represented as reversing completed host effects.
- **A-32** When authorization state cannot be positively established, HUMAN Actions MUST be refused.
- **A-33** v1 MUST NOT cache authorization decisions.
- **A-34** Every Decision MUST record the baseline and local policy revisions. A policy loosening MUST NOT widen an existing Decision.

**Audit and the compromised-K4 boundary**
- **A-35** Every Intent Authorization, Plan Authorization, revalidation, approval acceptance or rejection, cancellation and authorization-administration change MUST be recorded with the fields in §17.18. K4 MUST NOT record host execution facts as its own observations.
- **A-36** §17 MUST NOT be represented as protecting against a compromised K4 for any effect that K11 does not flag `approval_required`. R4 host effects MUST remain protected by K6 approval verification, whatever the state of K4.

---

## 17.24 Open Questions

| # | Question | Owner | Blocks? |
|---|---|---|---|
| P-1 | Approver key custody (off-host is required for protection against the platform) and approval-tool mechanics | §18 (threat) / §22 (mechanics) | Blocks enabling R4 host effects. Everything else can proceed. |
| P-2 | Service principals / API automation | Future gate | No (deferred) |
| P-3 | Multi-tenant platform roles (resellers, users) | Future gate plus adapter work | No (v1 is `PLATFORM_ADMIN`-only) |
| P-4 | Multi-party approval that K6 can verify | Would need a §16 amendment | No (deferred) |
| P-5 | K9 authority over authorization state beyond the bootstrap act, e.g. recovering a lost last administrator | Recovery gate | No |
| P-6 | Per-adapter platform subject stability declaration (CyberPanel still to be verified) | Platform Adapter gate | Blocks only the CyberPanel binding implementation |
| P-7 | Delegation, custom Roles, authorization caching, environmental conditions | Deferred by decision | No |
| P-8 | Audit noise control for view decisions | §21 | No |

---

## Gate Assessment

### Internal Consistency

**PASS.**

| Item | Resolution |
|---|---|
| `cancel` Permission vs SYSTEM revocation-triggered cancellation | **Clarified (the required change).** SYSTEM cancellation is Fixed System Authority: no Permission, no Grant, no Role, not K7-derived, and limited to revocation consequences under §16 semantics (§17.1.1, §17.12, §17.14, §17.22 step 12, A-05). The four-verb HUMAN Permission model is unchanged. |
| Approval is per K6 request, but an R4 Plan has several steps | Approvals are collected per request before the Job starts. Non-deterministic approval-requiring Plans are split (A-21). |
| K4-internal R4 Actions have no K6 verification | Stated explicitly: protected against threats other than K4 only (§17.8, §17.21, A-36). |
| Self-approval vs the purpose of approval | The value comes from the independent anchored key. Self-approval is not described as separation of duties. Separation is an optional narrowing (Owner Decision 1). |
| Package writes at R4 | Package install, remove and upgrade are unavailable until an approver anchor is enrolled (Owner Decision 2). |
| Platform unavailable vs asynchronous revalidation | The binding freshness rule is consistent with §15.13 (held, not continued). |
| Scheduled Actions vs approval | Limited to tiers without approval (A-30). |
| SYSTEM authority vs K7 failure | Fixed System Authority is release-defined and not K7-derived. This is consistent with §15.13. |

**Structural separations checked:**
- Authentication (K1/K2), Authorization (K4) and Execution enforcement (K6) stay separate.
- Authorization and admissibility have separate failure semantics (§17.6, A-09).
- SCC authorization (Principal → Capability → Target) and K11 execution authority (Execution Declaration → Operation → Resource) cannot widen each other (§17.4.2, A-10).
- A Plan is the authorized intended structure; a Job executes exactly one Plan.
- A Decision is a separate immutable record bound to `plan_digest`.
- Approval is independent signed evidence, not a Grant.

### §15 Compatibility

**PASS.** T-01 through T-31 are all preserved.
- **T-08:** §17 creates no additional K6 caller.
- **T-09 / T-17:** Grants cannot widen K11 (A-10).
- **T-10:** unaffected.
- **T-13:** the platform session is not SCC authorization (A-03, A-04).
- **T-14:** no second authentication path (A-01).
- **T-15:** K4 is the sole authorization point and fails closed (A-08, A-32).
- **T-16:** Principals are separate from launcher-bound Integration identities (A-06).
- **T-18 / T-19:** no credentials are introduced into K4. Approver keys are held outside SCC components.
- **T-28:** unaffected.
- **T-29:** the bootstrap act is host-local, audited, and limited to A-07. K9 stays outside the Principal model, and no further K9 powers are invented. Recovery authority remains with the recovery gate.

SYSTEM's Fixed System Authority is not K7-derived authorization.

### §16 Compatibility

**PASS.** X-01 through X-39 are all preserved.
- **X-06 / X-09:** Grants and local policy never touch K11 or the overlay.
- **X-15:** `authorization_ref` remains opaque (§17.19).
- **X-16:** the approval evidence interface is unchanged; one Approval covers one request (A-19).
- **X-17:** K6 remains policy-free and does not authenticate Principals.
- **X-18 to X-22 and X-27 to X-32:** consumed as defined. SYSTEM cancellation uses §16 cancellation semantics unchanged.
- **X-34 / X-35:** executable and endpoint identity controls are untouched.
- **X-36 to X-39:** Core Discovery remains read-only and reserved. SYSTEM uses it only for K4's own generic discovery under Fixed System Authority. A human-triggered rediscovery is authorized for the human and then performed by K4 under Core Discovery, which is K4's own generic discovery, not on behalf of K5.

No new execution vocabulary or K6 Operation semantics are introduced.

*Optional, not required:* A-23 is a K11 authoring rule. Having K6 also enforce "`executable_semantics` or package write ⇒ `approval_required`" when K11 is loaded would be stronger, but it would need a §16 amendment. It remains an optional proposal for the owner.

### Required Change

Only one: the SYSTEM revocation-triggered cancellation clarification (§17.1.1, with matching wording in §17.12, §17.14, §17.16, §17.18, §17.22 and A-05).

### Locked

Subject to your approval:
- Principal classes HUMAN and SYSTEM; SYSTEM holds Fixed System Authority, including revocation-triggered cancellation that is not a Permission.
- The Local Root Operator is an Actor, not a Principal.
- Enrollment-only authority, with root-only bootstrap.
- Built-in Roles; direct Grants; no deny Grants; no nesting; no custom Roles.
- Grant structure and closed selectors; the closed condition vocabulary.
- Risk tiers R0–R4 with monotonic derivation from K11; local policy can only narrow.
- REAUTH for R2/R3; REAUTH plus APPROVAL for R4.
- Per-request Approval via the unchanged §16.5 interface; approver trust needs both Grant and anchor; self-approval by default; optional separation of duties; mandatory what-you-see-is-what-you-sign; approval tooling outside K1–K4 and their pages.
- Anchor set controlled by root.
- Whole-Plan Decisions bound to `plan_digest`, with a new Decision on any change.
- One Decision per Job; revalidation at Job start and before every WRITE.
- Revocation table; no rollback; last-administrator protection.
- Scheduled Actions limited to ≤ R3 without approval, each run re-authorized.
- Fail-closed behavior; no caching or delegation in v1.
- Two-level policy versioning; `authorization_ref` semantics, opaque to K6.
- The audit field set.
- The compromised-K4 boundary and its residual risk.
- The normative algorithm; invariants A-01 through A-36.

### Owner Review Items (retained as owner decisions)

1. Self-approval is permitted by default in v1.
2. Package-family WRITE capabilities are R4.
3. Every platform administrator must be explicitly enrolled.
4. v1 is restricted to `PLATFORM_ADMIN`.

### Remaining Open Questions

P-1 through P-8.

### Conflicts

None.

### Gate Disposition

**§17 — PASS — READY FOR §18**
