## Current queue / canonical rollover — reconciled 2026-09-23

Part 4 is **CLOSED at P-481**. Part 5 (PREDICTION_LOG_COMBINED_5.md) is active and reconciled through **P-493**; next canonical ID is **P-494**. Three Part-5 cards remain open (P-489, P-491, P-493). The NBL P-487 source claim is held noncanonically pending issue-time evidence; P-490 is a retired unused provisional alias. No result-state refresh or retrospective was performed in the 2026-09-23 ID reconciliation. Performance status remains **LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE**.

## Current queue correction — 2026-09-17(c)

Historical 2026-09-17 snapshot (superseded by the 2026-09-21 rollover above): Part 4 was the queue authority at P-452; the historical open-handle counts remain evidence, not the current next-ID state. TMP-AUDIT-20260912-03 and -04 are reopened for P-255-C05/P-256-C05 as UNRESOLVED_PERIOD. The two older bounded WIN labels and handle retirements are superseded. No historical forecast was changed. [Correction and receipts](PREDICTION_LOG_COMBINED_4.md).

# Current complete game-log register — updated 2026-09-23

**LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE.** The ID register spans 493 numbered slots (P-001–P-493), including reserved/unused P-372, P-487 and P-490; this is not a prediction count. Next canonical ID: **P-494**, controlled by PREDICTION_LOG_COMBINED_5.md.

**2026-09-17 update:** `P-424`–`P-437` imported from an external mini log, settled and audited ([Part 4 §"2026-09-17"](PREDICTION_LOG_COMBINED_4.md)). **12 cards scored** (52 graded rows, 36 W / 16 L, mean Brier 0.1892 — every row independently recomputed), **2 administratively closed** (`P-424`, `P-428`: correct start-crossing fail-closes, no forecast issued). Rank #1 10 W / 2 L; at least one of the top two won on 11 of 12; both won on 8 of 12. One row open: `P-430-C05` (`TMP-OPEN-20260917-01`). All five ACLE finals and both ETPL scorecards were independently verified at ESPN; the four KBO finals could not be (lane degraded). Canonical IDs now `P-001`–`P-437`; **next ID `P-438`**. New cross-sport rules `G-L17`–`G-L20` (`RULES_GENERAL.md` §16.12).

