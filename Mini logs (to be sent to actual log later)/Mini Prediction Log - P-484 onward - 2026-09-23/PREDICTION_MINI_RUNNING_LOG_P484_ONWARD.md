# Prediction Mini Running Log - P-484 onward

**Created:** 2026-09-23 (Australia/Sydney)  
**Canonical authority:** `PREDICTION_LOG_COMBINED_5.md`, whose current top snapshot lists P-483 as highest and P-484 as next.  
**Existing local claim:** P-484 is the Padres card preserved in this file; it is not imported into the canonical combined log.  
**Next ID:** FROZEN pending reconciliation of the P-484 collision and the supplied P-485/P-486/P-488/P-489 claims.  
**Performance status:** LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE.  
**Operating mode:** SPORTS_ONLY / MARKET_BLIND.  
**Retrospective:** Attached completed cards audited below on 2026-09-23; the Padres card remains live and unsettled.

## 1. Incomplete / Unsettled Logs

### P-484 - MLB - San Diego Padres @ Los Angeles Dodgers

| Field | Preserved / current state |
|---|---|
| Scheduled start | 2026-09-22 19:10 PDT = 2026-09-23 12:10 AEST, Dodger Stadium |
| Supplied ID | P-484. At initial entry creation, the current Part 5 snapshot listed P-484 as next. A later supplied WNBA card also claims P-484; collision recorded below. Preserve both claims until reconciliation. |
| Supplied rank #1 | Michael King 15+ pitching outs / Over 14.5 outs |
| Supplied rank #2 | Padres +1.5 runs |
| Supplied rank #3 | Dodgers moneyline |
| Supplied rank #4 | Combined runs Over 8.5 |
| Projected winner in supplied card | Los Angeles Dodgers, narrow lean |
| Original issue-time statement | The author reported a final verification at 12:13 AEST, after the 12:10 AEST scheduled start, and reported using no live scoring information. The actual first-pitch time and a before-start freeze are not independently established here. |
| State check at log creation | MLB Stats API event 823897 reported `In Progress` / `Live` at 2026-09-23 03:20:28 UTC. This check is for status only and was not used to revise the supplied picks. |
| Current settlement status | LIVE / UNSETTLED. Latest official MLB Stats API response: In Progress, Padres 0 – Dodgers 5, bottom of the 5th; feed metadata 20260923_034355. No pick grade or retrospective entered. |
| Forecast integrity | START_CROSSED / PREGAME STATUS UNVERIFIED. Under `METHOD.md` section 3, step 3 and `RULES_GENERAL.md` start-crossing control, these supplied ranks cannot be presented as a valid current pregame forecast or reissued as live picks. Preserve for audit; assess issuance status at canonical import. |
| Operator terms | No operator, odds, action/void terms or offer-time confirmation supplied. NO VALUE DETERMINABLE. |
| Event cluster / official record | MLB gamePk 823897; official status route: https://statsapi.mlb.com/api/v1.1/game/823897/feed/live |

**Document mapping:** Import or administrative disposition belongs in `PREDICTION_LOG_COMBINED_5.md`; the start-crossing/provenance finding belongs with that entry and, if a recurring process issue is established, `LEARNING_REGISTER.md`. Baseball-specific evidence would map to `RULES_BASEBALL.md` only after a supported retrospective. No rule or source-register change is inferred from this one card.

**Source status:** The full as-supplied research and its material source list are preserved below. Those claims and source timestamps were not independently revalidated for this logging task. The separate official MLB API status check above does not change the original research basis.

#### Original supplied research card (selection and reasoning preserved as received)

## SD Padres @ LA Dodgers — pregame research card

**Scheduled:** Tuesday, 22 September 2026, 7:10 PM PDT at Dodger Stadium = **Wednesday, 23 September 2026, 12:10 PM AEST**. My final verification crossed the scheduled start by a few minutes. At **12:13 PM AEST**, the official MLB page I could retrieve was still displaying the matchup as a preview rather than supplying a live state. **No live score, live play, or result has been used to form these picks.** ([MLB.com][1])

I used the Sports Research Drive **read-only**, including `RULES_BASEBALL.md`, `METHOD.md`, `RULES_GENERAL.md`, `UPCOMING_GAME_RESEARCH_GUIDE.md`, `DATA_SOURCE_REGISTER.md`, and today's `IMPLEMENTED_CHANGES_2026_09_23.md`. The latest Drive implementation identifies **P-484 as the next canonical prediction ID**, so this card is logged below as **P-484**. Nothing in Drive was edited.

### Best 4 picks

| Rank   | Pick                                                | Assessment                                 |
| ------ | --------------------------------------------------- | ------------------------------------------ |
| **#1** | **Michael King 15+ pitching outs / Over 14.5 outs** | **Strongest selection**                    |
| **#2** | **Padres +1.5 runs**                                | **Strong**                                 |
| **#3** | **Dodgers ML**                                      | **Moderate**                               |
| **#4** | **Combined Total Over 8.5 runs**                    | **Moderate-low; materially more volatile** |

**Potential game winner: LA Dodgers, narrowly.**

I am **not** recommending Under 8.5 as a second totals pick. That would amount to mechanically covering both sides of the same total, which the Drive methodology specifically rejects.

---

# 1. Michael King 15+ pitching outs — Pick #1

This is the cleanest exposure on the card.

King is officially listed by MLB for San Diego at **12-9, 3.03 ERA, 154 strikeouts and 1.16 WHIP**. More importantly for an outs market, his recent workload has been extremely stable: his last five starts were **7.0, 6.0, 6.0, 7.0 and 6.0 innings**, so he cleared 15 outs in all five and recorded **32 innings total**. He had a 1.41 ERA over those starts. ([MLB.com][2])

There is also no strong evidence of a planned abbreviated outing. San Diego deliberately moved King up to this Tuesday start on **normal rest**, specifically so he would remain lined up for the regular-season finale if needed. Manager Craig Stammen described him as their preferred pitcher for a possible must-win finale. That rotation decision is much more consistent with a normal starter workload than a tune-up restriction. ([MLB.com][3])

There is one important caution: his run prevention has been better than some underlying contact metrics. Statcast has King at a **3.00 ERA but 4.36 xERA**, with a .321 xwOBA allowed in 2026. That prevents me from treating his 1.41 recent ERA as a sustainable true-talent number against this Dodgers lineup. But that concern affects **runs allowed much more than it affects his likelihood of reaching the fifth inning**. ([baseballsavant.com][4])

**Why #1:** this market asks King to remain in the game for five innings, not to completely suppress Los Angeles. His current role, rotation scheduling and five-start workload distribution support that better than any side or total on this card.

---

# 2. Padres +1.5 — Pick #2

Of your originally supplied markets, **this is my strongest**.

The Dodgers have the superior season résumé: **96-60, +193 run differential and 50-28 at home**, versus San Diego at **87-69, +41 and 38-40 away**. But a +1.5 line does not require San Diego to be the better team. It wins if San Diego wins outright **or loses by exactly one run**. ([MLB.com][5])

There are three mechanisms supporting that cushion:

**King materially compresses Los Angeles' early-game scoring distribution.** Even after accounting for the xERA warning, he has been pitching deep and effectively. His most recent five starts included just **five earned runs in 32 innings**. ([StatMuse][6])

**San Diego enters with unusually strong offensive form.** The Padres have scored **40 runs in their last five** and **71 in their last 10**. I am deliberately shrinking that signal because much of the most explosive production came against Colorado and Miami, but it still tells us this is not a cold lineup merely hoping King keeps the game close. ([StatMuse][7])

