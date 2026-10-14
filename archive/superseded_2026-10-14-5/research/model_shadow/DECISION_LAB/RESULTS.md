# DECISION_LAB results: EPL paper staking study (firewalled)

> **Firewall (CURRENT_RULES §5a).** Historical paper simulation only. Not betting advice, not a value claim, never read by prompts 1–3, never cited by a card, rule, rank, width or learning disposition. Raw prices stay in the local, git-excluded football-data capture; only these aggregates are committed.

Join: {'predictions': 2660, 'matched': 2490, 'ftr_mismatch': 0}. Warm-up seasons 2019-20 and 2020-21 (method choice, sigma_p, bandit warm-up); reported seasons 2021-22 to 2025-26. Model: `EPL-DC-r1` prices, frozen at each week's Monday from earlier games. Taken price: Pinnacle pre-closing (PSH/PSD/PSA, collected before the weekend). Close: Pinnacle closing (PSCH/PSCD/PSCA), de-vigged by **multiplicative** (warm-up closing log loss multiplicative 0.98460, power 0.98582, shin 0.98551).

## 1. Forecast benchmark: model against the no-vig market (MKT-BENCH-r1)

Three-way half-sum Brier; lower is better.

| season | MODEL | TB1 | BASELINE_LEAGUE_V1 | NOVIG_TAKEN | NOVIG_CLOSE |
|---|---|---|---|---|---|
| 2021 | 0.2837 | 0.2973 | 0.3242 | 0.2769 | 0.2772 |
| 2022 | 0.2966 | 0.2964 | 0.3186 | 0.2870 | 0.2856 |
| 2023 | 0.2798 | 0.2904 | 0.3196 | 0.2663 | 0.2629 |
| 2024 | 0.2954 | 0.3056 | 0.3276 | 0.2894 | 0.2875 |
| 2025 | 0.2988 | 0.3075 | 0.3235 | 0.2958 | 0.2956 |
| ALL | 0.2901 | 0.2987 | 0.3226 | 0.2818 | 0.2804 |


Paired differences (model − other), week-block intervals:

| model_minus | season | mean | lo | hi | k_weeks | status |
|---|---|---|---|---|---|---|
| NOVIG_CLOSE | 2021 | 0.0058 | -0.0009 | 0.0125 | 36 | SPANS_ZERO |
| NOVIG_CLOSE | 2022 | 0.0101 | 0.0041 | 0.0161 | 34 | ABOVE_ZERO |
| NOVIG_CLOSE | 2023 | 0.0181 | 0.0104 | 0.0259 | 37 | ABOVE_ZERO |
| NOVIG_CLOSE | 2024 | 0.0120 | 0.0034 | 0.0206 | 36 | ABOVE_ZERO |
| NOVIG_CLOSE | 2025 | 0.0034 | -0.0039 | 0.0106 | 19 | SPANS_ZERO |
| NOVIG_CLOSE | ALL | 0.0106 | 0.0073 | 0.0139 | 162 | ABOVE_ZERO |
| NOVIG_TAKEN | 2021 | 0.0051 | -0.0028 | 0.0129 | 36 | SPANS_ZERO |
| NOVIG_TAKEN | 2022 | 0.0090 | 0.0030 | 0.0150 | 34 | ABOVE_ZERO |
| NOVIG_TAKEN | 2023 | 0.0149 | 0.0075 | 0.0223 | 37 | ABOVE_ZERO |
| NOVIG_TAKEN | 2024 | 0.0090 | 0.0029 | 0.0150 | 36 | ABOVE_ZERO |
| NOVIG_TAKEN | 2025 | 0.0031 | -0.0043 | 0.0105 | 19 | SPANS_ZERO |
| NOVIG_TAKEN | ALL | 0.0088 | 0.0057 | 0.0119 | 162 | ABOVE_ZERO |
| TB1 | 2021 | -0.0123 | -0.0195 | -0.0051 | 36 | BELOW_ZERO |
| TB1 | 2022 | -0.0026 | -0.0138 | 0.0086 | 34 | SPANS_ZERO |
| TB1 | 2023 | -0.0109 | -0.0190 | -0.0028 | 37 | BELOW_ZERO |
| TB1 | 2024 | -0.0088 | -0.0173 | -0.0003 | 36 | BELOW_ZERO |
| TB1 | 2025 | -0.0101 | -0.0192 | -0.0010 | 19 | BELOW_ZERO |
| TB1 | ALL | -0.0089 | -0.0128 | -0.0050 | 162 | BELOW_ZERO |
| BASELINE_LEAGUE_V1 | 2021 | -0.0341 | -0.0491 | -0.0191 | 36 | BELOW_ZERO |
| BASELINE_LEAGUE_V1 | 2022 | -0.0255 | -0.0394 | -0.0117 | 34 | BELOW_ZERO |
| BASELINE_LEAGUE_V1 | 2023 | -0.0389 | -0.0536 | -0.0242 | 37 | BELOW_ZERO |
| BASELINE_LEAGUE_V1 | 2024 | -0.0351 | -0.0468 | -0.0233 | 36 | BELOW_ZERO |
| BASELINE_LEAGUE_V1 | 2025 | -0.0258 | -0.0409 | -0.0106 | 19 | BELOW_ZERO |
| BASELINE_LEAGUE_V1 | ALL | -0.0326 | -0.0388 | -0.0265 | 162 | BELOW_ZERO |


