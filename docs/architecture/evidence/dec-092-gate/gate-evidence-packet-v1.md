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

# Gate Evidence Packet v1 — §17/K4 Architecture Gate, DEC-092 convening (EVIDENCE ONLY)

Prepared read-only at HEAD `185e9e96e8bc7e668c6be6ec9c9c203d723da5de`. This packet records sources only. It makes no
candidate determination and answers none of R-1, R-2 or R-3.

**Controlling scope.** DEC-091 D91-2 (a)–(c); DEC-092 D92-1 … D92-11.
- Not admitted (DEC-092 D92-2): Q19-04, the DEC-090 D90-6 item, and the K2 issuer side of R-1.
- Not considered in this convening (DEC-092 D92-3):
  - K2 issuer-side `audience` behaviour;
  - a replay-storage technology, database or schema;
  - implementation mechanics;
  - any P2/K3, §15, §16, §17, §19, §21 or §22 amendment;
  - §19 classification;
  - OD19-01 resolution;
  - implementation authorization.

**Tags used here.**
- **[L]:** text of a Category 1 locked document: §15, §16, §17, §19, §21, §22 or P2/K3.
- **[DEC]:** an existing Category 2 owner decision. This includes the ones the task calls "existing owner interpretations [OI]".

Nothing in this packet is a new [OI].

**Line references.** Lines are cited at HEAD.
- `p2` = `docs/architecture/current/p2-protocol.md`
- `s15` = `current/15-runtime-topology.md`
- `s17` = `current/17-authorization.md`
- `s19` = `current/19-persistence-secrets-data-lifecycle.md`
- `s21` = `current/21-audit-events.md`
- `s22` = `current/22-lifecycle-recovery.md`
- `log` = `decisions/decision-log.md`

---

## R-1 evidence packet

### 1. Question
DEC-091 D91-2(a): "R-1, K4 side: what K4 compares an assertion's `audience` against, and how K4 obtains that expected
value".

### 2. Locked facts [L]
| # | Source | What is locked |
|---|---|---|
| L1-1 | §15.6 (s15:150) | K2 may "issue a short-lived, audience-bound identity assertion". |
| L1-2 | §15.10 P2 row (s15:227) | The P2 assertion is "short-lived, audience-bound (SCC), nonce/session-bound". |
| L1-3 | §17.2 (s17:124–126) | K4 independently verifies "the assertion's signature, audience, freshness and single use". |
| L1-4 | §17.22 step 1 (s17:549) | "Verify the K2 assertion: signature, audience, freshness, single use. … On any failure, **deny**." |
| L1-5 | P2/K3 §P.3.1 (p2:61) | The assertion carries "`audience`, identifying the SCC instance the assertion is for". |
| L1-6 | P2/K3 §P.4.1 (p2:79–80) | K4 rejects an assertion that "carries the wrong `audience`". |
| L1-7 | P2/K3 §P.3.5 (p2:73–75) | The assertion is signed by K2 and verified by K4. Its encoding is CBOR and its signature is Ed25519. |
| L1-8 | P2/K3 §P.5.3 (p2:94–95); §15.6 | The relay route and the proxy route both remain admissible. |
| L1-9 | P2/K3 §P.7.2 (p2:117–118) | K3 "never inspects or validates the assertion". |
| L1-10 | P2/K3 §P.10 (p2:166) | Identity: "K1/K2 issue, K4 verifies". |
| L1-11 | §15 scope rule (s15:53) | Everything in §15 must remain true for any future Platform Adapter. |

**Literal observation.** The term "SCC instance" also appears in:
- §21.4 (s21:62) and §21.5 (s21:69);
- §19 S19-08 (s19:390);
- §22.3 (s22:68).

None of these passages, nor §P.3.1, defines an SCC-instance identifier, value or representation.

### 3. Existing owner decisions [DEC]
- **DEC-080 D80-2 (log, DEC-080):** "audience binding" is P2 scope. D80-7: "No post-lock route is created now".
- **DEC-088 D88-6(3):** the lock criterion says the assertion "supports every §17.22 step-1 check (signature, audience,
  freshness, single use)".
