# Predictability across sports — what the models and the cards can and cannot do (2026-09-26(e))

**Status: LEARNING_ONLY. Measurement only; no probability, rank, width or card rule changes.**
- P1–P4 were preregistered in [`PREREGISTRATION.md`](PREREGISTRATION.md), committed in `cc447c9` before any run.
- P5 and the P3 disagreement split are **exploratory** and labelled as such.
- Market-blind throughout: no odds, lines or prices were read.

**Origin.** On 2026-09-26 the user asked for predictability across all sports to be improved "properly". This pass answers three questions:
1. How predictable is each sport?
2. Where do the numerical models add information?
3. Would anchoring the cards on those models have made them better?

## Headline

1. **Predictability differs enormously by sport** (P5). The table gives the share of games in which the validated model's favourite reaches 0.70 (the STRONG tier), and how often those favourites won, on the latest season, leak-free:

   | League | Result Brier: model v population | Games with a favourite ≥ 0.70 | Those favourites won |
   |---|---|---:|---:|
   | AFL | 0.183 v 0.244 | **39%** | **90.6%** |
   | WNBA | 0.209 v 0.251 | 28% | 83.7% |
   | NBL | 0.213 v 0.253 | 26% | 80.4% |
   | NBA | 0.210 v 0.248 | 29% | 79.5% |
   | NFL | 0.226 v 0.250 | 27% | 73.1% (the 0.70–0.80 band won 67% at a stated 0.747: over-confident) |
   | NHL | 0.248 v 0.250 | 6% | 72.9% |
   | NRL | 0.235 v 0.249 | 19% | 68.3% (the 0.70–0.80 band won 67% at 0.737: over-confident) |
   | EPL (three-way winner) | 0.222 v 0.243 | 6% | 58.8% (n = 17) |
   | **MLB** | 0.247 v 0.250 | **0%** | — (90% of games fall at 0.50–0.60) |

   **Totals** almost never reach 0.70 at a line near the league mean (3–15% of games). The WNBA's 30% is an artefact: its line came from earlier seasons, and 2026 scoring rose by about 10.7 points.

   **Tennis** (the ATP model) and **IPL cricket** were validated in the 2026-09-26 pass:
   - tennis winners are well predicted, but by Elo, which A1 improves only narrowly (Brier 0.222 against 0.224);
   - IPL results are no better than a coin flip.

2. **Where the models add information** (P2 plus the 2026-09-26 validation).
   - **Sides and results:** soccer's top five leagues, NFL, AFL, NBA, WNBA, NHL (small), NBL (2025-26), MLB (small).
   - **Totals:** only basketball (NBA, WNBA; NBL in 2024-25), La Liga and the Bundesliga, and MLB totals with starters (2026 only).
   - **Not demonstrated:** NRL results; MLB's starter term on results; NHL, EPL, Serie A, Ligue 1, NFL, AFL and NRL totals.
3. **The cards are not worse than the models on the cards' own contracts** (P3). This covers 98 contracts from 54 settled cards (34 MLB; 20 across WNBA, NBL, NFL, AFL, NRL and EPL).

   | Source | Brier |
   |---|---:|
   | Card | **0.2438** |
   | A1 | 0.2505 |
   | Population | 0.2680 |

   Card − A1 is −0.007 [−0.025, +0.011]: **no demonstrated difference.** **Anchoring the cards on the models would not have improved the record**, so the model registry stays a reference, not a card input (below).
4. **MLB's declared starter term did not add skill on results** (P1, preregistered verdict: "not demonstrated"). It improved the 2026 totals but not the 2025 totals. Correction: the claim that historical probable starters "cannot be reconstructed leak-free" was wrong, and `tools/mlb_model.py` is corrected.

**What this means for Rank 1 and Rank 2.** Rank 1 wins "far more often than it loses" only in the STRONG tier (`research/rank_model_2026-09-25e`). The models show where that tier exists:
- **often:** sides in the AFL, basketball and the NFL;
- **sometimes:** NRL and NHL;
- **almost never:** MLB, most totals, and soccer three-way results. Soccer's STRONG rows come from phase, team-total and double-chance markets.

No method can make a coin-flip contract strong. The predictability map is now a reference row (`BASE_RATES_REGISTER.md` §7.8) for choosing and describing slates (`SLATE_ADVISORY`, `C-EVENT-UNIVERSE`).

## P1 — MLB: the declared starter term (preregistered)

