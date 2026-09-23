> **Document status:** HISTORICAL / FORENSIC — NON-NORMATIVE
> **Authority category:** 5 — Historical / forensic material (see [Authority Hierarchy](../../README.md#authority-hierarchy))
> **What this is:** The historical architecture gate review of the §18 **candidate**
> ([`18-candidate.md`](18-candidate.md)).
> **This document is NOT the current §18 authority.** Current §18 status is established by the
> [architecture index](../../README.md), the [decision log](../../decisions/decision-log.md) (DEC-015) and the
> [open register](../register.md), and summarized in [`README.md`](README.md).
> **No "PASS" wording here or in the candidate is current authority.** In particular, the candidate's historical
> "§18 — PASS — READY FOR §19" self-assessment, and any discussion below of a "path to PASS", do not establish the
> current status of §18. §18 is CONDITIONAL — NOT FULLY LOCKED (DEC-015).
> **Superseded parts of this review:** Its proposed disposition "CONDITIONAL — OWNER REVIEW REQUIRED" and its blocking
> owner decision ODF-18-01 were subsequently addressed by the owner: ODF-18-01 was deferred to each platform's K2 gate
> (DEC-015). Its statements that ODF-18-01 requires a §15 amendment were written before DEC-015.
> **Transcription notes:** Reproduced verbatim. Removed process-wrapper text only: the two-line title heading
> ("# SCC §18 — Threat Model" / "# Architecture Gate Review") was merged into the single title below; the opening
> italic line ("This is a forensic review of the candidate §18 submitted in the previous turn. … I have not modified or
> created any files.") and the closing line ("I have stopped at the end of the forensic gate review. …") were removed.

# SCC §18 — Threat Model: Architecture Gate Review

---

## 1. Executive Gate Finding

The candidate §18 is **substantially correct**. It does not reopen §15, §16 or §17. Most of its compromise boundaries are stated honestly. Its main contributions hold up under review:
- treating K6, K1/K2 and K9 as root-equivalent;
- the analysis of approval-key custody;
- the observation that cross-instance approval replay is possible;
- identifying the local tenant as a threat actor;
- naming resource exhaustion that affects K8 as a way to disable observation.

It is **not ready to lock as written**. The review found five kinds of problem.

**1. One finding that contradicts a claim made in §15 (blocks lock).** §15.6 bounds a compromised K3 to *"only send K4 requests K4 would accept from the authenticated user anyway."* Under the same-origin embedding that §15 OQ-1 allows, this bound is false. A compromised K3, or any unsafe rendering of observed data, runs script inside the parent platform's origin. The viewer is always a `PLATFORM_ADMIN` (A-04), and the platform is root-equivalent (§15.5). Resolving this requires either a constraint on how SCC's UI is embedded or a correction to §15.6. Either one changes §15's text. See TF-18-02 and ODF-18-01.

**2. Four places where the candidate claims more than the architecture guarantees.**
- SP-05 lists K6 as enforcing Plan integrity for R4 requests. K6 enforces request integrity only.
- SC-12 and §18.6/§18.14 treat approval signatures stored in K8 as proof of who approved. Root controls the anchor set, so it can add its own key, and that inference no longer holds.
- T-18-09/SR-12 require tamper evidence without stating that it is meaningless against the component that writes the record.
- SC-09 does not account for an attacker pushing records out of K8 through volume.

**3. Two new SCC-specific threats that change dispositions.**
- §16.2 defines `executable_semantics` as content that makes a *Security System* execute commands. Platform Services writes target the *parent platform*, which that definition does not cover. A compromised K4 could therefore escalate to root through platform configuration without any approval. See TF-18-10.
- K8 retention can be flushed by request volume. See TF-18-09.

**4. Several identifier and consistency defects.**
- Boundary B-04 is missing.
- TH-01 is absent from the taxonomy.
- §18.14 cites T-18-10 for a rule that is actually T-18-09.
- K3 is misclassified under T-A9.
- §18.3 calls everything left of B-07 unprivileged, which contradicts K1/K2 being root-equivalent.
- K10 is listed as able to modify K11.
- SR-08 bundles two unrelated requirements.

**5. The Plan-digest issue is an accepted residual risk, not a defect.** K6 guarantees *per-request* integrity for approval-required requests. It does not guarantee that the Plan is complete, exclusive or correctly ordered at any tier. The candidate says this correctly in §18.10 but contradicts it in SP-05. It needs to be stated as an explicit residual risk and claim.

**Proposed disposition: §18 — CONDITIONAL — OWNER REVIEW REQUIRED.** One owner decision blocks lock (ODF-18-01). Eight others do not block and have coherent interim positions.

---

## 2. Source / Scope

- **Reviewed:** the candidate §18 (§18.1–§18.25 plus Gate Assessment).
- **Reference:** the locked §15 (T-01…T-31, §15.1–§15.18), §16 (X-01…X-39, §16.1–§16.16) and §17 (A-01…A-36, §17.1–§17.24).
- **Operating-system and platform facts** are labelled *(model analysis — verify)*. This applies to process-argument visibility and CyberPanel embedding in particular. They are not treated as established.
- **Out of scope:** writing the corrected §18, starting §19, implementation.

---

## 3. §15 Compatibility Findings

| ID | §15 anchor | §18 statement | Finding | Class |
|---|---|---|---|---|
| CF-18-01 | T-01; §15.3 K3 = identity W | §18.1 puts "a compromised K3" under **T-A9** (parent platform) | **Misclassification.** K3 is an SCC component running as W. It is not part of the platform and not root-equivalent. §18.12 itself calls it "T-A9 (partial)", which is inconsistent. K3 needs its own actor entry, or placement under T-A2 as the brief suggested. | §18 correction |
| CF-18-02 | §15.5, §15.15 (K1/K2 root-equivalent) | §18.3: "Everything to the left of B-07 is unprivileged" | **Internal contradiction.** K1/K2 sit left of B-07 in the diagram and are root-equivalent. | §18 correction |
| TF-18-02 | §15.6 ("a compromised K3 can only send K4 requests K4 would accept…"); §15.18 OQ-1 ("both satisfy §15") | Not identified by the candidate | **The §15 bound is conditionally false.** If SCC views share the platform's origin, a compromised K3 serves script into that origin. That script can use the admin's platform session and act beyond SCC. This contradicts §15.6 and makes OQ-1's "both options satisfy §15" untrue. | **Required §15 amendment or owner decision (ODF-18-01)** |
| CF-18-03 | T-06, T-16; §15.8 (fault isolation required; security isolation between Integrations not required in v1) | TH-18: one worker can interfere with siblings | **Consistent.** §15.8 explicitly accepted this. The candidate correctly labels it accepted (RR-09). | Already satisfied / accepted |
| CF-18-04 | §15.4 item 6 (K4/K6 have no default egress) — **prose, not a T-invariant** | §18.5: "K4 cannot reach the network directly. Holds." | **Cites a non-normative basis.** No T-invariant forbids egress from K4. T-31 covers listeners only. The claim should cite §15.4 prose, or be recorded as a downstream implementation requirement. | §18 correction (weaken citation) |
| CF-18-05 | T-21 (K11 not writable by W, C, I) | §18.8: "Who can modify K11: root only (T-21), through K9, lifecycle (§22) **or K10**" | **Inaccurate.** K10 supervises processes. §15 never gives it a role in modifying K11. | §18 correction |
| — | T-08, T-31 | TH-28 (tenant reaching IPC) | Consistent | Already satisfied |
| — | T-12; §15.13 K8 row | §18.17 (reads refused when K8 is unwritable) | Consistent (§16 X-29 closed the option §15 left open) | Already satisfied |
| — | T-18/T-19 (credential placement) | §18.13 | Consistent. SR-05 adds approver keys, which §15.12 did not cover. That is a new §18 rule, not a conflict. | §18 requirement |
| — | T-29 | T-18-12 | Mostly redundant with T-29. It is slightly broader ("any non-root component"). | See the invariant audit |
| — | §15.5 (what SCC cannot guarantee if the platform is compromised) | §18.12 | Consistent, and more precise | Already satisfied |

---

## 4. §16 Compatibility Findings

| §16 anchor | §18 reliance | Verified? | Finding |
|---|---|---|---|
| X-05 | SC-15 (observed data cannot become K6 instructions) | Yes | — |
| X-06 | SC-02, §18.9 | Yes | — |
| X-08 | §18.8 release-signed class | Yes. §18 correctly says a signature proves authenticity, not freshness. | — |
| X-09 | Overlay is root-authored only | Yes | — |
| X-10 | Used as precedent in TF-18-04 | Yes | K6 already performs a load-time consistency check (a validator is required for `executable_semantics`). That supports treating OD-2 as an execution invariant rather than authorization. |
| X-13 | TH-29 "Partly" | Yes | X-13 already forbids *any* escape, which implicitly includes escape by racing directory components. X-13 does **not** check ownership. See TF-18-05. |
| X-14 | TH-42 | Yes | — |
| X-15 | §18.10 (`authorization_ref` opaque) | Yes | — |
| X-16 | SC-03/04/05, TH-14 | Yes. The nonce is checked "against K8", which makes it **host-local**. §16.5 digest fields contain **no instance identity**. | TH-14 is confirmed |
| X-17 | OD-2 compatibility | See TF-18-04 | A mechanical well-formedness check does not make K6 an authorization engine |
| X-21 | SC-07 | Yes | — |
| X-23 | SC-15 | Yes. It covers K6 only. **No invariant covers presentation.** | That is the gap behind SR-01 |
| X-24 | TH-31 (exact-match scrub only) | Yes | — |
| X-26 | SC-08 | Yes | — |
| X-29 | TH-34, §18.17 | Yes | — |
| X-31 | Replay | Yes | — |
| X-34 | SC-11, TH-27 | Yes. It binds the executable and interpreter, not transitive dependencies. | — |
| X-35 | §18.13 (endpoint checked before credentials are sent) | Yes | — |
| X-36 | §18.13 (process inventory is METADATA_ONLY) | Yes | — |
| X-37/X-38/X-39 | §18.5 (declaration identity only partially trusted) | Yes (§16.3) | — |
| **§16.2 configuration-as-code rule** | Not examined by the candidate | — | **TF-18-10.** The definition covers only content that makes a Security System execute commands. Platform Services WRITE entries targeting the parent platform fall outside it. |
| §16.1.5 profile slot types | TH-30 ("None in §16") | Yes. `handle_ref` is a permitted slot type in argument templates, and §16.8 resolves it at invocation. | TH-30 is confirmed |

No §18 claim relies on a §16 guarantee that does not exist, **except**:
- SP-05 (K6 enforcing Plan integrity; CF-18-06);
- §18.6/§18.14/SC-12 (approval signatures as proof of who approved; CLF-18-05).

---

## 5. §17 Compatibility Findings

| §17 anchor | §18 treatment | Finding |
|---|---|---|
| Principal classes, SYSTEM Fixed System Authority | §18.5 ("request cancellation of any in-flight request") | Consistent. A compromised K4 can issue cancellations either way. No residual risk has been turned into a protection. |
| Enrollment (A-03), Owner Decision 3 | §18.11 | Consistent |
| Tiers, criteria (a)–(e), A-16, A-23 | TH-21 | Consistent. It correctly treats A-23 as an authoring-only rule. |
| Approval (A-19–A-22), anchors (§17.9) | §18.7 | Consistent. The precision "off-host protects the approval, not the host" is **correct and does not conflict** with §17. |
| Self-approval (Owner Decision 1) | TH-10 / RR-10 | Accepted. It is not presented as mitigated. |
| **§17.21:** "a compromised K1/K2 … can act only as enrolled Principals. They cannot mint authority." | §18.12 treats K1/K2 as root-equivalent | **CF-18-07.** §17.21's statement holds only for actions taken *through SCC's interfaces*. Because the platform is root-equivalent, it can also write K7 directly. §18 should state that scope explicitly. This is a §18 clarification, not a conflict: §17.21 never claimed protection against root. |
| A-26 / §17.19 (reuse of `authorization_ref` not detectable by K6) | §18.10 | Consistent |
| A-28 (revalidation window) | TH-36 | Consistent |
| §17.21 compromised-K4 boundary | §18.5 adds cross-instance replay | This is an **addition**. It stays consistent only if SC-03 is given a precondition (CLF-18-01). |
| §17.5.3 criterion (c) | TF-18-10 | Criterion (c) covers *host access control*. It does **not** cover writes to root-equivalent consumers such as the parent platform's configuration. |

---

## 6. Internal Consistency Findings

| ID | Finding | Evidence | Correction |
|---|---|---|---|
| CF-18-01 | K3 is filed under T-A9 | §18.1 vs §18.12 | Give K3 its own actor entry, or place it under T-A2 as a partial compromise |
| CF-18-02 | "Left of B-07 is unprivileged" | §18.3 vs K1/K2 being root-equivalent | Restate: K3, K4 and K5 are unprivileged; K1, K2, K6, K9 and K10 are root-equivalent |
| CF-18-05 | K10 listed as able to modify K11 | §18.8 | Remove K10 |
| CF-18-06 | **SP-05 lists K6 as enforcing Plan integrity for R4** | SP-05 vs §18.10 ("K6 does not check `plan_digest` against any Plan") | Change the SP-05 enforcer to "K4 only; K6 enforces **request** integrity for approval-required requests" |
| CF-18-08 | B-04 is missing | §18.3 goes from B-03 to B-05/B-06 | Renumber, or declare B-04 reserved |
| CF-18-09 | TH-01 is missing from the taxonomy; TH-21, TH-30 and TH-34 each appear twice | §18.4 | Add TH-01. Mark the multi-category entries explicitly. |
| CF-18-10 | §18.14 cites "Forensic rule (T-18-10)" for the fabrication rule | That rule is in T-18-09. T-18-10 is the attestation-source rule. | Fix the reference |
| CF-18-11 | SR-08 combines "tenant-writable resources" and "release review of `approval_required`" | §18.22 | Split into two requirements (see SRF-18-08) |
| CF-18-12 | T-18-08 says "excluded; where unavoidable…" | Internally contradictory | Separate WRITE (MUST NOT) from READ (limited) (TF-18-05) |
| CF-18-13 | TH-06 is labelled a "Gap" | §15.6 already accepts that a compromised K3 can send any request as the authenticated user | Reclassify as an accepted §15 residual that §18 quantifies (TF-18-08) |
| CF-18-14 | The Gate Assessment says "Required architecture changes: none to the locked gates" | Contradicted by TF-18-02 | Correct in the final gate |
| CF-18-15 | TH-32 residual is mapped to RR-03 (compromised root) | TH-32 also covers **honest** root restoring a backup | Map to a separate residual, or to SR-16 without RR-03 |

**Contradiction tests (§28 of the brief):**

| Test | Result |
|---|---|
| K6 claimed to protect something it enforces itself | **Found.** SC-12 / §18.6 (CLF-18-05). |
| Approval called independent while K4 can manufacture it | Not found. The candidate states that K4-internal R4 approvals are verified by K4 only. |
| K8 called tamper-evident while its writer can rewrite it | **Found.** T-18-09 / SR-12 (CLF-18-07). |
| R4 said to require approval while K11 can omit the flag | Acknowledged (TH-21). **A second path exists** (TF-18-10). |
| Plans called immutable while K6 never sees them | **Found.** SP-05 (CF-18-06). |
| Observed data called inert while presentation may render it | Not a contradiction: SR-01 is a requirement and SC-16 is conditional. SC-16's preconditions are incomplete (CLF-18-06). |
| Platform compromise called "contained" | Not found. The candidate is honest here. |
| Tenant said unable to affect K8 while storage is shared | Not found. T-18-11 is a requirement. The candidate missed volume flushing (TF-18-09). |
| Executable identity called protected while dependencies are mutable | Not found. SC-11 scopes it correctly. |

---

## 7. Critical Threat Findings

### TF-18-01 — TH-04 / SR-01: hostile observed data rendered as active content

1. **Supported by the locked architecture?** Yes, conditionally. §15.6 places SCC's UI inside the parent platform's page frame (K2), served by K3. §15.5 already concedes that panel scripts share the page with SCC. §15 contains **no** rule on how observed data is rendered. X-23 covers K6 only.
2. **Is the platform's origin/session a trust boundary?** Only if SCC content runs in the platform's origin. §15 OQ-1 leaves the path open (relay through K2, or a platform proxy route). *(Model analysis — verify for CyberPanel:)* both options in OQ-1 plausibly serve SCC content under the platform's origin. If so, the boundary exists and is currently unenforced.
3. **Does §15 establish a presentation boundary?** No.
4. **Where does it belong?** The principle belongs in §18 as a normative requirement (SR-01 / T-18-01). The mechanism belongs to the Presentation / Platform Adapter gate. The *origin model* affects §15 (TF-18-02).
5. **Does SR-01 overreach?** No. It states an outcome ("inert data") and names no mechanism.
6. **Does SC-16 depend on SR-01 correctly?** Partly. It also depends on K3 not being compromised and on the origin model (CLF-18-06).
7. **Escalation into the platform?** It requires three assumptions:
   - (a) same-origin embedding;
   - (b) the viewer being a platform administrator, which is **guaranteed in v1** by A-04;
   - (c) platform-administrator actions being root-equivalent, which §15.5 assumes.

   Given (a), the escalation path from an unauthenticated external attacker (T-A1) to host root is valid.

**Disposition:** a valid threat. **§18 normative requirement** (SR-01 as it stands). Mechanism goes downstream. Severity: **High where same-origin embedding is used.**

### TF-18-02 — NEW: a compromised K3 escalates into the parent platform through the shared origin

- **Attack path:** K3 (identity W) is compromised through its HTTP parser (§15.3 calls it the exposed parser). It serves modified SCC UI assets. Under same-origin embedding, that script runs with the admin's platform session. The attacker gains platform-administrator actions, which are root-equivalent.
- **Conflict:** this contradicts §15.6's bound on a compromised K3, and §15.18 OQ-1's claim that the choice of path is security-neutral.
- **Disposition:** **§15 amendment required** in one of two forms, chosen by the owner (ODF-18-01):
  - (a) constrain OQ-1 so that SCC-served content runs in an origin isolated from the parent platform; or
  - (b) correct §15.6 so that under same-origin embedding, K3 and all SCC-rendered content are inside the parent platform's TCB.
- **This blocks lock.**

### TF-18-03 — TH-14: cross-instance approval replay

1. **Does §16 bind approval to an instance?** No. The §16.5 digest has no instance field.
2. **Nonce scope:** host-local. The nonce is checked against that host's K8.
3. **Can two instances anchor the same key?** Yes. §17.9 has local root add anchors on each host, and nothing forbids reusing a key. An administrator managing several servers will do this naturally.
4. **Possible in v1?** Yes, when all of these hold:
   - K4 on host B is compromised;
   - the attacker obtains evidence from host A (evidence is not secret; K4 on A carries it and C can read K8);
   - host B's canonical request matches exactly: declaration, parameters, resources, `expected_state`, `plan_digest` (opaque), and a deadline still valid.

   Identical fleet configurations make an exact match plausible.
5. **Is SR-07 a §22 operational constraint?** Yes. It constrains anchor provisioning. **K6 cannot verify it.** The anchor holds no cross-host information.
6. **Optional or required?** It is required **only if** SC-03 is to hold without qualification for deployments that share approver keys. Otherwise it is optional, and SC-03 must carry an SR-07 precondition.
7. **Cleanest fix:** add instance binding to the digest. This needs a stable K6 instance identity (a new lifecycle item for §22) and a §16.5 interface change. Alternatives:
   - K6-issued challenge nonces: needs a new K6 Operation and K6 state, so a larger amendment;
   - putting the instance ID inside the Plan: useless against a compromised K4, because `plan_digest` is opaque to K6 (the candidate states this correctly).
8. **Does single-host v1 make it irrelevant?** No. "Single-host" describes SCC's management scope. It says nothing about how approver keys are distributed.

**Disposition:** **owner decision** (ODF-18-02). Options: an optional §16 amendment (instance binding), or SR-07 plus a scoped SC-03.

### TF-18-04 — TH-21 / SR-08 / OD-2: an R4 scope entry missing `approval_required`

- **Who declares R4:** the Integration, in K11 (§17.5.3 (e)).
- **Who determines effective risk:** K4. It takes the maximum of the declared tier, the tier derived from criteria (a)/(b) in K11, and any local raise.
- **Who sets `approval_required`:** the declaration author (release), under the A-23 authoring rule.
- **Is it only authoring metadata?** From K6's point of view, yes: K6 obeys the flag without checking that it is consistent.
- **Can it be omitted?** Yes, by accident or on purpose. A malicious author can also omit `executable_semantics`, so a check keyed on `executable_semantics` protects only against *accidental* omission.
  - **Criterion (b)** (package-family WRITE) is intrinsic to `op_id`. A mechanical check on it is **robust against accidental and careless authoring**.
  - **Criterion (e)** (declared tier) is checkable if the tier is present in the signed declaration.
  - **Criterion (c)** is semantic and cannot be mechanically derived.
  - **Local raises** live in K7 and can never be enforced by K6.
- **Does a K6 check make K6 an authorization engine?** No. It evaluates no principal, Grant, role or condition. It is a load-time well-formedness check on signed data, exactly like X-10. It enforces an invariant (A-23) that §17 already imposes.

**Disposition:**
- **Authoring rule:** A-23. Already locked.
- **Release validation:** mechanically check (a)/(b)/(e) before signing. **Downstream §22. Required.**
- **K6 execution invariant:** reject at load any declaration where a package-family WRITE, an `executable_semantics` WRITE, or an entry for a declared-R4 capability lacks `approval_required`. **Optional §16 amendment**, recommended for (b).
- **Authorization policy:** unchanged.

### TF-18-05 — TH-29 / OD-5: tenant-writable declared resources

- **What §16 means by a declared resource:** a named host object resolved from K11 patterns (§16.2). X-13 forbids escaping the declared root, including through symlinks and special files. **Ownership is not checked.**
- **READ:** a tenant can place content inside the declared root, or, where the OS allows hardlinks to files it doesn't own, link other files there *(model analysis: many distributions restrict this by default — verify)*. That content is disclosed to **C/I**, not to the tenant. The effect is to widen what a compromised K4 or K5 can learn. With `METADATA_ONLY` or `DIGEST_ONLY` exposure the risk is negligible. With `FULL` exposure the risk is disclosure across the identity boundary.
- **WRITE:** a root atomic commit into a directory whose components the tenant controls can be redirected by racing directory replacement. X-13's "no escape" arguably forbids the outcome, but **the contract does not require that path components be root-owned**, while it does require that for executables (§16.2.2). The effect is a root write to an attacker-chosen location. **This is privilege escalation.**
- **Is tenant-writable necessarily unsafe?** READ with restricted exposure: no. WRITE: yes, in practice.

**Disposition:**
- **§18 authoring rule:** WRITE resources MUST NOT be declared where any path component is writable by a non-root identity. READ resources in such locations MUST NOT use `FULL` exposure.
- **Optional §16 amendment (recommended for WRITE):** K6 verifies path-component ownership at resolution, mirroring the rule for executable paths.

### TF-18-06 — TH-30 / SR-09: credential-derived values in process arguments

- **Does §16 permit handles in argument slots?** Yes (§16.1.5).
- **When is the handle resolved?** At invocation (§16.8). The invoked program receives the value as an argument.
- **Can an unprivileged local user read it?** *(Model analysis — verify per Host Environment:)* on common Linux defaults, process arguments are readable by all local users unless process-information hiding is configured. Some hosting-oriented distributions enable that hiding. So exposure **depends on the Host Environment**. The threat is architectural (the contract permits the channel), and its severity depends on the host.
- **Is forbidding it too broad?** Possibly. Some product CLIs accept secrets only as arguments. A blanket ban makes those profiles unsupportable.

**Disposition:** **owner decision** (ODF-18-04). Options:
- (a) a K11 authoring ban on credential-derived argument slots;
- (b) a §16 amendment making that ban a Global Execution Policy load-time check;
- (c) permit argument delivery only where the Host Environment asserts process-argument confidentiality (a §12 compatibility condition).

SR-09's second clause (transformed echoes in output) is sound as an authoring rule.

### TF-18-07 — Plan digest and K6: what is and is not guaranteed

- **§17** does not require K6 to understand Plan identity (§17.19, A-26).
- **§16** makes `plan_digest` opaque, and uses it only as an input to the approval digest (§16.3, §16.5).

**Guaranteed at K6** (while K6 and K11 are intact):
- each executed approval-required request is exactly a request that an anchored approver signed, carrying the `plan_digest` *value* the approver saw;
- it executes at most once on this instance, before its deadline.

**Not guaranteed at K6, at any tier:**
- that the Plan is **complete** (no approved step skipped);
- that it is **exclusive** (no extra in-scope non-R4 steps added under the same, or any, `authorization_ref`);
- that steps run in **order**, except where `expected_state` happens to force an order;
- that the `plan_digest` corresponds to any real Plan.

A compromised K4 can execute an approved R4 request without the non-R4 steps the approver assumed would accompany it (such as a backup or a restart), and can add in-scope R2/R3 steps.

**Is this intentional?** Yes. It follows from §17's per-request approval model, §17.21, and K6 being policy-free. Making K6 enforce Plans would require K6 to hold Plan state and sequencing semantics, which contradicts §16's policy-free boundary and the one-request-one-Operation principle (X-05).

**Disposition:** **accepted residual risk.** Add it as an explicit RR. Correct SP-05. Add a claim: "Approval binds requests, not Plans." Add a §22 requirement that the approval tool state this to the approver.

### TF-18-08 — TH-06: K3 request substitution

- **What K2 signs:** identity, audience and freshness (§15.10 P2). **Not request content.**
- **What K3 can modify:** the request, which K3 relays separately from the assertion.
- **Possible under §15?** Yes. §15.6 already accepts it ("a compromised K3 can only send K4 requests K4 would accept from the authenticated user anyway").
- **Does REAUTH help?** No: the assertion is fresh.
- **Does R4 approval help?** Yes: the approver sees the canonical request.
- **Request-bound assertions:** possible only where K2 relays requests. This is an adapter contract matter and **needs no §15 amendment**.

**Disposition:** an **accepted §15 residual risk**, which §18 quantifies. Adapter option: ODF-18-06. Correct the candidate's "Gap" label (CF-18-13).

### TF-18-09 — NEW: K8 record displacement by volume

A compromised K4, or users generating legitimate traffic, can issue high volumes of READ requests. If K8 retention (§19) evicts records by size or age, older records, including evidence, are pushed out. X-29 addresses only an *unwritable* journal.

**Disposition:** **downstream §19.** Retention must not evict unexported records under pressure, or must fail closed first. SC-09 must be weakened (CLF-18-03).

### TF-18-10 — NEW: Platform Services writes and the `executable_semantics` definition

- **§16.2 definition:** content that can cause the **Security System** to execute commands.
- **§17 criterion (c):** host *access control* only.

Platform Services WRITE entries can target parent-platform configuration. The platform is root-equivalent, and its configuration may be code-like or code-invoking. Such entries fall outside both definitions. Unless the author flags them anyway, they are R3 and not `approval_required`. A compromised K4 (identity C, non-root) can then escalate to root through platform configuration. **That breaks the §17.21 picture of a compromised K4 as bounded and non-root.**

A related point applies to any WRITE whose consumer interpolates values into commands (for example, jail parameters substituted into action commands). *(Model analysis — verify per product.)* That too comes down to how carefully `executable_semantics` is classified.

**Disposition:** **owner decision** (ODF-18-09).
- Interim: a §18 authoring rule. Authors may flag more strictly than §16 requires, so this is coherent without an amendment.
- Clean fix: amend §16.2's definition to "content consumed by any root-equivalent or command-executing component".

Also add a residual-risk entry: the compromised-K4 bound is only as strong as the accuracy of `executable_semantics` classification.

---

## 8. Threat Completeness Findings

| ID | Threat | SCC-specific path | Classification |
|---|---|---|---|
| TF-18-02 | Compromised K3 → platform origin | See §7 | §15 amendment / ODF-18-01 |
| TF-18-09 | K8 displacement by volume | See §7 | §19 |
| TF-18-10 | Platform-configuration writes escalate a compromised K4 | See §7 | ODF-18-09 |
| TF-18-11 | **Anchor injection / approval attribution laundering.** Root or a compromised K6 adds an anchor naming Principal P, then produces "approved" K8 entries that verify against that anchor. | Root controls the anchor set (§17.9) | Accepted under RR-03. Needs a **claim correction** (CLF-18-05). **Downstream §19/§21/§22:** keep an off-host record of legitimate anchors. |
| TF-18-12 | **Approval volume / fatigue.** Large R4 Plans need many per-request signatures, which encourages rubber-stamping. | §17.8 is per request | Accepted residual risk. Presentation of multiple requests belongs to §22. Not architecture. |
| — | Stale signed declarations | TH-24 already covers this | — |
| — | Target / resource substitution | TH-42 and X-14 cover this | — |
| — | Honest-root restore rollback | TH-32 (mapping fix CF-18-15) | — |
| — | Self-approval abuse | TH-10 | — |
| — | Cross-component confusion (K4 using another declaration's scope) | Already inside RR-01 (§16.3: `integration_id` partially trusted) | — |

No other threat with a meaningful SCC-specific path was found missing.

---

## 9. Threat-ID / Cross-Reference Audit

| Namespace | Result |
|---|---|
| T-A* | T-A1…T-A13 contiguous. T-A9's scope is wrong (CF-18-01). |
| SP-* | SP-01…SP-25 contiguous. SP-05's enforcer is wrong (CF-18-06). SP-09 is never referenced by a threat (minor). |
| B-* | **B-04 missing** (CF-18-08). |
| TH-* | TH-01…TH-42 contiguous in the matrix. **TH-01 missing from the taxonomy.** TH-21, 30 and 34 each appear in two categories (CF-18-09). |
| SC-* | SC-01…SC-19 contiguous. References correct except for strength (see §10). |
| RR-* | RR-01…RR-13 contiguous. TH-32 → RR-03 is a mismatch (CF-18-15). The Plan-level residual (TF-18-07) and TF-18-10 have no entries. |
| SR-* | SR-01…SR-25 contiguous. SR-08 is a compound requirement (CF-18-11). SR-02/03/04 are redundant (G). |
| T-18-* | T-18-01…T-18-17 contiguous. §18.14 cites T-18-10 for the T-18-09 rule (CF-18-10). |
| TQ-* | TQ-01…TQ-10 contiguous. Mapping TQ-05↔SR-18 and TQ-06↔OD-4 is correct. |
| OD-* | OD-1…OD-5 ↔ SR-19…SR-23 is correct. |

---

## 10. Security Claim Audit

| Claim | Verdict | Finding |
|---|---|---|
| SC-01 | **Weaken slightly** | CLF-18-08. Add "no root-equivalent compromise" to the preconditions. Root can write K7 directly. |
| SC-02 | Correct | — |
| SC-03 | **Weaken** | CLF-18-01. Add preconditions: SR-07 (or OD-1); anchor-set integrity; correct `executable_semantics` classification (TF-18-10). |
| SC-04 | Correct | — |
| SC-05 | Correct (already conditional) | — |
| SC-06 | Correct | — |
| SC-07 | Correct | — |
| SC-08 | Mostly correct | CLF-18-02. Add "credential-derived values are not delivered through channels observable by other identities (ODF-18-04)". That precondition concerns tenants, not K4. The claim as written is about K4, so it is acceptable, but note the scope. |
| SC-09 | **Weaken** | CLF-18-03. "Cannot directly alter or erase." It may displace records through volume unless §19 prevents it (TF-18-09). |
| SC-10 | Correct | Precondition "OS isolation intact" is sufficient. It correctly makes no claim about sibling workers. |
| SC-11 | Correct | — |
| SC-12 | **Overclaim** | CLF-18-05. A valid signature proves that *a key anchored at verification time* signed. Attribution to a Principal holds only if the anchor set was legitimate, which is root-controlled. Restate the claim with that precondition and TF-18-11. |
| SC-13 | Correct | "Fail rather than lie" is stated. |
| SC-14 | Correct | — |
| SC-15 | Correct | — |
| SC-16 | **Incomplete preconditions** | CLF-18-06. Add "K3 / Presentation Adapter not compromised" and "the origin model per ODF-18-01". |
| SC-17 | Correct but vague | CLF-18-07. Tamper evidence against the *writer* requires anchoring outside the writer's control. Make that explicit. |
| SC-18 | Correct for key secrecy | CLF-18-04. Add: "Attribution of approvals still depends on anchor-set integrity." |
| SC-19 | Correct | Consider extending: "…nor the integrity of SCC components or records on the host." |

**New claim required (from TF-18-07):** *"Approval binds individual K6 requests, not Plans. Plan completeness, exclusivity and ordering are guaranteed only by an intact K4."*

---

## 11. Residual Risk Audit

| RR | Verdict | Finding |
|---|---|---|
| RR-01 | Residual; accepted by §17.21 | — |
| RR-02 | Residual; accepted | — |
| RR-03 | Residual; accepted | Should explicitly include anchor injection (TF-18-11) |
| RR-04 | Residual; accepted | — |
| RR-05 | Residual; accepted | — |
| RR-06 | **Already accepted in §15.6** | RF-18-01. Relabel as a §15-accepted residual risk. |
| RR-07 | **Not purely residual** | RF-18-02. Depends on the owner decision (ODF-18-02). |
| RR-08 | Combines two threats | RF-18-03. Split into TH-29 (authoring rule, optional amendment) and TH-30 (owner decision, ODF-18-04). |
| RR-09 | Residual; accepted by §15.8 | — |
| RR-10 | Accepted (Owner Decision 1) | — |
| RR-11 | Partly downstream (§22) | Correct |
| RR-12 | Residual after release validation | RF-18-04. Also covers the TF-18-10 classification gap. |
| RR-13 | Downstream (§19) | Also covers TF-18-09. |
| *(missing)* | **Plan-level integrity depends on K4** | RF-18-05. Add it (TF-18-07). |
| *(missing)* | **SCC as a path into the platform via the presentation origin** | RF-18-06. Add it, pending ODF-18-01. |

---

## 12. Security Requirement Audit

Classes (from the brief): A = MUST lock in §18 · B = downstream · C = implementation guidance · D = owner decision · E = possible §16 amendment · F = possible §15 amendment · G = redundant · H = overreach.

| SR | Class | Finding |
|---|---|---|
| SR-01 | **A** (+ B for mechanism; **F** via ODF-18-01) | SRF-18-01. Keep. Origin dependency is noted. |
| SR-02 / 03 / 04 | **G** | SRF-18-02. Redundant with A-03/A-04, A-10/X-06 and T-12. Keep as cross-references, or delete. |
| SR-05 | **A** | — |
| SR-06 | **A** (claim discipline) + B (§22 mechanics) | — |
| SR-07 | **D** (alternative: E) | SRF-18-03. Enforcement belongs to §22 anchor provisioning. |
| SR-08 | Split: (i) tenant-writable rule = **A** (+ E optional); (ii) `approval_required` release review = **B** (§22 release validation); its MUST is **G** (A-23) | SRF-18-04 |
| SR-09 | Argument clause = **D** (+ E); transformed-echo clause = **A** (authoring) | SRF-18-05 |
| SR-10 | **B** (§20/§21) | — |
| SR-11 | **C** | — |
| SR-12 | **B** (§19/§21), with **scope correction** | SRF-18-06. Tamper evidence produced by the writer is meaningless against that writer. |
| SR-13 | **D** + B | SRF-18-07. Whether off-host export is a v1 requirement is an owner decision (ODF-18-07). |
| SR-14 | **B** (§19) | — |
| SR-15 | **B** (§22) | — |
| SR-16 | **B** (§19 / Recovery) | — |
| SR-17 | **B** (§19). Extend to cover volume displacement (TF-18-09). | SRF-18-08 |
| SR-18 | **D** / B (adapter) | — |
| SR-19…SR-23 | **E** (optional) | See §16 of this review |
| SR-24 / 25 | Deferred | — |
| *(new)* | **A** interim / **E** clean fix: platform-configuration and command-consuming writes flagged `executable_semantics` + `approval_required` (TF-18-10) | SRF-18-09 |
| *(new)* | **B** (§22): the approval tool states that approval binds requests, not Plans (TF-18-07) | SRF-18-10 |
| *(new)* | **B** (§19/§21/§22): off-host record of legitimate anchors, for attribution (TF-18-11) | SRF-18-11 |

No SR amounts to an attempt to rewrite §15 or §16 through the back door. The one requirement that touches §15 (SR-01 via the origin model) is surfaced as an explicit owner decision.

---

## 13. Normative Invariant Audit

| Invariant | Genuine? | Already covered elsewhere? | Owner correct? | Finding |
|---|---|---|---|---|
| T-18-01 | Yes | No | Yes | Keep. Depends on ODF-18-01. |
| T-18-02 | Yes (claim discipline) | No | Yes | Keep |
| T-18-03 | Yes | Duplicates SR-05 (acceptable: the invariant form of the requirement) | Yes | Keep |
| T-18-04 | Yes | — | Yes | Could merge with T-18-17 |
| T-18-05 | Conditional | — | §22 | Pending ODF-18-02 |
| T-18-06 | Yes. Refines A-22. | Partly A-22 | §22 | Keep |
| T-18-07 | Conditional | — | — | Pending ODF-18-04 |
| T-18-08 | Yes | — | — | **CF-18-12:** rewrite as WRITE MUST NOT / READ limited exposure |
| T-18-09 | **Overclaims** | — | §19/§21 | **CF-18-16 / CLF-18-07:** scope tamper evidence to actors who cannot rewrite the anchor, and require the anchor to be outside the writer's control where tamper evidence is claimed |
| T-18-10 | Yes | — | §21 | Fix the §18.14 citation |
| T-18-11 | Yes | — | §19 | Extend to SCC-internal volume (TF-18-09) |
| T-18-12 | Mostly | **Largely T-29** | Recovery | Keep only the broader "no new ability for non-root" clause, or remove |
| T-18-13 | Yes | — | §19 / Recovery | Keep |
| T-18-14 | Yes | — | §22 | Keep |
| T-18-15 | Yes | — | §20/§21/§13 | Keep |
| T-18-16 | Partly | Baseline §13 (freshness visible) and T-30 | — | Keep as the threat-derived form, or note the overlap |
| T-18-17 | Yes (documentation) | — | — | Keep |
| *(new)* | — | — | — | Add: approval binds requests, not Plans (TF-18-07) |
| *(new)* | — | — | — | Add the TF-18-10 authoring invariant (interim) |

None of these prescribes an implementation mechanism, except SR-12's "monotonic sequence". That is acceptable at the §21 level.

---

## 14. Open Question Audit

| TQ | Genuine? | Blocks §18? | Finding |
|---|---|---|---|
| TQ-01 | Yes (§22) | No (blocks R4 enablement) | Keep. Link to ODF-18-08. |
| TQ-02 | Yes (Recovery) | No | Keep |
| TQ-03 | Yes (Adapter) | No | Keep |
| TQ-04 | Yes (§19/§21) | No | Keep. Scope per CLF-18-07. |
| TQ-05 | Yes, but the residual is already §15-accepted | No | Relabel (TF-18-08) |
| TQ-06 | Yes (§22) | No | Keep |
| TQ-07 | Yes (approval usability with security relevance) | No | Keep |
| TQ-08 | Yes | No | Keep |
| TQ-09 | Yes | No | Extend to volume displacement |
| TQ-10 | **Understated** | **Yes**, through ODF-18-01 | CF-18-17. Elevate the origin model to an owner decision. What remains in TQ-10 is the mechanism only. |
| *(new)* | Platform-configuration write classification | No, with the interim rule | Covered by ODF-18-09 |

No artificial open questions were found.

---

## 15. Owner Decisions Required

### Owner Decisions Required Before §18 Lock

**ODF-18-01 — Presentation origin model (BLOCKS LOCK)**
- **Decision:** does SCC-served content run in the parent platform's origin or session?
- **Why it matters:** §15.6's bound on a compromised K3, SC-16, and the escalation path from T-A1 to root through observed data.
- **Options:**

| Option | What it means | Security consequence | §15 change |
|---|---|---|---|
| (a) | Require origin isolation of SCC content from the parent platform | The §15.6 bound holds. SR-01 becomes defence in depth. It may constrain "native" presentation (§13.55), and its feasibility must be verified per platform. | Amend OQ-1 with a constraint |
| (b) | Accept same-origin embedding | K3, the Presentation Adapter, and all rendered observed data join the platform TCB. SR-01 becomes critical. K3's compromise radius becomes root-equivalent. | Correct §15.6 |
| (c) | Per-adapter choice with a declared TCB consequence | Same as (a) or (b) per adapter | Amend §15 to say so |

- **Affects:** §15 yes; §16 no; §17 no (A-22 is already outside K3).
- **Architectural-consistency recommendation:** (a) where feasible, because it keeps §15.6's stated bound true. Otherwise (c), with explicit disclosure of the TCB consequence.

**ODF-18-02 — Cross-instance approval replay (does not block)**
- **Options:**
  - (a) §16 amendment binding an instance identity into the digest. The replay closes, and a lifecycle item for instance identity is needed.
  - (b) SR-07 operational rule plus a scoped SC-03. It cannot be verified by K6. Residual RR-07 remains wherever the rule is violated.
  - (c) Accept the risk.
- **Affects:** §16 under (a); §22 under (b).
- **Recommendation:** (a) for consistency with SC-03 being the central compromised-K4 claim. (b) is coherent for v1 if SC-03 is scoped.

**ODF-18-03 — K6 enforcement of R4 `approval_required` (does not block)**
- **Options:**
  - (a) release validation only (§22);
  - (b) also a K6 load-time invariant for criteria (a)/(b)/(e) (optional §16 amendment, analogous to X-10).
- **Consequence:** (b) catches bad declarations even if release tooling fails. Neither option stops a malicious release author.
- **Recommendation:** (a) is required. (b) is recommended at least for criterion (b).

**ODF-18-04 — Credential-derived argument slots (does not block)**
- **Options:**
  - (a) authoring ban;
  - (b) §16 load-time ban;
  - (c) permit only on Host Environments with process-argument confidentiality.
- **Consequence:** (a)/(b) may make some products unsupportable. (c) moves the check into §12 compatibility.
- **Recommendation:** (b) or (c). Pure (a) relies on authoring discipline alone.

**ODF-18-05 — Resource ownership for WRITE (does not block)**
- **Options:**
  - (a) authoring rule only;
  - (b) §16 amendment: K6 verifies path-component ownership for WRITE resources.
- **Recommendation:** (b), because it mirrors the existing executable-path rule. (a) is the interim.

**ODF-18-06 — Request-bound assertions (does not block)**
- **Options:**
  - (a) mandatory where K2 relays requests;
  - (b) optional;
  - (c) not pursued.
- **Affects:** Adapter contract only. The residual risk is already §15-accepted.
- **Recommendation:** (a) where feasible. It interacts with ODF-18-01.

**ODF-18-07 — Off-host audit export in v1 (does not block)**
- **Options:**
  - (a) required;
  - (b) supported but optional;
  - (c) deferred.
- **Consequence:** without export, no audit or attribution property survives root compromise. SC-17 is empty in practice.
- **Affects:** §19/§21.
- **Recommendation:** at least (b), with RR-03 disclosed.

**ODF-18-08 — Minimum approval-key custody class for v1 (does not block lock; blocks R4 enablement)**
- **Options:**
  - Case A allowed, with claims restricted per SR-06;
  - Case C required.
- **Consequence:** under Case A, R4 resists only non-root SCC compromise.
- **Recommendation:** allow Case A, with SR-06 claim discipline enforced in documentation. That is consistent with Owner Decision 2's usability impact.

**ODF-18-09 — Classification of platform-configuration writes (does not block with the interim rule)**
- **Options:**
  - (a) §18 authoring rule: flag such writes `executable_semantics` + `approval_required`;
  - (b) amend the §16.2 definition to cover any root-equivalent or command-executing consumer;
  - (c) add an R4 criterion to §17. §17 is locked, so this would reopen it.
- **Recommendation:** (a) now, and (b) as the clean fix. Avoid (c).

---

## 16. Required §16 Amendments

| Issue | §16 amendment? | Required or optional? | Why |
|---|---|---|---|
| Cross-instance approval replay (TF-18-03) | Yes, if option (a) | **Optional** (owner decision) | SR-07 provides a coherent interim, if SC-03 is scoped |
| R4 `approval_required` consistency (TF-18-04) | Yes, if option (b) | **Optional** | Release validation meets the A-23 intent. The K6 check adds defence in depth and is not authorization. |
| Credential-derived argument slots (TF-18-06) | Yes, if option (b) | **Optional** | The authoring or Host Environment alternatives are coherent |
| Declaration rollback (TH-24 / OD-4) | Yes, if adopted | **Optional** | §22 update-channel monotonicity is the primary control |
| WRITE path-component ownership (TF-18-05) | Yes, if option (b) | **Optional (recommended)** | X-13's outcome requirement exists, but ownership is unspecified |
| `executable_semantics` definition scope (TF-18-10) | Yes, if option (b) | **Optional (recommended clarification)** | The interim authoring rule is permitted, because flagging more strictly is allowed |

**Verdict: no §16 amendment is required for §18 to be coherent.** All six have coherent interim positions.

---

## 17. Required §15 Amendments

| Issue | Amendment | Required? | Why |
|---|---|---|---|
| Presentation origin / K3 compromise bound (TF-18-02) | Constrain OQ-1 (option a), or correct §15.6 (option b), or declare per-adapter TCB (option c) | **Required** | §15.6's bound, and OQ-1's "both options satisfy §15", are false under same-origin embedding. §18 cannot state a consistent K3 boundary until this is resolved. |
| K4 egress (CF-18-04) | Optional: promote §15.4 item 6 to a T-invariant | Optional | §18 can instead cite the prose and weaken its claim |

---

## 18. Downstream Requirements

| Finding | Destination | Blocks §18? | Why |
|---|---|---|---|
| SR-01 mechanism | Presentation / Platform Adapter gate | No (the origin model does, via ODF-18-01) | Mechanism is out of scope for §18 |
| SR-07 anchor provisioning | §22 | No | Operational rule |
| Release validation of R4 flags | §22 | No | TF-18-04 |
| Approval tool: identifiers, request-vs-Plan statement, handling many requests | §22 | No | T-18-06, SRF-18-10, TF-18-12 |
| Tamper evidence, sequence, export | §19/§21 | No | SRF-18-06/07 |
| Retention that cannot displace unexported records | §19 | No | TF-18-09 |
| K8 capacity isolation | §19 | No | SR-17 |
| Full approval evidence retained | §19 | No | SR-14 |
| Off-host record of legitimate anchors | §19/§21/§22 | No | TF-18-11 |
| Restore rollback detection | §19 / Recovery | No | SR-16 |
| Rollback-safe updates, release-key custody | §22 | No | SR-15 |
| Generic evidence vs interpretation | §20/§21 | No | SR-10 |
| Same-identity worker hardening | Implementation gate | No | SR-11 |
| Request-bound assertions | Platform Adapter gate | No | ODF-18-06 |
| Process-argument confidentiality as a Host Environment fact | §12 / Platform Adapter | No | ODF-18-04 option (c) |
| Origin model | **§15 amendment** | **Yes** | ODF-18-01 |

---

## 19. Accepted Residual Risks

These remain accepted after this review:
- **RR-01** compromised K4, including Plan-level integrity (RF-18-05);
- **RR-02** compromised K6;
- **RR-03** root / K11, including anchor injection;
- **RR-04** compromised platform;
- **RR-05** stolen session;
- **RR-06** K3 substitution (already §15-accepted);
- **RR-09** shared K5 identity (§15.8);
- **RR-10** self-approving administrator (Owner Decision 1);
- **RR-11** supply chain;
- **RR-12** authoring accuracy of `approval_required` and `executable_semantics`;
- **RR-13** exhaustion causing loss of observation;
- approval fatigue (TF-18-12).

RR-07 and RR-08 stay residual only if the owner chooses the non-amendment options in ODF-18-02 and ODF-18-04.

---

## 20. Recommended Corrections to Candidate §18

| # | Correction | Source |
|---|---|---|
| RC-01 | Move K3 out of T-A9 | CF-18-01 |
| RC-02 | Fix the "left of B-07" statement | CF-18-02 |
| RC-03 | Remove K10 as a K11 modifier | CF-18-05 |
| RC-04 | Change the SP-05 enforcer to K4, with K6 enforcing request integrity only | CF-18-06 |
| RC-05 | Fix the B-04 gap | CF-18-08 |
| RC-06 | Add TH-01 to the taxonomy; mark multi-category threats | CF-18-09 |
| RC-07 | Fix the T-18-09/T-18-10 citation in §18.14 | CF-18-10 |
| RC-08 | Split SR-08 | CF-18-11 |
| RC-09 | Rewrite T-18-08 | CF-18-12 |
| RC-10 | Relabel TH-06/RR-06 as §15-accepted | CF-18-13 |
| RC-11 | Correct the Gate Assessment's "no locked-gate changes" statement | CF-18-14 |
| RC-12 | Remap TH-32 | CF-18-15 |
| RC-13 | Scope T-18-09 / SR-12 tamper evidence | CLF-18-07 |
| RC-14 | Weaken SC-01, SC-03, SC-09, SC-12, SC-16 and SC-18 as audited | CLF-18-01…08 |
| RC-15 | Add the claim "approval binds requests, not Plans", and residual risk RF-18-05 | TF-18-07 |
| RC-16 | Add threats TF-18-02, TF-18-09, TF-18-10 and TF-18-11, with matrix rows | §8 of this review |
| RC-17 | Add an SR and invariant for platform-configuration and command-consuming writes (interim) | SRF-18-09 |
| RC-18 | Scope the §17.21 K1/K2 statement to the SCC-interface path | CF-18-07 |
| RC-19 | Re-cite the K4 egress claim to §15.4 prose, or record it as downstream | CF-18-04 |
| RC-20 | Elevate TQ-10's origin question to ODF-18-01 | CF-18-17 |
| RC-21 | Split RR-08; relabel RR-07 as pending an owner decision | RF-18-02/03 |

---

## 21. Proposed Final Gate Disposition

| Dimension | Result |
|---|---|
| Threat-model completeness | **CONDITIONAL.** Three missing threats need adding (TF-18-02, TF-18-09, TF-18-10). |
| §15 compatibility | **CONDITIONAL.** TF-18-02 shows that a §15.6 claim is false under same-origin embedding, so a §15 amendment is required in some form (ODF-18-01). |
| §16 compatibility | **PASS.** No §16 amendment is required. Six optional amendments are identified. |
| §17 compatibility | **PASS.** One scoping clarification (CF-18-07). No conflict. |
| Internal consistency | **CONDITIONAL.** RC-01…RC-21 must be applied. |

**Conflicts:** one. TF-18-02 conflicts with §15.6 and §15.18 OQ-1 under same-origin embedding.

**Blocking owner decision:** ODF-18-01.

**Non-blocking owner decisions:** ODF-18-02…ODF-18-09.

### Proposed disposition

**§18 — CONDITIONAL — OWNER REVIEW REQUIRED**

The path to PASS:
1. The owner decides ODF-18-01 and authorizes the matching §15 amendment.
2. The owner records dispositions for ODF-18-02…ODF-18-09. Choosing the interim, non-amendment option is acceptable for each.
3. The canonical §18 is reissued with RC-01…RC-21 applied.
