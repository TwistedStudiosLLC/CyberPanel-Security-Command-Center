> **Document status:** CONDITIONAL — candidate text (NOT FULLY LOCKED)
> **Authority category:** 4 — Conditional/open architecture (see [Authority Hierarchy](../../README.md#authority-hierarchy))
> **Source:** §18 candidate as submitted at the §18 architecture gate.
> **Normative:** Conditional only. Nothing in this document is locked.
> **Overridden self-assessment:** The candidate's closing Gate Assessment says "§18 — PASS — READY FOR §19". **That
> self-assessment is not current authority.** The [§18 gate review](18-gate-review.md) found the candidate CONDITIONAL,
> and the owner recorded §18 as CONDITIONAL — NOT FULLY LOCKED (DEC-015). Current status: [README](README.md).
> **Known corrections pending:** The gate review lists recommended corrections RC-01 … RC-21 (for example, SP-05's
> enforcer, the K3 actor classification, the missing boundary B-04, the T-18-09/T-18-10 citation). They are **not**
> applied here; this file preserves the candidate as submitted.
> **Transcription notes:** Reproduced verbatim. Removed process-wrapper text only: the opening italic line ("This is
> candidate architecture text for owner approval. … I have not modified or created any files.") and the closing line
> ("I've stopped here and have not started §19.").

# SCC §18 — Threat Model

**Notation.** IDs from earlier gates keep their meanings: §15 T-01…T-31, §16 X-01…X-39, §17 A-01…A-36. This section adds:

| Prefix | Meaning |
|---|---|
| T-A*n* | Threat actors |
| SP-*nn* | Security properties |
| B-*nn* | Trust boundaries |
| TH-*nn* | Threats |
| SC-*nn* | Security claims |
| RR-*nn* | Residual risks |
| SR-*nn* | Security requirements |
| T-18-*nn* | §18 invariants |
| TQ-*nn* | Open questions |

---

## Terms

- **Threat actor:** an entity or a compromised component that can try to violate a security property.
- **Control:** an architectural rule enforced by a specific component.
- **Survival:** whether a control still holds when the component that enforces it, or the attacking component, is compromised. A control enforced by a component **never** survives that component's compromise.
- **Constrains honest X / protects against compromised X:** a rule "constrains honest X" when it limits X only while X follows the rule. It "protects against compromised X" only when a component other than X enforces it.
- **Root-equivalent:** able to act with host root authority. Under §15, K1/K2 (the parent platform), K6, K9/local root and K10 are root-equivalent. A root-equivalent compromise is a **host compromise**.
- **Observed data:** any data that comes from the host or from Security Systems (files, logs, tool output, endpoint responses). It may be controlled by an attacker (§16.7, X-23).
- **Residual risk:** an accepted consequence that remains after all locked controls, stated explicitly.

---

## 18.1 Threat Actors

| ID | Actor | Capability assumed | Root-equivalent? |
|---|---|---|---|
| **T-A1** | Unauthenticated external attacker | Network access to the host. Can put content into observed data (HTTP requests in WAF logs, usernames in auth logs, crafted files that malware scanners read). **SCC-specific:** this indirect channel is the external attacker's most direct path into SCC. | No |
| **T-A2** | Compromised platform identity | A stolen platform session or credential for an enrolled Principal's platform account. | No |
| **T-A3** | Low-privilege HUMAN Principal | Enrolled, with limited Grants. | No |
| **T-A4** | Privileged HUMAN Principal | Operator, administrator or approver, whether malicious, careless or coerced. | No (acts through SCC) |
| **T-A5** | Compromised K4 | Code execution as identity C (§17.21). | No |
| **T-A6** | Compromised K5 host / planner | Code execution as identity I. | No |
| **T-A7** | Compromised K6 | Code execution as root inside the executor. | **Yes** |
| **T-A8** | Compromised or malicious Integration | Malicious code, or code subverted by hostile observed data, running in one K5 worker (identity I). | No |
| **T-A9** | Compromised parent platform (K1/K2, and a compromised K3 relaying for it) | Control of the platform's process. K3 alone is identity W and is not root-equivalent (see B-03). | **Yes** (K1/K2) |
| **T-A10** | Local Root Operator / K9 | Legitimate, careless, malicious or compromised host root. It is **not a Principal** (§17.1.2). | **Yes** |
| **T-A11** | Supply-chain attacker | Can alter SCC releases, the release signing key, Integration declarations, Security System packages, interpreters or dependencies before or during delivery. | Varies |
| **T-A12** | Storage / persistence attacker | Can corrupt, alter, roll back or restore K7 or K8. Realistically this is only root or C, or a restore performed during recovery. | Via root or C |
| **T-A13** | **Local unprivileged host user / hosted-tenant code** *(added)* | Code execution as a non-SCC, non-root identity on the host, for example a compromised website or PHP code, which is typical on a hosting panel. Can create files in tenant-writable locations, read `/proc` subject to OS policy, and consume shared resources. | No |

**Why T-A13 is added.** On hosting-panel servers this is the most likely local foothold. None of T-A1 to T-A12 covers it, and it attacks SCC boundaries directly: IPC channels, declared resources, `/proc` and disk space.

---

## 18.2 Security Properties

| ID | Property | Type | Definition in SCC | Primary enforcer |
|---|---|---|---|---|
| SP-01 | Authentication integrity | Authenticity | A HUMAN identity used by K4 comes only from a K4-verified K2 assertion | K1/K2 (issue), K4 (verify) |
| SP-02 | Principal identity integrity | Integrity | `principal_id` ↔ Binding cannot be substituted or reused | K4 / K7 |
| SP-03 | Authorization integrity | Authorization | An Action proceeds only if Grants, conditions and policy permit it | K4 |
| SP-04 | Grant / Role / Policy integrity | Integrity | Authorization state changes only through authorized, audited K4 actions | K4 / K7 |
| SP-05 | Plan integrity | Integrity | What executes is the Plan that was authorized | K4 (all tiers); K6 through the approval digest (R4 only) |
| SP-06 | Decision integrity / `authorization_ref` binding | Integrity | One Decision covers one Plan and one Job | K4 |
| SP-07 | Approval authenticity | Authenticity | Evidence was produced by an anchored approver key | K6 (verify), approval environment (custody) |
| SP-08 | Approval binding and non-replay | Integrity | Evidence authorizes exactly one request, once, before its deadline | K6 (X-16, X-31) |
| SP-09 | Approval context confidentiality | Confidentiality | Sensitive request content shown for approval is exposed only as §19 permits | Approval environment, §19 |
| SP-10 | K11 integrity | Integrity | Vocabulary, scope, identities, anchors and overlay are what the release and root intended | Root file ownership (T-21), release signature (X-08) |
| SP-11 | Operation scope integrity | Integrity | K6 executes only in-scope, declared Operations | K6 |
| SP-12 | Executable / endpoint identity integrity | Integrity / Authenticity | The code or endpoint invoked is the approved one | K6 (X-34, X-35) |
| SP-13 | Credential confidentiality | Confidentiality | Credential values never leave K6 | K6 (T-18, X-24, X-26) |
| SP-14 | Privileged execution integrity | Integrity | Host effects come only from validated K6 requests | K6 |
| SP-15 | Target / resource binding integrity | Integrity | The object acted on is the declared and expected one | K6 (X-13, X-14), K4 (targets) |
| SP-16 | Job integrity | Integrity | A Job executes exactly its bound Plan | K4 |
| SP-17 | Revocation integrity | Integrity | Revoked authority is not exercised after the next revalidation point | K4 (A-28, A-29), K6 (anchors) |
| SP-18 | Audit integrity / tamper evidence | Accountability / Integrity | Records cannot be altered undetectably | K4 (K7 audit), K6 (K8); off-host export if used |
| SP-19 | Audit completeness | Accountability | Every relevant event has a record | K4, K6 |
| SP-20 | Fail-closed behavior | Authorization | Uncertain authorization or journaling leads to refusal | K4 (A-32), K6 (X-29) |
| SP-21 | Availability of observation | Availability | Security Systems stay observed, or are clearly marked stale | K4, K5, K6, K8 |
| SP-22 | Availability of action | Availability | Authorized actions can execute | K4, K6, approval environment |
| SP-23 | Recovery integrity | Integrity / Authorization | Recovery creates no web-reachable bypass (T-29) | Recovery gate / K9 |
| SP-24 | Supply-chain integrity | Integrity / Authenticity | SCC code, declarations and invoked executables are genuine | Release process, K11, K6 |
| SP-25 | Presentation integrity *(added)* | Integrity | Content shown to users cannot execute in, or alter, the user's platform session | K3 / Presentation Adapter |

---

## 18.3 Trust Boundaries

```
 [T-A1 Internet] ──B-01──▶ [K1 Parent Platform ▸ K2 Bridge] ──B-02──▶ [K3 Gateway (W)] ──B-03──▶ [K4 Core (C)]
                                (root-equivalent; identity TCB)                                        │  ▲
                                                                                               B-05    │  │ B-06
                                                                                                       ▼  │
                                                                                   [K5 Integration Host (I)]
                                                         B-07 (K4→K6, peer = C only)
 [K4] ─────────────────────────────────────────────────▶ [K6 Executor (root)] ──B-08──▶ [Host / Security Systems]
                                                              ▲         │                          │
                                               B-09 (reads)   │         └──B-10──▶ [K8 Journal]    │ B-11 observed data
                                                 [K11 Install Tree (root-owned)]                   ▼ (untrusted, flows back
                                                                                                       via K6→K4→K5→K3→Browser)
 [K9 / Local Root] ──B-12── (outside SCC boundary: controls K6, K10, K11, K7, K8, host)

 APPROVAL PATH (distinct):
 [Approver] ──B-13──▶ [Independent Approval Environment + key] ──(signature only)──▶ K4 (carrier) ──▶ K6 (verifier, B-14)
 [T-A13 Local tenant] ── attacks B-07/B-03/B-05 channels, declared resources (B-08), /proc, disk
```

| ID | Boundary | Authentication | Authorization | Privilege | Integrity | Credential | Administrative |
|---|---|---|---|---|---|---|---|
| B-01 | Internet → platform | ● (platform login) | | | | | |
| B-02 | K1/K2 → K3 | ● (assertion issued) | | | | | |
| B-03 | K3 → K4 | ● (K4 verifies the assertion end-to-end) | ● (K4 decides) | | ● (K4 revalidates input) | | |
| B-05 / B-06 | K4 ↔ K5 | ● (launcher-bound identity) | ● (K4 checks scope and authorization) | | ● (K5 output is untrusted) | | |
| B-07 | K4 → K6 | ● (peer C) | ◐ (K6 checks presence of the authorization interface only) | ● | ● (§16 validation) | | |
| B-08 | K6 → host | | | ● (root effect) | ● (identity, resolution) | ● (handle use) | |
| B-09 | K11 → K6/K4 | | | | ● (root-owned, release-signed) | | ● |
| B-10 | K6 → K8 | | | | ● | | |
| B-11 | Observed data → SCC | | | | ● (untrusted) | | |
| B-12 | K9 / root ↔ SCC | | | ● | | | ● |
| B-13 | Approver → approval environment | ● (the approver's own control of the key) | | | ● (WYSIWYS) | ● (key custody) | |
| B-14 | Approval evidence → K6 | ● (signature against the anchor) | ◐ (evidence, not policy) | | ● (digest binding) | | |

**Topological fact that governs the whole analysis.** Everything to the left of B-07 is unprivileged. Anything at or below K6, K9, K10 or K11 is root-equivalent. **No SCC control survives a root-equivalent compromise, except information that has already left the host** (off-host approver keys, and exported audit records).

---

## 18.4 Threat Taxonomy

Threats are grouped by what they attack:
- **Identity:** TH-02, 05, 06, 07, 39
- **Authorization:** TH-08, 09, 10, 36
- **Plan/Job:** TH-16, 41, 42
- **Approval:** TH-11, 13, 14, 37, 38
- **Execution:** TH-12, 20, 21, 22, 26, 27
- **Declaration/K11:** TH-21, 23, 24, 25
- **Integration:** TH-03, 17, 18, 19
- **Credentials:** TH-30, 31
- **Local host:** TH-28, 29, 30, 34
- **Presentation:** TH-04
- **Audit:** TH-15, 33
- **Persistence:** TH-32
- **Recovery:** TH-40
- **Availability:** TH-34, 35

The full matrix is in §18.19.

---

## 18.5 Compromised-K4 Analysis (formalizing §17.21)

Each claim below was checked against §16.

**A compromised K4 CAN:**
- forge K4-side authorization state: Principals, Grants, Roles, Decisions, `authorization_ref` values, policy revisions;
- alter or forge K4 audit records in K7;
- request any READ that any loaded Execution Declaration grants, including the Core Discovery Declaration, under any declaration identity (§16.3: `integration_id` is only partially trusted);
- request any WRITE whose scope entry is not `approval_required`;
- change K4-internal SCC state, including R4 `scc.*` administration, without approval;
- misreport state, withhold work, reorder work, or starve Jobs;
- present misleading context to approvers, which WYSIWYS limits (§18.7);
- request cancellation of any in-flight request;
- **use** credentials indirectly through in-scope Operations that reference handles. It cannot read the values (see limits below);
- **replay a valid approval on a different SCC instance that anchors the same approver key** (TH-14). §16 does not prevent this; it is **not** stated in §17.21 and is added here.

**A compromised K4 CANNOT, on its own:**

| Claim | §16 basis | Precise limit |
|---|---|---|
| Escape the Operation vocabulary or K11 scope | X-01, X-04, X-06 | Holds while K6 and K11 are intact |
| Substitute an unapproved executable or endpoint | X-34, X-35 | Covers the executable and interpreter only; **not transitive libraries or modules** (TH-27) |
| Obtain credential values | X-24, X-26 | Scrubbing is **exact-match only**. A profile whose output can contain a *transformed* credential (encoded, partial) defeats it (TH-31) |
| Perform an `approval_required` WRITE without evidence | X-16 | Holds **only for scope entries that are actually flagged**. A declaration authoring error defeats it (TH-21) |
| Reuse a nonce, alter an approved request, exceed its deadline | X-16, X-31 | Holds **per K6 instance** (TH-14) |
| Modify K11 or the anchors | T-21 | Holds (K11 is not writable by C) |
| Erase K8 | T-12, K8 root-owned | Holds (C has read access only) |
| Reach the network directly | §15.4 | Holds. Exfiltration is limited to user-facing channels and in-scope Operations. |

---

## 18.6 K6 Compromise Analysis

K6 is root. **A compromised K6 is a host compromise.**

| Question | Answer |
|---|---|
| Direct access | Everything on the host: files, processes, credentials, K7, K8, K11, other SCC processes |
| Alteration | Anything, including SCC binaries, K11, K7, K8, Security Systems |
| Does K11 protect against it? | **No.** K11 only constrains an honest K6. |
| Credential secrecy | **Lost** for every credential K6 holds |
| K8 | **Lost** from the point of compromise: it can be altered, forged or deleted. Records exported off-host earlier are the only survivors. Past K8 entries that carry approval signatures stay *verifiable* (a compromised K6 cannot forge approver signatures), but they can be **deleted**. |
| Approval evidence | Irrelevant to future actions, because K6 can act without it. Off-host keys are still not exposed: a compromised K6 cannot produce *new* valid approvals. |
| Executable identity | Irrelevant, because K6 runs whatever it likes |
| Host integrity | Lost |
| Protections outside K6 | Off-host approver keys (stay unforgeable) and off-host audit copies (if exported). **Nothing on the host.** |

**How K6 could come to be compromised** (the reason K6 must be kept small):
- (a) malformed requests from C;
- (b) hostile observed data during mechanical framing (X-23 keeps interpretation out of K6);
- (c) hostile output from invoked tools;
- (d) supply chain (TH-25, TH-27).

§16 already minimizes (a) to (c). This analysis adds no component.

---

## 18.7 Approval Threat Model

### 18.7.1 Key custody

| Resists compromise of → | **Case A:** key on SCC host (root-only permissions; tool runs as root through a K9-style path) | **Case B:** key on parent platform / in K1/K2 | **Case C:** key off-host, in an independent environment |
|---|---|---|---|
| K3 (W) | Yes | Yes | Yes |
| K4 (C) | Yes | Yes | Yes |
| K5 (I), T-A13 tenant | Yes | Yes | Yes |
| K1/K2 / parent platform (root-equivalent) | **No**: key theft | **No**: direct theft | Key: **yes**. Host integrity: **no** (the platform can act as root without SCC). |
| Host root / K6 / K9 compromise | **No** | **No** | Key: **yes**. Host integrity: **no** |
| Cross-host misuse after theft | Key usable on every host that anchors it | Same | Not stealable |

**Precise conclusions**
- **Against a root-equivalent attacker, no custody choice protects host integrity.** Case C protects **the approval property itself**: nobody without the approver can create valid approval evidence. That keeps K8 approval records credible (the attacker can delete them but not forge them) and keeps other hosts safe from forged approvals. This refines §17.9/§17.21 and does not conflict with them (§18.24).
- **Case B adds nothing over REAUTH** against platform compromise, because the platform is the identity TCB. It also places key material in K1/K2 without the protection that A-22 gives the signing tool → **SR-05 prohibits it.**
- **Case A is adequate against all non-root SCC compromise** (K3, K4, K5, tenants). It is **inadequate** against the platform or root.

### 18.7.2 What "independent" requires (SR-06)

An approval environment resists K1–K4, platform and root compromise only if **all** of the following hold:
1. **Key material is never present** on the SCC host or on the parent platform, and cannot be exported to them.
2. **No shared administrative control.** The environment cannot be administered or updated with credentials available on the SCC host or the platform.
3. **Only the signature leaves.** Its only input from SCC is the canonical request, and its only output is a signature. It follows no instructions from SCC.
4. **Display is independently derived (WYSIWYS).** What it shows comes only from the canonical content. Identifiers such as `integration_id`, `capability_id`, `op_id` and `resource_ref` are interpreted using **release-signed K11 declarations that the environment verifies itself**, never mappings supplied by K4.
5. **It never trusts K4's description of the request.**

Being off-host does not satisfy these requirements by itself. For example, an off-host tool fed and rendered by K4 violates items 4 and 5.

### 18.7.3 Approval tool threats

| Threat | Control | Residual |
|---|---|---|
| Malicious or misleading display | WYSIWYS (A-22, SR-06 item 4) | Human misjudgment of accurately displayed content. `file.replace` shows new content, but the approver cannot see a diff unless they obtain the pre-image by other means (pre-image content is not in the digest). |
| Altered digest; parameter, target or resource substitution | K6 recomputes the digest from the actual request (X-16) | None, while K6 is intact |
| Replay or nonce reuse on the same host | X-16, X-31 | None |
| **Replay on another host that anchors the same key** | **None in §16** | **Gap (TH-14):** SR-07 is the interim rule; OD-1 is the possible §16 amendment |
| Theft or forwarding of evidence | Evidence authorizes only one exact request, once, before its deadline | Forwarding is harmless unless the target host shares the anchor (TH-14) |
| Deadline manipulation | The deadline is inside the digest and checked against K6's clock | Clock manipulation needs root (outside the boundary) |
| Signature substitution (a different key) | Anchor check (X-16) | None |

---

## 18.8 K11 Compromise Analysis

**Who can modify K11:** root only (T-21), through K9, lifecycle (§22) or K10. The release process creates its contents. K11 has **two provenance classes**:

| Class | Contents | Protection |
|---|---|---|
| **Release-signed** | Operation Catalogue, Global Execution Policy, declarations (Integration, Platform Services, Core Discovery), release trust anchors | Release signature (X-08) plus root ownership |
| **Host-local, root-authored** | Approver anchor set, Host Restriction Overlay, local package-source changes (if §22 allows them) | **Root ownership only.** The release signature does not cover them. |

| Threat | Result |
|---|---|
| Scope expansion, removal of `approval_required`, malicious executable or endpoint identity, malicious resource or overlay, malicious Core Discovery or Integration declaration **by root** | Undefended by design. Root is outside the boundary. |
| The same attacks **by a release-key holder** (TH-25) | Accepted by K6 as genuine. **Supply-chain residual risk.** Release-key custody belongs to §22. |
| **Rollback** to an older, validly signed declaration set with wider scope, fewer flags or known flaws (TH-24) | **Not prevented by §16.** A signature proves authenticity, not recency. The attack needs root or a compromised update channel. SR-15 assigns it to §22; OD-4 is the possible §16 amendment. |
| Wholesale replacement of trust anchors | Root only. Undefended by design. |
| **Declaration authoring error:** an R4-relevant scope entry is not flagged `approval_required` (TH-21) | K6 would not require approval, and a compromised K4 could then perform that R4 host effect. A-23 is an authoring rule only. OD-2 would make criteria (a) and (b) mechanically enforced by K6. |

---

## 18.9 Integration Threat Model (T-A8, T-A6)

| Attack | Control | Survives the attacking Integration's compromise? | Residual |
|---|---|---|---|
| False discovery or health reports | K4 generic discovery (Core Discovery) does not depend on K5. Raw evidence carries K6 provenance (§16.7). | Yes, for generic inventory. No, for product-specific interpretation. | Product-level health and interpretation can be falsified. This is a detection-integrity risk. |
| False capability declarations | Capabilities come from **K11**, not from the running code (§15.8, X-06) | Yes | None beyond authoring |
| Unauthorized Operation requests, parameter manipulation | K4 checks scope and authorization. K6 re-validates. | Yes | Within scope the Integration can propose harmful but in-scope content (TH-16) |
| Target substitution | K4 resolves targets. `expected_state` is checked at K6. | Yes | — |
| Credential acquisition | K5 holds no credentials (T-19) | Yes | — |
| Bypassing K4 or calling K6 directly | T-06, T-08 | Yes | — |
| Modifying K11 | T-21 | Yes | — |
| **Impersonating or attacking another Integration** | Launcher-bound channel identity (T-16) | **No, in v1.** All workers share identity I (§15.8), so one compromised worker can interfere with sibling workers (including Platform Services), for example through debugging or signalling interfaces the OS allows between processes of the same identity. | **Compromise of one worker ≈ compromise of all K5 workers.** Contained by T-06/T-08/T-19: the attacker still has no host, K6, network or credentials. OS-level restriction of same-identity interference is SR-11 (implementation hardening). Per-Integration identity is §15 OQ-7. |
| Exploiting hostile observed data (T-A1 → K5) | K5 is unprivileged, isolated and has no network | Yes | K5 compromise (see above) |

**Preserved principles:** an Integration's identity is not a Principal's authority (A-06). Declaring a capability confers no privilege (X-06).

---

## 18.10 Plan / Job / Decision Threat Model

| Threat | Honest K4 | Compromised K4 | R4 at K6 |
|---|---|---|---|
| Intent manipulation (an unauthorized Principal gets an Action planned) | Intent Authorization before planning (§17.11) | Bypassable | n/a |
| Plan substitution (K5 plans something other than what was asked) | K4 validates coverage and targets. **Content semantics are not validated** (TH-16). | Bypassable | Approver sees exact content (WYSIWYS) |
| Plan mutation after authorization; step substitution | Digest binding (A-24). Job bound to Plan (A-26). | Bypassable | Digest includes `plan_digest`, parameters and resources (X-16) |
| Digest mismatch | K4 computes it | Bypassable | K6 checks request fields against the signed digest. **K6 does not check `plan_digest` against any Plan** (it is opaque to K6). |
| Decision substitution / `authorization_ref` replay | A-26 | Bypassable | Not detectable by K6 (§17.19) |
| Job substitution | A-26, A-27 | Bypassable | Per-request digest |
| Target substitution / drift | `system_id` resolution fails closed (§17.6) | — | `expected_state` (X-14) at every tier where the Plan supplies it |
| Approval mismatch | K4 pre-check | — | X-16 |
| Revocation race | Per-request revalidation (A-28). **The window is one in-flight request.** Anchor revocation waits for a K11 reload. | — | Deadline bounds it |
| Expiry race | `expires_at` checked per request | — | Deadline checked at validation. A request accepted just before its deadline may run up to `max_duration`. |

**Conclusion:** below R4, Plan/Job/Decision integrity depends entirely on K4. At R4, K6 enforces request-level integrity, but **not** Plan-level integrity, because `plan_digest` is not interpreted by K6.

---

## 18.11 Principal / Grant Threat Model

| Threat | Control | Residual |
|---|---|---|
| Impersonation (T-A2) | Assertion verification (A-01); REAUTH for R2 and above | A valid stolen session with fresh authentication acts as the Principal up to R3 |
| `principal_id` substitution | Only K4 creates or resolves it (A-02) | Compromised K4 |
| Platform subject reuse | Binding lost on absence; a new subject is unenrolled (§17.1.3) | Depends on the adapter's stability declaration (P-6 → TQ-07) |
| Stale binding / binding loss | Freshness rule; held when unconfirmed (§17.1.4) | Window up to the maximum age |
| Automatic enrollment abuse | None exists (A-03, Owner Decision 3) | — |
| Unauthorized enrollment; Grant or Role escalation; forgery | R4 administration (A-17); no self-Grant (A-14) | Compromised K4 bypasses all of these (they are K4-internal). K4 alone verifies approval of K4-internal R4 actions. |
| Last-administrator manipulation | A-15 | Compromised K4; recovery via root (P-5) |
| Reuse of a revoked Principal | REVOKED is terminal; IDs are never reused (§17.1.4) | Rollback of K7 (TH-32) |
| Display-name confusion | Authorization uses `principal_id` only (A-02) | **Approval displays:** an approver identifying a requester by display name can be misled. SR-06 requires the approval environment to show the stable identifiers from the canonical content. |

---

## 18.12 Platform Compromise Analysis

| Scenario | Actor | What the attacker gains | Helps | Does not help |
|---|---|---|---|---|
| **Stolen session** | T-A2 | Acts as that Principal within its Grants | REAUTH (bounds stale use); enrollment (only enrolled accounts matter); Grants; R4 approval | — |
| **Compromised K3 (W)** | T-A9 (partial) | **Request substitution:** K3 can drop a user's request and pair that user's fresh, genuine assertion with a request of its own. The assertion binds identity, **not request content**. It can act as any user active during the compromise, up to R3, and satisfies REAUTH. | Enrollment and Grants bound it; R4 approval blocks R4; K8 records it | REAUTH (the assertion *is* fresh). **Gap (TH-06).** Request-bound assertions (TQ-05) would close it wherever K2 relays requests. |
| **Compromised K1/K2 (the parent platform)** | T-A9 | Mints assertions for **any** enrolled Principal. It is also root-equivalent (host compromise). | Through SCC: R4 still needs off-host approval (Case C). K8 records any SCC-mediated actions until the attacker uses root against K8. | Host integrity, K7, K8 and K11 against the platform's root authority. REAUTH (the platform asserts freshness itself). |
| **SCC-originated platform compromise** (TH-04) | T-A1 through observed data | Hostile observed content rendered as active content in the SCC UI runs in the **parent platform's origin and session**. That yields actions as the viewing user in SCC (up to R3) **and in the parent platform itself**, which is root-equivalent. **SCC would become a path to escalate from an external attacker to host root.** | SR-01 / T-18-01 | Nothing in §15–§17 explicitly addresses presentation of observed data |

These are three different threats: platform compromise (T-A9), K4 compromise (T-A5) and host-root compromise (T-A10). A platform compromise is *also* a root compromise because of root-equivalence. A K4 compromise is **not**.

---

## 18.13 Credential Threat Model

| Threat | Control | Residual / gap |
|---|---|---|
| Exposure to K4, K5, Integration code | Handles only (T-18, T-19, X-26) | — |
| Exposure through errors, results, K8, K4 audit | Exact-match scrubbing; handle IDs only (X-24, X-26) | Transformed echoes (TH-31) |
| **Exposure through process arguments to local users** (T-A13) | **None in §16.** If a profile delivers a handle-resolved value in an argument slot, any local user may be able to read it from the process table, depending on OS policy. | **Gap (TH-30):** SR-09 (authoring rule, interim) and OD-3 (possible §16 amendment) |
| Exposure to a spoofed endpoint | X-35 (checked before sending) | — |
| Substitution (wrong credential) | Handles are bound to scope entries (§16.9) | — |
| Reuse by compromised K4 | Within scope, via Operations. It can *use* credentials but not read them. | Consistent with §18.5 |
| Exposure through K6 compromise | None | Total (§18.6) |
| Exposure through core discovery process inventory | METADATA_ONLY (X-36) | — |

---

## 18.14 Audit / Forensics Threat Model

| Record | Written by | Can be altered or forged by | Proves (if its writer was honest when writing) | Cannot prove |
|---|---|---|---|---|
| **K4 audit** (in K7) | K4 (C) | K4 (C), root | What SCC *decided* and why | That anything executed. Anything at all if K4 was compromised. |
| **K8 journal** | K6 (root) | K6, root. **Not** C. | What K6 *received and did*, including requests from a compromised K4 | That the Principal or authorization it records as "claimed" was real |
| **Approval evidence** (in K8) | Approver key | Nobody without the key | That an anchored approver signed that exact request (offline-verifiable) | That it executed (a deleted K8 entry leaves no trace) |

**Threats**
- **Deletion or alteration** by root or K6: undetectable unless records were anchored or exported off-host beforehand. That determines SR-12/SR-13.
- **Suppression:** K6 cannot run without journaling (X-29). K4 can suppress K4 audit.
- **False K4 entries:** detectable by cross-checking against K8. A K4 claim of execution with no matching K8 `journal_seq` is evidence of K4 falsification or of K8 loss.
- **False K8 entries** (by a compromised K6 or root): not detectable locally. Forged *approval-bearing* entries are detectable, because signatures can't be forged.
- **Sequence gaps:** K8 has `journal_seq`. **K4 audit has no mandated monotonic sequence** → SR-12.
- **Corruption:** fail-closed (X-29, A-32).

**Forensic rule (T-18-10):** no record may be presented as proving more than its writer could have fabricated.

**Approval evidence retention:** §16 requires K8 to keep the evidence *ID* and the verification result. Keeping the **full evidence** makes approvals verifiable offline after the fact. That is SR-14 (§19).

---

## 18.15 Recovery / K9 Threat Model

K9 is root, so every attack by it is outside the boundary. It can:
- change K11;
- replace SCC binaries;
- rewrite K7 (for example, resurrect revoked Grants or restore the last administrator);
- destroy K8;
- bypass SCC entirely.

**What the threat model establishes as requirements (without designing the protocol, which is P-5):**
- **No new remote reach.** Recovery must not give any non-root component, or any network-reachable path, an ability that component did not already have (T-29, restated as T-18-12).
- **Leave a record.** Recovery acts that change SCC state should leave a record in a store the recovery operator does not casually overwrite. The only protection against a *malicious* operator is a record that has already been exported off-host.
- **Restoring K7 is a rollback risk (TH-32).** Restoring an older K7 can resurrect revoked Principals, Grants or Decisions. Recovery and §19 must make such resurrection detectable, and must not perform it silently (SR-16).

---

## 18.16 Supply-Chain Threat Model

| Attack | Control | Protects against | Does not protect against |
|---|---|---|---|
| Replacing a profile executable or interpreter | X-34 (DIGEST_PINNED / PACKAGE_ATTESTED), root-owned path rules | Non-root substitution; accidental drift | Root; a compromised package source (PACKAGE_ATTESTED trusts the distribution's signing chain) |
| Replacement between verification and invocation | "Execute the verified object" (X-34) | Swap races | Root |
| **Transitive dependencies** (shared libraries, interpreter modules) | Root ownership of paths only; fixed environment (no preload or module-path injection by the request) | Non-root tampering | Root; a compromised package. **Not identity-bound** (TH-27). |
| Modified SCC binaries (K3, K4, K5, K6) | Root-owned install tree (T-21); release signature at install time (§22) | Non-root modification | Root; a compromised release key; no runtime re-verification |
| Malicious Integration code or declaration | Release signature; built-in only (T-22) | Third-party injection | A compromised release key (TH-25) |
| Rollback to an older signed release or declaration | None in §16 | — | TH-24 → SR-15 / OD-4 |
| Compromised dependency of SCC itself | Release process | — | §22 |

---

## 18.17 Availability Threat Model

| Condition | Effect | Security failure or availability failure? |
|---|---|---|
| K4 unavailable | No decisions, no observation, no actions | Availability. Fails closed. |
| K6 unavailable | No observation or action. Inventory stale, not absent (T-28). | Availability |
| K7 unavailable | HUMAN actions refused. SYSTEM observation continues but is not recorded durably. | Availability |
| **K8 unwritable** | K6 refuses **all** requests (X-29) → SCC stops observing | Availability. **An attacker who can fill the file system holding K8 (T-A13 filling disk, T-A1 inflating logs) can make SCC stop observing** (TH-34) → SR-17 (§19 capacity isolation) |
| K11 unreadable or invalid | Affected declarations excluded (X-08) or K6 refuses | Availability |
| K1/K2 unavailable | No interactive actions | Availability |
| Integration unavailable | That capability unavailable; the system stays visible | Availability |
| Request floods (K3→K4, K5→K4, K4→K6) | Bounded by K4 rate limits and K6 concurrency ceilings (§15.10, §16) | Availability |
| Expensive discovery or planning | Output and time bounds (§16.1.2); K4 time bounds on K5 | Availability |
| Job starvation | Per-resource write exclusion (X-22); K4 scheduling (§8) | Availability |
| Approval environment unavailable | R4 unavailable (Owner Decision 2 makes package operations R4) | Availability, accepted by owner decision |

**Principle:** SCC turns uncertainty into refusal, so many attacks that would compromise security in other designs only cause **loss of availability** in SCC. Availability failures must be visible (stale or unavailable), never silent.

---

## 18.18 Deferred / Non-Required Threats (no v1 architecture added)

| Threat or idea | Why no v1 architecture |
|---|---|
| Distributed authorization caching | No cache exists (A-33); single host |
| General policy language | The closed vocabulary is sufficient; a policy language would add attack surface |
| Service principals / API automation | No second authentication path in v1 (P-2) |
| Delegation | Deferred (§17.15) |
| Multi-party approval without §16 support | Would give false assurance against K4 (P-4) |
| Multiple active Integrations per system | Deferred (audit CHANGE-026) |
| Multi-server authorization | Single host. Cross-host *approval replay* is handled by SR-07 without adding multi-server architecture. |
| Protection against a malicious root / host | Impossible by design; acknowledged (§15.15) |
| Per-Integration OS identity | Deferred until non-built-in Integrations exist (§15 OQ-7); v1 risk accepted (RR-09) |
| Runtime re-verification of SCC binaries | Only helps against non-root attackers, who are already stopped by T-21 |
| Broad zero-trust claims | SCC trusts root, K10, K11 and the platform for identity. Claiming otherwise would be false. |

---

## 18.19 Threat Matrix

*Abbreviations: Surv = does the control survive compromise of the attacking or enforcing component; Own = owner of the required action.*

| ID | Threat | Actor | Target | Preconditions | Boundary | Existing control | Enforcer | Surv | Impact | Residual | Required action | Own |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TH-01 | Direct access to SCC endpoints | A1 | SP-01/03 | Network reach | B-01 | No external listener (T-31); K3 only via platform | OS, K10 | Yes | None | None | — | Locked |
| TH-02 | Credential stuffing or phishing of a platform account | A1→A2 | SP-01 | Weak or reused credentials | B-01 | Platform authentication; enrollment (A-03); REAUTH; R4 approval | K1, K4, K6 | Yes (for R4) | Up to R3 as that Principal | Session abuse | — | Locked |
| TH-03 | Hostile observed data exploits a K5 parser | A1 | K5 | Can influence logs or files | B-11 | K5 unprivileged, isolated, no network (T-06) | OS | Yes | K5 compromise (TH-16/17/18) | RR-09 | SR-10 | §18 / impl. |
| TH-04 | **Hostile observed data rendered as active content in the panel origin** | A1 | SP-25, SP-01 | UI renders observed data | B-11→K3→browser | Only the general "untrusted data" rule | — | — | Actions as the viewer; **possible parent-platform (root-equivalent) takeover** | High until mitigated | **SR-01** | §18 → Presentation / Platform Adapter gate |
| TH-05 | Stolen platform session | A2 | SP-03 | Session theft | B-01/03 | REAUTH (A-17); R4 approval | K4, K6 | Yes (R4) | ≤ R3 | RR-05 | — | Locked |
| TH-06 | **Compromised K3 pairs a genuine assertion with a substituted request** | A9 (K3) | SP-03/05 | K3 compromise | B-02/03 | Enrollment, Grants, R4 approval | K4, K6 | R4 only | ≤ R3 as active users | RR-06 | **TQ-05** (request-bound assertions) | Platform Adapter gate |
| TH-07 | Compromised K1/K2 forges any identity | A9 | SP-01 | Platform compromise | B-02 | Off-host R4 approval | Approval env., K6 | Key: yes. Host: no. | Host compromise | RR-04 | SR-05/06 | §18, §22 |
| TH-08 | Low-privilege Principal escalates through crafted requests | A3 | SP-03 | Enrolled | B-03 | Grant evaluation (A-11); K11 | K4, K6 | Yes | None | None | — | Locked |
| TH-09 | Self-grant or role escalation | A3/A4 | SP-04 | Administrator access | B-03 | A-14, A-17 | K4 | No (vs K4) | Escalation | RR-01 | — | Locked |
| TH-10 | Malicious administrator self-approves R4 | A4 | SP-14 | Admin + approver + anchor | B-13/14 | Audit; optional separation of duties | K4, K8 | n/a | Legitimate-looking R4 | RR-10 (Owner Decision 1) | — | Accepted |
| TH-11 | Approver misled | A4/A5 | SP-07 | Misleading context | B-13 | WYSIWYS (A-22) | Approval env. | Yes, if independent | Wrong R4 approved | Human error | SR-06 | §22 |
| TH-12 | Compromised K4 performs R2/R3 host effects | A5 | SP-14 | K4 compromise | B-07 | K11 scope only | K6 | Scope: yes | In-scope R2/R3 | RR-01 | — | Accepted |
| TH-13 | Compromised K4 attempts R4 without approval | A5 | SP-14 | — | B-07/14 | X-16 | K6 | Yes | None | Depends on TH-21 | OD-2 | §16 amend. (opt.) |
| TH-14 | **Cross-host replay of a valid approval** | A5 on host B | SP-08 | Same approver anchored on several hosts; matching request | B-14 | Nonce is per host only | K6 | No | Approved R4 effect replayed on another host | RR-07 | **SR-07**; OD-1 | §18; §16 amend. (opt.) |
| TH-15 | Compromised K4 forges audit | A5 | SP-18 | — | K7 | Cross-check with K8 | Analyst | Yes (K8 intact) | False decision record | Detectable | SR-12 | §19/§21 |
| TH-16 | Compromised K5 plans harmful in-scope content | A6/A8 | SP-05 | K5 compromise; a user requests the capability | B-06 | K4 coverage check; R4 WYSIWYS | K4, approval env. | R4 only | Harmful R2/R3 content | RR-09 | SR-10 | §18/§20 |
| TH-17 | False product-level observations or health | A6/A8 | SP-21 | K5 compromise | B-06 | Generic discovery independent; raw evidence provenance | K4, K6 | Partly | Hidden threats | RR-09 | SR-10 | §18/§20 |
| TH-18 | One Integration worker interferes with siblings | A8 | T-16 | Shared identity I | K5 internal | None at OS level in v1 | — | No | All K5 workers compromised | RR-09 | SR-11 | Impl. / §15 OQ-7 |
| TH-19 | Integration impersonation towards K4 | A8 | SP-11 | TH-18 | B-06 | Launcher binding | K10/K5 | No (with TH-18) | Uses another declaration's scope | RR-09 | SR-11 | Impl. |
| TH-20 | Integration calls K6 or the host directly | A8 | SP-14 | — | B-07/08 | T-06, T-08 | OS, K6 | Yes | None | None | — | Locked |
| TH-21 | **R4 scope entry missing `approval_required`** | A11 / authoring error | SP-14 | Declaration error | B-09 | A-23 (authoring only) | Release process | No | R4 open to compromised K4 | RR-12 | **OD-2**; SR-08 | §16 amend. (opt.) |
| TH-22 | Compromised K6 | A7 | All | Root-level compromise of K6 | B-08 | None on host | — | No | Host compromise | RR-02 | — | Accepted |
| TH-23 | Root modifies K11 | A10 | SP-10 | Root | B-09/12 | None | — | No | Arbitrary | RR-03 | — | Accepted |
| TH-24 | Rollback of K11 or release | A10/A11 | SP-10/24 | Update channel or root | B-09 | None | — | — | Wider scope, fewer flags | RR-11 | **SR-15**; OD-4 | §22; §16 amend. (opt.) |
| TH-25 | Release signing key compromise | A11 | SP-24 | Key theft | B-09 | Release signature | Release process | No | Malicious declarations accepted | RR-11 | SR-15 | §22 |
| TH-26 | Non-root replacement of an executable | A11/A13 | SP-12 | Writable path | B-08 | X-34, path rules | K6 | Yes | None | None | — | Locked |
| TH-27 | Transitive dependency substitution | A11/A10 | SP-12 | Root or compromised package | B-08 | Root ownership only | OS | No | Code runs through an approved executable | RR-11 | Document | §22 |
| TH-28 | Local tenant connects to SCC IPC | A13 | SP-01/14 | Local shell | B-03/05/07 | Channel ACLs; peer identity (T-08) | OS, K6 | Yes | None | None | — | Locked |
| TH-29 | **Tenant plants links or files in declared resource locations** | A13 | SP-15, SP-13 | Declared resource under a tenant-writable path | B-08 | X-13 (symlink and special-file escape) | K6 | Partly | Disclosure or mis-write inside the declared root | RR-08 | **SR-08**; OD-5 | §18; §16 amend. (opt.) |
| TH-30 | **Credential exposed in process arguments** | A13 | SP-13 | Profile puts a handle value in an argument slot | B-08 | None | — | — | Credential disclosure | RR-08 | **SR-09**; OD-3 | §18; §16 amend. (opt.) |
| TH-31 | Transformed credential echoed in output | A5 | SP-13 | Profile output can contain an encoded credential | B-07 | Exact-match scrub | K6 | Partly | Credential disclosure to K4 | RR-01 | SR-09 | §18 (authoring) |
| TH-32 | K7 rollback or restore resurrects revoked authority | A12/A10 | SP-17 | Restore operation | K7 | None | — | — | Revoked authority returns | RR-03 | **SR-16** | §19 / Recovery |
| TH-33 | K8 deleted or altered | A7/A10 | SP-18 | Root | B-10 | Root ownership; X-29 | OS | No | Evidence lost | RR-02/03 | SR-12/13 | §19/§21 |
| TH-34 | **Disk exhaustion makes K8 unwritable, so SCC stops observing** | A13/A1 | SP-21 | Shared file system | B-10 | Fail-closed (X-29) | K6 | Yes (safe) | Loss of observation | RR-13 | **SR-17** | §19 |
| TH-35 | Request floods | A5/A6/A2 | SP-21/22 | — | B-03/05/07 | Rate limits; concurrency ceilings | K4, K6 | Partly | Degraded service | Availability | — | Locked / impl. |
| TH-36 | Revocation race | A4/A5 | SP-17 | Timing | B-07 | Per-request revalidation; deadline | K4, K6 | Partly | One in-flight request completes | Accepted | — | Locked |
| TH-37 | Approver key stolen from host | A9/A10 | SP-07 | Case A custody | B-13 | None against root | — | No | Forged approvals, including on other hosts | RR-04 | SR-06/07 | §22 |
| TH-38 | Approver key held by the platform | A9 | SP-07 | Case B custody | B-13 | — | — | No | As TH-37 | — | **SR-05** | §18 |
| TH-39 | Platform subject reuse | A2 | SP-02 | Unstable subject IDs | B-02 | Binding lost on absence | K4 | Yes | Inherited identity | Adapter-dependent | TQ-07 | Platform Adapter gate |
| TH-40 | Recovery abuse by root | A10 | SP-23 | Root | B-12 | Outside the boundary | — | No | Arbitrary | RR-03 | SR-16, T-18-12 | Recovery gate |
| TH-41 | Plan mutation after authorization | A5/A6 | SP-05 | — | B-07 | A-24 (K4); X-16 (R4) | K4, K6 | R4 only | Changed Plan | RR-01 | — | Locked |
| TH-42 | Target drift between authorization and execution | External change | SP-15 | Host changes | B-08 | `expected_state` (X-14); `system_id` resolution | K6, K4 | Yes | Refused | None | — | Locked |

---

## 18.20 Security Claims

Each claim holds **only** under its stated preconditions.

| ID | Claim | Preconditions | Protecting boundary | Source | Fails if |
|---|---|---|---|---|---|
| SC-01 | A platform session alone confers no SCC authority | K4 intact | B-03 | A-03, A-04 | K4 compromised |
| SC-02 | A Grant cannot widen K11 execution scope | K6 and K11 intact | B-07, B-09 | A-10, X-06 | K6 or root compromised |
| SC-03 | A compromised K4 cannot perform a host write whose scope entry is flagged `approval_required` without valid evidence from an anchored key it does not hold | K6 and K11 intact; approver key not reachable by C | B-07, B-14 | X-16, T-21 | K6 or root compromised; key reachable by C; **the entry is not flagged** (TH-21) |
| SC-04 | An Approval cannot authorize a modified request on the same SCC instance | K6 intact | B-14 | X-16 | K6 compromised |
| SC-05 | An Approval cannot authorize a request on a different SCC instance | **SR-07 holds** (the approver key is anchored on only one instance), or OD-1 is adopted | B-14 | §18.7 | The same anchor is present on several instances without OD-1 |
| SC-06 | Revocation prevents subsequent WRITE issuance | K4 intact | B-03/07 | A-28, A-29 | K4 compromised. The request already in flight completes. |
| SC-07 | A completed host effect is not rolled back by revocation | — | — | A-31, X-21 | — (by design) |
| SC-08 | K4 cannot obtain credential values from K6 | K6 intact; profiles do not return transformed credentials (SR-09) | B-07 | X-24, X-26 | K6 compromised; TH-31 |
| SC-09 | K4 cannot alter or erase K8 | OS permissions intact | B-10 | T-12 | Root or K6 compromised |
| SC-10 | An Integration cannot reach K6, the host, the network or credentials | OS isolation intact | B-05/07 | T-06, T-08, T-19 | Root compromise |
| SC-11 | A non-root actor cannot substitute an approved executable or its interpreter | Path rules and X-34 | B-08 | X-34 | Root; transitive dependencies (TH-27) |
| SC-12 | A valid approval signature in K8 was produced by the anchored key | Signature scheme sound | B-14 | X-16 | Key compromise |
| SC-13 | Loss of K4, K6, K7, K8 or K11 causes refusal or staleness, never false authorization or false absence | Components fail rather than lie | — | X-29, A-32, T-28 | Compromise (not failure) of those components |
| SC-14 | Generic inventory does not depend on Integration honesty | K4 and K6 intact | B-06 | X-36, §15.7 | K4 compromised |
| SC-15 | Observed data cannot become K6 instructions | K6 intact | B-11 | X-23, X-05 | K6 compromised |
| SC-16 | Observed data cannot run in the user's platform session | **SR-01 implemented** | Presentation | T-18-01 | SR-01 not met |
| SC-17 | K8 and K4 audit provide tamper evidence against any actor who cannot also rewrite the off-host anchor or export | SR-12/SR-13 implemented, with records exported before the compromise | B-10 | T-18-09 | No export; compromise before export |
| SC-18 | Off-host approval keys stay unforgeable under host or platform compromise | SR-06 independence holds | B-13 | §18.7 | The environment is not independent |
| SC-19 | Host integrity is **not** protected by SCC against a root-equivalent attacker | — | — | §15.15 | (negative claim, always true) |

---

## 18.21 Residual Risk Register

| ID | Risk | What remains protected | What fails | Why | Mitigation | Where |
|---|---|---|---|---|---|---|
| RR-01 | Compromised K4 | K11 scope; executable and endpoint identity; credential values (SC-08 conditions); R4 flagged entries; K8; K11 | All R0–R3 authority; K4-internal administration; K4 audit; misleading presentation | K4 is the authorization authority (§17.21) | Keep K4 unprivileged and without egress; cross-check with K8 | Accepted |
| RR-02 | Compromised K6 | Off-host keys; exported audit | Everything on the host | K6 is root | Minimal K6 (§16) | Accepted |
| RR-03 | Compromised K11 / root / K9 | Off-host keys; exported audit | Everything on the host, including K7 rollback | Root is outside the boundary | Off-host audit export (SR-13) | Accepted |
| RR-04 | Compromised parent platform | Off-host keys (Case C) | Identity; host (root-equivalent) | Platform is both identity TCB and root-equivalent | SR-05, SR-06 | Accepted |
| RR-05 | Stolen platform session | R4 (approval) | ≤ R3 as that Principal | Platform authentication is trusted | REAUTH | Accepted |
| RR-06 | Compromised K3 (request substitution) | R4 | ≤ R3 as users active at the time | Assertion is not bound to request content | TQ-05 | Platform Adapter gate |
| RR-07 | Approver key anchored on several instances | Per-instance replay protection | Cross-instance replay | Digest has no instance binding | SR-07; OD-1 | §18 / §16 amend. (opt.) |
| RR-08 | Tenant-writable declared resources; credentials in arguments | Most declared resources | Confinement and credential confidentiality for badly authored entries | §16 does not constrain these | SR-08, SR-09; OD-3, OD-5 | §18 / §16 amend. (opt.) |
| RR-09 | Malicious or compromised Integration or K5 | Host, K6, credentials, generic inventory | Product-level truth; content of R2/R3 Plans; sibling workers | Shared identity I; semantics owned by the Integration | SR-10, SR-11 | Impl. / §15 OQ-7 |
| RR-10 | Malicious privileged administrator | Accountability (K8 + K4 audit) | Prevention (self-approval is the default) | Owner Decision 1 | Optional separation of duties | Accepted |
| RR-11 | Supply chain (release key, rollback, transitive dependencies, package sources) | Non-root substitution | Genuine-looking malicious or old content | Signatures prove authenticity, not safety or recency | SR-15 | §22 |
| RR-12 | Declaration authoring error (`approval_required` missing) | Everything else | R4 protection against compromised K4 for that entry | A-23 is an authoring rule | OD-2; SR-08 | §16 amend. (opt.) / release review |
| RR-13 | Loss of observation through resource exhaustion | Security (fails closed) | Visibility | X-29 fails closed | SR-17 | §19 |

---

## 18.22 Security Requirements Arising from §18

| ID | Requirement | Classification | Owner |
|---|---|---|---|
| SR-01 | All observed data and Integration-supplied text MUST be presented as inert data. It MUST NOT be interpreted as markup, script or navigation in any SCC view hosted within the parent platform's origin or session. | **§18 REQUIREMENT** (implementation in the Presentation Adapter / Platform Adapter gate) | §18 → Platform Adapter gate |
| SR-02 | Platform authentication is not SCC authorization | LOCKED / ALREADY SATISFIED | §17 |
| SR-03 | Grants cannot widen K11 | LOCKED / ALREADY SATISFIED | §16/§17 |
| SR-04 | K8 is not writable by C | LOCKED / ALREADY SATISFIED | §15 |
| SR-05 | Approver key material MUST NOT be stored in, or be accessible to, K1, K2, K3, K4, K5 or the parent platform | **§18 REQUIREMENT** | §18 (custody mechanics: §22) |
| SR-06 | An approval environment claimed to resist platform or root compromise MUST satisfy all five independence conditions (§18.7.2). Host-local custody (Case A) MUST be described as resisting only non-root SCC compromise. | **§18 REQUIREMENT** | §18 / §22 |
| SR-07 | Until the approval digest binds a K6-instance identity, an approver key MUST NOT be anchored on more than one SCC instance | **§18 REQUIREMENT** (interim) | §18 / §22 |
| SR-08 | K11 declarations SHOULD NOT declare resources in locations writable by non-root identities. Where unavoidable, they MUST be READ-only with non-FULL exposure. Every R4-relevant entry MUST carry `approval_required` (release-review rule reinforcing A-23). | **§18 REQUIREMENT** (authoring rule) | Release process |
| SR-09 | Profiles MUST NOT deliver credential-derived values in argument slots, and MUST NOT have FULL-exposure outputs that can contain transformed credentials | **§18 REQUIREMENT** (authoring rule); OD-3 would make it K6-enforced | Release process |
| SR-10 | K4 MUST keep generic inventory and raw evidence visibly separate from Integration interpretations. Integration-derived conclusions MUST be attributed to their Integration. | **DOWNSTREAM** | §20/§21 (UI binding §13) |
| SR-11 | Implementation SHOULD apply OS-level restrictions that limit interference between processes of the same K5 identity | **DOWNSTREAM** (implementation) | Implementation gate |
| SR-12 | K4 audit MUST carry a monotonic sequence. Both K4 audit and K8 MUST be tamper-evident. | **DOWNSTREAM** | §19/§21 |
| SR-13 | Off-host export of K8 and K4 audit SHOULD be supported. Without it, no audit property survives a root compromise. | **DOWNSTREAM** | §19/§21 |
| SR-14 | K8 SHOULD retain the full approval evidence, not only its ID | **DOWNSTREAM** (within the §16 "minimum" fields) | §19 |
| SR-15 | Updates MUST refuse older releases or declarations unless root explicitly overrides, with the override audited. Release-key custody MUST be defined. | **DOWNSTREAM** | §22 |
| SR-16 | K7 restore MUST NOT silently resurrect revoked Principals, Grants, anchors or Decisions. Such rollback MUST be detectable. | **DOWNSTREAM** | §19 / Recovery gate |
| SR-17 | K8 MUST have capacity isolated from file systems that tenants or observed data can fill | **DOWNSTREAM** | §19 |
| SR-18 | Assertions SHOULD be bound to request content wherever K2 relays requests | **DOWNSTREAM** / owner decision (TQ-05) | Platform Adapter gate |
| SR-19 | K6-instance identity inside the approval digest | **POSSIBLE AMENDMENT** (§16) | OD-1 |
| SR-20 | K6 enforces at load time that `executable_semantics` or package-WRITE entries carry `approval_required` | **POSSIBLE AMENDMENT** (§16) | OD-2 |
| SR-21 | Global Execution Policy forbids handle values in argument slots | **POSSIBLE AMENDMENT** (§16) | OD-3 |
| SR-22 | K6 refuses to load declarations older than the last accepted version | **POSSIBLE AMENDMENT** (§16), alternative to SR-15 | OD-4 |
| SR-23 | Resource declarations carry an expected ownership that K6 verifies on resolution | **POSSIBLE AMENDMENT** (§16) | OD-5 |
| SR-24 | Per-Integration OS identities | **DEFERRED** | §15 OQ-7 |
| SR-25 | K6-verifiable multi-party approval | **DEFERRED** | P-4 |

---

## 18.23 Normative Threat-Model Invariants

- **T-18-01** Observed data and Integration-supplied text MUST be presented only as inert data in any SCC view that shares an origin or session with the parent platform. *(Owner: Presentation / Platform Adapter gate)*
- **T-18-02** No security claim MAY be made for a root-equivalent compromise (K1/K2, K6, K9, K10, root) beyond the survival of data held off-host. *(Owner: §18)*
- **T-18-03** Approver key material MUST NOT be stored in, or be accessible to, K1–K5 or the parent platform. *(Owner: §18 / §22)*
- **T-18-04** An approval environment MUST NOT be described as resisting platform or root compromise unless it meets every independence condition in §18.7.2. *(Owner: §18 / §22)*
- **T-18-05** Until the approval digest binds an SCC-instance identity, an approver anchor MUST NOT be installed on more than one SCC instance. *(Owner: §18 / §22)*
- **T-18-06** Approval displays MUST interpret identifiers only through release-signed declarations that the approval environment has verified itself. *(Owner: §22)*
- **T-18-07** Credential-derived values MUST NOT reach any channel observable by non-root local identities, including process arguments. *(Owner: release authoring; OD-3)*
- **T-18-08** Declared resources in non-root-writable locations are excluded; where unavoidable, they MUST be READ-only with non-FULL exposure. *(Owner: release authoring; OD-5)*
- **T-18-09** Every audit store (K4 audit, K8) MUST be tamper-evident and gap-detectable, and MUST NOT be presented as proving facts its writer could have fabricated. *(Owner: §19/§21)*
- **T-18-10** Forensic conclusions MUST distinguish: K4 decisions (K4-attested), K8 execution records (K6-attested) and approval signatures (key-attested). *(Owner: §21)*
- **T-18-11** Resource exhaustion reachable by non-SCC identities MUST NOT be able to make K8 unwritable. *(Owner: §19)*
- **T-18-12** Recovery MUST NOT give any non-root or network-reachable component an ability it lacked before recovery. *(Owner: Recovery gate)*
- **T-18-13** Restoring SCC state MUST NOT silently reinstate revoked authority. *(Owner: §19 / Recovery gate)*
- **T-18-14** Updates MUST NOT silently install older release or declaration content. *(Owner: §22)*
- **T-18-15** Generic inventory and raw evidence MUST remain distinguishable from Integration-derived interpretation in every presentation and record. *(Owner: §20/§21/§13)*
- **T-18-16** Availability failures caused by fail-closed behavior MUST be visible as stale or unavailable states. They MUST NOT be silent. *(Owner: §21 / UI)*
- **T-18-17** Each residual risk RR-01–RR-13 MUST be stated in operator-facing security documentation, and MUST NOT be contradicted by product claims. *(Owner: documentation)*

---

## 18.24 Compatibility Audits

### §15

The following are all unchanged:
- topology;
- process identities (W, C, I, root);
- trust direction;
- K4 authority;
- the K6 privilege boundary;
- the K9 boundary;
- IPC assumptions;
- the parent-platform trust model (identity TCB, root-equivalent).

T-01…T-31 are **all preserved**. TH-18 restates §15.8's accepted v1 posture on shared Integration identity; it does not change it.

**PASS.**

### §16

The following are unchanged:
- Operation vocabulary;
- K11 scope;
- executable and endpoint identity;
- the approval interface;
- Core Discovery;
- credential handling;
- cancellation;
- K6 independence.

§18 identifies five **possible amendments** (OD-1…OD-5). None is applied. Each has an interim §18 authoring or deployment rule (SR-07, SR-08, SR-09, SR-15), so none of them blocks progress. X-01…X-39 are **all preserved**.

**PASS.**

### §17

The following are unchanged:
- Principal classes;
- Grants and Roles;
- tiers;
- approval semantics;
- self-approval default;
- Plan authorization;
- Job revalidation;
- revocation;
- fail-closed behavior;
- `authorization_ref`;
- the compromised-K4 boundary.

**Precision, not conflict:** §17.9/§17.21 describe off-host keys as needed "for protection against the platform". §18.7 clarifies what that protection is. Off-host custody protects **the unforgeability of approvals**. It does **not** protect host integrity against a root-equivalent platform. §17 never claimed the latter.

**Addition, not conflict:** §18.5 adds cross-instance approval replay (TH-14) to the compromised-K4 capabilities in §17.21. That list was scoped to one instance.

A-01…A-36 are **all preserved**.

**PASS.**

---

## 18.25 Open Questions

| ID | Question | Owner | Blocks? | Proposed disposition |
|---|---|---|---|---|
| TQ-01 | (P-1) Approver key custody and approval-environment mechanics, meeting SR-05/06/07 and T-18-06 | §22 | Blocks enabling R4 | Carry to §22 |
| TQ-02 | (P-5) K9 recovery authority, constrained by T-18-12/13 | Recovery gate | No | Carry |
| TQ-03 | (P-6) Platform subject stability for CyberPanel | Platform Adapter gate | Blocks CyberPanel binding | Carry |
| TQ-04 | Audit tamper-evidence mechanism, sequencing and off-host export (SR-12/13/14) | §19/§21 | No | Carry |
| TQ-05 | Request-bound assertions (SR-18), and what happens when the adapter uses a proxy route in which K2 cannot see requests | Platform Adapter gate / owner | No | Owner decision at the adapter gate. RR-06 is accepted until then. |
| TQ-06 | Release-key custody and rollback protection (SR-15), and whether OD-4 is also adopted | §22 / owner | No | Carry |
| TQ-07 | Pre-image visibility for approvers of `file.replace` (a diff needs content that is not in the digest) | §22 | No | Carry (approval-tool usability; does not affect security binding) |
| TQ-08 | K7 restore rollback detection (SR-16) | §19 / Recovery | No | Carry |
| TQ-09 | K8 capacity isolation (SR-17) | §19 | No | Carry |
| TQ-10 | Presentation isolation mechanism for SR-01 within each parent platform's supported extension model | Platform Adapter gate | Blocks the UI implementation | Carry |

---

## Gate Assessment

**Threat-model completeness: PASS.**
- All twelve required actors are covered, plus T-A13.
- All required properties are covered, plus SP-25.
- Every requested compromise analysis is included.

**§15 compatibility: PASS.**
**§16 compatibility: PASS.** Possible amendments are listed but none are applied.
**§17 compatibility: PASS.** There is one precision (off-host scope) and one addition (cross-instance replay). There are no conflicts.

**Required architecture changes:** none to the locked gates. §18 adds invariants T-18-01…T-18-17 and requirements SR-01, SR-05–SR-09.

**Downstream requirements:**
- SR-10 → §20/§21
- SR-11 → implementation
- SR-12/13/14 → §19/§21
- SR-15 → §22
- SR-16 → §19/Recovery
- SR-17 → §19
- SR-18 → Platform Adapter gate
- SR-01 implementation → Presentation / Platform Adapter gate

**Possible amendments (for you to decide; none blocks §19):**

| ID | Proposed §16 amendment | Interim rule if not adopted |
|---|---|---|
| OD-1 | Bind SCC-instance identity into the approval digest | SR-07 |
| OD-2 | K6 load-time enforcement of `approval_required` for criteria (a)/(b) | SR-08 |
| OD-3 | K6 forbids handle values in argument slots | SR-09 |
| OD-4 | K6 refuses older declarations | SR-15 |
| OD-5 | Resource ownership expectations, verified by K6 | SR-08 |

**Residual risks accepted:** RR-01…RR-13.

**Owner decisions:**
- OD-1…OD-5: adopt, defer, or reject each §16 amendment.
- TQ-05: whether request-bound assertions become mandatory where the adapter can support them.

**Open questions:** TQ-01…TQ-10.

**Conflicts:** none.

**Gate disposition:**

**§18 — PASS — READY FOR §19**

The possible amendments and TQ-05 are owner decisions. Their interim requirements keep the architecture consistent, so none blocks progress to §19.
