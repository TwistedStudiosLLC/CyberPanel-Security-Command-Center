> **Document status:** EVIDENCE — NON-NORMATIVE (non-authoritative candidate evidence)
> **Authority category:** Evidence of gate work only (outside the DEC-023 hierarchy). Candidate output of the
> DEC-092 convening of the §17/K4 Architecture Gate on DEC-091 D91-2 (a)–(c). **Not SCC architecture and not an
> owner decision.** Gate output becomes an owner interpretation only to the extent an owner decision records it
> under DEC-091 D91-4 (DEC-092 D92-5, D92-7).
> **Source:** Prepared during the DEC-092 convening against HEAD `185e9e96e8bc7e668c6be6ec9c9c203d723da5de`; the
> convening concluded under DEC-092 D92-10 (commit `70b1d1aa14f5d754a567d6f772bd09c00ca1d486`). The text below this
> header is reproduced verbatim from the session working copy; references in it to "the scratchpad" mean that
> working copy, and references to "the task" mean the owner's instructions for that step of the convening.
> **Normative:** No. Locked architecture and adopted owner decisions control. Nothing here adopts, amends, assigns
> or decides anything.

# Gate Deliberation — R-1 (K4 side) — Candidate Determination

**Status:** This is candidate gate output under DEC-092 D92-5 and D92-7.
- It has no architectural effect.
- It is not an owner decision, an [OI], or locked architecture.
- It takes effect only if the owner records it as a new DEC under DEC-091 D91-4.

**Tags used:**
- **[L]:** directly stated by Category 1 locked text.
- **[DEC]:** established by an adopted owner decision.
- **[U]:** unresolved.
- **"Candidate inference from …":** gate reasoning only.

Line references are cited at HEAD:
- `p2` = `docs/architecture/current/p2-protocol.md`
- `s15` = `current/15-runtime-topology.md`
- `s17` = `current/17-authorization.md`
- `s19` = `current/19-persistence-secrets-data-lifecycle.md`
- `s21` = `current/21-audit-events.md`
- `s22` = `current/22-lifecycle-recovery.md`
- `log` = `decisions/decision-log.md`

## 1. Scope

DEC-091 D91-2(a), admitted verbatim by DEC-092 D92-2(a) (log:9361, 9892): "R-1, K4 side: what K4 compares an assertion's
`audience` against, and how K4 obtains that expected value".

- **Permitted.** DEC-092 D92-4 (log:9905–9908) lets the gate consider and report "a candidate expected `audience` value
  and how K4 obtains it". The gate may not adopt or lock that value, create a final owner decision, modify P2/K3, or
  assign K2's issuer-side behaviour. DEC-092 "selects no `audience` value".
- **Outside this deliberation:**
  - **The K2 issuer side.** It is not assigned and returns to the owner (DEC-091 D91-3, log:9368–9371; D92-3).
  - **R-2 and R-3.**
  - **§19 classification and OD19-01 resolution** (D92-3).
  - **DC-18 material.** Anything determined to be DC-18 assertion-verification material stays in OD19-01 (D91-3).

The R-3 deliberation is prior gate work only and is not relied on here.

## 2. Repository State

| Item | State |
|---|---|
| HEAD | `185e9e96e8bc7e668c6be6ec9c9c203d723da5de` |
| Working tree | Clean (0 entries, including untracked) |
| Remote branch `origin/docs/architecture/19-persistence-secrets-data-lifecycle` | `9d24121eca99b8941b366edee92bed959ae100cf` |
| Register §8 row (register:227) | "§17/K4 Architecture Gate \| OPEN (DEC-092) — not a §17 amendment gate; §17 remains LOCKED (DEC-064) \| Q19-04 (§19.21.1) — not admitted (DEC-092); DEC-091 D91-2 (a)–(c), convened by DEC-092" |
| DEC-091, DEC-092 | CURRENT (log:9138, 9497) |
| Evidence packet | `gate-evidence-packet-v1.md`. Used for organization only, not as authority. |

## 3. Locked Evidence

