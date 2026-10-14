# Parameters: `BKB-AUSTRIA-BASKETBALL-BUNDESLIGA-JOINT-r1`

Fit as of **2026-05-22** on every regular-season and post-season game in the archive from season 2022 to the archive's last game (2026-05-21), with the frozen hyperparameters below. Ratings drift: these numbers are a snapshot, and current-season games after the archive's last date are not in them. Class: `HAND_APPLICABLE` (ML_RL_IMPLEMENTATION_FRAMEWORK §6.7).

Hyperparameters: `half_life_days` = 1460.0, `ridge` = 8.0, `cov_inflation` = 1.0

League constants: mu_home **82.730**, mu_away **74.836**; residual covariance [[38.76, 2.77], [2.77, 41.75]] (inflation included); margin SD **8.66**; residual draw share **0.000**.

**Worked example (check by hand).** BK IMMOunited Dukes at home to C門 / Coldamaris Fürstenfeld Panthers: mean home = 82.730 + attack[BK IMMOunited Dukes] +4.472 + defence[C門 / Coldamaris Fürstenfeld Panthers] +4.782 = **91.98**; mean away = 74.836 + attack[C門 / Coldamaris Fürstenfeld Panthers] -5.806 + defence[BK IMMOunited Dukes] -4.389 = **64.64**. Normal approximation P(home ahead) = Phi(27.34 / 8.66) = **0.999**; the lattice price including the extra-time branch is **0.999** (PROBABILITY_TOOLKIT §1).

| team | attack | defence | net (points per game vs average) |
|---|---|---|---|
| BK IMMOunited Dukes | 4.4725 | -4.3889 | 8.8613 |
| Unger Steel Gunners Oberwart | 4.2167 | -2.4790 | 6.6957 |
| Swans Gmunden | 4.2669 | -1.0146 | 5.2815 |
| Raiffeisen Flyers Wels | 2.3701 | -0.5305 | 2.9007 |
| Arkadia Traiskirchen Lions | 1.6241 | -1.0175 | 2.6416 |
| UBSC Raiffeisen Graz | 1.8116 | -0.1616 | 1.9732 |
| BC Vienna | -0.4493 | -0.7091 | 0.2597 |
| Kapfenberg Bulls | -0.9333 | -0.1637 | -0.7696 |
| SKN St. Pölten Basketball | -3.1357 | 1.0531 | -4.1889 |
| BBC Nord Dragonz Eisenstadt | -4.0000 | 1.1957 | -5.1957 |
| Vienna Timberwolves | -4.4376 | 3.4340 | -7.8716 |
| C門 / Coldamaris Fürstenfeld Panthers | -5.8059 | 4.7820 | -10.5879 |


## Receipt

- `run_utc`: 2026-10-14T09:01:30Z
- `repo_head`: 3ab6d27fedb177add7cca5b41b14346107688ce3
- `code_sha256`: 9e24d01d2cb6f9878f0c00b2664fee163c69090a6b79972a091fbdfcf6db63be
- `python`: 3.14.6
- `numpy`: 2.5.2
- `pandas`: 3.0.5
- `scipy`: 1.18.1
- `model_id`: BKB-AUSTRIA-BASKETBALL-BUNDESLIGA-JOINT-r1
- `archive_snapshot_sha256`: d3f929d227064f3bba145eb30be882958de56ac76945c19d90ebb6ba44040268
- `seconds`: 140
