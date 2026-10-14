# Parameters: `BKB-NBA-JOINT-r1`

Fit as of **2026-06-14** on every regular-season and post-season game in the archive from season 2022 to the archive's last game (2026-06-13), with the frozen hyperparameters below. Ratings drift: these numbers are a snapshot, and current-season games after the archive's last date are not in them. Class: `HAND_APPLICABLE` (ML_RL_IMPLEMENTATION_FRAMEWORK §6.7).

Hyperparameters: `half_life_days` = 45.0, `ridge` = 8.0, `cov_inflation` = 1.1

League constants: mu_home **115.550**, mu_away **113.671**; residual covariance [[152.42, 32.46], [32.46, 155.29]] (inflation included); margin SD **15.58**; residual draw share **0.000**.

**Worked example (check by hand).** New York Knicks at home to Washington Wizards: mean home = 115.550 + attack[New York Knicks] +0.904 + defence[Washington Wizards] +6.911 = **123.37**; mean away = 113.671 + attack[Washington Wizards] -0.717 + defence[New York Knicks] -8.254 = **104.70**. Normal approximation P(home ahead) = Phi(18.67 / 15.58) = **0.885**; the lattice price including the extra-time branch is **0.886** (PROBABILITY_TOOLKIT §1).

| team | attack | defence | net (points per game vs average) |
|---|---|---|---|
| New York Knicks | 0.9036 | -8.2539 | 9.1576 |
| San Antonio Spurs | 2.6269 | -5.8136 | 8.4404 |
| Oklahoma City Thunder | 2.7761 | -4.4631 | 7.2392 |
| Boston Celtics | -1.1409 | -5.7420 | 4.6011 |
| Detroit Pistons | -0.7483 | -5.2184 | 4.4701 |
| Charlotte Hornets | 0.6499 | -3.3595 | 4.0094 |
| Denver Nuggets | 3.8230 | 1.1651 | 2.6579 |
| Houston Rockets | -1.6795 | -4.0434 | 2.3640 |
| Toronto Raptors | -0.0329 | -2.3196 | 2.2867 |
| Cleveland Cavaliers | 0.9499 | -0.8601 | 1.8100 |
| Los Angeles Clippers | 0.2123 | -1.1479 | 1.3602 |
| Atlanta Hawks | 1.6553 | 0.3544 | 1.3009 |
| Los Angeles Lakers | -1.0057 | -2.1756 | 1.1700 |
| Miami Heat | 4.4645 | 3.6392 | 0.8254 |
| Minnesota Timberwolves | 0.0533 | -0.6174 | 0.6707 |
| Portland Trail Blazers | -0.9757 | -1.5810 | 0.6053 |
| Orlando Magic | -1.2147 | -1.6951 | 0.4804 |
| Phoenix Suns | -1.8315 | -2.0391 | 0.2076 |
| Team Chuck | -0.0055 | -0.0060 | 0.0005 |
| Team Shaq | -0.0054 | -0.0058 | 0.0004 |
| Team Candace | -0.0058 | -0.0054 | -0.0004 |
| Team Kenny | -0.0060 | -0.0055 | -0.0005 |
| Philadelphia 76ers | -0.7571 | 0.0664 | -0.8236 |
| New Orleans Pelicans | 1.2056 | 2.9950 | -1.7894 |
| Golden State Warriors | -0.6157 | 1.1830 | -1.7986 |
| Dallas Mavericks | 0.5090 | 4.3997 | -3.8908 |
| Indiana Pacers | 0.1090 | 4.0801 | -3.9711 |
| Chicago Bulls | 0.8458 | 4.9832 | -4.1374 |
| Milwaukee Bucks | -3.0780 | 2.0449 | -5.1230 |
| Utah Jazz | 1.3855 | 6.7918 | -5.4063 |
| Sacramento Kings | -1.7399 | 3.7079 | -5.4477 |
| Memphis Grizzlies | -0.4281 | 5.8165 | -6.2447 |
| Brooklyn Nets | -6.1818 | 1.2137 | -7.3956 |
| Washington Wizards | -0.7171 | 6.9114 | -7.6285 |


## Receipt

- `run_utc`: 2026-10-14T09:07:28Z
- `repo_head`: 3ab6d27fedb177add7cca5b41b14346107688ce3
- `code_sha256`: 9e24d01d2cb6f9878f0c00b2664fee163c69090a6b79972a091fbdfcf6db63be
- `python`: 3.14.6
- `numpy`: 2.5.2
- `pandas`: 3.0.5
- `scipy`: 1.18.1
- `model_id`: BKB-NBA-JOINT-r1
- `archive_snapshot_sha256`: 20aa58d79a1236a3129e418a188f86aa9bec0e22da15a341aee9eb71da187434
- `seconds`: 361
