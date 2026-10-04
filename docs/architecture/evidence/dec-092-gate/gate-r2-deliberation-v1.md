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

# Gate Deliberation — R-2 — Candidate Determination

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

DEC-091 D91-2(b), admitted verbatim by DEC-092 D92-2(b) (log:9362–9363, 9893): "R-2: the persistence and lifecycle of
the replay record K4 keeps under §P.4.2, including behaviour across K4 restart, host restart and restore within the
validity window".

**Not considered in this convening (D92-3, log:9900–9904):**
- a replay-storage technology;
- a replay database or schema;
- implementation mechanics;
- §19 classification;
- any amendment;
- OD19-01 resolution;
- implementation authorization.

**Excluded aspects stay assigned to the gate under D91-2 (D92-9).** No technology is considered or selected here.

The R-1 and R-3 deliberations are prior candidate work only and are not relied on.

## 2. Repository State

| Item | State |
|---|---|
| HEAD | `185e9e96e8bc7e668c6be6ec9c9c203d723da5de`. Unchanged since the R-1 deliberation. |
| Working tree | Clean (0 entries, including untracked) |
| Remote branch `origin/docs/architecture/19-persistence-secrets-data-lifecycle` | `9d24121eca99b8941b366edee92bed959ae100cf` |
| Register §8 (register:227) | "§17/K4 Architecture Gate \| OPEN (DEC-092) — not a §17 amendment gate; §17 remains LOCKED (DEC-064) \| Q19-04 (§19.21.1) — not admitted (DEC-092); DEC-091 D91-2 (a)–(c), convened by DEC-092" |
| DEC-091, DEC-092 | CURRENT (log:9138, 9497) |
| Prior gate work (scratchpad) | Evidence packet v1; R-3 deliberation v1; R-1 deliberation v1. None is authority. |

## 3. Locked Evidence

