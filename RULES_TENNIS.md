> **Current authority (October 5):** [METHOD.md](METHOD.md) and [CURRENT_RULES.md](CURRENT_RULES.md) govern new work. Requested qualitative or explicitly uncalibrated research receives canonical Part 6 IDs regardless of calibration; numerical performance certification is separate. Read current IDs/freeze from the [status register](GAME_LOG_STATUS_CURRENT.md), unresolved items from the [carryover](research/verification/closure_2026-10-05/carryover.md), and [current implementation evidence](research/verification/implementation_2026-10-05/REPORT.md). Earlier method, queue, freeze and eligibility statements below retain their historical scope.

**Local authority and all-log reconciliation (October 5):** Local working files govern; GitHub main publishes them. The latest user instruction supersedes earlier GitHub-only prompts. Current [all-log evidence](research/verification/all_log_resolution_2026-10-05/REPORT.md) accounts for all 537 slots and temporary aliases, ten repaired documentary mappings, four new sporting reviews and 53 precise carryovers. Existing IDs and frozen forecast/source bytes remain unchanged.

# Tennis analysis rules

**Live rules for Tennis. Markdown-only operation, 2026-09-28.** Read §0 in full for every card: it governs this file.
- §1 onward is the reference algorithm and the competition rules; it is consulted by citation.
- The dated history (settlement learnings and the evidence behind every numbered control) was moved verbatim to `archive/superseded_2026-09-28/sport_history/RULES_TENNIS_history_to_2026-09-28.md`, which is no longer in the Markdown tree. A maintainer can recover it from the pinned commit ([Git 3fbf0c981b40](https://github.com/danisgreat/Sports-Research/blob/3fbf0c981b40a1d0e3ffff9725dcc8e383ff05fa/archive/superseded_2026-09-28/sport_history/RULES_TENNIS_history_to_2026-09-28.md); [index](HISTORICAL_LINK_INDEX.md#removed-paths-cited-in-operating-documents)) when a control's full text or evidence is needed. The model works from §0 and the sections below.
- Arithmetic: `PROBABILITY_TOOLKIT.md`. Sources: `SOURCES.md` §3.10. Card and self-audit: `CARD_AND_LOG_TEMPLATES.md`. The cross-sport rules are in `CURRENT_RULES.md`, which outranks this file.
- No sport, competition or target is prospectively validated. Every card is LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE.

<!-- LIVE-RULES-PAGE-2026-09-26 -->
## 0. Live rules — one page (consolidated 2026-09-26)

**Status (md-only, 2026-09-28).** This page is the live rule set for this sport and governs the rest of the file. It was consolidated on 2026-09-26 from the numbered controls, the SFA algorithm and the dated sections through 2026-09-25(e). Those dated sections are now archived (see the header). Where a control below is one line, that line is the operative rule, and the archived history is its evidence.

**Tennis is `NO_DEMONSTRATED_SKILL`.** 16 decisions won 50.0% at a stated 0.601 (Brier 0.281, worse than a coin flip). The evidence grade is capped at LOW, the departure ledger is required, and the card stays near the Elo benchmark and the population rates unless serve/return numerators justify moving (2026-09-25(d)).

### 0.1 Blocking preconditions (§9.1)
| Gate | Requirement | If it fails |
|---|---|---|
| TE-P1 format | Tour, event, round, surface (from the official calendar, not memory), best-of-3/5, final-set and tiebreak rules | Stop |
| TE-P2 participants | Exact players from the official event source, re-handshaken at freeze | No directional analysis |
| TE-P3 retirement terms | Operator retirement/walkover rules for every row | `UNKNOWN_DEFINITION`, `NO VALUE DETERMINABLE` (control 7) |
| TE-P4 status | Withdrawal, medical, rest, travel and qualifying workload | Missingness code; never infer fitness from results |
| **TE-P5 Elo benchmark (blocking)** | Dated Tennis Abstract Elo (overall and surface), snapshotted before the event, converted to the format's win probability and printed beside the card's winner mass | A gap above 10 percentage points needs a named current mechanism (control 13) |

### 0.2 Building the match tree
1. **Serve and return as numerators and denominators**, match by match, so every rate carries its n (TE-S2). **Matchup holds, not season holds:** each player's hold comes from their level- and surface-adjusted serve points won against *this opponent's* return points won (TE-S4). Level and opponent comparability is shown, not assumed (control 9).
2. **Both players get the full branch set** (TE-B1–B6): straight-set control, close straight sets/tiebreaks, deciding-set win. An underdog's win mass is never attached only to long matches (§4).
3. **Set-count mixture before within-set closeness** (TE-S7). Best-of-five holds three-, four- and five-set endpoints separately (TE-B7). A total without an explicit set-count mixture is capped at FORCED RANK (override 3).
4. **Width.** A long layoff widens the tree (control 14). Workload carries both signs, so at least width (G-L2). The WTA raw total-games SD is 5.79 (men best of 3 6.00).
5. **One tree → every row** (TE-S8). Write a representative Rank-1 scoreline and check it against every leading row (control 12, override 1). Tiebreak sets count 7+6 = 13 games; tiebreak points are not games (L-068).

### 0.3 Row rules
- **Totals (TE-R1).** Print P(deciding set) against the reference (WTA best of 3 0.340; men best of 3 0.358; women's qualifying 0.313 v main draw 0.352). WTA total games are bimodal: 18.2 in straight sets, 28.6 with a decider. Lines from 19.5 to 25.5 are mostly P(deciding set) rows, and the card says so. For best-of-three lines from 18.5 to 21.5, print P(decisive straight sets) and P(three sets) (§9.4).
- **Games handicaps (TE-R2, C-HCP-COHERENCE).** Hard identity: P(A −k.5) ≤ P(A wins), or the card fails closed. Print P(A −k.5) = P(straight-set win)·c_s + P(deciding-set win)·c_d, with the population c_s/c_d beside them (WTA −5.5: 0.663/0.168). Above the reference without dated hold/break evidence is `HCP_CONDITIONAL_ABOVE_REFERENCE`. A games handicap is aggregate games, independent of the set winner (override 7).
- **Cushions.** +k.5 games cushions won 1/4 at 0.58: `C-PLUS-CUSHION` applies with C-HCP-COHERENCE, and RM-1's cushion term covers them (q ≈ 0.30 at a stated 0.58). A cushion supported by close sets lengthens the same match, so an Under co-ranked with it is a coherence question (§9.5).
- **Over + underdog games cushion as the top two** underperforms when the card's favourite mass sits below Elo (`C-TEN-FAV-SEPARATION`, TESTING).
- **Low-tier games handicaps of 5.5+ at a normalised edge below 0.15** are `T-TEN-LOWTIER-HCP` (TESTING; no cap meanwhile).
- **Rankings, seeding, streaks, cover counts and old H2H** are diagnostic only (overrides 4–5; controls 3, 8, 10).

### 0.4 Ranking
Rank by RM-1 q. There is no TB-1 lane: the anchors are the dated Elo benchmark (TE-P5) and the §7.4 population. A total-games Over at Rank 1 prints P(deciding set) against 0.340, because the Over is mostly a third-set bet.

### 0.5 Settlement
Raw ATP/WTA/ITF records for set and tiebreak scores (G-L13). ITF: the tournament "draws-and-results" page through `r.jina.ai` (T-1). Name the settling record and the retirement rule at issue (G-L14). Record medical time-outs, retirements and rain suspensions with the set and game score.

### 0.6 Withdrawn in tennis — never apply
The clay/Challenger handicap cap (L-20260924-F06); "winner implies games handicap" and "cushion implies underdog winner"; long-match-only coupling of underdog wins; pseudo-tails, path-count categories, 40–60% bands and normalised-edge ordering.

### Numerical shadow model (2026-09-26(c); suspended for md-only operation, 2026-09-28)

The tennis model: on ATP 2023 to January 2026, surface-blended Elo narrowly beat overall Elo on winners (Brier 0.222 against 0.224). The serve-chain games route lost to the population at v1; after v2 (a match-level gap effect, selected on 2021–22) it is level to slightly better. WTA was not validated. A retirement voids the games rows. It is maintainer Python, never a card input, and the model does not run it: print `SHADOW: NO_LANE (md-only)` at settlement (`research/sport_models_2026-09-26/README.md` ([removed; recovery](HISTORICAL_LINK_INDEX.md#removed-paths-cited-in-operating-documents))). The hand-computable team baseline that does feed cards is TB-1-MD (`PROBABILITY_TOOLKIT.md` §4).

**Predictability (2026-09-26(e)).** Tennis winners are predictable by Elo (Brier 0.222 against a coin flip's 0.25), and A1 improves that only narrowly. The WTA is not validated (`research/predictability_2026-09-26/README.md` ([removed; recovery](HISTORICAL_LINK_INDEX.md#removed-paths-cited-in-operating-documents)); `BASE_RATES_REGISTER.md` §7.8).

### 0.7 Control index (full text in §5 and the dated sections)
1 surface is a regime · 2 current stability decomposed · 3 H2H needs continuity · 4 set count and total linked · 5 set cushions aren't free safety · 6 qualifying and workload · 7 retirement terms gate · 8 no ranking-only confidence · 9 level comparability demonstrated · 10 win-conditioned cover counts descriptive · 11 kill paths include opponent control · 12 scoreline coherence · 13 Elo benchmark beside the winner probability · 14 a long layoff widens the tree. Receipts and references: T-1 ITF route · T-2 surface from the calendar · TE-R1 totals reference · TE-R2 handicap coherence · TE-R3 qualifying v main draw.

### 0.8 Numerical engine specification (MDS-v8.0 / CR-2026.10.06-NUMERICAL-1)
Under the numerical ML architecture (`runtime/src/sports/tennis/engine.py`):
1. **Event-First Modeling**: Surface-adjusted serve/return point Markov model:
   $$\text{Point Win Prob } p_{\text{serve}} \longrightarrow \text{Game Hold/Break } P(\text{Hold}) \longrightarrow \text{Tiebreak/Set Distribution} \longrightarrow \text{Match Winner & Games Matrix } (G_1, G_2)$$
2. **Derivative Coherence**: Games totals and games handicaps ($G_1 - G_2$) are integrated directly from the discrete joint games grid; P(deciding set) and straight-set distributions are explicit.
3. **Regime Conditioning**: Surface (Clay, Hard, Grass, Indoor) and tournament format (Best-of-3 vs Best-of-5) condition serve/return transition kernels.
4. **Independent Training**: Fit exclusively on `H0-TENNIS-v1` (Tennis Abstract / OnCourt / Jeff Sackmann match charting); D0 is strictly reserved for qualitative error diagnostics.


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


Algorithm ID: `SFA-TENNIS`. Effective **2026-09-02**. Instantiates `GFA-2` (RULES_GENERAL (archived) §11) with tennis content. Process composition only; no fitted weight, scenario weight or published probability is introduced, and no tennis target, source, dataset or model is approved or fit. ATP, WTA, Challenger, ITF, junior, UTR and exhibition levels are separate populations and their rates are not exchangeable.


### 9.1 Blocking preconditions


| Precondition | Requirement | Failure output |
|---|---|---|
| `TE-P1` format and endpoint | Tour, event, round, surface, best-of-three or best-of-five, final-set format, tiebreak rules and match-tiebreak substitutions | `GATE-TARGET` failure; do not proceed |
| `TE-P2` participants | Exact players, handedness, entry status, draw position and scheduled start from the official event or tour source, re-handshaken at G31 | Identity unresolved means no directional analysis |
| `TE-P3` retirement terms | The operator's retirement, walkover and withdrawal rules for every supplied row | `UNKNOWN_DEFINITION` and `NO VALUE DETERMINABLE` |
| `TE-P4` current status | Verified withdrawal, medical, rest, travel and qualifying-workload state | Record the missingness code; never infer fitness from a result list |
| `TE-P5` independent benchmark (added 2026-09-25; R-2 of the 2026-09-22 audit; enforces control 13) | Dated Tennis Abstract Elo, overall and surface-specific (ATP `tennisabstract.com/reports/atp_elo_ratings.html`; WTA `tennisabstract.com/reports/wta_elo_ratings.html`), **snapshotted before the event** with its page date. The card prints the implied best-of-three or best-of-five win probability beside its own winner mass. If the two differ by more than 10 percentage points, the card names the current mechanism or rebuilds the serve/return tree before issue | `BENCHMARK_NOT_RETRIEVED`: no winner, games-handicap or total row may be Rank #1. The benchmark is a check, never a probability source or calibration target |


### 9.2 Exposure chain


| Step | Output |
|---|---|
| `TE-S1` | Participation and completion state: start probability, retirement and walkover branches |
| `TE-S2` | Surface- and opponent-adjusted serve profile for each player: first-serve in rate, first- and second-serve points won, ace and double-fault shape. **Stored as numerators and denominators, match by match (added 2026-09-25):** total service points, first serves in, first-serve points won, second-serve opportunities, second-serve points won, double faults and aces, so that every rate carries its n and can be reproduced |
| `TE-S3` | Return profile for each player: return points won, break-point creation, and pressure-point behaviour |
| `TE-S4` | Hold and break distributions per player from `TE-S2` and `TE-S3`, with score-state uncertainty. **Matchup holds, not season holds (added 2026-09-25; R-3):** each player's expected hold is derived from their level- and surface-adjusted serve points won against **this opponent's** return points won, and printed before any total or handicap is ranked. Comparing season hold percentages serve against serve (P-483) does not satisfy this step |
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
| Total games | Set-count mixture times within-set closeness | Which set count carries the mass; a deciding-set branch can rescue an Over without being independent of the handicap. **For best-of-three totals from 18.5 to 21.5, print P(decisive straight sets for either player) and P(three sets) beside the row (added 2026-09-25; R-4)**: at these lines the Over is close to "no decisive straight-set win". Best-of-five analogue: P(straight sets) and P(five sets) |
| Set betting and correct score | The same tree | The exact set sequence, not a directional lean |
| First set | Its own opening-set sub-tree from early hold, break and return pressure | Why the opening state differs from or agrees with the full-match state |
| Player props | Service and return point counts from `TE-S2`/`TE-S3` times expected games | The provider's own definition |


### 9.5 Kill-path library


| Kill path | Defeats | Evidence origin |
|---|---|---|
| An opponent's ordinary straight-set control | A favourite handicap whose kill path is written only as "favourite wins narrowly" | §5 control 11, C-PL6-TEN-BIDIRECTIONAL-TREE |
| Favourite control at 6-2, 6-2 | An Over ranked alongside a preference for that same favourite and their game handicap; also an Over plus an underdog games cushion as the top two | §5 control 12, C-PL9-TEN-CROSSMARKET; recurrence P-212, P-242, P-310, P-483 (Volynets 6-3 6-0); counter-example P-350 (tracked as `C-TEN-FAV-SEPARATION`, LEARNING_REGISTER) |
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
17. **Benchmark (`TE-P5`; added 2026-09-25):** the dated Elo benchmark is printed beside the winner mass. A gap of more than 10 percentage points is explained by a named current mechanism, or the tree is rebuilt.
18. **Matchup holds (`TE-S4`; added 2026-09-25):** each player's hold against this opponent is derived from serve × return, with the numerators and denominators shown.
19. **Decisive-branch disclosure (§9.4; added 2026-09-25):** P(decisive straight sets) and P(three sets) are printed beside any best-of-three total from 18.5 to 21.5.


### 9.8 Recency, head-to-head and trend windows


Implements `GFA-2` step G13.1 (RULES_GENERAL (archived) §11.3B) and runs at that point in the algorithm, not at the end. Retrieval of L5/L10/L15/L20 for both sides and for the head-to-head series is mandatory; a window that does not exist is recorded with its true count and a missingness code.


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


Implements `GFA-2` step G15.1 (RULES_GENERAL (archived) §11.3C). Venue classification for this sport is normally **OUTDOOR unless the event is indoors or the roof is closed**.


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


**Maintenance (RULES_GENERAL (archived) §3, `G2`).** The tours revise the rulebook most years (the 2022 final-set tiebreak alignment, on-court coaching becoming permanent in 2025, the spread of electronic line-calling, changes to medical-timeout and bathroom-break rules). Before the first card of a new Grand Slam, a new season on any tour, or a competition format not seen before (a Davis Cup / Billie Jean King Cup tie, a United Cup, an exhibition), re-verify the match format (best-of-3 vs 5, ad vs no-ad, standard vs match-tiebreak decider), the deciding-set rule, the coaching and line-calling rules, and the event's own draw/advancement structure, and update this section **before** issuing the card. The first time a new circuit is forecast (WTA 125, ATP Finals, a team event, a senior/legends event), document its full format and any format flexibility here first.


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
