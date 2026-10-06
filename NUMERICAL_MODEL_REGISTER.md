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
