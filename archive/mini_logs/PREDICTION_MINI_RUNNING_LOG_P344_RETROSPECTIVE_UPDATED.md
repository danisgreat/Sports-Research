# Prediction Mini Running Log — P-333 Continuation

**Status:** ACTIVE LOCAL EXTERNAL MINI-LOG  
**Started:** 2026-09-08 Australia/Melbourne  
**Google Drive:** READ ONLY  
**Canonical Drive authority:** `PREDICTION_LOG_COMBINED_3.md`  
**Closed predecessors:** `PREDICTION_LOG_COMBINED.md` (`P-001`–`P-271`) and `PREDICTION_LOG_COMBINED_2.md` (`P-272`–`P-332`)  
**Method:** `MDS-2026.09.06-v4.0 — SPORTS_ONLY / MARKET_BLIND`  
**Drive next canonical ID at this mini-log initialization:** `P-333`  
**Local occupied IDs:** `P-333`, `P-334`, `P-335`, `P-336`, `P-337`, `P-338`, `P-339`, `P-340`, `P-341`, `P-342`, `P-343`, `P-344`  
**Next local continuation slot:** **`P-345`**  
**Drive write state:** no Drive file edited; this mini-log is the local running continuation requested by the user.

> **Controlling rule:** incomplete/unsettled/no-action records remain in the separate top queue below. They are moved to the normal chronological settled section only after a verified settlement/administrative closure under the current Drive method. Every card retains its full source register. Issued evidence is immutable; settlements and corrections are append-only.

---

# 0. CURRENT CONTROLLING SNAPSHOT — SUPERSEDING 2026-09-09 RETROSPECTIVE PASS

| Field | Current value |
|---|---|
| Active canonical Drive log | `PREDICTION_LOG_COMBINED_3.md` |
| Canonical range | `P-333` onward |
| Drive state verified 2026-09-09 | Part 3 still opens at **next canonical ID `P-333`** and contains no reconciled `P-333+` forecast component yet. The raw/local mini-log therefore does **not presently collide with an occupied canonical Part-3 ID**, but it remains unreconciled. |
| Local mini-log range | `P-333`–`P-344` |
| Local unresolved/incomplete queue after this pass | **`P-341-C03`** (BUL–Ntugasaze corners: frozen source gate not met); **`P-342-C03`** (Lučenec–Komárno corners: provisional research result only; provider/operator definition unresolved) |
| Local fully settled/admin-closed cards | `P-333`, `P-334`, `P-335`, `P-336`, `P-337`, `P-338`, `P-339`, `P-340`, `P-343`, `P-344` |
| Local partially settled cards | `P-341`, `P-342` |
| Next local ID | **`P-345`** |
| Retrospective state | Comprehensive 2026-09-09 retrospective completed for every issued local forecast; no-action cards received administrative closure reviews only, with no hindsight picks/probabilities |
| Deep-retrospective triggers | Triggered for `P-337` (two high-ranked misses), `P-339` (Rank #1 lost), `P-342` (Rank #1 and Rank #2 lost), and `P-344` (Rank #1 lost). `P-335` also receives an expanded review because two ranked rows missed despite Rank #1 winning. |
| Probability rule | Every genuinely issued v4.0 ranked row retains its original `UNVALIDATED_SUBJECTIVE` probability. No probability is added to `P-333`, `P-334`, or `P-343`, because no forecast was issued. |
| Value state | `NO VALUE DETERMINABLE` unless a validated model + same-time price/terms pass the value gate |
| Primary-scored update | Only `P-335` is `PRIMARY_SCORED` in this local cohort. It adds 4 binary rows (2W/2L), mean Brier **0.2541**. Carried mixed v4.0 total becomes approximately **37 rows, 19W/18L, mean Brier ~0.2220**; MLB subset becomes **8 rows, 4W/4L, mean Brier ~0.2217**. These are descriptive and too small for calibration/superiority claims. |
| Exploratory Brier treatment | Soccer, KBO, tennis, FIBA and other non-primary populations receive card-level descriptive Brier diagnostics only. Incomplete/provisional derivative rows are excluded until settlement reaches the frozen source standard. |
| Drive write state | **READ ONLY. No Google Drive file was edited in this pass.** |

## Canonical reconciliation / temporary-ID decision

The current Drive authority still identifies `P-333` as the next canonical Part-3 slot. Because no canonical `P-333+` records are presently occupied in `PREDICTION_LOG_COMBINED_3.md`, **none of this mini-log's `P-333`–`P-344` records requires a temporary replacement ID at this time**. The local IDs must still not be reused.

The older Part-2 appendix items (`P-126`, `P-148`, `P-149`, `P-166`, `P-176`, `P-178`, `P-179`, `P-200`, `P-217`, `P-233`, `P-234`, `P-235`, `P-274`, `P-307`) are updates to already-existing historical canonical records, not new Part-3 events, so they **retain their original IDs**. No temporary ID is created for those either.

**Ledger-integrity consequence:** this external mini-log is beyond the current Drive method's reconciliation window. Under `METHOD.md`/`CONTROLS.md`, the appropriate next repository action is reconciliation into `PREDICTION_LOG_COMBINED_3.md` before another new forecast is issued. This file records that requirement but does not edit Drive.

---

# 1. UNSETTLED / INCOMPLETE QUEUE — KEEP AT TOP UNTIL THE FROZEN FIELD SETTLES

| ID / row | Sport | Event | Final score state | Open field | Current disposition |
|---|---|---|---|---|---|
| **P-341-C03** | Soccer — Uganda Premier League | BUL FC vs Ntugasaze FC | **BUL 4-1 Ntugasaze; HT 2-1 — final verified** | Over 7.5 total corners | **UNSETTLEABLE UNDER FROZEN SOURCE GATE in this pass.** Secondary post-match displays previously indicated a 12-corner state, directionally consistent with a WIN, but the card explicitly pre-registered a named official/data-partner field as the requirement. No such settling endpoint was verified, so no official W/L/Brier is created for C03. |
| **P-342-C03** | Soccer — Slovnaft Cup | MŠK Novohrad Lučenec vs KFC Komárno | **Lučenec 0-2 Komárno; HT 0-0 — official/competition reporting verified** | Over 8.5 total corners | **PROVISIONAL RESEARCH WIN / NOT FULLY CLOSED.** Two current post-final secondary structured sources report **Lučenec 1-15 Komárno (16 total)**, but the exact operator/provider definition was never frozen. The directional result is strongly corroborated, while `OPERATOR_ACTION` and full field-owner-grade settlement remain unresolved. No official Brier is booked for C03 yet. |

**Everything else in the local `P-333`–`P-344` component is now final/administratively closed and has been retrospectively reviewed below.**

### Historical Drive appendix remains separate

The inherited unsettled/incomplete items in closed `PREDICTION_LOG_COMBINED_2.md` are **not imported into this Part-3 queue**. A fresh review of those historical appendix items is recorded in the separate bottom section `Historical Drive appendix settlement review`, including the newly strengthened `P-178` corner result.

---
# 2. ACTIVE GOVERNING CONTROLS AND LEARNINGS CARRIED FORWARD

The following are the current load-bearing controls for this mini-log. They are summarized from the active Drive method, controls and Part-3 opening snapshot; the Drive documents remain the authority.

1. **Fresh-read current authority each query.** Read `METHOD.md`, `RULES_GENERAL.md` §16, the relevant `RULES_<SPORT>.md`, `CONTROLS.md`, and the active Part-3 snapshot before issuing a new card.
2. **Queue first.** State-check every local unresolved `P-333+` record in ID order before a new forecast. Verified finals are settled/closed first; live records remain at the top.
3. **Strict state gate.** After scheduled start, a stale `Upcoming`, `0-0`, or “not started” shell does not preserve pregame status. Use a verified live state, a field-owner-confirmed zero-play delay, or fail closed.
4. **Immutable issuance.** Do not rewrite an issued rank, probability, target, source set, cutoff or participant state after the fact.
5. **`UNVALIDATED_SUBJECTIVE` probabilities.** Mandatory only on genuinely issued ranked rows from v4.0 onward; they are scored by Brier once settled but are never described as calibrated or validated.
6. **Explicit event arithmetic.** New actionable forecasts must show prior + signed adjustments + centre/width and target-line placement rather than prose-only shrinkage.
7. **Structured/field-owner first.** Query field-owning structured records before narrative reporting where available; synthetic/simulated/AI content never establishes a result.
8. **Derivative settlement coverage.** Powerplay, corner and other derivative rows require a reachable settling field before ranking where the relevant sport rules require it.
9. **Cricket phase/innings separation.** Powerplay and full-innings totals are separate targets connected through runs, wickets and resources; a correct phase direction does not validate the innings direction.
10. **Cricket pitch/conditions gate.** Actively perform the required exact-match strip search and separately establish match conditions. Never infer unreported seam/spin/grass/hardness from generic weather or venue reputation.
11. **No streak weighting without mechanism.** Recent result sequences have zero directional weight unless a currently active mechanism explains why they should persist.
12. **Ledger integrity.** Preserve one-to-one IDs and full source registers. A local external log should be reconciled into the canonical Part-3 ledger within the current Drive ledger-integrity window; until then, do not reuse its local IDs.

## Candidate watch items carried from the P-318–P-332 retrospective cohort — NOT promoted rules

- current route-to-corner / route-to-shot-on-target evidence when a major central attacker is absent;
- explicit second-half bench-attacker scoring contribution;
- distance-to-line recorded in derivative retrospectives;
- disrupted-match flag for later baseline learning when a red card, goalkeeper dismissal or long weather delay materially changes the game state.

These remain observations/candidate-watch items only. They must not be treated as fitted weights or automatic ranking rules.

---

# 3. SOURCE REGISTER — MINI-LOG INITIALIZATION

## Google Drive governing sources — read only

- `PREDICTION_LOG_COMBINED_3.md` — active canonical log, `P-333` onward, Part-3 queue/ID authority.
- `METHOD.md` — `MDS-2026.09.06-v4.0`, current lifecycle, probability mandate, retrospective and ledger-integrity rules.
- `RULES_GENERAL.md` — current state/timing, identity, participant, source and target gates.
- `CONTROLS.md` — quick-reference controls and the 2026-09-07 Part-3 restructuring / first-Brier-cohort addendum.
- `LEARNING_REGISTER.md` — lesson archive and current promoted/candidate-control history.
- `RULES_CRICKET.md` — SFA-CRICKET and pitch/conditions/phase controls applicable to `P-333`.
- `LEAGUE_RULES_CRICKET.md` — T20 playing-condition reference applicable to `P-333`.

## Carry-forward statistical context from Part 3 opening snapshot

- v4.0 first scored cohort (`P-318`–`P-332`): **33 binary ranked rows, 17 W / 16 L; mean Brier 0.2181 vs 0.2500 baseline**.
- `PRIMARY_SCORED` subset at Part-3 opening: EPL 10 rows, MLB 4 rows, NRL/AFL 0 rows; sample explicitly too small for calibration or superiority claims.

---

# 4. CHRONOLOGICAL SETTLED / ADMIN-CLOSED LOCAL LOGS — CURRENT STATUS

| ID | Event | Current closure | Ranked-row result |
|---|---|---|---|
| **P-333** | Pakistan Women vs Hong Kong Women | **ADMIN CLOSED / NO FORECAST:** Pakistan 143/8 beat Hong Kong 71 by 72 runs. | None issued; no W/L/Brier. Administrative gate review completed. |
| **P-334** | Germany Women vs Mali Women | **ADMIN CLOSED / NO FORECAST:** Germany 83-58 Mali. | None issued; no W/L/Brier. Administrative gate review completed. |
| **P-335** | Washington Nationals @ San Diego Padres | **FINAL / SETTLED:** Padres 3-2 Nationals. | R1 W, R2 L, R3 L, R4 W; winner Padres W; mean Brier **0.2541**. |
| **P-336** | Carabobo FC vs Estudiantes de Mérida | **FINAL / SETTLED:** Carabobo 1-0, HT 1-0; post-final stats 3-9 corners. | R1 W, R2 W, R3 W, R4 L, R5 L; winner Carabobo W; mean Brier **0.1751**. |
| **P-337** | Barracas Central vs Argentinos Juniors | **FINAL / SETTLED:** 0-0, HT 0-0; corners 3-4. | R1 W, R2 L, R3 L, R4 W, R5 L; winner Argentinos L (draw); mean Brier **0.2603**. |
| **P-338** | Iva Jovic vs Coco Gauff | **FINAL / SETTLED:** Gauff 6-1, 6-4. | R1 W, R2 W, R3 L, R4 L; winner Gauff W; mean Brier **0.2163**. |
| **P-339** | Doosan Bears @ Hanwha Eagles | **FINAL / SETTLED:** Hanwha 6-1 Doosan. | R1 L, R2 L, R3 W, R4 W; winner Hanwha W; mean Brier **0.3368**. |
| **P-340** | Incheon United vs Bucheon FC 1995 | **FINAL / SETTLED:** Incheon 2-1, HT 1-1; 7 total corners. | R1 W, R2 W, R3 L, R4 W, R5 L; winner Incheon W; mean Brier **0.2155**. |
| **P-341** | BUL FC vs Ntugasaze FC | **FINAL / PARTIAL:** BUL 4-1, HT 2-1. | Score rows: R1 W, R2 L, R4 W, R5 L; winner BUL W; R3 corners remains unscored; 4-row partial mean Brier **0.2443**. |
| **P-342** | MŠK Novohrad Lučenec vs KFC Komárno | **FINAL / PARTIAL:** Komárno 2-0, HT 0-0. | Fully settled score rows: R1 L, R2 L, R4 W, R5 W; winner Komárno W; R3 corners provisional W only; 4-row settled mean Brier **0.3880**. |
| **P-343** | Bangladesh Women vs UAE Women | **ADMIN CLOSED / NO FORECAST:** Bangladesh 103/7 beat UAE 69/9 by 34 runs. | None issued; no W/L/Brier. Administrative gate review completed. |
| **P-344** | Hungary Women vs Japan Women | **FINAL / SETTLED:** Hungary 84-63 Japan. | R1 L, R2 W, R3 L, R4 W; winner Hungary W; mean Brier **0.2834**. |

The original issuance text remains immutable below. The 2026-09-09 settlement and retrospective addenda appended to each card supersede earlier "no retrospective yet" administrative labels without rewriting the pregame forecast.

---
# 5. DETAILED OPEN RECORDS

# P-333 — Pakistan Women vs Hong Kong Women — ACC Women's T20 Asia Cup 2026, Group A

## Controlling status

**Local external continuation ID:** `P-333`  
**Active Drive canonical file:** `PREDICTION_LOG_COMBINED_3.md`  
**Drive next canonical ID at session start:** `P-333`  
**Google Drive:** **READ ONLY — not edited by this session**  
**Method:** `MDS-2026.09.06-v4.0`  
**Population:** `EXPLORATORY — NOT SCORED`  
**User-requested retrospective:** **NOT PERFORMED**  
**Forecast disposition:** **LIVE STATE NOT VERIFIED — NO ACTIONABLE LIVE FORECAST**  
**Ranked rows issued:** **NONE**  
**UNVALIDATED_SUBJECTIVE probabilities issued:** **NONE**  
**Potential winner issued:** **NONE**  

> This is a state-gate/no-action record, not a forecast card. The user's supplied contracts and all pre-cutoff research are preserved below, but no stale pregame rank is issued after the scheduled start. This follows the current `RULES_GENERAL.md` start-crossing rule: once scheduled start passes, an `Upcoming` shell or zero-score shell does not prove pregame status; a verified live state, a field-owner-confirmed zero-play delay, or a verified final is required.

## 1. Time correction and state gate

The user estimated the start as **8 September 2026, 12:30 PM AEST**. Current fixture sources instead resolve:

- Dubai local start: **7 September 2026, 18:30 GST (UTC+4)**;
- UTC start: **7 September 2026, 14:30 UTC**;
- Melbourne/AEST equivalent: **8 September 2026, 00:30 AEST**.

The research freeze occurred at **2026-09-08 00:28:54 AEST**, while current match pages still displayed `Upcoming`. The scheduled start then passed during research. At the final state check after 00:37 AEST:

- Cricbuzz still said the scorecard would appear once the match starts and listed the start as 14:30 GMT;
- Wisden still displayed `Upcoming`, toss `-`, teams to be announced at toss;
- MyKhel displayed `Match Yet To Begin` / toss `-` / playing XIs `-`;
- ABC's score centre displayed `Game not started`.

None of those establishes a **field-owner-confirmed zero-play delay**, and none exposes an exact verified live score/over/innings state. Therefore the active Drive timing gate fails closed.

**State code:** `LIVE_STATE_NOT_VERIFIED`  
**Action:** `NO_ACTIONABLE_LIVE_FORECAST`  

## 2. Frozen user-supplied decision set

These are preserved for provenance only; they were **not ranked**.

| Contract | Exact target | Condition |
|---|---|---|
| `P-333-C01` | Pakistan Women first-innings **Over 139.5 runs** | Only meaningful if Pakistan bat first and the innings/settlement endpoint is actioned under the operator's rules |
| `P-333-C02` | Pakistan Women first-innings **Under 139.5 runs** | Same condition |
| `P-333-C03` | Pakistan Women first six completed overs / powerplay **Over 42.5 runs** | Only meaningful if Pakistan bat first; six completed legal overs is the target |
| `P-333-C04` | Pakistan Women first six completed overs / powerplay **Under 42.5 runs** | Same condition |

The user's note that “the first innings is of the team batting first” is preserved. The toss/innings order was **not verified before the research cutoff**, so these Pakistan innings rows remained conditional.

## 3. Current rules / contract identity

The current cricket reference confirms standard T20 structure for the relevant target family:

- 20 overs per innings in a full T20;
- six legal deliveries per over;
- powerplay = overs 1–6, with only two fielders permitted outside the 30-yard circle;
- maximum four overs per bowler in a full innings;
- DLS/shortening is a distinct settlement/state branch;
- phase output and full-innings output must be modelled separately through the phase-end runs/wickets/resources state.

No operator-specific shortening/action wording was supplied. Had a forecast been issuable, `RESEARCH_GRADE` and later `OPERATOR_ACTION` would have remained separate.

## 4. Participant and availability research — pre-cutoff only

### Pakistan Women

Current Pakistan squad recovered from PCB/current competition records:

- Fatima Sana (captain)
- Muneeba Ali (wicketkeeper)
- Shawaal Zulfiqar
- Gull Feroza
- Ayesha Zafar
- Sadaf Shamas
- Eyman Fatima
- Umm-e-Hani
- Tuba Hassan
- Nashra Sundhu
- Sadia Iqbal
- Waheeda Akhtar
- Saira Jabeen
- Momina Riasat
- Eman Naseer

**Material availability change:** wicketkeeper-batter **Najiha Alvi was ruled out** with posterior left-knee pain / suspected sprain and PCB said her rehabilitation could take up to four weeks. **Sadaf Shamas** replaced her in the Asia Cup squad.

The last Pakistan Asia Cup XI before this fixture had Muneeba Ali and Shawaal Zulfiqar opening, with Fatima Sana captaining. Exact Sep 7 playing XI and full bench were **not announced before the cutoff** and are not reconstructed from predictions.

### Hong Kong Women

Current tournament squad/current-match resources recovered from reputable scorecard/squad sources include:

- Natasha Miles (captain)
- Yasmin Daswani (wicketkeeper)
- Mariko Hill
- Kary Chan
- Marina Lamplough
- Maryam Bibi
- Shanzeen Shahzad
- Alison Siu
- Iqra Sahar
- Joyleen Kaur
- Ruchitha Venkatesh
- Charlotte Chan
- Shing Chan Dorothea
- Mahekdeep Kaur
- Hailey Wong

No authoritative current Hong Kong injury bulletin was recovered before the cutoff. That is recorded as **availability evidence incomplete**, not as “no injuries”.

### Participant-gate consequence

- Pakistan squad: `CONFIRMED / CURRENT` at squad level.
- Hong Kong squad: `CURRENT / MULTI-SOURCE`, but no complete field-owner injury bulletin recovered.
- Exact current XIs/toss: `NOT_YET_VERIFIED_AT_CUTOFF`.
- Full current bench/rotation state: `NOT_RETRIEVED`.

Those missing fields would have capped evidence even if the event had remained pregame.

## 5. Pakistan batting form windows — cutoff-safe

### L5 completed T20 innings

Pakistan's five most recent completed T20 batting totals entering this fixture:

1. **55** vs India — 5 Sep, Dubai
2. **119/9** vs Thailand — 1 Sep, Dubai
3. **115/6** vs Sri Lanka — 4 Aug, Dambulla
4. **175/5** vs Sri Lanka — 2 Aug, Dambulla
5. **176/7** vs Sri Lanka — 31 Jul, Dambulla

**L5 mean: 128.0.**

This is highly dispersed: a 55–176 range, so the average is not a sufficient distribution by itself.

### L10 completed T20 innings

Adding the preceding five completed T20 innings gives approximately:

- 126 vs Netherlands
- 86 vs Australia
- 100 vs Bangladesh
- 126 vs South Africa
- 106 vs India

**L10 mean: 118.4.**

### L15 continuity diagnostic

Adding the late-May Zimbabwe/qualifier-era high totals produces an L15 mean around **144.3**, but this window has a clear continuity problem: several large scores came against materially different opposition and on different surfaces, and it predates the current Dubai tournament state. It therefore cannot simply override the nearer L5/L10 evidence.

### Current tournament signal

Pakistan's two Asia Cup innings at Dubai before this match were:

- **119/9 vs Thailand**;
- **55 all out vs India**.

The Thailand match was won by 35 runs; India then dismissed Pakistan for 55 and chased in 8.4 overs.

### Current opening / powerplay signal

Pakistan's opening pair produced a run-a-ball **27** against India before Muneeba Ali was dismissed in the fifth over. The subsequent batting collapse was dominated by India's spin attack. Across the two current Dubai matches, Pakistan's early phase has not resembled the 170+ Dambulla ceiling consistently.

**Important structural rule:** this is not permission to infer the full innings mechanically from six-over output. Phase and innings are separate targets linked through wickets/resources remaining.

## 6. Hong Kong current context

Hong Kong entered this match 0–2 in the group:

- lost to Thailand by **6 runs** after Thailand made **120/9** and Hong Kong **114/7**;
- lost to India by **137 runs** after India made **193/5** and Hong Kong were dismissed for **56**.

Their recent Namibia quadrangular batting totals included roughly **108, 152, 113, 114, 138, 120 and 116**, demonstrating that the side is not uniformly a sub-100 batting unit, but the opponent-quality distribution is much weaker than Pakistan's broader international schedule.

For the specific Pakistan batting target, Hong Kong's bowling evidence is mixed:

- they restricted Thailand to 120/9;
- they conceded 193/5 to India;
- **Marina Lamplough** entered this fixture among the tournament's leading wicket-takers (six wickets from two matches in Cricbuzz's tournament table).

Therefore “Hong Kong are weaker” is not a sufficient mechanism by itself to assume Pakistan will clear 140.

## 7. Pitch / strip search — required six-rung audit

**STRIP STATUS: `NOT FOUND AFTER SEARCH`**  
**MATCH CONDITIONS STATUS: `FORECAST / PARTIAL`**

| Rung | Source/search attempted | Result before cutoff |
|---|---|---|
| 1. Official competition / match centre | PCB competition page; Pakistan current fixture material | Fixture/venue verified; no same-day observed strip assessment exposed |
| 2. Venue / curator | Dubai International Cricket Stadium venue search; curator references | Tony Hemming identified in current venue records; no dated same-day curator/groundsman strip report recovered |
| 3. Specialist exact-match pitch/conditions article | Exact Pakistan Women–Hong Kong Women preview searches | Match-specific commentary described possible early pace/bounce and later slowing, but it was not an observed toss-window strip report |
| 4. ICC pitch/outfield rating context | ICC/venue pitch-rating search | No match-specific pregame rating that could substitute for today's strip; ratings are retrospective context only |
| 5. Broadcast/live/toss commentary | Wisden and Cricbuzz match centre | No toss or pitch report before cutoff; toss remained `-` / teams to be announced |
| 6. Additional reputable venue/current search | Current venue profiles and tournament reports | Broad venue tendencies found, but no verified same-day strip observation |

The cricket rules explicitly prohibit turning weather or generic venue tendency into invented claims about grass, hardness, seam, spin or deterioration. Accordingly no such strip feature is asserted.

## 8. Conditions

Available match-specific forecast material before the scheduled start described **clear/hot Dubai conditions**, around the low 30s °C, with no material rain signal. Wisden's current match page also displayed **Clear**.

However, the v4.0 cross-sport environment gate requires a **venue-coordinate hourly forecast**, not merely a city or generic match-page forecast. A sufficiently field-specific coordinate-hourly record was not established before the start crossed.

**Environment gate:** `VENUE_COORDINATE_HOURLY_NOT_VERIFIED`.

This independently prevents treating the research as a fully compliant issued pregame card.

## 9. Pre-cutoff analytical observations — NOT PICKS

These observations are preserved because they were knowable before the scheduled start. They are **not ranks, probabilities, bets, winner calls, or an issued forecast**.

- The **139.5 innings threshold** sat above Pakistan's L5 (128.0) and L10 (118.4) averages and above both of Pakistan's current Dubai Asia Cup totals (119 and 55), but Hong Kong represent a materially weaker bowling matchup than India and Pakistan demonstrated a 175–176 ceiling in Dambulla. The target therefore required a genuinely wide distribution rather than a simple “recent average Under” shortcut.
- The **42.5 powerplay threshold** was also vulnerable to the current opening instability, but Pakistan retained an upper branch if Muneeba/Shawaal/Gull survived the new ball against weaker bowling. The current rules require explicit runs+wickets phase state, not phase-run extrapolation alone.
- Pakistan had the stronger overall international roster and competition position, but **no winner call is issued** because the current state gate failed.

