# Parameters: `BKB-EUROLEAGUE-JOINT-r1`

Fit as of **2026-05-25** on every regular-season and post-season game in the archive from season 2022 to the archive's last game (2026-05-24), with the frozen hyperparameters below. Ratings drift: these numbers are a snapshot, and current-season games after the archive's last date are not in them. Class: `HAND_APPLICABLE` (ML_RL_IMPLEMENTATION_FRAMEWORK §6.7).

Hyperparameters: `half_life_days` = 180.0, `ridge` = 8.0, `cov_inflation` = 1.1

League constants: mu_home **87.500**, mu_away **84.013**; residual covariance [[115.61, 43.79], [43.79, 109.84]] (inflation included); margin SD **11.74**; residual draw share **0.000**.

**Worked example (check by hand).** Olympiacos Piraeus at home to ALBA Berlin: mean home = 87.500 + attack[Olympiacos Piraeus] +3.086 + defence[ALBA Berlin] +2.144 = **92.73**; mean away = 84.013 + attack[ALBA Berlin] -2.935 + defence[Olympiacos Piraeus] -3.515 = **77.56**. Normal approximation P(home ahead) = Phi(15.17 / 11.74) = **0.902**; the lattice price including the extra-time branch is **0.904** (PROBABILITY_TOOLKIT §1).

| team | attack | defence | net (points per game vs average) |
|---|---|---|---|
| Olympiacos Piraeus | 3.0856 | -3.5147 | 6.6003 |
| Real Madrid | 1.9115 | -2.8196 | 4.7311 |
| Valencia Basket | 3.3947 | 0.1539 | 3.2408 |
| Panathinaikos AKTOR Athens | 0.8737 | -1.4488 | 2.3224 |
| Zalgiris Kaunas | -0.2661 | -2.3884 | 2.1223 |
| Fenerbahce Beko Istanbul | -2.3719 | -4.3438 | 1.9719 |
| Hapoel IBI Tel Aviv | 1.3960 | -0.1188 | 1.5148 |
| AS Monaco | 1.8362 | 0.5007 | 1.3356 |
| FC Barcelona | -1.1586 | -2.3818 | 1.2232 |
| Crvena Zvezda Meridianbet Belgrade | 0.7599 | -0.1321 | 0.8919 |
| Dubai Basketball | 2.1170 | 1.6487 | 0.4684 |
| Cazoo Baskonia Vitoria-Gasteiz | 0.0785 | -0.0289 | 0.1074 |
| Paris Basketball | 3.2123 | 3.1237 | 0.0886 |
| Panathinaikos Athens | -0.1995 | -0.0875 | -0.1120 |
| Baskonia Vitoria-Gasteiz | -0.3942 | -0.0312 | -0.3630 |
| Maccabi Playtika Tel Aviv | 0.8667 | 1.6338 | -0.7672 |
| EA7 Emporio Armani Milan | 0.3088 | 1.0906 | -0.7818 |
| Anadolu Efes Istanbul | -3.1825 | -1.8458 | -1.3368 |
| FC Bayern Munich | -2.6737 | -1.1682 | -1.5055 |
| Maccabi Rapyd Tel Aviv | 3.6732 | 5.2718 | -1.5986 |
| Virtus Segafredo Bologna | -2.6590 | -0.9861 | -1.6729 |
| Partizan Mozzart Bet Belgrade | -2.8243 | -0.8674 | -1.9569 |
| Kosner Baskonia Vitoria-Gasteiz | 2.5344 | 5.5762 | -3.0418 |
| Virtus Bologna | -2.8802 | 0.8445 | -3.7247 |
| LDLC ASVEL Villeurbanne | -4.5036 | 0.1753 | -4.6789 |
| ALBA Berlin | -2.9351 | 2.1437 | -5.0788 |


## Receipt

- `run_utc`: 2026-10-14T09:02:09Z
- `repo_head`: 3ab6d27fedb177add7cca5b41b14346107688ce3
- `code_sha256`: 9e24d01d2cb6f9878f0c00b2664fee163c69090a6b79972a091fbdfcf6db63be
- `python`: 3.14.6
- `numpy`: 2.5.2
- `pandas`: 3.0.5
- `scipy`: 1.18.1
- `model_id`: BKB-EUROLEAGUE-JOINT-r1
- `archive_snapshot_sha256`: be335921205567a11b625046f80d2b2011c835a56a25427eaad2df6992cfaa9d
- `seconds`: 106
