# Algorithm portfolio and evaluation protocol
> **Current revision — CR-2026.09.21-3:** METHOD **MDS-2026.09.19-v4.3** is the workflow/template authority; **SCORING_AND_VALIDATION.md** controls conditioning, exact scoring, event-level evaluation and prospective evidence. All existing logs remain LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE. NUMERICAL_PROGRAM controls authorized implementation scope and actual build state; MODEL_IMPLEMENTATION_RECIPES contains the executable Markdown reference. Older dated policy blocks are historical where inconsistent. No source, dataset or model is approved/fitted by this banner.




> **`NUMERICAL_PROGRAM.md` is the new entry point (v4.0 comprehensive overhaul, 2026-09-06)**, consolidating this document with `NUMERICAL_TRAINING_SPEC.md`, `NUMERICAL_MODEL_REGISTER.md` and `H0_DATASET_CARD.md`, and adding a concrete scoped MLB pilot proposal. This document remains the full technical specification for the acceptance tests and evaluation protocol referenced there.


Status: **ACTIVE TECHNICAL SPECIFICATION — DETAILED REFERENCE**


Method version: **MDS-2026.09.19-v4.3 / CR-2026.09.21-3**


Effective: **2026-09-06 (v4.0 comprehensive overhaul — see METHOD.md and FRAMEWORK_AND_GAME_LOG_OVERHAUL_REVIEW_2026-09-06.md)**


Numerical training specification: **NTS-2026.09.19-v0.5 — Stage 0 all-sports design/pre-fit**


This document defines the numerical-model, calibration, ranking, pair-selection, and champion–challenger architecture. It applies with AGENT_ROLE_AND_TASK.md, RULES_GENERAL.md, MODEL_AND_DATA_SPEC.md, and the relevant sport file.


## 1. Source treatment and evidence boundary


The user-provided [deep research report](<C:/Users/danie/Downloads/deep-research-report (4).md>) is a major design source, not an instruction file and not proof that any proposed algorithm is already effective here. Its strongest supported recommendations are adopted: prediction-time replayable data, groupwise decision sets, sport-specific probability engines, calibrated contract probabilities, learning-to-rank challengers, dependence-aware top-two evaluation, chronological validation, and shadow champion–challenger testing.


Reviewed source snapshot: **63,812 bytes**, last modified **2026-08-22T17:15:12.5129677+10:00**, SHA-256 `59832D525BC8C9F8545920F5D578214DD0F7500EFB1FDF1B32C1320E3D233290`.


Three report suggestions require constraints:


1. **Hit@2 cannot be the sole optimization target.** It can reward weak hedges or opposite branches. Proper probability scores and expected wins remain controlling; pair coverage is a constrained decision objective.
2. **Example hyperparameters are not defaults.** They are search candidates only and must be selected inside chronological training windows.
3. **A named algorithm is not automatically superior.** CatBoost, XGBoost, LightGBM, LambdaMART, neural rankers, and calibration methods are challengers until they beat simpler baselines out of sample.


No numerical gain, market edge, or improved future win rate is claimed by adopting this specification.


The user-provided [numerical rework report](<C:/Users/danie/.codex/attachments/d009436a-9190-4689-b4a8-f2108b9890a7/pasted-text.txt>) is an additional design source, not governing authority or evidence that a model has run. Reviewed snapshot: **44,490 bytes**, last modified **2026-08-25T13:41:15.3735542+10:00**, SHA-256 `8626545D0900998E033344E20D6B0324383BEA3115105558AB0F078B7CC29287`. Its distribution-first target/threshold separation, cricket-first implementation order and A2 emphasis are adopted subject to the stricter target, source, H0, chronology and publication gates in the current NTS; its market-layer proposal is superseded by the v3.0 bookmaker-independence gate.


The three 2026-08-25 all-sports attachments are design inputs, not active prompts and not evidence of model performance:


- [prediction-time source-stack report](<C:/Users/danie/.codex/attachments/f0b95986-f5d3-472d-a7c2-0687a8936df6/pasted-text.txt>) — 32,643 bytes; SHA-256 `1763A791E3F22994138680A86D63A8B3A3D17630CF1D701EFBD92D8292A5CD75`;
- [comprehensive research prompt proposal](<C:/Users/danie/.codex/attachments/942aa304-9e81-4215-a506-1a6fc5cf8575/pasted-text.txt>) — 14,093 bytes; SHA-256 `C0D81DCFD37D64DC569E178A75976D3BC9FF3AE4F3F5278AA916EAC7B6B33D55`;
- [event-level distribution and market-layer report](<C:/Users/danie/.codex/attachments/74cb7fb8-bb0d-4345-bc87-70776d588a1a/pasted-text.txt>) — 17,232 bytes; SHA-256 `6F3A6307294512E3CCE50E1AD0B2798F1815D50A4527E63C5CD158C3A4B50E8C`.


Adopted: field-specific source ownership, volatile-facts-first web research, event/target-level distributions, systematic event populations, dependence groups, sports-only market-blind modelling, and proper-score evaluation. Not adopted or now retired: market-informed predictive tracks, permanent trust in named websites, unrestricted scraping assumptions, illustrative probabilities, post-hoc alternate-line selection, or a claim that one algorithm is best before chronological tests.


## 2. Objective hierarchy


The system solves three related but distinct problems.


| Layer | Question | Controlling objective |
|---|---|---|
| Probability | What is the distribution of the event and the win/push/loss probability of each exact contract? | Out-of-sample proper score, calibration, sharpness, and distribution coverage |
| Ranking | Which supplied eligible contracts are strongest individually? | Calibrated marginal `P(WIN)`, with lower `P(LOSS)`, evidence quality, and robustness as predeclared tie-breakers |
| Optional portfolio | If the user explicitly requests top-two coverage rather than a pure ordinal list, which two strong contracts provide useful coverage without metric gaming? | Expected wins first; union-win probability only among near-equivalent legal pairs |


