# Prediction Mini Running Log — P-474 Onward

> **2026-09-21 settlement / retrospective / audit layer for `PREDICTION_MINI_RUNNING_LOG_P474_ONWARD`.**
>
> The original P-474 to P-481 prediction cards and their 2026-09-20 settlements are preserved **unchanged** in the existing Google Doc `PREDICTION_MINI_RUNNING_LOG_P474_ONWARD.md` in this same folder. They were deliberately **not** re-uploaded, so that no preserved issued forecast could be altered in transit (`METHOD.md` §6).
>
> This audit layer is in two parts:
> - **Part A** — front matter, §1 Incomplete / Unsettled Logs, §2 Temporary-ID / Canonical-ID Conflict Logs, and the eight per-event `2026-09-21 independent re-audit` blocks that belong inside §3 Fully Settled Logs, one per card.
> - **Part B** — §4 General Learnings, Rule Changes, Observations and New Sources; §5 Document Update Mapping; §6 Settlement Lists; §7 Running Integrity Notes.
>
> The complete merged single-file version — original cards plus this audit layer, in the required order — is `PREDICTION_MINI_RUNNING_LOG_P474_ONWARD.md` at the Sports Research folder root.

Created: Sep 20, 2026
Last full settlement / retrospective / audit pass: **Sep 21, 2026 (Australia/Melbourne)**
Location/time basis: Australia/Melbourne
Governing method: MDS-2026.09.19-v4.3 / CR-2026.09.19-4
Control hashes recorded at issue: METHOD `da544d4c47efdf33bdbcc130a5ef0adc23055f77f80fd25284c1dc55f3d1b1b6`; RULES_BASEBALL `1e0b5a0e9636469f7b75fcc21d19f9fe3c557c691724e67bba821b145889a411`; RULES_BASKETBALL `f5ad8787a08fe6b1533c0f273058f26ab3ff3f731bc5307ebe40423993c14421`
Operating mode: SPORTS_ONLY / MARKET_BLIND
Performance status: **LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE**
Next intended ID after this card: P-482, subject to fresh reconciliation against `PREDICTION_LOG_COMBINED_4.md`.
Retrospective policy: settle completed events only after the CR-4 three-source terminal-state gate passes; live/unresolved events remain pending.

### What the 2026-09-21 pass did

Every one of P-474 through P-481 was already marked settled on 2026-09-20. This pass did **not** take that on trust. Each event's terminal state was re-verified against at least one source lineage that the original settlement did not use, and every pre-game claim that could be checked against a post-game record — confirmed lineups, benches, substitutions, participation, phase fields, corner fields — was checked.

Outcome of the re-audit:

- **All eight finals confirmed.** No settled row changed. No win became a loss or vice versa.
- **Three material new findings** that the 2026-09-20 pass did not record: the P-480 Anyembe availability error, the P-478 lineup-projection result (22 of 22 exact), and the P-478 corner-evidence downgrade (betting-branded pages used where a registered structured source publishes the field).
- **Two settlement-evidence upgrades:** P-478/P-480/P-481 corner fields now rest on the ESPN soccer `wonCorners` structured route, and P-479's phase field now rests on the ESPNcricinfo scorecard match note rather than a source that has since gone behind a bot wall.
- **One resolved pre-game uncertainty:** Natasha Cloud (P-475) is confirmed DNP.
- **A structural measurement correction:** the supplied-slate "record" across this mini log is almost entirely mechanical, because 28 of its 32 rows are strict complementary pairs. This is set out in §4.
- Document structure was rebuilt to the required order, and the mandatory validation questions are now answered explicitly and individually for every event.

Verification sources used in this pass are listed inside each event's `2026-09-21 independent re-audit` block.

## 1. Incomplete / Unsettled Logs

**None.** All eight events (P-474 through P-481) are completed, settled and retrospectively reviewed. Each passes the CR-4 three-source terminal-state gate, and after this pass each rests on at least four distinct lineages.

No event in this mini log is Upcoming, Live, Delayed, Suspended, Postponed, Abandoned or Cancelled.

| ID | Event | Event status | Settlement status |
|---|---|---|---|
| P-474 | Athletics @ Cleveland Guardians (MLB) | **Completed** | SETTLED / RETROSPECTIVE COMPLETE / RE-AUDITED 2026-09-21 |
| P-475 | Chicago Sky @ Atlanta Dream (WNBA) | **Completed** | SETTLED / RETROSPECTIVE COMPLETE / RE-AUDITED 2026-09-21 |
| P-476 | Minnesota Twins @ Los Angeles Angels (MLB) | **Completed** | SETTLED / RETROSPECTIVE COMPLETE / RE-AUDITED 2026-09-21 |
| P-477 | Sydney Kings vs Cairns Taipans (NBL) | **Completed** | SETTLED / RETROSPECTIVE COMPLETE / RE-AUDITED 2026-09-21 |
| P-478 | Djurgårdens IF vs IF Elfsborg (Allsvenskan) | **Completed** | SETTLED / RETROSPECTIVE COMPLETE / RE-AUDITED 2026-09-21 |
| P-479 | Edinburgh Castle Rockers vs Belfast Wolves (ETPL Final) | **Completed** | SETTLED / RETROSPECTIVE COMPLETE / RE-AUDITED 2026-09-21 |
| P-480 | Viborg FF vs FC Nordsjælland (Superligaen) | **Completed** | SETTLED / RETROSPECTIVE COMPLETE / RE-AUDITED 2026-09-21 |
| P-481 | Villarreal vs Levante (La Liga) | **Completed** | SETTLED / RETROSPECTIVE COMPLETE / RE-AUDITED 2026-09-21 |

## 2. Temporary-ID / Canonical-ID Conflict Logs

**No conflict, and no temporary ID is required for any entry in this mini log.**

Reconciliation performed on 2026-09-21:

- `PREDICTION_MINI_RUNNING_LOG_P452_ONWARD.md` covers **P-452 through P-473** and states next ID **P-474**. All 22 of its entries are settled with retrospectives complete and none awaiting settlement.
- This mini log covers **P-474 through P-481**, contiguous with the above, with no overlap and no reuse.
- `GAME_LOG_STATUS_CURRENT.md` enumerates canonical records through **P-451**.
- `PREDICTION_LOG_COMBINED_4.md` is the single active canonical log and remains the queue/next-ID authority.

**Outstanding integrity observations (not conflicts, but they should be cleared before the next issue).**

1. **The canonical register has not yet absorbed P-452 through P-481.** `GAME_LOG_STATUS_CURRENT.md` still ends at P-451, and one paragraph inside it still says "next ID `P-438`" alongside a later correction saying P-452. Thirty mini-log entries (P-452–P-481) exist only in the two mini logs. `METHOD.md` §3 step 7 requires an external log to be reconciled into the canonical log within 24 hours of availability, and states that an overdue unregistered log blocks the next forecast. **On a strict reading of that rule, P-482 is blocked until P-452–P-481 are imported into `PREDICTION_LOG_COMBINED_4.md` and the status register is extended.** That is a documentation-integrity matter, not a settlement defect — every entry is settled and evidenced.
2. **Temporary handles held elsewhere remain open and are unaffected by this pass.** 23 primary handles plus documentary/period audits sit in Parts 2–4. They are listed in §4.9 of Part B with the 2026-09-21 re-probe result. None belongs to this mini log and none blocks it.

## 3. Fully Settled Logs — per-event 2026-09-21 re-audit blocks

Each block below belongs immediately after that card's existing `Settlement and retrospective` section in the preserved log.