| # | Source | Text | Tag |
|---|---|---|---|
| R1 | P2/K3 §P.4.2 (p2:81–82) | "K4 records `assertion_id` for the assertion's validity period and rejects any second use [L §17.22 step 1 "single use"]. An assertion used to establish an SCC session is consumed by that act (§P.7.6)." | [L] |
| R2 | P2/K3 §P.4.3 (p2:83) | "Replay rejection is K4's; K3 performs none and holds no replay state [L §15.6; DEC-080 D80-4]." | [L] |
| R3 | P2/K3 §P.3.1 (p2:56, 62) | `assertion_id`, "unique per issued assertion"; `issued_at` and `expires_at` (short-lived) | [L] |
| R4 | P2/K3 §P.3.4 (p2:71–72) | "`expires_at` − `issued_at` is short and does not exceed a fixed maximum assertion lifetime that K4 enforces … The maximum is 60 seconds" | [L] |
| R5 | P2/K3 §P.4.1 (p2:79–80) | K4 rejects an assertion that "is not yet valid, has expired …" | [L] |
| R6 | P2/K3 §P.7.6 (p2:126, 134–136) | "a verified assertion may establish an SCC session; the assertion is consumed (§P.4.2)". "session validation state exists only in K4 runtime state; K4 restart terminates every active SCC session; it is not placed in K7, not recoverable across restart and has no recovery mechanism" | [L] |
| R7 | §17.22 step 1 (s17:549); §17.2 (s17:125) | "Verify the K2 assertion: signature, audience, freshness, single use. … On any failure, **deny**." | [L] |
| R8 | §15.10 P2 row, Replay column (s15:227) | "Assertion short-lived, audience-bound (SCC), nonce/session-bound" | [L] |
| R9 | §15.10 P3 row, Replay column (s15:228) | "K4 enforces assertion freshness and single use where applicable; state-changing requests carry request IDs" | [L] |
| R10 | §15 security boundary (s15:327) | SCC must defend against "replay or duplication on SCC channels" | [L] |
| R11 | §15.13 K4 crash row (s15:282) | Authorization "Unavailable → deny"; "On restart K4 must reconcile in-flight Jobs against K8" | [L] |
| R12 | §17.16 (s17:438, 440) | K4 restart: "Decisions persist in K7. Running Jobs are revalidated before any further request." Default posture: "if authorization cannot be positively established, the Action is **refused**. K4 never continues on stale, cached or assumed authorization state." | [L] |
| R13 | §17 Terms (s17:21); §17.2 (s17:128); §17.18 (s17:463) | The Authentication Context includes "assertion ID". Its reference is carried into the Authorization Decision and recorded in audit. | [L] |
| R14 | §21.7 (s21:127, 149) | `auth_context_ref`: "reference only; never a raw assertion or bearer token", "(§17; format P2)". `claimed_assertion_id` on B2: "marked unverified". | [L] |
| R15 | §21.14 (s21:246–256) | One B2 per failed step-1 attempt. `failure_reason` is "the step-1 check that failed". | [L] |
| R16 | §19.7 (s19:166–191) | DC-19: "SCC session validation state", "TBD by P2". DC-24 (TRANSIENT): "identity assertions in transit". Gate observation: no data class names an assertion replay record. | [L] (classes); observation (absence) |
| R17 | §19.22 (s19:449) | "SCC session semantics and whether session validation state is durable → P2". Gate observation: there is no corresponding row for a replay record. | [L] (row); observation (absence) |
| R18 | §19 LC-12 (s19:81), S19-07 (s19:389), s19:274 | K8 retention covers "the replay acceptance window" for K6 request IDs and approval nonces | [L] |
| R19 | §22 (s22:45, 125) | "replay" appears only for the P11 K9 → K4 bootstrap path ("the recovery gate's") and bootstrap request replay | [L] |
| R18a | DEC-048 R18a (log:2543); DEC-062 F06d (log:3506) | "K8 loss, removal, replacement, or reinitialization MUST NOT be treated as an implicit reset of replay, nonce, idempotency, approval, or execution-history protections" | [DEC], K8-scoped |
| R19a | §21.11 (s21:197–198) | "\"Durably recorded\" means the audit record is committed to SD-K7 and survives both a K4 process restart and a host restart" | [L], audit records only |
| R19b | §21.18 (s21:320); §22.8 O-8 (s22:154) | §21 "defines no restore-generation or K7 lifecycle mechanism"; O-8 "K7 backup and restore; restore generations and audit identity/sequence continuity" | [L] |
| R20 | DEC-080 D80-2 (log:5962–) | "freshness and replay resistance" are P2 scope | [DEC] |
| R21 | DEC-088 D88-2(c) (log:7957–7959) | "the validity window from `issued_at` to `expires_at` MUST NOT exceed 60 seconds; the freshness checks and single-use `assertion_id` requirement are unchanged" | [DEC] |
| R22 | DEC-088 D88-2(f) (log:7967–7970) | "session validation state exists only in K4 runtime state; K4 restart terminates every active SCC session; session state is not placed in K7, is not recoverable across K4 restart, and has no recovery mechanism" | [DEC] |
| R23 | DEC-047 R17c (log:2489) | "Restoring SD-K7 from an earlier backup point MUST place SCC into a recovery/reconciliation condition before ordinary authorization-dependent work may resume." | [DEC] |
| R24 | DEC-047 R17i (log:2504) | "A K7 restore MUST NOT assume that restored SCC session validation state remains valid … Session validity and invalidation after restore remain subject to P2 and §22." | [DEC] |
| R25 | DEC-091 §4 R-2 [U] | "Whether the record survives K4 restart, host restart or restore within the validity window; its §19 classification, owner and storage domain. (§P.7.6 volatility concerns SCC sessions only.)" | [DEC] |

## 4. A — Replay State Lifetime

- **Strongest text:** R1, "records `assertion_id` for the assertion's validity period", together with R3, R4 and R21.
- **[L]:** the record exists "for the assertion's validity period", which is bounded by `issued_at` and `expires_at`. That
  window is at most 60 seconds (R4).
- **Candidate inference from R1 + R5:**
  - An assertion outside its validity window is rejected under R5 whatever the record holds.
  - So R1's period is the span during which K4 must be able to detect a second use.
- **What R1 does not say:** whether the record may persist beyond that period. No upper bound or deletion rule is
  stated [U].

## 5. B — Process Restart Survival