The probability layer first estimates one exact underlying target distribution. Contract W/P/L probabilities are integrations over that object; bookmaker thresholds do not define separate primary models.


This remains a sports-only win-likelihood ranking, not expected value. Prices and bookmaker-derived information are excluded from predictive builds. An explicitly requested post-freeze price audit is a separate record and cannot change forecasts or ranks.


### 2.1 Required scorecard


Model promotion is controlled by probability quality. Decision metrics are important guardrails, not substitutes for calibration.


| Priority | Metrics |
|---|---|
| Primary probability | Binary or multiclass log loss; Brier score; CRPS for score/resource distributions |
| Primary calibration | Calibration intercept and slope; reliability curve with counts and uncertainty; interval coverage and width |
| Primary decision | Rank-1 win rate; Wins@2; NDCG@2 and NDCG@4 |
| Secondary decision | Hit@2, conditional Recall@2, pair Brier, exact-pair ordering; Precision@2 may be shown but equals Wins@2 divided by two whenever exactly two picks are selected |
| Candidate generation | WinnerAvailable, OracleWins@2, oracle regret, supplied-universe coverage, full-market coverage when observable |
| Optional post-freeze price audit | Descriptive terms/price comparison only when expressly requested; excluded from model promotion and forecast revision |


AUC and PR-AUC are secondary discrimination diagnostics. They cannot establish good top-of-list ordering or calibration.


## 3. Dataset roles and firewalls


| Dataset role | Contents | Permitted use | Prohibited use |
|---|---|---|---|
| D0 | P-001–P-060 historical log | Process, schema, error taxonomy, settlement tests, causal feature hypotheses, adversarial cases, and mechanism retrieval | Numerical coefficients, target rates, hyperparameters, calibration, validation, or claimed lift |
| H0 | Source-derived historical feature store | Numerical training and rolling-origin development when every feature is point-in-time reconstructable | Later lineups, corrected/final statistics, closing prices, inferred availability, or any field without prediction-time provenance |
| E1-Q | Qualitative issued cards, including USER_CONFIRMED_PREGAME_FREEZE history; preserve each issued method and separate live views | Historical directional/ranking evaluation, including process mistakes; D0 has a separate development role | Claiming validation/calibration of a model designed after these outcomes were observed |
| E1-Q-LATE_IMPORT | Historical administrative label; superseded for existing non-live cards by the September 5 user confirmation | Preserve original import evidence and append correction; new unconfirmed imports retain a provenance question | Misrepresenting a late local copy as proof of late forecasting, or inventing an independent timestamp |
| E1-P | Future predeclared probabilistic shadow cohort beginning only when a numerical challenger actually runs | Immutable shadow probability and ranking evaluation | Using earlier E1-Q outcomes as same-version calibration/test data or editing a frozen prediction |
| TRAIN-r | Earliest H0/E1 observations for rolling origin `r` | Fit model and preprocessing | Tuning on later outcomes |
| TUNE-r | Later disjoint block | Hyperparameters, early stopping, feature selection, candidate calibrator choice | Final performance claim |
| CAL-r | Later disjoint block | Fit the already-selected final calibrator or pair calibrator | Base-model or feature fitting |
| TEST-r | Latest untouched block | One-time model comparison | Any fit, selection, or repeated peeking |


E1 observations are not permanently one role. When earlier prospective cases are eventually used for training, they are spent for that purpose; a later untouched block must test the revised method. E1-Q does not silently become E1-P.


### 3.1 H0 dataset card


H0 cannot be built under this Markdown-only update; a future numerical implementation requires explicit user authorisation. H0_DATASET_CARD.md now preregisters design-only target populations for every dedicated sport but remains `NOT BUILT / NOT QUALITY-APPROVED`. Before any H0 row is fitted, its card must contain:


| Field | Required content |
|---|---|
| Dataset ID/version/as-of | Stable build identity and cutoff |
| Intended use | Exact probability, distribution, ranker, or calibration role |
| Homogeneous population | Sport, competition/rules era, market family, and pregame/live horizon |
| Grain/key | Event, view, decision set, candidate, and contract key |
| Inclusion/exclusion | Events, seasons, markets, data-quality gates, voids, and exceptions |
| Candidate policy | Supplied slate or versioned generator, universe close time, coverage limitations |
| Time semantics | Effective, known/published, observed, accessed, cutoff, and settlement rules |
| Sources/definitions | Provider ownership, version, coverage, known lags, and conflicts |
| Feature manifest | Feature/transform versions, units, shrinkage, missingness, and leakage tests |
| Label manifest | Official settlement source/version and W/P/L/VOID/UNSETTLEABLE policy |
| Dependence/duplicates | Alias rules, event/view grouping, normalized weights, and duplicate hashes |
| Selection limits | User-selection bias, unavailable markets, survivorship, and coverage gaps |
| Split manifest | Chronological TRAIN/TUNE/CAL/TEST dates and event grouping |
| Quality results | Completeness, uniqueness, temporal, range, join, drift, and negative-control checks |


If `known_at` cannot be established as no later than the applicable forecast cutoff, the historical feature is missing. “Likely available” is not sufficient provenance.


### 3.2 Shadow probability requirement


`probability_generated` and `probability_published` are separate.


