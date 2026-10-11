# PROMPT 1 — Research and append one individual game card

**Mode:** LOCAL_MINI_STAGING. **Writes:** the named active local mini only, including its evidence appendix and mutable footer. **GitHub/canonical writes:** none. Do not settle, retrospect, change rules or allocate canonical status.

Inputs: `Event: <participants, league/format, date/time/timezone or official event link>`; `Active mini: <path>`; `Supplied contracts: <exact text/lines, or none>`; `Specific research constraints: <if any>`. Treat estimated starts as estimates until verified. Locate accessible inputs first; ask only for information essential to resolve ambiguity. This is the complete game prompt; nothing from prompt 2 needs to be pasted with it.

## 1. Read and establish authority

Print the [reading receipt](README.md) after opening CURRENT_STATE, METHOD, CURRENT_RULES, SELECTION_RULES, CARD_AND_LOG_TEMPLATES, this prompt, the complete active mini, GAME_LOG_STATUS_CURRENT and relevant canonical event records. Read applicable sport/league rules below, ARCHIVE_USE_GUIDE, current SOURCES routes/freshness rules, and relevant probability/profile/base-rate sections. Record actual HEAD, working differences and time. Apply current controls over historical sport-engine notes.

If a required control or original mini is inaccessible, deliver a clearly labelled draft, not an issued append. Missing sporting data leads to explicit uncertainty or qualitative/NO_FORECAST research, not invented numbers.

## 2. Identity, duplicate and timing gate

Verify participants, competition, season, stage, venue, native ID/game number, official scheduled start, venue zone, UTC and Australia/Sydney time. Search every relevant local mini/carryover and canonical log body/status by ID, event key and aliases; doubleheaders and postponements need explicit identity handling. An existing event gets a dated addendum under its original ID, no new card.

For a new event, reconcile the mini's next working ID with current canonical state and outstanding local sequence. No gap, reservation, collision or renumbering. Record current source state before research and again immediately before write. Keep cutoff, research completion, actual issue and state-recheck times separate. If start is crossed, relabel honestly; exposure to live/final information prevents a clean pregame reconstruction. Retain requested late research in its separate cohort.

## 3. Evidence and archive

Follow official field-owner → structured provider → quality corroboration routes. For each decisive claim retain URL, exact field/value or brief extract, source publication/update time when known, retrieval time and provenance/lineage. Log inaccessible/stale/conflicting sources. Three domains are not three independent collectors. No odds/tips/previews/fantasy inputs.

Verify lineups/starters/goalies/QB/XI as relevant; probable is not confirmed. Distinguish fact, historical estimate and analyst assumption. Inspect actual archive contents and print files, logical rows read, season/endpoint filters, latest usable date and missingness. Use only results known before cutoff; a date alone does not prove a same-day game had finished. Do not use postgame narrative or full-season aggregates from after cutoff. A profile older than one season triggers STALE_PROFILE, a current-source check and sensitivity; missing replacement data does not justify a fabricated refresh.

## 4. Distribution, expected score and comparator

Build the simplest defensible coherent sport/endpoint distribution you can actually calculate. Print every parameter and its basis, formula/table, normalization, tail treatment, covariance and endpoint transitions. A named family is not evidence that a grid or exact simulation was computed. If the required calculation cannot be done, report a supported approximation with limitations, or qualitative research with NOT_ESTIMATED probabilities.

Produce expected score terms from CARD_AND_LOG_TEMPLATES §3a, including team/total/signed-margin means and supported SDs. Keep zeros; mark missing or irrelevant terms. Print all winner/draw/tie masses. For every candidate retain unconditional W/P/L/V and p_card=W/(W+L), with denominator and action convention.

Attempt BASELINE_LEAGUE_V1 on the same line/endpoint from league-only inputs, frozen before issue. Print recipe, source cohort/n/cutoff and parameters separately from the team model. No 0.5 placeholder or retrospective baseline fill. Missing baseline does not stop the card; it limits later skill measurement.

Show an adjustment table, unadjusted distribution/pair and low/base/high sensitivity on material uncertain inputs. Any adjustment-driven pair change is ADJUSTMENT_DEPENDENT, even below 0.25 SD. Report plausible probability ranges as sensitivity, not confidence intervals. Do not move individual probabilities outside the shared model.

## 5. Candidate selection and dependence

Freeze the supported family/line-generation recipe before pricing. Price supplied rows and the declared derived universe; retain exclusions and unused supplied rows. Do not move thresholds repeatedly toward 90% to manufacture a strong gate. Values above the selection ceiling keep their true probabilities in the diagnostic appendix and are excluded, never capped.

Apply family eligibility and deterministic decreasing-p primary order from SELECTION_RULES. Show up to four supported rows, the first two as PICK. Fewer rows or qualitative/NO_FORECAST output is acceptable with the reason; unsupported rows are never padding. The best non-complementary gate alternative comes from the entire declared eligible universe, not a pruned four. Print original gate and RET03 shadow separately.

Freeze RET04 different-quantity and XCARD6 minimum-joint-failure shadow Rank 2 where calculable. Neither changes primary ordering. Print exact unconditional joint loss from common states, or honest Fréchet bounds. Label disjoint losing sets MECHANICALLY_PROTECTED; do not claim they improve skill or guarantee profit. Report both-decisive conditioning where pushes/voids exist.

## 6. Sport research blocks — apply the matching one