## 10. Why no four ranked picks were issued

This is not an omission. It is the required consequence of three independent unresolved controls:

1. **Scheduled start crossed during research.** Current rules prohibit preserving a stale pre-start ranking after that point.
2. **Exact live state was not verified.** Current pages saying `Upcoming`, `Game not started`, `Match Yet To Begin`, or showing no score do not establish a valid live state after scheduled start.
3. **No field-owner zero-play delay confirmation was recovered.** Without explicit delay + zero-play evidence, the event cannot be classified `LIVE — DELAYED ZERO-PLAY`.

Additionally, the exact toss/XIs and venue-coordinate hourly environment record were not verified.

Therefore:

- **Rank #1:** NOT ISSUED
- **Rank #2:** NOT ISSUED
- **Rank #3:** NOT ISSUED
- **Rank #4:** NOT ISSUED
- **Potential winner:** NOT ISSUED
- **Probability rows:** NOT ISSUED
- **Retrospective:** NOT PERFORMED

## 11. Settlement source pre-registration / later closure

If this record is later administratively closed after the event finishes, the result should be fetched from an official competition/PCB/ACC scorecard or another field-owning structured scorecard. Because no forecast was issued, the eventual result must **not** create retrospective W/L selections.

The two Pakistan phase/innings rows would only be settleable as research endpoints if Pakistan actually batted first and the standard-rules/operator conditions make the phase/innings action valid. That future result is provenance only for this no-action record.

## 12. Source register

### Google Drive — governing sources (read-only)

- `METHOD.md` — `MDS-2026.09.06-v4.0`, lifecycle, probability and no-hindsight requirements.
- `RULES_GENERAL.md` — start-crossing/state gate, participant and source rules, explicit target/contract requirements.
- `RULES_CRICKET.md` — SFA-CRICKET; six-rung pitch search; phase/innings separation; wickets/resources structure.
- `LEAGUE_RULES_CRICKET.md` — T20 playing conditions: 20 overs, six-over powerplay, four-over bowler cap, DLS rules.
- `CONTROLS.md` — active quick-reference controls and Sep 7 Part-3 restructuring.
- `PREDICTION_LOG_COMBINED_3.md` — active canonical log; next canonical ID `P-333`; queue empty at session start.

### Public / field sources used

- PCB — ACC Women's Asia Cup 2026 tournament record:  
  https://www.pcb.com.pk/acc-womens-asia-cup-2026/tournament/1462.html
- PCB — India beat Pakistan by seven wickets, Sep 5:  
  https://www.pcb.com.pk/news-detail/india-beat-pakistan-by-seven-wickets-in-acc-women-s-t20-asia-cup.html
- Cricbuzz — Pakistan Women vs Hong Kong Women exact match scorecard/info:  
  https://www.cricbuzz.com/live-cricket-scorecard/169867/pakw-vs-hkc-w-match-11-group-a-womens-asia-cup-2026
- Cricbuzz — Women's Asia Cup 2026 series/tournament stats:  
  https://www.cricbuzz.com/cricket-series/12927/womens-asia-cup-2026
- Wisden — exact Pakistan Women v Hong Kong Women match page:  
  https://www.wisden.com/match/6c956a22-c6fd-4cee-917d-e3861d52166d
- Wisden — Women's Asia Cup 2026 schedule/squads:  
  https://www.wisden.com/cricket-news/womens-asia-cup-2026-full-squads-captains-schedule
- ABC News — cricket score centre, state cross-check:  
  https://www.abc.net.au/news/sport/score-centre/cricket
- MyKhel — Women's Asia Cup 2026 results / exact state cross-check:  
  https://www.mykhel.com/cricket/asia-cup-women-s-t20-2026-schedule-results-sr12693/
- NDTV Sports — Women's Asia Cup 2026 completed results:  
  https://sports.ndtv.com/womens-asia-cup-2026/results

### Explicit exclusions

Bookmaker prices, implied probabilities, tipster rankings, fantasy-team predictions, simulated/AI predictions and betting-consensus pages were not used as predictive evidence. Generic fantasy “pitch report” pages were excluded under the cricket source rules.

## 13. Running-log handoff

**P-333 local status:** `OPEN / NO-ACTION — LIVE STATE NOT VERIFIED`  
**Forecast issued:** `NO`  
**Performance row:** `NONE`  
**Next local external slot if this P-333 record is reconciled:** `P-334`  
**Drive canonical file remains read-only and therefore still requires reconciliation before a later new forecast if this external component is retained beyond the ledger-integrity window.**
## 14. 2026-09-09 administrative closure review — NO FORECAST RETROSPECTIVE

**Verified final already recorded in this mini-log:** Pakistan Women 143/8 beat Hong Kong Women 71 by 72 runs.

This event issued **no ranked forecast, no potential winner and no probability**, because the scheduled start crossed before a valid live state/toss/XI handoff was established. Accordingly, the final cannot be used to manufacture an accuracy grade or to claim that the pre-cutoff analytical observations were "right".

### Three-question administrative review

1. **What did the outcome turn on?** Pakistan ultimately batted first and cleared the user's 139.5 first-innings threshold at 143/8, then defended the total decisively. Those are post-issue facts, not forecast results.
2. **Was that knowable before issue and in the card?** The possibility of Pakistan batting first and their high-ceiling branch were known, but the exact toss/innings order and start state were not verified within the permitted pregame window. The card explicitly failed closed.
3. **Smallest routine change?** None to the sporting model. The controlling improvement is operational: complete the toss/live-state handshake earlier when an exact innings-order-dependent cricket target is requested.

**Process disposition:** `ADMINISTRATIVE PASS — STATE/TARGET GATE WORKED AS DESIGNED`.  
**Learning disposition:** no new rule. This reinforces the existing `RULES_CRICKET.md` target-identity and toss/innings-order controls and the cross-sport start-crossing invariant.

### Settlement/closure source

- PCB/competition final already pre-registered and recorded in this mini-log's original source block.


---

# 6. RUNNING-LOG PROCEDURE FOR EVERY FUTURE QUERY

1. Refresh `PREDICTION_LOG_COMBINED_3.md`, current `METHOD.md`, `CONTROLS.md`, `RULES_GENERAL.md` §16 and the relevant sport rules.
2. Check every unresolved/no-action card in the top queue in ID order.
3. If a queued event is verified final, settle/administratively close it under its frozen issue state **before** issuing the new card; perform a retrospective only where an actual forecast was issued and the current user instruction permits/requires it.
4. Move a fully closed record out of the top queue into the chronological settled/admin-closed section; never duplicate it as both open and settled.
5. Assign the next unused **local** ID (`P-334` next), preserving the Drive canonical mapping note while Drive remains read-only.
6. Freeze exact event/contract/target/time/participants before directional analysis.
7. Append the complete issued/no-action record, including every decisive source, source role, missingness/conflict state, probability tier where applicable, and pre-registered settlement source.
8. Update the top snapshot, open queue and next-local-ID field in the same edit.
9. Return the fully updated Markdown running log to the user after every query.

---

# 7. CHANGE LOG

## 2026-09-08 — mini-log initialization

- Started a new local Part-3 continuation based on the latest Google Drive structure and controls.
- Preserved Google Drive as read-only.
- Added `P-333` exactly as its existing state-gated **no-action** record; no retrospective, W/L grade, probability or winner was invented.
- Placed `P-333` in the separate top unresolved/no-action queue.
- Set the next local continuation slot to `P-334` to prevent ID reuse while Drive reconciliation remains outstanding.
- Carried forward the current Part-3 source/learning baseline and the P-318–P-332 candidate-watch items without promoting them into predictive weights.


---

# P-334 — Germany Women vs Mali Women — FIBA Women's Basketball World Cup 2026, Group A

## Controlling status

**Research freeze:** 2026-09-08 **01:49:17 AEST**, before scheduled 01:50 AEST tip.  
**Final delivery-state refresh:** 2026-09-08 **01:50:40 AEST**, after scheduled start.  
**Method:** `MDS-2026.09.06-v4.0` · `SFA-BASKETBALL` · `SPORTS_ONLY / MARKET_BLIND`  
**Population:** `EXPLORATORY — NOT SCORED`.  
**Forecast disposition:** **LIVE STATE NOT VERIFIED — NO ACTIONABLE LIVE FORECAST**.  
**Ranked rows issued:** **NONE**.  
**UNVALIDATED_SUBJECTIVE probabilities issued:** **NONE**.  
**Potential winner issued:** **NONE**.  
**Retrospective:** **NOT PERFORMED**, per user instruction.

> The evidence below was gathered before the scheduled start and is retained for provenance. A draft ranking existed during research, but it was **not delivered before tip**. Once the scheduled start passed, `RULES_GENERAL.md` required a verified exact live state or field-owner-confirmed zero-play delay. FIBA still exposed only the scheduled fixture shell / `Live (0)` state, not a verified score/clock. Therefore the draft ranking is suppressed and is not an issued prediction.

## 1. Identity / timing / venue

- Official event: Germany vs Mali, Group A, FIBA Women's Basketball World Cup 2026.
- Venue: **Berlin Arena, Berlin, Germany**.
- Official FIBA local time: 17:50 Berlin (GMT+2), equivalent to **01:50 AEST, 8 Sep 2026**.
- At 01:49:17 AEST, FIBA had no score and listed zero live games.
- At the delivery-state refresh 01:50:40 AEST, the scheduled start had passed but FIBA still did not expose a verified live score/clock and still showed `Live (0)`.
- `P-333` state-check before this card: Pakistan Women vs Hong Kong Women was verified live (Pakistan batting) and remains open at the top; no P-333 forecast was issued.

**State code:** `LIVE_STATE_NOT_VERIFIED`  
**Action:** `NO_ACTIONABLE_LIVE_FORECAST`

## 2. Frozen supplied contracts — preserved but not ranked

| Contract | Settlement event | Issuance |
|---|---|---|
| `P-334-C01` | Germany -12.5 | **NOT ISSUED** |
| `P-334-C02` | Mali +12.5 | **NOT ISSUED** |
| `P-334-C03` | Combined total Over 149.5 | **NOT ISSUED** |
| `P-334-C04` | Combined total Under 149.5 | **NOT ISSUED** |

No probability, ordinal rank or potential winner is published after the start-crossing gate failed.

## 3. Availability / participant research — pre-start only

FIBA confirmed final tournament rosters for both countries before the World Cup. At the pre-start cutoff, the official Germany-Mali game page did **not** expose a confirmed starting five. No authoritative same-day late-withdrawal/injury bulletin was recovered in the pre-tip search. This is **not** proof of no injuries.

Decision-driving players demonstrated active tournament roles through the first two games:

- **Germany:** Nyara Sabally (14.0 PPG, 8.0 REB), Frieda Bühner (11.5 PPG), Marie Gülich (9.5 PPG), Leonie Fiebich (7.5 REB, 4.0 AST), with Alexis Peterson / Alexandra Wilke in the guard-creation structure.
- **Mali:** Djeneba N'Diaye (20.5 PPG), Sika Koné (20.0 PPG, 10.5 REB), Aminata Sangaré (15.0 PPG, 8.0 REB), Rokia Doumbia (5.0 AST), Alima Dembélé (4.0 AST).

**BK-P2 status at cutoff:** current tournament roster confirmed; exact starters unresolved. The basketball rules require unresolved starters to widen the minutes/lineup distribution rather than be guessed.

## 4. Current tournament evidence — pre-start only

### Germany
- Lost to Spain **83-53**. Germany shot 29% overall and 17.4% from three; Spain shot 54%.
- Beat Japan **74-58**. Germany shot 41%; the hosts opened 28-11 and then defended strongly.
- Tournament averages entering Mali: **63.5 PPG, 46 REB, 15.5 AST, 42.7% 2PT, 24% 3PT, 75% FT**.

### Mali
- Lost to Japan **102-97**; Japan made a Women's World Cup-record **20 threes**, so that 199-point game is an extreme shooting branch rather than an ordinary defensive baseline.
- Beat Spain **82-73**, the same Spain side that beat Germany by 30. Mali shot **50% overall, 55.3% on twos and 40.9% from three**.
- Tournament averages entering Germany: **89.5 PPG, 38.5 REB, 25 AST, 55.6% 2PT, 40% 3PT, 78.1% FT**.

The current World Cup sample was only two games per team. Full same-regime L5/L10/L15/L20 windows were not reconstructed inside the short pre-tip research window, so no longer-window claim is fabricated.

## 5. Pre-start analytical object — retained for audit, not an issued forecast

A preliminary cross-opponent arithmetic check produced:

- Germany raw cross-opponent centre: `(63.5 offence + 87.5 Mali allowed) / 2 = 75.5`.
- Mali raw cross-opponent centre: `(89.5 offence + 70.5 Germany allowed) / 2 = 80.0`.

After qualitative home/rebounding, shooting-regression and defensive-suppression adjustments, the working pre-start central state was roughly **Germany high-70s / Mali low-to-mid-70s**, placing the total near **150** and the central Germany margin far short of **13 points**. The corridor was deliberately wide because of two-game samples and high shooting variance.

This analytical object explains why the pre-start research did **not** support treating Germany -12.5 as automatic safety, but it is not converted into a delivered pick or probability after the start-crossing failure.

## 6. Main uncertainty / kill paths retained for later settlement context

1. Starting fives were unresolved at the pre-start cutoff.
2. Mali's 40% tournament three-point rate was a two-game sample and subject to regression.
3. Germany's offence had already ranged from 53 to 74; its 24% three-point rate created a material total downside.
4. Japan-Mali was an extreme three-point environment and should not be treated as Mali's ordinary total baseline.
5. Garbage time is multi-axis and can compress or preserve a margin while moving the total either way.
6. Operator overtime/action terms were not supplied.

## 7. P-334 source register

### Governing Drive sources — read only
- `METHOD.md` — `MDS-2026.09.06-v4.0` lifecycle, probability, state and scoring rules.
- `RULES_BASKETBALL.md` — `SFA-BASKETBALL`, BK-P2 availability, mismatch state tree, team-score and separation budgets.
- `RULES_GENERAL.md` §16 — start-crossing/state, participant and final-refresh controls.
- `PREDICTION_LOG_COMBINED_3.md` / local P-333 continuation — ID and queue authority.
- `CONTROLS.md` — current quick-reference controls.

### Official / current external sources
- FIBA Germany-Mali game centre: `https://www.fiba.basketball/en/events/fiba-womens-basketball-world-cup-2026/games/128121-GER-MLI`
- FIBA Germany team profile: `https://www.fiba.basketball/en/events/fiba-womens-basketball-world-cup-2026/teams/germany`
- FIBA Mali team profile: `https://www.fiba.basketball/en/events/fiba-womens-basketball-world-cup-2026/teams/mali`
- FIBA Spain-Germany: `https://www.fiba.basketball/en/events/fiba-womens-basketball-world-cup-2026/games/128117-ESP-GER`
- FIBA Germany-Japan: `https://www.fiba.basketball/en/events/fiba-womens-basketball-world-cup-2026/games/128118-GER-JPN`
- FIBA Japan-Mali: `https://www.fiba.basketball/en/events/fiba-womens-basketball-world-cup-2026/games/128116-JPN-MLI`
- FIBA Mali-Spain: `https://www.fiba.basketball/en/events/fiba-womens-basketball-world-cup-2026/games/128119-MLI-ESP`
- FIBA confirmed World Cup rosters: `https://www.fiba.basketball/en/news/rosters-confirmed-ahead-of-tip-off-at-fiba-womens-basketball-world-cup-2026`
- FIBA competition statistics: `https://www.fiba.basketball/en/events/fiba-womens-basketball-world-cup-2026/stats`

**Next local continuation slot:** `P-335`.
## 8. 2026-09-09 administrative closure review — NO FORECAST RETROSPECTIVE

**Verified final already recorded:** Germany Women 83-58 Mali Women.

No ranking or winner call was delivered before tip. The preliminary analytical object therefore remains audit context only and is **not** converted into a hindsight forecast.

### Three-question administrative review

1. **What did the outcome turn on?** Germany ultimately separated by 25 points in a much lower-scoring 141-point game than Mali's first two tournament games suggested.
2. **Was that knowable before issue and in the card?** Germany's defensive suppression and Mali's extreme Japan shooting environment were explicitly identified as uncertainty branches, but there was no issued forecast to grade.
3. **Smallest routine change?** Earlier acquisition of the official live/starting-five state would reduce start-crossing no-actions; no retrospective model weight is justified from an unpublished draft.

**Process disposition:** `ADMINISTRATIVE PASS — NO HINDSIGHT CONVERSION`.  
**Learning disposition:** no new basketball rule and no probability backfill.



---

# P-335 — Washington Nationals @ San Diego Padres — MLB — 2026-09-07 local / 2026-09-08 AEST

## Controlling status

**GAME-STATE:** PREGAME  
**Forecast cutoff / final volatile refresh:** **2026-09-08 07:06:13 AEST** (2026-09-07 14:06:13 PDT)  
**Scheduled start:** 2026-09-08 07:10 AEST / 2026-09-07 14:10 PDT  
**Venue:** Petco Park, San Diego  
**Method:** `MDS-2026.09.06-v4.0 — SPORTS_ONLY / MARKET_BLIND`  
**Population:** `PRIMARY_SCORED — MLB`  
**Retrospective:** NOT PERFORMED — user requested none yet  
**Operator action/listed-pitcher wording:** not supplied; research grade and operator action remain separate at settlement.

## Frozen supplied slate

1. San Diego Padres **-1.5**
2. Washington Nationals **+1.5**
3. Combined Total **Over 8.0 runs**
4. Combined Total **Under 8.0 runs**

## Final ranked forecast

| Rank | Pick | `UNVALIDATED_SUBJECTIVE` probability | Evidence grade | Core rationale |
|---:|---|---:|---|---|
| **1** | **Washington Nationals +1.5** | **59%** | MEDIUM | San Diego is the more likely outright winner, but Pivetta is making his first MLB start since April after a flexor/elbow layoff and rehab ramp; Padres' recent offence has been modest. Central margin is only SD +0.7, leaving the one-run/WSH-win branches larger than the 2+ SD branch. |
| **2** | **Over 8.0 runs** | **52% WIN / 12% PUSH / 36% LOSS** | MEDIUM | Irvin's 5.57 ERA/1.40 WHIP and 6.09 ERA over his last seven starts create a real SD scoring ceiling; Pivetta's return/short-start uncertainty moves innings to relief earlier. Very hot Petco conditions widen the upper tail. |
| **3** | **San Diego Padres -1.5** | **41%** | MEDIUM-LOW | Padres have home-field/defence and the stronger likely winner branch, but a 2+ margin requires separation beyond the central game object; Pivetta's return exposure and SD's recent scoring rate make that less likely than a one-run SD win or WSH result. |
| **4** | **Under 8.0 runs** | **36% WIN / 12% PUSH / 52% LOSS** | MEDIUM-LOW | Padres pitching/defence and Petco can suppress scoring, but the joint Irvin-contact plus Pivetta-return/bulk-relief upper tail is too prominent for the Under to outrank the Over. |

**Potential game winner:** **San Diego Padres — 57% `UNVALIDATED_SUBJECTIVE`**.  
This is not a calibrated probability and is not a value/edge claim.

## Identity / participant freeze

- MLB official probable-pitcher pages identify **Jake Irvin (WSH, RHP)** and **Nick Pivetta (SD, RHP)** for this exact Petco Park event.
- MLB transactions on 2026-09-07 show **San Diego activated Nick Pivetta from the 60-day injured list** and optioned Jhony Brito; the starter is therefore active rather than merely a rehab candidate.
- At the final refresh, MLB's official starting-lineup pages still displayed **TBD** for both batting orders. Under `BB-P2`, the card therefore uses lineup mixtures and does **not** treat any secondary projected order as confirmed. This caps lineup-sensitive confidence rather than blocking the team run-line/total slate.

### Material availability

**San Diego:** Nick Pivetta activated today after right elbow/flexor injury; Luis Rengifo is out for 2026 with ACL/MCL injury; Gavin Sheets remains on the injured list with a foot sprain; Jeremiah Estrada has been on the IL with a shoulder impingement.  
**Washington:** James Wood was activated Sep 2; Orlando Ribalta was reported with right-forearm discomfort and expected to miss time; Drew Millas remains out with a fractured finger; Josiah Gray remains on the 60-day IL.

## Starter / bullpen exposure

### Jake Irvin — Washington

- 2026: **2-8, 5.57 ERA, 1.40 WHIP, 87 K in 85.2 IP**.
- Last seven starts: **6.09 ERA**, 34.0 IP, 23 ER, 18 BB, 29 K.
- Last three: 4.0 IP/2 ER vs ATL; 4.1 IP/1 ER but **6 BB** vs COL; 6.0 IP/4 ER at MIA.
- The recent run prevention is mixed rather than clean improvement: walk/traffic risk remains material, and the season/contact baseline cannot be discarded.

### Nick Pivetta — San Diego

- 2026 MLB sample before injury: **1-2, 4.50 ERA, 1.13 WHIP, 24 K in 16.0 IP**.
- He has not made an MLB start since April because of a right flexor/elbow injury.
- Rehab: 47 pitches over 3 innings on Aug 25/26 after an earlier elbow-tightness setback, then 4.1 innings for Triple-A El Paso on Aug 30.
- This is explicitly a **return/small-sample starter mixture** under `RULES_BASEBALL.md`: good-start, ordinary, short-start and early-hook/contact branches remain live. A secondary Padres report identified Randy Vásquez as the likely bulk-relief safety valve behind him.

### Relief-state context

- San Diego received six scoreless innings from Michael King on Sep 6, limiting broad bullpen exposure; Mason Miller worked the ninth and struck out the side for save No. 33.
- Washington played three consecutive games at Dodger Stadium before this trip segment and allowed late runs in each; Will Dion surrendered the decisive three-run homer on Sep 6. Ribalta's forearm issue further reduces one relief option.
- Workload is treated as **availability**, not automatic performance quality.

## L5 / L10 / L15 / L20 trend audit

Derived from the current MLB schedule results through Sep 6, not from sportsbook totals.

| Window | Washington record | WSH RF/G | WSH RA/G | Avg combined runs | San Diego record | SD RF/G | SD RA/G | Avg combined runs |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| L5 | 1-4 | 4.40 | 6.40 | 10.80 | 2-3 | 2.80 | 4.20 | 7.00 |
| L10 | 5-5 | 5.10 | 4.80 | 9.90 | 4-6 | 3.60 | 4.20 | 7.80 |
| L15 | 6-9 | 4.67 | 5.13 | 9.80 | 7-8 | 3.93 | 3.60 | 7.53 |
| L20 | 7-13 | 4.05 | 4.55 | 8.60 | 9-11 | 3.65 | 3.40 | 7.05 |

**Trend test:** the two clubs point in opposite total directions: Washington's recent games have been materially higher scoring while San Diego's have been lower scoring. Therefore recent totals alone receive **zero directional ownership**. The Over lean comes instead from today's pitcher/exposure tree: Irvin's unstable run prevention plus Pivetta's first-start-back uncertainty and the associated relief transition.

## H2H / continuity

The May series in Washington ended SD 7-5, WSH 9-4, WSH 4-2. Washington won that series 2-1. Current starter identities, injury state and several roster roles differ, so this is **context only**, not a weighted directional mechanism.

## Venue / environment gate

Venue-coordinate weather at Petco Park around the game window showed **~93°F / 34°C at 14:03 local**, with the afternoon forecast reaching roughly **35-36°C** and a low precipitation threat. This is unusually hot for coastal San Diego and increases uncertainty around carry/fatigue, but no field-relative wind vector was verified, so heat is used only as a modest upper-tail widening input, not as an automatic Over coefficient.

## Joint event object — explicit arithmetic

### Team-run centres

**Washington prior:** mean of WSH season scoring (5.2 R/G) and SD season runs allowed (4.2 R/G) = **4.70**.  
Adjustments: **-0.35** Padres pitching/defence + Petco context; **-0.15** Pivetta strikeout/WHIP skill prior; **+0.20** first-MLB-start-since-April / short-start relief uncertainty; **-0.20** home-leverage/late-inning SD relief advantage.  
**WSH centre = 4.20 runs.**

**San Diego prior:** mean of SD season scoring (4.2 R/G) and WSH season runs allowed (5.1 R/G) = **4.65**.  
Adjustments: **+0.55** Irvin 5.57 ERA / 6.09 last-seven and traffic/HR tail; **-0.45** Padres L10 scoring suppression (3.6 R/G, .652 OPS); **+0.15** home field + unusually hot conditions.  
**SD centre = 4.90 runs.**

**Joint centre:** **SD 4.9 – WSH 4.2 = 9.1 total runs; SD +0.7 central margin.**  
**Total width:** approximately **3.2 runs** because of Pivetta-return and Irvin-cluster uncertainty.  
**Margin width:** approximately **3.7 runs**.

### Total 8.0 placement

- WSH 3 / SD 5 = **8 push**.
- WSH 4 / SD 5 or WSH 3 / SD 6 = **Over**.
- WSH 3 / SD 4 or WSH 2 / SD 5 = **Under**.
- The 9.1 centre lies above 8.0, but the push mass is meaningful; hence the explicit **52% win / 12% push / 36% loss** Over assessment rather than treating Over as a binary 64% non-loss claim.

### Run-line separation budget

- Central margin: **SD +0.7**.
- SD -1.5 requires a **2+ run win**, which lives primarily in Irvin early-hook / clustered-damage / Washington bullpen-failure states.
- WSH +1.5 wins on every WSH victory plus every one-run SD victory. The Pivetta-return branch and SD's low recent scoring centre materially preserve these paths.
- Therefore the cushion is the highest-probability supplied event even though San Diego remains the likelier outright winner.

