# Parameters: `BSB-NPB-NB-r1`

Fit as of **2025-10-31** on every regular-season and post-season game in the archive from season 2022 to the archive's last game (2025-10-30), with the frozen hyperparameters below. Ratings drift: these numbers are a snapshot, and current-season games after the archive's last date are not in them. Class: `HAND_APPLICABLE` (ML_RL_IMPLEMENTATION_FRAMEWORK §6.7).

Hyperparameters: `half_life_days` = 90.0, `ridge` = 128.0

League constants: intercept c **1.1863**, home **0.0537**, phi **0.3003**, P(home wins extra time) **0.390**; promoted-team prior centre (attack, defence) (+0.000, +0.000).

**Worked example (check by hand).** Fukuoka SoftBank Hawks at home to Hiroshima Toyo Carp: lambda_home = exp(1.1863 + 0.0537 + +0.0780 + +0.0598) = **3.966**; lambda_away = exp(1.1863 + -0.0635 + -0.1436) = **2.662**. Grid winner masses (home, draw, away) = **(0.613, 0.021, 0.366)** (PROBABILITY_TOOLKIT §2–§3 tables).

| team | attack | defence | net_log_rate |
|---|---|---|---|
| Fukuoka SoftBank Hawks | 0.0780 | -0.1436 | 0.2216 |
| Hokkaido Nippon-Ham Fighters | 0.0972 | -0.0994 | 0.1966 |
| Hanshin Tigers | -0.0124 | -0.1499 | 0.1375 |
| Yokohama DeNA BayStars | 0.0743 | 0.0112 | 0.0631 |
| Yomiuri Giants | 0.0046 | 0.0165 | -0.0118 |
| ORIX Buffaloes | 0.0185 | 0.0342 | -0.0156 |
| Saitama Seibu Lions | -0.0734 | 0.0095 | -0.0829 |
| Chunichi Dragons | -0.0844 | -0.0013 | -0.0831 |
| Tohoku Rakuten Golden Eagles | -0.0144 | 0.0826 | -0.0970 |
| Chiba Lotte Marines | -0.0231 | 0.0751 | -0.0982 |
| Tokyo Yakult Swallows | -0.0014 | 0.1053 | -0.1068 |
| Hiroshima Toyo Carp | -0.0635 | 0.0598 | -0.1233 |


## Receipt

- `run_utc`: 2026-10-14T09:01:37Z
- `repo_head`: 3ab6d27fedb177add7cca5b41b14346107688ce3
- `code_sha256`: 9e24d01d2cb6f9878f0c00b2664fee163c69090a6b79972a091fbdfcf6db63be
- `python`: 3.14.6
- `numpy`: 2.5.2
- `pandas`: 3.0.5
- `scipy`: 1.18.1
- `model_id`: BSB-NPB-NB-r1
- `archive_snapshot_sha256`: aa092627e3ea25c966cb025017aee11e6bcd7a15fcc243399fc83e5be38faa18
- `seconds`: 148
