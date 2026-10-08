# Duplicate and reference reconciliation — 2026-10-09

Source: `inputs/RECONCILIATION_INVENTORY.csv` (72 rows) cross-checked against the repository after import.

## Seven new events (LOCAL_UNIMPORTED_EVENT → canonical)

| ID | Before import | After import |
|---|---|---|
| P-550..P-556 | no card heading, no ledger record, no `ISSUE_*` record for the native event (P-550 `2026020055`, P-553 `506439`, P-554 `506440`); allocator `next-id` P-550 | exactly one canonical card heading each in Combined Log 7, one PREPARED+COMMITTED pair each, one addendum pair each; allocator `next-id` P-557 |

Checks: no heading ID appears more than once in Combined Log 7; the allocator's own event-key and native-event guards found no existing issuance; each card and addendum marker block occurs exactly once in the log and is byte-equal to its retained projection. Zero duplicates created.

## 65 older carryover reviews (ALREADY_CANONICAL_REFERENCE) — reconciled by reference only

* Not re-imported, not rewritten. `carryover.json` has 65 records whose ID set equals the inventory's 65 `ALREADY_CANONICAL_REFERENCE` rows exactly.
* Combined Log 7 is **append-only** for this import (884 insertions, 0 deletions), so the earlier carryover review text there is byte-unchanged.
* 27 of the 65 (P-523..P-549) are committed canonical research cards in the ledger. The rest are older IDs whose cards live in earlier Combined Logs (58 IDs have a heading in exactly one prediction-log file, 1 in two). Six IDs (P-217, P-234, P-235, P-341, P-342, P-430) have no heading-form entry but are referenced in the logs (193 mentions across 7 files); this is a pre-existing property of those records, unchanged here.
* No new grade was assigned to any of the 65 (`NO_NEW_GRADE_FROM_2026-10-09`); their unresolved sporting/operator/certification obligations carry forward unchanged (see `UNRESOLVED_POST_IMPORT.md`).

## Identity mapping

The packet's `LOCAL_ID_MAPPING.md` lists P-550..P-556 as `LOCAL_WORKING_ID — PENDING_IMPORT` with no fresh allocations. The allocator issued the same numbers, so every local ID maps to the identical canonical ID (`CANONICAL_ID_MAPPING.csv`); no renumbering and no collision. Local next working ID P-557 coincides with the repository next canonical ID P-557.
