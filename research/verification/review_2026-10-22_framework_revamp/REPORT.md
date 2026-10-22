# Framework revamp review: prediction, ML/RL, simulation and research sources, 22 October 2026

**Status: REVIEW AND PROPOSAL ONLY.** Owner request, 22 October 2026: rethink the framework from first principles; research how each part of the prediction can be improved, how to use ML/RL and simulation better, and what to research and where on the internet, across all sports and competitions. Nothing in this folder changes a rule, prompt, model, release, ID, grade or record. The recommendations (REV-01 to REV-22) take effect only through owner decisions (§13) and prompt-8 changes. Some of them conflict with standing owner rules (MARKET_BLIND; the card-first design of MLSCOPE-v2). Those are put to the owner as decisions with the evidence; none is assumed.

Read at `main` e67b545d0 (working tree clean and equal to `origin/main`), clock 2026-10-22T12:02+11:00, mode `LOCAL_WORKING_TREE`.

**Evidence classes.**
- Card numbers are outcome-exposed descriptive history (`RESEARCH_ONLY_NOT_CERTIFIED`). Rows within a card are dependent.
- Model numbers are `HISTORICAL_DEVELOPMENT` evidence from archive data whose source admission is unverified.
- External claims carry links. Where only an abstract or a citing source could be checked, the Sources section says so.

**"Professions".** Read as professional competitions (leagues, tours and tournaments), covered in §9. §10 also covers how professional forecasters and bookmakers work, in case that was the meaning.

## Summary

### What the evidence says

1. **The cards' probabilities carry information only far from 50%.** On the 862 graded rows with a stated p (220 cards; [CARD_P_DIAGNOSTICS.csv](CARD_P_DIAGNOSTICS.csv)):
   - **Rows stated at 0.40–0.65** (525 rows, 183 cards) won 52.6% against 52.5% stated. Inside that range the calibration slope is **0.15 (SE 0.31)**: a row stated at 0.62 won no more often than a row stated at 0.45.
   - **Rows stated at 0.65 or more** (256 rows, 101 cards) are well calibrated: slope 0.89, 78.1% won against 78.6% stated. These are mostly big favourites and lines far from the centre, which a simple baseline also prices well.

   Supplied spreads and totals sit near 50%. So far the research has not shown that it can pick the winning side of those lines.
2. **The overconfidence is concentrated.** Rows stated at 0.60–0.65 won 51.6% (n = 93); rows stated at 0.80–0.85 won 75.6% (n = 41).
3. **Skill against a strong reference has hardly been measured, and where it was, the card lost.** A same-row league baseline exists for 4 of the first 600 cards and 8 of 50 rows in the latest cohort. Card minus baseline Brier was +0.0222 (P-585–P-589) and +0.0244 (P-612–P-622).
4. **The betting market is the strongest public forecaster, and the framework's best model loses to it.** EPL Dixon–Coles scored 0.2901 against 0.2795 for the de-vigged Pinnacle close (difference +0.0129, week-block interval 0.0079 to 0.0180), in the firewalled decision lab. The literature agrees: in Štrumbelj & Vračar (2012), bookmaker odds were the best probabilistic forecasts.
5. **Fitted models are good at exactly what the cards get wrong.**
   - In 11 basketball leagues the fitted joint model beat the league baseline by 0.010–0.048 Brier and the hand team baseline TB-1 by 0.001–0.015.
   - Its widths are right (z SD 0.96–1.05), while the cards' margin widths were too narrow (z RMS 1.46).
   - But only NHL and MLB have releases, with 0 prospective events, so no model can help a card yet.
6. **Process is crowding out prediction.**
   - A basketball card's reading gate names about 500 KB of rules (about 125,000 tokens).
   - The method went from v10 on 11 October to v23 on 22 October.
   - Active documents contradict each other (§2.2, RC7).
   - None of the 11 primary cards in the last cohort has a verified pre-start issue, and all four new cards in today's mini were finished after the scheduled start. Requests often arrive 0–15 minutes before the start.

### The redesign in one paragraph

Stop asking the analyst to invent each probability from scratch.
- **Reference model.** Every requested competition gets a fitted, calibrated reference model (team ratings → one joint score distribution → every contract), run before the analyst writes.
- **The analyst's job** becomes finding information the reference does not have: confirmed line-ups, injuries, starting pitchers, goalies and quarterbacks, weather, schedule.
- **Adjustment ledger.** That information is priced as logged, bounded adjustments taken from measured effect tables. Each adjustment is scored on its own at settlement, which finally answers the question the framework cannot answer today: does the research add accuracy?
- **Picks** are ranked by calibrated probability. Easy lines are labelled as easy, a separate list shows where the research disagrees with the reference, and "no strong pick" is an allowed answer.
- **Evaluation** uses proper scores against the league baseline, the reference model and, if the owner allows, the market, at full-league volume.
- **Simulation** is used only where the path of the score matters, in code, with seed and N printed.
- **Reinforcement learning** has no forecasting role. The existing online weighting (Hedge) stays and is tuned.

### The changes that matter most

| ID | Change | Why | Effort |
|---|---|---|---|
| REV-01 | A reference model for each requested competition, run before the card | The cards lose to baselines, and the models beat them, so the card should start from the better number | Large |
| REV-02 | An adjustment ledger with measured effect tables; each adjustment scored | The only feasible test, at card volume, of whether research adds value | Medium |
| REV-03 | A line-implied benchmark (p = 0.5 at a supplied two-way line) in every settlement | Shows at once whether supplied-line picks beat a coin; needs no price | Small |
| REV-06 | Season releases and full-league pregame shadows, NBA first | Starts the clocks that can actually reach a decision | Medium |
| REV-07 | Ingest verified history for the competitions actually requested | No model without data; the store holds MLB and NHL only | Large |
| REV-05 | Width floors and tail rules from measured residuals | The cards' margin widths ran too narrow | Small |
| REV-09 | New pick format: probabilities for every supplied contract, a most-likely list with line difficulty, an information list, abstain | A hit rate on self-chosen lines measures line choice, not forecasting | Small |
| REV-15 | Earlier requests where possible, a time budget and a "fast card", so forecasts exist before the start | 0 of 11 cards verified pre-start in the last cohort | Small |
| REV-08 | Consolidate the rulebook to a core of about 30 KB plus code checks; freeze statistics for a season | Contradictions, churn and the reading burden | Medium |
| REV-11 | A player-props engine in code (minutes × rates, shared pace) | Props are requested and cannot be priced honestly by hand | Medium |
| REV-12 | Path simulators where needed (baseball innings, cricket balls, tennis points, hockey late game) | The only places simulation beats an exact formula | Medium to large |
| REV-04 | A no-vig closing benchmark after settlement (owner decision D1) | The hardest honest test of skill | Small to medium |

### What not to do

- **No RL agent for forecasting.** Outcomes do not depend on the forecast, and every contract's outcome is observed at settlement, so there is nothing to explore (§6).
- **No optimising the headline hit rate by choosing easier lines.** It has already happened once: the 85% E3 cohort was mechanical.
- **No "10,000 simulations"** where an exact formula exists, and none at all without code.
- **No deep neural networks** on a few thousand games per league. Trees and ridge models are the right tools for small tabular data (Grinsztajn et al. 2022), and features matter more than algorithms (Bunker & Susnjak 2022).
- **No more procedure documents.** Every new rule should replace one, and checks should move into code.

## 1. What was examined

**Repository:**
- README, CURRENT_STATE, METHOD, CURRENT_RULES (§0–§12), SELECTION_RULES, PROBABILITY_TOOLKIT (§1, §4, §5);
- EXECUTION_ENVIRONMENT_PROTOCOL, ML_EXECUTION_PROTOCOL, FORECAST_CYCLE_PROTOCOL;
- [ML_RL_IMPLEMENTATION_FRAMEWORK_2026-10-14](../../../ML_RL_IMPLEMENTATION_FRAMEWORK_2026-10-14.md) (§1, §5, §7) and prompt 8;
- [`ml/config.py`](../../../ml/config.py) and the `ml/` module layout, [CURRENT_RELEASES.csv](../../cycle_releases/CURRENT_RELEASES.csv);
- the [active mini](../../active_minis/20261022F6K3OJNO.md)'s intake and event inventory;
- the [decision-lab results](../../model_shadow/DECISION_LAB/RESULTS.md);
- the [2026-10-16 full-history retrospective](../retrospective_2026-10-16-full/RETROSPECTIVE_REPORT.md) and the [2026-10-21 cohort retrospective](../retrospective_2026-10-21/RETROSPECTIVE_REPORT.md);
- the [21 October league-neutral, ML and simulation review](../review_2026-10-21_league_neutral_ml_sim/REPORT.md) and the [22 October simulation review](../framework_change_2026-10-22-1/SIMULATION_REVIEW.md).

SOURCES.md was searched by heading and by source name, not read in full.

**New analysis** ([CARD_P_DIAGNOSTICS.csv](CARD_P_DIAGNOSTICS.csv)):
- **Input:** the committed [CARD_ROWS.csv](../retrospective_2026-10-21/HISTORY/CARD_ROWS.csv) (SHA-256 `0c40342a…850eda`). Kept rows: numeric p and a WIN or LOSS grade (862 rows, 220 cards).
- **Per group:** rows, cards, mean stated p, realised rate, Brier, in-sample climatology, and Murphy reliability and resolution over ten 0.1-wide bins.
- **Slope rows:** a logistic regression of the outcome on logit(p), with its standard error.
- **Bands:** 0.05 wide; groups under 15 rows are omitted. A single band is one bin, so its reliability and resolution columns are degenerate and should be ignored.
- **Check:** the run reproduces the retrospective's headline (862 rows, Brier 0.2269, climatology 0.2414, slope 0.79, SE 0.11).
- **Script:** ran outside the repository (MD-only rule), so it is described here instead of committed.

