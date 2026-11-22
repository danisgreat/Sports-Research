# Mini Settlement · 20261118DA6D9F6251746B979F5895FA · P-686 to P-696 (mini-settlement-10)

**Settled:** 2026-11-22T17:40:00+11:00 · **Framework:** MDS-2026.11.18-v29.1 / CR-2026.11.18-R2 / SCV-2026.11.18-v20 / P-2026.11.18-v29.1 · **Authority:** `LOCAL_WORKING_TREE`, branch `main`.
**Source mini:** `20261118DA6D9F6251746B979F5895FA` pulled from `origin/forecast-seals` (10 sealed cards: G0002, G0003, G0005, G0006, G0008–G0013; 12 registered requests) and `origin/card-drops` (G0001 unsealed card + G0004 unregistered draft request). Archived byte-exact at `archive/settled_minis_2026-11-22/20261118DA6D9F6251746B979F5895FA/`.

## Executive summary

- **Games settled:** 11 distinct events (**P-686 to P-696**), **46 contract rows** (23 WIN, 23 LOSS, **0 UNRESOLVED**, 0 PUSH, 0 VOID).
- **Non-card keys accounted for (0 IDs consumed):** `20261118DA6D9F6251746B979F5895FA-G0004` (unregistered AHL draft request using `ML`, superseded by `G0005`) and `20261118DA6D9F6251746B979F5895FA-G0007` (`NBA:0022600258` MEM @ CLE, registered on `forecast-seals`, no card produced — `NO_FORECAST`).
- **Descriptive slot counts (ONECHAT_V1 cards):** Rank 1 **8W / 3L (72.7%)**; Rank 2 **5W / 6L (45.5%)**.
- **Card-mean Brier vs 0.25:** all 11 cards = **0.2422** (`d = +0.0078`); 10 sealed cards = **0.2449** (`d = +0.0051`). Descriptive only; no predictive advantage is certified.
- **Track P (`ONE-CHAT-v3`) first-play custody:** **1 game (`P-689` / `G0005`, AHL)** has an official verified first-play capture (`7:05 pm EST` in `G0005_ahl_api.json`) proving server seal 7m20s before puck drop (`SEALED_PRE_START_SERVER`). The other 9 sealed cards lack an official first-play capture (`FIRST_PLAY_UNVERIFIED`), and 5 of those 9 were sealed after scheduled start.
- **Deep loss reviews (`DEEPLOSS-v1`):** **10 reviews** across 7 cards appended to `research/deep_loss/DEEP_LOSS_REGISTER.csv` (`DLR-2026-11-22-001` through `DLR-2026-11-22-010`).

## Source discovery, corroboration and reuse register (EXH-v1 / SRC-ALT-v3)

Every settlement URL was checked with `ml.source_audit` before fetching. Hosts returning `RULES_UNKNOWN` (`cdn.nba.com`, `site.api.espn.com`) or `BLOCKED` (`www.espn.com`, `www.cricbuzz.com`) were strictly skipped. All 11 finals were captured directly from permitted (`ALLOWED` / `NO_RULES_FILE`) sources into `../one_chat_captures/2026-11-22/` with SHA-256 verification; full audits are in `SOURCE_ACCESS_AUDIT.csv`, `SOURCE_DISCOVERY_REGISTER.csv`, `SOURCE_SEARCH_ATTEMPTS.csv`, `REQUIREMENT_CLOSURE.csv`, and `CITED_URL_ACCESS_AUDIT_CHATGPT.csv`.

## Per-card settlements, R1–R12 retrospectives and DEEPLOSS-v1 reviews

<!-- BEGIN SETTLEMENT P-686 LOCAL-20261118DA6D9F6251746B979F5895FA-G0001 revision-1 -->
### P-686 · Basketball/NBA Regular Season (game 0022600254) — Portland Trail Blazers @ Minnesota Timberwolves · 2026-11-17 CT · revision-1

- **Local key / native ID:** `LOCAL-20261118DA6D9F6251746B979F5895FA-G0001` · `NBA:0022600254` · **Effective:** `2026-11-22T17:40:00+11:00`
- **Custody & timing:** `UNSEALED` (server push `NONE`; assessment `UNSEALED_DROP_REFUSED`; actual first play `NOT_VERIFIED`).
- **Verified final (B):** **Minnesota Timberwolves 106-105 Portland Trail Blazers** · Linescore: `POR 17-31-31-26=105; MIN 29-20-30-27=106 (sum check: 17+31+31+26=105, 29+20+30+27=106)`.
- **Permitted source & capture:** `https://www.foxsports.com/nba/portland-trail-blazers-vs-minnesota-timberwolves-nov-17-2026-game-boxscore-106739` · capture `2026-11-22/G0001_fox_box.html` (SHA-256 `f3af78436756f7609a31e9afe90763ca3fc4588754d51f590b74bf8d896112b8`). Corroboration: https://basketball.realgm.com/nba/scores/2026-11-17 (web search corroboration; script blocked, not fetched by script).
- **Card-mean Brier / d:** `0.2150` / `+0.0350`.

| Label | Rank | Family | Side | Line | Stated p | Centre | Avail | Grade | Brier |
|---|---|---|---|---:|---:|---:|---|---|---:|
| L1 | R1 | HANDICAP | AWAY | 4.5 | 0.538347 | -2.945 | UNMEASURED | **WIN** | 0.2131 |
| L1 | NOT_RANKED | HANDICAP | HOME | -4.5 | 0.461653 | 2.945 | UNMEASURED | **LOSS** | 0.2131 |
| L2 | NOT_RANKED | TOTAL | OVER | 225.5 | 0.465662 | 224.127 | UNMEASURED | **LOSS** | 0.2168 |
| L2 | R2 | TOTAL | UNDER | 225.5 | 0.534338 | 224.127 | UNMEASURED | **WIN** | 0.2168 |

**R1–R12 retrospective:** Jaden McDaniels hit the go-ahead basket with 2.6s left; Ayo Dosunmu scored 30, Damian Lillard 25, Jrue Holiday 23. Both card leans won (POR +4.5 by 3.5 pts; Under 225.5 by 14.5 pts). Card failed DROP-SEAL due to 4 FACTS rows missing source URLs. All contracts settled from box-score/linescore sum check; original stated probabilities and `UNMEASURED` availability flags preserved literally; no post-event backfilling.

**Deep loss review:** None required (Rank 1, top side, and top total all won).
<!-- END SETTLEMENT P-686 LOCAL-20261118DA6D9F6251746B979F5895FA-G0001 revision-1 -->

