# Numerical Model Register & Portfolio Specification

**Authority:** MDS-2026.10.01-v8.0 / CR-2026.10.06-NUMERICAL-1.
**Status:** Mandatory Register for all Numerical ML Model Architectures, Prioritized Candidates, Fixed-Cohort Comparative Evaluation, and Promotion Gates.

---

## 1. Prioritized Implementation Roadmap & Candidate Hierarchy

The repository prioritizes candidates for empirical testing—not guaranteed improvements in winning rate. Candidates are organized into a strict 5-stage testing hierarchy. Complex deep learning and transformer architectures are explicitly deferred until the core portfolio demonstrates reliable out-of-sample skill.

```text
 ┌─────────────────────────────────────────────────────────────────────────────┐
 │ Priority 1: Fitted Empirical, Rating & Hierarchical Baselines               │
 │  • Elo / Glicko / TrueSkill (Skill uncertainty, draws, tennis/team baselines)│
 │  • Regularized Logistic / Bradley–Terry (Draw-aware paired comparisons)     │
 │  • Hierarchical Bayesian Attack–Defence (Team shrinkage, Karlis-Ntzoufras)  │
 │  • Dixon–Coles Model (Soccer: attack, defence, home adv, time decay, ρ)     │
 │  • Negative Binomial Regression (Overdispersed counts: runs, corners)        │
 │  • Joint Score / Student-t Regression (Heavy-tailed margin-total covariance) │
 │  • Dynamic State-Space Models (Time-varying latent strength)                │
 └──────────────────────────────────────┬──────────────────────────────────────┘
                                        │
                                        ▼
 ┌─────────────────────────────────────────────────────────────────────────────┐
 │ Priority 2: Sport-Specific Simulators with Endpoint & Stopping Rules        │
 │  • Cricket: Delivery/phase engine with chase stopping rules & wicket limits │
 │  • Tennis: Surface-adjusted point-to-match Markov chain (Hold/Break/TB)     │
 │  • Baseball: Base–out Markov chain & starter leash / bullpen transitions    │
 │  • American Football: Markov drive outcome chains (TD, FG, Safety, Punt)    │
 │  • Mixture Models: Starting pitcher, goalkeeper, QB participation scenarios │
 └──────────────────────────────────────┬──────────────────────────────────────┘
                                        │
                                        ▼
 ┌─────────────────────────────────────────────────────────────────────────────┐
 │ Priority 3: First Machine Learning Challenger                               │
 │  • CatBoost: High-cardinality categoricals, rest/travel/form interactions,   │
 │    ordered boosting, evaluated under strict chronological splits            │
 └──────────────────────────────────────┬──────────────────────────────────────┘
                                        │
                                        ▼
 ┌─────────────────────────────────────────────────────────────────────────────┐
 │ Priority 4: Distributional Boosting & Quantile Modeling                     │
 │  • NGBoost: Conditional distribution parameters (matchup-dependent variance)│
 │  • LightGBM / XGBoost: Quantile objectives with non-crossing checks         │
 │  • Generalized Additive Models (GAMs): Interpretable smooth nonlinearities  │
 └──────────────────────────────────────┬──────────────────────────────────────┘
                                        │
                                        ▼
 ┌─────────────────────────────────────────────────────────────────────────────┐
 │ Priority 5: Out-of-Sample Chronological Stacking & Probability Mixtures     │
 │  • Non-negative constrained blender (A2 Simulator + CatBoost + NGBoost)     │
 │  • Weights fit strictly on CAL (earlier fold); evaluated on TEST (later)    │
 └─────────────────────────────────────────────────────────────────────────────┘
                                        │
                                        ▼
   [ DEFERRED: Transformers, ListNet, Deep Sequence Models ] (Require n > 50,000)
```

---

## 2. Recommended Model Combinations by Sport

