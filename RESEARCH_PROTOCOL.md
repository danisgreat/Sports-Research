# Research protocol: completion, persistence, retention, checklists and timing

**AUDIT-v1 supplement:** [AUDIT_REVIEW_PROTOCOL](AUDIT_REVIEW_PROTOCOL.md) adds required opponent-strength and material-availability checks, method/sample/uncertainty evidence, actual-reader/path source decisions, exact rematch identity and final-mini custody. A required unsupported effect becomes UNPRICED plus separately labelled sensitivity; no predictive parameter is inferred from the audit losses. The TIMING-v3 acceptance policy remains; executable first-play review is now required before pooled scoring.

**Consolidated 2026-11-07, CR-2026.11.07-R3.** Five protocols joined verbatim on 2026-11-07 (R2) and then rewritten (R3): contradictions are resolved by the framework's precedence (owner instruction, then [CORE](CORE.md) for v24 cards, then the v24 protocols), repeated text is stated once, and the publication times in Part D were rechecked on 2026-11-07. Part and section numbers are unchanged. What changed and why: [consolidation report](research/verification/framework_change_2026-11-07-3/CONTRADICTIONS.md). Verbatim originals: [archive/consolidation_2026-11-07/merged_sources/](archive/consolidation_2026-11-07/merged_sources/).

Versions in force are in [CURRENT_STATE](CURRENT_STATE.md); rule IDs (MINI-v2, EXH-v1, HIST-v3, AVAIL-v4, RETAIN-v3, MLSCOPE-v3, ENV-v2, REF-v1) are defined where [CORE](CORE.md) §9 lists them. **The owner's standing rule governs every part: research is never rushed or cut short for the start time.**

---

# Part A: RESEARCH_COMPLETION_PROTOCOL

*RC-2026.10.16-v2. Owner instruction, 15 October 2026: complete the analysis, procedures and research regardless of calibration or other problems, for every requested game, including obscure, regional, women's, youth and lower-tier competitions. [RULES_REFERENCE](RULES_REFERENCE.md#part-a-current_rules) governs numerical selection, custody and timing.*

## 1. Strict rule: no dependency failure ends independent research

**Complete and deliver every applicable independent research procedure and the full sport-specific analysis.** Missing calibration, an unavailable or failed model, unsupported markets, incomplete history, unconfirmed lineups, kickoff, an existing mini, an identity or ID disagreement, a writer-lease conflict or a write failure never stop the rest of the work. A refusal, an intake-only supplement, a brief summary or a table of NO_FORECAST labels is not the deliverable.

Track three questions separately: was the research performed; which numerical procedures ran; can the record be issued or appended. A genuine unresolved dependency gets its evidence, the exact affected fields, the impact and the next action. Unattempted independent work is INCOMPLETE, never silently waived. An explicit owner cancellation or scope limit still governs: keep the completed work and state what remains.

An existing active mini is the continuation route: verify its original, sequence, identity, writer authority and unfrozen state, then append. If those checks fail, complete the research as a no-ID `READ_ONLY_DRAFT / NOT_ISSUED` artifact. Never create a competing mini or allocation, reconstruct inaccessible bytes, claim an unissued ID or advance an unwritten footer. A duplicate event gets an addendum under its existing key; originals stay unchanged.

## 2. Required independent work

Execute the selected sport's seven steps and A1–A9 with actual findings, not copied headings:

1. **Identity and timing:** controls, exact competition, season, stage, participants and aliases, venue, endpoint and format, schedule, event state and duplicates. Quarantine ambiguity field by field and never merge different possible fixtures; with genuinely ambiguous identity, document the candidates and finish the work that does not depend on choosing. Timing labels follow Part E.
2. **Both-side availability:** [ROSTER_AVAILABILITY_PROTOCOL](ROSTER_AVAILABILITY_PROTOCOL.md) in full: official releases, both teams, medical and disciplinary sources, permitted providers, original-language organiser, federation and local sources. Starters, bench and absences are assessed separately; a projection never becomes a confirmation. Record queries, URLs, results, failures, times, contradictions and the final recheck. One broken page is not an exhausted search.
3. **History and form:** [HISTORICAL_SOURCE_PROTOCOL](HISTORICAL_SOURCE_PROTOCOL.md) for every event: both sides' L5, L10, L15, L20, season and league, with true usable n, dated rows, endpoint, source and known-at evidence, de-duplication and corrections. One unavailable metric does not suppress the rest. No major-league defaults for an obscure competition; no invented 20-game history.
4. **Sport mechanisms:** the complete sport section: form, home and away or surface and venue effects, matchups, rest, travel and congestion, workload, weather and conditions, competition rules and scoring or phase mechanisms. Separate observed facts, calculated estimates and analyst assumptions. N/A needs a sport or format reason.
5. **Procedures and calculation:** section 3. Attempt the exact-row league baseline and the sensitivity cases. Keep every supported family that completes when another fails, and for an uncomputable quantity explain the missing parameter, data or implementation and what the qualitative evidence still says.
6. **Every requested contract:** exact line, period, endpoint and action. In A2 and A5: supporting and opposing evidence, the calculation or why it cannot be computed, sensitivity to unresolved inputs, and a reasoned conclusion (supported lean, balanced or undefined). The two sides of a complementary pair share one mechanism and are not two pieces of evidence. An undefined term stays `UNKNOWN_DEFINITION` (basketball overtime is defined: BK-OT-1). A row-level NO_FORECAST comes only after this analysis; an unsupported first-half, player or corner market never erases the supported full-game work.
7. **Delivery and verification:** decision block, appendices, audit and the section 4 matrix. Write the card into the active mini, read it back and commit and push it (ENV-v2); canonical IDs wait for prompt 4. If the append is blocked, keep the mini's bytes untouched and deliver the complete separate draft with its actual status. State exact remaining work; never promise an unscheduled retry.