- A validated model may publish calibrated probabilities.
- An unvalidated numerical challenger may store **SHADOW** probabilities before the result, while the user-facing card remains `NOT PUBLISHED — VALIDATION PENDING`.
- A model that does not exist or did not run records `NOT_GENERATED`; no probability may be invented to fill a field.
- Shadow outputs are immutable and proper-score eligible only when their method, data cutoff, candidate universe, and timestamp were frozen before settlement.


This resolves the cold-start problem: prospective calibration evidence can accumulate without exposing unvalidated numbers.


## 4. Canonical numerical data grains


The distribution engine and contract engine use two linked grains.


1. **Underlying target prediction:** one exact target at one frozen state for one model build:


   `event_id → view_id → state_snapshot_id → target_id → model_build_id`.


2. **Derived contract:** one settlement query linked to that stored distribution:


   `decision_set_id → candidate_id → canonical_contract_id → distribution_prediction_id`.


Ten thresholds for the same target create ten derived contract rows but only one underlying prediction row. They do not create ten independent training examples or ten independent target fits.


The event enumeration grain is separately frozen. A numerical build uses every eligible event in a preregistered competition/date/rules population, subject only to predeclared quality exclusions. User-requested or visually interesting events are a selected issuance sample and cannot define H0 or TEST. Alternate-line evaluation uses a versioned grid or all mathematically supported thresholds fixed before outcomes; it is never selected after the forecast or result.


Required identifiers and controls:


| Domain | Required fields |
|---|---|
| Identity | append sequence, official event ID, view ID, state snapshot ID, target ID/version, decision-set ID, candidate ID, canonical contract ID, alias-of ID |
| Candidate generation | origin, policy version, universe frozen time, complete-universe flag, universe type, eligibility, exclusion reason |
| Time | request, effective, published/known, observed, accessed, cutoff, issue, and settlement timestamps |
| Contract | sport, competition/rules era, market family, phase, metric, operator, line, win/push/loss intervals, OT/extra-time terms |
| Feature provenance | atomic evidence-unit and upstream-lineage ID, exact source record/snapshot/URL, claim owner, definition and transformation versions, effective/known/observed/access times, feature age, source tier, conflict count and missingness code; for decision-driving roles, official event/team/role/participant tuple and release status |
| Model provenance | code/data/feature/model/simulator/calibrator versions or hashes |
| Dependence | group, relation type, covariance/correlation, joint-win probability, dependence method version |
| Prediction | underlying PMF/CDF/posterior-sample reference, support, raw/calibrated distribution, scenario/parameter uncertainty, OOD and display status |
| Contract integration | exact W/P/L intervals, raw/calibrated W/P/L vector, distribution reference, integration/coherence version and marginal rank score |
| Pair | pair ID, legality, exclusion reason, expected wins, joint-win probability, union-win probability, selector version |
| Label | official W/P/L/VOID/UNSETTLEABLE, final value, source, boundary flag, settlement version |
| Evaluation | block/cohort, controlling-view flag, performance role, model eligibility, exclusion reason |


Raw source snapshots and final labels remain separate immutable tables conceptually. A point-in-time join creates features; the label joins only after settlement.


## 5. Feature architecture


### 5.1 Sport-native rate and exposure


Numerical features implement the relevant sport file: participants, role, expected exposure, opponent-adjusted rate/process quality, venue, rest/workload, state, and explicit tails. No generic cross-sport last-five score vector replaces this layer.


Dynamic Elo/Glicko-style overall, offence, defence, venue and regime ratings are candidate feature families and simple baselines, not the universal forecasting backbone. Rebuild them inside each chronological fold. Recent form uses preregistered multi-horizon and time-decayed candidates, with regime breaks, rather than a fixed last-five/last-ten rule selected after seeing TEST.


The feature row must also carry the exact target ID, start state, endpoint, exposure and termination definition. A feature set for named-day output is not automatically valid for innings-total output.


### 5.2 Contract geometry


Store line value, integer/half status, push interval, regulation/extra-time treatment, standardized distance from the event distribution, nested-line relation, exact complement, overlap/gap width, phase/full relation, and sport-specific key values.


### 5.3 Evidence and uncertainty


Store availability entropy, exposure variance, source age, missingness indicators, source conflicts, model disagreement, scenario dispersion, live-feed age, and out-of-distribution flags. Missingness is information only when its status was known at prediction time.


### 5.4 Dependence


Store same event/team/player/phase, market-family relation, shared causal thesis, exact complement, nested/overlapping/gapped geometry, simulator covariance, `P(both win)`, and `P(any win)`.


### 5.5 Feature safety


- Every feature requires `known_at <= cutoff_at`.
- Fit imputers, encoders, scalers, target statistics, feature selection, calibrators, and stackers inside each chronological fold.
- CatBoost ordered categorical handling is a challenger, not a replacement for time separation.
- Never globally target-encode team, player, coach, venue, or competition before splitting.
- Do not blindly winsorize genuine red-card, wicket-collapse, HR-cluster, blowout, overtime, or sin-bin tails.
- `NOT_CHECKED` is an analyst-process failure and is audit metadata, never a predictive feature. Other missingness states are challengers only when known at cutoff and justified mechanistically.
- D0 result labels may identify a candidate feature family but cannot supply the feature's numerical weight.


### 5.6 Feature admission card


Every numerical feature or feature family requires a frozen Markdown record before it enters a challenger:


| Field | Required definition |
|---|---|
| Feature ID/version | Stable name and transformation version |
| Target and population | Sport, competition/rules population, market, phase, and horizon |
| Role | Causal-process measure, proxy, context, uncertainty, geometry, or audit-only |
| Definition/unit | Numerator, denominator, unit, aggregation grain, and valid range |
| Expected direction | Sign or monotonic relation when defensible; otherwise explicitly unconstrained |
| Provenance | Provider, definition version, effective/known/access times, and expected lag |
| Missingness | Permitted codes, imputation rule, missingness indicator eligibility, and fallback |
| Adjustment | Opponent, venue, era, exposure, decay, shrinkage, and regime treatment |
| Leakage test | Point-in-time assertion and any target-encoding safeguard |
| Admission test | Chronological ablation metric, guardrails, comparator, and review block |


