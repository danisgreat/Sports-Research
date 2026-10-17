# PROMPT 1 — sport file: CRICKET

**P-2026.10.17-v22.2 · prompt 1 sport file.** Use this file together with the [prompt 1 core](../1_GAME_CARD.md): read the core first, then this file. The core holds every rule shared by all sports, including the shared rules of steps 1, 3, 4, 5 and 7; this file holds this sport's own instructions for steps 1–7. At each step apply the core's shared rules for that step together with this file's. Fill in the Upcoming game block below; it is the only part the owner edits. Do not read the other sport files.

CRICKET
----------------------------

## Upcoming game — CRICKET

- Competition details: <India vs West Indies, 4th T20 Match>
- Scheduled start: <12:30 AM AEDT, 15 October 2026 (can be delayed)>
- Supplied contracts: <West Indies 1st Innings Runs at end of 20 overs: Over/Under 200.5 Runs>, <West Indies 1st Innings Runs at end of Powerplay (6 overs): Over/Under 57.5 Runs>,
- Research constraints: <continue pre game research even if game starts, continue until research is properly done>

Read [COMMON_OPERATING_PROTOCOL](../COMMON_OPERATING_PROTOCOL.md), [MINI_LOG_IDENTITY_PROTOCOL](../../../MINI_LOG_IDENTITY_PROTOCOL.md) and the complete seven-step sport workflow below. The primary card is ANALYST_PRIMARY_V1: researched and priced by hand under NOCODE-v1 (prompt header). No model, runtime, shadow or decision-lab output is read or used; ML/RL belongs to prompts 6 and 8.

Also apply the core's **Before step 1 — evidence standard** ([prompt 1 core](../1_GAME_CARD.md)).

## 1. Read and establish authority

Also apply the core's **Step 1 — Read and establish authority** shared rules ([prompt 1 core](../1_GAME_CARD.md)).

Read COMMON_OPERATING_PROTOCOL and every control from the latest commit of the GitHub repository's `main` branch, pinned by its full SHA for the run, in read-only mode (`PUBLISHED_MAIN_PINNED`) (EXTERNAL_CHAT); this prompt never uses local controls. Print the [reading receipt](../README.md) after opening CURRENT_STATE, METHOD, CURRENT_RULES, SELECTION_RULES, CARD_AND_LOG_TEMPLATES, RULES_CRICKET, LEAGUE_RULES_CRICKET, [SOURCES §3.3](../../../SOURCES.md#33-cricket) (cricket routes), ARCHIVE_USE_GUIDE, BASE_RATES_REGISTER, this prompt, the complete active mini, GAME_LOG_STATUS_CURRENT and relevant canonical event records. Read them within the ENV-v1 reading budget (named sections of large files; only this sport's workflow) and record the latest `main` SHA, exactly what was read and the read time. Apply current controls over historical sport-engine notes.

## 2. Identity, duplicate and timing gate

Verify teams, competition/tournament, format (Test, ODI, T20, The Hundred), match number, venue, pitch conditions, scheduled start, weather forecast, reserve days, venue zone, UTC and Australia/Sydney time. Search every relevant local mini/carryover and canonical log body/status by ID, event key and aliases; doubleheaders and postponements need explicit identity handling. An existing event gets a dated addendum under its original local key or verified existing canonical reference, no new card or canonical assignment.

For a new event, use the mini's next stable LOCAL-<MINI_KEY>-G0001-style event key under MINI_LOG_IDENTITY_PROTOCOL; set canonical ID NOT_ASSIGNED / PROMPT_4_IMPORT. Do not assign, reserve, forecast or advance a P-ID during research. Read canonical state only for duplicate/context checks; canonical allocation happens in prompt 4. Record current source state before research and again immediately before write. Keep cutoff, research completion, actual issue and state-recheck times separate. Continue until research is complete even if play starts. Keep actual issue phase and input evidence separate: independently proved pre-start fields with no outcome exposure may be CLEAN_PRE_START_INPUTS / POST_START_ISSUE, scored in its own research cohort; it is not a pre-start-issued prospective forecast. Live/final exposure or unverified known-at facts prevent the clean-input claim. Apply [TIMING_RESEARCH_PROTOCOL](../../../TIMING_RESEARCH_PROTOCOL.md), with no minimum lead or forced early freeze. Log the request in the mini's intake table (template §2-D) whatever its outcome. Confirm you hold the mini's issuing-writer lease and that the mini is not frozen for settlement; otherwise route the event to the next authorised mini (CURRENT_RULES §8). Follow [TIMING_RESEARCH_PROTOCOL](../../../TIMING_RESEARCH_PROTOCOL.md): complete research without a countdown deadline, even after start; freeze only the completed issued original. Complete the mandatory availability search and final recheck first (CURRENT_RULES §5b; ROSTER_AVAILABILITY_PROTOCOL). If selections remain genuinely unpublished or unverified, record the exact side/field and completed attempts, then use supported scenarios or qualitative/NO_FORECAST research with the honest `LINEUP_UNCONFIRMED` label; do not claim an unperformed scheduled retry.