Do not retry an unchanged broken route without progress: try the alternatives and focused repairs, record the failures and finish the independent work. If a task must stop early, label the deliverable INCOMPLETE and list what is pending.

## 3. Execution and fallback hierarchy

*Replaces the pre-v24 order ("experimental ML first, then an analyst comparison labelled NOT_PRIMARY"), which MLSCOPE-v1 and v3 superseded.*

**A. Reference stage first (MLSCOPE-v3).** Run the reference for the competition's tier before typing any probability ([REFERENCE_MODEL_PROTOCOL](REFERENCE_MODEL_PROTOCOL.md)): a tier A release, TB-2-MD or TB-1-MD from a dated standings table, or the league-only baseline. Investigate a concrete failure, correct an admitted input, schema, identity or endpoint problem from evidence and retry where it can be resolved; record the receipt or the exact error. Never bypass the known-at, hash, fit or unsupported-engine guards, and never report an execution that did not happen. A cached forecast for another event never substitutes.

**B. ANALYST_PRIMARY_V1 from the reference.** The card's probability is the frozen reference plus logged adjustments ([RULES_REFERENCE](RULES_REFERENCE.md#part-a-current_rules) section 7; [ADJUSTMENT_LEDGER_PROTOCOL](ADJUSTMENT_LEDGER_PROTOCOL.md)), labelled `ANALYST_PRIMARY_V1 / UNCALIBRATED_ANALYST_PRIMARY`. With no reference (tier C), the card builds its own coherent distribution from [PROBABILITY_TOOLKIT](PROBABILITY_TOOLKIT.md), the sport rules and researched data. Either way: equations, source-backed inputs, explicit assumptions, sample sizes, executed arithmetic, approximation limits and low/base/high sensitivity. Scenario weights need a defensible basis written before pricing; otherwise describe the scenarios in words. A missing calibration certificate is never a reason to skip a feasible calculation, and calibration alone neither invalidates arithmetic nor proves reliability. Never combine incompatible family estimates into a fake joint model.

**C. Full qualitative analysis where honest numbers are impossible.** Finish all available research and every contract assessment with evidence, competing mechanisms, conditional scenarios and limits in words, and a direction only if justified: `UNCALIBRATED_QUALITATIVE` with p_card `NOT_ESTIMATED`, or `NO_FORECAST` for a genuinely indeterminate or undefined row. NO_FORECAST is a numeric disposition, not a reason to stop research. Never force a winner, a probability, four rows or a confirmed lineup.

If a live or final target outcome was seen, continue only with honest `LIVE_OBSERVED` / `HISTORICAL_DIAGNOSTIC` labels; an observed proposition is never a new clean prediction.

<a id="4-completion-receipt-and-return"></a>

## 4. Completion receipt and return

Every card carries this matrix in A9, with pointers and actual outcomes rather than check marks:

| Required procedure | Actual work/evidence and result | Remaining gap, affected field/contract and next action | Status |
|---|---|---|---|
| Authority / exact identity / duplicate / timing | | | |
| Both-side starters / bench / absences / final recheck | | | |
| Online history / source comparison / correction / known-at | | | |
| Both-side L5 / L10 / L15 / L20 / season / league | | | |
| Selected sport's mechanisms / conditions / rules | | | |
| Reference stage receipt / pregame freeze receipt or exact failure | | | |
| Adjustment ledger rows / equations / arithmetic or justified non-numeric handling | | | |
| Every supplied row and declared supported candidate / definitions | | | |
| Expected score / exact-row baseline attempt / sensitivity / dependence | | | |
| All seven sport steps / A1–A9 / audit / custody / delivery readback and commit | | | |

Statuses: DONE; EXHAUSTED_WITH_EVIDENCE (every applicable route attempted, a genuine gap remains); NOT_APPLICABLE with reason; NOT_DONE. Split mixed rows so an unattempted item cannot hide behind a completed one. Keep a contract-by-contract coverage table in A2 and A5.

Overall information status follows Part B §3: **COMPLETE** only when every required field is corroborated, independently recomputed or truly N/A, every contract disposition is evidenced and delivery and readback pass; otherwise **INFORMATION_INCOMPLETE**, with the remaining fields, attempts and next actions. EXHAUSTED_WITH_EVIDENCE describes attempts, not closure; COMPLETE_WITH_DOCUMENTED_GAPS is a legacy label. Retention, model availability and issue status are separate.

