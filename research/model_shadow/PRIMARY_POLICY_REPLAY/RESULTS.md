# Primary policy replay: random expert selection (Exp3) versus a full-information mixture

**Evidence class: `HISTORICAL_DEVELOPMENT`.** Market-free; not a card input. Question: given the primary runtime's own three experts (ml/primary.py), which way of producing ONE primary distribution is more accurate? Method and policies: module docstring of `ml/evaluation/primary_replay.py`. Every policy is scored on identical games (unseen teams excluded, as the runtime refuses them) and identical questions. Primary metric: home-win Brier per game (lower is better). Intervals: t-intervals over ISO-week means of game differences (SCORING_AND_VALIDATION §5); test seasons only; eta chosen on tune seasons only.

**Pooled over all competitions:** HEDGE_MIX − EXP3_SELECT = -0.0081 [-0.0087, -0.0074] over 1909 competition-weeks (BELOW_ZERO).

Why a mixture cannot lose to random selection with the same weights: Brier and log loss are convex in p, so the expected score of a randomly selected expert is never better than the score of the probability-weighted mixture (Jensen's inequality). Exp3 additionally ignores the other experts' observable losses, although every bundle freezes all three grids.

| competition | n_test | eta | EXP3_SELECT | FAST | SLOW | BASELINE | EQUAL_MIX | HEDGE_MIX | hedge_minus_exp3 | lo | hi | status | best_single | hedge_minus_best | best_lo | best_hi | best_status | exp3_p_baseline | hedge_w_baseline | warnings |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AFL/AFL | 621 | 1.0000 | 0.2143 | 0.2055 | 0.2004 | 0.2456 | 0.2013 | 0.2032 | -0.0112 | -0.0142 | -0.0082 | BELOW_ZERO | SLOW | 0.0020 | -0.0027 | 0.0067 | SPANS_ZERO | 0.2672 | 0.0000 |  |
| AFL/AFLW | 261 | 50.0000 | 0.2189 | 0.2094 | 0.2021 | 0.2506 | 0.2025 | 0.2021 | -0.0165 | -0.0256 | -0.0075 | BELOW_ZERO | SLOW | 0.0000 | 0.0000 | 0.0000 | SPANS_ZERO | 0.2950 | 0.0000 |  |
| American Football/NFL | 816 | 0.5000 | 0.2337 | 0.2271 | 0.2282 | 0.2490 | 0.2264 | 0.2265 | -0.0073 | -0.0092 | -0.0055 | BELOW_ZERO | FAST | -0.0007 | -0.0028 | 0.0014 | SPANS_ZERO | 0.2849 | 0.0023 |  |
| Baseball/KBO | 2187 | 0.5000 | 0.2499 | 0.2505 | 0.2487 | 0.2507 | 0.2492 | 0.2488 | -0.0012 | -0.0017 | -0.0008 | BELOW_ZERO | SLOW | 0.0001 | -0.0004 | 0.0006 | SPANS_ZERO | 0.3067 | 0.1366 |  |
| Baseball/MLB | 7288 | 0.5000 | 0.2465 | 0.2453 | 0.2448 | 0.2499 | 0.2446 | 0.2445 | -0.0021 | -0.0028 | -0.0014 | BELOW_ZERO | SLOW | -0.0003 | -0.0007 | 0.0001 | SPANS_ZERO | 0.3039 | 0.0000 |  |
| Baseball/Minor Leagues | 6462 | 0.5000 | 0.2496 | 0.2498 | 0.2490 | 0.2501 | 0.2490 | 0.2490 | -0.0001 | -0.0009 | 0.0007 | SPANS_ZERO | SLOW | -0.0000 | -0.0000 | 0.0000 | SPANS_ZERO | 0.3071 | 0.0001 |  |
| Baseball/NPB | 2565 | 0.5000 | 0.2496 | 0.2495 | 0.2483 | 0.2514 | 0.2485 | 0.2484 | -0.0012 | -0.0019 | -0.0005 | BELOW_ZERO | SLOW | 0.0003 | -0.0004 | 0.0009 | SPANS_ZERO | 0.2948 | 0.0173 |  |
| Basketball/Austria Basketball Bundesliga | 396 | 50.0000 | 0.1454 | 0.1345 | 0.1238 | 0.1851 | 0.1272 | 0.1238 | -0.0217 | -0.0283 | -0.0150 | BELOW_ZERO | SLOW | 0.0000 | 0.0000 | 0.0000 | SPANS_ZERO | 0.2928 | 0.0000 | OVERTIME_FIELD_IMPLAUSIBLE:0/909 |
| Basketball/B League | 2212 | 20.0000 | 0.2134 | 0.2045 | 0.2106 | 0.2496 | 0.2059 | 0.2045 | -0.0088 | -0.0104 | -0.0071 | BELOW_ZERO | FAST | 0.0000 | 0.0000 | 0.0000 | SPANS_ZERO | 0.1454 | 0.0000 |  |
| Basketball/EuroBasket | 138 | 0.5000 | 0.2600 | 0.2629 | 0.2529 | 0.2639 | 0.2574 | 0.2582 | -0.0017 | -0.0066 | 0.0032 | INSUFFICIENT_EVIDENCE | SLOW | 0.0010 | -0.0168 | 0.0188 | INSUFFICIENT_EVIDENCE | 0.3291 | 0.2736 |  |
| Basketball/EuroCup | 523 | 50.0000 | 0.2208 | 0.2135 | 0.2103 | 0.2448 | 0.2110 | 0.2103 | -0.0098 | -0.0145 | -0.0051 | BELOW_ZERO | SLOW | 0.0000 | 0.0000 | 0.0000 | SPANS_ZERO | 0.2695 | 0.0000 |  |
| Basketball/EuroLeague | 979 | 1.0000 | 0.2179 | 0.2141 | 0.2116 | 0.2321 | 0.2121 | 0.2134 | -0.0047 | -0.0066 | -0.0029 | BELOW_ZERO | SLOW | 0.0016 | -0.0016 | 0.0047 | SPANS_ZERO | 0.2597 | 0.0000 | OVERTIME_FIELD_IMPLAUSIBLE:0/1718 |
| Basketball/Greek Basket League | 416 | 2.0000 | 0.1889 | 0.1789 | 0.1647 | 0.2401 | 0.1698 | 0.1654 | -0.0236 | -0.0286 | -0.0185 | BELOW_ZERO | SLOW | 0.0007 | 0.0001 | 0.0013 | ABOVE_ZERO | 0.2492 | 0.0000 | OVERTIME_FIELD_IMPLAUSIBLE:1/812;IMPLAUSIBLE_SCORE_DISPERSION:1977,1978,1979,1980,1981,1982,1983,1984,1985,2000,2001,2004,2005,2006 |
| Basketball/KBL | 807 | 2.0000 | 0.2355 | 0.2302 | 0.2315 | 0.2478 | 0.2298 | 0.2304 | -0.0050 | -0.0078 | -0.0022 | BELOW_ZERO | FAST | 0.0001 | -0.0005 | 0.0006 | SPANS_ZERO | 0.2724 | 0.0000 |  |
| Basketball/Liga ACB | 908 | 1.0000 | 0.2102 | 0.2036 | 0.1984 | 0.2395 | 0.2001 | 0.1990 | -0.0113 | -0.0136 | -0.0090 | BELOW_ZERO | SLOW | 0.0006 | -0.0006 | 0.0017 | SPANS_ZERO | 0.2382 | 0.0000 |  |
| Basketball/NBA | 3692 | 50.0000 | 0.2222 | 0.2118 | 0.2230 | 0.2479 | 0.2160 | 0.2118 | -0.0104 | -0.0118 | -0.0090 | BELOW_ZERO | FAST | 0.0000 | 0.0000 | 0.0000 | SPANS_ZERO | 0.1774 | 0.0000 |  |
| Basketball/NBA G League | 1599 | 2.0000 | 0.2417 | 0.2385 | 0.2400 | 0.2486 | 0.2381 | 0.2385 | -0.0029 | -0.0048 | -0.0010 | BELOW_ZERO | FAST | -0.0000 | -0.0000 | 0.0000 | SPANS_ZERO | 0.2610 | 0.0000 |  |
| Basketball/NBL | 450 | 5.0000 | 0.2349 | 0.2276 | 0.2314 | 0.2485 | 0.2284 | 0.2276 | -0.0078 | -0.0123 | -0.0033 | BELOW_ZERO | FAST | -0.0000 | -0.0000 | 0.0000 | SPANS_ZERO | 0.2969 | 0.0000 |  |
| Basketball/WNBA | 768 | 1.0000 | 0.2289 | 0.2149 | 0.2287 | 0.2488 | 0.2193 | 0.2164 | -0.0131 | -0.0163 | -0.0100 | BELOW_ZERO | FAST | 0.0016 | -0.0002 | 0.0034 | SPANS_ZERO | 0.2701 | 0.0000 |  |
| Ice Hockey/Czech Extraliga | 1092 | 0.5000 | 0.2476 | 0.2462 | 0.2440 | 0.2530 | 0.2440 | 0.2440 | -0.0047 | -0.0077 | -0.0017 | BELOW_ZERO | SLOW | 0.0010 | -0.0012 | 0.0032 | SPANS_ZERO | 0.3063 | 0.0419 |  |
| Ice Hockey/Danish Metal Ligaen | 576 | 50.0000 | 0.2108 | 0.2135 | 0.2098 | 0.2090 | 0.2114 | 0.2100 | -0.0011 | -0.0039 | 0.0018 | SPANS_ZERO | SLOW | 0.0003 | -0.0003 | 0.0008 | SPANS_ZERO | 0.3428 | 0.0187 |  |
| Ice Hockey/NHL | 3933 | 0.5000 | 0.2512 | 0.2499 | 0.2489 | 0.2564 | 0.2485 | 0.2490 | -0.0020 | -0.0029 | -0.0010 | BELOW_ZERO | SLOW | 0.0005 | -0.0006 | 0.0015 | SPANS_ZERO | 0.2647 | 0.0000 |  |
| Rugby League/NRL | 611 | 50.0000 | 0.2333 | 0.2277 | 0.2286 | 0.2466 | 0.2267 | 0.2298 | -0.0030 | -0.0073 | 0.0012 | SPANS_ZERO | FAST | 0.0018 | -0.0036 | 0.0073 | SPANS_ZERO | 0.2801 | 0.0000 |  |
| Soccer/Premier League | 1137 | 50.0000 | 0.2228 | 0.2178 | 0.2129 | 0.2457 | 0.2143 | 0.2131 | -0.0098 | -0.0132 | -0.0065 | BELOW_ZERO | SLOW | 0.0002 | -0.0002 | 0.0006 | SPANS_ZERO | 0.2385 | 0.0000 |  |
| State Level AFL/SANFL | 270 | 10.0000 | 0.2167 | 0.2032 | 0.2015 | 0.2496 | 0.2004 | 0.2024 | -0.0151 | -0.0217 | -0.0084 | BELOW_ZERO | SLOW | -0.0000 | -0.0051 | 0.0050 | SPANS_ZERO | 0.3079 | 0.0000 |  |
| State Level AFL/VFL | 518 | 2.0000 | 0.2192 | 0.2059 | 0.2075 | 0.2507 | 0.2044 | 0.2061 | -0.0129 | -0.0174 | -0.0084 | BELOW_ZERO | FAST | 0.0008 | -0.0045 | 0.0061 | SPANS_ZERO | 0.2815 | 0.0000 |  |
| State Level AFL/VFLW | 251 | 2.0000 | 0.2408 | 0.2381 | 0.2347 | 0.2509 | 0.2338 | 0.2348 | -0.0060 | -0.0121 | 0.0001 | SPANS_ZERO | SLOW | 0.0001 | -0.0054 | 0.0056 | SPANS_ZERO | 0.3038 | 0.0000 |  |
| State Level AFL/WAFL | 276 | 50.0000 | 0.2125 | 0.1961 | 0.2016 | 0.2468 | 0.1966 | 0.1961 | -0.0167 | -0.0212 | -0.0122 | BELOW_ZERO | FAST | 0.0000 | -0.0000 | 0.0000 | SPANS_ZERO | 0.2828 | 0.0000 |  |


`exp3_p_baseline` is the average probability that Exp3 prices a primary card from the team-blind league baseline; `hedge_w_baseline` is the mixture weight the full-information policy gives it.

## Receipt

- `run_utc`: 2026-10-15T00:42:48Z
- `repo_head`: 3727aff6b79c56fdbd3a2c0f43ec0d2f9b57b25c
- `code_sha256`: b200d092b17f46a72a274385aa2ac278e012e9c0375ca2316afcb5faced0a141
- `python`: 3.14.6
- `numpy`: 2.5.2
- `pandas`: 3.0.5
- `scipy`: 1.18.1
