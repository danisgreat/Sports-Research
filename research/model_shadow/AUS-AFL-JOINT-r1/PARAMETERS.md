# Parameters: `AUS-AFL-JOINT-r1`

Fit as of **2025-09-28** on every regular-season and post-season game in the archive from season 2022 to the archive's last game (2025-09-27), with the frozen hyperparameters below. Ratings drift: these numbers are a snapshot, and current-season games after the archive's last date are not in them. Class: `HAND_APPLICABLE` (ML_RL_IMPLEMENTATION_FRAMEWORK §6.7).

Hyperparameters: `half_life_days` = 90.0, `ridge` = 2.0, `cov_inflation` = 1.2

League constants: mu_home **87.212**, mu_away **81.546**; residual covariance [[519.87, -73.53], [-73.53, 447.97]] (inflation included); margin SD **33.39**; residual draw share **0.685**.

**Worked example (check by hand).** Western Bulldogs at home to West Coast: mean home = 87.212 + attack[Western Bulldogs] +19.926 + defence[West Coast] +18.077 = **125.22**; mean away = 81.546 + attack[West Coast] -17.588 + defence[Western Bulldogs] -4.275 = **59.68**. Normal approximation P(home ahead) = Phi(65.53 / 33.39) = **0.975**; the lattice price including the extra-time branch is **0.974** (PROBABILITY_TOOLKIT §1).

| team | attack | defence | net (points per game vs average) |
|---|---|---|---|
| Western Bulldogs | 19.9261 | -4.2747 | 24.2009 |
| Geelong | 18.7448 | -4.5012 | 23.2460 |
| Brisbane Lions | 10.7801 | -10.2788 | 21.0589 |
| Hawthorn | 7.7718 | -10.4043 | 18.1761 |
| Adelaide | 6.7818 | -8.4682 | 15.2500 |
| Collingwood | 0.1776 | -10.8143 | 10.9919 |
| Gold Coast | 5.0713 | -5.8293 | 10.9006 |
| Greater Western Sydney | 7.8328 | -1.6907 | 9.5235 |
| Fremantle | 1.4502 | -4.2919 | 5.7421 |
| Sydney | -3.2533 | -2.2162 | -1.0371 |
| Melbourne | 0.3633 | 2.4071 | -2.0438 |
| Carlton | -5.5489 | -0.7726 | -4.7762 |
| St Kilda | -4.9288 | 2.7567 | -7.6854 |
| Port Adelaide | -7.8056 | 5.4241 | -13.2296 |
| North Melbourne | -4.2493 | 16.6204 | -20.8697 |
| Essendon | -15.6234 | 9.6385 | -25.2618 |
| Richmond | -19.9026 | 8.6185 | -28.5212 |
| West Coast | -17.5882 | 18.0769 | -35.6651 |


## Receipt

- `run_utc`: 2026-10-14T09:01:08Z
- `repo_head`: 3ab6d27fedb177add7cca5b41b14346107688ce3
- `code_sha256`: 9e24d01d2cb6f9878f0c00b2664fee163c69090a6b79972a091fbdfcf6db63be
- `python`: 3.14.6
- `numpy`: 2.5.2
- `pandas`: 3.0.5
- `scipy`: 1.18.1
- `model_id`: AUS-AFL-JOINT-r1
- `archive_snapshot_sha256`: ae44699d2ca08b3f169f285693e78b71fa9eb323ac967be745ff4c824c299e19
- `seconds`: 119
