> **Document status:** LOCKED [DEC-086]
> **Authority category:** 1 — Locked architecture, from DEC-086 forward (see [Authority Hierarchy](../README.md#authority-hierarchy)).
> The earlier Category 4 classification is historical [DEC-086].
> **Source:** §22 gate (PHASE 4 of DEC-025). Scope and gate structure: DEC-076. Recovery gate identity: DEC-077.
> Post-lock route: DEC-078. Phase-6 dependency: DEC-079. Dispositions, locked form and lock: DEC-086.
> **Normative:** Yes. Passages tagged [L] carry only the authority of the locked text cited; [DEC-0xx] passages point
> to the owner decision they implement. Items in §22.8 are OPEN and change only through DEC-078. Neither this
> document nor the decision log amends §15–§17, locked §19 or locked §21.
> **Findings against this text:** none recorded.
> **Implementation:** This document defines no schema, storage engine, service, protocol encoding, file format or
> installer, and creates no implementation authority (DEC-029; DEC-079).

# §22 — Lifecycle / Recovery

---

## 22.1 Purpose, Authority and Scope

§22 is the lifecycle and recovery gate, designed under DEC-025 PHASE 4 in the DEC-024 order [DEC-076 D76-1]. It is
the recovery gate referenced by locked §15–§17 [DEC-077 D77-1]. §22's status as the recovery gate grants it no
authority over K4: K4 remains the authorization point, K6 the execution enforcer and K9 the host-local administrative
interface [DEC-077 D77-3].

§22 decides only the pre-lock scope of DEC-076 D76-3:
1. Local Root Operator authority for the first-administrator bootstrap act;
2. the mechanics establishing the first `scc.administrator` membership;
3. K9 mechanics and Local Root Operator authentication for that act, including the meaning of `lro_auth_ref`;
4. the P11 K9 → K4 interface as the bootstrap act requires it;
5. the bootstrap audit record, under the contract locked §21 supplies.

Every other §22-owned subject is recorded OPEN in §22.8 and resolved only through DEC-078 [DEC-076 D76-4].

## 22.2 Governing Constraints (locked or adopted; not restated as §22 decisions)

- The first `scc.administrator` Role Membership can be created only by the Local Root Operator, through the
  host-local path (K9), and is audited as a bootstrap act; the mechanics belong to §22 [L §17.1.5; A-07].
- The Local Root Operator is an Actor, not a Principal; its authority belongs to the recovery gate except for the
  bootstrap act and root's control of K11 anchors [L §17 Terms; §17.1 Local Root Operator row].
- The bootstrap act is host-local, audited and limited to A-07; K9 stays outside the Principal model and no further K9
  powers are invented [L §17 T-29 note; §15 T-29].
- No failure condition may enable a web-reachable path that bypasses authorization or audit; recovery authority is
  host-local [L T-29]. No temporary web bootstrap [DEC-021].
- K9 is a host-local operator tool invoked only by OS root; it is a short-lived process with no persistent state
  [L §15.3 K9 row]. P11 (K9 → K4 / K6) is authenticated by OS root, host-local only, never network-exposed, and
  schema-validated; its authorization, replay and failure rules are the recovery gate's [L §15.10 P11 row].
- K7 is accessible only to identity C [L T-23]. K9 therefore cannot write authorization state directly; the bootstrap
  mutation is made by K4.
- SCC must not create, persist or rely on a secret whose possession confers bootstrap or recovery authority; bootstrap
  authority is OS root acting host-locally through K9 [DEC-045 R15a, R15d].
- A HUMAN Principal has exactly one immutable Platform Identity Binding (`platform_adapter_id`,
  `platform_instance_id`, `platform_subject_id`) [L §17.1.3]. Binding status values are CONFIRMED, UNCONFIRMED(since)
  and LOST [L §17.1.4]. In v1 a HUMAN Principal may act only while its platform identity holds `PLATFORM_ADMIN`
  [L §17.1.5].
- Roles are built-in and release-defined; no custom roles, no nesting [L §17.3; A-12]. A Role Membership is
  (principal, role, validity, state) [L §17.3].
- K4 refuses any Action that would leave no ACTIVE `scc.administrator`, except when performed by the Local Root
  Operator [L A-15].
- For every K4 authorization-state mutation for which §17 requires an audit record, the mutation and the record
  become durable atomically [DEC-034 R4a; S19-06].
- The bootstrap A6 record: `actor_type` = Local Root Operator; `authority_basis` = Local Root Operator bootstrap
  authority (A-07); `lro_auth_ref` — "the Local Root Operator authentication reference for the bootstrap act, with
  semantics as established by §22 (DEC-076 D76-3(3)). §21 records the value K4 receives. It defines no authentication
  mechanics, format or lifecycle." [L §21.6, §21.7; DEC-085 C3].

## 22.3 Local Root Operator Authority for the Bootstrap Act (D76-3(1))

1. [DEC-086] The Local Root Operator's bootstrap authority is exactly the authority to originate the first
   `scc.administrator` Role Membership in the SCC instance [L A-07; T-29]. It is not a Grant, a Role or a Permission,
   and it is not K7-derived [L §17 Terms].
2. [DEC-086] **"First."** The bootstrap act is available only while K7 holds no `scc.administrator` Role Membership record
   in any state. Once any such record exists, the bootstrap act is refused. Restoring authority after the loss of
   every administrator is recovery (§17.24 P-5), not bootstrap, and is OPEN (§22.8).
3. [DEC-086] The bootstrap act grants nothing else: no other Role, no direct Grant, no approver anchor, no credential, no
   K6 request, no policy change.
4. The bootstrap act also creates the HUMAN Principal that receives the first membership. Principal creation and
   membership creation are part of the same narrow bootstrap act. This creates no general Principal-management
   capability and grants K9 no general authority over K7, K4, memberships, roles or other state [DEC-086].

## 22.4 First `scc.administrator` Membership Mechanics (D76-3(2))

1. [DEC-086] **Input.** The Local Root Operator supplies, through K9 over P11, the Platform Identity Binding tuple for the
   Principal to be created.
2. [DEC-086] **Effect.** K4 creates one Role Membership (principal, `scc.administrator`, validity, `ACTIVE`) [L §17.3],
   and the HUMAN Principal in state `ACTIVE` with no Grants and its Platform Identity Binding in
   status `UNCONFIRMED(since)` [L §17.1.4, §17.1.5]. The Binding becomes CONFIRMED only through a verified assertion
   or the platform observation §17.1.4 names; until then, and while the platform identity does not hold
   `PLATFORM_ADMIN`, the Principal cannot act [L §17.1.4, §17.1.5; A-01].
3. [DEC-086] **Validity.** The membership has no expiry set by the bootstrap act; validity follows §17 Role Membership
   rules.
4. [DEC-086] **Atomicity.** All bootstrap mutations and their A6 record(s) become durable in one atomic K7 commit
   [DEC-034 R4a]. If any part cannot be committed, nothing is committed and no partial state results.
5. [DEC-086] **Platform subject.** §22 does not define `platform_subject_id` format or stability; these are the Platform
   Adapter's [L §17.1.3; §17.24 P-6].
6. Nothing in §22 creates an alternative path to a first administrator: no web path, no K2 or K3 path, no default or
   implicit administrator, no installer-created administrator [DEC-021; T-29].

## 22.5 K9 Mechanics and Local Root Operator Authentication (D76-3(3))

1. [DEC-086] **Authentication.** The Local Root Operator is authenticated by OS-enforced peer identity: K4 accepts a P11
   bootstrap request only on a host-local channel on which the operating system establishes that the caller runs as
   root [L §15.3 K9 row; §15.10 P11 row]. No password, token, key or other secret confers or proves bootstrap
   authority [DEC-045 R15a].
2. [DEC-086] **`lro_auth_ref` meaning.** `lro_auth_ref` is K4's reference to the OS-enforced peer-identity determination
   it made for the P11 channel carrying the bootstrap request. It identifies that the caller was established as root
   by the operating system at the time of the act. It carries no secret and is not a credential; it is not reusable as
   authority. §22 defines no format for it [DEC-085 C3; L §21.7].
3. [DEC-086] **K9 role.** K9 is a short-lived, root-invoked host-local tool with no persistent state [L §15.3]. For the
   bootstrap act it only conveys the Local Root Operator's request to K4 over P11 and reports K4's result. It holds no
   SCC authority of its own, makes no authorization decision and does not access K7 [L T-23; DEC-077 D77-3].
4. K9's other operations, its code provenance and installation (K11 placement), and any K9 → K6 path are OPEN
   (§22.8).

## 22.6 P11 K9 → K4 Interface for Bootstrap (D76-3(4))

[DEC-086] The architectural contract of the P11 bootstrap request:

| Property | Contract | Basis |
|---|---|---|
| Direction | K9 → K4 only; no K9 → K6 for bootstrap | D76-3(4) |
| Exposure | Host-local only; never network-exposed; not reachable through K1, K2, K3 or any web path | [L §15.10 P11; T-29; DEC-021] |
| Authentication | OS-enforced peer identity = root (§22.5) | [L §15.10 P11] |
| Authorization | K4 accepts the request only if §22.3 applies (no prior `scc.administrator` membership record). Basis: A-07. No Grant evaluation. | [L A-07] |
| Content | The target per §22.4.1; nothing else that confers authority | §22.4 |
| Validation | Schema-validated by K4; malformed requests refused | [L §15.10 P11] |
| Replay | A repeated or replayed bootstrap request is refused, because the first act leaves a membership record (§22.3.2) | §22.3 |
| Result | K4 reports success or refusal and the refusal reason to K9; K9 reports it to the operator | — |
| Failure | Atomic: nothing is committed unless all mutations and the A6 record commit (§22.4.4). If K4 or K7 is unavailable, bootstrap is unavailable; no fallback, no direct K7 write, no bypass | [DEC-034 R4a; L T-23; T-29] |

§22 defines no transport, encoding, command syntax or endpoint.

## 22.7 Bootstrap Audit Record (D76-3(5))

1. The bootstrap act is recorded as a §21 A6 record with `actor_type` = Local Root Operator, `authority_basis` = Local
   Root Operator bootstrap authority (A-07), and `lro_auth_ref` as defined in §22.5.2 [L §21.6, §21.7; DEC-085 C3].
   `principal_id` is not set for the Actor [L §21.7]; the Principal receiving the membership is in `targets`.
2. [DEC-086] One A6 record is written for each bootstrap mutation (Principal creation; membership), all
   in the same atomic commit as the mutations (§22.4.4).
3. If the A6 record cannot be durably recorded, the bootstrap act is not committed [DEC-034 R4a; L §21.12].
4. §22 does not change any §21 field, class or rule.

## 22.8 Items Recorded OPEN (resolved only through DEC-078)

Each item below is OPEN in §22 and changes locked §22 text only through a new DEC under DEC-078 D78-1 … D78-4.

| # | Item | Source |
|---|---|---|
| O-1 | Recovery of authority after loss of every administrator; K9 authority beyond the bootstrap act | §17.24 P-5; TQ-02 |
| O-2 | K9 operations other than bootstrap; whether K9 may reach K6 (P11 K9 → K6) | §15.18 OQ-6 |
| O-3 | K9 code provenance and K11 installer placement | §15.18 OQ-6; DEC-079 D79-4 |
| O-4 | K2 assertion-key (re)provisioning; K2 re-registration after platform upgrades | §15.18 OQ-6; §15.14 |
| O-5 | Local Root Operator credential provisioning, rotation, revocation and destruction mechanics and their recording | DEC-046 R16c, R16h; DEC-082 D82-15 |
| O-6 | Approver anchor provisioning and revocation mechanics; anchor representation (`revoked` vs `removed`) | §16.15 Q-1; §17.9; §21.15 |
| O-7 | Approver key custody and approval-tool mechanics | §17.24 P-1; TQ-01; ODF-18-08 (conditional) |
| O-8 | K7 backup and restore; restore generations and audit identity/sequence continuity | DEC-047; DEC-082 D82-19; §21.18 |
| O-9 | Reconstruction of lost pending late-recorded audit records | DEC-082 D82-9, D82-10; §21.12 |
| O-10 | Migration of K7 audit history and other state; downgrade | DEC-049; CHANGE-025; TQ-06 |
| O-11 | K8 lifetime, loss, reinitialization and recovery mechanics; K8 lifetime-change observation | DEC-048; §19.21.2 rows 1–2; DEC-082 D82-16 |
| O-12 | SCC removal and data disposition; release-key custody and rollback protection | §19.22; TQ-06 |
| O-13 | Pre-image visibility for approvers of `file.replace` | TQ-07 |
| O-14 | §16.15 Q-4, Q-5, Q-7 (refresh) | §16.15 |
| O-15 | Assertion verification material placement and provisioning, in DEC-051 coordination | OD19-01 |
| O-16 | Remaining DEC-071 D71-6 hand-offs and §19.22 rows naming §22 | DEC-071 D71-6; §19.22 |
| O-17 | DC-01 / DC-02 R4 owner dependency | DEC-066 |
| O-18 | Export artifact lifecycle (with the DEC-075 D75-3 §19 decision) | DEC-072 D72-6; DEC-082 D82-6 |

## 22.9 Non-Effects and Boundaries

§22 does not: amend §15, §16, §17, locked §19 or locked §21; give §22 or K9 authority over K4 [DEC-077 D77-3]; create a
web, K2 or K3 bootstrap or recovery path; create any secret, token or credential scheme; touch any §16 Amendment Gate
item (DEC-083, DEC-084, §19.21.2); decide export, CyberPanel K2 or P2/K3 matters; or create implementation authority.

## 22.10 Lock Criteria [DEC-076 D76-7]

§22 may be locked when: (1) every D76-3 item is decided; (2) every other §22-owned item is decided, deferred to an
established gate, or recorded as open under DEC-078; (3) no accepted decision widens authority, transfers
responsibility between K2–K11, contradicts §15–§17, or makes an unauthorized §15/§16/§17 amendment; (4) no
web-reachable recovery or bootstrap path is created (T-29; DEC-021); (5) every deferral names its owning gate;
(6) no implementation authority is created, and the lock is a separate explicit owner DEC.
