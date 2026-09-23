> **Document status:** FOUNDATIONAL / CURRENT WITH OVERRIDES
> **Authority category:** 3 — Current foundational principles (see [Authority Hierarchy](../README.md#authority-hierarchy))
> **Source:** The original SCC candidate architecture §1–§14, as submitted for the Forensic Architectural Audit (DEC-014 / D-1).
> **Override rule (D-1):** Earlier principle + later locked architecture = later locked architecture controls. Where any
> statement below conflicts with §15, §16 or §17, the locked section controls.
> **Unannotated statements** are CURRENT FOUNDATIONAL PRINCIPLES, subject to the override rule.
> **Annotations** ANN-01 … ANN-32 were approved by the owner (DEC-030, Q8, with ANN-25 amended).
>
> **How to read this document**
> - **Original text** appears only (a) inside fenced `text` blocks and (b) as the original `# §n` section heading lines.
>   It is reproduced verbatim and has not been edited.
> - **Annotations** appear only as blockquotes that begin with **ANN-nn** and say *"Annotation — not original text."*
> - **Transcription notes:** The original text was placed in fenced blocks so that line breaks and diagrams render
>   exactly and so that annotations are visibly separate from the original. The original `# §n` heading lines are kept
>   as Markdown headings for navigation. The original "STATUS DURING DESIGN / STATUS FOR THIS AUDIT" lines are retained;
>   they describe the status at the time of the audit, not the current status (which is stated above). The closing
>   "END CANDIDATE ARCHITECTURE" separator and the audit instructions that surrounded the original text are not included.

# §1 — PURPOSE, SCOPE & NON-GOALS

```text
STATUS DURING DESIGN: LOCKED
STATUS FOR THIS AUDIT: CANDIDATE / SUBJECT TO AUDIT

SCC is a free/open-source security platform for CyberPanel initially, designed to discover, assess, install, configure, monitor, and manage supported security components.
```

> **ANN-31 · CURRENT-REFINED** · *Annotation — not original text.*
> Installation, configuration and management remain in scope, but only through the locked execution and authorization
> architecture. For example, package-family WRITE capabilities are R4 and require approval (DEC-009).
> **Source:** §16; §17 (§17.5.3); DEC-009.

```text
Security is treated as a collection of independent Security Systems and capabilities, not as one product or one score.

Primary objectives:

- discover Security Systems
- assess their state
- identify gaps
- install supported systems
- configure supported systems
- monitor systems
- manage supported systems
- provide diagnostics
- provide auditability
- integrate naturally with hosting-control panels

Central principle:

" SCC observes first and acts only through explicitly declared capabilities. "

SCC is provider-neutral; the architectural term is Security Integration.

SCC must support external systems without automatically taking ownership of them.

There is no universal SCC security score.

Scope includes:

- discovery
- inventory
- health
- state
- compatibility
- Integration availability
- capabilities
- installation
- configuration
- monitoring
- diagnostics
- Jobs
- authorization
- auditability
- CyberPanel integration
- future hosting-panel adapters

Non-goals:

- SCC is not an antivirus product itself.
- SCC is not an Imunify360 replacement.
- SCC is not a replacement for CyberPanel.
- SCC is not a generic shell interface.
- SCC does not automatically "fix everything."
- SCC does not automatically install everything.
- SCC must not blindly modify hosting-panel core files.
- SCC must not assume ownership of externally installed systems.
- SCC must not expose sensitive information unnecessarily.

Doctrine:

"Discover what exists.
Understand what it does.
Report what is known.
Expose only explicitly supported actions.
Require authorization before changing anything.
Record what SCC changes."

============================================================
```

# §2 — SECURITY INTEGRATION MODEL

```text
A Security System is the actual thing present on the server.

A Security Integration is SCC's knowledge of and ability to safely interact with that system.

Examples:

- Firewalld
- Fail2Ban
- ModSecurity
- OWASP CRS
- ClamAV
- ImunifyAV
- CrowdSec

A Security System does NOT require an SCC Integration to appear in inventory.

Discovery is independent of Integration.

Generic discovery may detect known systems without corresponding Integrations, as well as unknown security-related services.

Integration identity includes:

- stable machine-readable ID
- name
- description
- version
- vendor/maintainer
- category
- documentation

Categories may include:

- firewall
- intrusion-prevention
- web-application-firewall
- malware-detection
- malware-scanning
- authentication
- access-control
- tls
- network-security
- system-hardening
- security-monitoring

The category model must remain extensible.

Integration state may include:

- installed
- version
- enabled
- running
- configured
- supported
```

> **ANN-01 · OPEN** · *Annotation — not original text.*
> This list mixes Security System state with Integration state. The Integration state vocabulary is not yet resolved.
> **Source:** Forensic audit MED-02 (CHANGE-019); see [`../open/register.md`](../open/register.md).

```text
Installation does not imply operation.

Health reports should include:

- overall state
- checks
- diagnostics
- timestamp

Evidence should support health conclusions where practical.

Capabilities are explicit.

Possible capabilities:

- discover
- inspect
- health
- install
- uninstall
- enable
- disable
- start
- stop
- restart
- configure
- update
- scan
- diagnostics

Not every Integration implements every capability.

Capability != permission.

Authorization is separate.

Ownership modes:

- owned
- external
- observation_only
```

> **ANN-02 · OPEN** · *Annotation — not original text.*
> `observation_only` appears both as an ownership mode (here and §5) and as a management state (§3, §5). The
> ownership × management model and its valid combinations are not yet resolved.
> **Source:** Forensic audit HIGH-01 (CHANGE-005); see [`../open/register.md`](../open/register.md).

```text
Operations must be structured and validated.

NO generic:

- execute(command)
- run(command)
- shell
- arbitrary root command

Integration compatibility should declare:

- supported platforms
- OS versions
- architectures
- CyberPanel versions
- dependencies
```

> **ANN-03 · SUPERSEDED (replacement OPEN)** · *Annotation — not original text.*
> SCC Core metadata must not name a specific platform. Platform knowledge belongs at the platform boundary
> (K2, Presentation Adapter, Platform Services). The replacement platform-compatibility field is not yet designed.
> **Source:** §15 T-27; DEC-016 (D-4); forensic audit HIGH-11.

```text
Integration version is distinct from underlying Security System version.

Integration isolation is mandatory.
```

> **ANN-04 · SUPERSEDED** · *Annotation — not original text.*
> Integration isolation is now defined by the K5 Integration Host boundary: per-Integration workers, launcher-bound
> identity, no host access, no network, no path to K6.
> **Source:** §15.8; §15 T-05, T-06, T-16.

```text
One Integration failure must not take down SCC.

Discovery must be safe/read-only.

Existing systems must be adopted without unnecessary reinstall/reset/alteration.

Unknown/unmapped systems must remain visible.

The Integration Registry is the list of SCC Integrations, NOT the inventory of installed Security Systems.

Core must remain free of product-specific commands, paths, and service details that belong inside Integrations.

Foundational doctrine:

"A Security System is something that exists on the server. A Security Integration is SCC's knowledge of and ability to interact with that system. Discovery determines what exists; Integrations determine what SCC understands and can safely do about it.

The absence of an Integration must never cause SCC to hide a Security System that it can otherwise detect."

============================================================
```

# §3 — DISCOVERY & STATE MODEL

```text
The Discovery Engine is a dedicated subsystem responsible for building the server's Security System inventory.

Discovery is read-only.

Discovery may inspect:

- package managers
- systemd
- processes
- binaries
- filesystem
- configuration
- service APIs
- sockets/listening state
- CyberPanel state
- Integration-specific detection
```

> **ANN-06 · CURRENT-REFINED** · *Annotation — not original text.*
> All host inspection occurs only through K6 READ Operations. Generic, product-neutral discovery belongs to K4 through
> the reserved Core Discovery Declaration. Product-specific detection belongs to K5.
> **Source:** §15 T-07; §16 X-36, X-39; DEC-019 (D-7).

```text
Discovery must not:

- install
- remove
- modify
- restart
- create
- change permissions
- alter configuration

No single discovery source is always authoritative.

Discovery is evidence-based.

Evidence should retain enough information to explain why SCC believes a system exists.

Example evidence:

- package
- service
- version
- executable
- configuration
- API response

Discovery confidence:

- confirmed
- probable
- possible
- unknown

Weak evidence must not be represented as certainty.

Security System identity must distinguish:

- system_id
- display_name
- detected_version
- integration_id

Unknown systems should receive stable unknown identities where possible.

State dimensions are independent:

- installed
- enabled
- running
- configured
- healthy
- supported

Unknown is valid.

Unknown must NOT become false.

State is not a score.

Integration state is separately recorded.

Management state may include:

- fully_managed
- partially_managed
- observation_only
- unmanaged
- unknown
```

> **ANN-02 (see §2) · OPEN** · *Annotation — not original text.*
> See ANN-02: the ownership × management model is not yet resolved.

```text
Discovery lifecycle:

Initial discovery
→ inventory
→ Integration inspection
→ health evaluation
→ current state
→ later reconciliation

Inventory must support reconciliation.

Important state changes may become events.

Discovery failures must NOT be represented as evidence that a Security System is absent.

One detection failure must not prevent other detection.

Existing-System Adoption:

When SCC is installed, it should:

- discover existing systems
- record current state
- associate compatible Integrations
- determine capabilities
- avoid unnecessary changes
- present inventory

Unknown systems remain visible.

DetectionEvidence conceptually:

- source
- type
- value
- confidence
- observed_at
- metadata

Sensitive evidence must be handled appropriately.

Conceptual SecuritySystem:

SecuritySystem
├── identity
├── display_name
├── category
├── version
├── detection
│   ├── detected
│   ├── confidence
│   └── evidence
├── state
│   ├── installed
│   ├── enabled
│   ├── running
│   ├── configured
│   ├── healthy
│   └── supported
├── integration
│   ├── available
│   ├── version
│   └── capabilities
├── management
└── timestamps
```

> **ANN-05 · OPEN** · *Annotation — not original text.*
> The conceptual model shows a single Integration per Security System. Cardinality (one system / several Integrations,
> one Integration / several systems) and arbitration are not yet resolved.
> **Source:** Forensic audit MED-05 (CHANGE-021).

```text
Foundational doctrine:

"Discovery determines what exists. Integration determines what SCC understands and can safely do about it.

Absence of Integration must never hide a detectable Security System.

Unknown is valid and must not be replaced by false certainty.

Discovery is read-only and safe to repeat.

Discovery failures must not be represented as evidence that a Security System is absent."

============================================================
```

# §4 — CAPABILITIES & ACTIONS

```text
A Capability describes an operation explicitly supported by an Integration.

Examples:

- inspect
- health
- install
- uninstall
- enable
- disable
- start
- stop
- restart
- configure
- update
- scan
- diagnostics

Capability != authorization.

Read, write, and destructive capabilities should be distinguishable.

An Action is an actual invocation of a Capability.

Actions must use structured, validated parameters.

No arbitrary string concatenation.

No generic shell/execute/run_as_root capability.

Actions may have:

- preconditions
- dependencies
- target validation
- risk classification
- confirmation requirements

Installation is explicit.

Existing systems must not be reinstalled merely because an Integration exists.

Configuration actions must be explicit.

No unrestricted configuration editor.

Service lifecycle operations must be risk-aware.

Long-running actions become Jobs.
```

> **ANN-07 · CURRENT-REFINED / OPEN** · *Annotation — not original text.*
> §17.5.2 defines the entity chain Capability → Action → Plan → Job → K6 Operation, with a Job being the execution of
> exactly one authorized Plan. The Job state model is not yet resolved.
> **Source:** §17.5.2, §17.11; forensic audit CHANGE-007; §16 Q-6.

```text
Actions must return structured results.

Dry-run may be supported.

Validation must occur before execution.

Sensitive actions should be revalidated before execution.

Concurrency/conflict handling is required.
```

> **ANN-08 · CURRENT-REFINED / OPEN** · *Annotation — not original text.*
> K6 enforces at most one WRITE in flight per resolved resource (X-22). Lock domains across Security Systems are not
> yet resolved.
> **Source:** §16 X-22; forensic audit CHANGE-009.

```text
Rollback should be supported where technically possible but never falsely promised.

High-risk actions require stronger confirmation/safety controls.

State-changing actions are audited.

External changes are expected.

SCC must reconcile them.

Foundational doctrine:

"Detection does not imply capability.

Capability does not imply authorization.

Authorization does not imply unrestricted execution.

Every state-changing action must be explicit, validated, authorized, and auditable.

SCC must never expose arbitrary command execution as a general capability.

Existing Security Systems must never be reinstalled merely because SCC has an Integration for them.

External changes to Security Systems must be expected and reconciled."

============================================================
```

# §5 — OWNERSHIP & MANAGEMENT MODEL

```text
Ownership is distinct from installation.

Ownership modes:

- owned
- external
- observation_only

Management states:

- fully_managed
- partially_managed
- observation_only
- unmanaged
- unknown
```

> **ANN-02 (see §2) · OPEN** · *Annotation — not original text.*
> See ANN-02: the ownership × management model is not yet resolved.

```text
Ownership does not grant permission.

Adoption must not reinstall/reset an existing system unnecessarily.

Adoption is explicit.
```

> **ANN-09 · OPEN** · *Annotation — not original text.*
> The meaning of "adoption" (automatic inventory association in §3 vs explicit ownership transition here), and whether
> successful installation implies ownership (§6, §8), are not yet resolved.
> **Source:** Forensic audit HIGH-02 (CHANGE-006).

```text
Partial management is supported.

External management must be detectable where possible.

Management conflicts must be handled safely.

CyberPanel may be an external management authority where appropriate.

Direct system management is only allowed where an Integration supports it.

Ownership transitions are explicit and auditable.

Releasing SCC ownership does not mean uninstalling.

Uninstall is separately authorized.

SCC must never force ownership.

Inventory must keep separate:

- ownership
- management
- Integration
- capabilities
- health

The UI must clearly show management boundaries.

Removing an Integration does not remove the underlying Security System.

Integration failure does not mean the Security System disappeared.

Management != health.

Foundational doctrine:

"Discovery does not establish ownership.

Integration availability does not establish ownership.

Technical ability to modify a system does not establish management authority.

Existing Security Systems must be adoptable without unnecessary reinstallation/reset.

Ownership, management, Integration, capability, and health are separate concepts.

SCC must never claim more management authority than it actually possesses.

Releasing SCC ownership does not imply uninstalling.

Removing an Integration never removes the underlying Security System.

External changes are expected and reconciled.

Uncertainty results in transparency and safe observation."

============================================================
```

# §6 — INSTALLATION MODEL

```text
Installation is a workflow, not an opaque action.

Required conceptual lifecycle:

Detection
→ Integration
→ Compatibility
→ Plan
→ Review/Authorization
→ Preparation
→ Install
→ Configuration
→ Verification
→ Adoption

Inspect before install.

Eligibility:

- supported
- unsupported
- unknown

Compatibility may include:

- OS
- architecture
- CyberPanel version
- OpenLiteSpeed version
- dependencies
- disk space
- privileges
- conflicts

Installation plans must identify meaningful changes.

No hidden installation steps.

Dependencies must be explicit.

Dependency authorization is separate.

Existing compatible systems should be adopted/used instead of reinstalled.

Conflicts must stop or pause the workflow.

Installation sources must be explicitly defined.

No arbitrary installation URLs.
```

> **ANN-11 · CURRENT-REFINED** · *Annotation — not original text.*
> Package sources are an allowlist in the K11 Global Execution Policy. Package Operations install only packages named in
> scope, with an exact version or artifact identity.
> **Source:** §16.2.2; §16.1.3.

```text
Package/artifact integrity must be verified.

Elevated privileges must be controlled.

Preparation and backups should occur where applicable.

Execution occurs through the Integration.
```

> **ANN-10 · SUPERSEDED** · *Annotation — not original text.*
> Execution occurs only in K6 under the §16 Privileged Execution Contract. Integrations run unprivileged in K5, propose
> Plans and operation requests to K4, and have no host access.
> **Source:** §15.8; §16; §15 T-05, T-07.

```text
Long-running installation uses Jobs.

Post-install verification is mandatory.

Partial success/failure must be transparent.

Rollback/recovery should exist where practical.

Interrupted installation must be reconciled.

Installation should be idempotent where practical.

Ownership is established only after successful verification.
```

> **ANN-09 (see §5) · OPEN** · *Annotation — not original text.*
> See ANN-09: whether successful installation implies ownership is not yet resolved.

```text
Installed != configured != enabled != healthy.

Installation lifecycle must be audited.

Foundational doctrine:

"Installation is controlled workflow, not opaque action.

SCC inspects first, plans explicitly, obtains authorization, executes only through explicit Integration, verifies, and handles failure transparently.

Existing compatible systems should be adopted/used rather than unnecessarily reinstalled.

Dependencies are explicit and authorized.

Installation only occurs through an Integration.

Successful package installation is not sufficient proof of success.

Failed/interrupted installations must be recoverable or transparently partial.

SCC never silently assumes ownership."

============================================================
```

# §7 — HEALTH & ASSESSMENT MODEL

```text
Health describes the operational condition of a specific Security System.

Health is separate from:

- state
- configuration
- management
- ownership
- coverage

Health states:

- healthy
- degraded
- unhealthy
- unknown

Unknown is valid.

Integrations define health checks and health derivation.

Health checks should include:

- id
- name
- status
- severity
- evidence
- message
- observed_at
- remediation/recommendation information where applicable

HealthReport:

- overall
- checks[]
- diagnostics
- recommendations[]
- observed_at

Checks may be:

- required
- important
- informational

Health evidence must be explainable and freshness-aware.

Stale data may become unknown as appropriate.

Discovery failure != health failure.

Dependency health must be distinguishable.

Recommendations are not actions.

No automatic remediation by default.

Severity may include:

- info
- warning
- error
- critical

Coverage is not health.

Health history should be supported.

Health transitions may become events.

Health checks are read-only, bounded, and isolated.
```

> **ANN-32 · CURRENT-REFINED** · *Annotation — not original text.*
> Health checks read host facts only through K6 READ Operations.
> **Source:** §15 T-07.

```text
Errors must be distinguishable from health failures.

Health must be explainable.

Without an Integration, only generic health facts may be available.

Specialized Integrations may provide deeper health checks.

Foundational doctrine:

"Health describes the operational condition of a specific Security System.

Health must be evidence-based and explainable.

Unknown is valid.

Health, configuration, management, ownership, and coverage remain separate.

Health checks are read-only and bounded.

Health failure does not automatically trigger remediation.

Recommendations are not actions.

Freshness is required.

Dependency failures must be distinguishable.

One failed check must not prevent others.

There is no verdict without sufficient explanation."

============================================================
```

# §8 — JOBS & ASYNCHRONOUS OPERATIONS

```text
Long-running/state-changing operations should use:

Capability
→ Action
→ Job
→ Execution
→ Result

Jobs require:

- identity
- correlation
- state
- progress
- stages
- messages
- logs
- structured output

Job states:

- queued
- running
- completed
- failed
- cancel_requested
- cancelled
```

> **ANN-12 · OPEN** · *Annotation — not original text.*
> The Job state model is not yet resolved. The locked architecture requires outcomes such as UNKNOWN and PARTIAL
> (§16.6.2, §16.12) that this state list cannot represent.
> **Source:** Forensic audit CHANGE-007; §16 Q-6; §16.12.

```text
Waiting/paused may be added later.

Cancellation request does not guarantee immediate cancellation.

Authorization must occur before privileged Job creation.

Sensitive operations must revalidate authorization before execution.
```

> **ANN-13 · CURRENT-REFINED** · *Annotation — not original text.*
> Refined by Plan Authorization, Job start conditions, and revalidation at Job start and before every WRITE K6 request.
> **Source:** §17.11, §17.12, §17.13; A-27, A-28.

```text
Jobs must be isolated.

No generic Job command execution.

Concurrency and conflicting Jobs must be controlled.

Locks may be required.

Duplicate/idempotency behavior must be defined.

Retries must be explicit, bounded, and Integration-aware.

Interrupted or uncertain execution must not be falsely reported as failed/successful without evidence.

Recovery begins with reconciliation.

Completion requires verification.

Audit correlation must exist.

Job logs and Audit records are distinct.

Sensitive Job data must be protected.

Job retention and cleanup must be defined.

Job visibility requires authorization.

Notifications are separate from Jobs.

Discovery/health reconciliation should follow significant actions.

Ownership changes occur only after verified installation/adoption.

Foundational doctrine:

"Long-running/state-changing operations are represented as Jobs where appropriate.

A Job executes an authorized Action, not an arbitrary command.

Authorization occurs before privileged Job creation.

Sensitive Jobs revalidate authorization.

Jobs are isolated.

Cancellation is not a guarantee.

Retries are bounded.

Interrupted/uncertain execution is not falsely reported.

Completion requires verification.

Significant operations trigger reconciliation.

Logs and Audit are distinct.

The Job system must never become a disguised shell executor."

============================================================
```

# §9 — SECURITY, AUTHORIZATION & PRIVILEGE MODEL

```text
Security lifecycle:

Identity
→ Authentication
→ Authorization
→ Capability
→ Action
→ Job
→ Privileged Execution

Authentication and Authorization are separate.

Where CyberPanel provides identity, SCC should use that identity rather than unnecessarily creating a second administrator identity.
```

> **ANN-14 · CURRENT-REFINED** · *Annotation — not original text.*
> Platform identity establishes who a user is, never what they may do. HUMAN Principals require explicit enrollment.
> In v1, `PLATFORM_ADMIN` is required, as a restriction only.
> **Source:** §17.1.5; A-03, A-04; DEC-010, DEC-011, DEC-018 (D-6).

```text
SCC retains capability-level authorization.

No authentication bypass.

Authorization must be capability-aware.

Read and write permissions must be distinct.

High-risk operations require stronger controls.

Capability != permission.

Authorization is enforced server-side.

UI visibility is not authorization.

Least privilege is mandatory.

The web application must not have unrestricted root access.

Privileged work should be isolated through a controlled worker/mechanism.
```

> **ANN-15 · SUPERSEDED** · *Annotation — not original text.*
> Privileged work is isolated in K6, the Privileged Executor, under the §16 Privileged Execution Contract.
> **Source:** §15.9; §16.

```text
No root shell.

Privileged capabilities must be explicit.

Target and parameter validation is required.

Sensitive operations include:

- SSH
- firewall
- TLS
- administrator accounts
- other high-impact controls

Secrets and credentials must be minimized and redacted.

Credential scope must be limited.

Failed authentication must be handled safely.

Privilege escalation must be prevented.

Integration trust boundaries must exist.

Emergency/recovery operations must not create hidden backdoors.
```

> **ANN-16 · CURRENT-REFINED / mechanism OPEN** · *Annotation — not original text.*
> Recovery authority is host-local (K9). No web-reachable path may bypass authorization or audit. The recovery
> mechanism is not yet designed.
> **Source:** §15 T-29; A-07; DEC-021 (D-9); recovery gate.

```text
State-changing operations fail closed if authorization is uncertain.

Authorization decisions are audited.

Foundational doctrine:

"Authentication establishes identity; authorization establishes permission.

Capability availability never implies user authorization.

Authorization is enforced server-side.

Privileged execution is isolated.

There is no unrestricted root shell.

High-risk actions receive stronger controls.

Confirmation is not authorization.

Uncertain authorization results in denial of state-changing operations.

Secrets are protected and redacted.

Integration access is limited to declared capabilities.

Emergency recovery never creates an undocumented authorization bypass."

============================================================
```

# §10 — AUDIT & ACCOUNTABILITY MODEL

```text
Audit records what SCC knows happened.

Audit is distinct from:

- application logs
- Job logs
- current state
- history views

Structured AuditEvent should contain as appropriate:

- event_id
- type
- timestamp
- actor
- source
- Security System
- Integration
- capability
- action
- Job
- result
- evidence
- metadata

Events may include:

- SYSTEM_DETECTED
- SYSTEM_STATE_CHANGED
- HEALTH_CHANGED
- ACTION_REQUESTED
- ACTION_AUTHORIZED
- ACTION_DENIED
- JOB_CREATED
- JOB_STARTED
- JOB_COMPLETED
- JOB_FAILED
- CONFIGURATION_CHANGED
- INSTALLATION_STARTED
- INSTALLATION_COMPLETED
- INSTALLATION_FAILED
- OWNERSHIP_CHANGED
- INTEGRATION_CHANGED

Request, authorization, execution, and result must remain distinct.

Actor != executor.

Before/after state is recorded only when observed.

External changes are not attributed to SCC without evidence.

Failed authentication is audited.

Installation/configuration/ownership/Integration changes are audited.

Audit should be append-only and integrity-protected.
```

> **ANN-17 · CURRENT principle / mechanism OPEN (scope qualified)** · *Annotation — not original text.*
> The audit mechanism is not yet designed (§21). The conditional §18 gate review notes that tamper evidence produced by
> a record's own writer does not protect against that writer; this qualification is conditional material, not locked.
> **Source:** §21 (not designed); §18 gate review CLF-18-07 (conditional).

```text
Sensitive information must be minimized.

Audit access is authorized.

Audit should support export.

Audit noise must be controlled.

Unknown outcomes remain unknown until evidence establishes the result.

Causality must not be invented.

Audit failure cannot silently be represented as success.

Foundational doctrine:

"SCC records what it knows happened—not what it assumes.

Audit is distinct from logs and Jobs.

State-changing operations are traceable through actor → action → Job → execution → result.

Requests, authorization, execution, and outcomes remain distinct.

Before/after values are recorded only when observed.

External changes are not attributed without evidence.

Unknown stays unknown.

Security audit is append-only/protected.

Sensitive data is minimized.

Audit access is authorized.

Audit failure is not silently treated as success.

Meaningful events are prioritized."

============================================================
```

# §11 — CYBERPANEL INTEGRATION & PLATFORM BOUNDARY

```text
SCC integrates with CyberPanel but does not become CyberPanel core.

CyberPanel is the hosting platform.

SCC is the security management/observability layer.

SCC is not a replacement for CyberPanel core functionality.

Integration may use:

- authentication/session
- navigation
- plugin registration
- supported APIs
- internal interfaces where necessary
- security subsystems
```

> **ANN-18 · CURRENT-REFINED** · *Annotation — not original text.*
> Parent-platform authentication, session, navigation and registration are used only by K2 within its limited role.
> K2 consumes the platform session and produces the SCC identity assertion. It does not authenticate users, authorize,
> or execute, and it talks only to K3 through P2.
> **Source:** §15.6; DEC-018 (D-6); DEC-026 (D-14).

```text
CyberPanel authentication may establish identity, but SCC retains capability-level authorization.

SCC should integrate naturally into CyberPanel.

Avoid modifying CyberPanel core files wherever possible, including:

- settings.py
- urls.py
- base templates
- core views
- arbitrary core assets

Upgrade survival is a major architectural requirement.

CyberPanel compatibility states:

- supported
- unsupported
- partially_supported
- unknown

SCC must degrade gracefully.

CyberPanel failure must not take down unrelated SCC functionality.

Direct OS access is permitted only for explicit Security Integrations.
```

> **ANN-19 · SUPERSEDED** · *Annotation — not original text.*
> Only K6 performs host operations. Integrations have no direct OS access.
> **Source:** §15 T-02, T-06, T-07.

```text
Prefer the narrowest supported interface.

CyberPanel-owned security systems should be treated as externally managed where appropriate.

API/internal API adapters should be isolated.

Undocumented internal APIs are higher risk.

SCC owns its own data:

- inventory
- Integration registry
- health history
- Jobs
- audit
- authorization metadata
- SCC configuration
```

> **ANN-20 · CURRENT / design OPEN** · *Annotation — not original text.*
> K7 is SCC-owned and accessible only to identity C. The persistence design is not yet designed (§19).
> **Source:** §15 T-23; DEC-024 (D-12).

```text
SCC should avoid duplicating CyberPanel-owned data unnecessarily.

Direct core configuration edits are exceptional and must be:

- guarded
- backed up
- authorized
- audited
- recoverable where possible

Removing SCC must not remove Security Systems.

CyberPanel upgrade detection and compatibility assessment are required.

CyberPanel-specific knowledge must remain behind the platform boundary.

CyberPanel itself is not automatically a Security System simply because SCC integrates with it.

Other direct hosting-panel platforms are explicitly part of the architectural model:

- CyberPanel
- cPanel
- DirectAdmin

Potential architecture:

SCC Core
├── CyberPanel Platform Adapter
├── cPanel Platform Adapter
└── DirectAdmin Platform Adapter

These are future platform capabilities, not claims of current implementation/support.
```

> **ANN-21 · SUPERSEDED (structure) / HISTORICAL (platform list)** · *Annotation — not original text.*
> The single "Platform Adapter" is split into K2 Platform Bridge, Presentation Adapter and Platform Services (§15.3).
> Platforms are implemented one at a time, and future platforms are not designed speculatively.
> **Source:** §15.3; DEC-016 (D-4).

```text
Foundational doctrine:

"SCC integrates with CyberPanel; it does not become CyberPanel core.

CyberPanel authentication may establish identity, while SCC retains capability-level authorization.

Supported interfaces are preferred.

CyberPanel-specific details remain isolated behind the platform boundary.

Core modifications should be avoided.

Upgrade compatibility must be explicit and evidence-based.

Integration failure does not take down independent SCC functionality.

Direct OS interaction occurs only through explicit Integrations.

SCC does not compete with CyberPanel's management authority.

SCC owns its own data.

Removing SCC does not remove Security Systems.

CyberPanel-specific knowledge remains at the platform boundary."

============================================================
```

# §12 — UPGRADE, COMPATIBILITY & RECOVERY MODEL

```text
SCC, Integrations, Platform Adapters, Security Systems, CyberPanel, and the OS have independent version identities.

Version domains include:

- SCC version
- Integration version
- Platform Adapter version
- Security System version
- CyberPanel version
- OS version

These are not interchangeable.

Example:

SCC:
1.4.0

CyberPanel:
3.0 build 7

ModSecurity:
3.0.15

OWASP CRS:
3.3.2

Integration version is distinct from Security System version.

Platform Adapter version is distinct from CyberPanel version.

Compatibility must be explicit where practical.

Compatibility states:

- supported
- unsupported
- partially_supported
- unknown

Compatibility != health.

SCC upgrades should primarily modify SCC itself.

SCC must not automatically upgrade underlying Security Systems.

Upgrade preflight may inspect:

- current version
- target version
- CyberPanel compatibility
- OS compatibility
- database/schema compatibility
- installed Integrations
- active Jobs
- disk space
- dependencies
- configuration compatibility
- backup availability

Active Jobs must be accounted for before upgrades.

Upgrade locking should prevent incompatible simultaneous administrative operations.

Backups should be made where SCC data/configuration may be modified.

Audit history must survive upgrades.

Schema migrations must be:

- versioned
- deterministic
- recoverable where practical
- idempotent where practical

Migration failure must not be reported as success.

Configuration must be preserved unless explicitly migrated.

Integration upgrades must not silently uninstall/disable Systems.

Security Systems remain visible even if an updated Integration becomes unsupported.

Graceful degradation is required.

Integration upgrades may occur independently where practical.
```

> **ANN-23 · OPEN** · *Annotation — not original text.*
> Whether Integrations may be upgraded independently of SCC releases is not yet resolved (lifecycle).
> **Source:** §22 (not designed); forensic audit CHANGE-026.

```text
CyberPanel upgrades are external changes.

OS upgrades are external changes.

Security System upgrades are external changes unless SCC explicitly initiated them.

External changes must not be falsely attributed to SCC.

Recovery mode is required for situations such as:

- failed migration
- incompatible SCC version
- corrupt configuration
- broken Platform Adapter
- failed startup validation
```

> **ANN-22 · SUPERSEDED (as a web UI) / recovery OPEN** · *Annotation — not original text.*
> Recovery authority is host-local through K9. There is no web recovery path. Recovery mechanics are not yet designed.
> **Source:** §15 T-29; A-07; DEC-021 (D-9).

```text
Recovery mode prioritizes:

- diagnostics
- inspection
- backup restoration
- migration recovery
- safe rollback
- administrative repair

Recovery mode must NOT be a backdoor.
```

> **ANN-16 (see §9) · CURRENT-REFINED / mechanism OPEN** · *Annotation — not original text.*
> See ANN-16: recovery authority is host-local (K9); the recovery mechanism is not yet designed.

```text
Startup validation should verify:

- database
- schema
- configuration
- platform compatibility
- Integrations
- Job system
- audit system

Partial startup/degraded mode should be possible where safe.

High-risk functionality may be blocked if required safeguards are unavailable.

Rollback should exist where technically possible.

SCC must never falsely claim universal rollback.

Upgrade plans should identify:

- rollback_supported
- rollback_limited
- rollback_unavailable

Interrupted upgrades must be detected and reconciled.

Version pinning may be supported where necessary.

Compatibility warnings should explain why something is unsupported/unknown.

Upgrade authorization follows the same authorization architecture.

Upgrade events are audited.

Recovery events are audited.

Foundational doctrine:

"SCC, Integrations, Platform Adapters, Security Systems, CyberPanel, and the OS have independent version identities.

An SCC upgrade must not automatically modify underlying Security Systems.

Compatibility must be explicit, version-aware, and evidence-based.

Unsupported or unknown compatibility must not be silently treated as supported.

Existing Security Systems remain visible even when an updated Integration can no longer manage them.

Upgrades preserve SCC configuration, inventory, ownership, and audit history.

Migrations are versioned, deterministic, and recoverable where practical.

Interrupted upgrades must be detected rather than blindly repeated.

Rollback is never claimed where technically unsupported.

CyberPanel and OS upgrades are external changes SCC must detect and reconcile.

Upgrade/recovery operations remain authenticated, authorized, and auditable.

Recovery mode is never an authorization bypass.

One failed component must not unnecessarily take down unrelated SCC functionality."

============================================================
```

# §13 — UI / COMMAND CENTER ARCHITECTURE

```text
The Command Center is the primary administrative interface.

It is an observability and controlled-action interface, not merely a collection of product links.

The UI must never imply that SCC knows/manages/controls more than the backend architecture establishes.

Core distinctions:

Detected != Integrated
Integrated != Managed
Managed != Healthy
Healthy != Secure
Compatible != Installed
Installed != Enabled
Enabled != Running
Capability != Authorization

The Command Center should answer:

"What is happening with security on this server right now?"

Primary overview should include:

- Security Systems
- health
- compatibility
- management
- attention required
- active Jobs
- recent events

No universal security score.

Security System cards should expose independently:

Primary:
- identity
- operational state
- health
- attention

Secondary:
- version
- compatibility
- Integration
- management

Detail:
- evidence
- checks
- capabilities
- configuration
- audit
- diagnostics

State dimensions remain independent.

Unknown is a first-class visual state.

Discovery confidence should distinguish:

- confirmed
- probable
- possible
- unknown

Integration state must be visible.

Management boundary must be visible.

Ownership must be separately visible.

Compatibility is first-class.

Attention Required is a separate concept from:

- health
- severity
- score

Dashboard summaries may show counts, such as:

Security Systems:
12 detected

Health:
9 healthy
2 degraded
1 unknown

Compatibility:
10 supported
1 partial
1 unknown

Management:
6 fully managed
3 partially managed
2 external
1 observation only

Attention:
4 items

These are counts, not rankings/scores.

No artificial overall server-security status.

Filtering/grouping may use:

- category
- health
- installation state
- enabled state
- running state
- compatibility
- Integration availability
- management
- ownership
- attention
- confidence

System detail views may include:

- overview
- health
- compatibility
- capabilities
- configuration
- diagnostics
- evidence
- Jobs
- history
- audit

Health view exposes HealthReport.

Compatibility view explains the determination.

Capabilities view shows actual Integration capabilities.

Authorization-aware actions distinguish capability availability from permission.

Actions should be grouped by risk.

No generic "Run Command" UI.

Action confirmation should explain:

- what happens
- affected system
- reason
- expected impact
- rollback availability

Jobs get their own interface.

Failed Jobs explain:

- what was attempted
- what failed
- what changed
- what did not change
- current known state
- recovery availability

Recovery has a controlled UI.
```

> **ANN-22 (see §12) · SUPERSEDED (as a web UI) / recovery OPEN** · *Annotation — not original text.*
> See ANN-22: recovery authority is host-local through K9; there is no web recovery path.

```text
Audit has its own interface.

Current State, History, Audit, and Logs remain distinct.

Event timelines must not invent causality.

Discovery evidence should be inspectable by authorized users.

Freshness/staleness must be visible.

External reconciliation must be visible.

Notifications should link to underlying evidence.

UI is never authoritative for authorization.

UI failures must be isolated.

Integration errors must not automatically become Security System failures.

Unknown systems remain visible.

Installation recommendations are informational until explicitly authorized.

Opening the Command Center is read-only with respect to the server.

Actions follow:

UI
→ Capability
→ Authorization
→ Action
→ Job
→ Execution
→ Verification
→ Reconciliation
→ Audit

Navigation may include:

Overview
Security Systems
Attention
Jobs
Audit
Diagnostics
Integrations
Settings

The Integration Registry is separate from the Security System inventory.

Platform information should be visible:

- hosting panel
- version
- build
- OS
- architecture
- web server
- SCC version

Diagnostics must not become an unrestricted shell.

Sensitive information must be minimized.

Accessibility requirements include:

- clear state labels
- readable indicators
- non-color-only communication
- keyboard accessibility
- understandable errors
- explicit action consequences

Responsive design should support desktop/laptop/tablet.

------------------------------------------------------------
```

# §13.55 — PARENT PLATFORM THEME & NATIVE UI INTEGRATION

> **ANN-24 · HISTORICAL (as a universal model) / per-platform OPEN** · *Annotation — not original text.*
> This annotation applies to §13.55 and all of its subsections (§13.55.2 – §13.55.10). A universal Parent Theme /
> Presentation model shared by all platforms is not current architecture. Each platform's K2 gate determines its own
> conforming presentation arrangement. For CyberPanel, the placement question is OPEN (D-15).
> **Source:** DEC-015 (D-3), DEC-016 (D-4), DEC-027 (D-15).

```text
------------------------------------------------------------

This is an explicit architectural requirement.

SCC must inherit and respect the visual language of the hosting-control-panel platform into which it is integrated.

SCC must NOT impose one universal SCC theme on every platform.

Initial target platforms:

- CyberPanel
- cPanel
- DirectAdmin
- future hosting-panel platforms

Conceptually:

SCC Command Center
    │
    ├── CyberPanel Adapter
    │      └── CyberPanel Parent Theme
    │
    ├── cPanel Adapter
    │      └── cPanel Parent Theme
    │
    └── DirectAdmin Adapter
           └── DirectAdmin Parent Theme

The same SCC functionality should present naturally within each supported platform.

Native appearance should respect, where available:

- typography
- colors
- spacing
- component shapes
- navigation conventions
- buttons
- forms
- tables
- cards
- alerts
- icons
- menus
- responsive behavior
- light/dark mode
- accessibility conventions

SCC branding may remain identifiable but must not visually fight the parent platform.

------------------------------------------------------------
```

# §13.55.2 — NO DESIGN HACKING

```text
------------------------------------------------------------

SCC must NOT achieve visual integration through arbitrary modification or overriding of parent-panel core design.

It should not require:

- modifying core panel templates
- arbitrary global CSS injection
- replacing parent stylesheets
- rewriting parent components
- patching minified assets
- copying large portions of parent styles
- hard-coded selectors against unrelated parent UI
- DOM manipulation intended to force compatibility

Doctrine:

"Integrate with the platform's presentation architecture, not hack around it."
```

> **ANN-25 · OPEN — CyberPanel K2 gate** · *Annotation — not original text.*
> T-24 (SCC's installation and normal operation must not require modification of parent-platform core files) is **not**
> resolved for CyberPanel. The CyberPanel installation and registration mechanism is deferred to the CyberPanel K2 gate.
> **Source:** §15 T-24; DEC-017 (D-5); DEC-027 (D-15); DEC-030 (Q8 amendment); architecture index KF-03.

```text
------------------------------------------------------------
```

# §13.55.3 — PARENT THEME CONTRACT

```text
------------------------------------------------------------

Platform adapters should expose a Parent Theme Contract to the presentation layer.

Conceptually:

Parent Theme
├── colors
├── typography
├── spacing
├── surfaces
├── borders
├── controls
├── navigation
├── icons
├── status semantics
├── responsive rules
├── accessibility rules
└── theme capabilities

Exact implementation is platform-specific.

If a platform exposes:

- native theme APIs
- design tokens
- component libraries
- supported extension mechanisms

SCC should use those mechanisms.

------------------------------------------------------------
```

# §13.55.4 — THEME CAPABILITY DISCOVERY

```text
------------------------------------------------------------

SCC should determine what presentation capabilities the parent platform actually exposes.

Examples:

Theme API:
Available

Design Tokens:
Available

Dark Mode:
Supported

Native Components:
Available

If the platform does not expose a capability, SCC should gracefully fall back to its own compatibility layer rather than using unsupported modifications.

------------------------------------------------------------
```

# §13.55.5 — PLATFORM-SPECIFIC PRESENTATION ADAPTERS

```text
------------------------------------------------------------

Platform-specific presentation logic belongs in the Platform Adapter, not throughout SCC Core.

Conceptually:

SCC Core
    │
    └── Presentation Contract
             │
             ├── CyberPanel Presentation Adapter
             ├── cPanel Presentation Adapter
             └── DirectAdmin Presentation Adapter

SCC Core defines WHAT needs to be presented.

The Platform Adapter determines HOW it naturally belongs inside the parent platform.

------------------------------------------------------------
```

# §13.55.6 — FUNCTIONAL INDEPENDENCE

```text
------------------------------------------------------------

Theme integration must not change SCC security semantics.

Switching from CyberPanel to cPanel must not change:

- Security System definitions
- Integration capabilities
- health semantics
- authorization
- audit
- Jobs
- ownership
- compatibility

Only the appropriate platform integration/presentation changes.

------------------------------------------------------------
```

# §13.55.7 — PARENT THEME FAILURE

```text
------------------------------------------------------------

If native theme integration cannot load:

Parent Theme:
Unavailable

SCC:
Functional

Presentation:
Compatibility/default theme

Theme failure must not disable:

- discovery
- health
- audit
- security management

But SCC should clearly identify that native visual integration is unavailable.

------------------------------------------------------------
```

# §13.55.8 — THEME VERSION COMPATIBILITY

```text
------------------------------------------------------------

Theme compatibility must be treated similarly to platform compatibility.

Example:

Parent Platform:
CyberPanel 3.0 build 7

Parent Theme:
Compatible

SCC Presentation Adapter:
Compatible

Result:
Native Presentation

If a panel update changes the design system:

Parent Platform:
Updated

Theme Compatibility:
Unknown

Result:
Compatibility assessment required

SCC must not blindly assume an older presentation adapter remains compatible.

------------------------------------------------------------
```

# §13.55.9 — THEME IS NOT BRANDING

```text
------------------------------------------------------------

Parent Theme =
how SCC visually belongs to the host platform.

SCC Branding =
how SCC identifies itself.

SCC may retain identity without forcing every platform to look SCC-branded.

------------------------------------------------------------
```

# §13.55.10 — SEAMLESS INTEGRATION DOCTRINE

```text
------------------------------------------------------------

"SCC should look like it belongs wherever it is installed.

The parent control panel determines the surrounding visual language.

SCC adapts to the parent platform rather than forcing the parent platform to adapt to SCC.

Native platform extension mechanisms are preferred over core modifications or visual hacks.

Platform-specific presentation logic belongs behind the Platform Adapter boundary.

Failure of theme integration must not compromise SCC's underlying security functionality."

------------------------------------------------------------

Additional UI doctrine:

"Show what exists.

Show what SCC knows.

Show what SCC can do.

Show what SCC is authorized to do.

Show what is happening.

Show what happened.

Never imply more certainty, authority, or control than SCC actually possesses."

Foundational UI rules:

- Command Center is observability + controlled action, not a score.
- Security Systems remain visible regardless of Integration availability.
- Detected/integrated/managed/healthy/compatible/authorized remain separate.
- Unknown is first-class.
- Evidence and explanations should be exposed where practical.
- Capabilities come from Integration capability model.
- No arbitrary command execution.
- Authorization is server-side.
- State-changing actions follow the full lifecycle.
- One failed system/integration must not break unrelated systems.
- External changes must be distinguishable from SCC actions.
- Ownership and management boundaries must be visible.
- Compatibility is first-class.
- Health/compatibility/management/ownership/attention/confidence must not collapse into one status.
- Viewing the Command Center is read-only.
- Parent theme must be inherited through supported mechanisms.
- Platform presentation logic belongs behind platform adapters.
- Theme integration failure must not compromise SCC.

============================================================
```

# §14 — INTEGRATION REGISTRY & FIRST INTEGRATIONS

```text
============================================================

The Integration Registry defines how SCC knows which Security Integrations are available.

It is distinct from Security System Inventory.

Security System Inventory =
what actually exists on the server.

Integration Registry =
what SCC knows how to understand/interact with.

The Registry is authoritative for available SCC Integrations.

Each Integration has a stable machine-readable identity:

- integration_id
- name
- description
- version
- category
- vendor/maintainer
- documentation

Integration metadata may declare:

- supported Security Systems
- supported OS versions
- supported architectures
- supported CyberPanel versions
- supported hosting panels
- dependencies
- capabilities
- compatibility requirements
- configuration requirements
- documentation
```

> **ANN-29 · SUPERSEDED (replacement OPEN)** · *Annotation — not original text.*
> SCC Core metadata must not name specific platforms. Platform knowledge belongs at the platform boundary. The
> replacement platform-compatibility field is not yet designed.
> **Source:** §15 T-27; DEC-016 (D-4).

```text
Integration lifecycle may conceptually include:

available
→ validated
→ enabled
→ disabled
→ removed

Integration availability states may include:

- available
- unavailable
- disabled
- incompatible
- invalid
- error

These describe the Integration itself, not the Security System.

Before management operations, Integrations should validate:

- metadata
- version
- capabilities
- compatibility
- dependencies
- required interfaces
- security constraints

Invalid Integrations must not silently become executable.

Integration Registry is NOT inherently a marketplace.

Integrations may be:

- built-in
- installed
- locally developed
- externally supplied
```

> **ANN-26 · SUPERSEDED (for v1)** · *Annotation — not original text.*
> v1 provides no load path for non-built-in Integration code. Integrations are built-in and shipped in K11.
> **Source:** §15 T-22; §15.4 item 7.

```text
But Integration installation follows §6 integrity/security requirements.

Integrations cross a security boundary and require trust metadata where appropriate:

- source
- version
- integrity
- signature/verification
- maintainer
- permissions/capabilities
```

> **ANN-27 · CURRENT-REFINED** · *Annotation — not original text.*
> Execution Declarations in K11 are signed and validated by K6; a declaration that fails validation is excluded on its
> own without affecting other declarations.
> **Source:** §16.2; X-08.

```text
No arbitrary Integration code may simply declare itself and receive unrestricted access.

Capabilities must be explicitly declared.

Declared capabilities must correspond to actual implementation.

Compatibility should be declared where possible but verified at runtime where necessary.

Integration detection may supplement Discovery but never replace generic Discovery.
```

> **ANN-28 · CURRENT-REFINED** · *Annotation — not original text.*
> Generic discovery belongs to K4 through the reserved Core Discovery Declaration. Integration detection is
> product-specific and belongs to K5.
> **Source:** §15.7; §16 X-36; DEC-019 (D-7).

```text
Integration matching must be evidence-based.

Multiple Integrations for one Security System may be supported where appropriate.
```

> **ANN-30 · OPEN** · *Annotation — not original text.*
> Multiple Integrations per Security System (cardinality and arbitration) is not yet resolved.
> **Source:** Forensic audit MED-05; CHANGE-021, CHANGE-026.

```text
Observation-only Integrations are valid.

Integration-specific configuration belongs within the Integration boundary.

Dependencies are explicit.

Dependency installation is separately authorized.

Documentation must explain:

- scope
- detection
- capabilities
- compatibility
- limitations
- risks
- dependencies

First Integration candidates:

- Firewalld
- Fail2Ban
- ModSecurity
- OWASP CRS
- ClamAV
- ImunifyAV
- SSH Security
- TLS/SSL

The first set should exercise different architectural patterns rather than simply maximize product count.

Firewalld should demonstrate:

- service discovery
- configuration inspection
- health
- enable/disable
- reload
- structured configuration
- privileged operations

No arbitrary firewall commands.

Fail2Ban should demonstrate:

- service state
- jail discovery
- ban status
- health
- configuration inspection
- controlled service management

Fail2Ban service state must be distinguishable from individual jail state.

ModSecurity should demonstrate complex integration involving:

- OpenLiteSpeed
- hosting-panel integration
- module state
- rules
- audit logs
- WAF health
- CRS

OWASP CRS should remain conceptually distinct from ModSecurity.

ClamAV should demonstrate malware scanning and Job-based long-running operations.

ImunifyAV should recognize existing installations rather than installing a duplicate scanner.

SSH Security should be carefully scoped around:

- OpenSSH
- SSH configuration
- authentication configuration
- authorized-key policy
- hardening state

It must not expose unrestricted SSH configuration editing.

TLS/SSL should distinguish:

- certificate
- TLS configuration
- web server
- mail service
- hostname certificate

First Integrations collectively should exercise:

- read-only observation
- health
- configuration inspection
- service management
- firewall management
- long-running scans
- dependencies
- compatibility differences
- external ownership
- partial management
- platform-specific behavior

Every Integration follows a common conceptual contract:

Identity
Metadata
Detection
Compatibility
Capabilities
Health Checks
Operations
Validation
Verification
Diagnostics
Documentation

Integration-specific knowledge belongs inside the Integration.

SCC Core remains product-neutral.

Core concepts include:

- SecuritySystem
- Integration
- Capability
- Action
- Job
- HealthReport
- DetectionEvidence
- Compatibility
- Ownership
- Management
- AuditEvent

Core must NOT contain product-specific conditionals such as:

if product == "fail2ban"

or hard-coded product paths/service names.

Platform-specific knowledge belongs behind Platform Adapters.

Integration tests should cover:

- detection
- non-detection
- version detection
- compatibility
- health
- capability declaration
- authorization boundaries
- action validation
- execution
- verification
- failure
- external changes

Testing should support safe modes such as:

- mock
- fixture
- read-only
- isolated
- integration

Integration failure must not hide the underlying Security System.

Removing an Integration must not remove the Security System.

Updating an Integration must not automatically update the Security System.

Integrations must operate with least privilege.

Integration secrets must be protected.

Integration observability must distinguish:

- loaded
- validated
- compatible
- healthy
- degraded
- error
- unavailable

Integration health asks:

"Can SCC currently perform the functions this Integration claims to provide?"

Security System health asks:

"Is the underlying Security System operating correctly?"

These remain separate.

Registry integrity must be protected.

Registry changes must be audited.

On startup/upgrade:

Load Registry
→ Validate Integrations
→ Evaluate Compatibility
→ Register Capabilities
→ Discover Security Systems
→ Associate Integrations

Invalid Integrations must not prevent valid Integrations from loading.

Foundational doctrine:

"The Integration Registry describes what SCC knows how to work with; it is not an inventory of what exists on the server.

Every Integration has a stable identity independent of its version.

Integrations explicitly declare capabilities.

Declared capabilities do not imply authorization.

Integration compatibility must be declared where possible and verified at runtime where necessary.

Integration-specific knowledge belongs inside the Integration boundary, not SCC Core.

Platform-specific knowledge belongs inside the Platform Adapter boundary.

An Integration may provide observation without management.

An Integration failure must never hide the underlying Security System.

Removing or updating an Integration must not silently remove, disable, or modify the underlying Security System.

Existing Security Systems must be recognized and adopted rather than unnecessarily reinstalled.

Integrations must operate with the minimum privileges required for their declared capabilities.

Integration secrets must be protected and excluded from ordinary logs and audit records.

Security System health and Integration health are separate concepts.

The Registry itself must be integrity-protected and auditable.

The first Integrations should be chosen to exercise the architecture, not merely maximize product count."
```

---

## Annotation Index

| ANN | Location | Class |
|---|---|---|
| ANN-01 | §2 Integration state list | OPEN |
| ANN-02 | §2 ownership modes (also §3, §5) | OPEN |
| ANN-03 | §2 Integration compatibility ("CyberPanel versions") | SUPERSEDED (replacement OPEN) |
| ANN-04 | §2 "Integration isolation is mandatory." | SUPERSEDED |
| ANN-05 | §3 Conceptual SecuritySystem (`integration`) | OPEN |
| ANN-06 | §3 "Discovery may inspect:" | CURRENT-REFINED |
| ANN-07 | §4 "Long-running actions become Jobs." | CURRENT-REFINED / OPEN |
| ANN-08 | §4 "Concurrency/conflict handling is required." | CURRENT-REFINED / OPEN |
| ANN-09 | §5 "Adoption is explicit." (also §6) | OPEN |
| ANN-10 | §6 "Execution occurs through the Integration." | SUPERSEDED |
| ANN-11 | §6 "No arbitrary installation URLs." | CURRENT-REFINED |
| ANN-12 | §8 Job states | OPEN |
| ANN-13 | §8 authorization before Job creation / revalidation | CURRENT-REFINED |
| ANN-14 | §9 "Where CyberPanel provides identity…" | CURRENT-REFINED |
| ANN-15 | §9 "Privileged work should be isolated through a controlled worker/mechanism." | SUPERSEDED |
| ANN-16 | §9 emergency/recovery (also §12) | CURRENT-REFINED / mechanism OPEN |
| ANN-17 | §10 "Audit should be append-only and integrity-protected." | CURRENT principle / mechanism OPEN (scope qualified) |
| ANN-18 | §11 "Integration may use:" | CURRENT-REFINED |
| ANN-19 | §11 "Direct OS access is permitted only for explicit Security Integrations." | SUPERSEDED |
| ANN-20 | §11 "SCC owns its own data:" | CURRENT / design OPEN |
| ANN-21 | §11 "Potential architecture:" | SUPERSEDED (structure) / HISTORICAL (platform list) |
| ANN-22 | §12 "Recovery mode is required…" (also §13) | SUPERSEDED (as a web UI) / recovery OPEN |
| ANN-23 | §12 "Integration upgrades may occur independently…" | OPEN |
| ANN-24 | §13.55 and all subsections | HISTORICAL (as a universal model) / per-platform OPEN |
| ANN-25 | §13.55.2 "No design hacking" | **OPEN — CyberPanel K2 gate** |
| ANN-26 | §14 "Integrations may be:" | SUPERSEDED (for v1) |
| ANN-27 | §14 trust metadata | CURRENT-REFINED |
| ANN-28 | §14 "Integration detection may supplement Discovery…" | CURRENT-REFINED |
| ANN-29 | §14 metadata ("supported CyberPanel versions / hosting panels") | SUPERSEDED (replacement OPEN) |
| ANN-30 | §14 "Multiple Integrations for one Security System…" | OPEN |
| ANN-31 | §1 opening paragraph (scope: install… manage) | CURRENT-REFINED |
| ANN-32 | §7 "Health checks are read-only, bounded, and isolated." | CURRENT-REFINED |
