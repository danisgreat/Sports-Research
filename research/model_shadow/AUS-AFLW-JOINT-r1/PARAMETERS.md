# Parameters: `AUS-AFLW-JOINT-r1`

Fit as of **2025-11-30** on every regular-season and post-season game in the archive from season 2022 to the archive's last game (2025-11-29), with the frozen hyperparameters below. Ratings drift: these numbers are a snapshot, and current-season games after the archive's last date are not in them. Class: `HAND_APPLICABLE` (ML_RL_IMPLEMENTATION_FRAMEWORK §6.7).

Hyperparameters: `half_life_days` = 180.0, `ridge` = 1.0, `cov_inflation` = 1.4

League constants: mu_home **41.401**, mu_away **38.433**; residual covariance [[345.86, -65.77], [-65.77, 332.05]] (inflation included); margin SD **28.45**; residual draw share **1.000**.

**Worked example (check by hand).** North Melbourne at home to Gold Coast SUNS: mean home = 41.401 + attack[North Melbourne] +22.415 + defence[Gold Coast SUNS] +19.570 = **83.39**; mean away = 38.433 + attack[Gold Coast SUNS] -12.630 + defence[North Melbourne] -18.511 = **7.29**. Normal approximation P(home ahead) = Phi(76.09 / 28.45) = **0.996**; the lattice price including the extra-time branch is **0.994** (PROBABILITY_TOOLKIT §1).

| team | attack | defence | net (points per game vs average) |
|---|---|---|---|
| North Melbourne | 22.4148 | -18.5111 | 40.9259 |
| Brisbane Lions | 12.8144 | -7.5017 | 20.3161 |
| Melbourne | 11.4984 | -6.4213 | 17.9197 |
| Adelaide Crows | 4.3572 | -5.0850 | 9.4422 |
| Western Bulldogs | -1.9638 | -5.5996 | 3.6358 |
| Carlton | 3.2256 | 1.8222 | 1.4035 |
| Geelong Cats | 1.4283 | 1.0154 | 0.4129 |
| Hawthorn | -1.7017 | -1.9223 | 0.2207 |
| Port Adelaide | 8.3845 | 8.1988 | 0.1857 |
| Sydney Swans | 2.4088 | 4.2418 | -1.8330 |
| Fremantle | -5.2574 | -2.9384 | -2.3191 |
| St Kilda | -4.3810 | 1.9736 | -6.3547 |
| West Coast Eagles | -8.5229 | 1.0522 | -9.5751 |
| Richmond | -7.1088 | 4.6021 | -11.7108 |
| Essendon | -11.6922 | 2.3474 | -14.0396 |
| Collingwood | -13.2747 | 3.1561 | -16.4309 |
| Gold Coast SUNS | -12.6295 | 19.5699 | -32.1994 |


## Receipt

- `run_utc`: 2026-10-14T09:00:23Z
- `repo_head`: 3ab6d27fedb177add7cca5b41b14346107688ce3
- `code_sha256`: 9e24d01d2cb6f9878f0c00b2664fee163c69090a6b79972a091fbdfcf6db63be
- `python`: 3.14.6
- `numpy`: 2.5.2
- `pandas`: 3.0.5
- `scipy`: 1.18.1
- `model_id`: AUS-AFLW-JOINT-r1
- `archive_snapshot_sha256`: a43882ba9d94778710fa0eeb9e28a1ed1f6e1b5fb95d431c301ecd27d24039be
- `seconds`: 74
