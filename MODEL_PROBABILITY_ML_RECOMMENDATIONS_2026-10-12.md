# Model, probability and machine-learning improvement recommendations

**Prepared:** 12 October 2026, Australia/Sydney. **Status:** recommendations only. **Scope:** Sports Research forecasting, probability estimation, model comparison and qualification.

The strongest next step is a small portfolio of fitted, coherent models evaluated against strong frozen baselines. Model complexity should follow measured benefit. Calibration, prediction accuracy, distribution coherence and operational readiness each need their own evidence.

This document proposes future work. It changes no operating rule, model, prompt, data file, prediction or log. The only repository addition from this request is this document.

## 1. Repository context and priority

The inspected local HEAD was `10fb47a160d96325690dc9ee58a9cc16d3b35beb`. It contains the archive quarantine/rebuild commit following the earlier audit. The working tree also contains existing control edits, including v11 wording in `CURRENT_RULES.md`. This recommendation document uses those files as context and does not treat an unpublished working revision as a released model.

Inspected reference documents include [CURRENT_STATE](CURRENT_STATE.md), [CURRENT_RULES](CURRENT_RULES.md), [SCORING_AND_VALIDATION](SCORING_AND_VALIDATION.md), [HYPOTHESIS_REGISTER](HYPOTHESIS_REGISTER.md), the suspended [NUMERICAL_MODEL_REGISTER](NUMERICAL_MODEL_REGISTER.md), and the earlier [audit recommendations](AUDIT_RECOMMENDATIONS_2026-10-12.txt).

The numerical model register is explicitly suspended. Its model names, old fitted-runtime descriptions and historical promotion thresholds are design/history. The current state does not establish a fitted, calibrated production model. A future implementation would require a separately authorized implementation scope; this request supplies the recommendations.

| Priority | Improvement | Practical benefit | Evidence needed before adoption |
|---|---|---|---|
| 1 | Verified event population and point-in-time features | Prevents fitting convincing models to invented, duplicated or unavailable inputs | Declared population; field provenance; identity and availability audit |
| 1 | League baseline plus regularized team-strength baseline | Establishes whether event information adds useful prediction | Same-event, same-endpoint, same-line comparisons |
| 1 | Coherent event distribution with discrete support | Makes winner, total, handicap and push probabilities compatible | Normalization, endpoint, support and contract checks |
| 1 | Rolling chronological development and untouched future tests | Measures performance in the conditions of actual use | Frozen folds, training-only feature construction and retained predictions |
| 2 | Hierarchical shrinkage and dynamic strengths | Reduces noise in small samples and adapts to changing teams | Learning curves and season/regime holdouts |
| 2 | Conditional variance, tails and roster mixtures | Improves uncertainty and difficult-tail probabilities | Distribution scores, interval calibration and subgroup checks |
| 2 | Calibration fitted on separate predictions | Corrects systematic probability distortion where supported | Independent evaluation, sufficient precision and coherence checks |
| 3 | CatBoost and distributional boosting challengers | Tests nonlinear interactions and matchup-dependent uncertainty | Incremental improvement over simpler fitted models |
| 3 | Chronological stacking of compatible distributions | Combines complementary strengths | Out-of-fold fit; separate calibration; advantage over best single model |
| Later | Deep sequence models, transformers and elaborate simulators | May exploit rich granular information | Relevant data, learning curves, compute justification and honest benchmarks |

These priorities are judgments for this repository, not claims that a named method will improve its outcomes.

## 2. Probability improvements

### P01. Define the complete event state before deriving propositions

Use an event distribution over states containing everything needed to grade the declared endpoints. For ordinary score sports this can begin with joint scores; some sports require a richer state.

- Tennis needs set outcomes, game counts, serving order and format. Match winner cannot generally be inferred from total games won.
- Cricket needs innings, wickets, resources, completion/result method and chase stopping. A common cross-team score margin often has no useful interpretation.
- Hockey needs regulation, overtime and shootout accounting. A shootout award in the official final is different from goals scored during play.
- Baseball needs the innings/rules endpoint, home-team final-inning stopping and permitted ties or suspended games.

