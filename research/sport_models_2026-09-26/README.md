# Numerical models for every sport — rolling-origin validation (2026-09-26)

**Status: LEARNING_ONLY. Descriptive comparisons on public results data. Nothing here is a promotion, and no model output may appear on a card (`C-SPORT-SHADOW`, `C-MLB-SHADOW`).**

`tools/sport_models.py` carries an A0 baseline and an A1 challenger for every sport (listed in [`research/sport_shadow/README.md`](../sport_shadow/README.md)). This folder records how the A1 models did against A0 on every public results set that could be reached from the implementing session, and against TB-1 (`tools/team_baseline.py`) where TB-1 exists. There were two passes:
- the first pass, 2026-09-26(c), covered soccer, NFL, AFL, NBA 2013–15, MLB and ATP;
- the second pass, 2026-09-26(d), covered NHL, NBA 2023–26, WNBA and IPL cricket.

## Protocol

- **Priors declared first.** Every constant in `tools/sport_models.py` was committed in ac6fdc5 before the first run on real data. The second pass ran on the constants frozen in 0872a36 and changed none for it. Three routes failed and were re-selected on an earlier TUNE window (MLB, tennis, cricket); all three are disclosed below.
- **Rolling origin, leak-free.** Each game is forecast from games strictly before its date. Ratings are refit on each date, warm-started. Widths come only from earlier out-of-sample residuals.
- **Known ordering limit.** Tennis runs in tournament and round order. The source dates every match by its tournament's start, so when two tournaments start the same week, the Elo updates from one tournament's later rounds can precede the other's early rounds. This touches the A0 and A1 winner routes equally.
- **Proper scores only.** Each metric is a loss, so lower is better:
  - Brier and log loss on the result;
  - three-way RPS where draws exist, and the regulation three-way for hockey;
  - integer RPS (discrete CRPS) on the margin and the total;
  - Brier at one total line, fixed from pre-window history as floor(mean) + 0.5;
  - soccer: first-half total RPS and BTTS;
  - tennis: total-games RPS, total games at a fixed line, and three sets.
