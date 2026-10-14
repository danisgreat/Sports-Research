# Parameters: `AUSST-VFL-JOINT-r1`

Fit as of **2025-09-22** on every regular-season and post-season game in the archive from season 2022 to the archive's last game (2025-09-21), with the frozen hyperparameters below. Ratings drift: these numbers are a snapshot, and current-season games after the archive's last date are not in them. Class: `HAND_APPLICABLE` (ML_RL_IMPLEMENTATION_FRAMEWORK §6.7).

Hyperparameters: `half_life_days` = 180.0, `ridge` = 8.0, `cov_inflation` = 1.1

League constants: mu_home **82.493**, mu_away **81.870**; residual covariance [[550.46, -81.85], [-81.85, 502.34]] (inflation included); margin SD **34.88**; residual draw share **1.000**.

**Worked example (check by hand).** Footscray Bulldogs at home to Northern Bullants: mean home = 82.493 + attack[Footscray Bulldogs] +8.787 + defence[Northern Bullants] +18.681 = **109.96**; mean away = 81.870 + attack[Northern Bullants] -15.333 + defence[Footscray Bulldogs] -13.845 = **52.69**. Normal approximation P(home ahead) = Phi(57.27 / 34.88) = **0.950**; the lattice price including the extra-time branch is **0.948** (PROBABILITY_TOOLKIT §1).

| team | attack | defence | net (points per game vs average) |
|---|---|---|---|
| Footscray Bulldogs | 8.7874 | -13.8454 | 22.6327 |
| Southport Sharks | 12.2109 | -4.9572 | 17.1681 |
| Casey Demons | 9.3272 | -6.2755 | 15.6027 |
| Box Hill Hawks | 8.0491 | -5.5136 | 13.5626 |
| Brisbane Lions | 9.4687 | 3.0130 | 6.4557 |
| Werribee | -3.9263 | -7.9913 | 4.0650 |
| Gold Coast SUNS | 1.8489 | -0.5917 | 2.4406 |
| Williamstown | 2.0938 | -0.0566 | 2.1504 |
| Geelong Cats | -1.9856 | -1.9394 | -0.0462 |
| Richmond | -4.9628 | -4.3148 | -0.6479 |
| Frankston | 1.1928 | 2.7715 | -1.5787 |
| North Melbourne | -0.0716 | 1.9707 | -2.0423 |
| Collingwood | -0.5600 | 2.0780 | -2.6380 |
| Coburg | -2.3240 | 0.9746 | -3.2986 |
| Port Melbourne | -5.0786 | -1.1859 | -3.8927 |
| Essendon | -3.9248 | 2.6662 | -6.5910 |
| Carlton | -3.2345 | 3.9227 | -7.1572 |
| Sandringham | -3.6719 | 5.9783 | -9.6501 |
| Sydney Swans | -7.9056 | 4.6152 | -12.5207 |
| Northern Bullants | -15.3333 | 18.6811 | -34.0144 |


## Receipt

- `run_utc`: 2026-10-14T09:04:41Z
- `repo_head`: 3ab6d27fedb177add7cca5b41b14346107688ce3
- `code_sha256`: 9e24d01d2cb6f9878f0c00b2664fee163c69090a6b79972a091fbdfcf6db63be
- `python`: 3.14.6
- `numpy`: 2.5.2
- `pandas`: 3.0.5
- `scipy`: 1.18.1
- `model_id`: AUSST-VFL-JOINT-r1
- `archive_snapshot_sha256`: 230f8737cee8decd6fe2e2949cd832561402b8ba555cb8322726ea9038eceb82
- `seconds`: 42
