# PROMPT 5 — Roll over the Combined Log without consuming IDs

**P-2026.10.15-v16.1 · COMBINED_LOG_ROLLOVER · LOCAL_WORKING_TREE.** Read [COMMON_OPERATING_PROTOCOL](COMMON_OPERATING_PROTOCOL.md). Default trigger: working file exceeds 1.5 MB, contains at least 50 canonical entries, or cannot be opened/rendered reliably. Record the actual trigger/measurement; rollover is not required to settle or import. Run between complete imports.

**Required repository fallback (REF-v1).** Always keep [https://github.com/danisgreat/Sports-Research/tree/main](https://github.com/danisgreat/Sports-Research/tree/main) as the standing reference. If required local files are not fully accessible (missing, unreadable, truncated or incomplete), retrieve the actual required contents from this repository before declaring them unavailable. Apply [GITHUB_REFERENCE_PROTOCOL](../../GITHUB_REFERENCE_PROTOCOL.md): resolve one main commit SHA, record exact files/read time and fallback results in the existing reading receipt, and preserve the declared authority mode. Never substitute an unpublished local mini, claim unread content or treat viewing code as executing it. If authorized remote access also fails, record the real gap and continue independent work.

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

## Mandatory ML execution coverage (EXEC-v1)

**Strict per-event execution:** read [ML_EXECUTION_PROTOCOL](../../ML_EXECUTION_PROTOCOL.md). Every new game requires an actual `primary execute` attempt and retained success/failure receipt even without a pre-existing league baseline/profile, plus its `ML_EXECUTION_MANIFEST.csv` row. Build the comparator from reviewed exact-competition history where possible; missing paired scoring never waives fitting/learning. No numeric success is claimed for unsupported/failed runs. Require C21 and `primary verify-log` before completion/import, preserve real capability gaps as INCOMPLETE execution, and keep full independent research. Successful settled bundles require source-backed feedback or a named pending/blocked reason; baselines, analyst comparisons and absent feedback never manufacture a learning observation.

Carry the execution-manifest/attempt/bundle/effective-feedback custody pointers and open repair queue into the continuity report. Recheck that new EXEC-v1 imports were verified; a rollover must not drop execution gaps, manufacture runs/feedback, refit old cards or copy forecasts. Canonical-md-1 is unchanged.
