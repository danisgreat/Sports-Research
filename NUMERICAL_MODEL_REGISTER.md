# Numerical Model Register & Portfolio Specification

**Authority:** MDS-2026.10.01-v8.0 / CR-2026.10.06-NUMERICAL-1.
**Status:** Mandatory Register for all Numerical ML Model Architectures, Engines, and Promotion Gates.

---

## 1. Algorithm Portfolio Architecture (A0–A8 & BigQuery ML)

The system enforces a tiered algorithm portfolio where the central engine generates a coherent predictive outcome distribution, and machine learning models challenge and refine it.

```text
       [ A0: Simple Empirical Baseline ]  (Venue / Season Rate × Exposure)
                      │
                      ▼
       [ A1: Regularized Hierarchical GLM ]  (Shrunk priors & team strengths)
                      │
                      ▼
  ★  [ A2: Generative Distribution Simulator ]  (CENTRAL MODEL: Simulates match events)
                      │
       ┌──────────────┴──────────────┐
       ▼                             ▼
 [ A3: CatBoost Challenger ]   [ A4: XGBoost / LightGBM ]
       │                             │
       └──────────────┬──────────────┘
                      ▼
        [ BigQuery ML Cloud Engine ] (AI.FORECAST / ARIMA_PLUS / Vertex AI)
                      │
                      ▼
         [ A6: Chronological Ensemble ] (Out-of-fold weighted consensus)
                      │
                      ▼
      [ Probability Calibration Layer ] (Platt Sigmoid / Isotonic / Temp Scaling)
                      │
                      ▼
          [ Contract Derivation Engine ] (O/U, Spreads, 1X2, Moneylines)
```

### Model Descriptions

| ID | Model Type | Core Technology | Operational Role | Target Scope |
|---|---|---|---|---|
| **A0** | Empirical Baseline | Empirical rate × exposure | Simple comparator baseline; no model is promoted unless beating A0 | Expected score, rate per min/possession |
| **A1** | Hierarchical GLM | Poisson / Negative Binomial GLM with L2 penalty | Ridge regression with Bayesian team-strength shrinkage | Team scores, total runs/points |
| **A2** | **Central Simulator** | Sport-native Monte Carlo / Discrete Markov Chain | **Core generative model**: Simulates possessions, drives, balls, shots into full PMF | Full joint score & outcome distribution |
| **A3** | Gradient Boosted Trees | CatBoost with ordered boosting | Non-linear feature interactions, handles high-cardinality categorical entities | Target distribution adjustments |
| **A4** | Gradient Boosted Trees | LightGBM / XGBoost | Fast feature ablations, split-loss evaluation, quantile regression | Conditional quantiles (10th, 50th, 90th) |
| **A5** | Ranking Model | LambdaMART / Pairwise ranker | Supply-to-rank optimization over candidate sets | Candidate row priority |
| **A6** | Out-Of-Fold Ensemble | Stacking regressor / mixture model | Chronological combination of A2 + A3/A4 on out-of-fold predictions | Ensembled target PMF |
| **A7** | Portfolio Optimizer | Constrained top-two selection | Optimizes joint hit rate and risk diversification across card rows | Top-two selection |
| **A8** | Deep Listwise | Transformer / ListNet | Deferred: Requires massive sample size (n > 50,000) | Long-term research only |
| **BQML** | Cloud ML Engine | BigQuery AI / Vertex AI / `AI.FORECAST` | Cloud-scale time-series forecasting and remote LLM extraction | Enterprise feature store & forecast |

---

## 2. Core Architectural Invariant: Event Distribution First

1. **No Direct Betting Line Models**: Models must never be trained directly as binary classifiers on bookmaker lines (e.g. `is_over_221_5 = 1`).
2. **Distribution Estimation**: The model estimates the discrete probability mass function (PMF) of the underlying sporting event $P(Y = y \mid X)$.
3. **Analytical Contract Derivation**: Every contract proposition (Over/Under, Spread, Moneyline, 1X2) is calculated directly as a tail sum or integral of the generated PMF.
4. **Guaranteed Monotonicity**:
   $$P(\text{Over } K_2) \le P(\text{Over } K_1) \quad \text{for any } K_2 > K_1$$
   $$\sum P(\text{1X2}) = 1.0 \quad \text{and} \quad P(\text{Team A}) + P(\text{Team B}) = 1.0$$

---

## 3. Strict Model Promotion Criteria

A challenger model ($M_{cand}$) will **never** be promoted over a baseline ($M_{base}$) on simple win rate or short-term lucky streaks. Promotion requires meeting **all** of the following quantitative conditions on the untouched `TEST` fold:

| Evaluation Dimension | Metric | Required Threshold | Verification Method |
|---|---|---|---|
| **Probabilistic Accuracy** | Brier Score | $\Delta \text{Brier} \le -0.010$ (Lower is better) | Paired test across identical fixtures |
| **Information Loss** | Log Loss | $\Delta \text{LogLoss} \le 0.0$ (No deterioration) | Strict penalty on overconfident errors |
| **Distribution Quality** | CRPS | $\Delta \text{CRPS} < 0.0$ | Continuous Ranked Probability Score |
| **Calibration Quality** | Calibration Slope | $0.90 \le \beta \le 1.10$ | Logistic calibration fit |
| **Calibration Quality** | Calibration Intercept | $|\alpha| \le 0.05$ | Logistic calibration fit |
| **Interval Reliability** | 80% Coverage | $75.0\% \le \text{Coverage} \le 85.0\%$ | Central quantile check |
| **Slice Invariance** | Slice Performance | No critical demographic/regime degradation | Homogeneous performance across teams |
| **Leakage & Provenance** | Feature Timing | 100% compliance with $known\_at \le cutoff\_at$ | Automated audit via feature store |
| **Prospective Shadow** | Shadow Verification | $\ge 50$ prospective predictions across $\ge 28$ days | Frozen shadow ledger |

---

## 4. Model Output Specification

Every model prediction emitted by the runtime generates a standardized JSON payload:

```json
{
  "model_version": "Cricket-Test-v3.4",
  "cutoff_utc": "2026-10-06T00:26:13Z",
  "calibration_id": "CAL-CRICKET-v2",
  "state": "PREGAME",
  "underlying_forecast": {
    "metric": "first_innings_runs",
    "expected_value": 221.7,
    "median": 218.0,
    "std_dev": 45.2,
    "intervals": {
      "50_percent": [190.0, 249.0],
      "80_percent": [166.0, 284.0],
      "95_percent": [135.0, 312.0]
    }
  },
  "contracts": [
    {"contract_id": "C01", "type": "OVER", "threshold": 185.5, "prob_win": 0.778, "prob_push": 0.0, "prob_loss": 0.222},
    {"contract_id": "C02", "type": "OVER", "threshold": 235.5, "prob_win": 0.391, "prob_push": 0.0, "prob_loss": 0.609},
    {"contract_id": "C03", "type": "UNDER", "threshold": 235.5, "prob_win": 0.609, "prob_push": 0.0, "prob_loss": 0.391},
    {"contract_id": "C04", "type": "UNDER", "threshold": 285.5, "prob_win": 0.893, "prob_push": 0.0, "prob_loss": 0.107}
  ],
  "market_benchmark": {
    "target_contract": "C03",
    "observed_odds": 1.91,
    "market_implied_prob": 0.5236,
    "devigged_fair_prob": 0.5080,
    "model_prob": 0.6090,
    "raw_edge": 0.1010,
    "uncertainty_band": 0.0420,
    "actionability": "VALUE_SUPPORTED"
  }
}
```

