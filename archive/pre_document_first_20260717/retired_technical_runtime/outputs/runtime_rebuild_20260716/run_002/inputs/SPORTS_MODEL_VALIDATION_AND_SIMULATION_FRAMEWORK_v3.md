# Sports Model Validation and Simulation Framework v3

Effective: 2026-07-16  
Status: CANONICAL SPECIFICATION  
Operational status: **SUSPENDED — NO ACTIVE MODELS**

This standard implements the technical controls in `combined_sports_doc_v3.md`. It does not activate a model. `SPORTS_DEVELOPMENT_MODEL_CATALOG_v1.md` instantiates these rules as non-fitted DEVELOPMENT cards; those cards are not prediction artifacts. Activation requires an exact ACTIVE model card and ACTIVE coverage row plus every hard gate in `SPORTS_ACCEPTANCE_TESTS_v3.md`. `SPORTS_MODEL_COVERAGE_REGISTRY_v3.csv` currently contains no ACTIVE row.

## 1. Activation contract

Under **GATE-MODEL-001**, a quantitative ISSUE is allowed only when all of the following join exactly:

- sport, competition, market, target, settlement convention, forecast state, state bucket and horizon;
- `analysis_mode`, including a registered PRICE_ENABLED decision policy where applicable;
- model, data, feature, code and calibration artifact versions/hashes;
- candidate-universe and selection-policy versions;
- ACTIVE unexpired model card and ACTIVE unexpired coverage row;
- passed untouched-test and mandatory prospective-shadow reports;
- calibration, uncertainty, source, regression, drift and decision-policy gates.

If any join fails, freeze `decision=PASS`, `pass_reason=MODEL_UNAVAILABLE` (or the more specific failed gate) with null model/probability/edge/EV fields. A non-probabilistic research note may be supplied. Never substitute a qualitative numeric probability range.

## 2. Point-in-time data and target definition

For every historical and prospective observation preserve:

- official event/ruleset/settlement IDs and start time;
- exact target branch set, forecast state, state/horizon bucket and cutoff;
- feature values, definitions, latency, `known_at`, sources and artifact hashes;
- projected versus confirmed availability;
- candidate universe and primary-question status;
- outcome and corrections in separate append-only settlement records.

Historical features must reproduce production latency and missingness. Final lineups, revised injuries, later live states, closing prices, final weather, post-event statistics and score corrections are prohibited when unavailable at the historical cutoff. Modern retrieval of an as-of source must prove the historical version existed; otherwise the row is not eligible.

## 3. Development, split and spent-test design

### 3.1 Required chronological sequence

1. **Training:** estimate model parameters.
2. **Tuning folds:** rolling/expanding origins inside the development era for features, decay, hyperparameters, distribution and scenario design.
3. **Calibration:** later disjoint data used only for the registered probability mapping or identity-calibration justification.
4. **Untouched test:** a predeclared event/time manifest evaluated once after all model and decision choices freeze.
5. **Prospective shadow:** mandatory later forecasts generated exactly as production, frozen before events and not user-facing; activation requires its preregistered rule to pass.

Random future-to-past shuffling is prohibited. Season/era blocks and transfer assumptions must reflect rule/regime changes. Purge overlapping targets and information windows where labels or features cross a boundary.

### 3.2 Spent-test rule — GATE-TEST-001

The primary metric, baseline, minimum relevant effect, effective-N/precision rule, guardrails, event manifest and analysis code hash must be registered before any untouched outcome or aggregate is viewed. At first view the test becomes `SPENT` for the entire related hypothesis/model family, not merely one code version. A failure, feature change, threshold change, manual rule or additional challenger requires a new later untouched period. Repeated peeking, alternate-window selection and using the same external forecast as both fitting target and validator are prohibited.

Prospective shadow is not optional and cannot reuse the untouched historical test. “Consistent” means the exact preregistered shadow pass rule is met; it is not an analyst narrative.

### 3.3 Dependence and effective sample

Multiple markets from one event share latent state. Primary comparisons use event-level clustering; the model card must add time/participant/competition blocks when residual dependence remains. Card IDs never replace event IDs. Report unique events, clusters, effective N and the resampling unit. Nested last-5/10/15/20 windows are features, not independent confirmations.

## 4. Baselines, primary metric and promotion rule

Every model freezes before test:

