# Model Card: `MLB-NB-v1`

**Model ID:** `MLB-NB-v1`
**Sport & Competition:** Baseball / Major League Baseball (MLB)
**Version:** `1.0.0`
**Owner:** External Quantitative Workshop
**Status:** `SHADOW`
**Registered Hypothesis:** `ML-MLB-NB-v1` in [HYPOTHESIS_REGISTER.md](../../../HYPOTHESIS_REGISTER.md)
**Hand-Applicability Class:** `HAND_APPLICABLE`

---

## 1. Scope & Target Contracts

- **Governing Endpoint:** `FULL_GAME_INCL_EXTRAS` (Official 9-inning game plus extra innings if tied; home 9th-inning stopping rule enforced).
- **Contracts Priced:**
  - `MONEYLINE_2WAY`: Home Win ($h > a$), Away Win ($h < a$). No ties in official MLB games.
  - `RUN_LINE`: Spread lines (-1.5 / +1.5).
  - `TOTAL`: Game totals Over/Under (e.g. 7.5, 8.5).

---

## 2. Mathematical Specification

Team runs $(H, A)$ are modelled as Negative Binomial distributions with starting pitcher, bullpen, and park factor components:
$$\log(\mu_H) = \alpha_{\text{park}} + \theta_{\text{bat}, H} - \eta_{\text{pitcher}, A} + \gamma_{\text{home}}$$
$$\log(\mu_A) = \alpha_{\text{park}} + \theta_{\text{bat}, A} - \eta_{\text{pitcher}, H}$$

### Home Final Half-Inning Stopping Rule:
If the home team leads after the top of the 9th inning ($H > A$ after 8.5 innings), the bottom of the 9th is unplayed. If tied, walk-off plate appearances terminate the game immediately.

---

## 3. Data & Point-in-Time Features

- **Training Population:** MLB 2018â€“2026 from `Previous Sports Results/Baseball/MLB/` (LABEL_A receipt-verified, 65,008 rows). Doubleheaders segregated by native game number.
- **Starting Pitchers:** Confirmed SP announced and verified at $T-90$ minutes.

---

## 4. Comparators & Performance Acceptance

- **Comparators:** `BASELINE_LEAGUE_V1` and `TEAM_BASELINE_P` (TB-1 MLB).
- **Stage 1 Target:** MLB 2027 Opening 100 games.
- **Promotion Threshold:** 95% CI upper bound of paired Brier difference $< -0.002$ across Stage 2.
