# Card-record training run 2026-11-15-2 (CARD-TRAIN-v1)

Run after the P-660–P-685 import (commit ab8b2ea92), as prompt 4 requires. `python -m ml card-training verify --run research/card_training/2026-11-15-2` rebuilds all 2,805 predictions byte for byte. Evidence class HISTORICAL_OUTCOME_EXPOSED_STUDY; nothing is applied to any card (ML-SEP-v1).

## Ingested and admitted

All 685 settled cards, P-001 to P-685: 3,150 rows ingested; 3,029 admitted (1,273 with a stated probability, 1,756 outcome-only with reason NO_STATED_P); 121 excluded (82 UNRESOLVED, 12 UNATTAINABLE, 12 VOID, 10 PUSH, 5 UNDATED). The 325 rows from P-660–P-685 are chat research rows (ANALYST_NOT_PRIMARY); they train these study models like every other settled row and never count as issued forecasts.

## Walk-forward results (negative favours the model; 95% interval over cards)

| Model | vs | Rows / cards | Brier model / baseline | Card-mean difference |
|---|---|---|---|---|
| Stated p as written | training base rate | 1,049 / 224 | 0.2282 / 0.2455 | **-0.0184 [-0.0293, -0.0076]** |
| Platt recalibration | stated p | 1,049 / 224 | 0.2286 / 0.2282 | +0.0005 [-0.0016, +0.0026] |
| Per-sport Platt | stated p | 1,049 / 224 | 0.2316 / 0.2282 | +0.0056 [-0.0019, +0.0131] |
| Outcome model | training base rate | 2,805 / 608 | 0.2452 / 0.2482 | -0.0013 [-0.0059, +0.0032] |
| Outcome model | stated p | 1,273 / 279 | 0.2358 / 0.2312 | +0.0041 [-0.0004, +0.0086] |

Same conclusions as run 2026-11-15-1 with 26 more games: the stated probabilities carry information, recalibration does not improve them, and the outcome model adds nothing beyond the stated p. The newest week (2026-W46) is still the last scored week; rows from 15 November enter training for the next week's refit.

## Limits

Outcome-exposed historical study; approximate timing (card date, outcome two days later); dependent rows. The sporting learning store is unchanged: no source captures were retained for the new finals.
