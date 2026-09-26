# Numerical model register
> **Current revision — CR-2026.09.21-3:** METHOD **MDS-2026.09.19-v4.3** is the workflow/template authority; **SCORING_AND_VALIDATION.md** controls conditioning, exact scoring, event-level evaluation and prospective evidence. All existing logs remain LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE. NUMERICAL_PROGRAM controls authorized implementation scope and actual build state; MODEL_IMPLEMENTATION_RECIPES contains the executable Markdown reference. Older dated policy blocks are historical where inconsistent. No source, dataset or model is approved/fitted by this banner.








> **`NUMERICAL_PROGRAM.md` is the new entry point (v4.0 comprehensive overhaul, 2026-09-06).** This document remains the full candidate-model reference.




Status: **ACTIVE DESIGN REGISTER — ALL NUMERICAL BUILDS NOT FIT — DETAILED REFERENCE**




Register version: **NMR-2026.09.19-v0.4**




Numerical training specification: **NTS-2026.09.19-v0.5**




Governing published forecast method: **MDS-2026.09.19-v4.3 / CR-2026.09.21-3 — SPORTS_ONLY / MARKET_BLIND qualitative method; no numerical champion is fitted**




Effective: **2026-08-25**




This register separates an architecture candidate from an immutable fitted build. A model family, paper, source, external forecast or completed Markdown card is not a fitted model and cannot generate an internal probability.




## 1. Status vocabulary




| Status | Meaning |
|---|---|
| DESIGN REGISTERED | Target, family, role and comparison documented; no fit |
| DATA BLOCKED | Fit cannot start because H0/source/feature approval is missing |
| FIT — TRAIN ONLY | Training artifact exists; no TUNE/CAL/TEST claim |
| TUNED | Selection completed inside the permitted TUNE block |
| CALIBRATED | Frozen calibrator fitted on disjoint CAL data |
| TESTED — NOT PROMOTED | Untouched TEST opened and recorded; publication remains disabled |
| SHADOW | Immutable pre-result E1-P outputs accumulating; not user-facing |
| VALIDATED CHALLENGER | Required gates passed but build is not published champion |
| CHAMPION — VERSIONED | Governing model for one exact approved scope |
| SUPPRESSED | Build exists but display blocked by source/OOD/drift/calibration/version failure |
| RETIRED | No new predictions; artifacts remain immutable evidence |




No model currently exceeds `DESIGN REGISTERED / DATA BLOCKED`.




## 2. Portfolio roles




| Role | Definition |
|---|---|
| A0 | Mandatory empirical/rating/simple count or rate × exposure baseline |
| A1 | Interpretable hierarchical/distributional model with target-valid support |
| A2 | Sport-native generative event/state simulator |
| A3/A4 | Flexible distributional boosting, ordered-CDF or non-crossing-quantile challenger |
| M0 | RETIRED — market-only predictive benchmark excluded by MARKET_BLIND |
| M1 | RETIRED — market-informed hybrid excluded by MARKET_BLIND |




A2 is structurally preferred for expressing state transitions and dependence, but it is not presumed superior. A simpler candidate remains champion until an untouched chronological comparison and prospective shadow support promotion.




## 3. All-sports candidate register




Each group is instantiated for an exact target/population/horizon only after its H0 card is frozen.