## Bidirectional / kill-path audit

- Pivetta returning can **suppress Washington** if his pre-injury swing-and-miss returns, but can also **raise Washington's scoring tail** if he is inefficient/short and the game reaches bulk relief early.
- Hot weather may aid carry but may also be neutralised by marine/field-direction effects that were not verified; no one-sign weather claim is used.
- Padres' recent low scoring supports Washington +1.5, but Irvin's walk/contact/HR tail creates the main kill path: one clustered SD inning can simultaneously beat the cushion and push the total Over.
- A low-scoring game does not automatically mean WSH +1.5 wins; 3-1/4-1 SD remains a live separation branch.

## Settlement source

Use the **official MLB game/box score** as field owner for final score, inning state and listed starters. `RESEARCH_GRADE` and `OPERATOR_ACTION` remain separate because operator-specific listed-pitcher/action terms were not supplied.

## P-335 source register

### Governing Drive sources — read only
- `METHOD.md` — MDS-2026.09.06-v4.0.
- `RULES_GENERAL.md` §16 — current mandatory gate classification/start-state rules.
- `RULES_BASEBALL.md` — SFA-BASEBALL, return/small-sample starter, bullpen and run-line controls.
- `CONTROLS.md` — current quick-reference and Part-3 carry-forward.
- `PREDICTION_LOG_COMBINED_3.md` — active canonical Part-3 authority.

### Public/field sources
- MLB official probable pitchers: https://www.mlb.com/nationals/roster/probable-pitchers
- MLB official starting lineups: https://www.mlb.com/nationals/roster/starting-lineups
- MLB official transactions: https://www.mlb.com/roster/transactions
- Padres official injury/transaction tracker: https://www.mlb.com/news/padres-injuries-and-roster-moves
- Nationals official injury/transaction tracker: https://www.mlb.com/news/nationals-injuries-and-roster-moves
- MLB Nick Pivetta rehab report: https://www.mlb.com/news/nick-pivetta-single-a-rehab-start
- MLB Jake Irvin player/game-log page: https://www.mlb.com/player/jake-irvin-663623?stats=gamelogs-r-pitching-mlb&year=2026
- Baseball Savant Jake Irvin: https://baseballsavant.mlb.com/savant-player/jake-irvin-663623
- StatMuse Padres last 10: https://www.statmuse.com/mlb/ask/padres-last-10-games
- StatMuse Nationals last 10: https://www.statmuse.com/mlb/ask/nationals-last-10-games
- Reuters, Padres 4-3 Yankees (Sep 6): https://www.reuters.com/sports/baseball/padres-open-game-with-3-straight-homers-hold-edge-yankees--flm-2026-09-06/
- Reuters, Dodgers 7-5 Nationals (Sep 6/7): https://www.reuters.com/sports/baseball/mookie-betts-blast-lifts-dodgers-over-nationals--flm-2026-09-07/
- theScore matchup/team-season comparison: https://www.thescore.com/mlb/event/98277
- Baseball-Reference game preview/H2H: https://www.baseball-reference.com/previews/2026/SDN202609070.shtml
- Venue weather cross-check: https://www.timeanddate.com/weather/%405382258/hourly
- Structured MLB schedule results used to reconstruct L5/L10/L15/L20 through Sep 6.
- Structured venue-coordinate Petco Park weather feed used at final refresh.

**No sportsbook odds, market consensus, line movement or tipster analysis was used as predictive evidence.**
## 2026-09-09 full settlement + retrospective addendum

### Official result and row settlement

**Final:** San Diego Padres 3, Washington Nationals 2. MLB's postgame record confirms Nick Pivetta returned with **5.0 scoreless innings** and San Diego won by exactly one run.

| Rank | Frozen row | p | Result | Brier |
|---:|---|---:|---|---:|
| 1 | Washington Nationals +1.5 | 0.59 | **WIN** | 0.1681 |
| 2 | Over 8.0 | 0.52 win probability | **LOSS** | 0.2704 |
| 3 | San Diego Padres -1.5 | 0.41 | **LOSS** | 0.1681 |
| 4 | Under 8.0 | 0.36 win probability | **WIN** | 0.4096 |

**Potential winner:** Padres — **CORRECT**.  
**Card mean Brier:** **0.2541**.  
**Population:** `PRIMARY_SCORED — MLB`; this is the only local card in this mini-log that changes the headline primary population scorecard.

### What actually happened

The strongest outcome driver was the **best-case branch of Pivetta's return distribution**. The pregame card treated his first MLB start since April as a wide good/ordinary/short-start mixture, but the realized state was five scoreless innings. Washington therefore never accessed the upper-scoring branch that had helped lift the total centre to 9.1. Jake Irvin allowed three runs, enough for the Padres winner call, but the game never developed the bilateral scoring needed for Over 8.0.

The **separation logic was substantially better than the total logic**. San Diego won, but by one run, exactly the state that made Washington +1.5 Rank #1 and Padres -1.5 a loss.

### Three-question retrospective

1. **What did the score turn on?** Pivetta supplied five scoreless innings in his return, San Diego generated the necessary three runs against Irvin, and Washington's late scoring stopped at two. The result was a low-total one-run Padres win.
2. **Was the driver knowable and in the card?** **Partly yes.** The card explicitly modelled Pivetta as a return/small-sample mixture and stated that a strong return could suppress Washington. What was wrong was the mass allocation: the analysis gave too much directional force to "return uncertainty → earlier relief/upper total tail" and too little to a normal/strong five-inning return. The exact realized five scoreless innings were not knowable.
3. **Smallest routine change:** for a returning MLB starter, explicitly quantify a **normal/strong 4–5 inning branch** using the freshest rehab pitch count, velocity/command and recovery reports before converting "return uncertainty" into a net Over adjustment.

### Expanded/deep review

**What went right**
- Rank #1 cushion and potential winner were both correct.
- The one-run/favourite-win coexistence was correctly represented.
- The card correctly warned that a low-scoring game could still produce a Padres win without -1.5 separation.

**What went wrong**
- The 9.1 total centre was materially too high relative to the realized five runs.
- Pivetta's rehab/return uncertainty was treated asymmetrically: the short-start/relief tail had a visible +0.20 scoring adjustment, but the strong return branch was not assigned comparable explicit mass.
- The total forecast effectively over-read uncertainty as scoring direction.

**Process grade:** **B-** — strong margin decomposition and correct Rank #1/winner, but the total object did not weight the return-starter branches well enough.

### Learning / rule disposition

**No new rule.** `RULES_BASEBALL.md` controls 11 and 13 already require a small-sample/return mixture and an explicit season-prior versus current-regime branch. This is an **application/tuning failure**, not a missing-framework failure.

**Where this belongs on Drive after reconciliation:** settlement + retrospective in `PREDICTION_LOG_COMBINED_3.md`; no new `CONTROLS.md` promotion.

### New decisive source

- MLB official postgame video/recap: https://www.mlb.com/padres/video/pivetta-s-scoreless-start-merrill-s-big-day-fuel-win



---

# P-336 — Carabobo FC vs Estudiantes de Mérida — Venezuela Primera División, Torneo Clausura J8

## Controlling status

**GAME-STATE:** PREGAME  
**Forecast cutoff / final volatile refresh:** **2026-09-08 07:38:00 AEST** (2026-09-07 17:38:00 VET)  
**Scheduled start:** **2026-09-08 08:00 AEST / 2026-09-07 18:00 VET**  
**Venue:** Estadio Polideportivo Misael Delgado, Valencia, Venezuela  
**Method:** `MDS-2026.09.06-v4.0 — SPORTS_ONLY / MARKET_BLIND`  
**Population:** `EXPLORATORY — NOT SCORED`  
**Retrospective:** **NOT PERFORMED — user requested none yet**  
**Operator endpoint/definition:** standard regulation assumptions for goal contracts; no operator-specific corner definition supplied. `RESEARCH_GRADE` and `OPERATOR_ACTION` remain separate at settlement.

## Queue state before issuance

- `P-335` Washington Nationals @ San Diego Padres is **LIVE / PENDING SETTLEMENT** and remains at the top unresolved queue. It was not final, so no retrospective/settlement was performed.
- `P-333` and `P-334` remain administratively closed with no issued forecast rows.
- This new event therefore occupies local continuation slot **`P-336`**.

## New-competition onboarding record

The current Drive `LEAGUE_RULES_SOCCER.md` did not expose a Venezuela Primera División section during the fresh read. Current Drive rules require new-competition onboarding before forecasting. Because Drive is read-only under the user's standing instruction, the verified onboarding facts are recorded here rather than written back to Drive:

- competition: **Liga FUTVE / Venezuelan Primera División, 2026 Torneo Clausura**;
- this fixture: **Clausura first stage, Jornada 8**;
- current first stage is a **14-team, 13-match** short tournament; official Liga FUTVE coverage shows the top eight progressing to the final phase, which uses two four-team quadrangular groups in the 2026 edition;
- this is an ordinary league fixture: the regulation-result endpoint is **90 minutes plus stoppage time**, with a draw permitted; no extra time or penalties apply to the supplied goal/corner rows;
- standard IFAB 2026 Laws apply unless a competition-specific rule is documented otherwise.

No unverified claim about VAR, foreign-player quotas or operator corner settlement is added.

## Frozen candidate slate

The user supplied both sides of two exact goal targets. The fifth row is an independently researched corner target, as requested.

1. First-half goals **Over 0.5**
2. First-half goals **Under 0.5**
3. Full-time combined goals **Over 2.5**
4. Full-time combined goals **Under 2.5**
5. Full-time total match corners **Over 7.5**

## Final ranked forecast

| Rank | Pick | `UNVALIDATED_SUBJECTIVE` probability | Evidence grade | Core reason |
|---:|---|---:|---|---|
| **1** | **Under 2.5 total goals** | **60%** | **MEDIUM** | Carabobo's 2026 home matches are Under 2.5 in 71%; their current Clausura home games are 2-0, 1-0 and 0-0, while Estudiantes' L10 league environment is only 2.00 total goals/game. Carabobo's disrupted 4-3 loss is not allowed to own the baseline because it included a 27' red card. |
| **2** | **Over 7.5 total match corners** | **59%** | **FORCED RANK / LOW** | Carabobo matches average 9.22 corners and Estudiantes 9.50; Over 7.5 has occurred in roughly 70% and 57-58% respectively. However, the exact current width/cross/block/end-line chain and operator/provider definition are incomplete, so the soccer derivative rule prevents a stronger label. |
| **3** | **1H Over 0.5 goals** | **56%** | **MEDIUM-LOW** | Conflicting first-half profiles: Carabobo home 1H Over 0.5 is only 36%, but Estudiantes away is 77%. Estudiantes' latest 1-1 with UCV had both goals by 23', while the latest Carabobo-Estudiantes meeting was 0-0 at HT. This supports only a narrow Over lean. |
| **4** | **1H Under 0.5 goals** | **44%** | **MEDIUM-LOW** | Exact complement of the 1H Over. Carabobo's 86% home first-half clean-sheet rate and 64% home 0-0-HT frequency preserve a substantial scoreless-half branch, but Estudiantes' away first-half goal environment prevents it from outranking the Over. |
| **5** | **Over 2.5 total goals** | **40%** | **MEDIUM-LOW** | Exact complement of the FT Under. Eric Ramírez's return, Estudiantes' improved current attack and Carabobo's defensive absences create an upper tail, but the ordinary centre remains below 2.5. |

**Potential regulation winner:** **Carabobo FC — 52% `UNVALIDATED_SUBJECTIVE`**  
Indicative 1X2 distribution used for coherence: **Carabobo 52% / Draw 29% / Estudiantes 19%**. This is not a calibrated model probability and not a value/edge claim.

## Identity, participants and current availability

### Carabobo — field-owner verified

Carabobo's official 6 September preview confirms:

- **Eric Ramírez returns from suspension**. He has seven 2026 goals, second on the club behind Loureins Martínez (eight).
- **Ángelo Lucena** remains out recovering from an ACL tear plus posterior medial-meniscus injury.
- **Franner López** is out with a medial collateral ligament sprain.
- **Ezequiel Neira is suspended** after his direct red card against Rayo Zuliano.

Official match squad:

- GK: Miguel Silva, Keiber Roa.
- Defenders: Leonardo Aponte, José Durán, Franyer Oliveros, Alexander González, Jonathan Bilbao.
- Midfield: Edson Castillo, Abraham Bahachille, Juan Camilo Pérez, Maurice Cova, Dimas Meza, Sebastián Mendoza.
- Attack: Bryan Castillo, Yohandry Orozco, Darwin Machís, Joshuan Berríos, Loureins Martínez, Exon Arzú, Eric Ramírez.

Carabobo's most recent XI in the 4-3 Rayo Zuliano match was Miguel Silva; José Durán, Jonathan Bilbao, Jean Fuentes; Juan Camilo Pérez, Yohandry Orozco, Matías Núñez, Sebastián Mendoza, Dimas Meza; Loureins Martínez and Bryan Castillo. The game was heavily distorted by Neira's 27' red card and is flagged as a disrupted match for descriptive learning only.

### Estudiantes de Mérida

The latest official Liga FUTVE match report, the 1-1 draw with UCV on 3 September, lists:

**Eddie Roberts; Héctor Acosta, Luis Caicedo, Christopher Rodríguez, José Montilla; Cristhian Rivas, Wilken Ramírez, Andrés Montero; Darwin Matheus, Romeesh Ivey, Jesús Hernández.** Coach: **Jesús Gómez**.

The same report records substitute use including Cristian Caicedo, Ronaldo Chacón, Angelo Peña, Ender Albarrán and Geovan Montes.

Current roster-regime context: former leading striker **Kevin Quejada (12 goals)** transferred abroad before the Clausura; **Jesús Hernández** returned and had three goals in his first five matches of the current run, so the older Quejada-era H2H is not treated as a full current-attacking-strength proxy.

**Participant status at cutoff:** Carabobo official squad/absences are verified; **same-day official starting XIs for both teams and a same-day Estudiantes injury release were not found before the 07:38 AEST cutoff**. Therefore no player is invented as a confirmed starter and side confidence is capped at MEDIUM-LOW under `SO-P2`.

## L5 / L10 / L15 / L20 league-only trend audit

The windows below are reconstructed from 2026 Venezuelan league results only, excluding CONMEBOL matches so competition populations are not mixed.

| Window | Carabobo W-D-L | GF-GA | Combined goals/game | O2.5 | Estudiantes W-D-L | GF-GA | Combined goals/game | O2.5 |
|---|---:|---:|---:|---:|---:|---:|---:|
| **L5** | 1-2-2 | 5-6 | **2.20** | 1/5 | 2-2-1 | 5-6 | **2.20** | 2/5 |
| **L10** | 4-3-3 | 15-10 | **2.50** | 3/10 | 3-3-4 | 8-12 | **2.00** | 3/10 |
| **L15** | 6-4-5 | 20-15 | **2.33** | 5/15 | 5-3-7 | 13-20 | **2.20** | 5/15 |
| **L20** | 8-6-6 | 34-25 | **2.95** | 8/20 | 8-4-8 | 21-25 | **2.30** | 7/20 |

**Trend test:** the longest Carabobo window is higher scoring because it includes several high-scoring spring fixtures (including 6-3 and 4-2). That history is not silently discarded, but the more current L5/L15 environment is lower and the home-specific 2026 data are especially restrictive. The current Under lean therefore comes from a venue/current-regime mixture, not a simple streak rule.

## Home/away and first-half process

### Carabobo at home — 2026 league

- 1.71 goals scored/game, 0.57 conceded/game.
- 2026 home match-goal average: **2.29**.
- **Under 2.5: 71%**.
- First-half match-goal average: **0.86**.
- **1H Over 0.5: 36%; 1H Under 0.5: 64%**.
- Home 1H clean sheet: **86%**.

Carabobo's official club preview adds that they are unbeaten at the Misael Delgado in domestic play and have conceded **zero goals in their three Clausura home fixtures**, scoring three.

### Estudiantes away — 2026 league

- 1.08 goals scored/game, 1.38 conceded/game.
- Away Under 2.5: **54%**.
- First-half match-goal average: **1.31**.
- **1H Over 0.5: 77%; 1H Under 0.5: 23%**.
- Estudiantes have failed to score in 46% of away league games.

This is the key first-half conflict: Carabobo's home first halves are very quiet, while Estudiantes' away first halves are much more likely to contain a goal. The rank therefore stays close to 50/50 rather than pretending one sample owns the outcome.

## H2H and continuity audit

Carabobo's official club preview records 70 historical meetings: **Carabobo 34 wins, 21 draws, Estudiantes 15 wins**. Across the most recent 10, Carabobo are **7-2-1**, goals **16-5**, and the club says it has not lost this fixture at the Misael Delgado since 2001.

The two most recent May 2026 meetings were Carabobo **1-0** Estudiantes and Estudiantes **0-2** Carabobo; the latter was **0-0 at half-time**, with goals at 73' and 88'. In March, Estudiantes won 3-2 and the first two goals came at 8' and 23'. These opposite phase profiles reinforce the current first-half uncertainty.

Continuity is incomplete: Quejada has left Estudiantes, Jesús Hernández now leads the central-striker replacement branch, Carabobo have added players including Darwin Machís/Exon Arzú, and today's absences differ from May. H2H therefore supports context/home-effect but does not receive standalone deterministic weight.

## Goal joint event object — explicit arithmetic

### Step 1 — home/away prior

Carabobo home attacking prior against Estudiantes away defence:

`(Carabobo home GF 1.71 + Estudiantes away GA 1.38) / 2 = 1.545`

Estudiantes away attacking prior against Carabobo home defence:

`(Estudiantes away GF 1.08 + Carabobo home GA 0.57) / 2 = 0.825`

**Venue/home-away base total = 2.370 goals.**

### Step 2 — current Clausura shrinkage

Through seven Clausura games:

- Carabobo: 7 GF + 7 GA = 14 total goals / 7 = **2.00**.
- Estudiantes: 8 GF + 8 GA = 16 / 7 = **2.286**.
- current two-team Clausura environment midpoint = **2.143**.

Use an explicit qualitative mixture rather than allowing either sample to dominate:

`0.60 × 2.370 + 0.40 × 2.143 = 2.279`

### Step 3 — signed current-personnel adjustments

- **+0.10** Carabobo attack: Eric Ramírez returns.
- **+0.05** Estudiantes scoring tail: Neira suspension weakens one Carabobo defensive branch.
- **-0.04** total attacking/depth exposure: Lucena + Franner López unavailable reduces Carabobo midfield/depth options.
- **0.00 signed weather adjustment:** forecasts disagree on shower probability and no exact surface degradation was established; weather increases width, not direction.

**Final working total centre ≈ 2.39 goals.**  
**Working total width ≈ ±1.55 goals.**

Line placement: **2.5 is only slightly above the centre**, so Under is a moderate 60% lean, not a high-certainty selection. The 4+ goal branch remains material through Ramírez/Martínez, Estudiantes' current recovery and transition/set-piece variance.

## First-half event object

Observed venue/side phase rates pull in opposite directions:

- Carabobo home 1H average total: **0.86**; O0.5 **36%**.
- Estudiantes away 1H average total: **1.31**; O0.5 **77%**.

Simple phase midpoint:

`(0.86 + 1.31) / 2 = 1.085 first-half goals`

Empirical O0.5 midpoint:

`(36% + 77%) / 2 = 56.5%`

After a small uncertainty haircut for unresolved XIs/keeper confirmation and the strong Carabobo home 1H suppression branch, the published qualitative assessment is **56% 1H Over 0.5 / 44% Under 0.5**.

## Corner process and derivative-completeness audit

Current 2026 statistical sources show:

- Carabobo matches: **9.22 total corners/game**, Carabobo winning **5.81/game**; Over 7.5 in **70%**.
- Estudiantes matches: approximately **9.50 total corners/game**; Over 7.5 around **57-58%**.
- Primera División overall: about **8.72 total corners/game**.

Base match-corner centre:

`(9.22 + 9.50) / 2 = 9.36 corners`

Empirical O7.5 midpoint:

`(70% + 58%) / 2 ≈ 64%`

However `RULES_SOCCER.md` requires current direct corner-causing evidence (width/crosses/blocked crosses/end-line entries/clearances/set plays), score-state branches and an exact settling provider/definition before a corner row may be labelled LEAN/SUPPORTED. Those layers were **not fully recoverable before cutoff**, and no operator-specific corner definition was supplied.

Accordingly the row is deliberately reduced to **59% `UNVALIDATED_SUBJECTIVE`, FORCED RANK / LOW evidence**. The data justify including it in the five-row order; they do **not** justify pretending the derivative-completeness gate was satisfied.

## Weather / surface gate

Venue-coordinate game-window forecast for Misael Delgado / Valencia:

- around 17:00 local: mostly cloudy, roughly 32°C;
- around scheduled 18:00: warm/humid, with sources ranging from near-zero rain to roughly mid-20% shower probability;
- later evening shower probability rises modestly in one forecast.

No reliable exact-pitch surface report showed waterlogging, poor drainage or material degradation before cutoff. Therefore weather gets **no automatic Under or corner sign**. Heat/humidity and shower uncertainty widen late-game pace/substitution and surface branches only.

## Potential winner — Carabobo FC 52%

Positive Carabobo mechanisms:

1. strong 2026 home record and only 0.57 league goals conceded/game at home;
2. unbeaten domestic record at Misael Delgado in the official club preview;
3. no Clausura home goals conceded entering this match;
4. Eric Ramírez returns;
5. official H2H: 7-2-1 across the latest 10 and no home loss to Estudiantes at Misael Delgado since 2001.

Counterweights:

1. Neira suspended plus Lucena/Franner López unavailable;
2. Estudiantes are 3-3-1 in this Clausura and have taken five points from their last three;
3. Jesús Hernández has partly replaced Quejada's scoring role;
4. same-day official XIs were still unresolved at cutoff.

Those counterweights prevent a stronger home-win probability. A draw remains a large branch in a game whose central score object is near **Carabobo 1.5 – Estudiantes 0.9**.

## Final ordered card

1. **Under 2.5 total goals — 60%**
2. **Over 7.5 total match corners — 59% — FORCED RANK / LOW derivative evidence**
3. **1H Over 0.5 goals — 56%**
4. **1H Under 0.5 goals — 44%**
5. **Over 2.5 total goals — 40%**

**Potential regulation winner: Carabobo FC — 52%.**

All numbers above are `UNVALIDATED_SUBJECTIVE` analyst probabilities under MDS v4.0, not calibrated/validated model probabilities and not price/value claims.

## P-336 source register

### Governing Google Drive sources — READ ONLY

- `METHOD.md` — `MDS-2026.09.06-v4.0` lifecycle, probability, source, arithmetic and settlement requirements.
- `RULES_GENERAL.md` §16 — current gate classification, state/start-crossing, new-competition onboarding and participant rules.
- `RULES_SOCCER.md` — `SFA-SOCCER`, goal/corner process separation, participant cap, early-goal reconciliation and derivative completeness.
- `LEAGUE_RULES_SOCCER.md` — IFAB/current competition reference; Venezuela section not found in the current Drive copy, triggering local onboarding.
- `CONTROLS.md` — current quick-reference controls and candidate-watch firewall.
- `PREDICTION_LOG_COMBINED_3.md` — active canonical Part-3 authority (`P-333` onward).

### Field-owner / official sources

- Carabobo official fixture/preview and current squad/absences: https://www.carabobofc.org/noticia.php?id=1035
- Carabobo official club home/calendar: https://www.carabobofc.org/
- Carabobo official Rayo Zuliano match report/red-card record: https://www.carabobofc.org/noticia.php?id=1033
- Carabobo official May H2H match sheet: https://carabobofc.org/partido.php?id=269
- Liga FUTVE current table: https://ligafutve.org/clasificacion-liga-futve/
- Liga FUTVE Estudiantes 1-1 UCV match report/current XI: https://ligafutve.org/estudiantes-salvo-un-punto-en-su-recinto/
- Liga FUTVE Jesús Hernández/current-striker regime feature: https://ligafutve.org/jesus-hernandez-apago-las-alarmas-de-estudiantes-tras-la-ida-de-quejada/

### Statistical / schedule sources

- FBref Carabobo 2026 scores/fixtures: https://fbref.com/en/squads/90e07850/2026/matchlogs/c105/schedule/Carabobo-Scores-and-Fixtures-Venezuelan-Primera-Division
- FBref Estudiantes de Mérida 2026 scores/fixtures: https://fbref.com/en/squads/dcbc2e42/2026/matchlogs/c105/schedule/Estudiantes-de-Merida-Scores-and-Fixtures-Venezuelan-Primera-Division
- BeSoccer Carabobo full 2026 result sequence: https://www.besoccer.com/team/matches/carabobo
- BeSoccer Estudiantes full 2026 result sequence: https://es.besoccer.com/equipo/partidos/estudiantes-merida-fc
- FootyStats Carabobo home/1H/goal profile: https://footystats.org/clubs/carabobo-fc-2848
- FootyStats Estudiantes away/1H/goal profile: https://footystats.org/clubs/estudiantes-de-merida-fc-2850
- OddAlerts Primera División 2026 corner statistics: https://www.oddalerts.com/leagues/venezuela/primera-division/corners
- APWin Primera División 2026 corner context: https://www.apwin.com/league/venezuela/primera-division/corners/
- PerformanceOdds match-corner statistical cross-check: https://www.performanceodds.com/fixtures_match/8629306/

### Conditions source

- Venue-coordinate weather feed for Estadio Polideportivo Misael Delgado / Valencia at 17:00-20:00 VET on 2026-09-07.
- Hourly weather cross-check: https://www.tiempo.es/venezuela/valencia/hora-a-hora

