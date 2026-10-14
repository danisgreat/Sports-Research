# Model Card: `NRL-JOINT-v1`

**Model ID:** `NRL-JOINT-v1`
**Sport & Competition:** Rugby League / National Rugby League (NRL)
**Version:** `1.0.0`
**Owner:** External Quantitative Workshop
**Status:** `SHADOW`
**Registered Hypothesis:** `ML-NRL-JOINT-v1` in [HYPOTHESIS_REGISTER.md](../../../HYPOTHESIS_REGISTER.md)
**Hand-Applicability Class:** `HAND_APPLICABLE`

---

## 1. Scope & Target Contracts

- **Governing Endpoint:** `FULL_MATCH_INCL_GOLDEN_POINT` (80 minutes regulation plus 10 minutes Golden Point extra time).
- **Contracts Priced:**
  - `HEAD_TO_HEAD`: Match Winner (incl. Golden Point).
  - `LINE`: Point spread lines (-4.5 / +4.5, etc.).
  - `TOTAL_POINTS`: Match totals Over/Under (e.g. 42.5, 46.5).

---

## 2. Mathematical Specification

Discretised bivariate normal with Golden Point transition dynamics:
$$\mu_H = \text{Tries}_H \times 4 + \text{Goals}_H \times 2 + \text{FieldGoals}_H \times 1 + \gamma_{\text{home}}$$
$$\mu_A = \text{Tries}_A \times 4 + \text{Goals}_A \times 2 + \text{FieldGoals}_A \times 1$$

Golden point draws ($H_{\text{reg}} = A_{\text{reg}}$) occur in approximately 4.2% of regular-season fixtures.

---

## 3. Data & Point-in-Time Features

- **Training Population:** NRL 2018â€“2026 from `Previous Sports Results/Rugby League/NRL/` (LABEL_B observed fields).
- **Lineup Check:** Official team lists confirmed at $T-60$ minutes.

---

## 4. Comparators & Performance Acceptance

- **Comparators:** `BASELINE_LEAGUE_V1` and `TEAM_BASELINE_P` (TB-1 NRL).
- **Stage 1 Target:** NRL 2027 Rounds 1â€“8.
- **Promotion Threshold:** 95% CI upper bound of paired Brier difference $< -0.005$ across Stage 2.
