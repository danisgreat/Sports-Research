# Numerical training specification

Status: **ACTIVE DESIGN — TRAINING PHASE, STAGE 0 (PRE-FIT), NOT FINALISED**

Specification ID: **NTS-2026.08.25-v0.2**

Governing published forecast method: **MDS-2026.08.30-v2.7 — qualitative champion**

Effective: **2026-08-25**

Scope: cricket, basketball, American football, baseball including MLB/NPB/KBO, AFL/AFLW, rugby league, soccer, and ice hockey. Other sports require an explicit target/source/model card before numerical work.

This is a Markdown-only training specification. It authorises definitions, registries, candidate models, tests, and gates. It does **not** authorise or imply a downloaded dataset, runtime, notebook, fitted model, calibration object, generated probability, numerical champion, market edge, or staking system. The eventual label “MDS v3: Numerical Implementation” remains reserved until all applicable promotion gates pass.

## 1. Decision for multiple lines on one event

Train the underlying sporting target, not each bookmaker threshold.

For cricket, these are different random variables and must not share a label or model ID:

| Target ID | Exact outcome |
|---|---|
| `TEST_DAY_RUNS_FULL` | All runs scored by both teams during the named Test day |
| `TEST_DAY_RUNS_REMAINING` | Runs scored after a frozen live state until that Test day ends |
| `TEAM_FIRST_INNINGS_TOTAL` | The named team's eventual first-innings total, even if it continues on another day |
| `TEAM_INNINGS_RUNS_REMAINING` | Additional runs from a frozen innings state until its exact endpoint |

For an integer target `Y`, define `F(k) = P(Y <= k | X)`. One CDF gives every half-unit contract:

- `P(Over k.5) = 1 - F(k)`;
- `P(Under k.5) = F(k)`.

Therefore `P(O185.5) >= P(O235.5) >= P(O285.5)`, while Under probabilities have the reverse ordering. `O235.5` and `U235.5` are exact complements. `O185.5` and `U285.5` overlap: both win when `186 <= Y <= 285`, with joint probability `F(285) - F(185)`. Never multiply their marginals as if they were independent.

The same principle applies to basketball totals, football spreads, baseball run lines, AFL handicaps, NRL totals, soccer goal lines, and hockey puck lines. A real market request should supply the complete candidate slate, exact terms, operator, capture time, and both-side decimal odds where value is requested. Without odds, the output is a likelihood ranking only.

## 2. Governing principles

1. **Target before model.** Freeze target ID, unit, support, start state, endpoint, horizon, exposure, termination, censoring, and settlement rules.
2. **One distribution per exact target.** Produce a PMF/CDF, score grid, posterior predictive sample, or validated monotone quantile representation.
3. **Linked does not mean interchangeable.** Team score, phase, player, corner, shot, wicket, and other targets may share state/scenarios but retain separate labels and validation.
4. **Contracts are deterministic queries.** Moneylines, totals, spreads, handicaps, alternates, and milestones are integrations over the controlling target distribution.
5. **Event is the independent unit.** Several contracts from one event share an event/dependence group and do not inflate sample size.
6. **Forecast before price comparison.** Sports-only probability, market benchmark, hybrid forecast, likelihood rank, and value decision remain distinguishable.
7. **Chronology controls.** Every feature, transformation, fit, selection, calibration, and test is point-in-time and time ordered.
8. **No family wins by reputation.** Simple, distributional, flexible, and structural candidates compete on identical folds and proper scores.
9. **Calibration preserves coherence.** Independent line-by-line calibration cannot control production if it breaks complements, pushes, support, or nested ordering.
10. **Uncertainty is structural.** Participation, minutes/workload, weather, playable time, extra periods, declarations, substitutions, tactical state, and parameter uncertainty are propagated.

## 3. Target registry and event universe

Every target requires a versioned row before H0 construction.

| Required field | Definition |
|---|---|
| Target ID/version | Stable identifier; changed endpoint, rules or information horizon requires a new version |
| Sport/population | Competition, format, rules era, sex/category and exclusions |
| Forecast mode | Pregame, scheduled checkpoint, or exact live horizon |
| Outcome/unit/support | Runs, points, goals, margin, result state, player/event count, or another native outcome |
| Start state and cutoff | Exact prediction-time state and information boundary |
| Endpoint and exposure | Regulation/match/phase/innings end plus scheduled and uncertain opportunities |
| Termination/censoring | Weather, abandonment, declaration, all-out, chase, mercy rule, overtime, extra innings, void and push treatment |
| Label source/version | Official result/event source, provider definition and correction policy |
| Contract map | Exact W/P/L integration for every supported contract form |
| Evaluation population | Systematic eligible universe, chronological blocks, grouping, material slices and exclusions |