Training split counts or tree split importance are not evidence that a feature generalizes or causes the outcome. Use held-out permutation importance and feature-family ablation only after the underlying model has predictive skill, report uncertainty, and note that correlated features can mask one another. A feature enters the champion only through the challenger promotion protocol.


## 6. Algorithm portfolio


The simplest qualified algorithm is champion. Every more complex method is a frozen challenger on identical point-in-time inputs.


| ID | Algorithm | Role | Promotion requirement |
|---|---|---|---|
| A0 | Competition/venue prior, conditional empirical CDF, and simple rate × exposure; Poisson where relevant as a diagnostic | Mandatory naïve and distribution baselines | Never removed |
| A1 | Regularized/hierarchical GLM or distributional regression, including target-appropriate negative-binomial, location-scale or GAMLSS-style candidates | First interpretable numerical distribution baseline | Improve over A0 in rolling-origin distribution score, contract proper score and calibration |
| A2 | Sport-specific generative joint simulator | Central architectural candidate for coherent score/resource, contract, tail, transition and dependence probabilities | Improve distribution score/coverage and contract proper scores with valid state/termination behavior |
| A3 | Categorical-heavy nonlinear rate/distribution-component or NGBoost-style distributional challenger | Nonlinear conditional-distribution challenger; not unrelated threshold heads | Leakage-safe categorical processing, valid support and out-of-sample distribution improvement |
| A4 | XGBoost/LightGBM tabular component, ordered-CDF, or joint non-crossing quantile challenger | Flexible distribution approximation or simulator correction | Same folds/targets as A1–A3; valid monotone CDF and calibrated final output |
| A5 | LambdaMART/RankNet groupwise ranker | Within-decision-set ordering challenger | Sufficient independent decision sets; improve NDCG@2/@4 without probability harm |
| A6 | Regularized chronological sports-only stacker | Blend A1–A5 sports/environment inputs | Out-of-fold inputs only; beat best component on untouched test |
| A7 | Optional constrained top-two portfolio selector | When explicitly requested, choose an unordered legal pair from calibrated marginals and joint dependence | Pair Brier and decision metrics validated prospectively; never silently changes the ordinal rank objective |
| A8 | Neural embeddings/listwise ranker | Deferred research challenger | Large stable H0; material improvement over boosted-tree ranker |


For every sport, maintain only the `SPORTS_ONLY / MARKET_BLIND` predictive lane. `MARKET_ONLY_BASELINE` and `MARKET_INFORMED` are retired from active, shadow and promotion-eligible modelling under v3.0. Historical design text remains evidence only; bookmaker/operator material is limited to exact supplied contract/terms and an explicitly requested post-freeze descriptive price audit.


Long-term design principle: **A2 generates the coherent underlying outcome distribution; A1/A3/A4 challenge, approximate, or correct it.** A2 is not promoted by this sentence and can lose to a simpler qualified model.


No model family receives permanent priority by reputation. CatBoost is attractive for high-cardinality categorical inputs; NGBoost is a candidate for distributional boosting; XGBoost and LightGBM can estimate state components, ordered buckets or non-crossing quantiles; regularized models remain essential leakage and overfit checks. Independent Over/Under classifiers may be retained only as diagnostic comparators and may not control production probabilities unless reconciled into one validated CDF.


### 6.1 Hierarchical and dynamic structure


Within defensible populations, use:


`competition/rules era → team/venue/regime → player/role → current exposure`.


Compare complete pooling, no pooling, and partial pooling on identical folds. Sparse entities should shrink more than well-supported entities. Coach, role, roster, rules, venue, and season changes create explicit regime indicators or state uncertainty; they do not justify arbitrary history deletion.


### 6.2 Scenario mixture and simulation accuracy


The event distribution is:


`P(event) = Σ_s P(scenario s) × P(event | scenario s)`.


Scenario weights must be estimated from H0 or remain qualitative. Simulations continue until Monte Carlo uncertainty in decision-driving contract probabilities is below a predeclared tolerance; store seed, draws, standard error, and convergence check. A large draw count cannot repair a misspecified event model.


## 7. Probability and settlement heads


The production path models the underlying target distribution and integrates it across exact settlement intervals. For integer target `Y` with `F(k)=P(Y<=k)`, a half-unit Over is `1-F(k)` and the matching Under is `F(k)`. For integer or other push-capable contracts, preserve the distribution's exact boundary mass in a coherent W/P/L vector.


Direct binary win/loss heads at selected half-point lines are diagnostic challengers only. They may not replace the shared CDF, and separately calibrated nested lines may not control publication because they can violate complement and monotonicity constraints.


Required outputs:


- `p_win_raw`, `p_push_raw`, `p_loss_raw`;
- `p_win_calibrated`, `p_push_calibrated`, `p_loss_calibrated`;
- `distribution_prediction_id`, target ID/version, support and contract-integration version;
- each vector bounded in `[0,1]` and summing to one;
- VOID and UNSETTLEABLE excluded from predictive outcome scores under a frozen policy;
- ranking relevance defaults to WIN=`1`, otherwise=`0`; any push utility is a separate predeclared decision experiment.


Class weights, focal loss, or imbalance sampling are challengers only after support is measured by homogeneous slice. Retain an unweighted baseline and recalibrate the final output because weighting can distort probability estimates. Synthetic oversampling may not mix unrelated sports, competitions, seasons, market families, events, or correlated contracts.


