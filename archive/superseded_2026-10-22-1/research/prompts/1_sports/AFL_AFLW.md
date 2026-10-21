# PROMPT 1 — sport file: AFL / AFLW

**P-2026.10.17-v22.2 · prompt 1 sport file.** Use this file together with the [prompt 1 core](../1_GAME_CARD.md): read the core first, then this file. The core holds every rule shared by all sports, including the shared rules of steps 1, 3, 4, 5 and 7; this file holds this sport's own instructions for steps 1–7. At each step apply the core's shared rules for that step together with this file's. Fill in the Upcoming game block below; it is the only part the owner edits. Do not read the other sport files.

AFL / AFLW
----------------------------

## Upcoming game — AFL / AFLW

**Inactive template:** run only when the user fills or explicitly invokes this sport’s event. Empty examples allocate no ID and trigger no forecast.

- Event / official link: <participants and exact game identity>
- Competition details: <Exact men’s/women’s/regional competition / stage; teams; selected side/interchange/emergencies and late changes.>
- Scheduled start: <local date/time, venue timezone; verify UTC and Australia/Sydney>
- Active local mini: <exact path>
- Supplied contracts: <copy every exact proposition/line/period/action term, or NONE>
- Research constraints: <actual request; only-confirmed issuance if expressly required>

Read [COMMON_OPERATING_PROTOCOL](../COMMON_OPERATING_PROTOCOL.md), [MINI_LOG_IDENTITY_PROTOCOL](../../../MINI_LOG_IDENTITY_PROTOCOL.md) and the complete seven-step sport workflow below. The primary card is ANALYST_PRIMARY_V1: researched and priced by hand under NOCODE-v1 (prompt header). No model, runtime, shadow or decision-lab output is read or used; ML/RL belongs to prompts 6 and 8.

Also apply the core's **Before step 1 — evidence standard** ([prompt 1 core](../1_GAME_CARD.md)).

## 1. Read and establish authority

Also apply the core's **Step 1 — Read and establish authority** shared rules ([prompt 1 core](../1_GAME_CARD.md)).

Read COMMON_OPERATING_PROTOCOL and every control from the latest commit of the GitHub repository's `main` branch, pinned by its full SHA for the run, in read-only mode (`PUBLISHED_MAIN_PINNED`) (EXTERNAL_CHAT); this prompt never uses local controls. Print the [reading receipt](../README.md) after opening CURRENT_STATE, METHOD, CURRENT_RULES, SELECTION_RULES, CARD_AND_LOG_TEMPLATES, RULES_AFL, LEAGUE_PROFILES (current admission; independently source the exact competition online), [SOURCES §3.5](../../../SOURCES.md#35-afl-and-aflw) (AFL/AFLW routes), ARCHIVE_USE_GUIDE, this prompt, the complete active mini, GAME_LOG_STATUS_CURRENT and relevant canonical event records. Read them within the ENV-v1 reading budget (named sections of large files; only this sport's workflow) and record the latest `main` SHA, exactly what was read and the read time. Apply current controls over historical sport-engine notes.

## 2. Identity, duplicate and timing gate

Verify clubs, competition (AFL men vs AFLW), round/finals stage, venue, native ID, official scheduled first bounce, venue zone, UTC and Australia/Sydney time. Search every relevant local mini/carryover and canonical log body/status by ID, event key and aliases; doubleheaders and postponements need explicit identity handling. An existing event gets a dated addendum under its original local key or verified existing canonical reference, no new card or canonical assignment.

For a new event, use the mini's next stable LOCAL-<MINI_KEY>-G0001-style event key under MINI_LOG_IDENTITY_PROTOCOL; set canonical ID NOT_ASSIGNED / PROMPT_4_IMPORT. Do not assign, reserve, forecast or advance a P-ID during research. Read canonical state only for duplicate/context checks; canonical allocation happens in prompt 4. Record current source state before research and again immediately before write. Keep cutoff, research completion, actual issue and state-recheck times separate. Continue until research is complete even if play starts. Keep actual issue phase and input evidence separate: independently proved pre-start fields with no outcome exposure may be CLEAN_PRE_START_INPUTS / POST_START_ISSUE, scored in its own research cohort; it is not a pre-start-issued prospective forecast. Live/final exposure or unverified known-at facts prevent the clean-input claim. Apply [TIMING_RESEARCH_PROTOCOL](../../../TIMING_RESEARCH_PROTOCOL.md), with no minimum lead or forced early freeze. Log the request in the mini's intake table (template §2-D) whatever its outcome. Confirm you hold the mini's issuing-writer lease and that the mini is not frozen for settlement; otherwise route the event to the next authorised mini (CURRENT_RULES §8). Follow [TIMING_RESEARCH_PROTOCOL](../../../TIMING_RESEARCH_PROTOCOL.md): complete research without a countdown deadline, even after start; freeze only the completed issued original. Complete the mandatory availability search and final recheck first (CURRENT_RULES §5b; ROSTER_AVAILABILITY_PROTOCOL). If selections remain genuinely unpublished or unverified, record the exact side/field and completed attempts, then use supported scenarios or qualitative/NO_FORECAST research with the honest `LINEUP_UNCONFIRMED` label; do not claim an unperformed scheduled retry.

