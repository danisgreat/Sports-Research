# PROMPT 1 — sport file: OTHER SPORTS

**P-2026.10.17-v22.2 · prompt 1 sport file.** Use this file together with the [prompt 1 core](../1_GAME_CARD.md): read the core first, then this file. The core holds every rule shared by all sports, including the shared rules of steps 1, 3, 4, 5 and 7; this file holds this sport's own instructions for steps 1–7. At each step apply the core's shared rules for that step together with this file's. Fill in the Upcoming game block below; it is the only part the owner edits. Do not read the other sport files.

OTHER SPORTS
----------------------------

## Upcoming game — OTHER SPORTS

**Inactive template:** run only when the user fills or explicitly invokes this sport’s event. Empty examples allocate no ID and trigger no forecast.

- Event / official link: <participants and exact game identity>
- Competition details: <Exact sport / organizer / competition / format; participants; legal endpoint, start/entry list and replacements where applicable.>
- Scheduled start: <local date/time, venue timezone; verify UTC and Australia/Sydney>
- Active local mini: <exact path>
- Supplied contracts: <copy every exact proposition/line/period/action term, or NONE>
- Research constraints: <actual request; only-confirmed issuance if expressly required>

Read [COMMON_OPERATING_PROTOCOL](../COMMON_OPERATING_PROTOCOL.md), [MINI_LOG_IDENTITY_PROTOCOL](../../../MINI_LOG_IDENTITY_PROTOCOL.md) and the complete seven-step sport workflow below. The primary card is ANALYST_PRIMARY_V1: researched and priced by hand under NOCODE-v1 (prompt header). No model, runtime, shadow or decision-lab output is read or used; ML/RL belongs to prompts 6 and 8.

Also apply the core's **Before step 1 — evidence standard** ([prompt 1 core](../1_GAME_CARD.md)).

## 1. Read and establish authority

Also apply the core's **Step 1 — Read and establish authority** shared rules ([prompt 1 core](../1_GAME_CARD.md)).