For a frozen contract, derive its WIN/PUSH/LOSS/VOID sets from this state. Reuse those sets for settlement and evaluation. This is more general than assuming every winner is determined by `home score > away score`.

**Acceptance:** every published proposition has a deterministic endpoint/contract mapping; mathematically possible states are retained and impossible states have structural zero mass.

### P02. Keep unconditional masses and decisive probabilities distinct

For a declared outcome universe:

\[
W+P+L+V=1,\qquad p_{\mathrm{decisive}}=\frac{W}{W+L}.
\]

The decisive probability evaluates WIN versus LOSS conditional on a decisive result. It does not specify push or void probability. Record both the conditioning and the mass vector where computed. If the model conditions on the event taking place or the contract being in action, state that explicitly; do not invent a numeric cancellation/void probability.

Wolfram verified a synthetic case with `W=0.55`, `P=0.10`, `L=0.35`, `V=0`: decisive probability is `11/18 = 0.611111…`. The unconditional loss probability remains `0.35`.

**Acceptance:** binary scores use the original decisive probability only on matching WIN/LOSS outcomes; categorical scores use the complete forecast outcome vector on the matching universe.

### P03. Model dependence and respect score support

For team scores \(H,A\), total \(T=H+A\) and signed margin \(M=H-A\):

\[
\begin{aligned}
\operatorname{Var}(T)&=\operatorname{Var}(H)+\operatorname{Var}(A)+2\operatorname{Cov}(H,A),\\
\operatorname{Var}(M)&=\operatorname{Var}(H)+\operatorname{Var}(A)-2\operatorname{Cov}(H,A).
\end{aligned}
\]

Estimate dependence from an appropriate training population or explain its uncertainty. Missing covariance is not evidence of independence. A shared pace/environment factor is one possible mechanism, but its sign and strength should follow the sport and data.

Separate total/margin regressions require a compatible joint reconstruction. For integer scores, \(T\) and \(M\) must have matching parity, \(T\geq |M|\), and nonnegative reconstructed scores. Continuous normal or Student-t approximations require an explicit discretization, boundary and tail treatment before claiming exact discrete push probabilities.

**Acceptance:** related rows reconcile to the same state distribution; truncation error is measured; any numerical covariance matrix is valid. Fréchet bounds remain bounds when a joint is unavailable.

### P04. Replace universal dispersion with conditional dispersion

Allow uncertainty to depend on matchup, pace, team strengths, expected minutes, roster uncertainty and supported competition conditions. Fit the variance/dispersion function and test its additional value.

For overdispersed counts, one candidate is:

\[
Y\sim\operatorname{NB}(\mu,\phi),\qquad \operatorname{Var}(Y)=\mu+\phi\mu^2.
\]

Wolfram verified that \(\mu=4,\phi=0.2\) gives variance \(7.2\). Choosing negative binomial solely because it has wider tails is insufficient: compare it to Poisson and alternative support-appropriate models on held-out outcomes.

For high-scoring sports, test a heteroscedastic model and a heavier-tailed challenger. Avoid forcing one global SD or a heavy-tail distribution without evidence.

**Acceptance:** improvement in distribution/interval scores, sensible subgroup coverage and stable estimated dispersion.

### P05. Include roster and parameter uncertainty

For genuine pregame scenario probabilities \(\pi_s\):

\[
p(y\mid x)=\sum_s\pi_s p(y\mid x,s),
\]

\[
\operatorname{Var}(Y)=\sum_s\pi_s\sigma_s^2+
\sum_s\pi_s(\mu_s-\bar\mu)^2.
\]

Wolfram checked an illustrative two-scenario mixture: weights `0.7/0.3`, means `180/200`, SDs `12/18`. Its mean is `186`, within-scenario variance `198`, between-scenario variance `84`, total variance `282`, and SD `16.792856`. Omitting between-scenario uncertainty understates the spread.

Use supported availability probabilities when available. Otherwise publish scenario sensitivity or bounds rather than assigning arbitrary scenario weights. Integrate fitted parameter uncertainty through a posterior predictive distribution or a justified resampling method; keep this separate from uncertainty about one game's outcome.

**Acceptance:** scenario inputs and weights are traceable, and predictive intervals include the relevant uncertainty sources without double-counting them.

