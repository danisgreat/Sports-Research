# Parameters: `RL-NRL-JOINT-r1`

Fit as of **2025-10-06** on every regular-season and post-season game in the archive from season 2022 to the archive's last game (2025-10-05), with the frozen hyperparameters below. Ratings drift: these numbers are a snapshot, and current-season games after the archive's last date are not in them. Class: `HAND_APPLICABLE` (ML_RL_IMPLEMENTATION_FRAMEWORK §6.7).

Hyperparameters: `half_life_days` = 180.0, `ridge` = 2.0, `cov_inflation` = 1.1

League constants: mu_home **25.316**, mu_away **21.515**; residual covariance [[136.55, -32.99], [-32.99, 121.69]] (inflation included); margin SD **18.01**; residual draw share **0.163**.

**Worked example (check by hand).** Melbourne Storm at home to Newcastle Knights: mean home = 25.316 + attack[Melbourne Storm] +3.383 + defence[Newcastle Knights] +2.759 = **31.46**; mean away = 21.515 + attack[Newcastle Knights] -6.723 + defence[Melbourne Storm] -4.162 = **10.63**. Normal approximation P(home ahead) = Phi(20.83 / 18.01) = **0.876**; the lattice price including the extra-time branch is **0.857** (PROBABILITY_TOOLKIT §1).

| team | attack | defence | net (points per game vs average) |
|---|---|---|---|
| Melbourne Storm | 3.3832 | -4.1620 | 7.5452 |
| Sydney Roosters | 4.2014 | -3.0617 | 7.2632 |
| Penrith Panthers | 1.8380 | -4.7138 | 6.5518 |
| Cronulla Sutherland Sharks | 1.9079 | -3.8053 | 5.7132 |
| Brisbane Broncos | 3.8513 | -1.4876 | 5.3389 |
| Dolphins | 5.1101 | 2.6045 | 2.5056 |
| Canterbury Bankstown Bulldogs | -1.3022 | -3.5654 | 2.2632 |
| Manly Warringah Sea Eagles | 0.2937 | -0.6144 | 0.9082 |
| Canberra Raiders | 0.8462 | -0.0535 | 0.8997 |
| Warriors | -2.5670 | -1.5865 | -0.9806 |
| Parramatta Eels | -0.4653 | 1.1005 | -1.5658 |
| North Queensland Cowboys | 0.5217 | 2.9601 | -2.4385 |
| St George Illawarra Dragons | -2.1025 | 2.9172 | -5.0196 |
| South Sydney Rabbitohs | -3.6251 | 1.4936 | -5.1186 |
| Gold Coast Titans | -1.5707 | 5.5668 | -7.1375 |
| Wests Tigers | -3.5978 | 3.6486 | -7.2464 |
| Newcastle Knights | -6.7230 | 2.7588 | -9.4818 |


## Receipt

- `run_utc`: 2026-10-14T09:04:58Z
- `repo_head`: 3ab6d27fedb177add7cca5b41b14346107688ce3
- `code_sha256`: 9e24d01d2cb6f9878f0c00b2664fee163c69090a6b79972a091fbdfcf6db63be
- `python`: 3.14.6
- `numpy`: 2.5.2
- `pandas`: 3.0.5
- `scipy`: 1.18.1
- `model_id`: RL-NRL-JOINT-r1
- `archive_snapshot_sha256`: e6ae0e16ed76975379c4e355e58b8f06a0155738636c942807d2b97c3ce8751c
- `seconds`: 103
