# Parameters: `AUSST-VFLW-JOINT-r1`

Fit as of **2025-08-31** on every regular-season and post-season game in the archive from season 2022 to the archive's last game (2025-08-30), with the frozen hyperparameters below. Ratings drift: these numbers are a snapshot, and current-season games after the archive's last date are not in them. Class: `HAND_APPLICABLE` (ML_RL_IMPLEMENTATION_FRAMEWORK §6.7).

Hyperparameters: `half_life_days` = 90.0, `ridge` = 2.0, `cov_inflation` = 1.4

League constants: mu_home **36.674**, mu_away **33.097**; residual covariance [[427.79, -117.07], [-117.07, 283.90]] (inflation included); margin SD **30.75**; residual draw share **1.000**.

**Worked example (check by hand).** North Melbourne Werribee at home to Geelong Cats: mean home = 36.674 + attack[North Melbourne Werribee] +17.133 + defence[Geelong Cats] +15.173 = **68.98**; mean away = 33.097 + attack[Geelong Cats] -4.231 + defence[North Melbourne Werribee] -8.476 = **20.39**. Normal approximation P(home ahead) = Phi(48.59 / 30.75) = **0.943**; the lattice price including the extra-time branch is **0.934** (PROBABILITY_TOOLKIT §1).

| team | attack | defence | net (points per game vs average) |
|---|---|---|---|
| North Melbourne Werribee | 17.1331 | -8.4758 | 25.6089 |
| Collingwood | 7.2043 | -6.2557 | 13.4600 |
| Box Hill Hawks | 5.3379 | -2.8417 | 8.1797 |
| Port Melbourne | 3.9176 | -1.7114 | 5.6290 |
| Sydney Swans | 2.4420 | -0.7310 | 3.1729 |
| Williamstown | -2.2083 | -5.1166 | 2.9083 |
| Essendon | -0.5789 | -1.0785 | 0.4997 |
| Sandringham | -7.7579 | -4.9206 | -2.8372 |
| Darebin | -6.9463 | -3.4061 | -3.5401 |
| Western Bulldogs | -5.3832 | 3.2017 | -8.5848 |
| Carlton | -4.8102 | 4.0274 | -8.8376 |
| Casey Demons | -4.1189 | 12.1349 | -16.2539 |
| Geelong Cats | -4.2313 | 15.1735 | -19.4048 |


## Receipt

- `run_utc`: 2026-10-14T09:04:58Z
- `repo_head`: 3ab6d27fedb177add7cca5b41b14346107688ce3
- `code_sha256`: 9e24d01d2cb6f9878f0c00b2664fee163c69090a6b79972a091fbdfcf6db63be
- `python`: 3.14.6
- `numpy`: 2.5.2
- `pandas`: 3.0.5
- `scipy`: 1.18.1
- `model_id`: AUSST-VFLW-JOINT-r1
- `archive_snapshot_sha256`: c116f28e7e887b77556d2bc0e82fdab6f9edb7fff8fb5de323743773e614b514
- `seconds`: 44