### P06. Shrink noisy estimates and distinguish sampling zeros from structural zeros

Use partial pooling for team/player strengths, home effects, venue effects and sparse competition segments. Explain the population being pooled and avoid borrowing across incompatible formats or rule regimes.

An empirical category probability can use a declared Dirichlet prior:

\[
\widehat p_k=\frac{n_k+\alpha_k}{n+\sum_j\alpha_j}.
\]

Apply positive prior mass only to logically possible outcomes. A rare outcome absent from a small training set is different from an impossible event. Estimate/tune shrinkage using earlier data and report sensitivity.

**Acceptance:** small-sample predictions revert toward an appropriate prior; uncertainty widens where data is scarce; no unsupported deterministic probabilities are created by zero observed counts.

### P07. Fix endpoint-specific logical constraints

Check subset relationships from the actual event sets. The archived tennis toolkit's proposed bound `P(negative games handicap) <= P(match win)` is not universal.

Wolfram verified the counterexample `6-0, 4-6, 4-6`: player A loses the match one set to two, wins total games `14-12`, and covers `-1.5 games`. Tennis handicap probabilities must include match-loss states where the player still covers.

Apply the same discipline to draw action, overtime-inclusive contracts, phase totals and cricket margins. A sport-specific invariant needs a proof or an explicit declared assumption.

**Acceptance:** adversarial legal score states pass contract arithmetic while invalid subset assumptions fail review.

## 3. Statistical-model improvements

### M01. Fit two strong baselines before complex models

Retain the frozen league-only baseline required by the current framework. Add a separate fitted team-strength comparator, such as regularized Bradley–Terry/logistic, a draw-aware model or a suitable Elo-style rating.

The league baseline tests whether event information helps beyond the population. The team-strength comparator tests whether a complex model helps beyond a simple fitted model. Neither may use future standings, test-season aggregate parameters or post-event lineups.

Keep baseline parameters, probability conditioning and exact-row predictions frozen. Historical realized climatology remains a descriptive reference.

**Acceptance:** the candidate beats meaningful comparators on the same events, endpoints and lines, with coverage/exclusions disclosed.

### M02. Estimate dynamic strengths with partial pooling

Replace unsupported last-game adjustments with time-varying attack/defence or latent strength models. Test exponential time weighting, a state-space evolution model and a static shrinkage baseline.

Model offseason turnover, promoted teams, personnel changes and verified rule changes explicitly. Select forgetting rates and process noise on chronological development folds; do not infer a universal shift from a few misses.

**Acceptance:** better future prediction than the static model, stable parameter evolution and appropriate uncertainty for newly observed teams.

### M03. Use exposure models where data supports them

Predict opportunities before converting them into scoring: possessions, minutes, drives, shots, deliveries or plate appearances. Estimate scoring conditional on exposure and relevant state.

The exposure estimate itself is uncertain. Preserve its distribution, substitution/rotation limits and stopping rules. Avoid multiplying unrelated average rates and then presenting the result as a fitted simulator.

**Acceptance:** exposure and conversion are both evaluated; the final distribution respects the competition's rules.

### M04. Prioritise these sport-specific model candidates

The table is a proposed architecture shortlist. Each row needs its own data audit and test; qualification does not transfer between sports or endpoints.