| Candidate group ID | Sport/target family | Role and output | Frozen comparison purpose | Status |
|---|---|---|---|---|
| `CR-A0-ECDF-COUNT-v0` | Cricket run/resource targets | Conditional empirical CDF plus Poisson diagnostic | Transparent distribution/dispersion baseline | DESIGN REGISTERED / DATA BLOCKED |
| `CR-A1-DIST-v0` | Cricket run/resource targets | Hierarchical NB/GAMLSS or target-valid distributional regression | Test interpretable location/dispersion/shape | DESIGN REGISTERED / DATA BLOCKED |
| `CR-A2-STATE-SIM-v0` | Cricket run/wicket/match state | Coupled delivery/over resource and termination simulation | Coherent runs, wickets, innings/day transitions, match outcomes | DESIGN REGISTERED / DATA BLOCKED |
| `CR-A3-FLEX-CDF-v0` | Cricket target distribution | NGBoost, ordered CDF or non-crossing quantile challenger | Nonlinear/flexible shape without line classifiers | DESIGN REGISTERED / DATA BLOCKED |
| `BB-A0-EMP-POSS-v0` | Basketball joint score | Empirical/ratings and simple possession × efficiency distribution | Minimal possession-aware baseline | DESIGN REGISTERED / DATA BLOCKED |
| `BB-A1-JOINT-DIST-v0` | Basketball joint score | Hierarchical bivariate/discrete location-scale score model | Test covariance, league/rules and lineup adjustments | DESIGN REGISTERED / DATA BLOCKED |
| `BB-A2-POSS-SIM-v0` | Basketball joint score | Possession/lineup-stint shot/FT/turnover/rebound simulator | Coherent score, total, margin, winner and OT tails | DESIGN REGISTERED / DATA BLOCKED |
| `BB-A3-FLEX-GRID-v0` | Basketball joint score | Boosted/ordered joint score or component distribution | Nonlinear challenger with support/calibration checks | DESIGN REGISTERED / DATA BLOCKED |
| `AF-A0-EMP-DRIVE-v0` | American-football joint score | Empirical/key-score and simple drive-rate baseline | Minimal discrete scoring comparator | DESIGN REGISTERED / DATA BLOCKED |
| `AF-A1-DRIVE-DIST-v0` | American-football joint score | Hierarchical drive outcome and discrete score distribution | Test QB/field-position/rules partial pooling | DESIGN REGISTERED / DATA BLOCKED |
| `AF-A2-DRIVE-SIM-v0` | American-football joint score | Drive/play/clock/field-position/scoring-state simulation | Coherent side/total/margin, key values and OT | DESIGN REGISTERED / DATA BLOCKED |
| `AF-A3-FLEX-GRID-v0` | American-football score grid | Boosted state components/ordered score grid | Flexible challenger without independent line heads | DESIGN REGISTERED / DATA BLOCKED |
| `BS-A0-EMP-COUNT-v0` | Baseball joint runs | Empirical plus Poisson/NB diagnostic | Run-dispersion and simple baseline | **MLB: CODE IMPLEMENTED (2026-09-26, `tools/mlb_model.py` A0) — SHADOW lane open; not fit** |
| `BS-A1-JOINT-RUN-v0` | Baseball joint runs | Hierarchical bivariate count/distributional model | Test lineup/starter/bullpen/park covariance | **MLB: CODE IMPLEMENTED (2026-09-26, `tools/mlb_model.py` A1: pooled team, park, home, starter; shared-gamma joint) — SHADOW lane open (`C-MLB-SHADOW`); declared priors, not fit; historical validation not yet run** |
| `BS-A2-PA-BASEOUT-v0` | Baseball joint runs | PA/base-out/starter-hook/bullpen/home-ninth/extra simulation | Coherent winner, totals and run lines | DESIGN REGISTERED / DATA BLOCKED |
| `BS-A3-FLEX-RUN-v0` | Baseball joint runs | Boosted/ordered run-grid challenger | Flexible overdispersion/interaction test | DESIGN REGISTERED / DATA BLOCKED |
| `AFL-A0-EMP-SHOT-v0` | AFL/AFLW joint score | Empirical and simple scoring-shot/conversion baseline | Separate territory/volume from conversion | DESIGN REGISTERED / DATA BLOCKED |
| `AFL-A1-GOAL-BEHIND-v0` | AFL/AFLW joint score | Hierarchical goals/behinds/score distribution | Test competition/venue/shot-quality covariance | DESIGN REGISTERED / DATA BLOCKED |
| `AFL-A2-TERRITORY-SIM-v0` | AFL/AFLW joint score | Territory -> inside-50 -> shot -> goal/behind simulation | Coherent totals, margins, winner and phase paths | DESIGN REGISTERED / DATA BLOCKED |
| `AFL-A3-FLEX-SCORE-v0` | AFL/AFLW joint score | Boosted/ordered score challenger | Nonlinear target-valid distribution comparison | DESIGN REGISTERED / DATA BLOCKED |
| `RL-A0-EMP-SET-v0` | Rugby-league joint score | Empirical and simple set/try/conversion baseline | Minimal field-position/scoring comparator | DESIGN REGISTERED / DATA BLOCKED |
| `RL-A1-DISCRETE-SCORE-v0` | Rugby-league joint score | Hierarchical discrete try/goal/field-goal distribution | Test scoring-combination and population fit | DESIGN REGISTERED / DATA BLOCKED |
| `RL-A2-SET-SIM-v0` | Rugby-league joint score | Set/field-position/try/conversion/sin-bin/golden-point simulation | Coherent winner, total and margin | DESIGN REGISTERED / DATA BLOCKED |
| `RL-A3-FLEX-SCORE-v0` | Rugby-league joint score | Boosted/ordered score-grid challenger | Nonlinear interactions with support safeguards | DESIGN REGISTERED / DATA BLOCKED |
| `SOC-A0-POIS-v0` | Soccer regulation goals | Independent Poisson/empirical score grid | Mandatory low-count baseline | DESIGN REGISTERED / DATA BLOCKED |
| `SOC-A1-DC-BIVAR-v0` | Soccer regulation goals | Dynamic hierarchical Dixon–Coles/bivariate count grid | Low-score dependence, attack/defence and draw comparison | DESIGN REGISTERED / DATA BLOCKED |
| `SOC-A2-SHOT-GOAL-SIM-v0` | Soccer regulation goals | Shot/goal/lineup/score-state/red-card simulation | Coherent 1X2, totals, BTTS and handicap | DESIGN REGISTERED / DATA BLOCKED |
| `SOC-A3-FLEX-GRID-v0` | Soccer score grid | Boosted/ordered joint goal-grid challenger | Flexible score distribution and calibration | DESIGN REGISTERED / DATA BLOCKED |
| `IH-A0-POIS-v0` | Ice-hockey regulation goals | Empirical/independent Poisson score grid | Mandatory low-count baseline | DESIGN REGISTERED / DATA BLOCKED |
| `IH-A1-JOINT-GOAL-v0` | Ice-hockey regulation goals/result | Hierarchical bivariate goal/shot distribution | Test dispersion, covariance, goalie/manpower effects | DESIGN REGISTERED / DATA BLOCKED |
| `IH-A2-SHIFT-SHOT-SIM-v0` | Ice-hockey regulation plus result state | Shift/shot/xG/manpower/goalie/pulled-goalie/OT-SO simulation | Coherent regulation and match-result contracts | DESIGN REGISTERED / DATA BLOCKED |
| `IH-A3-FLEX-GRID-v0` | Ice-hockey goal grid | Boosted/ordered goal-grid challenger | Flexible nonlinear and tail comparison | DESIGN REGISTERED / DATA BLOCKED |
| `TEN-A0-SERVE-RETURN-v0` | Tennis, surface/format-specific completed matches | Serve/return empirical baseline, point-to-match recursion | Joint games/sets/winner with tiebreak, final-set and retirement contract | DESIGN REGISTERED / DATA BLOCKED |
| `TEN-A1-HIER-POINT-v0` | Tennis, exact surface/format | Hierarchical opponent-adjusted serve/return point model | Role/workload scenarios and coherent total-games distribution | DESIGN REGISTERED / DATA BLOCKED |
| `TEN-A2-MATCH-STATE-v0` | Tennis, exact rule era | Point/game/set/retirement state process | Termination, break-back and fatigue scenarios without independent line heads | DESIGN REGISTERED / DATA BLOCKED |
| `RU-A0-EMP-SCORE-v0` | Rugby union, competition-specific regulation score | Empirical scoring-event baseline | Tries/conversions/penalties/drop-goals, exact draw/endpoint support | DESIGN REGISTERED / DATA BLOCKED |
| `RU-A1-HIER-SCORE-v0` | Rugby union, competition-specific joint score | Hierarchical event/exposure model | Territory, kicker, cards, bench and joint totals/margins | DESIGN REGISTERED / DATA BLOCKED |
| `RU-A2-PHASE-STATE-v0` | Rugby union, regulation and separately scoped extra time | Possession/territory/scoring/clock state process | Joint phase/full-match queries and exact terminal rules | DESIGN REGISTERED / DATA BLOCKED |








