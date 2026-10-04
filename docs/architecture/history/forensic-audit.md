> **Document status:** HISTORICAL / FORENSIC — NON-NORMATIVE
> **Authority category:** 5 — Historical / forensic material (see [Authority Hierarchy](../README.md#authority-hierarchy))
> **What this is:** The Forensic Architectural Audit of the original §1–§14 candidate architecture. It is the audit
> that identified CRIT-01 … CRIT-04 and led to §15, §16 and §17.
> **This document is not current authority.** Its findings, proposed changes (CHANGE-001 … CHANGE-027) and proposed
> sections were inputs to later gates. Where a later gate addressed a finding, the later gate controls. The current
> standing of each CHANGE is indexed in the [open register](../open/register.md) §7. Its "NOT READY FOR ADOPTION"
> determination describes the §1–§14 candidate at the time of the audit.
> **Transcription notes:** Reproduced verbatim. Removed process-wrapper text only: the closing line ("I followed your
> no-files instruction, so this report exists only in this conversation. If you want it as a shareable private page,
> I can publish it."). The "What I checked" and "Scope note" paragraphs are retained as part of the report.

# SCC Architecture Forensic Audit

**What I checked:** the candidate architecture §1–§14 as pasted. The local repository at `C:\dev\CyberPanel SCC` contains only `LICENSE` (commit `d7b1b9f`), so nothing exists yet to check the architecture against. I did not modify, create, or commit anything.

**Scope note:** I say "verify" wherever a finding depends on how CyberPanel, cPanel, or DirectAdmin behave. Those claims come from general platform knowledge. They are not confirmed against current releases.

---

## 1. Executive Summary

**Overall condition:** The architecture is a strong **principles and domain-vocabulary layer**. It does not yet contain a **security enforcement architecture**. §§1–14 describe well what SCC must believe, show, and refuse to do. They do not say *where code runs*, *with what privilege*, *who can instruct whom*, or *how "no generic shell" is actually enforced* rather than just intended.

**Internal coherence:** Mostly coherent at the principle level. At the state-vocabulary level there are several real contradictions:
- ownership and management values are mixed together in the §13 dashboard
- "Integration state" in §2 actually lists Security System state
- the §8 Job state set cannot represent the "uncertain" outcome that §8 itself requires
- "adoption" means two different things

**Biggest strengths:**
- Keeping detection, Integration, management, ownership, health, compatibility, and authorization separate. This is the architecture's most valuable property, and it is applied consistently.
- "Unknown is valid, and discovery failure is not absence." This prevents a whole class of false-certainty bugs.
- A firm ban on generic execution, and an explicit refusal to promise rollback universally.
- Treating external changes as normal, and never attributing them to SCC without evidence.
- Separating the Registry from the Inventory.

**Biggest risks:**
1. **The runtime topology and privilege boundary are undefined.** A CyberPanel plugin normally runs inside CyberPanel's own web process. That process likely already has broad privileged execution paths (verify). If so, §9's "the web application must not have unrestricted root access" may be unachievable in the obvious deployment.
2. **The Integration trust model rests on self-declaration.** Integrations are code. "Declared capabilities must correspond to actual implementation" cannot be enforced against code that runs in-process with privilege. §14 also allows externally supplied Integrations.
3. **The authorization model has no principals, permission grammar, or bootstrap.**
4. **Recovery mode has no way to authenticate** when the thing that failed is the Platform Adapter or the database holding authorization metadata. Its only options are a deadlock or a bypass.

**Ready for adoption?** No, not as the canonical architecture. The philosophy, terminology, and doctrine can be locked now. The enforcement layer (topology, privileged execution contract, authorization model, recovery authentication, reconciliation semantics) has to be added before implementation of anything that changes state. These additions leave the philosophy unchanged; they fill in structure it currently lacks.

**Additional architectural work required?** Yes. See §§17–18 of this report.

---

## 2. Critical Findings

### CRIT-01: Runtime topology and privilege boundary undefined; likely contradiction with plugin hosting
- **Severity:** CRITICAL
- **Type:** Omission + hidden unsafe assumption + likely contradiction
- **Affected Sections:** §9, §11, §8, §12, §13
- **Finding:** The architecture never states which processes exist, which user each runs as, or how they talk to each other. §9 says the web application must not have unrestricted root access, and that privileged work should go through a "controlled worker/mechanism". §11 says SCC integrates through CyberPanel plugin registration and session auth. In the natural implementation, that puts SCC's web tier inside CyberPanel's web process. CyberPanel's web tier has historically run with, or had direct access to, root-level command execution utilities (verify against current CyberPanel).
- **Why It Matters:** If SCC's web code runs in a process that can already execute as root, the privileged worker adds no isolation. Any SCC web-tier bug, and any CyberPanel bug, reaches root without passing SCC's worker, validation, or audit. Conversely, if SCC runs as its own daemon, then "CyberPanel failure must not take down SCC" (§11) and "identity comes from CyberPanel" (§9) need a defined cross-process identity handoff.
- **Consequence:** Engineers will make the most consequential security decision in the system (process layout and trust direction) ad hoc. Most likely they will pick in-process execution because it is easiest, which quietly voids §9.
- **Evidence:** §9 lists "Privileged work should be isolated through a controlled worker/mechanism" as a requirement, but defines no worker. §11 lists integration surfaces but no execution location. §8 describes Jobs but not which process executes them.
- **Potential Resolution(s):**
  - (a) Add a *Runtime Topology & Trust Boundaries* section that names each process: web and UI tier, SCC core service, privileged executor, and Integration host. For each, give its OS identity, the channel it uses, and the direction of trust.
  - (b) Require the privileged executor to **re-verify every request on its own**: authorization token, capability, parameter schema, and target allowlist. It must never trust the web tier's validation.
  - (c) State explicitly what SCC can guarantee when the parent panel is itself root-equivalent. SCC cannot protect against its own host. This belongs in the threat model, not left implicit.

### CRIT-02: Integration code trust and privileged execution contract undefined
- **Severity:** CRITICAL
- **Type:** Omission + unsafe assumption
- **Affected Sections:** §2, §4, §8, §9, §14, §6
- **Finding:** The architecture says Integrations "execute" operations (§6: "Execution occurs through the Integration"). It says access is "limited to declared capabilities" (§9) and that "declared capabilities must correspond to actual implementation" (§14). But an Integration is code. If that code runs privileged operations itself, capability declarations are metadata that nothing enforces. The "no generic shell" rule then holds only as far as code review catches violations. §14 also allows "locally developed" and "externally supplied" Integrations.
- **Why It Matters:** This is the single largest attack surface. A malicious or compromised Integration (or an Integration update) that runs in-process with privilege is a root backdoor, and it passes every principle in the document. "Integration isolation is mandatory" is stated without saying what the isolation is against: crashes, or malice.
- **Consequence:** Either the "no arbitrary command" doctrine can't be enforced, or every Integration must be trusted as fully as SCC core. In the second case, third-party Integrations are unsafe.
- **Evidence:** Nowhere does the architecture say *who* performs the privileged syscall or subprocess. "Isolation" is never given a threat model (fault isolation versus security isolation).
- **Potential Resolution(s):**
  - (a) **Split Integration logic from privileged effect.** Integrations run unprivileged and emit *structured operation requests* drawn from a closed vocabulary that the privileged executor owns (for example: manage a named systemd unit, write a file under a declared path allowlist, install a package from a declared repository). The executor enforces the Integration's declared scope. This makes capability declarations mechanically enforceable.
  - (b) Decide the isolation model explicitly (in-process, subprocess, sandboxed), and whether it is fault isolation, security isolation, or both.
  - (c) **Defer non-built-in Integrations** until the (a) model exists. In v1, only allow Integrations shipped and signed with SCC itself. See §16 of this report.

### CRIT-03: Authorization model has no principals, permission grammar, or bootstrap
- **Severity:** CRITICAL
- **Type:** Omission
- **Affected Sections:** §9, §11, §13, §10, §12
- **Finding:** §9 requires authorization that is capability-aware, split into read and write, and stronger for high risk. It does not define:
  - who the principals are (CyberPanel admin, reseller, user, service identities, recovery operator)
  - the permission grammar (capability × Security System × target × risk class?)
  - who grants permissions, and where grants are stored
  - how the first administrator gets SCC permissions (bootstrap)
  - how parent-panel roles map to SCC permissions
  - how "stronger controls" for high risk are implemented (re-authentication? a second approver? a time delay?)
- **Why It Matters:** Every state-changing path in §§4, 6, 8, and 12 gates on this model. Without it, the first implementation will almost certainly be "CyberPanel admin can do everything". That erases the "SCC retains capability-level authorization" requirement without anyone noticing.
- **Consequence:** Capability and authorization collapse into one in practice. There is also no answer for multi-tenant panels: cPanel and DirectAdmin resellers and users, and CyberPanel resellers.
- **Evidence:** §9 lists properties of authorization, not a model. §11 says "SCC owns authorization metadata" but doesn't say what that metadata is.
- **Potential Resolution(s):**
  - (a) Add an Authorization Model section defining: principal types, a platform-neutral role model with per-adapter mapping, the permission tuple, risk classes, step-up mechanisms, the bootstrap rule, and revocation semantics for queued Jobs.
  - (b) At minimum, state explicitly that v1 is "parent-panel superadmin only, and every action requires an explicit SCC grant". Defer delegation.

### CRIT-04: Recovery-mode authentication either deadlocks or bypasses
- **Severity:** CRITICAL
- **Type:** Contradiction
- **Affected Sections:** §12, §9, §11
- **Finding:** Recovery mode is needed exactly when there is a "broken Platform Adapter", a "failed migration", "corrupt configuration", or failed startup validation. But identity comes through the Platform Adapter (§9, §11), and authorization metadata lives in SCC's own data store (§11), which may be the thing that is corrupt. §9 says uncertain authorization means denial. So recovery can't authenticate or authorize, unless a secondary path exists. Any undocumented secondary path is exactly what §9 prohibits.
- **Why It Matters:** This is a direct deadlock-versus-bypass contradiction. In practice, teams resolve it under pressure with a hidden override flag or file.
- **Consequence:** Either SCC can't be recovered without manual database surgery, or a backdoor appears.
- **Potential Resolution(s):**
  - (a) Define recovery authority as **local OS root via an SCC CLI** (host console or SSH). This is already the ultimate authority on the box, so it creates no new trust. The recovery UI then becomes optional or read-only.
  - (b) Define a minimal *recovery authorization store* that is independent of the main database and integrity-checked.
  - (c) Enumerate what recovery mode may do: diagnostics, restore, migration repair. It must never perform Security System actions.

---

## 3. High-Priority Findings

### HIGH-01: Ownership and management vocabularies overlap, and the §13 dashboard mixes them
- **Type:** Contradiction + terminology problem
- **Sections:** §2, §3, §5, §13
- **Finding:** `observation_only` appears as an ownership mode (§2, §5), a management state (§3, §5), and an Integration kind (§14). The §13 dashboard counts "6 fully managed, 3 partially managed, **2 external**, 1 observation only" under **Management**. But `external` is an ownership mode, and the numbers sum to 12, so it treats ownership and management as a single dimension. That violates §13's own rule against collapsing these into one status. There is also no matrix of valid combinations. Can a system be `owned` + `unmanaged`? `external` + `fully_managed`? What is the difference between `unmanaged` and `observation_only`?
- **Consequence:** Every engineer will invent their own state lattice. UI counts will contradict backend semantics.
- **Resolutions:** Define ownership and management as orthogonal axes and publish a valid-combination matrix. Rename one of the `observation_only` values (for example, ownership becomes `observe`, or management becomes `read_only`). Fix the §13 example.

### HIGH-02: "Adoption" means two things; ownership after install contradicts "explicit"
- **Type:** Contradiction + terminology problem
- **Sections:** §3, §5, §6, §8
- **Finding:** §3's "Existing-System Adoption" is an automatic inventory step on install (discover, associate, determine capabilities). §5 says "Adoption is explicit" and SCC "must never force ownership". §6 ends its lifecycle with "→ Adoption" and says "Ownership is established only after successful verification". Read literally, a successful install automatically makes the system `owned`. §8 says "Ownership changes occur only after verified installation/adoption".
- **Consequence:** It's unclear whether an SCC-installed system becomes owned automatically, whether "adoption" needs a separate authorization, and what happens after an external install of the same package.
- **Resolutions:** Split the terms: *association* (automatic, read-only Integration matching) versus *adoption* (explicit ownership transition). State whether installation authorization implicitly includes adoption, or whether adoption is a separate grant.

### HIGH-03: Job state set cannot represent the outcomes §8 requires
- **Type:** Contradiction + missing state
- **Sections:** §8, §6, §4, §10
- **Finding:** §8 says interrupted or uncertain execution must not be reported as failed or successful without evidence, and that completion requires verification. The defined states are `queued, running, completed, failed, cancel_requested, cancelled`. None of them means *outcome unknown*, *interrupted*, *verifying*, *partially completed*, *awaiting authorization/review*, or *verification failed after execution succeeded*.
- **Consequence:** Implementers will force uncertain outcomes into `failed`, which violates §8 and §10 directly.
- **Resolutions:** Add terminal and non-terminal states for: unknown/interrupted, verifying, partial, and (optionally) awaiting_approval. Separately, define an *execution outcome* and a *verification outcome* as two fields.

### HIGH-04: Which actions are Jobs is inconsistent
- **Type:** Contradiction/ambiguity
- **Sections:** §4, §8, §13
- **Finding:** §4 says "Long-running actions become Jobs." §8 says long-running or state-changing operations become Jobs "where appropriate". §13's action pipeline always includes a Job. For audit correlation (§10: actor → action → Job → execution → result), a Job either always exists or the chain has holes.
- **Resolutions:** Pick one rule, for example "every state-changing Action is a Job, regardless of duration". Specify how synchronous read Actions are correlated.

### HIGH-05: Plan-to-execution binding and TOCTOU are undefined
- **Type:** Omission (security)
- **Sections:** §4, §6, §8, §9
- **Finding:**
  - An installation plan is reviewed and authorized (§6), but nothing binds execution to *that exact plan*.
  - The server state can change between approval and execution: external change, another Job, a new package version in the repository.
  - "Sensitive operations revalidate authorization", but "sensitive" is undefined, as is what happens to queued Jobs when authorization is revoked.
  - Nothing says whether *preconditions* (not just authorization) are revalidated.
- **Consequence:** An approved plan can execute a different effect than the one approved: stale authorization and plan substitution.
- **Resolutions:** Make plans immutable, content-addressed objects. Authorization binds to the plan identity. Execution re-checks preconditions and refuses if the plan's inputs have drifted. Define plan expiry. Define revocation behavior for queued and running Jobs.

### HIGH-06: Lock domains and conflict model undefined; external actors cannot be locked
- **Type:** Omission
- **Sections:** §4, §8, §12
- **Finding:** "Locks may be required" is the whole locking specification. Real conflicts cross Security Systems:
  - Firewalld and any panel firewall UI share netfilter.
  - ModSecurity, CRS, and the web server are coupled.
  - A web server restart affects the TLS, WAF, and CRS systems.

  The parent panel and administrators working over SSH can't take SCC locks.
- **Resolutions:** Define a *resource/lock domain* concept that Integrations declare, separate from Security System identity. Define upgrade locks relative to Job locks. State that external actors can't be excluded, so verification plus reconciliation is the only defense against external races.

### HIGH-07: No sub-component or target model (jails, zones, rulesets, vhosts, certificates)
- **Type:** Omission
- **Sections:** §3, §4, §7, §14
- **Finding:** §14 requires that "Fail2Ban service state must be distinguishable from individual jail state". TLS must distinguish certificate, hostname, and service. ModSecurity rules apply per vhost. The §3 SecuritySystem model has no sub-component or target entity. §4 requires "target validation" but never defines a target.
- **Consequence:** Every Integration invents its own sub-model, core can't render or authorize per target, and per-target permissions become impossible.
- **Resolutions:** Add a generic *Component/Target* entity: owned by a Security System, with its own identity, state dimensions, and health, and addressable in Action parameters and authorization.

### HIGH-08: No relationships between Security Systems
- **Type:** Omission
- **Sections:** §3, §7, §14, §6
- **Finding:**
  - "Dependency health must be distinguishable" (§7).
  - "OWASP CRS should remain conceptually distinct from ModSecurity" (§14).
  - ModSecurity depends on the web server.
  - ClamAV-based scanning may depend on freshclam.

  The model has *Integration* dependencies (§14) but no *Security System ↔ Security System* relationships (depends_on, provides_rules_for, component_of, conflicts_with).
- **Resolutions:** Add a relationship edge set to the inventory model, with evidence and confidence like everything else.

### HIGH-09: "Reconcile" is undefined, and could mean enforcement
- **Type:** Ambiguity (dangerous)
- **Sections:** §4, §5, §7, §12
- **Finding:** "SCC must reconcile external changes" appears repeatedly. It never says whether reconciliation means *update SCC's model to match reality* (observe), or *restore SCC's desired configuration* (enforce). There is no desired-state or observed-state concept, and no drift concept. Enforcement would conflict with "no automatic remediation" (§7) and "SCC must never force ownership" (§5).
- **Consequence:** Somebody will implement "reconcile" as "re-apply", producing silent automatic changes.
- **Resolutions:** Define reconciliation as observation-only. Introduce *drift* as a recorded, visible condition (observed ≠ SCC's last applied configuration). Any restoration is an explicit, authorized Action.

### HIGH-10: No absence or removal lifecycle for Security Systems
- **Type:** Missing state
- **Sections:** §3, §5, §10
- **Finding:** Discovery failure ≠ absence. That is correct, but there is no rule for when SCC *may* conclude a system is gone: `not_detected`, `removed`, a tombstone, retention. The inventory will either grow forever or quietly delete entries, and deleting would violate "remain visible".
- **Resolutions:** Define a "successful negative observation" (every relevant probe succeeded and found nothing) as distinct from a probe failure. Define a `not_detected` state carrying last-seen evidence. Define whether ownership automatically lapses when an owned system disappears.

### HIGH-11: Integration–platform binding missing; core metadata hard-codes CyberPanel
- **Type:** Contradiction + multi-panel risk
- **Sections:** §2, §6, §11, §14, §13.55
- **Finding:** Integration compatibility metadata declares "CyberPanel versions" (§2, §14). §6 lists "OpenLiteSpeed version". But platform knowledge must stay behind Platform Adapters (§11). The ModSecurity Integration on CyberPanel must know CyberPanel/OLS paths and CyberPanel's management authority. On cPanel it must know EasyApache and vendor rule management (verify). Nothing says whether that knowledge belongs to the Integration, the Platform Adapter, or a platform-specific Integration variant.
- **Consequence:** Integrations accumulate `if platform == cyberpanel` branches. That is the same contamination §14 forbids in core, moved one layer down.
- **Resolutions:** Pick one:
  - (a) Platform Adapters expose a platform-neutral *Platform Services* interface (web server type and config locations, panel-managed security features, identity) that Integrations consume.
  - (b) Allow per-platform Integration variants that share an identity.

  Replace "CyberPanel versions" in the metadata schema with a generic "supported platforms and versions" field.

### HIGH-12: Same-origin UI embedding enables confused-deputy actions
- **Type:** Security risk
- **Sections:** §9, §11, §13, §13.55
- **Finding:** Native embedding in the parent panel (§13.55) usually means SCC's UI shares an origin and session with parent-panel pages. Any script injection in the parent panel, whether an XSS in a panel page or a compromised panel asset, can drive SCC actions *including confirmations*. §9 rightly says "confirmation is not authorization". But the "stronger controls" for high-risk actions are never defined in a way that holds up against a same-origin script.
- **Resolutions:** Define step-up for high-risk actions using a factor the DOM can't forge (re-authentication, or an out-of-band or CLI approval). Define CSRF and anti-automation expectations. List "compromised parent panel" explicitly in the threat model, together with what SCC can and cannot defend against.

### HIGH-13: Audit integrity threat model and audit-failure policy undefined
- **Type:** Omission/ambiguity
- **Sections:** §10, §12, §9
- **Finding:** "Append-only and integrity-protected" can't be absolute against local root, and possibly not against the SCC database user. Is the goal tamper-*proof* or tamper-*evident*? Against whom? Separately, "Audit failure cannot silently be represented as success" doesn't say whether state-changing Actions are **blocked** when audit writes fail (fail-closed) or proceed with an alarm.
- **Resolutions:** Specify tamper-evident audit (for example, a chained integrity scheme) plus optional off-host export as the only defense against local root. Specify fail-closed for state-changing Actions when audit is unavailable, or state the alternative explicitly.

### HIGH-14: Integration and SCC supply chain has no trust root
- **Type:** Omission
- **Sections:** §6, §12, §14
- **Finding:**
  - Nothing says who signs SCC releases, built-in Integrations, or Integration updates, or where the trust anchors live and how they rotate.
  - "Installation sources must be explicitly defined" doesn't say *who* defines them. If an Integration declares its own install sources, a malicious Integration supplies arbitrary URLs, circumventing §6's "no arbitrary installation URLs".
  - Nothing says how "independent Integration upgrades" (§12) are distributed.
- **Resolutions:** Define trust anchors and signing responsibility. Make install sources an allowlist that core or the administrator controls, not something an Integration can extend unilaterally. Tie Integration update authorization to the same model as SCC upgrades.

---

## 4. Medium Findings

**MED-01: Three overlapping Integration state vocabularies**
- **Type:** Terminology/contradiction
- **Sections:** §2, §14
- **Finding:** There are three lists: lifecycle (`available → validated → enabled → disabled → removed`), availability (`available, unavailable, disabled, incompatible, invalid, error`), and observability (`loaded, validated, compatible, healthy, degraded, error, unavailable`). "available" means different things in the first two. "healthy/degraded" reuses Security System health words (§7) with different meaning.
- **Resolution:** One Integration state machine, plus a separately named *Integration operational status* whose vocabulary is distinct from System health.

**MED-02: §2 "Integration state" lists Security System state**
- **Type:** Contradiction
- **Sections:** §2 vs §3/§14
- **Finding:** §2's "Integration state" (installed, version, enabled, running, configured, supported) is really Security System state. §3 says Integration state is recorded separately.
- **Resolution:** Retitle or move the §2 list.

**MED-03: Tri-state booleans can't express "not applicable"**
- **Type:** Missing state
- **Sections:** §3, §13
- **Finding:** CRS (a ruleset), SSH hardening, and TLS certificates have no meaningful "running" or "enabled" dimension. Without `not_applicable`, the UI shows `unknown` forever, which is a false signal of uncertainty.
- **Resolution:** Add `not_applicable`, and let Integrations declare which dimensions apply.

**MED-04: "configured" and "supported" as state dimensions are undefined or duplicated**
- **Type:** Ambiguity
- **Sections:** §3, §6, §12
- **Finding:** "configured" implies a baseline that doesn't exist. Configured to what, by whom? "supported" duplicates Compatibility (§12) and Eligibility (§6).
- **Resolution:** Define "configured" as "has an Integration-evaluable configuration and passes the Integration's minimum-validity check", or remove it. Replace the "supported" state dimension with a reference to the Compatibility determination.

**MED-05: Singular Integration association vs multiple Integrations**
- **Type:** Contradiction
- **Sections:** §3 model vs §14
- **Finding:** The §3 SecuritySystem has `integration.available/version/capabilities` (singular). §14 allows multiple Integrations per System and one Integration spanning multiple Systems. Nothing defines arbitration: whose health is canonical, whose capability executes, or how conflicts are resolved.
- **Resolution:** Make the association many-to-many with a declared role (primary or observer). Define arbitration, or defer multiplicity explicitly (see §16 of this report).

**MED-06: Event model undefined; audit vs history vs domain events blur**
- **Type:** Ambiguity
- **Sections:** §3, §7, §10, §13
- **Finding:** Discovery and health "may become events". Audit event types include `SYSTEM_DETECTED` and `HEALTH_CHANGED`. §7 wants health history. §10 says audit is distinct from history and must control noise. A flapping health check becomes audit spam.
- **Resolution:** Define a domain event stream. Audit records only accountability-relevant facts (actor-caused or security-significant). History and notifications are consumers of the event stream.

**MED-07: Attention Required has no derivation, lifecycle, or scope**
- **Type:** Omission
- **Sections:** §13
- **Finding:** Nothing says what generates an attention item, whether it can be acknowledged or snoozed, or whether it is per user or global. Without rules, it tends to drift into a covert score.
- **Resolution:** Define attention items as explicit, evidence-linked conditions with their own lifecycle (open, acknowledged, resolved-by-observation).

**MED-08: Scheduling, freshness thresholds, and resource bounds**
- **Type:** Architectural gap (partially an implementation detail)
- **Sections:** §3, §7
- **Finding:** Nothing says who triggers discovery and health, at what cadence, or who defines staleness (per check? per Integration?). "Bounded" has no owner.
- **Resolution:** Integrations declare freshness TTL and cost class. Core owns the scheduler and the global budget.

**MED-09: Sensitive-data classification undefined**
- **Type:** Omission
- **Sections:** §3, §8, §9, §10, §13
- **Finding:** Evidence, diagnostics, and Job logs may contain configuration secrets, keys, and IPs. Redaction is required everywhere, but no classification or redaction boundary exists. Nothing says who redacts: the Integration or core.
- **Resolution:** Integrations tag fields with a sensitivity class. Core redacts at persistence and presentation boundaries.

**MED-10: Presentation Adapter and Parent Theme are missing from §12 version domains**
- **Type:** Contradiction
- **Sections:** §12 vs §13.55.5, §13.55.8
- **Finding:** §13.55.8 requires theme and presentation-adapter compatibility, but §12's version-domain list omits both. It also doesn't say whether the Presentation Adapter is part of the Platform Adapter or a separately versioned component.
- **Resolution:** Make that decision, then add it to §12.

**MED-11: Theme fallback vs "no copying parent styles"**
- **Type:** Ambiguity
- **Sections:** §13.55.2, §13.55.4
- **Finding:** When a platform exposes no theme API or tokens (plausibly CyberPanel, verify), the "compatibility layer" either approximates the parent's look, which drifts toward "copying parent styles", or is a neutral SCC default. Also undefined: what is displayed while theme compatibility is `unknown`.
- **Resolution:** Define the fallback as a neutral SCC default. Define that `unknown` theme compatibility uses the fallback until assessed.

**MED-12: Parent theme controls "status semantics"**
- **Type:** Security/integrity risk
- **Sections:** §13.55.3
- **Finding:** If the parent theme maps status colors or icons, a broken or compromised theme could render "unhealthy" as benign.
- **Resolution:** Status semantics stay core-owned. The theme may style them but not remap meaning. Always require a text label (this is already partly implied by the accessibility rules).

**MED-13: SCC's own uninstall lifecycle undefined**
- **Type:** Omission
- **Sections:** §5, §11, §12
- **Finding:** "Removing SCC must not remove Security Systems" is necessary but not sufficient. What happens to:
  - SCC-owned systems whose scheduled scans or config regeneration depended on SCC?
  - SCC-applied configuration?
  - audit data (export before removal)?
  - panel registration?
- **Resolution:** Add an SCC Removal lifecycle: pre-removal report, audit export, ownership release, and what persists.

**MED-14: Downgrade is not addressed**
- **Type:** Omission
- **Sections:** §12
- **Finding:** Rollback is discussed; *downgrade after a successful migration* is not. Consider a forward-migrated schema, audit records containing event types the old code doesn't know, and Integrations newer than the core API.
- **Resolution:** Declare downgrade as restore-from-pre-upgrade-backup only, or define schema backward-compatibility windows.

**MED-15: Web server, init system, and virtualization are missing from compatibility domains**
- **Type:** Omission
- **Sections:** §6, §12
- **Finding:** The following are all load-bearing for firewall, WAF, and service Integrations, but none is modeled: web server type and version (§13 even displays it), init system (§3 assumes systemd), package-manager family, netfilter backend, MAC framework (SELinux/AppArmor), and container/VPS type (firewall behavior in LXC/OpenVZ differs).
- **Resolution:** Add a *Host Environment* compatibility domain that a platform-neutral host probe fills in.

**MED-16: Single category per Integration**
- **Type:** Overconstraint
- **Sections:** §2, §14
- **Finding:** CrowdSec, Imunify, and similar products span several categories.
- **Resolution:** Allow multi-category, with one designated as primary.

**MED-17: Unknown-system detection scope and identity rules**
- **Type:** Ambiguity
- **Sections:** §2, §3
- **Finding:** "Unknown security-related services" requires a heuristic for "security-related", which is either noisy or incomplete. "Stable unknown identities" needs a fingerprint rule that survives package rename and reinstall.
- **Resolution:** Core owns a declared, versioned heuristic catalogue. Identity is derived from the strongest stable evidence, and the derivation is recorded.

---

## 5. Low / Observational Findings

- **LOW-01:** Are audit *reads* audited? §10 authorizes audit access but is silent on whether viewing audit, evidence, or secrets creates records. (§10, §13)
- **LOW-02:** Dry-run authorization class is undefined (read or write permission?). Dry-run must itself be guaranteed side-effect-free. (§4)
- **LOW-03:** Job retention "must be defined" but has no owner. This is an implementation detail provided the audit↔Job link survives Job cleanup. (§8, §10)
- **LOW-04:** "Healthy ≠ Secure" is in §13's distinctions, but "Secure" is never defined anywhere. That's fine, and consistent with "no score". Worth a sentence stating that SCC never asserts "secure". (§13)
- **LOW-05:** Notifications are declared separate but not otherwise specified. This is a reasonable deferral. (§8, §13)
- **OBS-01:** Multi-server and fleet management aren't mentioned. It is reasonable for v1 to be implicitly single-host; say so explicitly.
- **OBS-02:** Multi-tenant visibility (should a reseller ever see SCC?) is unmentioned. It only matters because cPanel and DirectAdmin are explicitly in scope.
- **OBS-03:** "SSH Security" and "TLS/SSL" are *policy views across mechanisms* rather than products. The §0 terminology ("configuration-backed mechanism") allows this, but they stress ownership: who "owns" a hostname certificate issued by the panel's ACME client? They are good architecture-exercising choices; their ownership should be explicitly `external` by default.

---

## 6. Cross-Section Contradiction Matrix

| Finding | Section A | Section B | Conflict | Severity | Resolution Needed |
|---|---|---|---|---|---|
| CRIT-01 | §9 web app not root | §11 plugin/session integration | Likely in-process hosting inside a privileged panel process | CRITICAL | Topology section |
| CRIT-04 | §12 recovery for broken adapter/DB | §9/§11 identity via adapter; fail-closed | Recovery can't authenticate without bypass | CRITICAL | Recovery authority definition |
| CRIT-02 | §14 declared caps = implementation; external Integrations | §9 access limited to declared caps | Declaration can't be enforced against in-process code | CRITICAL | Execution contract |
| HIGH-01 | §5 management states | §13 dashboard "2 external" under Management | Ownership value counted as management state | HIGH | Fix vocab + example |
| HIGH-01 | §5 ownership `observation_only` | §5 management `observation_only` | Same token, two axes | HIGH | Rename |
| HIGH-02 | §5 adoption explicit, never force | §3 automatic "Existing-System Adoption" | Term collision | HIGH | Split terms |
| HIGH-02 | §6 ownership after verification | §5 transitions explicit | Is install→owned automatic? | HIGH | Explicit rule |
| HIGH-03 | §8 uncertain ≠ failed/success | §8 Job state set | No state for uncertain | HIGH | Add states |
| HIGH-04 | §4 long-running → Job | §13 every action → Job | Job cardinality | HIGH | Single rule |
| HIGH-09 | §4/§5 must reconcile | §7 no automatic remediation | Reconcile could mean enforce | HIGH | Define reconcile |
| HIGH-11 | §2/§14 metadata: CyberPanel versions | §11/§14 platform knowledge behind adapter | Core schema is panel-specific | HIGH | Generic platform field |
| HIGH-14 | §6 no arbitrary install URLs | §14 external Integrations declare sources | Integration can supply sources | HIGH | Source allowlist ownership |
| MED-02 | §2 Integration state (running…) | §3 Integration state separate | Mislabeled list | MEDIUM | Retitle |
| MED-01 | §14 lifecycle "available" | §14 availability "available" | Same word, different meaning | MEDIUM | Unify |
| MED-01 | §14 Integration "healthy/degraded" | §7 System health states | Vocabulary reuse across separate concepts | MEDIUM | Distinct vocab |
| MED-05 | §3 singular `integration` | §14 many-to-many | Cardinality | MEDIUM | Many-to-many + arbitration |
| MED-06 | §10 audit ≠ history | §10 HEALTH_CHANGED/SYSTEM_DETECTED in audit; §7 health history | Overlap/noise | MEDIUM | Event model |
| MED-10 | §12 version domains | §13.55.8 theme/presentation compat | Missing domains | MEDIUM | Add to §12 |
| MED-15 | §6 compat: OpenLiteSpeed | §12 domains lack web server | Undeclared domain | MEDIUM | Host Environment domain |
| MED-04 | §3 state `supported` | §6 eligibility / §12 compatibility | Three encodings of one fact | MEDIUM | Single source |

---

## 7. Missing Architectural Concepts

| Concept | Why needed | Affected | Proposed place |
|---|---|---|---|
| Runtime topology / process identities | Privilege isolation can't be designed otherwise | §8, §9, §11, §12 | New section |
| Privileged Executor + closed operation vocabulary | Makes "no generic shell" enforceable | §2, §4, §8, §9, §14 | New section |
| Principal / Role / Grant / Permission tuple | Authorization can't be implemented | §9, §11, §13 | New section |
| Recovery authority | Resolve CRIT-04 | §9, §12 | §12 amendment |
| Plan (immutable, bound to authorization) | TOCTOU, plan substitution | §4, §6, §8 | §4/§6 |
| Component/Target | Jails, zones, certs, vhosts | §3, §4, §7, §14 | §3 |
| System↔System relationships | Dependency health, CRS/ModSec, conflicts | §3, §7, §14 | §3 |
| Lock / resource domain | Concurrency | §4, §8, §12 | §8 |
| Desired vs observed state; Drift | Defines reconcile safely | §4, §5, §7 | New or §5 |
| Negative observation / not_detected | Absence lifecycle | §3 | §3 |
| Domain event stream | Separates audit/history/notifications | §3, §7, §10, §13 | New section |
| Attention item | Dashboard requirement | §13 | §13 or §7 |
| Integration–Platform binding (Platform Services) | Multi-panel viability | §11, §14 | §11/§14 |
| Host Environment domain | Compatibility completeness | §6, §12 | §12 |
| Sensitivity classification | Consistent redaction | §3, §8–§10, §13 | §9 |
| Trust anchors / signing | Supply chain | §6, §12, §14 | §9 or new |
| Scheduler / freshness TTL | Staleness semantics | §3, §7 | §3/§7 |
| SCC self-lifecycle (install/bootstrap/remove) | Bootstrap auth, clean removal | §9, §11, §12 | New section |
| Persistence model (store, secrets store, retention) | Where "SCC owns its own data" lives | §11, §12 | New section |
| Capability-level compatibility | Partial compatibility meaning | §12, §14 | §12 |

---

## 8. State Model Audit

**States and transitions I believe exist:**
- **Discovery confidence:** confirmed / probable / possible / unknown
- **SecuritySystem dimensions** (installed, enabled, running, configured, healthy, supported): each true / false / unknown
- **Health:** healthy / degraded / unhealthy / unknown
- **Ownership:** owned / external / observation_only
- **Management:** fully / partially / observation_only / unmanaged / unknown
- **Compatibility:** supported / partially_supported / unsupported / unknown
- **Eligibility:** supported / unsupported / unknown
- **Integration lifecycle:** available→validated→enabled→disabled→removed
- **Integration availability:** available / unavailable / disabled / incompatible / invalid / error
- **Integration observability:** loaded / validated / compatible / healthy / degraded / error / unavailable
- **Job:** queued / running / completed / failed / cancel_requested / cancelled
- **Install workflow:** Detection→Integration→Compatibility→Plan→Review→Preparation→Install→Configuration→Verification→Adoption
- **Rollback:** supported / limited / unavailable
- **SCC run mode:** normal / degraded / recovery (implied)
- **Theme:** native / fallback; compatibility compatible / unknown

**Missing states:**
- Job: interrupted/unknown outcome, verifying, partial, awaiting_approval, verification_failed
- SecuritySystem: not_detected/removed; `not_applicable` per dimension; stale (freshness as a state, not just a timestamp)
- Ownership: transitional states (adopting, releasing)
- Plan: draft / approved / expired / superseded / executed
- Install workflow: no mapping to Job states, so "paused on conflict" (§6) has no representation, since §8 defers "waiting/paused"
- Upgrade: preflight / locked / migrating / migrated-unverified / rolled-back / failed-unknown
- SCC run mode: entry and exit conditions for degraded and recovery modes
- Integration: quarantined (failed integrity after load)

**Impossible or contradictory combinations needing rules:**
- `owned` + `unmanaged`
- `external` + `fully_managed` (does CyberPanel-as-authority permit this?)
- `observation_only` ownership + `fully_managed`
- Health `healthy` while installed=`false` (possible only with bad evidence; should be flagged, not stored)
- Integration `incompatible` while its capabilities are still registered as executable

**Ambiguous transitions:**
- Install success → owned (automatic?)
- Integration removed → management state becomes? (unknown vs unmanaged)
- System upgraded externally → compatibility re-evaluation → capabilities revoked mid-Job?
- Compatibility `unknown` after a panel upgrade → are write capabilities suspended until assessed?

**Dangerous transitions:**
- external→owned without the administrator seeing what SCC will now consider its responsibility
- Releasing ownership or disabling an Integration while a Job is running on that system
- Recovery→normal without full startup revalidation
- Compatibility `unknown`→treated as supported by default (§12 forbids this, but no transition rule enforces it)
- Queued Job executing after the grantor's authorization was revoked

---

## 9. Security Threat Model Findings

| Threat | Architectural status | Required mitigation |
|---|---|---|
| Malicious Integration | Unmitigated (CRIT-02) | Unprivileged Integration host; closed executor vocabulary; scope enforcement by executor; signed built-ins only in v1 |
| Compromised Integration (bug) | Partially: "isolation" undefined | Same as above; per-Integration path/unit allowlists |
| Malicious administrator | Partially: audit exists, but a local root admin can tamper | State limits honestly; tamper-evident audit + off-host export; two-person approval as optional high-risk control |
| Compromised hosting panel | Unaddressed | Threat model must declare panel = trusted computing base for identity; SCC can't defend against a root-equivalent panel; step-up factor outside panel DOM (HIGH-12) |
| Compromised Security System | Unaddressed | Treat Security System output (health, API responses, logs) as untrusted input: parse strictly, bound size, never interpolate into operations, escape in UI |
| Privilege escalation | Depends on CRIT-01 | Executor re-validates everything; web tier holds no privileged credentials |
| Authorization race / stale authorization | Partially | HIGH-05: plan binding, revocation checks at execution |
| Job/Action replay & duplication | "Idempotency must be defined" only | Single-use Action identifiers; executor rejects reused IDs; idempotency keys per Plan |
| Parameter manipulation | Principle stated | Typed parameter schemas declared per capability; executor-side validation independent of UI |
| Path traversal | Not mentioned explicitly | Executor path allowlists per Integration; canonicalization before check; no symlink following outside allowlist |
| Command injection | "No concatenation" stated | Executor uses argv-vector invocation only; vocabulary operations never accept free-form strings passed to shells |
| Arbitrary shell | Prohibited in principle | Enforced only if CRIT-02 is resolved; also "diagnostics" must be a fixed set of read-only probes |
| Secret exposure | Principle stated | MED-09 classification; secrets store separate from main DB; never in evidence/Job logs by default |
| Audit tampering / suppression | Principle stated | HIGH-13; audit writer separate from web tier; fail-closed policy |
| Recovery-mode abuse | Principle stated, but contradictory (CRIT-04) | OS-root CLI recovery authority; recovery cannot run Security System actions |
| Malicious SCC upgrade | Unaddressed | Signed releases; trust anchors; upgrade authorization; preflight verifies signature before any migration |
| Malicious Integration update | Unaddressed | Same channel/signing as SCC for v1; capability-set diff shown and authorized on update ("capability escalation on update") |
| Package/artifact substitution | "Integrity verified" | Define verification root (distro repo signing keys vs pinned hashes); plan binds exact artifact identity |
| Dependency compromise | Partially | Dependency sources subject to same allowlist; dependency authorization shows exact versions/sources |
| Theme/presentation spoofing | Unaddressed | MED-12: core-owned status semantics |

One gap is worth calling out on its own. **Capability escalation through Integration update:** an Integration update that adds `uninstall` or `configure` capabilities isn't covered by any stated authorization rule.

---

## 10. Compatibility Audit

```
SCC (core version, schema version, core↔Integration API version)
 ├─ Platform Adapter (version; adapter↔core API)
 │    ├─ Hosting Panel (product, version, build, edition)
 │    ├─ Presentation Adapter (version?)  ← unclear if separate (MED-10)
 │    │    └─ Parent Theme (theme/skin id, version, capabilities)
 │    └─ Panel-managed security features (MISSING as a domain)
 ├─ Host Environment (MISSING as a unified domain)
 │    ├─ OS family/version
 │    ├─ Architecture
 │    ├─ Init system (MISSING)
 │    ├─ Package manager family (MISSING)
 │    ├─ Web server type/version (MISSING in §12)
 │    ├─ Netfilter backend / kernel features (MISSING)
 │    ├─ MAC framework (MISSING)
 │    └─ Virtualization/container type (MISSING)
 ├─ Security Integration (version; declared compat)
 │    ├─ Integration ↔ Integration (MISSING: e.g., CRS Integration requires ModSecurity Integration)
 │    └─ Capability-level compatibility (MISSING)
 └─ Security System (version)
      ├─ Security System dependencies (versions)
      └─ Security System ↔ Security System conflicts (MISSING as a relationship)
```

**Can §12 and §13.55 represent partial compatibility?** Not adequately. `partially_supported` is a single value attached to a whole pairing. It can't say *which capabilities* remain valid. For example: read and health work, but configure is disabled because the configuration format changed. That is the most common real case, and it is what the UI must show. Compatibility needs to be evaluated per (Integration × System version × Host Environment × Platform) **per capability**, and the result has to feed capability registration directly. That would include downgrading write capabilities to unavailable whenever compatibility is `unknown`.

**Also missing:** *time*. A compatibility determination needs evidence and `evaluated_at`, and it becomes stale on any upstream version change.

---

## 11. Integration Model Stress Test

1. **Simple service (Fail2Ban service-level)**
   - **Result:** Works.
   - **Support:** Good.
   - **Gap:** Jails need the Component model (HIGH-07).
   - **Rec:** Add Component/Target.
2. **Configuration-only mechanism (SSH hardening)**
   - **Result:** Partially works.
   - **Gap:** No `not_applicable` for running or enabled (MED-03). "configured" is undefined (MED-04). Ownership of sshd_config is shared with the administrator and possibly the panel.
   - **Rec:** Per-dimension applicability. Default ownership is external.
3. **Multiple services as one System (ClamAV: clamd + freshclam)**
   - **Result:** Ambiguous.
   - **Gap:** No rule for aggregating service states into one System's `running` value. Can "running" be partial?
   - **Rec:** Component model plus Integration-defined aggregation, with evidence.
4. **One System, multiple Integrations**
   - **Result:** Breaks.
   - **Gap:** Singular association; no arbitration (MED-05).
   - **Rec:** Define arbitration or defer.
5. **One Integration, multiple Systems (ModSecurity Integration also inspecting CRS)**
   - **Result:** Breaks at model level. Also unclear whether CRS is a separate Integration.
   - **Rec:** Many-to-many; relationship edges (HIGH-08).
6. **Observation-only system**
   - **Result:** Works.
   - **Support:** Strong; one of the architecture's best-covered cases.
   - **Gap:** Vocabulary collision (HIGH-01).
7. **Externally managed system (panel-managed ModSecurity toggles)**
   - **Result:** Partially works.
   - **Gap:** "Management conflicts must be handled safely" is undefined. It isn't specified whether SCC capabilities are auto-restricted when the panel is the authority.
   - **Rec:** Rule: when an external management authority is detected, write capabilities default to unavailable unless explicitly adopted.
8. **Partially compatible system**
   - **Result:** Breaks.
   - **Gap:** Compatibility isn't per capability (§10 of this report).
   - **Rec:** Capability-level compatibility.
9. **System with no supported API (parse config files and logs only)**
   - **Result:** Works for observation.
   - **Gap:** Confidence and evidence for parsed output are fine. Treating that output as untrusted input is not stated.
   - **Rec:** Add to threat model.
10. **Configuration format changes (e.g., major CRS version)**
    - **Result:** Risky.
    - **Gap:** Nothing forces write capabilities off when the format is unrecognized.
    - **Rec:** Rule: unrecognized format → compatibility unknown for configure-class capabilities.
11. **System disappears externally**
    - **Result:** Breaks.
    - **Gap:** No absence lifecycle (HIGH-10). Ownership after disappearance undefined.
    - **Rec:** `not_detected` state; ownership rule.
12. **System upgraded outside SCC**
    - **Result:** Partially works.
    - **Gap:** Re-evaluation trigger is undefined, as is the effect on queued Jobs and approved Plans (HIGH-05).
    - **Rec:** Version change invalidates compatibility and pending Plans for that System.

---

## 12. Multi-Panel Audit

**Hidden CyberPanel assumptions:**
- Integration metadata field "supported CyberPanel versions" (§2, §14): panel-specific core schema.
- OpenLiteSpeed in §6 compatibility.
- The assumption that the panel supplies a single admin identity. cPanel (WHM ACLs, resellers) and DirectAdmin (admin/reseller/user levels) have richer role models (verify specifics). With no platform-neutral principal model (CRIT-03), the CyberPanel mapping becomes the de facto model.
- The implied in-process plugin hosting model (CRIT-01). Plugin execution models differ across panels: cPanel/WHM plugins and DirectAdmin plugins run under different user and privilege contexts (verify). A single "SCC runs as a panel plugin" topology won't port.
- "CyberPanel-owned security systems" (§11) is framed per panel, not generically as "panel-managed security features". On cPanel, cPHulk and vendor-managed ModSecurity rules have the same role. Any panel-bundled Imunify has it too.
- UI technology. "Native" presentation in three panels with different template and frontend stacks implies either three UI implementations or one framework-agnostic frontend that the Presentation Adapter wraps. That choice is unmade, and it is architectural.

**What holds up:** §13.55.6 (functional independence) and §14 (core product-neutrality) are the right rules. The Platform Adapter boundary is the right shape.

**What's needed:**
- A platform-neutral Platform Services interface (HIGH-11)
- A platform-neutral principal/role model with adapter mapping
- A decision on UI delivery (embedded server-rendered vs. adapter-hosted SPA)
- A generic "panel-managed security feature" concept

Without these, the second adapter will force a core refactor.

---

## 13. UI Architecture Audit

- **Command Center / second source of truth:** The principles are right ("UI is never authoritative"). The risk is *derived state*: attention items, dashboard counts, freshness. If the UI computes these, it becomes a second model. **Rule needed:** all derived classifications (attention, staleness, counts) come from the backend.
- **State presentation / unknown:** Well specified. `not_applicable` is missing (MED-03). The dashboard example is contradictory (HIGH-01).
- **Compatibility:** First-class in principle; can't show *which* capabilities are affected until compatibility is per capability.
- **Capabilities / authorization:** "Distinguish capability availability from permission" is good. There's no defined API contract that returns (capability, available?, authorized?, reason), and without one, UIs guess.
- **Jobs:** The failed-Job explanation requirements ("what changed / what did not") require the executor to record observed before/after per step. That isn't specified in §8.
- **Audit:** Separate interface; fine.
- **Parent theme / adapters:** See MED-10, MED-11, MED-12, and HIGH-12 (same-origin risk).
- **Failure isolation:** "UI failures must be isolated" doesn't say whether a per-Integration UI panel can be Integration-supplied code. If Integrations can contribute UI fragments, that is another code-trust boundary. **Recommend:** Integrations supply data and declarative descriptors only, never UI code.

---

## 14. Upgrade / Recovery Audit

- **SCC upgrade:** Preflight, locks, backups, and audit survival are well covered. Missing: signature verification as the *first* preflight step; the mode of operation during upgrade (read-only? fully down?); upgrade-lock semantics versus running Jobs (wait, cancel, or refuse?).
- **Integration upgrade:** Missing: capability-set diff and re-authorization (§9 of this report); what happens to in-flight Jobs using the old Integration version; whether persisted Integration configuration is migrated by the Integration (a migration contract per Integration).
- **Platform Adapter upgrade:** Barely addressed. Adapter-version compatibility with core isn't in the preflight list.
- **CyberPanel / OS upgrade:** Correctly external. Missing: the detection trigger, and a rule that affected capabilities are suspended (compatibility → unknown) until re-evaluated.
- **Security System upgrade:** Correctly external. Missing: invalidation of pending Plans.
- **Schema migration / interrupted migration:** Principles present. Missing: migration journal/marker so interruption can be detected (§12 requires detection but gives no mechanism); relationship to recovery mode entry.
- **Rollback / partial rollback:** Honest labelling (supported/limited/unavailable) is a real strength. Partial rollback (core rolled back, Integrations not) is unaddressed. Rollback of a Security System change and rollback of SCC are conflated in wording.
- **Incompatible downgrade:** Unaddressed (MED-14).
- **Recovery:** CRIT-04.

---

## 15. Implementability Audit

Questions a team would have to invent answers for on day one:

**ARCHITECTURAL GAPS**
1. What processes exist, and as which OS users? (CRIT-01)
2. Does SCC run inside the panel's web process?
3. Who executes privileged operations: the Integration or a core executor? (CRIT-02)
4. What is the closed set of privileged operations?
5. Are Integrations in-process? Is isolation for faults or for security?
6. Who are the principals? What is a permission? How is the first admin granted? (CRIT-03)
7. How are high-risk "stronger controls" implemented?
8. How does recovery authenticate? (CRIT-04)
9. Is every state-changing Action a Job? (HIGH-04)
10. What Job state represents an uncertain outcome? (HIGH-03)
11. Does install success make the system owned? (HIGH-02)
12. Valid ownership × management combinations? (HIGH-01)
13. Does "reconcile" ever change the server? (HIGH-09)
14. When is a Security System considered gone? (HIGH-10)
15. How are jails, zones, certs, and vhosts represented? (HIGH-07)
16. How are System↔System dependencies represented? (HIGH-08)
17. What does a lock protect, and how are lock domains declared? (HIGH-06)
18. How is an approved plan bound to execution? (HIGH-05)
19. Where does platform-specific knowledge for a product Integration live? (HIGH-11)
20. Is compatibility per capability? What happens to write capabilities when compatibility is unknown?
21. Does audit failure block Actions? (HIGH-13)
22. What are the trust anchors for signed artifacts? Who controls install-source allowlists? (HIGH-14)
23. Is the Presentation Adapter separately versioned? How is UI delivered across panels?
24. Can Integrations contribute UI code?
25. What is audited versus merely recorded as history? (MED-06)

**IMPLEMENTATION DETAILS** (legitimately deferrable)
- Database engine and schema layout
- Job queue technology
- Specific integrity-chain algorithm
- Scheduler cadences and default TTLs
- Retention periods
- Specific theme token names
- UI framework choice *within* a decided delivery model
- Log formats
- Exact confidence-scoring heuristics
- Notification channels

---

## 16. Overengineering / Complexity Review

**1. Externally supplied / locally developed Integrations in v1**
- **Current design:** Allowed, with trust metadata.
- **Why excessive:** It forces a full plugin-security model before one Integration exists.
- **Risk it prevents:** None; it *adds* risk.
- **Simplification:** v1 ships only built-in, signed Integrations. Third-party Integrations are deferred until CRIT-02's executor model is proven.
- **Tradeoff:** Community extensibility is delayed.

**2. Multiple Integrations per Security System**
- **Current design:** Supported "where appropriate".
- **Why excessive:** It needs arbitration rules and has no first-set use case.
- **Risk it prevents:** Future schema migration.
- **Simplification:** Model many-to-many in data but allow one *active* Integration per System in v1.
- **Tradeoff:** Minor future work.

**3. Runtime theme capability discovery (§13.55.4)**
- **Current design:** Runtime probing.
- **Why excessive:** Theme capabilities are a property of (adapter version, panel version). A static declaration plus a version check is simpler and more deterministic.
- **Risk it prevents:** Mis-rendering on panel updates.
- **Simplification:** Static capability declaration per adapter, invalidated by panel version change.
- **Tradeoff:** Less adaptive to unexpected panel variants.

**4. Full three-panel presentation contract up front**
- **Current design:** Detailed contract for three panels.
- **Why excessive:** Designing contract details without a second implementation usually produces the wrong abstraction.
- **Risk it prevents:** Core contamination.
- **Simplification:** Lock the *boundary rule* (no platform logic in core) and the functional-independence rule. Defer contract details until the second adapter.
- **Tradeoff:** Some refactor later, but the rules still keep core clean.

**5. Recovery mode as a full controlled UI**
- **Current design:** Recovery has a controlled UI.
- **Why excessive:** A recovery web UI must authenticate when authentication infrastructure is broken (CRIT-04).
- **Risk it prevents:** Admin inconvenience.
- **Simplification:** CLI-only recovery (OS-root authority), with an optional read-only web status page.
- **Tradeoff:** Less friendly for non-shell admins.

**6. Independent Integration upgrades**
- **Current design:** "Where practical".
- **Why excessive:** It adds a distribution channel, a compatibility matrix, and a supply-chain surface.
- **Simplification:** Integrations version with SCC releases in v1.
- **Tradeoff:** Slower Integration fixes.

**7. Three Integration state vocabularies**
- **Why excessive:** Redundant, and they diverge (MED-01).
- **Simplification:** One state machine plus one operational status.
- **Tradeoff:** None meaningful.

**8. Four confidence levels**
- **Assessment:** Reasonable, and it serves "no false certainty". **Keep.** The cost is low if the mapping from evidence to confidence is Integration-declared.

**9. Health history, audit export, version pinning**
- **Assessment:** Valuable, but not needed to prove the architecture. Mark as explicit deferrals rather than v1 requirements.

---

## 17. Recommended Architectural Changes

- **CHANGE-001**
  - **Affected section:** New section; §9, §11
  - **Reason:** CRIT-01
  - **Proposed change:** Define runtime topology, process identities, IPC channels, trust direction, and the panel-as-TCB statement.
  - **Impact:** Foundational; gates all privileged work.
  - **Dependencies:** None.
- **CHANGE-002**
  - **Affected section:** New section; §2, §4, §8, §14
  - **Reason:** CRIT-02
  - **Proposed change:** Define the Privileged Executor, the closed operation vocabulary, and per-Integration declared scope enforced by the executor. Integrations run unprivileged.
  - **Impact:** Makes "no generic shell" enforceable.
  - **Dependencies:** CHANGE-001.
- **CHANGE-003**
  - **Affected section:** New section; §9, §11, §13
  - **Reason:** CRIT-03
  - **Proposed change:** Authorization model: principals, platform-neutral roles with adapter mapping, permission tuple, risk classes, step-up, bootstrap, and revocation semantics.
  - **Impact:** Gates all actions.
  - **Dependencies:** CHANGE-001.
- **CHANGE-004**
  - **Affected section:** §12, §9
  - **Reason:** CRIT-04
  - **Proposed change:** Define recovery authority (e.g., OS-root CLI) and recovery's permitted operations.
  - **Impact:** Removes the deadlock and bypass.
  - **Dependencies:** CHANGE-001.
- **CHANGE-005**
  - **Affected section:** §2, §3, §5, §13
  - **Reason:** HIGH-01
  - **Proposed change:** Disambiguate `observation_only`, add an ownership × management validity matrix, and fix the dashboard example.
  - **Impact:** Vocabulary.
  - **Dependencies:** None.
- **CHANGE-006**
  - **Affected section:** §3, §5, §6, §8
  - **Reason:** HIGH-02
  - **Proposed change:** Split "association" from "adoption"; state the install→ownership rule.
  - **Impact:** Vocabulary and lifecycle.
  - **Dependencies:** CHANGE-005.
- **CHANGE-007**
  - **Affected section:** §8
  - **Reason:** HIGH-03, HIGH-04
  - **Proposed change:** Add Job states (interrupted/unknown, verifying, partial, awaiting_approval), separate execution and verification outcomes, and adopt "every state-changing Action is a Job".
  - **Impact:** Job model.
  - **Dependencies:** None.
- **CHANGE-008**
  - **Affected section:** §4, §6, §8
  - **Reason:** HIGH-05
  - **Proposed change:** Immutable, identity-bound Plans; authorization binds to Plan; precondition revalidation; expiry; revocation.
  - **Impact:** TOCTOU closure.
  - **Dependencies:** CHANGE-003, CHANGE-007.
- **CHANGE-009**
  - **Affected section:** §4, §8
  - **Reason:** HIGH-06
  - **Proposed change:** Lock/resource domains declared by Integrations; upgrade-lock semantics.
  - **Impact:** Concurrency.
  - **Dependencies:** CHANGE-010.
- **CHANGE-010**
  - **Affected section:** §3
  - **Reason:** HIGH-07, HIGH-08
  - **Proposed change:** Add the Component/Target entity and System↔System relationships.
  - **Impact:** Domain model.
  - **Dependencies:** None.
- **CHANGE-011**
  - **Affected section:** §4, §5, §7
  - **Reason:** HIGH-09
  - **Proposed change:** Define reconciliation as observation-only; introduce desired vs observed state and Drift; restoration is an explicit Action.
  - **Impact:** Prevents silent enforcement.
  - **Dependencies:** None.
- **CHANGE-012**
  - **Affected section:** §3
  - **Reason:** HIGH-10
  - **Proposed change:** Negative-observation rule; `not_detected` state; ownership-on-disappearance rule.
  - **Impact:** Inventory lifecycle.
  - **Dependencies:** None.
- **CHANGE-013**
  - **Affected section:** §2, §11, §14
  - **Reason:** HIGH-11
  - **Proposed change:** Platform Services interface; replace "CyberPanel versions" with generic platform compatibility; generic "panel-managed security feature".
  - **Impact:** Multi-panel viability.
  - **Dependencies:** CHANGE-001.
- **CHANGE-014**
  - **Affected section:** §9, §13
  - **Reason:** HIGH-12
  - **Proposed change:** Step-up factors outside the parent DOM; CSRF/anti-automation; panel-compromise threat statement.
  - **Impact:** High-risk action safety.
  - **Dependencies:** CHANGE-003.
- **CHANGE-015**
  - **Affected section:** §10
  - **Reason:** HIGH-13
  - **Proposed change:** Tamper-evidence model; off-host export as the defense against local root; fail-closed on audit unavailability for state-changing Actions.
  - **Impact:** Accountability.
  - **Dependencies:** CHANGE-001.
- **CHANGE-016**
  - **Affected section:** §6, §12, §14
  - **Reason:** HIGH-14
  - **Proposed change:** Trust anchors, signing, core-controlled install-source allowlist, capability-diff authorization on Integration update.
  - **Impact:** Supply chain.
  - **Dependencies:** CHANGE-003.
- **CHANGE-017**
  - **Affected section:** §12, §14
  - **Reason:** §10 of this report; stress tests 8 and 10
  - **Proposed change:** Capability-level compatibility; unknown compatibility disables write-class capabilities; compatibility evidence and timestamps.
  - **Impact:** Safe degradation.
  - **Dependencies:** None.
- **CHANGE-018**
  - **Affected section:** §12
  - **Reason:** MED-10, MED-15
  - **Proposed change:** Add Host Environment, web server, Presentation Adapter, and Parent Theme version domains.
  - **Impact:** Compatibility completeness.
  - **Dependencies:** CHANGE-013.
- **CHANGE-019**
  - **Affected section:** §2, §14
  - **Reason:** MED-01, MED-02
  - **Proposed change:** One Integration state machine plus a distinct operational-status vocabulary; retitle the §2 list.
  - **Impact:** Vocabulary.
  - **Dependencies:** None.
- **CHANGE-020**
  - **Affected section:** §3
  - **Reason:** MED-03, MED-04
  - **Proposed change:** Add `not_applicable`; define or remove "configured"; derive "supported" from Compatibility.
  - **Impact:** State model.
  - **Dependencies:** CHANGE-017.
- **CHANGE-021**
  - **Affected section:** §3, §14
  - **Reason:** MED-05
  - **Proposed change:** Many-to-many System↔Integration with roles; arbitration or v1 single-active rule.
  - **Impact:** Model cardinality.
  - **Dependencies:** None.
- **CHANGE-022**
  - **Affected section:** New section; §3, §7, §10, §13
  - **Reason:** MED-06, MED-07
  - **Proposed change:** Domain event model; audit-eligibility rule; Attention item lifecycle.
  - **Impact:** Noise control; UI integrity.
  - **Dependencies:** None.
- **CHANGE-023**
  - **Affected section:** §9
  - **Reason:** MED-09
  - **Proposed change:** Sensitivity classification with a defined redaction boundary.
  - **Impact:** Secret handling.
  - **Dependencies:** None.
- **CHANGE-024**
  - **Affected section:** §13, §13.55
  - **Reason:** MED-11, MED-12, §13 of this report
  - **Proposed change:** Fallback-theme definition; core-owned status semantics; backend-derived classifications only; Integrations supply no UI code.
  - **Impact:** UI integrity.
  - **Dependencies:** None.
- **CHANGE-025**
  - **Affected section:** New section; §11, §12
  - **Reason:** MED-13, MED-14
  - **Proposed change:** SCC self-lifecycle: install/bootstrap, removal, downgrade policy.
  - **Impact:** Lifecycle completeness.
  - **Dependencies:** CHANGE-003, CHANGE-004.
- **CHANGE-026**
  - **Affected section:** §14, §12
  - **Reason:** §16 of this report
  - **Proposed change:** Explicitly defer third-party Integrations, independent Integration upgrades, and multi-active Integrations to post-v1.
  - **Impact:** Attack-surface reduction.
  - **Dependencies:** None.
- **CHANGE-027**
  - **Affected section:** §8
  - **Reason:** HIGH-03 (a hazard observed while reviewing failed-Job UI requirements)
  - **Proposed change:** The executor records observed before/after per step, so the §13 "what changed / what didn't" is answerable.
  - **Impact:** Job transparency.
  - **Dependencies:** CHANGE-002.

---

## 18. Proposed Additional Sections

- **§15 Runtime Topology & Trust Boundaries**
  - **Purpose:** Processes, identities, channels, TCB statement.
  - **Why needed:** CRIT-01. Nothing else can be secured without it.
  - **Affects:** §8, §9, §11, §12
- **§16 Privileged Execution Contract**
  - **Purpose:** Executor, closed operation vocabulary, scope enforcement, argv-only invocation, path allowlists.
  - **Why needed:** CRIT-02.
  - **Affects:** §2, §4, §6, §8, §14
- **§17 Authorization Model**
  - **Purpose:** Principals, roles, grants, permission tuple, step-up, bootstrap, revocation.
  - **Why needed:** CRIT-03.
  - **Affects:** §9, §11, §13
- **§18 Threat Model**
  - **Purpose:** Adversaries, assets, trust assumptions (including what SCC explicitly cannot defend against: root-equivalent panel or admin).
  - **Why needed:** "Isolation", "integrity-protected", and "least privilege" are meaningless without a named adversary.
  - **Affects:** §9, §10, §14
- **§19 Persistence, Secrets & Data Lifecycle**
  - **Purpose:** Stores, secrets store, retention, backup scope, sensitivity classes.
  - **Why needed:** "SCC owns its own data" has no home.
  - **Affects:** §8, §10, §11, §12
- **§20 Reconciliation, Desired State & Drift**
  - **Purpose:** Observation-only reconcile semantics; drift representation.
  - **Why needed:** HIGH-09.
  - **Affects:** §4, §5, §7
- **§21 Event Model**
  - **Purpose:** Domain events vs audit vs history vs notifications vs attention.
  - **Why needed:** MED-06, MED-07.
  - **Affects:** §3, §7, §10, §13
- **§22 SCC Lifecycle (Install, Bootstrap, Removal, Downgrade)**
  - **Why needed:** MED-13, MED-14; bootstrap authorization.
  - **Affects:** §9, §11, §12

---

## 19. Adoption Readiness

**NOT READY FOR ADOPTION**

The determination rests on these facts:
- An engineering team starting tomorrow would have to invent the process topology, the privileged-execution mechanism, the authorization model, and recovery authentication. These are the four decisions that determine whether SCC's central security promises ("no generic shell", "least privilege", "capability ≠ authorization", "recovery is not a bypass") are enforceable or just aspirational.
- Two of these gaps are internal contradictions, not just omissions. A likely in-process plugin deployment conflicts with §9's least-privilege rule (CRIT-01), and recovery authentication conflicts with fail-closed authorization (CRIT-04).
- Several core state vocabularies contradict each other (HIGH-01 to HIGH-04). Persistence schemas would encode those contradictions from day one.

This determination does **not** mean the architecture is unsound. §1–§14's philosophy, terminology, and doctrine could be adopted as a *locked principles baseline* immediately. The remaining work is additive (new sections) plus corrections to vocabulary. It doesn't change the direction.

---

## 20. Final Audit Position

**Architecturally strong:**
- Separation of detection, Integration, management, ownership, health, compatibility, and authorization
- Unknown as a first-class state
- Discovery failure ≠ absence
- Registry ≠ Inventory
- No universal score
- Honest rollback labelling
- External-change doctrine
- Functional independence of theme from semantics
- Core product-neutrality rule
- The first-Integration selection principle (exercise patterns, not count)

**Must change before adoption:**
- CHANGE-001 to CHANGE-004 (topology, executor contract, authorization model, recovery authority)
- CHANGE-005 to CHANGE-008 (ownership/management vocabulary, adoption terminology, Job states and Job cardinality, Plan binding)
- CHANGE-011 (reconciliation semantics)
- CHANGE-013 (remove CyberPanel from core Integration metadata; Platform Services boundary)

**Can safely remain implementation detail:** Database engine; queue technology; integrity-chain algorithm; TTL defaults; retention periods; log formats; UI framework within a chosen delivery model; theme token naming; confidence heuristics; notification channels.

**Should be explicitly deferred:**
- Third-party and externally supplied Integrations
- Independent Integration upgrade channel
- Multiple active Integrations per System
- cPanel and DirectAdmin adapters (keep the boundary rules, defer the contract details)
- Delegated/non-superadmin authorization
- Recovery web UI (beyond read-only)
- Health history, audit export, version pinning
- Waiting/paused Job states beyond those required by CHANGE-007
- Multi-server management

The human architecture owner decides whether to accept or reject each change listed here. None of them has been applied.