<!-- BEGIN SETTLEMENT P-687 LOCAL-20261118DA6D9F6251746B979F5895FA-G0002 revision-1 -->
### P-687 · Basketball/NCAAB 2026-27 — Michigan State Spartans @ Tennessee Volunteers · 2026-11-17 ET · revision-1

- **Local key / native ID:** `LOCAL-20261118DA6D9F6251746B979F5895FA-G0002` · `UTK_GAMECENTER:30166` · **Effective:** `2026-11-22T17:40:00+11:00`
- **Custody & timing:** `SEALED` (server push `2026-11-18T01:59:51Z`; assessment `SEALED_BEFORE_SCHEDULED_FIRST_PLAY_UNVERIFIED`; actual first play `NOT_VERIFIED`).
- **Verified final (A):** **Tennessee 61-46 Michigan State** · Linescore: `MSU 25-21=46; TENN 27-34=61 (sum check: 25+21=46, 27+34=61)`.
- **Permitted source & capture:** `https://www.foxsports.com/college-basketball/michigan-state-spartans-vs-tennessee-volunteers-nov-17-2026-game-boxscore-264973` · capture `2026-11-22/G0002_fox_box.html` (SHA-256 `2eb3a3d42da1d9407edad4f3d4a8afb53769459e9b7635cebf59e5e1ee3d9694`). Corroboration: https://utsports.com/game-center/30166 (official host game center captured in G0002_utk.html).
- **Card-mean Brier / d:** `0.2845` / `-0.0345`.

| Label | Rank | Family | Side | Line | Stated p | Centre | Avail | Grade | Brier |
|---|---|---|---|---:|---:|---:|---|---|---:|
| L1 | R1 | HANDICAP | AWAY | -2.5 | 0.5346 | 3.5417 | UNMEASURED | **LOSS** | 0.2858 |
| L1 | NOT_RANKED | HANDICAP | HOME | 2.5 | 0.4654 | -3.5417 | UNMEASURED | **WIN** | 0.2858 |
| L2 | R2 | TOTAL | OVER | 149.5 | 0.5322 | 150.7917 | UNMEASURED | **LOSS** | 0.2832 |
| L2 | NOT_RANKED | TOTAL | UNDER | 149.5 | 0.4678 | 150.7917 | UNMEASURED | **WIN** | 0.2832 |

**R1–R12 retrospective:** Tennessee held Michigan State to 9-50 FG (18.0%) and 4-19 3PT (21.1%); MSU scored 24 of its 46 points at the free-throw line (Jeremy Fears Jr. 0-3 FG, 16-18 FT). Total finished 42.5 points below 149.5. All contracts settled from box-score/linescore sum check; original stated probabilities and `UNMEASURED` availability flags preserved literally; no post-event backfilling.

#### Deep loss review(s) (DEEPLOSS-v1)

**DLR-2026-11-22-001 · P-687 · Michigan -2.5 (TOP_SIDE_AND_RANK_1) — Verdict: `VARIANCE` · Class: `VARIANCE`**
1. **Contract & trigger:** Michigan -2.5 (TOP_SIDE_AND_RANK_1).
2. **Frozen forecast & distribution:** see table above (all rows marked `availability_basis=UNMEASURED`).
3. **Verified box score & linescore:** Tennessee 61-46 Michigan State (MSU 25-21=46; TENN 27-34=61 (sum check: 25+21=46, 27+34=61)).
4. **Outcome in frozen distribution & what decided the game:** MSU shot an extreme-tail 9-50 FG (18.0%), a multi-sigma shooting collapse despite drawing 30 FTAs and committing only 3 turnovers. However, stated p=0.5346 sat inside the H-NODIR coin-flip band (|p-0.5| < 0.05) and carried availability_basis=UNMEASURED.
5. **Pre-issue evidence & timing audit:** custody `SEALED`, timing `SEALED_BEFORE_SCHEDULED_FIRST_PLAY_UNVERIFIED`, exposure `NONE`.
6. **Plain verdict & process lesson:** `VARIANCE` (`VARIANCE`). No rule change applied during `FREEZE-v1`; logged to `DEEP_LOSS_REGISTER.csv` for prompt 8.

**DLR-2026-11-22-002 · P-687 · Over 149.5 (TOP_TOTAL) — Verdict: `MODEL_LIMIT` · Class: `BASKETBALL_TOTAL_WITHOUT_PACE_MODEL`**
1. **Contract & trigger:** Over 149.5 (TOP_TOTAL).
2. **Frozen forecast & distribution:** see table above (all rows marked `availability_basis=UNMEASURED`).
3. **Verified box score & linescore:** Tennessee 61-46 Michigan State (MSU 25-21=46; TENN 27-34=61 (sum check: 25+21=46, 27+34=61)).
4. **Outcome in frozen distribution & what decided the game:** Card projected 150.79 (p=0.5322) from raw early-season scoring averages without a tempo/defensive-efficiency model for Tennessee's elite half-court defense; actual total was 107 (-42.5 vs line, z approx -2.4).
5. **Pre-issue evidence & timing audit:** custody `SEALED`, timing `SEALED_BEFORE_SCHEDULED_FIRST_PLAY_UNVERIFIED`, exposure `NONE`.
6. **Plain verdict & process lesson:** `MODEL_LIMIT` (`BASKETBALL_TOTAL_WITHOUT_PACE_MODEL`). No rule change applied during `FREEZE-v1`; logged to `DEEP_LOSS_REGISTER.csv` for prompt 8.

**Joint side + total loss note (P-687):** Both top side and top total lost on this card (card-mean Brier `0.2845`, `d = -0.0345`). Shared root causes: unmeasured availability / opponent-strength overreach paired with unadjusted total Over bias.
<!-- END SETTLEMENT P-687 LOCAL-20261118DA6D9F6251746B979F5895FA-G0002 revision-1 -->

<!-- BEGIN SETTLEMENT P-688 LOCAL-20261118DA6D9F6251746B979F5895FA-G0003 revision-1 -->
### P-688 · Basketball/Japan B.LEAGUE Premier 2026-27 (ScheduleKey 506605) — Chiba Jets vs Akita Northern Happinets · 2026-11-18 JST · revision-1

