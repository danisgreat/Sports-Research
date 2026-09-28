# Combined prediction log 5

> **Controlling status:** all combined-log material remains **LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE**. Settlement preserves evidence; it does not make the dataset formally performance-valid. Issued records are immutable.

Status: **ACTIVE CANONICAL LOG — ALL NEW FORECASTS APPEND HERE**
Opened: **2026-09-21**, after Part 4 was closed at `P-481`.
Canonical range: **`P-482` onward**.
Next canonical ID: **`P-484`** (updated 2026-09-22, after `P-482`–`P-483` were registered and settled), subject to the normal fresh reconciliation / preflight before issue.
Current governing method at rollover: **MDS-2026.09.19-v4.3 / CR-2026.09.19-4**. Always fresh-read `METHOD.md` and the current control manifest before a new prediction rather than relying on this snapshot.
Operating mode: **SPORTS_ONLY / MARKET_BLIND**.

| Part | File | ID range | Status |
|---|---|---|---|
| 1 | `PREDICTION_LOG_COMBINED.md` | `P-001`–`P-271` | CLOSED — read/settle only |
| 2 | `PREDICTION_LOG_COMBINED_2.md` | `P-272`–`P-332` | CLOSED — read/settle only |
| 3 | `PREDICTION_LOG_COMBINED_3.md` | `P-333`–`P-423` (`P-372` reserved/unused) | CLOSED — read/settle only |
| 4 | `PREDICTION_LOG_COMBINED_4.md` | `P-424`–`P-481` | CLOSED 2026-09-21 — read/settle only |
| **5** | **`PREDICTION_LOG_COMBINED_5.md` (this file)** | **`P-482` onward** | **ACTIVE** |

## Current controlling snapshot

| Field | Current value |
|---|---|
| As of | **2026-09-22, Australia/Melbourne** — `P-482`–`P-483` registered, settled and retrospectively reviewed |
| Highest canonical prediction ID | **`P-483`** |
| Next canonical ID | **`P-484`** |
| Part-5 issued events | **2** — `P-482` (cricket, CPL 2026 Final), `P-483` (tennis, WTA Seoul R32); both **FINAL / SETTLED / RETROSPECTIVE COMPLETE** (2026-09-22) |
| Part-5 open / pending events | **None** |
| Part-5 learning-only diagnostics | Rank-1 1/2; top over/under 1/2; decisions 1 W / 2 L (forced pairs counted once); winner calls 2/2. Not a performance figure |
| Active mini log | **`PREDICTION_MINI_RUNNING_LOG_P482_ONWARD.md`** |
| Historical open handles | Continue to be tracked in `GAME_LOG_STATUS_CURRENT.md`; do not renumber or silently settle them |
| Performance status | **LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE** |
| Value status | `NO VALUE DETERMINABLE` unless the current governing value gate is explicitly satisfied |

## Mandatory continuity rules

1. Fresh-read the current governing methodology, controls, source register and relevant sport-specific rule file before every forecast.
2. Check `GAME_LOG_STATUS_CURRENT.md` and the active mini log before assigning an ID.
3. Do not reuse or renumber a canonical ID. Use a temporary ID if a collision cannot be safely reconciled.
4. Preserve the original pre-game prediction exactly after issue; settlement and retrospective material is appended, never retrofitted.
5. Keep unresolved/live events explicitly pending. Do not settle from incomplete or non-terminal data.
6. Record all material sources and field ownership. Primary/official and high-quality statistical sources take priority.
7. Rank #1 is the strongest justified selection under the governing methodology. Rank-1 failures receive enhanced retrospective scrutiny.
8. Totals, phase markets, alternate lines, lineups/bench availability, coaching, venue/weather and source-quality controls follow the current root framework and relevant sport file.
9. Sportsbook odds, betting picks, tipsters, line movement and fantasy/DFS material are not predictive evidence under the market-blind firewall.
10. After each new prediction, append the complete event to the active mini log and provide the entire updated mini log.

## Chronological issued / settled events

### 2026-09-22 — import of `P-482`–`P-483` from the P-482-onward mini log, with settlement and retrospective

Both Part-5 events to date were issued in the external running log `PREDICTION_MINI_RUNNING_LOG_P482_ONWARD.md` and are registered here for the first time. Each issued card is reproduced **verbatim**; the settlement and retrospective that follow each card are dated 2026-09-22 and identical to the settled mini log.

