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

# Gate Deliberation — R-3 — Candidate Determination

**Status:** This is candidate gate output under DEC-092 D92-5 and D92-7.
- It has no architectural effect.
- It is not an owner decision, an [OI], or locked architecture.
- It takes effect only if the owner records it as a new DEC under DEC-091 D91-4.

Prepared read-only at HEAD `185e9e96e8bc7e668c6be6ec9c9c203d723da5de`.

Line references are cited at HEAD:
- `p2` = `docs/architecture/current/p2-protocol.md`
- `s15` = `current/15-runtime-topology.md`
- `s17` = `current/17-authorization.md`
- `s21` = `current/21-audit-events.md`
- `log` = `decisions/decision-log.md`

## 1. Scope

DEC-091 D91-2(c), admitted by DEC-092 D92-2(c): under which §17.22 step-1 check each of these §P.4.1 conditions is
recorded in B2 `failure_reason`:

1. not yet valid;
2. unknown `key_id`;
3. retired `key_id`.

Outside R-3:
- "expired", "wrong `audience`" and "fails signature verification";
- check ordering;
- multi-failure precedence;
- serialization or storage of the reason;
- R-1 and R-2.

## 2. Locked evidence

| # | Source | Text |
|---|---|---|
| E1 | §17.22 step 1 (s17:549) [L] | "Verify the K2 assertion: signature, audience, freshness, single use. Resolve the Binding, then the Principal. Require the Principal to be ACTIVE and the Binding CONFIRMED. On any failure, **deny**." |
| E2 | §17.2 (s17:124–126) [L] | K4 independently verifies "the assertion's signature, audience, freshness and single use" and "Binding and Principal state". |
| E3 | §21.7 (s21:148) [L] | `failure_reason`: "The §17.22 step-1 check that failed". It is Required, on B2. Sensitivity: "no assertion content; no credential". Note: "the checks are §17's". |
| E4 | §21.14 (s21:246, 256) [L] | A failure in §17.22 step 1 "produces one **B2** record per attempt"; "`failure_reason` identifies the step-1 check that failed". |
| E5 | P2/K3 §P.4 heading (p2:77) [L] | "P2 — Freshness, Replay and Single Use". Context only: the heading spans all five §P.4.1 conditions, including audience and signature, so it does not tell them apart. |
| E6 | P2/K3 §P.4.1 (p2:79–80) [L] | "K4 rejects an assertion that is not yet valid, has expired, carries the wrong `audience`, has an unknown or retired `key_id`, or fails signature verification [L §17.22 step 1]." |
| E7 | P2/K3 §P.4.2 (p2:81–82) [L] | "K4 records `assertion_id` for the assertion's validity period and rejects any second use [L §17.22 step 1 "single use"]." |
| E8 | P2/K3 §P.3.1 (p2:62, 64) [L] | The assertion carries `issued_at` and `expires_at`, and "`key_id`, identifying the K2 signing key used (P.6)". |
| E9 | P2/K3 §P.3.4 (p2:71–72) [L] | "`expires_at` − `issued_at` is short and does not exceed a fixed maximum assertion lifetime that K4 enforces". |
| E10 | P2/K3 §P.3.5 (p2:73–75) [L] | "The assertion is signed by K2 with its asymmetric signing key and verified by K4 with verification material only". |
| E11 | P2/K3 §P.6.1 (p2:104–105) [L] | "Each assertion names its signing key by `key_id`. K4 accepts a `key_id` only while K4 holds the corresponding active verification material". |
| E12 | P2/K3 §P.6.2 (p2:106–108) [L] | "the old key remains accepted for an overlap no longer than the maximum assertion lifetime, then is retired". |
| E13 | §15.12 (s15:264) [L] | "Verification material only in K4 (asymmetric so no verifier can mint)". |
| E14 | §15.10 P3 (s15:228) [L] | "K4 enforces assertion freshness and single use where applicable". |
| E15 | DEC-088 D88-2(c) (log:7957–7959) [DEC] | "the validity window from `issued_at` to `expires_at` MUST NOT exceed 60 seconds; the freshness checks and single-use `assertion_id` requirement are unchanged". |
| E16 | DEC-092 D92-2 [DEC] | Matter (c) "is considered against the existing §21 `failure_reason` contract, which is unchanged". |

