> **Current research controls (2026-10-01):** [CURRENT_RULES.md](CURRENT_RULES.md) controls new numerical work, source evidence, p_card ranking, availability and admission. The sport mechanics/reference below remain applicable only to their exact competition/season/endpoint after current official verification. Historical q/manual-method instructions or freeze pointers do not qualify a new model. No unregistered league/family can receive an issued numerical forecast.

# Basketball analysis rules

**Live rules for Basketball (NBA, WNBA, NBL, FIBA, EuroLeague, ACB, LKL, LNBP). Markdown-only operation, 2026-09-28.** Read §0 in full for every card: it governs this file.
- §1 onward is the reference algorithm and the competition rules; it is consulted by citation.
- The dated history (settlement learnings and the evidence behind every numbered control) was moved verbatim to `archive/superseded_2026-09-28/sport_history/RULES_BASKETBALL_history_to_2026-09-28.md`, which is no longer in the Markdown tree. A maintainer can recover it from the pinned commit ([Git 3fbf0c981b40](https://github.com/danisgreat/Sports-Research/blob/3fbf0c981b40a1d0e3ffff9725dcc8e383ff05fa/archive/superseded_2026-09-28/sport_history/RULES_BASKETBALL_history_to_2026-09-28.md); [index](HISTORICAL_LINK_INDEX.md#removed-paths-cited-in-operating-documents)) when a control's full text or evidence is needed. The model works from §0 and the sections below.
- Arithmetic: `PROBABILITY_TOOLKIT.md`. Sources: `SOURCES.md` §3.2. Card and self-audit: `CARD_AND_LOG_TEMPLATES.md`. The cross-sport rules are in `CURRENT_RULES.md`, which outranks this file.
- No sport, competition or target is prospectively validated. Every card is LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE.

<!-- LIVE-RULES-PAGE-2026-09-26 -->
## 0. Live rules — one page (consolidated 2026-09-26)

**Status (md-only, 2026-09-28).** This page is the live rule set for this sport and governs the rest of the file. It was consolidated on 2026-09-26 from the numbered controls, the SFA algorithm and the dated sections through 2026-09-25(e). Those dated sections are now archived (see the header). Where a control below is one line, that line is the operative rule, and the archived history is its evidence.

NBA, WNBA, NBL, NCAA, FIBA, EuroLeague, LKL, LNBP, summer league and preseason are never pooled (§8).

### 0.1 Blocking preconditions (§8.1)
| Gate | Requirement | If it fails |
|---|---|---|
| BK-P1 league and clock | Rules era, period length, foul/bonus, overtime terms. A competition with no current regulation packet (LNBP 2026) stays `FAIL` | Stop; no rank, probability or direction (P-451 is the reference fail-close) |
| BK-P2 availability | Official injury report plus both starting fives and the active roster from the official feed, with fetch time (K-1) | Start/minutes mixtures; dependent rows capped. `PROJECTED_BEAT_VERIFIED` needs the S-1 Rev 2 receipt |
| BK-P3 phase identity | Which segment each row settles on (Q1/Q2/H1/H2/full; OT in or out) | A completed segment is `SETTLED_AT_ISSUE` and unranked |
| BK-P4 endpoint | Regulation or including overtime for every total, spread and team total | `UNKNOWN_DEFINITION`; the OT branch stays explicit |

Pregame means before the actual tip. NBL: the first `jumpBall` event in the match feed (K-3). ESPN `plays[].wallclock` gives the tip for NBA/WNBA/NBL. When an injury note shares a surname with an active teammate, print first names and the official active list (`O-ROSTER-NAME-COLLISION`).

### 0.2 Building the score distribution
1. **Anchor.** NBA/WNBA/NBL sides: `TEAM_BASELINE_P` from TB-1-MD (`PROBABILITY_TOOLKIT.md` §4) (K-11). NBA/WNBA totals also anchor on TB-1; **NBL totals do not** (no resolution) and anchor on the population. Uncovered leagues (FIBA, LKL, BCL, EuroLeague, LNBP, LMB) anchor on `BASELINE_P` and print `TEAM_BASELINE_P: NOT_COVERED`.
2. **Team scoring input** = season rate (NBL: a last-10 rate is acceptable because scoring rises through the season) + the opponent's defence to date. A single previous game is the worst predictor (+18% to +36% RMSE); the opponent's defence improves RMSE by 7–11% (K-8, R-1).
3. **Exposure.** Minutes, lineup stints, usage and replacement quality for every decision-driving player (BK-S1). Every top-three scorer and every player of about 20+ minutes has a quantified line (PPG, minutes, rebounds, assists); a bare name is `AGGREGATE_ONLY` and caps the dependent rows (control 20).
4. **Possessions × efficiency** by lineup (BK-S2–S4). Raw PPG and recent shooting percentages never substitute. Shooting inputs print attempts and makes; small samples are width (control 22, G-L11).
5. **Windows and regimes (K-6).** NBL rounds 1–3: print the early-season reference (−8.5, 95% CI −14.3 to −2.7). WNBA early season runs +6.5, so there is no cross-league rule. WNBA 2026 scores +10.7 over 2024–25: exclude or adjust those seasons (M24). A team's first competitive game of a season is `T-BKB-SEASON-OPENER-WIDTH` (width only).
6. **Rest (K-7).** NBA back-to-back against a rested opponent is worth about −1.8 on the margin; totals show no fatigue effect, so fatigue is width. Rest is segmented by half and mechanism (controls 7, 14).
7. **Width (K-5).** References: NBA 19.4/15.1, WNBA 19.5/13.3, NBL 18.7/15.2 (total/margin). Below 0.85 × the reference, name what the card knows. Without a benchmark, a width below 13.6 (total) or 9.4 (margin) needs a reason. **Recent basketball total widths ran about 39% narrow (M31).**
8. **Branches.** All eight BK-B states; for a double-digit spread the four mismatch states (favourite sustain, slowdown, underdog response, underdog suppression) are enumerated separately (§8.3). Overtime is about 4–5.5% of games and adds about 25 points; a total within about 12 of the line keeps OT as explicit mass (K-4).
9. **One joint score object → every row.** Use `PROBABILITY_TOOLKIT.md` §1–§3 for margins (basketball margins are never 0).

### 0.3 Row rules
- **Underdog cushions (C-PLUS-CUSHION, K-9, K-12).** Print the population margin band, `BASELINE_P`, P(underdog wins) + P(loses by ≤ k) and the named reason the margin stays inside k. The weaker team's +1.5/+2.5/+3.5/+5.5 covers only 0.32–0.40 / 0.35–0.43 / 0.38–0.45 / 0.44–0.51. Stated more than 0.05 above that without a receipted mechanism on the favourite's side is `PLUS_CUSHION_UNSUPPORTED`, and RM-1 flips the pair. "The underdog keeps it close" is not a mechanism: P(|margin| ≤ 2) is only 7–12%.
- **Spreads.** Opening separation, maximum lead and closing margin are three distributions (§8.4). Large spreads are factorised (control 16). A same-competition, same-roster meeting is current evidence: decompose it into repeatable versus variance shares before shrinking it (control 25).
- **Totals.** Solve the team-score budget at the supplied line in both directions (control 17). A cushion and an Under can die to one fourth-quarter run: print P(¬R1 ∧ ¬R2) and name the state (control 26, G-L17).
- **Segments.** Nested Q1/H1/full rows on one pace thesis are one primary row (control 1). Q2 is not Q1 (control 2). Quarter shape: NBA Q4 averages 55.3 against 57.6–58.7 in Q1–Q3; the NBL second half runs below the first; the WNBA is flat.
- **Props:** participation × minutes × usage/opportunity × rate (control 8).
- **Intentions are not constraints.** An announced minutes plan keeps a close-game restoration branch (`O-ANNOUNCED-MINUTES-PLAN`). A coach's stated pace intent is at most a branch, never a centre shift (S-2).

### 0.4 Ranking and track record
- Rank by **RM-1 q**. A flipped favourite handicap is capped at SUPPORTED unless `TEAM_BASELINE_P` gives the stated cushion ≥ 0.55. An Under at Rank 1 needs its width at or above the reference (K-13).
- A departure of more than 0.10 from `TEAM_BASELINE_P` names a receipted mechanism (K-11). With resolution near zero, the departure ledger is mandatory (K-10).
- **Track record:** 31 decisions won 58.1% at 0.586, resolution **0.012**. Underdog cushions 3/8 (2/9 at Rank 1/2). Rank 1/2 overall 18 W / 16 L.

### 0.5 Settlement
- Official box scores. ESPN `summary` corroborates, and gives the process record and the starter diff (`starter`, `didNotPlay`; `SOURCES.md` §2.1) (K-1). The NBL match API settles only; skip its `betting`/`odds` keys. Flashscore is an independent third lineage.
- LNBP finals render only in a browser: `JS_ONLY — RENDER REQUIRED` is reachable, so a miss is `RETRIEVAL_MISS` (control 27).
- Record regulation versus OT exactly (control 13) and disruption facts (ejections, injury exits with clock and score).

### 0.6 Withdrawn in basketball — never apply
Derby Under suppression; the FIBA club-qualifier +5.5 possessions coefficient; `C-ABSENCE-DEFENSIVE-PENALTY`; upper-decile pace × ORtg tail sums as a ranking bar; path-count categories; 40–60% top-slot bands; normalised-edge ordering; a fixed cushion-plus-Under coupling sign; the equal-attempt 1.7-SE claim; one-result response rules.

### Numerical shadow model (2026-09-26(c); suspended for md-only operation, 2026-09-28)

The basketball model (A1) is ridge offence/defence ratings with a no-tie normal margin and residual widths. It beat both the league baseline and TB-1 on results **and totals** in the NBA (2012-13 to 2014-15, and again 2023-24 to 2025-26) and the WNBA (2022–2026). In the NBL it beat the baseline and TB-1 on 2025-26 results, but not significantly on 2024-25; NBL totals improved in 2024-25 only. It is maintainer Python, never a card input, and the model does not run it: print `SHADOW: NO_LANE (md-only)` at settlement (`research/sport_models_2026-09-26/README.md` ([removed; recovery](HISTORICAL_LINK_INDEX.md#removed-paths-cited-in-operating-documents))). The hand-computable team baseline that does feed cards is TB-1-MD (`PROBABILITY_TOOLKIT.md` §4).

**Predictability and cards (2026-09-26(e)).** Basketball sides are highly predictable. The model's favourite reached 0.70 in 26–29% of games and won **80–84%** (NBA 79.5%, WNBA 83.7%, NBL 80.4%). Totals at a neutral line rarely reach 0.70 (NBA 12%, NBL 15%). On the cards' own contracts the samples are too small to separate card from model (WNBA: 8 contracts, card 0.170 against A1 0.270; NBL: 6 contracts, 0.285 against 0.322) (`research/predictability_2026-09-26/README.md` ([removed; recovery](HISTORICAL_LINK_INDEX.md#removed-paths-cited-in-operating-documents)); `BASE_RATES_REGISTER.md` §7.8).

### 0.7 Control index (full text in §4 and the dated sections)
1 nested rows dependent · 2 Q1 pace ≠ Q2 · 3 small H2H phase samples weak · 4 minutes are a distribution · 5 blowout/garbage time two-sided · 6 late fouling and OT explicit · 7 rest is mechanistic · 8 prop role coherence · 9 extreme spread is not safety · 10 friendly halves differ · 11 mismatch total and margin share a tree · 12 current roster regime · 13 exact regulation/OT attribution · 14 rest segmented by half · 15 low total can coexist with a blowout · 16 factorised large spreads · 17 team-score budget · 18 late blowouts are multi-axis · 19 names become exposure · 20 quantify every rotation scorer · 21 secondary-scorer usage transfer; floor from worst same-regime shooting · 22 shooting uncertainty with real denominators · 23 spread families incl. underdog separation · 24 conditional margin-total coupling (corrected) · 25 same-competition meeting is current evidence · 26 shared late-game kill state · 27 JS-only field owner is a render escalation. Receipts and references: K-1 official starters/roster · K-2 blowout/rest/shooting states are width · K-3 NBL tip marker · K-4 league reference row · K-5 width benchmark · K-6 early-season and WNBA regime · K-7 back-to-backs · K-8 recency · K-9 plus-cushion disclosure · K-10 departure ledger · K-11 TB-1 anchor · K-12 cushion population rates · K-13 ranking.


## 1. Identity and contract


Resolve league, season/rules era, regulation/OT treatment, venue, scheduled start, quarter/half/full-game phase, team/player statistic, line, and operator terms. NBA, WNBA, NCAA, FIBA, domestic leagues, summer league, and preseason have different clocks, foul rules, rotations, and overtime environments.


A phase already completed at issue is SETTLED_AT_ISSUE and unranked.


## 2. High-value inputs


### Participants and minutes


- Use the newest official injury/availability report and confirmed starting five.
- Separate active status from expected minutes, role, usage, and closing-lineup probability.
- Model replacement minutes and lineup combinations; uncertain minutes widen the distribution rather than making all player projections worthless.
- Record rest, back-to-back, travel, altitude, and recent overtime.


### Possession process


Use opponent-adjusted:


- possessions/pace and transition share;
- half-court efficiency and shot quality;
- rim, three-point, and midrange mix;
- free-throw rate;
- turnover and offensive-rebound rates;
- lineup-specific offence/defence;
- foul/bonus and late-game behaviour.


Raw points per game and recent shooting percentage do not substitute for possessions and shot profile.


## 3. Model


Exposure units are minutes, possessions, lineup stints, usage, and shot/rebound/turnover opportunities. Estimate possessions and per-possession efficiency jointly, with lineup branches and overdispersed shooting outcomes.


Model Q1, Q2, first half, second half, and full game as related but distinct segments. Derive all totals, spreads, winners, and props from one coherent joint game distribution.


For numerical training, benchmark a conditional empirical/joint score distribution and simple regularized possession × efficiency model before a possession/lineup state simulator. Candidate nonlinear models estimate possession, efficiency, shot/rebound/turnover or distribution parameters—not unrelated classifiers for each total/spread. The A2 candidate samples remaining possessions, lineup stints, shot/FT/turnover/rebound outcomes, foul/bonus, late fouling, blowout and overtime, then produces one joint team-score distribution. Direct bivariate Normal/Student-t or distributional boosting forms are challengers only with discrete/support, tail, covariance and held-out calibration checks. None is currently fit or validated.


## 4. Structural controls


1. **Nested rows are dependent.** One Q1/H1/full-game pace thesis gets one PRIMARY_FORMAL row unless another phase has independent evidence.
2. **Q1 pace does not determine Q2.** Use rotation, matchup, fouls, possessions, and shot quality for the next segment.
3. **Small H2H phase samples are weak.** A two-game Q2 acceleration pattern cannot control a current H1 direction.
4. **Minutes uncertainty is a distribution.** Do not use active/inactive as a full-workload binary.
5. **Blowout and garbage time are two-sided.** They change starters' minutes, bench pace, defence, and late scoring differently by contract.
6. **Late fouling and overtime are explicit tails.** Match the operator's inclusion rule.
7. **Rest is mechanistic.** Connect fatigue to pace, transition defence, shot quality, or minutes; no automatic Under/Over.
8. **Player props need role coherence.** Usage, minutes, teammates, defensive matchup, and stat opportunity must point in the same direction.
9. **Extreme spread size is not automatic safety.** For large mismatches, model opening separation, maximum-lead and closing-margin distributions separately. Rest/back-to-back, depth, bench quality, rotation intent, mercy/clock rules where applicable and garbage-time compression can move the final margin in opposite directions.
10. **Friendly halves can be different games.** Preparation matches require starter, bench and closing-lineup mixtures. A strong first half does not validate the full-game side when creators, minutes and late-game roles are deliberately rotated.
11. **Mismatch total and margin share a state tree.** Favourite offensive dominance can lift both margin and total, while underdog suppression can lift margin and lower the total. Derive both branches from the same possession/lineup simulation instead of treating an extreme handicap and an Under as independent safety plays.
12. **Current roster regime must be reconciled explicitly.** A missing rim protector, rebound anchor, primary creator or closer changes minutes, paint deterrence, rebounding, turnover pressure and closing-lineup quality. Old H2H and cover counts remain priors and cannot retain a high evidence grade unless the card explains why the present replacements preserve the old mechanism.
13. **Regulation and overtime attribution is exact.** Settle under the operator's endpoint, then report whether the threshold was already crossed in regulation. Do not describe an Over/Under miss as overtime-caused when regulation alone settled it.
14. **Rest is segmented, not a full-game scalar.** When a back-to-back/travel/fatigue branch is material, estimate its first-half versus second-half effect on transition defence, turnovers, defensive rebounding, shot quality, foul/bonus exposure and closing-lineup probability. If the card names a supported late-fatigue failure path, reconcile it with the side rank before issue.
15. **Low total can coexist with favourite blowout.** In depleted-roster or depth mismatches, model the underdog scoring floor and favourite defensive suppression separately from pace. An Under centre does not make the extreme underdog spread safe.
16. **Large spreads require factorised separation.** Before ranking a double-digit favourite, separately estimate possessions, shooting-efficiency advantage, rebound/turnover conversion, bench/rotation separation and true blowout probability. A small set of recent ugly opponent finals widens the lower tail but cannot by itself place the next game's central margin beyond the line.
17. **Totals require an explicit team-score budget.** For each plausible underdog score at its floor, centre and ordinary high state, solve the favourite score that crosses the total line, and repeat in the other direction. Compare those thresholds with the possession, transition, shooting and bench branches. An underdog offensive downgrade cannot support an Under when the favourite's ordinary high branch consumes the remaining budget.
18. **Late blowouts are multi-axis states.** Separate favourite starter reduction, favourite bench offensive quality/pace, favourite defensive-intensity change, underdog response scoring and closing-margin compression. Garbage time can raise the total while preserving or widening the margin; never apply one automatic scoring or compression sign.
19. **Roster names become exposure before effects.** For every decision-driving player, distinguish available, confirmed starter, bench/closing role, expected minutes, lineup stints, usage and replacement quality. A deep roster can sustain a scoring tail with fewer starter minutes; availability of a star is not the same as full-event star-lineup exposure.


## 5. Live state


Store score, quarter/clock, possession estimate, lineups on court, fouls/bonus, timeouts, rotations/minutes, shot profile, turnovers, offensive rebounds, injuries, and current pace. Rebuild remaining possessions and each later segment independently.


## 6. Sources and settlement


- Official league match centres and play-by-play control state/final.
- Official injury reports and team releases control availability.
- The [NBA statistics glossary](https://www.nba.com/stats/help/glossary) controls NBA definitions; use the equivalent official competition source elsewhere.
- Reputable play-by-play/tracking sources may support lineup and shot-quality features after coverage checks.


Settle from the official final and named statistic provider, preserving regulation/OT and phase boundaries.


## 7. Upcoming-game research sequence


1. Verify league/rules, regulation/OT terms, phase and statistic provider; freeze the complete candidate slate.
2. Retrieve official injury/availability status and likely starters before process history. Recheck the official release and confirmed lineup near tip.
3. Estimate active/start probabilities, minutes/lineup stints and replacement tree, then possessions, shot volume/mix, two- and three-point conversion variance, transition/turnover opportunities, free throws, offensive rebounds, bench scoring and matchup effects.
4. Generate lower, central, shooting-variance, foul/late-foul, blowout and OT branches. Split every material blowout into favourite sustain/slowdown, underdog response/suppression, pace/defensive-intensity and margin-compression states. Phase targets use their own remaining rotations and possessions. Material rest/travel effects are segmented by half and mechanism rather than applied as one full-game scalar.
5. When current roster evidence conflicts with old H2H/cover history, show the baseline/current-regime mixture and make the spread ranking explain why the named separation branch is or is not subordinate.
6. Build the team-score budget at the supplied total and spread, then derive team scores, winner, total and margin from the joint game object. If the line is inside the stated central corridor or ordinary branches cross both sides without explicit weights, cap the directional evidence at LOW under RULES_GENERAL (archived). Player props use a linked `participation × minutes × usage/opportunity × rate` target, not team score alone.


Official league/team sources control current facts; official metric glossaries and audited play-by-play/tracking sources control their defined fields. Query/reference sites may cross-check trends but never override injuries, starters, rules or the operator's price.


## 8. SFA-BASKETBALL — sport forecast algorithm


Algorithm ID: `SFA-BASKETBALL`. Effective **2026-09-02**. Instantiates `GFA-2` (RULES_GENERAL (archived) §11) with basketball content. Process composition only; no fitted weight, scenario weight or published probability is introduced. NBA, WNBA, NCAA, FIBA, EuroLeague, domestic, summer-league and preseason populations are never pooled.


### 8.1 Blocking preconditions


| Precondition | Requirement | Failure output |
|---|---|---|
| `BK-P1` league and clock | League, season/rules era, quarter or half structure, period length, foul and bonus rules, overtime terms | `GATE-TARGET` failure; do not proceed |
| `BK-P2` availability | Newest official injury/availability report plus the confirmed starting five for both sides, re-handshaken at G31 | Model start and minutes mixtures; dependent rows cap at `FORCED RANK` / `MEDIUM-LOW` |
| `BK-P3` phase identity | Which segment each supplied row settles on: Q1, Q2, H1, H2, full game, and whether overtime is included | A completed segment is `SETTLED_AT_ISSUE` and unranked |
| `BK-P4` operator endpoint | Regulation or including overtime, for every total, spread and team total | Label `UNKNOWN_DEFINITION` and keep the overtime branch explicit |


### 8.2 Exposure chain


| Step | Output |
|---|---|
| `BK-S1` | Availability to expected minutes: start probability, minutes distribution, lineup stints, closing-lineup probability and replacement quality for every decision-driving player |
| `BK-S2` | Possession estimate for the frozen segment, with transition share, from both teams' opponent-adjusted pace |
| `BK-S3` | Shot mix by lineup: rim, three-point and midrange share, free-throw rate, shot quality |
| `BK-S4` | Per-possession efficiency by lineup, with turnover and offensive-rebound rates on both sides |
| `BK-S5` | Foul, bonus and late-game behaviour, including intentional fouling and clock state |
| `BK-S6` | Segment linkage: Q1, Q2, H1, H2 and full game as related but separately parameterised states, each with its own rotations |
| `BK-S7` | One joint team-score object with lineup branches and overdispersed shooting, from which every contract is queried |


Raw points per game and a recent shooting percentage never substitute for `BK-S2`–`BK-S4`.


### 8.3 Mandatory branch set


| Branch | Content |
|---|---|
| `BK-B1` | Central possessions with central efficiency for both sides |
| `BK-B2` | Shooting-variance branch: three-point rate high and low against the same possession estimate |
| `BK-B3` | Favourite sustain: starters retained, pace and defensive intensity maintained — raises margin and total together |
| `BK-B4` | Favourite slowdown: starter reduction with bench offence sustaining scoring — can raise the total while compressing or preserving the margin |
| `BK-B5` | Underdog response: opponent scoring against reduced defensive intensity |
| `BK-B6` | Underdog suppression: opponent floor state — raises margin and lowers the total |
| `BK-B7` | Foul, bonus and late intentional fouling adding free-throw possessions |
| `BK-B8` | Overtime under the exact operator endpoint |


`BK-B3`–`BK-B6` are the mismatch state tree. They must be enumerated separately for any double-digit spread; a large handicap and an Under may never be treated as independent safety plays.


### 8.4 Contract derivation map


| Contract | Queried from | Extra condition the mechanism must predict |
|---|---|---|
| Full total | Sum marginal of the joint object | The team-score budget: for each ordinary underdog score at floor, centre and high, the favourite score that crosses the line, and the reverse |
| Spread and handicap | Margin marginal | Opening separation, maximum lead and closing margin as three distinct distributions |
| Team total | Team marginal | That team's own possessions and efficiency, not the game pace alone |
| Q1, Q2, H1, H2 | The segment's own rotations and possessions | A prior segment is neither a ceiling nor a continuation rule |
| Player props | `participation x minutes x usage/opportunity x rate` | Teammate competition, defensive matchup and closing-lineup role |


### 8.5 Kill-path library


| Kill path | Defeats | Evidence origin |
|---|---|---|
| Bench offence sustaining pace after starter reduction | An Under justified by garbage-time slowdown | §4 control 18, C-PL5-BSK-MISMATCH-PATH |
| Underdog scoring floor plus favourite suppression | An Over justified by the favourite's ceiling; and, in reverse, a cushion justified by a low total | §4 controls 15 and 17 |
| Signed turnover and transition effects running both ways | A one-sign turnover argument; transition possessions add to the opponent even while the turnover suppresses their half-court offence | C-PL9-BSK-MISMATCH-FACTORS |
| A short set of recent opponent blowout finals | A central margin placed beyond the line on outcome history rather than on possessions and efficiency | §4 control 16, C-PL9-BSK-MISMATCH-FACTORS |
| Second-half fatigue on a back-to-back, expressed through transition defence and closing lineups | A side ranked on full-game strength while the card itself names the late-fatigue path | §4 control 14, C-PL7-BSK-REST-SEGMENT |
| Overtime supplying points that regulation did not | An Over recorded as validation of a regulation scoring centre | §4 control 13 |
| A missing rim protector, rebound anchor, primary creator or closer | Old head-to-head and cover history retained at high evidence | §4 control 12 |
| Q2 rotation and foul state differing from Q1 | An H1 row inherited from a Q1 pace read | §4 controls 1–3 |


### 8.6 Sport ordering overrides


1. Nested Q1, H1 and full-game rows sharing one pace thesis contribute one `PRIMARY_FORMAL` row. A derivative segment reaches a top slot only on independent segment evidence.
2. An extreme spread is not `OUTSIDE` corridor by size alone. Classify it from the factorised separation estimate in `BK-B3`–`BK-B6`.
3. Rest and travel enter as half-segmented mechanisms, never as a full-game scalar. If the card names a supported late-fatigue failure path, it must be reconciled with the side rank before issue.
4. Minutes uncertainty widens the distribution. It never converts an availability binary into a full-workload assumption, and it never makes a player projection worthless.
5. Cover counts, recent scoring averages and reputation are `E — diagnostic only`.


### 8.7 Pre-issue checklist


1. `BK-P1`–`BK-P4` status printed, with the availability release time.
2. Minutes and lineup-stint distribution stated for every decision-driving player, including replacements.
3. Possession estimate and shot mix stated before any total is discussed.
4. All eight `BK-B*` branches represented; team-score budget solved at the supplied total and spread.
5. For any double-digit spread, the four mismatch states enumerated separately.
6. Kill-path rows selected from §8.5 and reconciled against the issued order.
7. Segment rows carry their own rotations and possessions.
8. Overtime treatment stated for every total, spread and team total.
9. Injury report and confirmed five refreshed at G31 before the view is appended.
10. Recency block complete per §8.8: L5/L10/L15/L20 for both sides and for head-to-head, continuity count stated, trend verdict per metric, unique-event de-duplication done.
11. Environment block complete per §8.9: Venue classified; altitude, rest and travel entered through a named mechanism.
12. `REFERENCE_BASE_RATE`, exact threshold, population and denominator recorded for every supplied row per §8.10 as a descriptive diagnostic only; no reference-band, trend or slot-frequency adjustment may move an ordinal (G23.1).
13. Extra-condition support audit (G24) recorded for every handicap, team-total and cushion row; no retrospective contract-family penalty is applied.
14. Separation budget (G20.1) solved for every margin, handicap and cushion row by quarter, with starter, bench and closing-lineup states and the maximum-lead/compression path held separately.
15. Rank-1 implied-target interval (G25.1) stated in the unit of every other supplied line, each remaining row classified `COHERENT`/`PARTIAL_OVERLAP`/`DISJOINT`, and every aggregate budget re-solved conditional on the Rank-1 state.
16. Winner-and-cushion reconciliation (G30.1) whenever Rank #1 is an underdog cushion, with the outright-win and narrow-loss branch ordering stated. Example separation kill path for this sport: a fourth-quarter closing-lineup run.
17. Deficit attribution (G14.1) recorded for every weak, absent, returning or small-sample participant: which side's distribution moved and through which exposure step.


### 8.8 Recency, head-to-head and trend windows


Implements `GFA-2` step G13.1 (RULES_GENERAL (archived) §11.3B) and runs at that point in the algorithm, not at the end. Retrieval of L5/L10/L15/L20 for both sides and for the head-to-head series is mandatory; a window that does not exist is recorded with its true count and a missingness code.


Populate one windowed table per side with these metrics, and one head-to-head table:


| Window metric | Content |
|---|---|
| Pace | Possessions per 48 or per 40 minutes, opponent-adjusted |
| Efficiency | Offensive and defensive rating, opponent-adjusted |
| Shot profile | Rim, three-point and midrange share, three-point attempt rate and free-throw rate |
| Ball control and boards | Turnover rate and offensive-rebound rate for both sides |
| Margin shape | Final margins in each window, held separately from the win-loss count |
| Decision-driving players | Each player's own last 5/10/15/20 games: minutes, usage and the contract's stat |


**Head-to-head continuity.** Continuity means the same rotation and coach. A two-game head-to-head phase pattern cannot control a current segment, and a meeting played before a trade, an injury return or a coaching change fails continuity.


**Descriptive recency windows (G13.1; revised 2026-09-17).** Retrieve L5/L10/L15/L20 and continuity-qualified H2H with unique-event counts. These windows overlap. Monotonicity and dispersion among their averages are not a statistical trend/noise test. Report direction descriptively; estimate recency decay and opponent/regime effects using time-ordered validation. See SCORING_AND_VALIDATION section 5.


**De-duplication.** The windows overlap by construction and share matches with the head-to-head and venue series. Shrink from unique underlying events under G9; never treat L5, L10, L15 and L20 as four confirmations.


### 8.9 Environment and conditions


Implements `GFA-2` step G15.1 (RULES_GENERAL (archived) §11.3C). Venue classification for this sport is normally **INDOOR**.


| Field | Use in this sport |
|---|---|
| Venue classification | Indoor; record it and move to the rows below |
| Altitude | Denver, Mexico City and similar venues, entered through conditioning and pace, not as a label |
| Rest, travel and back-to-back | Segmented by half under §8.6, never a full-game scalar |


Failure to obtain the match-window forecast for an outdoor or open-roof event yields `WEATHER_NOT_AVAILABLE`, widened total and margin distributions, and a `LEAN` cap on every weather-dependent row. No factor above carries an automatic total direction.


### 8.10 Base-rate anchors and derived stat lanes


**Anchoring (G12.1).** Anchor spreads on the league frequency of covering at that number and totals on the competition scoring environment. A double-digit handicap is `CONJUNCT` and anchors below a match total of similar apparent confidence.


StatMuse is an accepted research accelerator for this sport under `SOURCES.md`, using the verified query patterns recorded there. Every returned row is date-checked and reconciled against the official league source before it is decision-driving, and StatMuse never controls participants, availability, rules, state or settlement.


**Derived and low-salience fields that are available and routinely skipped:**


| Field | Note |
|---|---|
| Closing-lineup probability | Distinct from minutes; controls late scoring and margin compression |
| Foul and bonus state | Feeds `BK-B7` free-throw possessions |
| Officiating crew pace and foul rate | Conditional only, and only where current data support it |


## 9. Sport and competition rules reference


Added 2026-09-04; last reviewed 2026-09-04. Standing reference for the playing rules of basketball and the competition-specific rules of every basketball competition in the prediction logs. Supports `BK-P3` (rule set and duration) and §6 settlement; introduces no rate, weight or ordering rule. **The single most important identity fact in basketball is which rule set applies — FIBA, WNBA or NBA — because it changes game length, the foul/bonus economy, overtime, and the three-point distance.**


**Maintenance (RULES_GENERAL (archived) §3, `G2`).** Before the first card of a new WNBA season, a new FIBA qualifier window, or a new tournament edition, re-verify the rule set (FIBA / WNBA / NBA), the roster and expansion state, the playoff/finals format and any in-season-tournament structure against the official body, and update this section **before** issuing the card. Basketball adds structural events regularly (the NBA play-in tournament, in-season cups, WNBA's move to a best-of-seven final and 15-team league). The first time a new basketball competition is forecast (an NBA card, a EuroLeague card, another national league), document its full rules — including whether it is FIBA or NBA rules — here first.


### 9.1 Universal basketball rules


**Objective.** Two teams of five on court. Score by putting the ball through the opponent's basket: **2 points** inside the three-point arc, **3 points** beyond it, **1 point** per free throw. Most points at the end wins; a tie forces overtime.


**Game clock.** Four quarters. **Stop clock** — the game clock stops on every whistle, made basket in the last minutes, timeout and out-of-bounds. Quarter length is rule-set-specific (§9.2).


**Shot clock.** The offence must attempt a shot that hits the rim within **24 seconds**. After an offensive rebound the shot clock resets to **14** (FIBA, WNBA, NBA all use 14). Failure = shot-clock violation, ball over.


**Possession and restarts.** Opening tip-off is a jump ball. Thereafter, held balls and other tie situations are resolved by the **alternating-possession arrow** in FIBA and the WNBA; the **NBA still uses jump balls** for held balls. After a made basket the opponent inbounds from the baseline without the clock starting until the ball is touched in-bounds.


**Fouls.** A personal foul is illegal contact. Shooting fouls → free throws (2, or 3 beyond the arc, or 1 + the basket if it went in). Non-shooting fouls → inbound, unless the team is **in the bonus / penalty** (over the team-foul limit for the period), in which case → free throws. **Player foul-out** limit and **team-foul bonus** thresholds are rule-set-specific (§9.2). **Technical fouls** (unsportsmanlike conduct, illegal substitution, etc.) and **unsportsmanlike/flagrant fouls** (excessive contact) award free throws **and** possession.


**Violations.** Traveling, double dribble, carrying, 3-second (offensive) lane violation, 5-second closely guarded (FIBA/college), 8-second backcourt (FIBA/WNBA/NBA), backcourt ("over and back"), goaltending / basket interference, out of bounds, kicked ball.


**Substitutions and timeouts.** Unlimited substitutions at dead balls. Timeout counts, who may call one, and when, are rule-set-specific.


**Overtime.** **5 minutes**, repeated until a winner — in every professional rule set. Team fouls usually carry over or reset per rule set (NBA/WNBA: fouls carry; FIBA: bonus is per period and OT counts with the 4th quarter). Full-game betting contracts **include overtime** unless the operator states "regulation only" (RULES_BASKETBALL.md §1; the log's WNBA cards state this explicitly).


### 9.2 Rule-set differences — FIBA vs WNBA vs NBA


| Element | FIBA | WNBA | NBA |
|---|---|---|---|
| Game length | 4 × 10 min (40) | 4 × 10 min (40) | 4 × 12 min (48) |
| Overtime | 5 min | 5 min | 5 min |
| Shot clock / offensive-rebound reset | 24 / 14 | 24 / 14 | 24 / 14 |
| Three-point distance | 6.75 m (6.60 m corner) | 22'1¾" (6.75 m); 22' corner | 23'9" (7.24 m); 22' corner |
| Lane (key) | Rectangular; **no defensive 3-second rule** | Rectangular; **defensive 3-second violation** (tech FT + possession) | Rectangular; **defensive 3-second violation** |
| Personal fouls to foul out | **5** | 6 | 6 |
| Team-foul bonus | **5 per quarter** → 2 FT (OT counts with Q4) | 5 per quarter → 2 FT; also 2 FT on any foul in the last 2 min if the team already has 1; fouls **carry into OT** | Same structure as WNBA (bonus at 5, or 4 in the last 2 min); fouls carry into OT |
| Held ball | Alternating-possession arrow | Alternating-possession arrow | **Jump ball** |
| Goaltending / ball on the rim | Ball is **live once it touches the rim** — either team may play it (no basket interference off the rim) | NBA-style basket interference (cannot touch ball in the cylinder / on the rim on a downward flight to the basket) | NBA-style basket interference |
| Timeouts | Coach requests only, at a dead ball / made basket; 2 in H1, 3 in H2 (max 2 in last 2 min), 1 per OT; **no advance-the-ball** | Team timeouts; **advance-the-ball** to the frontcourt on a timeout in the last ~1–2 min | Team timeouts; advance-the-ball in the last 2 min; coach's challenge |
| Coach's challenge | Competition-dependent (some FIBA events use one) | Yes (one) | Yes (one, retained if successful) |
| Continuous vs stop clock in low minutes | Stop clock throughout | Stop clock | Stop clock |


**Analytical consequences.** A FIBA game is ~17% shorter than an NBA game (40 vs 48 min) and its foul economy is different: fewer fouls to foul out (5) and a quarter-reset bonus mean **star foul trouble bites earlier** and free-throw volume is lower per minute. FIBA's "no defensive 3 seconds" plus a live-off-the-rim ball favour **interior defence and second-chance points**. Never transfer an NBA or WNBA per-game total or pace figure into a FIBA game without rescaling to 40 minutes and the FIBA foul environment.


### 9.3 WNBA


**Structure (2026).** **15 teams** (Portland Fire and Toronto Tempo added for 2026), nominal Eastern/Western conferences but a **single league table for playoff seeding**. **44-game** regular season. Rosters **11–12 players** (hard salary cap frequently forces 11). WNBA plays under its own rule book, which is close to the NBA's but on a **40-minute** game (four 10-minute quarters).


**In-season tournament.** The **Commissioner's Cup** — designated early-season games count both for the standings and a separate Cup table; the two Cup finalists play a standalone final that does **not** count in the standings. Treat a Commissioner's Cup final as its own event/population.


**Playoffs (2026).** **Top 8 by record**, no conference requirement. **First round: best-of-three** (higher seed hosts Games 1 and 2). **Semi-finals: best-of-five.** **Finals: best-of-seven**, 2-2-1-1-1 (higher seed hosts Games 1, 2, 5, 7) — best-of-seven since 2025. Higher seed has home-court throughout. No play-in tournament (that is NBA-only).


**Settlement (WNBA).** Full-game lines include overtime. Quarter/half lines settle at the buzzer of that period. Player-prop providers differ on whether OT counts toward player totals — freeze the provider. A forfeit/abandonment is operator-specific.


### 9.4 FIBA national-team competitions


All FIBA events use the **FIBA rule set** (§9.2): 40-minute games, 5 fouls out, per-quarter bonus at 5, alternating possession, live-off-the-rim ball.


**FIBA Basketball World Cup 2027 — Qualifiers (the "Qualifiers" and "Pre-Qualifiers" cards).**
- **80 teams** across four regions (Africa 16, Americas 16, Asia/Oceania 16, Europe 32). **Six windows**, Nov 2025 → Mar 2027 (Africa five windows). Each window is a ~9-day FIBA international break with **two games per team**.
- **First round:** groups of four, **home-and-away round-robin** over the first three windows. **Second round:** the top three of each first-round group merge into new groups of six, **carrying their head-to-head results forward**, and play the teams they have not yet met, over windows 4–6.
- Qualification slots per region: Europe 12, Americas 7, Africa 5, Asia/Oceania (with the co-host) a similar number — the top teams in the second-round groups qualify for the 32-team World Cup.
- **Pre-Qualifiers** (e.g. the "FIBA Asia Cup 2029 Pre-Qualifiers" card, and European pre-qualifiers) are a preliminary knockout/group stage for lower-ranked nations to reach the main qualifiers — small home-and-away group or two-legged ties, same FIBA rules.
- **Standings within a group:** points (win 2, loss 1, forfeit 0), then, if level, the **mini-league of results between the tied teams** (head-to-head points, then head-to-head point difference, then head-to-head points scored), then overall point difference. Note this is **not** net-points-first like some leagues.
- **Roster:** 12 players per game from a wider registered pool; **NBA and top-league players are frequently unavailable in qualifier windows** because the windows fall inside club seasons — participant identity and effective strength are highly window-dependent. A qualifier "national team" is often a domestic-league + second-tier-Europe roster, not the World Cup roster.


**FIBA Women's Basketball World Cup 2026 and its warm-ups.** Same FIBA rules. Warm-up / preparation games are **friendlies** — treat as a phased, rotation-heavy population (RULES_GENERAL (archived) friendly handling), not competitive form.


### 9.5 LNBP (Mexico) and the 2026 Copa Value


**Onboarding status: `PARTIAL / BLOCKING FOR A FUTURE CARD`.** P-279 was the first Copa Value card and was issued before this competition existed in the reference section, so it failed the new-competition onboarding requirement in RULES_GENERAL (archived) §3. This subsection repairs the verified reference facts after the event; it does not retroactively make P-279 compliant and it is not permission to forecast the next Copa/LNBP event until the unresolved fields below are closed.


**Verified 2026 competition identity.** The Copa Value is an LNBP mid-season tournament for the top eight teams after the first half of the 2026 regular season. The 2026 edition runs 3–6 September at the Gimnasio Marcelino González in Zacatecas, using a single-game, single-elimination bracket: four quarterfinals, two semifinals and a final. Mineros is the arena's resident team and therefore had a real host/home-floor state against Abejas; the single-site label must not be converted into neutral-court treatment. The [Government of Zacatecas event release](https://www.zacatecas.gob.mx/zacatecas-epicentro-del-basquetbol-nacional-con-la-copa-value-2026-gobernador-david-monreal/) owns the host venue/date/format statement; the dated [NTR Zacatecas match report](https://ntrzacatecas.com/2026/09/mineros-avanza-a-las-semifinales-de-la-copa-value/) confirms that Mineros–Abejas was a quarterfinal, that Mineros won 96–86 and that the winner advanced to the 5 September semifinal. Named reporting may corroborate those fields but does not own the league's playing rules.


**Playing-law and roster gap.** No accessible 2026 LNBP/Copa Value regulations or field-owner rulebook was recovered in the P-279 promote/archive audit. Do **not** infer from the league's professional status, FIBA affiliation, a live-score front end or a sportsbook that the exact LNBP clock, bonus, challenge, roster/import, overtime, abandonment or player-eligibility provisions equal another FIBA competition. [FIBA's official download page](https://about.fiba.basketball/en/services/resource-hub/downloads) states that the 2026 FIBA rules become effective on **1 October 2026**; on 3 September the 2024 FIBA edition was still the current international rule baseline. That date distinction does not establish which edition or local variations LNBP adopted.


Before another LNBP or Copa Value card, obtain an exact current league regulation, competition bulletin or field-owner statement and record all of the following at `BK-P1`/`G2`: period length and clock; foul-out/bonus/challenge rules; overtime and tie resolution; Copa bracket/seeding and any reseeding; home/bench designation at the single site; roster size and game-day activation; foreign/import-player and replacement eligibility; postponement/forfeit/abandonment treatment; and whether the Copa result affects the regular-season table. Until that packet is complete, `BK-P1 = FAIL`, the event is not forecastable, and no LNBP rate may be pooled with a generic FIBA population.


**Settlement.** Freeze the operator's own regulation-versus-overtime, postponement, abandonment and player-prop terms. Without them, full-game side/total action is `UNKNOWN_DEFINITION` even if a research settlement is direction-invariant. P-279 did not require overtime and every recovered high-quality final agreed on 96–86, so its winner, ±5.5 and 169.5 result fields are direction-invariant; that does not validate an unstated operator rule. Quarter/player detail remains provisional unless an exact LNBP field-owner box or a provider with a frozen definition is recovered. Fox Sports México's statement that Mineros won all four quarters conflicts with the provisional 20–23 third-quarter row and may not control phase settlement.


**Source state at review (2026-09-04; superseded for results by §"2026-09-17(b)" — the domain now returns HTTP 200 with a JavaScript-only shell, and the per-Jornada finals are recoverable by rendering `lnbp.mx/<Team>/team_results.html`).** `https://lnbp.mx/` identifies the field owner but returned HTTP 403 to the scripted research route; the official mobile-app listing did not expose a validated API, stable event IDs, correction history or use/retention terms. Use the exact LNBP record when accessible; otherwise seek an official club/static report and then two independent dated high-quality reports for a provisional final. Never upgrade the fallback into a league-wide structured-stat source.


### 9.6 Identity checklist (basketball)


Resolve before any rate work: **rule set (FIBA / WNBA / NBA / other league)** and therefore game length, foul-out limit, bonus threshold, three-point distance and overtime economy; competition and stage (regular season / in-season cup / qualifier window / knockout / friendly); roster availability for the specific window; whether the contract is **regulation-only or includes overtime**; the standings tiebreak system if the card touches qualification; and the operator's forfeit/abandonment rule.
