# Research protocol: completion, persistence, retention, checklists and timing

**Merged 2026-11-07, CR-2026.11.07-R2 (FORMAT).** This document joins the files below, verbatim and in this order. Nothing was reworded. Each source's title line became its part heading. The banner paragraphs that every source repeated appear once, below. Links to the old files now point to their parts, and the originals are kept unchanged in [archive/consolidation_2026-11-07/merged_sources/](archive/consolidation_2026-11-07/merged_sources/).

| Part | Former file | Bytes | SHA-256 of the original |
|---|---|---:|---|
| [A](#part-a-research_completion_protocol) | `RESEARCH_COMPLETION_PROTOCOL.md` | 13,948 | `d9f65ab6ee8c2dbc7eb9b73609f26a39a2e608ba46ecf822dfac09cbbc040419` |
| [B](#part-b-research_exhaustiveness_protocol) | `RESEARCH_EXHAUSTIVENESS_PROTOCOL.md` | 12,698 | `bee4e597cf98a6c74f6faa4d7f07eff9e1cf22c4858c719ec8cbe714b5677491` |
| [C](#part-c-research_retention_protocol) | `RESEARCH_RETENTION_PROTOCOL.md` | 7,888 | `45768e84e192c2d0f3b9832f612057489ff3870b4af6988114fd66950ca45e1f` |
| [D](#part-d-research_checklists) | `RESEARCH_CHECKLISTS.md` | 8,623 | `47a1f56f6161bef5c59d783a7201954568d8bfc6e2518de6a5fc3834fd894187` |
| [E](#part-e-timing_research_protocol) | `TIMING_RESEARCH_PROTOCOL.md` | 8,997 | `1acfc38a043aa03612d06ecf06b6e50faf782a234c0fa18a253769195bfb8987` |

**ML/RL scope (MLSCOPE-v3).** Defined in [FORECAST_CYCLE_PROTOCOL](REFERENCE_MODEL_PROTOCOL.md#merged-forecast_cycle_protocol); summarised in [CORE](CORE.md) §7.

**Local keys until settlement; updated mini after every game (MINI-v2).** Defined in [MINI_LOG_IDENTITY_PROTOCOL](WORKFLOW.md#part-b-mini_log_identity_protocol); summarised in [CORE](CORE.md) §2.

**Persistent research and corroboration (EXH-v1).** Defined in [RESEARCH_EXHAUSTIVENESS_PROTOCOL](#part-b-research_exhaustiveness_protocol); summarised in [CORE](CORE.md) §5.

**Online history and confirmed players (HIST-2026.10.16-v3 / AVAIL-2026.10.16-v4).** Defined in [HISTORICAL_SOURCE_PROTOCOL](HISTORICAL_SOURCE_PROTOCOL.md); summarised in [CORE](CORE.md) §5.

**Required repository fallback (REF-v1).** Defined in [GITHUB_REFERENCE_PROTOCOL](GITHUB_REFERENCE_PROTOCOL.md); summarised in [CORE](CORE.md) §1.

**Research retention before model availability (RETAIN-v2).** Defined in [RESEARCH_RETENTION_PROTOCOL](#part-c-research_retention_protocol); summarised in [CORE](CORE.md) §2.

**Local research record and updated-document delivery (owner update, 16 October 2026).** Defined in [MINI_LOG_IDENTITY_PROTOCOL](WORKFLOW.md#part-b-mini_log_identity_protocol); summarised in [CORE](CORE.md) §2.

**Executable forecast cycle (CYCLE-v1).** Defined in [FORECAST_CYCLE_PROTOCOL](REFERENCE_MODEL_PROTOCOL.md#merged-forecast_cycle_protocol); summarised in [CORE](CORE.md) §7.

---

# Part A: RESEARCH_COMPLETION_PROTOCOL

*Formerly `RESEARCH_COMPLETION_PROTOCOL.md` (original title: Mandatory research completion for every sport and competition). Original kept unchanged at [archive/consolidation_2026-11-07/merged_sources/RESEARCH_COMPLETION_PROTOCOL.md](archive/consolidation_2026-11-07/merged_sources/RESEARCH_COMPLETION_PROTOCOL.md).*

**RC-2026.10.16-v2 · MDS-2026.10.16-v20.0 · CR-2026.10.16-R7 · P-2026.10.16-v20.0.** Owner instruction, 15 October 2026: complete the analysis, procedures and research regardless of calibration or other problems. Applies to every requested game, including obscure, regional, women's, youth and lower-tier competitions. [Current rules](RULES_REFERENCE.md#part-a-current_rules) govern numerical selection, custody and truthful timing.

## 1. Strict rule: no dependency failure ends independent research

**MUST complete and deliver every applicable independent research procedure and the full sport-specific analysis.** Missing calibration/certification, an unavailable/failed model, unsupported markets, incomplete history, unconfirmed lineups, kickoff, an existing mini, identity/ID disagreement, writer-lease conflict or write failure are never grounds to stop the rest of the work. Continue until the applicable research attempts, calculations, analysis and verification are done. Do not substitute a refusal, intake-only supplement, brief matchup summary or table of NO_FORECAST labels for the complete deliverable.

Track three separate questions: was the research performed; which numerical procedures actually executed; can this record be issued/appended? Failure in one does not imply failure in all. Exhaustive research cannot guarantee that every fact is public or every model is executable. A genuine unresolved dependency gets evidence, its precise affected fields, impact and next action. Unattempted independent work remains INCOMPLETE, never silently waived. Explicit user cancellation or scope/time limits still govern; preserve completed work and state what remains.

An existing contiguous active mini is a continuation route, not a new-mini prerequisite. Verify its complete original, sequence, identity, writer authority and unfrozen state, then append there if permitted. If those checks cannot pass, complete the full no-ID READ_ONLY_DRAFT / NOT_ISSUED research artifact. Never create a competing mini/allocation, reconstruct inaccessible original bytes, claim an unverified candidate ID was issued, or advance an unwritten footer. Duplicate events route new research to an addendum under the verified original ID; originals stay unchanged.

## 2. Required independent work

Execute the selected sport's seven steps and A1–A9, with actual findings and evidence rather than copied headings:

1. **Authority, identity and timing:** inspect available controls, exact competition/season/stage, participants/aliases, venue, endpoint/format, schedules, event state and duplicate records. Quarantine ambiguities by field; do not merge different possible fixtures. If identity is genuinely ambiguous, document the candidates and finish work independent of choosing one; do not fabricate a definitive matchup analysis. Preserve actual start/issue, field-known-at and exposure labels under [timing rules](#part-e-timing_research_protocol). Research continues after start; later issue is never backdated.
2. **Both-side availability:** execute [ROSTER_AVAILABILITY_PROTOCOL](ROSTER_AVAILABILITY_PROTOCOL.md), including exact-match official releases, both teams, medical/disciplinary sources, permitted providers and original-language organizer/federation/local sources for obscure coverage. Assess starters, bench/replacements and absences separately; a projected side never becomes confirmed. Record actual queries/URLs, results, failures, times, contradictions and final recheck. One broken page is not an exhausted search.
3. **Historical data and form:** [research prior games online](HISTORICAL_SOURCE_PROTOCOL.md) for every event. Build both sides' L5/L10/L15/L20, season and league comparisons with true usable n, dated observations, endpoint/source/known-at evidence, overlap/dedup/corrections and prior-season continuity. Complete all available windows; one unavailable metric does not suppress the rest. Do not borrow major-league defaults for an obscure competition. No invented 20-game history or fabricated availability time.
4. **Sport-specific mechanisms:** execute the complete selected sport section: current form, home/away or surface/venue effects, matchups/tactics, rest/travel/congestion, lineup workload, weather/playing conditions, competition-specific rules and supported scoring/phase mechanisms. Distinguish observed facts, calculated estimates and analyst assumptions; explain conflicting evidence. A generic form paragraph does not replace this work. N/A requires a sport/format reason.
5. **Procedures and calculation:** attempt the supported primary inference route and repairs in §3, then execute supported analyst comparisons for unavailable/unsupported parts. Attempt exact-row league baselines and sensitivity. Keep completed supported families even when another family fails. For uncomputable quantities explain the missing parameter/data/implementation and what qualitative evidence still says; do not merely name a model that was not run.
6. **Every requested contract:** preserve exact line, period, endpoint and action terms. In A2/A5 provide supporting evidence, opposing evidence/failure route, actual numeric calculation or reason it cannot be computed, sensitivity to unresolved inputs, and a reasoned conclusion (supported lean, balanced/indeterminate or undefined). Both sides of a complementary pair share a consistent mechanism; do not count them as independent evidence. Unknown operator terms stay UNKNOWN_DEFINITION, with any conditional sporting assessment explicitly labelled. A row-level NO_FORECAST is allowed only after this analysis. Unsupported first-half/player/corner markets do not erase supported full-game research.
7. **Delivery and verification:** complete the decision block, evidence/arithmetic appendices, audit and §4 matrix. Write/read back the authorized mini and return its complete updated .md after each prompt-1 request; use stable local keys and defer canonical IDs to prompt 4. If blocked, return the full separate draft with actual delivery status. If mini bytes are accessible but append is blocked, preserve them and provide the separate complete artifact; if inaccessible, never claim to reproduce the complete mini. State precise remaining work rather than promising a background retry that is not scheduled.

Do not repeatedly retry an identical broken route without progress. Try the applicable alternate routes and focused repairs, record observed capability/access failures and exhaust the independent work. A real environment limit is a documented gap, not a fabricated success. If a task must yield before completion, label the deliverable INCOMPLETE and identify the pending work; do not claim completed research.

## 3. Execution and fallback hierarchy

**A. Actual experimental ML first where supported.** Read [PRIMARY_PREDICTION_PROTOCOL](ML_PIPELINE.md#part-a-primary_prediction_protocol). Prepare reviewed exact-competition history/metadata and exact supported contracts; use accessible tools to run the runtime and verify its bundle. Missing independent calibration is disclosed EXPERIMENTAL_PRIMARY_NOT_CERTIFIED and is not a prerequisite for this already-authorised use. Do not demand production certification before running it. Uniform weights/no admitted feedback are disclosed states, not grounds to invent learning. Investigate concrete failures, correct admitted input/schema/identity/endpoint issues from evidence, retry where resolvable and record the result. Do not bypass data-known-at/hash/fit/unsupported-engine guards or falsely report inaccessible execution. An exact-event verified bundle may be read if actually available; a historical/cached unrelated forecast cannot substitute.

**B. Supported analyst procedure automatically.** The standing owner instruction authorises and requires an uncalibrated analyst comparison for the portions unavailable to ML. Carry out an actually supported sport/endpoint method from [PROBABILITY_TOOLKIT](PROBABILITY_TOOLKIT.md), the sport rules and selection controls, using researched data. Write equations, source-backed inputs, explicit assumptions, sample sizes, executed arithmetic, approximation limits and low/base/high sensitivity. Where numerical scenarios/weights have a defensible basis, calculate their results; otherwise describe scenarios qualitatively rather than invent weights or SDs. If a source-supported calculation is feasible, lack of a calibration certificate is not a reason to skip it. Calibration alone neither invalidates arithmetic nor establishes predictive reliability.

Label these calculations **UNCALIBRATED_ANALYST_SCENARIO / NOT_PRIMARY**, with `analyst_p` and separate scenario/base values in A4/A5. They are not a verified ML run, not calibrated confidence, not model p_card, not a numerical primary gate PASS, not T2 model wins and not model-learning feedback. Do not overwrite any successful model distribution or combine incompatible family estimates into a fake joint model. An analyst comparison never silently promotes an unsupported runtime adapter. Primary numerical policy PRIMARY_HEDGE_MIX_V3 is unchanged.

**C. Full qualitative analysis where honest numbers are impossible.** Finish all available research and each contract assessment with evidence-backed reasoning, competing mechanisms, conditional scenarios, confidence limits in words and a supported direction only if justified. Use UNCALIBRATED_QUALITATIVE with p_card NOT_ESTIMATED, or NO_FORECAST for genuinely indeterminate/undefined rows. NO_FORECAST is a numerical/selection disposition, not a research stopping condition. Never force a winner, probability, four picks or confirmed lineup. Missing a baseline limits paired scoring, not research delivery.

If live/final target outcomes were exposed, continue only with truthful LIVE_OBSERVED/HISTORICAL_DIAGNOSTIC labelling. Do not run the outcome-blind primary lane with a false exposure declaration or call an already-observed proposition a new clean prediction. Preserve what pre-start information can actually be evidenced; calibration or completion cannot repair hindsight.

## 4. Completion receipt and return

Add this matrix within A9; new minis use mini-log-10 with an honest execution-disposition manifest, including no-model rows, while old issued formats are preserved, including artifact/source pointers and actual outcomes, not unsupported check marks:

| Required procedure | Actual work/evidence and result | Remaining gap, affected field/contract and next action | Status |
|---|---|---|---|
| Authority / exact identity / duplicate / timing | | | |
| Both-side starters / bench / absences / final recheck | | | |
| Online history / source comparison / correction / known-at | | | |
| Both-side L5 / L10 / L15 / L20 / season / league | | | |
| Selected sport's mechanisms / conditions / rules | | | |
| Actual primary run / repair / verified bundle or capability failure | | | |
| Supported analyst procedure / equations / arithmetic or justified nonnumeric handling | | | |
| Every supplied row and declared supported candidate / definitions | | | |
| Expected-score / exact-row baseline attempt / sensitivity / dependence | | | |
| All seven sport steps / A1–A9 / audit / custody / delivery readback | | | |

Per row: DONE; EXHAUSTED_WITH_EVIDENCE (applicable routes attempted, genuine gap remains); NOT_APPLICABLE with reason; or NOT_DONE. Split mixed rows so an unattempted item cannot hide behind a completed one. Keep a separate contract-by-contract coverage table in A2/A5.

Overall information status follows RESEARCH_EXHAUSTIVENESS_PROTOCOL: **COMPLETE** only when every required field has corroborated factual evidence, an independent mechanical check or justified true N/A, all required procedures/contract dispositions are evidenced and delivery/readback passes. Otherwise **INFORMATION_INCOMPLETE**; keep searching alternatives and record exact remaining fields, corroboration, actual attempts and next actions. EXHAUSTED_WITH_EVIDENCE describes process attempts only. COMPLETE_WITH_DOCUMENTED_GAPS is a legacy label, not permission to claim new-run information completeness. Retention, model availability and issuance status remain separate; do not manufacture facts to close gaps.

Return the complete updated cumulative mini .md (or the explicitly blocked separate draft), and concise findings, supported conclusions/uncertainties, contract dispositions, actual calculations, completion matrix, paths, issuance/allocation state and remaining gaps. Do not lead with an administrative mini refusal and stop. Existing cards, frozen original ranks/grades, ID sequence, reserved ranges and publication scope remain protected. Prompts1–3 still make no canonical/GitHub writes.

---

# Part B: RESEARCH_EXHAUSTIVENESS_PROTOCOL

*Formerly `RESEARCH_EXHAUSTIVENESS_PROTOCOL.md` (original title: Persistent research, corroboration and source reuse). Original kept unchanged at [archive/consolidation_2026-11-07/merged_sources/RESEARCH_EXHAUSTIVENESS_PROTOCOL.md](archive/consolidation_2026-11-07/merged_sources/RESEARCH_EXHAUSTIVENESS_PROTOCOL.md).*

**EXH-2026.10.16-v1 · MDS/P v19.2 · CR-R6.** Owner instruction, 16 October 2026: pursue the full information needed for every research/log/settlement requirement, switch sources when one is incomplete, verify findings with another source and retain newly discovered routes for future use. Applies to all sports, competitions, requested contracts and every lifecycle task. New settlements use mini-settlement-10; mini-log-10 follows MINI-v1 local-key identity and cumulative-document delivery. No statistical threshold, scoring formula or original issued record is changed.

## 1. No early exit; no false closure

Do not stop at the first source, partial page, failed request, familiar provider, missing English result, unsupported model, kickoff or earlier unresolved label. Continue searching and verifying until each applicable information requirement has a justified closure. A populated table, link, search snippet, repeated claim, a NO_FORECAST label or an exhausted first route is not completion. Keep doing independent work while another field is blocked.

An agent cannot make unpublished, private, future or contradictory evidence exist. Never fill such a gap with a guess, forced WIN/LOSS/VOID, invented source, backdated lineup, substituted operator terms or unsupported model output. A real access/publication/identity/definition/implementation barrier remains OPEN_BLOCKED_WITH_EVIDENCE with actual attempts, exact missing field, impact and next action. The overall information status stays INCOMPLETE while any required field or corroboration is open. Process work can be performed even when the facts remain incomplete; do not label that state complete. Research retention and the stable local event key (canonical P-ID assigned only in prompt 4) still apply under RESEARCH_RETENTION_PROTOCOL.

This release supersedes COMPLETE_WITH_DOCUMENTED_GAPS as a new-run overall information-completion label. Older originals keep their literal labels and rule versions. EXHAUSTED_WITH_EVIDENCE describes attempts, not fact closure. Respect explicit user cancellation/scope/time limits; never claim unexecuted background retries, a scheduled job or future completion. Resume open fields at the next authorized review instead of silently treating the queue as resolved.

## 2. Requirement-by-requirement search loop

1. Inventory every required field, side, event/contract, exact scope/endpoint, information horizon and success condition before declaring completion. Cover authority/custody/IDs, identity/rules/time, both-side players/roles/bench/absences, L5/L10/L15/L20/season/league populations, sport mechanisms/conditions, model/input/baseline/calculation evidence, original action/void/retirement/OT terms, final/period/innings/field statistics, source/final-at times, scoring/revisions and output/readback/retention. Split partially completed requirements; a completed result does not close its definition, player or timing fields.
2. Consult SOURCES and [RESEARCH_SOURCE_REGISTER](RESEARCH_SOURCE_REGISTER.md), including prior settlement source registers. Open the actual relevant page/document/data endpoint; follow exact match IDs, correct dates, tabs, pagination, original scorecards/PDFs and evidence links. Read the fields needed, not only a summary or a navigation listing. Old route observations are discovery aids requiring a fresh scope/status check.
3. If any needed field is missing, truncated, inaccessible, stale or ambiguous, immediately try another appropriate source. Start with the responsible organizer/league/federation, exact official match/gamebook and both teams/participants; then permitted structured providers, original-language local sources, broadcasters and accredited reporters. Search alternate names/scripts, event date/round/native ID, site navigation and original documents. A schedule, season roster or probable selection cannot stand in for the final/lineup/action field.
4. Acquire the missing pieces across sources with field-level mapping. Never import unrelated games, genders, age groups, seasons, formats or endpoints to fill blanks. Reconcile reschedules, doubleheaders and aliases before combining values. Record queries/routes and exact successes, failures and partial fields in SOURCE_SEARCH_ATTEMPTS.csv; record discoveries in SOURCE_DISCOVERY_REGISTER.csv.
5. Verify every material factual field used to satisfy a requirement with a second opened source. Compare exact identity, orientation, endpoint, value/status and relevant time. Seek independently collected evidence; mirrors/syndication and one feed on two domains are not independent corroboration. Unknown lineage stays UNKNOWN and does not pass an independence claim. The responsible normative rule/contract source governs its own scope; a secondary report can check interpretation but cannot override it. Disagreement triggers more owner/correction evidence, not averaging, majority vote or last-page-wins.
6. Recompute calculated values independently from their evidenced inputs and read back custody/byte/hash/ID results against the actual original and published counterpart where applicable. These are verification operations, not fabricated extra internet citations. A valid implemented method may finish with an evidenced NOT_ESTIMATED/NOT_APPLICABLE numerical disposition; do not manufacture a result or imply that software is an independent factual collector.
7. Revisit every remaining field after each discovery. Use newly found links, source archives, gamebooks and local-language routes to drive the next search. Do not repeatedly hit an unchanged failed endpoint while alternatives remain. Before a blocked disposition, review the relevant register entries and every applicable route family, including material conflicts and corroboration; record what was actually attempted, not an imaginary exhaustive search of the entire internet.
8. Recheck fragile fields at the actual release window and before issue/settlement finalization. Preserve field-level known-at, source publication/correction/retrieval and actual event/issue times under TIMING_RESEARCH_PROTOCOL. Later facts may settle a result or inform a future forecast, never prove earlier player confirmation or repair outcome exposure. Complete authorized writes and readback independently; a missing fact does not erase retained research.

## 3. Closure and corroboration states

Each applicable factual requirement has a REQUIREMENT_CLOSURE.csv row, split by field/side/scope as needed. VERIFIED_CORROBORATED means the primary and second actually opened evidence match, scope/time/endpoint are compatible, collector independence is evidenced and conflicts are resolved. VERIFIED_RECALCULATED is reserved for reproducible arithmetic or mechanical custody checks, with the independent calculation/readback named. NOT_APPLICABLE needs a real sport/format/task reason; it cannot hide a missing field or unavailable model.

SINGLE_SOURCE_OPEN, CORROBORATION_PENDING, LINEAGE_UNKNOWN_OPEN, CONFLICT_OPEN, NOT_ATTEMPTED and OPEN_BLOCKED_WITH_EVIDENCE are open states. A source's authority alone does not waive the requested second-source search. If two sources share a collector, find another collector; if no permitted independent confirmation can be obtained, keep that corroboration requirement open and explain the barrier. Do not call unresolved information complete because every attempted route failed.

Overall information completion is COMPLETE only when every required row is VERIFIED_CORROBORATED, VERIFIED_RECALCULATED or justified NOT_APPLICABLE, every contract has an evidenced supported disposition, and output/readback/source-register checks pass. Otherwise INFORMATION_INCOMPLETE; retain verified work and precise outstanding tasks. The original sporting/operator/evidence/forecast status vocabulary remains separate. No single status string guarantees source truth, calibration, publication timing or model availability.

## 4. Mandatory settlement section and reusable registers

Every new mini-settlement-10 package contains a visible section titled **Source discovery, corroboration and reuse register** in its settled output and standalone settlement report. It includes all sources actually used/rechecked, newly discovered source routes, which required fields each exposes, its corroborating sources/conflicts, and every remaining information gap. Include the three CSV sidecars below and link them from that section. An empty source list is allowed only with an evidenced no-discovery/no-access result; it does not make missing requirements complete.

- SOURCE_DISCOVERY_REGISTER.csv: stable local source ID, discovery time, phase/sport/competition/exact event or coverage scope, publisher/owner/collector lineage, URL/deep link, navigation/query/pagination/language, fields actually observed, fields absent, publication/update and retrieval/last-check times, access result, evidence capture/hash, corroborating source IDs and comparison outcome, reuse instructions/limits and source record status.
- SOURCE_SEARCH_ATTEMPTS.csv: attempt ID, event/requirement/field, time, query/route/source ID/URL, access result, actual fields found, unresolved pieces, collector relation, next source/action and evidence pointer. Failed and partial searches stay visible; never mark an unopened source checked.
- REQUIREMENT_CLOSURE.csv: requirement/event/phase/side/field/scope/horizon, primary and corroborating source or independent check, independence/conflict result, field status, remaining issue, next route/action, actor/due time and actual automation status.

Templates are under research/prompts/templates. Keep source IDs and observation revisions stable. A new discovery or changed access/coverage adds a dated observation; do not overwrite prior receipts, source extracts or failed attempts. Old settlement packages keep their formats; a new review records new work in a dated addendum/new package, not by editing the old report. A register records observed source capabilities, not a promise that the source is always available or complete.

## 5. Reuse, write scope and publication

Start future research and settlement by consulting the shared register, applicable SOURCES routes and relevant prior package registers, then revalidate the exact event/field/version and continue discovery until requirements close. Do not limit research to existing entries. One complete fact from a source does not establish its other fields, other seasons or historic known-at. Retain raw captures/helpers outside Git; market-free extracts and Markdown/CSV/text receipts stay in authorized scopes. Exclude odds/tips/fantasy/market data from normalized research.

Prompts1-3 remain within their named mini/primary/evidence/settlement scope and do not silently edit shared files or publish. They record discoveries locally and identify candidate shared additions. Authorized prompt4 imports the complete source registers, search attempts and closure table with original IDs/hashes; it appends deduplicated dated observations to RESEARCH_SOURCE_REGISTER when in its declared scope. Prompt7/8 may maintain the shared source map under their authorized changes. Reuse never changes old cards, original grades, canonical allocation, accepted source truth or model qualification.

## 6. Audit and edge cases

C13/C20 and A3/A8/A9 check persistent field-level research and corroboration. New settlement check S17 verifies the visible source section, all three sidecars, complete requirement coverage, genuine second-source/independent checks, discovery reuse, unresolved-field barriers and readback. Old settlement8 uses S1-S16, earlier formats their own checks. Record actual PASS/FAIL/NOT_VERIFIED/N/A evidence. A template or checklist alone is not an executed search.

A partial lineup requires another route for bench/absences; a final score does not close corners/periods/OT/terms; an authoritative single source still needs corroboration; two feed mirrors cannot pass independence; conflicting endpoints stay open; private terms/unpublished lineups/future final-at cannot be invented; unsupported ML permits truthful no-model retention and independent research. Documentation/process improvements never demonstrate predictive gain.

A window with fewer eligible games can close only when the true short population and its coverage are independently verified; missing collection is not proof that games do not exist. Always retain actual n rather than inventing20 games.

---

# Part C: RESEARCH_RETENTION_PROTOCOL

*Formerly `RESEARCH_RETENTION_PROTOCOL.md` (original title: Retain local research independently of model availability). Original kept unchanged at [archive/consolidation_2026-11-07/merged_sources/RESEARCH_RETENTION_PROTOCOL.md](archive/consolidation_2026-11-07/merged_sources/RESEARCH_RETENTION_PROTOCOL.md).*

**RETAIN-2026.10.16-v2 · MDS/P v19.2 · CR-2026.10.16-R7.** Owner update: prompts 1–3 retain researched events under stable local event keys. Canonical P-IDs are assigned only during prompt 4 import. After every prompt-1 game request, deliver the complete updated mini .md. This supersedes RETAIN-v1's pregame working/permanent P-ID assignment while preserving model-independent research retention, original source bytes, truthful timing and numerical PRIMARY_HEDGE_MIX_V3 policy.

Read [MINI_LOG_IDENTITY_PROTOCOL](WORKFLOW.md#part-b-mini_log_identity_protocol), [RESEARCH_EXHAUSTIVENESS_PROTOCOL](#part-b-research_exhaustiveness_protocol), [GITHUB_REFERENCE_PROTOCOL](GITHUB_REFERENCE_PROTOCOL.md) and [PRIMARY_PREDICTION_PROTOCOL](ML_PIPELINE.md#part-a-primary_prediction_protocol).

## 1. Local research and delivery before canonical allocation

Retain every identified researched event in the authorized mini under its stable LOCAL-<MINI_KEY>-G0001-style key. Do not assign/reserve a canonical number during research or settlement; use canonical ID NOT_ASSIGNED / PROMPT_4_IMPORT. Append the full card, update intake/manifest/queues and local footer, read back the complete mini and return the complete cumulative updated .md after each request. Missing ML, adapter, interpreter/module, baseline, calibration, data or receipt never by itself prevents the local research record or later canonical import. Duplicates/addenda retain their original key; existing canonical references keep their already assigned ID.

Use RESEARCH_ONLY_NO_MODEL where no verified fitted primary output exists. Keep model p_card NOT_ESTIMATED and supported analyst_p separately NOT_PRIMARY, with source-backed reasoning, assumptions/gaps and actual times/exposure. Incomplete required facts remain INFORMATION_INCOMPLETE under EXH-v1; retaining research is separate from full evidence completion. Never invent probabilities, execution, scores or pregame timing.

Only real event-identity/custody/lease/freeze/write conflicts block the affected append. Preserve independent research and return an honest complete separate draft if the mini cannot be safely updated. Do not reconstruct an inaccessible original. Follow MINI-v1's complete-document, duplicate and blocked-delivery rules.

## 2. Honest execution disposition without a fake receipt

Attempt a supported primary run when accessible. Retain actual success/failure bundles. If it cannot run, record NOT_RUN_CAPABILITY_BLOCKED, NOT_IMPLEMENTED or NOT_RUN_DATA_UNAVAILABLE with the concrete reason. Do not repeat a known capability failure indefinitely or fabricate an execution receipt.

ML_EXECUTION_MANIFEST.csv keeps its existing columns with one row per new card; card_id is the stable local key and event_id is the native/stable event identity. For no actual artifact leave execution_path/execution_sha256 blank, feedback_status NOT_APPLICABLE_NO_MODEL, feedback paths/hashes blank and a substantive reason. C21 accepts honest research-only disposition. Actual model claims require a verified successful bundle. verify-log supports mini-log-10 local cards and preserves legacy8/9 P-card support, without allocating a canonical ID.

New minis use mini-log-10 / mini-settlement-10. Old cores and formats remain unchanged; new local-key work in an old active mini follows the dated lifecycle-addendum rule. Canonical assignment/status never changes a frozen primary request, native event ID, probability, feedback row or hash.

## 3. Import may precede settlement; only prompt 4 assigns canonical IDs

An authorized prompt4 retention-only import can precede settlement or ML execution. Inventory all sources and reconcile exact events against canonical/native aliases; assign genuinely new canonical IDs contiguously only in the verified import plan, preserve already committed mappings/reserved ranges, and append literal local cores inside canonical wrappers. Record the complete local-key → canonical-ID map separately from frozen originals. Update actual highest/next only after successful append/readback. Duplicate/addendum/rerun consumes no new ID. Pending outcomes remain PENDING_SETTLEMENT / OUTCOME_NOT_REVIEWED, never invented finals or performance rows.

Prompt3 before import settles original local keys with canonical mapping NOT_ASSIGNED. After import the same original key has a verified canonical mapping; later revisions preserve that mapping in new evidence, never rewrite the source. New events after freeze go to the next authorized mini namespace. Existing issued legacy P labels remain literal and are mapped explicitly at import, never renumbered in place.

## 4. Two kinds of learning evidence

Future-development targets: retain verified final endpoints/grades, source/time/hash, original research/features, actual availability/exposure, effective revision and feature-admission status. Local prompt3 retains reviewed LABELS.csv and evidence by local key. The current research_learning exporter requires a canonical P-ID, so run it only after prompt4 verifies assignment, using mapped canonical original and settlement wrappers containing the unchanged local source. Do not allocate an early ID for an exporter.

```text
python -m ml.research_learning retain --card-id P-NNN --record CANONICAL_WRAPPER.md --settlement MAPPED_SETTLEMENT_WRAPPER.md --labels LABELS.csv --out research/training_candidates/P-NNN/revision-1
python -m ml.research_learning verify --candidate research/training_candidates/P-NNN/revision-1
```

LABELS.csv retains schema event_id,competition,endpoint,label_key,label_value,label_unit,event_at,final_at,available_at,source_url,evidence_path,evidence_sha256,definition_status,review_status,revision_id,feature_status. review_status is TERMINAL_LABEL_REVIEWED; units GOALS/POINTS/RUNS/GAMES/SETS/WICKETS/BALLS or OUTCOME (WIN/LOSS/PUSH/VOID). The exporter allocates no ID. Reviewed labels are RESEARCH_TRAINING_CANDIDATE / LABELS_RETAINED_NOT_MODEL_FEEDBACK. Independent future-training source/scope/point-in-time/effective-revision admission remains required; a trusted target does not establish pre-start feature availability or prospective skill.

Existing expert feedback: only an actually issued frozen expert bundle supplies its own loss via primary settle. Without one retain verified targets and mark expert feedback NOT_APPLICABLE_NO_MODEL. Never manufacture probabilities, propensities, losses or model feedback. Preserve one effective native-event contribution and existing warm/feedback deduplication.

**Candidate-to-training admission (LEARN-v1).** A verified candidate is linked into an immutable training release by `python -m ml training build --candidates research/training_candidates` when its event's structured research export has been ingested. A candidate without exported history is listed as CANDIDATE_WITHOUT_STRUCTURED_HISTORY, never dropped and never given invented features ([LEARNING_PIPELINE_PROTOCOL](ML_PIPELINE.md#part-c-learning_pipeline_protocol) §5). Linking a label to features does not create expert feedback.

## 5. Counts and custody

Report local retained-card count, canonical imported-event count, numerical forecast coverage, feedback coverage and future-label export coverage separately. Local retention consumes only a local ordinal; prompt4 canonical import counts the mapped retained event even if qualitative/research-only. Analyst rows never inflate model T2/Brier/calibration/prospective cohorts. Existing cards, canonical state/IDs, issued ranks/grades, old formats and all prior source bytes remain protected. Check C2/C16/C21/C22 and S18 with actual evidence.

---

# Part D: RESEARCH_CHECKLISTS

*Formerly `RESEARCH_CHECKLISTS.md` (original title: Value-ranked research checklists, by sport (CHECK-v1)). Original kept unchanged at [archive/consolidation_2026-11-07/merged_sources/RESEARCH_CHECKLISTS.md](archive/consolidation_2026-11-07/merged_sources/RESEARCH_CHECKLISTS.md).*

**P-2026.10.22-v24.0 · CR-2026.10.22-R2.** Implements REV-14 of the [framework revamp review](research/verification/review_2026-10-22_framework_revamp/REPORT.md). The existing exhaustiveness rule (EXH-v1) treated every field alike; the value is concentrated. Work the **H** rows first and time them to when they are published, then the **M** rows, and spend effort on **L** rows only when the first two are closed. Each fact that moves a number becomes an adjustment row with a size from [EFFECT_TABLES](PARAMETERS.md#part-b-effect_tables).

**Value.** H: can move a fair probability by several points. M: about one to three. L: rarely matters. Stated publication times were checked on 22 October 2026 unless marked *unverified*; a rule change by the league supersedes this page. The verified source routes are in [SOURCES](SOURCES.md); this page ranks the inputs and does not replace the routes.

**Timing rule.** The evidence horizon is the game-log scheduled start. A decisive fact needs a publication time and a second independent source; a rumour, a projection or a depth chart is not confirmation. A fact published after the freeze is not in the card; it goes in a dated addendum (never an edit).

**Every sport:** the scheduled start and timezone; the venue and whether it is neutral; the stage and format (overtime, extra time, tie rules); weather for outdoor play in venue-local time for the match window (Open-Meteo, keyless); travel and schedule congestion; the competition's [parameter row](PARAMETERS.md#part-a-competition_parameters).

## Basketball (NBA, WNBA, NBL, EuroLeague, ACB, B.League, KBL and others)

| Input | Value | When it is published | Where |
|---|---|---|---|
| Status of the top-minute players | H | NBA: a status by 5 p.m. local the day before (1 p.m. on the second night of a back-to-back); a game-day report between 11 a.m. and 1 p.m. local (8-10 a.m. for tip-offs at 5 p.m. or earlier) | official.nba.com injury report; team and league sites elsewhere; ESPN site API for NBL and WNBA starters and did-not-play |
| Starting five; minute restrictions | H | Shortly before the tip | Team announcements; league game centres |
| Rest, back-to-backs, travel | M | Schedule | League schedule; ESPN API (measured NBA back-to-back effect: [EFFECT_TABLES](PARAMETERS.md#part-b-effect_tables), half size) |
| Player impact and minutes history | M | Continuous | NBA stats, Basketball-Reference; public impact metrics sit on different scales, so check before comparing |
| Officials | L | NBA about 9 a.m. ET on game day *(unverified timing)* | official.nba.com referee assignments |

Traps: preseason games; competition-specific overtime and quarter lengths; never carry NBA defaults into FIBA leagues. History: the ESPN scoreboard and Basketball-Reference schedule (two lineages) for the store; league routes in SOURCES 3.2.

## Baseball (MLB, KBO, NPB, CPBL, LMB)

| Input | Value | When | Where |
|---|---|---|---|
| Starting pitcher (probable, then confirmed) | H | Days ahead; confirmed on the day *(unverified timing)* | MLB Stats API; KBO and NPB official sites |
| Line-up | M-H | A few hours before *(unverified timing)* | MLB game feed; club accounts |
| Bullpen use over the last three days | M | Box scores | MLB Stats API |
| Park, temperature, wind | M (H for totals at wind-sensitive parks) | Forecast | Open-Meteo; MLB game-feed wind |
| Umpire | L-M | Day of the game | MLB game feed |
| Pitcher quality | M | Continuous | Baseball Savant, FanGraphs |

Traps: doubleheaders; openers; KBO and NPB ties and extra-inning rules. History: MLB Stats API, Retrosheet, the KBO GetScoreBoardScroll and npb.jp routes.

## Ice hockey (NHL, AHL, Liiga, SHL, Czech Extraliga and others)

| Input | Value | When | Where |
|---|---|---|---|
| Starting goalie | H | Morning skate or warm-up *(unverified timing)* | Team announcements; NHL API game centre |
| Skater absences; line changes | M | Day of the game | Team sites |
| Back-to-backs, travel | M | Schedule | NHL API (measured NHL back-to-back effect: null) |
| Expected goals and goalie quality | M | Nightly | MoneyPuck shot data from 2007-08, 124 attributes per shot |

Traps: regulation-only against overtime/shootout settlement; empty-net goals in puck lines.

## Soccer

| Input | Value | When | Where |
|---|---|---|---|
| Confirmed XI | H | Premier League: submitted at least 75 minutes before kick-off and published from then; most leagues about 60 minutes *(unverified)* | Club and league channels; ESPN API; FotMob (structured fallback) |
| Key absences and suspensions | H | Press conferences; disciplinary lists | League discipline pages; club news |
| Team strength with expected goals | M | After each round | Understat (top leagues). FBref's advanced Opta data was removed in January 2026; its basic results remain |
| Club ratings | M | After each round | ClubElo (CSV API), as a comparator |
| Rotation, fixture congestion | M | Fixture lists | League and cup schedules |

Traps: draws; extra time and penalties in cups; women's leagues have thin data; corners need a named provider (Premier League pulselive, UEFA matchstats).

## AFL and AFLW

| Input | Value | When | Where |
|---|---|---|---|
| Selected 22, emergencies, late changes | H | Team lists at fixed times (Wednesday 6:20 p.m. for Thursday games); final teams about 50-60 minutes before the bounce; a late change only with AFL approval | AFL team lists; Champion Data's selected-team schedule |
| Venue, travel, ground familiarity | H | Fixture | AFL fixture |
| Rain and wind | M | Forecast | Open-Meteo |
| External benchmark | - | Weekly | Squiggle API (set a User-Agent with contact details; cache; do not poll) |

Traps: AFLW is not the AFL (its widths are separate rows); draws exist; sources disagree on the number of named emergencies (three or four): check the current rule.

## Rugby league (NRL, Super League)

| Input | Value | When | Where |
|---|---|---|---|
| Team list and the final 19 | H | Tuesday about 4 p.m. AEST; two players cut 24 hours out; the final 19 at 90 minutes before kick-off | NRL.com team lists |
| Halves, hooker, fullback | H | Same | Same |
| Rain and wind | M | Forecast | Open-Meteo |

Traps: golden point; depleted squads in the State of Origin period.

## Rugby union

| Input | Value | When | Where |
|---|---|---|---|
| Team announcement | H | Usually two days before *(unverified)* | Unions and clubs |
| International strength prior | M | Weekly | World Rugby rankings (its API is undocumented) |
| Weather | M | Forecast | Open-Meteo |

Traps: draws; neutral venues in tournaments.

## American football (NFL, college)

| Input | Value | When | Where |
|---|---|---|---|
| Quarterback status | H | Weekly injury report; inactives 90 minutes before kick-off | Team and league reports |
| Other key positions, offensive line | M | Same | Same |
| Wind and precipitation | M (totals) | Forecast | Open-Meteo |
| History and play-by-play | - | - | nflverse (schedules, play-by-play, injuries, depth charts) |

Traps: key numbers 3 and 7 (use the margin table); overtime rules differ between regular season and playoffs.

## Cricket

| Input | Value | When | Where |
|---|---|---|---|
| XI and toss | H | At the toss, usually about 30 minutes before the start *(unverified)* | Cricbuzz, ESPNcricinfo, board sites |
| Venue scoring and pitch | H for totals | Pitch report on the day | Cricsheet history by venue; pitch reports |
| Rain and DLS | H in rain | Forecast | Open-Meteo |
| Dew in night games | M (weak evidence) | - | Weather (dew point) |

Traps: chase totals are capped near the target; reduced-overs games; the toss is worth about 2.8 points of win probability over 44,000 matches and less in T20 (ESPNcricinfo blog, 2016).

## Tennis

| Input | Value | When | Where |
|---|---|---|---|
| Surface-specific Elo | H | Weekly | Tennis Abstract Elo reports (a 50/50 blend of surface and overall rating) |
| Fitness, recent workload, withdrawals | H | Tournament news | ATP and WTA; tournament sites |
| Serve and return statistics | M | Continuous | Tennis Abstract; ATP and WTA statistics |
| Indoor or outdoor, altitude, balls | L-M | Tournament facts | Tournament sites |

Traps: retirements and walkovers (settlement rules); best of three against best of five; the Sackmann data licence is CC BY-NC-SA and the route's current status is unverified.

## Other sports

Use the sport that is closest in structure, then state the missing competition row and the family prior used. Tier C ([REFERENCE_MODEL_PROTOCOL](REFERENCE_MODEL_PROTOCOL.md)) applies unless the competition has history in the store.

---

# Part E: TIMING_RESEARCH_PROTOCOL

*Formerly `TIMING_RESEARCH_PROTOCOL.md` (original title: Completion-based research and honest event timing). Original kept unchanged at [archive/consolidation_2026-11-07/merged_sources/TIMING_RESEARCH_PROTOCOL.md](archive/consolidation_2026-11-07/merged_sources/TIMING_RESEARCH_PROTOCOL.md).*

**TIMING-2026.10.15-v2 · MDS-2026.10.15-v15.0 · CR-2026.10.15-R4 · SCV-2026.10.15-v10.** Owner instructions 15 October 2026 ([v1](archive/superseded_2026-10-15-3/TIMING_RESEARCH_PROTOCOL.md) → v2: no separate cutoff; the evidence horizon is the game-log scheduled start). Applies to manual cards in every sport, competition and format, including obscure events. [Rules](RULES_REFERENCE.md#part-a-current_rules), [scoring](SCORING_AND_VALIDATION.md), [templates](CARD_AND_LOG_TEMPLATES.md).

## 1. Complete research without a fixed freeze deadline

**No separate cutoff (owner instruction, 15 October 2026).** The evidence horizon of every card is the game's scheduled (expected) start as recorded in the game log for that event. Gather lineups, confirmed starters, bench, injuries, suspensions, team news, weather and other sporting information up until then; whatever is published by then is admissible. The horizon is never set earlier by choice. It moves earlier only to the actual issue time when the card is issued before the scheduled start (later information cannot have been used), or to a verified earlier first play. A rescheduling announced before the scheduled start updates the game-log start with its source; a delay announced after it does not extend the horizon.

There is no mandatory number of minutes before scheduled or actual start at which manual research must stop, finish, freeze or issue. Do not rush incomplete evidence to meet a countdown, stop because play starts, or drop a requested game. Continue until identity/contract, both-side starter/bench/absence research and source escalation, relevant archive/form evidence, coherent calculations, baseline attempt, sensitivity and audit are properly completed. A genuine remaining publication/access gap is recorded with supported uncertainty or qualitative/NO_FORECAST; completion is comprehensive work, not a promise all missing facts will appear.

Recheck decisive availability and actual event state when the analysis is ready. Freeze the completed original at its real issue time, then write/read it back. This immutable issue freeze and the later settlement source snapshot remain essential custody controls, not advance research deadlines. User-specific explicit timing or only-confirmed constraints still apply; report unmet constraints instead of silently changing them.

## 2. Record input quality and issuance separately

Use existing Timing, Known-at, Evidence receipt, Lineup state and A1/A3/A8/A9 metadata. Keep source publication/update, field-known-at horizon, retrieval, research completion, final recheck, actual issue and actual first play as separate facts. Scheduled start and lead minutes are descriptive estimates when not independently verified.

| Dimension | Label | Evidence required |
|---|---|---|
| Actual issue phase | PREGAME | Reliable exact-event not-started observation at issuance or independently evidenced issue before actual first play; no minimum scheduled lead |
| Actual issue phase | POST_START_ISSUE | Reliable evidence play began before the actual issue; keep real issue time even if the analysis is outcome-blind |
| Actual issue phase | TIMING_UNVERIFIED | Actual start/not-started or issue timing insufficient; scheduled time or stale 0-0 alone cannot certify phase |
| Input evidence | CLEAN_PRE_START_INPUTS | Every decision-driving field demonstrably available before the declared horizon and actual first play, no target live/final outcome exposure, with audit and preserved evidence |
| Input evidence | KNOWN_AT_UNVERIFIED | At least one decisive field/start boundary lacks sufficient publication/known-at proof; never assume pre-start availability from its game date |
| Input evidence | OUTCOME_EXPOSED | Analyst or input pipeline observed target in-game/final information; retain LIVE_OBSERVED or HISTORICAL_DIAGNOSTIC and the exact exposure |

Research can continue after start and still qualify as **CLEAN_PRE_START_INPUTS**, if those input and exposure gates actually pass. That is clean pre-start-input research, not a claim its forecast was issued before the game. A post-start issue is recorded and scored in its own lane. Arrival after an advertised start is not automatically late when actual play is independently still not started. Conversely an advertised delay does not prove actual not-started state. Unknown start stays unknown; no arbitrary scheduled buffer replaces evidence.

## 3. Admit only defensible pre-start information

The pre-start evidence horizon is the game-log scheduled start (§1), not a declared earlier time; declare the intended full-event/phase contract before late research. Track the sources and any outcome exposure throughout. Each fact entering CLEAN_PRE_START_INPUTS needs its exact event/field/value, URL/extract, original publication/version known-at time, retrieval time and lineage or honest uncertainty. A later retrieval is permitted only when the pre-start version/value is demonstrably recoverable. Current-page last-update time, historical game date, analyst intent or a new local receipt alone cannot establish old availability.

Do not use target live scores, wickets/balls, pace, shots, goals, live substitutions, realized participation, final boxes or postgame narrative to estimate a purported pre-start full-event forecast. Even an accidentally seen score is recorded as exposure. A status-only started/not-started flag used solely for the timing audit is not outcome exposure; it never conditions the full-event probabilities. A page exposing score, elapsed-play statistics or realized sporting events is different and must be logged as exposure. A verified toss or selection published before actual first play may enter; a lineup first announced during play may improve the factual record but cannot enter the clean pre-start input set. If a later page blends pre-start and live fields and they cannot be separated, exclude the affected input or retain the analysis as unverified/exposed. Missing material facts keep supported scenarios or qualitative status; never infer confirmation from playing time.

Comprehensive availability research continues. Report current confirmed facts separately from the facts admissible to the declared horizon when those differ. Freeze candidate recipe before pricing and baseline before original issue, both bounded by the same horizon; no outcome-driven line choice, hindsight baseline fill, probability or timestamp backdating. A baseline first constructed outcome-blind after start is in the late-issued research lane, not independently pre-start-frozen evidence.

## 4. Counting, retrospective and model boundaries

Retain original T2 primary results for all research requests in their own declared policy/timing/evidence cohort. Show counts and proper scores separately for PREGAME-issued, CLEAN_PRE_START_INPUTS / POST_START_ISSUE, unverified and outcome-exposed research; report zero when none actually qualify and missing baselines as NOT_COMPUTABLE. Near-start PREGAME has no lead-time penalty under the new policy. No arbitrary advance-completion success target remains for manual issuance.

Historical issued timing, contracts, ranks, probabilities, baselines, grades and policy labels remain immutable. New source proof can be a dated addendum, not silent relabelling or reconstruction. Original experimental timing/cohort rules remain unchanged; a new prospective test needs its own preregistration. Do not pool late-issued clean-input research with clean pre-start-issued forecasts to claim prospective predictive advantage. No fitted model, ML/RL/shadow qualification or source certification is conferred by this policy. Independent prospective sporting-model receipts still have to prove their actual pre-start release. The manual completion workflow does not wait for or depend on a model shadow; a late manual card may have no eligible same-event prospective shadow.

## 5. Required checks

Verify every sport retains comprehensive availability/source work and no countdown forces freeze. Exercise legitimate near-start, independently delayed-start and post-start clean-input cases. Reject unknown starts, late-published fields, target outcome exposure, mutable retrospective source versions and invented issue times for their claimed clean/pre-start status. Keep actual timings and cohort arithmetic distinct. [Executed fixtures and receipt](research/verification/framework_change_2026-10-15-1/VERIFICATION_REPORT.md). Correct process or byte checks do not establish predictive improvement.

**Primary-model amendment (15 October 2026):** [PRIMARY_PREDICTION_PROTOCOL](ML_PIPELINE.md#part-a-primary_prediction_protocol) permits the named source-reviewed primary runtime and sporting feedback. Comprehensive availability and truthful timing remain mandatory. These first runtime models do not fit player/lineup effects; record material unsupported scenarios rather than inventing an adjustment. The market decision lab remains excluded.
