# PROMPT 1 — sport file: ICE HOCKEY

**P-2026.10.17-v22.2 · prompt 1 sport file.** Use this file together with the [prompt 1 core](../1_GAME_CARD.md): read the core first, then this file. The core holds every rule shared by all sports, including the shared rules of steps 1, 3, 4, 5 and 7; this file holds this sport's own instructions for steps 1–7. At each step apply the core's shared rules for that step together with this file's. Fill in the Upcoming game block below; it is the only part the owner edits. Do not read the other sport files.

ICE HOCKEY
----------------------------

## Upcoming game — ICE HOCKEY

- Competition details: <>
- Scheduled start: <local date/time, venue timezone; verify UTC and Australia/Sydney>
- Active local mini: <exact path>
- Supplied contracts: <copy every exact proposition/line/period/action term, or NONE>
- Research constraints: <actual request; only-confirmed issuance if expressly required>

Read [COMMON_OPERATING_PROTOCOL](../COMMON_OPERATING_PROTOCOL.md), [MINI_LOG_IDENTITY_PROTOCOL](../../../MINI_LOG_IDENTITY_PROTOCOL.md) and the complete seven-step sport workflow below. The primary card is ANALYST_PRIMARY_V1: researched and priced by hand under NOCODE-v1 (prompt header). No model, runtime, shadow or decision-lab output is read or used; ML/RL belongs to prompts 6 and 8.

Also apply the core's **Before step 1 — evidence standard** ([prompt 1 core](../1_GAME_CARD.md)).

## 1. Read and establish authority

Also apply the core's **Step 1 — Read and establish authority** shared rules ([prompt 1 core](../1_GAME_CARD.md)).

