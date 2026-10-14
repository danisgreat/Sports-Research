# Parameters: `BKB-EUROBASKET-JOINT-r1`

Fit as of **2022-09-19** on every regular-season and post-season game in the archive from season 2016 to the archive's last game (2022-09-18), with the frozen hyperparameters below. Ratings drift: these numbers are a snapshot, and current-season games after the archive's last date are not in them. Class: `HAND_APPLICABLE` (ML_RL_IMPLEMENTATION_FRAMEWORK §6.7).

Hyperparameters: `half_life_days` = 5840.0, `ridge` = 32.0, `cov_inflation` = 1.1

League constants: mu_home **79.783**, mu_away **114.536**; residual covariance [[352.62, 511.95], [511.95, 25687.21]] (inflation included); margin SD **158.16**; residual draw share **0.000**.

**Worked example (check by hand).** Georgia at home to Turkey: mean home = 79.783 + attack[Georgia] +31.271 + defence[Turkey] +31.276 = **142.33**; mean away = 114.536 + attack[Turkey] -5.400 + defence[Georgia] -3.773 = **105.36**. Normal approximation P(home ahead) = Phi(36.97 / 158.16) = **0.592**; the lattice price including the extra-time branch is **0.453** (PROBABILITY_TOOLKIT §1).

| team | attack | defence | net (points per game vs average) |
|---|---|---|---|
| Georgia | 31.2709 | -3.7730 | 35.0439 |
| Lithuania | 17.0411 | -4.9063 | 21.9474 |
| Finland | 15.5579 | -4.5904 | 20.1483 |
| Italy | 10.5991 | -6.2228 | 16.8219 |
| Germany | -2.0400 | -8.6738 | 6.6337 |
| Slovenia | -0.6894 | -6.5118 | 5.8224 |
| Greece | -2.0312 | -4.8798 | 2.8486 |
| Serbia | -3.5309 | -6.0725 | 2.5416 |
| Croatia | -3.4110 | -4.8046 | 1.3936 |
| Latvia | -0.9666 | -2.0667 | 1.1000 |
| Estonia | -2.1308 | -3.1199 | 0.9891 |
| France | 12.4170 | 12.2693 | 0.1477 |
| Ukraine | -4.8434 | -4.3774 | -0.4659 |
| Bosnia and Herzegovina | -2.1590 | -1.4091 | -0.7499 |
| Bulgaria | -2.3284 | -1.0020 | -1.3264 |
| Russia | -4.1484 | -2.6520 | -1.4964 |
| Hungary | -4.9390 | -3.3665 | -1.5725 |
| Czech Republic | -3.8496 | -1.9403 | -1.9093 |
| Netherlands | -3.8905 | -1.1097 | -2.7808 |
| Iceland | -3.1612 | -0.1352 | -3.0259 |
| Montenegro | -7.0852 | -4.0584 | -3.0269 |
| Romania | -4.0550 | -0.7203 | -3.3347 |
| Poland | -6.6139 | -2.7762 | -3.8378 |
| Great Britain | -5.8871 | -1.1651 | -4.7220 |
| Spain | -2.8456 | 8.7212 | -11.5668 |
| Israel | -3.8721 | 15.3624 | -19.2345 |
| Belgium | -7.0075 | 12.7052 | -19.7127 |
| Turkey | -5.4003 | 31.2756 | -36.6759 |


## Receipt

- `run_utc`: 2026-10-14T08:59:41Z
- `repo_head`: 3ab6d27fedb177add7cca5b41b14346107688ce3
- `code_sha256`: 9e24d01d2cb6f9878f0c00b2664fee163c69090a6b79972a091fbdfcf6db63be
- `python`: 3.14.6
- `numpy`: 2.5.2
- `pandas`: 3.0.5
- `scipy`: 1.18.1
- `model_id`: BKB-EUROBASKET-JOINT-r1
- `archive_snapshot_sha256`: 0b2f088de6f8ae1884ccfbf3e5c7ad89715e4063e9d114c7cd473c79b9fd38f9
- `seconds`: 31
