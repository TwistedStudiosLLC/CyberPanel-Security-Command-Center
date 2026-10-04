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

# Gate Consolidation Review — DEC-092 convening (R-1, R-2, R-3)

**Nature of this document.** Read-only consolidation of the three candidate deliberations. It is gate work only and
not authority:
- not an [OI];
- not a DEC;
- not a closure determination;
- not a register change.

**Authority.**
- Locked architecture and adopted decisions control.
- The deliberation files and the evidence packet are evidence of gate work only.

**Inputs.** All are in the scratchpad:
- `gate-r1-deliberation-v1.md`
- `gate-r2-deliberation-v1.md`
- `gate-r3-deliberation-v1.md`
- `gate-evidence-packet-v1.md`

Sources: DEC-091, DEC-092, and the locked P2/K3, §15, §17, §19, §21 and §22 documents.

**Repository state at start.**
- HEAD `185e9e96e8bc7e668c6be6ec9c9c203d723da5de`; working tree clean.
- Register row (register:227): "OPEN (DEC-092) — not a §17 amendment gate; §17 remains LOCKED (DEC-064)".
- Remote branch `9d24121eca99b8941b366edee92bed959ae100cf`.

---

## Consolidation table

Column C summarises each deliberation's determination table, plus the evidence-gap [U]s listed below the table.
The "Adoption risk" column is raised by this consolidation, not by the deliberations.

| Matter | Locked conclusion (A) | Candidate inference (B) | Remaining [U] (C) | Dependencies | Adoption risk |
|---|---|---|---|---|---|
| **R-1** (D91-2(a), K4 side) | [L] §P.3.1: `audience` is "identifying the SCC instance the assertion is for". [L] §15.6: "audience-bound"; §15.10: "audience-bound (SCC)". [L] §17.2, §17.22 step 1: K4 verifies audience. [L] §P.4.1: K4 rejects "wrong `audience`". No locked text defines an SCC-instance identifier. | (i) K4 compares against a value designating the SCC instance on whose behalf it verifies (§P.3.1 + §P.4.1 + §17.2 / §17.22). (ii) The expected value is not taken from the presented assertion's own `audience`, nor from other locked request-path elements (§P.4.1 + §P.7.1 / §P.7.3 + §P.8). (iii) If the expected value cannot be established, no authorization proceeds for that assertion (A-01 level; not classified as a step-1 failure). | The concrete value and form. Where and how K4 obtains it. Creator, owner, provisioning, storage, lifecycle, rotation. DC-18 status. B2 record and P2 result when unavailable. Whether K4 belongs to exactly one SCC instance (relation to ODF-18-02). | K2 issuer side (D91-3): coupling only, "constrain, not assign"; no ordering. OD19-01 / DC-18: [U] and excluded (D92-3). §19 route D91-6: excluded. | (i) assumes K4 belongs to exactly one SCC instance [U]. Any later concrete value would constrain the issuer side. "Cannot be determined" on the value and source leaves R-1 operationally open. |
| **R-2** (D91-2(b)) | [L] §P.4.2: "K4 records `assertion_id` for the assertion's validity period and rejects any second use". [L] §P.4.3: "Replay rejection is K4's; K3 performs none and holds no replay state". [L] §P.3.4: validity ≤ 60 s. [L] §P.7.6: session-establishing assertion "consumed". Runtime-only text (§P.7.6, D88-2(f)) covers sessions only. | (i) The validity period is the minimum span in which a second use must be detectable (§P.4.2 + §P.4.1). (ii) If prior use cannot be determined, no authorization proceeds (§17.22 + §17.16 + §17.2 + A-01; not classified as a step-1 failure). | Survival across K4 restart, host restart, K4 reinitialization, K7 restore and recovery. Durable vs volatile. Upper bound or removal. §19 class, owner, storage domain. B2, `failure_reason` and P2 result when prior use is unknown. Scope of §15.10 "where applicable". DC-18 status. | No locked connection to K7, restore generations, SD-K7 or §22 recovery. §19 route D91-6: excluded (D92-3). OD19-01: [U], excluded. | The R-2 table phrase "keyed by `assertion_id`" paraphrases "records `assertion_id`". An adopter could read it as a storage structure. Inference (i) could be misread as a retention ceiling or as restart survival. Neither is stated. |
| **R-3** (D91-2(c)) | [L] §17.22 step 1 names four assertion checks (signature, audience, freshness, single use), then Binding and Principal. [L] §P.4.1 attributes the five conditions to step 1 collectively. [L] §P.6.1: `key_id` is accepted only while K4 holds "the corresponding active verification material". [L] §21.7, §21.14: `failure_reason` = "the §17.22 step-1 check that failed". | not yet valid → **freshness** (weakest; relies partly on the ordinary meaning of "freshness"). Unknown `key_id` → **signature**. Retired `key_id` → **signature** (a freshness reading was considered and is weaker). All are inferred; none is explicit. | No explicit per-condition attribution. Step-1 check set not stated to be closed. Clock reference and skew. Multi-failure rule. | None on R-1, R-2, C-1 or OD19-01 for the classification itself. | On an explicit-text-only standard, all three are undetermined. Classification A carries the most risk. Raised by this consolidation, not by R-3: whether temporary unavailability of verification material counts as "unknown `key_id`" (H-3). |

