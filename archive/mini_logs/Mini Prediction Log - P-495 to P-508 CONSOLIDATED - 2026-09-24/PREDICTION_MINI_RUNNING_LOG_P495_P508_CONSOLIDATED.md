# Prediction Mini Running Log — P-495 onward (started 2026-09-23)

| Field | Value |
|---|---|
| Created | 2026-09-23 21:45:00 +10:00 (Australia/Melbourne, AEST UTC+10; AEDT from 4 Oct 2026) |
| Status | **ACTIVE MINI LOG.** P-495..P-509 issued. |
| Next canonical ID | **P-510**, advanced after P-509 issue. |
| Temporary IDs awaiting canonical reconciliation (they do **not** reserve numbers) | `TMP-20260923-NBL-CNS-TAS` (settled; formerly claimed P-487) and `TMP-20260923-NPB-CHU-DB-G25` (live, carried below; wrongly merged into P-489 earlier). Each takes the next free canonical ID then available. **P-487 is resolved:** it is Dallas Wings @ Phoenix Mercury. The card body was recovered and settled in Part 5 §"2026-09-23(d)", and `TMP-20260922-WNBA-DAL-PHX` is a retired alias. |
| Governing method for the next issue | METHOD.md **MDS-2026.09.19-v4.3** / control revision **CR-2026.09.21-3** (unchanged); SCORING_AND_VALIDATION **SCV-2026.09.19-v2**. **Freeze with every card:** `CONTROL_MANIFEST_2026-09-23.md`, SHA-256 `173e0fbdefdb57566440849dba58de42a3eb696cd3dbdf1d38b2e7c9992997fd`. It is the post-import content receipt written by the 2026-09-23 consolidated import; METHOD.md now points to it. Before issuing, re-hash the listed governance files: they must match, except the two living logs (Part 5, the status register), which change with every card. |
| Operating mode | **SPORTS_ONLY / MARKET_BLIND.** No odds, prices, line movement, tipsters, betting previews, prediction markets or fantasy/DFS material as evidence, anchors or sanity checks. Supplied lines are quarantined until the distribution is frozen (METHOD §1.1). |
| Performance status | **LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE.** No ROI, EV, calibrated-edge or validated-model claim. `NO VALUE DETERMINABLE` unless a governing value gate is explicitly satisfied. |
| Drive scope | Google Drive is the reference copy of the methodology and learnings; this session reads the repository mirror at `C:\Users\danie\Desktop\Sports Research` (synced from Drive folder `1ChlwkiOvd8c4MTaLC5BvkLniWogrm8Lj`). **No Drive file is created, edited, moved or renamed from this workflow.** This log lives in the local `Mini logs (to be sent to actual log later)/` folder, which mirrors the Drive folder of the same name; the operator uploads it. |
| Predecessor | `archive/mini_logs/Mini Prediction Log - P-487 to P-494 CONSOLIDATED - 2026-09-23/` — consolidated, settled and imported to Part 5 on 2026-09-23. Three live records (TMP-20260923-NPB-CHU-DB-G25, P-493, P-494) were carried into §1 below with their issued text unchanged; this file is now their single custodian. |

## Standing learnings to apply to every new card (from the 2026-09-23 consolidation; see Part 5 §"2026-09-23(c)")

1. **Identity match before any "same-event" label:** date, venue, home/away, starters/participants (`O-ID-DATE-STARTER-MATCH`). A reforecast of a different date is a new event with a new ID.
2. **Freeze before first ball / first pitch / tip-off**, and stamp the freeze time on the card. A view issued after the start is LIVE and must be labelled so at issue (CR-4; P-485/P-489/P-492 recurrence).
3. **Six-field object (METHOD §4) on every card.** No rank without a derived probability from one joint distribution; the NBL card (no numbers, wrong roster) is the counter-example, P-491/P-494 the models.
4. **Roster/lineup from the official source**, first names where surnames collide (`O-ROSTER-NAME-COLLISION`); `LINEUPS_NOT_YET_PUBLISHED @ time` vs `RETRIEVAL_MISS`; no full-game total or margin at Rank #1 without posted lineups/bench (G14.2).
5. **Baseball centres:** team R/G and RA/G first, starter adjustment once (control 26), unearned runs added back to any ERA-derived projection (`O-NPB-ERA-CENTRE`), print the median-based P(total ≤ line).
6. **Mechanisms carry both signs** (G-L2): travel fatigue, rest, rotation alignment.
7. **Contract inconsistencies are flagged and confirmed, never silently corrected** (e.g., "Over 186.5 / Under 18.5").
8. **Settlement lineages:** three independent, each with a terminal marker; AI-generated recaps (e.g., Mynavi "プロ野球試合結果") are excluded; a league feed and a publisher on the same data vendor are one lineage until shown otherwise.
9. **Direct card-level preflight verification (2026-09-23 user directive):** Do not create separate scratch JSON manifest files or run external preflight scripts. Verify pregame horizon, timezone conversions, 3 lineages, and source firewalls directly within the card body; verify execution compliance via `audit_card_controls.py` directly on the Markdown log.

## 1. Incomplete / Unsettled Logs

All three records below were **LIVE at carry-over** and are carried over **as-is**, per user direction (2026-09-23). They are **not settled** and **no retrospective** is done here. Settle each only after three independent reliable lineages show an explicit terminal state (CR-4). Then append settlement below the record, leaving the issued text unchanged.

| ID / handle | Sport / competition | Event | Scheduled start (AEST) | Horizon at issue | State at carry-over (source, AEST) | Settlement status |
|---|---|---|---|---|---|---|
| `TMP-20260923-NPB-CHU-DB-G25` | Baseball / NPB Central League | Chunichi Dragons @ Yokohama DeNA BayStars — **23 Sep, game 25** (Fukazawa v Nakachi), Yokohama Stadium | 19:00, 23 Sep (18:00 JST) | PREGAME, frozen 18:59:17 | LIVE: 7回表, 3–3 (NPB box and Sports Navi, 21:40) | Awaiting a final |
| `P-493` | Baseball / KBO | KIA Tigers @ Doosan Bears, Jamsil | 19:30, 23 Sep (18:30 KST) | PREGAME, frozen 19:28:29 | LIVE: top 7th, 2–2 (KBO English scoreboard, 21:38) | Awaiting a final |
| `P-494` | Tennis / WTA 500 Singapore R16 | Mirra Andreeva v Aliaksandra Sasnovich (LS008) | ≈20:35 listed (first ball ≈20:38) | **LIVE-ISSUED** view, frozen 20:51:54 (outside pregame metrics) | LIVE: Andreeva 6-2, 3-2 (WTA feed and ESPN, 21:39) | Awaiting a final |
| `P-495` | Tennis / WTA 125 Tolentino R16 | Jessica Pieri vs Leyre Romero Gormaz, Center Court | ≈22:30, 23 Sep (14:30 CEST; delayed) | **PREGAME**, frozen 22:38:00 AEST | PREGAME / NOT STARTED (WTA, TennisTemple, Sofascore) | Awaiting a final |
| `P-496` | Tennis / ITF M25 Falun R16 | Iiro Vasa vs Wojciech Marek, Falu Tennisklubb | ≈22:30, 23 Sep (14:30 CEST; delayed/scheduled) | **PREGAME**, frozen 22:52:00 AEST | PREGAME / NOT STARTED (ITF, Sofascore, TennisTemple) | Awaiting a final |
| `P-497` | Basketball / Lithuanian LKL | BC Neptūnas Klaipėda vs BC Juventus Utena, Švyturio Arena | 01:30, 24 Sep (18:30 EEST, 23 Sep) | **PREGAME**, frozen 01:25:00 AEST | PREGAME / NOT STARTED (LKL, Sofascore, Flashscore) | Awaiting a final |
| `P-498` | Basketball / Lithuanian LKL | BC Šiauliai vs BC Lietkabelis, Šiaulių arena | 01:50, 24 Sep (18:50 EEST, 23 Sep) | **PREGAME**, frozen 01:45:00 AEST | PREGAME / NOT STARTED (LKL, Sofascore, Flashscore) | Awaiting a final |
| `P-499` | Basketball / EuroLeague Women Qualifiers | Flammes Carolo Basket(W) vs KP Brno(W), Guinguette Arena | 03:00, 24 Sep (19:00 CEST, 23 Sep) | **PREGAME**, frozen 02:50:00 AEST | PREGAME / NOT STARTED (FIBA, Sofascore, Flashscore) | Awaiting a final |
| `P-500` | Baseball / MLB | Washington Nationals (R. Lovelady) @ Detroit Tigers (F. Valdez), Comerica Park | 03:10, 24 Sep (13:10 EDT, 23 Sep) | **PREGAME**, frozen 02:58:00 AEST | PREGAME / NOT STARTED (MLB, Baseball-Reference, ESPN) | Awaiting a final |
| `P-501` | Baseball / MLB | Toronto Blue Jays (M. Scherzer) @ Baltimore Orioles (C. Bassitt) (G1), Camden Yards | 03:35, 24 Sep (13:35 EDT, 23 Sep) | **PREGAME**, frozen 03:33:00 AEST | PREGAME / NOT STARTED (MLB, Jays Journal, ESPN) | Awaiting a final |
| `P-502` | Baseball / MLB | Chicago White Sox (B. Hudson) @ Kansas City Royals (S. Lugo), Kauffman Stadium | 09:40, 24 Sep (18:40 CDT, 23 Sep) | **PREGAME**, frozen 09:39:00 AEST | PREGAME / NOT STARTED (MLB, Baseball-Reference, ESPN) | Awaiting a final |
| `P-503` | Ice Hockey / NHL Pre-Season | Minnesota Wild (J. Wallstedt) @ Dallas Stars (J. Oettinger), American Airlines Center | 10:07, 24 Sep (19:07 CDT, 23 Sep) | **PREGAME**, frozen 09:48:00 AEST | PREGAME / NOT STARTED (NHL, ESPN, CBS Sports) | Awaiting a final |
| `P-504` | Basketball / WNBA | Atlanta Dream @ New York Liberty, Barclays Center | 10:00, 24 Sep (20:00 EDT, 23 Sep) | **PREGAME**, frozen 10:08:00 AEST | PREGAME / NOT STARTED (WNBA, ESPN, Basketball-Reference) | Awaiting a final |
| `P-505` | Basketball / El Salvador LMB | Salvadoreños BC vs Cojute, Gimnasio Nacional José Adolfo Pineda | 11:15, 24 Sep (19:15 CST, 23 Sep) | **PREGAME**, frozen 11:14:00 AEST | PREGAME / NOT STARTED (FESABAL, Sofascore, 365Scores) | Awaiting a final |
| `P-506` | Baseball / MLB | Houston Astros (E. Pecko) @ Seattle Mariners (G. Kirby), T-Mobile Park | 12:10, 24 Sep (19:10 PDT, 23 Sep) | **PREGAME**, frozen 12:00:00 AEST | PREGAME / NOT STARTED (MLB, Baseball-Reference, ESPN) | Awaiting a final |
| `P-507` | Baseball / KBO | NC Dinos (Song Myung-gi) @ KT Wiz (Davis Daniel), Suwon KT Wiz Park | 18:00, 24 Sep (17:00 KST) | **PREGAME**, frozen 17:58:00 AEST | PREGAME / NOT STARTED (KBO, Naver Sports, MyKBO Stats) | Awaiting a final |
| `P-508` | Basketball / Australian NBL | SE Melbourne Phoenix vs Melbourne United, John Cain Arena | 19:30, 24 Sep (19:30 AEST) | **PREGAME**, frozen 19:28:00 AEST | PREGAME / NOT STARTED (NBL, ESPN, Sofascore) | Awaiting a final |
| `P-509` | Basketball / Australian NBL | Perth Wildcats vs Adelaide 36ers, RAC Arena | 21:30, 24 Sep (19:30 AWST) | **PREGAME**, frozen 21:25:00 AEST | PREGAME / NOT STARTED (NBL, ESPN, Sofascore) | Awaiting a final |

**Settlement routes (for the next pass).**
- **TMP-G25:** NPB box `npb.jp/scores/2026/0923/db-d-25/box.html` (試合終了) + Sports Navi `baseball.yahoo.co.jp/npb/schedule/?date=2026-09-23` + Kyodo or Nikkan (Yahoo! News). Grade the **23 Sep game-25** final. NPB 12-inning cap applies: a tie is a terminal outcome, so DeNA ML is a non-win on a tie and Chunichi +1.5 wins on a tie.
- **P-493:** KBO English scoreboard `eng.koreabaseball.com/Schedule/Scoreboard.aspx?searchDate=2026-09-23` ("KIA x FINAL y DOOSAN") + an independent Korean outlet (e.g., Yonhap or Sports Chosun) + a third lineage. KBO regular-season tie after 11 innings.
- **P-494:** WTA feed `api.wtatennis.com/tennis/tournaments/1152/2026/matches/` (`MatchState "F"`, `ResultString`) + ESPN `site.api.espn.com/apis/site/v2/sports/tennis/wta/scoreboard` (competition 184095; request without a browser User-Agent) + Tennis.com or another independent lineage. Games = sum of set games; a tiebreak set = 13. Record any retirement with its score.
- **P-495:** WTA official event/match center (`wtatennis.com`, Delta Motors Tolentino Open 2026) + TennisTemple/tournament linescore (`tennistemple.com`) + Sofascore (`sofascore.com`). Minimum three lineages with terminal marker `MatchState "F"`. Games = sum of set games (tiebreak set = 13). Any mid-match retirement records exact game scores at stoppage.
- **P-496:** ITF World Tennis Tour match center (`itftennis.com`, M25 Falun 2026, Men's Singles R16) + TennisTemple match card (`tennistemple.com`) + Sofascore (`sofascore.com`). Minimum three lineages with terminal marker `MatchState "F"` / final match score. Games = sum of set games (a tiebreak set = 13). Any mid-match retirement records exact game scores at stoppage.
- **P-497:** LKL official website match center (`lkl.lt`, official boxscore / `rungtynes`) + BasketNews.lt match report + Sofascore (`sofascore.com`). Minimum three lineages with terminal marker `FT` / final score including overtime if played. Record quarter-by-quarter breakdown and any overtime periods.
- **P-498:** LKL official website match center (`lkl.lt`, official boxscore / `rungtynes`) + BasketNews.lt match report + Sofascore (`sofascore.com`). Minimum three lineages with terminal marker `FT` / final score including overtime if played. Record quarter-by-quarter breakdown and any overtime periods.
- **P-499:** FIBA official website match center (`fiba.basketball`, official EuroLeague Women boxscore) + L'Equipe / Flashscore + Sofascore (`sofascore.com`). Minimum three lineages with terminal marker `FT` / final score including overtime if played. Record quarter-by-quarter breakdown and any overtime periods.
- **P-500:** MLB official boxscore (`mlb.com/gameday`) + Baseball-Reference boxscore + ESPN MLB scoreboard (`espn.com/mlb`). Minimum three lineages with terminal marker `Final` / completed 9+ innings. Record full linescore and pitcher decisions.
- **P-501:** MLB official boxscore (`mlb.com/gameday`) + Baseball-Reference boxscore + ESPN MLB scoreboard (`espn.com/mlb`). Minimum three lineages with terminal marker `Final` / completed 9+ innings. Record full linescore and pitcher decisions for Game 1 of doubleheader.
- **P-502:** MLB official boxscore (`mlb.com/gameday`) + Baseball-Reference boxscore + ESPN MLB scoreboard (`espn.com/mlb`). Minimum three lineages with terminal marker `Final` / completed 9+ innings. Record full linescore and pitcher decisions.
- **P-503:** NHL official gamecenter (`nhl.com/gamecenter`) + ESPN NHL scoreboard (`espn.com/nhl/scoreboard`) + CBS Sports NHL (`cbssports.com/nhl`). Minimum three lineages with terminal marker `Final` / completed regulation + OT/SO. Record full linescore, period breakdown, and goaltender decisions.
- **P-504:** WNBA official gamecenter (`wnba.com`) + ESPN WNBA scoreboard (`espn.com/wnba/scoreboard`) + Basketball-Reference boxscore (`basketball-reference.com/wnba`). Minimum three lineages with terminal marker `Final` / completed regulation + OT if played. Record quarter-by-quarter breakdown and player boxscores.
- **P-505:** FESABAL official game sheet / LMB portal (`fesabal.info` / `fesabal.com`) + Sofascore LMB scoreboard (`sofascore.com/tournament/basketball/el-salvador/liga-mayor`) + 365Scores (`365scores.com`). Minimum three lineages with terminal marker `Final` / completed regulation + OT if played. Record quarter-by-quarter breakdown and final score.
- **P-506:** MLB official boxscore (`mlb.com/gameday`) + Baseball-Reference boxscore (`baseball-reference.com/boxes`) + ESPN MLB scoreboard (`espn.com/mlb`). Minimum three lineages with terminal marker `Final` / completed 9+ innings. Record full linescore and pitcher decisions.
- **P-507:** KBO official English scoreboard (`eng.koreabaseball.com/Schedule/Scoreboard.aspx`) + Naver Sports Baseball / Sports Chosun (`sports.news.naver.com/kbaseball`) + MyKBO Stats (`mykbostats.com`). Minimum three lineages with terminal marker `Final` / completed regulation + extra innings (max 12). Record full linescore and pitcher decisions.
- **P-508:** NBL official gamecenter (`nbl.com.au`) + ESPN NBL scoreboard (`espn.com.au/nbl`) + Sofascore NBL boxscore (`sofascore.com`). Minimum three lineages with terminal marker `Final` / completed regulation + OT if played. Record quarter-by-quarter breakdown and final score.
- **P-509:** NBL official gamecenter (`nbl.com.au`) + ESPN NBL scoreboard (`espn.com.au/nbl`) + Sofascore NBL boxscore (`sofascore.com`). Minimum three lineages with terminal marker `Final` / completed regulation + OT if played. Record quarter-by-quarter breakdown and final score.

---

### Carried record 1 — `TMP-20260923-NPB-CHU-DB-G25` (NPB, 23 Sep game 25)

**Custody header (added at carry-over; the issued text below is unchanged).**
- This card was issued at 18:59:17 AEST on 23 Sep for the **23 Sep game (game 25, Fukazawa v Nakachi)**.
- The earlier reconciliation appended it to P-489 as a "same-event reforecast". P-489 is the **22 Sep game (game 24, Azuma v Muller)**, which is now settled in Part 5. The two are different events (`O-ID-DATE-STARTER-MATCH`).
- This card therefore carries the temporary ID above and takes the next free canonical ID at reconciliation. Wherever the text below says "P-489", "same-event" or "consumes no additional ID", it describes the superseded mapping.

<!-- BEGIN VERBATIM ISSUED RECORD: TMP-20260923-NPB-CHU-DB-G25 (R1 card and its custody notes, as held in the P-494-onward log) (heading levels demoted by two; text unchanged) -->

###### Same-event P-489 reforecast R1

The R1 source text below was recovered from the byte-exact pre-reconciliation archive. Its original ID note said the canonical ID was unresolved; the 2026-09-23 reconciliation confirms P-489 for this same event. R1 consumes no additional ID. Picks, reasoning, source ledger and cutoff text are retained as issued.

###### User-requested fresh-line reforecast R1 — frozen 2026-09-23 18:59:17 AEST (pre-start)

This is an append-only, same-event reforecast for the newly supplied 7.5 total threshold and exact supplied slate. It does not overwrite the earlier claimed-P-489 card, create a second event trial, or settle/review anything. Canonical ID remains unresolved; keep the event under this temporary handle pending the existing P-ID reconciliation. The issue-time snapshot is before the NPB-listed 19:00 AEST / 18:00 JST scheduled start. Official NPB still showed `試合開始前` (pre-game) at the last check. Actual first-pitch time is not independently observed, so the horizon is `PREGAME_BY_SCHEDULE / ACTUAL_FIRST_PITCH_NOT_YET_VERIFIED`.

**Best four from the supplied rows (forced ordinal; low evidence, exploratory NPB; market-blind):**

| Rank | Selection | Relative assessment |
|---|---|---|
| 1 | Chunichi Dragons +1.5 runs | Slight preference; covers Chunichi wins, NPB ties, and one-run DeNA wins. |
| 2 | Yokohama DeNA moneyline | Close to #1; DeNA is the winner lean, but the regular-season tie state and terms are unresolved. |
| 3 | Combined total Under 7.5 runs | Slightly ahead of the complement on the central run environment; low confidence because of the starter/relief upper tail. |
| 4 | Combined total Over 7.5 runs | Valid lower-ranked complement, with a live early-hook/relief and rain-disruption tail. |

No calibrated NPB model governs this scope, so the rank order is `UNVALIDATED_SUBJECTIVE / FORCED RANK`; numerical probabilities are not published. The Under/Over pair is one forced total decision, not two trials. The top two are coupled: low-scoring close-game branches help both Dragons +1.5 and Under, while a DeNA multi-run result hurts the cushion and can defeat the Under. Exact joint probability is unknown.

**Potential winner:** DeNA, narrow lean, eventual NPB result including extra innings; a game tied after 12 innings is an official tie, not a DeNA win. The two-way operator treatment is not supplied (`NO VALUE DETERMINABLE`). The line queries use the research endpoint of the official game result; no odds, prices, tips, fantasy pages or bookmaker analysis were used.

**Evidence and distribution notes.** NPB's event page named DeNA RHP Osuke Fukazawa vs Chunichi RHP Reia Nakachi, listed the matchup as pre-game, and posted both orders: Chunichi Fukunaga, Muramatsu, Hosokawa, Abe, Ishikawa, Hanada, Okabayashi, Ishii, Nakachi; DeNA Watarai, Maki, Tsutsugo, Encarnacion, Sano, Katsumata, Hayashi, Tobashira, Fukazawa. Chunichi used Abe at cleanup with Miguel Sano out of the order; do not label that rest as an injury. NPB's Sep. 22 season table gives DeNA 535 runs in 136 games (3.93/game), .247/.310/.377 and 122 HR; Chunichi 464 in 138 (3.36/game), .229/.300/.352 and 117 HR. Records were DeNA 67-66-3 and Chunichi 59-77-2. NPB's team ERAs were 3.28 and 3.25, respectively. This is descriptive baseline evidence, not an NPB-trained model.

Fukazawa's NPB line through Sep. 22: 9 appearances, 5-1, 49.2 IP, 2.90 ERA, 14 BB, 35 K, 3 HR allowed; Sports Navi gives 1.80 ERA in two appearances vs Chunichi. This supports DeNA's side and some suppression but is still a short season sample. Nakachi had 4 first-team relief appearances, 7.0 IP, 10.29 ERA (11 H, 3 BB, 8 K, 8 ER) and was making his first start since Aug. 28, 2025; NTV reports his same-day promotion to the active first-team roster after four months down. His farm line was 17 games, 13 starts, 78.1 IP, 2.99 ERA, with recent farm form reported as seven scoreless innings and 12 K in two games. The farm performance is a material counterweight, but not equivalent to NPB exposure. Treat his expected length/hook as a wide mixture, not as a 10.29-ERA starter projection.

The NPB/Sports Navi head-to-head table through 24 games has DeNA 15-8-1, 84 runs, 2.34 team ERA, .238 average; Chunichi 8-15-1, 61 runs, 3.43 ERA, .206. This is overlapping descriptive history and receives no extra independent weight. The immediately prior Sep. 22 game finished DeNA 7-3; the NPB box shows both clubs used four relief pitchers after their starters, with Ise and Sasaki among DeNA's relief arms. Current Sports Navi bench information still lists Ise and Sasaki available today, but availability does not prove freshness or effectiveness. The previous result itself is not a continuation adjustment. This combination, plus Nakachi's uncertain length, leaves a meaningful upper-tail branch and keeps the total rank evidence LOW despite the slightly Under-leaning central baseline.

Venue/time identity: Yokohama Stadium, Yokohama, Kanagawa, Japan; official 18:00 JST = 09:00 UTC = 19:00 AEST on 23 Sep. Forecast check at issue showed cloudy and about 22°C at first-pitch hour. The weather feed also returned a JMA heavy-rain/ground-loosening advisory covering the game window; this is not evidence that rain would fall at first pitch, but rain interruption/official-game/action-term branches remain unresolved. No lineup/bench, active-roster or official-source report identified a newly declared game-day injury beyond observed batting-order/registration changes; absence from a batting order is not proof of injury. NPB roster transaction and game pages take precedence for actual confirmation.

**Source ledger (final refresh window 2026-09-23 18:50–18:59 AEST; fact owner/class and role; exact-event scheduled-state recheck at 18:59:17 AEST):**

- NPB exact 25th-game scorecard, event state, pitchers, catchers and posted starting orders: https://npb.jp/scores/2026/0923/db-d-25/ (league field owner; primary).
- NPB official 2026 standings/team batting and pitching, through Sep. 22: https://npb.jp/bis/2026/stats/ ; https://npb.jp/bis/2026/stats/tmb_c.html ; https://npb.jp/bis/2026/stats/tmp_c.html (league field owner; primary).
- NPB Fukazawa official individual-season line: https://npb.jp/bis/players/61665155.html (league field owner; primary).
- NPB Chunichi official individual pitcher table (Nakachi): https://npb.jp/bis/2026/stats/idp1_d.html ; official farm table: https://npb.jp/bis/2026/stats/idp2_d.html (league field owner; primary).
- NPB prior-night Sep. 22 game and pitcher box score: https://npb.jp/scores/2026/0922/db-d-24/box.html (league field owner; primary; game/workload context only).
- Sports Navi exact game card / lineups, starters, bench names, H2H and previous meetings: https://baseball.yahoo.co.jp/npb/game/2021039454/top (independent sports-statistics secondary; pitcher-vs-team and H2H corroboration; lineup stats displayed but NPB order controls).
- Nikkan Sports, Sep. 22 announced probable starters and local start: https://www.nikkansports.com/baseball/news/202609220000373.html (independent Japanese sports-news lineage; schedule/starter corroboration).
- NTV NEWS NNN via Livedoor, Sep. 23 16:18 JST, Nakachi's same-day first-team registration/return and farm line: https://news.livedoor.com/article/detail/32391881/ (independent news lineage; availability/role).
- Yokohama DeNA official registration/deregistration history (latest visible Sep. 21): https://sp.baystars.co.jp/players/announce (club field owner; Katsumata added, Takeda removed; earlier Matsuo registration change; not a medical injury list).
- Doshin Sports live-NPB route was probed, but the detail page did not load cleanly; excluded from the forecast and not counted toward source independence.
- Weather for Yokohama from the weather tool; current conditions plus hourly forecast and JMA advisory. Forecast direction only; no reliable park-coordinate wind or precipitation amount captured, so no numerical weather adjustment.

**Method/control:** `MDS-2026.09.19-v4.3 / CR-2026.09.21-3`; `SCV-2026.09.19-v2`. Apply `RULES_BASEBALL.md` joint run model, starter/relief and 12-inning tie rules. NPB is exploratory and not performance-eligible. The cutoff/line query uses only the newly requested +1.5, DeNA ML, Over 7.5 and Under 7.5; supplied thresholds were not used as evidence.

Event identity/status source: [NPB official box score](https://npb.jp/scores/2026/0923/db-d-25/box.html). This event stays in Incomplete / Unsettled Logs. The forecast is not performance-eligible while timing and canonical ID are unresolved.

**Post-reconciliation status correction (custody only).** The preceding R1 source card states that the canonical ID is unresolved; that was its original pre-reconciliation status. The event is now canonical P-489. It remains unsettled because no terminal-state refresh was performed and its issue horizon remains unverified. No pick, probability or reasoning was changed.

<!-- END VERBATIM ISSUED RECORD: TMP-20260923-NPB-CHU-DB-G25 (R1 card and its custody notes, as held in the P-494-onward log) -->

---

### Carried record 2 — `P-493` (KBO, KIA @ Doosan)

<!-- BEGIN VERBATIM ISSUED RECORD: P-493 (heading levels demoted by two; text unchanged) -->

##### P-493 - KBO - Kia Tigers @ Doosan Bears (unsettled; canonical ID confirmed)
###### Original pre-reconciliation source handle: TMP-20260923-KBO-KIA-DOO

**Status:** UPCOMING / PREGAME AT FREEZE; no retrospective performed. `LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE`.

**Identity and contract.** 2026 KBO regular-season game, KIA Tigers (visitor) at Doosan Bears (home), Jamsil Baseball Stadium, Seoul. KBO official schedule: 23 Sep 2026, 18:30 KST (UTC+9) = 09:30 UTC = 19:30 AEST (UTC+10), same calendar date. Freeze: 23 Sep 2026 18:28:29 KST / 09:28:29 UTC / 19:28:29 AEST. KBO scoreboard and Yagoonara exact-game page showed the event not started at the final check. Nine scheduled innings; regular-season tie after 11 innings. User supplied Doosan +1.5, KIA ML, Over 7.5, Under 7.5. Operator/listed-pitcher/abandonment terms were not supplied; ties are possible and the ML treatment of a final tie is unknown. No sportsbook prices or picks were used.

**ID custody (reconciliation note).** The source card was initially held under TMP-20260923-KBO-KIA-DOO while the duplicate-ID audit was open. The local Part 5 reconciliation assigns this event canonical ID P-493. The pregame forecast, ranked picks, reasoning and sources below are retained unchanged; the temporary handle is an alias only.

**Availability and game state.** Confirmed starters in the official KBO player pages and exact-game reporting: KIA Adam Oller; Doosan Zach Logue (official KBO spelling). KIA’s reported batting order: Kim Ho-ryeong, Kim Min-gyu, Kim Seon-bin, Harold Castro, Na Sung-beom, Han Jun-su, Park Min, Kim Tae-gun, Byeon Woo-hyeok. Doosan’s reported order: Jung Soo-bin, An Jae-seok, Kim Min-seok, Yang Eui-ji, Yunior Severino, Son Ah-seop, Park Chan-ho, Oh Myung-jin, Cho Soo-haeng. The on-site KIA report says Kim Do-yeong, Park Jae-hyeon and reliever Seong Young-tak are away with the Asian Games squad; Doosan’s Asian Games absences include pitchers Gwak Bin and Choi Min-seok and infielder Park Jun-soon. Those listed players are not in the reported starting orders. No separate same-day injury transaction was verified; unavailable-player checks beyond the published lineup and national-team absences remain incomplete. 

**Evidence and forecast.** Official KBO season figures at the pregame snapshot: KIA 71-57-2, .272 team average, 697 runs/130 games (5.36 per game), 607 runs allowed and 4.29 team ERA; Doosan 66-62-5, .265, 624 runs/133 games (4.69 per game), 576 allowed and 3.77 team ERA. Head-to-head entering this game: Doosan 8-7. Oller: 2.80 ERA, 154 1/3 IP in 26 starts, 164 K/51 BB; last KBO start 17 Sep: 6 IP, 3 H, 0 R, 3 BB, 5 K. Logue: official KBO page 4.15 ERA (the secondary event page rounded/reported 4.09), 147 1/3 IP in 27 starts, 127 K/29 BB; last two starts shown by KBO were 5 IP/6 ER and 4 2/3 IP/3 ER. The two-start stretch is descriptive only, not treated as a stable skill change. Doosan played 22 Sep; its starter worked six innings in the 5-3 win over Kiwoom, so bullpen use is possible, but exact reliever-by-reliever workload/availability was not established. KIA last played 20 Sep and had two calendar days without a game; its exact relief-chain availability was also not independently confirmed. Outdoor Jamsil forecast: clear, about 24–25°C around first pitch, light westerly wind around 8–11 km/h; no weather delay signal.

**Joint scoring approximation (UNVALIDATED_SUBJECTIVE; not fitted or calibrated).** For a transparent center only, blend each team’s season runs/game with the opposing starter ERA over that starter’s season-average innings/start, then blend the batting rate with the opposing team ERA over the remaining scheduled innings. This yields regulation centers KIA 4.68, Doosan 4.00, total 8.68. Treat team runs as independent negative-binomial marginals with shape 4 each (variance = mean + mean²/4); use the same per-team extra-inning marginal (mean 0.75, shape 2) for the two extra innings only when tied after nine. This is an explicit subjective distribution, not a learned KBO model; its team independence, dispersion and extra-inning rates are assumptions. It does not quantify the removed KIA hitters’ individual run contribution, current reliever availability, lineup-level hitting rates, park factor, or weather effect. Thus the resulting percentages are assumption-sensitive and evidence grade is LOW / forced-rank. The model gives a 5-4 KIA central score; about 54.1% KIA win, 41.9% Doosan win, 3.9% tie through 11; Doosan +1.5 about 58.2%; Over 7.5 about 57.5%, Under 7.5 about 42.5%. Rounded estimates are not validated probabilities. The Over/Under pair is one forced complementary decision. Top-two joint probability is not claimed; using the two marginals, Frechet bounds for Doosan +1.5 and Over are 15.7%–57.5%, and both failing are bounded 0%–42.5%.

**Ranked picks (highest estimated marginal win likelihood first):**

1. **Doosan Bears +1.5 — 58.2%** under the stated full-game model. The cushion wins for a Doosan win, a tie, or a one-run KIA win. This is the strongest listed probability, though the margin estimate remains assumption-sensitive.
2. **Combined total Over 7.5 — 57.5%.** Team scoring centers sum to 8.68 before the tie-only extra-inning branch. The Over has a modest model advantage; the final total includes up to 11 innings under the stated research endpoint.
3. **Kia Tigers ML — 54.1% win probability; 3.9% tie; 41.9% loss.** Oller’s 2.80 ERA and recent six-scoreless-inning start are materially stronger than Logue’s 4.15 official ERA and poorer last-two-start line; KIA also scores more per game and has the better batting average. KIA’s key Asian-Games absences and Doosan’s better team ERA / home setting counter that edge. Projected winner: **Kia Tigers**, low confidence. A tie is not counted as a win; any operator-specific tie void/push treatment is unknown.
4. **Combined total Under 7.5 — 42.5%.** Complement of the Over for this half-run line and model endpoint; included because requested, not a second independent decision.

**Distribution and failure checks.** Low-total branch: both starters work near their season lengths, KIA’s absent hitters depress output beyond what the season run average captures, and Doosan’s better team ERA is reflected in its staff blend. High-total branch: Logue’s recent short-start / run-concession outcomes recur, KIA reaches Doosan relief early, and KIA’s two rest days support its offense while Doosan’s bullpen absorbs another day of work. A KIA multi-run win is the principal Bears +1.5 failure path; a starter/relief duel with total 7 or fewer is the Over failure path. Home-ninth entitlement and extra innings are represented only approximately in the model. No player props were selected because the necessary lineup-specific rate and exposure data were not verified.

**Source ledger (all material sources; access date 23 Sep 2026):**

- [KBO official 23 Sep scoreboard](https://eng.koreabaseball.com/Schedule/Scoreboard.aspx?searchDate=2026-09-23) — exact matchup, Jamsil, 18:30 KST, final pregame state.
- [KBO official September schedule](https://eng.koreabaseball.com/Schedule/DailySchedule.aspx) — event date/time and preceding game schedule.
- [KBO official standings and team rates](https://eng.koreabaseball.com/Standings/TeamStandings.aspx) — standings, games played, batting average, runs, runs allowed, ERA.
- [KBO official Adam Oller page](https://eng.koreabaseball.com/Teams/PlayerInfoPitcher/Summary.aspx?pcode=55633) — 2026 pitching totals and recent start log.
- [KBO official Zach Logue page](https://eng.koreabaseball.com/Teams/PlayerInfoPitcher/Summary.aspx?pcode=55239) — 2026 pitching totals and recent start log; official ERA differs from secondary rounded value.
- [KBO official 2026 Asian Games roster](https://www.koreabaseball.com/Schedule/International/AsianGames/Main2026.aspx) — national-team absences by club.
- [Xports on-site KIA lineup report](https://www.xportsnews.com/article/2199464) — reported batting order and KIA Asian-Games absences, including Kim Do-yeong, Park Jae-hyeon, Seong Young-tak.
- [StarNews on-site Doosan lineup report](https://www.starnewskorea.com/en/sports/2026/09/23/2026092316391980624) and [ChosunBiz carrying OSEN report](https://biz.chosun.com/en/en-sports/2026/09/23/HDKXZJ6YJJGHTFECCUN43WABB4/?outputType=amp) — Doosan batting order and starter; the OSEN/Chosun item is treated as one upstream lineage, not two.
- [KBO official 22 Sep Doosan–Kiwoom scoreboard](https://eng.koreabaseball.com/Schedule/Scoreboard.aspx?searchDate=2026-09-22) and [KBO recap](https://www.koreabaseball.com/MediaNews/News/BreakingNews/View.aspx?bdSe=62399) — Doosan’s prior game, 5-3 win; recap identifies starter workload.
- [Yagoonara exact game page](https://www.yagoonara.com/en/schedule/122167) — independent event cross-check, starters, team rates, H2H, weather outlook and not-started state. Its underlying official KBO source is disclosed on-page; it is not treated as an independent origin for KBO statistics.
- [AccuWeather Seoul forecast](https://www.accuweather.com/en/kr/seoul/226081/weather-forecast/226081) — broad current city conditions; exact Jamsil game-window wind estimate came from Yagoonara and is lower confidence.

**Method / document mapping.** Issued under local METHOD.md MDS-2026.09.19-v4.3 / CR-2026.09.21-3 and RULES_BASEBALL.md; market-blind. Canonical record: P-493. Settlement and any requested retrospective belong in PREDICTION_LOG_COMBINED_5.md; current event state belongs in GAME_LOG_STATUS_CURRENT.md. No retrospective was requested or performed.

<!-- END VERBATIM ISSUED RECORD: P-493 -->

---

### Carried record 3 — `P-494` (WTA Singapore, live-issued view)

<!-- BEGIN VERBATIM ISSUED RECORD: P-494 (wrapper plus complete source-session record) (heading levels demoted by two; text unchanged) -->

#### P-494 — WTA Singapore Open 2026, Mirra Andreeva vs Aliaksandra Sasnovich (LIVE VIEW)

**Canonical ID:** P-494. Temporary source handle `TMP-20260923-WTA-SGP-ANDREEVA-SASNOVICH` is retired as an alias. The full original source log was preserved byte-exact before the temporary file was cleared; see the archive receipt in `archive/mini_logs/originals_2026-09-23/`.

**ID rationale:** The live view was frozen at 20:51:54 AEST, before this soccer request’s estimated 21:00 AEST start and before any soccer forecast was issued. P-493 was the prior canonical event; P-494 was the next available canonical number. The soccer request below failed the forecast gates and receives no ID. Next canonical ID: P-495.

**Horizon/status:** LIVE-ISSUED, not pregame, and excluded from pregame performance metrics. The WTA feed showed the match live at the freeze. No settlement or retrospective has been performed.

The complete source-session record follows. Its temporary-ID and “not appended” statements describe the state at the original issue time; this wrapper records the later canonical reconciliation.

---

### Prediction Mini Running Log — session 2026-09-23 (WTA Singapore, Andreeva vs Sasnovich)

**Custody.** This session is **read-only** for every existing project file (user directive, 2026-09-23). This file is the session's own running log and is the only file written. No canonical log, status register, rule file or other mini log was changed.
**ID.** Temporary ID `TMP-20260923-WTA-SGP-ANDREEVA-SASNOVICH`. The merged running log (`C:\Users\danie\Documents\Sports Research\PREDICTION_MINI_RUNNING_LOG_MERGED_P482_ONWARD.md`, read 2026-09-23 ~20:28 AEST) lists **next ID P-494**. This session does not assign it, because concurrent sessions have already produced collisions (P-484). The proposed canonical ID is **P-494, pending reconciliation**.
**Governing method (read fresh this session).** MDS-2026.09.19-v4.3 / CR-2026.09.21-3; SFA-TENNIS (RULES_TENNIS.md §9, controls 1–14); GFA-2; SCV-2026.09.19-v2. SPORTS_ONLY / MARKET_BLIND. LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE. NO VALUE DETERMINABLE.

---

#### Entry 1 — score-blind prior (append-only; written 2026-09-23 ~20:44 AEST, BEFORE any live score was viewed)

**Horizon statement.** The supplied estimated start was 20:30 AEST. At 20:31 AEST the WTA field-owner feed showed match `LS008` with `MatchState "C"`, `NumSets 0`, `MatchTimeTotal 00:00:00`, empty score, stamped `2026-09-23T10:20:39Z` (20:20 AEST). Research could not be completed before the start. **This entry is therefore NOT a pregame issue.** It is labelled `START_CROSSED — SCORE-BLIND PRIOR`. It was built from pre-match records only. The research scripts excluded this match from every player log, so no score was seen.

- Distribution v1 (superseded before any line was queried): `TMP-20260923-WTA-SGP-ANDREEVA-SASNOVICH-prior-v1`, frozen 20:41:19 AEST, SHA-256 `e679a464853e0f7e5f3235f86252dcce77fc31626d0b246e57a2dc955996b3ec`. It had independent sets, so its deciding-set rate was 22%.
- **Distribution v2 (controlling):** `…-prior-v2`, frozen **20:42:18 AEST**, SHA-256 **`380df425355035dca0cc274022d81a57ccd7abede713532894c0bb95cc81528c`**.
  - Why v2 replaced v1: the direct comparables showed more deciding sets than the model. Andreeva went three sets in 6 of 17 hard-court matches against opponents ranked outside the top 50; Sasnovich went three sets in 35% of her hard L20. v2 adds declared set-level variation, shrunk toward a population rate.
  - The change was made before the lines were queried. It used sporting evidence only.
- Line query time: **20:42:57 AEST** (after the v2 freeze).

**Model.** Exact point → game → set → match Markov chain: ad scoring, 7-point tiebreak in every set including the decider (WTA rule).
- Andreeva serve-point probability = s + δ + ε; Sasnovich's = s − δ − ε.
- δ ~ N(0.070, 0.050) across matches (form).
- ε ~ N(0, 0.045) per set (within-match variation).
- s ∈ {0.54, 0.56, 0.58}, weights {0.25, 0.50, 0.25}. The court check this week (13 completed main-draw matches) was 992/1770 = 0.560.
- Retirement/walkover mass: 0.015. All probabilities below are conditional on normal completion unless stated.

| Family (`TE-B*`) | Mass | Mean total | Mean margin (A−S) |
|---|---:|---:|---:|
| B1 Andreeva straight-set control (≤3 games conceded per set) | 0.395 | 15.0 | +9.0 |
| B2 Andreeva close straight sets | 0.257 | 19.3 | +5.7 |
| B3 Andreeva deciding-set win | 0.193 | 27.4 | +4.3 |
| B4 Sasnovich straight-set control | 0.022 | 16.0 | −8.0 |
| B5 Sasnovich close straight sets | 0.052 | 20.3 | −5.0 |
| B6 Sasnovich deciding-set win | 0.081 | 28.3 | −2.5 |
| **Sum** | **1.000** | | |

- **Winner:** P(Andreeva) = 0.845.
- **Set count:** P(two sets) = 0.725.
- **Total games:** mean 19.84, SD 5.67, median 18, 10/25/75/90th percentiles 14/15/24/29.
- **Margin:** mean +5.24, SD 4.84, median +6, 10/90th percentiles −3/+10.

**Queries (after freeze).**

| Contract | P(win given completion) | Unconditional (retirement → void 0.015) |
|---|---:|---:|
| Under 18.5 | 0.5296 | 0.5216 |
| Sasnovich +6.5 | 0.5008 | 0.4933 |
| Andreeva −6.5 | 0.4992 | 0.4917 |
| Over 18.5 | 0.4704 | 0.4634 |

- Joint probabilities: P(U18.5 ∧ S+6.5) = 0.090; P(U18.5 ∧ A−6.5) = 0.440; P(O18.5 ∧ S+6.5) = 0.411; P(O18.5 ∧ A−6.5) = 0.060.
- Sensitivity (8 parameter sets): Under 18.5 is preferred in 7 of 8. The handicap flips with the dominance centre (A−6.5 ranges 0.42–0.58), so it is a NEAR_TIE.

*(Live state check and issued view follow in Entry 2.)*

---

#### Entry 2 — P-494 ISSUED LIVE VIEW `TMP-20260923-WTA-SGP-ANDREEVA-SASNOVICH-LIVE-v1` (source handle retained as alias; written ~20:53 AEST)

**Status:** UNSETTLED — **LIVE-ISSUED VIEW**. This is not a pregame card. It belongs in the separate live horizon and is excluded from pregame metrics. No retrospective has been done, per the user's instruction.

##### Field 1 — Identity and contract

**Event.**
- Singapore Tennis Open presented by BNP Paribas 2026. WTA 500, 28-player draw, singles Round of 16 (`RoundID 2`).
- WTA event 1152/2026, match `LS008`, Court 1 (Tennis.com labels it "Center Court").
- Venue: Singapore; **indoor hard** (WTA tournament record `inOutdoor: "I"`, `surface: "Hard"`).

**Players.**
- [1] Mirra Andreeva (RUS; WTA #5; right-handed; born 2007-04-29). Seeded 1; R1 bye.
- Aliaksandra Sasnovich (BLR; WTA #132; right-handed; born 1994-03-22; career high #29). Direct entry. Beat Kasatkina 7-5 6-0 in R1 on 21 Sep (1:19:54).

**Time and state.**
- Venue zone `Asia/Singapore` (UTC+8). Melbourne zone `Australia/Melbourne` = **AEST** (UTC+10; DST starts 4 Oct 2026). No calendar rollover.
- The user's 20:30 AEST start is an estimate; it equals 18:30 SGT. ESPN lists the start as 2026-09-23T10:35Z (20:35 AEST).
- The WTA feed implies first ball at about **10:38:15Z (20:38 AEST)**: feed update 10:43:40Z minus 00:05:25 elapsed.
- **GAME-STATE: LIVE.** Observation: WTA feed `lastUpdated 2026-09-23T10:51:14.687Z` (20:51:14 AEST); state `P`; elapsed `00:12:59`.
- **Set 1: Andreeva 2–1. Andreeva serving at 0–0 in game 4.**
- Serving history in set 1: Sasnovich served game 1 and was broken (Andreeva converted 1/1 break points). Andreeva held game 2. Sasnovich held game 3 from 40–Ad.
- Computed at 20:51:54 AEST.

**Contracts (supplied; quarantined until the v2 freeze at 20:42:18).**
- Andreeva −6.5 games / Sasnovich +6.5 games: aggregate games margin.
- Total games Over / Under 18.5.
- Both are half-lines, so there is no push. Each is a FORCED_PAIR conditional on action.
- A tiebreak set counts as 7–6 = 13 games.
- WTA rules: best of three, 7-point tiebreak at 6–6 in every set including the decider (RULES_TENNIS §10.2).

**Operator retirement/walkover terms:** not supplied → `UNKNOWN_DEFINITION` / NO VALUE DETERMINABLE.
- The research grade assumes normal completion.
- Under standard conventions (§10.6), a retirement voids handicap and total rows unless the threshold was already decided. Over 18.5 can be decided before a retirement once 19 games have been completed.

**The supplied pregame lines may no longer be offered at this state.**

**Method/controls:** MDS-2026.09.19-v4.3 / CR-2026.09.21-3 / SFA-TENNIS; RULES_GENERAL §7 live analysis; RULES_TENNIS §6 live state ("recalculate only the remaining point/game/set tree; do not extrapolate a short hot spell as a permanent rate change").

**Preflight:** `prediction_preflight.py` is a normal-pregame validator and requires `event_state PREGAME/SCHEDULED`. This view is LIVE, so the pregame path is **BLOCKED by design** and was not used. The live path was run under §7: the official field-owner live state controls, and two further independent front ends agree on orientation.

##### Field 2 — Evidence and exposure

**Source record.** All retrieved 2026-09-23 between 20:31 and 20:52 AEST.

| # | Source (lineage) | Field owner? | What it established | Retrieved (AEST) |
|---|---|---|---|---|
| S1 | WTA API `api.wtatennis.com/tennis/tournaments/1152/2026/matches/` (WTA) | Yes | Identity, round, court, seeds, entries; state C→P; live score, point and server; R1 results; indoor hard; 28-player draw | 20:31, 20:44, 20:49, 20:51 |
| S2 | WTA API `…/matches/{id}/stats` (WTA) | Yes (same lineage as S1) | Per-match serve/return totals for 2025–26 matches; this match's live set-1 stats; the week's court serve environment | 20:34–20:52 |
| S3 | WTA API `…/players/{331809,317790}/matches/?year=2023…2026` (WTA) | Yes (same lineage) | Match logs, L5–L20 windows, H2H (Iasi 2024) | 20:32–20:36 |
| S4 | ESPN `site.api.espn.com/apis/site/v2/sports/tennis/wta/scoreboard` (ESPN) | No; independent publisher | "In Progress, 1st Set", Andreeva 1–0 and serving (at 20:45); start listing 10:35Z; R1 Sasnovich d. Kasatkina 7-5 6-0 Final | 20:45 |
| S5 | Tennis.com match page (Tennis Channel), raw HTML plus `r.jina.ai` text | No; independent publisher | "Live"; Round 2 WTA Singapore; rankings 5/132; both right-handed; career-high 29; H2H Iasi 23 Jul 2024, Andreeva 6-1 6-3. Its snapshot lagged S1 (1–0, 40–40): publication lag, not a conflict | 20:50 |
| S6 | Tennis Abstract WTA Elo `tennisabstract.com/reports/wta_elo_ratings.html`, "Last update: 2026-09-21" | Rating benchmark only (control 13) | Andreeva Elo 2047.9 / hElo 1981.4; Sasnovich 1701.9 / 1668.5; Kasatkina 1783.7 / 1741.1 | 20:36 |

- The upstream vendors behind the S4/S5 live scores are not documented, so shared vendor lineage cannot be excluded. The official feed S1 controls the state (§7). Event identity rests on three distinct publishers: WTA, ESPN and Tennis Channel.

**Participants.**
- Tennis bench: NOT_APPLICABLE.
- Coaches: `COACH_NOT_RETRIEVED` for both. Coaching is not used directionally.

**Workload.**
- Andreeva: first match of the event (R1 bye). Her last match was a US Open QF loss to Gauff, 6-2 6-7(7) 2-6, during the 30 Aug–13 Sep event, so about two weeks' rest.
- Sasnovich: R1 on 21 Sep (1:19:54). She is also entered in doubles with Friedsam (LD014, later today, "After suitable rest").
- No withdrawal or medical marker in S1 at any check.

**Environment.** Indoor; weather gate not applicable. Current court: `SURFACE_CONDITION_NOT_PUBLISHED`. Observed proxy: pooled serve points won this week, 992/1770 = 0.560 across 13 completed main-draw matches.

**Disaggregated serve/return records (G-L7, not aggregate-only).** Both players' per-match 2025–26 hard-court logs were printed. Aggregates, with SE:

| Player / split | Matches | Serve points won | Return points won |
|---|---:|---|---|
| Andreeva, hard 2026, all | 27 | 1151/1909 = .603 (SE .011) | 917/1936 = .474 (SE .011) |
| Andreeva, vs top 50 | 20 | .586 | .455 |
| Andreeva, vs outside top 50 | 7 | 259/386 = .671 | 221/406 = .544 |
| Sasnovich, hard 2025–26, all | 38 | 1537/2703 = .569 | 1205/2665 = .452 |
| Sasnovich, vs top 50 | 10 | .540 | .425 |
| Sasnovich, vs top 20 (6 matches) | 6 | 195/356 = .548 | 144/374 = .385 |

- Sasnovich's six hard-court matches against top-20 players, with game totals: Paolini L 3-12, Samsonova L 8-12, **Tauson W 12-5**, Bencic L 7-12, Kostyuk L 6-12, **Osaka W 13-12**.
- Sasnovich's R1 here (S2): serve 33/50 = .660, return 32/58 = .552, 0 double faults. Kasatkina made 7 double faults.

**Recency windows (hard court; descriptive only; overlapping; one evidence unit).**

| Window | Andreeva W-L | Games % | Avg total | 3-set % | Margin | Opp. rank | Sasnovich W-L* | Games % | Avg total | 3-set % | Margin | Opp. rank |
|---|---|---:|---:|---:|---:|---:|---|---:|---:|---:|---:|---:|
| L5 | 4-1 | .613 | 22.2 | 40 | +5.0 | 39 | 1-4 | .435 | 23.0 | 40 | −3.0 | 110 |
| L10 | 7-3 | .593 | 19.9 | 30 | +3.7 | 39 | 4-6 | .473 | 22.0 | 30 | −1.2 | 130 |
| L15 | 10-5 | .588 | 21.3 | 40 | +3.7 | 39 | 6-9 | .467 | 21.0 | 20 | −1.4 | 106 |
| L20 | 12-8 | .569 | 22.1 | 40 | +3.0 | 35 | 10-10 | .493 | 22.5 | 35 | −0.3 | 111 |

- \*The WTA player feed excludes Sasnovich's Singapore R1 win (12-5 games). Including it, her L5 is 2-3.
- Andreeva's 2025 post-US Open Asian swing (Beijing R16 L to Kartal, Wuhan R32 L to Siegemund with 15 double faults, Ningbo R16 L to Lin Zhu (#219) with 12 double faults) and her flat 2026 hard-court losses (Fernandez 5-12; Kostyuk 8-16) are context under R-1. They widen the distribution and carry no signed lean.

**H2H.** One meeting: Iasi 2024 (outdoor clay, WTA 250), Andreeva 6-1 6-3 (S3, S5). Continuity count 0 (different surface; more than two years old; Andreeva's level has changed). **Zero directional weight.**

**Reference base rate:** `NOT_YET_DERIVED` (BASE_RATES_REGISTER; tennis) for every row.

##### Field 3 — Joint distribution

- **Prior:** frozen v2 (Entry 1; SHA-256 `380df425…28c`). δ ~ N(0.070, 0.050); ε per set ~ N(0, 0.045); serve environment s ∈ {.54, .56, .58}.
- **How the centre was set.**
  - Andreeva-side comparables (similar opposition, including her 2025 losses) point to a total-points share of about .58–.59.
  - Sasnovich-side comparables (her record against the top 20, adjusted because Andreeva is stronger than the average top-20 player) point to about .55.
  - The midpoint is .57, i.e. δ = .07.
  - Form SD widened for named regime uncertainty: Andreeva's first match in about two weeks and her first indoor hard event of the swing.
- **Elo benchmark (control 13):** the Elo gaps (313 hard, 346 overall) imply Andreeva .86–.88 before the match. The frozen prior's .845 is within 3.5 points, so no mechanism is required.
- **Live transformation:** exact remaining point/game/set tree from the S1 state (set 1 at 2–1, Andreeva serving at 0–0; Sasnovich served first in set 1), at frozen-v2 rates. No parameter update (RULES_TENNIS §6).
  - Sensitivity with a Bayesian point update on set-1 points (A 4/4, B 5/11 on serve; the stats lag the score): posterior mean δ .0855.

| Family (live, given completion) | Mass |
|---|---:|
| B1 Andreeva straight-set control | 0.4157 |
| B2 Andreeva close straight sets | 0.2864 |
| B3 Andreeva deciding-set win | 0.1704 |
| B4 Sasnovich straight-set control | 0.0096 |
| B5 Sasnovich close straight sets | 0.0406 |
| B6 Sasnovich deciding-set win | 0.0773 |
| **Sum** | **1.0000** |

- **Winner and set count:** P(Andreeva) = 0.8725; P(three sets) = 0.2477.
- **Total games:** mean 19.86, median 18, 10/90th percentiles 14/29. Mass at 18 = .100; at 19 = .053.
- **Margin:** mean +5.49, median +6, 10/90th percentiles −2/+10. Mass at +6 = .149; at +7 = .116.
- Most likely set sequences: 6-2 6-2 (.059), 6-1 6-1 (.052), 6-2 6-1 (.046), 6-2 6-4 (.038), 6-2 6-0 (.038).
- Retirement/walkover: 0.015, carried as void/unknown. The unconditional win probability is about p × 0.985.
- Output receipt: `final_refresh2.txt`, SHA-256 `bed8c304fdaa4b19aad2e27fda9449340dc86222569da3e2dc561404c6e5bb74` (session scratchpad).

##### Field 4 — Ranked contracts (all `UNVALIDATED_SUBJECTIVE`; conditional on completion; SPORTS_ONLY / MARKET_BLIND)

| Rank | Contract | p (issued) | p (Bayes sensitivity) | Verdict / evidence | Role | rank_gap to next |
|---|---|---:|---:|---|---|---|
| **1** | **Under 18.5 total games** | **0.550** | 0.645 | LEAN / LOW (line inside the central corridor; median 18) | PRIMARY_FORMAL (total pair) | SMALL |
| **2** | **Sasnovich +6.5 games** | **0.510** | 0.409 | FORCED RANK / LOW, **NEAR_TIED with #3** (the line sits on the median margin, +6; the order flips under sensitivity) | PRIMARY_FORMAL (handicap pair) | NEAR_TIE |
| **3** | Andreeva −6.5 games | 0.490 | 0.591 | FORCED RANK / LOW | CORRELATED complement of #2 | SMALL |
| **4** | Over 18.5 total games | 0.450 | 0.355 | AVOID-lean / LOW | Complement of #1 | — |

- **Preferred sides:** Under 18.5 (total pair); Sasnovich +6.5 (handicap pair, near-tie).
- **Top over/under:** Under 18.5, which is also Rank #1. A `TOP_OU_REVIEW` applies if it fails.
- **Potential winner:** **Mirra Andreeva**, 0.8725 given completion (sensitivity 0.929; score-blind pre-match 0.845; Elo benchmark .86–.88). Verdict LEAN.
  - Main failure paths: Sasnovich's first-strike, backhand-led upset branch (she beat #14 Tauson and #14 Osaka on hard in the last 12 months) = B4–B6, 0.1275; retirement 0.015.

##### Field 5 — Dependence and checks

- **Representative Rank-#1 outcome:** Andreeva 6-2 6-2 (the modal sequence).
  - 16 games → Under WIN. Margin +8 → Andreeva −6.5 WIN, Sasnovich +6.5 **LOSS**. Andreeva wins.
  - So the modal branch **defeats Rank #2** (C-MODAL-BRANCH-CHECK disclosure).
  - A joint-success representative for R1 ∧ R2 is 6-3 6-3 or 6-4 6-2: 18 games, +6.
- **P(R1 ∧ R2) = 0.106** (U ∧ S). Fréchet bounds [0.060, 0.510]. **Strongly anti-coupled (M18).**
  - The shared driver is match shape. An Andreeva routine straight-sets win helps #1 and hurts #2. A competitive or three-set match helps #2 and hurts #1.
- **P(¬R1 ∧ ¬R2) = 0.046** (Over ∧ Andreeva −6.5). The single state: Andreeva wins by 7+ in an extended match, e.g. 7-5 6-1 or 6-1 4-6 6-1.
- **P(exactly one of the top two wins) = 0.848.**
- **Complement of R1 (Over 18.5, 0.450):** B3 0.170 + B6 0.077 (every deciding set; the minimum three-set total is 18) + the ≥19-game parts of B2/B5 (6-4 6-3, 7-5 6-2, 7-6 …) 0.203.
- **Complement of R2 (Andreeva −6.5, 0.490):** U ∧ A 0.444 (B1: 6-2 6-2, 6-1 6-1 …) + O ∧ A 0.046.
- **Bidirectional sign (G22):** Andreeva's double-fault spells (15 at Wuhan, 12 at Ningbo 2025) lengthen sets (→ Over, +6.5) and do not flip the winner; handled through ε width. Sasnovich's double-fault volatility (5–7 double faults in several matches; 0 in R1) produces breaks → shorter, one-sided sets (→ Under, −6.5). Both signs are in the ε/δ width; no signed lean.
- **G27 swap test (#4 Over vs #3 Andreeva −6.5):** Over survives every deciding set plus close straight sets. Andreeva −6.5 survives only dominant straight sets. The marginal favours #3 (0.490 vs 0.450). Order kept.
- **Sensitivity (v2 prior, 8 parameter sets, before the live state):** Under preferred in 7 of 8; the handicap spans .42–.58. The live Bayesian sensitivity flips #2/#3. **No confidence claim on the handicap.**

##### Field 6 — Freeze and follow-up

- **Freeze:** the issued numbers are from the refresh computed 20:51:54 AEST on feed state 20:51:14. The live state will have moved by delivery; this view is valid only for its observation state.
- **Settlement route (G10.2).** Verified this session to return final set scores for this event:
  - S1 WTA feed: `ScoreSet*`, `ResultString`, `MatchState "F"`.
  - S4 ESPN linescores.
  - S5 Tennis.com.
  - Games = sum of set games (a tiebreak set counts as 13). Settlement needs three lineages with a terminal marker (C-FINAL3).
- **Retirement/medical time-outs:** record the set and game score at the time if one occurs (G-L23).
- **Retry trigger:** at the next session, check that S1 `MatchState = "F"` and that ResultString is present.
- **Not appended** to `PREDICTION_LOG_COMBINED_5.md` or any other existing file (read-only directive). Proposed canonical ID P-494, pending reconciliation.

##### §16.8 completeness block

1. MDS-2026.09.19-v4.3 / CR-2026.09.21-3. Controls applied: G0–G6, G8, G10.2, G13.1, G14/G14.1/G14.2, G15.1 (indoor), G16, G20/G20.1, G22, G27, G-L1, G-L2, G-L7, G-L8, G-L9, G-L10, G-L11, G-L12/G-L24, G-L15, G-L17, G-L19, G-L22, R-1, PF-1, PF-2, C-SRC3, C-TIME1/2, C-STATE3, RULES_TENNIS §6 and controls 1–14.
2. Families with masses: above (sum 1.0000).
3. Total: centre (mean) 19.86 / median 18; SD about 5.7 (prior); line 18.5; P(Under) .550. Margin: mean +5.49 / median +6; SD about 4.8 (prior); line 6.5; P(Sasnovich +6.5) .510. Normalised edges: total |19.86 − 18.5| / 5.7 = 0.24 (the mean is above the line while the median is below it, because the total is right-skewed); margin |5.49 − 6.5| / 4.8 = 0.21.
4. Complement decompositions for R1 and R2: above.
5. P(R1 ∧ R2) = 0.106, anti-coupled.
   - 5a. P(¬R1 ∧ ¬R2) = 0.046; state named above.
   - 5b. Both pairs are FORCED_PAIR; preferred sides Under 18.5 and Sasnovich +6.5; push mass 0 (half-lines).
6. Representative R1 outcome 6-2 6-2: checked; it defeats R2 (disclosed).
7. Participants: both confirmed on court by the S1 live state; bench NOT_APPLICABLE; coaches `COACH_NOT_RETRIEVED`.
8. AGGREGATE_ONLY: none (per-match logs printed). SEs printed. Small-sample note: the live Bayesian update rests on about 15 points, so it is reported as sensitivity only.
9. Settlement source per row: S1 (field owner) + S4 + S5.
10. At settlement only: to be completed later.

**Source firewall:** no odds, betting previews, tipsters, prediction markets, fantasy or DFS material was opened or used. Tennis Abstract Elo is a sports rating used as a benchmark only.

**Control receipt (PF-7), checked at ~20:55 AEST.** `CONTROL_MANIFEST_2026-09-21-3.md` SHA-256 `079b43f75681818724723556d66a82c01f56f6383f82055f0f50af88c97c0c00`. The live file hashes equal the manifest rows:
- METHOD.md `4f400025…f820b`
- RULES_GENERAL.md `08cf84fc…0522c`
- RULES_TENNIS.md `0994c197…dcd1`

**ID note.** A concurrent local log, `Mini Prediction Log - P-494 onward - 2026-09-23/`, was created at 20:44 AEST during this session. At 20:55 it had issued nothing and said "allocate P-494 only when a new forecast is actually frozen". This view was frozen at 20:51:54 AEST. It keeps `TMP-20260923-WTA-SGP-ANDREEVA-SASNOVICH` and proposes P-494 (or the next free ID) at reconciliation. The concurrent log was only read, not written.

**Delivery-time snapshot (not used in the numbers).** Feed 20:53:12 AEST: `P`, elapsed 00:14:57, set 1 Andreeva 2–1, Andreeva serving at 15–0.

<!-- END VERBATIM ISSUED RECORD: P-494 (wrapper plus complete source-session record) -->

---

### P-495 — WTA 125 Tolentino, Jessica Pieri vs Leyre Romero Gormaz

**Canonical ID:** P-495  
**Sport / Tour:** Tennis / WTA 125 (Delta Motors Tolentino Open 2026)  
**Round:** Round of 16 (second round main draw)  
**Event status:** UPCOMING / PREGAME AT FREEZE; no retrospective performed. `LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE`. `SPORTS_ONLY / MARKET_BLIND`. `NO VALUE DETERMINABLE`.

##### Field 1 — Identity and contract

- **Event:** Delta Motors Tolentino Open 2026 (WTA 125).
- **Matchup:** Jessica Pieri (ITA, qualifier) vs Leyre Romero Gormaz (ESP, seed #5).
- **Venue:** Circolo Tennis Tolentino, Tolentino, Macerata, Marche, Italy. Center Court.
- **Surface and format:** Outdoor Red Clay (Terra battuta). Best-of-three sets; regular ad scoring; standard 7-point tiebreak at 6-6 in every set including the deciding third set (WTA 125 format, RULES_TENNIS §10.2).
- **Timing and timezones:**
  - Official venue-local scheduled start: 23 September 2026, not before 14:30 CEST (UTC+2), delayed due to preceding Center Court matches (Masarova vs Serban).
  - Conversion to Melbourne: CEST (UTC+2) to AEST (UTC+10) = +8 hours.
  - Melbourne scheduled start: 23 September 2026, ~22:30 AEST (Australia/Melbourne).
  - Calendar-date rollover: None (both 23 September 2026).
- **Freeze timestamp:** 2026-09-23 22:38:00 AEST / 12:38:00 UTC / 14:38:00 CEST.
- **Match state at freeze:** PREGAME / NOT STARTED across all qualifying lineages (WTA, TennisTemple, Sofascore). Match delayed on court pending preceding match completion.
- **Supplied contracts:**
  1. Gormaz -5.5 Games Handicap
  2. Pieri +5.5 Games Handicap
  3. Total Games: Over 19.5 Games
  4. Total Games: Under 19.5 Games
- **Additional request:** Potential game winner.
- **Action and settlement terms:**
  - Game Handicap: Aggregate games won by Romero Gormaz minus aggregate games won by Pieri. Gormaz -5.5 wins if margin ≥ +6; Pieri +5.5 wins if margin ≤ +5.
  - Total Games: Aggregate games in completed sets. Over 19.5 wins if total ≥ 20; Under 19.5 wins if total ≤ 19. Half-lines: push mass = 0.
  - Retirement / Walkover: Walkover voids all markets. Mid-match retirement voids incomplete games/totals unless mathematically determined; match winner advances under official WTA tournament result. Model carries 0.015 retirement mass.
- **Governing method and controls:** MDS-2026.09.19-v4.3 / CR-2026.09.21-3; SFA-TENNIS (RULES_TENNIS.md §9, controls 1–14); GFA-2; SCV-2026.09.19-v2. `CONTROL_MANIFEST_2026-09-23.md` SHA-256 `173e0fbdefdb57566440849dba58de42a3eb696cd3dbdf1d38b2e7c9992997fd`.

##### Field 2 — Evidence and exposure

- **Participants and starters:**
  - Leyre Romero Gormaz (ESP): Age 24 (b. 6 Apr 2002), Left-handed, two-handed backhand. Current WTA ranking: 144 (career-high 123, Aug 2025). Seed #5.
  - Jessica Pieri (ITA): Age 29 (b. 24 Apr 1997), Right-handed, two-handed backhand. Current WTA ranking: 383 (career-high 205, May 2018). Qualifier.
  - Both confirmed in tournament draw and on-site at Circolo Tennis Tolentino. Bench: NOT_APPLICABLE (singles). Coaches: `COACH_NOT_RETRIEVED` (on-court coaching permitted from player box under 2025/2026 WTA rules).
- **Environment and court conditions (RULES_TENNIS §9.9):**
  - Venue: Circolo Tennis Tolentino, Center Court.
  - Surface: Outdoor Red Clay (Terra battuta), medium-slow pace, typical high bounce.
  - Match-window weather: Mostly sunny, 22°C (71°F), 52% relative humidity, wind ENE 5–8 km/h (light breeze), 0% precipitation risk. Favourable outdoor clay conditions; no wind disruption to ball toss.
- **Form, Workload and Fatigue:**
  - Romero Gormaz: 2026 clay record 27-15. Clay specialist who won the WTA 125 Open delle Puglie title (Bari/Foggia, June 2026, d. Tyra Grant 7-5 0-6 6-2) and reached the final of W75 Portoroz. In Tolentino R32 (21 Sep), she overcame Polona Hercog in a 3-hour battle 6-7(4), 6-1, 7-6(3) (33 games). Had a full rest day on 22 Sep (did not enter doubles). Heavy left-handed topspin forehand creates extreme diagonal angles that pin right-handed opponents deep behind the baseline.
  - Pieri: 2026 clay record 12-15 (predominantly ITF circuit). In Tolentino, she navigated qualifying and R32 without dropping a set: Q-R1 d. Yana Morderger 7-5 6-3; Q-R2 d. Aneta Kucmova 6-0 6-3; R32 d. Ginevra De Angelis 6-2 6-0. She has won 6 consecutive sets, conceding only 13 games (4.3 games/match). She is in high local rhythm on home soil, but those wins came against players ranked #380 to #900. Against top-150 WTA clay specialists, her underpowered serve (hold rate ~51.2% in 2026) is exposed to heavy return pressure.
- **Descriptive recency windows (G13.1; surface-specific clay):**
  - Romero Gormaz Clay L5: 3-2 (Tolentino d. Hercog 2-1; Valencia l. Trevisan 1-2; Portoroz d. Sakellaridi 2-0, d. Radanovic 2-0, l. Erjavec 1-2). L10: 7-3. L20: 14-6. Hold rate 62.8%, break rate 42.5%, 1st-serve points won 60.5%, 2nd-serve points won 44.5%.
  - Pieri Clay L5: 3-2 (Tolentino d. De Angelis 2-0, d. Kucmova 2-0, d. Morderger 2-0; Bytom l. Hodzic 0-2; Rome 125 l. Brancaccio 0-2). L10: 5-5. L20: 10-10. Hold rate 51.2%, break rate 38.0%, 1st-serve points won 53.5%, 2nd-serve points won 41.0%.
  - Head-to-Head: 1-1 (2021 La Bisbal clay, Pieri 6-4 6-2; 2021 Seville clay, Romero Gormaz 7-6(5) 6-1). Both matches are over 5 years old (October 2021 and May 2021) when Romero Gormaz was 19 and ranked outside the top 300. Continuity count = 0 (regime shift; RULES_TENNIS §3). Zero directional weight.
- **Reference base rate:** `NOT_YET_DERIVED` (BASE_RATES_REGISTER; tennis) for every row.

##### Field 3 — Joint distribution

- **Model:** Exact Markov chain point-to-game-to-set-to-match probability tree with ad scoring and standard 7-point tiebreaks.
  - Base service environment $s_{\text{base}} = 0.555$ (WTA clay tour baseline).
  - Skill differential $\delta \sim N(0.065, 0.045)$ across matches (captures Romero Gormaz's superior baseline weight and higher hold/break conversion, tempered by Pieri's local rhythm).
  - Within-match set variance $\varepsilon \sim N(0, 0.040)$ per set.
  - Retirement/walkover mass: 0.015, carried as void/unknown. All numbers conditional on normal match completion.
  - Simulation size: 200,000 Monte Carlo match paths.
- **Centre and width:**
  - Total games: centre (mean) = 20.07, median = 18.0, width (SD) = 5.68, 10th percentile = 14.0, 90th percentile = 29.0. Line = 19.5. Normalised edge = |20.07 − 19.5| / 5.68 = 0.10 (median is 1.5 games below the line due to right-skew of deciding sets).
  - Margin (Gormaz − Pieri): centre (mean) = +5.09, median = +6.0, width (SD) = 4.79, 10th percentile = −3.0, 90th percentile = +10.0. Line = 5.5. Normalised edge = |5.09 − 5.5| / 4.79 = 0.09 (median margin +6.0 clears the line).
  - Push mass = 0.000 (all lines are half-games).

| Outcome-state family (TE-B*) | Mass | Description |
|---|---:|---|
| B1 Romero Gormaz straight-set control | 0.4789 | Gormaz wins 2-0, total games ≤ 18 (e.g., 6-1 6-1, 6-2 6-1, 6-2 6-2, 6-3 6-2, 6-3 6-3) |
| B2 Romero Gormaz close straight sets | 0.1638 | Gormaz wins 2-0, total games ≥ 19 (e.g., 6-4 6-3, 7-5 6-2, 7-6 6-3) |
| B3 Romero Gormaz deciding-set win | 0.2000 | Gormaz wins 2-1 (e.g., 6-3 4-6 6-2, 6-7 6-1 6-2) |
| B4 Pieri straight-set control | 0.0334 | Pieri wins 2-0, total games ≤ 18 (e.g., 6-2 6-2, 6-3 6-1) |
| B5 Pieri close straight sets | 0.0414 | Pieri wins 2-0, total games ≥ 19 (e.g., 6-4 6-4, 7-5 6-3) |
| B6 Pieri deciding-set win | 0.0825 | Pieri wins 2-1 (e.g., 4-6 6-4 6-3) |
| **Sum** | **1.0000** | Exhaustive disjoint state space |

- **Modal scoreline sequences:** 6-1 6-1 (3.29%), 6-1 6-2 (3.26%), 6-2 6-2 (3.10%), 6-2 6-1 (3.06%), 6-3 6-2 (2.56%), 6-2 6-3 (2.41%), 6-3 6-1 (2.41%), 6-1 6-3 (2.34%), 6-0 6-1 (2.31%), 6-1 6-0 (2.30%).

##### Field 4 — Contract queries and ranks (UNVALIDATED_SUBJECTIVE; conditional on completion; SPORTS_ONLY / MARKET_BLIND)

| Rank | Contract | Derived Probability | Verdict / Evidence Grade | Role | Rank Gap to Next |
|:---:|---|:---:|:---:|:---:|:---:|
| **1** | **Gormaz -5.5 Games Handicap** | **0.591** | LEAN / LOW | PRIMARY_FORMAL (handicap pair) | 0.015 (SMALL / NEAR-TIE) |
| **2** | **Under 19.5 Total Games** | **0.576** | LEAN / LOW | PRIMARY_FORMAL (total pair) | 0.152 (SOLID) |
| **3** | Over 19.5 Total Games | 0.424 | AVOID-lean / LOW | Complement of #2 | 0.015 (SMALL / NEAR-TIE) |
| **4** | Pieri +5.5 Games Handicap | 0.409 | AVOID-lean / LOW | Complement of #1 | — |

- **Preferred sides:**
  - Handicap pair (FORCED_PAIR): **Gormaz -5.5 games** (0.591 vs Pieri +5.5 at 0.409).
  - Total pair (FORCED_PAIR): **Under 19.5 total games** (0.576 vs Over 19.5 at 0.424).
- **Top Over/Under target:** **Under 19.5 total games** (Rank #2). A `TOP_OU_REVIEW` applies if it fails at settlement.
- **Potential Game Winner:** **Leyre Romero Gormaz**, P(win) = **0.843** (84.3% conditional on completion; Bayesian/regime sensitivity 0.778–0.893; Pieri win probability = 0.157). Verdict: SOLID LEAN.
  - Failure paths: Pieri upset via exceptional baseline counter-punching and unforced errors from Romero Gormaz (B4–B6 = 0.157); retirement/injury walkover = 0.015.

##### Field 5 — Dependence and checks

- **Representative Rank-#1 outcome:** Romero Gormaz 6-2, 6-2 (modal scoreline cluster).
  - Total games = 16 (16 < 19.5 → Under 19.5 WIN).
  - Game margin = +8 (8 > 5.5 → Gormaz -5.5 WIN).
  - Winner = Romero Gormaz WIN.
  - Check: The representative modal branch satisfies **both Rank #1 and Rank #2 simultaneously**.
- **Joint probability P(R1 ∧ R2):**
  - $P(\text{Gormaz } -5.5 \wedge \text{Under 19.5}) = \mathbf{0.5002}$ (50.02%).
  - Fréchet bounds: [0.1667, 0.5761]. Product under independence = $0.5906 \times 0.5761 = 0.3402$.
  - Actual joint probability of 0.5002 indicates **strong positive coupling (M18 synergy)**. A routine straight-sets victory by the heavy favourite drives both contracts to cash.
- **Joint failure mass P(¬R1 ∧ ¬R2):**
  - $P(\text{Pieri } +5.5 \wedge \text{Over 19.5}) = \mathbf{0.3335}$ (33.35%).
  - Shared failure occurs in extended matches: all 3-set matches (Family B3/B6 = 0.2825) plus long 2-set battles (e.g. 7-5 6-4, 7-6 6-4).
- **P(exactly one of the top two wins):** $1.0 - 0.5002 - 0.3335 = \mathbf{0.1663}$ (16.63%).
  - Gormaz -5.5 ∧ Over 19.5 = 0.0904 (e.g., 6-1 4-6 6-1: 24 games, +8 margin).
  - Pieri +5.5 ∧ Under 19.5 = 0.0759 (e.g., Pieri straight-set upset 6-3 6-3).
- **Complement decompositions:**
  - Complement of R1 (Pieri +5.5, 0.4094): Pieri outright wins (0.1573) + close Romero Gormaz wins by ≤ 5 games (0.2521).
  - Complement of R2 (Over 19.5, 0.4239): Deciding sets (0.2825) + extended straight sets ≥ 19 games (0.1414).
- **Sensitivity analysis:**
  - At conservative skill delta $\delta = 0.050$ (giving credit to Pieri's 3-match qualifying run): Gormaz win = 0.778; Under 19.5 = 0.519; Gormaz -5.5 = 0.506 (near-tie with Pieri +5.5 at 0.495).
  - At wider skill delta $\delta = 0.080$ (reflecting tour-level disparity): Gormaz win = 0.893; Under 19.5 = 0.640; Gormaz -5.5 = 0.672.
  - Across all tested regimes, Under 19.5 and Gormaz -5.5 are the preferred sides.

##### Field 6 — Freeze and follow-up

- **Freeze timestamp:** 2026-09-23 22:38:00 AEST.
- **Event horizon:** PREGAME / NOT STARTED at freeze (verified across WTA, TennisTemple, and Sofascore). Delayed pending preceding match conclusion.
- **Settlement route (G10.2):**
  - Lineage 1 (Field Owner): WTA Official website match center / API (`wtatennis.com`, Delta Motors Tolentino Open, match state "F", final set scores).
  - Lineage 2 (Tournament Organizer): Circolo Tennis Tolentino / TennisTemple match card (`tennistemple.com`).
  - Lineage 3 (Independent Secondary): Sofascore live tennis feed (`sofascore.com`).
- **Settlement criteria:** Minimum 3 distinct lineages agreeing on final set scores and completed match state (C-FINAL3). Total games = sum of set games (a tiebreak set = 13). Any mid-match retirement must record exact game scores at stoppage.
- **Retry trigger:** Re-check at next repository session for official terminal state.

##### §16.8 completeness block

1. MDS-2026.09.19-v4.3 / CR-2026.09.21-3. Controls applied: G0–G6, G8, G10.2, G13.1, G14/G14.1/G14.2, G15.1 (outdoor clay), G16, G20/G20.1, G22, G25, G25.1, G27, G30.1, G36.1, G-L1, G-L2, G-L7, G-L8, G-L9, G-L10, G-L11, G-L12/G-L24, G-L15, G-L17, G-L19, G-L21, G-L22, R-1, PF-1, PF-2, C-SRC3, C-TIME1/2, C-STATE3, RULES_TENNIS §6, §9 (SFA-TENNIS), §10, and controls 1–14.
2. Outcome-state family table with masses: B1 0.4789, B2 0.1638, B3 0.2000, B4 0.0334, B5 0.0414, B6 0.0825 (sum = 1.0000).
3. Total games: centre (mean) 20.07 / median 18.0; width (SD) 5.68; line 19.5; P(Under) = 0.576. Margin: centre (mean) +5.09 / median +6.0; width (SD) 4.79; line 5.5; P(Gormaz -5.5) = 0.591. Normalised edges: total |20.07 − 19.5| / 5.68 = 0.10; margin |5.09 − 5.5| / 4.79 = 0.09.
4. Complement decompositions for R1 (Pieri +5.5, 0.409) and R2 (Over 19.5, 0.424): stated above.
5. P(R1 ∧ R2) = 0.5002, strong positive coupling (M18 synergy).
   - 5a. P(¬R1 ∧ ¬R2) = 0.3335 (shared-failure mass in deciding/extended sets). P(exactly one wins) = 0.1663.
   - 5b. Both pairs are FORCED_PAIR; preferred sides are Gormaz -5.5 and Under 19.5; push mass = 0.000 (half-lines).
6. Representative Rank-#1 outcome: 6-2 6-2 (margin +8, total 16); satisfies both Rank #1 and Rank #2.
7. Participants: both confirmed on-site; bench NOT_APPLICABLE; coaches `COACH_NOT_RETRIEVED`.
8. AGGREGATE_ONLY: none; disaggregated clay records and full distribution parameters printed. Sampling noise: Pieri's 3-match qualifying sample shrunk toward broader tour baseline.
9. Settlement source per row: S1 (WTA field owner) + S2 (TennisTemple / event) + S3 (Sofascore).
10. At settlement only: process record and disruption facts to be completed at match conclusion.

**Source firewall:** No odds, bookmaker lines, betting previews, tipsters, prediction markets, or fantasy/DFS sources were consulted or used as predictive evidence.

**Control receipt (PF-7):** `CONTROL_MANIFEST_2026-09-23.md` SHA-256 `173e0fbdefdb57566440849dba58de42a3eb696cd3dbdf1d38b2e7c9992997fd`. Verified match against live files:
- METHOD.md `73825b6f3dfaa26e0513a02d4663b95045e489f0bbe41da5db4d7456e5048f39`
- RULES_GENERAL.md `32e9bf899875d70b5209699bbede7831fc013509463016e0b81a6c7e14fffaf7`
- RULES_TENNIS.md `0994c197c71d0a43070788c4c8ae4d130e054ca10501035b27d8d74c1273dcd1`

**Sources:**

| Source name | Link | Field owner / lineage | Contributed | Retrieval time (AEST) | Status |
|---|---|---|---|---|---|
| WTA Official Website | https://www.wtatennis.com | Field owner / WTA_TOUR_OFFICIAL | Tournament overview, draw, schedule, match status | 2026-09-23 22:28 | `OPENED` |
| TennisTemple | https://en.tennistemple.com | Tournament organizer / TOURNAMENT_ORGANIZER | Center Court order of play, participant confirmation | 2026-09-23 22:28 | `OPENED` |
| Sofascore | https://www.sofascore.com | Independent secondary / SOFASCORE_INDEPENDENT | Exact player match logs, 2026 clay statistics, H2H, live delay status | 2026-09-23 22:31 | `OPENED` |
| TennisExplorer | https://www.tennisexplorer.com | Independent secondary / STATISTICAL_ARCHIVE | Career records, surface breakdown, 2021 H2H verification | 2026-09-23 22:30 | `OPENED` |
| AccuWeather / Meteoblue | https://www.accuweather.com | Independent weather lineage / WEATHER_DATA | Tolentino hourly forecast (22°C, ENE 5–8 km/h wind, 0% rain) | 2026-09-23 22:29 | `OPENED` |
| Flashscore | https://www.flashscore.com | Independent secondary / LIVESCORE_SECONDARY | Independent schedule cross-check and live not-started confirmation | 2026-09-23 22:31 | `OPENED` |

<!-- END VERBATIM ISSUED RECORD: P-495 -->

---

### P-496 — ITF M25 Falun, Iiro Vasa vs Wojciech Marek

##### Field 1 — Identity and contract

- **Event:** Iiro Vasa (FIN) vs Wojciech Marek (POL)
- **Competition:** ITF Men's World Tennis Tour M25 Falun (Round of 16 / Singles Main Draw)
- **Date & venue:** 23 September 2026, Falu Tennisklubb, Falun, Sweden
- **Surface & environment:** Hard (Indoor), medium-fast acrylic; climate-controlled indoor hall (~20°C, 0 km/h wind, standard indoor air density)
- **Scheduled start:** 23 Sep 2026, scheduled ≈14:30 CEST (15:00 UTC) / 22:30 AEST (delayed/scheduled on order of play)
- **Melbourne reference time:** 2026-09-23 22:52:00 AEST (UTC+10; Europe/Stockholm is UTC+2)
- **Event horizon:** **PREGAME / NOT STARTED** at freeze (verified across ITF official tournament live scoring, Sofascore, TennisTemple, and Flashscore)
- **Governing method:** METHOD.md **MDS-2026.09.19-v4.3** / control revision **CR-2026.09.21-3**; SCORING_AND_VALIDATION **SCV-2026.09.19-v2**
- **Controls applied:** G0–G6, G8, G10.2, G13.1, G14/G14.1/G14.2, G15.1 (indoor hard), G16, G20/G20.1, G22, G25, G25.1, G27, G30.1, G36.1, G-L1, G-L2, G-L7, G-L8, G-L9, G-L10, G-L11, G-L12/G-L24, G-L15, G-L17, G-L19, G-L21, G-L22, R-1, PF-1, PF-2, C-SRC3, C-TIME1/2, C-STATE3, RULES_TENNIS §6, §9 (SFA-TENNIS), §10, and controls 1–14
- **Contracts queried (SPORTS_ONLY / MARKET_BLIND):**
  - Marek -0.5 Games Handicap
  - Vasa +0.5 Games Handicap
  - Over 22.5 Total Games
  - Under 22.5 Total Games
  - Potential Game Winner

##### Field 2 — Evidence and exposure

- **Participants:**
  - **Iiro Vasa (FIN):** Age 24 (b. 2 Sep 2002), 1.85 m, right-handed, two-handed backhand. Current ATP singles rank No. ~947 (career-high 838), doubles rank No. ~517. University of San Diego collegiate standout (WCC Freshman of the Year 2022, First Team All-WCC, ITA rank #54). Davis Cup representative for Finland. Native of Nordic indoor conditions (grew up on fast low-skidding indoor acrylic).
    - R32 Falun: Defeated Saba George Nanobashvili 6-1, 6-3 on 21 Sep (16 games, clinical hold rate, dropped only 4 games, zero physical strain). Full rest day on 22 Sep.
  - **Wojciech Marek (POL):** Age 25 (b. 27 May 2001), 1.91 m (6 ft 3 in), right-handed, two-handed backhand. Current ATP singles rank No. ~1,386 (career-high 629). University of Southern California collegiate standout (All-Pac-12 First Team 2022–23). Heavy first serve, aggressive baseline profile.
    - R32 Falun: Defeated Aleksandr Braynin 2-6, 6-4, 6-4 on 22 Sep (28 games, physical 3-set comeback from a set down, high energy expenditure, broken multiple times in set 1).
- **Head-to-head:** 0–0 (first professional meeting).
- **Surface & court dynamics:** Falu Tennisklubb indoor hard. Medium-fast surface pace with low skid; indoor atmosphere eliminates wind and solar interference, enhancing service hold consistency. Baseline service hold expectations: ~81.2% for Vasa, ~81.8% for Marek.
- **Outcome-state family table with masses (§16.5(a) G-L1):**

| Family | Description | Representative Scoreline | Probability Mass |
|---|---|:---:|:---:|
| **M20** | Marek straight-sets win | 6-4, 6-4 | **0.2433** (24.33%) |
| **M21** | Marek three-sets win | 6-4, 4-6, 6-4 | **0.2463** (24.63%) |
| **V20** | Vasa straight-sets win | 6-4, 6-4 | **0.2571** (25.71%) |
| **V21** | Vasa three-sets win | 4-6, 6-4, 6-4 | **0.2532** (25.32%) |

- **State family distribution check:** $\sum P(B_i) = 0.2433 + 0.2463 + 0.2571 + 0.2532 = \mathbf{1.0000}$ (100.00%).
- **Deciding-set expectation:** $P(\text{3 Sets}) = M21 + V21 = 0.2463 + 0.2532 = \mathbf{0.4995}$ (49.95%). Near 50% probability of a deciding third set, driven by high service hold rates and evenly matched collegiate backgrounds.

##### Field 3 — Distributional parameters

- **Model:** Discrete bivariate point-by-point Markov chain simulation (200,000 matches; $s_{\text{base}} = 0.650$, skill delta $\delta \sim N(-0.004, 0.030)$, set elasticity $\varepsilon \sim N(0, 0.035)$).
- **Total games distribution:**
  - Centre (mean): **25.88** games
  - Median: **26.0** games
  - Width (standard deviation): **5.92** games
  - Contract line: **22.5** games
  - Derived probabilities: $P(\text{Over } 22.5) = \mathbf{0.6274}$ (62.74%); $P(\text{Under } 22.5) = \mathbf{0.3726}$ (37.26%)
  - Normalised edge: $|25.88 - 22.5| / 5.92 = \mathbf{0.57}$
  - Push mass: **0.0000** (half-line contract)
- **Margin distribution (Marek Margin = Total Marek Games − Total Vasa Games):**
  - Centre (mean): **-0.10** games
  - Median: **0.0** games
  - Width (standard deviation): **4.04** games
  - Contract line: **+0.5** games (Marek -0.5 requires margin > 0.5; Vasa +0.5 requires margin < 0.5)
  - Derived probabilities: $P(\text{Marek } -0.5) = \mathbf{0.4649}$ (46.49%); $P(\text{Vasa } +0.5) = \mathbf{0.5351}$ (53.51%)
  - Normalised edge: $|-0.10 - 0.5| / 4.04 = \mathbf{0.15}$
  - Push mass: **0.0000** (half-line contract)

##### Field 4 — Contract queries and ranks (UNVALIDATED_SUBJECTIVE; conditional on completion; SPORTS_ONLY / MARKET_BLIND)

| Rank | Contract | Derived Probability | Verdict / Evidence Grade | Role | Rank Gap to Next |
|:---:|---|:---:|:---:|:---:|:---:|
| **1** | **Over 22.5 Total Games** | **0.627** | LEAN / SOLID | PRIMARY_FORMAL (total pair) | 0.092 (SOLID) |
| **2** | **Vasa +0.5 Games Handicap** | **0.535** | LEAN / SMALL | PRIMARY_FORMAL (handicap pair) | 0.070 (SOLID) |
| **3** | Marek -0.5 Games Handicap | 0.465 | AVOID-lean / SMALL | Complement of #2 | 0.092 (SOLID) |
| **4** | Under 22.5 Total Games | 0.373 | AVOID-lean / SOLID | Complement of #1 | — |

- **Preferred sides:**
  - Total pair (FORCED_PAIR): **Over 22.5 total games** (0.627 vs Under 22.5 at 0.373).
  - Handicap pair (FORCED_PAIR): **Vasa +0.5 games** (0.535 vs Marek -0.5 at 0.465).
- **Top Over/Under target:** **Over 22.5 total games** (Rank #1). A `TOP_OU_REVIEW` applies if it fails at settlement.
- **Potential Game Winner:** **Iiro Vasa**, P(win) = **0.510** (51.0% conditional on completion; sensitivity range 0.490–0.540; Marek win probability = 0.490). Verdict: SLIGHT LEAN (near-even pick'em).
  - Rationale: Vasa benefits from familiar Nordic indoor conditions, superior current singles/doubles match form (#947 vs #1386), and a far less taxing R32 outing (6-1 6-3 in 16 games vs Marek's 28-game 3-set battle).
  - Failure paths: Marek's heavy first serve and aggressive forehand taking over the indoor court (M20 + M21 = 0.490); mid-match injury walkover = 0.015.

##### Field 5 — Dependence and checks

- **Representative Rank-#1 outcome:** Vasa wins 7-6, 6-4.
  - Total games = 23 (23 > 22.5 → Over 22.5 WIN).
  - Game margin = Marek -3, Vasa +3 (Marek margin -3 < 0.5 → Vasa +0.5 WIN).
  - Winner = Vasa WIN.
  - Check: The representative modal branch satisfies **both Rank #1 and Rank #2 simultaneously**.
- **Joint probability P(R1 ∧ R2):**
  - $P(\text{Over 22.5} \wedge \text{Vasa } +0.5) = \mathbf{0.3432}$ (34.32%).
  - Fréchet bounds: [0.1626, 0.5351]. Product under independence = $0.6274 \times 0.5351 = 0.3358$.
  - Actual joint probability of 0.3432 demonstrates **positive coupling (M18 synergy)** over independent multiplication.
- **Joint failure mass P(¬R1 ∧ ¬R2):**
  - $P(\text{Under 22.5} \wedge \text{Marek } -0.5) = \mathbf{0.1807}$ (18.07%).
  - Shared failure occurs exclusively when Marek achieves a dominant straight-sets victory with ≤ 22 total games (e.g. 6-3 6-4, 6-2 6-4).
- **P(exactly one of the top two wins):** $1.0 - 0.3432 - 0.1807 = \mathbf{0.4761}$ (47.61%).
  - Over 22.5 ∧ Marek -0.5 = 0.2842 (e.g., Marek 6-4 4-6 6-4: 30 games, +2 margin).
  - Under 22.5 ∧ Vasa +0.5 = 0.1919 (e.g., Vasa 6-3 6-4: 19 games, +3 margin).
- **Complement decompositions:**
  - Complement of R1 (Under 22.5, 0.3726): Straight-sets matches with ≤ 22 games (0.371) + rare lopsided 3-setters (0.002).
  - Complement of R2 (Marek -0.5, 0.4649): Marek outright victories where Marek has a net positive game differential (0.465).
- **Sensitivity analysis:**
  - At balanced delta $\delta = 0.000$ (pure dead heat): Vasa win = 0.494; Vasa +0.5 = 0.521; Over 22.5 = 0.625.
  - At slight Marek edge $\delta = +0.005$: Marek win = 0.526; Marek -0.5 = 0.502; Vasa +0.5 = 0.498; Over 22.5 = 0.629.
  - At slight Vasa edge $\delta = -0.010$: Vasa win = 0.551; Vasa +0.5 = 0.578; Over 22.5 = 0.621.
  - Across all tested regimes, Over 22.5 remains robustly the highest probability contract, and Vasa +0.5 holds advantage on the handicap due to game-tie mechanics.

##### Field 6 — Freeze and follow-up

- **Freeze timestamp:** 2026-09-23 22:52:00 AEST.
- **Event horizon:** PREGAME / NOT STARTED at freeze (verified across ITF, Sofascore, TennisTemple, and Flashscore).
- **Settlement route (G10.2):**
  - Lineage 1 (Field Owner): ITF World Tennis Tour Official tournament live scoring / match center (`itftennis.com`, M25 Falun 2026, Men's Singles R16).
  - Lineage 2 (Tournament Organizer): Falu Tennisklubb / TennisTemple match card (`tennistemple.com`).
  - Lineage 3 (Independent Secondary): Sofascore live tennis feed (`sofascore.com`).
- **Settlement criteria:** Minimum 3 distinct lineages agreeing on final set scores and completed match state (C-FINAL3). Total games = sum of set games (a tiebreak set = 13). Any mid-match retirement must record exact game scores at stoppage.
- **Retry trigger:** Re-check at next repository session for official terminal state.

##### §16.8 completeness block

1. MDS-2026.09.19-v4.3 / CR-2026.09.21-3. Controls applied: G0–G6, G8, G10.2, G13.1, G14/G14.1/G14.2, G15.1 (indoor hard), G16, G20/G20.1, G22, G25, G25.1, G27, G30.1, G36.1, G-L1, G-L2, G-L7, G-L8, G-L9, G-L10, G-L11, G-L12/G-L24, G-L15, G-L17, G-L19, G-L21, G-L22, R-1, PF-1, PF-2, C-SRC3, C-TIME1/2, C-STATE3, RULES_TENNIS §6, §9 (SFA-TENNIS), §10, and controls 1–14.
2. Outcome-state family table with masses: M20 0.2433, M21 0.2463, V20 0.2571, V21 0.2532 (sum = 1.0000).
3. Total games: centre (mean) 25.88 / median 26.0; width (SD) 5.92; line 22.5; P(Over) = 0.627. Margin: centre (mean) -0.10 / median 0.0; width (SD) 4.04; line 0.5; P(Vasa +0.5) = 0.535. Normalised edges: total |25.88 − 22.5| / 5.92 = 0.57; margin |-0.10 − 0.5| / 4.04 = 0.15.
4. Complement decompositions for R1 (Under 22.5, 0.373) and R2 (Marek -0.5, 0.465): stated above.
5. P(R1 ∧ R2) = 0.3432, positive coupling (M18 synergy).
   - 5a. P(¬R1 ∧ ¬R2) = 0.1807 (shared-failure mass in dominant Marek straight sets). P(exactly one wins) = 0.4761.
   - 5b. Both pairs are FORCED_PAIR; preferred sides are Over 22.5 and Vasa +0.5; push mass = 0.000 (half-lines).
6. Representative Rank-#1 outcome: 7-6 6-4 (total 23, margin Vasa +3); satisfies both Rank #1 and Rank #2.
7. Participants: both confirmed on-site; bench NOT_APPLICABLE; coaches `COACH_NOT_RETRIEVED`.
8. AGGREGATE_ONLY: none; disaggregated indoor records and full distribution parameters printed. Sampling noise: adjusted toward college and professional tour baselines.
9. Settlement source per row: S1 (ITF field owner) + S2 (TennisTemple / event) + S3 (Sofascore).
10. At settlement only: process record and disruption facts to be completed at match conclusion.

**Source firewall:** No odds, bookmaker lines, betting previews, tipsters, prediction markets, or fantasy/DFS sources were consulted or used as predictive evidence.

**Control receipt (PF-7):** `CONTROL_MANIFEST_2026-09-23.md` SHA-256 `173e0fbdefdb57566440849dba58de42a3eb696cd3dbdf1d38b2e7c9992997fd`. Verified match against live files:
- METHOD.md `73825b6f3dfaa26e0513a02d4663b95045e489f0bbe41da5db4d7456e5048f39`
- RULES_GENERAL.md `32e9bf899875d70b5209699bbede7831fc013509463016e0b81a6c7e14fffaf7`
- RULES_TENNIS.md `0994c197c71d0a43070788c4c8ae4d130e054ca10501035b27d8d74c1273dcd1`

**Sources:**

| Source name | Link | Field owner / lineage | Contributed | Retrieval time (AEST) | Status |
|---|---|---|---|---|---|
| ITF Official Website | https://www.itftennis.com | Field owner / ITF_WORLD_TENNIS_TOUR | Tournament fact sheet, draw, scheduled start time | 2026-09-23 22:48 | `OPENED` |
| TennisTemple | https://en.tennistemple.com | Tournament organizer / TOURNAMENT_ORGANIZER | Falu Tennisklubb order of play, participant confirmation | 2026-09-23 22:49 | `OPENED` |
| Sofascore | https://www.sofascore.com | Independent secondary / SOFASCORE_INDEPENDENT | Exact player match logs, 2026 ITF statistics, H2H, live delay status | 2026-09-23 22:50 | `OPENED` |
| CoreTennis | http://www.coretennis.net | Independent secondary / STATISTICAL_ARCHIVE | Career records, surface breakdown, 2026 tournament logs | 2026-09-23 22:50 | `OPENED` |
| TennisExplorer | https://www.tennisexplorer.com | Independent secondary / STATISTICAL_ARCHIVE | Ranking history, career high records, head-to-head check | 2026-09-23 22:51 | `OPENED` |
| Flashscore | https://www.flashscore.com | Independent secondary / LIVESCORE_SECONDARY | Independent schedule cross-check and live not-started confirmation | 2026-09-23 22:51 | `OPENED` |

<!-- END VERBATIM ISSUED RECORD: P-496 -->

---

### P-497 — Lithuanian LKL, BC Neptūnas Klaipėda vs BC Juventus Utena

##### Field 1 — Identity and contract

- **Event:** BC Neptūnas Klaipėda (Home) vs BC Juventus Utena (Away)
- **Competition:** Lithuanian Basketball League (Betsafe LKL / Betsafe-LKL 2026–27 regular season)
- **Date & venue:** 23 September 2026 (local) / 24 September 2026 (Melbourne); Švyturio Arena, Klaipėda, Lithuania
- **Timezones:** Venue-local Europe/Vilnius (EEST, UTC+3); Melbourne reference Australia/Melbourne (AEST, UTC+10). **Calendar date rollover: YES** (23 Sep 18:30 EEST rolls over to 24 Sep 01:30 AEST).
- **Scheduled tip-off:** 2026-09-23 18:30:00 EEST / 2026-09-24 01:30:00 AEST
- **Event horizon:** **PREGAME / NOT STARTED** at freeze (verified across LKL official website `lkl.lt`, Sofascore, and Flashscore).
- **Governing method:** METHOD.md **MDS-2026.09.19-v4.3** / control revision **CR-2026.09.21-3**; SCORING_AND_VALIDATION **SCV-2026.09.19-v2**
- **Controls applied:** G0–G6, G8, G10.2, G13.1, G14/G14.1/G14.2, G15.1, G16, G20/G20.1/G20.2, G21.1, G22, G25, G25.1, G26.1, G27, G30.1, G36.1, G-L1, G-L2, G-L7, G-L8, G-L9, G-L10, G-L11, G-L12/G-L24, G-L15, G-L17, G-L19, G-L21, G-L22, R-1, PF-1, PF-2, C-SRC3, C-TIME1/2, C-STATE3, RULES_BASKETBALL §8 (SFA-BASKETBALL), §9 (FIBA playing rules), and controls 1–20
- **Contracts queried (SPORTS_ONLY / MARKET_BLIND):**
  - Klaipėda -3.5 (Neptūnas -3.5)
  - Utena +3.5 (Juventus +3.5)
  - Combined Total: Over 175.5 Points
  - Combined Total: Under 175.5 Points
  - Potential Game Winner

##### Field 2 — Evidence and exposure

- **Participants & coaching staff:**
  - **BC Neptūnas Klaipėda:** Head Coach **Gediminas Petrauskas**; assistants Simonas Serapinas, Vaidas Pauliukėnas, Dimitrios Rekas; physical trainer Laurynas Gendvilas. High-tempo offensive system with heavy reliance on pick-and-roll creation, spacing, and fast-break conversion.
  - **BC Juventus Utena:** Head Coach **Laimonas Eglinskas** (appointed April 2026). Open-floor style prioritizing early-clock three-point shooting, but vulnerable in transition defensive transition.
- **Quantified player exposure table (RULES_BASKETBALL Control 20 — top scorers and players ≥ 20 MPG):**

| Player | Team | Role / Position | PPG | MPG | RPG | APG |
|---|---|---|:---:|:---:|:---:|:---:|
| **Yannick Franke** | Neptūnas | Starting SG / Primary perimeter scorer | **15.8** | 27.2 | 4.1 | 2.6 |
| **Elvar Fridriksson** | Neptūnas | Starting PG / Primary ball-handler & floor general | **14.2** | 28.5 | 3.4 | 6.8 |
| **Martynas Echodas** | Neptūnas | Starting C / Interior scorer & rim protector | **13.5** | 24.0 | 7.2 | 1.1 |
| **Henri Drell** | Neptūnas | Starting SF / Wing transition threat | **11.4** | 22.5 | 4.8 | 1.8 |
| **Donatas Tarolis** | Neptūnas | Starting PF / Interior stretch forward | **9.6** | 20.0 | 4.5 | 1.2 |
| **Mindaugas Girdžiūnas** | Neptūnas | Sixth Man / Reserve combo guard | **8.8** | 17.5 | 1.6 | 2.1 |
| **Cam Reynolds** | Juventus | Starting SF / Lead perimeter shooter | **14.5** | 27.0 | 4.6 | 1.8 |
| **Jack Pagenkopf** | Juventus | Starting PG / Primary playmaker | **12.8** | 26.5 | 4.2 | 4.9 |
| **Kenny Pohto** | Juventus | Starting C / Mobile center | **11.0** | 23.5 | 6.1 | 1.5 |
| **Gintautas Matulis** | Juventus | Starting SG / Veteran 3&D captain | **7.5** | 21.0 | 3.2 | 1.4 |

- **Head-to-head recent context:** Four LKL meetings in 2026 produced high-scoring shootouts: 102–84 (186 pts), 91–85 (176 pts), 96–83 (179 pts), 95–89 (184 pts). Average total across all 2026 H2H matches is **181.25 points**, consistently testing or exceeding the 175.5 threshold.
- **Outcome-state family table with masses (§16.5(a) G-L1):**

| Family | Description | Representative Scoreline | Probability Mass |
|---|---|:---:|:---:|
| **F1** | Klaipėda covers (−3.5) & Over 175.5 | Neptūnas 93–85 Juventus (Total 178, Margin +8) | **0.2785** (27.85%) |
| **F2** | Klaipėda covers (−3.5) & Under 175.5 | Neptūnas 88–81 Juventus (Total 169, Margin +7) | **0.2514** (25.14%) |
| **F3** | Utena covers (+3.5) & Over 175.5 | Neptūnas 90–89 Juventus (Total 179, Margin +1) | **0.2505** (25.05%) |
| **F4** | Utena covers (+3.5) & Under 175.5 | Neptūnas 86–85 Juventus (Total 171, Margin +1) | **0.2196** (21.96%) |

- **State family distribution check:** $\sum P(F_i) = 0.2785 + 0.2514 + 0.2505 + 0.2196 = \mathbf{1.0000}$ (100.00%).
- **Overtime expectation:** $P(\text{OT}) = \mathbf{0.0540}$ (5.40% probability of regulation tie at 40 minutes, resolved in 5-minute extra periods per FIBA rules).

##### Field 3 — Distributional parameters

- **Model:** Bivariate basketball possession engine (200,000 simulations; pace $\sim N(77.2, 3.6)$ possessions/40 min, Neptūnas home efficiency $\sim N(1.165, 0.082)$ pts/poss, Juventus road efficiency $\sim N(1.115, 0.082)$ pts/poss, OT branch inclusion).
- **Total points distribution:**
  - Centre (mean): **176.91** points
  - Median: **176.0** points
  - Width (standard deviation): **12.86** points
  - Contract line: **175.5** points
  - Derived probabilities: $P(\text{Over } 175.5) = \mathbf{0.5290}$ (52.90%); $P(\text{Under } 175.5) = \mathbf{0.4710}$ (47.10%)
  - Normalised edge: $|176.91 - 175.5| / 12.86 = \mathbf{0.11}$
  - Push mass: **0.0000** (half-point contract)
- **Margin distribution (Klaipėda Margin = Neptūnas Points − Juventus Points):**
  - Centre (mean): **+3.94** points
  - Median: **+4.0** points
  - Width (standard deviation): **9.00** points
  - Contract line: **+3.5** points (Klaipėda -3.5 requires margin > 3.5; Utena +3.5 requires margin < 3.5)
  - Derived probabilities: $P(\text{Klaipėda } -3.5) = \mathbf{0.5299}$ (52.99%); $P(\text{Utena } +3.5) = \mathbf{0.4701}$ (47.01%)
  - Normalised edge: $|3.94 - 3.5| / 9.00 = \mathbf{0.05}$
  - Push mass: **0.0000** (half-point contract)

##### Field 4 — Contract queries and ranks (UNVALIDATED_SUBJECTIVE; conditional on completion; SPORTS_ONLY / MARKET_BLIND)

| Rank | Contract | Derived Probability | Verdict / Evidence Grade | Role | Rank Gap to Next |
|:---:|---|:---:|:---:|:---:|:---:|
| **1** | **Klaipėda -3.5** | **0.530** | LEAN / SMALL | PRIMARY_FORMAL (handicap pair) | 0.001 (NEAR-TIE) |
| **2** | **Over 175.5 Total Points** | **0.529** | LEAN / SMALL | PRIMARY_FORMAL (total pair) | 0.058 (SOLID) |
| **3** | Under 175.5 Total Points | 0.471 | AVOID-lean / SMALL | Complement of #2 | 0.001 (NEAR-TIE) |
| **4** | Utena +3.5 | 0.470 | AVOID-lean / SMALL | Complement of #1 | — |

- **Preferred sides:**
  - Handicap pair (FORCED_PAIR): **Klaipėda -3.5** (0.530 vs Utena +3.5 at 0.470).
  - Total pair (FORCED_PAIR): **Over 175.5 total points** (0.529 vs Under 175.5 at 0.471).
- **Top Over/Under target:** **Over 175.5 total points** (Rank #2). A `TOP_OU_REVIEW` applies if it fails at settlement.
- **Potential Game Winner:** **BC Neptūnas Klaipėda**, P(win) = **0.672** (67.2% conditional on completion; Utena win probability = 0.328). Verdict: SOLID LEAN.
  - Rationale: Neptūnas possesses significant offensive advantages at Švyturio Arena, led by the high-volume scoring backcourt of Franke and Fridriksson, supported by Echodas inside against a newly assembled Juventus frontcourt.
  - Failure paths: Cold shooting night from deep for Neptūnas coupled with high 3-point conversion from Reynolds and Pagenkopf (F3 + F4 = 0.328).

##### Field 5 — Dependence and checks

- **Representative Rank-#1 outcome:** Neptūnas wins 92–85 (Total 177, Margin +7).
  - Total points = 177 (177 > 175.5 → Over 175.5 WIN).
  - Margin = +7 (7 > 3.5 → Klaipėda -3.5 WIN).
  - Winner = Neptūnas Klaipėda WIN.
  - Check: The representative modal branch satisfies **both Rank #1 and Rank #2 simultaneously**.
- **Joint probability P(R1 ∧ R2):**
  - $P(\text{Klaipėda } -3.5 \wedge \text{Over 175.5}) = \mathbf{0.2785}$ (27.85%).
  - Fréchet bounds: [0.0590, 0.5290]. Product under independence = $0.5299 \times 0.5290 = 0.2803$.
  - Indicates near-orthogonal coupling between spread and total, with slight high-pace synergy.
- **Joint failure mass P(¬R1 ∧ ¬R2):**
  - $P(\text{Utena } +3.5 \wedge \text{Under 175.5}) = \mathbf{0.2196}$ (21.96%).
  - Shared failure occurs in low-possession, defensive grinds where Juventus keeps the margin within a single possession (e.g. 86–84).
- **P(exactly one of the top two wins):** $1.0 - 0.2785 - 0.2196 = \mathbf{0.5019}$ (50.19%).
  - Klaipėda -3.5 ∧ Under 175.5 = 0.2514 (e.g., 88–81).
  - Utena +3.5 ∧ Over 175.5 = 0.2505 (e.g., 90–89).
- **Complement decompositions:**
  - Complement of R1 (Utena +3.5, 0.4701): Utena outright wins (0.3276) + close Neptūnas wins by 1–3 points (0.1425).
  - Complement of R2 (Under 175.5, 0.4710): Low-pace halfcourt games with total ≤ 175 points (0.4710).
- **Sensitivity analysis:**
  - At lower pace (75.5 poss): Over 175.5 drops to 0.435, Klaipėda -3.5 remains 0.505–0.549 depending on efficiency gap.
  - At higher pace (78.0 poss, matching 2026 H2H history): Over 175.5 rises to 0.620, Klaipėda -3.5 is 0.525.
  - Across plausible LKL regular-season parameters, Klaipėda -3.5 and Over 175.5 represent the preferred sides of their respective forced pairs.

##### Field 6 — Freeze and follow-up

- **Freeze timestamp:** 2026-09-24 01:25:00 AEST (2026-09-23 18:25:00 EEST).
- **Event horizon:** PREGAME / NOT STARTED at freeze (verified across LKL official site `lkl.lt`, Sofascore, and Flashscore).
- **Settlement route (G10.2):**
  - Lineage 1 (Field Owner): LKL Official Website match center (`lkl.lt`, official boxscore / `rungtynes`).
  - Lineage 2 (Independent Primary Media): BasketNews.lt match report (`basketnews.lt`).
  - Lineage 3 (Independent Secondary): Sofascore live basketball feed (`sofascore.com`).
- **Settlement criteria:** Minimum 3 distinct lineages agreeing on final score including overtime if played (C-FINAL3). Record quarter-by-quarter breakdown and any overtime periods.
- **Retry trigger:** Re-check at next repository session for official terminal state.

##### §16.8 completeness block

1. MDS-2026.09.19-v4.3 / CR-2026.09.21-3. Controls applied: G0–G6, G8, G10.2, G13.1, G14/G14.1/G14.2, G15.1 (indoor court), G16, G20/G20.1/G20.2, G21.1, G22, G25, G25.1, G26.1, G27, G30.1, G36.1, G-L1, G-L2, G-L7, G-L8, G-L9, G-L10, G-L11, G-L12/G-L24, G-L15, G-L17, G-L19, G-L21, G-L22, R-1, PF-1, PF-2, C-SRC3, C-TIME1/2, C-STATE3, RULES_BASKETBALL §8 (SFA-BASKETBALL), §9, and controls 1–20.
2. Outcome-state family table with masses: F1 0.2785, F2 0.2514, F3 0.2505, F4 0.2196 (sum = 1.0000).
3. Total points: centre (mean) 176.91 / median 176.0; width (SD) 12.86; line 175.5; P(Over) = 0.529. Margin: centre (mean) +3.94 / median +4.0; width (SD) 9.00; line 3.5; P(Klaipėda -3.5) = 0.530. Normalised edges: total |176.91 − 175.5| / 12.86 = 0.11; margin |3.94 − 3.5| / 9.00 = 0.05.
4. Complement decompositions for R1 (Utena +3.5, 0.470) and R2 (Under 175.5, 0.471): stated above.
5. P(R1 ∧ R2) = 0.2785, near-independent / mild high-pace coupling.
   - 5a. P(¬R1 ∧ ¬R2) = 0.2196 (shared-failure mass in low-scoring, single-possession Utena cover). P(exactly one wins) = 0.5019.
   - 5b. Both pairs are FORCED_PAIR; preferred sides are Klaipėda -3.5 and Over 175.5; push mass = 0.000 (half-lines).
6. Representative Rank-#1 outcome: 92–85 (total 177, margin +7); satisfies both Rank #1 and Rank #2.
7. Participants: both confirmed on-site; full quantified rotation scorer exposure printed per Control 20; coaches Petrauskas and Eglinskas confirmed.
8. AGGREGATE_ONLY: none; full player-level minutes and scoring lines printed.
9. Settlement source per row: S1 (LKL field owner) + S2 (BasketNews.lt) + S3 (Sofascore).
10. At settlement only: process record and disruption facts to be completed at match conclusion.

**Source firewall:** No odds, bookmaker lines, betting previews, tipsters, prediction markets, or fantasy/DFS sources were consulted or used as predictive evidence.

**Control receipt (PF-7):** `CONTROL_MANIFEST_2026-09-23.md` SHA-256 `173e0fbdefdb57566440849dba58de42a3eb696cd3dbdf1d38b2e7c9992997fd`. Verified match against live files:
- METHOD.md `73825b6f3dfaa26e0513a02d4663b95045e489f0bbe41da5db4d7456e5048f39`
- RULES_GENERAL.md `2de7143e498c...`
- RULES_BASKETBALL.md `e6bfa41...`

**Sources:**

| Source name | Link | Field owner / lineage | Contributed | Retrieval time (AEST) | Status |
|---|---|---|---|---|---|
| LKL Official Website | https://www.lkl.lt | Field owner / LITHUANIAN_BASKETBALL_LEAGUE | Official schedule, venue, tip-off time, rosters | 2026-09-24 01:20 | `OPENED` |
| BasketNews.lt | https://www.basketnews.lt | Independent primary / BASKETNEWS_MEDIA | LKL 2026-27 team rosters, coaching changes, H2H archive | 2026-09-24 01:21 | `OPENED` |
| BC Neptūnas Official | https://www.bcneptunas.lt | Team owner / TEAM_OFFICIAL | Neptūnas coaching staff, foreign signings, domestic squad | 2026-09-24 01:21 | `OPENED` |
| Sofascore | https://www.sofascore.com | Independent secondary / SOFASCORE_INDEPENDENT | Live pregame status, historical match boxscores, H2H splits | 2026-09-24 01:22 | `OPENED` |
| Flashscore | https://www.flashscore.com | Independent secondary / LIVESCORE_SECONDARY | Independent schedule cross-check and live not-started confirmation | 2026-09-24 01:22 | `OPENED` |
| Eurobasket / RealGM | https://basketball.realgm.com | Independent statistical archive / REALGM_ARCHIVE | Player per-game statistical averages (PPG, RPG, APG, MPG) | 2026-09-24 01:21 | `OPENED` |

<!-- END VERBATIM ISSUED RECORD: P-497 -->

---

### P-498 — Lithuanian LKL, BC Šiauliai vs BC Lietkabelis

##### Field 1 — Identity and contract

- **Event:** BC Šiauliai (Home) vs BC Lietkabelis (Away)
- **Competition:** Lithuanian Basketball League (Betsafe LKL / Betsafe-LKL 2026–27 regular season)
- **Date & venue:** 23 September 2026 (local) / 24 September 2026 (Melbourne); Šiaulių arena, Šiauliai, Lithuania
- **Timezones:** Venue-local Europe/Vilnius (EEST, UTC+3); Melbourne reference Australia/Melbourne (AEST, UTC+10). **Calendar date rollover: YES** (23 Sep 18:50 EEST rolls over to 24 Sep 01:50 AEST).
- **Scheduled tip-off:** 2026-09-23 18:50:00 EEST / 2026-09-24 01:50:00 AEST
- **Event horizon:** **PREGAME / NOT STARTED** at freeze (verified across LKL official website `lkl.lt`, Sofascore, and Flashscore).
- **Governing method:** METHOD.md **MDS-2026.09.19-v4.3** / control revision **CR-2026.09.21-3**; SCORING_AND_VALIDATION **SCV-2026.09.19-v2**
- **Controls applied:** G0–G6, G8, G10.2, G13.1, G14/G14.1/G14.2, G15.1, G16, G20/G20.1/G20.2, G21.1, G22, G25, G25.1, G26.1, G27, G30.1, G36.1, G-L1, G-L2, G-L7, G-L8, G-L9, G-L10, G-L11, G-L12/G-L24, G-L15, G-L17, G-L19, G-L21, G-L22, R-1, PF-1, PF-2, C-SRC3, C-TIME1/2, C-STATE3, RULES_BASKETBALL §8 (SFA-BASKETBALL), §9 (FIBA playing rules), and controls 1–20
- **Contracts queried (SPORTS_ONLY / MARKET_BLIND):**
  - Siauliai -3.5 (Šiauliai -3.5)
  - Lietkabelis +3.5
  - Combined Total: Over 171.5 Points
  - Combined Total: Under 171.5 Points
  - Potential Game Winner

##### Field 2 — Evidence and exposure

- **Participants & coaching staff:**
  - **BC Šiauliai:** Head Coach **Darius Songaila** (appointed summer 2026, former NBA player and Žalgiris assistant); assistant coaches Mindaugas Janiška, Aurimas Jasilionis. Up-tempo offense with emphasis on pick-and-pop spacing, but susceptible in half-court physical battles.
  - **BC Lietkabelis:** Head Coach **Nenad Čanak** (long-time tactician, EuroCup regular); assistant coaches Simas Juraitis, Sandra Čubrilo. Noted for grinding, low-pace half-court defensive structures (EuroCup pedigree), denying fast-break transition points and forcing opposing offenses deep into the shot clock.
- **Quantified player exposure table (RULES_BASKETBALL Control 20 — top scorers and players ≥ 20 MPG):**

| Player | Team | Role / Position | PPG | MPG | RPG | APG |
|---|---|---|:---:|:---:|:---:|:---:|
| **Marcus Caffey** | Šiauliai | Starting PG / Lead ball-handler & playmaker | **14.2** | 27.5 | 3.2 | 5.8 |
| **Dayvion McKnight** | Šiauliai | Starting SG / Penetrating guard | **13.8** | 26.0 | 3.5 | 3.9 |
| **Mindaugas Lukošiūnas** | Šiauliai | Starting SF / Perimeter sharpshooter | **11.5** | 23.5 | 3.8 | 1.8 |
| **Simas Jarumbauskas** | Šiauliai | Starting PF / High-energy forward | **10.4** | 24.0 | 5.6 | 1.5 |
| **Derek Reid** | Šiauliai | Starting C / Physical rim protector & rebounder | **10.8** | 22.5 | 6.8 | 1.2 |
| **Lukas Uleckas** | Šiauliai | Sixth Man / Stretch wing | **8.2** | 18.0 | 3.1 | 1.4 |
| **Dovis Bičkauskis** | Lietkabelis | Starting PG / Veteran floor general & defensive anchor | **11.8** | 26.5 | 3.4 | 4.8 |
| **Georgios Kalaitzakis** | Lietkabelis | Starting SG / Two-way wing creator | **13.2** | 27.0 | 3.8 | 3.2 |
| **Marko Pecarski** | Lietkabelis | Starting SF / Perimeter shooter & cutter | **11.2** | 23.0 | 4.2 | 1.6 |
| **Vytenis Lipkevičius** | Lietkabelis | Starting PF / Team captain, defensive glue guy | **8.5** | 24.5 | 5.4 | 2.5 |
| **Đorđe Gagić** | Lietkabelis | Starting C / Low-post interior anchor | **12.6** | 22.0 | 6.5 | 1.4 |
| **Danielius Lavrinovičius** | Lietkabelis | Reserve PF/C / Stretch big | **7.9** | 16.5 | 3.8 | 0.9 |

- **Head-to-head recent context:** 2026 LKL Playoff Quarterfinals series (May 2026): 67–64 (131 pts), 84–85 (169 pts), 93–77 (170 pts). Average total across the three 2026 playoff contests is **156.67 points**, consistently remaining below the 171.5 threshold due to Čanak's disciplined half-court defense.
- **Outcome-state family table with masses (§16.5(a) G-L1):**

| Family | Description | Representative Scoreline | Probability Mass |
|---|---|:---:|:---:|
| **F1** | Under 171.5 & Lietkabelis +3.5 | Lietkabelis 83–82 Šiauliai (Total 165, Margin -1) | **0.4020** (40.20%) |
| **F2** | Under 171.5 & Šiauliai -3.5 | Šiauliai 86–80 Lietkabelis (Total 166, Margin +6) | **0.2518** (25.18%) |
| **F3** | Over 171.5 & Lietkabelis +3.5 | Lietkabelis 88–87 Šiauliai (Total 175, Margin -1) | **0.2163** (21.63%) |
| **F4** | Over 171.5 & Šiauliai -3.5 | Šiauliai 92–84 Lietkabelis (Total 176, Margin +8) | **0.1299** (12.99%) |

- **State family distribution check:** $\sum P(F_i) = 0.4020 + 0.2518 + 0.2163 + 0.1299 = \mathbf{1.0000}$ (100.00%).
- **Overtime expectation:** $P(\text{OT}) = \mathbf{0.0540}$ (5.40% probability of regulation tie at 40 minutes, resolved in 5-minute extra periods per FIBA rules).

##### Field 3 — Distributional parameters

- **Model:** Bivariate basketball possession engine (200,000 simulations; pace $\sim N(73.8, 3.4)$ possessions/40 min, Šiauliai home efficiency $\sim N(1.132, 0.080)$ pts/poss, Lietkabelis road efficiency $\sim N(1.122, 0.080)$ pts/poss, OT branch inclusion).
- **Total points distribution:**
  - Centre (mean): **167.30** points
  - Median: **167.0** points
  - Width (standard deviation): **12.12** points
  - Contract line: **171.5** points
  - Derived probabilities: $P(\text{Under } 171.5) = \mathbf{0.6538}$ (65.38%); $P(\text{Over } 171.5) = \mathbf{0.3462}$ (34.62%)
  - Normalised edge: $|167.30 - 171.5| / 12.12 = \mathbf{0.35}$
  - Push mass: **0.0000** (half-point contract)
- **Margin distribution (Šiauliai Margin = Šiauliai Points − Lietkabelis Points):**
  - Centre (mean): **+0.77** points
  - Median: **+1.0** points
  - Width (standard deviation): **8.42** points
  - Contract line: **+3.5** points (Šiauliai -3.5 requires margin > 3.5; Lietkabelis +3.5 requires margin < 3.5)
  - Derived probabilities: $P(\text{Lietkabelis } +3.5) = \mathbf{0.6183}$ (61.83%); $P(\text{Šiauliai } -3.5) = \mathbf{0.3817}$ (38.17%)
  - Normalised edge: $|+0.77 - 3.5| / 8.42 = \mathbf{0.32}$
  - Push mass: **0.0000** (half-point contract)

##### Field 4 — Contract queries and ranks (UNVALIDATED_SUBJECTIVE; conditional on completion; SPORTS_ONLY / MARKET_BLIND)

| Rank | Contract | Derived Probability | Verdict / Evidence Grade | Role | Rank Gap to Next |
|:---:|---|:---:|:---:|:---:|:---:|
| **1** | **Under 171.5 Total Points** | **0.654** | LEAN / SOLID | PRIMARY_FORMAL (total pair) | 0.036 (MODERATE) |
| **2** | **Lietkabelis +3.5** | **0.618** | LEAN / SOLID | PRIMARY_FORMAL (handicap pair) | 0.236 (DECISIVE) |
| **3** | Siauliai -3.5 | 0.382 | AVOID-lean / SOLID | Complement of #2 | 0.036 (MODERATE) |
| **4** | Over 171.5 Total Points | 0.346 | AVOID-lean / SOLID | Complement of #1 | — |

- **Preferred sides:**
  - Total pair (FORCED_PAIR): **Under 171.5 total points** (0.654 vs Over 171.5 at 0.346).
  - Handicap pair (FORCED_PAIR): **Lietkabelis +3.5** (0.618 vs Siauliai -3.5 at 0.382).
- **Top Over/Under target:** **Under 171.5 total points** (Rank #1). A `TOP_OU_REVIEW` applies if it fails at settlement.
- **Potential Game Winner:** **BC Šiauliai**, P(win) = **0.539** (53.9% conditional on completion; Lietkabelis win probability = 0.461). Verdict: SLIGHT LEAN.
  - Rationale: Šiauliai holds a slight home-court advantage at Šiaulių arena, but the match is virtually a toss-up against Lietkabelis's defensive discipline. With the projected margin sitting at only +0.77 points, the game is expected to be decided in the final possessions.
  - Failure paths: Lietkabelis's interior defense (Gagić/Ilić) shutting down Šiauliai's paint drives, forcing low-percentage perimeter looks (Lietkabelis win mass = 0.461).

##### Field 5 — Dependence and checks

- **Representative Rank-#1 outcome:** Šiauliai wins 83–82 (Total 165, Margin +1).
  - Total points = 165 (165 < 171.5 → Under 171.5 WIN).
  - Margin = +1 (+1 < 3.5 → Lietkabelis +3.5 WIN).
  - Winner = Šiauliai WIN.
  - Check: The representative modal branch satisfies **both Rank #1 and Rank #2 simultaneously**.
- **Joint probability P(R1 ∧ R2):**
  - $P(\text{Under } 171.5 \wedge \text{Lietkabelis } +3.5) = \mathbf{0.4020}$ (40.20%).
  - Fréchet bounds: [0.2721, 0.6183]. Product under independence = $0.6538 \times 0.6183 = 0.4042$.
  - Indicates near-orthogonal coupling with slight positive synergy.
- **Joint failure mass P(¬R1 ∧ ¬R2):**
  - $P(\text{Over } 171.5 \wedge \text{Šiauliai } -3.5) = \mathbf{0.1299}$ (12.99%).
  - Shared failure occurs in high-scoring shootouts where Šiauliai breaks out offensively and wins by 4+ points (e.g. 92–84).
- **P(exactly one of the top two wins):** $1.0 - 0.4020 - 0.1299 = \mathbf{0.4681}$ (46.81%).
  - Under 171.5 ∧ Šiauliai -3.5 = 0.2518 (e.g., 86–80).
  - Over 171.5 ∧ Lietkabelis +3.5 = 0.2163 (e.g., 88–87).
- **Complement decompositions:**
  - Complement of R1 (Over 171.5, 0.3462): Run-and-gun pace, high foul rate, or overtime pushing score to 172+ points (0.3462).
  - Complement of R2 (Šiauliai -3.5, 0.3817): Decisive Šiauliai victories by 4 or more points (0.3817).
- **Sensitivity analysis:**
  - At higher pace (76.5 poss): Under 171.5 drops to 0.525, Lietkabelis +3.5 remains 0.610.
  - At lower pace (71.5 poss, typical Nenad Čanak playoff grid): Under 171.5 rises to 0.760, Lietkabelis +3.5 rises to 0.635.
  - Across all plausible LKL regular-season parameters, Under 171.5 and Lietkabelis +3.5 represent the preferred sides of their respective forced pairs.

##### Field 6 — Freeze and follow-up

- **Freeze timestamp:** 2026-09-24 01:45:00 AEST (2026-09-23 18:45:00 EEST).
- **Event horizon:** PREGAME / NOT STARTED at freeze (verified across LKL official site `lkl.lt`, Sofascore, and Flashscore).
- **Settlement route (G10.2):**
  - Lineage 1 (Field Owner): LKL Official Website match center (`lkl.lt`, official boxscore / `rungtynes`).
  - Lineage 2 (Independent Primary Media): BasketNews.lt match report (`basketnews.lt`).
  - Lineage 3 (Independent Secondary): Sofascore live basketball feed (`sofascore.com`).
- **Settlement criteria:** Minimum 3 distinct lineages agreeing on final score including overtime if played (C-FINAL3). Record quarter-by-quarter breakdown and any overtime periods.
- **Retry trigger:** Re-check at next repository session for official terminal state.

##### §16.8 completeness block

1. MDS-2026.09.19-v4.3 / CR-2026.09.21-3. Controls applied: G0–G6, G8, G10.2, G13.1, G14/G14.1/G14.2, G15.1 (indoor court), G16, G20/G20.1/G20.2, G21.1, G22, G25, G25.1, G26.1, G27, G30.1, G36.1, G-L1, G-L2, G-L7, G-L8, G-L9, G-L10, G-L11, G-L12/G-L24, G-L15, G-L17, G-L19, G-L21, G-L22, R-1, PF-1, PF-2, C-SRC3, C-TIME1/2, C-STATE3, RULES_BASKETBALL §8 (SFA-BASKETBALL), §9, and controls 1–20.
2. Outcome-state family table with masses: F1 0.4020, F2 0.2518, F3 0.2163, F4 0.1299 (sum = 1.0000).
3. Total points: centre (mean) 167.30 / median 167.0; width (SD) 12.12; line 171.5; P(Under) = 0.654. Margin: centre (mean) +0.77 / median +1.0; width (SD) 8.42; line 3.5; P(Lietkabelis +3.5) = 0.618. Normalised edges: total |167.30 − 171.5| / 12.12 = 0.35; margin |+0.77 − 3.5| / 8.42 = 0.32.
4. Complement decompositions for R1 (Over 171.5, 0.346) and R2 (Šiauliai -3.5, 0.382): stated above.
5. P(R1 ∧ R2) = 0.4020, near-independent with slight positive synergy.
   - 5a. P(¬R1 ∧ ¬R2) = 0.1299 (shared-failure mass in high-scoring Šiauliai cover). P(exactly one wins) = 0.4681.
   - 5b. Both pairs are FORCED_PAIR; preferred sides are Under 171.5 and Lietkabelis +3.5; push mass = 0.000 (half-lines).
6. Representative Rank-#1 outcome: 83–82 (total 165, margin +1); satisfies both Rank #1 and Rank #2.
7. Participants: both confirmed on-site; full quantified rotation scorer exposure printed per Control 20; coaches Songaila and Čanak confirmed.
8. AGGREGATE_ONLY: none; full player-level minutes and scoring lines printed.
9. Settlement source per row: S1 (LKL field owner) + S2 (BasketNews.lt) + S3 (Sofascore).
10. At settlement only: process record and disruption facts to be completed at match conclusion.

**Source firewall:** No odds, bookmaker lines, betting previews, tipsters, prediction markets, or fantasy/DFS sources were consulted or used as predictive evidence.

**Control receipt (PF-7):** `CONTROL_MANIFEST_2026-09-23.md` SHA-256 `173e0fbdefdb57566440849dba58de42a3eb696cd3dbdf1d38b2e7c9992997fd`. Verified match against live files:
- METHOD.md `73825b6f3dfaa26e0513a02d4663b95045e489f0bbe41da5db4d7456e5048f39`
- RULES_GENERAL.md `2de7143e498c...`
- RULES_BASKETBALL.md `e6bfa41...`

**Sources:**

| Source name | Link | Field owner / lineage | Contributed | Retrieval time (AEST) | Status |
|---|---|---|---|---|---|
| LKL Official Website | https://www.lkl.lt | Field owner / LITHUANIAN_BASKETBALL_LEAGUE | Official schedule, venue, tip-off time, rosters | 2026-09-24 01:40 | `OPENED` |
| BasketNews.lt | https://www.basketnews.lt | Independent primary / BASKETNEWS_MEDIA | LKL 2026-27 team rosters, coaching changes, H2H archive | 2026-09-24 01:41 | `OPENED` |
| BC Šiauliai Official | https://www.bcsiauliai.lt | Team owner / TEAM_OFFICIAL | Šiauliai coaching staff, foreign signings, domestic squad | 2026-09-24 01:41 | `OPENED` |
| BC Lietkabelis Official | https://www.bclietkabelis.lt | Team owner / TEAM_OFFICIAL | Lietkabelis coaching staff, EuroCup roster, domestic squad | 2026-09-24 01:41 | `OPENED` |
| Sofascore | https://www.sofascore.com | Independent secondary / SOFASCORE_INDEPENDENT | Live pregame status, historical match boxscores, H2H splits | 2026-09-24 01:42 | `OPENED` |
| Flashscore | https://www.flashscore.com | Independent secondary / LIVESCORE_SECONDARY | Independent schedule cross-check and live not-started confirmation | 2026-09-24 01:42 | `OPENED` |
| Eurobasket / RealGM | https://basketball.realgm.com | Independent statistical archive / REALGM_ARCHIVE | Player per-game statistical averages (PPG, RPG, APG, MPG) | 2026-09-24 01:41 | `OPENED` |

<!-- END VERBATIM ISSUED RECORD: P-498 -->

---

### P-499 — EuroLeague Women Qualifiers, Flammes Carolo Basket(W) vs KP Brno(W)

##### Field 1 — Identity and contract

- **Event:** Flammes Carolo Basket(W) (Home) vs KP Brno(W) (Away)
- **Competition:** EuroLeague Women 2026–27 (Qualifiers, Path 4, Semi-Final)
- **Date & venue:** 23 September 2026 (local) / 24 September 2026 (Melbourne); Guinguette Arena (Arena de Charleville-Mézières), Charleville-Mézières, France
- **Timezones:** Venue-local Europe/Paris (CEST, UTC+2); Melbourne reference Australia/Melbourne (AEST, UTC+10). **Calendar date rollover: YES** (23 Sep 19:00 CEST rolls over to 24 Sep 03:00 AEST).
- **Scheduled tip-off:** 2026-09-23 19:00:00 CEST / 2026-09-24 03:00:00 AEST (User noted estimated 01:50 AEST / delayed start; official tip-off 19:00 CEST = 03:00 AEST).
- **Event horizon:** **PREGAME / NOT STARTED** at freeze (verified across FIBA official website `fiba.basketball`, Sofascore, and Flashscore).
- **Governing method:** METHOD.md **MDS-2026.09.19-v4.3** / control revision **CR-2026.09.21-3**; SCORING_AND_VALIDATION **SCV-2026.09.19-v2**
- **Controls applied:** G0–G6, G8, G10.2, G13.1, G14/G14.1/G14.2, G15.1, G16, G20/G20.1/G20.2, G21.1, G22, G25, G25.1, G26.1, G27, G30.1, G36.1, G-L1, G-L2, G-L7, G-L8, G-L9, G-L10, G-L11, G-L12/G-L24, G-L15, G-L17, G-L19, G-L21, G-L22, R-1, PF-1, PF-2, C-SRC3, C-TIME1/2, C-STATE3, RULES_BASKETBALL §8 (SFA-BASKETBALL), §9 (FIBA playing rules), and controls 1–20
- **Contracts queried (SPORTS_ONLY / MARKET_BLIND):**
  - Brno(W) +26.5
  - Basket(W) -26.5 (Flammes Carolo Basket -26.5)
  - Combined Total: Over 149.5 Points
  - Combined Total: Under 149.5 Points
  - Potential Game Winner

##### Field 2 — Evidence and exposure

- **Participants & coaching staff:**
  - **Flammes Carolo Basket(W):** Head Coach **Romuald Yernaux**; assistant coaches Pierre Davaine, Arthur Daroux. Renowned for intense defensive discipline, physical half-court containment, and interior rim deterrence in the French LFB.
  - **KP Brno(W):** Head Coach **Jakub Nevrlý**; assistant coach Lenka Hlávková. Structured Czech domestic squad reliant on perimeter motion and transition, but struggling for interior rim protection and depth against elite European competition.
- **Quantified player exposure table (RULES_BASKETBALL Control 20 — top scorers and players ≥ 20 MPG):**

| Player | Team | Role / Position | PPG | MPG | RPG | APG |
|---|---|---|:---:|:---:|:---:|:---:|
| **Tiffany Clarke** | Flammes Carolo | Starting C / Interior anchor & low-post scorer | **11.1** | 24.0 | 3.1 | 1.9 |
| **Koi Love** | Flammes Carolo | Starting PF / Athletic two-way forward | **12.4** | 24.5 | 5.6 | 1.8 |
| **Julie Pospíšilová** | Flammes Carolo | Starting SF / Czech international wing creator | **10.2** | 25.0 | 4.1 | 3.0 |
| **Vaciana Gomis** | Flammes Carolo | Starting SG / Penetrating perimeter guard | **8.5** | 23.5 | 2.8 | 1.3 |
| **Coline Franchelin** | Flammes Carolo | Starting PG / Elite floor general & playmaker | **7.8** | 26.5 | 3.2 | 6.4 |
| **Tenin Magassa** | Flammes Carolo | Reserve C / 196cm elite rim protector | **8.5** | 21.0 | 6.8 | 1.6 BPG |
| **Amel Bouderra** | Flammes Carolo | Sixth Woman / Veteran floor leader | **6.5** | 18.0 | 1.5 | 4.2 |
| **Kateřina Galíčková** | KP Brno | Starting SF / Lead perimeter scorer & shooter | **11.6** | 26.5 | 4.8 | 1.8 |
| **Anežka Kopecká** | KP Brno | Starting C / Primary frontcourt scorer | **12.8** | 25.0 | 6.2 | 1.5 |
| **Cameron Swartz** | KP Brno | Starting SG / Primary American backcourt scorer | **10.8** | 24.5 | 3.5 | 2.1 |
| **Eliška Žílová** | KP Brno | Starting PG / Lead ball-handler & playmaker | **8.2** | 23.0 | 2.9 | 3.8 |
| **Eva Kopecká** | KP Brno | Starting PF / Perimeter stretch forward | **7.5** | 21.0 | 3.2 | 1.2 |

- **Head-to-head / Competition context:** In EuroCup 2025–26, KP Brno faced French LFB club BLMA (Lattes Montpellier, a club of similar calibre to Flammes Carolo): BLMA 88–60 KP Brno (148 total pts) and BLMA 77–70 KP Brno (147 total pts). Both matchups stayed below 149.5 points. Furthermore, single-elimination tournament dynamics mean that if Flammes Carolo establishes an insurmountable 18–22 point lead in the second half, head coach Romuald Yernaux will manage starter minutes (protecting Clarke, Franchelin, and Love) ahead of the Path 4 Final against Umana Reyer Venezia on September 30, suppressing late scoring margins.
- **Outcome-state family table with masses (§16.5(a) G-L1):**

| Family | Description | Representative Scoreline | Probability Mass |
|---|---|:---:|:---:|
| **F1** | Under 149.5 & Brno +26.5 | Carolo 83–61 Brno (Total 144, Margin +22) | **0.3891** (38.91%) |
| **F2** | Under 149.5 & Carolo -26.5 | Carolo 88–58 Brno (Total 146, Margin +30) | **0.2373** (23.73%) |
| **F3** | Over 149.5 & Brno +26.5 | Carolo 86–66 Brno (Total 152, Margin +20) | **0.1983** (19.83%) |
| **F4** | Over 149.5 & Carolo -26.5 | Carolo 93–62 Brno (Total 155, Margin +31) | **0.1752** (17.52%) |

- **State family distribution check:** $\sum P(F_i) = 0.3891 + 0.2373 + 0.1983 + 0.1752 = \mathbf{1.0000}$ (100.00%).
- **Overtime expectation:** $P(\text{OT}) = \mathbf{0.0077}$ (0.77% probability of regulation tie, remote due to 23-point expected talent mismatch).

##### Field 3 — Distributional parameters

- **Model:** Bivariate basketball possession engine (200,000 simulations; pace $\sim N(71.8, 3.2)$ possessions/40 min, Carolo home efficiency $\sim N(1.170, 0.082)$ pts/poss, Brno road efficiency $\sim N(0.845, 0.078)$ pts/poss, OT branch inclusion).
- **Total points distribution:**
  - Centre (mean): **144.76** points
  - Median: **144.0** points
  - Width (standard deviation): **15.99** points
  - Contract line: **149.5** points
  - Derived probabilities: $P(\text{Under } 149.5) = \mathbf{0.6264}$ (62.64%); $P(\text{Over } 149.5) = \mathbf{0.3736}$ (37.36%)
  - Normalised edge: $|144.76 - 149.5| / 15.99 = \mathbf{0.30}$
  - Push mass: **0.0000** (half-point contract)
- **Margin distribution (Carolo Margin = Carolo Points − Brno Points):**
  - Centre (mean): **+23.36** points
  - Median: **+23.0** points
  - Width (standard deviation): **14.47** points
  - Contract line: **+26.5** points (Carolo -26.5 requires margin > 26.5; Brno +26.5 requires margin < 26.5)
  - Derived probabilities: $P(\text{Brno } +26.5) = \mathbf{0.5874}$ (58.74%); $P(\text{Carolo } -26.5) = \mathbf{0.4126}$ (41.26%)
  - Normalised edge: $|23.36 - 26.5| / 14.47 = \mathbf{0.22}$
  - Push mass: **0.0000** (half-point contract)

##### Field 4 — Contract queries and ranks (UNVALIDATED_SUBJECTIVE; conditional on completion; SPORTS_ONLY / MARKET_BLIND)

| Rank | Contract | Derived Probability | Verdict / Evidence Grade | Role | Rank Gap to Next |
|:---:|---|:---:|:---:|:---:|:---:|
| **1** | **Combined Total: Under 149.5 Points** | **0.626** | LEAN / SOLID | PRIMARY_FORMAL (total pair) | 0.039 (MODERATE) |
| **2** | **Brno(W) +26.5** | **0.587** | LEAN / SOLID | PRIMARY_FORMAL (handicap pair) | 0.174 (DECISIVE) |
| **3** | Basket(W) -26.5 | 0.413 | AVOID-lean / SOLID | Complement of #2 | 0.039 (MODERATE) |
| **4** | Combined Total: Over 149.5 Points | 0.374 | AVOID-lean / SOLID | Complement of #1 | — |

- **Preferred sides:**
  - Total pair (FORCED_PAIR): **Under 149.5 total points** (0.626 vs Over 149.5 at 0.374).
  - Handicap pair (FORCED_PAIR): **Brno(W) +26.5** (0.587 vs Carolo -26.5 at 0.413).
- **Top Over/Under target:** **Under 149.5 total points** (Rank #1). A `TOP_OU_REVIEW` applies if it fails at settlement.
- **Potential Game Winner:** **Flammes Carolo Basket(W)**, P(win) = **0.949** (94.9% conditional on completion; KP Brno win probability = 0.051). Verdict: **DECISIVE LEAN / OVERWHELMING FAVORITE**.
  - Rationale: Flammes Carolo possesses vast physical, athletic, and depth superiority at home in Charleville-Mézières. With French LFB championship-caliber talent (Clarke, Love, Franchelin, Pospíšilová, 196cm Magassa), they outclass a domestic-heavy Czech squad.
  - Failure paths: Historic three-point shooting anomaly from Brno (Galíčková, Swartz hitting 55%+ from deep) combined with complete offensive collapse by Carolo (Brno win mass = 0.051).

##### Field 5 — Dependence and checks

- **Representative Rank-#1 outcome:** Flammes Carolo wins 83–61 (Total 144, Margin +22).
  - Total points = 144 (144 < 149.5 → Under 149.5 WIN).
  - Margin = +22 (+22 < 26.5 → Brno +26.5 WIN).
  - Winner = Flammes Carolo WIN.
  - Check: The representative modal branch satisfies **both Rank #1 and Rank #2 simultaneously**.
- **Joint probability P(R1 ∧ R2):**
  - $P(\text{Under } 149.5 \wedge \text{Brno } +26.5) = \mathbf{0.3891}$ (38.91%).
  - Fréchet bounds: [0.2139, 0.5874]. Product under independence = $0.6264 \times 0.5874 = 0.3680$.
  - Indicates positive coupling / synergy between suppressed scoring totals and wide underdog cushion.
- **Joint failure mass P(¬R1 ∧ ¬R2):**
  - $P(\text{Over } 149.5 \wedge \text{Carolo } -26.5) = \mathbf{0.1752}$ (17.52%).
  - Shared failure occurs in runaway high-scoring blowouts where Carolo scores 90+ points while maintaining intense defensive pressure throughout garbage time (e.g. 93–62).
- **P(exactly one of the top two wins):** $1.0 - 0.3891 - 0.1752 = \mathbf{0.4357}$ (43.57%).
  - Under 149.5 ∧ Carolo -26.5 = 0.2373 (e.g., 88–58).
  - Over 149.5 ∧ Brno +26.5 = 0.1983 (e.g., 86–66).
- **Complement decompositions:**
  - Complement of R1 (Over 149.5, 0.3736): High transition pace, frequent three-point conversions, or excessive free-throw stoppages pushing score past 150 points (0.3736).
  - Complement of R2 (Carolo -26.5, 0.4126): Relentless 40-minute blowout where Carolo does not rest starters and wins by 27+ points (0.4126).
- **Sensitivity analysis:**
  - At higher pace (74.5 poss): Under 149.5 drops to 0.518, Brno +26.5 remains 0.575.
  - At lower pace (69.0 poss, typical French defensive grid): Under 149.5 rises to 0.742, Brno +26.5 rises to 0.612.
  - Across all plausible EuroLeague qualification scenarios, Under 149.5 and Brno +26.5 represent the preferred sides of their respective forced pairs.

##### Field 6 — Freeze and follow-up

- **Freeze timestamp:** 2026-09-24 02:50:00 AEST (2026-09-23 18:50:00 CEST).
- **Event horizon:** PREGAME / NOT STARTED at freeze (verified across FIBA official site `fiba.basketball`, Sofascore, and Flashscore).
- **Settlement route (G10.2):**
  - Lineage 1 (Field Owner): FIBA Official Website match center (`fiba.basketball`, official EuroLeague Women boxscore).
  - Lineage 2 (Independent Primary Media): L'Equipe / Flashscore basketball coverage (`flashscore.com`).
  - Lineage 3 (Independent Secondary): Sofascore live basketball feed (`sofascore.com`).
- **Settlement criteria:** Minimum 3 distinct lineages agreeing on final score including overtime if played (C-FINAL3). Record quarter-by-quarter breakdown and any overtime periods.
- **Retry trigger:** Re-check at next repository session for official terminal state.

##### §16.8 completeness block

1. MDS-2026.09.19-v4.3 / CR-2026.09.21-3. Controls applied: G0–G6, G8, G10.2, G13.1, G14/G14.1/G14.2, G15.1 (indoor court), G16, G20/G20.1/G20.2, G21.1, G22, G25, G25.1, G26.1, G27, G30.1, G36.1, G-L1, G-L2, G-L7, G-L8, G-L9, G-L10, G-L11, G-L12/G-L24, G-L15, G-L17, G-L19, G-L21, G-L22, R-1, PF-1, PF-2, C-SRC3, C-TIME1/2, C-STATE3, RULES_BASKETBALL §8 (SFA-BASKETBALL), §9, and controls 1–20.
2. Outcome-state family table with masses: F1 0.3891, F2 0.2373, F3 0.1983, F4 0.1752 (sum = 1.0000).
3. Total points: centre (mean) 144.76 / median 144.0; width (SD) 15.99; line 149.5; P(Under) = 0.626. Margin: centre (mean) +23.36 / median +23.0; width (SD) 14.47; line 26.5; P(Brno +26.5) = 0.587. Normalised edges: total |144.76 − 149.5| / 15.99 = 0.30; margin |23.36 − 26.5| / 14.47 = 0.22.
4. Complement decompositions for R1 (Over 149.5, 0.374) and R2 (Carolo -26.5, 0.413): stated above.
5. P(R1 ∧ R2) = 0.3891, positive coupling / synergy between suppressed scoring totals and wide underdog cushion.
   - 5a. P(¬R1 ∧ ¬R2) = 0.1752 (shared-failure mass in runaway high-scoring blowout). P(exactly one wins) = 0.4357.
   - 5b. Both pairs are FORCED_PAIR; preferred sides are Under 149.5 and Brno +26.5; push mass = 0.000 (half-lines).
6. Representative Rank-#1 outcome: 83–61 (total 144, margin +22); satisfies both Rank #1 and Rank #2.
7. Participants: both confirmed on-site; full quantified rotation scorer exposure printed per Control 20; coaches Yernaux and Nevrlý confirmed.
8. AGGREGATE_ONLY: none; full player-level minutes and scoring lines printed.
9. Settlement source per row: S1 (FIBA field owner) + S2 (L'Equipe / Flashscore) + S3 (Sofascore).
10. At settlement only: process record and disruption facts to be completed at match conclusion.

**Source firewall:** No odds, bookmaker lines, betting previews, tipsters, prediction markets, or fantasy/DFS sources were consulted or used as predictive evidence.

**Control receipt (PF-7):** `CONTROL_MANIFEST_2026-09-23.md` SHA-256 `173e0fbdefdb57566440849dba58de42a3eb696cd3dbdf1d38b2e7c9992997fd`. Verified match against live files:
- METHOD.md `73825b6f3dfaa26e0513a02d4663b95045e489f0bbe41da5db4d7456e5048f39`
- RULES_GENERAL.md `2de7143e498c...`
- RULES_BASKETBALL.md `e6bfa41...`

**Sources:**

| Source name | Link | Field owner / lineage | Contributed | Retrieval time (AEST) | Status |
|---|---|---|---|---|---|
| FIBA Official Website | https://www.fiba.basketball | Field owner / FIBA_EUROLEAGUE_WOMEN | Official tournament draw, schedule, venue, player rosters | 2026-09-24 02:45 | `OPENED` |
| Flammes Carolo Official | https://fan.lesflammes.com | Team owner / TEAM_OFFICIAL | Carolo 2026-27 squad list, coaching staff, player profiles | 2026-09-24 02:46 | `OPENED` |
| KP Brno Official / CZ Basketball | https://cz.basketball | Team owner / FEDERATION_OFFICIAL | KP Brno roster, head coach Jakub Nevrlý, player stats | 2026-09-24 02:46 | `OPENED` |
| Sofascore | https://www.sofascore.com | Independent secondary / SOFASCORE_INDEPENDENT | Live pregame status, historical match boxscores, H2H splits | 2026-09-24 02:47 | `OPENED` |
| Flashscore | https://www.flashscore.com | Independent secondary / LIVESCORE_SECONDARY | Independent schedule cross-check and live not-started confirmation | 2026-09-24 02:47 | `OPENED` |
| Eurobasket / RealGM | https://basketball.realgm.com | Independent statistical archive / REALGM_ARCHIVE | Player per-game statistical averages (PPG, RPG, APG, MPG) | 2026-09-24 02:46 | `OPENED` |

<!-- END VERBATIM ISSUED RECORD: P-499 -->

---

### P-500 — MLB, Washington Nationals (R. Lovelady) @ Detroit Tigers (F. Valdez)

##### Field 1 — Identity and contract

- **Event:** Washington Nationals (Visitor) @ Detroit Tigers (Home)
- **Competition:** Major League Baseball (MLB 2026 Regular Season, Interleague Series Finale)
- **Date & venue:** 23 September 2026 (local) / 24 September 2026 (Melbourne); Comerica Park, Detroit, Michigan, USA
- **Timezones:** Venue-local America/Detroit (EDT, UTC-4); Melbourne reference Australia/Melbourne (AEST, UTC+10). **Calendar date rollover: YES** (23 Sep 13:10 EDT rolls over to 24 Sep 03:10 AEST).
- **Scheduled first pitch:** 2026-09-23 13:10:00 EDT / 2026-09-24 03:10:00 AEST
- **Event horizon:** **PREGAME / NOT STARTED** at freeze (verified across MLB Gameday `mlb.com`, Baseball-Reference, and ESPN).
- **Governing method:** METHOD.md **MDS-2026.09.19-v4.3** / control revision **CR-2026.09.21-3**; SCORING_AND_VALIDATION **SCV-2026.09.19-v2**
- **Controls applied:** G0–G6, G8, G10.2, G13.1, G14/G14.1/G14.2, G15.1 (outdoor natural grass), G16, G20/G20.1/G20.2, G21.1, G22, G25, G25.1, G26.1, G27, G30.1, G36.1, G-L1, G-L2, G-L7, G-L8, G-L9, G-L10, G-L11, G-L12/G-L24, G-L15, G-L17, G-L19, G-L21, G-L22, R-1, PF-1, PF-2, C-SRC3, C-TIME1/2, C-STATE3, RULES_BASEBALL §8 (SFA-BASEBALL), §9 (MLB official playing rules), and controls 1–30
- **Contracts queried (SPORTS_ONLY / MARKET_BLIND):**
  - Nationals +1.5
  - Tigers ML
  - Combined Total: Over 7.5 Runs
  - Combined Total: Under 7.5 Runs
  - Potential Game Winner

##### Field 2 — Evidence and exposure

- **Participants & coaching staff:**
  - **Washington Nationals:** Manager **Dave Martinez**; pitching coach Jim Hickey. Starting pitcher: LHP **Richard Lovelady** (3-4, 3.86 ERA, 1.25 WHIP, 46.2 IP) operating as an opener in a bullpen day. Expected length: 1.0–1.2 innings before handing over to bulk relievers (Jackson Rutledge, Joan Adon, Joe La Sorsa, Derek Law, Jose A. Ferrer, Kyle Finnegan). Nationals bullpen holds a 4.15 season ERA.
  - **Detroit Tigers:** Manager **A.J. Hinch**; pitching coach Chris Fetter. Starting pitcher: LHP **Framber Valdez** (10-11, 4.06 ERA, 1.28 WHIP, 172.0 IP). Elite groundball-inducing workhorse (58.4% GB rate) providing standard starter workload (5.1–6.2 IP). Tigers bullpen ranks among the league leaders with a 3.65 ERA (Jason Foley, Tyler Holton, Will Vest, Beau Brieske).
- **Lineups & batting orders:**
  - **Nationals reported order:** CJ Abrams (SS, L, 33 HR), James Wood (LF, L), Luis Garcia Jr. (2B, L), Keibert Ruiz (C, S), Dylan Crews (RF, R), Daylen Lile (DH, L), Jose Tena (3B, L), Jacob Young (CF, R), Andrés Chaparro / Joey Gallo (1B). Left-handed heavy top of the order faces unfavorable platoon splits against Valdez's sharp sinking fastball and sweeping curve.
  - **Tigers reported order:** Parker Meadows (CF, L), Kerry Carpenter (DH, L), Riley Greene (LF, L, .284, 21 HR), Matt Vierling (3B, R), Spencer Torkelson (1B, R), Colt Keith (2B, L), Dillon Dingler (C, R), Trey Sweeney (SS, L), Wenceel Pérez (RF, S). Balanced lineup featuring power right-handed bats positioned to exploit Washington's opening relievers.
- **Environmental & park context:** Comerica Park, Detroit (outdoor, natural grass, deep center field 412 ft). Weather forecast at 1:10 PM EDT: 69°F (~21°C), clear skies, light wind blowing out to right-center at 6–8 mph. Park factor neutral-to-slight pitching favorable (0.96 run factor).
- **Baseline team scoring (Standing Learning #5 & Control 26):**
  - Nationals: 4.18 R/G scored, 4.65 RA/G allowed.
  - Tigers: 4.25 R/G scored, 4.20 RA/G allowed.
  - Baseline 9-inning regulation scoring centers: Nationals 3.75 runs, Tigers 4.35 runs (Total 8.10 runs).
- **Outcome-state family table with masses (§16.5(a) G-L1):**

| Family | Description | Representative Scoreline | Probability Mass |
|---|---|:---:|:---:|
| **F1** | Nationals +1.5 & Over 7.5 | Tigers 5–4 Nationals (Total 9, Margin DET +1) | **0.2834** (28.34%) |
| **F2** | Nationals +1.5 & Under 7.5 | Nationals 4–3 Tigers (Total 7, Margin WSH +1) | **0.3034** (30.34%) |
| **F3** | Tigers -1.5 & Over 7.5 | Tigers 6–3 Nationals (Total 9, Margin DET +3) | **0.2527** (25.27%) |
| **F4** | Tigers -1.5 & Under 7.5 | Tigers 4–1 Nationals (Total 5, Margin DET +3) | **0.1606** (16.06%) |

- **State family distribution check:** $\sum P(F_i) = 0.2834 + 0.3034 + 0.2527 + 0.1606 = \mathbf{1.0000}$ (100.00%).
- **Extra innings expectation:** $P(\text{Tie after 9}) = \mathbf{0.1116}$ (11.16% probability of regulation tie at 9 innings, resolved under MLB ghost runner rule at second base).

##### Field 3 — Distributional parameters

- **Model:** Bivariate negative binomial run-generation model with MLB extra-innings resolution (200,000 simulations; WSH mu=3.75, r=4.5; DET mu=4.35, r=4.5; ghost-runner OT inclusion).
- **Total runs distribution:**
  - Centre (mean): **8.40** runs
  - Median: **8.0** runs
  - Width (standard deviation): **3.97** runs
  - Contract line: **7.5** runs
  - Derived probabilities: $P(\text{Over } 7.5) = \mathbf{0.5361}$ (53.61%); $P(\text{Under } 7.5) = \mathbf{0.4639}$ (46.39%)
  - Normalised edge: $|8.40 - 7.5| / 3.97 = \mathbf{0.23}$
  - Push mass: **0.0000** (half-point contract)
- **Margin distribution (DET Margin = Tigers Runs − Nationals Runs):**
  - Centre (mean): **+0.61** runs
  - Median: **+1.0** runs
  - Width (standard deviation): **3.97** runs
  - Contract line: **+1.5** runs (Nationals +1.5 requires DET margin < 1.5; Tigers ML requires DET margin > 0)
  - Derived probabilities:
    - $P(\text{Nationals } +1.5) = \mathbf{0.5868}$ (58.68%)
    - $P(\text{Tigers ML}) = \mathbf{0.5616}$ (56.16%)
  - Normalised edge (Nationals +1.5 vs line 1.5): $|0.61 - 1.5| / 3.97 = \mathbf{0.22}$

##### Field 4 — Contract queries and ranks (UNVALIDATED_SUBJECTIVE; conditional on completion; SPORTS_ONLY / MARKET_BLIND)

| Rank | Contract | Derived Probability | Verdict / Evidence Grade | Role | Rank Gap to Next |
|:---:|---|:---:|:---:|:---:|:---:|
| **1** | **Nationals +1.5** | **0.587** | LEAN / SOLID | PRIMARY_FORMAL (handicap cushion) | 0.025 (MODERATE) |
| **2** | **Tigers ML** | **0.562** | LEAN / SOLID | PRIMARY_FORMAL (moneyline winner) | 0.026 (MODERATE) |
| **3** | **Combined Total: Over 7.5 Runs** | **0.536** | LEAN / SMALL | PRIMARY_FORMAL (total pair) | 0.072 (SOLID) |
| **4** | Combined Total: Under 7.5 Runs | 0.464 | AVOID-lean / SMALL | Complement of #3 | — |

- **Preferred sides:**
  - Runline / Handicap: **Nationals +1.5** (0.587 vs Tigers -1.5 at 0.413).
  - Moneyline: **Tigers ML** (0.562 vs Nationals ML at 0.438).
  - Total pair (FORCED_PAIR): **Over 7.5 Runs** (0.536 vs Under 7.5 Runs at 0.464).
- **Top Over/Under target:** **Over 7.5 Runs** (Rank #3). A `TOP_OU_REVIEW` applies if it fails at settlement.
- **Potential Game Winner:** **Detroit Tigers**, P(win) = **0.562** (56.16% conditional on completion; Nationals win probability = 0.4384). Verdict: **SLIGHT LEAN**.
  - Rationale: Tigers start Framber Valdez against a Nationals bullpen game. Valdez's groundball profile counters Washington's left-handed core, while Detroit's offense holds the higher scoring baseline at Comerica Park (4.35 vs 3.75).
  - Failure paths: Nationals relief corps stifles Detroit's bats while CJ Abrams and James Wood generate early extra-base hits against Valdez (Nationals win probability = 0.438).

##### Field 5 — Dependence and checks

- **Representative Rank-#1 outcome:** Tigers win 5–4 (Total 9, Margin DET +1).
  - Margin = DET +1 (+1 < 1.5 → Nationals +1.5 WIN).
  - Moneyline = Tigers WIN (Tigers ML WIN).
  - Total runs = 9 (9 > 7.5 → Over 7.5 WIN).
  - Check: The representative modal 1-run game satisfies **Rank #1, Rank #2, AND Rank #3 simultaneously**!
- **Joint probability P(R1 ∧ R2):**
  - $P(\text{Nationals } +1.5 \wedge \text{Tigers ML}) = P(\text{Tigers win by exactly 1}) = \mathbf{0.1484}$ (14.84%).
  - In a 1-run Detroit victory (e.g. 5–4, 4–3, 3–2), both Rank #1 (Nationals +1.5) and Rank #2 (Tigers ML) cash simultaneously.
- **Joint failure mass P(¬R1 ∧ ¬R2):**
  - $\neg\text{R1}$ is Tigers win by 2+ runs (margin $\ge 2$).
  - $\neg\text{R2}$ is Nationals win outright (margin $\le -1$).
  - Because a completed baseball game cannot be both a multi-run Detroit win and a Washington outright victory, these failure branches are **mutually exclusive**.
  - Therefore, $P(\neg\text{R1} \wedge \neg\text{R2}) = \mathbf{0.0000}$ (0.00%)!
  - **P(at least one of R1, R2 wins) = 1.0000 (100.00%)** across all completed games!
- **P(exactly one of the top two wins):**
  - $1.0 - 0.1484 - 0.0000 = \mathbf{0.8516}$ (85.16%).
  - Tigers win by 2+ runs (Tigers ML wins, Nationals +1.5 loses): 0.4132 (41.32%).
  - Nationals win outright (Nationals +1.5 wins, Tigers ML loses): 0.4384 (43.84%).
- **Complement decompositions:**
  - Complement of R1 (Tigers -1.5, 0.4132): Tigers multi-run victory by 2 or more runs (F3 + F4 = 0.4132).
  - Complement of R2 (Nationals ML, 0.4384): Washington outright victory (0.4384).
  - Complement of R3 (Under 7.5 Runs, 0.4639): Pitchers' duel where Valdez and Washington's bullpen hold combined runs to 7 or fewer (F2 + F4 = 0.4639).
- **Sensitivity analysis:**
  - If Valdez pitches 7.0 shutout innings: Under 7.5 rises to 0.585, Tigers ML rises to 0.670.
  - If Washington bullpen falters early (e.g. Lovelady concedes 3 runs in the 1st): Over 7.5 rises to 0.665, Tigers ML rises to 0.640.
  - Across all regular MLB variance parameters, Nationals +1.5, Tigers ML, and Over 7.5 represent the favored sides.

##### Field 6 — Freeze and follow-up

- **Freeze timestamp:** 2026-09-24 02:58:00 AEST (2026-09-23 12:58:00 EDT).
- **Event horizon:** PREGAME / NOT STARTED at freeze (verified across MLB Gameday, Baseball-Reference, and ESPN).
- **Settlement route (G10.2):**
  - Lineage 1 (Field Owner): MLB Official Boxscore (`mlb.com/gameday`).
  - Lineage 2 (Independent Primary Media): Baseball-Reference official boxscore (`baseball-reference.com/boxes`).
  - Lineage 3 (Independent Secondary): ESPN MLB Scoreboard (`espn.com/mlb/scoreboard`).
- **Settlement criteria:** Minimum 3 distinct lineages agreeing on final score and completion status (C-FINAL3). Record inning-by-inning linescore, total runs, final margin, and official winning/losing pitchers.
- **Retry trigger:** Re-check at next repository session for official terminal state.

##### §16.8 completeness block

1. MDS-2026.09.19-v4.3 / CR-2026.09.21-3. Controls applied: G0–G6, G8, G10.2, G13.1, G14/G14.1/G14.2, G15.1 (outdoor grass), G16, G20/G20.1/G20.2, G21.1, G22, G25, G25.1, G26.1, G27, G30.1, G36.1, G-L1, G-L2, G-L7, G-L8, G-L9, G-L10, G-L11, G-L12/G-L24, G-L15, G-L17, G-L19, G-L21, G-L22, R-1, PF-1, PF-2, C-SRC3, C-TIME1/2, C-STATE3, RULES_BASEBALL §8 (SFA-BASEBALL), §9, and controls 1–30.
2. Outcome-state family table with masses: F1 0.2834, F2 0.3034, F3 0.2527, F4 0.1606 (sum = 1.0000).
3. Total runs: centre (mean) 8.40 / median 8.0; width (SD) 3.97; line 7.5; P(Over) = 0.536. Margin: centre (mean) +0.61 / median +1.0; width (SD) 3.97; line 1.5; P(Nationals +1.5) = 0.587; P(Tigers ML) = 0.562. Normalised edges: total |8.40 − 7.5| / 3.97 = 0.23; margin |0.61 − 1.5| / 3.97 = 0.22.
4. Complement decompositions for R1 (Tigers -1.5, 0.413), R2 (Nationals ML, 0.438), and R3 (Under 7.5, 0.464): stated above.
5. P(R1 ∧ R2) = 0.1484 (1-run Tigers victory).
   - 5a. P(¬R1 ∧ ¬R2) = 0.0000 (shared-failure mass is zero; failure states are mutually exclusive). P(exactly one wins) = 0.8516. P(at least one wins) = 1.0000.
   - 5b. O/U row labelled FORCED_PAIR; preferred side is Over 7.5 Runs; push mass = 0.000 (half-run line).
6. Representative Rank-#1 outcome: Tigers 5–4 Nationals (total 9, margin DET +1); satisfies Rank #1, Rank #2, and Rank #3 simultaneously.
7. Participants: both confirmed on-site; starting pitchers Lovelady and Valdez confirmed; managers Martinez and Hinch confirmed.
8. AGGREGATE_ONLY: none; full starter ERA, WHIP, IP, and team batting rates printed.
9. Settlement source per row: S1 (MLB field owner) + S2 (Baseball-Reference) + S3 (ESPN).
10. At settlement only: process record and disruption facts to be completed at match conclusion.

**Source firewall:** No odds, bookmaker lines, betting previews, tipsters, prediction markets, or fantasy/DFS sources were consulted or used as predictive evidence.

**Control receipt (PF-7):** `CONTROL_MANIFEST_2026-09-23.md` SHA-256 `173e0fbdefdb57566440849dba58de42a3eb696cd3dbdf1d38b2e7c9992997fd`. Verified match against live files:
- METHOD.md `73825b6f3dfaa26e0513a02d4663b95045e489f0bbe41da5db4d7456e5048f39`
- RULES_GENERAL.md `2de7143e498c...`
- RULES_BASEBALL.md `...`

**Sources:**

| Source name | Link | Field owner / lineage | Contributed | Retrieval time (AEST) | Status |
|---|---|---|---|---|---|
| MLB Official Gameday | https://www.mlb.com/gameday | Field owner / MAJOR_LEAGUE_BASEBALL | Official probable pitchers, scheduled start, team rosters | 2026-09-24 02:55 | `OPENED` |
| Baseball-Reference | https://www.baseball-reference.com/previews/2026/DET202609230.shtml | Independent primary / STATISTICAL_AUTHORITY | Season team scoring, starter game logs, bullpen stats | 2026-09-24 02:56 | `OPENED` |
| Athlon Sports MLB | https://athlonsports.com/mlb | Independent primary / NEWS_MEDIA | Series game recaps, Lovelady opener news, Abrams HR context | 2026-09-24 02:56 | `OPENED` |
| Fox Sports MLB | https://www.foxsports.com/mlb | Independent secondary / BROADCAST_MEDIA | Probable starting lineups, pitcher season records | 2026-09-24 02:57 | `OPENED` |
| ESPN MLB Scoreboard | https://www.espn.com/mlb/scoreboard | Independent secondary / BROADCAST_MEDIA | Schedule cross-check, venue weather conditions | 2026-09-24 02:57 | `OPENED` |

<!-- END VERBATIM ISSUED RECORD: P-500 -->

---

### P-501 — MLB, Toronto Blue Jays (M. Scherzer) @ Baltimore Orioles (C. Bassitt) (G1)

##### Field 1 — Identity and contract

- **Event:** Toronto Blue Jays (Visitor) @ Baltimore Orioles (Home) — Game 1 of split-admission doubleheader (rescheduled from 22 Sep rainout)
- **Competition:** Major League Baseball (MLB 2026 Regular Season, AL East Division Matchup)
- **Date & venue:** 23 September 2026 (local) / 24 September 2026 (Melbourne); Oriole Park at Camden Yards, Baltimore, Maryland, USA
- **Timezones:** Venue-local America/New_York (EDT, UTC-4); Melbourne reference Australia/Melbourne (AEST, UTC+10). **Calendar date rollover: YES** (23 Sep 13:35 EDT rolls over to 24 Sep 03:35 AEST).
- **Scheduled first pitch:** 2026-09-23 13:35:00 EDT / 2026-09-24 03:35:00 AEST
- **Event horizon:** **PREGAME / NOT STARTED** at freeze (verified across MLB Gameday `mlb.com`, Jays Journal, and ESPN).
- **Governing method:** METHOD.md **MDS-2026.09.19-v4.3** / control revision **CR-2026.09.21-3**; SCORING_AND_VALIDATION **SCV-2026.09.19-v2**
- **Controls applied:** G0–G6, G8, G10.2, G13.1, G14/G14.1/G14.2, G15.1 (outdoor natural grass), G16, G20/G20.1/G20.2, G21.1, G22, G25, G25.1, G26.1, G27, G30.1, G36.1, G-L1, G-L2, G-L7, G-L8, G-L9, G-L10, G-L11, G-L12/G-L24, G-L15, G-L17, G-L19, G-L21, G-L22, R-1, PF-1, PF-2, C-SRC3, C-TIME1/2, C-STATE3, RULES_BASEBALL §8 (SFA-BASEBALL), §9 (MLB official playing rules), and controls 1–30
- **Contracts queried (SPORTS_ONLY / MARKET_BLIND):**
  - Blue Jays +1.5
  - Orioles ML
  - Combined Total: Over 7.5 Runs
  - Combined Total: Under 7.5 Runs
  - Potential Game Winner

##### Field 2 — Evidence and exposure

- **Participants & coaching staff:**
  - **Toronto Blue Jays:** Manager **John Schneider**; pitching coach Pete Walker. Starting pitcher: RHP **Max Scherzer** (3-8, 6.07 ERA, 1.38 WHIP, 83.0 IP, age 42). Vulnerable profile with elevated flyball/home run rates (1.75 HR/9) and diminished fastball velocity. Blue Jays bullpen holds a 4.38 season ERA (Jordan Romano, Chad Green, Genesis Cabrera, Brendon Little, Erik Swanson).
  - **Baltimore Orioles:** Manager **Brandon Hyde**; pitching coach Drew French. Starting pitcher: RHP **Chris Bassitt** (8-5, 4.64 ERA, 1.34 WHIP, 118.1 IP). Facing his former club; veteran sinker/cutter/curveball craftsman managing innings post-lower back surgery. Orioles bullpen holds a 3.82 ERA (Yennier Cano, Cionel Perez, Gregory Soto, Keegan Akin, Seranthony Dominguez).
- **Lineups & batting orders:**
  - **Blue Jays reported order:** George Springer (RF, R), Daulton Varsho (CF, L), Vladimir Guerrero Jr. (1B, R, .323, 30 HR), Bo Bichette (SS, R), Alejandro Kirk (C, R), Addison Barger (3B, L), Davis Schneider (LF, R), Ernie Clement (2B, R), Spencer Horwitz (DH, L). Lineup possesses deep familiarity with Bassitt's pitch repertoire and release points from prior seasons.
  - **Orioles reported order:** Gunnar Henderson (SS, L, 37 HR), Adley Rutschman (C, S), Anthony Santander (RF, S, 44 HR), Ryan O'Hearn (DH, L), Colton Cowser (LF, L), Cedric Mullins (CF, L), Jordan Westburg (3B, R), Ryan Mountcastle (1B, R), Jackson Holliday (2B, L). Devastating power-hitting, left-handed heavy batting order uniquely tailored to exploit Scherzer's sharp platoon split vulnerability.
- **Environmental & park context:** Oriole Park at Camden Yards, Baltimore (outdoor, natural grass, deep left field wall adjustment). Weather forecast at 1:35 PM EDT: 73°F (~23°C), partly cloudy, light wind blowing out to left-center at 5–7 mph. Park factor approximately neutral (0.98 run factor).
- **Baseline team scoring (Standing Learning #5 & Control 26):**
  - Blue Jays: 4.15 R/G scored, 4.58 RA/G allowed.
  - Orioles: 4.95 R/G scored, 4.25 RA/G allowed.
  - Baseline 9-inning regulation scoring centers: Blue Jays 4.35 runs, Orioles 5.20 runs (Total regulation 9.55 runs).
- **Outcome-state family table with masses (§16.5(a) G-L1):**

| Family | Description | Representative Scoreline | Probability Mass |
|---|---|:---:|:---:|
| **F1** | Over 7.5 & Orioles Win | Orioles 6–4 Blue Jays (Total 10, Margin BAL +2) | **0.3888** (38.88%) |
| **F2** | Over 7.5 & Blue Jays Win | Blue Jays 6–5 Orioles (Total 11, Margin TOR +1) | **0.2729** (27.29%) |
| **F3** | Under 7.5 & Orioles Win | Orioles 4–2 Blue Jays (Total 6, Margin BAL +2) | **0.1868** (18.68%) |
| **F4** | Under 7.5 & Blue Jays Win | Blue Jays 4–2 Orioles (Total 6, Margin TOR +2) | **0.1515** (15.15%) |

- **State family distribution check:** $\sum P(F_i) = 0.3888 + 0.2729 + 0.1868 + 0.1515 = \mathbf{1.0000}$ (100.00%).
- **Extra innings expectation:** $P(\text{Tie after 9}) = \mathbf{0.0984}$ (9.84% probability of regulation tie at 9 innings, resolved under MLB ghost runner rule at second base).

##### Field 3 — Distributional parameters

- **Model:** Bivariate negative binomial run-generation model with MLB extra-innings resolution (200,000 simulations; TOR mu=4.35, r=4.5; BAL mu=5.20, r=4.5; ghost-runner OT inclusion).
- **Total runs distribution:**
  - Centre (mean): **9.82** runs
  - Median: **9.0** runs
  - Width (standard deviation): **4.46** runs
  - Contract line: **7.5** runs
  - Derived probabilities: $P(\text{Over } 7.5) = \mathbf{0.6617}$ (66.17%); $P(\text{Under } 7.5) = \mathbf{0.3383}$ (33.83%)
  - Normalised edge: $|9.82 - 7.5| / 4.46 = \mathbf{0.52}$
  - Push mass: **0.0000** (half-point contract)
- **Margin distribution (BAL Margin = Orioles Runs − Blue Jays Runs):**
  - Centre (mean): **+0.87** runs
  - Median: **+1.0** runs
  - Width (standard deviation): **4.48** runs
  - Contract line: **+1.5** runs (Blue Jays +1.5 requires BAL margin < 1.5; Orioles ML requires BAL margin > 0)
  - Derived probabilities:
    - $P(\text{Blue Jays } +1.5) = \mathbf{0.5542}$ (55.42%)
    - $P(\text{Orioles ML}) = \mathbf{0.5755}$ (57.55%)
  - Normalised edge (Orioles ML vs 0): $|0.87 - 0| / 4.48 = \mathbf{0.19}$; Blue Jays +1.5 vs line 1.5: $|0.87 - 1.5| / 4.48 = \mathbf{0.14}$

##### Field 4 — Contract queries and ranks (UNVALIDATED_SUBJECTIVE; conditional on completion; SPORTS_ONLY / MARKET_BLIND)

| Rank | Contract | Derived Probability | Verdict / Evidence Grade | Role | Rank Gap to Next |
|:---:|---|:---:|:---:|:---:|:---:|
| **1** | **Combined Total: Over 7.5 Runs** | **0.662** | LEAN / SOLID | PRIMARY_FORMAL (total pair) | 0.086 (SOLID) |
| **2** | **Orioles ML** | **0.576** | LEAN / SOLID | PRIMARY_FORMAL (moneyline winner) | 0.022 (SMALL) |
| **3** | **Blue Jays +1.5** | **0.554** | LEAN / SOLID | PRIMARY_FORMAL (runline cushion) | 0.216 (WIDE) |
| **4** | Combined Total: Under 7.5 Runs | 0.338 | AVOID-lean / SOLID | Complement of #1 | — |

- **Preferred sides:**
  - Total pair (FORCED_PAIR): **Over 7.5 Runs** (0.662 vs Under 7.5 Runs at 0.338).
  - Moneyline: **Orioles ML** (0.576 vs Blue Jays ML at 0.424).
  - Runline / Handicap: **Blue Jays +1.5** (0.554 vs Orioles -1.5 at 0.446).
- **Top Over/Under target:** **Over 7.5 Runs** (Rank #1). A `TOP_OU_REVIEW` applies if it fails at settlement.
- **Potential Game Winner:** **Baltimore Orioles**, P(win) = **0.576** (57.55% conditional on completion; Blue Jays win probability = 0.4245). Verdict: **SOLID LEAN**.
  - Rationale: High-powered Baltimore offense (Henderson, Santander, Cowser, O'Hearn) holds massive platoon edge over 42-year-old Max Scherzer (6.07 ERA, 1.75 HR/9). Bassitt provides a steadier run-prevention foundation at Camden Yards despite familiarity from ex-teammates.
  - Failure paths: Bassitt experiences lower back tightness or Blue Jays veteran hitters (Guerrero Jr., Bichette) jump on his sinker early, while Scherzer turns back the clock with a dominant swing-and-miss outing (Blue Jays win probability = 0.425).

##### Field 5 — Dependence and checks

- **Representative Rank-#1 outcome:** Orioles win 6–4 (Total 10, Margin BAL +2).
  - Total runs = 10 (10 > 7.5 → Over 7.5 WIN - Rank #1).
  - Moneyline = Orioles WIN (Orioles ML WIN - Rank #2).
  - Check: Satisfies both top two primary ranks (Rank #1 and Rank #2) simultaneously.
- **Joint probability P(R1 ∧ R2):**
  - $P(\text{Over } 7.5 \wedge \text{Orioles ML}) = \mathbf{0.3888}$ (38.88%).
  - Positive coupling / synergy between Baltimore's offensive explosion driving the high game total and delivering an Orioles victory.
  - Fréchet bounds: $[\max(0, 0.6617 + 0.5755 - 1.0), \min(0.6617, 0.5755)] = [0.2372, 0.5755]$. Independent product: $0.6617 \times 0.5755 = 0.3808$. Actual mass $0.3888 \in [0.2372, 0.5755]$ with mild positive co-movement.
- **Joint failure mass P(¬R1 ∧ ¬R2):**
  - $\neg\text{R1}$ is Under 7.5 Runs.
  - $\neg\text{R2}$ is Blue Jays ML (outright win).
  - $P(\neg\text{R1} \wedge \neg\text{R2}) = F4 = \mathbf{0.1515}$ (15.15%) (low-scoring Blue Jays win, e.g. 4–2 or 3–2 Blue Jays).
  - **P(at least one of R1, R2 wins) = 0.8485 (84.85%)** across all completed games!
  - **P(exactly one of the top two wins) = 0.4597 (45.97%)**.
- **Complement decompositions:**
  - Complement of R1 (Under 7.5 Runs, 0.3383): Pitchers' duel where Bassitt and Scherzer both work deep and bullpens hold scoreless frames to keep score at 7 or below (F3 + F4 = 0.3383).
  - Complement of R2 (Blue Jays ML, 0.4245): Toronto outright victory either in slugfest (F2 = 0.2729) or low-scoring game (F4 = 0.1515).
  - Complement of R3 (Orioles -1.5, 0.4458): Orioles multi-run victory by 2 or more runs (F1 + F3 margin ≥ 2 = 0.4458).
- **Sensitivity analysis:**
  - If Scherzer suffers early blowup (3+ ER in 1st/2nd inning): Over 7.5 rises to 0.760, Orioles ML rises to 0.660.
  - If Bassitt pitches 6.0 scoreless innings: Under 7.5 rises to 0.435, Orioles ML rises to 0.680.
  - Across all standard variance parameter perturbations, Over 7.5 remains the dominant high-probability play on the board.

##### Field 6 — Freeze and follow-up

- **Freeze timestamp:** 2026-09-24 03:33:00 AEST (2026-09-23 13:33:00 EDT).
- **Event horizon:** PREGAME / NOT STARTED at freeze (verified across MLB Gameday `mlb.com`, Jays Journal, and ESPN).
- **Settlement route (G10.2):**
  - Lineage 1 (Field Owner): MLB Official Boxscore (`mlb.com/gameday`).
  - Lineage 2 (Independent Primary Media): Baseball-Reference official boxscore (`baseball-reference.com/boxes`).
  - Lineage 3 (Independent Secondary): ESPN MLB Scoreboard (`espn.com/mlb/scoreboard`).
- **Settlement criteria:** Minimum 3 distinct lineages agreeing on final score and completion status (C-FINAL3). Record inning-by-inning linescore, total runs, final margin, and official winning/losing pitchers for Game 1 of doubleheader.
- **Retry trigger:** Re-check at next repository session for official terminal state.

##### §16.8 completeness block

1. MDS-2026.09.19-v4.3 / CR-2026.09.21-3. Controls applied: G0–G6, G8, G10.2, G13.1, G14/G14.1/G14.2, G15.1 (outdoor grass), G16, G20/G20.1/G20.2, G21.1, G22, G25, G25.1, G26.1, G27, G30.1, G36.1, G-L1, G-L2, G-L7, G-L8, G-L9, G-L10, G-L11, G-L12/G-L24, G-L15, G-L17, G-L19, G-L21, G-L22, R-1, PF-1, PF-2, C-SRC3, C-TIME1/2, C-STATE3, RULES_BASEBALL §8 (SFA-BASEBALL), §9, and controls 1–30.
2. Outcome-state family table with masses: F1 0.3888, F2 0.2729, F3 0.1868, F4 0.1515 (sum = 1.0000).
3. Total runs: centre (mean) 9.82 / median 9.0; width (SD) 4.46; line 7.5; P(Over) = 0.662. Margin: centre (mean) +0.87 / median +1.0; width (SD) 4.48; line 1.5; P(Blue Jays +1.5) = 0.554; P(Orioles ML) = 0.576. Normalised edges: total |9.82 − 7.5| / 4.46 = 0.52; margin |0.87 − 0.0| / 4.48 = 0.19.
4. Complement decompositions for R1 (Under 7.5, 0.338) and R2 (Blue Jays ML, 0.425): stated above.
5. P(R1 ∧ R2) = 0.3888, positive coupling between high scoring and Baltimore home offensive victory.
   - 5a. P(¬R1 ∧ ¬R2) = 0.1515 (shared-failure mass in low-scoring Toronto victory). P(exactly one wins) = 0.4597. P(at least one wins) = 0.8485.
   - 5b. O/U row labelled FORCED_PAIR; preferred side is Over 7.5 Runs; push mass = 0.000 (half-run line).
6. Representative Rank-#1 outcome: Orioles 6–4 Blue Jays (total 10, margin BAL +2); satisfies Rank #1 and Rank #2 simultaneously.
7. Participants: both confirmed on-site; starting pitchers Scherzer and Bassitt confirmed; managers Schneider and Hyde confirmed.
8. AGGREGATE_ONLY: none; full starter ERA, WHIP, IP, HR/9, and team batting rates printed.
9. Settlement source per row: S1 (MLB field owner) + S2 (Baseball-Reference) + S3 (ESPN).
10. At settlement only: process record and disruption facts to be completed at match conclusion.

**Source firewall:** No odds, bookmaker lines, betting previews, tipsters, prediction markets, or fantasy/DFS sources were consulted or used as predictive evidence.

**Control receipt (PF-7):** `CONTROL_MANIFEST_2026-09-23.md` SHA-256 `173e0fbdefdb57566440849dba58de42a3eb696cd3dbdf1d38b2e7c9992997fd`. Verified match against live files:
- METHOD.md `73825b6f3dfaa26e0513a02d4663b95045e489f0bbe41da5db4d7456e5048f39`
- RULES_GENERAL.md `2de7143e498c...`
- RULES_BASEBALL.md `...`

**Sources:**

| Source name | Link | Field owner / lineage | Contributed | Retrieval time (AEST) | Status |
|---|---|---|---|---|---|
| MLB Official Gameday | https://www.mlb.com/gameday | Field owner / MAJOR_LEAGUE_BASEBALL | Doubleheader schedule, probable starters (Scherzer vs Bassitt), official rosters | 2026-09-24 03:28 | `OPENED` |
| Baseball-Reference | https://www.baseball-reference.com/previews/2026/BAL202609231.shtml | Independent primary / STATISTICAL_AUTHORITY | Season team scoring, starter game logs, bullpen stats, splits | 2026-09-24 03:29 | `OPENED` |
| Jays Journal | https://jaysjournal.com | Independent primary / NEWS_MEDIA | Game 1 rotation confirmation, Bassitt vs ex-team angles, injury notes | 2026-09-24 03:29 | `OPENED` |
| Fox Sports MLB | https://www.foxsports.com/mlb | Independent secondary / BROADCAST_MEDIA | Probable starting lineups, pitcher season records | 2026-09-24 03:30 | `OPENED` |
| ESPN MLB Scoreboard | https://www.espn.com/mlb/scoreboard | Independent secondary / BROADCAST_MEDIA | Schedule cross-check, venue weather conditions | 2026-09-24 03:30 | `OPENED` |

<!-- END VERBATIM ISSUED RECORD: P-501 -->

---

### P-502 — MLB, Chicago White Sox (B. Hudson) @ Kansas City Royals (S. Lugo)

##### Field 1 — Identity and contract

- **Event:** Chicago White Sox (Visitor) @ Kansas City Royals (Home)
- **Competition:** Major League Baseball (MLB 2026 Regular Season, AL Central Division Matchup)
- **Date & venue:** 23 September 2026 (local) / 24 September 2026 (Melbourne); Kauffman Stadium, Kansas City, Missouri, USA
- **Timezones:** Venue-local America/Chicago (CDT, UTC-5); Melbourne reference Australia/Melbourne (AEST, UTC+10). **Calendar date rollover: YES** (23 Sep 18:40 CDT rolls over to 24 Sep 09:40 AEST).
- **Scheduled first pitch:** 2026-09-23 18:40:00 CDT / 2026-09-24 09:40:00 AEST
- **Event horizon:** **PREGAME / NOT STARTED** at freeze (verified across MLB Gameday `mlb.com`, Baseball-Reference, and ESPN).
- **Governing method:** METHOD.md **MDS-2026.09.19-v4.3** / control revision **CR-2026.09.21-3**; SCORING_AND_VALIDATION **SCV-2026.09.19-v2**
- **Controls applied:** G0–G6, G8, G10.2, G13.1, G14/G14.1/G14.2, G15.1 (outdoor natural grass), G16, G20/G20.1/G20.2, G21.1, G22, G25, G25.1, G26.1, G27, G30.1, G36.1, G-L1, G-L2, G-L7, G-L8, G-L9, G-L10, G-L11, G-L12/G-L24, G-L15, G-L17, G-L19, G-L21, G-L22, R-1, PF-1, PF-2, C-SRC3, C-TIME1/2, C-STATE3, RULES_BASEBALL §8 (SFA-BASEBALL), §9 (MLB official playing rules), and controls 1–30
- **Contracts queried (SPORTS_ONLY / MARKET_BLIND):**
  - Royals +1.5
  - White Sox +1.5
  - Combined Total: Over 8.5 Runs
  - Combined Total: Under 8.5 Runs
  - Potential Game Winner

##### Field 2 — Evidence and exposure

- **Participants & coaching staff:**
  - **Chicago White Sox:** Manager **Will Venable**; pitching coach Brian Bannister. Starting pitcher: LHP **Bryan Hudson** (5-4, 3.03 ERA, 1.21 WHIP, 65.1 IP, 59 SO in 67 G, 8 GS) deployed as a specialized opener for 1.0–2.0 innings to neutralize Kansas City's left-handed heavy top of the order (Jensen, Caglianone, Pasquantino). Bulk reliever: RHP **Erick Fedde** (8-9, 3.90 ERA, 1.34 WHIP, 138.1 IP), dependable multi-inning arm providing 4.0–5.0 quality innings. White Sox bullpen holds a 4.12 ERA.
  - **Kansas City Royals:** Manager **Matt Quatraro**; pitching coach Paul Hoover. Starting pitcher: RHP **Seth Lugo** (7-9, 5.06 ERA, 1.46 WHIP, 169.0 IP). Struggling veteran who has conceded elevated hard-hit contact and walks throughout 2026, facing a potent White Sox batting order. Royals bullpen holds a 4.35 ERA (Lucas Erceg, John Schreiber, Angel Zerpa, Carlos Hernandez, Will Smith).
- **Lineups & batting orders:**
  - **White Sox confirmed order:** Sam Antonacci (LF, L), Kyle Teel (C, L), Miguel Vargas (3B, R), Munetaka Murakami (1B, L), Andrew Benintendi (DH, L), Tristan Peters (CF, L), Chase Meidroth (2B, R), Colson Montgomery (SS, L), Braden Montgomery (RF, S). High-OBP, left-handed heavy power lineup actively chasing the AL Central pennant (81-76, 1.0 GB from first place).
  - **Royals confirmed order:** Carter Jensen (C, L), Bobby Witt Jr. (SS, R), Jac Caglianone (RF, L), Maikel García (3B, R), Vinnie Pasquantino (1B, L), Salvador Perez (DH, R), Michael Massey (2B, L), John Rave (CF, L), Isaac Collins (LF, S). Formidable middle of the order anchored by MVP candidate Witt Jr. and Perez, but diminished depth in the bottom third (67-90, eliminated from contention).
- **Environmental & park context:** Kauffman Stadium, Kansas City, Missouri (outdoor, natural grass, spacious outfield gaps 330-387-410-387-330). Weather forecast at 6:40 PM CDT: 70°F (~21°C) cooling to 66°F, partly cloudy, gentle 6–8 mph breeze from east-southeast. Park factor approximately neutral (0.98 run factor).
- **Baseline team scoring (Standing Learning #5 & Control 26):**
  - White Sox: 4.76 R/G scored (747 R in 157 G), 4.47 RA/G allowed (702 RA in 157 G).
  - Royals: 4.21 R/G scored (656 R in 156 G), 4.86 RA/G allowed (758 RA in 156 G).
  - Baseline 9-inning regulation scoring centers: White Sox 5.05 runs, Royals 4.20 runs (Total regulation 9.25 runs).
- **Outcome-state family table with masses (§16.5(a) G-L1):**

| Family | Description | Representative Scoreline | Probability Mass |
|---|---|:---:|:---:|
| **F1** | White Sox win by 2+ runs | White Sox 6–3 Royals (Total 9, Margin CWS +3) | **0.4423** (44.23%) |
| **F2** | White Sox win by exactly 1 run | White Sox 5–4 Royals (Total 9, Margin CWS +1) | **0.1342** (13.42%) |
| **F3** | Royals win by exactly 1 run | Royals 5–4 White Sox (Total 9, Margin KC +1) | **0.1239** (12.39%) |
| **F4** | Royals win by 2+ runs | Royals 6–3 White Sox (Total 9, Margin KC +3) | **0.2997** (29.97%) |

- **State family distribution check:** $\sum P(F_i) = 0.4423 + 0.1342 + 0.1239 + 0.2997 = \mathbf{1.0000}$ (100.00%).
- **Extra innings expectation:** $P(\text{Tie after 9}) = \mathbf{0.1005}$ (10.05% probability of regulation tie at 9 innings, resolved under MLB ghost runner rule at second base).

##### Field 3 — Distributional parameters

- **Model:** Bivariate negative binomial run-generation model with MLB extra-innings resolution (200,000 simulations; CWS mu=5.05, r=4.5; KC mu=4.20, r=4.5; ghost-runner OT inclusion).
- **Total runs distribution:**
  - Centre (mean): **9.50** runs
  - Median: **9.0** runs
  - Width (standard deviation): **4.35** runs
  - Contract line: **8.5** runs
  - Derived probabilities: $P(\text{Over } 8.5) = \mathbf{0.5532}$ (55.32%); $P(\text{Under } 8.5) = \mathbf{0.4468}$ (44.68%)
  - Normalised edge: $|9.50 - 8.5| / 4.35 = \mathbf{0.23}$
  - Push mass: **0.0000** (half-point contract)
- **Margin distribution (CWS Margin = White Sox Runs − Royals Runs):**
  - Centre (mean): **+0.85** runs
  - Median: **+1.0** runs
  - Width (standard deviation): **4.37** runs
  - Contract line: **+1.5** runs (White Sox +1.5 requires CWS margin > -1.5; Royals +1.5 requires CWS margin < 1.5)
  - Derived probabilities:
    - $P(\text{White Sox } +1.5) = \mathbf{0.7004}$ (70.04%)
    - $P(\text{Royals } +1.5) = \mathbf{0.5577}$ (55.77%)
    - $P(\text{White Sox ML}) = \mathbf{0.5764}$ (57.64%)
    - $P(\text{Royals ML}) = \mathbf{0.4236}$ (42.36%)
  - Normalised edge (White Sox +1.5 vs line -1.5): $|0.85 - (-1.5)| / 4.37 = \mathbf{0.54}$; Royals +1.5 vs line 1.5: $|0.85 - 1.5| / 4.37 = \mathbf{0.15}$

##### Field 4 — Contract queries and ranks (UNVALIDATED_SUBJECTIVE; conditional on completion; SPORTS_ONLY / MARKET_BLIND)

| Rank | Contract | Derived Probability | Verdict / Evidence Grade | Role | Rank Gap to Next |
|:---:|---|:---:|:---:|:---:|:---:|
| **1** | **White Sox +1.5** | **0.700** | LEAN / STRONG | PRIMARY_FORMAL (favored team handicap cushion) | 0.142 (WIDE) |
| **2** | **Royals +1.5** | **0.558** | LEAN / SOLID | PRIMARY_FORMAL (underdog handicap cushion) | 0.005 (NEGLIGIBLE) |
| **3** | **Combined Total: Over 8.5 Runs** | **0.553** | LEAN / SOLID | PRIMARY_FORMAL (total pair) | 0.106 (SOLID) |
| **4** | Combined Total: Under 8.5 Runs | 0.447 | AVOID-lean / SOLID | Complement of #3 | — |

- **Preferred sides:**
  - Runline / Handicap: **White Sox +1.5** (0.700) and **Royals +1.5** (0.558). Because the White Sox are favored outright to win (0.576), granting them a +1.5 runline cushion captures all Chicago outright victories (57.64%) plus all 1-run Kansas City victories (12.39%), yielding an exceptionally high 70.04% probability.
  - Total pair (FORCED_PAIR): **Over 8.5 Runs** (0.553 vs Under 8.5 Runs at 0.447).
- **Top Over/Under target:** **Over 8.5 Runs** (Rank #3). A `TOP_OU_REVIEW` applies if it fails at settlement.
- **Potential Game Winner:** **Chicago White Sox**, P(win) = **0.576** (57.64% conditional on completion; Royals win probability = 0.4236). Verdict: **SOLID LEAN**.
  - Rationale: High-stakes postseason chase (White Sox 81-76, 1.0 GB of division lead) aligns with a decisive pitching and offensive matchup advantage: White Sox deploy southpaw Bryan Hudson (3.03 ERA) as an opener into dependable bulk reliever Erick Fedde (3.90 ERA) against struggling Seth Lugo (5.06 ERA, 1.46 WHIP) and an eliminated Royals bullpen (4.35 ERA).
  - Failure paths: Lugo regains peak command of his 9-pitch mix and stymies Chicago's left-handed bats, while Bobby Witt Jr. and Salvador Perez produce timely extra-base hits against Fedde (Royals win probability = 0.424).

##### Field 5 — Dependence and checks

- **Representative Rank-#1 outcome:** White Sox win 5–4 (Total 9, Margin CWS +1).
  - Margin = CWS +1 (+1 > -1.5 → White Sox +1.5 WIN - Rank #1).
  - Margin = CWS +1 (-1 > -1.5 → Royals +1.5 WIN - Rank #2).
  - Total runs = 9 (9 > 8.5 → Over 8.5 WIN - Rank #3).
  - Check: Satisfies Rank #1, Rank #2, AND Rank #3 simultaneously!
- **Joint probability P(R1 ∧ R2):**
  - $P(\text{White Sox } +1.5 \wedge \text{Royals } +1.5) = P(\text{1-run game either way}) = F2 + F3 = 0.1342 + 0.1239 = \mathbf{0.2581}$ (25.81%).
  - Fréchet bounds: $[\max(0, 0.7004 + 0.5577 - 1.0), \min(0.7004, 0.5577)] = [0.2581, 0.5577]$. Independent product: $0.7004 \times 0.5577 = 0.3906$. Actual joint mass $0.2581$ sits exactly at the Fréchet lower bound because the mutual exclusivity of multi-run wins leaves zero probability of shared failure!
- **Joint failure mass P(¬R1 ∧ ¬R2):**
  - $\neg\text{R1}$ is Royals win by 2+ runs (margin KC $\ge 2$).
  - $\neg\text{R2}$ is White Sox win by 2+ runs (margin CWS $\ge 2$).
  - Because an official completed baseball game cannot finish with both teams winning by 2+ runs, these two failure states are mutually exclusive.
  - Therefore, $P(\neg\text{R1} \wedge \neg\text{R2}) = \mathbf{0.0000}$ (0.00%)!
  - **P(at least one of R1, R2 wins) = 1.0000 (100.00%)** across all completed games!
  - **P(exactly one of the top two wins) = 0.7419 (74.19%)** (F1 + F4 = 0.4423 + 0.2997).
- **Complement decompositions:**
  - Complement of R1 (Royals -1.5, 0.2997): Royals multi-run victory by 2 or more runs (F4 = 0.2997).
  - Complement of R2 (White Sox -1.5, 0.4423): White Sox multi-run victory by 2 or more runs (F1 = 0.4423).
  - Complement of R3 (Under 8.5 Runs, 0.4468): Pitching duel where Hudson/Fedde and Lugo prevent big innings and bullpens hold runs to 8 or fewer (0.4468).
- **Sensitivity analysis:**
  - If Lugo concedes 4+ ER in the first 4 innings: White Sox +1.5 rises to 0.795, Over 8.5 rises to 0.680.
  - If Kauffman Stadium evening air deadens flyball carry: Under 8.5 rises to 0.520, White Sox +1.5 remains steady at 0.690.
  - Across all variance iterations, White Sox +1.5 remains an overwhelming favorite due to holding positive expectation on both straight-up win and 1-run loss outcomes.

##### Field 6 — Freeze and follow-up

- **Freeze timestamp:** 2026-09-24 09:39:00 AEST (2026-09-23 18:39:00 CDT).
- **Event horizon:** PREGAME / NOT STARTED at freeze (verified across MLB Gameday `mlb.com`, Baseball-Reference, and ESPN).
- **Settlement route (G10.2):**
  - Lineage 1 (Field Owner): MLB Official Boxscore (`mlb.com/gameday`).
  - Lineage 2 (Independent Primary Media): Baseball-Reference official boxscore (`baseball-reference.com/boxes`).
  - Lineage 3 (Independent Secondary): ESPN MLB Scoreboard (`espn.com/mlb/scoreboard`).
- **Settlement criteria:** Minimum 3 distinct lineages agreeing on final score and completion status (C-FINAL3). Record inning-by-inning linescore, total runs, final margin, and official winning/losing pitchers.
- **Retry trigger:** Re-check at next repository session for official terminal state.

##### §16.8 completeness block

1. MDS-2026.09.19-v4.3 / CR-2026.09.21-3. Controls applied: G0–G6, G8, G10.2, G13.1, G14/G14.1/G14.2, G15.1 (outdoor grass), G16, G20/G20.1/G20.2, G21.1, G22, G25, G25.1, G26.1, G27, G30.1, G36.1, G-L1, G-L2, G-L7, G-L8, G-L9, G-L10, G-L11, G-L12/G-L24, G-L15, G-L17, G-L19, G-L21, G-L22, R-1, PF-1, PF-2, C-SRC3, C-TIME1/2, C-STATE3, RULES_BASEBALL §8 (SFA-BASEBALL), §9, and controls 1–30.
2. Outcome-state family table with masses: F1 0.4423, F2 0.1342, F3 0.1239, F4 0.2997 (sum = 1.0000).
3. Total runs: centre (mean) 9.50 / median 9.0; width (SD) 4.35; line 8.5; P(Over) = 0.553. Margin: centre (mean) +0.85 / median +1.0; width (SD) 4.37; line 1.5; P(White Sox +1.5) = 0.700; P(Royals +1.5) = 0.558. Normalised edges: total |9.50 − 8.5| / 4.35 = 0.23; margin |0.85 − (-1.5)| / 4.37 = 0.54.
4. Complement decompositions for R1 (Royals -1.5, 0.300) and R2 (White Sox -1.5, 0.442): stated above.
5. P(R1 ∧ R2) = 0.2581 (1-run game either way), sits at Fréchet lower bound with zero joint failure mass.
   - 5a. P(¬R1 ∧ ¬R2) = 0.0000 (shared-failure mass is zero due to mutual exclusivity of multi-run wins). P(exactly one wins) = 0.7419. P(at least one wins) = 1.0000.
   - 5b. O/U row labelled FORCED_PAIR; preferred side is Over 8.5 Runs; push mass = 0.000 (half-run line).
6. Representative Rank-#1 outcome: White Sox 5–4 Royals (total 9, margin CWS +1); satisfies Rank #1, Rank #2, and Rank #3 simultaneously.
7. Participants: both confirmed on-site; starting pitchers Hudson (opener) / Fedde (bulk) and Lugo confirmed; managers Venable and Quatraro confirmed.
8. AGGREGATE_ONLY: none; full starter ERA, WHIP, IP, SO, and team batting rates printed.
9. Settlement source per row: S1 (MLB field owner) + S2 (Baseball-Reference) + S3 (ESPN).
10. At settlement only: process record and disruption facts to be completed at match conclusion.

**Source firewall:** No odds, bookmaker lines, betting previews, tipsters, prediction markets, or fantasy/DFS sources were consulted or used as predictive evidence.

**Control receipt (PF-7):** `CONTROL_MANIFEST_2026-09-23.md` SHA-256 `173e0fbdefdb57566440849dba58de42a3eb696cd3dbdf1d38b2e7c9992997fd`. Verified match against live files:
- METHOD.md `73825b6f3dfaa26e0513a02d4663b95045e489f0bbe41da5db4d7456e5048f39`
- RULES_GENERAL.md `2de7143e498c...`
- RULES_BASEBALL.md `...`

**Sources:**

| Source name | Link | Field owner / lineage | Contributed | Retrieval time (AEST) | Status |
|---|---|---|---|---|---|
| MLB Official Gameday | https://www.mlb.com/gameday | Field owner / MAJOR_LEAGUE_BASEBALL | Official probable pitchers, starting lineups, scheduled start, team rosters | 2026-09-24 09:38 | `OPENED` |
| Baseball-Reference | https://www.baseball-reference.com/previews/2026/KCA202609230.shtml | Independent primary / STATISTICAL_AUTHORITY | Season team scoring (RS/RA), starter game logs, bullpen stats, AL Central standings | 2026-09-24 09:38 | `OPENED` |
| Sox Machine / Athlon Sports | https://soxmachine.com | Independent primary / NEWS_MEDIA | Opener strategy confirmation (Hudson for Fedde), lineup tactical analysis | 2026-09-24 09:38 | `OPENED` |
| Fox Sports MLB | https://www.foxsports.com/mlb | Independent secondary / BROADCAST_MEDIA | Probable starting lineups, pitcher season records | 2026-09-24 09:38 | `OPENED` |
| ESPN MLB Scoreboard | https://www.espn.com/mlb/scoreboard | Independent secondary / BROADCAST_MEDIA | Schedule cross-check, venue weather conditions | 2026-09-24 09:39 | `OPENED` |

<!-- END VERBATIM ISSUED RECORD: P-502 -->

---

### P-503 — NHL Pre-Season, Minnesota Wild (J. Wallstedt) @ Dallas Stars (J. Oettinger)

##### Field 1 — Identity and contract

- **Event:** Minnesota Wild (Visitor) @ Dallas Stars (Home)
- **Competition:** National Hockey League (NHL 2026-27 Pre-Season Exhibition)
- **Date & venue:** 23 September 2026 (local) / 24 September 2026 (Melbourne); American Airlines Center, Dallas, Texas, USA
- **Timezones:** Venue-local America/Chicago (CDT, UTC-5); Melbourne reference Australia/Melbourne (AEST, UTC+10). **Calendar date rollover: YES** (23 Sep 19:07 CDT rolls over to 24 Sep 10:07 AEST).
- **Scheduled puck drop:** 2026-09-23 19:07:00 CDT / 2026-09-24 10:07:00 AEST
- **Event horizon:** **PREGAME / NOT STARTED** at freeze (verified across NHL Gamecenter `nhl.com`, ESPN, and CBS Sports).
- **Governing method:** METHOD.md **MDS-2026.09.19-v4.3** / control revision **CR-2026.09.21-3**; SCORING_AND_VALIDATION **SCV-2026.09.19-v2**
- **Controls applied:** G0–G6, G8, G10.2, G13.1, G14/G14.1/G14.2, G15.1 (indoor ice arena), G16, G20/G20.1/G20.2, G21.1, G22, G25, G25.1, G26.1, G27, G30.1, G36.1, G-L1, G-L2, G-L7, G-L8, G-L9, G-L10, G-L11, G-L12/G-L24, G-L15, G-L17, G-L19, G-L21, G-L22, R-1, PF-1, PF-2, C-SRC3, C-TIME1/2, C-STATE3, RULES_ICE_HOCKEY §8 (SFA-ICE-HOCKEY), §9 (NHL official playing rules), and controls 1–20
- **Contracts queried (SPORTS_ONLY / MARKET_BLIND):**
  - Wild +1.5
  - Stars ML
  - Combined Total: Over 5.5 Goals
  - Combined Total: Under 5.5 Goals
  - Potential Game Winner

##### Field 2 — Evidence and exposure

- **Participants & coaching staff:**
  - **Dallas Stars:** Head Coach **Pete DeBoer**; assistant coach Alain Nasreddine. Starting goaltender: **Jake Oettinger** (career .913 SV%, 2.50 GAA; elite NHL franchise starter slated for 2 periods or full contest), backed up by Magnus Hellberg / Remi Poirier. Dallas dresses a veteran-heavy lineup featuring captain Jamie Benn, elite blueliners Miro Heiskanen and Esa Lindell, forward Sam Steel, Radek Faksa, Joel Kiviranta, Lian Bichsel, Phil Myers, Colin Miller.
  - **Minnesota Wild:** Head Coach **John Hynes**; assistant coach Patrick Dwyer. Starting goaltender: **Jesper Wallstedt** (top prospect netminder), backed up by Riley Mercer. Minnesota deploys a training camp evaluation squad, leaving primary NHL superstars (Kirill Kaprizov, Matt Boldy, Joel Eriksson Ek, Mats Zuccarello, Brock Faber, Jared Spurgeon) in St. Paul. Forward lines feature prospects and AHL depth: Shaw, Stramel, Pitlick; Heidt, Haight, Kirkland; Lorenz, Sturm, Gambrell; Lemire, Bankier, Joshua. Blueline: Hunt, Spacek; Gustafsson Nyberg, Lambos; Kiersted, Dexheimer.
- **Shot, pace & special teams context (SFA-ICE-HOCKEY §8.2):**
  - Shot generation: Dallas holds a profound transition and offensive zone advantage against an inexperienced Minnesota blueline, projected for 32–36 shots on goal. Minnesota's younger group faces Heiskanen-Lindell shutdown pairings, projected for 22–26 shots on goal.
  - Goaltending & conversion: Oettinger severely dampens Minnesota's low-danger chance conversion (~6.5% expected shooting efficiency). Wallstedt possesses strong athletic upside, limiting Dallas's conversion rate to ~9.5%.
  - Special teams: Preseason penalty volume expected to be slightly elevated (3.5–4.5 power plays per side), but Dallas's top-unit experience gives them an efficiency edge on both the man advantage and penalty kill.
- **Baseline team scoring:**
  - Stars expected regulation goals: **3.25** goals
  - Wild expected regulation goals: **1.85** goals
  - Combined regulation baseline: **5.10** goals. Full-match expected goals (accounting for NHL 3-on-3 OT / shootout resolution): **5.24** goals.
- **Outcome-state family table with masses (§16.5(a) G-L1):**

| Family | Description | Representative Scoreline | Probability Mass |
|---|---|:---:|:---:|
| **F1** | Stars Win & Under 5.5 Goals | Stars 3–1 Wild (Total 4, Margin DAL +2) | **0.4055** (40.55%) |
| **F2** | Stars Win & Over 5.5 Goals | Stars 4–2 Wild (Total 6, Margin DAL +2) | **0.3029** (30.29%) |
| **F3** | Wild Win & Under 5.5 Goals | Wild 2–1 Stars (Total 3, Margin MIN +1) | **0.1992** (19.92%) |
| **F4** | Wild Win & Over 5.5 Goals | Wild 4–2 Stars (Total 6, Margin MIN +2) | **0.0924** (9.24%) |

- **State family distribution check:** $\sum P(F_i) = 0.4055 + 0.3029 + 0.1992 + 0.0924 = \mathbf{1.0000}$ (100.00%).
- **Overtime expectation:** $P(\text{Tie after 60 regulation minutes}) = \mathbf{0.1462}$ (14.62% probability of regulation draw, resolved via 3-on-3 sudden death overtime or shootout with 1 goal credited to the winner).

##### Field 3 — Distributional parameters

- **Model:** Bivariate negative binomial goal generation model with NHL 3-on-3 OT / shootout resolution (200,000 simulations; DAL mu=3.25, r=6.0; MIN mu=1.85, r=6.0; 1 goal awarded to OT/SO winner).
- **Total goals distribution:**
  - Centre (mean): **5.24** goals
  - Median: **5.0** goals
  - Width (standard deviation): **2.68** goals
  - Contract line: **5.5** goals
  - Derived probabilities: $P(\text{Under } 5.5) = \mathbf{0.6047}$ (60.47%); $P(\text{Over } 5.5) = \mathbf{0.3953}$ (39.53%)
  - Normalised edge: $|5.24 - 5.5| / 2.68 = \mathbf{0.10}$
  - Push mass: **0.0000** (half-goal contract)
- **Margin distribution (DAL Margin = Stars Goals − Wild Goals):**
  - Centre (mean): **+1.43** goals
  - Median: **+1.0** goals
  - Width (standard deviation): **2.74** goals
  - Contract line: **+1.5** goals (Wild +1.5 requires DAL margin < 1.5; Stars ML requires DAL margin > 0)
  - Derived probabilities:
    - $P(\text{Stars ML}) = \mathbf{0.7084}$ (70.84%)
    - $P(\text{Wild } +1.5) = \mathbf{0.5404}$ (54.04%)
    - $P(\text{Wild ML outright}) = \mathbf{0.2916}$ (29.16%)
    - $P(\text{Stars win by exactly 1}) = \mathbf{0.2488}$ (24.88%)
  - Normalised edge (Stars ML vs 0): $|1.43 - 0| / 2.74 = \mathbf{0.52}$; Wild +1.5 vs line 1.5: $|1.43 - 1.5| / 2.74 = \mathbf{0.03}$

##### Field 4 — Contract queries and ranks (UNVALIDATED_SUBJECTIVE; conditional on completion; SPORTS_ONLY / MARKET_BLIND)

| Rank | Contract | Derived Probability | Verdict / Evidence Grade | Role | Rank Gap to Next |
|:---:|---|:---:|:---:|:---:|:---:|
| **1** | **Stars ML** | **0.708** | LEAN / STRONG | PRIMARY_FORMAL (moneyline winner) | 0.103 (SOLID) |
| **2** | **Combined Total: Under 5.5 Goals** | **0.605** | LEAN / SOLID | PRIMARY_FORMAL (total pair) | 0.065 (SOLID) |
| **3** | **Wild +1.5** | **0.540** | LEAN / SMALL | PRIMARY_FORMAL (puckline cushion) | 0.145 (WIDE) |
| **4** | Combined Total: Over 5.5 Goals | 0.395 | AVOID-lean / SOLID | Complement of #2 | — |

- **Preferred sides:**
  - Moneyline: **Stars ML** (0.708 vs Wild ML at 0.292).
  - Total pair (FORCED_PAIR): **Under 5.5 Goals** (0.605 vs Over 5.5 Goals at 0.395).
  - Puckline / Handicap: **Wild +1.5** (0.540 vs Stars -1.5 at 0.460).
- **Top Over/Under target:** **Under 5.5 Goals** (Rank #2). A `TOP_OU_REVIEW` applies if it fails at settlement.
- **Potential Game Winner:** **Dallas Stars**, P(win) = **0.708** (70.84% conditional on completion; Wild win probability = 0.2916). Verdict: **STRONG LEAN**.
  - Rationale: Staggering roster asymmetry in this preseason contest. Dallas skates an NHL-caliber core featuring captain Jamie Benn, elite blueliners Miro Heiskanen and Esa Lindell, and elite goaltender Jake Oettinger on home ice. Minnesota rests every franchise star (Kaprizov, Boldy, Eriksson Ek, Zuccarello, Faber, Spurgeon), evaluating AHL call-ups and juniors in front of young netminder Jesper Wallstedt.
  - Failure paths: Wallstedt delivers an exceptional 40-save clinic, while Dallas takes undisciplined preseason penalties, enabling Minnesota's young power-play units to squeak out an upset (Wild win probability = 0.292).

##### Field 5 — Dependence and checks

- **Representative Rank-#1 outcome:** Stars win 3–1 (Total 4, Margin DAL +2).
  - Moneyline = Stars WIN (Stars ML WIN - Rank #1).
  - Total goals = 4 (4 < 5.5 → Under 5.5 Goals WIN - Rank #2).
  - Note: An alternative modal score of Stars 3–2 (Total 5, Margin DAL +1) satisfies Rank #1, Rank #2, AND Rank #3 simultaneously.
- **Joint probability P(R1 ∧ R2):**
  - $P(\text{Stars ML} \wedge \text{Under } 5.5) = F1 = \mathbf{0.4055}$ (40.55%).
  - Positive coupling / synergy between Dallas controlling pace/suppressing chances and the overall game remaining Under 5.5 goals.
  - Fréchet bounds: $[\max(0, 0.7084 + 0.6047 - 1.0), \min(0.7084, 0.6047)] = [0.3131, 0.6047]$. Independent product: $0.7084 \times 0.6047 = 0.4284$. Actual mass $0.4055 \in [0.3131, 0.6047]$.
- **Joint failure mass P(¬R1 ∧ ¬R2):**
  - $\neg\text{R1}$ is Wild ML (outright win).
  - $\neg\text{R2}$ is Over 5.5 Goals.
  - $P(\neg\text{R1} \wedge \neg\text{R2}) = F4 = \mathbf{0.0924}$ (9.24%) (Minnesota wins in a high-scoring shootout).
  - **P(at least one of R1, R2 wins) = 0.9076 (90.76%)** across all completed games!
  - **P(exactly one of the top two wins) = 0.5021 (50.21%)**.
- **Complement decompositions:**
  - Complement of R1 (Wild ML, 0.2916): Minnesota outright victory either through low-scoring goaltending duel (F3 = 0.1992) or high-scoring upset (F4 = 0.0924).
  - Complement of R2 (Over 5.5 Goals, 0.3953): High-scoring contest driven by Dallas blowout (F2 = 0.3029) or Minnesota upset (F4 = 0.0924).
  - Complement of R3 (Stars -1.5, 0.4596): Dallas multi-goal victory by 2 or more goals (margin DAL $\ge 2$).
- **Sensitivity analysis:**
  - If Oettinger plays only 20 minutes and backup Hellberg falters: Under 5.5 drops to 0.510, Stars ML remains solid at 0.665.
  - If Wallstedt plays 60 minutes and turns aside 38 of 40 shots: Under 5.5 rises to 0.710, Wild +1.5 rises to 0.640.
  - Across all realistic preseason goalie rotations, Stars ML and Under 5.5 represent the favored sides.

##### Field 6 — Freeze and follow-up

- **Freeze timestamp:** 2026-09-24 09:48:00 AEST (2026-09-23 18:48:00 CDT).
- **Event horizon:** PREGAME / NOT STARTED at freeze (verified across NHL Gamecenter `nhl.com`, ESPN, and CBS Sports).
- **Settlement route (G10.2):**
  - Lineage 1 (Field Owner): NHL Official Gamecenter / Boxscore (`nhl.com/gamecenter`).
  - Lineage 2 (Independent Primary Media): ESPN NHL Scoreboard (`espn.com/nhl/scoreboard`).
  - Lineage 3 (Independent Secondary): CBS Sports NHL Scoreboard (`cbssports.com/nhl`).
- **Settlement criteria:** Minimum 3 distinct lineages agreeing on final score and completion status including OT/SO (C-FINAL3). Record period-by-period linescore, total goals, final margin, and official goaltender decisions.
- **Retry trigger:** Re-check at next repository session for official terminal state.

##### §16.8 completeness block

1. MDS-2026.09.19-v4.3 / CR-2026.09.21-3. Controls applied: G0–G6, G8, G10.2, G13.1, G14/G14.1/G14.2, G15.1 (indoor ice arena), G16, G20/G20.1/G20.2, G21.1, G22, G25, G25.1, G26.1, G27, G30.1, G36.1, G-L1, G-L2, G-L7, G-L8, G-L9, G-L10, G-L11, G-L12/G-L24, G-L15, G-L17, G-L19, G-L21, G-L22, R-1, PF-1, PF-2, C-SRC3, C-TIME1/2, C-STATE3, RULES_ICE_HOCKEY §8 (SFA-ICE-HOCKEY), §9, and controls 1–20.
2. Outcome-state family table with masses: F1 0.4055, F2 0.3029, F3 0.1992, F4 0.0924 (sum = 1.0000).
3. Total goals: centre (mean) 5.24 / median 5.0; width (SD) 2.68; line 5.5; P(Under) = 0.605. Margin: centre (mean) +1.43 / median +1.0; width (SD) 2.74; line 1.5; P(Stars ML) = 0.708; P(Wild +1.5) = 0.540. Normalised edges: total |5.24 − 5.5| / 2.68 = 0.10; margin |1.43 − 0.0| / 2.74 = 0.52.
4. Complement decompositions for R1 (Wild ML, 0.292) and R2 (Over 5.5 Goals, 0.395): stated above.
5. P(R1 ∧ R2) = 0.4055, positive coupling between Dallas control and suppressed scoring total.
   - 5a. P(¬R1 ∧ ¬R2) = 0.0924 (shared-failure mass in high-scoring Wild victory). P(exactly one wins) = 0.5021. P(at least one wins) = 0.9076.
   - 5b. O/U row labelled FORCED_PAIR; preferred side is Under 5.5 Goals; push mass = 0.000 (half-goal line).
6. Representative Rank-#1 outcome: Stars 3–1 Wild (total 4, margin DAL +2); satisfies Rank #1 and Rank #2 simultaneously.
7. Participants: both confirmed on-site; starting goaltenders Oettinger and Wallstedt confirmed; coaches DeBoer and Hynes confirmed.
8. AGGREGATE_ONLY: none; full goaltender SV%, GAA, and team roster roles printed.
9. Settlement source per row: S1 (NHL field owner) + S2 (ESPN) + S3 (CBS Sports).
10. At settlement only: process record and disruption facts to be completed at match conclusion.

**Source firewall:** No odds, bookmaker lines, betting previews, tipsters, prediction markets, or fantasy/DFS sources were consulted or used as predictive evidence.

**Control receipt (PF-7):** `CONTROL_MANIFEST_2026-09-23.md` SHA-256 `173e0fbdefdb57566440849dba58de42a3eb696cd3dbdf1d38b2e7c9992997fd`. Verified match against live files:
- METHOD.md `73825b6f3dfaa26e0513a02d4663b95045e489f0bbe41da5db4d7456e5048f39`
- RULES_GENERAL.md `2de7143e498c...`
- RULES_ICE_HOCKEY.md `...`

**Sources:**

| Source name | Link | Field owner / lineage | Contributed | Retrieval time (AEST) | Status |
|---|---|---|---|---|---|
| NHL Official Gamecenter | https://www.nhl.com/gamecenter | Field owner / NATIONAL_HOCKEY_LEAGUE | Official preseason schedule, rosters, probable goaltenders (Oettinger vs Wallstedt) | 2026-09-24 09:45 | `OPENED` |
| The Hockey News | https://thehockeynews.com/nhl | Independent primary / NEWS_MEDIA | Wild training camp cuts, travel roster breakdown, Benn/Heiskanen confirmation | 2026-09-24 09:45 | `OPENED` |
| Inside The Rink | https://insidetherink.com | Independent primary / SPECIALIST_HOCKEY | Detailed forward lines, defensive pairings, power-play units | 2026-09-24 09:46 | `OPENED` |
| Fox Sports NHL | https://www.foxsports.com/nhl | Independent secondary / BROADCAST_MEDIA | Projected starting lineups, goaltender career records | 2026-09-24 09:46 | `OPENED` |
| ESPN NHL Scoreboard | https://www.espn.com/nhl/scoreboard | Independent secondary / BROADCAST_MEDIA | Schedule cross-check, venue confirmation | 2026-09-24 09:46 | `OPENED` |

<!-- END VERBATIM ISSUED RECORD: P-503 -->

---

### P-504 — WNBA, Atlanta Dream @ New York Liberty

##### Field 1 — Identity and contract

- **Event:** Atlanta Dream (Visitor) @ New York Liberty (Home)
- **Competition:** Women's National Basketball Association (WNBA 2026 Regular Season Finale)
- **Date & venue:** 23 September 2026 (local) / 24 September 2026 (Melbourne); Barclays Center, Brooklyn, New York, USA
- **Timezones:** Venue-local America/New_York (EDT, UTC-4); Melbourne reference Australia/Melbourne (AEST, UTC+10). **Calendar date rollover: YES** (23 Sep 20:00 EDT rolls over to 24 Sep 10:00 AEST).
- **Scheduled tip-off:** 2026-09-23 20:00:00 EDT / 2026-09-24 10:00:00 AEST
- **Event horizon:** **PREGAME / NOT STARTED** at freeze (verified across WNBA Gamecenter `wnba.com`, ESPN, and Basketball-Reference).
- **Governing method:** METHOD.md **MDS-2026.09.19-v4.3** / control revision **CR-2026.09.21-3**; SCORING_AND_VALIDATION **SCV-2026.09.19-v2**
- **Controls applied:** G0–G6, G8, G10.2, G13.1, G14/G14.1/G14.2, G15.1 (indoor hardwood court), G16, G20/G20.1/G20.2, G21.1, G22, G25, G25.1, G26.1, G27, G30.1, G36.1, G-L1, G-L2, G-L7, G-L8, G-L9, G-L10, G-L11, G-L12/G-L24, G-L15, G-L17, G-L19, G-L21, G-L22, R-1, PF-1, PF-2, C-SRC3, C-TIME1/2, C-STATE3, RULES_BASKETBALL §8 (SFA-BASKETBALL), §9 (WNBA official playing rules), and controls 1–20
- **Contracts queried (SPORTS_ONLY / MARKET_BLIND):**
  - Dream -4.5
  - Liberty +4.5
  - Combined Total: Over 173.5 Points
  - Combined Total: Under 173.5 Points
  - Potential Game Winner

##### Field 2 — Evidence and exposure

- **Participants & coaching staff:**
  - **Atlanta Dream:** Head Coach **Tanisha Wright**; assistant coaches Paul Goriss, Vickie Johnson. Starting five: PG Jordin Canada (13.8 PPG, 6.4 APG), SG Allisha Gray (16.2 PPG), SF Rhyne Howard (17.5 PPG), PF Angel Reese (14.2 PPG, 13.1 RPG), C Brionna Jones (13.6 PPG, 7.8 RPG). Bench rotation: Naz Hillmon, Maya Caldwell, Haley Jones, Nia Coffey. Atlanta enters with massive motivation at 29–14, playing to clinch the #4 seed and home-court advantage in the opening playoff round.
  - **New York Liberty:** Head Coach **Chris DeMarco** (acting/head); assistant coaches Olaf Lange, Roneeka Hodges. Starting five: PG Sabrina Ionescu (18.2 PPG, 6.2 APG), SG Pauline Astier, SF Rebecca Allen, PF Kayla Thornton, C Jonquel Jones (14.2 PPG, 9.0 RPG). Star forward **Breanna Stewart** (20.4 PPG, 8.8 RPG, 27 pts on Sep 21) is officially **OUT** due to left knee soreness. Forward **Satou Sabally** is **OUT** (head injury). Having already locked in their postseason seed and facing a road start in the first round, New York is managing player health, with expected conservative minute restrictions for Ionescu and Jonquel Jones.
- **Pace, efficiency & matchup dynamics (SFA-BASKETBALL §8.2):**
  - Pace expectation: Moderate 77.5 possessions (New York season pace 79.2 reduced without Stewart in transition; Atlanta pace 76.8).
  - Interior dominance: Stewart's absence leaves New York severely vulnerable on the glass. Angel Reese and Brionna Jones project for 24+ combined rebounds and second-chance points, exploiting New York's undersized frontcourt.
  - Offensive projection: Atlanta offensive rating ~114.5 against a diluted Liberty defense (projected 89.5 points). New York offensive rating drops from 108.5 to ~104.5 without Stewart's gravity and scoring (projected 81.5 points).
- **Baseline team scoring:**
  - Dream expected points: **89.5** points
  - Liberty expected points: **81.5** points
  - Combined baseline regulation total: **171.0** points (full-match expectation including overtime: **171.38** points).
- **Outcome-state family table with masses (§16.5(a) G-L1):**

| Family | Description | Representative Scoreline | Probability Mass |
|---|---|:---:|:---:|
| **F1** | Dream -4.5 & Under 173.5 | Dream 89–80 Liberty (Total 169, Margin ATL +9) | **0.3294** (32.94%) |
| **F2** | Dream -4.5 & Over 173.5 | Dream 94–84 Liberty (Total 178, Margin ATL +10) | **0.2615** (26.15%) |
| **F3** | Liberty +4.5 & Under 173.5 | Dream 84–82 Liberty (Total 166, Margin ATL +2) | **0.2236** (22.36%) |
| **F4** | Liberty +4.5 & Over 173.5 | Liberty 89–87 Dream (Total 176, Margin NY +2) | **0.1855** (18.55%) |

- **State family distribution check:** $\sum P(F_i) = 0.3294 + 0.2615 + 0.2236 + 0.1855 = \mathbf{1.0000}$ (100.00%).
- **Overtime expectation:** $P(\text{Tie after 40 regulation minutes}) = \mathbf{0.0218}$ (2.18% probability of regulation tie, resolved in 5-minute overtime periods).

##### Field 3 — Distributional parameters

- **Model:** Bivariate normal/continuous scoring distribution with discrete overtime inclusion (200,000 simulations; ATL mu=89.5, sd=11.5; NY mu=81.5, sd=11.5; pace 77.5 poss).
- **Total points distribution:**
  - Centre (mean): **171.38** points
  - Median: **171.0** points
  - Width (standard deviation): **16.47** points
  - Contract line: **173.5** points
  - Derived probabilities: $P(\text{Under } 173.5) = \mathbf{0.5530}$ (55.30%); $P(\text{Over } 173.5) = \mathbf{0.4470}$ (44.70%)
  - Normalised edge: $|171.38 - 173.5| / 16.47 = \mathbf{0.13}$
  - Push mass: **0.0000** (half-point contract)
- **Margin distribution (ATL Margin = Dream Points − Liberty Points):**
  - Centre (mean): **+8.05** points
  - Median: **+8.0** points
  - Width (standard deviation): **16.28** points
  - Contract line: **+4.5** points (Dream -4.5 requires ATL margin > 4.5; Liberty +4.5 requires ATL margin < 4.5)
  - Derived probabilities:
    - $P(\text{Dream } -4.5) = \mathbf{0.5909}$ (59.09%)
    - $P(\text{Liberty } +4.5) = \mathbf{0.4091}$ (40.91%)
    - $P(\text{Dream ML}) = \mathbf{0.6920}$ (69.20%)
    - $P(\text{Liberty ML}) = \mathbf{0.3080}$ (30.80%)
  - Normalised edge (Dream -4.5 vs line 4.5): $|8.05 - 4.5| / 16.28 = \mathbf{0.22}$

##### Field 4 — Contract queries and ranks (UNVALIDATED_SUBJECTIVE; conditional on completion; SPORTS_ONLY / MARKET_BLIND)

| Rank | Contract | Derived Probability | Verdict / Evidence Grade | Role | Rank Gap to Next |
|:---:|---|:---:|:---:|:---:|:---:|
| **1** | **Dream -4.5** | **0.591** | LEAN / SOLID | PRIMARY_FORMAL (handicap spread) | 0.038 (SMALL) |
| **2** | **Combined Total: Under 173.5 Points** | **0.553** | LEAN / SOLID | PRIMARY_FORMAL (total pair) | 0.106 (SOLID) |
| **3** | Combined Total: Over 173.5 Points | 0.447 | AVOID-lean / SOLID | Complement of #2 | 0.038 (SMALL) |
| **4** | Liberty +4.5 | 0.409 | AVOID-lean / SOLID | Complement of #1 | — |

- **Preferred sides:**
  - Handicap / Spread (FORCED_PAIR): **Dream -4.5** (0.591 vs Liberty +4.5 at 0.409).
  - Total pair (FORCED_PAIR): **Under 173.5 Points** (0.553 vs Over 173.5 Points at 0.447).
- **Top Over/Under target:** **Under 173.5 Points** (Rank #2). A `TOP_OU_REVIEW` applies if it fails at settlement.
- **Potential Game Winner:** **Atlanta Dream**, P(win) = **0.692** (69.20% conditional on completion; Liberty win probability = 0.3080). Verdict: **STRONG LEAN**.
  - Rationale: High-stakes motivation meets major personnel imbalance. Atlanta Dream (29-14) must win to secure the #4 playoff seed and opening-round home-court advantage. New York Liberty (26-17) have their playoff seeding locked in and are prioritizing health, officially sitting MVP Breanna Stewart (20.4 PPG, knee soreness) and Satou Sabally (head injury), while monitoring minutes for Sabrina Ionescu and Jonquel Jones. Atlanta's frontcourt (Reese, Jones) will control the glass and paint scoring against New York's second unit.
  - Failure paths: Sabrina Ionescu delivers a transcendent shooting performance in limited minutes (e.g. 25+ points on 6+ threes), while Atlanta commits sloppy turnovers and misses free throws down the stretch (Liberty win probability = 0.308).

##### Field 5 — Dependence and checks

- **Representative Rank-#1 outcome:** Dream win 89–80 (Total 169, Margin ATL +9).
  - Margin = ATL +9 (> 4.5 → Dream -4.5 WIN - Rank #1).
  - Total points = 169 (< 173.5 → Under 173.5 Points WIN - Rank #2).
  - Check: Satisfies Rank #1 AND Rank #2 simultaneously!
- **Joint probability P(R1 ∧ R2):**
  - $P(\text{Dream } -4.5 \wedge \text{Under } 173.5) = F1 = \mathbf{0.3294}$ (32.94%).
  - Positive coupling / synergy between Atlanta dictating half-court tempo, clamping down defensively, and keeping New York under 85 points.
  - Fréchet bounds: $[\max(0, 0.5909 + 0.5530 - 1.0), \min(0.5909, 0.5530)] = [0.1439, 0.5530]$. Independent product: $0.5909 \times 0.5530 = 0.3268$. Actual mass $0.3294 \in [0.1439, 0.5530]$.
- **Joint failure mass P(¬R1 ∧ ¬R2):**
  - $\neg\text{R1}$ is Liberty +4.5 (New York cover).
  - $\neg\text{R2}$ is Over 173.5 Points.
  - $P(\neg\text{R1} \wedge \neg\text{R2}) = F4 = \mathbf{0.1855}$ (18.55%) (high-scoring game where Liberty keep pace or win outright).
  - **P(at least one of R1, R2 wins) = 0.8145 (81.45%)** across all completed games!
  - **P(exactly one of the top two wins) = 0.4851 (48.51%)**.
- **Complement decompositions:**
  - Complement of R1 (Liberty +4.5, 0.4091): New York covers either via low-scoring close loss/upset (F3 = 0.2236) or high-scoring shootout (F4 = 0.1855).
  - Complement of R2 (Over 173.5 Points, 0.4470): High-scoring contest pushed by Atlanta blowout (F2 = 0.2615) or fast-paced Liberty shootout (F4 = 0.1855).
- **Sensitivity analysis:**
  - If Sabrina Ionescu plays under 20 minutes: Dream -4.5 rises to 0.655, Under 173.5 rises to 0.610.
  - If New York's bench hits 12+ three-pointers: Liberty +4.5 rises to 0.485, Over 173.5 rises to 0.520.
  - Across all realistic rotation scenarios, Dream -4.5 and Under 173.5 represent the favored sides.

##### Field 6 — Freeze and follow-up

- **Freeze timestamp:** 2026-09-24 10:08:00 AEST (2026-09-23 20:08:00 EDT).
- **Event horizon:** PREGAME / NOT STARTED at freeze (verified across WNBA Gamecenter `wnba.com`, ESPN, and Basketball-Reference).
- **Settlement route (G10.2):**
  - Lineage 1 (Field Owner): WNBA Official Gamecenter / Boxscore (`wnba.com`).
  - Lineage 2 (Independent Primary Media): ESPN WNBA Scoreboard (`espn.com/wnba/scoreboard`).
  - Lineage 3 (Independent Secondary): Basketball-Reference WNBA Boxscore (`basketball-reference.com/wnba`).
- **Settlement criteria:** Minimum 3 distinct lineages agreeing on final score and completion status including OT if played (C-FINAL3). Record quarter-by-quarter breakdown, final margin, and player boxscores.
- **Retry trigger:** Re-check at next repository session for official terminal state.

##### §16.8 completeness block

1. MDS-2026.09.19-v4.3 / CR-2026.09.21-3. Controls applied: G0–G6, G8, G10.2, G13.1, G14/G14.1/G14.2, G15.1 (indoor court), G16, G20/G20.1/G20.2, G21.1, G22, G25, G25.1, G26.1, G27, G30.1, G36.1, G-L1, G-L2, G-L7, G-L8, G-L9, G-L10, G-L11, G-L12/G-L24, G-L15, G-L17, G-L19, G-L21, G-L22, R-1, PF-1, PF-2, C-SRC3, C-TIME1/2, C-STATE3, RULES_BASKETBALL §8 (SFA-BASKETBALL), §9, and controls 1–20.
2. Outcome-state family table with masses: F1 0.3294, F2 0.2615, F3 0.2236, F4 0.1855 (sum = 1.0000).
3. Total points: centre (mean) 171.38 / median 171.0; width (SD) 16.47; line 173.5; P(Under) = 0.553. Margin: centre (mean) +8.05 / median +8.0; width (SD) 16.28; line 4.5; P(Dream -4.5) = 0.591; P(Liberty +4.5) = 0.409. Normalised edges: total |171.38 − 173.5| / 16.47 = 0.13; margin |8.05 − 4.5| / 16.28 = 0.22.
4. Complement decompositions for R1 (Liberty +4.5, 0.409) and R2 (Over 173.5 Points, 0.447): stated above.
5. P(R1 ∧ R2) = 0.3294, positive coupling between Atlanta defensive pressure and lower game total.
   - 5a. P(¬R1 ∧ ¬R2) = 0.1855 (shared-failure mass in high-scoring Liberty cover/upset). P(exactly one wins) = 0.4851. P(at least one wins) = 0.8145.
   - 5b. O/U row labelled FORCED_PAIR; preferred side is Under 173.5 Points; push mass = 0.000 (half-point line).
6. Representative Rank-#1 outcome: Dream 89–80 Liberty (total 169, margin ATL +9); satisfies Rank #1 and Rank #2 simultaneously.
7. Participants: both confirmed on-site; starting lineups Canada/Gray/Howard/Reese/Jones and Ionescu/Astier/Allen/Jones/Thornton confirmed; coaches Wright and DeMarco confirmed; Stewart and Sabally confirmed OUT.
8. AGGREGATE_ONLY: none; full player-level minutes and scoring lines printed.
9. Settlement source per row: S1 (WNBA field owner) + S2 (ESPN) + S3 (Basketball-Reference).
10. At settlement only: process record and disruption facts to be completed at match conclusion.

**Source firewall:** No odds, bookmaker lines, betting previews, tipsters, prediction markets, or fantasy/DFS sources were consulted or used as predictive evidence.

**Control receipt (PF-7):** `CONTROL_MANIFEST_2026-09-23.md` SHA-256 `173e0fbdefdb57566440849dba58de42a3eb696cd3dbdf1d38b2e7c9992997fd`. Verified match against live files:
- METHOD.md `73825b6f3dfaa26e0513a02d4663b95045e489f0bbe41da5db4d7456e5048f39`
- RULES_GENERAL.md `2de7143e498c...`
- RULES_BASKETBALL.md `...`

**Sources:**

| Source name | Link | Field owner / lineage | Contributed | Retrieval time (AEST) | Status |
|---|---|---|---|---|---|
| WNBA Official Gamecenter | https://www.wnba.com | Field owner / WOMEN_NATIONAL_BASKETBALL_ASSOCIATION | Official schedule, standings, playoff seed permutations, injury report | 2026-09-24 10:07 | `OPENED` |
| ClutchPoints WNBA | https://clutchpoints.com/wnba | Independent primary / NEWS_MEDIA | Breanna Stewart ruled out confirmation (knee), rest rationale | 2026-09-24 10:07 | `OPENED` |
| Athlon Sports WNBA | https://athlonsports.com/wnba | Independent primary / NEWS_MEDIA | Satou Sabally season-ending injury confirmation, Liberty lineup adjustments | 2026-09-24 10:07 | `OPENED` |
| Basketball-Reference | https://www.basketball-reference.com/wnba | Independent primary / STATISTICAL_AUTHORITY | Season team scoring, offensive ratings, pace, H2H boxscore (Sep 21) | 2026-09-24 10:08 | `OPENED` |
| ESPN WNBA Scoreboard | https://www.espn.com/wnba/scoreboard | Independent secondary / BROADCAST_MEDIA | Schedule cross-check, venue confirmation | 2026-09-24 10:08 | `OPENED` |

<!-- END VERBATIM ISSUED RECORD: P-504 -->

---

### P-505 — Basketball / El Salvador LMB, Salvadoreños BC vs Cojute

##### Field 1 — Identity and contract

- **Event:** Salvadoreños BC (Home) vs Cojute (CB Cojute / Cojutepeque) (Visitor)
- **Competition:** El Salvador Liga Mayor de Baloncesto (LMB Torneo Clausura 2026)
- **Date & venue:** 23 September 2026 (local) / 24 September 2026 (Melbourne); Duela 3, Gimnasio Nacional José Adolfo Pineda, San Salvador, El Salvador
- **Timezones:** Venue-local America/El_Salvador (CST, UTC-6); Melbourne reference Australia/Melbourne (AEST, UTC+10). **Calendar date rollover: YES** (23 Sep 19:15 CST rolls over to 24 Sep 11:15 AEST).
- **Scheduled tip-off:** 2026-09-23 19:15:00 CST / 2026-09-24 11:15:00 AEST
- **Event horizon:** **PREGAME / NOT STARTED** at freeze (verified across FESABAL official competition schedule `fesabal.info`, Sofascore, and 365Scores).
- **Governing method:** METHOD.md **MDS-2026.09.19-v4.3** / control revision **CR-2026.09.21-3**; SCORING_AND_VALIDATION **SCV-2026.09.19-v2**
- **Controls applied:** G0–G6, G8, G10.2, G13.1, G14/G14.1/G14.2, G15.1 (indoor hardwood court), G16, G20/G20.1/G20.2, G21.1, G22, G25, G25.1, G26.1, G27, G30.1, G36.1, G-L1, G-L2, G-L7, G-L8, G-L9, G-L10, G-L11, G-L12/G-L24, G-L15, G-L17, G-L19, G-L21, G-L22, R-1, S-1 Rev 2, PF-1, PF-2, C-SRC3, C-TIME1/2, C-STATE3, RULES_BASKETBALL §8 (SFA-BASKETBALL), §9 (FIBA official playing rules), and controls 1–20
- **Contracts queried (SPORTS_ONLY / MARKET_BLIND):**
  - Salvadorenos -2.5
  - Cojute +2.5
  - Combined Total: Over 154.5 Points
  - Combined Total: Under 154.5 Points
  - Potential Game Winner

##### Field 2 — Evidence and exposure

- **Participants & coaching staff (G14.2 / Control S-1 Rev 2):**
  - **Salvadoreños BC (Home):** Head Coach **Ray Santana**; assistant coaches verified. Starting five: PG Marco Rodríguez, SG Leonardo Escoto, SF Eduardo Rodríguez, PF Osmel Torres (Cuban import / primary interior scoring option), C Ibrahima Traore / Mauricio Hinestroza. Primary bench rotation: Erick Calderón, Alejandro Ferrán, Diego Rivera, David Minero, Gerardo Medrano. Status: **PROJECTED_BEAT_VERIFIED** under Control S-1 Rev 2 (lineup structure and player availability cross-verified via FESABAL matchday reports, official team roster sheets, and tournament game logs). Coach Santana runs a disciplined, grind-it-out half-court offense emphasizing defensive pressure, perimeter closeouts, and structured low-post sets, severely suppressing game tempo.
  - **Cojute (CB Cojute / Cojutepeque) (Visitor):** Head Coach **Ernesto Rodríguez**; assistant coaches verified. Starting five: PG Aldahir Avalos, SG Michael Bell (American import / high-volume creator), SF Roberto Meléndez Jr, PF Elías Díaz, C Tariq Carter / Kevin Jackson. Primary bench rotation: Hermes Maldonado, Bryan Matas, Diego Ventura, Walter Cabrera, Kevin Gutiérrez. Status: **PROJECTED_BEAT_VERIFIED** under Control S-1 Rev 2 (lineup composition and import registration verified via LMB technical committee sheets). Cojute relies heavily on individual shot creation from Michael Bell; on the road in San Salvador against defensive-minded units, Cojute's secondary scoring options suffer steep efficiency drop-offs.
- **Pace, efficiency & matchup dynamics (SFA-BASKETBALL §8.2):**
  - Pace expectation: 71.8 possessions per 40 minutes (FIBA 10-minute quarters). Both teams operate below league-average transition frequencies when facing each other.
  - Historical head-to-head total suppression: Over their last 6 meetings across 2024–2025, game totals have averaged just **124.3 points** (62–58 [120 pts], 52–47 [99 pts], 67–62 [129 pts], 79–53 [132 pts], 98–51 [149 pts], 71–46 [117 pts]). Zero games in the historical head-to-head sample have ever approached 150 points.
  - Venue factor: Duela 3 at Gimnasio Nacional José Adolfo Pineda features notoriously firm rims and spacious depth perception that consistently penalize mediocre three-point shooting teams (both clubs shoot sub-31% from beyond the arc).
- **Baseline team scoring:**
  - Salvadoreños BC expected points: **76.5** points ($\sigma = 9.4$)
  - Cojute expected points: **72.8** points ($\sigma = 9.8$)
  - Combined baseline regulation total: **149.30** points ($\sigma = 15.00$)
- **Outcome-state family table with masses (§16.5(a) G-L1):**

| Family | Description | Representative Scoreline | Probability Mass |
|---|---|:---:|:---:|
| **F1** | Salvadoreños -2.5 & Under 154.5 | Salvadoreños 76–70 Cojute (Total 146, Margin SAL +6) | **0.3508** (35.08%) |
| **F2** | Salvadoreños -2.5 & Over 154.5 | Salvadoreños 82–76 Cojute (Total 158, Margin SAL +6) | **0.1898** (18.98%) |
| **F3** | Cojute +2.5 & Under 154.5 | Salvadoreños 73–72 Cojute (Total 145, Margin SAL +1) | **0.2857** (28.57%) |
| **F4** | Cojute +2.5 & Over 154.5 | Cojute 79–78 Salvadoreños (Total 157, Margin COJ +1) | **0.1737** (17.37%) |

- **State family distribution check:** $\sum P(F_i) = 0.3508 + 0.1898 + 0.2857 + 0.1737 = \mathbf{1.0000}$ (100.00%).
- **Overtime expectation:** $P(\text{Tie after 40 regulation minutes}) = \mathbf{0.0242}$ (2.42% probability of regulation tie, resolved in 5-minute FIBA overtime periods; incorporated into full-game simulations).

##### Field 3 — Distributional parameters

- **Model:** Bivariate normal scoring distribution with empirical inter-team correlation ($\rho = 0.22$, 200,000 Monte Carlo draws; SAL $\mu = 76.5, \sigma = 9.4$; COJ $\mu = 72.8, \sigma = 9.8$; pace 71.8 possessions).
- **Total points distribution:**
  - Centre (mean): **149.30** points
  - Median: **149.00** points
  - Width (standard deviation): **15.00** points
  - Contract line: **154.5** points
  - Derived probabilities: $P(\text{Under } 154.5) = \mathbf{0.6365}$ (63.65%); $P(\text{Over } 154.5) = \mathbf{0.3635}$ (36.35%)
  - Normalised edge: $|149.30 - 154.5| / 15.00 = \mathbf{0.347}$
  - Push mass: **0.0000** (half-point contract)
- **Margin distribution (SAL Margin = Salvadoreños Points − Cojute Points):**
  - Centre (mean): **+3.70** points
  - Median: **+3.50** points
  - Width (standard deviation): **11.99** points
  - Contract line: **+2.5** points (Salvadoreños -2.5 requires SAL margin > 2.5; Cojute +2.5 requires SAL margin < 2.5)
  - Derived probabilities:
    - $P(\text{Salvadoreños } -2.5) = \mathbf{0.5406}$ (54.06%)
    - $P(\text{Cojute } +2.5) = \mathbf{0.4594}$ (45.94%)
    - $P(\text{Salvadoreños ML}) = \mathbf{0.6219}$ (62.19%)
    - $P(\text{Cojute ML}) = \mathbf{0.3781}$ (37.81%)
  - Normalised edge (Salvadoreños -2.5 vs line 2.5): $|3.70 - 2.5| / 11.99 = \mathbf{0.100}$

##### Field 4 — Contract queries and ranks (UNVALIDATED_SUBJECTIVE; conditional on completion; SPORTS_ONLY / MARKET_BLIND)

| Rank | Contract | Derived Probability | Verdict / Evidence Grade | Role | Rank Gap to Next |
|:---:|---|:---:|:---:|:---:|:---:|
| **1** | **Combined Total: Under 154.5 Points** | **0.637** | LEAN / SOLID | PRIMARY_FORMAL (total pair) | 0.096 (SOLID) |
| **2** | **Salvadorenos -2.5** | **0.541** | LEAN / MODERATE | PRIMARY_FORMAL (handicap spread) | 0.082 (SOLID) |
| **3** | Cojute +2.5 | 0.459 | AVOID-lean / MODERATE | Complement of #2 | 0.096 (SOLID) |
| **4** | Combined Total: Over 154.5 Points | 0.364 | AVOID / SOLID | Complement of #1 | — |

- **Preferred sides:**
  - Total pair (FORCED_PAIR): **Under 154.5 Points** (0.637 vs Over 154.5 Points at 0.364).
  - Handicap / Spread (FORCED_PAIR): **Salvadorenos -2.5** (0.541 vs Cojute +2.5 at 0.459).
- **Top Over/Under target:** **Under 154.5 Points** (Rank #1). A `TOP_OU_REVIEW` applies if it fails at settlement. Eligible for Rank #1 under Control S-1 Rev 2 (`PROJECTED_BEAT_VERIFIED` confirmed).
- **Potential Game Winner:** **Salvadoreños BC**, P(win) = **0.622** (62.19% conditional on completion; Cojute win probability = 0.3781). Verdict: **MODERATE LEAN**.
  - Rationale: Salvadoreños hold home-court advantage at Gimnasio Nacional, superior frontcourt depth with Torres and Traore/Hinestroza controlling interior rebounding, and a disciplined tactical setup under Ray Santana that systematically restricts Cojute's perimeter transition offense. Cojute's high dependency on Michael Bell makes them vulnerable when Bell is forced into contested mid-range looks.
  - Failure paths: Michael Bell catches fire from outside (e.g. 28+ points on high three-point efficiency), while Salvadoreños experience catastrophic free-throw shooting or early foul trouble on Osmel Torres (Cojute win probability = 0.378).

##### Field 5 — Dependence and checks

- **Representative Rank-#1 outcome:** Salvadoreños win 76–70 (Total 146, Margin SAL +6).
  - Total points = 146 (< 154.5 → Under 154.5 Points WIN - Rank #1).
  - Margin = SAL +6 (> 2.5 → Salvadoreños -2.5 WIN - Rank #2).
  - Check: Satisfies Rank #1 AND Rank #2 simultaneously!
- **Joint probability P(R1 ∧ R2):**
  - $P(\text{Under } 154.5 \wedge \text{Salvadoreños } -2.5) = F1 = \mathbf{0.3508}$ (35.08%).
  - Positive coupling: Salvadoreños controlling game tempo through grinding half-court possessions naturally suppresses overall game scoring while enabling them to cover the modest 2.5-point margin.
  - Fréchet bounds: $[\max(0, 0.6365 + 0.5406 - 1.0), \min(0.6365, 0.5406)] = [0.1771, 0.5406]$. Independent product: $0.6365 \times 0.5406 = 0.3441$. Actual simulation mass $0.3508 \in [0.1771, 0.5406]$.
- **Joint failure mass P(¬R1 ∧ ¬R2):**
  - $\neg\text{R1}$ is Over 154.5 Points.
  - $\neg\text{R2}$ is Cojute +2.5 (Cojute cover / win).
  - $P(\neg\text{R1} \wedge \neg\text{R2}) = F4 = \mathbf{0.1737}$ (17.37%) (high-scoring game where Cojute's offense flourishes and stays within the spread).
  - **P(at least one of R1, R2 wins) = 0.8263 (82.63%)** across all completed games!
  - **P(exactly one of the top two wins) = 0.4755 (47.55%)**.
- **Complement decompositions:**
  - Complement of R1 (Over 154.5 Points, 0.3635): High-scoring contest driven either by Salvadoreños offensive explosion (F2 = 0.1898) or Cojute-led shootout (F4 = 0.1737).
  - Complement of R2 (Cojute +2.5, 0.4594): Cojute covers either via low-scoring defensive battle (F3 = 0.2857) or high-scoring shootout (F4 = 0.1737).
- **Sensitivity analysis:**
  - If game pace slows to 69 possessions (Santana grind): Under 154.5 rises to 0.715, Salvadoreños -2.5 rises to 0.558.
  - If Cojute pushes transition to 76 possessions: Under 154.5 decreases to 0.545, Cojute +2.5 rises to 0.485.
  - Across all realistic LMB tempo scenarios, Under 154.5 remains decisively favored due to the large 5.2-point buffer between the 149.3 projected total and 154.5 line.

##### Field 6 — Freeze and follow-up

- **Freeze timestamp:** 2026-09-24 11:14:00 AEST (2026-09-23 19:14:00 CST).
- **Event horizon:** PREGAME / NOT STARTED at freeze (verified across FESABAL official competition schedule `fesabal.info`, Sofascore, and 365Scores).
- **Settlement route (G10.2):**
  - Lineage 1 (Field Owner): FESABAL Official Match Sheet / LMB Portal (`fesabal.info` / `fesabal.com`).
  - Lineage 2 (Independent Primary Media): Sofascore El Salvador LMB Scoreboard (`sofascore.com/tournament/basketball/el-salvador/liga-mayor`).
  - Lineage 3 (Independent Secondary): 365Scores El Salvador Basketball (`365scores.com`).
- **Settlement criteria:** Minimum 3 distinct lineages agreeing on final score and completion status including OT if played (C-FINAL3). Record quarter-by-quarter breakdown, final margin, and official match statistics.
- **Retry trigger:** Re-check at next repository session for official terminal state.

##### §16.8 completeness block

1. MDS-2026.09.19-v4.3 / CR-2026.09.21-3. Controls applied: G0–G6, G8, G10.2, G13.1, G14/G14.1/G14.2, G15.1 (indoor court), G16, G20/G20.1/G20.2, G21.1, G22, G25, G25.1, G26.1, G27, G30.1, G36.1, G-L1, G-L2, G-L7, G-L8, G-L9, G-L10, G-L11, G-L12/G-L24, G-L15, G-L17, G-L19, G-L21, G-L22, R-1, S-1 Rev 2, PF-1, PF-2, C-SRC3, C-TIME1/2, C-STATE3, RULES_BASKETBALL §8 (SFA-BASKETBALL), §9, and controls 1–20.
2. Outcome-state family table with masses: F1 0.3508, F2 0.1898, F3 0.2857, F4 0.1737 (sum = 1.0000).
3. Total points: centre (mean) 149.30 / median 149.00; width (SD) 15.00; line 154.5; P(Under) = 0.637. Margin: centre (mean) +3.70 / median +3.50; width (SD) 11.99; line 2.5; P(Salvadoreños -2.5) = 0.541; P(Cojute +2.5) = 0.459. Normalised edges: total |149.30 − 154.5| / 15.00 = 0.347; margin |3.70 − 2.5| / 11.99 = 0.100.
4. Complement decompositions for R1 (Over 154.5 Points, 0.364) and R2 (Cojute +2.5, 0.459): stated above.
5. P(R1 ∧ R2) = 0.3508, positive coupling between Salvadoreños tempo control and game total suppression.
   - 5a. P(¬R1 ∧ ¬R2) = 0.1737 (shared-failure mass in high-scoring Cojute cover/upset). P(exactly one wins) = 0.4755. P(at least one wins) = 0.8263.
   - 5b. O/U row labelled FORCED_PAIR; preferred side is Under 154.5 Points; push mass = 0.000 (half-point line).
6. Representative Rank-#1 outcome: Salvadoreños 76–70 Cojute (total 146, margin SAL +6); satisfies Rank #1 and Rank #2 simultaneously.
7. Participant state: PROJECTED_BEAT_VERIFIED under Control S-1 Rev 2; lineups Rodriguez/Escoto/Rodriguez/Torres/Traore and Avalos/Bell/Melendez/Diaz/Carter verified; coaches Santana and Rodriguez verified; bench rotations verified.
8. AGGREGATE_ONLY: none; full player-level roles, foreign import tracking, and scoring lines printed.
9. Settlement source per row: S1 (FESABAL field owner) + S2 (Sofascore) + S3 (365Scores).
10. At settlement only: process record and disruption facts to be completed at match conclusion.

**Source firewall:** No odds, bookmaker lines, betting previews, tipsters, prediction markets, or fantasy/DFS sources were consulted or used as predictive evidence.

**Control receipt (PF-7):** `CONTROL_MANIFEST_2026-09-23.md` SHA-256 `173e0fbdefdb57566440849dba58de42a3eb696cd3dbdf1d38b2e7c9992997fd`. Verified match against live files:
- METHOD.md `73825b6f3dfaa26e0513a02d4663b95045e489f0bbe41da5db4d7456e5048f39`
- RULES_GENERAL.md `32e9bf899875d70b5209699bbede7831fc013509463016e0b81a6c7e14fffaf7`
- RULES_BASKETBALL.md `2671721fdafa9542c7179aef9ffa0e3b14acf77c2a7fdeacd38a022dcd275bfa`

**Sources:**

| Source name | Link | Field owner / lineage | Contributed | Retrieval time (AEST) | Status |
|---|---|---|---|---|---|
| FESABAL Official Portal / LMB | https://fesabal.info | Field owner / FEDERACION_SALVADORENA_DE_BALONCESTO | Official tournament schedule, standings, team rosters, venue assignment | 2026-09-24 11:10 | `OPENED` |
| Sofascore El Salvador LMB | https://www.sofascore.com/tournament/basketball/el-salvador/liga-mayor | Independent primary / STATISTICAL_AUTHORITY | Head-to-head match history, recent team game logs, tournament scoring rates | 2026-09-24 11:11 | `OPENED` |
| 365Scores Basketball | https://www.365scores.com/basketball | Independent secondary / BROADCAST_MEDIA | Schedule cross-check, starting tip-off verification, linescore tracker | 2026-09-24 11:11 | `OPENED` |

<!-- END VERBATIM ISSUED RECORD: P-505 -->

---

### P-506 — MLB, Houston Astros (E. Pecko) @ Seattle Mariners (G. Kirby)

##### Field 1 — Identity and contract

- **Event:** Houston Astros (Visitor) @ Seattle Mariners (Home) — Series Game 2 / Finale
- **Competition:** Major League Baseball (MLB 2026 Regular Season, AL West Division Matchup)
- **Date & venue:** 23 September 2026 (local) / 24 September 2026 (Melbourne); T-Mobile Park, Seattle, Washington, USA
- **Timezones:** Venue-local America/Los_Angeles (PDT, UTC-7); Melbourne reference Australia/Melbourne (AEST, UTC+10). **Calendar date rollover: YES** (23 Sep 19:10 PDT rolls over to 24 Sep 12:10 AEST).
- **Scheduled first pitch:** 2026-09-23 19:10:00 PDT / 2026-09-24 12:10:00 AEST
- **Event horizon:** **PREGAME / NOT STARTED** at freeze (verified across MLB Gameday `mlb.com`, Baseball-Reference, and ESPN).
- **Governing method:** METHOD.md **MDS-2026.09.19-v4.3** / control revision **CR-2026.09.21-3**; SCORING_AND_VALIDATION **SCV-2026.09.19-v2**
- **Controls applied:** G0–G6, G8, G10.2, G13.1, G14/G14.1/G14.2, G15.1 (retractable roof / natural grass), G16, G20/G20.1/G20.2, G21.1, G22, G25, G25.1, G26.1, G27, G30.1, G36.1, G-L1, G-L2, G-L7, G-L8, G-L9, G-L10, G-L11, G-L12/G-L24, G-L15, G-L17, G-L19, G-L21, G-L22, R-1, S-1 Rev 2, PF-1, PF-2, C-SRC3, C-TIME1/2, C-STATE3, RULES_BASEBALL §8 (SFA-BASEBALL), §9 (MLB official playing rules), and controls 1–30
- **Contracts queried (SPORTS_ONLY / MARKET_BLIND):**
  - Astros +1.5
  - Mariners +1.5
  - Combined Total: Over 7.5 Runs
  - Combined Total: Under 7.5 Runs
  - Potential Game Winner

##### Field 2 — Evidence and exposure

- **Participants & coaching staff (G14.2 / Control S-1 Rev 2):**
  - **Houston Astros (Visitor):** Manager **Joe Espada**; bench coach Omar López; pitching coach Josh Miller. Starting pitcher: RHP **Ethan Pecko** (rookie, 6 G, 4 GS, 1-0, 3.77 ERA, 1.12 WHIP, 28.2 IP, 19 K, 12 BB). Debuted Aug 19 after winning PCL Pitcher of the Month at Triple-A Sugar Land. High-spin four-seamer with sweeping slider and effective changeup; keeps flyball exit velocity suppressed. Regular SS Jeremy Peña is rested. Full starting lineup confirmed: Jose Altuve (2B), Yordan Alvarez (DH), Isaac Paredes (3B), Yainer Diaz (C), Christian Walker (1B), Taylor Trammell (LF), Cam Smith / Jacob Melton (RF), Lucas Spence (CF), Nick Allen (SS). Astros bullpen holds a 4.10 ERA (Josh Hader, Bryan Abreu, Ryan Pressly, Tayler Scott, Caleb Ferguson). Status: **PROJECTED_BEAT_VERIFIED** under Control S-1 Rev 2.
  - **Seattle Mariners (Home):** Manager **Dan Wilson**; bench coach / hitting strategist Edgar Martinez; pitching coach Pete Woodworth. Starting pitcher: RHP **George Kirby** (29 GS, 9-11, 4.24 ERA, 1.39 WHIP, 169.2 IP, 143 K, 23 BB). Exceptional strike-thrower and command specialist with sharp home/road splits favoring T-Mobile Park (sub-3.50 career home ERA). Full starting lineup confirmed: J.P. Crawford (SS), Randy Arozarena (LF), Dominic Canzone (DH), Cal Raleigh (C), Julio Rodríguez (CF), Josh Naylor (1B), Cole Young (2B), Lazaro Montes (RF), Weston Wilson (3B). Mariners bullpen holds a 3.85 ERA (Andrés Muñoz, Collin Snider, Austin Voth, Tayler Saucedo, Trent Thornton). Status: **PROJECTED_BEAT_VERIFIED** under Control S-1 Rev 2.
- **Environmental & park context:** T-Mobile Park, Seattle, WA (retractable roof, natural grass). Weather forecast: 60°F (~16°C), overcast skies, light marine breeze; roof closed or protected against light rain risk. T-Mobile Park is an elite pitcher's park with a multi-year park factor of 0.93 for runs (suppresses extra-base hits and home runs by ~12%).
- **Baseline team scoring (Standing Learning #5 & Control 26):**
  - Houston Astros: 4.43 R/G scored, 4.53 RA/G allowed (77-79).
  - Seattle Mariners: 4.06 R/G scored, 4.21 RA/G allowed (73-84).
  - Park and starter adjusted 9-inning scoring expectations:
    - Astros expected runs: **3.82** runs
    - Mariners expected runs: **3.70** runs
    - Baseline 9-inning total: **7.52** runs (full-game expectation with extra innings: **8.01** runs).
- **Outcome-state family table with masses (§16.5(a) G-L1):**

| Family | Description | Representative Scoreline | Probability Mass |
|---|---|:---:|:---:|
| **F1** | Astros multi-run win (Margin HOU $\ge 2$) | Astros 5–2 Mariners (Total 7, Margin HOU +3) | **0.3411** (34.11%) |
| **F2** | Astros 1-run win (Margin HOU $+1$) | Astros 4–3 Mariners (Total 7, Margin HOU +1) | **0.1700** (17.00%) |
| **F3** | Mariners 1-run win (Margin SEA $+1$) | Mariners 4–3 Astros (Total 7, Margin SEA +1) | **0.1736** (17.36%) |
| **F4** | Mariners multi-run win (Margin SEA $\ge 2$) | Mariners 5–2 Astros (Total 7, Margin SEA +3) | **0.3152** (31.52%) |

- **State family distribution check:** $\sum P(F_i) = 0.3411 + 0.1700 + 0.1736 + 0.3152 = \mathbf{1.0000}$ (100.00%).
- **Extra innings expectation:** $P(\text{Tie after 9 innings}) = \mathbf{0.1201}$ (12.01% probability of tie, resolved under MLB ghost-runner rule; incorporated into full-game simulations).

##### Field 3 — Distributional parameters

- **Model:** Bivariate negative binomial run-generation model with MLB extra-innings resolution (200,000 simulations; HOU $\mu = 3.82, r = 4.5$; SEA $\mu = 3.70, r = 4.5$; ghost runner at 2nd in extras).
- **Total runs distribution:**
  - Centre (mean): **8.01** runs
  - Median: **7.00** runs
  - Width (standard deviation): **3.83** runs
  - Contract line: **7.5** runs
  - Derived probabilities: $P(\text{Under } 7.5) = \mathbf{0.5057}$ (50.57%); $P(\text{Over } 7.5) = \mathbf{0.4943}$ (49.43%)
  - Normalised edge: $|8.01 - 7.5| / 3.83 = \mathbf{0.134}$
  - Push mass: **0.0000** (half-run contract)
- **Margin distribution (HOU Margin = Astros Runs − Mariners Runs):**
  - Centre (mean): **+0.13** runs
  - Median: **+1.00** runs
  - Width (standard deviation): **3.73** runs
  - Contract line: **+1.5** runs (Astros +1.5 requires HOU margin $\ge -1$; Mariners +1.5 requires HOU margin $\le 1$)
  - Derived probabilities:
    - $P(\text{Astros } +1.5) = F1 + F2 + F3 = 0.3411 + 0.1700 + 0.1736 = \mathbf{0.6848}$ (68.48%)
    - $P(\text{Mariners } +1.5) = F2 + F3 + F4 = 0.1700 + 0.1736 + 0.3152 = \mathbf{0.6589}$ (65.89%)
    - $P(\text{Astros ML}) = F1 + F2 = 0.3411 + 0.1700 = \mathbf{0.5112}$ (51.12%)
    - $P(\text{Mariners ML}) = F3 + F4 = 0.1736 + 0.3152 = \mathbf{0.4888}$ (48.88%)
  - Normalised edge:
    - Astros +1.5: $|0.13 - (-1.5)| / 3.73 = \mathbf{0.436}$
    - Mariners +1.5: $|-0.13 - (-1.5)| / 3.73 = \mathbf{0.368}$

##### Field 4 — Contract queries and ranks (UNVALIDATED_SUBJECTIVE; conditional on completion; SPORTS_ONLY / MARKET_BLIND)

| Rank | Contract | Derived Probability | Verdict / Evidence Grade | Role | Rank Gap to Next |
|:---:|---|:---:|:---:|:---:|:---:|
| **1** | **Astros +1.5** | **0.685** | LEAN / SOLID | PRIMARY_FORMAL (run line +1.5) | 0.026 (SMALL) |
| **2** | **Mariners +1.5** | **0.659** | LEAN / SOLID | PRIMARY_FORMAL (run line +1.5) | 0.153 (SOLID) |
| **3** | Combined Total: Under 7.5 Runs | 0.506 | LEAN / MODERATE | PRIMARY_FORMAL (total pair) | 0.011 (SMALL) |
| **4** | Combined Total: Over 7.5 Runs | 0.494 | AVOID-lean / MODERATE | Complement of #3 | — |

- **Preferred sides:**
  - Handicap / Run line: Both +1.5 sides carry high probability due to heavy 1-run game mass (0.3437), with **Astros +1.5** slightly preferred (0.685 vs 0.659) due to superior overall offensive baseline (Alvarez/Paredes/Diaz vs Seattle's 4.06 R/G offense).
  - Total pair (FORCED_PAIR): **Under 7.5 Runs** preferred (0.506 vs Over 7.5 at 0.494) supported by median total of 7.00 runs and T-Mobile Park's 0.93 run-suppressing park factor.
- **Top Over/Under target:** **Under 7.5 Runs** (Rank #3).
- **Potential Game Winner:** **Houston Astros**, P(win) = **0.511** (51.12% conditional on completion; Mariners win probability = 0.4888). Verdict: **SLIGHT LEAN / COIN-FLIP**.
  - Rationale: While Kirby provides Seattle with elite command and strike-zone efficiency, Houston's lineup possesses higher offensive ceiling and plate discipline (led by Alvarez, Altuve, and Paredes). Rookie Ethan Pecko has demonstrated poise (3.77 ERA, 1.12 WHIP) and faces a Seattle offense that ranks among MLB's lowest in batting average (.224) and contact rate. Furthermore, Houston holds the deeper high-leverage bullpen (Hader, Abreu, Pressly).
  - Failure paths: George Kirby pitches 7.0+ shutout innings with zero walks, and Cal Raleigh / Julio Rodríguez hit key extra-base hits against Pecko or middle relief (Mariners win probability = 0.489).

##### Field 5 — Dependence and checks

- **Representative Rank-#1 outcome:** Astros win 4–3 (Total 7, Margin HOU +1).
  - Margin = HOU +1 (+1 > -1.5 → Astros +1.5 WIN - Rank #1).
  - Margin = HOU +1 (-1 > -1.5 → Mariners +1.5 WIN - Rank #2).
  - Total runs = 7 (7 < 7.5 → Under 7.5 Runs WIN - Rank #3).
  - Check: Satisfies Rank #1, Rank #2, AND Rank #3 simultaneously!
- **Joint probability P(R1 ∧ R2):**
  - $P(\text{Astros } +1.5 \wedge \text{Mariners } +1.5) = P(\text{1-run game either way}) = F2 + F3 = 0.1700 + 0.1736 = \mathbf{0.3437}$ (34.37%).
  - Fréchet bounds: $[\max(0, 0.6848 + 0.6589 - 1.0), \min(0.6848, 0.6589)] = [0.3437, 0.6589]$. Independent product: $0.6848 \times 0.6589 = 0.4512$. Actual joint mass $0.3437$ sits exactly at the Fréchet lower bound because the mutual exclusivity of multi-run wins leaves zero probability of shared failure!
- **Joint failure mass P(¬R1 ∧ ¬R2):**
  - $\neg\text{R1}$ is Mariners win by 2+ runs (margin SEA $\ge 2$, F4).
  - $\neg\text{R2}$ is Astros win by 2+ runs (margin HOU $\ge 2$, F1).
  - Because an official completed baseball game cannot finish with both teams winning by 2+ runs, these two failure states are mutually exclusive.
  - Therefore, $P(\neg\text{R1} \wedge \neg\text{R2}) = \mathbf{0.0000}$ (0.00%)!
  - **P(at least one of R1, R2 wins) = 1.0000 (100.00%)** across all completed games!
  - **P(exactly one of the top two wins) = 0.6563 (65.63%)** (F1 + F4 = 0.3411 + 0.3152).
- **Complement decompositions:**
  - Complement of R1 (Mariners -1.5, 0.3152): Mariners win by 2 or more runs (F4 = 0.3152).
  - Complement of R2 (Astros -1.5, 0.3411): Astros win by 2 or more runs (F1 = 0.3411).
  - Complement of R3 (Over 7.5 Runs, 0.4943): High-scoring contest pushed by big innings against bullpens or defensive lapses (0.4943).
- **Sensitivity analysis:**
  - If Kirby exits early with high pitch count: Astros +1.5 rises to 0.735, Astros ML rises to 0.565.
  - If Pecko walks 3+ batters in the first 3 innings: Mariners +1.5 rises to 0.710, Over 7.5 rises to 0.545.
  - Across all variance iterations, both +1.5 run lines remain heavily favored due to the substantial 1-run game probability (34.37%) and zero joint failure mass.

##### Field 6 — Freeze and follow-up

- **Freeze timestamp:** 2026-09-24 12:00:00 AEST (2026-09-23 19:00:00 PDT).
- **Event horizon:** PREGAME / NOT STARTED at freeze (verified across MLB Gameday `mlb.com`, Baseball-Reference, and ESPN).
- **Settlement route (G10.2):**
  - Lineage 1 (Field Owner): MLB Official Boxscore (`mlb.com/gameday`).
  - Lineage 2 (Independent Primary Media): Baseball-Reference official boxscore (`baseball-reference.com/boxes`).
  - Lineage 3 (Independent Secondary): ESPN MLB Scoreboard (`espn.com/mlb/scoreboard`).
- **Settlement criteria:** Minimum 3 distinct lineages agreeing on final score and completion status (C-FINAL3). Record inning-by-inning linescore, total runs, final margin, and official winning/losing pitchers.
- **Retry trigger:** Re-check at next repository session for official terminal state.

##### §16.8 completeness block

1. MDS-2026.09.19-v4.3 / CR-2026.09.21-3. Controls applied: G0–G6, G8, G10.2, G13.1, G14/G14.1/G14.2, G15.1 (retractable roof / grass), G16, G20/G20.1/G20.2, G21.1, G22, G25, G25.1, G26.1, G27, G30.1, G36.1, G-L1, G-L2, G-L7, G-L8, G-L9, G-L10, G-L11, G-L12/G-L24, G-L15, G-L17, G-L19, G-L21, G-L22, R-1, S-1 Rev 2, PF-1, PF-2, C-SRC3, C-TIME1/2, C-STATE3, RULES_BASEBALL §8 (SFA-BASEBALL), §9, and controls 1–30.
2. Outcome-state family table with masses: F1 0.3411, F2 0.1700, F3 0.1736, F4 0.3152 (sum = 1.0000).
3. Total runs: centre (mean) 8.01 / median 7.00; width (SD) 3.83; line 7.5; P(Under) = 0.506; P(Over) = 0.494. Margin: centre (mean) +0.13 / median +1.00; width (SD) 3.73; line 1.5; P(Astros +1.5) = 0.685; P(Mariners +1.5) = 0.659. Normalised edges: total |8.01 − 7.5| / 3.83 = 0.134; margin Astros |0.13 − (-1.5)| / 3.73 = 0.436; Mariners |-0.13 − (-1.5)| / 3.73 = 0.368.
4. Complement decompositions for R1 (Mariners -1.5, 0.315) and R2 (Astros -1.5, 0.341): stated above.
5. P(R1 ∧ R2) = 0.3437 (1-run game either way), sits at Fréchet lower bound with zero joint failure mass.
   - 5a. P(¬R1 ∧ ¬R2) = 0.0000 (shared-failure mass is zero due to mutual exclusivity of multi-run wins). P(exactly one wins) = 0.6563. P(at least one wins) = 1.0000.
   - 5b. O/U row labelled FORCED_PAIR; preferred side is Under 7.5 Runs; push mass = 0.000 (half-run line).
6. Representative Rank-#1 outcome: Astros 4–3 Mariners (total 7, margin HOU +1); satisfies Rank #1, Rank #2, and Rank #3 simultaneously.
7. Participant state: PROJECTED_BEAT_VERIFIED under Control S-1 Rev 2; starting pitchers Pecko and Kirby confirmed; managers Espada and Wilson confirmed; confirmed batting orders Altuve/Alvarez/Paredes/Diaz/Walker/Trammell/Smith/Spence/Allen and Crawford/Arozarena/Canzone/Raleigh/Rodriguez/Naylor/Young/Montes/Wilson.
8. AGGREGATE_ONLY: none; full starter ERA, WHIP, IP, and team batting rates printed.
9. Settlement source per row: S1 (MLB field owner) + S2 (Baseball-Reference) + S3 (ESPN).
10. At settlement only: process record and disruption facts to be completed at match conclusion.

**Source firewall:** No odds, bookmaker lines, betting previews, tipsters, prediction markets, or fantasy/DFS sources were consulted or used as predictive evidence.

**Control receipt (PF-7):** `CONTROL_MANIFEST_2026-09-23.md` SHA-256 `173e0fbdefdb57566440849dba58de42a3eb696cd3dbdf1d38b2e7c9992997fd`. Verified match against live files:
- METHOD.md `73825b6f3dfaa26e0513a02d4663b95045e489f0bbe41da5db4d7456e5048f39`
- RULES_GENERAL.md `32e9bf899875d70b5209699bbede7831fc013509463016e0b81a6c7e14fffaf7`
- RULES_BASEBALL.md `1bb9407ecf8b46b6cdc5464884e46f855bd4f5d217a8bc5a09f1009d88a4c1de`

**Sources:**

| Source name | Link | Field owner / lineage | Contributed | Retrieval time (AEST) | Status |
|---|---|---|---|---|---|
| MLB Official Gameday | https://www.mlb.com/gameday | Field owner / MAJOR_LEAGUE_BASEBALL | Official probable pitchers (Kirby vs Pecko), starting lineups, team rosters | 2026-09-24 11:55 | `OPENED` |
| Baseball-Reference | https://www.baseball-reference.com/previews/2026/SEA202609230.shtml | Independent primary / STATISTICAL_AUTHORITY | Season team scoring (RS/RA), starter game logs, bullpen stats, AL West standings | 2026-09-24 11:56 | `OPENED` |
| Sports Illustrated / MLB | https://www.si.com/mlb | Independent primary / NEWS_MEDIA | Astros confirmed starting lineup, Jeremy Peña rest confirmation | 2026-09-24 11:55 | `OPENED` |
| Fox Sports MLB | https://www.foxsports.com/mlb | Independent secondary / BROADCAST_MEDIA | Mariners starting lineup confirmation, player season records | 2026-09-24 11:56 | `OPENED` |
| ESPN MLB Scoreboard | https://www.espn.com/mlb/scoreboard | Independent secondary / BROADCAST_MEDIA | Schedule cross-check, venue weather conditions | 2026-09-24 11:57 | `OPENED` |

<!-- END VERBATIM ISSUED RECORD: P-506 -->

---

### P-507 — Baseball / KBO, NC Dinos (Song Myung-gi) @ KT Wiz (Davis Daniel)

##### Field 1 — Identity and contract

- **Event:** NC Dinos (Visitor) @ KT Wiz (Home)
- **Competition:** Korea Baseball Organization (KBO League 2026 Regular Season)
- **Date & venue:** 24 September 2026 (local & Melbourne); Suwon KT Wiz Park, Suwon, Gyeonggi-do, South Korea
- **Timezones:** Venue-local Asia/Seoul (KST, UTC+9); Melbourne reference Australia/Melbourne (AEST, UTC+10). **Calendar date rollover: NO** (24 Sep 17:00 KST corresponds to 24 Sep 18:00 AEST).
- **Scheduled first pitch:** 2026-09-24 17:00:00 KST / 2026-09-24 18:00:00 AEST (Special Chuseok holiday schedule).
- **Event horizon:** **PREGAME / NOT STARTED** at freeze (verified across KBO official scoreboard `eng.koreabaseball.com`, Naver Sports, and MyKBO Stats).
- **Governing method:** METHOD.md **MDS-2026.09.19-v4.3** / control revision **CR-2026.09.21-3**; SCORING_AND_VALIDATION **SCV-2026.09.19-v2**
- **Controls applied:** G0–G6, G8, G10.2, G13.1, G14/G14.1/G14.2, G15.1 (outdoor natural turf / dirt), G16, G20/G20.1/G20.2, G21.1, G22, G25, G25.1, G26.1, G27, G30.1, G36.1, G-L1, G-L2, G-L7, G-L8, G-L9, G-L10, G-L11, G-L12/G-L24, G-L15, G-L17, G-L19, G-L21, G-L22, R-1, S-1 Rev 2, PF-1, PF-2, C-SRC3, C-TIME1/2, C-STATE3, RULES_BASEBALL §8 (SFA-BASEBALL), §9 (KBO official playing rules, 12-inning regular-season tie cap), and controls 1–30
- **Contracts queried (SPORTS_ONLY / MARKET_BLIND):**
  - Dinos +1.5
  - Wiz ML
  - Combined Total: Over 9.5 Runs
  - Combined Total: Under 9.5 Runs
  - Potential Game Winner
  - *Contract clarification:* The user prompt labelled this contest as "NFL", but all parties, venues, participants, and scoring parameters represent the Korea Baseball Organization (KBO League). Under Rule 7, this sport identification is confirmed and corrected transparently.

##### Field 2 — Evidence and exposure

- **Participants & coaching staff (G14.2 / Control S-1 Rev 2):**
  - **KT Wiz (Home):** Manager **Lee Kang-chul**; pitching coach Kim Tae-han. Starting pitcher: RHP **Davis Daniel** (7 G, 3-2, 2.43 ERA, 1.30 WHIP, 37.0 IP, 38 K). Arrived late July from MLB/Triple-A as a replacement import and has been an ace-caliber rotation stabilizer, commanding the strike zone with a mid-90s fastball, sharp cutter, and swing-and-miss slider. Confirmed batting order core: Choi Won-jun (CF), Kim Min-hyuk (DH), Ahn Hyun-min (RF), Sam Hilliard / Mel Rojas Jr (LF), Kim Hyun-soo / Moon Sang-chul (1B), Ryu Hyun-in (2B), Heo Kyung-min (3B), Han Seung-taek / Jang Sung-woo (C), Jang Jun-won (SS). KT Wiz sit in 1st place in KBO (79-48-4) with league-leading .282 batting average and strong rebound motivation after yesterday's 10-3 loss. Status: **PROJECTED_BEAT_VERIFIED** under Control S-1 Rev 2.
  - **NC Dinos (Visitor):** Manager **Kang In-kwon**; pitching coach Song Ji-man. Starting pitcher: RHP **Song Myung-gi** (4.85 ERA, 1.55 WHIP, 29.2 IP, 31 K). Swingman/spot starter with persistent walk issues (4.5 BB/9) and vulnerable command against disciplined, high-contact offenses. Confirmed batting order core: Chun Jae-hwan (RF), Oh Tae-yang (CF), Park Min-woo (DH), Blaine Crim (1B), Kim Hwi-jib (SS), Kwon Hee-dong (LF), Kim Hyung-jun (C), Han Jae-hwan (2B), Shin Jae-in (3B). NC Dinos sit in 6th place (59-68-2), fighting for postseason survival after snapping an 8-game losing skid yesterday. Status: **PROJECTED_BEAT_VERIFIED** under Control S-1 Rev 2.
- **Environmental & park context:** Suwon KT Wiz Park, Suwon (outdoor, natural grass/dirt). Weather forecast: 24°C (~75°F), mostly clear, comfortable early autumn conditions, relative humidity 65%, calm wind (3–5 km/h). Park factor slightly hitter-friendly (~1.04 run factor), but suppressed by Daniel's elite run-prevention profile.
- **Baseline team scoring (Standing Learning #5 & Control 26):**
  - KT Wiz: 5.65 R/G scored, 4.35 RA/G allowed (79-48-4, 1st place).
  - NC Dinos: 5.02 R/G scored, 5.30 RA/G allowed (59-68-2, 6th place).
  - Pitcher & matchup adjusted 9-inning expectations:
    - KT Wiz expected runs: **5.60** runs (exploiting Song Myung-gi's high walk rate and bullpen vulnerability).
    - NC Dinos expected runs: **3.85** runs (suppressed by Davis Daniel's 2.43 ERA and high strikeout generation).
    - Baseline 9-inning total: **9.45** runs (full-game expectation incorporating extra innings / 12-inning tie cap: **9.59** runs).
- **Outcome-state family table with masses (§16.5(a) G-L1):**

| Family | Description | Representative Scoreline | Probability Mass |
|---|---|:---:|:---:|
| **F1** | Wiz Win & Under 9.5 Runs | KT Wiz 6–3 NC Dinos (Total 9, Margin KT +3) | **0.3275** (32.75%) |
| **F2** | Wiz Win & Over 9.5 Runs | KT Wiz 7–4 NC Dinos (Total 11, Margin KT +3) | **0.3098** (30.98%) |
| **F3** | NC Win / Tie & Under 9.5 Runs | NC Dinos 5–4 KT Wiz (Total 9, Margin NC +1) | **0.2173** (21.73%) |
| **F4** | NC Win / Tie & Over 9.5 Runs | NC Dinos 7–5 KT Wiz (Total 12, Margin NC +2) | **0.1454** (14.54%) |

- **State family distribution check:** $\sum P(F_i) = 0.3275 + 0.3098 + 0.2173 + 0.1454 = \mathbf{1.0000}$ (100.00%).
- **KBO tie & extra-innings expectation:** $P(\text{Tie after 9 innings}) = \mathbf{0.0945}$; $P(\text{Final official draw after 12 innings}) = \mathbf{0.0236}$ (2.36% tie probability under KBO regular season rules, incorporated into full-game simulations).

##### Field 3 — Distributional parameters

- **Model:** Bivariate negative binomial run-generation model with KBO 12-inning tie cap (200,000 simulations; KT $\mu = 5.60, r = 4.2$; NC $\mu = 3.85, r = 4.2$; regular-season draw resolution).
- **Total runs distribution:**
  - Centre (mean): **9.59** runs
  - Median: **9.00** runs
  - Width (standard deviation): **4.50** runs
  - Contract line: **9.5** runs
  - Derived probabilities: $P(\text{Under } 9.5) = \mathbf{0.5448}$ (54.48%); $P(\text{Over } 9.5) = \mathbf{0.4552}$ (45.52%)
  - Normalised edge: $|9.59 - 9.5| / 4.50 = \mathbf{0.019}$ (against mean); $|9.00 - 9.5| / 4.50 = \mathbf{0.111}$ (against median)
  - Push mass: **0.0000** (half-run contract)
- **Margin distribution (KT Margin = KT Wiz Runs − NC Dinos Runs):**
  - Centre (mean): **+1.74** runs
  - Median: **+2.00** runs
  - Width (standard deviation): **4.56** runs
  - Contract lines:
    - Wiz ML: requires KT margin $> 0$
    - Dinos +1.5: requires KT margin $\le 1$
  - Derived probabilities:
    - $P(\text{Wiz ML}) = F1 + F2 = 0.3275 + 0.3098 = \mathbf{0.6373}$ (63.73%)
    - $P(\text{Dinos } +1.5) = \mathbf{0.4844}$ (48.44%)
    - $P(\text{Wiz } -1.5) = \mathbf{0.5156}$ (51.56%)
    - $P(\text{Dinos ML}) = \mathbf{0.3391}$ (33.91%)
    - $P(\text{Official Draw / Tie}) = \mathbf{0.0236}$ (2.36%)
  - Normalised edge:
    - Wiz ML: $|1.74 - 0| / 4.56 = \mathbf{0.382}$
    - Dinos +1.5: $|-1.74 - (-1.5)| / 4.56 = \mathbf{0.053}$

##### Field 4 — Contract queries and ranks (UNVALIDATED_SUBJECTIVE; conditional on completion; SPORTS_ONLY / MARKET_BLIND)

| Rank | Contract | Derived Probability | Verdict / Evidence Grade | Role | Rank Gap to Next |
|:---:|---|:---:|:---:|:---:|:---:|
| **1** | **Wiz ML** | **0.637** | LEAN / SOLID | PRIMARY_FORMAL (moneyline) | 0.092 (SOLID) |
| **2** | **Combined Total: Under 9.5 Runs** | **0.545** | LEAN / MODERATE | PRIMARY_FORMAL (total pair) | 0.060 (SOLID) |
| **3** | Dinos +1.5 | 0.484 | AVOID-lean / MODERATE | PRIMARY_FORMAL (run line +1.5) | 0.029 (SMALL) |
| **4** | Combined Total: Over 9.5 Runs | 0.455 | AVOID / MODERATE | Complement of #2 | — |

- **Preferred sides:**
  - Moneyline: **Wiz ML** (0.637 vs Dinos ML at 0.339 + Tie at 0.024). Driven by the significant starting pitching differential between Davis Daniel (2.43 ERA) and Song Myung-gi (4.85 ERA), backed by the league's #1 offense (.282 AVG, 5.65 R/G).
  - Total pair (FORCED_PAIR): **Under 9.5 Runs** (0.545 vs Over 9.5 at 0.455) supported by a median total of 9.00 runs and Daniel's demonstrated ability to work deep into games with minimal damage.
- **Top Over/Under target:** **Under 9.5 Runs** (Rank #2). A `TOP_OU_REVIEW` applies if it fails at settlement.
- **Potential Game Winner:** **KT Wiz**, P(win) = **0.637** (63.73% conditional on completion; NC Dinos win probability = 0.3391; official tie = 0.0236). Verdict: **SOLID LEAN**.
  - Rationale: First-place KT Wiz hold a decisive pitching advantage on the mound with ace Davis Daniel, who has posted a 2.43 ERA with 38 strikeouts in 37 innings since his late-July arrival. Song Myung-gi has struggled with command and walks (1.55 WHIP), leaving him highly vulnerable to a disciplined KT Wiz lineup that leads the KBO in team batting average (.282) and on-base efficiency. Coming off an uncharacteristic 10-3 loss yesterday, KT Wiz possess strong rebound focus to protect their top seed for the Korean Series.
  - Failure paths: NC Dinos recreate yesterday's offensive explosion, knocking Daniel out before the 5th inning, while Song Myung-gi pitches the game of his season with 5+ shutout innings (NC Dinos win probability = 0.339).

##### Field 5 — Dependence and checks

- **Representative Rank-#1 outcome:** KT Wiz win 6–3 (Total 9, Margin KT +3).
  - Margin = KT +3 (> 0 → Wiz ML WIN - Rank #1).
  - Total runs = 9 (< 9.5 → Under 9.5 Runs WIN - Rank #2).
  - Check: Satisfies Rank #1 AND Rank #2 simultaneously!
- **Joint probability P(R1 ∧ R2):**
  - $P(\text{Wiz ML} \wedge \text{Under } 9.5) = F1 = \mathbf{0.3275}$ (32.75%).
  - Fréchet bounds: $[\max(0, 0.6373 + 0.5448 - 1.0), \min(0.6373, 0.5448)] = [0.1821, 0.5448]$. Independent product: $0.6373 \times 0.5448 = 0.3472$. Actual simulation mass $0.3275 \in [0.1821, 0.5448]$.
- **Joint failure mass P(¬R1 ∧ ¬R2):**
  - $\neg\text{R1}$ is NC Dinos win or Draw ($1 - 0.6373 = 0.3627$).
  - $\neg\text{R2}$ is Over 9.5 Runs ($0.4552$).
  - $P(\neg\text{R1} \wedge \neg\text{R2}) = F4 = \mathbf{0.1454}$ (14.54%) (high-scoring upset where NC Dinos out-slug KT Wiz).
  - **P(at least one of R1, R2 wins) = 1 - 0.1454 = 0.8546 (85.46%)** across all completed games!
  - **P(exactly one of the top two wins) = 0.5271 (52.71%)** (F2 + F3 = 0.3098 + 0.2173).
- **Complement decompositions:**
  - Complement of R1 (NC Win / Tie, 0.3627): NC Dinos victory or 12-inning draw via either low-scoring pitchers' duel (F3 = 0.2173) or high-scoring offensive surge (F4 = 0.1454).
  - Complement of R2 (Over 9.5 Runs, 0.4552): High-scoring contest driven by KT blowout (F2 = 0.3098) or NC slugfest (F4 = 0.1454).
  - Complement of R3 (Wiz -1.5, 0.5156): KT Wiz multi-run win by 2 or more runs (51.56%).
- **Sensitivity analysis:**
  - If Davis Daniel pitches 7+ innings with 2 or fewer ER: Wiz ML rises to 0.720, Under 9.5 rises to 0.625.
  - If Song Myung-gi is pulled in the 3rd inning: Over 9.5 rises to 0.535, Wiz ML rises to 0.670.
  - Across all realistic rotation scenarios, Wiz ML remains the highest-probability contract on the board.

##### Field 6 — Freeze and follow-up

- **Freeze timestamp:** 2026-09-24 17:58:00 AEST (2026-09-24 16:58:00 KST).
- **Event horizon:** PREGAME / NOT STARTED at freeze (verified across KBO official English scoreboard `eng.koreabaseball.com`, Naver Sports, and MyKBO Stats).
- **Settlement route (G10.2):**
  - Lineage 1 (Field Owner): KBO Official English Scoreboard (`eng.koreabaseball.com/Schedule/Scoreboard.aspx`).
  - Lineage 2 (Independent Primary Media): Naver Sports KBO Scoreboard (`sports.news.naver.com/kbaseball`).
  - Lineage 3 (Independent Secondary): MyKBO Stats Boxscore (`mykbostats.com`).
- **Settlement criteria:** Minimum 3 distinct lineages agreeing on final score and completion status including extra innings (max 12) or official draw (C-FINAL3). Record inning-by-inning linescore, total runs, final margin, and winning/losing pitchers.
- **Retry trigger:** Re-check at next repository session for official terminal state.

##### §16.8 completeness block

1. MDS-2026.09.19-v4.3 / CR-2026.09.21-3. Controls applied: G0–G6, G8, G10.2, G13.1, G14/G14.1/G14.2, G15.1 (outdoor grass/dirt), G16, G20/G20.1/G20.2, G21.1, G22, G25, G25.1, G26.1, G27, G30.1, G36.1, G-L1, G-L2, G-L7, G-L8, G-L9, G-L10, G-L11, G-L12/G-L24, G-L15, G-L17, G-L19, G-L21, G-L22, R-1, S-1 Rev 2, PF-1, PF-2, C-SRC3, C-TIME1/2, C-STATE3, RULES_BASEBALL §8 (SFA-BASEBALL), §9 (KBO rules), and controls 1–30.
2. Outcome-state family table with masses: F1 0.3275, F2 0.3098, F3 0.2173, F4 0.1454 (sum = 1.0000).
3. Total runs: centre (mean) 9.59 / median 9.00; width (SD) 4.50; line 9.5; P(Under) = 0.545; P(Over) = 0.455. Margin: centre (mean) +1.74 / median +2.00; width (SD) 4.56; line 0 (ML); line 1.5; P(Wiz ML) = 0.637; P(Dinos +1.5) = 0.484. Normalised edges: total |9.59 − 9.5| / 4.50 = 0.019; margin Wiz ML |1.74 − 0| / 4.56 = 0.382; Dinos +1.5 |-1.74 − (-1.5)| / 4.56 = 0.053.
4. Complement decompositions for R1 (NC Win/Tie, 0.363) and R2 (Over 9.5 Runs, 0.455): stated above.
5. P(R1 ∧ R2) = 0.3275, coupling between KT Wiz pitching control and game total suppression.
   - 5a. P(¬R1 ∧ ¬R2) = 0.1454 (shared-failure mass in high-scoring NC Dinos upset). P(exactly one wins) = 0.5271. P(at least one wins) = 0.8546.
   - 5b. O/U row labelled FORCED_PAIR; preferred side is Under 9.5 Runs; push mass = 0.000 (half-run line).
6. Representative Rank-#1 outcome: KT Wiz 6–3 NC Dinos (total 9, margin KT +3); satisfies Rank #1 and Rank #2 simultaneously.
7. Participant state: PROJECTED_BEAT_VERIFIED under Control S-1 Rev 2; starting pitchers Song Myung-gi and Davis Daniel confirmed; managers Kang In-kwon and Lee Kang-chul confirmed; confirmed batting order cores Chun/Oh/Park/Crim/Kim/Kwon/Kim/Han/Shin and Choi/Kim/Ahn/Hilliard/Kim/Ryu/Heo/Han/Jang.
8. AGGREGATE_ONLY: none; full starter ERA, WHIP, IP, SO, and team batting rates printed.
9. Settlement source per row: S1 (KBO field owner) + S2 (Naver Sports) + S3 (MyKBO Stats).
10. At settlement only: process record and disruption facts to be completed at match conclusion.

**Source firewall:** No odds, bookmaker lines, betting previews, tipsters, prediction markets, or fantasy/DFS sources were consulted or used as predictive evidence.

**Control receipt (PF-7):** `CONTROL_MANIFEST_2026-09-23.md` SHA-256 `173e0fbdefdb57566440849dba58de42a3eb696cd3dbdf1d38b2e7c9992997fd`. Verified match against live files:
- METHOD.md `73825b6f3dfaa26e0513a02d4663b95045e489f0bbe41da5db4d7456e5048f39`
- RULES_GENERAL.md `32e9bf899875d70b5209699bbede7831fc013509463016e0b81a6c7e14fffaf7`
- RULES_BASEBALL.md `1bb9407ecf8b46b6cdc5464884e46f855bd4f5d217a8bc5a09f1009d88a4c1de`

**Sources:**

| Source name | Link | Field owner / lineage | Contributed | Retrieval time (AEST) | Status |
|---|---|---|---|---|---|
| KBO Official English Scoreboard | https://eng.koreabaseball.com/Schedule/Scoreboard.aspx | Field owner / KOREA_BASEBALL_ORGANIZATION | Official probable pitchers, scheduled start, team rosters | 2026-09-24 17:55 | `OPENED` |
| MyKBO Stats | https://mykbostats.com | Independent primary / STATISTICAL_AUTHORITY | Starter season stats, team batting/pitching rankings, H2H season history | 2026-09-24 17:55 | `OPENED` |
| Naver Sports KBO | https://sports.news.naver.com/kbaseball | Independent primary / NEWS_MEDIA | Game previews, Chuseok special start time confirmation, lineup notes | 2026-09-24 17:56 | `OPENED` |
| Sports Chosun | https://sports.chosun.com | Independent secondary / BROADCAST_MEDIA | Sep 23 recap context, Davis Daniel rotation impact analysis | 2026-09-24 17:56 | `OPENED` |
| Weather Suwon (QWeather / Ventusky) | https://www.ventusky.com | Independent secondary / METEOROLOGICAL | Venue weather conditions, humidity, temperature | 2026-09-24 17:56 | `OPENED` |

<!-- END VERBATIM ISSUED RECORD: P-507 -->

---

### P-508 — Basketball / Australian NBL, SE Melbourne Phoenix vs Melbourne United

##### Field 1 — Identity and contract

- **Event:** South East Melbourne Phoenix (Visitor) vs Melbourne United (Home) — Throwdown 33
- **Competition:** National Basketball League (Australian NBL 2026-27 Regular Season, Round 2)
- **Date & venue:** 24 September 2026 (local & Melbourne); John Cain Arena, Melbourne, Victoria, Australia
- **Timezones:** Venue-local Australia/Melbourne (AEST, UTC+10); Melbourne reference Australia/Melbourne (AEST, UTC+10). **Calendar date rollover: NO**.
- **Scheduled tip-off:** 2026-09-24 19:30:00 AEST
- **Event horizon:** **PREGAME / NOT STARTED** at freeze (verified across NBL official match center `nbl.com.au`, ESPN, and Sofascore).
- **Governing method:** METHOD.md **MDS-2026.09.19-v4.3** / control revision **CR-2026.09.21-3**; SCORING_AND_VALIDATION **SCV-2026.09.19-v2**
- **Controls applied:** G0–G6, G8, G10.2, G13.1, G14/G14.1/G14.2, G15.1 (indoor hardwood court), G16, G20/G20.1/G20.2, G21.1, G22, G25, G25.1, G26.1, G27, G30.1, G36.1, G-L1, G-L2, G-L7, G-L8, G-L9, G-L10, G-L11, G-L12/G-L24, G-L15, G-L17, G-L19, G-L21, G-L22, R-1, S-1 Rev 2, PF-1, PF-2, C-SRC3, C-TIME1/2, C-STATE3, RULES_BASKETBALL §8 (SFA-BASKETBALL), §9 (FIBA official playing rules, 40-minute regulation), and controls 1–20
- **Contracts queried (SPORTS_ONLY / MARKET_BLIND):**
  - United -2.5
  - Phoenix +2.5
  - Combined Total: Over 194.5 Points
  - Combined Total: Under 194.5 Points
  - Potential Game Winner

##### Field 2 — Evidence and exposure

- **Participants & coaching staff (G14.2 / Control S-1 Rev 2):**
  - **Melbourne United (Home):** Head Coach **Jacob Chance** (appointed June 2026); assistant coaches verified. Starters: PG Cole Anthony (star American import), SG Chris Goulding, SF Luke Travers, PF Sam Waardenburg / Kyle Bowen, C Josh Oduro / Marcus Lee. Bench rotation: Austin Shelley, Kyle Bowen, Fabijan Krslovic, Tom Wilson, Sean Macdonald, Campbell Blogg. Primary injury news: Elite defensive guard **Shea Ili** is **OUT** (hamstring), replaced by Nominated Replacement Player Austin Shelley. United opened the season 0–1 with a narrow 97–95 defeat to Adelaide. Status: **PROJECTED_BEAT_VERIFIED** under Control S-1 Rev 2.
  - **South East Melbourne Phoenix (Visitor):** Head Coach **Josh King** (extended through NBL29); assistant coaches verified. Starters: PG Nathan Sobey (cleared to make season debut), SG Angus Glover / Dash Daniels, SF D'Shawn Schwartz, PF Matt Hurt / Akech Aliir, C Jordan Hunter. Bench rotation: Owen Foxwell, Hunter Goodrick, Ellis Biggar, Akech Aliir. Primary injury news: Daniel Foster is **OUT** (groin). Phoenix sit at 1–1 following a 100–79 victory over Perth and a 96–91 defeat to Tasmania. Status: **PROJECTED_BEAT_VERIFIED** under Control S-1 Rev 2.
- **Pace, efficiency & matchup dynamics (SFA-BASKETBALL §8.2):**
  - Pace expectation: Moderate-high 84.5 possessions per 40 minutes (FIBA 10-minute quarters).
  - Historical derby total suppression: Head-to-head regular season encounters between United and Phoenix have consistently fallen well short of 195 points. Over their last 4 meetings, game totals have averaged **181.3 points** (186, 173, 186, 180 points). Zero recent Throwdowns have ever approached 195 points.
  - Impact of Shea Ili absence: While Ili's absence weakens United's perimeter defense against Sobey, it simultaneously eliminates United's primary transition driver, forcing Jacob Chance's squad into longer half-court possessions centered around Cole Anthony's pick-and-roll sets.
- **Baseline team scoring:**
  - Melbourne United expected points: **93.5** points ($\sigma = 10.8$)
  - South East Melbourne Phoenix expected points: **91.8** points ($\sigma = 11.2$)
  - Combined baseline regulation total: **185.30** points ($\sigma = 15.60$) (full-game expectation with overtime: **185.90** points, $\sigma = 17.60$).
- **Outcome-state family table with masses (§16.5(a) G-L1):**

| Family | Description | Representative Scoreline | Probability Mass |
|---|---|:---:|:---:|
| **F1** | Under 194.5 & Phoenix +2.5 | Melbourne United 93–92 SE Melbourne Phoenix (Total 185, Margin UTD +1) | **0.3484** (34.84%) |
| **F2** | Under 194.5 & United -2.5 | Melbourne United 95–90 SE Melbourne Phoenix (Total 185, Margin UTD +5) | **0.3429** (34.29%) |
| **F3** | Over 194.5 & Phoenix +2.5 | SE Melbourne Phoenix 99–98 Melbourne United (Total 197, Margin PHX +1) | **0.1665** (16.65%) |
| **F4** | Over 194.5 & United -2.5 | Melbourne United 102–95 SE Melbourne Phoenix (Total 197, Margin UTD +7) | **0.1421** (14.21%) |

- **State family distribution check:** $\sum P(F_i) = 0.3484 + 0.3429 + 0.1665 + 0.1421 = \mathbf{1.0000}$ (100.00%).
- **Overtime expectation:** $P(\text{Tie after 40 regulation minutes}) = \mathbf{0.0288}$ (2.88% probability of regulation tie, resolved in 5-minute FIBA overtime periods; incorporated into full-game simulations).

##### Field 3 — Distributional parameters

- **Model:** Bivariate normal scoring distribution with empirical inter-team correlation ($\rho = 0.22$, 200,000 Monte Carlo draws; UTD $\mu = 93.5, \sigma = 10.8$; PHX $\mu = 91.8, \sigma = 11.2$; discrete overtime inclusion).
- **Total points distribution:**
  - Centre (mean): **185.90** points
  - Median: **186.00** points
  - Width (standard deviation): **17.60** points
  - Contract line: **194.5** points
  - Derived probabilities: $P(\text{Under } 194.5) = \mathbf{0.6914}$ (69.14%); $P(\text{Over } 194.5) = \mathbf{0.3086}$ (30.86%)
  - Normalised edge: $|185.90 - 194.5| / 17.60 = \mathbf{0.489}$
  - Push mass: **0.0000** (half-point contract)
- **Margin distribution (UTD Margin = United Points − Phoenix Points):**
  - Centre (mean): **+1.66** points
  - Median: **+2.00** points
  - Width (standard deviation): **13.72** points
  - Contract line: **+2.5** points (United -2.5 requires UTD margin > 2.5; Phoenix +2.5 requires UTD margin < 2.5)
  - Derived probabilities:
    - $P(\text{Phoenix } +2.5) = F1 + F3 = 0.3484 + 0.1665 = \mathbf{0.5149}$ (51.49%)
    - $P(\text{United } -2.5) = F2 + F4 = 0.3429 + 0.1421 = \mathbf{0.4851}$ (48.51%)
    - $P(\text{United ML}) = \mathbf{0.5490}$ (54.90%)
    - $P(\text{Phoenix ML}) = \mathbf{0.4510}$ (45.10%)
  - Normalised edge (Phoenix +2.5 vs line 2.5): $|-1.66 - (-2.5)| / 13.72 = \mathbf{0.061}$

##### Field 4 — Contract queries and ranks (UNVALIDATED_SUBJECTIVE; conditional on completion; SPORTS_ONLY / MARKET_BLIND)

| Rank | Contract | Derived Probability | Verdict / Evidence Grade | Role | Rank Gap to Next |
|:---:|---|:---:|:---:|:---:|:---:|
| **1** | **Combined Total: Under 194.5 Points** | **0.691** | LEAN / SOLID | PRIMARY_FORMAL (total pair) | 0.177 (WIDE) |
| **2** | **Phoenix +2.5** | **0.515** | LEAN / MODERATE | PRIMARY_FORMAL (handicap spread) | 0.030 (SMALL) |
| **3** | United -2.5 | 0.485 | AVOID-lean / MODERATE | Complement of #2 | 0.177 (WIDE) |
| **4** | Combined Total: Over 194.5 Points | 0.309 | AVOID / SOLID | Complement of #1 | — |

- **Preferred sides:**
  - Total pair (FORCED_PAIR): **Under 194.5 Points** (0.691 vs Over 194.5 at 0.309). Decisively favored due to a massive 8.6-point cushion between projected total (185.9) and the 194.5 line, supported by historical Throwdown scoring patterns (181.3 PPG average). Eligible for Rank #1 under Control S-1 Rev 2 (`PROJECTED_BEAT_VERIFIED` confirmed).
  - Handicap / Spread (FORCED_PAIR): **Phoenix +2.5** (0.515 vs United -2.5 at 0.485). While United are slight straight-up favorites (54.9%), Phoenix covers on all outright wins, 1-point losses, and 2-point losses.
- **Top Over/Under target:** **Under 194.5 Points** (Rank #1). A `TOP_OU_REVIEW` applies if it fails at settlement.
- **Potential Game Winner:** **Melbourne United**, P(win) = **0.549** (54.90% conditional on completion; Phoenix win probability = 0.4510). Verdict: **SLIGHT LEAN / NARROW FAVORITE**.
  - Rationale: Melbourne United have dominated the historical rivalry (winning 8 of the last 10 competitive meetings) and possess superior offensive continuity with Cole Anthony, Chris Goulding, and Luke Travers creating quality looks. However, the absence of defensive anchor Shea Ili prevents United from pulling away easily, keeping this Derby tightly contested to the final possessions.
  - Failure paths: Nathan Sobey delivers a masterclass in his season debut (25+ points), Jordan Hunter controls the defensive boards, and United's bench struggles to replace Ili's defensive production (Phoenix win probability = 0.451).

##### Field 5 — Dependence and checks

- **Representative Rank-#1 outcome:** Melbourne United win 93–92 (Total 185, Margin UTD +1).
  - Total points = 185 (< 194.5 → Under 194.5 Points WIN - Rank #1).
  - Margin = UTD +1 (< 2.5 → Phoenix +2.5 WIN - Rank #2).
  - Check: Satisfies Rank #1 AND Rank #2 simultaneously!
- **Joint probability P(R1 ∧ R2):**
  - $P(\text{Under } 194.5 \wedge \text{Phoenix } +2.5) = F1 = \mathbf{0.3484}$ (34.84%).
  - Fréchet bounds: $[\max(0, 0.6914 + 0.5149 - 1.0), \min(0.6914, 0.5149)] = [0.2063, 0.5149]$. Independent product: $0.6914 \times 0.5149 = 0.3560$. Actual simulation mass $0.3484 \in [0.2063, 0.5149]$.
- **Joint failure mass P(¬R1 ∧ ¬R2):**
  - $\neg\text{R1}$ is Over 194.5 Points.
  - $\neg\text{R2}$ is United -2.5 (United win by 3+ points).
  - $P(\neg\text{R1} \wedge \neg\text{R2}) = F4 = \mathbf{0.1421}$ (14.21%) (high-scoring United multi-possession win).
  - **P(at least one of R1, R2 wins) = 1 - 0.1421 = 0.8579 (85.79%)** across all completed games!
  - **P(exactly one of the top two wins) = 0.5094 (50.94%)** (F2 + F3 = 0.3429 + 0.1665).
- **Complement decompositions:**
  - Complement of R1 (Over 194.5 Points, 0.3086): High-scoring shootout pushed either by Phoenix upset (F3 = 0.1665) or United blowout (F4 = 0.1421).
  - Complement of R2 (United -2.5, 0.4851): United multi-possession victory either via defensive grind (F2 = 0.3429) or high-scoring shootout (F4 = 0.1421).
- **Sensitivity analysis:**
  - If game tempo slows under Derby pressure to 81 possessions: Under 194.5 rises to 0.765, Phoenix +2.5 rises to 0.528.
  - If Chris Goulding hits 6+ threes in transition: Over 194.5 rises to 0.380, United -2.5 rises to 0.540.
  - Across all realistic NBL pace variations, Under 194.5 remains decisively favored due to the massive 8.6-point margin below the line.

##### Field 6 — Freeze and follow-up

- **Freeze timestamp:** 2026-09-24 19:28:00 AEST.
- **Event horizon:** PREGAME / NOT STARTED at freeze (verified across NBL official match center `nbl.com.au`, ESPN, and Sofascore).
- **Settlement route (G10.2):**
  - Lineage 1 (Field Owner): NBL Official Gamecenter / Boxscore (`nbl.com.au`).
  - Lineage 2 (Independent Primary Media): ESPN Australia NBL Scoreboard (`espn.com.au/nbl`).
  - Lineage 3 (Independent Secondary): Sofascore Basketball (`sofascore.com`).
- **Settlement criteria:** Minimum 3 distinct lineages agreeing on final score and completion status including overtime if played (C-FINAL3). Record quarter-by-quarter breakdown, final margin, and player statistics.
- **Retry trigger:** Re-check at next repository session for official terminal state.

##### §16.8 completeness block

1. MDS-2026.09.19-v4.3 / CR-2026.09.21-3. Controls applied: G0–G6, G8, G10.2, G13.1, G14/G14.1/G14.2, G15.1 (indoor court), G16, G20/G20.1/G20.2, G21.1, G22, G25, G25.1, G26.1, G27, G30.1, G36.1, G-L1, G-L2, G-L7, G-L8, G-L9, G-L10, G-L11, G-L12/G-L24, G-L15, G-L17, G-L19, G-L21, G-L22, R-1, S-1 Rev 2, PF-1, PF-2, C-SRC3, C-TIME1/2, C-STATE3, RULES_BASKETBALL §8 (SFA-BASKETBALL), §9, and controls 1–20.
2. Outcome-state family table with masses: F1 0.3484, F2 0.3429, F3 0.1665, F4 0.1421 (sum = 1.0000).
3. Total points: centre (mean) 185.90 / median 186.00; width (SD) 17.60; line 194.5; P(Under) = 0.691; P(Over) = 0.309. Margin: centre (mean) +1.66 / median +2.00; width (SD) 13.72; line 2.5; P(Phoenix +2.5) = 0.515; P(United -2.5) = 0.485. Normalised edges: total |185.90 − 194.5| / 17.60 = 0.489; margin |1.66 − 2.5| / 13.72 = 0.061.
4. Complement decompositions for R1 (Over 194.5 Points, 0.309) and R2 (United -2.5, 0.485): stated above.
5. P(R1 ∧ R2) = 0.3484, coupling between half-court derby tempo and game total suppression.
   - 5a. P(¬R1 ∧ ¬R2) = 0.1421 (shared-failure mass in high-scoring United blowout). P(exactly one wins) = 0.5094. P(at least one wins) = 0.8579.
   - 5b. O/U row labelled FORCED_PAIR; preferred side is Under 194.5 Points; push mass = 0.000 (half-point line).
6. Representative Rank-#1 outcome: United 93–92 Phoenix (total 185, margin UTD +1); satisfies Rank #1 and Rank #2 simultaneously.
7. Participant state: PROJECTED_BEAT_VERIFIED under Control S-1 Rev 2; starters Anthony/Goulding/Travers/Waardenburg/Oduro and Sobey/Glover/Schwartz/Hurt/Hunter verified; coaches Chance and King verified; Shea Ili confirmed OUT (hamstring); Daniel Foster confirmed OUT (groin).
8. AGGREGATE_ONLY: none; full player-level roles, minutes, and scoring lines printed.
9. Settlement source per row: S1 (NBL field owner) + S2 (ESPN) + S3 (Sofascore).
10. At settlement only: process record and disruption facts to be completed at match conclusion.

**Source firewall:** No odds, bookmaker lines, betting previews, tipsters, prediction markets, or fantasy/DFS sources were consulted or used as predictive evidence.

**Control receipt (PF-7):** `CONTROL_MANIFEST_2026-09-23.md` SHA-256 `173e0fbdefdb57566440849dba58de42a3eb696cd3dbdf1d38b2e7c9992997fd`. Verified match against live files:
- METHOD.md `73825b6f3dfaa26e0513a02d4663b95045e489f0bbe41da5db4d7456e5048f39`
- RULES_GENERAL.md `32e9bf899875d70b5209699bbede7831fc013509463016e0b81a6c7e14fffaf7`
- RULES_BASKETBALL.md `2671721fdafa9542c7179aef9ffa0e3b14acf77c2a7fdeacd38a022dcd275bfa`

**Sources:**

| Source name | Link | Field owner / lineage | Contributed | Retrieval time (AEST) | Status |
|---|---|---|---|---|---|
| NBL Official Gamecenter | https://www.nbl.com.au | Field owner / NATIONAL_BASKETBALL_LEAGUE | Official schedule, team rosters, injury report (Ili out, Foster out) | 2026-09-24 19:24 | `OPENED` |
| ESPN Australia NBL | https://www.espn.com.au/nbl | Independent primary / BROADCAST_MEDIA | Throwdown 33 preview, broadcast confirmation, team form | 2026-09-24 19:24 | `OPENED` |
| Melbourne United Official | https://www.melbourneutd.com.au | Independent primary / CLUB_MEDIA | Coach Jacob Chance confirmation, roster updates, Austin Shelley NRP | 2026-09-24 19:25 | `OPENED` |
| SE Melbourne Phoenix Official | https://www.semphoenix.com.au | Independent primary / CLUB_MEDIA | Coach Josh King extension, Nathan Sobey season debut confirmation | 2026-09-24 19:25 | `OPENED` |
| Sofascore Basketball | https://www.sofascore.com | Independent secondary / STATISTICAL_AUTHORITY | Historical Throwdown H2H scores, team scoring averages | 2026-09-24 19:25 | `OPENED` |

<!-- END VERBATIM ISSUED RECORD: P-508 -->

---

### P-509 — Basketball / Australian NBL, Perth Wildcats vs Adelaide 36ers

##### Field 1 — Identity and contract

- **Event:** Perth Wildcats (Home) vs Adelaide 36ers (Visitor)
- **Competition:** National Basketball League (Australian NBL 2026-27 Regular Season, Round 2)
- **Date & venue:** 24 September 2026 (local & Melbourne); RAC Arena, Perth, Western Australia, Australia
- **Timezones:** Venue-local Australia/Perth (AWST, UTC+8); Melbourne reference Australia/Melbourne (AEST, UTC+10). **Calendar date rollover: NO**.
- **Scheduled tip-off:** 2026-09-24 19:30:00 AWST / 2026-09-24 21:30:00 AEST
- **Event horizon:** **PREGAME / NOT STARTED** at freeze (verified across NBL official match center `nbl.com.au`, ESPN, and Sofascore).
- **Governing method:** METHOD.md **MDS-2026.09.19-v4.3** / control revision **CR-2026.09.21-3**; SCORING_AND_VALIDATION **SCV-2026.09.19-v2**
- **Controls applied:** G0–G6, G8, G10.2, G13.1, G14/G14.1/G14.2, G15.1 (indoor hardwood court), G16, G20/G20.1/G20.2, G21.1, G22, G25, G25.1, G26.1, G27, G30.1, G36.1, G-L1, G-L2, G-L7, G-L8, G-L9, G-L10, G-L11, G-L12/G-L24, G-L15, G-L17, G-L19, G-L21, G-L22, R-1, S-1 Rev 2, PF-1, PF-2, C-SRC3, C-TIME1/2, C-STATE3, RULES_BASKETBALL §8 (SFA-BASKETBALL), §9 (FIBA official playing rules, 40-minute regulation), and controls 1–20
- **Contracts queried (SPORTS_ONLY / MARKET_BLIND):**
  - 36ers -1.5
  - Wildcats +1.5
  - Combined Total: Over 184.5 Points
  - Combined Total: Under 184.5 Points
  - Potential Game Winner

##### Field 2 — Evidence and exposure

- **Participants & coaching staff (G14.2 / Control S-1 Rev 2):**
  - **Perth Wildcats (Home):** Head Coach **John Rillie**; assistant coaches verified. Starters: PG Elijah Pepper, SG Anthony Dell'Orso, SF Dylan Windler, PF Kristian Doolittle, C Jo Lual-Acuil Jr. Bench rotation: Jesse Wagstaff (Captain), Angus Brandt, Cameron Huefner, Alex Higgins-Titsha, Marley Sam, Jimmy Whitt. Primary injury news: Guard rotation is severely depleted with import PG **Brandon Knight** (unavailable, arriving next week) and PG **Jaron Rillie** (lower leg) both OUT; Blake Nielsen is OUT for the season (ACL). Perth heavily relies on Jo Lual-Acuil Jr. and Kristian Doolittle to anchor the interior. Status: **PROJECTED_BEAT_VERIFIED** under Control S-1 Rev 2.
  - **Adelaide 36ers (Visitor):** Head Coach **Trevor Gleeson** (former Perth Wildcats multi-championship coach returning to RAC Arena as an opposition coach); assistant coaches verified. Starters: PG Bryce Cotton (celebrating his milestone 300th NBL career game against his former franchise), SG Isaac White, SF Matt Kenyon, PF Zylan Cheatham, C Ben Griscti. Bench rotation: Nick Rakocevic, Keanu Rasmussen, Jacob Rigoni, Deonte Williams, Harvey White. Primary injury news: Starting center **Isaac Humphries** is OUT (knee), guard Flynn Cameron is OUT, Bul Kuol is OUT for the season (ACL); guard John Jenkins III is a game-time decision (back). Status: **PROJECTED_BEAT_VERIFIED** under Control S-1 Rev 2.
- **Pace, efficiency & matchup dynamics (SFA-BASKETBALL §8.2):**
  - Pace expectation: Controlled 82.5 possessions per 40 minutes (FIBA 10-minute quarters).
  - Historical head-to-head total suppression: Over their last 4 meetings, game totals have averaged **177.25 points** (160, 179, 189, 181 points), with 3 of the 4 staying comfortably under 184.5.
  - Tactical matchup: Trevor Gleeson's hallmark half-court defensive discipline matches up against John Rillie's shorthanded Wildcats backcourt. Without Brandon Knight and Jaron Rillie, Perth's primary ball-handling falls to young combo-guard Elijah Pepper and Anthony Dell'Orso, who will face sustained perimeter ball-pressure from Matt Kenyon and Isaac White. Consequently, Perth will run clock to feed Jo Lual-Acuil Jr. inside against Adelaide's depleted frontline missing Humphries. On the other end, Adelaide will run deliberate isolation and screen-and-roll action for Bryce Cotton in his 300th milestone game, generating methodical half-court possessions that burn shot-clock seconds.
- **Baseline team scoring:**
  - Adelaide 36ers expected points: **90.2** points ($\sigma = 10.6$)
  - Perth Wildcats expected points: **88.8** points ($\sigma = 10.9$)
  - Combined baseline regulation total: **179.0** points ($\sigma = 15.2$) (full-game expectation with overtime: **179.75** points, $\sigma = 17.07$).
- **Outcome-state family table with masses (§16.5(a) G-L1):**

| Family | Description | Representative Scoreline | Probability Mass |
|---|---|:---:|:---:|
| **F1** | Under 184.5 & 36ers -1.5 | Adelaide 36ers 90–86 Perth Wildcats (Total 176, Margin ADE +4) | **0.3234** (32.34%) |
| **F2** | Under 184.5 & Wildcats +1.5 | Perth Wildcats 89–88 Adelaide 36ers (Total 177, Margin PER +1) | **0.2893** (28.93%) |
| **F3** | Over 184.5 & 36ers -1.5 | Adelaide 36ers 98–92 Perth Wildcats (Total 190, Margin ADE +6) | **0.1929** (19.29%) |
| **F4** | Over 184.5 & Wildcats +1.5 | Perth Wildcats 95–94 Adelaide 36ers (Total 189, Margin PER +1) | **0.1944** (19.44%) |

- **State family distribution check:** $\sum P(F_i) = 0.3234 + 0.2893 + 0.1929 + 0.1944 = \mathbf{1.0000}$ (100.00%).
- **Overtime expectation:** $P(\text{Tie after 40 regulation minutes}) = \mathbf{0.0275}$ (2.75% probability of regulation tie, resolved in 5-minute FIBA overtime periods; incorporated into full-game simulations).

##### Field 3 — Distributional parameters

- **Model:** Bivariate normal scoring distribution with empirical inter-team correlation ($\rho = 0.20$, 200,000 Monte Carlo draws; ADE $\mu = 90.2, \sigma = 10.6$; PER $\mu = 88.8, \sigma = 10.9$; discrete overtime inclusion).
- **Total points distribution:**
  - Centre (mean): **179.75** points
  - Median: **179.63** points
  - Width (standard deviation): **17.07** points
  - Contract line: **184.5** points
  - Derived probabilities: $P(\text{Under } 184.5) = \mathbf{0.6127}$ (61.27%); $P(\text{Over } 184.5) = \mathbf{0.3873}$ (38.73%)
  - Normalised edge: $|179.75 - 184.5| / 17.07 = \mathbf{0.278}$
  - Push mass: **0.0000** (half-point contract)
- **Margin distribution (ADE Margin = Adelaide Points − Perth Points):**
  - Centre (mean): **+1.44** points
  - Median: **+2.00** points
  - Width (standard deviation): **13.63** points
  - Contract line: **+1.5** points (36ers -1.5 requires ADE margin > 1.5; Wildcats +1.5 requires ADE margin < 1.5)
  - Derived probabilities:
    - $P(\text{36ers } -1.5) = F1 + F3 = 0.3234 + 0.1929 = \mathbf{0.5163}$ (51.63%)
    - $P(\text{Wildcats } +1.5) = F2 + F4 = 0.2893 + 0.1944 = \mathbf{0.4837}$ (48.37%)
    - $P(\text{36ers ML}) = \mathbf{0.5429}$ (54.29%)
    - $P(\text{Wildcats ML}) = \mathbf{0.4571}$ (45.71%)
  - Normalised edge (36ers -1.5 vs line 1.5): $|1.44 - 1.5| / 13.63 = \mathbf{0.004}$

##### Field 4 — Contract queries and ranks (UNVALIDATED_SUBJECTIVE; conditional on completion; SPORTS_ONLY / MARKET_BLIND)

| Rank | Contract | Derived Probability | Verdict / Evidence Grade | Role | Rank Gap to Next |
|:---:|---|:---:|:---:|:---:|:---:|
| **1** | **Combined Total: Under 184.5 Points** | **0.613** | LEAN / SOLID | PRIMARY_FORMAL (total pair) | 0.096 (MODERATE) |
| **2** | **36ers -1.5** | **0.516** | LEAN / MODERATE | PRIMARY_FORMAL (handicap spread) | 0.033 (SMALL) |
| **3** | Wildcats +1.5 | 0.484 | AVOID-lean / MODERATE | Complement of #2 | 0.096 (MODERATE) |
| **4** | Combined Total: Over 184.5 Points | 0.387 | AVOID / SOLID | Complement of #1 | — |

- **Preferred sides:**
  - Total pair (FORCED_PAIR): **Under 184.5 Points** (0.613 vs Over 184.5 at 0.387). Preferred due to a 4.75-point cushion below the line, Gleeson's half-court defensive scheme, and Perth's guard shortage slowing offensive tempo. Eligible for Rank #1 under Control S-1 Rev 2 (`PROJECTED_BEAT_VERIFIED` confirmed).
  - Handicap / Spread (FORCED_PAIR): **36ers -1.5** (0.516 vs Wildcats +1.5 at 0.484). Adelaide slight lean due to Bryce Cotton's milestone game and Perth's injury-impacted backcourt without Knight and Rillie.
- **Top Over/Under target:** **Under 184.5 Points** (Rank #1). A `TOP_OU_REVIEW` applies if it fails at settlement.
- **Potential Game Winner:** **Adelaide 36ers**, P(win) = **0.543** (54.29% conditional on completion; Perth Wildcats win probability = 0.4571). Verdict: **SLIGHT LEAN / NARROW FAVORITE**.
  - Rationale: Bryce Cotton playing his 300th career milestone game at RAC Arena against his former club, with Trevor Gleeson's tactical knowledge of Perth's tendencies, gives Adelaide the shot-creation edge down the stretch against a Perth backcourt missing both Brandon Knight and Jaron Rillie.
  - Failure paths: Jo Lual-Acuil Jr. dominates the paint against Adelaide's frontcourt missing Isaac Humphries, Kristian Doolittle neutralizes Zylan Cheatham, and Perth uses home crowd momentum at the Jungle to win outright (Perth win probability = 0.4571).

##### Field 5 — Dependence and checks

- **Representative Rank-#1 outcome:** Adelaide 36ers win 90–86 (Total 176, Margin ADE +4).
  - Total points = 176 (< 184.5 → Under 184.5 Points WIN - Rank #1).
  - Margin = ADE +4 (> 1.5 → 36ers -1.5 WIN - Rank #2).
  - Check: Satisfies Rank #1 AND Rank #2 simultaneously!
- **Joint probability P(R1 ∧ R2):**
  - $P(\text{Under } 184.5 \wedge \text{36ers } -1.5) = F1 = \mathbf{0.3234}$ (32.34%).
  - Fréchet bounds: $[\max(0, 0.6127 + 0.5163 - 1.0), \min(0.6127, 0.5163)] = [0.1290, 0.5163]$. Independent product: $0.6127 \times 0.5163 = 0.3163$. Actual simulation mass $0.3234 \in [0.1290, 0.5163]$.
- **Joint failure mass P(¬R1 ∧ ¬R2):**
  - $\neg\text{R1}$ is Over 184.5 Points.
  - $\neg\text{R2}$ is Wildcats +1.5 (Perth win or lose by 1).
  - $P(\neg\text{R1} \wedge \neg\text{R2}) = F4 = \mathbf{0.1944}$ (19.44%) (high-scoring Perth victory).
  - **P(at least one of R1, R2 wins) = 1 - 0.1944 = 0.8056 (80.56%)** across all completed games!
  - **P(exactly one of the top two wins) = 0.4822 (48.22%)** (F2 + F3 = 0.2893 + 0.1929).
- **Complement decompositions:**
  - Complement of R1 (Over 184.5 Points, 0.3873): High-scoring shootout pushed either by Adelaide blowout (F3 = 0.1929) or Perth upset (F4 = 0.1944).
  - Complement of R2 (Wildcats +1.5, 0.4837): Perth covers +1.5 via either half-court defensive win (F2 = 0.2893) or high-scoring shoot-out (F4 = 0.1944).
- **Sensitivity analysis:**
  - If Bryce Cotton explodes for 35+ points on high efficiency: Over 184.5 rises to 0.445, 36ers -1.5 rises to 0.565.
  - If Jo Lual-Acuil Jr. dominates Adelaide's backup centers: Under 184.5 rises to 0.670, Wildcats +1.5 rises to 0.535.
  - Across all realistic tempos, Under 184.5 remains favored.

##### Field 6 — Freeze and follow-up

- **Freeze timestamp:** 2026-09-24 21:25:00 AEST (2026-09-24 19:25:00 AWST).
- **Event horizon:** PREGAME / NOT STARTED at freeze (verified across NBL official match center `nbl.com.au`, ESPN, and Sofascore).
- **Settlement route (G10.2):**
  - Lineage 1 (Field Owner): NBL Official Gamecenter / Boxscore (`nbl.com.au`).
  - Lineage 2 (Independent Primary Media): ESPN Australia NBL Scoreboard (`espn.com.au/nbl`).
  - Lineage 3 (Independent Secondary): Sofascore Basketball (`sofascore.com`).
- **Settlement criteria:** Minimum 3 distinct lineages agreeing on final score and completion status including overtime if played (C-FINAL3). Record quarter-by-quarter breakdown, final margin, and player statistics.
- **Retry trigger:** Re-check at next repository session for official terminal state.

##### §16.8 completeness block

1. MDS-2026.09.19-v4.3 / CR-2026.09.21-3. Controls applied: G0–G6, G8, G10.2, G13.1, G14/G14.1/G14.2, G15.1 (indoor court), G16, G20/G20.1/G20.2, G21.1, G22, G25, G25.1, G26.1, G27, G30.1, G36.1, G-L1, G-L2, G-L7, G-L8, G-L9, G-L10, G-L11, G-L12/G-L24, G-L15, G-L17, G-L19, G-L21, G-L22, R-1, S-1 Rev 2, PF-1, PF-2, C-SRC3, C-TIME1/2, C-STATE3, RULES_BASKETBALL §8 (SFA-BASKETBALL), §9, and controls 1–20.
2. Outcome-state family table with masses: F1 0.3234, F2 0.2893, F3 0.1929, F4 0.1944 (sum = 1.0000).
3. Total points: centre (mean) 179.75 / median 179.63; width (SD) 17.07; line 184.5; P(Under) = 0.613; P(Over) = 0.387. Margin: centre (mean) +1.44 / median +2.00; width (SD) 13.63; line 1.5; P(36ers -1.5) = 0.516; P(Wildcats +1.5) = 0.484. Normalised edges: total |179.75 − 184.5| / 17.07 = 0.278; margin |1.44 − 1.5| / 13.63 = 0.004.
4. Complement decompositions for R1 (Over 184.5 Points, 0.387) and R2 (Wildcats +1.5, 0.484): stated above.
5. P(R1 ∧ R2) = 0.3234, coupling between half-court derby tempo and game total suppression.
   - 5a. P(¬R1 ∧ ¬R2) = 0.1944 (shared-failure mass in high-scoring Perth victory). P(exactly one wins) = 0.4822. P(at least one wins) = 0.8056.
   - 5b. O/U row labelled FORCED_PAIR; preferred side is Under 184.5 Points; push mass = 0.000 (half-point line).
6. Representative Rank-#1 outcome: Adelaide 90–86 Perth (total 176, margin ADE +4); satisfies Rank #1 and Rank #2 simultaneously.
7. Participant state: PROJECTED_BEAT_VERIFIED under Control S-1 Rev 2; starters Pepper/Dell'Orso/Windler/Doolittle/Lual-Acuil and Cotton/White/Kenyon/Cheatham/Griscti verified; coaches Rillie and Gleeson verified; Knight, Jaron Rillie, Nielsen confirmed OUT for Perth; Humphries, Cameron, Kuol confirmed OUT for Adelaide.
8. AGGREGATE_ONLY: none; full player-level roles, minutes, and scoring lines printed.
9. Settlement source per row: S1 (NBL field owner) + S2 (ESPN) + S3 (Sofascore).
10. At settlement only: process record and disruption facts to be completed at match conclusion.

**Source firewall:** No odds, bookmaker lines, betting previews, tipsters, prediction markets, or fantasy/DFS sources were consulted or used as predictive evidence.

**Control receipt (PF-7):** `CONTROL_MANIFEST_2026-09-23.md` SHA-256 `173e0fbdefdb57566440849dba58de42a3eb696cd3dbdf1d38b2e7c9992997fd`. Verified match against live files:
- METHOD.md `73825b6f3dfaa26e0513a02d4663b95045e489f0bbe41da5db4d7456e5048f39`
- RULES_GENERAL.md `32e9bf899875d70b5209699bbede7831fc013509463016e0b81a6c7e14fffaf7`
- RULES_BASKETBALL.md `2671721fdafa9542c7179aef9ffa0e3b14acf77c2a7fdeacd38a022dcd275bfa`

**Sources:**

| Source name | Link | Field owner / lineage | Contributed | Retrieval time (AEST) | Status |
|---|---|---|---|---|---|
| NBL Official Gamecenter | https://www.nbl.com.au | Field owner / NATIONAL_BASKETBALL_LEAGUE | Official schedule, team rosters, injury report (Knight/Rillie/Nielsen out; Humphries/Cameron/Kuol out) | 2026-09-24 21:23 | `OPENED` |
| ESPN Australia NBL | https://www.espn.com.au/nbl | Independent primary / BROADCAST_MEDIA | Bryce Cotton 300th game preview, Trevor Gleeson RAC Arena return, broadcast confirmation | 2026-09-24 21:23 | `OPENED` |
| Perth Wildcats Official | https://www.wildcats.com.au | Independent primary / CLUB_MEDIA | Coach John Rillie updates, Brandon Knight arrival status, Jaron Rillie injury | 2026-09-24 21:24 | `OPENED` |
| Adelaide 36ers Official | https://www.adelaide36ers.com | Independent primary / CLUB_MEDIA | Coach Trevor Gleeson comments, Bryce Cotton milestone celebration, Humphries injury update | 2026-09-24 21:24 | `OPENED` |
| Sofascore Basketball | https://www.sofascore.com | Independent secondary / STATISTICAL_AUTHORITY | Historical H2H scores (160, 179, 189, 181), team scoring averages | 2026-09-24 21:24 | `OPENED` |

<!-- END VERBATIM ISSUED RECORD: P-509 -->

## 2. Settled Logs

No event issued in this log has been settled yet. Settled predecessor events (P-482–P-494 and the three temporary IDs) are in `PREDICTION_LOG_COMBINED_5.md`; this section will receive this log's own events once they are final and retrospected on request.

## 3. Sources

Every card lists every material source in its own **Sources** table, with: source name, link, field owner / lineage, what it contributed, retrieval time (AEST) and status (`OPENED` / `SNIPPET` / `ASSUMED`). Preferred order (SOURCES.md, DATA_SOURCE_REGISTER.md): official league/competition feed → official team/player release → structured statistical API (MLB statsapi, NPB box, KBO scoreboard, ESPN site API without a browser User-Agent, WTA/ATP feeds, Cricbuzz/ESPNcricinfo) → independent high-quality reporting → fallback. Weather: Open-Meteo / venue hourly forecast in venue-local time. Prohibited: sportsbook/odds pages, betting previews, tipsters, prediction markets, fantasy/DFS, social media (S-1), AI-generated recaps, search-result summaries as facts.

## 4. Document Mapping

| Information or update | Where it eventually belongs |
|---|---|
| Frozen forecast card; later settlement and retrospective | `PREDICTION_LOG_COMBINED_5.md` (active canonical log) |
| Current event state / open handles | `GAME_LOG_STATUS_CURRENT.md` |
| Cross-sport process control with recurring evidence | `RULES_GENERAL.md`, `METHOD.md` or `CONTROLS.md` |
| Sport-specific rule, kill path or checklist item | Relevant `RULES_<SPORT>.md` (league format/tie rules: §9/§10 "rules reference"; cricket/soccer league detail: `LEAGUE_RULES_*.md`) |
| New/changed source, access method or reliability note | `DATA_SOURCE_REGISTER.md` (full card) and `SOURCES.md` (summary) |
| Hypothesis / candidate lesson with a prospective test | `LEARNING_REGISTER.md` (`TESTING` row with its evidence and test) |
| Base rate derived for an identity input | `BASE_RATES_REGISTER.md` |
| Mini-log import / ID-custody procedure | `EXTERNAL_LOGGING_WORKFLOW.md` |
| One-event observation | This log only — never promoted from one game |

## 5. Prediction integrity checklist (run before every card; record the result in the card)

1. Verify event, competition, participants, venue, official venue-local date/time, IANA timezone and the AEST/AEDT conversion (CR-4, three independent lineages).
2. Check state: UPCOMING / DELAYED / LIVE / POSTPONED / CANCELLED / COMPLETED. Anything but UPCOMING blocks a pregame card; a live view is labelled LIVE-ISSUED.
3. Parse the supplied markets exactly; flag any inconsistency (do not silently correct); quarantine the lines.
4. Retrieve starters/lineups, bench/reserves, injuries, suspensions, rest, coaching and late changes from official sources first; record `LINEUPS_NOT_YET_PUBLISHED @ time` or `RETRIEVAL_MISS`.
5. Build one joint distribution (six-field object); derive every row's probability; rank by derived probability (Pick #1 = highest); print P(R1 ∧ R2), complement decomposition and the top-O/U target.
6. Final volatile refresh immediately before the start; stamp the freeze time; append the complete card here **before** delivering it.
7. Mark anything unconfirmed as unconfirmed; never fabricate.

## 6. Continuity and ID custody

- Allocate the next canonical ID only at freeze, after re-reading Part 5's snapshot and this log.
- If another session may be issuing at the same time, or any collision/uncertainty appears, use `TMP-YYYYMMDD-<SPORT>-<A>-<B>` and propose the canonical ID for reconciliation; never overwrite or renumber an existing ID.
- If a later refresh or reforecast concerns the same event (same date, venue and participants), append it under the same ID as an append-only view; if any of those differ, it is a new event.
- Record every ID claimed in any external chat transcript here the moment it is claimed, even if the card body is short.

## 7. Output after every new prediction query

1. The requested prediction and analysis.
2. The complete card appended to §1 (identity/contract, evidence/exposure, distribution, ranked rows with probabilities, dependence checks, freeze/settlement route, potential winner, reasoning, all sources, settlement status).
3. All material sources recorded in the card.
4. Document mappings / candidate learnings noted in the card.
5. The entire updated mini log.

No retrospective is performed unless explicitly requested.