**External research.** About 60 targeted searches and page reads on 22 October 2026. Topics:
- market efficiency and odds as forecasts;
- rating and score models for each sport;
- calibration, scoring rules and forecast aggregation;
- LLM forecasting;
- ML for tabular data;
- simulation methods;
- the current state of public data sources and team-news timing.

This was a targeted check, not a systematic review. Sources are listed at the end.

## 2. Diagnosis: why accuracy is not improving

### 2.1 The record

| Measure | Value | Source |
|---|---|---|
| Rank 1 / Rank 2 / Ranks 3–4, all history | 342–201 (63.0%) / 293–219 (57.2%) / 557–442 (55.8%) | 2026-10-21 retrospective §5 |
| Stated-p rows: Brier, in-sample climatology, slope | 0.2269, 0.2414, 0.79 (SE 0.11) | Same; reproduced here |
| Murphy resolution / uncertainty | 0.016 / 0.241 | This review |
| Rows 0.40–0.65: slope; realised v stated | 0.15 (SE 0.31); 52.6% v 52.5% | This review |
| Rows ≥ 0.65: slope; realised v stated | 0.89 (SE 0.30); 78.1% v 78.6% | This review |
| Chronological recalibration study | A Platt refit would move the test Brier only from 0.2072 to 0.2063; IDENTITY kept | 2026-10-16 full history §3.4 |
| Same-row league baseline coverage | 4 of 600 cards; 8 of 50 rows in P-612–P-622 | Retrospectives |
| Card − baseline Brier where measured | +0.0222 (P-585–P-589, 4 rows); −0.0007 (P-580–P-583); +0.0244 (P-612–P-622, 8 rows) | CURRENT_STATE scoreboard |
| Latest primary cohort | 11W/10L/1P, Brier 0.2041 (21 rows); Rank 1 5–0 at p ≥ 0.60, 1–5 below | 2026-10-21 retrospective |
| The 85% "RANK1_UNSTABLE" cohort | Every top-two pair covered itself; skill −0.03 against climatology | [2026-10-11 retrospective](../retrospective_2026-10-11/RETROSPECTIVE_REPORT.md) |
| EPL model v market (three-way half Brier) | Model 0.2901; TB-1 0.3001; league baseline 0.3236; no-vig close 0.2795 | Decision lab |
| Basketball models (11 leagues, 12,750 games) | Beat the league baseline by 0.010–0.048 and TB-1 by 0.001–0.015; calibration slope above 1 in 10 of 11 | 2026-10-21 review |
| Width | Card margins z RMS 1.46 (n = 6), totals 0.48 (n = 10); fitted models z SD 0.96–1.05 | Same |
| Model lanes | Releases NHL-CYCLE-4 and MLB-CYCLE-4 only; 0 prospective events | CURRENT_RELEASES.csv |
| Pre-start issue | 0 of 11 primary cards verified pre-start (2026-10-21); all 4 new cards in today's mini finished after the scheduled start | Retrospective; active mini |

**Band detail** (stated p against realised rate):

| Stated p | Rows | Mean stated | Realised |
|---|---:|---:|---:|
| 0.35–0.40 | 57 | 0.373 | 0.439 |
| 0.40–0.45 | 94 | 0.424 | 0.489 |
| 0.45–0.50 | 98 | 0.467 | 0.551 |
| 0.50–0.55 | 97 | 0.527 | 0.515 |
| 0.55–0.60 | 143 | 0.569 | 0.545 |
| 0.60–0.65 | 93 | 0.621 | 0.516 |
| 0.65–0.70 | 54 | 0.670 | 0.704 |
| 0.70–0.75 | 44 | 0.722 | 0.727 |
| 0.75–0.80 | 36 | 0.767 | 0.722 |
| 0.80–0.85 | 41 | 0.827 | 0.756 |
| 0.85–0.90 | 75 | 0.883 | 0.907 |

From 0.40 to 0.65 the realised rate stays flat at about 49–55%, whatever the card said. Above 0.65 it tracks the stated value.

**By sport.** Resolution measures how much the stated p separates winners from losers:
- highest in cricket (0.047) and basketball (0.044);
- lower in soccer (0.022);
- lowest in baseball (0.009) and rugby league (0.009).

Tennis (reliability 0.048) and American football (reliability 0.124, 28 rows) were badly calibrated.

**Limits:**
- Rows are dependent: about four per card, often complementary.
- Supplied and analyst-derived lines were not flagged before 12 October, so the band result cannot be split by line source.
- The pattern is consistent with near-efficient supplied lines and with research that does not move them. It does not prove the research is worthless.

### 2.2 Root causes

**RC1 — The target rewards easy lines.** "Four picks from most to least likely" ranks by p, and p is highest on big favourites and on lines far from the centre. A Rank 1 that is the favourite's moneyline or a wide alternative line wins often, whatever research was done. The framework already knows this (line-difficulty labels, mechanical-protection flags), but the headline still counts slot wins.

**RC2 — The analyst is the probability engine.**
- **Every card re-derives everything by hand:** anchors, widths and adjustments.
- **The analyst is a language model, and LLM probabilities lean high.** Leng et al. (2024) trace part of this to the reward models used in RLHF. Schoenegger et al. (2024) found an acquiescence bias in LLM forecasts.
- **The cards show the same pattern:** overconfidence at 0.60–0.65 and 0.80–0.85, and margins too narrow.
- **After-the-fact calibration did not work:** a calibrator fitted on earlier cards did not transfer to later ones (§2.1), because the error moves with line choice. The fix has to come earlier in the process.

**RC3 — Most cards have no strong prior.**
- TB-1-MD constants are validated for 13 leagues (nine plus four European soccer leagues), LEAGUE_PROFILES admits none, and no fitted release exists outside MLB and NHL.
- The latest cohort covered about 20 competitions in two weeks, most with one card each: NBA preseason, NBL, J1, Chinese Super League, UAE Pro League, Indian Super League, Algeria Ligue 1, LaLiga, Liiga, NHL, B.League, PBA, KBO, LBA, rugby union, Test, ODI and women's T20I cricket, and Czech women's football.

**RC4 — The supplied line is information, and the framework throws it away.**
- **A two-way line is the market's median.** A spread or total offered at standard prices on both sides is roughly 50% each side before the bookmaker's margin.
- **In major leagues that median is hard to beat** (Štrumbelj & Vračar 2012; the decision lab above).
- **A card that says 0.62 on such a row claims a 12-point edge over the market.** The cards' 0.60–0.65 band won 51.6%.
- **MARKET_BLIND has a real benefit and a real cost.** It keeps the research independent, but it also means a card never knows when it disagrees with the market, and no settlement measures whether it should have.

