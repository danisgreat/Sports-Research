# Parameters: `BSB-KBO-NB-r1`

Fit as of **2025-11-01** on every regular-season and post-season game in the archive from season 2022 to the archive's last game (2025-10-31), with the frozen hyperparameters below. Ratings drift: these numbers are a snapshot, and current-season games after the archive's last date are not in them. Class: `HAND_APPLICABLE` (ML_RL_IMPLEMENTATION_FRAMEWORK §6.7).

Hyperparameters: `half_life_days` = 180.0, `ridge` = 128.0

League constants: intercept c **1.5866**, home **-0.0169**, phi **0.2767**, P(home wins extra time) **0.359**; promoted-team prior centre (attack, defence) (+0.000, +0.000).

**Worked example (check by hand).** LG Twins at home to Kiwoom Heroes: lambda_home = exp(1.5866 + -0.0169 + +0.1054 + +0.1361) = **6.118**; lambda_away = exp(1.5866 + -0.0999 + -0.0903) = **4.040**. Grid winner masses (home, draw, away) = **(0.639, 0.019, 0.342)** (PROBABILITY_TOOLKIT §2–§3 tables).

| team | attack | defence | net_log_rate |
|---|---|---|---|
| LG Twins | 0.1054 | -0.0903 | 0.1958 |
| Samsung Lions | 0.0701 | -0.0353 | 0.1054 |
| Hanwha Eagles | 0.0035 | -0.0863 | 0.0898 |
| SSG Landers | -0.0809 | -0.0930 | 0.0122 |
| KT Wiz | -0.0279 | -0.0163 | -0.0116 |
| NC Dinos | 0.0504 | 0.0758 | -0.0254 |
| Doosan Bears | -0.0347 | -0.0079 | -0.0268 |
| KIA Tigers | 0.0089 | 0.0486 | -0.0397 |
| Lotte Giants | 0.0017 | 0.0684 | -0.0666 |
| Kiwoom Heroes | -0.0999 | 0.1361 | -0.2360 |


## Receipt

- `run_utc`: 2026-10-14T09:01:27Z
- `repo_head`: 3ab6d27fedb177add7cca5b41b14346107688ce3
- `code_sha256`: 9e24d01d2cb6f9878f0c00b2664fee163c69090a6b79972a091fbdfcf6db63be
- `python`: 3.14.6
- `numpy`: 2.5.2
- `pandas`: 3.0.5
- `scipy`: 1.18.1
- `model_id`: BSB-KBO-NB-r1
- `archive_snapshot_sha256`: fa56bb7595bb5f65f52984e32765222d2035a1c6b67d78f3ba901b81d50d6a25
- `seconds`: 138
