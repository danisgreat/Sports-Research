# Active file and usable-data index

**Built 2026-10-12** (audit R37, framework change [2026-10-12-1](research/verification/framework_change_2026-10-12-1/IMPLEMENTATION.md)). The repository holds tens of thousands of files, mostly history and empty placeholders. This page names the files that govern current work and the archive folders that actually contain rows, so an operator does not have to scan everything. Counts are logical CSV records, read with a CSV parser on 2026-10-12. A header-only file is missing data, never a finding. Refresh this page whenever a task adds, repairs or retires an operating file or an archive folder.

## 1. Operating documents (read these; everything else is reference or history)

| Role | File |
|---|---|
| Current values (IDs, active log, versions, scoreboard) | [CURRENT_STATE.md](CURRENT_STATE.md) |
| Method and rules | [METHOD.md](METHOD.md), [CURRENT_RULES.md](CURRENT_RULES.md), [SELECTION_RULES.md](SELECTION_RULES.md) |
| Card, mini, settlement and canonical formats; self-audit C1–C20, S1–S15 | [CARD_AND_LOG_TEMPLATES.md](CARD_AND_LOG_TEMPLATES.md) |
| Scoring and evaluation | [SCORING_AND_VALIDATION.md](SCORING_AND_VALIDATION.md) |
| Verification checks | [VERIFICATION_PROTOCOL.md](VERIFICATION_PROTOCOL.md) |
| Operator prompts 1–8 | [research/prompts/README.md](research/prompts/README.md), [PROMPTS.md](PROMPTS.md) |
| Experiments and their status | [HYPOTHESIS_REGISTER.md](HYPOTHESIS_REGISTER.md) |
| Arithmetic aids (with operative-status table) | [PROBABILITY_TOOLKIT.md](PROBABILITY_TOOLKIT.md) |
| League levels, base rates | [LEAGUE_PROFILES.md](LEAGUE_PROFILES.md), [BASE_RATES_REGISTER.md](BASE_RATES_REGISTER.md) |
| Source routes and reachability | [SOURCES.md](SOURCES.md) |
| Archive use, recipes (R2 form windows) and integrity rules | [ARCHIVE_USE_GUIDE.md](ARCHIVE_USE_GUIDE.md) |
| Sport rules and lessons (v11 precedence banner at the top of each) | `RULES_<SPORT>.md`, [LEAGUE_RULES_CRICKET.md](LEAGUE_RULES_CRICKET.md), [LEAGUE_RULES_SOCCER.md](LEAGUE_RULES_SOCCER.md) |
| Current queue and canonical status | [GAME_LOG_STATUS_CURRENT.md](GAME_LOG_STATUS_CURRENT.md) (current section at the top; later sections are dated history) |
| Active Combined Log | named in CURRENT_STATE (Part 7 on 2026-10-12) |
| Contribution and publication rules | [CONTRIBUTING.md](CONTRIBUTING.md) |
| Recovery of removed or moved paths | [HISTORICAL_LINK_INDEX.md](HISTORICAL_LINK_INDEX.md) |
| Model workshop (maintainer code; never read by prompts 1–3) | [ml/README.md](ml/README.md), outputs in [research/model_shadow/](research/model_shadow/README.md), design [ML_RL_IMPLEMENTATION_FRAMEWORK_2026-10-14.md](ML_RL_IMPLEMENTATION_FRAMEWORK_2026-10-14.md) |

**History, not instructions:** `archive/`, `prediction logs/` parts 1–6, dated folders under `research/verification/`, `research/issued_research/`, LEARNING_REGISTER / LEARNINGS_INDEX (lessons, with promotion status), FRAMEWORK_RETROSPECTIVE_2026-10-09, NUMERICAL_MODEL_REGISTER (design notes), VALIDATION_EVIDENCE.

