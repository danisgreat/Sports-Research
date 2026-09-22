# Sports Development Model Catalog v1

Effective: 2026-07-16  
Status: **DEVELOPMENT MODEL-CARD CATALOG — NOT FITTED OR ACTIVE**  
Operational status: **SUSPENDED — NO ACTIVE MODELS**  
Owner: Unassigned  
Approver: None

## 1. What this catalog is

This document instantiates the universal requirements in `SPORTS_MODEL_VALIDATION_AND_SIMULATION_FRAMEWORK_v3.md` as sport-specific DEVELOPMENT model cards. It is a design and implementation contract, not a fitted model, backtest, probability source or performance claim.

Every card below has version `0.1.0`, status `DEVELOPMENT`, no approved source map, no frozen data manifest, no fitted artifact, no calibration evidence, no untouched-test report and no prospective-shadow report. Therefore none can produce an authorized probability or recommendation. `SPORTS_MODEL_COVERAGE_REGISTRY_v3.csv` remains the final operational allowlist.

The cards deliberately separate sports, competitions, markets, forecast states and rules. A future fitted implementation must replace each broad development scope with exact non-wildcard coverage rows. Men’s, women’s, youth, domestic, international, shortened-format and changed-rule competitions are separate evaluation strata unless a preregistered hierarchical transfer test passes.

## 2. Shared model architecture

All cards use the same nine-layer contract while retaining sport-native likelihoods.

### 2.1 Point-in-time eligibility

An event enters a training or forecast dataset only when identity, competition, rules, venue, scheduled start, target branches and settlement convention resolve. Every feature carries `known_at_utc`, `fetched_at_utc`, `data_through`, definition/version, source observation IDs and a raw artifact hash. Production-like latency and missingness must be replayed historically.

### 2.2 Dynamic participant strength

For participant or unit `j` at event time `t`, latent attack, defence, pace and other sport-specific abilities use a partially pooled state model such as:

`theta[j,t] = mu[group,t] + rho * (theta[j,t-1] - mu[group,t-1]) + epsilon[j,t]`

where `epsilon` is a declared evolution distribution. Identifiability constraints, promotion/relegation priors, expansion teams, transfers, coaching changes and offseason evolution are fixed during tuning. Rating updates use only prior events available at the forecast cutoff.

### 2.3 Participation and exposure scenarios

Projected availability is a probability mixture over explicit lineup, role and exposure scenarios. Confirmed lineups collapse only the resolved dimensions. Player props require a separately validated minutes/overs/balls/possessions/snaps/shifts/attempts exposure model. A missing material participant or role distribution is never replaced by an analyst’s single guess.

### 2.4 Context layer

Venue, home/neutral status, rest, travel, surface, weather/roof, rules, officiating, competition strength and schedule congestion enter only with stable definitions and point-in-time availability. Context effects use shrinkage and interactions declared before untouched testing.

### 2.5 Sport-native event engine

Each module generates the smallest coherent primitive events—scoring events, possessions, balls, points, plate appearances, drives, rallies, holes, laps or round hazards—and derives all related market branches from one joint distribution. Opposing lines and overlapping markets never receive independently fitted probabilities that can contradict each other.

### 2.6 Distribution and structural uncertainty

Candidate distributions and structural challengers are chosen by rolling-origin tuning. Ensemble weights, if used, freeze before calibration and untouched testing. The operative forecast integrates parameter draws, participation/context scenarios and supported structural alternatives:

`P(Y) = sum_m sum_s w_model[m] * w_scenario[s] * integral P(Y | theta, s, m) dP(theta | D_cutoff)`.

Model disagreement is not silently averaged away; it is retained as a typed uncertainty component and can force PASS.

### 2.7 Calibration and branch reconciliation

Raw joint distributions are mapped to mutually exclusive settlement states first. Calibration is then fitted on a later disjoint calibration period at the exact sport/competition/market/state/horizon scope, using a multiclass or coherent marginal method that preserves branch sums. All branches must sum to one within `1e-9`; non-structural exact zero or one is prohibited.

### 2.8 Decision and abstention