M0/M1 are RETIRED from active, shadow and promotion-eligible prediction. A user-requested post-freeze price audit is segregated and cannot train or alter a forecast.




## 4. Player and niche-target templates




These are separate model groups, not direct team-score queries:




| Template ID | Target process | Candidate ladder | Status |
|---|---|---|---|
| `PLAYER-COUNT-EXP-RATE-v0` | Participation/start × workload/exposure × opponent-adjusted event rate | Empirical/hierarchical count -> state-linked simulator -> flexible CDF | DESIGN REGISTERED / DATA BLOCKED |
| `SOCCER-CORNER-v0` | Corner-causing exposure/rate with score-state dependence | Poisson diagnostic -> NB/compound count -> state-linked simulator | DESIGN REGISTERED / DATA BLOCKED |
| `SOCCER-SOT-v0` | Minutes × shots per minute × role/box share × on-target conversion | Hierarchical components -> linked event simulator -> flexible CDF | DESIGN REGISTERED / DATA BLOCKED |
| `CRICKET-BATTER-RUNS-v0` | Balls faced jointly with dismissal hazard × run rate | Survival/count components -> ball-state simulator | DESIGN REGISTERED / DATA BLOCKED |




Every instantiated target requires exact provider/action/void terms and its own H0/support/calibration gate.