- a credible naive/base-rate or transparent sport baseline on the identical eligible events;
- a no-vig market comparator for PRICE_ENABLED when a complete contemporaneous market exists;
- exactly one primary promotion metric, with other metrics as guardrails;
- a minimum practically relevant improvement and a confidence/posterior decision rule;
- minimum effective N or maximum interval width justified for the target;
- calibration, interval/tail and protected-segment non-inferiority/failure thresholds.

A challenger cannot choose the easiest of several baselines after results. It passes only if the primary comparison meets the preregistered effect and uncertainty rule and every guardrail passes. A positive point estimate with an interval that merely excludes a large deterioration is not “beats baseline.”

For probability targets, Brier and log loss must both be reported under `SPORTS_SCORING_SPECIFICATION_v3.md`; one is preregistered primary. Count/continuous models additionally report a proper distribution score, interval coverage/width and secondary point-error metrics. All comparisons use identical eligibility and weights.

## 5. Distribution selection

Choose distributions from sport mechanics and chronological out-of-sample performance, never the desired side of a line.

### 5.1 Poisson

For non-negative count `Y` with rate `lambda`:

`P(Y=k)=exp(-lambda)*lambda^k/k!`, with `E[Y]=Var(Y)=lambda`.

Poisson is a candidate when exposure is defined, events are reasonably homogeneous after conditioning and residual dispersion/dependence/tails are acceptable. It can be a transparent baseline for soccer/hockey goals and opportunity-conditioned props. It is usually only a benchmark for full-game baseball/cricket counts and compound high-scoring sports.

### 5.2 Alternatives

- Negative binomial, generalized Poisson or Conway-Maxwell-Poisson for dispersion.
- Hurdle/zero-inflated models for structural zeros.
- Bivariate/shared-state models for dependent team/opponent counts.
- Hierarchical/dynamic models for sparse or changing teams/players/competitions.
- Empirical bootstrap/mixtures for tails and regimes.
- Sport-native state models for possessions, drives, innings/balls/overs, points/games/sets, holes, survival/rank and duration.

Residual/tail calibration, zero frequency, dependence, stability, regime drift and interval coverage are diagnostics, not automatic threshold switches. Compare proper scores on frozen chronological holdouts.

## 6. Sport-native minimum development requirements

These requirements define model-card scope; none implies a current ACTIVE model.

| Sport/market | Required transparent baseline | Candidate challengers | Minimum state/feature coverage |
| --- | --- | --- | --- |
| Soccer goals/results | team attack/defence Poisson | Dixon-Coles; dynamic, bivariate or hierarchical score | XI/roles, venue/rest, regulation vs advance/ET/shootout, dependence and exact live state |
| Soccer counts/props | empirical/count regression | negative-binomial, hurdle/bivariate, opportunity/minutes | provider-stable definitions, style/opponent allowance, game state and exposure/minutes |
| Baseball | team/inning run baseline | plate-appearance/inning simulation; hierarchical run model | starter exposure, confirmed lineup/handedness, bullpen/park/defence, extras/ties/suspension; F5/full/NRFI separate |
| Basketball | possessions × adjusted efficiency | lineup/possession simulation; hierarchical distribution | lineup/minutes mixtures, shot/turnover/rebound components, rest, late fouling/garbage/OT; phases separate |
| Cricket | format/venue/phase baseline | ball/over wicket-state simulation; phase hierarchy/mixture | format/innings role, XI/roles/bowling allocation, pitch/boundary/weather, wickets, chase/DLS/truncation |
| Australian football | score/territory baseline | scoring-shot/conversion; hierarchical margin/total | final team, territory/pressure, venue/weather, goal/behind conversion and state-dependent tails; AFL/AFLW separate |
| Ice hockey | regulation goal baseline | dynamic/bivariate/negative-binomial state model | goalie/lines, xG, special teams, empty-net, regulation vs OT/shootout and exact live state |
| American football | team/drive baseline | play/drive simulation; hierarchical margin-total | QB/line, EPA, pace, weather, field position, clock and OT/rules branches |
| Rugby league/union | possession/scoring-event baseline | compound possession/score simulation | final team, territory/completion/kicking, HIA/cards, clock and extra-time rules; codes/leagues separate |
| Tennis/volleyball | point/rally baseline | point-game-set or rally-set Markov | surface/participant state, serve/return, format, win-by-two and variable match length |
| Golf/motorsport/combat | sport-native hole/rank/hazard baseline | hierarchical hole; survival/rank; bout hazard/duration | exposure, censoring, withdrawal/DNF and coherent result/rank constraints |

Transfer across leagues, men's/women's, senior/junior or rule variants requires validated hierarchical pooling and exact coverage. Otherwise the scope is UNSUPPORTED.