| # | Source | Text | Tag |
|---|---|---|---|
| A1 | §15.6 (s15:150) | K2 may "issue a short-lived, audience-bound identity assertion" | [L] |
| A2 | §15.10 P2 row (s15:227), in the **Replay** column (header s15:224) | "Assertion short-lived, audience-bound (SCC), nonce/session-bound" | [L] |
| A3 | §17.2 (s17:124–125) | "K4 independently verifies: the assertion's signature, audience, freshness and single use" | [L] |
| A4 | §17.2 (s17:123); A-01 (s17:584) | §17.2: "There is no authorization based on an unverified claim." A-01: authorization only for a Principal "resolved from a K4-verified Authentication Context" | [L] |
| A5 | §17.22 step 1 (s17:549) | "Verify the K2 assertion: signature, audience, freshness, single use. … On any failure, **deny**." | [L] |
| A6 | P2/K3 §P.2 (p2:24, 34, 44) | Restates A1, A2 and A3 as locked architecture | [L] |
| A7 | P2/K3 §P.3.1 (p2:61) | "`audience`, identifying the SCC instance the assertion is for [L §15.10 P2 "audience-bound (SCC)"]" | [L] (DEC-088 locked text) |
| A8 | P2/K3 §P.3.1 (p2:57–58) | A separate field: "`platform` = (`platform_adapter_id`, `platform_instance_id`)". Together with `subject` it forms the Platform Identity Binding tuple (s17:86) | [L] |
| A9 | P2/K3 §P.4.1 (p2:79) | "K4 rejects an assertion that … carries the wrong `audience`" | [L] |
| A10 | P2/K3 §P.5.4 (p2:96) | `UNAUTHENTICATED` for "any §17.22 step-1 failure" | [L] |
| A11 | P2/K3 §P.7.1, §P.7.3 (p2:115–120) | The P3 envelope carries "the relayed request, the unmodified assertion or SCC session token, and, for state-changing requests, the request ID". K3 "adds only its own peer identity, which the OS establishes". | [L] |
| A12 | P2/K3 §P.8 (p2:148–149); §15.6 | "K2 → K3 → K4 … K2 has no path to K4, K5 or K6" | [L] |
| A13 | P2/K3 §P.11 criterion 3 (p2:174); DEC-088 D88-6(3) | The assertion "supports every §17.22 step-1 check (signature, audience, freshness, single use)" | [L] / [DEC] |
| A14 | "SCC instance" elsewhere: §21.4 (s21:62), §21.5 (s21:69), §19 S19-08 (s19:390), §22.3 (s22:68) | The term is used ("unique within the SCC instance", etc.). None of these defines an identifier, value or representation. | [L] |
| A15 | §19.7 (s19:166–191) | No data class names an expected `audience` value. DC-18 is "Assertion verification material", OPEN under OD19-01. | [L] |
| A16 | DEC-080 D80-2 (log:5962–) | "audience binding" is P2 scope | [DEC] |
| A18 | P2/K3 §P.9 (p2:162) | "Cross-instance approval replay (instance identity in approvals) \| ODF-18-02 / KF-04 (§18, conditional)". This points to a Category 4 §18 item (register: ODF-18-02 **OPEN**), whose owner-decision-gate material discusses a possible "SCC instance identity held by K6 in root-owned storage" (open/18-threat-model/18-owner-decision-gate.md:159). That material is not relied on. | [L] (pointer only); Category 4 content |
| A19 | P2/K3 §P.9 (p2:158) | "Assertion-verification material storage and provisioning \| OD19-01, DEC-051 R01b" | [L] |
| A17 | DEC-091 §4 R-1 [U]; §7 | "The concrete value; its creator, owner, storage, provisioning and lifecycle; how K4 obtains the expected value; how K2 obtains the value it places." "[U] Whether any part of R-1 or R-2 is DC-18 material is not decided". | [DEC] |

## 4. R1-A: Semantic Meaning of `audience`

- **[L] A7:** `audience` identifies "the SCC instance the assertion is for".
- **[L] A1:** §15.6: K2 may issue an "audience-bound identity assertion".
- **[L] A2:** §15.10: "audience-bound (SCC)". The phrase appears in the P2 row's Replay column.
- **[L] A3, A5, A9:** K4 verifies the audience and rejects an assertion carrying the "wrong" `audience`.
- **Answer:** the locked text establishes the **meaning** of the field: it designates the SCC instance the assertion is
  for. It establishes no value.
- **Candidate inference from A7 + A9 (+ A3/A5):**
  - `audience` designates the SCC instance the assertion is for (A7).
  - K4 is the verifier (A3, A5) and rejects a "wrong" `audience` (A9).
  - So the `audience` K4 accepts as right is the one designating the SCC instance on whose behalf that K4 verifies.
  - This is inference. No locked sentence says "the K4's own SCC instance".
  - It also assumes that a verifying K4 belongs to exactly one SCC instance. That assumption is not locked [U].
  - The routing path K2 → K3 → K4 (A12) is not relied on here. It says how assertions travel, not which instance K4
    belongs to.