**Los Angeles has a non-standard pitching sequence.** Same-day reporting identified Brock Stewart as the opener, with the Dodgers working through a broader pitching plan rather than using a conventional full-length starter. Stewart himself has pitched very well, so “bullpen game = Padres advantage” would be an analytical mistake. Statcast shows Stewart allowing just a **.245 xwOBA**, .184 xBA and .301 xSLG in the current dataset. But every transition creates another branch for inherited runners, matchup changes and an arm having an off night. ([baseballsavant.com][8])

The Drive's required +1.5 decomposition is therefore:

* **Padres win:** meaningful branch because of King plus current offense.
* **Padres lose by one:** also substantial, particularly in a competitive game where LA has last-bat advantage.
* **Padres lose by 2+:** very real because Los Angeles' lineup has significant late separation and home-run capacity.

The first two branches together are why **+1.5 ranks well above Padres ML** and above Dodgers ML.

---

# 3. Dodgers ML — Pick #3

This might initially look inconsistent with Padres +1.5, but it is not. A **Dodgers one-run win cashes both**. That is exactly why the run-line cushion ranks above the outright winner.

My narrow winner lean remains Los Angeles because its **full-season centre is substantially stronger**:

* 96-60 versus 87-69.
* +193 run differential versus +41.
* 50-28 at Dodger Stadium.
* 780 season runs versus 690 for San Diego.
* 587 runs allowed versus 649 for San Diego. ([MLB.com][5])

The Dodgers' current offense is also running above its season baseline. They have scored **52 runs over their last 10** and **116 over their last 20**. ([StatMuse][9])

The lineup context remains strong despite **Shohei Ohtani being unavailable for this game**. MLB placed Ohtani on the IL with left-knee and right-biceps issues, with Wednesday identified as the earliest realistic activation point. ([MLB.com][10])

The same-day Dodgers order reported before the game was:

**Betts, Freeman, Will Smith, Muncy, Kyle Tucker, Teoscar Hernández, Josue De Paula, Andy Pages, Tommy Edman.** Pages had just returned from the injured list. ([Dodgers Nation][11])

Tucker is particularly relevant: MLB's own preview noted he entered this game **15-for-35 with five home runs over his previous 10 games**. ([MLB.com][12])

So why isn't Dodgers ML higher? **Michael King.** He meaningfully reduces the normal Dodgers offensive edge, while San Diego's current lineup is hot enough to challenge LA's pitching plan.

**Winner projection: Dodgers, but closer to a one-run game than a comfortable multi-run separation in my central scenario.**

---

# 4. Over 8.5 runs — Pick #4

This is the weakest of my four recommendations because the total has competing high-quality signals.

### Over mechanisms

San Diego's offense has produced **8.0 runs/game over its latest five** and 7.1 over the latest 10, although that must be heavily shrunk toward its season baseline because of opponent quality. ([StatMuse][7])

Los Angeles has scored **5.2/game over its latest 10** and 116 over its latest 20. Its lineup also has multiple extra-base/HR threats even without Ohtani. ([StatMuse][9])

San Diego has allowed **47 runs over its last 10 games**, so King leaving the game does not automatically eliminate the Dodgers' late scoring pathways. ([StatMuse][13])

And the Stewart/opener configuration introduces the Drive's mandatory **relief-transition and joint upper-tail branches**. Stewart can pitch well and the game can still become high scoring after he exits.

### Under mechanisms

There is equally legitimate suppression evidence. King has the 1.41 ERA across his latest five starts, and the Dodgers as a staff have surrendered only **28 runs over their latest 10 games**. ([StatMuse][6])

Stewart himself has not been weak: Baseball Savant's current data shows excellent expected-contact outcomes against him. ([baseballsavant.com][8])

Ohtani's absence lowers LA's offensive ceiling.

Weather also does **not** give me a strong reason to inflate the total. Conditions around game time were approximately **21°C/71°F and clear**, without a rain concern or an extreme temperature environment. That is broadly neutral compared with a genuinely strong wind/heat total signal.

### Totals verdict

I still put **Over 8.5 narrowly above Under 8.5**, principally because the number requires nine runs and there are several plausible cluster pathways through both offenses and the Dodgers' multi-pitcher structure.

But the evidence separation is **not large enough** for me to rank it ahead of the side markets.

---

## Important starter/lineup integrity note

There is a source-timing discrepancy that I am not going to conceal.

During my final official MLB retrieval, MLB's probable-pitcher and lineup pages **still showed the Dodgers starter as TBD and both batting orders as awaiting confirmation**, even though multiple same-day sources were already identifying **Brock Stewart as the opener** and publishing the Dodgers batting order. ([MLB.com][14])

Accordingly:

* **Michael King:** `CONFIRMED/PROBABLE_OFFICIAL` from MLB.
* **Brock Stewart opener:** strong same-day evidence, but the specific official MLB page I captured had not propagated the update.
* **Dodgers order:** strongly same-day supported, but the captured MLB lineup endpoint remained stale.
* **Padres order:** a same-day game-data feed showed Tatis, Harris, Machado, France, Merrill, Hays, Bogaerts, Campusano and Cronenworth, but the MLB endpoint I captured still said “awaiting starting lineup.” I therefore did **not** use exact Padres batting-order placement as a high-weight model input. ([Reddit][15])

This uncertainty is one reason I have not attached numerical win probabilities to the picks.

---

## Compact data audit

| Variable                 |                   Padres |                          Dodgers |
| ------------------------ | -----------------------: | -------------------------------: |
| Record                   |                    87-69 |                            96-60 |
| Run differential         |                      +41 |                             +193 |
| Home/Away relevant split |               38-40 away |                       50-28 home |
| L5 offense               |              **40 runs** |                      **31 runs** |
| L10 offense              |              **71 runs** |                      **52 runs** |
| L20 offense              | Fresh aggregate not used |                     **116 runs** |
| L10 runs allowed         |                   **47** |                           **28** |
| Starter/primary arm      |     King, established SP | Stewart opener / relief sequence |
| Major lineup absence     |                        — |                           Ohtani |

The important interpretation is that **recent scoring alone would massively overrate San Diego**. Their 2026 full-season run differential and road record remain well below Los Angeles, so the recent offensive surge was treated as a form modifier rather than the base rate. ([MLB.com][5])

---

# Final card

**1. Michael King 15+ pitching outs / Over 14.5 outs**
**2. Padres +1.5**
**3. Dodgers ML**
**4. Over 8.5 combined runs**

**Potential winner: LA Dodgers**

**Original-market preference:**
**Padres +1.5 > Dodgers ML > Over 8.5 > Under 8.5**

Under 8.5 is the rejected side rather than an additional recommendation.

---

## Sources used

**Drive methodology, read-only:** `RULES_BASEBALL.md`; `METHOD.md`; `RULES_GENERAL.md`; `UPCOMING_GAME_RESEARCH_GUIDE.md`; `DATA_SOURCE_REGISTER.md`; `SOURCES.md`; `IMPLEMENTED_CHANGES_2026_09_23.md`.

**Primary / statistical:** MLB official standings and team pages for schedule, records and season run differential; MLB Michael King/player and Padres reporting; MLB transactions/injury reporting; MLB/Statcast Baseball Savant for King, Stewart, Sasaki and hitter expected-contact metrics; StatMuse for current L5/L10/L20 team windows and King's recent starts; same-day Los Angeles weather data. ([MLB.com][5])

