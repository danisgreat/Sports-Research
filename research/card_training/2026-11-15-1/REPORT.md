# Card-record training run 2026-11-15-1 (CARD-TRAIN-v1)

Code commit 33455a41f2fd5db915941b46c71cfa98ef788ffb. `python -m ml card-training verify --run research/card_training/2026-11-15-1`
rebuilds all 2,530 predictions byte for byte. Evidence class HISTORICAL_OUTCOME_EXPOSED_STUDY; nothing is applied to any card (ML-SEP-v1).

## Ingested and admitted

Every settled card P-001 to P-659 (the effective history: combined logs, rank log, import inventories and settlement revisions).

| Status | Reason | Rows |
|---|---|---|
| OUTCOME_AND_CALIBRATION | decisive, dated, stated p | 1,195 |
| OUTCOME_ONLY | NO_STATED_P (mostly the earliest era) | 1,559 |
| EXCLUDED | NOT_DECISIVE:UNRESOLVED | 32 |
| EXCLUDED | NOT_DECISIVE:UNATTAINABLE | 12 |
| EXCLUDED | NOT_DECISIVE:VOID | 12 |
| EXCLUDED | NOT_DECISIVE:PUSH | 10 |
| EXCLUDED | UNDATED | 5 |
| **Total** | 659 cards | **2,825** |

## Training (walk-forward by week)

Each week's rows were predicted only by models fitted on earlier weeks. The first scored week had 216 training rows; 11 weeks
were scored (2026-W34 to W46). Differences are averaged within card first; negative favours the model. Intervals are 95% over cards.

| Model | vs | Rows / cards | Brier model / baseline | Card-mean difference [95%] |
|---|---|---|---|---|
| Stated p as written | training base rate | 971 / 215 | 0.2293 / 0.2448 | **-0.0173 [-0.0285, -0.0061]** |
| Platt recalibration | stated p | 971 / 215 | 0.2295 / 0.2293 | +0.0003 [-0.0018, +0.0025] |
| Per-sport Platt | stated p | 971 / 215 | 0.2328 / 0.2293 | +0.0060 [-0.0017, +0.0138] |
| Outcome model | training base rate | 2,530 / 583 | 0.2452 / 0.2476 | -0.0011 [-0.0059, +0.0036] |
| Outcome model | stated p | 1,195 / 270 | 0.2365 / 0.2322 | +0.0039 [-0.0008, +0.0085] |

What it shows:
- The stated probabilities carry real information: they beat the base rate, and the interval is entirely below zero.
- Recalibrating them did not help. Neither pooled nor per-sport Platt improved on the probabilities as written, so there is no
  evidence of a systematic over- or under-confidence that a simple correction would fix.
- The outcome model (sport, family, rank, direction and stated p) learned almost nothing beyond the base rate and did slightly
  worse than the stated p alone. Those card attributes add no reliable signal yet.

## Limits

- Outcome-exposed historical study, not prospective evidence. Rows within a card and across a week are dependent; the card-level
  interval handles the first, not the second.
- Timing is approximate: issue at the card date (00:00 UTC), outcome treated as available two days later. Per-row settlement times
  are not in the history.
- The sporting learning store (`research/learning_store/`) is separate. It holds 5,402 finals: bulk NBA, NHL and MLB seasons plus
  about 25 card games whose source pages were captured. The other card games' finals were settled from sources whose pages were
  never captured with hashes, so they cannot enter the store or its training releases until recaptured. Settlement from this
  release onward should retain those captures.