## 8. Groupwise ranking


`decision_set_id` is the query/group ID. In the present workflow, the candidate universe is every user-supplied legally rankable row plus any distinct model-proposed candidate explicitly permitted by the request. Do not invent a complete sportsbook universe. If a future candidate generator exists, freeze its separately versioned full output, including unselected candidates; selected recommendations alone are a biased ranker dataset.


The first ranker challengers are:


1. XGBoost `rank:ndcg`/LambdaMART and RankNet-style `rank:pairwise`;
2. LightGBM `lambdarank` or `rank_xendcg`;
3. CatBoost LambdaMart, YetiRank, PairLogit, or groupwise alternatives;
4. neural ListMLE/ApproxNDCG only after the dataset is large enough.


Tune group construction, tree complexity, regularization, learning rate, pair sampling, and top cutoff chronologically. For top-two emphasis, search a cutoff slightly above two as a candidate; never hardcode report example settings.


Ranker scores are relevance scores, not probabilities. The probability head controls probability statements and pair calculations.


## 9. Optional constrained top-two portfolio


The ordinary ranked table always orders candidates by marginal win likelihood and the frozen tie-breakers in §2. A pair optimizer selects an **unordered portfolio** and may be used only when the user explicitly requests top-two coverage or portfolio diversification. It never silently redefines rank #1 or rank #2.


For candidate pair `(i,j)`:


`ExpectedWins(i,j) = p_i + p_j`


`AnyWin(i,j) = p_i + p_j - p_ij`, where `p_ij = P(i wins and j wins)`.


The joint must satisfy `max(0,p_i+p_j-1) <= p_ij <= min(p_i,p_j)`. A violation fails the prediction record; never clip an incoherent joint probability into range.


Dependence changes AnyWin but not expected win count. To prevent coverage gaming in the optional portfolio:


1. enumerate legal pairs only;
2. find the pair with maximum ExpectedWins;
3. define a predeclared tolerance `epsilon` around that maximum;
4. only within that near-equivalent set, choose the pair with maximum calibrated AnyWin;
5. default `epsilon = 0` until rolling-origin evidence supports a non-zero value.


Illegal top-two pairs include aliases, duplicate canonical contracts, and opposite sides of the same exact decision. Integer complements, nested alternatives, phase/full relations, and shared-thesis pairs receive explicit geometry/dependence treatment and cannot be used to manufacture guaranteed coverage.


Store the ordinary **marginal rank** and, only when requested, a separate **portfolio-selected** flag. The optimizer does not create an alternative ordinal rank. Before A7 is validated, AnyWin is diagnostic only. A materially weaker candidate cannot be selected merely for diversity.


## 10. Calibration protocol


The chronology is always:


`train → tune/select → fit final base/ensemble → calibrate on CAL-r → evaluate once on TEST-r`.


For an outcome distribution, first challenge calibration of the full CDF or a shared monotone transformation. Threshold-specific calibration is admissible only as research: it must be reconciled through a frozen coherence method, pass complement/nesting tests, and be re-scored as one final distribution. Independent calibrators per bookmaker line are not a production shortcut.


Calibrate the final ensemble, not only its components. Candidate methods:


| Method | Default role |
|---|---|
| Logistic/Platt recalibration | First binary method at modest effective sample size |
| Temperature scaling | First low-parameter multiclass/logit challenger |
| Beta calibration | Binary challenger when sigmoid shape is inadequate |
| Isotonic | Large-sample challenger; avoid with small effective samples and audit ranking ties |
| Dirichlet/multinomial recalibration | Later W/P/L challenger with sufficient data |


Do not use a universal calibrator across incompatible sports and horizons. Prefer the simplest defensible pooling level, with hierarchical calibration as a challenger for sparse related slices. Report both aggregate and sport × competition × market × pregame/live calibration.


Pair union probabilities require their own reliability assessment and pair Brier score. Do not calculate `AnyWin` from uncalibrated marginals and an unvalidated joint model as if it were a published probability.


If the feature vector is materially outside H0/CAL support, the model/version is missing, or calibration has drifted beyond a predeclared gate, set probability display to **SUPPRESSED** and fall back to the qualitative corridor.


## 11. Chronological validation and metric definitions


All rows and views from one event stay in the same fold. Pregame and live horizons are separate models or explicit strata. Preprocessing is refit within every origin.


### 11.1 Decision-set metrics


For decision set `g` with top-two set `S_g`:


- `Hit@2_g = 1` if at least one selected contract wins, else `0`;
- `Wins@2_g = number of selected wins`;
- `Precision@2_g = Wins@2_g / 2` when two candidates are eligible;
- `Recall@2_g = selected wins / all eligible winning candidates`, reported only when at least one eligible winner exists;
- `WinnerAvailable_g = 1` when the frozen candidate set contains any winner;
- `OracleWins@2_g = min(2, eligible winning candidates)`;
- `PairBrier_g = (q_any_win - Hit@2_g)^2` only when `q_any_win` was issued in shadow or published form before the result.


NDCG@2 and NDCG@4 use groupwise binary relevance and state the treatment and denominator for no-winner groups. Do not substitute single-label multiclass `top_k_accuracy_score`.


When exactly two candidates are always selected, Precision@2 is a fixed rescaling of Wins@2 and adds no independent information. Hit@2 on ordinary ranks must disclose `DEPENDENT_TOP2` when ranks one and two share a dependence group; optional portfolio coverage is evaluated only for legal distinct-contract pairs under §9.


### 11.2 Probability and distribution metrics