**Secondary late-information sources:** same-day Dodgers lineup reporting and a game-feed cross-check were used only where the official MLB cached endpoint had not yet propagated the lineup/starter update. ([Dodgers Nation][11])

**Excluded:** sportsbook odds, betting previews and fantasy projections were **not used** to form or rank the selections.

---

[1]: https://www.mlb.com/dodgers/scores/2026-09-22?utm_source=chatgpt.com "Dodgers Scores: Scoreboard, Results and Highlights | Los Angeles Dodgers"
[2]: https://www.mlb.com/dodgers?msockid=26ec392d182969bd397b2f93198768a4&utm_source=chatgpt.com "Official Los Angeles Dodgers Website | MLB.com"
[3]: https://www.mlb.com/padres/news/michael-king-moved-up-in-line-to-start-padres-season-finale?utm_source=chatgpt.com "Michael King moved up, in line to start Padres' season finale"
[4]: https://baseballsavant.mlb.com/savant-player/michael-king-650633?season=2023&utm_source=chatgpt.com "Michael King Stats: Statcast, Visuals & Advanced Metrics | baseballsavant.com"
[5]: https://www.mlb.com/dodgers/standings/?msockid=2e4d9e7fe67b69cc1cb08840e7fa68f9&utm_source=chatgpt.com "2026 Dodgers Standings and Record: Regular Season | Los Angeles Dodgers"
[6]: https://www.statmuse.com/mlb/ask/michael-king-last-5-games-pitching?utm_source=chatgpt.com "Michael King Last 5 Games Pitching | StatMuse"
[7]: https://www.statmuse.com/mlb/ask/padres-runs-last-5-games?utm_source=chatgpt.com "Padres Runs Last 5 Games | StatMuse"
[8]: https://baseballsavant.mlb.com/team/119?utm_source=chatgpt.com "Los Angeles Dodgers Statcast, Visuals & Advanced Metrics | MLB.com | baseballsavant.com"
[9]: https://www.statmuse.com/mlb/ask/dodgers-runs-per-game-this-season-last-10-games?utm_source=chatgpt.com "Dodgers Runs Per Game This Season Last 10 Games | StatMuse"
[10]: https://www.mlb.com/dodgers/news/shohei-ohtani-out-of-lineup-again-vs-reds?partnerId=it-20260912-19785433-mlb-1-A&utm_source=chatgpt.com "Shohei Ohtani placed on injured list with knee, biceps injuries"
[11]: https://dodgersnation.com/dodgers-lineup-vs-padres-andy-pages-roki-sasaki-are-back/2026/09/22/?utm_source=chatgpt.com "Dodgers Lineup vs. Padres: Andy Pages, Roki Sasaki Are Back"
[12]: https://www.mlb.com/stories/game-preview/823897?utm_source=chatgpt.com "San Diego Padres at Los Angeles Dodgers Preview - 09/22/2026 - MLB Stories"
[13]: https://www.statmuse.com/mlb/ask/padres-runs-allowed-last-10-games?utm_source=chatgpt.com "Padres Runs Allowed Last 10 Games | StatMuse"
[14]: https://www.mlb.com/dodgers/roster/starting-lineups/2026-09-22?utm_source=chatgpt.com "MLB Starting Lineups Today | Los Angeles Dodgers"
[15]: https://www.reddit.com/r/mlb/comments/1wnrtu9/game_thread_1010pm_edt_san_diego_padres_8769_at/?utm_source=chatgpt.com "[Game Thread | 10:10PM EDT] | San Diego Padres [87-69] at Los Angeles Dodgers [96-60]"


### TMP-20260923-NPB-CHU-DB — Chunichi Dragons @ Yokohama DeNA BayStars (claimed P-489; unsettled)

| Field | Current audit |
|---|---|
| Card as supplied | Four-ranked forecast: Under 6.5 (~62%); DeNA moneyline (~60%); Chunichi +1.5 (~57%); Over 6.5 (~38%). Potential winner DeNA (~60%); representative score DeNA 3–2. Probabilities are marked unvalidated subjective. |
| Event status | UPCOMING at the latest check. The official NPB box score for 23 September 2026 says pre-game and schedules first pitch for 18:00 JST. At the recorded check time, that start was still in the future. |
| Issue-time integrity | The card says its final refresh was just after the corrected scheduled start. That conflicts with the official page still showing pre-game at the latest check. Exact issue time and whether the card was frozen before play are unresolved. Keep ISSUE_HORIZON_UNVERIFIED; do not treat the current pre-game status as proof of the card’s issue time. |
| Settlement | NOT SETTLED. No result, ranking score or retrospective until an official terminal result is available and the three-lineage gate passes. |
| Original card | Preserved unchanged at C:\Users\danie\.codex\attachments\8d873c0b-ccec-4784-961e-5cbca169cc34\Pasted text.txt. |

#### User-requested fresh-line reforecast R1 — frozen 2026-09-23 18:59:17 AEST (pre-start)

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

### TMP-20260923-NPB-BUF-MAR — Orix Buffaloes @ Chiba Lotte Marines (unsettled)

