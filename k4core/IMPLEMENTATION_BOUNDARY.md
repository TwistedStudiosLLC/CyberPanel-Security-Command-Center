# K4 Authorization and Audit Core — Implementation Boundary Record

> **Status:** implementation record for the first PHASE 6 slice authorized by DEC-089.
> **Authority:** none of its own. This file is not architecture, is not a decision-log entry and does not amend
> DEC-089 or any locked document. Locked §15, §16, §17, §19, §21, §22, the locked P2/K3 gate, DEC-029 and DEC-089
> control this code. Where this file and those documents differ, those documents control.

## 1. Owner interpretations recorded for this slice (DEC-089 era)

The owner gave the following rulings during the DEC-089 implementation step (2026-10-03). They are **owner
interpretations made because the locked text does not specify the point**. They are not stated by §17 itself, and
this code does not present them as §17 text. They are recorded here, outside the decision log, because the owner
directed that they be recorded before coding and DEC-089 must not be modified. Recording them formally in the decision
log is a separate owner matter.

### D89-22 — Approval-required requests (owner label)

Owner wording:

> For this Phase 6 slice, when a Plan requires approval, every K6 request in the Plan is an approval-requiring request
> for purposes of §17.22 steps 9–10.
>
> - Step 10 evaluates approval evidence for each K6 request in the Plan.
> - Step 9 reaches `AUTHORIZED` only when the required evidence is present and valid for all such requests.
> - This does not mean every Plan requires approval; §17.8 still determines whether the Action/Plan requires approval.
> - `APPROVAL_REQUIRED` on a matched Grant remains effective in determining that approval is required.
> - K11's per-scope-entry `approval_required` flag remains an additional locked input/condition; it does not replace
>   the Plan-level rule.
> - Do not invent a separate WRITE-only approval rule.
>
> This is an explicit DEC-089-era owner interpretation because the locked text does not specify the request-level
> mapping.

The label "D89-22" is the owner's. DEC-089 in the decision log ends at D89-21 and is unchanged.

DEC-090 (decision log) does not adopt or ratify D89-22 and governs its flag bullet: the K11 flag is not a K4 Plan-level
approval trigger (DEC-090 D90-3).

### Grants used = every matched Grant (confirmed owner reading)

> "Grants used" means every Grant that matched, consistent with §17.4.2's requirement that K4 record every matching
> Grant. Approval determination considers all matched Grants; `APPROVAL_REQUIRED` on any matched Grant has its locked
> effect; `expires_at` uses the earliest applicable `valid_until` among the matched Grants. Do not silently select only
> the "best" or highest-priority matching Grant.

### PLAN_MAX_AGE source (confirmed owner reading; implementation reading, not a new architectural rule)

> Evaluate `PLAN_MAX_AGE` from the applicable locked policy inputs: matched Grant conditions; applicable
> release-baseline/local-settings policy where the locked policy model supplies one. If neither applicable source
> supplies a limiting value, do not invent a default maximum age.

## 2. Readings applied

Rows citing DEC-090 apply that owner decision (decision log); the others are readings of the locked text.

Each item cites the passage it rests on. Where the text leaves a choice, the reading taken is the fail-closed one and
is stated here so the owner can confirm or correct it; none grants authority the cited text does not.

