# DECISION_LAB results: EPL paper staking study (firewalled)

> **Firewall (CURRENT_RULES §5a).** Historical paper simulation only. Not betting advice, not a value claim, never read by prompts 1–3, never cited by a card, rule, rank, width or learning disposition. Raw prices stay in the local, git-excluded football-data capture; only these aggregates are committed.

Join: {'predictions': 1900, 'matched': 1730, 'ftr_mismatch': 0}. Warm-up season labels [np.int64(2021), np.int64(2022)] (method choice, sigma_p, bandit warm-up); later evaluation season labels [np.int64(2023), np.int64(2024), np.int64(2025)]. Model: `SOC-PREMIER-LEAGUE-DC-r1` prices, frozen at each week's Monday from earlier games. Taken price: Pinnacle pre-closing columns PSH/PSD/PSA; quote/capture/fill times are not verified. Close: Pinnacle closing (PSCH/PSCD/PSCA), de-vigged by **power** (warm-up closing log loss multiplicative 0.94944, power 0.94900, shin 0.94913).

## 1. Forecast benchmark: model against the no-vig market (MKT-BENCH-r1)

Three-way half-sum Brier; lower is better.

| season | MODEL | TB1 | BASELINE_LEAGUE_V1 | NOVIG_TAKEN | NOVIG_CLOSE |
|---|---|---|---|---|---|
| 2023 | 0.2798 | 0.2904 | 0.3196 | 0.2659 | 0.2625 |
| 2024 | 0.2954 | 0.3056 | 0.3276 | 0.2897 | 0.2877 |
| 2025 | 0.2988 | 0.3075 | 0.3235 | 0.2958 | 0.2955 |
| ALL | 0.2901 | 0.3001 | 0.3236 | 0.2817 | 0.2795 |


Paired differences (model − other), week-block intervals:

| model_minus | season | mean | lo | hi | k_weeks | status |
|---|---|---|---|---|---|---|
| NOVIG_CLOSE | 2023 | 0.0185 | 0.0103 | 0.0268 | 37 | ABOVE_ZERO |
| NOVIG_CLOSE | 2024 | 0.0121 | 0.0030 | 0.0211 | 36 | ABOVE_ZERO |
| NOVIG_CLOSE | 2025 | 0.0036 | -0.0040 | 0.0112 | 19 | SPANS_ZERO |
| NOVIG_CLOSE | ALL | 0.0129 | 0.0079 | 0.0180 | 92 | ABOVE_ZERO |
| NOVIG_TAKEN | 2023 | 0.0152 | 0.0072 | 0.0232 | 37 | ABOVE_ZERO |
| NOVIG_TAKEN | 2024 | 0.0089 | 0.0024 | 0.0154 | 36 | ABOVE_ZERO |
| NOVIG_TAKEN | 2025 | 0.0033 | -0.0045 | 0.0111 | 19 | SPANS_ZERO |
| NOVIG_TAKEN | ALL | 0.0103 | 0.0059 | 0.0147 | 92 | ABOVE_ZERO |
| TB1 | 2023 | -0.0109 | -0.0190 | -0.0028 | 37 | BELOW_ZERO |
| TB1 | 2024 | -0.0088 | -0.0173 | -0.0003 | 36 | BELOW_ZERO |
| TB1 | 2025 | -0.0101 | -0.0192 | -0.0010 | 19 | BELOW_ZERO |
| TB1 | ALL | -0.0099 | -0.0148 | -0.0051 | 92 | BELOW_ZERO |
| BASELINE_LEAGUE_V1 | 2023 | -0.0389 | -0.0536 | -0.0242 | 37 | BELOW_ZERO |
| BASELINE_LEAGUE_V1 | 2024 | -0.0351 | -0.0468 | -0.0233 | 36 | BELOW_ZERO |
| BASELINE_LEAGUE_V1 | 2025 | -0.0258 | -0.0409 | -0.0106 | 19 | BELOW_ZERO |
| BASELINE_LEAGUE_V1 | ALL | -0.0347 | -0.0426 | -0.0268 | 92 | BELOW_ZERO |