| Sport | First fitted candidate | Valuable challenger | Structural requirements |
|---|---|---|---|
| Soccer | Hierarchical attack/defence Poisson model with estimated home effect and time variation | Low-score dependence correction; bivariate or overdispersed count model | Regulation goals and 1X2 coherent; corners use their own observed fields and count process |
| Basketball | Joint possession/efficiency model, or a simpler regularized joint-score model when possession data is unavailable | Heteroscedastic distributional regression; heavy-tail/mixture model | Minutes/rotation, pace uncertainty, regulation ties and exact overtime endpoint |
| Baseball | Hierarchical run model with starter, bullpen and park inputs | Base–out/inning state model with pitcher transitions | Innings/tie rules, no unnecessary home final half-inning, walk-off scoring and lineup exposure |
| American football | Regularized team-strength and drive-outcome model | State/drive simulator; tree-based distribution challenger | Preserve discrete scoring/key-number masses, QB scenarios and competition overtime rules |
| AFL/AFLW | Joint scoring-shot volume and goal-conversion model | Dynamic strength and conditional-dispersion model | Derive points from `6 × goals + behinds`; use the correct competition/era |
| Rugby league | Try/conversion/penalty/field-goal event model | Dynamic strength and discipline-state mixture | Competition/era scoring values, possession exposure and golden-point convention |
| Rugby union | Separate scoring-event model for union | Territory/discipline/availability challenger | Union scoring values and match rules; no transfer of league's try values |
| Ice hockey | Regulation dependent-goal model with goalie and special-team inputs | Shot-quality, empty-net and manpower-state model | Regulation/OT/SO states, pulled-goalie tail and official shootout-score accounting |
| Limited-overs cricket | Delivery/phase transition model with runs, wickets and legal-ball state | Role/lineup/toss/weather mixture | Chase stops on the winning delivery with legal overshoot; wickets/overs/DLS/resources handled explicitly |
| Test cricket | Separate multi-innings match/result model | Time/weather and declaration strategy model | Draw/time limits, declarations and multiple innings; no reuse of a limited-overs endpoint |
| Tennis | Surface-aware serve/return point model connected through game/set/match transitions | Fatigue/form mixture and dynamic ratings | Serving order, format and tiebreak rules; consistent winner/sets/games outputs and retirement definition |

Exact sport simulators are valuable only when transition probabilities and inputs can be fitted and audited. Sparse final-score data often supports a simpler model first.

## 4. Machine-learning improvements

### ML01. Start with interpretable regularized challengers

Use regularized logistic/multinomial models, generalized additive models and count regression before large nonlinear systems. Include opponent-adjusted strengths, rest, venue, availability and supported exposure variables.

Report feature ablations on future folds. An apparently useful feature can be a proxy for leakage, team identity or a changing data feed.

**Acceptance:** stable incremental benefit over the baseline, with a clear explanation of which inputs create it.

### ML02. Test CatBoost on tabular event features

