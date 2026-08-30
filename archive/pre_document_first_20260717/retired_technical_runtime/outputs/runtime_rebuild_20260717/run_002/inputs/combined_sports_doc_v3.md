# Sports Research Operating Manual v3

Effective: 2026-07-16 (Australia/Sydney)  
Status: CANONICAL SPECIFICATION  
Operational status: **SUSPENDED — NO ACTIVE MODELS**

Analysis-only capability: **ACTIVE_ANALYSIS_ONLY — FIVE QUALITATIVE LIVE-STATE MODELS**
Scope: research requests, abstentions, probabilistic forecasts, optional price evaluation, settlement and model review

This file is the complete human instruction set for transfer to a new task or workspace. The registries, schemas, source catalogues and runtime files remain the executable evidence and enforcement layer, but no separate prose document is required to understand the general workflow, logging rules, retrospective process or sport-specific boundaries.

`SPORTS_RESEARCH_AUTHORITY_MANIFEST.md` controls document authority and precedence. `SPORTS_MODEL_COVERAGE_REGISTRY_v3.csv` controls operational activation. It currently contains no ACTIVE row, so every quantitative request must return `PASS` with `pass_reason=MODEL_UNAVAILABLE`. A canonical specification is not evidence that a model is fitted, calibrated, profitable or ready.

## 1. Claims and decision meanings

- A probability is not a promise. Never use `lock`, `certain`, `guaranteed`, `safe`, or equivalent language.
- No honest process can promise no mistakes. The commitment is to frozen inputs, reproducibility, proper scoring, uncertainty, error measurement and abstention.
- `ISSUE` means a user-facing quantitative forecast from an ACTIVE, exactly in-scope model. It does not mean bet, value or guaranteed outcome.
- `WATCH` is a temporary non-forecast state while a named prerequisite is pending. It contains no decision probability, edge, expected value or stake, is not scored as a forecast, and must expire or be replaced by a new immutable snapshot.
- `PASS` is an abstention. It always has a controlled `pass_reason` and contains no forecast probability when the reason is `MODEL_UNAVAILABLE`, `CONTRACT_UNRESOLVED`, `CUTOFF_FAILURE`, `SOURCE_FAILURE`, `OUT_OF_SCOPE`, `UNCERTAINTY_UNRESOLVED`, or `PRICE_PACKET_INVALID`.
- A non-probabilistic research note may accompany WATCH/PASS, but it must not contain a numeric probability range, confidence label, edge, value, staking or profitability language.
- Historical v2/v3 probabilities are `LEGACY_UNVERIFIED_SNAPSHOT`. They are diagnostic evidence only and cannot support a verified accuracy, calibration, ROI, yield or CLV claim.
- `Comprehensive` means completed coverage against a declared checklist. It never means all possible facts were found.

## 2. Orthogonal modes

Every request freezes two independent fields under **GATE-MODE-001**:

1. `analysis_mode = RESEARCH_ONLY | PRICE_ENABLED`.
2. `forecast_state = PREGAME_PROJECTED | PREGAME_CONFIRMED | LIVE`.

`RESEARCH_ONLY` hard-blocks price-derived edge, expected value, stake, yield, P&L and CLV. `PRICE_ENABLED` permits evaluation only after a complete, contemporaneous market packet passes **GATE-PRICE-001**. LIVE is not a price mode; it is a forecast state and needs exact state/exposure.

Pregame-projected, pregame-confirmed and live forecasts use separate model scopes, identifiers, evaluation strata and calibration evidence. Live forecasts are further segmented by sport-native state/horizon buckets declared in the model card.

## 3. Universal hard gates

These gates fail closed. Their owners and executable acceptance tests are in `SPORTS_ACCEPTANCE_TESTS_v3.md`.

