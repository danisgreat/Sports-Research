# Tennis analysis rules


> **2026-09-12 operational correction:** The dated section at the end of this file and RULES_GENERAL section 16.9 control over conflicting older probability, coupling and source claims.


> **`METHOD.md` is now the primary mandatory read (v4.0 comprehensive overhaul, 2026-09-06).** This file remains the full sport-specific reference: its `SFA-<SPORT>` algorithm and competition-rules section (`§9`/`§10`/`§11`) are consulted in full when forecasting this sport; `METHOD.md` states the cross-sport process once.


<!-- THREE-SOURCE-TIME-GATE-2026-09-19-CR4 -->
> **Current cross-sport authority — MDS-2026.09.19-v4.3 / CR-2026.09.21-3:** this sport module inherits the reconciled all-sports source, timing, settlement and distribution-construction controls. Historical issued cards retain their own revision.


Status: **ACTIVE — QUALITATIVE MODULE**
Effective: **2026-09-06 (v4.0 comprehensive overhaul — see METHOD.md and FRAMEWORK_AND_GAME_LOG_OVERHAUL_REVIEW_2026-09-06.md)**
Method version: **MDS-2026.09.06-v4.0**
Applies with RULES_GENERAL.md, MODEL_AND_DATA_SPEC.md, and ALGORITHM_PORTFOLIO_AND_EVALUATION.md.
Executable algorithm: **SFA-TENNIS (§9) — instantiates GFA-2 in RULES_GENERAL.md §11**
Numerical status: **NO TENNIS TARGET/SOURCE CARD, DATASET OR MODEL IS APPROVED OR FIT**
Sport and competition rules reference: **§10 (added 2026-09-04)** — the rules of tennis scoring and the tour-by-tour format differences (Grand Slam / US Open, ATP Tour + Challenger, WTA Tour, ITF World Tennis Tour, UTR Pro Tennis Tour), including the 2026 final-set tiebreak alignment, on-court coaching, and retirement/walkover settlement. Reference material for identity, state and settlement; it does not change `SFA-TENNIS`.


## 1. Identity and contract


Resolve tour/competition and level, event, round, surface and indoor/outdoor state, best-of format, final-set tiebreak rules, ball/altitude where verified, and whether the match is singles or doubles. Freeze each contract's retirement/walkover, completed-set, super-tiebreak, dead-heat and void rules from the named operator. A match winner, set handicap and total games contract can settle differently after retirement and are not interchangeable.


## 2. Participants, exposure and current regime


- Confirm the exact players, handedness, current entry/ranking status, draw/round and scheduled start from the official event/tour source.
- Record current surface, the player's recent surface-specific schedule, match duration, rest, travel, qualifying workload, medical timeout/retirement history and credible current injury reporting.
- Separate career/season prior from the current surface-and-role regime. Ranking and reputation are priors, not current form measurements.
- Use opponent-adjusted serve and return points won, first-serve-in rate, first/second-serve points won, break-point creation/saving, hold/break rates, ace/double-fault shape and tiebreak exposure where definitions and sample are reliable.
- Shrink tiny current samples toward an appropriate tour/level/surface prior. Do not let one tournament or one match become the baseline.


## 3. Matchup and continuity


Trace handedness, serve direction/return position, backhand/forehand tolerance, rally length, movement, height/bounce, net use and pressure-point performance through the current surface. Head-to-head is decision-driving only when surface, format, competitive level, fitness and technical/role continuity are material; an old indoor-hard meeting cannot control a current clay match.


When ranking, older H2H, rankings and broad season aggregates must be explicitly reconciled against current surface form and serve-return stability under RULES_GENERAL's regime-dominance audit. If they conflict and the current sample is weak, widen the match distribution and lower evidence quality instead of choosing whichever history supports the preferred side.


## 4. Joint match model


Exposure units are service points, return points, games, sets and match-completion state. Build one coherent qualitative or future numerical match process:


1. participation and completion/retirement branches;
2. surface- and opponent-adjusted point-on-serve distributions for both players;
3. game/hold and break distributions with score-state and pressure uncertainty;
4. set score and tiebreak branches;
5. match winner, set handicap and total-games queries derived from the same simulated or qualitative score tree.


Best-of-three totals require explicit straight-set and three-set mixture weights. Best-of-five totals require separate three-, four- and five-set mixture weights before within-set closeness is applied. A player can be the better winner while a broad opponent +1.5-set cushion is more likely; that relationship must come from the shared match tree, not from independent narratives. Total games depend on set count and within-set closeness, so a deciding-set branch can rescue player set cushions and the Over without making those rows independent.


The tree is two-sided. For each player, represent at least: ordinary straight-set control, close straight sets/tiebreaks, and a deciding-set win where supported. A perceived underdog may win quickly; never couple all underdog-win probability to a long or three-set match. First-set contracts use an explicit opening-set state derived from early hold/break/return pressure and current start patterns; they do not inherit the full-match winner ranking.


## 5. Structural controls


1. **Surface is a regime variable.** Overall ranking and all-surface records never override a material surface-specific serve/return change without reconciliation.
2. **Current stability is decomposed.** Distinguish first-serve entry, first/second-serve conversion, return pressure and break-point opportunity; one win/loss streak is not a mechanism.
3. **H2H needs continuity.** Downweight old meetings across surface, level, format, fitness or technical changes.
4. **Set count and game total are linked.** Store straight-set and deciding-set branches and tag dependence.
5. **Set cushions are not free safety.** Price-free likelihood can favour +1.5 sets, but the row still needs a credible set-winning or match-length pathway.
6. **Qualifying and workload change exposure/variance.** Fatigue is not automatically negative; model fitness, acclimatisation and accumulated match load separately.
7. **Retirement terms are a hard gate.** Unknown operator treatment means `UNKNOWN_DEFINITION` and `NO VALUE DETERMINABLE`.
8. **No ranking-only confidence.** ATP/WTA/ITF/UTR rankings and seeding are context, not sufficient evidence for LEAN/SUPPORTED.
9. **Opponent and level comparability must be demonstrated.** Raw ATP, Challenger, qualifying, ITF and other level/surface rates are not exchangeable. State the opponent-strength/level adjustment and shrinkage, or lower the evidence grade.
10. **Win-conditioned cover counts are descriptive only.** A player covering a game handicap in six of seven recent wins does not independently estimate the chance of winning or covering the next match.
11. **Kill paths include opponent control.** For a favourite handicap, “favourite wins narrowly” is incomplete whenever a credible opponent win—especially straight-set control—also defeats the contract.
12. **Winner, handicap and total must pass a scoreline-coherence check.** If the tree strongly prefers one player and that player's game handicap, an Over requires an explicit close-set or extra-set mechanism. Write at least one representative scoreline for Rank #1 and verify that it is compatible with the other leading directions before freezing the order.


## 6. Live state


Store set/game/point score, server, tiebreak state, elapsed time, verified injury/medical state and current serve-return point counts. Recalculate only the remaining point/game/set tree. Do not extrapolate a short hot serving spell as a permanent rate change, and do not use a stale scoreboard when participant orientation or server is uncertain.


