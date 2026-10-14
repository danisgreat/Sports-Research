# Parameters: `SOC-PREMIER-LEAGUE-DC-r1`

Fit as of **2026-05-25** on every regular-season and post-season game in the archive from season 2022 to the archive's last game (2026-05-24), with the frozen hyperparameters below. Ratings drift: these numbers are a snapshot, and current-season games after the archive's last date are not in them. Class: `HAND_APPLICABLE` (ML_RL_IMPLEMENTATION_FRAMEWORK §6.7).

Hyperparameters: `half_life_days` = 365.0, `ridge` = 16.0

League constants: intercept c **0.2571**, home **0.1765**, rho **-0.079**, P(home wins extra time) **0.500**; promoted-team prior centre (attack, defence) (-0.236, +0.245).

**Worked example (check by hand).** Arsenal at home to Southampton: lambda_home = exp(0.2571 + 0.1765 + +0.2826 + +0.2771) = **2.700**; lambda_away = exp(0.2571 + -0.3114 + -0.4527) = **0.602**. Grid winner masses (home, draw, away) = **(0.810, 0.135, 0.054)** (PROBABILITY_TOOLKIT §2–§3 tables).

| team | attack | defence | net_log_rate |
|---|---|---|---|
| Arsenal | 0.2826 | -0.4527 | 0.7354 |
| Man City | 0.3491 | -0.3203 | 0.6694 |
| Liverpool | 0.2850 | -0.1062 | 0.3912 |
| Newcastle | 0.1572 | -0.0420 | 0.1992 |
| Man United | 0.1191 | -0.0755 | 0.1946 |
| Aston Villa | 0.1034 | -0.0750 | 0.1784 |
| Chelsea | 0.1061 | -0.0685 | 0.1746 |
| Brighton | 0.0695 | -0.0598 | 0.1293 |
| Brentford | 0.0897 | -0.0269 | 0.1167 |
| Bournemouth | 0.0575 | -0.0387 | 0.0962 |
| Nott'm Forest | -0.0140 | -0.0606 | 0.0466 |
| Fulham | -0.0429 | -0.0551 | 0.0122 |
| Everton | -0.1340 | -0.1172 | -0.0168 |
| Tottenham | 0.0490 | 0.0764 | -0.0274 |
| Crystal Palace | -0.0906 | -0.0528 | -0.0379 |
| Leeds | -0.0345 | 0.0154 | -0.0499 |
| West Ham | -0.0662 | 0.1020 | -0.1682 |
| Sunderland | -0.2084 | -0.0338 | -0.1747 |
| Luton | 0.0002 | 0.2062 | -0.2060 |
| Wolves | -0.2571 | 0.1278 | -0.3849 |
| Leicester | -0.2174 | 0.2143 | -0.4317 |
| Burnley | -0.2076 | 0.2313 | -0.4389 |
| Ipswich | -0.1904 | 0.2581 | -0.4485 |
| Sheffield United | -0.1300 | 0.3212 | -0.4511 |
| Southampton | -0.3114 | 0.2771 | -0.5885 |


## Receipt

- `run_utc`: 2026-10-14T09:05:41Z
- `repo_head`: 3ab6d27fedb177add7cca5b41b14346107688ce3
- `code_sha256`: 9e24d01d2cb6f9878f0c00b2664fee163c69090a6b79972a091fbdfcf6db63be
- `python`: 3.14.6
- `numpy`: 2.5.2
- `pandas`: 3.0.5
- `scipy`: 1.18.1
- `model_id`: SOC-PREMIER-LEAGUE-DC-r1
- `archive_snapshot_sha256`: 042634114d6d7a64619ab41fd5c28d9b544503d9e2319d41783a91e477e956d2
- `seconds`: 128