| Gate ID | Requirement | Failure result |
| --- | --- | --- |
| GATE-AUTH-001 | Canonical authority resolves through the manifest; every dependency exists | PASS / SYSTEM_NOT_READY |
| GATE-CONTRACT-001 | Event, primary question, market, outcome space and settlement convention are exact | PASS / CONTRACT_UNRESOLVED |
| GATE-MODE-001 | Analysis mode and forecast state are independently recorded | PASS / MODE_UNRESOLVED |
| GATE-CUTOFF-001 | Snapshot is immutable; all decisive facts were knowable by cutoff; live state is at/before publication | PASS / CUTOFF_FAILURE |
| GATE-SOURCE-001 | Identity/rules/state/final use approved authority; source packet has fact-level timestamps/status/hashes | PASS / SOURCE_FAILURE |
| GATE-UNIVERSE-001 | Primary question, selection mode, universe version and every inspected/rejected candidate were frozen before outcome | PASS / UNIVERSE_NOT_FROZEN |
| GATE-MODEL-001 | Model and coverage rows are ACTIVE, approved, unexpired and exactly match sport/competition/market/settlement/state/horizon and artifacts | PASS / MODEL_UNAVAILABLE |
| GATE-TEST-001 | Train/tune/calibrate/test periods are disjoint; test was untouched; mandatory prospective shadow passed; viewed tests are spent | PASS / MODEL_UNAVAILABLE |
| GATE-PROB-001 | Complete outcome branches reconcile; decision probability is reproducible; calibration wording is supported | PASS / PROBABILITY_INVALID |
| GATE-COHERENCE-001 | Related markets share a registered joint outcome space and satisfy every declared logical/arithmetic invariant | PASS / PROBABILITY_INVALID |
| GATE-UNCERTAINTY-001 | Typed total and material component uncertainty is quantified; decision is robust to declared scenarios | PASS / UNCERTAINTY_UNRESOLVED |
| GATE-PRICE-001 | PRICE_ENABLED packet has complete outcome quotes, time/source, de-vig method, commission/payoffs, staleness and limits | PASS / PRICE_PACKET_INVALID |
| GATE-EXECUTION-001 | Stake/yield/P&L/CLV has an authorized immutable execution and applicable closing snapshot | Claim prohibited |
| GATE-SETTLEMENT-001 | Official result and stored convention produce an append-only grade; forecast remains unchanged | UNGRADABLE/PENDING |
| GATE-LEGACY-001 | Legacy and mixed-cutoff rows are excluded from v3 metrics | Exclude from evaluation |

No evidence grade, analyst judgment or “stricter rule” may override a failed hard gate.

## 4. Prediction lifecycle

### Stage A — freeze the request and primary question

Before research, record:

- `request_id`, verbatim/raw request, `primary_question_id`, `forecast_series_id`, author and request time;
- official sport, competition, season/round, participants, venue, event ID, scheduled start and ruleset;
- exact market ID/definition, selection, line, full outcome space and settlement convention;
- `analysis_mode`, `forecast_state`, forecast horizon and cutoff;
- `selection_mode = USER_SUPPLIED | FIXED_UNIVERSE | MODEL_SELECTED`;
- candidate-universe version and selection-policy version;
- whether overtime, extra time, shootouts, extra innings, Super Overs, DLS/reduced exposure, target-score overtime or other branches count.

If identity, primary question, outcome space, settlement or mode is unresolved, freeze a PASS snapshot with the raw request and unresolved fields null; do not invent placeholder IDs and do not continue to a probability.

### Stage B — freeze the complete candidate universe

Log every candidate inspected, including rejected candidates, before the outcome is known. Each candidate stores market ID, selection, line, relationship, inclusion source, selection-policy score if any, eligibility, rejection reason and whether it is the primary question. A model-selected pipeline must be evaluated with the same universe-generation and selection code used prospectively.

The opposite side and push branch belong to one mutually exclusive outcome space. They are not independent picks. One issued prediction addresses one declared selection; secondary claims cannot replace the primary requested outcome in reporting.

### Stage C — build a point-in-time source packet

Use `SPORTS_SOURCE_REGISTRY_v3.md` as the researched fact-specific catalog. Each ACTIVE model must still supply an approved scoped `source_map_id` with parser/latency tests. Each decisive fact stores:

`source_observation_id | source_id | URL/route | authority tier | published_at | known_at | fetched_at | applies_to_time | access status | fact value/unit | raw hash`

Minimum packet:

- official fixture, identity, rules and settlement authority;
- official or explicitly projected availability/lineup state;
- performance features with definition, competition/season scope, latency and last observation time;
- venue/match-window conditions when material;
- exact official live state for LIVE;
- complete market snapshot for PRICE_ENABLED.

