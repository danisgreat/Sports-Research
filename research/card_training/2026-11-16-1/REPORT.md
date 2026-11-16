# Card-record training run 2026-11-16-1 (CARD-TRAIN-v1)

Run after the settlement revisions import of 16 November 2026 (53 rows moved from UNRESOLVED to WIN or LOSS), as prompt 4 requires. `python -m ml card-training verify --run research/card_training/2026-11-16-1` rebuilds all 2,858 predictions byte for byte. Evidence class HISTORICAL_OUTCOME_EXPOSED_STUDY; nothing is applied to any card (ML-SEP-v1).

## Ingested and admitted

All 685 settled cards, P-001 to P-685: 3,150 rows ingested; 3,082 admitted (1,291 with a stated probability, 1,791 outcome-only with reason NO_STATED_P); 68 excluded (29 UNRESOLVED, 12 UNATTAINABLE, 12 VOID, 10 PUSH, 5 UNDATED). Against run 2026-11-15-2, 53 more rows are admitted because their grades are now settled. The 29 rows still UNRESOLVED are older rank-log rows outside the import queues.

## Walk-forward results (negative favours the model; 95% interval over cards)

| Model | vs | Rows / cards | Brier model / baseline | Card-mean difference |
|---|---|---|---|---|
| Stated p as written | training base rate | 1,067 / 225 | 0.2282 / 0.2456 | **-0.0186 [-0.0294, -0.0079]** |
| Platt recalibration | stated p | 1,067 / 225 | 0.2287 / 0.2282 | +0.0005 [-0.0015, +0.0026] |
| Per-sport Platt | stated p | 1,067 / 225 | 0.2316 / 0.2282 | +0.0059 [-0.0015, +0.0134] |
| Outcome model | training base rate | 2,858 / 609 | 0.2454 / 0.2484 | -0.0013 [-0.0059, +0.0033] |
| Outcome model | stated p | 1,291 / 280 | 0.2358 / 0.2311 | +0.0041 [-0.0004, +0.0086] |

The conclusions of the two earlier runs are unchanged: the stated probabilities carry information against the base rate, recalibration does not improve them, and the outcome model adds nothing beyond the stated p.

## Limits

Outcome-exposed historical study; approximate timing (card date, outcome two days later); dependent rows. The sporting learning store is unchanged.