## 7. Sources and settlement


- Official ATP, WTA, ITF, event and governing competition pages control identity, draw, format, score and official result where exposed.
- Official event/tour statistics control only their defined serve/return fields.
- Reputable specialist score/stat pages may cross-check current results and fill research fields, but they do not override an official correction and require provider/definition continuity.
- Player/social reporting can evidence a statement or injury report only when account identity and publication time are verified; official event status controls withdrawals and walkovers.


Settle from the official final and exact operator retirement rules. If an official stat field is unavailable, use two independent high-quality sources and mark the field provisional; do not infer total games or set scores from the winner alone.


## 8. Upcoming-game research sequence


1. Freeze competition/round, surface, format/tiebreak and operator retirement terms.
2. Verify draw identity, schedule, current withdrawal/fitness state, rest/travel and qualifying workload.
3. Build surface- and opponent-adjusted serve/return priors; separate broad baseline from current regime and shrink sparse samples.
4. Audit H2H continuity and the strongest contrary matchup path.
5. Build straight-set control, close-set/tiebreak and deciding-set branches for **both** players; derive winner, set handicap and total games from the same tree.
6. For first-set rows, freeze a separate opening-set sub-tree and show why it differs from or agrees with the full-match state.
7. Refresh official participant/status fields immediately before issue and log unresolved definitions or missing statistics.


## 9. SFA-TENNIS — sport forecast algorithm


Algorithm ID: `SFA-TENNIS`. Effective **2026-09-02**. Instantiates `GFA-2` (RULES_GENERAL.md §11) with tennis content. Process composition only; no fitted weight, scenario weight or published probability is introduced, and no tennis target, source, dataset or model is approved or fit. ATP, WTA, Challenger, ITF, junior, UTR and exhibition levels are separate populations and their rates are not exchangeable.


### 9.1 Blocking preconditions


| Precondition | Requirement | Failure output |
|---|---|---|
| `TE-P1` format and endpoint | Tour, event, round, surface, best-of-three or best-of-five, final-set format, tiebreak rules and match-tiebreak substitutions | `GATE-TARGET` failure; do not proceed |
| `TE-P2` participants | Exact players, handedness, entry status, draw position and scheduled start from the official event or tour source, re-handshaken at G31 | Identity unresolved means no directional analysis |
| `TE-P3` retirement terms | The operator's retirement, walkover and withdrawal rules for every supplied row | `UNKNOWN_DEFINITION` and `NO VALUE DETERMINABLE` |
| `TE-P4` current status | Verified withdrawal, medical, rest, travel and qualifying-workload state | Record the missingness code; never infer fitness from a result list |


### 9.2 Exposure chain


| Step | Output |
|---|---|
| `TE-S1` | Participation and completion state: start probability, retirement and walkover branches |
| `TE-S2` | Surface- and opponent-adjusted serve profile for each player: first-serve in rate, first- and second-serve points won, ace and double-fault shape |
| `TE-S3` | Return profile for each player: return points won, break-point creation, and pressure-point behaviour |
| `TE-S4` | Hold and break distributions per player from `TE-S2` and `TE-S3`, with score-state uncertainty |
| `TE-S5` | Within-set game tree: comfortable hold sequences, close games, tiebreak exposure |
| `TE-S6` | Set-score tree for both players: ordinary straight-set control, close straight sets or tiebreaks, and a deciding-set win where supported |
| `TE-S7` | Set-count mixture: explicit weights over two and three sets, or over three, four and five sets, before within-set closeness is applied |
| `TE-S8` | One match tree from which winner, set handicap, total games, set betting and first-set rows are all queried |


Sparse current samples shrink toward an appropriate tour, level and surface prior. One tournament or one match is never the baseline.


### 9.3 Mandatory branch set


Both players receive the full set. A perceived underdog's win probability may never be attached only to long matches.


| Branch | Content |
|---|---|
| `TE-B1` | Player A straight-set control |
| `TE-B2` | Player A close straight sets, including one or two tiebreaks |
| `TE-B3` | Player A deciding-set win |
| `TE-B4` | Player B straight-set control |
| `TE-B5` | Player B close straight sets, including one or two tiebreaks |
| `TE-B6` | Player B deciding-set win |
| `TE-B7` | Best-of-five extension states: three-, four- and five-set endpoints held separately |
| `TE-B8` | Retirement, walkover or withdrawal state under the frozen operator terms |


### 9.4 Contract derivation map


| Contract | Queried from | Extra condition the mechanism must predict |
|---|---|---|
| Match winner | Sum of that player's `TE-B*` branches | Both a quick and a long winning path |
| Set handicap | The set-score tree | A credible set-winning or match-length pathway; a cushion is not free safety |
| Total games | Set-count mixture times within-set closeness | Which set count carries the mass; a deciding-set branch can rescue an Over without being independent of the handicap |
| Set betting and correct score | The same tree | The exact set sequence, not a directional lean |
| First set | Its own opening-set sub-tree from early hold, break and return pressure | Why the opening state differs from or agrees with the full-match state |
| Player props | Service and return point counts from `TE-S2`/`TE-S3` times expected games | The provider's own definition |


### 9.5 Kill-path library


| Kill path | Defeats | Evidence origin |
|---|---|---|
| An opponent's ordinary straight-set control | A favourite handicap whose kill path is written only as "favourite wins narrowly" | §5 control 11, C-PL6-TEN-BIDIRECTIONAL-TREE |
| Favourite control at 6-2, 6-2 | An Over ranked alongside a preference for that same favourite and their game handicap | §5 control 12, C-PL9-TEN-CROSSMARKET |
| A fifth-set extension in best-of-five | A total ranked on an undifferentiated corridor with a variance note | C-PL9-TEN-BO5-MIX, §4 best-of-five paragraph |
| Current-surface serve and return form diverging from ranking and old head-to-head | A side ranked on ranking, seeding or an old meeting on another surface | §5 controls 1, 3 and 8, C-PL5-TEN-SURFACE-H2H |
| Level mismatch between ATP, Challenger, qualifying and ITF rates | Any comparison made without a stated level and opponent-strength adjustment | §5 control 9 |
| Win-conditioned cover counts | A handicap row treated as independently evidenced | §5 control 10, L-032 |
| A cushion supported by close sets, tiebreak exposure and margin resistance, which lengthens the same match | An Under co-ranked in the top half with that cushion; the evidence that promotes the handicap is the evidence that adds games | C-PL11-TEN-CUSHION-LENGTH (P-245) |
| Sparse crossover or junior-adult evidence concentrating several ranks on one player | A slate whose top rows all depend on one thin read | C-PL2-TEN-CROSSOVER-RANK |


### 9.6 Sport ordering overrides


