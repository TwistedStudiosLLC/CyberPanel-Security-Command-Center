> **Document status:** HISTORICAL — NON-NORMATIVE
> **Authority category:** 5 — Historical / forensic material (see [Authority Hierarchy](../README.md#authority-hierarchy))
> **What this is:** The Phase A repository reconnaissance report produced in response to an implementation brief that
> has since been superseded (see [`superseded-register.md`](superseded-register.md), entries C-12 and C-13).
> **This document is not current authority.** Its decisions do not independently establish current architecture
> (DEC-030, Q5).
> **Rejected content:** STOP-2 option (b) ("A recorded, time-limited §15 deviation for this privilege-free slice that
> lets K3/K4 logic run inside CyberPanel") was **REJECTED** by the owner (superseded-register C-11; DEC-018, DEC-016).
> **Later decisions:** The questions at the end of this report were answered by the owner in DEC-013 … DEC-030. The
> platform facts in §A.2 were re-verified against upstream `stable` at commit
> `592efd528e4a36a088536ce9f31fe5a32746ae7a` and are recorded in
> [`../../platforms/cyberpanel/reconnaissance.md`](../../platforms/cyberpanel/reconnaissance.md).
> **Transcription notes:** Reproduced verbatim. No wrapper text was removed.

# Phase A: Repository Reconnaissance

**Result: I've stopped at a STOP condition (§23 of your brief).** The repository has no SCC Core to integrate with. There is also a direct conflict between "native Django route inside CyberPanel" and the locked §15 topology. I made no changes to the repository or to any server. The only reads outside the repo were the upstream CyberPanel sources, which I saved to my scratchpad.

## A.1 SCC repository (`TwistedStudiosLLC/CyberPanel-Security-Command-Center`)

The local checkout and `git ls-remote` agree: there is exactly one commit, `d7b1b9f Initial commit`, on the only branch, `main`. The only tracked file is `LICENSE` (MIT, Twisted Studios LLC).

| Item you asked for | Found |
|---|---|
| SCC Core location | None |
| Integration / provider abstraction | None |
| Principal implementation (§17.1) | None |
| Authorization implementation (§17.4, §17.19, §17.22) | None |
| Operation / K6 / K11 implementation (§16) | None |
| Core Discovery declaration | None |
| Test framework or conventions | None |
| Packaging | None |
| CI (`.github/`) | None |
| Release mechanism | None |

The §1–§18 architecture exists only in this conversation. It has never been committed. It is also not finished:
- §18 is still **CONDITIONAL**, with ODF-18-01 to 09 undecided.
- §19 (persistence), §21 (audit/events) and §22 (lifecycle) haven't been written.

A Principal needs somewhere to be stored (K7, which is §19's job), and an authorization decision needs an audit record (§21's job).

## A.2 Upstream CyberPanel, checked against source rather than assumed

Upstream `usmannasir/cyberpanel` branch `stable` has `version.txt` = `{"version":"3.0","build":7}`, which matches your target. What I found:

1. **The plugin mechanism edits CyberPanel's core files.** `pluginInstaller.py` on `stable` does the following:
   - unzips the plugin into `/usr/local/CyberCP/<name>`;
   - adds the plugin to `INSTALLED_APPS` in `CyberCP/settings.py` by inserting text after the `'emailPremium',` line;
   - adds a route to `CyberCP/urls.py` by inserting after the `manageservices` line;
   - adds a navigation link to `baseTemplate/templates/baseTemplate/index.html` at `{# pluginsList #}`;
   - runs the plugin's pre/post install scripts as root;
   - runs migrations;
   - runs `systemctl restart lscpd`.

   These are string insertions. Running the installer twice would add duplicate lines, so it isn't idempotent.
2. **Plugin registry.** `/home/cyberpanel/plugins/<name>` is just an empty marker file. `pluginHolder/plugin_metadata.py` reads each plugin's `/usr/local/CyberCP/<name>/meta.xml` without executing any plugin code. `testPlugin` is not the reference to follow; `pluginInstaller.py` plus `examplePlugin.zip` are.
3. **Upgrades wipe plugins.** `plogical/upgrade.py` does a fresh `git clone` of the CyberPanel tree and switches to it. It keeps only:
   - the virtualenv;
   - a short list of critical files (`.env`, `secret_key`, …);
   - the `DATABASES` block from `settings.py`.

   Plugin code, the `INSTALLED_APPS` entry, the URL route and the navigation link are all lost. This is my reading of the source; please verify it on the live host.
4. **Your static-file pipeline assumption is only half right.** `upgrade.py` moves collected static files to `/usr/local/CyberCP/public/static`. The plugin installer instead moves them to `/usr/local/lscp/cyberpanel/static`. The current code uses two different destinations.
5. The middleware list and `X_FRAME_OPTIONS = 'SAMEORIGIN'` match what you described.

The live instance may differ from upstream `stable`. It should be checked read-only before Phase B.

## A.3 Stop conditions

**STOP-1: The SCC Core contracts don't exist.** Brief §7: *"If the SCC Core is not yet implemented sufficiently… STOP."*
- **Missing, all in the repository root:**
  - the Principal and Platform Identity Binding (§17.1);
  - Grant and Role evaluation (§17.3, §17.4);
  - Authorization Decisions and `authorization_ref` (§17.19);
  - the K7 store (§19, not yet designed);
  - the audit record format (§17.18 lists the fields, but §21's format isn't designed).
- **Why it matters:** if the adapter built these itself, it would become the "second authorization engine" your brief forbids.
- **Options:**
  - (a) Build a minimal SCC Core slice first, in its own package: Principal, Binding, enrollment, built-in Roles, Grant evaluation, and fail-closed deny.
  - (b) Do a §19 persistence design pass first.

**STOP-2: "Native Django route in CyberPanel" conflicts with the locked §15 topology.**
- **What §15 requires:**
  - K2 (the CyberPanel-side bridge) may only register navigation, render the page frame and issue identity assertions. It must hold no SCC domain logic or authorization data (§15.6).
  - SCC Core (K4) must run as a separate process with its own identity (T-01, T-04).
  - Its data must not live in CyberPanel's store (T-23, T-25).
- **What the brief requires:** an SCC-owned UI plus SCC authorization. If both run as Django code inside CyberPanel, that code runs in K1's root-equivalent process, which breaks those invariants.
- **ODF-18-01 is effectively decided by this brief.** "No iframe, no cross-origin" together with CyberPanel's `SAMEORIGIN` / `frame-ancestors 'self'` headers rules out Option A (origin isolation) on CyberPanel. That leaves Option B or C, and each needs its §15 amendment.
- **Options:**
  - (a) The CyberPanel Django app is K2 only. It relays same-origin requests to separate SCC K3/K4 services. This follows §15, but only after ODF-18-01 is resolved as B or C, and it needs K3/K4 built first.
  - (b) A recorded, time-limited §15 deviation for this privilege-free slice that lets K3/K4 logic run inside CyberPanel. That puts SCC authorization in a root-equivalent process and must be explicitly accepted.
  - (c) Something else you specify.

**STOP-3: The installation mechanism conflicts with §11 / T-24 / T-25 and your brief §17.**
- The only current CyberPanel plugin path edits `settings.py`, `urls.py` and `index.html`.
- That path doesn't survive a CyberPanel upgrade.
- It isn't idempotent.
- **Options:**
  - (a) Use CyberPanel's installer, treating it as the documented "exceptional, guarded" core edit that §11 allows, and add a re-registration step after every CyberPanel upgrade.
  - (b) Our own repository-built installer that makes the same three edits, but idempotently and reversibly, with a post-upgrade re-apply hook.
  - (c) Propose a supported extension point upstream to CyberPanel, which is a longer route.

  One observation that is not a decision: the virtualenv survives upgrades, so a package installed there would survive, but its three registrations still wouldn't.

**Minor points:**
- Your brief calls SCC "System Control Contract". The repository and architecture call it "Security Command Center". Please confirm which name to use.
- There are no tooling conventions yet. The Python and Django versions will need to be pinned to CyberPanel 3.0.7's virtualenv.

## What I need from you before Phase B

1. **Architecture in the repo:** should §1–§18 be committed as the documentation source of truth (for example under `docs/architecture/`)? I'd do that on a feature branch.
2. **STOP-2:** choose (a), (b) or (c). This also settles ODF-18-01.
3. **STOP-1:** approve building a minimal SCC Core slice, and decide whether §19 persistence comes first.
4. **STOP-3:** choose an installation strategy.
5. **Live-host check:** may I run a read-only comparison of the live instance against upstream `stable`, using commands you run and send back to me, not changes I make?