- **Local key / native ID:** `LOCAL-20261118DA6D9F6251746B979F5895FA-G0003` · `B.LEAGUE:506605` · **Effective:** `2026-11-22T17:40:00+11:00`
- **Custody & timing:** `SEALED` (server push `2026-11-18T10:05:22Z`; assessment `SEALED_AFTER_SCHEDULED_FIRST_PLAY_UNVERIFIED`; actual first play `NOT_VERIFIED`).
- **Verified final (A):** **Chiba Jets 89-84 Akita Northern Happinets** · Linescore: `CHB 24-24-16-25=89; AKI 18-27-15-24=84 (sum check: 24+24+16+25=89, 18+27+15+24=84)`.
- **Permitted source & capture:** `https://www.bleague.jp/game_detail/?ScheduleKey=506605` · capture `2026-11-22/G0003_bleague.html` (SHA-256 `740da59fec86f6c659e0dc2fe18b16a2eb065cfdb9100eb2060cbe7cd5e09055`). Corroboration: https://www.bleague.jp/en/game_detail/?ScheduleKey=506605 (captured in G0003_bleague_en.html).
- **Card-mean Brier / d:** `0.2341` / `+0.0159`.

| Label | Rank | Family | Side | Line | Stated p | Centre | Avail | Grade | Brier |
|---|---|---|---|---:|---:|---:|---|---|---:|
| L1 | NOT_RANKED | HANDICAP | HOME | -8.5 | 0.356623 | 2.9875 | UNMEASURED | **LOSS** | 0.1272 |
| L1 | R1 | HANDICAP | AWAY | 8.5 | 0.643377 | -2.9875 | UNMEASURED | **WIN** | 0.1272 |
| L2 | R2 | TOTAL | OVER | 180.5 | 0.583898 | 184.7375 | UNMEASURED | **LOSS** | 0.3409 |
| L2 | NOT_RANKED | TOTAL | UNDER | 180.5 | 0.416102 | 184.7375 | UNMEASURED | **WIN** | 0.3409 |

**R1–R12 retrospective:** Chiba won by 5 (Akita +8.5 Rank 1 won comfortably at p=0.6434); slow Q3 (16-15, 31 pts) kept combined total at 173 vs 180.5. All contracts settled from box-score/linescore sum check; original stated probabilities and `UNMEASURED` availability flags preserved literally; no post-event backfilling.

#### Deep loss review(s) (DEEPLOSS-v1)

**DLR-2026-11-22-003 · P-688 · Over 180.5 (TOP_TOTAL) — Verdict: `MODEL_LIMIT` · Class: `BASKETBALL_TOTAL_WITHOUT_PACE_MODEL`**
1. **Contract & trigger:** Over 180.5 (TOP_TOTAL).
2. **Frozen forecast & distribution:** see table above (all rows marked `availability_basis=UNMEASURED`).
3. **Verified box score & linescore:** Chiba Jets 89-84 Akita Northern Happinets (CHB 24-24-16-25=89; AKI 18-27-15-24=84 (sum check: 24+24+16+25=89, 18+27+15+24=84)).
4. **Outcome in frozen distribution & what decided the game:** Card projected 184.74 (p=0.5839) from blended scoring rates without adjusting for Akita's slower defensive tempo; Q3 produced only 31 combined points and final total finished 173 (-7.5 vs line).
5. **Pre-issue evidence & timing audit:** custody `SEALED`, timing `SEALED_AFTER_SCHEDULED_FIRST_PLAY_UNVERIFIED`, exposure `NONE`.
6. **Plain verdict & process lesson:** `MODEL_LIMIT` (`BASKETBALL_TOTAL_WITHOUT_PACE_MODEL`). No rule change applied during `FREEZE-v1`; logged to `DEEP_LOSS_REGISTER.csv` for prompt 8.
<!-- END SETTLEMENT P-688 LOCAL-20261118DA6D9F6251746B979F5895FA-G0003 revision-1 -->

<!-- BEGIN SETTLEMENT P-689 LOCAL-20261118DA6D9F6251746B979F5895FA-G0005 revision-1 -->
### P-689 · Ice Hockey/AHL 2026-27 (game 1029340) — Rochester Americans @ Syracuse Crunch · 2026-11-18 ET · revision-1

- **Local key / native ID:** `LOCAL-20261118DA6D9F6251746B979F5895FA-G0005` · `AHL:1029340` · **Effective:** `2026-11-22T17:40:00+11:00`
- **Custody & timing:** `SEALED` (server push `2026-11-18T23:57:40Z`; assessment `SEALED_PRE_START_SERVER`; actual first play `2026-11-18T19:05:00-05:00`).
- **Verified final (A):** **Rochester Americans 2-1 Syracuse Crunch (Regulation)** · Linescore: `ROC 0-1-1=2; SYR 0-0-1=1 (sum check: 0+1+1=2, 0+0+1=1; shots ROC 20, SYR 24; 3 PPG total)`.
- **Permitted source & capture:** `https://lscluster.hockeytech.com/feed/index.php?feed=statviewfeed&view=gameSummary&game_id=1029340&key=50c2cd9b5e18e390&site_id=1&client_code=ahl&lang=en` · capture `2026-11-22/G0005_ahl_api.json` (SHA-256 `a6f3993e2999c3f45d7af74104235746df02e3b6340016db19c878b904c51f19`). Corroboration: https://theahl.com/stats/game-center/1029340 (captured in G0005_ahl_web.html) + amerks.com / syracusecrunch.com.
- **Card-mean Brier / d:** `0.2128` / `+0.0372`.

| Label | Rank | Family | Side | Line | Stated p | Centre | Avail | Grade | Brier |
|---|---|---|---|---:|---:|---:|---|---|---:|
| L1 | R1 | HANDICAP | AWAY | -0.5 | 0.5822 | 0.5150 | UNMEASURED | **WIN** | 0.1746 |
| L1 | NOT_RANKED | HANDICAP | HOME | 0.5 | 0.4178 | -0.5150 | UNMEASURED | **LOSS** | 0.1746 |
| L2 | NOT_RANKED | HANDICAP | HOME | -0.5 | 0.4178 | -0.5150 | UNMEASURED | **LOSS** | 0.1746 |
| L2 | R2 | HANDICAP | AWAY | 0.5 | 0.5822 | 0.5150 | UNMEASURED | **WIN** | 0.1746 |
| L3 | R3 | TOTAL | OVER | 5.5 | 0.5378 | 5.8980 | UNMEASURED | **LOSS** | 0.2892 |
| L3 | NOT_RANKED | TOTAL | UNDER | 5.5 | 0.4622 | 5.8980 | UNMEASURED | **WIN** | 0.2892 |

**R1–R12 retrospective:** Official HockeyTech JSON verifies puck drop 7:05 pm EST (00:05Z), 7m20s AFTER GitHub server seal (23:57:40Z) — first SEALED_PRE_START_SERVER qualifying game in Track P. Rochester won 2-1 in regulation (both L1 -0.5 and L2 +0.5 won, though L1 and L2 are duplicate representations of the same 2-way OT/SO-inclusive side). Low-event game (44 combined shots, scoreless P1) finished 3 goals vs 5.5. All contracts settled from box-score/linescore sum check; original stated probabilities and `UNMEASURED` availability flags preserved literally; no post-event backfilling.