| Sport | Starting Combination | Highest-Value Inputs | Key Structural Rule |
|---|---|---|---|
| **Soccer** | Dynamic Hierarchical Dixon–Coles + CatBoost challenger | Opponent-adjusted chance creation (xG), lineup strength, rest, venue, competition | Fit attack, defence, home advantage, time decay; model low-score bivariate dependence ($\rho$). |
| **Basketball** | Joint possession/efficiency model + distributional boosting (NGBoost/quantiles) | Expected minutes, player availability, pace, offensive/defensive rating, rest | Possessions $\times$ PPP; Student-t margin-total covariance; handle draw/OT endpoint. |
| **Baseball** | Starter/bullpen model + negative binomial or base–out simulator | Confirmed lineup, pitcher quality/workload, bullpen availability, park, weather | Overdispersed negative binomial runs; starter leash transition inning; Statcast regimes. |
| **NFL / CFB** | Drive-based scoring model + boosted-tree challenger | QB availability, opponent-adjusted EPA/play, pace, offensive line, weather | Markov drive progression; exact preservation of key numbers (3, 7, 10, 14, 17, 20, 21). |
| **AFL / AFLW** | Scoring-shot and conversion model + dynamic ratings | Territory (I50), scoring opportunities, personnel, venue dimensions, wind | Decouple shot creation volume from conversion efficiency; Beta-Binomial $6\text{G} + \text{B}$. |
| **NRL / Rugby** | Sport-specific scoring-event model + hierarchical ratings | Team selection, attacking 20m entries, defence, kicking accuracy, disciplinary risk | Completed sets $\to$ tries (4), conversions (2), penalty goals (2); 2020 six-again regime. |
| **NHL** | Shot-quality/goalie model + dependent goal distribution | Confirmed goalie, shot quality (unblocked xG), special teams, rest, empty-net states | 60-min regulation 1X2 + empty-net goal tail + OT/shootout moneyline conversion. |
| **Cricket** | Delivery/phase model with wickets and chase stopping rules + CatBoost | Format, batting order, bowlers, toss, venue, weather, remaining resources | **Chase stopping rule**: Second innings terminates when target reached or 10 wickets lost. Two independent unrestricted innings totals are mathematically invalid for a chase. |
| **Tennis** | Surface-adjusted ratings + serve/return point model | Surface, opponent-adjusted serve/return point win ability, fatigue, format | Point-level Markov chain connecting serve/return to games, tiebreaks, sets, match winner, games handicaps, and games totals. |

---

## 3. Coherent Joint Probability Foundations

Let Home score be $H$, Away score $A$, Margin $M = H - A$, and Total $T = H + A$. All betting contracts must be derived directly from a single valid joint distribution matrix $P(H=h, A=a)$:

1. **Home Win**: $P(M > 0)$ under the specified competition endpoint.
2. **Away Win**: $P(M < 0)$.
3. **Draw / Tie**: $P(M = 0)$.
4. **Home Covering Handicap $s$**: $P(M + s > 0)$.
5. **Away Covering Handicap $s$**: $P(-M + s > 0)$.
6. **Over Total $L$**: $P(T > L)$.
7. **Under Total $L$**: $P(T < L)$.
8. **Push Probabilities**: Retain exact discrete equality mass where applicable ($P(M + s = 0)$, $P(T = L)$).
9. **Monotonicity**: $P(\text{Over } L_1) \ge P(\text{Over } L_2)$ for any $L_1 < L_2$.
10. **Covering Pair Consistency**: $P(\text{Home } +k) \ge P(\text{Home ML})$ for any $k \ge 0$.
11. **Reconciliation Requirement**: Separately fitted margin and total models require an explicit joint reconciliation step before claiming a coherent joint score distribution.

---

## 4. Fixed-Cohort Comparative Evaluation Mandate

### The Line Selection Fallacy
"Game lines" are treated as handicaps or spreads. **Performance improvement must be measured strictly on identical fixtures and supplied lines.**
- Selecting easier handicaps or heavier favourites can artificially increase hit rate without improving prediction quality.
- Challenger models must be benchmarked on the exact same line cohort as the champion.

### Multi-Metric Promotion Matrix
Promotion from challenger to production requires meeting **all** conditions on the untouched `TEST` fold:

| Evaluation Dimension | Metric | Required Threshold | Operational Meaning |
|---|---|---|---|
| **Probabilistic Accuracy** | Brier Score | $\Delta \text{Brier} \le -0.010$ | Statistically superior probability resolution |
| **Information Loss** | Log Loss | $\Delta \text{LogLoss} \le 0.0$ | No deterioration; severe penalty on overconfident misses |
| **Distribution Quality** | CRPS | $\Delta \text{CRPS} < 0.0$ | Superior continuous ranked probability score across all thresholds |
| **Calibration Quality** | Slope $\beta$ | $0.90 \le \beta \le 1.10$ | Cox calibration slope ($\text{logit}(P) = \alpha + \beta \cdot \text{logit}(p)$) |
| **Calibration Quality** | Intercept $\alpha$ | $|\alpha| \le 0.05$ | Unbiased central calibration |
| **Fixed-Cohort Cover** | Hit Rate on Same Line | $\ge \text{Baseline Hit Rate}$ | Evaluated on identical fixture and handicap line |
| **Push Preservation** | Push Mass Accuracy | Error $\le 0.015$ | Correct discrete key number equality retention |
| **Leakage & Provenance** | Feature Timing | 100% compliance | $t_{\text{known\_at}} \le t_{\text{cutoff\_at}}$ strictly audited |
| **Prospective Shadow** | Shadow Ledger | $\ge 50$ matches / 28 days | Out-of-sample forward verification before promotion |

---

## 5. Calibration Protocol