All feature/source joins must satisfy the temporal tests in `SPORTS_ACCEPTANCE_TESTS_v3.md`. Blocked, stale, snippet-only, conflicting or missing decisive evidence is recorded and fails closed unless the registered model explicitly supports that missingness and the uncertainty gate passes.

### Stage D — data and leakage tests

- Event/team/player IDs, competition, season, phase, venue and rules variant match.
- Feature definitions and units are versioned and stable over their applicable window.
- Duplicates, postponements, corrections, projected/confirmed status and missing phases are explicit.
- No final, closing, revised post-cutoff injury/lineup, later live state or outcome-derived field enters a frozen feature snapshot.
- Historical backtests reproduce production latency and missingness; a modern fetch of an as-of dataset is labelled reconstruction and must prove the value/version existed by cutoff.
- Snapshot hash recomputation, foreign keys and immutability tests pass.

### Stage E — activate only a validated model

The exact coverage row and model card must both be ACTIVE. The current registry has no ACTIVE models.

An activation candidate must have:

- exact target, scope, settlement, state and forecast horizon;
- cutoff-safe training data and reproducible artifacts;
- frozen naive baseline and, in PRICE_ENABLED mode, no-vig market comparator on identical eligible events;
- one preregistered primary metric, minimum practically relevant improvement, effective-N/precision rule and guardrails;
- disjoint train, tune, calibration and untouched-test periods;
- an untouched mandatory prospective shadow period after all choices are frozen;
- typed calibration evidence and total uncertainty;
- approval, expiry, drift, suspend, rollback and restart rules.

The untouched test may be evaluated once. Once any test outcome or aggregate is viewed, that period is `SPENT` for every related challenger or manual rule. A failed or modified model needs a new later untouched period. A point-estimate win without the preregistered uncertainty/effect rule is not evidence of improvement.

### Stage F — freeze ISSUE, WATCH or PASS

Every request receives a new immutable `snapshot_id`. Updates use a new snapshot and link `parent_snapshot_id`; a stable `forecast_series_id` groups the sequence. An ISSUE also receives a unique immutable `prediction_id` that is never versioned or reused.

ISSUE requires:

- exact ACTIVE model/coverage scope and artifact hashes;
- complete branch probabilities and raw/decision probability;
- calibration status/evidence without unsupported “calibrated” wording;
- typed uncertainty and invalidation triggers;
- baseline on the same eligibility set;
- price/no-vig/EV fields only for PRICE_ENABLED;
- one primary question and the frozen candidate universe.

WATCH/PASS store the missing prerequisite and contain null model/probability/edge/EV fields when no valid quantitative forecast exists. A later update is a new snapshot; nothing overwrites the prior one.

### Stage G — settle independently

- Wait for an official final/gamebook/scorecard or a predeclared fallback.
- Apply the exact stored settlement convention and outcome branch.
- Append settlement versions with official status, numeric outcome, `WIN | LOSS | PUSH | VOID | UNGRADABLE | PENDING`, source, fetch time and reviewer.
- Corrections append; they never alter the frozen request, candidates, sources, model, probability, rationale or price snapshot.

### Stage H — evaluate and review

Evaluation is a derived, versioned entity keyed by prediction, settlement version, scoring-spec version and scoring-code hash. Use `SPORTS_SCORING_SPECIFICATION_v3.md`. Report the primary question, complete selection pipeline, proper scores, baseline deltas, coverage/abstention, interval coverage and event-clustered uncertainty. Do not hand-edit KPI totals.

Postmortems may create hypotheses, not rules. A change requires a ticket, new future test data, mandatory prospective shadow and a new model version. No single outcome can activate a permanent rule.

## 5. Evidence-integrity grades

Grades describe evidence integrity, not confidence or activation. They can only restrict an otherwise ACTIVE, in-scope model.

| Grade | Meaning | Maximum action |
| --- | --- | --- |
| A | Contract/source/cutoff complete; volatile inputs current; model validated for the exact state | ISSUE, WATCH or PASS if all hard gates pass |
| B | One non-critical, model-supported projected/secondary input; registered sensitivity passes | ISSUE only if the model card explicitly covers this missingness; otherwise WATCH/PASS |
| C | Material lineup/exposure/surface/phase gap, transfer or unresolved component | WATCH/PASS |
| D | Contract/cutoff/leakage/stale-state/settlement failure | PASS |

## 6. Sport and model scope