#### Deep loss review(s) (DEEPLOSS-v1)

**DLR-2026-11-22-004 · P-689 · Over 5.5 (TOP_TOTAL) — Verdict: `VARIANCE` · Class: `VARIANCE`**
1. **Contract & trigger:** Over 5.5 (TOP_TOTAL).
2. **Frozen forecast & distribution:** see table above (all rows marked `availability_basis=UNMEASURED`).
3. **Verified box score & linescore:** Rochester Americans 2-1 Syracuse Crunch (Regulation) (ROC 0-1-1=2; SYR 0-0-1=1 (sum check: 0+1+1=2, 0+0+1=1; shots ROC 20, SYR 24; 3 PPG total)).
4. **Outcome in frozen distribution & what decided the game:** Card projected 5.90 goals (p=0.5378, inside H-NODIR band). Game had 44 combined shots and 9 power plays (3 PPG) but zero even-strength goals; 3 total goals is routine Poisson variance (approx 16% tail under lambda=5.9).
5. **Pre-issue evidence & timing audit:** custody `SEALED`, timing `SEALED_PRE_START_SERVER`, exposure `NONE`.
6. **Plain verdict & process lesson:** `VARIANCE` (`VARIANCE`). No rule change applied during `FREEZE-v1`; logged to `DEEP_LOSS_REGISTER.csv` for prompt 8.
<!-- END SETTLEMENT P-689 LOCAL-20261118DA6D9F6251746B979F5895FA-G0005 revision-1 -->

<!-- BEGIN SETTLEMENT P-690 LOCAL-20261118DA6D9F6251746B979F5895FA-G0006 revision-1 -->
### P-690 · Basketball/NBA Regular Season (game 0022600259) — Houston Rockets @ Indiana Pacers · 2026-11-18 ET · revision-1

- **Local key / native ID:** `LOCAL-20261118DA6D9F6251746B979F5895FA-G0006` · `NBA:0022600259` · **Effective:** `2026-11-22T17:40:00+11:00`
- **Custody & timing:** `SEALED` (server push `2026-11-19T00:06:05Z`; assessment `SEALED_AFTER_SCHEDULED_FIRST_PLAY_UNVERIFIED`; actual first play `NOT_VERIFIED`).
- **Verified final (B):** **Houston Rockets 119-104 Indiana Pacers** · Linescore: `HOU 39-23-31-26=119; IND 28-18-30-28=104 (sum check: 39+23+31+26=119, 28+18+30+28=104)`.
- **Permitted source & capture:** `https://www.foxsports.com/nba/houston-rockets-vs-indiana-pacers-nov-18-2026-game-boxscore-106744` · capture `2026-11-22/G0006_fox_box.html` (SHA-256 `9912841ae4cfdef255429da28a6958457165ab404b604ba832f0aec611edad18`). Corroboration: https://basketball.realgm.com/nba/scores/2026-11-18 (web search corroboration; script blocked).
- **Card-mean Brier / d:** `0.3636` / `-0.1136`.

| Label | Rank | Family | Side | Line | Stated p | Centre | Avail | Grade | Brier |
|---|---|---|---|---:|---:|---:|---|---|---:|
| L1 | NOT_RANKED | HANDICAP | AWAY | -8.5 | 0.3958 | 4.4246 | UNMEASURED | **WIN** | 0.3651 |
| L1 | R1 | HANDICAP | HOME | 8.5 | 0.6042 | -4.4246 | UNMEASURED | **LOSS** | 0.3651 |
| L2 | R2 | TOTAL | OVER | 224.5 | 0.6018 | 229.6354 | UNMEASURED | **LOSS** | 0.3622 |
| L2 | NOT_RANKED | TOTAL | UNDER | 224.5 | 0.3982 | 229.6354 | UNMEASURED | **WIN** | 0.3622 |

**R1–R12 retrospective:** Houston jumped to a 62-46 halftime lead (Kevin Durant 21, Reed Sheppard 20 on 6-7 3PT, Jabari Smith Jr. 17) against an Indiana backcourt missing Tyrese Haliburton and Andrew Nembhard. Both Pacers +8.5 (p=0.6042) and Over 224.5 (p=0.6018, actual 223) lost. All contracts settled from box-score/linescore sum check; original stated probabilities and `UNMEASURED` availability flags preserved literally; no post-event backfilling.

#### Deep loss review(s) (DEEPLOSS-v1)

**DLR-2026-11-22-005 · P-690 · Packers +8.5 (TOP_SIDE_AND_RANK_1) — Verdict: `ERROR` · Class: `UNFITTED_ANALYST_ADJUSTMENT` (alias `UNMEASURED_AVAILABILITY_PRICED`)**
1. **Contract & trigger:** Packers +8.5 (TOP_SIDE_AND_RANK_1).
2. **Frozen forecast & distribution:** see table above (all rows marked `availability_basis=UNMEASURED`).
3. **Verified box score & linescore:** Houston Rockets 119-104 Indiana Pacers (HOU 39-23-31-26=119; IND 28-18-30-28=104 (sum check: 39+23+31+26=119, 28+18+30+28=104)).
4. **Outcome in frozen distribution & what decided the game:** Indiana was missing both starting guards (Haliburton, Nembhard); card marked availability_basis=UNMEASURED yet priced Pacers +8.5 at 0.6042 (Rank 1) with an expected margin of -4.42 instead of leaving the line UNPRICED per AUDIT-v1. Houston won by 15.
5. **Pre-issue evidence & timing audit:** custody `SEALED`, timing `SEALED_AFTER_SCHEDULED_FIRST_PLAY_UNVERIFIED`, exposure `NONE`.
6. **Plain verdict & process lesson:** `ERROR` (`UNFITTED_ANALYST_ADJUSTMENT` / `UNMEASURED_AVAILABILITY_PRICED`). No rule change applied during `FREEZE-v1`; logged to `DEEP_LOSS_REGISTER.csv` for prompt 8.

