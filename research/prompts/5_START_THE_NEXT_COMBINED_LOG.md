# PROMPT 5 — Roll over the Combined Log without consuming IDs

**Online history and confirmed players (HIST-2026.10.16-v2 / AVAIL-2026.10.16-v3).** For every game, research both sides' L5/L10/L15/L20 online under [HISTORICAL_SOURCE_PROTOCOL](../../HISTORICAL_SOURCE_PROTOCOL.md), with opened sources, dated game rows and true n. Seek exact-game confirmed players, starting roles, bench/replacements and absences under [ROSTER_AVAILABILITY_PROTOCOL](../../ROSTER_AVAILABILITY_PROTOCOL.md); projected players remain unconfirmed. The retired local results store and its derived profiles are not required inputs or fallbacks. Earlier archive-first directions are superseded.

**P-2026.10.16-v17.1 · COMBINED_LOG_ROLLOVER · LOCAL_WORKING_TREE.** Read [COMMON_OPERATING_PROTOCOL](COMMON_OPERATING_PROTOCOL.md). Default trigger: working file exceeds 1.5 MB, contains at least 50 canonical entries, or cannot be opened/rendered reliably. Record the actual trigger/measurement; rollover is not required to settle or import. Run between complete imports.

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

## Research retention and execution disposition (RETAIN-v1)

**Retain the research regardless of ML (RETAIN-v1).** Read [RESEARCH_RETENTION_PROTOCOL](../../RESEARCH_RETENTION_PROTOCOL.md). Missing/unsupported/failed ML or `No module named ml`, baseline/calibration and unavailable receipts never by themselves block recording a researched game under its next reconciled P-ID or canonical import. Run the supported model when accessible; otherwise retain RESEARCH_ONLY_NO_MODEL with actual reason, no fake receipt/model probability, and supported analyst_p separately NOT_PRIMARY. C21 verifies honest disposition, including blank execution paths for no run. Settle original contracts and retain verified targets for future training even when no expert existed; only real frozen bundles supply Hedge feedback. Preserve complete research, genuine gaps and real timing; do not backdate.

Carry the execution-manifest/attempt/bundle/effective-feedback custody pointers and open repair queue into the continuity report. Recheck that new EXEC-v1 imports were verified; a rollover must not drop execution gaps, manufacture runs/feedback, refit old cards or copy forecasts. Canonical-md-1 is unchanged.


**Model use and mandatory running-log record (owner clarification, 16 October 2026).** Use the supported ML/RL mechanisms when they are available for the exact sport, competition and endpoint. Whether a model exists or not, assign the reconciled permanent P-ID, append the researched game card to the active running mini-log, read it back and advance its footer. A missing sport-specific model must not leave an otherwise recordable game as intake-only, unissued or without an ID. With no verified model output, record RESEARCH_ONLY_NO_MODEL, the actual reason and supported analyst work; never invent model probabilities or receipts. Carry that same P-ID through verified canonical import; do not allocate another ID. Before an authorized import, the local card may truthfully say PENDING_IMPORT; that status never cancels its ID or running-log entry. Identity/allocation conflicts, frozen or inaccessible originals and real write failures still block only the affected mutation. Verified settlements remain available for future model development in both paths.

See [RETAIN-v1](../../RESEARCH_RETENTION_PROTOCOL.md). This is an editorial clarification of the existing two-path behavior; no model, numerical policy or format change.
