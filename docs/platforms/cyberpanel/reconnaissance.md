> **Document status:** EVIDENCE — NON-NORMATIVE
> **Authority category:** Evidence about the platform. **Not SCC architecture.** (See DEC-017: upstream CyberPanel
> installer behavior "is evidence about the platform, not an SCC architectural decision.")
> **Source:** Phase A reconnaissance ([historical report](../../architecture/history/phase-a-report.md) §A.2),
> re-verified against upstream source on 2026-09-23.
> **Verification scope:** Facts marked **[upstream]** were read from upstream `usmannasir/cyberpanel` branch `stable`
> at commit `592efd528e4a36a088536ce9f31fe5a32746ae7a`. **None of them were verified on the live host.** Facts marked
> **[owner-reported]** come from the owner's reconnaissance of the live instance and were not independently verified.
> **Normative:** No. Nothing here decides the CyberPanel K2 gate questions ([`k2-gate.md`](k2-gate.md)).

# CyberPanel Platform Reconnaissance

## Target

| Fact | Source |
|---|---|
| Target: CyberPanel 3.0.7, Django-based, OpenLiteSpeed / lswsgi, Ubuntu 22.04.5 LTS | [owner-reported] |
| Live development/test instance: `https://alpha.twisted-networks.com:8090` (test/deployment target only) | [owner-reported] |
| Upstream `stable` `version.txt` = `{"version":"3.0","build":7}` | [upstream] |
| Upstream default branch is `v3.0.5-dev`; `stable` is 3.0 build 7 | [upstream] |

## Identity and request handling

| Fact | Source |
|---|---|
| Custom `Administrator` model in `/usr/local/CyberCP/loginSystem/models.py`, including `userName` and `acl` | [owner-reported] |
| Legacy page helper `httpProc` uses `request.session['userID']` and resolves the CyberPanel ACL. It is CyberPanel's ACL gate, not SCC authorization. | [owner-reported]; `pluginHolder/views.py` uses `httpProc` [upstream] |
| Middleware includes `SecurityMiddleware`, `SessionMiddleware`, `LocaleMiddleware`, `CommonMiddleware`, `CsrfViewMiddleware`, `AuthenticationMiddleware`, `MessageMiddleware`, `XFrameOptionsMiddleware`, `CyberCP.secMiddleware.secMiddleware` | [upstream] `CyberCP/settings.py`; [owner-reported] |
| `X_FRAME_OPTIONS = 'SAMEORIGIN'` | [upstream] `CyberCP/settings.py` |
| Panel sends `CSP frame-ancestors 'self'` | [owner-reported] |

## Plugin mechanism

| Fact | Source |
|---|---|
| `pluginInstaller.py` unzips the plugin into `/usr/local/CyberCP` | [upstream] `pluginInstaller/pluginInstaller.py` |
| It inserts the plugin into `INSTALLED_APPS` in `CyberCP/settings.py` after the line containing `'emailPremium',` | [upstream] |
| It inserts a route into `CyberCP/urls.py` after the line containing `manageservices` | [upstream] |
| It inserts a navigation link into `baseTemplate/templates/baseTemplate/index.html` at `{# pluginsList #}` | [upstream] |
| It runs the plugin's pre/post install scripts, runs migrations when `enable_migrations` exists, collects static files, and runs `systemctl restart lscpd` | [upstream] |
| These edits are string insertions; running the installer twice would insert duplicate lines | [upstream] (reading of the source) |
| Plugin registry: `/home/cyberpanel/plugins/<name>` marker files; `pluginHolder/plugin_metadata.py` reads `/usr/local/CyberCP/<name>/meta.xml` without importing or executing plugins | [upstream] |
| `/usr/local/CyberCP/testPlugin` is stale and is not the canonical plugin architecture | [owner-reported] |

## Static files

| Fact | Source |
|---|---|
| `STATIC_ROOT = os.path.join(BASE_DIR, "static/")`, `STATIC_URL = '/static/'` | [upstream] `CyberCP/settings.py` |
| The plugin installer's static step removes `/usr/local/lscp/cyberpanel/static`, runs `collectstatic`, and moves the result to `/usr/local/lscp/cyberpanel` | [upstream] `pluginInstaller.py` |
| The upgrade's static step removes `/usr/local/CyberCP/public/static`, runs `collectstatic --clear`, and moves the result to `/usr/local/CyberCP/public/` | [upstream] `plogical/upgrade.py` |
| The two code paths use different destinations | [upstream] (observation) |

## Upgrade behavior

| Fact | Source |
|---|---|
| The upgrade clones a fresh CyberPanel tree (`git clone -- https://github.com/usmannasir/cyberpanel …`) and activates it | [upstream] `plogical/upgrade.py` |
| `preserve_installation_state` copies only the embedded runtime (virtualenv) and explicitly backed-up private files; `settings.py` receives only the database configuration merged into the new source | [upstream] |
| Consequence (reading of the source, not verified on the host): plugin code under `/usr/local/CyberCP/<name>`, the `INSTALLED_APPS` entry, the URL route and the navigation link would be lost on upgrade | [upstream] (inference) |

## Not yet established

- The live host has not been compared read-only against upstream `stable` (Phase A request 5 is unanswered).
- The stability of CyberPanel's identity fields over time (K2-Q5).
- Whether any supported extension mechanism avoids core-file edits (K2-Q2, K2-Q6).
