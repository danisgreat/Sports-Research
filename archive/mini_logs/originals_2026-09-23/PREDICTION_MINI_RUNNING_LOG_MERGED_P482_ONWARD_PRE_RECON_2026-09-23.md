# Prediction Mini Running Log — MERGED (P-482 onward)

**Merged:** 2026-09-23 ~15:45 AEST (Australia/Melbourne). This is the **single active mini log**.
**Last updated:** 2026-09-23 ~18:00 AEST — added **P-491** (NPB Orix @ Lotte, pre-start freeze). Earlier update ~16:55 AEST — added void record for WTA Singapore R16 Mertens vs Krejčíková (walkover before issue; no ID consumed). The previous Drive version of this file is kept in `_superseded_source_logs/` with a `_v1` suffix.
**Sources merged into this file.** The originals are kept unchanged in `_superseded_source_logs/` inside this folder:

| # | Source mini log (Drive) | Original folder | Entries it held |
|---|---|---|---|
| 1 | `PREDICTION_MINI_RUNNING_LOG_P482_ONWARD.md` (created 2026-09-21) | Mini Prediction Log - P-482 onward - 2026-09-21 | P-482 (CPL final), P-483 (WTA Seoul); both unsettled in that file; user workflow brief |
| 2 | `PREDICTION_MINI_RUNNING_LOG_P484_ONWARD.md` (created 2026-09-23) | Mini Prediction Log - P-484 onward - 2026-09-23 | Padres card (claimed P-484), plus WNBA (claimed P-484), NFL (P-485), MLB MIN-SF (P-486), WTA (P-488), NPB (P-489), NBL request-only |
| 3 | `PREDICTION_MINI_RUNNING_LOG_P484_ONWARD_SETTLED_2026-09-23.md` | same folder as #2 | Settled revision of #2 (P-484 collision resolved, Padres → P-490) |
| 4 | `PREDICTION_MINI_RUNNING_LOG_P490_ONWARD.md` (Google Doc, created 2026-09-23) | Mini Prediction Log - P-490 onward | Initialised template only. **No prediction entries.** Its reserved P-490 is used by the Padres card. |

**Not merged:** the `archive/` folder's historic mini logs (e.g. `PREDICTION_MINI_LOG_12_P304_P305_SETTLED_2026-09-06.md`, `archive/mini_logs/`). They cover IDs at or below P-481 that were already reconciled into Combined Logs 1–4. Merging them would duplicate canonical records.

**Canonical authority:** `PREDICTION_LOG_COMBINED_5.md` still shows "highest P-481 / next P-482 / no Part-5 events yet". This merged log holds every P-482+ record in custody until canonical import.
**Governing method:** MDS-2026.09.19-v4.3 / CR-2026.09.21-3 (read-only).
**Operating mode:** SPORTS_ONLY / MARKET_BLIND. **Performance status:** LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE. **Value:** NO VALUE DETERMINABLE.

## Master ID register (single source of truth for P-482 onward)

| ID | Sport / event | Source log | Status | Horizon |
|---|---|---|---|---|
| **P-482** | Cricket — CPL 2026 Final, Antigua & Barbuda Falcons vs Jamaica Kingsmen | #1 | **SETTLED** (this merge) | Clean (refresh 08:54:41 AEST < 09:00 start) |
| **P-483** | Tennis — WTA Seoul R32, Volynets vs Kalieva | #1 | **SETTLED** (this merge) | START_CROSSED by 42 s (refresh 13:00:42 vs 13:00:00 scheduled) |
| **P-484** | WNBA — Atlanta Dream @ New York Liberty | #2/#3 | SETTLED | Card-stated near-tip; unverified |
| **P-485** | NFL — NY Giants @ LA Rams | #2/#3 | SETTLED | START_CROSSED (Q1 15:00) |
| **P-486** | MLB — Minnesota @ San Francisco | #2/#3 | SETTLED | Clean per card (11:30 vs 11:45) |
| **P-487** | — | — | **GAP / UNASSIGNED**. No log in Drive claims it. | — |
| **P-488** | WTA Singapore — Wolff vs Oliynykova | #2/#3 | SETTLED | Card-stated pre-match |
| **P-489** | NPB — Chunichi @ Yokohama DeNA | #2/#3 | **UNSETTLED** (starts 19:00 AEST 23 Sep) | ISSUE_HORIZON_UNVERIFIED |
| **P-490** | MLB — SD Padres @ LA Dodgers (claimed P-484; renumbered) | #2/#3 | SETTLED | START_CROSSED (12:13 vs 12:10) |
| **P-491** | NPB — Orix Buffaloes @ Chiba Lotte Marines (23 Sep, ZOZO Marine) | this file | **UNSETTLED** (starts 18:00 AEST 23 Sep) | **CLEAN** (NPB page 試合開始前 at ~17:54 AEST freeze) |
| — | NBL — Tasmania vs SE Melbourne | #2/#3 | Request-only, no forecast, no ID | — |
| — | WTA Singapore R16 — Mertens vs Krejčíková (added 2026-09-23 ~16:50 AEST) | this file | **WALKOVER before any card was issued — no forecast, no ID, VOID** | Not applicable (no card) |

**NEXT ID: P-492.** Every new prediction appends to this file only. (P-491 is the NPB Orix @ Lotte card. The earlier Mertens–Krejčíková walkover produced no forecast and consumed no ID.)

## Overlap audit performed for this merge (user-directed: "choose 1 and move the other to the next number")

- All four source logs, `PREDICTION_LOG_COMBINED_5.md`, `GAME_LOG_STATUS_CURRENT.md` (per its Part-5 pointer) and `IMPLEMENTED_CHANGES_2026_09_23` were checked for P-482+ claims.
- **One overlap found: P-484.** The Padres @ Dodgers card and the WNBA Dream @ Liberty card both claimed it.
  - **Kept at P-484:** the WNBA card.
  - **Moved to the next free number, P-490:** the Padres card. P-490 was reserved but never used in log #4.
  - Resolved 2026-09-23 ~15:20 AEST; details in §0A below.
- **No other overlaps.** P-482/P-483 appear only in log #1 (and are referenced consistently by `IMPLEMENTED_CHANGES_2026_09_23`). P-485, P-486, P-488 and P-489 each have one claimant. Log #4 holds no entries.
- **P-487** is a gap, not an overlap. No record anywhere claims it, and it is left unassigned rather than back-filled. Back-filling would make the number order disagree with issue order: P-488–P-490 were issued before any card that could take P-487. Close it administratively at canonical import.

---

## 0A. P-484 collision resolution (performed 2026-09-23 ~15:20 AEST; carried into this merge)

The user directed: "resolve the 484 and add it as a latest number".

**Collision.** Two cards claimed P-484:
- the Padres @ Dodgers card, the first local claimant;
- the Atlanta @ New York WNBA card.

**Resolution applied.**

| Card | Previous label | Resolved mini-log ID | Basis |
|---|---|---|---|
| SD Padres @ LA Dodgers (MLB gamePk 823897) | P-484 (local claim) | **P-490** | Moved to the latest free number per user direction. `PREDICTION_MINI_RUNNING_LOG_P490_ONWARD.md` (created 2026-09-23 04:59 UTC) listed P-490 as next, with no entries. P-490, P-491 and P-492 had no Drive records. P-490 is therefore unused and is consumed here. |
| Atlanta Dream @ New York Liberty (WNBA) | TMP-20260923-WNBA-ATL-NYL (card claims P-484) | **P-484** | With the Padres claim moved, P-484 has a single claimant. |
| NY Giants @ LA Rams (NFL) | TMP-20260923-NFL-NYG-LAR (claims P-485) | **P-485** | Uncontested claim, retained. |
| Minnesota @ San Francisco (MLB) | TMP-20260923-MLB-MIN-SF (claims P-486) | **P-486** | Uncontested claim, retained. |
| Wolff vs Oliynykova (WTA Singapore) | TMP-20260923-WTA-WOLFF-OLI (claims P-488) | **P-488** | Uncontested claim, retained. |
| Chunichi @ Yokohama DeNA (NPB) | TMP-20260923-NPB-CHU-DB (claims P-489) | **P-489** | Uncontested claim, retained. |
| — | P-487 | **UNASSIGNED GAP** | No card in the supplied set claims P-487. Per EXTERNAL_LOGGING_WORKFLOW and the P-490 log's continuity rule, the gap is **not** silently filled. |
| Tasmania vs SE Melbourne (NBL) | REQUEST-ONLY-NBL-TAS-SEM | **No ID** | No issued forecast exists. |

**Caveats that remain in force.**
- All numbers are **provisional mini-log IDs**.
- The canonical `PREDICTION_LOG_COMBINED_5.md` / `GAME_LOG_STATUS_CURRENT.md` snapshot still lists **P-482 as next**. `IMPLEMENTED_CHANGES_2026_09_23` records P-482/P-483 as settled, but they are not yet in canonical custody.
- At canonical import these IDs must be reconciled against Part 5, not assumed.
- Temporary aliases are preserved in each entry heading so no audit trail is lost.
- The P-490-onward mini log is superseded by this merged log, which records **P-491** as the next ID.

---

## 1. Incomplete / Unsettled Logs

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

## 2. Temporary-ID / Canonical-ID Conflict Logs

- **No entry currently needs a temporary ID.** The P-484 collision is resolved by §0A. The WNBA, NFL, MLB-MIN-SF, WTA and NPB cards now carry their own provisional numbers. Their former TMP aliases are retained in the headings.
- **Outstanding reconciliation items**, carried to canonical import:
  1. **REVIEW-P487-GAP:** P-487 unassigned. Confirm at import whether another external variant claimed it before any number is reused.
  2. **REVIEW-PART5-SNAPSHOT:** Part 5 still lists P-482 as next.
     - P-482/P-483 are settled per `IMPLEMENTED_CHANGES_2026_09_23` but are not yet in canonical custody.
     - P-484–P-490 in this log sit above them.
       - Import this log in ID order, starting at P-482.
  3. **REVIEW-HORIZON:** Several cards stay learning-only whatever their canonical number:
     - P-483 (WTA Seoul), P-485 (NFL) and P-490 (Padres) are START_CROSSED / PREGAME STATUS UNVERIFIED.
     - P-489 (NPB) is ISSUE_HORIZON_UNVERIFIED.
  4. **REVIEW-P490-PROP-BOX:** Re-capture the official MLB box-score pitching line for Michael King (gamePk 823897) at import.
     - The outs figure used below comes from two independent recaps, consistent with the official linescore.
     - The official boxscore endpoint returned a stale cached snapshot at settlement time.
  5. **REVIEW-P482-PHASE / REVIEW-P483-FINALITY:** re-capture the official CPL phase scorecard and the WTA official score at import. Settlement directions are unaffected.
  6. **Source-log retirement:** the four superseded source logs are in `_superseded_source_logs/`. Do not append to them.

---

## 3. Fully Settled Logs (ID order)

### Summary table (all settled cards in this merged log)

| ID | Event | Final | #1 | #2 | #3 | #4 | Winner call | Rank-1 | Hit@2 | NDCG@2 | TOP_OU_REVIEW | Horizon |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P-482 | CPL Final ABF v JAK | ABF by 8 wkts; JAK PP 59/2 | JAK PP O47.5 **W** | U47.5 **L** | — | — | ABF ✔ | W | Y | 0.613 | NO | Clean |
| P-483 | WTA Seoul Volynets v Kalieva | Volynets 6–3 6–0 | O19.5 **L** | Kalieva +4.5 **L** | Volynets −4.5 **W** | U19.5 **W** | Volynets ✔ | L | N | 0.000 | YES | START_CROSSED |
| P-484 | Dream @ Liberty | ATL 95–84 | U177.5 **L** | ATL −1.5 **W** | NYL +1.5 **L** | O177.5 **W** | ATL ✔ | L | Y | 0.387 | YES | Unverified |
| P-485 | Giants @ Rams | LAR 28–6 | NYG +6.5 **L** | U47.5 **W** | O47.5 **L** | LAR −6.5 **W** | LAR ✔ | L | Y | 0.387 | NO | START_CROSSED |
| P-486 | Twins @ Giants | SF 5–2 | MIN ML **L** | SF +1.5 **W** | U8.0 **W** | O8.0 **L** | MIN ✘ | L | Y | 0.387 | NO | Clean |
| P-488 | Wolff v Oliynykova | Oli 6–1 7–6 | U20.5 **W** | Wolff +4.5 **L** | Oli −4.5 **W** | O20.5 **L** | Oli ✔ | W | Y | 0.613 | NO | Card-stated pre |
| P-490 | Padres @ Dodgers | LAD 7–0 | King O14.5 outs **L** | SD +1.5 **L** | LAD ML **W** | O8.5 **L** | LAD ✔ | L | N | 0.000 | YES | START_CROSSED |

- Binary NDCG@2 = (rel₁ + rel₂/log₂3) / (1 + 1/log₂3).
- Descriptive only; not performance evidence.

---

### P-482 - Cricket - CPL 2026 Final - Antigua & Barbuda Falcons vs Jamaica Kingsmen

#### Settlement (added 2026-09-23 at merge; original card preserved verbatim below)

