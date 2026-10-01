# Cricket analysis rules

**Live rules for Cricket. Markdown-only operation, 2026-09-28.** Read §0 in full for every card: it governs this file.
- §1 onward is the reference algorithm and the competition rules; it is consulted by citation.
- The dated history (settlement learnings and the evidence behind every numbered control) was moved verbatim to `archive/superseded_2026-09-28/sport_history/RULES_CRICKET_history_to_2026-09-28.md`, which is no longer in the Markdown tree. A maintainer can recover it from the pinned commit ([Git 3fbf0c981b40](https://github.com/danisgreat/Sports-Research/blob/3fbf0c981b40a1d0e3ffff9725dcc8e383ff05fa/archive/superseded_2026-09-28/sport_history/RULES_CRICKET_history_to_2026-09-28.md); [index](HISTORICAL_LINK_INDEX.md#removed-paths-cited-in-operating-documents)) when a control's full text or evidence is needed. The model works from §0 and the sections below.
- Arithmetic: `PROBABILITY_TOOLKIT.md`. Sources: `SOURCES.md` §3.3. Card and self-audit: `CARD_AND_LOG_TEMPLATES.md`. The cross-sport rules are in `CURRENT_RULES.md`, which outranks this file.
- No sport, competition or target is prospectively validated. Every card is LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE.

<!-- LIVE-RULES-PAGE-2026-09-26 -->
## 0. Live rules — one page (consolidated 2026-09-26)

**Status (md-only, 2026-09-28).** This page is the live rule set for this sport and governs the rest of the file. It was consolidated on 2026-09-26 from the numbered controls, the SFA algorithm and the dated sections through 2026-09-25(e). Those dated sections are now archived (see the header). Where a control below is one line, that line is the operative rule, and the archived history is its evidence.

### 0.1 Blocking preconditions (§10.1) and the three evidence objects (§2)
| Gate | Requirement | If it fails |
|---|---|---|
| CR-P1 format and rules | Overs, playing conditions, powerplay definition, DLS/shortening, super over, no-result | Stop |
| CR-P2 target identity | Named-day runs, remaining-day runs, innings total, phase total, milestone or result, each with its own endpoint (control 11) | A phase, innings and match target never share a label |
| CR-P3 toss and innings order | Toss from the TOSS FACT ladder (T1–T6), or an explicit bat-first/chase mixture. Check the ESPN `notes[]` toss at toss + 5 minutes (§2.7) | Innings-total rows capped at LOW unless the direction survives both branches (override 2) |
| CR-P4 XIs and phase roles | Both XIs; the phase map names the openers, the **incoming Nos. 3–4 and both opposing new-ball bowlers** (control 20). After the toss the XIs exist: "unresolved" is `RETRIEVAL_MISS` (control 26) | Unconfirmed participants stay role branches; XI-dependent rows capped |
| CR-P5 strip and conditions | `TOSS STATUS`, `STRIP STATUS` and `MATCH CONDITIONS STATUS` kept separately, each with its search trail (§2) | Continue with a disclosed evidence limit; never invent the strip |

- **Conditional activation (control 32).** A contract defined by innings role ("team batting first", "the chase") with the toss unretrieved stores the activation condition beside the contract, names the forbidden substitute in advance, and at settlement grades `NO ACTION / CONDITION NOT MET` before looking at the score. Such rows are excluded from every statistic.
- **Toss and strip.** Only P1–P5 establish the exact strip. A previous match at the venue is a **different strip** (P6). Duplicated unusual feed labels across front ends are one automated lineage (§2.4). The toss decision is weak context, never a pitch report or a direction (§2.8, control 5). **Bowl-first does not mean low-scoring.**
- **Debutants.** ESPN `debuts[]`: a debutant is `NO_PRIOR_FORMAT_RECORD` and contributes width only (2026-09-19).
- Record whether the freeze was `PRE_TOSS` or `POST_TOSS` (`T-CRI-POST-TOSS-FREEZE` compares them).

### 0.2 Building the run distribution
1. **Anchor.** `BASELINE_P` from the venue window by innings order where one exists (§2.6 attempts it; `INSUFFICIENT_VENUE_HISTORY` is an honest state). There is no TB-1 lane (`TEAM_BASELINE_P: NOT_COVERED`). Sparse or inaugural competitions shrink hierarchically (control 17).
2. **Innings-order mixture (control 21).** Before the toss, every innings **and phase** total is a bat-first/chase mixture; after it, the realised branch. The chase is capped by the target and may end early. Windows are split by innings order: a chase powerplay may not size a batting-first powerplay (M24; P-482).
3. **Resources through phases.** Phase-end state (runs, wickets, which batters survive, bowling overs left) carries into the next phase (controls 16, 19). One CDF per target integrates every nested line (controls 12, 14). Wickets change the rate, the ceiling and termination (CR-S6).
4. **Current-surface evidence.** Same-venue, same-week scoring in another format is a named, weighted adjustment (control 25). A same-venue current-regime innings that already cleared the line gets its own mass and a named reason it won't repeat (control 30, G-L20).
5. **Bowling replacement chain.** Outgoing role → incoming bowler → the residual attack's phase resources; never a one-sign absence (control 31).
6. **Tests.** Session priors start from the batting side's **current-series** run-rate table (control 27). A Test winner label is a win/draw/loss time budget with a resistance branch (control 28). Rearguards are survival processes (control 18).
7. **Recency (R-1).** Magnitudes are `NOT_YET_DERIVED` for cricket and are not imported from baseball. A single prior innings on a different strip is a weak comparator (P-457). Streaks need a named mechanism (control 24).
8. **Interruptions.** Runs scored before a stop count. DLS is an endpoint event, not a surface misread (G-L23). Incomplete is not zero (control 15).

### 0.3 Row rules
- Phase and innings rows on one innings are dependent; only one is primary without independent phase-participant evidence (override 1).
- Nested lines follow the CDF: a higher Over never outranks a lower Over on likelihood (override 4).
- Upper Unders need a finisher/death branch (control 4). A low projected total is checked for defendability before any winner lean (control 6).
- Most cricket contracts are `FREE`, not forced pairs. That is part of why cricket Briers look better than MLB's: **contract geometry, not skill** (G-L22).

### 0.4 Ranking and track record
- RM-1 applies its global recalibration only (no cushion-class rows; no held-out cricket card was re-ordered). Rows stated at 0.55–0.60 read as coin flips.
- **Track record:** 34 decisions won 64.7% at 0.630; resolution 0.039 but **reliability 0.022, the worst calibration of any sport with n ≥ 30**. Unders 9/12 at 0.589 against Overs 7/12 at 0.631 (`T-TOTAL-DIRECTION-LEAGUE`, non-binding). Rank 1/2 17 W / 10 L.

### 0.5 Settlement
- Official scorecards only, never narrative reports. Zero is not a duck.
- Six-over checkpoints: the ESPN matchnote `Powerplay 1: Overs 0.1 - 6.0 (Mandatory - N runs, W wickets)`, valid only for a full 6.0-over powerplay (control 29).
- Settlement tables print the contract text (several historical rows were blank).
- Record rain stoppages, overs lost and DLS revisions with the score (§16.11(o)).

### 0.6 Withdrawn in cricket — never apply
"Bowl-first means low-scoring"; guaranteed venue-history availability; the six-rung/eight-rung pitch ladder numbering (replaced by the separate toss and strip ladders); the "bimodal phase total" shape claim from two observations (L-112); additive cricket tail shortcuts; pseudo-tails, path-count categories, 40–60% bands and normalised-edge ordering.

### Numerical shadow model (2026-09-26(c); suspended for md-only operation, 2026-09-28)

The cricket model (A1) is Elo for the result plus a ridge batting/bowling/venue first-innings total, priced 50/50 on who bats first. Second innings are target-censored and not modelled. **On the IPL (2016–2026), v1 was worse than a coin flip on results and worse than the format mean on totals**; v2 (elo_k 4, lam_team 200, re-selected on 2016–19) is only level with both. Cricket has **no demonstrated model skill**. It is maintainer Python, never a card input, and the model does not run it: print `SHADOW: NO_LANE (md-only)` at settlement (`research/sport_models_2026-09-26/README.md` ([removed; recovery](HISTORICAL_LINK_INDEX.md#removed-paths-cited-in-operating-documents))). The hand-computable team baseline that does feed cards is TB-1-MD (`PROBABILITY_TOOLKIT.md` §4).

**Predictability (2026-09-26(e)).** IPL results are no better than a coin flip for a team-strength model (Brier 0.254 against 0.250). A STRONG cricket result row needs event evidence (the toss, the strip and the XI), not team strength (`research/predictability_2026-09-26/README.md` ([removed; recovery](HISTORICAL_LINK_INDEX.md#removed-paths-cited-in-operating-documents)); `BASE_RATES_REGISTER.md` §7.8).

### 0.7 Control index (full text in §5 and the dated sections)
1 legal deliveries · 2 phase ≠ innings · 3 wicket-cluster floor · 4 finisher ceiling · 5 toss is context · 6 winner independence · 7 adjusted venue samples · 8 direct ceiling conflict · 9 rain/dew conditional · 10 milestones boundary-sensitive · 11 target identity first · 12 one CDF for nested totals · 13 stochastic exposure · 14 calibration preserves geometry · 15 incomplete is not zero · 16 phase-to-innings is joint · 17 sparse competitions shrink · 18 Test rearguards are survival processes · 19 retained resources reverse phase direction (which wickets fall) · 20 phase participants outrank phase H2H (Nos. 3–4, both new-ball bowlers) · 21 innings-order mixture for innings and phase totals · 22 near-start identity gaps cap evidence · 23 overlap-aware evidence units · 24 runs are neither self-correcting nor self-perpetuating · 25 same-venue, same-week cross-format evidence · 26 retrieve XIs after the toss · 27 current-series tempo prior; restart is width · 28 Test winner as a three-way time budget · 29 phase-checkpoint settlement route · 30 direct same-venue current-regime ceiling · 31 bowling replacement chain · 32 conditional activation.


## 1. Identity and contract


Resolve format and competition: Test, ODI, T20, The Hundred, domestic format, international, warm-up, or exhibition. Record innings, batting team, target/chase state, scheduled balls/overs, legal-ball definition, powerplay/field restrictions, DLS/shortening terms, winner/tie/super-over rules, and exact player/team metric.


Never assume that a broadcaster label uses the same boundary as the user's contract. Official current-season playing conditions control.


### Underlying cricket target hard gate


Freeze one exact target before modelling or mapping a line:


| Target ID family | Outcome and endpoint |
|---|---|
| `TEST_DAY_RUNS_FULL` | All runs by both teams during a named Test day, through stumps or earlier match completion |
| `TEST_DAY_RUNS_REMAINING` | Additional runs after a timestamped live state until that named day ends |
| `TEAM_FIRST_INNINGS_TOTAL` | Named team's completed first-innings total, even if it continues on another day |
| `TEAM_INNINGS_RUNS_REMAINING` | Additional runs from a frozen innings state to all-out, declaration, chase/forfeit or contract endpoint |
| `SESSION_RUNS` | Runs inside an officially defined session boundary |
| `MATCH_RESULT` | Governing result state, including draw/tie/abandonment rules |


These are not aliases. A day total may cross innings and batting-team boundaries; an innings total stops at that innings endpoint. Pregame, end-of-day and live versions have distinct target/horizon/model IDs.


## 2. Toss, exact-strip and match-conditions hard gate — CR-2026.09.21-1


For every cricket card, keep **three different evidence objects**. They are not aliases:


- **TOSS STATUS:** `VERIFIED` / `NOT_VERIFIED_AFTER_SEARCH` / `NOT_YET_PUBLISHED` / `CONFLICTING`;
- **STRIP STATUS (exact-match pitch report):** `OBSERVED` / `NOT_FOUND_AFTER_SEARCH` / `CONFLICTING` / `STALE_ONLY`;
- **MATCH CONDITIONS STATUS:** `OBSERVED` / `NOT_AVAILABLE` / `CONFLICTING`.


A card is not compliant merely because it prints one of those labels. It must show the relevant search attempts, source lineage and freshness. Toss facts, exact-strip observations, venue history and weather are stored separately so one cannot silently stand in for another.


### 2.1 TOSS FACT ladder


Search the toss in this order:


| Rank | Source lane | Use |
|---:|---|---|
| T1 | Official competition/national-board exact-match centre or board-branded sanctioned scorecard | Toss winner, bat/bowl decision, XIs |
| T2 | Official competition/board verified video or rights-holder broadcast | Toss, captain interview, confirmed-XI graphic; record match timestamp |
| T3 | Official team/competition live blog or timestamped official post | Toss/XI corroboration |
| T4 | Admitted structured cricket endpoint already in `SOURCES.md` (for example the ESPN cricket summary route where covered) | Toss note, XIs and event state; ESPN/ESPNcricinfo variants sharing the same record are one lineage |
| T5 | High-quality exact-match specialist scorecard/commentary | Toss corroboration |
| T6 | Reputable independent exact-match reporting | Fallback/corroboration; identity/date/venue must match exactly |


If this ladder does not verify the toss, record `TOSS STATUS: NOT_VERIFIED_AFTER_SEARCH`. **Do not infer the toss winner merely from which side bats first.** If the contract activates only for the batting-first/chasing side, control 32 remains binding.


### 2.2 STRIP/PITCH EVIDENCE ladder


Only P1–P5 can establish the current exact-match strip. P6–P8 are context only.


| Rank | Source lane | Evidence class | Can set `STRIP STATUS: OBSERVED`? |
|---:|---|---|---|
| P1 | Named current-match rights-holder/official broadcast pitch report by a presenter, curator/groundsman or captain | `EXACT_MATCH_OBSERVED` | Yes |
| P2 | Current curator/groundsman/venue/board statement about the exact strip | `EXACT_MATCH_OBSERVED` | Yes |
| P3 | Official board/competition toss report or preview quoting a captain/coach/curator on the wicket/strip | `EXACT_MATCH_REPORTED` | Yes |
| P4 | Specialist live commentary explicitly transcribing a named broadcast pitch report | `EXACT_MATCH_REPORTED` | Yes, but lineage-tag to the broadcast it transcribes |
| P5 | Named reputable journalist/reporting outlet with match-specific observed/quoted strip information | `EXACT_MATCH_REPORTED` | Yes |
| P6 | Immediately preceding same-venue match in the same series/tournament | `DIFFERENT_STRIP_CONTEXT` | No, unless same-strip reuse is explicitly confirmed |
| P7 | Same-venue, same-format/rules-era scoring and phase baseline by innings order | `VENUE_HISTORY` | No |
| P8 | ICC post-match pitch rating or an explicitly quoted approved historical surface metric such as PitchViz | `VENUE_REPUTATION_CONTEXT` | No |


A previous match is a **different strip** unless a current curator/broadcast/field-owner statement explicitly confirms reuse. Weather or an automated conditions field cannot imply unreported grass, hardness, pace, seam, turn or deterioration.


### 2.3 Mandatory retrieval sequence before `NOT_FOUND_AFTER_SEARCH`


At minimum:


1. exact competition/board match centre and sanctioned scoring partner;
2. official/rights-holder live video or verified board/competition video channel;
3. `"<venue>" pitch report`, `"<venue>" curator`, `"<venue>" groundsman/groundstaff`;
4. official team/competition live blog or current exact-match report;
5. reputable specialist live commentary / match preview / “pitch and conditions” item;
6. named reputable cricket reporting;
7. P6 previous same-venue match context;
8. P7 venue-format historical baseline, or the explicit state `INSUFFICIENT_VENUE_HISTORY`;
9. P8 historical pitch-rating/surface context where applicable.


For marquee international/franchise fixtures, stopping after one or two failed routes is not compliant. For sparse associate/minor domestic cricket, `NOT_FOUND_AFTER_SEARCH` is an honest outcome after the shown search.


### 2.4 Source-lineage fingerprint and automated metadata


Identical or near-identical unusual structured pitch fields across different front ends — for example the same `Pitch Condition`, `Batting Condition`, pace or spin labels — are a **suspected shared upstream feed** until provenance proves independence.


Store unattributed feed-generated labels as:


`CLAIM_TYPE = AUTOMATED_PITCH_METADATA`


They may be weak supporting context, but:


- `STRIP_OBSERVATION = NO`;
- they do not count as multiple independent pitch sources;
- they cannot by themselves set `STRIP STATUS: OBSERVED`;
- a specialist transcript and the original broadcast it transcribes are one lineage.


Generic fantasy-cricket/tipping/“Dream11” pitch-report pages remain excluded.


### 2.5 Official-page staleness


Official does not automatically mean current. If an official dynamic page remains `UPCOMING`, blank or otherwise stale while fresher reliable evidence shows a live/final/toss/XI state:


1. mark the affected field `STALE`;
2. keep still-valid identity/schedule fields if they remain correct;
3. retrieve another official/static/sanctioned scoring route;
4. reconcile with independent high-quality evidence;
5. do not let the stale field control the current state.


### 2.6 Venue-history missingness


The same-format venue baseline is **attempted**, not presumed to exist. A new venue, a new competition, a rules-era break or insufficient comparable history can produce:


`VENUE_HISTORY_STATUS = INSUFFICIENT_VENUE_HISTORY`


In that state, use a broader explicitly labelled comparable prior only if appropriate and widen uncertainty. Never invent a sample merely to satisfy a checklist.


### 2.7 Toss-window and final refresh


At the competition's actual toss window, refresh the official match centre, official/rights-holder video, structured toss/XI endpoint where available, specialist live commentary and official team/competition updates. Immediately before issue refresh **event state, toss, confirmed XI, late changes, exact strip, weather/radar and source conflicts**.


Record explicitly whether the forecast freeze was `PRE_TOSS` or `POST_TOSS`.

**Toss check at toss + 5 minutes (added 2026-09-25; 2026-09-22 audit).** Where the registered ESPN `summary?event=` route carries a `toss` note in `notes[]`, query it about five minutes after the competition's usual toss time and before the final refresh. In P-482 the CPL toss (about 30 minutes before the first ball, roughly 08:30 AEST) was probably public before the 08:54:41 AEST final refresh, yet it was not retrieved: a probable `RETRIEVAL_MISS` under control 32.


### 2.8 Toss decision as weak circumstantial context


Once verified, the captain's decision to bat or bowl may be `D-conditional` context because captains have direct local information. It **never** becomes a pitch report by itself and never independently creates or reverses an Over/Under or winner lean. It is subordinate to an actual observed/reported strip source.


## 3. High-value inputs


- Confirm toss, innings order, full XIs, batting order/roles, wicketkeeper, bowling resources, substitutes, and material availability.
- Estimate balls faced, batting position, bowling phase/overs, wicket-taking resources, and likely death roles.
- Use opponent-adjusted scoring and dismissal rates by phase and matchup.
- Build a format/competition/season/venue baseline with innings order, contest strength, boundary dimensions, and rules era.
- Record match-window weather, dew only when observed/forecast and mechanistically relevant, interruptions, and DLS risk.
- Use direct H2H only with meaningful XI/role/format continuity.


## 4. Model


The active MDS v2.9 method remains a qualitative rate × exposure corridor. The following numerical models are **training candidates only** under NTS-2026.09.02-v0.3. H0 is not built; none is fit, calibrated, validated, champion, or authorised to publish a probability.


### 4.1 Candidate probability-model ladder


| Candidate | Cricket role | Required caution |
|---|---|---|
| Conditional empirical CDF | Transparent target/state baseline | Sparse states require chronological hierarchical pooling |
| Poisson regression | Equidispersion diagnostic only | Cricket totals may be overdispersed; convenience is not model fit |
| Hierarchical negative-binomial distributional regression | Primary simple count challenger for integer run targets | One component may miss declaration/weather/innings-switch multimodality |
| GAMLSS-style or other hierarchical location/scale/shape regression | Interpretable flexible distribution challenger | Family, link, support, skew and tail behavior require held-out selection |
| Truncated/discretised Normal or Student-t | Direct day/innings-total benchmark | Untreated negative/fractional mass is invalid; symmetry may be wrong |
| Joint non-crossing quantile model | Flexible-shape challenger | Independently estimated quantiles can cross; interpolation and tails must be frozen |
| Ordered bucket/cumulative-link CDF | Discrete monotone challenger | Bucket and tail resolution must be selected before TEST |
| NGBoost/distributional boosting | Nonlinear conditional-distribution challenger | The chosen family can still have wrong support or tails |
| Bayesian hierarchical state simulator | Preferred structural A2 challenger | Highest data/transition/validation burden; not promoted by architecture alone |


Mean and standard deviation are sufficient only when they identify a tested predictive family with valid support and calibrated tails. For Test cricket, a stored PMF/CDF or posterior predictive trajectory sample is preferred because playable time, declaration, innings changes, collapse and early completion can create skewed or multimodal outcomes.


Zero-inflated/hurdle families are not automatic defaults. A no-play day is an exposure/weather scenario with its own label/void rule, not generic evidence that normal cricket scoring follows a zero-inflated count process.


### 4.2 Test cricket structural A2 candidate


Exposure units are sessions, scheduled and playable time, legal balls/overs, wickets, crease time, batter/bowler resources, ball age/new-ball cycles and innings state.


At the frozen start state, record only prediction-time-known fields:


- innings, batting side, score, wickets, lead/trail, day/session and target endpoint;
- striker/non-striker, current scores/balls, batting order and replacement queue;
- current/available bowlers, spell/workload, attack composition, ball age and new-ball eligibility;
- expected playable overs/time with weather, light, delay and over-rate scenario uncertainty;
- venue/era, exact-match strip evidence, dynamic team/player strengths and matchup;
- declaration, follow-on, chase, match-completion and draw/win incentives.


The engine then:


1. samples playable exposure and other discrete scenarios using only cutoff-safe information;
2. estimates a coupled transition such as `P(runs, wicket, extras | state)`, or another factorisation that preserves run/wicket dependence;
3. updates score, wickets, participants, bowling state, ball age, clock/session, innings and lead/trail;
4. applies explicit hazards for dismissal, all-out, declaration, innings change, chase/match completion, stumps, weather/bad-light interruption and abandonment/void treatment;
5. simulates to the exact target endpoint across scenario and parameter uncertainty;
6. stores one predictive distribution from which every contract is derived.


Runs and wickets may not be modelled as unrelated totals. A wicket changes subsequent rate, batter exposure, collapse risk, innings termination and possible transition to the next innings. A survival/hazard or competing-event component can model part of this process, but it is not a complete run-total distribution.


For `TEST_DAY_RUNS_FULL`, continue across any innings/team transitions until the day endpoint. For `TEAM_FIRST_INNINGS_TOTAL`, stop at that innings endpoint even if it occurs on a later day.


### 4.3 Limited-overs structural candidate


Exposure units are legal balls, wickets, batting position, batter/bowler resources, scheduled balls/overs and opening/powerplay, middle and death phases. Estimate a ball/over transition such as `P(runs, wicket, extras | state)`, conditioned on target, required rate, current resources, matchup, venue/conditions and phase. Wickets change both rate and remaining ceiling. A chase is capped by the target and may end early; DLS/shortening is a distinct rules/state branch.


Limited-overs and Test engines do not share fitted distributions merely because both use runs and wickets.


### 4.4 One CDF for every line


For integer target `Y` with `F(k)=P(Y<=k)`:


- `P(O185.5) = P(Y>=186) = 1-F(185)`;
- `P(O235.5) = P(Y>=236) = 1-F(235)`;
- `P(U235.5) = P(Y<=235) = F(235)`;
- `P(U285.5) = P(Y<=285) = F(285)`.


Therefore `O235.5` and `U235.5` are exact complements. `O185.5` and `U285.5` overlap and both win for `186<=Y<=285`; their joint probability is `F(285)-F(185)`, not the product of their marginals. Ask for every real line and its same-time price, but train the one target distribution. Without odds, rank likelihood only; do not claim value.


### 4.5 Training and evaluation


Use match/series-grouped chronological `TRAIN -> TUNE -> CAL -> untouched TEST`, followed by immutable E1-P shadow output. Random delivery-row splits, later lineups, realised weather, post-state declarations and closing prices fail the point-in-time gate.


Primary metrics are CRPS/ranked probability score and log score for the full distribution; randomized PIT/discrete-rank calibration; 50/80/90% interval coverage and width; and threshold Brier/log score/reliability at frozen lines. MAE/RMSE/bias are secondary point diagnostics. Required slices include target, pregame/live horizon, day/session/innings, venue/region, team/participant support, weather/exposure, declaration/innings-switch and OOD state.


Calibrate the whole CDF or a shared monotone transformation. Separate threshold calibrators that can reverse nested-line ordering are prohibited as the production output.


## 5. Structural controls


1. **Exact-ball contracts use legal deliveries.** Reconstruct from official delivery data when no phase row exists, reconciling extras and legality.
2. **Phase does not equal innings.** A fast or slow first phase cannot determine the full total.
3. **Wicket-cluster floor.** Map which bowlers and phases can create early/middle/death collapse, including support bowlers.
4. **Finisher ceiling.** Upper Unders require a separate last-phase branch using likely batters, wickets remaining, boundary access, and death bowling.
5. **Toss is context, not direction.** Bowl-first does not automatically support an Under or winner.
6. **Winner independence.** If a selected side is projected to post a low target, model whether that target is defendable against the confirmed chase.
7. **Venue samples are adjusted.** Do not mix formats, eras, innings order, or target-censored chases.
8. **Direct ceiling conflict.** A same-season comparable high innings cannot be dismissed by a venue median without current XI/bowling/strip evidence.
9. **Rain/dew are conditional.** DLS, interruptions, wet ball, skid, swing, spin grip, and chase incentives can have different signs.
10. **Player milestones are boundary-sensitive.** Model crease time and dismissal risk, not reputation alone.
11. **Target identity precedes the line.** Day runs, remaining-day runs and innings totals cannot share a label or be substituted after seeing the result.
12. **One CDF controls nested totals.** Over probability decreases as the line rises; Under probability increases. A violation is a failed model record.
13. **Exposure is stochastic.** Weather, light, over rate, early match completion and declarations change playable opportunities; they are scenario branches, not fixed afterthoughts.
14. **Calibration preserves geometry.** Do not calibrate each line independently and then publish crossed probabilities.
15. **Incomplete is not zero.** Abandoned, void, censored or not-yet-completed innings/days follow the frozen target/label policy and are never silently recorded as ordinary zero-run outcomes.
16. **Phase-to-innings transition is joint.** Link a powerplay/first-five/first-six target to the innings only through the phase-end state distribution—runs, wickets, batters/resources, bowling allocation and conditions. Phase runs alone cannot project the completed innings. A correct phase direction does not validate the innings direction, or vice versa.
17. **Sparse or inaugural competitions require hierarchical shrinkage.** One venue innings, one prior match or a short direct series cannot own the baseline. Separate competition, venue, team/player and broader format priors; disclose their compatibility and weight, then condition on verified toss/XI/strip. If toss/XI or start state is unresolved, lower evidence quality rather than using weather or one low total as a deterministic Under.
18. **Test rearguards are survival processes.** A large lead and wickets required are not sufficient for a win lean. Model remaining playable balls, current batters, partnership/farming ability, new-ball cycles, bowler workload, dismissal hazards, weather/light and follow-on fatigue. Repeated same-match tail resistance is current evidence, not merely a season-average outlier. A multi-day match's own strip is not a fixed condition: where a day-1/day-2 pitch/toss report exists, treat later-day turn, bounce and deterioration as a within-match wear trajectory distinct from that opening report, and update it from what the match itself has shown (footmarks, patch wear, ball behaviour already observed) rather than re-using the first-day description unchanged.
19. **Retained resources can reverse phase direction.** At every limited-overs phase boundary, condition the next rate on runs, wickets, batter identities/roles, boundary access, bowling overs remaining, target/required rate and conditions. A slow powerplay with wickets/resources intact can accelerate above the innings line; a fast powerplay with depleted batting resources can finish below it. Rank phase and innings contracts on their own conditional distributions. **Extended 2026-09-25 (audit closure; 2026-09-23 read-only audit item 7):** model *which* wickets fall and the surviving batters' strike exposure jointly with the phase-bowler allocation (which batter faces which bowler, for roughly how many balls), not a wicket count alone. Derive the full-match winner from the explicit innings states: the bat-first total distribution, then the target, then the chase-resource process. Never derive it from an innings-total lean. Structure only; no coefficient. Evidence: P-482, where the realised mechanism was one batter (Sadaqat 114) and the named failure path fired for him alone.
20. **Phase participants outrank phase H2H.** For powerplay, middle and death contracts, confirm or explicitly mix the batting-order positions and likely bowlers actually exposed to that phase. A prior same-opponent phase score with materially different openers, finishers or bowling roles is a discounted mechanism clue, not the phase baseline; unresolved roles cap evidence. **Reinforced 2026-09-25 (2026-09-22 audit, P-482):** the phase map must at minimum name the incoming Nos. 3–4 and **both** opposing new-ball bowlers, not only the openers.
21. **Pregame innings totals require an innings-order mixture.** Before the toss, build separate bat-first and bat-second/chase branches. The chase branch includes target censoring, early completion and required-rate incentives; it cannot borrow the full 20/50-over exposure of the first-innings branch. Merely mentioning chase truncation without propagating it through the corridor and rank is insufficient. **Extended 2026-09-25 to every phase total (R-1 of the 2026-09-22 audit; audit closure).** The same mixture governs powerplay, middle-overs, death and first-N-overs rows. Before the toss a phase row is an explicit bat-first / chase mixture with printed weights. After the toss it uses the realised branch only. Team and venue phase windows are split by innings order and printed with n. A phase component sized on chase powerplays may not be applied to a batting-first innings, and vice versa. Evidence: ETPL 2026 Match 15 (69/1 chasing v 60/1 setting); P-445 (Jamaica 79/0 chasing v a batting-first mean of 43.5); P-482 (Kensington 12–18 Sep, batting-first powerplay mean 35.0 v chasing 60.0, n = 5 each). This is a construction and disclosure rule; no coefficient.
22. **Near-start identity gaps cap evidence.** When toss, innings order, confirmed XI or exact current strip remains unresolved near scheduled start, target-specific evidence is at most `LOW` unless a predeclared mixture demonstrates that the direction survives every material state. Named openers, phase bowlers or finishers that are not confirmed must remain role branches, not facts.
23. **Evidence units are overlap-aware.** The same match cannot count independently as a recent-form row, same-venue row, H2H row and prior-log case. Likewise, several score fronts sharing one upstream feed are one source lineage. Preserve each useful transformation, but shrink from the unique underlying events and disclose the overlap.
24. **A batting or bowling run is not self-correcting, and it is not self-perpetuating.** A team or player on a run of Unders, Overs, low powerplay scores, or wicket clusters neither "regresses" nor "continues" without a named, currently active mechanism under the streak persistence-versus-reversion audit (RULES_GENERAL (archived) §11.3E, G17.1) — for example a returning bowler/batter, a genuinely different attack/order faced, a strip that behaves differently from the recent venue run, or a demonstrated tactical change. Absent that, rank from the longer-run format/venue baseline (rung 6, `SOURCES.md` and widen the corridor rather than leaning on the streak's direction or its reversal. This applies equally to a chasing team's recent target-censored totals, which must first be separated from bat-first totals under control 21 before any trend across them is assessed.


## 6. Live state


Store target ID/version, cutoff and endpoint; innings, score, legal balls/overs, wickets, striker/non-striker, current bowler, ball age/new-ball state, target/required rate, powerplay/field state, session/time remaining, interruptions/DLS par where official, weather/light observation and resources remaining. Rebuild future phases from current batters, wickets, bowlers, playable exposure and termination branches; never extrapolate run rate alone. A live row uses a distinct remaining-output target/model ID rather than reusing the pregame distribution.


## 7. Sources and settlement


- ICC/ECB/national-board playing conditions control rules.
- Official competition scorecards and delivery feeds control state, exact balls, result, and statistics.
- Government weather services and official venue reporting control conditions.
- Reputable match specialists may supply exact-match strip reports after date/event verification.


For DLS, use the official revised target/result; do not reverse-engineer proprietary resource tables. Settle exact phases from official phase data or a legality-reconciled delivery reconstruction.

**Settlement additions (2026-09-25 audit closure).**
- **Official final reports first.** The competition's own final report or scorecard is the first settlement lineage, for example the CPL official final report or an exact final scorecard on Cricbuzz or ESPNcricinfo. Republications of one release (such as CaribbeanCricket.com and CricTracker copying the CPL release) count as **one** lineage.
- **Zero is not a duck.** A batter who did not bat, or who was not out on 0, is different from a dismissed duck. Player-level rows settle from the official scorecard's dismissal field, never from a runs value alone.
- **Over labels in summarised feeds.** An ESPN over label can be off by one (its "over 5" deliveries were the sixth over in P-482). Verify every phase checkpoint with the run-rate identity (e.g. 59 at 9.83 per over means 6.0 overs) before settling a phase row.


## 8. Numerical research basis


- [Cricsheet official JSON format](https://cricsheet.org/format/json/) — candidate versioned event-data format; source approval remains pending in `SOURCES.md`
- [A simulator for Twenty20 cricket — Davis, Perera and Swartz](https://doi.org/10.1111/anzs.12109) — limited-overs component precedent, not an active Test model
- [Modelling and simulation for one-day cricket — Swartz, Gill and Muthukumarana](https://doi.org/10.1002/cjs.10017) — ODI simulation precedent only
- [Bayesian survival analysis of batsmen in Test cricket — Stevenson and Brewer](https://doi.org/10.1515/jqas-2016-0090) — dismissal-hazard and hierarchical evidence, not a complete team-total model
- [On the distribution of runs scored and batting strategy in Test cricket — Scarf, Shi and Akhtar](https://doi.org/10.1111/j.1467-985X.2010.00672.x) — evidence to test count-family candidates, not proof of transfer to this target
- [NGBoost — Duan et al.](https://proceedings.mlr.press/v119/duan20a.html) and [noncrossing quantile regression — Bondell, Reich and Wang](https://doi.org/10.1093/biomet/asq048) — general distributional challengers


These sources justify candidate components and safeguards only. Model family selection and any probability claim require the local H0, chronological and prospective gates.


## 9. Upcoming-game research sequence


1. Freeze format, rules, scheduled day/innings/phase, target endpoint, toss state, DLS/shortening terms and every line before analysis. If the toss is unresolved, declare the bat-first versus bat-second/chase-censored mixture that will control the innings-total corridor.
2. Retrieve official event/state, squad/XI/toss and rules first; exact-match strip evidence and government match-window weather/light next, running and disclosing the full §2/§6A rung-by-rung pitch-report search rather than a single query; historical ball/innings process and comparable venue/format evidence after volatile facts.
3. Build separate playable-exposure, run-rate, dismissal/wicket-resource, batting-order/bowling-resource and termination branches. Map confirmed or mixed openers and new-ball/middle/death bowlers to their actual phase exposure. For Tests include innings changes, declaration/follow-on/chase/match-completion; for limited overs include bat-first/chase mixture, target pressure, phase/death resources and DLS.
4. De-duplicate the unique underlying event and source-lineage units before weighting recent, venue, H2H and prior-log evidence. One phase transition may inform a branch but cannot own the centre in a sparse competition.
5. Refresh state, XI/toss, weather/radar and surface reporting immediately before issue. A scheduled start crossing creates a new live target and remaining-exposure view. Unresolved toss/XI/strip near start invokes the LOW evidence cap.
6. Derive every total/milestone from the exact target corridor/CDF. Locate the line against all ordinary branches; if it sits inside the central corridor or unweighted branches cross both sides, apply the general LOW-evidence coherence cap. Match winner/draw comes from the full match-resource process, not mechanically from an innings-total lean.


Source examples in `SOURCES.md` are candidates by function. Do not make one scorecard, query site or archive a permanent mandatory source, and do not retain its data for H0 until approved.


## 10. SFA-CRICKET — sport forecast algorithm


Algorithm ID: `SFA-CRICKET`. Effective **2026-09-04**. Instantiates `GFA-2` (RULES_GENERAL (archived) §11) with cricket content. Process composition only; no fitted weight, scenario weight or published probability is introduced. Test, first-class, List A, T20, T10, The Hundred and each competition remain separate populations; limited-overs and Test engines never share a fitted distribution.


### 10.1 Blocking preconditions


| Precondition | Requirement | Failure output |
|---|---|---|
| `CR-P1` format and rules | Format, competition, overs, playing conditions, powerplay definition, DLS and shortening terms, super-over and no-result rules | `GATE-TARGET` failure; do not proceed |
| `CR-P2` target identity | Which random variable settles the row: named-day runs, remaining-day runs, team innings total, phase total, milestone or match result — with its own endpoint and exposure | A phase, innings and full-match target may never share a label or be substituted after the result |
| `CR-P3` toss and innings order | Toss result and batting order, or an explicit declared bat-first versus bat-second mixture | Unresolved toss caps target evidence at `LOW` unless the direction survives every predeclared material state |
| `CR-P4` XI and phase roles | Both XIs, batting order, likely openers, new-ball, middle and death bowlers, wicketkeeper | Unconfirmed phase participants remain role branches, never facts; dependent rows cap under RULES_GENERAL (archived) §11.5 |
| `CR-P5` strip and conditions | `STRIP STATUS` and `MATCH CONDITIONS STATUS` recorded separately under §2 | Continue with a disclosed evidence limit and forced or low-confidence ranking; never invent the strip |


### 10.2 Exposure chain


| Step | Output |
|---|---|
| `CR-S1` | Playable exposure: scheduled legal balls or overs, sessions and time, with weather, light, over-rate, interruption and early-completion uncertainty |
| `CR-S2` | Innings-order state: bat-first exposure, or chase exposure censored by the target and by early completion |
| `CR-S3` | Batting resource state by phase: which order positions are exposed to the powerplay, middle and death, with balls faced per position |
| `CR-S4` | Bowling resource state by phase: new-ball, middle and death allocations, overs remaining per bowler, matchup and support-bowler coverage |
| `CR-S5` | Phase-conditional run and dismissal rates, opponent-adjusted, on the observed strip and conditions |
| `CR-S6` | Coupled `runs, wicket, extras` transition: a wicket changes the subsequent rate, the remaining ceiling, batter exposure and innings termination |
| `CR-S7` | Termination and censoring hazards: all-out, declaration, follow-on, target reached, DLS revision, abandonment, void |
| `CR-S8` | One corridor or CDF per frozen target, from which every nested line is integrated |


### 10.3 Mandatory branch set


| Branch | Content |
|---|---|
| `CR-B1` | Central phase-by-phase progression with resources retained |
| `CR-B2` | Early-wicket cluster mapped to the bowlers and phases that can create it, with a collapse floor |
| `CR-B3` | Retained-resources acceleration: a slow phase with wickets in hand finishing above the innings line |
| `CR-B4` | Depleted-resources suppression: a fast phase with batting resources gone finishing below the innings line |
| `CR-B5` | Death or finisher ceiling: named finishers, wickets remaining, boundary access and death bowling |
| `CR-B6` | Chase-censored state: target reached early, required-rate incentive, and the cap on second-innings totals |
| `CR-B7` | Interruption state: DLS revision, shortened innings, no result, and the runs already scored before any stop |
| `CR-B8` | Test-specific rearguard or declaration state where the format applies: playable balls remaining, partnership survival, new-ball cycles, bowler workload |


### 10.4 Contract derivation map


| Contract | Queried from | Extra condition the mechanism must predict |
|---|---|---|
| Innings total | The innings-target corridor with `CR-S2` innings-order mixture | For a chasing side, the target cap and early completion; a first-innings corridor may not be reused |
| Phase total | The phase's own conditional distribution from `CR-S3`/`CR-S4`, as a bat-first / chase mixture before the toss or the realised branch after it (control 21, extended 2026-09-25) | The batting positions and bowlers actually exposed to those balls, and the innings order |
| Nested lines on one target | One CDF, integrated at each threshold | Over probability falls as the line rises; Under probability rises; a violation is a failed model record |
| Match result | Full match-resource process, including defendability of the projected target | Never inferred mechanically from an innings-total lean |
| Player milestone | Crease time, balls faced and dismissal hazard | Boundary sensitivity at the exact threshold |


### 10.5 Kill-path library


| Kill path | Defeats | Evidence origin |
|---|---|---|
| A confirmed opener or promoted hitter changing who faces the powerplay | A phase Under built on prior same-opponent phase history | C-PL9-CR-PHASE-ROLE, §5 control 20 |
| Retained wickets converting a slow phase into acceleration | An innings Under inferred from a correct phase Under | L-009, L-039, §5 controls 16 and 19 |
| A named finisher with boundary access at the death | An upper Under lacking a separate last-phase branch | T-001, §5 control 4 |
| Target censoring in the chase | A second-innings team-total Over carrying full-overs exposure | §5 control 21, L-050 |
| One venue innings or one prior match owning the baseline | A sparse-competition Under or Over ranked above a shrunk hierarchical prior | C-PL5-CR-SPARSE-COMP, §5 control 17 |
| An elite batting unit clearing a venue median | An Under ranked on the venue median without current XI, bowling and strip evidence | §5 control 8 |
| Test lower-order and follow-on resistance | A win lean resting on lead and wickets required | C-PL5-CR-TEST-REARGUARD, §5 control 18 |
| Runs already scored before a rain stop | The assumption that interruption risk supports an Under | §5 controls 9 and 13, L-040 |
| The same match counted as form, venue, head-to-head and prior-log evidence | An evidence grade inflated by repetition | §5 control 23, L-049 |
| A chase-anchored phase read applied to a batting-first innings (the reverse of chasing-side powerplay inflation) | A phase Over sized on chase powerplays for a side that may bat first | P-482 (Kensington batting-first mean 35.0 v chasing 60.0; Jamaica chasing 77.0 v batting-first 50.0); control 21 extension (2026-09-25) |
| A returning bowler/batter, genuinely different attack faced, or a strip that reads differently from the recent run | An Under/Over or a reversal ranked purely on streak length without a currently active named mechanism | §5 control 24, RULES_GENERAL (archived) §11.3E (G17.1) |


### 10.6 Sport ordering overrides


1. Phase and innings rows on one innings are dependent. Only one is `PRIMARY_FORMAL` unless the other has independent phase-participant evidence.
2. Before the toss, no innings-total row may exceed `LOW` evidence unless the direction survives both the bat-first and the chase-censored branch.
3. Toss direction alone is context. Bowl-first supports neither an Under nor a winner without a mechanism.
4. Nested lines on one target are ordered by the CDF, never by separate narratives. A higher Over may not outrank a lower Over on likelihood.
5. Raw Over/Under counts, competition medians and old head-to-head are `E — diagnostic only`.


### 10.7 Pre-issue checklist


1. `CR-P1`–`CR-P5` status printed, including both conditions statuses and the toss state.
2. Format-and-venue baseline stated before any line.
3. Batting and bowling phase-resource maps stated, with unconfirmed roles held as branches, naming at least the incoming Nos. 3–4 and both opposing new-ball bowlers (control 20).
4. All eight `CR-B*` branches represented, with the innings-order mixture explicit when the toss is unresolved.
5. Nested-line monotonicity verified across every supplied line on one target.
6. Kill-path rows selected from §10.5 and reconciled against the issued order.
7. Evidence units de-duplicated to unique underlying matches and source lineages.
8. Toss, XI, strip, radar and state refreshed at G31; a start crossing creates a new live remaining-exposure target.
9. Recency block complete per §10.8: L5/L10/L15/L20 for both sides and for head-to-head, continuity count stated, trend verdict per metric, unique-event de-duplication done.
10. Environment block complete per §10.9: the **TOSS FACT** and **STRIP/PITCH EVIDENCE** ladders from `SOURCES.md` are shown with exact attempted sources/results; source lineages are de-duplicated; the venue-history state is `COMPUTED` with sample size/innings-order split or `INSUFFICIENT_VENUE_HISTORY`; automated pitch metadata is not relabelled as an observed strip.
10a. Streak/reversion block complete per RULES_GENERAL (archived) §11.3E (G17.1) for every Under/Over run, wicket-cluster run, phase-score run, or series/reverse-fixture prior used directionally in either direction.
11. `REFERENCE_BASE_RATE`, exact threshold, population and denominator recorded for every supplied row per §10.10 as a descriptive diagnostic only; no reference-band, trend or slot-frequency adjustment may move an ordinal (G23.1).
12. Extra-condition support audit (G24) recorded for every handicap, team-total and cushion row; no retrospective contract-family penalty is applied.
13. Separation budget (G20.1) solved for every margin, handicap and cushion row across powerplay, middle and death phases with the wicket-resource state at each transition.
14. Rank-1 implied-target interval (G25.1) stated in the unit of every other supplied line, each remaining row classified `COHERENT`/`PARTIAL_OVERLAP`/`DISJOINT`, and every aggregate budget re-solved conditional on the Rank-1 state.
15. Winner-and-cushion reconciliation (G30.1) whenever Rank #1 is an underdog cushion, with the outright-win and narrow-loss branch ordering stated. Example separation kill path for this sport: a death-overs acceleration or a middle-order collapse.
16. Deficit attribution (G14.1) recorded for every weak, absent, returning or small-sample participant: which side's distribution moved and through which exposure step.
17. **Phase rows (added 2026-09-25):** the innings-order mixture is printed before the toss, or the realised branch after it, with team and venue phase windows split by innings order and n (control 21). The toss is retrieved at the toss window, via the registered ESPN `summary` `notes[]` route where available (§2.7).


### 10.8 Recency, head-to-head and trend windows


Implements `GFA-2` step G13.1 (RULES_GENERAL (archived) §11.3B) and runs at that point in the algorithm, not at the end. Retrieval of L5/L10/L15/L20 for both sides and for the head-to-head series is mandatory; a window that does not exist is recorded with its true count and a missingness code.


Populate one windowed table per side with these metrics, and one head-to-head table:


| Window metric | Content |
|---|---|
| Team innings totals | Completed innings totals in this exact format, split by bat-first and chase |
| Phase output | Powerplay, middle and death runs and wickets, for and against, as separate series, **each split by bat-first and chase** (control 21, extended 2026-09-25) |
| Batting resources | Each decision-driving batter's own last 5/10/15/20 innings: position, balls faced, strike rate and dismissal mode |
| Bowling resources | Each likely bowler's own last 5/10/15/20 spells: phase bowled, overs, economy and wickets |
| Venue window | **The last 5/10/15/20 matches at this exact venue in this format and rules era, by innings order.** This is rung 6 of the conditions ladder and is mandatory |


**Head-to-head continuity.** Continuity means the same format, a comparable XI, the same venue class and the same rules era. Cricket head-to-head across formats or across three years of squad turnover fails continuity and carries no directional weight.


**Descriptive recency windows (G13.1; revised 2026-09-17).** Retrieve L5/L10/L15/L20 and continuity-qualified H2H with unique-event counts. These windows overlap. Monotonicity and dispersion among their averages are not a statistical trend/noise test. Report direction descriptively; estimate recency decay and opponent/regime effects using time-ordered validation. See SCORING_AND_VALIDATION section 5.


**De-duplication.** The windows overlap by construction and share matches with the head-to-head and venue series. Shrink from unique underlying events under G9; never treat L5, L10, L15 and L20 as four confirmations.


### 10.9 Environment and conditions


Implements `GFA-2` step G15.1 (RULES_GENERAL (archived) §11.3C). Venue classification for this sport is normally **OUTDOOR**.


| Field | Use in this sport |
|---|---|
| Toss / strip ladders | Separate TOSS FACT and STRIP/PITCH attempt-and-result tables shown per §2 / `SOURCES.md`; de-duplicate shared upstream lineages; venue history is `COMPUTED` or `INSUFFICIENT_VENUE_HISTORY` rather than forced |
| Pitch/curator search | `"<venue>" pitch report` and `"<venue>" curator/groundsman` queries run every card, including for a dated venue-tendency profile piece when no toss-day statement exists; caption a profile piece as historical tendency, not confirmed current preparation |
| Marquee-fixture preview lane | For internationally televised or major franchise-league fixtures, the competition's specialist "pitch and conditions" preview article, retrieved through the RULES_GENERAL (archived) §4 access ladder | Verified live 2026-09-04: an ESPNcricinfo IPL match preview, fetched through the proxy lane, named the exact numbered strip in use, its prior scores and the head coach's stated expectation — a real, decision-relevant example, not filler |
| ICC Pitch and Outfield Monitoring rating | `SRC-CRIC-ICC-PITCH-RATING` — official, multi-year venue-reputation signal for internationally accredited grounds only; retrospective, never a substitute for a live report |
| PitchViz/CricViz index | `SRC-CRIC-CRICVIZ-PITCHVIZ` — citation-only: usable only when a dated named article/broadcast quotes an exact figure; the underlying database is not a directly fetchable public feed |
| Toss decision | `D-conditional` circumstantial context per §2 when unusual for the format/venue; never a standalone directional lean |
| Dew point and relative humidity | Second-innings dew changes grip, ball behaviour and chase difficulty; it is measured, never asserted |
| Cloud cover | Swing conditions; opposite sign to a dry, hard, sunlit surface |
| Wind speed, gusts and direction | Resolved against ground orientation for boundary size and for swing |
| Hourly precipitation and forecast interruption windows | Feeds `CR-B7`, DLS and the abandonment branch |


Failure to obtain the match-window forecast for an outdoor or open-roof event yields `WEATHER_NOT_AVAILABLE`, widened total and margin distributions, and a `LEAN` cap on every weather-dependent row. No factor above carries an automatic total direction.


### 10.10 Base-rate anchors and derived stat lanes


**Anchoring (G12.1).** When a comparable same-format venue distribution exists, use it as contextual anchoring split by innings order with the sample size stated. When it does not, record `INSUFFICIENT_VENUE_HISTORY`, use a broader explicitly labelled prior if appropriate and widen uncertainty. A chase-innings line and a first-innings line at the same number are different propositions.


**Derived and low-salience fields that are available and routinely skipped:**


| Field | Note |
|---|---|
| Boundary dimensions and square-versus-straight sizes | Interacts with wind direction and with the phase in which each batter is exposed |
| Strip identity and reuse | Which pitch on the square, and whether it is a used surface, where the source states it |
| Start time and session structure | Day, day-night and the dew window are different conditions problems |
| Umpire and match-referee assignment | Recorded; conditional and rarely decision-driving |


## 11. Sport and competition rules reference


Added 2026-09-04. The laws of cricket, the format-level playing conditions (Test / ODI / T20 / The Hundred), and the competition-specific rules of every cricket league in the prediction logs live in **[LEAGUE_RULES_CRICKET.md](LEAGUE_RULES_CRICKET.md)**. That file is the reference for `§1` identity, the `§2` conditions gate, `§6` live state and `§7` settlement — it does not change `SFA-CRICKET`. Consult it whenever a card needs the exact innings length, powerplay structure, bowler limit, DLS minimum, Super Over rule, points system or knockout format for the competition in hand. Its **maintenance note** carries the season-boundary rules-currency check and the new-competition onboarding requirement (RULES_GENERAL (archived) §3, `G2`): at a new season / edition, re-verify the ICC playing conditions and the league's regulations before the first card; a new cricket competition must be fully documented there before it is forecast.
