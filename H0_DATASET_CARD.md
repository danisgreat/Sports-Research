# H0 dataset card — current implementation dependency


Version **H0-2026.09.19-v0.4**; training specification **NTS-2026.09.19-v0.5**; method **MDS-2026.09.19-v4.3 / CR-2026.09.21-3**.


Status: **NOT BUILT / NOT QUALITY-APPROVED**. The root file was missing; the detailed schema below is recovered from audit_2026-09-12/before/H0_DATASET_CARD.md. Recovery does not certify the old schema's data or approval state. The current card and NUMERICAL_PROGRAM override historical design text below.


## Current first-build scope


PILOT-MLB-RUNS-2026: systematic MLB regular-season game universe; joint completed final home/away scores, with exact extras/home-termination/shortened-game endpoint policy. One gamePk per event; every view shares that cluster. No user-selected log cohort is the fitting universe. Other sport H0 cards remain design-only.


| Field | State / admission requirement |
|---|---|
| User authorization | Audit implementation authorized 17 September; latest steering prioritizes Markdown |
| Data artifacts | NONE for a quality-approved H0; prior season-scale retrieval is retrospective reference data |
| Source manifest | MLB official schedule/linescore is a candidate field-owner lane; verify exact field schemas, status, coverage, revision semantics and allowed access before admission |
| Label fields | gamePk, sport/competition, season/gameType, actual endpoint, final state, scheduled/completed innings, home/away IDs, home/away runs, venue, original and revised dates; regulation splits separately if used |
| Feature fields | Snapshot and availability time for every team/park/starter/lineup/relief/weather input; no end-of-season statistics joined backward; labels kept separate |
| Availability evidence | Required for genuine historical pregame evaluation; otherwise DEVELOPMENT_RECONSTRUCTION_ONLY, never E1-P |
| Data quality | Unique event keys, duplicate/alias audit, complete eligible schedule, exclusions with denominators, joins/timezones, postponed/suspended games, final-score consistency, missingness, current-versus-historical revision checks |
| Splits | TRAIN/TUNE/CAL/TEST exact dates NOT YET FROZEN; all event views grouped; fitting/calibration before test; untouched test opened once |
| Baseline and scoring | A0/A1 on identical events, fixed threshold grid plus issued lines; complete W/P/L and event-level distribution metrics under SCORING_AND_VALIDATION |
| Build eligibility | None until source fields and time joins pass; no fitted/champion status from this restored file |


## Minimum machine-readable Markdown record


```json
{"event_id":"REQUIRED","event_cluster":"REQUIRED","competition":"MLB","game_type":"R","target":"JOINT_FINAL_RUNS","endpoint_rules_version":"REQUIRED","scheduled_start_utc":"REQUIRED","forecast_cutoff_utc":"REQUIRED","issued_at_utc":"REQUIRED","features_available_by_utc":"REQUIRED","source_retrieved_at_utc":"REQUIRED","source_snapshot_hash":"REQUIRED","home_id":"REQUIRED","away_id":"REQUIRED","venue_id":"REQUIRED","feature_values":{},"feature_missingness":{},"label_available_at_utc":null,"home_runs":null,"away_runs":null,"final_state":null,"exclusion_reason":null,"split":"UNASSIGNED","eligibility":"NOT_ADMITTED"}
```


REQUIRED is a placeholder, never a valid value in an admitted record. Label fields remain null before outcome availability. Freeze the population/split/feature manifest and its hash before fitting. Schema acceptance must reject duplicate events, future features, unresolved labels in training, mismatched endpoints and missing cutoff/availability records.


## Recovered detailed design reference


The following pre-existing field lists and sport schemas are retained for traceability. Status, authority and eligibility statements are historical; the current card above and SCORING_AND_VALIDATION govern.


# H0 numerical-training dataset cards


> **`NUMERICAL_PROGRAM.md` is the new entry point (v4.0 comprehensive overhaul, 2026-09-06).** This document remains the full dataset-card reference.


Status: **ACTIVE DESIGN — NOT BUILT / NOT QUALITY-APPROVED — DETAILED REFERENCE**


Card version: **H0-CARDS-2026.08.25-v0.2**


Numerical training specification: **NTS-2026.08.25-v0.2**


Effective: **2026-08-25**


H0 is a future source-derived historical dataset, not a reconstruction of PREDICTION_LOG.md. This document preregisters target populations, grains, labels and gates for every dedicated sport. It contains no source rows, fitted values, split dates, sample counts, probabilities or performance results.


## 1. Dataset firewall


