# Parameters: `IH-DANISH-METAL-LIGAEN-REG-r1`

Fit as of **2026-04-01** on every regular-season and post-season game in the archive from season 2022 to the archive's last game (2026-03-31), with the frozen hyperparameters below. Ratings drift: these numbers are a snapshot, and current-season games after the archive's last date are not in them. Class: `HAND_APPLICABLE` (ML_RL_IMPLEMENTATION_FRAMEWORK §6.7).

Hyperparameters: `half_life_days` = 730.0, `ridge` = 0.125

League constants: intercept c **1.0100**, home **0.3467**, P(home wins extra time) **0.566**; promoted-team prior centre (attack, defence) (+0.000, +0.000).

**Worked example (check by hand).** Aalborg Pirates at home to Rødovre Mighty Bulls: lambda_home = exp(1.0100 + 0.3467 + +0.0255 + +0.1040) = **4.420**; lambda_away = exp(1.0100 + -0.1100 + -0.1640) = **2.087**. Grid winner masses (home, draw, away) = **(0.826, 0.000, 0.174)** (PROBABILITY_TOOLKIT §2–§3 tables).

| team | attack | defence | net_log_rate |
|---|---|---|---|
| Aalborg Pirates | 0.0255 | -0.1640 | 0.1896 |
| Herning Blue Fox | 0.0571 | -0.0944 | 0.1515 |
| SønderjyskE Ishockey | 0.0319 | -0.0460 | 0.0779 |
| Esbjerg Energy | -0.0235 | -0.0418 | 0.0183 |
| Rungsted Seier Capital | -0.0427 | 0.0009 | -0.0436 |
| Odense Bulldogs | -0.0563 | 0.0068 | -0.0631 |
| Herlev Eagles | -0.0559 | 0.0621 | -0.1180 |
| Frederikshavn White Hawks | -0.0836 | 0.0856 | -0.1692 |
| Rødovre Mighty Bulls | -0.1100 | 0.1040 | -0.2141 |


## Receipt

- `run_utc`: 2026-10-14T09:03:55Z
- `repo_head`: 3ab6d27fedb177add7cca5b41b14346107688ce3
- `code_sha256`: 9e24d01d2cb6f9878f0c00b2664fee163c69090a6b79972a091fbdfcf6db63be
- `python`: 3.14.6
- `numpy`: 2.5.2
- `pandas`: 3.0.5
- `scipy`: 1.18.1
- `model_id`: IH-DANISH-METAL-LIGAEN-REG-r1
- `archive_snapshot_sha256`: e89e937ee34807d28071cb84dbe658154778eb8f758183d0482583fd50d5310a
- `seconds`: 70