- **Uncertainty.** Each A1 − A0 figure is a paired mean with a 95% block-bootstrap interval. Blocks are ISO weeks, or tournaments for tennis. "A1 better" means the whole interval is below 0.
- **Market-blind.** No odds, lines or prices are inputs. Some source files also carry betting columns (NFL) or third-party forecasts (538's NBA file). The loaders read only the named score columns.

## Headline

| Sport (data) | Result / side | Margin | Totals | Against TB-1 |
|---|---|---|---|---|
| Soccer — EPL, La Liga, Bundesliga, Serie A, Ligue 1 (2022-23 to 2025-26; 7,061 matches) | **A1 better in all five** (3-way RPS −0.025 to −0.033) | **A1 better in all five** | Better in La Liga; better at the line in the Bundesliga; **no difference** in the EPL, Serie A and Ligue 1. BTTS no better (Ligue 1 slightly worse) | EPL: **better on the result** (−0.008); the same on totals |
| NFL (2021–2025; 1,359 games) | **A1 better** (−0.021) | **A1 better** | No difference | Better on the result by 0.005, but the interval crosses 0; the same on totals |
| AFL (2021–2024, plus 27 games of 2025; 873 games) | **A1 better** (−0.036) | **A1 better** | No difference | **Better on the result** (−0.012); **worse on the total at the line** (+0.008; the interval just crosses 0) |
| NBA (2023-24 to 2025-26; 3,701 games) | **A1 better** (−0.037) | **A1 better** | **A1 better** (−0.021 at the line) | **Better on both** (−0.008 result, −0.006 total) |
| NBA (2012-13 to 2014-15, first pass; 3,689 games) | **A1 better** (−0.036) | **A1 better** | **A1 better** | **Better on both** |
| WNBA (2022–2026; 1,308 games) | **A1 better** (−0.038) | **A1 better** | **A1 better** (−0.017 at the line) | **Better on both** (−0.008 result, −0.007 total) |
| NHL (2023-24 to 2025-26; 3,936 games) | **A1 better** (−0.0075; regulation 3-way also better) | **A1 better** | **A1 worse** (total RPS +0.008) | **Better on the result** (−0.003); **worse at the total line** (+0.002) |
| MLB, team-only core, v1 (2022–2024; 6,964 games) | No difference | No difference | No difference | **TB-1 better on the result** (+0.004) |
| MLB, team-only core, v2 (team_prior_games 120; TEST 2023–2024; 4,647 games) | **A1 better** (−0.0045) | No difference | **A1 better** | Level on the result; **better at the total line** (−0.0013) |
| ATP tennis v1 (2023 to January 2026; 7,814 matches) | **A1 better**, narrowly (−0.0017) | — | **Games route worse** (+0.118 RPS) | — |
| ATP tennis v2 (gap_sd 0.09; same window) | **A1 better**, narrowly | — | Games route **level to slightly better** (−0.0017 at the line) | — |
| IPL cricket v1 (2016–2026; 720 matches) | **A1 worse than a coin flip** (+0.009) | — | **A1 worse** on first-innings total RPS | — |
| IPL cricket v2 (elo_k 4, lam_team 200; TEST 2020–2026; 482 matches) | No difference from a coin flip (+0.004, the interval crosses 0) | — | No difference | — |

**Not validated anywhere yet:** NBL, NRL, rugby union, the Asian baseball leagues (NPB, KBO, CPBL), and cricket outside the IPL. No public results for them could be reached. `python tools/sport_models.py validate --league <key> --from … --to …` runs the same comparison from ESPN, or from a `--csv` results file.

**What this does and does not show.**
- **Results and margins.** A pooled team-strength model with a sport-native distribution clearly beats the league baseline in soccer, the NFL, AFL, NBA, WNBA and NHL. It also beats the TB-1 baseline the cards already print in the EPL, AFL, NBA, WNBA and NHL.
- **Totals.** The model helps in basketball (NBA and WNBA, clearly), in two soccer leagues, and in MLB after the v2 re-selection (not independent). It is level elsewhere, and worse in the NHL.
- **Cricket.** IPL results are close to a coin flip for a team-strength model. v2 gets the model to "no worse than the baseline" and no further.
- **The cards.** None of this is evidence about the cards. Their skill is measured by `C-BASELINE-SKILL` and `T-RM1-PROSPECTIVE`, and the models' prospective record by the shadow lanes.

## v2 re-selections (disclosed)

Three v1 routes failed. Each was diagnosed (`diagnose.py`, `diagnostics.json`). Then one parameter per component was re-selected on an **earlier** TUNE window, with a selection rule declared first (`tune_v2.py`):

- **MLB team-only core was overconfident.** v1's P(home win) ranged from 0.08 to 0.90 (SD 0.147).
  - Grid: team_prior_games 20, 40, 60, 80, 120, 160. TUNE: 2022. Rule: lowest win log loss. Selected: **120**.
  - `tools/mlb_model.py` uses it too (`MLB-A1-shadow/2026-09-26b`).
- **The tennis games route was biased toward close matches.** It predicted 24.9 games against 23.7 actual, and 45% three-setters against 37%.
  - v2 adds a match-level random effect on the serve-point gap, which keeps the winner probability unchanged.
  - Grid: gap_sd 0, 0.03, 0.06, 0.09, 0.12. TUNE: 2021–2022. Rule: lowest total-games RPS. Selected: **0.09**.
- **Cricket (IPL) Elo over-reacted and the ridge model over-fitted.** Both components were tuned independently on TUNE 2016–2019:
  - result: elo_k 4, 8, 12, 24; rule: lowest win log loss; selected **4**;
  - first-innings total: lam_team 6, 20, 60, 200 innings; rule: lowest total RPS; selected **200**.

  Both selections shrink the model toward A0, because IPL team strength barely carries from match to match.

**The v2 TEST numbers are not independent evidence**, because the v1 failures were seen on those windows first. The independent tests are:
- the 2025 MLB season: `python tools/mlb_model.py validate --season 2025`;
- competitions neither version has seen, for cricket: the BBL, CPL, T20Is and The Hundred;
- the prospective shadow lanes.

The **Dixon–Coles** candidate (soccer, ρ fitted on each training window) made no measurable difference in any league: every interval includes 0. It stays off, as the recipe requires.

## Full tables

**epl** — 1520 forecasts, 2022-08-01 to 2026-06-30; fixed total line 2.5

| Metric | A0 | A1 | A1 − A0 (95% block CI) | Verdict | A1 v TB-1 (95% CI) |
|---|---:|---:|---|---|---|
| Result (home win) Brier | 0.2473 | 0.2151 | -0.0322 (-0.0397, -0.0241) | **A1 better** | -0.0079 (-0.0133, -0.0026), n 1480 |
| Result (3-way) RPS | 0.2317 | 0.2027 | -0.0290 (-0.0356, -0.0219) | **A1 better** | — |
| Result log loss | 1.0683 | 0.9854 | -0.0829 (-0.1026, -0.0617) | **A1 better** | — |
| Margin RPS | 1.0298 | 0.9323 | -0.0975 (-0.1220, -0.0735) | **A1 better** | — |
| Total RPS | 0.9234 | 0.9279 | +0.0045 (-0.0075, +0.0160) | no clear difference | — |
| Total at fixed line (Brier) | 0.2447 | 0.2445 | -0.0002 (-0.0050, +0.0045) | no clear difference | -0.0012 (-0.0057, +0.0032), n 1480 |
| First-half total RPS | 0.5906 | 0.5921 | +0.0015 (-0.0048, +0.0076) | no clear difference | — |
| BTTS Brier | 0.2460 | 0.2472 | +0.0012 (-0.0024, +0.0048) | no clear difference | — |

**laliga** — 1510 forecasts, 2022-08-01 to 2026-06-30; fixed total line 2.5

| Metric | A0 | A1 | A1 − A0 (95% block CI) | Verdict | A1 v TB-1 (95% CI) |
|---|---:|---:|---|---|---|
| Result (home win) Brier | 0.2491 | 0.2160 | -0.0332 (-0.0401, -0.0260) | **A1 better** | — |
| Result (3-way) RPS | 0.2260 | 0.1988 | -0.0272 (-0.0329, -0.0213) | **A1 better** | — |
| Result log loss | 1.0624 | 0.9822 | -0.0802 (-0.0983, -0.0629) | **A1 better** | — |
| Margin RPS | 0.8855 | 0.7948 | -0.0907 (-0.1108, -0.0714) | **A1 better** | — |
| Total RPS | 0.8877 | 0.8655 | -0.0222 (-0.0388, -0.0069) | **A1 better** | — |
| Total at fixed line (Brier) | 0.2499 | 0.2429 | -0.0070 (-0.0135, -0.0006) | **A1 better** | — |
| First-half total RPS | 0.5762 | 0.5658 | -0.0104 (-0.0187, -0.0027) | **A1 better** | — |
| BTTS Brier | 0.2489 | 0.2480 | -0.0009 (-0.0054, +0.0035) | no clear difference | — |

**bundesliga** — 1224 forecasts, 2022-08-01 to 2026-06-30; fixed total line 3.5

| Metric | A0 | A1 | A1 − A0 (95% block CI) | Verdict | A1 v TB-1 (95% CI) |
|---|---:|---:|---|---|---|
| Result (home win) Brier | 0.2470 | 0.2154 | -0.0315 (-0.0400, -0.0225) | **A1 better** | — |
| Result (3-way) RPS | 0.2314 | 0.2031 | -0.0283 (-0.0353, -0.0212) | **A1 better** | — |
| Result log loss | 1.0761 | 0.9986 | -0.0775 (-0.0981, -0.0548) | **A1 better** | — |
| Margin RPS | 1.1110 | 0.9997 | -0.1113 (-0.1403, -0.0816) | **A1 better** | — |
| Total RPS | 0.9851 | 0.9716 | -0.0135 (-0.0309, +0.0035) | no clear difference | — |
| Total at fixed line (Brier) | 0.2432 | 0.2366 | -0.0066 (-0.0125, -0.0007) | **A1 better** | — |
| First-half total RPS | 0.6435 | 0.6386 | -0.0049 (-0.0136, +0.0045) | no clear difference | — |
| BTTS Brier | 0.2411 | 0.2397 | -0.0014 (-0.0067, +0.0037) | no clear difference | — |

**seriea** — 1510 forecasts, 2022-08-01 to 2026-06-30; fixed total line 2.5

| Metric | A0 | A1 | A1 − A0 (95% block CI) | Verdict | A1 v TB-1 (95% CI) |
|---|---:|---:|---|---|---|
| Result (home win) Brier | 0.2420 | 0.2099 | -0.0321 (-0.0394, -0.0244) | **A1 better** | — |
| Result (3-way) RPS | 0.2288 | 0.1963 | -0.0325 (-0.0387, -0.0259) | **A1 better** | — |
| Result log loss | 1.0864 | 0.9909 | -0.0955 (-0.1143, -0.0758) | **A1 better** | — |
| Margin RPS | 0.9170 | 0.8160 | -0.1010 (-0.1211, -0.0800) | **A1 better** | — |
| Total RPS | 0.8518 | 0.8543 | +0.0025 (-0.0104, +0.0149) | no clear difference | — |
| Total at fixed line (Brier) | 0.2504 | 0.2506 | +0.0001 (-0.0053, +0.0053) | no clear difference | — |
| First-half total RPS | 0.5326 | 0.5355 | +0.0030 (-0.0035, +0.0092) | no clear difference | — |
| BTTS Brier | 0.2511 | 0.2534 | +0.0023 (-0.0015, +0.0062) | no clear difference | — |

**ligue1** — 1297 forecasts, 2022-08-01 to 2026-06-30; fixed total line 2.5

| Metric | A0 | A1 | A1 − A0 (95% block CI) | Verdict | A1 v TB-1 (95% CI) |
|---|---:|---:|---|---|---|
| Result (home win) Brier | 0.2469 | 0.2203 | -0.0266 (-0.0338, -0.0196) | **A1 better** | — |
| Result (3-way) RPS | 0.2332 | 0.2086 | -0.0247 (-0.0303, -0.0189) | **A1 better** | — |
| Result log loss | 1.0705 | 1.0001 | -0.0704 (-0.0872, -0.0529) | **A1 better** | — |
| Margin RPS | 1.0012 | 0.9170 | -0.0842 (-0.1056, -0.0621) | **A1 better** | — |
| Total RPS | 0.9420 | 0.9431 | +0.0011 (-0.0126, +0.0151) | no clear difference | — |
| Total at fixed line (Brier) | 0.2488 | 0.2489 | +0.0001 (-0.0050, +0.0056) | no clear difference | — |
| First-half total RPS | 0.5956 | 0.6010 | +0.0054 (-0.0015, +0.0122) | no clear difference | — |
| BTTS Brier | 0.2483 | 0.2525 | +0.0042 (+0.0001, +0.0085) | **A1 worse** | — |

**nfl** — 1359 forecasts, 2021-09-01 to 2026-02-15; fixed total line 47.5

| Metric | A0 | A1 | A1 − A0 (95% block CI) | Verdict | A1 v TB-1 (95% CI) |
|---|---:|---:|---|---|---|
| Result (home win) Brier | 0.2491 | 0.2282 | -0.0209 (-0.0277, -0.0148) | **A1 better** | -0.0050 (-0.0105, +0.0008), n 1279 |
| Result (3-way) RPS | 0.2490 | 0.2283 | -0.0207 (-0.0274, -0.0149) | **A1 better** | — |
| Result log loss | 0.7119 | 0.6694 | -0.0424 (-0.0574, -0.0294) | **A1 better** | — |
| Margin RPS | 7.9437 | 7.4156 | -0.5281 (-0.6993, -0.3722) | **A1 better** | — |
| Total RPS | 7.7068 | 7.5980 | -0.1088 (-0.2299, +0.0114) | no clear difference | — |
| Total at fixed line (Brier) | 0.2423 | 0.2397 | -0.0026 (-0.0084, +0.0034) | no clear difference | -0.0005 (-0.0054, +0.0042), n 1279 |

**afl** — 873 forecasts, 2021-03-01 to 2025-10-01; fixed total line 151.5

| Metric | A0 | A1 | A1 − A0 (95% block CI) | Verdict | A1 v TB-1 (95% CI) |
|---|---:|---:|---|---|---|
| Result (home win) Brier | 0.2466 | 0.2106 | -0.0360 (-0.0462, -0.0257) | **A1 better** | -0.0116 (-0.0183, -0.0048), n 819 |
| Result (3-way) RPS | 0.2459 | 0.2100 | -0.0359 (-0.0461, -0.0256) | **A1 better** | — |
| Result log loss | 0.7352 | 0.6553 | -0.0798 (-0.1029, -0.0554) | **A1 better** | — |
| Margin RPS | 22.0707 | 19.1629 | -2.9078 (-3.6107, -2.2174) | **A1 better** | — |
| Total RPS | 16.9357 | 16.8068 | -0.1289 (-0.4256, +0.1556) | no clear difference | — |
| Total at fixed line (Brier) | 0.2308 | 0.2269 | -0.0039 (-0.0097, +0.0017) | no clear difference | +0.0083 (-0.0002, +0.0177), n 819 |

**nba** — 3689 forecasts, 2012-10-01 to 2015-04-30; fixed total line 192.5

| Metric | A0 | A1 | A1 − A0 (95% block CI) | Verdict | A1 v TB-1 (95% CI) |
|---|---:|---:|---|---|---|
| Result (home win) Brier | 0.2420 | 0.2065 | -0.0356 (-0.0402, -0.0308) | **A1 better** | -0.0087 (-0.0112, -0.0063), n 3635 |
| Result log loss | 0.6771 | 0.5994 | -0.0777 (-0.0879, -0.0670) | **A1 better** | — |
| Margin RPS | 7.4795 | 6.7305 | -0.7489 (-0.8498, -0.6480) | **A1 better** | — |
| Total RPS | 10.7815 | 9.9478 | -0.8337 (-0.9950, -0.6727) | **A1 better** | — |
| Total at fixed line (Brier) | 0.2308 | 0.2092 | -0.0216 (-0.0263, -0.0172) | **A1 better** | -0.0047 (-0.0070, -0.0025), n 3635 |

**nhl (second pass, 2026-09-26(d))** — 3936 forecasts, 2023-10-01 to 2026-06-30; fixed total line 6.5

| Metric | A0 | A1 | A1 − A0 (95% block CI) | Verdict | A1 v TB-1 (95% CI) |
|---|---:|---:|---|---|---|
| Result (home win) Brier | 0.2483 | 0.2408 | -0.0075 (-0.0107, -0.0042) | **A1 better** | -0.0029 (-0.0056, -0.0004), n 3875 |
| Result log loss | 0.6898 | 0.6743 | -0.0155 (-0.0222, -0.0085) | **A1 better** | — |
| Margin RPS | 1.4849 | 1.4488 | -0.0361 (-0.0497, -0.0219) | **A1 better** | — |
| Total RPS | 1.2894 | 1.2974 | +0.0080 (+0.0010, +0.0151) | **A1 worse** | — |
| Total at fixed line (Brier) | 0.2476 | 0.2491 | +0.0015 (-0.0004, +0.0033) | no clear difference | +0.0017 (+0.0003, +0.0030), n 3875 |
| Regulation 3-way RPS | 0.2373 | 0.2306 | -0.0067 (-0.0094, -0.0038) | **A1 better** | — |

**nba_recent (second pass; 2023-24 to 2025-26)** — 3701 forecasts, 2023-10-01 to 2026-06-30; fixed total line 230.5

| Metric | A0 | A1 | A1 − A0 (95% block CI) | Verdict | A1 v TB-1 (95% CI) |
|---|---:|---:|---|---|---|
| Result (home win) Brier | 0.2481 | 0.2112 | -0.0369 (-0.0418, -0.0321) | **A1 better** | -0.0080 (-0.0106, -0.0054), n 3649 |
| Result log loss | 0.6893 | 0.6105 | -0.0788 (-0.0896, -0.0680) | **A1 better** | — |
| Margin RPS | 8.9677 | 8.0199 | -0.9479 (-1.0792, -0.8130) | **A1 better** | — |
| Total RPS | 11.5800 | 10.8730 | -0.7070 (-0.8380, -0.5759) | **A1 better** | — |
| Total at fixed line (Brier) | 0.2489 | 0.2284 | -0.0205 (-0.0245, -0.0164) | **A1 better** | -0.0056 (-0.0077, -0.0032), n 3649 |

**wnba (second pass)** — 1308 forecasts, 2022-05-01 to 2026-09-20; fixed total line 163.5

| Metric | A0 | A1 | A1 − A0 (95% block CI) | Verdict | A1 v TB-1 (95% CI) |
|---|---:|---:|---|---|---|
| Result (home win) Brier | 0.2500 | 0.2121 | -0.0379 (-0.0457, -0.0297) | **A1 better** | -0.0076 (-0.0112, -0.0035), n 1253 |
| Result log loss | 0.6932 | 0.6126 | -0.0806 (-0.0981, -0.0631) | **A1 better** | — |
| Margin RPS | 8.0097 | 7.0994 | -0.9104 (-1.1062, -0.7297) | **A1 better** | — |
| Total RPS | 10.5024 | 9.9495 | -0.5529 (-0.7463, -0.3590) | **A1 better** | — |
| Total at fixed line (Brier) | 0.2426 | 0.2260 | -0.0166 (-0.0231, -0.0100) | **A1 better** | -0.0066 (-0.0101, -0.0028), n 1253 |

**mlb (v1, team_prior_games 20)** — 6964 forecasts, 2022-04-01 to 2024-10-01; fixed total line 9.5

| Metric | A0 | A1 | A1 − A0 (95% block CI) | Verdict | A1 v TB-1 (95% CI) |
|---|---:|---:|---|---|---|
| Result (home win) Brier | 0.2497 | 0.2491 | -0.0007 (-0.0033, +0.0020) | no clear difference | +0.0041 (+0.0025, +0.0058), n 6964 |
| Result log loss | 0.6926 | 0.6932 | +0.0006 (-0.0050, +0.0062) | no clear difference | — |
| Margin RPS | 2.4587 | 2.4640 | +0.0053 (-0.0097, +0.0204) | no clear difference | — |
| Total RPS | 2.4551 | 2.4495 | -0.0056 (-0.0152, +0.0041) | no clear difference | — |
| Total at fixed line (Brier) | 0.2370 | 0.2361 | -0.0009 (-0.0023, +0.0004) | no clear difference | +0.0001 (-0.0007, +0.0009), n 6964 |

**mlb v1 on the TEST window** — 4647 forecasts, 2023-04-01 to 2024-10-01; fixed total line 8.5

| Metric | A0 | A1 | A1 − A0 (95% block CI) | Verdict | A1 v TB-1 (95% CI) |
|---|---:|---:|---|---|---|
| Result (home win) Brier | 0.2500 | 0.2508 | +0.0007 (-0.0025, +0.0038) | no clear difference | +0.0050 (+0.0030, +0.0070), n 4647 |
| Result log loss | 0.6932 | 0.6966 | +0.0034 (-0.0034, +0.0103) | no clear difference | — |
| Margin RPS | 2.4725 | 2.4840 | +0.0115 (-0.0065, +0.0284) | no clear difference | — |
| Total RPS | 2.4764 | 2.4697 | -0.0068 (-0.0185, +0.0046) | no clear difference | — |
| Total at fixed line (Brier) | 0.2500 | 0.2488 | -0.0012 (-0.0028, +0.0004) | no clear difference | -0.0004 (-0.0015, +0.0007), n 4647 |

**mlb v2 on the TEST window (team_prior_games 120)** — 4647 forecasts, 2023-04-01 to 2024-10-01; fixed total line 8.5

| Metric | A0 | A1 | A1 − A0 (95% block CI) | Verdict | A1 v TB-1 (95% CI) |
|---|---:|---:|---|---|---|
| Result (home win) Brier | 0.2500 | 0.2456 | -0.0045 (-0.0062, -0.0027) | **A1 better** | -0.0002 (-0.0008, +0.0004), n 4647 |
| Result log loss | 0.6932 | 0.6842 | -0.0090 (-0.0125, -0.0054) | **A1 better** | — |
| Margin RPS | 2.4725 | 2.4698 | -0.0027 (-0.0132, +0.0073) | no clear difference | — |
| Total RPS | 2.4764 | 2.4603 | -0.0162 (-0.0242, -0.0080) | **A1 better** | — |
| Total at fixed line (Brier) | 0.2500 | 0.2479 | -0.0021 (-0.0034, -0.0010) | **A1 better** | -0.0013 (-0.0021, -0.0005), n 4647 |

**atp v1 (gap_sd 0)** — 7814 forecasts, 2023-01-01 to 2026-09-20

| Metric | A0 | A1 | A1 − A0 (95% block CI) | Verdict | A1 v TB-1 (95% CI) |
|---|---:|---:|---|---|---|
| Winner (player A) Brier | 0.2237 | 0.2220 | -0.0017 (-0.0033, -0.0001) | **A1 better** | — |
| Result log loss | 0.6390 | 0.6342 | -0.0049 (-0.0088, -0.0011) | **A1 better** | — |
| Total games RPS | 3.7232 | 3.8407 | +0.1176 (+0.0645, +0.1701) | **A1 worse** | — |
| Total games at fixed line (Brier) | 0.2442 | 0.2519 | +0.0077 (+0.0041, +0.0113) | **A1 worse** | — |
| Three sets (Brier) | 0.2326 | 0.2389 | +0.0063 (+0.0036, +0.0090) | **A1 worse** | — |

**atp v2 on the same window (gap_sd 0.09)** — 7814 forecasts, 2023-01-01 to 2026-09-20

| Metric | A0 | A1 | A1 − A0 (95% block CI) | Verdict | A1 v TB-1 (95% CI) |
|---|---:|---:|---|---|---|
| Winner (player A) Brier | 0.2237 | 0.2220 | -0.0017 (-0.0033, -0.0002) | **A1 better** | — |
| Result log loss | 0.6390 | 0.6342 | -0.0049 (-0.0089, -0.0011) | **A1 better** | — |
| Total games RPS | 3.7232 | 3.7128 | -0.0104 (-0.0320, +0.0122) | no clear difference | — |
| Total games at fixed line (Brier) | 0.2442 | 0.2425 | -0.0017 (-0.0033, -0.0001) | **A1 better** | — |
| Three sets (Brier) | 0.2326 | 0.2321 | -0.0005 (-0.0017, +0.0007) | no clear difference | — |

**ipl v1 (elo_k 24, lam_team 6), 2016–2026** — 720 forecasts, 2016-01-01 to 2026-09-20; fixed total line 160.5

| Metric | A0 | A1 | A1 − A0 (95% block CI) | Verdict | A1 v TB-1 (95% CI) |
|---|---:|---:|---|---|---|
| Result Brier | 0.2500 | 0.2588 | +0.0088 (+0.0025, +0.0151) | **A1 worse** | — |
| Result log loss | 0.6931 | 0.7117 | +0.0186 (+0.0054, +0.0318) | **A1 worse** | — |
| Total RPS | 18.0654 | 18.4022 | +0.3368 (+0.0298, +0.6260) | **A1 worse** | — |
| Total at fixed line (Brier) | 0.2088 | 0.2135 | +0.0048 (-0.0006, +0.0101) | no clear difference | — |

**ipl v1 on the TEST window** — 482 forecasts, 2020-01-01 to 2026-09-20; fixed total line 165.5

| Metric | A0 | A1 | A1 − A0 (95% block CI) | Verdict | A1 v TB-1 (95% CI) |
|---|---:|---:|---|---|---|
| Result Brier | 0.2500 | 0.2599 | +0.0099 (+0.0031, +0.0171) | **A1 worse** | — |
| Result log loss | 0.6931 | 0.7138 | +0.0206 (+0.0067, +0.0355) | **A1 worse** | — |
| Total RPS | 18.9513 | 19.3095 | +0.3582 (-0.0160, +0.7281) | no clear difference | — |
| Total at fixed line (Brier) | 0.2207 | 0.2258 | +0.0051 (-0.0013, +0.0116) | no clear difference | — |

**ipl v2 on the TEST window (elo_k 4, lam_team 200)** — 482 forecasts, 2020-01-01 to 2026-09-20; fixed total line 165.5

| Metric | A0 | A1 | A1 − A0 (95% block CI) | Verdict | A1 v TB-1 (95% CI) |
|---|---:|---:|---|---|---|
| Result Brier | 0.2500 | 0.2537 | +0.0037 (-0.0003, +0.0075) | no clear difference | — |
| Result log loss | 0.6931 | 0.7006 | +0.0075 (-0.0006, +0.0152) | no clear difference | — |
| Total RPS | 18.9514 | 18.8422 | -0.1091 (-0.3281, +0.1000) | no clear difference | — |
| Total at fixed line (Brier) | 0.2207 | 0.2191 | -0.0016 (-0.0057, +0.0023) | no clear difference | — |

Dixon–Coles candidate (soccer, A1dc − A1 on the result RPS):
- epl: -0.00005 (95% CI -0.00018 to +0.00008)
- laliga: +0.00007 (95% CI -0.00002 to +0.00016)
- bundesliga: -0.00016 (95% CI -0.00051 to +0.00018)
- seriea: -0.00012 (95% CI -0.00032 to +0.00009)
- ligue1: +0.00016 (95% CI -0.00003 to +0.00035)

TUNE windows:
- mlb_tune_20: win_logloss A1 0.6864 (A0 0.6915)
- mlb_tune_40: win_logloss A1 0.6805 (A0 0.6915)
- mlb_tune_60: win_logloss A1 0.6782 (A0 0.6915)
- mlb_tune_80: win_logloss A1 0.6774 (A0 0.6915)
- mlb_tune_120: win_logloss A1 0.6773 (A0 0.6915)
- mlb_tune_160: win_logloss A1 0.6780 (A0 0.6915)
- atp_tune_0: games_rps A1 3.8913 (A0 3.7318)
- atp_tune_0.03: games_rps A1 3.8127 (A0 3.7318)
- atp_tune_0.06: games_rps A1 3.6985 (A0 3.7318)
- atp_tune_0.09: games_rps A1 3.6920 (A0 3.7318)
- atp_tune_0.12: games_rps A1 3.8106 (A0 3.7318)
- ipl_elo_k_tune_4: win_logloss A1 0.6890 (A0 0.6931)
- ipl_elo_k_tune_8: win_logloss A1 0.6918 (A0 0.6931)
- ipl_elo_k_tune_12: win_logloss A1 0.6959 (A0 0.6931)
- ipl_elo_k_tune_24: win_logloss A1 0.7077 (A0 0.6931)
- ipl_lam_team_tune_6: total_rps A1 16.5489 (A0 16.2558)
- ipl_lam_team_tune_20: total_rps A1 16.2921 (A0 16.2557)
- ipl_lam_team_tune_60: total_rps A1 16.2202 (A0 16.2557)
- ipl_lam_team_tune_200: total_rps A1 16.2062 (A0 16.2557)

## Reproduce

```
python research/sport_models_2026-09-26/validate_public.py            # every dataset, about 3 minutes each (NHL, NBA 2023-26 and WNBA need `pip install pyarrow`)
python research/sport_models_2026-09-26/tune_v2.py --sport mlb --phase tune --value 120   # one v2 cell (also atp, ipl)
python research/sport_models_2026-09-26/validate_public.py --merge    # combine parts into validation_results.json
python research/sport_models_2026-09-26/report.py                     # the tables above
python research/sport_models_2026-09-26/diagnose.py                   # the two v1 failure diagnostics
```

`validate_public.py` now runs with the v2 constants, so a rerun of its MLB, ATP and IPL cells reproduces v2, not v1. v1 is `tools/sport_models.py` at ac6fdc5. Raw downloads are cached in the git-ignored `cache/`. Their URLs and SHA-256 are in `provenance.json`.

## Sources and licences

- **openfootball/football.json:** public domain.
- **nflverse/nfldata:** only scores and teams are read.
- **akareen/AFL-Data-Analysis:** `team_1` is treated as the home side; neutral venues are not flagged.
- **fivethirtyeight/data `nba-elo`:** CC BY 4.0; only scores are read.
- **Tennismylife/TML-Database.**
- **sportsdataverse** (`hoopR-nba-data`, `wehoop-wnba-data`, `fastRhockey-nhl-data`): ESPN and NHL schedules and scoring, compiled from the leagues' feeds. The NBA repository also carries a betting-lines folder, which is never fetched.
- **ritesh-ojha/IPL-DATASET:** match information and ball-by-ball data. Renamed franchises are mapped to their current names.
- **Retrosheet game logs via chadwickbureau/retrosheet:** *"The information used here was obtained free of charge from and is copyrighted by Retrosheet. Interested parties may contact Retrosheet at www.retrosheet.org."*

No third-party data file is committed.
