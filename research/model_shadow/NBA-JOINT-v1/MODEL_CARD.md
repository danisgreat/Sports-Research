# Model Card: `NBA-JOINT-v1`

**Model ID:** `NBA-JOINT-v1`
**Sport & Competition:** Basketball / NBA
**Version:** `1.0.0`
**Owner:** External Quantitative Workshop
**Status:** `SHADOW`
**Registered Hypothesis:** `ML-NBA-JOINT-v1` in [HYPOTHESIS_REGISTER.md](../../../HYPOTHESIS_REGISTER.md)
**Hand-Applicability Class:** `HAND_APPLICABLE` (Discretised joint normal parameters printed in [PARAMETERS.md](PARAMETERS.md))

---

## 1. Scope & Target Contracts

- **Governing Endpoint:** `FULL_GAME_INCL_OT` (Full 48 minutes regulation plus all required overtime periods).
- **Contracts Priced from Unified State:**
  - `MONEYLINE_2WAY`: Home Win ($h > a$), Away Win ($h < a$). No draw permitted under NBA rules.
  - `TOTAL`: Over / Under lines (e.g. 222.5, 226.5).
  - `HANDICAP`: Point spreads (e.g. -4.5 / +4.5).

---

## 2. Mathematical Specification

Team scores $(H, A)$ are modelled as a bivariate normal distribution discretised onto the integer lattice $\mathbb{Z}^2$ with parity constraints:
$$\begin{pmatrix} H \\ A \end{pmatrix} \sim \mathcal{N}\left( \begin{pmatrix} \mu_H \\ \mu_A \end{pmatrix}, \begin{pmatrix} \sigma_H^2 & \rho \sigma_H \sigma_A \\ \rho \sigma_H \sigma_A & \sigma_A^2 \end{pmatrix} \right)$$

Expected team points condition on pace ($P$) and offensive/defensive efficiency ($O_i, D_j$):
$$\mu_H = \text{Pace}_{ij} \cdot \frac{O_i \cdot D_j}{\text{League\_Pace}} + \gamma_{\text{home}}$$
$$\mu_A = \text{Pace}_{ij} \cdot \frac{O_j \cdot D_i}{\text{League\_Pace}}$$

### Regulation Ties & Overtime Branch:
If regulation yields $H_{\text{reg}} = A_{\text{reg}}$, probability mass flows to a 5-minute overtime state space:
$$P(\text{Home Win}) = P(H_{\text{reg}} > A_{\text{reg}}) + P(H_{\text{reg}} = A_{\text{reg}}) \cdot P(\text{Home Win} \mid \text{OT})$$
where $P(\text{Home Win} \mid \text{OT}) = 0.50 + 0.04 \cdot \frac{\mu_H - \mu_A}{\sigma_{\text{margin}}}$.

---

## 3. Data & Point-in-Time Features

- **Training Population:** NBA regular seasons 2021-22 through 2025-26 from `Previous Sports Results/Basketball/NBA/` (LABEL_B observed fields).
- **Schedule Rest Factors:** Rest days ($0, 1, 2, 3+$), back-to-back flags, and travel miles.
- **Lineup Check:** Confirmed starting 5 and injury reports captured at $T-30$ minutes.

---

## 4. Comparators & Performance Acceptance

- **Comparators:**
  - `BASELINE_LEAGUE_V1`: Frozen 3-season league home win rate (0.552) and format total mean.
  - `TEAM_BASELINE_P`: Hand-computable TB-1 basketball margin baseline.
- **Stage 1 Target:** 8 weeks and 80 fixtures.
- **Promotion Threshold:** 95% CI upper bound of paired Brier difference $< -0.005$ across Stage 2.
