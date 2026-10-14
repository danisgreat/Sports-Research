# Parameters: `IH-CZECH-EXTRALIGA-REG-r1`

Fit as of **2026-03-07** on every regular-season and post-season game in the archive from season 2022 to the archive's last game (2026-03-06), with the frozen hyperparameters below. Ratings drift: these numbers are a snapshot, and current-season games after the archive's last date are not in them. Class: `HAND_APPLICABLE` (ML_RL_IMPLEMENTATION_FRAMEWORK §6.7).

Hyperparameters: `half_life_days` = 180.0, `ridge` = 64.0

League constants: intercept c **0.8278**, home **0.1992**, P(home wins extra time) **0.505**; promoted-team prior centre (attack, defence) (+0.000, +0.000).

**Worked example (check by hand).** Pardubice at home to Litvínov: lambda_home = exp(0.8278 + 0.1992 + +0.1077 + +0.1385) = **3.572**; lambda_away = exp(0.8278 + -0.1079 + -0.1013) = **1.856**. Grid winner masses (home, draw, away) = **(0.767, 0.000, 0.233)** (PROBABILITY_TOOLKIT §2–§3 tables).

| team | attack | defence | net_log_rate |
|---|---|---|---|
| Pardubice | 0.1077 | -0.1013 | 0.2091 |
| Sparta Prague | 0.1284 | -0.0284 | 0.1568 |
| Liberec | 0.0705 | -0.0708 | 0.1413 |
| Plzeň | -0.0070 | -0.1475 | 0.1404 |
| Hradec Králové | 0.0011 | -0.0713 | 0.0723 |
| Třinec | 0.0109 | -0.0439 | 0.0548 |
| Karlovy Vary | -0.0122 | -0.0330 | 0.0208 |
| Brno | 0.0286 | 0.0473 | -0.0187 |
| České Budějovice | 0.0201 | 0.0549 | -0.0347 |
| Kladno | -0.0220 | 0.0229 | -0.0449 |
| Vítkovice | -0.0011 | 0.1086 | -0.1097 |
| Mladá Boleslav | -0.1626 | 0.0080 | -0.1705 |
| Olomouc | -0.0546 | 0.1161 | -0.1707 |
| Litvínov | -0.1079 | 0.1385 | -0.2465 |


## Receipt

- `run_utc`: 2026-10-14T09:03:58Z
- `repo_head`: 3ab6d27fedb177add7cca5b41b14346107688ce3
- `code_sha256`: 9e24d01d2cb6f9878f0c00b2664fee163c69090a6b79972a091fbdfcf6db63be
- `python`: 3.14.6
- `numpy`: 2.5.2
- `pandas`: 3.0.5
- `scipy`: 1.18.1
- `model_id`: IH-CZECH-EXTRALIGA-REG-r1
- `archive_snapshot_sha256`: d55afa9fd1088e934e4d4fa18cb976587e44e9bdbb05afed6b9644c806ec2ed3
- `seconds`: 80