---

**Additional evidence-gap [U]s not in the determination tables:**
- **R-1:** comparison semantics (gap 2); whether more than one SCC instance can exist (gap 6).
- **R-2:**
  - whether DEC-047 R17c's recovery condition before "authorization-dependent work" covers step-1 verification (§8,
    T-5, gap 2);
  - the format of `auth_context_ref` ("format P2", not defined in P2/K3) (T-3, gap 8);
  - clock reference and skew (gap 7).

## Consolidation questions

1. **Does R-1 conflict with R-2?** No. R-1 concerns the comparison value for `audience`. R-2 concerns the `assertion_id`
   replay record. Each is a distinct step-1 check, and neither output states anything about the other's state.
2. **Does R-1 hide an assumption about replay persistence?** No. R-1 leaves the expected value's storage and lifecycle
   [U]. It assumes nothing about the replay record.
3. **Does R-2's minimum detection window hide an assumption about audience lifetime?** No. R-2's window is the
   assertion's validity period (§P.3.4). It is unrelated to the lifetime of the expected `audience` value, which R-1
   leaves [U].
4. **Does R-3 depend on R-1 or R-2?** No. R-3 classifies only not yet valid, unknown `key_id` and retired `key_id`. It
   does not classify "wrong `audience`" or second use, and its reasoning cites neither deliberation.
5. **Does any output accidentally depend on OD19-01?** No.
   - R-1 and R-2 mark DC-18 status [U] and excluded.
   - R-3 cites §P.6.1 (K4 holds verification material) but states that where the material is stored does not alter
     the classification.
   - See H-3 for an unaddressed edge.
6. **Does any output accidentally decide the K2 issuer side?** No. R-1 reports a coupling, "constrain, not assign", as an
   observation under D92-9.
7. **Does any output accidentally establish a §19 data classification?** No. R-1 and R-2 mark classification [U] and
   excluded (D92-3).
8. **Does any output accidentally establish a storage or persistence technology?** No. Two wording risks are noted: R-2's
   "keyed by" (table above) and R-2 inference (i).
9. **Does any output accidentally close the §17.22 check set?** No.
   - R-3 states that the set is not stated to be closed.
   - R-1 (unavailable expected value) and R-2 (unknown prior use) both stop at the A-01 level and do not classify those
     cases as step-1 failures.
10. **Does any output establish check ordering or multi-failure precedence?** No. R-3 reports the source-stated sequence
    (assertion verification, then Binding, then Principal) and decides no order among the four checks and no
    multi-failure rule.
11. **Does any output establish a serialized `failure_reason` vocabulary?** No. R-3 states that "freshness" and
    "signature" name the §17.22 check and are not serialized strings.