`SPORTS_MODEL_COVERAGE_REGISTRY_v3.csv` is the only operational allowlist. Sport-native baselines, candidate model families, transfer restrictions and minimum development evidence are defined once in `SPORTS_MODEL_VALIDATION_AND_SIMULATION_FRAMEWORK_v3.md`; instantiated non-operational model cards are in `SPORTS_DEVELOPMENT_MODEL_CATALOG_v1.md`; fact-source chains are defined in `SPORTS_SOURCE_REGISTRY_v3.md`. A DEVELOPMENT card records intended mechanics and blockers only. An unlisted, expired or non-ACTIVE scope must PASS.

## 7. Distributions and simulation

Distribution choice, Poisson diagnostics, alternatives, simulation records, convergence and Monte Carlo error are owned by the validation framework. Poisson is not an all-sport default, simulation repeatability is not forecast validity, and no simulated probability may bypass GATE-MODEL-001 or GATE-UNCERTAINTY-001.

## 8. Price, EV and execution

`SPORTS_SCORING_SPECIFICATION_v3.md` is the single authority for de-vig, outcome-branch payoff and expected-return mathematics; `SPORTS_DATA_DICTIONARY_v3.md` owns the price and execution entities. Keep `baseline_probability_delta`, realized proper-score skill, `market_edge` and `expected_return` distinct. RESEARCH_ONLY prohibits price/value/stake claims. PRICE_ENABLED still requires the registered conservative decision rule, and realized yield/P&L/CLV require an actual execution.

## 9. Monitoring, suspension and rollback

The validation framework owns monitoring windows, drift thresholds, suspension, restart and rollback. Leakage, scope/artifact mismatch, broken definitions, unresolved settlement error, regression failure or a preregistered drift breach must fail closed immediately; only a new approved version with new untouched evidence and prospective shadow may resume.

## 10. Minimum outputs

### ISSUE

```text
REQUEST / PRIMARY QUESTION / FORECAST SERIES:
SNAPSHOT ID / PREDICTION ID / PARENT SNAPSHOT:
ANALYSIS MODE / FORECAST STATE / HORIZON / CUTOFF UTC:
EVENT / MARKET / SELECTION / OUTCOME BRANCHES / SETTLEMENT:
CANDIDATE UNIVERSE / SELECTION MODE / POLICY VERSION:
DATA-QUALITY GRADE / DECISIVE SOURCES:
MODEL / COVERAGE / DATA / FEATURE / CODE / CALIBRATION ARTIFACTS:
RAW P / DECISION P / TYPED UNCERTAINTY:
BASELINE / BASELINE SKILL DELTA:
PRICE SNAPSHOT / NO-VIG METHOD / MARKET EDGE / EV INTERVAL: PRICE_ENABLED only
DECISION: ISSUE
INVALIDATION TRIGGERS:
```

### WATCH or PASS

```text
REQUEST / PRIMARY QUESTION / FORECAST SERIES:
SNAPSHOT ID / PARENT SNAPSHOT:
ANALYSIS MODE / FORECAST STATE / CUTOFF UTC:
EVENT / MARKET / SETTLEMENT:
CANDIDATE UNIVERSE / SELECTION MODE:
DECISION: WATCH | PASS
PASS OR WATCH REASON / MISSING PREREQUISITE / EXPIRY:
NON-PROBABILISTIC RESEARCH NOTE (optional):
MODEL / PROBABILITY / EDGE / EV / STAKE: N/A
```

Storage is controlled by `SPORTS_DATA_DICTIONARY_v3.md`; scoring by `SPORTS_SCORING_SPECIFICATION_v3.md`; modelling by `SPORTS_MODEL_VALIDATION_AND_SIMULATION_FRAMEWORK_v3.md`; gates by `SPORTS_ACCEPTANCE_TESTS_v3.md`.

## 11. Mandatory request-time runbook

Apply this sequence to every sports request, including requests for four ranked picks and a potential winner.

