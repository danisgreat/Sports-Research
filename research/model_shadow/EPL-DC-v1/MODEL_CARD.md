# Model Card: `EPL-DC-v1`

**Model ID:** `EPL-DC-v1`
**Sport & Competition:** Soccer / English Premier League (EPL)
**Version:** `1.0.0`
**Owner:** External Quantitative Workshop
**Status:** `SHADOW` (Informational evaluation only; never anchors or adjusts live cards)
**Registered Hypothesis:** `ML-EPL-DC-v1` in [HYPOTHESIS_REGISTER.md](../../../HYPOTHESIS_REGISTER.md)
**Hand-Applicability Class:** `HAND_APPLICABLE` (Poisson parameters and $\tau$ table printed in [PARAMETERS.md](PARAMETERS.md))

---

## 1. Scope & Target Contracts

- **Governing Endpoint:** `REGULATION_90` (90 minutes plus official stoppage time; excludes extra time and penalties).
- **Contracts Priced from Unified State:**
  - `MONEYLINE_3WAY`: Home Win ($h > a$), Draw ($h = a$), Away Win ($h < a$).
  - `TOTAL`: Over / Under standard lines ($1.5, 2.5, 3.5$).
  - `HANDICAP`: Asian handicap lines ($0.0, -0.5/+0.5, -1.0/+1.0, -1.5/+1.5$).
  - `BOTH_TEAMS_TO_SCORE`: Yes ($h \ge 1 \land a \ge 1$) / No.

All contracts are derived as exact deterministic projections from the joint bivariate goal probability matrix $P(H=h, A=a) \in \mathbb{R}^{10 \times 10}$.

---

## 2. Mathematical Specification

The expected goals for home team $i$ and away team $j$ are modeled as:
$$\log(\lambda_{ij}) = \mu + \alpha_i + \beta_j + \gamma_{\text{home}}$$
$$\log(\mu_{ij}) = \mu + \alpha_j + \beta_i$$

where $\alpha_i$ is attack strength, $\beta_i$ is defense strength, $\gamma_{\text{home}}$ is the home advantage, subject to identifiability constraint $\sum_{k} \alpha_k = 0$.

### Low-Score Dependence Correction ($\tau$ Function):
$$P(H=h, A=a) = \tau(h, a, \lambda, \mu, \rho) \cdot \frac{\lambda^h e^{-\lambda}}{h!} \cdot \frac{\mu^a e^{-\mu}}{a!}$$

where $\tau(h, a) = 1$ for all scores except:
- $\tau(0, 0) = 1 - \lambda \mu \rho$
- $\tau(0, 1) = 1 + \lambda \rho$
- $\tau(1, 0) = 1 + \mu \rho$
- $\tau(1, 1) = 1 - \rho$

Parameters are fitted via maximum likelihood with exponential time decay:
$$w_k = \exp(-\xi \cdot \Delta t_k)$$
where decay parameter $\xi$ is chosen strictly on historical development seasons.

---

## 3. Data & Point-in-Time Features

- **Training Population:** Historical EPL seasons 1993-94 through 2025-26 from `Previous Sports Results/Soccer/EPL/` (LABEL_B observed fields).
- **Known-at Rule:** Only matches completed strictly prior to the scheduled kickoff date are admitted. No post-match adjustments or full-season aggregates.
- **Lineups:** Pregame base distribution conditions on regular squad rotation; starting lineups verified at $T-60$ minutes trigger parameter updates if major regulars are confirmed absent.

---

## 4. Comparators & Performance Acceptance

- **Comparators:**
  - `BASELINE_LEAGUE_V1`: Frozen 3-year rolling league rates ($H=0.455, D=0.235, A=0.310$).
  - `TEAM_BASELINE_P`: Hand-computable TB-1 goal margin baseline.
- **Stage 1 Target:** Minimum 8 weeks and 40 fixtures to estimate weekly variance $\text{SD}_w$.
- **Promotion Threshold:** 95% CI upper bound of paired Brier difference $< -0.005$ against both comparators across a sized Stage 2.
