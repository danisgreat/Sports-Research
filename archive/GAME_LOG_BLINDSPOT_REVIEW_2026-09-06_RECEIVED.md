<!-- PROVENANCE HEADER -- added by this repository on receipt, 2026-09-06(d). Everything below the horizontal rule is the received document, preserved as found (no content changed). The original file remains in place at the repository root; this is a preserved copy with provenance context added. -->

# Received document: second independent internal blindspot review

**Found:** 2026-09-06, already present at the repository root as `GAME_LOG_BLINDSPOT_REVIEW_2026-09-06.md` when this session checked for it after the user asked for it to be fully reviewed and merged.
**Apparent origin:** a separate session's read-only, no-external-web-research review of this repository's own records, cross-checked against the first external blindspot audit (`archive/EXTERNAL_BLINDSPOT_AUDIT_2026-09-06_RECEIVED.md`) and this repository's rule files as they existed at the time it was written.
**Disposition:** all 30 findings (`F01`-`F30`) were checked against primary source (the settlement table, the ESPN API records retrieved during this session, and the raw preserved component text in `PREDICTION_LOG_COMBINED_2.md`) before any correction was made. The disposition of every finding is recorded in `LEARNING_REGISTER.md` section "2026-09-06(d) second independent review disposition", with the resulting corrections spread across `RULES_GENERAL.md` section 15, all ten `RULES_<SPORT>.md` files, `PREDICTION_LOG_COMBINED_2.md`, `IMPROVEMENT_PLAN_2026-09-06.md`, `DATA_SOURCE_REGISTER.md` and `LEAGUE_RULES_CRICKET.md`.

## What was verified and corrected as a direct result of this document

This document's numerical and mathematical claims held up under independent re-derivation from primary source, and several real errors in this session's own earlier work were found and fixed as a result: an O/U diagnosis that contradicted its own settlement table (`F01`), five settlement rows that were recoverable but recorded as missing (`F02`), an incomplete Rank #1/#2 comparison population (`F03`), three newly-adopted gates (`G20.2`/`G21.1`/`G26.1`) that reintroduced the exact same-session-derived-ordinal-rule problem this session had just adopted a firewall to prevent (`F07`/`F11`), a union/intersection category error and an overclaimed "already observed" joint-tail claim in those same gates (`F08`/`F09`), nine sport-specific tail-budget formulas that failed a basic dimensional check (`F10`), an overclaim in a pre-existing coherence gate and an overclaim in a pre-existing winner/cushion gate (`F12`/`F13`), a genuine reasoning defect in a preserved tennis card that this session had not caught (`F14`), an incomplete and partly mislabelled cricket reference population (`F15`), an overclaimed statistical-shape label from a two-observation sample (`F16`), an overstated "cannot fail" claim about a source-register fallback rung (`F18`), an unsupported causal claim about a settled cricket card (`F19`), a team-identity swap in a basketball retrospective (`F22`), and a corridor-containment claim that did not actually hold on any of its stated bounds (`F21`).

Several other findings were checked and found to already be covered by existing controls, requiring no new mechanism (`F05`, `F17`, `F20`, `F23`-`F26`, `F30`) — these are recorded as "already covered" in the disposition table rather than silently ignored. One finding (`F04`) was found to be a since-superseded interim figure rather than a live inconsistency. The full P-001-P-200 game-by-game table this document supplies (its section 7) was not individually re-litigated row by row in this repository's own documents — most of those entries restate or reinforce controls this framework already carries, and the register instead absorbs the underlying *classes* of finding so future work catches the same class automatically, rather than duplicating roughly 200 historical-card annotations a second time.

---

# Game-log blind-spot review — P-001 through P-305, plus the Geelong local record

**Read-only audit of the source records; 6 September 2026.** This is a separate observations document. No changes to predictions, settlements, rules, registers or historical files are proposed as already implemented.

## Overall assessment

The record supports several recurring weaknesses, but it does **not** support automatically preferring Rank #2, underdog cushions, Overs, or first-half selections. The most consequential problems are incomplete row accounting, evidence that is acknowledged without a checkable effect on the forecast, outcome-driven retrospective explanations, and new rules whose wording introduces mathematical or operational contradictions.

There are also important strengths: many corrections preserve the original forecast; several audits distinguish research settlement from ticket action; the September 5 audit correctly warns that complementary selections manufacture raw wins; and the framework already contains substantial controls for identity, current personnel, phase boundaries, scenario arithmetic and adverse branches. Much of the recurring failure is enforcement or evidence propagation, rather than a completely missing rule.

### Scope and limits

- Reviewed the **306 canonical records** in the September 6 ledger: P-001–P-305 and `LOCAL-GEELONG-20260904`. The appendix follows canonical log order, including the local record between P-293 and P-294. This is not a claim of 306 independent physical games: some records are different views of the same event, and some contain multiple issue states.
- Compared available original cards, recorded results, retrospective corrections, current general and sport rules, the learning register, source register, eligibility policy and the supplied pasted analysis. Historical archive copies are provenance, not additional predictions.
- Results below are **the results recorded in this workspace**. This audit did not independently refetch every external scorecard. An internally corroborated settlement and a newly verified real-world result are different claims.
- Some original materials are incomplete. The repeatedly referenced `PREDICTION_LOG_COMBINED_P267_SETTLED_2026-09-03.md` was not found. Several P-241–P-267 settlements can therefore only be followed through inherited summaries and available component text. The archived P-294–P-305 mini log is a summary, not the complete original cards; P-304/P-305 lower-ranked selections cannot be reconstructed from the available summary. Those limitations are identified, not filled with invented results or reasoning.
- The current controlling policy is **EP-2026.09.06-v2**: settled logs count for historical performance, including process failures and live-issued views. Preserve horizon and provenance labels for interpretation; do not resurrect superseded blanket exclusions. Already-decided/no-forecast records still do not become predictive wins, and historical cases do not become prospective tests of rules written afterward.
- `W`, `L`, `P` and `U` mean recorded/reconstructible research win, loss, push and unresolved respectively. They do not establish payout under an unidentified operator's terms.

Primary navigation: [canonical ledger](GAME_LOG_LEDGER_2026-09-06.md), [status index](GAME_LOG_STATUS_INDEX_2026-09-05.md), [combined log through P-271](PREDICTION_LOG_COMBINED.md), [continuation P-272–P-305](PREDICTION_LOG_COMBINED_2.md), [August 22 retrospective](COMPREHENSIVE_RETROSPECTIVE_2026-08-22.md), [September 2 audit](COMPREHENSIVE_SETTLEMENT_AUDIT_2026-09-02.md), [September 5 audit](COMPREHENSIVE_SETTLEMENT_AUDIT_2026-09-05.md), [September 6 improvement plan](IMPROVEMENT_PLAN_2026-09-06.md), [learning register](LEARNING_REGISTER.md), [eligibility policy](PERFORMANCE_ELIGIBILITY_POLICY.md).

## 1. Confirmed accounting and record defects

### F01 — The newest O/U summary uses an incomplete set of ranked selections

The September 6 plan says 8/12 cards had at least one winning ranked O/U selection, and says every O/U selection failed on P-294, P-295, P-297 and P-299. Each of those four cards has a **winning Rank #4 Over in the existing settlement table**. Thus the claim is contradicted by the table it summarizes.

Recalculation from all available ranked goal/point/run/game total selections, excluding corners:

| Card | Available Over results | Available Under results | Highest-ranked O/U |
|---|---|---|---|
| P-294 | W | L | L |
| P-295 | W | L | L |
| P-296 | L | W | W |
| P-297 | W | L | L |
| P-298 | L | W | W |
| P-299 | W | L | L |
| P-300 | PP L; innings L | innings W; PP W | L |
| P-301 | L | W | W |
| P-302 | first half W; full time W | full time L; first half L | W |
| P-303 | L | W | W |
| P-304 | first half W | Not preserved | W |
| P-305 | PP W, batting-first condition met | Not preserved | W |
| **Total** | **8 W / 6 L** | **6 W / 6 L** | **7 W / 5 L** |

There are **26 available total rows: 14 W / 12 L**. All **12/12 cards** contain a recorded winning O/U row. For P-304/P-305 that statement needs only the preserved winning top row; it does not imply their full slates are archived.

The useful event-level directional measure here is **7/12 highest-ranked O/U selections winning**, not 8/12 union coverage. Multiple complementary pairs make “at least one won” largely mechanical. The September 5 audit explicitly explained this, but the September 6 diagnosis regressed to the misleading definition. Its “Overs 4–1 / Unders 5–4” comparison does not describe all ranked total rows. Consequently it cannot justify a direction or geometry rule.

**Evidence:** continuation log, settlement table at lines 7296–7316 and September 6 O/U summary around 7487–7509; improvement plan Parts F and summary; September 5 audit lines 11–13. **Relevant rules:** General G4/G20/G23.1/G34.1 and the existing complementary-row warning in L-055.

### F02 — Five carried-forward cards lose 16 lower-ranked rows in the summary

The later table prints dashes at Rank #2 and below for P-288 and P-290–P-293, although the original continuation log preserves these selections:

| Card; recorded result | Original lower-ranked selections and reconstructible grades | Original continuation-log location |
|---|---|---|
| P-288; Athletics 7–6 Seattle | #2 Over 7.0 **W**; #3 Under 7.0 **L**; #4 Athletics +1.5 **W** | Lines 4758–4761 |
| P-290; Pachuca 2–0 Juárez, goals 53 and 90+10 minutes | #2 first-half Over 0.5 **L**; #3 Pachuca X2 **W**; #4 Pachuca most corners **U in this reconstruction**; #5 full-time Over 2.5 **L** | Lines 5468–5472 |
| P-291; Shelton 25 games, Shapovalov 20 | #2 Over 38.5 **W**; #3 Shelton -5.5 **L**; #4 Under 38.5 **L** | Lines 5930–5933 |
| P-292; North Melbourne 99–7 St Kilda | #2 St Kilda +51.5 **L**; #3 North -51.5 **W**; #4 Over 89.5 **W** | Lines 6427–6430 |
| P-293; Gold Coast 17–14 Port Adelaide | #2 Under 87.5 **W**; #3 Port -13.5 **L**; #4 Over 87.5 **L** | Lines 6785–6788 |

That is **16 omitted rows, 15 arithmetically settleable from recorded scores and one corner row needing its own settling field**. The P-290 corner row is a candidate omission from the supposedly complete follow-up queue; it should be reconciled before declaring the queue exhaustive. This report does not invent its corner count or silently regrade the source.

**Blind spot:** summaries are being rebuilt by prose extraction rather than a complete join on immutable contract IDs. G34.1 needs a row-count reconciliation: supplied rows = settled rows + explicit unresolved/void/withdrawn rows, separately for each frozen issue.

### F03 — Rank comparisons use unequal and incomplete populations

Restoring the five Rank #2 rows above gives a matched 15-card cohort: P-288, P-290–P-293, and P-294–P-303.