*Example (today's request; no research done).* Mavericks +9.5 at Rockets, total 230.5:
- **What the line implies.** Suppose the margin around the line has an SD of about 12 points (Winston's back-of-envelope figure for the NBA; the repository's model residual is 16.0, and residuals around a market line are smaller). Then the line implies Rockets win ≈ Φ(9.5/12) = 0.79 (0.72 with an SD of 16), Rockets −9.5 ≈ 0.50 and Over 230.5 ≈ 0.50.
- **So the "most likely" list is predictable before any research:** the Rockets moneyline first, then wide alternative lines. Its hit rate measures line choice.
- **What would show skill** is a well-sourced reason to move the −9.5 or 230.5 probability away from 0.50, and a record of whether those moves were right.

**RC5 — The models are built but disconnected.**
- No basketball, soccer, cricket, tennis, AFL, rugby or NFL release exists.
- The learning store holds 1,686 MLB/NHL finals plus 21 card events.
- Until 22 October any `ml/` edit retired a release, so NHL and MLB reached version 4 with 0 prospective events.
- The card-first rule (MLSCOPE-v2) then guarantees that a card cannot use a model, even where one exists.

**RC6 — Evaluation cannot reach a decision at card volume.** About three cards a week per league cannot settle "model versus card" in any league (2026-10-21 review §4). Rule changes are therefore made on small, outcome-exposed samples, and the statistical rules change faster than the evidence accumulates.

**RC7 — Governance overload and rule drift.**
- **Scale:** 56 root documents; about 500 KB in the reading gate for one basketball card (21 files, before SOURCES.md's 203 KB); 117 commits since 1 October; method v10 on 11 October to v23 on 22 October.
- **Active documents now contradict each other:**
  - CURRENT_RULES §0 says only prompts 6 and 8 use the workshop and that "Prompts 1–5 never run code" (MLSCOPE-v1). §1 of the same file says prompt 1 runs `python -m ml pregame run` (MLSCOPE-v2).
  - CURRENT_RULES §7 says "No code is run (MLSCOPE-v1)". MLSCOPE-v2 says "code may do the arithmetic".
  - CURRENT_RULES §8 says prompt 4 adds the byte count and SHA-256 at intake (ENV-v1). ENV-v2 §4 says prompt 3 records them.
  - METHOD.md still prints "ACTIVE: MDS-2026.10.16-v20.0" and says primary cards use PRIMARY_HEDGE_MIX_V3. CURRENT_STATE says v23.0 and ANALYST_PRIMARY_V1.
  - SELECTION_RULES §10 and CURRENT_STATE "Models" still say that prompts 1–5 use no model runtime or code.
- **Effect:** an agent that reads the whole gate receives conflicting instructions, and the reading itself uses up the attention the forecast needs.

**RC8 — Research effort is spread evenly instead of by value.**
- **EXH-v1 treats every field the same:** it asks for corroboration of every required field.
- **But value is concentrated** in a few inputs per sport: key-player availability; starting pitchers, goalies and quarterbacks; confirmed line-ups; and weather for outdoor totals. Those are published late (§8).
- **The losses came from late facts.** The latest cohort's Rank-1 loss reviews found the decisive facts were not knowable at issue: a Sunday starting five, Milano's active five, an overtime branch.
- **More sources do not fix that. Timing does.**

**RC9 — Latency.** The research takes longer than the time between request and start:
- **The requests come late:**
  - G0002 was requested 12 minutes before kick-off;
  - G0003 10 minutes before the tip;
  - G0005 5 minutes after the start;
  - today's Mavericks–Rockets request about 13 minutes before the tip.
- **A full card then finishes after the start.** It cannot be evaluated as a pre-game forecast, and the picks reach the owner too late to use.
- **Two fixes:** earlier requests where possible, and a card that can be issued in minutes (REV-15).

## 3. The redesign

### 3.1 Principles

1. **One reference model per competition, always run.** Every card starts from the same fitted distribution, so cards are consistent and widths are right.
2. **Information, not opinion.** A departure from the reference needs a named fact, its publication time and a size taken from a measured table.
3. **Probabilities, not slots.** Report a calibrated p for every supplied contract. Slot hit rates are a diagnostic.
4. **Beat a reference, not a coin.** Score against the league baseline, the reference model and, under D1, the market.
5. **Widths from data.** Never narrower than the competition's measured residual SD without a written reason.
6. **Exact where possible.** Simulate only score paths, and only in code.
7. **Freeze the statistics for a season.** Fix bugs at any time; change methods between seasons.
8. **Short rules, enforced by code.**
9. **"No strong pick" is an answer.**
10. **Honest labels** (kept from the current framework).

### 3.2 Architecture

| Layer | What it does | Exists today | Change |
|---|---|---|---|
| L0 Data | Results, scores, periods and venues; player minutes and availability history; schedule; weather archive; pregame snapshots with publication times | Learning store (MLB/NHL plus 21 events); prospective-capture rules | Ingest the requested competitions (REV-07); snapshot line-ups at every freeze |
| L1 Reference model | Team ratings → one joint score grid → every contract, with the league-only BASELINE_P beside it | The `ml/` contextual cycle (NHL and MLB releases); 11 basketball development models | A release per requested competition (REV-01, REV-06) |
| L2 Information adjustments | Availability turned into a rating change by player value × expected minutes; starters; rest, travel, altitude, weather, motivation. Each comes from an effect table and is logged with its known-at time | Hand adjustments in prose; the ADJUSTMENT_DEPENDENT flag | Adjustment ledger and effect tables (REV-02, REV-17) |
| L3 Combination and calibration | Reference plus adjustments (plus a market prior if D1 = c), calibrated, with widths floored | Hedge weighting inside the cycle; calibration code not deployed | Calibrate in development (REV-10); shrink adjustments by a learned factor |
| L4 Selection | A probability table for every supplied contract; most-likely list with line difficulty; information list; winner probability; abstain | P_ORDER_V2 top four, gate 0.62 / 0.04, five shadow selections | New pick format (REV-09) |
| L5 Evaluation | Proper scores against the references; adjustment-ledger value; calibration and coverage; full-league shadows | Shadow ledger, `cycle evaluate`, `card-history` | Dashboard per competition (REV-18); line-implied and market benchmarks (REV-03, REV-04) |
| L6 Learning | Hedge updates at settlement; refits and effect tables between seasons | Hedge in the cycle; the LEARN-v1 pipeline | Season releases (REV-06); Hedge tuning (REV-19) |

### 3.3 What prompt 1 would do

1. Identify the event and the contract definitions (unchanged).
2. Run the reference model in code. Print, for every supplied contract, the reference p, the league BASELINE_P, the centre and the widths.
3. Work through the sport's value-ranked checklist (§8), timed to when each item is published.
4. Turn confirmed facts into adjustments from the effect tables. Print the ledger (fact, source, time, size, basis) and recompute the grid.
5. Print, beside the reference p:
   - the final p for every supplied contract;
   - the winner probability for both sides;
   - the most-likely list with line difficulty;
   - the information list: rows the adjustments moved by at least 0.03;
   - or "no strong pick".
6. Freeze, commit and push before the start (unchanged).

The decision block fits on one page; sources and arithmetic go in an appendix, as now.

### 3.4 Keep

- evidence grades A–X and settlement revisions;
- deep reviews of Rank-1 losses (shorter);
- the shadow ledger, the pregame freeze and commit-before-start;
- local keys and canonical IDs;
- the source register and the verified lanes;
- honest labels;
- the exact score grids and the 22 October structural rules (NFL key numbers, hockey one-goal games, baseball one-run games).

### 3.5 Simplify or retire

- **Two-source corroboration:** keep it for decisive facts only, not for every field.
- **RM-1 and q residue** (already non-operative): move to the archive.
- **The five shadow selections** (RET03 gate, RET04, XCARD6, RANK_DELTA, BASE_ONLY): replace with the information list and the reference comparison, which test the same questions directly.
- **Self-audit checklists ticked by hand:** replace with a card validator in `ml/` (REV-08c).
- **The 500 KB reading gate:** replace with a core of about 30 KB, plus the sport sheet and the competition row.

### 3.6 Migration

| Phase | When | What | Gate to the next phase |
|---|---|---|---|
| 0 | Now to 2 weeks | Fix the contradictions; line-implied benchmark in settlement; width floors; adjustment-ledger template; NBA data ingest and release; fast-card rule | An NBA release frozen and running pregame before first tips |
| 1 | To the end of 2026 | Releases for the competitions requested most (the soccer leagues, NBL, EuroLeague/ACB, B.League; NHL and MLB already exist); a full-league NBA shadow; a props engine for NBA points, rebounds and assists | Lanes accumulating; the ledger on every card |
| 2 | Through each season | Monthly dashboard; effect tables re-estimated only between seasons; a decision per competition on REFERENCE → ANCHOR (D2) | Preregistered floors met per lane |
| 3 | Off-seasons | AFL, NRL and IPL/BBL lanes before March 2027; tennis Elo plus a serve model; a cricket ball-by-ball simulator; a baseball inning simulator | Development tests passed |

## 4. Each part of the prediction and how to improve it

### 4.1 Team strength

| Sport family | Reference rating | Evidence |
|---|---|---|
| Points sports (basketball, AFL, NFL, rugby) | Ratings built on margins (ridge, or Elo/Glicko with a margin term); separate attack and defence for totals; exponential time decay; reversion to the mean between seasons | The joint model beat TB-1 in all 11 basketball leagues (2026-10-21 review). Team strength as a state-space process with mean reversion is the standard (Glickman & Stern 1998, extended across four leagues by Lopez, Matthews & Baumer 2018). AFL ratings gain from ground familiarity and travel terms (Ryall & Bedford 2010) |
| Soccer | Dixon–Coles or bivariate Poisson with time decay; xG-informed attack and defence | Dixon & Coles (1997); the dynamic bivariate Poisson of Koopman & Lit (2015); Bayesian hierarchical models (Baio & Blangiardo 2010). xG predicts future results better than goals do (PLOS ONE 2023; ElHabr 2024) |
| Ice hockey | Poisson goals with a goalie term; xG-based team ratings | MoneyPuck shot-level xG data. The count grids beat the league baseline on winners (0.2401 v 0.2483) |
| Baseball | Run scoring and prevention with the starting pitcher and bullpen; park and weather | The run grid beat the baseline on winners (0.2445 v 0.2499) but not on totals. The starting pitcher is the largest single input |
| Tennis | Surface-blended Elo (50% overall, 50% surface) plus a serve/return point model | Tennis Abstract's tested blend; Barnett & Clarke (2005) on combining serve and return statistics; Kovalchik (2016) benchmarked 11 published models, including Elo, on 2,395 ATP matches |
| Cricket | Batting and bowling strength by format and venue; player-based XI strength | Ball-outcome models with batter, bowler, overs and wickets (Davis, Perera & Swartz 2015) |

**What not to expect.** In the 2017 Soccer Prediction Challenge the top entries differed very little (RPS 0.2054–0.2087), whatever method they used (Berrar, Lopes & Dubitzky 2019 and the same special issue). Better data beats a cleverer algorithm.

**How to improve it:**
- fit ratings per competition from verified history (REV-07);
- set the time decay and the between-season reversion on walk-forward history;
- give promoted, relegated and expansion teams a prior from their previous league;
- widen early-season forecasts by propagating rating uncertainty (§7.1).

### 4.2 Player availability and line-ups: where research can add value

The reference model does not know who plays. That is the analyst's real contribution, and it can be measured.

- **Convert availability into strength with player value × minutes:**
  - **Basketball:** a public player-impact metric times the minutes the player would have played, redistributed to the replacements.
  - **Soccer:** player ratings or plus-minus. Team plus player ratings forecast better than either alone (Arntzen & Hvattum 2021).
  - **Hockey:** the starting goalie's goals saved above expected, from MoneyPuck shot data.
  - **Baseball:** the starting pitcher's projected run prevention and the bullpen's recent workload.
  - **NFL:** quarterback value.
  - **AFL and rugby:** the selected team against the club's best side (games, positions, key roles such as ruck, halves and hooker).
- **Price uncertain status as a mixture.** "Questionable" or "game-time decision" becomes a probability of playing, estimated from how often players with that status played. That needs prospective capture; it should not be a guess.
- **Time research to publication** (verified 22 October 2026):

  | Competition | When team news is published |
  |---|---|
  | NBA | Statuses due 5 p.m. local the day before (1 p.m. on the second night of a back-to-back); game-day report between 11 a.m. and 1 p.m. (official NBA injury-report page) |
  | Premier League | XIs submitted at least 75 minutes before kick-off and published from then (since 2024-25) |
  | NRL | Team lists about 4 p.m. AEST Tuesday; two players cut 24 hours out; final 19 named 90 minutes before kick-off |
  | AFL | Team lists at fixed times (Wednesday 6:20 p.m. for Thursday games); final teams about 50–60 minutes before the bounce; late changes only with AFL approval |
  | NFL | Inactives 90 minutes before kick-off |
  | MLB | Probable pitchers days ahead; line-ups a few hours before |
  | Cricket | XIs and toss at the toss, usually about 30 minutes before the start (not separately verified for this review) |
- **Measure it.** Each availability adjustment enters the ledger and is scored: did the rows it moved score better than the reference on the same rows?

### 4.3 Context

| Factor | What the evidence says | Use |
|---|---|---|
| Home advantage | Differs sixfold between basketball leagues (B.League +0.6, ACB +3.8 points). In soccer it fell or vanished in empty stadiums, and in some leagues it stayed weak after fans returned | Estimate per competition and season; refresh each season |
| Rest and back-to-backs | One old NBA estimate: about 2.3 points for a back-to-back against three or more rest days (1999-2000 data). Recent work finds lower shooting efficiency and win rates on back-to-backs | Re-estimate on current seasons before use |
| Travel, time zones, altitude | Ground familiarity and travel matter in the AFL (Ryall & Bedford 2010) | Estimate per competition |
| Weather (outdoor) | Wind and rain move totals in the NFL, MLB, AFL, rugby and cricket; rain also brings DLS in cricket | Venue-local forecast for the match window (existing rule) |
| Officials | NBA crews are posted about 9 a.m. ET; MLB umpires appear in the game feed | Low priority; use only with a measured effect |
| Motivation and rotation | Dead rubbers, cup rotation, resting stars | A scenario only when team news supports it |
| Recent form | The framework's own study found no bounce-back effect in six leagues, and the last game is the worst single predictor | Through ratings with time decay; never a separate lean |
| Early season | Ratings are least certain | Wider widths from rating uncertainty |

Every size goes in an effect table with its n, period and interval (REV-17). Sizes made up by hand stay out.

### 4.4 Score distribution and width

- **Basketball, AFL and NFL:** totals and margins are close to normal, with slightly heavy margin tails (4.8–6.5% of games beyond 2 SD, against 4.55%). Use a Student-t or empirical tail beyond 2 SD for big spreads.
- **NRL:** needs wider widths (z SD 1.07–1.10) and a lower total centre. In development the Over was priced 5 points above its realised rate.
- **NFL key numbers:** margins of exactly 3 occur in about 14% of games and exactly 7 in about 8%, against 5.7% and 5.2% under a normal. Use an empirical margin table near those numbers.
- **Hockey and baseball:** ties are always broken, so one-goal and one-run games are far more common than a symmetric distribution says (NHL 39.9% v 28.7%; MLB 28.1% v 17.4%). Price the extras explicitly, and in hockey add the empty net.
- **Cricket:** innings tails are about three times heavier than normal beyond 2.5 SD (collapses and late-over surges).
- **Width floor (REV-05):** a card's margin and total SD may not fall below the competition's measured residual SD without a written reason. Coverage (z RMS; share outside ±1 and ±2 SD) is reported monthly by family.

### 4.5 Contract pricing

Keep one grid for all contracts. Add:
- **Alternative lines:** allowed, but labelled `ANALYST_DERIVED` with their distance from the centre.
- **Period markets:** from period models, never from a scaled full-game total.
- **Player props:** only from player models (REV-11).
- **Corners:** only with a named provider and a count model (existing rule).

### 4.6 Calibration and combination

- **Fitted models.** The basketball models are under-confident (slope above 1 in 10 of 11 leagues; NBA 1.37).
  - Fit a calibration map in development, on walk-forward data, before a lane starts.
  - Beta calibration includes the identity map and is as easy to fit as Platt scaling (Kull, Silva Filho & Flach 2017).
  - Isotonic calibration needs more data.
- **Analyst adjustments.** Shrink each adjustment by a factor λ estimated from the ledger: start at 1 and re-estimate between seasons. Do not fit a calibrator to hand probabilities alone; it did not transfer across eras.
- **Combining forecasts:**
  - **Average independent forecasts** with a trimmed mean. This is what brought an LLM pipeline close to crowd accuracy (Halawi et al. 2024).
  - **Average rather than show.** Averaging human and LLM forecasts beat letting the LLM see the human forecast (Schoenegger et al. 2024).
  - **Extremise only aggregates.** It helps only for aggregates of independent forecasters (Satopää et al. 2014; Baron et al. 2014). Never extremise a single model.

### 4.7 Picks: what a game request should return

- **A probability table** for every supplied contract: reference p, final p, and (after settlement) the line-implied and market p.
- **The game winner** for both sides, with probability.
- **A most-likely list** (up to four). Each row is labelled SUPPLIED or ANALYST_DERIVED with its distance from the centre in SDs. This list answers "most likely"; it does not claim skill.
- **An information list:** rows where confirmed facts moved p by at least 0.03 from the reference, with those facts. This is the list that tests the research.
- **Abstain:** if no row has a calibrated p of at least 0.65 and there is no information row, say "no strong pick". Below 0.65, stated probabilities have behaved like coin flips (§2.1); the 2026-10-09 retrospective made the same recommendation.
- **No covering pairs as two picks.** If Rank 1 and Rank 2 cover each other, say so and count them as one.

### 4.8 Evaluation

- **Scores.** Brier and log loss for binary rows, the ranked probability score for three-way results, and CRPS for margins and totals. All are proper scoring rules (Gneiting & Raftery 2007).
- **References, on identical rows:**
  - the league baseline;
  - the reference model;
  - a line-implied 0.5 for supplied two-way lines (REV-03);
  - the no-vig close (REV-04, D1).
- **Paired tests.** Differences per event, averaged by week, with week-block bootstrap intervals (as now).
- **The ledger test.** Final p against reference p on the same rows. Every adjusted card adds paired evidence in every sport, so this test grows much faster than any single-competition lane.
- **Calibration and coverage.** Slope and intercept, reliability bins, z RMS and band coverage, every month.
- **Decisions:**
  - Model promotion comes from full-league lanes: the NBA is answerable within a season; the NBL takes about 34 weeks against the league baseline.
  - The value of the analyst's research comes from the ledger.
  - Nothing is decided from card hit rates.

### 4.9 How the research agent works

- **Checklist:** a fixed, value-ranked checklist per sport (§8), not "every field equally".
- **Sources:** two independent sources for decisive facts only; one official source is enough for the rest.
- **Recording:** structured extraction into the card's tables, with publication and retrieval times; arithmetic done in code.
- **No story adjustments:** no "must-win", "revenge" or streak adjustment without a measured effect.
- **Base rates first, then adjustments.** In a large forecasting tournament, training in reference-class thinking improved accuracy (Mellers et al. 2014). A 2025 reanalysis questions how much of the gain came from training and teams, so treat it as plausible, not proven.
- **Two passes (optional):** for important cards, two independent research passes averaged. This doubles the cost.
- **A time budget (REV-15):** if the full research will not finish before the start, issue a fast card (reference plus confirmed availability) first, then add the full card as a dated addendum.

## 5. Machine learning: what to build and how it improves

### 5.1 The model ladder

| Level | Model | Expected gain | Cost | Status |
|---|---|---|---|---|
| M0 | League baseline | Reference only | None | Exists |
| M1 | Team ratings → joint score grid | The largest step: 0.010–0.048 Brier over M0 in basketball development | Data per competition | 11 basketball development models; NHL and MLB releases |
| M2 | M1 plus availability from player values and minutes | The main remaining gain: team plus player ratings beat either alone (Arntzen & Hvattum 2021) | Player data; snapshots for training | Not built |
| M3 | Contextual ridge or gradient boosting on rest, travel, xG form and weather | Modest; needs thousands of games | Moderate | The ridge contextual cycle exists |
| M4 | Simulators (possession, inning, ball, point) | Coherent prices for props and path contracts, not better winners: Štrumbelj & Vračar (2012) found comparable accuracy and more insight | High | Not built |

Default per competition: M1 now, M2 where availability data exists, M3 only after M2, and M4 only for the contracts listed in §7.

### 5.2 By sport

| Sport | Reference (L1) | Availability inputs (L2) | Context (L3) | Distribution and simulation | Calibration notes | Training history |
|---|---|---|---|---|---|---|
| Basketball | Joint-normal ridge, attack and defence, time decay; home edge and widths per league | Impact metric × minutes; confirmed starters; rest status | Back-to-backs, travel, altitude | Normal plus an OT branch; t-tails for big spreads; props by simulation | Under-confident in development: calibrate before lanes | Basketball-Reference, NBA stats, ESPN API, league sites; the SOURCES routes behind the retired 2026-10-14 builds (KBL, B.League, ACB, EuroCup, G League), re-verified into the learning store |
| Baseball | Run model with starter and bullpen; park; platoon | Probable and confirmed starter; line-up; bullpen use in the last three days | Weather (temperature, wind); umpire (low) | Negative binomial grid with extras; inning simulator for run lines and first-five markets | Little resolution on totals | MLB Stats API, Retrosheet, Baseball Savant; KBO and NPB owner routes |
| Ice hockey | Poisson with goalie and xG ratings | Confirmed starting goalie; skater absences | Back-to-backs, travel | Regulation grid plus OT/SO plus an empty-net adjustment | Small edges; hockey and baseball are the most random of the four North American leagues (Lopez et al. 2018) | NHL API; MoneyPuck shot data from 2007-08 |
| Soccer | Dixon–Coles with time decay; xG-informed | XI; key absences and suspensions through player ratings | Rotation, fixture congestion, weather | Exact grid; corners by a count model | Totals show little resolution outside a few leagues | football-data.co.uk (results only, odds stripped), ESPN API; Understat xG for the top leagues |
| AFL / AFLW | Margin ratings with ground familiarity and travel | The selected 22 against the best 22; late changes | Weather; short breaks | Normal; separate AFLW parameters | The Squiggle aggregate as an external benchmark (never an input) | AFL Tables, fitzRoy, Squiggle API |
| Rugby league | Margin ratings | Halves, hooker and fullback availability; the final 19 | Weather; State of Origin period | Normal with wider widths; golden point | The Over was priced 5 points high in development | Rugby League Project, NRL.com |
| Rugby union | Margin ratings; World Rugby rankings as the international prior | Selected XV and bench | Weather; travel | Normal; draws possible | Little stored data | Competition sites; World Rugby rankings |
| American football | Margin ratings with a QB adjustment | Quarterback and other key positions; inactives | Wind, rest | Empirical margin table at 3 and 7 | The cards are weakest here (7–12 at Rank 1) | nflverse (play-by-play, schedules, injuries, depth charts) |
| Cricket | Innings-total model by venue and pitch; team batting and bowling | XI; toss | Dew (weak evidence); rain and DLS | Ball-by-ball simulator for innings and chases, after data capture | The IPL team model showed no skill over a team-free model | Cricsheet ball-by-ball, all formats, men and women |
| Tennis | Surface-blended Elo plus a serve/return point model | Fitness, withdrawals, retirement risk | Fatigue from previous matches; altitude; indoor play | Exact point → game → set → match recursion; form shock by integration | The cards are badly calibrated in tennis: abstain more until a model is live | Tennis Abstract; Sackmann data (licence CC BY-NC-SA; current-season status unverified, and the route returned 404 earlier) |

### 5.3 Data plan

Ingest in the order the owner requests games. Cards by sport, P-001 to P-600:

| Sport | Cards |
|---|---:|
| Baseball | 186 |
| Soccer | 136 |
| Basketball | 67 |
| Cricket | 52 |
| Tennis | 40 |
| AFL | 27 |
| American football | 19 |
| Rugby league | 19 |
| Ice hockey | 9 |

So soccer and baseball lanes matter as much as the NBA, and the soccer lane has to cover several leagues.

- **Label tiers:** as in the 14 October framework (receipt-verified A, observed-field B).
- **Line-up snapshots:** capture them, with publication times, at every freeze. This is the only honest route to models that know the line-ups.

### 5.4 Validation

- **Walk-forward only:** fit on earlier games, tune on a later window, calibrate on a third, and test on the newest.
- **Log every attempted candidate.**
- **Preregister the shadow:** metric, effect size, floors and stopping rule.

These are already the framework's rules. The change is to apply them to the competitions that are actually requested.

### 5.5 How it improves over time

| Cadence | What changes | What does not |
|---|---|---|
| Every settlement | Hedge weights (frozen recipe); ledger rows | Model structure; effect tables |
| Weekly | Dashboard; data-quality checks | Anything statistical |
| Monthly | Review only; a defect is fixed with a new version and lane | Parameters |
| Season end | Refit; effect tables and λ re-estimated; new calibration; new release and lane | Issued records |

### 5.6 Season releases (REV-06)

A release stays frozen for a competition's season. Bug fixes that do not change outputs are allowed; anything else waits for the next season or starts a new lane. This removes the churn that kept every lane at 0 events.

## 6. Reinforcement learning

**Why not for forecasting.**
- RL learns actions whose consequences depend on the action. A forecast does not change the game.
- At settlement the outcome of every contract is known, whichever ones were picked. That is full-information online learning, where exploration has no value.
- The decision lab confirmed the full-information setting: the bandit's inverse-propensity estimate matched the exact value.
- It also found every staking policy negative against the close, because the model itself was worse than the close.

**What to keep and improve.** Online expert weighting (Hedge; Freund & Schapire 1997) is the right tool: it re-weights the fast, slow and baseline experts from settled losses. To improve it:
- tune the half-life and learning rate per sport on walk-forward history;
- try stacking (a logistic regression on the experts' logits) as a challenger;
- if D1 allows, add a market expert as a benchmark;
- call it "online learning", not RL, in the documents.

**Where RL-like methods could apply, and the verdict:**

| Use | Verdict |
|---|---|
| Forecasting outcomes | No (above) |
| Choosing which sources to check under a time budget (a contextual bandit rewarded by error reduction) | A research idea only; low priority |
| Staking (Kelly, bandits) | Outside this framework (CURRENT_RULES §5). If it were ever a separate project, the practical finding is an adaptive fractional Kelly with risk controls (Uhrín et al. 2021), and it needs a real edge first |
| In-play | Out of scope: online in-play betting is prohibited in Australia (Interactive Gambling Act 2001; CURRENT_RULES §5a) |

## 7. Simulation

### 7.1 When to simulate

| Sport / contract | Exact method | Simulation? |
|---|---|---|
| Basketball, AFL, NFL and rugby winner, spread, total | Normal (t-tails); NFL key-number table | No |
| Soccer results, totals, handicaps | Dixon–Coles grid | No |
| Hockey winner, totals | Regulation grid plus OT/SO | No |
| Hockey puck lines ±1.5 and ±2.5 | Grid plus an empty-net adjustment | Optional: a late-game simulation of the goalie pull. Teams trailing in the final two minutes pulled the goalie in about 98% of cases from 2013-14 to 2019-20 (Hockey-Graphs) |
| Baseball run lines, first five innings, extras | Grid with the tie mass reassigned (by hand) | Yes: a half-inning Markov chain (Bukiet, Harold & Palacios 1997) |
| Cricket innings totals, chases, DLS | Normal with heavy tails (approximate) | Yes, once ball-by-ball data is captured (Davis, Perera & Swartz 2015) |
| Tennis match, sets, games | Exact recursion | Only for match-level form shocks or retirement risk |
| Player props, one player | Count model × minutes | Optional |
| Correlated props and same-game combinations | None | Yes: shared pace and minutes. Error correlation is essential: basketball season simulations were systematically overconfident until it was added ("Misadventures in Monte Carlo", *Journal of Sports Analytics*) |
| Early season and new competitions | None | Yes: draw ratings from their uncertainty and push each draw through the exact grid |
| Ladders, finals, futures | None | Yes: season simulation |
| Evaluation intervals and power | None | Yes: block bootstrap (exists) |

### 7.2 Standards

- **Code only**, with the seed and N printed.
- **N ≥ 100,000 near a threshold** (standard error ≤ 0.0016 at p = 0.5), with the Monte Carlo error reported.
- **Common random numbers** when comparing contracts.
- **Validate first:** a simulator is checked against history (coverage and calibration) before any card uses it.
- **Never claim a simulation that did not run.**

### 7.3 Rewording the game request

Replace "Do as many simulations as possible" with: "Use exact distributions; where the framework's simulation table requires it, run code simulations and report the seed, N and Monte Carlo error."

## 8. What to research and where, by sport

Value: **H** can move a fair probability by several points, **M** by about one to three, **L** rarely matters. Sizes must come from the effect tables (REV-17). The verified lanes in [SOURCES.md](../../../SOURCES.md) remain the first port of call.

### 8.1 Basketball (NBA, WNBA, NBL, EuroLeague, ACB, B.League, KBL and others)

| Input | Value | When published | Where |
|---|---|---|---|
| Status of key players (top minutes) | H | NBA: 5 p.m. local the day before; game-day report 11 a.m.–1 p.m. | NBA official injury report; team and league sites elsewhere; ESPN API for NBL and WNBA starters and DNPs |
| Starting five, minutes restrictions | H | Shortly before the tip | Team announcements; league game centres |
| Rest, back-to-backs, travel | M | Schedule | League schedule; ESPN API |
| Player impact and minutes history | M (for L2) | Continuous | NBA stats, Basketball-Reference; public impact metrics (on different scales, so check before use) |
| Officials | L | NBA: about 9 a.m. ET | official.nba.com referee assignments |
| History for models | — | — | The SOURCES routes behind the retired 2026-10-14 builds (KBL, B.League, ACB, EuroCup, G League) and the EuroLeague and NBL routes, re-verified into the learning store |

Traps: preseason games; competition-specific overtime and quarter lengths; never carrying NBA defaults into FIBA leagues.

### 8.2 Baseball (MLB, KBO, NPB, CPBL, LMB)

| Input | Value | When published | Where |
|---|---|---|---|
| Starting pitchers (probable, then confirmed) | H | Days ahead; confirmed on the day | MLB Stats API; KBO and NPB official sites |
| Line-up | M–H | A few hours before | MLB game feed; club accounts |
| Bullpen workload (last three days) | M | Box scores | MLB Stats API |
| Park, temperature, wind | M (H for totals at wind-sensitive parks) | Forecast | Open-Meteo; MLB game-feed wind |
| Umpire | L–M | Day of the game | MLB game feed |
| Pitcher-quality data | — | — | Baseball Savant (Statcast), FanGraphs |
| History | — | — | Retrosheet; MLB Stats API; KBO GetScoreBoardScroll and npb.jp box scores (verified lanes) |

Traps: doubleheaders; openers; KBO and NPB ties and extra-inning rules.

### 8.3 Ice hockey (NHL, AHL, Liiga, SHL, Czech Extraliga and others)

| Input | Value | When published | Where |
|---|---|---|---|
| Starting goalie | H | Morning skate or warm-up | Team announcements; NHL API game centre |
| Skater absences, line changes | M | Day of the game | Team sites |
| Back-to-backs, travel | M | Schedule | NHL API |
| xG and goalie quality | M (for L1 and L2) | Nightly | MoneyPuck (shot data; game-by-game skaters and goalies) |
| History | — | — | NHL API; league sites for the AHL and European leagues (HockeyTech for the AHL) |

Traps: regulation-only against OT/SO settlement; ties from before the shootout era; empty-net goals in puck lines.

### 8.4 Soccer

| Input | Value | When published | Where |
|---|---|---|---|
| Confirmed XI | H | EPL: at least 75 minutes before; most leagues about 60 minutes | Club and league channels; ESPN API; FotMob (structured fallback) |
| Key absences, suspensions | H | Press conferences; disciplinary lists | League discipline pages; club news |
| Team strength (xG) | M | After each round | Understat (top leagues); FBref basic data (its advanced Opta data was removed in January 2026) |
| European club ratings | M (benchmark) | After each round | ClubElo (CSV API) |
| Rotation, fixture congestion | M | Fixture lists | League and cup schedules |
| Corners | — | — | Premier League pulselive API and UEFA matchstats (verified lanes); definitions differ by provider |
| History | — | — | football-data.co.uk (results; odds columns stripped), ESPN API |

Traps: draws; extra time and penalties in cups; women's leagues with thin data.

### 8.5 AFL and AFLW

| Input | Value | When published | Where |
|---|---|---|---|
| Selected 22 and late changes | H | Team lists at fixed times; final teams about 60 minutes before | AFL team lists; Champion Data's selected-team schedule |
| Venue, travel, ground familiarity | H | Fixture | AFL fixture |
| Weather (rain, wind) | M | Forecast | Open-Meteo |
| External model benchmark | — | Weekly | Squiggle API (games, tips, sources, standings, ladder, power; set a User-Agent with contact details) |
| History | — | — | AFL Tables; fitzRoy; Squiggle |

Traps: AFLW is not the AFL (widths and home edge are not yet derived); draws.

### 8.6 Rugby league (NRL, Super League and others)

| Input | Value | When published | Where |
|---|---|---|---|
| Team list and final 19 | H | Tuesday about 4 p.m. AEST; cut to 19 at 24 hours and 90 minutes | NRL.com team lists |
| Halves, hooker, fullback | H | Same | Same |
| Weather | M | Forecast | Open-Meteo |
| History | — | — | Rugby League Project; NRL.com match centre |

Traps: golden point; squads depleted during State of Origin.

### 8.7 Rugby union

| Input | Value | When published | Where |
|---|---|---|---|
| Team announcement | H | Usually about two days before | Unions' and clubs' channels |
| International strength prior | M | Weekly | World Rugby rankings (rankings page; its API is undocumented) |
| Weather | M | Forecast | Open-Meteo |

Traps: draws; neutral venues in tournaments.

### 8.8 American football (NFL, college)

| Input | Value | When published | Where |
|---|---|---|---|
| Quarterback status | H | Weekly injury report; inactives 90 minutes before kick-off | Team and league reports |
| Other key positions, offensive line | M | Same | Same |
| Wind, precipitation | M (totals) | Forecast | Open-Meteo |
| History and play-by-play | — | — | nflverse (play-by-play, schedules, injuries, depth charts) |

Traps: key numbers; overtime rules that differ between the regular season and the playoffs.

### 8.9 Cricket

| Input | Value | When published | Where |
|---|---|---|---|
| XI and toss | H | At the toss, usually about 30 minutes before the start | Cricbuzz, ESPNcricinfo, board sites |
| Venue scoring, pitch | H for totals | Pitch report on the day | Cricsheet history by venue; pitch reports |
| Rain and DLS | H in rain | Forecast | Open-Meteo |
| Dew in night games | M (weak evidence) | — | Weather (dew point) |
| History | — | — | Cricsheet ball-by-ball, all formats |

Traps: chase totals are capped near the target (existing rule); reduced-overs games. The toss: a study of over 44,000 matches found toss winners won about 2.8% more often, with a smaller edge in T20 (ESPNcricinfo blog, 2016).

### 8.10 Tennis

| Input | Value | When published | Where |
|---|---|---|---|
| Surface-specific Elo | H | Weekly | Tennis Abstract Elo reports |
| Fitness, recent workload, withdrawals | H | Tournament news | ATP and WTA; tournament sites |
| Serve and return statistics | M | Continuous | Tennis Abstract; ATP and WTA statistics |
| Indoor or outdoor, altitude, balls | L–M | Tournament facts | Tournament sites |
| History | — | — | Sackmann data (licence and status above) |

Traps: retirements and walkovers (settlement rules); best of three against best of five.

### 8.11 Every sport

- weather (Open-Meteo, venue-local match window, as the existing rule says);
- start time and timezone (existing rule);
- venue and neutral site;
- travel distance and time zones;
- schedule congestion;
- officials (low priority).

## 9. Competitions: tiers

The owner requests games from many competitions, often one card each. Different levels of data need different procedures.

| Tier | Definition | Examples | Procedure |
|---|---|---|---|
| A | Fitted release, verified history, official team news | NBA, NHL and MLB now; the EPL and top European leagues, NBL, EuroLeague, AFL, NRL and IPL after REV-07 | Full card from the reference model; information list; may anchor (D2) |
| B | Verified history but no release; reasonable team news | KBO, NPB, B.League, ACB, A-League, J1, Liiga, BBL, Super Rugby, Challenger tennis | Hand reference from TB-1-MD or a family prior; widths 10% wider; abstain more |
| C | Thin or unverified data; little team news | Bosnian Prva Liga RS, Algeria Ligue 1, UAE Pro League, Indian Super League, Czech women's league, PBA | Fast card only: family prior, wide widths, probabilities for the supplied rows, and "no strong pick" unless a fact is decisive. No Rank-1 claim above 0.65 on a near-even line |

A competition moves from C to B to A when its history is ingested (REV-07). Put the model work into the competitions the owner requests most.

## 10. How professionals do it, and what transfers

- **Bookmakers and exchanges.**
  - They set an opening line from a model, then move it as informed money arrives. In major markets the closing line reflects most public information.
  - Bettors who beat it consistently get limited. Kaunitz, Zhong & Kreiner (2017) found a strategy built on the bookmakers' own consensus odds and were restricted soon after.
  - *What transfers:* treat the close as the hardest benchmark (REV-04), and do not expect to beat it often in major leagues.
- **Betting syndicates and trading desks.**
  - They combine a rating model, player-level availability adjustments and fast news, and judge themselves by closing-line value, not hit rate.
  - Choosing models by calibration beat choosing by accuracy (Walsh & Joshi 2024, NBA, one betting season). Decorrelating a model from the bookmaker helped profit (Hubáček, Šourek & Železný 2019).
  - Profit and accuracy have to be judged separately: Wunderlich (dissertation, building on Wunderlich & Memmert 2020) argues that profitable returns can come from inaccurate models.
  - *What transfers:* the reference-plus-ledger design and choosing models by calibration.
- **Forecasting tournaments** (Good Judgment, ForecastBench).
  - They use reference classes, frequent small updates, averages of independent forecasts and Brier scoring.
  - On ForecastBench the best LLM (0.101) still trailed superforecasters (0.081) in the Forecasting Research Institute's late-2025 update.
  - *What transfers:* averaging, base rates and proper scores, and humility about LLM probabilities.
- **Public model aggregators.** Squiggle scores many AFL models on the same games every week.
  - *What transfers:* an external, non-market benchmark for the AFL (REV-20).
- **What has changed in the public landscape:**
  - FiveThirtyEight's sports models are gone: ABC News closed the site.
  - FBref lost its Opta advanced data in January 2026.
  - MoneyPuck, nflverse, Cricsheet, Retrosheet and Squiggle remain open.

## 11. Simplifying the governance

| ID | Change |
|---|---|
| REV-08a | Fix the contradictions listed in §2.2 RC7 (editorial; no change in behaviour) |
| REV-08b | A core of about 30 KB: honesty and custody (2 pages), contract and settlement rules (2 pages), the card checklist (2 pages), plus one sport sheet and one competition row. Everything else becomes reference or archive |
| REV-08c | `python -m ml card lint`: checks the card's arithmetic (masses sum to 1, p comes from the grid, line distances, width floors), required fields and timestamps, so the hand-ticked self-audit checklists can go |
| REV-08d | Statistical rules frozen for a season; procedure changes batched monthly; editorial changes at any time |
| REV-08e | Every new rule names the rule it replaces |

## 12. Roadmap

| ID | Priority | Change | Owner / prompt | Acceptance test | Effort | Depends on |
|---|---|---|---|---|---|---|
| REV-01 | P0 | Reference model for each requested competition, run before the card and printed as REFERENCE (D2) | Prompt 8 | Every Tier A card prints the reference p for every supplied row before the analyst's numbers | Large | REV-06, REV-07 |
| REV-02 | P0 | Adjustment ledger and effect tables; the ledger scored at settlement | Prompts 8 and 3 | Ledger on at least 90% of numeric cards; paired reference v final Brier reported monthly | Medium | REV-01 (TB-1-MD as the reference meanwhile) |
| REV-03 | P0 | Line-implied benchmark (0.5 at supplied two-way lines) in every settlement | Prompt 3 | Every settled supplied two-way row has a benchmark score | Small | D1 (a) |
| REV-04 | P1 | No-vig closing benchmark after settlement, outside the reading gate | Prompts 3 and 6 | A monthly table of card and model v close | Small to medium | D1 (b) |
| REV-05 | P0 | Width floors and tail rules; monthly coverage | Prompt 8 (toolkit) | Margin z RMS within 0.85–1.15 over 40 cards per family | Small | Competition rows |
| REV-06 | P0 | Season releases; a full-league NBA pregame shadow, then the soccer leagues, NBL and EuroLeague/ACB | Prompt 8 | The lane gains at least 40 games a week from its first week | Medium | REV-07 |
| REV-07 | P0 | Ingest verified history for requested competitions; line-up snapshots at freeze | Prompts 7 and 8 | NBA, NBL, EuroLeague, ACB, EPL and the top European leagues admitted | Large | — |
| REV-08 | P1 | Governance consolidation (REV-08a to REV-08e) | Prompt 8 | Reading gate ≤ 60 KB; 0 contradictions on a cross-check; card lint passes | Medium | — |
| REV-09 | P0 | New pick format (probability table, winner, most-likely list with difficulty, information list, abstain) | Prompt 8 | Every new card follows it | Small | REV-01 for full use |
| REV-10 | P1 | Calibrate fitted models in development before lanes; λ shrinkage for adjustments | Prompt 8 | Development calibration slope between 0.9 and 1.1 | Medium | REV-07 |
| REV-11 | P1 | Player-props engine in code | Prompt 8 | Development coverage of props within ±3 points at the 50% and 80% bands | Medium | Player data |
| REV-12 | P2 | Path simulators (baseball innings, cricket balls, tennis points plus form, hockey late game) | Prompt 8 | Each passes a historical coverage test before any card uses it | Medium to large | Data |
| REV-13 | P0 | Competition tiers and the Tier C fast procedure | Prompt 8 | Every card prints its tier | Small | — |
| REV-14 | P1 | Value-ranked, time-windowed research checklists per sport | Prompt 8 | A checklist in every sport sheet; research time per card falls | Small | — |
| REV-15 | P0 | Earlier requests where possible; a time budget and a fast card | Owner; prompt 8 | At least 80% of cards issued before the start | Small | — |
| REV-16 | P2 | Two independent research passes averaged on important cards | Owner's choice | A paired comparison after 40 cards | Small | REV-02 |
| REV-17 | P1 | Effect-size programme (home edge, rest, travel, altitude, weather, play rates by status) | Prompts 7 and 8 | Tables with n, period and interval per competition | Medium | REV-07 |
| REV-18 | P1 | Monthly dashboard per competition | Prompt 6 | Published every month | Small | REV-02, REV-06 |
| REV-19 | P2 | Hedge tuning study; rename "ML/RL" to "ML and online learning" | Prompt 8 | Walk-forward study report | Small | Lanes |
| REV-20 | P2 | External non-market benchmarks after settlement (Squiggle, ClubElo, Tennis Abstract Elo) | Prompt 6 | A paired table per sport | Small | — |
| REV-21 | P0 | Reword the game-request template (simulation, picks, abstain) | Owner | Template updated | Small | — |
| REV-22 | P1 | Data-quality gates before any release (integrity warnings; final scores from two sources) | Prompt 8 | No release with an open integrity flag | Small | — |

**Relation to open proposals:**
- REV-05 extends RET-12 and RET-19.
- REV-03 and REV-04 extend RET-10 and the 14 October D3-ii option.
- REV-07 extends RET-15, RET-21 and recommendation 3 of the 21 October review.
- REV-06 is that review's recommendation 5, and REV-10 its recommendation 4.
- Its competition parameter sheet (recommendations 1–2) becomes the competition rows used by REV-01 and REV-05.
- REV-22 includes RET-18.

## 13. Decisions for the owner

| # | Decision | Options | Recommendation |
|---|---|---|---|
| D1 | Market information | (a) a line-implied 0.5 benchmark, at settlement only; (b) a no-vig close benchmark after settlement; (c) the market line as the prior | (a) now: it needs no price and does not enter the research. (b) if you want to know whether the research beats the market. (c) only if accuracy matters more to you than independence. (c) would probably help most; most cards would then say "about 50%" on supplied lines, and the ledger would measure what the research adds to the market |
| D2 | Model role on cards | SHADOW (now, card-first); REFERENCE (printed before the card); ANCHOR (the card starts from the model and the analyst's changes are logged) | REFERENCE for Tier A now; ANCHOR per competition once its lane passes. The ledger keeps the measurement clean, because it compares the model and the final p on the same rows |
| D3 | Scope | Any competition, or a core list | Keep any competition, with tiers; put the model work into the competitions you request most |
| D4 | Governance | Keep or consolidate | Consolidate (REV-08) |
| D5 | Pick format | Top four by p, or the new format | The new format (REV-09); it still answers "most likely" |
| D6 | Latency | Research until done, or earlier requests plus a time budget and a fast card | Earlier requests where possible, plus a time budget and a fast card (REV-15) |
| D7 | RL | Confirm no RL in forecasting | Confirm |

## 14. Limits

- **Card statistics** are outcome-exposed and descriptive. Rows are dependent, and supplied and derived lines cannot be separated before 12 October.
- **Model numbers** are development evidence on unadmitted archive data.
- **External sources:** several were checked only through abstracts or citing papers (marked below). Effect sizes quoted from them are starting points to be re-estimated, never constants.
- **The redesign's benefits** are expectations drawn from the evidence above, not demonstrated results. Each needs its own test.
- **No rule, model or record** was changed by this review.

## Sources

### Repository

- [CARD_P_DIAGNOSTICS.csv](CARD_P_DIAGNOSTICS.csv) (this review), from [CARD_ROWS.csv](../retrospective_2026-10-21/HISTORY/CARD_ROWS.csv)
- [2026-10-21 cohort retrospective](../retrospective_2026-10-21/RETROSPECTIVE_REPORT.md) · [2026-10-16 full-history retrospective](../retrospective_2026-10-16-full/RETROSPECTIVE_REPORT.md) · [2026-10-11 retrospective](../retrospective_2026-10-11/RETROSPECTIVE_REPORT.md)
- [21 October league-neutral, ML and simulation review](../review_2026-10-21_league_neutral_ml_sim/REPORT.md) · [22 October simulation review](../framework_change_2026-10-22-1/SIMULATION_REVIEW.md)
- [Decision-lab results](../../model_shadow/DECISION_LAB/RESULTS.md) · [CURRENT_RELEASES.csv](../../cycle_releases/CURRENT_RELEASES.csv) · [active mini](../../active_minis/20261022F6K3OJNO.md)
- [CURRENT_RULES](../../../CURRENT_RULES.md) · [METHOD](../../../METHOD.md) · [CURRENT_STATE](../../../CURRENT_STATE.md) · [SELECTION_RULES](../../../SELECTION_RULES.md) · [PROBABILITY_TOOLKIT](../../../PROBABILITY_TOOLKIT.md) · [FORECAST_CYCLE_PROTOCOL](../../../FORECAST_CYCLE_PROTOCOL.md) · [ML_RL_IMPLEMENTATION_FRAMEWORK_2026-10-14](../../../ML_RL_IMPLEMENTATION_FRAMEWORK_2026-10-14.md)

### Markets, odds and forecast quality

- Štrumbelj, E. and Vračar, P. (2012). Simulating a basketball match with a homogeneous Markov model and forecasting the outcome. *International Journal of Forecasting* 28(2), 532–542. [Abstract](https://iaorifors.com/paper/76013)
- Štrumbelj, E. (2014). On determining probability forecasts from betting odds. *International Journal of Forecasting* 30(4), 934–943. Checked through citing sources only; Shin's method is reported more accurate than basic normalisation ([shin package](https://pypi.org/project/shin/)).
- Goto, K., Takeishi, N. and Yairi, T. (2026). Forecast sports outcomes under efficient market hypothesis. [arXiv 2604.17194](https://arxiv.org/abs/2604.17194)
- Snowberg, E. and Wolfers, J. (2010). Explaining the favorite-longshot bias: is it risk-love or misperceptions? *Journal of Political Economy* 118(4), 723–746. [NBER w15923](https://www.nber.org/papers/w15923)
- Kaunitz, L., Zhong, S. and Kreiner, J. (2017). Beating the bookies with their own numbers. [arXiv 1710.02824](https://arxiv.org/pdf/1710.02824)
- Hubáček, O., Šourek, G. and Železný, F. (2019). Exploiting sports-betting market using machine learning. *International Journal of Forecasting* 35(2), 783–796. [IDEAS](https://ideas.repec.org/a/eee/intfor/v35y2019i2p783-796.html)
- Walsh, C. and Joshi, A. (2024). Machine learning for sports betting: should model selection be based on accuracy or calibration? *Machine Learning with Applications* 16, 100539. [Bath portal](https://researchportal.bath.ac.uk/en/publications/machine-learning-for-sports-betting-should-model-selection-be-bas/)
- Wunderlich, F. and Memmert, D. (2020). Are betting returns a useful measure of accuracy in (sports) forecasting? *International Journal of Forecasting* 36(2), 713–722. [IDEAS](https://ideas.repec.org/a/eee/intfor/v36y2020i2p713-722.html); abstract not checked, argument taken from [Wunderlich's dissertation](https://fis-db.dshs-koeln.de/ws/portalfiles/portal/6465170/Dissertation_Wunderlich.pdf)
- Uhrín, M., Šourek, G., Hubáček, O. and Železný, F. (2021). Optimal sports betting strategies in practice: an experimental review. [arXiv 2107.08827](https://arxiv.org/abs/2107.08827v1)
- Winston, W. (2018). Why is the standard deviation of NBA scores about the point spread 12 points? (back-of-envelope estimate). [Blog](https://www.goodreads.com/author_blog_posts/16483561-why-is-standard-deviation-of-nba-scores-about-point-spread-12-points)
- Lopez, M., Matthews, G. and Baumer, B. (2018). How often does the best team win? *Annals of Applied Statistics* 12(4), 2483–2516. [arXiv 1701.05976](https://arxiv.org/abs/1701.05976v2); extends Glickman, M. and Stern, H. (1998), A state-space model for National Football League scores, *JASA* (not separately checked)

### Ratings and score models

- Dixon, M. and Coles, S. (1997). Modelling association football scores and inefficiencies in the football betting market. *JRSS C* 46, 265–280. [Bristol](https://research-information.bris.ac.uk/en/publications/modelling-association-football-scores-and-inefficiencies-in-the-f/)
- Koopman, S. J. and Lit, R. (2015). A dynamic bivariate Poisson model for analysing and forecasting match results in the English Premier League. *JRSS A* 178(1), 167–186. [Working paper](https://econpapers.repec.org/RePEc:tin:wpaper:20120099)
- Baio, G. and Blangiardo, M. (2010). Bayesian hierarchical model for the prediction of football results. *Journal of Applied Statistics* 37(2), 253–264. [UCL](https://discovery.ucl.ac.uk/id/eprint/16040/)
- Constantinou, A. and Fenton, N. (2013). Determining the level of ability of football teams by dynamic ratings (pi-ratings). *JQAS* 9(1), 37–50. [Accepted draft](https://qmro.qmul.ac.uk/xmlui/bitstream/123456789/10776/5/CONSTANTINOU%20Determing%20the%20Level%20of%20Ability%202012%20Accepted.pdf)
- Hvattum, L. M. and Arntzen, H. (2010). Using ELO ratings for match result prediction in association football. *International Journal of Forecasting* 26(3), 460–470. [BibSonomy](https://www.bibsonomy.org/bibtex/a0ef8f0c642f671fd027607d2b69ac6a); Arntzen, H. and Hvattum, L. M. (2021). Predicting match outcomes in association football using team ratings and player ratings. *Statistical Modelling* 21(5), 449–470. [Abstract](https://statmod.org/smij/Vol21/Iss5/Arntzen/Abstract.html)
- Berrar, D., Lopes, P. and Dubitzky, W. (2019). Incorporating domain knowledge in machine learning for soccer outcome prediction. *Machine Learning* 108, 97–126. [Anthology](https://mlanthology.org/mlj/2019/berrar2019mlj-incorporating); challenge comparison in [arXiv 2403.07669](https://arxiv.org/pdf/2403.07669)
- Expected goals: [PLOS ONE (2023)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10075453/); [ElHabr (2024)](https://tonyelhabr.rbind.io/posts/xg-predictor-future-results/)
- Ryall, R. and Bedford, A. (2010). An optimized ratings-based model for forecasting Australian Rules football. *International Journal of Forecasting* 26(3), 511–517. [USC](https://research.usc.edu.au/esploro/outputs/journalArticle/An-optimized-ratings-based-model-for-forecasting/99451405402621)
- Kovalchik, S. (2016). Searching for the GOAT of tennis win prediction. *JQAS* 12(3), 127–138. [De Gruyter](https://www.degruyterbrill.com/document/doi/10.1515/jqas-2015-0059/html)
- Barnett, T. and Clarke, S. (2005). Combining player statistics to predict outcomes of tennis matches. *IMA Journal of Management Mathematics* 16(2), 113–120. [VU](https://vuir.vu.edu.au/8502/)
- Klaassen, F. and Magnus, J. (2001). Are points in tennis independent and identically distributed? *JASA* 96(454), 500–509. [Tilburg](https://research.tilburguniversity.edu/en/publications/are-points-in-tennis-independent-and-identically-distributed-evid/)
- Tennis Abstract. An introduction to tennis Elo (surface blend). [Blog](https://www.tennisabstract.com/blog/2019/12/03/an-introduction-to-tennis-elo/)
- Rest effects: [Small (NESSIS 2007)](https://www.nessis.org/nessis07/Dylan_Small.pdf); [Frontiers in Psychology (2021)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7925613/)
- Home advantage without crowds: [PMC8560007](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8560007/); [Tinbergen 24-014](https://papers.tinbergen.nl/24014.pdf)

### Simulation

- Bukiet, B., Harold, E. and Palacios, J. (1997). A Markov chain approach to baseball. *Operations Research* 45(1), 14–23. [NJIT](https://researchwith.njit.edu/en/publications/a-markov-chain-approach-to-baseball/)
- Davis, J., Perera, H. and Swartz, T. (2015). A simulator for Twenty20 cricket. *Australian and New Zealand Journal of Statistics* 57(1), 55–71. [Preprint](https://www.sfu.ca/~tswartz/papers/t20sim.pdf)
- Misadventures in Monte Carlo. *Journal of Sports Analytics*. [SAGE](https://journals.sagepub.com/doi/10.3233/JSA-170220) (abstract only)
- Hockey-Graphs (2020). The state of goalie pulling in the NHL. [Article](https://hockey-graphs.com/2020/05/18/the-state-of-goalie-pulling-in-the-nhl/)

### Calibration, scoring and aggregation

- Gneiting, T. and Raftery, A. (2007). Strictly proper scoring rules, prediction, and estimation. *JASA* 102(477), 359–378. DOI 10.1198/016214506000001437 (abstract only)
- Kull, M., Silva Filho, T. and Flach, P. (2017). Beta calibration. *AISTATS*, PMLR 54, 623–631. [PMLR](https://proceedings.mlr.press/v54/kull17a.html)
- Satopää, V. et al. (2014). Combining multiple probability predictions using a simple logit model. *International Journal of Forecasting* 30(2), 344–356. [Academia](https://www.academia.edu/13898151/Combining_multiple_probability_predictions_using_a_simple_logit_model)
- Baron, J. et al. (2014). Two reasons to make aggregated probability forecasts more extreme. *Decision Analysis* 11(2), 133–145. [IDEAS](https://ideas.repec.org/a/inm/ordeca/v11y2014i2p133-145.html)
- Mellers, B. et al. (2014). Psychological strategies for winning a geopolitical forecasting tournament. *Psychological Science* 25(5), 1106–1115. [APS](https://www.psychologicalscience.org/journals/psychological-science/0956797614524255/); 2025 reanalysis: [APS](https://www.psychologicalscience.org/journals/psychological-science/09567976241266481/)
- Freund, Y. and Schapire, R. (1997). A decision-theoretic generalization of on-line learning and an application to boosting (Hedge). *Journal of Computer and System Sciences* 55(1), 119–139.

### Machine learning and LLM forecasting

- Bunker, R. and Susnjak, T. (2022). The application of machine learning techniques for predicting match results in team sport: a review. *JAIR* 73, 1285–1322. [JAIR](https://jair.org/index.php/jair/article/view/13509)
- Grinsztajn, L., Oyallon, E. and Varoquaux, G. (2022). Why do tree-based models still outperform deep learning on typical tabular data? *NeurIPS Datasets and Benchmarks*. [arXiv 2207.08815](https://arxiv.org/abs/2207.08815v1)
- Halawi, D., Zhang, F., Yueh-Han, C. and Steinhardt, J. (2024). Approaching human-level forecasting with language models. *NeurIPS*. [arXiv 2402.18563](https://arxiv.org/html/2402.18563v1)
- Schoenegger, P., Tuminauskaite, I., Park, P. and Tetlock, P. (2024). Wisdom of the silicon crowd. *Science Advances*. [arXiv 2402.19379](https://www.arxiv.org/abs/2402.19379)
- Karger, E. et al. (2025). ForecastBench. *ICLR*. [Proceedings](https://proceedings.iclr.cc/paper_files/paper/2025/hash/ea74e45a229dac70b5b63b28d8934db6-Abstract-Conference.html); late-2025 leaderboard update: [Forecasting Research Institute](https://forecastingresearch.substack.com/p/ai-llm-forecasting-model-forecastbench-benchmark)
- Leng, J. et al. (2024). Taming overconfidence in LLMs: reward calibration in RLHF. [arXiv 2410.09724](https://arxiv.org/pdf/2410.09724v1)

### Team news, data sources and the public landscape

- [NBA injury report rules, 2025-26](https://official.nba.com/nba-injury-report-2025-26/) · [NBA referee assignments](https://official.nba.com/referee-assignments/)
- [Premier League line-up timing change, 2024-25](https://www.liverpoolfc.com/news/explained-premier-league-changes-2024-25-season)
- [NRL team lists, 2026](https://www.nrl.com/news/2026/04/14/nrl-team-lists-round-7/)
- [AFL selected-team schedule (Champion Data)](https://docs.api.afl.championdata.com/support/selected-team-schedule/)
- [NFL inactives timing (ESPN)](https://africa.espn.com/fantasy/football/story/_/page/FFSundayInactives-47255473/nfl-fantasy-football-espn-injured-inactives-watchlist-week-15-2025-december-14)
- [MoneyPuck data](https://moneypuck.com/data.htm) · [Squiggle API](https://api.squiggle.com.au/) · [ClubElo via soccerdata](https://soccerdata.readthedocs.io/en/latest/datasources/ClubElo.html) · [Cricsheet via cricketdata](https://pkg.robjhyndman.com/cricketdata/articles/cricketdata_R_pkg.html) · [nflverse (nfl_data_py)](https://github.com/nflverse/nfl_data_py) · [Sackmann archive mirror and licence](https://huggingface.co/datasets/Aneeshers/tennis-sackmann-archive)
- [FBref loses Opta advanced data (January 2026)](https://amp.awfulannouncing.com/soccer/sports-reference-pulls-advanced-data-agreement-violation-dispute.html) · [FiveThirtyEight closed by ABC News](https://frontofficesports.com/article/abc-disney-layoffs-538-shuttered/)
- [Cricket toss study (ESPNcricinfo blog, 2016)](https://gsood.com/research/press/CricketESPN.pdf)
