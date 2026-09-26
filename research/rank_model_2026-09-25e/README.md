# RM-1: the ranking-probability model (2026-09-25(e))

**Status: operative for ranking under `C-RANK-MODEL`** (`RULES_GENERAL.md` §"2026-09-25(e)").
- RM-1 is a **user-authorised exception to `L-087`**. On 2026-09-25 the user instructed that a new probabilistic model or calibration be built if one is required or can be done, to make Rank 1 and Rank 2 far more likely to win than lose.
- The safeguards that stand in for `L-087` are at the end of this file.

**What RM-1 is.** A calibration of the card's own stated probability `p` into a ranking probability `q`, fitted on the pooled settled record:

```
logit(q) = a + b · logit(p) + c · [decision side is a +k.5 cushion outside baseball, hockey and soccer]
```

- `p` is the side with stated p ≥ 0.5, the decision side. A row stated below 0.5 is scored through its complement, so a row and its complement always sum to one.
- q is clipped to [0.03, 0.97].
- A stated 0.50 stays 0.50.
- **Coefficients** ([`tools/rank_model_coefficients.json`](../../tools/rank_model_coefficients.json)): a = −0.187, b = 1.543, c = −1.127, fitted on 409 decision rows from 154 cards.
- RM-1 reads no odds, prices or market material.

**Worked values:**

| Stated p | q (ordinary row) | q (such a cushion) |
|---:|---:|---:|
| 0.55 | 0.53 | 0.27 |
| 0.60 | 0.61 | 0.34 |
| 0.65 | 0.68 | 0.41 |
| 0.75 | 0.82 | 0.59 |

## Files

| File | What it is |
|---|---|
| `validate_rank_model.py` → `validation_results.json` | Out-of-sample comparison of every specification, with re-ranking of held-out cards |
| `../../tools/rank_model.py` | The model: classification, fitting, `score`, `rank`, `fit`, `show` |
| `../../tools/test_rank_model.py` | Unit tests; CI runs them |
| `../settled_rows_2026-09-25/settled_rows.csv` | The data, rebuilt for this pass (below) |

## The data, and the corrections made first

The settled-row dataset was rebuilt before any fitting:
1. **A result-parsing bug.** Where a settlement table has both a narrative column ("Lobos lost by 1; +2.5 covers") and an exact result column ("**WIN**"), the extractor was reading the narrative.
   - **17 rows had been graded the wrong way round** in the 2026-09-25(d) dataset: P-077, P-082, P-083, P-085, P-124, P-125, P-127, P-128, P-132 and P-464.
   - A further 55 rows had been dropped.
   - The exact-token column now wins.
2. **The P-510+ mini log** is now read (24 rows).
3. **P-514** (NBL) had been mis-classed as NPB through the shared "Hawks" nickname; an explicit league word now wins.

**Result:** 1,264 graded rows from 315 cards; 641 carry a stated probability (155 cards).

## Question and design

**Question.** If Rank 1 and Rank 2 had been chosen by a calibrated probability instead of the stated one, would they have won more often on cards the model had not seen?

| Spec | Form |
|---|---|
| IDENTITY | q = p (the issued ranking) |
| GLOBAL | a + b·logit(p) |
| **RM-1** | GLOBAL plus the pre-specified cushion term. The effect was documented in G-L12's origin (10 W / 13 L), in `C-UNDERDOG-SEPARATION` and in the 2026-09-25(d) review (17/40), so it was **named before this test**, not searched for. Baseball and hockey are excluded because one-unit margins are common there (MLB +1.5 base rate 0.62–0.66). Soccer +k.5 rows are excluded because they won 7/8; "+0.5 / 1X" rows are classed as double chances |
| RM-1X (challenger) | RM-1 plus ridge-penalised sport slopes, sport offsets and 14 market-class offsets; ridge weight chosen by grouped CV |

**Designs.** All group whole cards:
- grouped 10-fold CV × 5 repeats;
- leave-one-card-out (LOCO) re-ranking;
- four forward-in-time splits (train before P-T, test from P-T), with RM-1X's ridge chosen inside the training cards only;
- an ordinal-era check.

## Results

### 1. Probability quality (log loss / Brier of the decision rows)

