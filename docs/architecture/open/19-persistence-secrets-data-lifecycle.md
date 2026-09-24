> **Document status:** CANDIDATE — OWNER DISPOSITIONS RECORDED — NOT LOCKED [DEC-064]
> **Authority category:** 4 — Conditional/open architecture (see [Authority Hierarchy](../README.md#authority-hierarchy))
> **Source:** §19 architecture gate (PHASE 2 of DEC-025). Replaces the earlier "NOT DESIGNED — GATE PENDING" stub.
> Owner dispositions: DEC-031 … DEC-062. Post-lock resolution route: DEC-063. Change-set reconciliation
> decisions: DEC-064.
> **Normative:** **No.** §19 is not locked. A passage tagged **[DEC-0xx]** points to the owner decision it implements.
> The decision log holds the complete owner wording and is its authoritative record (Category 2). A passage marked
> *verbatim* reproduces the cited owner text exactly. Passages tagged **[LOCKED-DERIVED]** carry only the authority of
> the locked text cited. Items marked OPEN or DEFERRED carry no authority beyond the requirement that they be resolved
> at the gate named for them. Neither this document nor the decision log amends or locks §15–§17.
> **Implementation:** This document defines no schema, storage engine, key-management product, algorithm, service or
> installer. It must not be used as an implementation specification until the owner locks it.

# §19 — Persistence, Secrets & Data Lifecycle (Candidate)

---

## 19.1 Purpose

§19 defines the architectural contract for everything SCC keeps, references or must never keep:
- which data classes exist;
- which storage domain holds each one, and who owns, reads and writes it;
- which secrets exist, who holds them, and whether SCC stores the material or only a reference;
- how data and secrets are retained, rotated, revoked and destroyed;
- what persistence must guarantee when components fail;
- which consequences §21 (audit), §22 (lifecycle/recovery), P2 and the CyberPanel K2 gate must later honour, and which
  items the §16 Amendment Gate (not scheduled) must consider (§19.21.2).

It fits inside the locked §15–§17 constraints and does not redefine them.

## 19.2 Scope

**In scope:** data classification; storage domains; ownership and access; secret and credential placement;
lifecycle, retention, deletion, rotation and revocation semantics; failure consequences for persistence;
backup/restore, upgrade/migration and recovery *dependencies*; cross-boundary data flow; security invariants.

**Out of scope (owned elsewhere):**

| Topic | Owner |
|---|---|
| Storage engine, schema, tables, indexes, migrations | Implementation (after lock) |
| Audit record format, event model, audit retention periods, audit noise | §21 |
| Tamper-evidence mechanism and off-host export | §21 / ODF-18-07 (see §19.20) |
| Install, bootstrap, provisioning, backup/restore procedures, recovery protocol, key custody mechanics | §22 / recovery gate |
| Reconciliation, desired state, drift records | §20 |
| Assertion format, SCC session semantics, K2↔K3 transport | P2 |
| CyberPanel identity fields, presentation, installation | CyberPanel K2 gate |
| Cryptographic algorithms and key-management products | Not decided; no locked requirement forces a choice at this gate |

## 19.3 Authority

This document is Category 4 (conditional/open). Where it conflicts with §15, §16, §17 or the decision log, those
control. Where it conflicts with the foundational baseline, this candidate does **not** override the baseline until
locked; conflicts are listed in §19.5.3. Historical material (forensic audit, §18 gate review) is evidence only.

## 19.4 Governing Locked Constraints

The following are binding on §19. They are cited, not restated in full.

| ID | Constraint | Source |
|---|---|---|
| LC-01 | K7 is the SCC State Store for durable SCC data: inventory, registry state, Jobs, audit, authorization metadata, configuration. Engine deferred. | §15.3 (K7 row) |
| LC-02 | K7 MUST be accessible only to identity C and MUST NOT be hosted in, or depend on credentials of, the parent platform's data store. | T-23; §15.14 |
| LC-03 | K8 is an append-only record written only by K6, root-owned, readable by C. | §15.3 (K8 row); T-12; §15.10 P9 |
| LC-04 | Credential placement by class, including: Security System and platform administrative credentials only in K6; never plaintext in K7; platform session never persisted by K3; assertion signing key only in K2; verification material in K4; no transferable IPC secrets. | §15.12; T-18, T-19, T-20 |
| LC-05 | K11 is root-owned and not writable by W, C or I. It holds SCC code, declarations and public trust anchors. | T-21; §15.3 (K11 row) |
| LC-06 | SCC security-critical components and persistent state must not reside in, run under, or be supervised by anything the parent platform's update lifecycle manages. K2 is the sole permitted artifact in the platform's domain. | T-25; §15.14 |
| LC-07 | Loss of any component must never cause a Security System to be represented as absent. | T-28 |
| LC-08 | K7 unavailable → all state-changing actions refused; observation may run but cannot be recorded durably. | §15.13; §17.16 |
| LC-09 | §15 assigns to §18/§19: the tamper-evidence mechanism for K7 audit and K8, off-host export, and the audit fail-closed policy. | §15.10 P9; §15.13 note; §15.15; §15.18 OQ-5 |
| LC-10 | Credentials exist only in "K6's root-only credential storage"; handles are defined in K11 declarations; no request field carries credential material into K6; provisioning is §19/§22. | §16.9 |
| LC-11 | K8 is written before any result is reported; if K8 is unwritable K6 refuses all new requests; dangling intents become UNKNOWN on start. | X-27, X-28, X-29, X-30 |
| LC-12 | K8 retention must cover at least the replay acceptance window; used approval nonces are checked against K8. | §16.11; X-16, X-31 |
| LC-13 | `file.replace` stages content in a K6-internal location, commits atomically where supported, and retains the pre-image where declared. | §16.1.3; §16.8 |
| LC-14 | Reads journal metadata and a content digest only, never content. Exposure modes limit what K6 returns; credential-bearing resources are never `FULL`; resolved credential values are scrubbed. | §16.7; X-24; X-25 |
| LC-15 | Authorization state lives in K7: Principals, Bindings, Role Memberships, Grants, Decisions (immutable) with append-only status records, approvals, local policy revisions. | §17.1–§17.20 |
| LC-16 | `principal_id` is never reused; REVOKED is terminal. | §17.1.4 |
| LC-17 | K4-internal Actions are applied to K7 atomically together with their audit record. | §17.22 |
| LC-18 | K4 records every authorization event with the §17.18 fields. | A-35 |
| LC-19 | No authorization caching in v1. | A-33 |
| LC-20 | Approver anchors live in K11 and are controlled by root; approver keys are held outside SCC components. | §17.9; §17 Gate Assessment (T-18/T-19 line) |
| LC-21 | The first `scc.administrator` membership originates only from the Local Root Operator; no web bootstrap. | A-07; DEC-021 |

## 19.5 Existing Evidence

### 19.5.1 Classification of relevant statements

| Statement | Location | Classification |
|---|---|---|
| LC-01 … LC-21 | §15, §16, §17 | LOCKED |
| "Sensitive evidence must be handled appropriately." | Baseline §3 | CURRENT FOUNDATIONAL |
| "Sensitive Job data must be protected." / "Job retention and cleanup must be defined." | Baseline §8 | CURRENT FOUNDATIONAL |
| "Secrets and credentials must be minimized and redacted." / "Credential scope must be limited." | Baseline §9 | CURRENT FOUNDATIONAL (refined by §15.12, §16.9) |
| "Audit should be append-only and integrity-protected." | Baseline §10 | CURRENT principle; mechanism OPEN (ANN-17) |
| "SCC owns its own data: inventory, Integration registry, health history, Jobs, audit, authorization metadata, SCC configuration" | Baseline §11 | CURRENT; design OPEN (ANN-20) |
| "SCC should avoid duplicating CyberPanel-owned data unnecessarily." | Baseline §11 | CURRENT FOUNDATIONAL |
| "Backups should be made where SCC data/configuration may be modified." / "Audit history must survive upgrades." / "Schema migrations must be versioned, deterministic, recoverable where practical, idempotent where practical" / "Configuration must be preserved unless explicitly migrated." | Baseline §12 | CURRENT FOUNDATIONAL |
| "Recovery mode is required…" (as a web UI) | Baseline §12, §13 | SUPERSEDED (ANN-22) |
| "Health history should be supported." | Baseline §7 | CURRENT FOUNDATIONAL; retention OPEN — OD19-06 [DEC-056] |
| "Integration-specific configuration belongs within the Integration boundary." | Baseline §14 | Placement addressed by owner decision [DEC-037]. Write path and permitted contents remain OPEN [DEC-037 R7c, R7d]. Baseline text not annotated (ANN-33 deferred) [DEC-064]. |
| "Integration secrets must be protected and excluded from ordinary logs and audit records." | Baseline §14 | CURRENT FOUNDATIONAL (refined by X-26) |
| SR-12 … SR-17; T-18-09, T-18-11, T-18-13; TF-18-09; CLF-18-07; ODF-18-07 | §18 candidate / gate review / owner-decision gate | OPEN (conditional §18; not authority) |
| MED-09, MED-13, MED-14, HIGH-13; CHANGE-015, CHANGE-023, CHANGE-025 | Forensic audit | HISTORICAL (standing in the open register §7) |

### 19.5.2 What the locked text already decides

The locked sections already decide *where* several classes live (K7, K8, K11, K6, K2) and several failure behaviours.
They do **not** decide: retention periods beyond the replay window; the K6 storage areas' structure; rotation and
destruction semantics; backup scope; at-rest encryption; sensitivity classification; the placement of assertion
verification material; or how K4 learns credential-handle status.

### 19.5.3 Disagreements and gaps found (not silently resolved)

| ID | Disagreement / gap | Documents | Disposition in this candidate |
|---|---|---|---|
| D19-01 | T-12 says K6 refuses **write-class** operations when K8 is unwritable; §15.13 says reads continue "if §16 allows"; X-29 refuses **all** new requests. | §15 T-12, §15.13 vs §16 X-29 | Not a contradiction: §15 left read continuation to §16, and §16 (later, locked) decided. Recorded for completeness. |
| D19-02 | Baseline §14 places Integration-specific configuration "within the Integration boundary", but K5 has no host access beyond its runtime (T-06), so an Integration cannot persist anything itself. | Baseline §14 vs §15 T-06 | Placement addressed [DEC-037]; write path and permitted contents OPEN [DEC-037 R7c, R7d]. |
| D19-03 | §16.9 and §16.8 refer to K6 credential storage and retained pre-images, but §15's component catalogue names no persistent storage in the privileged domain other than K8. | §16.9, §16.8 vs §15.3 | Addressed [DEC-032]. |
| D19-04 | §15.12 says assertion verification material exists "only in K4" but does not say where it is persisted or who provisions it; §15.14 says K2 key re-provisioning is a K9/lifecycle operation. | §15.12 vs §15.14 | OPEN — OD19-01 [DEC-051]. No authoritative home is assigned to DC-18. |
| D19-05 | Credential-bearing content written through `file.replace` would pass through K4 (and K7, if the Plan is persisted) as a plaintext `blob`, which conflicts with the intent of T-18 (such credentials only in K6). §16 provides handle substitution only for profile slots, not for staged file content. | §16.1.5, §16.8 vs T-18, §15.12 | Finding F19-05 — deferred to OD19-04 and the §16 Amendment Gate [DEC-058]. Interpretation OPEN [DEC-058 F05a]. Not in the known-findings index while OD19-04 is open [DEC-058 F05d]. |
| D19-06 | Finding F19-06, as decomposed in DEC-059 (F06a). | §16.5, X-16, §16.11 | Horizon: OD19-03. Approval evidence after K8 loss: §22 and the §16 Amendment Gate. Nonce retention: [DEC-041 R11b; DEC-053 R03b]. [DEC-059] |
| D19-07 | K4 needs to know whether a credential handle is provisioned (to show a capability as unavailable before planning), but no `executor.*` Operation reports handle status, and provisioning is not a K6 request (so it is not journaled as one). | §16.1.3 (executor family), §16.9 | Rejected as a finding against locked text [DEC-060]. OD19-05 remains OPEN. |
| D19-08 | Finding F19-08, split into two surfaces [DEC-061 F08a]. | §16.9 | Provisioning: governed by [DEC-046 R16c, R16j]. Operation output: OPEN — §16 Amendment Gate [DEC-061 F08c, F08d]. |
| D19-09 | *Verbatim (DEC-062 F09a):* F19-09 concerns the recovery problem that an authorized restoration of SD-K7 to an earlier backup point may omit authoritative Principal, Role Membership, Grant, or other authorization-state changes made after that backup point. The finding does not assert that all revocation information exists only in K7, and does not apply to revocation or state represented authoritatively in other domains such as K11. | §17.14; §18 TH-32 / SR-16 (conditional) | Deferred to §22 / recovery gate; TQ-08; ODF-18-07 [DEC-062]. |

## 19.6 Terminology

- **Data class (DC):** a category of information. Ownership and storage-domain rule: S19-01 [DEC-031 R1]. Meaning of
  'owner': [DEC-031 R4].
- **Storage domain (SD):** a place data may durably reside, defined by its access boundary.
- **Secret material:** a value whose disclosure grants authority (credential, private key, bearer token).
- **Credential metadata:** non-secret facts about a credential (handle ID, provisioning state, version, timestamps).
- **Opaque reference:** an identifier that designates secret material without revealing or deriving it (for
  example a `handle_ref`).
- **Transient:** held only in process memory for the duration of one operation or session; never written to durable
  storage.
- **Destruction:** making secret material unusable by SCC and removing SCC's copies. **Not** a claim of physical
  erasure (§19.13).
- **Tombstone:** a retained minimal record proving that an identifier existed and must not be reused.

### Storage domains

| SD | Name | Access boundary | Basis |
|---|---|---|---|
| SD-K7 | SCC State Store | Identity C only (read/write) | LC-01, LC-02 |
| SD-K8 | Executor Journal | K6 append; C read; root | LC-03 |
| SD-K11R | K11 release-signed content | Root write; K4, K5 loader, K6 read | LC-05; §16.2 |
| SD-K11H | K11 host-local root-authored content | Root write; K4, K6 read | §16.2.2; §17.9 |
| SD-K6P | K6 Privileged Storage [DEC-032]: Credential Store (CS), Pre-image Store (PI), Staging Area (ST) | root only (K6) | §16.8, §16.9 (D19-03) |
| SD-K2 | K2 platform-side material | Platform domain (K1/K2) | LC-04 (T-20); §15.14 |
| SD-PLAT | Parent-platform state | Platform; **not SCC** | §15.5 |
| SD-HOST | Host / Security System state | Host; **not SCC** | §15.15 |
| SD-OFF | Off-host (approver keys, release signing keys, any exports) | Outside the host | §17.9; §18 (conditional) |
| TRANSIENT | Process memory | The holding process only | — |

## 19.7 Data / State Classification

| DC | Data class | Storage domain | Owner | Writers | Readers | Re-derivable? | Basis |
|---|---|---|---|---|---|---|---|
| DC-01 | SCC release content: code, Operation Catalogue, Global Execution Policy, Execution Declarations (incl. credential **handle definitions**), release trust anchors | SD-K11R | Release / Local Root Operator (install) | root via lifecycle | K4, K5 loader, K6 | From the release artifact | LC-05; §16.2 |
| DC-02 | Host-local root configuration: approver anchor set, Host Restriction Overlay, local package-source changes (if §22 permits) | SD-K11H | Local Root Operator | root only | K4, K6 | No | §16.2.2; §17.9 |
| DC-03 | K4 operational configuration writable by C, within the limits of [DEC-036 R6a–R6c] | SD-K7 | K4 | C | C | No | LC-01; DEC-036 |
| DC-04 | Authoritative domain state: inventory, Security System records, registry state, compatibility determinations, health reports | SD-K7 | K4 | C | C | **Largely yes** (by re-observation) | LC-01; §15.7 |
| DC-05 | Observation evidence and health history (content limited by exposure modes) | SD-K7 | K4 | C | C | Current values yes; history no | LC-14; baseline §7; retention OPEN — OD19-06 [DEC-056] |
| DC-06 | Integration-specific configuration (per `integration_id`) | SD-K7 | K4 (on the Integration's behalf) | C | C; passed to K5 per call | No | D19-02; DEC-037 |
| DC-07 | Authorization state: Principals (incl. tombstones), Platform Identity Bindings, Role Memberships, Grants, revocation records | SD-K7 | K4 | C | C | **No** | LC-15, LC-16; tombstones [DEC-038] |
| DC-08 | Authorization policy local settings and their revisions | SD-K7 | K4 | C (R4 `scc.*` Action) | C | No | §17.20 |
| DC-09 | Authorization Decisions (immutable) and their append-only status records; Approval Records | SD-K7 | K4 | C (append-only semantics) | C | No | §17.19; LC-15 |
| DC-10 | Plans and Jobs (Plan content, `plan_digest`, Job state) | SD-K7 | K4 | C | C | No | §17.11, §17.12 |
| DC-11 | K4 audit records | SD-K7 | K4 | C (append-only semantics) | C | No | LC-01; LC-17; LC-18; format §21 |
| DC-12 | K8 executor journal records (incl. request IDs, idempotency keys, used approval nonces, dangling intents, approval-evidence verification results) | SD-K8 | K6 | K6 (append) | C, root | **No** | LC-03, LC-11, LC-12 |
| DC-13 | Credential secret material | SD-K6P / CS | K6 | Local Root Operator, through the host-local lifecycle mechanism [DEC-046 R16c]; mechanics §22 | K6 only, at invocation | No | LC-04, LC-10 |
| DC-14 | Credential metadata (handle ID, provisioning state, material version, timestamps) | SD-K6P / CS (authoritative); definitions in DC-01 | K6 | Per §22 [DEC-046 R16a, R16c] | K6; K4 visibility OPEN — OD19-05 [DEC-055] | No | LC-10 |
| DC-15 | Retained pre-images of replaced files | SD-K6P / PI | K6 | K6 | K6 (via `file.restore_preimage`) | No | LC-13 |
| DC-16 | Staged content for `file.replace` | SD-K6P / ST | K6 | K6 | K6 | n/a (transient-durable, discarded at restart) | LC-13; §16.12 |
| DC-17 | Assertion signing key (K2) | SD-K2 | K2 (platform domain) | Provisioning (P2 / §22) | K2 only | No | T-20; §15.14 |
| DC-18 | Assertion verification material | OPEN — OD19-01; no authoritative domain assigned [DEC-051 R01a] | OPEN — OD19-01 | OPEN — OD19-01 | K4 | No | §15.12; D19-04 |
| DC-19 | SCC session validation state | TBD by P2 | K4 | C | C | — | §15.12; P2 |
| DC-20 | Platform state (sessions, ACLs, accounts, platform configuration) | SD-PLAT | Parent platform | Platform | — | — | §15.5 |
| DC-21 | Host / Security System state (configurations, logs, services) | SD-HOST | Host / administrators | Host; SCC only via K6 WRITE Operations | K6 | — | §15.15 |
| DC-22 | Approver private keys | SD-OFF or operator-managed host location outside W/C/I (custody per ODF-18-08) | Approver | Approver | Approval environment | — | §17.9; LC-20 |
| DC-23 | Release signing private keys | SD-OFF | Release owner | — | — | — | §16.2 (anchors are public); §22 |
| DC-24 | Transient values: resolved credential values, platform session cookies in transit, identity assertions in transit, approval evidence in transit, raw observation content before K4 persistence | TRANSIENT | Holding process | — | — | — | LC-04, LC-14 |

**Not a data class SCC holds:** IPC authentication secrets. §15.12 establishes OS peer identity, so no transferable
IPC secret exists [LOCKED-DERIVED].

## 19.8 Persistence Ownership Model

1. **One authoritative owner and storage domain per data class.** See S19-01 [DEC-031 R1, R3, R4].
2. **Storage domains stay distinct.** See S19-02 [DEC-031 R2].
3. **K3 and K5 persist nothing.** K3 holds no state (§15.6, T-30); K5 cannot persist beyond its runtime (T-06). Any
   durable state an Integration needs is held by K4 in K7 (DC-06). [LOCKED-DERIVED for K3/K5; DEC-037 for DC-06]
4. **Platform and host state are not SCC state.** SCC persists only what it needs to identify, observe and audit
   them: the Platform Identity Binding and non-authoritative display names (DC-07); observation evidence limited by
   exposure modes (DC-05). SCC does not keep copies of platform data it does not need (baseline §11).
5. **Re-derivable vs non-re-derivable.** Domain state (DC-04) can be rebuilt by re-observation, so its loss is an
   availability loss (LC-07). Authorization state, Decisions, Plans/Jobs, audit, K8 and credentials (DC-07 … DC-13)
   cannot be rebuilt, so their loss is security-relevant. Reliance on authorization state that K4 cannot establish as
   valid: [DEC-034 R4b]. Other failure consequences: §19.15.

## 19.9 Secret / Credential Ownership Model

| Secret | Owner | Where material lives | SCC stores material or reference? | Plaintext persisted? | May cross K2/K3/K4/K6? | Basis |
|---|---|---|---|---|---|---|
| Security System credentials (API keys, admin tokens, socket access) | K6 | SD-K6P / CS | **Material in K6 only**; everyone else holds `handle_ref` | Only inside SD-K6P. At-rest encryption: OPEN — OD19-02 [DEC-052]. Ciphertext outside SD-K6P: OPEN — Q19-01. | **Never** leaves K6 | LC-04, LC-10 |
| Parent-platform administrative / API credentials | K6 | SD-K6P / CS (only where no lower-impact read path exists) | Material in K6 only | Only inside SD-K6P | Never leaves K6 | §15.12 |
| Endpoint credentials (for `endpoint.call`) | K6 | SD-K6P / CS | Material in K6; sent only after endpoint identity check | Only inside SD-K6P | Never leaves K6 except to the verified endpoint | X-35; §16.9 |
| Parent-platform session | Platform | SD-PLAT; browser | Neither | Never by SCC | K3 may see it in transit and must strip it | §15.12; T-19 |
| Identity-assertion signing key | K2 | SD-K2 | Not by SCC Core | Platform-domain storage only | Never leaves K2 | T-20 |
| Assertion verification material | K4 (use) | OPEN — OD19-01 [DEC-051] | Public material | n/a (public) | K4 only uses it | §15.12 |
| SCC session tokens | K4 | TRANSIENT at K3; K4 validation state per P2 | K4 validation state only | See S19-14 [DEC-044 R14b] | Browser ↔ K3 ↔ K4 | §15.12; P2 |
| P2 session validation or issuance key (only if P2 requires a persistent one) | Custody not established [DEC-044 R14d] | Custody not established [DEC-044 R14d] | Custody not established [DEC-044 R14d] | Custody not established [DEC-044 R14d] | Custody not established [DEC-044 R14d] | Custody not established [DEC-044 R14d] |
| Approver private keys | Approver | SD-OFF or operator-managed location outside W/C/I | **Neither.** SCC holds only public anchors (DC-02) | Never by SCC | Never enters SCC; only signatures do | §17.9; A-22; DEC-043 |
| Release signing private keys | Release owner | SD-OFF | Neither; SCC holds public trust anchors | Never by SCC | Never | §16.2; §22 |
| Encryption keys protecting SCC data at rest (if adopted) | OPEN — OD19-02 [DEC-052]; if adopted, a separately governed class [DEC-052 R02d]. SCC backups/exports: S19-09 [DEC-040]. | OPEN — OD19-02 [DEC-052]; if adopted, a separately governed class [DEC-052 R02d]. SCC backups/exports: S19-09 [DEC-040]. | OPEN — OD19-02 [DEC-052]; if adopted, a separately governed class [DEC-052 R02d]. SCC backups/exports: S19-09 [DEC-040]. | OPEN — OD19-02 [DEC-052]; if adopted, a separately governed class [DEC-052 R02d]. SCC backups/exports: S19-09 [DEC-040]. | — | — |
| Bootstrap / recovery credentials | **None exist** | — | — | — | — | A-07; DEC-021; DEC-045 |
| IPC authentication | None (OS peer identity) | — | — | — | — | §15.12 |

## 19.10 Trust-Boundary Implications

| Component | SD-K7 | SD-K8 | SD-K11R / SD-K11H | SD-K6P | SD-K2 | SD-PLAT | SD-HOST |
|---|---|---|---|---|---|---|---|
| K2 | — | — | — | — | Own key only | Platform's | — |
| K3 | **No** | No | No | No | No | Transit only (strip) | No |
| K4 | Read/write | Read | Read | **No** | No | No | No (only via K6) |
| K5 | **No** | No | Loader reads its code | **No** | No | No | No |
| K6 | **No** | Append | Read | Read/write | No | No | Via Operations only |
| K9 / root | Outside the boundary: can read and alter everything on the host | | | | | | |

**Consequences** (compromise analysis restated only as it concerns persistence; §18 is conditional):
- A compromised K4 (C) can read and alter everything in SD-K7, including audit and authorization state, but cannot
  read SD-K6P or alter SD-K8 or SD-K11 [LOCKED-DERIVED from T-12, T-21, LC-04].
- A compromised K6 or root can read and alter every storage domain on the host. No on-host storage property survives
  it [LOCKED-DERIVED from §15.15].
- At-rest encryption on the host is not represented as protecting against root [DEC-040 R10f; DEC-052 R02b].

## 19.11 Lifecycle Model

### 19.11.1 Durable records

| DC | Lifecycle | Basis |
|---|---|---|
| DC-07 Principal | ACTIVE ⇄ SUSPENDED ⇄ DISABLED → REVOKED (terminal) → tombstone retained | §17.1.4; DEC-038 |
| DC-07 Grant / Role Membership | ACTIVE → REVOKED (terminal); record retained while referenced | §17.4.1; DEC-039 |
| DC-09 Decision | Created immutable; status records appended (AWAITING_APPROVAL, AUTHORIZED, CONSUMED, EXPIRED, REVOKED, INVALIDATED) | §17.19 |
| DC-10 Plan / Job | Job state model OPEN (§16 Q-6) | §17.12 |
| DC-11 K4 audit, DC-12 K8 | Append-only; never edited in place. Removal and retention floors: [DEC-042 R12A-2; DEC-039; DEC-041]. | LC-03; LC-17; DEC-041 |
| DC-15 Pre-image | Created at commit → retained for a bounded, declared period [DEC-041 R11f] → expiry behaviour OPEN [DEC-042 R12A-5; DEC-057 R07h] | LC-13; DEC-041 |
| DC-16 Staged content | Created at stage → committed or discarded → discarded at restart if left over | §16.12 |

### 19.11.2 Credential Handles [DEC-046]

Lifecycle states and conditions, resolution, lifecycle authority, rotation, revocation, orphaned material, stale
credentials, external revocation and provisioning paths are established by DEC-046 (R16a–R16j). Resolution for
credential use is governed by DEC-046 R16b. Every other condition yields `CREDENTIAL_UNAVAILABLE` (§16.4.1 stage 17)
[LOCKED-DERIVED for the refusal]. No state diagram is carried forward. Transition mechanics are §22.

## 19.12 Retention Model

| Data | Minimum retention | Basis / status |
|---|---|---|
| K8 request IDs | At least the replay acceptance window | LOCKED (§16.11); [DEC-041 R11a] |
| K8 idempotency records | See [DEC-041 R11a] | Period and key-reuse semantics OPEN — Q19-02 |
| K8 used approval nonces | See [DEC-041 R11b]; independent of any horizon [DEC-053 R03b] | Owner decision, consistent with X-16. Horizon OPEN — OD19-03 |
| K8 records of dangling intents / UNKNOWN or PARTIAL outcomes | See [DEC-041 R11c] | LOCKED-DERIVED (X-30, X-32); DEC-041 |
| K8 records referenced by K4 audit (`journal_seq`) | See [DEC-041 R11d]; references across lifetimes [DEC-048 R18c] | DEC-041; DEC-048 |
| **Pressure rule** | See S19-07 [DEC-041 R11e] | DEC-041 |
| Principal `principal_id` tombstone | See [DEC-038 R8d] | DEC-038; final disposition §22 |
| Revoked Grants, Role Memberships, policy revisions | See [DEC-039 R9a, R9b] | DEC-039 |
| Decisions and status records; Approval Records | See [DEC-039 R9a, R9e, R9h] | DEC-039; periods §21 |
| Plans | *Verbatim (DEC-064):* Governed by the general rule in R9a (first sentence) and R9b. No Plan-specific retention has been decided. | DEC-039; DEC-064 |
| K4 audit | Defined by §21; must survive upgrades; [DEC-049 R19g] | DEFERRED §21; baseline §12 CURRENT |
| Health history / evidence history | OPEN — OD19-06. Floor: [DEC-056 R06c]. No default: [DEC-056 R06d] | §19-owned [DEC-056 R06a] |
| Pre-images | Bounded and declared per scope entry [DEC-041 R11f]. Representation and enforcement: OPEN — OD19-07 [DEC-057 R07c]. Global Execution Policy maximum: OPEN [DEC-057 R07b, R07f] | Owner decision (R11f); OPEN (OD19-07) |
| Staged content | Transient; discarded at restart | LOCKED-DERIVED (§16.12) |
| Credential material after revocation | See [DEC-046 R16e]; destruction completion [DEC-042 R12A-4] | DEC-046; DEC-042 |

## 19.13 Deletion / Destruction Model [DEC-042 (A); DEC-046]

Deletion and destruction are governed by DEC-042 R12A-1 … R12A-6 (with note A7) and, for credentials, DEC-046 R16e.
The no-erasure rule is S19-10.

### 19.13.1 Interim Authoring Rule [DEC-042 (B); DEC-054; placement DEC-064]

*Verbatim (DEC-042 R12B-1):* Until OD19-04 is resolved, a K11 WRITE scope entry MUST NOT target a resource declared by the applicable execution contract to contain credential-bearing content.

Scope, limits and continuation: [DEC-042 R12B-2 … R12B-5; DEC-054 R04a–R04c, R04e]. F19-05 remains OPEN [DEC-058].

## 19.14 Rotation / Revocation Model

| Item | Rotation | Revocation | Status |
|---|---|---|---|
| Security System / endpoint credentials | [DEC-046 R16c, R16d] | [DEC-046 R16e, R16i] | DEC-046; mechanics §22 |
| SCC-generated credentials | Provisioning: [DEC-061 F08b; DEC-046 R16j] | Operation output: OPEN [DEC-061 F08c] | DEC-061 |
| Stale credentials (rejected by the product) | [DEC-046 R16g, R16h] | — | DEC-046 |
| Orphaned credentials | [DEC-046 R16f, R16h] | — | DEC-046 |
| Assertion signing key / verification material | Rollover [DEC-051 R01h] | — | OPEN (P2 / §22; OD19-01) |
| Approver anchors | Per §17.9 | Per §17.9; outstanding approvals invalid | LOCKED (§17.9) |
| Principals, Grants, Decisions | — | Per §17.14; persisted as terminal states / status records | LOCKED (§17.14); persistence [DEC-038; DEC-039] |

## 19.15 Failure Semantics

"Consequence" states what persistence must guarantee. Recovery *procedures* are §22's.

| Failure | Consequence | Status |
|---|---|---|
| K7 unavailable | All state-changing actions refused; observation not durably recorded and must be shown as such | LOCKED (LC-08) |
| **K4 audit cannot be durably written while K7 is otherwise available** | See [DEC-035 R5a, R5b] | DEC-035 |
| Partial write / interrupted transaction in K7 | See S19-06 [DEC-034 R4a] | LOCKED-DERIVED (LC-17) for K4-internal Actions; DEC-034 |
| K7 corrupted | See [DEC-034 R4b] | DEC-034 |
| Process crash / reboot | K6: dangling intents → UNKNOWN before new requests (X-30); staged content discarded; K4: in-flight Jobs reconciled against K8 (§15.13) | LOCKED |
| K8 unwritable | K6 refuses all new requests | LOCKED (X-29) |
| **K8 lost or reinitialized** | See [DEC-048 R18a–R18l] | DEC-048 |
| SD-K6P credential store unavailable or unreadable | `CREDENTIAL_UNAVAILABLE`; no fallback to any other source | LOCKED-DERIVED (§16.4 layer 17) |
| At-rest key material unavailable (if adopted) | OPEN; no general fail-closed rule is established [DEC-040 R10g; DEC-052 R02e] | OPEN — OD19-02 |
| Interrupted credential rotation | See [DEC-046 R16d] | DEC-046 |
| Interrupted deletion / destruction | DESTROYING does not resolve [DEC-046 R16b]; completion [DEC-042 R12A-4]; mechanics §22 | DEC-046; DEC-042 |
| Interrupted upgrade / migration | See [DEC-049 R19c, R19d] | Baseline §12; DEC-049 |
| Stale state | Domain state carries `observed_at`; staleness is shown, never presented as current | LOCKED-DERIVED (T-28, T-30, X-25) |
| Orphaned state (records for removed Integrations or Security Systems) | A Security System is not represented as absent; state may only become stale or unknown. | LOCKED-DERIVED (T-28); reduced per DEC-064 |
| Restore of K7 from backup | See §19.17 | DEC-047 |
| Loss of SD-K2 signing key (e.g., platform reinstall) | No new assertions; no interactive actions; SCC state unaffected | LOCKED-DERIVED (§15.14) |

## 19.16 Recovery Dependencies (for §22 and the recovery gate)

§19 places these requirements on §22 / the recovery gate. It does not design recovery.
1. Bootstrap and recovery secrets: S19-05; [DEC-045 R15c, R15d].
2. K7 restore: §19.17 [DEC-047]; F19-09 [DEC-062 F09c, F09e].
3. Recovery must never make K8 writable by C, or K7 readable by W or I. [LOCKED-DERIVED from LC-02 (T-23; §15.3 K7
   row: "Accessible to C only") and LC-03 (§15.3 K8 row: "Writable by root/K6; readable by C"); classification
   confirmed DEC-064]
4. Append-only semantics: [DEC-042 R12A-2; DEC-049 R19e].
5. K8 lifetime and reinitialization: [DEC-048 R18a, R18b, R18i, R18j].
6. Credential lifecycle mechanics: [DEC-046 R16c]. Provisioning record, if introduced: [DEC-055 R05e].
7. Downgrade and migration: [DEC-049 R19h, R19i, R19l].
8. Principal-ID non-reuse across restore: [DEC-038 R8c; DEC-047 R17j].
9. K2 key and verification material re-provisioning: [DEC-051 R01b].
10. SCC removal: [DEC-042 R12A-6]. SD-K6P backup: [DEC-040 R10c]. At-rest keys, if adopted: [DEC-052 R02d].

## 19.17 Backup / Restore Implications [DEC-047]

Backup scope, restore authority, the recovery/reconciliation condition, Decisions, Jobs, post-backup authorization
changes, audit continuity, K8 restore, sessions, Principal-ID non-reuse, host and external state, and mixed-domain
restore are established by DEC-047 (R17a–R17l). Core requirement: S19-11. Procedures: §22.

## 19.18 Upgrade / Migration Implications [DEC-049]

Format versioning, unknown formats, partial migrations, migration requirements, append-only records, K8
interpretability, K7 audit history, downgrade, K7/K8 downgrade interaction, K11R/K11H, other domains, migration
authority and upgrade-sensitive validation are established by DEC-049 (R19a–R19m). Core requirement: S19-15.

## 19.19 Cross-Boundary Data Flow

| Flow | May carry | Must never carry | Basis |
|---|---|---|---|
| P2 (K2 → K3) | Request; identity assertion | Platform session beyond what K3 must strip; any SCC state | §15.10, §15.12 |
| P3 (K3 → K4) | Request; assertion or SCC session token | Platform session | §15.12 |
| P4/P5 (K4 ↔ K5) | Observation data needed for the call; DC-06 configuration for that Integration; results and proposals | Credential material; other Integrations' configuration; authorization state | §15.10; T-19 |
| P6 (K4 → K6) | Request fields per §16.3, including `handle_ref` and `blob` | Credential material (§16.9). Credential-bearing `blob`: F19-05 OPEN [DEC-058]; interim rule §19.13.1. | §16.3, §16.9 |
| P7 (K6 → K4) | Results under exposure modes; scrubbed output | Credential values; `FULL` content of credential-bearing resources. Credential material newly created by an Operation: OPEN [DEC-061 F08c]. | X-24 |
| K6 → K8 | Journal fields per §16.10.2 (metadata, digests, handle IDs) | Content of reads; credential values | §16.7; X-26 |
| K4 → K7 | DC-03 … DC-11 | Credential material; platform session; SCC session tokens in a form prohibited by S19-14 [DEC-044] | LC-04; DEC-044 |

## 19.20 Security Invariants

Each invariant reproduces the cited owner text verbatim or restates the cited locked text.

- **S19-01** *(verbatim, DEC-031 R1)* Each SCC data class has exactly one authoritative owner and one authoritative storage domain. This does not prohibit transient, derived, or explicitly permitted non-authoritative copies, provided those copies do not become an alternate authoritative source or weaken the access boundary of the authoritative domain.
- **S19-02** *(verbatim, DEC-031 R2)* The authoritative SCC storage domains identified by §19 must remain distinct according to their defined trust and access boundaries; they must not be consolidated or exposed to another component merely for implementation convenience.
- **S19-03** Credential secret material MUST exist durably only in SD-K6P and transiently only in K6. [LOCKED-DERIVED from T-18, §16.9, for Security System and platform credentials] Scope: [DEC-033 C-03a]. Not resolved by this invariant: F19-05 [DEC-033 C-03b].
- **S19-04** *(verbatim, DEC-043 R13b, R13c, R13d)* The parent-platform session MUST NOT be persisted by an SCC component. K2/K3 may process or relay the session only as permitted by §15.12; K3 MUST strip it and MUST NOT persist, log, or forward it. Approver private keys MUST NOT enter or be persisted by an SCC component. SCC receives only the resulting approval signature and associated verification evidence required by §17. Release signing private keys MUST NOT enter or be persisted by an SCC component. SCC receives and relies only on the corresponding public release trust anchors and signed release artifacts. Scope: [DEC-043 R13a, R13f].
- **S19-05** *(verbatim, DEC-045 R15a)* SCC MUST NOT create, persist, or rely upon a secret whose possession itself confers bootstrap or recovery authority. Bootstrap and recovery authority remains OS root acting host-locally through K9, subject to the recovery gate.
- **S19-06** *(verbatim, DEC-034 R4a)* For every K4 authorization state mutation for which §17 requires an audit record, the authorization mutation and its required audit record MUST become durable atomically: either both are committed or neither is committed.
- **S19-07** *(verbatim, DEC-041 R11e)* K8 MUST NOT evict records whose retention is required to enforce replay protection, idempotency safety, approval-nonce single use, unresolved-outcome reconciliation, or an authoritative K7 audit reference. If K8 cannot preserve those required records, K6 MUST refuse new requests in accordance with X-29.
- **S19-08** *(verbatim, DEC-038 R8a)* A revoked Principal MUST have a retained tombstone sufficient to establish that its `principal_id` existed and MUST NOT be reused within the applicable SCC instance. The tombstone MUST contain no more identity information than is necessary to enforce that invariant and support required historical references. See also [DEC-038 R8b, R8d].
- **S19-09** *(verbatim, DEC-040 R10a)* When SCC deliberately creates a backup or export containing secret material, the secret-bearing artifact MUST be encrypted with a key that is not stored with that artifact.
- **S19-10** *(verbatim, DEC-040 R10f; DEC-042 R12A-1)* SCC MUST NOT claim that on-host at-rest encryption protects SCC data against a root-equivalent compromise. SCC MUST NOT claim that SCC-controlled deletion guarantees physical erasure of data from storage media, filesystem journals, backups outside SCC's control, or storage controlled by root or another external party.
- **S19-11** *(verbatim, DEC-047 R17c, R17f)* Restoring SD-K7 from an earlier backup point MUST place SCC into a recovery/reconciliation condition before ordinary authorization-dependent work may resume. The restored K7 state MUST be treated as potentially stale with respect to events occurring after the backup point. The exact recovery state and transition mechanics remain subject to §22. A K7 restore MUST treat authorization changes occurring after the backup point—including Principal revocations, Role Membership revocations, Grant revocations, and applicable policy or authorization-state changes—as potentially absent from restored K7. SCC MUST NOT represent restored authorization state as current merely because it was present in the backup. The recovery procedure MUST establish the disposition of post-backup authorization changes before ordinary authorization-dependent operation resumes. The mechanism for obtaining and reconciling those changes remains subject to §22 and applicable off-host evidence. See also [DEC-047 R17d, R17e].
- **S19-12** *(verbatim, DEC-036 R6b)* Configuration writable by C MUST NOT widen SCC authority or execution capability. Configuration that can widen authority or execution MUST be outside C's writable domain and governed by its applicable higher-authority control. Scope: [DEC-036 R6a, R6c].
- **S19-13** K3 and K5 MUST NOT hold durable state. [LOCKED-DERIVED for K3 (§15.6, T-30) and K5 (T-06)]
- **S19-14** *(verbatim, DEC-044 R14b)* An SCC session token MUST NOT be persisted in a form from which the token can be recovered for direct bearer use.
- **S19-15** *(verbatim, DEC-049 R19a, R19b)* Authoritative persistent content in SD-K7 and SD-K8 MUST carry sufficient format-version information to determine whether the currently executing SCC component can safely interpret that content. The format-version mechanism MUST NOT rely solely on an implicit software-release version. SCC MUST NOT interpret authoritative persistent content whose format is unrecognised or unsupported by the executing component. The affected component MUST fail closed with respect to operations that depend upon that content. The exact refusal behavior and any required §16 amendment for K6 remain subject to the applicable implementation/recovery gate.

## 19.21 Open Questions (require owner or later-gate decision)

| ID | Question | Disposition | Owning gate(s) | Blocks §19 lock? |
|---|---|---|---|---|
| OD19-01 | Authoritative domain, owner and provisioning of DC-18 | OPEN [DEC-051] | §19 [DEC-051 R01b], coordinated with P2, §22 / recovery gate, CyberPanel K2 gate | No |
| OD19-02 | Whether SCC-controlled at-rest encryption is required, optional or not required, and for which domains and classes [DEC-052 R02c] | OPEN [DEC-052] | §19 Owner Decision Gate (policy) [DEC-064]; §22 (key mechanics) [DEC-052 R02d] | No |
| OD19-03 | Whether a maximum approval-validity horizon exists; its value and enforcement point | OPEN [DEC-053] | §19 Owner Decision Gate [DEC-064]; §16 Amendment Gate if K6-enforced [DEC-053 R03e]; §22 approval-tool contract if tool-only [DEC-053 R03f] | No |
| OD19-04 | Permanent prohibition vs a §16 composition path for credential-bearing `file.replace` content | OPEN [DEC-054] | §16 Amendment Gate [DEC-054 R04c, R04d] | No |
| OD19-05 | Whether and how K4 obtains advisory credential-handle metadata | OPEN [DEC-055] | §16 Amendment Gate [DEC-055 R05d] / §22 [DEC-055 R05e] | No |
| OD19-06 | DC-05 retention period and basis [DEC-056 R06b] | OPEN [DEC-056] | §19 [DEC-056 R06a]; dependency inputs §21 [DEC-056 R06i], §20 [DEC-056 R06j] | No |
| OD19-07 | Representation and enforcement of R11f; whether a Global Execution Policy maximum exists | OPEN [DEC-057] | §16 Amendment Gate [DEC-057 R07c, R07d]; §22 [DEC-057 R07h] | No |

Resolution of any item in §19.21–§19.21.1 after §19 is locked follows DEC-063 (§19.26). The §16 Amendment Gate
(NOT SCHEDULED), the §19 Owner Decision Gate and the §17/K4 Architecture Gate are named by DEC-064.

### 19.21.1 Open Items Without an OD Number [DEC-064]

| ID | Item | Source | Owning gate |
|---|---|---|---|
| Q19-01 | Whether ciphertext of K6-held credential material may exist outside SD-K6P, including the §15.12 wording "K7 plaintext (storage design §19)" read against T-18 | DEC-040 R10b; DEC-052 R02h | §19 Owner Decision Gate, coordinated with §22 / credential-custody design as needed |
| Q19-02 | Idempotency-record retention period and key-reuse semantics | DEC-041 R11a; DEC-048 R18e | §16 Amendment Gate / §22 |
| Q19-03 | Definition of the identity slice | DEC-050 R20a; DEC-056 R06k | §19 Owner Decision Gate, coordinated with §20 as applicable |
| Q19-04 | Semantics of approvals for K4-internal Actions | DEC-053 R03i; DEC-059 F06f | §17/K4 Architecture Gate (NOT SCHEDULED). This is not a §17 amendment gate; §17 remains LOCKED. |

### 19.21.2 Items for the §16 Amendment Gate (NOT SCHEDULED)

No §16 text is changed.

| # | Source | Item |
|---|---|---|
| 1 | DEC-048 R18c, R18i | K8 lifetime identity in journal references |
| 2 | DEC-048 R18d | K6 acceptance after K8 reinitialization |
| 3 | DEC-049 R19b | K6 refusal on unknown or unsupported K8 format |
| 4 | DEC-049 R19f | K8 interpretability across authorized K6 versions |
| 5 | DEC-053 R03e | K6-enforced approval horizon, if chosen |
| 6 | DEC-054 R04c, R04d | Credential-bearing `file.replace` composition, if chosen |
| 7 | DEC-055 R05d | Executor-family handle visibility, if chosen |
| 8 | DEC-057 R07c, R07d | Representation of R11f; optional Global Execution Policy maximum |
| 9 | DEC-058 F05a, F05b | Interpretation of F19-05 |
| 10 | DEC-061 F08c, F08d | Credential material in Operation output |
| 11 | Q19-02 | Idempotency retention and key reuse (with §22) |

## 19.22 Deferred Questions (belong to other gates)

| Question | Gate |
|---|---|
| Audit record format, audit retention periods, tamper-evidence mechanism, off-host export | §21; ODF-18-07 |
| Credential provisioning / rotation / destruction mechanics; backup/restore procedures; SCC removal data disposition; key custody | §22 / recovery gate |
| SCC session semantics and whether session validation state is durable | P2 |
| CyberPanel identity field and subject stability | CyberPanel K2 gate (K2-Q5) |
| Reconciliation, desired-state and drift records | §20 [DEC-050 R20a, R20b] |
| SCC-generated credentials (F19-08) | Provisioning [DEC-061 F08b]; output: §16 Amendment Gate [DEC-061 F08d] |
| Sensitivity classification scheme beyond exposure modes (CHANGE-023) | §21 / owner (unchanged). The open register attributes CHANGE-023 to §19. This discrepancy is unresolved. |
| Job state model (§16 Q-6) | §8 amendment (no gate scheduled) |
| K8 lifetime, reinitialization and recovery mechanics | §22; §16 Amendment Gate [DEC-048 R18d, R18i] |
| Downgrade policy; migration authority and mechanics | §22; CHANGE-025; TQ-06 [DEC-049 R19h, R19l] |
| Format rules for SD-K6P, SD-K11H, SD-K11R, SD-K2 | Their respective gates [DEC-049 R19k] |
| Source of post-backup authorization evidence; detection of K7 rollback | §22 / recovery gate; TQ-08; ODF-18-07 [DEC-062 F09c, F09d] |

## 19.23 Owner Dispositions

| ID | Disposition | Entry |
|---|---|---|
| PD19-01 | REVISE | DEC-031 |
| PD19-02 | ACCEPT | DEC-032 |
| PD19-03 | ACCEPT as locked-derived, with clarification C-03a, C-03b | DEC-033 |
| PD19-04 … PD19-11 | REVISE | DEC-034 … DEC-041 |
| PD19-12 | REVISE, split into (A) and (B) | DEC-042 |
| PD19-13 … PD19-20 | REVISE | DEC-043 … DEC-050 |
| OD19-01 … OD19-07 | DEFER / KEEP OPEN | DEC-051 … DEC-057 |
| F19-05 | Deferred to OD19-04 / §16 Amendment Gate | DEC-058 |
| F19-06 | Deferred, decomposed | DEC-059 |
| F19-07 | Rejected as a finding against locked text | DEC-060 |
| F19-08 | Split: provisioning half governed by DEC-046; output half deferred | DEC-061 |
| F19-09 | Deferred; wording narrowed | DEC-062 |
| — | Post-lock resolution route (CS-1) | DEC-063 |
| — | §19 change-set reconciliation decisions | DEC-064 |

## 19.24 Gate Criteria

§19 may be locked when all of the following hold:
1. The owner has dispositioned PD19-01 … PD19-20 (accept, reject or revise).
2. OD19-01 … OD19-07 are each either decided or explicitly deferred to a named gate. Deferral is acceptable; none of
   them blocks the storage classification.
3. D19-05 (F19-05) and D19-06 (F19-06) are recorded as known findings against locked text in the architecture index,
   if the owner agrees they are findings.
4. No accepted decision widens authority, moves responsibility between K2–K11, or contradicts §15–§17.
5. Every deferral names its owning gate (§21, §22, P2, CyberPanel K2 gate, §20).

## 19.25 Gate Status

**CANDIDATE — OWNER DISPOSITIONS RECORDED — NOT LOCKED.**

- Owner dispositions are recorded as DEC-031 … DEC-062. The post-lock resolution route is DEC-063. Change-set
  reconciliation decisions are DEC-064.
- **Gate evaluation at this revision (§19.24):**

  | # | Result |
  |---|---|
  | 1 | **SATISFIED** |
  | 2 | **SATISFIED**, with the gates named by DEC-064 |
  | 3 | **NOT SATISFIED**. Criterion 3 has not been amended [DEC-064]. |
  | 4 | **NO VIOLATION IDENTIFIED.** Supporting readings [DEC-064]: DEC-035 R5b is the owner's interpretation of the interaction between A-05 Fixed System Authority and the audit-record requirement; DEC-041 R11e applies X-29's existing K8 refusal consequence to an inability to preserve required records. §16 and §17 are not rewritten. |
  | 5 | **SATISFIED.** Criterion 5 applies to the explicit §19 deferrals enumerated in §19.21–§19.22, including §19.21.1. It does not require every "applicable architecture/contract/design" dependency phrase inside an owner decision to have an independently registered gate [DEC-064]. CHANGE-023 remains unresolved. |

- §19 is **NOT LOCKABLE** at this revision, solely because criterion 3 is not satisfied. Criterion 3 has not been
  amended.
- Locking requires a separate, explicit owner decision recorded as a new DEC entry.
- No implementation is authorized by this document or by DEC-031 … DEC-064. DEC-029 remains standing.
- **Proposed lock statement (not adopted):**

  > §19 is LOCKED as the persistence, secrets and data-lifecycle classification of SCC: the storage domains and data
  > classes of §19.6–§19.7, the ownership and access model of §19.8–§19.10, and invariants S19-01 … S19-15, as
  > established by owner decisions DEC-031 … DEC-064. Items recorded as OPEN or DEFERRED in §19.21–§19.22 remain open
  > at the gates named there and are resolved after lock through DEC-063.

- This revision changes §19, the architecture index, the open register and the decision log (DEC-031 … DEC-064). It
  does not change locked §15–§17, the baseline, the §18 documents or historical material.

## 19.26 Post-Lock Resolution Route [DEC-063]

*Verbatim (DEC-063):* When an OD19 item, Q19 item or deferred finding is resolved after §19 is locked, the resolution is recorded as a new DEC entry. That entry identifies each §19 passage it changes, and §19 is amended to match it. No other route changes locked §19 text.