| Field | Record |
|---|---|
| Terminal state | **COMPLETED.** Falcons won by 8 wickets with 20 balls remaining. |
| Innings | Jamaica Kingsmen (batted first) **170/9** (20 ov). Falcons **173/2** (16.4 ov). |
| Settlement target | Kingsmen runs in the first 6 overs = **59/2**. The line was 47.5, so it cleared by 11.5. |
| Key performers | Maaz Sadaqat 100 off 49 balls (first century in a CPL final); Sufyan Moqim 4/14 (Player of the Match); Amir Jangoo 57* and Hasan Nawaz 47* in an unbeaten 89 stand |
| Result lineages | (1) ESPNcricinfo match report and live page, "Falcons won by 8 wickets (with 20 balls remaining)"; (2) Barbados Today (170/9, 173/2, 8 wickets, Moqim 4/14); (3) CricTracker (170/9, **powerplay 59/2**, 173/2). ESPN's page shares the Cricinfo feed and is not a separate lineage. **The final result passes the three-lineage gate.** |
| Phase-target lineage | 59/2 comes from **CricTracker only**. Cricinfo and ESPN full scorecards returned 403 or empty through the fetch tool. `IMPLEMENTED_CHANGES_2026_09_23` independently records "OVER 47.5 WIN". The direction is not in doubt: 59 clears 47.5 comfortably. **REVIEW-P482-PHASE:** re-capture the over-by-over total from the official CPL/Cricinfo scorecard at import. |
| Settlement sources | [Cricinfo report](https://www.cricinfo.com/series/caribbean-premier-league-2026-1534175/antigua-and-barbuda-falcons-vs-jamaica-kingsmen-final-1534217/match-report) · [Cricinfo scorecard](https://www.cricinfo.com/series/caribbean-premier-league-2026-1534175/antigua-and-barbuda-falcons-vs-jamaica-kingsmen-final-1534217/full-scorecard) · [Barbados Today](https://barbadostoday.bb/2026/09/20/antigua-and-barbuda-falcons-win-cpl-title/) · [CricTracker](https://www.crictracker.com/cricket-reviews/cpl-2026-antigua-and-barbuda-falcons-beat-jamaica-to-win-maiden-championship/) |

| Rank | Selection | Result | Settlement |
|---|---|---|---|
| #1 | Kingsmen first 6 overs OVER 47.5 (~59.9%) | 59/2 | **WIN** |
| #2 | Kingsmen first 6 overs UNDER 47.5 (forced complement) | 59/2 | LOSS |
| Winner | Antigua & Barbuda Falcons (~53%, LOW) | Falcons by 8 wickets | **CORRECT** |

**Diagnostics.**
- One distinct decision (the forced pair): 1/1.
- Rank-1 WIN. Hit@2 YES. NDCG@2 0.613. TOP_OU_REVIEW NO.
- Horizon clean: refresh 08:54:41 AEST, before the 09:00 AEST start.

**Retrospective (concise; the full audit is referenced in `IMPLEMENTED_CHANGES_2026_09_23` as `SPORTS_RESEARCH_READ_ONLY_AUDIT_2026-09-23.md`, which is not present in Drive).**
- **Why #1 won.** The card's current-role powerplay evidence (79/0 and 75/1 recent upside) was the correct regime. It rightly refused to let the older head-to-head's one-over-driven 54/1 define the centre. Two early wickets (59/2) did not stop Jamaica clearing the line.
- **What went right.**
  - The phase-target quarantine held: the line was queried after the distribution freeze.
  - The phase-participant controls were applied.
  - The winner lean (Falcons: extra rest, deeper bowling, head-to-head win) was correct. Moqim's middle-overs 4/14 capped Jamaica's total despite a century.
- **Blind spots.**
  - The confirmed XI and toss were not captured before issue. The card flagged this as a latency gap, and Jamaica batting first was not known in advance.
  - The early-wicket branch (2 down in the powerplay) still cleared, so it was not decisive. `IMPLEMENTED_CHANGES` flags "early-wicket suppression groups unlike remaining batting states" as an **experimental hypothesis**, not a rule.
- **Validation Qs.**
  - (1) XIs were not confirmed at issue, and the toss was unknown.
  - (2) Squads and roles were covered.
  - (3) Coaching was not material.
  - (4) Russell's fitness was monitored.
  - (5)/(6) CWI and CPL newsroom sources were accurate. Prefer the official CPL scorecard for phase settlement.
  - (7)/(8) The toss/XI latency is a known gap; keep the toss-window refresh (CR-2026.09.21-1).

#### Original P-482 card (preserved verbatim from source log #1)

##### P-482 — Cricket / Republic Bank CPL 2026 Final — Antigua & Barbuda Falcons vs Jamaica Kingsmen

**Status:** UNSETTLED — PREGAME FORECAST / NO RETROSPECTIVE.

**Identity / timing**
- Canonical ID: `P-482`.
- Competition: Republic Bank Caribbean Premier League 2026 Final.
- Event: Antigua & Barbuda Falcons vs Jamaica Kingsmen.
- Venue: Kensington Oval, Bridgetown, Barbados.
- Official scheduled start: 20 Sep 2026, 19:00 AST = 21 Sep 2026, 09:00 AEST (Australia/Melbourne).
- Final volatile refresh used for issuance: 21 Sep 2026, 08:54:41 AEST / 20 Sep 2026, 18:54:41 AST.
- Event state at final refresh: `PREGAME / MATCH YET TO BEGIN`. Cricket West Indies displayed no live matches and listed the final as coming up; Wisden also displayed Match Yet to Begin.
- Method / controls: `MDS-2026.09.19-v4.3 / CR-2026.09.19-4`; `SFA-CRICKET`; `SPORTS_ONLY / MARKET_BLIND`; `LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE`.

**Exact supplied contract**
- Target: Jamaica Kingsmen runs after the first **six legal overs** of their innings.
- Supplied line: 47.5 runs.
- Directions: Over 47.5 / Under 47.5.
- Half-run line: no push conditional on operator action.
- Exact operator rain/DLS/abandonment/action rules were not supplied and are not invented.
- The 47.5 threshold was quarantined until after the independent sporting distribution below was frozen.

**Toss / XI / availability gate**
- Toss was **not verified** at the final refresh.
- Confirmed XIs were **not recovered** from an authoritative accessible source before issuance. Current previews expected largely unchanged teams, but expected/probable XIs are not relabelled as confirmed.
- Jamaica's current opening combination is strongly indicated as **Maaz Sadaqat / Kirk McKenzie** by the two immediately preceding knockout chases, but final XI confirmation remains unresolved.
- Andre Russell is being monitored after leaving the field before completing his second over in Qualifier 2 and later returning to take a wicket. This matters more to the match-winner branch than to Jamaica's opening-six batting target.
- Under `RULES_CRICKET.md` near-start identity-gap control, evidence quality is capped at **LOW** rather than filling the missing toss/XI state by assumption.

**Pitch / venue / weather**
- No authoritative exact-strip report was recovered at the final refresh; strip state therefore remains `NOT_VERIFIED`, not inferred from generic venue history.
- Current Bridgetown conditions were warm/humid and partly cloudy around the pre-start window, with no basis for a deterministic signed weather adjustment. Weather remains an interruption/variance branch only.
- Kensington Oval has shown very wide playoff scoring states, so recent venue results are used as dispersion evidence rather than a one-direction pitch claim.

**Current-regime six-over evidence**
- 4 Sep vs Guyana: Jamaica **46/2** after six.
- 12 Sep vs Barbados at Kensington Oval: **50/1** after six.
- 16 Sep Eliminator vs Barbados at Kensington Oval: **79/0** after six.
- 18 Sep Qualifier 2 vs Guyana at Kensington Oval: **75/1** after six; the opening pair reached 42 in three overs and Sadaqat made 41 from 17 balls.
- Earlier 7 Aug H2H vs Antigua: Jamaica reached **54/1** after six, but the official CPL account says **28 runs came in the sixth over off Karima Gore** after an otherwise quiet powerplay. That result is discounted as a direct current-phase baseline because the opening personnel changed materially and Gore is not part of the main current probable attack.
- The recent 79/0 and 75/1 are retained as genuine current-role upside evidence, but they are not treated as a self-perpetuating streak. The 46/2 and older low states preserve the early-wicket floor.

**Independent first-six distribution — frozen before querying 47.5**
`UNVALIDATED_SUBJECTIVE` mixture; not fitted, calibrated or prospectively validated.

| Scenario | Weight | Six-over centre | SD | Mechanism |
|---|---:|---:|---:|---|
| Current-top-order breakaway | 0.35 | 65 | 10 | Sadaqat/McKenzie survive the first 2-3 overs and boundary access resembles the two knockout chases |
| Competitive central vs Falcons attack | 0.40 | 50 | 9 | One modest interruption/wicket but enough boundary scoring to remain around the high-40s/50s |
| Early-wicket suppression | 0.25 | 36 | 8 | Alzarri/Joshua James/Shamar Springer-type new-ball pressure removes an opener and compresses boundary access |

- Distribution ID: `P-482-PP6-dist-v1`.
- Distribution SHA-256: `34e8c91901d8bdfba533cd01bc852b7fa94c97ad7693888b8919bc7f348c8fa5`.
- Projected six-over mean: **51.75 runs**.
- Mixture SD: **~14.43 runs**.
- Representative central phase state: approximately **50-52/1**.
- Approximate central 50% corridor: **~41-62 runs**.

**Query of the supplied 47.5 line**
- Projected centre: **51.75**.
- Supplied line: **47.5**.
- Raw gap: **+4.25 runs**.
- Normalised gap: **~+0.29 SD**.
- Assessment: **MODEST separation, not a strong edge**.
- `P(Over 47.5) ≈ 59.9%`; `P(Under 47.5) ≈ 40.1%` from the frozen subjective mixture.
- Evidence grade: **LOW** because toss, confirmed XI and exact strip were unresolved at issue.

**Ranked supplied picks**
1. **Kingsmen first 6 overs OVER 47.5 — ~59.9% `UNVALIDATED_SUBJECTIVE` — Rank #1 / LOW evidence.**
 - Main support: the current opening regime has recently produced 50/1, 79/0 and 75/1, including two explosive Kensington knockout starts; the model centre is above 47.5 without using the line as an input.
 - Main failure path: Sadaqat or McKenzie is removed in the first 1-2 overs and the Falcons' stronger seam/spin control pushes Jamaica into a 30s/low-40s phase.
2. **Kingsmen first 6 overs UNDER 47.5 — ~40.1% — Rank #2 / forced complement.**
 - Live path: Jamaica was 46/2 as recently as 4 Sep; the old Antigua H2H was only 26 through five overs before a 28-run sixth-over spike, showing how thin the margin can be.

**Forced-pair integrity:** Over/Under 47.5 is one complementary decision conditional on action; both cannot win and there is no push at 47.5. Rank #1 is therefore the preferred side, not a hedge.

**Potential game winner**
- **Antigua & Barbuda Falcons — slight pre-toss lean, ~53% `UNVALIDATED_SUBJECTIVE` / LOW confidence.**
- Support: stronger tournament-wide/top-two campaign, direct H2H win, deeper/balanced bowling resources, a dominant Qualifier 1 win, and extra rest.
- Main failure path: Jamaica's top order carries its current Kensington form into another chase/innings, Powell closes efficiently, and Russell is fully available. The toss can materially alter this close winner view, but toss direction alone does not create a winner under the Drive method.

**Sources used**
1. Cricket West Indies official fixtures / Kensington Oval schedule — exact event, venue and 19:00 AST start; final pre-start state route: `https://www.windiescricket.com/fixtures/ground_id/1092/`.
2. Cricket West Indies official home/current schedule — final volatile state check; displayed no live matches and the CPL final as coming up: `https://www.windiescricket.com/`.
3. CPL official Newsroom, *Falcons Win Thrilling CPL Opener* — prior H2H final, Jamaica 167/7, Falcons chase win and the 28-run sixth-over mechanism: `https://cplt20.prezly.com/falcons-win-thrilling-cpl-opener`.
4. CPL official Newsroom, *Motie Magic Seals Playoffs for Tridents* — Jamaica 50/1 PowerPlay on 12 Sep: `https://cplt20.prezly.com/motie-magic-seals-playoffs-for-tridents`.
5. CPL official Newsroom, *Kingsmen Keep Hopes of Crown Alive* — Eliminator/Sadaqat current-form context: `https://cplt20.prezly.com/kingsmen-keep-hopes-of-crown-alive`.
6. CPL official Newsroom, *Kingsmen Overcome Hetmyer Hundred to Reach Final* — Qualifier 2 route/current form: `https://cplt20.prezly.com/kingsmen-overcome-hetmyer-hundred-to-reach-final`.
7. Jamaica Gleaner / CMC final preview and Qualifier 2 reports — unchanged-lineup expectation, Andre Russell monitoring, and opening-pair 42 in three overs: `https://beta2.jamaica-gleaner.com/article/sports/20260920/fairytale-finish` and `https://web5.jamaica-gleaner.com/article/sports/20260920/record-breaking-kingsmen-break-warriors`.
8. Wisden current fixture/live-score front — independent pre-start state (`Match Yet to Begin`) and final context: `https://www.wisden.com/schedule-fixtures`.
9. CricInnings 4 Sep scorecard — Jamaica 46/2 after six vs Guyana; secondary structured score route used only for that phase checkpoint.
10. Structured Bridgetown weather forecast retrieved immediately before issue — current temperature/cloud/humidity/precipitation context; used only as environment/uncertainty evidence, not to force direction.
11. Sports Research Drive — `METHOD.md`, `RULES_GENERAL.md`, `RULES_CRICKET.md`, `SOURCES.md`, active mini-log instructions — governing methodology and source/phase rules.

**Source firewall**
- No sportsbook odds, implied probabilities, line movement, betting picks, tipsters, fantasy/DFS projections or market consensus were used as predictive inputs.
- The user-supplied 47.5 line was queried only after `P-482-PP6-dist-v1` was frozen.

**Document mapping / candidate learning**
- `RULES_CRICKET.md`: existing phase-participant, retained-resource, near-start identity-gap and streak-persistence controls were applied; **no new permanent rule proposed from this one event**.
- `DATA_SOURCE_REGISTER.md`: current CPL official newsroom + CWI schedule remain preferred primary routes; exact confirmed-XI/toss retrieval remains a latency gap to monitor.
- Prediction log: preserve the contrast between Jamaica's current-role 79/0 and 75/1 upside and the older H2H's one-over-driven 54/1 so future phase models do not treat all >47.5 results as equivalent mechanisms.
- Settlement route: official CPL/CWI scorecard or legality-reconciled delivery record for Jamaica's first six legal overs, plus the governing three-lineage terminal-state gate.

---

### P-483 - Tennis - WTA Seoul R32 - Katie Volynets vs Elvina Kalieva

#### Settlement (added 2026-09-23 at merge; original card preserved verbatim below)

| Field | Record |
|---|---|
| Terminal state | **COMPLETED** (1 h 12 min) |
| Score | **Volynets d. Kalieva 6–3, 6–0.** Total **12 games**; margin **Volynets +9 games** |
| Result lineages | (1) TennisTemple match page; (2) Tennis Majors match page (lists the round as "third round", which conflicts with the WTA draw's R32; the score agrees); (3) `IMPLEMENTED_CHANGES_2026_09_23` recorded outcomes (Over LOSS, Kalieva +4.5 LOSS, Volynets −4.5 WIN, Under WIN), consistent with the score. The WTA exact score page was not re-fetched in this pass. **REVIEW-P483-FINALITY** (already listed in `IMPLEMENTED_CHANGES`): re-capture the WTA official score at import. The direction of every row is unaffected. |
| Sources | [TennisTemple](https://en.tennistemple.com/match/volynets-kalieva-seoul-2026/9482014/) · [Tennis Majors](https://www.tennismajors.com/matches/wta/korea-open-2026-women-s-singles/katie-volynets-vs-elvina-kalieva) |

| Rank | Selection | Result | Settlement |
|---|---|---|---|
| #1 | Total games OVER 19.5 (~65.2%) | 12 games | **LOSS** |
| #2 | Kalieva +4.5 games (~58.4%) | lost by 9 | **LOSS** |
| #3 | Volynets −4.5 games (~41.6%) | won by 9 | WIN |
| #4 | Total games UNDER 19.5 (~34.8%) | 12 games | WIN |
| Winner | Volynets (~62%) | Volynets 2–0 | **CORRECT** |

**Diagnostics.**
- Two distinct decisions (total pair, handicap pair): 0/2 on the preferred sides.
- Rank-1 LOSS. Hit@2 NO. Wins@2 0/2. NDCG@2 0.000. **TOP_OU_REVIEW YES.**
- Horizon: **START_CROSSED** by 42 seconds (refresh 13:00:42 AEST vs 13:00:00 scheduled). Tennis order-of-play times are often "not before", so play may not have begun, but the pregame freeze is not certified.

**Rank-1 failure review (enhanced).**
- **Why #1.** The card gave 39% to a deciding set, plus close straight-set scores (7–5, 6–4). It argued that Kalieva's improved 2026 service/hold profile and three-set resilience made a Volynets rout "less dominant than ranking alone suggests".
- **What happened.** The rout branch happened: 6–3, 6–0. The card's own named failure mode for Kalieva, double-fault volatility, is consistent with a bagel set. Per-match serve stats were not recovered, so that attribution is not asserted.
- **Justified at issue?** Partly. The winner read and the return-pressure evidence (the Philadelphia final: 56% of points won, 6/10 break points converted) pointed to Volynets dominance. Yet both top-ranked rows depended on Kalieva staying close.
- **Shared driver, disclosed by the card.** The #1 Over and #2 Kalieva +4.5 shared one driver, Kalieva staying competitive. Unlike P-490, the card **did** disclose the coupling:
  - it labelled the top two positively dependent;
  - it printed Fréchet bounds (joint success 23.6–58.4%; both-fail 0–34.8%);
  - it named the shared-failure family as "decisive Volynets straight-set control".
- **The key finding: the modal branch defeated both top picks.** The card's single heaviest branch was "Volynets decisive 2–0, 6–3 6–3" at 30%. That score is 18 games with a 6-game margin, so it fails **both** #1 (Over 19.5) and #2 (Kalieva +4.5). The actual 6–3 6–0 was a more extreme version of that modal branch. The top two were ranked on the aggregate of the five other branches against the single most likely one. That is mathematically legitimate in a mixture, but fragile when the other branches are each individually smaller.
- **Rule that should have caught it.** No existing rule requires flagging this. RULES_TENNIS's shared score tree was followed, and so was G-L10's coupling disclosure. **New candidate (C-MODAL-BRANCH-CHECK, disclosure only):** when the single most likely scenario branch defeats Rank #1 (and especially both top two), print that fact beside the ranking. A lower evidence label (LEAN rather than SUPPORTED) should be considered. No coefficient is proposed.
- **New rule?** No permanent rule. This is the candidate above plus the tennis two-set margin candidate; it is **n=2 underdog +4.5 losses in consecutive WTA cards** (P-483, P-488).

**Top-two review.** Neither won. The ordering (Over above Kalieva +4.5) was internally consistent and its coupling was disclosed. The loss came from the modal branch: the card's 30% decisive-Volynets family (plus its extreme tail, 6–0 sets) defeated both picks. Volynets −4.5 would rank higher only if its own supported likelihood justified it, and the card's 41.6% did not. So this is primarily a **distribution-shape issue**: the decisive-rout family had too little mass against a player whose serve is volatile (48 aces and 56 double faults in 126 service games).

**Over/under review.**
- The line of 19.5 needed roughly a close two-setter or a third set. The card's total leaned on 39% deciding-set mass.
- Missing indicators:
  - Kalieva's **per-match** hold % and double-fault distribution (not season totals);
  - Volynets' return-games-won against comparable servers;
  - the conditional probability of a bagel or breadstick set.
- The outdoor hard court in Seoul was not a driver.
- `IMPLEMENTED_CHANGES` §8 already proposes adding serve/return numerators and denominators to RULES_TENNIS. **This result supports that proposal.**

**What went right.**
- Winner correct.
- The WTA exact-match page was a high-value identity/state lane.
- Thresholds were quarantined until after the freeze.
- The retirement/walkover UNKNOWN_DEFINITION was stated honestly.

**Validation Qs.**
- (1)/(2) Not applicable to individual tennis; the draw and status were confirmed.
- (3) Coaching not material.
- (4) Availability checked; no withdrawal marker.
- (5) Sources current.
- (6) Prefer the WTA match-stats page plus per-match serve logs.
- (7)/(8) Blind spots: rout-branch mass and serve volatility per match; the start was crossed by 42 seconds. Account for these via PR-1 (hard freeze) and the tennis margin candidate.

#### Original P-483 card (preserved verbatim from source log #1)

##### P-483 — Tennis / WTA Seoul — Katie Volynets vs Elvina Kalieva

**Status:** UNSETTLED — PREGAME FORECAST / NO RETROSPECTIVE.

**Identity / timing**
- Canonical ID: `P-483`.
- Competition: Korea Open / WTA Seoul 2026, WTA 250, Round of 32.
- Event: Katie Volynets vs Elvina Kalieva.
- Venue: Seoul Olympic Park Tennis Center, Seoul, South Korea; Show Court 1.
- Surface: outdoor hard court.
- Official scheduled start: 21 Sep 2026, 12:00 KST (`Asia/Seoul`, UTC+9) = 21 Sep 2026, 13:00 AEST (`Australia/Melbourne`, UTC+10); no calendar-date rollover.
- Final event-state refresh used for issuance: 21 Sep 2026, 13:00:42 AEST / 12:00:42 KST. WTA exact-match page remained `Upcoming` with no score; L'Equipe and MyKhel independently also displayed the match as upcoming.
- Method / controls: `MDS-2026.09.19-v4.3 / CR-2026.09.19-4`; `SFA-TENNIS`; `SPORTS_ONLY / MARKET_BLIND`; `LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE`.

**Exact supplied contracts**
- Volynets -4.5 total games.
- Kalieva +4.5 total games.
- Match total Over 19.5 games.
- Match total Under 19.5 games.
- The user-supplied thresholds were quarantined until after the independent match-score tree below was frozen.
- Both half-game pairs are exact complements conditional on operator action; there is no push at a half-game line.
- Exact operator retirement/walkover/action rules were not supplied. Operator settlement therefore remains `UNKNOWN_DEFINITION / NO VALUE DETERMINABLE`; research probabilities below refer to a normally completed best-of-three match.

**Participant / availability / format state**
- WTA exact-event page confirms both players in the Round of 32 draw, with no score and no walkover/withdrawal marker at final refresh.
- Katie Volynets: WTA rank #77, right-handed, age 24, career high #56.
- Elvina Kalieva: WTA rank #113, right-handed, age 23, career high/current high #113.
- Head-to-head: 0-0; no prior direct match to weight.
- No credible current injury, retirement-warning or withdrawal report was recovered for either player in the final research pass. This is not relabelled as a medical clearance; it means no verified availability downgrade was found.
- Standard WTA singles format: best of three sets, 7-point tiebreak in each set including the decider under the current WTA ruleset.

**Current hard-court evidence and opponent-strength reconciliation**
- Volynets won the Philadelphia WTA 125 hard-court title immediately before the US Open, beating Tereza Valentova 6-3, 7-5 in the final after straight-set wins over Oksana Selekhmeteva, Mananchaya Sawangkaew, Mia Pohankova and Cody Wong.
- In that Philadelphia final, Volynets won 56% of total points and converted 6/10 break points; the result is direct evidence of current return pressure rather than only a ranking prior.
- Volynets then lost 5-7, 1-6 to world #6 Linda Noskova at the US Open. USTA's official account notes Volynets had led 5-2 in the first set before Noskova won 11 of the final 12 games. The defeat is therefore opponent-strength adjusted rather than treated as an unexplained form collapse.
- Kalieva has made a substantial 2026 level jump. WTA records 35-22 YTD and a career-high #113; she reached her first WTA semifinal in Memphis after wins over Zeynep Sonmez and Peyton Stearns and qualified for her first US Open main draw through three consecutive three-setters.
- The last US Open qualifying win over Vendula Valdmannova was 5-7, 6-4, 6-4 in 2h53; Kalieva won 61.3% of service points and 42.1% of return points in the WTA match record. This supports a real deciding-set/close-match branch.
- Since that qualifying run, Kalieva lost US Open R1 to Lanlana Tararudee in three sets and Guadalajara R1 to Kayla Day 7-6(9), 6-4. These losses reduce any temptation to make her the outright favourite, but neither is evidence that her 2026 level gain has disappeared.

**Serve / return mechanism**
WTA's exact-match 2026 comparison reports:
- Volynets: 73.9% first serves in; 58.2% first-serve points won; 44.2% second-serve points won; 54.5% service points won; 58.9% service games won; 51.9% break points saved.
- Kalieva: 58.6% first serves in; 64.5% first-serve points won; 44.1% second-serve points won; 56.1% service points won; 62.7% service games won; 52.5% break points saved.
- Kalieva's serve is higher-variance: 48 aces and 56 double faults in 126 service games versus Volynets' 40 aces and 40 double faults in 270 service games on the WTA comparison. Raw totals are not treated as equal-exposure rates.
- Interpretation: Volynets has the stronger ranking/current-title/return-pressure case, but Kalieva's current service-point and hold fields plus her three-set resilience keep a meaningful close-match branch. That is why the model can prefer Volynets to win while simultaneously preferring Kalieva +4.5 over Volynets -4.5.

**Conditions**
- Seoul pre-match weather: sunny, about 27 C around the research window, with a daily high around 31 C and no rain signal in the current forecast.
- Weather is used only as outdoor load/variance context. No unsupported signed court-speed adjustment is made from temperature alone.

**Independent joint match-score tree — frozen before querying ±4.5 / 19.5**
`UNVALIDATED_SUBJECTIVE`; this is an explicit scenario distribution, not a fitted/calibrated tennis model.

| Branch | Weight | Representative score | Main mechanism |
|---|---:|---|---|
| Volynets decisive 2-0 | 30% | 6-3, 6-3 | sustained return pressure + lower-error baseline creates repeated break separation |
| Volynets close 2-0 | 13% | 7-5, 6-4 | Volynets wins pressure games but Kalieva's serve prevents large separation |
| Volynets 2-1 | 19% | 6-4, 3-6, 6-3 | Kalieva's serve/first-strike level earns a set; Volynets' return consistency wins the decider |
| Kalieva 2-1 | 20% | 6-4, 3-6, 6-4 (Kalieva perspective) | Kalieva carries current service quality and defensive resilience through a close decider |
| Kalieva close 2-0 | 12% | 7-5, 6-4 | Volynets fails to convert return pressure and Kalieva wins the key break-point games |
| Kalieva decisive 2-0 | 6% | 6-3, 6-3 | Volynets' service vulnerability is repeatedly exposed while Kalieva avoids the double-fault tail |

- Distribution ID: `P-483-TEN-matchtree-v1`.
- Distribution SHA-256: `e4802b6c6551d1a2ca558417b5f5171e24f30fc914bd053a7ea2cde4957fb6f9`.
- Match-winner mass: Volynets **62%**, Kalieva **38%**.
- Weighted representative total from the six branch score families: **23.1 games**.
- Weighted representative Volynets game margin: **+1.66 games**.
- Straight-set mass: 61%; three-set mass: 39%. Straight-set does not automatically mean Under 19.5 because close 7-5/6-4-type two-set states clear 19.5.

**Queries of supplied lines after freeze**
- `P(Over 19.5) ~= 65.2%`; `P(Under 19.5) ~= 34.8%`.
- `P(Kalieva +4.5) ~= 58.4%`; `P(Volynets -4.5) ~= 41.6%`.
- These exact-contract figures are derived from branch-specific within-state spread/total uncertainty around the printed score families; they are `UNVALIDATED_SUBJECTIVE`, not calibrated probabilities.

**Ranked supplied picks**
1. **TOTAL GAMES OVER 19.5 — ~65.2% `UNVALIDATED_SUBJECTIVE` — Rank #1.**
 - Support: 39% deciding-set mass, plus close straight-set states such as 7-5/6-4; Kalieva's improved service/hold profile and three-set resilience make a complete Volynets rout less dominant than ranking alone suggests.
 - Main failure: Volynets repeatedly breaks Kalieva's volatile second-serve/double-fault branch and closes something like 6-2, 6-3 or 6-3, 6-3.
2. **KALIEVA +4.5 GAMES — ~58.4% — Rank #2.**
 - Support: wins outright in all Kalieva-win branches and survives many close Volynets wins/three-set Volynets wins. Kalieva's 2026 step-up and current service points/hold numbers give that pathway substance.
 - Main failure: Volynets' return pressure creates two-break set separation and wins by 5+ total games.
3. **VOLYNETS -4.5 GAMES — ~41.6% — Rank #3.**
 - Support: Volynets is the match favourite in the tree and her Philadelphia title run shows a credible straight-set separation branch.
 - Why below Kalieva +4.5: winning the match is not enough; Volynets needs 5+ game separation, and several of her ordinary win states fail that stricter condition.
4. **TOTAL GAMES UNDER 19.5 — ~34.8% — Rank #4.**
 - Live path: a clean one-sided 6-2/6-3 or 6-3/6-3 result for either player.
 - Why last: the shared tree gives substantial mass to a deciding set and to close straight sets that clear 20 games.

**Potential match winner**
- **Katie Volynets — ~62% `UNVALIDATED_SUBJECTIVE` / moderate sports lean.**
- Primary reasons: stronger current ranking/level prior, recent hard-court WTA125 title, demonstrated return pressure in Philadelphia, and evidence that the US Open loss came against elite #6 Noskova after Volynets initially led rather than from a broad loss of form.
- Main failure: Kalieva's 2026 improvement is genuine; if her first-serve conversion holds and her double-fault volatility stays contained, her service edge plus defensive three-set tolerance can flip the match.

**Scoreline coherence / dependence**
- A representative top-two joint-success state is **Volynets 6-4, 3-6, 6-3**: Over 19.5 and Kalieva +4.5 both win while Volynets still wins the match. This is why the winner and handicap directions are not contradictory.
- Top two are positively dependent through close/two-break-limited and deciding-set states.
- Exact top-two joint probability is `JOINT_UNQUANTIFIED`; Frechet bounds from the frozen marginals: **23.6% to 58.4%**.
- Both top two fail only when the match lands Under 19.5 **and** Volynets covers -4.5; dominant shared-failure family: decisive Volynets straight-set control. From the marginals alone, the Frechet bound on both-fail mass is **0% to 34.8%**.
- Forced pairs: Over/Under 19.5 is one decision; Volynets -4.5/Kalieva +4.5 is one decision. Opposite sides are not counted as independent confirmation.

**Material sources**
1. WTA exact match page — Volynets vs Kalieva, Korea Open R32 — identity, Show Court 1, hard surface, scheduled venue time, current upcoming state, H2H 0-0, rankings and 2026 serve comparison: `https://www.wtatennis.com/tournaments/1024/seoul/2026/scores/LS029`.
2. WTA Korea Open overview — tournament dates, outdoor hard surface, Seoul Olympic Park Tennis Center and WTA level: `https://www.wtatennis.com/tournaments/1024/seoul/2026`.
3. WTA Katie Volynets record/profile — current ranking, career high and current-season record/profile context: `https://www.wtatennis.com/players/327391/katie-volynets/record`.
4. WTA Philadelphia final — Volynets d. Valentova 6-3, 7-5; detailed serve/return and break-point process: `https://www.wtatennis.com/tournaments/1166/philadelphia-125/2026/scores/LS001`.
5. WTA Volynets vs Noskova US Open R1 — 5-7, 1-6, detailed match stats: `https://www.wtatennis.com/tournaments/905/us-open/2026/scores/LS74124880`.
6. USTA / US Open official Noskova-Volynets report — opponent-strength/game-script context; Volynets led 5-2 before Noskova won 11 of the last 12 games: `https://www.usopen.org/amp/en_US/news/articles/2026-08-31/linda_noskova_roars_back_for_2026_us_open_round_1_win.html`.
7. WTA Elvina Kalieva record/profile — current #113, 35-22 YTD and tournament record: `https://www.wtatennis.com/players/327834/-/record`.
8. WTA US Open feature on 2026 debutants — Kalieva's 2026 level rise, five Top-100 wins, Memphis semifinal and three consecutive three-set qualifying wins: WTA article `US Open 2026's Grand Slam debuts`.
9. WTA Kalieva vs Valdmannova US Open qualifying — 5-7, 6-4, 6-4 and detailed service/return process: `https://www.wtatennis.com/tournaments/905/us-open/2026/scores/RS74106774`.
10. WTA Kalieva vs Kayla Day / Kalieva record — Guadalajara R32 loss 7-6(9), 6-4 and current hard-court context.
11. L'Equipe exact match page — independent current event-state, court/surface, ranking and recent-result cross-check.
12. MyKhel exact match scoreboard — independent current `UPCOMING` state and scheduled instant cross-check.
13. Structured Seoul weather feed — pre-match temperature/precipitation context for outdoor hard conditions.
14. Sports Research Drive — `METHOD.md`, `RULES_GENERAL.md`, `RULES_TENNIS.md`, `SOURCES.md`, `DATA_SOURCE_REGISTER.md`, `SCORING_AND_VALIDATION.md` — governing methodology and source/firewall rules.

**Source firewall / limitations**
- No sportsbook odds, implied probabilities, betting predictions, line movement, tipsters, fantasy/DFS projections or market consensus were used as predictive inputs.
- Search results that mixed sports data with betting/prediction content were excluded from the evidence set.
- No direct H2H exists.
- Exact operator retirement/void terms remain unknown; research probabilities assume normal completion and do not imply bet value.
- No fitted or calibrated tennis model exists in the Drive framework; every printed probability is explicitly `UNVALIDATED_SUBJECTIVE`.

**Document mapping / candidate observations**
- `RULES_TENNIS.md`: retain current rule that winner, game handicap and total must come from one shared score tree; P-483 demonstrates a coherent Volynets-winner + Kalieva-+4.5 + Over pathway without requiring a new rule.
- `DATA_SOURCE_REGISTER.md` / `SOURCES.md`: WTA exact match page is a high-value current lane because it exposes identity, status, surface, rankings and same-page 2026 serve comparison.
- `LEARNING_REGISTER.md`: observation only — Kalieva's service profile is materially more volatile (high ace and double-fault frequency per exposed service game) than raw ace/DF totals imply; no coefficient or permanent adjustment is proposed from one card.
- No retrospective performed, per user instruction.

---

### P-484 - WNBA - Atlanta Dream @ New York Liberty (alias TMP-20260923-WNBA-ATL-NYL)

**Original card and forecast preserved:** `C:\Users\danie\.codex\attachments\7526db47-c50c-4fbf-91ec-69820861257e\Pasted text.txt`.
- The card reports a near-tip refresh, with the WNBA event page still showing Upcoming.
- Its numerical probabilities were explicitly UNVALIDATED_SUBJECTIVE estimates.
- The forecast included no odds.

**Final result:** Atlanta Dream 95, New York Liberty 84; total 179.
- The WNBA event page confirms the fixture identity.
- The Atlanta and Liberty recaps, the AP recap and the CBS Atlanta report agree on the result.
- The AP report records the 41–38 halftime score and Atlanta's 73–62 lead after three. It also says New York played in Toronto the day before.
- Atlanta scored 32 in the third quarter. New York did not get closer than eight in the fourth.
- Sources: [Atlanta recap](https://dream.wnba.com/news/balanced-attack-propels-dream-to-important-road-win), [Liberty recap](https://liberty.wnba.com/news/liberty-fall-to-dream-95-84), [AP recap](https://www.foxsports.com/articles/wnba/atlanta-dream-beat-the-new-york-liberty-9584-close-in-on-a-top4-wnba-seed), [CBS Atlanta report](https://www.cbsnews.com/atlanta/news/jordin-canada-scores-19-andel-reese-records-another-double-double-as-dream-beat-liberty-95-84/).

| Original rank | As-issued selection | Result | Settlement |
|---|---|---|---|
| #1 | Under 177.5 | 179 points | LOSS by 1.5 |
| #2 | Atlanta Dream -1.5 | Atlanta by 11 | WIN |
| #3 | New York Liberty +1.5 | Atlanta by 11 | LOSS |
| #4 | Over 177.5 | 179 points | WIN |
| Winner | Atlanta Dream, ~58% | Atlanta won | CORRECT |

**Decision and ranking diagnostics.**
- Two distinct decisions were offered: Atlanta -1.5 won; the preferred total Under lost (1/2).
- Rank-1 loss: YES. Hit@2: YES. Wins@2: 1/2. Standard binary NDCG@2: 0.387.
- TOP_OU_REVIEW: YES; the highest-ranked total was Under and it did not win.
- The Under and Over rows are one forced binary total decision, not two independent successes or failures.
- Metrics are descriptive only.

**Pick-by-pick review.**

- **#1 Under 177.5 — loss.**
  - The pregame centre was 176.7, only 0.8 below the line, and the card correctly labelled the edge low confidence.
  - The game finished 179: a small miss in a near-line scoring distribution, not a large centre error.
  - Atlanta's 32-point third quarter was the decisive scoring burst: the Dream reached 73 while New York reached 62 entering the fourth.
  - Atlanta's balanced scoring and turnover pressure supported its offense. CBS records 11 New York turnovers converted into 14 Atlanta points, against only four Dream turnovers.
  - The forecast had already listed transition possessions, Reese's offensive boards, late fouling and overtime as Under kill paths. No overtime occurred.
  - Pace and possession count were not recovered. The review therefore attributes the miss to the documented third-quarter scoring cluster, not to an unverified claim that the whole game was unusually fast.
- **#2 Atlanta -1.5 — win.**
  - The card's read of Atlanta's stronger season profile, defensive pressure, rebounding and rest position was directionally right.
  - The margin was much larger than the central estimate of about +2.4.
  - Canada scored 19, Reese 18, Bonner 17 off the bench, Howard 16 and Gray 14. Five Dream players reached double figures and Atlanta pulled away after halftime.
  - The pregame report had no authoritative same-day starting five for either team, so this win does not validate its unconfirmed rotation assumptions.
- **#3 New York +1.5 — loss.**
  - The Liberty's home-defense and star-core path did not keep the game within one possession late.
  - Stewart led New York with 27 and Jones had 18, but Atlanta's third-quarter run produced an 11-point final margin.
  - The card's central expectation was that New York could hold Atlanta near the mid-80s; the Dream scored 95.
  - New York's major absences were identified before the game, but the report lacked a final confirmed lineup.
- **#4 Over 177.5 — win.** The total crossed the number by 1.5. This is the complement of the losing Under and supplies no independent second total result.
- **Projected winner — Atlanta — correct.** The winner call held even though the margin was far larger than the central score. As the card itself noted, an outright win and a -1.5 cover are separate outcomes.

**Rank-1 and top-two review.**
- Under was ranked first because the estimated total centre sat below the threshold. The card cited both teams' defense, an 80–81 possession baseline and New York's back-to-back.
- That was internally coherent, but the advantage over Atlanta -1.5 was negligible: Under ~54% against the spread at ~53–54%.
- With the total centre only 0.8 below the line, there was no robust basis for a stable ordinal distinction.
- On frozen pregame information, the card did disclose the principal scoring failure branches and kept confidence low.
- The result alone does not justify moving Atlanta -1.5 above the Under in future cards. A useful improvement is to show ranking uncertainty when estimated probabilities overlap at this precision.
- Exactly one of the top two won.

**Total-market review.**
- The miss was narrow and the predicted centre was close.
- The report covered pace, defense, rest, the prior matchup and several scoring tails.
- It lacked a verified game-day lineup and a quantified transition/turnover scoring component. The third-quarter burst was a realised high-scoring branch.
- One game does not support a permanent basketball-total adjustment.
- Keep the low-confidence label. Next time, obtain same-day actives and starters, then disclose a score/pace distribution around the line rather than letting a 0.8-point centre gap look rank-determinative.

**Validation and source audit.**

| Required question | Finding |
|---|---|
| Both confirmed starting lineups obtained before issue? | No. The card explicitly says it only had each team's latest prior-game five and could not verify tonight's starting fives. |
| Bench/reserve or rotation information? | Not sufficiently. The report discussed team rebounding and rotation context but did not confirm expected game-day reserve roles. Bonner's 17 off the bench (CBS, postgame) is outcome evidence, not pregame knowledge. |
| Coaching information? | No game-specific tactical plan is established in the forecast. Atlanta coach Karl Smesko later described broad contribution and second-half execution. Do not convert the postgame quote into a pregame assumption. |
| Injuries/availability adequately checked? | Partly. The card identified Brionna Jones as out for the season and Sabally's long-term absence, but day-of starters were not confirmed. |
| Original sources accurate/current? | Event and result sources are clear. The forecast attachment's inline content-reference tokens are not usable URLs, which limits independent review of its inputs and timestamps. |
| Better future sources? | Prefer the WNBA game-day lineup and box score, official team availability reports, and a distinct independent recap for result verification. Do not count multiple pages backed by the same feed as independent lineages. |
| Meaningful blind spots? | Yes: unconfirmed lineup, a near-line total, unmeasured game-day rotation, and the chance that turnover pressure creates efficient extra offense rather than only lower opponent scoring. |
| Future treatment | Keep missing lineup status explicit, widen uncertainty, and calculate turnover-to-transition points alongside pace and half-court efficiency. |

**Connection to Drive lessons (Phase 5).**
- The TOP_OU_REVIEW trigger (L-20260919-12 / METHOD §7) fired correctly and is complete.
- The near-tie ordinal is a recurrence of the "probabilities overlapping at the stated precision" issue. It is the same pattern as the P-486 Twins 59% vs 57% gap below.
- One-off variance plus a known missing-lineup blind spot. No new rule.

**Learning status.** WNBA Rank-1 and top-total scrutiny complete. The Under's small central edge was not robust to a one-quarter offensive burst, while Atlanta's side case benefited from distributed scoring. No permanent rule change.

---

### P-485 - NFL - New York Giants @ Los Angeles Rams (alias TMP-20260923-NFL-NYG-LAR)

**Original card preserved:** `C:\Users\danie\.codex\attachments\316c1cf1-1085-4205-914d-32b02772d84a\Pasted text.txt`.
- Ranks: Giants +6.5 (~61%), Under 47.5 (~54%), Over (~46%), Rams -6.5 (~39%).
- Projects the Rams to win (~64%), representative score 24–20.
- The estimates are explicitly UNVALIDATED_SUBJECTIVE.

**Event result and timing gate.**
- NFL Game Center confirms Final, Rams 28–6. The Rams scored seven in every quarter; the Giants scored six in total.
- NFL, Rams and Giants reports agree on the event and result. The three result lineages are NFL, Associated Press and the Los Angeles Times.
- Sources: [NFL Game Center](https://www.nfl.com/games/giants-at-rams-2026-reg-2), [Rams recap](https://www.therams.com/news/game-recap-rams-defeat-giants-28-6-on-monday-night-football), [Giants recap](https://www.giants.com/news/instant-analysis-giants-fall-to-rams-28-6), [AP report via WRAL](https://www.wral.com/news/ap/c991e-giants-qb-jaxson-dart-exits-with-knee-injury-on-first-series-vs-rams/), [Los Angeles Times report](https://www.latimes.com/sports/rams/story/2026-09-21-rams-defeat-giants-aaron-donald-return).
- **Timing problem.** The card says "final pre-kickoff" but also reports the game at Q1 15:00. A 15:00 first-quarter clock means kickoff has occurred, and no score at that instant does not prove a pregame freeze.
- Marked START_CROSSED / PREGAME STATUS UNVERIFIED. This result is for learning and cannot enter a valid pregame performance sample.

| Original rank | As-issued selection | Result | Settlement |
|---|---|---|---|
| #1 | Giants +6.5 | Lost by 22 | LOSS |
| #2 | Under 47.5 | Total 34 | WIN |
| #3 | Over 47.5 | Total 34 | LOSS |
| #4 | Rams -6.5 | Rams won by 22 | WIN |
| Winner | Rams, ~64% | Rams won | CORRECT |

**Decision and ranking diagnostics.**
- Two distinct decisions: Giants +6.5 lost; the preferred Under 47.5 won (1/2).
- Rank-1 loss: YES. Hit@2: YES. Wins@2: 1/2. Standard binary NDCG@2: 0.387.
- TOP_OU_REVIEW: NO; the highest-ranked total was Under at rank #2 and it won.
- Descriptive learning only, with the issue horizon unverified.

**Pick-by-pick review.**

- **#1 Giants +6.5 — loss.**
  - The card ranked the cushion first because it projected a competitive 24–20 game.
  - It treated Nacua and Whittington as unavailable, the Giants' primary offensive line as active, and Dart's Week 1 form as a counterweight to the Rams' team-quality edge.
  - The forecast explicitly named a 7–14 point Rams win as its main failure path.
  - The game diverged sharply. Dart injured his knee at the end of New York's opening drive and did not return; Winston replaced him. The Giants scored two field goals and no touchdowns.
  - Stafford completed 22/31 for 327 yards and four touchdowns, and Adams had 195 receiving yards and two touchdowns.
  - The inactive/active checks were relevant, but the in-game quarterback injury was not knowable before kickoff.
  - This was a real variance event layered on a model that did not give enough probability mass to the Rams' high-scoring outcome.
- **#2 Under 47.5 — win.**
  - Thirty-four points finished 13.5 below the line.
  - The forecast's Under case included Nacua's absence, a potential run/clock-control script and a central score below the line.
  - The Rams scored 28, four above the card's estimate, but the Giants' six points more than offset that.
  - This supports the total direction on this result, not the specific scoring mechanism or its unvalidated 54%.
- **#3 Over 47.5 — loss.** Several listed Over pathways existed, but New York's quarterback loss and low output prevented them from combining with Rams production. This row is the complement of the Under.
- **#4 Rams -6.5 — win.**
  - Los Angeles covered by a wide margin.
  - The card preferred the Rams outright but ranked the larger-margin branch last: its central margin was only about +4.35, and New York's offense was expected to stay intact.
  - The result came from a different state after Dart's injury, combined with an exceptional Stafford/Adams performance.
- **Projected winner — Rams — correct.** The ~64% winner lean did not imply a high probability of covering -6.5, and the card correctly kept those contracts separate.

**Rank-1 and top-two review.**
- The underdog Rank-1 was coherent only if the card was actually frozen pregame.
- The injury is not a fair hindsight criticism of a pregame process. But the Q1 15:00 timestamp defeats the card's own pre-kickoff claim until an independent issue timestamp proves otherwise.
- Existing start-crossing controls should prevent it being treated as a certified pregame forecast.
- Conditional on a genuine pregame freeze, the report recognised both the cornerback-loss failure path and a 27+ point Rams branch. The miss is largely explained by the opening-drive QB injury and realised Rams efficiency.
- No new "avoid underdogs" rule is warranted.
- One of the top two won (Under).

**Total review.**
- The Under won comfortably, but the realised total was driven by New York scoring only six after Dart's injury, not by both offenses staying near the 24–20 representative state.
- The card correctly separated the total from the Rams' win probability, and identified the Rams' offensive tail and the Giants' secondary tail.
- The game was at SoFi Stadium. The card reports a fixed roof and climate-controlled conditions, so weather was not a material variable.

**Validation and source audit.**

| Required question | Finding |
|---|---|
| Both starting lineups and QB status obtained before issue? | Official inactive lists were reportedly published and Dart was not inactive. The Q1 15:00 state leaves the issue horizon unresolved; the record does not prove the forecast preceded kickoff. |
| Bench/reserve or replacement information? | The card discussed depth and inactive players. Winston's entry followed Dart's in-game injury and was not a pregame availability omission. |
| Coaching information? | Team-quality and coaching context appeared in the winner rationale; no game-specific tactical adjustment drove the pick. Postgame reports describe the outcome, and no coaching change is needed to explain the injury. |
| Injuries/availability adequately checked? | Known inactives were checked per the card. Dart's knee injury occurred during play and was not a known pregame absence. |
| Sources accurate/current? | NFL Game Center and both team recaps agree on final status and result. The forecast's content-reference markers prevent independent replay of each cited pregame feed and exact cutoff. |
| Better future sources? | Preserve the official inactive-list URLs and a true pre-kickoff timestamp. Use NFL Game Center plus each team's final report for settlement. |
| Meaningful blind spots? | The main unresolved issue is timing. Conditional on pregame issuance, the forecast named the Rams scoring path but underweighted its joint high tail, and had no way to anticipate a first-drive QB injury. |
| Future treatment | Enforce an event-time freeze before kickoff, separate post-kickoff no-score refreshes, and keep injury-shock losses out of pregame process attribution unless the injury risk was known. |

**Connection to Drive lessons (Phase 5).**
- The start-crossing control (README CR-4 gate; RULES_GENERAL start-crossing) exists and was **not followed at issue**.
- This is the **second** START_CROSSED card in this log (with P-490), and P-489 also has an issue-horizon conflict. That makes a recurring process pattern: see §4.
- The QB injury is one-off variance.

**Learning status.** Cannot be used as a clean pregame test until the timestamp conflict is reconciled. No permanent football rule change from this result.

---

### P-486 - MLB - Minnesota Twins @ San Francisco Giants (alias TMP-20260923-MLB-MIN-SF)

**Original card preserved:** `C:\Users\danie\.codex\attachments\ffd9702e-2f1c-4a3e-8a2f-422b92cb696b\Pasted text.txt`.
- It reports an 11:30 AEST final research pass, about 15 minutes before the scheduled start.
- Rows: Twins ML (~59%); Giants +1.5 (~57%); Under 8.0 (~47%, ~10% push); Over 8.0 (~43%, ~10% push). Representative score Twins 4–3.
- The card explicitly says San Francisco's final lineup was not reliably confirmed in the captured official source.

**Final result:** San Francisco 5, Minnesota 2 after nine innings; total 7.
- MLB's game page shows 10 Giants hits, four Twins hits and no errors.
- Matthews took the loss after five earned runs in five innings, with nine strikeouts.
- AP and NBC Sports Bay Area also report the 5–2 final.
- Sources: [MLB game record](https://www.mlb.com/video/game/823169), [AP recap hosted by Fox Sports](https://www.foxsports.com/articles/mlb/drew-gilberts-homer-and-2run-single-lead-giants-past-twins-52-to-end-3game-losing-streak), [NBC Sports Bay Area recap](https://www.nbcsportsbayarea.com/mlb/san-francisco-giants/drew-gilbert-bo-davidson-blade-tidwell-twins/1965184/).

| Original rank | As-issued selection | Result | Settlement |
|---|---|---|---|
| #1 | Minnesota Twins moneyline | Minnesota lost 2–5 | LOSS |
| #2 | San Francisco Giants +1.5 | San Francisco won | WIN |
| #3 | Under 8.0 runs | 7 total | WIN; no push |
| #4 | Over 8.0 runs | 7 total | LOSS; no push |
| Winner | Minnesota Twins, ~59% | Minnesota lost | INCORRECT |

**Decision and ranking diagnostics.**
- Three distinct decisions: Twins moneyline lost, Giants +1.5 won, and the preferred Under won (2/3).
- Twins ML and Giants +1.5 are not complementary contracts. The Under/Over pair is complementary and counts as one decision.
- Rank-1 loss: YES. Hit@2: YES. Wins@2: 1/2. Standard binary NDCG@2: 0.387.
- TOP_OU_REVIEW: NO; the highest-ranked total was Under at rank #3 and it won.

**Pick-by-pick review.**

- **#1 Twins moneyline — loss.**
  - Minnesota was ranked first on four grounds: Matthews was seen as the more established, deeper starter; SF was missing key bats; Minnesota had a fresher leverage bullpen; and the captured Twins order looked stronger than the uncertain Giants order.
  - The report explicitly named the failure path: Matthews' road/first-inning command problem, a Giants hitter capitalising, Tidwell repeating a strong start, and SF taking a lead to its home bullpen.
  - That path substantially happened. SF scored twice in the first on Brett Harris's single, added two in the second on Drew Gilbert's single, and Gilbert homered in the fifth.
  - Matthews allowed five earned runs in five innings despite nine strikeouts.
  - The forecast described the risk correctly but gave the Minnesota-win branch too much probability relative to that known early-inning downside and the unresolved SF lineup.
- **#2 Giants +1.5 — win.**
  - San Francisco won outright, so the cushion covered.
  - The park/run-line analysis was consistent with a protective plus-run contract, but it expected a tighter family of scores.
  - The 5–2 result was one of the card's named kill paths for Minnesota ML and still comfortably won Giants +1.5. It is not evidence that the game was close.
- **#3 Under 8.0 — win.**
  - Seven runs cash the Under by one; the integer line did not push.
  - Oracle Park and the recognised absences supported suppression.
  - The total stayed below eight even though San Francisco scored five, because Minnesota managed only two.
- **#4 Over 8.0 — loss.** Seven runs did not reach nine, so the Over lost without a push. It is the complement of the Under row.
- **Projected winner — Minnesota — incorrect.** The distribution leaned Twins despite listing Matthews' early-inning failure as its primary adverse state.

**Rank-1 and top-two review.**
- Twins ML (~59%) exceeded Giants +1.5 (~57%) by only two estimated points.
- The ranking can be defended as a small preference on the frozen starter/bullpen evidence, but it was fragile. The SF lineup uncertainty should have widened the uncertainty around that ordinal choice.
- The first two innings followed the forecast's explicit kill path. That does not prove the 59% was irrational ex ante. It does show that naming a path is not enough unless its weight shows up in the distribution.
- One of the top two won.

**Total review.**
- The line was eight, with material push probability assigned. Seven was a clean Under.
- Scoring was asymmetric: the Giants beat their 3.3 central estimate while the Twins fell well below 4.2.
- That asymmetry explains how the total call can be right while the projected winner is wrong.
- One game does not justify changing park or pitcher coefficients.

**Validation and source audit.**

| Required question | Finding |
|---|---|
| Both batting orders confirmed before issue? | No. Minnesota's order was captured; the card explicitly records San Francisco's order as unresolved in the official feed. |
| Bench/reserve and bullpen information? | Bullpens and workload were discussed. The full final SF order and substitutions were not verified at issue. Bo Davidson's debut hit and first-inning run is outcome evidence and cannot be backfilled. |
| Manager information? | Team/manager context was present, but no tactical move was central to the forecast. |
| Injuries/availability adequately checked? | Key absences and Minnesota's out list were covered. The main information gap was the final SF batting order. |
| Sources accurate/current? | MLB's game record, AP and NBC Sports Bay Area agree on the final. |
| Better future sources? | Keep the exact MLB gamePk, the final batting-order page and the official lineup feed, with capture time. Use AP or local reporting only as corroboration. |
| Meaningful blind spots? | Yes: unconfirmed SF lineup, high variance in Matthews' early innings, and the chance that one early cluster decides a low-total game before Minnesota's bullpen edge matters. |
| Future treatment | Reduce winner-ranking certainty when an opponent order is missing. Model starter first-five and bullpen states separately. Record which lineup version was known at the freeze. |

**Connection to Drive lessons (Phase 5).**
- This is a direct recurrence of **L-075**: a named early-hook/short-start kill path sits beside a ranked row that assumes the starter's normal workload (RULES_BASEBALL §8.5, P-297 origin).
- It is also a recurrence of **G-L9 / RULES_GENERAL §16.5(e)**: named kill paths without mass.
- **BB-P2** (both posted orders) was not met, so under that precondition the moneyline row should have been capped at FORCED RANK / MEDIUM-LOW. **Existing rules were inadequately applied; no new rule is needed.**

**Learning status.** A calibration question, not a new baseball rule. The protective run line and the total remain separate decisions under the scoring method.

---

### P-488 - WTA Singapore - Vivian Wolff vs Oleksandra Oliynykova (alias TMP-20260923-WTA-WOLFF-OLI)

**Original card preserved:** `C:\Users\danie\.codex\attachments\4c5e0ff5-985b-46f3-afc0-e560f91b1e90\Pasted text.txt`.
- It reports a final pre-match refresh around 12:56 PM AEST, while the WTA match page showed Upcoming.
- Rows: Under 20.5 (~60%); Wolff +4.5 (~58%); Oliynykova -4.5 (~42%); Over 20.5 (~40%). Oliynykova to win ~74%, representative score 6–4, 6–4.
- Probabilities are labelled UNVALIDATED_SUBJECTIVE.

**Final result:** Oliynykova defeated Wolff 6–1, 7–6; total 20 games; six-game margin (Oliynykova 13, Wolff 7).
- The WTA score page, Tennis.com, TennisDB and MyKhel confirm completion, set score and winner.
- TennisDB identifies a balldontlie_wta provider key.
- **Tiebreak-point discrepancy:** the WTA score page and Tennis.com/MyKhel show 7–1, while a WTA news recap says 7–5. It does not change winner, game total or margin, so no market is affected.
- Sources: [WTA score page](https://www.wtatennis.com/tournaments/1152/singapore/2026/scores/LS022), [Tennis.com](https://www.tennis.com/tournaments/singapore-open/matches/v-wolff-vs-o-oliynykova-2026-09-22), [TennisDB](https://tennis-db.com/wta/matches/balldontlie_wta%3A16975394/oleksandra-oliynykova-vs-vivian-wolff), [MyKhel](https://www.mykhel.com/tennis/singapore-tennis-open-presented-by-bnp-paribas-2026-womens-singles-1-32-final-live-scoreboard-435624/), [WTA news recap](https://www.wtatennis.com/news/4579876/anisimova-pulls-out-of-singapore-with-left-wrist-injury).

| Original rank | As-issued selection | Result | Settlement |
|---|---|---|---|
| #1 | Under 20.5 total games | 20 games | WIN |
| #2 | Vivian Wolff +4.5 games | Lost by 6 games | LOSS |
| #3 | Oleksandra Oliynykova -4.5 games | Won by 6 games | WIN |
| #4 | Over 20.5 total games | 20 games | LOSS |
| Winner | Oliynykova, ~74% | Oliynykova won 2–0 | CORRECT |

**Decision and ranking diagnostics.**
- Two distinct decisions: total Under (win) and Wolff +4.5 (loss), 1/2.
- Rank-1 loss: NO. Hit@2: YES. Wins@2: 1/2. NDCG@2: 0.613.
- TOP_OU_REVIEW: NO.
- Under/Over and +4.5/-4.5 are forced complements within their own pairs.

**Pick-by-pick review.**

- **#1 Under 20.5 — win.**
  - The representative 6–4, 6–4 totals exactly 20, and the match also finished on 20.
  - The two-set branch occurred. The first set was far more one-sided than projected; the second went to a tiebreak.
  - The total landed only half a game under the line, so the correct direction does not validate 60% on its own.
- **#2 Wolff +4.5 — loss.**
  - The margin was six games, 1.5 beyond the handicap.
  - The card correctly named the main failure mechanism, Oliynykova attacking Wolff's second serve, but put more probability on a close straight-set match.
  - Official WTA stats: Wolff won 12/34 second-serve points (35.3%) against Oliynykova's 14/21 (66.7%). Oliynykova converted 4 of 7 break points; Wolff 1 of 4.
  - Tennis.com reports different serve totals, so its figures are not used for this causal claim.
  - The 6–1 opening set created a five-game gap and the tiebreak set added one more.
  - The loss came from the exact vulnerability the card named, at a size that broke the cushion.
- **#3 Oliynykova -4.5 — win.** The six-game win covered. The winner and second-serve reads were sound; the row ranked lower because the card gave substantial mass to a close two-set branch.
- **#4 Over 20.5 — loss.** Twenty games stayed below the half-point line. The tiebreak added points, not a game.
- **Projected winner — Oliynykova — correct.** The 74% figure remains subjective and unvalidated.

**Top-two review.**
- Rank #1 won and rank #2 lost.
- The ordering is defensible from the original score tree: the predicted two-set centre supported the Under, while Wolff +4.5 depended on a narrower close-score branch.
- The result exposes a joint-distribution issue: a straight-set match can stay under 20.5 while the favourite still covers -4.5.
- Future tennis cards should estimate set count, total games and game margin conditional on two sets, rather than treating "straight sets" as enough support for the underdog handicap.

**Total and match review.** The indoor hard-court context was relevant and weather was not. Winner and total were right; the handicap was not. The total landed exactly on the representative game count, but the game split between players was asymmetric.

**Validation and source audit.**

| Required question | Finding |
|---|---|
| Starting lineups confirmed? | Not applicable to individual tennis. Both scheduled participants and event status were identified by the official WTA page. |
| Bench/reserves or rotation? | Not applicable. |
| Coaching information? | No coach-specific input was needed or documented. |
| Injury/rest/availability checked? | Recent workload and participation were reviewed, and both players were reported as entered. No medical information was established. |
| Sources accurate/current? | WTA score page, Tennis.com and TennisDB agree on event, set score and winner. The WTA news recap conflicts on tiebreak points, and Tennis.com service stats differ from WTA totals; neither changes any market. |
| Better future sources? | Use the tournament/WTA live score as the field-owner record, plus independent score publishers. Retain the raw set/game score and document tiebreak differences separately. |
| Meaningful blind spots? | Yes: the distribution underweighted a lopsided first set followed by one competitive set. |
| Future treatment | Keep the joint score tree and report conditional game-margin quantiles for two-set outcomes. |

**Connection to Drive lessons (Phase 5).**
- `IMPLEMENTED_CHANGES_2026_09_23` records **P-483**, where the Kalieva **+4.5 handicap lost** while Volynets -4.5 won. That is **two consecutive WTA cards** in which the underdog +4.5 games handicap lost, while the favourite won in straight sets. The Under won in both, but it was the preferred total only in P-488; P-483's preferred total, the Over, lost.
- This is an **emerging sport-specific pattern (n=2)**. It is not yet a rule.
- It connects to the RULES_TENNIS action already proposed in `IMPLEMENTED_CHANGES_2026_09_23` §8: match-by-match serve/return numerators and denominators, including second-serve wins.

**Learning status.** Correct winner and total, failed cushion. Tennis two-set margin geometry is a candidate for testing (§4).

---

### P-490 - MLB - San Diego Padres @ Los Angeles Dodgers (formerly local claim P-484; renumbered 2026-09-23)

#### Identity, state and settlement status

| Field | Record |
|---|---|
| Event | MLB regular season, SD Padres @ LA Dodgers, series game 1 of 3. UNIQLO Field at Dodger Stadium (open air, grass). MLB gamePk **823897**. |
| Scheduled start | 2026-09-22 19:10 PDT (UTC−7) = 2026-09-23 02:10 UTC = **2026-09-23 12:10 AEST** (Australia/Melbourne) |
| Issue-time statement (preserved) | The author reported a final verification at 12:13 AEST, after the scheduled start, and said no live information was used. |
| Issue horizon | **START_CROSSED / PREGAME STATUS UNVERIFIED.** Learning-only whatever its canonical number. The first run scored in the bottom of the 2nd, so no score existed at 12:13 AEST, but a score-free state does not certify a pregame freeze. |
| Terminal state | **FINAL / "Game Over"** — MLB Stats API schedule endpoint (`/api/v1/schedule?gamePk=823897&hydrate=linescore,decisions`), retrieved 2026-09-23 ~15:10 AEST |
| Final score | **Los Angeles Dodgers 7, San Diego Padres 0**. Total 7; margin LAD +7. Nine innings; bottom 9th not played. |
| Linescore | SD 000 000 000 – 0 R, 5 H, 0 E. LAD 040 101 10x – 7 R, 9 H, 1 E. |
| Decisions | W: Justin Wrobleski. L: Michael King. |
| Result lineages (CR-4 gate) | (1) MLB Stats API official schedule/linescore/decisions; (2) Dodgers Digest recap (independent blog); (3) True Blue LA recap (SB Nation, independent). Dodger Blue via Yardbarker also agrees but is a syndicated copy: one further lineage, not two. **Gate passed: three independent lineages agree on event, terminal state and 7–0.** |
| Prop field (King outs) | King recorded **12 outs (4.0 IP)**. Dodgers Digest says King finished the 4th ("That was it for King") and Wandy Peralta entered in the bottom 5th. Dodger Blue (Yardbarker) describes the same run sequence. It is consistent with the official linescore: all 5 LAD runs came in the 2nd and 4th. The official box-score pitching line could not be captured (stale cached endpoint), so it is logged as **REVIEW-P490-PROP-BOX**. The outcome (12 < 14.5) does not depend on the unresolved detail. |
| Operator terms | None supplied. NO VALUE DETERMINABLE. Listed-pitcher/action terms unknown; King did start, so no void issue arises on research-line grading. |

#### Settlement

| Original rank | As-issued selection | Result | Settlement |
|---|---|---|---|
| #1 | Michael King 15+ pitching outs / Over 14.5 outs | 12 outs (4.0 IP) | **LOSS** |
| #2 | Padres +1.5 runs | Lost by 7 | **LOSS** |
| #3 | Dodgers moneyline | Dodgers won 7–0 | **WIN** |
| #4 | Combined runs Over 8.5 | 7 runs | **LOSS** |
| Rejected side (not a pick) | Under 8.5 | 7 runs | Would have won; not graded as a pick |
| Projected winner | LA Dodgers (narrow lean) | Dodgers won | **CORRECT** |

**Decision and ranking diagnostics.**
- Four distinct decisions: King outs, Padres +1.5, Dodgers ML and the game total. Padres +1.5 and Dodgers ML are **not** complements; a Dodgers one-run win would have cashed both. Result: **1/4**.
- Rank-1 loss: **YES**. Hit@2: **NO**. Wins@2: **0/2**. NDCG@2: **0.000**.
- **TOP_OU_REVIEW: YES**, triggered twice. The highest-ranked over/under row was the King outs Over at #1, and the only game-total row, Over 8.5 at #4, also lost (METHOD §7; L-20260919-12).
- No probabilities were attached, so no Brier/log score is computed.

#### What happened in the game (evidence-supported only)

- **1st–2nd.**
  - King retired the side in order in the 1st and got the first two outs of the 2nd.
  - Teoscar Hernández and Josue De Paula singled, then King hit Andy Pages (first PA back from IL).
  - Tommy Edman and Mookie Betts walked with the bases loaded, forcing in two runs. Freddie Freeman singled in two more: **LAD 4–0**.
- **3rd–4th.**
  - A scoreless 3rd. In the 4th, a two-out Betts ground-rule double was followed by a Freeman RBI single: **5–0**.
  - King's night ended after 4.0 IP.
- **Padres relief.**
  - Peralta pitched the 5th–6th. In the 6th, De Paula tripled with help from a Tatis misplay and was called out at home on a sacrifice fly the Dodgers could not challenge. Edman then hit a solo HR: **6–0**.
  - Griffin Canning allowed Will Smith's solo HR in the 7th: **7–0**.
- **Dodgers pitching.**
  - A bullpen game: Stewart (1st), Wrobleski (2nd, the win), Treinen (3rd), Sasaki (4th, first appearance off IL), Díaz (5th), Hurt (6th–7th), Vesia (8th), Dreyer (9th).
  - Eight pitchers combined on a shutout: 9 IP, 5 H, 0 R, 10 K, 2 BB (Dodger Blue/Yardbarker).
  - The Padres left 8 on base.
- **Why King exited after four innings is not established.** Two explanations fit the evidence:
  - **performance** — 5 runs, a hit batter and two bases-loaded walks; Dodgers Digest wrote that he "didn't look right";
  - **workload management** — protecting a pitcher San Diego had lined up for a possible must-win finale.
  - His pitch count was not recovered. Neither explanation is asserted as fact.

#### Pick-by-pick causal review

**#1 King Over 14.5 outs — LOSS (12 outs).**

*Why it was ranked first:*
- King's last five starts were all six-plus innings (7, 6, 6, 7, 6).
- He was moved up to pitch on normal rest.
- The manager called him the preferred arm for a possible must-win finale.
- The card judged that the xERA warning affected runs more than length.

*What was correct:*
- King started as confirmed.
- He was on normal rest, with no announced pitch limit.

*What was incorrect or under-weighted:*
- **Hook depends on runs allowed.** The card treated reaching the 5th as largely independent of run prevention. RULES_BASEBALL §2 and BB-S2 require hook point and batters faced to be modelled *separately* from runs allowed, but not as independent of them. In practice a 5-run, walk-heavy start is the main driver of an early hook. The card's own xERA gap (4.36 xERA vs ~3.00 ERA; FIP ~4.16 per Dodgers Digest) was evidence of a fatter run tail, and that tail feeds straight into the outs row.
- **Opponent-specific exit history was knowable and omitted.**
  - Dodgers Digest's pregame preview reported King's three 2026 starts against LA: 7 shutout innings (May); chased in the 5th on June 28 after 4⅓ IP (four runs, four walks); and six shutout innings on July 3 before unravelling in the 7th.
  - So **1 of 3 prior starts against this opponent ended below 15 outs**, the June 28 start at 13 outs.
  - The L5 window used by the card was mostly against weaker or non-contending opponents, and CBS/Field Level Media noted the Dodgers' recent run had not come against playoff teams.
- **Short recency window used as the primary exposure base.** RULES_BASEBALL §8.8 requires the starter's L5/L10/L15/L20 innings, batters faced, pitches and hook points. Control 24 requires a per-start log that includes walks. The card printed innings and ERA only, for L5 only. RECENCY_AND_REBOUND.md (control R-1) found that short windows predict monotonically worse than longer baselines in MLB 2026.
- **Bidirectional mechanism not represented.** Lining King up for the finale was read only as "supports a normal workload." The same fact also creates an incentive to pull him early once the game is lost, to protect a must-win start. G-L2 / RULES_GENERAL §16.5(b) requires both signs of a mechanism.

*Driver classification:*
- **Mainly predictable-process weakness plus in-game performance variance.**
- The early exit was a within-distribution outcome for a pitcher facing the league's highest-scoring offense (780 runs).
- Whether it was performance-driven or management-driven cannot be determined from the recovered evidence.
- It is **not** an unforeseeable shock.

**#2 Padres +1.5 — LOSS (lost by 7).**
- *Ranked on:* King compressing LA's early scoring, San Diego's hot offense (40 runs in L5, 71 in L10) and the Dodgers' bullpen-game structure.
- *Correct:* the card explicitly warned that "bullpen game = Padres advantage" would be an analytical error. That was right: eight Dodgers relievers allowed nothing. It also listed "Padres lose by 2+" as "very real".
- *Incorrect:*
  - The Padres' offensive form was shrunk only verbally, not in the numbers. The run came against Colorado and Miami.
  - The cushion rested on King's early suppression, which failed. A 5–0 deficit after four innings breaks a +1.5 cushion almost regardless of the bullpens.
- *Existing rules applied inadequately:*
  - RULES_BASEBALL §8.6 override 3: before a positive run line outranks the opposing side, state which BB-B4 one-sided separation scores are excluded. The 7–0 shutout is exactly the BB-B4 family (opponent floor 0–2), and the card did not exclude it with evidence.
  - Control 21: favourite separation and run clusters are linked.
  - The 2026-09-15(b) baseball note records underdog +1.5 rows going **4 W / 6 L**. This adds a further cushion loss, albeit at rank #2.

**#3 Dodgers ML — WIN.**
- The card's season-level reasoning held: 96–60, +193 run differential, 50–28 at home, and a strong lineup even without Ohtani.
- The same-day Dodgers order (Betts, Freeman, Smith, Muncy, Tucker, T. Hernández, De Paula, Pages, Edman) matched the order that played.
- Freeman drove in three runs. De Paula (two hits, a triple and a walk) and the returning Pages both contributed, as the lineup read implied.
- This is the one supplied row that aligned with the card's own stated winner lean.

**#4 Over 8.5 — LOSS (7 runs).**
- The Over needed both offenses. All seven runs came from the Dodgers and the Padres were shut out.
- The card had correctly listed LA's bullpen quality (a staff 2.90 ERA over the last 10 games per Bleacher Nation; the card cited 28 runs allowed in 10) and Stewart's strong expected-contact numbers as Under mechanisms.
- It still put the Over narrowly ahead, mainly on San Diego's recency-inflated offense and generic "relief transition" branches.
- RULES_BASEBALL §8.6 override 1 applies: a short start or bullpen game raises uncertainty but is **not directional**.
- The rejected Under would have won by 1.5.

**Projected winner — Dodgers — CORRECT.** The card expected something near a one-run game; the actual game was a one-sided BB-B4 separation.

#### Rank-1 failure review (enhanced, METHOD §7)

1. **Why #1.** Five consecutive 6+ inning starts, normal rest, stated manager trust, and the argument that an outs row needs only survival, not dominance.
2. **Justified on information available at issue?** Partly.
   - The row type (a starter-length floor) is legitimately often the most robust row on a card.
   - But the evidence was a short, opponent-unadjusted window.
   - The opponent-specific exit record (a 13-out start against LAD on June 28) was published pregame in a source used at settlement and likely findable at issue.
   - No batters-faced, pitch-count or walk-rate log was printed (control 24 / §8.8), and the hook-given-runs dependence was argued away rather than modelled.
3. **Should another row have ranked higher?**
   - The card attached no probabilities, so no counterfactual order can be asserted numerically.
   - Qualitatively, Dodgers ML (the card's own winner lean, strongest season-level evidence) had a stronger evidence base than a single-pitcher length prop against the league's best offense.
   - The rules do not require any particular order, but G23.1 requires rank by supported marginal likelihood. The #1 support was thinner than presented.
4. **Missed, under- or over-weighted variables.**
   - Missed: King vs LAD exit history; hook-on-runs dependence; the bidirectional finale incentive.
   - Over-weighted: the L5 innings streak.
   - Under-weighted: the xERA/FIP gap as a length risk.
5. **Should an existing rule have prevented it?** Yes, in part:
   - RULES_BASEBALL §8.4 (pitcher props from BB-S2: hook risk and lineup turn count, not season rate);
   - §8.8 (starter L5–L20 including BF, pitches and hook point);
   - control 24 (per-start log with walks);
   - R-1 (recency revises a rate only through a named mechanism).
   - Applying them would have exposed the thinner evidence and likely lowered the row's confidence, but not necessarily its rank.
6. **New rule warranted?** No permanent rule from one game. A **candidate** (not promoted) is registered in §4: *C-P490-SP-OUTS-OPP*, an opponent-specific exit record and hook-given-runs branch before a starter-length row may rank #1 against a top-quartile offense.

#### Top-two review

- Pick #1 lost; pick #2 lost; neither succeeded.
- Both rows depended on **one shared driver**: King suppressing the Dodgers early. Once King conceded four in the 2nd, both rows were effectively decided together.
- The top two were therefore **positively dependent**, and the card did not print P(R1 ∧ R2) or its coupling label (RULES_BASEBALL §8.7 additions: "`P(R1 ∧ R2)` with its coupling label (G-L10)").
- **Improvement.** When the top two share a single causal driver, disclose the coupling. Consider whether a row with a different driver (here Dodgers ML) gives better top-two robustness — only where its own supported likelihood justifies it, not to hedge.

#### Over/under review (TOP_OU_REVIEW — both O/U rows lost)

- **Scoring environment.** Dodger Stadium in near-neutral weather (card: ~21°C, clear; not re-verified at settlement). No weather-driven total signal, correctly stated.
- **Pace/tempo.** Not a baseball driver; N/A.
- **Offensive/defensive efficiency.** LA's run prevention was excellent entering the game and carried on through eight relievers. SD's offensive surge was opponent-inflated.
- **Lineups/absences.** Ohtani's absence was correctly noted. The Padres order was captured only from a Reddit game-thread feed (SOURCES S-1: social media is not an admissible lane) and never confirmed officially. It matched the order that played, but that is luck, not verification.
- **Distribution around the line.** 8.5 needs nine runs. With one team shut out, the Under was the realised family. The card named "Over narrowly" but never built the component budget at the line (G20, the §8.4 game-total row) at the opponent floor, centre and ordinary high.
- **Variance sensitivity.** High on both sides because of the bullpen game. Under §8.6 override 1 that is width, not direction.
- **Sport-specific indicators missing.** The two-team component budget at 8.5; the Padres' floor against a bullpen of mostly strong leverage arms; King's own run tail (xERA/FIP).
- **Verdict.** The Over lean came mainly from recency-inflated SD scoring and non-directional bullpen-game uncertainty. No new totals rule is proposed. **Controls that were not applied:** R-1, §8.6 override 1, and the §8.4 component budget.
- **King outs Over (#1).** Covered in the Rank-1 review above.

#### What went right

- **Winner call and lineup read.** The Dodgers were the right winner lean, and the same-day Dodgers order was captured correctly despite the stale MLB endpoint.
- **Bullpen-game warning.** "Bullpen game = Padres advantage would be an analytical mistake" was exactly right.
- **Transparent integrity section.** The card disclosed stale official endpoints, the TBD starter and the unconfirmed Padres order instead of hiding them. Keep this.
- **No two-sided hedge.** The card declined to add Under 8.5 as a second totals pick, consistent with the no-mechanical-both-sides rule.
- **Rival cushion decomposition.** The card correctly noted that a Dodgers one-run win cashes both Padres +1.5 and Dodgers ML (§8.4 worked slate).

#### Blind spots and future handling

| Blind spot | Future handling |
|---|---|
| Opponent-specific starter exit history (King vs LAD: 7.0 / 4.1 / 6+ IP in 2026) | Print the starter's current-season starts against this opponent, with IP/BF/pitches/BB, beside the L5–L20 log (§8.8; control 24). |
| Hook dependence on runs allowed | For any starter-length row, show the conditional branch: exit before 5 IP given 3+ early runs, with mass derived from his own log (BB-S2; G-L9). |
| Bidirectional rotation-alignment incentive | When a starter is lined up for a later must-win game, record both signs: normal workload *and* an earlier hook once the game is lost (G-L2). |
| Recency-inflated opponent offense | Opponent-adjust or shrink L5/L10 scoring toward the season baseline in the numbers, not only in words (R-1; control 13). |
| Padres batting order from a social-media feed | Use MLB Stats API `hydrate=lineups` / boxscore `battingOrder` (README 2026-09-19 lanes) and record `LINEUPS_NOT_YET_PUBLISHED` vs `RETRIEVAL_MISS`. Never use Reddit as a lineup source (S-1). |
| Padres bench/bullpen and injuries not recorded | Record both benches and relief ladders (G14.2). CBS listed Adam, Estrada, Sheets, Andujar and Musgrove among Padres absences; the card recorded none of them. |
| Start-crossed issuance | Final refresh must finish before scheduled first pitch. After it, the card is labelled LIVE/START_CROSSED at issue, not afterwards (see §4 process item). |

#### Mandatory validation questions

1. **Confirmed starting lineups for both teams?**
   - Not from an official source.
   - Dodgers: same-day secondary (Dodgers Nation), correct in hindsight.
   - Padres: a Reddit/game-feed copy only, inadmissible under S-1, also correct in hindsight.
   - The official MLB lineup endpoint was stale at capture.
2. **Bench/reserve/rotation?**
   - Dodgers: the bullpen-game plan and Sasaki's return were known and discussed.
   - Padres: the bench and relief ladder were not recorded.
3. **Coaching/manager information?** Yes. Stammen on King's finale alignment; Roberts on the bullpen-game plan (per CBS/FLM preview).
4. **Injuries, rest, late changes adequately checked?**
   - Partly. Ohtani's IL status and Pages' return were captured. Padres injuries were not recorded.
   - King was on normal rest. No pitch cap was announced; none was found.
5. **Original sources accurate and current?**
   - Mostly accurate on facts.
   - **Defect:** the cited Baseball Savant link for King's xERA has the parameter `season=2023`, so attributing the 3.00 ERA / 4.36 xERA to 2026 cannot be verified from the cited URL.
   - MLB probable/lineup pages were stale; StatMuse windows were not independently reconciled.
6. **Better sources available?**
   - MLB Stats API `schedule?hydrate=probablePitcher,lineups` and the boxscore `battingOrder`/`bench`/`bullpen` fields.
   - Baseball Savant with an explicit `season=2026` parameter.
   - The pitcher's MLB game log (IP/BF/pitches/BB per start).
7. **Blind spots?** Yes, see the table above.
8. **How to account for them?** Apply RULES_BASEBALL §8.8, control 24, BB-S2, G-L2 and R-1 as written. Enforce the pre-start freeze. Candidate C-P490-SP-OUTS-OPP for testing.

*Not treated as pregame failures (hindsight-only):* King's in-game command problems in the 2nd; the umpire call and missing challenge on De Paula at home; the exact reason for his exit.

#### Connection to Drive lessons (Phase 5)

| Lesson / rule | Status in P-490 |
|---|---|
| RECENCY_AND_REBOUND.md control **R-1** (short windows predict worse; recency revises a rate only via a named mechanism) | **Inadequately applied**: an L5 innings streak was the primary Rank-1 basis. Mirrors README's reclassification of P-453 (a Rank #1 resting on three-start form). **Recurring.** |
| RULES_BASEBALL control **24** / §8.8 (per-start log incl. BB, BF, pitches, hook point, L5–L20) | **Not applied.** AGGREGATE_ONLY-style input. |
| RULES_BASEBALL §8.6 override **3** / control **17** (exclude BB-B4 separation before a +1.5 outranks the opposing side) | **Not applied.** The 7–0 shutout is BB-B4. |
| Baseball underdog +1.5 record (2026-09-15(b): 4 W / 6 L at rank #1) | One more cushion loss (rank #2). **Recurring sport-specific pattern.** |
| **G-L10** (P(R1 ∧ R2) coupling label) | **Not printed.** Top two shared one driver. |
| **L-075** (named kill path next to a ranked row that ignores it) | **Recurring**: "Padres lose by 2+ very real" was named and then out-ranked. Same pattern as P-486. |
| Start-crossing control (README CR-4) | **Not followed at issue.** Recurring with P-485 and P-489. |
| S-1 (social media not admissible) | **Breached for the lineup lane**, although the content was accurate. |

**Learning status.** Full settlement complete; START_CROSSED; LEARNING_ONLY. Outcome: 1 of 4 decisions won; winner correct; Rank-1 and top-two both failed. The primary process lesson is the evidence base for starter-length props, not variance alone.

#### Settlement sources (P-490)

| Source | Link / record | Field ownership | Access state / time | Contribution | Limitation |
|---|---|---|---|---|---|
| MLB Stats API (official) | `https://statsapi.mlb.com/api/v1/schedule?sportId=1&gamePk=823897&hydrate=linescore,decisions` | Field owner: state, score, linescore, decisions | OPENED, ~15:10 AEST 23 Sep | Final/Game Over; 7–0; linescore; W Wrobleski / L King | `feed/live` and `boxscore` endpoints returned **stale cached pregame/mid-game snapshots** via the fetch tool; pitching line not captured |
| Dodgers Digest | [recap](https://dodgersdigest.com/2026/09/22/dodgers-7-padres-0-8-relievers-combine-on-shutout-in-remix-of-2024-nlds-game-4/) | Independent narrative | OPENED | Inning-by-inning scoring; King exit after 4th; Dodgers relief order; De Paula play | Team-oriented blog; embedded X posts are illustrative, not sources |
| True Blue LA (SB Nation) | [recap](https://www.truebluela.com/dodgers-scores-standings/125086/freddie-freeman-tommy-edman-will-smith-dodgers-bullpen-padres) | Independent narrative | Search snippet | Edman and Smith solo HRs; 8-pitcher shutout; Wrobleski/Sasaki one inning each | Snippet-level only |
| Dodger Blue via Yardbarker | [syndicated recap](https://www.yardbarker.com/mlb/articles/recap_dodgers_begin_final_home_series_by_shutting_out_padres_with_bullpen_game/s1_17075_44337655) | Narrative (one lineage) | Search snippet | Bullpen 9 IP, 5 H, 0 R, 10 K, 2 BB; 2nd- and 4th-inning run sequence | Syndicated copy; not a separate lineage from Dodger Blue |
| Dodgers Digest preview (pregame) | [preview](https://dodgersdigest.com/2026/09/22/padres-dodgers-september-22-2026-pages-and-sasaki-return-as-dodgers-open-up-final-home-series-of-the-season-with-san-diego/) | Pregame context | Search snippet | King's 2026 starts vs LAD; 4.16 FIP; bullpen game started by Stewart | Used only for the *knowability* audit, not settlement |
| CBS Sports gametracker | [page](https://www.cbssports.com/mlb/gametracker/boxscore/MLB_20260922_SD@LAD/) | Aggregator | OPENED but stale (preview state) | Confirmed both batting orders as posted; Padres/Dodgers injury lists | Stale; the partial "BF 16" snippet was a mid-game snapshot and is not used |

---

### Original supplied research card for P-490 (selection and reasoning preserved as received; formerly logged as P-484)

> Preserved verbatim from the P-484-onward mini log. The only change is this heading. The card's own references to "P-484" are historical and superseded by §0.

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

**Los Angeles has a non-standard pitching sequence.** Same-day reporting identified Brock Stewart as the opener, with the Dodgers working through a broader pitching plan rather than using a conventional full-length starter. Stewart himself has pitched very well, so "bullpen game = Padres advantage" would be an analytical mistake. Statcast shows Stewart allowing just a **.245 xwOBA**, .184 xBA and .301 xSLG in the current dataset. But every transition creates another branch for inherited runners, matchup changes and an arm having an off night. ([baseballsavant.com][8])

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
* **Padres order:** a same-day game-data feed showed Tatis, Harris, Machado, France, Merrill, Hays, Bogaerts, Campusano and Cronenworth, but the MLB endpoint I captured still said "awaiting starting lineup." I therefore did **not** use exact Padres batting-order placement as a high-weight model input. ([Reddit][15])

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

---

### REQUEST-ONLY-NBL-TAS-SEM — Tasmania JackJumpers vs South East Melbourne Phoenix (no forecast supplied; no ID; unscored)

- The attached text contains an event/market request (Phoenix -4.5, Tasmania +4.5, total 188.5) but no issued forecast, ranking, probabilities or projected winner. There is nothing to score and no retrospective to fabricate.
- **Final:** Tasmania 96, Phoenix 91 (total 187).
- *Contract-outcome illustration only, not picks:* Tasmania +4.5 WIN; Phoenix -4.5 LOSS; Under 188.5 WIN; Over 188.5 LOSS.
- The NBL schedule, NBL/AAP recap, Pulse Tasmania and Basketball.com.au agree. Tasmania scored 36 in the third quarter after trailing by 14 at half.
- Sources: [NBL schedule](https://www.nbl.com.au/club-schedule/sem), [NBL/AAP](https://www.nbl.com.au/news/jackjumpers-dig-deep-to-beat-phoenix), [Pulse Tasmania](https://pulsetasmania.com.au/news/jackjumpers-rally-from-16-down-to-beat-phoenix-96-91-in-first-game-of-season/), [Basketball.com.au](https://www.basketball.com.au/news/david-johnson-tasmania-jackjumpers-comeback-to-beat-south-east-melbourne-phoenix).
- The NBL recap is AAP-syndicated and is not counted separately from the AAP copy.

---

### REQUEST-VOID-WTA-SGP-MERTENS-KREJCIKOVA — Elise Mertens vs Barbora Krejčíková, WTA Singapore R16 (walkover before issue; no forecast; no ID; VOID)

**Status:** NO CARD ISSUED — `TE-P2` / `TE-P4` blocking-precondition failure (participant withdrawn). No picks, no potential winner forecast, no probabilities, no score tree. Nothing to settle or score; no retrospective (none requested).

**Request (logged 2026-09-23 16:30 AEST)**
- Event: Singapore Tennis Open presented by BNP Paribas 2026, WTA 500, singles Round of 16 (WTA RoundID 2), OCBC Arena, Kallang, Singapore; indoor hard.
- Supplied estimated start: 23 Sep 2026, 4:30 PM AEST (= 14:30 SGT, UTC+8).
- Supplied contracts: Mertens −3.5 games; Krejčíková +3.5 games; total games Over/Under 20.5. User also asked for a potential winner.
- Participants: [4] Elise Mertens (BEL, WTA #19, received a first-round bye as a top-4 seed; defending 2025 champion) vs Barbora Krejčíková (CZE, WTA #38 per Wikipedia infobox dated 14 Sep; TennisTemple shows #44 — unreconciled, immaterial now).

**Terminal event state (field owner: WTA)**
- WTA official match feed, `MatchID LS010`, retrieved ~16:40 and re-checked ~16:50 AEST, raw fields: `MatchState "F"`; `ResultString "[4]E. Mertens d B. Krejcikova  W/O"`; `ScoreString " W/O"`; `NumSets 0`; `MatchTimeTotal "00:00:00"`; `MatchTimeStamp "2026-09-23T06:27:15.12+00:00"` (= 14:27 SGT / 16:27 AEST); `Winner "6"`; `SeedA "4"`.
- WTA exact match page `…/scores/LS010` shows "WO" beside E. Mertens and "Finished: 0:00".
- Independent cross-check: Tennis Majors match page shows the match "Ended" with a 0–0 score (consistent with a walkover; it does not state the reason).
- Lagging sources at the time: Tennis.com still showed "upcoming"; TennisTemple (cached) showed "not started". These are publication lag, not a conflict with the field owner. `RULES_TENNIS.md` §2/§7: official event status controls withdrawals and walkovers.
- **Withdrawal reason: NOT PUBLISHED at logging time.** No injury, illness or other cause is inferred. (Krejčíková played a 31-game, three-set R1 the previous day, beating Friedsam 6–0, 5–7, 7–6(4) after saving two match points, and has 2025–26 thigh, back and knee injury history; that is context only, not evidence of the cause.) Her WTA doubles matches were still listed `U` (upcoming) in the same feed; that is not evidence either way.

**Settlement of the supplied contracts (`RULES_TENNIS.md` §10.6; standard rules per `G36.1`, operator terms not supplied)**

| Contract | Outcome |
|---|---|
| Mertens −3.5 games | **VOID** (walkover: no ball struck) |
| Krejčíková +3.5 games | **VOID** |
| Over 20.5 games | **VOID** |
| Under 20.5 games | **VOID** |
| Match winner | **VOID** as a contract under standard walkover rules. Draw advancement: Mertens to the quarterfinals via W/O. |

**Pre-withdrawal research captured (context only; NOT a forecast — nothing was frozen or issued)**
- Head-to-head: 0–0 (no prior meeting).
- Tennis Abstract WTA Elo (snapshot 2026-09-21): Mertens overall 1912.3 / hard 1848.5; Krejčíková overall 1874.2 / hard 1819.9. A plain Elo conversion would give Mertens ~55% (overall) / ~54% (hard). This is a rating benchmark only (control 13) and is **not** an issued winner probability.
- Mertens' last completed match: US Open R32 loss to Osaka (Osaka 6–3, 3–6, 7–5). Her 2026 hard-court run included the Monterrey final (lost to Parry 6–4, 0–6, 6–3).
- Krejčíková: 2026 Athens title (d. Sakkari); US Open R1 loss to Rakhimova 7–6(4), 6–2; Singapore R1 serve line vs Friedsam (Tennis.com): 1st-serve in 62% (55/89), 1st won 69% (38/55), 2nd won 50% (16/32), BP saved 4/9, service games won 10/15.

**Data-quality observations (for `SOURCES.md` / `DATA_SOURCE_REGISTER.md`)**
- A tool-summarised read of the official WTA draw PDF returned invented first-round results (e.g. "Mertens d. Krejčíková" in R1, though Mertens had a bye). It was rejected. **Use raw field-owner JSON (`api.wtatennis.com …/matches/`) with verbatim key:value capture for state and result fields; never a model paraphrase of a PDF.**
- TennisTemple's recent-results list labelled Krejčíková's US Open match against Rakhimova as a win; the WTA recap confirms a loss. Its W/L labels are not reliable for form windows.
- The WTA raw match feed exposed the walkover about 20 minutes before any independent publisher. It is the best first lane for last-minute withdrawal checks, and should be re-checked as close to the start as possible before any tennis card is frozen.

**Sources:** [WTA match feed (api.wtatennis.com, event 1152/2026)](https://api.wtatennis.com/tennis/tournaments/1152/2026/matches/) · [WTA match page LS010](https://www.wtatennis.com/tournaments/1152/singapore/2026/scores/LS010) · [Tennis Majors match page](https://www.tennismajors.com/matches/wta/singapore-tennis-open/elise-mertens-vs-barbora-krejcikova) · [WTA Singapore 411](https://www.wtatennis.com/news/4578150/singapore-411-dates-draws-schedule-prize-money-and-more) · [Tennis Abstract WTA Elo](https://tennisabstract.com/reports/wta_elo_ratings.html) · [WTA — Rakhimova d. Krejčíková, US Open 2026](https://www.wtatennis.com/news/4569164/by-the-numbers-rakhimova-battles-through-marathon-final-game-to-upset-krejcikova) · [Tennis.com — Krejčíková vs Friedsam](https://www.tennis.com/tournaments/singapore-open/matches/b-krejcikova-vs-a-friedsam-2026-09-22) · [Wikipedia — Barbora Krejčíková](https://en.wikipedia.org/wiki/Barbora_Krej%C4%8D%C3%ADkov%C3%A1) · [WTA API — Mertens 2026 matches](https://api.wtatennis.com/tennis/players/317964/matches/?page=0&pageSize=40&year=2026&type=S&sort=desc) · `RULES_TENNIS.md` (§2, §7, §9.1, §10.6).
- **Source firewall:** no odds, prediction-market, tipster, fantasy or betting-preview pages were opened or used. Betting-preview and prediction-market pages appeared in search results and were excluded.

---

# General Learnings, Rule Changes, Observations, and New Sources

## Merged-log descriptive totals (7 settled cards: P-482–P-486, P-488, P-490; not performance evidence)

This table **supersedes** the 5-card totals in the section below.

| Measure | Result |
|---|---|
| Rank #1 | **2 W / 5 L** (P-482, P-488 won) |
| Hit@2 | 5 / 7 (P-483 and P-490 missed) |
| Both top two won | 0 / 7. In P-482 the top two were a forced pair, so both could not win. |
| Projected winner | 6 / 7 (P-486 wrong) |
| Preferred total/phase direction | 4 W / 3 L. Unders 3–1; Overs 1–2 (P-482 won; P-483 and P-490 lost) |
| TOP_OU_REVIEW triggered | P-483, P-484, P-490 |
| Horizon problems | P-483, P-485, P-490 (START_CROSSED) plus P-489 (unverified): 4 of 8 cards |
| Top two sharing one driver, both lost | P-483 (Kalieva competitiveness), P-490 (King early suppression) |

**Additional learnings from P-482 / P-483 (added at merge).**
- **Cross-sport (strengthened): correlated top two.** Two cards, in two sports, lost both top picks to a single shared driver.
  - P-490 did not disclose the coupling.
  - P-483 did disclose it, but its own modal branch defeated both picks.
  - PR-3 (shared-driver disclosure) remains a candidate. A new disclosure candidate, **C-MODAL-BRANCH-CHECK**, is added: print whether the most likely scenario branch defeats Rank #1 / the top two.
- **Cross-sport (strengthened): horizon.** Four of eight cards have horizon problems. **PR-1 stays the strongest candidate.**
- **Tennis.** P-483 and P-488 are two consecutive WTA cards where the underdog +4.5 games handicap lost to a lopsided straight-set win by the favourite. In P-488 the Under was the preferred total and won. In P-483 the preferred total was the Over, which lost.
  - This is still **n=2**. It supports the `IMPLEMENTED_CHANGES` §8 proposal (serve/return numerators and denominators in RULES_TENNIS) and the two-set margin-quantile candidate.
  - It is not yet a rule.
- **Cricket.** P-482's current-role powerplay evidence beat the stale head-to-head regime. Early wickets (2 down) did not suppress the phase total below 47.5. The "early-wicket suppression" hypothesis stays experimental.

## Earlier 5-card analysis (P-484–P-490 revision; retained)

Scope: five settled cards (P-484, P-485, P-486, P-488, P-490) across four sports and five leagues. Everything below is descriptive and learning-only.

## Descriptive log totals (not performance evidence)

| Measure | Result |
|---|---|
| Rank #1 | **1 W / 4 L** (only P-488 won) |
| Hit@2 | 4 / 5 cards (P-490 missed) |
| Both top two won | 0 / 5 |
| Projected winner | 4 / 5 correct (P-486 wrong) |
| Preferred game-total direction | 3 W / 2 L. Unders 3–1 (P-485, P-486, P-488 won; P-484 lost); the only preferred Over (P-490) lost. |
| TOP_OU_REVIEW triggered | P-484, P-490 |
| Issue-horizon problems | P-485, P-490, plus unsettled P-489 |

Two cards are START_CROSSED and the sample is tiny. **No calibration, value or performance claim is made.**

## Cross-sport learnings

1. **Issue-horizon discipline is the most frequent process defect in this log.**
   - Three of six cards have start-crossing or horizon conflicts: P-485, P-490 and P-489.
   - The rule already exists (README CR-4 gate; RULES_GENERAL start-crossing). It is being breached operationally, not missing.
   - **Strong candidate process change** (see Potential rule changes).
2. **Named kill paths without mass recur across sports.**
   - P-486: Matthews' early-inning failure named, then Twins ML ranked #1.
   - P-490: "Padres lose by 2+ very real", then +1.5 ranked #2.
   - P-484: the Under's transition tail named, then Under ranked #1 on a 0.8-point edge.
   - This is L-075 / G-L9. **Existing rules inadequately applied.**
3. **Near-tie ordinals presented as confident ranks.**
   - P-484: 54% vs ~53–54%. P-486: 59% vs 57%.
   - When subjective estimates overlap within about 2–3 points, the ordinal is unstable. Label it FORCED RANK / near-tie rather than implying a real ordering.
4. **Top-two rows sharing a single driver.** P-490's #1 and #2 both depended on King's early suppression and failed together. Print P(R1 ∧ R2) with a coupling label (G-L10) and state it in the card.
5. **Opponent-unadjusted short recency windows.** P-490 (King's L5; the Padres' L5/L10 against Colorado and Miami) is a recurrence of the R-1 finding and the README's P-453 reclassification.

## Sport-specific learnings

- **Baseball (MLB), 2 cards.**
  - Starter-length props need the opponent-specific exit record, the per-start BF/pitch/BB log and a hook-given-runs branch.
  - Underdog +1.5 cushions keep losing to the BB-B4 separation family, adding to the 4 W / 6 L note from 2026-09-15(b).
  - A bullpen game is not directional. P-490's card said so, correctly, for the side market but not for the total.
- **Tennis (WTA), 2 cards including P-483 from IMPLEMENTED_CHANGES.**
  - In both, the underdog +4.5 games handicap lost as the favourite won in straight sets. The Under won in both, but was the preferred total only in P-488.
  - This is an emerging geometry pattern: a two-set match with one lopsided set. **n=2; needs more evidence.**
- **Basketball (WNBA), 1 card.** Near-line totals need a quantified transition/turnover component. Single-quarter bursts decide 1–2 point misses.
- **American football (NFL), 1 card.** QB injury shock is variance, and the horizon breach makes the card unscorable for pregame learning.
- **NPB, 1 card pending.** At settlement, use the three-way end state (tie after 12) per control 32. Chunichi +1.5 wins on a tie.

## Potential rule changes

| Proposal | Evidence | Status |
|---|---|---|
| **PR-1 Hard pre-start freeze.** A card's final volatile refresh and freeze timestamp must precede the verified scheduled start. If the freeze time is at or after scheduled start, the card is labelled START_CROSSED at issue, not only at settlement, and the mini log records it that way from creation. | 3 of 6 cards in this log (P-485, P-490, P-489). The rule text already exists; this is an operational enforcement checklist item. | **Strong candidate.** Recurring, process-only, no predictive weight. |
| **PR-2 Near-tie ordinal label.** When the top two subjective estimates differ by ≤3 points, print `NEAR_TIE` beside the ordinal (links METHOD §7 `rank_gap`). | P-484, P-486 | Candidate. Disclosure only. |
| **PR-3 Shared-driver disclosure for the top two.** Print the single dominant driver of R1 and R2 and the coupling label (G-L10). | P-490 | Candidate. Reinforces an existing gate. |

## Algorithm improvements (to test prospectively; nothing fitted)

- **C-P490-SP-OUTS-OPP (new candidate).**
  - Before a starter-length (outs/IP) row may rank #1 against a top-quartile offense, the card must print:
    - the starter's current-season starts against that opponent (IP/BF/pitches/BB);
    - the L10–L20 hook-point distribution;
    - the conditional early-exit branch given 3+ early runs.
  - Test prospectively; no promotion from one game (L-087).
- **Tennis two-set margin model (candidate).** Estimate game margin conditional on set count; report quantiles for straight-set outcomes. Evidence: P-483, P-488.
- **WNBA turnover-to-transition component for totals (candidate).** Evidence: P-484.
- **MLB first-five vs relief-state separation (candidate).** Evidence: P-486, P-490.

## Source improvements and new sources

| Source | Best suited for | Assessment |
|---|---|---|
| MLB Stats API `/api/v1/schedule?gamePk=…&hydrate=linescore,decisions` | Terminal state, final score, linescore, W/L decisions | **Reliable and current at settlement.** The `feed/live` and `boxscore` endpoints returned stale cached snapshots through the fetch tool in this pass. Prefer the schedule+hydrate route for state and final; re-try the boxscore via curl or a later fetch for pitcher lines. This supplements the 2026-09-11 note (HTTP 406 via WebFetch). |
| Dodgers Digest game previews/recaps | Independent inning-by-inning narrative; pregame starter-vs-opponent history | Useful and accurate here, and independent of MLB. Team-oriented; one success is not grounds for promotion. |
| True Blue LA (SB Nation) | Independent corroborating lineage | Adequate as a third lineage. Snippet-level use only this pass. |
| Dodger Blue (syndicated on Yardbarker) | Narrative stats | Syndication: count as **one** lineage with Dodger Blue. |
| Baseball Savant player pages | xERA/xwOBA | **Always pin `season=2026` in the URL.** P-490's cited link carried `season=2023`, making the xERA attribution unverifiable. |
| Reddit game threads | — | **Inadmissible** for lineups (S-1), even when accurate. Use the MLB Stats API `hydrate=lineups` / boxscore `battingOrder` instead. |
| NPB official box score | NPB state and final (field owner) | Reliable. Pair with the NPB English box and an independent Japanese outlet for three lineages. |

## Data-quality observations

- Several attachments carry opaque content-reference tokens instead of URLs. Future cards must store real URLs and retrieval timestamps.
- Official MLB lineup/probable endpoints can lag same-day reporting. Record `LINEUPS_NOT_YET_PUBLISHED` vs `RETRIEVAL_MISS` explicitly.
- A tennis tiebreak-point conflict between WTA pages did not affect any contract. Record which disputed fields are contract-relevant.
- (Added 2026-09-23 ~16:55 AEST, Mertens–Krejčíková request.) A model-summarised read of the official WTA draw PDF invented results. Take state and result fields verbatim from raw field-owner JSON. The WTA raw match feed showed the walkover about 20 minutes before independent publishers, so it is the lane for the final pre-freeze withdrawal check.

## Recurring blind spots

- Missing official lineups at issue: P-484 (both), P-486 (SF), P-490 (both officially).
- Missing bench/relief ladders and injury lists for one side: P-484, P-486, P-490.
- Starter/opponent-specific history not retrieved: P-490.
- Freeze after start: P-485, P-490, P-489.

## Items requiring more evidence before becoming formal rules

- C-P490-SP-OUTS-OPP (starter-length props vs strong offenses).
- The tennis underdog +4.5 two-set geometry (n=2).
- Whether near-tie labelling improves top-two accuracy across a prospective, event-grouped sample.
- Any systematic Over/Under bias in this log (sample of 5; mixed sports).

---

# Document Update Mapping

No governing document or canonical log was modified. The four source mini logs were moved, unchanged, into `_superseded_source_logs/`. This merged file is the single active mini log.

| Finding / disposition | Target document (later, if evidence warrants) |
|---|---|
| P-482 settlement (phase total 59/2; Falcons won) and REVIEW-P482-PHASE | `PREDICTION_LOG_COMBINED_5.md`; `RULES_CRICKET.md` (phase-regime note, no rule) |
| P-483 settlement, correlated top two, rout-branch mass | `PREDICTION_LOG_COMBINED_5.md`; `RULES_TENNIS.md` (serve/return numerators per `IMPLEMENTED_CHANGES` §8; margin quantiles, candidate); `LEARNING_REGISTER.md` |
| C-MODAL-BRANCH-CHECK (flag when the modal scenario branch defeats Rank #1 / top two) | `METHOD.md`, `SCORING_AND_VALIDATION.md` (disclosure candidate); `LEARNING_REGISTER.md` (CANDIDATE) |
| Merge of four mini logs into one file/folder; master ID register; next ID P-491 | `EXTERNAL_LOGGING_WORKFLOW.md` (single-active-mini-log rule); `GAME_LOG_STATUS_CURRENT.md` |
| §0A ID resolution (Padres → P-490; WNBA → P-484; P-487 gap; next P-491) | `PREDICTION_LOG_COMBINED_5.md`, `GAME_LOG_STATUS_CURRENT.md` |
| Import order (this log in ID order from P-482) | `EXTERNAL_LOGGING_WORKFLOW.md` (atomic registration checklist) |
| PR-1 hard pre-start freeze | `METHOD.md`, `CONTROLS.md`, `FORECAST_PREFLIGHT_MANIFEST.md` / `prediction_preflight.py` (code change only by authorised audit) |
| PR-2 near-tie label; PR-3 shared-driver disclosure | `SCORING_AND_VALIDATION.md`, `METHOD.md` |
| Named kill path without mass (P-484, P-486, P-490) | `LEARNING_REGISTER.md` (recurrence under L-075 / G-L9); `RULES_GENERAL.md` §16.5 note |
| C-P490-SP-OUTS-OPP; hook-given-runs; opponent exit record | `RULES_BASEBALL.md` §8.4/§8.7 (candidate); `LEARNING_REGISTER.md` (CANDIDATE) |
| MLB +1.5 cushion loss vs BB-B4 | `RULES_BASEBALL.md` 2026-09-15(b) tally update; `LEARNING_REGISTER.md` |
| R-1 recency misuse (King L5; Padres L5/L10) | `RECENCY_AND_REBOUND.md` example log; `LEARNING_REGISTER.md` |
| Tennis two-set margin geometry (P-483, P-488) | `RULES_TENNIS.md` (testable observation); `LEARNING_REGISTER.md` |
| WNBA turnover-to-transition totals | `RULES_BASKETBALL.md` (unpromoted note) |
| NFL horizon breach + QB-shock attribution | `RULES_AMERICAN_FOOTBALL.md`; `METHOD.md` horizon handling |
| NPB three-way settlement reminder (tie after 12) | Already covered by `RULES_BASEBALL.md` control 32; no change |
| MLB Stats API schedule+hydrate as settlement route; stale feed/live caching; Savant `season=` pinning; Reddit inadmissible | `SOURCES.md`, `DATA_SOURCE_REGISTER.md` (MLB section) |
| Dodgers Digest / True Blue LA / Dodger Blue lineage notes | `DATA_SOURCE_REGISTER.md` (lineage/syndication notes; no promotion) |
| Cross-sport decision accounting; learning-only status | `SCORING_AND_VALIDATION.md`, `PERFORMANCE_ELIGIBILITY_POLICY.md` (no change; status confirmed) |
| Mertens–Krejčíková walkover before issue: void record, no ID; WTA raw match feed as last-minute withdrawal lane; reject model-paraphrased PDFs | `EXTERNAL_LOGGING_WORKFLOW.md` (no-card / void request handling); `SOURCES.md`, `DATA_SOURCE_REGISTER.md` (WTA section); `RULES_TENNIS.md` §10.6 already covers settlement — no change |

**Proposed new document (not created):** `ISSUE_HORIZON_REGISTER.md`. It would be one table per card: scheduled start (venue-local and Melbourne), freeze timestamp, first-pitch/kick-off timestamp, and horizon label. Its purpose is to let canonical import filter START_CROSSED cards mechanically, since horizon failures are this log's most frequent defect.

---

## Settled logs (first to most recent)

1. **P-482** — Cricket — CPL 2026 Final, Antigua & Barbuda Falcons vs Jamaica Kingsmen — Falcons by 8 wickets; JAK powerplay 59/2 — settled at merge
2. **P-483** — Tennis — WTA Seoul, Volynets vs Kalieva — Volynets 6–3 6–0 — settled at merge; START_CROSSED
3. **P-484** — WNBA — Atlanta Dream @ New York Liberty — ATL 95–84 — settled
4. **P-485** — NFL — NY Giants @ LA Rams — LAR 28–6 — settled; START_CROSSED
5. **P-486** — MLB — Minnesota Twins @ San Francisco Giants — SF 5–2 — settled
6. **P-488** — WTA Singapore — Wolff vs Oliynykova — Oliynykova 6–1 7–6 — settled
7. **P-490** — MLB — SD Padres @ LA Dodgers (claimed P-484; moved to next number) — LAD 7–0 — settled; START_CROSSED
- Unscored record: REQUEST-ONLY-NBL-TAS-SEM — Tasmania 96–91 — result verified; no forecast, no ID
- Void record: REQUEST-VOID-WTA-SGP-MERTENS-KREJCIKOVA — Mertens d. Krejčíková W/O (WTA official, 23 Sep 2026, logged 16:27 AEST) — no card issued, all supplied contracts VOID, no ID

## Logs still awaiting settlement (first to most recent)

1. **P-489** — NPB — Chunichi Dragons @ Yokohama DeNA BayStars — UPCOMING (18:00 JST = 19:00 AEST, 23 Sep 2026); ISSUE_HORIZON_UNVERIFIED; settle three-way (a tie after 12 innings is possible)

2. **P-491** — NPB — Orix Buffaloes @ Chiba Lotte Marines — 17:00 JST = 18:00 AEST, 23 Sep 2026; horizon CLEAN; settle with tie rule (Buffaloes +1.5 wins a tie; totals push at exactly 7)

Unassigned: **P-487** (gap preserved). **NEXT ID: P-492.**

All records in this mini log remain **LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE**.

---

# Appendix A — Source log #1 (P-482 onward) closing sections, preserved verbatim

## 2. Settled Logs

**None.**

## 3. Sources

P-483 source index: WTA exact Seoul match/tournament pages; WTA player records and match-stat pages; USTA/US Open official report; L'Equipe current match page; MyKhel current scoreboard; structured Seoul weather; full URLs and contributions are preserved inside the P-483 card above.

### P-482 event sources
See the full source ledger under P-482 above. Material primary/current lineages: Cricket West Indies official schedule/state route; CPL official Newsroom match reports; Jamaica Gleaner/CMC; Wisden current fixture state; structured weather source.

Initialization authority:
- `METHOD.md`
- `RULES_GENERAL.md`
- `CONTROLS.md`
- `SOURCES.md`
- `DATA_SOURCE_REGISTER.md`
- `SCORING_AND_VALIDATION.md`
- `EXTERNAL_LOGGING_WORKFLOW.md`
- relevant `RULES_<SPORT>.md` and league-specific rules
- `PREDICTION_LOG_COMBINED_5.md` for canonical-ID authority
- `GAME_LOG_STATUS_CURRENT.md` for historical open-handle custody

Every event must add its own material sources, links/retrieval methods and contribution.

## 4. Document Mapping

P-483: `RULES_TENNIS.md` shared score-tree coherence; `SOURCES.md` / `DATA_SOURCE_REGISTER.md` WTA exact-match lane; `LEARNING_REGISTER.md` ace/double-fault exposure-normalization observation only. No permanent rule or coefficient change proposed.

### P-482
- `RULES_CRICKET.md`: existing phase-participant, phase-distribution, near-start XI/toss-gap and streak controls applied; no permanent rule change proposed.
- `DATA_SOURCE_REGISTER.md`: retain CWI/CPL primary routes; note confirmed-XI/toss retrieval latency.
- Prediction log: carry P-482 as unsettled until exact six-over phase and match final are verified; no retrospective has been performed.
 Each prediction, source discovery, learning or proposed rule change will record its appropriate Markdown destination here.

## 5. Running Integrity Notes

- P-452–P-481 were reconciled into `PREDICTION_LOG_COMBINED_4.md` before this log was opened.
- Do not overwrite existing canonical IDs.
- Keep unresolved entries at the top until fully settleable.
- Preserve enough source and reasoning detail to support later exact settlement and retrospective audit.
- After every new sports prediction, return the **entire updated mini running log**.

---

# Appendix B — User-supplied mini-log and settlement workflow brief

The full brief (dated 2026-09-21) is preserved verbatim at the end of source log #1, `_superseded_source_logs/Mini Prediction Log - P-482 onward - 2026-09-21/PREDICTION_MINI_RUNNING_LOG_P482_ONWARD.md`, under "User-Supplied Mini-Log and Settlement Instructions — 2026-09-21". It is a standing workflow instruction, not a log entry, so it is referenced here rather than duplicated. Where the root methodology is more current, the root framework controls.