1. **Chronological Isolation**: Calibration algorithms (Platt sigmoid, Isotonic PAVA, Beta calibration, Temperature scaling) are fit exclusively on the chronological calibration fold `CAL`.
2. **Isotonic Sample Sufficiency**: Isotonic regression requires $n \ge 200$ events per market to prevent overfitting step functions to noise. If $n < 200$, Platt scaling or Temperature scaling is mandatory.
3. **Distribution Coherence Check**: If contracts are calibrated independently, recheck that monotonicity and covering pair invariants ($P(O_{k+1}) \le P(O_k)$ and $P(\text{Home } +k) \ge P(\text{Home ML})$) remain strictly preserved.

---

## 6. October 9 implementation: what exists and what it showed

This section records the implementation of the retrospective's engineering, distribution and ML items. The thresholds in section 4 still define promotion; the evaluator now applies them with uncertainty.

**Promotion gate with uncertainty (EVL-02, EVL-03).** `FixedCohortEvaluator.evaluate` (runtime/src/common/evaluation.py) requires block identifiers (week or match day; single rows are never resampled), a minimum number of blocks, a week-block bootstrap 95% interval of delta Brier and delta log loss that lies entirely below zero, a Cox calibration slope interval that contains 1 and an intercept interval that contains 0, no deterioration of the same-line hit rate, and the same decision under every resampling seed. A calibration estimation failure fails promotion. Power at the observed sample is reported. `prospective.py` produces the same intervals for the shadow ledger.

**Engines and shared modules** (all raise on fitting failure instead of falling back to a default; none writes pickles):

| Module | Purpose |
|---|---|
| `common/distributional.py` | Distributional regression, Student-t joint score, quantile reconstruction with non-crossing (ML-02, DST-15) |
| `common/dixon_coles.py`, `strengths.py`, `ratings.py` | Dixon-Coles with time decay chosen by cross-validation (ML-04); opponent-adjusted, shrunk attack/defence strengths (DST-05); Elo, Glicko and a rating baseline (ML-07) |
| `common/calibration.py`, `calibration_layer.py` | PAVA isotonic, Platt, temperature and beta calibration with a reference test (ML-01); rolling calibration layer with slope monitoring (ML-05) |
| `common/stacking.py` | Chronological linear and logit pooling; a stack is used only if it beats the best single model on TEST (ML-10) |
| `common/boosting.py` | Dependency-free histogram gradient boosting for Poisson rates, Gaussian means and log-variance (ML-06) |
| `common/selection.py`, `endpoints.py`, `counts.py` | Joint outcome space, candidate ladder, Rank-1 gate, Rank-2 minimum joint failure, endpoint resolution (PRD-02..05, DST-02) |
| `common/bigquery_ml.py` | SQL generation for point-in-time feature joins and BOOSTED_TREE challengers only; no ARIMA_PLUS or AI.FORECAST; no project or dataset is hard-coded (ML-09) |
| `common/snapshots.py` | Hashed raw snapshots in `runtime/data/raw/<sport>/<provider>/<date>/` (SRC-06) |
| `sports/*/engine.py` | Coherent engines for soccer (with `halves.py`, `corners.py`), basketball, baseball, NHL, NFL, AFL, NRL, cricket (exact innings dynamic program with the chase stopping rule) and tennis (exact point-to-match tree with a match-level form effect) |

**Fitted receipts (ML-03).** `research/model_builds/runtime_h0/` holds a rolling-origin receipt per engine with monthly refits and point-in-time features, scored against a population baseline with week-block intervals (`python -B -m research.operations.fit_runtime_models verify`). Seven engines are fitted: NHL, NBA, MLB, NFL, NRL, AFL and EPL. Cricket and tennis are **not fitted**: the archive has scorecards and results, not ball-by-ball or serve-point data. Result: the point estimate of delta Brier favours the engine for home win in all seven, but the 95% interval lies below zero for the baseline comparison only where `INDEX.json` says so (AFL and EPL home win; AFL, EPL and MLB margin cover). On the totals contract no engine's interval lay below zero (the point estimate favours the engine in NBA, MLB, NFL and NRL and the baseline in NHL, AFL and EPL). These are development evidence on opened data. Nothing here is a promotion.

**Boosted challenger (ML-06).** `research/model_builds/runtime_h0/challenger/` compares a boosted-distribution challenger with the engine baseline on winner log loss and total CRPS for NHL, NBA, EPL and MLB. The acceptance criterion (beats the baseline on both metrics, with the 95% interval below zero, in at least two sports) is **not met**: no sport met it. NBA shows lower point estimates on both metrics, with intervals that include zero. The challenger is not used.

**What is still needed before any promotion:** prospective shadow cards under the EVL-02 gate (at least 50 matches in 28 days per contract, per section 4), cricket ball-by-ball and tennis serve-point data for the two unfitted engines, and independently audited source quorums.
