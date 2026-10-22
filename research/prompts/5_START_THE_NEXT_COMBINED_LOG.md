# PROMPT 5 — Roll over the Combined Log without consuming IDs

**Local keys until settlement; updated mini after every game (MINI-v2).** Defined in [MINI_LOG_IDENTITY_PROTOCOL](../../MINI_LOG_IDENTITY_PROTOCOL.md); summarised in [CORE](../../CORE.md) §2.

**Persistent research and corroboration (EXH-v1).** Defined in [RESEARCH_EXHAUSTIVENESS_PROTOCOL](../../RESEARCH_EXHAUSTIVENESS_PROTOCOL.md); summarised in [CORE](../../CORE.md) §5.

**Online history and confirmed players (HIST-2026.10.16-v3 / AVAIL-2026.10.16-v4).** Defined in [HISTORICAL_SOURCE_PROTOCOL](../../HISTORICAL_SOURCE_PROTOCOL.md); summarised in [CORE](../../CORE.md) §5.

**P-2026.10.22-v24.0 · COMBINED_LOG_ROLLOVER · LOCAL_WORKING_TREE.** Read [COMMON_OPERATING_PROTOCOL](COMMON_OPERATING_PROTOCOL.md). Default trigger: working file exceeds 1.5 MB, contains at least 50 canonical entries, or cannot be opened/rendered reliably. Record the actual trigger/measurement; rollover is not required to settle or import. Run between complete imports.

**ML/RL scope (MLSCOPE-v3).** Defined in [FORECAST_CYCLE_PROTOCOL](../../FORECAST_CYCLE_PROTOCOL.md); summarised in [CORE](../../CORE.md) §7.

**Execution environment (ENV-v2).** Defined in [EXECUTION_ENVIRONMENT_PROTOCOL](../../EXECUTION_ENVIRONMENT_PROTOCOL.md); summarised in [CORE](../../CORE.md) §1.

**Required repository fallback (REF-v1).** Defined in [GITHUB_REFERENCE_PROTOCOL](../../GITHUB_REFERENCE_PROTOCOL.md); summarised in [CORE](../../CORE.md) §1.

## Inputs and allowed writes

Resolve active Part N, user request/trigger and current queues. Writes: old-part closure, one new part, current state/status/live pointers, CHANGELOG and a new rollover receipt. No forecasts, settlements, copied cards, P-ID allocation or model promotion. Publish under the invoked task unless explicitly local-only.

## 1. Reconcile and plan

Read common controls/protocol, templates §8, verification §4, current status and actual log entries/opening/closure records. Print authority/HEAD/dirty inventory. Resolve current Part N, highest/next ID, reserved IDs, pending and evidence queues, and any partial import. Opening snapshots are historical; do not revise them to current values.

Block rollover over an unfinished import. Snapshot the entire old-part working bytes/count/hash and proposed Part N+1 path. An exact completed rollover returns ALREADY_COMPLETED with zero writes. A partial closure/new part requires scoped comparison/recovery; never overwrite an occupied file or create N+2 to hide it.

## 2. Apply closure and new opening

Immediately before closure, recheck HEAD, active path, raw count/hash/tail, next ID and source plan. On drift, re-plan. Append a dated closure with measured contained range/count, highest global ID, unchanged next ID, both queues and prior identity, plus the new-part link.

Recheck again before creating Part N+1. Create its ACTIVE opening, method/control/scoring/HEAD, time/zone, explicit OPENING_SNAPSHOT, previous-part continuity, reserved-ID note, highest/next ID unchanged, queue pointers and research-only/market-blind labels. Use canonical-md-1 and the END ACTIVE COMBINED LOG HEADER marker. Do not insert a placeholder forecast.

Later revisions for closed-part originals go into the new active part with original/prior-revision pointers; the closed original stays immutable. Shadow/model IDs and receipts remain at their existing independent locations. Rollover is no qualification or artifact change.

Update only live pointers and dated change/report records. Prefer dynamic CURRENT_STATE references; retain historical links and old-format semantics.

## 3. Verify, publish and return

Compare the entire old prefix, confirm only closure appended, and verify new part contains header/continuity/queues only. Reconcile all current pointers, zero copied forecasts, unchanged IDs and rerun idempotency. Read back every output; report raw/committed identities separately.

Stage exact paths and publish without force when authorized; fetch and verify remote SHA and artifacts. Return trigger, old/new paths, queue continuity, unchanged next ID, byte verification and actual publication status.

## Research retention and execution disposition (RETAIN-v1)

**Retain the research (RETAIN-v3).** Defined in [RESEARCH_RETENTION_PROTOCOL](../../RESEARCH_RETENTION_PROTOCOL.md); summarised in [CORE](../../CORE.md) §2.

Carry any legacy execution-manifest/attempt/bundle/feedback custody pointers and the open repair queue into the continuity report unchanged; prompt 6 owns them. A rollover must not manufacture runs or feedback, refit old cards or copy forecasts. Canonical-md-1 is unchanged.

**Local research record and updated-document delivery (owner update, 16 October 2026).** Defined in [MINI_LOG_IDENTITY_PROTOCOL](../../MINI_LOG_IDENTITY_PROTOCOL.md); summarised in [CORE](../../CORE.md) §2.

## Persistent sourcing and information closure (EXH-v1)

Carry the current source-register and exact outstanding requirement/attempt pointers through rollover without duplicating facts, closing a gap or allocating an ID. Missing evidence remains open; preserve closed-part and source bytes. Research continuation uses EXH-v1 and current source observations.