- **DEC-091 D91-2(a):** assigns the K4 side to the gate.
- **DEC-091 D91-3:**
  - The issuer side ("what K2 places in `audience` and how K2 obtains it") "is not assigned" and "returns to the owner".
  - "Anything later determined to be DC-18 assertion-verification material stays in OD19-01 under DEC-051 R01b".
- **DEC-091 §4 R-1 [U] (log ~9400):** "The concrete value; its creator, owner, storage, provisioning and lifecycle; how
  K4 obtains the expected value; how K2 obtains the value it places."
- **DEC-091 §7:** "[U] Whether any part of R-1 or R-2 is DC-18 material is not decided".
- **DEC-092 D92-4:** the gate may consider and report a candidate expected value and how K4 obtains it. DEC-092 "selects
  no `audience` value".
- **DEC-092 D92-3:** excludes K2 issuer-side `audience` behaviour and §19 classification from this convening.

### 4. Unresolved matters [U]
These are as stated in DEC-091 §4, restricted to the K4 side:
- what value or representation K4 compares `audience` against;
- the source from which K4 obtains that expected value;
- that value's creator, owner, storage, provisioning and lifecycle.

A §19 data-class, owner or storage-domain assignment is a §19 change (D91-6), and §19 classification is excluded from this convening (D92-3).

### 5. Dependencies
- **Blocking (stated by source):** none found. No source states that R-1 cannot be considered until another item is resolved.
- **Contextual:**
  - The K2 issuer side is with the owner (D91-3). No source states an order between the issuer side and the K4 side.
  - The DC-18 boundary applies: material determined to be DC-18 stays in OD19-01 (D91-3; DEC-091 §7).
  - CyberPanel-specific aspects go to the CyberPanel K2 gate only within K2-Q1 … K2-Q7 (D91-8).
- **Adjacent unresolved questions:**
  - OD19-01 (s19:403; DEC-051).
  - §22 O-4, K2 re-registration after platform upgrades (s22:150).
  - "Cross-instance approval replay (instance identity in approvals)", ODF-18-02 / KF-04, which is conditional §18 (p2:162). It is listed only because of the shared word "instance"; no source links it to `audience`.
  - §19 consequences of any persisted value (D91-6), which this convening does not consider.

### 6. Existing failure / refusal behaviour
- A wrong `audience` causes rejection (§P.4.1), which is a deny (§17.22 step 1).
- The client receives `UNAUTHENTICATED` (§P.5.4, p2:96).
- K4 writes one B2 record per attempt (§21.14, s21:246). If the B2 record cannot be durably recorded, the §21.12 denial row applies (s21:265, s21:214).
- §17.16's default posture is: "if authorization cannot be positively established, the Action is **refused**" (s17:440).
- No source addresses what happens when K4 cannot obtain its expected `audience` value.

### 7. Evidence gaps (not filled)
- The definition, form or encoding of an SCC-instance identity. No source defines one.
- The type or representation of the `audience` field. CBOR fixes the encoding of the assertion only.
- Comparison semantics for `audience` (not specified).
- (Raised by this review, not by a source.) Whether the expected value is expected to stay the same across SCC reinstall, upgrade, K7 restore or platform reinstall (not specified).
- (Raised by this review, not by a source.) Whether more than one SCC instance can coexist on one host (not addressed in the sources read).
- K4 behaviour when the expected value is unavailable (not specified).

---

## R-2 evidence packet

### 1. Question
DEC-091 D91-2(b): "R-2: the persistence and lifecycle of the replay record K4 keeps under §P.4.2, including behaviour
across K4 restart, host restart and restore within the validity window".

