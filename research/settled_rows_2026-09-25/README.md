# Settled-row dataset and calibration review — every completed log (2026-09-25(d))

**Status: LEARNING_ONLY / descriptive.** This folder turns the settled rows of the five combined logs into one dataset, and describes how the framework's stated probabilities have performed. Nothing here is a fitted coefficient, shrink or cap (`L-087`); the findings feed disclosures, prospective tests and tools. Every figure is hindsight on the framework's own selected cards, and rows within a card are dependent. Intervals therefore resample **whole cards**.

## Files

| File | What it is |
|---|---|
| `extract_settled_rows.py` | Parser: rank tables and bullet settlements in Parts 1–5 → `settled_rows.csv`. The method is in its docstring |
| `settled_rows.csv` | One row per graded ranked row. Columns: card, number, sport, rank, contract, family, direction, p, result, source line, event |
| `conflicts.csv`, `coverage.txt` | Parse diagnostics |
| `analyze_settled.py` → `analysis_results.json` | Calibration bands; breakdowns by family, sport, rank and direction; trend; top-two |
| `analyze_supplement.py` → `supplement_results.json` | Murphy decomposition; non-baseball cushions; the 0.50–0.65 band; same-card phase v full total |
| `../../tools/calibration_report.py` | The reusable version of this analysis (run it at every 25-card review) |

## Coverage and validation

- **1,185 graded rows from 307 cards.** 600 rows (149 cards, P-318–P-509) carry an issued probability. 123 of those probabilities were joined from issue-time tables, with contract-text matching.
- 62 rows could not be attributed to a card and were dropped. One (card, rank) conflict remains: P-036, two different live views.
- **Validation against the logs' own cohort figures:**

  | Cohort | Logs | Dataset |
  |---|---|---|
  | P-424–P-437 | 52 rows, 36 W / 16 L, Brier 0.1892 | **identical** |
  | P-345–P-371 | 105 rows, 0.2434 | 107 rows, 0.2451 |
  | P-373–P-423 | 194 rows, ≈ 0.2276 | 200 rows, 0.2250 |
  | Legacy scorecard to 2026-09-12 | Brier 0.2265 | 0.2249 overall |

- **Limitations.**
  - Sport and market family are classified from the event name and contract text.
  - "Decisions" (p ≥ 0.5) approximate the preferred side of each pair.
  - The ordinal era (P-001–P-317) has no probabilities, so it enters only the rank-slot analysis.

## Findings

Decisions are the preferred rows, with p ≥ 0.5.

**1. Overall calibration is good, and skill is modest.**
- All 598 probability rows: Brier **0.2249**.
- Murphy decomposition: reliability **0.002** (tiny miscalibration), resolution **0.019**, uncertainty 0.244. Skill against the base rate is **+7.7%**.
- Logistic calibration slope **1.06** (SE 0.16). There is **no global over-confidence**, so no global shrink is warranted.
- `C-PROB-EXTREMITY` is not supported. The prospective subset (79 of its required 100 rows) won 91.1% against a mean stated 79.3%.

**2. The skill sits in rows stated at 0.65 or more; rows between 0.50 and 0.65 behave like coin flips.**

| Decisions | n (cards) | Win rate | Mean stated | Gap [card-cluster 95%] | Brier |
|---|---|---:|---:|---|---:|
| p 0.50–0.65 | 235 (132) | **0.536** | 0.574 | −0.037 [−0.105, +0.031] | 0.2494 |
| p ≥ 0.65 | 152 (68) | **0.803** | 0.744 | +0.058 [−0.011, +0.118] | 0.1529 |

A card's modest leans carry essentially no information beyond a coin flip, and its strong leans are, if anything, slightly under-stated.

**3. The clearest systematic error: underdog cushions (+k.5) outside baseball are over-confident.**

| +k.5 decisions | n | Won | Mean stated | Gap [95%] |
|---|---:|---:|---:|---|
| Baseball | 45 | 60.0% | 0.613 | −0.013 (calibrated) |
| **All other sports** | **40** | **42.5%** | **0.642** | **−0.217 [−0.353, −0.073]** |

- By sport: basketball 3/8; NFL/NCAA 1/6; AFL 0/3; tennis 1/4; soccer 8/13 at a stated 0.77.
- Favourite handicaps (−k.5): 16/26 at 0.559, which is fine.
- **This recurs across cohorts:** the G-L12 origin (underdog cushions 10 W / 13 L), `C-UNDERDOG-SEPARATION` (basketball), and now the full record.

**4. Where the process has shown skill, and where it hasn't.**

| Sport | Decisions | Won | Mean stated | Brier | Resolution | Reading |
|---|---:|---:|---:|---:|---:|---|
| Soccer | 143 | 74.8% | 0.700 | **0.170** | 0.036 | clear skill (mainly phase and team-total rows) |
| NPB / KBO / CPBL | 56 | 64.3% | 0.623 | 0.216 | 0.023 | some skill |
| Cricket | 34 | 64.7% | 0.630 | 0.227 | 0.039 | resolution, but miscalibrated (reliability 0.022) |
| MLB | 70 | 58.6% | 0.596 | 0.238 | **0.0075** | near-zero resolution |
| Basketball | 31 | 58.1% | 0.586 | 0.241 | 0.012 | near-zero resolution |
| Tennis | 16 | 50.0% | 0.601 | **0.281** | — | worse than a coin flip |
| NFL / NCAA | 12 | 25.0% | 0.544 | **0.276** | — | **over-confident**, gap −0.294 [−0.466, −0.124] |
| AFL | 10 | 30.0% | 0.662 | **0.257** | — | **over-confident**, gap −0.362 [−0.601, −0.102] |