## 3. Evidence, lineup and online history

Also apply the core's **Step 3 — Evidence, line-ups and online history** shared rules ([prompt 1 core](../1_GAME_CARD.md)).

**Availability research (AVAIL-2026.10.16-v4).** Read and apply [ROSTER_AVAILABILITY_PROTOCOL](../../../ROSTER_AVAILABILITY_PROTOCOL.md) §§1–6 for both sides: exact starters/starting role, selected bench/replacements, current injuries/illness/suspensions/absences, and late changes. Complete its official match → both teams → eligibility/medical → permitted provider → local-language/obscure-competition escalation before reporting a missing field. Record actual searches, evidence/times and failures in the existing Evidence receipt/A3/A8; update the existing lineup-state metadata and audit C20. A roster, probable starter or predicted side is not confirmation. Recheck around the actual competition release window and immediately before freeze; re-price changed inputs. Never invent a healthy roster, bench or confirmation. If material gaps survive the full search, retain supported scenarios or qualitative/NO_FORECAST research with the exact reason. Model output and market/decision-lab material are never read.

Follow official AFL match centre / AFLW app → structured provider → quality corroboration routes. For each decisive claim retain URL, exact field/value or brief extract, source publication/update time when known, retrieval time and provenance/lineage. Log inaccessible/stale/conflicting sources. Three domains are not three independent collectors. No odds/tips/previews/fantasy inputs.

Verify teams, ruck/midfield, clearances, inside-50/scoring-shot creation, conversion, defence, rest/venue/weather; probable is not confirmed. Research the exact competition's prior games online under HISTORICAL_SOURCE_PROTOCOL and print source URLs, dated event rows, true window n, endpoint filters, latest usable date and missingness. Use only results known before cutoff. Do not use postgame narrative or full-season aggregates from after cutoff.

## 4. Distribution, expected score and comparator

Also apply the core's **Step 4 — Distribution, expected score and comparator** shared rules ([prompt 1 core](../1_GAME_CARD.md)).

Build the simplest defensible coherent Australian rules distribution: separate shots from accuracy; points = 6 × goals + behinds. Use competition-specific pace/length and draw/finals rules. Explain shrinkage of unusual conversion rather than assuming a rebound. Print every parameter and its basis, formula/table, normalization, tail treatment, covariance and endpoint transitions. If the required calculation cannot be done, report a supported approximation with limitations, or qualitative research with NOT_ESTIMATED probabilities. Hand method: PROBABILITY_TOOLKIT §1.

Produce expected score terms from CARD_AND_LOG_TEMPLATES §3a: goals, behinds, team points (means & SDs), total points, signed margin and supported SDs for the correct competition. Keep zeros; mark missing or irrelevant terms. Print all winner/draw/tie masses. For every candidate retain unconditional W/P/L/V and p_card=W/(W+L), with denominator and action convention.

Attempt BASELINE_LEAGUE_V1 on the same line/endpoint from league-only inputs, frozen before issue. Print recipe, source cohort/n/cutoff and parameters separately from the team model. No 0.5 placeholder or retrospective baseline fill. Missing baseline does not stop the card; it limits later skill measurement.

Show an adjustment table (venue, rest, weather/wind, ruck/midfield matchups), unadjusted distribution/pair and low/base/high sensitivity on material uncertain inputs. Any adjustment-driven pair change is ADJUSTMENT_DEPENDENT, even below 0.25 SD. Report plausible probability ranges as sensitivity, not confidence intervals. Do not move individual probabilities outside the shared model.

## 5. Candidate selection and dependence

Also apply the core's **Step 5 — Candidate selection and dependence** shared rules ([prompt 1 core](../1_GAME_CARD.md)).

Freeze the supported family/line-generation recipe before pricing (head-to-head, lines/handicaps, match totals, team totals). Price supplied rows and the declared derived universe; retain exclusions and unused supplied rows. Do not move thresholds repeatedly toward 90% to manufacture a strong gate. Values above the selection ceiling keep their true probabilities in the diagnostic appendix and are excluded, never capped.

## 6. AFL/AFLW playing conditions and rules

Verify competition-specific pace and match duration: AFL men (four 20-min quarters + time-on) vs AFLW (four 15–17-min quarters). Confirm draw/finals rules (draw allowed in regular season; extra time in finals).

## 7. Write, audit and return

Also apply the core's **Step 7 — Write, audit and return** shared rules ([prompt 1 core](../1_GAME_CARD.md)).