**Explicit exclusions:** no sportsbook price, bookmaker consensus, line movement, tipster prediction, AI simulation or synthetic result was used as predictive evidence. Search results containing odds/tips were excluded from the decision process.

**Next local continuation slot:** `P-337`.
## 2026-09-09 full settlement + retrospective addendum

### Verified final and post-match process fields

**Carabobo 1-0 Estudiantes de Mérida; HT 1-0.** Eric Ramírez scored in the 30th minute. Current post-final statistics report **Carabobo 3 corners, Estudiantes 9; shots 15-27; shots on target 4-8**.

| Rank | Frozen row | p | Result | Brier |
|---:|---|---:|---|---:|
| 1 | Under 2.5 goals | 0.60 | **WIN** | 0.1600 |
| 2 | Over 7.5 total corners | 0.59 | **WIN** | 0.1681 |
| 3 | 1H Over 0.5 goals | 0.56 | **WIN** | 0.1936 |
| 4 | 1H Under 0.5 goals | 0.44 | **LOSS** | 0.1936 |
| 5 | Over 2.5 goals | 0.40 | **LOSS** | 0.1600 |

**Potential winner:** Carabobo — **CORRECT**.  
**Card mean Brier:** **0.1751** (`EXPLORATORY`, not added to the primary scorecard).

### What actually happened

The 1-0 score validates the literal Under result but **does not validate a low-event match mechanism**. Estudiantes produced 27 shots, eight on target and nine corners. The realized clean sheet was therefore a combination of Carabobo goalkeeping/defensive resolution and Estudiantes finishing inefficiency, not simple territorial suppression. Carabobo's attacking winner came through **Eric Ramírez**, whose return from suspension was explicitly identified before issue.

### Three-question retrospective

1. **What did the score turn on?** Ramírez converted Carabobo's first-half opportunity, while Estudiantes generated substantial territory/shot/corner volume without converting any of it.
2. **Was the driver knowable and in the card?** **Partly.** Ramírez's return was known and directly included. The card also acknowledged Estudiantes' improving attack. However, the Under case leaned heavily on Carabobo's home clean sheets and low goal outcomes without enough explicit separation of **chance creation vs finishing vs goalkeeping**.
3. **Smallest routine change:** whenever a soccer Under is supported by a run of clean sheets/low scores, place current **shots/xG/SOT creation and goalkeeper/finishing decomposition** beside the outcome rates before treating the low-score history as a low-event mechanism.

### What went right / wrong

**Right:** result, corners, first-half goal and winner all aligned; the corner pick was supported by a genuinely high-event attacking state despite the low final score.  
**Wrong/process caution:** the scoreline alone would make the Under reasoning look stronger than it was. This is exactly the retrospective trap the soccer rules are designed to prevent.

**Process grade:** **B+** — strong card-level results, but the post-match mechanism shows the Under thesis was partly outcome-driven.

### Learning / rule disposition

No new rule. `RULES_SOCCER.md` already says recent goals/clean sheets are outcomes and requires creation, finishing and goalkeeping to be separated. Record this as an **application reminder** only.

**Potential destination if recurrence appears:** `LEARNING_REGISTER.md` observation; not a new `CONTROLS.md` rule from one exploratory event.

### New sources

- Carabobo official report: https://www.carabobofc.org/noticia.php?id=1036
- Post-final structured stats: https://www.playmakerstats.com/match/2026-09-07-carabobo-estudiantes-de-merida/12415032



---

# P-337 — Barracas Central vs Argentinos Juniors — Argentina Liga Profesional, Torneo Clausura 2026, Fecha 8

## Controlling status

**Local external continuation ID:** `P-337`  
**Method:** `MDS-2026.09.06-v4.0 — SPORTS_ONLY / MARKET_BLIND`  
**Population:** `EXPLORATORY — NOT SCORED`  
**GAME-STATE:** `PREGAME`  
**Forecast freeze:** **2026-09-08 07:49:09 AEST** / 2026-09-07 18:49:09 Argentina time  
**Scheduled kickoff:** **2026-09-08 08:00 AEST** / **2026-09-07 19:00 ART**  
**Venue:** Estadio Claudio Fabián “Chiqui” Tapia, Buenos Aires  
**Regulation endpoint:** 90 minutes + stoppage time; draw is a live league result; no extra time  
**User-requested retrospective:** **NOT PERFORMED**  
**Next local ID after issuance:** `P-338`

## 1. Frozen candidate slate and ranking

| Rank | Contract | `UNVALIDATED_SUBJECTIVE` probability | Evidence state |
|---:|---|---:|---|
| **1** | **Under 2.5 total goals** | **65%** | `SUPPORTED / MEDIUM` |
| **2** | **1st Half Over 0.5 goals** | **60%** | `LEAN / MEDIUM` |
| **3** | **Argentinos Juniors team corners Over 4.5** | **58%** | `FORCED RANK / LOW` — operator/provider corner definition not supplied |
| **4** | **1st Half Under 0.5 goals** | **40%** | `MEDIUM-LOW` |
| **5** | **Over 2.5 total goals** | **35%** | `MEDIUM-LOW` |

**Potential regulation winner:** **Argentinos Juniors — 46%**  
**Coherent 1X2 split:** Argentinos Juniors **46%** / Draw **31%** / Barracas Central **23%**.

The half-point complementary goal rows are internally coherent: `P(U2.5)=65%`, `P(O2.5)=35%`; `P(1H O0.5)=60%`, `P(1H U0.5)=40%`.

## 2. Identity, rules and schedule freeze

LPF and Barracas' official preview both list the fixture for **Monday 7 September at 19:00 Argentina time**, Estadio Chiqui Tapia, Clausura Fecha 8, Zone B. LPF lists **Leandro Rey Hilfer** as referee, **Héctor Paletta** as VAR and **Lucas Germanotta** as AVAR.

Current Drive `LEAGUE_RULES_SOCCER.md` records the 2026 Liga Profesional structure as Apertura/Clausura, two zones, top eight in each zone advancing to single-match playoffs. This is a regular-phase league match: the ranked goal rows and potential winner settle on regulation time only.

## 3. Current participant / availability gate

**Barracas Central — coach Damián Ayude.** Current 365Scores/TyC coverage lists a 5-3-2 structure around Marcelo Miño in goal, with Damián Martínez / Nicolás Demartini / Yonatthan Rak / Kevin Jappert / Elías Pereyra, midfield Dardo Miloc / Tomás Porra / Iván Tapia, and Norberto Briasco / Facundo Bruera as the current starting group. TyC still labelled the Barracas XI as possible rather than field-owner confirmed at the research cutoff. 365Scores lists **Fernando Tobio** and **Manuel Duarte** unavailable.

**Argentinos Juniors — coach Nicolás Diez.** Current match coverage lists **Brayan Cortés; Kevin Coronel, Franco Vázquez, Francisco Álvarez, Sebastián Prieto; Kevin Gutiérrez, Nicolás Oroz, Hernán López Muñoz; Gastón Verón, Tomás Molina, Diego Porcel.** The available bench list includes Gonzalo Siri, Erik Godoy, Franco Paredes, Alan Núñez, Claudio Bravo, Gabriel Florentín, Emiliano Viveros, Iván Morales, Matías Giménez, Alan Alcaraz and Facundo Jainikoski. **Alan Lescano is listed unavailable**, consistent with the reported agreement for his move to Vasco da Gama.

Because the official clubs/LPF had not exposed a full field-owner-confirmed XI/bench package at the freeze, side confidence is capped. The goal totals are less participant-dependent but still carry wider tails; the corner derivative is `FORCED RANK / LOW` because the user's operator definition was not supplied.

## 4. Current Clausura process comparison

Through seven Clausura matches:

| Metric | Barracas | Argentinos |
|---|---:|---:|
| Record | 3-1-3 | 5-1-1 |
| Points | 10 | 16 |
| Goals for | 4 | 12 |
| Goals against | 5 | 7 |
| Goals for/game | 0.57 | 1.71 |
| xG/game | 0.91 | 1.56 |
| Shots/game | 11.14 | 15.71 |
| Corners/game | 3.14 | 5.57 |

Argentinos therefore own the stronger current chance-volume and finishing environment, but Barracas' games remain extremely compressed. The side edge is clearer than the evidence for a high combined-goal environment.

## 5. Required L5/L10/L15/L20 trend audit — regular league results

### Barracas Central

| Window | GF/game | GA/game | Combined goals/game | Under 2.5 |
|---|---:|---:|---:|---:|
| L5 | 0.40 | 1.00 | **1.40** | 4/5 |
| L10 | 0.60 | 0.80 | **1.40** | 8/10 |
| L15 | 0.87 | 0.87 | **1.73** | 9/15 |
| L20 | 0.90 | 0.90 | **1.80** | 13/20 |

### Argentinos Juniors

| Window | GF/game | GA/game | Combined goals/game | Under 2.5 |
|---|---:|---:|---:|---:|
| L5 | 1.20 | 1.00 | **2.20** | 3/5 |
| L10 | 1.50 | 1.00 | **2.50** | 5/10 |
| L15 | 1.60 | 1.07 | **2.67** | 7/15 |
| L20 | 1.40 | 1.00 | **2.40** | 11/20 |

**Trend interpretation:** Barracas' low-output environment is persistent across every window; Argentinos are more productive and more volatile. The Under is therefore not based on a single recent result. Conversely, Argentinos' stronger current attack prevents the Under from being pushed into an extreme probability.

## 6. Season / venue priors

FootyStats' 2026 league sample gives:

- **Barracas:** 0.83 GF and 0.87 GA overall; at home **1.00 GF / 1.00 GA**; **70% Under 2.5 overall**, 55% Under 2.5 at home; first-half Over 0.5 **61% overall / 82% home**.
- **Argentinos:** 1.27 GF and 0.81 GA overall; away **1.09 GF / 1.27 GA**; **65% Under 2.5 overall / 64% away**; first-half Over 0.5 **62% overall / 73% away**.

The important split is that the full-match total profile is low, while both teams' first-half venue splits still produce a first-half goal relatively often. That supports `Under 2.5 FT + 1H Over 0.5` as a coherent state: one early goal followed by a controlled 1-0 / 1-1 / 2-0 type game is entirely compatible with both picks.

## 7. First-half goal process

Current Clausura match-by-match review gives a first-half goal in **4/7 Barracas matches** and **6/7 Argentinos matches**. Season venue priors are also relatively supportive of at least one first-half goal (Barracas home O0.5 1H 82%; Argentinos away 73%), although those season rates are not treated as deterministic because current participants and match state differ.

Lescano's absence removes one important Argentinos creator/finisher, so the early-goal probability is shrunk rather than copied from the raw 6/7 recent rate. Final assessment: **1H Over 0.5 60% / Under 0.5 40%**.

## 8. Explicit goal arithmetic / joint event object

### Team-score prior

Barracas home scoring / Argentinos away concession midpoint:

`(1.00 + 1.27) / 2 = 1.135`

Argentinos away scoring / Barracas home concession midpoint:

`(1.09 + 1.00) / 2 = 1.045`

Raw combined prior:

`1.135 + 1.045 = 2.180 goals`

### Signed current-regime adjustments

- Argentinos current Clausura creation advantage (1.56 xG/game; 15.71 shots/game): **+0.15**
- Barracas persistent recent scoring suppression (L5/L10 combined environment 1.40): **-0.20**
- Alan Lescano unavailable from current Argentinos attack: **-0.08**
- Barracas compact / low-output current regime: **-0.05**
- clear, cool venue-targeted weather with no supported scoring mechanism: **+0.00**

`2.180 + 0.15 - 0.20 - 0.08 - 0.05 = 2.00`

**Working total centre: ~2.0 goals.**  
**Practical central corridor:** roughly **1–3 goals**, with a meaningful but subordinate 3+ tail.  
This locates **2.5 above the centre**, yielding **Under 2.5 = 65%** and **Over 2.5 = 35%** as `UNVALIDATED_SUBJECTIVE` probabilities.

### Regulation separation

The centre does not require an Argentinos multi-goal win. A plausible central grid places most mass around 0-1, 1-1, 0-0 and 1-0, with 0-2 / 1-2 as the main Argentinos separation tail. The stronger current Argentinos process produces the winner split **46/31/23**, but the large draw band prevents a high-confidence outright side call.

## 9. Corner process — separate from goals

The corner row is **Argentinos Juniors team corners Over 4.5**, not a total-corners proxy.

Evidence chain:

- Current Clausura: Barracas **3.14 corners for/game**, Argentinos **5.57**.
- FotMob's 2026 Liga Profesional table has **Argentinos first in total corners taken (151)**, while Barracas are last (54) in the cited season table.
- FotMob also places Argentinos around **5.3 accurate crosses/game**, versus Barracas around **2.9–3.0**, providing an actual width/cross mechanism rather than using goals/possession as a corner proxy.
- Eight recent H2Hs in Scores24 total **70 corners (8.75/game)**, split **50 Argentinos / 20 Barracas**, supporting a large historical Argentinos corner share.
- Leading-state kill path: an early Argentinos goal can reduce later attacking/corner demand; this is why the row is not assigned a high probability despite strong share/width evidence.
- Trailing-state path: if Barracas score first or hold 0-0 late, Argentinos' width and volume can increase corner exposure.

**Probability:** **58% Over 4.5 team corners.**  
**Evidence cap:** `FORCED RANK / LOW` because the operator's exact corner-settlement provider/definition was not supplied. Planned research settlement source: a defined post-final match-stat provider such as FotMob/Opta or 365Scores, with `OPERATOR_ACTION = UNKNOWN_DEFINITION` unless operator terms are later supplied.

## 10. Potential winner

**Argentinos Juniors — 46% regulation.**

Supporting mechanisms:

- 16 points from 7 Clausura matches versus Barracas' 10;
- 12-7 goals versus 4-5;
- 1.56 xG and 15.71 shots/game versus Barracas' 0.91 and 11.14;
- stronger cross/corner territory;
- Argentinos' defence is among the better full-season xGA groups in the league.

Counterweights:

- Argentinos are only 4-3-4 away in the broader 2026 league sample;
- Lescano is unavailable;
- Barracas' home environment is low-event and draw-friendly;
- participant confirmation is not fully field-owner complete.

Hence the winner is a **plurality, not a majority lock**: Argentinos 46%, Draw 31%, Barracas 23%.

## 11. Match conditions

Venue-targeted hourly weather search for Estadio Claudio Chiqui Tapia resolved to the Buenos Aires grid: approximately **10–11°C, clear**, with no material rain signal around kickoff. No signed goal/corner adjustment is assigned because no supported mechanism from wind, rain or surface condition was established.

## 12. Kill paths / honesty audit

**Under 2.5 loses if:** Argentinos convert their superior chance volume efficiently, Barracas are forced into a chase, or an early penalty/red card breaks the low-event structure.

**1H Over 0.5 loses if:** Barracas' compression succeeds and Lescano's absence lowers Argentinos' early final-third quality enough to preserve 0-0 through halftime.

**Argentinos corners O4.5 loses if:** Argentinos score early and manage the game centrally, or their attacks resolve into shots/goals without repeated blocked/cross/end-line actions.

**Argentinos winner loses if:** Barracas turn the low-event state into a draw or convert one set piece/transition while denying Argentinos clean chances.

No outcome is described as certain, safe or calibrated. No bookmaker odds, line movement or tipster consensus entered the ranking.

## P-337 source register

### Governing / competition sources
- Google Drive `METHOD.md` — MDS-2026.09.06-v4.0.
- Google Drive `RULES_SOCCER.md` — SFA-SOCCER, goal/corner separation, participant and derivative controls.
- Google Drive `LEAGUE_RULES_SOCCER.md` — Argentina Liga Profesional 2026 format and regulation endpoint.
- Google Drive `CONTROLS.md` — G14.2/G15.1/G16/G31 and probability/ledger controls.
- Liga Profesional de Fútbol de AFA — Fecha 8 schedule and referee/VAR assignments: `https://www.ligaprofesional.ar/?p=86406`, `https://www.ligaprofesional.ar/?p=86768`.
- Barracas Central official preview — fixture, venue, current Clausura points/scorers and H2H: `https://www.barracascentral.com/2026/09/06/fecha-8-previa-vs-argentinos-2/`.

### Participant / current-state sources
- 365Scores match page / lineup article — current listed XIs, benches and unavailable players: `https://www.365scores.com/es/football/match/liga-profesional-72/argentinos-juniors-barracas-central-871-9051-72`; `https://www.365scores.com/pt-br/news/magazine/barracas-central-x-argentinos-juniors-onde-assistir-escalacoes/`.
- TyC Sports — probable Barracas XI / current match preview: `https://www.tycsports.com/liga-profesional-de-futbol/argentina-torneo-clausura-2026-barracas-central-vs-argentinos-juniors-fecha-8-id759373.html`.
- TyC Sports — Alan Lescano/Vasco transfer status: `https://www.tycsports.com/futbol-de-brasil/acuerdo-de-palabra-para-que-alan-lescano-deje-argentinos-y-sea-nuevo-refuerzo-de-vasco-da-gama-id758848.html`.

### Statistical / process sources
- Soccerzz — Clausura records, GF/GA, xG, shots and corners: `https://www.soccerzz.com/match/2026-09-07-barracas-central-argentinos-juniors/12234404`.
- FootyStats — Barracas 2026 goals/home/first-half/Under 2.5 profile: `https://footystats.org/clubs/ca-barracas-central-750`.
- FootyStats — Argentinos 2026 goals/away/first-half/Under 2.5 profile: `https://footystats.org/clubs/argentinos-juniors-725`.
- FotMob — 2026 corner-taken table and accurate-cross table: `https://www.fotmob.com/es-419/leagues/112/stats/season/28207/teams/corner_taken_team/liga-profesional-teams`; `https://www.fotmob.com/en-GB/leagues/112/stats/season/28207/teams/accurate_cross_team/team/10086/argentinos-juniorsteamsplayersteamsplayersplayersplayersplayersteamsteamsteamsplayersteams-teams`.
- Scores24 — H2H goal/corner splits: `https://scores24.live/es/soccer/m-06-09-2026-barracas-central-argentinos-juniors-h2h`.
- FotMob — current fixture/form/unavailable context: `https://www.fotmob.com/en-GB/matches/argentinos-juniors-vs-barracas-central/bhib0fc`.
- Venue-targeted weather query — Estadio Claudio Chiqui Tapia / Buenos Aires hourly grid, accessed pre-kickoff 2026-09-08 AEST.

**Settlement source predeclaration:** LPF/official competition result for goals and 90-minute result; FotMob/Opta or another defined post-final match-stat provider for corners if the exact operator definition remains unavailable. Research grade and operator action remain separate.
## 2026-09-09 full settlement + DEEP retrospective addendum

### Verified final and derivative field

**Barracas Central 0-0 Argentinos Juniors; HT 0-0.** Post-final structured statistics report **Barracas 3 corners, Argentinos 4**, shots 7-7, SOT 1-3, xG 0.54-0.34.

| Rank | Frozen row | p | Result | Brier |
|---:|---|---:|---|---:|
| 1 | Under 2.5 goals | 0.65 | **WIN** | 0.1225 |
| 2 | 1H Over 0.5 goals | 0.60 | **LOSS** | 0.3600 |
| 3 | Argentinos team corners Over 4.5 | 0.58 | **LOSS — Argentinos had 4** | 0.3364 |
| 4 | 1H Under 0.5 goals | 0.40 | **WIN** | 0.3600 |
| 5 | Over 2.5 goals | 0.35 | **LOSS** | 0.1225 |

**Potential regulation winner:** Argentinos — **INCORRECT; match drew**.  
**Card mean Brier:** **0.2603** (`EXPLORATORY`).

### Actual mechanism

Unlike P-336, this **was a genuinely low-event state**: only 14 total shots, four combined SOT and 0.88 combined xG. Argentinos' territorial/possession edge did not turn into high-quality chance volume, and their corner count stopped at four — exactly **one corner below** the 4.5 threshold.

### Three-question retrospective

1. **What did the score turn on?** Barracas successfully compressed the match, Argentinos failed to transform possession into enough high-quality chances, and the first half remained 0-0. The corner derivative also stopped just below the line.
2. **Was the driver knowable and in the card?** **Yes, substantially.** The card's Rank #1 Under explicitly modelled Barracas' low-output environment. It also named Lescano's absence and Barracas' compact/draw-friendly profile. The contradiction was internal: the same low-event mechanism was not reconciled strongly enough before giving 1H Over 0.5 a 60% Rank #2 probability.
3. **Smallest routine change:** before a 1H Over outranks its complement inside an overall low-total/draw-band card, require a current **early-chance creation mechanism** after creator absences and opponent compression, not only historical first-half occurrence rates.

### Deep review — Rank #2 and Rank #3 misses

**What went right**
- Rank #1 Under was strongly correct for the right broad mechanism.
- The draw band was correctly substantial at 31%.
- The card correctly kept the outright Argentinos winner below 50%.

**What went wrong**
- The 1H Over leaned too heavily on raw venue/phase frequencies and not enough on the same compact game-state model that drove Rank #1.
- The corner pick missed by **exactly one corner**. That is important for retrospective distance-to-line tracking but is not evidence that 58% was "almost correct".
- The winner call overstated Argentinos' ability to turn creation metrics into scoring separation.

**Process grade:** **C+** — Rank #1 mechanism was good, but the top-of-card cross-market coherence was weak.

### Learning / rule disposition

No new rule. This is a direct reinforcement of existing `RULES_SOCCER.md` control 20 (early-goal rank reconciliation) and the corner-process rules.

**Candidate-watch update:** the derivative missed by one corner. Add this event to the existing **distance-to-line retrospective observation** only. Because `P-337` is `EXPLORATORY`, it does not by itself satisfy or advance the 25-card `PRIMARY_SCORED` promotion cadence.

### New source

- Post-final structured stats: https://www.playmakerstats.com/match/2026-09-07-barracas-central-argentinos-juniors/12234404



---

# P-338 — Iva Jovic vs Coco Gauff — 2026 US Open Women Singles, Round of 16

## Controlling status

**Local external continuation ID:** `P-338`  
**Method:** `MDS-2026.09.06-v4.0 — SPORTS_ONLY / MARKET_BLIND`  
**Population:** `EXPLORATORY — NOT SCORED`  
**Competition:** 2026 US Open Women Singles, Round of 16  
**Surface:** Outdoor hard court, Arthur Ashe Stadium, USTA Billie Jean King National Tennis Center, Flushing, New York  
**Format:** best-of-three sets; standard Grand Slam/US Open singles scoring and final-set tiebreak rules under the current tennis reference  
**Scheduled start:** 2026-09-07 19:00 EDT / 2026-09-07 23:00 UTC / 2026-09-08 09:00 AEST  
**State at research freeze:** `PREGAME` at **2026-09-08 08:52:28 AEST** — official/structured tournament bracket still `not_started` before the scheduled start  
**Operator retirement/walkover terms:** `UNKNOWN_DEFINITION` — user supplied lines but no sportsbook rulebook; research directions below assume standard match completion and `NO VALUE DETERMINABLE` remains mandatory  
**User-requested retrospective:** **NOT PERFORMED**  
**Google Drive:** **READ ONLY**

## Frozen supplied candidate slate

1. Iva Jovic +4.5 aggregate games handicap
2. Coco Gauff -4.5 aggregate games handicap
3. Total games Over 21.5
4. Total games Under 21.5

Half-game complementary pairs are mutually exclusive on a completed match: `Gauff -4.5` vs `Jovic +4.5` and `Over 21.5` vs `Under 21.5`.

## Final ranked card

| Rank | Contract | `UNVALIDATED_SUBJECTIVE` probability | Evidence state |
|---:|---|---:|---|
| **1** | **Coco Gauff -4.5 games** | **54%** | `MEDIUM / LEAN` |
| **2** | **Under 21.5 total games** | **53%** | `MEDIUM / LEAN` |
| **3** | **Over 21.5 total games** | **47%** | `MEDIUM-LOW / FORCED RANK` |
| **4** | **Iva Jovic +4.5 games** | **46%** | `MEDIUM-LOW / FORCED RANK` |

**Potential match winner:** **Coco Gauff — 78% `UNVALIDATED_SUBJECTIVE`**.  
This is an analyst probability from the qualitative match tree, not a calibrated or validated tennis model probability.

## Why Rank #1 is Gauff -4.5 rather than merely Gauff to win

Gauff enters this match with the stronger current hard-court regime and substantially more straight-set control. She has won nine consecutive matches across the Cincinnati title and her first three US Open rounds, and the official US Open record shows she has won 18 consecutive sets since dropping the opening set of Cincinnati. Her US Open scorelines are 6-3 6-4 over Zeynep Sonmez, 6-4 7-6(5) over Paula Badosa, and 6-3 6-4 over Cristina Bucsa. Two of those three scores clear -4.5 games; the Badosa score is the important close-straight kill path because Gauff won while failing to clear the handicap.

Jovic has also been excellent in New York: 7-5 6-3 over Magdalena Frech, 6-4 6-4 over Francesca Jones, and 7-5 3-6 7-5 over Alexandra Eala. The Eala match lasted more than three hours and contained 17 service breaks. The workload is a modest Gauff-positive adjustment, not an automatic fatigue penalty.

The strongest contrary evidence is the only previous meeting. On Rome clay in May, Jovic led by a set and served for the match before Gauff escaped 5-7 7-5 6-2. Gauff won that match by only four aggregate games, which would have **lost Gauff -4.5 and won Jovic +4.5**, while the 32-game match easily cleared 21.5. Because the surface was clay and Gauff's present hard-court serve/control regime is materially better, the H2H is retained as a live kill path rather than allowed to own the current forecast.

## L5 / L10 / L15 / L20 form audit

Derived from the current 2026 match logs, with current tournament/tour-level continuity preserved rather than pooling junior/ITF data into WTA/Grand Slam rates.

