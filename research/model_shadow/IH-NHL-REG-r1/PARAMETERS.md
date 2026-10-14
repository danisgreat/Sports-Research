# Parameters: `IH-NHL-REG-r1`

Fit as of **2026-06-15** on every regular-season and post-season game in the archive from season 2022 to the archive's last game (2026-06-14), with the frozen hyperparameters below. Ratings drift: these numbers are a snapshot, and current-season games after the archive's last date are not in them. Class: `HAND_APPLICABLE` (ML_RL_IMPLEMENTATION_FRAMEWORK §6.7).

Hyperparameters: `half_life_days` = 180.0, `ridge` = 32.0

League constants: intercept c **1.0623**, home **0.0497**, P(home wins extra time) **0.522**; promoted-team prior centre (attack, defence) (+0.000, +0.000).

**Worked example (check by hand).** Colorado Avalanche at home to Vancouver Canucks: lambda_home = exp(1.0623 + 0.0497 + +0.1303 + +0.1655) = **4.087**; lambda_away = exp(1.0623 + -0.1201 + -0.1323) = **2.248**. Grid winner masses (home, draw, away) = **(0.768, 0.000, 0.232)** (PROBABILITY_TOOLKIT §2–§3 tables).

| team | attack | defence | net_log_rate |
|---|---|---|---|
| Colorado Avalanche | 0.1303 | -0.1323 | 0.2626 |
| Carolina Hurricanes | 0.1148 | -0.1057 | 0.2205 |
| Tampa Bay Lightning | 0.0909 | -0.0827 | 0.1736 |
| Buffalo Sabres | 0.1226 | -0.0226 | 0.1452 |
| Dallas Stars | 0.0477 | -0.0735 | 0.1212 |
| Vegas Golden Knights | 0.0489 | -0.0712 | 0.1201 |
| Ottawa Senators | 0.0436 | -0.0629 | 0.1065 |
| Washington Capitals | 0.0488 | -0.0319 | 0.0807 |
| Minnesota Wild | 0.0520 | -0.0286 | 0.0806 |
| Montréal Canadiens | 0.0419 | -0.0369 | 0.0789 |
| Utah Mammoth | 0.0548 | 0.0052 | 0.0496 |
| Pittsburgh Penguins | 0.0995 | 0.0500 | 0.0495 |
| Edmonton Oilers | 0.0871 | 0.0505 | 0.0366 |
| Boston Bruins | 0.0041 | -0.0256 | 0.0297 |
| Columbus Blue Jackets | 0.0020 | -0.0037 | 0.0057 |
| New York Rangers | -0.0045 | -0.0091 | 0.0046 |
| St. Louis Blues | -0.0225 | -0.0271 | 0.0045 |
| Florida Panthers | 0.0227 | 0.0212 | 0.0016 |
| Philadelphia Flyers | -0.0662 | -0.0576 | -0.0086 |
| Utah Utah Hockey Club | -0.0174 | -0.0053 | -0.0121 |
| Los Angeles Kings | -0.0970 | -0.0657 | -0.0313 |
| Winnipeg Jets | -0.0575 | -0.0254 | -0.0320 |
| Detroit Red Wings | -0.0402 | 0.0162 | -0.0564 |
| New Jersey Devils | -0.0694 | 0.0072 | -0.0766 |
| Nashville Predators | -0.0344 | 0.0464 | -0.0808 |
| New York Islanders | -0.0933 | -0.0125 | -0.0808 |
| Toronto Maple Leafs | 0.0089 | 0.0959 | -0.0870 |
| Anaheim Ducks | 0.0031 | 0.1170 | -0.1139 |
| Seattle Kraken | -0.0804 | 0.0469 | -0.1273 |
| Calgary Flames | -0.1247 | 0.0110 | -0.1357 |
| San Jose Sharks | -0.0522 | 0.1579 | -0.2100 |
| Chicago Blackhawks | -0.1451 | 0.0898 | -0.2349 |
| Vancouver Canucks | -0.1201 | 0.1655 | -0.2856 |


## Receipt

- `run_utc`: 2026-10-14T09:06:07Z
- `repo_head`: 3ab6d27fedb177add7cca5b41b14346107688ce3
- `code_sha256`: 9e24d01d2cb6f9878f0c00b2664fee163c69090a6b79972a091fbdfcf6db63be
- `python`: 3.14.6
- `numpy`: 2.5.2
- `pandas`: 3.0.5
- `scipy`: 1.18.1
- `model_id`: IH-NHL-REG-r1
- `archive_snapshot_sha256`: 6621881af29ea6ad02308dd6bff3bcd337b47daaca7d44980656ed5771d0ecce
- `seconds`: 179