## 5. R1-B: Expected Audience Value

- **Answer:** No. **Undetermined within current locked evidence.**
- **[L] A7** defines what the value means, not what it is.
- **[L] A2:** "(SCC)" describes the binding. It is no value.
- **[L] A14:** no locked text defines an SCC-instance identifier.
- **[L] A8:** `platform_instance_id` is a separate field of the Platform Identity Binding tuple (§17.1.3, s17:86). No
  locked text equates it with the SCC instance, so it is not a source for the value.
- **No other source.** The locked text never names a "verifier-expected" value as a separate object. The issuer and
  verifier split appears in DEC-091 D91-2(a), D91-3 and §4, and in DEC-092 D92-2, D92-3, D92-4 and D92-9 [DEC].

## 6. R1-C: How K4 Obtains It

- **Answer:** No. The locked architecture does not establish where or how K4 obtains the expected value. **Undetermined
  within current locked evidence.**
- **Candidate inference from A9 + A11 + A12 (+ §P.8 "does not mint or alter identity") — a negative constraint only:**
  - The expected value cannot be read from the presented assertion's own `audience` field. Comparing that field against
    itself could never yield "wrong `audience`" (A9).
  - The locked P3 envelope carries only:
    - the relayed request;
    - the unmodified assertion or token;
    - the request ID;
    - K3's OS-established peer identity (A11).
  - K2 has no path to K4 except through that envelope (A12).
  - No locked request-path element is identified as a source of a verifier-side expected value.
  - Content supplied by the presenter, including the relayed request, is excluded by the same reasoning as the
    self-comparison point. This is consistent with §P.8 (K3 "does not mint or alter identity"), which is cited as consistent, not as a further exclusion.
  - Any source would therefore lie outside the listed envelope elements. This is inference: the locked text is silent
    and places the source nowhere.
- **[U]:** what that source is, and every mechanism behind it. It is not specified anywhere in the locked text.

## 7. R1-D: Ownership / Provisioning

- **Answer:** No. Owner, creator, provisioning, storage, lifecycle and change or rotation are not established
  (A15; A17 [U]).
- **[U]:** whether the expected value is DC-18 "assertion verification material".
  - If it is, it stays in OD19-01 (D91-3; DEC-091 §7).
  - This deliberation does not decide it, because OD19-01 resolution is excluded by D92-3.
- **Outside this convening (D92-3):** any §19 data-class, owner or storage-domain assignment is a §19 change under
  D91-6.
- **[L] A19:** assertion-verification material storage and provisioning are routed to OD19-01.

## 8. R1-E: Failure to Obtain Expected Value

- **Answer:** No locked text addresses this case specifically [U].
- **Candidate inference from A3 + A4 + A5:**
  - K4 must verify the audience (A3, A5).
  - Authorization proceeds only from a K4-verified Authentication Context (A4).
  - If K4 cannot establish the expected value, it cannot complete audience verification. Under A4, no authorization
    can then proceed for that assertion.
  - This is inference. No locked sentence treats "expected value unavailable" as a step-1 failure. This deliberation
    does not classify it as one.
- **[U]:**
  - whether such a case produces a B2 record, and under which `failure_reason`. That touches the §21 contract and is
    not decided here;
  - whether the P2 result would be `UNAUTHENTICATED` or `UNAVAILABLE` (§P.5.4). That is adjacent to R-3 and not decided;
  - any K4 behaviour other than the per-assertion outcome, such as startup or availability posture.

## 9. R1-F: K2 Issuer-Side Dependency

- **Answer:** No source requires the issuer side to be resolved first.
  - D91-3 states only that the issuer side is unassigned and returns to the owner.
  - DEC-091 and DEC-092 state no ordering.
- **Candidate inference from A9 (a coupling, not an ordering):**
  - K4 accepts only an assertion whose `audience` is not "wrong" (A9).
  - So any concrete K4-side expected value would constrain, though not assign, what K2 must place for its assertions to
    be accepted. Comparison semantics are themselves [U] (gap 2).