Return the findings, supported conclusions and uncertainties, contract dispositions, calculations, the completion matrix, paths, issue and allocation state, remaining gaps and the commit. Never lead with an administrative refusal and stop. Existing cards, frozen ranks and grades, the ID sequence and reserved ranges stay protected; prompts 1–3 commit their own records but assign no canonical ID.

---

# Part B: RESEARCH_EXHAUSTIVENESS_PROTOCOL

*EXH-2026.10.16-v1. Owner instruction, 16 October 2026: pursue the full information needed for every research, log and settlement requirement, switch sources when one is incomplete, verify findings with another source and keep newly found routes for reuse. Applies to every sport, competition, contract and lifecycle task. It changes no statistical threshold, scoring formula or issued record.*

## 1. No early exit; no false closure

Do not stop at the first source, a partial page, a failed request, a familiar provider, a missing English result, an unsupported model, kickoff or an earlier unresolved label. Continue until each applicable requirement has a justified closure. A populated table, link, snippet, repeated claim, NO_FORECAST label or failed first route is not completion. Keep working on independent fields while another is blocked.

Unpublished, private, future or contradictory evidence cannot be made to exist. Never fill such a gap with a guess, a forced WIN, LOSS or VOID, an invented source, a backdated lineup, substituted operator terms or unsupported model output. A real barrier stays `OPEN_BLOCKED_WITH_EVIDENCE` with the attempts, the exact field, the impact and the next action, and the overall status stays INFORMATION_INCOMPLETE. COMPLETE_WITH_DOCUMENTED_GAPS is no longer a new-run label; older records keep theirs. Never claim a background retry, scheduled job or future completion that does not exist; open fields resume at the next authorised review.

## 2. Requirement-by-requirement search loop

1. **Inventory** every required field, side, contract, scope, endpoint, horizon and success condition before declaring completion: authority, custody and IDs; identity, rules and time; both sides' players, roles, bench and absences; the history windows and populations; mechanisms and conditions; reference, input, baseline and calculation evidence; action, void, retirement and OT terms; final, period, innings and field statistics; source and final-at times; scoring and revisions; output, readback and retention. A completed result does not close its definition, player or timing fields.
2. **Consult** [SOURCES](SOURCES.md), [RESEARCH_SOURCE_REGISTER](RESEARCH_SOURCE_REGISTER.md) and prior settlement registers. Open the actual page, document or data endpoint (exact match IDs, dates, tabs, pagination, original scorecards and PDFs) and read the needed fields, not a summary. Old route notes are discovery aids that need a fresh check.
3. **Switch** at once when a field is missing, truncated, inaccessible, stale or ambiguous: the organiser, league or federation, the official match record and both teams first; then permitted structured providers, original-language local sources, broadcasters and accredited reporters. Search alternate names and scripts, dates, rounds and native IDs. A schedule, roster or probable selection never stands in for a final, a lineup or an action field.
4. **Assemble** missing pieces across sources with field-level mapping; never borrow from other games, genders, age groups, seasons, formats or endpoints. Reconcile reschedules, doubleheaders and aliases first. Record queries and results in SOURCE_SEARCH_ATTEMPTS.csv and discoveries in SOURCE_DISCOVERY_REGISTER.csv.
5. **Corroborate** every material field with a second opened source, comparing identity, orientation, endpoint, value and time. Mirrors, syndication and one feed on two domains are not independent; unknown lineage stays UNKNOWN and fails an independence claim. The normative rule or contract source governs its own scope. Disagreement calls for more owner or correction evidence, never averaging, a majority or last-page-wins.
6. **Recompute** calculated values from their inputs and read back custody, byte, hash and ID results. These are verification operations, not extra citations.
7. **Revisit** every open field after each discovery, following new links, archives, gamebooks and local-language routes. Before a blocked disposition, review the register and every applicable route family and record what was actually tried.
8. **Recheck** fragile fields at the release window and before issue or settlement. Known-at, publication, correction, retrieval, event and issue times follow Part E. A later fact may settle a result or inform a future forecast; it never proves earlier confirmation or repairs outcome exposure.

## 3. Closure and corroboration states

Each factual requirement has a REQUIREMENT_CLOSURE.csv row, split by field, side and scope. `VERIFIED_CORROBORATED`: the primary and second opened sources match, scope, time and endpoint are compatible, collector independence is evidenced and conflicts are resolved. `VERIFIED_RECALCULATED`: reproducible arithmetic or a mechanical custody check, with the check named. `NOT_APPLICABLE`: a real sport, format or task reason; never cover for a missing field or model.

Open states: `SINGLE_SOURCE_OPEN`, `CORROBORATION_PENDING`, `LINEAGE_UNKNOWN_OPEN`, `CONFLICT_OPEN`, `NOT_ATTEMPTED`, `OPEN_BLOCKED_WITH_EVIDENCE`. A source's authority does not waive the second-source search; two sources with one collector need a third; if no independent confirmation can be obtained, the requirement stays open with the barrier explained.