12. **Does any output change the meaning of §21 audit durability?** No. R-2 cites §21.11 ("survives both a K4 process
    restart and a host restart") as applying to audit records only, and expressly does not extend it to the replay
    record.

---

### Cross-Matter Contradictions

No contradiction found.

The C-1 qualifier (§15.10 "single use where applicable") is treated differently across the matters, but the treatments
do not contradict each other:
- R-3 finds that C-1 does not affect its classification.
- R-2 leaves C-1's effect on the record's scope [U].

The two deliberations ask different questions.

### Hidden Assumptions

| # | Assumption | Needed for | Classification |
|---|---|---|---|
| H-1 | A verifying K4 belongs to exactly one SCC instance | R-1 inference (i) | **Unresolved.** R-1 marks it [U]. No locked text states it; §P.9 points to ODF-18-02, which is OPEN. Not needed by R-2 or R-3. |
| H-2 | Out-of-window assertions are rejected under §P.4.1 independently of the replay record | R-2 inference (i). Consistent with R-3 classification A. | **Supported** by [L] §P.4.1, which rejects "not yet valid" and "has expired" unconditionally. Its use to bound the detection window is candidate inference. |
| H-3 | "Unknown `key_id`" means K4 holds no corresponding verification material, as distinct from that material being temporarily unavailable | Bears on the scope of R-3 condition B, alongside R-1 and R-2's A-01-level unavailability inferences. It does not affect the classification itself. Raised by this consolidation, not by R-3. | **Unresolved.** R-3 infers "unknown" from §P.6.1. Whether temporary inability to read verification material counts as "unknown `key_id`", or as a separate unavailability case like those in R-1 and R-2, is not addressed by any output or locked text. It touches OD19-01 territory (storage) without depending on its resolution. |
| H-4 | Unavailability cases (expected `audience` unavailable; prior use undeterminable) are not among the three R-3 conditions | Coexistence of R-1 and R-2's A-01-level inferences with R-3's classifications | **Candidate inference.** They are different conditions in text. Neither R-1 nor R-2 classifies its case as a step-1 failure, so no R-3 classification is affected. |
| H-5 | The "validity" vocabulary means the `issued_at`–`expires_at` window in both R-2 (validity period) and R-3 A (not yet valid) | Consistency of R-2 and R-3 | **Supported** for R-2 by [L] §P.3.1, §P.3.4 and §P.4.1–§P.4.2, and by [DEC] D88-2(c). Its application to R-3 A is candidate inference. The clock reference is [U] in both. |

### Boundary Audit

| Boundary | Result |
|---|---|
| No P2/K3 amendment | Confirmed |
| No §15 amendment | Confirmed |
| No §16 amendment | Confirmed |
| No §17 amendment | Confirmed |
| No §19 amendment | Confirmed |
| No §21 amendment | Confirmed |
| No §22 amendment | Confirmed |
| No OD19-01 resolution | Confirmed. H-3 is an unaddressed edge, not a resolution. |
| No K2 issuer-side decision | Confirmed |
| No implementation authority | Confirmed |
| No storage technology decision | Confirmed. R-2 "keyed by" wording is flagged as a reading risk only. |
| No new [OI] | Confirmed. Every candidate inference is labelled as such, and none is tagged [L], [DEC] or [OI]. |

### D92-10 Status

D92-10's substantive condition (log:9944–9946) is: for each of D92-2 (a)–(c), "either (1) the gate has produced
candidate output, or (2) the gate has reported that the matter cannot be determined within the permitted scope".

| Matter | Candidate output | Cannot-determine report |
|---|---|---|
| (a) R-1 | Yes (determination B) | Yes, for the concrete value and source |
| (b) R-2 | Yes (determination B) | Yes, for restart, restore and durability |
| (c) R-3 | Yes (candidate mapping) | Not used |

**The substantive condition appears satisfied for all three matters.**

D92-10's text continues: "Once that condition is satisfied for all three matters, the convening is complete for the
purposes of this decision, with no further confirmation step, and the register row's status returns to its
pre-convening NOT SCHEDULED status under D92-11; the Stub entry added under D92-11 is retained." D92-11 provides for that return "by a register update citing this
decision".

As instructed:
- This review makes no closure determination and no register update.
- The register row currently still shows OPEN (DEC-092).
- Whether and when the D92-11 register update is made is outside this review.

### Owner Review Package

If the owner later adopts the candidate outputs, in whole or in part, under DEC-091 D91-4 (a new DEC in the DEC-090
D90-1 form), the owner would be:

**Accepting (if adopted):**
- **R-1:**
  - K4 compares `audience` against a value designating the SCC instance on whose behalf it verifies. This rests on H-1,
    which is unresolved.
  - That value is not taken from the presented assertion or from the locked request path.
  - If it cannot be established, no authorization proceeds for that assertion.
- **R-2:**
  - The replay record must allow second-use detection for at least the assertion's validity period (≤ 60 s).
  - If prior use cannot be determined, no authorization proceeds.
- **R-3:**
  - not yet valid → freshness;
  - unknown `key_id` → signature;
  - retired `key_id` → signature;
  - all on the inference standard.

**Rejecting (if not adopted):** the corresponding candidate inference. The [L] text stays as it is in every case.

**Leaving unresolved, whatever is adopted:**
- **R-1:** the concrete expected `audience` value, its form and source; owner, provisioning, storage, lifecycle and
  rotation; DC-18 status; the K2 issuer side (D91-3); H-1.
- **R-2:** survival across K4 restart, host restart, K4 reinitialization and K7 restore or recovery; durable vs
  volatile; upper bound or removal; §19 classification, owner and storage domain; the scope of §15.10 "where
  applicable".
- **R-3:** explicit attribution; whether the step-1 check set is closed; clock reference and skew; multi-failure
  precedence.
- **Raised by this consolidation:** H-3, the scope of "unknown `key_id`" when verification material is temporarily
  unavailable.
- **Common to R-1 and R-2:** B2 record, `failure_reason` and P2 result for the unavailability and unknown-prior-use
  cases.

**Choices only the owner can make:**
- inference standard vs explicit-text-only standard (R-3);
- whether to accept the R-1 inference that rests on H-1;
- whether to address H-3;
- how the R-1 and R-2 cannot-determine parts proceed. That would be by owner decision, or by further gate work: within this
  convening while it remains open, or under a new D91-9 convening after it concludes.

No recommendation is made.
