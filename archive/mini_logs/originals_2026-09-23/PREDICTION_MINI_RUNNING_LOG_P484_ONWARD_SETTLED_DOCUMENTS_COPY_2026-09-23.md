# Prediction Mini Running Log - P-484 onward (settlement and retrospective update)

**Created:** 2026-09-23 (Australia/Sydney). **This revision:** 2026-09-23 ~15:20 AEST.
**Supersedes for working use:** `PREDICTION_MINI_RUNNING_LOG_P484_ONWARD.md` (Drive folder "Mini Prediction Log - P-484 onward - 2026-09-23"). That original file is **not modified**; it stays as immutable evidence.
**Governing method:** MDS-2026.09.19-v4.3 / control revision CR-2026.09.21-3 (read-only from the Sports Research Drive).
**Performance status:** LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE.
**Operating mode:** SPORTS_ONLY / MARKET_BLIND. No odds, operator terms or prices were used in any settlement or review. Every settlement is a research-line grade: NO VALUE DETERMINABLE.
**Next mini-log ID after this revision:** **P-491** (provisional; canonical reconciliation still required).

---

## 0. ID reconciliation performed in this revision (user-directed)

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
- The P-490-onward mini log must show **P-491** as its next ID when it is next used. That file was not edited by this task.

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

## 2. Temporary-ID / Canonical-ID Conflict Logs

- **No entry currently needs a temporary ID.** The P-484 collision is resolved by §0. The WNBA, NFL, MLB-MIN-SF, WTA and NPB cards now carry their own provisional numbers. Their former TMP aliases are retained in the headings.
- **Outstanding reconciliation items**, carried to canonical import:
  1. **REVIEW-P487-GAP:** P-487 unassigned. Confirm at import whether another external variant claimed it before any number is reused.
  2. **REVIEW-PART5-SNAPSHOT:** Part 5 still lists P-482 as next.
     - P-482/P-483 are settled per `IMPLEMENTED_CHANGES_2026_09_23` but are not yet in canonical custody.
     - P-484–P-490 in this log sit above them.
     - Import P-482/P-483 first, then this log in ID order.
  3. **REVIEW-HORIZON:** Several cards stay learning-only whatever their canonical number:
     - P-485 (NFL) and P-490 (Padres) are START_CROSSED / PREGAME STATUS UNVERIFIED.
     - P-489 (NPB) is ISSUE_HORIZON_UNVERIFIED.
  4. **REVIEW-P490-PROP-BOX:** Re-capture the official MLB box-score pitching line for Michael King (gamePk 823897) at import.
     - The outs figure used below comes from two independent recaps, consistent with the official linescore.
     - The official boxscore endpoint returned a stale cached snapshot at settlement time.

---

## 3. Fully Settled Logs (ID order)

### Summary table

| ID (alias) | Event | Final | #1 | #2 | #3 | #4 | Winner call | Rank-1 | Hit@2 | NDCG@2 | TOP_OU_REVIEW |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P-484 (TMP-…WNBA-ATL-NYL) | Dream @ Liberty | ATL 95–84 | Under 177.5 **L** | ATL −1.5 **W** | NYL +1.5 **L** | Over 177.5 **W** | ATL ✔ | L | Y | 0.387 | YES |
| P-485 (TMP-…NFL-NYG-LAR) | Giants @ Rams | LAR 28–6 | NYG +6.5 **L** | Under 47.5 **W** | Over 47.5 **L** | LAR −6.5 **W** | LAR ✔ | L | Y | 0.387 | NO |
| P-486 (TMP-…MLB-MIN-SF) | Twins @ Giants | SF 5–2 | MIN ML **L** | SF +1.5 **W** | Under 8.0 **W** | Over 8.0 **L** | MIN ✘ | L | Y | 0.387 | NO |
| P-488 (TMP-…WTA-WOLFF-OLI) | Wolff v Oliynykova | Oli 6–1 7–6 | Under 20.5 **W** | Wolff +4.5 **L** | Oli −4.5 **W** | Over 20.5 **L** | Oli ✔ | W | Y | 0.613 | NO |
| **P-490** (formerly local P-484) | Padres @ Dodgers | **LAD 7–0** | King O14.5 outs **L** | SD +1.5 **L** | LAD ML **W** | Over 8.5 **L** | LAD ✔ | **L** | **N** | **0.000** | **YES** |

- Binary NDCG@2 = (rel₁ + rel₂/log₂3) / (1 + 1/log₂3).
- Descriptive only. The P-485, P-490 and P-489 horizons are unverified.
- None of this is performance evidence.

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
- `IMPLEMENTED_CHANGES_2026_09_23` records **P-483**, where the Kalieva **+4.5 handicap lost** while Volynets -4.5 won. That is **two consecutive WTA cards** in which the underdog +4.5 games handicap lost, while the preferred Under won in both.
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

# General Learnings, Rule Changes, Observations, and New Sources

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
  - In both, the underdog +4.5 games handicap lost while the Under won and the favourite won in straight sets.
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

No Google Drive governing document, canonical log or prior mini log was modified. This file was uploaded as a **new** file alongside the original.

| Finding / disposition | Target document (later, if evidence warrants) |
|---|---|
| §0 ID resolution (Padres → P-490; WNBA → P-484; P-487 gap; next P-491) | `PREDICTION_LOG_COMBINED_5.md`, `GAME_LOG_STATUS_CURRENT.md`; next-ID note for `PREDICTION_MINI_RUNNING_LOG_P490_ONWARD.md` |
| Import order (P-482/P-483 first, then P-484–P-490) | `EXTERNAL_LOGGING_WORKFLOW.md` (atomic registration checklist) |
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

**Proposed new document (not created):** `ISSUE_HORIZON_REGISTER.md`. It would be one table per card: scheduled start (venue-local and Melbourne), freeze timestamp, first-pitch/kick-off timestamp, and horizon label. Its purpose is to let canonical import filter START_CROSSED cards mechanically, since horizon failures are this log's most frequent defect.

---

## Settled logs (first to most recent)

1. **P-484** — WNBA — Atlanta Dream @ New York Liberty (alias TMP-20260923-WNBA-ATL-NYL) — ATL 95–84 — settled
2. **P-485** — NFL — NY Giants @ LA Rams (alias TMP-20260923-NFL-NYG-LAR) — LAR 28–6 — settled; START_CROSSED
3. **P-486** — MLB — Minnesota Twins @ San Francisco Giants (alias TMP-20260923-MLB-MIN-SF) — SF 5–2 — settled
4. **P-488** — WTA Singapore — Wolff vs Oliynykova (alias TMP-20260923-WTA-WOLFF-OLI) — Oliynykova 6–1 7–6 — settled
5. **P-490** — MLB — SD Padres @ LA Dodgers (formerly local P-484) — LAD 7–0 — settled this revision; START_CROSSED
- Unscored record: REQUEST-ONLY-NBL-TAS-SEM — Tasmania 96–91 — result verified; no forecast, no ID

## Logs still awaiting settlement (first to most recent)

1. **P-489** — NPB — Chunichi Dragons @ Yokohama DeNA BayStars — UPCOMING (18:00 JST = 19:00 AEST, 23 Sep 2026); ISSUE_HORIZON_UNVERIFIED

Unassigned: **P-487** (gap preserved). **Next ID: P-491.**

All records in this mini log remain **LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE**.