**Root-document archive, 2026-10-14:** the ten historical documents approved for archiving have moved to [archive/root_documents_2026-10-14/](archive/root_documents_2026-10-14/README.md), including FRAMEWORK_RETROSPECTIVE_2026-10-09 and NUMERICAL_MODEL_REGISTER. Their contents are preserved; they are not operating instructions. See [old-path recovery](HISTORICAL_LINK_INDEX.md#root-document-archive-2026-10-14). The data-coverage counts below remain their original dated snapshot.

## 2. Archive folders that contain rows

40 of 172 competition folders hold at least one data row: 522,048 logical rows, or 500,328 after excluding the four alias copies (updated 2026-10-14 for the five basketball folders rebuilt by framework change [2026-10-14-1](research/verification/framework_change_2026-10-14-1/IMPLEMENTATION.md): +46,314 rows). The other 132 folders are header-only placeholders (Baseball 7, Basketball 15, Canadian Football 3, College Football 8, Cricket one-day 6, Cricket T20 11, Cricket Tests 5, Field Hockey 7, Ice Hockey 12, Rugby League 7, Rugby Union 14, Soccer 30, State Level AFL 5, Tennis 2). Paths are `Previous Sports Results/<Sport>/<Competition>/<Year>/<Year>_games.csv`.

**Duplicate folders on main (found 2026-10-12).** Four pairs are byte-identical across all their seasons, which breaks ARCHIVE_USE_GUIDE §9 rule 1. The canonical member is named below, and each alias carries a note. Rows were **not** deleted; whether to empty the alias folders is an owner decision (implementation map NEW-01).

**SUSPECTED_DEFAULT** (ARCHIVE_USE_GUIDE §9 rule 4) marks a column where one non-blank value fills at least half of 200+ rows, or a date pattern that is concentrated. It is a diagnostic, **not** a verdict. KBO 18:30 and NPB 18:00 weekday starts and New Year's Day bowl games may be genuine. Austrian and Greek basketball and Danish hockey start times match the pattern of the fabricated builds quarantined on 2026-10-12, and NBA/WNBA `Attendance = 0` looks like zero standing in for missing. Until a prompt-7 check classifies a flagged column, do not use it as evidence (rest-day, start-time, attendance or date-window features).

| Sport / competition | Populated seasons (first–last) | Logical rows | Header columns (populated files) | Provenance doc | Status and notes (2026-10-12 scan) |
|---|---|---:|---:|---|---|
| [AFL / AFL](Previous%20Sports%20Results/AFL/AFL/) | 126 (1900–2025) | 18,221 | 13 | no | — |
| [AFL / AFL Grand Final](Previous%20Sports%20Results/AFL/AFL%20Grand%20Final/) | 126 (1900–2025) | 129 | 13 | no | — |
| [AFL / AFLW](Previous%20Sports%20Results/AFL/AFLW/) | 13 (2013–2025) | 793 | 13 | no | — |
| [American Football / College Football](Previous%20Sports%20Results/American%20Football/College%20Football/) | 126 (1900–2025) | 790 | 13 | no | **ALIAS** (byte-identical to `College Football/NCAA Division I FBS`, 51 or 126 of the same seasons): not canonical; never aggregate with it; `SUSPECTED_DEFAULT` Date: 306/790 rows on month-day 01-01 (39%) |
| [American Football / IFAF World Championship](Previous%20Sports%20Results/American%20Football/IFAF%20World%20Championship/) | 5 (1999–2015) | 50 | 13 | no | — |
| [American Football / NFL](Previous%20Sports%20Results/American%20Football/NFL/) | 106 (1920–2025) | 18,192 | 13 | no | — |
| [American Football / Super Bowl](Previous%20Sports%20Results/American%20Football/Super%20Bowl/) | 59 (1967–2025) | 59 | 13 | no | — |
| [American Football / UFL](Previous%20Sports%20Results/American%20Football/UFL/) | 2 (2024–2025) | 78 | 13 | no | — |
| [Baseball / KBO](Previous%20Sports%20Results/Baseball/KBO/) | 26 (2000–2025) | 17,764 | 45 | no | `SUSPECTED_DEFAULT` Start Time (KST): '18:30' on 10410/17764 (59%). 2025 innings, extras and stage labels repaired from the KBO owner record on 2026-10-12 (R31); 2000–2024 innings remain placeholders (ARCHIVE_USE_GUIDE §8) |
| [Baseball / MLB](Previous%20Sports%20Results/Baseball/MLB/) | 27 (2000–2026) | 77,831 | 104 | no | — |
| [Baseball / Minor Leagues](Previous%20Sports%20Results/Baseball/Minor%20Leagues/) | 26 (2000–2025) | 57,665 | 46 | no | — |
| [Baseball / NPB](Previous%20Sports%20Results/Baseball/NPB/) | 26 (2000–2025) | 22,345 | 46 | no | `SUSPECTED_DEFAULT` Start Time (JST): '18:00' on 16657/22345 (75%). 2025 innings, extras and two stage labels repaired from npb.jp box scores on 2026-10-12 (R31); 2000–2024 innings remain placeholders |
| [Basketball / Austria Basketball Bundesliga](Previous%20Sports%20Results/Basketball/Austria%20Basketball%20Bundesliga/) | 51 (1975–2025) | 7,449 | 39 | no | CANONICAL for a duplicated pair; `SUSPECTED_DEFAULT` Start Time (Local): '17:30' on 4818/7449 (65%) |
| [Basketball / B League](Previous%20Sports%20Results/Basketball/B%20League/) | 11 (2016–2026) | 6,350 | 46 | yes | Rebuilt 2026-10-14 (bleague.jp, field owner); no quarters, attendance or referees in the source; pre-2016 leagues not rebuilt |
| [Basketball / BSL](Previous%20Sports%20Results/Basketball/BSL/) | 51 (1975–2025) | 7,449 | 39 | no | **ALIAS** (byte-identical to `Basketball/Austria Basketball Bundesliga`, 51 or 126 of the same seasons): not canonical; never aggregate with it; `SUSPECTED_DEFAULT` Start Time (Local): '17:30' on 4818/7449 (65%) |
| [Basketball / EuroBasket](Previous%20Sports%20Results/Basketball/EuroBasket/) | 51 (1975–2025) | 1,319 | 44 | no | — |
| [Basketball / EuroCup](Previous%20Sports%20Results/Basketball/EuroCup/) | 25 (2002–2026) | 4,851 | 46 | yes | Rebuilt 2026-10-14 (Euroleague Basketball API, field owner); pre-2002 cups not rebuilt |
| [Basketball / EuroLeague](Previous%20Sports%20Results/Basketball/EuroLeague/) | 26 (2000–2025) | 6,685 | 49 | no | — |
| [Basketball / Greek Basket League](Previous%20Sports%20Results/Basketball/Greek%20Basket%20League/) | 51 (1975–2025) | 8,179 | 39 | no | `SUSPECTED_DEFAULT` Start Time (Local): '19:30' on 5596/8179 (68%) |
| [Basketball / KBL](Previous%20Sports%20Results/Basketball/KBL/) | 31 (1996–2026) | 8,285 | 46 | yes | Rebuilt 2026-10-14 (KBL API, field owner); the inaugural 1997 season is filed under 1996 |
| [Basketball / Liga ACB](Previous%20Sports%20Results/Basketball/Liga%20ACB/) | 52 (1975–2026) | 15,881 | 46 | yes | Rebuilt 2026-10-14 (acb.com, field owner); start times blank 1975-76 to 1989-90 (source placeholder); no venue, attendance, referee or quarter fields |
| [Basketball / NBA](Previous%20Sports%20Results/Basketball/NBA/) | 51 (1975–2025) | 59,788 | 29 | no | `SUSPECTED_DEFAULT` Attendance: '0' on 30313/59788 (51%) |
| [Basketball / NBA G League](Previous%20Sports%20Results/Basketball/NBA%20G%20League/) | 22 (2004–2025) | 10,947 | 46 | yes | Rebuilt 2026-10-14 (stats.gleague.nba.com, field owner; ESPN enrichment on 4,809 rows, evidence B); `Basketball/G League/` must not be recreated |
| [Basketball / NBL](Previous%20Sports%20Results/Basketball/NBL/) | 52 (1975–2026) | 8,124 | 39 | no | 2025 dates and stage types repaired 2026-10-12 (R30); some quarter rows do not sum to the final (ARCHIVE_USE_GUIDE §8) |
| [Basketball / WNBA](Previous%20Sports%20Results/Basketball/WNBA/) | 51 (1975–2025) | 6,676 | 29 | no | `SUSPECTED_DEFAULT` Attendance: '0' on 3824/6676 (57%) |
| [College Football / NCAA Division I FBS](Previous%20Sports%20Results/College%20Football/NCAA%20Division%20I%20FBS/) | 126 (1900–2025) | 790 | 13 | no | CANONICAL for a duplicated pair; `SUSPECTED_DEFAULT` Date: 306/790 rows on month-day 01-01 (39%) |
| [Cricket One-Day Format / Men's ODI International](Previous%20Sports%20Results/Cricket%20One-Day%20Format/Men%27s%20ODI%20International/) | 51 (1975–2025) | 4,428 | 47 | no | **ALIAS** (byte-identical to `Cricket One-Day Format/ODI International`, 51 or 126 of the same seasons): not canonical; never aggregate with it |
| [Cricket One-Day Format / ODI International](Previous%20Sports%20Results/Cricket%20One-Day%20Format/ODI%20International/) | 51 (1975–2025) | 4,428 | 47 | no | CANONICAL for a duplicated pair |
| [Cricket T20 / IPL](Previous%20Sports%20Results/Cricket%20T20/IPL/) | 51 (1975–2025) | 1,213 | 46 | no | — |
| [Cricket Tests / County Championship](Previous%20Sports%20Results/Cricket%20Tests/County%20Championship/) | 51 (1975–2025) | 7,894 | 57 | no | — |
| [Ice Hockey / Czech Extraliga](Previous%20Sports%20Results/Ice%20Hockey/Czech%20Extraliga/) | 51 (1975–2025) | 18,752 | 56 | yes | — |
| [Ice Hockey / Danish Metal Ligaen](Previous%20Sports%20Results/Ice%20Hockey/Danish%20Metal%20Ligaen/) | 51 (1975–2025) | 9,053 | 41 | no | CANONICAL for a duplicated pair; `SUSPECTED_DEFAULT` Start Time (Local): '15:00' on 5672/9053 (63%) |
| [Ice Hockey / Metal Ligaen](Previous%20Sports%20Results/Ice%20Hockey/Metal%20Ligaen/) | 51 (1975–2025) | 9,053 | 41 | no | **ALIAS** (byte-identical to `Ice Hockey/Danish Metal Ligaen`, 51 or 126 of the same seasons): not canonical; never aggregate with it; `SUSPECTED_DEFAULT` Start Time (Local): '15:00' on 5672/9053 (63%) |
| [Ice Hockey / NHL](Previous%20Sports%20Results/Ice%20Hockey/NHL/) | 51 (1975–2025) | 58,379 | 32 | no | — |
| [Rugby League / NRL](Previous%20Sports%20Results/Rugby%20League/NRL/) | 51 (1975–2025) | 9,583 | 39 | no | — |
| [Soccer / Premier League](Previous%20Sports%20Results/Soccer/Premier%20League/) | 51 (1975–2025) | 20,740 | 54 | yes | — |
| [State Level AFL / SANFL](Previous%20Sports%20Results/State%20Level%20AFL/SANFL/) | 4 (2022–2025) | 384 | 13 | no | — |
| [State Level AFL / VFL](Previous%20Sports%20Results/State%20Level%20AFL/VFL/) | 5 (2021–2025) | 972 | 13 | no | — |
| [State Level AFL / VFLW](Previous%20Sports%20Results/State%20Level%20AFL/VFLW/) | 5 (2021–2025) | 460 | 13 | no | — |
| [State Level AFL / WAFL](Previous%20Sports%20Results/State%20Level%20AFL/WAFL/) | 126 (1900–2025) | 10,019 | 13 | no | — |