**DLR-2026-11-22-006 · P-690 · Over 224.5 (TOP_TOTAL) — Verdict: `VARIANCE` · Class: `VARIANCE`**
1. **Contract & trigger:** Over 224.5 (TOP_TOTAL).
2. **Frozen forecast & distribution:** see table above (all rows marked `availability_basis=UNMEASURED`).
3. **Verified box score & linescore:** Houston Rockets 119-104 Indiana Pacers (HOU 39-23-31-26=119; IND 28-18-30-28=104 (sum check: 39+23+31+26=119, 28+18+30+28=104)).
4. **Outcome in frozen distribution & what decided the game:** Actual total 223 missed 224.5 by 1.5 points despite a 67-point Q1; Q2 slowed to 41 combined points (23-18). Within 0.4 SD of card's 229.6 centre.
5. **Pre-issue evidence & timing audit:** custody `SEALED`, timing `SEALED_AFTER_SCHEDULED_FIRST_PLAY_UNVERIFIED`, exposure `NONE`.
6. **Plain verdict & process lesson:** `VARIANCE` (`VARIANCE`). No rule change applied during `FREEZE-v1`; logged to `DEEP_LOSS_REGISTER.csv` for prompt 8.

**Joint side + total loss note (P-690):** Both top side and top total lost on this card (card-mean Brier `0.3636`, `d = -0.1136`). Shared root causes: unmeasured availability / opponent-strength overreach paired with unadjusted total Over bias.
<!-- END SETTLEMENT P-690 LOCAL-20261118DA6D9F6251746B979F5895FA-G0006 revision-1 -->

<!-- BEGIN SETTLEMENT P-691 LOCAL-20261118DA6D9F6251746B979F5895FA-G0008 revision-1 -->
### P-691 · Basketball/NBA Regular Season (game 0022600265) — Atlanta Hawks @ Oklahoma City Thunder · 2026-11-18 CT · revision-1

- **Local key / native ID:** `LOCAL-20261118DA6D9F6251746B979F5895FA-G0008` · `NBA:0022600265` · **Effective:** `2026-11-22T17:40:00+11:00`
- **Custody & timing:** `SEALED` (server push `2026-11-19T00:55:08Z`; assessment `SEALED_BEFORE_SCHEDULED_FIRST_PLAY_UNVERIFIED`; actual first play `NOT_VERIFIED`).
- **Verified final (B):** **Atlanta Hawks 117-112 Oklahoma City Thunder** · Linescore: `ATL 31-33-19-34=117; OKC 29-22-32-29=112 (sum check: 31+33+19+34=117, 29+22+32+29=112)`.
- **Permitted source & capture:** `https://www.foxsports.com/nba/atlanta-hawks-vs-oklahoma-city-thunder-nov-18-2026-game-boxscore-106749` · capture `2026-11-22/G0008_fox_box.html` (SHA-256 `b23f869d9f53b087b49a1254313a09fba051faacf4d2a59b8ff9e06d9efb134c`). Corroboration: https://basketball.realgm.com/nba/scores/2026-11-18 (web search corroboration; script blocked).
- **Card-mean Brier / d:** `0.1950` / `+0.0550`.

| Label | Rank | Family | Side | Line | Stated p | Centre | Avail | Grade | Brier |
|---|---|---|---|---:|---:|---:|---|---|---:|
| L1 | R1 | HANDICAP | AWAY | 6.5 | 0.5988 | -2.6368 | UNMEASURED | **WIN** | 0.1610 |
| L1 | NOT_RANKED | HANDICAP | HOME | -6.5 | 0.4012 | 2.6368 | UNMEASURED | **LOSS** | 0.1610 |
| L2 | R2 | TOTAL | OVER | 228.5 | 0.5214 | 229.5704 | UNMEASURED | **WIN** | 0.2291 |
| L2 | NOT_RANKED | TOTAL | UNDER | 228.5 | 0.4786 | 229.5704 | UNMEASURED | **LOSS** | 0.2291 |

**R1–R12 retrospective:** Atlanta won outright 117-112 behind 20-50 3PT shooting (Okongwu 28, Alexander-Walker 19, Jalen Johnson 16/12/11 triple-double). Both ATL +6.5 (Rank 1, p=0.5988) and Over 228.5 (Rank 2, p=0.5214, total 229) won. All contracts settled from box-score/linescore sum check; original stated probabilities and `UNMEASURED` availability flags preserved literally; no post-event backfilling.

**Deep loss review:** None required (Rank 1, top side, and top total all won).
<!-- END SETTLEMENT P-691 LOCAL-20261118DA6D9F6251746B979F5895FA-G0008 revision-1 -->

<!-- BEGIN SETTLEMENT P-692 LOCAL-20261118DA6D9F6251746B979F5895FA-G0009 revision-1 -->
### P-692 · Basketball/NBA Regular Season (game 0022600264) — Detroit Pistons @ New Orleans Pelicans · 2026-11-18 CT · revision-1

- **Local key / native ID:** `LOCAL-20261118DA6D9F6251746B979F5895FA-G0009` · `NBA:0022600264` · **Effective:** `2026-11-22T17:40:00+11:00`
- **Custody & timing:** `SEALED` (server push `2026-11-19T01:06:10Z`; assessment `SEALED_AFTER_SCHEDULED_FIRST_PLAY_UNVERIFIED`; actual first play `NOT_VERIFIED`).
- **Verified final (B):** **Detroit Pistons 122-109 New Orleans Pelicans** · Linescore: `DET 31-36-25-30=122; NOP 31-29-26-23=109 (sum check: 31+36+25+30=122, 31+29+26+23=109)`.
- **Permitted source & capture:** `https://www.foxsports.com/nba/detroit-pistons-vs-new-orleans-pelicans-nov-18-2026-game-boxscore-106748` · capture `2026-11-22/G0009_fox_box.html` (SHA-256 `994cc432a25fd1625c413b8a32bc3e880febc9b965b7fc802bdf959c0136fe81`). Corroboration: https://basketball.realgm.com/nba/scores/2026-11-18 (web search corroboration; script blocked).
- **Card-mean Brier / d:** `0.0682` / `+0.1818`.

| Label | Rank | Family | Side | Line | Stated p | Centre | Avail | Grade | Brier |
|---|---|---|---|---:|---:|---:|---|---|---:|
| L1 | R1 | HANDICAP | AWAY | 3.5 | 0.7901 | 8.9492 | UNMEASURED | **WIN** | 0.0441 |
| L1 | NOT_RANKED | HANDICAP | HOME | -3.5 | 0.2099 | -8.9492 | UNMEASURED | **LOSS** | 0.0441 |
| L2 | R2 | TOTAL | OVER | 224.5 | 0.6961 | 234.7127 | UNMEASURED | **WIN** | 0.0924 |
| L2 | NOT_RANKED | TOTAL | UNDER | 224.5 | 0.3039 | 234.7127 | UNMEASURED | **LOSS** | 0.0924 |

