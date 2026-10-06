> **Current authority (October 5):** [METHOD.md](METHOD.md) and [CURRENT_RULES.md](CURRENT_RULES.md) govern new work. Requested qualitative or explicitly uncalibrated research receives canonical Part 6 IDs regardless of calibration; numerical performance certification is separate. Read current IDs/freeze from the [status register](GAME_LOG_STATUS_CURRENT.md), unresolved items from the [carryover](research/verification/closure_2026-10-05/carryover.md), and [current implementation evidence](research/verification/implementation_2026-10-05/REPORT.md). Earlier method, queue, freeze and eligibility statements below retain their historical scope.

**Local authority and all-log reconciliation (October 5):** Local working files govern; GitHub main publishes them. The latest user instruction supersedes earlier GitHub-only prompts. Current [all-log evidence](research/verification/all_log_resolution_2026-10-05/REPORT.md) accounts for all 537 slots and temporary aliases, ten repaired documentary mappings, four new sporting reviews and 53 precise carryovers. Existing IDs and frozen forecast/source bytes remain unchanged.

# Rugby league / NRL analysis rules

**Live rules for Rugby league (NRL). Markdown-only operation, 2026-09-28.** Read §0 in full for every card: it governs this file.
- §1 onward is the reference algorithm and the competition rules; it is consulted by citation.
- The dated history (settlement learnings and the evidence behind every numbered control) was moved verbatim to `archive/superseded_2026-09-28/sport_history/RULES_NRL_RUGBY_history_to_2026-09-28.md`, which is no longer in the Markdown tree. A maintainer can recover it from the pinned commit ([Git 3fbf0c981b40](https://github.com/danisgreat/Sports-Research/blob/3fbf0c981b40a1d0e3ffff9725dcc8e383ff05fa/archive/superseded_2026-09-28/sport_history/RULES_NRL_RUGBY_history_to_2026-09-28.md); [index](HISTORICAL_LINK_INDEX.md#removed-paths-cited-in-operating-documents)) when a control's full text or evidence is needed. The model works from §0 and the sections below.
- Arithmetic: `PROBABILITY_TOOLKIT.md`. Sources: `SOURCES.md` §3.6. Card and self-audit: `CARD_AND_LOG_TEMPLATES.md`. The cross-sport rules are in `CURRENT_RULES.md`, which outranks this file.
- No sport, competition or target is prospectively validated. Every card is LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE.

<!-- LIVE-RULES-PAGE-2026-09-26 -->
## 0. Live rules — one page (consolidated 2026-09-26)

**Status (md-only, 2026-09-28).** This page is the live rule set for this sport and governs the rest of the file. It was consolidated on 2026-09-26 from the numbered controls, the SFA algorithm and the dated sections through 2026-09-25(e). Those dated sections are now archived (see the header). Where a control below is one line, that line is the operative rule, and the archived history is its evidence.

**Track record.** Rugby codes combined: 12 decisions won 58.3% at a stated 0.567 (too few to judge). NFL, AFL and NRL together went 12 W / 20 L at Rank 1/2, the worst group. NRL and NRLW are separate populations. League and union are never pooled (control 8).

### 0.1 Blocking preconditions (§8.1)
| Gate | Requirement | If it fails |
|---|---|---|
| RL-P1 laws | Law variations, interchange, six-again/set restarts, regulation, golden point and draw terms | Stop |
| RL-P2 team list | Official list, final match-day reduction and late mail, starting 13, bench and the confirmed spine (fullback, five-eighth, halfback, hooker), from the raw NRL match centre or club page with publication time (G-L13). After late mail, `NOT_RETRIEVED` is `RETRIEVAL_MISS` | Spine and role mixtures; dependent rows capped |
| RL-P3 goal kicker | Primary goal kicker and replacement (control 5) | Required before any total or margin row |
| RL-P4 conditions | Venue, surface and match-window weather with a named mechanism | Wet weather is bidirectional (control 4) |

### 0.2 Building the score distribution
1. **Anchor.** Sides and totals both anchor on the population (`BASELINE_P`).
   - **Sides (corrected 2026-09-26(e), validity repair):** TB-1's 2026 point gain (0.240 v 0.253) has a 95% interval that crosses 0 (−0.0294, +0.0044), so `TEAM_BASELINE_P` is printed with `TB1_NO_RESOLUTION:margin` and is not the anchor.
   - **Totals have no TB-1 resolution either** (its RMSE is worse than the league mean): anchor on the population row (2026: mean 47.8, SD 13.9).
2. **Scoring components, not points** (September 6). Points = 4×tries + 2×conversions + 2×penalty goals + 1×field goals, with conversions = tries × goal-kicking %. A debutant kicker's own reserve-grade kicking percentage enters the conversion term (L-075).
3. **Branches.** Before any Under or underdog cushion is ranked, write one favourite-only scoring path (RL-B2) and one low-total separation path (RL-B3) with their mechanisms (override 1; controls 13, 14). The second half carries score, possession, field position, bench and fatigue forward (control 15). Close-game winners need the terminal-event branch (RL-B5, control 16; override 3). Blowouts are possession-native (control 12).
4. **Regimes.** A changed spine rebuilds set organisation, kicking and edge attack (control 1). A current defensive collapse or spine return against season averages is a baseline/current-regime mixture (control 11).
5. **Small samples.** Completion, goal-kicking and try rates over three or four rounds print their standard error before any signed adjustment (G-L11).
6. **Width.** TB-1 residual widths: total 13.9, margin 19.9 (2026).
7. **One score object → total and margin queried separately** (override 2). Possession imbalance is bidirectional (control 2, override 4).

### 0.3 Row rules
- **Cushions (C-PLUS-CUSHION).** The TB-1 underdog covered +1.5 at 0.41–0.43, +2.5 at 0.44–0.49, +4.5 at 0.51, +6.5 at 0.55–0.57, +8.5 at 0.62, +12.5 at 0.65–0.67 (2025–26). Print the favourite's 7+ and 13+ margin families beside any cushion (G-L12). Stated more than 0.05 above the rate without a receipted mechanism, RM-1 flips it.
- **Over + underdog cushion.** When RL-B3 carries material mass, print P(R1 ∧ R2) and its sign (P-397). These are distinct targets with a shared driver (G-L15).
- **Totals departing from the population by about 0.10 or more** need a receipted mechanism, such as a confirmed wet-track forecast for the match window (P-515).
- **Recent cover rates, points averages and old H2H** are diagnostic only (control 3, override 5).

### 0.4 Reference rows (NRL, all completed games; `BASE_RATES_REGISTER.md` §7.7)
| Row | 2025 (n = 216) | 2026 (n = 213) |
|---|---:|---:|
| Home win | 0.551 | 0.545 |
| Total mean (SD) | 46.1 (14.0) | 47.8 (13.9) |
| Total 10th / 50th / 90th percentile | 29 / 44 / 64 | 30 / 48 / 66 |
| Home margin; margin SD | +3.8; 18.7 | +0.0; 20.7 |
| P(\|m\| ≤ 2); P(\|m\| ≤ 6) | 0.13; 0.34 | 0.15; 0.29 |

NRLW has no population reference yet (`NOT_YET_DERIVED`).

### 0.5 Ranking and settlement
- Rank by RM-1 q; its cushion term applies to NRL +k.5 rows.
- Settle from ESPN `rugby-league/3` (regular season is season type 1, finals type 2; `linescores` carry half-time then full-time) plus two further lineages. nrl.com statistics are admissible only when fetched and pasted with a URL.
- Record sin bins, send-offs and HIA removals with the minute and score.

### 0.6 Withdrawn or not operative in rugby league
`C-NRL-SPINE-PEDIGREE-TOTAL-FLOOR` (rejected: one game, invented statistic). `C-FINALS-BYE-RUST` is TESTING only (`T-NRL-BYE-RUST`, 30 games), with no ranking effect. Pseudo-tails, path-count categories, 40–60% bands and normalised-edge ordering.

### Numerical shadow model (2026-09-26(c); suspended for md-only operation, 2026-09-28)

The NRL model (A1) is ridge ratings with key-number weights. Validated on 2026: results not significant (−0.0273, +0.0003); margin RPS better; totals no better than the population. TB-1's result gain was not significant either, so the NRL reference is the population. The hand-computed TB-1-MD did beat the population on 2026 sides (`PROBABILITY_TOOLKIT.md` §4.4). That is one season found after the fact, so it is test `T-TB1MD-NRL`, not an anchor. It is maintainer Python, never a card input, and the model does not run it: print `SHADOW: NO_LANE (md-only)` at settlement (`research/sport_models_2026-09-26/README.md` ([removed; recovery](HISTORICAL_LINK_INDEX.md#removed-paths-cited-in-operating-documents))). The hand-computable team baseline that does feed cards is TB-1-MD (`PROBABILITY_TOOLKIT.md` §4).

**Predictability and cards (2026-09-26(e)).** The model's favourite reached 0.70 in 19% of games and won 68.3%. The 0.70–0.80 band won 67% at 0.737, so it is over-confident. On the cards' own NRL contracts (4, from 2 cards): card 0.271, A1 0.203. That is too few to read (`research/predictability_2026-09-26/README.md` ([removed; recovery](HISTORICAL_LINK_INDEX.md#removed-paths-cited-in-operating-documents)); `BASE_RATES_REGISTER.md` §7.8).

### 0.7 Control index (full text in §4 and the dated sections)
1 spine is a regime · 2 possession imbalance drives dependence · 3 cover rates diagnostic · 4 wet weather bidirectional · 5 goal-kicker state · 6 sin-bin/send-off tail · 7 winner ≠ handicap · 8 league and union never pooled · 9 motivation conditional · 10 no calibration claim · 11 defensive regime and spine-return mixture · 12 blowouts are possession-native · 13 a total can clear through one team · 14 low total ≠ close margin · 15 halftime doesn't freeze separation · 16 close-game winner needs terminal events.

### 0.8 Numerical engine specification (MDS-v8.0 / CR-2026.10.06-NUMERICAL-1)
Under the numerical ML architecture (`runtime/src/sports/nrl/engine.py`):
1. **Event-First Modeling**: Sets, completion, and territorial field position simulation:
   $$\text{Completed Sets} \longrightarrow \text{Attacking 20m Entries} \longrightarrow \text{Tries (4 pts) + Conversions (2 pts) + Penalty/Field Goals (1/2 pts)}$$
2. **Key Number Discrete Preservation**: Rugby league margins cluster around 2, 4, 6, 8, 10, 12; scores are discrete combinations, never continuous Gaussian approximations.
3. **Regime Conditioning**: 2020 six-again rule change strictly demarcates high-pace modern NRL from legacy low-pace rugby league. Spine availability (1, 6, 7, 9) and primary goal-kicker accuracy condition transition rates.
4. **Independent Training**: Fit exclusively on `H0-NRL-v1` via `nrlR` (ingested through isolated R script `runtime/r_ingestion/nrl_nrlr.R`); D0 is strictly reserved for qualitative error diagnostics.


## 1. Identity and contract


Resolve NRL, NRLW, Super League, reserve-grade, international, or another league competition; current laws/interchange rules; venue; regulation/golden-point/draw terms; team/player/phase statistic; and exact settlement provider. Do not call a Super League fixture NRL.


## 2. High-value inputs


### Participants and roles


- Confirm the official team list, final match-day reduction/release, starting 13, bench, late changes, and current competition interchange/activation rules.
- Identify the spine: fullback, five-eighth, halfback, hooker; primary goal kicker; playmakers and replacement tree.
- Estimate minutes, interchange, carries, tackles, kicking role, goal-kicking share, and position changes.
- Translate absences into set organisation, field position, ruck speed, edge defence, and conversion.


### Possession and field position


Use opponent-adjusted:


- possessions/sets and set starts;
- completion and error rates;
- metres/set and post-contact metres;
- play-the-ball/ruck speed where defined;
- line breaks, tackle breaks, offloads and kick returns;
- repeat sets, penalties, six-again, field position and goal-line entries;
- tries, try location, goal conversion, and defensive conversion;
- tackle load and interchange fatigue.


Raw points and cover history do not substitute for possession and field position.


### Context


Record rest, travel, turnaround, venue, match-window weather, surface, ladder/finals incentives, referee only with current relevant data, and verified tactical changes. Wet conditions can reduce handling but also create short fields and fatigue; no automatic Under.


## 3. Model


Exposure units are possessions/sets, set starts, field position, carries/tackles, line-break opportunities, tries, and conversions. Estimate territory and try opportunities first, then finishing and goal-kicking. Use a joint score/margin distribution with sin-bin, intercept/short-field, fatigue, and golden-point tails.


Derive winner, handicap, total, phase, and player contracts from the same distribution.


For numerical training, compare empirical/simple set-and-try baselines with a sets → field position → goal-line entry → try → conversion A2 simulator. It samples completion/errors, repeat sets, penalties/six-again, ruck/fatigue, line breaks, sin-bin/send-off, kicker and golden-point states while preserving both teams' possession dependence. Direct score or boosted-distribution models are challengers only after discrete-support, scoring-combination, population and calibration checks. Elo is contextual strength, not the scoring engine. Every contract integrates the same joint score distribution. All candidates remain unfit and unvalidated.


## 4. Structural controls


1. **Spine is a regime variable.** Rebuild set organisation, kicking, and edge attack for a changed spine.
2. **Possession imbalance drives dependence.** It can raise favourite margin while suppressing the underdog contribution; total direction remains scenario-specific.
3. **Recent cover rates are diagnostic.** Current participants, set distance, line breaks, and field position control.
4. **Wet weather is bidirectional.** Trace handling errors, kicking, short fields, ruck speed, and goal-kicking.
5. **Goal-kicker state matters.** Tries and conversions are dependent; record the current kicker and replacement.
6. **Sin-bin/send-off is an explicit tail.** Rebuild remaining possessions when it occurs live.
7. **Winner and handicap differ.** Model separation, narrow result, and golden-point branches.
8. **League and union cannot be pooled.** Laws, scoring, possession and settlement differ.
9. **Motivation is conditional.** Tie it to selections, interchange, tempo or risk.
10. **No current calibration claim.** P-039 is one NRL event and cannot establish model performance.
11. **Current defensive regime and spine return require a mixture.** When a recent conceded-points/line-break/field-position collapse or a key spine return conflicts with season averages and old H2H, freeze baseline and current-regime branches with named mechanisms. Weather and historical close scores cannot silently suppress a credible separation tail.
12. **Blowout branch is possession-native.** Stress repeated short fields, missed-tackle/line-break clusters, spine-led set control and conversion quality before ranking a broad Under or underdog cushion. One realised blowout creates a candidate, not an automatic coefficient.
13. **A total can clear through one team.** For every broad Under, test a favourite-only scoring branch in which the underdog remains suppressed but errors, short fields, repeat sets, line breaks and conversions let the favourite carry the total over the line.
14. **Low total does not imply close margin.** A territorial/completion/defensive-control state can produce a multi-score favourite cover while the match stays Under. Margin and total must be queried separately from the joint score tree.
15. **Halftime does not freeze full-time separation.** Carry score, possession/set starts, field position, completion/error state, spine function, bench/interchange usage, defensive workload and conditions into the second-half branch. A competitive first half can become a favourite cover through opponent suppression and fatigue without creating a high total.
16. **Close-game winner needs terminal-event sensitivity.** In a competitive low-total branch, separately model final-five-minute field position, interchange/conditioning, spine/kicker availability, repeat sets, penalties, sin-bin/injury states and conversion/kick outcomes. A sound Under or broad cushion does not identify which side wins the last scoring sequence.


## 5. Live state


Store score, clock/half, possession/set and tackle, field position, repeat-set/six-again, penalties/errors, line breaks, sin bins/send-offs, injuries, interchanges, kicker, and current ruck/territory. Recompute remaining sets and field-position distribution.


## 6. Sources and settlement


- NRL official team lists, late mail, match centres, judiciary and [game/statistics resources](https://www.nrl.com/operations/the-game/) control NRL.
- Official competition sources control Super League, NRLW, internationals, and other leagues.
- Government weather services and venue reports control conditions.


Settle from the official final and named provider, preserving regulation/golden-point and exact player-stat definitions.


## 7. Upcoming-game research sequence


1. Freeze rugby-league competition/laws, regulation/golden-point/draw terms, player/stat provider and candidate slate.
2. Retrieve official team lists, injury/casualty status, reductions/late mail, starting 13, bench, spine and goal kicker. Refresh at the current competition's final-update deadline and immediately before kickoff.
3. Model player minutes/interchange, sets and set starts, field position/tackle state, completion/errors, ruck/fatigue, goal-line entry, try location, conversion, penalties/six-again, sin-bin and golden-point tails.
4. Possession dominance can increase margin while reducing the opponent contribution; total direction must be scenario-derived.
5. Before ranking an Under or underdog cushion, calculate one explicit favourite-only blowout path and one low-total separation path; record which mechanisms and score families make each credible.
6. Derive joint score, winner, total and handicap from the same score object. Player props use position, minutes, carries/tackles/kicks or goal-kicking exposure and exact provider definitions.


Official competition sources own current teams/state/rules. Historical archives are cross-check/research lanes and cannot override late mail or enter H0 before field-level approval.


## 8. SFA-RUGBY-LEAGUE — sport forecast algorithm


Algorithm ID: `SFA-RUGBY-LEAGUE`. Effective **2026-09-02**. Instantiates `GFA-2` (RULES_GENERAL (archived) §11) with rugby-league content. Process composition only; no fitted weight, scenario weight or published probability is introduced. NRL, NRLW, Super League, internationals and lower grades are separate populations, and no rugby-union or sevens data enters any step.


### 8.1 Blocking preconditions


| Precondition | Requirement | Failure output |
|---|---|---|
| `RL-P1` competition and laws | Competition, law variations, interchange and activation rules, six-again and set-restart conventions, regulation, golden-point and draw terms | `GATE-TARGET` failure; do not proceed |
| `RL-P2` team list | Official team list, final match-day reduction and late mail, starting 13, bench, and the confirmed spine — fullback, five-eighth, halfback, hooker — re-handshaken at the competition's final update deadline and again at G31 | Spine and role mixtures; dependent rows cap at `FORCED RANK` / `MEDIUM-LOW` |
| `RL-P3` goal kicker | Primary goal kicker and replacement | Required before any total or margin row, because tries and conversions are dependent |
| `RL-P4` conditions | Venue, surface and match-window weather with a named mechanism | Wet weather is bidirectional; no automatic Under |


### 8.2 Exposure chain


| Step | Output |
|---|---|
| `RL-S1` | Minutes and interchange by player, with the spine replacement tree and positional changes |
| `RL-S2` | Possession: sets and set starts for both sides, from completion rate, errors, penalties and six-again |
| `RL-S3` | Field position: metres and post-contact metres per set, kick metres, kick return, and resulting set-start position |
| `RL-S4` | Goal-line entry rate from `RL-S2` and `RL-S3`, including repeat sets and short fields |
| `RL-S5` | Try conversion from entries: line breaks, tackle breaks, offloads, edge defence, missed-tackle clusters and try location |
| `RL-S6` | Goal-kicking from the current kicker, plus penalty-goal and field-goal decisions by score state |
| `RL-S7` | Fatigue state: tackle load, interchange usage, ruck speed and second-half decay for both sides |
| `RL-S8` | One joint score and margin object with sin-bin, send-off, intercept, short-field and golden-point tails |


Raw points and cover history never substitute for `RL-S2`–`RL-S5`.


### 8.3 Mandatory branch set


| Branch | Content |
|---|---|
| `RL-B1` | Central possession with central entry conversion for both sides |
| `RL-B2` | Favourite-only scoring branch: the underdog stays suppressed while errors, short fields, repeat sets, line breaks and conversions carry the total up through one side |
| `RL-B3` | Low-total separation branch: territorial, completion and defensive control producing a multi-score cover inside an Under |
| `RL-B4` | Second-half separation: the complete halftime state — score, set starts, field position, completion, spine function, bench usage, defensive workload and conditions — carried forward |
| `RL-B5` | Terminal-sequence branch: final-five-minute field position, interchange and conditioning, spine and kicker availability, repeat sets, penalties and conversion outcomes |
| `RL-B6` | Sin-bin or send-off state, with the remaining possession rebuild for the exact man-down duration |
| `RL-B7` | Wet-weather state, with handling errors, kicking, short fields, ruck speed and goal-kicking each signed separately |
| `RL-B8` | Golden point or draw treatment under the exact competition and operator terms |


### 8.4 Contract derivation map


| Contract | Queried from | Extra condition the mechanism must predict |
|---|---|---|
| Total | Sum marginal | The component budget, including the `RL-B2` favourite-only path |
| Line and handicap | Margin marginal | Separation, narrow result and golden-point branches stated separately |
| Winner | Margin sign, including terminal sequence | A sound Under or broad cushion does not identify the last scoring sequence |
| Team total | Team marginal | That side's own entries and conversion, not the match tempo |
| Half or phase | The segment's own possession and field-position state | Halftime never freezes full-time separation |
| Player props | Position, minutes, carries, tackles, kicks or goal-kicking exposure | The exact provider definition |


### 8.5 Kill-path library


| Kill path | Defeats | Evidence origin |
|---|---|---|
| A favourite carrying the total alone while the underdog is suppressed | A broad Under justified by two-team scoring expectations | §4 control 13, C-PL6-RL-FAVOURITE-ONLY-TOTAL |
| Territorial and completion control producing a multi-score cover | The framing that a low total protects an underdog cushion | §4 control 14 |
| A competitive first half becoming a second-half cover through fatigue and suppression | A close-margin row anchored to the halftime state | §4 control 15, C-PL8-RL-H2-SEPARATION |
| Two late tries flipping the winner inside an otherwise correct low-total tree | An outright winner derived from the total and cushion | §4 control 16, C-PL9-RL-TERMINAL-WINNER |
| A changed spine rebuilding set organisation, kicking and edge attack | Season averages and old head-to-head retained at high evidence | §4 controls 1 and 11 |
| Repeated short fields and missed-tackle clusters | An Under ranked before a possession-native blowout branch is stressed | §4 control 12 |
| Wet conditions creating short fields and fatigue as well as handling errors | A one-sign wet-weather Under | §4 control 4 |
| A sin-bin rebuilding remaining possession | A margin or total row with no man-down branch | §4 control 6 |


### 8.6 Sport ordering overrides


1. Before any Under or underdog cushion is ranked, write one explicit `RL-B2` favourite-only path and one `RL-B3` low-total separation path, and record which mechanisms make each credible.
2. Total and margin are separate queries against the same score object. Neither raises the other's `states` count.
3. A close-margin or winner row requires the `RL-B5` terminal branch before it can exceed `LEAN`.
4. Possession imbalance is bidirectional: it can raise the favourite's margin while suppressing the opponent's contribution, so it may not be counted only in the direction that supports the selected total.
5. Recent cover rates, points averages and old head-to-head are `E — diagnostic only`. The single logged NRL event cannot calibrate anything.


### 8.7 Pre-issue checklist


1. `RL-P1`–`RL-P4` status printed, including late mail and the confirmed spine and kicker.
2. Competition and venue scoring baseline stated before any line.
3. Set, field-position and goal-line-entry chain written before any points figure.
4. All eight `RL-B*` branches represented; component budget solved at the supplied total.
5. Favourite-only and low-total-separation paths both written explicitly.
6. Kill-path rows selected from §8.5 and reconciled against the issued order.
7. Golden-point and draw treatment stated for every winner, total and margin row.
8. Team lists, late changes, kicker and conditions refreshed at G31 before the view is appended.
9. Recency block complete per §8.8: L5/L10/L15/L20 for both sides and for head-to-head, continuity count stated, trend verdict per metric, unique-event de-duplication done.
10. Environment block complete per §8.9: Match-window rain and wind recorded, with the bidirectional wet-weather audit run rather than an assumed Under.
11. `REFERENCE_BASE_RATE`, exact threshold, population and denominator recorded for every supplied row per §8.10 as a descriptive diagnostic only; no reference-band, trend or slot-frequency adjustment may move an ordinal (G23.1).
12. Extra-condition support audit (G24) recorded for every handicap, team-total and cushion row; no retrospective contract-family penalty is applied.
13. Separation budget (G20.1) solved for every margin, handicap and cushion row by half, with the closing twenty minutes, interchange state and late-try/penalty-goal paths held separately.
14. Rank-1 implied-target interval (G25.1) stated in the unit of every other supplied line, each remaining row classified `COHERENT`/`PARTIAL_OVERLAP`/`DISJOINT`, and every aggregate budget re-solved conditional on the Rank-1 state.
15. Winner-and-cushion reconciliation (G30.1) whenever Rank #1 is an underdog cushion, with the outright-win and narrow-loss branch ordering stated. Example separation kill path for this sport: a late try plus conversion.
16. Deficit attribution (G14.1) recorded for every weak, absent, returning or small-sample participant: which side's distribution moved and through which exposure step.


### 8.8 Recency, head-to-head and trend windows


Implements `GFA-2` step G13.1 (RULES_GENERAL (archived) §11.3B) and runs at that point in the algorithm, not at the end. Retrieval of L5/L10/L15/L20 for both sides and for the head-to-head series is mandatory; a window that does not exist is recorded with its true count and a missingness code.


Populate one windowed table per side with these metrics, and one head-to-head table:


| Window metric | Content |
|---|---|
| Possession | Sets and set starts, completion rate and error count, opponent-adjusted |
| Field position | Metres and post-contact metres per set, kick metres and average set start |
| Goal-line access | Goal-line entries, repeat sets and line breaks, for and against |
| Defence | Missed tackles and points conceded, held separately from points scored |
| Goal kicking | The current kicker's own last 5/10/15/20 games: attempts, success and range |


**Head-to-head continuity.** Continuity means the same spine and the same kicker. A head-to-head record across a halfback or hooker change fails continuity, which is the exact failure recorded when season averages and close head-to-head history outranked a current defensive collapse.


**Descriptive recency windows (G13.1; revised 2026-09-17).** Retrieve L5/L10/L15/L20 and continuity-qualified H2H with unique-event counts. These windows overlap. Monotonicity and dispersion among their averages are not a statistical trend/noise test. Report direction descriptively; estimate recency decay and opponent/regime effects using time-ordered validation. See SCORING_AND_VALIDATION section 5.


**De-duplication.** The windows overlap by construction and share matches with the head-to-head and venue series. Shrink from unique underlying events under G9; never treat L5, L10, L15 and L20 as four confirmations.


### 8.9 Environment and conditions


Implements `GFA-2` step G15.1 (RULES_GENERAL (archived) §11.3C). Venue classification for this sport is normally **OUTDOOR**.


| Field | Use in this sport |
|---|---|
| Hourly precipitation | Handling errors, short fields, ruck speed and goal kicking all move, and not in the same direction; run the G22 audit |
| Wind speed and direction | Kicking game, drop-outs and goal kicking, resolved against ground orientation |
| Surface state | Official venue source |
| Temperature and humidity | Interchange usage and second-half fatigue under `RL-B4` |


Failure to obtain the match-window forecast for an outdoor or open-roof event yields `WEATHER_NOT_AVAILABLE`, widened total and margin distributions, and a `LEAN` cap on every weather-dependent row. No factor above carries an automatic total direction.


### 8.10 Base-rate anchors and derived stat lanes


**Anchoring (G12.1).** Anchor totals on the competition scoring environment and margins on the competition margin distribution. A cushion is `CONJUNCT` and does not start level with a match total.


**Derived and low-salience fields that are available and routinely skipped:**


| Field | Note |
|---|---|
| Six-again and set-restart counts | Possession-native and often the mechanism behind a blowout |
| Interchange usage and tackle load | Feeds the fatigue state at `RL-S7` |
| Turnaround length and travel | Entered through fatigue and rotation |


## 9. Sport and competition rules reference


Added 2026-09-04; last reviewed 2026-09-04. Standing reference for the laws of rugby league and the competition rules of the NRL Telstra Premiership — the only rugby-league competition in the prediction logs. Supports `RL-P` identity and §6 settlement; introduces no rate, weight or ordering rule.


**Maintenance (RULES_GENERAL (archived) §3, `G2`).** Before the first card of a new NRL season, the pre-season Challenge, or the first finals card, re-verify the golden-point rule (regular season vs finals), the interchange/18th-man rules, the captain's-challenge and Bunker rules, the two-point field-goal rule, the team count and the finals bracket against nrl.com, and update this section **before** issuing the card — the NRL has changed the six-again, interchange, field-goal and finals rules within the last few seasons and adds an expansion team for 2028. The first time another rugby-league competition is forecast (Super League, State of Origin, an international, the NSW/Q Cup), document its full rules here first.


### 9.1 The laws of rugby league


**Field and teams.** A rectangular field ~100 m (try line to try line) × 68 m, with **in-goal areas** at each end. **13 players a side** on the field, **4 interchange** players on the bench.


**Scoring.**
- **Try = 4 points:** grounding the ball in the opponent's in-goal.
- **Conversion = 2 points:** a kick at goal from in line with where the try was scored.
- **Penalty goal = 2 points:** a kick at goal from a penalty.
- **Field goal (drop goal) = 1 point** — **or 2 points if kicked from 40 m or more** (an NRL rule since 2021).


**Possession — the six-tackle set.** The team in possession gets **six tackles** to advance and score. After the sixth tackle without a score, possession hands over (usually via a kick on the fifth or sixth). A **"six again"** (set restart) is called for a ruck infringement by the defence — the tackle count resets to zero with **no penalty and no stoppage** (introduced 2020; a major driver of fatigue-based blowouts, `SFA-RUGBY-LEAGUE` §8, §8.10). The **play-the-ball** restarts play after each tackle; the defensive line must retreat **10 m**.


**Kicking.** A **40/20** kick (kicked from inside your own 40, bouncing into touch inside the opponent's 20) or **20/40** wins the kicking team the next set with the feed. A kick dead in-goal or into touch on the full from open play hands possession to the defending team.


**Match structure.** **Two 40-minute halves**, running clock (stopped only for the Bunker, serious injury and other referee interventions), ~10-minute half-time. Teams change ends at half-time.


**Officiating.** One on-field referee (the NRL trialled and dropped two referees), two touch judges, and the **Bunker** (a central video-review centre) for tries and foul play. **Captain's challenge:** each team has **one** challenge of a referee's ruling (knock-on, ball-strip, obstruction, etc.); it is **retained if successful**, lost if not.


**Interchange and player-safety rules.** **8 interchanges** per team per game from the 4-man bench. An **18th player** may be activated if a team loses players to failed Head Injury Assessments (HIA) or foul-play send-offs beyond a threshold — a concussion/foul-play safety valve, not a free extra rotation. **Send-off (red card)** = off for the game, no replacement; **sin bin (yellow)** = 10 minutes off, no replacement; a "professional foul" in-goal can draw a sin bin plus a penalty try.


### 9.2 NRL Telstra Premiership — 2026


**Structure.** **17 clubs** (10 NSW, 4 Queensland, plus Melbourne, Canberra, and the New Zealand Warriors). **27 rounds**, each club with byes (an uneven fixture, not a full double round-robin). **Magic Round** (Round 11) stages the entire round at one venue. The **State of Origin** period (three interstate representative matches, ~May–July) removes many of the best players from their clubs for those weeks — a large, predictable availability shock (`SFA-RUGBY-LEAGUE` participant handling).


**Ladder.** Win **4**, draw **2**, loss **0**. Separated by: (1) competition points, (2) **points differential**, (3) percentage, (4) tries scored, then further tiebreakers. No bonus points.


**Golden point (extra time).**
- **Regular season:** if level after 80 minutes, **two 5-minute halves** of golden point — **first score of any kind wins** (a field goal, try or penalty goal). If still level after the 10 minutes, the match is a **draw**.
- **Finals:** the same two 5-minute halves, then, if still level, **unlimited golden point until a score** — **finals cannot be drawn**.


**Finals system (top 8).** Same structure as the AFL final-eight:
- **Week 1:** Qualifying Finals **1 v 4**, **2 v 3** (winners get a week off and a home Preliminary Final; losers get a second life); Elimination Finals **5 v 8**, **6 v 7** (losers eliminated).
- **Week 2 (Semi-Finals):** Qualifying-Final losers host Elimination-Final winners.
- **Week 3 (Preliminary Finals):** Qualifying-Final winners host Semi-Final winners.
- **Week 4:** the **Grand Final** (Accor Stadium, Sydney — 4 October 2026), a fixed neutral-ish venue.
Higher seed hosts every final before the Grand Final.


**Pre-season.** The **NRL Pre-season Challenge** (trial matches, February) — heavily rotated, experimental lineups; treat as friendlies, not form.


### 9.3 Settlement (NRL)


- Full-game line and total settle at the **end of 80 minutes for regular-season matches** — most operators settle the head-to-head and line **excluding golden point** (so a regular-season draw is a live outcome and pushes the line / settles the moneyline as "tie" or dead-heat), but **"including golden point"** markets exist — freeze which one the card is using.
- For **finals**, there is no draw; freeze whether the market endpoint is "regulation (80 min)" or "including golden point / eventual winner."
- The **2-point field goal** matters for margin and total settlement — a late long-range one-pointer-that-is-two can flip a handicap on a key number.
- Try-scorer, first-try, and player run/tackle-metre props settle on the official NRL statistics provider; freeze the provider.


### 9.4 Identity checklist (rugby league)


Resolve before any rate work: confirm the competition is the **NRL** (not the NSW Cup, Q Cup, Super League, or an international) and the **season's rule set** (six-again, captain's challenge, 18th-man, 2-point field goal are all current NRL); the **stage** (pre-season trial / regular season / Origin-affected round / finals bracket / Grand Final) and therefore whether a **draw is possible** and how **golden point** is handled; representative-window availability; and the operator's golden-point settlement rule for the market endpoint.