Numerical evaluation must enumerate **every eligible event** in a preregistered competition/date/rules population, subject only to frozen data-quality exclusions. User-requested or “interesting” events are a selected issuance sample and cannot establish population performance.

If alternate thresholds are evaluated, freeze the grid or threshold-selection policy before results. Prefer evaluating the continuous/discrete distribution directly. Do not add easy-looking alternates after seeing a forecast or outcome.

## 4. Distribution-first architecture and data grain

```text
prediction-time source snapshots
        -> canonical event, participant and state tables
        -> exact target/state row
        -> dynamic strength + exposure + matchup + context features
        -> sport-native outcome engine
        -> one predictive distribution per target
        -> coherence-preserving calibration
        -> deterministic contract integration
        -> marginal likelihood ranking
        -> optional same-time market/value layer
```

Canonical numerical grains:

1. one `event_id × state_snapshot_id × target_id × model_build_id` distribution row;
2. one linked `decision_set_id × candidate_id × contract_id` row per derived contract;
3. one separate `event_id × contract_id × operator × captured_at` market snapshot;
4. one official target label joined only after the feature/prediction snapshot is frozen.

Ten lines from one target are ten contract queries, not ten independent model-training observations. Player and niche targets use their own distribution rows, linked to the same event state where defensible.

## 5. Candidate probability-model ladder

All models are candidates. None is fitted, calibrated, validated, promoted, or authorised for published probabilities.

| Layer | Candidate family | Purpose | Required safeguard |
|---|---|---|---|
| A0 | Competition/venue prior, rating baseline, conditional empirical CDF or resampling | Transparent minimal-assumption comparator | Point-in-time pooling, decay, sparse-state and tail audit |
| A0 | Poisson or independent-count diagnostic where relevant | Simple auditable count benchmark | Test dispersion, dependence, scoring values, support and excess zeros; never assume fit |
| A1 | Hierarchical GLM, negative binomial, bivariate count, Dixon–Coles, GAMLSS/location-scale-shape | Interpretable conditional distribution | Frozen family/link/support; partial pooling and held-out tail/calibration checks |
| A1 | Truncated/discretised Normal or Student-t | Direct score/total benchmark | Remove invalid mass; test symmetry, covariance, discreteness and tails |
| A2 | Sport-specific state-transition or possession/event simulator | Coherent joint scores/resources, tails and termination | Validate every transition, exposure, scenario and endpoint; quantify simulation error |
| A3 | NGBoost or other distributional boosting | Nonlinear conditional distribution parameters | Supported family, enough H0, OOD and calibration safeguards |
| A4 | Ordered-bucket/monotone CDF or joint non-crossing quantiles | Flexible distribution shape | Frozen bins/interpolation/tails; no crossing; normalized support |
| M0 | Same-time de-vigged market-only probability | Strong external benchmark | Exact contract/time, overround and predeclared de-vig method |
| M1 | Calibrated market-informed hybrid | Test incremental sports signal and operational accuracy | Label market-informed; out-of-fold components and separate sport-only scorecard |

Hurdle/zero-inflated families require a separately defined structural-zero mechanism. Conformal intervals may test coverage but are not a complete conditional CDF and cannot alone generate line probabilities.

## 6. Sport-specific outcome engines

The universal contract is shared; the event engine is sport-native. No score scale or coefficient is pooled across unrelated sports.

