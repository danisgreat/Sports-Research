# Receipt: GAME_PREDICTION_RANK_LOG.csv extended to P-583 (2026-10-14)

**What changed.** 241 rows (61 cards, P-523 to P-583) were appended to [GAME_PREDICTION_RANK_LOG.csv](../../../GAME_PREDICTION_RANK_LOG.csv). The first 1,523,097 bytes (2,004 rows, P-001 to P-522, UTF-8 BOM, CRLF) are unchanged and remain an exact prefix. The file now has 2,245 rows and 583 cards, contiguous from P-001 to P-583.

**Why P-583.** It is the highest canonical ID with a terminal result in [GAME_LOG_STATUS_CURRENT.md](../../../GAME_LOG_STATUS_CURRENT.md). P-584 is `PENDING_EVENT` (no result), so it is not in the file. Next to add: P-584 once settled, then P-585 onward.

## Where each row comes from

One row per ranked contract in the settlement table of the card's own settlement block in [Combined Log Part 7](../../../prediction%20logs/PREDICTION_LOG_COMBINED_7.md). Nothing is recomputed.

| IDs | Settlement source in Part 7 | Card (for p) |
|---|---|---|
| P-523 to P-537, P-550 to P-556 | Dated addendum "Final settlement (2026-10-09)" | Part 6 (P-523 to P-537), Part 7 (P-550 to P-556) |
| P-538 to P-549 | "Final settlement · P-xxx" entries in the 2026-10-09 final-settlement block | Part 6 |
| P-557 to P-576 | `SETTLEMENT P-xxx` in the 2026-10-11 import addenda | Part 7 |
| P-577 to P-583 | `SETTLEMENT P-xxx revision-1` (2026-10-13) | Part 7 |

Column rules (same as the existing rows unless noted):
- `logged_result` W / L from WIN / LOSS. `rank_pass_fail` PASS / FAIL.
- **New codes:** `V` with `rank_pass_fail` = `VOID` on 6 rows: P-523 rank 5 (corners with no line) and P-537 rank 4 (corners, no data in any source), both informational ranks; and P-540 ranks 1 to 4 (a tennis retirement voids the games rows under RULES_TENNIS). The old file only had `V` inside a conflict value (`L/V`).
- `stated_p`, in order of preference: the settlement table's `p_card`; the card's own rank table (or `Rank N … p_card` heading); the Rank 1/2 "Claim" line of a deep retrospection. **Blank on 62 rows**: P-525 to P-531 and P-533 to P-540 (qualitative cards or `NOT_ESTIMATED`; P-528's summary did not retain p), plus the undefined corners row P-523 rank 5.
- `ranking_q`: filled only where the card printed an RM-1 q (4 rows). Cards from P-557 onward carry none.
- `lesson_next_time`: the retrospection's "Proposed correction" where one exists. Otherwise the card's R11 hypothesis, **prefixed "Hypothesis (PROPOSED_NOT_TESTED)"** because it is a proposal, not a verified lesson. Blank on 88 rows with neither.
- `grade_source` is the log line of the settlement-table row; `status_source` is the line of the card's row in GAME_LOG_STATUS_CURRENT.md.
- **P-532 and P-583** issued no ranked forecast: one `NO_SCORED_RANK` row each (rank blank). P-532's shadow-order outcomes are in `notes`. P-583's source conflict (KT 4-2 per wire and club, 4-1 per a stale detail page) is in `source_claim_or_conflict`. P-581, P-582 and P-583 also carry the open evidence tasks of the 2026-10-13 register.
- `record_status` says "FINAL / SETTLED <date>" with `NOT_CERTIFIED`. P-577 to P-583 are sporting settlements with operator terms unknown. No row is performance-certified.

## Checks (2026-10-14)

| Check | Result |
|---|---|
| Original rows unchanged | Exact byte prefix: PASS |
| Row and card counts | 2,245 rows, 583 cards, 0 duplicate (card, rank, contract), 0 ragged rows, 0 control characters |
| Rank 1 and Rank 2 grades against the 2026-10-09 report's per-record table (P-523 to P-556) | 34 of 34 cards with a table agree. The exception is P-532, where the report shows shadow grades for a no-forecast card |
| Top-two class against the status register (P-557 to P-583) | 26 of 26 agree |
| Counted wins, P-557 to P-576 | 34 wins in 40 live rows, as in CURRENT_STATE |
| P-577 to P-579; P-580 to P-582 | 5W/1L each, as in CURRENT_STATE |
| Cited lines | All 241 `grade_source` lines hold the same rank and proposition; all `status_source` lines hold the card's register row |

## Limits

- The earlier 2,004 rows were **not** touched. Some are `UNVERIFIED` or `QUARANTINED_SOURCE_CLAIM` (for example P-519 to P-522), although the 2026-10-09 final settlement in Part 7 later settled P-126 to P-522 (50 records, including a corrected P-519). A refresh of those rows is a separate step.
- The file is a learning artefact (ARCHIVE_USE_GUIDE section 1). It is not an official record, and its win rates are descriptive, not prospective evidence. Rank 1 and 2 counts reflect each card's covering-pair construction where the settlement says so.
- Evidence grades differ by row (A owner, B structured, C best-available, OP operator default, X no data): see `notes`.
- The extraction ran from a helper outside the repository (CONTRIBUTING). Its rules are the column rules above.