Read COMMON_OPERATING_PROTOCOL and every control from the latest commit of the GitHub repository's `main` branch, pinned by its full SHA for the run, in read-only mode (`PUBLISHED_MAIN_PINNED`) (EXTERNAL_CHAT); this prompt never uses local controls. Print the [reading receipt](../README.md) after opening CURRENT_STATE, METHOD, CURRENT_RULES, SELECTION_RULES, CARD_AND_LOG_TEMPLATES, applicable sport rule file if present, SOURCES (the sport's §3 section if one exists, otherwise §2 and the [§3.11](../../../SOURCES.md#311-field-fallback-and-official-social-use-by-sport) fallback rules), ARCHIVE_USE_GUIDE, this prompt, the complete active mini, GAME_LOG_STATUS_CURRENT and relevant canonical event records. Read them within the ENV-v1 reading budget (named sections of large files; only this sport's workflow) and record the latest `main` SHA, exactly what was read and the read time. Apply current controls over historical sport-engine notes.

## 2. Identity, duplicate and timing gate

Verify participants, competition, season, stage, venue, native ID, official scheduled start, venue zone, UTC and Australia/Sydney time. Search every relevant local mini/carryover and canonical log body/status by ID, event key and aliases; doubleheaders and postponements need explicit identity handling. An existing event gets a dated addendum under its original local key or verified existing canonical reference, no new card or canonical assignment.

For a new event, use the mini's next stable LOCAL-<MINI_KEY>-G0001-style event key under MINI_LOG_IDENTITY_PROTOCOL; set canonical ID NOT_ASSIGNED / PROMPT_4_IMPORT. Do not assign, reserve, forecast or advance a P-ID during research. Read canonical state only for duplicate/context checks; canonical allocation happens in prompt 4. Record current source state before research and again immediately before write. Keep cutoff, research completion, actual issue and state-recheck times separate. Continue until research is complete even if play starts. Keep actual issue phase and input evidence separate: independently proved pre-start fields with no outcome exposure may be CLEAN_PRE_START_INPUTS / POST_START_ISSUE, scored in its own research cohort; it is not a pre-start-issued prospective forecast. Live/final exposure or unverified known-at facts prevent the clean-input claim. Apply [TIMING_RESEARCH_PROTOCOL](../../../TIMING_RESEARCH_PROTOCOL.md), with no minimum lead or forced early freeze. Log the request in the mini's intake table (template §2-D) whatever its outcome. Confirm you hold the mini's issuing-writer lease and that the mini is not frozen for settlement; otherwise route the event to the next authorised mini (CURRENT_RULES §8). Follow [TIMING_RESEARCH_PROTOCOL](../../../TIMING_RESEARCH_PROTOCOL.md): complete research without a countdown deadline, even after start; freeze only the completed issued original. Complete the mandatory availability search and final recheck first (CURRENT_RULES §5b; ROSTER_AVAILABILITY_PROTOCOL). If selections remain genuinely unpublished or unverified, record the exact side/field and completed attempts, then use supported scenarios or qualitative/NO_FORECAST research with the honest `LINEUP_UNCONFIRMED` label; do not claim an unperformed scheduled retry.

## 3. Evidence and online history

Also apply the core's **Step 3 — Evidence, line-ups and online history** shared rules ([prompt 1 core](../1_GAME_CARD.md)).

**Availability research (AVAIL-2026.10.16-v4).** Read and apply [ROSTER_AVAILABILITY_PROTOCOL](../../../ROSTER_AVAILABILITY_PROTOCOL.md) §§1–6 for both sides: exact starters/starting role, selected bench/replacements, current injuries/illness/suspensions/absences, and late changes. Complete its official match → both teams → eligibility/medical → permitted provider → local-language/obscure-competition escalation before reporting a missing field. Record actual searches, evidence/times and failures in the existing Evidence receipt/A3/A8; update the existing lineup-state metadata and audit C20. A roster, probable starter or predicted side is not confirmation. Recheck around the actual competition release window and immediately before freeze; re-price changed inputs. Never invent a healthy roster, bench or confirmation. If material gaps survive the full search, retain supported scenarios or qualitative/NO_FORECAST research with the exact reason. Model output and market/decision-lab material are never read.

Follow official governing body / field owner match center → structured providers → quality corroboration routes. For each decisive claim retain URL, exact field/value or brief extract, source publication/update time when known, retrieval time and provenance/lineage. Log inaccessible/stale/conflicting sources. Three domains are not three independent collectors. No odds/tips/previews/fantasy inputs.

Verify confirmed participant readiness, lineups and availability; probable is not confirmed. Research exact participants' prior games online under HISTORICAL_SOURCE_PROTOCOL. If sources cannot support an authoritative model, use UNCALIBRATED_QUALITATIVE or NO_FORECAST.

## 4. Distribution, expected score and comparator

Also apply the core's **Step 4 — Distribution, expected score and comparator** shared rules ([prompt 1 core](../1_GAME_CARD.md)).

Build the simplest defensible coherent sport distribution you can actually compute. Print every parameter and its basis, formula/table, normalization, tail treatment, covariance and endpoint transitions. If the required calculation cannot be done, report a supported approximation with limitations, or qualitative research with NOT_ESTIMATED probabilities. Hand method: PROBABILITY_TOOLKIT §1–§3.

Produce expected score terms from CARD_AND_LOG_TEMPLATES §3a where supported; otherwise mark NOT_COMPUTED. Keep zeros; mark missing or irrelevant terms. Print all winner/draw/tie masses. For every candidate retain unconditional W/P/L/V and p_card=W/(W+L), with denominator and action convention.

Attempt BASELINE_LEAGUE_V1 if league data exists. Show sensitivity on material uncertain inputs. Report plausible probability ranges as sensitivity, not confidence intervals. Do not move individual probabilities outside the shared model.

## 5. Candidate selection and dependence

Also apply the core's **Step 5 — Candidate selection and dependence** shared rules ([prompt 1 core](../1_GAME_CARD.md)).

Freeze the supported family/line-generation recipe before pricing. Price supplied rows and the declared derived universe; retain exclusions and unused supplied rows. Values above the selection ceiling keep their true probabilities in the diagnostic appendix and are excluded, never capped.

## 6. General sport playing conditions and rules

Verify exact competition conditions, regulation duration, tiebreak/overtime rules, and abandonment rules. Do not borrow a model from an unrelated sport whose endpoint does not fit.

## 7. Write, audit and return

Also apply the core's **Step 7 — Write, audit and return** shared rules ([prompt 1 core](../1_GAME_CARD.md)).