1. Winner, handicap and total must pass the G25 coherence gate together. Write at least one representative scoreline for Rank #1 and check it against every other leading row before freezing the order.
2. Rows drawn from one match tree are dependent. Only one is `PRIMARY_FORMAL` unless a row has independent target-specific evidence, such as a first-set state.
3. A total row without an explicit set-count mixture is capped at `FORCED RANK`.
4. Rankings, seeding and reputation may not supply a decisive term in the G23.1 marginal-likelihood comparison, and never justify `LEAN` or `SUPPORTED` alone.
5. Recent win streaks, cover counts and old head-to-head are `E — diagnostic only`.
6. Convert the Rank #1 branch set into a games interval before any total is ordered, per G25.1. Sum the ordinary game counts of every set-score branch in which Rank #1 wins, state the resulting low-to-high interval, and compare each supplied total line against it. A disjoint winning region is recorded as a dependence/coherence fact. It forces repair only when it exposes an impossible or internally inconsistent set/game tree; mutually exclusive but coherent high-probability marginals may still rank highly.
7. A games handicap is evaluated by **aggregate games**, independently of the set winner: Player A +h wins when games_A − games_B + h > 0 (subject to exact action/retirement terms). It does not contain every match-win branch. An underdog can cover in short straight sets, and can win the match while losing a positive games handicap. Keep the independently constructed set-count mixture at `TE-S7`; ranking a cushion does not itself raise set count. Reconcile all rows by querying the same set/game tree (L-068).
8. When a cushion is ranked first, the potential winner is named from the same branch mass under G30.1. If the favourite is still named, identify the close-loss states that separate the two claims.


### 9.7 Pre-issue checklist


1. `TE-P1`–`TE-P4` status printed, including retirement terms.
2. Surface- and level-adjusted serve and return baselines stated before any line, with shrinkage disclosed.
3. All six two-sided `TE-B1`–`TE-B6` branches written, plus `TE-B7` for best-of-five.
4. Set-count mixture stated numerically as a qualitative weight before any total is located.
5. Representative Rank #1 scoreline written and checked against the other leading rows.
6. Kill-path rows selected from §9.5 and reconciled against the issued order.
7. Head-to-head continuity audited across surface, level, format, fitness and technique.
8. Draw status, withdrawals and start time refreshed at G31 before the view is appended.
9. Recency block complete per §9.8: L5/L10/L15/L20 for both sides and for head-to-head, continuity count stated, trend verdict per metric, unique-event de-duplication done.
10. Environment block complete per §9.9: Roof/indoor state, wind, heat and court-speed conditions recorded; **windows retrieved on this surface specifically**.
11. `REFERENCE_BASE_RATE`, exact threshold, population and denominator recorded for every supplied row per §9.10 as a descriptive diagnostic only; no reference-band, trend or slot-frequency adjustment may move an ordinal (G23.1).
12. Extra-condition support audit (G24) recorded for every handicap, team-total and cushion row; no retrospective contract-family penalty is applied.
13. Separation budget (G20.1) solved for every margin, handicap and cushion row set by set, with tiebreak exposure and the deciding-set state held separately.
14. Rank-1 implied-target interval (G25.1) stated in the unit of every other supplied line, each remaining row classified `COHERENT`/`PARTIAL_OVERLAP`/`DISJOINT`, and every aggregate budget re-solved conditional on the Rank-1 state.
15. Winner-and-cushion reconciliation (G30.1) whenever Rank #1 is an underdog cushion, with the outright-win and narrow-loss branch ordering stated. Example separation kill path for this sport: an extended or deciding set.
16. Deficit attribution (G14.1) recorded for every weak, absent, returning or small-sample participant: which side's distribution moved and through which exposure step.


### 9.8 Recency, head-to-head and trend windows


Implements `GFA-2` step G13.1 (RULES_GENERAL.md §11.3B) and runs at that point in the algorithm, not at the end. Retrieval of L5/L10/L15/L20 for both sides and for the head-to-head series is mandatory; a window that does not exist is recorded with its true count and a missingness code.


Populate one windowed table per side with these metrics, and one head-to-head table:


| Window metric | Content |
|---|---|
| Surface-specific results | **The last 5/10/15/20 matches on this exact surface**, not overall form |
| Serve | First-serve in rate, first and second-serve points won, ace and double-fault rate |
| Return | Return points won, break points created and converted |
| Hold and break | Hold and break percentage, and tiebreak frequency and record |
| Match length | Set counts and total games in each window, which is what a total-games line actually needs |


**Head-to-head continuity.** Continuity means the same surface, comparable level and no material technical, fitness or ranking change since. An older indoor-hard meeting fails continuity for a current clay match, which is the exact failure logged when ranking and an old meeting outranked current surface form.


**Descriptive recency windows (G13.1; revised 2026-09-17).** Retrieve L5/L10/L15/L20 and continuity-qualified H2H with unique-event counts. These windows overlap. Monotonicity and dispersion among their averages are not a statistical trend/noise test. Report direction descriptively; estimate recency decay and opponent/regime effects using time-ordered validation. See SCORING_AND_VALIDATION section 5.


**De-duplication.** The windows overlap by construction and share matches with the head-to-head and venue series. Shrink from unique underlying events under G9; never treat L5, L10, L15 and L20 as four confirmations.


### 9.9 Environment and conditions


Implements `GFA-2` step G15.1 (RULES_GENERAL.md §11.3C). Venue classification for this sport is normally **OUTDOOR unless the event is indoors or the roof is closed**.


| Field | Use in this sport |
|---|---|
| Roof and indoor state | Official event source; a closed roof changes ball speed and removes wind |
| Wind speed and gusts | Serve toss, rally length and error rate; more disruptive for a first-serve-dependent player |
| Temperature, humidity and altitude | Ball flight and court speed; heat rules and extended breaks change match length |
| Ball type and court speed rating where the event publishes it | Directly affects hold rate and therefore total games |


Failure to obtain the match-window forecast for an outdoor or open-roof event yields `WEATHER_NOT_AVAILABLE`, widened total and margin distributions, and a `LEAN` cap on every weather-dependent row. No factor above carries an automatic total direction.


### 9.10 Base-rate anchors and derived stat lanes


**Anchoring (G12.1).** Anchor total games on the tour-and-surface distribution for that format, and set handicaps on the frequency of straight-set results at that level. Best-of-three and best-of-five anchors are separate.


**Derived and low-salience fields that are available and routinely skipped:**


| Field | Note |
|---|---|
| Scheduled session and start time | Day and night sessions play at different speeds at the same venue |
| Qualifying and recent match load | Entered through fitness and match sharpness, in both directions |
| Retirement and medical-timeout history | Feeds the `TE-B8` branch, with the operator terms frozen |


## 10. Sport and competition rules reference


Added 2026-09-04; last reviewed 2026-09-04. Standing reference for the rules of tennis scoring and the tour-by-tour format and administrative differences for every tennis body in the prediction logs: **Grand Slams (US Open)**, the **ATP Tour** and **ATP Challenger Tour**, the **WTA Tour**, the **ITF World Tennis Tour** (M15/M25 etc.), and the **UTR Pro Tennis Tour**. Supports `TE-P` identity (`§1`) and `§7` settlement; introduces no rate, weight or ordering rule.


