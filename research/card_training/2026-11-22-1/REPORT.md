# Card-record training run 2026-11-22-1 (CARD-TRAIN-v1)

Run after the settlement and canonical import of 22 November 2026 (P-686 to P-696 from mini `20261118DA6D9F6251746B979F5895FA`; 11 cards, 46 decisive rows added, 0 UNRESOLVED), as prompt 4 requires. `python -m ml card-training verify --run research/card_training/2026-11-22-1` rebuilds all 2,904 predictions byte for byte. Evidence class HISTORICAL_OUTCOME_EXPOSED_STUDY; nothing is applied to any card (ML-SEP-v1).

## Ingested and admitted

All 696 settled cards, P-001 to P-696: 3,196 rows ingested; 3,128 admitted (1,337 with a stated probability, 1,791 outcome-only with reason NO_STATED_P); 68 excluded (29 UNRESOLVED, 12 UNATTAINABLE, 12 VOID, 10 PUSH, 5 UNDATED). Against run 2026-11-16-1, 11 new cards and 46 new stated-probability rows are admitted. The 29 rows still UNRESOLVED are older rank-log rows outside the import queues.

## Walk-forward results (negative favours the model; 95% interval over cards)

| Model | vs | Rows / cards | Brier model / baseline | Card-mean difference |
|---|---|---|---|---|
| Stated p as written | training base rate | 1,113 / 236 | 0.2287 / 0.2460 | **-0.0183 [-0.0288, -0.0078]** |
| Platt recalibration | stated p | 1,113 / 236 | 0.2291 / 0.2287 | +0.0005 [-0.0015, +0.0025] |
| Per-sport Platt | stated p | 1,113 / 236 | 0.2320 / 0.2287 | +0.0057 [-0.0014, +0.0128] |
| Outcome model | training base rate | 2,904 / 620 | 0.2451 / 0.2484 | -0.0015 [-0.0060, +0.0031] |
| Outcome model | stated p | 1,337 / 291 | 0.2359 / 0.2314 | +0.0039 [-0.0004, +0.0082] |

**Regenerated 22 November 2026 (Codex review of PR #11).** The import inventory wrote ranks as `R1`, `R2`, `R3` and `ml/evaluation/card_history.py` read only digits, so the first run gave all 46 new rows rank 0. The reader now accepts the prefix; P-686 to P-696 carry 11 Rank 1, 11 Rank 2 and 1 Rank 3 rows (23 are unranked research rows). Only the outcome-model rows moved, by at most 0.0003.

The conclusions of the earlier runs are unchanged: the stated probabilities carry information against the base rate, recalibration does not improve them, and the outcome model adds nothing beyond the stated p.

## Limits

Outcome-exposed historical study; approximate timing (card date, outcome two days later); dependent rows. The sporting learning store is unchanged.
