# Parameters: `BKB-NBA-G-LEAGUE-JOINT-r1`

Fit as of **2026-04-11** on every regular-season and post-season game in the archive from season 2022 to the archive's last game (2026-04-10), with the frozen hyperparameters below. Ratings drift: these numbers are a snapshot, and current-season games after the archive's last date are not in them. Class: `HAND_APPLICABLE` (ML_RL_IMPLEMENTATION_FRAMEWORK §6.7).

Hyperparameters: `half_life_days` = 90.0, `ridge` = 8.0, `cov_inflation` = 1.1

League constants: mu_home **117.089**, mu_away **115.602**; residual covariance [[145.93, 41.58], [41.58, 127.28]] (inflation included); margin SD **13.79**; residual draw share **0.000**.

**Worked example (check by hand).** Greensboro Swarm at home to Oklahoma City Blue: mean home = 117.089 + attack[Greensboro Swarm] +6.187 + defence[Oklahoma City Blue] +2.352 = **125.63**; mean away = 115.602 + attack[Oklahoma City Blue] -2.564 + defence[Greensboro Swarm] -0.373 = **112.66**. Normal approximation P(home ahead) = Phi(12.96 / 13.79) = **0.826**; the lattice price including the extra-time branch is **0.829** (PROBABILITY_TOOLKIT §1).

| team | attack | defence | net (points per game vs average) |
|---|---|---|---|
| Greensboro Swarm | 6.1870 | -0.3732 | 6.5602 |
| South Bay Lakers | 3.6138 | -2.9350 | 6.5488 |
| Osceola Magic | 2.3373 | -2.0017 | 4.3389 |
| Motor City Cruise | 2.7507 | -1.0015 | 3.7521 |
| Austin Spurs | -3.1029 | -6.2040 | 3.1011 |
| Rio Grande Valley Vipers | 0.5513 | -2.3414 | 2.8927 |
| Cleveland Charge | 3.4992 | 0.6697 | 2.8295 |
| Iowa Wolves | 3.2710 | 0.5333 | 2.7377 |
| Raptors 905 | 0.8210 | -1.8906 | 2.7115 |
| Stockton Kings | -1.4593 | -4.0357 | 2.5763 |
| Sioux Falls Skyforce | 1.3735 | -0.9531 | 2.3266 |
| Capital City Go-Go | 1.5411 | 0.1133 | 1.4278 |
| Indiana Mad Ants | -0.5619 | -0.9402 | 0.3783 |
| Long Island Nets | -2.0716 | -2.1885 | 0.1168 |
| Mexico City Capitanes | -2.9078 | -3.0018 | 0.0940 |
| Fort Wayne Mad Ants | -0.0153 | -0.0441 | 0.0288 |
| Ontario Clippers | -0.0466 | -0.0684 | 0.0218 |
| G League Ignite | -0.1435 | 0.0024 | -0.1459 |
| Rip City Remix | 1.4943 | 1.7364 | -0.2421 |
| San Diego Clippers | -0.7104 | -0.2939 | -0.4166 |
| Maine Celtics | -3.3386 | -2.6514 | -0.6871 |
| Noblesville Boom | 1.0944 | 1.8479 | -0.7535 |
| Texas Legends | -2.2519 | -1.0378 | -1.2140 |
| Salt Lake City Stars | 2.6718 | 3.9499 | -1.2781 |
| College Park Skyhawks | 3.4561 | 5.6683 | -2.2122 |
| Santa Cruz Warriors | -1.3985 | 0.8862 | -2.2848 |
| Delaware Blue Coats | 1.5982 | 4.4623 | -2.8640 |
| Memphis Hustle | -0.6268 | 2.2912 | -2.9180 |
| Birmingham Squadron | -3.5607 | -0.4158 | -3.1449 |
| Westchester Knicks | -2.0249 | 1.4826 | -3.5075 |
| Valley Suns | -2.9782 | 0.8289 | -3.8071 |
| Grand Rapids Gold | -1.4871 | 2.4827 | -3.9698 |
| Windy City Bulls | 2.1268 | 6.1428 | -4.0160 |
| Wisconsin Herd | -7.1376 | -3.0719 | -4.0656 |
| Oklahoma City Blue | -2.5639 | 2.3517 | -4.9156 |


## Receipt

- `run_utc`: 2026-10-14T09:03:08Z
- `repo_head`: 3ab6d27fedb177add7cca5b41b14346107688ce3
- `code_sha256`: 9e24d01d2cb6f9878f0c00b2664fee163c69090a6b79972a091fbdfcf6db63be
- `python`: 3.14.6
- `numpy`: 2.5.2
- `pandas`: 3.0.5
- `scipy`: 1.18.1
- `model_id`: BKB-NBA-G-LEAGUE-JOINT-r1
- `archive_snapshot_sha256`: b6b7e881eb74f963f6205432acbafb818949b56e753a63e0621b23d1069bce85
- `seconds`: 98