| Item | Reading | Basis |
|---|---|---|
| `PLAN_MAX_AGE` timing | Not evaluated at step 4, where no Plan exists. At Decision time it is evaluated on every Grant used, whether matched at step 4 or step 7; a condition that is false, or cannot be evaluated because the Plan carries no observation time, denies the Plan (A2). | §17.11; §17.22 step 7; owner reading "used = matched" |
| `PLATFORM_ADMIN` | Implicit `PLATFORM_ROLE(PLATFORM_ADMIN)` condition on every Grant, evaluated against the Binding's latest confirmed platform role; failure is an authorization denial, not B2. Any other role value cannot be evaluated in v1 and counts as false. | §17.7; A-04; A-13; DEC-089 Q1 |
| Unidentifiable capability or unresolvable target | Refused (fail closed) and recorded as A1. | §17.16 default posture; A-32; §17.6 |
| `scc.*` requests | Evaluated through Phase I (steps 1–4, A1). Plans for them are refused as unsupported in this slice with no state or audit effect, because their step-10 approval semantics are open (Q19-04). | DEC-089 D89-11, D89-19, D89-20; §17.5.3(d) |
| Step-5 determinism rule | "Every approval-requiring request must be fully determined" is enforced before step 9, once the §17.8 approval determination is known. That determination needs the step-6 tier and the step-7 matched Grants, so it cannot be evaluated earlier. A Plan failing it is denied (A2). | §17.22 steps 5–9; §17.8; D89-22 |
| Plan identity and `INVALIDATED` | K4 generates `plan_ref` for every commit; the Plan proposal carries none. Every commit creates a new Plan; K4 deliberately establishes no Plan-change identity and links no commit to an earlier Plan or Decision. No `INVALIDATED` status is written; a denied commit has no state effect; no commit affects another Principal's Decision. The `INVALIDATED` status stays in the K7 vocabulary. | DEC-090 D90-6, D90-7(d); §17.11 (not displaced; applies once Plan-change identity is defined) |
| Anchor reliance | An anchor read becomes usable only after every B3 record for its observed changes is durable. Only the most recent read is usable; once a newer read begins, earlier reads are never relied on, including when the newer read fails or the caller reports a failed K11 read (`anchor_read_failed`). Without an established read, R4 Actions and approvals are refused. | §21.12 ("MUST NOT fall back to a stale, cached, previously observed or assumed anchor set"); §21.15; §17.16 |
| B3 times | `timestamp` and `observed_at` are K4's clock at the read, not a time supplied by the input. | §21.7 (`timestamp` "K4 clock"; `observed_at` origin K4) |
| Step-1 failures | Any step-1 failure is B2 with `UNAUTHENTICATED`, including Binding or Principal state that cannot be read or decoded from K7. Any other unreadable K7 record is K7 unavailability (§17.16: denied). If step 1 passes but the Q1 confirmation cannot be recorded, the Binding's latest confirmed role cannot be positively established, so the request is denied after step 1 and recorded as A1. | §21.6 ("Failed authentication is B2, not A1"); §21.14; P2/K3 §P.5; §17.7; §17.16 |
| Step-up and approval tier | Step-up, the approval requirement, the R4 anchor check and the separation-of-duties tier use the higher of the Action's effective tier and the Plan tier. Whether a Plan must realize its Action is not defined; it is not checked, and step 7 authorizes every (capability, target) pair in the Plan regardless. | §17.10 ("the effective tier of the Action or Plan"); §17.8; §17.22 steps 6–8; confirmed by DEC-090 D90-2 |
| K11 `approval_required` flag | Not a K4 Plan-level approval trigger; its locked effect is per request, at K6, which is untouched. K4 approval comes only from effective tier R4, a matched Grant carrying `APPROVAL_REQUIRED` and the §17.20 policy (the local setting adding `APPROVAL_REQUIRED`, or a release-baseline default step-up that includes APPROVAL). A Plan in which any step's covering scope entry is flagged, and to which none of those applies, is refused as an unsupported case (A2, `k11_flag_without_k4_approval_requirement`). Which requests inside an approval-requiring Plan need approval is not decided by DEC-090. | DEC-090 D90-3 (owner option C), D90-7(a); §17.7; §17.8; §17.20; X-16 |
| Role-subject Grants | Role Grants for evaluation come from the release baseline. A K7 Grant row whose subject is a Role the Principal holds through an effective Role Membership, in any state and whether or not it would match, is never ignored: the evaluation fails closed (`role_subject_grant_unsupported`): denied at steps 4 and 7 (A1, A2), approval rejected at step 10 (A4). Its relation to the release-defined Role is unresolved. | DEC-090 D90-5, D90-7(c); §17.16 |
| `scc.*` matching and admissibility | `ALL(read)`/`ALL(write)` cannot be evaluated for reserved `scc.*` capabilities, which have no class, so only `EXACT` and `ALL(any)` match them (fail closed). Step 3 still requires supplied admissibility facts for them. | §17.4.1; A-13; §17.22 step 3; D89-5(b) |
| Missing policy maxima | A missing configured Decision maximum, or a missing REAUTH age for a tier that needs REAUTH, makes the policy invalid for that evaluation (§17.16: denied). Local settings may set a maximum age where the baseline defines none, as a narrowing from no limit, and may only shorten one the baseline defines. | §17.19; §17.10; §17.16; §17.20 |
| Method claims | Recorded in the Decision's `authentication_context` (DC-09), with the assertion ID and authentication time; not in audit, whose field set has no slot for them. They satisfy REAUTH freshness only. | §17.2; A-18; §21.7 |
| Approval after `expires_at` | Not rejected at step 10, which lists no expiry check; the `EXPIRED` status is outside this slice. The Job-start revalidation that refuses expired Decisions is Phase IV. | §17.22 step 10; DEC-089 D89-2, D89-12 |
| Grants used at Plan commit | Plan commit is the full steps 1–9 evaluation, so Grants matched at step 4 and at step 7 are all Grants used: for the approval requirement, `expires_at` and the Decision record. | §17.13.1; §17.4.2; owner reading "used = matched" |
| Approver's Grant tier | The approver's `approve` Grant must cover the tier of the request being approved: that step's capability, re-derived from the current inputs. | §17.8 "covering the capability, target and tier"; §17.17 |
| One Decision per digest | A Plan whose `plan_digest` already has a Decision is denied (A2, `plan_already_decided`). The check is keyed on `plan_digest` only; the digest covers the K4-generated `plan_ref`, so the check links no commit to another and affects no other Decision. | A-24; DEC-090 D90-7(d) |
| Malformed Plan envelope | Input that is not a Plan proposal is refused as MALFORMED before evaluation, with no state or audit effect. Every other malformed Plan is denied at step 5 with A2, recorded under the K4-generated `plan_ref`. | §15.10 P3 ("schema-validated by K4"); P2/K3 §P.5; §17.22 step 5 |
| Stored-state strictness | K7 content that cannot be decoded, or decodes outside the stored-state contract (naive timestamps, selector values outside the closed sets, unrepresentable ages, malformed Decision bodies), is treated as unreadable: K7 unavailability, denied (§17.16). An expiry bound K4 cannot represent is denied the same way. | §17.16; A-32; S19-15 |
| Abstract input types | The abstract input types reject wrong types when constructed, before K4 sees them; a Plan proposal is the exception, because step 5 is where K4 validates it. | DEC-089 D89-17 (representation); §17.22 step 5 |
| Ambiguous anchor digest | If one `anchor_digest` names more than one Principal in the established read, the approval is rejected: the anchor cannot positively identify the approver. | §17.9; A-20; §17.16 |
| Release-baseline Role Grants | Built-in Role Grants supplied by the baseline must use the closed selectors, classes and conditions with representable ages; otherwise the policy is invalid (§17.16: denied). | §17.4.1; §17.7; A-12; A-13; §17.16 |
| Times later than K4's clock | An authentication time or newest-observation time later than K4's clock by any amount is not fresh for `AUTH_FRESH`, REAUTH, `PLAN_MAX_AGE` or the policy Plan maximum age; a time equal to K4's clock is. No tolerance. The existing denial paths apply. | DEC-090 D90-4, D90-7(b) |
| Concurrency | The A-24 duplicate check, the approval-completion check and the §22.3.2 bootstrap check are re-read inside the committing transaction. | DEC-034 R4a; A-24; §22.3.2 |
| Pending denial B1 | The count of unrecorded denials is held in memory and written as one B1 when recording is possible. It is lost if K4 restarts first; §21.12 requires only "written when possible". | §21.12; DEC-085 C6 |
| `lro_auth_ref` | K4 takes the reference from the abstract root determination for the P11 channel; it carries no secret. | §22.5.2; DEC-089 D89-15 |
| Not exercised | A3, A5, A7, B4, R5b, `late_recorded`, SYSTEM observation, `LOST`/automatic `SUSPENDED`, Decision statuses `CONSUMED`/`EXPIRED`/`REVOKED`, the `scc.*` atomic-apply path, DC-08 writes. | DEC-089 D89-7, D89-11 … D89-14 |