**Baseball:** Read RULES_BASEBALL, league conditions and the baseball profile/toolkit sections. Verify starter identity and expected workload, lineup/platoon, bullpen availability, opponent-adjusted offence, park, weather and rest. Use supported overdispersed team-run scenarios with shared environment, starter/bullpen segments and correct home last-inning/extras handling. Verify season-specific tie/innings rules; do not assume MLB rules in KBO/NPB. +1.5 needs team-directional win and exactly-one-run-loss mass, with tie/action treatment. A league absolute one-run share is not the selected team's probability. Unknown pitcher weights stay assumptions, not facts.

**Cricket:** Read RULES_CRICKET and LEAGUE_RULES_CRICKET. Confirm exact format/playing conditions, XI, toss, batting order, bowling allocations, pitch/weather/dew and rain resources. Model innings/phase/wicket dependence with explicit toss/rain branches. A chase ends on the winning delivery and can legally overshoot the target; do not simply cap every total at the target. Tests retain draw/weather branches; tie, super-over, DLS and no-result conventions must match each row. Unsupported ball-by-ball calculation is not an exact simulation.

**Basketball:** Read RULES_BASKETBALL and the correct league/era profile. Confirm rotation, minutes, injuries, rest/travel, pace, offensive/defensive efficiency, shot mix, rebounding, turnovers and free throws. Print possessions × efficiency centres, team covariance, total/margin widths and OT treatment. A raw scoring average is a labelled approximation, not a fitted pace model. No NBA defaults for NBL/B.LEAGUE/European leagues. Stale NBL profiles require disclosure/current evidence, not a +16.8 adjustment copied from three retrospective games.

**Ice hockey:** Read RULES_ICE_HOCKEY; RULES_NHL only when applicable. Confirm goalies or supported mixture, lines/scratches, 5v5 creation/suppression, special teams, rest and travel. Separate regulation draw from full-game OT/SO and final-score convention; empty-net tails must be explicit. Print directional handicap mass, not unconditional league absolute-margin frequency. Unconfirmed goalie sensitivity must reach totals/ranks. Other leagues require their own rules/profile.

**Tennis:** Read RULES_TENNIS; inspect current tennis archive/provider coverage rather than assuming it is empty. Verify event/player identity, round, tour, surface, best-of format, tiebreak rules, fitness, workload, serve/return data and appropriate benchmark. Games/sets/winner come from compatible point-to-match construction with a supported form mixture; show calculation or label the approximation. Compare deciding-set mass with relevant tour/surface/format data, never force a global reference rate. Freeze retirement/walkover rules per row; sporting advance and operator settlement are different.

**Soccer:** Read RULES_SOCCER and LEAGUE_RULES_SOCCER. Confirm XI/keeper, injuries, rotation, opponent-adjusted xG/shot process, set pieces, schedule, weather and competition incentives. Use a coherent regulation score model with explicit draw, supported half split for phase rows and appropriate low-score correction. Goal counts do not generate corner probabilities; corners need their own supported count/provider model and joint dependence if combined. ET/penalties only where specified. Check first-half and team-to-score assumptions against confirmed availability; no EPL constants silently transferred to another league.

**Rugby league / union:** Read RULES_NRL_RUGBY or RULES_RUGBY_UNION and exact competition conditions. Verify team/bench/spine or halves/front row, kicking, possession/territory, discipline, workload and weather. Model the appropriate score events and key margins; league and union scoring systems differ. Use only applicable measured regime effects; finals need not always reduce the mean. Resolve draw/golden point/extra time per competition and endpoint.

**AFL / AFLW:** Read RULES_AFL and correct league/season profile. Verify teams, ruck/midfield, clearances, inside-50/scoring-shot creation, conversion, defence, rest/venue/weather. Separate shots from accuracy; points=6×goals+behinds. Use competition-specific pace/length and draw/finals rules. Explain shrinkage of unusual conversion rather than assuming a rebound.

**American football:** Read RULES_AMERICAN_FOOTBALL and exact NFL/college/other rules. Verify QB, line/skill/defensive availability, efficiency, drive/play pace, pressure, special teams, rest/weather. Use supported discrete score/drive structure or disclose an approximation; show push/key-margin mass near 3/7 and other relevant numbers. NFL and college overtime/tie rules differ. No claim to an exact drive model without its calculation.

**Other sport:** Read its actual rules and supported source/model route. If unavailable, retain qualitative/NO_FORECAST research rather than borrowing a model whose endpoint does not fit.

## 7. Write, audit and return

Use CARD_AND_LOG_TEMPLATES §3 in the mini's own format; v10 uses mini-log-6. Keep the decision block concise and put full evidence/arithmetic in A1–A9. State exact settlement fields, definitions and capture plan. Write one card before the footer, update only the footer's new-card/ID totals, and read it back. Audit C1–C16 with specific evidence. Preserve every earlier issued block.

For a duplicate or late-news correction, append a dated addendum; reforecast is NOT_PRIMARY and never changes the original grade. If writing is unavailable, return the complete updated mini as READ_ONLY_DRAFT / NOT_ISSUED and do not claim allocation.

Return the full new card, exact file path, working ID/status, timing and lead band, top two or no-forecast reason, baseline coverage, gate/joint/sensitivity summary, audit evidence and updated footer. Explicitly state settlement NOT_PERFORMED and GitHub writes NO. Do not promise prediction success.
