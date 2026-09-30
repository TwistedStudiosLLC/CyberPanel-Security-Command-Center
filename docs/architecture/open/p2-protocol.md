> **Document status:** NOT DESIGNED — GATE PENDING
> **Authority category:** 4 — Conditional/open architecture (see [Authority Hierarchy](../README.md#authority-hierarchy))
> **Source:** DEC-026 (D-14).
> **Gate structure (pointers only):** P2/K3 scope and gate structure: DEC-080 (covers P2 and the P3 K3 → K4 service
> boundary).
> **Normative:** No. **This stub contains no normative behavior.** It must not be used to invent the P2 protocol.

# P2 — K2 ↔ K3 Protocol

**Status:** NOT DESIGNED — GATE PENDING. The P2 protocol must be designed as its own architecture gate before K3/K2
implementation (DEC-026).

## What the current architecture establishes

Per DEC-026, the current architecture only establishes that:

```text
    K2 talks to K3

and:

    K2 does not talk directly to K4/K5/K6.
```

## What the gate must formally specify

Per DEC-026:

```text
    message format
    assertion format
    freshness
    replay resistance
    request binding
    error model
    transport
    endpoint exposure
    key provisioning
```

## Inbound open items (pointers only)

- §15.10 (P2 row) and §15.12 (assertion signing key only in K2) — locked constraints; see §15
- §15.18 OQ-3 (assertion format and lifetime)
- §18 ODF-18-06 / TQ-05 (request-bound assertions) — open
- DEC-025: PHASE 5 "Establish the K3/P2 service boundary"

See the [open register](register.md).
