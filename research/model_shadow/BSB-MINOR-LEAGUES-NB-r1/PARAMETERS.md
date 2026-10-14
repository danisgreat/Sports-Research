# Parameters: `BSB-MINOR-LEAGUES-NB-r1`

Fit as of **2025-09-28** on every regular-season and post-season game in the archive from season 2022 to the archive's last game (2025-09-27), with the frozen hyperparameters below. Ratings drift: these numbers are a snapshot, and current-season games after the archive's last date are not in them. Class: `HAND_APPLICABLE` (ML_RL_IMPLEMENTATION_FRAMEWORK §6.7).

Hyperparameters: `half_life_days` = 365.0, `ridge` = 128.0

League constants: intercept c **1.6827**, home **-0.0222**, phi **0.2398**, P(home wins extra time) **0.523**; promoted-team prior centre (attack, defence) (+0.000, +0.000).

**Worked example (check by hand).** Scranton/Wilkes-Barre RailRiders at home to Charlotte Knights: lambda_home = exp(1.6827 + -0.0222 + +0.0319 + +0.1144) = **6.091**; lambda_away = exp(1.6827 + -0.0131 + -0.0953) = **4.827**. Grid winner masses (home, draw, away) = **(0.598, 0.000, 0.402)** (PROBABILITY_TOOLKIT §2–§3 tables).

| team | attack | defence | net_log_rate |
|---|---|---|---|
| Scranton/Wilkes-Barre RailRiders | 0.0319 | -0.0953 | 0.1272 |
| Nashville Sounds | 0.0044 | -0.1128 | 0.1172 |
| Oklahoma City Dodgers | 0.0689 | -0.0379 | 0.1068 |
| Durham Bulls | -0.0087 | -0.1150 | 0.1064 |
| Tacoma Rainiers | 0.0821 | 0.0025 | 0.0796 |
| Oklahoma City Baseball Club | -0.0072 | -0.0826 | 0.0754 |
| Oklahoma City Comets | 0.0860 | 0.0151 | 0.0709 |
| Memphis Redbirds | 0.0468 | -0.0210 | 0.0678 |
| Worcester Red Sox | 0.0123 | -0.0454 | 0.0577 |
| Toledo Mud Hens | -0.0112 | -0.0637 | 0.0526 |
| Jacksonville Jumbo Shrimp | -0.0984 | -0.1300 | 0.0316 |
| Indianapolis Indians | -0.0309 | -0.0599 | 0.0290 |
| Las Vegas Aviators | 0.1212 | 0.0969 | 0.0243 |
| Lehigh Valley IronPigs | 0.0342 | 0.0150 | 0.0192 |
| Round Rock Express | -0.0202 | -0.0150 | -0.0052 |
| Iowa Cubs | -0.0082 | -0.0007 | -0.0075 |
| Columbus Clippers | -0.0426 | -0.0270 | -0.0156 |
| El Paso Chihuahuas | 0.0964 | 0.1138 | -0.0174 |
| Norfolk Tides | 0.0226 | 0.0428 | -0.0202 |
| Reno Aces | 0.0980 | 0.1239 | -0.0260 |
| Sugar Land Space Cowboys | -0.0965 | -0.0652 | -0.0314 |
| Syracuse Mets | -0.0426 | -0.0087 | -0.0339 |
| Louisville Bats | -0.0110 | 0.0359 | -0.0469 |
| Omaha Storm Chasers | -0.0048 | 0.0421 | -0.0469 |
| Sacramento River Cats | -0.0665 | -0.0186 | -0.0479 |
| St. Paul Saints | -0.0266 | 0.0421 | -0.0687 |
| Buffalo Bisons | -0.0670 | 0.0061 | -0.0731 |
| Gwinnett Stripers | -0.2022 | -0.1241 | -0.0780 |
| Rochester Red Wings | -0.0133 | 0.0866 | -0.1000 |
| Salt Lake Bees | -0.0176 | 0.0900 | -0.1076 |
| Albuquerque Isotopes | 0.0776 | 0.1916 | -0.1140 |
| Charlotte Knights | -0.0131 | 0.1144 | -0.1275 |


## Receipt

- `run_utc`: 2026-10-14T09:04:14Z
- `repo_head`: 3ab6d27fedb177add7cca5b41b14346107688ce3
- `code_sha256`: 9e24d01d2cb6f9878f0c00b2664fee163c69090a6b79972a091fbdfcf6db63be
- `python`: 3.14.6
- `numpy`: 2.5.2
- `pandas`: 3.0.5
- `scipy`: 1.18.1
- `model_id`: BSB-MINOR-LEAGUES-NB-r1
- `archive_snapshot_sha256`: f0df08d6dce87a1350a9c713e15fb9e612766fa2745888de63757074b460eafd
- `seconds`: 304