- **This coupling is not a scope bar.**
  - D92-4 explicitly permits reporting a candidate expected value, and forbids only *assigning* K2's issuer-side
    behaviour.
  - The coupling is reported to the owner as an observation (D92-9).
  - The semantic K4-side interpretation in R1-A can be reported without the issuer side.

## 10. R1-G: Candidate K4-Side Interpretation

**Yes, partially.** The following can be reported without inventing a value or a provisioning mechanism:

1. **Meaning** [L] A7: the `audience` K4 checks designates "the SCC instance the assertion is for".
2. **What K4 compares against.** *Candidate inference from A7 + A9 (+ A3/A5):* a value designating the SCC instance on
   whose behalf the verifying K4 operates.
   - Its form and content are [U].
   - It assumes, without locked basis, that K4 belongs to exactly one SCC instance [U].
3. **Where it does not come from.** *Candidate inference from A9 + A11 + A12 (+ §P.8):* not from the presented assertion's own
   `audience`, and not from any other element of the locked P2/P3 request path.
4. **If it is unavailable.** *Candidate inference from A3 + A4 + A5:* audience verification cannot complete, and no
   authorization proceeds for that assertion.

**No candidate value is reported.**
- No source defines an SCC-instance identifier (A14).
- Choosing one would require inventing a format, generator, store or provisioning path, which is excluded.
- That lack of evidence is the only ground for reporting no value.
- Any candidate value would also constrain, not assign, the issuer side (R1-F). That is reported as an observation, not
  as a bar.

## 11. Evidence Gaps

1. No locked definition, form or representation of an SCC-instance identifier (A14).
2. No locked expected `audience` value, and no comparison semantics.
3. No locked source, owner, creator, storage, provisioning, lifecycle or change or rotation for the expected value
   (A15, A17).
4. It is undecided whether the expected value is DC-18 material (DEC-091 §7). This is OD19-01 territory (A19), excluded by D92-3.
5. No locked text on K4 behaviour when the expected value is unavailable, beyond the per-assertion inference in R1-E.
6. Whether a verifying K4 belongs to exactly one SCC instance, and whether more than one SCC instance can exist.
   - Locked §P.9 (A18) points to an OPEN Category 4 item on cross-instance approval replay and instance identity
     (ODF-18-02).
   - No locked text settles the question.
   - Raised by this deliberation, not by a source: whether the value is meant to survive SCC reinstall, upgrade, K7
     restore or platform reinstall.

## 12. Conflicts / Tensions

No contradiction was found among §15.6, §15.10, §17.2, §17.22, §P.3.1 and §P.4.1. They are consistent. The tensions
below are recorded and not resolved.

| # | Tension | Sides | Authority | Effect on R-1 |
|---|---|---|---|---|
| T-1 | Granularity | §15.10: "audience-bound (SCC)" | §P.3.1: "identifying the SCC **instance** the assertion is for", citing §15.10 as its basis | Both Category 1 | Not a contradiction: §P.3.1 is the more specific locked text. It still defines meaning, not value. |
| T-2 | Placement of the binding | §15.10 puts "audience-bound (SCC)" in the **Replay** column | §17.22 lists audience as its own step-1 check | Both Category 1 | None for R-1. Recorded so the column is not read as defining a value. |
| T-3 | Issuer vs verifier value | Locked text has one field, `audience`, and the word "wrong" (A9) | DEC-091 D91-2(a) and D91-3 split "what K4 compares … against" from "what K2 places" | Category 1 vs Category 2 | The split is an owner framing. The verifier-expected value is not a locked object. |
| T-4 | Candidate value vs issuer side | D92-4 permits reporting a candidate expected value | D92-4 and D91-3: no assignment of K2's issuer-side behaviour | Category 2, both | A concrete value would constrain, not assign, the issuer side (R1-F). This is not why no value is reported; that is lack of evidence. Reported to the owner as an observation (D92-9). |
| T-5 | Possible DC-18 overlap | §15.12: "Verification material only in K4"; DC-18 OPEN | DEC-091 §7: whether R-1 is DC-18 material is [U] | Category 1 / Category 2 | Unresolved. Outside this convening (D92-3). |
| T-6 | Platform instance vs SCC instance | §P.3.1 `platform_instance_id` (Binding tuple) | §P.3.1 `audience` (SCC instance) | Category 1 | Distinct fields. Equating them would be invention. |
| T-7 | Possible coupling with any SCC/K6-instance identity | §P.9 (A18): ODF-18-02 / KF-04 "instance identity in approvals" | Category 4 §18 material, OPEN | Category 1 pointer / Category 4 | [U]. Not relied on, not decided. Reported to the owner (D92-9). |

