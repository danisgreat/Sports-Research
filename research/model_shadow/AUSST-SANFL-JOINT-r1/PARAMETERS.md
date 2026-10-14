# Parameters: `AUSST-SANFL-JOINT-r1`

Fit as of **2025-09-22** on every regular-season and post-season game in the archive from season 2022 to the archive's last game (2025-09-21), with the frozen hyperparameters below. Ratings drift: these numbers are a snapshot, and current-season games after the archive's last date are not in them. Class: `HAND_APPLICABLE` (ML_RL_IMPLEMENTATION_FRAMEWORK §6.7).

Hyperparameters: `half_life_days` = 90.0, `ridge` = 8.0, `cov_inflation` = 1.2

League constants: mu_home **78.535**, mu_away **79.163**; residual covariance [[537.56, -122.72], [-122.72, 612.69]] (inflation included); margin SD **37.36**; residual draw share **0.488**.

**Worked example (check by hand).** Sturt at home to West Adelaide: mean home = 78.535 + attack[Sturt] +16.623 + defence[West Adelaide] +10.024 = **105.18**; mean away = 79.163 + attack[West Adelaide] -8.807 + defence[Sturt] -9.641 = **60.71**. Normal approximation P(home ahead) = Phi(44.47 / 37.36) = **0.883**; the lattice price including the extra-time branch is **0.880** (PROBABILITY_TOOLKIT §1).

| team | attack | defence | net (points per game vs average) |
|---|---|---|---|
| Sturt | 16.6233 | -9.6408 | 26.2642 |
| Glenelg | 8.7510 | -5.5523 | 14.3033 |
| Adelaide | 7.0051 | -3.8909 | 10.8960 |
| Norwood | 1.5045 | -7.1301 | 8.6346 |
| Central District | -3.6630 | -3.4774 | -0.1855 |
| Port Adelaide | -0.2956 | 3.4291 | -3.7247 |
| South Adelaide | -7.1827 | 0.1680 | -7.3507 |
| North Adelaide | -5.2825 | 8.1315 | -13.4140 |
| Woodville-West Torrens | -8.6527 | 7.9386 | -16.5913 |
| West Adelaide | -8.8074 | 10.0244 | -18.8318 |


## Receipt

- `run_utc`: 2026-10-14T09:04:14Z
- `repo_head`: 3ab6d27fedb177add7cca5b41b14346107688ce3
- `code_sha256`: 9e24d01d2cb6f9878f0c00b2664fee163c69090a6b79972a091fbdfcf6db63be
- `python`: 3.14.6
- `numpy`: 2.5.2
- `pandas`: 3.0.5
- `scipy`: 1.18.1
- `model_id`: AUSST-SANFL-JOINT-r1
- `archive_snapshot_sha256`: 24bd39fff403156337cb2e0a80e6e1949cab78d4bdb4b495220b745e0dd66d40
- `seconds`: 19
