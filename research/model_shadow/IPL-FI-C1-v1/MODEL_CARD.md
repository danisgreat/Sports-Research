# Model Card: `IPL-FI-C1-v1`

**Model ID:** `IPL-FI-C1-v1`
**Sport & Competition:** Cricket / Indian Premier League (IPL)
**Version:** `1.0.0`
**Owner:** External Quantitative Workshop
**Status:** `SHADOW`
**Registered Hypothesis:** `ML-IPL-FI-C1-v1` in [HYPOTHESIS_REGISTER.md](../../../HYPOTHESIS_REGISTER.md)
**Hand-Applicability Class:** `HAND_APPLICABLE` (Negative Binomial distribution with shrunk venue adjustments printed in [PARAMETERS.md](PARAMETERS.md))

---

## 1. Scope & Target Contracts

- **Governing Endpoint:** `FIRST_INNINGS_FULL_LENGTH` (Completed 20-over first innings; void if interrupted/reduced by rain per contract terms).
- **Contracts Priced:**
  - `FIRST_INNINGS_TOTAL`: Over / Under lines (e.g. 175.5, 185.5).
  - `POWERPLAY_TOTAL`: First 6 overs total Over / Under lines (e.g. 48.5).

---

## 2. Mathematical Specification

The first innings total $Y \sim \text{NegBinomial}(\mu, \phi)$ has conditional expectation:
$$\log(\mu) = \alpha_{\text{regime}} + \theta_{\text{venue}} + \beta_{\text{toss\_order}}$$

where:
- $\alpha_{\text{regime}} = \log(178.5)$ for the post-2023 Impact Player era.
- $\theta_{\text{venue}}$ is shrunk toward the league mean via empirical Bayes partial pooling:
  $$\hat{\theta}_v = \frac{n_v}{n_v + \sigma^2 / \tau^2} \bar{y}_v + \frac{\sigma^2 / \tau^2}{n_v + \sigma^2 / \tau^2} \mu_{\text{league}}$$
- Dispersion parameter $\phi = 18.5$ reflects overdispersion ($\operatorname{Var}(Y) = \mu + \frac{\mu^2}{\phi} \approx 180 + \frac{32400}{18.5} \approx 1930$, $\text{SD} \approx 43.9$ runs).

### Pre-Toss vs. Post-Toss Mixture:
- Before the toss: mixture $0.50 \cdot F_{\text{TeamA}} + 0.50 \cdot F_{\text{TeamB}}$.
- After the toss: realised batting-first branch $F_{\text{BatFirst}}$ only.

---

## 3. Data & Point-in-Time Features

- **Training Population:** IPL 2008â€“2026 scorecards from `Previous Sports Results/Cricket/IPL/` (LABEL_B observed fields).
- **Toss Provenance:** Toss winner and decision verified from official IPL / BCCI match centres.

---

## 4. Comparators & Performance Acceptance

- **Comparators:** `BASELINE_LEAGUE_V1` (C0 empirical format climatology: 178.2 runs) and `TEAM_BASELINE_P` (TB-1-MD cricket).
- **Stage 1 Target:** IPL 2027 matches 1â€“35.
- **Promotion Threshold:** CRPS improvement over C0 with $p < 0.05$ across Stage 2.
