# League-neutral basketball, ML/RL adequacy and simulations — review, 21 October 2026

**Status: REVIEW ONLY.** Owner request. Nothing in this folder changes a rule, prompt, model, release, ID, grade or record. Recommendations need a prompt-7 or prompt-8 change before they take effect. Model numbers below are `HISTORICAL_DEVELOPMENT` evidence from unadmitted archive data (`FIELD_OWNER_ADMISSION_UNVERIFIED`): good enough for planning, never evidence of prospective skill.

Read at `main` 29e25a798 (local working tree, no uncommitted control changes).

## Summary

| Question | Answer |
|---|---|
| Can one basketball framework cover the NBA, NBL, EuroLeague and other leagues? | **Yes, and most of it already does.** The method (possessions × efficiency, one joint score distribution, explicit overtime) works the same way in all 11 leagues tested. What cannot be shared are the **numbers**: league mean total, home edge, widths and overtime rate differ a lot between leagues. The gap is that no league's numbers are currently admitted, so every chat re-derives them. A per-competition parameter sheet fixes that. |
| Is the ML/RL framework adequate as is? | **The design is adequate; the operation is not.** The written design (Oct 14) follows good practice. But in the week since, no model forecast has been frozen and committed before a game. Five practical gaps stop it: no pregame step in any prompt, no admitted basketball data in the learning store, weekly code changes that reset the clock, a test sized for leagues with many games per week, and calibration that is untested on the basketball models. RL is correctly excluded from forecasting. |
| Would simulations help? | **Not for basketball cards.** The normal distribution fits basketball margins and totals closely, so the hand table gives the exact answer and a simulation adds only noise. In a no-code chat, "simulations" cannot actually be run and invite made-up output. Exact score grids in repository code are better than Monte Carlo. Simulation earns its place only for path-dependent sports (tennis, cricket innings, baseball innings) and joint player props, and only in code. |
| Is 8 weeks enough? | **Eight weeks is a floor, not a length.** At the effects the stored basketball models actually show, a full-league shadow needs about 8 weeks in the NBA and 34 in the NBL against the league-only baseline. Against the team baseline a chat can compute by hand (TB-1), the NBL needs about 436 weeks, so it is not feasible. Card-only testing (about 3 cards a week per league) is not feasible in any league. |

## 1. What was examined

**Repository:**
- prompt 1 core and [BASKETBALL.md](../../prompts/1_sports/BASKETBALL.md);
- [RULES_BASKETBALL.md](../../../RULES_BASKETBALL.md) §0 and §9.2;
- [LEAGUE_PROFILES.md](../../../LEAGUE_PROFILES.md);
- [PROBABILITY_TOOLKIT.md](../../../PROBABILITY_TOOLKIT.md) §4;
- [BASE_RATES_REGISTER.md](../../../BASE_RATES_REGISTER.md) §7.1 and §7.8;
- [SELECTION_RULES.md](../../../SELECTION_RULES.md) §9;
- [ML_RL_IMPLEMENTATION_FRAMEWORK_2026-10-14.md](../../../ML_RL_IMPLEMENTATION_FRAMEWORK_2026-10-14.md) §§1, 7–11;
- [FORECAST_CYCLE_PROTOCOL.md](../../../FORECAST_CYCLE_PROTOCOL.md);
- [research/model_shadow/STATUS.md](../../model_shadow/STATUS.md);
- `ml/config.py`, `ml/shadow/lane.py`, `ml/calibration.py`;
- [CURRENT_RELEASES.csv](../../cycle_releases/CURRENT_RELEASES.csv);
- the 2026-10-16 full-history and 2026-10-21 retrospectives.

**New analysis.** The analysis covers every stored basketball development prediction (`research/model_shadow/BKB-*-r1/DEVELOPMENT_PREDICTIONS.csv`):
- rows with status FROZEN in test seasons 2023–2025;
- 11 competitions, 12,750 games.