| Player | L5 | L10 | L15 | L20 | Current regime note |
|---|---:|---:|---:|---:|---|
| **Coco Gauff** | **5-0** | **9-1** | **13-2** | **18-2** | Cincinnati champion; 3-0 at US Open, all straight sets |
| **Iva Jovic** | **4-1** | **7-3** | **10-5** | **13-7** | 3-0 at US Open; two straight-set wins then three-set win over Eala |

The streak itself receives no directional weight under `G17`; the decision-driving mechanism is the current hard-court serve/return and set-control regime plus opponent-quality continuity.

## Current serve/return evidence

### Jovic

Against Frech, official WTA match statistics recorded:
- 62% first serves in;
- 72.7% first-serve points won;
- only 33.3% second-serve points won;
- 11 break points faced;
- 53.3% return points won.

Against Jones:
- 50.9% first serves in;
- 69.0% first-serve points won;
- 64.3% second-serve points won;
- 66.7% total service points won;
- 46.2% return points won.

This is a high-variance profile: Jovic can protect serve well enough to make the handicap and Over live, but the Frech second-serve vulnerability and the 17-break Eala match create a credible Gauff separation branch because Gauff is the strongest return/defence opponent Jovic has faced in this US Open run.

### Gauff

Against Badosa, official WTA match statistics recorded:
- 50% first serves in;
- 71.4% first-serve points won;
- 57.1% second-serve points won;
- 64.3% total service points won;
- 44.2% return points won;
- 3/7 break points converted.

The serve is not flawless — five double faults against Badosa and six against Bucsa keep the Jovic cushion/Over branch alive — but the current overall service-point protection plus elite return pressure is a stronger two-way baseline than Jovic's.

## Explicit joint match tree and arithmetic

The tennis rules require a single set/game tree rather than four independent binary opinions. The working pregame branch allocation is:

| Branch | Weight | Representative score family | Gauff winner | Gauff -4.5 | Under 21.5 |
|---|---:|---|---|---|---|
| Gauff dominant straight-set control | **42%** | 6-3 6-4 / 6-3 6-3 / 6-2 6-3 | Yes | Yes | Primarily yes |
| Gauff close straight-set control | **20%** | 7-5 6-4 / 7-6 6-4 | Yes | No | Mixed, primarily Over |
| Gauff wide deciding-set win | **12%** | one lost set plus two strong winning sets | Yes | Yes | Over |
| Gauff close deciding-set win | **4%** | three competitive sets | Yes | No | Over |
| Jovic straight-set win | **7%** | 6-4 6-4 / close two-set upset | No | No | Mixed |
| Jovic deciding-set win | **15%** | three-set upset | No | No | Over |

Winner mass:
`42 + 20 + 12 + 4 = 78%` Gauff; `7 + 15 = 22%` Jovic.

Handicap mass:
`42 + 12 = 54%` Gauff -4.5; residual `46%` Jovic +4.5.

Total-games mass after splitting the close straight-set/Jovic-straight branches around the 21.5 boundary:
- Under: `42 + 6 + 5 = 53%`;
- Over: residual `47%`.

**Representative Rank-#1 scoreline:** Gauff 6-3, 6-4 = **19 games**, Gauff +5 aggregate games. This simultaneously clears **Gauff -4.5** and **Under 21.5**, so the top two directions pass the scoreline-coherence check.

### Target placement / width

The match tree does not have a fitted numerical game-margin model. The qualitative centre is approximately **Gauff +4 to +5 games**, with a broad ordinary corridor from about **Jovic +2 to Gauff +8**, driven by the close-straight and three-set branches. The supplied -4.5 therefore lies close to the centre, which is why the probability is only 54% rather than a strong favourite-handicap claim.

For total games, the primary straight-set score family places the centre around **20–21 games**, while any ordinary deciding-set state generally moves well beyond 21.5. The line is therefore also near the modal mixture boundary, producing only a 53/47 Under lean.

## Bidirectional-sign / kill-path audit

**Against Gauff -4.5:**
- Gauff can win close straight sets such as 7-5 6-4 and still fail -4.5.
- A three-set Gauff win often increases total games while compressing aggregate game margin.
- Jovic's Rome performance showed a real ability to take a set and pressure Gauff's second serve/forehand patterns, though surface continuity is incomplete.

**Against Jovic +4.5:**
- Gauff's return pressure can turn Jovic's second-serve instability into clustered breaks.
- A 6-3 6-4 or 6-3 6-3 Gauff win is entirely ordinary in Gauff's present hard-court regime.

**Against Under 21.5:**
- any three-set match is overwhelmingly an Over branch;
- a close Gauff straight-set win such as 7-5 6-4 already reaches 22 games;
- the Rome H2H reached 32 games.

**Against Over 21.5:**
- Gauff has won two of her three US Open matches 6-3 6-4 (19 games), and her current straight-set control creates a substantial sub-22 mass.

## Workload / fitness / conditions

- Jovic's previous match against Eala lasted more than three hours; Gauff's Bucsa win was a routine two-set match. This is included as a modest exposure/variance adjustment only.
- No current official withdrawal or medical-limitation notice for either player was recovered before the freeze. This is **not** treated as proof of perfect fitness.
- Match-window conditions around Arthur Ashe were forecast near **24–25°C and mostly clear**, with no material precipitation signal. No signed total/handicap adjustment was applied from weather. Arthur Ashe has a retractable roof; no decisive same-time roof-closure signal was recovered.

## Contract / settlement caveat

The user did not identify an operator or provide retirement/walkover terms. Under `TE-P3`:
- `OPERATOR_ACTION = UNKNOWN_DEFINITION`;
- `NO VALUE DETERMINABLE`;
- the directional research assumes a normally completed best-of-three match;
- a retirement or walkover can grade winner, handicap and total-games contracts differently by operator.

## Source register — P-338

### Governing Google Drive — read only
- `METHOD.md` — `MDS-2026.09.06-v4.0`.
- `RULES_GENERAL.md` — start/state, target, source and participant gates.
- `CONTROLS.md` — G0–G6, G8, G13.1, G15.1, G16, G20, G22, G31, G36, G10.1/G10.2.
- `RULES_TENNIS.md` — SFA-TENNIS, TE-P1–TE-P4, match-tree and scoreline-coherence requirements.
- `PREDICTION_LOG_COMBINED_3.md` — active Drive canonical Part-3 authority.

### Current official / structured event and result sources
- US Open official: `Coco Gauff and Iva Jovic to meet in All-American showdown at 2026 US Open` — round, players, 7 p.m. Monday Arthur Ashe start, prior Rome meeting.
- US Open official IBM SlamTracker — R4 upcoming state, player identity/H2H metadata.
- US Open official tournament schedule / current bracket — Jovic-Gauff R16, 23:00 UTC scheduled start, pregame state.
- US Open official: Gauff d. Cristina Bucsa 6-3 6-4; 18 consecutive sets noted in current tournament coverage.
- US Open official: Jovic d. Alexandra Eala 7-5 3-6 7-5; current workload/match context.
- Reuters: Jovic-Eala three-hour match and current R4 setup.
- WTA official: Jovic-Frech match statistics.
- WTA official: Jovic-Jones match statistics.
- WTA official: Badosa-Gauff match statistics.
- Current structured tennis player summaries: Gauff #4 and Jovic #14, 2026 tournament/result sequences used for the L5/L10/L15/L20 transformation.
- Venue-targeted match-window weather for Arthur Ashe / Flushing, New York.

## P-338 disposition after issue

**OPEN / PENDING SETTLEMENT — DO NOT RETROSPECT YET.**  
Move this record from the top unresolved queue into its chronological settled position only after a verified official final/settlement is available and the user requests/permits the appropriate settlement workflow.

**Next local continuation slot after P-338:** `P-339`.
## 2026-09-09 full settlement + retrospective addendum

### Official result

**Coco Gauff def. Iva Jovic 6-1, 6-4.** US Open reporting notes that Gauff converted **5 of 11 break-point opportunities**.

| Rank | Frozen row | p | Result | Brier |
|---:|---|---:|---|---:|
| 1 | Gauff -4.5 games | 0.54 | **WIN** | 0.2116 |
| 2 | Under 21.5 games | 0.53 | **WIN** | 0.2209 |
| 3 | Over 21.5 games | 0.47 | **LOSS** | 0.2209 |
| 4 | Jovic +4.5 games | 0.46 | **LOSS** | 0.2116 |

**Potential winner:** Gauff — **CORRECT**.  
**Card mean Brier:** **0.2163** (`EXPLORATORY`).

### Three-question retrospective

1. **What did the match turn on?** Gauff's return pressure created repeated break opportunities and she converted enough of them to make the dominant straight-set branch real. Jovic never forced the deciding-set/close-straight-set mass needed for the cushion or Over.
2. **Was the driver knowable and in the card?** **Yes.** The original tree gave its largest weight (42%) to Gauff dominant straight-set control and explicitly identified Jovic's second-serve/break exposure against Gauff's return pressure. The actual 6-1, 6-4 score was even more separated than the representative 6-3, 6-4 Rank #1 scoreline.
3. **Smallest routine change:** none beyond continuing to quantify break-opportunity/return-pressure evidence from the current surface and preserving the one-tree scoreline coherence check.

### What went right

- Winner, handicap and Under were generated coherently from the same straight-set branch.
- The old Rome H2H was correctly retained as a kill path rather than allowed to dominate the hard-court forecast.
- The representative scoreline test was useful and directionally accurate.

**Process grade:** **A-** — correct mechanism and coherent cross-market geometry; probabilities remained close to 50% and are not evidence of calibration.

### Learning / rule disposition

No new tennis control. This is positive evidence that the existing `RULES_TENNIS.md` scoreline-coherence and shared match-tree procedure was applied correctly in this instance.

### New official sources

- https://www.usopen.org/en_US/news/articles/2026-09-07/iva_jovic_vs_coco_gauff_at_the_2026_us_open.html
- https://www.usopen.org/amp/en_US/news/articles/2026-09-07/coco_gauff_beats_iva_jovic_in_all-american_2026_us_open_clash.html



---

# 8. 2026-09-08 QUEUE SETTLEMENT UPDATE — NO RETROSPECTIVES

The user explicitly instructed **“Don't do a retrospective yet.”** This update therefore performs settlement/queue administration only. No three-question retrospective, deep Rank-#1 review, or new learning/control is created here.

## P-335 — Washington Nationals @ San Diego Padres — SETTLED

**Verified final:** San Diego Padres 3, Washington Nationals 2. MLB official postgame record.

| Frozen row | Issued probability | Result | Brier |
|---|---:|---|---:|
| Nationals +1.5 | 0.59 | **WIN** | 0.1681 |
| Over 8.0 runs | 0.52 win probability | **LOSS** | 0.2704 |
| Padres -1.5 | 0.41 | **LOSS** | 0.1681 |
| Under 8.0 runs | 0.36 win probability | **WIN** | 0.4096 |

Potential winner: **Padres — WIN**.  
P-335 card mean Brier across the four ranked binary outcomes: **0.2541**. This is descriptive only, not calibration or edge evidence.

Settlement source: MLB official Padres/Nationals September 7, 2026 final and postgame slate.

## P-338 — Iva Jovic vs Coco Gauff — SETTLED

**Verified final:** Coco Gauff def. Iva Jovic **6-1, 6-4**.

| Frozen row | Issued probability | Result |
|---|---:|---|
| Gauff -4.5 games | 0.54 | **WIN** |
| Under 21.5 games | 0.53 | **WIN** |
| Over 21.5 games | 0.47 | **LOSS** |
| Jovic +4.5 games | 0.46 | **LOSS** |

Potential winner: **Coco Gauff — WIN**.  
Tennis remains `EXPLORATORY — NOT SCORED` in the current Drive population framework, so this settlement is not added to the primary scored population record.

Settlement source: current US Open Women Singles 2026 official/structured bracket state.

## P-336 / P-337 queue state

- **P-336 Carabobo vs Estudiantes:** official Carabobo final **1-0** is verified. Score-derived rows can be determined, but the separately ranked **Over 7.5 match corners** derivative has not yet been settled from its frozen/acceptable field, so the event remains in the incomplete queue.
- **P-337 Barracas vs Argentinos Juniors:** official Argentinos report verifies **0-0**. Score-derived rows can be determined, but **Argentinos team corners Over 4.5** remains without a completed derivative settlement in this pass, so the event remains in the incomplete queue.

No retrospective was performed on either event.

---

# P-339 — Doosan Bears @ Hanwha Eagles — KBO — 2026-09-08

## Controlling status

**Local external continuation ID:** `P-339`  
**Google Drive:** **READ ONLY — not edited**  
**Method:** `MDS-2026.09.06-v4.0 — SPORTS_ONLY / MARKET_BLIND`  
**Sport algorithm:** `SFA-BASEBALL`  
**Population:** `EXPLORATORY — NOT SCORED`  
**GAME-STATE:** **PREGAME**  
**Scheduled start:** 2026-09-08 **18:30 KST** = **19:30 AEST**  
**Final volatile freeze:** **2026-09-08 19:19:50 AEST / 18:19:50 KST**  
**Venue:** Hanwha Life Eagles Park, Daejeon  
**Home last-bat:** Hanwha Eagles  
**User-requested retrospective:** **NOT PERFORMED**

At the final volatile refresh, the official KBO English scoreboard still showed Doosan–Hanwha scheduled for **18:30 in Daejeon** with blank inning/run fields. Because the cutoff remained before scheduled first pitch, this card is valid `PREGAME` under the current start-crossing rule.

## Frozen supplied contracts

1. Hanwha Eagles **-1.5 runs**
2. Doosan Bears **+1.5 runs**
3. Combined total **Over 9.5 runs**
4. Combined total **Under 9.5 runs**
5. Potential full-game winner under standard KBO competition rules; a tie after the regular-season extra-innings cap remains possible.

### Operator/contract caveat

The user supplied the thresholds but not an operator ruleset. Therefore listed-pitcher action, suspension/termination treatment, and operator-specific tie/action rules remain **`UNKNOWN_DEFINITION`**. `NO VALUE DETERMINABLE`. Research directions assume a normally completed KBO regular-season game under standard competition rules.

KBO rules carried from the current Drive reference: nine scheduled innings; universal DH; regular-season game may finish tied after **11 innings**; no automatic extra-inning runner; no mercy rule; Hanwha bats last.

## Issued ranking

| Rank | Pick | `UNVALIDATED_SUBJECTIVE` probability | Evidence state |
|---:|---|---:|---|
| **1** | **Doosan Bears +1.5** | **60%** | **MEDIUM-LOW / FORCED RANK** |
| **2** | **Over 9.5 total runs** | **56%** | **MEDIUM-LOW / FORCED RANK** |
| **3** | **Under 9.5 total runs** | **44%** | **MEDIUM-LOW** |
| **4** | **Hanwha Eagles -1.5** | **40%** | **MEDIUM-LOW** |

### Potential winner

**Hanwha Eagles — 53% `UNVALIDATED_SUBJECTIVE`**  
Doosan Bears — 44%  
Tie after the KBO regular-season cap — 3%

The winner and run line are intentionally separated: Hanwha is the slightly more likely outright winner, but a substantial portion of that winning mass is by exactly one run, while Doosan also owns a large outright-win branch. That makes **Doosan +1.5** more likely than Hanwha -1.5.

## Identity / participant freeze

### Starting pitchers — current field-owner-supported identity

**Doosan — Choi Seung-yong, LHP**
- 2026: **3-11, 5.74 ERA**, 100 1/3 IP.
- 120 H, 10 HR, 36 BB, 72 SO.
- **1.55 WHIP**, opponent AVG **.292**, only 3 QS.
- Last ten starts: **5.88 ERA** across 49 IP.
- Most recent start, Sep 2 vs LG: 4 IP, 6 H, 1 BB, 2 K, 4 ER.
- KBO roster/entry record shows him active through Sep 8.

**Hanwha — Ryu Hyun-jin, LHP**
- 2026: **8-5, 3.91 ERA**, 119 2/3 IP through 22 starts.
- First half: **8-2, 2.67 ERA** in 87 2/3 IP.
- Current second-half regime: **0-3, 7.31 ERA** through seven starts in the official KBO preview.
- 2026 vs Doosan: **3 starts, 16 IP, 20 H, 3 BB, 8 K, 12 R/11 ER, 6.19 ERA, .294 opponent AVG**.

Ryu's reputation/full-season line is therefore retained as a prior, but it does not erase the current second-half and opponent-specific deterioration.

### Hanwha official starting lineup

The current KBO media page published this order against Choi:
1. Sim Woo-jun — SS
2. Yonathan Perlaza — RF
3. Moon Hyun-bin — LF
4. Kang Baek-ho — DH
5. Roh Si-hwan — 3B
6. Kim Tae-yean — 1B
7. Heo In-seo — C
8. Choi In-ho — CF
9. Lee Do-yun — 2B

The heart of this order has meaningful current power: the official KBO team table has Hanwha at **152 HR** through 120 games.

### Doosan current lineup state

The current MyKBO game page lists:
1. Park Chan-ho SS
2. Park Ji-hoon 3B
3. Park Jun-soon 2B
4. Yang Eui-ji DH
5. Kim Min-suk LF
6. Kang Seung-ho 1B
7. Jung Soo-bin CF
8. Kim Ki-yeon C
9. Kim Dae-han RF

This Doosan order was **secondary-only at the freeze**, not independently recovered from a current field-owner lineup release. Therefore participant certainty is not upgraded to `CONFIRMED_OFFICIAL`; this directly caps the evidence grade on participant-sensitive team rows.

### Availability / bench / management

- Hanwha's current official starting order omits Chae Eun-seong, but no current authoritative cause was established in this pass. **Do not label him injured from omission alone.**
- Yang Eui-ji and Kim Min-suk are present in the current Doosan secondary lineup; older injury/pain reports are not treated as current restrictions without a same-day source.
- Current injury/availability evidence is **incomplete**, not “no injuries”.
- MyKBO exposes full current benches for both clubs; exact score-state bullpen availability was only partially recovered.
- Both clubs were off on Sep 7, which improves broad reliever availability, but workload is treated as availability evidence only, not as a performance boost.
- Managers: Hanwha **Kim Kyung-moon**; Doosan **Kim Won-hyung**. No same-day manager change was identified.

Because the Doosan lineup is secondary-only and the exact bullpen ladder is partial, both margin and full-game total rows remain **MEDIUM-LOW / FORCED RANK** where applicable.

## Season-level team process

Official KBO batting table at the freeze:

| Team | G | AVG | Runs | R/G | HR | OBP | SLG | OPS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Hanwha | 120 | .276 | 702 | **5.85** | **152** | .354 | .437 | **.791** |
| Doosan | 123 | .267 | 575 | **4.67** | 95 | .340 | .392 | .732 |

The latest accessible official KBO team-pitching table was a few games behind the batting table but showed a large structural prevention gap:
- **Doosan team ERA 3.64** (1st at that snapshot);
- **Hanwha team ERA 5.13** (8th).

This is why Hanwha's stronger offence does not translate into a large favourite margin. Today's starters partially reverse the season staff picture: Choi is substantially weaker than Doosan's overall staff, while Ryu's current second-half regime is substantially weaker than his first-half/full-season reputation.

## L5 / L10 / L15 / L20 audit

Secondary result feed, used descriptively and reconciled against the named starter/lineup mechanisms:

### Doosan

| Window | RF/G | RA/G | Combined/G | Games over 9.5 |
|---|---:|---:|---:|---:|
| L5 | 3.80 | 4.40 | **8.20** | 1/5 |
| L10 | 5.00 | 3.80 | **8.80** | 2/10 |
| L15 | 4.80 | 3.87 | **8.67** | 4/15 |
| L20 | 4.95 | 4.00 | **8.95** | 7/20 |

### Hanwha

| Window | RF/G | RA/G | Combined/G | Games over 9.5 |
|---|---:|---:|---:|---:|
| L5 | 10.00 | 6.80 | **16.80** | 5/5 |
| L10 | 6.90 | 8.00 | **14.90** | 8/10 |
| L15 | 6.47 | 8.40 | **14.87** | 11/15 |
| L20 | 6.05 | 8.05 | **14.10** | 14/20 |

Trend audit: these raw streaks receive **zero automatic directional weight**. Hanwha's recent high-total sequence is only directionally relevant to the extent it is supported by current mechanisms that remain active today: a power-heavy lineup, Choi's weak run-prevention profile, and Ryu's second-half / Doosan-specific vulnerability. Doosan's recent low-total sequence is likewise not assumed to continue after a 16-9 game and a different starter matchup.

Season series entering today: approximately **7-7-1**, which is context rather than a directional cause.

## Joint run object — explicit arithmetic

### Doosan run centre

Season offence vs opposing season staff baseline:

`(Doosan 4.67 R/G + Hanwha 5.13 team ERA) / 2 = 4.90`

Signed adjustments:
- Ryu full-season quality versus Hanwha staff baseline: **-0.25**
- Ryu second-half 7.31 ERA regime: **+0.25**
- Ryu's 2026 Doosan split (6.19 ERA / .294 AVG): **+0.15**
- Hanwha relief/late-inning uncertainty relative to Doosan's offensive baseline: **+0.05**

**Doosan centre ≈ 5.10 runs.**

### Hanwha run centre

Season offence vs opposing season staff baseline:

`(Hanwha 5.85 R/G + Doosan 3.64 team ERA) / 2 = 4.745`

Signed adjustments:
- Choi's 5.74 ERA / 1.55 WHIP / .292 opponent AVG versus Doosan staff baseline: **+0.45**
- Hanwha's current power concentration and 152-HR season shape against a left-handed starter: **+0.15**
- Doosan's materially stronger overall relief/staff prevention: **-0.15**
- Sep 7 off-day / broader leverage availability: **-0.05**
- weather: **0.00 signed direction**

**Hanwha centre ≈ 5.15 runs.**

### Combined centre and width

`5.10 + 5.15 = 10.25 runs`

Working total centre: **10.25**  
Working total width: approximately **±4.1 runs**, reflecting KBO scoring dispersion, starter exit uncertainty, sequencing/HR clusters and partial bullpen-state knowledge.

Working margin centre: **Hanwha +0.05 runs** before home-last-bat/tie-state branching; after home batting entitlement and score-state treatment, the full-game winner branch tilts modestly Hanwha while the separation distribution remains broad.

## Separation budget — exact run-line logic

Frozen branch mass:
- **Doosan outright win:** 44%
- **Tie after KBO cap:** 3%
- **Hanwha by exactly 1:** 13%
- **Hanwha by 2+:** 40%

Therefore:

`P(Doosan +1.5) = 44% + 3% + 13% = 60%`

`P(Hanwha -1.5) = 40%`

Potential winner:

`P(Hanwha win) = 13% + 40% = 53%`

This explicitly preserves the KBO tie branch rather than forcing a binary MLB-style winner assumption.

## Total budget — 9.5 runs

The joint centre of **10.25** lies only modestly above the 9.5 threshold and the game has wide two-sided tails. The frozen distribution allocates:
- **10+ runs:** 56%
- **0–9 runs:** 44%

So:

`P(Over 9.5) = 56%`  
`P(Under 9.5) = 44%`

The Over is not promoted simply because Hanwha's last five games were high scoring. It is supported by the current starter/lineup chain. The primary Under kill path is that Ryu recovers toward his season prior while Doosan's strong bullpen suppresses Hanwha once Choi exits; the primary Over kill path is traffic against both starters plus a clustered HR/relief-transition inning.

## Representative coherent scoreline

**Hanwha 6 — Doosan 5**

This representative central state simultaneously produces:
- **Doosan +1.5 — WIN**
- **Over 9.5 — WIN**
- **Hanwha potential winner — WIN**
- Hanwha -1.5 — LOSS

This is why the most likely winner can be Hanwha while the strongest supplied contract is still Doosan +1.5.

## Weather / termination branch

Venue-targeted weather near first pitch was clear, roughly mid-20s °C, with **0% precipitation** through the main game window. No reliable field-relative wind mechanism strong enough for a signed total adjustment was established. Therefore weather receives **0.00 directional adjustment** and the weather-termination branch is negligible in the central object, subject to ordinary forecast uncertainty.

## Bidirectional / kill-path audit

### Doosan +1.5 kill paths
- Hanwha's top/middle order can punish Choi early and force a middle-relief entry before Doosan's best leverage arms are relevant.
- Perlaza / Moon / Kang / Roh / Heo provide multiple HR and extra-base-hit paths; clustered damage can create a 2+ run gap quickly.
- A high-total environment increases margin variance rather than automatically protecting the underdog cushion.

### Hanwha -1.5 kill paths
- Ryu's second-half deterioration and 6.19 ERA vs Doosan can put Hanwha behind or keep the score within one.
- Doosan's overall pitching staff has been materially stronger than Hanwha's, giving the Bears a better late-game prevention branch once Choi exits.
- KBO ties remain possible; any tie also defeats Hanwha -1.5.

### Over 9.5 kill paths
- Ryu can revert toward his full-season/first-half quality.
- Doosan's bullpen can sharply lower Hanwha scoring after the starter transition.
- Doosan's own recent scoring floor has been volatile, with several 0–2 run outputs in the recent window.

### Under 9.5 kill paths
- Choi's traffic/contact profile against Hanwha's 5.85-R/G, 152-HR offence creates a genuine multi-run early-inning tail.
- Ryu's current second-half state and poor 2026 Doosan matchup create a second independent scoring channel.
- Relief transitions and inherited runners keep an upper tail alive even if neither starter is immediately shelled.

## Final source register — P-339

### Governing Google Drive — read only
- `METHOD.md` — `MDS-2026.09.06-v4.0`.
- `RULES_GENERAL.md` §16 / start-state and target gates.
- `CONTROLS.md` — current v4.0 gate quick reference.
- `RULES_BASEBALL.md` — `SFA-BASEBALL`, KBO §9.4 and KBO-specific settlement/source rules.
- `PREDICTION_LOG_COMBINED_3.md` — active Drive Part-3 authority.