- D0 remains process, representation, error-mechanism and case-retrieval evidence only.
- H0 may use source-derived outcomes/features only when every prediction field is reconstructable at the frozen cutoff and approved by DATA_SOURCE_REGISTER.md.
- Later lineups, realised weather, declarations, corrections, finals, closing prices and future season aggregates cannot enter an earlier feature snapshot.
- Labels join only after the feature/prediction snapshot is frozen.
- User-selected forecasts, alternate lines and repeated views do not define the training population or create independent events.
- E1-Q and `E1-Q-LATE_IMPORT` do not become same-version H0/CAL/TEST evidence merely because outcomes are known.
- The log's issued forecasts and settlements remain untouched by an H0 build.


## 2. Systematic population rule


Every build must enumerate all eligible events in a frozen competition, rules era, date range and forecast horizon before outcomes are used. Exclusions are limited to preregistered identity, rules, source-coverage, label, censoring and quality conditions. “Interesting game,” “available easy alternate,” user request and model confidence are prohibited inclusion criteria.


Store both:


1. the event/target population used to train and score distributions; and
2. a one-to-many contract evaluation table generated by a frozen main/alternate-line policy.


Contract rows never change the event's independent weight.


## 3. Design-only build register


| H0 build ID | Population awaiting source audit | Primary target | Mode | State |
|---|---|---|---|---|
| `H0-CRICKET-MTEST-DAY-v0-DESIGN` | Men's Tests | `TEST_DAY_RUNS_FULL-v1` | Named-day pre-play | NOT BUILT |
| `H0-CRICKET-MTEST-INN-v0-DESIGN` | Men's Tests | `TEAM_FIRST_INNINGS_TOTAL-v1` | Pregame/frozen innings-state strata | NOT BUILT |
| `H0-CRICKET-LO-v0-DESIGN` | Each ODI/T20 competition/format separately | `LIMITED_OVERS_JOINT_RESOURCE_SCORE-v1` | Pregame and separate live horizons | NOT BUILT |
| `H0-BASKETBALL-FULL-v0-DESIGN` | Each league/rules population separately | `BASKETBALL_JOINT_FINAL_SCORE-v1` | Pregame regulation/OT-defined | NOT BUILT |
| `H0-AMFOOT-FULL-v0-DESIGN` | NFL/NCAA/UFL/CFL separate | `AMFOOT_JOINT_FINAL_SCORE-v1` | Pregame regulation/OT-defined | NOT BUILT |
| `H0-BASEBALL-FULL-v0-DESIGN` | MLB/NPB/KBO separate | `BASEBALL_JOINT_FINAL_RUNS-v1` | Pregame with action terms | NOT BUILT |
| `H0-AFL-FULL-v0-DESIGN` | AFL and AFLW separate | `AFL_JOINT_FINAL_SCORE-v1` | Pregame full match | NOT BUILT |
| `H0-RL-FULL-v0-DESIGN` | NRL/NRLW/Super League separate | `RUGBY_LEAGUE_JOINT_FINAL_SCORE-v1` | Pregame regulation/golden-point-defined | NOT BUILT |
| `H0-SOCCER-REG-v0-DESIGN` | Each competition/rules population | `SOCCER_REGULATION_JOINT_GOALS-v1` | Pregame 90-minute regulation | NOT BUILT |
| `H0-HOCKEY-NHL-v0-DESIGN` | NHL; other competitions separate | `ICE_HOCKEY_REG_SCORE_MATCH_RESULT-v1` | Pregame regulation plus linked OT/SO result | NOT BUILT |


Women/men, senior/youth, preseason/regular/postseason, domestic/international and materially different rules/coverage populations are not silently pooled. Hierarchical pooling is a future challenger only after exchangeability tests.


## 4. Universal paired-score target card


Applies to basketball, American football, baseball, AFL/AFLW, rugby league, soccer goals and ice hockey, with a sport-specific target version.


| Field | Frozen design requirement |
|---|---|
| Outcome | Joint official score/resource pair `(X,Y)` at the target endpoint |
| Start state | Pregame or a separately versioned live/phase snapshot |
| Endpoint | Exact regulation/full-match/extra-period endpoint matching contract terms |
| Exposure | Possessions, drives, PAs/innings, territory/scoring shots, sets, attacking sequences, shifts/shots, or other native opportunities |
| Structural state | Participants/roles, strength, matchup, score/game state, environment and termination |
| Support | Sport-valid discrete score combinations and any draw/tie state |
| Labels | Official score/result plus component labels, provider and correction version |
| Derived contracts | Winner/result, total, margin/handicap, team totals and predeclared alternate grid from one joint distribution |
| Separate targets | Phase, player, corners/cards/shots and materially different regulation/OT/advance endpoints |
| Censoring/void | Frozen treatment of abandonment, postponement, shortening, mercy, listed-player/action and incomplete events |


