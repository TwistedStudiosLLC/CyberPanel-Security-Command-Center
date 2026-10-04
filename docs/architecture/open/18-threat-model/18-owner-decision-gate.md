> **Document status:** OPEN — owner-decision record for ODF-18-01 … ODF-18-09
> **Authority category:** 4 — Conditional/open architecture (see [Authority Hierarchy](../../README.md#authority-hierarchy))
> **Source:** §18 owner-decision gate document.
> **Normative:** No. This document records questions, options and consequences. It decides nothing.
> **Current dispositions (recorded elsewhere, not edited into this file):**
> - **ODF-18-01** was dispositioned by the owner in DEC-015 (D-3): the universal presentation/origin question is
>   deferred to the Platform/K2 gate for each concrete platform; for CyberPanel it goes to the CyberPanel K2 /
>   Platform Adapter gate. The "OWNER DECISION REQUIRED" marker and the "BLOCKING" status below are therefore
>   **historical** for ODF-18-01. The statements below that ODF-18-01 requires a §15 amendment under every option
>   were written before DEC-015, which states "Do not resolve ODF-18-01 by weakening §15."
> - **ODF-18-02 … ODF-18-09 remain OPEN** (DEC-015).
>
> See [`README.md`](README.md) and the [decision log](../../decisions/decision-log.md).
> **Transcription notes:** Reproduced verbatim. Removed process-wrapper text only: the opening italic line ("This is a
> decision record, not a rewrite. … I have not created or modified any files.") and the closing line ("Stopping here.
> … I'll wait for your explicit owner decisions.").

# SCC §18 — Owner Decision Gate

**Labels used below.** Each statement is tagged with its source:
- **[L]** locked architectural fact (§15, §16 or §17)
- **[F]** finding from the §18 threat model or the forensic review
- **[O]** owner choice
- **[D]** downstream requirement
- **[A]** optional amendment
- **[M]** model analysis or inference that needs verification

---

## 1. Gate Status

> **§18 — CONDITIONAL — OWNER REVIEW REQUIRED**

The evidence does not support any other status:
- ODF-18-01 is unresolved and still blocks.
- The analysis below finds **one new cross-decision dependency that affects locked text**: ODF-18-07 in combination with §15.4 and §16.1.3 (see §8 and §11). It does not change the blocking classification, but the owner must decide it together with the export mechanism.

---

## 2. ODF-18-01 — Presentation Origin Model

**Current status:** BLOCKING

**Architectural question**

Does content served by SCC (K3 and the Presentation Adapter) run in the parent platform's origin and session, or in an origin isolated from it?

**Locked constraints**
- [L] §15.5: K1 is the identity TCB and is root-equivalent. SCC cannot guarantee that the page the user sees contains what SCC sent.
- [L] §15.6: K3 is identity W, has no path to K6 and cannot mint identity. The same section states the bound: *"Even a fully compromised K3 can only send K4 requests K4 would accept from the authenticated user anyway."*
- [L] §15.18 OQ-1: requests may reach K3 through a K2 relay or a platform proxy route. OQ-1 says "Both satisfy §15."
- [L] T-24: platform integration must use only supported extension mechanisms.
- [L] T-27: platform-specific code lives only in K2, the Presentation Adapter or Platform Services.
- [L] A-04: in v1 every viewer is `PLATFORM_ADMIN`.
- [L] A-22: the approval tool must run outside K1–K4 and outside pages served through them.
- [L] Baseline §13.55: native presentation through supported mechanisms, with no design hacks.

**Threat-model consequence**
- [F] TF-18-01: under same-origin embedding, hostile observed data rendered as active content runs with the platform administrator's session.
- [F] TF-18-02: under same-origin embedding, a compromised K3 can inject script into the platform origin. That escalation is root-equivalent (§15.5 + A-04), which contradicts the §15.6 bound and OQ-1's "both satisfy".
- [M] Whether each OQ-1 path yields a shared origin on CyberPanel has not been verified.

**Missing information** [M]
- Whether CyberPanel's supported extension mechanism can host SCC content in an isolated origin while still providing navigation and parent-theme integration.

The owner can decide the policy without this. It determines only whether Option A is feasible for the CyberPanel adapter.

**Options**

**Option A — Origin isolation**
- **What changes:** SCC-served content must run in an origin isolated from the parent platform. The navigation integration and page frame from K2 stay in the platform. SCC content runs in its own origin, and communication between the two uses a constrained channel. (The mechanism belongs to the adapter.)
- **What does not change:** K3's identity, its lack of a path to K6, end-to-end assertion verification by K4, and A-22.
- **Security consequence:** the §15.6 bound on a compromised K3 becomes true again. SR-01 becomes defence in depth, not the main containment. A compromise of K3 or of rendering stays inside SCC's non-root domain.
- **Architectural consequence:**
  - Native appearance must come from theme data such as tokens and capabilities, not from shared DOM or styles.
  - [M] This is compatible with §13.55.3/§13.55.4 (Parent Theme Contract, capability discovery). It may limit how "native" the result looks.
  - An adapter that cannot provide isolation cannot be supported for presentation.
- **§15:** YES. Constrain OQ-1 so that only isolated paths conform, and add a normative invariant, e.g. T-32: "SCC-served content MUST execute in an origin isolated from the parent platform". §15.6 text stays valid.
- **§16:** NO.
- **§17:** NO.
- **Downstream:** YES. The Presentation Adapter gate defines the isolation mechanism and the parent-theme transport. CyberPanel feasibility must be verified.

**Option B — Same-origin embedding accepted**
- **What changes:** SCC content explicitly runs in the platform origin and session.
- **What does not change:** K3's OS identity and IPC position.
- **Security consequence:**
  - K3, the Presentation Adapter and every rendered item of observed or Integration data become part of the parent platform's **effective TCB**.
  - A compromised K3 becomes root-equivalent through the platform session.
  - SR-01 becomes a **critical** control. Any failure of it lets an unauthenticated external attacker (T-A1) reach root-equivalent control.
  - Claims that must be weakened: the §15.6 K3 bound; §15.15's "compromised-code isolation" row for K3; SC-16 (it holds only if K3 is uncompromised and SR-01 is perfect); and any claim that K3 compromise stays non-root.
- **Architectural consequence:** K3 hardening becomes platform-critical. The attack surface of SCC's exposed parser now counts toward platform compromise.
- **§15:** YES. Rewrite the §15.6 bound, qualify the §15.15 table, and correct OQ-1's "both satisfy".
- **§16:** NO.
- **§17:** NO.
- **Downstream:** YES. The Presentation Adapter gate carries SR-01 as a critical requirement.

**Option C — Per-adapter declared TCB consequence**
- **What changes:** each Presentation Adapter declares either `ISOLATED` or `IN_PLATFORM_TCB`.
- **What does not change:** everything outside presentation.
- **Security consequence:** security claims become conditional on the adapter's declaration. `IN_PLATFORM_TCB` adapters inherit all of Option B's consequences. `ISOLATED` adapters get Option A's.
- **Architectural consequence:**
  - The declaration becomes a **compatibility dimension** (§12), and SCC must show it.
  - SC-16 and the §15.6 bound become per-adapter claims.
  - If an adapter's isolation claim cannot be verified, it must be treated as `IN_PLATFORM_TCB` (fail closed).
- **§15:** YES. §15.6 and OQ-1 must state the two classes, and a new invariant must require a declared TCB consequence.
- **§16:** NO.
- **§17:** NO.
- **Downstream:** YES. §12 compatibility, the Presentation Adapter gate, and documentation (T-18-17).

**Recommended owner disposition**
- Option A is the only one that keeps the §15.6 boundary as written.
- Option C keeps it where it is feasible, and discloses the consequence where it is not.
- Option B keeps it nowhere.

This recommendation is based only on consistency with the existing §15 text.

**Owner decision**

> OWNER DECISION REQUIRED

**Post-decision consequence (what the canonical §18 must record)**
- **If A:** SR-01 and T-18-01 become defence in depth. TF-18-02 is closed by the §15 invariant. SC-16's preconditions become "K3 not compromised **or** isolation holds". RF-18-06 is withdrawn.
- **If B:** TF-18-02 becomes an accepted residual risk. SR-01 and T-18-01 are marked critical. SC-16 is weakened. K3 is listed in the T-A9-equivalent TCB. RF-18-06 is added.
- **If C:** all of the above, made conditional per adapter declaration. A compatibility requirement is recorded.

In every case, the matching §15 amendment must be authorized **before** §18 locks.

---

## 3. ODF-18-02 — Cross-instance Approval Replay

**Current status:** NON-BLOCKING

**Architectural question**

Must an approval be cryptographically bound to one SCC/K6 instance, or is replay across instances controlled operationally or accepted?

**Locked constraints**
- [L] §16.5: the digest fields contain no instance identity. The nonce is checked "against K8", so it is host-local.
- [L] X-16.
- [L] A-19: approval uses the §16.5 interface without change. After an amendment, A-19 would refer to the amended §16.5; §17 would not be edited.
- [L] §17.9: local root adds anchors on each host, and nothing prohibits the same key being anchored on several hosts.
- [L] SC-03 as written in the candidate.

**Threat-model consequence**
- [F] TF-18-03: when a compromised K4 on host B holds evidence from host A and the canonical requests are identical, the R4 protection claimed against a compromised K4 fails on B.
- [F] "Single-host SCC" describes what SCC manages, not how approver keys are distributed. It does not remove the issue.

**Options**

**Option A — Amend §16 to bind approvals to an instance**
- **What changes:** a stable K6 instance identity becomes part of the §16.5 canonical digest, and X-16 verifies it.
- **What does not change:** single-use nonces, deadlines, the anchor model.
- **Security consequence:** cross-instance replay is closed. SC-03 holds without an SR-07 precondition.
- **Architectural consequence:**
  - It adds a new concept: an SCC instance identity held by K6 in root-owned storage. How it is provisioned is a §22 matter.
  - The approval tool must display that identity (WYSIWYS, A-22/T-18-06).
- **§15:** NO.
- **§16:** YES (§16.5 digest field list, X-16).
- **§17:** NO. A-19 keeps referring to §16.5.
- **Downstream:** §22 (instance identity lifecycle; approval-tool display).

**Option B — Keep §16 as is; SR-07 operational rule**
- **What changes:** an approver key may be anchored on only one instance until instance binding exists. This rule is enforced by anchor provisioning (§22).
- **What does not change:** §16.
- **Security consequence:**
  - SC-03 becomes conditional: "…provided the approver's anchor is present on no other SCC instance."
  - K6 cannot verify this, because an anchor carries no cross-host knowledge. A violation cannot be detected locally.
  - RR-07 remains wherever the rule is broken.
- **Architectural consequence:** operational burden (a separate approver key per host).
- **§15:** NO. **§16:** NO. **§17:** NO.
- **Downstream:** YES. §22 anchor provisioning, and documentation.

**Option C — Accept as residual risk**
- **What changes:** nothing in the architecture.
- **Security consequence:** SC-03 is scoped to "on the instance where the approval was issued". RR-07 is accepted without a mitigating rule.
- **§15:** NO. **§16:** NO. **§17:** NO.
- **Downstream:** documentation only.

**SC-03 under each option**
- **A:** holds with its existing preconditions.
- **B:** holds only if SR-07 is honoured.
- **C:** holds only for the originating instance.

**Is a §16 amendment required?** Only if SC-03 must be unconditional. Otherwise, no.

**Recommended owner disposition**

Option A. SC-03 is the architecture's central compromised-K4 claim, and SR-07 cannot be verified by the component that would rely on it. Option B is internally coherent for v1 if SC-03 is scoped.

**Owner decision**

> OWNER DECISION REQUIRED

**Post-decision consequence**
- **A:** record OD-1 as adopted, pending a §16 amendment gate. TH-14 is closed once that amendment lands. RR-07 is withdrawn.
- **B:** record SR-07 and T-18-05 as normative, with §22 as owner. SC-03 is scoped. RR-07 is kept.
- **C:** record RR-07 as accepted, and scope SC-03 and SC-05.

---

## 4. ODF-18-03 — R4 `approval_required`

**Current status:** NON-BLOCKING

**Architectural question**

Is the consistency between R4 criteria and the `approval_required` flag enforced only when a release is validated, or also by K6 when it loads K11?

**Locked constraints**
- [L] A-23: K11 declarations MUST set `approval_required` on every scope entry used by an R4 capability. This is an authoring rule.
- [L] §17.5.3: effective tier is the maximum of the declared tier (signed in K11), the tier derived from criteria (a)/(b), and any local raise.
- [L] X-17: K6 does not evaluate authorization policy.
- [L] X-10: precedent for a K6 load-time consistency check (a validator is required for `executable_semantics`).
- [L] X-08: declarations that fail validation are excluded.

**Three different functions** [F]
- **Authorization:** principal, Grant, condition and tier evaluation. K4 only. Unchanged under every option.
- **Signed-declaration validation:** checks that a declaration is well-formed. Done at release time, and optionally again by K6 at load.
- **Execution enforcement:** K6 obeying `approval_required` at request time (X-16). Unchanged.

**Which criteria can be checked mechanically** [F]

| Criterion | Mechanically validatable from signed K11 data? | Notes |
|---|---|---|
| (a) `executable_semantics` WRITE | Yes, **if the flag is present** | Cannot catch an author who omits `executable_semantics` itself |
| (b) package-family WRITE | **Yes, robustly** | Follows from `op_id` itself |
| (c) host access-control semantics | No | Requires judging what the content means |
| (d) reserved `scc.*` | Not applicable | Internal to K4; never reaches K6 |
| (e) Integration-declared R4 | Yes, if the declared tier is carried in the signed declaration | [M] §17.5.3 says it is "signed in K11" |
| Local raise | No | Lives in K7 |

**Threat-model consequence**

[F] TF-18-04: accidental omission of the flag removes R4 protection against a compromised K4 (RR-12). Neither option stops a malicious release author.

**Options**

**Option A — Release validation only**
- **What changes:** §22 release tooling must check (a), (b) and (e) before signing. [D]
- **What does not change:** K6.
- **Security consequence:** protection depends on the release tooling being correct. A declaration that is corrupted after signing is already caught by the signature (X-08). A signed declaration that passed faulty tooling is not caught.
- **§15:** NO. **§16:** NO. **§17:** NO.
- **Downstream:** §22.

**Option B — Release validation plus a K6 load-time well-formedness check**
- **What changes:** the §16.2 Global Execution Policy gains a rule. K6 excludes any declaration where a package-family WRITE, an `executable_semantics` WRITE, or an entry of a declared-R4 capability lacks `approval_required`. A new X-invariant follows. It works like X-10.
- **What does not change:** K6 still evaluates no principal, Grant, role, condition or local policy, so **K6 does not become an authorization engine**. A-23 is unchanged.
- **Security consequence:** defence in depth against release-tooling failure for (a), (b) and (e). Criterion (c) and malicious authors are still not covered.
- **§15:** NO. **§16:** YES (optional amendment: §16.2 Global Execution Policy and a new X-invariant). **§17:** NO.
- **Downstream:** §22 (still required).

**Recommended owner disposition**

Option A is required in either case. Option B is recommended at least for criterion (b), because it is robust and matches the X-10 precedent.

**Owner decision**

> OWNER DECISION REQUIRED

**Post-decision consequence**
- **A:** record SR-08(ii) as §22 release validation. RR-12 is retained, with release tooling as its control.
- **B:** additionally record OD-2 as adopted, pending a §16 amendment gate. RR-12 is narrowed to criterion (c) and malicious authors.

---

## 5. ODF-18-04 — Credential-derived Arguments

**Current status:** NON-BLOCKING

**Architectural question**

May a value derived from a credential handle be delivered to an invoked program as a process argument?

**Locked constraints**
- [L] §16.1.5: `handle_ref` is a permitted profile slot type, and argument slots are typed slots.
- [L] §16.8: credentials are resolved inside K6 at invocation.
- [L] T-18/T-19: credentials exist only in K6.
- [L] X-24: output scrubbing is exact-match.
- [L] X-26.

**Threat-model consequence**
- [F] TF-18-06: argument delivery may expose the credential to local non-SCC identities (T-A13).
- [M] Whether process arguments are visible to other local users depends on the **Host Environment** (OS defaults, and process-information hiding if configured). This must not be assumed universal.
- [F] This is a **separate** threat from transformed credential values echoed back through outputs (TH-31). That second threat is handled by SR-09's output clause, whichever option is chosen here.

**Options**

**Option A — Authoring prohibition**
- **What changes:** a K11 authoring rule forbids credential-derived argument slots.
- **Security consequence:** protection depends on authoring. K6 does not enforce it.
- **Architectural consequence:** products that accept secrets only through arguments cannot be supported.
- **§15:** NO. **§16:** NO. **§17:** NO.
- **Downstream:** release validation (§22).

**Option B — §16 load-time prohibition**
- **What changes:** the Global Execution Policy forbids `handle_ref` in argument slots, allowing only stdin, a declared file descriptor or environment. [M] Environment visibility is also Host Environment dependent. K6 excludes offending profiles. A new X-invariant follows.
- **Security consequence:** enforced mechanically, and universal.
- **Architectural consequence:** same product limitation as Option A.
- **§16:** YES (§16.1.5 and §16.2, plus a new X-invariant). **§15:** NO. **§17:** NO.

**Option C — Permit only with process-argument confidentiality from the Host Environment**
- **What changes:** profiles that use argument delivery must declare a `requires_argument_confidentiality` condition. It becomes a Host Environment compatibility fact (§12).
- **Security consequence:**
  - If only K4 checks compatibility, a compromised K4 can ignore it.
  - Mechanical enforcement would need K6 to check the host condition before invocation. That is a §16 precondition amendment.
- **Architectural consequence:** products that need argument delivery remain supportable where the host environment allows.
- **§16:** YES if K6 enforces it; otherwise NO. **§15:** NO. **§17:** NO.
- **Downstream:** §12 Host Environment, and the Platform Adapter.

**What SR-09 becomes under each option**
- **A:** an authoring restriction.
- **B:** a universal prohibition.
- **C:** a compatibility-conditioned rule.

**Recommended owner disposition**

Option B or Option C with K6 enforcement. Both give mechanical enforcement. Option A relies on authoring alone.

**Owner decision**

> OWNER DECISION REQUIRED

**Post-decision consequence**
- Record the chosen form of SR-09's argument clause and T-18-07.
- Record OD-3 if Option B, or C with K6 enforcement, is chosen.
- Keep the transformed-echo clause as an authoring rule in every case.
- Split RR-08 (RC-21).

---

## 6. ODF-18-05 — WRITE Resource Ownership

**Current status:** NON-BLOCKING

**Architectural question**

Must K6 mechanically verify path-component ownership for WRITE resources, in the same way it already does for executable paths?

**Locked constraints**
- [L] X-13: K6 MUST resolve only through declared resources and MUST refuse any resolution that escapes the declared root, including through symlinks and special files. This is a **guarantee about the outcome**; it does not specify how.
- [L] §16.2.2: executable paths must be root-owned and not group- or world-writable. That rule is a **preventive, mechanical check**.
- [L] X-24: exposure modes.

**Threat-model consequence**
- [F] TF-18-05, READ: tenant-controlled content can be disclosed to C or I. The risk depends on the exposure mode. It is not a privilege escalation.
- [F] TF-18-05, WRITE: redirecting a root commit through tenant-controlled path components is a privilege escalation.
- X-13 already forbids the outcome. An ownership rule would add a preventive control that is simpler to verify.

**Options**

**Option A — Authoring rule only**
- **What changes:**
  - §18 authoring rule: WRITE resources MUST NOT be declared where any path component is writable by a non-root identity other than an identity declared for that resource.
  - READ resources in such locations MUST NOT use `FULL` exposure.
- **Security consequence:** relies on authoring, plus X-13's outcome guarantee being implemented race-safely.
- **§15:** NO. **§16:** NO. **§17:** NO.
- **Downstream:** release validation.

**Option B — K6 verifies path-component ownership for WRITE**
- **What changes:** §16.2 resource path rules and an extension of X-13 or a new X-invariant. At resolution, WRITE resources require every path component to be owned by root or by a declared owner identity, and not writable by any other non-root identity.
- **What does not change:** READ semantics, apart from the Option A exposure rule, which stays an authoring rule.
- **Security consequence:** a mechanical preventive control that mirrors the executable-path rule.
- **§16:** YES (optional amendment). **§15:** NO. **§17:** NO.

READ and WRITE stay distinct under both options. **Tenant-writable READ resources are not prohibited.**

**Recommended owner disposition**

Option B for WRITE, for consistency with the existing executable-path rule. Option A is a coherent interim.

**Owner decision**

> OWNER DECISION REQUIRED

**Post-decision consequence**
- Rewrite T-18-08 as "WRITE MUST NOT / READ limited exposure" (RC-09) in both cases.
- **B:** record OD-5 as adopted, pending a §16 amendment gate.
- Split SR-08 (RC-08).

---

## 7. ODF-18-06 — Request-bound Assertions

**Current status:** NON-BLOCKING

**Architectural question**

Must K2-issued assertions be bound to the content of the request, where K2 relays requests?

**Locked constraints**
- [L] §15.10 P2: the assertion is signed, short-lived, audience-bound and bound to a nonce or session. **It is not bound to request content.**
- [L] §15.6 already accepts that a compromised K3 can send any request as the authenticated user.
- [L] §17.2: K4 verifies signature, audience, freshness and single use. Additional checks are not forbidden.
- [L] A-01.

**Threat-model consequence**
- [F] TF-18-08: substitution by K3 is an **accepted §15 residual risk** that §18 now quantifies. REAUTH does not help. R4 approval does.
- Request-bound assertions are **not** part of §15 today.

**Options**

**Option A — Mandatory where K2 relays**
- **What changes:** the adapter contract requires K2 to sign a request digest together with the identity, and K4 to verify it.
- **Security consequence:** closes substitution below R4 wherever K2 relays. Does nothing on proxy routes, where K2 cannot see the request. K3 can still **drop** requests.
- **§15:** NO. It is compatible with P2 and adds strength without changing it. **§16:** NO.
- **§17:** NO. It is an additional K4 verification that can be recorded in the adapter contract. It does not alter §17.2's required checks.
- **Downstream:** YES (Platform Adapter gate).

**Option B — Optional adapter hardening**
- **What changes:** the capability is declared per adapter and shown for compatibility.
- **Security consequence:** protection varies by adapter. RR-06 remains wherever it is absent.
- **§15:** NO. **§16:** NO. **§17:** NO.

**Option C — Do not pursue**
- **Security consequence:** RR-06 is accepted as §15 already accepts it.
- **§15:** NO. **§16:** NO. **§17:** NO.

**Where this belongs:** the Platform Adapter gate. Not §15.

**Recommended owner disposition**

Option A where the relay path exists. Note the interaction with ODF-18-01: origin isolation may determine whether relay is the available path.

**Owner decision**

> OWNER DECISION REQUIRED

**Post-decision consequence**

Relabel TH-06/RR-06 as a §15-accepted residual risk (RC-10), and record the chosen adapter obligation (SR-18/TQ-05).

---

## 8. ODF-18-07 — Off-host Audit Export

**Current status:** NON-BLOCKING, but it carries an **amendment-sensitive dependency** (see "Hidden dependency" below).

**Architectural question**

Is off-host export of the K8 journal and K4 audit (including a record of legitimate anchors) required in v1, supported, or deferred? **Which component performs the export?**

**Locked constraints**
- [L] T-12: K8 is written by K6 and is root-owned. C can only read it.
- [L] T-23: K7 is accessible only to identity C.
- [L] §15.4 item 6: K4 and K6 have no default egress. Any required egress must be a **declared K6 Operation**.
- [L] §16.1.3: there is **no general network operation**. Egress exists only to allowlisted package sources and to loopback, unix or D-Bus endpoints.
- [L] T-31: no external listeners.

**Four properties that must not be confused** [F]
- **Integrity while the writer is honest:** provided locally by access control.
- **Tamper evidence against a compromised writer:** only if the evidence anchor lies outside that writer's control. Local tamper evidence **does not** protect against K6 or root for K8, or against C for K4 audit.
- **Survival of evidence through a root or K6 compromise:** only for records exported **before** the compromise.
- **Attribution of approvals:** requires an off-host record of which anchors are legitimate (TF-18-11).

**Hidden dependency** [F]

Export requires egress, and **the locked architecture provides no path for this egress**:
- (i) A new K6 export Operation would be a §16 vocabulary amendment.
- (ii) K4 egress would contradict §15.4 item 6.
- (iii) A host-level export facility administered by root **outside the SCC runtime** needs no amendment. [M] It may still need an SCC-produced artifact that it can read, which is a §19 matter. Reading K7 or K8 as root is outside SCC's boundary and does not breach T-23, which constrains SCC identities.

**Options**

**Option A — Required in v1**
- **What changes:** §19/§21 define what is exported, and the anchor-legitimacy record is exported too. The owner must also choose mechanism (i), (ii) or (iii).
- **Security consequence:** SC-17 can claim that records exported before a compromise remain tamper-evident, and that approval attribution is checkable against the off-host anchor record.
- **§15:** YES only under mechanism (ii). **§16:** YES only under mechanism (i). **§17:** NO.
- **Downstream:** §19, §21, §22.

**Option B — Supported but optional**
- **What changes:** the same as Option A, but deployments opt in.
- **Security consequence:** SC-17 becomes conditional on export being enabled. Without export, RR-03 fully applies, including to attribution.
- **Amendments:** same dependency on mechanism as Option A.
- **Downstream:** §19, §21, §22.

**Option C — Deferred**
- **Security consequence:** SC-17 must be reduced to "integrity while the writer is honest, plus detection of accidental corruption". No evidence survives a root or K6 compromise. Approval attribution depends entirely on root being honest.
- **§15:** NO. **§16:** NO. **§17:** NO.

**Recommended owner disposition**

At least Option B, using mechanism (iii). That keeps §15.4 and §16.1.3 unchanged. The owner should record the mechanism choice together with the option.

**Owner decision**

> OWNER DECISION REQUIRED (option **and** export mechanism)

**Post-decision consequence**
- Rewrite SC-17 according to the chosen option.
- Scope T-18-09 and SR-12 (RC-13).
- Weaken SC-09 for displacement by volume (CLF-18-03).
- Record the mechanism and any amendment it triggers.
- Assign SRF-18-11 (the anchor record).

---

## 9. ODF-18-08 — Approval-key Custody

**Current status:** NON-BLOCKING for the §18 lock. It blocks enabling R4 (TQ-01).

**Architectural question**

What is the minimum custody class for approver keys in v1?

**Locked constraints**
- [L] A-20/A-22: approval requires both a Grant and an anchor, and the approval tool runs outside K1–K4.
- [L] §17.9: a key stored on the host gives no protection against a root-equivalent host or platform.
- [L] T-18-03/SR-05 (candidate): no key in K1–K5 or the platform. This excludes Case B.
- [L] Owner Decision 2: package writes are R4, so approval is needed operationally.

**Threat-model consequence by custody class** [F]

| Protection against | Case A (on host, not readable by W/C/I; tool not running as W/C/I) | Case C (independent, off-host) |
|---|---|---|
| Non-root SCC compromise (K3, K5, tenant) | Yes | Yes |
| K4 compromise (for flagged R4) | Yes | Yes |
| K6 compromise | No: host compromise; key readable | Key secrecy: yes. Host: no. |
| Root compromise | No | Key secrecy: yes. Host: no. |
| Approval authenticity (no forgery without the approver) | Only while root is honest | Yes |
| Approval attribution (key → Principal) | Depends on anchor-set integrity (root) | **Still** depends on anchor-set integrity, unless an off-host anchor record exists (ODF-18-07) |

Off-host custody **never** protects the host itself.

**Options**

**Case A — The key may reside on the SCC host** (Case C also permitted)
- **Claims to scope:**
  - SC-18 applies only to keys held in Case C.
  - SC-12 is "valid while root is honest".
  - SC-06, as applied to approvals: a stolen host key still works until root removes its anchor. Disabling the approver's Principal stops use at K4 but not at K6.
- **§15:** NO. **§16:** NO. **§17:** NO.
- **Downstream:** §22 tool placement (must not run as W, C or I).

**Case C — The key must reside in an independent off-host environment** that meets all five §18.7.2 conditions
- **Claims:**
  - SC-18 holds generally.
  - SC-12 holds for authenticity. Attribution still depends on ODF-18-07.
  - SC-06 for approvals: the key cannot be stolen from the host, so the risk left after revocation is limited to keys compromised off-host.
- **Consequence:** operational burden, amplified by Owner Decision 2.
- **§15:** NO. **§16:** NO. **§17:** NO.
- **Downstream:** §22.

**Recommended owner disposition**

Either choice is architecturally consistent, provided the claims are scoped as shown. Case A with SR-06 claim discipline keeps R4 operable for single-administrator hosts. Case C is required for any claim about approval authenticity that survives a root compromise.

**Owner decision**

> OWNER DECISION REQUIRED

**Post-decision consequence**

Record the custody minimum, scope SC-06, SC-12 and SC-18 accordingly (RC-14), and link TQ-01.

---

## 10. ODF-18-09 — Platform-configuration Writes

**Current status:** NON-BLOCKING, provided Option A is recorded.

**Architectural question**

How are WRITE entries that target parent-platform configuration, or any consumer that can execute commands, prevented from escaping `executable_semantics` and `approval_required`?

**Locked constraints**
- [L] §16.2: `executable_semantics` covers content that can make **the Security System** execute commands.
- [L] X-10: every `executable_semantics` entry MUST declare a validator.
- [L] §17.5.3 criterion (a): using an `executable_semantics` WRITE entry makes a capability **R4 automatically**.
- [L] A-23.
- [L] §15.5: the platform is root-equivalent.
- [L] §16.2.2: Platform Services has its own declaration kind.

**Threat-model consequence**
- [F] TF-18-10: an unflagged platform-configuration write lets a compromised K4 (non-root C) reach root without approval. That breaks the §17.21 picture.
- [F] The gap is in **flagging**, not in **tiering**. Once an entry is flagged, §17 already derives R4.

**Hidden consequence** [F]

Under Options A and B, X-10 applies. A flagged platform-configuration write **must declare a validator profile**. Where no suitable validator exists, the capability cannot be offered. That is fail-closed and consistent, but the owner should be aware of it.

**Options**

**Option A — Interim §18 authoring rule**
- **What changes:** platform-configuration writes, and writes whose consumer can execute commands, MUST be declared `executable_semantics` and `approval_required`.
- **What does not change:** §16's text. Authors may always flag more strictly than §16 requires.
- **Security consequence:** closes the gap for correctly authored releases. Criterion (a) then derives R4, and A-23 applies. Residual risk RR-12 remains for authoring errors.
- **§15:** NO. **§16:** NO. **§17:** NO.
- **Downstream:** release validation (§22), consistent with ODF-18-03.

**Option B — Amend the §16.2 definition**
- **What changes:** `executable_semantics` is redefined as content consumed by any root-equivalent or command-executing component.
- **Security consequence:** the same as Option A, but carried in the locked definition. It also widens what ODF-18-03 Option B checks.
- **§16:** YES (optional clarification). **§15:** NO. **§17:** NO.

**Option C — Reopen §17 with a new R4 criterion**
- **Security consequence:** **does not fix the gap.** The failure is an unflagged entry, and an entry nobody flagged also cannot be tier-derived from K11 data. It would also reopen a locked gate.
- **§17:** YES.
- **Architectural consequence:** undesirable, and ineffective on its own.

**Is Option A sufficient for §18 lock?** Yes. It is coherent without any amendment.

**Recommended owner disposition**

Option A now. Option B as the durable clarification. Option C is not recommended.

**Owner decision**

> OWNER DECISION REQUIRED

**Post-decision consequence**
- Record SRF-18-09 and the invariant as normative.
- Add TF-18-10 to the matrix.
- Extend RR-12 to cover classification accuracy.
- Record the X-10 validator consequence.
- If Option B: record OD-6 as adopted, pending a §16 amendment gate.

---

## 11. Cross-Decision Dependencies

| Dependency | Effect |
|---|---|
| ODF-18-01 → SC-16, §15.6, SR-01 | Determines whether SC-16 is a defence-in-depth claim (A), a critical conditional claim (B), or per-adapter (C) |
| ODF-18-01 ↔ ODF-18-06 | The origin model may decide whether the K2 relay path exists. Request-bound assertions only work with relay. |
| ODF-18-02 → SC-03, RR-07 | Covered in §3 |
| **ODF-18-02 ↔ ODF-18-08** | **Hidden.** Case C custody (for example, one off-host token per approver) makes it *more* likely that one key is anchored on many hosts. That raises the importance of ODF-18-02. Case A keeps keys per host by default but does not guarantee it. |
| ODF-18-02 ↔ ODF-18-07 | An off-host anchor record could *detect* SR-07 violations (the same key anchored on several instances), even though K6 cannot. |
| ODF-18-03 → A-23, K6 role | A-23 is unchanged. Option B adds a validation step at declaration load, not authorization. |
| **ODF-18-03 ↔ ODF-18-09** | ODF-18-09 Option B widens what ODF-18-03 Option B's `executable_semantics` check covers. Both depend on flag accuracy (RR-12). |
| ODF-18-04 → SR-09, §12 | Option C makes Host Environment compatibility a security input |
| ODF-18-05 → X-13 | Option B adds a preventive control. X-13's outcome guarantee remains either way. |
| ODF-18-06 → §15 K3 residual | Narrows RR-06 in relay deployments only. It never removes RR-06 in general. |
| **ODF-18-07 → §15.4 / §16.1.3** | **Hidden.** The export mechanism may itself need an amendment. Mechanism (iii) avoids one. |
| ODF-18-07 → SC-09, SC-17, SC-12 attribution | Covered in §8 |
| ODF-18-08 → SC-06 (approval revocation window), SC-12, SC-18 | Covered in §9 |
| ODF-18-09 → the compromised-K4 boundary, RR-12, X-10 | Covered in §10 |

No dependency requires new architecture beyond what each individual decision already identifies.

---

## 12. Owner Decision Matrix

| Decision | Current status | Options | Recommended disposition | Requires §15 amendment? | Requires §16 amendment? | Requires §17 amendment? | Blocks §18 lock? |
|---|---|---|---|---|---|---|---|
| ODF-18-01 Presentation origin | BLOCKING | A isolation / B same-origin / C per-adapter | A (C if A is infeasible) | **YES** (any option) | NO | NO | **YES** |
| ODF-18-02 Cross-instance replay | NON-BLOCKING | A §16 instance binding / B SR-07 / C accept | A | NO | OPTIONAL (A) | NO | NO |
| ODF-18-03 R4 flag enforcement | NON-BLOCKING | A release only / B + K6 load check | A required; B recommended for (b) | NO | OPTIONAL (B) | NO | NO |
| ODF-18-04 Credential arguments | NON-BLOCKING | A authoring / B K6 prohibition / C Host Environment conditional | B, or C with K6 enforcement | NO | OPTIONAL (B; C if K6-enforced) | NO | NO |
| ODF-18-05 WRITE ownership | NON-BLOCKING | A authoring / B K6 path ownership | B (A interim) | NO | OPTIONAL (B) | NO | NO |
| ODF-18-06 Request-bound assertions | NON-BLOCKING | A mandatory for relay / B optional / C none | A where relay exists | NO | NO | NO | NO |
| ODF-18-07 Off-host export | NON-BLOCKING | A required / B optional / C deferred, **plus mechanism (i)/(ii)/(iii)** | B with mechanism (iii) | PENDING OWNER (only with mechanism ii) | PENDING OWNER (only with mechanism i) | NO | NO |
| ODF-18-08 Key custody | NON-BLOCKING (blocks R4 enablement) | Case A minimum / Case C required | Either, with claims scoped | NO | NO | NO | NO |
| ODF-18-09 Platform-configuration writes | NON-BLOCKING with A recorded | A authoring / B §16.2 definition / C §17 criterion | A now; B later; not C | NO | OPTIONAL (B) | NO (only C) | NO, if A is recorded |

All nine owner decisions: **PENDING OWNER**. None is approved.

---

## 13. §18 Lock Conditions

§18 may become **PASS** only when **all** of the following hold:

1. **ODF-18-01 is decided** (A, B or C).
2. **The resulting §15 amendment is explicitly authorized** before §18 locks. The exact text:
   - **A:** constrain §15.18 OQ-1 and add a presentation-isolation invariant.
   - **B:** rewrite the §15.6 compromised-K3 bound and qualify the §15.15 K3 row.
   - **C:** revise §15.6 and OQ-1 for two presentation classes, and add an invariant requiring a declared TCB consequence.
3. **ODF-18-02 to ODF-18-09 each have a recorded disposition.** For ODF-18-07 this includes the export mechanism. For ODF-18-09, at least Option A.
4. **No §16 amendment is implied.** Every chosen §16 amendment (OD-1 to OD-6) is recorded as *pending a separate §16 amendment gate*. §18 records only the interim rule that applies until that gate completes.
5. **The canonical §18 incorporates RC-01 to RC-21** as applicable, plus the post-decision consequences recorded above.
6. **Claims are within guarantees.** Every SC-* respects §15–§17 and the owner's choices. In particular:
   - SC-03 is scoped per ODF-18-02;
   - SC-09 and SC-17 per ODF-18-07;
   - SC-06, SC-12 and SC-18 per ODF-18-08;
   - SC-16 per ODF-18-01.
7. **Residual risks are classified explicitly.** This includes RF-18-05 (Plan-level integrity), RF-18-06 (depending on ODF-18-01), and the split of RR-08. None may be represented as a protection.
8. **Identifier integrity.** Every cross-reference defect in the forensic review §9 is corrected.
9. **No boundary reassignment.** K4 remains the authorization and policy component, K6 the enforcement component, K11 the source of declarations and anchors, and K8 the execution evidence. None of the adopted mitigations moves responsibility between components without a recorded amendment.

---

## 14. Recommended Next Gate

1. **Owner decision recording.** The owner records a disposition for ODF-18-01 to ODF-18-09, including the ODF-18-07 export mechanism.
2. **§15 amendment gate (narrow).** Only the change required by the ODF-18-01 decision, plus the ODF-18-07 change if mechanism (ii) is chosen.
3. **§16 amendment gate (only if any are chosen).** Batch all adopted optional amendments (OD-1 to OD-6, and mechanism (i) under ODF-18-07) into one §16 amendment pass with its own compatibility audit. If none are chosen, skip this step.
4. **Canonical §18 rewrite.** Apply RC-01 to RC-21 and the recorded decision consequences.
5. **§18 lock gate.** Verify the lock conditions in §13, then PASS.
6. Only after that: **§19 — Persistence, Secrets & Data Lifecycle**, which inherits SR-12 to SR-17, SRF-18-11, and the ODF-18-07 outcome.