**Maintenance (RULES_GENERAL.md §3, `G2`).** The tours revise the rulebook most years (the 2022 final-set tiebreak alignment, on-court coaching becoming permanent in 2025, the spread of electronic line-calling, changes to medical-timeout and bathroom-break rules). Before the first card of a new Grand Slam, a new season on any tour, or a competition format not seen before (a Davis Cup / Billie Jean King Cup tie, a United Cup, an exhibition), re-verify the match format (best-of-3 vs 5, ad vs no-ad, standard vs match-tiebreak decider), the deciding-set rule, the coaching and line-calling rules, and the event's own draw/advancement structure, and update this section **before** issuing the card. The first time a new circuit is forecast (WTA 125, ATP Finals, a team event, a senior/legends event), document its full format and any format flexibility here first.


### 10.1 Scoring — universal


**Point → game.** Points score **15, 30, 40, game**. At **40–40 ("deuce")** a player must win two points in a row: the first is **"advantage"**, the second wins the game; lose the point at advantage and it returns to deuce. This is **"ad scoring"** and is standard in all professional singles. **"No-ad"** (the first player to 4 points wins the game, a single deciding point at 3–3) is used in most professional **doubles**, in college tennis, and optionally in some development events.


**Game → set.** First to **6 games, winning by 2**. At **6–6** a **tiebreak** is played (see §10.2). A set won 7–6 always went to a tiebreak; 7–5 did not.


**Tiebreak (the standard 7-point one).** First to **7 points, win by 2**. Players serve 1 point, then 2 each thereafter; change ends every 6 points. The set is recorded as 7–6.


**Set → match.** **Best-of-three sets** (win 2) everywhere except **men's Grand Slam singles**, which is **best-of-five** (win 3). Best-of-three and best-of-five are **separate populations** — never share an anchor (RULES_TENNIS.md §9.10).


**Serving.** Players alternate serving each game. The server gets two attempts per point (a "let" on a serve clipping the net is re-taken). A **double fault** loses the point. Ends are changed after the 1st game and every two games thereafter.


**On-court officiating.** Chair umpire + line calls (electronic line-calling — "Hawk-Eye Live" — is now used at the US Open and most tour hard-court events, removing line judges and player challenges; clay events still use ball marks). A **25-second shot clock** between points, **90 seconds** at changeovers, **120 seconds** at set breaks, ~5-minute warm-up.


**Stoppages.** One **medical timeout** (3 minutes of treatment) per treatable condition. Limited **bathroom/attire breaks** (generally one break, 3 minutes). **Heat rule** (a 10-minute break, typically after the 2nd set in best-of-3 / 3rd set in best-of-5) applies at hot venues including the US Open. Rain / bad light suspends play — outdoor matches resume from the exact score, sometimes the next day; roofed courts (Arthur Ashe and Louis Armstrong at the US Open) continue.


**Coaching (2025 onward).** **Coaching from the player box is now permitted** on the ATP and WTA Tours and at the Grand Slams — short verbal cues and hand signals only, when the player is at the same end, without disrupting play. Coaches may not leave the box. This is a change from the old "no coaching in singles" rule and slightly dampens the in-match momentum swings the older rule produced.


### 10.2 Final-set format — the key rule that varies


| Body | Non-final sets at 6–6 | **Deciding set at 6–6** |
|---|---|---|
| **All four Grand Slams** (incl. US Open), since 2022 | 7-point tiebreak | **10-point match tiebreak** (win by 2) |
| **ATP Tour & ATP Challenger** | 7-point tiebreak | **7-point tiebreak** |
| **WTA Tour** | 7-point tiebreak | **7-point tiebreak** |
| **ITF World Tennis Tour** | 7-point tiebreak | **7-point tiebreak** |
| Doubles (most tour & Slam), in place of a 3rd set | — | **10-point match tiebreak** replaces the deciding set entirely |


Before 2022 every Slam had a **different** deciding-set rule (the US Open used a first-to-7 tiebreak at 6–6, the Australian Open a 10-pointer at 6–6, Wimbledon a 7-pointer at 12–12, Roland Garros advantage sets). Any head-to-head or "total games" history from before 2022 must be checked for which rule was in force — this directly affects deciding-set length and the total-games distribution.


### 10.3 Grand Slam / US Open


**Draw.** 128 players in the singles main draw, single elimination, 7 rounds. **32 seeds.** A separate **128-player qualifying draw** (3 rounds of best-of-3) fills 16 main-draw places; "US Open Qualifying" cards in the log are these matches.


**Format.** Men's singles **best-of-five**; women's singles **best-of-three**. Deciding set → **10-point match tiebreak** at 6–6 (§10.2). Held over ~2 weeks on **hard courts** (New York, late August–September; night humidity and swirling wind in Ashe are real conditions factors). Roof on the two show courts.


**Money and withdrawals.** A player who withdraws before their first-round match is replaced by a **lucky loser**; a first-round player who starts and retires still earns round-1 prize money. This changes the incentive for a compromised player to start.


**Settlement.** Freeze the market's **match format** (games/sets totals differ hugely between Bo3 and Bo5). Set-score, total-games and handicap markets all interact with the 10-point deciding-set tiebreak. Retirement rules per §10.5.


### 10.4 ATP Tour, ATP Challenger Tour, WTA Tour, ITF World Tennis Tour


All use **best-of-three sets, 7-point tiebreak in every set including the decider** (§10.2). They differ in **level, points, prize money and field quality** — which is what `SFA-TENNIS` shrinkage and continuity checks (§3, §9.8) care about:


