# Implementation following the full-history retrospective (P-2026.10.16-v19.2 / CR-2026.10.16-R6 / LEARN-v1.1)

**Instruction (owner, 16 October 2026):** "can you run prompt 6 on every card from the first card, P-001, to the most recent one … and implement whats necessary". Authority LOCAL_WORKING_TREE, base `b86f89d3718a1fae9780303fef5a7e4b3c9b0558`. Class: PROCEDURE (prompt minor bump) plus workshop code under `ml/`. PRIMARY_HEDGE_MIX_V3, selection, scoring, formats, IDs and issued records are unchanged.

**Concurrent work.** During the run another session modified `GAME_PREDICTION_RANK_LOG.csv` and added `archive/rank_log_2026-10-16/` and `research/verification/rank_log_update_2026-10-16/`. Those files are not part of this change, are not staged, and were not used. This review reads the committed rank log.

## What the findings required, and what was built

| Finding (report §) | Necessary change | Implemented |
|---|---|---|
| No model ever priced a card; 7 cards record only `No module named ml` (§2.4) | A receipt proving what the environment can run, plus a bootstrap step, before any ML_NOT_RUN | `ml/capability.py` (`python -m ml capability [--out]`). Prompt 1, all eleven workflows: capability receipt, pinned-SHA checkout plus `pip install -r ml/requirements.txt` retry, every command and error recorded in A9. CURRENT_RULES R36 |
| 4 baseline-paired events in 600 cards (§2.3, §3.8) | A same-line comparator that does not depend on the full V3 run | `ml/league_baseline.py` (`python -m ml baseline`): BASELINE_LEAGUE_V1 from reviewed horizon-admitted history, **tested equal to V3's LEAGUE_BASELINE `baseline_p`**. Prompt 1 requires it when V3 cannot price an event |
| Shadow ledger empty forever; tennis primary not implemented (§5) | A path from real model bundles to frozen shadows | `rows_from_primary_bundle` / `rows_from_tennis_bundle` and `python -m ml prospective rows`. Rows are `PRE_START_VERIFIED` only when issued and converted before the start, otherwise `TIMING_UNVERIFIED`; tested through `freeze`. Prompt-1 tennis workflow freezes TENNIS_EXPERIMENTAL_HEDGE_V1 as a prospective shadow |
| Ambiguous supplied contracts (P-577, P-596, P-598) | A definition gate | Prompt 1, all eleven workflows: unit, period and action stated before pricing; an ambiguous text is priced and frozen under every reading and queued |
| Prompt-6 counts rebuilt by one-off scripts each time | A reproducible tool | `ml/evaluation/card_history.py` (`python -m ml card-history --rank-log … --out …`). It joins the rank log, the effective grades and the import inventories. It assigns date, era, sport and family, flags ID collisions, and produces slot, class, calibration and Rank-1 dependence tables with a collision-excluded sensitivity. Inventory rows are appended only for cards absent from the rank log, so the pending refresh will not be double counted. Prompt 6 now uses it |

**Not implemented here, by design:**
- **RET-14** (ID-collision repair) needs prompt-7 work on original bodies.
- **RET-15** (history backfill into the learning store) needs field-owner re-verification of every result.
- **RET-16** is a monitoring test that becomes possible once baselines are frozen.
- **No recalibration:** the chronological study found that none transfers out of sample.
- **No selection-rule change:** sport and band findings need frozen comparisons first.

## Files

- **Code (`ml/`):** `capability.py`, `league_baseline.py`, `evaluation/card_history.py` (new); `evaluation/prospective.py` (bundle adapters, `rows` command); `run.py` (dispatch for `capability`, `baseline`, `card-history`).
- **Tests:** `tests/test_card_history_tools.py` (sport/family rules, literal grades and eras, repository invariants, effective-grade precedence, collision detector, Rank-1 tests, capability receipt, baseline equality with V3, adapters through freeze). `tests/test_prompt_consistency.py` now also requires the runtime paragraph to be identical in all eleven workflows and the tennis shadow step to appear once.
- **Documents:**
  - Prompt 1: one identical paragraph in each of eleven workflows, the tennis sentence, and the header version.
  - Prompt 6: a card-history section.
  - Prompt README: the v19.2 section.
  - LEARNING_PIPELINE_PROTOCOL §10 (v1.1), PRIMARY_PREDICTION_PROTOCOL §7 note, CURRENT_RULES R36, ml/README.
  - CURRENT_STATE: current release, versions table and learning row.
  - Version-only alignment in the remaining controls.
- **Originals:** archived byte-for-byte from HEAD in `archive/superseded_2026-10-16-7/` with `ARCHIVE_HASHES.csv`.
- **Review outputs (this folder):** DATA_INVENTORY, RETROSPECTIVE_REPORT, HISTORY/ (generated), CALIBRATION/ (generated), CARD_PREDICTIONS.csv.
- **Summaries:** REVIEW_LOG rows, HYPOTHESIS_REGISTER dated lines and RET-14–RET-16, scoreboard section, CHANGELOG.

## Verification

- **Prompt 1:** all eleven owner-entered Upcoming blocks are byte-identical to HEAD (block checker).
- **Tests:** `python -m pytest ml/tests` gave **395 passed in 190.13s** (367 before this change plus 28 new), run after the last `ml/` source change.

**Timestamp correction (disclosed, not rewritten).** The eight review-log rows committed in `b86f89d37` (cohort retrospective P-577–P-600) carry `recorded_at` 2026-10-16T20:45:00+11:00. That was a pre-filled value: the commit itself was made at 20:35:59+11:00, so the rows were recorded before 20:35:59. REVIEW_LOG is append-only and `recorded_at` drives no trigger (`through_at` does), so the committed rows stay as published and this note is the correction. The twelve rows added here carry the actual write time (21:07:45+11:00), and this folder's file times were checked against the clock.
- **Generated artifacts:** `HISTORY/` and `CALIBRATION/` were generated after the last `ml/` source change, and their receipts carry that code hash.
- **Not verified:** no external source was fetched, and no sporting grade or historical record was changed.