- binary Brier and log loss for no-push win probabilities;
- multiclass Brier and log loss for W/P/L vectors;
- CRPS/ranked probability score plus empirical interval coverage and width for score/resource distributions;
- log score and discrete PIT/randomized-rank calibration for ordered count distributions, with zero-density tail failures disclosed;
- calibration intercept/slope and reliability bins with counts and uncertainty;
- sharpness alongside calibration;
- baseline-relative skill, never score alone.


Every independent decision set receives equal total evaluation weight by default. Multiple candidates, views, or dependence groups do not inflate effective sample size. Use paired event-level bootstrap intervals and date/week blocks when temporal dependence matters.


### 11.3 Candidate-generation ceiling


Report supplied-universe and full-market coverage separately. A ranker cannot select a winner absent from its candidate set. If the user supplied exact complements, WinnerAvailable may be mechanically high and must not be presented as evidence of candidate-generation quality.


## 12. Champion–challenger governance


Before a comparison block opens, freeze:


- champion and challenger IDs;
- code/data/feature/model/simulator/calibrator versions or hashes;
- eligible population and candidate-generation policy;
- shared source snapshot and cutoff policy;
- primary score, decision guardrails, slice guardrails, and minimally useful effect;
- sample horizon or information-based stopping rule;
- missing-data, operational-failure, promotion, rollback, and multiple-challenger policy.


Run challengers in shadow mode first. The champion alone controls publication. A viewed test block is spent: any feature, model, tolerance, calibrator, or threshold change requires a later untouched block.


Promotion requires:


1. all identity, time, label, fold, and probability integrity checks pass;
2. primary proper score improves with decision-useful uncertainty;
3. calibration is non-inferior and no critical slice is materially harmed;
4. rank/decision guardrails are non-inferior, with any claimed gain supported at decision-set grain;
5. complexity, latency, source fragility, and missing-data behavior are acceptable.


A Hit@2 gain cannot promote a materially less calibrated model. A calibration gain cannot excuse unusable rank deterioration. No automatic retraining occurs after a short losing sequence.


## 13. Monitoring and drift


| Layer | Monitor |
|---|---|
| Input | Feature distributions, category mix, missingness, source age, conflicts, out-of-distribution rate |
| Model | Raw/calibrated probability distribution, rank score, model disagreement, simulation error |
| Calibration | Reliability, intercept/slope, Brier/log loss, pair Brier, interval coverage |
| Decision | Rank-1, Wins@2, Hit@2, NDCG@2/@4, pair redundancy, oracle regret |
| Slice | Sport, competition, market family, pregame/live horizon, evidence quality, support decile |
| Operations | Source failures, late lineups, settlement delays, model/version mismatch, suppressed outputs |


Drift triggers investigation or recalibration review under a frozen policy; it does not automatically change weights. Distinguish data drift, label drift, calibration drift, and genuine performance drift.


## 14. Automated acceptance checks


1. Unique key: `(event_id, view_id, decision_set_id, candidate_id, model_build_id)`.
2. Temporal: `known/accessed/observed <= cutoff <= issued`; later facts fail ingestion.
3. Fold: one event never crosses train/tune/calibrate/test.
4. D0 firewall: no D0 result-derived value enters numerical fitting.
5. Universe: frozen before issue; selected candidates are a subset; ranks are unique and contiguous.
6. Alias/dependence: aliases are one observation; decision-set/event weights normalize correlated rows.
7. Probability: W/P/L vectors are finite, bounded, and sum to one.
8. Calibration: fit and test rows are disjoint; method/version and dates exist.
9. Contract: intervals are exhaustive and noncontradictory; push and overtime rules replay correctly.
10. Monotonicity: a higher nested Over cannot have greater win probability than its lower Over; analogous handicap/Under checks apply.
11. Pair bounds: `max(0,p_i+p_j-1) <= p_ij <= min(p_i,p_j)` and AnyWin lies in `[0,1]`.
12. Anti-gaming: illegal complements/aliases cannot fill top two.
13. Metric grain: independent event/decision-set count is displayed beside every result.
14. Champion parity: all compared models share the same cutoff, source snapshot, and candidate universe.
15. Preserve the original prediction/model record and record its freeze basis. Existing non-live qualitative cards use USER_CONFIRMED_PREGAME_FREEZE. A numerical shadow/test build still requires its own recorded prediction-time output; no backfilled output can validate it.
16. Negative control: a deliberately future-dated feature must fail; implausibly strong shuffled-time performance triggers a leakage audit.
17. Simulation: seed, draws, Monte Carlo error, and convergence status exist when simulation controls a rank.
18. Publication: unvalidated shadow probabilities remain unpublished; missing runs remain NOT_GENERATED.
19. Target identity: target ID/version, unit, start state, endpoint, exposure and termination are frozen; named-day and innings-total labels cannot mix.
20. Distribution support: PMF/CDF is normalized, monotone and target-feasible; invalid continuous negative/fractional mass is removed by the frozen model, not ignored at display time.
21. Quantiles: any quantile representation is non-crossing and has versioned interpolation and tail rules before contract integration.
22. Exposure/termination: weather/no-play, early completion, declaration, innings switch, overtime or other sport-specific endpoints follow the target card and reconcile in simulation tests.
23. Shared calibration: calibrated nested thresholds still derive from one coherent CDF and retain complement/push identities.
24. Population: every H0/TEST event comes from the frozen eligible universe; user selection and post-hoc market selection cannot enter the evaluation population.
25. Bookmaker independence: the predictive feature manifest is `SPORTS_ONLY / MARKET_BLIND`; market-derived, bookmaker, affiliate and tipster inputs are absent and the independence check is recorded.
26. Source permission: numerical ingestion is blocked unless the source card approves the exact field, access method, retention/use and snapshot behavior.
27. Pregame time: `cutoff_at < scheduled_start_at`; otherwise the row is a distinct verified live target, a fail-closed no-action state, or final/no forecast.
28. Evidence lineage: one underlying event/upstream feed has one evidence-unit weight even when exposed through several features or front ends.
29. Corridor/threshold: every qualitative line records below/inside/above-central relation and supported ordinary branches on each side; an inside-corridor row cannot carry greater-than-LOW evidence without a frozen mixture basis.
30. Aggregate budget: team/phase component thresholds reconcile to the joint target; a one-component suppression feature cannot silently force the aggregate direction.