## 3. Implementation-level choices (not architecture)

These are representation choices permitted by DEC-089 D89-17. They are not derived from the architecture, carry no
architectural meaning and must not be cited as architecture.

- **Language:** Python 3.11, standard library only.
- **K7 representation:** SQLite (`synchronous=FULL`) at a caller-supplied path. A commit is the durability point used
  for "durably recorded" (§21.11); one SQLite transaction is the atomic unit used for R4a. Tables are internal
  representation only and create no new source of truth. A `format_version` value is stored and content in any other
  version is not interpreted (S19-15).
- **Digest:** `plan_digest` is SHA-256 over a deterministic canonical JSON encoding of the Plan content. §16.5 leaves
  canonical encoding to an implementation specification.
- **Identifiers:** `audit_id`, `authorization_ref`, `principal_id` and other K4-assigned identities are random UUIDs.
  `audit_seq` is the SQLite row position assigned at commit (recording order).
- **Abstract inputs:** frozen dataclasses in `k4core/inputs.py`. Implementers chose only their representation; their
  content and meaning are those of the locked text, DEC-089 D89-3 … D89-5 and Q1 … Q6.
- **Result codes and reason codes:** `Outcome` mirrors the P2/K3 §P.5 error-model names; reason-code strings are
  non-normative detail (§21.7, DEC-085 F-1).
- **Tests:** `unittest`.
