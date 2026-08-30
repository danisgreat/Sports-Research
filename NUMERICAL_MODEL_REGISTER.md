# Numerical model register

Status: **ACTIVE DESIGN REGISTER — ALL NUMERICAL BUILDS NOT FIT**

Register version: **NMR-2026.08.25-v0.2**

Numerical training specification: **NTS-2026.08.25-v0.2**

Governing published forecast method: **MDS-2026.08.30-v2.7 — qualitative champion**

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
| M0 | Same-time de-vigged market-only benchmark |
| M1 | Explicitly market-informed hybrid using out-of-fold sports and market signals |

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
| `BS-A0-EMP-COUNT-v0` | Baseball joint runs | Empirical plus Poisson/NB diagnostic | Run-dispersion and simple baseline | DESIGN REGISTERED / DATA BLOCKED |
| `BS-A1-JOINT-RUN-v0` | Baseball joint runs | Hierarchical bivariate count/distributional model | Test lineup/starter/bullpen/park covariance | DESIGN REGISTERED / DATA BLOCKED |
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

For each sport/target group, instantiate `M0-MARKET-v0` and `M1-HYBRID-v0` only when exact same-time market snapshots and de-vig cards exist. They are not silently part of A0–A4.

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
| `CMP-ALL-MARKET-v0` | How do sport-only, market-only and hybrid lanes compare? | Identical event/cutoff scorecard; independent-signal and hybrid claims kept separate | CANDIDATE — NOT STARTED |
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
| Qualitative champion | MDS-2026.08.30-v2.7 |
| H0 dependency | NOT BUILT / NOT QUALITY-APPROVED for every sport |
| Registered numerical candidates | DESIGN ONLY / DATA BLOCKED |
| Trained coefficients or priors | NONE |
| Calibrator | NONE |
| Untouched TEST result | NONE |
| E1-P shadow output | NONE |
| Probability publication | DISABLED |
| Market/value model | NOT ESTABLISHED |

Volatile queue state belongs only to the top controlling snapshot of the active log identified in README.