#### 2026-09-21 independent re-audit — P-474

**Re-verification of the settled final.** The 2026-09-20 settlement was re-checked against a source lineage that was not used in the original settlement pass, so the terminal state now rests on four distinct lineages rather than three.

- MLB Stats API official schedule record, `statsapi.mlb.com/api/v1/schedule?sportId=1&date=2026-09-19`, gamePk **824380**: status `Final`, Athletics 6 @ Cleveland Guardians 12.
- MLB Stats API official linescore for gamePk 824380: 9 innings; away line 2-0-1-1-2-0-0-0-0 (6 runs, 12 hits, 1 error); home line 5-0-5-1-0-1-0-0-X (12 runs, 15 hits, 1 error). The bottom of the ninth was not played, which is consistent with the home side leading.
- MLB Stats API official boxscore for gamePk 824380: Jacob Lopez 2.2 IP, 10 R / 10 ER, 10 H, 2 HR; Tanner Bibee 4.2 IP, 6 R / 6 ER, 12 H, 1 HR.

Every settled row is unchanged. **Final total 18; margin Cleveland +6.** The inning-by-inning record independently confirms the game-script claims in the 2026-09-20 retrospective (Athletics 2-0 in the top of the first, Cleveland 5 in the bottom of the first and 5 more in the third).

**Settlement-evidence upgrade.** The original settlement leaned on narrative recaps (AP/CBS, Athletics Nation, Field Level Media). Those remain valid corroboration, but the MLB Stats API linescore/boxscore is a structured field-owner record that settles run totals, margins, innings played and individual pitching lines without narrative interpretation. It should be the first settlement route for every MLB card, ahead of any recap.

**Ranking metrics — supplied slate (the only ranked slate on this card).**

| Metric | Value | Basis |
|---|---|---|
| Rank-1 | **WIN** | Guardians ML |
| Hit@2 | **YES** | Guardians ML + Over 7.5 |
| Wins@2 | **2 / 2** | both top-two rows won |
| NDCG@2 (binary relevance, ideal drawn from the whole ranked slate) | **1.000** | DCG@2 = 1 + 1/log₂3 = 1.6309; IDCG@2 = 1.6309 |
| Ranked-row record | 2 W / 2 L | forced-pair structure; see the note below |
| Winner call | **WIN** | Cleveland, p ≈ 0.655 |

**Forced-pair caveat (new, and it matters).** Over 7.5 / Under 7.5 is a strict complementary pair on a half-line: exactly one of those two rows wins by construction, whatever the model says. Only the preferred side carries information. Counting the preferred sides once, this card's informative decision rows are Guardians ML (0.655, **W**), Athletics +1.5 (0.528, **L**) and Over 7.5 (0.606, **W**) — 2 W / 1 L, not "2 W / 2 L out of four". The self-selected targets add Over 6.5 (**W**), Athletics team total Under 4.5 (**L**) and Cleveland team total Over 3.5 (**W**).

**Mandatory validation questions.**