## 15. Implementation sequence


| Stage | Deliverable | Numeric publication |
|---|---|---|
| S0 — active now | NTS target/model design plus source, H0 and model Markdown registries; no data or fit | Disabled |
| S1 | Approve sources and freeze one pilot sport/target population; no source is admitted site-wide | Disabled |
| S2 | Build and quality-audit that pilot H0 with systematic event enumeration and complete point-in-time joins | Disabled |
| S3 | Fit empirical/simple and A1 distributional baselines, then the sport-specific A2 simulator on identical folds | Disabled |
| S4 | A3/A4 distributional, ordered-CDF and non-crossing-quantile challengers with rolling-origin OOF archive | Disabled |
| S5 | Shared-CDF/final-ensemble calibration and one-time untouched TEST | Only if every target-specific publication gate passes |
| S6 | Immutable E1-P shadow deployment and scheduled champion decision | Disabled during shadow; later version-specific |
| S7 | A5 ranker and A7 pair selector only after sufficient independent decision sets | Probability publication unchanged; pair probability requires its own gate |


Neural embeddings and listwise models remain deferred until independent decision-set counts, categorical support, and holdout evidence justify their complexity.


## 16. Current model card


| Field | Current state at v3.0 activation |
|---|---|
| Published numerical model | None |
| Current published output | Qualitative scenario corridor and ordinal ranking |
| D0 role | Process and representation learning only |
| H0 status | NOT BUILT / NOT QUALITY-APPROVED |
| E1-Q status | Use README to identify the active log and only that log's top controlling snapshot for volatile queue/cohort counts; user-confirmed non-live cards are admitted by issued method, including process defects; live views and unscorable endpoints are separate under PERFORMANCE_ELIGIBILITY_POLICY.md |
| E1-P status | NOT STARTED; begins only with a frozen, actually running numerical shadow model |
| Champion | A0 qualitative rate × exposure process |
| Numerical challengers | Specified but NOT TRAINED / NOT VALIDATED |
| Numerical training program | NTS-2026.09.02-v0.3 Stage 0 all-sports design/pre-fit; model candidates are registered but DATA BLOCKED |
| Calibration | NOT FIT / NOT VALIDATED |
| Pair selector | Optional portfolio specification only; not active ordinal policy |
| Bookmaker-input state | PROHIBITED FROM PREDICTIVE ANALYSIS |


## 17. Research basis