### KBO / current baseball sources
- KBO official English scoreboard, 2026-09-08 — Doosan @ Hanwha, Daejeon, 18:30; final pregame state check.
- KBO official preview, 2026-09-08 — Ryu Hyun-jin season / first-half / second-half state and matchup preview.
- KBO official current Hanwha lineup report, 2026-09-08.
- KBO official Choi Seung-yong player page — 2026 season and recent-ten-start record.
- KBO official Ryu Hyun-jin opponent-split page — 2026 Doosan split.
- KBO official team batting `Basic1` / `Basic2` — runs, HR, AVG/OBP/SLG/OPS.
- KBO official team pitching table — latest accessible team ERA snapshot.
- MyKBO current game page — current secondary Doosan lineup/bench, Hanwha corroboration, starters, current team comparison, venue/weather context. Explicitly treated as unofficial secondary evidence.
- Live-Result current last-20 results feed — L5/L10/L15/L20 transformations only; descriptive secondary evidence.
- Venue-targeted hourly weather for Hanwha Life Eagles Park / Daejeon — clear conditions and negligible rain risk.

### Exclusions
- No bookmaker odds, implied probabilities, market movement, tipster predictions, affiliate previews or synthetic simulations were used as predictive evidence.

## P-339 disposition after issue

**OPEN / PENDING SETTLEMENT — DO NOT RETROSPECT YET.**  
Move this event from the top unresolved queue only after verified final settlement under the frozen KBO contract interpretation. No retrospective should be performed unless/until the user asks.

**Next local continuation slot after P-339:** `P-340`.
## 2026-09-09 full settlement + DEEP Rank-#1 retrospective addendum

### Official KBO result

**Hanwha Eagles 6-1 Doosan Bears.** KBO's official current report attributes the win to **Ryu Hyun-jin's strong outing** plus home runs from **Heo In-seo and Kang Baek-ho**.

| Rank | Frozen row | p | Result | Brier |
|---:|---|---:|---|---:|
| 1 | Doosan Bears +1.5 | 0.60 | **LOSS** | 0.3600 |
| 2 | Over 9.5 runs | 0.56 | **LOSS** | 0.3136 |
| 3 | Under 9.5 runs | 0.44 | **WIN** | 0.3136 |
| 4 | Hanwha Eagles -1.5 | 0.40 | **WIN** | 0.3600 |

**Potential winner:** Hanwha — **CORRECT**.  
**Card mean Brier:** **0.3368** (`EXPLORATORY`).

### What actually happened

The game realized the exact branch that the card acknowledged but underweighted: **Ryu reverted sharply toward his established skill prior**, holding Doosan to a very low scoring state, while Hanwha's power translated Choi's traffic/contact vulnerability into actual separation. The final total of seven was well below the 10.25 centre, and the five-run margin was far outside the card's near-zero central separation.

### Three-question retrospective

1. **What did the score turn on?** Ryu's run prevention dominated Doosan, while Hanwha converted power against Choi and separated 6-1.
2. **Was the driver knowable and in the card?** **Yes.** The card explicitly named Ryu's full-season/first-half quality as the primary Over kill path and Hanwha's power as a Doosan +1.5 kill path. The error was weighting: the short second-half deterioration and small opponent-specific split received too much directional force relative to the veteran skill/reversion branch.
3. **Smallest routine change:** where a veteran starter's established skill conflicts with a short bad current run or small opponent split, quantify a **reversion-to-skill branch from current pitch/command/velocity indicators** before assigning positive runs to the opponent.

### Deep review

**What went right**
- The potential winner, Hanwha, was correct.
- Choi's vulnerability and Hanwha's power concentration were correctly identified.
- The card did not blindly force a binary winner and preserved the KBO tie branch.

**What went wrong**
- Rank #1 failed badly; the five-run separation was the opposite of the central +0.05 margin.
- Rank #2 Over failed; the 10.25 total centre was three-plus runs above the actual game.
- The analysis knew the Ryu reversion kill path but did not make it competitive enough with the negative recent-regime adjustment.
- Ryu's **0-3 / 7.31 second-half** line and 2026 Doosan split were treated too much like persistent mechanisms rather than noisy outcome summaries unless supported by current pitch-quality evidence.

**Process grade:** **C** — correct winner and correct identification of both key branches, but poor probability mass allocation across them.

### Learning / rule disposition

**No new rule.** This is a textbook application of existing `RULES_BASEBALL.md` control 13: season prior versus current starter regime. The retrospective should be recorded as an **application failure / branch-weighting warning**, not promoted into a fresh rule.

**Where it belongs after reconciliation:** `PREDICTION_LOG_COMBINED_3.md` retrospective; no `CONTROLS.md` change unless the same failure recurs prospectively.

### New field-owner source

- KBO official current report: https://www.koreabaseball.com/MediaNews/News/BreakingNews/View.aspx?bdSe=62285



---

# P-340 — Soccer — K League 1

## Incheon United vs Bucheon FC 1995

**Scheduled start:** 2026-09-08 19:30 KST / 20:30 AEST  
**Venue:** Incheon Football Stadium (Sungui Arena Park), Incheon  
**Issue state:** `PREGAME`  
**Forecast freeze:** 2026-09-08 20:25:04 AEST / 2026-09-08 19:25:04 KST  
**Method:** `MDS-2026.09.06-v4.0 — SPORTS_ONLY / MARKET_BLIND`  
**Population:** `EXPLORATORY — NOT SCORED`  
**Operator terms:** `UNKNOWN_DEFINITION` for exact corner-provider/stat-correction treatment and abandonment/void terms; standard 90-minute + stoppage-time goal endpoint assumed for the directional analysis.  
**Retrospective:** NOT PERFORMED — user explicitly requested no retrospective yet.

## Candidate contracts supplied / selected

1. First-half goals Over 0.5
2. First-half goals Under 0.5
3. Full-time total goals Over 2.5
4. Full-time total goals Under 2.5
5. Analyst-selected derivative: total match corners Under 10.5

## Final ranked card

| Rank | Pick | `UNVALIDATED_SUBJECTIVE` probability | Evidence state |
|---:|---|---:|---|
| **1** | **1H Over 0.5 goals** | **61%** | **MEDIUM / LEAN** |
| **2** | **Under 10.5 total match corners** | **59%** | **LOW / FORCED RANK** |
| **3** | **Under 2.5 total goals** | **55%** | **MEDIUM-LOW / LEAN** |
| **4** | **Over 2.5 total goals** | **45%** | **MEDIUM-LOW** |
| **5** | **1H Under 0.5 goals** | **39%** | **MEDIUM-LOW** |

### Potential regulation winner

- **Incheon United — 45%**
- Draw — 31%
- Bucheon FC 1995 — 24%

Winner endpoint is **90-minute regulation result**. This is not an advance/eventual-winner market.

## Competition / identity freeze

The event is a 2026 K League 1 Round 28 fixture. Field-owner and club schedule records place it at Incheon Football Stadium on 2026-09-08 at 19:30 KST. K League 1 is a league match, so a draw is a live 90-minute outcome; no extra time or penalties apply. The 2026 league format is 12 clubs, 33 regular-round matches followed by the top-six/bottom-six split and five final-round matches, for 38 matches per club.

The active Drive soccer reference did not surface a readily searchable dedicated K League 1 subsection in the fetched text, so the card records the current 2026 league format/rules check from current field-owner evidence rather than silently borrowing another league's structure. Drive remains read-only, so this onboarding verification is preserved here rather than written back to Drive.

## Current participant state

### Incheon United — current matchday reported XI, `SECONDARY_ONLY`

Sports Chosun's on-site lineup report lists Yoon Jong-hwan using a **4-4-2**:
- GK: **Kim Dong-heon**
- DEF: **Kim Myung-sun, Kim Yeon-su, Juan Ibiza, Lee Ju-yong**
- MID: **Lee Dong-ryul, Seo Jae-min, Lee Myung-joo, Leandro**
- FWD: **Stefan Mugoša, Morgan Ferrier**

This is a reputable same-day matchday lineup report, but a field-owner official XI endpoint was not recovered before freeze. Therefore it is **not labelled CONFIRMED_OFFICIAL** under the Drive participant gate.

### Bucheon FC 1995 — current matchday reported XI, `SECONDARY_ONLY`

Lee Young-min is reported in a **3-4-3**:
- GK: **Kim Hyeong-geun**
- DEF: **Hong Seong-uk, Patrick, Jeong Ho-jin**
- MID: **Ahn Tae-hyun, Sung Ye-geon, Kaz, Kim Seung-bin**
- FWD: **Galego, Gustavo, Bassani**

Again, this is current matchday reporting rather than a recovered official K League lineup endpoint.

### Availability / absences

- **Kim Gun-hee (Incheon)** is unavailable after the early red card against FC Seoul on September 5; that dismissal is treated as a current central-defensive availability loss rather than as an ordinary recent-match performance signal.
- No complete authoritative same-day injury bulletin for both squads was recovered before cutoff. Therefore this card does **not** claim that every unlisted player is healthy.
- The exact full current benches were **NOT_RETRIEVED**. Under `G14.2`, that missingness blocks a full-match total/margin row from Rank #1. It is one reason the full-time Under is only Rank #3 and MEDIUM-LOW.

## Current season/home-away process

### Incheon home

- xG for: **1.47/game**
- xG against: **1.30/game**
- goals scored: **1.08/game**
- goals conceded: **1.08/game**
- observed combined goals: **2.15/game**
- FT Over 2.5: **38%** / Under 2.5: **62%**
- first-half combined goals: **0.92/game**
- first-half Over 0.5: **69%**
- shots: **11.38/game**

### Bucheon away

- xG for: **1.18/game**
- xG against: **1.62/game**
- goals scored: **1.00/game**
- goals conceded: **1.00/game**
- observed combined goals: **2.00/game**
- FT Over 2.5: **33%** / Under 2.5: **67%**
- first-half combined goals: **0.83/game**
- first-half Over 0.5: **58%**
- first-half scored: **0.33/game**; conceded: **0.50/game**
- shots: **9.33/game**

The major structural split is therefore: low full-game observed scoring, but a materially higher-than-50% first-half goal frequency for both venue-specific samples.

## L5 / L10 / L15 / L20 league-only trend audit

### Incheon United

| Window | GF/game | GA/game | Combined goals/game | O2.5 |
|---|---:|---:|---:|---:|
| L5 | 0.80 | 1.00 | **1.80** | 1/5 |
| L10 | 1.10 | 1.10 | **2.20** | 3/10 |
| L15 | 1.20 | 0.87 | **2.07** | 5/15 |
| L20 | 1.20 | 0.95 | **2.15** | 8/20 |

### Bucheon FC 1995

| Window | GF/game | GA/game | Combined goals/game | O2.5 |
|---|---:|---:|---:|---:|
| L5 | 1.40 | 1.80 | **3.20** | 3/5 |
| L10 | 1.40 | 1.60 | **3.00** | 6/10 |
| L15 | 1.27 | 1.33 | **2.60** | 7/15 |
| L20 | 1.10 | 1.40 | **2.50** | 9/20 |

### Trend interpretation

Incheon's environment is stable around roughly 1.8–2.2 total goals across all windows. Bucheon's recent totals are much higher, but the short windows contain tail results such as the **0-5 loss to Daejeon** and **3-0 win over Pohang**. Per `G17/G17.1`, those outcomes receive no automatic continuation weight. The current mechanism supporting an upper tail is instead the attacking personnel actually selected plus Incheon's defensive absence.

Incheon's September 5 loss at Seoul is also not treated as an ordinary baseline game because the third-minute dismissal changed the match state almost immediately.

## Current-season H2H continuity

Two 2026 meetings are directly relevant:
- **2026-04-18: Bucheon 2-2 Incheon**, HT 0-2. First-half goal condition cleared; 7 total corners reported.
- **2026-07-26: Incheon 1-1 Bucheon**, HT 0-1. First-half goal condition cleared; the match had a much higher corner tail than the April meeting.

Both current-season H2Hs contained a first-half goal and ended level. The sample is only two matches, so it supports continuity but does not control the probability.

## Goal-process arithmetic

### Full-match total prior

Observed home/away environment:

`(Incheon home 2.15 + Bucheon away 2.00) / 2 = 2.075`

Cross xG process:

- Incheon attack vs Bucheon away defence: `(1.47 + 1.62) / 2 = 1.545`
- Bucheon attack vs Incheon home defence: `(1.18 + 1.30) / 2 = 1.240`
- Cross xG total: `1.545 + 1.240 = 2.785`

Blended prior:

`0.60 × 2.075 + 0.40 × 2.785 = 2.359`

Signed current-state adjustments:
- **+0.08** Incheon's Mugoša + Ferrier striker pairing with Leandro/Lee Dong-ryul width
- **+0.05** Bucheon's Galego + Gustavo + Bassani front three
- **+0.07** Incheon central-defensive suspension/rotation tail
- **-0.15** short turnaround + Bucheon's low away shot volume and observed away scoring suppression
- **0.00** weather/surface: no verified adverse mechanism

Resulting working total centre:

`2.359 + 0.08 + 0.05 + 0.07 - 0.15 = 2.409`

**Working goal centre: ≈ 2.40 goals** with a broad discrete width of about **±1.8 goals**.

That places 2.5 only slightly above the centre, hence:
- `P(Under 2.5) = 55%`
- `P(Over 2.5) = 45%`

This is deliberately moderate rather than a strong Under.

## First-half goal budget

Venue-specific first-half mean:

`(0.92 + 0.83) / 2 = 0.875 first-half goals`

A simple one-rate translation gives:

`1 - exp(-0.875) ≈ 58.3%` for at least one first-half goal.

Observed first-half O0.5 midpoint:

`(69% + 58%) / 2 = 63.5%`

Shrinking the empirical rate toward the phase-rate prior and accounting for the unresolved official-XI/bench detail gives a working probability of **61%** rather than taking the raw 63.5% at face value.

Therefore:
- **1H Over 0.5 = 61%**
- **1H Under 0.5 = 39%**

The strongest representative early-goal branch is a single goal before half-time followed by a lower-tempo second half; that is fully compatible with FT Under 2.5.

## Corner process — separate from goals

The corner process is not inferred from xG or team strength.

Available current rates give an approximate team-share construction:
- Incheon home corners-for ≈ **4.62**; Bucheon away corners-conceded ≈ **4.67** → Incheon corner centre ≈ **4.65**
- Bucheon away corners-for ≈ **4.42**; Incheon home corners-conceded ≈ **3.46** → Bucheon corner centre ≈ **3.94**

Combined centre:

`4.65 + 3.94 ≈ 8.59 corners`

The present tactical shapes widen the upper tail: Incheon use a 4-4-2 with two wide midfielders and two forwards; Bucheon use a 3-4-3 with wingback width. Current-season H2H also spans a low-corner April match and a much higher-corner July match.

However, the exact operator corner definition/provider, current blocked-cross/end-line/clearance chain, and complete benches were not recovered. Therefore the row is capped under the soccer derivative gate:

**Under 10.5 total corners — 59% — `FORCED RANK / LOW`**.

It is Rank #2 numerically, but its lower evidence grade is explicit and should not be confused with a fully supported derivative model.

## Potential-winner separation budget

Incheon retain the stronger overall season position and the better home attacking xG against Bucheon's weaker away xGA, but the side is not dominant:
- Incheon: 34 points from 26 before this fixture, 32 GF / 29 GA.
- Bucheon: 31 points from 27, 28 GF / 34 GA.
- Incheon home actual record is only 4-3-6.
- Bucheon away are 4-4-4 and have conceded only 1.00/game away in the observed sample.
- Incheon's defensive suspension expands Bucheon's counter/scoring branch.

Working 1X2 distribution:
- **Incheon 45%**
- **Draw 31%**
- **Bucheon 24%**

Potential winner: **Incheon United**, but the draw band is too large to treat the winner call as stronger than the Rank #1 phase-total contract.

## Representative coherent score states

Primary central family:
- **Incheon 1-0 Bucheon** — 1H Over can win; FT Under wins; Incheon wins.
- **Incheon 1-1 Bucheon** — 1H Over can win; FT Under wins; draw.
- **Incheon 2-0 Bucheon** — 1H Over can win; FT Under wins; Incheon wins.

Upper-tail kill state:
- **Incheon 2-1 Bucheon** — FT Over wins and the Under loses; this remains a meaningful branch because of the attacking selections and Incheon defensive absence.

## Weather / surface gate

Venue-targeted hourly conditions for Incheon Football Stadium were approximately **26°C, mostly clear, ~2% precipitation** through the main match window. No current pitch degradation or strong wind mechanism was verified. Therefore:
- goal weather adjustment: **0.00**
- corner weather adjustment: **0.00**

## Bidirectional / kill-path audit

### 1H Over 0.5 kill paths
- Incheon's observed home 0-0 HT rate remains meaningful.
- Bucheon away score only 0.33 first-half goals/game and fail to score in many opening halves.
- A cautious relegation/split-position game state can suppress early risk despite both attacking XIs.

### Under 2.5 kill paths
- Incheon field both Mugoša and Ferrier with Leandro supplying width.
- Bucheon deploy Galego/Gustavo/Bassani and face an Incheon defence missing Kim Gun-hee.
- An early goal can trigger a chasing-state transition and push the same match into 2-1/2-2 territory.

### Corner Under 10.5 kill paths
- Both formations have plausible wide/crossing routes.
- A trailing side may drive repeated end-line entries and blocks after 60'.
- The July H2H showed a high-corner branch; the underlying distribution is clearly wider than a simple mean of 8.6.

## Final source register — P-340

### Governing Google Drive — READ ONLY
- `METHOD.md` — MDS-2026.09.06-v4.0.
- `RULES_GENERAL.md` §16 — state/participant/environment/joint-object gates.
- `RULES_SOCCER.md` — SFA-SOCCER and separate corner-process requirements.
- `LEAGUE_RULES_SOCCER.md` — general soccer competition identity/settlement reference.
- `CONTROLS.md` — v4.0 quick-reference controls.
- `PREDICTION_LOG_COMBINED_3.md` — active canonical Drive authority.

### Current event / participants / state
- Incheon United official club schedule / ticket pages — fixture, 2026-09-08 19:30 KST, Incheon Football Stadium.
- K League current 2026 competition format releases — 12 teams, 33-match regular round + five-game split/final round.
- Sports Chosun, 2026-09-08 on-site lineup report — current reported XIs and formations for both teams.
- Reuters current K League reporting — Kim Gun-hee red-card event on September 5.

### Current statistical evidence
- FootyStats Incheon United 2026 K League 1 — home/overall goals, first-half, xG/xGA, shot data.
- FootyStats Bucheon FC 1995 2026 K League 1 — away/overall goals, first-half, xG/xGA, shot data.
- FotMob current match page — current recent-result corroboration and top-scorer context.
- Current result histories transformed into L5/L10/L15/L20 league-only windows.
- TotalCorner / current corner-stat providers — H2H and team corner rates used only as secondary derivative evidence.
- Venue-targeted hourly weather for Incheon Football Stadium.

### Explicit exclusions
- Bookmaker odds, implied probabilities, line movement, tipster/editorial prediction models, synthetic forecasts and market consensus were excluded from predictive evidence under `SPORTS_ONLY / MARKET_BLIND`.

## P-340 disposition after issue

**OPEN / PENDING SETTLEMENT — DO NOT RETROSPECT YET.**

Keep P-340 in the top unresolved queue until the match is final and every derivative field required for settlement is recoverable. The exact corner provider/definition remains unresolved, so the corner row may require field-by-field settlement treatment after the final rather than inference from the score.

**Next local continuation slot after P-340:** `P-341`.
## 2026-09-09 full settlement + retrospective addendum

### Verified final

**Incheon United 2-1 Bucheon FC 1995; HT 1-1.** Goals: Bucheon 33', Mugoša 43', Juan Fernandez 70'. The event timeline contains **7 total corners**.

| Rank | Frozen row | p | Result | Brier |
|---:|---|---:|---|---:|
| 1 | 1H Over 0.5 goals | 0.61 | **WIN** | 0.1521 |
| 2 | Under 10.5 total corners | 0.59 | **WIN** | 0.1681 |
| 3 | Under 2.5 goals | 0.55 | **LOSS** | 0.3025 |
| 4 | Over 2.5 goals | 0.45 | **WIN** | 0.3025 |
| 5 | 1H Under 0.5 goals | 0.39 | **LOSS** | 0.1521 |

**Potential winner:** Incheon — **CORRECT**.  
**Card mean Brier:** **0.2155** (`EXPLORATORY`).

### Actual mechanism

The match entered the **explicitly written 2-1 upper-tail kill state**. Both attacking selections were active, Incheon's central-defensive absence remained relevant, and a Bucheon opener forced the score-state transition. The early-goal read and corner-centre read were good; the full-time goal centre was too low.

### Three-question retrospective

1. **What did the score turn on?** Bucheon scored first, Incheon responded before halftime, and Incheon converted again after the break. The early goal caused the match to occupy a chasing/response branch rather than settle into the 1-0/1-1 low-event family.
2. **Was the driver knowable and in the card?** **Yes.** The card explicitly named both attacking units, Incheon's defensive suspension and **2-1** as an Under kill state. Those factors received only a modest signed net adjustment, leaving the centre at 2.40.
3. **Smallest routine change:** when a named upper-tail score state is supported by both confirmed attacking shapes plus a defensive absence, assign it an explicit branch mass in the joint event object rather than leaving it as an unquantified kill-path sentence.

### What went right / wrong

**Right:** Rank #1, corner Under and winner were correct; first-half modelling was stronger than full-time total modelling.  
**Wrong:** the full-game Under was placed above 50% even though the card itself contained a concrete and current 2-1 mechanism.

**Process grade:** **B-**.

### Learning / rule disposition

No new rule. This reinforces `G16/G22` and the soccer score-state controls: **kill paths must carry enough probability mass to affect ranking when their mechanisms are current and specific**. Under `L-087`, this remains an observation, not a new ordinal weighting rule.

### New source

- Match timeline: https://www.futbol24.com/match/2026/09/08/national/South-Korea/K-League-1/2026/Regular-season/Incheon-Utd/vs/Bucheon-1995


---

# P-341 — BUL FC vs Ntugasaze FC — Uganda Premier League — 2026-09-08

**Status:** OPEN / PREGAME FORECAST — PENDING SETTLEMENT  
**Population:** EXPLORATORY — NOT SCORED  
**Method:** MDS-2026.09.06-v4.0 — SPORTS_ONLY / MARKET_BLIND  
**Freeze:** 2026-09-08 22:58:33 AEST = 15:58:33 EAT, before scheduled 16:00 EAT / 23:00 AEST kickoff.  
**Competition/venue:** 2026/27 Uganda Premier League, Round 3; BUL FC vs Ntugasaze FC; FUFA Technical Centre, Njeru.  
**Competition onboarding:** Uganda Premier League was not recovered in the Drive league-rules reference. Drive remains read-only per user directive, so the onboarding record is preserved locally: senior 18-club Ugandan top flight, ordinary 90-minute league match with draw live, 3/1/0 points; exact operator derivative settlement definitions remain UNKNOWN_DEFINITION. FUFA confirms 18 clubs and current head coaches.  
**Participant state:** same-day official starting XIs/benches were NOT recovered before freeze. BUL coach Alex Isabirye and Ntugasaze coach Pius Ngabo are FUFA-confirmed. Ntugasaze's previous official/reputable match XI/bench is recorded below only as continuity evidence, not today's confirmed XI.  

## Issued ranked rows
1. **1H Over 0.5 goals — 61% UNVALIDATED_SUBJECTIVE — MEDIUM-LOW / FORCED RANK**
2. **Under 2.5 total goals — 58% UNVALIDATED_SUBJECTIVE — MEDIUM-LOW / FORCED RANK**
3. **Over 7.5 total corners — 55% UNVALIDATED_SUBJECTIVE — LOW / FORCED RANK**
4. **Over 2.5 total goals — 42% UNVALIDATED_SUBJECTIVE — MEDIUM-LOW**
5. **1H Under 0.5 goals — 39% UNVALIDATED_SUBJECTIVE — MEDIUM-LOW**

**Potential regulation winner:** BUL FC — 62% UNVALIDATED_SUBJECTIVE; Draw 24%; Ntugasaze 14%.  
**Representative central score:** BUL 2-0 Ntugasaze.  

## Evidence / arithmetic
- Current UPL: BUL 2-0-0, 5:1 goals; Ntugasaze 0-0-2, 1:4 goals.
- BUL current: 1-0 Express (HT 1-0), 4-1 Kataka (HT 2-1). Ntugasaze current: 0-1 Blacks Power (HT 0-0), 1-3 Maroons (HT 0-2).
- BUL continuity L5: 2W-1D-2L, GF 6 GA 6; current two-match league sample is aggressively shrunk toward 2025/26 low-event home regime.
- Ntugasaze continuity uses prior Big League only as a separate lower-tier branch: promoted after a strong late run (3-0 Kiyinda, 2-1 Bunyaruguru, 2-0 Bright Stars, 0-0 Kaaro Karungi, 3-0 Wakiso), but its first two top-flight matches show a materially tougher defensive environment.
- No senior H2H was found; H2H continuity = NOT AVAILABLE / first top-flight meeting.
- Goal prior: BUL attack 1.65, Ntugasaze attack 0.70 => total centre ~2.35 goals, width high due new-season/promoted-team uncertainty. Poisson-shaped diagnostic at lambda 2.35 implies ~58% U2.5; used only as arithmetic support, not a fitted model.
- 1H centre ~0.95 goals => ~61% chance of at least one first-half goal; supported by BUL scoring before HT in both 2026/27 matches and Ntugasaze conceding twice before HT vs Maroons, but heavily shrunk due tiny sample.
- Corner evidence: BUL-Express 11 total corners; Kataka-BUL 5; Ntugasaze-Maroons 11 (Ntugasaze 8). Three-match observed mean ~9.0. Over 7.5 retained at 55% only; exact provider definition, direct cross/end-line chain and today's benches unresolved => LOW / FORCED RANK.
- Weather at FUFA Technical Centre/Njeru around 16:00 EAT: ~29-32C with shower/thunderstorm risk; no deterministic signed goal direction. Surface condition NOT VERIFIED; weather widens variance rather than forcing Under/Over.
- Kill paths: BUL early two-goal separation; Ntugasaze chasing-corner inflation; weather interruption/surface degradation; promoted-side counterattack; BUL current finishing regression.