| Card | Rank #1 | Rank #2 |
|---|---|---|
| P-288 | L | W |
| P-290 | W | L |
| P-291 | W | W |
| P-292 | L | L |
| P-293 | W | W |
| P-294 | L | W |
| P-295 | L | L |
| P-296 | W | W |
| P-297 | W | L |
| P-298 | L | W |
| P-299 | L | L |
| P-300 | L | W |
| P-301 | L | W |
| P-302 | W | W |
| P-303 | W | W |
| **Matched total** | **7/15 = 46.7%** | **10/15 = 66.7%** |

Both win in **5/15**; neither wins in **3/15**; Rank #1 alone wins in **2/15**; Rank #2 alone wins in **5/15**. The narrower P-294–P-303 comparison is 4/10 versus 7/10. The 17-card Rank #1 record becomes 9/17 after P-304/P-305, but their missing second rows mean it must not be compared as if matched to a 10-card or 15-card Rank #2 record.

This is a descriptive local advantage for Rank #2. It is not a stable “always select Rank #2” result. Earlier recorded cohorts run the other way: P-103–P-123 has Rank #1 14/21 versus Rank #2 12/21; P-137–P-163 has 16/26 versus 12/25 plus one unresolved second row; the six settled cards in the P-239–P-248 cohort have 5/6 versus 2/6. Different sports, lines and issue versions also change the mix.

**Relevant rules:** General marginal-ordering discipline, L-055 and the frozen Rank #2 candidate. Use a matched event-level comparison, retain pushes/unresolved denominators explicitly, and cluster repeated views of a physical event. No global reversal is supported.

### F04 — “Fully graded,” “open,” and record totals are not consistent labels

The canonical ledger totals are arithmetically 285 final/settled + 9 partial + 3 research-settled + 1 unresolved + 1 terminally unsettleable + 7 no-action = **306**. However, “285 fully graded” overstates completeness where a closed event still contains terminal unresolved rows, such as P-070/P-073/P-104/P-105/P-136, or an incompletely archived slate such as P-304/P-305.

The named current open list has **13 records**, not 11 or 12: P-126, P-148, P-149, P-166, P-176, P-178, P-179, P-200, P-217, P-233, P-234, P-235 and P-274. Some prose says “12 plus P-274,” which is 13; other snapshots enumerate more entries than their heading says. Also 306 minus 285 minus 9 minus 3 is **9**, not 12.

Use separate fields for event finality, contract evidence, archive completeness, research grade and operator action. “No score awaited” does not mean “every supplied contract graded.” Investigate the extra P-290 corner row before revising a total.

### F05 — Identity, orientation and phase corrections remain first-order risks

P-006/P-017/P-060 contain sign/identity/duplicate corrections; P-085 records a live Puebla 25–12 lead that is incompatible with the later stated first-quarter Fuerza 24–20 result; P-088's first-half timeline does not match its stated goal count; P-095 used wrong starters despite a winning top row; P-126 remains identity/state-conflicted; P-203 needed score/half/corner correction; P-225 confuses similarly named Zhang players; P-268 first used the wrong 9–6 game before correction to 13–11; P-272 required a previous-score correction. These are not ranking problems that a new tail formula can cure.

Structured sources still need event ID, participant ID, home/away mapping, date/time zone, phase, regulation/extra-time state, units, field-presence and monotonic-score checks. A winning forecast does not validate contaminated inputs. **Relevant rules:** General G0–G4/G10 and sport contract mapping.

### F06 — Incomplete original archives prevent some retrospective claims from being verified

The missing P-267 settlement artifact limits exact reconstruction of parts of P-241–P-267. The P-294–P-305 archive says complete bodies were supplied inline but does not preserve those bodies. A fingerprint of a later summary establishes the summary's identity, not completeness or pre-issue authorship of every claimed rationale.

P-304/P-305 can be assessed for their preserved top selections and subsequent recorded scores. The statement that P-305 won “for the stated reason,” using the same personnel and a particular 72/1 precedent, is not independently demonstrated by the surviving original card text. Preserve the difference between original evidence, later reconstruction and retrospective interpretation. This is a G34.1 implementation gap, not grounds to remove settled logs from the user's historical record.

## 2. The new rules introduce substantive blind spots

### F07 — Disclosure-only candidates are already written as mandatory ordering overrides

The learning register and General's L-084/L-085 map say tail and path disclosures are mandatory while their **ordinal effects remain candidates**. Yet G20.2 bars an exposed row from #1 without a mechanism sentence; G21.1 restricts which row may outrank another; G26.1 disqualifies near-even reference splits. These are ordinal effects, even if described as humility or disclosure.

The candidate champion/challenger cannot remain uncontaminated if the champion is already subject to the challenger restriction. In addition, C-TAIL-BUDGET's challenger bars exposed rows outright, whereas operative G20.2 allows a prose exception. They are different interventions. Clarify the controlling behavior, exception criteria, adoption date and frozen test definition before claiming a candidate was evaluated. **Evidence:** General lines 632–633, 693–695, 799–807; Learning Register L-084/L-085 and candidate manifests.

### F08 — Path-count geometry does not establish relative probability

G21.1 mixes three different concepts: unions of scoring events, an interval staying under a threshold, and a line near the centre of a distribution. These are not mutually exclusive mathematical categories. A whole-match event can be represented as a union of complete paths and simultaneously as constraints on cumulative scoring. Dividing a path into more descriptions increases N without increasing its probability.

First-half Over 0.5 goals is indeed satisfied by at least one goal. Powerplay Over 50.5 runs is **not** satisfied by any one ordinary scoring event; it needs enough cumulative runs. An Under does not become a union merely because the phase is low-scoring. None of these representations makes one selection more likely without estimated event probabilities and their dependence.

The rule therefore risks a built-in Over/short-phase preference, despite its stated neutrality. The rugby-union instruction that a sevens Under should very rarely rank first compounds that risk. The threshold, time exposure, scoring distribution and conditional state determine difficulty. A valid path diagram is useful disclosure; its path count is not a ranking statistic.

### F09 — Second-highest plus median is a stress scenario, not an observed joint tail

G20.2 adds separate teams' second-highest and median L10 scores and calls the result an “already-observed combination.” The component scores may each have occurred, but their combination need never have occurred. Opponents, pace, possession allocation, bowling strength, eras, venue, lineup continuity and match state affect their joint feasibility. Both second-highest scores can be especially incompatible in possession-limited contests.

The second-highest of ten is also a noisy order statistic, not an estimated joint quantile. The rule lacks an explicit branch for fewer than ten comparable matches, tied values, missing fields, changed formats, shortened games and chase-censored cricket innings. Some newest ETPL examples have only two team observations despite “already retrieved L10” wording.

Treat such sums, where dimensionally valid, as labelled sensitivity scenarios. A sentence claiming to **prevent** a past high score recurring is too strong: current evidence may reduce a branch's probability without making it impossible. The present wording rewards persuasive narrative, can penalize an honest uncertainty statement and cannot by itself demonstrate ordinal improvement.

### F10 — Several sport-specific tail recipes fail unit or component checks

These observations concern the literal September 6 additions; they do not imply every older sport model uses the same faulty calculation.

| Sport rule | Problem in the new shorthand | Required interpretation/check |
|---|---|---|
| [AFL](RULES_AFL.md), September 6 tail recipe | Scoring shots × goal-conversion rate gives goals, not points; behinds disappear. | With S = goals + behinds and p = goals/S, points = S(1 + 5p). P-292's 29 shots and 14 goals imply 99 points, not 14. |
| [NRL](RULES_NRL_RUGBY.md) | Tries × kicking percentage omits try points and the value/number of conversion opportunities. | Separate 4T + 2C + 2 penalty goals + applicable field-goal points; model attempt counts and success rates distinctly. |
| [Rugby union](RULES_RUGBY_UNION.md) | The same tries/kicking shortcut omits scoring components. | Separate ordinary tries, conversions, penalty goals, drop goals and penalty tries; use the applicable competition scoring rules. |
| [Cricket](RULES_CRICKET.md) | Adding a team's high innings score to its opponent's median concession double-counts two estimates of the **same innings output**. Calling second-highest/second-lowest phase values “modes” is also invalid. | Combine batting and bowling information into one conditional innings distribution; extrema are not modes. Keep powerplay, six-over checkpoint and whole innings separate. |
| [Ice hockey](RULES_ICE_HOCKEY.md) | Goals plus powerplay-conversion percentage adds a count and a rate. | Need expected powerplay opportunities and time exposure; separate even-strength, special-teams and empty-net contributions without overlap. |
| [Basketball](RULES_BASKETBALL.md) | Possessions × offensive rating requires rating units and normalization; mixing independent extreme pace/efficiency is not a joint tail. | If rating is points per 100 possessions, divide by 100; specify how opponent defence adjusts it. Preserve pace/efficiency dependence. |
| [Soccer](RULES_SOCCER.md) | Adding a post-60-minute bench scoring tail to an already full-match scoring quantity double-counts that interval. | Partition the match into nonoverlapping exposure periods, or replace the existing late-period component. |
| [Baseball](RULES_BASEBALL.md) | Starter-centre + relief high **rate** lacks expected relief innings; starter hook and bullpen exposure are dependent. | Multiply rates by innings/exposure and conserve the game's innings. Include early starter failure as well as late relief failure. |
| [Tennis](RULES_TENNIS.md) | Second-highest set count × median games per set misses close-set variation and legal score/format constraints. | Enumerate legal score paths; sum each player's games and signed handicap directly. |
| [American football](RULES_AMERICAN_FOOTBALL.md) | Points per drive × “opponent drives allowed” needs a coherent possession definition; quarterback-only bench analogues miss line and defensive-unit exposure. | Define drives, clock/field-position effects and unit-specific rotation. A run-heavy blowout does not automatically raise points per drive. |

Additional baseball defect: the new explanation that a 17-run game cannot be a starter misread and must arise after the starters is not inferable from a final total. P-281's seven-run fourth is a direct example of early damage. Attribution needs inning-by-inning scoring and pitcher exposure, not the size of the final score alone.

### F11 — The 40–60% top-slot rule is an unvalidated ranking threshold

G26.1 uses a descriptive population split to remove a row from #1, while G23.1 prohibits mechanical ordinal changes from such splits. Removing one row necessarily changes the order relative to others; calling it a disqualifier does not eliminate the ordinal effect.

There is no demonstrated reason for 40–60 rather than another band, no sample-adequacy requirement, and no reliable procedure for establishing that current evidence moves the conditional probability outside it. `UNKNOWN` passes the gate, creating an incentive to have less measured evidence. The fact that P-300's #2 won by 20.5 runs is a realized margin, not proof that it had a wider **pre-issue probability separation**. Record the base rate and uncertainty; any exclusion rule needs a separately frozen evaluation.

### F12 — Conditional compatibility is being confused with marginal ranking

G25.1's arithmetic and branch-consistency check is useful. Its blanket ban on a `DISJOINT` row appearing in the top half is not generally consistent with ranking individual selections by marginal probability.