## 5. Prohibited production designs




The following may exist only as labelled diagnostics unless a new specification proves coherence:




- unrelated binary classifiers/calibrators for each bookmaker threshold;
- training on user-selected games/lines as if they were an eligible-event universe;
- post-forecast or post-result alternate-line selection;
- a point mean with an assumed, unestimated standard deviation;
- an untreated continuous distribution with invalid negative/fractional mass;
- a team-score model substituted for a player, corner, SOT or other unmodelled event;
- a pregame build reused for live states or regulation output reused for OT/advance terms;
- a market-informed build presented as market-blind;
- a later closing price used at an earlier cutoff;
- a website search result or external forecast presented as an internal fitted probability.




## 6. Immutable build card




Every actual fit appends:




| Field | Required value |
|---|---|
| Build ID/parent/status/created | Stable immutable identity and artifact time |
| Target/population/horizon | Exact target and homogeneous scope |
| H0/split manifest | Dataset hash and chronological TRAIN/TUNE/CAL/TEST blocks |
| Source/feature manifest | Approved snapshots, definitions and transform versions |
| Market lane | MARKET_BLIND, MARKET_ONLY or MARKET_INFORMED |
| Algorithm/distribution | Family, link, support, parameters and software/code version |
| Hierarchy/dynamic state | Pooling, priors, ratings, decay and regime handling |
| Simulator/scenarios | State, transitions, termination, weights, seed/draws/error |
| Tuning | Frozen search, score, guardrails and spent TUNE block |
| Calibration | Method/version, disjoint CAL and coherence treatment |
| Test | One-time untouched TEST, baselines, uncertainty and slices |
| Operations | Latency, source/missing/OOD/drift/version suppression behavior |
| Publication | NOT PUBLISHED/PUBLISHED/SUPPRESSED and approved scope |
| Provenance | Code/data/model/calibrator hashes and immutable references |
| Limitations | Unsupported populations, failure modes and prohibited uses |