For each game it compared the fitted joint model (`MODEL_*`), the league-only baseline (`BASE_*`) and TB-1 (`TB1_*`) against the final score. The per-league results are in [BKB_CROSS_LEAGUE.csv](BKB_CROSS_LEAGUE.csv). Method:
- Brier = (p − outcome)²; "Over" uses the file's league-median line;
- paired differences are model minus comparator per game, then averaged by ISO week;
- weeks needed = ⌈(2.802 × SD of week means ÷ effect)²⌉, minimum 8 (the register's formula, HYPOTHESIS_REGISTER / ML framework §9.6);
- calibration slope = logistic regression of the outcome on logit(p) (1 = calibrated, above 1 = under-confident);
- z = (actual − model mean) ÷ model SD for margin and total.

The analysis script ran outside the repository (MD-only operation), so it is described here instead of committed.

**Data warnings.**
- **Austria Bundesliga:** total SD 8.4 points and home-win rate 0.755 are not credible for basketball. That matches its OVERTIME_FIELD_IMPLAUSIBLE flag. Its row is listed but not used in any conclusion.
- **Greek league:** it carries IMPLAUSIBLE_SCORE_DISPERSION flags for old seasons. It is shown but treated with caution.
- **EuroBasket:** it produced no rows under this filter (three tournaments, development FAIL).

**External literature** checked for this review is listed under Sources.

## 2. Can one basketball framework be league-neutral?

### 2.1 What is already league-neutral

- **Prompt 1:** `1_sports/BASKETBALL.md` is written for every league. Step 6 says to resolve the exact competition's rules and **never import NBA defaults** (pace, totals, overtime rate, home edge, quarter length) into NBL, B.League, ACB, EuroLeague or other leagues.
- **Rules:** RULES_BASKETBALL §9.2 has the FIBA / WNBA / NBA rule-set table. Gate BK-P1 refuses a competition with no current regulation packet.
- **Model code:** `ml/config.py` maps the whole sport to one engine (`Basketball → gaussian, FULL_GAME_INCL_OT, tie_rule=overtime`) and fits each competition separately. The same code produced models for all 11 leagues below.

### 2.2 The structure transfers across leagues

The same joint-normal model, fitted per league, had a lower Brier score than the league-only baseline and TB-1 in every league. These are point estimates; against TB-1 the margin is small and often not significant:

| League | Games | Model Brier (home win) | League baseline | TB-1 | Model − baseline | Model − TB-1 | Calibration slope (SE) | Favourite ≥ 0.70: share, won |
|---|---:|---:|---:|---:|---:|---:|---|---|
| NBA | 3,692 | 0.2125 | 0.2479 | 0.2202 | −0.0354 | −0.0076 | 1.37 (0.06) | 23%, 82.5% |
| NBA G League | 1,599 | 0.2385 | 0.2486 | 0.2404 | −0.0101 | −0.0019 | 0.91 (0.12) | 9%, 73.2% |
| WNBA | 768 | 0.2188 | 0.2488 | 0.2201 | −0.0300 | −0.0013 | 1.14 (0.12) | 25%, 77.8% |
| NBL | 450 | 0.2278 | 0.2485 | 0.2309 | −0.0207 | −0.0031 | 1.21 (0.21) | 14%, 76.2% |
| EuroLeague | 979 | 0.2118 | 0.2321 | 0.2189 | −0.0202 | −0.0070 | 1.24 (0.14) | 27%, 80.5% |
| EuroCup | 523 | 0.2103 | 0.2448 | 0.2189 | −0.0346 | −0.0086 | 1.28 (0.16) | 29%, 79.7% |
| Liga ACB | 908 | 0.1994 | 0.2395 | 0.2144 | −0.0401 | −0.0150 | 1.33 (0.12) | 37%, 82.5% |
| B.League | 2,212 | 0.2019 | 0.2496 | 0.2149 | −0.0477 | −0.0130 | 1.08 (0.06) | 41%, 81.4% |
| KBL | 807 | 0.2302 | 0.2478 | 0.2324 | −0.0176 | −0.0022 | 1.07 (0.15) | 12%, 77.1% |
| Greek (caution) | 416 | 0.1619 | 0.2401 | 0.2035 | −0.0782 | −0.0416 | 1.29 (0.15) | 53%, 87.8% |
| Austria (data defect) | 396 | 0.1228 | 0.1851 | 0.1599 | — | — | — | — |

The normal shape also fits equally well in every league (§5.1). One procedure is therefore justified for basketball.

### 2.3 The numbers must stay league-specific

| League | Mean total | Total SD | Home margin | Margin SD | Home win | Margin SD ÷ mean total |
|---|---:|---:|---:|---:|---:|---:|
| NBA | 229.1 | 20.0 | +1.83 | 16.0 | 0.547 | 0.070 |
| WNBA | 164.0 | 17.3 | +1.70 | 14.1 | 0.535 | 0.086 |
| NBL | 183.1 | 19.3 | +1.56 | 16.3 | 0.547 | 0.089 |
| EuroLeague | 168.1 | 17.9 | **+3.50** | 12.5 | **0.635** | 0.074 |
| Liga ACB | 171.6 | 18.2 | **+3.80** | 13.5 | 0.605 | 0.079 |
| B.League | 159.3 | 17.7 | +0.63 | 15.1 | 0.521 | 0.095 |
| KBL | 159.1 | 18.0 | +1.25 | 13.5 | 0.549 | 0.085 |

- **Home edge** ranges from +0.6 (B.League) to +3.8 (ACB), a factor of six.
- **Margin width relative to scoring** ranges from 0.070 (NBA) to 0.095 (B.League), so there is no universal ratio to rescale by.
- Scaling NBA numbers to 40 minutes would put the EuroLeague's home edge at under half its true size (1.5 against 3.5) and its margin SD 1–2 points too wide.

This confirms the existing rule: one method, league-specific numbers.

### 2.4 The real gap: no admitted league numbers

- **LEAGUE_PROFILES (LP-2026.10.16-v4)** admits **no** profile for any competition. Every former store-derived value is RETIRED_SOURCE, and new cards must research the population online each time.
- **TB-1-MD** has validated constants only for the NBA, WNBA and NBL. EuroLeague, ACB, FIBA, LKL and the rest are `UNVALIDATED` or `NOT_COVERED` (PROBABILITY_TOOLKIT §4.3; RULES_BASKETBALL §0.2).
- **Result:**
  - each external chat re-derives league anchors from scratch, under a reading budget and with no code;
  - same-row baseline coverage was **8 of 50** primary rows in the latest cohort (2026-10-21 retrospective);
  - card margin widths were too narrow: z RMS 1.46 on 6 rows, against a z SD of 0.98–1.08 for the fitted models' margins (§5.1).

### 2.5 Recommended design: one procedure plus a competition parameter sheet

1. **Keep the single basketball sport file.** It is already neutral.
2. **Add a basketball competition parameter sheet** (Markdown, one row per competition and season). Each row holds:
   - rule set (FIBA-40 or NBA-48), quarter length and overtime length;
   - mean total, home edge, margin and total residual SD, and overtime rate with points added;
   - early-season shift and TB-1 k;
   - source, n, date range and status.

   Prompt 7 builds the rows from verified results, and prompt 8 admits them. Prompt 1 reads its competition's row instead of re-deriving it.
3. **Fallback ladder** for a competition without an admitted row:
   1. the league's own previous completed season, verified online;
   2. a rule-set family prior (FIBA-40 club or NBA-48), shrunk toward the league's partial data and printed as `FAMILY_PRIOR`;
   3. widen the widths and label the row `NOT_COVERED`.
4. **Tournaments** (FIBA World Cup, EuroBasket, Olympics, AmeriCup) have short, sparse national-team histories, and their development model failed. Keep them qualitative or widely priced until a national-team rating across FIBA windows is built. The literature has single-league hierarchical models but no tested cross-league basketball pooling (Sources).
5. **Order of work:** competitions you actually request first. Plausibly NBL, NBA, EuroLeague and ACB, then B.League, KBL, EuroCup and WNBA (2027).

**Is it too much?** Not for basketball. The prompt cost is zero: the sport file stays as it is. The cost is data: one verified parameter row per competition and season, refreshed each season. The same pattern (one sport file plus competition rows) carries to the other sports.

## 3. Is the ML/RL framework adequate?

### 3.1 Design against good practice

| Element | Framework | Practice / literature | Verdict |
|---|---|---|---|
| One joint score distribution; every contract derived from it | §8.0, CYCLE-v1 score grids | Normal margin models are standard: Stern (1991), NFL σ ≈ 13.86 | Adequate |
| Proper scores (Brier, log loss, CRPS); calibration judged separately | §9.4 | Walsh & Joshi (2024): selecting NBA models by calibration beat selecting by accuracy in their betting test | Adequate |
| Strong comparators: league-only baseline and TB-1 | §8.0, §9.5 | The models above beat TB-1 by only 0.001–0.015, so TB-1 is the right bar | Adequate |
| Chronological development, untouched test, preregistration | §9.2, HYPOTHESIS_REGISTER | Standard | Adequate |
| Features and data quality before model complexity | §8.6 defers deep models | Bunker & Susnjak (2022): feature quality matters more than many instances or complex models | Adequate |
| Lineup and injury effects | Prospective capture only (§7.3–7.4); hand scenarios meanwhile | Historical pregame lineups do not exist in the archive | Adequate, but the main reason a hand card can still beat a model |
| RL | No forecasting role; staking excluded (§10) | Outcomes do not depend on the forecaster's action | Correct |
| Online expert weighting (Hedge, fast and slow decay) | CYCLE-v1 | Online learning, not RL; settings are untuned starting values | Acceptable as experimental |

### 3.2 Gaps that stop it working

| # | Gap | Evidence | Consequence |
|---|---|---|---|
| G1 | **No pregame step exists.** MLSCOPE-v1 removed ML from prompts 1–5, and prompts 6 and 8 run after games or in the workshop | CURRENT_RELEASES: MLB-CYCLE-3 and NHL-CYCLE-3, `prospective_events` 0. No `SHADOW_LEDGER.csv`. The full-league freezer `ml/shadow/lane.py` exists but has never run | The 8-week clock has not started for any model |
| G2 | **No admitted basketball data.** The learning store holds 1,686 MLB/NHL finals and 21 card events | No basketball release. Every `BKB-*-r1` model is DATA_HOLD or DEVELOPMENT_ONLY with unverified source admission; NBL r1 failed development | A basketball lane cannot start until verified history is ingested |
| G3 | **Code churn resets the clock.** A release freezes the `ml/` source digest | 24 commits touched `ml/` between 14 and 21 October. NHL and MLB are already on version 3 with no prospective events | A lane must run from a pinned release that workshop edits cannot touch |
| G4 | **Test length.** The floor is 8 weeks and 50 events, with δ = 0.01 | §4 below: realistic lengths are 8 to 400+ weeks depending on league and comparator | Plans and expectations need per-league sizing; card-only tests are not feasible |
| G5 | **Calibration untested on basketball.** `ml/calibration.py` (Platt, isotonic, hierarchical Platt, coherent grid reweighting) is CALIBRATION_STUDY_NOT_DEPLOYED | The basketball models are **under-confident**: slope above 1 in 10 of 11 leagues (NBA 1.37 ± 0.06). The hand cards are **over-confident** (slope 0.82, 2026-10-16) | Fix the slope in development *before* a lane starts. Changing it later restarts the lane |

### 3.3 RL

RL stays excluded, and nothing found here argues otherwise:
- Forecasts do not change outcomes.
- Learning stake size needs thousands of bets (framework §10.2).
- Staking advice is outside CURRENT_RULES §5.

The Hedge weighting in CYCLE-v1 is online learning and should keep that name.

## 4. How long the 8-week test really takes (basketball)

Weeks needed for 80% power at a two-sided 5% level, by the register's formula. **Full league** prices every fixture (ML framework §9.3). **Card only** assumes about 3 carded games a week in one league.

| League | Games per week | Weeks in a season | Full league, observed effect v league baseline | Full league, observed effect v TB-1 | Full league, δ = 0.01 v TB-1 | Card only, δ = 0.01 v TB-1 |
|---|---:|---:|---:|---:|---:|---:|
| NBA | 49 | ~25 | **8** | **11** | 8 | 67 |
| B.League | 29 | ~26 | 8 | 16 | 27 | 229 |
| Liga ACB | 9 | ~33 | 10 | 22 | 48 | 140 |
| WNBA | 15 | ~17 | 11 | ~2,900 (not feasible) | 49 | 196 |
| EuroCup | 9 | ~19 | 15 | 72 | 53 | 134 |
| EuroLeague | 12 | ~27 | 19 | 55 | 27 | 90 |
| NBL | 7 | ~21 | **34** | **~436 (not feasible)** | 42 | 77 |
| KBL | 11 | ~24 | 34 | ~475 (not feasible) | 23 | 74 |

How to read this:
- **NBA:** a full-league lane can answer within one season, even against TB-1.
- **NBL:** beating the league baseline takes about a season and a half. Showing the model beats a hand TB-1 is out of reach, because the two are nearly the same (−0.003). For NBL cards, a fitted model would add **coherence and correct widths, not accuracy**.
- **Card-only:** "is the model better than my cards?" cannot be settled at card volume in any league. The framework already says so (§9.5, `INFEASIBLE_AT_THIS_EFFECT`). Promotion therefore has to rest on the full-league result plus an explicit owner decision.
- **Weeks** here are in-season weeks. A test longer than one season pauses over the off-season.

## 5. Simulations

### 5.1 Does the normal distribution fit basketball?

Share of games beyond 1, 2 and 2.5 model SDs (a normal distribution gives 31.7%, 4.55% and 1.24%):

| League | Margin \|z\|>1 / >2 / >2.5 | Margin z SD | Total \|z\|>1 / >2 / >2.5 | Total z SD |
|---|---|---:|---|---:|
| NBA | 31.3% / 5.4% / 2.0% | 1.03 | 30.3% / 3.9% / 1.1% | 0.98 |
| NBL | 30.7% / 5.8% / 1.8% | 1.02 | 28.4% / 3.8% / 1.3% | 0.96 |
| EuroLeague | 28.8% / 5.6% / 2.2% | 1.00 | 27.9% / 4.1% / 1.5% | 0.97 |
| Liga ACB | 29.2% / 4.8% / 1.2% | 0.98 | 27.3% / 4.2% / 1.2% | 0.98 |
| B.League | 31.4% / 5.0% / 1.1% | 1.01 | 31.6% / 4.4% / 1.0% | 1.00 |
| WNBA | 30.7% / 6.5% / 2.1% | 1.05 | 33.6% / 3.8% / 1.3% | 1.00 |
| KBL | 28.6% / 5.9% / 1.1% | 1.00 | 29.6% / 3.8% / 1.0% | 0.96 |

- **Totals are close to normal** in every league.
- **Margins** have slightly heavier tails: games beyond 2 SD happen 4.8–6.5% of the time instead of 4.6%, and the excess kurtosis is about 0.1–0.8.
- **Where this matters:** large spreads more than about 2 SD from the centre, where the normal slightly underprices big upsets and big blowouts. A Student-t or an empirical tail fixes that analytically. It is not a reason to simulate.

### 5.2 What simulation would cost

The standard error of a simulated probability is √(p(1 − p) ÷ N). At p = 0.5:

| Simulated games (N) | SE | 95% band |
|---:|---:|---:|
| 1,000 | 0.016 | ±0.031 |
| 10,000 | 0.005 | ±0.010 |
| 100,000 | 0.0016 | ±0.003 |

The differences the framework tries to measure are about 0.01 Brier, which means probability shifts of 0.02–0.03. A 1,000-run simulation is as noisy as the effect itself. Exact calculation (a normal table by hand, or a discretised score grid in code, which `ml/core/distributions.py` already uses) has **zero** simulation error. It also gives exact push and overtime mass.

### 5.3 Where simulation helps, and where it must not be used

| Use | Verdict |
|---|---|
| Basketball winner, spread or total in prompt 1 | **No.** Use the normal table (PROBABILITY_TOOLKIT §1) with the explicit overtime branch |
| "Run 10,000 simulations" in an external no-code chat | **Never.** The chat cannot run them, so the numbers would be invented (a hallucination risk, against NOCODE-v1) |
| Joint loss of Rank 1 and Rank 2 (spread plus total) | Useful, but a bivariate normal is analytic. In the chat use the Fréchet bounds the core already allows; in code use the grid |
| Player props linked to team score | Monte Carlo in code is reasonable (minutes × usage × rate with shared game pace). Not in the chat |
| Tennis, cricket innings, baseball innings, live states | Monte Carlo or exact recursion in code, with a fixed seed and N ≥ 100,000 recorded |

### 5.4 Width matters more than the method

The fitted models' widths are right (z SD 0.96–1.05). The cards' margin widths were too narrow (z RMS 1.46, retrospective 2026-10-21; RET-12). Setting the parameter sheet's residual SD as the **minimum** margin and total width on a card would fix the error that actually showed up. A simulation would not.

## 6. Recommendations, in order

| # | What | Where | Why |
|---|---|---|---|
| 1 | Build the basketball competition parameter sheet (§2.5) for NBL, NBA, EuroLeague and ACB first, from verified prior-season results | prompt 7 builds it, prompt 8 admits it; prompt 1 reads it | Makes one basketball file truly league-neutral and lets every card print BASELINE_P (now 8/50) |
| 2 | Use the sheet's residual SD as the minimum card width, with written exceptions | prompt 8 (toolkit / sport file) | The cards' margins ran too narrow |
| 3 | Ingest verified history for those leagues into the learning store and re-run development | prompts 7 and 8 | No basketball lane is possible without admitted data (G2) |
| 4 | Fit and freeze the calibration (slope above 1) in development before any lane | prompt 8 | Changing it later restarts the clock (G5) |
| 5 | Start a **full-league pregame shadow** from a **pinned release**, committed before each first tip: NBA first (answerable within a season), then NBL and EuroLeague | prompt 8 lane (new pregame step, repository side) | Starts the 8-week clock (G1, G3). Card pairing is reported but not used to promote |
| 6 | Keep prompts 1–5 no-code, and add an explicit "no simulations in chat" line | prompt 8 (core) | §5 |
| 7 | RL: no change | — | §3.3 |

## 7. Limits

- The model numbers come from archive data whose source admission is unverified. They are development evidence, not skill.
- The models have no lineup information, so they understate what availability research adds.
- Power figures assume week means behave independently. Team and serial dependence would lengthen them.
- The literature search was a short targeted check, not a systematic review.

## Sources

**Repository**

Paths are in §1; per-league results are in [BKB_CROSS_LEAGUE.csv](BKB_CROSS_LEAGUE.csv).

**External**
- Walsh, C. and Joshi, A. (2024). "Machine learning for sports betting: Should model selection be based on accuracy or calibration?" *Machine Learning with Applications* 16. [University of Bath research portal](https://researchportal.bath.ac.uk/en/publications/machine-learning-for-sports-betting-should-model-selection-be-bas/)
- Bunker, R. and Susnjak, T. (2022). "The Application of Machine Learning Techniques for Predicting Match Results in Team Sport: A Review." *JAIR* 73, 1285–1322. [JAIR](https://jair.org/index.php/jair/article/view/13509)
- Stern, H. (1991). Normal model of the NFL margin about the point spread (σ ≈ 13.86), as reproduced in [Pro-Football-Reference's win-probability notes](https://www.pro-football-reference.com/about/win_prob.htm); limitations of the continuous normal for discrete scores in [arXiv 2212.08116](https://arxiv.org/pdf/2212.08116).
- Lopez, M., Matthews, G. and Baumer, B. "How often does the best team win?" (Bayesian state-space comparison of the NFL, NBA, NHL and MLB). [arXiv 1701.05976](https://arxiv.org/abs/1701.05976v2)
- Single-league hierarchical basketball model (NBA 2008/09): [SCITEPRESS 2023](https://www.scitepress.org/Papers/2023/121591/121591.pdf)
- A broader review of ML in sports betting: [arXiv 2410.21484](https://arxiv.org/pdf/2410.21484)