| | Grouped CV | Fwd P-420+ | Fwd P-450+ | Fwd P-480+ | Fwd P-495+ |
|---|---|---|---|---|---|
| Test decisions | 409 | 187 | 109 | 59 | 49 |
| IDENTITY | 0.6112 / 0.2129 | 0.5756 / 0.1974 | 0.6154 / 0.2145 | 0.6646 / 0.2362 | 0.6559 / 0.2320 |
| GLOBAL | 0.6090 / 0.2129 | 0.5656 / 0.1944 | 0.6050 / 0.2111 | 0.6525 / 0.2305 | 0.6448 / 0.2268 |
| **RM-1** | **0.6032 / 0.2100** | **0.5551 / 0.1892** | **0.5861 / 0.2019** | **0.6371 / 0.2235** | **0.6233 / 0.2169** |
| RM-1X | 0.6043 / 0.2104 | 0.5560 / 0.1895 | 0.5872 / 0.2024 | 0.6376 / 0.2237 | 0.6237 / 0.2171 |

- **RM-1 is best in every design.**
- **RM-1X never beats it.** Its ridge weight went to the grid maximum (256) in every forward split. Sport slopes and class offsets beyond the cushion term do not generalise at this sample size. RM-1X is kept switched off for re-testing at each review.
- **The cushion coefficient was estimable early and has stayed negative:** −0.50 by P-420, −0.75 by P-450, −1.11 by P-480, −1.03 by P-495.

### 2. Rank 1 and Rank 2 on held-out cards (issued order → RM-1 order)

| Design | Cards | R1 | R2 | Both win | Both lose | Change in top-two wins per card [95%] |
|---|---:|---|---|---|---|---|
| LOCO | 148 | 64.2% → **68.9%** | 60.1% → **62.2%** | 42.6% → 45.9% | 18.2% → **14.9%** | **+0.068 [+0.007, +0.128]** |
| Fwd P-420+ | 68 | 69.1% → **72.1%** | 64.7% → **69.1%** | 48.5% → 52.9% | 14.7% → **11.8%** | +0.074 [0.000, +0.147] |
| Fwd P-450+ | 42 | 66.7% → **69.0%** | 59.5% → **69.0%** | 45.2% → 52.4% | 19.0% → **14.3%** | +0.119 [0.000, +0.262] |
| Fwd P-480+ | 25 | 68% → 68% | 56% → **68%** | 40% → 52% | 16% → 16% | +0.120 [−0.080, +0.320] |
| Fwd P-495+ | 20 | 70% → **75%** | 60% → **70%** | 45% → 60% | 15% → 15% | +0.150 [−0.050, +0.350] |

The order is exactly the tool's (`tools/rank_model.rank_rows`), including the near-tie rule.

- **Rank 1 and Rank 2 are never lower** in any design.
- **The LOCO interval excludes zero:** 17 cards better, 7 worse, 124 unchanged.
- **The direction is the same in all five designs,** and the specification was fixed before the test.
- The forward intervals touch zero. With 20–68 cards they cannot exclude it.

**By sport (LOCO), where the order changes:**
- Oval sports: R1 37.5% → 62.5%; both lose 50% → 25%.
- Basketball: R1 50% → 68.8%; both win 31% → 56%.
- Tennis: R2 43% → 86%.
- MLB, NPB/KBO, soccer and cricket: **unchanged**.

A first draft that let near-tied flips move a side cost MLB three Rank-1 wins. Ties within 0.05 of 0.5 are now labelled `NEAR_TIED_FLIP` and keep the stated side; held out, such flips won 27/57.

### 3. Held-out reliability of q (LOCO)

| Tier (q) | Decisions | Won | Mean q | Mean stated p | Held-out Rank-1 record |
|---|---:|---:|---:|---:|---|
| STRONG (≥ 0.70) | 134 | **80.6%** | 0.819 | 0.757 | 49/67 (73.1%) |
| SUPPORTED (0.62–0.70) | 68 | 61.8% | 0.660 | 0.634 | 24/38 (63.2%) |
| LEAN (0.55–0.62) | 72 | 56.9% | 0.583 | 0.583 | 19/30 (63.3%) |
| COIN_FLIP (< 0.55) | 135 | 51.9% | 0.477 | 0.549 | 7/13 |

**Only the STRONG tier is "far more likely to win than lose."** Below q 0.70 the record is 52–63% at every tier. For the user's objective this is the most important single fact. Stated p agrees: rows stated at 0.70 or more won 83%; rows at 0.50–0.65 won 54%.

