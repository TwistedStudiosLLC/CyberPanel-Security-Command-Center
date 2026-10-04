> **Document status:** LOCKED [DEC-085]
> **Authority category:** 1 — Locked architecture, from DEC-085 forward (see [Authority Hierarchy](../README.md#authority-hierarchy)).
> The earlier Category 4 classification is historical [DEC-085].
> **Source:** §21 architecture gate (PHASE 3 of DEC-025). Scope and gate structure: DEC-071. ODF-18-07: DEC-072.
> Owner dispositions: DEC-082, DEC-085. §16 Amendment Gate assignments: DEC-083, DEC-084. Locked form and lock:
> DEC-085.
> **Normative:** Yes. Passages tagged [DEC-0xx] point to the owner decision they implement; the decision log holds the
> complete owner wording. Passages tagged [L] carry only the authority of the locked text cited. Neither this document
> nor the decision log amends §15–§17 or locked §19.
> **Findings against this text:** none recorded.
> **Implementation:** This document defines no schema, storage engine, service, algorithm or file format.
> Implementation remains subject to DEC-029 and DEC-079.

# §21 — Audit Events

---

## 21.1 Purpose and Authority

§21 defines the contract for the K4 audit record: what K4 records, with what fields, how records are identified,
sequenced, durably recorded, retained, correlated with K8 and exported, and what may and may not be claimed from them
[DEC-071 D71-2].

§21 is designed under DEC-025 PHASE 3 in the order of DEC-024, following the candidate → owner dispositions →
separate lock DEC pattern [DEC-071 D71-1; D71-8 criterion 6]. Where §21 conflicts with §15, §16, §17 or locked §19,
those control [DEC-023; DEC-081].

## 21.2 Scope

§21 covers:
- the K4 audit-record contract for every event A-35 enumerates, covering the §17.18 field set without redefining it
  [DEC-071 D71-2(a)];
- the meaning of "durably recorded" [DEC-082 D82-2];
- audit-write failure conditions [DEC-071 D71-2(c); DEC-082 D82-9, D82-10];
- sequencing and gap detection [DEC-082 D82-3, D82-4];
- the tamper-evidence claim scope [DEC-082 D82-4, D82-5(a)];
- the minimal event model [DEC-071 D71-3];
- export content [DEC-072 D72-5; DEC-082 D82-6];
- K4 audit retention and capacity details within the §19 floors [DEC-071 D71-4; DEC-082 D82-7];
- the bootstrap act record that §22 relies on §21 to define [DEC-076 D76-3(5)].

Explicit non-ownership is in §21.21.

## 21.3 Audit Record Definition

A **§21 audit record** is a record written by K4, as identity C, to SD-K7 as data class DC-11 [L §15.3 K4 and K7
rows; locked §19 DC-11]. It is append-only and never edited in place [locked §19.11.1; DEC-042 R12A-2].

There are exactly two record classes [DEC-071 D71-3]:
- **Class A** — K4 audit records required by A-35 and §17.18 [L], including the K6-reported outcome records that
  §17.18 and §17.22 step 14 require for Job steps (§21.6 A7).
- **Class B** — operational-condition and observation records required by an authoritative source [DEC-071
  D71-3(B)]: audit-write failure conditions, failed authentication, anchor-change observation and export-production
  failure [DEC-082 D82-6, D82-9, D82-10, D82-11, D82-12].

§21 creates no general-purpose domain-event bus, no generic event architecture and no Attention-item lifecycle
[DEC-071 D71-3]. A §21 audit record is not a K8 journal record, not a DC-09 Decision or status record, not an
application or host log and not a Job log [L §16.10.3; DEC-044 R14e; baseline §8, §10].

## 21.4 Audit Identity

Every §21 audit record has an identity (`audit_id`) unique within the SCC instance [DEC-082 D82-3(a)]. The identity
lets later records refer to earlier ones, including resolution of UNKNOWN outcomes, late recording and B-class
conditions. Uniqueness must hold across K7 restoration (§21.18) [DEC-082 D82-19]. K4 assigns the identity when the
record is written. §21 defines no identity format.

## 21.5 Audit Sequence

§21 audit records carry a monotonic sequence (`audit_seq`) over all §21 audit records within the SCC instance
[DEC-082 D82-3(b)].

1. `audit_seq` is **recording order, not event order**. A record receives its sequence position when it becomes
   durably recorded; a late-recorded record (§21.12, §21.13) takes the position current at that time. `timestamp`
   (event time) and `recorded_at` (recording time) are distinct. Event chronology is not inferred from `audit_seq`
   [DEC-085 F-2].
2. For a class A record subject to DEC-034 R4a, the sequence position is part of the same atomic commit as the
   authorization mutation.
3. The sequence must remain unambiguous across K7 restoration (§21.18).

**Claims** [DEC-082 D82-4]. SCC may claim K4 audit sequence-gap detection. The claim concerns loss detectable while
the K4 writer is functioning honestly. It does not detect falsification by a compromised K4 (§17.21) and provides no
protection against host or root compromise (§15.15). Restore-related loss follows §22; retention-related
resolvability follows §21.17.

## 21.6 Event Kinds

| Kind | Class | Required by | Producer | Scope |
|---|---|---|---|---|
| **A1 Intent Authorization** | A | A-35; §17.18; §17.22 steps 1–4 | K4 | Includes denials and inadmissible refusals (§17.22 step 3: "Record the result separately"); HUMAN `view` decisions of tier R1 and above (R0 excepted, §21.16); SYSTEM observation authorization (§21.13). Failed authentication is B2, not A1. |
| **A2 Plan Authorization** | A | A-35; §17.22 steps 5–9 | K4 | Includes step-up (REAUTH) failure and whole-Plan denial; creation of the Decision and `authorization_ref`. |
| **A3 Revalidation** | A | A-35; §17.13; §17.22 steps 11–12 | K4 | Job start; before each WRITE request; after revocation or disablement (hold or halt). |
| **A4 Approval acceptance or rejection** | A | A-35; §17.22 step 10 | K4 | One record per approval received and verified or rejected. |
| **A5 Cancellation** | A | A-35; §17.18; A-05 | K4 | HUMAN (`cancel` Permission) or SYSTEM (Fixed System Authority). |
| **A6 Authorization-administration change** | A | A-35; §17.22 (K4-internal Actions); §17.1.5 | K4 | Applied to K7 atomically with its record [L §17.22; DEC-034 R4a]. Includes revocations and the **bootstrap act**: `actor_type` = Local Root Operator; `authority_basis` = Local Root Operator bootstrap authority (A-07); `lro_auth_ref` (§21.7) [L §17.1.5; DEC-076 D76-3(5); DEC-085 C3]. |
| **A7 K6-reported outcome** | A | §17.18; §17.22 step 14; §15.13 | K4 | **K6 requests issued as Job steps only** [DEC-085 C1]. The outcome K6 reported, marked "reported by K6", with the K8 reference; includes UNKNOWN / PARTIAL and outcomes recorded after reconciliation of in-flight Jobs (§15.13). SYSTEM observation requests and SYSTEM cancellation requests do not receive A7. |
| **B1 Audit-write failure condition** | B | DEC-035 R5b; DEC-082 D82-9, D82-10 | K4 | For A5 SYSTEM cancellation, SYSTEM observation A1 and denials (§21.12). |
| **B2 Failed authentication** | B | Baseline §10; DEC-082 D82-12 | K4 | One per failed attempt (§21.14). |
| **B3 Anchor-change observation** | B | §17.9; DEC-082 D82-11 | K4 | §21.15. |
| **B4 Export-production failure** | B | DEC-082 D82-6 (R3-A) | K4 | §21.19. |

Not §21 event kinds (DEC-071 D71-3):
- Decision status transitions (AUTHORIZED, CONSUMED, EXPIRED, REVOKED, INVALIDATED) — DC-09 status records
  (locked §19 DC-09). The A-35 events that cause them are recorded.
- Job creation or lifecycle, Integration or health events, notifications — baseline §10's example list is permissive
  and is limited for §21 by DEC-071 D71-3.
- K8 journal events (§16.10.1) — §16's [DEC-071 D71-9].
- A separate outcome event for SYSTEM observation — none; K8 is the execution evidence [DEC-085 C1; DEC-082 D82-10].
- K8 lifetime changes; Local Root Operator credential-lifecycle acts — left to §22 [DEC-082 D82-15, D82-16].

## 21.7 Required Record Fields

**Req.**: R = required for every record of the kinds listed; C = conditional as stated. **Origin**: K4 = generated
by K4; RX = received from another layer. **§21 semantics**: whether §21 defines the field's meaning or only records a
value whose meaning is owned elsewhere.

| Field | Meaning | Req. | Kinds | Source | Sensitivity constraint | Origin | §21 semantics |
|---|---|---|---|---|---|---|---|
| `audit_id` | Record identity | R | all | DEC-082 D82-3(a) | — | K4 | Yes |
| `audit_seq` | Sequence position (recording order) | R | all | DEC-082 D82-3(b); DEC-085 F-2 | — | K4 | Yes |
| `record_class`, `event_kind` | Class and kind (§21.6) | R | all | DEC-071 D71-3 | — | K4 | Yes |
| `timestamp` | Time of the audited event or condition (K4 clock) | R | all | §17.18 [L] | — | K4 | Field: §17.18; no ordering claim beyond K4's clock |
| `recorded_at` | Time the record became durably recorded | R | all | DEC-085 F-2 | — | K4 | Yes |
| `late_recorded` | Record written after its event proceeded | C | A5 (SYSTEM), A1 (SYSTEM observation) | DEC-082 D82-9(b), D82-10 | — | K4 | Yes |
| `refers_to` | `audit_id` of an earlier related record | C | B1 (A5 / SYSTEM observation cases); A7 resolving an earlier UNKNOWN | DEC-082 D82-3(a), D82-9, D82-10 | — | K4 | Yes |
| `actor_type` | HUMAN, SYSTEM, Local Root Operator | R | class A | §17.18 [L] | — | K4 | No (§17) |
| `principal_id` | Principal of the Actor, where one exists | C (not for the Local Root Operator); B2 per §21.14 | class A; B2 | §17.18; A-01; A-02 | a verified or resolved `principal_id` only | K4 | No (§17) |
| `auth_context_ref` | Authentication Context reference | C (HUMAN) | class A | §17.18 [L] | reference only; never a raw assertion or bearer token | K4 | No (§17; format P2) |
| `lro_auth_ref` | "the Local Root Operator authentication reference for the bootstrap act, with semantics as established by §22 (DEC-076 D76-3(3)). §21 records the value K4 receives. It defines no authentication mechanics, format or lifecycle." | R (bootstrap A6) | A6 (bootstrap) | DEC-085 C3; DEC-076 D76-3 | reference only; no credential or secret (S19-05) | RX (K9 via P11) | No (§22) |
| `authority_basis` | Grants and Roles used or absence of a match; SYSTEM: fixed-authority basis; bootstrap: Local Root Operator bootstrap authority (A-07) | R | class A | §17.18 [L]; A-07; DEC-085 C3 | — | K4 | No (§17) |
| `capability`, `action`, `targets` | Capability, Action and resolved targets (SCC domain IDs) | C | A1–A7 | §17.18 [L] | identifiers only | K4 | No (§17) |
| `admissibility_result` | Recorded separately from the authorization result | C | A1, A2 | §17.18; A-09 [L] | — | K4 | No (§17) |
| `conditions` | Conditions evaluated, with their values | C | A1–A3 | §17.18 [L]; DEC-082 D82-14 | closed vocabulary §17.7; no DC-05 reference | K4 | No (§17) |
| `effective_tier`, `step_up` | Effective tier and step-up required | C | A1–A3 | §17.18 [L] | — | K4 | No (§17) |
| `approval_refs` | Approval evidence references and K4's verification results | C | A2–A4 | §17.18 [L] | references only; no approver private key (S19-04) | K4 | No (§17) |
| `plan_ref`, `plan_digest` | Plan reference and digest | C | A2–A5, A7 | §17.18 [L]; DEC-082 D82-13 | no Plan content, no `blob` | K4 | No (§17) |
| `authorization_ref` | Authorization Decision reference | C | A2–A5, A7 | §17.18, §17.19 [L] | — | K4 | No (§17) |
| `decision`, `reason_code` | Decision and reason code | R | class A | §17.18 [L]; DEC-085 F-1 | — | K4 | No; §21 defines no closed reason-code vocabulary or registry; values are non-normative detail [DEC-085 F-1] |
| `policy_revisions` | Policy identity and revisions (baseline and local) | C | A1–A3, A6 | §17.18; A-34 [L] | — | K4 | No (§17) |
| `revalidation_results` | Revalidation results | C | A3 | §17.18 [L] | — | K4 | No (§17) |
| `revocation_state` | Revocation state of every referenced item | C | class A | §17.18 [L] | — | K4 | No (§17) |
| `job_id` | Job identity | C | A3, A5, A7 | DEC-082 D82-13(a) | identifier only | K4 | No (§17) |
| `k6_request_ids` | K6 `request_id`(s) | C | A5, A7 | DEC-082 D82-13(a); §16.3 | identifier only | K4 | No (§16) |
| `k8_ref` | (K8 lifetime identity, `journal_seq`) | C | A5, A7 | §17.18; DEC-048 R18c; DEC-082 D82-13 | reference only | RX (K6) | No (§16; lifetime identity §19.21.2 row 1) |
| `k6_reported_outcome` | Outcome K6 reported, marked "reported by K6" | R | A7 | §17.18; A-35 [L] | no host execution facts as K4's own; no observation content; no credential values | RX (K6) | No (§16) |
| `p3_request_id` | "the request ID carried by a state-changing P3 request under §15.10, with semantics as established by the architecture that §15.10 designates (§16/§17). §21 records the value K4 receives. It defines no generation, uniqueness, transport or lifecycle semantics and applies only to state-changing P3 requests." | C (state-changing P3 requests, once defined) | A1, A2 | DEC-082 D82-13(b) (verbatim) | identifier only | RX (P3) | No |
| `condition_kind` | Kind of B-class condition | R | B1, B4 | DEC-082 D82-6, D82-9, D82-10 | — | K4 | Yes |
| `count` | Number of denial records the condition represents | R (denial B1) | B1 (denial) | DEC-085 C6 | — | K4 | Yes |
| `failure_reason` | The §17.22 step-1 check that failed | R | B2 | DEC-082 D82-12(2); §17.22 step 1 | no assertion content; no credential | K4 | Yes (as a record field); the checks are §17's |
| `claimed_assertion_id` | The assertion ID as claimed by the presented assertion, **marked unverified** | C (where present) | B2 | DEC-085 C4; DEC-082 D82-12(2) | its recording establishes neither authenticity nor attribution; no raw assertion, no claimed platform subject, no bearer credential | RX (P3) | Yes (marking); the ID format is P2's |
| `named_principal`, `anchor_digest` | As named in the anchor entry | R | B3 | §17.9 [L] | public anchor material only | RX (K11) | No (§17.9) |
| `observed_at` | Time K4 observed the change during its K11 read | R | B3 | DEC-082 D82-11(c) | — | K4 | Yes |
| `change_kind` | `added`, `revoked`, `removed` or `modified` | R | B3 | DEC-082 D82-11(c); DEC-085 §21.15 | — | K4 | Yes |
| `observer` | "observed by K4", or the changer where independent evidence establishes it | R | B3 | DEC-082 D82-11(b) | no attribution without evidence | K4 | Yes |

No other field is part of the §21 record contract. Content not listed (observation content, Plan content, host
state, assertion content, claimed platform subject) is excluded (§21.20).

## 21.8 Conditions and Evaluated Values

The record carries the conditions evaluated and their values [L §17.18; DEC-082 D82-14]. Values are recorded as
values, not references, so the field set creates no dependency on DC-05 observation evidence or health history. §21
identifies no DC-05 dependency under DEC-056 R06i and creates no DC-05 retention semantics.

## 21.9 Authorization / Plan / Job Correlation

Correlation within K4 audit uses `authorization_ref`, `plan_ref` and `plan_digest`, `job_id`, `k6_request_ids`,
`k8_ref`, and `p3_request_id` where defined [L §17.18; DEC-082 D82-13]. A Job is bound to one Plan and one Decision
[L §17.5.2; §17.22 step 11]; a Decision is identified by `authorization_ref` [L §17.19].

The chain Actor → Intent (A1) → Plan and Decision (A2) → approvals (A4) → Job revalidations (A3) → Job-step K6
requests and reported outcomes (A7) is traceable through these fields [baseline §10 "Audit correlation must exist"].
§21 defines no request-ID semantics.

## 21.10 K8 Correlation

| | §21 audit record | K8 journal record |
|---|---|---|
| Writer | K4 (C) | K6 (root) [L §15.3; T-12] |
| Store | SD-K7 (DC-11) | SD-K8 (DC-12) |
| Records | what SCC decided and why | what K6 received and did [L §16.10.3] |
| Format owner | §21 | §16 [DEC-071 D71-9] |

- K4 audit references K8 by `k8_ref` = (K8 lifetime identity, `journal_seq`) [L §17.18; DEC-048 R18c]. The
  lifetime identity's representation is a §16 Amendment Gate item (§19.21.2 row 1); §21 records it as received.
- K4 records Job-step outcomes K6 reported, marked "reported by K6" (A7). K4 does not record host execution facts as
  its own observations [L A-35]. Observation content is never copied [DEC-082 D82-10; L §16.7]. SYSTEM observation
  requests are evidenced in K8 only [DEC-085 C1].
- K7 and K8 are not one store; there is no cross-store atomicity [DEC-034].
- **What SCC may claim** [DEC-082 D82-4]: K4 ↔ K8 cross-check detection — discrepancies between K4 execution claims
  and K8 evidence (for example a K4 claim of execution with no matching K8 record).
- **What SCC may not claim**: that the cross-check proves K4 honest; detection of falsification by a compromised K4;
  protection against host or root compromise; that K8 is tamper-evident (DEC-083 assigns the K8 mechanism to the §16
  Amendment Gate, undecided); any K8 lifetime-gap representation (§16 / §22 routes).

## 21.11 Durable Recording

"Durably recorded" means the audit record is committed to SD-K7 and survives both a K4 process restart and a host
restart [DEC-082 D82-2]. This creates no storage-engine specification.

A K4 action or authorization decision that requires an audit record does not proceed when that record cannot be
durably recorded, except as DEC-035 R5b and DEC-035's statement on ordinary SYSTEM observation provide [DEC-035;
DEC-082 D82-9, D82-10]. For A6, the mutation and its record become durable atomically [DEC-034 R4a; S19-06]. A Job
does not progress past a step whose A7 record is not durable (§21.12) [DEC-085 C2]. Behaviour for each record kind is
tabulated in §21.12.

## 21.12 Audit-Write Failure

| Record | When the record cannot be durably recorded | Source |
|---|---|---|
| A1–A4 (HUMAN), HUMAN A5 | The action or decision does not proceed. No bypass. | DEC-035 R5a |
| A6 (including bootstrap) | Neither the mutation nor the record is committed. | DEC-034 R4a |
| **A5 SYSTEM revocation-triggered cancellation** | Proceeds; not delayed. The A5 record is written late once durable recording is possible, with `late_recorded` set; a **B1** record references it. | DEC-035 R5b; DEC-082 D82-9(a), (b) |
| **Denials** (A1–A3 denials and inadmissible refusals) | The denial remains a refusal. A **B1** record is written when possible containing only `condition_kind`, `timestamp`, `count` and its own identity, sequence and recording fields. It does **not** reproduce the Actor, Principal, capability, targets, authorization data or the denial record, and the denial is **not** late-recorded. | DEC-035 ("Denials"); DEC-082 D82-9(c); DEC-085 C6 |
| **B2 failed authentication** | A failed authentication is a denial (§17.22 step 1: "On any failure, deny"); the denial row applies. | §17.22 step 1 [L]; DEC-082 D82-9(c) |
| **A1 SYSTEM observation authorization** | Observation proceeds. The A1 record is written late with `late_recorded` set, and a **B1** record records the failure and references it. | DEC-082 D82-10 |
| **A7 K6-reported outcome (Job step)** | The Job does not proceed to its next step and does not reach a terminal state that requires the A7 record; K4 does not treat the Job as having progressed past that point. There is no A7 late-recording mechanism and no `late_recorded` marking for A7; B1 and R5b semantics do not extend to A7. The outcome itself is evidenced in K8. This rule applies to Job-step A7 records only and does not make every K6 request audit-fail-closed. | DEC-085 C2 |
| **B1** | Written when possible. | DEC-082 D82-9, D82-10 |
| **B3 anchor-change observation** | K4 does not treat the changed anchor set as established until the B3 record is durable. K4 MUST NOT fall back to a stale, cached, previously observed or assumed anchor set. §17.16's "K11 anchors unreadable" behaviour therefore applies: R4 is denied. No B3 late-recording rule is created; the A5 and SYSTEM-observation late-recording behaviour is unchanged. This is a reliance and authorization-state rule, not a claim that the anchor change did not occur. | §17.9, §17.16 [L]; DEC-082 D82-11; DEC-085 C7 |
| **B4 export-production failure** | Written when possible. | DEC-082 D82-6 (R3-A) |

§21 defines the B1 record contract; §22 defines the recovery and reconstruction procedure [DEC-082 D82-9(a)]. If a
pending late record (A5 SYSTEM or SYSTEM observation A1) is lost before it is written, for example on K4 restart,
its reconstruction is §22's [DEC-082 D82-10].

B1 fields: `audit_id`, `audit_seq`, `condition_kind`, `timestamp`, `recorded_at`; for the A5 SYSTEM and SYSTEM
observation cases, `refers_to` the late-recorded record; for denials, `count` and no other content (DEC-085 C6).

## 21.13 SYSTEM Observation

- SYSTEM observation authorization is an A-35 Intent Authorization (A1) and receives the required record; no new event
  kind is created [DEC-082 D82-10]. `authority_basis` is the Fixed System Authority basis [L §17.18].
- Observation data is not copied into the record; K4 is not responsible for auditing observation content. K8 remains
  the execution evidence for the resulting K6 requests, which receive no A7 record [DEC-085 C1]. If K8 is unavailable, X-29
  refusal applies [DEC-082 D82-10; L X-29].
- Observation proceeds when K7 authorization data is unavailable [L §17.1.1; §17.16], and DEC-035 imposes no
  audit-write dependency on ordinary SYSTEM observation. DEC-035 continues to govern [DEC-082 D82-10].
- When the A1 record cannot be durably recorded at the time, it is written late with `late_recorded` set and a B1
  record references it. Loss of the pending record before it is written is a §22 reconstruction matter [DEC-082
  D82-10].
- The §17.18 R0 `view` exception does not apply: SYSTEM holds no `view` Permission [L §17.1.1]. Audit volume grows
  accordingly; the owner has accepted this consequence [DEC-082 D82-10 (R5-A)].
- State-changing SYSTEM cancellation is A5 (§21.12).

## 21.14 Failed Authentication

- A failed authentication at K4 — a failure in §17.22 step 1 [L] — produces one **B2** record per attempt; aggregation
  is not permitted as a substitute [DEC-082 D82-12].
- **Unverified identifier versus verified Principal** [DEC-082 D82-12(1); L A-01; DEC-085 C4; DEC-085 §21.14]:
  - B2 may contain `claimed_assertion_id`, the assertion ID as claimed by the presented assertion, **marked
    unverified**. It identifies the attempt only. Its recording establishes neither the authenticity of the
    assertion, nor Principal attribution, nor that any claimed subject is the Actor.
  - B2 does not contain the claimed platform subject.
  - Where the assertion itself was verified and K4 resolved a Principal whose Binding or Principal-state check then
    failed, the resolved `principal_id` may be recorded as the Principal associated with the failed check. This
    never permits attribution from an unverified claim.
- `failure_reason` identifies the step-1 check that failed [DEC-082 D82-12(2)].
- Raw authentication assertions and bearer credentials are never stored [DEC-082 D82-12(3)].
- Noise control must not silently destroy required failed-authentication evidence; capacity protection must not
  simply drop required records [DEC-082 D82-12(4), (5)].
- A refusal made by K4 before authentication processing, because of an audit or capacity admission control, is not
  itself audited. §21 neither requires nor prohibits such a control. Intake limiting before K4 is not assigned to
  P2/K3 [DEC-082 D82-12].
- The owner accepts that unbounded failed-authentication volume can exhaust K4 audit capacity, after which DEC-035
  R5a refuses audited HUMAN operations [DEC-082 D82-12].
- If a B2 record cannot be durably recorded, §21.12 (denial row) applies.
- P2/K3 owns transport and request-failure semantics; K3 is not an authorization component [DEC-080].

## 21.15 Anchor-Change Observation

- K4 writes a **B3** record for each anchor change it observes when reading K11 [L §17.9; DEC-082 D82-11(a)].
- Fields: `named_principal` and `anchor_digest` [L §17.9]; `observed_at`, the time K4 observed the change during its
  K11 read; and `change_kind` [DEC-082 D82-11(c)].
- `change_kind` is one of `added`, `revoked`, `removed`, `modified` [DEC-085 §21.15]. Where the anchor representation
  defined by §22 (§17.9: "The mechanics belong to §22") does not distinguish `revoked` from `removed`, K4 records the
  state it observed and does not infer the other.
- `observer` is "observed by K4" unless the architecture has independent evidence establishing who made the change
  (for example a K9 act, which §17.9 audits as the Local Root Operator) [DEC-082 D82-11(b); L §17.9].
- The record does not claim, and must not be presented as showing, that the change was legitimate or authorized, that
  it was complete, or that no unobserved change occurred [DEC-082 D82-11]. K4 observes K11 only when it reads it.
- These records are the §21 content for the record DEC-072 D72-5 names "the anchor-legitimacy record"; that name is
  not changed and does not imply legitimacy [DEC-082 D82-6(a)].
- Write failure: K4 does not treat the changed anchor set as established until the B3 record is durable and MUST NOT
  fall back to a stale, cached, previously observed or assumed anchor set; R4 is denied (§17.16). This is a reliance
  and authorization-state rule, not a claim that the change did not occur (§21.12) [DEC-085 C7; L §17.16].

## 21.16 Audit Views and Noise Control

- R0 `view` authorization decisions are exempt from individual audit-record creation under §17.18. No aggregate
  audit record is required solely by §17.18. Denied R0 `view` decisions follow the same rule. This does not amend §17,
  does not eliminate A-35 generally, and creates no R0 audit mechanism [DEC-082 D82-8].
- R1 and above `view` decisions are individually recorded as A1 [L §17.18].
- Viewing SCC audit and K8-derived views is R1 [L §17.3; §17.5.3], so each such view is itself an A1 record. Recording
  a view does not trigger a further view; there is no recursion.
- Roles that may view audit: `scc.auditor`, `scc.operator` and `scc.administrator` (`view` ≤ R1); not `scc.viewer`
  (≤ R0) or `scc.approver` [L §17.3]. No role is created. The Local Root Operator has no audit-view power through SCC
  [L T-29]; root access to host storage is outside SCC's boundary [L §15.15].
- No other noise-control mechanism is defined. Failed-authentication and SYSTEM observation records are not reduced
  (§21.13, §21.14).

## 21.17 Retention

- K4 audit has no time-based expiry in v1; records are retained for the life of the SCC instance. Removal occurs only
  through an explicitly defined disposition consistent with DEC-042 R12A-2 [DEC-082 D82-7(a)].
- One retention rule applies to all §21 record kinds; no numerical period is set [DEC-082 D82-7(c)].
- While an audit record is authoritative and retained, its referenced K8 evidence is subject to DEC-041 R11d and must
  remain resolvable for as long as the record requires. K8 lifetime loss, reinitialization or restoration is handled
  by the established K8 lifecycle and §22 (DEC-048; DEC-047 R17g). If K8 cannot retain required evidence, K6 refuses
  new requests (X-29; S19-07) [DEC-082 D82-7(b)].
- The §19 floors apply: DEC-039 R9a, R9e, R9h; DEC-049 R19g; the `principal_id` tombstone (S19-08).
- Capacity: when a record cannot be durably recorded because capacity is exhausted, §21.12 applies. Records are not
  evicted to make room [DEC-042 R12A-2]. Thresholds and warnings are implementation detail (DEC-071 D71-5).
- Migration of §21 records (R19g) preserves each record's identity, sequence position and content. The migration
  mechanism is §22's [DEC-071 D71-6].

## 21.18 Restoration and Continuity

- Audit identity and sequence must remain unambiguous across K7 restoration. A K7 restore may roll K7 back and remove
  audit records created after the backup point (DEC-047 R17g); §21 does not assume that restarting from the restored
  state preserves uniqueness or continuity [DEC-082 D82-19].
- §21 defines no restore-generation or K7 lifecycle mechanism. Its representation is a §22 dependency (DEC-076)
  [DEC-082 D82-19].
- Recovery must not silently treat surviving K8 references to lost audit records as nonexistent (DEC-047 R17g).
  Records exported before a restore may carry identities or sequence positions the restored K7 no longer holds; this
  is part of the same §22 dependency.

## 21.19 Export

- **Content** [DEC-072 D72-5; DEC-082 D82-6(a)]: §21 audit records, including the B3 anchor-change observation
  records, which are the §21 content for the record D72-5 names. No second anchor representation is created
  [D82-6(c)]. K8 journal records are not in the §21 export set; their format and authority remain §16's.
- **Mechanism** [DEC-072; DEC-082 D82-6(b)]: an SCC-produced export artifact, consumed by the external
  root-administered facility. The facility is outside SCC's boundary, is not an SCC component and gains no SCC
  authority [DEC-072 D72-4]. It is not granted, and does not rely on, direct access to K7; T-23 is unchanged. SCC has
  no egress [L §15.4 item 6; DEC-072 D72-3].
- **Not authorization**: the artifact is not an SCC authorization mechanism and confers no authority.
- **Production barred until §19 permits it**: the artifact may not be produced until a DEC-075 D75-3 decision under the
  §19.22 route permits and classifies it (S19-01). Its lifecycle follows §19 and §22 (DEC-072 D72-6) [DEC-082
  D82-6(b)]. How export is enabled for a deployment is part of that classification.
- Artifact content preserves each record's `audit_id`, `audit_seq` and field content, so that sequence-gap detection
  (§21.5) applies to exported records. §21 defines no artifact format.
- **Failure** [DEC-082 D82-6 (R3-A)]: failure to produce the artifact for an already-created record produces a **B4**
  record (`condition_kind`, `timestamp`, `recorded_at`, and its own identity and sequence) when possible. It does not
  alter R5a or R5b, does not refuse audited operations and creates no fail-closed dependency; export remains optional
  [DEC-072 D72-1]. Failure to create the K7 record remains §21.12. Failure of the external facility is outside SCC.
- **Claims** [DEC-082 D82-6 (R-4)]: the artifact is produced by K4 (identity C) from K7 audit records. It carries no
  greater evidentiary weight than the records it contains. It can be falsified by a compromised K4 or by root
  (§17.21; §15.15). Any off-host survival depends on the external facility (DEC-072 D72-4) and cannot extend to
  content still on the host at the time of a compromise (§15.15). It claims no completeness beyond what sequence-gap
  detection shows while the writer is honest. It carries no provenance beyond its K4 production. It defines no
  cryptographic mechanism. Without export, RR-03 applies fully (DEC-072 D72-7).

## 21.20 Security and Sensitivity Boundaries

§21 records never contain:
- credential values or credential material [L T-18; S19-03; X-26], or a secret conferring bootstrap or recovery
  authority [S19-05];
- the parent-platform session [S19-04]; SCC session tokens in a form recoverable for bearer use [DEC-044 R14b];
- raw authentication assertions or a claimed platform subject [DEC-082 D82-12(3); DEC-085 C4];
- approver or release private keys [S19-04];
- host execution facts as K4's own observations, or observation or read content [L A-35; §16.7; DEC-082 D82-10];
- Plan content or `blob` content — only `plan_ref` and `plan_digest` [§21.7]; this keeps F19-05 / KF-12 exposure out of
  audit and does not reopen DEC-070 Path A;
- Integration secrets [baseline §14; X-26].

§21 creates no content inspection, resulting-content test, runtime credential detector or classifier [DEC-070]. §21
adopts no sensitivity classification scheme; CHANGE-023 remains unresolved and outside §21 [DEC-071 D71-7].

## 21.21 Non-Ownership and Explicit Boundaries

§21 does not own or redefine:
- the K8 journal, its event types, fields or writer, the K8 tamper-evidence mechanism, K8 lifetime-identity semantics,
  or K8 digests of credential-bearing content [DEC-071 D71-9; DEC-083; DEC-084];
- the §17.18 fields or any §17 authorization semantics, including reason-code meaning [DEC-085 F-1];
- DC-05 retention (§19; DEC-056);
- recovery, restoration, reconstruction, migration, bootstrap mechanics, Local Root Operator authentication and the
  meaning of `lro_auth_ref`, K9, and K8 lifetime observation (§22; DEC-076; DEC-077);
- P2/K3, including P3 request-ID semantics (DEC-080; §15.10 → §16/§17);
- CyberPanel K2;
- the external export facility (DEC-072 D72-4), and the export artifact's §19 classification, lifecycle and enablement
  (D75-3 route; DEC-072 D72-6);
- conditional §18 rewrites (SC-17; T-18-09 / SR-12; SC-09; SRF-18-11; SR-13; SR-14) [DEC-072 D72-8; DEC-082 D82-18];
- sensitivity classification (CHANGE-023);
- logs;
- storage engine, schema, implementation.

§21 defines the K4 audit ↔ K8 correlation contract without merging K7 and K8 [DEC-082 D82-21]. §21 creates no
authority for any component (K2–K11), no SCC egress and no post-lock amendment route.

## 21.22 Open Dependencies and Deferrals

| Item | Route | Blocks §21 lock? |
|---|---|---|
| K8 tamper-evidence mechanism | §16 Amendment Gate, DEC-083 (assigned; NOT SCHEDULED) | No |
| K8 digests of credential-bearing content | §16 Amendment Gate, DEC-084 | No |
| K8 lifetime identity; K6 acceptance after K8 reinitialization | §16 Amendment Gate, §19.21.2 rows 1–2 | No |
| Restore-generation representation for audit identity and sequence | §22 (DEC-076) | No |
| Reconstruction of lost pending late records | §22 | No |
| Migration mechanism | §22 (DEC-071 D71-6) | No |
| Bootstrap mechanics; Local Root Operator authentication; meaning of `lro_auth_ref` | §22 (DEC-076 D76-3) | No |
| Local Root Operator credential-lifecycle acts; K8 lifetime-change observation | §22 [DEC-082 D82-15, D82-16] | No |
| Anchor representation (`revoked` vs `removed`) | §22 (§17.9 mechanics) | No |
| Export artifact classification, lifecycle, enablement | §19.22 → DEC-075 D75-3 → DEC-063; §22 | No |
| Conditional §18 rewrites | §18 (DEC-072 D72-8) | No |

External, not §21 deferrals: P3 request-ID semantics (B1-B) — unrouted; affects the P2/K3 lock and Phase 6.
CHANGE-023 — unassigned (DEC-071 D71-7).

## 21.23 Lock Criteria

§21 may be locked when [DEC-071 D71-8]:
1. every §21-owned item is decided or explicitly deferred to a named/established gate where required;
2. ODF-18-07 is dispositioned;
3. the audit contract covers every A-35 event and every §17.18 field and introduces no host-execution facts;
4. no accepted decision widens authority, transfers responsibility between K2–K11, contradicts §15–§17, or makes an
   unauthorized §15/§16 amendment;
5. every genuine architectural deferral has an established owning route (interpreted as in D71-5);
6. no implementation authority is created, and §21 lock requires a separate explicit owner DEC.