**R1–R12 retrospective:** Detroit shot 53.2% FG / 53.1% 3PT (17-32) to win 122-109 despite Zion Williamson's 24 and Jordan Poole's 22. Both DET +3.5 (p=0.7901) and Over 224.5 (p=0.6961, total 231) won decisively (best card Brier 0.0682, d=+0.1818). Note: sealed 6m10s after scheduled start (actual tip unverified). All contracts settled from box-score/linescore sum check; original stated probabilities and `UNMEASURED` availability flags preserved literally; no post-event backfilling.

**Deep loss review:** None required (Rank 1, top side, and top total all won).
<!-- END SETTLEMENT P-692 LOCAL-20261118DA6D9F6251746B979F5895FA-G0009 revision-1 -->

<!-- BEGIN SETTLEMENT P-693 LOCAL-20261118DA6D9F6251746B979F5895FA-G0010 revision-1 -->
### P-693 · Basketball/NCAAB 2026-27 — Samford Bulldogs @ USC Upstate Spartans · 2026-11-18 ET · revision-1

- **Local key / native ID:** `LOCAL-20261118DA6D9F6251746B979F5895FA-G0010` · `UPSTATE_GAMECENTER:6709` · **Effective:** `2026-11-22T17:40:00+11:00`
- **Custody & timing:** `SEALED` (server push `2026-11-19T01:29:43Z`; assessment `SEALED_BEFORE_SCHEDULED_FIRST_PLAY_UNVERIFIED`; actual first play `NOT_VERIFIED`).
- **Verified final (A):** **Samford 74-64 USC Upstate** · Linescore: `SAM 37-37=74; UPST 27-37=64 (sum check: 37+37=74, 27+37=64)`.
- **Permitted source & capture:** `https://samfordsports.com/boxscore.aspx?id=13967` · capture `2026-11-22/G0010_samford_box.html` (SHA-256 `5d6331f79e9b10982a3186fd322967aca776517d22231128967baa750efb69c6`). Corroboration: https://upstatespartans.com/game-center/6709 (captured in G0010_upstate.html).
- **Card-mean Brier / d:** `0.4185` / `-0.1685`.

| Label | Rank | Family | Side | Line | Stated p | Centre | Avail | Grade | Brier |
|---|---|---|---|---:|---:|---:|---|---|---:|
| L1 | R1 | HANDICAP | HOME | 8.5 | 0.7354 | 1.5667 | UNMEASURED | **LOSS** | 0.5408 |
| L1 | NOT_RANKED | HANDICAP | AWAY | -8.5 | 0.2646 | -1.5667 | UNMEASURED | **WIN** | 0.5408 |
| L2 | R2 | TOTAL | OVER | 150.5 | 0.5442 | 152.5000 | UNMEASURED | **LOSS** | 0.2962 |
| L2 | NOT_RANKED | TOTAL | UNDER | 150.5 | 0.4558 | 152.5000 | UNMEASURED | **WIN** | 0.2962 |

**R1–R12 retrospective:** Samford led 37-27 at half and won 74-64 (Cooper Noard 19, Will Shaver 15/11, Cade Norris 14/7/7). Worst Brier card of mini (0.4185, d=-0.1685): Upstate +8.5 was priced at 0.7354 (expected margin +1.57 home) on a 1-5 mid-major without opponent-strength adjustment. All contracts settled from box-score/linescore sum check; original stated probabilities and `UNMEASURED` availability flags preserved literally; no post-event backfilling.

#### Deep loss review(s) (DEEPLOSS-v1)

**DLR-2026-11-22-007 · P-693 · Upstate +8.5 (TOP_SIDE_AND_RANK_1) — Verdict: `ERROR` · Class: `SMALL_SAMPLE_STRENGTH_OVERREACH` (alias `PLUS_HANDICAP_WITHOUT_OPPONENT_CHECK`)**
1. **Contract & trigger:** Upstate +8.5 (TOP_SIDE_AND_RANK_1).
2. **Frozen forecast & distribution:** see table above (all rows marked `availability_basis=UNMEASURED`).
3. **Verified box score & linescore:** Samford 74-64 USC Upstate (SAM 37-37=74; UPST 27-37=64 (sum check: 37+37=74, 27+37=64)).
4. **Outcome in frozen distribution & what decided the game:** Card priced USC Upstate +8.5 at 0.7354 (centre +1.57 home!) from raw early-season PPG on a tiny sample (1-5 record) with no opponent-strength adjustment against a stronger SoCon opponent (Samford). This repeats the exact PLUS_HANDICAP_WITHOUT_OPPONENT_CHECK failure class from P-660 and P-685, causing a -0.2908 Brier loss on L1 alone.
5. **Pre-issue evidence & timing audit:** custody `SEALED`, timing `SEALED_BEFORE_SCHEDULED_FIRST_PLAY_UNVERIFIED`, exposure `NONE`.
6. **Plain verdict & process lesson:** `ERROR` (`SMALL_SAMPLE_STRENGTH_OVERREACH` / `PLUS_HANDICAP_WITHOUT_OPPONENT_CHECK`). No rule change applied during `FREEZE-v1`; logged to `DEEP_LOSS_REGISTER.csv` for prompt 8.

**DLR-2026-11-22-008 · P-693 · Over 150.5 (TOP_TOTAL) — Verdict: `MODEL_LIMIT` · Class: `BASKETBALL_TOTAL_WITHOUT_PACE_MODEL`**
1. **Contract & trigger:** Over 150.5 (TOP_TOTAL).
2. **Frozen forecast & distribution:** see table above (all rows marked `availability_basis=UNMEASURED`).
3. **Verified box score & linescore:** Samford 74-64 USC Upstate (SAM 37-37=74; UPST 27-37=64 (sum check: 37+37=74, 27+37=64)).
4. **Outcome in frozen distribution & what decided the game:** Card projected 152.50 (p=0.5442, inside H-NODIR band) from unadjusted early-season averages; actual total finished 138 (-12.5 vs line).
5. **Pre-issue evidence & timing audit:** custody `SEALED`, timing `SEALED_BEFORE_SCHEDULED_FIRST_PLAY_UNVERIFIED`, exposure `NONE`.
6. **Plain verdict & process lesson:** `MODEL_LIMIT` (`BASKETBALL_TOTAL_WITHOUT_PACE_MODEL`). No rule change applied during `FREEZE-v1`; logged to `DEEP_LOSS_REGISTER.csv` for prompt 8.

**Joint side + total loss note (P-693):** Both top side and top total lost on this card (card-mean Brier `0.4185`, `d = -0.1685`). Shared root causes: unmeasured availability / opponent-strength overreach paired with unadjusted total Over bias.
<!-- END SETTLEMENT P-693 LOCAL-20261118DA6D9F6251746B979F5895FA-G0010 revision-1 -->

