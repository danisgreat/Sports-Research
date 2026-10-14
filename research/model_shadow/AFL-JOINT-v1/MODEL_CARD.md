# Model Card: `AFL-JOINT-v1`

**Model ID:** `AFL-JOINT-v1`
**Sport & Competition:** Australian Rules Football / Australian Football League (AFL)
**Version:** `1.0.0`
**Owner:** External Quantitative Workshop
**Status:** `SHADOW`
**Registered Hypothesis:** `ML-AFL-JOINT-v1` in [HYPOTHESIS_REGISTER.md](../../../HYPOTHESIS_REGISTER.md)
**Hand-Applicability Class:** `HAND_APPLICABLE`

---

## 1. Scope & Target Contracts

- **Governing Endpoint:** `FULL_MATCH_REGULATION` (Regular season matches allow draws; finals have extra time). Total score derived from $6 \times \text{Goals} + \text{Behinds}$.
- **Contracts Priced:**
  - `MONEYLINE_3WAY`: Home Win ($h > a$), Draw ($h = a$), Away Win ($h < a$).
  - `HANDICAP`: Line betting (e.g. -14.5 / +14.5).
  - `TOTAL`: Match total points Over/Under (e.g. 165.5).

---

## 2. Mathematical Specification

Discretised bivariate normal on total points with goals-and-behinds scoring shot conversion:
$$\mu_H = \text{Shots}_H \times (6 \cdot p_{G,H} + p_{B,H}) + \gamma_{\text{home}}$$
$$\mu_A = \text{Shots}_A \times (6 \cdot p_{G,A} + p_{B,A})$$

Historical AFL scoring variance is high ($\sigma_{\text{margin}} \approx 32.5$, $\sigma_{\text{total}} \approx 28.0$), with draw probability $\approx 0.85\%$.

---

## 3. Data & Point-in-Time Features

- **Training Population:** AFL 2015â€“2026 from `Previous Sports Results/AFL/` (LABEL_A receipt-verified, 16,637 rows).
- **Interstate Travel & Ground Dimensions:** Venue dimensions (MCG vs GMHBA) and interstate travel penalties.
- **Lineups:** Final 22 confirmed at $T-60$ minutes.

---

## 4. Comparators & Performance Acceptance

- **Comparators:** `BASELINE_LEAGUE_V1` and `TEAM_BASELINE_P` (TB-1 AFL).
- **Stage 1 Target:** AFL 2027 Rounds 1â€“8.
- **Promotion Threshold:** 95% CI upper bound of paired Brier difference $< -0.005$ across Stage 2.
