# Recency, rebound and the value of the last game

**Opened 2026-09-19.** Empirical answer to a recurring question: *when a team or player performs poorly, should the next forecast move toward a bounce-back?*

**Headline: no.** Across every test below, the previous game's result carries essentially no information about the next, and conditioning on "high calibre" does not change that. The point estimates for a rebound are **negative or zero**, not positive. Nothing in this document licenses a bounce-back adjustment, and nothing licenses a hangover adjustment either.

**What this document is.** Historical field-owner frequencies and out-of-sample prediction comparisons, with samples, confidence intervals and selection caveats stated. They are empirical estimates on one season of one competition, not identities, not universal bounds and not fitted coefficients (`L-087`). They inform how much weight recent results may carry; they do not by themselves change a rank. Governing scoring and evaluation rules remain in [`SCORING_AND_VALIDATION.md`](SCORING_AND_VALIDATION.md).

---

## 1. Method

Population: **all 2,297 completed MLB 2026 regular-season games through 18 September** (4,594 team-games), from `statsapi.mlb.com/api/v1/schedule?...&hydrate=linescore`, retrieved 2026-09-19. Pitcher tests use the **108 starters with ≥20 games started**, via `people/{id}/stats?stats=gameLog&group=pitching`, restricted to their starts (2,784 consecutive-start pairs).

The baseline for every "did they rebound?" test is the unit's **own** mean with the two games in the comparison **left out**, so the baseline is not contaminated by the games being tested. An earlier version of this analysis omitted that correction and also mislabelled an opponent variable; both are fixed here and the corrected figures are the ones below.

**The hypothesis being tested.** H₀: after a poor game, the next game equals the unit's own mean — ordinary regression to the mean, no adjustment warranted. H₁: the next game exceeds the unit's own mean — a genuine rebound, which *would* warrant an adjustment.

---

## 2. Team scoring — is there a bounce-back?

Next-game runs versus the team's own leave-two-out mean:

| Condition | n | next | baseline | diff | 95% CI |
|---|---:|---:|---:|---:|---|
| previous game 0 runs | 282 | 4.372 | 4.475 | **−0.102** | [−0.456, +0.251] |
| previous game ≤1 run | 787 | 4.346 | 4.475 | **−0.129** | [−0.344, +0.086] |
| previous game ≤2 runs | 1,420 | 4.374 | 4.486 | **−0.112** | [−0.272, +0.047] |
| previous game ≤3 runs | 2,043 | 4.397 | 4.483 | **−0.086** | [−0.222, +0.050] |
| previous game ≥8 runs | 745 | 4.656 | 4.511 | +0.145 | [−0.098, +0.387] |

**Every low-scoring condition has a negative point estimate.** Teams that were shut out score *slightly below* their own average next time, not above. No interval excludes zero, so the honest reading is "no detectable effect, and certainly not a rebound".

### Does high calibre change it? — the specific question asked

| Condition | n | next | baseline | diff | 95% CI |
|---|---:|---:|---:|---:|---|
| **Top-10 offence**, previous ≤2 runs | 425 | 4.736 | 4.862 | **−0.126** | [−0.438, +0.186] |
| **Bottom-10 offence**, previous ≤2 runs | 520 | 4.090 | 4.183 | −0.093 | [−0.353, +0.168] |

**The best offences in the league do not rebound harder than the worst.** The two estimates are statistically indistinguishable and both are negative. The intuition that "good players will bounce back" is not visible in the data at all.

### After a string of poor games

| Condition | n | diff | 95% CI |
|---|---:|---:|---|
| 2 straight ≤3 runs | 928 | +0.005 | [−0.207, +0.217] |
| 3 straight ≤3 runs | 429 | +0.160 | [−0.163, +0.484] |
| 4 straight ≤3 runs | 192 | +0.212 | [−0.265, +0.688] |

This is the **only** slice with a positive drift, and it grows with streak length — which is mildly suggestive. But no interval excludes zero, the sample shrinks fast, and this is exactly the slice most exposed to selection. **Treat as a watch item, not a finding.** It may also be mechanical: a team on a four-game scoring drought is disproportionately likely to have faced hard pitching, and the next opponent regresses.

### What actually correlates with next-game runs

| Predictor | r | R² |
|---|---:|---:|
| Opponent's season runs **allowed** | +0.158 | **2.50%** |
| Team's own season runs/game | +0.098 | 0.96% |
| **Previous game's runs** | **+0.029** | **0.08%** |

Lag-1 autocorrelation of a team's own runs: **+0.019** (4,564 pairs).