The model generates distributions; a separately versioned policy selects at most one primary candidate for the user’s primary question. Missing contract, stale source, unsupported scope, unresolved exposure, out-of-distribution state, material scenario sensitivity, invalid probability, absent price packet or failed uncertainty guardrail produces WATCH/PASS. DEVELOPMENT cards always produce `PASS / MODEL_UNAVAILABLE`.

### 2.9 Evaluation

Train, tune, calibrate, untouched test and prospective shadow are chronological and disjoint. Comparisons use the same events, branches and weights as the frozen baseline. Probability distributions report Brier and log loss; count/continuous distributions add a proper distribution score, interval coverage and tail diagnostics. Inference clusters by event and any residual participant/time/competition block. Candidate selection is replayed from the complete frozen universe.

## 3. Shared artifact and activation contract

Every future fitted card must populate all fields in the canonical model-card template, including immutable hashes for data, features, code, model, calibration, event manifests and selection policy. Before first untouched-test view it must also freeze:

- exactly one primary promotion metric;
- a credible naive baseline and, when authorized, a contemporaneous no-vig market comparator;
- a minimum practically relevant improvement;
- an effective-N or precision requirement;
- calibration, interval, tail, missingness and protected-segment guardrails;
- numeric drift warning/suspension windows;
- a later prospective-shadow rule.

Those numeric rules are intentionally `UNSET` in version `0.1.0`. Choosing them after viewing test results would invalidate the test.

## 4. Australian football model card

**Model ID:** `DEV_AFL_SCORE_V0`  
**Scope:** Australian football; AFL and AFLW must be fitted separately; pregame winner, line, margin, total and team total. Phase and player markets require later subcards.  
**Target engine:** A hierarchical marked scoring-event model. Team territory/pace generates scoring opportunities; each opportunity is marked goal, behind or no score with opponent- and venue-adjusted conversion. A shared match-tempo latent variable creates home/away dependence. Final score is derived as `6 * goals + behinds`, and margin/total/winner branches come from the same joint simulation. Direct bivariate negative-binomial score components and empirical residual mixtures are tuning challengers, not automatic defaults.  
**Baseline:** Dynamic team score-for/against and venue baseline with recency chosen only in tuning.  
**Required features:** Final or scenario-weighted team; player availability and role; team/opponent territory, inside-50, pressure, intercept/clearance and scoring-efficiency definitions from a stable provider; venue geometry; rest/travel; weather and roof; competition/rule regime; opponent strength.  
**Live state:** Quarter, official clock mode, score, remaining exposure, possession/field zone if supported, personnel/substitutions, reportable injuries and exceptional delays. Pregame and live models are separate.  
**Diagnostics:** Goal/behind calibration, score covariance, close-game and large-margin tails, quarter aggregation, venue and weather segments, AFL/AFLW separation.  
**Hard exclusions:** Unverified team sheet, incompatible provider definitions, missing weather when material, state-league transfer without validation, player props without exposure submodel.

## 5. Rugby league model card

**Model ID:** `DEV_RUGBY_LEAGUE_SCORE_V0`  
**Scope:** NRL, NRLW and other leagues separately; pregame winner, line, margin, total and team total.  
**Target engine:** A compound possession-set model. Possessions transition through field position, tackle count, restart and turnover states; terminal events include try, penalty goal, one-point field goal, competition-authorized two-point field goal and no score. Conversions are conditional on try location and kicker. Score is reconstructed from the exact competition scoring rules, including rare exceptional branches rather than approximating total points with a single Poisson.  
**Baseline:** Dynamic points-for/against plus home/neutral and opponent adjustment.  
**Required features:** Final 17 and positional roles, interchange/bench usage scenarios, injuries/HIA availability, possession and completion rates, run metres/field position, tackle efficiency, errors, penalties, set restarts, kicking and goal-kicking, pace, rest/travel, venue/weather, referee definition where stable.  
**Live state:** Half, clock, score, tackle count, field position, possession, sin-bin/send-off/HIA/interchange state and remaining time.  
**Diagnostics:** Try-versus-kick composition, conversion calibration, possession count, card/HIA scenarios, large-margin tails, NRL/NRLW and rule-era segments.  
**Hard exclusions:** Final-team gate unresolved, league rules mixed, generic rugby-union features substituted, undocumented player-position changes.