1. Read the newest entry in `PREDICTION_RESULTS_LOG_v5.md`. If its event is still live, upcoming, suspended or not reliably final, do not grade it. If it is final and an exact settlement contract exists, settle it before using the result as retrospective evidence.
2. Freeze the verbatim request, one primary question, event identity, competition, scheduled start, market definitions, supplied lines, forecast state and UTC cutoff. Never silently substitute a similarly named match or a newer line.
3. Resolve the contract: regulation/full-game scope, overtime or extra innings, DLS/reduced overs, push/void rules, player participation thresholds, dead-heat rules and official correction policy. Missing material terms require PASS.
4. Capture point-in-time evidence. Prefer the exact official match centre, league/organiser rules and official team or player status. Record the source URL, observation time, fetch time, applicable time, access state and retained-content hash.
5. For LIVE analysis, state the exact scoreboard, clock/inning/over/period and market line as of the cutoff. A bookmaker scoreboard is a secondary live feed unless the registered source map explicitly approves it. Disclose feed conflicts and stale user lines.
6. Freeze the complete candidate universe. Rank every supplied item, but do not pretend opposing or overlapping branches are independent recommendations. Explain middle, push and dead-zone outcomes explicitly.
7. Run only an exactly in-scope ACTIVE or ACTIVE_ANALYSIS_ONLY model. Never transfer a model across competition, format, sex, age group, regulation variant, market, forecast state or horizon without registered evidence.
8. Return ISSUE, WATCH or PASS. A qualitative live model may return a named-side lean or TOSSUP, but not a numeric probability or betting claim.
9. Put the exact user-facing ranking, potential winner, cutoff and decisive limitations in the recorded research or analysis note. The chat answer and stored ranking must match.
10. Record the decision and regenerate the copy-friendly prediction log before finishing the request.

### Four-pick presentation rule

When four candidate markets are supplied, rank all four from best supported to weakest. Label each as `SUPPORTED`, `LEAN`, `AVOID` or `PASS`. Do not call all four picks when some are opposites. The potential game winner is a separate qualitative field unless it is itself one of the four frozen candidates. Never create a player pick without verified availability and the exact prop settlement rule.

## 12. Research, source and freshness instructions

Use this fact hierarchy: official league/organiser rules and match centre; official team/player announcement; licensed definition-stable data provider; reputable secondary reporting; search snippet or social post only as a discovery lead. One source need not control every fact. Identity, rules, live state, final result, lineup, weather and market price may each require different authorities.

For every decisive fact, preserve `source_id`, URL or route, authority class, published time when available, known-at time, fetched-at time, applies-to time, access status, value/unit and raw-content hash. Dynamic pages must be captured at the cutoff. Snippet-only, blocked, stale, conflicting, wrong-event or post-cutoff evidence cannot be treated as verified. Current availability must not be inferred from an old roster, and a schedule listing does not establish a final lineup.

Official corrections control settlement when the stored convention says so. If core identity fields conflict—participants, venue, toss, lineup, inning order, period or event ID—leave the item unresolved instead of choosing the convenient source.

## 13. Prediction-log and copy/paste contract

`runtime/store/journal.jsonl` is the tamper-evident machine record. `PREDICTION_RESULTS_LOG_v5.md` is the generated, human-readable document that must contain every recorded decision packet and every recorded qualitative live analysis. It includes PASS and WATCH records so abstentions cannot disappear from the history.

- `new-request` records by default and regenerates the Markdown log. `--no-record` is permitted only for explicit testing or draft construction, never for a delivered prediction or analysis.
- `analyse-live` records by default and regenerates the Markdown log. It stores both the frozen input and output, including the participant names, state summary, lean and hashes.
- `record`, `settle` and `evaluate` regenerate the Markdown log after a successful journal append.
- `render-log` safely rebuilds the document from a verified journal.
- Never hand-edit the generated log to add, remove, repair or grade an entry. Append or correct the source record, verify the journal, then regenerate.
- Every delivered ranked list must have a structured `PUBLICATION` record containing the exact order, selection and line, verdict, rationale, potential winner and faithful public summary. The frozen research note retains the evidence narrative. If no formal selection was issued, the log must say `NONE — abstained` rather than inventing a quantitative pick later.
- Legacy v2–v4 rows remain labelled historical evidence and are not silently merged into current performance totals.

Recommended commands:

```powershell
node scripts/sportsctl.mjs new-request --input request.json --output packet.json
node scripts/sportsctl.mjs analyse-live --input live_request.json --output live_output.json
node scripts/sportsctl.mjs publish --input publication.json
node scripts/sportsctl.mjs render-log
node scripts/sportsctl.mjs verify-store
```