## 5. Cricket target cards


### Test day runs


| Field | Frozen design |
|---|---|
| Target | `TEST_DAY_RUNS_FULL-v1`: integer sum of official runs by either team during the named scheduled Test day |
| Start/endpoint | Official preceding close or predeclared pre-play snapshot to named-day close, earlier match completion, or frozen abandonment rule |
| Cross-innings | Includes every innings/team transition during the day; innings completion does not stop the target |
| Exposure | Scheduled time/overs plus point-in-time weather, light, delays, over rate and early-completion uncertainty |
| Label | Official day/session segmentation or legality-reconciled event reconstruction |
| Unresolved | Population/dates, no-play/abandoned days, extensions, over-rate effects and day-boundary reliability |


### Team first-innings total


| Field | Frozen design |
|---|---|
| Target | `TEAM_FIRST_INNINGS_TOTAL-v1`: named team's official completed first-innings total |
| Start/endpoint | Pregame or separately versioned innings state to all-out, declaration, chase/forfeit or contract-defined innings end |
| Cross-day | Continues across days; excludes the next innings |
| Exposure | Legal balls, batter/bowler resources, weather/light, declaration and match-state incentives |
| Censoring | Incomplete innings use a preregistered censor/exclude/void policy; never ordinary completed totals |
| Unresolved | Forfeiture, declaration timing, corrections and incomplete-innings policy |


## 6. Player and niche-target card


Every player/event target is a separate distribution row linked to the event state.


| Field | Requirement |
|---|---|
| Identity/action | Exact player/entity, starter/action rule, provider statistic and void terms |
| Participation | Active/start probability and replacement branch known by cutoff |
| Exposure | Minutes, possessions, usage, snaps/routes/carries/targets, PAs/batters faced, balls faced, time on ground, sets, ice time or event opportunities |
| Rate | Opponent-adjusted event rate conditional on role/exposure |
| Team-state link | Shared pace, lineup, field position, score state, manpower or tactical scenarios where justified |
| Label | Exact provider definition/version; provider changes create a new target version or reconciliation gate |
| Support/tails | Valid integer/continuous support, zero/low exposure, substitution, injury and blowout/early-exit tails |
| Exclusion | Missing identity, action, provider definition or unreconstructable known-at state blocks the row |


## 7. Canonical normalized grains


| Table concept | Grain/key | Purpose |
|---|---|---|
| `raw_snapshot` | source release/retrieval | Immutable bytes/response, version, hash, coverage and use record |
| `event` | official event ID | Competition, rules era, participants, venue, schedule and identities |
| `participant_status` | event × entity × known-at revision | Availability, role, lineup/starter and expected exposure evidence |
| `event_sequence` | event × official sequence | Delivery/play/possession/PA/shot/set/shift with provider semantics |
| `state_snapshot` | event × target × cutoff | Exact prediction-time state and source references |
| `feature_value` | state snapshot × entity × feature version | Value/unit/times/source/quality and transform |
| `target_label` | state snapshot × target version | Official eventual outcome joined after freeze |
| `distribution_prediction` | state snapshot × model build | Immutable raw/calibrated distribution reference |
| `derived_contract` | distribution prediction × contract | W/P/L geometry, dependence and integrated probability |
| `market_snapshot` | event × contract × operator × captured time | Separate price/value benchmark |


No bookmaker threshold is a primary target label for the main engine. Threshold W/P/L labels are deterministic evaluation views derived from the official target label.


## 8. Point-in-time fields


Every feature stores:


| Field | Requirement |
|---|---|
| IDs | `event_id`, `state_snapshot_id`, `target_id`, entity/feature/version |
| Value | Typed value, unit, quality flag and permitted missingness/conflict state |
| `effective_at` | When the underlying fact became true |
| `known_at` | Earliest demonstrable availability to the forecasting process |
| `observed_at` | Live observation time when applicable |
| `retrieved_at` / `cutoff_at` | Snapshot access and forecast boundary |
| Provenance | Source/version/raw hash and definition version |
| Transformation | Exact fold-safe transform/rating/decay version |


Admission assertion: `known_at <= cutoff_at`. If it cannot be demonstrated, store the governing missingness code; do not infer that it was probably available.


## 9. Candidate feature families by sport


All require feature-admission cards and chronological ablation.