## 6. Rugby union model card

**Model ID:** `DEV_RUGBY_UNION_SCORE_V0`  
**Scope:** Fifteens only in this card; international and each club competition separate; pregame winner, line, margin, total and team total. Sevens, tens, youth and community variations require different cards.  
**Target engine:** A hierarchical possession/phase model with field-position transitions and competing terminal hazards for try, penalty goal, drop goal, penalty try, turnover and no score. Conversions depend on try location and kicker. The scoring identity is `5*T + 2*C + 3*PG + 3*DG + 7*PT`, subject to the exact event regulations. Cards, replacement rules, uncontested scrums and competition law trials are explicit scenarios.  
**Baseline:** Dynamic competition-adjusted points-for/against plus venue and World Rugby rating only where its effective definition is frozen.  
**Required features:** Final XV and bench, positions and replacements, availability/HIA, possession/territory, carries and gain line, ruck speed, turnovers, penalties, scrum/lineout performance, kicking and goal-kicking, referee, rest/travel, venue/weather, competition and effective law variation.  
**Live state:** Half, clock, score, possession/territory, card and replacement clocks, scrum/lineout status where material, penalty advantage and remaining exposure.  
**Diagnostics:** Scoring-mode composition, card and referee segments, home/neutral tests, competition transfer, close-game/drop-goal tails and law-era drift.  
**Hard exclusions:** Rugby league pooled into union, sevens pooled into fifteens, law trial/effective date unresolved, incomplete card/replacement state for live forecasts.

## 7. Cricket model card

**Model ID:** `DEV_CRICKET_BALL_STATE_V0`  
**Scope:** T20, ODI, Test and other formats require distinct fitted cards; innings, phase, team total and winner markets. Player props require role/exposure subcards.  
**Target engine:** A legal-delivery state model over innings, over/ball, striker/non-striker, bowler, wickets, score, target, resources and fielding restrictions. Each delivery jointly models runs off bat, extras, wicket type, legal-delivery status and strike transition. Bowler allocation and batting order are scenario distributions. Chases use target/resource-dependent strategy; rain and DLS are explicit competing truncation/revision branches.  
**Baseline:** Format, venue, innings and phase empirical rate/wicket baseline with team-strength shrinkage.  
**Required features:** Toss, confirmed or scenario-weighted XI, batting position, bowling allocation, handedness/style matchups, recent opportunity-adjusted ability, venue/boundary, pitch evidence with access status, weather/dew, format and playing conditions.  
**Live state:** Innings, legal balls/overs, score, wickets, target, striker, non-striker, current/remaining bowlers where known, powerplay/field restrictions, DLS resource/target, interruptions.  
**Diagnostics:** Run and wicket calibration by phase, extras, zero/six tails, batter/bowler exposure, chase/truncation, venue/format transfer, innings-total tail coverage.  
**Hard exclusions:** Formats pooled without hierarchy validation, toss/XI invented, DLS state missing, pitch description treated as quantified without a registered encoding.

## 8. Soccer score model card

**Model ID:** `DEV_SOCCER_SCORE_V0`  
**Scope:** Competition-specific regulation-time goals, result, handicap, total and team total; advancement, extra time and shootout require explicit connected submodels.  
**Target engine:** Dynamic hierarchical attack/defence goal rates with a bivariate Poisson or Dixon-Coles low-score dependence correction selected on rolling-origin tuning. Red-card, lineup and tactical scenarios alter rates; an optional event-hazard challenger handles live forecasts. Regulation, extra time, shootout and aggregate-leg state are separate branches.  
**Baseline:** Independent attack/defence Poisson with home/neutral and competition intercepts.  
**Required features:** Official or scenario XI, positions/minutes, goalkeeper and striker availability, rest/travel, venue/surface/weather, opponent strength, stable-provider shot/xG components, game importance only through preregistered definitions, competition substitution and advancement rules.  
**Live state:** Period, official clock convention, score, red/yellow cards, substitutions, aggregate score/away-goal rule status, possession/territory or event state if supported, remaining stoppage/extra-time structure.  
**Diagnostics:** Scoreline matrix, nil frequency, draws, low-score dependence, red-card segments, totals/handicap coherence, competition and season drift.  
**Hard exclusions:** Different xG providers spliced, projected XI called confirmed, regulation and qualification settlement mixed.