## Current participant/availability evidence
- FUFA 2026/27 coach list: BUL — Alex Musongola Isabirye; Ntugasaze — Pius Ngabo.
- Ntugasaze previous XI vs Maroons: Richard Afoyo; Simon Mukisa; Apollo Kagogwe; Fredrick Junior Mayindi; Tevin Kevin Kyeyune; Abdallah Kawanguzi; Jacob Opar; Fahad Nsamba; Norman Ndyamuhaki; Ronald Kaye; Jimmy Ndalambi. Previous bench: Isaac Kiberu, Arafat Kakonge, Reagan Steve Male, Shafiq Raiven Magogo, Shafick Matovu, Jerome Otim, Yassintah Sabir, Amisi Muba, Hamza Bukenya. This is NOT today's confirmed XI.
- No authoritative same-day injury/suspension bulletin recovered for either club before freeze. Do not infer full availability.

## Source register
Drive: METHOD.md; RULES_GENERAL.md; RULES_SOCCER.md; CONTROLS.md; PREDICTION_LOG_COMBINED_3.md; LEAGUE_RULES_SOCCER.md search (no Uganda section recovered).  
External: FUFA head-coach list (2026-09-08); FUFA licensing decision (2026-07-23); Ntugasaze official website 2026 signings/coaching/home-ground pages; Kawowo Ntugasaze-Maroons report and full XI/bench; Kawowo Kataka-BUL report; BUL official results/team pages; Sofascore BUL-Ntugasaze fixture; BeSoccer team fixture histories; BetExplorer result histories; UgandaFootball fixture/attendance records; venue-coordinate weather for FUFA Technical Centre, Njeru; Footboom Ntugasaze-Maroons corner stats; Forebet historical corner result pages used only for observed corner counts, not predictions.

**Settlement source pre-registration:** FUFA/official Uganda Premier League result first; field-level corners require a named official/data-partner record after final. If exact corner provider cannot be verified, corner row remains UNSETTLEABLE rather than inferred.  
**Operator action:** UNKNOWN_DEFINITION.  
**Retrospective:** NOT PERFORMED — user explicitly deferred.  

**Next local ID:** P-342.
## 2026-09-09 partial settlement + retrospective addendum

### Verified score state

**BUL FC 4-1 Ntugasaze FC; HT 2-1.** Kawowo reports BUL scored at 10', Ntugasaze equalised at 30', BUL restored the lead before halftime, then added two second-half goals.

### Score-derived row settlement

| Rank | Frozen row | p | Result | Brier |
|---:|---|---:|---|---:|
| 1 | 1H Over 0.5 goals | 0.61 | **WIN** | 0.1521 |
| 2 | Under 2.5 goals | 0.58 | **LOSS** | 0.3364 |
| 3 | Over 7.5 corners | 0.55 | **UNSETTLEABLE TO FROZEN SOURCE STANDARD** | — |
| 4 | Over 2.5 goals | 0.42 | **WIN** | 0.3364 |
| 5 | 1H Under 0.5 goals | 0.39 | **LOSS** | 0.1521 |

**Potential winner:** BUL — **CORRECT**.  
**Partial mean Brier across the four fully settled ranked rows:** **0.2443**.

### Corner row status

The frozen card explicitly pre-registered: **"field-level corners require a named official/data-partner record after final; if exact provider cannot be verified, corner row remains UNSETTLEABLE rather than inferred."** This pass did not recover such an endpoint. Secondary displays previously indicated a 12-corner state, which would be directionally consistent with Over 7.5, but that does **not** meet the card's own frozen settlement standard. No W/L/Brier is booked for Rank #3.

### Actual mechanism

The key miss was the full-time Under. The promoted side did not remain merely a low-scoring underdog: Ntugasaze contributed an equaliser, while BUL's superior attacking level converted repeatedly. The five-goal state was therefore a **mismatch plus underdog-contribution branch**, not simply favourite dominance.

### Three-question retrospective

1. **What did the score turn on?** BUL's attacking superiority was real, but Ntugasaze also scored. Once the match reached 1-1 by 30', the pregame low-total centre was no longer representative and BUL's finishing/depth drove the game to 4-1.
2. **Was the driver knowable and in the card?** **Partly.** The card knew Ntugasaze had conceded four goals in its first two top-flight games and labelled promoted-team uncertainty as wide. However, it shrank aggressively toward BUL's older low-event home regime and partially imported Ntugasaze's lower-tier history into a top-flight translation problem.
3. **Smallest routine change:** for a newly promoted side in its first few top-flight matches, create a separate **promotion-translation defensive branch** before pooling lower-tier form or older opponent home regimes into the same total centre.

### What went right / wrong

**Right:** Rank #1 early-goal call and BUL winner were correct.  
**Wrong:** the 2.35 total centre materially underrepresented the 3+/4+ scoring branch that a class gap plus early-season defensive translation could create.

**Process grade:** **C+** on the settled score fields; derivative completeness remains unresolved.

### Learning / rule disposition

**Observation only — no new rule.** If this exact promoted-team translation failure recurs, it could become a `LEARNING_REGISTER.md` candidate. It is not promoted from one exploratory Uganda Premier League event.

**Potential future destination:** a Uganda Premier League competition subsection in `LEAGUE_RULES_SOCCER.md` for identity/format/source coverage; not a new standalone Markdown document.

### New result source

- Kawowo Sports: https://kawowo.com/2026/09/08/bul-put-four-past-league-newbies-ntugasaze-to-maintain-perfect-start/



---

# P-342 — MŠK Novohrad Lučenec vs KFC Komárno — Slovnaft Cup, Round 3

**Issued view:** PREGAME  
**Scheduled start:** 2026-09-08 16:00 CEST = 2026-09-09 00:00 AEST  
**Freeze:** 2026-09-08 23:57:05 AEST / 15:57:05 CEST  
**Population:** EXPLORATORY — NOT SCORED  
**Method:** MDS-2026.09.06-v4.0 — SPORTS_ONLY / MARKET_BLIND  
**Status:** OPEN / PENDING SETTLEMENT  
**Retrospective:** NOT REQUESTED

## Frozen card

| Rank | Contract | UNVALIDATED_SUBJECTIVE | Evidence |
|---:|---|---:|---|
| 1 | 1H Over 0.5 goals | 68% | MEDIUM-LOW / FORCED RANK |
| 2 | Over 2.5 total goals | 56% | MEDIUM-LOW / FORCED RANK |
| 3 | Over 8.5 total corners | 54% | LOW / FORCED RANK |
| 4 | Under 2.5 total goals | 44% | MEDIUM-LOW |
| 5 | 1H Under 0.5 goals | 32% | MEDIUM-LOW |

**Potential regulation winner:** KFC Komárno 67% / Draw 21% / Lučenec 12%.

## Identity / competition onboarding
- Official SFZ programme: Slovnaft Cup 2026/27, Round 3, MŠK Novohrad Lučenec vs KFC Komárno, 8 Sep 2026 16:00 CEST.
- Single-match cup fixture. Supplied goal contracts are frozen as regulation-only (1H and 90-minute totals). Potential winner is explicitly the **90-minute regulation winner**, not advance/qualify.
- The active Drive league-rules companion did not contain a dedicated Slovak Cup section at research time. Under the user's read-only Drive directive, the onboarding note is preserved locally rather than modifying Drive.
- Current-season exact ET/direct-penalty regulation was not recovered from a field-owning regulation document before cutoff. Prior Slovnaft Cup early-round records show ties decided by penalties after 90 minutes, but that is not used to settle the regulation markets here.
- OPERATOR_ACTION = UNKNOWN_DEFINITION for corner provider/definition and any operator-specific cup abandonment/void rules.

## Participant freeze
Current matchday provider at 15:57 CEST still showed `pred zápasom` and posted:

**Lučenec XI:** Varholák; Málek, Sojka (C), Drugda, Kotora, Hulec, Schmidt, Motoška, Lačný, Adamec, Kuruc.  
**Bench:** Jenčo, Kulich, Pipíška, Ádám, Dudáš, Kovács.  
**Coach:** Igor Kotora.

**KFC Komárno XI:** Dlubáč; Šmehyl (C), Vlasenko, Vojtko, Leoni, Havrylenko, Domonkos, Mitring, Tamás, Palán, Sylvestr.  
**Bench:** Gyurákovics, Žák, Masaryk, Špiriak, Mišovič, Krčík, Vakulya.  
**Coach:** Norbert Czibor.

Participant status = **SECONDARY_ONLY**, because a same-refresh field-owner SFZ XI endpoint was not recovered. No authoritative same-day injury bulletin for both teams was recovered. Non-selection is not labelled injury. Komárno's XI is materially rotated versus its latest league side; Lučenec also rotates several positions. This caps lineup-sensitive rows.

## L5/L10/L15/L20 audit
Lučenec competitive cross-season windows:
- L5: GF 2.20, GA 1.20, total 3.40; O2.5 60%; 1H O0.5 80%.
- L10: GF 1.90, GA 1.30, total 3.20; O2.5 60%; 1H O0.5 80%.
- L15: GF 1.53, GA 1.47, total 3.00; O2.5 60%; 1H O0.5 ~67%.
- L20: GF 1.55, GA 1.20, total 2.75; O2.5 55%; 1H O0.5 65%.

Komárno competitive cross-season windows:
- L5: GF 1.60, GA 1.40, total 3.00; O2.5 80%; 1H O0.5 60%.
- L10: GF 1.40, GA 1.20, total 2.60; O2.5 60%; 1H O0.5 80%.
- L15: GF 1.27, GA 1.27, total 2.53; O2.5 60%; 1H O0.5 80%.
- L20: GF 1.20, GA 1.20, total 2.40; O2.5 60%; 1H O0.5 75%.

Cross-season continuity is discounted for roster/role changes. One old H2H (2019, Lučenec 0-1 Komárno, HT 0-1) is descriptive only.

## Goal-object arithmetic
Long-window total prior:
`(Lučenec L20 2.75 + Komárno L20 2.40) / 2 = 2.575`.

Signed adjustments:
- +0.30 top-flight-vs-third-tier separation / Komárno bench-depth tail.
- -0.15 Komárno heavy rotation/non-selection of several regular league attackers.
- +0.10 Lučenec current attacking/home scoring regime.
- +0.00 venue weather direction (hot/sunny but no reliable one-way scoring mechanism).

Working total centre = **2.83 goals**, approximate width **1.9**.  
Approximate allocation = **Komárno 1.95, Lučenec 0.88**.

This yields a modest O2.5 lean, not a dominant one: Over 56%, Under 44%.

For the first-half target, current early-goal windows are materially stronger than the full-time total signal. A diagnostic phase centre near 1.2 goals would imply roughly 70%+ for a first-half goal, but lineup/knockout/rotation uncertainty is shrunk to **68% O0.5 / 32% U0.5**.

## Corner process
Current reliable Lučenec corner-rate coverage was not recovered. Komárno recent observed match totals include roughly 10 vs Skalica, 9 vs Banská Bystrica, and other 7–10 corner games. A chasing Lučenec branch can add width/set-piece exposure, while an early multi-goal Komárno lead can suppress later corner demand. Exact operator/provider definition and full direct cross/block/end-line data are missing.

Therefore **Over 8.5 corners = 54%, LOW / FORCED RANK** only.

## Weather / surface
Venue-specific hourly forecast for Mestský futbalový štadión, Športová 1, Lučenec: around 31°C at pregame, sunny, 0% precipitation through the main match window. No current adverse-pitch report was recovered. Weather gets **0.00 signed direction**; heat is treated as uncertainty/fatigue context rather than an automatic Under.

## Coherence / kill paths
Central score families: **Komárno 2-0, 2-1**. Upper mismatch branch: **3-0 / 3-1**.
- 1H Over can cash in both central and mismatch states.
- Over 2.5 depends on either Lučenec contributing or Komárno's rotated side still achieving 3+ separation.
- Under 2.5 remains live through 1-0/2-0 control states.
- Corner Over kill path: early Komárno multi-goal control reduces attacking demand and match width.

## Source register
- SFZ official administrative/programme notice: Slovnaft Cup R3, Lučenec–Komárno, 08.09.2026 16:00 CEST.
- SFZ/Sportnet competition programme: Round 3 schedule.
- KFC Komárno official fixtures: Slovnaft Cup Round 3 fixture and previous cup result.
- STVR official programme: live broadcast window for Lučenec–Komárno.
- Onlajny current matchday page: pregame state, XIs, benches, coaches, referee (secondary live provider; betting-price fields excluded by MARKET_BLIND).
- MŠK Novohrad Lučenec official/club recent match records and BetExplorer match sequence for form windows.
- KFC Komárno official match report vs Skalica and BetExplorer match sequence for form windows.
- Venue-specific hourly weather feed for Mestský futbalový štadión, Lučenec.

**No retrospective performed.**

**Next local ID: P-343.**
## 2026-09-09 partial settlement + DEEP Rank-#1 retrospective addendum

### Verified final

Official/competition reporting confirms **MŠK Novohrad Lučenec 0-2 KFC Komárno, HT 0-0**, with Komárno goals at 74' and 90'.

### Score-derived settlement

| Rank | Frozen row | p | Result | Brier |
|---:|---|---:|---|---:|
| 1 | 1H Over 0.5 goals | 0.68 | **LOSS** | 0.4624 |
| 2 | Over 2.5 total goals | 0.56 | **LOSS** | 0.3136 |
| 3 | Over 8.5 corners | 0.54 | **PROVISIONAL RESEARCH WIN — 16 reported corners** | not booked |
| 4 | Under 2.5 total goals | 0.44 | **WIN** | 0.3136 |
| 5 | 1H Under 0.5 goals | 0.32 | **WIN** | 0.4624 |

**Potential regulation winner:** Komárno — **CORRECT**.  
**Mean Brier across the four fully settled score rows:** **0.3880**.  
If the provisional 16-corner field were later accepted under the exact frozen provider definition, its row Brier would be **0.2116** and the indicative five-row mean would be **0.3527**; those figures are **not** entered as final scorecard values now.

### Corner settlement status

Two current post-final secondary structured sources report **Lučenec 1-15 Komárno = 16 corners**, comfortably clearing Over 8.5. However, the card never had a frozen operator/provider definition and the current soccer rules say aggregator agreement does not automatically promote a niche field to full settlement. Therefore:
- `RESEARCH_DIRECTION = PROVISIONAL WIN`;
- `OPERATOR_ACTION = UNKNOWN_DEFINITION`;
- full field-owner-grade C03 settlement remains open.

### Actual mechanism

The match realized the **2-0 control branch** already printed in the pregame kill paths, but the goals came late. Komárno's rotated side eventually asserted quality and territorial pressure, yet the rotation reduced early conversion enough to keep the first half scoreless and the final at exactly two goals.

### Three-question retrospective

1. **What did the score turn on?** Komárno controlled enough territory to win but did not convert until 74'; the second goal came at 90'. The class gap showed up in eventual result and corner pressure, not in the early-goal or 3+ goal markets.
2. **Was the driver knowable and in the card?** **Yes.** The card explicitly documented heavy Komárno rotation and stated that a 1-0/2-0 control state was an Under kill path. The error was giving the class gap/early-goal history more mass than the rotated-favourite "territorial control without early conversion" branch.
3. **Smallest routine change:** in a cup mismatch with a heavily rotated favourite, split **territorial dominance** from **conversion timing** and explicitly weight a "late depth breakthrough / 1-0 or 2-0" branch before ranking 1H Over and FT Over.

### Deep review

**What went right**
- Potential winner was correct.
- The class-gap/pressure read appears consistent with the enormous reported corner edge.
- The 2-0 control state was explicitly present before issue.

**What went wrong**
- Rank #1 at 68% was the most serious miss in the local cohort because the actual HT state was 0-0 and the card had already documented rotation.
- Rank #2 Over 2.5 also lost; the final total was only two.
- The knockout/rotation uncertainty was acknowledged but not allowed to change the order enough.

**Process grade:** **C-**.

### Learning / rule disposition

No new rule. `RULES_SOCCER.md` already contains rotation and knockout-population controls. This is an **application failure**: class gap was allowed to imply timing/total conversion too readily.

**Potential destination if repeated:** `LEARNING_REGISTER.md` observation on rotated cup favourites; not `CONTROLS.md` yet.

### New sources

- Official/competition result coverage: https://sportnet.sme.sk/spravy/futbal-vysledky-dnes-utorok-8-september-3-kolo-slovnaft-cup-2026-2027/
- SFZ/Sportnet competition program: https://sportnet.sme.sk/futbalnet/z/sfz/s/slovnaft-cup/program/
- Secondary corner corroboration: https://www.forebet.com/en/football/matches/sk-novohrad-lucenec-kfc-komarno-2535121



---

# P-343 — Bangladesh Women vs United Arab Emirates Women — DP World Women’s T20 Asia Cup 2026, Group B

**Requested view:** PREGAME
**Official scheduled start:** 2026-09-08 18:30 GST (UTC+04:00) = 2026-09-09 00:30 AEST
**Population:** EXPLORATORY — NOT SCORED
**Method:** MDS-2026.09.06-v4.0 — SPORTS_ONLY / MARKET_BLIND
**Final issuance state:** **START CROSSED — LIVE STATE NOT VERIFIED — NO ACTIONABLE LIVE FORECAST**
**Ranked rows issued:** NONE
**UNVALIDATED_SUBJECTIVE probabilities issued:** NONE
**Potential winner issued:** NONE
**Retrospective:** NOT PERFORMED — user explicitly deferred

## Why no card issued
- The user specified that “first innings” means the team batting first. Therefore the supplied Bangladesh 20-over and 6-over first-innings contracts require a verified toss/innings order before they can be frozen as Bangladesh targets.
- Drive cricket rule `CR-P3` permits an unresolved toss only as a LOW-evidence mixture when the exact target survives all material innings-order states. This request does **not** survive both states because Bangladesh may not be the team batting first under the user's own contract definition.
- Before 00:30 AEST, current Cricbuzz, cricket.com.au, Wisden and myKhel records still had no toss and no confirmed XI.
- At 00:30:04 AEST the scheduled start had passed. Under the Drive start-crossing invariant, an “upcoming/preview” shell after scheduled start cannot preserve PREGAME status.
- Immediate post-start refreshes through 00:31:47 AEST still did not establish toss, batting order, exact score/balls, or an explicit field-owner zero-play delay. Therefore the only compliant disposition was `LIVE STATE NOT VERIFIED — NO ACTIONABLE LIVE FORECAST`.

## Contract freeze attempted
Requested candidate slate, not issued:
1. Bangladesh Women first-innings 20-over total: Over 139.5 / Under 139.5.
2. Bangladesh Women first-innings powerplay (overs 1–6) total: Over 42.5 / Under 42.5.

These were **not ranked** and **no probabilities were minted**, because the batting-order target was unresolved at the pregame cutoff.

## Competition / rules state
- Women’s Asia Cup 2026 is a T20 competition: one innings per side, 20 overs, six-over powerplay under the ICC-derived T20 playing conditions, DLS/shortening rules applicable, and five overs minimum for a result in a normal T20 unless tournament-specific terms supersede.
- ICC confirmed the 2026 Women’s Asia Cup squads and Group B composition; Emirates Cricket officially scheduled Bangladesh vs UAE for 8 September at Dubai International Stadium, 18:30 local.
- Operator-specific shortening/void/action wording was not supplied: `OPERATOR_ACTION = UNKNOWN_DEFINITION`.

## Current squad / participant evidence recovered before start crossing
Bangladesh tournament squad includes Nigar Sultana Joty (c), Nahida Akter (vc), Dilara Akter, Juairiya Ferdous, Sharmin Akter Supta, Sarmin Sultana, Sobhana Mostary, Shorna Akter, Ritu Moni, Fahima Khatun, Rabeya Khan, Marufa Akter, Sultana Khatun, Shanjida Akther Maghla and Farjana/Fariha squad variation across ICC/BCB-listed releases.

UAE official tournament squad: Esha Oza (c), Archara Supriya, Heena Hotchandani, Indhuja Nandakumar, Janani Thirukkumaran, Lavanya Keny, Mehul Kulkarni, Rinitha Rajith, Samaira Dharnidharka, Siya Gokhale, Sashikala/Athige Silva, Suraksha Kotte, Theertha Satish (wk), Uttara Iyer and Vaishnave Mahesh.

No same-cutoff confirmed playing XI or current injury/rest list for both sides was recovered before the scheduled start. Probable/fantasy XIs were explicitly not promoted to facts.

## Recent tournament context — research only, not a forecast
- Bangladesh first-innings totals in this Asia Cup before this match: **129/8 vs Indonesia** and **114/8 vs Sri Lanka**.
- Against Sri Lanka, Bangladesh were about six runs per over through the five-over mark before finishing 114/8, illustrating that powerplay pace and full-innings ceiling are separate processes.
- UAE beat Indonesia after bowling them out in 19.4 overs and chasing the small target in 13.1 overs; this chase is target-censored and is not used as a first-innings batting baseline.

## Pitch / strip search
**STRIP STATUS: NOT FOUND AFTER SEARCH for an observed exact-match strip report before cutoff.**
Attempts included:
- Cricbuzz exact-match match centre/commentary: no toss or strip assessment before/just after start.
- cricket.com.au exact match centre: still “Upcoming”, teams not announced.
- ICC / Emirates Cricket tournament and squad releases: schedule/squads, no exact-match strip description.
- Exact venue + pitch/curator web searches: Cricbuzz venue guide identified Dubai International Stadium and curator context; no toss-day strip observation.
- Specialist exact-match preview: Female Cricket described the venue tendency as balanced, with new-ball bounce/movement and a surface that can settle for batting. This is labelled **preview/historical venue tendency**, not an observed live strip.
- No current ICC pitch/outfield monitoring rating specific to this match was recovered.

Venue-context only: Cricbuzz's T20 venue page listed a broad historical first-innings average around **140**, but this aggregates competitions/eras/sexes and therefore cannot own a women’s 2026 Asia Cup target without adjustment.

## Match conditions
At approximately 18:30 local, structured venue weather showed about **38°C**, clear conditions, no meaningful rain signal. Hot, dry evening conditions reduce interruption risk but do not by themselves determine batting direction or total-run sign. Dew was discussed by secondary broadcast-preview material as a possible second-innings factor, but was not directly observed before the cutoff.

## Source register
- Google Drive `METHOD.md` — MDS-2026.09.06-v4.0, start-crossing and probability requirements.
- Google Drive `RULES_CRICKET.md` — `CR-P1`–`CR-P5`, toss/innings-order, XI/phase-role and strip/conditions requirements.
- Google Drive `LEAGUE_RULES_CRICKET.md` — T20 format, six-over powerplay, DLS and result rules.
- ICC: “All the squads at the Women’s Asia Cup 2026”; Bangladesh squad announcement; Bangladesh–Sri Lanka report/scorecard context.
- Emirates Cricket Board: official UAE Women Asia Cup squad and official 8 Sep Bangladesh fixture at 18:30 local.
- cricket.com.au: Bangladesh Women v UAE Women match centre, still upcoming/teams TBD around scheduled start.
- Cricbuzz: match ID 169871, exact match centre/scorecard/commentary; no toss/XI/score through immediate post-start checks; venue guide and prior Bangladesh/UAE tournament scorecards.
- Female Cricket exact-match preview: historical/preview pitch tendency only, not observed strip.
- Structured venue weather source for Dubai International Cricket Stadium.

**No retrospective performed.**
**Next local ID: P-344.**
## 2026-09-09 administrative closure review — NO FORECAST RETROSPECTIVE

### Official final

Asian Cricket Council match record: **Bangladesh Women 103/7 beat UAE Women 69/9 by 34 runs**.

No forecast had been issued because the exact Bangladesh first-innings target depended on a toss/innings-order fact that was not verified before the scheduled start crossed.

### Three-question administrative review

1. **What did the outcome turn on?** Bangladesh ultimately batted first, made 103/7, then restricted UAE to 69/9.
2. **Was that knowable before issue and in the card?** Bangladesh batting first was **not verified at the required pregame cutoff**. The card correctly refused to treat an unresolved conditional Bangladesh first-innings market as unconditional.
3. **Smallest routine change:** earlier toss/XI acquisition for innings-order-dependent cricket targets; no sporting probability may be backfilled after the fact.

**Process disposition:** `ADMINISTRATIVE PASS — TARGET/TOSS/START GATES WORKED`.  
**No W/L, Brier or potential-winner grade exists.**

### New official source

- Asian Cricket Council scorecard: https://www.asiancricket.org/match/415/2798



---

# P-344 — Hungary Women vs Japan Women — FIBA Women’s Basketball World Cup 2026, Qualification to Quarter-Finals

