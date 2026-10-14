# Model Card: `NBL-JOINT-v1`

**Model ID:** `NBL-JOINT-v1`
**Sport & Competition:** Basketball / National Basketball League (NBL Australia)
**Version:** `1.0.0`
**Owner:** External Quantitative Workshop
**Status:** `SHADOW`
**Registered Hypothesis:** `ML-NBL-JOINT-v1` (links RET-01 / FC10-PROFILE-v1) in [HYPOTHESIS_REGISTER.md](../../../HYPOTHESIS_REGISTER.md)
**Hand-Applicability Class:** `HAND_APPLICABLE`

---

## 1. Scope & Target Contracts

- **Governing Endpoint:** `FULL_GAME_INCL_OT` (40 minutes regulation FIBA rules plus 5-minute overtime periods).
- **Contracts Priced:**
  - `MONEYLINE_2WAY`: Home Win ($h > a$), Away Win ($h < a$).
  - `HANDICAP`: Point spread lines (e.g. -3.5 / +3.5).
  - `TOTAL`: Combined totals (Over/Under lines e.g. 176.5, 180.5).

---

## 2. Mathematical Specification

Discretised bivariate normal on integer lattice with NBL 40-minute regulation scaling and conditional total variance to correct the historical +16.8 totals overshoot documented in retrospective RET-01:
$$\mu_H = \text{Pace}_{ij} \cdot \frac{O_i \cdot D_j}{\text{League\_Pace}} + \gamma_{\text{home}}$$
$$\mu_A = \text{Pace}_{ij} \cdot \frac{O_j \cdot D_i}{\text{League\_Pace}}$$

NBL FIBA rules mean lower baseline totals than the NBA ($\approx 178$ vs $\approx 228$). Overtime frequency is approximately 5.8% historically.

---

## 3. Data & Point-in-Time Features

- **Training Population:** NBL 2022-23 through 2025-26 from `Previous Sports Results/Basketball/NBL/` (LABEL_B observed fields with 2025 repaired dates).
- **Home Advantage:** $\gamma_{\text{home}} = +3.10$ points.
- **Total Variance Scaling:** $\sigma_{\text{total}} = 14.5$ points (FIBA 40-minute scale).

---

## 4. Comparators & Performance Acceptance

- **Comparators:** `BASELINE_LEAGUE_V1` (NBL 2023â€“25 profile `LP-2026.10.11-v2`) and `TEAM_BASELINE_P` (TB-1-MD NBL).
- **Stage 1 Target:** 8 weeks and 30 fixtures.
- **Promotion Threshold:** 95% CI upper bound of paired Brier difference $< -0.005$ across Stage 2.