## 9. Soccer counts and player model card

**Model ID:** `DEV_SOCCER_COUNTS_V0`  
**Scope:** Corners, cards, shots and player event counts only when provider definitions and exposure are stable.  
**Target engine:** Opportunity/exposure model followed by negative-binomial, hurdle or marked-event count likelihood. Team/opponent counts share match pace and game-state latents; cards include referee and score-state components. Player counts integrate start probability, minutes, position/role and team-event allocation.  
**Baseline:** Competition/team empirical count rates with minutes or possession exposure.  
**Required features:** Everything required by the score card plus exact provider metric definition, lineup/role/minutes scenarios, set-piece responsibility, referee for cards, opponent style and match state.  
**Diagnostics:** Dispersion, zeros, count covariance, minutes calibration, provider-version stability and player role changes.  
**Hard exclusions:** Undefined “shot” or “card” semantics, missing minutes model, combining team totals and player shares as independent evidence.

## 10. Basketball model card

**Model ID:** `DEV_BASKETBALL_POSSESSION_V0`  
**Scope:** NBA, WNBA, FIBA, domestic and Summer League separately; winner, spread, margin, total, team total and phase. Player props require minutes/usage validation.  
**Target engine:** Joint possession-count and possession-outcome model. Pace generates regulation possessions; offensive efficiency decomposes shot location/value, make probability, free throws, turnovers and offensive rebounds, conditioned on opponent and lineup. Late fouling, garbage-time mixtures and overtime are explicit state branches.  
**Baseline:** Possessions multiplied by adjusted offensive/defensive efficiency.  
**Required features:** Confirmed or scenario lineups, injuries/rest, projected minutes and rotations, on/off or regularized player effects, shooting profile, turnovers, rebounds, free-throw rate, pace, travel/altitude, venue, competition rules and officiating where stable.  
**Live state:** Period, clock, score, possession, team fouls/bonus, timeouts, player fouls/ejections, lineup on court and overtime rules.  
**Diagnostics:** Pace/efficiency calibration, score covariance, overtime and late-fouling tails, lineup/minutes error, competition/rule transfer.  
**Hard exclusions:** Summer League pooled with regular NBA, missing star-player exposure scenario, player prop without minutes and opportunity model.

## 11. Baseball model card

**Model ID:** `DEV_BASEBALL_PA_V0`  
**Scope:** MLB, NPB, KBO and other leagues separately; full game, first five, inning, NRFI, winner, run line and totals.  
**Target engine:** Plate-appearance/base-out Markov simulation with batter-pitcher-handedness effects, starter times-through-order and pitch-count removal, bullpen availability/selection, park/defence and rule-specific extra innings. Outcomes include out type, walk/HBP, singles through home runs, errors and advancement; runs emerge from state transitions.  
**Baseline:** Team/league run environment with park and starter adjustment.  
**Required features:** Confirmed lineup, announced starter, projected starter exposure, bullpen workload/availability, batter/pitcher skill, handedness, park, defence/catcher, weather/roof, league rules and doubleheader/suspension state.  
**Live state:** Inning/half, outs, bases, score, count, current pitcher/batter, bullpen exposure and extra-inning runner rules.  
**Diagnostics:** Run distribution/zero inflation, inning dependence, starter removal, bullpen tails, park/weather, league transfer and extra innings.  
**Hard exclusions:** F5/full-game sharing one target, unconfirmed starter treated as certain, suspended-game state missing.

## 12. Ice hockey model card