Counterexample: three mutually exclusive complete outcomes have probabilities 0.45, 0.40 and 0.15. Selections A and B cover the first and second outcomes respectively. A and B are correctly ranked first and second, although they cannot both win. A card may have a single coherent joint distribution and still contain incompatible high-ranked marginal selections.

Distinguish an impossible score tree, a contradictory probability assignment, and a deliberate objective to maximize the probability that **both** top selections win. The last is a portfolio objective and may yield a different ranking; it should not be silently imposed on marginal ordering. Opposing picks can be supplied legitimately without manufacturing performance credit.

### F13 — Cushion strength does not force an underdog winner call

G30.1 correctly asks winner and handicap reasoning to use the same distribution. Its suggestion that strong cushion evidence necessarily transfers substantial weight to the outright-win branch is too strong.

Example: favourite wins narrowly 50% of the time, wins by more than the handicap 30%, and loses 20%. The underdog cushion wins 70%, while the favourite still wins outright 80%. Both can be well-supported high-confidence conclusions. The share carried by narrow losses must be measured or reasoned through, not presumed.

Also, “team receiving points” is not synonymous with “weaker team.” P-303 literally gives strongly favoured Nigeria **+25.5**. Preserve the supplied sign, flag the unusual contract for identity/sign confirmation, and do not cite it as evidence that an underdog strategy works. The same caution applies to unusual supplied signs such as P-276.

### F14 — Tennis match wins and aggregate-game handicaps are still conflated

P-287 prompted explicit score-tree arithmetic repairs, but P-291 still says Shapovalov +5.5 covers every Shapovalov match win. That is false in best-of-five tennis. A legal winner can lose 0–6, 0–6 and win 7–6, 7–6, 7–6: the winner has 21 games to the loser's 30 and fails +5.5.

The actual P-291 match has **45 total games**, 25–20, not “20–25 total games”; two tiebreak sets do not erase the other sets. Its +5.5 win is valid, but does not validate the general claim. The retrospective's 5–0 H2H also differs from the original 4–0 reference and needs cutoff reconciliation. Current G4/G20, Tennis mapping and L-068 already cover this failure class; it persisted despite the repair.

## 3. Cricket-specific observations from the first logs to the latest

### F15 — The September 6 ETPL reference population is not reproducibly complete

The ten numbers in the plan are 28, 39, 49, 50, 51, 55, 56, 61, 68 and 72. Their **mean 52.9 and median 53 are correct**. The problem is their identity, inclusion rule and interpretation.

- The table describes matches 9–13 as every completed relevant powerplay before the latest matches, but earlier logs already contain full six-over observations: P-099 Amsterdam **56/2**, P-115 Belfast **52/3**, and P-171 Glasgow **44/2**, among others. These require an explicit inclusion/exclusion explanation.
- “Amsterdam's only prior full powerplay was 72/1” conflicts with the preserved P-099 56/2 observation.
- The table labels Match 13 Amsterdam–Glasgow, with 72/1 and 56/0. P-286 and the September 5 audit instead identify Match 13 as **Belfast–Glasgow**, reduced to 12 overs, Belfast first six **54/2**, with an actual **four-over powerplay 40/1**. The new table cannot be treated as an uncontested baseline until those event identities are reconciled.
- P-252's match-number labeling also needs reconciliation with the new table. Match numbers alone are not safe joins.
- Mixing first and second innings does not directly estimate a batting-first contract. Chases are conditional on target, remaining wickets and termination; the two innings of one match are not independent observations.
- A toss winner's choice is not automatically a 50% chance that a specified team bats first; both captains' conditional choices matter.

**Relevant rules:** Cricket phase/format identity, G10/G13.1 population continuity, reference-rate provenance, and the cricket league adapter. Keep the descriptive arithmetic, but qualify/quarantine the disputed sample mapping before using it for an ordinal rule.

### F16 — Two wicket observations do not establish bimodality

P-300's cited Edinburgh priors are **68/3 and 55/1**, averaging two wickets. That does not establish a bimodal powerplay run distribution, nor a validated discontinuity at the new 1.5-wicket cutoff. The 68/3 observation itself demonstrates that several wickets can coexist with high scoring. Timing, incoming batter quality, scoring before dismissals and bowling exposure matter.

Explicit wicket-resource branches are sensible and were already relevant in P-007/P-019/P-032/P-094/P-099/P-115/P-171/P-175/P-187/P-216/P-217/P-236/P-237/P-238/P-252/P-283/P-286. Calling a distribution “bimodal,” assigning its mass, or forcing a ranking from n=2 is a stronger statistical claim. Separate the promoted process requirement to retrieve wickets from any candidate shape or weighting rule.

### F17 — Phase, resource and format mismatches recur more often than a missing universal pitch rule

P-020 needs a Hundred 25-ball powerplay, not 30 balls. P-094 is a five-over checkpoint. P-216's early acceleration and later lower-order partnership are distinct innings mechanisms. P-217 requires explicit shortened-match action and phase remapping. P-286's supplied first-six-over contract is **not** its reduced-match four-over powerplay. P-300's 28/3 powerplay and 148 innings, and P-305's 60/1 powerplay and 169/7 innings, demonstrate why phase and full-innings directions can differ without contradiction.

Do not pool these endpoints by the word “powerplay.” Define legal balls, wickets, batting order, innings identity, target, planned overs and revised phase rules before comparison.

### F18 — The six-rung pitch ladder is useful, but its guaranteed fallback is overstated

The [source register](DATA_SOURCE_REGISTER.md) §6A improves acquisition discipline. However, “rung 6 cannot fail” / “always computable” is false for a new venue, missing same-format observations or insufficient comparable data. A historical venue baseline is also not a current-strip inspection.

Two retrieved rungs can share the same upstream quote, so they are not automatically independent confirmation. Toss and match-state information do not necessarily describe the pitch. A curator's earlier-season comment has a different validity period from a same-day report. Exact conditional refresh timing should depend on the contract's issue cutoff and available publications.

The honest endpoint can be `UNKNOWN`, with an explicitly labelled broader comparable-context prior and wider uncertainty. The user may still request a ranking under uncertainty; the ladder should expose its basis instead of fabricating pitch certainty. The supplied pasted analysis understates these fallback limitations.

### F19 — Later matches cannot prove the cause of P-300's low powerplay

P-300 records 28/3; P-305 records 60/1, and another later phase records 69. Later scoring does not by itself rule out different strips, conditions, attacks or event states in P-300. Nor does P-300's failure prove that wickets were the only causal explanation.

A retrospective can say early wickets are consistent with the observed low phase. It cannot infer their pre-match probability or eliminate other causes from subsequent high scores. Where the retrospective calls wicket retrieval defective but elsewhere records no compliance defect, distinguish a rule that existed at issue from a new proposed diagnostic.

## 4. Retrospective reasoning and evidence propagation

### F20 — A named kill path is neither sufficient compliance nor proof of bad ranking

Across P-002/P-034/P-059/P-064/P-068/P-083/P-090/P-096/P-114/P-131/P-138/P-150/P-152/P-159/P-184/P-220/P-229/P-247/P-270/P-280/P-295/P-299/P-301, adverse mechanisms repeatedly appear in prose and subsequently occur. The enduring issue is whether the frozen forecast shows how that evidence changed the corridor, branch ordering or uncertainty.

L-006/L-009/L-010/L-029/L-033/L-038/L-039/L-043/L-047/L-058/L-065/L-069/L-070 already address variants of this. Adding another named branch does not solve non-propagation. Conversely, a plausible adverse branch can rationally remain less likely and then occur. A loss alone does not prove it was underweighted.

Require an auditable before/after implication of material evidence, or an explicit reason it does not change the estimate. Grade process against the issue-time rule and available evidence; use repeated outcomes to test weighting. Without issued numerical probabilities, avoid treating “calibration defect” as an established quantitative result.

### F21 — Winning results receive more generous process narratives than losing results

P-085's winning rows coexist with an impossible live snapshot; P-095's top Over wins with wrong starter identification; P-112's side succeeds through a different mechanism than its starter explanation; P-204's cushion wins while the separate winner call fails. These should receive the same input and mechanism audit as losses.

P-303 is the clearest recent arithmetic example. The retrospective calls Nigeria 81–53 “almost exactly” inside Nigeria 72–78, Hungary 64–71, total 136–149. **Both team scores and total 134 are outside**, and margin 28 is outside the implied 1–14 central margin. Winning Nigeria +25.5 and Under 145.5 does not make the forecast corridor accurate.

P-304's first-half Over wins through a penalty; that is a valid winning path, not proof that the model identified its probability or that the result was “not luck.” Late substitute goals explain the full-time result, not the already-settled first-half goal. P-302's three Bournemouth corners beat 2.5 by **0.5 numerically**; it is the smallest integer winning count, rather than a one-corner numerical margin. Its first-half and full-time Overs both won, so this card alone does not show one outperformed the other.

### F22 — The P-299 personnel correction changes team identity in later rule text

The continuation retrospective states **Spain** lacked five eventual World Cup rotation players in the friendly, and separately notes Mali's Sika Koné was absent from its reported friendly box score. Later learning/rule wording attributes the five-player absence to **Mali**. That changes the causal premise of the precedent.

The appropriate lesson is to reconcile named players, team, date, competition and expected exposure before transferring an exhibition margin. “Use current tournament data above any friendly” should also be conditional on opponent and roster comparability; one current game is not automatically a reliable replacement sample. **Evidence:** continuation lines 7348–7352; Basketball's later P-299 learning/September 6 additions.

### F23 — Knowability must be timestamped, not assumed from post-match reports

P-280 has identifiable pre-match personnel information; P-289's late Taylor withdrawal needs its publication time relative to issue; P-286's Maharaj absence is not established as knowable before the cutoff merely because he did not play; P-295's sin-bin after 15 seconds was unknowable pregame.

Distinguish confirmed-before-issue facts, scheduled-but-unavailable lineup confirmation, reasonable pre-match uncertainty, and realized in-game shocks. The September 5 audit often does this well. Later summaries should preserve those distinctions instead of upgrading every eventual absence to a research failure.

### F24 — Bench/coaching analysis was already required; the gap is consistent implementation

The September 6 plan says the earlier framework had no bench/coaching gate. The saved pre-update Soccer rules already require the XI, goalkeeper, **bench**, formation and expected minutes; the pre-update General rules already discuss bench/sub quality and expected exposure. P-174/P-180/P-273 retrospectives also identify substitute mechanisms.

G14.2 can improve a dedicated structured record and make omissions visible, but it should be described as stronger enforcement/schema coverage, not the discovery of a wholly absent requirement. Bench analogues differ by sport: relievers, batting resources, replacement lines, substitutes and reserve quarterbacks are not interchangeable. Allow explicit `NOT_APPLICABLE`; justify any 40%-starts or 15-minute thresholds instead of treating them as validated impact cutoffs.

### F25 — Several familiar heuristics remain conditional, not rules of direction