| Sport | Primary event object | Structural A2 candidate | Mandatory target distinctions |
|---|---|---|---|
| Cricket | Runs/wickets/resources over legal-ball and playable-time exposure | Coupled ball/over simulator with batting order, bowling resources, pitch/weather/light, innings transitions, declaration, chase, DLS and match termination | Format; full day vs remaining day; innings total vs remaining innings; phase; match win/draw/loss |
| Basketball | Joint team-score distribution | Possession/lineup-stint simulator for pace, shot/FT/turnover/rebound outcomes, foul state, late fouling, blowout and overtime | League clock/rules; regulation vs OT; quarter/half/full; player minutes/usage targets |
| American football | Discrete joint team-score distribution | Drive/play simulator using field position, QB/regime, plays, TD/FG/safety/no-score/turnovers, tries, clock/script and competition OT | NFL/NCAA/UFL/CFL rules; phase; listed player/action; player snap/route/carry targets |
| Baseball | Joint team-run distribution | PA/base-out simulator with lineup, starter hook, bullpen chain, park/weather, home ninth and extra innings | MLB/NPB/KBO populations; listed pitcher/action; regulation vs extras; pitcher/batter props |
| AFL/AFLW | Joint goals/behinds/score and margin distribution | Territory -> inside-50 -> scoring-shot quality -> goal/behind process with roles, conversion, tempo and separation | AFL vs AFLW; quarter/half/full; draw/overtime/finals terms; player role/time-on-ground targets |
| Rugby league | Joint discrete score/margin distribution | Set/field-position simulator for completion, goal-line entry, try, conversion, penalty/field goal, fatigue, sin-bin and golden point | NRL/NRLW/Super League; regulation/golden point; player minutes/position/kicking targets |
| Soccer | Regulation joint goal grid and result state | Dynamic attack/defence shot/goal process with lineups, score state, red cards and stoppage | Regulation 1X2 vs qualify/advance; extra time/penalties; goals vs corners/cards/player events |
| Ice hockey | Regulation joint goal distribution plus match-result state | Shift/shot/xG/manpower/goalie simulator with special teams, score state, pulled goalie, OT and shootout | Regulation result vs moneyline incl. OT/SO; period/full; goalie/action terms; player shot/point targets |

### Cricket structural detail

The Test engine samples playable exposure, then estimates a coupled `P(runs, wicket, extras | state)` transition. The state includes innings, score, wickets, lead/trail, day/session, ball age, participants, bowling resources, pitch/weather/light and declaration/chase incentives. It updates the state and applies explicit hazards for all-out, declaration, innings switch, stumps, interruption, abandonment and match completion. `TEST_DAY_RUNS_FULL` may cross innings/team boundaries; `TEAM_FIRST_INNINGS_TOTAL` stops at the named innings endpoint. Those targets never share a label.

## 7. Player and niche-event targets

Player and niche contracts are connected to the team/game state but are not direct queries of team score unless the generative model explicitly contains that event.

Use a target-native decomposition such as:

- basketball points: `active/start scenario × minutes × possessions × usage × scoring efficiency`;
- football receiving: `active × snaps/routes × target rate × catch/yards process`;
- baseball strikeouts: `starter action × batters faced × strikeout rate`;
- soccer SOT: `start/minutes × shots per minute × role/box share × on-target conversion`;
- cricket batter runs: balls faced jointly with dismissal hazard × runs per legal ball;
- hockey shots/points: lineup/ice time × shot or point-event intensity × manpower/score state;
- corners/cards: their own event exposure/rate/provider definition, not goal or possession as a substitute.

Uncertain participation is a scenario mixture, not a silent full-workload assumption. Exact provider/statistic definitions and action/void terms are target gates.

## 8. Prediction-time web research versus training data

Web research supplies current point-in-time inputs; it does not create a trained model on demand.

Field ownership:

1. official governing/league/team/match/venue sources for identities, rules, lineups, state and finals;
2. government weather for its forecast/observation;
3. official data partners and specialist sources for their defined historical or derived metrics;
4. reputable named reporting for material news not yet official;
5. the actual operator/exchange for exact contract, terms and price;
6. aggregators/query engines for discovery or cross-checking only.

Every decisive field stores effective, first-known/published, observed, retrieved and cutoff times. A current web page may inform an issued forecast only if first known by cutoff. A source may enter H0 only after DATA_SOURCE_REGISTER.md approves the exact field, coverage, access method, licence/use, revisions, definition and snapshot behavior. “Publicly visible” does not mean unrestricted scraping or training use.

Acquisition order is volatile facts -> process history -> matchup/context -> contrary-path check -> final volatile refresh. Stop when every material field is verified or explicitly missing/conflicting and more searching is unlikely to change the decision before the refresh deadline.

## 9. Market lanes and value layer

Maintain three comparable lanes:

| Lane | Market input | Permitted claim |
|---|---|---|
| `SPORT_ONLY / MARKET_BLIND` | None | Independent sports-feature forecast quality |
| `MARKET_ONLY_BASELINE` | Same-time de-vigged price | Strength of the market benchmark |
| `MARKET_INFORMED` | Same-time market plus sport features | Hybrid forecast quality, explicitly labelled |

Capture the market even when it is not a sports-model feature: exact event/contract, operator, line, both-side odds, terms and `captured_at`. Never insert a later closing price into an earlier forecast. Raw reciprocal odds include overround; basic normalization, Shin or another de-vig method must be preregistered and compared rather than chosen after results.

Likelihood and value are different. `VALUE SUPPORTED` additionally requires a published calibrated W/P/L distribution, exact same-time price, de-vig and push/refund return arithmetic, uncertainty margin and a frozen decision threshold. ROI requires valid odds, stakes, terms and costs. Staking remains disabled.

## 10. Training chronology and stages

Random event, play, delivery, candidate or contract-row splits are prohibited. Every row/view from one event remains in one block; series/round/date blocking is added where dependence warrants it.

`TRAIN -> TUNE -> CAL -> untouched TEST -> prospective E1-P shadow`

| Stage | Required deliverable | Current state |
|---|---|---|
| S0 | Markdown targets, source register, H0 cards, model register, metrics, guide and gates | **ACTIVE — this specification** |
| S1 | Field-level source audits and immutable point-in-time snapshots for one frozen pilot target | NOT STARTED |
| S2 | Systematically enumerated H0 with identity, label, join, leakage and quality tests | NOT BUILT |
| S3 | A0 and interpretable A1 baselines on frozen chronological folds | NOT FIT |
| S4 | Sport-specific A2 simulator with transition, termination and simulation tests | NOT FIT |
| S5 | A3/A4 flexible challengers and M0/M1 market comparisons | NOT FIT |
| S6 | Disjoint calibration and one-time untouched TEST | NOT STARTED |
| S7 | Immutable pre-result E1-P shadow run | NOT STARTED |
| S8 | Versioned publication decision | DISABLED |

Every imputer, encoder, scaler, rating, decay, feature selector, distribution choice, calibrator, de-vig transform, stacker and ensemble weight is fitted only inside its permitted earlier block. A viewed TEST block is spent.

## 11. Calibration, coherence and evaluation

Prefer calibration of the complete CDF/score grid or a shared monotone transformation. If threshold calibration is studied, reconcile it through a preregistered coherence method and re-score the final distribution.

Required integrity checks:

- PMF mass is finite, non-negative and sums to one; CDF/ordered buckets never decrease and obey support;
- exact complements, integer push mass and W/P/L normalization hold;
- Over probabilities never rise with the line; Under probabilities never fall;
- every contract integration reproduces the stored distribution exactly;
- related winner/total/margin outputs reconcile with the same joint score/resource object;
- pregame/live and regulation/full-result targets have distinct IDs;
- simulation seed, draws, Monte Carlo error and convergence exist;
- calibrator data follows model fitting and precedes untouched TEST.

Primary evaluation:

| Output | Primary measures |
|---|---|
| Full univariate CDF/PMF | CRPS or ranked probability score; log score; PIT/randomized ranks; interval coverage and width |
| Winner/result vector | Brier and log score; calibration/reliability with uncertainty |
| Joint score/resource | Marginal distribution scores plus a dependence-sensitive score when support permits |
| Derived W/P/L contracts | Binary/multiclass Brier and log score at frozen thresholds; complement/nesting checks |
| Point summaries | Bias, MAE and RMSE as secondary diagnostics |
| Ranking | Rank-1, Wins@2, NDCG and oracle/candidate-availability diagnostics at event/decision-set grain |
| Market comparison | Sport-only, market-only and hybrid scores on identical cutoffs; ROI only with valid recorded economics |

Report event- or schedule-block-clustered uncertainty and slices by sport, competition/rules era, target, pregame/live horizon, participant/exposure regime, source/version, weather/context, probability band and OOD state. No sparse slice publishes merely because an aggregate passes.

## 12. Numerical output and publication contract

A genuine frozen run eventually stores:

```text
TARGET
target_id/version; state/cutoff; endpoint; unit/support; H0/feature/model/calibrator builds

UNDERLYING DISTRIBUTION
PMF/CDF/score-grid/posterior-sample reference; mean/median/quantiles if authorised;
scenario and parameter uncertainty; support; OOD/drift state

DERIVED CONTRACTS
contract ID; exact W/P/L geometry; raw/calibrated P(W/P/L);
distribution reference; complement/monotonicity checks; dependence group

MARKET, ONLY WHEN CAPTURED
operator; exact contract/line; both-side odds; captured_at; terms; de-vig method;
market lane; model-market comparison; uncertainty; value state

PUBLICATION
NOT_GENERATED / SHADOW / GENERATED_VALIDATED
NOT PUBLISHED / PUBLISHED / SUPPRESSED
```

Until a model actually runs, use `NOT_GENERATED`. An unvalidated run may freeze `SHADOW — NOT PUBLISHED`. A validated build still becomes `SUPPRESSED` when source version, OOD, drift, missingness or calibration gates fail. The user-facing fallback is the MDS v2.3 qualitative corridor, not an invented number.

## 13. Current truth table

| Item | Honest current state |
|---|---|
| Live forecasting method | MDS-2026.08.30-v2.7 qualitative champion |
| Numerical program | NTS-2026.08.25-v0.2, Stage 0 all-sports design/pre-fit |
| H0 | NOT BUILT / NOT QUALITY-APPROVED for every sport |
| Numerical models | CANDIDATE SPECIFICATIONS ONLY; NOT FIT / NOT VALIDATED |
| Calibrator | NOT FIT |
| E1-P | NOT STARTED |
| Published probabilities | DISABLED |
| Market edge / profitability | NOT ESTABLISHED / NOT MEASURABLE |
| Runtime or data files created by this update | NONE |

## 14. Version history

| Version | Change |
|---|---|
| NTS-2026.08.25-v0.1 | Cricket-first distribution design, target/threshold separation and initial source/H0/model registries |
| NTS-2026.08.25-v0.2 | Generalised the Stage-0 design to eight sport modules; added target families, systematic event universes, player/niche targets, prediction-time web-source governance, market-blind/market-only/hybrid lanes, and universal evaluation gates; no data or model was created |

## 15. Research basis

General probability and evaluation:

- [Strictly Proper Scoring Rules, Prediction, and Estimation — Gneiting and Raftery](https://doi.org/10.1198/016214506000001437)
- [Probabilistic Forecasts, Calibration and Sharpness — Gneiting, Balabdaoui and Raftery](https://doi.org/10.1111/j.1467-9868.2007.00587.x)
- [Rolling-origin time-series cross-validation — Forecasting: Principles and Practice](https://otexts.com/fpp3/tscv.html)
- [scikit-learn probability calibration](https://scikit-learn.org/stable/modules/calibration.html)
- [GAMLSS — Rigby and Stasinopoulos](https://doi.org/10.1111/j.1467-9876.2005.00510.x)
- [NGBoost — Duan et al.](https://proceedings.mlr.press/v119/duan20a.html)
- [Noncrossing quantile regression — Bondell, Reich and Wang](https://doi.org/10.1093/biomet/asq048)
- [On determining probability forecasts from betting odds — Štrumbelj](https://doi.org/10.1016/j.ijforecast.2014.02.008)

Sport engines and data-definition candidates:

- [Cricsheet official formats](https://cricsheet.org/format/) and [JSON specification](https://cricsheet.org/format/json/)
- [NBA official statistics glossary](https://www.nba.com/stats/help/glossary)
- [nflverse documentation](https://nflverse.nflverse.com/)
- [MLB Statcast glossary](https://www.mlb.com/glossary/statcast)
- [Dixon and Coles football score model](https://doi.org/10.1111/1467-9876.00065)
- [StatsBomb Open Data](https://github.com/statsbomb/open-data) — selective competitions and attribution/use conditions apply
- [AFL official statistics glossary](https://www.afl.com.au/news/144837/stats-glossary-every-stat-explained)
- [NRL official team-list source lane](https://www.nrl.com/news/topic/team-lists/)
- [NHL official statistics/glossary](https://www.nhl.com/info/hockey-glossary)
- [MoneyPuck data and use conditions](https://www.moneypuck.com/data.htm) — candidate non-commercial/download lane; its listed shot dataset omits blocked shots

These sources justify candidates, definitions and safeguards. They do not prove that a source is approved for H0, that a candidate is calibrated, or that any model transfers to a requested event.