1. **Confirmed starting lineups for both sides?** **NO — partial.** The card recorded `MLB_FIELD_OWNER_POSTED_LINEUPS_NOT_RECOVERED_TO_GATE_STANDARD`: the MLB starting-lineups index still rendered the matchup as TBD inside the research window, and a CBS/STATS-Field Level secondary cross-check was used with an explicit evidence cap. That was handled correctly — no player prop was ranked. The post-hoc boxscore shows the secondary cross-check was materially right, but that is hindsight and does not retroactively upgrade the pre-game evidence grade.
2. **Bench / bullpen / rotation state obtained?** **YES, partially and with the right framing.** Cleveland's preceding-game bullpen usage (Cantillo six relief innings; Gaddis and Smith in late innings) was recovered and used as an availability constraint only, not as a quality penalty. The Athletics bullpen was characterised by current-regime ERA rather than by named availability, which is weaker.
3. **Coaching / manager information?** **NOT OBTAINED, and not material.** MLB managerial decisions that mattered here (Lopez's hook at 2⅔ innings) are downstream of performance, not a pre-game identity fact.
4. **Injuries, suspensions, rest, late withdrawals checked?** **YES.** Rooker, Kurtz, Wilson (60-day IL) and Soderstrom (season-ending surgery) for the Athletics; Hoskins, Holderman and Armstrong for Cleveland, with DeLauter and Martínez flagged as day-to-day with residual uncertainty. DeLauter and Martínez both played and both homered, so the decision to treat them as available was correct.
5. **Were the original sources accurate and current?** **YES for availability and starters; INCOMPLETE for posted lineups.** No source used in the card was contradicted by the final record.
6. **Better sources available for future use?** **YES.** `statsapi.mlb.com` `game/{pk}/boxscore` exposes `battingOrder`, `bench` and `bullpen` by name, and `schedule?hydrate=lineups` returns 9+9 once orders are posted. The 2026-09-19 implementation ledger already recorded this lane as demonstrated. This card fell back to a CBS/STATS secondary instead of using it. That is an execution gap, not a missing capability.
7. **Blind spots in the pre-game analysis?** **YES.** The joint two-starter-failure branch. Both starters carried a documented contact/home-run tail, and the card said so about each of them separately, but the state in which *both* tails fire in the same game was never given explicit mass. The realised 18-run total sat far above the 8.34 centre precisely because both fired.
8. **How should this be handled in future?** When both starters carry a credible upper-tail contact/HR profile, print an explicit joint-collapse branch with its own weight *before* ranking any total or team-total Under. `RULES_BASEBALL` controls BB-B2 (joint early hook), BB-B3 (cluster) and BB-B5 (relief transition) already require these states; the defect is that they were listed and not executed as weighted branches. That is recurring-mistake **M15 (control listed, not executed)**, which turns out to be the dominant defect across this mini log — see §4.7.

**Verdict on this event.** Rank #1 and the top over/under both won, the winner call was right, and the one genuine analytical miss — the magnitude of the upper tail — did not change any ranked outcome. No rule change is warranted. The realised 18-run game is a single upper-tail realisation and, per `SCORING_AND_VALIDATION.md` §5, one named failure does not prove its mass was too low.

---

#### 2026-09-21 independent re-audit — P-475

**Re-verification of the settled final.** Re-checked at the ESPN WNBA site API, a lineage not used in the original settlement pass.

- `site.api.espn.com/apis/site/v2/sports/basketball/wnba/scoreboard?dates=20260919`, event **401857199**: status `Final`, Atlanta Dream 106, Chicago Sky 81.
- Quarter lines — Atlanta 26 / 25 / **32** / 23; Chicago 25 / 22 / 19 / 15. The third-quarter separation described in the 2026-09-20 retrospective is confirmed exactly.
- ESPN summary team statistics — Atlanta FG 36-68 (52.9%), 3PT **13-26 (50.0%)**, 29 assists, 13 steals, 35 rebounds, 15 turnovers; Chicago FG 31-67 (46.3%), 3PT **4-20 (20.0%)**, 21 assists, 8 steals, 30 rebounds, 17 turnovers.

Every settled row is unchanged. **Final total 187; margin Atlanta +25.**

**Two pre-game uncertainties are now resolved — this is new information the 2026-09-20 pass did not record.**

- **Natasha Cloud did not play.** The ESPN player box lists Cloud as a **DNP**, alongside Azurá Stevens, Skylar Diggins and DiJonai Carrington. The card's pre-tip status for her was QUESTIONABLE and was represented as a minutes/role mixture rather than a binary. The mixture was the right handling, and the "limited/out" leg of it is what actually occurred. The card should not be credited with knowing this, but the method of representing an unresolved availability as a weighted branch rather than as an assumed state is validated here.
- **Atlanta's starting five was exactly Canada / Gray / Howard / Hillmon / Reese** — the "long-running most-used starting unit" the card identified from Basketball-Reference lineup history but explicitly refused to relabel as confirmed. Chicago started Cardoso / Vandersloot / Coulibaly / Taylor / Jaquez. The Basketball-Reference lineup-continuity proxy was exactly right on the favourite, and the card was right not to overclaim it. Continuity history is a good prior on a starting five and a bad substitute for a confirmed team sheet.

**Chicago's scoring shape, newly visible.** Chicago's 81 came from breadth rather than from its nominal core: Jaquez 14, Cardoso 11, Coulibaly 11, Vandersloot 10, Maly 10, Sheldon 9, with 4-of-20 from three. The Chicago team-total Under 86.5 therefore won through the mechanism the card named — limited creation and no perimeter efficiency — not by accident.

**Ranking metrics.**

| Metric | Model-selected slate | Supplied slate |
|---|---|---|
| Rank-1 | **WIN** (Atlanta ML) | **WIN** (Dream -15.5) |
| Hit@2 | **YES** | **YES** |
| Wins@2 | **2 / 2** | **1 / 2** |
| NDCG@2 | **1.000** | **0.613** (DCG 1.000 / IDCG 1.6309) |
| Row record | 4 W / 0 L | 2 W / 2 L (one forced pair each way) |
| Top over/under | Atlanta TT Over 88.5 (Rank #2) — **WIN** | Under 176.5 (Rank #2) — **LOSS**, `TOP_OU_REVIEW` fired and the enhanced review is in the preserved log |
| Winner call | **WIN** — Atlanta, p ≈ 0.873 | — |

**Forced-pair caveat.** Both supplied pairs (-15.5 / +15.5 and Over / Under 176.5) are strict complements, so the supplied "2 W / 2 L" is mechanically fixed and carries no information. The informative content of the supplied slate is exactly two decisions: prefer Atlanta -15.5 (0.551, **W**) and prefer Under 176.5 (0.516, **L**) — 1 W / 1 L at probabilities barely above a coin flip. The model-selected slate is where the signal is: four free targets at 0.719–0.873, all four won.

**Mandatory validation questions.**

1. **Confirmed starting fives?** **NO.** The card carried `CONFIRMED_STARTING_FIVES_NOT_RECOVERED_TO_GATE_STANDARD` and capped participant-sensitive confidence accordingly. Correct handling. Post-hoc, the projected Atlanta five was exact.
2. **Bench / rotation information?** **PARTIALLY.** The available-core lists for both teams were recovered and were accurate. Depth quality was not modelled — and Atlanta's bench produced Borlase 18 and Paopao 5 in 36 combined minutes, which is precisely what beat the full-game Under.
3. **Coaching information?** **NOT OBTAINED.** The material coaching variable here was starter-minute management in a blowout (Reese 28 min, Gray 28, Canada 27 — never fully rested). That is knowable only as a tendency, not as a fact, and the card did carry a "blowout slowdown / bench compression" scenario at weight 0.18.
4. **Injuries / availability changes checked?** **YES, but the decisive row was left unresolved.** Season-ending absences (Diggins, Jackson, Brionna Jones) and the Stevens / Carrington absences were all correct. Natasha Cloud's final status was not recovered pre-tip — `CLOUD_FINAL_ACTIVE/INACTIVE_STATUS_NOT_RECOVERED_PRETIP_TO_FIELD_OWNER_STANDARD`. She was out.
5. **Were the original sources accurate and current?** **MOSTLY YES.** The WNBA official injury page did not expose its dynamic rows through the accessible route, which is the root cause of question 4. An Athlon 2:00 PM EDT injury report was used as a current independent secondary, was correct on every row it covered, and was correctly not promoted to field-owner status.
6. **Better sources available?** **YES, and concrete.** The ESPN WNBA `summary?event=` endpoint returns a per-player `starter` boolean and a `didNotPlay` flag. Post-game it settles the participation question definitively; pre-game the same endpoint exposes a `rosters` block once inactives are posted. It should be added to the WNBA settlement route and tested as a pre-tip availability route, because the official WNBA injury page is JS-rendered and has now failed this lane twice.
7. **Blind spots?** **YES — one, and the card half-saw it.** The favourite's bench offensive efficiency after separation. The card explicitly warned that "a depleted underdog does not automatically make the full game Under; Atlanta's own ceiling could consume the budget" — that warning describes exactly what happened — but the ranking then still preferred Under 176.5 while simultaneously assigning Atlanta team-total Over 88.5 a 77% probability. Those two statements are in tension and the tension was never reconciled numerically.
8. **How should this be handled in future?** Before a full-game Under can be ranked as the preferred total in a mismatch, print the implied joint budget: P(favourite team total ≥ x) against P(underdog team total ≤ total − x) in the same frozen states. If the favourite's own team-total Over is already high-confidence, the full-game Under must be labelled LOW evidence unless the underdog floor is demonstrably low in those same states. `RULES_BASKETBALL` controls 11, 17 and 18 and `PF-10` (distribution-first) already require this; the failure is execution, not absence — recurring-mistake **M15** (control listed, not executed) and **M14** (total probability not reconciled with the card's own centre and width in the ranking narrative).

**Verdict on this event.** The strongest call on the card — Atlanta to win, and to win comfortably — was right, all four free targets won, and the single loss was a 0.516 near-coin-flip the card had already labelled `CLOSE TO PROJECTION / WEAK MAIN-TOTAL EDGE`. The honest reading is that the labelling was right and the ordering was fragile, not that the total model is broken. No new rule; execution reinforcement only.

---

#### 2026-09-21 independent re-audit — P-476

**Re-verification of the settled final.** Re-checked at the MLB Stats API, a structured field-owner lineage not used in the original settlement pass (which relied on Reuters / Field Level Media, CBS/AP and MLB video).

- `statsapi.mlb.com/api/v1/schedule?sportId=1&date=2026-09-19`, gamePk **823976**: status `Final`, Minnesota Twins 5 @ Los Angeles Angels 6.
- Official linescore: **11 innings played** (scheduled 9). Minnesota by inning 0-0-2-1-1-0-0-1-0-0-0 = 5 (11 hits, 1 error); Los Angeles 0-0-0-2-0-0-0-2-1-0-1 = 6 (11 hits, 0 errors, 15 left on base).
- Official boxscore: **Joe Ryan 5.0 IP, 2 R / 2 ER, 5 K**; **Reid Detmers 5.0 IP, 4 R / 4 ER, 5 K**.

Every settled row is unchanged. **Final total 11; margin Angels +1 in 11 innings.**

The linescore independently confirms the retrospective's game script to the inning: Minnesota led **5-2** entering the bottom of the eighth, the Angels scored 2 in the eighth (5-4), 1 in the ninth (5-5) and 1 in the eleventh (6-5). The claim that the game stood at seven runs through seven innings is exact — 4 + 3 = 7 after seven.

**Detmers 5+ strikeouts settles WIN at exactly the threshold**, now confirmed at the field owner rather than at a box-score aggregator. One strikeout fewer would have flipped it; that fragility belongs beside the win rather than being read as a validated exposure model.

**Ranking metrics.**

| Metric | Supplied slate | Model-selected slate |
|---|---|---|
| Rank-1 | **WIN** (Twins +1.5) | **WIN** (Detmers 5+ K) |
| Hit@2 | **YES** | **YES** |
| Wins@2 | **2 / 2** | **2 / 2** |
| NDCG@2 | **1.000** | **1.000** |
| Row record | 3 W / 1 L | 2 W / 2 L |
| Top over/under | Over 7.0 (Rank #3) — **WIN** | Full-game Under 8.5 (Rank #4) — **LOSS** |
| Winner call | **WIN** — Angels, p ≈ 0.569 | — |

**Push-capable scoring, done properly.** Over 7.0 was frozen as a three-state target, W/P/L = 0.466 / 0.159 / 0.375, and the realised outcome was a WIN. Complete W/P/L Brier = **0.2255**; decisive q = 0.466 / (1 − 0.159) = **0.5541**, decisive binary Brier = **0.1988**. Reporting only the decisive score would overstate the card, because the 15.9% push mass was real and was correctly disclosed. This is the best-executed piece of contract geometry in the mini log.

**The top-two overlap logic is the standout result.** The card ranked Twins +1.5 (0.634) above Angels ML (0.569) and said why: both rows win when Los Angeles wins by exactly one run, and the joint model put material mass on that state. Los Angeles won by exactly one run. The mechanism was named before the event and then occurred — that is a validated piece of reasoning, not a favourable-looking coincidence.

**Mandatory validation questions.**

1. **Confirmed starting lineups?** **YES — both, in full.** The MLB all-club starting-lineups index returned complete nine-man posted orders for both teams. This is the only card in the mini log that cleared the lineup gate outright, and it is also the only card that passed preflight with zero blocking findings. That co-occurrence is worth noting: the card issued earliest relative to first pitch was also the card with the best evidence.
2. **Bench / bullpen state?** **YES.** Both bullpens were reconstructed from the preceding Sep 18 game with named-arm workload (Prielipp 7 IP, Nance, Adams for Minnesota; Rodriguez 6⅔, Peralta, Murphy for Los Angeles), and the extra-inning Sep 16/17 usage was carried forward as an availability constraint. Correct treatment — workload informed availability, not quality.
3. **Coaching information?** **NOT OBTAINED, not material.**
4. **Injuries / availability?** **YES, and correctly current.** Buxton (hip labrum repair, Sep 18), Larnach and Culpepper for Minnesota; Paris, Schanuel and Natera for Los Angeles; Bachman activated Sep 16; Ryan activated Sep 7. Critically, the card **removed an obsolete absence flag** on Royce Lewis because he appeared in the posted order. That is the correct direction of error-correction, and the exact opposite of the P-480 failure below.
5. **Were the original sources accurate and current?** **YES**, with one disclosed inconsistency: MLB's team-specific lineup subpages still rendered TBD while the all-club index exposed full orders. The card recorded the inconsistency instead of hiding it.
6. **Better sources available?** **Marginally.** `game/{pk}/linescore` and `game/{pk}/boxscore` should be the first settlement route rather than Reuters/CBS recaps — they settle innings played, team totals, margins and pitcher lines in two calls with no narrative interpretation. Same upgrade as recommended for P-474.
7. **Blind spots?** **YES — one, and it is the card's own stated tail.** Under 8.5 was selected as a self-chosen alternate sitting 1.15 runs above the 7.346 centre, while the same frozen object carried about 14.25% tie-after-nine mass plus an explicit automatic-runner branch. The card described the mechanism that beat it and then chose a threshold that could not survive it.
8. **How should this be handled in future?** For any MLB alternate Under, print P(tie after nine) + P(late relief-transition crossing) against the chosen threshold, not merely the distance from the central total. `RULES_BASEBALL` BB-B5 and BB-B7 already require both states; the card had them as prose rather than as a threshold-crossing calculation. **M14 / M15 again.**

**Verdict on this event.** Process-best card of the mini log: preflight PASS, both lineups confirmed, push mass handled honestly, dependence between the top two stated in advance and then realised. The only defect is the self-selected Under 8.5, beaten by a tail the card itself had documented.

---

#### 2026-09-21 independent re-audit — P-477

**Re-verification of the settled final.** The NBL/AAP postgame report was re-opened in full this pass and returns the complete quarter sequence, which the 2026-09-20 settlement summarised but did not enumerate.

- NBL / AAP postgame report: **Sydney Kings 111, Cairns Taipans 90**. Q1 32-26; halftime **59-53**; three-quarter time **90-73**; final 111-90.
- Leading scorers: Kendric Davis 26 (6 ast, 5 reb), Xavier Cooks 18 (7 reb, 2 blk), Torrey Craig 13 for Sydney; **Keanu Pinder 27** (5 reb, 4 ast), Shaun Bruce 13, Malique Lewis 13 for Cairns.
- Shooting: Sydney 65% from the field in the first half and **6-of-9 from three in the third quarter**; Cairns **13-of-44 from beyond the arc (29.5%)**.
- Corroborating lineages already recorded: Cairns Taipans official postgame report (111-90) and the Austadiums exact-event record (111-90 Final, Sep 20 2026, 5:00 PM, Afterpay Arena).

Every settled row is unchanged. **Final total 201; margin Sydney +21.**

**A source-state warning recorded on 2026-09-20 is confirmed and should be promoted.** The NBL public schedule shell displayed a generic `LIVE NOW` label on fixtures that had not started. This pass re-confirms that the NBL schedule shell is not an event-state authority. Event state for NBL must come from an exact-event record (league match centre, club postgame report or an independent exact-event record such as Austadiums), never from a schedule-page badge.

**Ranking metrics.**

| Metric | Model-selected slate | Supplied slate |
|---|---|---|
| Rank-1 | **WIN** (Sydney ML) | **WIN** (Over 185.5) |
| Hit@2 | **YES** | **YES** |
| Wins@2 | **2 / 2** | **1 / 2** |
| NDCG@2 | **1.000** | **0.613** |
| Row record | 2 W / 2 L | 2 W / 2 L (both forced pairs) |
| Top over/under | Over 179.5 (Rank #2) — **WIN** | Over 185.5 (Rank #1) — **WIN** |
| Winner call | **WIN** — Sydney, p ≈ 0.70 | — |

**Forced-pair caveat.** Both supplied pairs (Over/Under 185.5 and Cairns +8.5 / Sydney -8.5) are strict complements, so the supplied 2 W / 2 L is again mechanically fixed. Informative decisions: prefer Over 185.5 (0.533, **W**) and prefer Cairns +8.5 (0.529, **L**) — two near-coin-flips, one each way.

**The internal contradiction on this card is worth naming.** The model-selected slate simultaneously held **Over 179.5 (0.69)** and **Under 191.5 (0.63)**, which is a corridor bet of 180–191 with a stated width of about 12 points around a 186.7 centre. The realised 201 cleared the corridor. Selecting both ends of a narrow corridor as two of the four "best" targets inflates the apparent slate size without adding independent information: the two rows share one driver and can only both win inside a band the card itself described as uncertain. Under `SCORING_AND_VALIDATION.md` §3 these are not two independent trials.

**Mandatory validation questions.**

1. **Confirmed starting fives?** **NO.** Expected/projected fives were retrieved; a formal confirmed five for either club was not recovered before issue. Rotation-sensitive props were correctly not promoted.
2. **Bench / rotation information?** **PARTIALLY.** Squad composition was known; rotation depth was treated qualitatively. Six Kings finished in double figures, which is a depth outcome the card did not quantify.
3. **Coaching information?** **NOT OBTAINED.** For an opening-round game with a new Sydney signing (Andrew Carr) and a substantially rebuilt Cairns roster, rotation policy is genuinely uncertain and arguably deserved an explicit uncertainty widening rather than a narrower corridor.
4. **Injuries / availability?** **YES and correct.** Sydney: Keli Leaupepe out. Cairns: Jaylin Galloway and Luke Paul out. All three were correctly modelled as absent, and the NBL postgame report confirms Cairns still had Galloway and Paul to come into the team. Kendric Davis's shortened preparation (passport-delayed return) was flagged and correctly not converted into a performance penalty — he scored 26.
5. **Were the original sources accurate and current?** **YES on availability and identity.** The one defective source was the NBL schedule shell's `LIVE NOW` badge, which was correctly refused.
6. **Better sources available?** **YES.** Austadiums proved to be a clean independent exact-event terminal record for Australian fixtures and should be registered as a third lineage for NBL/AFL/NRL settlement. Separately, the ESPN site API does **not** cover NBL, so the standard keyless lane is unavailable for this competition and the league/club/independent-event triad is the correct substitute.
7. **Blind spots?** **YES — two.** (a) An opening-round game after a long off-season has wider outcome dispersion than the card's ~12-point corridor allowed; roster turnover on both sides was known pre-game and should have widened, not narrowed, the distribution. (b) The joint state in which the favourite's perimeter efficiency spikes *and* the underdog shoots high-volume/low-efficiency threes produces a larger margin **and** a higher total at the same time. Cairns went 13-of-44 from three; that is 44 possessions ending in a low-percentage shot, which sustains pace while losing the game.
8. **How should this be handled in future?** Two specific changes. First, treat **round-one / post-off-season / heavy-roster-turnover** games as an explicit variance-widening state, and record it as a candidate test rather than a fixed coefficient until there is a sample. Second, never rank an upper Under and a lower Over from the same corridor as two independent "best" targets — state the corridor once, with its probability, and count it as one decision.

**Verdict on this event.** Direction was right on every axis that mattered (winner, the lower Over, the supplied Over) and the two losses were the two corridor-closing rows. The correct lesson is about corridor width and slate independence, not about the winner model.

---

#### 2026-09-21 independent re-audit — P-478

**Re-verification of the settled final, and a material upgrade to the corner evidence.**

- ESPN soccer site API, `swe.1` scoreboard for 2026-09-20, event **401842828**: status `Full Time`, **Djurgården 1 — IF Elfsborg 2**.
- ESPN `swe.1` summary for event 401842828 — key events: Stensson yellow 39'; **Rasmus Wikström goal 44' (Elfsborg)**; Djurgården substitutions Fallenius 45', Abdulmalik 60', Max Larsson 60'; **Jacob Une goal 66' (Djurgården)**; **Simon Olsson goal 76' (Elfsborg)**; Langhoff 75', Rosenquist 78'.
- ESPN team statistics for the same event: **corners Djurgården 4, Elfsborg 7 — total 11**; possession 55.6 / 44.4; shots 9 / 15; shots on target 2 / 3.

**This resolves a genuine evidence-quality defect in the 2026-09-20 settlement.** That pass settled Total Corners Over 7.5 from three betting-branded derivative pages (WinDrawWin, BetStudy, TotalCorner) because it could not reach a trustworthy final corner field, and it recorded that limitation honestly. The corner count is in fact published by the ESPN soccer summary endpoint as `wonCorners`, a keyless structured route that is already in the project source register as the verified owner of soccer corner fields. **The settlement outcome is unchanged — 11 corners, Over 7.5 WIN — but the evidence now rests on a registered non-market structured source instead of three betting-branded pages.** The betting-branded citations should be demoted to "not required" for this row.

This is the most transferable finding in the whole audit: a known-good source in the register was not used, and a weaker substitute was accepted in its place. That is recurring-mistake **M15** in its source-selection form.

**A strong, and genuinely surprising, positive finding on lineups.** The card published role-continuity XIs for both clubs while explicitly refusing to label them confirmed. Against the ESPN confirmed team sheets:

- **Djurgården — 11 of 11 exact.** Rinne; Ståhl, Tenho, Une (Larsson), Johansson; Stensson, Siltanen; Åslund, Hegland, Okkels; Lien.
- **Elfsborg — 11 of 11 exact.** Pettersson; Jensen, Wikström, Isherwood, Hult; Magnússon, Olsson; Kamara, Beck, Zeneli; Östman.

The method that produced this was: take the starting XI from each club's **own official report of its most recent league match**, then cross-check against a current independent lineup feed, and publish it as projected. That produced 22 of 22 correct names here. Contrast P-481 below, where a same-day third-party lineup page was treated as fresher and got three of the four named attackers wrong. **Role continuity from the club's own last official team sheet is the stronger projection route; same-day third-party lineup pages are not.** This is a concrete, testable source-quality conclusion and the single most useful thing recovered in this pass.

**Ranking metrics.**

| Metric | Model-selected slate | Supplied slate |
|---|---|---|
| Rank-1 | **WIN** (Djurgården TT Over 0.5) | **WIN** (1H Over 0.5) |
| Hit@2 | **YES** | **YES** |
| Wins@2 | **1 / 2** | **2 / 2** |
| NDCG@2 | **0.613** | **1.000** |
| Row record | 3 W / 2 L | 2 W / 2 L (both forced pairs) |
| Top over/under | Total Corners Over 7.5 (Rank #4) — **WIN**; Under 3.5 (Rank #5) — **WIN** | 1H Over 0.5 (Rank #1) — **WIN** |
| Winner call | **LOSS** — Djurgården, p ≈ 0.602 | — |

**Mandatory validation questions.**

1. **Confirmed starting XIs?** **NO — projected only, and correctly labelled.** The official Djurgården preview still said the squad would be published one hour before kick-off, and the accessible route never refreshed. Post-hoc the projections were exact, which validates the method but does not retroactively confer a confirmed evidence grade.
2. **Bench / substitute information?** **NO — and this is where it mattered.** The card had no matchday bench. The decisive 1-2 came at 76', after Djurgården had made three attacking substitutions (45', 60', 60'), and postgame tactical reporting attributes the goal to two substitutes failing defensive assignments, which let Alexander Jensen run free to create for Simon Olsson. A missing bench is not a missing detail on this card; it is a missing input to the decisive mechanism.
3. **Coaching / tactical information?** **PARTIALLY.** Formation shape (4-2-3-1 both sides) was modelled. In-game substitution policy was not, and it is what the postgame analysis identifies as causal.
4. **Injuries / suspensions / withdrawals?** **YES and correct.** Djurgården: Christos Almyras suspended after a red card v GAIS, correctly characterised as a bench/rotation loss because he was not in the recent XI. Elfsborg: Per Frick unavailable with a broken hand, correctly characterised as a loss of late attacking depth. Neither was contradicted by the team sheets.
5. **Were the original sources accurate and current?** **MIXED.** Club official reports, the Allsvenskan round schedule and the xG/corner statistical sources were accurate. The structured event feed still returned `Scheduled` after kick-off had passed, which is a staleness defect and is the reason the card was correctly labelled a late-issued research forecast rather than a normal pregame PASS. For settlement, the betting-branded corner routes were adequate but unnecessary — see above.
6. **Better sources available?** **YES, decisively.** ESPN `swe.1` `summary?event=` supplies the final, halftime-implied goal times, both confirmed XIs, both benches, substitution times and `wonCorners` in a single keyless call. It should be the primary settlement and lineup-audit route for every ESPN-covered soccer competition, ahead of both the structured event feed and any derivative statistics page.
7. **Blind spots?** **YES — three, in order of materiality.** (a) The away side's win branch was assigned only 17.9% while Elfsborg were a 34-point top-half side with 29.1 xG and 25.7 xGA; that is too thin for a competent visiting team even against a five-win home streak. (b) Goalkeeper error was not represented at all, and the 0-1 came through a weak Jacob Rinne intervention. (c) Substitution-driven defensive-transition risk existed in prose but carried no weight in the side or away-team-total distributions.
8. **How should this be handled in future?** Three specific, small changes. First, **floor the away-win branch** in a two-competent-sides league fixture at the competition's own away-win base rate unless there is a named suppression mechanism — Djurgården's home record is a reason to sit above the base rate, not a reason to sit at half of it. Second, require the **bench/substitution branch to carry explicit weight** in the winner and team-total distributions whenever the favourite is expected to chase or extend a lead, rather than appearing only as narrative. Third, record **goalkeeper-error mass** as part of ordinary low-event variance rather than treating a single defensive mistake as unmodellable; the point is not to predict the error but to stop the away-win branch being compressed below its base rate.

**Verdict on this event.** Rank #1, both corner and goal totals and the first-half direction all landed; the side/winner view was materially wrong and the away-team-total Under was too confident. The corner model deserves specific credit: it was built independently of the goal model from corner-exposure rates and score-state width, it predicted about 9.4, the realised count was 11, and it won even though the goal-side view was wrong. That independence is the right design and should be preserved.

---

#### 2026-09-21 independent re-audit — P-479

**Re-verification of the settled final at a stronger source than the original settlement used.** The 2026-09-20 pass settled at CricketWorld, BBC-via-Yahoo and MyKhel. CricketWorld is now behind a bot-verification wall and returns nothing through either the direct route or the text proxy, so that lineage is no longer reproducible. The ESPNcricinfo full scorecard, reached through the `r.jina.ai` text proxy, reproduces every settled field and adds the exact phase record:

- **Belfast Wolves 150/5 (20 overs)**; Edinburgh Castle Rockers **151/3 (18.4 overs)**; **Edinburgh won by 7 wickets with 8 balls remaining**.
- **Toss: Edinburgh Castle Rockers, elected to field first.** Belfast therefore batted first, which is what activated every supplied "Belfast first innings" and "Belfast first six" contract.
- **`Powerplay 1: Overs 0.1 - 6.0 (Mandatory - 41 runs, 1 wicket)`** — the exact field that settles both powerplay rows, published as a structured match note rather than inferred from a ball-by-ball reconstruction.
- Belfast batting: Stirling 8 (10), **Tim Tector 84 (62)**, **Devon Conway 29 (24)**, Maxwell 3 (5), Tucker 6 (5), Manenti 16* (14); extras 4. Fall of wickets 1-18 (2.6), 2-81 (11.3), 3-95 (12.6), 4-105 (14.4), **5-150 (19.6)**.
- Belfast did not bat: Chris Jordan, Mark Adair, Gavin Hoey, Fred Klaassen, Matthew Humphreys. **Neither Mark Chapman nor David Miller appears in the XI at all** — confirming the card's decision to treat them as selection uncertainties rather than asserting availability.
- Edinburgh chase: Ross Adair 23 (14), Smuts 15 (23), **Andries Gous 90* (61)**, McMullen 17 (12), Santner 2* (2).

Every settled row is unchanged. **Belfast powerplay 41/1; Belfast innings 150; Edinburgh won by 7 wickets.**

One correction to a secondary source used in the settlement chain: the Yahoo-syndicated BBC summary names the No. 3 batter as "Paul Conway". The scorecard shows **Devon Conway**. The mini log's original text said Devon Conway and was right; the syndicated summary was wrong. This is a small but useful illustration of why a scorecard and not a recap owns player-level fields.

**Ranking metrics.**

| Metric | Model-selected slate | Supplied slate |
|---|---|---|
| Rank-1 | **WIN** (Belfast first six Under 55.5) | **WIN** (Belfast first six Under 46.5) |
| Hit@2 | **YES** | **YES** |
| Wins@2 | **2 / 2** | **1 / 2** |
| NDCG@2 | **1.000** | **0.613** |
| Row record | **4 W / 0 L** | 2 W / 2 L (both forced pairs) |
| Top over/under | Under 55.5 (Rank #1) — **WIN** | Under 46.5 (Rank #1) — **WIN** |
| Winner call | **WIN** — Edinburgh, p ≈ 0.56 | — |

**Why this card worked, mechanically.** The powerplay was modelled *separately* from the full innings rather than as a fraction of it. The card's powerplay centre was ~45 against a realised 41, and its full-innings corridor was 145–175 against a realised 150. Both were right at the same time precisely because they were built as two linked but distinct quantities. The card also explicitly wrote down the state in which a subdued powerplay still recovers into a large total — it had a 36/2-to-190/4 precedent from the same two teams three days earlier — and then declined to let that precedent drag the innings centre upward. That is correct use of a small sample: as a width argument, not as a centre shift.

**Mandatory validation questions.**

1. **Confirmed XIs / toss?** **NO — neither, before issue.** The final pre-issue refresh recovered neither the toss nor a confirmed XI. The card issued anyway and labelled the gap. In a T20 final where every supplied contract was conditioned on "Belfast first innings", **the toss is an activation condition, not a detail** — if Belfast had bowled first, all four supplied rows would have needed activation review rather than settlement. The card was one coin-flip away from a `CONDITION NOT MET` outcome of the kind recorded at P-445.
2. **Bench / squad information?** **PARTIALLY.** Squad availability was known at competition level; the final XI was not.
3. **Coaching / captaincy information?** **NOT MATERIAL** beyond the toss decision, which is covered above.
4. **Injuries / withdrawals?** **YES, and handled to the right standard.** Charlie Tear was officially ruled out for Edinburgh. Mark Chapman had retired hurt in the previous meeting, but no reliable current source confirmed an ongoing injury, so the card treated Chapman and David Miller as **selection uncertainties rather than inventing absences**. Both were in fact absent from the XI. Declining to assert an unverified absence and then being right is exactly the behaviour `METHOD.md` §6 requires.
5. **Were the original sources accurate and current?** **YES at the time; one has since degraded.** CricketWorld supplied the powerplay field on 2026-09-20 and is now bot-walled. That is a live source-availability change and should be recorded.
6. **Better sources available?** **YES.** ESPNcricinfo's full scorecard via the text proxy exposes `Powerplay 1: Overs 0.1 - 6.0 (Mandatory - N runs, W wickets)` as an explicit structured match note, plus toss, fall of wickets and the did-not-bat list. It is strictly better than CricketWorld for phase settlement and is the same route that settled P-406's six-over rows on 2026-09-16. It should be the registered first route for T20 phase fields.
7. **Blind spots?** **TWO, both about conditions rather than modelling.** (a) **Strip status was `NOT FOUND AFTER SEARCH`** after the full pitch-report ladder, so the innings centre rested on venue/format history plus the preceding same-venue match, which the rules correctly treat as a different strip. Postgame metadata describes the surface as spinning/average with swing — useful, but retrospective, and correctly not backfilled. (b) The supplied 158.5 line sat within ~8.5 runs of a ~160 centre with substantial innings variance, so neither side of it ever deserved confidence; the card said 53/47 and that was honest.
8. **How should this be handled in future?** Keep the corridor-first construction, which worked. Add one hard requirement: **when every supplied contract is conditioned on a specific team batting first, the toss must be treated as a blocking activation gate** — either recover it, or state the activation probability explicitly and rank conditional on activation. The existing cricket rules cover innings-phase separation well; they do not currently force the toss to be treated as an activation condition on the supplied slate.

**Verdict on this event.** The best-forecast card in the mini log: four of four model-selected targets won, the powerplay and the innings corridor were both centred correctly, the winner was right, and the two supplied losses were the dead side of a near-coin-flip line. The only real exposure was procedural — issuing four toss-conditional contracts without the toss.

---

#### 2026-09-21 independent re-audit — P-480

**Re-verification of the settled final at the keyless structured lane.**

- ESPN soccer site API, `den.1` scoreboard for 2026-09-20, event **401874495**: status `Full Time`, **Viborg FF 4 — FC Nordsjælland 1**.
- ESPN `den.1` summary key events: Nelsson yellow 8'; **Mads Søndergaard 16' (Viborg)**; **Alexander Lind 26' (FCN)**; **Dorian Hanza 33' (Viborg)**; **Charly Horneman 41' (Viborg)**; FCN double substitution at 45'; Viborg triple substitution at 70'; **Adam Kleis-Kristoffersen 81' (Viborg)**.
- ESPN team statistics: **corners Viborg 4, FC Nordsjælland 5 — total 9**; possession 47.7 / 52.3; shots **20 / 14**; shots on target **6 / 2**.

Every settled row is unchanged. **Final 4-1; halftime 3-1; corners 9.** The four first-half goals (16', 26', 33', 41') are confirmed to the minute, so the Rank #1 first-half Under 1.5 was dead by the 33rd minute.

**A pre-game availability error that the 2026-09-20 pass did not catch — this is the most important new finding on this card.**

The card recorded: *"Viborg: Riahi long-term knee injury officially confirmed; current feeds also listed **Anyembe**, Freriks and Njoh unavailable."*

The ESPN confirmed team sheet for this match lists Viborg's starting XI as **Kasper Kiilerich; Daniel Anyembe, Lukas Kirkegaard, Oliver Kristensen, Hjalte Bidstrup, Jeppe Grønning, Mads Søndergaard, Asker Bech, Dorian Hanza, Charly Horneman, Sami Jalal**.

**Daniel Anyembe started.** A player the card carried as unavailable, on the authority of a third-party "current feed", was in the starting eleven. The Riahi absence was sourced to Viborg's own official medical update and was correct; the three additional names came from a non-official feed and at least one of them was wrong.

Materiality: **CONTRIBUTORY, not decisive.** The distribution failure at P-480 was a phase-total and recency-shrinkage failure, and a full-back's presence does not by itself explain four first-half goals. But the direction of the error is exactly wrong for this card — the model was already under-rating Viborg's home attacking capacity, and it was simultaneously subtracting an available starter from Viborg's XI. An availability feed that removes real starters systematically depresses the home side's modelled ceiling. That is a compounding error, not an isolated one.

Classification: this is the **mirror image of the P-481 defect** (a projected XI treated as more confirmed than it was) and the **mirror image of the P-476 success** (an obsolete absence flag correctly removed because the player appeared in the posted order). Three cards in the same mini log, one rule: **an unavailability claim from a non-official aggregator is a hypothesis, and it must be dropped the moment a team sheet contradicts it — and flagged as unverified until then.**

**Ranking metrics.**

| Metric | Model-selected slate | Supplied slate (derived from stated probabilities) |
|---|---|---|
| Rank-1 | **LOSS** (First-half Under 1.5) | **WIN** (1H Over 0.5, 0.609) |
| Hit@2 | **YES** (FCN TT Over 0.5) | **YES** |
| Wins@2 | **1 / 2** | **1 / 2** |
| NDCG@2 | **0.387** (DCG 0.6309 / IDCG 1.6309) | **0.613** |
| Row record | 2 W / 3 L | 2 W / 2 L (both forced pairs) |
| Top over/under | First-half Under 1.5 (Rank #1) — **LOSS**, `TOP_OU_REVIEW` fired and the enhanced review is in the preserved log | FT Under 2.5 (0.502) — **LOSS** |
| Winner call | **LOSS** — FC Nordsjælland, p ≈ 0.411 | — |

This is the mini log's only Rank #1 failure, and the only event where Rank #1 and the top over/under are the same row, so one enhanced review covers both triggers. NDCG@2 of 0.387 is the worst on the card set and correctly reflects that the winning row was the second-ranked one.

**Mandatory validation questions.**

1. **Confirmed starting XIs?** **NO.** The accessible feed labelled both XIs projected, and the card said so. No player prop was promoted, which was correct.
2. **Bench / substitute information?** **NO.** Viborg's triple substitution at 70' produced the 81' fifth goal through Adam Kleis-Kristoffersen, who came on at 70'. A card with no bench cannot represent that path.
3. **Coaching information?** **NOT OBTAINED.**
4. **Injuries / suspensions / withdrawals?** **PARTIALLY, AND ONE ROW WAS WRONG.** Riahi (official, correct) and the FCN absences (Salquist, Araphat Mohammed, Souleymane Alio — none appear in the XI or on the bench, so those were correct). **Anyembe was listed unavailable and started.** Viborg's official preview reported no suspensions, which was consistent.
5. **Were the original sources accurate and current?** **NO — not fully.** The official Viborg and FCN material was accurate. The third-party availability feed was not, and it was used without a label distinguishing official-confirmed absences from feed-asserted ones. `METHOD.md` §1.1 requires `source_class` and `field_owner` on every material input; that was not carried through to the availability rows.
6. **Better sources available?** **YES.** ESPN `den.1` `summary?event=` returns both confirmed XIs, both benches, all substitutions with minutes, goal times and `wonCorners` in one keyless call, and it settles goal *timing*, which is what a first-half phase contract actually needs. Viborg's own matchday squad announcement is the correct pre-game authority for Viborg absences; the third-party feed should be demoted to corroboration only.
7. **Blind spots?** **YES — four, and they compound.** (a) A first-half phase Under built on a small, overlapping goal-timing sample ("FCN's last five league goals all after the 60th minute", "FCN's last two league matches were 0-0 at half") — five goals and two matches is not a basis for 75%. (b) Viborg's own home first-half attacking capacity was never given an independent branch; the phase model was constructed almost entirely from the *opponent's* recent timing. (c) No confirmed XI or bench. (d) The Anyembe availability error, which pushed in the same direction as (b).
8. **How should this be handled in future?** Four specific changes, none of which is a new coefficient. First, **a phase total may not exceed the competition/home-away phase base rate by more than a stated shrinkage allowance when the only supporting evidence is a goal-timing streak of fewer than ~10 events** — shrink hard toward the base rate and say by how much. Second, **model both sides' phase production independently**; a first-half Under requires bilateral suppression evidence, and this card had unilateral evidence. Third, prefer the **structurally shorter path**: 1H Over 0.5 needs one event, 1H Under 1.5 needs the whole half to avoid a second event; when two rows have similar stated probability, the one with fewer failure paths should outrank. Fourth, **label every availability row with its source class** and never let an aggregator-asserted absence into the XI without an official corroboration or an explicit `UNVERIFIED_ABSENCE` tag.

**Verdict on this event.** The enhanced Rank-1 / `TOP_OU_REVIEW` conducted on 2026-09-20 reached the right conclusion — FCN team total Over 0.5 should have outranked the first-half Under on frozen information — and this pass confirms it and adds a fourth contributing cause that the earlier pass missed. The corner model again held up independently of the wrong goal-total direction, landing at 9 against a 7.5 line. Classification: **not variance.** This was a knowable over-confidence built on a small timing sample, compounded by an unverified availability subtraction.

---

#### 2026-09-21 independent re-audit — P-481

**Re-verification of the settled final at the keyless structured lane.**

- ESPN soccer site API, `esp.1` scoreboard for 2026-09-20, event **401882857**: status `Full Time`, **Villarreal 3 — Levante 1**.
- ESPN `esp.1` summary key events: Mandi yellow 13'; **Ayoze Pérez 41'** (assisted by Alberto Moleiro); **Iván Romero 42'** (assisted by Jeremy Toljan); **halftime 1-1**; **Alberto Moleiro 54'** (assisted by Ilias Akhomach); **Georges Mikautadze 86'** (assisted by Moleiro); substitutions Gerard Moreno and Mikautadze **on at 67'**, Nicolas Pépé **on at 79'**.
- ESPN team statistics: **corners Villarreal 7, Levante 1**; possession 62.2 / 37.8; shots **21 / 6**; shots on target **7 / 1**.

Every settled row is unchanged. **Final 3-1; halftime 1-1; Villarreal 7 corners.** The corner field is now confirmed at a registered structured source rather than only at Europa Press / Soccerzz / a Sofascore article.

**The lineup defect identified on 2026-09-20 is confirmed in full, and it is worse than described.** ESPN's confirmed team sheet:

- **Villarreal XI:** Péter Gulácsi; Renato Veiga, Pau Navarro, Sergi Cardona, Alex Freeman; Alberto Moleiro, Nathan Saliba, Pape Gueye; Ayoze Pérez, Tajon Buchanan, Ilias Akhomach.
- **Villarreal bench:** Gerard Moreno, Carlos Maciá, **Georges Mikautadze**, Tani Oluwaseyi, **Juan Foyth**, **Nicolas Pépé**, Luiz Júnior, Rubén Gómez, Logan Costa, Santiago Mouriño, Alassane Diatta, Carlos Romero.

The pregame card described the Villarreal attack as "Pépé, Moleiro, Gerard Moreno and Mikautadze". **Three of those four started on the bench.** Only Moleiro started. Juan Foyth, whose return to availability the card specifically resolved in favour of the fresher same-day source, also did not start. Santi Comesaña, correctly recorded as out, appears in neither the XI nor the bench — so the availability call was right and the **starting-XI call was wrong**.

Set against P-478 in the same mini log, the contrast is exact and instructive:

| Card | Lineup projection method | Result vs confirmed team sheet |
|---|---|---|
| P-478 | Starting XI from each club's **own official report of its last league match**, cross-checked against a current independent feed, published as **projected** | **22 of 22 names correct** |
| P-481 | A **same-day third-party lineup page** (AS), treated as "the freshest accessible lineup state" | **3 of 4 named attackers wrong**; also wrong on Foyth |

"Same-day" is a recency property, not a confirmation property. A same-day page that has not yet ingested the official team sheet is simply a stale projection with a fresh timestamp, and treating it as more authoritative than the club's own last official XI is a source-hierarchy inversion.

**Ranking metrics.**

| Metric | Model-selected slate | Supplied slate (derived from stated probabilities) |
|---|---|---|
| Rank-1 | **WIN** (Villarreal TT Over 0.5) | **WIN** (1H Over 0.5, 0.72) |
| Hit@2 | **YES** | **YES** |
| Wins@2 | **2 / 2** | **2 / 2** |
| NDCG@2 | **1.000** | **1.000** |
| Row record | **5 W / 0 L** | 2 W / 2 L (both forced pairs) |
| Top over/under | Full-game Under 4.5 (Rank #2) — **WIN** | FT Over 2.5 (0.56) — **WIN** |
| Winner call | **WIN** — Villarreal, p ≈ 0.54 | — |

**Why the picks survived a wrong lineup, and why that is not reassurance.** Every model-selected row was a **team-level** target: Villarreal to score at least once, the match to stay under 4.5, Villarreal-or-draw, a first-half goal, Villarreal over 4.5 corners. None of those depends on which individual starts. The territorial thesis — Villarreal's underlying attack being far stronger than its early results — was confirmed emphatically postgame (about 2.90 xG to 0.94, 21-6 shots, 7-1 shots on target, 7-1 corners). **The forecast was right for the right reason and the lineup was wrong at the same time.** Five wins from five is not evidence that the lineup retrieval worked; it is evidence that the targets chosen were robust to it. A single player prop on Pépé, Moreno or Mikautadze would have been built on a false premise.

**Mandatory validation questions.**

1. **Confirmed starting XIs?** **NO — and, unlike every other card in this mini log, this one did not say so clearly enough.** The card described the AS page as "the freshest accessible lineup feed" and used its player list as if it were the attacking structure. The `PROJECTED` label must survive until a field owner or exact-event provider explicitly marks the XI confirmed.
2. **Bench / substitute information?** **NO.** The 86' third goal came from Mikautadze, an unmodelled 67' substitute; the 79' introduction of Pépé is likewise a bench event. Two of Villarreal's three goals involved players the card had placed in the starting XI and who were in fact substitutes.
3. **Coaching information?** **NOT OBTAINED.** Villarreal had short rest after a Sep 17 Málaga fixture and Levante's midweek Athletic game had been postponed — a rotation-relevant asymmetry the card did identify. Villarreal did in fact rotate. The card had the *reason* to expect rotation and still published a non-rotated XI.
4. **Injuries / suspensions / withdrawals?** **YES and correct.** Levante's official call-up ruled out Álex Primo, Karl Etta Eyong and Hugo Sotelo — none appear. Comesaña out and Foyth available were both correct as **availability** statements. The card conflated availability with selection.
5. **Were the original sources accurate and current?** **MIXED.** LaLiga official, the Villarreal calendar, the Levante official call-up, StatMuse and MatchPulse were all accurate. The AS lineup page was not accurate as a team sheet and was over-weighted.
6. **Better sources available?** **YES.** ESPN `esp.1` `summary?event=` provides both confirmed XIs, both benches, every substitution with its minute, goal times with assists and `wonCorners` — one keyless call that would have settled every field this card had to assemble from four separate providers. For pre-game use, the confirmed XI appears in the same `rosters` block once the team sheet is published (typically one hour before kick-off), which is a cleaner confirmation gate than reading a newspaper lineup page.
7. **Blind spots?** **YES — two.** (a) Lineup confirmation state, as above. (b) The total centre of ~2.98 was slightly low against a realised four goals, but the distribution retained enough upper-tail mass for Under 4.5 and Over 2.5 to coexist, so this is a minor calibration observation rather than a failure.
8. **How should this be handled in future?** One hard rule, which already exists and was not executed: **a lineup may only be labelled confirmed when the source explicitly exposes a confirmation marker or is the club/league team sheet itself.** Add one operational test that makes the rule self-enforcing: before publishing a projected XI, check it against the club's own most recent official match report; where the two disagree, publish the union with both labelled, and never name a specific attacking quartet as "the" structure. Also: when the card has already identified a **short-rest rotation risk**, that is a positive reason to widen the XI uncertainty, not to publish a single XI with more confidence.

**Verdict on this event.** Best raw result in the mini log — 5 W / 0 L on the model-selected slate, correct winner, correct on both supplied directions, and a territorial thesis confirmed by the postgame data. It also contains the mini log's clearest process failure. Both statements are true at once and the record should keep both. Recurring-mistake **M19 (published lineup not retrieved / projected treated as confirmed)** applies squarely.

---
