# Parameters: `AUSST-WAFL-JOINT-r1`

Fit as of **2025-09-22** on every regular-season and post-season game in the archive from season 2022 to the archive's last game (2025-09-21), with the frozen hyperparameters below. Ratings drift: these numbers are a snapshot, and current-season games after the archive's last date are not in them. Class: `HAND_APPLICABLE` (ML_RL_IMPLEMENTATION_FRAMEWORK §6.7).

Hyperparameters: `half_life_days` = 90.0, `ridge` = 2.0, `cov_inflation` = 1.4

League constants: mu_home **73.478**, mu_away **70.405**; residual covariance [[641.25, -5.39], [-5.39, 448.21]] (inflation included); margin SD **33.17**; residual draw share **0.866**.

**Worked example (check by hand).** South Fremantle at home to West Coast Eagles: mean home = 73.478 + attack[South Fremantle] +12.648 + defence[West Coast Eagles] +19.374 = **105.50**; mean away = 70.405 + attack[West Coast Eagles] -6.123 + defence[South Fremantle] -18.015 = **46.27**. Normal approximation P(home ahead) = Phi(59.23 / 33.17) = **0.963**; the lattice price including the extra-time branch is **0.961** (PROBABILITY_TOOLKIT §1).

| team | attack | defence | net (points per game vs average) |
|---|---|---|---|
| South Fremantle | 12.6482 | -18.0150 | 30.6632 |
| Claremont | 5.1706 | -13.6785 | 18.8491 |
| East Perth | 2.9713 | -10.6016 | 13.5729 |
| East Fremantle | 8.1253 | 2.2029 | 5.9224 |
| Perth | 2.2094 | 1.4834 | 0.7260 |
| Peel Thunder | -5.5581 | -4.2456 | -1.3125 |
| Swan Districts | -8.5289 | -0.0980 | -8.4310 |
| West Perth | 2.2866 | 12.8295 | -10.5428 |
| Subiaco | -13.2015 | 10.7488 | -23.9502 |
| West Coast Eagles | -6.1229 | 19.3742 | -25.4971 |


## Receipt

- `run_utc`: 2026-10-14T09:05:35Z
- `repo_head`: 3ab6d27fedb177add7cca5b41b14346107688ce3
- `code_sha256`: 9e24d01d2cb6f9878f0c00b2664fee163c69090a6b79972a091fbdfcf6db63be
- `python`: 3.14.6
- `numpy`: 2.5.2
- `pandas`: 3.0.5
- `scipy`: 1.18.1
- `model_id`: AUSST-WAFL-JOINT-r1
- `archive_snapshot_sha256`: 768780bcda5aba1a81538e455a4fe41cb9611a13de7fe0a3ddf3b0ee2d3987bf
- `seconds`: 81