| Sport | Exposure/state | Rate/quality | Required scenarios |
|---|---|---|---|
| Cricket | Balls/overs/time, wickets, batting order, bowlers, lead/target | Opponent-adjusted runs and dismissals by phase/state | Toss, pitch/weather/light, declaration, DLS, innings switch, collapse/death |
| Basketball | Minutes, lineups, possessions, usage | Shot/FT/turnover/rebound and per-possession efficiency | Availability, foul trouble, blowout, late foul, OT |
| American football | Drives, plays, field position, snaps | QB-regime success/EPA, trenches, coverage, red zone | Turnovers, explosive/non-offensive score, script, weather, OT |
| Baseball | PA, batters faced, pitch/inning, base-out, bullpen chain | K/BB/contact/HR/platoon/defence/park | Starter exit, reliever availability, home ninth, extras |
| AFL/AFLW | Time/role, possessions, inside-50s, scoring shots | Territory, shot quality and conversion | Late changes, venue/weather, tempo, separation |
| Rugby league | Minutes/interchange, sets, tackle/field position | Completion, metres, line breaks, try/conversion | Spine/kicker, fatigue, errors/short fields, sin-bin, golden point |
| Soccer | Minutes, XI/formation, attacking sequences, shots | Dynamic attack/defence, xG/keeper, target-specific corner/card/SOT rates | Rotation, score state, red card, stoppage, extra-time distinction |
| Ice hockey | Ice time/shifts, shots/chances, manpower, goalie exposure | xG/finishing/goaltending/special teams | Starting goalie, penalties, pulled goalie, empty net, OT/SO |


Raw L5/L10 outcomes, old H2H, future aggregates, realised weather and closing markets are not automatic sports features.


## 10. Label, exclusion and market policy to freeze


Before any build:


1. official label/provider and correction cutoff;
2. competition/rules/population and abnormal-event exclusions;
3. regulation/extra-period, home-last-exposure, shortening, abandonment and censoring treatment;
4. player action, substitution and provider-stat definitions;
5. duplicate identities, source conflicts and later corrections;
6. event/series/round grouping and normalized event weight;
7. minimum feature/source quality per target horizon;
8. systematic event enumeration and candidate-line grid;
9. `MARKET_BLIND`, `MARKET_ONLY` and `MARKET_INFORMED` feature manifests;
10. de-vig method candidates and price timestamp/terms rules.


## 11. Chronological split manifest


| Field | Current value |
|---|---|
| Eligible date ranges | NOT ASSIGNED — requires approved source coverage audits |
| TRAIN/TUNE/CAL/TEST dates | NOT ASSIGNED |
| Grouping | Event mandatory; series/round/date blocks to be frozen where material |
| Rolling origins | NOT ASSIGNED |
| Refit/decay policy | NOT ASSIGNED |
| Multiple-search budget | NOT ASSIGNED |
| Prospective E1-P start | NOT ASSIGNED |


Dates are frozen before corresponding outcomes are inspected for selection.


## 12. Quality gates


H0 remains `NOT QUALITY-APPROVED` until applicable checks pass:


- source hash/version/coverage/exclusions/use status and replayable corrections;
- event, participant, venue and provider identity reconciliation;
- event-sequence legality and official score/stat reconciliation;
- target endpoint, support, censoring, label and contract-integration tests;
- `known_at <= cutoff_at`, deliberately future-dated negative controls and shuffled-time leakage checks;
- row/distinct-key counts before/after every join and one-to-many normalization;
- missingness, conflicts, staleness, units, ranges and outliers;
- fold isolation and fold-local transformations/ratings;
- rules/provider/competition drift and material subgroup support;
- systematic-universe completeness and absence of post-hoc event/line selection;
- deterministic rebuild manifest and hashes.


## 13. Current state


| Claim | State |
|---|---|
| Historical source data downloaded | NO |
| H0 rows built | NO |
| Sport/competition coverage measured | NO |
| Split dates assigned | NO |
| Quality gates run | NO |
| Model fitted | NO |
| H0 approved for probability publication | NO |


This card makes future work auditable; it does not claim that work has begun.


<!-- DEEP-RESEARCH-IMPLEMENTATION-2026-09-19-V42 -->
## 2026-09-19(c) — H0 provenance firewall


H0 must contain **no sportsbook/bookmaker/odds/line-movement/picks/tips/prediction-market/fantasy/DFS predictive fields**. User-requested totals/spreads are stored, if needed for evaluation, in a separate contract-query table that is never joined into the model feature matrix.


Minimum provenance columns for every predictive field: `event_id`, `field_name`, `value`, `source_id`, `source_class`, `field_owner`, `upstream_lineage_id`, `source_definition_version`, `published_at`, `first_known_at`, `retrieved_at`, `forecast_cutoff_at`, `snapshot_hash`, `freshness_status`, `missingness_reason` and `correction_semantics`.


Quality approval must explicitly test duplicate upstream lineages, future-known values, postgame revised fields, stale critical state, identifier leakage, label leakage, schema drift and competition/era coverage. H0 approval is a data-quality decision; it is not evidence that a model is accurate.