- **Low total does not imply a close margin:** P-062/P-131/P-158/P-193/P-206/P-284/P-298. A shut-down opponent can lose heavily in an Under.
- **A short starter outing does not automatically cause an Over:** P-043/P-055. Actual relief quality and innings matter.
- **A rookie/replacement is not automatically weak:** P-064/P-068/P-096/P-295; use their own current evidence and role.
- **A winning cushion is not proof the winner call was correct:** P-008/P-022/P-054/P-060/P-112/P-204/P-240/P-244/P-271/P-293.
- **High possession, many goals and many corners are different processes:** P-023/P-031/P-047/P-080/P-098/P-113/P-147/P-173/P-183/P-194/P-197/P-201/P-202/P-208/P-210/P-273/P-290/P-302.
- **A streak does not compel continuation or reversal:** P-059/P-296 and the existing L-011/L-062 controls.
- **Tournament advancement is not a regulation-time win:** P-041/P-045/P-063/P-079/P-098/P-107/P-121/P-130/P-255/P-256.

These are recurring boundaries already represented in the sport rules. Enforce them in the actual contract arithmetic and component model; do not replace one oversimplified heuristic with its opposite.

## 5. Sourcing, settlement and validation governance

### F26 — Structured data is preferable for many fields, but is not infallible or independent by default

G10.1's suggestion that a structured result cannot be misread is too absolute. A valid JSON field can belong to the wrong event, contain a provisional value, use a different phase or map participants in an unexpected order. Zero can mean a genuine zero, an unpopulated shell or unsupported coverage; P-123 illustrates that distinction.

ESPN summary, ESPN scoreboard and an ESPNcricinfo endpoint are not automatically three independent sources. Count publisher/upstream lineage, not URLs. A 403 in an automation client establishes an access failure in that route, not global absence of evidence; a guessed endpoint's 400 or an empty search likewise does not prove competition-wide noncoverage. Earlier official corner settlements also contradict blanket “corners are unavailable” claims.

Pre-register expected provider, event ID and required settling fields, then verify those fields after final. Do not require a future final field to exist pregame. Preserve alternate official lanes such as NV Play; “no ESPN ID means unsourced” would wrongly discard useful evidence from P-286's source family.

### F27 — Competition rules cannot determine an unidentified operator's contract action

G36.1 correctly pushes against indefinite unresolved **research scores**. However, sporting rules do not determine all retirement, reduced-overs, overtime or listed-pitcher ticket terms. Price independence is not operator-term independence.

P-136, P-166, P-200, P-217 and P-274 demonstrate the distinction. A score can support a clearly labelled research grade under an explicit convention while operator action remains unknown. Earlier General §8 and September 5 audit language already make this separation. Use two fields rather than inventing a universally standard betting settlement. This preserves the user's settlement-based historical eligibility without asserting a ticket payout.

### F28 — Candidate tests need a single frozen intervention and independent units

C-TAIL-BUDGET and C-PATH-GEOMETRY need resolution of F07–F11 before their comparisons are interpretable. The tail manifest's unconditional bar differs from the operative prose-exception gate. A stopping rule referring to a predeclared date must actually specify that date. Multiple total pairs on one event are dependent; “40 pairs” is not automatically 40 independent events. Pair direction, threshold and phase can confound the proposed geometry comparison.

The Rank #2 candidate's paired prospective approach is appropriate in principle, but needs complete original ranks, one defined issue per evaluation unit, frozen handling of pushes/unresolved rows and physical-event clustering. Do not use discovery games as validation of a rule derived from those games. Historical eligibility and suitability for a particular prospective experiment are different questions.

### F29 — Method/version authority is difficult to follow across active documents

The current General rules declare v3.7, while some cards and register headings still refer to older versions. Historical version labels are legitimate when explicitly historical. The problem is an active instruction that appears to govern new work while referring to a superseded gate or status.

G0's fresh rule read addresses the P-268/P-270/P-271 stale-method pattern, but a fresh read cannot resolve contradictory current text by itself. Maintain an explicit precedence map for mandatory process, experimental ordinal changes and historical examples. General's rule against dated narratives in active rules also conflicts with extensive dated sport additions. That is a maintainability/compliance contradiction, even when the examples are useful.

### F30 — No reliable aggregate all-history strike rate follows from the present summaries alone

The August 22 audit corrected an early raw tally to 61 W / 46 L rather than 63 W / 44 L. Later summaries mix primary selections, every supplied row, repeated live views, paired opposites, terminal unknowns and imported settlement updates. F01–F06 add fresh evidence that a single pooled headline would be premature.

A reproducible history table would need physical event ID, canonical card ID, issue/horizon, frozen rank, exact contract, original source location, settling field, outcome, unresolved/action status, method version and process grade. This is an observation about what is missing, not an instruction executed in this audit. Current counts are useful only with their stated denominators. No profit, market edge, calibration or causal uplift can be inferred from raw W/L counts without the corresponding probabilities/prices and evaluation design.

## 6. Priority order for future decisions — observations only

1. **Repair evidence and accounting first:** F01–F06 and F15. Reconcile missing supplied rows, disputed cricket identities, incomplete archives and summary denominators.
2. **Resolve rule contradictions before relying on new ordering gates:** F07–F14. Correct the unit errors and separate disclosure from experimental ranking effects.
3. **Make process grading auditable:** F20–F24. Preserve issue-time knowability; examine winning and losing cards symmetrically; distinguish observed outcomes from probability claims.
4. **Preserve the useful existing controls:** exact contract mapping, current participants, phase identity, scenario arithmetic, adverse branches and research/operator separation.
5. **Evaluate proposed ordering changes prospectively:** F28–F30. The evidence supports testing; it does not support an automatic Rank #2, cushion, Under/Over or short-phase policy.

## 7. Game-by-game observations

Each entry below records the available outcome/reconstruction and the most relevant comparison with the rules. Absence of a new defect in an entry is not certification that every source fact was correct. Rows marked inherited or incomplete have the limitation described in F06. Event names and canonical order come from the linked ledger; local source references are provided for navigation.

Rule families: **ID** = General identity/state/source/contract gates; **AR** = General G4/G20 and sport-native arithmetic; **EV** = General evidence continuity/exposure and G14/G17; **BR** = General branch/ordering G20/G23/G25/G26/G30, subject to F07–F14; **ST** = settlement/archive G34/G36 and §8, subject to F27. Each row also inherits its named sport's relevant rule file from F10.

### P-001?P-100