**Premise used for all three conditions.**
- E6 attributes every listed condition to §17.22 step 1.
- E1 names four assertion-verification checks: "signature, audience, freshness, single use". These are the only assertion
  checks named in locked text.
- The locked text does **not** state that the set of step-1 checks is closed (evidence packet C-2, gap 8).
- R-3 as admitted (D92-2(c)) asks under which *existing* check each condition falls. Each condition is tested against
  these four named checks. No new check or value is considered (E3, E16).
- None of the three conditions is a Binding or Principal-state matter, because each concerns the assertion itself.
- **Elimination is not proof.** Ruling out checks assumes that some existing check fits. DEC-091's own [OI]
  (log:9425–9426) allows for the case where none does: "if no existing check fits, D91-5 applies." Each candidate below
  therefore states its **positive** textual support separately from any elimination.

## 3. Condition A — not yet valid

- **Candidate determination: freshness.**
- **Evidence:** E1, E6, E8, E9, E14, E15. E5 is context only; E7 is used for elimination only.
- **Reasoning from the text:**
  1. "Not yet valid" is a condition on the assertion's validity in time. The assertion's only time-bound validity fields are `issued_at` and `expires_at` (E8, E9).
  2. **Single use** is excluded. The locked text ties "single use" specifically to a second use of a recorded `assertion_id` (E7), not to validity in time.
  3. **Audience** is excluded. The audience check concerns the `audience` field (E6 lists "wrong `audience`" as its own condition).
  4. **Signature** is excluded. The signature check concerns signature verification with verification material (E10), not time.
  5. The remaining named check is **freshness**. Steps 2–4 are elimination only. The positive support is:
     - E15: the validity window from `issued_at` to `expires_at` and "the freshness checks" are stated in the same
       clause. E15 is owner-decision text, used here as support only.
     - E14: §15.10 names assertion freshness as a property K4 enforces. Its time sense rests on the ordinary meaning
       of the word (see Explicitness).
  6. E5 (the §P.4 heading) is not relied on, because it spans all §P.4.1 conditions.
- **Explicitness: inferred, and the weakest of the three.**
  - No locked sentence says "not yet valid is recorded as freshness".
  - Locked text does not define "freshness". The link to a not-yet-valid assertion rests on two things:
    - the ordinary meaning of the word;
    - the juxtaposition in E15, which is owner-decision text.
  - It is therefore partly dependent on the term's ordinary meaning, not on locked text alone.
- **Competing classifications in locked text:** none found.
  - §17 also uses "freshness" outside the step-1 assertion check (s17:103, 129, 259/560, 324–327, 347): the Binding
    freshness rule, REAUTH / `AUTH_FRESH` and Plan freshness (`PLAN_MAX_AGE`).
  - None is a step-1 assertion check, so none competes. All of them are time-bound, which is context only.
- **C-1 dependency:** none.
  - E6 states the rejection unconditionally: "K4 rejects an assertion that is not yet valid".
  - Whatever "where applicable" in E14 qualifies, it does not alter which check a not-yet-valid rejection belongs to.
- **§21 change required:** no. The determination records the existing check "freshness" under E3 and E4.
- **P2/K3 change required:** no.
- **Independent of R-1 and R-2:**
  - Yes for R-1: no `audience` value is involved.
  - Yes for R-2: the replay record governs single use, not validity in time.
- **Unresolved dependencies:** none for the classification. Outside R-3 and not decided here:
  - the clock reference and skew for "not yet valid" (evidence gap 5);
  - how "not yet valid" is computed.

## 4. Condition B — unknown `key_id`

- **Candidate determination: signature.**
- **Evidence:** E1, E6, E8, E10, E11, E13.
- **Reasoning from the text:**
  1. `key_id` identifies "the K2 signing key used" (E8).
  2. The assertion is "verified by K4 with verification material only" (E10, E13).
  3. K4 accepts a `key_id` "only while K4 holds the corresponding active verification material" (E11).
  4. (Inferred from E11.) An unknown `key_id` is therefore one for which K4 holds no corresponding verification material.
  5. Among the four named checks, only the signature check involves the signing key and verification material.
  6. Audience, freshness and single use concern other assertion fields (E6, E7, E9).