Read COMMON_OPERATING_PROTOCOL and every control from the latest commit of the GitHub repository's `main` branch, pinned by its full SHA for the run, in read-only mode (`PUBLISHED_MAIN_PINNED`) (EXTERNAL_CHAT); this prompt never uses local controls. Print the [reading receipt](../README.md) after opening CURRENT_STATE, METHOD, CURRENT_RULES, SELECTION_RULES, CARD_AND_LOG_TEMPLATES, RULES_ICE_HOCKEY, RULES_NHL (if applicable), LEAGUE_PROFILES (current admission; independently source the exact competition online), [SOURCES §3.9](../../../SOURCES.md#39-nhl) (NHL routes). For any other league, use [§3.13](../../../SOURCES.md#313-game-level-detail-results-line-ups-coaches-and-officials-tested-2026-09-30) (Liiga API, Elite Prospects), §3.29 (Danish Metal Ligaen), §3.31 (the Czech archive) or the league's own official site, and say which. An NHL route is never assumed to cover another league, ARCHIVE_USE_GUIDE, this prompt, the complete active mini, GAME_LOG_STATUS_CURRENT and relevant canonical event records. Read them within the ENV-v1 reading budget (named sections of large files; only this sport's workflow) and record the latest `main` SHA, exactly what was read and the read time. Apply current controls over historical sport-engine notes.

## 2. Identity, duplicate and timing gate

Verify teams, league (NHL, Tipsport Extraliga, Liiga, SHL, etc.), season, venue, native ID, official scheduled puck drop, venue zone, UTC and Australia/Sydney time. Search every relevant local mini/carryover and canonical log body/status by ID, event key and aliases; doubleheaders and postponements need explicit identity handling. An existing event gets a dated addendum under its original local key or verified existing canonical reference, no new card or canonical assignment.

For a new event, use the mini's next stable LOCAL-<MINI_KEY>-G0001-style event key under MINI_LOG_IDENTITY_PROTOCOL; set canonical ID NOT_ASSIGNED / PROMPT_4_IMPORT. Do not assign, reserve, forecast or advance a P-ID during research. Read canonical state only for duplicate/context checks; canonical allocation happens in prompt 4. Record current source state before research and again immediately before write. Keep cutoff, research completion, actual issue and state-recheck times separate. Continue until research is complete even if play starts. Keep actual issue phase and input evidence separate: independently proved pre-start fields with no outcome exposure may be CLEAN_PRE_START_INPUTS / POST_START_ISSUE, scored in its own research cohort; it is not a pre-start-issued prospective forecast. Live/final exposure or unverified known-at facts prevent the clean-input claim. Apply [TIMING_RESEARCH_PROTOCOL](../../../TIMING_RESEARCH_PROTOCOL.md), with no minimum lead or forced early freeze. Log the request in the mini's intake table (template §2-D) whatever its outcome. Confirm you hold the mini's issuing-writer lease and that the mini is not frozen for settlement; otherwise route the event to the next authorised mini (CURRENT_RULES §8). Follow [TIMING_RESEARCH_PROTOCOL](../../../TIMING_RESEARCH_PROTOCOL.md): complete research without a countdown deadline, even after start; freeze only the completed issued original. Complete the mandatory availability search and final recheck first (CURRENT_RULES §5b; ROSTER_AVAILABILITY_PROTOCOL). If selections remain genuinely unpublished or unverified, record the exact side/field and completed attempts, then use supported scenarios or qualitative/NO_FORECAST research with the honest `LINEUP_UNCONFIRMED` label; do not claim an unperformed scheduled retry.

## 3. Evidence, goalies and archive

Also apply the core's **Step 3 — Evidence, line-ups and online history** shared rules ([prompt 1 core](../1_GAME_CARD.md)).

**Availability research (AVAIL-2026.10.16-v4).** Read and apply [ROSTER_AVAILABILITY_PROTOCOL](../../../ROSTER_AVAILABILITY_PROTOCOL.md) §§1–6 for both sides: exact starters/starting role, selected bench/replacements, current injuries/illness/suspensions/absences, and late changes. Complete its official match → both teams → eligibility/medical → permitted provider → local-language/obscure-competition escalation before reporting a missing field. Record actual searches, evidence/times and failures in the existing Evidence receipt/A3/A8; update the existing lineup-state metadata and audit C20. A roster, probable starter or predicted side is not confirmation. Recheck around the actual competition release window and immediately before freeze; re-price changed inputs. Never invent a healthy roster, bench or confirmation. If material gaps survive the full search, retain supported scenarios or qualitative/NO_FORECAST research with the exact reason. Model output and market/decision-lab material are never read.

Follow official league game sheet / match reports → structured provider → quality corroboration routes. For each decisive claim retain URL, exact field/value or brief extract, source publication/update time when known, retrieval time and provenance/lineage. Log inaccessible/stale/conflicting sources. Three domains are not three independent collectors. No odds/tips/previews/fantasy inputs.

Confirm starting goalies or supported mixture, lines/scratches, special teams, rest and travel; probable is not confirmed. Unconfirmed goalie sensitivity must reach totals/ranks. Research the exact competition's prior games online under HISTORICAL_SOURCE_PROTOCOL and print source URLs, dated event rows, true window n, endpoint filters, latest usable date and missingness. Use only results known before cutoff. Do not use postgame narrative or full-season aggregates from after cutoff.

## 4. Distribution, expected score and comparator

Also apply the core's **Step 4 — Distribution, expected score and comparator** shared rules ([prompt 1 core](../1_GAME_CARD.md)).

Build the simplest defensible coherent ice hockey distribution: 5v5 creation/suppression, special teams, rest/travel, and explicit empty-net tails. Separate regulation draw from full-game OT/SO and final-score convention. Print directional handicap mass, not unconditional league absolute-margin frequency. Print every parameter and its basis, formula/table, normalization, tail treatment, covariance and endpoint transitions. If the required calculation cannot be done, report a supported approximation with limitations, or qualitative research with NOT_ESTIMATED probabilities. Hand method: PROBABILITY_TOOLKIT §2.

Produce expected score terms from CARD_AND_LOG_TEMPLATES §3a: regulation and/or full-game goals with OT/SO accounting, total, signed margin and supported SDs. Keep zeros; mark missing or irrelevant terms. Print all winner/draw/tie masses. For every candidate retain unconditional W/P/L/V and p_card=W/(W+L), with denominator and action convention.

Attempt BASELINE_LEAGUE_V1 on the same line/endpoint from league-only inputs, frozen before issue. Print recipe, source cohort/n/cutoff and parameters separately from the team model. No 0.5 placeholder or retrospective baseline fill. Missing baseline does not stop the card; it limits later skill measurement.

Show an adjustment table (goalie mixture, special teams, rest/travel), unadjusted distribution/pair and low/base/high sensitivity on material uncertain inputs. Any adjustment-driven pair change is ADJUSTMENT_DEPENDENT, even below 0.25 SD. Report plausible probability ranges as sensitivity, not confidence intervals. Do not move individual probabilities outside the shared model.

## 5. Candidate selection and dependence

Also apply the core's **Step 5 — Candidate selection and dependence** shared rules ([prompt 1 core](../1_GAME_CARD.md)).

Freeze the supported family/line-generation recipe before pricing (puck lines, full-game totals, regulation lines, team totals). Price supplied rows and the declared derived universe; retain exclusions and unused supplied rows. Do not move thresholds repeatedly toward 90% to manufacture a strong gate. Values above the selection ceiling keep their true probabilities in the diagnostic appendix and are excluded, never capped.

## 6. Ice hockey playing conditions and rules

Verify regulation 60 minutes vs regular-season 3-on-3 OT + shootout vs playoff continuous OT. Confirm whether contract is 60-minute regulation or includes OT/SO. Empty-net goal tails must be explicit in full-game totals and margins. Other leagues require their own rules and profile.

## 7. Write, audit and return

Also apply the core's **Step 7 — Write, audit and return** shared rules ([prompt 1 core](../1_GAME_CARD.md)).