## 7. Frozen comparison questions




| Comparison ID | Question | Primary evidence | Current state |
|---|---|---|---|
| `CMP-ALL-DIST-v0` | Does one target distribution outperform/cohere better than independent threshold heads? | CRPS/RPS plus threshold Brier/log score and complement/nesting checks | CANDIDATE — NOT STARTED |
| `CMP-ALL-A2-v0` | Does the sport-native A2 simulator improve over best A0/A1? | Same-fold distribution score, coverage, critical scenarios and simulation error | CANDIDATE — NOT STARTED |
| `CMP-ALL-FLEX-v0` | Does A3/A4 improve over the simplest qualified distribution? | Proper-score improvement with support, calibration, OOD and complexity guardrails | CANDIDATE — NOT STARTED |
| `CMP-ALL-CAL-v0` | Does shared-distribution calibration improve without breaking coherence? | Held-out proper score/reliability, sharpness and slice non-inferiority | CANDIDATE — NOT STARTED |
| `CMP-ALL-MARKET-v0` | RETIRED — market-only/hybrid prediction excluded | No active training or shadow comparison | RETIRED |
| `CMP-ALL-UNIVERSE-v0` | Does systematic event enumeration remove selected-sample distortion? | Frozen population coverage, missing-event audit and event-weighted scores | CANDIDATE — NOT STARTED |
| `CMP-ALL-FRESH-v0` | Do field-specific freshness triggers improve process without leakage? | Source-age/missingness audit and predeclared chronological ablation | CANDIDATE — NOT STARTED |




No comparison becomes `TESTING` until population, folds, builds, metrics, uncertainty, horizon and decision rule are frozen before outcomes.




## 8. Promotion rule




A build advances only when target, source, H0, feature and label cards are approved; candidates use identical point-in-time folds; integrity/leakage/support/coherence tests pass; the primary proper score improves with useful uncertainty; calibration/coverage/critical slices and rank guardrails are non-inferior; complexity/source failure behavior is acceptable; TEST is opened once; and immutable prospective E1-P shadow evidence supports publication.




Hit rate, a short winning run, attractive examples, external-model reputation, one backtest slice or ROI without complete price/stake records cannot promote a model.




## 9. Current model card




| Field | Current state |
|---|---|
| Published numerical model | NONE |
| Qualitative method | MDS-2026.09.19-v4.3 / CR-2026.09.21-3; unvalidated qualitative forecasts under current controls |
| H0 dependency | NOT BUILT / NOT QUALITY-APPROVED for every sport |
| Registered numerical candidates | DESIGN ONLY / DATA BLOCKED |
| Trained coefficients or priors | NONE |
| Calibrator | NONE |
| Untouched TEST result | NONE |
| E1-P shadow output | NONE |
| Probability publication | DISABLED |
| Market/value model | NOT ESTABLISHED |




Volatile queue state belongs only to the top controlling snapshot of the active log identified in README.




## September 5 user confirmation — controlling eligibility correction




[Controlling policy](PERFORMANCE_ELIGIBILITY_POLICY.md). The user confirmed: **all existing game logs except views explicitly labelled LIVE were strictly frozen pre-game**. Accept this as the provenance basis `USER_CONFIRMED_PREGAME_FREEZE`, effective September 5. Non-live issued cards are eligible for historical qualitative directional/ranking evaluation. A late local import alone no longer excludes them. This correction supersedes earlier blanket `E1-Q-LATE_IMPORT`, “all non-performance-eligible” and “zero eligible historical units” statements. It records user confirmation; it does not assert independent timestamp verification or change original file times.




Keep four distinct fields: **forecast horizon at issue**, **event state when checked for settlement**, **provenance basis**, and **endpoint settlement status**. An originally pre-game card found live during settlement stays pre-game and awaits a final; it does not become a live-issued forecast. A live source/page, a “live counter-branch”, or a post-issue status check is not an issuance label. Explicit live or live-state-unverified issued views stay outside pre-game metrics. Original pre-game and later live views of one event must retain their own ranks and share an event cluster.