**Requested view:** PREGAME
**Official scheduled start:** 2026-09-08 17:45 CEST (Europe/Berlin) = 2026-09-09 01:45 AEST
**Venue:** Berlin Arena, Berlin, Germany
**Population:** EXPLORATORY — NOT SCORED
**Method:** MDS-2026.09.06-v4.0 — SPORTS_ONLY / MARKET_BLIND
**Frozen pregame cutoff:** 2026-09-09 01:36:45 AEST
**GAME-STATE:** PREGAME — FIBA official game page still showed the qualification fixture without live score at final refresh.
**Operator endpoint:** UNKNOWN_DEFINITION for spread/total OT treatment. Research mapping below assumes a conventional completed FIBA full game including any overtime; if the user's operator settles regulation only, the exact probabilities do not apply.

## Issued ranked card
1. **Japan Women +3.0 — 56% WIN / 7% PUSH / 37% LOSS — FORCED RANK / MEDIUM-LOW**
2. **Over 146.5 points — 54% — FORCED RANK / MEDIUM-LOW**
3. **Under 146.5 points — 46% — MEDIUM-LOW**
4. **Hungary Women -3.0 — 37% WIN / 7% PUSH / 56% LOSS — MEDIUM-LOW**

**Potential winner (completed game including OT): Hungary Women — 54% UNVALIDATED_SUBJECTIVE.** Japan 46%.

## Identity / competition state
- FIBA official event page: Qualification to Quarter-Finals, Hungary vs Japan, Berlin Arena, 17:45 local on 8 Sep 2026.
- The winner advances to the quarter-finals. Standard FIBA game structure applies (four 10-minute quarters; overtime if required to produce a winner in this knockout game).
- Full-game spread/total operator treatment was not supplied, therefore `OPERATOR_ACTION = UNKNOWN_DEFINITION`.

## Participant / availability state
- FIBA confirmed the final World Cup rosters before the tournament.
- Hungary's current World Cup leaders include Dorka Juhasz (17.0 PPG, 12.3 RPG), Virag Takacs-Kiss (13.0 PPG, 10.0 RPG), Reka Lelik and Agnes Studer. Juhasz played 24/33/27 minutes in the three group games, so the earlier pre-tournament injury concern is not treated as a current restriction.
- Japan's current leaders include Kokoro Tanaka (16.0 PPG), Saki Hayashi (11.0 PPG after three group games), Norika Konno, Rui Machida, Maki Takada, Ramu Tokashiki and Stephanie Mawuli. Hayashi played 22 minutes against Spain on Sep 7, so she is not treated as absent.
- No new official FIBA withdrawal/injury announcement for a decision-driving player on either side was recovered before the cutoff.
- The official game page had not published a confirmed starting five at the frozen cutoff. Start/minutes are therefore modelled as current-role mixtures. This caps dependent full-game rows at `FORCED RANK / MEDIUM-LOW`.

## Current World Cup process
Hungary group results:
- HUN 53–99 FRA
- HUN 71–67 NGR
- HUN 82–73 KOR
Current tournament: **68.7 PF, 79.7 PA, 148.3 combined**.

Japan group results:
- JPN 102–97 MLI
- JPN 58–74 GER
- JPN 59–79 ESP
Current tournament: **73.0 PF, 83.3 PA, 156.3 combined**.

Official FIBA team comparison before this match:
- Hungary: 43.7 RPG, 19.3 APG, 48.8% 2PT, 29.5% 3PT, 74.6% FT.
- Japan: 31.7 RPG, 14.0 APG, 49.0% 2PT, 32.6% 3PT, 70.5% FT.

FIBA's exact-match preview adds the decisive matchup split:
- Hungary turnovers: **23.0/game**; Japan **12.7/game**.
- Japan bench scoring: **34.3/game**; Hungary **24.7/game**.
- Hungary holds a large rebounding advantage.

## Form windows / trend test
Same-event / recent-national-team reconstruction:
- Hungary L5: 72.6 PF, 75.0 PA, **147.6 total**.
- Hungary L10: 73.2 PF, 75.9 PA, **149.1 total** (mixed World Cup, preparation, qualifying and older international windows; context only).
- Japan L5: 76.2 PF, 83.4 PA, **159.6 total**.
- Japan L10: 80.1 PF, 74.5 PA, **154.6 total** (mixed World Cup, preparation/William Jones/international windows; context only).
- L15/L20 were not reconstructed to a reliable same-roster/same-regime standard before cutoff; they are recorded as missing rather than fabricated. This contributes to the evidence cap.

Trend interpretation: Japan's L5 high total is materially inflated by 102–97 vs Mali and high-scoring preparation games, while their two most recent European matchups finished 58–74 and 59–79. Hungary's current World Cup is also bimodal: 53–99 vs France, then 71–67 and 82–73. Recent totals receive no automatic streak weight.

## H2H continuity
- March 2026 World Cup Qualifying Tournament: Hungary beat Japan **77–65**; Dorka Juhasz scored 35 points and Hungary's size was a decisive matchup mechanism.
- February 2024 Olympic qualifier: Hungary beat Japan **81–75**.
- H2H is used only as mechanism context because the current matchup still features the same core size-vs-speed/turnover tension; it is not a standalone weighting rule.

## Joint score object / explicit arithmetic
World Cup cross-score prior:
- Hungary raw = (68.7 HUN PF + 83.3 JPN PA) / 2 = **76.0**.
- Japan raw = (73.0 JPN PF + 79.7 HUN PA) / 2 = **76.35**.

Signed adjustments:
Hungary:
- **-2.0** Japan turnover pressure / transition generation against Hungary's 23 TO/game.
- **+1.5** Hungary offensive-rebound/paint advantage through Juhasz + Takacs-Kiss.
- **-0.5** knockout half-court/control branch and lineup uncertainty.
= **75.0 projected Hungary centre**.

Japan:
- **-2.2** Hungary size/rebounding/paint suppression.
- **+1.4** transition points created by Hungary ball-security weakness.
- **-1.0** shooting normalization after the 20-three opener; Japan shot only 11.1% from three vs Germany and 23.3% vs Spain.
= **74.55 projected Japan centre**.

Working joint centre: **Hungary 75.0 – Japan 74.5; total ≈149.5; margin HUN +0.5**.
Practical central score family after rounding/branch shrinkage: **Hungary 75–73 / 76–74 / Japan 74–73**.
Approximate total width: **15–17 points**. Approximate margin width: **10–12 points**.

## Team-score budget at 146.5
- If Japan scores 70, Hungary needs 77+ for the Over.
- If Japan scores 73, Hungary needs 74+.
- If Japan scores 76, Hungary needs 71+.
Both ordinary centre branches cross the line, so Over 146.5 is only a modest lean rather than a high-confidence pick.

## Spread separation budget at HUN -3 / JPN +3
The working centre is inside the +3/-3 corridor rather than beyond it.
- Japan outright win branches all cash JPN +3.
- Hungary wins by 1–2 also cash JPN +3.
- Hungary exactly +3 pushes both integer spreads.
- Hungary must win by 4+ for HUN -3 to cash.
This is why Japan +3 ranks above Hungary as the potential winner call.

## Bidirectional-sign audit / kill paths
- Hungary size helps scoring via second chances and hurts Japan's interior efficiency, but can be offset by Japan forcing turnovers before Hungary reaches the half court.
- Japan's fast transition/three-point game lifts the total when shots fall, but its high three-point variance can also produce prolonged scoring droughts as against Germany and Spain.
- Late fouling in a close knockout game is an Over tail; a decisive early separation and slower half-court close is an Under tail.
- Overtime is an explicit Over tail and can also move the spread; operator regulation-vs-OT wording remains unknown.

## Source register
- Google Drive `METHOD.md` — MDS-2026.09.06-v4.0.
- Google Drive `RULES_GENERAL.md` — pregame cutoff, participant release, integer-line push treatment, one-distribution requirement.
- Google Drive `RULES_BASKETBALL.md` — FIBA/full-game identity, starting-five/availability mixture, possession/efficiency process, team-score and separation budgets, OT branch.
- Google Drive `CONTROLS.md` — G13.1, G14.2, G16, G20/G20.1, G22, G31.
- FIBA official Hungary–Japan game page (event 128145) — identity, venue, schedule, referees, current pregame state, World Cup team comparison.
- FIBA official September 8 preview — turnover, bench-scoring and rebounding matchup; March 2026 77–65 H2H context.
- FIBA official Hungary and Japan team profiles — current tournament leaders and current-stage rosters.
- FIBA official player profiles — Juhasz, Takacs-Kiss, Hayashi, Tokashiki and current tournament minutes/statistics.
- FIBA official group game pages — HUN-FRA, NGR-HUN, HUN-KOR, JPN-MLI, GER-JPN, JPN-ESP.
- FIBA official March 2026 Istanbul qualifying tournament schedule/results and JPN-HUN 65–77 game page.
- FIBA official preparation-game tracker — Hungary 68–62 Germany on Aug 23.
- AiScore recent national-team result lists used only to reconstruct mixed-regime L5/L10 chronology; official FIBA pages override all event facts where available.

**No retrospective performed.**
**Next local ID: P-345.**
## 2026-09-09 full settlement + DEEP Rank-#1 retrospective addendum

### Official FIBA final

**Hungary 84-63 Japan**. FIBA's event report identifies **Réka Lelik** as Hungary's decisive "third dimension"; her official tournament reporting credits a major scoring/rebounding contribution. FIBA's player profile shows **Saki Hayashi played only 8 minutes against Hungary**, down from 22–23 minutes in Japan's prior group games.

| Rank | Frozen row | p | Result | Brier |
|---:|---|---:|---|---:|
| 1 | Japan +3.0 | 0.56 win probability | **LOSS** | 0.3136 |
| 2 | Over 146.5 | 0.54 | **WIN — final total 147** | 0.2116 |
| 3 | Under 146.5 | 0.46 | **LOSS** | 0.2116 |
| 4 | Hungary -3.0 | 0.37 win probability | **WIN** | 0.3969 |

**Potential winner:** Hungary — **CORRECT**.  
**Card mean Brier:** **0.2834** (`EXPLORATORY`).

### Actual mechanism

The pregame card centred the margin at Hungary +0.5; the actual margin was **Hungary +21**. Hungary's size/rebounding advantage remained important, but the decisive separation was broader than a Juhasz-only mismatch: **Lelik became an additional scoring/creation axis**, while Japan's perimeter attack failed to generate enough efficient scoring. Hayashi's in-game availability was also materially reduced to eight minutes, an event that was **not knowable pregame** from the evidence available at cutoff.

The total Over won by **only 0.5 points** (147 vs 146.5). That should not be treated as strong validation of the projected 149.5 centre; the spread distribution was the larger modelling failure.

### Three-question retrospective

1. **What did the score turn on?** Hungary converted its size/rebounding foundation into a much larger two-way margin, Lelik supplied a decisive secondary scoring dimension, and Japan did not sustain enough perimeter offence. Hayashi's sharply reduced minutes added an in-game disruption.
2. **Was the driver knowable and in the card?** **Partly.** Hungary's rebounding/size edge and Japan's shooting volatility were explicitly known. Lelik was a current player but her decisive high-usage scoring branch was not sufficiently represented. Hayashi's in-game injury/minutes reduction was not knowable before issue and must not be backfit into a pregame rule.
3. **Smallest routine change:** for basketball knockout spreads, explicitly model a **secondary/third scorer usage-transfer branch** when the defence focuses on the primary interior star, and separately tag in-game injury disruption so it is not confused with a pregame model miss.

### Deep review

**What went right**
- Hungary was correctly named the potential winner.
- The size/rebounding mismatch was correctly identified.
- The Over direction survived, although only by half a point.

**What went wrong**
- Rank #1 Japan +3 failed by a very large distance.
- The HUN +0.5 central margin was far too compressed.
- The card gave Japan turnover pressure/transition too much ability to neutralize Hungary's physical and half-court advantages.
- The scoring tree was too concentrated on Juhasz/Takacs-Kiss and did not sufficiently represent a high-impact Lelik branch.

**Irreducible post-issue factor**
- Hayashi's reduction to eight minutes was not a pregame-known absence. It can explain part of Japan's offensive downside, but it does **not** erase the model error: the retrospective must separate this unforeseeable in-game shock from the already-underweighted Hungary separation branch.

**Process grade:** **C**.

### Learning / rule disposition

No new rule. `RULES_BASKETBALL.md` already requires minutes/lineup branches, replacement quality and one joint score distribution. Record this as:
- **application observation:** secondary-scorer usage transfer needs more explicit treatment in mismatch trees;
- **disruption note:** in-game injury is aleatory unless pregame evidence existed;
- no new `CONTROLS.md` promotion from one exploratory game.

### New official sources

- FIBA game-center result/report: https://www.fiba.basketball/en/events/fiba-womens-basketball-world-cup-2026/news/2026-wwc-game-center-sep-8-9
- FIBA Japan player profile / Hayashi minutes: https://www.fiba.basketball/en/events/fiba-womens-basketball-world-cup-2026/teams/japan/236949-saki-hayashi
---

# 9. 2026-09-09 CROSS-CARD RETROSPECTIVE SYNTHESIS

## 9.1 Local cohort settlement summary

Issued forecast cards in this mini-log: **P-335, P-336, P-337, P-338, P-339, P-340, P-341, P-342, P-344**.

- Rank #1 record on those nine issued cards: **6 W / 3 L** (`P-339`, `P-342`, `P-344` losses).
- Potential-winner calls: **8 correct / 1 incorrect** (`P-337` draw instead of Argentinos), descriptive only.
- Fully settled binary ranked rows currently available locally: **39**, comprising **20 W / 19 L**.
- One additional `P-342` corner row is a **provisional research WIN** but is not counted as a final scored row.
- `P-341-C03` remains unscored under its frozen corner-source gate.
- `P-333`, `P-334`, `P-343` were no-action/admin closures and contribute **zero** forecast rows.

These counts mix `PRIMARY_SCORED` and `EXPLORATORY` populations and therefore are **not** a valid headline performance statistic, calibration claim, ROI measure or market-edge result.

## 9.2 Most important general learnings — observations, not promoted weights

### Observation A — final score and underlying process must remain separate

`P-336` finished 1-0 and the Under won, but Estudiantes produced 27 shots, eight on target and nine corners. The literal contract result was right while the "low-event" interpretation would have been wrong. This reinforces the existing soccer rule to decompose:
`chance creation -> shot quality -> finishing -> goalkeeping -> final goals`.

**Action:** no new rule; apply the existing rule more rigorously in retrospectives and pregame Under construction.

### Observation B — kill paths that are current and specific must carry probability mass

`P-340` explicitly named 2-1 as a live Under kill state and had current attacking-lineup + defensive-absence evidence for it. The match finished 2-1. `P-342` explicitly named 1-0/2-0 control as a kill state and finished 0-2. A kill path written only as prose is not enough if the current evidence makes it ordinary.

**Action:** reinforce `G16/G22`; no new weighting rule.

### Observation C — veteran/current-regime conflict requires branch weighting, not narrative choice

`P-339` knew both Ryu's strong established prior and his poor short current run. The poor short run effectively won the pregame arithmetic; the game realized the strong-skill branch. `P-335` similarly knew Pivetta could return well but gave more explicit scoring mass to the short-start uncertainty branch.

**Action:** `RULES_BASEBALL.md` controls 11/13 already cover this. Mark as application failures; do not invent a new baseball rule.

### Observation D — promoted-team translation is a distinct uncertainty problem

`P-341` mixed Ntugasaze's lower-tier promotion run, only two top-flight matches, and BUL's older low-event home regime. The result was 4-1. Lower-tier competence and top-flight defensive translation should not be pooled as though they were one stable population.

**Action:** single-event `LEARNING_REGISTER.md` observation only. Consider candidate status only if this recurs.

### Observation E — rotated cup favourites can dominate territory without early conversion

`P-342` is a clean example: Komárno won 2-0, the reported corner state was 15-1 in their favour, but HT was 0-0 and both Over-based top rows lost. Class gap can manifest in territory and late depth without producing a first-half goal or 3+ final goals.

**Action:** reinforce existing soccer rotation/knockout controls; no new gate.

### Observation F — basketball winner and spread are different questions

`P-344` correctly identified Hungary as the likelier winner but placed the margin centre around +0.5 and ranked Japan +3 first. Hungary won by 21. The size matchup, a secondary scorer breakout and an in-game Japan injury combined into much greater separation.

**Action:** reinforce the basketball separation budget and usage-transfer/secondary-scorer branches. The in-game injury is explicitly not backfit as a pregame rule.

### Observation G — derivative distance-to-line remains useful as a diagnostic only

`P-337` Argentinos team corners Over 4.5 lost with exactly four corners. This is another useful distance-to-line record, but it does not turn a loss into a partial win and does not justify a new ordinal rule.

**Action:** append to the existing distance-to-line watch item if the canonical reconciliation is performed. Because this is an exploratory card, do not count it toward the primary 25-card promotion cadence.

## 9.3 Rule-change decision

**PROMOTED NEW RULES: NONE.**

Reason:
- `METHOD.md` v4.0 deliberately prevents per-event lesson inflation.
- `L-087` prohibits turning one same-session retrospective finding into a new predictive weight/ordinal rule.
- Most observed failures already map to existing controls in `RULES_SOCCER.md`, `RULES_BASEBALL.md`, `RULES_BASKETBALL.md`, or `RULES_TENNIS.md`.
- The genuinely new-looking item (promoted-team top-flight translation) appears once and remains an observation.

## 9.4 Where each learning should live in the Google Drive repository — NOT IMPLEMENTED HERE

| Material from this pass | Recommended eventual Drive location | Action now |
|---|---|---|
| `P-333`–`P-344` settlements, W/L/Brier and retrospectives | `PREDICTION_LOG_COMBINED_3.md` | **Record in this local mini-log only; no Drive edit** |
| P-335 primary MLB scorecard increment | `PREDICTION_LOG_COMBINED_3.md` top running Brier snapshot | Local calculation recorded; no Drive edit |
| P-337 distance-to-line miss (1 corner) | Existing candidate-watch history in `CONTROLS.md` / `LEARNING_REGISTER.md` | Observation only; no promotion |
| P-341 promoted-team translation observation | `LEARNING_REGISTER.md` if retained as a candidate observation | Do not promote yet |
| P-342 rotated-cup late-breakthrough observation | `LEARNING_REGISTER.md` only if recurrence develops | No rule change |
| P-344 secondary-scorer / in-game disruption observation | Per-card retrospective first; `LEARNING_REGISTER.md` only if recurring | No rule change |
| Venezuela Primera onboarding from P-336 | `LEAGUE_RULES_SOCCER.md` competition section | Recommended future reconciliation |
| K League 1 onboarding from P-340 | `LEAGUE_RULES_SOCCER.md` competition section | Recommended future reconciliation |
| Uganda Premier League onboarding from P-341 | `LEAGUE_RULES_SOCCER.md` competition section | Recommended future reconciliation |
| Slovnaft Cup onboarding from P-342 | `LEAGUE_RULES_SOCCER.md` competition section | Recommended future reconciliation |
| New/expanded post-final source notes | existing `SOURCES.md` / `DATA_SOURCE_REGISTER.md` | Source-role observations below; no Drive edit |
| Part-2 historical appendix updates | `PREDICTION_LOG_COMBINED_2.md` lettered unsettled appendix | Preserve historical IDs; no Part-3 copy |

**No new Markdown document is required** by the findings in this pass.

## 9.5 Source-role observations / new source candidates

These are source-role observations, **not automatic field-owner promotions**:

1. **PlaymakerStats / zerozero / leballonrond family** — useful structured post-final soccer fields (shots, SOT, corners, xG where present). Strong research/cross-check utility, but still secondary to an official competition/data-partner definition.
2. **Futbol24** — useful minute-by-minute event timelines, including reconstructable corner events; appropriate as a cross-check when provenance is clear, not an automatic provider-definition substitute.
3. **Forebet post-final corner display** — can corroborate niche corner counts in sparse competitions; remains secondary and cannot alone repair an unfrozen operator/provider definition.
4. **KBO official Korean news/scoreboard** — field-owner source for KBO finals and current Korean-language match detail; reinforces `L-067` native-language sourcing.
5. **FIBA game reports + player profiles** — field-owner route for result, current player minutes and tournament context.
6. **Asian Cricket Council scorecards** — field-owner route for Women’s Asia Cup finals/innings state.
7. **Kawowo Sports** — strong specialist current Uganda football reporting for result/timeline when league official match detail is sparse; not automatically a corner-stat field owner.

---

# 10. HISTORICAL GOOGLE DRIVE APPENDIX SETTLEMENT REVIEW — PART 2 ONLY

`PREDICTION_LOG_COMBINED_2.md` remains the closed authority for the inherited unsettled/incomplete records. They are **not** renumbered or migrated into Part 3. This 2026-09-09 pass checked their latest known dispositions and performed a fresh search where useful.

| Historical ID | Existing Part-2 disposition | 2026-09-09 update | Canonical/temporary-ID action |
|---|---|---|---|
| `P-126` | Identity/state conflict unresolved | **UNCHANGED — unresolved.** No authenticated final/identity chain sufficient to repair the event. | Retain `P-126`; no temporary ID |
| `P-148-C02` | Provisional loss — Toluca team corners | **STRENGTHENED PROVISIONAL LOSS.** Fresh post-match feeds support the lower Toluca corner count rather than the previously ambiguous ordering, but provider-definition ownership is still not upgraded. | Retain historical ID |
| `P-149-C02` | Provisional win — Ventura team corners | **UNCHANGED.** No stronger field-owning corner endpoint recovered. | Retain historical ID |
| `P-166` | Research settled; operator endpoint unknown | **UNCHANGED — research settled.** | Retain historical ID |
| `P-176-C05` | Provisional win — Amiens/Versailles Under 10.5 corners | **STRENGTHENED.** Current APWin/Football365/TotalCorner evidence consistently gives **5-3 = 8 corners**. Still a research/provisional field under the frozen provider standard. | Retain historical ID |
| `P-178-C05` | **Previously unresolved** — Cannes/Le Puy Under 10.5 corners | **MATERIAL UPDATE: PROVISIONAL LOSS.** Current Playmaker/LeBallonRond-family statistics give **8-8 = 16 corners**; Forebet independently displays **8-8**. This defeats Under 10.5. It is not promoted to field-owner settlement because the exact provider definition was not frozen. | Retain `P-178`; no temporary ID |
| `P-179-C05` | Provisional win — Thionville/Paris 13 Under 10.5 | **STRENGTHENED PROVISIONAL WIN.** Fresh secondary structured reporting continues to support **8-1 = 9 corners**. | Retain historical ID |
| `P-200` | Research settled; operator endpoint unknown | **UNCHANGED — research settled.** | Retain historical ID |
| `P-217` | Research settled under revised-innings/DLS distinction | **UNCHANGED — research settled.** | Retain historical ID |
| `P-233` | Provisional win — Beijing/Lanzhou Over 8.5 corners | **STRENGTHENED ONLY, not promoted.** Current secondary structured displays support **9-4 = 13 corners**; official/field-owner corner ownership remains unresolved. | Retain historical ID |
| `P-234-C03` | Provisional win — Dalian/Shenhua Over 8.5 | **UNCHANGED/STRENGTHENED by secondary corroboration.** Disrupted-match flag remains material. | Retain historical ID |
| `P-235` | Provisional win — Shandong/Shanghai Port Over 8.5 | **UNCHANGED/STRENGTHENED by secondary corroboration.** | Retain historical ID |
| `P-274` | Research settled; operator listed-pitcher terms unknown | **UNCHANGED — research settled.** | Retain historical ID |
| `P-307` | Incomplete/no forecast issued — administrative | **UNCHANGED — non-scorable.** A final can never create a historical pick. | Retain historical ID |

### Most important historical appendix correction: P-178

The previous maximum-attempt note said the Cannes–Le Puy Under 10.5 corner field was unresolved and mentioned an unverified 8-8 candidate. Current post-final structured sources now independently expose **8 corners for Cannes and 8 for Le Puy**. The research direction can therefore be updated from `UNRESOLVED` to **`PROVISIONAL LOSS`**, while preserving the source-quality caveat.

New corroborating sources:
- https://www.leballonrond.fr/match/2026-08-29-cannes-le-puy/12276056
- https://www.forebet.com/fr/football/matches/as-cannes-le-puy-foot-2497844

### P-176 strengthening

Amiens–Versailles Under 10.5 remains a provisional/research WIN with **8 total corners**:
- https://www.apwin.com/es/partido/amiens-sc-versailles/rmhUl/
- https://www.football365.fr/direct-foot/359214/359496/amiens-sc-versailles.html
- https://www.totalcorner.com/tr/h2h/amiens-vs-versailles

### Historical appendix rule decision

No new Part-2 record gets a new ID: these are **field-status updates to existing canonical historical IDs**. The user's temporary-ID safeguard is therefore **not triggered**.

---

# 11. MINI-LOG INTEGRITY / REVISION RECORD

**Source component:** `PREDICTION_MINI_RUNNING_LOG_P344_UPDATED - Copy.md`  
**Source byte size:** `151143` bytes  
**Source line count:** `2394` physical lines (`wc -l`)  
**SHA-256:** `72ae84b77c7588b2d495b8b55a9314fd044688f057d37dd47a9bfbe22f946307`  
**First demonstrable file presence in this pass:** **2026-09-09 11:50 AEST**, from the current conversation/upload context. The mounted filesystem modification timestamp is container metadata only and is **not** used as a forecast/issuance provenance time.  
**Drive state:** READ ONLY throughout.  
**Issued forecast text:** preserved; no frozen ranks/probabilities/targets were rewritten.  
**Administrative sections updated:** top controlling snapshot, queue, chronological status.  
**Append-only evidence added:** settlement tables, Brier diagnostics, retrospectives, cross-card learning synthesis, Part-2 historical appendix refresh, source-role observations.  
**Next local continuation ID remains:** **`P-345`**, subject to required canonical Part-3 reconciliation before a new forecast under the current ledger-integrity rule.
