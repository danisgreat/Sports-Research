# PROMPT 5 — Roll over the Combined Log without consuming IDs

**Mode:** COMBINED_LOG_ROLLOVER. Input: user request or documented trigger. **Default triggers (R21; calibrated 2026-10-12 against the existing parts, which rolled over at 0.4–1.3 MB, and Part 7 at 1.26 MB with 30 entries):** whichever comes first of the active part's working file exceeding 1.5 MB, holding 50 or more canonical entries, or a reader reporting that it will not open or render reliably. Record which trigger applied, with the measured size, count or failure. A rollover is never required to settle or import anything. Run between imports, never over a partial import. Writes: current log closure, one new part, CURRENT_STATE, current GAME_LOG_STATUS_CURRENT pointer, explicit live pointer documents if needed, CHANGELOG and a new rollover report. No forecast, settlement, duplicate card or ID allocation.

## 1. Read and reconcile

Print the [reading receipt](README.md) after common controls, template §8, VERIFICATION_PROTOCOL §4, status, active/previous log opening and closure records, current entry tail and this prompt. Record branch/HEAD/status; preserve unrelated changes. Resolve active Part N from CURRENT_STATE and current status against actual entries. Opening ranges and IDs are historical snapshots, not claims of today's state.

Inventory pending/evidence queues, highest canonical ID, next ID, current part's actual canonical entries and unresolved import plans. Block rollover until any half-import is resolved. Record the full original old-part bytes for comparison; verify exact proposed Part N+1 path without relying on lexicographic filename sorting.

## 2. Plan and apply

If exact rollover already exists and current pointers match, return ALREADY_COMPLETED with zero writes. A partially created new part/closure requires scoped recovery by comparison; never overwrite an occupied file or create Part N+2 to hide the conflict.

Append a dated closure to Part N: closure time/HEAD, actual contained ID range and entry count, highest global ID, unchanged next ID, both queue pointers, prior byte/line counts if measured, and link to Part N+1. Preserve every old byte.

Create Part N+1 with title, ACTIVE status, opening time in Sydney/UTC, actual method/control/scoring/HEAD, explicit OPENING_SNAPSHOT label, previous part/continuity links, reserved-ID note, global highest/next ID unchanged, pending and evidence queues, research-only/market-blind labels and canonical-md-1 append/addendum rules. End header with `<!-- END ACTIVE COMBINED LOG HEADER -->`. No placeholder forecast/card.

Recheck immediately before the closure append and again before creating the new part (R18). HEAD, the active path, the old part's byte count and SHA-256 and the next ID must match the plan; otherwise stop and re-plan. After rollover, later settlement revisions and addenda for cards in the closed part are appended to the **new active part**, with a pointer to the original part and revision key (template §8, R21). The closed part is never edited.

Update only current destination pointers and append the changelog/rollover receipt. Prefer dynamic CURRENT_STATE references to more hard-coded active filenames; historical links remain unchanged. Do not alter an old opening header to make it look current.

## 3. Verify, publish, report

Compare full old prefix exactly; inspect suffix/diff endings; next ID identical; new part has zero canonical blocks; one closure/new part; continuity links work; current status/state agree; queues retain every item. Verify scope against the initial dirty inventory.

Commit scoped changes and push without force when this full prompt is invoked unless user limits to local work; fetch and verify remote SHA and pointers. Return old/new paths, entry counts, preserved-prefix evidence, unchanged next ID, zero IDs consumed, queue counts, checks, commit and remote publication status. A failed check means rollover NOT_COMPLETE.