The headline historical scorecard includes all identifiable, genuinely issued, settled contracts/ranks in its stated cohort, including `FORCED RANK`, LOW evidence, and `PROCESS_DEFECT` outcomes. Do not remove a bad pick because its reasoning was poor. Process grade is a diagnostic column and a separately labelled compliance slice. No-forecast/no-action records are not trials; unresolved/void/push/partial rows have explicit denominators; materially unidentifiable contracts remain unscorable with the reason recorded. A row’s missing operator terms may limit ticket settlement without erasing a clearly defined research endpoint. Never use an issue-time row already decided as a predictive success.




Use the exact original pre-game order, including the latest genuinely pre-game refresh; never substitute a later live or retrospective order. Deduplicate aliases and group related targets/views by underlying event. Report historical performance by issued method, sport/competition, horizon and target. The ten newly settled cards are an evaluated v3.4 pre-game cohort. Earlier historical scorecards need those same row/view joins before a new all-history aggregate is reported; the complete status index is not itself a performance denominator.




Old games may measure their issued methods and supply development evidence for improvements. They cannot validate a v3.5/v3.6 change designed after their outcomes were seen. Keep the historical ranking count separate from each frozen challenger’s later test count. No probabilities, fitted coefficients, calibration or market-edge claims are created by this provenance correction. Future snapshots/hashes and externally timestamped revisions are useful provenance records; a local hash or editable git timestamp alone is not an independent timestamp authority, and no git-only approval gate is imposed on this user-confirmed history.




## Implementation priority — 2026-09-17




BS-A0-EMP-COUNT-v0 and BS-A1-JOINT-RUN-v0 have executable probability primitives and complete estimation/data specifications in MODEL_IMPLEMENTATION_RECIPES; **NOT FIT**. Soccer A0/A1 have Poisson/Dixon-Coles grids and linked phase composition in the same reference; **NOT FIT**. Cricket resource/wicket state is specified there. All A3/A4 flexible models and learned rank/pair selectors are **DORMANT — BASELINE EVIDENCE REQUIRED**, overriding the generic candidate table's build ordering. A2 is deferred unless necessary for a correct endpoint. Tennis/union scopes are design-only additions. No calibrated, TESTED or SHADOW build exists. Publication requires S5 plus qualifying S6 evidence under NUMERICAL_PROGRAM.




<!-- DEEP-RESEARCH-IMPLEMENTATION-2026-09-19-V42 -->




## 2026-09-19 registration requirements for any future fitted model




No existing `NOT FIT` model status is promoted by this documentation change. A newly registered model must additionally declare:




- `market_independence = SPORTS_ONLY / MARKET_BLIND`;
- training dataset hash and point-in-time feature schema version;
- prohibited-source scan result and source-lineage manifest;
- chronological TRAIN/TUNE/CAL/TEST definition with event grouping;
- all fitted preprocessing/encoding/imputation scope;
- distribution family/support and how one frozen distribution answers multiple lines;
- calibration method and CAL-only fitting receipt;
- full-distribution proper scores plus target-specific scores, calibration, interval coverage and error by key data-quality/OOD slices;
- untouched TEST opening date and commit/hash; and
- prospective shadow status before any production promotion.




A model that requires market lines/odds, fantasy/DFS projections or betting-consensus features is **INELIGIBLE FOR THIS PROJECT**, regardless of predictive performance elsewhere.

<!-- REDUCED-FEATURE-BUILDS-2026-09-26C -->
## 2026-09-26(c) — reduced-feature A0/A1 builds for every sport

These builds implement the A0/A1 roles of the candidate groups above in reduced-feature form: final scores, dates and venue roles only. The candidate rows keep their designs for the full builds, which remain DATA BLOCKED. Every build here is **shadow only** and never a card input.

