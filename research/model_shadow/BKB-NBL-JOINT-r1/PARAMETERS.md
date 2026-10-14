# Parameters: `BKB-NBL-JOINT-r1`

Fit as of **2026-10-12** on every regular-season and post-season game in the archive from season 2023 to the archive's last game (2026-10-11), with the frozen hyperparameters below. Ratings drift: these numbers are a snapshot, and current-season games after the archive's last date are not in them. Class: `HAND_APPLICABLE` (ML_RL_IMPLEMENTATION_FRAMEWORK §6.7).

Hyperparameters: `half_life_days` = 90.0, `ridge` = 8.0, `cov_inflation` = 1.2

League constants: mu_home **93.948**, mu_away **92.319**; residual covariance [[168.37, 41.45], [41.45, 140.08]] (inflation included); margin SD **15.02**; residual draw share **0.000**.

**Worked example (check by hand).** Sydney Kings at home to Brisbane Bullets: mean home = 93.948 + attack[Sydney Kings] +3.306 + defence[Brisbane Bullets] +1.585 = **98.84**; mean away = 92.319 + attack[Brisbane Bullets] -3.140 + defence[Sydney Kings] -2.045 = **87.13**. Normal approximation P(home ahead) = Phi(11.70 / 15.02) = **0.782**; the lattice price including the extra-time branch is **0.784** (PROBABILITY_TOOLKIT §1).

| team | attack | defence | net (points per game vs average) |
|---|---|---|---|
| Sydney Kings | 3.3056 | -2.0450 | 5.3506 |
| South East Melbourne Phoenix | 1.9438 | 0.3173 | 1.6265 |
| Melbourne United | -0.6375 | -2.1319 | 1.4944 |
| Perth Wildcats | -0.1101 | -1.3467 | 1.2366 |
| New Zealand Breakers | -1.2114 | -2.2323 | 1.0209 |
| Tasmania JackJumpers | 0.1883 | -0.4368 | 0.6251 |
| Adelaide 36ers | -1.6749 | -1.2721 | -0.4028 |
| Illawarra Hawks | 3.2096 | 6.2518 | -3.0423 |
| Cairns Taipans | -1.8736 | 1.3108 | -3.1844 |
| Brisbane Bullets | -3.1399 | 1.5848 | -4.7247 |


## Receipt

- `run_utc`: 2026-10-14T09:02:39Z
- `repo_head`: 3ab6d27fedb177add7cca5b41b14346107688ce3
- `code_sha256`: 9e24d01d2cb6f9878f0c00b2664fee163c69090a6b79972a091fbdfcf6db63be
- `python`: 3.14.6
- `numpy`: 2.5.2
- `pandas`: 3.0.5
- `scipy`: 1.18.1
- `model_id`: BKB-NBL-JOINT-r1
- `archive_snapshot_sha256`: e021011368510ac7f3e1ec167b426403426f1afc8c9b7d8412d25ddffc57cddb
- `seconds`: 61
