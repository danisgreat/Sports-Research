# Implementation · v26.0 / CR-2026.11.16-R3 · 16 November 2026

Prompt 8, LOCAL_WORKING_TREE, base main `d8080da60`. Owner order: "i need the demonstrated predictive advantage to be fully implemented, and any other improvements as needed", after an independent review of v25.0 (6/10; demonstrated advantage "Unproven"; six reproduced defects). Classification: measurement policy + PROCEDURE, so method, prompt and scoring versions move: MDS-2026.11.16-v26.0, P-2026.11.16-v26.0, SCV-2026.11.16-v17. The card format (`ONECHAT_V1`) is unchanged; two timing rules inside it are now enforced.

## What "fully implemented" can and cannot mean

A predictive advantage cannot be written into code; it exists only if the cards beat the comparator on games whose results were unknown when the numbers were fixed. What is implemented is everything needed for that claim to be made, checked and decided:
- a custody chain a reader can verify: GitHub's own push time before first play, committed inputs and re-hashed captures;
- an eligibility rule that cannot be gamed by repetition or relabelling;
- a decision rule that stays valid however often it is read, and can say DEMONSTRATED as soon as the evidence allows.

No game has been sealed yet, so the current verdict is NOT_YET_DEMONSTRATED with 0 games.

## The review's six defects

| # | Finding | Fix | Test (ml/tests) |
|---|---|---|---|
| 1 | One game in 100 intakes reached READY and met the criterion | Cards are joined across every scored intake by game identity and by the outcome rows' `event_id` (native match identity); the first sealed card is the card of record | `test_review_defect_1_one_game_in_a_hundred_intakes_counts_once`, `test_review_defect_1b_respelled_teams_are_one_game_when_the_settled_event_is_one` |
| 2 | A two-card cohort reached READY | The first 100 are frozen once with COHORT_RECEIPT.csv (hash, count); a supplied cohort must match its receipt, hold exactly 100 distinct games and be committed; a second freeze is refused | `test_review_defect_2_a_supplied_cohort_must_be_the_frozen_hundred`, `test_a_sealed_skilled_sequence_is_demonstrated_and_the_first_hundred_freeze_once` |
| 3 | Edited intake probabilities and a fabricated capture hash were accepted | Intake writes MANIFEST.csv; scoring checks every file against it and requires intakes, outcomes and cohort to be committed unchanged (else NOT_ASSESSABLE); each capture is re-hashed from `final_capture_path` | `test_review_defect_3_edited_intakes_uncommitted_outcomes_and_invented_captures_are_refused` |
| 4 | Facts after research end, and a not-started check before research start, passed | Intake requires both inside [research_start_at, research_end_at]; scoring requires every clock and fact at or before first play, and the research end before the seal | two new cases in `test_incomplete_or_incoherent_cards_are_refused_with_the_reason`; `K6` in the custody test |
| 5 | Whole-number lines left push mass unscored | Each side scored on p ÷ (sum of the line's sides), the W/(W+L) rule | `test_review_defect_5_whole_number_lines_are_scored_on_the_probability_given_no_push` |
| 6 | An aged lock held by a live writer could be taken over | `ml/timing_corrections.py` uses an operating-system lock (msvcrt or flock) released only when the holder exits; a leftover file is not a lock | `test_binding_ignores_extra_frame_columns_and_a_live_lock_is_never_taken_over` |

## Added

| Piece | What it does | Where |
|---|---|---|
| Seal | Validates the card file, copies it to `research/one_chat/sealed/`, appends SEALS.csv, commits, pushes and records GitHub's server push time (activity API) in PUSH_RECEIPTS.csv | `ml one-chat seal` |
| Receipts | Mirrors GitHub's push record for main | `ml one-chat receipts` |
| Custody classes | SEALED_PRE_START_SERVER (eligible); SEALED_PRE_START_CLIENT, SEALED_AFTER_START, SEALED_NOT_PUSHED, UNSEALED, CLOCK_INCONSISTENT, POST_START, OUTCOME_EXPOSED (reported, never counted) | COVERAGE.csv |
| Sequence | Eligible games ordered by scheduled start, cut at the first sealed, fully priced card still unsettled | SEQUENCE.csv |
| Verdict | Betting e-process on d = 0.25 − Brier: DEMONSTRATED at e-value 20 with mean d at least 0.01 within 400 games; 95% anytime-valid lower bound; per sport at 220 | SUMMARY.csv, SPORT_EVIDENCE.csv |
| History | The same test on historical cards, labelled not confirmatory | `ml one-chat history` |

**Simulation before registration** (500-game sequences):

| Case | Crossed | Note |
|---|---|---|
| Mean-zero null | 5 of 400 | |
| Coin-flip results, card states 55–75% | 0 of 200 | |
| Calibrated card favouring sides at 55–65% | 59% within 400 games | median 327 |
| Calibrated card favouring sides at 58–72% | 99% | median 176 |
| Calibrated card favouring sides at 62–78% | 100% | median 92 |

The bet cap (0.75) was chosen from 0.5, 0.75 and 0.9 on these runs, before any real game.

## Historical context

`historical_evidence/HISTORICAL_EVIDENCE.csv` (from CARD-TRAIN-v1 run 2026-11-16-1):

| Cohort | Result | Mean d | Lower bound |
|---|---|---|---|
| All 280 cards with stated p | e-value 59, crossing at card 198 | +0.020 | +0.005 |
| 31 chat-research cards on supplied lines (P-639 onward) | e-value 1.0 | +0.0015 | −0.0945 |

Neither result counts toward the registered claim. The cards were never sealed, they mix policies and line types, and this analysis was chosen after the results were known.

## Verification

- `ml/tests/test_one_chat.py`: 32 tests, including the error-rate and power checks, the custody classes, the held-back sequence, sealing (refusal, no re-seal, clean tree) and the six defect reproductions. Each test runs against a temporary git repository with a bare origin and a stand-in for GitHub's push record.
- Full suite: count in the commit message.
- Not testable offline: the live GitHub activity API call. It was exercised against this repository on 16 November 2026, and `PUSH_RECEIPTS.csv` was started from it.

## Not changed

- Every issued card, grade, canonical ID and earlier registration.
- The card format and the chats' kit.
- The six hypothesis flags.

v25.0 brief and plan files are retained.

## Rollback

Revert this commit. Sealed files, receipts and score folders written later stay readable as records.