Overall **COMPLETE** only when every required row is VERIFIED_CORROBORATED, VERIFIED_RECALCULATED or justified NOT_APPLICABLE, every contract has an evidenced disposition and the output, readback and register checks pass; otherwise **INFORMATION_INCOMPLETE**. The sporting, evidence-grade and forecast vocabularies stay separate from this status.

## 4. Mandatory settlement section and reusable registers

Every mini-settlement-10 package has a visible section titled **Source discovery, corroboration and reuse register**: every source used or rechecked, newly found routes, the fields each exposes, corroborating sources and conflicts, and every remaining gap, with links to the three sidecars below. An empty list needs an evidenced no-discovery or no-access result.

- **SOURCE_DISCOVERY_REGISTER.csv:** stable source ID, discovery time, phase, sport, competition and scope, publisher and collector lineage, URL, navigation or query, fields observed and absent, publication, update and retrieval times, access result, capture and hash, corroborating IDs and outcome, reuse limits and status.
- **SOURCE_SEARCH_ATTEMPTS.csv:** attempt ID, event, requirement and field, time, route, access result, fields found, unresolved pieces, collector relation, next action and evidence pointer. Failed and partial searches stay visible; an unopened source is never marked checked.
- **REQUIREMENT_CLOSURE.csv:** requirement, event, phase, side, field, scope and horizon, primary and corroborating source or check, independence result, status, remaining issue, next action, actor, due time and automation status.

Templates: `research/prompts/templates/`. Source IDs and observations are stable; a new discovery or changed access adds a dated observation and never overwrites a receipt or failed attempt. Old packages keep their formats; a new review is a new package or dated addendum. A register records observed capabilities, not a promise of availability.

## 5. Reuse, write scope and publication

Start every research and settlement task from the shared register, SOURCES and prior registers, revalidate the exact event and field, and continue beyond them. One complete fact from a source says nothing about its other fields, seasons or historical known-at. Raw captures and helpers stay outside git; market-free extracts and Markdown or CSV receipts stay in authorised scopes; odds, tips, fantasy and market data never enter research.

Prompts 1–3 write and commit only their own mini, card and settlement records and the files their commands produce; they do not edit shared registers. They list candidate shared additions, and prompt 4 appends the deduplicated, dated observations to RESEARCH_SOURCE_REGISTER within its declared scope. Prompts 7 and 8 maintain the shared source map. Reuse never changes old cards, grades, canonical allocation, accepted source truth or model qualification.

## 6. Audit and edge cases

C13, C20 and A3, A8, A9 check field-level research and corroboration; settlement check S17 checks the visible source section, the three sidecars, requirement coverage, genuine second sources, reuse, barriers and readback (mini-settlement-8 and earlier keep their own checks). Record actual PASS, FAIL, NOT_VERIFIED or N/A evidence; a checklist alone is not an executed search.

A partial lineup needs another route for the bench and absences; a final score does not close corners, periods, OT or terms; an authoritative single source still needs corroboration; two mirrors never pass independence; conflicting endpoints stay open; private terms, unpublished lineups and future final times cannot be invented. A window with fewer eligible games closes only when the short population and its coverage are verified: missing collection is not proof that games do not exist, and the actual n is always kept. Process improvements never demonstrate predictive gain.

---

# Part C: RESEARCH_RETENTION_PROTOCOL