## 14. Retrospective learning and settlement

Before each new card, inspect the most recent recorded event. Ignore it if it is live, upcoming, abandoned without a final ruling, or still inside an official correction window. Never grade a live projection using an intermediate score.

For a final eligible event:

1. verify the official final state and event identity;
2. apply the exact frozen market and settlement convention independently to every issued selection;
3. append `WIN`, `LOSS`, `PUSH`, `VOID`, `UNGRADABLE` or `PENDING` with the official source and fetch time;
4. compare the frozen reasoning with what actually happened—data quality, state interpretation, lineup/exposure, market relation, model mechanics and source timing;
5. separate process quality from outcome luck;
6. record what was right, what was wrong and what remains unknowable;
7. treat lessons as hypotheses only. Do not change a model from one result, backfill post-event facts, or tune on a supposedly untouched period;
8. implement a change only through a versioned ticket, future chronological test, prospective shadow and reviewed release.

Report proper scores, calibration, baseline differences, risk/coverage and clustered uncertainty only for eligible quantitative ISSUE records. PASS/WATCH and qualitative analyses may be reviewed operationally but must not inflate win-rate or profitability claims.

## 15. Sport-specific operating instructions

The following instructions are mandatory boundaries, not permission to issue a numeric forecast. Every competition and market still needs an exact registered contract and ACTIVE coverage.

| Sport | Required modelling and evidence | Critical separation and failure conditions |
| --- | --- | --- |
| Soccer goals/results | Competition-specific attack/defence joint-score model; low-score dependence; official fixture, XI, roles, venue/rest and regulation rules | Regulation result, qualification, extra time and shootout are different targets; do not transfer xG definitions or strength across leagues |
| Soccer counts/player markets | Definition-stable event feed with minutes/opportunity, role and opponent/game-state exposure; negative-binomial, hurdle or joint count candidates | Corners, cards, shots, shots on target and player props are separate models; unconfirmed starter/minutes means PASS |
| Baseball | Starter/bullpen/lineup/handedness, park, weather and defence in a plate-appearance, inning or hierarchical run model | MLB, NPB, KBO, LMB and other leagues are separate; full game, first five, run line, total and NRFI are separate; resolve extras, suspended games and pitcher-change rules |
| Basketball | Possession and efficiency distribution with confirmed availability, minutes, usage, rest and late-foul/garbage-time/overtime branches | NBA, WNBA, FIBA and development leagues are separate; game, half, quarter, team and player markets require coherent but distinct exposure models |
| Cricket | Format/venue/phase model with official toss, XI, batting order, bowling allocation, pitch, boundary, weather, wickets and resources | Test, ODI, T20 and shortened formats do not pool automatically; first innings, chase, powerplay and player markets are separate; DLS/revised targets and reduced overs require explicit support |
| Australian football | Scoring-shot opportunity plus goal/behind conversion with final team, venue dimensions, roof/wind, territory and pressure | AFL and AFLW are separate; regulation winner, line, margin, total, team total and player markets need exact exposure and coherent margin/total structure |
| Ice hockey | Regulation joint-goal process with confirmed goalie/lines, 5v5 chances, special teams and empty-net tail | Regulation, moneyline including overtime, and shootout branches differ; NHL and IIHF rules/data definitions cannot be pooled without proof |
| American football | Drive/play scoring model with quarterback, line, skill-position availability, pace, field position, weather and overtime | NFL, NCAA and other rules differ; game, half, quarter, spread, total and player props require separate exposure/settlement support |
| Rugby league | Possession/set/field-position scoring process with official final team, completion, kicking, venue/weather, HIA and card state | NRL, NRLW, Super League and other competitions are separate; Golden Point and handicap/total settlement must be explicit; never substitute rugby-union data |
| Rugby union | Territory, possession, set piece and scoring-event process with official teams, replacements, cards, weather and exact laws | Fifteens, sevens, tens, youth and law trials are separate; knockout extra time and penalty/try mix require explicit modelling; never substitute rugby-league data |
| Tennis | Point-on-serve/player-surface model with official draw, order, format, surface, ball, altitude and withdrawal state | Retirement, walkover and dead-settlement rules must be frozen; singles/doubles, men/women and best-of formats are separate |
| Volleyball | Rally/serve-receive and set Markov model with official roster, format and venue | Indoor/beach, men/women, best-of and golden-set rules differ; variable match length and win-by-two branches must be explicit |
| Golf | Player-course-round model with field, tee time, course setup, weather and cut rules | Outright, placement, matchup and round props have different dead-heat, withdrawal and cut settlement; field changes require a new snapshot |
| Motorsport | Driver/car/track/session model with official entry list, grid, penalties, weather and session format | Practice, qualifying, sprint and race are separate; classification laps, disqualification and teammate/team markets require exact rules |
| Combat sports | Fighter/style/weight/round model with official bout status, weigh-in, format and judging rules | Moneyline, method, round and decision props are separate; cancellations, catchweights, replacements and no-contest rules must be frozen |
| Other or unsupported | Research and contract resolution only | No model inheritance by similarity; return PASS unless a reviewed scope is added |