## 2. Staking policies (one position per match on the model's highest-EV outcome)

Estimation-error SD for Kelly shrinkage, sigma_p = **0.0663** (SD of model − no-vig close on the warm-up seasons). Caps: 2% per bet, 10% per matchweek; a drawdown over 20% halts staking pending review, and bankroll figures freeze there. CLV = taken odds × no-vig closing probability − 1. The CLV columns cover every decision the policy staked over all reported seasons, independent of the bankroll path.

| policy | n_bets | mean_clv | clv_week_lo | clv_week_hi | share_clv_positive | stake_weighted_clv | hit_rate | mean_odds | turnover | pnl | roi | final_bankroll | max_drawdown | halted_at_week |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FLAT_EV>0.03 | 845 | -0.0684 | -0.0825 | -0.0630 | 0.2438 | -0.0684 | 0.2249 | 5.3698 | 1.1734 | -0.1877 | -0.1600 | 0.8123 | 0.2111 | 2023-11-27 |
| QUARTER_KELLY_SHRUNK | 919 | -0.0656 | -0.0792 | -0.0603 | 0.2448 | -0.0595 | 0.2372 | 5.1863 | 1.1880 | -0.1237 | -0.1042 | 0.8763 | 0.2246 | 2023-11-27 |
| LINTS_BANDIT | 574 | -0.0645 | -0.0797 | -0.0569 | 0.2439 | -0.0597 | 0.2195 | 5.2253 | 0.7452 | -0.1732 | -0.2324 | 0.8268 | 0.2489 | 2023-10-23 |
| FULL_INFO_RIDGE | 59 | -0.0478 | -0.0871 | -0.0293 | 0.3051 | -0.0260 | 0.2542 | 4.3825 | 0.0206 | -0.0074 | -0.3603 | 0.9926 | 0.0091 | never |


## 3. Off-policy evaluation check

Every arm's reward (stake × CLV) is computable for every match here, so the problem is full-information and the bandit's inverse-propensity estimate can be checked against the exact value of the policy 'always quarter stake': {'exact_mean_reward': -0.00041284502517001566, 'ips_estimate': -0.00039796662066739766, 'ips_se': 7.462164664416554e-05, 'n': 970, 'bandit_arm_share': {'0.0': 0.37010309278350517, '0.25': 0.33608247422680415, '0.5': 0.29381443298969073}}.

## Reading

- These are historical development comparisons; market-relative scores or simulated profit do not establish future economic performance or causal blame.
- Feedback timing: DATE_BATCHED_CLOSE_FEEDBACK; quote/fill timestamps unverified. All same-day actions precede that day's closing-reward updates; date-only inputs still do not verify execution timing.
- Actions are sampled from the returned probability vector, so logged propensities describe the actual behaviour policy. Full-information rewards still assume observable counterfactual payoffs without market impact.
- Prices, limits, latency and account restrictions of a real operator are not modelled.

## Receipt

- `run_utc`: 2026-10-14T09:45:59Z
- `repo_head`: 980e60178ec1fb9af09b78dce8bb2f6b4cbd8897
- `code_sha256`: 645d4b4de2e1291ad1c7b9135b4f37fafa34aead2be3ba8f69939ecf5f13b442
- `python`: 3.14.6
- `numpy`: 2.5.2
- `pandas`: 3.0.5
- `scipy`: 1.18.1
- `prediction_source_sha256`: dd75d8b36ed324ba80478ee19c71a8b90752beeea17ade0d1ab3a977c837f6db
- `local_market_capture_sha256`: d1b449c2bf097d9abf517d01cc3c4d2797d6e5e1bcaa35abfd99b61798c04574
- `completed_utc`: 2026-10-14T09:46:05Z
- `rows`: 1730