### 2. Locked facts [L]
| # | Source | What is locked |
|---|---|---|
| L2-1 | §17.22 step 1; §17.2 | K4 verifies "single use". On failure it denies. |
| L2-2 | §15.10 P3 row (s15:228) | "K4 enforces assertion freshness and single use where applicable". |
| L2-3 | P2/K3 §P.4.2 (p2:81–82) | "K4 records `assertion_id` for the assertion's validity period and rejects any second use." An assertion used to establish an SCC session "is consumed by that act". |
| L2-4 | P2/K3 §P.4.3 (p2:83) | "Replay rejection is K4's; K3 performs none and holds no replay state". |
| L2-5 | P2/K3 §P.3.1 (p2:56, 62) | `assertion_id` is "unique per issued assertion". The assertion has `issued_at` and `expires_at`. |
| L2-6 | P2/K3 §P.3.4 (p2:71–72) | `expires_at` − `issued_at` ≤ 60 seconds, and K4 enforces it. |
| L2-7 | P2/K3 §P.7.6 (p2:134–136) | *SCC session* validation state exists only in K4 runtime state, and K4 restart terminates every active SCC session. This concerns sessions, not the replay record. |
| L2-8 | §15 security boundary (s15:327) | SCC must defend against "replay or duplication on SCC channels". |
| L2-9 | §15.13 K4 crash row (s15:282) | Authorization is "Unavailable → deny". On restart K4 reconciles in-flight Jobs against K8. |
| L2-10 | §19.7 (s19:166–191) | None of DC-01 … DC-24 names an assertion replay record. DC-24 (TRANSIENT) includes "identity assertions in transit". DC-19 is "SCC session validation state", with storage domain "TBD by P2". |
| L2-11 | §19.8(1) (s19:200) | "One authoritative owner and storage domain per data class" (S19-01). |
| L2-12 | §19.15 (s19:326) | The process-crash/reboot row covers K6 and K4 Jobs. It does not mention a replay record. |
| L2-13a | §17.16 K4-restart row (s17:438) | "Decisions persist in K7. Running Jobs are revalidated before any further request." This concerns Decisions and Jobs; the replay record is not mentioned. |
| L2-13b | §17.16 default posture (s17:440) | "K4 never continues on stale, cached or assumed authorization state." This concerns authorization state; the replay record is not mentioned. |
| L2-13 | §19.17 (s19:355–359) | Backup and restore implications are established by DEC-047 R17a–R17l. Procedures belong to §22. |

### 3. Existing owner decisions [DEC]
- **DEC-080 D80-2:** "freshness and replay resistance" are P2 scope.
- **DEC-088 D88-2(c):** a 60-second maximum lifetime; "the freshness checks and single-use `assertion_id` requirement
  are unchanged".
- **DEC-088 D88-2(f):** session durability. Session validation state is K4 runtime-only and is terminated on K4 restart.
  This is about sessions only.
- **DEC-047 R17c:** a K7 restore "MUST place SCC into a recovery/reconciliation condition before ordinary
  authorization-dependent work may resume".
- **DEC-047 R17i:** restored *session* validation state is not assumed valid. "Session validity and invalidation after
  restore remain subject to P2 and §22."
- **DEC-091 §4 R-2 [U]:** "Whether the record survives K4 restart, host restart or restore within the validity window;
  its §19 classification, owner and storage domain. (§P.7.6 volatility concerns SCC sessions only.)"
- **DEC-091 D91-6:** governs §19 consequences.
- **DEC-092 D92-3:** excludes from this convening replay-storage technology, replay database or schema, and §19
  classification.

### 4. Unresolved matters [U]
These are as stated in DEC-091 §4 R-2:
- whether the replay record survives K4 restart, host restart and restore within the validity window;
- the record's persistence and lifecycle in general.

The §19 classification, owner and storage domain are also unresolved. Their assignment is a §19 change (D91-6), and §19 classification is excluded from this convening (D92-3).