| Record / event | Recorded outcome and observation | Rules |
|---|---|---|
| [P-001](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Welsh Fire Women v Trent Rockets Women, The Hundred Women's 11th Match (carried over from legacy V6-022) | Trent 132/2 beat Welsh 129/3. Winner right, higher totals wrong; distinguish chase termination from an uncensored first-innings ceiling. | AR, BR |
| [P-002](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Philadelphia Phillies @ Miami Marlins (MLB regular season) | Miami 8?6. Winning cushion did not rescue the wrong Philadelphia winner/Under rationale; audit the winning row's mechanism too. | EV, BR |
| [P-003](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? FC København v Polissya Zhytomyr (UEFA Conference League, Q2, 2nd leg) | Copenhagen 2?1. Goals/player rows graded; a corner row remains terminally unsettleable. Closed event is not fully graded slate. | ID, ST |
| [P-004](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? MI London (Men) v London Spirit (Men), The Hundred Men's Competition 2026 | Spirit 165/3 beat MI London 164/5. Phase/full-innings Unders worked; Over/winner directions did not. Preserve separate phase resources. | AR, BR |
| [P-005](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Texas Rangers @ Tampa Bay Rays (MLB regular season) | Tampa Bay 3?2. Side worked, Over 8 failed. Starter/relief run components need their own support. | EV, BR |
| [P-006](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Southern Brave (Men) v Birmingham Phoenix (Men), The Hundred Men's Competition 2026 | Brave 128, Birmingham 116. Full-innings Under worked; phase Under/winner failed. Sign/source correction reinforces exact contract mapping. | ID, AR |
| [P-007](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Manchester Super Giants (Men) v Trent Rockets (Men), The Hundred Men's Competition 2026 | Trent 140/4 beat Manchester 137/3. Phase Over won while full-innings Over failed; early scoring is not a complete innings distribution. | AR, EV |
| [P-008](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? New York Yankees @ Chicago Cubs, MLB regular season | Yankees 2?0. Cushion/Under won; Cubs winner failed. Receiving runs and winning outright remain different events. | AR, BR |
| [P-009](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Indiana Fever @ Portland Fire, WNBA regular season — FORECAST | Indiana 112?98. Winner right, three correlated Unders lost. One shared pace/scoring miss is not three independent lessons. | EV, BR |
| [P-010](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Carlton v Brisbane Lions, AFL Round 21 — FORECAST (locked 2026-08-01T08:56:26Z / 18:56:26 AEST) | Carlton 154?78. Cushion won but Brisbane winner/total failed. Scoring opportunity and conversion tails defeated the central read. | EV, BR |
| [P-011](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Arizona Diamondbacks @ Cleveland Guardians — PREGAME CARD | Cleveland 5?0. Cleveland winner right, Arizona cushion top row wrong. Run suppression need not preserve a close margin. | BR |
| [P-012](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Welsh Fire Women v Southern Brave Women, The Hundred Women's Competition 2026, Match 19 | Welsh 122/6 beat Brave 121/5. No formal forecast; correct Under watch direction should not become a formal issued win. | ID, ST |
| [P-013](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Welsh Fire Men v Southern Brave Men, The Hundred Men's Competition 2026, Match 19 | Welsh 116/4 beat Brave 115/8. Informal Under watch right, phase Over wrong. Preserve watch versus forecast and phase distinction. | ID, AR |
| [P-014](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? San Diego Padres (Michael King) at Arizona Diamondbacks (Brandon Pfaadt) | Arizona 5?1. Abstention/watch material should retain its status; correct winner direction is not automatically an issued contract win. | ID, ST |
| [P-015](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Sri Lanka Women vs Pakistan Women, 3rd T20I | Pakistan 115/6 beat Sri Lanka 113/6. Both Unders won, Sri Lanka winner lost. Suppression and winner allocation are distinct. | BR |
| [P-016](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Kiwoom Heroes at Lotte Giants, KBO regular season | Lotte 3?2. Supplied rows won, but centre remained too high. Evaluate forecast distribution even when thresholds are forgiving. | EV, BR |
| [P-017](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Sunrisers Leeds Women v London Spirit Women, The Hundred 2026 | Sunrisers 142/5 beat Spirit 136/7 after identity correction. Original and live directions differed; do not merge issue states. | ID, ST |
| [P-018](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Sunrisers Leeds Men vs London Spirit Men, The Hundred 2026 Match 20 (2026-08-04) | Sunrisers 241/2, Spirit 204/6. Full-innings Under failed badly while phase band/winner worked. Death-overs ceiling was underrepresented. | EV, BR |
| [P-019](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Manchester Super Giants Women v Welsh Fire Women, The Hundred Women's Competition 2026, Match 21 | Welsh 88/7 beat Manchester 85/9. Original Over/winner failed; later Under/new winner worked. Live information cannot validate pregame inference. | ID, EV |
| [P-020](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Trent Rockets Women v Birmingham Phoenix Women, The Hundred Women's Competition 2026, Match 22 | Trent 124/4 beat Birmingham 122/7. Rows worked. Preserve Hundred's 25-ball powerplay rather than silently using 30 balls. | AR |
| [P-021](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Los Angeles Angels (Reid Detmers) at Baltimore Orioles (Trevor Rogers), MLB | Baltimore 5?2. No forecast issued; administrative closure, not a predictive win. | ID, ST |
| [P-022](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Los Angeles Angels (Ryan Johnson) at Baltimore Orioles (Brandon Young), MLB | Angels 4?1. Under/cushion worked, Baltimore winner failed. Same suppression distribution can favour the opposite winner. | BR |
| [P-023](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Benfica v Heart of Midlothian, UEFA Europa League qualifying | Benfica 6?1; eight corners. Goals were abundant but the corner selection failed. Goals do not proxy corner volume. | EV, AR |
| [P-024](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Toronto Tempo @ Portland Fire, WNBA regular season - LIVE FORECAST (appended 2026-08-07 AEST) | Portland 97?83; Q1 48, H1 88. Raw card 3?1 with full-game Over miss. Keep phase successes separate from full-game pace. | AR, BR |
| [P-025](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Brisbane Lions v Hawthorn, AFL Round 22 - LIVE FORECAST (appended 2026-08-07 AEST) | Brisbane 125?58. Several selections won but Under/Hawthorn direction failed. Conversion and one-sided scoring need explicit budgets. | EV, BR |
| [P-026](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Birmingham Phoenix Women v Sunrisers Leeds Women, The Hundred 2026 - START-CROSSED/PRE-DELIVERY FORECAST (appended 2026-08-08 AEST) | Sunrisers 111/1 beat Birmingham 107/9. Three of four rows won; low chase termination still exposed an over-high lower band. | AR, BR |
| [P-027](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Melbourne v Fremantle, AFL Round 22 - LIVE FORECAST (appended 2026-08-08 AEST) | Melbourne 113?109. Cushion/Over worked; top Under and winner failed. Close-game scoring and winner probability need separate treatment. | EV, BR |
| [P-028](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? West Coast v Collingwood, AFL Round 22 - LIVE FORECAST (appended 2026-08-09 AEST) | Collingwood 117?98. All rows won, top by 0.5. Thin realized clearance is a boundary observation, not proof of calibrated confidence. | AR, BR |
| [P-029](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? St Kilda v Carlton, AFL Round 22 - PREGAME FORECAST (appended 2026-08-09 AEST) | Carlton 106?62. Three of four rows won; cushion ordering still missed the margin distribution. | BR |
| [P-030](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Sunrisers Leeds Women v Welsh Fire Women, The Hundred 2026 Match 27 - PREGAME FORECAST (appended 2026-08-09 AEST) | Sunrisers 122/4 beat Welsh 121/8. Lower Over missed by 0.5. Chase target and legal endpoint determine the available run ceiling. | AR |
| [P-031](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Manchester City v Atletico Madrid, 2026 Coupang Play Series - LIVE FORECAST (appended 2026-08-09 AEST) | City 3?1, City three corners. Corner Over failed despite attacking success. Separate chance creation from corner production. | EV, AR |
| [P-032](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? London Spirit Women v Birmingham Phoenix Women, The Hundred 2026 Match 28 - START-CROSSED/PRE-DELIVERY FORECAST (appended 2026-08-09 AEST) | Spirit 140/4, Birmingham 108/8. Mixed 2?2 result; late scoring defeated full-innings suppression while other phase reasoning survived. | EV, BR |
| [P-033](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Cincinnati Reds at Washington Nationals - PREGAME FORECAST (appended 2026-08-10 AEST) | Washington 7?1. Total eight makes Over 8 a push. Exact-line arithmetic and push denominator matter. | AR, ST |
| [P-034](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Baltimore Orioles at Minnesota Twins - PREGAME FORECAST (appended 2026-08-11 AEST) | Minnesota 9?5. Top winner failed despite a live adverse branch. Require a traceable ranking effect, not just risk prose. | EV, BR |
| [P-035](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Atlanta Dream @ Connecticut Sun, WNBA regular season - LIVE FORECAST | Atlanta 104?69; Q1 45, H1 83. Mixed phase rows; Q2 requires its own possession/rotation explanation. | AR, EV |
| [P-036](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Philadelphia Phillies at Minnesota Twins — MLB Field of Dreams | Philadelphia 7?1. Mixed 2?2 card. Separate starter exposure from relief allocation before attributing the total. | EV, BR |
| [P-037](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Jamaica Kingsmen vs Guyana Amazon Warriors — CPL | Jamaica 117, Guyana 118/4; PP 26. Under worked but central lower band was too high. Winning line is not accurate corridor. | AR, BR |
| [P-038](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Australia vs Bangladesh — 1st Test | Bangladesh 426 and 57/1; Australia 198 and 284. Winner and most rows worked; preserve innings and match endpoints separately. | AR, ST |
| [P-039](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Manly-Warringah Sea Eagles vs Dolphins — NRL | Dolphins 22?0. Under/winner worked. A shutout supports suppression but can still produce material separation. | BR |
| [P-040](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Fremantle vs Adelaide Crows — AFL | Fremantle 112?88. Mixed rows and live views; winner miss must not be overwritten by later issue-state success. | ID, EV |
| [P-041](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Wolverhampton Wanderers v Blackburn Rovers, EFL Championship Round 1 — PREGAME FORECAST (appended 2026-08-15T02:07:19+10:00) | Wolves 2?2. Formal rows worked but standalone winner drew. Regulation draw differs from a protected double-chance selection. | AR, ST |
| [P-042](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Manchester Super Giants Men v Sunrisers Leeds Men, The Hundred Eliminator — LIVE FORECAST (appended 2026-08-15T03:01:20+10:00) | Manchester 186/4, Sunrisers 166/7; PP 30. Mixed result. Low early phase did not prevent a high death-overs outcome. | EV, BR |
| [P-043](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? St. Louis Cardinals at Chicago Cubs, MLB — PREGAME FORECAST (appended 2026-08-15T04:16:53+10:00) | Cubs 3?0. Side worked; a short starter outing did not generate an Over. Relief exposure needs quality and innings evidence. | EV |
| [P-044](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Richmond v Collingwood, AFLW — PREGAME FORECAST (appended 2026-08-15T16:58:00+10:00) | Richmond 46?28. Primary 2/2 success. Territory and scoring opportunities remain stronger explanation than final score alone. | EV, BR |
| [P-045](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Hawthorn v Collingwood, AFL — PREGAME FORECAST (appended 2026-08-15T19:35:00+10:00) | Hawthorn 92?92 Collingwood. Draw defeats an outright-winner call; ensure three-way outcome treatment. | AR, ST |
| [P-046](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Chelsea v Real Sociedad, soccer — PREGAME FORECAST (appended 2026-08-15T22:49:00+10:00) | Chelsea 3?1; corners 4?2. Rows won, some near their boundary. No independent calibration follows from one complete card. | AR, BR |
| [P-047](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Bayern Munich v RB Leipzig, soccer — PREGAME FORECAST (appended 2026-08-15T22:59:00+10:00) | Bayern 3?1; corners 2?1. Corner forecast failed despite goals. Goal efficiency can reduce repeated corner sequences. | EV, AR |
| [P-048](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Essendon v Sydney Swans, AFL Round 23 — ZERO-SCORE LIVE-START FORECAST | Sydney 112?76. Top Under lost, winner worked. Aggregate scoring ceiling and margin should be separately modeled. | EV, BR |
| [P-049](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Doosan Bears at KIA Tigers, KBO regular season — PREGAME FORECAST | KIA 2?1. Primary side/Under worked despite high central estimate. Audit distribution accuracy as well as contract wins. | EV, BR |
| [P-050](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Trent Rockets Women v Sunrisers Leeds Women, The Hundred 2026 Final — LIVE ORIGINAL-LINE ASSESSMENT | Trent 92/2 beat Sunrisers 91. Live Under worked; original floor remained high. Preserve chase-censoring and live horizon. | ID, AR |
| [P-051](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? FC Basel v FC Barcelona, senior men's club friendly — PREGAME FORECAST | Barcelona 5?2, eight corners. Rotation's defensive effect needs explicit exposure; lineup changes do not imply lower scoring. | EV, BR |
| [P-052](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Athletics at Kansas City Royals, MLB regular season — PREGAME FORECAST | Kansas City 9?5. Starter home-run tail matters alongside relief; do not attribute all high totals to bullpens. | EV, BR |
| [P-053](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Yomiuri Giants at Yokohama DeNA BayStars, NPB Central League — PREGAME FORECAST | DeNA 4?3. Mixed 2?2 card with wrong winner. Opposing cushion/total rows are not independent confirmations. | AR, BR |
| [P-054](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Kiwoom Heroes at Lotte Giants, KBO — PREGAME FORECAST | Lotte 5?4. Both +1.5 cushions can win simultaneously. Correctly count overlapping selections without inferring two independent edges. | AR, BR |
| [P-055](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Detroit Tigers at Pittsburgh Pirates, MLB — PREGAME FORECAST | Pittsburgh 4?3. Short starting exposure did not automatically imply high total; conserve starter/relief innings. | EV, AR |
| [P-056](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Arizona Diamondbacks at Boston Red Sox, MLB — PREGAME FORECAST | Arizona 7?6 in ten. Home-run and extra-inning tails require explicit endpoint treatment. | AR, BR |
| [P-057](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Minnesota Lynx @ Golden State Valkyries, WNBA — LATE ADMINISTRATIVE IMPORT OF ISSUED CHAT FORECAST | Minnesota 77?66; Q1 34, H1 67. Unsupported Q2 extrapolation remains a process issue; settlement eligibility is retained under current policy. | EV, ST |
| [P-058](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? St Kilda v Gold Coast SUNS, AFL Round 24 — ZERO-SCORE WARMUP / ORIGINAL-LINE FORECAST | Gold Coast 103?80. Primary 0?2. Clearance/territory evidence did not adequately translate to scoring opportunities. | EV, BR |
| [P-059](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? St. Louis Cardinals (Michael McGreevy) at Cincinnati Reds (Brady Singer), MLB — ZERO-SCORE WARMUP / ORIGINAL-LINE FORECAST | St Louis 10?9. Under-streak reasoning lost to home-run/relief exposure. A streak is neither a continuation nor automatic reversal law. | EV, BR |
| [P-060](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? New York Yankees (Gerrit Cole) at Baltimore Orioles (Kyle Bradish), MLB — INCLEMENT-WEATHER START DELAY / ORIGINAL-LINE FORECAST | Yankees 6?1. Under does not mean close game. Duplicate P-059 material inside source requires canonical separation. | ID, BR |
| [P-061](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Hokkaido Nippon-Ham Fighters at Chiba Lotte Marines | Lotte 3?2 Fighters. Under 8.5 won; Fighters winner lost. Suppression and winner allocation differ. | BR |
| [P-062](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? West Coast Eagles v Hawthorn (late import) | Hawthorn 107?45. Under 198.5 won; West Coast +59.5 lost. One-sided low aggregate can still defeat a large cushion. | BR |
| [P-063](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Newcastle United v Liverpool (late import) | Newcastle 2?2 Liverpool; eight corners. X2 won, Over 8.5 corners and Osula SOT failed; provider xG correction matters. | ID, AR, EV |
| [P-064](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Texas Rangers (Kumar Rocker) at Chicago White Sox (José Urquidy), MLB — PRE-FIRST-PITCH FORECAST | Texas 11?2. White Sox +1.5 and Under 9.5 lost. Current starter upside was knowable; generic rookie framing was insufficient. | EV, BR |
| [P-065](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Golden State Valkyries at Minnesota Lynx, WNBA regular season — PRE-TIP FORECAST | Golden State 80?66. Under 162.5 won, Minnesota -5.5 lost. Roster creation/absence effects must reach margin allocation. | EV, BR |
| [P-066](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Atlanta Dream at Los Angeles Sparks, WNBA regular season — PRE-TIP FORECAST | Atlanta 78?71. Atlanta -10.5 lost, Under 181.5 won. Low total is not evidence for favourite separation. | BR |
| [P-067](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Doosan Bears at KT Wiz, KBO regular season — PRE-FIRST-PITCH FORECAST | Doosan 3?1. Under 11 and Doosan +1.5 won; KT winner failed. Reconcile side and winner without forcing equality. | BR |
| [P-068](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Hanwha Eagles at SSG Landers, KBO regular season — PRE-FIRST-PITCH FORECAST | SSG 7?1. Hanwha -1.5 lost, Under 10.5 won. Rookie good-tail evidence must survive into branch weighting. | EV, BR |
| [P-069](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Lotte Giants at KIA Tigers, KBO regular season — PRE-FIRST-PITCH FORECAST | KIA 8?5 after walk-off grand slam. Winner worked, Under 9.5 failed. Terminal play can add more than the minimum winning run. | AR, BR |
| [P-070](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Central Ballester Reserves vs El Porvenir Reserves — START PASSED / LIVE STATE NOT VERIFIED | Central Ballester 0?1. X2/first-half Under research directions graded; no-action/state and unresolved corner distinctions survive event closure. | ID, ST |
| [P-071](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Alejandro Juan Mano vs Alejandro Turriziani Alvarez, ITF M25 Oviedo — DELAYED / NOT STARTED FORECAST | Juan Manuel 6?4, 6?4. ML/Under 20.5 won; -4 pushed; Under 19.5 lost. Integer boundaries matter. | AR, ST |
| [P-072](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Jelle Sels vs Stijn Paardekooper — DELAYED / NOT STARTED FORECAST | Sels won 2?1. All four rows won through a shared three-set path. Do not count the result as four independent validations. | AR, BR |
| [P-073](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Tobol Kostanay vs Kaisar Kyzylorda — PREGAME FORECAST | Tobol 3?2, HT 2?1. 1X won; full/half Unders lost; corner unresolved. Full settlement label masks sub-row uncertainty. | AR, ST |
| [P-074](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Maccabi Herzliya U19 vs Hapoel Rishon LeZion U19 — PREGAME FORECAST | Maccabi U19 4?3, HT 3?3. Full/half Unders failed. Sparse youth samples need broad scoring tails and explicit evidence limitations. | EV, BR |
| [P-075](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? OKS vs Middelfart — PREGAME FORECAST | Middelfart 1?0, 16 corners. X2 won; goal Over and corner Under lost. Distinct territorial and finishing processes. | EV, AR |
| [P-076](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? FK Horní Ředice vs FK Dukla Praha — PREGAME FORECAST | Dukla 5?0, seven corners. All rows won; sparse corner evidence remains sparse after a favourable outcome. | EV, ST |
| [P-077](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Vincent Weaver vs Aryan Jit Singh — PREGAME FORECAST | Weaver won 2?0. Singh-correlated selections failed. Without point-level evidence, specific causal attribution remains uncertain. | EV, BR |
| [P-078](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? SK Brann (W) vs FK Austria Wien (W) — PREGAME FORECAST | Brann 2?1, HT 1?1, eight corners. Four rows won, some at tight boundaries. Shared event dependence remains. | AR, BR |
| [P-079](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Abha vs Al Khaleej Saihat — PREGAME | Abha 1?1; both goals in H1, seven corners. Over/X2 worked, outright winner did not. Draw endpoint must remain explicit. | AR, ST |
| [P-080](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Al Taawoun Buraidah vs Al Fayha — PREGAME | Taawoun 0?0; 15 corners, 26 shots, recorded xG 2.6. 1X worked, other directions failed. Chances are not goals; corners are separate. | EV, AR |
| [P-081](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Independiente del Valle vs Deportes Tolima — PREGAME | Independiente del Valle 3?1, HT 0?0, aggregate 4?1. Side/full Over worked; first-half Over/corners failed. Aggregate state changes exposure. | AR, EV |
| [P-082](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? CF Monterrey vs Chicago Fire FC — PREGAME | Monterrey 2?1, HT 1?0, nine corners. Early/full Overs worked; Chicago X2/winner failed. Winner is not implied by scoring. | BR |
| [P-083](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Cleveland Guardians at Los Angeles Angels, MLB regular season — PREGAME FORECAST | Cleveland 8?6 in ten; 6?6 regulation. Under 8 and Angels +1.5 lost. Separate pre-extras scoring miss from extra-inning increment. | AR, EV |
| [P-084](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Washington Mystics at Phoenix Mercury, WNBA regular season — PREGAME FORECAST | Washington beat Phoenix by ten. Winning Washington cushion does not by itself validate all rotation or scoring assumptions; keep phase-specific evidence. | EV, BR |
| [P-085](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Lobos Puebla vs Fuerza Regia, LNBP regular season — LIVE START-CROSSING FORECAST | Fuerza 91?90. Puebla +2.5 and Over 171.5 won despite an impossible recorded earlier score sequence. Input defect survives success. | ID, AR |
| [P-086](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Club León vs Real Salt Lake — Leagues Cup quarterfinal — START PASSED / LIVE STATE NOT VERIFIED | Recorded closure retains a state/research-source limitation. Do not reconstruct an exact missing corner field from the final event label. | ID, ST |
| [P-087](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? India vs Sri Lanka, 2nd Test, Day 4 — PRE-START DAY-4 LIVE-STATE RESEARCH CARD | India?Sri Lanka Test drew; Sri Lanka first innings 290. Under 286.5/winner failed. Same physical Test as P-114, different forecast state. | ID, AR |
| [P-088](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Howlers Sporting Singtam vs Sikkim Boys Football Club — SFA A Division S-League — PREGAME FORECAST | Sikkim Boys 8?3. Winner protection failed while goal rows worked; first-half timeline/count inconsistency requires source-level repair. | ID, AR |
| [P-089](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Hanshin Tigers @ Chunichi Dragons — PREGAME | Chunichi 4?0. Under 8 worked, Hanshin cushion failed. A suppressed total can accompany a shutout margin. | BR |
| [P-090](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Hokkaido Nippon-Ham Fighters @ Saitama Seibu Lions — PREGAME | Fighters 9?1. Seibu +1.5 and Under 7.5 lost. Adverse starter/offence branch was not adequately reflected in the order. | EV, BR |
| [P-091](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Tohoku Rakuten Golden Eagles @ Orix Buffaloes — PREGAME | Orix 7?5. Orix +1.5 won; Under 8.5 lost. Comeback and relief sequence require score-state exposure, not generic bullpen labels. | EV, BR |
| [P-092](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Doosan Bears @ KT Wiz — PREGAME | KT 5?4. Four winning rows contain overlapping cushions. Count rows correctly without treating their wins as independent evidence. | AR, BR |
| [P-093](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? NC Dinos @ LG Twins, KBO regular season — PREGAME FORECAST | LG 8?0. LG cushion won, NC cushion lost; both Over 7.5 and Under 9.5 won. Distinct thresholds create an overlap band. | AR |
| [P-094](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Yorkshire Women vs Surrey Women, Metro Bank One Day Cup Women — TOSS COMPLETE / PRE-FIRST-BALL FORECAST | Surrey 172/8, Yorkshire 171; Yorkshire 34/0 after five. Phase Over 19.5 won, full Over 225.5 lost. Five-over and innings targets differ. | AR, EV |
| [P-095](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? TSG Hawks @ Fubon Guardians, CPBL regular season — PREGAME FORECAST | Fubon 5?4. Over 6.5 won despite wrong starter identification. Winning result cannot certify source accuracy. | ID, EV |
| [P-096](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Rakuten Monkeys @ CTBC Brothers, CPBL regular season — PREGAME FORECAST | CTBC 2?0. Rakuten winner failed; both starters threw seven scoreless. Rookie/returning-pitcher upside and late relief decide allocation. | EV, BR |
| [P-097](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Wei-Chuan Dragons @ Uni-President 7-ELEVEn Lions, CPBL regular season — PREGAME FORECAST | Uni 1?0. Under 7.5/winner worked. Preserve narrow suppression mechanism without extrapolating an automatic Under rule. | EV, BR |
| [P-098](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Vietnam vs Thailand, ASEAN Hyundai Cup 2026 Final Leg 2 — PRE-KICKOFF-DATA VIEW | Vietnam 2?2, aggregate 4?2. Under 2.5 lost while Thai corner/first-half rows worked. Aggregate protection and corner processes differ. | AR, EV |
| [P-099](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Rotterdam Dockers vs Amsterdam Flames, European T20 Premier League 2026 — TOSS COMPLETE / PRE-FIRST-BALL VIEW | Rotterdam 158/5 beat Amsterdam 157/8; Amsterdam PP 56/2. Full Under won, PP Under 40.5 lost. This is omitted from the newest 'only prior' baseline. | ID, AR, EV |
| [P-100](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Apollon Limassol Women vs FH Hafnarfjordur Women, UEFA Women's Europa Cup 2026/27 — PREGAME FORECAST | FH 2?0 Apollon, two goals before half. Apollon +0.5 failed; H1 Over won; full Over failed. Keep phase and team allocation separate. | AR, BR |

### P-101?P-200

| Record / event | Recorded outcome and observation | Rules |
|---|---|---|
| [P-101](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Germany Women vs Türkiye Women, international friendly — PREGAME FORECAST | Turkey 63?62. Under 131.5 won, Germany -2.5 lost after a 40?30 halftime lead; second-half allocation needs its own evidence. | EV, BR |
| [P-102](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? VfL Wolfsburg Women vs Inter Women, UEFA Women's Champions League 2026/27 — PREGAME FORECAST | Wolfsburg 2?0, HT 1?0. Winner/H1 Over won, full Over lost; corner race unresolved. Separate field sourceability. | AR, ST |
| [P-103](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Tampa Bay Rays at Detroit Tigers | Tampa Bay 3?0. Detroit winner lost, Under 7.5 won. Starter underlying evidence and winner allocation diverged. | EV, BR |
| [P-104](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Ajax Women vs Real Madrid Women — UEFA Women's Champions League third qualifying round, first leg — PREGAME | Madrid 2?0. X2/H1 Over/Under 2.5 won; corners unresolved. Final score does not settle a missing statistic. | ST |
| [P-105](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Al Ahli Saudi FC vs Auckland FC — FIFA Intercontinental Cup 2026, African-Asian-Pacific Cup Playoff — PREGAME | Al Ahli 1?0, goal 63. Winner won, H1/full Overs lost; corners unresolved. Dominance need not produce early/multiple goals. | EV, ST |
| [P-106](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Newcastle United vs West Bromwich Albion — Carabao Cup Second Round — PREGAME | Newcastle 3?2. All four rows won, through dependent scoring paths; one card cannot certify confidence calibration. | BR |
| [P-107](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Bradford City vs Burnley — Carabao Cup Round 2 — PREGAME | Bradford 0?0 Burnley, Bradford won penalties; 19 corners. Protected/Under/corner rows won; H1 Over/regulation winner failed. | AR, ST |
| [P-108](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Tottenham Hotspur vs Charlton Athletic — Carabao Cup Round 2 — PREGAME | Tottenham 5?1, two H1 goals, 17 corners. All four rows won; check pre-issue rotation evidence independently of outcome. | EV, BR |
| [P-109](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Chicago Cubs @ Arizona Diamondbacks — MLB regular season — PREGAME | Arizona 2?0. Arizona +1.5/Under 8.5 won; Cubs +1.5 lost. Suppression need not preserve opposing cushions. | BR |
| [P-110](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Kei Nishikori vs Michael Antonius — US Open Men's Qualifying Q2 — DELAYED / NOT STARTED | Nishikori 6?4, 6?4. Winner/set cushion won; opposing set cushion/Over 20.5 lost. Sets and games require separate arithmetic. | AR |
| [P-111](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Boston Red Sox @ Miami Marlins — MLB regular season — PREGAME | Miami 4?0. Boston winner lost; Under 7.5 won. Current pitcher improvement should survive reputation-based priors. | EV, BR |
| [P-112](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Minnesota Twins @ Athletics — MLB regular season — PREGAME | Athletics 7?4. Athletics +1.5 won; Under 10.5 lost. Relief outcome differed from starter rationale; audit successful row too. | EV, BR |
| [P-113](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Club América vs Columbus Crew — Leagues Cup 2026 Quarterfinal | Am?rica 2?0, both goals H1, corners 2?10. 1X/H1 Over won, full Over lost. Goals and corner territory decoupled. | EV, AR |
| [P-114](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? India vs Sri Lanka, 2nd Test, Day 5 — PRE-DAY-5 LIVE-STATE FORECAST | Sri Lanka 429/9; Test drawn. Under 291.5/India winner failed. Tail resistance matters; same physical event as P-087. | ID, EV |
| [P-115](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Belfast Wolves vs Dublin Guardians, European T20 Premier League 2026 — START-CROSSED / NOT STARTED | Belfast 184/7, Dublin 132/9; PP 52/3. Under 171.5/PP Under 47.5 lost. Wickets do not ensure low phase scoring. | AR, EV |
| [P-116](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Brisbane Broncos vs Melbourne Storm — PREGAME | Storm 46?20, HT 30?10. Under 50.5/Broncos +4.5 lost. Defensive failure tail affects total and margin together. | EV, BR |
| [P-117](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? ISI Dangkor Senchey FC vs Life FC Sihanoukville — PREGAME | Life 2?1 ISI, HT 0?1. H1 Over won; Under 2.5/ISI 1X failed; corners unresolved. Phase success is not final control. | AR, ST |
| [P-118](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Sandro Kopp vs Martin Krumich — PREGAME | Kopp 6?2, 6?4. Krumich set +1.5 failed; wrong surface undermines the reference population before ranking. | ID, EV |
| [P-119](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Noah Karma vs Alessandro Hunziker — PREGAME | Karma 6?3, 5?7, 6?2. Four wins share one three-set path; not four independent validations. | AR, BR |
| [P-120](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Guinea vs South Sudan — PREGAME | South Sudan 81?71. Guinea +11.5/Under 159.5 won. Cushion success need not imply outright winner success. | AR, BR |
| [P-121](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Sardarapat FC vs FC Syunik — Armenian Cup | Sardar 1?1 Syunik, Syunik won penalties. H1 Over/1X won, full Over/regulation winner failed; corners unresolved. | AR, ST |
| [P-122](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Bahrain vs Oman — PREGAME | Bahrain 106?62. Oman +42.5/Under 156.5 failed. One team can carry both a large margin and aggregate Over. | EV, BR |
| [P-123](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? BuxDU vs Metallurg Bekabad — SCHEDULE-CONFLICT / NO VERIFIED LIVE SCORE | Metallurg 4?0. X2/H1/full Overs won; corners unresolved. Official zero-filled shells are not verified zero statistics. | ID, ST |
| [P-124](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Chase Ferguson vs Fumin Jiang — M15 Maanshan 8 Quarterfinal | Ferguson 5?7, 6?4, 6?3. Winner/cushion won; first-set/straight-set calls lost. Match and trajectory differ. | AR |
| [P-125](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Canberra Brave vs Sydney Bears — 2026 AIHL Goodall Cup Preliminary Final | Canberra 4?3 Sydney, shots 41?29. Sydney +1.5 won, Over 8.5 lost. Goalie/finishing quality mediates shot volume. | EV, BR |
| [P-126](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Sikkim Aakraman FC vs Sikkim Boys Club — SFA A Division S-League | No reliable final reconstructed: event identity, score/phase and corners conflict. Do not attach a similarly named team's result. | ID, ST |
| [P-127](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Iran vs New Zealand — FIBA Basketball World Cup 2027 Asian Qualifiers | New Zealand 93?91 after 80?80 regulation. Iran +7.5 won; Under 158.5 already lost before OT. Do not blame overtime alone. | AR, ST |
| [P-128](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Auckland vs Bay of Plenty — Hilux NPC Round 5 | Bay of Plenty 22?19. Over 60 lost, Auckland +4.5 won. Four-game frequency needs comparable-population uncertainty. | EV, BR |
| [P-129](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Manly Warringah Sea Eagles vs St George Illawarra Dragons — NRL Round 26 | Manly 44?10. Manly +10.5 won, Under 50.5 lost. One-sided scoring can carry an Over despite opponent suppression. | EV, BR |
| [P-130](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Beitar Haifa Yakov vs Hapoel Bnei Arrara Ara — Israel State Cup 2026/27 | Beitar 1?1 regulation, 3?1 after extra time. Protected/early rows won, regulation Over failed. Advancement is not regulation victory. | AR, ST |
| [P-131](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Penrith Panthers vs Canterbury-Bankstown Bulldogs — NRL Round 26 | Penrith 24?10. Bulldogs +9.5 lost, Under 40.5 won. Low total did not imply a within-line margin. | BR |
| [P-132](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? RC Vannes Sevens vs LOU Rugby Sevens — In Extenso SuperSevens, Pau | Vannes 17?10. Under 35.5/Lyon +9.5 won. A counterexample to blanket sevens-Under demotion; no policy follows from one game. | AR, BR |
| [P-133](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Arthur Géa vs Nishesh Basavareddy — US Open 2026 Men's Qualifying Final | Basilashvili 6?3, 6?1. Gea -2.5/Over 22.5 lost. Gea-control-only score tree omitted the dominant alternative. | EV, AR |
| [P-134](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Cape Verde vs Guinea — FIBA Basketball World Cup 2027 African Qualifiers | Guinea 81?61. Cape Verde +10.5 lost, Under 150.5 won. Tavares absence affects scoring/rebounding exposure specifically. | EV, BR |
| [P-135](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Unión de Santa Fe vs Sarmiento — Torneo Clausura 2026 | Uni?n 4?1, HT 1?0. Sarmiento team Over/H1/full Overs won; Sarmiento X2 lost; corners unresolved. | AR, ST |
| [P-136](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? James Duckworth vs Arthur Fery — ATP Winston-Salem Open 2026 Semifinal | Fery advanced after Duckworth retirement. Four game-total/handicap rows unresolved on retirement terms; not normal completed-match settlement. | AR, ST |
| [P-137](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Los Angeles Dodgers (Tarik Skubal) @ Detroit Tigers (Drew Anderson) — MLB | Dodgers 2?1. Detroit +2.5 and lower total direction worked. Cushion geometry can survive an outright-winner miss. | BR |
| [P-138](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Miami Marlins (Eury Pérez) @ Washington Nationals (Jackson Kent) — MLB | Washington 9?2. Miami winner/Under 8.5 lost. Material adverse evidence needs a checkable effect on assumptions. | EV, BR |
| [P-139](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Falcons @ Dolphins preseason | Atlanta 17?12. Under 36.5 won, Falcons -5.5 lost. Preseason rep plans and canonical identity outrank franchise-strength shorthand. | ID, EV |
| [P-140](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Astros @ Mets | Houston 3?1. Houston +1.5/Under worked; opposing cushion/Over failed. Keep margin and total separate. | AR, BR |
| [P-141](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Red Sox @ Yankees | Yankees 1?0. Boston +1.5/Yankees winner/Under won. Cushion selection and winner can legitimately differ. | BR |
| [P-142](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Rockies @ Braves | Atlanta 6?4. Atlanta winner/Colorado +2.5/Over 9 won; Under lost. Overlapping side rows are dependent. | AR, BR |
| [P-143](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Giants @ Jets preseason | Giants 23?6. Under 37 won, Jets +6 lost. Low-scoring preseason does not imply low separation. | EV, BR |
| [P-144](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Buccaneers @ Jaguars preseason | Jacksonville 19?0. Tampa -2.5/Over 35.5 lost. Quarterback, line and defensive rep plans all matter. | EV, BR |
| [P-145](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Rangers @ Brewers | Milwaukee 6?1. Texas +1.5/Over 7.5 lost. Side suppression and scoring ceiling invalidate distinct assumptions. | EV, BR |
| [P-146](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Sun @ Fever | Indiana 111?91. Indiana -17.5/Over 177.5 won. Component scoring explains the pair; no universal favourite/Over coupling. | EV, BR |
| [P-147](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Gotham v Portland | Gotham 1?1, HT 0?0, corners 4?3. H1 Over/Gotham corner Over 4.5/full Over failed. Different scoring/territorial processes. | EV, AR |
| [P-148](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Toluca Femenil v León Femenil | Toluca Femenil 1?0, goal 76. H1/full Overs failed; corners provisional. Late winner does not validate early scoring. | AR, ST |
| [P-149](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Colorado Rapids 2 v Ventura County | Ventura 3?2, HT 1?1. Early/full Overs worked; corner win provisional. Keep statistic confidence separate from score confidence. | ID, ST |
| [P-150](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Montreal @ Winnipeg, CFL | Winnipeg 44?28. Montreal -6.5/Under 60.5 lost. Adverse personnel/state branch mattered to both top assumptions. | EV, BR |
| [P-151](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Boca Juniors v Lanús | Boca 1?0 at 90+3, HT 0?0; corners 11?3 now confirmed. Recoverable corners; late goal is not first-half evidence. | ID, AR |
| [P-152](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Atlante v León | Atlante 1?1, HT 0?0, corners 3?3. Early/corner/full Over directions failed. Named low-event path needed actual influence. | EV, BR |
| [P-153](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Necaxa v Cruz Azul | Cruz Azul 3?1, HT 0?1, corners 7?7. Goal/corner directions won through one shared event state. | EV, BR |
| [P-154](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Vikings @ Broncos preseason | Denver 34?6. Under 37.5 lost. Backup offence can score against backup defence; analyze both units. | EV, BR |
| [P-155](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Phillies @ Angels | Philadelphia 5?3. Philadelphia +1.5/Over 7.5 won with grand-slam contribution. Tail-event success is not centre accuracy. | EV, BR |
| [P-156](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Orioles @ Athletics | Baltimore 4?3. Athletics +1.5/Under 9.5/Baltimore winner won. Valid narrow-loss cushion and opposing winner coexistence. | BR |
| [P-157](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Sacramento @ Reno | Reno 6?1. Nothing issued to grade; retain administrative closure. | ID, ST |
| [P-158](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Tempo @ Aces | Las Vegas 93?73. Under 174.5 won, Toronto +14.5 lost. Suppressed total and large favourite margin coexist. | BR |
| [P-159](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Mystics @ Sparks | Los Angeles 88?82. Washington -4.5 lost after reversal. Known back-to-back/late-exposure risks need more than acknowledgment. | EV, BR |
| [P-160](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Diamondbacks @ Giants | Arizona 10?6. Arizona side worked; opposing cushion/Under 8 failed. Separate starter, home-run and relief attribution. | EV, BR |
| [P-161](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Sultanes @ Toros | Toros 2?0. Sultanes +1.5 lost; Under/Toros winner worked. Two-run shutout defeats a standard cushion. | BR |
| [P-162](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Te v Ferguson | Te 6?1, 6?4. Te -2.5/Under 22.5 won; later ITF confirmation resolves evidence, not a new prediction. | ID, ST |
| [P-163](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Adelaide v West Coast AFLW | Adelaide 60?43. West Coast +21.5 won, Under 93.5 lost. Conversion and scoring opportunity need sport-native units. | AR, EV |
| [P-164](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Lotte @ Nippon-Ham, live | Fighters 9?7. Fighters +1.5 won; Lotte +1.5/Under 8.5 lost. Opposing cushions are not exhaustive at this margin. | AR, BR |
| [P-165](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Tohoku Rakuten Golden Eagles @ Saitama Seibu Lions — NPB Pacific League | Seibu 1?0. Suppression/side worked; final score alone does not independently identify the pitching mechanism. | EV, BR |
| [P-166](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Melbourne Mustangs vs Canberra Brave — AIHL Goodall Cup Semifinal | Canberra 5?4 after overtime. Cushion research grade and operator OT/action terms must remain separate. | AR, ST |
| [P-167](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Kiwoom Heroes @ Doosan Bears — KBO | Doosan 7?2. Side worked with relief separation material. Use pitcher role/exposure, not bullpen average alone. | EV, BR |
| [P-168](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? LG Twins @ Lotte Giants — KBO | LG 8?3 in seven, rain termination. Under 10.5 crossed before stoppage; still distinguish research arithmetic from action terms. | AR, ST |
| [P-169](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Melbourne vs Carlton — AFL Wildcard Final | Carlton 74?55, total 129. Broad Under/side worked. Winning endpoints do not certify every component centre. | EV, BR |
| [P-170](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? North Queensland Cowboys vs Wests Tigers — NRL | Cowboys 24?10, second half 16?0. Under/favourite cover worked. Half-specific allocation matters to the path. | EV, BR |
| [P-171](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Glasgow Cosmic vs Dublin Guardians — European T20 Premier League | Glasgow 183/5, Dublin 150; PP 44/2. Phase Under worked, full Under failed; earlier observation omitted from new cricket baseline. | ID, AR |
| [P-172](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Liverpool vs Nottingham Forest — English Premier League | Liverpool 2?2, corners 5?3. Early scoring worked. Low possession is not low event production. | EV, BR |
| [P-173](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Chengdu Rongcheng vs Liaoning Tieren (Ironman) — Chinese Super League | Chengdu 2?1, corners 7?6. Side/goal worked; corner tail failed. Keep territorial sequence model distinct. | EV, AR |
| [P-174](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Henan vs Chongqing Tonglianglong — Chinese Super League | Henan 1?1, corners 6?3. Top missed; bench/substitution exposure was required before September 6. | EV, BR |
| [P-175](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? South Africa vs Zimbabwe — Namibia T20I Tri-Series | South Africa 146/3, Zimbabwe 144/8; PP 54. Fast phase/low full innings coexist via resources and target. | AR, EV |
| [P-176](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Amiens SC vs FC Versailles — France Ligue 3 | Amiens 3?0, eight corners provisionally. Top goal read missed; corner win retains evidence qualification. | ID, ST |
| [P-177](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? SC Aubagne Air Bel vs Bourg-en-Bresse Péronnas — France Ligue 3 | Aubagne 2?0, corners 3?4. Team allocation missed while suppression worked. Winner and total need separate support. | BR |
| [P-178](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? AS Cannes vs Le Puy-en-Velay — France Ligue 3 | Cannes 2?0. Winner/BTTS/Under worked; corners unknown. Never infer the missing statistic from goals. | ID, ST |
| [P-179](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Thionville Lusitanos vs Paris 13 Atletico — France Ligue 3 | Thionville 1?1, corners 8?1 provisionally. Winner missed on draw; corner direction provisionally won. | AR, ST |
| [P-180](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? 1. FC Köln vs TSG Hoffenheim — Germany Bundesliga | K?ln 3?2, two substitute goals. Bench exposure changed team allocation; this predates newest bench gate. | EV, BR |
| [P-181](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Coventry City vs Hull City — English Premier League | Hull 1?0, corners 6?2. Top side lost while suppression worked. Territory does not determine who converts. | EV, BR |
| [P-182](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Excelsior Rotterdam vs Sparta Rotterdam — Netherlands Eredivisie | Excelsior 2?1, corners 6?4. Five of five rows won on one event; preserve dependence and overlap. | AR, BR |
| [P-183](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Levante UD vs Real Betis — La Liga | Levante 5?2, corners 5?8. Top Under lost; tiny clean-sheet sample missed opponent/finishing tails. | EV, BR |
| [P-184](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? North Carolina vs TCU — NCAA Football | UNC 15?10. TCU top lost, Under won. Known uncertainty mattered; corrected penalty yards are 89, not 85. | ID, EV |
| [P-185](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Robert Morris @ Wagner — NCAA FCS / NEC | Robert Morris 28?7. Under/RMU cushion worked, winner prior failed. Stale official sources need date/role continuity checks. | ID, EV |
| [P-186](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Los Angeles Dodgers @ Detroit Tigers — MLB | Detroit 2?1 walk-off. Detroit cushion/Under worked, away winner failed. Termination affects total/run-line support. | AR, BR |
| [P-187](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Trinbago Knight Riders vs Jamaica Kingsmen — Republic Bank CPL 2026 | Jamaica won by seven under DLS; TKR 180/6, PP 60/0. Top Under failed, Overs worked. Separate phase and revised endpoint. | AR, EV |
| [P-188](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Boston Red Sox @ New York Yankees — MLB | Yankees 9?2, five runs in eighth. Opposing cushion failed. Relief availability is not score-state role/quality. | EV, BR |
| [P-189](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Alabama A&M Bulldogs vs Howard Bison — Cricket MEAC/SWAC Challenge | Howard 31?24. Alabama A&M top failed; late explosive play material. Rep/defensive uncertainty is not hindsight certainty. | EV, BR |
| [P-190](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? New Zealand Warriors (W) vs St George Illawarra Dragons (W) — NRLW Round 9 | Dragons 22?18. Under 47.5/Dragons +15.5 won; Warriors winner failed. Cushion success does not rescue winner inference. | BR |
| [P-191](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Walyalup (Fremantle W) vs Carlton W — AFLW Round 3 | Carlton 48?42. Top margin failed. Wind-end allocation requires phase-specific opportunity modeling. | EV, AR |
| [P-192](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? SSG Landers @ KIA Tigers — KBO | Rainout. No action to grade; no hypothetical predictive win. | ID, ST |
| [P-193](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Essendon (W) vs Richmond (W) — AFLW Round 3 | Richmond 38?33. Essendon +2.5 failed, Under 83.5 won. Low total does not mean close enough margin. | BR |
| [P-194](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? FC St. Pauli vs 1. FC Kaiserslautern — Germany 2. Bundesliga | Kaiserslautern 2?1, HT 0?1, corners 5?4. Top Under failed; half state/finishing changed aggregate. | EV, BR |
| [P-195](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? KAA Gent vs Club Brugge — Belgium First Division A | Gent 2?1, HT 1?1, corners 1?5. Early top worked; side/corner assumptions failed. Goals and territory decoupled. | EV, AR |
| [P-196](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Egypt vs Congo DR — FIBA Basketball World Cup 2027 African Qualifiers | Congo 77?75. Egypt -14.5/Under 151.5 lost; latter by 0.5. Margin and boundary-total misses need separate diagnoses. | AR, BR |
| [P-197](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Feyenoord vs ADO Den Haag — Netherlands Eredivisie | Feyenoord 2?2, HT 0?1, corners 11?3. Early top worked; corner Under failed. Trailing pressure can raise corners. | EV, AR |
| [P-198](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Poland vs Germany — FIBA Basketball World Cup 2027 European Qualifiers | Germany 96?94 after 83?83 regulation. Poland +8.5 won; Over 180.5 depended on OT. Freeze scope before grading. | AR, ST |
| [P-199](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Frederikshavn White Hawks vs Sønderjyske — Danish Metal Ligaen | Frederikshavn 7?3. Top Under failed with unconfirmed goalie. Missing status raises uncertainty, not an automatic Over. | ID, EV |
| [P-200](GAME_LOG_LEDGER_2026-09-06.md#full-list-in-id-order) ? Herning Blue Fox vs Rungsted Seier Capital — Danish Metal Ligaen | Herning 4?3 after 3?3 regulation. -2.5 failed; operator OT/action scope remains conditional. | AR, ST |

<!-- GAME_APPENDIX_C -->

## 8. Calculation and preservation notes

The corrected totals count each preserved ranked total selection once in its latest recorded final state. Corners are excluded from the O/U diagnostic because that diagnostic concerns goal/point/run/game scoring totals. The paired ranking table includes only cards with both original ranks recoverable. Conditions are checked against the recorded event state; P-305's batting-first condition was met. Unknown lower rows are not imputed from a typical four- or five-row template.

No original file was edited. Only this separate Markdown report was created. A content-hash check of the existing source-text corpus before and after report generation is recorded in the delivery verification.