**2026-09-16 update:** No new card was issued (next ID still **P-424**; no event is live). **P-406 is now FINAL / SETTLED:** its six-over rows settled at the ESPN cricket API matchnote `Powerplay 1: Overs 0.1 - 6.0 (Mandatory - 68 runs, 2 wickets)` for the Edinburgh innings — C01 Over 50.5 WIN, C04 Under 50.5 LOSS; `TMP-OPEN-20260914-06` retired. **P-418 re-classified** from identity conflict to `RESULT_NOT_RECOVERED`: the "2026-09-15" BBS report cited earlier is dated 2026-07-17, and RSSSF lists Round 15 "[Sep 14] Drukpa – RTC" (unscored; page updated 11 Sep). A later external settlement variant of log C (`…P407_P423_FULL_RETROSPECTIVE_2026-09-15.md`, SHA-256 `f0c77cf8…`) was found in Downloads and reconciled; its conflicting handle numbers are recorded as retired aliases below. **Primary queue: 22 handles** (Part 3 custody 13 — the 2026-09-15(c) figure "13" should have read 14 — plus Part 2's 9). **Documentary audits: 5 → 3.** Four of the five parked corner rows were re-probed successfully (P-251, P-255, P-256, P-265); P-255 and P-256 settled at the UEFA field owner with a period-scope bound and their handles retired. Full records: [Part 4 Appendix A](PREDICTION_LOG_COMBINED_4.md). Evidence: [combined log 3 §"2026-09-16"](PREDICTION_LOG_COMBINED_3.md).

**2026-09-15 update:** P-364 is FINAL (England won by 8 wickets, 12 Sep; ESPNcricinfo full scorecard via r.jina.ai, corroborated by Wikipedia) and its winner label is settled — `TMP-OPEN-20260911-03` retired. **No live event remains.** The primary queue is now **13**: one identity conflict and twelve corner fields. No new mini log was supplied or found on 2026-09-15 (local tree and Google Drive searched), so no new canonical or temporary IDs were created. [combined log §"2026-09-15"](PREDICTION_LOG_COMBINED_3.md).

*(Historical, 2026-09-12:)* The fourteen result/derivative follow-ups include one live event (P-364), one identity conflict and twelve other corner fields. Five additional historical documentary-audit tasks were exposed during mini-log recovery. Four operator-only exceptions remain research settled. Historical grades are carried unless the dated evidence explicitly says they were independently rechecked; a final label alone does not mean every original input or retrospective source was revalidated.

[Detailed current audit](COMPREHENSIVE_SETTLEMENT_AUDIT_2026-09-12.md) | [Recent queue evidence](audit_2026-09-12/recent_queue_evidence.md) | [Historical queue evidence](audit_2026-09-12/historical_queue_evidence.md) | [Recovered historical tables and retrospectives](audit_2026-09-12/recovered_historical_retrospectives.md)

## Historical canonical-record category snapshot — superseded for totals by the 2026-09-21 rollover

| Category | Records |
|---|---:|
| SETTLED | 383 |
| TERMINAL FIELD GAP | 1 |
| ADMINISTRATIVE / NO SCORED TRIAL | 19 |
| OPEN RESULT OR FIELD | 22 |
| RESEARCH SETTLED | 4 |
| INHERITED CLOSED / AUDIT GAP | 5 |
| ALIAS | 1 |
| CENSORED TARGETS | 1 |
| RESERVED / UNUSED | 1 |
| Total | 437 |

This category table was computed before the P-452–P-481 rollover and is retained as historical evidence; use the 2026-09-21 header for the current total of 481 canonical IDs. Counts describe record custody, not performance, independent events or the number of contracts. OPEN RESULT OR FIELD includes the 14 primary follow-ups. INHERITED CLOSED / AUDIT GAP preserves prior closure while explicitly qualifying evidence completeness.

## Every canonical record from the first

| ID | Event | Current status | Evidence / remaining requirement |
|---|---|---|---|
| P-001 | Welsh Fire Women v Trent Rockets Women, The Hundred Women's 11th Match (carried over from legacy V6-022) | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-002 | Philadelphia Phillies @ Miami Marlins (MLB regular season) | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-003 | FC København v Polissya Zhytomyr (UEFA Conference League, Q2, 2nd leg) | FINAL / CLOSED; old corner terminal unsettleable | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-004 | MI London (Men) v London Spirit (Men), The Hundred Men's Competition 2026 | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-005 | Texas Rangers @ Tampa Bay Rays (MLB regular season) | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-006 | Southern Brave (Men) v Birmingham Phoenix (Men), The Hundred Men's Competition 2026 | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-007 | Manchester Super Giants (Men) v Trent Rockets (Men), The Hundred Men's Competition 2026 | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-008 | New York Yankees @ Chicago Cubs, MLB regular season | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-009 | Indiana Fever @ Portland Fire, WNBA regular season — FORECAST | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-010 | Carlton v Brisbane Lions, AFL Round 21 — FORECAST (locked 2026-08-01T08:56:26Z / 18:56:26 AEST) | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-011 | Arizona Diamondbacks @ Cleveland Guardians — PREGAME CARD | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-012 | Welsh Fire Women v Southern Brave Women, The Hundred Women's Competition 2026, Match 19 | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-013 | Welsh Fire Men v Southern Brave Men, The Hundred Men's Competition 2026, Match 19 | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-014 | San Diego Padres (Michael King) at Arizona Diamondbacks (Brandon Pfaadt) | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-015 | Sri Lanka Women vs Pakistan Women, 3rd T20I | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-016 | Kiwoom Heroes at Lotte Giants, KBO regular season | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-017 | Sunrisers Leeds Women v London Spirit Women, The Hundred 2026 | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-018 | Sunrisers Leeds Men vs London Spirit Men, The Hundred 2026 Match 20 (2026-08-04) | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-019 | Manchester Super Giants Women v Welsh Fire Women, The Hundred Women's Competition 2026, Match 21 | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-020 | Trent Rockets Women v Birmingham Phoenix Women, The Hundred Women's Competition 2026, Match 22 | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-021 | Los Angeles Angels (Reid Detmers) at Baltimore Orioles (Trevor Rogers), MLB | ADMINISTRATIVE / NO SCORED TRIAL | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-022 | Los Angeles Angels (Ryan Johnson) at Baltimore Orioles (Brandon Young), MLB | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-023 | Benfica v Heart of Midlothian, UEFA Europa League qualifying | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-024 | Toronto Tempo @ Portland Fire, WNBA regular season - LIVE FORECAST (appended 2026-08-07 AEST) | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-025 | Brisbane Lions v Hawthorn, AFL Round 22 - LIVE FORECAST (appended 2026-08-07 AEST) | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-026 | Birmingham Phoenix Women v Sunrisers Leeds Women, The Hundred 2026 - START-CROSSED/PRE-DELIVERY FORECAST (appended 2026-08-08 AEST) | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-027 | Melbourne v Fremantle, AFL Round 22 - LIVE FORECAST (appended 2026-08-08 AEST) | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-028 | West Coast v Collingwood, AFL Round 22 - LIVE FORECAST (appended 2026-08-09 AEST) | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-029 | St Kilda v Carlton, AFL Round 22 - PREGAME FORECAST (appended 2026-08-09 AEST) | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-030 | Sunrisers Leeds Women v Welsh Fire Women, The Hundred 2026 Match 27 - PREGAME FORECAST (appended 2026-08-09 AEST) | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-031 | Manchester City v Atletico Madrid, 2026 Coupang Play Series - LIVE FORECAST (appended 2026-08-09 AEST) | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-032 | London Spirit Women v Birmingham Phoenix Women, The Hundred 2026 Match 28 - START-CROSSED/PRE-DELIVERY FORECAST (appended 2026-08-09 AEST) | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-033 | Cincinnati Reds at Washington Nationals - PREGAME FORECAST (appended 2026-08-10 AEST) | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-034 | Baltimore Orioles at Minnesota Twins - PREGAME FORECAST (appended 2026-08-11 AEST) | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-035 | Atlanta Dream @ Connecticut Sun, WNBA regular season - LIVE FORECAST | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-036 | Philadelphia Phillies at Minnesota Twins — MLB Field of Dreams | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-037 | Jamaica Kingsmen vs Guyana Amazon Warriors — CPL | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-038 | Australia vs Bangladesh — 1st Test | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-039 | Manly-Warringah Sea Eagles vs Dolphins — NRL | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-040 | Fremantle vs Adelaide Crows — AFL | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-041 | Wolverhampton Wanderers v Blackburn Rovers, EFL Championship Round 1 — PREGAME FORECAST (appended 2026-08-15T02:07:19+10:00) | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-042 | Manchester Super Giants Men v Sunrisers Leeds Men, The Hundred Eliminator — LIVE FORECAST (appended 2026-08-15T03:01:20+10:00) | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-043 | St. Louis Cardinals at Chicago Cubs, MLB — PREGAME FORECAST (appended 2026-08-15T04:16:53+10:00) | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-044 | Richmond v Collingwood, AFLW — PREGAME FORECAST (appended 2026-08-15T16:58:00+10:00) | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-045 | Hawthorn v Collingwood, AFL — PREGAME FORECAST (appended 2026-08-15T19:35:00+10:00) | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-046 | Chelsea v Real Sociedad, soccer — PREGAME FORECAST (appended 2026-08-15T22:49:00+10:00) | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-047 | Bayern Munich v RB Leipzig, soccer — PREGAME FORECAST (appended 2026-08-15T22:59:00+10:00) | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-048 | Essendon v Sydney Swans, AFL Round 23 — ZERO-SCORE LIVE-START FORECAST | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-049 | Doosan Bears at KIA Tigers, KBO regular season — PREGAME FORECAST | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-050 | Trent Rockets Women v Sunrisers Leeds Women, The Hundred 2026 Final — LIVE ORIGINAL-LINE ASSESSMENT | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-051 | FC Basel v FC Barcelona, senior men's club friendly — PREGAME FORECAST | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-052 | Athletics at Kansas City Royals, MLB regular season — PREGAME FORECAST | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-053 | Yomiuri Giants at Yokohama DeNA BayStars, NPB Central League — PREGAME FORECAST | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-054 | Kiwoom Heroes at Lotte Giants, KBO — PREGAME FORECAST | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-055 | Detroit Tigers at Pittsburgh Pirates, MLB — PREGAME FORECAST | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-056 | Arizona Diamondbacks at Boston Red Sox, MLB — PREGAME FORECAST | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-057 | Minnesota Lynx @ Golden State Valkyries, WNBA — LATE ADMINISTRATIVE IMPORT OF ISSUED CHAT FORECAST | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-058 | St Kilda v Gold Coast SUNS, AFL Round 24 — ZERO-SCORE WARMUP / ORIGINAL-LINE FORECAST | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-059 | St. Louis Cardinals (Michael McGreevy) at Cincinnati Reds (Brady Singer), MLB — ZERO-SCORE WARMUP / ORIGINAL-LINE FORECAST | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-060 | New York Yankees (Gerrit Cole) at Baltimore Orioles (Kyle Bradish), MLB — INCLEMENT-WEATHER START DELAY / ORIGINAL-LINE FORECAST | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-061 | Hokkaido Nippon-Ham Fighters at Chiba Lotte Marines | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-062 | West Coast Eagles v Hawthorn (late import) | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-063 | Newcastle United v Liverpool (late import) | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-064 | Texas Rangers (Kumar Rocker) at Chicago White Sox (José Urquidy), MLB — PRE-FIRST-PITCH FORECAST | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-065 | Golden State Valkyries at Minnesota Lynx, WNBA regular season — PRE-TIP FORECAST | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-066 | Atlanta Dream at Los Angeles Sparks, WNBA regular season — PRE-TIP FORECAST | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-067 | Doosan Bears at KT Wiz, KBO regular season — PRE-FIRST-PITCH FORECAST | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-068 | Hanwha Eagles at SSG Landers, KBO regular season — PRE-FIRST-PITCH FORECAST | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-069 | Lotte Giants at KIA Tigers, KBO regular season — PRE-FIRST-PITCH FORECAST | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-070 | Central Ballester Reserves vs El Porvenir Reserves — START PASSED / LIVE STATE NOT VERIFIED | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-071 | Alejandro Juan Mano vs Alejandro Turriziani Alvarez, ITF M25 Oviedo — DELAYED / NOT STARTED FORECAST | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-072 | Jelle Sels vs Stijn Paardekooper — DELAYED / NOT STARTED FORECAST | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-073 | Tobol Kostanay vs Kaisar Kyzylorda — PREGAME FORECAST | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-074 | Maccabi Herzliya U19 vs Hapoel Rishon LeZion U19 — PREGAME FORECAST | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-075 | OKS vs Middelfart — PREGAME FORECAST | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-076 | FK Horní Ředice vs FK Dukla Praha — PREGAME FORECAST | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-077 | Vincent Weaver vs Aryan Jit Singh — PREGAME FORECAST | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-078 | SK Brann (W) vs FK Austria Wien (W) — PREGAME FORECAST | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-079 | Abha vs Al Khaleej Saihat — PREGAME | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-080 | Al Taawoun Buraidah vs Al Fayha — PREGAME | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-081 | Independiente del Valle vs Deportes Tolima — PREGAME | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-082 | CF Monterrey vs Chicago Fire FC — PREGAME | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-083 | Cleveland Guardians at Los Angeles Angels, MLB regular season — PREGAME FORECAST | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-084 | Washington Mystics at Phoenix Mercury, WNBA regular season — PREGAME FORECAST | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-085 | Lobos Puebla vs Fuerza Regia, LNBP regular season — LIVE START-CROSSING FORECAST | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-086 | Club León vs Real Salt Lake — Leagues Cup quarterfinal — START PASSED / LIVE STATE NOT VERIFIED | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-087 | India vs Sri Lanka, 2nd Test, Day 4 — PRE-START DAY-4 LIVE-STATE RESEARCH CARD | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-088 | Howlers Sporting Singtam vs Sikkim Boys Football Club — SFA A Division S-League — PREGAME FORECAST | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-089 | Hanshin Tigers @ Chunichi Dragons — PREGAME | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-090 | Hokkaido Nippon-Ham Fighters @ Saitama Seibu Lions — PREGAME | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-091 | Tohoku Rakuten Golden Eagles @ Orix Buffaloes — PREGAME | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-092 | Doosan Bears @ KT Wiz — PREGAME | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-093 | NC Dinos @ LG Twins, KBO regular season — PREGAME FORECAST | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-094 | Yorkshire Women vs Surrey Women, Metro Bank One Day Cup Women — TOSS COMPLETE / PRE-FIRST-BALL FORECAST | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-095 | TSG Hawks @ Fubon Guardians, CPBL regular season — PREGAME FORECAST | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-096 | Rakuten Monkeys @ CTBC Brothers, CPBL regular season — PREGAME FORECAST | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-097 | Wei-Chuan Dragons @ Uni-President 7-ELEVEn Lions, CPBL regular season — PREGAME FORECAST | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-098 | Vietnam vs Thailand, ASEAN Hyundai Cup 2026 Final Leg 2 — PRE-KICKOFF-DATA VIEW | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-099 | Rotterdam Dockers vs Amsterdam Flames, European T20 Premier League 2026 — TOSS COMPLETE / PRE-FIRST-BALL VIEW | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-100 | Apollon Limassol Women vs FH Hafnarfjordur Women, UEFA Women's Europa Cup 2026/27 — PREGAME FORECAST | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-101 | Germany Women vs Türkiye Women, international friendly — PREGAME FORECAST | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-102 | VfL Wolfsburg Women vs Inter Women, UEFA Women's Champions League 2026/27 — PREGAME FORECAST | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-103 | Tampa Bay Rays at Detroit Tigers | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-104 | Ajax Women vs Real Madrid Women — UEFA Women's Champions League third qualifying round, first leg — PREGAME | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-105 | Al Ahli Saudi FC vs Auckland FC — FIFA Intercontinental Cup 2026, African-Asian-Pacific Cup Playoff — PREGAME | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-106 | Newcastle United vs West Bromwich Albion — Carabao Cup Second Round — PREGAME | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-107 | Bradford City vs Burnley — Carabao Cup Round 2 — PREGAME | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-108 | Tottenham Hotspur vs Charlton Athletic — Carabao Cup Round 2 — PREGAME | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-109 | Chicago Cubs @ Arizona Diamondbacks — MLB regular season — PREGAME | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-110 | Kei Nishikori vs Michael Antonius — US Open Men's Qualifying Q2 — DELAYED / NOT STARTED | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-111 | Boston Red Sox @ Miami Marlins — MLB regular season — PREGAME | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-112 | Minnesota Twins @ Athletics — MLB regular season — PREGAME | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-113 | Club América vs Columbus Crew — Leagues Cup 2026 Quarterfinal | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-114 | India vs Sri Lanka, 2nd Test, Day 5 — PRE-DAY-5 LIVE-STATE FORECAST | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-115 | Belfast Wolves vs Dublin Guardians, European T20 Premier League 2026 — START-CROSSED / NOT STARTED | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-116 | Brisbane Broncos vs Melbourne Storm — PREGAME | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-117 | ISI Dangkor Senchey FC vs Life FC Sihanoukville — PREGAME | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-118 | Sandro Kopp vs Martin Krumich — PREGAME | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-119 | Noah Karma vs Alessandro Hunziker — PREGAME | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-120 | Guinea vs South Sudan — PREGAME | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-121 | Sardarapat FC vs FC Syunik — Armenian Cup | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-122 | Bahrain vs Oman — PREGAME | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-123 | BuxDU vs Metallurg Bekabad — SCHEDULE-CONFLICT / NO VERIFIED LIVE SCORE | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-124 | Chase Ferguson vs Fumin Jiang — M15 Maanshan 8 Quarterfinal | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-125 | Canberra Brave vs Sydney Bears — 2026 AIHL Goodall Cup Preliminary Final | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-126 | Sikkim Aakraman FC vs Sikkim Boys Club — SFA A Division S-League | IDENTITY/STATE UNRESOLVED; secondary 3-0 candidate, no authenticated reconciliation | Current time-only/postponed surfaces do not reconcile the older claimed 1–0. Need exact SFA event/reschedule identity, final, half and corner owner.; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-127 | Iran vs New Zealand — FIBA Basketball World Cup 2027 Asian Qualifiers | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-128 | Auckland vs Bay of Plenty — Hilux NPC Round 5 | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-129 | Manly Warringah Sea Eagles vs St George Illawarra Dragons — NRL Round 26 | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-130 | Beitar Haifa Yakov vs Hapoel Bnei Arrara Ara — Israel State Cup 2026/27 | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-131 | Penrith Panthers vs Canterbury-Bankstown Bulldogs — NRL Round 26 | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-132 | RC Vannes Sevens vs LOU Rugby Sevens — In Extenso SuperSevens, Pau | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-133 | Arthur Géa vs Nishesh Basavareddy — US Open 2026 Men's Qualifying Final | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-134 | Cape Verde vs Guinea — FIBA Basketball World Cup 2027 African Qualifiers | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-135 | Unión de Santa Fe vs Sarmiento — Torneo Clausura 2026 | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-136 | James Duckworth vs Arthur Fery — ATP Winston-Salem Open 2026 Semifinal | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-137 | Los Angeles Dodgers (Tarik Skubal) @ Detroit Tigers (Drew Anderson) — MLB | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-138 | Miami Marlins (Eury Pérez) @ Washington Nationals (Jackson Kent) — MLB | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-139 | Falcons @ Dolphins preseason | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-140 | Astros @ Mets | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-141 | Red Sox @ Yankees | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-142 | Rockies @ Braves | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-143 | Giants @ Jets preseason | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-144 | Buccaneers @ Jaguars preseason | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-145 | Rangers @ Brewers | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-146 | Sun @ Fever | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-147 | Gotham v Portland | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-148 | Toluca Femenil v León Femenil | FINAL / PARTIAL; corner field pending | Prior Toluca 2 corners remains provisional; operator/provider ownership missing. Fresh corner fetch failed.; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-149 | Colorado Rapids 2 v Ventura County | FINAL / PARTIAL; corner field pending | Ventura O3.5 remains provisional. Official club narrative has no full corner count.; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-150 | Montreal @ Winnipeg, CFL | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-151 | Boca Juniors v Lanús | FINAL / SETTLED — Boca 1-0 Lanús (90+3'); Boca 11 corners, Lanús 3; Boca Over 4.5 corners WIN | 2026-09-06 audit: corners confirmed from `SRC-ESPN-SITE-API-SOCCER` (`arg.1`/`401841527`), exactly reproducing the previously specialist-only 11–3. No longer provisional; outcome unchanged; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-152 | Atlante v León | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-153 | Necaxa v Cruz Azul | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-154 | Vikings @ Broncos preseason | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-155 | Phillies @ Angels | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-156 | Orioles @ Athletics | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-157 | Sacramento @ Reno | ADMINISTRATIVE / NO SCORED TRIAL | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-158 | Tempo @ Aces | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-159 | Mystics @ Sparks | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-160 | Diamondbacks @ Giants | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-161 | Sultanes @ Toros | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-162 | Te v Ferguson | FINAL / SETTLED — ITF field-owner confirmation recovered | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-163 | Adelaide v West Coast AFLW | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-164 | Lotte @ Nippon-Ham, live | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-165 | Tohoku Rakuten Golden Eagles @ Saitama Seibu Lions — NPB Pacific League | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-166 | Melbourne Mustangs vs Canberra Brave — AIHL Goodall Cup Semifinal | FINAL / RESEARCH SETTLED; operator definition unknown | Canberra 5–4 OT, regulation 4–4. Obtain actual operator/market wording; ordinary game result cannot establish ticket terms.; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-167 | Kiwoom Heroes @ Doosan Bears — KBO | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-168 | LG Twins @ Lotte Giants — KBO | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-169 | Melbourne vs Carlton — AFL Wildcard Final | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-170 | North Queensland Cowboys vs Wests Tigers — NRL | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-171 | Glasgow Cosmic vs Dublin Guardians — European T20 Premier League | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-172 | Liverpool vs Nottingham Forest — English Premier League | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-173 | Chengdu Rongcheng vs Liaoning Tieren (Ironman) — Chinese Super League | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-174 | Henan vs Chongqing Tonglianglong — Chinese Super League | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-175 | South Africa vs Zimbabwe — Namibia T20I Tri-Series | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-176 | Amiens SC vs FC Versailles — France Ligue 3 | FINAL / PARTIAL; corner field pending | Prior complete timeline sums 8; field ownership and operator definition not supplied.; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-177 | SC Aubagne Air Bel vs Bourg-en-Bresse Péronnas — France Ligue 3 | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-178 | AS Cannes vs Le Puy-en-Velay — France Ligue 3 | FINAL / PARTIAL; corner field pending (provisional LOSS at inherited 16) | Cannes 2–0 confirmed. Unverified GioScore 8–8 is not accepted; need trusted complete corner endpoint.; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-179 | Thionville Lusitanos vs Paris 13 Atletico — France Ligue 3 | FINAL / PARTIAL; corner field pending | 8–1 corners reappears on specialist; not a new independent field owner.; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-180 | 1. FC Köln vs TSG Hoffenheim — Germany Bundesliga | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-181 | Coventry City vs Hull City — English Premier League | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-182 | Excelsior Rotterdam vs Sparta Rotterdam — Netherlands Eredivisie | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-183 | Levante UD vs Real Betis — La Liga | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-184 | North Carolina vs TCU — NCAA Football | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-185 | Robert Morris @ Wagner — NCAA FCS / NEC | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-186 | Los Angeles Dodgers @ Detroit Tigers — MLB | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-187 | Trinbago Knight Riders vs Jamaica Kingsmen — Republic Bank CPL 2026 | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-188 | Boston Red Sox @ New York Yankees — MLB | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-189 | Alabama A&M Bulldogs vs Howard Bison — Cricket MEAC/SWAC Challenge | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-190 | New Zealand Warriors (W) vs St George Illawarra Dragons (W) — NRLW Round 9 | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-191 | Walyalup (Fremantle W) vs Carlton W — AFLW Round 3 | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-192 | SSG Landers @ KIA Tigers — KBO | ADMINISTRATIVE / NO SCORED TRIAL | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-193 | Essendon (W) vs Richmond (W) — AFLW Round 3 | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-194 | FC St. Pauli vs 1. FC Kaiserslautern — Germany 2. Bundesliga | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-195 | KAA Gent vs Club Brugge — Belgium First Division A | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-196 | Egypt vs Congo DR — FIBA Basketball World Cup 2027 African Qualifiers | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-197 | Feyenoord vs ADO Den Haag — Netherlands Eredivisie | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-198 | Poland vs Germany — FIBA Basketball World Cup 2027 European Qualifiers | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-199 | Frederikshavn White Hawks vs Sønderjyske — Danish Metal Ligaen | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-200 | Herning Blue Fox vs Rungsted Seier Capital — Danish Metal Ligaen | FINAL / RESEARCH SETTLED; operator definition unknown | Herning 4–3 OT versus 3–3 regulation; supplied 6.5 total changes side. Need actual contract terms.; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-201 | SC Freiburg vs Werder Bremen — Germany Bundesliga | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-202 | Randers FC vs AGF Aarhus — Denmark 3F Superliga | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-203 | RC Deportivo de A Coruña vs Valencia CF — LaLiga | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-204 | Boston Red Sox @ New York Yankees — MLB | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-205 | Chicago White Sox @ Minnesota Twins — MLB | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-206 | Los Angeles Dodgers @ Detroit Tigers — MLB | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-207 | Cagliari vs Inter Milan — Italy Serie A | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-208 | Lazio vs Genoa — Italy Serie A | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-209 | Corinthians vs Santos — Brazil Série A | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-210 | Flamengo vs Botafogo — Brazil Série A | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-211 | Jaime Faria vs Jenson Brooksby — US Open Men's Singles R1 | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-212 | McCartney Kessler vs Ekaterina Alexandrova — US Open Women R1 | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-213 | Toby Samuel vs Tomas Machac — US Open Men's Singles R1 | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-214 | Baltimore Orioles @ Athletics — MLB | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-215 | Japan vs Qatar — FIBA Basketball World Cup 2027 Asian Qualifiers | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-216 | Namibia vs Zimbabwe — Namibia T20I Tri-Series 2026 | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-217 | Trinbago Knight Riders vs Guyana Amazon Warriors — CPL | FINAL / RESEARCH SETTLED; operator definition unknown | Revised completed 16-over innings convention: C01 Over 174.5 WIN, C02 Under LOSS; six-over grades retained; OPERATOR_ACTION UNKNOWN_DEFINITION. See current retrospective.; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-218 | Ann Li vs Antonia Ruzic — US Open Women 2026 | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-219 | New York Mets (Robert Stock) @ Tampa Bay Rays (Ian Seymour) — MLB 2026 | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-220 | San Diego Padres (Michael King) @ Cincinnati Reds (Brady Singer) — MLB 2026 | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-221 | Miami Marlins (Ryan Gusto) @ Washington Nationals (Will Dion) — MLB 2026 | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-222 | Seattle Mariners (George Kirby) @ Boston Red Sox (Payton Tolle) — MLB 2026 | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-223 | New York Yankees at Los Angeles Angels | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-224 | Philadelphia Phillies (Aaron Nola) @ Arizona Diamondbacks (Brandon Pfaadt) — MLB 2026 | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-225 | Chun-Hsin Tseng vs Tianhui Zhang — ATP Challenger Zhangjiagang 2026 | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-226 | Hanshin Tigers @ Tokyo Yakult Swallows — NPB 2026 | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-227 | Hiroshima Toyo Carp @ Chunichi Dragons — NPB 2026 | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-228 | Orix Buffaloes @ Tohoku Rakuten Golden Eagles — NPB 2026 | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-229 | Hanwha Eagles @ KT Wiz — KBO 2026 | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-230 | KIA Tigers @ NC Dinos — KBO 2026 | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-231 | LG Twins @ Doosan Bears — KBO 2026 | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-232 | Lotte Giants @ Samsung Lions — KBO 2026 | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-233 | Beijing Guoan vs Lanzhou Longyuan Athletic — China FA Cup 2026 (quarterfinal, corrected) | FINAL / PARTIAL; corner field pending | New original reports confirm Beijing 3–1, half 1–0. Corner 13 inherited specialist-only.; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-234 | Dalian Yingbo vs Shanghai Shenhua — China FA Cup 2026 (quarterfinal, corrected) | FINAL / PARTIAL; corner field pending | New original reports confirm Dalian 1–0, half 0–0. Corner 10 inherited specialist-only.; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-235 | Shandong Taishan vs Shanghai Port — China FA Cup 2026 (quarterfinal, corrected) | FINAL / PARTIAL; corner field pending | New original reports confirm Shandong 0–3 Port, half 0–2. Corner 14 inherited specialist-only.; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-236 | England Women vs Ireland Women — 1st ODI, 2026 | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-237 | Zimbabwe vs South Africa — Namibia T20I Tri-Series 2026 | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-238 | Glasgow Cosmic vs Rotterdam Dockers — European T20 Premier League 2026 | FINAL / SETTLED | Inherited September 2 full canonical index; later controlling snapshots applied; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-239 | Athletics @ Texas Rangers | FINAL / SETTLED (inherited) | September 4 controlling snapshots / stored component; not re-researched as a new pending event; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-240 | Chicago White Sox @ Houston Astros | FINAL / SETTLED (inherited) | September 4 controlling snapshots / stored component; not re-researched as a new pending event; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-241 | Zachary Svajda vs Daniel Altmaier | FINAL / SETTLED (inherited) | September 4 controlling snapshots / stored component; not re-researched as a new pending event; retrospective source recovery: audit_2026-09-12/recovered_historical_retrospectives.md; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-242 | Fabian Marozsan vs Michael Zheng | FINAL / SETTLED (inherited) | September 4 controlling snapshots / stored component; not re-researched as a new pending event; retrospective source recovery: audit_2026-09-12/recovered_historical_retrospectives.md; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-243 | Magda Linette vs Francesca Jones | FINAL / SETTLED (inherited) | September 4 controlling snapshots / stored component; not re-researched as a new pending event; retrospective source recovery: audit_2026-09-12/recovered_historical_retrospectives.md; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-244 | Baltimore Orioles @ Colorado Rockies | FINAL / SETTLED (inherited) | September 4 controlling snapshots / stored component; not re-researched as a new pending event; retrospective source recovery: audit_2026-09-12/recovered_historical_retrospectives.md; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-245 | Alexander Zverev vs Lorenzo Sonego | FINAL / SETTLED (inherited) | September 4 controlling snapshots / stored component; not re-researched as a new pending event; retrospective source recovery: audit_2026-09-12/recovered_historical_retrospectives.md; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-246 | New York Yankees @ Los Angeles Angels | ADMINISTRATIVE / NO SCORED TRIAL | September 4 controlling snapshots / stored component; not re-researched as a new pending event; retrospective source recovery: audit_2026-09-12/recovered_historical_retrospectives.md; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-247 | Philadelphia Phillies @ Arizona Diamondbacks | FINAL / SETTLED (inherited) | September 4 controlling snapshots / stored component; not re-researched as a new pending event; retrospective source recovery: audit_2026-09-12/recovered_historical_retrospectives.md; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-248 | St. Louis Cardinals @ Los Angeles Dodgers | FINAL / SETTLED (inherited) | September 4 controlling snapshots / stored component; not re-researched as a new pending event; retrospective source recovery: audit_2026-09-12/recovered_historical_retrospectives.md; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-249 | Hanwha Eagles @ KT Wiz | ADMINISTRATIVE / NO SCORED TRIAL | September 4 controlling snapshots / stored component; not re-researched as a new pending event; retrospective source recovery: audit_2026-09-12/recovered_historical_retrospectives.md; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-250 | Yunnan Yukun vs Chongqing Tonglianglong | INHERITED CLOSED; corner row still unsettleable — no keyless China FA Cup route (re-probed 2026-09-16), see TMP-AUDIT queue | Issued card/available retrospective restored to Part 1; missing P267 settlement artifact not recreated; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-251 | Sassuolo vs Frosinone | INHERITED CLOSED; corner row reproduced 2026-09-16 at ESPN `ita.coppa_italia` (6+5 = 11, threshold-invariant research WIN); Lega Serie A record still unreached — see TMP-AUDIT queue and [Part 4 Appendix A](PREDICTION_LOG_COMBINED_4.md) | Issued card/available retrospective restored to Part 1; missing P267 settlement artifact not recreated; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-252 | Belfast Wolves vs Edinburgh Castle Rockers | FINAL / SETTLED (inherited) | September 4 controlling snapshots / stored component; not re-researched as a new pending event; retrospective source recovery: audit_2026-09-12/recovered_historical_retrospectives.md; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-253 | El Gounah vs Al Mokawloon Al Arab | FINAL / SETTLED (inherited) | September 4 controlling snapshots / stored component; not re-researched as a new pending event; retrospective source recovery: audit_2026-09-12/recovered_historical_retrospectives.md; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-254 | Jan Choinski vs Botic Van de Zandschulp | FINAL / SETTLED (inherited) | September 4 controlling snapshots / stored component; not re-researched as a new pending event; retrospective source recovery: audit_2026-09-12/recovered_historical_retrospectives.md; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-255 | Inter Women vs VfL Wolfsburg Women | Other rows retain recorded status; C05 UNRESOLVED_PERIOD, TMP-AUDIT-20260912-03 reopened 2026-09-17(c) | Whole-match 24 corners does not prove regulation Over 8.5; original custody Part 1, evidence/correction Part 4 Appendix A |
| P-256 | Paris Saint-Germain Women vs Eintracht Frankfurt Women | Other rows retain recorded status; C05 UNRESOLVED_PERIOD, TMP-AUDIT-20260912-04 reopened 2026-09-17(c) | Whole-match 15 corners does not prove regulation Over 8.5; original custody Part 1, evidence/correction Part 4 Appendix A |
| P-257 | San Diego Padres @ Cincinnati Reds | FINAL / SETTLED (inherited) | September 4 controlling snapshots / stored component; not re-researched as a new pending event; retrospective source recovery: audit_2026-09-12/recovered_historical_retrospectives.md; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-258 | Atlanta Braves @ Washington Nationals | FINAL / SETTLED (inherited) | September 4 controlling snapshots / stored component; not re-researched as a new pending event; retrospective source recovery: audit_2026-09-12/recovered_historical_retrospectives.md; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-259 | New York Mets @ Tampa Bay Rays | FINAL / SETTLED (inherited) | September 4 controlling snapshots / stored component; not re-researched as a new pending event; retrospective source recovery: audit_2026-09-12/recovered_historical_retrospectives.md; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-260 | San Francisco Giants @ Pittsburgh Pirates | FINAL / SETTLED (inherited) | September 4 controlling snapshots / stored component; not re-researched as a new pending event; retrospective source recovery: audit_2026-09-12/recovered_historical_retrospectives.md; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-261 | Toronto Blue Jays @ Cleveland Guardians | FINAL / SETTLED (inherited) | September 4 controlling snapshots / stored component; not re-researched as a new pending event; retrospective source recovery: audit_2026-09-12/recovered_historical_retrospectives.md; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-262 | Trinbago Knight Riders vs Antigua & Barbuda Falcons | FINAL / SETTLED (inherited) | September 4 controlling snapshots / stored component; not re-researched as a new pending event; retrospective source recovery: audit_2026-09-12/recovered_historical_retrospectives.md; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-263 | Jaime Faria vs Carlos Alcaraz | FINAL / SETTLED (inherited) | September 4 controlling snapshots / stored component; not re-researched as a new pending event; retrospective source recovery: audit_2026-09-12/recovered_historical_retrospectives.md; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-264 | Chicago White Sox @ Houston Astros | FINAL / SETTLED (inherited) | September 4 controlling snapshots / stored component; not re-researched as a new pending event; retrospective source recovery: audit_2026-09-12/recovered_historical_retrospectives.md; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-265 | Toluca vs Club León | INHERITED CLOSED; corner row reproduced 2026-09-16 at ESPN `concacaf.leagues.cup` (4+5 = 9 — research WIN at exactly the threshold, provider-sensitive); see TMP-AUDIT queue and [Part 4 Appendix A](PREDICTION_LOG_COMBINED_4.md) | Issued card/available retrospective restored to Part 1; missing P267 settlement artifact not recreated; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-266 | New York Yankees @ Los Angeles Angels | FINAL / SETTLED (inherited) | September 4 controlling snapshots / stored component; not re-researched as a new pending event; retrospective source recovery: audit_2026-09-12/recovered_historical_retrospectives.md; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-267 | Lanlana Tararudee vs Linda Noskova | FINAL / SETTLED (inherited) | September 4 controlling snapshots / stored component; not re-researched as a new pending event; retrospective source recovery: audit_2026-09-12/recovered_historical_retrospectives.md; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-268 | Hanwha Eagles @ KT Wiz | FINAL / SETTLED (inherited) | September 4 controlling snapshots / stored component; not re-researched as a new pending event; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-269 | KIA Tigers @ NC Dinos — cancelled before first pitch | ADMINISTRATIVE / NO SCORED TRIAL | September 4 controlling snapshots / stored component; not re-researched as a new pending event; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-270 | Canterbury-Bankstown Bulldogs vs Brisbane Broncos | FINAL / SETTLED (inherited) | September 4 controlling snapshots / stored component; not re-researched as a new pending event; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-271 | Fremantle vs Hawthorn — AFL first qualifying final | FINAL / SETTLED (inherited) | September 4 controlling snapshots / stored component; not re-researched as a new pending event; [canonical log](PREDICTION_LOG_COMBINED.md) |
| P-272 | Naomi Osaka vs Katerina Siniakova | ADMINISTRATIVE / NO SCORED TRIAL | September 4 controlling snapshots / stored component; not re-researched as a new pending event; [canonical log](PREDICTION_LOG_COMBINED_2.md) |
| P-273 | Palermo vs Mantova | FINAL / SETTLED — Palermo 5-2 Mantova (HT 2-0); Palermo 3 corners, Mantova 2; Palermo Over 4.5 corners LOSS | 2026-09-06 audit: corners confirmed from `SRC-ESPN-SITE-API-SOCCER` (`ita.coppa_italia`/`401911809`). No longer provisional; outcome unchanged; [canonical log](PREDICTION_LOG_COMBINED_2.md) |
| P-274 | San Francisco Giants @ Pittsburgh Pirates | FINAL / RESEARCH SETTLED; operator definition unknown | Standard-action score grades remain settled. A Jared Jones-listed contract may have different action; no such ticket/terms supplied. Preserve conditional review, not automatic VOID.; [canonical log](PREDICTION_LOG_COMBINED_2.md) |
| P-275 | Alexander Zverev vs Quentin Halys | FINAL / SETTLED (inherited) | September 4 controlling snapshots / stored component; not re-researched as a new pending event; [canonical log](PREDICTION_LOG_COMBINED_2.md) |
| P-276 | UAlbany @ Buffalo | FINAL / SETTLED (inherited) | September 4 controlling snapshots / stored component; not re-researched as a new pending event; [canonical log](PREDICTION_LOG_COMBINED_2.md) |
| P-277 | Athletics @ Seattle Mariners | FINAL / SETTLED (inherited) | September 4 controlling snapshots / stored component; not re-researched as a new pending event; [canonical log](PREDICTION_LOG_COMBINED_2.md) |
| P-278 | St. Louis Cardinals @ Los Angeles Dodgers | FINAL / SETTLED (inherited) | September 4 controlling snapshots / stored component; not re-researched as a new pending event; [canonical log](PREDICTION_LOG_COMBINED_2.md) |
| P-279 | Mineros de Zacatecas vs Abejas de León | FINAL / SETTLED (inherited) | September 4 controlling snapshots / stored component; not re-researched as a new pending event; [canonical log](PREDICTION_LOG_COMBINED_2.md) |
| P-280 | South Sydney Rabbitohs vs Sydney Roosters | FINAL / SETTLED — Rabbitohs 50–20 Roosters | New September 5 source-backed audit; ordinary completed endpoint; [canonical log](PREDICTION_LOG_COMBINED_2.md) |
| P-281 | Rakuten Monkeys @ Fubon Guardians | FINAL / SETTLED — Rakuten 0–13 Fubon | New September 5 source-backed audit; ordinary completed endpoint; [canonical log](PREDICTION_LOG_COMBINED_2.md) |
| P-282 | TSG Hawks @ Uni-Lions | FINAL / SETTLED — TSG 0–11 Uni | New September 5 source-backed audit; ordinary completed endpoint; [canonical log](PREDICTION_LOG_COMBINED_2.md) |
| P-283 | Namibia vs South Africa — tri-series match 6 | FINAL / SETTLED — South Africa 228/4; Namibia 217/3 (20 overs each) | New September 5 source-backed audit; ordinary completed endpoint; [canonical log](PREDICTION_LOG_COMBINED_2.md) |
| P-284 | USA vs China — Women’s World Cup | FINAL / SETTLED — USA 94–61 China | New September 5 source-backed audit; ordinary completed endpoint; [canonical log](PREDICTION_LOG_COMBINED_2.md) |
| P-285 | Korea vs Nigeria — Women’s World Cup | FINAL / SETTLED — Korea 99–81 Nigeria | New September 5 source-backed audit; ordinary completed endpoint; [canonical log](PREDICTION_LOG_COMBINED_2.md) |
| P-286 | Glasgow Cosmic vs Belfast Wolves — Match 13 | FINAL / SETTLED — Belfast 146/3; Glasgow 120/8 (12 overs each) | New September 5 source-backed audit; ordinary completed endpoint; [canonical log](PREDICTION_LOG_COMBINED_2.md) |
| P-287 | Alexander Bublik vs Tommy Paul — US Open R3 | FINAL / SETTLED — Paul won 6–4, 3–6, 6–7(4), 6–1, 6–3 | New September 5 source-backed audit; ordinary completed endpoint; [canonical log](PREDICTION_LOG_COMBINED_2.md) |
| P-288 | Athletics @ Seattle Mariners — September 4 local | FINAL / SETTLED — Athletics 7–6 Mariners; Mariners -1.5 LOSS | 2026-09-05(b) audit; confirmed final matches first-check in-progress score, no change; [canonical log](PREDICTION_LOG_COMBINED_2.md) |
| P-289 | Western Bulldogs vs Sydney Swans — Round 4 | FINAL / SETTLED — Bulldogs 60–33 Sydney (9.6–5.3) | New September 5 source-backed audit; ordinary completed endpoint; [canonical log](PREDICTION_LOG_COMBINED_2.md) |
| P-290 | FC Juárez vs Pachuca — Liga MX | FINAL / SETTLED — Pachuca 2–0 | Full slate W/L/W/W/L; fresh ESPN corners Pachuca 3, Juárez 1 settles rank 4 most corners as research WIN.; [canonical log](PREDICTION_LOG_COMBINED_2.md) |
| P-291 | Ben Shelton vs Denis Shapovalov — US Open R3 | FINAL / SETTLED — Shelton d. Shapovalov 7-6(3), 6-7(5), 6-3, 6-4 (25–20 games); Shapovalov +5.5 games WIN | 2026-09-05(b) audit; [canonical log](PREDICTION_LOG_COMBINED_2.md) |
| P-292 | Euro-Yroke/St Kilda vs North Melbourne — AFLW | FINAL / SETTLED — North Melbourne 14.15 (99) d. St Kilda 1.1 (7); Under 89.5 LOSS | 2026-09-05(b) audit; AFL official match report verbatim quote; [canonical log](PREDICTION_LOG_COMBINED_2.md) |
| P-293 | Yartapuulti/Port Adelaide vs Gold Coast — AFLW | FINAL / SETTLED — Gold Coast 2.5 (17) d. Port Adelaide 1.8 (14); Gold Coast +13.5 WIN | 2026-09-05(b) audit; [canonical log](PREDICTION_LOG_COMBINED_2.md) |
| P-294 | Newcastle Knights (W) vs Canterbury-Bankstown Bulldogs (W) — NRLW Round 10 | FINAL / SETTLED — Newcastle 56–22 Canterbury; Under 48.5 LOSS, Knights -15.5 WIN | 2026-09-05(b) audit; ABC NRLW Score Centre verbatim quote; [canonical log](PREDICTION_LOG_COMBINED_2.md) |
| P-295 | North Queensland Cowboys vs Canberra Raiders — NRL Round 27 | FINAL / SETTLED — Raiders 50–30 Cowboys (major upset, Coby Black debut record); Under 56.5 LOSS, Cowboys -5.5 LOSS | 2026-09-05(b) audit; deep retrospective, L-075 adopted; [canonical log](PREDICTION_LOG_COMBINED_2.md) |
| P-296 | Doosan Bears @ SSG Landers — KBO | FINAL / SETTLED — SSG 3–2 Doosan; Under 10.5 WIN, SSG +1.5 WIN | 2026-09-05(b) audit; clean top-two win; [canonical log](PREDICTION_LOG_COMBINED_2.md) |
| P-297 | Hanwha Eagles @ Lotte Giants — KBO | FINAL / SETTLED — Hanwha 11–6 Lotte; Hanwha ML WIN, Under 11.0 LOSS | 2026-09-05(b) audit; [canonical log](PREDICTION_LOG_COMBINED_2.md) |
| P-298 | Brisbane Lions (W) vs GWS GIANTS (W) — AFLW Round 4 | FINAL / SETTLED — Brisbane 7.13 (55) d. GWS 3.6 (24); GWS +29.5 LOSS, Under 95.5 WIN | 2026-09-05(b) audit; L-077 adopted; [canonical log](PREDICTION_LOG_COMBINED_2.md) |
| P-299 | Mali (W) vs Spain (W) — FIBA Women's World Cup Group A | FINAL / SETTLED — Mali 82–73 Spain (major upset); Spain -25.5 LOSS, Under 144.5 LOSS | 2026-09-05(b) audit; deep retrospective, L-076 adopted; [canonical log](PREDICTION_LOG_COMBINED_2.md) |
| P-300 | Rotterdam Dockers vs Edinburgh Castle Rockers — ETPL Match 14 | FINAL / SETTLED — ECR 148 (19.3 ov) d. Rotterdam 93 (18 ov) by 55 runs; ECR powerplay 28/3; PP Over 50.5 LOSS, PP Under 50.5 WIN, 20-ov Under 168.5 WIN | 2026-09-06 audit closed the powerplay evidence gap from `SRC-ESPN-SITE-API-CRICKET`; cross-checked against ESPNcricinfo fall of wickets. Deep Rank-#1-loss retrospective recorded (L-083, bimodal phase totals); [canonical log](PREDICTION_LOG_COMBINED_2.md) |
| P-301 | Cronulla Sharks vs Melbourne Storm — NRL Round 27 | FINAL / SETTLED — Melbourne 24–20 Cronulla (last-second try); Storm -8.5 LOSS, Under 52.5 WIN | 2026-09-05(b) audit; [canonical log](PREDICTION_LOG_COMBINED_2.md) |
| P-302 | Newcastle United vs AFC Bournemouth — EPL Matchweek 3 | FINAL / SETTLED — 2-2; Bournemouth 3 corners, Newcastle 4; BOU Over 2.5 corners WIN, 1H Over 0.5 WIN, FT Over 2.5 WIN | 2026-09-06 audit closed the corners evidence gap from `SRC-ESPN-SITE-API-SOCCER` (`eng.1`/`401879286`, `wonCorners`). This settlement falsified L-073's stated premise; see L-081; [canonical log](PREDICTION_LOG_COMBINED_2.md) |
| P-303 | Nigeria (W) vs Hungary (W) — FIBA Women's World Cup Group B | FINAL / SETTLED — Nigeria 81–53 Hungary; Nigeria +25.5 WIN, Under 145.5 WIN | 2026-09-05(b) audit; clean top-two win; [canonical log](PREDICTION_LOG_COMBINED_2.md) |
| P-304 | Slavia Praha vs Zbrojovka Brno — Chance Liga | FINAL / SETTLED — 4–0, HT 1–0 | Full five-rank slate recovered from preserved mini: W/W/W/L/L. Official Slavia corners 5. Prior archival-omission claim withdrawn.; [canonical log](PREDICTION_LOG_COMBINED_2.md) |
| P-305 | Dublin Guardians vs Amsterdam Flames — ETPL | FINAL / SETTLED — Amsterdam 169/7 vs Dublin 160/8 | Full FOUR-rank slate recovered: W/L/W/L. PP 60/1; batting-first condition met. Prior archival-omission claim withdrawn.; [canonical log](PREDICTION_LOG_COMBINED_2.md) |
| P-306 | Manchester City v Coventry | FINAL / SETTLED | City 1–0 Coventry; W/L/L/W/L; [Full retrospective](archive/mini_logs/PREDICTION_MINI_LOG_SETTLEMENT_2026-09-06.md#p-306); [canonical log](PREDICTION_LOG_COMBINED_2.md) |
| P-307 | India Women v Pakistan Women | ADMINISTRATIVE / NO SCORED TRIAL | ADMINISTRATIVE / NO FORECAST ISSUED; [Full retrospective](archive/mini_logs/PREDICTION_MINI_LOG_SETTLEMENT_2026-09-06.md#p-307); [canonical log](PREDICTION_LOG_COMBINED_2.md) |
| P-308 | Francisco Cerundolo v Taylor Fritz | FINAL / SETTLED | Cerundolo 3–2 Fritz, games 25–23; W/W/L/L; [Full retrospective](archive/mini_logs/PREDICTION_MINI_LOG_SETTLEMENT_2026-09-06.md#p-308); [canonical log](PREDICTION_LOG_COMBINED_2.md) |
| P-309 | Gardner-Webb v Wofford | FINAL / SETTLED | Wofford 17–13 Gardner-Webb; W/L/W/L; [Full retrospective](archive/mini_logs/PREDICTION_MINI_LOG_SETTLEMENT_2026-09-06.md#p-309); [canonical log](PREDICTION_LOG_COMBINED_2.md) |
| P-310 | Luciano Darderi v Dane Sweeny | FINAL / SETTLED | Darderi 3–0 Sweeny, games 18–10; L/L/W/W; [Full retrospective](archive/mini_logs/PREDICTION_MINI_LOG_SETTLEMENT_2026-09-06.md#p-310); [canonical log](PREDICTION_LOG_COMBINED_2.md) |
| P-311 | Barbados Women v Trinbago Knight Riders Women | FINAL / SETTLED | TKR Women 155 beat Barbados 134, PP 71/1; L/L/W/W; [Full retrospective](archive/mini_logs/PREDICTION_MINI_LOG_SETTLEMENT_2026-09-06.md#p-311); [canonical log](PREDICTION_LOG_COMBINED_2.md) |
| P-312 | Detroit Tigers v Cleveland Guardians | FINAL / SETTLED | Detroit 6–0 Cleveland; W/L/W/L; [Full retrospective](archive/mini_logs/PREDICTION_MINI_LOG_SETTLEMENT_2026-09-06.md#p-312); [canonical log](PREDICTION_LOG_COMBINED_2.md) |
| P-313 | Cincinnati Reds v Milwaukee Brewers | FINAL / SETTLED | Cincinnati 5–3 Milwaukee; L/L/W/W; [Full retrospective](archive/mini_logs/PREDICTION_MINI_LOG_SETTLEMENT_2026-09-06.md#p-313); [canonical log](PREDICTION_LOG_COMBINED_2.md) |
| P-314 | Los Angeles Angels v Pittsburgh Pirates | FINAL / SETTLED | Angels 6–1 Pittsburgh; W/L/W/L/W/L; [Full retrospective](archive/mini_logs/PREDICTION_MINI_LOG_SETTLEMENT_2026-09-06.md#p-314); [canonical log](PREDICTION_LOG_COMBINED_2.md) |
| P-315 | Melbourne v West Coast (AFLW) | FINAL / SETTLED | Melbourne 81–44 West Coast; L/L/W/W; [Full retrospective](archive/mini_logs/PREDICTION_MINI_LOG_SETTLEMENT_2026-09-06.md#p-315); [canonical log](PREDICTION_LOG_COMBINED_2.md) |
| P-316 | Doosan Bears v SSG Landers (superseded card) | CANONICAL ALIAS OF P-317; no separate trial | SUPERSEDED / ARCHIVAL ONLY, same event as P-317; [Full retrospective](archive/mini_logs/PREDICTION_MINI_LOG_SETTLEMENT_2026-09-06.md#p-316); [canonical log](PREDICTION_LOG_COMBINED_2.md) |
| P-317 | Doosan Bears v SSG Landers | FINAL / SETTLED | Doosan 16–9 SSG; L/L/W/W; [Full retrospective](archive/mini_logs/PREDICTION_MINI_LOG_SETTLEMENT_2026-09-06.md#p-317); [canonical log](PREDICTION_LOG_COMBINED_2.md) |
| P-318 | Henan vs Chengdu Rongcheng — CSL R26 | FINAL / SETTLED | Henan 0–0 Chengdu; L/L/L/W/W; [canonical log](PREDICTION_LOG_COMBINED_2.md) |
| P-319 | Yunnan Yukun vs Liaoning Tieren — CSL R26 | FINAL / SETTLED (`START-CROSSED / LIVE 0-0`) | Yunnan 5–0; W/W/W/L/L; [canonical log](PREDICTION_LOG_COMBINED_2.md) |
| P-320 | Tianjin Jinmen Tigers vs Zhejiang — CSL R26 | FINAL / SETTLED | Tianjin 2–1; W/L/W/L/L; [canonical log](PREDICTION_LOG_COMBINED_2.md) |
| P-321 | Sønderjyske vs AC Horsens — Denmark Superliga R7 | FINAL / SETTLED | Sønderjyske 2–5; W/L/W/L/L; [canonical log](PREDICTION_LOG_COMBINED_2.md) |
| P-322 | South Africa vs Zimbabwe — Namibia T20I Tri-Series Final | FINAL / SETTLED (`START-CROSSED / TOSS-CONDITIONAL`) | SA 205/5 bt Zimbabwe 157; W/W/L/L; [canonical log](PREDICTION_LOG_COMBINED_2.md) |
| P-323 | Everton vs Manchester United — EPL MW3 | FINAL / SETTLED (`EPL PRIMARY_SCORED`) | Everton 2–2; L/L/W/L/W; Brier 0.3749; [canonical log](PREDICTION_LOG_COMBINED_2.md) |
| P-324 | Valencia vs Barcelona — LaLiga MD4 | ADMINISTRATIVE / NO SCORED TRIAL | Valencia 0–5 Barcelona; [canonical log](PREDICTION_LOG_COMBINED_2.md) |
| P-325 | Bangladesh W vs Sri Lanka W — Women's Asia Cup M10 | FINAL / SETTLED | BAN 114/8; SL won by 4 wkts; W/W/L/L; Brier 0.1332; [canonical log](PREDICTION_LOG_COMBINED_2.md) |
| P-326 | Western Carolina @ Campbell — NCAA FCS | ADMINISTRATIVE / NO SCORED TRIAL | Campbell 28–19; [canonical log](PREDICTION_LOG_COMBINED_2.md) |
| P-327 | Angers SCO vs Rennes — Ligue 1 | FINAL / SETTLED (best card of cohort) | Angers 1–2; W/W/W/L/L; Brier 0.1149; [canonical log](PREDICTION_LOG_COMBINED_2.md) |
| P-328 | Arsenal vs Chelsea — EPL MW3 | FINAL / SETTLED (`EPL PRIMARY_SCORED`) | Arsenal 2–1; W/W/W/L/L; Brier 0.1582; [canonical log](PREDICTION_LOG_COMBINED_2.md) |
| P-329 | Bologna vs Sassuolo — Serie A MD3 | FINAL / SETTLED | Bologna 2–2; W/L/W/L/W; Brier 0.2460; [canonical log](PREDICTION_LOG_COMBINED_2.md) |
| P-330 | Puerto Rico W vs Belgium W — FIBA W WC | ADMINISTRATIVE / NO SCORED TRIAL | Puerto Rico 64–76; [canonical log](PREDICTION_LOG_COMBINED_2.md) |
| P-331 | Milwaukee Brewers @ Cincinnati Reds — MLB | FINAL / SETTLED (`MLB PRIMARY_SCORED`) | Cincinnati 12–8; W/W/L/L; Brier 0.1893; [canonical log](PREDICTION_LOG_COMBINED_2.md) |
| P-332 | Deportivo Alavés vs CA Osasuna — LaLiga MD4 | FINAL / SETTLED | Alavés 5–2; L/L/W/L/W; Brier 0.2876; [canonical log](PREDICTION_LOG_COMBINED_2.md) |
| P-333 | Pakistan W vs Hong Kong W — Women's T20 Asia Cup Gp A | ADMINISTRATIVE / NO SCORED TRIAL | Pakistan 143/8 bt Hong Kong 71 by 72 runs; [canonical log](PREDICTION_LOG_COMBINED_3.md) |
| P-334 | Germany W vs Mali W — FIBA W World Cup Gp A | ADMINISTRATIVE / NO SCORED TRIAL | Germany 83–58 Mali; [canonical log](PREDICTION_LOG_COMBINED_3.md) |
| P-335 | Washington Nationals @ San Diego Padres — MLB | FINAL / SETTLED (`MLB PRIMARY_SCORED`) | SD 3–2 WSH; W/L/L/W; winner W; Brier 0.2541; [canonical log](PREDICTION_LOG_COMBINED_3.md) |
| P-336 | Carabobo FC vs Estudiantes de Mérida — Venezuela Clausura J8 | FINAL / SETTLED — top 3 rows all won | Carabobo 1–0 (HT 1–0); W/W/W/L/L; winner W; Brier 0.1751; [canonical log](PREDICTION_LOG_COMBINED_3.md) |
| P-337 | Barracas Central vs Argentinos Juniors — Argentina Clausura F8 | FINAL / SETTLED — deep retro (R2+R3 lost, winner wrong) | 0–0 (HT 0–0); W/L/L/W/L; winner L (draw); Brier 0.2603; [canonical log](PREDICTION_LOG_COMBINED_3.md) |
| P-338 | Iva Jovic vs Coco Gauff — US Open Women's R16 | FINAL / SETTLED — best card of cohort, top 2 won | Gauff 6–1, 6–4; W/W/L/L; winner W; Brier 0.2163; [canonical log](PREDICTION_LOG_COMBINED_3.md) |
| P-339 | Doosan Bears @ Hanwha Eagles — KBO | FINAL / SETTLED — deep Rank-#1 retro | Hanwha 6–1; L/L/W/W; winner W; Brier 0.3368; [canonical log](PREDICTION_LOG_COMBINED_3.md) |
| P-340 | Incheon United vs Bucheon FC 1995 — K League 1 R28 | FINAL / SETTLED — top 2 rows both won | Incheon 2–1 (HT 1–1); W/W/L/W/L; winner W; Brier 0.2155; [canonical log](PREDICTION_LOG_COMBINED_3.md) |
| P-341 | BUL FC vs Ntugasaze FC — Uganda Premier League R3 | FINAL / PARTIAL; corner field pending | BUL 4–1 (HT 2–1); W/L/—/W/L; winner W; 4-row Brier 0.2443; [canonical log](PREDICTION_LOG_COMBINED_3.md) |
| P-342 | MŠK Novohrad Lučenec vs KFC Komárno — Slovnaft Cup R3 | FINAL / PARTIAL; corner field pending | Komárno 2–0 (HT 0–0); L/L/—/W/W; winner W; 4-row Brier 0.3880; [canonical log](PREDICTION_LOG_COMBINED_3.md) |
| P-343 | Bangladesh W vs UAE W — Women's T20 Asia Cup Gp B | ADMINISTRATIVE / NO SCORED TRIAL | Bangladesh 103/7 bt UAE 69/9 by 34 runs; [canonical log](PREDICTION_LOG_COMBINED_3.md) |
| P-344 | Hungary W vs Japan W — FIBA W World Cup Qual. to QF | FINAL / SETTLED — deep Rank-#1 retro; mini-log's stated 0.2834 corrected | Hungary 84–63 (total 147); L/W/L/W; winner W; Brier 0.3334; [canonical log](PREDICTION_LOG_COMBINED_3.md) |
| P-345 | Club Brugge v Aston Villa — UCL MD1 | FINAL / SETTLED (corner row settled at UEFA this pass) — deep Rank-#1 retro | R1 L, R2 W, R3 W, R4 W, R5 L; winner L; Brier 0.2466; [canonical log](PREDICTION_LOG_COMBINED_3.md) |
| P-346 | AEK Athens v LASK — UCL MD1 | FINAL / SETTLED — all five rows won | W W W W W; winner W; Brier 0.0816; [canonical log](PREDICTION_LOG_COMBINED_3.md) |
| P-347 | Rangers @ Mariners (`MLB PRIMARY_SCORED`) | FINAL / SETTLED | W L W L; winner W; Brier 0.2374; [canonical log](PREDICTION_LOG_COMBINED_3.md) |
| P-348 | Blue Jays @ Athletics (`MLB PRIMARY_SCORED`) | FINAL / SETTLED | W L L L; winner W; Brier 0.2803; [canonical log](PREDICTION_LOG_COMBINED_3.md) |
| P-349 | Cardinals @ Giants (`MLB PRIMARY_SCORED`) | FINAL / SETTLED — all four rows won | W W W W; winner L; Brier 0.1440; [canonical log](PREDICTION_LOG_COMBINED_3.md) |
| P-350 | Shelton v Alcaraz — US Open men's QF | FINAL / SETTLED — deep Rank-#1 retro | L W W W; winner = R1; Brier 0.2574; [canonical log](PREDICTION_LOG_COMBINED_3.md) |
| P-351 | Reds @ Dodgers (`MLB PRIMARY_SCORED`) | FINAL / SETTLED — top two won | W W L L; winner W; Brier 0.2460; [canonical log](PREDICTION_LOG_COMBINED_3.md) |
| P-352 | Namibia v South Africa — 1st ODI | FINAL / SETTLED — deep Rank-#1 retro | L W W W; winner W; Brier 0.2158; [canonical log](PREDICTION_LOG_COMBINED_3.md) |
| P-353 | Dragons @ Giants — NPB, 9 Sep | FINAL / SETTLED | W L W L; winner L; Brier 0.2549; [canonical log](PREDICTION_LOG_COMBINED_3.md) |
| P-354 | Carp @ Tigers — NPB | FINAL / SETTLED | W L L W; winner L; Brier 0.2968; [canonical log](PREDICTION_LOG_COMBINED_3.md) |
| P-355 | Sydney FC v Melbourne Victory — Australia Cup SF | FINAL / SETTLED (corner row settled at FotMob this pass) — top two won | W W L W W; winner L; Brier 0.1531; [canonical log](PREDICTION_LOG_COMBINED_3.md) |
| P-356 | KT @ Samsung — KBO | FINAL / SETTLED — deep Rank-#1 retro | L W W W; winner L; Brier 0.2418; [canonical log](PREDICTION_LOG_COMBINED_3.md) |
| P-357 | Dublin Guardians v Belfast Wolves — ETPL M18 | FINAL / SETTLED — deep Rank-#1 retro | L L W W; winner L; Brier 0.3377; [canonical log](PREDICTION_LOG_COMBINED_3.md) |
| P-358 | Puerto Rico W v China W — FIBA WWC (mini-log alias `TMP-CANON-20260911-01`, retired) | FINAL / SETTLED — deep Rank-#1 retro | L W L W; winner W; Brier 0.2973; [canonical log](PREDICTION_LOG_COMBINED_3.md) |
| P-359 | Jordan v Chinese Taipei — Asian Games | FINAL / SETTLED | W L W L; winner L; Brier 0.2467; [canonical log](PREDICTION_LOG_COMBINED_3.md) |
| P-360 | South Korea v Saudi Arabia — Asian Games | FINAL / SETTLED | W L W L; winner W; Brier 0.2409; [canonical log](PREDICTION_LOG_COMBINED_3.md) |
| P-361 | Dragons @ Giants — NPB, 10 Sep | FINAL / SETTLED | W L W L; winner W; Brier 0.2493; [canonical log](PREDICTION_LOG_COMBINED_3.md) |
| P-362 | Eagles @ Landers — KBO | FINAL / SETTLED | W L W L; winner W; Brier 0.2450; [canonical log](PREDICTION_LOG_COMBINED_3.md) |
| P-363 | Roosters W v Bulldogs W — NRLW R11 | FINAL / SETTLED — top two won | W W L L; winner W; Brier 0.1773; [canonical log](PREDICTION_LOG_COMBINED_3.md) |
| P-364 | England v Pakistan — 3rd Test (Day-2 card) | FINAL / SETTLED (2026-09-15) — England won by 8 wickets on Day 4 (12 Sep); winner label settled | L L W W; winner **W**; Brier 0.3429 (4 ranked rows; winner label not a Brier row); [canonical log](PREDICTION_LOG_COMBINED_3.md) §"2026-09-15"; [combined log §"2026-09-15"](PREDICTION_LOG_COMBINED_3.md) |
| P-365 | Uni-Lions @ CTBC Brothers — CPBL | FINAL / SETTLED — deep Rank-#1 retro | L W L W; winner W; Brier 0.2768; [canonical log](PREDICTION_LOG_COMBINED_3.md) |
| P-366 | Rotterdam v Glasgow — ETPL M19 | FINAL / CLOSED; C02/C03 terminal censored, other rows settled | W C C L; winner W; Brier 0.1936 (2 rows); [canonical log](PREDICTION_LOG_COMBINED_3.md) |
| P-367 | China W v France W — FIBA WWC QF | FINAL / SETTLED — top two won | W W L L; winner W; Brier 0.2071; [canonical log](PREDICTION_LOG_COMBINED_3.md) |
| P-368 | Al Jazira v Al Nasr — UAE Pro League | FINAL / PARTIAL; corner field pending | W P L W L; winner L (draw); Brier 0.1917 (4 rows); [canonical log](PREDICTION_LOG_COMBINED_3.md) |
| P-369 | Dubai United v Shabab Al Ahli — UAE Pro League | FINAL / PARTIAL; corner field pending | P L L W W; winner L (draw); Brier 0.3909 (4 rows); [canonical log](PREDICTION_LOG_COMBINED_3.md) |
| P-370 | Jamaica Empress W v TKR W — WCPL | ADMINISTRATIVE / NO SCORED TRIAL | none issued; [canonical log](PREDICTION_LOG_COMBINED_3.md) |
| P-371 | Belgium W v Germany W — FIBA WWC QF | FINAL / SETTLED — deep Rank-#1 retro | L L W W; winner L; Brier 0.3145; [canonical log](PREDICTION_LOG_COMBINED_3.md) |
| P-372 | — | RESERVED / UNUSED — no record was ever issued under this ID (both external sessions started at P-373 / P-390 / P-407) | none |
| P-373 | Tampa Bay Rays @ Atlanta Braves — MLB — 2026-09-10 (Atlanta local) | FINAL / SETTLED | L W L W |
| P-374 | Fenerbahçe vs Roma — UEFA Champions League — 2026-09-10 | FINAL / SETTLED — canonical record for Fenerbahçe v Roma; absorbs TMP-SETTLED-20260911-01 | W W W L L |
| P-375 | Coco Gauff vs Elena Rybakina — US Open Women — Semifinal | FINAL / SETTLED | W W L L |
| P-376 | San Francisco 49ers vs Los Angeles Rams — NFL Week 1 — Melbourne | FINAL / SETTLED | W L W L |
| P-377 | Xelajú MC vs Cobán Imperial — Guatemala Liga Nacional Apertura 2026 | FINAL / PARTIAL — C02 corners provisional (TMP-OPEN-20260912-01) | L P L W W |
| P-378 | Philippines vs Bahrain — 2026 Aichi-Nagoya Asian Games Men's Basketball | FINAL / SETTLED | L L W W |
| P-379 | Namibia vs South Africa — 2nd ODI — South Africa tour of Namibia 2026 | FINAL / SETTLED | W W L L |
| P-380 | Wests Tigers (W) vs Canberra Raiders (W) — NRLW Round 11, 2026 | FINAL / SETTLED | W W L L |
| P-381 | Chiba Lotte Marines @ Fukuoka SoftBank Hawks — NPB Pacific League | FINAL / SETTLED | W W L L |
| P-382 | Saitama Seibu Lions @ Orix Buffaloes — NPB Pacific League | FINAL / SETTLED | L W W L |
| P-383 | Yokohama DeNA BayStars @ Hiroshima Toyo Carp — NPB Central League | FINAL / SETTLED | L L W W |
| P-384 | Kiwoom Heroes @ Samsung Lions — KBO League | FINAL / SETTLED | W W L L |
| P-385 | KT Wiz @ Lotte Giants — KBO League | FINAL / SETTLED | W L W L |
| P-386 | South Sydney Rabbitohs vs Newcastle Knights — NRL Finals Week 1 Elimination Final | FINAL / SETTLED | W L W L |
| P-387 | Kyoto Sanga F.C. vs Kashiwa Reysol — J1 League | FINAL / SETTLED | W L L W L |
| P-388 | Fremantle Dockers vs Geelong Cats — AFL First Semi-Final | FINAL / SETTLED | L L W W |
| P-389 | Dublin Guardians vs Edinburgh Castle Rockers — ETPL 2026 Match 21 | ADMINISTRATIVE / NO FORECAST (toss gate withheld correctly) | none issued |
| P-390 | Cincinnati Reds @ Milwaukee Brewers — MLB | FINAL / SETTLED | W L W L |
| P-391 | Cleveland Guardians @ Minnesota Twins — MLB | FINAL / SETTLED | L W L W |
| P-392 | Chicago White Sox @ St. Louis Cardinals — MLB | FINAL / SETTLED | W W L L |
| P-393 | Seattle Mariners @ Athletics — MLB | FINAL / SETTLED | L W L W |
| P-394 | Parramatta Eels Women vs North Queensland Cowboys Women — NRLW | FINAL / SETTLED | W W L L |
| P-395 | Belfast Wolves vs Rotterdam Dockers — European T20 Premier League | FINAL / SETTLED | W W L L |
| P-396 | Brisbane Lions vs Adelaide Crows — AFL Semi Final | FINAL / SETTLED | L L W W |
| P-397 | Cronulla-Sutherland Sharks vs North Queensland Cowboys — NRL Elimination Final | FINAL / SETTLED | L L W W |
| P-398 | Racing Santander vs Deportivo Alavés — La Liga | FINAL / SETTLED | W W L W L |
| P-399 | Genoa vs Frosinone — Serie A | FINAL / PARTIAL — C02 corners provisional (TMP-OPEN-20260914-01) | W P W L L |
| P-400 | Trinbago Knight Riders Women vs Guyana Amazon Warriors Women — WCPL | FINAL / SETTLED | W W L L |
| P-401 | IFK Göteborg vs Halmstads BK — Allsvenskan | FINAL / PARTIAL — C01, C03 corners provisional (TMP-OPEN-20260914-02/-03) | P W P L W |
| P-402 | Tottenham Hotspur vs Everton — Premier League | FINAL / SETTLED (2026-09-15: corners settled at Premier League official record; TMP-OPEN-20260914-04/-05 retired) | W W W L L |
| P-403 | Colorado Rockies @ Detroit Tigers — MLB | FINAL / SETTLED | L W L W |
| P-404 | Seattle Mariners (Bryan Woo) @ Athletics (Gage Jump) — MLB | FINAL / SETTLED | L L W W |
| P-405 | Chunichi Dragons @ Hanshin Tigers — NPB | FINAL / SETTLED | W W L L |
| P-406 | Edinburgh Castle Rockers vs Amsterdam Flames — ETPL Match 24 | FINAL / SETTLED (2026-09-16: six-over rows settled at ESPN cricket API event 1547895 — Edinburgh 68/2 after 6.0; TMP-OPEN-20260914-06 retired) | W L W L |
| P-407 | Club Brugge vs Royal Antwerp FC — Belgium Jupiler Pro League | FINAL / PARTIAL — C01 corners provisional (TMP-OPEN-20260915-01) | P W W L W |
| P-408 | Coventry City vs Brighton & Hove Albion — English Premier League | FINAL / SETTLED | L W W W W |
| P-409 | Lille OSC vs ESTAC Troyes — French Ligue 1 | FINAL / PARTIAL — C02 corners provisional (TMP-OPEN-20260915-02) | W P W W W |
| P-410 | RB Leipzig vs Hamburger SV — German Bundesliga | FINAL / PARTIAL — C05 corners provisional (TMP-OPEN-20260915-03) | W W W W P |
| P-411 | Spain (W) vs Germany (W) — FIBA Women's Basketball World Cup 2026, 3rd Place | FINAL / SETTLED | L W L W |
| P-412 | Atlanta Falcons @ Pittsburgh Steelers — NFL Regular Season Week 1 | FINAL / SETTLED | L W L W |
| P-413 | Baltimore Ravens @ Indianapolis Colts — NFL Regular Season Week 1 | FINAL / SETTLED | L L W W |
| P-414 | Buffalo Bills @ Houston Texans — NFL Regular Season Week 1 | FINAL / SETTLED | L L W W |
| P-415 | LA Angels @ Washington Nationals — MLB | ADMINISTRATIVE / NOT ISSUED (interrupted) | none issued |
| P-416 | New York Mets @ New York Yankees — MLB | FINAL / SETTLED | W L W L |
| P-417 | Chunichi Dragons @ Hanshin Tigers — NPB Central League | FINAL / SETTLED | W L W L |
| P-418 | Drukpa FC vs Royal Thimphu College (RTC) FC — Bhutan Premier League | OPEN — RESULT NOT RECOVERED (2026-09-16 re-classification): fixture listed by RSSSF Round 15 [Sep 14], unscored, page updated 11 Sep; the earlier "no Drukpa–RTC match" evidence was a BBS report dated 2026-07-17 (TMP-OPEN-20260915-04) | 5 rows issued; none graded |
| P-419 | Djurgårdens IF vs GAIS — Sweden Allsvenskan | FINAL / PARTIAL — C05 corners provisional (TMP-OPEN-20260915-05) | W W W W P |
| P-420 | Atlanta Braves @ Chicago Cubs — MLB | FINAL / SETTLED | L W L W |
| P-421 | New York Yankees @ Minnesota Twins — MLB | FINAL / SETTLED | W W L L |
| P-422 | Denver Broncos @ Kansas City Chiefs — NFL Regular Season Week 1 | FINAL / SETTLED | L W L W |
| P-423 | San Diego Padres @ Colorado Rockies — MLB | FINAL / SETTLED | L W W L |
| P-424 | Amsterdam Flames vs Dublin Guardians — ETPL 2026 Match 26 | ADMINISTRATIVE / NO SCORED TRIAL — start-crossing fail-close; no forecast issued | none issued; final Amsterdam 214/5 bt Dublin 155/9, PP 48/2 |
| P-425 | Daejeon Hana Citizen vs Kyoto Sanga — AFC Champions League Elite MD1 | FINAL / SETTLED | W L W L W; winner W; Brier 0.2416 |
| P-426 | Gamba Osaka vs Cong An Ha Noi — AFC Champions League Elite MD1 | FINAL / SETTLED | W L L L L; winner W; Brier 0.3816 |
| P-427 | Biotekno Körfez Basket vs Kolossos H Hotels — BCL Qualification Round | FINAL / SETTLED — deep Rank-#1 retro (top two both lost) | L L W W; winner L; Brier 0.3542 |
| P-428 | Edinburgh Castle Rockers vs Rotterdam Dockers — ETPL Match 27 | ADMINISTRATIVE / NO SCORED TRIAL — start-crossing fail-close; no forecast issued | none issued; final Rotterdam 181/6 bt Edinburgh 176/5, PP 54/2 |
| P-429 | Afghanistan vs India — 2nd T20I, Delhi | FINAL / SETTLED — top two both won; both XIs confirmed | W W W L; winner W; Brier 0.1635 |
| P-430 | Al Ain FC vs Al Nassr — AFC Champions League Elite MD1 | FINAL / PARTIAL — C05 corners unresolved (TMP-OPEN-20260917-01); deep Rank-#1 retro | L W W L P; winner L; 4-row Brier 0.3459 |
| P-431 | England vs Sri Lanka — 1st T20I, Southampton | FINAL / SETTLED — top two both won | W W L L; winner W; Brier 0.1925 |
| P-432 | KT Wiz @ Hanwha Eagles — KBO | FINAL / SETTLED — game ended 4–4 (terminal tie); winner label did not realise | W W L L; winner tie; Brier 0.1525 |
| P-433 | LG Twins @ NC Dinos — KBO | FINAL / SETTLED | W W L W; winner W; Brier 0.2017 |
| P-434 | Samsung Lions @ Doosan Bears — KBO | FINAL / SETTLED — all four ranked rows won | W W W W; winner L; Brier 0.0809 |
| P-435 | SSG Landers @ Lotte Giants — KBO | FINAL / SETTLED — all four ranked rows won | W W W W; winner W; Brier 0.0629 |
| P-436 | Jeonbuk Hyundai Motors vs Kashiwa Reysol — AFC Champions League Elite MD1 | FINAL / SETTLED — all five ranked rows won | W W W W W; winner L; Brier 0.0579 |
| P-437 | Port FC vs Vissel Kobe — AFC Champions League Elite MD1 | FINAL / SETTLED — all five ranked rows won | W W W W W; winner W; Brier 0.0439 |
| P-438 | Al-Wahda Abu Dhabi vs Kuwait SC — AFC Champions League Two Group A | FINAL / SETTLED — **Rank #1 LOSS; both top two lost**; deep Rank-#1 retro (diagnosis corrected from the mini log's) | L L L W L; winner W; Brier 0.5053 |
| P-439 | Al Khaldiya vs Nasaf Qarshi — AFC Champions League Two Group A | FINAL / SETTLED — all five ranked rows won (0–0) | W W W W W; winner L (draw); Brier 0.0378 |
| P-440 | Ararat-Armenia vs Sparta Praha — UEFA Europa League MD1 | FINAL / SETTLED — phase Under won, 90-minute Under lost on the same card | W W W L W; winner W; Brier 0.1590 |
| P-441 | Omonia Nicosia vs Celta Vigo — UEFA Europa League MD1 | FINAL / SETTLED — **all five ranked rows won; best card in Part 4** | W W W W W; winner L; Brier 0.0112 |
| P-442 | Chicago White Sox @ Cleveland Guardians — MLB | FINAL / SETTLED — **Rank #1 LOSS**; deep retro (middle-relief branch) | L W L W; winner W; Brier 0.3131 |
| P-443 | San Francisco Giants @ St. Louis Cardinals — MLB | FINAL / SETTLED — 10 innings; **regulation 4–4, exactly the push at L=8** | W W L L; winner L; Brier 0.1958 |
| P-444 | New York Yankees @ Minnesota Twins — MLB | FINAL / SETTLED — 13 innings; **Rank #1 LOSS; both top two lost**; deep retro (margin identity + extras) | L L W W; winner L; Brier 0.2967 |
| P-445 | Barbados Tridents vs Jamaica Kingsmen — CPL 2026 Eliminator | **FINAL / CONDITION NOT MET — all four ranked rows NO ACTION** (Jamaica bowled first; batting-first targets never activated). Process success; excluded from every cohort rate | — — — —; winner L; no Brier |
| P-446 | Atlanta Braves @ Chicago Cubs — MLB | FINAL / SETTLED | W L W L; winner W; Brier 0.2373 |
| P-447 | Boston Red Sox @ Texas Rangers — MLB | FINAL / SETTLED | W L W L; winner W; Brier 0.1903 |
| P-448 | Kansas City Royals @ Houston Astros — MLB | FINAL / SETTLED — both top two won | W W L L; winner L; Brier 0.1587 |
| P-449 | San Diego Padres @ Colorado Rockies — MLB | FINAL / SETTLED | W L L W; winner W; Brier 0.2513 |
| P-450 | Miami Marlins @ Arizona Diamondbacks — MLB | FINAL / SETTLED — both top two won | W W L L; winner L; Brier 0.1910 |
| P-451 | Dorados de Chihuahua vs El Calor de Cancún — LNBP Jornada 20 | **FINAL / BLOCKED AT ISSUE — `BK-P1 = FAIL`, no forecast issued, NOT GRADED.** Final recovered 2026-09-17(b): **Dorados 97–86** (rendered `lnbp.mx/Dorados/team_results.html`) | —; no winner issued; no Brier |

| P-452 | Cricket / Afghanistan vs India T20I Series 2026 — Afghanistan vs India, 3rd T20I | FINAL / SETTLED / RETROSPECTIVE COMPLETE | Canonical source: `PREDICTION_LOG_COMBINED_4.md` 2026-09-21 rollover import; original mini-log reasoning, source register and retrospective preserved there |
| P-453 | Baseball / MLB — Milwaukee Brewers @ Pittsburgh Pirates | FINAL / SETTLED / RETROSPECTIVE COMPLETE | Canonical source: `PREDICTION_LOG_COMBINED_4.md` 2026-09-21 rollover import; original mini-log reasoning, source register and retrospective preserved there |
| P-454 | Soccer / Denmark DBU Pokalen (Betano Pokalen) — Vejle Boldklub vs Brøndby IF | FINAL / SETTLED / RETROSPECTIVE COMPLETE | Canonical source: `PREDICTION_LOG_COMBINED_4.md` 2026-09-21 rollover import; original mini-log reasoning, source register and retrospective preserved there |
| P-455 | Baseball / MLB — Los Angeles Dodgers @ Cincinnati Reds | FINAL / SETTLED / RETROSPECTIVE COMPLETE | Canonical source: `PREDICTION_LOG_COMBINED_4.md` 2026-09-21 rollover import; original mini-log reasoning, source register and retrospective preserved there |
| P-456 | Soccer / Spain LaLiga — Real Betis vs Getafe CF | FINAL / SETTLED / RETROSPECTIVE COMPLETE | Canonical source: `PREDICTION_LOG_COMBINED_4.md` 2026-09-21 rollover import; original mini-log reasoning, source register and retrospective preserved there |
| P-457 | Cricket / Zimbabwe v Australia ODIs 2026 — Zimbabwe vs Australia, 2nd ODI | FINAL / SETTLED / RETROSPECTIVE COMPLETE | Canonical source: `PREDICTION_LOG_COMBINED_4.md` 2026-09-21 rollover import; original mini-log reasoning, source register and retrospective preserved there |
| P-458 | Baseball / NPB Central League — Chunichi Dragons @ Yomiuri Giants | FINAL / SETTLED / RETROSPECTIVE COMPLETE | Canonical source: `PREDICTION_LOG_COMBINED_4.md` 2026-09-21 rollover import; original mini-log reasoning, source register and retrospective preserved there |
| P-459 | AFL / 2026 Toyota AFL Finals Series — Sydney Swans vs Fremantle Dockers, Preliminary Final | FINAL / SETTLED / RETROSPECTIVE COMPLETE | Canonical source: `PREDICTION_LOG_COMBINED_4.md` 2026-09-21 rollover import; original mini-log reasoning, source register and retrospective preserved there |
| P-460 | Baseball / Taiwan CPBL — Rakuten Monkeys @ Fubon Guardians | FINAL / SETTLED / RETROSPECTIVE COMPLETE | Canonical source: `PREDICTION_LOG_COMBINED_4.md` 2026-09-21 rollover import; original mini-log reasoning, source register and retrospective preserved there |
| P-461 | Tennis / WTA 125 Valencia — Clara Burel vs Guiomar Maristany Zuleta De Reales, Quarterfinal | FINAL / SETTLED / RETROSPECTIVE COMPLETE | Canonical source: `PREDICTION_LOG_COMBINED_4.md` 2026-09-21 rollover import; original mini-log reasoning, source register and retrospective preserved there |
| P-462 | Soccer / Chinese Super League — Zhejiang FC vs Wuhan Three Towns | FINAL / SETTLED / RETROSPECTIVE COMPLETE | Canonical source: `PREDICTION_LOG_COMBINED_4.md` 2026-09-21 rollover import; original mini-log reasoning, source register and retrospective preserved there |
| P-463 | Baseball / MLB — Chicago Cubs @ Cincinnati Reds | FINAL / SETTLED / RETROSPECTIVE COMPLETE | Canonical source: `PREDICTION_LOG_COMBINED_4.md` 2026-09-21 rollover import; original mini-log reasoning, source register and retrospective preserved there |
| P-464 | Baseball / MLB — Milwaukee Brewers @ Baltimore Orioles | FINAL / SETTLED / RETROSPECTIVE COMPLETE | Canonical source: `PREDICTION_LOG_COMBINED_4.md` 2026-09-21 rollover import; original mini-log reasoning, source register and retrospective preserved there |
| P-465 | Basketball / WNBA — Indiana Fever @ Toronto Tempo | FINAL / SETTLED / RETROSPECTIVE COMPLETE | Canonical source: `PREDICTION_LOG_COMBINED_4.md` 2026-09-21 rollover import; original mini-log reasoning, source register and retrospective preserved there |
| P-466 | Soccer / Argentina Torneo Clausura — Racing Club vs Sarmiento | FINAL / SETTLED / RETROSPECTIVE COMPLETE | Canonical source: `PREDICTION_LOG_COMBINED_4.md` 2026-09-21 rollover import; original mini-log reasoning, source register and retrospective preserved there |
| P-467 | Baseball / MLB — Toronto Blue Jays @ Texas Rangers | FINAL / SETTLED / RETROSPECTIVE COMPLETE | Canonical source: `PREDICTION_LOG_COMBINED_4.md` 2026-09-21 rollover import; original mini-log reasoning, source register and retrospective preserved there |
| P-468 | Basketball / WNBA — Portland Fire @ Golden State Valkyries | FINAL / SETTLED / RETROSPECTIVE COMPLETE | Canonical source: `PREDICTION_LOG_COMBINED_4.md` 2026-09-21 rollover import; original mini-log reasoning, source register and retrospective preserved there |
| P-469 | Australian Rules Football / AFL Finals — Hawthorn vs Brisbane Lions | FINAL / SETTLED / RETROSPECTIVE COMPLETE | Canonical source: `PREDICTION_LOG_COMBINED_4.md` 2026-09-21 rollover import; original mini-log reasoning, source register and retrospective preserved there |
| P-470 | Baseball / NPB — Saitama Seibu Lions @ Chiba Lotte Marines | FINAL / SETTLED / RETROSPECTIVE COMPLETE | Canonical source: `PREDICTION_LOG_COMBINED_4.md` 2026-09-21 rollover import; original mini-log reasoning, source register and retrospective preserved there |
| P-471 | Basketball / Australia NBL — Melbourne United vs Adelaide 36ers | FINAL / SETTLED / RETROSPECTIVE COMPLETE | Canonical source: `PREDICTION_LOG_COMBINED_4.md` 2026-09-21 rollover import; original mini-log reasoning, source register and retrospective preserved there |
| P-472 | American Football / NCAA FBS — Coastal Carolina @ Delaware | FINAL / SETTLED / RETROSPECTIVE COMPLETE | Canonical source: `PREDICTION_LOG_COMBINED_4.md` 2026-09-21 rollover import; original mini-log reasoning, source register and retrospective preserved there |
| P-473 | Soccer / English Premier League — Nottingham Forest vs Coventry City | FINAL / SETTLED / RETROSPECTIVE COMPLETE | Canonical source: `PREDICTION_LOG_COMBINED_4.md` 2026-09-21 rollover import; original mini-log reasoning, source register and retrospective preserved there |
| P-474 | MLB — Athletics @ Cleveland Guardians | FINAL / SETTLED / RETROSPECTIVE COMPLETE | Canonical source: `PREDICTION_LOG_COMBINED_4.md` 2026-09-21 rollover import; original mini-log reasoning, source register and retrospective preserved there |
| P-475 | WNBA — Chicago Sky @ Atlanta Dream | FINAL / SETTLED / RETROSPECTIVE COMPLETE | Canonical source: `PREDICTION_LOG_COMBINED_4.md` 2026-09-21 rollover import; original mini-log reasoning, source register and retrospective preserved there |
| P-476 | MLB — Minnesota Twins @ Los Angeles Angels | FINAL / SETTLED / RETROSPECTIVE COMPLETE | Canonical source: `PREDICTION_LOG_COMBINED_4.md` 2026-09-21 rollover import; original mini-log reasoning, source register and retrospective preserved there |
| P-477 | Australia NBL — Sydney Kings vs Cairns Taipans | FINAL / SETTLED / RETROSPECTIVE COMPLETE | Canonical source: `PREDICTION_LOG_COMBINED_4.md` 2026-09-21 rollover import; original mini-log reasoning, source register and retrospective preserved there |
| P-478 | Soccer / Sweden Allsvenskan — Djurgårdens IF vs IF Elfsborg | FINAL / SETTLED / RETROSPECTIVE COMPLETE | Canonical source: `PREDICTION_LOG_COMBINED_4.md` 2026-09-21 rollover import; original mini-log reasoning, source register and retrospective preserved there |
| P-479 | Cricket / European T20 Premier League Final — Edinburgh Castle Rockers vs Belfast Wolves | FINAL / SETTLED / RETROSPECTIVE COMPLETE | Canonical source: `PREDICTION_LOG_COMBINED_4.md` 2026-09-21 rollover import; original mini-log reasoning, source register and retrospective preserved there |
| P-480 | Soccer / Denmark Superligaen — Viborg FF vs FC Nordsjælland | FINAL / SETTLED / RETROSPECTIVE COMPLETE | Canonical source: `PREDICTION_LOG_COMBINED_4.md` 2026-09-21 rollover import; original mini-log reasoning, source register and retrospective preserved there |
| P-481 | Soccer / Spain La Liga — Villarreal vs Levante | FINAL / SETTLED / RETROSPECTIVE COMPLETE | Canonical source: `PREDICTION_LOG_COMBINED_4.md` 2026-09-21 rollover import; original mini-log reasoning, source register and retrospective preserved there |
| P-482 | Cricket / CPL 2026 Final — Antigua & Barbuda Falcons vs Jamaica Kingsmen | FINAL / SETTLED / RETROSPECTIVE COMPLETE | Canonical source: PREDICTION_LOG_COMBINED_5.md; full card and review in the P-482-P-493 predecessor mini log |
| P-483 | Tennis / WTA 250 Korea Open (Seoul) R32 — Katie Volynets vs Elvina Kalieva | FINAL / SETTLED / RETROSPECTIVE COMPLETE (ENHANCED) | Canonical source: PREDICTION_LOG_COMBINED_5.md; full card and review in the P-482-P-493 predecessor mini log |
| P-484 | WNBA — Atlanta Dream @ New York Liberty | FINAL / SETTLED | Retained as actual P-484 in collision with later Padres claim; full card and review in the P-482-P-493 predecessor mini log |
| P-485 | NFL — New York Giants @ Los Angeles Rams | FINAL / SETTLED; START_CROSSED / PREGAME STATUS UNVERIFIED | Full card and review in active mini log |
| P-486 | MLB — Minnesota Twins @ San Francisco Giants | FINAL / SETTLED | Full card and review in active mini log |
| P-487 | RESERVED / ISSUE-TIME HOLD — NBL Cairns vs Tasmania source claims this ID | Noncanonical forecast under TMP-20260923-NBL-CNS-TAS; no verified original freeze time; do not reuse |
| P-488 | WTA Singapore — Vivian Wolff vs Oleksandra Oliynykova | FINAL / SETTLED | Full card and review in active mini log |
| P-489 | NPB — Chunichi Dragons @ Yokohama DeNA BayStars | UNSETTLED / ISSUE_HORIZON_UNVERIFIED | Original card plus same-event R1 retained; result state not refreshed |
| P-490 | RESERVED / UNUSED — retired provisional Padres alias | No event maps to this slot; do not reuse |
| P-491 | NPB — Orix Buffaloes @ Chiba Lotte Marines | UNSETTLED / terminal state not checked | Pregame freeze recorded around 17:54 AEST; full card carried forward in the P-494-onward mini log |
| P-492 | MLB — San Diego Padres @ Los Angeles Dodgers | FINAL / SETTLED; START_CROSSED / PREGAME STATUS UNVERIFIED | Source claim P-484 and prior provisional P-490 are aliases; one card, one canonical record |
| P-493 | KBO — Kia Tigers @ Doosan Bears | UNSETTLED / pregame freeze recorded at 19:28:29 AEST | Scheduled 19:30 AEST; terminal state not refreshed |

## Noncanonical records and retired identity aliases

| ID | Event | Status / mapping |
|---|---|---|
| TMP-20260923-NBL-CNS-TAS | Cairns Taipans vs Tasmania JackJumpers (source claims P-487) | Temporary issue-time hold; full card and status notes carried forward in the P-494-onward mini log; no canonical ID promoted and no retrospective. |
| LOCAL-GEELONG-20260904 | Geelong v Fremantle (AFL); inherited final Geelong 107-74 | Research-settled local record; never overwrite canonical P-272 Osaka-Siniakova |
| TMP-SETTLED-20260911-01 | Fenerbahce v Roma; unsupplied external P-358 no-forecast record | **RETIRED 2026-09-15(b) — merged into canonical P-374** (the genuine pregame forecast for the same event; final 1-1 re-verified at ESPN 401915444). Not scored twice. `TMP-RECON-20260912-01` retired with it |
| TMP-CANON-20260911-01 | Puerto Rico Women v China Women | RETIRED alias of canonical P-358; not another game |
| C′ `TMP-OPEN-20260915-01` | P-407-C01 (external log C′ numbering) | Same row as canonical `TMP-OPEN-20260915-01`; no separate handle (2026-09-16) |
| C′ `TMP-OPEN-20260915-02` | P-408-C01 Brighton team corners O3.5 | RETIRED alias — canonical row already settled LOSS at the Premier League record (2026-09-15(b)); no handle |
| C′ `TMP-OPEN-20260915-03` | P-409-C02 Troyes team corners O2.5 | RETIRED alias of canonical `TMP-OPEN-20260915-02` |
| C′ `TMP-OPEN-20260915-04` | P-410-C05 Leipzig team corners O4.5 | RETIRED alias of canonical `TMP-OPEN-20260915-03` |
| C′ `TMP-OPEN-20260915-05` | P-418 whole card | RETIRED alias of canonical `TMP-OPEN-20260915-04` |
| C′ `TMP-OPEN-20260915-06` | P-419-C05 total corners O7.5 | RETIRED alias of canonical `TMP-OPEN-20260915-05` |

## Primary result/derivative follow-up queue - 23 (2026-09-17(b))

**Opened and retired within the same pass, 2026-09-17(b):** `TMP-OPEN-20260917-02` — `P-451` LNBP **Jornada 20** final. The external mini log recorded `RESULT_NOT_RELIABLY_RECOVERED` and correctly warned against reusing the Jornada 19 91–89. Recovered from the field owner by escalating to the rendering rung: `lnbp.mx/Dorados/team_results.html` returns HTTP 200 with a JavaScript-only shell to a text fetch, and the per-Jornada finals when rendered — **Dorados 97, El Calor 86**. No forecast was issued on that card (`BK-P1 = FAIL`), so nothing is graded; the handle is closed as a result-recovery item only. Count unchanged at 23.

**Added 2026-09-17 (Part 4 custody):**

| Handle | Parent | Remaining item | Current disposition / next trigger |
|---|---|---|---|
| `TMP-OPEN-20260917-01` | `P-430-C05` | Al Ain team corners Over 3.5 | **Research LOSS, not booked.** The card pre-registered the AFC official match-stat record, which publishes no corner field. ESPN `soccer/afc.champions` (2 Al Ain, 10 Al Nassr) and two secondary displays agree, but ESPN was not pre-registered (§16.10(j)). Retry: an AFC field-owning statistics record, or an explicitly reconciled approved provider |

**Retired 2026-09-16:** `TMP-OPEN-20260914-06` (`P-406-C01/C04`, Edinburgh score after 6.0 overs) — settled at `SRC-ESPN-SITE-API-CRICKET` (`cricket/1547871/summary?event=1547895`, matchnote 767111 in the Edinburgh innings section): **68/2** → C01 Over 50.5 **WIN** (Brier 0.1296), C04 Under 50.5 **LOSS** (0.1296). **Retry pass 2026-09-16 on every Part-3 corner handle:** official records probed — bundesliga.com stats (raw text = zero placeholders; direct HTTP 403), allsvenskan.se match page (JS/cookie wall), plus.ligue1.com live page (empty), proleague.be 2026-27 match slug (404), Lega Serie A 2026-27 page (not found); none settles a row. Part-2 handles were not re-researched this pass.

**Retired 2026-09-15(b):** `TMP-OPEN-20260914-04`/`-05` (P-402 corners — WIN at the Premier League official record, 5+6 = 11, Tottenham 5) and `TMP-SETTLED-20260911-01` / `TMP-RECON-20260912-01` (merged into P-374).

**Retired 2026-09-15:** `TMP-OPEN-20260911-03` (`P-364` potential winner, England) — **WIN**: England 453 & 130/2 bt Pakistan 133 & 449 by 8 wickets, Edgbaston, 9–12 Sep 2026 (Day 4). Evidence and retrospective: [combined log §"2026-09-15"](PREDICTION_LOG_COMBINED_3.md).

| Handle | Parent | Remaining item | Current disposition / next trigger |
|---|---|---|---|
| `TMP-OPEN-20260915-04` | `P-418` whole card | Drukpa v RTC — result | `RESULT_NOT_RECOVERED` (re-classified 2026-09-16). RSSSF `bhutan2026.html` (last updated 11 Sep 2026) lists Round 15 "[Sep 14] Drukpa – RTC" unscored. The BBS report previously cited as "2026-09-15" is `bbs.bt/244289`, published **2026-07-17** (end of first round) — not evidence about 14 Sep. BFF's RTC 1–1 Drukpa report is the 13 Jun first-round meeting. Kickoff-time conflict (12:00 v 13:00 UTC) remains. Retry: RSSSF update, BFF match report or BBS second-round report dated on/after 14 Sep |
| `TMP-OPEN-20260915-01` | `P-407-C01` | Club Brugge team corners O4.5 | PROVISIONAL WIN (ESPN 9); Pro League record not reached — 2026-09-16: 2026-27 proleague.be match slug 404 |
| `TMP-OPEN-20260915-02` | `P-409-C02` | Troyes team corners O2.5 | PROVISIONAL WIN (ESPN 5); LFP record not reached — 2026-09-16: plus.ligue1.com `live/306887` raw text empty (JS) |
| `TMP-OPEN-20260915-03` | `P-410-C05` | RB Leipzig team corners O4.5 | PROVISIONAL WIN (ESPN 8; Guardian/StatMuse/SoccerNews 7 per external log C′ — provider split, both clear 4.5); DFL record not reached — 2026-09-16: bundesliga.com stats raw text is zero placeholders, direct 403; a WebFetch summary's "7–7" is not on the page and is excluded (`G-L13`) |
| `TMP-OPEN-20260915-05` | `P-419-C05` | Total corners O7.5 | PROVISIONAL LOSS (ESPN 2+2 = 4); Allsvenskan record not reached — 2026-09-16: allsvenskan.se page JS/cookie wall. Match disrupted: three red cards (59', 86', 90+10') |
| `TMP-OPEN-20260914-01` | `P-399-C02` | Combined corners O8.5 | PROVISIONAL WIN (ESPN 17 = 8+9; secondaries agree; 2026-09-16 Sky Sport Italia tabellino also 8–9); Serie A record not reached |
| `TMP-OPEN-20260914-02` | `P-401-C01` | Combined corners O8.5 | PROVISIONAL WIN (ESPN 17); Allsvenskan record not reached (2026-09-16: allsvenskan.se JS only) |
| `TMP-OPEN-20260914-03` | `P-401-C03` | IFK team corners O4.5 | PROVISIONAL WIN (ESPN 8) |
| `TMP-OPEN-20260912-01` | `P-377-C02` | Combined corners O8.5 | PROVISIONAL LOSS (secondary 7); ESPN `gua.1` exposes no statistics |
| `TMP-OPEN-20260911-01` | `P-368-C02` | Over 7.5 total corners | `PROVISIONAL RESEARCH WIN` (9; multiple secondary displays; independence unverified; no frozen provider). **2026-09-15:** ESPN has no UAE Pro League route (`uae.1`, `are.1`, `uae.pro_league`, `uae.league` all HTTP 400) |
| `TMP-OPEN-20260911-02` | `P-369-C01` | Under 10.5 total corners | `PROVISIONAL RESEARCH LOSS` (11; multiple secondary displays; independence unverified; no frozen provider). Same ESPN non-coverage finding |
| `TMP-OPEN-20260909-01` | `P-341-C03` | Over 7.5 total corners | `UNSETTLEABLE` to its frozen standard; ESPN `uga.1` still stale — **re-probed 2026-09-15 06:06 UTC: season 2025 ("2025-26"), 0 events on 2026-09-08, newest events 2026-05-23** |
| `TMP-OPEN-20260909-02` | `P-342-C03` | Over 8.5 total corners | `PROVISIONAL RESEARCH WIN` (16) |
| `TMP-OPEN-20260909-03` | `P-126` (appendix A) | corners + event identity | `IDENTITY_STATE_CONFLICT — UNRESOLVED` |
| `TMP-OPEN-20260909-04` | `P-148-C02` (B) | Toluca team corners | `PROVISIONAL LOSS` |
| `TMP-OPEN-20260909-05` | `P-149-C02` (C) | Ventura team corners | `PROVISIONAL WIN` |
| `TMP-OPEN-20260909-06` | `P-176-C05` (E) | Amiens/Versailles U10.5 corners | `PROVISIONAL WIN` (5–3 = 8) |
| `TMP-OPEN-20260909-07` | `P-178-C05` (F) | Cannes/Le Puy U10.5 corners | `PROVISIONAL LOSS` (8–8 = 16) |
| `TMP-OPEN-20260909-08` | `P-179-C05` (G) | Thionville/Paris 13 U10.5 corners | `PROVISIONAL WIN` (8–1 = 9) |
| `TMP-OPEN-20260909-09` | `P-233` (J) | Beijing/Lanzhou O8.5 corners | `PROVISIONAL WIN` (13) |
| `TMP-OPEN-20260909-10` | `P-234-C03` (K) | Dalian/Shenhua O8.5 corners | `PROVISIONAL WIN` (10; disrupted match) |
| `TMP-OPEN-20260909-11` | `P-235` (L) | Shandong/Shanghai Port O8.5 corners | `PROVISIONAL WIN` (14) |

Recheck live/identity first, then move on. Settle only the completed frozen field; append evidence, the why-right/why-wrong retrospective and rule disposition before retiring its handle. Never add these handles as forecast rows.

## Historical documentary/period follow-ups - 5 (2026-09-17(c))

These concern inherited settled records whose later corner adjudication could not be reproduced. They are separate from the primary open items and must not disappear under a generic settled label. **Four of the five were re-probed successfully on 2026-09-16** — full records in [`PREDICTION_LOG_COMBINED_4.md` Appendix A](PREDICTION_LOG_COMBINED_4.md).

**Reopened 2026-09-17(c):** the two earlier period-bound retirements are withdrawn; no valid lower bound on regulation corners was recovered.

| Handle | Parent | Requirement / current disposition (2026-09-17(c)) |
|---|---|---|
| TMP-AUDIT-20260912-01 | P-250-C05 | **No route.** ESPN `chn.fa`, `chn.cup`, `chn.fa_cup`, `chn.super_cup`, `chn.2` all HTTP 400 on 2026-09-16. Requirement unchanged: a China FA Cup field-owner or data-partner corner record |
| TMP-AUDIT-20260912-02 | P-251-C05 | **Reproducible now:** ESPN `ita.coppa_italia` event 401911806 gives Sassuolo 6 + Frosinone 5 = **11** — research WIN, threshold-invariant across every recovered count (10, 11, 11). Still open only for the Lega Serie A record, because ESPN was not pre-registered on the card (§16.10(j)) |
| TMP-AUDIT-20260912-05 | P-265-C05 | **Reproducible now:** ESPN `concacaf.leagues.cup` event 401914297 gives Toluca 4 + León 5 = **9** — research WIN **at exactly the threshold**, so provider-sensitive. Still open for a Leagues Cup official record |
| TMP-AUDIT-20260912-03 | P-255-C05 | UNRESOLVED_PERIOD; require regulation corner split or a sourced upper bound excluding 16+ extra-period corners from the whole-match 24. Prior WIN withdrawn. |
| TMP-AUDIT-20260912-04 | P-256-C05 | UNRESOLVED_PERIOD; require regulation corner split or a sourced upper bound excluding 7+ extra-period corners from the whole-match 15. Prior WIN withdrawn. |

## Legacy task aliases and operator-only records

| Legacy handle | Current custody |
|---|---|
| T-001 | TMP-OPEN-20260909-03 |
| T-002 | TMP-OPEN-20260909-04 |
| T-003 | TMP-OPEN-20260909-05 |
| T-004 | P-166 research settled; operator-only |
| T-005 | TMP-OPEN-20260909-06 |
| T-006 | TMP-OPEN-20260909-07 |
| T-007 | TMP-OPEN-20260909-08 |
| T-008 | P-200 research settled; operator-only |
| T-009 | P-217 research settled; operator-only |
| T-010 | TMP-OPEN-20260909-09 |
| T-011 | TMP-OPEN-20260909-10 |
| T-012 | TMP-OPEN-20260909-11 |
| T-013 | P-274 research settled; operator-only |

TMP-OPEN-20260910-01/-02/-03 are retired: P-345-C03, P-346-C05 and P-355-C05 were settled in the prior September 11 import at their frozen field owners. P-366-C02/C03 are terminal censored. The four operator-only rows require an actual ticket/definition if operator settlement is later requested; no sporting-result search can reconstruct those terms.

Latest live-state reference: [Cricbuzz](https://www.cricbuzz.com/live-cricket-scores/129596/pak-vs-eng-3rd-test-pakistan-tour-of-england-2026), checked 2026-09-11 23:43 UTC. Stumps is not final. **Superseded 2026-09-15 06:06 UTC:** [ESPNcricinfo full scorecard](https://www.espncricinfo.com/series/pakistan-tour-in-england-2026-1496563/england-vs-pakistan-3rd-test-1496584/full-scorecard) (opened via r.jina.ai; direct route HTTP 403) reads "England won by 8 wickets … day 4 - England 2nd innings 130/2 (24.2 ov) - end of match". No event in any queue is live.