| Provenance field | Value |
|---|---|
| Source file | `Mini logs (to be sent to actual log later)/Mini Prediction Log - P-482 onward - 2026-09-21/PREDICTION_MINI_RUNNING_LOG_P482_ONWARD.md` |
| As-issued (pre-settlement) bytes | 45,286 bytes — SHA-256 `857413c7d2b50087ad4c71c670ed632dcd5d4c9e89e2ac4f0801e04e659557c5` — Drive file `1WgrecYGDkaYOhWPOCTXDHl9b46QjxEGr`, Drive modifiedTime 2026-09-21T03:03:36Z. Byte-exact copy: `archive/mini_logs/originals_2026-09-22/PREDICTION_MINI_RUNNING_LOG_P482_ONWARD_PRE_SETTLEMENT.md` |
| Settled variant written by this pass | 144,868 bytes — SHA-256 `6beb4b5cdaab2e31c3665331101307a56a7ebf02a71d01522f2762ed49558549` |
| Issue horizon | **P-482 — PREGAME**: final volatile refresh 2026-09-21 08:54:41 AEST (2026-09-20 22:54:41 UTC), 5 min 19 s before the scheduled start. **P-483 — PREGAME**: final refresh 2026-09-21 13:00:42 AEST (03:00:42 UTC), at the scheduled-start minute, with the WTA exact-match page, L'Equipe and MyKhel all showing the match as upcoming |
| Issued method / control revision | MDS-2026.09.19-v4.3 / **CR-2026.09.19-4** for both (issued before CR-2026.09.21-1 existed). Not retrofitted |
| Provenance basis | Genuine pregame issue recorded on each card; no live information used. A local hash is content evidence, not an independent timestamp |
| Registration timing | **Overdue** under METHOD §3 step 7: about 39 h (P-482) and 35 h (P-483) after issue against a 24-hour window. Nothing was lost — the mini log held both cards on Drive throughout — but this log's snapshot was stale until this pass |
| Pre-write integrity check | Two IDs, each used once; no collision with `P-001`–`P-481`; no duplicate events (the CPL Final, ESPN event 1534217, is distinct from P-445's Eliminator, event 1534214); no temporary IDs; both events **FINAL**, each passing the three-lineage terminal-state gate with four independent lineages |
| Eligibility | **LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE** |

**Cohort summary (learning-only diagnostics; forced pairs counted once in decisions).**

| ID | Event | Result | Rank-1 | Hit@2 | Wins@2 | NDCG@2 | Decisions | Top O/U | Winner call | Grade (G37) |
|---|---|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|---|
| P-482 | CPL 2026 Final — Falcons v Kingsmen | Jamaica 170/9, Falcons 173/2 (16.4) — Falcons by 8 wkts; **Jamaica 59/2 after six** | **W** | YES (mechanical) | 1/2 | 1.000 | 1 W / 0 L (Brier 0.1608) | W | **W** (0.2209) | Result-right / process-different |
| P-483 | WTA Seoul R32 — Volynets v Kalieva | **Volynets 6-3, 6-0** — 15 games, +9 | **L** | NO | 0/2 | 0.000 | 0 W / 2 L (Brier 0.4251, 0.3411) | **L** (`TOP_OU_REVIEW`) | **W** (0.1444) | Result-wrong / process-wrong in part |

Decisions 1 W / 2 L; decision Brier 0.3090 across targets, 0.2719 event-weighted; winner calls 2 of 2 (mean Brier 0.1826). The 3 W / 3 L row record is mechanical — all six rows are halves of forced pairs — and is not a performance figure.


> **P-482 — SETTLED 2026-09-22 / RETROSPECTIVE COMPLETE.** Jamaica Kingsmen 170/9 (20) lost to Antigua & Barbuda Falcons 173/2 (16.4) by 8 wickets. **Jamaica after six legal overs: 59/2.** Rank #1 Over 47.5 **WIN**; Rank #2 Under 47.5 **LOSS**; projected winner Falcons **WIN**. G37 grade: **RESULT-RIGHT / PROCESS-DIFFERENT** — the Over won through the mechanism the card named (Maaz Sadaqat), but the evidence that sized it came from chase powerplays and Jamaica batted first.
>
> The issued card below is preserved **verbatim**, including its as-issued "UNSETTLED" status line. Settlement and retrospective follow the card.

### P-482 — Cricket / Republic Bank CPL 2026 Final — Antigua & Barbuda Falcons vs Jamaica Kingsmen

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

#### P-482 — Settlement (2026-09-22)

**Event state at settlement check (2026-09-22 ≈ 23:45 AEST / 13:45 UTC): COMPLETED.** Full 20-over innings for both sides. No rain stoppage, DLS revision, reduction or abandonment appears in any source. Explicit terminal marker present.

**Terminal-state gate — four independent lineages agree on event, date, final and the settling field.**

| Lineage | Source (opened) | Terminal marker | Fields confirmed |
|---|---|---|---|
| L1 — ESPN / ESPNcricinfo structured record (data partner; ESPN and ESPNcricinfo variants are one lineage) | `https://site.web.api.espn.com/apis/site/v2/sports/cricket/8623/summary?event=1534217`; ball-by-ball `…/playbyplay?event=1534217&period=1&page=1` and `&page=2` | "Antigua and Barbuda Falcons won the 2026 Caribbean Premier League" | Toss: "Antigua and Barbuda Falcons, elected to field first". Jamaica innings: `Powerplay 1: Overs 0.1 - 6.0 (Mandatory - 59 runs, 2 wickets)`; "Jamaica Kingsmen: 50 runs in 5.1 overs (31 balls), Extras 4"; "Innings Break: Jamaica Kingsmen - 170/9 in 20.0 overs". Falcons innings: `Powerplay 1 … (Mandatory - 76 runs, 1 wicket)`. Over-end checkpoints: 7/1 (1.0), 31/2 (4.0), **59/2 (6.0, run rate 9.83)**, 63/2 (7.0) |
| L2 — CPL official (competition owner) | CPL Newsroom, *Falcons Complete Dream Flight to Maiden Title* — `https://cplt20.prezly.com/falcons-complete-dream-flight-to-maiden-title`. Its release text is reproduced verbatim by CaribbeanCricket.com and CricTracker ("The Kingsmen ended the Power Play on 59 for 2, just one run short of the landmark ten runs an over") — **counted once** | "won by 8 wickets", maiden CPL title | 170/9; 173/2 with 20 balls to spare; Moqim 4-14; Falcons 76/1 after six |
| L3 — Nation News (Barbados), independent reporting | `https://nationnews.com/2026/09/21/moqims-historic-haul-carries-falcons-to-maiden-cpl-title/` | "won by eight wickets" | Kingsmen sent in; McKenzie c Cornwall (first slip) b Seales, 0, first over; Carty c Shadab b Joseph "to make the score 30 for two" (ball 3.4); Sadaqat 114 (58; 8×4, 9×6); Moqim 4-14; Joseph 2-27; Falcons 173/2 in 16.4 |
| L4 — WIC News, independent reporting | `https://wicnews.com/antigua-barbuda/antigua-and-barbuda-falcons-make-history-clinch-maiden-cpl-title-with-dominant-win-over-jamaica` | victory "in 16.4 overs" | "After winning the toss and electing to bowl…"; Sadaqat "helped Jamaica reach 59 for two at the end of the Powerplay"; collapse "from 110 for two to 113 for six" |
| Further corroboration | Jamaica Gleaner (`https://jamaica-gleaner.com/article/sports/20260922/kingsmen-lose-cpl-final-falcons-8-wickets`); Times of Sports ("59 runs in the powerplay"); Dawn (`https://www.dawn.com/news/2031582`); Crex scorecard (toss, player of the match, Russell 0/30 in 2.4 overs) | — | — |

**Gate: PASS.** No live or in-progress source; no material conflict. One secondary summary described Sadaqat as "100 not out"; 100 was his 49-ball milestone, and the scorecard lineages give 114 off 58, caught off the penultimate ball. Player-level fields are taken from scorecard lineages (P-479 precedent).

**Exact settlement record.**

- **Toss:** Falcons won and chose to field → **Jamaica batted first.**
- **Jamaica's first six legal overs** (runs include extras): 7/1 after 1.0 (McKenzie 0 off 4, c Cornwall b Seales, ball 0.6) → 30/2 at 3.4 (Carty 9 off 8, c Shadab b Joseph) → 31/2 after 4.0 → 46/2 after 5.0 (derived: 59 minus the 13-run sixth over) → 50/2 at 5.1 (31 balls, 4 extras) → **59/2 after 6.0**. Batters at the end of the phase: Maaz Sadaqat and Saim Ayub. Sixth over, per the ESPN ball-by-ball feed as retrieved (bowler shown as Alzarri Joseph; single retrieval, not cross-checked): 4 (Sadaqat), 0, 1, 6 (Ayub), 1, 1.
- **Rest of the Jamaica innings:** 110/2 → 113/6 inside twelve balls — Moqim removed Saim Ayub (29 off 22) and Rovman Powell (0) in one over; Romaine Morris lbw b Shadab 0; Hassan Khan 1. Sadaqat 114 off 58 (fifty off 27 balls; hundred off 49 — the first century in a CPL final), caught by Springer at long-off off the penultimate ball. **Jamaica 170/9 (20).**
- **Falcons chase:** Cornwall 20 in the first over, then bowled; 76/1 after six; Evin Lewis 38 (26), reprieved by an Andre Russell no-ball, later b Lawes; Amir Jangoo 57* (34) and Hasan Nawaz 47* (35) added an unbroken 89. **Falcons 173/2 (16.4) — won by 8 wickets with 20 balls remaining.**
- **Awards:** Sufyan Moqim player of the match (4-14, the best figures in a CPL final); Shadab Khan player of the tournament.
- **Participant note:** Andre Russell played and bowled 2.4 overs (0/30). He had no role in the Jamaica powerplay.

**Contract settlement.**

| Rank | Issued contract | Issued p (`UNVALIDATED_SUBJECTIVE`) | Realised | Research endpoint | Operator settlement | Row Brier |
|---:|---|---:|---|---|---|---:|
| 1 | Kingsmen first 6 legal overs **OVER 47.5** | 0.599 | 59 | **WIN** (by 11.5) | WIN | 0.1608 |
| 2 | Kingsmen first 6 legal overs **UNDER 47.5** | 0.401 | 59 | **LOSS** | LOSS | 0.1608 |
| Winner | **Antigua & Barbuda Falcons** | ≈ 0.53 | Falcons by 8 wickets | **WIN** | — | 0.2209 |

**Settlement ambiguity: none material.** The operator's rain/DLS/abandonment terms were never supplied and the card correctly did not invent them. No interruption occurred and all 36 legal balls of the phase were bowled, so every standard action rule gives the same settlement. The matchnote counts legal deliveries (overs 0.1–6.0) and includes extras, which is the contract's unit.

**Top-of-list diagnostics.**

| Metric | Value | Note |
|---|---|---|
| Rank-1 | **WIN** | |
| Hit@2 | **YES** | Mechanical: a half-line forced pair always has exactly one winner once active |
| Wins@2 | **1 / 2** | The maximum possible for a forced pair |
| Both top two won | **Not possible** | `FORCED_PAIR` |
| NDCG@2 | **1.000** | Binary relevance; the slate holds exactly one winner, so IDCG@2 = 1.0 (P-474 convention) |
| Decision score (`SCORING_AND_VALIDATION.md` §3; forced pair counted once) | 1 decision — **WIN** — Brier **0.1608** | |
| Top over/under | Over 47.5 (= Rank #1) — **WIN** | `TOP_OU_REVIEW` not triggered |
| Winner call | **WIN** — Falcons, p ≈ 0.53, Brier 0.2209 | |

**Distribution check — recomputed from the frozen card.** The mixture reproduces exactly: mean 51.75, SD 14.43, P(>47.5) = 0.5986. The realised 59 sits inside the card's central 50% corridor (41–62), at a PIT of about 0.68. Posterior component weights at 59: breakaway 0.52, central 0.47, early-wicket suppression 0.01. That last figure is the interesting one. The realised path **contained the suppression component's trigger** (two wickets inside 3.4 overs) and still finished in breakaway territory — a state the mixture did not represent, because it tied "early wicket" to "low runs" inside a single component. The published SHA-256 of `P-482-PP6-dist-v1` cannot be re-derived because its serialisation was not preserved; the parameters themselves reproduce.

**Process grade (G37): RESULT-RIGHT / PROCESS-DIFFERENT.** Reasoning in C below.

#### P-482 — Retrospective (2026-09-22)

##### A. Prediction outcome

- **Pick #1 — Over 47.5:** WIN (59/2).
- **Pick #2 — Under 47.5:** LOSS (forced complement).
- **Remaining ranked picks:** none; the supplied slate was one forced pair.
- **Over/under market:** the only target was a phase total; its preferred side won.
- **Projected winner — Falcons:** WIN.
- **Overall:** one of one decision correct; winner correct; process incomplete in the variable that mattered most for this line.

##### B. Why each pick won or lost

**Pick #1 — Over 47.5 — WIN.**

- *What happened.* Jamaica lost McKenzie to the last ball of the first over (7/1) and Carty to the fourth ball of the fourth (30/2). That is the first half of the card's named failure path: "Sadaqat or McKenzie is removed in the first 1-2 overs". The second half — the Falcons "push Jamaica into a 30s/low-40s phase" — never arrived. Sadaqat survived, Saim Ayub came in at No. 4, and the last fourteen balls of the phase produced 29 runs, including a 13-run sixth over with a Sadaqat four and an Ayub six.
- *Why it won.* The card's central thesis — Sadaqat's current-role boundary threat — was the operative mechanism; he went on to 114 off 58. The two early wickets did not compress boundary access because the dismissed batters were the two non-dominant ones and the incoming batter was another attacking top-order player.
- *Assumptions that held.* Sadaqat and McKenzie opened. Sadaqat was the upside driver. The 7 Aug H2H was rightly discounted: different openers, and 28 of its 54 runs came in one over off Karima Gore. Russell was carried as an availability branch rather than a fact; he played and bowled, and had no bearing on the phase. The LOW evidence cap was appropriate.
- *Assumptions that failed or were never tested.*
  1. The breakaway component (weight 0.35, centre 65) was sized from "the two immediately preceding knockout chases" — 79/0 on 16 Sep and 75/1 on 18 Sep. **Both were chase powerplays** (ESPN: Jamaica fielded first in both). Jamaica batted first in the final, and the card carried no innings-order split.
  2. The suppression component assumed an opener's dismissal compresses boundary access. Two early wickets did not, because the dominant hitter survived.
  3. The card's new-ball threat list ("Alzarri/Joshua James/Shamar Springer-type") did not name Jayden Seales, who opened the bowling and struck in the first over. Saim Ayub, Jamaica's No. 4, is not on the card at all.
- *Driver classification.* A predictable factor (dominant-hitter form, correctly identified), plus favourable variance in *which* batters fell, an information gap (innings order / toss) and a model weakness (wicket→runs coupling inside one component).
- *Weighting.* The most important factor, Sadaqat, was central — correctly. Innings order was not weighted at all.

**Pick #2 — Under 47.5 — LOSS (forced complement).**

Its live path was real and half-realised: 31/2 after four overs is an Under-trajectory state, and the card's 46/2 precedent (4 Sep) was genuine. It failed because 28 runs came in overs five and six. As a forced complement it carries no independent information (`SCORING_AND_VALIDATION.md` §3).

**Projected winner — Antigua & Barbuda Falcons (≈ 53%) — WIN.**

- The card's stated support operated. "Deeper/balanced bowling resources": Seales and Joseph took the new-ball wickets, and Moqim's 4-14 turned 110/2 into 113/6 inside twelve balls. The 7 Aug H2H pattern — Jamaica around 170 batting first, Falcons chasing it down — repeated almost exactly.
- The named failure path ("Jamaica's top order carries its current Kensington form into another chase/innings") fired for one batter only. Sadaqat made 114; Saim Ayub (29) was the only other batter to reach double figures.
- Not on the card: post-toss innings-order context. In every Kensington match from 12 to 18 Sep (ESPN events 1534212–1534216) the toss winner chose to field and the chasing side won — 5 of 5; the final made it 6 of 6. Under `RULES_CRICKET.md` §2.8 and control 5 that is circumstantial context, not a directional rule, and six matches at one venue in one fortnight is not a base rate. Recorded as an observation only.
- 53% was a close call and the result was decisive. One event says nothing about the size of the 53%.

##### C. Rank-1 review — a win, audited under METHOD §7 ("inspect wins as well as losses")

The enhanced failure review is **not triggered**: Rank #1 is also the top over/under, and it won. The same questions are still asked, because a Rank-1 win can hide a process that did not justify the rank.

1. **Why it ranked first.** It was the preferred side of the only supplied target, at 59.9% from the frozen mixture.
2. **Was the placement justified by information available before issue?** Only in part. The card's own evidence, re-sorted by innings order and re-verified at the ESPN matchnotes, together with the venue window the card did not print:

| Evidence set | Six-over powerplays | Mean | Cleared 47.5 |
|---|---|---:|---:|
| Jamaica batting first — the checkpoints on the card | 54/1 (7 Aug, Arnos Vale; different openers), 46/2 (4 Sep, Providence), 50/1 (12 Sep, Kensington) | 50.0 | 2 of 3 |
| Jamaica chasing — the two knockout chases that sized the breakaway component | 79/0 (16 Sep, Kensington), 75/1 (18 Sep, Kensington) | 77.0 | 2 of 2 |
| Kensington Oval, all teams batting first, 12–18 Sep (not on the card) | 50/1, 30/3, 24/4, 34/1, 37/2 | 35.0 | 1 of 5 |
| Kensington Oval, all teams chasing, 12–18 Sep (not on the card) | 36/3, 33/2, 79/0, 77/1\*, 75/1 | 60.0 | 3 of 5 |

\* Target-censored: the Falcons needed 77 in Qualifier 1.

The line sat on Jamaica's own batting-first mean and far above the venue's batting-first mean. The 65-centre breakaway component was built from the chasing row. A pre-toss card that split the phase by innings order would have carried two branches with very different chances of clearing 47.5. A post-toss card would have used the batting-first branch alone.

3. **Should the other row have ranked higher?** Possibly. On the batting-first evidence alone, 47.5 is close to a coin flip, and the venue's batting-first record points the other way. Unless Sadaqat's current form had been given an explicit, named upward effect — which was the card's thesis and turned out to be the realised mechanism — a compliant process could have preferred the Under and **lost**. The honest reading: this Rank-1 win owes more to Sadaqat than to the process that sized its probability. It must not be read as validating a chase-anchored breakaway component.
4. **Variable missed or mis-weighted.** Innings order, and therefore the toss. Secondary: the incoming No. 4 and the opponent's actual new-ball pair (phase participants).
5. **Did an existing control cover it, and was it executed?** Yes, several; mostly not executed.
   - `RULES_CRICKET.md` §10.5 kill path **"Chasing-side powerplay inflation — a first-innings-anchored phase read applied to the chase"**. This card made the same error in reverse: a chase-anchored read applied to a first innings. Not applied.
   - The P-445 settlement (`PREDICTION_LOG_COMBINED_4.md`; cricket control 32) recorded, **for this same team**, that "Jamaica chase powerplay was 79/0 against a batting-first sample whose mean was 43.5". The warning was on file four days before issue. Not applied.
   - §10.8 requires the venue window "at this exact venue in this format … by innings order" (rung 6, mandatory). Not printed; the card used Kensington only as "dispersion evidence".
   - Control 32 / `G-L14`: "Where the toss is retrievable before the freeze it must be retrieved." CPL tosses fall roughly 30 minutes before the first ball (P-445 note), about 08:30 AEST here; the final refresh was at 08:54:41 AEST. The registered ESPN summary route carries the toss note, and the CPL 2026 series has been in `DATA_SOURCE_REGISTER.md` since P-217. **Probable `RETRIEVAL_MISS`.** The exact publication minute of the toss note is not independently proven, so this is recorded as probable, not certain.
   - Control 22 (near-start identity gaps cap evidence at LOW) — executed correctly.

   This is the `M15` pattern (control listed, not executed) plus an `M19`-type retrieval miss.
6. **Is a new rule warranted?** A construction and disclosure rule, not a coefficient: **model a phase total as an explicit batting-first / chasing mixture before the toss, or on the realised branch after it, with the team and venue windows split the same way.** Control 21 already requires this for innings totals but says nothing about phase totals. Evidence now spans three events — ETPL 2026 Match 15 (Dublin 69/1 chasing v Amsterdam 60/1 setting), P-445 and P-482 — with a clear mechanism (target knowledge, night conditions, the toss-winner's choice). Proposed as **R-1** in §4.3.

##### D. Top-two review

- Pick #1 won; at least one of the top two won; both could not win (forced pair).
- Ordering: the right side, with an overstated margin (see C).
- For a forced pair, Hit@2 is guaranteed and says nothing about skill. The informative quantities are the one decision (WIN) and its Brier (0.1608).
- Improvement for future top-two reliability: condition the phase distribution on innings order before any line is queried. The rest of the top-two construction was sound.

##### E. Over/under review — phase total

| Factor | Card's treatment | What the record shows | Assessment |
|---|---|---|---|
| Scoring environment | Kensington used only as "dispersion evidence" | Final-week Kensington powerplays split sharply by innings order: batting-first mean 35.0, chasing mean 60.0 (n = 5 each); toss winners fielded 6 of 6 | Material, available before issue, not used |
| Pace / tempo | Current-regime checkpoints listed individually, with wickets (L-083 executed) | The realised 59 beat all three of Jamaica's batting-first checkpoints (54, 46, 50) | Right direction via Sadaqat; magnitude evidence chase-inflated |
| Offensive efficiency | Sadaqat / McKenzie form | Sadaqat decisive; McKenzie 0; Ayub (not listed) contributed | Phase-participant map incomplete (No. 4) |
| Defensive efficiency | "Alzarri/Joshua James/Shamar Springer-type new-ball pressure" | Seales and Joseph opened and each took a powerplay wicket; the Falcons had held Guyana to 34/1 in Qualifier 1 and Jamaica to 26 through five overs on 7 Aug | Opponent powerplay concession not quantified |
| Venue / conditions | Warm, humid, no rain; strip `NOT_VERIFIED` | No interruption; one secondary source (Crex) says dew helped the chase — unverified | Weather correctly treated as variance only |
| Lineups / absences | Toss and XIs unresolved; LOW cap | Jamaica's top four matched a probable XI published about 21 hours before the start; the toss happened about 25 minutes before the final refresh | Probable retrieval miss |
| Line position | 47.5 queried after the freeze; +4.25 runs, +0.29 SD | The line sat on Jamaica's batting-first mean and far above the venue's batting-first mean | A highly state-sensitive line |
| Distribution around the line | SD 14.4; central 50% 41–62 | 59 at PIT ≈ 0.68 | The width was honest |
| Variance sensitivity | 28-run sixth over in the H2H noted | One 13-run over carried the final from 46 to 59 | Very high: single overs swing 13–28 runs |
| Sport-specific indicators | Runs with wickets (✓); H2H continuity (✓); streak control 24 (✓) | Missing: venue window by innings order; competition-level phase population (P-300 requirement 4); opponent phase concession; phase map for Nos. 3–4 and both new-ball bowlers | Incomplete |

**Verdict.** The preferred side was right. The process that sized it was incomplete in exactly the variable that mattered most for this line. The fix is analytic — split by innings order — not directional. No rule that nudges phase totals Over or Under is justified.

##### F. What went right — keep these

1. **Contract identity.** "Jamaica runs after the first six legal overs of their innings" does not depend on innings order, so the row activated whatever the toss. Correctly parsed; no P-445-style NO ACTION risk.
2. **Line quarantine and freeze.** The distribution was frozen and hashed before 47.5 was queried, and its arithmetic reproduces exactly.
3. **Every factual checkpoint was right.** 54/1, 46/2, 50/1, 79/0 and 75/1 all match the ESPN matchnotes.
4. **The operative mechanism was on the card.** Sadaqat's current-role boundary threat was the stated main support and it decided the phase.
5. **Continuity discipline.** The 7 Aug H2H was discounted for changed openers and a one-over spike (control 20); the 79/0 and 75/1 were explicitly "not a self-perpetuating streak" (control 24).
6. **An honest evidence grade.** LOW under control 22, because toss, XI and strip were unresolved.
7. **Availability handling.** Russell was kept as a branch. He played. No absence was invented.
8. **Winner reasoning.** Bowling depth was the stated edge, and it decided the match.
9. **Settlement route.** The registered ESPN matchnote (cricket control 29) settled the phase field on the first query.

##### G. Blind spots

| # | Blind spot | Available before issue? | How much it mattered | Future handling | Rule or observation |
|---|---|---|---|---|---|
| 1 | Innings order / toss not retrieved | Probably (toss ≈ 08:30 AEST; final refresh 08:54) | High for the probability; none for the outcome | Toss-window refresh under CR-2026.09.21-1 (now in force); query the ESPN summary `notes[]` toss line at toss + 5 minutes | Existing rule — execution |
| 2 | Phase evidence not split by innings order | Yes — all on ESPN | High | R-1 (§4.3) | Rule candidate, three events |
| 3 | Venue window by innings order not printed | Yes (five ESPN calls) | High | §10.8 rung 6 is mandatory — print it with n | Existing rule — execution |
| 4 | Probable XI unused: Saim Ayub (No. 4) absent; Seales not named | A probable XI was public ≈ 21 h before the start | Moderate | Print the probable XI as `PROJECTED`; name Nos. 3–4 and both new-ball bowlers in the phase map (control 20) | Existing rule — execution |
| 5 | Early-wicket component keyed to wicket count, not to who is dismissed | Partly (the concentration of Jamaica's scoring in Sadaqat was visible) | Moderate | Tentative: key the collapse branch to the dominant hitter's survival | Observation (n = 1; P-300 is a counter-example) |
| 6 | Opponent powerplay concession not quantified | Yes | Moderate | Print the opponent's phase-conceded windows (§10.8 bowling window) | Existing rule — execution |
| 7 | Competition-level phase population not printed | Yes | Low to moderate | P-300 requirement 4 already asks for it | Existing rule — execution |
| 8 | Night / dew chase context | Weakly | Low (winner only) | Record as conditions context only when a primary source reports it | Observation |
| — | *Not blind spots:* McKenzie's first-over dismissal; Sadaqat's late-phase burst | Hindsight only | — | — | — |

##### Mandatory validation questions

1. **Were confirmed starting lineups obtained for both teams?** **No.** Neither XI was confirmed at issue. A probable Jamaica XI was public (Yahoo Sports preview, 20 Sep 11:30 UTC: Sadaqat, McKenzie, Carty, Saim Ayub, Powell, Russell, Hassan Khan, Morris, Keemo Paul, Lawes, Hunain Shah), and its top four matched the actual order. The Falcons' new-ball pair included Jayden Seales, who was not in that preview's XI (it listed Fabian Allen). Confirmed XIs appear at the toss, which preceded the final refresh — a probable `RETRIEVAL_MISS`.
2. **Were bench / reserve / substitute lineups obtained where relevant?** Not recorded. Not material to a six-over batting phase.
3. **Was coaching / manager information obtained where material?** Not recorded. The one captaincy decision that mattered — the Falcons choosing to field — is the toss, covered in Q1.
4. **Were injuries, suspensions, rest decisions and late withdrawals adequately checked?** Yes. Russell, the one fitness concern, played and bowled 2.4 overs; the card kept him as a branch. No late withdrawals were found.
5. **Were the original sources accurate and current?** Accurate: all five phase checkpoints and the H2H mechanism verify. The official pages used for event state (CWI, Wisden) were right that play had not begun but do not carry the toss — reliable for state, blind for the toss.
6. **Were better sources available?** Yes. The ESPN cricket summary route (T4 in the toss ladder; registered) carries the toss, innings order and per-innings powerplay matchnotes for every CPL match. About six calls would have supplied the toss and the Kensington innings-order window.
7. **Were there blind spots?** Yes — table G.
8. **How should they be handled in future?** Retrieve the toss at the toss window (now mandatory). Split phase evidence by innings order. Print the venue window by innings order and the opponent's phase concession. Name Nos. 3–4 and both new-ball bowlers.

##### Connection to earlier learnings

| Earlier lesson or rule | Relationship to P-482 | Status |
|---|---|---|
| P-445 settlement; cricket control 32 ("79/0 chase v batting-first sample mean 43.5" — same team) | Described this exact contamination four days earlier | **Not applied — recurrence** |
| §10.5 kill path "Chasing-side powerplay inflation" (ETPL 2026 Match 15) | Same mechanism, reverse direction | Not applied |
| L-083 / P-300 (retrieve wickets with runs; name the collapse branch) | Executed: every checkpoint carried its wickets; the collapse branch was weighted 0.25 | **Working** |
| Control 20 (phase participants outrank phase H2H) | Executed for the H2H; not for Nos. 3–4 or the new-ball pair | Partial |
| Control 24 / `R-1` (no self-perpetuating streak) | Executed | Working |
| Control 22 (LOW cap for near-start identity gaps) | Executed | Working |
| Control 29 / `G-L14` (phase settlement route) | Worked on the first query | Working |
| `AUDIT_AND_CRICKET_SOURCE_UPDATE_2026-09-21.md` §1.2 D (named this card's toss/XI/strip latency) → CR-2026.09.21-1 toss-window refresh | The settlement shows the gap mattered for the probability, not for the outcome | Fix already in force for new cards |
| P-474 mini log R-D (toss as an activation gate) | Extended: even an innings-agnostic contract needs the toss, because innings order changes the distribution | Extension |
| `M15` / `M19` | Both recur | Cross-sport recurring |

**Classification.** Innings-order contamination of phase evidence is a **sport-specific recurring pattern** (ETPL Match 15, P-445, P-482) and a **strong rule candidate**. The `M15` execution gap is **cross-sport and recurring** (§4). The wicket-count versus dominant-hitter point is **tentative, n = 1**.

##### Source audit

| Source | Used for | Accurate? | Current? | Authority | Future use |
|---|---|---|---|---|---|
| Cricket West Indies fixtures / home page | Identity, venue, 19:00 AST, pre-start state | Yes | Yes for state; carries no toss | Field owner (schedule) | Keep for identity and state; never for the toss |
| CPL Newsroom (prezly) | Phase facts (50/1; the Eliminator; Qualifier 2); H2H mechanism | Yes — all verified | Post-match publication | Competition owner | Keep — primary match narrative |
| Jamaica Gleaner / CMC | Lineup expectation; Russell monitoring; Qualifier 2 opening burst | Yes | Yes | Reputable media | Keep — secondary |
| Wisden fixture front | Independent pre-start state | Yes | Yes | Secondary | Keep for event state |
| CricInnings 4 Sep scorecard | 46/2 checkpoint | Yes (ESPN confirms) | — | Secondary structured | Fallback; prefer ESPN |
| Structured Bridgetown weather | Conditions | No contradiction | Yes | — | Keep |
| **ESPN cricket API** — `site.web.api.espn.com/apis/site/v2/sports/cricket/8623/summary?event=<id>` and `…/playbyplay?event=<id>&period=<innings>&page=<n>` | Settlement: toss, innings order, powerplay matchnotes, milestones, over-end checkpoints; the whole Kensington window | Yes | Updates in-match | Data partner; one lineage with ESPNcricinfo | **Make it the first call for toss, innings order and phase fields.** 8623 is ESPN's league ID — an alternative path to the series-ID route already registered (1534175) |
| Nation News (Barbados) | Settlement corroboration; ball-level narrative (30/2 at 3.4) | Yes | Next day | Independent reputable media | Add as an independent Caribbean lineage |
| WIC News | Toss decision; 59/2; collapse | Yes | Next day | Independent media | Secondary |
| CaribbeanCricket.com, CricTracker | CPL release reproduced verbatim | Yes | — | **Same lineage as CPL** | Count once, never as independent confirmation |
| Crex | Toss, player of the match, Russell's figures; dew remark | Figures consistent; dew remark unverified | — | Aggregator | Fallback only |
| Yahoo Sports preview | Probable XIs before the match | Top four right; Falcons attack partly wrong | ≈ 21 h before start | Projected, not confirmed | `PROJECTED` class only |
| ESPNcricinfo HTML pages | — | — | HTTP 403 to automated fetch in this pass | — | Use the API route |

No source is promoted on the strength of this one result. The ESPN route is recommended because it is the field-owning data partner's structured record and has now settled phase fields on P-406, P-445, P-479 and P-482.

##### Event-specific learnings

1. Split every phase-total evidence window by innings order before it sizes a component. Before the toss, carry both branches; after it, use the realised one (R-1).
2. Retrieve the toss at the toss window from the ESPN summary `notes[]` line. The CR-2026.09.21-1 refresh exists for exactly this.
3. Print the venue window by innings order, with n, as §10.8 already requires.
4. Name the incoming Nos. 3–4 and both new-ball bowlers in the phase-participant map.
5. Tentative: define the collapse branch by the dominant hitter's dismissal rather than by wicket count (n = 1; P-300 is a counter-example, where a wicket cluster did suppress the phase).
6. A Rank-1 win reached through the right mechanism but sized on the wrong evidence is graded **process-different**, not process-right.

Document destinations for each of these are in §5.

---

> **P-483 — SETTLED 2026-09-22 / RETROSPECTIVE COMPLETE (ENHANCED).** Katie Volynets d. Elvina Kalieva **6-3, 6-0** — 15 games, Volynets +9. Rank #1 Over 19.5 **LOSS** (also the top over/under → `TOP_OU_REVIEW`); Rank #2 Kalieva +4.5 **LOSS**; Rank #3 Volynets −4.5 **WIN**; Rank #4 Under 19.5 **WIN**; projected winner Volynets **WIN**. G37 grade: **RESULT-WRONG / PROCESS-WRONG IN PART** — existing tennis controls that bear on favourite strength and hold rates were not executed, which tilted the score tree toward a close match; the Rank-1 direction itself is not shown to be wrong.
>
> The issued card below is preserved **verbatim**, including its as-issued "UNSETTLED" status line. Settlement and the enhanced retrospective follow the card.

### P-483 — Tennis / WTA Seoul — Katie Volynets vs Elvina Kalieva

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

#### P-483 — Settlement (2026-09-22)

**Event state at settlement check (2026-09-22 ≈ 23:50 AEST / 13:50 UTC): COMPLETED.** The match finished normally in 1 h 12 min — about 14:12 AEST on 21 Sep if it began at the scheduled 12:00 KST. No retirement, walkover or medical time-out appears in any source checked.

**Terminal-state gate — four independent lineages agree on event, date, final status and score.**

| Lineage | Source (opened) | Terminal marker | Fields confirmed |
|---|---|---|---|
| L1 — WTA (field owner) | Exact-match page `https://www.wtatennis.com/tournaments/1024/seoul/2026/scores/LS029`, plus the official main-draw PDF `https://wtafiles.wtatennis.com/pdf/draws/2026/1024/MDS.pdf` (released "21 Sep 2026 10:35 PM": "K. Volynets 63 60") — two artefacts, one lineage | "Finished" | 6-3, 6-0; 1 h 12 min; full match statistics (below) |
| L2 — Tennis Majors | `https://www.tennismajors.com/matches/wta/korea-open-2026-women-s-singles/katie-volynets-vs-elvina-kalieva` | "Ended" | 6-3, 6-0; 21 Sep 2026; 1 h 12 min; no retirement noted |
| L3 — TennisTemple | `https://en.tennistemple.com/match/volynets-kalieva-seoul-2026/9482014/` | "Completed" | Volynets 6-3 6-0; Show Court 1; about 1 h 11 min |
| L4 — Canal Tenis draw article | `https://canaltenis.com/cuadro-wta-seul-2026/` | Result line | "Katie Volynets (USA) vs Elvina Kalieva (USA) 6-3, 6-0" |
| Onward corroboration | Tennis Majors Round-of-16 page, Kamilla Rakhimova vs Katie Volynets | — | Volynets advanced |

**Gate: PASS.** No live source, no conflict. (A Sofascore page displayed an ambiguous set counter; it was not used.)

**Exact settlement record.**

- WTA 250 Korea Open, Round of 32, Seoul Olympic Park Tennis Center, outdoor hard, 21 Sep 2026, scheduled 12:00 KST (13:00 AEST).
- **Score: Volynets 6-3, 6-0.** Games: Volynets 12, Kalieva 3 → **total 15; Volynets aggregate margin +9.** Sets 2-0.
- Service record, derived from the score and the break-point fields: Volynets served 8 games and held all 8, **facing no break point**. Kalieva served 7 and held 3, saving 5 of 9 break points.

| Field (WTA exact-match page) | Volynets — this match | Volynets — 2026, as printed on the card | Kalieva — this match | Kalieva — 2026, as printed on the card |
|---|---|---|---|---|
| First serves in | 82.9% (34/41) | 73.9% | 47.8% (22/46) | 58.6% |
| First-serve points won | 76.5% (26/34) | 58.2% | 68.2% (15/22) | 64.5% |
| Second-serve points won | 85.7% (6/7) | 44.2% | 29.2% (7/24) | 44.1% |
| Aces / double faults | 1 / 0 | 40 / 40 in 270 service games | 0 / 4 | 48 / 56 in 126 service games |
| Service games held | 8 of 8 | 58.9% | 3 of 7 | 62.7% |
| Break points | converted 4 of 9 | — | saved 5 of 9 | 52.5% saved |
| Total points won | 56 of 87 (64.4%) | — | 31 of 87 (35.6%) | — |

(WTA's "service games won" field shows 8 and 7, which are games served; the holds above follow from the score and from Volynets facing no break point.)

**Contract settlement.**

| Rank | Issued contract | Issued p (`UNVALIDATED_SUBJECTIVE`) | Realised | Research endpoint | Operator settlement | Row Brier |
|---:|---|---:|---|---|---|---:|
| 1 | **TOTAL GAMES OVER 19.5** | 0.652 | 15 | **LOSS** (by 4.5) | LOSS | 0.4251 |
| 2 | **KALIEVA +4.5 GAMES** | 0.584 | 3 + 4.5 = 7.5 v 12 | **LOSS** | LOSS | 0.3411 |
| 3 | **VOLYNETS −4.5 GAMES** | 0.416 | 12 − 4.5 = 7.5 v 3 | **WIN** | WIN | 0.3411 |
| 4 | **TOTAL GAMES UNDER 19.5** | 0.348 | 15 | **WIN** | WIN | 0.4251 |
| Winner | **Katie Volynets** | ≈ 0.62 | won 2-0 | **WIN** | — | 0.1444 |

**Settlement ambiguity: none.** Operator retirement/walkover terms were `UNKNOWN_DEFINITION` at issue. The match finished normally, so every standard rule settles identically. Half-game lines: no pushes.

**Top-of-list diagnostics.**

| Metric | Value | Note |
|---|---|---|
| Rank-1 | **LOSS** | |
| Hit@2 | **NO** | |
| Wins@2 | **0 / 2** | |
| Both top two won | **NO** — both lost in the same state | |
| NDCG@2 | **0.000** | The slate holds two winners (Ranks 3 and 4), so IDCG@2 = 1.6309; DCG@2 = 0 |
| Decision score (two `FORCED_PAIR` targets, preferred sides counted once) | **0 W / 2 L** — Brier 0.4251 (total) and 0.3411 (handicap); event mean **0.3831** | |
| Top over/under | Over 19.5 (= Rank #1) — **LOSS** | **`TOP_OU_REVIEW` fired.** One enhanced review below covers both triggers |
| Rank #2 loss | Yes | Deep review required (`EXTERNAL_LOGGING_WORKFLOW.md` §0.4) |
| Both total rows on the wrong side | Yes — Over ranked #1, Under #4; Under won | Deep review required |
| Winner call | **WIN** — p ≈ 0.62, Brier 0.1444 | |

**Distribution check — recomputed from the frozen card.** The six-branch tree reproduces at representative-score level: weighted total 23.1 games and Volynets margin +1.66, as printed. The representative Over mass is 64% (card: 65.2% after its within-branch spread) and the representative Kalieva +4.5 mass is 70% (card: 58.4%). The realised 6-3, 6-0 belongs to the card's "Volynets decisive 2-0" family (weight 30%, representative 6-3, 6-3 = 18 games), below its representative score; a love set sits in that family's lower tail. **The card printed no within-branch spread or interval for total games or margin, so P(total ≤ 15) and a PIT value cannot be reproduced.** METHOD field 3 requires a variance or interval with its definition; this is a reproducibility gap.

**Process grade (G37): RESULT-WRONG / PROCESS-WRONG IN PART.** The defects are execution failures of existing controls (`M15`), not a broken construction. The tree was coherent; its inputs leaned toward closeness without the checks that exist to catch that. Details in C.

#### P-483 — Retrospective (2026-09-22) — enhanced review

##### A. Prediction outcome

- **Pick #1 — Over 19.5:** LOSS (15 games).
- **Pick #2 — Kalieva +4.5:** LOSS (aggregate 3–12).
- **Pick #3 — Volynets −4.5:** WIN.
- **Pick #4 — Under 19.5:** WIN.
- **Over/under market:** preferred side (Over) lost; the Under, ranked last, won by 4.5 games.
- **Projected winner — Volynets:** WIN.
- **Overall:** the winner call was right; both preferred contract sides were wrong; the two winning rows were ranked #3 and #4.

##### B. Why each pick won or lost

**Pick #1 — Over 19.5 — LOSS.**

- *What happened.* Volynets won in 72 minutes without facing a break point. Kalieva's first-serve entry dropped to 47.8%, which put 24 of her 46 service points on her second serve; she won 7 of those and double-faulted four times. Volynets broke four times from nine chances, and the second set was 6-0.
- *Why it lost.* A line of 19.5 sits between the card's "decisive straight-set" representatives (18 games) and its "close straight-set" representatives (22). At that height **Over 19.5 is, in practice, "not a decisive straight-set win for either player"**, so the whole row turned on one quantity — the mass of decisive straight-set wins — and the match landed deep inside it.
- *Assumptions that held.* Volynets was the better player. Kalieva's serve was volatile: the card's named failure path — "Volynets repeatedly breaks Kalieva's volatile second-serve/double-fault branch and closes something like 6-2, 6-3" — is what happened, and it was weighted (30%). The scoreline-coherence mechanics were right, and no retirement branch was needed.
- *Assumptions that failed.* That Kalieva's higher 2026 service-points-won (56.1% v 54.5%) and hold rate (62.7% v 58.9%) pointed to a close match. Those were raw season aggregates from unequal samples (126 v 270 service games) and unequal opponent pools, compared serve with serve. Neither player's **return** profile was printed, so the matchup hold rates were never derived. Kalieva's volatility was read as a source of close sets rather than as width in both directions — a volatile server is also more likely to be routed. That is a possible `M11` instance (uncertainty converted into an Over lean).
- *Driver classification.* Partly knowable (favourite strength understated; Kalieva's second-serve exposure already documented), partly variance (Volynets served far above her season baseline over only 41 service points; a love set).
- *Weighting.* The decisive quantity — decisive-branch mass — was represented but under-sized relative to the independent strength benchmark (C, item 2).

**Pick #2 — Kalieva +4.5 — LOSS.**

- The row needed Volynets to win by four games or fewer: Kalieva had to take a set or stay close in both. It failed in the same state as Pick #1 — the two rows share one failure family, and that family occurred.
- The failed assumption was that "Kalieva's 2026 step-up and current service points/hold numbers give that pathway substance". The step-up is real (Memphis semifinal, US Open qualifying run), but an opponent-adjusted rating placed her far below her ranking (Tennis Abstract Elo #177 overall against WTA #113), and both of her main-draw matches since qualifying were losses (US Open R1 to Lanlana Tararudee; Guadalajara R1 to Kayla Day, 6-7(9), 4-6).
- The card ranked Kalieva +4.5 (58.4%) seventeen points above Volynets −4.5 (41.6%). That was the most benchmark-sensitive decision on the card (C, item 3).

**Pick #3 — Volynets −4.5 — WIN.** The card named "a credible straight-set separation branch" on the strength of Volynets' Philadelphia title. That branch occurred. Correctly identified; under-weighted.

**Pick #4 — Under 19.5 — WIN (by 4.5 games).** The card's stated live path — "a clean one-sided 6-2/6-3 or 6-3/6-3 result for either player" — is what happened, and then some.

**Projected winner — Volynets (≈ 62%) — WIN.** Every reason on the card held: level, the Philadelphia title and its return pressure, and the US Open loss read against world #6 Linda Noskova. The probability was under-confident relative to the benchmark.

##### C. Enhanced Rank-1 failure review — also the `TOP_OU_REVIEW`, the Rank-2 review and the mis-ordered-total review

| Pre-issue expectation | Actual driver | Difference | Knowability | Process grade | Defect class | Lesson / test | Method change |
|---|---|---|---|---|---|---|---|
| 39% deciding-set mass and frequent close straight sets → Over 65%, Kalieva +4.5 58% | A decisive Volynets straight-set win: Kalieva's second serve exposed, Volynets faced no break point | Decisive-branch mass (30%) too small; Volynets' winner mass (62%) 12–15 points below an independent benchmark | Partly knowable: the benchmark, both players' return profiles, a base rate and match-length windows were all retrievable | `PROCESS_DEFECT` (execution) | `M15` (tennis control 13, TE-S3 / `G-L18`, §9.8, §9.10 not executed); possible `M11`; `M17` | Print the benchmark before freezing; derive matchup holds from serve × return | Execution rules R-2, R-3, R-4 (§4.3). No coefficient |

1. **Why it ranked first.** It had the highest marginal on the frozen tree (65.2%), built from 39% three-set mass plus the close straight-set branches. The rank was coherent with the tree; the question is the tree.
2. **Was it justified on information available before issue?** Partly.
   - *For the Over — available, and partly used.* Recent match lengths were mostly above 19.5: Volynets' Philadelphia final 6-3, 7-5 (21 games) and her US Open loss 5-7, 1-6 (19); Kalieva's US Open qualifier 5-7, 6-4, 6-4 (32), her three-set US Open R1 and her Guadalajara loss 6-7(9), 4-6 (23). The card cited these results but did not print the §9.8 match-length windows.
   - *Against the closeness skew — available, not used:*
     - **Independent rating benchmark (tennis structural control 13, in force since 2026-09-11).** Tennis Abstract WTA Elo (page dated 2026-09-21; retrieved 2026-09-22): Volynets 1809.8 overall / 1766.3 hard; Kalieva 1597.8 overall (#177) / 1567.2 hard. Implied best-of-three win probability for Volynets: **≈ 77% (overall) and ≈ 76% (hard)**. Because the page is dated on match day, it may already include this result; allowing about ±14 Elo points for that, the range is **≈ 74–77%**. The card's 62% sits **12–15 points below**, and control 13 requires a named current mechanism for any gap over about 10 points. The benchmark was not printed.
     - **Level comparability (control 9) and `G-L7`.** The 2026 serve comparison was aggregate-only, not opponent- or level-adjusted, and not flagged `AGGREGATE_ONLY`.
     - **Return profile (TE-S3) and matchup holds (`G-L18`).** Printed for neither player. The card compared Kalieva's serve with Volynets' serve, never with Volynets' return.
     - **Reference base rate (§9.10; checklist item 11).** Not printed.
3. **Should another row have ranked higher?** For Rank #1, probably not decisively. An illustrative sensitivity — **not a forecast, not scored, and not entered in any aggregate** — re-weights the card's own six branches to a 76% Volynets winner mass:
   - Proportional re-weighting (Volynets' branch shares unchanged): representative Over ≈ 59% (≈ 61% after the card's own spread adjustment); Kalieva +4.5 ≈ 63% (≈ 52% adjusted). **Ranks unchanged; margins much thinner.**
   - If the added favourite mass also moves toward decisive wins (Volynets decisive branch 45%): representative Over ≈ 51% (≈ 52% adjusted); Kalieva +4.5 ≈ 55% (≈ 43% adjusted). **Volynets −4.5 moves above Kalieva +4.5**, and the Over becomes close to a coin flip.

   Which of these is right is exactly what a serve × return hold/break model decides — and that model was not built. So the Over may well have stayed Rank #1 under a compliant process, but its 65% was not supported, and the seventeen-point gap between Ranks #2 and #3 was not justified.
4. **Variable missed or mis-weighted.** Favourite strength (the benchmark), and the return side of the hold/break matchup. Kalieva's first-serve fragility should have been treated as a matchup weakness against a strong returner, not as symmetric variance.
5. **Should an existing control have prevented it, and was it executed?** Control 13 (benchmark), control 9 (level comparability), `G-L7` (`AGGREGATE_ONLY`), `G-L18` (hold marginals), §9.8 (windows including match length) and §9.10 (base rate) — **none executed** (`M15`). Controls that were executed: control 12 (a representative top-two scoreline, 6-4, 3-6, 6-3), `L-068` (winner, handicap and total derived jointly), `G-L17` (the shared-failure family named, with bounds) and line quarantine.
6. **Is a rule change warranted?** No coefficient and no directional tilt. Execution rules: make the benchmark a blocking pre-freeze field (R-2); derive matchup holds from serve × return (R-3); print P(decisive straight sets) for any best-of-three total between 18.5 and 21.5 (R-4). The underlying failure family recurs (D), which is why these are proposed now rather than logged as one-off.
7. **Variance share.** Volynets holding 8 of 8 without facing a break point (season hold 58.9%) and the love set are tail outcomes on a 41-point service sample. Even a benchmark-consistent tree would have left the Under at only about 40–49%. The loss is a mix of variance and a knowable over-confidence in a close match. It is **not** evidence that WTA Overs should be down-weighted.

##### D. Top-two review

- Rank #1 lost, Rank #2 lost; neither of the top two won. Both failed in the single state the card itself named as the shared-failure family ("decisive Volynets straight-set control").
- That family carried **30% of the card's own disjoint, exhaustive branch mass**. The card printed only Fréchet bounds (0–34.8%) and `JOINT_UNQUANTIFIED`. With an explicit six-branch tree, the representative-level figure (≈ 30%) was available and should have been printed (`G-L17`; METHOD field 5).
- Ordering: #1 above #2 is defensible; #2 above #3 is not, at 58.4 v 41.6 (C, item 3).
- **A recurring tennis pattern.** A favourite's separation — straight-set or efficient three-set — has now defeated a ranked Over (and, where one was ranked, an underdog games cushion) on four logged cards: P-212 (Alexandrova 6-2, 6-2 against Over 21.5), P-242 (Zheng's 28-game straight-set win against Marozsan +2.5 and Over 38.5, with the Zheng winner call correct), P-310 (efficient separation against a cushion and an Over) and P-483. The same pairing has also succeeded — P-350's Over 38.5 and Shelton +4.5 both won — so the pairing is not bad in itself. Its failures concentrate in one state whose mass these cards under-sized. Candidate test `C-TEN-FAV-SEPARATION` (§4.8).
- Improving top-two reliability without hedging: print the shared-failure number; benchmark the winner mass; and when Ranks #1 and #2 share one failure state, say plainly that the top two are one thesis ("the match is competitive"), so nobody reads them as two independent calls.

##### E. Over/under review — total games

| Factor | Card's treatment | What the record shows | Assessment |
|---|---|---|---|
| Conditions | Outdoor hard, ≈ 27–31 °C, no rain; no signed adjustment | No weather disruption | Correctly neutral |
| Set-count mixture | 61% straight sets / 39% three sets | Straight sets | Three-set mass generous for a ≈ 76% favourite |
| Serve / hold | 2026 serve aggregates for both players | Kalieva held 3 of 7; Volynets 8 of 8 | Matchup holds not derived |
| Return / break | Not printed (Philadelphia's 6/10 break points only) | Volynets converted 4 of 9; Kalieva earned none | Missing input |
| Lineups / availability | No injury found; retirement terms unknown | None; no retirement | Correct |
| Line position | 19.5 queried after the freeze | 19.5 sits between decisive (18) and close (22) straight-set representatives | The line was a decisive-branch question; the card did not say so |
| Distribution around the line | Representative total 23.1; no interval | 15 | Width not printed; PIT not reproducible |
| Variance sensitivity | High (Kalieva's double-fault volatility) | 4 double faults; 47.8% first serves in | The volatility cut toward a rout, not a close match |
| Sport-specific indicators | Serve comparison; recent results | — | Missing: benchmark, return points won, hold/break matchup, tour/surface base rate, match-length windows |

The defensible improvement is to derive P(decisive straight sets) from matchup holds, check the implied winner probability against the benchmark, and rank the total from that. Nothing here justifies tilting totals toward the Under.

##### F. What went right — keep these

1. **Winner correct, for the stated reasons** — level, the Philadelphia title, return pressure, and the Noskova-adjusted reading of the US Open loss.
2. **One shared six-branch tree, with every row derived from it.** The arithmetic reproduces (23.1 games, +1.66 margin). `L-068` executed.
3. **Control 12 executed.** A representative top-two state (6-4, 3-6, 6-3) was printed and checked against the winner.
4. **The real failure mechanism was on the card and weighted (30%).** The named-mechanism-closure standard from the P-474 audit (R-A) was met.
5. **Forced pairs labelled, preferred sides named,** opposite sides not counted as confirmation.
6. **Every factual claim checked was accurate** — identity, rankings, 2026 serve fields, Kalieva's US Open R1 against Tararudee, the Guadalajara loss, the Noskova match.
7. **Retirement terms marked `UNKNOWN_DEFINITION`** rather than assumed; no injury invented.
8. **The opponent-strength reading of the Noskova loss** was correct and is reusable.

##### G. Blind spots

| # | Blind spot | Available before issue? | How much it mattered | Future handling | Rule or observation |
|---|---|---|---|---|---|
| 1 | Elo benchmark not printed | Yes — keyless sports rating, market-free | High: winner mass 12–15 points low | Make control 13 a blocking pre-freeze field | Existing rule — execution (R-2) |
| 2 | No return profile; matchup holds not derived | Yes (WTA match statistics) | High | Derive each player's hold from server serve × returner return | Existing rule — execution (R-3) |
| 3 | Aggregate serve statistics not level-adjusted or flagged | Yes | Moderate to high | Flag `AGGREGATE_ONLY`; shrink toward the level prior | Existing rule — execution |
| 4 | No reference base rate for 19.5 | Partly — no admitted WTA dataset; the Sackmann `tennis_wta` repository returned HTTP 404 on 2026-09-22 | Moderate | Register a WTA totals base-rate source | Source gap |
| 5 | Match-length windows (§9.8) not printed | Yes | Low to moderate (they mildly supported the Over) | Print L5/L10 set counts and total games per player | Existing rule — execution |
| 6 | Within-branch spread not printed | — | Reproducibility only | Print the interval or SD for total and margin | Existing METHOD field 3 |
| 7 | Shared-failure mass given as bounds despite an explicit tree | Yes | Moderate (top-two honesty) | Print the number | Existing `G-L17` |
| 8 | Volatility read one way (toward close sets) | Yes | Moderate | Volatility widens both tails | Possible `M11` |
| — | *Not blind spots:* Volynets facing no break point; the love set | Hindsight only | — | — | — |

##### Mandatory validation questions

1. **Were confirmed starting lineups obtained?** Not applicable (singles). Both players were confirmed in the official draw, with no walkover marker.
2. **Were bench / reserve / rotation lineups obtained?** Not applicable. The rotation analogue — recent workload — was covered (Kalieva's three-set qualifying run; both players' recent schedules).
3. **Was coaching information obtained where material?** Not recorded. No coaching change was reported; not material on the available evidence.
4. **Were injuries, withdrawals and availability checked?** Yes. None found before the match, none reported during it, no retirement.
5. **Were the original sources accurate and current?** Yes for every fact used. The problem was using the aggregate 2026 serve comparison without a level or opponent adjustment.
6. **Were better sources available?** Yes: Tennis Abstract WTA Elo (the source control 13 names); WTA per-match statistics pages for each recent match — the per-match serve/return logs `G-L7` asks for, as P-338 printed them; and WTA draw PDFs for scores with a release timestamp.
7. **Were there blind spots?** Yes — table G.
8. **How should they be handled in future?** Benchmark before the freeze; derive matchup holds; print a base rate and match-length windows; print within-branch widths and the shared-failure number.

##### Connection to earlier learnings

| Earlier lesson or rule | Relationship to P-483 | Status |
|---|---|---|
| Tennis structural control 13 (P-350 origin, 2026-09-11): print an Elo benchmark; a gap over ~10 points needs a named mechanism | The single cheapest signal available before issue; not executed | **Recurrence of `M15`** |
| Control 9 (level comparability); `G-L7` (P-338's per-match serve/return logs as the positive model) | Not applied | `M15` |
| `G-L18` (print each player's expected hold marginal before ranking a total) | Not applied | `M15` |
| `G-L17` (shared-failure number) | Family named; bounds only | Partial |
| Control 12 / `L-068` / `C-PL9-TEN-CROSSMARKET` | Executed | Working |
| P-212, P-242, P-310 (favourite separation defeats an Over / underdog cushion) | Same failure family — fourth instance | **Recurring sport-specific pattern** |
| P-350 (a Rank-1 loss judged mostly variance, with the benchmark agreeing with the card) | Contrast: here the benchmark disagreed by 12–15 points, so this was not pure variance | Useful comparator |
| P-474 audit R-A (named-mechanism closure) | Met | Working |
| `M11` (uncertainty converted into an Over lean) | Possible instance | Watch |

**Classification.** A material variance share; a **sport-specific recurring pattern** (favourite separation against an Over and an underdog cushion); and the **cross-sport recurring** `M15` execution gap.

##### Source audit

| Source | Used for | Accurate? | Current? | Authority | Future use |
|---|---|---|---|---|---|
| WTA exact-match page | Identity, state, rankings, H2H, 2026 serve comparison; settlement statistics | Yes | Yes | Field owner | Keep as primary. The 2026 comparison is aggregate and must be level-adjusted before directional use |
| WTA tournament overview | Surface, dates, level | Yes | Yes | Field owner | Keep |
| WTA player record pages | Rankings, year-to-date record | Yes at issue | In this pass an automated fetch of Kalieva's record page returned figures inconsistent with WTA's own match pages (rank 140; 16-7; "no Grand Slam main draw") — probably a cached or partial render | Field owner | Take facts from match-level pages; do not rely on automated profile renders |
| WTA match pages (Philadelphia final; Noskova; Valdmannova; Day) | Recent process | Yes | — | Field owner | Keep |
| USTA / US Open report | Noskova game-script context | Yes | — | Event owner | Keep |
| L'Equipe; MyKhel | Pre-match state | Yes | Yes | Secondary | Keep for state |
| Structured Seoul weather | Conditions | No contradiction | Yes | — | Keep |
| **Tennis Abstract WTA Elo** — `https://tennisabstract.com/reports/wta_elo_ratings.html` | Independent strength benchmark, overall and hard | Dated snapshot | Weekly-dated | Sports rating, market-free, keyless | **Add to the tennis pre-freeze checklist** as the control-13 benchmark. Record the snapshot date and confirm it precedes the event; rating models have their own error |
| **WTA draw PDFs** — `https://wtafiles.wtatennis.com/pdf/draws/<year>/<tournament-id>/MDS.pdf` | Official result lines with a release timestamp | Yes | Same day | Field owner (same lineage as WTA pages) | Settlement corroboration. Parse the text layer: a summary extraction of one bracket was unreliable in this pass |
| Tennis Majors; TennisTemple; Canal Tenis | Terminal state | Yes | Same day | Independent secondary | Terminal-state lineages |
| Sackmann `tennis_wta` (GitHub) | Historical WTA match data for base rates | — | HTTP 404 on 2026-09-22 | — | Unavailable; the base-rate route needs a replacement |

No source is promoted because of one result. Tennis Abstract Elo is recommended because an existing control already names it and it is independent of the card's inputs.

##### Event-specific learnings

1. Print the rating benchmark before freezing. A 12–15 point gap is a construction warning, not a footnote.
2. Build each player's hold rate from their serve against the opponent's return — both ways.
3. For best-of-three totals between 18.5 and 21.5, state P(decisive straight sets); in practice it is the Over's complement.
4. Treat serve volatility as two-sided width.
5. Print the shared-failure number whenever the tree is explicit.
6. The winner call was right; the handicap and total ranks over-weighted closeness.

Document destinations for each of these are in §5.

---

### 4. General Learnings, Rule Changes, Observations, and New Sources — 2026-09-22 cohort (P-482–P-483)

Everything below is **LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE**. Two events cannot establish calibration, edge or model quality, and nothing here is a prospective validation. Every probability referenced is `UNVALIDATED_SUBJECTIVE`.

#### 4.0 What the two events show

| ID | Rank-1 | Hit@2 | Wins@2 | NDCG@2 | Decisions (forced pairs counted once) | Top over/under | Winner call |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| P-482 | W | YES (mechanical) | 1/2 | 1.000 | 1 W / 0 L | W | **W** |
| P-483 | **L** | NO | 0/2 | 0.000 | 0 W / 2 L | **L** (`TOP_OU_REVIEW`) | **W** |

- **Decisions:** 3 targets → 1 W / 2 L. Decision Brier: mean across targets **0.3090**; event-weighted **0.2719** (P-482 0.1608; P-483 0.3831).
- **Rank-1:** 1 of 2. **Top over/under:** 1 of 2. **Winner calls:** 2 of 2, mean Brier **0.1826**.
- **Row record:** 3 W / 3 L across six rows — **entirely mechanical**, because all six rows are halves of three forced pairs (P-474 audit rule R-G). It is not a performance figure.
- **Arithmetic check:** every printed card figure reproduced (P-482 mean 51.75 / SD 14.43 / P 0.5986; P-483 total 23.1 / margin +1.66). All Brier values above were recomputed from the issued probabilities.

**The common thread.** Both winner calls were right, and neither card got a fact wrong. On both cards, an **existing, mandatory control that bore directly on the decisive variable was not executed**: the innings-order venue window, the chase-inflation kill path and the toss retrieval for P-482; the rating benchmark, the return profile and the base rate for P-483. That is the `M15` pattern, and it is now the dominant defect across the last two mini logs (6 of 8 cards in P-474–P-481; 2 of 2 here).

#### 4.1 Cross-sport learnings

1. **Inspect wins as closely as losses.** P-482 won through the right mechanism with a probability sized on the wrong evidence. Grading it "process-different" rather than "process-right" keeps a lucky sizing from being reinforced. METHOD §7 already requires this; P-482 is a worked example.
2. **`M15` dominates, and the mechanical audit cannot see it.** Every decisive omission in this log is an existing control: cricket §10.8 venue window by innings order, control 32 toss retrieval and the §10.5 chase-inflation kill path; tennis control 13, TE-S3 / `G-L18`, §9.8 and §9.10. `audit_card_controls.py` detected none of them. It checks the retired §16.8 block rather than METHOD v4.3's six-field object, and it has no sport-checklist items. Tooling change R-7.
3. **Split evidence by the state that produced it before it sizes a distribution.** P-482 sized a batting-first phase on chase powerplays; P-483 sized a tour-level matchup on unadjusted season aggregates. The principle already exists (regime-dominance audit, `G-L7`); these two cards show it failing in two sports on the same day. Candidate registry item **M21** (§4.7).
4. **Near-start issuance and unresolved volatile fields travel together.** P-482 was issued six minutes before the scheduled start with toss and XIs unresolved (probably retrievable); P-483 at the scheduled-start minute. Same observation as the P-474 audit (§4.1 item 7). The start-state gate held; the evidence behind it thinned.
5. **Print joint masses as numbers when the tree is explicit.** P-483's own disjoint six-branch tree gave the shared-failure mass (≈ 30%); the card printed only Fréchet bounds. Keep `JOINT_UNQUANTIFIED` for dependence the model genuinely does not represent (R-5).
6. **Ledger discipline.** Register each mini-log card in the active combined log within 24 hours of issue (missed here; corrected in this pass).

#### 4.2 Sport-specific learnings

**Cricket (T20 franchise; CPL).**

- A phase total must be conditioned on innings order. Chase and batting-first powerplays at the same venue in the same week differed by about 25 runs on average (Kensington, 12–18 Sep). Pooling them, or sizing one from the other, is the error (R-1).
- Retrieve the toss at the toss window; the ESPN summary `notes[]` toss line is the fastest registered route. CR-2026.09.21-1 now makes the toss-window refresh mandatory.
- The phase-participant map must name the incoming Nos. 3–4 and both new-ball bowlers, not just the openers (control 20).
- Tentative: a collapse branch keyed to *who* is dismissed (the dominant hitter) may describe phase risk better than one keyed to wicket count. n = 1, with P-300 as a counter-example (R-6; evidence needed).
- Venue context only, not a rule: toss winners at Kensington chose to field in 6 of 6 matches from 12 to 20 Sep, and chasing sides won all six.

**Tennis (WTA).**

- The rating benchmark (control 13) is the cheapest check on a winner mass and was the most informative omission on P-483 (R-2).
- Hold rates must come from serve against return, for both players; season hold percentages compared serve-to-serve say little about a specific matchup (R-3).
- For best-of-three totals near 19.5, the Over is essentially "no decisive straight-set win". Print that mass (R-4).
- Serve volatility is two-sided width. A double-fault-prone server is also more likely to be routed.
- Favourite separation defeating a ranked Over plus an underdog cushion is now a four-card pattern (P-212, P-242, P-310, P-483), with at least one clean counter-example (P-350). Test it, do not ban it (§4.8).

#### 4.3 Potential rule changes

Ordered by strength of evidence. None is asserted as validated. **No Google Drive or repository rule document was edited by this pass**; each proposal is mapped in §5.

| # | Proposal | Evidence | Status | Target document |
|---|---|---|---|---|
| R-1 | **Cricket phase totals: innings-order conditioning.** Before the toss, model any powerplay/phase total as an explicit batting-first / chasing mixture; after the toss, use the realised branch. Team and venue phase windows are split the same way and printed with n. | ETPL 2026 Match 15 (69/1 chasing v 60/1 setting); P-445 (Jamaica 79/0 chasing v batting-first sample mean 43.5); P-482 (breakaway component sized on chases; Kensington batting-first mean 35.0 v chasing 60.0) | **Strong** — construction/disclosure rule with a clear mechanism; no coefficient. Recommend adoption | `RULES_CRICKET.md` §5 control 21 (extend to phase totals), §10.4 phase-total row, §10.8; `LEARNING_REGISTER.md` |
| R-2 | **Tennis benchmark as a blocking pre-freeze field.** Winner, handicap and total cards print the dated Elo benchmark (overall and surface) before freezing; a gap over ~10 points requires a named current mechanism or a rebuilt tree before issue. | Control 13 exists (P-350 origin). P-350: benchmark agreed, loss judged variance. P-483: benchmark 12–15 points away, not printed | **Strong** — enforces an existing control | `RULES_TENNIS.md` §9.7 checklist and control 13; `CONTROLS.md` |
| R-3 | **Tennis matchup holds from serve × return.** Print each player's return points won and derive each player's expected hold against this opponent before any total or handicap is ranked. | P-483 (serve-to-serve comparison only); P-338 (positive model: per-match serve/return logs) | **Strong** — makes TE-S3/TE-S4 and `G-L18` explicit | `RULES_TENNIS.md` §9.2; `RULES_GENERAL.md` §16.12 (`G-L18`) |
| R-4 | **Tennis decisive-branch disclosure.** For best-of-three totals from 18.5 to 21.5 (and the best-of-five analogue), print P(decisive straight sets for either player) alongside the Over, since the two are near-complements. | P-212, P-242, P-310, P-483 | **Moderate to strong** — disclosure only | `RULES_TENNIS.md` §9.4 total-games row; §9.5 kill path "Favourite control at 6-2, 6-2" (add P-483 as evidence) |
| R-5 | **Numeric shared-failure mass when the joint states are explicit.** `JOINT_UNQUANTIFIED` with bounds is reserved for dependence the model does not represent. | P-483; earlier `G-L17` execution misses (P-438, P-444) | **Strong** — clarification | `METHOD.md` §4 field 5; `RULES_GENERAL.md` §16.12(a) |
| R-6 | **Cricket collapse branch keyed to the dominant hitter's dismissal.** | P-482 supports; P-300 counter-example | **Weak — n = 1.** Log as a candidate only | `LEARNING_REGISTER.md` (TESTING) |
| R-7 | **Completeness tooling aligned with the current template.** Extend `audit_card_controls.py` (or add a companion) to METHOD v4.3's six fields and to sport checklist items — at minimum the tennis benchmark, the cricket venue window by innings order and `REFERENCE_BASE_RATE`. | This pass: the script flagged template drift on both cards and missed every omission that mattered | **Strong** — tooling | `audit_card_controls.py`; `CONTROLS.md`; `EXTERNAL_LOGGING_WORKFLOW.md` §2 |

**Explicitly rejected:**

- Any Under tilt for WTA totals, or any Over tilt for T20 powerplays. Both cards' errors were missing inputs, not a directional bias.
- "Fade the underdog games cushion" as a rule — P-350 and P-291 won with exactly that row.
- "The chasing side wins at Kensington" as a winner rule — six matches, one venue, one fortnight; `RULES_CRICKET.md` control 5 and §2.8 keep toss/innings order as context.
- Lowering Rank-1 confidence across the board after P-483.
- Treating P-482's win as evidence for chase-anchored breakaway components.

#### 4.4 Algorithm improvements

All are design proposals; none is fitted, calibrated or validated (`NUMERICAL_PROGRAM.md` governs any build).

1. **Cricket phase model.** Two innings-order branches, each built from the team's same-order phase window, shrunk toward the venue's same-order window and the competition phase population, with named participant adjustments (dominant hitter, incoming No. 3–4, opponent new-ball pair). Pre-toss weights are explicit; post-toss the model collapses to the realised branch.
2. **Tennis hold/break layer.** Each player's hold probability from their level-adjusted serve points won against the opponent's level-adjusted return points won; set and match distributions from the two hold rates; winner, handicap and total all queried from that one object; benchmark check before freezing. If the check fails, revisit the inputs, not the outputs.
3. **Tennis totals output.** Report P(decisive straight sets) and P(three sets) as the two primary total drivers beside every best-of-three total.
4. **Both sports.** Print the joint-failure number for the top two from the branch states.

#### 4.5 Source improvements

| Source / route | Best used for | Evidence from this pass | Recommended class |
|---|---|---|---|
| ESPN cricket API by league ID: `site.web.api.espn.com/apis/site/v2/sports/cricket/8623/summary?event=<id>` and `…/playbyplay?event=<id>&period=<innings>&page=<n>` | Toss, innings order, per-innings `Powerplay 1` matchnotes, milestones, over-end checkpoints; whole venue windows in a few calls | Settled P-482; verified every checkpoint on the card; built the Kensington window (events 1534212–1534216) | Primary structured route (one lineage with ESPNcricinfo). Complements the registered series-ID route (1534175) |
| Nation News (Barbados) | Independent Caribbean match reporting with ball-level detail | Supplied 30/2 at 3.4 and the dismissal sequence | Secondary / independent lineage |
| Tennis Abstract WTA Elo — `tennisabstract.com/reports/wta_elo_ratings.html` | Independent strength benchmark (control 13) | Benchmark 74–77% v card 62% | Pre-freeze check (not a probability source). Record the snapshot date |
| WTA draw PDFs — `wtafiles.wtatennis.com/pdf/draws/<year>/<id>/MDS.pdf` | Official result lines with a release timestamp | Corroborated 6-3 6-0 | Field-owner corroboration; parse the text layer |
| Tennis Majors; TennisTemple | Independent tennis terminal state | Both confirmed the final | Terminal-state lineages |

**Demoted or flagged.**

- **CaribbeanCricket.com and CricTracker** reproduce the CPL release verbatim — the same lineage as CPL. Never count them as independent.
- **Crex** — figures consistent, but it carried an unverified dew claim. Fallback only.
- **Yahoo Sports previews** — useful probable XIs; always `PROJECTED`.
- **WTA player profile pages under automated fetch** returned internally inconsistent figures in this pass. Take facts from match-level pages.
- **ESPNcricinfo HTML pages** returned HTTP 403 to automated fetch; use the API route.
- **Sackmann `tennis_wta` repository** returned HTTP 404 on 2026-09-22; no admitted WTA totals base-rate source currently exists.

#### 4.6 Data-quality observations

1. **Every issue-time fact checked was accurate** — all five cricket powerplay checkpoints; tennis identity, rankings, serve fields and recent results. Source accuracy was not the problem.
2. **Over labels in summarised ESPN JSON can be off by one.** The feed's "over 5" deliveries were the sixth over. Verify checkpoints with the run-rate identity (59 at 9.83 per over ⇒ 6.0 overs).
3. **One media summary misreported a milestone as a final score** (Sadaqat "100 not out"). Scorecards own player-level fields.
4. **An automated WTA profile render conflicted with WTA's own match pages** (rank 140; 16-7; "no Grand Slam main draw" for a player who played the US Open main draw).
5. **Summaries of draw PDFs are unreliable.** Two extractions of one Philadelphia bracket disagreed; use a text-layer parse.
6. **The Elo page was dated match day**, so whether the match is included cannot be read from the page. Snapshot benchmarks before the event.
7. **Mechanical audit mismatch.** `audit_card_controls.py --settlement` on the pre-settlement file flagged blocking fields 2, 3, 5a and 7 on both cards (and 10 on P-483 before settlement). Manual adjudication: field 2 is present on both (a three-component mixture with weights; a six-branch tree with masses); field 3 is present on both (mean/SD/corridor on P-482; representative total, margin and line probabilities on P-483, though with no interval for total games); field 5a is present on P-483 as named family plus bounds and is trivially zero on P-482's forced pair; field 7 is genuinely partial on P-482 (XIs, toss and coaches unrecorded) and not applicable in form on P-483 (singles). The script missed every omission that decided the outcome (R-7).

#### 4.7 Recurring blind spots

Mapped to the recurring-mistake registry so repeats are countable.

| Registry item | Where it appears here | Repeat? |
|---|---|---|
| **M15** — control listed, not executed | P-482: §10.8 venue window, control 32 toss retrieval, §10.5 chase-inflation kill path. P-483: control 13, TE-S3 / `G-L18`, §9.8, §9.10 | **Yes — 2 of 2 cards** (6 of 8 in P-474–P-481) |
| **M19** — published lineup not retrieved | P-482: toss and XIs were probably public before the final refresh | Yes |
| **M17** — small-sample rate used as direction | P-483: Kalieva's 126-service-game aggregate used to argue a close match | Yes |
| **M11** — unit uncertainty converted into an Over lean | P-483: serve volatility read as support for close sets (possible instance) | Possible repeat |
| **M10** — kill path written as prose, not weighted | Not observed — both cards weighted their named failure paths | Holding |
| **Candidate M21 (new) — state-contaminated evidence window:** evidence from one game state or level sizes a component for a different state | P-482 (chase → batting first); P-483 (lower-level aggregates → tour-level matchup); precedent P-445 | Proposed for the registry |

#### 4.8 Items requiring more evidence before becoming rules

1. **Dominant-hitter collapse keying (R-6).** One supporting case (P-482) and one counter-case (P-300). Needs a counted sample of phases with early wickets, split by whether the team's top-scoring batter was dismissed.
2. **Kensington night / chase effect.** 6 of 6 in one fortnight at one venue. Needs season-level innings-order splits at the venue before it is used as anything more than context.
3. **`C-TEN-FAV-SEPARATION`.** Do top-two pairs of "Over + underdog games cushion" underperform when the card's favourite mass sits below the benchmark? Needs a counted denominator of every such pair across Parts 1–5 and a prospective manifest frozen before new cards.
4. **Benchmark gap as an error predictor.** P-350 (inside the band; loss judged variance) and P-483 (outside; process defects) are consistent with the idea but are two cases. Track the gap against outcomes prospectively; do not use it for calibration.
5. **Post-toss freezing for cricket phase rows.** Track pre-toss against post-toss cards before recommending a default freeze time.

### 5. Document Update Mapping — 2026-09-22 cohort (P-482–P-483)

**No governing rule, method, source or register document was edited in this pass.** The mini log was updated in place, and P-482/P-483 were appended to this log. Every other item below is a mapping for later incorporation.

| # | Learning / change | Target document | Section | Type |
|---|---|---|---|---|
| 1 | R-1 — phase totals conditioned on innings order; windows split the same way | `RULES_CRICKET.md` | §5 control 21 (extend to phase totals); §10.4 phase-total row; §10.8 | Construction / disclosure rule |
| 2 | P-482 as reverse-direction evidence for the chase-inflation kill path | `RULES_CRICKET.md` | §10.5 kill-path table | Evidence row |
| 3 | Phase map names Nos. 3–4 and both new-ball bowlers | `RULES_CRICKET.md` | control 20; §10.7 checklist item 3 | Execution reinforcement |
| 4 | Toss via ESPN `notes[]` at toss + 5 minutes; P-482 as the evidence case for the CR-2026.09.21-1 toss-window refresh | `RULES_CRICKET.md` §2.7; `DATA_SOURCE_REGISTER.md` §6A (T4) | toss ladder | Execution evidence |
| 5 | ESPN league-ID route (8623) and `playbyplay` pages | `DATA_SOURCE_REGISTER.md` (`SRC-ESPN-SITE-API-CRICKET`); `SOURCES.md` | cricket structured routes | Source extension |
| 6 | Kensington CPL 2026 powerplays by innings order, 12–20 Sep (descriptive, n stated) | `BASE_RATES_REGISTER.md` | cricket | Descriptive base rate |
| 7 | Nation News as an independent Caribbean lineage; CaribbeanCricket.com / CricTracker = CPL lineage | `DATA_SOURCE_REGISTER.md`; `SOURCES.md` | lineage notes | Source classification |
| 8 | R-6 dominant-hitter collapse keying | `LEARNING_REGISTER.md` | TESTING candidates | Candidate |
| 9 | R-2 — benchmark as a blocking pre-freeze field | `RULES_TENNIS.md`; `CONTROLS.md` | §9.7 checklist; structural control 13 | Execution rule |
| 10 | R-3 — matchup holds from serve × return | `RULES_TENNIS.md`; `RULES_GENERAL.md` | §9.2 TE-S3/TE-S4; §16.12 `G-L18` | Execution rule |
| 11 | R-4 — decisive-branch disclosure for totals 18.5–21.5 | `RULES_TENNIS.md` | §9.4 total-games row; §9.5 kill path (add P-483) | Disclosure rule |
| 12 | Tennis Abstract WTA Elo; WTA draw PDFs; Sackmann repository 404 | `DATA_SOURCE_REGISTER.md`; `SOURCES.md` | tennis | New sources / source gap |
| 13 | WTA totals base rate: no admitted source as of 2026-09-22 | `BASE_RATES_REGISTER.md` | tennis | Gap record |
| 14 | `C-TEN-FAV-SEPARATION` manifest | `LEARNING_REGISTER.md` | §3 prospective tests | Candidate test |
| 15 | R-5 — numeric shared-failure mass when joint states are explicit | `METHOD.md`; `RULES_GENERAL.md` | §4 field 5; §16.12(a) | Clarification |
| 16 | R-7 — completeness tooling aligned to METHOD v4.3 and sport checklists | `audit_card_controls.py`; `CONTROLS.md`; `EXTERNAL_LOGGING_WORKFLOW.md` | tooling; §2 settle prompt | Tooling |
| 17 | `M15`, `M19`, `M17`, `M11` evidence rows; candidate `M21` | `LEARNING_REGISTER.md` | recurring-mistake registry | Registry update |
| 18 | "Result-right / process-different" worked example (P-482) | `LEARNING_REGISTER.md`; `RULES_GENERAL.md` | §5 retrospective examples | Worked example |
| 19 | P-482 / P-483 cards, settlements and retrospectives | `PREDICTION_LOG_COMBINED_5.md` | chronological events; controlling snapshot | **Done in this pass** |
| 20 | Register rows for P-482 and P-483 (text below) | `GAME_LOG_STATUS_CURRENT.md` | "Every canonical record from the first" table | Ledger — **not edited** |
| 21 | 24-hour registration window missed for this mini log | `EXTERNAL_LOGGING_WORKFLOW.md` | cadence / §3 | Process note |

Rows for item 20, ready to paste under P-481:

```
| P-482 | Cricket / CPL 2026 Final — Antigua & Barbuda Falcons vs Jamaica Kingsmen | FINAL / SETTLED / RETROSPECTIVE COMPLETE | Canonical source: `PREDICTION_LOG_COMBINED_5.md` 2026-09-22 import; mini log `PREDICTION_MINI_RUNNING_LOG_P482_ONWARD.md` |
| P-483 | Tennis / WTA 250 Korea Open (Seoul) R32 — Katie Volynets vs Elvina Kalieva | FINAL / SETTLED / RETROSPECTIVE COMPLETE (ENHANCED) | Canonical source: `PREDICTION_LOG_COMBINED_5.md` 2026-09-22 import; mini log `PREDICTION_MINI_RUNNING_LOG_P482_ONWARD.md` |
```

**Proposed new document: none.** A venue-by-innings-order phase register was considered and rejected: `BASE_RATES_REGISTER.md` already exists for descriptive base rates, and a second file would split them. Likewise the tennis benchmark belongs in the existing control 13 and `DATA_SOURCE_REGISTER.md`.

### 2026-09-22 — integrity notes for this import

- No issued probability, rank, selection, reasoning, distribution or source list was altered; the cards above are verbatim.
- Every printed card figure was recomputed and reproduced; every Brier value above was recomputed from the issued probabilities.
- Settlement used four independent lineages per event; syndicated copies of one release were counted once. No betting, tipster, line-movement or fantasy/DFS material was used.
- No governing rule, method, source or register document was edited. The proposals above are mapped for later incorporation; `GAME_LOG_STATUS_CURRENT.md` still ends at P-481 (rows ready to paste are in the mapping above).
- The P-482-onward mini log is fully settled but **not archived**: it remains the active running log for `P-484` onward.
- Next canonical ID: **`P-484`**.
