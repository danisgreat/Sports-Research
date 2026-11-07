# Verification — settlement revisions import 2026-11-07

| Check | Result | Evidence |
|---|---|---|
| Frozen sources unchanged | PASS | 79B3 `ORIGINAL_MINI.md` 313,155 bytes `b7478342…ad7e`; X7Q4 `ORIGINAL_MINI.md` 150,699 bytes `8bca9a3e…2748`; both equal the 2026-10-21 FROZEN_SOURCE_RECEIPTS (re-hashed on LF bytes before any write) |
| Owner drop fully reconciled | PASS | 14 of 14 files byte-identical to retained 2026-10-21 inputs ([OWNER_DROP_RECONCILIATION.csv](OWNER_DROP_RECONCILIATION.csv)); no card, addendum or revision in the drop lacks a canonical or documented disposition |
| Identity | PASS | Highest P-622, next P-623, reserved P-518–P-522 unchanged; 0 IDs consumed; 3 units are revisions of existing events |
| Revision chains | PASS | P-604 revision-3 → parent revision-2; P-606 revision-2 → parent revision-1; P-620 revision-2 → parent revision-1; unique keys; no branch |
| Pre-mutation recheck | PASS | HEAD `749bca06d…8815`; Part 9 5,070 bytes `7796d904…7610` = committed blob, immediately before the append |
| Append-only | PASS | Post-append prefix equals the pre-append bytes in full; Part 8 untouched (closed part) |
| Readback | PASS | Each of the 3 wrapped cores re-hashed at its destination offset ([IMPORT_READBACK.csv](IMPORT_READBACK.csv)) |
| Markers | PASS | Part 9: 3 BEGIN/END RESEARCH ADDENDUM pairs, balanced, unique, no nesting; the header-end marker is standalone by design, as in Part 8 |
| Line endings | PASS | Part 9 and the new documents are LF only; `GAME_LOG_STATUS_CURRENT.md` is committed `-text` with mixed endings, and its new lines are LF appends |
| Retained copies | PASS | Both revision documents in `inputs/` are byte-identical to `research/active_minis/` ([SOURCE_FILE_INVENTORY.csv](SOURCE_FILE_INVENTORY.csv)) |
| Grades | PASS | Only the two P-604 corner rows changed (UNRESOLVED → WIN/LOSS); every other row is as before; P-606 and P-620 grades unchanged |
| Counts | PASS | P-601–P-611: 26 + 26 + 0 + 0 = 52 rows; P-612–P-622: 25 + 23 + 2 + 0 = 50 rows; primary 11W/10L/1P |
| Hard rule (no prices) | PASS | No price, line or odds page was opened or cited; every statistics page was used for the named field only |
| Timing | PASS | Effective time read from the clock (2026-11-07T20:53:07+11:00); retrievals bounded "before 20:48:26 AEDT" (clock read after them), not estimated |
| Repository tests | see report | `python -m pytest ml/tests` result recorded in the commit message |
