# Parameters: `BSB-MLB-NB-r1`

Fit as of **2026-10-01** on every regular-season and post-season game in the archive from season 2023 to the archive's last game (2026-09-30), with the frozen hyperparameters below. Ratings drift: these numbers are a snapshot, and current-season games after the archive's last date are not in them. Class: `HAND_APPLICABLE` (ML_RL_IMPLEMENTATION_FRAMEWORK §6.7).

Hyperparameters: `half_life_days` = 180.0, `ridge` = 128.0

League constants: intercept c **1.4863**, home **0.0134**, phi **0.2718**, P(home wins extra time) **0.499**; promoted-team prior centre (attack, defence) (+0.000, +0.000).

**Worked example (check by hand).** Milwaukee Brewers at home to Athletics: lambda_home = exp(1.4863 + 0.0134 + +0.1045 + +0.2211) = **6.204**; lambda_away = exp(1.4863 + -0.0252 + -0.1257) = **3.801**. Grid winner masses (home, draw, away) = **(0.684, 0.000, 0.316)** (PROBABILITY_TOOLKIT §2–§3 tables).

| team | attack | defence | net_log_rate |
|---|---|---|---|
| Milwaukee Brewers | 0.1045 | -0.1257 | 0.2302 |
| Los Angeles Dodgers | 0.0729 | -0.1268 | 0.1997 |
| New York Yankees | 0.0510 | -0.1108 | 0.1618 |
| Chicago Cubs | 0.1164 | -0.0418 | 0.1581 |
| Atlanta Braves | 0.0030 | -0.0928 | 0.0957 |
| Boston Red Sox | -0.0204 | -0.1103 | 0.0899 |
| Tampa Bay Rays | 0.0072 | -0.0799 | 0.0872 |
| San Diego Padres | 0.0077 | -0.0789 | 0.0866 |
| Detroit Tigers | -0.0017 | -0.0660 | 0.0643 |
| Philadelphia Phillies | 0.0081 | -0.0550 | 0.0631 |
| Chicago White Sox | 0.0298 | 0.0111 | 0.0187 |
| Arizona Diamondbacks | 0.0392 | 0.0207 | 0.0185 |
| Pittsburgh Pirates | -0.0036 | -0.0194 | 0.0158 |
| Cleveland Guardians | -0.0606 | -0.0701 | 0.0095 |
| New York Mets | 0.0118 | 0.0029 | 0.0088 |
| Toronto Blue Jays | -0.0309 | -0.0284 | -0.0024 |
| Miami Marlins | -0.0106 | 0.0076 | -0.0182 |
| Baltimore Orioles | -0.0005 | 0.0209 | -0.0214 |
| St. Louis Cardinals | -0.0160 | 0.0257 | -0.0416 |
| Washington Nationals | 0.0654 | 0.1089 | -0.0435 |
| Houston Astros | -0.0161 | 0.0283 | -0.0445 |
| Texas Rangers | -0.0597 | -0.0065 | -0.0532 |
| Seattle Mariners | -0.0505 | 0.0159 | -0.0663 |
| San Francisco Giants | -0.0562 | 0.0162 | -0.0724 |
| Minnesota Twins | 0.0038 | 0.0829 | -0.0791 |
| Kansas City Royals | -0.0351 | 0.0674 | -0.1026 |
| Cincinnati Reds | -0.0458 | 0.0774 | -0.1232 |
| Los Angeles Angels | -0.0984 | 0.0563 | -0.1547 |
| Colorado Rockies | 0.0099 | 0.2469 | -0.2370 |
| Athletics | -0.0252 | 0.2211 | -0.2463 |


## Receipt

- `run_utc`: 2026-10-14T09:05:02Z
- `repo_head`: 3ab6d27fedb177add7cca5b41b14346107688ce3
- `code_sha256`: 9e24d01d2cb6f9878f0c00b2664fee163c69090a6b79972a091fbdfcf6db63be
- `python`: 3.14.6
- `numpy`: 2.5.2
- `pandas`: 3.0.5
- `scipy`: 1.18.1
- `model_id`: BSB-MLB-NB-r1
- `archive_snapshot_sha256`: f63cc6ebac4b4dc987a6598e915bc30f08644bbef87b142aa39bce2b0f38f667
- `seconds`: 353
