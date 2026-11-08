> **Authority.** [CORE](CORE.md) and [CURRENT_RULES](RULES_REFERENCE.md#part-a-current_rules) govern new work; this page holds this sport's rules, and earlier statements below keep their historical scope.

**Current sourcing (9November2026):** use [SOURCES SRC-ALT-v2](SOURCES.md) and the [explicit competition catalogue](research/source_routes/COMPETITION_ROUTES.csv). Each required sporting field and exact event needs its own access/accuracy check; a major-league sample never certifies this competition.

**Executable forecast cycle (CYCLE-v1).** Defined in [FORECAST_CYCLE_PROTOCOL](REFERENCE_MODEL_PROTOCOL.md#merged-forecast_cycle_protocol); summarised in [CORE](CORE.md) §7.

**Local keys until settlement; updated mini after every game (MINI-v2).** Defined in [MINI_LOG_IDENTITY_PROTOCOL](WORKFLOW.md#part-b-mini_log_identity_protocol); summarised in [CORE](CORE.md) §2.

**Persistent research and corroboration (EXH-v1).** Defined in [RESEARCH_EXHAUSTIVENESS_PROTOCOL](RESEARCH_PROTOCOL.md#part-b-research_exhaustiveness_protocol); summarised in [CORE](CORE.md) §5.

**Online history and confirmed players (HIST-2026.10.16-v3 / AVAIL-2026.10.16-v4).** Defined in [HISTORICAL_SOURCE_PROTOCOL](HISTORICAL_SOURCE_PROTOCOL.md); summarised in [CORE](CORE.md) §5.

# Cricket analysis rules

**Live rules for Cricket. Markdown-only operation, 2026-09-28.** Read §0 in full for every card: it governs this file.
- §1 onward is the reference algorithm and the competition rules; it is consulted by citation.
- The dated history (settlement learnings and the evidence behind every numbered control) was moved verbatim to `archive/superseded_2026-09-28/sport_history/RULES_CRICKET_history_to_2026-09-28.md`, which is no longer in the Markdown tree. A maintainer can recover it from the pinned commit ([Git 3fbf0c981b40](https://github.com/danisgreat/Sports-Research/blob/3fbf0c981b40a1d0e3ffff9725dcc8e383ff05fa/archive/superseded_2026-09-28/sport_history/RULES_CRICKET_history_to_2026-09-28.md); [index](HISTORICAL_LINK_INDEX.md#removed-paths-cited-in-operating-documents)) when a control's full text or evidence is needed. The model works from §0 and the sections below.
- Arithmetic: `PROBABILITY_TOOLKIT.md`. Sources: `SOURCES.md` §3.3. Card and self-audit: `CARD_AND_LOG_TEMPLATES.md`. The cross-sport rules are in `RULES_REFERENCE.md`, which outranks this file.
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
2. **Innings-order mixture (control 21).** Before the toss, every innings **and phase** total is a bat-first/chase mixture; after it, the realised branch. The chase is capped by the target and may end early *[read as: the chase ends at the winning delivery, so its total is censored at the target plus that delivery's legal overshoot, not capped at the target itself; PROBABILITY_TOOLKIT §7, corrected 2026-10-12]*. Windows are split by innings order: a chase powerplay may not size a batting-first powerplay (M24; P-482).
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

### Numerical shadow model (2026-09-26(c); suspended for md-only operation, 2026-09-28) — historical

Moved verbatim to [archive/historical_engine_sections_2026-11-08/RULES_CRICKET.md](archive/historical_engine_sections_2026-11-08/RULES_CRICKET.md) on 2026-11-08 (CR-2026.11.08-R2): it describes the September numerical engine and shadow, suspended for markdown-only operation on 2026-09-28 and superseded by the v24 reference ([REFERENCE_MODEL_PROTOCOL](REFERENCE_MODEL_PROTOCOL.md)). It is not a current instruction.

### 0.7 Control index (full text in §5 and the dated sections)
1 legal deliveries · 2 phase ≠ innings · 3 wicket-cluster floor · 4 finisher ceiling · 5 toss is context · 6 winner independence · 7 adjusted venue samples · 8 direct ceiling conflict · 9 rain/dew conditional · 10 milestones boundary-sensitive · 11 target identity first · 12 one CDF for nested totals · 13 stochastic exposure · 14 calibration preserves geometry · 15 incomplete is not zero · 16 phase-to-innings is joint · 17 sparse competitions shrink · 18 Test rearguards are survival processes · 19 retained resources reverse phase direction (which wickets fall) · 20 phase participants outrank phase H2H (Nos. 3–4, both new-ball bowlers) · 21 innings-order mixture for innings and phase totals · 22 near-start identity gaps cap evidence · 23 overlap-aware evidence units · 24 runs are neither self-correcting nor self-perpetuating · 25 same-venue, same-week cross-format evidence · 26 retrieve XIs after the toss · 27 current-series tempo prior; restart is width · 28 Test winner as a three-way time budget · 29 phase-checkpoint settlement route · 30 direct same-venue current-regime ceiling · 31 bowling replacement chain · 32 conditional activation.

### 0.8 Numerical engine specification (MDS-v8.0 / CR-2026.10.06-NUMERICAL-1) — historical

Moved verbatim to [archive/historical_engine_sections_2026-11-08/RULES_CRICKET.md](archive/historical_engine_sections_2026-11-08/RULES_CRICKET.md) on 2026-11-08 (CR-2026.11.08-R2): it describes the September numerical engine and shadow, suspended for markdown-only operation on 2026-09-28 and superseded by the v24 reference ([REFERENCE_MODEL_PROTOCOL](REFERENCE_MODEL_PROTOCOL.md)). It is not a current instruction.

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

Exposure units are legal balls, wickets, batting position, batter/bowler resources, scheduled balls/overs and opening/powerplay, middle and death phases. Estimate a ball/over transition such as `P(runs, wicket, extras | state)`, conditioned on target, required rate, current resources, matchup, venue/conditions and phase. Wickets change both rate and remaining ceiling. A chase is capped by the target and may end early *[read as: censored at the target plus the winning delivery's legal overshoot; PROBABILITY_TOOLKIT §7]*; DLS/shortening is a distinct rules/state branch.

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

Added 2026-09-04. The laws of cricket, the format-level playing conditions (Test / ODI / T20 / The Hundred), and the competition-specific rules of every cricket league in the prediction logs live in **[RULES_CRICKET.md (LEAGUE_RULES_CRICKET)](#merged-league_rules_cricket)**. That file is the reference for `§1` identity, the `§2` conditions gate, `§6` live state and `§7` settlement — it does not change `SFA-CRICKET`. Consult it whenever a card needs the exact innings length, powerplay structure, bowler limit, DLS minimum, Super Over rule, points system or knockout format for the competition in hand. Its **maintenance note** carries the season-boundary rules-currency check and the new-competition onboarding requirement (RULES_GENERAL (archived) §3, `G2`): at a new season / edition, re-verify the ICC playing conditions and the league's regulations before the first card; a new cricket competition must be fully documented there before it is forecast.

---

# Merged: LEAGUE_RULES_CRICKET

*Merged 2026-11-07 (R2, verbatim). *(Wording cleaned 2026-11-07, CR-2026.11.07-R3: contract instead of market or bet wording; current governance pointers. Facts unchanged.)* Formerly `LEAGUE_RULES_CRICKET.md` (original title: Cricket — sport and competition rules reference). Original kept unchanged at [archive/consolidation_2026-11-07/merged_sources/LEAGUE_RULES_CRICKET.md](archive/consolidation_2026-11-07/merged_sources/LEAGUE_RULES_CRICKET.md).*

> **Current authority (October 5):** [CORE.md (METHOD)](CORE.md#merged-method) and [RULES_REFERENCE.md (CURRENT_RULES)](RULES_REFERENCE.md#part-a-current_rules) govern new work. Requested qualitative or explicitly uncalibrated research receives canonical Part 6 IDs regardless of calibration; numerical performance certification is separate. Read current IDs/freeze from the [status register](GAME_LOG_STATUS_CURRENT.md), unresolved items from the [carryover](archive/verification_2026-10/closure_2026-10-05/carryover.md), and [current implementation evidence](archive/verification_2026-10/implementation_2026-10-05/REPORT.md). Earlier method, queue, freeze and eligibility statements below retain their historical scope.

> **Authority.** [CORE](CORE.md) and [CURRENT_RULES](RULES_REFERENCE.md#part-a-current_rules) govern new work; this page holds this sport's rules, and earlier statements below keep their historical scope.


> **Status (md-only, 2026-09-28):** reference material for identity, format and settlement. No scope is prospectively validated; every card is LEARNING_ONLY. Live rules: `RULES_REFERENCE.md` and the sport file's §0.

Status: **ACTIVE — reference**
Created: **2026-09-04**
Companion to: **[RULES_CRICKET.md](RULES_CRICKET.md) §11**. Reference only; it does not change `SFA-CRICKET` or any selection rule. It documents the laws of cricket, the format-level playing conditions, and the competition-specific rules for every cricket competition that appears in the prediction logs.

Rules-era caveat: the playing conditions below are those in force for the **2025–2026** seasons the current log covers (ICC men's playing conditions effective July 2025; ICC Women's Championship 2025–2029; The Hundred 2026; CPL 2026; ETPL 2026 inaugural). Cricket changes its playing conditions almost every year — verify the era for any event outside this window.

**Maintenance (rule G2, kept here; RULES_GENERAL is archived).** Last reviewed **2026-11-08**: the ICC 2025 conditions and the MCC 2026 Laws above. The Hundred, CPL, WCPL and ETPL 2026 seasons are complete; their sections stand as records. Bilateral Tests, ODIs and T20Is follow the ICC conditions in force on the match date; the 2026 Women's T20 Asia Cup and the Namibia and Pakistan tri-series are complete. Before the first card of a new season / edition of any competition here — or the first appearance of a cricket competition after a break of ~6 weeks or more — re-verify the ICC playing conditions and the competition's own playing regulations against the field owner (ICC, the league operator) for changes to powerplay/bowler limits, DRS, DLS minima, the Super Over rule, the points/NRR system, squad rules, or the knockout format, and update the relevant section below **before** issuing the card. The first time a new cricket competition is forecast, add its full playing conditions and format here first. Watch especially for: a franchise-league deviation from ICC conditions (e.g. the IPL's two-bouncers-per-over and Impact Player rules, which are IPL-only and not guaranteed to persist), a format switch (The Hundred's investors have floated a move to franchise T20), and expansion/contraction of a league's team count.

---

## 1. The laws of cricket (all formats)

**Objective.** Two teams of eleven. One team bats (tries to score **runs**) while the other bowls and fields (tries to take **wickets** and restrict runs). The team that scores more runs, under the match's format rules, wins.

**The field.** An oval grass ground. In the centre is the **pitch**: 22 yards (20.12 m) between the two sets of **stumps** (three wooden stumps + two bails per end). A **30-yard (27.4 m) circle** is marked around the pitch for fielding-restriction purposes. The **boundary** is the edge of the field — ball over it on the full = **6 runs**, along the ground or bouncing = **4 runs**.

**An over.** Six legal deliveries bowled from one end by one bowler (five in The Hundred — see §4). After an over the bowling switches to the other end and a different bowler; a bowler may not bowl two overs in succession. Ends alternate; the batters do not swap ends between overs (they swap by running odd numbers of runs, or at the end of an over the striker/non-striker roles swap because the bowling end changed).

**Scoring runs.** The two batters at the crease run between the wickets — each completed length = 1 run. Plus boundaries (4/6). Plus **extras**: **wide** (1 run + re-bowled, ball passes out of the batter's reach), **no-ball** (1 run + re-bowled + **free hit** next ball in white-ball cricket, for overstepping / illegal delivery / dangerous ball), **bye** (ball passes the batter and keeper), **leg-bye** (ball hits the batter's body, not bat, and they run).

**Getting out (dismissals).** **Bowled** (ball hits stumps), **caught** (fielder catches it on the full), **leg before wicket / LBW** (ball would have hit the stumps but for the batter's pad, subject to the LBW law — pitching line, impact line, wickets-in-line), **run out** (stumps broken while a batter is out of the crease during a run), **stumped** (keeper breaks the stumps with the batter out of the crease and not attempting a run), **hit wicket**, **handled the ball / obstructing the field / hit the ball twice / timed out** (rare). When 10 of the 11 batters are out, the innings is **all out** (the 11th has no partner).

**The toss.** Before the match a coin is tossed; the winning captain chooses to **bat** or **bowl** first. In conditions terms this is one of the largest single levers in the sport (RULES_CRICKET.md §2).

**DRS (Decision Review System).** Where available, each side may **review** an on-field umpire's out/not-out decision to the third umpire (ball-tracking, UltraEdge/Snicko, replays). **Umpire's call** on marginal LBW ball-tracking keeps the on-field decision and the reviewing side keeps its review. Review allowance: **two unsuccessful reviews per team per innings** in T20Is and ODIs (Tests also two, topped back up after 80 overs in some eras); franchise leagues set their own (usually one or two).

**Powerplay / fielding restrictions (base concept).** For a defined early portion of each innings only **two** fielders are allowed outside the 30-yard circle; outside the powerplay the limit is **five** outside the circle (and never more than five on the leg side, and at delivery no more than two behind square on the leg side). The exact powerplay length is format-specific (§2–§4).

**Weather and DLS.** Rain/bad light stops play. If overs are lost, the target is recalculated by the **Duckworth–Lewis–Stern (DLS)** method, which accounts for overs and wickets remaining as "resources." A minimum number of overs must be bowled to the side batting second for a result (T20: **5 overs** each side unless further reduced by playing conditions; ODI: **20 overs**). Below that minimum the match is **no result** / abandoned. The team batting second chases a **par score + 1**; being level with the par score at a stoppage is a **tie**.

**Super Over (tie-breaker).** Where a match must produce a winner and the scores are level, each side bats **one over** (six balls, maximum **two wickets**). Higher score wins. If the Super Over is also tied, **further Super Overs are played until there is a winner** (the old boundary-count tie-break was abolished in 2019). Bowlers and batters used in one Super Over have restrictions on reuse in the next.

**Over-rate / stop clock (white-ball, in force 2024–2026).**
- **Stop clock:** the fielding side must be ready to bowl the first ball of the next over within **60 seconds** of the previous over ending. Two warnings per innings; the **third and each subsequent breach = 5 penalty runs** to the batting side.
- **In-match over-rate penalty:** if the fielding side is not in position to bowl the first ball of the **final over** by the scheduled cutoff time, **one fewer fielder is allowed outside the 30-yard circle** for the rest of the innings.

**Other current playing-condition points (ICC, effective July 2025).**
- **Wide judgement** now references the batter's leg position **at the moment of delivery**, so a batter who moves across cannot manufacture a wide by the movement alone (leg-side wides are still strict in white-ball cricket).
- **One bouncer (above shoulder height) per over** in ICC T20Is; **two per over** in ODIs. (The IPL uses two per over — a franchise-league deviation; do not assume it elsewhere.)
- **Serious-injury replacement:** from October 2025, on trial, a player who suffers a serious on-field injury after the match starts may be replaced by a **like-for-like fully participating** substitute (a widening of the older concussion-substitute rule).
- **Boundary catches (ICC men's playing conditions from June–July 2025, re-verified 2026-11-08):** a fielder must be **entirely within the boundary** (or their last contact with the ground was inside) when they touch the ball. A fielder who is airborne beyond the rope when touching the ball must then **land inside the field and stay inside** for the catch to stand.
- **MCC Laws of Cricket, 2026 edition (in force 1 October 2026; 73 material changes, the fourth revision of the 2017 Code):** when a wicket falls in the last over of a day in a multi-day match, the over is completed and the new batter faces the remaining balls; ball sizes are now classed Size 1, 2 and 3 with uniform tolerances; laminated bats are allowed in adult open-age cricket; the rules on when the ball is "finally settled" and on overthrows are clarified; and the wording is gender-neutral. ICC international playing conditions adopt Laws changes separately: check the series' playing conditions on the card (lords.org; icc-cricket.com).

---

## 2. Format playing conditions — Test and ODI (base reference; not directly forecast in the log so far)

### 2.1 Test cricket
- **Two innings per side**, up to **5 days**, minimum **90 overs per day**. No fixed innings length — an innings ends when the side is all out, declares, or (rarely) time runs out.
- **New ball** available after 80 overs. **Stop clock between overs in Tests** (ICC, from June 2025; warnings reset every 80 overs). **Follow-on:** the side batting first, if 200+ runs ahead after the first innings, may ask the opponent to bat again immediately.
- **Result:** win (opponent's second innings dismissed/target chased), **draw** (time expires with the match unfinished), or **tie** (extremely rare — scores level with the last team all out). **No DLS** in Tests — lost time simply makes a draw more likely.
- **World Test Championship (2025–2027):** a points percentage table (12 points per win, 4 per draw, of a possible 12 per match), with in-match over-rate and slow-over penalties; top two contest a one-off final.
- Settlement: the **draw is a first-class outcome** and must be an explicit branch for any Test winner market.

### 2.2 One Day International (ODI) / List A
- **50 overs per side**, one innings each. Bowler maximum **10 overs**.
- **Powerplays:** overs 1–10 = two fielders out (P1); overs 11–40 = four out (P2); overs 41–50 = five out (P3).
- **Two new balls** (one from each end) in ODIs for the first ~34 overs, then one chosen ball for the death — the exact rule has changed repeatedly; since 2 July 2025 (ICC), two new balls are used to the end of over 34 and the fielding side then picks one of them for overs 35–50 (re-verified 2026-11-08).
- **DRS:** two unsuccessful reviews per team per innings.
- **DLS** applies; minimum **20 overs** to the side batting second for a result.
- **Result:** win or tie; no draw. **Super Over** in knockouts, bilateral series usually record a tie.

---

## 3. Format playing conditions — Twenty20 (T20 / T20I)

This is the base format for the CPL, the ETPL, and the bilateral / tri-series T20Is in the log (Namibia T20I Tri-Series; Pakistan Women's T20Is).

- **20 overs per side**, one innings each. **Bowler maximum 4 overs** (in a full match; pro-rated down in a reduced match, normally to no more than 1/5 of the innings + rounding).
- **Powerplay:** overs **1–6** — only **two** fielders outside the 30-yard circle. Overs 7–20 — **five** outside the circle.
- **Free hit** for any no-ball (front-foot, back-foot, height, more-than-permitted-bouncer): the next ball, the striker can only be out run-out / handled / obstructing, and the field may not change unless the batters cross.
- **DRS** (where deployed): **two** unsuccessful reviews per team per innings.
- **DLS:** minimum **5 overs** each side for a result (unless playing conditions reduce further, e.g. some leagues use a 10-over minimum in knockouts). Par score at every ball is published.
- **Interval / strategic timeout:** ICC T20Is have an optional drinks break; most **franchise leagues have a compulsory 2½-minute strategic timeout in each innings** (see per-league notes).
- **Stop clock + over-rate fielder penalty** as in §1.
- **Result:** win, tie (→ Super Over in almost all T20 leagues and knockouts), or no result. **A tied league match is usually one point each; a tied knockout goes to a Super Over.**
- **Points (standard T20 league):** win **2**, tie/no-result **1**, loss **0**. Standings ordered by points, then **net run rate (NRR)** = (runs scored ÷ overs faced) − (runs conceded ÷ overs bowled) across the tournament; a side bowled out is treated as having faced its full quota of overs for NRR.

---

## 4. The Hundred (Men's and Women's Competition)

**Governing body:** ECB. **Teams:** 8 city franchises (7 England, 1 Wales), each fielding a men's and a women's side; matches are played as **men's + women's double-headers at the same venue**. **2026:** the 100-ball format is **retained**; franchise part-ownership stakes were sold to private investors in 2025 and several teams were rebranded (e.g. Oval Invincibles → **MI London**, Northern Superchargers → **Sunrisers Leeds**). New investors have floated converting the event to franchise T20, but not before 2028.

### 4.1 Playing conditions (the 100-ball format)
- **100 balls per innings.** Whoever scores more runs wins. Target match length ~2h30, two 65-minute innings + 15-minute interval.
- **"Overs" are 5 balls.** The bowling captain may have a bowler deliver **5 or 10 consecutive balls** (i.e. one or two 5-ball sets back-to-back).
- **Change of ends every 10 balls** (not every 5).
- **Bowler maximum: 20 balls per match** (four 5-ball sets), of which no more than **10 in a row**.
- **Powerplay: 25 balls** at the start of each innings — only **two** fielders outside the 30-yard circle. After ball 25, **five** outside the circle.
- **No-ball: 2-run penalty** (not 1) + **free hit**.
- **One strategic timeout** per bowling side, up to 90 seconds, not during the powerplay.
- **New-batter rule:** the incoming batter must be ready to face within 60 seconds; a warning, then **5 penalty runs** for repeat delays.
- **DRS** is used in televised matches (limited reviews per side).
- **DLS** applies for weather; a minimum number of balls (the equivalent of 5 five-ball overs, i.e. 25 balls) must be bowled to the chasing side for a result.

### 4.2 Competition format
- **Group stage:** each team plays 8 matches (4 home, 4 away) — a partial round-robin. Points: **win 4, tie 2, no-result/weather-abandoned 2 each, loss 0**. Ranking by points, then **net run rate** (computed per ball for the 100-ball format).
- **Knockout:** top **3** teams advance. **Eliminator:** 2nd v 3rd. **Final:** Eliminator winner v 1st. (Historically played across two "Finals Day" fixtures / Lord's finals — confirm the year's exact structure.)
- Men's and women's competitions run in parallel with the same format.

### 4.3 Settlement notes
- Innings are measured in **balls**, not overs — "first-innings total", "team X runs", "over/under" lines are set against a **100-ball** innings, and any recency comparison to T20 data must adjust for the ~20-ball shorter innings and 5-ball powerplay-overs difference (RULES_CRICKET.md §10.8).
- A weather-abandoned match is **2 points each** and a **no result**, not a loss for the higher-ranked side; a match contract on it is VOID only under its frozen void rule, otherwise UNRESOLVED (RULES_REFERENCE Part B §7).

---

## 5. Caribbean Premier League (CPL) — "Republic Bank CPL"

**Governing body:** Cricket West Indies / CPL. **Format:** Twenty20. **2026 season:** 7 August – 20 September, **7 teams**, **39 matches**, final in Barbados. The Jamaica franchise returned for 2026, expanding the league from 6 to 7.

**2026 teams:** Antigua & Barbuda Falcons, Barbados Tridents, Guyana Amazon Warriors, a returning Jamaica franchise, Saint Lucia Kings, St Kitts & Nevis Patriots, Trinbago Knight Riders. **Venues:** Sir Vivian Richards Stadium (Antigua), Kensington Oval (Barbados), Providence Stadium (Guyana), Sabina Park (Jamaica), Warner Park (St Kitts), Daren Sammy Cricket Ground (St Lucia), Arnos Vale (St Vincent), Queen's Park Oval (Trinidad).

**Squad and selection rules (2026):** 17-player squads = **9 West Indian + 5 overseas + 3 "breakout" (developmental West Indian) players**. In the XI: **maximum 4 overseas players**, and **at least 1 breakout player is mandatory** in every match XI.

**Scheduling quirk:** teams play their home fixtures in a concentrated **"home week"**, often with two venues hosting on the same day. This compresses travel and rest patterns unusually — the venue/travel block in a CPL card behaves differently from other T20 leagues (RULES_CRICKET.md §10.9).

**Playing conditions:** standard ICC-derived T20 conditions — 6-over powerplay, 4-over bowler cap, free hit for no-balls, compulsory strategic timeout each innings, DRS, DLS (5-over minimum for a result), **Super Over** for a tie in any match. Caribbean pitches are typically **slow, low and spin-friendly**, and dew can be a major second-innings factor at day-night venues — this is a heavy toss/chasing consideration.

**Points and playoffs:** win 2 / tie or no-result 1 / loss 0, ranked by points then NRR. **Top 4** qualify. Playoff bracket: **Qualifier 1** (1st v 2nd — winner to the Final), **Eliminator** (3rd v 4th — loser out), **Qualifier 2** (Qualifier 1 loser v Eliminator winner — winner to the Final), **Final**. All playoff games at a single host venue.

---

## 6. European T20 Premier League (ETPL) — inaugural 2026

**Governing body:** a private venture (ICC-sanctioned), run across the European Cricket pathway. **2026 is the inaugural edition** — 26 August – 20 September, played in Ireland, Northern Ireland, the Netherlands and Scotland.

**Teams:** **6 franchises** — two each from **Ireland, Scotland and the Netherlands**. (Log example: Belfast Wolves, Edinburgh Castle Rockers.)

**Squad and selection rules:** 17-player squads with **at least 8 local players**, **5–7 overseas players**, and **at least one European Associate** and **one Global Associate** player per squad. In the XI: **at least 5 local players** and a **maximum of 4 overseas players**.

**Format:** **double round-robin** — each franchise plays every other twice (10 group games each) — then a knockout: the **table-topper goes straight to the Final**, and **2nd v 3rd** play a **Qualifier** for the other Final place.

**Playing conditions:** standard ICC T20 playing conditions (6-over powerplay, 4-over bowler cap, free hit, DRS where broadcast, DLS 5-over minimum, Super Over for ties). Points: win 2 / tie or no-result 1 / loss 0, then NRR.

**Analytical caution (inaugural league):** there is **no venue-and-format history and no team history** for this competition (RULES_CRICKET.md control 17, sparse-competition hierarchical shrinkage). Player form must be imported from other competitions with heavy shrinkage; Irish, Scottish and Dutch late-August weather makes **reduced-over and no-result outcomes materially more likely** than in a Caribbean or subcontinental T20 league.

---

## 7. Bilateral and tri-series T20Is and ODIs

Covers: **Namibia T20I Tri-Series 2026** (men's T20Is), **Pakistan Women tour of Sri Lanka** (women's T20Is), **Ireland Women tour of England** (women's ODIs, part of the ICC Women's Championship).

### 7.1 T20Is (bilateral / tri-series)
- Full ICC **T20I playing conditions** as in §3 (6-over powerplay, 4-over cap, one bouncer/over, free hit, stop clock, DRS where deployed, DLS 5-over minimum, Super Over in a final).
- **Tri-series:** a short round-robin (each team plays the others once or twice) then a **final** between the top two. League ties → 1 point each; the **final** goes to a Super Over.
- **Associate / lower-profile fixtures** (Namibia and its opponents) may have **no DRS**, less reliable ball-tracking, uncovered-pitch or drop-in-pitch variability, and thin venue history — widen conditions and participant uncertainty accordingly.

### 7.2 Women's ODIs and the ICC Women's Championship (2025–2029)
- **50-over ODI** playing conditions (§2.2): 10-over P1 (2 out), overs 11–40 (4 out), 41–50 (5 out); bowler max 10 overs; two new balls; DRS two reviews/team/innings; DLS 20-over minimum.
- **ICC Women's Championship 2025–2029:** **11 teams** (India, South Africa, Australia, England, Sri Lanka, New Zealand, Bangladesh, Pakistan, West Indies, Ireland, Zimbabwe). Each team plays **8 three-match series** (4 home, 4 away) — **132 ODIs** total over the cycle. **2 points per ODI win, 1 for a tie/no-result.** The table decides direct qualification for the **2029 Women's World Cup** (the rest go to a qualifier).
- Settlement: each match is a standalone ODI (win/tie/no-result); the **series** and the **Championship table** are separate propositions. A women's ODI between a top side and Ireland/Zimbabwe has a **wide expected-margin distribution** and a real mismatch/rain-shortened tail.

---

## 8. Cross-competition quick reference

| Competition | Format | Innings unit | Powerplay | Bowler cap | Tie rule | Knockout |
|---|---|---|---|---|---|---|
| Test / WTC | 2 inns/side, 5 days | overs (no cap) | new ball @80 | none | draw or tie | WTC final (1 match) |
| ODI / Women's Championship | 50 overs | 50 overs | 10 / 11–40 / 41–50 | 10 overs | tie (SO in knockouts) | World Cup qualification table |
| T20I bilateral/tri-series | 20 overs | 20 overs | overs 1–6 | 4 overs | SO in finals, 1 pt each in league | tri-series final |
| The Hundred | 100 balls | 100 balls | 25 balls | **20 balls** | 2 pts each; SO in knockouts | top 3 → Eliminator → Final |
| CPL | 20 overs | 20 overs | overs 1–6 | 4 overs | Super Over | top 4 → Q1/Elim/Q2/Final |
| ETPL (2026) | 20 overs | 20 overs | overs 1–6 | 4 overs | Super Over | 1st → Final; 2nd v 3rd → Qualifier |

**Always resolve, per RULES_CRICKET.md §1:** the exact competition and season, the innings unit (overs vs balls), the powerplay and bowler limits, the DRS availability, the DLS minimum and current par, the Super Over / tie rule, the points and NRR rules, and the knockout bracket — before any rate or contract work. For weather-exposed fixtures also resolve the **minimum-overs-for-a-result** and the operator's **no-result / void** settlement.

## September 5 ETPL observed-match rules clarification

The official ETPL-linked NV Play record for [Match 13](https://www.etplofficial.com/nvplay-embed?customerId=1A9E0000-8D41-7CED-D487-08DEF280CD56&innings=2&matchId=ac4fe6d2-e979-49db-9803-83495a8a047f&theme=light&widget=match-centre) records a match reduced **before play to 12 overs**, a **four-over regulatory powerplay**, Belfast 40/1 at that boundary, 54/2 at six and 146/3 at twelve. The user's six-over contract is therefore distinct from this match’s powerplay. Glasgow won the toss and bowled. The scorer labels the ground Sportpark Westvliet, Den Haag; preserve that owner label alongside the original card’s Voorburg/Duivesteijn label rather than assuming aliases from name alone.

This is an exact-match observation, not a reconstructed universal ETPL reduced-over table. Verify the current competition conditions when another innings length is encountered. By Match 13 some inaugural-season match history exists; “no history” must mean no prior-season history, not zero current observations. Keep unique current-match denominators and condition on format/innings order rather than fabricating long windows or transferring 20-over averages unchanged to shortened innings.

## ETPL powerplay definition and settlement hazards — confirmed 2026-09-06

Added because ETPL phase contracts are now settleable and therefore need an exact, sourced definition rather than an assumed one.

**Standard mandatory powerplay:** `Overs 0.1 – 6.0`, recorded on the official scorecard as `Powerplay 1: Overs 0.1 - 6.0 (Mandatory - N runs, W wickets)`. Confirmed for ETPL 2026 matches 9 through 15 from the structured scorecard note (`SRC-ESPN-SITE-API-CRICKET`).

**Settlement hazard — the powerplay shortens with the innings.** In a rain-reduced ETPL match the mandatory powerplay is scaled down with the overs, and the scorecard note records the *actual* range. Two observed cases in this competition:

| Match | Powerplay range recorded | Innings length |
|---|---|---|
| Amsterdam Flames v Belfast Wolves (M8) | `Overs 0.1 - 1.3` | 5 overs per side |
| Glasgow Cosmic v Belfast Wolves (M13) | `Overs 0.1 - 3.4` | 12 overs per side |

A "powerplay Over/Under" contract frozen against an assumed six-over phase and settled against a 1.3-over or 3.4-over phase is a `GATE-CONTRACT` failure, not a close call. **Always read the actual powerplay range from the scorecard note before settling**, and where the toss is unpublished at freeze, state the phase length assumption alongside the batting-order condition.

**Observed ETPL 2026 full six-over powerplay population** (the descriptive `REFERENCE_BASE_RATE` for phase contracts in this competition, ESPN's official 8th–12th Matches): 28, 39, 49, 50, 51, 55, 56, 61, 68, 72 — median 53, mean 52.9. **Corrected 2026-09-06(d):** the population was originally mislabelled "matches 9-13"; the fixtures are officially the 8th through 12th Matches (verified against ESPN's `description` field). The actual 13th Match (Glasgow Cosmic v Belfast Wolves, reduced to 12 overs) is a different fixture from the one previously labelled M13 here, and is correctly excluded from a full-six-over population since its own powerplay was reduced. This population also does not yet reconcile three earlier same-competition cards (`P-099`, `P-115`, `P-171`) that ESPN's series ID does not appear to carry — treat this table as the confirmed 8th-12th-Match population only, not the tournament's complete history, until that gap is closed.

## 2026-09-06(f) — settlement and retrospective addendum

P-217 settlement clarification: the actual officially completed revised innings was 16 overs, GAW 185/5. The fixed 20-over target is preserved; research Over/Under grades use that revised completed-innings convention explicitly, with no extrapolated 20-over score and OPERATOR_ACTION UNKNOWN_DEFINITION. ESPN reports the mandatory PP ending at 4.5 (24/2), which must not replace the frozen six-completed-over target. P-305/P-311 batting-first conditions were met by the actual toss. [Details (historical; pinned Git 3fbf0c981b40)](https://github.com/danisgreat/Sports-Research/blob/3fbf0c981b40a1d0e3ffff9725dcc8e383ff05fa/archive/mini_logs/PREDICTION_MINI_LOG_SETTLEMENT_2026-09-06.md). No competition playing law or operator rule has been invented/changed.

## Exact exposure and retrospective correction - 2026-09-12

Keep P-364's completed innings/45-over targets separate from its still-live Test winner. P-366's fixed-20-over targets remain terminal censored after the actual 19-over match; P-217's inherited revised-16-over research convention does not automatically govern a different frozen contract. P-262's official CPL phase record is Falcons 43/1 at six and 183/4 at 20, illustrating resources and phase dependence, not a new competition law. No new ICC/league playing-condition change was established in this pass. See RULES_CRICKET and the recovered historical retrospective.

<!-- DEEP-RESEARCH-IMPLEMENTATION-2026-09-19-V42 -->
## 2026-09-19(c) — source firewall precedence

All league-specific source instructions are subordinate to `SOURCES.md` PF-1/PF-2. Official board/competition sources and admitted ball-level historical sources outrank derivative previews. Sportsbook/betting/fantasy/DFS material and market-derived projections are never predictive evidence; if an older league note suggests otherwise, this section controls.
