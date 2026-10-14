# Parameters: `BKB-KBL-JOINT-r1`

Fit as of **2026-10-13** on every regular-season and post-season game in the archive from season 2023 to the archive's last game (2026-10-12), with the frozen hyperparameters below. Ratings drift: these numbers are a snapshot, and current-season games after the archive's last date are not in them. Class: `HAND_APPLICABLE` (ML_RL_IMPLEMENTATION_FRAMEWORK §6.7).

Hyperparameters: `half_life_days` = 90.0, `ridge` = 8.0, `cov_inflation` = 1.1

League constants: mu_home **80.744**, mu_away **79.390**; residual covariance [[118.80, 34.29], [34.29, 120.86]] (inflation included); margin SD **13.08**; residual draw share **0.000**.

**Worked example (check by hand).** 안양 정관장 레드부스터스 at home to 울산 현대모비스 피버스: mean home = 80.744 + attack[안양 정관장 레드부스터스] -2.035 + defence[울산 현대모비스 피버스] +1.173 = **79.88**; mean away = 79.390 + attack[울산 현대모비스 피버스] -0.632 + defence[안양 정관장 레드부스터스] -3.584 = **75.17**. Normal approximation P(home ahead) = Phi(4.71 / 13.08) = **0.641**; the lattice price including the extra-time branch is **0.642** (PROBABILITY_TOOLKIT §1).

| team | attack | defence | net (points per game vs average) |
|---|---|---|---|
| 안양 정관장 레드부스터스 | -2.0355 | -3.5840 | 1.5485 |
| 창원 LG 세이커스 | -0.7980 | -2.0276 | 1.2297 |
| 수원 KT 소닉붐 | 0.2668 | -0.7758 | 1.0425 |
| 고양 소노 스카이거너스 | -0.0029 | -0.9837 | 0.9808 |
| 서울 SK 나이츠 | -1.3821 | -2.0004 | 0.6184 |
| 원주 DB 프로미 | 2.3536 | 2.7289 | -0.3752 |
| 서울 삼성 썬더스 | -0.6701 | 0.0936 | -0.7637 |
| 부산 KCC 이지스 | 3.3373 | 4.1961 | -0.8588 |
| 대구 한국가스공사 페가수스 | -0.4374 | 1.1801 | -1.6175 |
| 울산 현대모비스 피버스 | -0.6318 | 1.1728 | -1.8047 |


## Receipt

- `run_utc`: 2026-10-14T09:02:26Z
- `repo_head`: 3ab6d27fedb177add7cca5b41b14346107688ce3
- `code_sha256`: 9e24d01d2cb6f9878f0c00b2664fee163c69090a6b79972a091fbdfcf6db63be
- `python`: 3.14.6
- `numpy`: 2.5.2
- `pandas`: 3.0.5
- `scipy`: 1.18.1
- `model_id`: BKB-KBL-JOINT-r1
- `archive_snapshot_sha256`: 4ae0e14227af8cd619d34c35bb01b2192e6aa7f48dbdb8ea4f030cb77fc75af6
- `seconds`: 95