*RETAIN-v3 (prompt statement of 22 October 2026, P-2026.10.22-v24.0), which superseded RETAIN-v2 (16 October 2026) and RETAIN-v1. Prompts 1–3 keep researched events under stable local keys; canonical P-IDs are assigned only in the prompt-4 import at the end of settlement (MINI-v2, [WORKFLOW](WORKFLOW.md#part-b-mini_log_identity_protocol) Part B).*

## 1. Local research and delivery before canonical allocation

Record every researched event in the active mini under its stable `LOCAL-<MINI_KEY>-G####` key with the full research and its ANALYST_PRIMARY_V1 probabilities (or a bounded range, `UNCALIBRATED_QUALITATIVE` or a `NO_FORECAST` row with the reason). Append the card, intake row and footer after every game request, read the mini back, and commit and push it (ENV-v2); the committed mini is the updated-document deliverable (C22). The reference stage precedes the card and the pregame freeze follows it. Canonical ID: `NOT_ASSIGNED / PROMPT_4_IMPORT`; never assign or reserve a number during research or settlement. A missing model, adapter, module, baseline, calibration, data or receipt never prevents the local record or its later import. A duplicate or addendum keeps its original key; an existing canonical reference keeps its ID.

Incomplete required facts stay INFORMATION_INCOMPLETE (Part B); retaining research is separate from evidence completion. Never invent probabilities, execution, scores or pregame timing. Only real identity, custody, lease, freeze or write conflicts block an append; then keep the independent research and deliver an honest separate draft, never a reconstruction of inaccessible bytes.

## 2. Honest execution disposition without a fake receipt

Run the reference stage and the pregame freeze when they can run, and keep their receipts. A card records the freeze disposition and receipt path: EXECUTED, NOT_RUN_NO_RELEASE, NOT_RUN_STALE_RELEASE, NOT_RUN_INPUT_REFUSED or FAILED (R36), with the concrete reason; never a bare ML_NOT_RUN, a repeated known failure or a fabricated receipt. C21 checks that the probability method, inputs and arithmetic are disclosed.

New minis are mini-log-10 / mini-settlement-10 with **no execution-manifest companion**: model rows keep their own receipts under MLSCOPE-v3 (prompts 2 and 3). A legacy mini's `ML_EXECUTION_MANIFEST.csv` and bundles are left untouched. Old cores and formats never change; canonical assignment never changes a frozen request, native event ID, probability, feedback row or hash.

## 3. Import may precede settlement; only prompt 4 assigns canonical IDs

An authorised prompt 4 import may retain events before settlement. It inventories every source, reconciles each event against canonical and native aliases, reuses committed mappings, allocates genuinely new IDs contiguously in the verified import plan (reserved ranges respected), appends literal local cores inside canonical wrappers, records the full local-to-canonical map separately, and updates the highest and next ID only after a successful append and readback. Duplicates, addenda and reruns consume no ID. Pending outcomes stay `PENDING_SETTLEMENT / OUTCOME_NOT_REVIEWED`.

Before import, prompt 3 settles local keys with the mapping `NOT_ASSIGNED`; after import the same key has its verified canonical ID, and later revisions keep that mapping without rewriting the source. Events after a freeze go to the next mini. Legacy issued P labels stay literal and are mapped explicitly at import.

## 4. Two kinds of learning evidence

**Future-development targets.** Keep verified final endpoints and grades with source, time and hash, the original research and features, the actual availability and exposure, the effective revision and the feature-admission status; prompt 3 keeps reviewed LABELS.csv and evidence by local key. The exporter needs a canonical P-ID, so it runs only after prompt 4 has verified the assignment, on the canonical original and settlement wrappers:

```text
python -m ml.research_learning retain --card-id P-NNN --record CANONICAL_WRAPPER.md --settlement MAPPED_SETTLEMENT_WRAPPER.md --labels LABELS.csv --out research/training_candidates/P-NNN/revision-1
python -m ml.research_learning verify --candidate research/training_candidates/P-NNN/revision-1
```

LABELS.csv schema: `event_id,competition,endpoint,label_key,label_value,label_unit,event_at,final_at,available_at,source_url,evidence_path,evidence_sha256,definition_status,review_status,revision_id,feature_status`; review_status `TERMINAL_LABEL_REVIEWED`; units GOALS, POINTS, RUNS, GAMES, SETS, WICKETS, BALLS or OUTCOME (WIN/LOSS/PUSH/VOID). Labels are `RESEARCH_TRAINING_CANDIDATE / LABELS_RETAINED_NOT_MODEL_FEEDBACK`; a trusted target does not establish pre-start feature availability or skill. A candidate enters an immutable training release through `python -m ml training build --candidates research/training_candidates` once its structured research export has been ingested; one without exported history is listed `CANDIDATE_WITHOUT_STRUCTURED_HISTORY`, never dropped or given invented features ([ML_PIPELINE](ML_PIPELINE.md#part-c-learning_pipeline_protocol) Part C §5).

**Expert feedback.** Only a frozen model row settled through its own receipt supplies a loss (prompt 3, `cycle settle`). Without one, keep the verified target and mark feedback `NOT_APPLICABLE_NO_MODEL`. Never manufacture probabilities, propensities, losses or feedback; one native event contributes once.

## 5. Counts and custody

Report separately: locally retained cards, canonically imported events, numeric forecast coverage, feedback coverage and label-export coverage. Analyst rows never inflate model, calibration or prospective cohorts. Existing cards, canonical state and IDs, issued ranks and grades, old formats and source bytes stay protected. Checks C2, C16, C21, C22 and S18 with actual evidence.

---

# Part D: RESEARCH_CHECKLISTS

*CHECK-v1 (REV-14 of the [22 October review](research/verification/review_2026-10-22_framework_revamp/REPORT.md)). Work the **H** rows first, timed to when they are published, then **M**, and **L** only when the first two are closed. Each fact that moves a number becomes one adjustment-ledger row with an [EFFECT_TABLES](PARAMETERS.md#part-b-effect_tables) size, or a `SCENARIO` row when there is none. H can move a fair probability by several points, M by one to three, L rarely matters. Publication times were checked on 22 October and rechecked where marked on 7 November 2026; a league's own rule change supersedes this page. Source routes are in [SOURCES](SOURCES.md); this page ranks inputs and does not replace the routes. Timing follows Part E.*

**Every sport:** the scheduled start and timezone; the venue and whether it is neutral; the stage and format (overtime, extra time, tie rules); weather for outdoor play in venue-local time for the match window (Open-Meteo, keyless); travel and schedule congestion; the competition's [parameter row](PARAMETERS.md#part-a-competition_parameters).

## Basketball (NBA, WNBA, NBL, EuroLeague, ACB, B.League, KBL and others)

| Input | Value | When it is published | Where |
|---|---|---|---|
| Status of the top-minute players | H | NBA game day: a report between 11 a.m. and 1 p.m. local (8–10 a.m. for tip-offs at 5 p.m. or earlier), except the second game of a back-to-back; the report updates through the day (rechecked 2026-11-07; the league adjusted these rules in December 2025). The day-before 5 p.m. deadline was not re-confirmed on 2026-11-07 | official.nba.com injury report; team and league sites elsewhere; ESPN site API for NBL and WNBA starters and did-not-play |
| Starting five; minute restrictions | H | Shortly before the tip | Team announcements; league game centres |
| Rest, back-to-backs, travel | M | Schedule | League schedule; ESPN API (measured NBA back-to-back effect: [EFFECT_TABLES](PARAMETERS.md#part-b-effect_tables), half size) |
| Player impact and minutes history | M | Continuous | NBA stats, Basketball-Reference; impact metrics use different scales |
| Officials | L | NBA about 9 a.m. ET on game day *(unverified)* | official.nba.com referee assignments |

Traps: preseason games; competition-specific quarter lengths; never carry NBA defaults into FIBA leagues; every line includes overtime (BK-OT-1). History: the ESPN scoreboard and Basketball-Reference schedule (two lineages); league routes in SOURCES 3.2.

## Baseball (MLB, KBO, NPB, CPBL, LMB)

| Input | Value | When | Where |
|---|---|---|---|
| Starting pitcher (probable, then confirmed) | H | Days ahead; confirmed on the day *(unverified)* | MLB Stats API; KBO and NPB official sites |
| Line-up | M-H | A few hours before *(unverified)* | MLB game feed; club accounts |
| Bullpen use over the last three days | M | Box scores | MLB Stats API |
| Park, temperature, wind | M (H for totals at wind-sensitive parks) | Forecast | Open-Meteo; MLB game-feed wind |
| Umpire | L-M | Day of the game | MLB game feed |
| Pitcher quality | M | Continuous | Baseball Savant, FanGraphs |

Traps: doubleheaders; openers; KBO and NPB ties and extra-inning rules. History: MLB Stats API, Retrosheet, the KBO GetScoreBoardScroll and npb.jp routes.

## Ice hockey (NHL, AHL, Liiga, SHL, Czech Extraliga and others)

| Input | Value | When | Where |
|---|---|---|---|
| Starting goalie | H | Morning skate or warm-up *(unverified; no league-wide publication rule)* | Team announcements; NHL API game centre |
| Skater absences; line changes | M | Day of the game | Team sites |
| Back-to-backs, travel | M | Schedule | NHL API (measured NHL back-to-back effect: null) |
| Expected goals and goalie quality | M | Nightly | MoneyPuck shot data from 2007-08 |

Traps: regulation-only against overtime and shootout settlement; empty-net goals in puck lines.

## Soccer

| Input | Value | When | Where |
|---|---|---|---|
| Confirmed XI | H | Premier League: confirmed XIs and matchday squads are submitted at least 75 minutes before kick-off and may be published from then (handbook rule from 2024/25; the one-hour embargo was removed; rechecked 2026-11-07 from reports, not the current handbook text). EFL about 60 minutes; most other leagues about 60 minutes *(unverified)* | Club and league channels; ESPN API; FotMob (structured fallback) |
| Key absences and suspensions | H | Press conferences; disciplinary lists | League discipline pages; club news |
| Team strength with expected goals | M | After each round | Understat (top leagues). FBref's advanced Opta data was removed in January 2026; its basic results remain |
| Club ratings | M | After each round | ClubElo (CSV API), as a comparator |
| Rotation, fixture congestion | M | Fixture lists | League and cup schedules |

Traps: draws; extra time and penalties in cups; women's leagues have thin data; corners need a named provider (Premier League pulselive, UEFA matchstats).

## AFL and AFLW

| Input | Value | When | Where |
|---|---|---|---|
| Selected team, emergencies, late changes | H | Team lists at 6:20 p.m. on fixed days (Wednesday for Thursday games, Friday for Sunday games, Sunday for Monday games, per Champion Data's selected-team schedule); final teams lodged by 60 minutes before the start, usually released 50–60 minutes before; a change after release needs AFL approval (rechecked 2026-11-07) | AFL team lists; Champion Data's selected-team schedule |
| Venue, travel, ground familiarity | H | Fixture | AFL fixture |
| Rain and wind | M | Forecast | Open-Meteo |
| External benchmark | - | Weekly | Squiggle API (set a User-Agent with contact details; cache; do not poll) |

Traps: AFLW is not the AFL (separate width rows); draws exist; the number of named emergencies is unsettled across sources (Champion Data's schedule lists 18 + 5 interchange + 3 emergencies; AFL.com.au articles describe four emergencies): check the current rule for the round.

## Rugby league (NRL, Super League)

| Input | Value | When | Where |
|---|---|---|---|
| Team list and the final 19 | H | Tuesday about 4 p.m. AEST; two players cut 24 hours before kick-off; the final 19 confirmed 90 minutes before kick-off (NRL.com 2026 round team lists, rechecked 2026-11-07) | NRL.com team lists |
| Halves, hooker, fullback | H | Same | Same |
| Rain and wind | M | Forecast | Open-Meteo |

Traps: golden point; depleted squads in the State of Origin period.

## Rugby union

| Input | Value | When | Where |
|---|---|---|---|
| Team announcement | H | Usually two days before *(unverified)* | Unions and clubs |
| International strength prior | M | Weekly | World Rugby rankings (API undocumented) |
| Weather | M | Forecast | Open-Meteo |

Traps: draws; neutral venues in tournaments.

## American football (NFL, college)

| Input | Value | When | Where |
|---|---|---|---|
| Quarterback status | H | Weekly injury report; inactives about 90 minutes before kick-off (long-standing practice; not re-confirmed for 2026) | Team and league reports |
| Other key positions, offensive line | M | Same | Same |
| Wind and precipitation | M (totals) | Forecast | Open-Meteo |
| History and play-by-play | - | - | nflverse (schedules, play-by-play, injuries, depth charts) |

Traps: key numbers 3 and 7 (use the margin table); overtime rules differ between the regular season and the playoffs.

## Cricket

| Input | Value | When | Where |
|---|---|---|---|
| XI and toss | H | At the toss, usually about 30 minutes before the start *(unverified)* | Cricbuzz, ESPNcricinfo, board sites |
| Venue scoring and pitch | H for totals | Pitch report on the day | Cricsheet history by venue; pitch reports |
| Rain and DLS | H in rain | Forecast | Open-Meteo |
| Dew in night games | M (weak evidence) | - | Weather (dew point) |

Traps: chase totals are capped near the target; reduced-overs games; the toss is worth about 2.8 points of win probability over 44,000 matches and less in T20 (ESPNcricinfo, 2016).

## Tennis

| Input | Value | When | Where |
|---|---|---|---|
| Surface-specific Elo | H | Weekly | Tennis Abstract Elo reports (a 50/50 blend of surface and overall rating) |
| Fitness, recent workload, withdrawals | H | Tournament news | ATP and WTA; tournament sites |
| Serve and return statistics | M | Continuous | Tennis Abstract; ATP and WTA statistics |
| Indoor or outdoor, altitude, balls | L-M | Tournament facts | Tournament sites |

Traps: retirements and walkovers (settlement rules); best of three against best of five; the Sackmann data licence is CC BY-NC-SA and the route's current status is unverified.

## Other sports

Use the closest sport in structure, then state the missing competition row and the family prior used. Tier C ([REFERENCE_MODEL_PROTOCOL](REFERENCE_MODEL_PROTOCOL.md)) applies unless the competition has history in the store.

---

# Part E: TIMING_RESEARCH_PROTOCOL

*TIMING-2026.10.15-v2 (owner instructions of 15 October 2026: no separate cutoff; the evidence horizon is the game-log scheduled start). Applies to every card in every sport, competition and format. The owner's standing rule applies: research is never rushed for the start time.*

## 1. Complete research without a fixed freeze deadline

**No separate cutoff.** The evidence horizon of every card is the game's scheduled start as recorded in the game log. Lineups, starters, bench, injuries, suspensions, team news, weather and other sporting information are gathered up to then, and whatever is published by then is admissible. The horizon is never set earlier by choice; it moves earlier only to an actual issue before the scheduled start, or to a verified earlier first play. A reschedule announced before the scheduled start updates the game-log start with its source; a delay announced after it does not extend the horizon.

No number of minutes before the start forces research to stop, finish, freeze or issue. Never rush incomplete evidence, stop because play starts or drop a requested game. Continue until identity and contract, both-side availability with source escalation, history and form, the reference and adjustments, the baseline attempt, sensitivity and the audit are complete. A late request may be issued as a fast card first, with the full card as a dated addendum ([REFERENCE_MODEL_PROTOCOL](REFERENCE_MODEL_PROTOCOL.md) §7); the full research is never cut short. A genuine remaining gap is recorded with supported uncertainty, or qualitative or NO_FORECAST handling.

When the analysis is ready, recheck decisive availability and the actual event state, freeze the completed card at its real issue time and write and read it back. The issue freeze and the later settlement snapshot are custody controls, not research deadlines. An owner's explicit timing or only-confirmed constraint still applies; report it if unmet.

## 2. Record input quality and issuance separately

**TIMING-v3 (CR-2026.11.15-R1, owner instruction 15 November 2026).** Research that **begins before the actual start** is enough. A card whose writing finishes after the start counts as a forecast of record and is scored together with `PREGAME` cards when it is labelled `PRE_START_RESEARCH` and declares, in its PICKS_V2 header: `research_started_at` (when research began), `not_started_observed_at` and `not_started_source` (an official live page or match centre, observed at or after the research start, showing play had not begun) and `outcome_exposure: NONE_RECORDED`. Decision inputs still follow the horizon in §1 (facts published by the scheduled start), and no live or final target information may be used. Never shorten research or request a game earlier to meet a time: late lineups and team news only appear near the start. At settlement the official actual first play is checked; if research in fact began after it, the card is revised to `POST_START_ISSUE` by a dated settlement revision.

Use the card's Timing, Known-at, Evidence receipt, Lineup state and A1, A3, A8, A9 metadata. Source publication or update, the horizon, retrieval, research completion, final recheck, actual issue and actual first play are separate facts. A scheduled start and lead minutes are descriptive unless independently verified.

| Dimension | Label | Evidence required |
|---|---|---|
| Actual issue phase | PREGAME | A reliable exact-event not-started observation at issue, or an independently evidenced issue before actual first play; no minimum lead |
| Actual issue phase | PRE_START_RESEARCH | TIMING-v3: issued after the start, with a declared research start and a not-started observation at or after it, and no outcome exposure; scored with PREGAME |
| Actual issue phase | POST_START_ISSUE | Reliable evidence that play began before the actual issue and before research began (or no research-start declaration); the real issue time is kept even if the analysis is outcome-blind |
| Actual issue phase | TIMING_UNVERIFIED | Insufficient start, not-started or issue evidence; a scheduled time or a stale 0–0 cannot certify the phase |
| Input evidence | CLEAN_PRE_START_INPUTS | Every decision-driving field demonstrably available before the horizon and the actual first play, with no target live or final exposure, audited and preserved |
| Input evidence | KNOWN_AT_UNVERIFIED | At least one decisive field or start boundary lacks publication or known-at proof; a game date never proves availability |
| Input evidence | OUTCOME_EXPOSED | The analyst or a pipeline observed in-game or final target information; labelled LIVE_OBSERVED or HISTORICAL_DIAGNOSTIC with the exact exposure |

Research that continues after the start can still be CLEAN_PRE_START_INPUTS if the input and exposure checks pass; that is clean-input research, not a pre-start issue, and it is scored in its own lane. Arriving after an advertised start is not late if play has verifiably not begun; an advertised delay does not prove a not-started state. An unknown start stays unknown.

## 3. Admit only defensible pre-start information

Declare the full-event or phase contract before late research and track sources and any exposure throughout. Each fact entering CLEAN_PRE_START_INPUTS needs its exact event, field and value, URL or extract, original publication or version time, retrieval time and lineage or an honest uncertainty. A later retrieval is admissible only when the pre-start value is demonstrably recoverable; a page's last-update time, a game date, analyst intent or a new local receipt cannot establish old availability.

Never use target live scores, wickets, balls, pace, shots, goals, live substitutions, realised participation, final boxes or postgame narrative to build a pre-start forecast; an accidentally seen score is recorded as exposure. A status-only started or not-started flag used solely for the timing audit is not exposure and never conditions the probabilities. A verified toss or selection published before first play may enter; a lineup first announced during play may improve the record but not the clean input set. A page that mixes pre-start and live fields inseparably is excluded or kept as unverified or exposed.

Report current confirmed facts separately from those admissible at the horizon when they differ. Freeze the candidate recipe before pricing and the baseline before issue, both bounded by the same horizon: no outcome-driven line choice, hindsight baseline fill or backdating. A baseline first built outcome-blind after the start belongs to the late-issued lane.

## 4. Counting, retrospective and model boundaries

Keep each card's results in its own declared policy, timing and evidence cohort: counts and proper scores separately for PREGAME, CLEAN_PRE_START_INPUTS / POST_START_ISSUE, unverified and outcome-exposed work; zero when none qualify; missing baselines NOT_COMPUTABLE. There is no lead-time penalty and no advance-completion target.

Historical timing, contracts, ranks, probabilities, baselines, grades and labels are immutable; new source proof is a dated addendum. A new prospective test needs its own preregistration. Under TIMING-v3, `PRE_START_RESEARCH` cards are pooled with `PREGAME` cards; other late-issued clean-input research (research begun after the start) is never pooled with them to claim a prospective advantage. **Models (MLSCOPE-v3):** a model reaches a card only as the reference frozen before the card; the reference stage and the pregame freeze each carry their own pre-start receipts. The manual card never waits for a model shadow, and a late card may have no eligible prospective row. The current reference models fit no player or lineup effects; those facts enter as ledger rows or declared scenarios, never as invented adjustments.

## 5. Required checks

Every sport keeps comprehensive availability and source work, and no countdown forces a freeze. Near-start, independently delayed and post-start clean-input cases are handled legitimately; unknown starts, late-published fields, target exposure, mutable source versions and invented issue times are rejected for any clean or pre-start claim. Actual timings and cohort arithmetic stay distinct ([executed fixtures and receipt](research/verification/framework_change_2026-10-15-1/VERIFICATION_REPORT.md)). Correct process or byte checks do not establish predictive improvement.
