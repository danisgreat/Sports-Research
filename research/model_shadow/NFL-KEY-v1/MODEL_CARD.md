# Model Card: `NFL-KEY-v1`

**Model ID:** `NFL-KEY-v1`
**Sport & Competition:** American Football / NFL
**Version:** `1.0.0`
**Owner:** External Quantitative Workshop
**Status:** `SHADOW`
**Registered Hypothesis:** `ML-NFL-KEY-v1` in [HYPOTHESIS_REGISTER.md](../../../HYPOTHESIS_REGISTER.md)
**Hand-Applicability Class:** `HAND_APPLICABLE` (Key number mass tables and margin/total parameters in [PARAMETERS.md](PARAMETERS.md))

---

## 1. Scope & Target Contracts

- **Governing Endpoint:** `FULL_GAME_INCL_OT` (60 minutes regulation plus NFL regular-season overtime rules; ties allowed).
- **Contracts Priced:**
  - `MONEYLINE_2WAY`: Home Win / Away Win (ties treated under contract push rules).
  - `HANDICAP`: Point spread lines (notably key numbers 3, 7, 10, 6, 14).
  - `TOTAL`: Game totals Over/Under (e.g. 43.5, 47.5).

---

## 2. Mathematical Specification

Because scoring in American football occurs primarily in chunks of 3 (field goal) and 7 (touchdown + PAT), continuous normal models misprice spreads near key numbers. `NFL-KEY-v1` rescales an empirical historical margin distribution conditioned on team strengths $\theta_H, \theta_A$:
$$M \sim \mathcal{D}_{\text{NFL-Key}}(\mu_M, \sigma_M), \quad \mu_M = (\theta_H - \theta_A) + \gamma_{\text{home}}$$

Key number masses ($P(M = 3) \approx 0.152$, $P(M = 7) \approx 0.098$, $P(M = 10) \approx 0.058$) are preserved explicitly on integer boundaries.

---

## 3. Data & Point-in-Time Features

- **Training Population:** NFL 2018â€“2025 from `Previous Sports Results/American Football/NFL/` (LABEL_B observed fields with nflverse results; all market columns stripped).
- **Quarterback Availability:** QB starter confirmation verified at $T-90$ minutes.

---

## 4. Comparators & Performance Acceptance

- **Comparators:** `BASELINE_LEAGUE_V1` and `TEAM_BASELINE_P` (TB-1 NFL).
- **Stage 1 Target:** 8 weeks and 60 fixtures.
- **Promotion Threshold:** 95% CI upper bound of paired Brier difference $< -0.005$ across Stage 2.
