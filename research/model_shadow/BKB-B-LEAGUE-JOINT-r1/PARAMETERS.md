# Parameters: `BKB-B-LEAGUE-JOINT-r1`

Fit as of **2026-10-13** on every regular-season and post-season game in the archive from season 2023 to the archive's last game (2026-10-12), with the frozen hyperparameters below. Ratings drift: these numbers are a snapshot, and current-season games after the archive's last date are not in them. Class: `HAND_APPLICABLE` (ML_RL_IMPLEMENTATION_FRAMEWORK §6.7).

Hyperparameters: `half_life_days` = 90.0, `ridge` = 2.0, `cov_inflation` = 1.1

League constants: mu_home **82.121**, mu_away **81.930**; residual covariance [[131.65, 37.30], [37.30, 120.56]] (inflation included); margin SD **13.33**; residual draw share **0.000**.

**Worked example (check by hand).** 群馬 at home to 秋田: mean home = 82.121 + attack[群馬] -2.223 + defence[秋田] +0.991 = **80.89**; mean away = 81.930 + attack[秋田] -7.963 + defence[群馬] -10.061 = **63.91**. Normal approximation P(home ahead) = Phi(16.98 / 13.33) = **0.899**; the lattice price including the extra-time branch is **0.901** (PROBABILITY_TOOLKIT §1).

| team | attack | defence | net (points per game vs average) |
|---|---|---|---|
| 群馬 | -2.2235 | -10.0606 | 7.8371 |
| 名古屋D | 1.8690 | -4.1038 | 5.9728 |
| A東京 | 4.6799 | -1.2902 | 5.9700 |
| 三遠 | 5.3728 | -0.3835 | 5.7563 |
| 琉球 | -0.4315 | -5.9986 | 5.5670 |
| 三河 | 1.9050 | -3.3920 | 5.2969 |
| 長崎 | 1.3232 | -3.0567 | 4.3799 |
| 広島 | 5.5502 | 1.8277 | 3.7225 |
| 東京SR | 2.2044 | -1.2982 | 3.5026 |
| 宇都宮 | 1.1746 | -1.9663 | 3.1408 |
| 仙台 | 2.0329 | -0.6581 | 2.6911 |
| 千葉J | 6.5620 | 4.5401 | 2.0219 |
| 北海道 | 8.7622 | 7.1593 | 1.6029 |
| 滋賀 | 3.3691 | 3.0716 | 0.2975 |
| 京都 | -1.5112 | -1.3964 | -0.1148 |
| 島根 | -1.6234 | -1.3306 | -0.2927 |
| 横浜BC | -2.1225 | -0.9625 | -1.1600 |
| SR渋谷 | -4.9651 | -3.0649 | -1.9002 |
| 信州 | -0.1600 | 1.8976 | -2.0576 |
| 富山 | 1.3464 | 3.4319 | -2.0855 |
| 佐賀 | -2.1252 | 0.6557 | -2.7809 |
| 茨城 | -2.5760 | 0.6421 | -3.2182 |
| FE名古屋 | -1.6422 | 2.6978 | -4.3400 |
| 越谷 | -3.9155 | 1.1353 | -5.0508 |
| 神戸 | -5.1213 | 0.8980 | -6.0193 |
| A千葉 | -2.7685 | 3.3118 | -6.0803 |
| 大阪 | -4.0753 | 2.6553 | -6.7306 |
| 川崎 | -2.9272 | 4.0473 | -6.9745 |
| 秋田 | -7.9632 | 0.9908 | -8.9540 |


## Receipt

- `run_utc`: 2026-10-14T09:02:45Z
- `repo_head`: 3ab6d27fedb177add7cca5b41b14346107688ce3
- `code_sha256`: 9e24d01d2cb6f9878f0c00b2664fee163c69090a6b79972a091fbdfcf6db63be
- `python`: 3.14.6
- `numpy`: 2.5.2
- `pandas`: 3.0.5
- `scipy`: 1.18.1
- `model_id`: BKB-B-LEAGUE-JOINT-r1
- `archive_snapshot_sha256`: be13f37084c10310045ff6214298db22ed83fce1d5cacae2dbeb99be62df519d
- `seconds`: 216
