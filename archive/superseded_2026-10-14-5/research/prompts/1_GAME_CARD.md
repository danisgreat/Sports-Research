# PROMPT 1 — Research and append one individual game card

**Mode:** LOCAL_MINI_STAGING. **Writes:** the named active local mini only, including its evidence appendix and mutable footer. **GitHub repository (`main` branch):** read-only mode (no canonical or remote writes). Authority mode `PUBLISHED_MAIN_PINNED` (CURRENT_RULES §0) unless the user runs this inside the repository and asks for local controls (`LOCAL_WORKING_TREE`). Print the mode, the full SHA and any difference between published and local controls. Do not settle, retrospect, change rules or allocate canonical status. Prompt suite P-2026.10.14-v11.2, mini-log-7.

Inputs: `Event: <participants, league/format, date/time/timezone or official event link>`; `Active mini: <path>`; `Supplied contracts: <exact text/lines, or none>`; `Specific research constraints: <if any>`. Treat estimated starts as estimates until verified. Locate accessible inputs first; ask only for information essential to resolve ambiguity. This is the complete game prompt; nothing from prompt 2 needs to be pasted with it. Apply the matching sport section (1–7) below.

BASKETBALL
----------------------------

## 1. Read and establish authority

Read every control from one pinned commit of the GitHub repository (`main` branch) in read-only mode (`PUBLISHED_MAIN_PINNED`), or from the local working tree only in a `LOCAL_WORKING_TREE` run (CURRENT_RULES §0). Never mix the two. Print the [reading receipt](README.md) after opening CURRENT_STATE, METHOD, CURRENT_RULES, SELECTION_RULES, CARD_AND_LOG_TEMPLATES, RULES_BASKETBALL, LEAGUE_PROFILES (Basketball row for the league/era), ARCHIVE_USE_GUIDE (§8 defects), [SOURCES §3.2](../../SOURCES.md#32-basketball--nba-wnba-nbl-euroleague-acb-fiba-lkl-and-others) (basketball routes) and [§3.13](../../SOURCES.md#313-game-level-detail-results-line-ups-coaches-and-officials-tested-2026-09-30) (game-level detail), BASE_RATES_REGISTER (§3, §7.1), this prompt, the complete active mini, GAME_LOG_STATUS_CURRENT and relevant canonical event records. Record actual HEAD on `main`, working differences and time. Apply current controls over historical sport-engine notes.

If a required control or original mini is inaccessible, deliver a clearly labelled draft, not an issued append. Missing sporting data leads to explicit uncertainty or qualitative/NO_FORECAST research, not invented numbers.

## 2. Identity, duplicate and timing gate

Verify participants, competition/league (NBA, WNBA, NBL, B.League, ACB, EuroLeague, FIBA, etc.), season, stage, venue, native ID/game number, official scheduled start, venue zone, UTC and Australia/Sydney time. Search every relevant local mini/carryover and canonical log body/status by ID, event key and aliases; doubleheaders and postponements need explicit identity handling. An existing event gets a dated addendum under its original ID, no new card.

For a new event, reconcile the mini's next working ID with current canonical state and outstanding local sequence. No gap, reservation, collision or renumbering. Record current source state before research and again immediately before write. Keep cutoff, research completion, actual issue and state-recheck times separate. If start is crossed, relabel honestly; exposure to live/final information prevents a clean pregame reconstruction. Retain requested late research in its separate cohort. Log the request in the mini's intake table (template §2-D) whatever its outcome. Confirm you hold the mini's issuing-writer lease and that the mini is not frozen for settlement; otherwise route the event to the next authorised mini (CURRENT_RULES §8).

## 3. Evidence, roster and archive

**Availability research (AVAIL-2026.10.14-v1).** Read and apply [ROSTER_AVAILABILITY_PROTOCOL](../../ROSTER_AVAILABILITY_PROTOCOL.md) §§1–6 for both sides: exact starters/starting role, selected bench/replacements, current injuries/illness/suspensions/absences, and late changes. Complete its official match → both teams → eligibility/medical → permitted provider → local-language/obscure-competition escalation before reporting a missing field. Record actual searches, evidence/times and failures in the existing Evidence receipt/A3/A8; update the existing lineup-state metadata and audit C20. A roster, probable starter or predicted side is not confirmation. Recheck around the actual competition release window and immediately before freeze; re-price changed inputs. Never invent a healthy roster, bench or confirmation. If material gaps survive the full search, retain supported scenarios or qualitative/NO_FORECAST research with the exact reason. Do not read model-shadow or market material.

Follow official field-owner (league match centre / box score) → structured provider (RealGM, ESPN, etc.) → quality corroboration routes. For each decisive claim retain URL, exact field/value or brief extract, source publication/update time when known, retrieval time and provenance/lineage. Log inaccessible/stale/conflicting sources. Three domains are not three independent collectors. No odds/tips/previews/fantasy inputs.

Verify rotation, minutes, injuries, rest/travel, and especially **confirmed starting fives and active bench/reserve availability**; probable is not confirmed. Distinguish fact, historical estimate and analyst assumption. Inspect actual archive contents under `Previous Sports Results/Basketball/<league>/...` and print files, logical rows read, season/endpoint filters, latest usable date and missingness. Use only results known before cutoff; a date alone does not prove a same-day game had finished. Do not use postgame narrative or full-season aggregates from after cutoff. A profile older than one season triggers STALE_PROFILE, a current-source check and sensitivity; missing replacement data does not justify a fabricated refresh.

**Form windows and known-at (PR-01, R28).**
- Print each side's (team or player) L5, L10, L15, L20, season to date and league level, from dated games before the cutoff, with the true n of each window: CARD_AND_LOG_TEMPLATES §3b, ARCHIVE_USE_GUIDE recipe R2.
- Use the archive where it holds the games; otherwise use a SOURCES route (ESPN team schedule, MLB statsapi, StatMuse, Tennis Abstract) and say which.
- Exclude archive rows flagged as duplicates, awarded results, forfeits or abandonments.
- The windows overlap and count as one piece of evidence. Only the shrunk L20/season rate may move the centre, as a listed adjustment with the unadjusted pair; the four-window recency blend is printed beside it for comparison.
- A short-window swing is width, not a lean, unless a named, current mechanism explains it.
- Print the archive capture date. An input whose availability before the cutoff cannot be shown is `KNOWN_AT_UNVERIFIED` and may not decide Rank 1.

## 4. Distribution, expected score and comparator

Build the simplest defensible coherent basketball distribution you can actually calculate: calculate possessions × efficiency centres (ORtg/DRtg per 100 possessions), team covariance, total/margin normal or compound widths, and explicit overtime treatment (simulated Poisson OT scoring on regulation ties). Print every parameter and its basis, formula/table, normalization, tail treatment, covariance and endpoint transitions. A named family is not evidence that a grid or exact simulation was computed. If the required calculation cannot be done, report a supported approximation with limitations, or qualitative research with NOT_ESTIMATED probabilities.

Produce expected score terms from CARD_AND_LOG_TEMPLATES §3a: team points (means & SDs), total points (mean & SD), and signed margin (mean & SD). Keep zeros; mark missing or irrelevant terms. Print all winner/draw/tie masses. For every candidate retain unconditional W/P/L/V and p_card=W/(W+L), with denominator and action convention.

Attempt BASELINE_LEAGUE_V1 on the same line/endpoint from league-only inputs, frozen before issue. Print recipe, source cohort/n/cutoff and parameters separately from the team model. No 0.5 placeholder or retrospective baseline fill. Missing baseline does not stop the card; it limits later skill measurement.

Show an adjustment table (home venue, rest/travel, availability/minutes), unadjusted distribution/pair and low/base/high sensitivity on material uncertain inputs. Any adjustment-driven pair change is ADJUSTMENT_DEPENDENT, even below 0.25 SD. Report plausible probability ranges as sensitivity, not confidence intervals. Do not move individual probabilities outside the shared model.

**Pricing basis (PR-03).** When an input is labelled unfitted, stale, early-season or unconfirmed, the primary distribution is the declared mixture of its low/base/high cases (default weights 0.25/0.50/0.25, frozen before pricing). Print each row's `p_base` beside p_card. Compute at the precision actually used and print ε. A gate within ε of 0.62, or within 2ε of the 0.04 lead, is `GATE_UNRESOLVED_PRECISION`; rows within 2ε are a `PRECISION_TIE` (SELECTION_RULES §2). Apply any key-number, push or tie adjustment to the normalised common distribution, never to one row. Print each ranked row's line distance from centre (units and z, or N/A) and the card's baseline coverage, with an enumerated reason for each missing BASELINE_P (SELECTION_RULES §5, §9).

## 5. Candidate selection and dependence

Freeze the supported family/line-generation recipe before pricing (totals, team totals, spreads, cushions). Price supplied rows and the declared derived universe; retain exclusions and unused supplied rows. Do not move thresholds repeatedly toward 90% to manufacture a strong gate. Values above the selection ceiling keep their true probabilities in the diagnostic appendix and are excluded, never capped.

Apply family eligibility and deterministic decreasing-p primary order from SELECTION_RULES. Show up to four supported rows, the first two as PICK. Fewer rows or qualitative/NO_FORECAST output is acceptable with the reason; unsupported rows are never padding. The best non-complementary gate alternative comes from the entire declared eligible universe, not a pruned four. Print original gate and RET03 shadow separately.

Freeze RET04 different-quantity and XCARD6 minimum-joint-failure shadow Rank 2 where calculable. Also freeze `SHADOW_RANK_DELTA` (top two by p_card − BASELINE_P) and, when the card is priced from a mixture, `SHADOW_BASE_ONLY` (SELECTION_RULES §3). Neither changes primary ordering. Print exact unconditional joint loss from common states, or honest Fréchet bounds. Label disjoint losing sets MECHANICALLY_PROTECTED; do not claim they improve skill or guarantee profit. Report both-decisive conditioning where pushes/voids exist.

## 6. Basketball playing conditions and rules

Resolve the exact competition's rules: FIBA (40 mins, four 10-min quarters) vs NBA/WNBA (48/40 mins), foul-out/bonus thresholds, and 5-minute overtime periods. Do not import NBA defaults (pace, totals, overtime rate, home edge, quarter length) into NBL, B.League, ACB, EuroLeague, or other national leagues. A raw scoring average is a labelled approximation, not a fitted pace model. Disclose missing or stale league profiles and widen uncertainty accordingly.

## 7. Write, audit and return

Use CARD_AND_LOG_TEMPLATES §3 in the mini's own format; new minis use mini-log-7, and a mini-log-6 mini finishes in its own format. Keep the decision block concise and put full evidence/arithmetic in A1–A9. State exact settlement fields, definitions and capture plan. Write one card before the footer, update only the footer's new-card/ID totals, and read it back. Audit C1–C20 with specific evidence (C17–C20 apply to mini-log-7 cards). Preserve every earlier issued block.

For a duplicate or late-news correction, append a dated addendum; reforecast is NOT_PRIMARY and never changes the original grade. If writing is unavailable, return the complete updated mini as READ_ONLY_DRAFT / NOT_ISSUED and do not claim allocation.

Return the full new card, exact file path, working ID/status, timing and lead band, top two or no-forecast reason, baseline coverage, gate/joint/sensitivity summary, audit evidence and updated footer. Explicitly state settlement NOT_PERFORMED and GitHub writes NO (GitHub repo `main` branch referenced in read-only mode). Do not promise prediction success.

CRICKET
----------------------------

## 1. Read and establish authority

Read every control from one pinned commit of the GitHub repository (`main` branch) in read-only mode (`PUBLISHED_MAIN_PINNED`), or from the local working tree only in a `LOCAL_WORKING_TREE` run (CURRENT_RULES §0). Never mix the two. Print the [reading receipt](README.md) after opening CURRENT_STATE, METHOD, CURRENT_RULES, SELECTION_RULES, CARD_AND_LOG_TEMPLATES, RULES_CRICKET, LEAGUE_RULES_CRICKET, [SOURCES §3.3](../../SOURCES.md#33-cricket) (cricket routes), ARCHIVE_USE_GUIDE, BASE_RATES_REGISTER, this prompt, the complete active mini, GAME_LOG_STATUS_CURRENT and relevant canonical event records. Record actual HEAD on `main`, working differences and time. Apply current controls over historical sport-engine notes.

If a required control or original mini is inaccessible, deliver a clearly labelled draft, not an issued append. Missing sporting data leads to explicit uncertainty or qualitative/NO_FORECAST research, not invented numbers.

## 2. Identity, duplicate and timing gate

Verify teams, competition/tournament, format (Test, ODI, T20, The Hundred), match number, venue, pitch conditions, scheduled start, weather forecast, reserve days, venue zone, UTC and Australia/Sydney time. Search every relevant local mini/carryover and canonical log body/status by ID, event key and aliases; doubleheaders and postponements need explicit identity handling. An existing event gets a dated addendum under its original ID, no new card.

For a new event, reconcile the mini's next working ID with current canonical state and outstanding local sequence. No gap, reservation, collision or renumbering. Record current source state before research and again immediately before write. Keep cutoff, research completion, actual issue and state-recheck times separate. If start is crossed, relabel honestly; exposure to live/final information prevents a clean pregame reconstruction. Retain requested late research in its separate cohort. Log the request in the mini's intake table (template §2-D) whatever its outcome. Confirm you hold the mini's issuing-writer lease and that the mini is not frozen for settlement; otherwise route the event to the next authorised mini (CURRENT_RULES §8). Follow the two-step issue window: research complete by about T−60, then freeze after the official lineup check, no later than T−5. Complete the mandatory availability search and final recheck first (CURRENT_RULES §5b; ROSTER_AVAILABILITY_PROTOCOL). If selections remain genuinely unpublished or unverified, record the exact side/field and completed attempts, then use supported scenarios or qualitative/NO_FORECAST research with the honest `LINEUP_UNCONFIRMED` label; do not claim an unperformed scheduled retry.

## 3. Evidence, XI and archive

**Availability research (AVAIL-2026.10.14-v1).** Read and apply [ROSTER_AVAILABILITY_PROTOCOL](../../ROSTER_AVAILABILITY_PROTOCOL.md) §§1–6 for both sides: exact starters/starting role, selected bench/replacements, current injuries/illness/suspensions/absences, and late changes. Complete its official match → both teams → eligibility/medical → permitted provider → local-language/obscure-competition escalation before reporting a missing field. Record actual searches, evidence/times and failures in the existing Evidence receipt/A3/A8; update the existing lineup-state metadata and audit C20. A roster, probable starter or predicted side is not confirmation. Recheck around the actual competition release window and immediately before freeze; re-price changed inputs. Never invent a healthy roster, bench or confirmation. If material gaps survive the full search, retain supported scenarios or qualitative/NO_FORECAST research with the exact reason. Do not read model-shadow or market material.

Follow official board/ICC match center → ESPNcricinfo/structured provider → quality corroboration routes. For each decisive claim retain URL, exact field/value or brief extract, source publication/update time when known, retrieval time and provenance/lineage. Log inaccessible/stale/conflicting sources. Three domains are not three independent collectors. No odds/tips/previews/fantasy inputs.

Confirm playing XI, toss result, batting order, bowling allocations/quotas, pitch report, weather/dew and rain resources; probable is not confirmed. Distinguish fact, historical estimate and analyst assumption. Inspect actual archive contents under `Previous Sports Results/Cricket/...` and print files, logical rows read, format/tournament filters, latest usable date and missingness. Use only results known before cutoff. Do not use postgame narrative or full-season aggregates from after cutoff.

**Form windows and known-at (PR-01, R28).**
- Print each side's (team or player) L5, L10, L15, L20, season to date and league level, from dated games before the cutoff, with the true n of each window: CARD_AND_LOG_TEMPLATES §3b, ARCHIVE_USE_GUIDE recipe R2.
- Use the archive where it holds the games; otherwise use a SOURCES route (ESPN team schedule, MLB statsapi, StatMuse, Tennis Abstract) and say which.
- Exclude archive rows flagged as duplicates, awarded results, forfeits or abandonments.
- The windows overlap and count as one piece of evidence. Only the shrunk L20/season rate may move the centre, as a listed adjustment with the unadjusted pair; the four-window recency blend is printed beside it for comparison.
- A short-window swing is width, not a lean, unless a named, current mechanism explains it.
- Print the archive capture date. An input whose availability before the cutoff cannot be shown is `KNOWN_AT_UNVERIFIED` and may not decide Rank 1.

## 4. Distribution, expected score and comparator

Build the simplest defensible coherent cricket distribution: model innings/phase/wicket dependence with explicit toss and rain branches. Account for chase dynamics: a chase ends on the winning delivery and can legally overshoot the target; do not simply cap every total at the target. Print every parameter and its basis, formula/table, normalization, tail treatment, covariance and endpoint transitions. If the required calculation cannot be done, report a supported approximation with limitations, or qualitative research with NOT_ESTIMATED probabilities.

Produce expected score terms from CARD_AND_LOG_TEMPLATES §3a: format/innings-specific runs and wickets where supported (common cross-team margin is often N/A in chases). Keep zeros; mark missing or irrelevant terms. Print all winner/draw/tie masses. For every candidate retain unconditional W/P/L/V and p_card=W/(W+L), with denominator and action convention.

Attempt BASELINE_LEAGUE_V1 on the same line/endpoint from league-only inputs, frozen before issue. Print recipe, source cohort/n/cutoff and parameters separately from the team model. No 0.5 placeholder or retrospective baseline fill. Missing baseline does not stop the card; it limits later skill measurement.

Show an adjustment table (pitch, weather/rain, toss, XI selection), unadjusted distribution/pair and low/base/high sensitivity on material uncertain inputs. Any adjustment-driven pair change is ADJUSTMENT_DEPENDENT, even below 0.25 SD. Report plausible probability ranges as sensitivity, not confidence intervals. Do not move individual probabilities outside the shared model.

**Pricing basis (PR-03).** When an input is labelled unfitted, stale, early-season or unconfirmed, the primary distribution is the declared mixture of its low/base/high cases (default weights 0.25/0.50/0.25, frozen before pricing). Print each row's `p_base` beside p_card. Compute at the precision actually used and print ε. A gate within ε of 0.62, or within 2ε of the 0.04 lead, is `GATE_UNRESOLVED_PRECISION`; rows within 2ε are a `PRECISION_TIE` (SELECTION_RULES §2). Apply any key-number, push or tie adjustment to the normalised common distribution, never to one row. Print each ranked row's line distance from centre (units and z, or N/A) and the card's baseline coverage, with an enumerated reason for each missing BASELINE_P (SELECTION_RULES §5, §9).

## 5. Candidate selection and dependence

Freeze the supported family/line-generation recipe before pricing (match winner, innings totals, phase runs, handicap). Price supplied rows and the declared derived universe; retain exclusions and unused supplied rows. Do not move thresholds repeatedly toward 90% to manufacture a strong gate. Values above the selection ceiling keep their true probabilities in the diagnostic appendix and are excluded, never capped.

Apply family eligibility and deterministic decreasing-p primary order from SELECTION_RULES. Show up to four supported rows, the first two as PICK. Fewer rows or qualitative/NO_FORECAST output is acceptable with the reason; unsupported rows are never padding. The best non-complementary gate alternative comes from the entire declared eligible universe, not a pruned four. Print original gate and RET03 shadow separately.

Freeze RET04 different-quantity and XCARD6 minimum-joint-failure shadow Rank 2 where calculable. Also freeze `SHADOW_RANK_DELTA` (top two by p_card − BASELINE_P) and, when the card is priced from a mixture, `SHADOW_BASE_ONLY` (SELECTION_RULES §3). Neither changes primary ordering. Print exact unconditional joint loss from common states, or honest Fréchet bounds. Label disjoint losing sets MECHANICALLY_PROTECTED; do not claim they improve skill or guarantee profit. Report both-decisive conditioning where pushes/voids exist.

## 6. Cricket playing conditions and rules

Confirm exact playing conditions: overs limit, powerplays, bowler maximum overs, DLS rain calculations, tie/super-over conventions, and draw/weather branches for multi-day matches. Ensure row endpoints match tie, super-over, DLS and no-result rules. Unsupported ball-by-ball calculation is not an exact simulation.

## 7. Write, audit and return

Use CARD_AND_LOG_TEMPLATES §3 in the mini's own format; new minis use mini-log-7, and a mini-log-6 mini finishes in its own format. Keep the decision block concise and put full evidence/arithmetic in A1–A9. State exact settlement fields, definitions and capture plan. Write one card before the footer, update only the footer's new-card/ID totals, and read it back. Audit C1–C20 with specific evidence (C17–C20 apply to mini-log-7 cards). Preserve every earlier issued block.

For a duplicate or late-news correction, append a dated addendum; reforecast is NOT_PRIMARY and never changes the original grade. If writing is unavailable, return the complete updated mini as READ_ONLY_DRAFT / NOT_ISSUED and do not claim allocation.

Return the full new card, exact file path, working ID/status, timing and lead band, top two or no-forecast reason, baseline coverage, gate/joint/sensitivity summary, audit evidence and updated footer. Explicitly state settlement NOT_PERFORMED and GitHub writes NO (GitHub repo `main` branch referenced in read-only mode). Do not promise prediction success.

BASEBALL
----------------------------

## 1. Read and establish authority

Read every control from one pinned commit of the GitHub repository (`main` branch) in read-only mode (`PUBLISHED_MAIN_PINNED`), or from the local working tree only in a `LOCAL_WORKING_TREE` run (CURRENT_RULES §0). Never mix the two. Print the [reading receipt](README.md) after opening CURRENT_STATE, METHOD, CURRENT_RULES, SELECTION_RULES, CARD_AND_LOG_TEMPLATES, RULES_BASEBALL, LEAGUE_PROFILES (Baseball rows: MLB, KBO, NPB, CPBL), ARCHIVE_USE_GUIDE (§8 defects), [SOURCES §3.1](../../SOURCES.md#31-baseball--mlb-npb-kbo-cpbl-lmb) (baseball routes), this prompt, the complete active mini, GAME_LOG_STATUS_CURRENT and relevant canonical event records. Record actual HEAD on `main`, working differences and time. Apply current controls over historical sport-engine notes.

If a required control or original mini is inaccessible, deliver a clearly labelled draft, not an issued append. Missing sporting data leads to explicit uncertainty or qualitative/NO_FORECAST research, not invented numbers.

## 2. Identity, duplicate and timing gate

Verify participants, league/competition, season, game number (single game vs doubleheader G1/G2), venue, native ID, official scheduled first pitch, venue zone, UTC and Australia/Sydney time. Search every relevant local mini/carryover and canonical log body/status by ID, event key and aliases; doubleheaders and postponements need explicit identity handling. An existing event gets a dated addendum under its original ID, no new card.

For a new event, reconcile the mini's next working ID with current canonical state and outstanding local sequence. No gap, reservation, collision or renumbering. Record current source state before research and again immediately before write. Keep cutoff, research completion, actual issue and state-recheck times separate. If start is crossed, relabel honestly; exposure to live/final information prevents a clean pregame reconstruction. Retain requested late research in its separate cohort. Log the request in the mini's intake table (template §2-D) whatever its outcome. Confirm you hold the mini's issuing-writer lease and that the mini is not frozen for settlement; otherwise route the event to the next authorised mini (CURRENT_RULES §8). Follow the two-step issue window: research complete by about T−60, then freeze after the official lineup check, no later than T−5. Complete the mandatory availability search and final recheck first (CURRENT_RULES §5b; ROSTER_AVAILABILITY_PROTOCOL). If selections remain genuinely unpublished or unverified, record the exact side/field and completed attempts, then use supported scenarios or qualitative/NO_FORECAST research with the honest `LINEUP_UNCONFIRMED` label; do not claim an unperformed scheduled retry.

## 3. Evidence, starters and archive

**Availability research (AVAIL-2026.10.14-v1).** Read and apply [ROSTER_AVAILABILITY_PROTOCOL](../../ROSTER_AVAILABILITY_PROTOCOL.md) §§1–6 for both sides: exact starters/starting role, selected bench/replacements, current injuries/illness/suspensions/absences, and late changes. Complete its official match → both teams → eligibility/medical → permitted provider → local-language/obscure-competition escalation before reporting a missing field. Record actual searches, evidence/times and failures in the existing Evidence receipt/A3/A8; update the existing lineup-state metadata and audit C20. A roster, probable starter or predicted side is not confirmation. Recheck around the actual competition release window and immediately before freeze; re-price changed inputs. Never invent a healthy roster, bench or confirmation. If material gaps survive the full search, retain supported scenarios or qualitative/NO_FORECAST research with the exact reason. Do not read model-shadow or market material.

Follow official league scoreboard (MLB Gameday, KBO, NPB official, etc.) → structured provider (MyKBO, etc.) → quality corroboration routes. For each decisive claim retain URL, exact field/value or brief extract, source publication/update time when known, retrieval time and provenance/lineage. Log inaccessible/stale/conflicting sources. Three domains are not three independent collectors. No odds/tips/previews/fantasy inputs.

Verify starting pitcher identity and expected workload, confirmed batting lineup/platoon, bullpen availability, park factors, weather and rest; probable is not confirmed. Unknown pitcher weights stay assumptions, not facts. Inspect actual archive contents under `Previous Sports Results/Baseball/<league>/...` and print files, logical rows read, season/endpoint filters, latest usable date and missingness. Use only results known before cutoff. Do not use postgame narrative or full-season aggregates from after cutoff.

**Form windows and known-at (PR-01, R28).**
- Print each side's (team or player) L5, L10, L15, L20, season to date and league level, from dated games before the cutoff, with the true n of each window: CARD_AND_LOG_TEMPLATES §3b, ARCHIVE_USE_GUIDE recipe R2.
- Use the archive where it holds the games; otherwise use a SOURCES route (ESPN team schedule, MLB statsapi, StatMuse, Tennis Abstract) and say which.
- Exclude archive rows flagged as duplicates, awarded results, forfeits or abandonments.
- The windows overlap and count as one piece of evidence. Only the shrunk L20/season rate may move the centre, as a listed adjustment with the unadjusted pair; the four-window recency blend is printed beside it for comparison.
- A short-window swing is width, not a lean, unless a named, current mechanism explains it.
- Print the archive capture date. An input whose availability before the cutoff cannot be shown is `KNOWN_AT_UNVERIFIED` and may not decide Rank 1.

## 4. Distribution, expected score and comparator

Build the simplest defensible coherent baseball distribution: use supported overdispersed team-run scenarios with shared environment, starter/bullpen segments and correct home last-inning/extras handling. Print every parameter and its basis, formula/table, normalization, tail treatment, covariance and endpoint transitions. If the required calculation cannot be done, report a supported approximation with limitations, or qualitative research with NOT_ESTIMATED probabilities.

Produce expected score terms from CARD_AND_LOG_TEMPLATES §3a: team runs (means & SDs), total runs (mean & SD), signed margin (mean & SD) over exact innings/extras endpoint. +1.5 needs team-directional win and exactly-one-run-loss mass, with tie/action treatment. Moneyline action on a tie comes from the frozen contract (two-way void or push, three-way, or loss), never a sport-wide default (R13). Keep zeros; mark missing or irrelevant terms. Print all winner/draw/tie masses. For every candidate retain unconditional W/P/L/V and p_card=W/(W+L), with denominator and action convention.

Attempt BASELINE_LEAGUE_V1 on the same line/endpoint from league-only inputs, frozen before issue. Print recipe, source cohort/n/cutoff and parameters separately from the team model. No 0.5 placeholder or retrospective baseline fill. Missing baseline does not stop the card; it limits later skill measurement.

Show an adjustment table (starting pitcher, bullpen, park, weather), unadjusted distribution/pair and low/base/high sensitivity on material uncertain inputs. Any adjustment-driven pair change is ADJUSTMENT_DEPENDENT, even below 0.25 SD. Report plausible probability ranges as sensitivity, not confidence intervals. Do not move individual probabilities outside the shared model.

**Pricing basis (PR-03).** When an input is labelled unfitted, stale, early-season or unconfirmed, the primary distribution is the declared mixture of its low/base/high cases (default weights 0.25/0.50/0.25, frozen before pricing). Print each row's `p_base` beside p_card. Compute at the precision actually used and print ε. A gate within ε of 0.62, or within 2ε of the 0.04 lead, is `GATE_UNRESOLVED_PRECISION`; rows within 2ε are a `PRECISION_TIE` (SELECTION_RULES §2). Apply any key-number, push or tie adjustment to the normalised common distribution, never to one row. Print each ranked row's line distance from centre (units and z, or N/A) and the card's baseline coverage, with an enumerated reason for each missing BASELINE_P (SELECTION_RULES §5, §9).

## 5. Candidate selection and dependence

Freeze the supported family/line-generation recipe before pricing (totals, run lines, moneylines). Price supplied rows and the declared derived universe; retain exclusions and unused supplied rows. Do not move thresholds repeatedly toward 90% to manufacture a strong gate. Values above the selection ceiling keep their true probabilities in the diagnostic appendix and are excluded, never capped.

Apply family eligibility and deterministic decreasing-p primary order from SELECTION_RULES. Show up to four supported rows, the first two as PICK. Fewer rows or qualitative/NO_FORECAST output is acceptable with the reason; unsupported rows are never padding. The best non-complementary gate alternative comes from the entire declared eligible universe, not a pruned four. Print original gate and RET03 shadow separately.

Freeze RET04 different-quantity and XCARD6 minimum-joint-failure shadow Rank 2 where calculable. Also freeze `SHADOW_RANK_DELTA` (top two by p_card − BASELINE_P) and, when the card is priced from a mixture, `SHADOW_BASE_ONLY` (SELECTION_RULES §3). Neither changes primary ordering. Print exact unconditional joint loss from common states, or honest Fréchet bounds. Label disjoint losing sets MECHANICALLY_PROTECTED; do not claim they improve skill or guarantee profit. Report both-decisive conditioning where pushes/voids exist.

## 6. Baseball playing conditions and rules

Verify the competition's and season's own rules for innings limits, extra innings, ties, the automatic runner, shortened games and suspended games: regular season KBO/NPB ties after 11/12 innings vs MLB automatic runner in extra innings. Do not carry one league's rules to another. +1.5 needs team-directional win and exactly-one-run-loss mass, with tie/action treatment. A league absolute one-run share is not the selected team's probability.

## 7. Write, audit and return

Use CARD_AND_LOG_TEMPLATES §3 in the mini's own format; new minis use mini-log-7, and a mini-log-6 mini finishes in its own format. Keep the decision block concise and put full evidence/arithmetic in A1–A9. State exact settlement fields, definitions and capture plan. Write one card before the footer, update only the footer's new-card/ID totals, and read it back. Audit C1–C20 with specific evidence (C17–C20 apply to mini-log-7 cards). Preserve every earlier issued block.

For a duplicate or late-news correction, append a dated addendum; reforecast is NOT_PRIMARY and never changes the original grade. If writing is unavailable, return the complete updated mini as READ_ONLY_DRAFT / NOT_ISSUED and do not claim allocation.

Return the full new card, exact file path, working ID/status, timing and lead band, top two or no-forecast reason, baseline coverage, gate/joint/sensitivity summary, audit evidence and updated footer. Explicitly state settlement NOT_PERFORMED and GitHub writes NO (GitHub repo `main` branch referenced in read-only mode). Do not promise prediction success.

SOCCER
----------------------------

## 1. Read and establish authority

Read every control from one pinned commit of the GitHub repository (`main` branch) in read-only mode (`PUBLISHED_MAIN_PINNED`), or from the local working tree only in a `LOCAL_WORKING_TREE` run (CURRENT_RULES §0). Never mix the two. Print the [reading receipt](README.md) after opening CURRENT_STATE, METHOD, CURRENT_RULES, SELECTION_RULES, CARD_AND_LOG_TEMPLATES, RULES_SOCCER, LEAGUE_RULES_SOCCER, LEAGUE_PROFILES (Soccer rows), [SOURCES §3.4](../../SOURCES.md#34-soccer) (soccer routes; the English top-flight archive is described in §3.32), ARCHIVE_USE_GUIDE, this prompt, the complete active mini, GAME_LOG_STATUS_CURRENT and relevant canonical event records. Record actual HEAD on `main`, working differences and time. Apply current controls over historical sport-engine notes.

If a required control or original mini is inaccessible, deliver a clearly labelled draft, not an issued append. Missing sporting data leads to explicit uncertainty or qualitative/NO_FORECAST research, not invented numbers.

## 2. Identity, duplicate and timing gate

Verify clubs/national teams, competition, stage, venue, native ID, official scheduled kickoff, venue zone, UTC and Australia/Sydney time. Search every relevant local mini/carryover and canonical log body/status by ID, event key and aliases; doubleheaders and postponements need explicit identity handling. An existing event gets a dated addendum under its original ID, no new card.

For a new event, reconcile the mini's next working ID with current canonical state and outstanding local sequence. No gap, reservation, collision or renumbering. Record current source state before research and again immediately before write. Keep cutoff, research completion, actual issue and state-recheck times separate. If start is crossed, relabel honestly; exposure to live/final information prevents a clean pregame reconstruction. Retain requested late research in its separate cohort. Log the request in the mini's intake table (template §2-D) whatever its outcome. Confirm you hold the mini's issuing-writer lease and that the mini is not frozen for settlement; otherwise route the event to the next authorised mini (CURRENT_RULES §8). Follow the two-step issue window: research complete by about T−60, then freeze after the official lineup check, no later than T−5. Complete the mandatory availability search and final recheck first (CURRENT_RULES §5b; ROSTER_AVAILABILITY_PROTOCOL). If selections remain genuinely unpublished or unverified, record the exact side/field and completed attempts, then use supported scenarios or qualitative/NO_FORECAST research with the honest `LINEUP_UNCONFIRMED` label; do not claim an unperformed scheduled retry.

## 3. Evidence, XI and archive

**Availability research (AVAIL-2026.10.14-v1).** Read and apply [ROSTER_AVAILABILITY_PROTOCOL](../../ROSTER_AVAILABILITY_PROTOCOL.md) §§1–6 for both sides: exact starters/starting role, selected bench/replacements, current injuries/illness/suspensions/absences, and late changes. Complete its official match → both teams → eligibility/medical → permitted provider → local-language/obscure-competition escalation before reporting a missing field. Record actual searches, evidence/times and failures in the existing Evidence receipt/A3/A8; update the existing lineup-state metadata and audit C20. A roster, probable starter or predicted side is not confirmation. Recheck around the actual competition release window and immediately before freeze; re-price changed inputs. Never invent a healthy roster, bench or confirmation. If material gaps survive the full search, retain supported scenarios or qualitative/NO_FORECAST research with the exact reason. Do not read model-shadow or market material.

Follow official field-owner / federation match center → structured provider (FBref, official club reporting, etc.) → quality corroboration routes. For each decisive claim retain URL, exact field/value or brief extract, source publication/update time when known, retrieval time and provenance/lineage. Log inaccessible/stale/conflicting sources. Three domains are not three independent collectors. No odds/tips/previews/fantasy inputs.

Confirm starting XI, goalkeeper, bench/rotation, injuries, schedule congestion; probable is not confirmed. Inspect actual archive contents under `Previous Sports Results/Soccer/<league>/...` and print files, logical rows read, season/endpoint filters, latest usable date and missingness. Use only results known before cutoff. Do not use postgame narrative or full-season aggregates from after cutoff.

**Form windows and known-at (PR-01, R28).**
- Print each side's (team or player) L5, L10, L15, L20, season to date and league level, from dated games before the cutoff, with the true n of each window: CARD_AND_LOG_TEMPLATES §3b, ARCHIVE_USE_GUIDE recipe R2.
- Use the archive where it holds the games; otherwise use a SOURCES route (ESPN team schedule, MLB statsapi, StatMuse, Tennis Abstract) and say which.
- Exclude archive rows flagged as duplicates, awarded results, forfeits or abandonments.
- The windows overlap and count as one piece of evidence. Only the shrunk L20/season rate may move the centre, as a listed adjustment with the unadjusted pair; the four-window recency blend is printed beside it for comparison.
- A short-window swing is width, not a lean, unless a named, current mechanism explains it.
- Print the archive capture date. An input whose availability before the cutoff cannot be shown is `KNOWN_AT_UNVERIFIED` and may not decide Rank 1.

## 4. Distribution, expected score and comparator

Build the simplest defensible coherent soccer distribution: use a coherent regulation score model with explicit draw, opponent-adjusted xG/shot process, supported half split for phase rows, and appropriate low-score correction. Separate provider-backed corner count models (corners need their own supported count/provider model and joint dependence; goal counts never generate corner probabilities). Print every parameter and its basis, formula/table, normalization, tail treatment, covariance and endpoint transitions. If the required calculation cannot be done, report a supported approximation with limitations, or qualitative research with NOT_ESTIMATED probabilities.

Produce expected score terms from CARD_AND_LOG_TEMPLATES §3a: regulation goals per team/total/margin, supported half goals, and separate provider-backed corner counts. Keep zeros; mark missing or irrelevant terms. Print all winner/draw/tie masses. For every candidate retain unconditional W/P/L/V and p_card=W/(W+L), with denominator and action convention.

Attempt BASELINE_LEAGUE_V1 on the same line/endpoint from league-only inputs, frozen before issue. Print recipe, source cohort/n/cutoff and parameters separately from the team model. No 0.5 placeholder or retrospective baseline fill. Missing baseline does not stop the card; it limits later skill measurement.

Show an adjustment table (home venue, rotation/XI, rest, weather), unadjusted distribution/pair and low/base/high sensitivity on material uncertain inputs. Any adjustment-driven pair change is ADJUSTMENT_DEPENDENT, even below 0.25 SD. Report plausible probability ranges as sensitivity, not confidence intervals. Do not move individual probabilities outside the shared model.

**Pricing basis (PR-03).** When an input is labelled unfitted, stale, early-season or unconfirmed, the primary distribution is the declared mixture of its low/base/high cases (default weights 0.25/0.50/0.25, frozen before pricing). Print each row's `p_base` beside p_card. Compute at the precision actually used and print ε. A gate within ε of 0.62, or within 2ε of the 0.04 lead, is `GATE_UNRESOLVED_PRECISION`; rows within 2ε are a `PRECISION_TIE` (SELECTION_RULES §2). Apply any key-number, push or tie adjustment to the normalised common distribution, never to one row. Print each ranked row's line distance from centre (units and z, or N/A) and the card's baseline coverage, with an enumerated reason for each missing BASELINE_P (SELECTION_RULES §5, §9).

## 5. Candidate selection and dependence

Freeze the supported family/line-generation recipe before pricing (handicaps, totals, double chance, 1H totals). Price supplied rows and the declared derived universe; retain exclusions and unused supplied rows. Do not move thresholds repeatedly toward 90% to manufacture a strong gate. Values above the selection ceiling keep their true probabilities in the diagnostic appendix and are excluded, never capped.

Apply family eligibility and deterministic decreasing-p primary order from SELECTION_RULES. Show up to four supported rows, the first two as PICK. Fewer rows or qualitative/NO_FORECAST output is acceptable with the reason; unsupported rows are never padding. The best non-complementary gate alternative comes from the entire declared eligible universe, not a pruned four. Print original gate and RET03 shadow separately.

Freeze RET04 different-quantity and XCARD6 minimum-joint-failure shadow Rank 2 where calculable. Also freeze `SHADOW_RANK_DELTA` (top two by p_card − BASELINE_P) and, when the card is priced from a mixture, `SHADOW_BASE_ONLY` (SELECTION_RULES §3). Neither changes primary ordering. Print exact unconditional joint loss from common states, or honest Fréchet bounds. Label disjoint losing sets MECHANICALLY_PROTECTED; do not claim they improve skill or guarantee profit. Report both-decisive conditioning where pushes/voids exist.

## 6. Soccer playing conditions and rules

Verify regulation 90 minutes + stoppage endpoint. ET/penalties apply only where explicitly specified for cup knockout stages. Check league draw rules. Check first-half and team-to-score assumptions against confirmed availability; no constants from one league silently transferred to another.

## 7. Write, audit and return

Use CARD_AND_LOG_TEMPLATES §3 in the mini's own format; new minis use mini-log-7, and a mini-log-6 mini finishes in its own format. Keep the decision block concise and put full evidence/arithmetic in A1–A9. State exact settlement fields, definitions and capture plan. Write one card before the footer, update only the footer's new-card/ID totals, and read it back. Audit C1–C20 with specific evidence (C17–C20 apply to mini-log-7 cards). Preserve every earlier issued block.

For a duplicate or late-news correction, append a dated addendum; reforecast is NOT_PRIMARY and never changes the original grade. If writing is unavailable, return the complete updated mini as READ_ONLY_DRAFT / NOT_ISSUED and do not claim allocation.

Return the full new card, exact file path, working ID/status, timing and lead band, top two or no-forecast reason, baseline coverage, gate/joint/sensitivity summary, audit evidence and updated footer. Explicitly state settlement NOT_PERFORMED and GitHub writes NO (GitHub repo `main` branch referenced in read-only mode). Do not promise prediction success.

ICE HOCKEY
----------------------------

## 1. Read and establish authority

Read every control from one pinned commit of the GitHub repository (`main` branch) in read-only mode (`PUBLISHED_MAIN_PINNED`), or from the local working tree only in a `LOCAL_WORKING_TREE` run (CURRENT_RULES §0). Never mix the two. Print the [reading receipt](README.md) after opening CURRENT_STATE, METHOD, CURRENT_RULES, SELECTION_RULES, CARD_AND_LOG_TEMPLATES, RULES_ICE_HOCKEY, RULES_NHL (if applicable), LEAGUE_PROFILES (Ice hockey rows), [SOURCES §3.9](../../SOURCES.md#39-nhl) (NHL routes). For any other league, use [§3.13](../../SOURCES.md#313-game-level-detail-results-line-ups-coaches-and-officials-tested-2026-09-30) (Liiga API, Elite Prospects), §3.29 (Danish Metal Ligaen), §3.31 (the Czech archive) or the league's own official site, and say which. An NHL route is never assumed to cover another league, ARCHIVE_USE_GUIDE, this prompt, the complete active mini, GAME_LOG_STATUS_CURRENT and relevant canonical event records. Record actual HEAD on `main`, working differences and time. Apply current controls over historical sport-engine notes.

If a required control or original mini is inaccessible, deliver a clearly labelled draft, not an issued append. Missing sporting data leads to explicit uncertainty or qualitative/NO_FORECAST research, not invented numbers.

## 2. Identity, duplicate and timing gate

Verify teams, league (NHL, Tipsport Extraliga, Liiga, SHL, etc.), season, venue, native ID, official scheduled puck drop, venue zone, UTC and Australia/Sydney time. Search every relevant local mini/carryover and canonical log body/status by ID, event key and aliases; doubleheaders and postponements need explicit identity handling. An existing event gets a dated addendum under its original ID, no new card.

For a new event, reconcile the mini's next working ID with current canonical state and outstanding local sequence. No gap, reservation, collision or renumbering. Record current source state before research and again immediately before write. Keep cutoff, research completion, actual issue and state-recheck times separate. If start is crossed, relabel honestly; exposure to live/final information prevents a clean pregame reconstruction. Retain requested late research in its separate cohort. Log the request in the mini's intake table (template §2-D) whatever its outcome. Confirm you hold the mini's issuing-writer lease and that the mini is not frozen for settlement; otherwise route the event to the next authorised mini (CURRENT_RULES §8). Follow the two-step issue window: research complete by about T−60, then freeze after the official lineup check, no later than T−5. Complete the mandatory availability search and final recheck first (CURRENT_RULES §5b; ROSTER_AVAILABILITY_PROTOCOL). If selections remain genuinely unpublished or unverified, record the exact side/field and completed attempts, then use supported scenarios or qualitative/NO_FORECAST research with the honest `LINEUP_UNCONFIRMED` label; do not claim an unperformed scheduled retry.

## 3. Evidence, goalies and archive

**Availability research (AVAIL-2026.10.14-v1).** Read and apply [ROSTER_AVAILABILITY_PROTOCOL](../../ROSTER_AVAILABILITY_PROTOCOL.md) §§1–6 for both sides: exact starters/starting role, selected bench/replacements, current injuries/illness/suspensions/absences, and late changes. Complete its official match → both teams → eligibility/medical → permitted provider → local-language/obscure-competition escalation before reporting a missing field. Record actual searches, evidence/times and failures in the existing Evidence receipt/A3/A8; update the existing lineup-state metadata and audit C20. A roster, probable starter or predicted side is not confirmation. Recheck around the actual competition release window and immediately before freeze; re-price changed inputs. Never invent a healthy roster, bench or confirmation. If material gaps survive the full search, retain supported scenarios or qualitative/NO_FORECAST research with the exact reason. Do not read model-shadow or market material.

Follow official league game sheet / match reports → structured provider → quality corroboration routes. For each decisive claim retain URL, exact field/value or brief extract, source publication/update time when known, retrieval time and provenance/lineage. Log inaccessible/stale/conflicting sources. Three domains are not three independent collectors. No odds/tips/previews/fantasy inputs.

Confirm starting goalies or supported mixture, lines/scratches, special teams, rest and travel; probable is not confirmed. Unconfirmed goalie sensitivity must reach totals/ranks. Inspect actual archive contents under `Previous Sports Results/Ice Hockey/<league>/...` and print files, logical rows read, season/endpoint filters, latest usable date and missingness. Use only results known before cutoff. Do not use postgame narrative or full-season aggregates from after cutoff.

**Form windows and known-at (PR-01, R28).**
- Print each side's (team or player) L5, L10, L15, L20, season to date and league level, from dated games before the cutoff, with the true n of each window: CARD_AND_LOG_TEMPLATES §3b, ARCHIVE_USE_GUIDE recipe R2.
- Use the archive where it holds the games; otherwise use a SOURCES route (ESPN team schedule, MLB statsapi, StatMuse, Tennis Abstract) and say which.
- Exclude archive rows flagged as duplicates, awarded results, forfeits or abandonments.
- The windows overlap and count as one piece of evidence. Only the shrunk L20/season rate may move the centre, as a listed adjustment with the unadjusted pair; the four-window recency blend is printed beside it for comparison.
- A short-window swing is width, not a lean, unless a named, current mechanism explains it.
- Print the archive capture date. An input whose availability before the cutoff cannot be shown is `KNOWN_AT_UNVERIFIED` and may not decide Rank 1.

## 4. Distribution, expected score and comparator

Build the simplest defensible coherent ice hockey distribution: 5v5 creation/suppression, special teams, rest/travel, and explicit empty-net tails. Separate regulation draw from full-game OT/SO and final-score convention. Print directional handicap mass, not unconditional league absolute-margin frequency. Print every parameter and its basis, formula/table, normalization, tail treatment, covariance and endpoint transitions. If the required calculation cannot be done, report a supported approximation with limitations, or qualitative research with NOT_ESTIMATED probabilities.

Produce expected score terms from CARD_AND_LOG_TEMPLATES §3a: regulation and/or full-game goals with OT/SO accounting, total, signed margin and supported SDs. Keep zeros; mark missing or irrelevant terms. Print all winner/draw/tie masses. For every candidate retain unconditional W/P/L/V and p_card=W/(W+L), with denominator and action convention.

Attempt BASELINE_LEAGUE_V1 on the same line/endpoint from league-only inputs, frozen before issue. Print recipe, source cohort/n/cutoff and parameters separately from the team model. No 0.5 placeholder or retrospective baseline fill. Missing baseline does not stop the card; it limits later skill measurement.

Show an adjustment table (goalie mixture, special teams, rest/travel), unadjusted distribution/pair and low/base/high sensitivity on material uncertain inputs. Any adjustment-driven pair change is ADJUSTMENT_DEPENDENT, even below 0.25 SD. Report plausible probability ranges as sensitivity, not confidence intervals. Do not move individual probabilities outside the shared model.

**Pricing basis (PR-03).** When an input is labelled unfitted, stale, early-season or unconfirmed, the primary distribution is the declared mixture of its low/base/high cases (default weights 0.25/0.50/0.25, frozen before pricing). Print each row's `p_base` beside p_card. Compute at the precision actually used and print ε. A gate within ε of 0.62, or within 2ε of the 0.04 lead, is `GATE_UNRESOLVED_PRECISION`; rows within 2ε are a `PRECISION_TIE` (SELECTION_RULES §2). Apply any key-number, push or tie adjustment to the normalised common distribution, never to one row. Print each ranked row's line distance from centre (units and z, or N/A) and the card's baseline coverage, with an enumerated reason for each missing BASELINE_P (SELECTION_RULES §5, §9).

## 5. Candidate selection and dependence

Freeze the supported family/line-generation recipe before pricing (puck lines, full-game totals, regulation lines, team totals). Price supplied rows and the declared derived universe; retain exclusions and unused supplied rows. Do not move thresholds repeatedly toward 90% to manufacture a strong gate. Values above the selection ceiling keep their true probabilities in the diagnostic appendix and are excluded, never capped.

Apply family eligibility and deterministic decreasing-p primary order from SELECTION_RULES. Show up to four supported rows, the first two as PICK. Fewer rows or qualitative/NO_FORECAST output is acceptable with the reason; unsupported rows are never padding. The best non-complementary gate alternative comes from the entire declared eligible universe, not a pruned four. Print original gate and RET03 shadow separately.

Freeze RET04 different-quantity and XCARD6 minimum-joint-failure shadow Rank 2 where calculable. Also freeze `SHADOW_RANK_DELTA` (top two by p_card − BASELINE_P) and, when the card is priced from a mixture, `SHADOW_BASE_ONLY` (SELECTION_RULES §3). Neither changes primary ordering. Print exact unconditional joint loss from common states, or honest Fréchet bounds. Label disjoint losing sets MECHANICALLY_PROTECTED; do not claim they improve skill or guarantee profit. Report both-decisive conditioning where pushes/voids exist.

## 6. Ice hockey playing conditions and rules

Verify regulation 60 minutes vs regular-season 3-on-3 OT + shootout vs playoff continuous OT. Confirm whether contract is 60-minute regulation or includes OT/SO. Empty-net goal tails must be explicit in full-game totals and margins. Other leagues require their own rules and profile.

## 7. Write, audit and return

Use CARD_AND_LOG_TEMPLATES §3 in the mini's own format; new minis use mini-log-7, and a mini-log-6 mini finishes in its own format. Keep the decision block concise and put full evidence/arithmetic in A1–A9. State exact settlement fields, definitions and capture plan. Write one card before the footer, update only the footer's new-card/ID totals, and read it back. Audit C1–C20 with specific evidence (C17–C20 apply to mini-log-7 cards). Preserve every earlier issued block.

For a duplicate or late-news correction, append a dated addendum; reforecast is NOT_PRIMARY and never changes the original grade. If writing is unavailable, return the complete updated mini as READ_ONLY_DRAFT / NOT_ISSUED and do not claim allocation.

Return the full new card, exact file path, working ID/status, timing and lead band, top two or no-forecast reason, baseline coverage, gate/joint/sensitivity summary, audit evidence and updated footer. Explicitly state settlement NOT_PERFORMED and GitHub writes NO (GitHub repo `main` branch referenced in read-only mode). Do not promise prediction success.

TENNIS
----------------------------

## 1. Read and establish authority

Read every control from one pinned commit of the GitHub repository (`main` branch) in read-only mode (`PUBLISHED_MAIN_PINNED`), or from the local working tree only in a `LOCAL_WORKING_TREE` run (CURRENT_RULES §0). Never mix the two. Print the [reading receipt](README.md) after opening CURRENT_STATE, METHOD, CURRENT_RULES, SELECTION_RULES, CARD_AND_LOG_TEMPLATES, RULES_TENNIS, [SOURCES §3.10](../../SOURCES.md#310-tennis) (tennis routes), ARCHIVE_USE_GUIDE, this prompt, the complete active mini, GAME_LOG_STATUS_CURRENT and relevant canonical event records. Record actual HEAD on `main`, working differences and time. Apply current controls over historical sport-engine notes.

If a required control or original mini is inaccessible, deliver a clearly labelled draft, not an issued append. Missing sporting data leads to explicit uncertainty or qualitative/NO_FORECAST research, not invented numbers.

## 2. Identity, duplicate and timing gate

Verify players, tournament, tour (ATP, WTA, Challenger), round, court/surface, match order on court, scheduled time, venue zone, UTC and Australia/Sydney time. Search every relevant local mini/carryover and canonical log body/status by ID, event key and aliases; doubleheaders and postponements need explicit identity handling. An existing event gets a dated addendum under its original ID, no new card.

For a new event, reconcile the mini's next working ID with current canonical state and outstanding local sequence. No gap, reservation, collision or renumbering. Record current source state before research and again immediately before write. Keep cutoff, research completion, actual issue and state-recheck times separate. If start is crossed, relabel honestly; exposure to live/final information prevents a clean pregame reconstruction. Retain requested late research in its separate cohort. Log the request in the mini's intake table (template §2-D) whatever its outcome. Confirm you hold the mini's issuing-writer lease and that the mini is not frozen for settlement; otherwise route the event to the next authorised mini (CURRENT_RULES §8). Follow the two-step issue window: research complete by about T−60, then freeze after the official lineup check, no later than T−5. Complete the mandatory availability search and final recheck first (CURRENT_RULES §5b; ROSTER_AVAILABILITY_PROTOCOL). If selections remain genuinely unpublished or unverified, record the exact side/field and completed attempts, then use supported scenarios or qualitative/NO_FORECAST research with the honest `LINEUP_UNCONFIRMED` label; do not claim an unperformed scheduled retry.

## 3. Evidence, fitness and archive

**Availability research (AVAIL-2026.10.14-v1).** Read and apply [ROSTER_AVAILABILITY_PROTOCOL](../../ROSTER_AVAILABILITY_PROTOCOL.md) §§1–6 for both sides: exact starters/starting role, selected bench/replacements, current injuries/illness/suspensions/absences, and late changes. Complete its official match → both teams → eligibility/medical → permitted provider → local-language/obscure-competition escalation before reporting a missing field. Record actual searches, evidence/times and failures in the existing Evidence receipt/A3/A8; update the existing lineup-state metadata and audit C20. A roster, probable starter or predicted side is not confirmation. Recheck around the actual competition release window and immediately before freeze; re-price changed inputs. Never invent a healthy roster, bench or confirmation. If material gaps survive the full search, retain supported scenarios or qualitative/NO_FORECAST research with the exact reason. Do not read model-shadow or market material.

Follow official tour match center (ATP / WTA) → structured provider → quality corroboration routes. For each decisive claim retain URL, exact field/value or brief extract, source publication/update time when known, retrieval time and provenance/lineage. Log inaccessible/stale/conflicting sources. Three domains are not three independent collectors. No odds/tips/previews/fantasy inputs.

Verify event/player identity, round, tour, surface, best-of format, tiebreak rules, fitness, workload, serve/return data and appropriate benchmark; probable is not confirmed. Inspect current tennis archive/provider coverage rather than assuming it is empty. Use only results known before cutoff. Do not use postgame narrative or full-season aggregates from after cutoff.

**Form windows and known-at (PR-01, R28).**
- Print each side's (team or player) L5, L10, L15, L20, season to date and league level, from dated games before the cutoff, with the true n of each window: CARD_AND_LOG_TEMPLATES §3b, ARCHIVE_USE_GUIDE recipe R2.
- Use the archive where it holds the games; otherwise use a SOURCES route (ESPN team schedule, MLB statsapi, StatMuse, Tennis Abstract) and say which.
- Exclude archive rows flagged as duplicates, awarded results, forfeits or abandonments.
- The windows overlap and count as one piece of evidence. Only the shrunk L20/season rate may move the centre, as a listed adjustment with the unadjusted pair; the four-window recency blend is printed beside it for comparison.
- A short-window swing is width, not a lean, unless a named, current mechanism explains it.
- Print the archive capture date. An input whose availability before the cutoff cannot be shown is `KNOWN_AT_UNVERIFIED` and may not decide Rank 1.

## 4. Distribution, expected score and comparator

Build the simplest defensible coherent tennis distribution: games/sets/winner come from compatible point-to-match construction with a supported form mixture; show calculation or label the approximation. Compare deciding-set mass with relevant tour/surface/format data, never force a global reference rate. Derive game handicaps and totals from the complete set-score states, including match-losing states. Covering −k.5 games does not imply winning the match, and set handicaps are a different quantity from game handicaps (R12). Print every parameter and its basis, formula/table, normalization, tail treatment, covariance and endpoint transitions. If the required calculation cannot be done, report a supported approximation with limitations, or qualitative research with NOT_ESTIMATED probabilities.

Produce expected score terms from CARD_AND_LOG_TEMPLATES §3a: games per player/total/margin, expected sets and deciding-set probability for exact format. Keep zeros; mark missing or irrelevant terms. Print all winner/draw/tie masses. For every candidate retain unconditional W/P/L/V and p_card=W/(W+L), with denominator and action convention.

Attempt BASELINE_LEAGUE_V1 on the same line/endpoint from tour-only inputs, frozen before issue. Print recipe, source cohort/n/cutoff and parameters separately from the player model. No 0.5 placeholder or retrospective baseline fill. Missing baseline does not stop the card; it limits later skill measurement.

Show an adjustment table (surface, fatigue/workload, form), unadjusted distribution/pair and low/base/high sensitivity on material uncertain inputs. Any adjustment-driven pair change is ADJUSTMENT_DEPENDENT, even below 0.25 SD. Report plausible probability ranges as sensitivity, not confidence intervals. Do not move individual probabilities outside the shared model.

**Pricing basis (PR-03).** When an input is labelled unfitted, stale, early-season or unconfirmed, the primary distribution is the declared mixture of its low/base/high cases (default weights 0.25/0.50/0.25, frozen before pricing). Print each row's `p_base` beside p_card. Compute at the precision actually used and print ε. A gate within ε of 0.62, or within 2ε of the 0.04 lead, is `GATE_UNRESOLVED_PRECISION`; rows within 2ε are a `PRECISION_TIE` (SELECTION_RULES §2). Apply any key-number, push or tie adjustment to the normalised common distribution, never to one row. Print each ranked row's line distance from centre (units and z, or N/A) and the card's baseline coverage, with an enumerated reason for each missing BASELINE_P (SELECTION_RULES §5, §9).

## 5. Candidate selection and dependence

Freeze the supported family/line-generation recipe before pricing (match winner, game handicaps, set totals, game totals). Price supplied rows and the declared derived universe; retain exclusions and unused supplied rows. Do not move thresholds repeatedly toward 90% to manufacture a strong gate. Values above the selection ceiling keep their true probabilities in the diagnostic appendix and are excluded, never capped.

Apply family eligibility and deterministic decreasing-p primary order from SELECTION_RULES. Show up to four supported rows, the first two as PICK. Fewer rows or qualitative/NO_FORECAST output is acceptable with the reason; unsupported rows are never padding. The best non-complementary gate alternative comes from the entire declared eligible universe, not a pruned four. Print original gate and RET03 shadow separately.

Freeze RET04 different-quantity and XCARD6 minimum-joint-failure shadow Rank 2 where calculable. Also freeze `SHADOW_RANK_DELTA` (top two by p_card − BASELINE_P) and, when the card is priced from a mixture, `SHADOW_BASE_ONLY` (SELECTION_RULES §3). Neither changes primary ordering. Print exact unconditional joint loss from common states, or honest Fréchet bounds. Label disjoint losing sets MECHANICALLY_PROTECTED; do not claim they improve skill or guarantee profit. Report both-decisive conditioning where pushes/voids exist.

## 6. Tennis playing conditions and rules

Verify match format (best-of-3 vs best-of-5 sets), final-set tiebreak rules (e.g. 10-point champions tiebreak at 6–6). Freeze retirement/walkover rules per row; sporting advance and operator settlement are different.

## 7. Write, audit and return

Use CARD_AND_LOG_TEMPLATES §3 in the mini's own format; new minis use mini-log-7, and a mini-log-6 mini finishes in its own format. Keep the decision block concise and put full evidence/arithmetic in A1–A9. State exact settlement fields, definitions and capture plan. Write one card before the footer, update only the footer's new-card/ID totals, and read it back. Audit C1–C20 with specific evidence (C17–C20 apply to mini-log-7 cards). Preserve every earlier issued block.

For a duplicate or late-news correction, append a dated addendum; reforecast is NOT_PRIMARY and never changes the original grade. If writing is unavailable, return the complete updated mini as READ_ONLY_DRAFT / NOT_ISSUED and do not claim allocation.

Return the full new card, exact file path, working ID/status, timing and lead band, top two or no-forecast reason, baseline coverage, gate/joint/sensitivity summary, audit evidence and updated footer. Explicitly state settlement NOT_PERFORMED and GitHub writes NO (GitHub repo `main` branch referenced in read-only mode). Do not promise prediction success.

RUGBY LEAGUE / UNION
----------------------------

## 1. Read and establish authority

Read every control from one pinned commit of the GitHub repository (`main` branch) in read-only mode (`PUBLISHED_MAIN_PINNED`), or from the local working tree only in a `LOCAL_WORKING_TREE` run (CURRENT_RULES §0). Never mix the two. Print the [reading receipt](README.md) after opening CURRENT_STATE, METHOD, CURRENT_RULES, SELECTION_RULES, CARD_AND_LOG_TEMPLATES, RULES_NRL_RUGBY or RULES_RUGBY_UNION, LEAGUE_PROFILES (Rugby row), [SOURCES §3.6](../../SOURCES.md#36-nrl-and-rugby-league) (rugby league) or [§3.7](../../SOURCES.md#37-rugby-union) (rugby union), matching the code being played, ARCHIVE_USE_GUIDE, this prompt, the complete active mini, GAME_LOG_STATUS_CURRENT and relevant canonical event records. Record actual HEAD on `main`, working differences and time. Apply current controls over historical sport-engine notes.

If a required control or original mini is inaccessible, deliver a clearly labelled draft, not an issued append. Missing sporting data leads to explicit uncertainty or qualitative/NO_FORECAST research, not invented numbers.

## 2. Identity, duplicate and timing gate

Verify teams, competition (NRL, Super League, Rugby Championship, Six Nations, etc.), round/stage, venue, native ID, official scheduled kickoff, venue zone, UTC and Australia/Sydney time. Search every relevant local mini/carryover and canonical log body/status by ID, event key and aliases; doubleheaders and postponements need explicit identity handling. An existing event gets a dated addendum under its original ID, no new card.

For a new event, reconcile the mini's next working ID with current canonical state and outstanding local sequence. No gap, reservation, collision or renumbering. Record current source state before research and again immediately before write. Keep cutoff, research completion, actual issue and state-recheck times separate. If start is crossed, relabel honestly; exposure to live/final information prevents a clean pregame reconstruction. Retain requested late research in its separate cohort. Log the request in the mini's intake table (template §2-D) whatever its outcome. Confirm you hold the mini's issuing-writer lease and that the mini is not frozen for settlement; otherwise route the event to the next authorised mini (CURRENT_RULES §8). Follow the two-step issue window: research complete by about T−60, then freeze after the official lineup check, no later than T−5. Complete the mandatory availability search and final recheck first (CURRENT_RULES §5b; ROSTER_AVAILABILITY_PROTOCOL). If selections remain genuinely unpublished or unverified, record the exact side/field and completed attempts, then use supported scenarios or qualitative/NO_FORECAST research with the honest `LINEUP_UNCONFIRMED` label; do not claim an unperformed scheduled retry.

## 3. Evidence, team sheet and archive

**Availability research (AVAIL-2026.10.14-v1).** Read and apply [ROSTER_AVAILABILITY_PROTOCOL](../../ROSTER_AVAILABILITY_PROTOCOL.md) §§1–6 for both sides: exact starters/starting role, selected bench/replacements, current injuries/illness/suspensions/absences, and late changes. Complete its official match → both teams → eligibility/medical → permitted provider → local-language/obscure-competition escalation before reporting a missing field. Record actual searches, evidence/times and failures in the existing Evidence receipt/A3/A8; update the existing lineup-state metadata and audit C20. A roster, probable starter or predicted side is not confirmation. Recheck around the actual competition release window and immediately before freeze; re-price changed inputs. Never invent a healthy roster, bench or confirmation. If material gaps survive the full search, retain supported scenarios or qualitative/NO_FORECAST research with the exact reason. Do not read model-shadow or market material.

Follow official league match center → structured provider → quality corroboration routes. For each decisive claim retain URL, exact field/value or brief extract, source publication/update time when known, retrieval time and provenance/lineage. Log inaccessible/stale/conflicting sources. Three domains are not three independent collectors. No odds/tips/previews/fantasy inputs.

Verify team/bench/spine or halves/front row, kicking, possession/territory, discipline, workload and weather; probable is not confirmed. Inspect actual archive contents under `Previous Sports Results/Rugby/...` and print files, logical rows read, competition/stage filters, latest usable date and missingness. Use only results known before cutoff. Do not use postgame narrative or full-season aggregates from after cutoff.

**Form windows and known-at (PR-01, R28).**
- Print each side's (team or player) L5, L10, L15, L20, season to date and league level, from dated games before the cutoff, with the true n of each window: CARD_AND_LOG_TEMPLATES §3b, ARCHIVE_USE_GUIDE recipe R2.
- Use the archive where it holds the games; otherwise use a SOURCES route (ESPN team schedule, MLB statsapi, StatMuse, Tennis Abstract) and say which.
- Exclude archive rows flagged as duplicates, awarded results, forfeits or abandonments.
- The windows overlap and count as one piece of evidence. Only the shrunk L20/season rate may move the centre, as a listed adjustment with the unadjusted pair; the four-window recency blend is printed beside it for comparison.
- A short-window swing is width, not a lean, unless a named, current mechanism explains it.
- Print the archive capture date. An input whose availability before the cutoff cannot be shown is `KNOWN_AT_UNVERIFIED` and may not decide Rank 1.

## 4. Distribution, expected score and comparator

Build the simplest defensible coherent rugby distribution: model the appropriate score events (tries, conversions, penalties, field goals) and key margins; league and union scoring systems differ. Use only applicable measured regime effects; finals need not always reduce the mean. Print every parameter and its basis, formula/table, normalization, tail treatment, covariance and endpoint transitions. If the required calculation cannot be done, report a supported approximation with limitations, or qualitative research with NOT_ESTIMATED probabilities.

Produce expected score terms from CARD_AND_LOG_TEMPLATES §3a: team points, total, signed margin and supported SDs. Keep zeros; mark missing or irrelevant terms. Print all winner/draw/tie masses. For every candidate retain unconditional W/P/L/V and p_card=W/(W+L), with denominator and action convention.

Attempt BASELINE_LEAGUE_V1 on the same line/endpoint from league-only inputs, frozen before issue. Print recipe, source cohort/n/cutoff and parameters separately from the team model. No 0.5 placeholder or retrospective baseline fill. Missing baseline does not stop the card; it limits later skill measurement.

Show an adjustment table (venue, lineup, spine availability, rest/travel), unadjusted distribution/pair and low/base/high sensitivity on material uncertain inputs. Any adjustment-driven pair change is ADJUSTMENT_DEPENDENT, even below 0.25 SD. Report plausible probability ranges as sensitivity, not confidence intervals. Do not move individual probabilities outside the shared model.

**Pricing basis (PR-03).** When an input is labelled unfitted, stale, early-season or unconfirmed, the primary distribution is the declared mixture of its low/base/high cases (default weights 0.25/0.50/0.25, frozen before pricing). Print each row's `p_base` beside p_card. Compute at the precision actually used and print ε. A gate within ε of 0.62, or within 2ε of the 0.04 lead, is `GATE_UNRESOLVED_PRECISION`; rows within 2ε are a `PRECISION_TIE` (SELECTION_RULES §2). Apply any key-number, push or tie adjustment to the normalised common distribution, never to one row. Print each ranked row's line distance from centre (units and z, or N/A) and the card's baseline coverage, with an enumerated reason for each missing BASELINE_P (SELECTION_RULES §5, §9).

## 5. Candidate selection and dependence

Freeze the supported family/line-generation recipe before pricing (match winner, handicaps, totals, team totals). Price supplied rows and the declared derived universe; retain exclusions and unused supplied rows. Do not move thresholds repeatedly toward 90% to manufacture a strong gate. Values above the selection ceiling keep their true probabilities in the diagnostic appendix and are excluded, never capped.

Apply family eligibility and deterministic decreasing-p primary order from SELECTION_RULES. Show up to four supported rows, the first two as PICK. Fewer rows or qualitative/NO_FORECAST output is acceptable with the reason; unsupported rows are never padding. The best non-complementary gate alternative comes from the entire declared eligible universe, not a pruned four. Print original gate and RET03 shadow separately.

Freeze RET04 different-quantity and XCARD6 minimum-joint-failure shadow Rank 2 where calculable. Also freeze `SHADOW_RANK_DELTA` (top two by p_card − BASELINE_P) and, when the card is priced from a mixture, `SHADOW_BASE_ONLY` (SELECTION_RULES §3). Neither changes primary ordering. Print exact unconditional joint loss from common states, or honest Fréchet bounds. Label disjoint losing sets MECHANICALLY_PROTECTED; do not claim they improve skill or guarantee profit. Report both-decisive conditioning where pushes/voids exist.

## 6. Rugby playing conditions and rules

Distinguish Rugby League (NRL/SL: 80 mins, golden point in regular season vs extra time in finals) from Rugby Union (80 mins, regular season draw permitted, extra time in knockouts). Resolve draw/golden point/extra time per competition and endpoint.

## 7. Write, audit and return

Use CARD_AND_LOG_TEMPLATES §3 in the mini's own format; new minis use mini-log-7, and a mini-log-6 mini finishes in its own format. Keep the decision block concise and put full evidence/arithmetic in A1–A9. State exact settlement fields, definitions and capture plan. Write one card before the footer, update only the footer's new-card/ID totals, and read it back. Audit C1–C20 with specific evidence (C17–C20 apply to mini-log-7 cards). Preserve every earlier issued block.

For a duplicate or late-news correction, append a dated addendum; reforecast is NOT_PRIMARY and never changes the original grade. If writing is unavailable, return the complete updated mini as READ_ONLY_DRAFT / NOT_ISSUED and do not claim allocation.

Return the full new card, exact file path, working ID/status, timing and lead band, top two or no-forecast reason, baseline coverage, gate/joint/sensitivity summary, audit evidence and updated footer. Explicitly state settlement NOT_PERFORMED and GitHub writes NO (GitHub repo `main` branch referenced in read-only mode). Do not promise prediction success.

AFL / AFLW
----------------------------

## 1. Read and establish authority

Read every control from one pinned commit of the GitHub repository (`main` branch) in read-only mode (`PUBLISHED_MAIN_PINNED`), or from the local working tree only in a `LOCAL_WORKING_TREE` run (CURRENT_RULES §0). Never mix the two. Print the [reading receipt](README.md) after opening CURRENT_STATE, METHOD, CURRENT_RULES, SELECTION_RULES, CARD_AND_LOG_TEMPLATES, RULES_AFL, LEAGUE_PROFILES (AFL row), [SOURCES §3.5](../../SOURCES.md#35-afl-and-aflw) (AFL/AFLW routes), ARCHIVE_USE_GUIDE, this prompt, the complete active mini, GAME_LOG_STATUS_CURRENT and relevant canonical event records. Record actual HEAD on `main`, working differences and time. Apply current controls over historical sport-engine notes.

If a required control or original mini is inaccessible, deliver a clearly labelled draft, not an issued append. Missing sporting data leads to explicit uncertainty or qualitative/NO_FORECAST research, not invented numbers.

## 2. Identity, duplicate and timing gate

Verify clubs, competition (AFL men vs AFLW), round/finals stage, venue, native ID, official scheduled first bounce, venue zone, UTC and Australia/Sydney time. Search every relevant local mini/carryover and canonical log body/status by ID, event key and aliases; doubleheaders and postponements need explicit identity handling. An existing event gets a dated addendum under its original ID, no new card.

For a new event, reconcile the mini's next working ID with current canonical state and outstanding local sequence. No gap, reservation, collision or renumbering. Record current source state before research and again immediately before write. Keep cutoff, research completion, actual issue and state-recheck times separate. If start is crossed, relabel honestly; exposure to live/final information prevents a clean pregame reconstruction. Retain requested late research in its separate cohort. Log the request in the mini's intake table (template §2-D) whatever its outcome. Confirm you hold the mini's issuing-writer lease and that the mini is not frozen for settlement; otherwise route the event to the next authorised mini (CURRENT_RULES §8). Follow the two-step issue window: research complete by about T−60, then freeze after the official lineup check, no later than T−5. Complete the mandatory availability search and final recheck first (CURRENT_RULES §5b; ROSTER_AVAILABILITY_PROTOCOL). If selections remain genuinely unpublished or unverified, record the exact side/field and completed attempts, then use supported scenarios or qualitative/NO_FORECAST research with the honest `LINEUP_UNCONFIRMED` label; do not claim an unperformed scheduled retry.

## 3. Evidence, lineup and archive

**Availability research (AVAIL-2026.10.14-v1).** Read and apply [ROSTER_AVAILABILITY_PROTOCOL](../../ROSTER_AVAILABILITY_PROTOCOL.md) §§1–6 for both sides: exact starters/starting role, selected bench/replacements, current injuries/illness/suspensions/absences, and late changes. Complete its official match → both teams → eligibility/medical → permitted provider → local-language/obscure-competition escalation before reporting a missing field. Record actual searches, evidence/times and failures in the existing Evidence receipt/A3/A8; update the existing lineup-state metadata and audit C20. A roster, probable starter or predicted side is not confirmation. Recheck around the actual competition release window and immediately before freeze; re-price changed inputs. Never invent a healthy roster, bench or confirmation. If material gaps survive the full search, retain supported scenarios or qualitative/NO_FORECAST research with the exact reason. Do not read model-shadow or market material.

Follow official AFL match centre / AFLW app → structured provider → quality corroboration routes. For each decisive claim retain URL, exact field/value or brief extract, source publication/update time when known, retrieval time and provenance/lineage. Log inaccessible/stale/conflicting sources. Three domains are not three independent collectors. No odds/tips/previews/fantasy inputs.

Verify teams, ruck/midfield, clearances, inside-50/scoring-shot creation, conversion, defence, rest/venue/weather; probable is not confirmed. Inspect actual archive contents under `Previous Sports Results/Aussie Rules/...` and print files, logical rows read, competition/season filters, latest usable date and missingness. Use only results known before cutoff. Do not use postgame narrative or full-season aggregates from after cutoff.

**Form windows and known-at (PR-01, R28).**
- Print each side's (team or player) L5, L10, L15, L20, season to date and league level, from dated games before the cutoff, with the true n of each window: CARD_AND_LOG_TEMPLATES §3b, ARCHIVE_USE_GUIDE recipe R2.
- Use the archive where it holds the games; otherwise use a SOURCES route (ESPN team schedule, MLB statsapi, StatMuse, Tennis Abstract) and say which.
- Exclude archive rows flagged as duplicates, awarded results, forfeits or abandonments.
- The windows overlap and count as one piece of evidence. Only the shrunk L20/season rate may move the centre, as a listed adjustment with the unadjusted pair; the four-window recency blend is printed beside it for comparison.
- A short-window swing is width, not a lean, unless a named, current mechanism explains it.
- Print the archive capture date. An input whose availability before the cutoff cannot be shown is `KNOWN_AT_UNVERIFIED` and may not decide Rank 1.

## 4. Distribution, expected score and comparator

Build the simplest defensible coherent Australian rules distribution: separate shots from accuracy; points = 6 × goals + behinds. Use competition-specific pace/length and draw/finals rules. Explain shrinkage of unusual conversion rather than assuming a rebound. Print every parameter and its basis, formula/table, normalization, tail treatment, covariance and endpoint transitions. If the required calculation cannot be done, report a supported approximation with limitations, or qualitative research with NOT_ESTIMATED probabilities.

Produce expected score terms from CARD_AND_LOG_TEMPLATES §3a: goals, behinds, team points (means & SDs), total points, signed margin and supported SDs for the correct competition. Keep zeros; mark missing or irrelevant terms. Print all winner/draw/tie masses. For every candidate retain unconditional W/P/L/V and p_card=W/(W+L), with denominator and action convention.

Attempt BASELINE_LEAGUE_V1 on the same line/endpoint from league-only inputs, frozen before issue. Print recipe, source cohort/n/cutoff and parameters separately from the team model. No 0.5 placeholder or retrospective baseline fill. Missing baseline does not stop the card; it limits later skill measurement.

Show an adjustment table (venue, rest, weather/wind, ruck/midfield matchups), unadjusted distribution/pair and low/base/high sensitivity on material uncertain inputs. Any adjustment-driven pair change is ADJUSTMENT_DEPENDENT, even below 0.25 SD. Report plausible probability ranges as sensitivity, not confidence intervals. Do not move individual probabilities outside the shared model.

**Pricing basis (PR-03).** When an input is labelled unfitted, stale, early-season or unconfirmed, the primary distribution is the declared mixture of its low/base/high cases (default weights 0.25/0.50/0.25, frozen before pricing). Print each row's `p_base` beside p_card. Compute at the precision actually used and print ε. A gate within ε of 0.62, or within 2ε of the 0.04 lead, is `GATE_UNRESOLVED_PRECISION`; rows within 2ε are a `PRECISION_TIE` (SELECTION_RULES §2). Apply any key-number, push or tie adjustment to the normalised common distribution, never to one row. Print each ranked row's line distance from centre (units and z, or N/A) and the card's baseline coverage, with an enumerated reason for each missing BASELINE_P (SELECTION_RULES §5, §9).

## 5. Candidate selection and dependence

Freeze the supported family/line-generation recipe before pricing (head-to-head, lines/handicaps, match totals, team totals). Price supplied rows and the declared derived universe; retain exclusions and unused supplied rows. Do not move thresholds repeatedly toward 90% to manufacture a strong gate. Values above the selection ceiling keep their true probabilities in the diagnostic appendix and are excluded, never capped.

Apply family eligibility and deterministic decreasing-p primary order from SELECTION_RULES. Show up to four supported rows, the first two as PICK. Fewer rows or qualitative/NO_FORECAST output is acceptable with the reason; unsupported rows are never padding. The best non-complementary gate alternative comes from the entire declared eligible universe, not a pruned four. Print original gate and RET03 shadow separately.

Freeze RET04 different-quantity and XCARD6 minimum-joint-failure shadow Rank 2 where calculable. Also freeze `SHADOW_RANK_DELTA` (top two by p_card − BASELINE_P) and, when the card is priced from a mixture, `SHADOW_BASE_ONLY` (SELECTION_RULES §3). Neither changes primary ordering. Print exact unconditional joint loss from common states, or honest Fréchet bounds. Label disjoint losing sets MECHANICALLY_PROTECTED; do not claim they improve skill or guarantee profit. Report both-decisive conditioning where pushes/voids exist.

## 6. AFL/AFLW playing conditions and rules

Verify competition-specific pace and match duration: AFL men (four 20-min quarters + time-on) vs AFLW (four 15–17-min quarters). Confirm draw/finals rules (draw allowed in regular season; extra time in finals).

## 7. Write, audit and return

Use CARD_AND_LOG_TEMPLATES §3 in the mini's own format; new minis use mini-log-7, and a mini-log-6 mini finishes in its own format. Keep the decision block concise and put full evidence/arithmetic in A1–A9. State exact settlement fields, definitions and capture plan. Write one card before the footer, update only the footer's new-card/ID totals, and read it back. Audit C1–C20 with specific evidence (C17–C20 apply to mini-log-7 cards). Preserve every earlier issued block.

For a duplicate or late-news correction, append a dated addendum; reforecast is NOT_PRIMARY and never changes the original grade. If writing is unavailable, return the complete updated mini as READ_ONLY_DRAFT / NOT_ISSUED and do not claim allocation.

Return the full new card, exact file path, working ID/status, timing and lead band, top two or no-forecast reason, baseline coverage, gate/joint/sensitivity summary, audit evidence and updated footer. Explicitly state settlement NOT_PERFORMED and GitHub writes NO (GitHub repo `main` branch referenced in read-only mode). Do not promise prediction success.

AMERICAN FOOTBALL
----------------------------

## 1. Read and establish authority

Read every control from one pinned commit of the GitHub repository (`main` branch) in read-only mode (`PUBLISHED_MAIN_PINNED`), or from the local working tree only in a `LOCAL_WORKING_TREE` run (CURRENT_RULES §0). Never mix the two. Print the [reading receipt](README.md) after opening CURRENT_STATE, METHOD, CURRENT_RULES, SELECTION_RULES, CARD_AND_LOG_TEMPLATES, RULES_AMERICAN_FOOTBALL, LEAGUE_PROFILES (NFL row), [SOURCES §3.8](../../SOURCES.md#38-nfl-and-college-football) (NFL and college football routes), ARCHIVE_USE_GUIDE, this prompt, the complete active mini, GAME_LOG_STATUS_CURRENT and relevant canonical event records. Record actual HEAD on `main`, working differences and time. Apply current controls over historical sport-engine notes.

If a required control or original mini is inaccessible, deliver a clearly labelled draft, not an issued append. Missing sporting data leads to explicit uncertainty or qualitative/NO_FORECAST research, not invented numbers.

## 2. Identity, duplicate and timing gate

Verify teams, league/competition (NFL, college/NCAA, etc.), week, venue, native ID, official scheduled kickoff, venue zone, UTC and Australia/Sydney time. Search every relevant local mini/carryover and canonical log body/status by ID, event key and aliases; doubleheaders and postponements need explicit identity handling. An existing event gets a dated addendum under its original ID, no new card.

For a new event, reconcile the mini's next working ID with current canonical state and outstanding local sequence. No gap, reservation, collision or renumbering. Record current source state before research and again immediately before write. Keep cutoff, research completion, actual issue and state-recheck times separate. If start is crossed, relabel honestly; exposure to live/final information prevents a clean pregame reconstruction. Retain requested late research in its separate cohort. Log the request in the mini's intake table (template §2-D) whatever its outcome. Confirm you hold the mini's issuing-writer lease and that the mini is not frozen for settlement; otherwise route the event to the next authorised mini (CURRENT_RULES §8). Follow the two-step issue window: research complete by about T−60, then freeze after the official lineup check, no later than T−5. Complete the mandatory availability search and final recheck first (CURRENT_RULES §5b; ROSTER_AVAILABILITY_PROTOCOL). If selections remain genuinely unpublished or unverified, record the exact side/field and completed attempts, then use supported scenarios or qualitative/NO_FORECAST research with the honest `LINEUP_UNCONFIRMED` label; do not claim an unperformed scheduled retry.

## 3. Evidence, inactives and archive

**Availability research (AVAIL-2026.10.14-v1).** Read and apply [ROSTER_AVAILABILITY_PROTOCOL](../../ROSTER_AVAILABILITY_PROTOCOL.md) §§1–6 for both sides: exact starters/starting role, selected bench/replacements, current injuries/illness/suspensions/absences, and late changes. Complete its official match → both teams → eligibility/medical → permitted provider → local-language/obscure-competition escalation before reporting a missing field. Record actual searches, evidence/times and failures in the existing Evidence receipt/A3/A8; update the existing lineup-state metadata and audit C20. A roster, probable starter or predicted side is not confirmation. Recheck around the actual competition release window and immediately before freeze; re-price changed inputs. Never invent a healthy roster, bench or confirmation. If material gaps survive the full search, retain supported scenarios or qualitative/NO_FORECAST research with the exact reason. Do not read model-shadow or market material.

Follow official NFL Game Center / college box score → structured provider → quality corroboration routes. For each decisive claim retain URL, exact field/value or brief extract, source publication/update time when known, retrieval time and provenance/lineage. Log inaccessible/stale/conflicting sources. Three domains are not three independent collectors. No odds/tips/previews/fantasy inputs.

Verify QB, line/skill/defensive availability, 90-minute pregame inactives list, efficiency, drive/play pace, pressure, special teams, rest/weather; probable is not confirmed. Inspect actual archive contents under `Previous Sports Results/American Football/<league>/...` and print files, logical rows read, season/week filters, latest usable date and missingness. Use only results known before cutoff. Do not use postgame narrative or full-season aggregates from after cutoff.

**Form windows and known-at (PR-01, R28).**
- Print each side's (team or player) L5, L10, L15, L20, season to date and league level, from dated games before the cutoff, with the true n of each window: CARD_AND_LOG_TEMPLATES §3b, ARCHIVE_USE_GUIDE recipe R2.
- Use the archive where it holds the games; otherwise use a SOURCES route (ESPN team schedule, MLB statsapi, StatMuse, Tennis Abstract) and say which.
- Exclude archive rows flagged as duplicates, awarded results, forfeits or abandonments.
- The windows overlap and count as one piece of evidence. Only the shrunk L20/season rate may move the centre, as a listed adjustment with the unadjusted pair; the four-window recency blend is printed beside it for comparison.
- A short-window swing is width, not a lean, unless a named, current mechanism explains it.
- Print the archive capture date. An input whose availability before the cutoff cannot be shown is `KNOWN_AT_UNVERIFIED` and may not decide Rank 1.

## 4. Distribution, expected score and comparator

Build the simplest defensible coherent football distribution: use supported discrete score/drive structure or disclose an approximation; show push/key-margin mass near 3/7 and other relevant numbers. No claim to an exact drive model without its calculation. Print every parameter and its basis, formula/table, normalization, tail treatment, covariance and endpoint transitions. If the required calculation cannot be done, report a supported approximation with limitations, or qualitative research with NOT_ESTIMATED probabilities.

Produce expected score terms from CARD_AND_LOG_TEMPLATES §3a: team points, total, signed margin and supported SDs. Keep zeros; mark missing or irrelevant terms. Print all winner/draw/tie masses. For every candidate retain unconditional W/P/L/V and p_card=W/(W+L), with denominator and action convention.

Attempt BASELINE_LEAGUE_V1 on the same line/endpoint from league-only inputs, frozen before issue. Print recipe, source cohort/n/cutoff and parameters separately from the team model. No 0.5 placeholder or retrospective baseline fill. Missing baseline does not stop the card; it limits later skill measurement.

Show an adjustment table (QB/injuries, rest, weather/wind), unadjusted distribution/pair and low/base/high sensitivity on material uncertain inputs. Any adjustment-driven pair change is ADJUSTMENT_DEPENDENT, even below 0.25 SD. Report plausible probability ranges as sensitivity, not confidence intervals. Do not move individual probabilities outside the shared model.

**Pricing basis (PR-03).** When an input is labelled unfitted, stale, early-season or unconfirmed, the primary distribution is the declared mixture of its low/base/high cases (default weights 0.25/0.50/0.25, frozen before pricing). Print each row's `p_base` beside p_card. Compute at the precision actually used and print ε. A gate within ε of 0.62, or within 2ε of the 0.04 lead, is `GATE_UNRESOLVED_PRECISION`; rows within 2ε are a `PRECISION_TIE` (SELECTION_RULES §2). Apply any key-number, push or tie adjustment to the normalised common distribution, never to one row. Print each ranked row's line distance from centre (units and z, or N/A) and the card's baseline coverage, with an enumerated reason for each missing BASELINE_P (SELECTION_RULES §5, §9).

## 5. Candidate selection and dependence

Freeze the supported family/line-generation recipe before pricing (point spreads, game totals, team totals, moneyline). Price supplied rows and the declared derived universe; retain exclusions and unused supplied rows. Do not move thresholds repeatedly toward 90% to manufacture a strong gate. Values above the selection ceiling keep their true probabilities in the diagnostic appendix and are excluded, never capped.

Apply family eligibility and deterministic decreasing-p primary order from SELECTION_RULES. Show up to four supported rows, the first two as PICK. Fewer rows or qualitative/NO_FORECAST output is acceptable with the reason; unsupported rows are never padding. The best non-complementary gate alternative comes from the entire declared eligible universe, not a pruned four. Print original gate and RET03 shadow separately.

Freeze RET04 different-quantity and XCARD6 minimum-joint-failure shadow Rank 2 where calculable. Also freeze `SHADOW_RANK_DELTA` (top two by p_card − BASELINE_P) and, when the card is priced from a mixture, `SHADOW_BASE_ONLY` (SELECTION_RULES §3). Neither changes primary ordering. Print exact unconditional joint loss from common states, or honest Fréchet bounds. Label disjoint losing sets MECHANICALLY_PROTECTED; do not claim they improve skill or guarantee profit. Report both-decisive conditioning where pushes/voids exist.

## 6. American football playing conditions and rules

Verify competition-specific rules: NFL regular season (10-min modified sudden-death OT; ties permitted) vs NFL postseason (both teams guaranteed possession) vs NCAA college football (un-timed alternating overtime possessions). Overtime and tie rules differ by competition level and season.

## 7. Write, audit and return

Use CARD_AND_LOG_TEMPLATES §3 in the mini's own format; new minis use mini-log-7, and a mini-log-6 mini finishes in its own format. Keep the decision block concise and put full evidence/arithmetic in A1–A9. State exact settlement fields, definitions and capture plan. Write one card before the footer, update only the footer's new-card/ID totals, and read it back. Audit C1–C20 with specific evidence (C17–C20 apply to mini-log-7 cards). Preserve every earlier issued block.

For a duplicate or late-news correction, append a dated addendum; reforecast is NOT_PRIMARY and never changes the original grade. If writing is unavailable, return the complete updated mini as READ_ONLY_DRAFT / NOT_ISSUED and do not claim allocation.

Return the full new card, exact file path, working ID/status, timing and lead band, top two or no-forecast reason, baseline coverage, gate/joint/sensitivity summary, audit evidence and updated footer. Explicitly state settlement NOT_PERFORMED and GitHub writes NO (GitHub repo `main` branch referenced in read-only mode). Do not promise prediction success.

OTHER SPORTS
----------------------------

## 1. Read and establish authority

Read every control from one pinned commit of the GitHub repository (`main` branch) in read-only mode (`PUBLISHED_MAIN_PINNED`), or from the local working tree only in a `LOCAL_WORKING_TREE` run (CURRENT_RULES §0). Never mix the two. Print the [reading receipt](README.md) after opening CURRENT_STATE, METHOD, CURRENT_RULES, SELECTION_RULES, CARD_AND_LOG_TEMPLATES, applicable sport rule file if present, SOURCES (the sport's §3 section if one exists, otherwise §2 and the [§3.11](../../SOURCES.md#311-field-fallback-and-official-social-use-by-sport) fallback rules), ARCHIVE_USE_GUIDE, this prompt, the complete active mini, GAME_LOG_STATUS_CURRENT and relevant canonical event records. Record actual HEAD on `main`, working differences and time. Apply current controls over historical sport-engine notes.

If a required control or original mini is inaccessible, deliver a clearly labelled draft, not an issued append. Missing sporting data leads to explicit uncertainty or qualitative/NO_FORECAST research, not invented numbers.

## 2. Identity, duplicate and timing gate

Verify participants, competition, season, stage, venue, native ID, official scheduled start, venue zone, UTC and Australia/Sydney time. Search every relevant local mini/carryover and canonical log body/status by ID, event key and aliases; doubleheaders and postponements need explicit identity handling. An existing event gets a dated addendum under its original ID, no new card.

For a new event, reconcile the mini's next working ID with current canonical state and outstanding local sequence. No gap, reservation, collision or renumbering. Record current source state before research and again immediately before write. Keep cutoff, research completion, actual issue and state-recheck times separate. If start is crossed, relabel honestly; exposure to live/final information prevents a clean pregame reconstruction. Retain requested late research in its separate cohort. Log the request in the mini's intake table (template §2-D) whatever its outcome. Confirm you hold the mini's issuing-writer lease and that the mini is not frozen for settlement; otherwise route the event to the next authorised mini (CURRENT_RULES §8). Follow the two-step issue window: research complete by about T−60, then freeze after the official lineup check, no later than T−5. Complete the mandatory availability search and final recheck first (CURRENT_RULES §5b; ROSTER_AVAILABILITY_PROTOCOL). If selections remain genuinely unpublished or unverified, record the exact side/field and completed attempts, then use supported scenarios or qualitative/NO_FORECAST research with the honest `LINEUP_UNCONFIRMED` label; do not claim an unperformed scheduled retry.

## 3. Evidence and archive

**Availability research (AVAIL-2026.10.14-v1).** Read and apply [ROSTER_AVAILABILITY_PROTOCOL](../../ROSTER_AVAILABILITY_PROTOCOL.md) §§1–6 for both sides: exact starters/starting role, selected bench/replacements, current injuries/illness/suspensions/absences, and late changes. Complete its official match → both teams → eligibility/medical → permitted provider → local-language/obscure-competition escalation before reporting a missing field. Record actual searches, evidence/times and failures in the existing Evidence receipt/A3/A8; update the existing lineup-state metadata and audit C20. A roster, probable starter or predicted side is not confirmation. Recheck around the actual competition release window and immediately before freeze; re-price changed inputs. Never invent a healthy roster, bench or confirmation. If material gaps survive the full search, retain supported scenarios or qualitative/NO_FORECAST research with the exact reason. Do not read model-shadow or market material.

Follow official governing body / field owner match center → structured providers → quality corroboration routes. For each decisive claim retain URL, exact field/value or brief extract, source publication/update time when known, retrieval time and provenance/lineage. Log inaccessible/stale/conflicting sources. Three domains are not three independent collectors. No odds/tips/previews/fantasy inputs.

Verify confirmed participant readiness, lineups and availability; probable is not confirmed. Inspect archive if available. If sources cannot support an authoritative model, use UNCALIBRATED_QUALITATIVE or NO_FORECAST.

**Form windows and known-at (PR-01, R28).**
- Print each side's (team or player) L5, L10, L15, L20, season to date and league level, from dated games before the cutoff, with the true n of each window: CARD_AND_LOG_TEMPLATES §3b, ARCHIVE_USE_GUIDE recipe R2.
- Use the archive where it holds the games; otherwise use a SOURCES route (ESPN team schedule, MLB statsapi, StatMuse, Tennis Abstract) and say which.
- Exclude archive rows flagged as duplicates, awarded results, forfeits or abandonments.
- The windows overlap and count as one piece of evidence. Only the shrunk L20/season rate may move the centre, as a listed adjustment with the unadjusted pair; the four-window recency blend is printed beside it for comparison.
- A short-window swing is width, not a lean, unless a named, current mechanism explains it.
- Print the archive capture date. An input whose availability before the cutoff cannot be shown is `KNOWN_AT_UNVERIFIED` and may not decide Rank 1.

## 4. Distribution, expected score and comparator

Build the simplest defensible coherent sport distribution you can actually compute. Print every parameter and its basis, formula/table, normalization, tail treatment, covariance and endpoint transitions. If the required calculation cannot be done, report a supported approximation with limitations, or qualitative research with NOT_ESTIMATED probabilities.

Produce expected score terms from CARD_AND_LOG_TEMPLATES §3a where supported; otherwise mark NOT_COMPUTED. Keep zeros; mark missing or irrelevant terms. Print all winner/draw/tie masses. For every candidate retain unconditional W/P/L/V and p_card=W/(W+L), with denominator and action convention.

Attempt BASELINE_LEAGUE_V1 if league data exists. Show sensitivity on material uncertain inputs. Report plausible probability ranges as sensitivity, not confidence intervals. Do not move individual probabilities outside the shared model.

**Pricing basis (PR-03).** When an input is labelled unfitted, stale, early-season or unconfirmed, the primary distribution is the declared mixture of its low/base/high cases (default weights 0.25/0.50/0.25, frozen before pricing). Print each row's `p_base` beside p_card. Compute at the precision actually used and print ε. A gate within ε of 0.62, or within 2ε of the 0.04 lead, is `GATE_UNRESOLVED_PRECISION`; rows within 2ε are a `PRECISION_TIE` (SELECTION_RULES §2). Apply any key-number, push or tie adjustment to the normalised common distribution, never to one row. Print each ranked row's line distance from centre (units and z, or N/A) and the card's baseline coverage, with an enumerated reason for each missing BASELINE_P (SELECTION_RULES §5, §9).

## 5. Candidate selection and dependence

Freeze the supported family/line-generation recipe before pricing. Price supplied rows and the declared derived universe; retain exclusions and unused supplied rows. Values above the selection ceiling keep their true probabilities in the diagnostic appendix and are excluded, never capped.

Apply family eligibility and deterministic decreasing-p primary order from SELECTION_RULES. Show up to four supported rows, the first two as PICK. Fewer rows or qualitative/NO_FORECAST output is acceptable with the reason; unsupported rows are never padding. The best non-complementary gate alternative comes from the entire declared eligible universe, not a pruned four. Print original gate and RET03 shadow separately.

Freeze RET04 different-quantity and XCARD6 minimum-joint-failure shadow Rank 2 where calculable. Also freeze `SHADOW_RANK_DELTA` (top two by p_card − BASELINE_P) and, when the card is priced from a mixture, `SHADOW_BASE_ONLY` (SELECTION_RULES §3). Neither changes primary ordering. Print exact unconditional joint loss from common states, or honest Fréchet bounds. Label disjoint losing sets MECHANICALLY_PROTECTED; do not claim they improve skill or guarantee profit. Report both-decisive conditioning where pushes/voids exist.

## 6. General sport playing conditions and rules

Verify exact competition conditions, regulation duration, tiebreak/overtime rules, and abandonment rules. Do not borrow a model from an unrelated sport whose endpoint does not fit.

## 7. Write, audit and return

Use CARD_AND_LOG_TEMPLATES §3 in the mini's own format; new minis use mini-log-7, and a mini-log-6 mini finishes in its own format. Keep the decision block concise and put full evidence/arithmetic in A1–A9. State exact settlement fields, definitions and capture plan. Write one card before the footer, update only the footer's new-card/ID totals, and read it back. Audit C1–C20 with specific evidence (C17–C20 apply to mini-log-7 cards). Preserve every earlier issued block.

For a duplicate or late-news correction, append a dated addendum; reforecast is NOT_PRIMARY and never changes the original grade. If writing is unavailable, return the complete updated mini as READ_ONLY_DRAFT / NOT_ISSUED and do not claim allocation.

Return the full new card, exact file path, working ID/status, timing and lead band, top two or no-forecast reason, baseline coverage, gate/joint/sensitivity summary, audit evidence and updated footer. Explicitly state settlement NOT_PERFORMED and GitHub writes NO (GitHub repo `main` branch referenced in read-only mode). Do not promise prediction success.