<!-- BEGIN SETTLEMENT P-694 LOCAL-20261118DA6D9F6251746B979F5895FA-G0011 revision-1 -->
### P-694 · Basketball/NBA Regular Season (game 0022600268) — Utah Jazz @ Los Angeles Lakers · 2026-11-18 PT · revision-1

- **Local key / native ID:** `LOCAL-20261118DA6D9F6251746B979F5895FA-G0011` · `NBA:0022600268` · **Effective:** `2026-11-22T17:40:00+11:00`
- **Custody & timing:** `SEALED` (server push `2026-11-19T03:14:19Z`; assessment `SEALED_AFTER_SCHEDULED_FIRST_PLAY_UNVERIFIED`; actual first play `NOT_VERIFIED`).
- **Verified final (B):** **Utah Jazz 109-97 Los Angeles Lakers** · Linescore: `UTA 29-27-22-31=109; LAL 34-20-22-21=97 (sum check: 29+27+22+31=109, 34+20+22+21=97)`.
- **Permitted source & capture:** `https://www.foxsports.com/nba/utah-jazz-vs-los-angeles-lakers-nov-18-2026-game-boxscore-106753` · capture `2026-11-22/G0011_fox_box.html` (SHA-256 `c855ad9a03274036f90f90482c61e4499d6e72c6b985696424d3fa2d70b244c8`). Corroboration: https://basketball.realgm.com/nba/scores/2026-11-18 (web search corroboration; script blocked).
- **Card-mean Brier / d:** `0.2280` / `+0.0220`.

| Label | Rank | Family | Side | Line | Stated p | Centre | Avail | Grade | Brier |
|---|---|---|---|---:|---:|---:|---|---|---:|
| L1 | R1 | HANDICAP | AWAY | 11.5 | 0.6367 | -6.1050 | UNMEASURED | **WIN** | 0.1320 |
| L1 | NOT_RANKED | HANDICAP | HOME | -11.5 | 0.3633 | 6.1050 | UNMEASURED | **LOSS** | 0.1320 |
| L2 | R2 | TOTAL | OVER | 229.5 | 0.5692 | 232.9700 | UNMEASURED | **LOSS** | 0.3240 |
| L2 | NOT_RANKED | TOTAL | UNDER | 229.5 | 0.4308 | 232.9700 | UNMEASURED | **WIN** | 0.3240 |

**R1–R12 retrospective:** Utah upset the 13-2 Lakers 109-97 (Keyonte George 30/10, Ace Bailey 19; Luka Doncic 10-28 FG / 2-12 3PT for 29, LAL 38.2% FG / 27.3% 3PT on 0-day B2B). Jazz +11.5 (Rank 1, p=0.6367) won by 23.5 pts; Over 229.5 (Rank 2, p=0.5692) lost by 23.5 pts (total 206). Note: sealed 14m19s after scheduled start (request arrived 5m after schedule). All contracts settled from box-score/linescore sum check; original stated probabilities and `UNMEASURED` availability flags preserved literally; no post-event backfilling.

#### Deep loss review(s) (DEEPLOSS-v1)

**DLR-2026-11-22-009 · P-694 · Over 229.5 (TOP_TOTAL) — Verdict: `MODEL_LIMIT` · Class: `REGIME_IGNORED` (alias `BACK_TO_BACK_FATIGUE_TOTAL_OVER`)**
1. **Contract & trigger:** Over 229.5 (TOP_TOTAL).
2. **Frozen forecast & distribution:** see table above (all rows marked `availability_basis=UNMEASURED`).
3. **Verified box score & linescore:** Utah Jazz 109-97 Los Angeles Lakers (UTA 29-27-22-31=109; LAL 34-20-22-21=97 (sum check: 29+27+22+31=109, 34+20+22+21=97)).
4. **Outcome in frozen distribution & what decided the game:** Card explicitly noted BOTH teams were on the second night of a back-to-back (0 rest days, Jazz flying from Sacramento) yet projected 232.97 (Over 229.5 at p=0.5692) with no fatigue discount. LAL shot 38.2% FG / 27.3% 3PT and both teams committed 41 combined turnovers, finishing 206 (-23.5 vs line).
5. **Pre-issue evidence & timing audit:** custody `SEALED`, timing `SEALED_AFTER_SCHEDULED_FIRST_PLAY_UNVERIFIED`, exposure `NONE`.
6. **Plain verdict & process lesson:** `MODEL_LIMIT` (`REGIME_IGNORED` / `BACK_TO_BACK_FATIGUE_TOTAL_OVER`). No rule change applied during `FREEZE-v1`; logged to `DEEP_LOSS_REGISTER.csv` for prompt 8.
<!-- END SETTLEMENT P-694 LOCAL-20261118DA6D9F6251746B979F5895FA-G0011 revision-1 -->

<!-- BEGIN SETTLEMENT P-695 LOCAL-20261118DA6D9F6251746B979F5895FA-G0012 revision-1 -->
### P-695 · Basketball/Australia NBL 2026-27 Round 10 — Adelaide 36ers @ Illawarra Hawks · 2026-11-19 AEDT · revision-1

- **Local key / native ID:** `LOCAL-20261118DA6D9F6251746B979F5895FA-G0012` · `NBL:illawarra-hawks-v-adelaide-36ers-men-19-11-2026` · **Effective:** `2026-11-22T17:40:00+11:00`
- **Custody & timing:** `SEALED` (server push `2026-11-19T08:38:16Z`; assessment `SEALED_AFTER_SCHEDULED_FIRST_PLAY_UNVERIFIED`; actual first play `NOT_VERIFIED`).
- **Verified final (A):** **Illawarra Hawks 103-97 Adelaide 36ers** · Linescore: `ILL 23-23-25-32=103; ADE 26-23-24-24=97 (sum check: 23+23+25+32=103, 26+23+24+24=97)`.
- **Permitted source & capture:** `https://www.nblfixtures.com/games/illawarra-hawks-vs-adelaide-36ers-2026-11-19` · capture `2026-11-22/G0012_nblfixtures.html` (SHA-256 `5f026797ecd8d38c1d0d038524a37f5bd0bc0fc0bc2b66527d274b9e94e1e8a1`). Corroboration: https://www.nbl.com.au/matches/illawarra-hawks-v-adelaide-36ers-men-19-11-2026 (official match page captured in G0012_nbl.html + nbl.com.au recap corroboration).
- **Card-mean Brier / d:** `0.2205` / `+0.0295`.