| Field | Current audit / pregame record |
|---|---|
| Matchup & Schedule | Orix Buffaloes (Away) @ Chiba Lotte Marines (Home), NPB Pacific League (Game 25 of season series). Scheduled: 23 September 2026, 17:00 JST = 18:00 AEST, ZOZO Marine Stadium, Chiba. |
| Starting Pitchers | Aren Kuri (ORX, RHP, #22, 25 GS, 8-11, 150.2 IP, 3.35 ERA) vs Joey Lucchesi (LOT, LHP, #48, 3 GS, 1-1, 15.0 IP, 4.20 ERA). |
| Card as supplied | Four-ranked forecast: #1 Buffaloes +1.5; #2 Combined Total Under 7.0 Runs; #3 Marines ML; #4 Combined Total Over 7.0 Runs. Potential winner: Orix Buffaloes (lean, representative score Orix 4 – Lotte 3). |
| Event status | UPCOMING / PRE-GAME at issuance verification. Official NPB fixture lists first pitch at 17:00 JST (18:00 AEST). No live score, in-game play, or outcome data used. |
| Issue-time integrity | Research frozen around scheduled start (18:00 AEST); pregame conditions, starting pitchers, and season metrics verified. |
| Settlement | NOT SETTLED / AWAITING TERMINAL RESULT. Retain all picks unchanged until official final box score. |
| Key Rationale | Buffaloes +1.5 decomposes into outright win + 1-run loss, covering majority of score distribution. Kuri (3.35 ERA, 6.0 IP scoreless on 9/16 vs HAWKS) offers proven length; Lucchesi (3 starts in NPB) faces Orix for second time in 17 days. Game total 7.0 favors Under due to ZOZO Marine coastal air/park suppression, overcast 25°C autumn weather, and low-run baselines (ORX 3.47, LOT 3.52 RF/G). |

Event identity/status source: [NPB official scores](https://npb.jp/scores/2026/0923/). This event stays in Incomplete / Unsettled Logs.


## 2. Temporary-ID / Canonical-ID Conflict Logs

The current Part 5 file snapshot ends at P-483 and labels P-484 as next. This local mini log already contains a distinct Padres card claiming P-484, now verified live. The attached WNBA card also claims P-484. I preserve the existing local Padres record and use a temporary audit ID for the WNBA card. The other supplied cards claim P-485, P-486, P-488 and P-489, but those are not registered in the current canonical file and P-487 is absent from the supplied set. Do not infer that the gap is free or import these numbers yet. The completed cards still receive full result reviews here.

### TMP-20260923-WNBA-ATL-NYL — Atlanta Dream @ New York Liberty (card claims P-484)

**Original card and forecast preserved:** C:\Users\danie\.codex\attachments\7526db47-c50c-4fbf-91ec-69820861257e\Pasted text.txt. The card reports a near-tip refresh and that the WNBA event page still showed Upcoming. Its numerical probabilities were explicitly unvalidated subjective estimates; the forecast did not include odds.

**Final result:** Atlanta Dream 95, New York Liberty 84; total 179. The WNBA event page confirms the fixture identity; the Atlanta and Liberty recaps, AP recap and CBS Atlanta report agree on the result. The AP report records the 41–38 halftime score, Atlanta’s 73–62 lead after three, and says New York played in Toronto the day before. Atlanta scored 32 in the third quarter; New York did not get closer than eight in the fourth. [Atlanta recap](https://dream.wnba.com/news/balanced-attack-propels-dream-to-important-road-win), [Liberty recap](https://liberty.wnba.com/news/liberty-fall-to-dream-95-84), [AP recap](https://www.foxsports.com/articles/wnba/atlanta-dream-beat-the-new-york-liberty-9584-close-in-on-a-top4-wnba-seed), [CBS Atlanta report](https://www.cbsnews.com/atlanta/news/jordin-canada-scores-19-andel-reese-records-another-double-double-as-dream-beat-liberty-95-84/).

| Original rank | As-issued selection | Result | Settlement |
|---|---|---|---|
| #1 | Under 177.5 | 179 points | LOSS by 1.5 |
| #2 | Atlanta Dream -1.5 | Atlanta by 11 | WIN |
| #3 | New York Liberty +1.5 | Atlanta by 11 | LOSS |
| #4 | Over 177.5 | 179 points | WIN |
| Winner | Atlanta Dream, ~58% | Atlanta won | CORRECT |

**Decision and ranking diagnostics:** Two distinct decisions were offered: Atlanta -1.5 won; the preferred total Under lost (1/2). Rank-1 loss: YES. Hit@2: YES. Wins@2: 1/2. Standard binary NDCG@2: 0.387. TOP_OU_REVIEW: YES; the highest-ranked total was Under and did not win. The Under and Over rows are one forced binary total decision, not two independent successes/failures. Metrics are descriptive only.

**Pick-by-pick review.**

- **#1 Under 177.5 — loss.** The pregame centre was 176.7, only 0.8 below the line, and the card correctly labelled the edge low confidence. The game finished 179, a small miss in a near-line scoring distribution rather than a large centre error. Atlanta’s 32-point third quarter was the decisive scoring burst: the Dream reached 73 while New York reached 62 entering the fourth. Atlanta’s balanced scoring and turnover pressure supported its offense; the CBS account records 11 New York turnovers converted into 14 Atlanta points and only four Dream turnovers. The forecast had already listed transition possessions, Reese’s offensive boards, late fouling and overtime as Under kill paths. No overtime occurred. The specific pace and possession count were not recovered here, so the review attributes the miss to the documented third-quarter scoring cluster, not to an unverified claim that the whole game was unusually fast.
- **#2 Atlanta -1.5 — win.** The card’s read of Atlanta’s stronger season profile, defensive pressure, rebounding and rest position was directionally right. The margin was much larger than the central estimate of about +2.4. Canada scored 19, Reese 18, Bonner 17 off the bench, Howard 16 and Gray 14. The game recap says five Dream players reached double figures and Atlanta pulled away after halftime. The pregame report did not have an authoritative same-day starting five for both teams, so this win does not validate its unconfirmed rotation assumptions.
- **#3 New York +1.5 — loss.** The Liberty’s home-defense and star-core path did not keep the game within one possession late. Stewart led New York with 27 and Jones had 18, but Atlanta’s third-quarter run created an 11-point final margin. The central concern in the card was that New York could hold Atlanta near the mid-80s; the Dream scored 95. New York’s major absences were identified before the game, but the report lacked a final confirmed lineup.
- **#4 Over 177.5 — win.** The total crossed the number by 1.5. This is the complement of the losing Under and supplies no independent second total result.
- **Projected winner — Atlanta — correct.** The winner call survived even though the score margin was far larger than the central score. As the card itself observed, an outright win and a -1.5 cover are separate outcomes.

**Rank-1 and top-two review.** Under was ranked first because the estimated total centre sat below the threshold and the card cited both teams’ defense, an 80–81 possession baseline and New York’s back-to-back. That was internally coherent, but the advantage over Atlanta -1.5 was negligible: Under was ~54%, while the spread was ~53–54%. With the total centre only 0.8 below the line, there was no robust basis for a stable ordinal distinction. On frozen pregame information, the card did disclose the principal scoring failure branches and kept confidence low. The actual result alone does not justify moving Atlanta -1.5 above Under in future cards. A useful improvement is to show ranking uncertainty when estimated probabilities overlap at this precision. Exactly one of the top two won; they did not both win.

**Total-market review.** The total miss was narrow and the predicted total centre was close. The report included pace, defense, rest, prior matchup and several scoring tails, but lacked a verified game-day lineup and a quantified transition/turnover scoring component. The third-quarter burst was a realized high-scoring branch. This is one game and does not support a permanent basketball-total adjustment. Preserve the low-confidence label; next time obtain same-day active players and starters, then disclose a score/pace distribution around the line rather than letting a 0.8-point centre gap look rank-determinative.

**Validation and source audit.**

| Required question | Finding |
|---|---|
| Both confirmed starting lineups obtained before issue? | No. The card explicitly says it only had each team’s latest prior-game five and could not verify tonight’s authoritative starting fives. |
| Bench/reserve or rotation information? | Not sufficiently. The report discussed team rebounding and rotation context but did not confirm expected game-day reserve roles. Postgame CBS reports Bonner scored 17 off the bench; that is outcome evidence, not pregame knowledge. |
| Coaching information? | No game-specific tactical plan is established in the forecast. Atlanta coach Karl Smesko later described broad contribution and second-half execution; do not convert the postgame quote into a pregame assumption. |
| Injuries/availability adequately checked? | Partly. The card identified Brionna Jones as out for the season and Sabally’s long-term absence, but day-of starters were not confirmed. |
| Original sources accurate/current? | Event and result sources are clear. The forecast attachment’s inline content-reference tokens are not usable URLs, which limits independent review of its underlying inputs and timestamps. |
| Better future sources? | Prefer the WNBA game-day lineup/box score, official team availability reports, and a distinct independent recap for result verification. Do not count multiple pages backed by the same feed as independent lineages. |
| Meaningful blind spots? | Yes: unconfirmed lineup, a near-line total, unmeasured game-day rotation and the chance that turnover pressure creates efficient extra offense rather than merely lower opponent scoring. |
| Future treatment | Keep missing lineup status explicit, widen uncertainty, and calculate turnovers-to-transition points alongside pace and half-court efficiency. |

**Learning status:** WNBA Rank-1 and top-total failure scrutiny is complete. Event-specific observation: the Under’s small central edge was not robust to a one-quarter offensive burst, while Atlanta’s side case benefited from distributed scoring. No permanent rule change from one game.

### TMP-20260923-NFL-NYG-LAR — New York Giants @ Los Angeles Rams (card claims P-485)

**Original card preserved:** C:\Users\danie\.codex\attachments\316c1cf1-1085-4205-914d-32b02772d84a\Pasted text.txt. It ranks Giants +6.5 at ~61%, Under 47.5 at ~54%, Over at ~46%, Rams -6.5 at ~39%, and projects the Rams to win ~64%, with a representative score of 24–20. The estimates are explicitly unvalidated subjective.

**Event result and timing gate:** NFL Game Center confirms Final, Rams 28–6, with the Rams scoring seven in every quarter and the Giants scoring only six total. NFL, Rams and Giants reports agree on the event and result. [NFL Game Center](https://www.nfl.com/games/giants-at-rams-2026-reg-2), [Rams recap](https://www.therams.com/news/game-recap-rams-defeat-giants-28-6-on-monday-night-football), [Giants recap](https://www.giants.com/news/instant-analysis-giants-fall-to-rams-28-6), [AP report via WRAL](https://www.wral.com/news/ap/c991e-giants-qb-jaxson-dart-exits-with-knee-injury-on-first-series-vs-rams/), [Los Angeles Times report](https://www.latimes.com/sports/rams/story/2026-09-21-rams-defeat-giants-aaron-donald-return). Three result lineages are NFL, Associated Press and Los Angeles Times. However, the card says “final pre-kickoff” while also reporting the game at Q1 15:00. A 15:00 first-quarter clock means kickoff has occurred. No score at that instant does not prove a pregame freeze. Mark START_CROSSED / PREGAME STATUS UNVERIFIED; this result is for learning and cannot enter a valid pregame performance sample.

| Original rank | As-issued selection | Result | Settlement |
|---|---|---|---|
| #1 | Giants +6.5 | Lost by 22 | LOSS |
| #2 | Under 47.5 | Total 34 | WIN |
| #3 | Over 47.5 | Total 34 | LOSS |
| #4 | Rams -6.5 | Rams won by 22 | WIN |
| Winner | Rams, ~64% | Rams won | CORRECT |

**Decision and ranking diagnostics:** Two distinct decisions: Giants +6.5 lost; preferred Under 47.5 won (1/2). Rank-1 loss: YES. Hit@2: YES. Wins@2: 1/2. Standard binary NDCG@2: 0.387. TOP_OU_REVIEW: NO; the highest-ranked total was Under at rank #2 and it won. Descriptive learning only, with issue horizon unverified.

**Pick-by-pick review.**

- **#1 Giants +6.5 — loss.** The card ranked the cushion first because it projected a competitive 24–20 game and considered Nacua and Whittington unavailable, the Giants’ primary offensive line active, and Dart’s Week 1 form a counterweight to the Rams’ team-quality edge. The forecast explicitly named a 7–14 point Rams win as its main failure path. The game instead diverged sharply: Dart injured his knee at the end of New York’s opening drive and did not return; Winston replaced him. The Giants scored two field goals and no touchdowns. Meanwhile Stafford completed 22/31 for 327 yards and four touchdowns, and Adams had 195 receiving yards and two touchdowns. The Rams’ inactive/active checks were correctly relevant, but the in-game quarterback injury was not knowable before kickoff. This was a real variance event layered on a model that did not give enough probability mass to the Rams’ high-scoring outcome.
- **#2 Under 47.5 — win.** Thirty-four points finished 13.5 below the line. The forecast’s Under support included Nacua’s absence, a potential run/clock-control script and a central score below the line. Rams scored 28, four above the card’s Rams estimate, but the Giants’ six points overwhelmed that difference. This supports the total direction on this result, not the specific scoring mechanism or its unvalidated 54% probability.
- **#3 Over 47.5 — loss.** The 34-point total stayed below 47.5. Several listed Over pathways existed, but New York’s quarterback loss and low offensive output prevented them from combining with Rams production. This row is the complement of the Under.
- **#4 Rams -6.5 — win.** Los Angeles covered by a wide margin. The card preferred Rams outright but ranked its larger-margin branch last because its central margin was only about +4.35 and the Giants’ offensive state was expected to remain intact. The result came from a different state after Dart’s injury, alongside an exceptional Stafford/Adams performance.
- **Projected winner — Rams — correct.** The ~64% winner lean was right; it did not imply a high probability of covering -6.5, and the card correctly separated those contracts.

**Rank-1 and top-two review.** The explanation for the underdog rank was coherent only if this was actually frozen pregame. The injury is not a fair hindsight criticism of a pregame process, but the Q1 15:00 timestamp defeats the card’s own pre-kickoff claim until an independent issue timestamp proves otherwise. Existing start-crossing controls should prevent it from being treated as a certified pregame forecast. Conditional on a genuine pregame freeze, the report recognized both the cornerback-loss failure path and a 27+ point Rams branch; the miss is largely explained by the opening-drive QB injury and realized Rams efficiency. No new “avoid underdogs” rule is warranted. One of the top two won (Under); both did not.

**Total review.** Under won comfortably, but the realized total was driven by New York scoring only six after Dart’s injury, not by both offenses staying near the 24–20 representative state. The card correctly separated the total from the Rams’ win probability and identified the Rams’ offensive and Giants’ secondary upper tails. The game was at SoFi Stadium; the card reports a fixed roof and climate-controlled conditions, so weather was not a material variable. No TOP_OU_REVIEW trigger applies because the preferred total won.

**Validation and source audit.**

| Required question | Finding |
|---|---|
| Both starting lineups and QB status obtained before issue? | Official inactive lists were reportedly published and Dart was not inactive. But the Q1 15:00 state leaves the issue horizon unresolved; the record does not prove the final forecast preceded kickoff. |
| Bench/reserve or replacement information? | The card discussed depth and inactive players. Winston’s actual entry followed Dart’s in-game injury and was not a pregame availability omission. |
| Coaching information? | Team-quality and coaching context appeared in the winner rationale, but no game-specific tactical adjustment drove the pick. Postgame reports from both teams and the NFL describe the outcome; no coach change is needed to explain the injury. |
| Injuries/availability adequately checked? | Known inactives were checked per the card. Dart’s knee injury occurred during play and was not a known pregame absence. |
| Sources accurate/current? | NFL Game Center and both team recaps agree on final status and result. The supplied forecast’s content-reference markers prevent independent replay of each cited pregame feed and exact cutoff. |
| Better future sources? | Preserve the official inactive-list URLs and a true pre-kickoff timestamp; use NFL Game Center plus each team’s final report for settlement. |
| Meaningful blind spots? | The main unresolved issue is timing. Conditional on pregame issuance, the forecast named the Rams scoring path but underweighted its joint high tail and had no way to anticipate a first-drive QB injury. |
| Future treatment | Enforce an event-time freeze before kickoff, separate post-kickoff no-score refreshes, and keep injury-shock losses out of pregame process attribution unless the injury risk was known. |

**Learning status:** This card cannot be used as a clean pregame test until the timestamp conflict is reconciled. Its official outcome remains useful learning. No permanent football rule change from this single result.

### TMP-20260923-MLB-MIN-SF — Minnesota Twins @ San Francisco Giants (card claims P-486)

**Original card preserved:** C:\Users\danie\.codex\attachments\ffd9702e-2f1c-4a3e-8a2f-422b92cb696b\Pasted text.txt. It reports an 11:30 AEST final research pass about 15 minutes before the scheduled start, Twins ML ~59%, Giants +1.5 ~57%, Under 8.0 ~47% with ~10% push, Over 8.0 ~43% with ~10% push, and a Twins 4–3 representative score. The card explicitly says San Francisco’s final lineup was not reliably confirmed in the captured official source.

**Final result:** San Francisco 5, Minnesota 2 after nine innings; total 7. MLB’s exact game page shows 10 Giants hits, four Twins hits, no errors, and Matthews taking the loss after five earned runs in five innings with nine strikeouts. AP and NBC Sports Bay Area also report the 5–2 final. [MLB game record](https://www.mlb.com/video/game/823169), [AP recap hosted by CBS Sports](https://www.foxsports.com/articles/mlb/drew-gilberts-homer-and-2run-single-lead-giants-past-twins-52-to-end-3game-losing-streak), [NBC Sports Bay Area recap](https://www.nbcsportsbayarea.com/mlb/san-francisco-giants/drew-gilbert-bo-davidson-blade-tidwell-twins/1965184/).

| Original rank | As-issued selection | Result | Settlement |
|---|---|---|---|
| #1 | Minnesota Twins moneyline | Minnesota lost 2–5 | LOSS |
| #2 | San Francisco Giants +1.5 | San Francisco won | WIN |
| #3 | Under 8.0 runs | 7 total | WIN; no push |
| #4 | Over 8.0 runs | 7 total | LOSS; no push |
| Winner | Minnesota Twins, ~59% | Minnesota lost | INCORRECT |

**Decision and ranking diagnostics:** Three distinct decisions were represented: Twins moneyline lost, Giants +1.5 won, and the preferred Under won (2/3). Twins ML and Giants +1.5 are not complementary contracts; the total Under/Over pair is complementary and counts as one decision. Rank-1 loss: YES. Hit@2: YES. Wins@2: 1/2. Standard binary NDCG@2: 0.387. TOP_OU_REVIEW: NO; the highest-ranked total was Under at rank #3 and it won.

**Pick-by-pick review.**

- **#1 Twins moneyline — loss.** The card ranked Minnesota first because Matthews was viewed as the more established/deeper starter, SF was missing key bats, Minnesota had a fresher leverage bullpen, and the captured Twins order looked stronger than the uncertain Giants order. The report explicitly named the failure path: Matthews’ road/first-inning command problem, a Giants hitter capitalizing, Tidwell repeating a strong start and SF taking a lead to its home bullpen. That path substantially materialized. SF scored twice in the first on Brett Harris’s single, added two in the second on Drew Gilbert’s single, and Gilbert homered again in the fifth. Matthews allowed five earned runs in five innings despite striking out nine. The forecast found the right risk description but assigned too much probability to the Minnesota win branch relative to that known early-inning downside and unresolved SF lineup.
- **#2 Giants +1.5 — win.** San Francisco won outright, so the cushion covered. The card’s park/run-line analysis was consistent with a protective plus-run contract, but it expected a tighter family of scores. The actual 5–2 result was one of the card’s named kill paths for Minnesota ML and still safely won Giants +1.5. This is not evidence that the game was close.
- **#3 Under 8.0 — win.** Seven total runs cash the Under by one run; the integer line did not push. Oracle Park and the recognized absences supported suppression. The final total stayed below eight even though San Francisco produced five runs, because Minnesota managed only two. The forecast was directionally right on total despite a higher Minnesota run projection.
- **#4 Over 8.0 — loss.** Seven runs did not reach nine, so the Over lost without a push. It is the complement of the Under row, not an independent total trial.
- **Projected winner — Minnesota — incorrect.** The distribution leaned Twins despite listing Matthews’ early-inning failure as its primary adverse state. This is the principal process-review focus, not a reason to replace the winner label after the fact.

**Rank-1 and top-two review.** Twins ML (~59%) exceeded Giants +1.5 (~57%) by only two estimated points. The ranking can be defended as a small preference on the card’s frozen starter/bullpen evidence, but it was fragile and the SF lineup uncertainty should have widened the uncertainty around that ordinal choice. The actual first two innings followed the forecast’s explicit kill path. That does not prove the 59% estimate was irrational ex ante; it does show that naming a path is insufficient unless its weight is reflected in the distribution. Recheck early-inning run environment, starter command/recent early hooks, confirmed opponent order, and relief leverage before preferring an outright winner by two points. One of the top two won; both did not.

**Total review.** The line was eight, with the card assigning a material push probability. Actual total seven was a clean Under, not a push. The run-suppression story was partly correct, but the teams’ scoring was asymmetric: the Giants crossed their 3.3 central estimate while the Twins fell well below 4.2. That asymmetry explains why the total call can be right while the projected winner is wrong. No TOP_OU_REVIEW trigger applies. The one game does not justify changing the park or pitcher coefficients.

**Validation and source audit.**

| Required question | Finding |
|---|---|
| Both batting orders confirmed before issue? | No. Minnesota’s order was exposed, but the card explicitly records San Francisco’s order as unresolved in the captured official feed. |
| Bench/reserve and bullpen information? | Bullpens and workload were discussed; full final SF order and substitutions were not verified at issue. Postgame, Bo Davidson recorded a Giants debut hit and scored in the first; this is outcome evidence and cannot be backfilled into the forecast. |
| Manager information? | Team/manager context was present but no specific tactical move was central to the forecast. The run sequence was mainly pitcher execution and timely hits; no manager-change claim is supported here. |
| Injuries/availability adequately checked? | The card listed key absences and Minnesota’s inactive/out players. Its main information gap was the final SF batting order, not an undisclosed later injury. |
| Sources accurate/current? | MLB’s official game record, AP and NBC Sports Bay Area agree on the final. The MLB inning sequence and pitching line are the best settlement/statistical source. |
| Better future sources? | Keep the exact MLB gamePk, final batting-order page and official transaction/lineup feed, with capture time. Use AP or independent local reporting only as corroboration, not as a substitute for an official box score. |
| Meaningful blind spots? | Yes: unconfirmed SF lineup, high variance in Matthews’ early innings, and the possibility that one early cluster decides a low-total game before Minnesota’s bullpen advantage matters. |
| Future treatment | Reduce winner-ranking certainty when an opponent order is missing; model starter first-five and bullpen states separately; record which lineup version was known at the freeze. |

**Learning status:** The forecast stated its main failure path and the final game followed it. This is a useful calibration question, not a new baseball rule from one game. The protective run line and total remain separate decisions under the scoring method.

### TMP-20260923-WTA-WOLFF-OLI — Vivian Wolff vs Oleksandra Oliynykova, Singapore (card claims P-488)

**Original card preserved:** C:\Users\danie\.codex\attachments\4c5e0ff5-985b-46f3-afc0-e560f91b1e90\Pasted text.txt. It reports a final pre-match refresh around 12:56 PM AEST while the WTA match page showed Upcoming. It predicts Under 20.5 ~60%, Wolff +4.5 ~58%, Oliynykova -4.5 ~42%, Over 20.5 ~40%, Oliynykova to win ~74%, and gives 6–4, 6–4 as the representative score. The card explicitly labels probabilities unvalidated subjective.

**Final result:** Oliynykova defeated Wolff 6–1, 7–6; total 20 games and a six-game margin (Oliynykova 13, Wolff 7). The WTA score page, Tennis.com, TennisDB and MyKhel confirm the completed match, set score and winner. The TennisDB record identifies a balldontlie_wta data-provider key; the cross-publisher result agrees, while the Tennis.com service statistics differ from the WTA aggregate. There is a tiebreak-point discrepancy: the WTA score page and Tennis.com/MyKhel show the second-set tiebreak as 7–1, while a WTA news recap says 7–5. That disagreement does not change match winner, game total or margin, so it does not affect any listed market. [WTA score page](https://www.wtatennis.com/tournaments/1152/singapore/2026/scores/LS022), [Tennis.com score and stats](https://www.tennis.com/tournaments/singapore-open/matches/v-wolff-vs-o-oliynykova-2026-09-22), [TennisDB match record](https://tennis-db.com/wta/matches/balldontlie_wta%3A16975394/oleksandra-oliynykova-vs-vivian-wolff), [MyKhel scoreboard](https://www.mykhel.com/tennis/singapore-tennis-open-presented-by-bnp-paribas-2026-womens-singles-1-32-final-live-scoreboard-435624/), [WTA news recap](https://www.wtatennis.com/news/4579876/anisimova-pulls-out-of-singapore-with-left-wrist-injury).

| Original rank | As-issued selection | Result | Settlement |
|---|---|---|---|
| #1 | Under 20.5 total games | 20 games | WIN |
| #2 | Vivian Wolff +4.5 games | Lost by 6 games | LOSS |
| #3 | Oleksandra Oliynykova -4.5 games | Won by 6 games | WIN |
| #4 | Over 20.5 total games | 20 games | LOSS |
| Winner | Oleksandra Oliynykova, ~74% | Oliynykova won 2–0 | CORRECT |

**Decision and ranking diagnostics:** The two distinct decisions were total Under (win) and Wolff +4.5 (loss): 1/2. Rank-1 loss: NO. Hit@2: YES. Wins@2: 1/2. Standard binary NDCG@2: 0.613. TOP_OU_REVIEW: NO; the highest-ranked total was Under at rank #1 and it won. The Under/Over and +4.5/-4.5 rows are forced complements within their respective target pairs.

**Pick-by-pick review.**

- **#1 Under 20.5 — win.** The card’s representative 6–4, 6–4 score totals exactly 20 games, and the actual match also stayed at 20. The two-set branch occurred; the first set was much more one-sided than projected, while the second ran to a tiebreak. The total landed only half a game below the threshold, so the correct direction does not validate a 60% probability on its own.
- **#2 Wolff +4.5 — loss.** The match margin was six games, 1.5 beyond the handicap. The card correctly identified the main failure mechanism—Oliynykova repeatedly attacking Wolff’s second serve—but put more probability on a close straight-set match. The official WTA match stats show Wolff won 12/34 second-serve points (35.3%) versus Oliynykova 14/21 (66.7%); Oliynykova converted four of seven break points to Wolff one of four. Tennis.com reports different serve totals, so its point-by-point figures are not used for this causal claim. The actual 6–1 opening set created a five-game gap; the tiebreak second set added one more. The loss therefore came from the exact matchup vulnerability named in the card, realized at a magnitude that broke the cushion.
- **#3 Oliynykova -4.5 — win.** The six-game victory covered. The forecast’s likely-winner and second-serve mismatch reads were sound; its rank was lower because the card gave substantial mass to a close two-set branch.
- **#4 Over 20.5 — loss.** Exactly 20 games stayed below the half-point line. The second-set tiebreak did not add a game; it added only a tiebreak point sequence. The under/over pair is one total result.
- **Projected winner — Oliynykova — correct.** The higher-rated player won in straight sets. The 74% figure remains subjective and unvalidated.

**Top-two review.** Rank #1 won and rank #2 lost, so at least one but not both of the top two succeeded. The ordering is defensible from the original score tree: the predicted two-set center itself supported the Under, while Wolff +4.5 depended on a narrower close-score branch. The result exposed a joint-distribution issue: a straight-set match can stay under 20.5 while the favorite still covers -4.5. Future tennis cards should separately estimate set count, total games and game margin conditional on two sets instead of treating “straight sets” as sufficient support for the underdog handicap.

**Total and match review.** The surface and indoor-hard context were relevant; weather was not. The card adjusted for the large ranking difference, Wolff’s lower-level hard-court record and the difference between overall and hard-court strength. The winner and total were right, while the handicap was not. This is a useful split outcome: total score was exactly at the representative game count, but score distribution between players was asymmetric. No deep top-total failure review applies.

**Validation and source audit.**

| Required question | Finding |
|---|---|
| Starting lineups confirmed? | Not applicable to an individual tennis match; both scheduled participants and event status were identified by the official WTA page. |
| Bench/reserves or rotation? | Not applicable. |
| Coaching information? | No coach-specific input was necessary or documented as a decisive variable. |
| Injury/rest/availability checked? | The card reviewed recent workload and tournament participation and reported both players as entered and upcoming. It did not establish a medical examination or private health status. |
| Sources accurate/current? | The WTA score page, Tennis.com and TennisDB agree on event, completion, set score and winner; TennisDB identifies a balldontlie_wta provider. The WTA news recap conflicts on tiebreak points, and Tennis.com service statistics differ from WTA totals. Neither discrepancy changes the final game count, margin or winner. |
| Better future sources? | Use the tournament/WTA live score as the field-owner record, plus independent match-score publishers. Retain raw set/game score; document tiebreak differences without letting them alter totals. |
| Meaningful blind spots? | Yes: the estimated distribution underweighted a lopsided first set followed by one competitive set; a winner or two-set prior alone does not determine game margin. |
| Future treatment | Keep the joint score tree and report conditional game-margin quantiles for two-set outcomes. Do not change a rule from this single match. |

**Learning status:** Correct winner and total, failed cushion. The exact 20-game total despite a six-game margin is a sport-specific outcome-geometry observation, not evidence to promote a rule.

### REQUEST-ONLY-NBL-TAS-SEM — Tasmania JackJumpers vs South East Melbourne Phoenix (no forecast supplied)

The attached text contains an event/market request for Phoenix -4.5, Tasmania +4.5 and total 188.5, but contains no issued assistant forecast, ranking, probabilities or projected winner. Therefore there is no prediction entry to score or retrospective to fabricate.

The completed game was Tasmania 96, Phoenix 91 (total 187). If those lines are treated only as a contract-outcome illustration: Tasmania +4.5 WIN, Phoenix -4.5 LOSS, Under 188.5 WIN and Over 188.5 LOSS. These are not recorded as picks. The NBL schedule, NBL/AAP recap, Pulse Tasmania and Basketball.com.au agree on the result. NBL and independent reports describe Tasmania’s 36-point third quarter after trailing by 14 at half; reported final score and team/player detail support the arithmetic. [NBL schedule](https://www.nbl.com.au/club-schedule/sem), [NBL/AAP recap](https://www.nbl.com.au/news/jackjumpers-dig-deep-to-beat-phoenix), [Pulse Tasmania recap](https://pulsetasmania.com.au/news/jackjumpers-rally-from-16-down-to-beat-phoenix-96-91-in-first-game-of-season/), [Basketball.com.au recap](https://www.basketball.com.au/news/david-johnson-tasmania-jackjumpers-comeback-to-beat-south-east-melbourne-phoenix). This request-only item does not receive a prediction ID, ranking score or learning claim.

## 3. Fully Settled Logs

No new event above has been assigned a canonical P-ID. The WNBA, NFL, MLB and WTA outcomes and retrospectives are fully audited under temporary IDs, with canonical reconciliation still pending. The Tasmania NBL result is documented as request-only and unscored. Existing P-484 Padres card remains live. The NPB forecast remains upcoming and unresolved.

## 4. General Learnings, Rule Changes, Observations, and New Sources

### Cross-sport learnings

Ranking diagnostic definition: binary row relevance (win=1, loss=0), DCG@2 = rank-1 relevance + rank-2 relevance / log2(3), normalized by the ideal two-win top two. NDCG@2 ignores ranks below #2 and remains a secondary diagnostic.

- Keep forced complementary totals and handicaps as one target decision. Report row results, distinct decision results and event counts separately. The four forecast cards each have one winner among the top two (Hit@2), but a four-event sample cannot validate that metric.
- The four completed forecast cards each have two winning rows among four listed rows, but that raw 2/4 row count is not a four-independent-pick success rate. Three cards contain two forced pairs; the MLB card contains a forced total pair plus separate Twins moneyline and Giants +1.5 contracts. Use the decision accounting recorded per event.
- The probability estimates were subjective and unvalidated, no odds/operator terms were supplied, and one card’s issue horizon is unresolved. This mini log remains LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE. Do not claim calibration, value, ROI or prospective performance.
- A score/result explanation must distinguish pre-event process from in-game shocks. New York QB Dart’s first-drive injury is a game-state shock if the Giants card truly was pregame; the Q1 15:00 timestamp still prevents certification until reconciled.

### Sport-specific observations

- **WNBA, one event:** Atlanta’s third-quarter scoring cluster beat a near-line Under by only 1.5 points. The pregame card had identified transition and offensive-rebound tails and correctly labelled the Under low confidence. No permanent total adjustment follows.
- **NFL, one event:** The forecast named Rams scoring and New York-secondary failure as an adverse state, but New York’s QB injury drove a different game state. Preserve the source-time gate; do not create a generic underdog penalty from this result.
- **MLB, one event:** The Twins card’s stated Matthews early-inning/SF lineup failure path occurred. This is a calibration prompt for weighting a disclosed failure branch and for capturing the final opponent lineup; one case does not establish a new starter or road penalty.
- **WTA, one event:** A two-set result produced 20 games but a six-game margin. Match winner, total games and games handicap are separate projections; model game margin conditional on set score if evidence and validation permit.
- **NPB:** No result is available yet. The supplied timing statement is unresolved against the official pre-game status; retain the forecast unchanged and audit issue time at the next settlement update.
- **NBL request-only:** A completed score cannot be turned into a forecast retrospective where no original ranked card was supplied.

### Potential rule changes and algorithm improvements

These results connect to existing lessons L-20260917b-04 (forced-pair measurement) and L-20260919-12 (mandatory highest-ranked-total review); the WNBA Under loss receives that review. No permanent rule change is justified by these four different sports and four outcomes. Preserve existing controls: three independent event-result lineages, event-time freeze, source lineage tracking, separate result/decision counts, and the mandatory TOP_OU_REVIEW when the highest-ranked total does not win. The next algorithm work, if later validated, is to test ranking stability under probability uncertainty, lineup-missingness sensitivity, WNBA turnover-to-transition scoring, MLB first-five versus bullpen state, and tennis two-set game-margin distributions. Do not fit or promote any coefficient from these outcomes.

### Source improvements

- For completed results, prefer exact league event/box-score pages, then the host/participant primary report, then an independent high-quality report. Current useful examples are WNBA official game/team pages, NFL Game Center and team recaps, MLB gamePk scorecards, WTA’s tournament score page and NPB’s exact box score.
- The WTA result comparison caught a tiebreak-point conflict while leaving the total game count and margin stable. Record which disputed fields could change the contract; immaterial point-level differences do not block these market settlements.
- The user-supplied forecast attachments contain opaque content-reference tokens. For future auditability, preserve actual source URLs, timestamps, and the exact frozen event/lineup pages inside the card. Do not promote any publisher to a preferred-source register based on one match.
- NBL’s official schedule and independent Pulse Tasmania/Basketball.com.au reporting were useful for confirming the completed 96–91 result; the NBL recap is AAP-syndicated and should not be counted again as an independent publisher from the AAP copy.

### Data-quality observations and recurring blind spots

- One WNBA card lacked both game-day starting fives; the Twins card lacked a confirmed San Francisco order; the NFL card conflicts on whether issue preceded kickoff; the NPB card also has an unresolved issue-time statement. Record missing values and freeze times explicitly.
- A low evidence label does not remove the need to check lineups, source lineage or ranking sensitivity. It should widen uncertainty and limit claims.
- Do not infer that a stated “final pregame refresh” proves pregame status when its event-state timestamp says the clock has started.
- Settlement here is directional research-line grading only. No operator, price, accepted wager, void terms or cashout terms were provided.

### Items requiring more evidence before becoming formal rules

- Whether uncertainty-aware ranking improves top-two results across a prospective, event-grouped sample.
- Whether lineup completeness changes WNBA or MLB ranking/calibration after controlling for team strength and game timing.
- Whether tennis two-set conditional game-margin modeling improves handicap forecasts.
- Any claim about systematic under/over bias, NFL backup-quarterback tails, MLB early-inning variance, or provider performance needs a larger timestamped sample and prospective validation.

## 5. Document Update Mapping

No Google Drive document or canonical combined log was modified by this update.

| Finding or future disposition | Document for a later update, if evidence warrants it |
|---|---|
| Temporary-ID reconciliation for WNBA P-484 collision; P-485/P-486/P-488/P-489 claims and missing P-487 | PREDICTION_LOG_COMBINED_5.md; retain this mini-log evidence until the active canonical snapshot is reconciled |
| Universal event-time freeze and source-lineage evidence | METHOD.md and SCORING_AND_VALIDATION.md; current controls already cover start-crossing and three-lineage checks, so this audit proposes no change |
| WNBA lineup, pace/transition and total-distribution learning | RULES_BASKETBALL.md; record only as an unpromoted event note unless a repeated prospective pattern appears |
| NFL issue-time and QB-state review | RULES_AMERICAN_FOOTBALL.md plus METHOD.md for horizon handling; current start-crossing control should govern |
| Twins starter/lineup/bullpen review | RULES_BASEBALL.md; no coefficient or new rule proposed from one game |
| WTA conditional set/game-margin observation | RULES_TENNIS.md; keep as a testable observation, not a forecast rule |
| Captured source URLs, timestamps and publisher lineage | DATA_SOURCE_REGISTER.md and each future card’s source ledger; do not promote a source from a single event |
| Cross-sport decision accounting and learning-only status | SCORING_AND_VALIDATION.md and LEARNING_REGISTER.md; current measurement/eligibility controls already apply |

## Settled logs

- TMP-20260923-WNBA-ATL-NYL — result and all supplied markets settled; canonical P-484 collision retained.
- TMP-20260923-NFL-NYG-LAR — result and all supplied markets settled for learning; canonical P-485 claim held, pregame horizon unverified.
- TMP-20260923-MLB-MIN-SF — result and all supplied markets settled; canonical P-486 claim held.
- TMP-20260923-WTA-WOLFF-OLI — result and all supplied markets settled; canonical P-488 claim held.
- REQUEST-ONLY-NBL-TAS-SEM — final score verified; no forecast or picks to settle.

## Logs still awaiting settlement

- P-484 — Padres @ Dodgers — LIVE, 0–5 bottom of the fifth in the latest official MLB feed; retain all four picks unchanged.
- TMP-20260923-NPB-CHU-DB — Chunichi @ DeNA — UPCOMING at the latest official NPB check; retain all four picks unchanged. Audit the issue-time conflict when the event is final.
- TMP-20260923-NPB-BUF-MAR — Orix @ Lotte — UPCOMING / PRE-GAME (scheduled 17:00 JST / 18:00 AEST); pre-game research frozen; retain all four picks unchanged.

All records in this mini log remain LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE.
