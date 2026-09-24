# Prediction Mini Running Log - P-494 onward (local)

Created: 2026-09-23 20:44:23 +10:00; last updated: 2026-09-23 21:11 +10:00 (Australia/Sydney).
Status: ACTIVE LOCAL MINI LOG. P-494 is reconciled to the WTA live-view card below; the soccer request has a no-forecast disposition. Next canonical ID: P-495.
Canonical authority: PREDICTION_LOG_COMBINED_5.md is the canonical forecast log. Highest canonical ID: P-494; next is P-495. P-494 is the earlier WTA live-issued view frozen at 20:51:54 AEST; the later soccer request received no forecast and consumes no ID.
Previous mini log: P-482-P-493 cards and prior settled history remain in C:\Users\danie\Documents\Sports Research\PREDICTION_MINI_RUNNING_LOG_MERGED_P482_ONWARD.md, now a predecessor record. Unresolved cards are carried forward below; source cards and their pregame reasoning are preserved.
Current method: METHOD.md MDS-2026.09.19-v4.3 / CR-2026.09.21-3. Freeze the exact control-manifest receipt with each new card: CONTROL_MANIFEST_2026-09-21-3.md, SHA-256 079B43F75681818724723556D66A82C01F56F6383F82055F0F50AF88C97C0C00. Apply CONTROLS.md, RULES_GENERAL.md, SCORING_AND_VALIDATION.md, SOURCES.md, and the relevant sport-specific rule file after the event is known.
Operating mode: SPORTS_ONLY / MARKET_BLIND. No bookmaker, tipster, odds, or fantasy sources as forecast evidence.
Performance status: LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE. No ROI, EV, calibrated edge, or validated model claims.
Drive scope: This working log is local. No Google Drive files were created or changed.

## 1. Incomplete / Unsettled Logs

These carryovers remain unresolved because no fresh terminal-state verification and source-complete settlement was performed during this log handoff. Scheduled start times passing do not establish a final result. Keep every card and its original picks unchanged until a future settlement pass verifies the event and exact outcome under the current three-independent-lineage terminal-state gate.

### Current pending register

| ID / handle | Sport and event | Scheduled start | Last recorded status | Reason still pending |
|---|---|---|---|---|
| P-489 | NPB - Chunichi Dragons @ Yokohama DeNA BayStars | 23 Sep 2026, 19:00 AEST | Official page showed pre-game at the last recorded check around 15:15 AEST; scheduled start has since passed | No terminal-state refresh; issue horizon is unverified; same-event R1 is retained |
| P-491 | NPB - Orix Buffaloes @ Chiba Lotte Marines | 23 Sep 2026, 18:00 AEST | Official page and both starters were checked pregame around 17:53-17:56 AEST | Scheduled start has passed; terminal state not checked |
| P-493 | KBO - Kia Tigers @ Doosan Bears | 23 Sep 2026, 19:30 AEST | Pregame freeze 19:28:29 AEST; event was not started at final check | Scheduled start has passed; terminal state not checked |
| P-494 | WTA Singapore Open - Mirra Andreeva vs Aliaksandra Sasnovich | 23 Sep 2026, live view frozen 20:51:54 AEST | Feed at 20:51:14 AEST: set 1, Andreeva 2-1 and serving | LIVE-ISSUED; terminal state not refreshed; excluded from pregame metrics |
| TMP-20260923-NBL-CNS-TAS | NBL - Cairns Taipans vs Tasmania JackJumpers | 23 Sep 2026, 19:30 AEST | NBL homepage displayed LIVE NOW at 19:34:50; later raw endpoint response is quarantined and not usable as verified state | Exact live state and terminal result were not independently verified; P-487 issue-time claim is held, not canonical |

The following card records preserve all supplied pregame picks, reasoning and sources. Carry-forward status notes above are later custody information; they are not retrospective results.

### P-489 - NPB - Chunichi Dragons @ Yokohama DeNA BayStars (alias TMP-20260923-NPB-CHU-DB)

| Field | Current audit |
|---|---|
| Card as supplied (preserved) | Four-ranked forecast. Probabilities are marked UNVALIDATED_SUBJECTIVE. |
| Ranked rows | #1 Under 6.5 (~62%); #2 DeNA moneyline (~60%); #3 Chunichi +1.5 (~57%); #4 Over 6.5 (~38%) |
| Potential winner | DeNA (~60%); representative score DeNA 3–2 |
| Event status | **UPCOMING.** Re-checked 2026-09-23 ~15:15 AEST. The NPB official box score shows 【試合開始前】 (pre-game), 開始 18:00 JST at Yokohama Stadium. 18:00 JST = **19:00 AEST (Australia/Melbourne), 23 Sep 2026**. No score. |
| Competition rule relevant to settlement | NPB Central League regular season. A tie after 12 innings is a terminal outcome (RULES_BASEBALL §9.3 and control 32). The winner row must be settled three-way: DeNA / Chunichi / tie. A tie makes "DeNA ML" not a win, and it depends on the card's stated tie rule. Chunichi +1.5 **wins** on a tie. The totals settle on the final including extras up to 12. Central League pitchers bat (no DH in 2026). |
| Issue-time integrity | ISSUE_HORIZON_UNVERIFIED. The card says its final refresh was just after the corrected scheduled start. The official page showed pre-game at a later check, so the claim conflicts with the official state. Do not treat the current pre-game status as proof of the issue time. |
| Settlement | NOT SETTLED. No result, ranking score or retrospective until an official terminal state exists and three independent lineages agree (CR-4 gate). Recommended settlement lanes: NPB official box (field owner); the NPB English box score; and one independent Japanese outlet such as Nikkan Sports or Sponichi. Club and league mirrors are **not** separate lineages. |
| Original card | Preserved unchanged at `C:\Users\danie\.codex\attachments\8d873c0b-ccec-4784-961e-5cbca169cc34\Pasted text.txt`. |