### Player-market rule for every sport

Player props require verified participation, role and exposure as of the cutoff; the precise statistic definition; substitutions, overtime, abandonment and minimum-participation settlement; opponent and game-state context; and a player-specific validated model. Team strength or a player’s reputation alone is insufficient.

## 16. Active qualitative live models

Only these winner-lean scopes are currently `ACTIVE_ANALYSIS_ONLY`:

| Sport | Exact scope | Maximum source age | Inputs used | Exclusions |
| --- | --- | ---: | --- | --- |
| Baseball | MLB, NPB or KBO LIVE winner | 300 seconds | score, inning/half, outs, occupied bases | no LMB; no pitchers, lineup, park, weather, team rating, run line or total |
| Cricket | ODI, T20I, T20, WT20I or MLC second-innings standard-target chase | 180 seconds | target, score, wickets, legal balls, first-innings rate | no first innings, Test cricket, DLS/revised target, team/player markets |
| Soccer | FIFA, EPL, Bundesliga, UEFA Champions League or A-League LIVE winner | 180 seconds | score, elapsed regulation time, red cards | no xG, lineups, extra time, totals or props |
| AFL | AFL LIVE winner | 120 seconds | points, quarter and nominal time remaining | no AFLW, time-on, lines, totals or player markets |
| NRL | NRL LIVE winner | 120 seconds | points and elapsed regulation time | no NRLW/Super League, possession/field position, lines, totals or player markets |

The deterministic rules scale the current scoreboard state by remaining time or innings. Cricket additionally compares required rate and resource position; soccer applies only a bounded red-card adjustment; baseball applies a small late-bottom-inning base-state adjustment. Tied or near-balanced states return `TOSSUP`. `SLIGHT`, `MODERATE` and `STRONG` are ordinal rule outputs, not calibrated probability bands.

Every active-analysis run requires an approved official source ID and host, strict observation/fetch/as-of UTC order, freshness within the listed limit, a retained SHA-256 source hash and no duplicate or conflicting source. Unsupported competitions or states fail closed.

## 17. Analysis-only live path and its logging boundary

`ACTIVE_ANALYSIS_ONLY` accepts only the exact supported LIVE winner scopes above. It creates no candidate universe, probability distribution, calibration evidence, price evaluation or execution claim. Any request for probability, confidence percentage, odds, edge, expected value, stake or profitability must use the quantitative workflow and currently fails closed because that release remains suspended.

For complete history, every delivered qualitative analysis is now appended as `ANALYSIS_OUTPUT` with its frozen input to the same verified journal and rendered into `PREDICTION_RESULTS_LOG_v5.md`. Logging the lean does not turn it into a calibrated or calibration-eligible quantitative prediction.

## 18. Transfer and readiness checklist

To transfer the framework, copy this file plus the runtime, schemas, registries, templates and `PREDICTION_RESULTS_LOG_v5.md`. Before first use in the destination:

1. install dependencies and run `npm test`;
2. run `npm run validate` and `npm run verify-store`;
3. confirm the authority and release manifests agree;
4. confirm every active-analysis registry code/schema hash matches the copied files;
5. run `node scripts/sportsctl.mjs render-log` and compare its count/head with the journal;
6. retain the journal head hash and record count independently;
7. use the request-time runbook above for the next event.

The framework is ready only when these checks pass. Passing checks establishes integrity and the stated qualitative capabilities; it does not activate a quantitative model or guarantee a correct outcome.