**Data and method.**
- **Data:** statsapi schedule with `probablePitcher` (kept on completed games) and every probable starter's game log, 2025 and 2026 (to 24 Sep).
- **Constants:** PRIORS unchanged.
- **Protocol:** rolling origin, at least 300 prior games; day-block bootstrap.

| | 2025 (2,121 games) | 2026 (2,073 games) |
|---|---|---|
| **Primary:** A1S − A1 home-win log loss | +0.0012 [−0.0046, +0.0069] | −0.0019 [−0.0079, +0.0043] |
| Secondary: A1S − A1, mean of five Brier scores | +0.0005 [−0.0009, +0.0019] | **−0.0016 [−0.0031, −0.0002]** |
| A1 (team-only) − A0, win Brier | **−0.0043 [−0.0078, −0.0010]** | −0.0027 [−0.0054, +0.0000] |
| TB-1 − A0, win Brier | **−0.0045 [−0.0073, −0.0021]** | **−0.0023 [−0.0043, −0.0003]** |
| A1 − TB-1, win Brier | +0.0002 [−0.0010, +0.0014] | −0.0004 [−0.0014, +0.0005] |
| A1S − A0, total at 8.5 | −0.0014 [−0.0043, +0.0016] | **−0.0032 [−0.0065, −0.0002]** |

- **Verdict (preregistered): "not demonstrated."** The primary interval is below 0 in neither season.
- Probable starters were available for 96% of games (2,038 and 2,009 with both).
- MLB results are barely predictable by any model here: the best win Brier was 0.246 against 0.250.

## P2 — coverage: NBL and NRL (preregistered)

A1 constants are as at `0e98a46`. The data are the ESPN scoreboards cached on 2026-09-25. Figures are A1 − A0 with 95% week-block intervals.

| Window | Result Brier | Margin RPS | Total at line | A1 − TB-1 (result) |
|---|---|---|---|---|
| NBL 2024-25 (159) | −0.0164 [−0.0368, +0.0058] | −0.29 [−0.69, +0.17] | **−0.0244 [−0.0402, −0.0078]** | −0.0014 [−0.0130, +0.0119] |
| NBL 2025-26 (177) | **−0.0397 [−0.0578, −0.0201]** | **−1.39 [−1.95, −0.79]** | −0.0061 [−0.0251, +0.0136] | **−0.0135 [−0.0245, −0.0018]** |
| NRL 2026 (213) | −0.0137 [−0.0273, +0.0003] | **−0.51 [−0.97, −0.06]** | +0.0096 [−0.0018, +0.0218] | −0.0072 [−0.0180, +0.0029] |

## P3 — cards against models on the same contracts (preregistered; pooled)

**Matching.**
- Each card is matched to one completed game by teams, window and the card's own dates or probable starters.
- Among repeat meetings, a candidate must agree with every graded row. The settled results are used only to identify the game; they are not scored.
- Two MLB cards and two other-league cards stayed ambiguous and were excluded.
- Three "EPL"-tagged cards were other competitions (the Uganda Premier League, a European T20 match) or outside the window, and were excluded.

**Contracts.**
- Included: full-game winner, ±k.5 handicaps and half-point totals (plus the soccer first half).
- Excluded: integer totals (27 MLB rows), team totals, phase rows outside soccer, and rows without contract text.

| | Contracts | Cards | Card | A1 | A1S | TB-1 | Population | Card − A1 [95% card cluster] |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| MLB | 61 | 34 | 0.2384 | 0.2407 | 0.2410 | 0.2462 | 0.2515 | −0.0023 [−0.0216, +0.0166] |
| Other leagues | 37 | 20 | 0.2528 | 0.2666 | — | — | 0.2952 | −0.0138 [−0.0517, +0.0236] |
| **Pooled** | **98** | **54** | **0.2438** | **0.2505** | — | — | **0.2680** | **−0.0067 [−0.0251, +0.0113]** |

**Other comparisons.**
- Card − population, pooled: −0.0242 [−0.0555, +0.0029].
- RM-1 q against the card in MLB: no difference (−0.0005 [−0.0064, +0.0057]).
- 50/50 blend of card and A1 (exploratory): 0.2454, no better than the card.
- **When card and A1 disagreed by more than 0.10 (exploratory; 25 contracts):** the card was closer to the outcome 14 times. Brier 0.2553 against 0.2759, not significant.

**Reading.** On these contracts the cards' research carries about as much information as the team models, and possibly a little more. The models' advantage over the population is established on thousands of public games. It is not established over the cards.

## P4 — the reference registry (preregistered selection rule)

