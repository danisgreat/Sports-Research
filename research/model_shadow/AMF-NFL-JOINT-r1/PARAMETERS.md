# Parameters: `AMF-NFL-JOINT-r1`

Fit as of **2026-02-09** on every regular-season and post-season game in the archive from season 2022 to the archive's last game (2026-02-08), with the frozen hyperparameters below. Ratings drift: these numbers are a snapshot, and current-season games after the archive's last date are not in them. Class: `HAND_APPLICABLE` (ML_RL_IMPLEMENTATION_FRAMEWORK §6.7).

Hyperparameters: `half_life_days` = 180.0, `ridge` = 8.0, `cov_inflation` = 1.1

League constants: mu_home **23.990**, mu_away **21.848**; residual covariance [[86.69, 1.96], [1.96, 85.98]] (inflation included); margin SD **12.99**; residual draw share **0.086**.

**Worked example (check by hand).** Seattle Seahawks at home to New York Jets: mean home = 23.990 + attack[Seattle Seahawks] +3.394 + defence[New York Jets] +3.423 = **30.81**; mean away = 21.848 + attack[New York Jets] -3.445 + defence[Seattle Seahawks] -4.067 = **14.34**. Normal approximation P(home ahead) = Phi(16.47 / 12.99) = **0.898**; the lattice price including the extra-time branch is **0.894** (PROBABILITY_TOOLKIT §1).

| team | attack | defence | net (points per game vs average) |
|---|---|---|---|
| Seattle Seahawks | 3.3941 | -4.0669 | 7.4610 |
| Los Angeles Rams | 4.3169 | -1.1976 | 5.5146 |
| Buffalo Bills | 4.1890 | -0.3725 | 4.5616 |
| Houston Texans | 0.5243 | -3.3112 | 3.8355 |
| Detroit Lions | 4.1354 | 0.4916 | 3.6438 |
| New England Patriots | 0.8463 | -2.5138 | 3.3600 |
| Jacksonville Jaguars | 2.1017 | -1.2019 | 3.3036 |
| Philadelphia Eagles | 0.1362 | -2.8576 | 2.9938 |
| Baltimore Ravens | 2.1350 | -0.5609 | 2.6959 |
| Denver Broncos | 0.0499 | -2.3682 | 2.4181 |
| San Francisco 49ers | 1.5126 | -0.1802 | 1.6928 |
| Green Bay Packers | 0.5392 | -1.1514 | 1.6906 |
| Minnesota Vikings | -1.3924 | -2.8684 | 1.4760 |
| Kansas City Chiefs | -1.0326 | -2.1267 | 1.0941 |
| Indianapolis Colts | 2.1971 | 1.4848 | 0.7123 |
| Chicago Bears | 0.9328 | 0.2543 | 0.6785 |
| Los Angeles Chargers | -1.2318 | -1.7754 | 0.5436 |
| Tampa Bay Buccaneers | 0.2957 | 0.5086 | -0.2129 |
| Pittsburgh Steelers | -0.8289 | -0.3917 | -0.4372 |
| Cincinnati Bengals | 1.6186 | 3.1929 | -1.5743 |
| Atlanta Falcons | -1.0776 | 0.8159 | -1.8935 |
| Dallas Cowboys | 2.1562 | 4.3885 | -2.2323 |
| Washington Commanders | -0.2666 | 2.3142 | -2.5808 |
| New York Giants | -1.1040 | 1.4814 | -2.5854 |
| Miami Dolphins | -1.6620 | 0.9288 | -2.5908 |
| New Orleans Saints | -3.0001 | -0.3201 | -2.6799 |
| Arizona Cardinals | -0.9146 | 2.5989 | -3.5135 |
| Carolina Panthers | -2.6483 | 0.8785 | -3.5268 |
| Cleveland Browns | -4.5225 | -0.1284 | -4.3941 |
| Tennessee Titans | -3.1695 | 2.9536 | -6.1231 |
| Las Vegas Raiders | -4.7854 | 1.6777 | -6.4631 |
| New York Jets | -3.4447 | 3.4234 | -6.8681 |


## Receipt

- `run_utc`: 2026-10-14T09:00:32Z
- `repo_head`: 3ab6d27fedb177add7cca5b41b14346107688ce3
- `code_sha256`: 9e24d01d2cb6f9878f0c00b2664fee163c69090a6b79972a091fbdfcf6db63be
- `python`: 3.14.6
- `numpy`: 2.5.2
- `pandas`: 3.0.5
- `scipy`: 1.18.1
- `model_id`: AMF-NFL-JOINT-r1
- `archive_snapshot_sha256`: 6a3e2ed90a8ac962a6ec085295498c8acc8bd15774c2d5de3b86ac0d19a1eadf
- `seconds`: 83