- **D91-2(a) permits candidate material.** D92-4 and D92-7 make gate output candidate material. D91-4 requires any
  determination to be recorded by the owner.
- **D92-4 prevents the gate from adopting a value.** It does: "may not adopt or lock that value as architecture".

## 13. Candidate Determination

**B. Only a partial candidate interpretation can be reported. The actual value and source remain undetermined.**

| Portion | Status |
|---|---|
| Meaning of `audience`: designates "the SCC instance the assertion is for" | [L] A7 |
| K4 compares against a value designating the SCC instance on whose behalf it verifies | Candidate inference from A7 + A9 (+ A3/A5). Assumes K4 belongs to exactly one SCC instance [U] |
| The expected value is not taken from the presented assertion's own `audience`, nor from any other element of the locked request path | Candidate inference from A9 + A11 + A12 (+ §P.8) |
| If K4 cannot establish the expected value, audience verification cannot complete and no authorization proceeds for that assertion | Candidate inference from A3 + A4 + A5 (A-01 level; not classified as a step-1 failure) |
| The concrete expected value and its form | [U]: Undetermined within current locked evidence |
| Where and how K4 obtains it | [U]: Undetermined within current locked evidence |
| Creator, owner, provisioning, storage, lifecycle, rotation | [U]. §19 aspects are outside this convening (D92-3, D91-6) |
| Whether it is DC-18 material | [U]. OD19-01 (D91-3), excluded by D92-3 |
| B2 recording, P2 result, or other K4 behaviour when unavailable | [U] |
| Whether K4 belongs to exactly one SCC instance; relation to any ODF-18-02 instance identity | [U] (A18, T-7) |

Option C (cannot be determined) is not chosen, because the partial interpretation above is supportable. On the
concrete value and its acquisition, the gate reports that those parts **cannot be determined within the permitted
scope**:
- The locked evidence contains no identifier.
- Any concrete value or mechanism would require invention.

Those two points are the only determinative grounds. The issuer-side coupling (R1-F, T-4) and the ODF-18-02 pointer
(T-7) are reported to the owner under D92-9 as observations.

## 14. Non-Effects

This candidate output:
- selects no `audience` value and no identifier format;
- decides no source, provisioning, storage, ownership, lifecycle or rotation;
- does not decide or assign the K2 issuer side;
- does not resolve OD19-01 or decide DC-18 status;
- makes no §19 classification;
- does not amend §15, §16, §17, §19, §21, §22 or P2/K3;
- does not decide R-2 or R-3, and does not rely on the R-3 deliberation;
- creates no `failure_reason` value and no B2 behaviour;
- changes no register entry;
- authorizes no implementation;
- is not an [OI], not CURRENT and not LOCKED.

## 15. Owner Adoption Boundary

1. The owner decides whether to accept, reject or partially adopt any row of §13.
2. Adoption is recorded as a new DEC in the DEC-090 D90-1 form with [L], [OI] and [U] determinations (DEC-091 D91-4).
   Locked P2/K3, §17 and §21 are not edited.
   Under D91-5, a determination needing a change to locked text is handled differently by document:
   - P2/K3 or §21 changes return to the owner;
   - §15 and §17 have no amendment path;
   - a §16 change goes only through the §16 Amendment Gate after a D68-D assignment.
   On this candidate, no locked-text change is needed.
3. Gate output becomes [OI] only on that recording (D92-5).
4. A concrete expected value and its source are not in this candidate. The undetermined parts are reported to the
   owner (D92-9). They would need either:
   - further gate work. Within this convening that stays inside D92-3's and D92-4's limits. After the convening closes under
     D92-10, any further gate work needs a new owner convening decision (D91-9); or
   - an owner decision. The issuer side separately returns to the owner under D91-3, and DC-18 / OD19-01 are addressed where relevant (D91-3, D91-6).
5. **Closure (D92-10).** D92-2(a) now has candidate output, including a "cannot be determined within the permitted scope"
   report on the concrete value and source.
   - The convening concludes when each of (a)–(c) has candidate output or a cannot-be-determined report (D92-10).
   - The register row's status then returns to NOT SCHEDULED (D92-11).
6. Implementation requires a separate implementation authorization (DEC-091 §6 item 4). Real verification is blocked by
   OD19-01 (D79-8).
