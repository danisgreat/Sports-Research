# Prediction Mini Running Log — P-495 onward (started 2026-09-23)

| Field | Value |
|---|---|
| Created | 2026-09-23 21:45:00 +10:00 (Australia/Melbourne, AEST UTC+10; AEDT from 4 Oct 2026) |
| Status | **ACTIVE MINI LOG.** P-495 and P-496 issued. |
| Next canonical ID | **P-497**, advanced after P-496 issue. |
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

**Settlement routes (for the next pass).**
- **TMP-G25:** NPB box `npb.jp/scores/2026/0923/db-d-25/box.html` (試合終了) + Sports Navi `baseball.yahoo.co.jp/npb/schedule/?date=2026-09-23` + Kyodo or Nikkan (Yahoo! News). Grade the **23 Sep game-25** final. NPB 12-inning cap applies: a tie is a terminal outcome, so DeNA ML is a non-win on a tie and Chunichi +1.5 wins on a tie.
- **P-493:** KBO English scoreboard `eng.koreabaseball.com/Schedule/Scoreboard.aspx?searchDate=2026-09-23` ("KIA x FINAL y DOOSAN") + an independent Korean outlet (e.g., Yonhap or Sports Chosun) + a third lineage. KBO regular-season tie after 11 innings.
- **P-494:** WTA feed `api.wtatennis.com/tennis/tournaments/1152/2026/matches/` (`MatchState "F"`, `ResultString`) + ESPN `site.api.espn.com/apis/site/v2/sports/tennis/wta/scoreboard` (competition 184095; request without a browser User-Agent) + Tennis.com or another independent lineage. Games = sum of set games; a tiebreak set = 13. Record any retirement with its score.
- **P-495:** WTA official event/match center (`wtatennis.com`, Delta Motors Tolentino Open 2026) + TennisTemple/tournament linescore (`tennistemple.com`) + Sofascore (`sofascore.com`). Minimum three lineages with terminal marker `MatchState "F"`. Games = sum of set games (tiebreak set = 13). Any mid-match retirement records exact game scores at stoppage.
- **P-496:** ITF World Tennis Tour match center (`itftennis.com`, M25 Falun 2026, Men's Singles R16) + TennisTemple match card (`tennistemple.com`) + Sofascore (`sofascore.com`). Minimum three lineages with terminal marker `MatchState "F"` / final match score. Games = sum of set games (a tiebreak set = 13). Any mid-match retirement records exact game scores at stoppage.

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