| Label | Rank | Family | Side | Line | Stated p | Centre | Avail | Grade | Brier |
|---|---|---|---|---:|---:|---:|---|---|---:|
| L1 | R2 | HANDICAP | HOME | 4.5 | 0.5304 | -3.2746 | UNMEASURED | **WIN** | 0.2205 |
| L1 | NOT_RANKED | HANDICAP | AWAY | -4.5 | 0.4696 | 3.2746 | UNMEASURED | **LOSS** | 0.2205 |
| L2 | R1 | TOTAL | OVER | 196.5 | 0.5305 | 197.9838 | UNMEASURED | **WIN** | 0.2204 |
| L2 | NOT_RANKED | TOTAL | UNDER | 196.5 | 0.4695 | 197.9838 | UNMEASURED | **LOSS** | 0.2204 |

**R1–R12 retrospective:** Illawarra closed with a 32-24 Q4 to win 103-97 (Makur Maker 23/13, Tyler Harvey 22, Milton Doyle 19; Bryce Cotton 28/9). Both Over 196.5 (Rank 1, p=0.5305, total 200) and Hawks +4.5 (Rank 2, p=0.5304) won. Card itself explicitly self-labelled RESEARCH_ONLY / POST_SCHEDULED_START (sealed 8m16s after 19:30 AEDT schedule). All contracts settled from box-score/linescore sum check; original stated probabilities and `UNMEASURED` availability flags preserved literally; no post-event backfilling.

**Deep loss review:** None required (Rank 1, top side, and top total all won).
<!-- END SETTLEMENT P-695 LOCAL-20261118DA6D9F6251746B979F5895FA-G0012 revision-1 -->

<!-- BEGIN SETTLEMENT P-696 LOCAL-20261118DA6D9F6251746B979F5895FA-G0013 revision-1 -->
### P-696 · Cricket/Weber WBBL|12 Match 28 (CA:40648) — Adelaide Strikers Women vs Melbourne Renegades Women · 2026-11-20 AEDT · revision-1

- **Local key / native ID:** `LOCAL-20261118DA6D9F6251746B979F5895FA-G0013` · `CA:40648` · **Effective:** `2026-11-22T17:40:00+11:00`
- **Custody & timing:** `SEALED` (server push `2026-11-20T08:07:03Z`; assessment `SEALED_BEFORE_SCHEDULED_FIRST_PLAY_UNVERIFIED`; actual first play `NOT_VERIFIED`).
- **Verified final (A):** **Melbourne Renegades W 165/4 (20 ov; 32/1 after 6 ov); Adelaide Strikers W 168/5 (19.5 ov)** · Linescore: `Renegades 1st inns: Powerplay (1-6) 32/1 + Middle (7-16) 84/2 + Death (17-20) 49/1 = 165/4 (sum check: 32+84+49=165); Strikers 168/5 (19.5 ov)`.
- **Permitted source & capture:** `https://sportsguff.com/scorecard/women-s-big-bash-league-2026-27/adelaide-strikers-women-vs-melbourne-renegades-women-28th-match` · capture `2026-11-22/G0013_sportsguff.html` (SHA-256 `6f023f45466529c3aca35147dc6869c929a2a5e26e348564a24bfddc11bc967a`). Corroboration: https://www.cricket.com.au/matches/CA:40648 (official Cricket Australia captured in G0013_ca.html).
- **Card-mean Brier / d:** `0.2239` / `+0.0261`.

| Label | Rank | Family | Side | Line | Stated p | Centre | Avail | Grade | Brier |
|---|---|---|---|---:|---:|---:|---|---|---:|
| L1 | NOT_RANKED | TEAM_TOTAL | OVER | 157.5 | 0.4303 | 152.8000 | UNMEASURED | **WIN** | 0.3246 |
| L1 | R2 | TEAM_TOTAL | UNDER | 157.5 | 0.5697 | 152.8000 | UNMEASURED | **LOSS** | 0.3246 |
| L2 | NOT_RANKED | TEAM_TOTAL | OVER | 42.5 | 0.3511 | 37.4000 | UNMEASURED | **LOSS** | 0.1233 |
| L2 | R1 | TEAM_TOTAL | UNDER | 42.5 | 0.6489 | 37.4000 | UNMEASURED | **WIN** | 0.1233 |

**R1–R12 retrospective:** Renegades started slowly (32/1 after 6 overs, winning Rank 1 Under 42.5 at p=0.6489 by 10.5 runs), then Sophie Molineux (63* off 38) and a 49-run final 4 overs pushed the 20-over total to 165/4, defeating Rank 2 Under 157.5 (p=0.5697). All contracts settled from box-score/linescore sum check; original stated probabilities and `UNMEASURED` availability flags preserved literally; no post-event backfilling.

#### Deep loss review(s) (DEEPLOSS-v1)

**DLR-2026-11-22-010 · P-696 · Renegades(W) 1st Innings Runs at end of 20 overs Total: Under 157.5 (TOP_TOTAL) — Verdict: `VARIANCE` · Class: `VARIANCE`**
1. **Contract & trigger:** Renegades(W) 1st Innings Runs at end of 20 overs Total: Under 157.5 (TOP_TOTAL).
2. **Frozen forecast & distribution:** see table above (all rows marked `availability_basis=UNMEASURED`).
3. **Verified box score & linescore:** Melbourne Renegades W 165/4 (20 ov; 32/1 after 6 ov); Adelaide Strikers W 168/5 (19.5 ov) (Renegades 1st inns: Powerplay (1-6) 32/1 + Middle (7-16) 84/2 + Death (17-20) 49/1 = 165/4 (sum check: 32+84+49=165); Strikers 168/5 (19.5 ov)).
4. **Outcome in frozen distribution & what decided the game:** Renegades were 32/1 after 6 overs and 34/2 after 7 overs (on track well below 157.5), before Sophie Molineux (63* off 38) and 49 runs in overs 17-20 pushed the total to 165/4 (+7.5 vs line, +12.2 vs 152.8 centre; within 0.5 SD of T20 innings SD approx 25 runs).
5. **Pre-issue evidence & timing audit:** custody `SEALED`, timing `SEALED_BEFORE_SCHEDULED_FIRST_PLAY_UNVERIFIED`, exposure `NONE`.
6. **Plain verdict & process lesson:** `VARIANCE` (`VARIANCE`). No rule change applied during `FREEZE-v1`; logged to `DEEP_LOSS_REGISTER.csv` for prompt 8.
<!-- END SETTLEMENT P-696 LOCAL-20261118DA6D9F6251746B979F5895FA-G0013 revision-1 -->
