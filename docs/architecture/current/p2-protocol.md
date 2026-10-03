> **Document status:** LOCKED [DEC-088]
> **Authority category:** 1 — Locked architecture, from DEC-088 forward (see [Authority Hierarchy](../README.md#authority-hierarchy)).
> The earlier Category 4 classification is historical [DEC-088].
> **Source:** P2/K3 gate (PHASE 5 of DEC-025; DEC-026). Scope and gate structure: DEC-080. Phase-6 dependency:
> DEC-079 D79-5. Request-ID routing: DEC-087. Dispositions, locked form and lock: DEC-088.
> **Normative:** Yes. Tags: [L] locked text; [DEC-0xx] adopted decision. Neither this document nor the decision log
> amends §15–§17, §19, §21 or §22.
> **Findings against this text:** none recorded.
> **Implementation:** No schema, socket path, key or code is defined here, and no implementation authority is created
> (DEC-029; DEC-079; DEC-088).

# P2 / K3 — Platform Bridge Protocol and Gateway Boundary

---

## P.1 Purpose, Authority and Scope

This gate specifies the platform-neutral P2 protocol (K2 → K3) and the K3 service boundary on P3 (K3 → K4) that locked
§15.6 and §15.10 leave open [DEC-080 D80-1 … D80-3; DEC-026]. It is the P2 gate of DEC-026; no other gate is created
[DEC-080 D80-1]. Phase 5 is complete only when this gate is separately locked by an explicit owner DEC [DEC-079 D79-5].

## P.2 What Locked Architecture Already Fixes (not restated as decisions)

- K2 may register navigation, render the page frame, read the platform session, issue a short-lived audience-bound
  identity assertion and, where the adapter requires, relay browser requests to K3. K2 must not contain SCC domain
  logic, hold SCC authorization data, call K4 or K6 other than via K3's request path, invoke host operations or store
  SCC state [L §15.6].
- K3 may serve UI assets from K11, run the Presentation Adapter, validate request shape (not a security control) and
  relay requests plus the **unmodified** identity assertion or SCC session token to K4. K3 must not decide
  authorization, mint or alter identity, present cached state as current when K4 is unavailable, access K7, reach K5
  or K6, or persist or log platform session credentials [L §15.6; T-19; T-30].
- P2 (K2 → K3): relay request + identity assertion; peer identity of the platform process plus the assertion
  signature, verified end-to-end by K4, not K3; nothing authorized at K3; local-only channel; tokens not logged;
  assertion short-lived, audience-bound (SCC), nonce/session-bound [L §15.10 P2].
- P3 (K3 → K4): API calls carrying an assertion or SCC session token; peer identity W plus end-user assertion or
  session validated by K4; K4 decides; schema-validated by K4; local-only; K4 enforces assertion freshness and single
  use where applicable; state-changing requests carry request IDs (details §16/§17); K4 down → K3 returns
  "unavailable" and must not serve stale state as current [L §15.10 P3].
- Credential placement: the platform session may exist in the browser, K1 and K2 (read); K3 may see it in transit on a
  proxied path but must strip it and never persist, log or forward it. The assertion signing key exists only in K2;
  verification material only in K4, asymmetric so no verifier can mint. SCC session tokens: browser, K3 (transient
  relay), K4 (validation state) [L §15.12; T-20].
- No SCC process exposes a network listener reachable from outside the host [L T-31; §15 network posture item 6].
- K4 verifies signature, audience, freshness and single use, then Binding and Principal state; there is no
  authorization based on an unverified claim [L §17.2; §17.22 step 1; A-01]. Authentication Context = assertion ID,
  platform, subject, authentication time, and any method claims [L §17 Terms].
- Platform session identity is never authorization (T-13); platform role facts only restrict (A-04); in v1 a HUMAN
  Principal acts only while its platform identity holds `PLATFORM_ADMIN` [L §17.1.5]. Binding CONFIRMED comes from a
  verified assertion or recent Platform Services observation [L §17.1.4].
- SCC session tokens are never persisted in a form recoverable for bearer use [DEC-044 R14b]; session semantics and
  K4 validation-state form are P2's [DEC-044 R14c, R14f; locked §19 DC-19, §19.22].

## P.3 P2 — Assertion Contract (D80-2)

1. [DEC-088] **Required contents.** An identity assertion carries:
   - `assertion_id`, unique per issued assertion;
   - `platform` = (`platform_adapter_id`, `platform_instance_id`) and `subject` = `platform_subject_id` — the Platform
     Identity Binding tuple [L §17.1.3];
   - `auth_time`, the platform authentication time;
   - `method_claims`, if the platform supplies any [L §17 Terms];
   - `audience`, identifying the SCC instance the assertion is for [L §15.10 P2 "audience-bound (SCC)"];
   - `issued_at` and `expires_at` (short-lived) [L §15.10 P2];
   - `binding`, the nonce or session binding required by §15.10 P2 (§P.7.6);
   - `key_id`, identifying the K2 signing key used (P.6).
2. [DEC-088] **Platform role fact** [DEC-088]. The assertion carries the adapter-normalized platform role of the
   subject, so that K4 can apply the v1 `PLATFORM_ADMIN` restriction and Binding status (§17.1.4, §17.1.5). The role
   fact is restrictive only: it may restrict K4 authorization but never grants authority, never widens K11 scope,
   never bypasses K4 authorization and never overrides K7 state [L T-13; A-04; A-10]. K3 does not evaluate it.
3. [DEC-088] **No request-content binding.** The assertion is not bound to request content [DEC-080 D80-2; ODF-18-06
   NON-BLOCKING, DEC-079 D79-6].
4. [DEC-088] **Lifetime.** `expires_at` − `issued_at` is short and does not exceed a fixed maximum assertion lifetime that
   K4 enforces [L §15.10 P2]. The maximum is 60 seconds from `issued_at` to `expires_at` (owner choice) [DEC-088].
5. [DEC-088] **Signature.** The assertion is signed by K2 with its asymmetric signing key and verified by K4 with
   verification material only [L §15.12; T-20]. Assertion encoding: CBOR. Signature algorithm: Ed25519; no symmetric
   signing or verification keys (owner choices) [DEC-088].

## P.4 P2 — Freshness, Replay and Single Use

1. [DEC-088] K4 rejects an assertion that is not yet valid, has expired, carries the wrong `audience`, has an unknown or
   retired `key_id`, or fails signature verification [L §17.22 step 1].
2. [DEC-088] K4 records `assertion_id` for the assertion's validity period and rejects any second use [L §17.22 step 1
   "single use"]. An assertion used to establish an SCC session is consumed by that act (§P.7.6).
3. [DEC-088] Replay rejection is K4's; K3 performs none and holds no replay state [L §15.6; DEC-080 D80-4].

## P.5 P2 — Message, Transport, Endpoint and Error Model

1. [DEC-088] **Message.** A P2 message carries one browser-originated request plus exactly one assertion or one SCC session
   token. K3 relays both to K4 unmodified [L §15.6].
2. [DEC-088] **Transport.** Host-local only. K2 → K3 uses a channel on which the OS identifies the peer as the platform
   process; K3 → K4 uses a channel on which the OS identifies the peer as W [L §15.10 P2, P3]. Neither K3 nor K4
   exposes a listener reachable from outside the host [L T-31]. Transport: a host-local Unix domain socket with OS
   peer-credential verification; no TCP, HTTP listener exposure or other external transport; no socket path is defined
   architecturally (owner choice) [DEC-088].
3. [DEC-088] **Endpoint exposure.** K3 is reachable only through the platform edge, by K2 relay or by a platform-supported
   proxy route (an adapter choice) [L §15.6; DEC-080 D80-5]. Both remain admissible.
4. [DEC-088] **Error model.** K4 returns one of: `MALFORMED` (schema), `UNAUTHENTICATED` (any §17.22 step-1 failure),
   `FORBIDDEN` (authorization denial), `INADMISSIBLE`, `UNAVAILABLE`, or success. K3 relays K4's result unchanged, and
   returns `UNAVAILABLE` itself only when K4 cannot be reached; it never substitutes cached state [L T-30; §15.10
   P3]. K3 may return `MALFORMED` for shape failures, which is not a security decision [L §15.6]. Error bodies carry
   no assertion, token or credential [L T-19].

## P.6 P2 — Signing-/Verification-Key Relationship and Rollover (protocol level)

1. [DEC-088] Each assertion names its signing key by `key_id`. K4 accepts a `key_id` only while K4 holds the corresponding
   active verification material [L §15.12].
2. [DEC-088] Rollover: a new key is added and becomes active for verification before K2 starts using it; the old key
   remains accepted for an overlap no longer than the maximum assertion lifetime, then is retired. Multiple active
   values are permitted [DEC-051 R01h].
3. Storage, provisioning, recovery and rotation mechanics of verification material are not decided here: OD19-01
   (DEC-051 R01b coordination) and §22 O-4, O-15 [DEC-080 D80-2 excluded; locked §22.8]. K2 signing-key provisioning
   is §22 O-4.

## P.7 K3 Service Boundary on P3 (D80-3)

1. [DEC-088] **Envelope.** A P3 request carries: the relayed request, the unmodified assertion or SCC session token, and,
   for state-changing requests, the request ID required by §15.10 (semantics deferred to the §16 Amendment Gate, DEC-087, §P.7.7).
2. [DEC-088] **Structural validation.** K3 checks request shape only (well-formedness, size, known route). It never
   inspects or validates the assertion or token, and its validation is not a security control [L §15.6].
3. [DEC-088] **Relay.** K3 forwards the request, assertion or token and request ID to K4 unchanged, and K4's response to
   the client unchanged. K3 adds only its own peer identity, which the OS establishes [L §15.10 P3].
4. [DEC-088] **K4 unavailable.** K3 returns `UNAVAILABLE` and does not serve stale or cached state as current [L T-30].
5. [DEC-088] **Prohibited K3 persistence, caching and logging.** K3 persists no SCC state, caches no authorization or
   state, and never persists or logs assertions, SCC session tokens, platform session credentials or other
   credentials. On a proxied path it strips the platform session [L §15.6; §15.12; T-19; S19-13; DEC-044].
6. [DEC-088] **SCC session semantics** [DEC-088; DEC-044 R14b, R14c, R14f; locked §19 DC-19]:
   - a verified assertion may establish an SCC session; the assertion is consumed (§P.4.2);
   - sessions are stateful: K4 owns the session validation state and its invalidation, and K4 policy bounds session
     lifetime; K4 remains the authorization authority, and every request on a session is authorized by K4;
   - the session token is an opaque reference to K4 state, not a signed token; no persistent signing or MAC secret is
     introduced, so DEC-044 R14d is not triggered and no new secret class is created;
   - K4 never persists the token in a form recoverable for bearer use [DEC-044 R14b];
   - K3 holds no session authority, no authorization state and no validation state; session state is not
     recoverable through K3; K3 never mints or alters an assertion or a session token;
   - session validation state exists only in K4 runtime state; K4 restart terminates every active SCC session; it is
     not placed in K7, not recoverable across restart and has no recovery mechanism; locked §19 DC-19 is unchanged
     (owner choice) [DEC-088];
   - owner reading of the §15.12 impact rule, not an amendment to §15: the token may be transiently present in K1/K2
     while passing through the existing platform path; K1/K2 must not persist, log, mint, alter or independently
     authorize with it; K3 may transiently relay it within its locked boundary; K4 remains the sole authority for
     session validation and authorization; K1/K2 gain no SCC authorization authority [DEC-088].
   Stateless signed-session tokens are not used.
7. **Request-ID semantics** are §16/§17 matters, referenced, not redefined [DEC-080 D80-3]. Their owning route is the
   §16 Amendment Gate, by separate owner assignment under DEC-068 D68-D [DEC-087]. This contract does not define
   them. Locked §21's `p3_request_id` is unchanged.

## P.8 Identity Flow (D80-4)

K2 → K3 → K4. K4 verifies end-to-end and derives the Authentication Context [L §17.2; §17.22 step 1]. K3 performs no
authorization and does not mint or alter identity. K2 has no path to K4, K5 or K6 [DEC-080 D80-4; L §15.6]. A verified
assertion confirms the Binding (§17.1.4); this is the path by which the bootstrap-created first administrator
(locked §22.4) first becomes able to act.

## P.9 Open Items and Routes

| Item | Route |
|---|---|
| P3 request-ID semantics | §16 Amendment Gate (DEC-087) |
| Assertion-verification material storage and provisioning | OD19-01, DEC-051 R01b |
| K2 signing-key provisioning; K2 re-registration | §22 O-4 |
| CyberPanel route verification (relay vs proxy), presentation placement, installation, `platform_subject_id` stability | CyberPanel K2 gate (K2-Q1 … K2-Q7; OQ-1; P-6; KF-01, KF-02) [DEC-080 D80-5] |
| Request-bound assertions | Platform Adapter gate, ODF-18-06 (NON-BLOCKING) [DEC-079 D79-6] |
| Cross-instance approval replay (instance identity in approvals) | ODF-18-02 / KF-04 (§18, conditional) |

## P.10 Non-Ownership

P2/K3 does not own: authorization (K4, §17); identity (K1/K2 issue, K4 verifies); request-ID semantics (§16 Amendment
Gate); K6, K7, K8; DC-18 storage (OD19-01); key provisioning (§22); CyberPanel specifics (K2 gate); presentation
content; §21 audit records (K4 records failed authentication as B2 per locked §21.14).

## P.11 Lock Criteria [DEC-080 D80-8, verbatim]

1. every D80-2 element is specified or explicitly deferred to an established gate;
2. every D80-3 item is specified within locked §15.6/§15.10;
3. the delivered assertion supports every §17.22 step-1 check and every §17 Authentication Context field;
4. no CyberPanel-specific K2 question is decided, and both relay and proxy routes remain admissible;
5. no accepted decision widens authority, transfers responsibility between K2–K11, contradicts §15–§17, or makes an
   unauthorized amendment; K3 gains no authorization, identity or state authority;
6. every deferral names an established owning gate;
7. no implementation authority is created, and the lock is a separate explicit owner DEC.