- **Explicitness: inferred.**
  - No locked sentence says "unknown `key_id` is recorded as signature".
  - §P.4.1 lists "unknown or retired `key_id`" separately from "fails signature verification". That list is a list of rejection conditions, not of checks. It also lists "not yet valid" and "has expired" separately. So the separate listing neither confirms nor excludes the classification. This is an illustration only and decides nothing about "has expired", which is outside R-3.
- **Competing classifications in locked text:** none found. No locked text relates `key_id` to audience, freshness or single use.
- **Positive support, independent of elimination:** the chain E8 → E10 → E11 → E13 ties `key_id` to the verification
  material used for signature verification.
- **C-1 dependency:** none. E14's qualifier concerns freshness and single use, not signature.
- **§21 change required:** no. The existing check "signature" is used.
- **P2/K3 change required:** no.
- **Independent of R-1 and R-2:** yes for both.
- **Independent of OD19-01:** yes. Where verification material is stored (OD19-01) does not alter which check depends on it.
- **Unresolved dependencies:** none for the classification.

## 5. Condition C — retired `key_id`

- **Candidate determination: signature.**
- **Evidence:** E1, E6, E10, E11, E12, E13.
- **Reasoning from the text:**
  1. A key "is retired" after its overlap ends (E12).
  2. K4 accepts a `key_id` only while it holds the corresponding **active** verification material (E11). (Inferred from E11 and E12.) After retirement, the key's verification material is no longer active.
  3. As with Condition B, the failing step is acceptance of the verification material used for signature verification (E10, E11). Among the four named checks, that is the signature check.
- **Explicitness: inferred,** on the same basis as Condition B.
- **Competing reading considered: freshness, because retirement is time-related.**
  - E12 bounds the overlap by "the maximum assertion lifetime", so the retirement schedule is time-based.
  - However, the locked text makes retirement a state of the key and its verification material (E11, E12). It does not make it a validity condition of the assertion (E8, E9).
  - The §P.4 heading (E5) places retired `key_id` under "Freshness, Replay and Single Use" just as strongly as "not yet
    valid". Because the heading spans all §P.4.1 conditions, it does not decide between the two readings.
  - Beyond the heading, no locked text attributes retired-key rejection to freshness.
  - The signature reading has positive support in the word "active" in E11 and in "then is retired" in E12.
  - The freshness reading is therefore weaker but not excluded. It is recorded so the owner can choose.
- **C-1 dependency:** none.
- **§21 change required:** no.
- **P2/K3 change required:** no.
- **Independent of R-1 and R-2:** yes for both.
- **Independent of OD19-01 and §22 O-4/O-15:** yes. Those concern storage, provisioning and rollover mechanics, not which check applies.
- **Unresolved dependencies:** none for the classification.

## 6. Cross-condition analysis

- **B and C share the signature check.** In both, the failure is the absence of active verification material for the named key (E11), and signature verification is the check that uses that material (E10).
- **A falls under a different check.** It concerns the assertion's validity in time (E8, E9), and freshness is the only named check that bears on that (E14, E15).
- **No three-way grouping.** None of the three relies on single use or audience.
- **Mutual independence.** No classification depends on another, on check ordering, or on multi-failure precedence.
  - How `failure_reason` is set when one attempt fails more than one check remains unspecified (evidence gap 8).
  - This determination does not decide it.

## 7. Conflicts / limitations

- **C-1.**
  - Statements:
    - §15.10 P3 (Category 1): "K4 enforces assertion freshness and single use where applicable".
    - §17.22 step 1 (Category 1): "signature, audience, freshness, single use", with no qualifier.
  - **Effect on R-3: none.** R-3 asks which check records a rejection that has occurred. §P.4.1 states the three rejections unconditionally, and the candidate classifications do not rely on the qualifier.
  - C-1 is not reconciled here.