Variance of runs in a team-game is **10.36** (SD 3.22). All three season-level predictors together account for at most ~3.5%. **The opponent matters roughly 30× more than the team's own last game.**

---

## 3. Pitchers — the sharper version of the question

*"A high-calibre pitcher concedes a lot, then suddenly strikes out a lot and concedes little next start."* Tested directly (108 starters):

| Condition | n | next | own avg | diff | 95% CI |
|---|---:|---:|---:|---:|---|
| next-start **ER** after ≥6 ER | 228 | 2.49 | 2.51 | **−0.017** | [−0.279, +0.244] |
| next-start ER after ≥5 ER | 424 | 2.47 | 2.47 | +0.004 | [−0.187, +0.195] |
| next-start **K** after ≥6 ER | 228 | 4.81 | 4.88 | **−0.070** | [−0.352, +0.212] |
| next-start IP after ≥6 ER | 228 | 5.39 | 5.43 | −0.040 | [−0.200, +0.120] |
| next-start ER after 0 ER & 6+ IP | 340 | 2.31 | 2.30 | +0.003 | [−0.197, +0.203] |
| **Elite (top-25 ERA)**, next ER after ≥5 ER | 52 | 1.77 | 1.77 | **+0.003** | [−0.522, +0.528] |
| **Elite**, next K after ≥5 ER | 52 | 5.94 | 6.26 | −0.314 | [−0.992, +0.364] |

Lag-1 autocorrelation of earned runs across consecutive starts: **−0.037** (2,784 pairs).

**The scenario does not occur as a pattern.** After being hit hard, a starter's next outing lands on his own average — not better, not worse. Strikeouts do **not** spike. Elite pitchers behave identically to everyone else (+0.003 ER). A dominant start predicts nothing either.

---

## 4. The operational test: does recent form beat season form?

Out-of-sample prediction of a starter's next-start earned runs, using only prior starts (n = 2,244 predictions):

| Predictor | MAE | RMSE |
|---|---:|---:|
| **League constant (2.385)** | 1.6085 | **1.9844** |
| **Season-to-date mean** | **1.6053** | 2.0177 |
| Last 5 starts | 1.7028 | 2.1324 |
| Last 3 starts | 1.7885 | 2.2433 |
| **Last 1 start** | **2.1444** | **2.7677** |

**The degradation is monotonic: the shorter the recency window, the worse the forecast.** A single prior start is the worst predictor tested — its RMSE is **39% worse than simply assuming the league average**.

**Caveats, stated plainly.** The population is established starters (≥20 GS), a selected and fairly homogeneous group; true-talent spread is compressed, which flatters the constant. That caveat does **not** touch the robust part of the result — *shorter windows lose to longer windows* — which holds regardless of how the constant performs. Earned runs are also a noisy target contaminated by defence, park and opponent; a component-based target (FIP inputs, xERA) would be less noisy, which is precisely the argument for using them.

---

## 5. What this means for the framework — control `R-1`

### `R-1` Recent results are evidence about a **rate**, never a forecast of a **deviation**

A poor recent run may be used **only** to revise the estimate of the unit's underlying rate, and only through a **named mechanism** visible in the disaggregated record (`G-L7`): a velocity or release-point change, an injury or IL stint, a role change, a lineup/personnel change, a surface or conditions change, a workload limit. Absent such a mechanism, the best estimate of the next performance is the unit's **longer-window rate**, and the card states that explicitly.

The following are **prohibited** as signed adjustments, in either direction:

- "They are due" / "they will bounce back" — no rebound effect exists (§2, §3).
- "They are cold, fade them" — no hangover effect exists either; the point estimates are ~0.
- "High-calibre players will correct it" — calibre does not change the estimate (§2, §3).
- Moving a centre onto a **one-game** comparator — the worst predictor measured (§4).

**Positive obligation.** When a card cites recent form, it prints: the window length, the number of observations, the longer-window rate it is being compared against, and the **named mechanism** if the centre is being moved. A recent-form citation with no mechanism widens the distribution; it does not move the centre.

**This validates existing behaviour and corrects a recorded success.** `P-443` (Molina: kept the good-start branch alive on FIP 3.82 / xERA 4.08 against a 5.24 ERA — 5.2 scoreless innings) and `P-449` (Ray: refused to let two poor September starts define him — six innings, six strikeouts) are **exactly right** and are now empirically supported. Conversely, `P-453`'s Rank #1 rested on Harrison's *three-start* run of 17 ER in 7.1 IP — the third-worst predictor in the table — and it won. That card is currently recorded as a methodological success; on this evidence it was **directionally lucky**, and the log should not be read as evidence that three-start form is a reliable current-regime signal. The distinguishing feature of the genuine successes is that they used **underlying-rate estimators to override recent results**, not recent results to override the rate.

