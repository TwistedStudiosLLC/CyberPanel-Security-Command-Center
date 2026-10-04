> **Document status:** OPEN — CyberPanel K2 gate
> **Authority category:** 4 — Conditional/open architecture (see [Authority Hierarchy](../../architecture/README.md#authority-hierarchy))
> **Source:** DEC-015 (D-3), DEC-016 (D-4), DEC-017 (D-5), DEC-018 (D-6), DEC-025 (D-13), DEC-026 (D-14), DEC-027 (D-15).
> **Normative:** No. **This document lists questions only.** It answers none of them.

# CyberPanel K2 Gate — Open Questions

CyberPanel is the first platform (DEC-016). Its integration is K2 (DEC-018). This gate is PHASE 7 of the
implementation order (DEC-025). Platform facts gathered so far are in
[`reconnaissance.md`](reconnaissance.md) (evidence, non-normative).

## Implementation prohibition until this gate answers K2-Q1

Per DEC-027 (D-15):

```text
    do not implement the CyberPanel route
    do not implement the CyberPanel template
    do not implement the UI bridge
```

## Questions

| ID | Question | Source |
|---|---|---|
| K2-Q1 | See the verbatim question below. | DEC-027 (D-15) |
| K2-Q2 | How can SCC be installed and re-registered on CyberPanel while preserving idempotence, reversibility, upgrade behavior, version awareness, SCC process separation and SCC data ownership? Can a conforming K2 deployment mechanism be built around the actual CyberPanel extension model without amending T-24? If not, the contradiction must return as an explicit architecture decision. | DEC-017 (D-5); KF-03 |
| K2-Q3 | What conforming presentation/security boundary does the CyberPanel integration establish against the actual platform (ODF-18-01 for CyberPanel)? | DEC-015 (D-3); KF-01, KF-02 |
| K2-Q4 | Are K2 assertions bound to request content where K2 relays requests? | §18 ODF-18-06 / TQ-05 (open) |
| K2-Q5 | Which CyberPanel identity field is the canonical `platform_subject_id`, and how stable is it over time (for example, across deletion and re-creation of a username)? | §17.1.3; P-6; TQ-03 |
| K2-Q6 | Can CyberPanel's supported extension mechanism route browser requests to an independent K3 process without core-file modification? | §15.18 OQ-1 |
| K2-Q7 | How does the CyberPanel adapter normalize CyberPanel's account model to the platform role `PLATFORM_ADMIN` that §17 requires (as a restriction only)? | §17.1.5, A-04; DEC-011 |

**K2-Q1 (verbatim from DEC-027):**

```text
    Which portion of the CyberPanel-native presentation surface
    may execute inside K2, and what exact data/protocol boundary
    separates it from K3/K4, while preserving the §15 trust
    invariants and the §18 threat requirements?
```

## Constraints this gate must preserve (pointers only)

- K2's permitted and prohibited roles: §15.6; DEC-018.
- K2 talks only to K3 over P2 (DEC-026). The P2 contract is its own gate: [`../../architecture/open/p2-protocol.md`](../../architecture/open/p2-protocol.md).
- SCC Core stays provider-neutral; CyberPanel knowledge stays in CyberPanel K2 (DEC-016; T-27).
- DEC-015: do not resolve ODF-18-01 by weakening §15, by placing SCC authorization inside CyberPanel, by putting
  SCC Core into the CyberPanel Django process, or by inventing a universal iframe/cross-origin architecture.
- No privileged CyberPanel operations or execution paths (DEC-029).