Event identity/status source: [NPB official box score](https://npb.jp/scores/2026/0923/db-d-25/box.html).

---

#### Original P-489 card provenance

The full original forecast text is preserved in the supplied local attachment: C:\Users\danie\.codex\attachments\8d873c0b-ccec-4784-961e-5cbca169cc34\Pasted text.txt. The summary and ranked rows above match that card. It contains a date discrepancy (its own schedule line says 22 Sep, while NPB's event page and later R1 record say 23 Sep) and unresolved chatgpt-content-reference citation tokens. Do not reconstruct missing citation URLs. Its source names are NPB official schedule/Central League page, official NPB pitching leaders and player pages, SportsNavi starter logs and Sep 21 game boxes, Nikkansports, DeNA official transactions, Baseball Chronicle park factors, official NPB recent results, and the cited Drive/GitHub material. The attachment also appends a pre-reconciliation mini-log snapshot; its old next-ID/collision statements are superseded by the current register in this file. The original card's issue horizon remains unverified.

#### Same-event P-489 reforecast R1

The R1 source text below was recovered from the byte-exact pre-reconciliation archive. Its original ID note said the canonical ID was unresolved; the 2026-09-23 reconciliation confirms P-489 for this same event. R1 consumes no additional ID. Picks, reasoning, source ledger and cutoff text are retained as issued.

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

**Post-reconciliation status correction (custody only).** The preceding R1 source card states that the canonical ID is unresolved; that was its original pre-reconciliation status. The event is now canonical P-489. It remains unsettled because no terminal-state refresh was performed and its issue horizon remains unverified. No pick, probability or reasoning was changed.

### P-491 - NPB - Orix Buffaloes @ Chiba Lotte Marines (ZOZO Marine, 23 Sep 2026)

**Status:** UNSETTLED — PREGAME FORECAST / NO RETROSPECTIVE (none requested).

**Identity / timing**
- Canonical mini-log ID: `P-491`. NPB game page: `npb.jp/scores/2026/0923/m-b-25/`.
- Competition: NPB Pacific League regular season. Chiba Lotte Marines (home, bat last) vs Orix Buffaloes. ZOZO Marine Stadium, Chiba; outdoor, no roof.
- Scheduled start: 17:00 JST = **18:00 AEST, 23 Sep 2026** (NPB schedule and box page).
- Final refresh before issue: NPB official box page showed **【試合開始前】 ◇開始 17:00** with both スタメン posted. Captured about 17:53–17:56 AEST; picks were delivered to the user at about 17:54 AEST. **Horizon: CLEAN (pre-start).** The freeze preceded the 18:00 AEST scheduled first pitch.
- Method / controls: `MDS-2026.09.19-v4.3 / CR-2026.09.21-3`; `SFA-BASEBALL`; `SPORTS_ONLY / MARKET_BLIND`; `LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE`.

**Supplied contracts**
- Buffaloes +1.5; Marines ML; game total Over 7.0 / Under 7.0.
- The integer total carries **push** mass at exactly 7.
- NPB regular-season games are capped at 12 innings, and a tie is terminal (RULES_BASEBALL §9.3). Operator tie and action rules were **not supplied** (`UNKNOWN_DEFINITION`).
  - Marines ML is graded "not a win" on a tie. It is a push or void if the operator uses tie-no-bet.
  - Buffaloes +1.5 wins on a tie.
  - Totals settle on the 12-inning final.
- The lines were visible in the request. The run centres below were built from team and starter rates, and the lines were located only afterwards.

**BB-P gates**
- `BB-P1` starters: **CONFIRMED_OFFICIAL** from the NPB box page 先発 fields.
  - Orix: **九里 亜蓮 (Aren Kuri)**, RHP.
  - Lotte: **ジョーイ・ルケーシー (Joey Lucchesi)**, LHP.
  - Cross-check: SKY PerfecTV's starter page marks both as 予告先発.
- `BB-P2` batting orders: **both posted** (NPB box page).
  - Orix: 1 西川 左, 2 来田 中, 3 太田 二, 4 杉本 指, 5 宗 三, 6 紅林 遊, 7 内藤 一, 8 若月 捕, 9 池田 右.
  - Lotte: 1 藤原 中, 2 上田 一, 3 山口 左, 4 西川 右, 5 寺地 三, 6 ソト 指, 7 佐藤 捕, 8 山﨑 遊, 9 小川 二.
  - Individual injury lists and ichi-gun registration moves were **not retrieved** (`RETRIEVAL_MISS`). Absences are therefore only what the posted orders imply.
  - Bench and bullpen availability were not captured beyond the 9/22 game note below.
- `BB-P3`: Pacific League uses the DH (both sides). 9 innings, capped at 12, tie terminal. No roof.
- `BB-P4`: official-game rule per NPB. Operator terms unknown.
- `BB-P5`: Lotte bats last. The total includes extras up to the 12th.

**Starter evidence (G14.1 deficit attribution)**
- **Kuri (Orix).**
  - NPB official 2026 line: 25 G, 8–11, 150.2 IP, 132 H, 13 HR, 60 BB, 139 K, 65 R, 56 ER, **3.35 ERA**. His 2025 line was a 2.41 ERA over 164.1 IP.
  - Last ten starts (gurazeni per-game log; secondary source): 9/16 SoftBank 6 IP 0 R; 9/09 Seibu 4 IP 6 ER; 9/01 Rakuten 5 IP 3 ER, 5 BB; 8/25 Rakuten 5 IP 4 ER, 6 BB; 8/18 Seibu 3 IP 6 R (3 ER); 8/11 7 IP 1 ER; 8/03 6 IP 6 R (2 ER); **7/26 vs Lotte 6 IP 3 ER, 10 K, 127 pitches**; 7/20 7 IP 0 R; 7/14 6 IP 2 ER.
  - Recent walks and short starts are recorded. Under R-1 no named mechanism (velocity, injury or role change) was found, so the season rate is used and the recent form only **widens** Lotte's scoring distribution.
  - Hook distribution: usually 5–7 IP at 80–127 pitches. Early-hook (≤4 IP) share in the last ten starts: 2 of 10.
- **Lucchesi (Lotte).**
  - Ex-MLB left-hander, joined Lotte in mid-July. NPB: 3 G, 1–1, 15 IP, 7 ER, **4.20 ERA**. His three logged starts give 9 H, 1 HR, **10 BB**, 12 K.
  - Starts: 8/9 vs Orix 4 IP 2 ER, 71 pitches; **9/6 vs Orix 7 IP 0 R, 1 H, 4 BB, 103 pitches**; 9/13 vs SoftBank 4 IP 5 ER, 4 BB, 100 pitches.
  - Mynavi (23 Sep) confirms today is his fourth NPB start. It reports no health issue or pitch limit.
  - **Small-sample starter** (3 starts): his profile is a prior, not a rate. Per §8.6 override 8 this is attached to **Orix's** scoring branch as extra width.
  - His walk rate is the main upper-tail mechanism for Orix. He is 11 IP / 2 ER against Orix, but that is two games and is `E — diagnostic only`.

**Team context (NPB official, to 21 Sep)**
- Standings: Orix 63–71–2 (4th); Lotte 58–68–3 (5th). Both are out of contention.
- Runs scored per game: Orix 470/136 = **3.46** (.245/.307/.357, 90 HR, fewest in the PL); Lotte 453/129 = **3.51** (.237/.297/.363, 117 HR).
- Runs allowed per game: Orix 570/136 = **4.19** (3.93 ERA); Lotte 537/129 = **4.16** (3.88 ERA).
- The two teams' games average roughly 7.6–7.7 total runs on season rates.
- Previous game (22 Sep, same venue): **Orix 6–4 Lotte** (NPB box; linescore Orix 0-1-0-0-1-2-2-0-0, Lotte 1-2-0-0-0-0-0-0-1; 3 h 21 min). Both bullpens were used. Individual reliever lines were **not reliably extracted** (the fetched box summary was internally inconsistent), so bullpen fatigue is carried as `UNQUANTIFIED`, not as a signed input.
- Recent H2H (Mynavi): Orix 3–2 over the last five meetings. `E — diagnostic`.

**Environment (§8.9)**
- tenki.jp ZOZO Marine hourly forecast, issued 23 Sep 09:00: cloudy; 21.5–22.1°C; 30% rain probability with 0 mm/h; humidity 81–88%; **NE wind at 2 m/s** from 17:00 to 21:00.
- Light wind removes ZOZO Marine's usual wind-driven variance. Cool, humid air is mildly suppressive, but no signed park factor is applied beyond that.
- Umpire crew was not retrieved.
- Termination branch (rain) is small: 0 mm/h forecast.

**Joint run object (frozen before querying the lines)**
- Team centres, from partially pooled offence × opponent run prevention × starter adjustment around a PL run environment of ~3.8 runs per team-game: **Orix ≈ 3.6, Lotte ≈ 3.7** runs per 9.
- Simulation: per-inning Poisson with a gamma team-game multiplier (k = 2). Includes the home-ninth rule and extras to 12 with a tie cap. `UNVALIDATED_SUBJECTIVE`; not fitted or calibrated.
- Derived: mean total **7.19**; P(total ≥ 8) **0.397**; P(total = 7) **0.104**; P(total ≤ 6) **0.499**.
- Outcomes: Lotte win 0.494; Orix win 0.476; tie 0.030.
- Margin (Lotte minus Orix): +1 0.170 (modal); +2 0.097; +3 0.068; +4 0.048; −1 0.136; −2 0.091.
- Sensitivity (±0.2 runs per side): the Under minus Over gap stays at 3–17 points; Orix +1.5 stays at 0.66–0.70; the winner stays within ±3 points of 50/50.

**Nine-branch coverage**
- **B1** both starters central (~5–6 IP each) → 3–4 runs each, the modal family.
- **B2** early hook: Kuri 2/10 recent starts ≤4 IP; Lucchesi 2/3 starts at 4 IP. This is the largest Over and swing driver.
- **B3** HR cluster: Lotte has more power (117 HR) than Orix (90).
- **B4** one-sided separation with a 0–2 opponent floor. It defeats Orix +1.5 when Lotte is the side separating.
- **B5** relief transition after both pens were used on 9/22.
- **B6** Lotte skips the bottom 9th when leading. This caps the total and favours the Under.
- **B7** extras to 12 with no runner rule.
- **B8** rain is negligible.
- **B9** late separation through the bullpens.

**Ranked picks**
1. **Buffaloes +1.5 — ~0.67 `UNVALIDATED_SUBJECTIVE`. Evidence: LOW–MEDIUM.**
   - Wins: Orix win 0.476 + Lotte by exactly 1 (0.170) + tie 0.030.
   - Override 3: BB-B4 separations by Lotte (2+ runs, ~0.32) are **not** excluded. They are the kill path: a Lotte HR cluster (B3), or Kuri's walk-driven early hook (B2) followed by a pen used on 9/22. The row ranks first because a low-scoring game between two weak offences puts heavy mass on margins of one run or fewer, not because separation is impossible.
   - G30.1: the potential winner named below is Lotte. The separating states are Lotte by exactly 1 (+1.5 wins, Lotte ML wins) and Lotte by 2+ (+1.5 loses).
2. **Under 7.0 — ~0.50 win / 0.10 push / 0.40 loss (~0.56 excluding push). Evidence: LOW.**
   - Override 2 (why the upper tail is subordinate): both offences are bottom-half on OBP and SLG; Orix is last in HR; conditions are cool with light wind; and the home ninth is capped.
   - Named upper-tail kill path, with its mass: both starters are walk-prone (Lucchesi 10 BB in 15 IP; Kuri 14 BB over 9/1–9/9 and 8/25). Early-hook states (B2) plus pens used on 9/22 feed the ~0.40 Over mass.
   - Override 9 re-solve: P(Under 7 ∧ Orix +1.5) ≈ 0.354, so P(Under | +1.5 wins) ≈ 0.52. The rows are positively dependent through low-scoring, close games.
3. **Marines ML — ~0.49 (tie 0.03 counts as no-win). Evidence: LOW.**
   - Home, last at-bat, and Kuri's recent command issues on one side. Against that: Lucchesi's small-sample walk rate and Orix winning 9/22.
   - This is a near coin flip. Coherence check: P(Orix +1.5) 0.676 ≥ 1 − P(Marines ML) = 0.506 ✔.
4. **Over 7.0 — ~0.40 (0.10 push).** Live through B2/B3: early hooks, walk clusters and Lotte's power. It ranks last because the centre (7.19) sits barely above the line and the integer push absorbs part of the upper mass.

**Potential winner:** **Chiba Lotte Marines, narrowly — ~0.49 vs Orix ~0.48, tie ~0.03. LOW confidence; effectively a toss-up.** Endpoint: the eventual result including extras to 12; a tie is possible.

**Dependence / coherence**
- Representative Rank-1 scoreline: **Lotte 3–2**. That is Orix +1.5 **WIN**, Under 7 **WIN** (5 runs) and Marines ML **WIN**. All three top rows are compatible.
- Top-two both-fail state (Lotte by 2+ ∧ total ≥ 8), e.g. Lotte 6–3: **≈0.152** from the same simulation. Shared failure driver: **Lotte offensive separation after an early Kuri exit**.
- C-MODAL-BRANCH-CHECK: the modal margin (Lotte +1) and the modal total region (≤6) **satisfy** Rank #1 and #2. The modal branch does not defeat the top two.
- PR-3 shared driver: the top two share the "low-scoring, close game" driver. Positive coupling is disclosed.
- Forced pairs: Over/Under 7.0 is one decision. Marines ML and Buffaloes +1.5 are **not** complements; a Lotte one-run win cashes both.

**Sources**
1. [NPB official box/preview page — m-b-25](https://npb.jp/scores/2026/0923/m-b-25/box.html): state 【試合開始前】, 17:00 start, both 先発, both スタメン. Field owner.
2. [NPB 2026 September schedule](https://npb.jp/games/2026/schedule_09_detail.html): fixture, ZOZOマリン, 17:00.
3. [NPB English schedule 23 Sep](https://npb.jp/bis/eng/2026/games/gm20260923.html): fixture cross-check.
4. [SKY PerfecTV starter page](https://baseball.skyperfectv.co.jp/starter/): 予告先発 cross-check (ルケーシー / 九里).
5. [NPB — Kuri year-by-year](https://npb.jp/bis/players/71775139.html): 2026 and 2025 lines.
6. [NPB — Lucchesi year-by-year](https://npb.jp/bis/players/93095152.html): 2026 NPB line, LHP.
7. [gurazeni — Kuri game log](https://www.gurazeni.com/player/910) and [gurazeni — Lucchesi game log](https://www.gurazeni.com/player_pitching/2932/year:2026): per-start IP, pitches, BB, K, R, ER. Secondary source; totals reconcile with NPB for Lucchesi (15 IP, 7 ER).
8. [Mynavi — Lucchesi interview, 23 Sep](https://news.mynavi.jp/article/20260923-5013260/): fourth NPB start today; last start 9/13. Availability evidence only (S-2).
9. [Mynavi — pre-game page](https://news.mynavi.jp/article/20260923-5011451/): last-five H2H 3–2 Orix.
10. [NPB PL standings](https://npb.jp/bis/2026/stats/std_p.html), [team batting](https://npb.jp/bis/2026/stats/tmb_p.html), [team pitching](https://npb.jp/bis/2026/stats/tmp_p.html): to 21 Sep.
11. [NPB box 22 Sep (m-b-24)](https://npb.jp/scores/2026/0922/m-b-24/box.html) and [Weekly Baseball Online game flash 22 Sep](https://sp.baseball.findfriends.jp/?pid=game_flash&game_id=2026092205): prior-game result 6–4 Orix and linescore. Reliever lines not used (extraction inconsistent).
12. [tenki.jp — ZOZO Marine hourly forecast](https://tenki.jp/leisure/baseball/3/15/31009/1hour.html): conditions.
13. Drive methodology: `RULES_BASEBALL.md` (§8, §8.6 overrides 2/3/8/9, §9.3 NPB ties, 2026-09-19 R-1, CR-2026.09.21-3), `METHOD.md`, `RULES_GENERAL.md`.

**Source firewall / limitations**
- No odds, betting previews, prediction markets, tipsters or fantasy pages were used. Betting-preview results that appeared in searches were not opened.
- Missing inputs:
  - injury and registration list (`RETRIEVAL_MISS`);
  - reliever availability and pitch counts from 9/22;
  - umpire;
  - Statcast-grade arsenal data for NPB (not available);
  - handedness splits for both lineups (not retrieved).
- Several numbers came through a summarising fetch tool. Values used were cross-checked where two sources existed (Lucchesi totals; starters; lineups from the field owner).

**Document mapping / candidate observations**
- `RULES_BASEBALL.md`: no change. §9.3 tie handling is applied (Buffaloes +1.5 wins a tie; ML needs the operator's tie rule).
- `DATA_SOURCE_REGISTER.md`: the NPB box page (`/scores/YYYY/MMDD/<home>-<away>-NN/box.html`) exposes pre-game 先発 and スタメン about an hour before first pitch. Use it as the BB-P1/BB-P2 lane. The `/announcement/starter/` and `/scores/.../` index routes redirect-loop through the fetch tool.
- PR-1: this card is the first in the log with a verified pre-start freeze and both lineups posted.

---

### P-493 - KBO - Kia Tigers @ Doosan Bears (unsettled; canonical ID confirmed)
#### Original pre-reconciliation source handle: TMP-20260923-KBO-KIA-DOO

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

### TMP-20260923-NBL-CNS-TAS (source card and status corrections follow verbatim; no canonical ID assigned)
### TMP-20260923-NBL-CNS-TAS — Cairns Taipans vs Tasmania JackJumpers (claimed P-487; unsettled)

| Field | Current audit / pregame record |
|---|---|
| Matchup & Schedule | Cairns Taipans (Home) vs Tasmania JackJumpers (Away), Australia NBL 2026–27 Round 2. Scheduled: 23 September 2026, 7:30 PM AEST, Cairns Convention Centre. |
| Key Rosters & Availability | **Cairns:** Keanu Pinder, Shaun Bruce, Sunday Dech, Jaylon Brown, Jonah Bolden, Malique Lewis, Reyne Smith. *Out/Injured:* Jaylin Galloway (shoulder/arm), Luke Paul.<br>**Tasmania:** David Johnson, Taran Armstrong, Will Magnay, Dakota Mathias, Nick Marshall, Majok Deng, Ben Gold. *Return:* Josh Bannan. |
| Card as supplied | Four-ranked forecast: #1 JackJumpers +2.5; #2 Combined Total Under 186.5 Points (noting prompt text "Under 18.5" as clerical typo); #3 Combined Total Over 186.5 Points; #4 Taipans -2.5. Potential winner: Tasmania JackJumpers (lean, representative score Tasmania 91 – Cairns 88). |
| Event status | UPCOMING / PRE-GAME at issuance verification. Verified against official NBL schedule. No live score, in-game play, or outcome data used. |
| Issue-time integrity | Analysis-only pregame entry; no postgame retrospective or settlement fabricated. Operating under MARKET_BLIND / SPORTS_ONLY rules without odds or fantasy data. |
| Settlement | NOT SETTLED / AWAITING TERMINAL RESULT. Retain all picks unchanged until official final NBL box score. |
| Key Rationale | JackJumpers +2.5 provides dual cover branches (Tasmania outright win + 1–2 pt Cairns win). Scott Roth's defensive discipline and interior rim deterrence (Will Magnay) contrast with Cairns' defensive collapse in R1 (surrendered 111 pts to Sydney). Cairns is missing perimeter depth (Galloway, Paul). Total 186.5 favors Under given Tasmania's deliberate half-court pace, cross-country travel fatigue on 48h rest, and reduced offensive transition opportunities. |

Event identity/status sources: [NBL official schedule](https://www.nbl.com.au/), [Taipans official site](https://www.taipans.com/), [JackJumpers official site](https://www.jackjumpers.com.au/). This event stays in Incomplete / Unsettled Logs.

#### 2026-09-23 19:34:50 AEST research refresh — no new forecast; no retrospective

This is an append-only issue-time status update to the existing event record, not a second forecast and not a result review. At retrieval, the official NBL homepage marked Cairns–Tasmania **LIVE NOW**. The fixture is scheduled for 19:30 AEST at Cairns Convention Centre, but the official Game Centre page returned “Could not load match data.” I could not verify whether play had actually begun, the score, period/clock, possessions, active on-court lineups, fouls/bonus, or rotation minutes. With no reliable live-state feed, the live-state requirements in `RULES_BASKETBALL.md` §5 cannot be met. No new picks or winner are issued from this refresh.

The latest official NBL preview provides an **expected depth chart**, not confirmed starting fives. It lists Cairns absences Jaylin Galloway (shoulder; Round 6) and Luke Paul (ankle; Round 3), and Tasmania absences Ben Ayre (hip flexor; Round 3), Josh Bannan (ribs; TBC), Anthony Drmic (back; TBC), and Bryce Hamilton (ACL; TBC). The official league injury list was updated 23 Sep at 9:30am AEST. The existing roster note above saying “Return: Josh Bannan” is therefore unsupported by the current official preview and is superseded for availability: Bannan was listed out in the expected depth chart and injury section. No confirmed late change or starting five was retrieved.

The submitted total pair is contract-inconsistent as written: **Over 186.5** and **Under 18.5** are not complements. I have not changed 18.5 to 186.5. A clarification is needed before this can be treated as a matched Over/Under decision.

Historical ID custody note (superseded for sequence only): at this 19:34:50 AEST refresh, the earlier P-484/P-487 claims had not been reconciled, so no canonical ID was assigned in that update. The later 2026-09-23 reconciliation resolves the next ID as P-494 and keeps this NBL event under TMP-20260923-NBL-CNS-TAS with P-487 on issue-time hold. No pick, result or retrospective is changed.

Sources checked for this refresh:
- [Official NBL homepage](https://league.nbl.com.au/) — event indicator displayed LIVE NOW at retrieval.
- [Official NBL Game Centre](https://schedule.nbl.com.au/match?from=%2Fnbl%2F2026%3Flogo%3D0&league=NBL&match=36e0818b-58ad-11f1-89d2-fb9d3a8baf78&season=67d4a190-40bc-4bfb-a9a2-11bd0b93f020&year=2026) — exact match page; match data unavailable at retrieval.
- [Official NBL game preview and expected depth charts](https://www.nbl.com.au/news/how-to-watch-talking-points-cairns-v-tasmania-round2).
- [Official NBL injury list](https://www.nbl.com.au/news/nbl26-the-latest-injury-updates) — page states last updated 23 Sep 2026, 9:30am AEST.
- [Taipans official Round 1 injury report](https://www.taipans.com/news/injury-report-round-1-nbl27) and [official Cairns schedule](https://www.taipans.com/schedule) — cross-check of the published availability note and fixture.
- [Official Tasmania club schedule](https://www.nbl.com.au/club-schedule/tas) — fixture and prior-game context.

#### 2026-09-23 19:36 AEST official-feed correction — game in progress; no live forecast

The earlier 19:34:50 status note is supplemented by a raw response observed from the official NBL match-data endpoint: it reported `IN_PROGRESS` / `phase=live`, Cairns 0–Tasmania 0, Q1 9:45 with the clock running, and incomplete on-court data (zero Cairns player records versus five Tasmania player records). **That response is quarantined under the correction below and is not usable evidence**; do not treat its status, score or clock as verified. The NBL homepage displayed `LIVE NOW`, while the browser-readable Game Centre failed to load match data, so exact live score, clock and lineups remain unavailable from an admissible source. The supplied pregame lines cannot be freshly forecast in this unverified live state. The `Under 18.5` contract discrepancy is also unresolved. No picks or winner issued; no retrospective or settlement entered.

Additional source initially checked: [official NBL match-data endpoint for this fixture](https://schedule.nbl.com.au/api/calendar/match?match=36e0818b-58ad-11f1-89d2-fb9d3a8baf78&league=NBL). The full response also contained a separate bookmaker/market object; see the quarantine correction below. No market-derived value was used in forecasting.

#### Data-source quarantine correction

The full JSON response from the NBL match-data endpoint unexpectedly included a separate bookmaker/market object. The initial response was emitted in full before that field was recognized. No price or market-derived value was used in analysis, but this accidental exposure breaches the requested market-blind source boundary. Quarantine that endpoint from forecast evidence; specifically, do not rely on the `IN_PROGRESS` / score / Q1 9:45 snapshot above. Keep it only as a process-integrity receipt. The usable official page-level evidence is the NBL homepage's `LIVE NOW` indicator; the browser-readable Game Centre failed to load data, so exact score, clock and live lineups are unverified for this task. No forecast or retrospective was issued.

Method: local `METHOD.md` MDS-2026.09.19-v4.3 / CR-2026.09.21-3 and `RULES_BASKETBALL.md` SFA-BASKETBALL, especially BK-P2/BK-P3/BK-P4 and §5 live-state requirements. No bookmaker/fantasy/tipster material was used as forecast evidence; inadvertent API exposure is disclosed in the quarantine correction above.
## 2. Settled Logs

Previously settled cards and completed retrospectives remain in the canonical Part 5 log; this section is an index, not a second settlement record. No new settlement or retrospective was performed while creating this continuation log.

| Canonical ID | Event | Record location |
|---|---|---|
| P-482 | CPL Final - Antigua & Barbuda Falcons vs Jamaica Kingsmen | PREDICTION_LOG_COMBINED_5.md |
| P-483 | WTA Seoul - Katie Volynets vs Elvina Kalieva | PREDICTION_LOG_COMBINED_5.md |
| P-484 | WNBA - Atlanta Dream @ New York Liberty | PREDICTION_LOG_COMBINED_5.md |
| P-485 | NFL - New York Giants @ Los Angeles Rams | PREDICTION_LOG_COMBINED_5.md |
| P-486 | MLB - Minnesota Twins @ San Francisco Giants | PREDICTION_LOG_COMBINED_5.md |
| P-488 | WTA Singapore - Vivian Wolff vs Oleksandra Oliynykova | PREDICTION_LOG_COMBINED_5.md |
| P-492 | MLB - San Diego Padres @ Los Angeles Dodgers | PREDICTION_LOG_COMBINED_5.md; duplicate P-484 source claim and provisional P-490 are aliases |

P-487 remains reserved on issue-time hold for the NBL card below. P-490 remains retired/unused. Neither is a canonical prediction card.

## 3. Sources and Document Mapping

For any new forecast, first verify event identity, scheduled venue-local time and timezone, event state, contract/settlement terms, participant availability and latest lineup status. Prefer field-owner/official sources and independent reliable source lineages under SOURCES.md; disclose missing or conflicting information. Each card must list every material source, its link, the field it supports, and its retrieval/cutoff time.

| Information or update | Document destination |
|---|---|
| New frozen forecast and eventual pick-by-pick settlement/retrospective | PREDICTION_LOG_COMBINED_5.md |
| Current unresolved/final event status | GAME_LOG_STATUS_CURRENT.md |
| Cross-sport process control supported by repeated evidence | RULES_GENERAL.md, METHOD.md, or CONTROLS.md as appropriate |
| Sport-specific evidence or a supported operational rule | Relevant RULES_<SPORT>.md file |
| Source discovery, reliability or retrieval limits | SOURCES.md and, where present, DATA_SOURCE_REGISTER.md |
| Event-specific reasoning or unvalidated observation | This mini log; do not promote a one-event observation to a permanent rule |

## 4. Next Forecast Entry

P-494 is the reconciled live-issued WTA Singapore view detailed below. It is not a pregame card and is excluded from pregame metrics. The soccer request later in this log was fail-closed without a prediction or ID allocation. P-495 is next; assign it only after a complete, valid pregame card is frozen. Required fields remain: exact event and contract; venue/timezone; state and cutoff; latest starters/lineups/bench and injury/rest information; data and uncertainty; ordered ranked picks; potential winner where requested; full research reasoning; all sources and source lineages; settlement conditions; missing information; and document mapping. Do not perform a retrospective unless explicitly requested.

## P-494 — WTA Singapore Open 2026, Mirra Andreeva vs Aliaksandra Sasnovich (LIVE VIEW)

**Canonical ID:** P-494. Temporary source handle `TMP-20260923-WTA-SGP-ANDREEVA-SASNOVICH` is retired as an alias. The full original source log was preserved byte-exact before the temporary file was cleared; see the archive receipt in `archive/mini_logs/originals_2026-09-23/`.

**ID rationale:** The live view was frozen at 20:51:54 AEST, before this soccer request’s estimated 21:00 AEST start and before any soccer forecast was issued. P-493 was the prior canonical event; P-494 was the next available canonical number. The soccer request below failed the forecast gates and receives no ID. Next canonical ID: P-495.

**Horizon/status:** LIVE-ISSUED, not pregame, and excluded from pregame performance metrics. The WTA feed showed the match live at the freeze. No settlement or retrospective has been performed.

The complete source-session record follows. Its temporary-ID and “not appended” statements describe the state at the original issue time; this wrapper records the later canonical reconciliation.

---

# Prediction Mini Running Log — session 2026-09-23 (WTA Singapore, Andreeva vs Sasnovich)

**Custody.** This session is **read-only** for every existing project file (user directive, 2026-09-23). This file is the session's own running log and is the only file written. No canonical log, status register, rule file or other mini log was changed.
**ID.** Temporary ID `TMP-20260923-WTA-SGP-ANDREEVA-SASNOVICH`. The merged running log (`C:\Users\danie\Documents\Sports Research\PREDICTION_MINI_RUNNING_LOG_MERGED_P482_ONWARD.md`, read 2026-09-23 ~20:28 AEST) lists **next ID P-494**. This session does not assign it, because concurrent sessions have already produced collisions (P-484). The proposed canonical ID is **P-494, pending reconciliation**.
**Governing method (read fresh this session).** MDS-2026.09.19-v4.3 / CR-2026.09.21-3; SFA-TENNIS (RULES_TENNIS.md §9, controls 1–14); GFA-2; SCV-2026.09.19-v2. SPORTS_ONLY / MARKET_BLIND. LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE. NO VALUE DETERMINABLE.

---

## Entry 1 — score-blind prior (append-only; written 2026-09-23 ~20:44 AEST, BEFORE any live score was viewed)

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

## Entry 2 — P-494 ISSUED LIVE VIEW `TMP-20260923-WTA-SGP-ANDREEVA-SASNOVICH-LIVE-v1` (source handle retained as alias; written ~20:53 AEST)

**Status:** UNSETTLED — **LIVE-ISSUED VIEW**. This is not a pregame card. It belongs in the separate live horizon and is excluded from pregame metrics. No retrospective has been done, per the user's instruction.

### Field 1 — Identity and contract

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

### Field 2 — Evidence and exposure

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

### Field 3 — Joint distribution

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

### Field 4 — Ranked contracts (all `UNVALIDATED_SUBJECTIVE`; conditional on completion; SPORTS_ONLY / MARKET_BLIND)

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

### Field 5 — Dependence and checks

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

### Field 6 — Freeze and follow-up

- **Freeze:** the issued numbers are from the refresh computed 20:51:54 AEST on feed state 20:51:14. The live state will have moved by delivery; this view is valid only for its observation state.
- **Settlement route (G10.2).** Verified this session to return final set scores for this event:
  - S1 WTA feed: `ScoreSet*`, `ResultString`, `MatchState "F"`.
  - S4 ESPN linescores.
  - S5 Tennis.com.
  - Games = sum of set games (a tiebreak set counts as 13). Settlement needs three lineages with a terminal marker (C-FINAL3).
- **Retirement/medical time-outs:** record the set and game score at the time if one occurs (G-L23).
- **Retry trigger:** at the next session, check that S1 `MatchState = "F"` and that ResultString is present.
- **Not appended** to `PREDICTION_LOG_COMBINED_5.md` or any other existing file (read-only directive). Proposed canonical ID P-494, pending reconciliation.

### §16.8 completeness block

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

---

### Request disposition — Khonkaen United vs Royal Thai Navy FC (2026-09-23)

**Disposition:** NO FORECAST ISSUED for this soccer event; no canonical ID was allocated to the request. No retrospective performed. P-494 belongs to the earlier WTA live view; this no-issue disposition consumes no ID, and P-495 is next.

**Event/time check.** The request’s estimated 21:00 AEST start converts to 11:00 UTC. The Thai League’s official 2026/27 Chang FA Cup notice confirms the qualifying-round date window (22–23 September), but not this exact pairing or its kickoff. FotMob, SportScore, and AiScore’s timezone-explicit match details list Khonkaen United vs Siam/Royal Thai Navy at 11:00 UTC (21:00 AEST); AiScore also displays “19:00” with no timezone label. Global Sports Archive’s current-season Navy FC listing shows Khon Kaen United vs Navy FC at 13:00, also without a timezone. These records do not establish one exact kickoff. At the final state refresh, 2026-09-23 21:00:30 AEST, SportScore still showed “Upcoming,” no events and no announced lineups; FotMob and AiScore exposed no verified live-state transition. Since neither the kickoff conflict nor an official/field-owner PREGAME state was resolved, the framework’s pregame-state gate failed closed.

**Other blocking items.** No confirmed starting XI, goalkeeper, bench, or team-specific availability report was retrievable by the final check. A Scores24 page listed Khonkaen player Phanuphong Phonsa as injured, but I could not corroborate it with an official club/competition source; it is not treated as verified availability evidence. The user supplied first-half O/U 0.5 and match O/U 2.5 goal contracts, but supplied no exact corner market, line, or settlement definition. No corner exposure/rate chain or scenario branches were established. These gaps prevent an honest ordered five-pick card or potential-winner claim under `RULES_SOCCER.md` and the current pregame controls.

**Source record (retrieved 2026-09-23, approximately 20:56–21:04 AEST; final state check 21:00:30 AEST).**

- [Thai League announcement: Chang FA Cup 2026/27 qualifying-round draw and schedule window](https://thaileague.co.th/v1/news-index/%E0%B8%99%E0%B8%B3%E0%B9%81%E0%B8%A3%E0%B8%98%E0%B8%A3%E0%B8%A3%E0%B8%A1%E0%B8%8A%E0%B8%B2%E0%B8%95%E0%B8%A3%E0%B8%B2%E0%B8%8A%E0%B8%B2%E0%B8%87-%E0%B8%A3%E0%B8%A7%E0%B8%A1%E0%B8%81%E0%B8%B1%E0%B8%9A-%E0%B8%AA%E0%B8%A1%E0%B8%B2%E0%B8%84%E0%B8%A1%E0%B8%AF-%E0%B8%88%E0%B8%B1%E0%B8%94%E0%B8%9E%E0%B8%B4%E0%B8%98%E0%B8%B5%E0%B8%88%E0%B8%B1%E0%B8%9A%E0%B8%AA%E0%B8%A5%E0%B8%B2%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%81%E0%B8%82%E0%B9%88%E0%B8%87%E0%B8%82%E0%B8%B1%E0%B8%99%E0%B8%9F%E0%B8%B8%E0%B8%95%E0%B8%9A%E0%B8%AD%E0%B8%A5-%E0%B8%8A%E0%B9%89%E0%B8%B2%E0%B8%87-%E0%B9%80%E0%B8%AD%E0%B8%9F%E0%B9%80%E0%B8%AD-%E0%B8%84%E0%B8%B1%E0%B8%9E-%E0%B8%A4%E0%B8%94%E0%B8%B9%E0%B8%81%E0%B8%B2%E0%B8%A5-202627-%E0%B8%A3%E0%B8%AD%E0%B8%9A%E0%B8%84%E0%B8%B1%E0%B8%94%E0%B9%80%E0%B8%A5%E0%B8%B7%E0%B8%AD%E0%B8%81/) — official competition context/date window; not an exact match-state source.
- [FotMob event page](https://www.fotmob.com/matches/siam-navy-fc-vs-khonkaen-united-fc/403mxthy) — fixture identity, 11:00 UTC listing, venue/form; no confirmed lineup or live transition visible at final check.
- [SportScore event page](https://sportscore.com/football/match/khonkaen-united-vs-royal-thai-navy-fc/) — fixture/time cross-check; at final check page still said upcoming, no events, lineup not announced, exact ground unconfirmed on its feed. The page also displayed adjacent price fields; those were incidentally visible and not used.
- [AiScore event page](https://www.aiscore.com/live/football-khonkaen-united-vs-royal-thai-navy-fc) — fixture, 11:00 UTC in its match-info text, recent results and no verified state transition; its separate “19:00” display is timezone-ambiguous.
- [Global Sports Archive Navy FC page](https://globalsportsarchive.com/en/soccer/team/navy-fc/1210/overview) — identifies Navy FC in the 2026/27 Thai League III and lists the 23 Sep Khon Kaen fixture at 13:00 without a timezone; this conflicts with the 11:00 UTC listings and does not settle kickoff time.
- [FA Thailand Thai League 2 results page](https://fathailand.org/match-results/26/132?language=en) — shows a Navy Football Club result dated 19 Sep but the year/season context was not clear in the retrieved view; quarantined and not treated as proof of a different current club or used directionally.
- [Sanook fixture page](https://www.sanook.com/sport/1672379/) — Thai-language fixture and historical results; not used for live state or current lineups.
- [Scores24 event page](https://scores24.live/hu/soccer/m-23-09-2026-khonkaen-united-royal-thai-navy-fc) — uncorroborated Phanuphong Phonsa injury listing only; quarantined from directional use.

Method: local `METHOD.md` MDS-2026.09.19-v4.3 / CR-2026.09.21-3, `CONTROLS.md`, `RULES_SOCCER.md` identity, participant, corner-process and pregame-state gates. No prices, odds, fantasy, or tipster claims were used as evidence. A match-state page and one search-result snippet incidentally surfaced adjacent odds/market fields; they were not used or cited for any forecast reasoning. This is a request disposition only, not a scored prediction.
