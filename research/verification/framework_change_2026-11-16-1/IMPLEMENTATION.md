# Implementation · CR-2026.11.16-R1 · 16 November 2026

Prompt 8 at P-2026.11.15-v24.18, LOCAL_WORKING_TREE, base HEAD `4e60611bc`. Classification: bug fixes that change no forecast and no recorded score, plus records. Method MDS-2026.11.15-v24.20, prompt suite P-2026.11.15-v24.18 and scoring SCV-2026.11.15-v15 are unchanged. Proposal and everything not implemented: [CHANGE_PROPOSAL](CHANGE_PROPOSAL.md). Audit: [report](../retrospective_2026-11-16-1/RETROSPECTIVE_REPORT.md).

## Repairs

| # | File | Defect | Before | After |
|---|---|---|---|---|
| 1 | `ml/audit_controls.py` | The plus-handicap rule looked only at family HANDICAP. | A first-half, period or corners handicap above zero (side HOME or AWAY with a line) passed without an opponent-strength check. | Any priced side line above zero in HANDICAP, PERIOD, CORNERS or OTHER needs `opponent_check: CHECKED` with its evidence. Totals and minus handicaps are unaffected. |
| 2 | `ml/timing_corrections.py` | A correction's binding hashed whatever columns the ledger frame had. | Adding or reordering a column would have made every earlier first-play correction read as stale and stopped ledger scoring. | The binding covers the ledger's registered columns in registered order. For today's ledger the hash is identical, and no correction existed, so nothing is rebound. A frame missing a registered column is refused. |
| 3 | `ml/timing_corrections.py` | The lock file was never recovered. | A crashed correction left `TIMING_CORRECTIONS.lock` and every later correction failed with a bare FileExistsError. | A lock older than 600 seconds is removed once; a younger one is refused with a message naming the file. |
| 4 | `ml/learning_status.py` | Reviews logged with level USER_REQUEST were ignored. | The clocks said the last review was 16 October although the owner-requested review of 21 October is in REVIEW_LOG. | An owner-requested review of a scope resets that scope's clocks (AUDIT-ANYTIME-v1). |

Document repairs: PROMPTS.md named suite v24.14 and now points to the index without a version of its own; CURRENT_STATE named the 11 October retrospective as the latest and now names this audit. research/learning_status/README.md records how an on-request review is logged.

## Tests

- `test_plus_handicap_check_covers_period_and_corner_side_lines_but_not_totals`: three plus side lines refused, two totals and one minus handicap accepted.
- `test_binding_ignores_extra_frame_columns_and_a_dead_lock_is_recovered_but_a_live_one_refuses`: extra and reordered columns keep the binding; a missing registered column is refused; a fresh lock refuses and leaves no correction; an old lock is cleared and the correction appends; the ledger bytes are unchanged.
- `test_learning_counters_and_review_clocks_by_sport_and_competition` extended: a USER_REQUEST review of ALL resets INTERIM and COMPREHENSIVE and leaves the sport clock alone.
- Full suite: see the commit message for the count.

## Records

- REVIEW_LOG.csv: four appended rows for this audit (ALL — DATA_REPAIR_REQUIRED; Baseball/MLB, Ice Hockey/NHL and Basketball/NBA — INSUFFICIENT_EVIDENCE).
- HYPOTHESIS_REGISTER.md: a dated amendment registering H-NODIR, H-BAND, H-AVAIL-CHAT, H-OWN-EVIDENCE, H-SPORT and H-PERIOD as PROPOSED_NOT_TESTED and recording M-1 as awaiting an owner decision.
- CHANGELOG.md and CURRENT_STATE.md: one entry and two pointers.
- Originals of the five changed documents: [https://github.com/danisgreat/Sports-Research/blob/8f2f38faf2dda46986c20df3d503f4f8115e225b/archive/superseded_2026-11-16-1](https://github.com/danisgreat/Sports-Research/blob/8f2f38faf2dda46986c20df3d503f4f8115e225b/archive/superseded_2026-11-16-1/README.md). Changed code keeps its originals in git history.

## Not done, and why

- No card, grade, settlement, forecast, selection rule, parameter or model was changed (FREEZE-v1, STATFREEZE-v1).
- The measured-card design (M-1 to M-6), the FACTS block (L-2) and every format change wait for an owner order.
- The unresolved queue was not retried and Part 10 was not rolled over; neither was asked for.
- The review clock still counts store results (L-4 is proposed, not built).

## Rollback

Revert this commit. No other artifact depends on it.
