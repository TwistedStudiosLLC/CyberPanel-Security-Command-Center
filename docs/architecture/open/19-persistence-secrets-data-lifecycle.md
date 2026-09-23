> **Document status:** CANDIDATE — OWNER REVIEW REQUIRED — NOT LOCKED
> **Authority category:** 4 — Conditional/open architecture (see [Authority Hierarchy](../README.md#authority-hierarchy))
> **Source:** §19 architecture gate (PHASE 2 of DEC-025). Replaces the earlier "NOT DESIGNED — GATE PENDING" stub.
> **Normative:** **No.** Nothing in this document is locked. Statements marked **[LOCKED-DERIVED]** restate or follow
> directly from §15, §16 or §17 and carry only the authority of those sections. Every other rule is **PROPOSED**,
> **OPEN** or **DEFERRED** (§19.23) and requires an owner decision before it has any authority.
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
- which consequences §21 (audit), §22 (lifecycle/recovery), P2 and the CyberPanel K2 gate must later honour.

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
| "Health history should be supported." | Baseline §7 | CURRENT FOUNDATIONAL; retention OPEN |
| "Integration-specific configuration belongs within the Integration boundary." | Baseline §14 | **UNRESOLVED** (see D19-02) |
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
| D19-02 | Baseline §14 places Integration-specific configuration "within the Integration boundary", but K5 has no host access beyond its runtime (T-06), so an Integration cannot persist anything itself. | Baseline §14 vs §15 T-06 | UNRESOLVED in the baseline. PD19-07 proposes K4-owned, per-Integration namespaced configuration in K7. |
| D19-03 | §16.9 and §16.8 refer to K6 credential storage and retained pre-images, but §15's component catalogue names no persistent storage in the privileged domain other than K8. | §16.9, §16.8 vs §15.3 | Gap, not contradiction. PD19-02 names storage areas inside the existing privileged domain; no new runtime component. |
| D19-04 | §15.12 says assertion verification material exists "only in K4" but does not say where it is persisted or who provisions it; §15.14 says K2 key re-provisioning is a K9/lifecycle operation. | §15.12 vs §15.14 | OPEN (OD19-01): owner choice between K7 and K11 host-local placement. |
| D19-05 | Credential-bearing content written through `file.replace` would pass through K4 (and K7, if the Plan is persisted) as a plaintext `blob`, which conflicts with the intent of T-18 (such credentials only in K6). §16 provides handle substitution only for profile slots, not for staged file content. | §16.1.5, §16.8 vs T-18, §15.12 | Finding **F19-05**. PD19-12 proposes an authoring rule; the durable fix would need a §16 amendment (OD19-04). Recorded as a known finding for the index (not added there by this gate; see §19.25). |
| D19-06 | Approval nonces are checked against K8 (X-16), but no locked rule bounds how far in the future an approval `deadline` may be. Nonce records must therefore be kept until each evidence's deadline passes, and a lost K8 re-opens replay until then. | §16.5, X-16, §16.11 | Finding **F19-06**. OPEN (OD19-03). |
| D19-07 | K4 needs to know whether a credential handle is provisioned (to show a capability as unavailable before planning), but no `executor.*` Operation reports handle status, and provisioning is not a K6 request (so it is not journaled as one). | §16.1.3 (executor family), §16.9 | Finding **F19-07**. OPEN (OD19-05); possible §16 amendment or §22 provisioning record. |
| D19-08 | Credentials that an Integration workflow would *create* (for example, an agent registration that returns a key) cannot enter K6 storage, because no request field may carry credential material into K6. | §16.9 | Finding **F19-08**. DEFERRED: requires a §16 amendment or out-of-band root provisioning. |
| D19-09 | Restoring K7 from backup cannot recover revocations made after the backup point, because no revocation record exists outside K7. | §17.14; §18 TH-32 / SR-16 (conditional) | Finding **F19-09**. PD19-17 and dependency on ODF-18-07 / §22. |

## 19.6 Terminology

- **Data class (DC):** a category of information with one owner, one authoritative storage domain and one lifecycle.
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
| SD-K6P | K6 Privileged Storage (**proposed name**, PD19-02): Credential Store (CS), Pre-image Store (PI), Staging Area (ST) | root only (K6) | §16.8, §16.9 (D19-03) |
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
| DC-03 | K4 operational configuration that cannot widen authority or execution (for example scheduling cadence, freshness thresholds) | SD-K7 | K4 | C | C | No | LC-01; PD19-06 |
| DC-04 | Authoritative domain state: inventory, Security System records, registry state, compatibility determinations, health reports | SD-K7 | K4 | C | C | **Largely yes** (by re-observation) | LC-01; §15.7 |
| DC-05 | Observation evidence and health history (content limited by exposure modes) | SD-K7 | K4 | C | C | Current values yes; history no | LC-14; baseline §7 |
| DC-06 | Integration-specific configuration (per `integration_id`) | SD-K7 | K4 (on the Integration's behalf) | C | C; passed to K5 per call | No | D19-02; PD19-07 |
| DC-07 | Authorization state: Principals (incl. tombstones), Platform Identity Bindings, Role Memberships, Grants, revocation records | SD-K7 | K4 | C | C | **No** | LC-15, LC-16 |
| DC-08 | Authorization policy local settings and their revisions | SD-K7 | K4 | C (R4 `scc.*` Action) | C | No | §17.20 |
| DC-09 | Authorization Decisions (immutable) and their append-only status records; Approval Records | SD-K7 | K4 | C (append-only semantics) | C | No | §17.19; LC-15 |
| DC-10 | Plans and Jobs (Plan content, `plan_digest`, Job state) | SD-K7 | K4 | C | C | No | §17.11, §17.12 |
| DC-11 | K4 audit records | SD-K7 | K4 | C (append-only semantics) | C | No | LC-01; LC-17; LC-18; format §21 |
| DC-12 | K8 executor journal records (incl. request IDs, idempotency keys, used approval nonces, dangling intents, approval-evidence verification results) | SD-K8 | K6 | K6 (append) | C, root | **No** | LC-03, LC-11, LC-12 |
| DC-13 | Credential secret material | SD-K6P / CS | K6 | root (provisioning, §22); K6 (rotation state) | K6 only, at invocation | No | LC-04, LC-10 |
| DC-14 | Credential metadata (handle ID, provisioning state, material version, timestamps) | SD-K6P / CS (authoritative); definitions in DC-01 | K6 | root, K6 | K6; K4 visibility OPEN (D19-07) | No | LC-10 |
| DC-15 | Retained pre-images of replaced files | SD-K6P / PI | K6 | K6 | K6 (via `file.restore_preimage`) | No | LC-13 |
| DC-16 | Staged content for `file.replace` | SD-K6P / ST | K6 | K6 | K6 | n/a (transient-durable, discarded at restart) | LC-13; §16.12 |
| DC-17 | Assertion signing key (K2) | SD-K2 | K2 (platform domain) | Provisioning (P2 / §22) | K2 only | No | T-20; §15.14 |
| DC-18 | Assertion verification material | SD-K7 **or** SD-K11H (OD19-01) | K4 (use) / provisioning owner per OD19-01 | per OD19-01 | K4 | No | §15.12; D19-04 |
| DC-19 | SCC session validation state | TBD by P2 | K4 | C | C | — | §15.12; P2 |
| DC-20 | Platform state (sessions, ACLs, accounts, platform configuration) | SD-PLAT | Parent platform | Platform | — | — | §15.5 |
| DC-21 | Host / Security System state (configurations, logs, services) | SD-HOST | Host / administrators | Host; SCC only via K6 WRITE Operations | K6 | — | §15.15 |
| DC-22 | Approver private keys | SD-OFF or operator-managed host location outside W/C/I (custody per ODF-18-08) | Approver | Approver | Approval environment | — | §17.9; LC-20 |
| DC-23 | Release signing private keys | SD-OFF | Release owner | — | — | — | §16.2 (anchors are public); §22 |
| DC-24 | Transient values: resolved credential values, platform session cookies in transit, identity assertions in transit, approval evidence in transit, raw observation content before K4 persistence | TRANSIENT | Holding process | — | — | — | LC-04, LC-14 |

**Not a data class SCC holds:** IPC authentication secrets. §15.12 establishes OS peer identity, so no transferable
IPC secret exists [LOCKED-DERIVED].

## 19.8 Persistence Ownership Model

1. **One owner per data class.** Each DC above has exactly one owning component. Only the owner (or root, which is
   outside the boundary) writes it. [PROPOSED — PD19-01]
2. **K7 is not the only store, and it is not a generic database for everything.** SD-K7, SD-K8, SD-K11R, SD-K11H and
   SD-K6P are distinct storage domains with distinct access boundaries. They must not be merged into one store, and no
   component may be given access to another component's domain to "simplify" storage. [PROPOSED — PD19-01; basis
   LC-02, LC-03, LC-04, LC-05]
3. **K3 and K5 persist nothing.** K3 holds no state (§15.6, T-30); K5 cannot persist beyond its runtime (T-06). Any
   durable state an Integration needs is held by K4 in K7 (DC-06). [LOCKED-DERIVED for K3/K5; PD19-07 for DC-06]
4. **Platform and host state are not SCC state.** SCC persists only what it needs to identify, observe and audit
   them: the Platform Identity Binding and non-authoritative display names (DC-07); observation evidence limited by
   exposure modes (DC-05). SCC does not keep copies of platform data it does not need (baseline §11).
5. **Re-derivable vs non-re-derivable.** Domain state (DC-04) can be rebuilt by re-observation, so its loss is an
   availability loss (LC-07). Authorization state, Decisions, Plans/Jobs, audit, K8 and credentials (DC-07 … DC-13)
   cannot be rebuilt; their loss is a security-relevant loss and must fail closed.

## 19.9 Secret / Credential Ownership Model

| Secret | Owner | Where material lives | SCC stores material or reference? | Plaintext persisted? | May cross K2/K3/K4/K6? | Basis |
|---|---|---|---|---|---|---|
| Security System credentials (API keys, admin tokens, socket access) | K6 | SD-K6P / CS | **Material in K6 only**; everyone else holds `handle_ref` | Only inside SD-K6P (at-rest protection: PD19-10, OD19-02) | **Never** leaves K6 | LC-04, LC-10 |
| Parent-platform administrative / API credentials | K6 | SD-K6P / CS (only where no lower-impact read path exists) | Material in K6 only | Only inside SD-K6P | Never leaves K6 | §15.12 |
| Endpoint credentials (for `endpoint.call`) | K6 | SD-K6P / CS | Material in K6; sent only after endpoint identity check | Only inside SD-K6P | Never leaves K6 except to the verified endpoint | X-35; §16.9 |
| Parent-platform session | Platform | SD-PLAT; browser | Neither | Never by SCC | K3 may see it in transit and must strip it | §15.12; T-19 |
| Identity-assertion signing key | K2 | SD-K2 | Not by SCC Core | Platform-domain storage only | Never leaves K2 | T-20 |
| Assertion verification material | K4 (use) | OD19-01 | Public material | n/a (public) | K4 only uses it | §15.12 |
| SCC session tokens | K4 | TRANSIENT at K3; K4 validation state per P2 | K4 validation state only | **No bearer token persisted in plaintext** (PD19-14) | Browser ↔ K3 ↔ K4 | §15.12; P2 |
| Approver private keys | Approver | SD-OFF or operator-managed location outside W/C/I | **Neither.** SCC holds only public anchors (DC-02) | Never by SCC | Never enters SCC; only signatures do | §17.9; A-22; PD19-13 |
| Release signing private keys | Release owner | SD-OFF | Neither; SCC holds public trust anchors | Never by SCC | Never | §16.2; §22 |
| Encryption keys protecting SCC data at rest (if adopted) | OD19-02 | OD19-02 | OD19-02 | Never alongside the data they protect (PD19-10) | — | — |
| Bootstrap / recovery credentials | **None exist** | — | — | — | — | A-07; DEC-021; PD19-15 |
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
- At-rest encryption on the host does **not** protect against root and must never be described as doing so
  (PD19-10).

## 19.11 Lifecycle Model

### 19.11.1 Durable records

| DC | Lifecycle | Basis |
|---|---|---|
| DC-07 Principal | ACTIVE ⇄ SUSPENDED ⇄ DISABLED → REVOKED (terminal) → tombstone retained | §17.1.4; PD19-08 |
| DC-07 Grant / Role Membership | ACTIVE → REVOKED (terminal); record retained while referenced | §17.4.1; PD19-09 |
| DC-09 Decision | Created immutable; status records appended (AWAITING_APPROVAL, AUTHORIZED, CONSUMED, EXPIRED, REVOKED, INVALIDATED) | §17.19 |
| DC-10 Plan / Job | Job state model OPEN (§16 Q-6) | §17.12 |
| DC-11 K4 audit, DC-12 K8 | Append-only; retained until retention expiry; never edited | LC-03; LC-17; PD19-11 |
| DC-15 Pre-image | Created at commit → retained for its declared period → destroyed | LC-13; PD19-11 |
| DC-16 Staged content | Created at stage → committed or discarded → discarded at restart if left over | §16.12 |

### 19.11.2 Credential handles (PROPOSED — PD19-16)

```text
DECLARED (handle defined in a loaded K11 declaration)
   └─► UNPROVISIONED ──(root provisioning, §22)──► PROVISIONED
                                                     │
                                  (rotation begins)  ▼
                                                   ROTATING  (old and new material both held; handle resolves to
                                                     │        the last committed version)
                                  (new version committed) ▼
                                                   PROVISIONED (new version)
PROVISIONED / ROTATING ──(revocation)──► REVOKED (unusable) ──► DESTROYING ──► DESTROYED
Material with no loaded declaration referencing its handle ──► ORPHANED (unusable; reported; destroyed only by an
                                                                 explicit Local Root Operator act)
```

A handle resolves only in PROVISIONED or ROTATING. Every other state yields `CREDENTIAL_UNAVAILABLE` (§16.4 layer 17)
[LOCKED-DERIVED for the refusal; PROPOSED for the states].

## 19.12 Retention Model

| Data | Minimum retention | Basis / status |
|---|---|---|
| K8 request IDs and idempotency records | At least the replay acceptance window | LOCKED (§16.11) |
| K8 used approval nonces | Until the deadline of the evidence they belong to has passed | LOCKED-DERIVED (X-16 checks nonces against K8); horizon OPEN (D19-06, OD19-03) |
| K8 records of dangling intents / UNKNOWN or PARTIAL outcomes | Until reconciled (§16.11 `reconciled_after` must reference them) | LOCKED-DERIVED (X-30, X-32) |
| K8 records referenced by K4 audit (`journal_seq`) | At least as long as the referencing audit record | PROPOSED (PD19-11); periods §21 |
| **Pressure rule** | K8 MUST NOT evict any record in the three rows above to make space; if space is exhausted, K6 refuses new requests (X-29) rather than evicting | PROPOSED (PD19-11); aligns with §18 TF-18-09 (conditional) |
| Principal `principal_id` tombstone | Lifetime of the SCC instance | PROPOSED (PD19-08); derived from LC-16 |
| Revoked Grants, Role Memberships, policy revisions | While any Decision or audit record references them | PROPOSED (PD19-09); follows from A-35 fields |
| Decisions and status records; Approval Records | At least the life of the referencing Job, and at least as long as audit records that reference them | PROPOSED (PD19-09); periods §21 |
| Plans | At least until the Job is terminal and no audit record needs the Plan content | PROPOSED; periods §21 |
| K4 audit | Defined by §21; must survive upgrades | DEFERRED §21; baseline §12 CURRENT |
| Health history / evidence history | Not decided | OPEN (OD19-06) |
| Pre-images | Declared per scope entry, bounded by a global maximum in the Global Execution Policy | PROPOSED (PD19-11); needs K11 content, see OD19-07 |
| Staged content | Transient; discarded at restart | LOCKED-DERIVED (§16.12) |
| Credential material after revocation | Not retained beyond destruction | PROPOSED (PD19-16) |

## 19.13 Deletion / Destruction Model (PROPOSED — PD19-12, PD19-16)

1. **No physical-erasure claim.** SCC can make data unusable and remove its own copies. It cannot guarantee physical
   erasure (storage media, filesystem journals, backups outside its control, root). SCC documentation must not claim
   secure erasure.
2. **Append-only records are never deleted individually.** K4 audit, K8 records, Decisions and their status records
   are removed only by retention expiry under §21 rules, never edited.
3. **Principals are never deleted.** They are revoked and tombstoned.
4. **Credential destruction** removes material from SD-K6P and makes the handle unresolvable *before* the destruction
   is reported complete. Interrupted destruction leaves the handle in DESTROYING, which is unusable, and destruction
   resumes idempotently.
5. **Pre-images** are destroyed at the end of their declared retention.
6. **SCC removal** (uninstall) data disposition — what is exported, kept or destroyed — is DEFERRED to §22.

## 19.14 Rotation / Revocation Model

| Item | Rotation | Revocation | Status |
|---|---|---|---|
| Security System / endpoint credentials | Provisioning and rotation are Local Root Operator acts (K9 / §22) in v1, because no request may carry credential material into K6 (LC-10). Interrupted rotation keeps the last committed version resolvable. | Handle → REVOKED (unusable) → destroyed. Revoking the credential at the product itself is outside SCC unless a declared Operation exists. | PROPOSED (PD19-16); mechanics §22 |
| SCC-generated credentials | Not supported without a §16 amendment (D19-08) | — | DEFERRED |
| Stale credentials (rejected by the product) | K6 records the failed use in K8 (handle ID only); K4 surfaces it; **no automatic rotation** | — | PROPOSED |
| Orphaned credentials | Unusable; reported; destroyed only by explicit root act (automatic destruction could lose material during a declaration rollback) | — | PROPOSED |
| Assertion signing key / verification material | Rollover must allow overlap so that verification does not fail mid-rotation | Revoking verification material makes all assertions from that key fail closed | OPEN (P2 / §22; OD19-01) |
| Approver anchors | Per §17.9 | Per §17.9; outstanding approvals invalid | LOCKED (§17.9) |
| Principals, Grants, Decisions | — | Per §17.14; persisted as terminal states / status records | LOCKED (§17.14); persistence PROPOSED (PD19-08, PD19-09) |

## 19.15 Failure Semantics

"Consequence" states what persistence must guarantee. Recovery *procedures* are §22's.

| Failure | Consequence | Status |
|---|---|---|
| K7 unavailable | All state-changing actions refused; observation not durably recorded and must be shown as such | LOCKED (LC-08) |
| **K4 audit cannot be durably written while K7 is otherwise available** | State-changing actions, K4-internal Actions and authorization decisions that require an audit record are refused (fail closed) | PROPOSED (PD19-05); derived from A-35 and §17.22; closes the fail-closed part of CHANGE-015 that §15.13 assigns to §18/§19 |
| Partial write / interrupted transaction in K7 | A K4 state change and its audit record commit together or not at all | LOCKED-DERIVED (LC-17) for K4-internal Actions; PROPOSED (PD19-04) for all authorization records |
| K7 corrupted | Fail closed; corruption must be detectable before K4 relies on the data | PROPOSED (PD19-04); detection mechanism OPEN (§21 / implementation) |
| Process crash / reboot | K6: dangling intents → UNKNOWN before new requests (X-30); staged content discarded; K4: in-flight Jobs reconciled against K8 (§15.13) | LOCKED |
| K8 unwritable | K6 refuses all new requests | LOCKED (X-29) |
| **K8 lost or reinitialized** | Replay and idempotency protection for earlier requests is lost. K6 MUST NOT accept requests whose `issued_at` precedes reinitialization, and MUST NOT accept approval evidence until the approval horizon (OD19-03) has elapsed since reinitialization | PROPOSED (PD19-18); depends on OD19-03 |
| SD-K6P credential store unavailable or unreadable | `CREDENTIAL_UNAVAILABLE`; no fallback to any other source | LOCKED-DERIVED (§16.4 layer 17) |
| At-rest key material unavailable (if adopted) | Same as unavailable credential store / unavailable K7: fail closed | PROPOSED (PD19-10) |
| Interrupted credential rotation | Last committed version stays resolvable; both versions retained until the new one is committed | PROPOSED (PD19-16) |
| Interrupted deletion / destruction | DESTROYING is unusable; destruction resumes idempotently | PROPOSED (PD19-16) |
| Interrupted upgrade / migration | K4 must not operate on a partially migrated K7 (fail closed); migrations are versioned and deterministic | CURRENT FOUNDATIONAL (baseline §12); PROPOSED (PD19-19) |
| Stale state | Domain state carries `observed_at`; staleness is shown, never presented as current | LOCKED-DERIVED (T-28, T-30, X-25) |
| Orphaned state (records for removed Integrations or Security Systems) | Retained and marked, never silently deleted; Security Systems stay visible | LOCKED-DERIVED (T-28); PROPOSED marking |
| Restore of K7 from backup | See §19.17 | PROPOSED (PD19-17) |
| Loss of SD-K2 signing key (e.g., platform reinstall) | No new assertions; no interactive actions; SCC state unaffected | LOCKED-DERIVED (§15.14) |

## 19.16 Recovery Dependencies (for §22 and the recovery gate)

§19 establishes the following requirements that recovery design must honour. It does not design recovery.
1. No recovery or bootstrap path may introduce a stored SCC secret; authority is OS root through K9 (PD19-15).
2. Recovery must not restore authorization state without the consequences in §19.17.
3. Recovery must never make K8 writable by C, or K7 readable by W or I.
4. Recovery must preserve append-only semantics: records may be restored but not edited.
5. Re-provisioning of K2 key material and verification material after platform reinstall (§15.14) is a §22 / P2 act.
6. Credential provisioning, rotation and destruction are Local Root Operator acts in v1 (PD19-16).

## 19.17 Backup / Restore Implications (PROPOSED — PD19-17)

1. **Backup scope is per storage domain.** A backup of SD-K7 must not include SD-K6P material. SD-K6P material, if
   ever backed up, must be encrypted with a key not stored alongside the backup (PD19-10).
2. **Restore is a Local Root Operator act**, audited, never available through K3 (T-29).
3. **Restoring SD-K7 rolls back authorization state.** Revocations made after the backup point cannot be recovered
   from K7 alone (D19-09). Therefore, on restore:
   - every Decision that is not terminal MUST be treated as INVALIDATED;
   - Jobs not terminal MUST be held and reconciled against K8 before any further request;
   - the restore MUST be recorded as an event that states the backup point;
   - the residual risk (post-backup revocations lost) MUST be disclosed unless an off-host record exists
     (ODF-18-07, open).
4. **Restoring SD-K8** must never replace a newer journal with an older one silently; doing so is treated as K8
   reinitialization (§19.15, PD19-18).
5. Backup mechanics, frequency and storage location are DEFERRED to §22.

## 19.18 Upgrade / Migration Implications

1. K7 content must carry a format version; migrations are versioned and deterministic; K4 refuses to run on a K7
   version it does not recognise (fail closed). [PROPOSED — PD19-19; baseline §12 CURRENT]
2. K8 records must carry a format version and remain interpretable by later K6 versions for as long as they are
   retained. [PROPOSED — PD19-19]
3. Audit history must survive upgrades. [CURRENT FOUNDATIONAL — baseline §12]
4. Downgrade after a forward migration is not supported except by restore (§19.17). [PROPOSED; forensic audit MED-14
   HISTORICAL]
5. SD-K11R content changes only by release installation; SD-K11H survives upgrades unless the Local Root Operator
   changes it. Rollback protection for K11 is OPEN (§18 TH-24 / SR-15, conditional; §22).

## 19.19 Cross-Boundary Data Flow

| Flow | May carry | Must never carry | Basis |
|---|---|---|---|
| P2 (K2 → K3) | Request; identity assertion | Platform session beyond what K3 must strip; any SCC state | §15.10, §15.12 |
| P3 (K3 → K4) | Request; assertion or SCC session token | Platform session | §15.12 |
| P4/P5 (K4 ↔ K5) | Observation data needed for the call; DC-06 configuration for that Integration; results and proposals | Credential material; other Integrations' configuration; authorization state | §15.10; T-19 |
| P6 (K4 → K6) | Request fields per §16.3, including `handle_ref` and `blob` | Credential material (except as F19-05 describes for `blob`; see PD19-12) | §16.3, §16.9 |
| P7 (K6 → K4) | Results under exposure modes; scrubbed output | Credential values; `FULL` content of credential-bearing resources | X-24 |
| K6 → K8 | Journal fields per §16.10.2 (metadata, digests, handle IDs) | Content of reads; credential values | §16.7; X-26 |
| K4 → K7 | DC-03 … DC-11 | Credential material; platform session; bearer tokens in plaintext | LC-04; PD19-14 |

## 19.20 Security Invariants (PROPOSED unless marked)

- **S19-01** Each data class has exactly one owning component and one authoritative storage domain. [PD19-01]
- **S19-02** SD-K7, SD-K8, SD-K11R, SD-K11H and SD-K6P MUST remain separate storage domains with the access boundaries in §19.10. [PD19-01]
- **S19-03** Credential secret material MUST exist durably only in SD-K6P and transiently only in K6. [LOCKED-DERIVED from T-18, §16.9, for Security System and platform credentials]
- **S19-04** SCC components MUST NOT persist approver private keys, release signing private keys or the parent-platform session. [PD19-13; LC-04]
- **S19-05** SCC MUST NOT create or hold any bootstrap or recovery secret; bootstrap and recovery authority is OS root through K9. [PD19-15]
- **S19-06** A K4 state change that requires an audit record MUST NOT take effect unless its audit record is durably committed with it. [PD19-04, PD19-05; LC-17]
- **S19-07** K8 MUST NOT evict records needed for replay protection, idempotency, nonce single-use or unreconciled outcomes; it MUST refuse new requests instead. [PD19-11]
- **S19-08** `principal_id` tombstones MUST be retained for the life of the instance. [PD19-08]
- **S19-09** Data that leaves its storage domain in a backup or export and contains secret material MUST be encrypted with a key not stored with it. [PD19-10]
- **S19-10** SCC MUST NOT claim that on-host at-rest encryption protects against root, or that deletion guarantees physical erasure. [PD19-10, PD19-12]
- **S19-11** Restoring SD-K7 MUST invalidate non-terminal Decisions and hold non-terminal Jobs until reconciled. [PD19-17]
- **S19-12** Security-relevant configuration that could widen authority or execution MUST NOT be writable by C; C-writable configuration may only narrow or tune non-security behaviour. [PD19-06]
- **S19-13** K3 and K5 MUST NOT hold durable state. [LOCKED-DERIVED for K3 (§15.6, T-30) and K5 (T-06)]
- **S19-14** Bearer tokens (SCC session tokens) MUST NOT be persisted in plaintext. [PD19-14]
- **S19-15** K7 and K8 content MUST carry format versions; K4 and K6 MUST refuse to operate on unrecognised versions. [PD19-19]

## 19.21 Open Questions (require owner or later-gate decision)

| ID | Question | Owner | Blocks §19 lock? |
|---|---|---|---|
| OD19-01 | Where is assertion verification material persisted and who provisions it: (a) SD-K7, written by K4; (b) SD-K11H, root-provisioned with K2 installation? (a) matches §15.12's "only in K4" literally; (b) ties provisioning to root, as §15.14 anticipates for re-provisioning. | Owner; P2 / §22 | No (can be deferred to P2) |
| OD19-02 | At-rest encryption *inside* the host storage domains (SD-K7, SD-K6P): required, optional, or not required? Its value is limited because root is outside the boundary; it protects against disk theft, decommissioning and mis-set permissions. Key hierarchy and custody follow from the answer. | Owner; §22 | No |
| OD19-03 | Maximum approval validity horizon (bounds K8 nonce retention and the post-K8-loss exposure): enforced by (a) the approval tool (§22) only, (b) a K11 Global Execution Policy value checked by K6 (§16 amendment), or (c) unbounded with indefinite nonce retention. | Owner; §22 / possible §16 amendment | No |
| OD19-04 | Credential-bearing file content (F19-05): accept the authoring prohibition (PD19-12) as permanent, or open a §16 amendment for handle-based content composition in `file.replace`? | Owner; possible §16 amendment | No (PD19-12 is the interim) |
| OD19-05 | How K4 learns credential-handle provisioning state (F19-07): (a) a new `executor.*` Operation (§16 amendment), (b) a provisioning record written by K9/§22 that K4 can read, or (c) refusal-only discovery. | Owner; §16 / §22 | No |
| OD19-06 | Health and evidence history retention periods | §21 / owner | No |
| OD19-07 | Pre-image retention bounds: declared per scope entry and capped by a Global Execution Policy maximum — this places a new value in K11 content (release-signed), which may need §16 confirmation. | Owner; possible §16 clarification | No |

## 19.22 Deferred Questions (belong to other gates)

| Question | Gate |
|---|---|
| Audit record format, audit retention periods, tamper-evidence mechanism, off-host export | §21; ODF-18-07 |
| Credential provisioning / rotation / destruction mechanics; backup/restore procedures; SCC removal data disposition; key custody | §22 / recovery gate |
| SCC session semantics and whether session validation state is durable | P2 |
| CyberPanel identity field and subject stability | CyberPanel K2 gate (K2-Q5) |
| Reconciliation, desired-state and drift records | §20 (no dependency found for the identity slice) |
| SCC-generated credentials (F19-08) | Future §16 amendment |
| Sensitivity classification scheme beyond exposure modes (CHANGE-023) | §21 / owner |
| Job state model (§16 Q-6) | §8 amendment (no gate scheduled) |

## 19.23 Proposed Decisions

| ID | Proposed decision | Classification |
|---|---|---|
| PD19-01 | One owner and one authoritative storage domain per data class; SD-K7, SD-K8, SD-K11R, SD-K11H and SD-K6P remain separate (S19-01, S19-02) | **PROPOSED** |
| PD19-02 | Name the privileged-domain storage areas SD-K6P (Credential Store, Pre-image Store, Staging Area) as parts of K6's existing domain, not a new runtime component | **PROPOSED** |
| PD19-03 | Credential secret material durably only in SD-K6P, transiently only in K6 (S19-03) | **LOCKED** (already established by T-18, §15.12, §16.9; restated) |
| PD19-04 | Authorization records and their audit records commit atomically; corruption must be detectable before use (S19-06) | **PROPOSED** (atomicity for K4-internal Actions is LOCKED by §17.22) |
| PD19-05 | Audit fail-closed: state-changing actions and authorization decisions that require an audit record are refused if the record cannot be durably written | **PROPOSED** (derived from A-35 and §17.22; §15.13 assigns this policy to §18/§19) |
| PD19-06 | C-writable configuration may only narrow or tune non-security behaviour (S19-12) | **PROPOSED** |
| PD19-07 | Integration-specific configuration is K4-owned, namespaced by `integration_id`, stored in SD-K7, passed to K5 per call | **PROPOSED** (resolves D19-02) |
| PD19-08 | `principal_id` tombstones retained for the life of the instance (S19-08) | **PROPOSED** |
| PD19-09 | Revoked Grants, Role Memberships, policy revisions, Decisions and Approval Records retained while referenced | **PROPOSED** |
| PD19-10 | Secret material leaving its storage domain is encrypted with a separately held key; no claim that on-host encryption protects against root (S19-09, S19-10) | **PROPOSED** (in-host encryption is OD19-02) |
| PD19-11 | K8 and pre-image retention rules in §19.12, including the pressure rule (S19-07) | **PROPOSED** (replay-window minimum is LOCKED by §16.11) |
| PD19-12 | Deletion model in §19.13, and the authoring rule: WRITE scope entries MUST NOT target credential-bearing content until OD19-04 is decided | **PROPOSED** |
| PD19-13 | No SCC component persists approver private keys, release signing private keys or the parent-platform session (S19-04) | **PROPOSED** (platform-session part is LOCKED by §15.12) |
| PD19-14 | Bearer tokens are never persisted in plaintext (S19-14) | **PROPOSED**; session semantics DEFERRED to P2 |
| PD19-15 | No bootstrap or recovery secret exists; authority is OS root through K9 (S19-05) | **PROPOSED** (consistent with A-07, DEC-021) |
| PD19-16 | Credential handle lifecycle (§19.11.2), rotation, revocation, orphan and destruction semantics; provisioning and rotation are Local Root Operator acts in v1 | **PROPOSED**; mechanics DEFERRED to §22 |
| PD19-17 | Backup/restore implications in §19.17 (S19-11) | **PROPOSED**; procedures DEFERRED to §22 |
| PD19-18 | K8 loss or reinitialization semantics in §19.15 | **PROPOSED**; depends on OD19-03 |
| PD19-19 | Format versioning of K7 and K8 content; fail closed on unrecognised versions (S19-15) | **PROPOSED** |
| PD19-20 | No §20 dependency exists for the identity slice; §20 adds data classes to SD-K7 when designed | **PROPOSED** (records a finding) |

These are **not** added to the decision log: the log's current convention records owner decisions only
(`CURRENT — OWNER DECISIONS`), and has no status for proposals. They become decisions only when the owner records them.

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

**CANDIDATE — READY FOR OWNER REVIEW — NOT LOCKED.**

- **Not ready to lock yet**, because PD19-01 … PD19-20 require owner dispositions and OD19-01 … OD19-07 require
  decisions or explicit deferrals (§19.24).
- **Lockable after review** without waiting for §21, §22, P2 or the CyberPanel K2 gate, provided the deferrals in
  §19.22 are accepted. The later gates refine retention periods, formats and procedures within the classification
  and invariants defined here.
- **Owner decision required before any status change:** an explicit owner decision recording the PD dispositions and
  authorizing the lock (to be added to the decision log as a new DEC entry by the owner's instruction).
- **Proposed lock statement** (for the owner to adopt, amend or reject):

  > §19 is LOCKED as the persistence, secrets and data-lifecycle classification of SCC: the storage domains and
  > data classes of §19.6–§19.7, the ownership and access model of §19.8–§19.10, and invariants S19-01 … S19-15 as
  > accepted by the owner. Retention periods, formats, procedures and mechanisms remain owned by §21, §22, P2 and the
  > CyberPanel K2 gate as listed in §19.22.

- **Not changed by this gate:** the decision log, locked §15–§17, the baseline, the §18 documents and all historical
  material. The findings F19-05 and F19-06 are **not** added to the architecture index's known-findings table by this
  gate; the index was changed only to show §19's status.