- **Answer:** Undetermined within current locked evidence.
- **Context:**
  - R11 and R12 address K4 restart for Jobs and Decisions only.
  - R6 and R22 address SCC session state only (see §16).
- No locked text mentions replay state at K4 restart.

## 6. C — Host Restart Survival

- **Answer:** Undetermined within current locked evidence.
- §19.15's "Process crash / reboot" row covers K6 intents and K4 in-flight Jobs, not replay state.

## 7. D — K4 Reinitialization Survival

- **Answer:** Undetermined within current locked evidence.
- Locked text defines no "K4 reinitialization" event. Reinitialization is defined for K8 (DEC-048), not K4.
- This item is not separately addressed by any source [U].

## 8. E — K7 Restore / Recovery Survival

- **Answer:** Undetermined within current locked evidence.
- **R23:** "Restoring SD-K7 from an earlier backup point" puts SCC in a recovery condition before "ordinary
  authorization-dependent work".
- **R24** concerns session state only.
- **No locked connection** between replay state and K7 restore, restore generations (R19b: §21.18, §22 O-8), SD-K7 or §22
  recovery was found. Restore generations concern audit identity and sequence only.
- Whether step-1 verification counts as "authorization-dependent work" under R23 is not stated [U]. This question is
  raised by this deliberation, not by a source.

## 9. F — Durability vs Volatility

- **Answer:** Undetermined within current locked evidence.
- No text calls the replay record durable or volatile.
- The verb "records" in R1 is not read as durability.
- The runtime-only text in R6 and R22 is not extended to the replay record (see §16).

## 10. G — Ownership / Authority

- **[L] R2:** "Replay rejection is K4's; K3 performs none and holds no replay state."
- **[L] R1:** "K4 records `assertion_id`".
- These are the only locked statements on the point. Neither assigns an owner of the state in the §19 sense.
- **[U]:** the §19 data-class owner and storage domain. Their assignment is a §19 change (D91-6), and §19
  classification is excluded from this convening (D92-3).

## 11. H — Data Classification

- **Answer:** Undetermined within current locked evidence.
- **Gate observation (R16):** no §19.7 class names the replay record.
  - DC-19 is session validation state.
  - DC-24 covers assertions *in transit*.
  - Neither names the record.
- **Gate observation (R17):** §19.22 has no row routing the replay record.
- Classification is excluded from this convening (D92-3). Any §19 assignment follows D91-6.

## 12. I — Replay-State Lifecycle