**Model ID:** `DEV_ICE_HOCKEY_STATE_V0`  
**Scope:** NHL and each international/other competition separately; regulation result, winner, puck line and totals.  
**Target engine:** Dynamic goal/event hazard with shared pace, expected-goal opportunity process, goaltender effects, manpower state and score-dependent empty-net strategy. Regulation, overtime and shootout are separate connected modules. Negative-binomial/bivariate count models are baselines or challengers depending on holdout diagnostics.  
**Baseline:** Regulation team attack/defence Poisson with home and goalie adjustment.  
**Required features:** Confirmed/projected goalie, lines/pairs, injuries, rest/travel, shot/xG definition, special teams, venue, rule set and likely empty-net policy.  
**Live state:** Period, clock, score, manpower/penalty clocks, goalie-pulled state, possession/zone/event state where supported, overtime/shootout structure.  
**Diagnostics:** Regulation score matrix, special-team and empty-net tails, goalie scenario error, OT/shootout separation and provider xG stability.  
**Hard exclusions:** Regulation and moneyline settlement conflated, projected goalie called confirmed, incompatible xG providers pooled.

## 13. American football model card

**Model ID:** `DEV_AMERICAN_FOOTBALL_DRIVE_V0`  
**Scope:** NFL and college separately; winner, spread, margin, total, team total and phase.  
**Target engine:** Drive/play-state simulation over clock, field position, down, distance, possession, score and timeouts. Drive terminals include touchdown/extra-point choice, field goal, safety, turnover, punt and end of half; pace and play selection respond to state. Overtime and competition rules are explicit.  
**Baseline:** Team drive efficiency and points-per-drive adjusted for opponent and venue.  
**Required features:** QB and offensive-line availability, skill-player/defence roles, EPA/success-rate definitions, pace/pass rate, pressure/coverage, special teams, rest/travel, venue/weather/roof, coaching and exact rules.  
**Live state:** Quarter, clock, score, possession, field position, down/distance, timeouts, challenges, key injuries/ejections and overtime state.  
**Diagnostics:** Drive-count and scoring-mode calibration, explosive-play tails, kneel/end-game states, weather, QB scenarios and college/NFL separation.  
**Hard exclusions:** College pooled with NFL, unresolved QB, generic clock state for live use.

## 14. Tennis model card

**Model ID:** `DEV_TENNIS_POINT_V0`  
**Scope:** Tour, surface, sex and format-specific match winner, set, game, handicap and total.  
**Target engine:** Server/returner point-probability state model propagated exactly through game, tiebreak, set and match rules. Ability evolves by surface and opponent; fatigue and injury/retirement are explicit scenarios, not inferred from a completed result.  
**Baseline:** Surface-adjusted serve/return points won with hierarchical shrinkage.  
**Required features:** Official draw/order, surface, format, serve/return history, handedness, rest/travel, verified fitness/retirement evidence, weather/roof and exact tiebreak/retirement settlement.  
**Live state:** Set/game/point score, server, tiebreak state, medical timeout and retirement status.  
**Diagnostics:** Point-to-match coherence, tiebreaks, long-match tails, surface and tour segments, retirement handling.  
**Hard exclusions:** Entry treated as fitness proof, different retirement rules mixed, best-of-three/five pooled without structure.

## 15. Volleyball model card

**Model ID:** `DEV_VOLLEYBALL_RALLY_V0`  
**Scope:** Competition- and format-specific match, set, point, handicap and total.  
**Target engine:** Rotation-aware rally model with serving team, rotation, lineup and side-out/break-point probabilities, propagated through win-by-two set and match rules. Fifth-set or deciding-set rules are explicit.  
**Baseline:** Team side-out and break-point rates with venue/competition shrinkage.  
**Required features:** Final roster/lineup, setter/opposite/libero availability, rotations, serve/receive/block efficiency definitions, rest/travel, venue and exact set format.  
**Live state:** Set, set score, rally score, serving team, rotation/substitutions, challenge state and deciding-set rules.  
**Diagnostics:** Rally/set/match coherence, deuce tails, rotation effects, competition transfer and lineup error.  
**Hard exclusions:** Beach and indoor pooled, formats/rally scoring mixed, missing server/rotation for live forecasts.

## 16. Golf model card

