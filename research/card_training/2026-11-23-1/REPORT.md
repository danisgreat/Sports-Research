# Card-record training run 2026-11-23-1 (CARD-TRAIN-v1)

Run after the settlement and canonical import of 23 November 2026 (P-697 to P-703 from mini `20261120-495CEEB69E9540938CF6A7DAA7B546B4`; 7 cards, 30 decisive rows added, 0 UNRESOLVED), as prompt 4 requires. `python -m ml card-training verify --run research/card_training/2026-11-23-1` rebuilds all 2,934 predictions byte for byte. Evidence class HISTORICAL_OUTCOME_EXPOSED_STUDY; nothing is applied to any card (ML-SEP-v1).

## Ingested and admitted

All 703 settled cards, P-001 to P-703: 3,226 rows ingested; 3,158 admitted (1,367 with a stated probability, 1,791 outcome-only with reason NO_STATED_P); 68 excluded, as in run 2026-11-22-1. Against that run, 7 new cards and 30 new stated-probability rows are admitted, with their original ranks (7 Rank 1, 7 Rank 2, 2 Rank 3, 14 unranked).

## Walk-forward results (negative favours the model; 95% interval over cards)

| Model | vs | Rows / cards | Brier model / baseline | Card-mean difference |
|---|---|---|---|---|
| Stated p as written | training base rate | 1,143 / 243 | 0.2292 / 0.2461 | **-0.0178 [-0.0281, -0.0076]** |
| Platt recalibration | stated p | 1,143 / 243 | 0.2296 / 0.2292 | +0.0004 [-0.0015, +0.0024] |
| Per-sport Platt | stated p | 1,143 / 243 | 0.2327 / 0.2292 | +0.0058 [-0.0011, +0.0127] |
| Outcome model | training base rate | 2,934 / 627 | 0.2452 / 0.2485 | -0.0014 [-0.0060, +0.0031] |
| Outcome model | stated p | 1,367 / 298 | 0.2363 / 0.2318 | +0.0039 [-0.0003, +0.0081] |

The conclusions of the earlier runs are unchanged: the stated probabilities carry information against the base rate, recalibration does not improve them, and the outcome model adds nothing beyond the stated p.

## Limits

Outcome-exposed historical study; approximate timing (card date, outcome two days later); dependent rows. Four of the seven new cards were refused at sealing; their ranks are the registered rule computed on the card. The sporting learning store is unchanged.
