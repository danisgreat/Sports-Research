# Framework change 2026-11-10-1 — records and versions aligned (MDS v24.11 / CR-2026.11.10-R1)

**Owner instruction, 10 November 2026.** After a full log audit found nothing left to settle, the owner approved fixing the five record-keeping findings and writing a deep loss review for P-633.

**Class.** PROCEDURE (records and versions only). No issued card, grade, probability, rank, canonical ID, method, model, release or selection rule changes. No Python changed. Versions: method MDS-2026.11.10-v24.11, control CR-2026.11.10-R1, prompts P-2026.11.10-v24.9.

## What the audit found to be complete

All 638 cards have rows in the generated history (2,549 rows). The active mini has no cards and no league-day event is unsettled. Every issued local key maps to a canonical ID. Seven unmapped keys are next-key footers or cards that were never issued. Part 9 had only additions since 8 November and Parts 1–8 were untouched. Every deep loss review required by DEEPLOSS-v1 on the cards settled or revised under it is present.

## Changes

| Finding | Change | File |
|---|---|---|
| Scoreboard stopped at 7 November | New dated section for P-584 and P-623–P-638, using effective grades; earlier sections unchanged | [SCOREBOARD](../../scoreboard/SCOREBOARD.md) |
| Hand-kept IDs said P-637 / P-638 | Now P-638 / P-639, matching the generated block and the status file | [CURRENT_STATE](../../../CURRENT_STATE.md) |
| Be1–Neptunas corners shown as unresolved | Now shown as permanently closed; the dated R3 note stays, with a superseding bullet above it | [CURRENT_STATE](../../../CURRENT_STATE.md) |
| Three 9 November commits without a version bump | v24.11 / P v24.9 now identify the prompt 1 research-coverage section and reporting code | CORE, README, PROMPTS, CURRENT_STATE, CHANGELOG, 22 prompt files |
| Active mini header stale, lease ending 15 November | Dated section D gives current versions and the current open-item pointer, and extends the lease seven days to 2026-11-22T21:10:10+00:00; footer next-ID snapshot is P639; section A is unchanged | [mini](../../active_minis/20261109R3NEXT.md) |
| P-633 had no deep loss review | Owner-requested 14-section review, strict append to Part 9 | [Part 9](../../../prediction%20logs/PREDICTION_LOG_COMBINED_9.md), [append receipt](LOG_APPEND_RECEIPT.csv) |

No card was issued between the unversioned commits and this release, so no card carries an ambiguous version. File names are unchanged: the repository identifies a version by the strings inside its documents, and links and tests depend on the names.

## P-633 trigger status

The review was not required by DEEPLOSS-v1. Soccer's top total is the higher-p of goals and corners; p_card is NOT_ESTIMATED on both, and analyst_p put corners first (0.70873, WIN; goals 0.59541, LOSS). It is labelled TOP_TOTAL_OWNER_REQUESTED. P-637's existing goals review was labelled TOP_TOTAL in the same position (corners 0.645, goals 0.605). The review proposes a prompt 8 clarification; this release does not change the rule.

## Sources for the review

| URL | Site rule check 10 November 2026 | Result |
|---|---|---|
| https://promediosinfo.com/boca-juniors_talleres_2026-10-16_1493185_6WtiEiQi1As.html | ALLOWED | Read. Lineups, goal times and statistics table admitted, evidence C, one collector. No raw body was retained in this run, so no new hash exists; the earlier capture hash is in the [settlement's register](../mini_import_P-629_P-636_2026-11-09-1/SOURCE_DISCOVERY_REGISTER.csv) |
| https://elancasti.com.ar/edicion-impresa/boca-lo-dio-vuelta-talleres-gano-2-1-y-quedo-como-lider-la-tabla-anual-n624061 | ALLOWED | Fetch returned 403. Not admitted, not retried, not reached another way. A search summary of it was not used |

The statistics table has no team labels. Boca must be the first column, because its two goals cannot come from one shot on target.

## Custody

Pre-images of CURRENT_STATE, SCOREBOARD and the active mini are in [archive/framework_change_2026-11-10-1](../../../archive/framework_change_2026-11-10-1/MANIFEST.csv). Part 9 keeps its entire earlier byte prefix ([receipt](LOG_APPEND_RECEIPT.csv)). The REVIEW_LOG is unchanged; its MINI_SETTLEMENT rows wait for prompt 6.

## Limits

Predictive skill remains unproven: on frozen same-row baselines the cards are worse than the league baseline on the small sample available. MLB-CYCLE-4 stays stale and blocked. The learning-status INTERIM, COMPREHENSIVE, Basketball and NBA reviews show DUE because of about 3,700 bulk NBA history rows; they were not run here. Test results are in [TEST_RECEIPT](TEST_RECEIPT.md).