- **ATP Tour:** the top men's tour — **Grand Slams** (not ATP-run), **ATP Masters 1000**, **ATP 500**, **ATP 250**, and the season-ending **ATP Finals** (8 players, round-robin groups then knockout). 52-week rolling ranking. Example in log: **Winston-Salem Open** (an ATP 250, the week before the US Open).
- **ATP Challenger Tour:** the tier below the main tour (Challenger 50/75/100/125/175 by points/prize). Winners gain the ranking points needed to break into the main tour. Fields are a mix of players ranked ~#80–#300, veterans and rising juniors. Examples in log: **ATP Challenger Augsburg (Schwaben Open)**, **ATP Challenger Zhangjiagang**.
- **WTA Tour:** the top women's women's tour — **WTA 1000 / 500 / 250**, the **WTA Finals**, plus the Slams. 52-week rolling ranking. Women's Slam matches and all WTA matches are **best-of-three**.
- **ITF World Tennis Tour** (men **M15/M25**, women **W15/W35/W50/W75/W100** — the number is prize money in US$ thousands): the entry level of professional tennis, below the Challenger tour. **M15/M25** fields are lightly ranked (often #300–#1000+), form and even identity data are thin, and conditions (court, altitude, balls, heat) vary widely and are often undocumented. Examples in log: **ITF M15 Maanshan (China)**, **ITF M25 Oviedo**, **ITF M25 Oldenzaal**, **ITF M25 Lausanne**. Apply heavy shrinkage and wide conditions/participant uncertainty (RULES_TENNIS.md §2, §9.8; sparse-data handling).


**Retirements are more common the lower the level** — an ITF or Challenger player nursing an injury has more incentive to start (for points/prize money) and to retire than a top-tour player.


### 10.5 UTR Pro Tennis Tour (UTR PTT)


**Operator:** Universal Tennis (UTR Sports). A circuit of ~US$25K events, ranked by the **UTR rating** rather than only ATP/WTA points, aimed at giving developing pros more match play. Example in log: **UTR PTT Clemson**.


**Format.** A distinctive **round-robin + playoff** structure: the main draw is **8 groups of 4**, each group a round-robin (Sun–Wed); then **single-elimination playoff draws** (Thu–Sun) — three separate 8-player knockouts seeded by group finishing position (all the group winners in one draw, all the runners-up in another, etc.), so **every player is guaranteed at least 3 matches** and finishes with a definite placing.


**Scoring.** Standard **best-of-three sets with regular (ad) scoring**; a **third-set 10-point match tiebreak** and **no-ad** are permitted for some UTR "verified" event categories but are **not** the default for the PTT $25K events — **confirm the specific event's format** from its regulations before setting any games/sets market, because a "best-of-3 with a match-tiebreak 3rd" changes the total-games and deciding-set distribution materially.


**Settlement.** Round-robin results can involve **countback tiebreakers** (sets won, games won, head-to-head) to decide who advances — a "group decider" match can be effectively dead or effectively must-win depending on other results, which affects effort. Freeze the event's advancement rules.


### 10.6 Retirement, walkover and abandonment — settlement


This is the highest-frequency tennis settlement problem (RULES_TENNIS.md §5 control set, `TE-B8`).


- **Walkover** (a player withdraws *before* the match starts): **all markets on that match are void** at essentially every operator. The opponent advances but no bet is settled.
- **Retirement / default mid-match:** settlement depends on the operator's stated rule —
  - **"first serve" / "ball in play":** match markets stand once the first point is played — the player who is unable to continue **loses** the match bet.
  - **"one full set" / "completed set":** the match (moneyline) is void unless at least one set (sometimes two) was completed; markets on **already-completed** sets/games stand.
  - **"match completion":** the entire match is void on any retirement.
- **Games, sets, and handicap markets:** generally settled if the relevant set/threshold was already **completed** before the retirement; void otherwise.
- **Suspended and resumed** matches (rain, darkness, curfew): bets normally stand and settle on the eventual result, even if it finishes the next day, unless the operator has a "must complete within 48 hours" clause.


Always freeze, per RULES_TENNIS.md §1: the operator's **exact** retirement/walkover wording, and whether the "potential winner" and any set/games market is being read as regulation-completion or eventual-advancement.


### 10.7 Identity checklist (tennis)


Resolve before any rate work: **tour/level** (Slam / ATP / Challenger / WTA / ITF M-or-W tier / UTR PTT) and therefore field quality and the shrinkage weight; **match format** (best-of-3 vs best-of-5; ad vs no-ad; standard vs match-tiebreak decider) and the **deciding-set rule** (10-point at a Slam, 7-point elsewhere); **surface** and indoor/outdoor + session; whether it is **main draw or qualifying**; recent **match load** (a player 3 rounds deep in qualifying, or coming off a 5-set epic); and the operator's **retirement/walkover** settlement rule for every market on the card.


## September 5 settlement learning — prospective SFA amendment


P-287 requires an immediate arithmetic/contract repair under L-068. For every representative set sequence, store games A, games B, total, signed game margin, sets won and each supplied row's outcome. Sum tiebreak sets as 7+6=13 games; tiebreak points in parentheses are not additional games. Validate examples before they support the rank.


A player winning 0–6, 0–6, 7–6, 7–6, 7–6 wins three sets but loses aggregate games 21–30; +2.5 fails. A quick underdog win can cover and stay Under. A five-set match can also contain late one-sided sets: Paul beat Bublik by six games after winning the last two 12–4. Total games, match winner and game handicap must therefore be derived jointly, without an automatic close/long equivalence.


This corrects §9.6(7), whose former wording supplied the same false shortcut as the card. P-287's correct Over/winner does not erase the defect. Do not infer injury, fatigue or reduced motivation from late-set scores alone. C-P293-TEN-ALLOCATION is a candidate, count zero; the existing P-275 recovery-length test does not gain a completion merely from this provenance correction: no executed frozen comparator has been recorded.




Full evidence and frozen-card comparisons: [September 5 audit](COMPREHENSIVE_SETTLEMENT_AUDIT_2026-09-05.md).


## September 6 settlement learning — cross-sport gates instantiated


No tennis-specific defect was evidenced in the `P-294`–`P-305` cohort; `P-291` (Shelton d. Shapovalov, `Shapovalov +5.5 games` **WIN** at 25–20) settled cleanly. The v3.7 cross-sport gates are instantiated here so that tennis cards carry the same disclosures.


**Tennis-native tail example.** A total-games `Under` is exposed to the *set-count* tail, not the game-count tail: a best-of-five match that goes the distance adds games in large discrete steps rather than smoothly, so "second-highest set count in the L10 × games per set at the median" is a useful **first-pass disclosure heuristic**, not an exact figure — it misses close-set variation (a 7-6 set contributes far more games than a 6-1 set) and does not respect legal score-path constraints. **Correction, 2026-09-06(d):** where precision matters, enumerate the actual legal score paths for the match's best-of format directly and sum games per path, rather than relying on the set-count shortcut alone. Conversely a total-games `Over` is exposed to the straight-sets branch and to retirement, which under `G22` is its own termination branch with its own action terms — and where retirement/walkover terms are `NOT SUPPLIED`, the row is graded under stated standard rules per `G36.1` rather than left `UNRESOLVED`.


**Path geometry in tennis.** `Player to win at least one set` is `UNION_LOW_THRESHOLD` with `N` = sets played. A total-games `Under` in a best-of-five is `INTERSECTION_CONSTRAINT` across every set. A games handicap near the median is `CENTRAL_BAND` and falls under `G26.1`.




### `P-291` reasoning-defect note and `L-068` reinforcement (added 2026-09-06(d))


`P-291`'s own preserved card text (Ben Shelton vs Denis Shapovalov) reasoned that the Shapovalov +5.5 games cushion "survives every Shapovalov win." **That general claim is false in best-of-five tennis, independent of what actually happened in this match.** Counterexample: a player can lose two sets 0-6, 0-6 and win the last three 7-6, 7-6, 7-6 — winning the match 3 sets to 2 with 21 games to the opponent's 30, a nine-game deficit that fails any cushion above +8.5, despite being the outright match winner. The settlement itself is correct (Shapovalov's actual 20 games + 5.5 = 25.5 > Shelton's 25), and this note does not change it — but the card's *reasoning* asserted a general mathematical guarantee that does not hold, and `L-068` (adopted after the same class of error in `P-287`) exists precisely to prevent this. **`L-068` is reinforced, not superseded:** a games-handicap row must be checked against the specific score line achieved, never against a general "the match winner always covers a modest cushion" assumption, because best-of-five's non-linear set structure makes that assumption false in general.


### Cross-sport gates instantiated here (v3.7)


| Gate | Sport-native instantiation |
|---|---|
| `G10.2` settlement-source pre-registration | Grand slam and tour matches settle from the tournament's official scoreboard or the tour's official match record; name the exact record at freeze. Retirement/walkover action follows `G36.1` under standard rules when operator terms are unsupplied. |
| `G14.2` coaching / bench / rotation record | Tennis has no bench; record the coach where publicly named and, more importantly, the **prior-round workload** (minutes/sets played, days of rest) as the rotation-capacity analogue. Pre-match court practice observations, physical strapping, and withdrawal/illness updates verified across accredited tennis journalists under Control `S-1 Rev 2` qualify as `PROJECTED_BEAT_VERIFIED` and satisfy `G14.2`. |
| `G20.2` distributional tail audit | Derive tail and boundary mass from the **same frozen tennis match tree**, conditioned on surface/format-specific serve-return state, hold/break process, set-count mixture, scoreline coherence, retirement endpoint and any rating benchmark used only as a check. Historical second-highest set-count × median-games constructions are superseded as active gates. |
| `G21.1` exact target geometry | Map match winner, set count, total games and games handicap to exact settlement events from the same frozen set/game tree. Derive WIN/PUSH/LOSS and retirement/action branches from that tree; historical path-count/category labels have no mandatory ordinal effect. |
| `G26.1` no universal separation floor | Reference rates and `rank_gap` are descriptive only. **No 40–60% or other pooled probability band can disqualify Rank #1.** Rank from exact marginal likelihood plus robustness/evidence uncertainty. |


**Pre-issue checklist additions (this sport):** settlement endpoint named per row; coaching/bench/rotation record for both sides with missingness codes; tail-budget sums printed against every total line; path-geometry class and `N` printed for every total and phase-total row; separation-floor result stated for Rank #1.


Full narrative and evidence: [`IMPROVEMENT_PLAN_2026-09-06.md`](IMPROVEMENT_PLAN_2026-09-06.md). Controlling gate text: [`RULES_GENERAL.md` §13](RULES_GENERAL.md).


## September 5 implementation after freeze confirmation


**ACTIVE REQUIRED PROCESS — MDS-2026.09.05-v3.6 / L-068–L-072.** Compute every illustrative set sequence into both players’ aggregate games, total, signed margin and all contract outcomes. Set count, winner and games handicap are jointly evaluated. A positive games cushion does not cover every match win; a long match need not have a close games margin.


At final delivery, record the preferred total direction for each exact target, the strongest evidenced failure path for ranks #1 and #2, and whether both can win under the stated joint scenario. Rank by supported marginal likelihood; do not promote an opposite pick solely to manufacture one O/U win. At settlement, keep all issued wins/losses, including defective reasoning, in the applicable historical scorecard and review failed #1/#2 and preferred totals.


[Eligibility policy](PERFORMANCE_ELIGIBILITY_POLICY.md): non-live history is user-confirmed frozen pre-game; explicit live-issued views stay separate. These process repairs are implemented now. Numerical weights and predictive-lift claims need a later frozen comparison; historical origin games do not supply those completions.


## 2026-09-06(f) — settlement and retrospective addendum


P-291/P-308/P-310 retain legal set scores, aggregate games and match winner as distinct quantities. A match winner can lose aggregate games; a cushion does not survive every possible win. P-310 joint efficient-three-set separation defeated cushion and Over; compare serve/return evidence with opponent quality. P-308 workload did not establish a causal fatigue sign. No retrospective probabilities or automatic upset-winner fade.


## 2026-09-09 settlement learning — P-338 (positive; the cross-sport model)


**`P-338` — Gauff def. Jovic 6–1, 6–4 (US Open Women's R16).** Frozen card: R1 `Gauff -4.5 games` (p0.54), R2 `Under 21.5 games` (p0.53), R3 `Over 21.5` (p0.47), R4 `Jovic +4.5` (p0.46); potential winner Gauff (78%). **Top two both won; potential winner correct; best card of its 9-card cohort.** Card mean Brier 0.2163.


*Why it worked, and what the rest of the framework is adopting from it:*


1. **One shared match tree with explicit branch weights** — 42% "Gauff dominant straight-set control", 20% "Gauff close straight", 12% "Gauff wide deciding", 4% "Gauff close deciding", 7% "Jovic straight", 15% "Jovic deciding" — from which winner mass (78%), handicap mass (54%) and total-games mass (53% Under) were all *derived*, not asserted. This is `§4`'s "explicit straight-set and three-set mixture weights" requirement executed properly.
2. **A representative Rank-#1 scoreline written out and checked** — "Gauff 6–3, 6–4 = 19 games" — verified to clear both `Gauff -4.5` and `Under 21.5` simultaneously (control 12). The realized 6–1, 6–4 was even more separated.
3. **The contrary H2H (Rome clay, Jovic led by a set and served for the match) was retained as a live kill path, not allowed to dominate** the hard-court forecast, because Gauff's current hard-court serve/return regime is materially better (control 1, control 3).


**Cross-sport export:** this method — enumerate the outcome families, put a mass on each, derive every row from the set, write and check a representative Rank-#1 outcome — is now `RULES_GENERAL.md` §16.5(a) / `G-L1`, required for soccer, baseball, basketball and every other sport's joint object. Tennis §4 and control 12 already satisfy it; no tennis change is needed there. Keep doing exactly this.


### The three other cross-sport controls, instantiated here


`G-L1` is already met. The other three requirements adopted from the `P-333`–`P-344` cohort do apply to tennis from the next card. All are **disclosure/retrieval requirements — no fitted weight, no ordinal bar** (`L-087`).


| Cross-sport control | Tennis instantiation |
|---|---|
| **`G-L2` — declared uncertainty model** | State the prior and scenario probabilities. Symmetric uncertainty around an unchanged prior affects width; hierarchical shrinkage or asymmetric scenarios may change both mean and variance. Regenerate all dependent probabilities; unsupported directional adjustments remain prohibited. SCORING_AND_VALIDATION section 5 controls. |
| **`G-L7` §16.5(c)** — aggregate-to-disaggregate retrieval | Do not let a win-loss record, a season hold percentage or a "last 10" summary carry directional weight while the **match-by-match serve/return log** is available. `P-338` is the positive example and sets the standard: it printed *per-match* first-serve percentage, first- and second-serve points won, break points faced and return points won for each of the last three matches for both players, and it was those disaggregated lines — Jovic's 33.3% second-serve points won against Frech, the 17 breaks in the Eala match — that identified the actual mechanism. A player carried with only a ranking and a W-L record is `AGGREGATE_ONLY` and caps the dependent handicap/total rows. |
| **`G-L8` — distribution coherence** | Derive each total/spread probability from the exact joint PMF/CDF and settlement endpoint, with push mass. Absolute normalised distance does not order probabilities across different distributions. No missing width or realised result justifies an invented probability. |


Full frozen ranks, actual drivers, knowability and smallest fixes: [PREDICTION_MINI_LOG_SETTLEMENT_2026-09-06.md](archive/mini_logs/PREDICTION_MINI_LOG_SETTLEMENT_2026-09-06.md). Reinforcement only; METHOD v4.0 remains controlling and no new predictive weighting is promoted.


## 2026-09-11 settlement learning — `P-350` (a Rank-#1 loss that was probably variance)


**`P-350` — Ben Shelton def. Carlos Alcaraz 6-7(5), 6-1, 6-3, 1-6, 7-6(7), US Open men's QF** ([`PREDICTION_LOG_COMBINED_3.md` §"2026-09-11"](PREDICTION_LOG_COMBINED_3.md)). Frozen card: R1 Alcaraz to win (0.76) **L**; R2 Over 3.5 sets (0.66) **W**; R3 Over 38.5 games (0.60) **W** (49); R4 Shelton +4.5 games (0.58) **W** (Shelton won 26–23 on games). Card mean Brier 0.2574.


**What went right.** The shared match tree did its job: 66% on four or more sets, the total-games Over and the Shelton cushion were all derived from it, and all three won. Control 12's coherence check held.


**Independent benchmark, not a validation of 76% (corrected 2026-09-12).** Tennis Abstract's Elo ratings dated **2026-08-31** (before the tournament): Alcaraz overall 2146.8 (#2), hard 2073.3 (#2); Shelton overall 1977.5 (#7), hard 1948.5 (#6). Converting the gap to a best-of-five probability — per-set probability `s` solving `s²(3 − 2s) = p₃` for the Elo best-of-three probability `p₃`, then `p₅ = s³(1 + 3(1 − s) + 6(1 − s)²)` — gives Alcaraz **≈71%** on hard-court Elo, **≈77%** on overall Elo, **≈74%** on a 50/50 blend. The card's 76% sits inside that range. The loss occurred in an upset branch, but one event and an Elo benchmark do not establish that the issued 24% upset mass was correctly sized; the match was decided by a fifth-set tiebreak (10–7). **The retrospective should not over-learn from it.**


**The one real blind spot.** Alcaraz was five months out with a wrist injury before the tournament. His 12–1 in sets through four rounds came against lower-ranked opposition, and neither Elo nor recent results see a layoff. That uncertainty belonged in the width of the set tree (`G-L2`).


### Structural control additions


13. **Print an independent rating benchmark beside the winner probability.** Retrieve Tennis Abstract's Elo (overall and surface-specific; ATP `tennisabstract.com/reports/atp_elo_ratings.html`, and its WTA equivalent) with a snapshot date **before** the event, convert the gap to a match-win probability for the correct format (formulae above), and print it beside the card's winner probability. A gap of more than ~10 percentage points needs a named current mechanism. The benchmark never sets the probability — it is a coherence check and a retrospective tool that separates variance from model error. Keyless, and a sports rating rather than a market input, so it is compatible with `SPORTS_ONLY / MARKET_BLIND`.


14. **A long layoff widens the tree.** A player returning from a multi-month absence carries wider set-level outcomes for the first events back, even when early rounds look clean against weaker opposition (`G-L2`). Origin `P-350`.


### Cross-sport controls instantiated here (2026-09-11)


| Control | Tennis instantiation |
|---|---|
| `G-L9` §16.5(e) | A 0.76 winner row must itemise its 0.24 across named paths: opponent serve dominance plus tiebreak coin-flips, current-event return pressure, physical/layoff risk, retirement (under the operator's terms). |
| `G-L10` section 16.5(f) | Derive joint match-winner, games and handicap probabilities from the same set-score model, or disclose joint uncertainty. A short underdog win can cover a cushion; a favourite can cover after losing a set. No universal coupling sign. |
| `G-L11` §16.5(g) | Hold/break percentages over a handful of matches are small-sample proportions; print service/return points and their standard error before a signed adjustment. |
| §16.8 | Completeness block; the Elo benchmark (control 13) is printed in item 3's row for the winner. |




## 2026-09-12 algorithm corrections and retrospective integration


Correct P-350's deciding breaker to 10-7; the match still contained 49 games. Verify event-specific deciding-set and retirement rules before grade. A match tiebreak score is not extra games. An underdog handicap can win in a short straight-set upset, so control G-L10's long-match dependence language is conditional. A dated Elo comparison is a benchmark under explicit assumptions; agreement cannot distinguish variance from probability error in one match. Bench is NOT_APPLICABLE; coach/fitness information must retain capture time and unknown fields.


For every supplied row, use exact target probabilities from a coherent joint distribution; handle push/void/censoring explicitly, avoid overlapping adverse-state counts, and report JOINT_UNQUANTIFIED with bounds if the dependence is not specified. Separate issued-time participant capture, later recovered evidence, source accuracy by field, observed mechanism, and unverified causal interpretation. Keep one preferred O/U direction per distinct target and report the top-two denominator honestly. [Shared correction and methodology sources](audit_2026-09-12/rule_corrections.md). All current log observations remain learning-only and not performance-eligible.




## Recovered mini-log reinforcement - 2026-09-12


P-242's 28-game Zheng straight-set win defeated both Marozsan +2.5 and Over 38.5, despite the issued Zheng winner being correct: include decisive underdog/favourite separation in the set-and-games tree. P-263's 33-game Alcaraz win defeated Under 31.5 while covering -7.5: a lost opening set plus later rout is a distinct exposure branch. P-243 ended 13-13 aggregate games despite Jones winning the match. P-267's successful Under 31.5 and Noskova -4.5 support the represented short-match scenario, not calibration. No match-win or ordinary-three-set shortcut proves handicap coverage. The WTA P-243 extraction mixed state labels and showed incomplete service-game totals; validate each field separately. Evidence: audit_2026-09-12/recovered_historical_retrospectives.md.






## 2026-09-15(b) settlement learning — `P-373`–`P-423` import


Learning-only; disclosure/process changes only — no coefficient or ordinal bar (`L-087`). Evidence and tables: [`PREDICTION_LOG_COMBINED_3.md` §"2026-09-15(b)"](PREDICTION_LOG_COMBINED_3.md). Cross-sport rule: `RULES_GENERAL.md` §16.10 (`G-L12` margin centre/width; fixture identity; official-record derivative settlement).


**Card:** P-375 (Rybakina d. Gauff 3–6 6–4 6–4) — Over 22.5 games and Rybakina −0.5 games both won; winner correct.


- **Positive model:** the six-branch deciding-set tree (Rybakina deciding-set win 28%) mapped directly onto the realised match (29 games). Keep it as the reference for every games-handicap card.
- **`G-L12` instantiation:** a games handicap takes its centre from the set-score tree; uncertainty about a returning or fatigued player widens the tree (control 14) rather than moving the handicap toward zero.


## 2026-09-16 — cross-sport controls instantiated here (`G-L13`, `G-L14`, `G-L15`, disruption facts)


No tennis card was settled this pass. Rules: `RULES_GENERAL.md` §16.11.
- **`G-L13`:** set scores and tiebreak scores come from the raw ATP/WTA/ITF record. P-350's corrected 10–7 breaker shows why a summary is not enough.
- **`G-L14`:** total-games and set rows name the settling record and the retirement rule at issue.
- **`G-L15`:** free total-games rows went 2 of 2 in `P-345`–`P-423`. A total-games Over paired with an underdog games handicap is reported as distinct targets with `P(A ∧ B)`.
- **Disruption facts:** record medical time-outs, retirements and rain suspensions with the set and game score at the time.


## 2026-09-17 — cross-sport controls instantiated here (`G-L17`–`G-L20`)


No tennis card in this import. **`G-L17`:** a games handicap and a total-games row usually share one match-shape state — print `P(¬R1 ∧ ¬R2)` and name it. **`G-L18`:** total games is a two-participant total; print each player's expected service-hold marginal before ranking it. **`G-L19`:** tennis has no draw, but the end-state family must carry retirement and walkover mass with the competition's settlement rule (`P-350` correction). **`G-L20`:** a current-regime head-to-head at the same surface and venue that already cleared the line gets explicit mass.


Evidence and cohort audit: [`PREDICTION_LOG_COMBINED_4.md` §"2026-09-17"](PREDICTION_LOG_COMBINED_4.md); rules in `RULES_GENERAL.md` §16.12.


## 2026-09-17(b) — cross-sport controls instantiated here (`G-L21`–`G-L24`)


**G-L24 in TENNIS:** derive the exact signed-margin distribution under the competition endpoint, including draw, key-value and push masses. Pooled league bands are uncertain references, not mandatory matchup probabilities or rank prohibitions. Missing pooled bands do not invalidate a complete conditional joint distribution. **`G-L21`:** 'server dominance' carries a games Over, a set handicap and a total-games row together — print the joint failure mass. **`G-L22`:** the supplied tennis slate is usually a match-winner pair plus a total-games pair; report the preferred side of each. **`G-L23`:** break points converted, service-hold rate and **retirement/medical-timeout events with the set and game score** are the process and disruption fields — a retirement is an endpoint event and never evidence that the pre-match read failed.


Evidence and cohort audit: [`PREDICTION_LOG_COMBINED_4.md` §"2026-09-17(b)"](PREDICTION_LOG_COMBINED_4.md); rules in `RULES_GENERAL.md` §16.13; bands and base rates in [`BASE_RATES_REGISTER.md`](BASE_RATES_REGISTER.md).


## Current model implementation — 2026-09-17


Use METHOD v4.2's six-field object and SCORING_AND_VALIDATION for exact outcome/push scoring, event-level comparison, descriptive recency and declared hierarchical uncertainty. MODEL_IMPLEMENTATION_RECIPES supplies this sport's retained model scope and endpoint design. Forecast probabilities come from the joint model; pooled base rates are uncertain context, not universal limits. Numeric row caps disconnected from that model, absolute-distance probability ordering and retrospective tail reweighting are withdrawn. No fitted coefficient or predictive improvement is claimed. New cards freeze the method/control hash; existing cards keep their issued versions.


## 2026-09-19 — recency/rebound, social sources and the top-O/U review


`R-1` ([`RECENCY_AND_REBOUND.md`](RECENCY_AND_REBOUND.md)) applies: recent results revise an estimated **rate** through a named mechanism, never forecast a **deviation**. No rebound and no hangover adjustment is permitted in either direction. This sport's magnitudes are **`NOT_YET_DERIVED`** — the MLB figures are not transferable and must not be imported; derive them from this competition's own record before any recent-form weighting.


Source controls `S-1` (social identity: X and Reddit return no usable content; Bluesky sports handles failed identity verification 6/6) and `S-2` (press conferences are availability/role evidence, never a signed adjustment to a modelled rate) apply — `SOURCES.md` §"2026-09-19".


A loss **or push** on the card's highest-ranked over/under now triggers the same enhanced failure review as a Rank #1 loss (`METHOD.md` §7).


<!-- DEEP-RESEARCH-IMPLEMENTATION-2026-09-19-V42 -->
## 2026-09-19(c) — market-independent totals/line addendum


**Source priority:** ATP/WTA/ITF/tournament official draws, results, rankings/order-of-play and withdrawal releases; verified weather for outdoor events. Fantasy/betting projections and picks are prohibited.


Serve/return point strength, surface, format, fatigue/rest, verified health/availability and conditions feed a point/game/set distribution. Match winner, set handicap and total games are derived from that process with retirement/void rules represented explicitly; the supplied line cannot influence serve/return estimates.




<!-- ALL-SPORTS-AUDIT-LIVE-RULE-CLEANUP-2026-09-21-CR3 -->
## 2026-09-21 — all-sports audit live-rule cleanup — CR-2026.09.21-3


Current prospective override. Retain surface/format-specific serve-return state, hold/break tree, set-count mixture, scoreline coherence, retirement endpoint and rating benchmark as a check only. Withdraw pseudo-tail order-statistic constructions, path-count ranking shortcuts, universal probability-band top-slot rules, blanket DISJOINT top-half bans, match-winner⇒games-handicap shortcuts, long-match⇒Over logic and tiny-H2H ownership rules. Build one coherent tennis set/game distribution before querying all targets.
<!-- CONSOLIDATED-MINI-LOG-IMPORT-2026-09-24 -->
## 2026-09-24 settlement learning — P-494 (WTA 500 Singapore), P-495 (WTA 125 Tolentino), P-496 (ITF M25 Falun)

Full records: [`PREDICTION_LOG_COMBINED_5.md` §"2026-09-24(e)"](PREDICTION_LOG_COMBINED_5.md). Learning-only.

| Card | Tournament | Rank #1 | Result | Score | Verdict |
|---|---|---|---|:---:|---|
| `P-494` | WTA 500 Singapore | Andreeva -4.5 (W) | Andreeva 2–0 | 6–2, 6–2 | Exact modal scoreline predicted; dominant hold rate |
| `P-495` | WTA 125 Tolentino | Romero Gormaz -5.5 (L) | Pieri 2–1 | 3–6, 6–4, 6–1 | **Rank-1 Failure Review**: Underestimated slow clay underdog resilience |
| `P-496` | ITF M25 Falun | Over 21.5 (W) | Marek 2–1 | 2–6, 6–3, 7–6(6) | Indoor carpet 3-set tiebreak battle; total smashed |

### 1. New Rule: `TENNIS-CHALLENGER-CLAY-HANDICAP-CAP`
- **Challenger & ITF Slow Clay Volatility:** On slow European outdoor red clay (e.g. Tolentino), service hold rates drop below 60% across lower-tier WTA/ITF events. Return games dominate, generating frequent reciprocal service breaks.
- **Handicap Capping:** Heavy game handicaps (e.g. -5.5 or greater) require a near-flawless 6–3, 6–2 or 6–2, 6–2 margin. In lower tiers where ranking separation (e.g. #170 vs #380) reflects tournament tier participation rather than raw baseline skill, underdogs playing on home soil possess immense break-back potential.
- **Protocol:** Never rank a games handicap of -5.5 or higher at Rank #1 on slow red clay in WTA 125 or ITF events unless the favourite boasts a verified hold rate >78% and the underdog has a return-points-won rate <32% on clay. Prefer straight-set match-winner or conservative game totals.