`python tools/model_anchor.py registry` derives the table below mechanically from the evidence (`EVIDENCE` in the tool). Its status is **REFERENCE**:
- it names each league's reference model for the shadow-lane reviews and for the predictability map;
- it is **not a card input**;
- after P3 there is no case for making it one yet. That would be a `MODEL_CHANGE` requiring the user's explicit instruction.

| Target | A1 | TB-1 | A1S | POP (population) |
|---|---|---|---|---|
| **Side** | EPL, La Liga, Bundesliga, Serie A, Ligue 1, AFL, NBA, WNBA, NBL, NHL, ATP | NFL, MLB | — | NRL, and every league without held-out evidence |
| **Total** | La Liga, Bundesliga, NBA, WNBA, NBL | — | MLB (2026 only) | EPL, Serie A, Ligue 1, NFL, AFL, NRL, NHL, ATP, and every unvalidated league |

TB-1's own intervals against the population (`p4_tb1_intervals.json`) are significant on sides in NBL, WNBA, NBA, NHL, EPL, NFL, AFL and MLB, but not NRL. On totals they are significant only in the WNBA, and the EPL is significantly worse.

**Validity repairs to `tools/team_baseline.py` `resolution` flags.** Each flag was checked against both this interval and the multi-season TB-1 v A0 comparison in `research/sport_models_2026-09-26/validation_results.json`:

| Flag | Single season | Multi-season | Decision |
|---|---|---|---|
| NRL sides | [−0.0294, +0.0044] | — | **withdrawn** |
| NFL totals | [−0.0184, +0.0017] | 2021–25: 0.2403 v 0.2423, n = 1,359 | **withdrawn** |
| NBA totals | [−0.0181, +0.0005] | 2023–26: 0.2129 v 0.2308, n = 3,689 | **kept** |

## P5 — the predictability map (EXPLORATORY; descriptive)

`p5_predictability_results.json` holds the full band tables. The headline table is above.

**Calibration of the models' STRONG band:**
- basketball and the AFL are well calibrated or under-confident;
- the NFL and NRL 0.70–0.80 bands are over-confident (67% at 0.74–0.75);
- EPL three-way favourites at 0.70+ are rare, and the sample is too small (17) to read.

## The open 2025 MLB test (`T-MLB-V2-2025`, preregistered 2026-09-26(c))

P1's statsapi pull made the test runnable, so it was run exactly as registered: `python tools/mlb_model.py validate --season 2025` (`t_mlb_v2_2025.json`). This is separate from P1.
- **Data:** 2,121 games; mean Brier over home win and totals 6.5–10.5.
- **Result:** A1 0.2365 v A0 0.2388; A1 − A0 = **−0.0023 [−0.0042, −0.0005]**.
- **Verdict: replicated.** The v2 team prior (selected on 2022) beats the population on a season it has not seen.

## What was not done, and why

- **No model constant was changed.** The P5 over-confidence in the NFL and NRL bands and the NHL total failure are candidates for the next preregistered model version, **not** retrofits on the data that revealed them.
- **The other soccer competitions were not validated.** The 80 soccer cards spread across more than 30 competitions (AFC Champions League, Ligue 3, domestic cups, the Chinese Super League, women's competitions), so validating a few more major leagues would cover very few cards.
- **The prospective evidence is still zero.** `C-SPORT-SHADOW` and `C-MLB-SHADOW` have no frozen rows, and `C-BASELINE-SKILL` has no prospective decisions. Nothing here substitutes for them.

## Files

| File | What it is |
|---|---|
| `PREREGISTRATION.md` | P1–P4, committed before any run (`cc447c9`) |
| `mlb_starters.py` → `mlb_starters_results.json` | P1 (statsapi cache in `cache/`, git-ignored) |
| `t_mlb_v2_2025.json` | `T-MLB-V2-2025`, the output of `mlb_model.py validate --season 2025` |
| `p2_coverage.py` → `p2_coverage_results.json` | P2 |
| `p3_cards_mlb.py` → `p3_mlb_results.json`; `p3_cards_other.py` → `p3_other_results.json`; `p3_pooled.py` → `p3_pooled_results.json` | P3 |
| `p4_tb1_intervals.py` → `p4_tb1_intervals.json` | P4 input: TB-1 against the population, with intervals |
| `p5_predictability_map.py` → `p5_predictability_results.json` | P5 |
| `../../tools/model_anchor.py`, `../../tools/test_model_anchor.py` | The derived reference registry |

**To reproduce:** run each script from this folder, in the order above. `p3_cards_other.py` and `p5_predictability_map.py` read the ESPN caches of `research/base_rates_2026-09-25` and fetch only the few missing in-season days.