## 3. Evidence, XI and online history

Also apply the core's **Step 3 — Evidence, line-ups and online history** shared rules ([prompt 1 core](../1_GAME_CARD.md)).

**Availability research (AVAIL-2026.10.16-v4).** Read and apply [ROSTER_AVAILABILITY_PROTOCOL](../../../ROSTER_AVAILABILITY_PROTOCOL.md) §§1–6 for both sides: exact starters/starting role, selected bench/replacements, current injuries/illness/suspensions/absences, and late changes. Complete its official match → both teams → eligibility/medical → permitted provider → local-language/obscure-competition escalation before reporting a missing field. Record actual searches, evidence/times and failures in the existing Evidence receipt/A3/A8; update the existing lineup-state metadata and audit C20. A roster, probable starter or predicted side is not confirmation. Recheck around the actual competition release window and immediately before freeze; re-price changed inputs. Never invent a healthy roster, bench or confirmation. If material gaps survive the full search, retain supported scenarios or qualitative/NO_FORECAST research with the exact reason. Model output and market/decision-lab material are never read.

Follow official board/ICC match center → ESPNcricinfo/structured provider → quality corroboration routes. For each decisive claim retain URL, exact field/value or brief extract, source publication/update time when known, retrieval time and provenance/lineage. Log inaccessible/stale/conflicting sources. Three domains are not three independent collectors. No odds/tips/previews/fantasy inputs.

Confirm playing XI, toss result, batting order, bowling allocations/quotas, pitch report, weather/dew and rain resources; probable is not confirmed. Distinguish fact, historical estimate and analyst assumption. Research the exact competition's prior games online under HISTORICAL_SOURCE_PROTOCOL and print source URLs, dated event rows, true window n, endpoint filters, latest usable date and missingness. Use only results known before cutoff. Do not use postgame narrative or full-season aggregates from after cutoff.

## 4. Distribution, expected score and comparator

Also apply the core's **Step 4 — Distribution, expected score and comparator** shared rules ([prompt 1 core](../1_GAME_CARD.md)).

Build the simplest defensible coherent cricket distribution: model innings/phase/wicket dependence with explicit toss and rain branches. Account for chase dynamics: a chase ends on the winning delivery and can legally overshoot the target; do not simply cap every total at the target. Print every parameter and its basis, formula/table, normalization, tail treatment, covariance and endpoint transitions. If the required calculation cannot be done, report a supported approximation with limitations, or qualitative research with NOT_ESTIMATED probabilities. Hand method: PROBABILITY_TOOLKIT §7.

Produce expected score terms from CARD_AND_LOG_TEMPLATES §3a: format/innings-specific runs and wickets where supported (common cross-team margin is often N/A in chases). Keep zeros; mark missing or irrelevant terms. Print all winner/draw/tie masses. For every candidate retain unconditional W/P/L/V and p_card=W/(W+L), with denominator and action convention.

Attempt BASELINE_LEAGUE_V1 on the same line/endpoint from league-only inputs, frozen before issue. Print recipe, source cohort/n/cutoff and parameters separately from the team model. No 0.5 placeholder or retrospective baseline fill. Missing baseline does not stop the card; it limits later skill measurement.

Show an adjustment table (pitch, weather/rain, toss, XI selection), unadjusted distribution/pair and low/base/high sensitivity on material uncertain inputs. Any adjustment-driven pair change is ADJUSTMENT_DEPENDENT, even below 0.25 SD. Report plausible probability ranges as sensitivity, not confidence intervals. Do not move individual probabilities outside the shared model.

## 5. Candidate selection and dependence

Also apply the core's **Step 5 — Candidate selection and dependence** shared rules ([prompt 1 core](../1_GAME_CARD.md)).

Freeze the supported family/line-generation recipe before pricing (match winner, innings totals, phase runs, handicap). Price supplied rows and the declared derived universe; retain exclusions and unused supplied rows. Do not move thresholds repeatedly toward 90% to manufacture a strong gate. Values above the selection ceiling keep their true probabilities in the diagnostic appendix and are excluded, never capped.

## 6. Cricket playing conditions and rules

Confirm exact playing conditions: overs limit, powerplays, bowler maximum overs, DLS rain calculations, tie/super-over conventions, and draw/weather branches for multi-day matches. Ensure row endpoints match tie, super-over, DLS and no-result rules. Unsupported ball-by-ball calculation is not an exact simulation.

## 7. Write, audit and return

Also apply the core's **Step 7 — Write, audit and return** shared rules ([prompt 1 core](../1_GAME_CARD.md)).