**Cushion rows held out:** 26 rows, mean q 0.307, won 0.308. The term is exactly calibrated out of sample.

### 4. Ordinal-era check (a limit on generality)

In the ordinal era (P-001–P-317, before stated probabilities), the same cushions at Rank 1 or 2 won **17/28 (61%)**. In the probability era they won **7/24 (29%)**.
- So the penalty describes **how the current method prices cushions**. It is not a law of the sport.
- The population fact that explains it is in `../team_baseline_2026-09-25e/README.md`: a small cushion on the weaker team covers 32–54% in basketball, NFL and NRL.
- If cushion pricing is repaired (`C-PLUS-CUSHION` amended, TB-1 anchoring), the term should shrink at the next refit. That is what the refit is for.

## What RM-1 does not do

- **It creates no resolution in coin-flip contracts.** A slate of main-line rows priced near 0.55 stays near 0.55. The honest statement is `TOP2_QUALITY: TOP2_COIN_FLIP`.
- In MLB, NHL, basketball and tennis, the cards' stated probabilities carry little information. The better anchor is TB-1 where it has resolution, and the population rate elsewhere.
- **RM-1 is not a PUBLISHED numerical probability** (`NUMERICAL_PROGRAM.md`). q is a calibrated, unvalidated ranking probability. Both p and q are scored at settlement (`T-RM1-PROSPECTIVE`).

## Safeguards (stand-ins for `L-087`)

1. **Pooled, pre-specified terms only.** No coefficient comes from one game, card or cohort. A new term enters only if it beats RM-1 on log loss in every forward split at a 25-card review.
2. **Refit only at the 25-card review:**
   ```
   python research/settled_rows_2026-09-25/extract_settled_rows.py
   python research/rank_model_2026-09-25e/validate_rank_model.py
   python tools/rank_model.py fit --fitted <date> --out tools/rank_model_coefficients.json
   ```
   Then issue a new control manifest.
3. **Stated p is printed unchanged beside q.** q never overwrites the card's distribution.
4. **Both p and q are scored at settlement.** If q's Brier is worse than p's over the next 25 cards, RM-1 reverts to disclosure-only (`T-RM1-PROSPECTIVE`).
5. **A flip created by RM-1 is capped at SUPPORTED.** Override is allowed only when a TB-1 with resolution gives the stated side ≥ 0.55.


<!-- REVIEW-2026-09-26 -->
## 2026-09-26 review addendum — what the validation does and does not show

**Reproduced.** Re-running `validate_rank_model.py` on the committed dataset reproduced `validation_results.json` byte for byte (coefficients −0.1871 / 1.5433 / −1.1272).

**Three limits the headline figures do not show:**
1. **The cushion term was discovered on the data that validates it.** It was observed in P-345–P-423 (the G-L12 origin) and confirmed by the 2026-09-25(d) review of rows through P-509. The forward splits from P-420, P-450 and P-480 therefore test on rows that helped name the term. Only rows from P-518 onward are genuinely new.
2. **Only the leave-one-card-out figure excludes zero.** The forward-split re-ranking intervals, in top-two wins per card, are:

   | Split | Change (95% interval) | Cards | R1/R2 changed |
   |---|---|---:|---|
   | from P-420 | +0.074 [0.000, +0.147] | 68 | 4 / 7 |
   | from P-450 | +0.119 [0.000, +0.262] | 42 | 4 / 8 |
   | from P-480 | +0.120 [−0.080, +0.320] | 25 | 5 / 6 |
   | from P-495 | +0.150 [−0.050, +0.350] | 20 | 5 / 6 |

   The improvement comes from a handful of re-ordered cards per split.
3. **The cushion effect is era-dependent.** Top-two underdog cushions won 17/28 (61%) in the ordinal era and 7/24 (29%) in the probability era. The penalty may describe how probabilities were written in one period rather than a stable property of cushions.

**Consequence (`RULES_GENERAL.md` §"2026-09-26"(g)).** RM-1 stays operative for ranking, as the user authorised, but it is described as **promising and unproven**. `T-RM1-PROSPECTIVE` now also reports non-baseball cushion-class rows separately. If, over at least 15 prospective cushion-class rows, the win rate exceeds the mean q by more than 0.15, the cushion term reverts to disclosure-only until the next review.