**Model ID:** `DEV_GOLF_HOLE_V0`  
**Scope:** Tour and course-specific winner, placement, matchup, round and hole markets.  
**Target engine:** Hierarchical hole-score distribution conditioned on player skill components, course/hole, tee-time wave and weather. Round/tournament totals preserve player and wave dependence. Cut, withdrawal/disqualification and playoff rules are explicit branches; coherent rank probabilities derive from joint tournament simulation.  
**Baseline:** Player scoring average adjusted for field strength and course.  
**Required features:** Official field, withdrawals, tee times, course/hole setup, strokes-gained definitions, recent rounds with shrinkage, weather by wave and tournament/cut rules.  
**Live state:** Round/hole, strokes, lie/status where supported, remaining holes, cut/playoff and suspension state.  
**Diagnostics:** Hole/round tails, rank coherence, wave/weather, cut and withdrawal calibration.  
**Hard exclusions:** Field not final, withdrawn players treated as ordinary losses, rankings independently normalized after simulation.

## 17. Motorsport model card

**Model ID:** `DEV_MOTORSPORT_RACE_V0`  
**Scope:** Series-, circuit- and session-specific winner, podium, placement, matchup and finish markets.  
**Target engine:** Joint latent pace and race-time model with grid/start, tyre/stint and pit strategy scenarios plus competing mechanical/crash hazard. Safety car, red flag, weather and series classification rules change remaining exposure. Finishing ranks derive from coherent simulated race outcomes, never independent driver probabilities.  
**Baseline:** Qualifying/grid and recent pace with circuit and constructor shrinkage.  
**Required features:** Confirmed entry/grid, penalties, car/team state, practice/qualifying with session conditions, tyre allocation, circuit/overtaking, pit loss, weather and exact classification/DNF rules.  
**Live state:** Lap, running order/gaps, tyre/stint/pit state, flags/safety car/red flag, weather and classified runners.  
**Diagnostics:** Pace residuals, DNF/censoring, rank coherence, safety-car and wet/dry scenarios, series transfer.  
**Hard exclusions:** Different series pooled without hierarchy validation, grid penalties unresolved, DNF settlement ambiguous.

## 18. Combat model card

**Model ID:** `DEV_COMBAT_HAZARD_V0`  
**Scope:** Promotion-, sport- and rules-specific winner, method, duration and round markets. Boxing, MMA and other combat sports require separate fitted cards.  
**Target engine:** Round/time competing-risks model for stoppage methods, submission where applicable, disqualification/no-contest and decision. If the bout reaches decision, a judging submodel maps round-level latent performance to scorecard outcomes under the exact rules. Method, round and winner probabilities come from the same joint path.  
**Baseline:** Hierarchical participant strength plus method and scheduled-duration base rates.  
**Required features:** Official bout/rules/weight, weigh-in and late replacement, participant history with opponent adjustment, age/reach/stance where stable, pace/accuracy/defence/grappling definitions, scheduled rounds, judges/referee when released.  
**Live state:** Round/clock, official knockdowns/points or position/control events where reliably available, deductions, doctor checks and foul state.  
**Diagnostics:** Competing-risk calibration, censoring, decision/stoppage mix, weight-class/promotion transfer and late-replacement scenarios.  
**Hard exclusions:** Boxing/MMA pooled, post-weigh-in facts backfilled historically, independent method and winner models that do not reconcile.

## 19. Markets not yet supported

`OTHER_SPORT_ALL` remains `UNSUPPORTED`. A new sport needs a sport-native primitive-event model, official source chain, exact rules/settlement, point-in-time data contract, baseline, uncertainty plan and its own development card. Copying the nearest sport’s coefficients or distribution is prohibited.

## 20. Version 0.1.0 activation blockers

All development cards share these unresolved blockers:

1. no approved licensed/source-tested model feature maps;
2. no point-in-time data snapshots or eligible event manifests;
3. no fitted parameters or immutable model artifacts;
4. no tuned distribution/feature/hyperparameter decisions;
5. no separate calibration artifacts;
6. no preregistered numeric promotion/guardrail/drift thresholds;
7. no SPENT untouched-test reports;
8. no later prospective-shadow reports;
9. no production candidate generator or decision-policy evidence;
10. no owner, independent evaluator, approver or expiry.

Until each exact scope clears every blocker, the only authorized output is WATCH/PASS with null probability, edge, EV and stake fields.