## 2. Staking policies (one position per match on the model's highest-EV outcome)

Estimation-error SD for Kelly shrinkage, sigma_p = **0.0654** (SD of model − no-vig close on the warm-up seasons). Caps: 2% per bet, 10% per matchweek; a drawdown over 20% halts staking pending review, and bankroll figures freeze there. CLV = taken odds × no-vig closing probability − 1. The CLV columns cover every decision the policy staked over all reported seasons, independent of the bankroll path.

| policy | n_bets | mean_clv | clv_week_lo | clv_week_hi | share_clv_positive | stake_weighted_clv | hit_rate | mean_odds | turnover | pnl | roi | final_bankroll | max_drawdown | halted_at_week |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FLAT_EV>0.03 | 1524 | -0.0324 | -0.0416 | -0.0276 | 0.3399 | -0.0324 | 0.2290 | 5.5613 | 1.2612 | -0.2311 | -0.1832 | 0.7689 | 0.2311 | 2021-12-13 |
| QUARTER_KELLY_SHRUNK | 1659 | -0.0318 | -0.0406 | -0.0275 | 0.3388 | -0.0329 | 0.2405 | 5.3669 | 0.7743 | -0.2056 | -0.2655 | 0.7944 | 0.2056 | 2021-11-15 |
| LINTS_BANDIT | 1108 | -0.0313 | -0.0400 | -0.0242 | 0.3421 | -0.0298 | 0.2527 | 5.3843 | 0.9626 | -0.0822 | -0.0854 | 0.9178 | 0.2045 | 2021-12-06 |
| FULL_INFO_RIDGE | 248 | -0.0003 | -0.0376 | 0.0134 | 0.4718 | 0.0126 | 0.1089 | 9.8658 | 0.7083 | -0.2125 | -0.3000 | 0.7875 | 0.2360 | 2021-11-29 |


## 3. Off-policy evaluation check

Every arm's reward (stake × CLV) is computable for every match here, so the problem is full-information and the bandit's inverse-propensity estimate can be checked against the exact value of the policy 'always quarter stake': {'exact_mean_reward': -0.0002340478308322138, 'ips_estimate': -0.0003022683678428196, 'ips_se': 4.748551342382948e-05, 'n': 1730, 'bandit_arm_share': {'0.0': 0.3236994219653179, '0.25': 0.34046242774566476, '0.5': 0.33583815028901737}}.

## Reading

- A policy can only be as good as the forecasts it sizes. Section 1 states whether those forecasts beat the no-vig market; if they do not, positive closing-line value is not expected, and any profit is variance.
- The bandit learns from CLV, which is known before the result; the full-information learner uses the same rewards for every arm and is the fairer learner for this setting.
- Prices, limits, latency and account restrictions of a real operator are not modelled.

## Receipt

- `run_utc`: 2026-10-14T07:33:40Z
- `repo_head`: 3ab6d27fedb177add7cca5b41b14346107688ce3
- `code_sha256`: 8cb5bdb1c32a361d2ded8488a8f434690a4ab2ee807046e1ab8e465959353da2
- `python`: 3.14.6
- `numpy`: 2.5.2
- `pandas`: 3.0.5
- `scipy`: 1.18.1
- `rows`: 2490
