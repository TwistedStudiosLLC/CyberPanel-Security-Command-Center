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

### Grants used = every matched Grant (confirmed owner reading)

> "Grants used" means every Grant that matched, consistent with §17.4.2's requirement that K4 record every matching
> Grant. Approval determination considers all matched Grants; `APPROVAL_REQUIRED` on any matched Grant has its locked
> effect; `expires_at` uses the earliest applicable `valid_until` among the matched Grants. Do not silently select only
> the "best" or highest-priority matching Grant.

### PLAN_MAX_AGE source (confirmed owner reading; implementation reading, not a new architectural rule)

> Evaluate `PLAN_MAX_AGE` from the applicable locked policy inputs: matched Grant conditions; applicable
> release-baseline/local-settings policy where the locked policy model supplies one. If neither applicable source
> supplies a limiting value, do not invent a default maximum age.

## 2. Locked-text readings applied without a new rule

Each item cites the passage it rests on. Where the text leaves a choice, the reading taken is the fail-closed one and
is stated here so the owner can confirm or correct it; none grants authority the cited text does not.

| Item | Reading | Basis |
|---|---|---|
| `PLAN_MAX_AGE` timing | Not evaluated at step 4, where no Plan exists. At Decision time it is evaluated on every Grant used, whether matched at step 4 or step 7; a condition that is false, or cannot be evaluated because the Plan carries no observation time, denies the Plan (A2). | §17.11 "applies when the Decision is made"; §17.22 step 7 "and evaluate `PLAN_MAX_AGE`" |
| `PLATFORM_ADMIN` | Implicit `PLATFORM_ROLE(PLATFORM_ADMIN)` condition on every Grant, evaluated against the Binding's latest confirmed platform role; failure is an authorization denial, not B2. Any other role value cannot be evaluated in v1 and counts as false. | §17.7; A-04; A-13; DEC-089 Q1 |
| Unidentifiable capability or unresolvable target | Refused (fail closed) and recorded as A1. | §17.16 default posture; A-32; §17.6 |
| `scc.*` requests | Evaluated through Phase I (steps 1–4, A1). Plans for them are refused as unsupported in this slice with no state or audit effect, because their step-10 approval semantics are open (Q19-04). | DEC-089 D89-11, D89-19, D89-20; §17.5.3(d) |
| Step-5 determinism rule | "Every approval-requiring request must be fully determined" is enforced before step 9, once the §17.8 approval determination is known. That determination needs the step-6 tier and the step-7 matched Grants, so it cannot be evaluated earlier. A Plan failing it is denied (A2). | §17.22 steps 5–9; §17.8; D89-22 |
| Plan change → `INVALIDATED` | When a Plan with an existing `plan_ref` is committed with a different `plan_digest`, the earlier Decision's `INVALIDATED` status record is written in the same atomic commit as the A2 record of that Plan Authorization. | §17.11; §17.14; §21.6 ("The A-35 events that cause them are recorded"); DEC-034 R4a; DEC-089 Q4 |
| Anchor reliance | An anchor read becomes usable only after every B3 record for its observed changes is durable. Only the most recent read is usable; once a newer read begins, earlier reads are never relied on, including when the newer read fails or the caller reports a failed K11 read (`anchor_read_failed`). Without an established read, R4 Actions and approvals are refused. | §21.12 ("MUST NOT fall back to a stale, cached, previously observed or assumed anchor set"); §21.15; §17.16 |
| B3 times | `timestamp` and `observed_at` are K4's clock at the read, not a time supplied by the input. | §21.7 (`timestamp` "K4 clock"; `observed_at` origin K4) |
| Step-1 failures | Any step-1 failure is B2 with `UNAUTHENTICATED`, including Binding or Principal state that cannot be read or decoded from K7. Any other unreadable K7 record is K7 unavailability (§17.16: denied). If step 1 passes but the Q1 confirmation cannot be recorded, the Binding's latest confirmed role cannot be positively established, so the request is denied after step 1 and recorded as A1. | §21.6 ("Failed authentication is B2, not A1"); §21.14; P2/K3 §P.5; §17.7; §17.16 |
| Step-up and approval tier | Step-up, the approval requirement, the R4 anchor check and the separation-of-duties tier use the higher of the Action's effective tier and the Plan tier. Whether a Plan must realize its Action is not defined; it is not checked, and step 7 authorizes every (capability, target) pair in the Plan regardless. | §17.10 ("the effective tier of the Action or Plan"); §17.8; §17.22 steps 6–8 |
| K11 `approval_required` flag | A Plan step covered by a flagged scope entry adds APPROVAL to the Plan, and D89-22 then makes every request approval-requiring. This applies the owner's D89-22 bullet that the flag "remains an additional locked input/condition"; it fails closed. | D89-22; §17.7 (`APPROVAL_REQUIRED`); §17.8 K11 flags |
| Built-in Role Grants | Role Grants come only from the release baseline. K7 Grant rows whose subject is a role are not read, so K7 content cannot extend an immutable built-in Role. This slice has no path that writes Grants, so the point is not reached at runtime; it is recorded because §17.4.1 also lists a `role_id` subject. | §17.3 ("built-in, immutable, release-defined"); §17.20; §17.4.1 |
| `scc.*` matching and admissibility | `ALL(read)`/`ALL(write)` cannot be evaluated for reserved `scc.*` capabilities, which have no class, so only `EXACT` and `ALL(any)` match them (fail closed). Step 3 still requires supplied admissibility facts for them. | §17.4.1; A-13; §17.22 step 3; D89-5(b) |
| Missing policy maxima | A missing configured Decision maximum, or a missing REAUTH age for a tier that needs REAUTH, makes the policy invalid for that evaluation (§17.16: denied). Local settings may set a maximum age where the baseline defines none, as a narrowing from no limit, and may only shorten one the baseline defines. | §17.19; §17.10; §17.16; §17.20 |
| Method claims | Recorded in the Decision's `authentication_context` (DC-09), with the assertion ID and authentication time; not in audit, whose field set has no slot for them. They satisfy REAUTH freshness only. | §17.2; A-18; §21.7 |
| Approval after `expires_at` | Not rejected at step 10, which lists no expiry check; the `EXPIRED` status is outside this slice. The Job-start revalidation that refuses expired Decisions is Phase IV. | §17.22 step 10; DEC-089 D89-2, D89-12 |
| Grants used at Plan commit | Plan commit is the full steps 1–9 evaluation, so Grants matched at step 4 and at step 7 are all Grants used: for the approval requirement, `expires_at` and the Decision record. | §17.13.1; §17.4.2; owner reading "used = matched" |
| Approver's Grant tier | The approver's `approve` Grant must cover the tier of the request being approved: that step's capability, re-derived from the current inputs. | §17.8 "covering the capability, target and tier"; §17.17 |
| One Decision per digest | A Plan whose `plan_digest` already has a Decision for that `plan_ref`, in any status, is denied (A2); a changed-and-changed-back Plan does not get a second Decision. | A-24 |
| Malformed Plan envelope | A Plan that is not a Plan proposal, or has no non-empty `plan_ref`, is refused as MALFORMED before evaluation, with no state or audit effect, because no `plan_ref` exists to record an A2 against. Every other malformed Plan is denied at step 5 with A2. | §15.10 P3 ("schema-validated by K4"); P2/K3 §P.5; §17.22 step 5 |
| Stored-state strictness | K7 content that cannot be decoded, or decodes outside the stored-state contract (naive timestamps, selector values outside the closed sets, unrepresentable ages, malformed Decision bodies), is treated as unreadable: K7 unavailability, denied (§17.16). An expiry bound K4 cannot represent is denied the same way. | §17.16; A-32; S19-15 |
| Abstract input types | The abstract input types reject wrong types when constructed, before K4 sees them; a Plan proposal is the exception, because step 5 is where K4 validates it. | DEC-089 D89-17 (representation); §17.22 step 5 |
| Ambiguous anchor digest | If one `anchor_digest` names more than one Principal in the established read, the approval is rejected: the anchor cannot positively identify the approver. | §17.9; A-20; §17.16 |
| Release-baseline Role Grants | Built-in Role Grants supplied by the baseline must use the closed selectors, classes and conditions with representable ages; otherwise the policy is invalid (§17.16: denied). | §17.4.1; §17.7; A-12; A-13; §17.16 |
| Times later than K4's clock (for owner confirmation) | An `auth_time` or newest-observation time later than K4's clock counts as within any maximum age; the locked text defines freshness only as "within `max_age`". The fail-closed alternative would deny such times. | §17.7 `AUTH_FRESH`, `PLAN_MAX_AGE`; §17.10 |
| `plan_ref` reuse (for owner confirmation) | Any commit of a different `plan_digest` under an existing `plan_ref` is a Plan change and invalidates the earlier Decision, even when a different Principal commits it and is denied. `plan_ref` is supplied by the excluded K5, and the locked text does not tie a `plan_ref` to a Principal or Action. | §17.11; §17.14; DEC-089 Q4 |
| Concurrency | The A-24 duplicate check, Plan invalidation, the approval-completion check and the §22.3.2 bootstrap check are re-read inside the committing transaction. | DEC-034 R4a; A-24; §22.3.2 |
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