MLB and basketball, the two most-carded sports after soccer, show almost no discrimination. This matches the seed baseline check in `SKILL_BASELINE_LEDGER.md`.

**5. Market families.**

| Decisions | n | Won | Mean stated | Brier |
|---|---:|---:|---:|---:|
| Phase totals | 47 | 76.6% | 0.677 | 0.173 |
| Team totals | 25 | 76.0% | 0.744 | 0.171 |
| Corners | 26 | 73.1% | 0.649 | 0.198 |
| Full-game totals | 124 | 61.3% | 0.609 | 0.225 (≈ coin flip) |
| Handicaps | 111 | 54.1% | 0.611 | 0.236 |

- **The same event, compared:** in the 34 cards carrying both a phase and a full-game total, phase decisions won **30/36 (83%)** at a stated 0.693, and full totals **27/41 (66%)** at 0.652. That is new evidence for the existing `C-PHASE-VS-FULL-TOTAL` candidate. The edge-stratified test it requires is still pending.
- Team-total Unders won 9/10 at 0.78.

**6. Total direction, by league (small samples; TESTING only).**
- **NPB / KBO / CPBL:** Unders **11/14** at a stated 0.607; Overs 4/9 at 0.60.
- **Cricket:** Unders **9/12** at 0.589; Overs 7/12 at 0.631.
- **MLB and soccer:** no asymmetry.

**7. Rank slots below #1 carry no ordering information.**

| Record | #1 | #2 | #3 | #4 |
|---|---:|---:|---:|---:|
| All eras (1,179 rows) | **66.4%** | 56.1% | 55.6% | 54.0% |
| Ordinal era | 67.6% | 51.8% | 55.2% | 58.2% (above #2) |

Rank 1 separates; ranks 2–4 are indistinguishable. Report probabilities, not slots.

**8. Top-two joint failure matches independence on average.** Across 264 cards, both top rows lost on **14.4%**, against **14.5%** if they were independent. Joint failure mass should be close to the product of the two failure probabilities unless a shared driver is named (G-L17).

**9. Trend.** Decision Brier by cohort:

| P-318–344 | P-345–371 | P-373–423 | P-424–451 | P-452–481 | P-482–509 |
|---:|---:|---:|---:|---:|---:|
| 0.244 | 0.240 | 0.212 | 0.164 | 0.194 | 0.223 |

The movement follows the **sport mix** (the best cohort was soccer-heavy), not a demonstrated method improvement.

## What this changes

`RULES_GENERAL.md` §"2026-09-25(d)" and `LEARNING_REGISTER.md` §"2026-09-25(d)" hold the controls and tests:
- **`C-PLUS-CUSHION`:** a disclosure for non-baseball +k.5 rows.
- **`C-DEPARTURE-LEDGER`:** the card's departure from `BASELINE_P`, attributed to named mechanisms. The tool is `tools/card_math.py departure`.
- **`C-TRACK-RECORD`:** print the sport's calibration row; `NO_DEMONSTRATED_SKILL` for tennis, NFL/NCAA and AFL.
- **`C-LOW-RESOLUTION-BAND`:** rows at 0.50–0.65 are labelled coin-flip-grade.
- **`tools/card_math.py`:** the reference distribution-to-contract implementation (M14).
- **`tools/calibration_report.py`:** the review standard.
- **A canonical settlement table,** so future extraction is exact.


<!-- RANK-MODEL-2026-09-25E -->
## 2026-09-25(e) rebuild

1. **Result-parsing fix.** Where a table has both a narrative result column and an exact result column, the exact token (WIN/LOSS/PUSH/VOID) now wins.
   - In the (d) dataset, **17 rows were graded the wrong way round**, e.g. P-085 "Lobos lost by 1; +2.5 covers" was read as a loss.
   - **55 rows were missing.**
   - The (d) findings above move slightly; none of their conclusions changes.
2. **Mini logs.** Every file under `Mini logs (to be sent to actual log later)/*/` is read. A card also imported into Part 5 is de-duplicated: the last occurrence wins.
3. **Sport classification.** An explicit league word ("NBL", "Basketball") beats a shared nickname ("Hawks").

**Result:** 1,264 graded rows from 315 cards; 641 with p (155 cards).

**Use.** This dataset trains RM-1 (`research/rank_model_2026-09-25e/`). The (d) sections above remain the descriptive review.


<!-- REVIEW-2026-09-26 -->
## 2026-09-26 — figures on the rebuilt dataset

`python tools/calibration_report.py` on the 2026-09-25(e) dataset (411 decisions from 155 cards; 639 rows with p) gives:
- **Brier 0.2268**; reliability 0.0028, resolution 0.0167, uncertainty 0.2430; **skill +6.6%** over climatology;
- **calibration slope 1.01** (SE 0.16), intercept +0.11.

The (d) figures quoted above (0.2249, slope 1.06, +7.7%) came from the dataset before the result-parsing fix. **None of the conclusions changes.** Two readings are sharpened:
- **Soccer:** 146 decisions from only 37 cards; gap +0.054 with a card-cluster interval of [−0.035, +0.132]. It has the strongest resolution of any sport, but its calibration interval spans 0: "strongest evidence", not "proof of skill".
- **The whole record is self-selected.** Every card was for an event the operator chose. `C-EVENT-UNIVERSE` (2026-09-26) starts the first systematically declared sample.