### Cross-sport application

The tests above are MLB. The **mechanism** — that single-game results are dominated by within-game variance and carry little signal — is general, but the magnitudes are not transferable and must be derived per competition before use.

| Sport | Status | Note |
|---|---|---|
| MLB team runs; MLB starter ER | **DERIVED** (§2–§4) | |
| NBA, WNBA, NBL team points; NHL team goals; EPL team goals | **DERIVED 2026-09-25** (§7) | Same conclusion as MLB in all five: no rebound; the one-game window is the worst predictor tested |
| Cricket innings / phase | `NOT_YET_DERIVED` | Conditions and toss dominate; a prior innings on a *different strip* is a weaker comparator than a prior MLB start. `P-457` moved a 5-over centre onto one observation and lost |
| Soccer goals, other competitions | `NOT_YET_DERIVED` | EPL is derived (§7). Do not transfer it to cup or lower-tier competitions without deriving them. Finishing variance is large relative to the mean (`P-441`, `P-438`) |
| NPB runs | `NOT_YET_DERIVED` | Do **not** import the MLB figures. `P-458` moved a total centre above a 9-game same-venue base rate on one comparator and lost |
| Other basketball leagues (LKL, EuroLeague, LMB …), AFL, NRL, NFL, tennis | `NOT_YET_DERIVED` | The qualitative result replicated in six competitions (§7). Magnitudes still need deriving per competition before any number is quoted |

Until a sport's figures are derived, `R-1`'s **qualitative** requirement still applies: mechanism or width, never a bare rebound lean.

### Where the effort should go instead

The opponent explains ~30× more next-game variance than the unit's own last game (§2). For a totals or run-line card, marginal research time is better spent on **the opposing starter, the bullpen chain, the confirmed lineup and the conditions** than on the subject team's last result. That is where §6 and §7 below focus.

---

## 6. Related controls

`G-L7` (disaggregated record before an aggregate carries direction) · `G-L11` (real numerators before a small-sample rate takes a signed adjustment) · `G-L20` (a direct comparable gets explicit mass — but see §4: a *single* comparable is the weakest predictor measured, so `G-L20` mass must be sized accordingly) · `M13`, `M17` in the recurring-mistake registry · [`BASE_RATES_REGISTER.md`](BASE_RATES_REGISTER.md) for the frequencies themselves.

**Reproduction.** Every figure is recomputable from the two public endpoints named in §1. Refresh per season; a figure cited more than one completed season after 2026-09-19 is `STALE` until recomputed.

---

<!-- RESEARCH-2026-09-25 -->
## 7. Cross-sport derivation — basketball, hockey, soccer (added 2026-09-25)

**Why.** §5 required the magnitudes to be derived per competition before `R-1` could cite a number outside MLB. This section derives them for the five team-sport competitions carded most often after MLB.

**Population and method.** Regular-season games, retrieved 2026-09-25:

| Competition | Games | Team-games (out of sample) |
|---|---:|---:|
| NBA 2025-26 | 1,235 | 2,152 |
| WNBA 2026 | 327 | 496 |
| NBL 2025-26 | 165 | 222 |
| NHL 2025-26 | 1,312 | 2,290 |
| EPL 2025-26 | 380 | 600 |

- **Target:** a team's own points (goals in the NHL and EPL).
- **Baseline:** the team's own leave-two-out mean, as in §1.
- **"Poor game":** the bottom quintile of the previous-game residual.
- **Out-of-sample:** each prediction uses only earlier games; each team needs at least 10 prior games (8 in the EPL); the opponent's defence is measured to date.
- **Code and results:** [`research/base_rates_2026-09-25/`](research/base_rates_2026-09-25/README.md) (`analyze_leagues.py`, `league_results.json`).

### 7.1 Is there a bounce-back?

| Competition | After a bottom-quintile game: next − own mean (95% CI) | After a top-quintile game | Lag-1 r (own points) |
|---|---|---|---:|
| NBA | **−1.21** [−2.37, −0.06] (n = 487) | +1.09 [−0.03, +2.22] | +0.019 |
| WNBA | −0.27 [−2.25, +1.70] (n = 128) | +1.82 [−0.33, +3.98] | +0.030 |
| NBL | −0.07 [−2.82, +2.68] (n = 65) | +2.39 [−0.51, +5.29] | +0.036 |
| NHL (goals) | +0.01 [−0.14, +0.16] (n = 519) | +0.06 [−0.08, +0.20] | −0.016 |
| EPL (goals) | −0.11 [−0.30, +0.07] (n = 150) | −0.09 [−0.27, +0.08] | −0.046 |