### 5. Dependencies
- **Blocking (stated by source):** none found.
- **Contextual:**
  - DEC-047 R17 and §22 O-8 "K7 backup and restore" (s22:154). R17c applies on any K7 restore ("MUST place SCC into a
    recovery/reconciliation condition before ordinary authorization-dependent work may resume"). No source states how
    R17c, R17i or §22 O-8 relate to the replay record, or whether step-1 verification is "authorization-dependent work" (that last question is raised by this review, not by a source).
  - The 60-second validity window (D88-2(c)).
  - §15.13 K4-crash semantics.
- **Adjacent unresolved questions:**
  - The §19 classification route under D91-6, which this convening does not consider.
  - The K6/K8 replay protection in LC-12 (s19:81) and S19-07 (s19:389): the sources tie it to K8/K6 (§16.11; X-16,
    X-31). No source links it to P2 assertions.

### 6. Existing failure / refusal behaviour
- A second use is rejected (§P.4.2), which is a deny (§17.22 step 1). The client receives `UNAUTHENTICATED` (§P.5.4) and K4 writes one B2 record per attempt (§21.14).
- §17.16's default posture is refusal when authorization cannot be positively established.
- No source states K4's behaviour when it cannot determine whether an `assertion_id` was already used, for example after state loss.

### 7. Evidence gaps (not filled)
- No data class or storage domain for the replay record exists in §19.7.
- The clock reference and skew tolerance for "validity period" are not specified. §21.7 `timestamp` is "K4 clock", which
  applies to audit records only.
- What "host restart … within the validity window" assumes about K4 state is not specified.
- The "restore within the validity window" case relative to DEC-047 R17c's recovery condition is not specified.
- Capacity bounds of the record are not specified.
- How "consumed" (§P.4.2/§P.7.6) relates to the record's retention is not specified beyond "for the assertion's validity period".

---

## R-3 evidence packet

### 1. Question
DEC-091 D91-2(c): "R-3: under which §17.22 step-1 check each of the §P.4.1 conditions not yet valid, and has an unknown
or retired `key_id` is recorded in B2 `failure_reason`."

### 2. Locked facts [L]
| # | Source | What is locked |
|---|---|---|
| L3-1 | §17.22 step 1 (s17:549) | "Verify the K2 assertion: signature, audience, freshness, single use. Resolve the Binding, then the Principal. Require the Principal to be ACTIVE and the Binding CONFIRMED. On any failure, **deny**." |
| L3-2 | §17.2 (s17:124–126) | K4 verifies "signature, audience, freshness and single use", and Binding and Principal state. |
| L3-3 | P2/K3 §P.4.1 (p2:79–80) | K4 rejects an assertion that "is not yet valid, has expired, carries the wrong `audience`, has an unknown or retired `key_id`, or fails signature verification", tagged collectively "[L §17.22 step 1]". |
| L3-4 | P2/K3 §P.6.1–§P.6.2 (p2:104–108) | "K4 accepts a `key_id` only while K4 holds the corresponding active verification material". An old key is accepted for an overlap no longer than the maximum lifetime, "then is retired". |
| L3-5 | P2/K3 §P.3.1 (p2:62, 64) | The assertion carries `issued_at`, `expires_at` and `key_id`. |
| L3-6 | §21.7 (s21:148) | `failure_reason`: "The §17.22 step-1 check that failed". It is Required, on B2. Sensitivity: "no assertion content; no credential". Note: "the checks are §17's". |
| L3-7 | §21.14 (s21:246–256) | One B2 per failed attempt; no aggregation. "`failure_reason` identifies the step-1 check that failed". A verified assertion whose Binding or Principal-state check then failed may record the resolved `principal_id`. |
| L3-8 | §21.6 (s21:89, 97) | "Failed authentication is B2, not A1". |
| L3-9 | P2/K3 §P.5.4 (p2:96) | `UNAUTHENTICATED` is returned for "any §17.22 step-1 failure". |
| L3-10 | P2/K3 §P.10 (p2:166–168) | P2/K3 does not own "§21 audit records". |

### 3. Existing owner decisions [DEC]
- **DEC-082 D82-12(2):** the B2 record "may identify the authentication attempt and the failure reason".
- **DEC-085 D85-11:** there is no §21 post-lock route.
- **DEC-091 D91-2(c):** the assignment.
- **DEC-091 §4 R-3 [OI]:** "R-3 is a §17.22 step-1 classification question … if no existing check fits, D91-5 applies".
- **DEC-091 D91-5:** a determination needing a change to locked P2/K3 or §21 text "returns to the owner".
- **DEC-092 D92-2:** matter (c) is "considered against the existing §21 `failure_reason` contract, which is unchanged".
- **DEC-092 D92-3:** excludes any §21 amendment.
- **Owner request and correction text in the DEC-091 entry.** This is not adopted decision text.
  - The routing request (log:9185) describes R-3 as concerning conditions "explicitly named in §P.4.1 but not
    individually represented in the current §21 B2 `failure_reason` vocabulary".
  - The owner correction instruction (log:9272–9292) removed "has expired" from D91-2(c) and the R-3 [U] row, so that
    R-3 lists exactly not yet valid, unknown `key_id` and retired `key_id`.

### 4. Unresolved matters [U]
As stated in DEC-091 §4 R-3: "Under which step-1 check the §P.4.1 conditions not yet valid, and has an unknown or
retired `key_id` are recorded."

### 5. Dependencies
- **Blocking (stated by source):** none found.
- **Contextual:**
  - §P.6.1 ties `key_id` acceptance to the verification material K4 holds. Storage and provisioning of that material are
    OD19-01 and §22 O-15 (p2:109–111; s22:161). No source states that R-3 depends on their resolution.
- **Adjacent unresolved questions:** §22 O-4 and O-15 rollover and provisioning mechanics.

### 6. Existing failure / refusal behaviour
All five §P.4.1 conditions lead to:
- rejection (§P.4.1);
- deny (§17.22 step 1);
- `UNAUTHENTICATED` (§P.5.4);
- one B2 record with a Required `failure_reason` and no assertion content (§21.7, §21.14).

If B2 cannot be recorded, the §21.12 denial row applies. The mapping of conditions to checks is not stated here.

### 7. Evidence gaps (not filled)
- No source gives a closed list of `failure_reason` values or of "step-1 checks". §17.22 step 1 contains the four named
  verification checks plus the Binding and Principal requirements.
- No source states an order among signature, audience, freshness and single use. §17.22 step 1 puts assertion verification, then Binding resolution, then Principal resolution in sequence ("then"), and §21.14 (s21:253–254) assumes the same sequence.
- No source states how `failure_reason` is set when one attempt fails more than one check.
- §P.4.1's tag attributes the five conditions to step 1 collectively, not individually.

---

## Cross-question analysis

**A. Shared locked facts**
- §17.22 step 1 and §17.2 (K4 verifies signature, audience, freshness and single use; deny on failure).
- §P.4.1–§P.4.3.
- §P.5.4 `UNAUTHENTICATED`.
- §21.14 B2.
- §P.7.2 (K3 does not validate assertions).
- DEC-080 D80-2 (all three topics are P2 scope).
- DEC-088 lock (D80-7: no post-lock P2 route).

**B. Shared unresolved dependencies**
- **OD19-01 / DC-18:**
  - R-1 through DEC-091 §7 ("whether any part of R-1 or R-2 is DC-18 material is not decided");
  - R-2 through the same §7 sentence;
  - R-3 through §P.6.1, as context only.
- **The §19 classification route (D91-6):** relevant to R-2 and to any persisted R-1 value. This convening does not
  consider it.
- **§22 O-4 / O-15.**

**C. Explicit coupling**
- DEC-091 §4 R-3 [OI] groups the matters: R-3 "is assigned with R-1(a) and R-2 as part of K4's step-1 verification". This
  is an assignment grouping. It states no dependency.
- §P.4.2 bounds the replay record by "the assertion's validity period". §P.4.1's "not yet valid" uses the same validity
  vocabulary. This is a shared term only, and no source draws a dependency from it.

**D. Evidence of independence**
- D91-2 lists (a), (b) and (c) as separate items.
- DEC-092 D92-10 completes each item separately.
- D92-7 lets the gate report "cannot be determined" for an individual matter.

**Implementation context (not a deliberation dependency).**
- DEC-091 §7 and DEC-092 §12 state that OD19-01 blocks implementation of real assertion verification (DEC-079 D79-8).
  That implementation also needs a separate implementation authorization.
- DEC-092 §12 [U]: whether owner decisions on the gate's output and on the K2 issuer side of R-1 are also
  prerequisites.

**E. Ordering requirements**
- No source requires one of R-1, R-2 or R-3 to be resolved before another.
- No source orders the R-1 K4 side against the issuer side (D91-3).

---

## Conflict scan (literal; nothing resolved)

| # | Finding | Side A | Side B | Authority | Type |
|---|---|---|---|---|---|
| C-1 | Qualifier difference | §15.10 P3: "K4 enforces assertion freshness and single use **where applicable**" | §17.22 step 1: "signature, audience, freshness, single use" (unqualified); §P.4.2 unqualified | Both Category 1 | Literal difference. Whether "where applicable" narrows the P2 assertion case is not stated. |
| C-2 | "Step-1 check" set not closed | §17.22 step 1: four verification checks plus "Resolve the Binding, then the Principal. Require … ACTIVE … CONFIRMED" | §21.7 "The §17.22 step-1 check that failed"; §21.14 refers to a "Binding or Principal-state check" | Both Category 1 | Locked requirement whose consequence is unspecified. No list of checks or values is given. |
| C-3 | Per-condition attribution absent | §P.4.1: five conditions tagged "[L §17.22 step 1]" collectively | §17.22 step 1 names four checks | Both Category 1 | Not a contradiction. This is the R-3 subject itself. |
| C-4 | Agenda versus unaddressed conditions | DEC-091 §4 R-3 [L] lists §P.4.1 including "expired", "wrong `audience`" and "signature failure" | D91-2(c) admits only not yet valid, and unknown or retired `key_id` | Category 2 (owner scope choice) | No source literally maps "expired", "wrong `audience`" or "signature failure" to a check either. Reported only, as they are outside the agenda. The owner correction (log:9272–9292) removed "has expired" from the agenda. |
| C-7 | "Current vocabulary" vs no enumeration | DEC-091 owner routing request (log:9185): "the current §21 B2 `failure_reason` vocabulary" | §21.7 and §21.14 define `failure_reason` as "the §17.22 step-1 check that failed" and enumerate no values (see C-2) | Owner request text (not adopted decision text) vs Category 1 | Literal tension. Whether a "current vocabulary" exists beyond the step-1 check names is not stated. |
| C-5 | Two scope assignments | DEC-080 D80-2: "audience binding", "freshness and replay resistance" are P2 scope; P2 locked by DEC-088 with no post-lock route (D80-7) | DEC-091 D91-2 assigns K4-side aspects to the §17/K4 gate. D91-4 says outcomes do not amend P2/K3, and D91-5 sends locked-text changes to the owner | Both Category 2; DEC-091 self-describes as "an owner assignment" | Recorded by DEC-091 itself. Not resolved here. |
| C-6 | Literal statement about §19 table | §19 DC-19 storage "TBD by P2"; §19.22: P2 decides session durability | §P.7.6 / D88-2(f): runtime-only; "locked §19 DC-19 is not modified" | Category 1 / Category 2 | Concerns sessions, not the replay record. Not a conflict about R-2, and listed so it is not mistaken for one. |

- **Purported [U] already resolved:** none found. The DEC-091 [U] items in R-1, R-2 and R-3 have no answering text in the sources read.
- **Purported [L] that is only an inference:** none found in DEC-091/092 for the admitted matters. C-4 notes where inference would be needed for items outside the agenda.
- **Silent scope change:** none found. DEC-092 D92-3 narrows scope explicitly, not silently.

---

## Boundary verification

The packet was checked to contain none of the following. Each result is NO:
- a technical solution;
- an `audience` selection;
- a replay-storage or replay-persistence selection;
- an R-3 classification or mapping;
- a K2 assignment;
- an amendment proposal;
- an implementation plan;
- a new architecture decision or [OI].

Evidence gaps are phrased as "not specified", and no gap is filled.

---

## Exact source inventory (HEAD 185e9e9)

**Locked documents**
- `current/p2-protocol.md`: §P.2 (22–51), §P.3 (53–75), §P.4 (77–83), §P.5.3–§P.5.4 (94–100), §P.6 (102–111),
  §P.7.2, §P.7.6 (117–141), §P.9 (153–162), §P.10 (164–168), §P.11 (170–175).
- `current/15-runtime-topology.md`: 53, 150–152, 227–228, 257–274 (§15.12), 276–290 (§15.13), 320–330.
- `current/17-authorization.md`: Terms (16–37), §17.1.3–§17.1.5 (82–112), §17.2 (114–132), §17.16 (429–442),
  §17.22 (546–579), A-01, §17.24 (637–650).
- `current/21-audit-events.md`: §21.4–§21.5 (60–69), §21.6 (85–100), §21.7 rows (121, 126, 148–149), §21.12 (206–227),
  §21.14 (244–266), §21.18 (315–324), §21.22 (389–407).
- `current/19-persistence-secrets-data-lifecycle.md`: 73, 81, 127, §19.7 (164–196), §19.8 (198–212), §19.15–§19.17
  (316–359), 389–390, §19.21–§19.22 (399–460).
- `current/22-lifecycle-recovery.md`: §22.8 (141–164).

**Owner decisions (`decisions/decision-log.md`)**
- DEC-047 (2473–): R17c, R17i.
- DEC-051 (2819–): R01a–R01h.
- DEC-064 (3738–): gate naming.
- DEC-068 (4626–) and DEC-069 (4729–): precedent only, per DEC-092.
- DEC-080 (5920–): D80-1 … D80-9.
- DEC-082 (6149–): D82-12.
- DEC-085: D85-11.
- DEC-088 (7462–): D88-2, D88-6, D88-7, D88-13.
- DEC-090 D90-6: cited only as not admitted.
- DEC-091 (9138–): D91-2 … D91-9, §4, §7.
- DEC-092 (9497–): D92-1 … D92-11.

**Category 4 (non-normative):** `open/register.md` §8.

---

## Remaining evidence gaps (consolidated)
1. R-1: no definition of SCC-instance identity, or of the type or representation of the `audience` value.
2. R-1: comparison semantics and K4 behaviour when the expected value is unavailable are not specified.
3. R-1 (raised by this review, not by a source): stability of the expected value across reinstall, upgrade, restore or platform reinstall is not specified.
4. R-2: no §19 data class names the replay record. Classification is outside this convening.
5. R-2: the clock reference and skew for the "validity period" are not specified.
6. R-2: K4 behaviour when prior use of an `assertion_id` cannot be established is not specified.
7. R-2: the restore case relative to DEC-047 R17c's recovery condition is not specified.
8. R-3: no closed list of step-1 checks or `failure_reason` values; no order among the four verification checks (verification → Binding → Principal is sequenced); no multi-failure rule.

## Readiness assessment
The source record is **not internally contradictory**. C-1 is a literal qualifier difference between two Category 1
texts and is recorded, not resolved. C-7 sets owner request text (not adopted) against Category 1 text, and is likewise recorded, not resolved.

| Matter | Assessment |
|---|---|
| R-1 | Incomplete, but sufficient to identify the missing evidence (gaps 1–3). |
| R-2 | Incomplete, but sufficient to identify the missing evidence (gaps 4–7). |
| R-3 | Sufficient to deliberate. The governing texts (§17.22 step 1, §P.4.1, §P.6, §21.7, §21.14) are all present. Gap 8, C-2 and C-7 are recorded for the gate. |

This assessment does not indicate which answer is preferable. No candidate determination is made.