- **Established:** only the validity-period statement in R1 and the session-consumption statement ("consumed by that
  act").
- **Not defined:** creation point, removal, expiry handling beyond the validity period, capacity bounds, and lifecycle
  events (restart, restore, reinitialization).
- **Answer:** Undetermined within current locked evidence beyond R1.

## 13. J — Failure to Determine Prior Use

- **Answer:** no locked text addresses the case where K4 cannot determine whether an `assertion_id` was used [U].
- **Candidate inference from R7 + R12 (§17.16 default posture) + §17.2 (s17:123) + A-01 (s17:584):**
  - Single use is a step-1 verification check.
  - If K4 cannot establish it, the assertion is not K4-verified, and no authorization proceeds for it.
- **Not decided:**
  - whether that is a step-1 failure;
  - the B2 record and its `failure_reason` (an R-3 / §21 matter);
  - the P2 result.

## 14. K — Candidate Persistence Determination

**Determination: B.** The locked evidence establishes only a partial persistence and lifetime interpretation. Material
aspects remain [U].

| Portion | Status |
|---|---|
| "Replay rejection is K4's; K3 performs none and holds no replay state" | [L] R2 |
| "K4 records `assertion_id`" | [L] R1 |
| The record is keyed by `assertion_id` and exists for the assertion's validity period (≤ 60 s) | [L] R1, R4; [DEC] R21 |
| That period is the span in which K4 must be able to detect a second use | Candidate inference from R1 + R5 |
| A session-establishing assertion is consumed by that act | [L] R1, R6 |
| Upper bound or deletion of the record after the validity period | [U] |
| Survival across K4 restart, host restart, K4 reinitialization, K7 restore or recovery | [U]: Undetermined within current locked evidence |
| Durable or volatile | [U] |
| §19 class, owner, storage domain | [U]. Excluded from this convening (D92-3); route D91-6 |
| Outcome when prior use cannot be determined | Candidate inference: no authorization proceeds (R7 + R12 + §17.2 + A-01). B2, `failure_reason` and P2 result are [U] |

- **No technology was invented.** The partial interpretation uses R1, R2, R4, R5, R6, R7 and R21, plus §17.2 and A-01.
- **Why the rest is not a candidate.** A candidate for the restart and restore items would need text the sources do
  not contain, or a choice of storage behaviour. D92-3 excludes the latter.
- **Report to the owner (D92-7, D92-9).** The restart, restore and durability aspects **cannot be determined within the
  permitted scope**.

## 15. Restart / Restore Evidence Analysis (special checks)

1. **Does "for the assertion's validity period" set retention duration or only a detection window?**
   - It states that the record exists for that period.
   - Read with R5, it fixes the minimum span in which a second use must be detectable (candidate inference).
   - It sets no upper bound, and it says nothing about restart or restore.
2. **Does "records `assertion_id`" establish persistence?** No. It establishes a logical replay record kept by K4. The
   storage medium and durability are not stated.
3. **Does §P.4.3 establish anything about persistence?** No. It states "Replay rejection is K4's" and that K3 holds no replay state. It says nothing about persistence.
4. **Do §P.7.6 and D88-2(f) apply to replay state?** No. Their runtime-only text is about "session validation state" and
   SCC sessions (see §16).
5. **Does any locked text connect replay state to K7?** No.
6. **Does any locked text connect replay state to §22 recovery?** No. §22's "replay" references concern only the P11
   bootstrap path (R19).
7. **Does any locked text say replay prevention survives restart?** No.
8. **Does any locked text say replay prevention survives restore?** No.
9. **Is the replay record an audit record?**
   - No locked text says so.
   - §P.4.2 sits in the P2 protocol, and P2/K3 does not own §21 audit records (§P.10).
   - Audit separately records an `auth_context_ref` for authorization records (R13, R14) and a `claimed_assertion_id`
     on B2 (R14).
   - No locked text says replay detection uses audit records. Audit evidence of a replay event is not replay-prevention
     state.
   - Audit records are expressly durable: they survive "both a K4 process restart and a host restart" (R19a). No
     equivalent statement exists for the replay record, and R19a is not extended to it.
   - Whether the two are related is unresolved [U].
10. **Can the gate set a minimum lifetime without a storage mechanism?** Yes, as a candidate inference from R1 + R4 + R5:
    "at least the assertion's validity period (≤ 60 s)". It needs no storage choice.
    - It does not settle whether that span must hold across a restart or restore inside the window. That is T-6 and
      remains [U].

**Conclusion:** No locked connection between replay state and the referenced recovery mechanisms (K7 restore,
restore generations (R19b), SD-K7, §22 recovery) was found.

## 16. Runtime-Only Scope Check

- **§P.7.6 (R6):** the runtime-only clause's subject is "session validation state". Its consequences are framed as
  sessions: "K4 restart terminates every active SCC session".
- **D88-2(f) (R22):** headed "session durability (OQ-P4 = a)", with subject "session validation state".
- **DEC-091 §4 (R25)** states it directly: "§P.7.6 volatility concerns SCC sessions only".
- **The only link to replay** is R6's first bullet: "the assertion is consumed (§P.4.2)". That ties session
  establishment to the replay record's consumption rule. It does not make the replay record session state.
- **Finding:** the runtime-only text applies to session state only. Extending it to replay state, or ruling it out by
  analogy, has no textual support.

## 17. Conflicts / Tensions

| # | Tension | Side 1 | Side 2 | Authority | Effect on R-2 |
|---|---|---|---|---|---|
| T-1 (C-1) | "where applicable" | §15.10 P3: "single use where applicable" | §17.22 step 1 and §P.4.2: unqualified | Both Category 1 | Whether some assertions fall outside the record is [U]. §P.4.2 itself is unqualified. Not resolved. |
| T-2 | Session volatility vs replay window | R6/R22: K4 restart ends sessions | R1: record for the validity period, with no restart statement | Category 1 / Category 2 | No contradiction. They cover different state. Recorded so it is not read as one rule. |
| T-3 | Audit vs replay state | R13, R14: audit carries `auth_context_ref` and `claimed_assertion_id`. Authentication Context includes assertion ID. | R1: the replay record | Category 1 | Separate concepts in text. `auth_context_ref`'s format is "P2", but P2/K3 defines no such format [U]. |
| T-4 | K8 replay analogues | R18: K8 retains K6 request IDs and nonces for "the replay acceptance window". R18a: K8 loss or reinitialization is no "implicit reset of replay … protections". | R1: P2 assertion record | Category 1 / Category 2 | K8-scoped. Different mechanism and component. Not imported. |
| T-5 | Restore recovery condition | R23: recovery condition before "authorization-dependent work" | No text links replay state | Category 2 | [U]. Not resolved. |
| T-6 | Restart within window | R4: validity ≤ 60 s, so a K4 or host restart can fall inside a live window | No text on replay state across restart | Category 1 | This is the gap DEC-091 named (R25). It is not a contradiction. |

No literal contradiction was found among §15.10, §17.22, §P.4.1–§P.4.3, §P.7.6, §21.7 and §21.14.

## 18. Evidence Gaps

1. No text on replay-state behaviour across K4 restart, host restart or K4 reinitialization. K4 reinitialization is
   not a defined event.
2. No text on replay state across K7 restore or recovery, or on whether R23's recovery condition covers step-1
   verification.
3. No durability or volatility statement for the replay record.
4. No §19 data class, owner or storage domain (outside this convening).
5. No upper bound, removal rule or capacity bound for the record.
6. No text on K4 behaviour when prior use cannot be determined, beyond the inference in §13.
7. The clock reference and skew for the validity period are not specified.
8. The format of `auth_context_ref` ("format P2") is not defined in P2/K3.
9. The scope of "where applicable" in §15.10 P3 is not specified.
10. Whether any part of R-2 is DC-18 material is not decided (DEC-091 §7). That is OD19-01 territory, excluded by D92-3.

## 19. Non-Effects

This candidate output:
- selects no storage technology, database, schema, cache, journal or medium;
- decides no durability;
- does not extend §P.7.6 or D88-2(f);
- makes no §19 classification;
- does not resolve OD19-01;
- amends no locked document;
- does not decide R-1 or R-3, and does not rely on their deliberations;
- creates no B2 behaviour or `failure_reason`;
- changes no register entry;
- authorizes no implementation;
- is not an [OI], CURRENT or LOCKED.

## 20. Owner Adoption Boundary

1. **The owner's choice.** The owner may accept, reject or partly adopt any row of §14.
2. **How adoption is recorded.** As a new DEC in the DEC-090 D90-1 form (DEC-091 D91-4), with no edit to locked
   P2/K3, §17 or §21 text.
3. **If locked text would need to change**, D91-5 governs, by document:
   - P2/K3 or §21 changes return to the owner;
   - §15 and §17 have no amendment path;
   - a §16 change goes only through the §16 Amendment Gate after a D68-D assignment;
   - a §22 change goes only where DEC-078 D78-1 admits it, otherwise back to the owner (D91-7). This is relevant to
     restore.

   On this candidate, no locked-text change is needed.
4. **When it becomes [OI].** Gate output becomes [OI] only on that recording (D92-5).
5. **What remains undetermined:**
   - restart, restore and durability;
   - the record's classification (§19 route D91-6, excluded here by D92-3).

   Settling these needs either an owner decision or further gate work. Once this convening closes under D92-10, further
   gate work needs a new convening decision (D91-9).
6. **Closure (D92-10).**
   - D92-10 requires, for each of (a)–(c), candidate output or a cannot-determine report. The gate's reading is that D92-10 does not require adoption.
   - This output supplies that for (b) only.
   - Whether (a) and (c) are satisfied, and the resulting register update under D92-11, are not assessed here.
   - This deliberation makes no register update and no closure decision.
7. **Implementation** needs a separate implementation authorization (DEC-091 §6 item 4). Real verification is blocked by
   OD19-01 (D79-8).