The corresponding versioned DEVELOPMENT cards, primitive-event engines, required feature/state contracts, diagnostics and exclusions are maintained in `SPORTS_DEVELOPMENT_MODEL_CATALOG_v1.md`. A catalog entry does not satisfy GATE-MODEL-001.

## 7. Features, recency and selection pipeline

Last-N summaries may be candidate features but their observations are nested. Choose decay/window parameters inside tuning only. Candidate features should cover, where relevant:

- opponent and competition strength;
- venue/home-away/neutral and rules context;
- stable priors with partial pooling;
- verified role/lineup/exposure;
- schedule/rest/travel/conditions with stable definitions;
- sport-specific opportunities and state, not raw outcome alone.

Register candidate features and transformations before the untouched test. Use shrinkage/regularization or preregistered multiplicity control. Post-event ideas wait for future test data.

Under **GATE-UNIVERSE-001**, model-selected forecasts must replay the complete candidate generator, all inspected/rejected candidates and the production selection threshold. Performance of published survivors alone is selection-biased and cannot activate a pipeline.

## 8. Calibration evidence

Fit calibration only on data after training and before test. Candidate methods include logistic/Platt, sufficiently supported isotonic, beta/hierarchical calibration or a documented identity mapping where a separate transform is not justified.

Every model stores `calibration_evidence_id`, status, method/version or identity justification, fit/evaluation periods, raw-versus-decision mapping, reliability counts/uncertainty and calibration intercept/slope where suitable. A value is not “calibrated” because raw equals decision probability or because average predicted probability resembles a small mixed observed rate.

Do not recalibrate on test/shadow events used for performance reporting. Do not create fine bins with tiny counts. Calibration is scoped by model/sport/competition/market/state/horizon; pooling requires prevalidated hierarchical structure.

## 9. Typed uncertainty — GATE-UNCERTAINTY-001

Keep distinct:

- aleatoric outcome distribution;
- parameter uncertainty;
- input/lineup/weather/pitch/state scenario uncertainty;
- structural/model uncertainty;
- calibration uncertainty;
- Monte Carlo numerical error;
- total uncertainty in the decision-driving probability.

Every ISSUE needs a quantified total probability interval with stated level/method plus an assessment of each material component in the data dictionary. A material `NOT_ESTIMABLE` component forces PASS. The decision policy must be rerun across declared scenarios/parameter/model draws; if ISSUE/PASS flips outside the registered robustness tolerance, pass or wait for the input.

A predictive interval for the outcome is not a confidence/credible interval for its probability. Probability display precision follows the total probability uncertainty and prospective calibration evidence, not the simulation draw count.

## 10. Simulation

Use exact CDF/PMF calculations when they answer the question. Simulate only for dependence, mixtures, state transitions, uncertainty propagation or complicated settlement.

For `N` independent Bernoulli draws and estimated probability `p_hat`:

`MCSE=sqrt(p_hat*(1-p_hat)/N)`.

This formula is invalid for correlated/MCMC draws without effective-sample/autocorrelation correction; quasi-random and weighted simulations need their appropriate estimator. Choose N to meet a preregistered numerical-error target for all decision-driving branches, then verify convergence by increasing N. A fixed logged seed supports reproducibility; alternate seeds diagnose implementation only and may not be selected for favourability.

Each simulation-run record stores model/data/feature/code/calibration hashes, generator/PRNG, seed, draw count/effective N, dependence method, parameters and their uncertainty-draw source, scenario/model weights, branch distribution, convergence criterion/result, numerical-error method, MCSE where applicable, sensitivities and artifact hash.

Monte Carlo error must be reported beside—not substituted for—parameter, input, structural and calibration uncertainty. A precisely simulated unvalidated model remains unvalidated.

## 11. Metrics and scoring

`SPORTS_SCORING_SPECIFICATION_v3.md` is authoritative for formulas, branch reconciliation, push/void treatment, eligibility, aggregation and test fixtures.

### 11.1 Probability distributions

- preregistered primary: Brier or log loss;
- both reported, plus baseline skill on identical events;
- reliability/calibration diagnostics with sample counts and uncertainty;
- discrimination only as a complement to calibration;
- complete WIN/LOSS/PUSH/VOID outcome branches where applicable.

### 11.2 Count/continuous distributions

- log score/deviance and CRPS where implemented;
- interval coverage and width at preregistered levels;
- MAE/RMSE only as secondary point summaries;
- market-relevant tail calibration.

### 11.3 Selection and decisions

