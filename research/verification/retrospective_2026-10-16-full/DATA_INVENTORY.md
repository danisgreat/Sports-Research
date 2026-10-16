# Data inventory — full-history retrospective 2026-10-16 (P-001 to P-600)

## 1. Scope

Fixed from the user's instruction ("every card from the first card, P-001, to the most recent one") before any cohort arithmetic; written 2026-10-16T21:06+11:00.

| Item | Value |
|---|---|
| Repository / branch / HEAD | `danisgreat/Sports-Research` · `main` · `b86f89d3718a1fae9780303fef5a7e4b3c9b0558` (equal to `origin/main`) |
| Working-tree state at start | Unrelated `.gitignore` edit. During the run, **another session modified `GAME_PREDICTION_RANK_LOG.csv` in the working tree** (an uncommitted refresh to P-600 with its own receipt in `research/verification/rank_log_update_2026-10-16/`). That work is not this review's and was neither used nor staged. This review reads the **committed** rank log (blob SHA-256 `97944264…292322` at `b86f89d37`) |
| Authority | LOCAL_WORKING_TREE · MDS/P v19.1 → v19.2 (this change) · CR-R5 → R6 · SCV-2026.10.16-v11 · SEL-2026.10.12-v3 · LEARN-v1 → v1.1 |
| Trigger and level | User request. LEARN-v1 counters 0 (store empty; INTERIM/COMPREHENSIVE `NOT_DUE`). Content level COMPREHENSIVE: every sport, every card |
| IDs | P-001–P-600: 599 card records in the table (P-584 `PENDING_EVENT` excluded by design); 570 with at least one graded row; 562 with graded counted slots; 29 with no gradable row (administrative/no-scored-trial 16, alias/reserved/not issued/blocked/unrecovered and similar 13) |
| Event dates | 2026-07-29 to 2026-10-16. Dates from the first ISO date in each card's original block (467 cards), else the nearest date to its grade-source line (50) or to its first mention (81); 1 undated (P-320); the status-register fallback supplied none |
| Eras (date windows following documented policy changes) | E1a ≤ 2026-09-08 (297 graded cards); E1b 09-09 to 09-24 (189); E2 09-25 to 10-08, q-ranking and Markdown-only period (39); E3 10-09 to 10-11, v9 P_ORDER ceiling ladder and gate (28); E4 ≥ 10-12, v10/v11, supplied-first and legacy V3-era research (16) |
| Cohorts | `RANK_LOG_LITERAL` (P-001–P-583, literal ranks and grades); `SUPPLIED_FIRST_V1` (P-585–P-589); `LEGACY_ORIGINAL_RANK` (P-590–P-592 original ranks); `LEGACY_ANALYST_NOT_PRIMARY` (P-593–P-600 analyst rows, never counted) |
| Grades (2,311 rows) | WIN 1,284 · LOSS 950 · UNRESOLVED 47 · CONFLICT 11 · PUSH 11 · VOID 8 |
| Stated p | 837 graded rows on 214 cards (38% of graded cards); E1a 9 of 297 cards, E1b 144/189, E2 26/39, E3 27/28, E4 14/16 |
| Frozen same-row baselines | 4 events in the entire history (P-581, P-582, P-587, P-589), all in E3–E4 |
| Model lanes | V1/V2/V3 primary bundles issued: 0. Prospective model shadows frozen: 0. Workshop `-r1` outputs: historical development only |
| Comparisons | 2026-10-09 full history (522 cards, literal grades); 2026-10-11 and 2026-10-16 cohort retrospectives |
| Prior exposure | Fully outcome-exposed. The analyst ran the 2026-10-16 cohort review earlier the same day and had read the 2026-10-09 history figures |

## 2. Reading receipt

```text
READING RECEIPT
Repository / branch / HEAD SHA: danisgreat/Sports-Research · main · b86f89d3718a1fae9780303fef5a7e4b3c9b0558 · read 2026-10-16T20:52–21:06+11:00
Controls: research/prompts/6_COMBINED_LOG_RETROSPECTIVE.md (supplied by the user, identical to v19.1) · COMMON_OPERATING_PROTOCOL · LEARNING_PIPELINE_PROTOCOL §§6–8 ·
  CURRENT_STATE · CURRENT_RULES · SCORING_AND_VALIDATION · HYPOTHESIS_REGISTER (FC10, Retrospective 2026-10-11 and 2026-10-16) · PRIMARY_PREDICTION_PROTOCOL
Completed retrospectives: retrospective_2026-10-16 (same day, full), retrospective_2026-10-11 (full),
  archive/root_documents_2026-10-14/FRAMEWORK_RETROSPECTIVE_2026-10-09.md (§§1–3, failure classes)
Records: GAME_PREDICTION_RANK_LOG.csv (committed blob) · HISTORICAL_PRIMARY_RECONCILIATION.csv · the three import row inventories ·
  GAME_LOG_STATUS_CURRENT.md · prediction logs/PREDICTION_LOG_COMBINED*.md parts 1–7 (headings, dates and grade-source lines read by the tool; not every card body read)
Not used: research/SETTLED_OUTCOMES_LEDGER.csv (register summary with no probabilities or ranked results); the uncommitted rank-log refresh
GitHub fallback: not needed
```

## 3. Construction and checks

`python -m ml card-history --rank-log <committed rank log> --out HISTORY` produced [HISTORY/CARD_ROWS.csv](HISTORY/CARD_ROWS.csv) (one row per card × original rank, 2,311 rows) and [HISTORY/CARD_HISTORY.md](HISTORY/CARD_HISTORY.md), with a receipt of every input hash and the code hash.

- **Effective grades.** Ten rank-log rows disagree with the effective 2026-10-09 final settlement (eight UNRESOLVED and two PUSH literals that the effective table grades). The effective grade wins for Ranks 1–2; the list is in CARD_HISTORY.md.
- **Reproduction.** Applied to P-001–P-522, the table reproduces the 2026-10-09 full history to within those corrections: Rank 1 307–186 against 304–187, Rank 2 253–209 against 251–211.
- **Sport classification.** Explicit "Sport /" labels come first, then club and keyword rules; 9 manual overrides are made where the players or clubs identify the sport. Six cards stay UNCLASSIFIED rather than guessed. A first random audit of 25 cards found 3 errors, which were fixed; a fresh random audit of 30 cards then found 0.
- **Family classification.** Keyword rules: corners, cards, period, player, BTTS, handicap, total, winner. Rows without contract text are OTHER.
- **Identity collisions.** 21 IDs carry two different events in their original headings: a shifted block P-139–P-153, plus P-155, P-156, P-160, P-272, and P-370/P-415 (closed administratively, later reused). The rank log holds one event per ID. Every headline is repeated with these IDs excluded.
- **Calibration study.** [CALIBRATION/CALIBRATION_RECEIPT.csv](CALIBRATION/CALIBRATION_RECEIPT.csv) on [CARD_PREDICTIONS.csv](CARD_PREDICTIONS.csv). Issue time is taken as the card date and outcome availability as one day later; date resolution only.