- [User-provided deep research report](<C:/Users/danie/Downloads/deep-research-report (4).md>) — synthesis used for architecture and priorities; not governing authority
- [User-provided numerical rework report](<C:/Users/danie/.codex/attachments/d009436a-9190-4689-b4a8-f2108b9890a7/pasted-text.txt>) — distribution-first implementation proposal; not proof of a fit or result
- [NGBoost: Natural Gradient Boosting for Probabilistic Prediction](https://proceedings.mlr.press/v119/duan20a.html)
- [GAMLSS — Rigby and Stasinopoulos](https://doi.org/10.1111/j.1467-9876.2005.00510.x)
- [Noncrossing quantile regression — Bondell, Reich and Wang](https://doi.org/10.1093/biomet/asq048)
- [XGBoost learning-to-rank documentation](https://xgboost.readthedocs.io/en/latest/tutorials/learning_to_rank.html) — query groups, LambdaMART, pair construction, and small/large-data cautions
- [LightGBM parameters](https://lightgbm.readthedocs.io/en/latest/Parameters.html) — ranking objectives, truncation, and probability-weighting cautions
- [CatBoost ranking objectives](https://catboost.ai/docs/en/concepts/loss-functions-ranking) and [categorical-feature documentation](https://catboost.ai/docs/en/features/categorical-features)
- [CatBoost: Unbiased Boosting with Categorical Features](https://proceedings.neurips.cc/paper/2018/hash/14491b756b3a51daac41c24863285549-Abstract.html)
- [scikit-learn probability calibration](https://scikit-learn.org/stable/modules/calibration.html) — disjoint calibration, sigmoid, isotonic, and temperature scaling
- [scikit-learn top-k accuracy](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.top_k_accuracy_score.html) — single-label limitation
- [Strictly Proper Scoring Rules — Gneiting and Raftery](https://doi.org/10.1198/016214506000001437)
- [Rolling-origin evaluation](https://otexts.com/fpp3/tscv.html)
- [Predictive stacking — Yao et al.](https://doi.org/10.1214/17-BA1091)
- [Hierarchical partial pooling — Gelman](https://sites.stat.columbia.edu/gelman/surveys.course/Gelman2006.pdf)
- [Opta event definitions](https://www.statsperform.com/opta-event-definitions/) — provider-specific soccer event semantics, including shots on target and blocked shots
- [Corner-kick count forecasting with compound Poisson models](https://arxiv.org/abs/2112.13001) — basis for testing overdispersed/cluster-aware corner challengers against naive Poisson, not for activating a model without H0 validation
- [Player-level shot-output forecasting](https://escholarship.org/uc/item/21j688ph) — supports separating expected minutes and per-minute/per-90 shot rate; treated as challenger-design evidence only


## 18. v2.1 derivative-market challenger gates


No new numerical model is activated by P-061–P-063. Before a soccer corner or player-SOT challenger can enter shadow evaluation:


1. freeze the exact provider and event definition used by both feature and label pipelines;
2. model exposure separately from event rate, including role/substitution and score-state mixtures;
3. benchmark corner counts against naive Poisson and at least one overdispersed or cluster-aware alternative; select only inside chronological TRAIN/TUNE and test once on untouched event-grouped data;
4. for SOT, derive shots from minutes × opponent-adjusted shot rate, then model on-target conversion conditionally rather than treating recent 1+ SOT outcomes as Bernoulli form;
5. fail closed to `NOT_GENERATED` or a qualitative `FORCED RANK` when decisive direct-event inputs or provider definitions are missing.


These are admission and validation rules, not fitted weights and not claims of improved accuracy.


## September 5 user confirmation — controlling eligibility correction


[Controlling policy](PERFORMANCE_ELIGIBILITY_POLICY.md). The user confirmed: **all existing game logs except views explicitly labelled LIVE were strictly frozen pre-game**. Accept this as the provenance basis `USER_CONFIRMED_PREGAME_FREEZE`, effective September 5. Non-live issued cards are eligible for historical qualitative directional/ranking evaluation. A late local import alone no longer excludes them. This correction supersedes earlier blanket `E1-Q-LATE_IMPORT`, “all non-performance-eligible” and “zero eligible historical units” statements. It records user confirmation; it does not assert independent timestamp verification or change original file times.


Keep four distinct fields: **forecast horizon at issue**, **event state when checked for settlement**, **provenance basis**, and **endpoint settlement status**. An originally pre-game card found live during settlement stays pre-game and awaits a final; it does not become a live-issued forecast. A live source/page, a “live counter-branch”, or a post-issue status check is not an issuance label. Explicit live or live-state-unverified issued views stay outside pre-game metrics. Original pre-game and later live views of one event must retain their own ranks and share an event cluster.


The headline historical scorecard includes all identifiable, genuinely issued, settled contracts/ranks in its stated cohort, including `FORCED RANK`, LOW evidence, and `PROCESS_DEFECT` outcomes. Do not remove a bad pick because its reasoning was poor. Process grade is a diagnostic column and a separately labelled compliance slice. No-forecast/no-action records are not trials; unresolved/void/push/partial rows have explicit denominators; materially unidentifiable contracts remain unscorable with the reason recorded. A row’s missing operator terms may limit ticket settlement without erasing a clearly defined research endpoint. Never use an issue-time row already decided as a predictive success.


Use the exact original pre-game order, including the latest genuinely pre-game refresh; never substitute a later live or retrospective order. Deduplicate aliases and group related targets/views by underlying event. Report historical performance by issued method, sport/competition, horizon and target. The ten newly settled cards are an evaluated v3.4 pre-game cohort. Earlier historical scorecards need those same row/view joins before a new all-history aggregate is reported; the complete status index is not itself a performance denominator.


Old games may measure their issued methods and supply development evidence for improvements. They cannot validate a v3.5/v3.6 change designed after their outcomes were seen. Keep the historical ranking count separate from each frozen challenger’s later test count. No probabilities, fitted coefficients, calibration or market-edge claims are created by this provenance correction. Future snapshots/hashes and externally timestamped revisions are useful provenance records; a local hash or editable git timestamp alone is not an independent timestamp authority, and no git-only approval gate is imposed on this user-confirmed history.


## Current scoring, build and evaluation contract — 2026-09-17


SCORING_AND_VALIDATION defines exact binary versus W/P/L/action-conditional scoring; the full categorical Brier is half-scaled, realised pushes stay in its denominator, and WIN/LOSS-only scoring uses q=p_win/(1-p_push). Retain incompatible old scores as labelled legacy diagnostics. Average once per prespecified target then once per event; compare identical held-out events and fixed threshold grids with a frozen empirical/conditional baseline. Report paired event uncertainty, coverage, calibration and target difficulty. No global absolute-normalised-edge ranking is valid across unrelated distributions.


MODEL_IMPLEMENTATION_RECIPES supplies the executable empirical/count/scenario/scoring/phase/extra-state primitives. NUMERICAL_PROGRAM provides the single stage sequence: field-specific source admission and H0 before fitting; S5 held-out checks **and S6 prospective shadow before publication**. A3/A4 and learned rank/pair models are optional/dormant, not compulsory predecessors. Reference code tests do not establish model performance. Historical user-confirmed forecasts remain learning-only under the later controlling directive; no retrospective data join is called prospective.


<!-- DEEP-RESEARCH-IMPLEMENTATION-2026-09-19-V42 -->
## 2026-09-19(c) — model sequencing and promotion discipline


The audit changes the order of work, not the menu of possible models.


- **A0:** empirical/partially pooled conditional distribution is mandatory.
- **A1:** interpretable hierarchical count/location-scale model is the first champion candidate.
- **A2:** sport-native state-transition simulator is a challenger after A0/A1 pass data-quality gates.
- **A3/A4:** distributional boosting/nonlinear models are challengers only when the eligible sample and feature stability justify them.
- **A6:** ensemble only from frozen out-of-fold predictive distributions.


For over/unders and spreads, every candidate must emit a coherent score/total/margin distribution that supports multiple thresholds consistently. Independent binary heads per line are disfavoured unless they are constrained to a valid non-crossing distribution and beat the distributional baseline out of sample.


Do not select a model because it is sophisticated or because it improves hit rate on the development sample. Selection uses preregistered proper scores, calibration/support checks, critical slices and uncertainty on the same chronological test population.