- ISSUE/WATCH/PASS and abstention coverage for every request;
- complete candidate-pipeline selection/rejection coverage;
- primary question reported separately from secondary candidates;
- event-level weighting/clustering; no option-row pseudo-sample size;
- EV only from valid price packets; yield/P&L/CLV only from executions.

## 12. PRICE_ENABLED decision policy

PRICE_ENABLED is a separate registered production policy. Store the complete contemporaneous mutually exclusive price set, de-vig method, quote/expiry, limits, commission and branch payoffs.

All de-vig, branch-payoff, expected-return, execution, yield and CLV calculations must reproduce `SPORTS_SCORING_SPECIFICATION_v3.md`; they are not redefined in a model card.

The model card preregisters the conservative decision rule using the EV uncertainty distribution and model-risk allowance. Neither a positive point estimate nor a high win probability alone permits ISSUE as value. Staking requires a separate authorized risk policy and execution record.

## 13. Promotion, monitoring, suspension and rollback

### Promotion to SHADOW

Requires passed source/schema/leakage/regression checks, SPENT untouched-test report meeting the preregistered primary effect/uncertainty rule, all guardrails, exact artifacts and approval. It does not permit user-facing probabilities.

### Promotion to ACTIVE

Requires a later mandatory prospective-shadow report meeting its preregistered rule, exact ACTIVE coverage row, production decision-policy test, no unresolved incident, approval and expiry. The coverage registry is the final allowlist.

### Monitoring

Monitor exact homogeneous scopes, selection coverage, proper scores/baseline deltas, calibration/interval/tails, missingness/source failures and preregistered drift statistics. The model card specifies numeric window, minimum N, alert/suspend thresholds and response.

### Suspension and restart

Leakage, scope/artifact mismatch, broken definition, unresolved settlement error, regression failure or drift threshold breach immediately changes the model/coverage to SUSPENDED. Resume only as a new version with correction ticket, new later untouched evidence, new mandatory prospective shadow and approval. Never silently reactivate an old model.

## 14. Model card template

```text
MODEL ID / VERSION / OWNER / APPROVER / STATUS / EXPIRY:
SPORT / COMPETITION / MARKET / TARGET / SETTLEMENT:
ANALYSIS MODE / FORECAST STATE / STATE BUCKET / HORIZON:
CANDIDATE UNIVERSE / SELECTION POLICY / PRIMARY QUESTION RULE:
DATA SOURCES / LATENCY / LICENCE / SOURCE-MAP HASH:
FEATURE AVAILABILITY / MISSINGNESS / CUTOFF RULE:
TRAIN / TUNE / CALIBRATE / UNTOUCHED TEST EVENT-MANIFEST HASHES:
SPENT-TEST ID / FIRST VIEW TIME:
MANDATORY PROSPECTIVE SHADOW MANIFEST / REPORT:
NAIVE BASELINE / MARKET COMPARATOR:
MODEL / DISTRIBUTION / HYPERPARAMETERS / ARTIFACT HASHES:
CALIBRATION EVIDENCE / RAW-TO-DECISION MAPPING:
PRIMARY METRIC / MINIMUM EFFECT / EFFECTIVE-N OR PRECISION RULE:
CALIBRATION / INTERVAL / TAIL / PROTECTED-SEGMENT GUARDRAILS:
OUT-OF-SAMPLE RESULTS + EVENT/TIME CLUSTERS AND UNCERTAINTY:
TYPED UNCERTAINTY METHODS / ROBUSTNESS RULE:
ISSUE / WATCH / PASS POLICY:
PRICE_ENABLED EV POLICY (if applicable):
KNOWN LIMITATIONS / EXCLUSIONS:
DRIFT WINDOW / MINIMUM N / ALERT / SUSPEND / RETRAIN / ROLLBACK:
TEST / SHADOW / APPROVAL / COVERAGE IDS:
```

## 15. Research basis

- Proper scoring rules: https://doi.org/10.1198/016214506000001437
- Rolling-origin evaluation: https://pkg.robjhyndman.com/forecast/reference/tsCV.html
- Time-series cross-validation: https://robjhyndman.com/publications/cv-time-series/
- Dixon-Coles soccer score model: https://doi.org/10.1111/1467-9876.00065
- NIST Poisson reference: https://www.itl.nist.gov/div898/handbook/eda/section3/eda366j.htm
- Calibration metric/binning limitations: https://www.jmlr.org/papers/v23/22-0658.html

These sources establish general methods only. Each sport/market activation needs its own model card, data/source evidence and prospective report.