| Build | Implements | What it is | Status | Evidence |
|---|---|---|---|---|
| `SOC-A0/A1-RF-2026.09.26` | `SOC-A0-POIS-v0`; the attack/defence part of `SOC-A1-DC-BIVAR-v0` | League goal rates; time-decayed Gamma-pooled Poisson ratings with linked halves. Dixon–Coles tested as a separate candidate | **TESTED — NOT PROMOTED**; SHADOW (`C-SPORT-SHADOW`) | 5 leagues, 2022-23 to 2025-26: A1 better on results and margins everywhere; totals mixed; DC no gain |
| `IH-A0/A1-RF-2026.09.26` | `IH-A0-POIS-v0` and the regulation part of `IH-A1-JOINT-GOAL-v0` | Regulation Poisson ratings; OT won in proportion to scoring rates at the league's decided-in-OT rate; SO 0.5 | **TESTED — NOT PROMOTED** (NHL 2023–26); SHADOW | A1 better than A0 and TB-1 on results; regulation 3-way better; **totals worse** |
| `BB-A0/A1-RF-2026.09.26` | `BB-A0-EMP-POSS-v0` (without possessions) | Ridge offence/defence; discretised normal margin (no tie) and total; residual widths | **TESTED — NOT PROMOTED** (NBA 2013–15 and 2023–26; WNBA 2022–26); NBL not validated; SHADOW | A1 better than A0 and TB-1 on results and totals in every run |
| `AF-A0/A1-RF-2026.09.26` | `AF-A0-EMP-DRIVE-v0` (without drives) | As basketball, with the league's key-number weights | **TESTED — NOT PROMOTED** (NFL 2021–25); SHADOW | A1 better than A0 on results and margins; against TB-1 the interval crosses 0; totals no gain |
| `AFL-A0/A1-RF-2026.09.26` | `AFL-A0-EMP-SHOT-v0` (without shots) | As basketball, draws allowed | **TESTED — NOT PROMOTED** (2021–24); SHADOW | A1 better than A0 and TB-1 on results; at the total line TB-1 ahead by 0.008 (interval crosses 0) |
| `RL-A0/A1-RF-2026.09.26` | `RL-A0-EMP-SET-v0` (without sets) | As American football | CODE IMPLEMENTED — NOT VALIDATED; SHADOW | Synthetic only |
| `RU-A0/A1-RF-2026.09.26` | `RU-A0-EMP-SCORE-v0` | As American football; any ESPN path or CSV | CODE IMPLEMENTED — NOT VALIDATED; SHADOW | Synthetic only |
| `BS-A1-TEAM-v2` (MLB and NPB/KBO/CPBL) | Team + park + home core of `BS-A1-JOINT-RUN-v0` | Shared-gamma joint; team prior 120 games (v1: 20); competition tie rate kept where ties exist | **TUNED** (2022) then scored 2023–24 (not independent); SHADOW (`C-MLB-SHADOW`; Asian leagues via CSV) | v1 failed (overconfident); v2 better than A0, level with TB-1 on results |
| `TEN-A0/A1-RF-2026.09.26` | `TEN-A0-SERVE-RETURN-v0` (serve rate from Elo, not player serve stats) | Surface-blended Elo, then the exact point → match chain with a match-level gap effect (gap_sd 0.09; v1: 0) | **TUNED** (2021–22) then scored 2023–26 (not independent); SHADOW (from 2026-09-26(d)) | Winner: narrowly better than overall Elo; games: v1 worse than population, v2 level to slightly better |
| `CR-A0/A1-RF-2026.09.26` | `CR-A0-ECDF-COUNT-v0` (first innings only) | Elo result; ridge batting/bowling/venue first-innings total; target-censored second innings not modelled | **TUNED** (IPL 2016–19; elo_k 4, lam_team 200) then scored 2020–26 (not independent); SHADOW | v1 worse than a coin flip and the format mean; v2 level with both: **no demonstrated skill** |

Full tables, protocol and disclosures: `research/sport_models_2026-09-26/README.md`.