**No competition shows a rebound.**
- The only interval that excludes zero is the NBA's, and it points the other way: a poor game is followed by a slightly *below-average* next game.
- That is mild persistence. It is consistent with within-season changes in a team's true rate (injuries, rotation, trades), which is exactly the **named-mechanism** case `R-1` permits. It is not a licence to fade a cold team without naming the mechanism.
- Hockey and soccer show neither persistence nor rebound.

### 7.2 Which window predicts the next game best?

RMSE of next-game team points. The bracket is the change against the league constant (negative = better).

| Predictor | NBA | WNBA | NBL | NHL | EPL |
|---|---|---|---|---|---|
| League constant (running) | 13.08 | 12.84 | 13.32 | 1.730 | 1.135 |
| Season to date | 12.93 (−1.1%) | 12.30 (−4.2%) | 12.29 (−7.7%) | 1.731 (0.0%) | 1.135 (0.0%) |
| Last 10 | 13.33 (+1.9%) | 12.62 (−1.7%) | 11.93 (−10.4%) | 1.789 (+3.4%) | 1.160 (+2.2%) |
| Last 5 | 13.93 (+6.5%) | 12.95 (+0.9%) | 12.24 (−8.1%) | 1.872 (+8.2%) | 1.222 (+7.7%) |
| Last 3 | 14.69 (+12.3%) | 13.72 (+6.8%) | 12.92 (−3.0%) | 1.986 (+14.8%) | 1.303 (+14.9%) |
| **Last 1** | **17.76 (+35.7%)** | **16.46 (+28.2%)** | **15.71 (+18.0%)** | **2.421 (+39.9%)** | **1.562 (+37.6%)** |
| Season to date + opponent defence to date | **12.19 (−6.9%)** | **11.61 (−9.6%)** | **11.90 (−10.6%)** | 1.745 (+0.8%) | 1.146 (+1.0%) |
| Half season-to-date, half league | 12.89 (−1.5%) | 12.38 (−3.6%) | 12.58 (−5.6%) | **1.722 (−0.5%)** | **1.121 (−1.2%)** |

**Reading.**
1. **The one-game window is the worst predictor in every competition**, 18–40% worse than the league constant. This replicates §4 (MLB, +39%).
2. In the NBA, NHL and EPL, the shorter the window, the worse the forecast, monotonically. The NBL is the exception: last-10 beats season-to-date. That fits its three-season pattern of scoring rising through the season (`BASE_RATES_REGISTER.md` §7.1(c)), where a longer window lags the environment. It still does not favour last-3 or last-1.
3. **The opponent matters in basketball.** Adding the opponent's defence to date improves RMSE by 7–11%, more than any recency window. In hockey and soccer it adds nothing at team level; the target is too noisy.
4. **In hockey and soccer, a team's own season rate barely beats the league constant.** A half-way shrink to the league mean is the best of the simple predictors. Team-scoring leans in these sports need a named mechanism more than in any other sport tested.

### 7.3 A named mechanism that is measurable: back-to-backs

A team on the second night of a back-to-back, against a rested opponent. The figure is the margin residual against the season-to-date predictor (`analyze_extra.py`).

| Competition | n | Mean margin residual (95% CI) | Reading |
|---|---:|---|---|
| NBA | 261 | **−1.84** [−3.78, +0.11] | About two points, borderline; small next to a margin SD of about 15 |
| NHL | 253 | −0.20 goals [−0.53, +0.12] | Not distinguishable from zero |
| WNBA | 19 | −5.65 [−13.74, +2.44] | n too small |

- This is a **reference size for a named mechanism**, not a coefficient.
- A card that moves a margin centre for a back-to-back should move it by about this much or less, and say so.
- A card that moves a total for fatigue has no support here: NBA games with both teams on a back-to-back were −3.6 [−8.5, +1.4], n = 65.

### 7.4 What changes

- `R-1` now has derived magnitudes for six competitions. The rule is unchanged: recent form moves a rate only through a named mechanism, and otherwise widens.
- The operational corollary is new and cross-sport: **a one-game comparator should never carry more weight than the season rate.** In six of six competitions it is the worst predictor available.
- For basketball totals and margins, research time spent on the **opponent's defence and the confirmed rotation** buys more than time spent on the subject team's last result.
- **No coefficient is created.** The percentages above describe these seasons' out-of-sample errors; they are not weights to copy onto a card (`L-087`).
