# Model Card: `NHL-REG-v1`

**Model ID:** `NHL-REG-v1`
**Sport & Competition:** Ice Hockey / NHL
**Version:** `1.0.0`
**Owner:** External Quantitative Workshop
**Status:** `SHADOW`
**Registered Hypothesis:** `ML-NHL-REG-v1` in [HYPOTHESIS_REGISTER.md](../../../HYPOTHESIS_REGISTER.md)
**Hand-Applicability Class:** `HAND_APPLICABLE`

---

## 1. Scope & Target Contracts

- **Governing Endpoint:** `REGULATION_60` (60 minutes regulation time; overtime/shootouts resolved as separate state transitions).
- **Contracts Priced:**
  - `MONEYLINE_3WAY`: Regulation Home Win, Regulation Tie, Regulation Away Win.
  - `MONEYLINE_2WAY`: Full match winner (incl OT/SO).
  - `TOTAL`: Game totals (Over/Under 5.5, 6.0, 6.5).
  - `HANDICAP`: Puck Line (-1.5 / +1.5).

---

## 2. Mathematical Specification

Regulation goals $(H_{\text{reg}}, A_{\text{reg}})$ are modelled as bivariate Poisson with goalie-adjusted expected rates:
$$\lambda_H = \text{ExpGoals}_H \times \text{GoalieRate}_A \times \gamma_{\text{home}}$$
$$\mu_A = \text{ExpGoals}_A \times \text{GoalieRate}_H$$

Regulation ties ($H_{\text{reg}} = A_{\text{reg}}$, frequency $\approx 22.8\%$) flow to sudden-death 3-on-3 overtime and shootout states:
$$P(\text{Home OT Win} \mid \text{Tie}) = 0.50 + \gamma_{\text{home,OT}}$$

Empty-net pulled-goalie scenarios in late regulation are handled explicitly in the goal margin distribution.

---

## 3. Data & Point-in-Time Features

- **Training Population:** NHL 2021-22 through 2025-26 from `Previous Sports Results/Ice Hockey/NHL/` (LABEL_B observed fields with repaired start times and regulation/OT goal split flags).
- **Starting Goalie Confirmation:** Verified goalie starter publication time.

---

## 4. Comparators & Performance Acceptance

- **Comparators:** `BASELINE_LEAGUE_V1` (Regulation 3-way rates: 41.5% Home, 22.8% Tie, 35.7% Away) and `TEAM_BASELINE_P`.
- **Stage 1 Target:** 8 weeks and 80 fixtures.
- **Promotion Threshold:** 95% CI upper bound of paired Brier difference $< -0.003$.