CatBoost is a reasonable challenger where team/player/venue categories and nonlinear interactions are important. Its ordered boosting/categorical-statistics methods address specific training biases; temporal leakage still requires explicit chronological splits and training-only transformations. [CatBoost paper](https://arxiv.org/abs/1706.09516).

Start with a declared target such as regulation 1X2 or an endpoint-specific winner. A winner classifier does not itself supply a coherent score distribution for totals and handicaps. Retain a separate structural model or an explicit coherent integration.

**Acceptance:** improvement over regularized ratings on future events; robust results for new teams/seasons; no held-out labels used in encoding.

### ML03. Predict conditional distributions, not only point scores

Test NGBoost or distributional regression when the task needs event-specific mean, dispersion and tails. NGBoost trains predictive-distribution parameters rather than only a mean prediction. Distribution choice remains a modeling assumption. [NGBoost paper](https://proceedings.mlr.press/v119/duan20a.html).

Quantile boosting is another challenger for scalar scores. Correct quantile crossing and assess multiple quantiles. Quantiles alone do not establish a unique joint distribution, exact integer push masses or a complete event simulator.

**Acceptance:** better proper distribution scores and useful interval sharpness at comparable coverage; additional uncertainty parameters remain stable.

### ML04. Blend distributions using genuine out-of-fold predictions

For compatible event distributions:

\[
p_{\mathrm{blend}}(\omega)=\sum_m w_m p_m(\omega),\qquad
w_m\geq0,\quad\sum_m w_m=1.
\]

Fit weights on chronological out-of-fold/development predictions under a declared proper score. Prefer a constrained regularized blend initially. Evaluate against the best single model and use a later calibration stage.

Avoid fitting stack weights and a flexible calibrator on the same small calibration outcomes without a justified nested/cross-fitting design. Every component must describe the same event/endpoint or undergo an explicit compatible mapping.

**Acceptance:** held-out benefit exceeds the best individual component without loss of coherence or material coverage degradation.

### ML05. Defer deep models based on evidence, not a universal row threshold

Replace the archived `n > 50,000` rule with learning curves, effective unique-event counts, sequence quality, data availability and benchmark evidence. Thousands of points or propositions from a small number of matches do not create thousands of independent match-level tests.

Sequence models can become useful for granular event streams, but first compare them to state/transition models and simpler tabular learners. Pretraining and transfer require evaluation of the destination league/format and source compatibility.

**Acceptance:** benefit, stability and operating cost are justified on genuinely future events. Model size alone is never a promotion criterion.

## 5. Calibration improvements

### C01. Fit calibration on independent chronological predictions

Separate training, tuning/model selection, any stacking fit, calibration and final evaluation. When data is limited, use nested rolling-origin prediction generation with an untouched outer evaluation period. Fit every transformation using only the allowed earlier data.

For binary forecasts, compare identity, regularized sigmoid and beta calibration. Isotonic is a candidate when data and learning curves justify its flexibility. Beta calibration is a parametric alternative; the original paper also discusses isotonic's small-sample overfitting risk. [Beta calibration paper](https://proceedings.mlr.press/v54/kull17a.html).

For complete multiclass vectors, test temperature scaling and suitably regularized multiclass/Dirichlet calibration. Preserve sum-to-one and the full draw/tie class. [Dirichlet calibration paper](https://arxiv.org/abs/1910.12656).

**Acceptance:** the calibrated model improves independent probability scores or reliability at adequate precision; identity remains the fallback when benefit is unsupported.

### C02. Remove arbitrary calibration sample guarantees

The suspended register's `200 events` isotonic rule and `50 events / 28 days` gate do not guarantee calibration. Examine probability-range coverage, class counts, distinct events, independent time blocks, model complexity and learning curves.

Likewise, a confidence interval for calibration slope containing `1`, or intercept containing `0`, can simply be too wide to reveal an error. If claiming approximate calibration, predeclare practical tolerances and require adequate evidence within them. Do not present post-hoc observed power as a successful prospective sample plan.

**Acceptance:** qualification states its scope and precision; an underpowered result remains inconclusive.

### C03. Calibrate coherently and revalidate every affected endpoint

Prefer adjustment at the event-distribution level. For winner classes \(c\), an illustrative reweighting is:

\[
p'(\omega)=p(\omega)\frac{q_c}{p_c},\qquad \omega\in c,
\]

where \(p_c>0\), \(q_c\geq0\), and target class masses sum to one. If a required class has zero original support, repair the model/support rather than dividing by zero. This reweighting preserves a valid distribution but changes other derived probabilities.

Wolfram checked a four-state example: winner masses changed from `(0.70, 0.10, 0.20)` to `(0.60, 0.15, 0.25)`. Total Over 1.5 changed from `0.55` to `15/28 = 0.535714…`. Winner calibration therefore requires new checks of total, margin, push and joint outcomes.

Independent contract-by-contract calibration can break complement, monotonicity and joint constraints. If used, reconciliation and separate predictive evaluation are required.

**Acceptance:** logical coherence holds after calibration, and each advertised probability family has its own evaluated reliability.

### C04. Use conformal intervals as a separate uncertainty challenger

Conformal methods can complement forecast intervals, but a prediction set is not a replacement for calibrated event probabilities. Ordinary exchangeability assumptions need scrutiny for sports time series; test adaptive/time-aware approaches and track interval width as well as coverage. Long-run coverage does not establish conditional coverage for every team or individual game. [Adaptive conformal inference paper](https://arxiv.org/abs/2106.00170).

**Acceptance:** future interval coverage and width are reported by relevant strata, with the method's assumptions and limits stated.

## 6. Evaluation and qualification improvements

### E01. Train on a declared population rather than selected prediction logs

Define the eligible event universe, stage, seasons, endpoints and source coverage before fitting. Prediction logs are useful for research QA and prospective evaluation, but their selected events and lines can create training-selection bias.

Verify rebuilt archive inputs against their repair receipts before use. Preserve genuine zeros, missingness, source quality, native identities and historical correction versions. Do not assume that a larger archive is a better training dataset.

**Acceptance:** inclusion/exclusion and missingness are reproducible, and all event-level rows remain in one fold.

### E02. Evaluate with rolling chronological folds and realistic cutoffs

For each outer test period, construct ratings, priors, features, calibrators and encodings from earlier data only. Keep future standings, season-end aggregates, revised lineups and postgame features outside the fold.

Test the actual issue horizons separately: for example, an early pregame model and a lineup-confirmed model have different available information. Purge overlap where a label or feature interval crosses a split; an arbitrary embargo is not a substitute for an availability audit.

**Acceptance:** saved forecasts can be reproduced from the inputs available at their stated cutoff, including any scheduled-to-actual-start distinction.

### E03. Use proper scores on identical tasks

Use Brier/log loss for matching categorical or decisive outcomes and CRPS or suitable discrete distribution scores for score distributions. Report MAE/RMSE as point-prediction diagnostics, with predictive interval coverage and sharpness. Proper scoring supplies a principled basis for rewarding informative probability forecasts. [Gneiting and Raftery](https://sites.stat.washington.edu/people/raftery/Research/PDF/Gneiting2007jasa.pdf).

For joint outcomes, assess joint likelihood where the model supports it and dependence-specific diagnostics. Multivariate scores such as the variogram score can add information about dependence that marginal accuracy misses. [Scheuerer and Hamill](https://journals.ametsoc.org/doi/10.1175/MWR-D-14-00269.1).

Score original primary picks, informational candidates and frozen shadows separately. Retain unresolved, push, void, qualitative and no-forecast coverage. Evaluate the declared candidate universe as well as selected rows where possible, so selection cannot conceal poor probability estimates.

**Acceptance:** model comparisons use the same frozen events/lines/endpoints and explain every exclusion. A higher hit rate on easier propositions is not treated as incremental prediction skill.

### E04. Use dependence-aware, preplanned acceptance

Average dependent proposition differences within each event first. Choose time blocks and weights before evaluation; investigate repeated-team and serial dependence rather than assuming ISO weeks are always independent.

Predeclare one primary comparison, a meaningful improvement or noninferiority margin, calibration/coverage guardrails, multiplicity handling and a fixed stopping rule. Use development data for planning variance and learning curves. Avoid repeated peeking followed by acceptance at the first favorable result.

A Wolfram-verified illustration shows why minimum counts are insufficient: assuming independent normal block differences with SD `0.02`, one-sided alpha `0.05`, power `0.80`, and true improvement `0.005` against a zero-difference null, a normal approximation needs **99 independent blocks**. This is a synthetic planning example, not an estimate for this repository. Unknown variance, dependence, stricter effect-margin claims and multiple comparisons alter the design.

**Acceptance:** the final comparison answers a predeclared question with credible precision; model fitting, mechanics and mathematical checks are reported independently of predictive benefit.

### E05. Measure stability and monitor prospective drift

Break out league/format/endpoint, season/regime, probability range, lead time, evidence quality, uncertainty and availability states. Report both average performance and worst relevant subgroup limitations.

After a fixed model is approved, monitor feature/outcome availability, score degradation, residual shifts and calibration with a declared intervention policy. Retraining/recalibration produces a new version and fresh validation; past forecasts remain frozen. Diagnostic feature explanations do not by themselves establish causal effects.

**Acceptance:** drift alerts have an owner and response, and retrospective changes cannot quietly alter the record used to justify a model.

## 7. A practical first development programme

Start with **one well-supported league and one explicit endpoint**. EPL regulation 1X2 and NBL overtime-inclusive winner are plausible candidates from prior project work, subject to the current data audit. Select the first pilot by verified field coverage and time-safe history.

1. Produce the event/data card, known-at feature inventory and chronological folds.
2. Fit the league baseline and regularized team-strength baseline.
3. Fit one coherent sport-specific distribution and evaluate its mean, variance, tails and contract masses.
4. Add dynamic strengths and uncertainty; retain them only for reproducible future-fold benefit.
5. Test one tabular ML challenger and one distributional challenger.
6. Fit a conservative calibrator using independent predictions; evaluate the integrated output.
7. Freeze the chosen model, feature recipe, calibration, candidate policy and evaluation design.
8. Collect prospective shadow forecasts over the complete eligible population, including abstentions and unresolved evidence.
9. Adopt only the endpoints supported by the results. Repeat qualification for additional totals, handicaps, leagues and formats.

The first acceptance package should contain event IDs/cutoffs, data/source versions, model specifications, out-of-fold predictions, independent calibration results, paired comparator predictions, complete coverage, proper scores with justified uncertainty, endpoint checks and prospective outcomes.

## 8. Wolfram verification receipt

The explicitly selected [Wolfram plugin](plugin://app-69fe0bf66c8481919c513d799406436e@openai-curated-remote) was used for context discovery and **three Wolfram Language evaluator calls**. The broad context search did not establish sport-model performance; it supplied computational references, including [Markov process properties](https://reference.wolfram.com/language/ref/MarkovProcessProperties.html). The numerical results below were actually computed with exact rational inputs where applicable.

| Check | Inputs | Computed result | Recommendation supported |
|---|---|---|---|
| Push-aware probability | W/P/L/V = 0.55/0.10/0.35/0 | Decisive p = 11/18 | Declare probability conditioning |
| Joint moments | States (2,0),(1,0),(0,1),(1,1); masses .45,.25,.20,.10 | Means 1.25,.30; variances .5875,.21; covariance -.275; Var(total) .2475; Var(margin) 1.3475 | Preserve dependence and score identities |
| Scenario mixture | Weights .7/.3; means 180/200; SDs 12/18 | Mean 186; variance 282; SD 16.792856; P(score > 210) .091123974 | Include between-scenario uncertainty |
| Tennis score state | A wins 6-0, then loses 4-6,4-6 | A loses match, games 14-12, covers -1.5 | Use endpoint-specific event sets |
| Winner reweighting | Original classes .70/.10/.20; targets .60/.15/.25 | State masses 27/70,3/14,1/4,3/20; normalized; total Over 1.5 moves .55 to 15/28 | Recheck other endpoints after calibration |
| Variance reconstruction | Total/margin formulas with Cov(T,M)=Var(H)-Var(A) | Reconstructs Var(H), Var(A) exactly | Joint reconstruction checks |
| Negative binomial | Mean 4; phi .2 | Variance 36/5 = 7.2 | Explicit overdispersion parameterization |
| Illustrative sample planning | Alpha .05; power .80; independent block SD .02; alternative -.005 versus null 0 | 99 blocks under normal approximation | Plan precision rather than relying on minimum counts |

These are synthetic mathematical checks. They establish the reported arithmetic and counterexamples; predictive performance must be measured on the project's genuine future outcomes.

## 9. Suggested first experiments

| Proposed experiment | Frozen comparison | Primary evidence | Stop or reject when |
|---|---|---|---|
| PROPOSED-M01 | Regularized team-strength model versus league-only baseline | Same-event probability scores and coverage | Benefit is unsupported or features fail availability checks |
| PROPOSED-M02 | Dynamic partial pooling versus static fitted strengths | Future-fold scores; turnover/new-team strata | Instability or insufficient gain over static model |
| PROPOSED-P01 | Conditional dispersion versus fixed dispersion | Distribution scores, tails, interval calibration | Additional flexibility worsens future calibration or is unidentifiable |
| PROPOSED-P02 | Supported roster mixture versus point roster assumption | Future distribution scores and uncertain-roster coverage | Weights cannot be justified or uncertainty is double-counted |
| PROPOSED-ML01 | CatBoost versus strongest simple fitted model | Endpoint-specific proper scores and subgroup stability | Improvement does not survive chronological evaluation |
| PROPOSED-ML02 | Distributional boosting versus structural model | CRPS/log score and compatible joint checks | Marginal gains conceal joint or support defects |
| PROPOSED-C01 | Identity versus conservative calibration | Independent scores, reliability precision and coherence | Data is insufficient or derived endpoints deteriorate |
| PROPOSED-ENS01 | Constrained distribution mixture versus best component | Later held-out proper scores and coverage | Added complexity provides no robust benefit |

These are proposed identifiers within this document. They have not been added to the hypothesis register and have no approved sample plan or observed result. Before implementation, select the relevant subset and freeze its definitions, effect sizes, dependence treatment, sample justification and stopping rule.