- **C-2: the step-1 check set is not stated to be closed.**
  - §17.22 step 1 names four assertion checks plus Binding and Principal requirements, and no text closes the set.
  - **Effect on R-3:** the candidates use only named existing checks. If the owner treats the set as open, a candidate
    could be displaced only by a check that locked text does not name. The DEC-091 [OI] route ("if no existing check
    fits, D91-5 applies") remains available.
- **C-7: no closed `failure_reason` vocabulary.**
  - §21.7 and §21.14 define the field as "the §17.22 step-1 check that failed" and list no values.
  - The DEC-091 routing request (log:9185, owner request text, not adopted) refers to a "current … `failure_reason` vocabulary".
  - **Effect on R-3:** the candidate uses only the check names in §17.22 step 1 ("freshness", "signature"). It assumes no closed vocabulary and creates none.
  - "freshness" and "signature" name the §17.22 check. They are not a serialized `failure_reason` string.
  - It does not decide whether a record may also distinguish the condition within the check. That would fall outside R-3, and the §21 contract is unchanged (D92-2).
- **C-3: per-condition attribution is absent in §P.4.1.**
  - This is the R-3 subject itself.
  - The candidate fills it only by inference from locked text, and labels it as inference.
- **Other conflicts discovered:** none that affect R-3.
- **Limitation:** all three candidate classifications are inferred, not explicit. If the owner requires explicit locked text, all three would be "Undetermined within current locked evidence".

## 8. Gate candidate determination

The locked evidence supports a candidate mapping by inference from the text, with no general technical knowledge relied on beyond the ordinary meaning of "freshness"
(Condition A):

| §P.4.1 condition | Candidate §17.22 step-1 check recorded in B2 `failure_reason` | Basis | Explicitness |
|---|---|---|---|
| not yet valid | **freshness** | E1, E6, E8, E9, E14; E15 (support) | Inferred (weakest; relies partly on the ordinary meaning of "freshness") |
| unknown `key_id` | **signature** | E1, E6, E8, E10, E11, E13 | Inferred |
| retired `key_id` | **signature** (freshness reading considered; weaker) | E1, E6, E10–E13 | Inferred |

**[U] for R-3 (D92-5):**
- no locked text explicitly attributes any of the three conditions to a check (C-3);
- the step-1 check set is not stated to be closed (C-2, gap 8);
- clock reference and skew for "not yet valid" (gap 5);
- the multi-failure rule (gap 8).

No item is undetermined on the inference standard. All three are undetermined on an explicit-text-only standard.

## 9. Non-effects

This candidate determination:
- does not modify §21 or its `failure_reason` contract;
- does not modify P2/K3;
- does not modify §17 or §15;
- creates no new `failure_reason` value and no new check;
- does not decide check ordering, multi-failure precedence, or serialization or storage of the reason;
- does not decide R-1 or R-2;
- does not decide "expired", "wrong `audience`" or "fails signature verification";
- does not affect OD19-01, §22 O-4/O-15 or the K2 issuer side;
- authorizes no implementation;
- is not an [OI], not CURRENT and not LOCKED.

## 10. Owner-adoption boundary

For this to become an owner decision:

1. The owner separately decides whether to adopt it, in whole, in part, or not at all. The owner may also choose
   between the inference standard and an explicit-text-only standard (§7 limitation).
2. Adoption is recorded as a new DEC in the decision log, in the DEC-090 D90-1 form with [L], [OI] and [U]
   determinations (DEC-091 D91-4).
3. That DEC does not add to, amend or supersede locked §17, §21 or P2/K3 text, and those documents are not edited
   (D91-4). On this candidate, no locked-text change is needed, so D91-5 is not engaged.
4. Gate output does not become [OI] until that recording (D92-5).
5. Under D92-10, R-3 having candidate output does not by itself conclude the convening. R-1 and R-2 must also reach
   candidate output or a "cannot be determined" report.
6. Implementation of any recording behaviour still requires a separate implementation authorization (DEC-091 §6
   item 4) and is blocked for real verification by OD19-01 (D79-8).
