# Parameters: `BKB-GREEK-BASKET-LEAGUE-JOINT-r1`

Fit as of **2026-06-14** on every regular-season and post-season game in the archive from season 2022 to the archive's last game (2026-06-13), with the frozen hyperparameters below. Ratings drift: these numbers are a snapshot, and current-season games after the archive's last date are not in them. Class: `HAND_APPLICABLE` (ML_RL_IMPLEMENTATION_FRAMEWORK §6.7).

Hyperparameters: `half_life_days` = 180.0, `ridge` = 2.0, `cov_inflation` = 1.1

League constants: mu_home **84.183**, mu_away **81.204**; residual covariance [[114.31, 44.61], [44.61, 116.08]] (inflation included); margin SD **11.88**; residual draw share **0.000**.

**Worked example (check by hand).** Olympiacos at home to Apollon Patras: mean home = 84.183 + attack[Olympiacos] +9.898 + defence[Apollon Patras] +0.579 = **94.66**; mean away = 81.204 + attack[Apollon Patras] -4.833 + defence[Olympiacos] -5.200 = **71.17**. Normal approximation P(home ahead) = Phi(23.49 / 11.88) = **0.976**; the lattice price including the extra-time branch is **0.977** (PROBABILITY_TOOLKIT §1).

| team | attack | defence | net (points per game vs average) |
|---|---|---|---|
| Olympiacos | 9.8976 | -5.1997 | 15.0973 |
| Panathinaikos | 6.6905 | -6.2711 | 12.9617 |
| AEK Athens | 1.2119 | -2.9610 | 4.1729 |
| PAOK | 0.2994 | -2.0786 | 2.3780 |
| Aris Thessaloniki | 0.0755 | -1.4501 | 1.5256 |
| Peristeri | -3.4179 | -3.4885 | 0.0707 |
| Kolossos Rhodes | 0.0939 | 1.0402 | -0.9463 |
| Ionikos Nikaias | -0.5636 | 0.5386 | -1.1022 |
| Promitheas Patras | 1.2312 | 3.8645 | -2.6333 |
| Iraklis Thessaloniki | -1.6408 | 1.6973 | -3.3381 |
| Karditsa | -3.2965 | 0.2613 | -3.5578 |
| Maroussi | 2.5821 | 6.4577 | -3.8756 |
| Panionios | -3.9212 | 0.8448 | -4.7660 |
| Mykonos B.C. | -1.3882 | 3.8769 | -5.2652 |
| Lavrio Megabolt | -3.0209 | 2.2889 | -5.3098 |
| Apollon Patras | -4.8330 | 0.5787 | -5.4118 |


## Receipt

- `run_utc`: 2026-10-14T09:02:03Z
- `repo_head`: 3ab6d27fedb177add7cca5b41b14346107688ce3
- `code_sha256`: 9e24d01d2cb6f9878f0c00b2664fee163c69090a6b79972a091fbdfcf6db63be
- `python`: 3.14.6
- `numpy`: 2.5.2
- `pandas`: 3.0.5
- `scipy`: 1.18.1
- `model_id`: BKB-GREEK-BASKET-LEAGUE-JOINT-r1
- `archive_snapshot_sha256`: 3b339b1e6cfddb4dcd387071bcb2c5b5b786c9d8221dd03b6191f926a00174f8
- `seconds`: 90
