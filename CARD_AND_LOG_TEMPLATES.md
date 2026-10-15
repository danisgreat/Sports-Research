# Card, mini, settlement and canonical formats

**mini-log-7 · mini-settlement-6 · canonical-md-1.** Authority: MDS-2026.10.15-v15.0 / CR-2026.10.15-R4 / SCV-2026.10.15-v10 / SEL-2026.10.12-v3. [Rules](CURRENT_RULES.md) and [selection definitions](SELECTION_RULES.md) control semantics. Previous formats: [mini-log-6 / mini-settlement-5](archive/superseded_2026-10-12/CARD_AND_LOG_TEMPLATES.md).

<a id="local-mini-format-mini-log-2"></a>

## 1. Compatibility

Old minis finish in their original format. Never insert baselines, gates, expected scores, form windows or missing cutoffs into an old card. New dated addenda may carry unresolved status or diagnostic fields without changing its original selection/scoring version. Old numeric self-audits are interpreted against the original format, with gaps documented rather than repaired by fabrication. For new minis, use the structures below. A mini-log-6 mini still open on 2026-10-12 finishes as mini-log-6; its next mini is mini-log-7. Example IDs beginning EXAMPLE are not P-IDs and must never be imported.

**What mini-log-7 adds:**
- **Authority and lifecycle:** authority mode (R09), writer lease (R15), frozen-status pointer (R16), request intake (R22), executable queue fields (R38).
- **On each card:** known-at line (R28), lineup state and pricing basis (PR-03, PR-04), form-window block (PR-01), line distance and `p_base` columns (R33, PR-03), baseline coverage (PR-06), and the two new shadows (PR-05).

**What mini-settlement-6 adds:** revision keys with parent chains (R17), a frozen-source receipt (R16), evidence-stratified scores (R23) and executable queue fields.

## 2. Mini

Create `Mini Prediction Log - <FIRST> onward - <date>/PREDICTION_MINI_RUNNING_LOG_<FIRST>_ONWARD.md`:

```markdown
<!-- MINI-LOG-FORMAT: mini-log-7 -->
# Prediction Mini Running Log — <FIRST> onward

## A. Authority snapshot
| Field | Value |
|---|---|
| Authority mode | PUBLISHED_MAIN_PINNED <full SHA> or LOCAL_WORKING_TREE <branch/HEAD> |
| Repository / branch / read HEAD | <actual local or published authority> |
| Relevant working differences | <paths or NONE; which version was applied> |
| Method / control / scoring / selection | <versions> |
| Active Combined Log | <resolved path> |
| Highest committed / next canonical ID | <current values> |
| Outstanding local minis and IDs | <contiguous inventory or NONE> |
| First working ID | <reconciled next local ID> |
| Issuing writer / lease start / lease expiry | <named session or person / ISO time / ISO time> |
| Lease hand-overs | <from → to, time, reason; or NONE> |
| Frozen for settlement | NO, or YES: <FROZEN_SOURCE receipt path> |
| Reading receipt / opened at | <paths and ISO time with offset> |
| Mode | LOCAL_MINI_STAGING |

SPORTS_ONLY / MARKET_BLIND · RESEARCH_ONLY_NOT_CERTIFIED · CANONICAL_IMPORT_STATUS: PENDING

## B. Local ID rules
Creating this mini consumes no ID. One retained event receives one permanent working ID; canonical status requires import. Addenda/carryovers consume none. No silent skipping, reuse or renumbering. Only a complete written/read-back card advances the footer. Only the issuing writer appends cards. Another writer must wait for lease expiry or a recorded hand-over. Never append to a mini marked frozen; route the event to the next authorised mini.

## C. Carryover and evidence queue
| ID | Event key | Queue | Original card / frozen pick table | Latest revision | Open field | Responsible actor | Next source + exact field | Due (ISO, tz) | Final-time basis | Last attempt | Scheduled automation |
|---|---|---|---|---|---|---|---|---|---|---|---|
<one row per unresolved event/field, PENDING_EVENT or UNRESOLVED_EVIDENCE; or NONE>

## D. Request intake
| Request key | Received (ISO, tz) | Event / alias as requested | Disposition | Card or addendum pointer, or no-card reason |
|---|---|---|---|---|
<one row per request, including duplicates and blocked requests. Disposition: CARD, ADDENDUM_TO_EXISTING_ID, DUPLICATE_OF_EXISTING_ID, BLOCKED, OUT_OF_SCOPE, READ_ONLY_DRAFT or PENDING. Requests allocate no ID>

# NEW LOCAL EVENT CARDS

# RUNNING FOOTER
<!-- BEGIN FOOTER -->
| Field | Value |
|---|---|
| Highest new working ID used / next working ID | NONE / <FIRST> |
| Repository next-ID snapshot | <value> |
| New cards / numeric / qualitative / NO_FORECAST | 0 / 0 / 0 / 0 |
| Pending events / unresolved evidence records | <counts separately> |
| Local mini status / import status | ACTIVE / PENDING |
| GitHub writes performed | NO |
<!-- END FOOTER -->
```

Carryovers preserve canonical or LOCAL_UNIMPORTED status accurately; never call an unimported local card canonical. Do not duplicate a new card for an existing event. A cap breach is reported, never used to drop a queue item.

## 3. Card

Insert immediately before the footer. Preserve earlier card/addendum bytes; only the mutable running footer changes. No heading inside a local card starts `## P-`.

```markdown
<!-- BEGIN CARD P-NNN -->
## Card · P-NNN · <sport / league> · <event> · <local event date>

- **Working ID:** P-NNN — LOCAL_WORKING_ID — PENDING_CANONICAL_IMPORT
- **Event key / native ID / aliases:** <exact identity; unknown native ID explicit>
- **Authority:** <method/control/scoring/selection/HEAD; working differences>
- **Analysis status:** MODEL_ASSISTED_PRIMARY_V3 / EXPERIMENTAL_PRIMARY_NOT_CERTIFIED | UNCALIBRATED_QUALITATIVE | NO_FORECAST
- **Timing:** <state; cutoff = game-log scheduled start (or earlier actual issue / verified first play, with which); research completion; actual issue time; source state/recheck time; source publication time; actual start or NOT_VERIFIED>
- **Scheduled start:** <venue timezone, UTC and Australia/Sydney with offsets; source>
- **Scheduled lead / band:** <descriptive minutes only; actual issue phase PREGAME / POST_START_ISSUE / TIMING_UNVERIFIED; input evidence CLEAN_PRE_START_INPUTS / KNOWN_AT_UNVERIFIED / OUTCOME_EXPOSED>
- **Endpoint / definition:** <regulation/extras; tie/push/void/retirement/listed pitcher/abandonment convention; operator status>
- **Distribution object:** <id/family/parameters/approximation or NOT_COMPUTED>
- **Expected score:** <sport units; team means/SDs, total and signed margin, endpoint; N/A/NOT_COMPUTED as appropriate>
- **Baseline:** <BASELINE_LEAGUE_V1 recipe, cohort dates/n, parameters, cutoff/provenance or BASELINE_UNAVAILABLE reason>
- **Regime flags / context:** <approved flags; other context separately>
- **Settlement fields / capture plan:** <row-to-provider/field mapping; due time; responsible action; scheduled job YES/NO>
- **Rules read / archive check:** <paths/sections; actual files/rows/date window/filters/findings/gaps>
- **Evidence receipt:** <decisive claim/source/field/extract/source time/retrieval time/lineage; detail in A3>
- **Known-at:** <archive capture date; any KNOWN_AT_UNVERIFIED input and confirmation it does not decide Rank 1>
- **Lineup state / issue step:** <CONFIRMED (source, time) or LINEUP_UNCONFIRMED; actual research-completion/availability-check times; complete-search result; no required countdown>
- **Pricing basis:** <BASE (no input labelled uncertain) or MIXTURE low/base/high = <w1/w2/w3>, with the uncertain input named>
- **Form windows:** <per side: L5/L10/L15/L20/season/league for the scored and conceded rate, with n; the blended rate used; full table in A3 (§3b)>

### Decision block
<One-sentence assessment and principal uncertainty; mean score is not exact-score mode.>

| Rank | Role | Tag | Contract key / exact proposition | p_card | p_base | BASELINE_P | Line distance (units / z) | Probability basis | Main failure route |
|---|---|---|---|---|---|---|---|---|---|
| 1 | PICK | SUPPLIED or ANALYST_DERIVED | <line/period/endpoint/action> | <p or NOT_ESTIMATED> | <base-only p, or = p_card when BASE> | <p or missing reason> | <signed line − centre; z or N/A> | <distribution id or QUALITATIVE> | <mechanism> |
<up to four actual supported rows; roles PICK for ranks 1–2, INFORMATIONAL thereafter>

**Baseline coverage:** <rows with BASELINE_P>/<numeric ranked rows>; missing reasons from SELECTION_RULES §9
**Rank-1 gate:** <label (PASS / RANK1_UNSTABLE / GATE_UNRESOLVED_PRECISION / NOT_ASSESSABLE); p; alternative key/p; gap; ε; floor/family checks; scope>
**Rank-2 floor:** <PASS/BELOW_FLOOR/NOT_ASSESSABLE>
**Joint failure:** <exact unconditional value, bounds or NOT_COMPUTED; losing sets; P(both decisive) if relevant; MECHANICALLY_PROTECTED when applicable>
**Shadow gate / Rank 2:** <RET03 alternative/result; RET04 and XCARD6 contract/p/baseline/joint or NONE; NOT_PRIMARY>
**Shadow RANK_DELTA / BASE_ONLY:** <top two by p_card − BASELINE_P with Δ, or NONE; base-only ranks/gate when priced from a mixture, or N/A; NOT_PRIMARY>
**Adjustment dependence:** <NONE/ADJUSTMENT_DEPENDENT; LARGE_ADJUSTMENT separately; unadjusted pair when changed>
**Potential winner:** <result probabilities including allowed draw/tie, or NOT_ESTIMATED>
**Supplied rows not selected:** <each exact line/p or missing reason and disposition>

### Appendix
#### A1. Identity, timing and state
#### A2. Frozen supplied contracts and candidate recipe
#### A3. Evidence and archive inputs

Complete [ROSTER_AVAILABILITY_PROTOCOL](ROSTER_AVAILABILITY_PROTOCOL.md) for both sides in this existing evidence appendix: starters/starting role, selected bench/replacements, reported injuries/illness/suspensions/absences and final late changes, with exact-game sources/times and actual failed/escalated searches. Preserve each field's confirmed/projected/missing/conflicting state; N/A needs a sport/format reason. Existing lineup metadata summarises this evidence, not just the starting side.
#### A4. Distribution, baseline, expected-score arithmetic and sensitivity

For new primary cards include PRIMARY_PREDICTION_PROTOCOL receipt: exact runtime/bundle path, source/known-at review, event/endpoint/model/code/input/grid hashes, mixture weights with their cumulative losses, admitted η/default and its evidence snapshot, hashed WARM_START/FEEDBACK_LOSSES ledgers with unique event IDs, warm-start and feedback counts, information horizon and its source, policy/context/recipe, model source/status and actual generation/declared issue. Copy original numeric rows from PREDICTIONS.csv and expected moments from the mixed grid; retain all FORMS.csv true sample sizes and model feature/availability limits. No run means ML_NOT_RUN/NO_FORECAST, not an invented manual numeric replacement.
#### A5. Full priced universe or labelled subset; W/P/L/V by row
#### A6. Adjustments, regimes and unadjusted comparison
#### A7. Family checks and shadow records
#### A8. Sources, failures, capture/refresh plan
#### A9. Integrity receipt and readback
SPORTS_ONLY_MARKET_BLIND: <result> · OUTCOME_EXPOSURE: <actual state> · SETTLEMENT: NOT_PERFORMED · CANONICAL_IMPORT: PENDING
<!-- END CARD P-NNN -->
```

NO_FORECAST retains identity, reason, evidence, timing and follow-up, with an empty candidate table explicitly labelled NO_RANKED_ROWS. Qualitative cards may rank supported directions but do not create numeric probabilities or numerical PASS. Copy every original supplied contract even if unsupported; no four-row padding.

### 3a. Expected score

| Sport | Terms |
|---|---|
| Baseball | Team runs, total, signed margin and SDs over exact innings/extras endpoint |
| Basketball, rugby, American football | Team points, total, signed margin and SDs |
| Hockey | Regulation and/or full-game goals with OT/SO accounting, total, signed margin and SDs |
| Soccer | Regulation goals per team/total/margin; supported half goals; separate provider-backed corner counts |
| Tennis | Games per player/total/margin, expected sets and deciding-set probability for exact format |
| Cricket | Format/innings-specific runs and wickets where supported; chase stops at winning delivery with legal overshoot; common cross-team margin often N/A |
| AFL/AFLW | Goals, behinds, points=6×goals+behinds, total/margin/SDs for the correct competition |

For team scores X,Y: E(T)=E(X)+E(Y), E(M)=E(X)−E(Y); Var(T)=Var(X)+Var(Y)+2Cov(X,Y); Var(M)=Var(X)+Var(Y)−2Cov(X,Y). If using total/margin parameters, Var(X)=(Var(T)+Var(M)+2Cov(T,M))/4 and Var(Y)=(Var(T)+Var(M)−2Cov(T,M))/4. Missing covariance is not automatically zero. Preserve unsupported SD as NOT_COMPUTED. A mixture card prints the expected score of the mixture: the weighted mean of the case means, and a variance equal to the weighted case variances plus the weighted squared deviations of the case means from the mixture mean.

### 3b. Form windows (A3; PR-01, recipe R2)

One table per side. Use dated games before the cutoff only, and compute it as ARCHIVE_USE_GUIDE recipe R2 says.

| Window | n | Dates (first–last) | Scored per game | Conceded per game | Margin per game | Opponents' mean rating or rank (if available) | Games from previous season | Flags |
|---|---:|---|---:|---:|---:|---|---:|---|
| L5 | | | | | | | | |
| L10 | | | | | | | | |
| L15 | | | | | | | | |
| L20 | | | | | | | | |
| Season to date | | | | | | | | |
| League level (profile row / version) | — | — | | | — | — | — | |

Below each table print:
- the blended rate (recipe R2) with its arithmetic;
- the shrinkage constant k and its source;
- the roster-continuity note for any games from the previous season;
- the sentence "windows overlap; counted once".

A window shorter than its label prints its true n. A missing window prints `ARCHIVE_UNAVAILABLE:<reason>` or the SOURCES route used. Excluded flagged rows (for example the archive's duplicate or awarded-result flags) are listed.

## 4. Addenda

Use `<!-- BEGIN ADDENDUM P-NNN <timestamp-key> -->` and matching END; heading `### Addendum · P-NNN · <ISO timestamp>`. Record parent ID, original version, what changed, source/time, reason and current implications. No new P-ID, no edits to original ranks. A pregame reforecast table uses p_reforecast and is NOT_PRIMARY; it cannot replace original settlement. Post-event material is explicitly diagnostic. A mini's footer changes only for actual new cards or queue updates, never to pretend addenda allocate IDs.

## 5. Capture and contract evidence

Map each row to quantity, unit, provider, exact field, period, action/void rule and current availability. Include source update and read time, fallback and UNKNOWN lineage. Distinguish field-owner result from operator definition. Evidence bounds name their feasible range and whether it crosses a threshold. Merely listing a URL or future capture time is not a receipt.

## 6. Settlement package

Folder `Mini Settlement - <FIRST> to <LAST> - <date>/`: ORIGINAL_MINI (exact copy), PREDICTION_MINI_SETTLED file, LOCAL_ID_MAPPING.md, UNRESOLVED_CARRYOVER.md, SETTLEMENT_MANIFEST.md. Settled file = frozen bytes followed by the section below; on later runs preserve the earlier settled file and append a versioned revision in a new output, never overwrite it.

```markdown
# SETTLEMENT AND RETROSPECTIVES
<!-- SETTLEMENT-FORMAT: mini-settlement-6 -->
Authority/read time: <actual receipt, including authority mode>
Frozen original: <path; byte/line counts if measured; exact-prefix comparison result>
FROZEN_SOURCE receipt: <source path; raw byte count; SHA-256 of raw bytes; block inventory (card IDs, addenda keys); freeze time; writer hand-over to <next mini or NONE>>
Source growth check: <at package time the source still has the frozen byte count, or GROWTH_DETECTED: blocks after the snapshot and where they were routed>
Inventory: <cards/carryovers/addenda; pending and unresolved separately>

<!-- BEGIN SETTLEMENT P-NNN revision-1 -->
### Settlement · P-NNN · <event> · <actual review time>
**Revision:** revision-1 · parent NONE (or revision-<n−1>) · effective <ISO time> · affected contract keys <ALL or list> · changes <old → new, with reason; NONE for the first>
**Card state:** SETTLED | PARTIALLY_SETTLED | PENDING_EVENT | UNRESOLVED_EVIDENCE | NO_FORECAST
**Original card / prior revision:** <source pointers>
**Final event / verified final time:** <facts, endpoint, sources; unknown explicit>
**Definition status:** <sporting convention; operator verified/unknown separately>
**Expected vs final:** <frozen expected, observed, error and z or precise missing reason>

| Rank | Exact original proposition | Original p_card | Original BASELINE_P | Grade | Evidence | Counts toward wins | Basis / definition / time |
|---|---|---|---|---|---|---|---|
<one row per issued candidate, including UNRESOLVED; no invented missing ranks>

**Top-two result:** <class; W/L/PUSH/VOID/UNRESOLVED; decisive denominator>
**Proper scores:** <paired Brier/log loss rows or NOT_COMPUTABLE reasons; evidence class of each row (headline A/B, sensitivity C/E)>
**Shadow results:** <separate frozen RET03/RET04/XCARD6/RANK_DELTA/BASE_ONLY diagnostics or NOT_ISSUED>
**Form-window check:** <observed score against the unadjusted and the form-adjusted expected score; error of each; NOT_APPLICABLE when no form adjustment was made>
**Winner call:** <original call result on its exact endpoint or unresolved>
**R1. Original prediction:** <this card's literal top two and probabilities>
**R2. Final event:** <verified endpoint and outstanding fields>
**R3. Contract settlement:** <row arithmetic and frozen rules>
**R4. Rank diagnostics:** <primary counts, coverage, optional NDCG>
**R5. Winner call:** <original call, no hindsight replacement>
**R6. Line assessment:** <signed distance from each threshold; units>
**R7. Expected versus realised mechanism:** <original mean/SD and observed outcome>
**R8. Missed mechanism:** <supported observation or NOT_ASSESSABLE>
**R9. Source/timing review:** <cutoff knowledge, refreshes, source gaps and process evidence>
**R10. Classification:** <process SOUND/DEFICIENT/NOT_ASSESSABLE; model uncalibrated separately; failure class>
**R11. Hypothesis:** <testable proposal, PROPOSED_NOT_TESTED>
**R12. Disposition:** <NO_CHANGE/MONITOR/PROPOSE_EXPERIMENT/process candidate; next action for gaps>
<Rank-1 LOSS: eight-part deep review required by CURRENT_RULES §3>
<!-- END SETTLEMENT P-NNN revision-1 -->
```

Pending cards get state evidence, literal original reference and next check, with result-dependent R sections N/A. Terminal unresolved rows retain the supported settlement work and open questions. Manifest inventories each source block, local/canonical status, latest revision, grades/counts, outputs, prefix check and import PENDING. No guessed hash or byte-comparison PASS.

**Later revisions (R17).** A rerun or correction appends `<!-- BEGIN SETTLEMENT P-NNN revision-<n> -->` with the next unused n for that ID, its parent and the affected contract keys. It never re-uses a key or edits an earlier block. UNRESOLVED_CARRYOVER.md uses the queue columns of §2-C, so that every open item has an actor, a route, a due time and a scheduling status.

## 7. Card self-audit

| Check | Required evidence |
|---|---|
| C1 | Actual authority, format, full required reading and working scope |
| C2 | Exact event/endpoint, duplicate search across minis/status/log bodies, continuous working ID |
| C3 | Candidate recipe frozen; keys unique; primary numeric p descending; supplied dispositions; ≤4 supported rows |
| C4 | Recompute row W/P/L/V, p and result masses including draw/tie; rounding tolerance declared (normally ≤0.001); monotonicity/complements |
| C5 | Gate alternative from declared universe, p/gap/floor arithmetic; RET03 explicitly shadow |
| C6 | Primary Rank-2 floor; exact/bounded joint with correct unconditional masses; mechanical protection disclosed |
| C7 | Adjustment table and any-size top-two flips; unadjusted pair/sensitivity; >0.25 SD separately |
| C8 | Regime vocabulary, matching source/version and no double adjustment |
| C9 | Sport/family/endpoint/provider checks; no invented exact engine |
| C10 | Contract definitions, field capture and actual scheduling status |
| C11 | Timing protocol: evidence horizon = game-log scheduled start (no separate cutoff), independent retrieval/completion/issue/state; no fixed deadline; pre-start input proof and actual issue phase separate; honest outcome exposure |
| C12 | Market blindness, supported evidence with times, lineage unknowns |
| C13 | Actual archive window/sample/coverage and point-in-time availability |
| C14 | Frozen same-row baseline and independent league-only parameters, or explicit unavailable reason |
| C15 | Expected-score arithmetic/units/covariance and missingness; decision block/appendix complete |
| C16 | Written card and footer read back; earlier blocks unchanged; audit has actual evidence, not just check names |
| C17 | Form windows: L5/L10/L15/L20/season/league printed per side with true n, from dated pre-cutoff games; flagged archive rows excluded; blend/k/arithmetic retained as comparison diagnostics where supported; windows not counted as separate confirmations; fitted primary centre is not manually overwritten; explicit manual comparisons retain their adjustment/unadjusted pair (or ARCHIVE_UNAVAILABLE with the route tried) |
| C18 | Line distance (units and z, or N/A) on every ranked row; baseline coverage line present; each missing BASELINE_P uses an enumerated reason |
| C19 | Primary runtime: actual source/fit/bundle checked; mixture weights recompute from recorded losses and η; all rows match the mixed grid, model features/limits explicit. Pricing basis: primary W/P/L and p_card derive from the actual retained mixed ML grid; manual mixtures/adjustments cannot overwrite it. Material unsupported effects mean NO_FORECAST. An explicitly requested manual comparison retains frozen mixture weights/p_base and base-only diagnostics; ε and any GATE_UNRESOLVED_PRECISION / PRECISION_TIE stated |
| C20 | Availability: comprehensive both-side starter/bench/absence search per ROSTER_AVAILABILITY_PROTOCOL completed with actual attempts and final recheck in A3/A8; projections, access/publication gaps and material uncertainty honest. Lifecycle: issuing writer and lease valid at append time; mini not frozen; request logged in the intake table; known-at line present; lineup state and issue-step times recorded |

## 8. Canonical entry and rollover

Keep canonical-md-1: `<!-- BEGIN CANONICAL RESEARCH P-NNN -->`, heading `## P-NNN — <sport/league/event/date>`, actual import note, original card core unchanged from Working ID through integrity receipt, then matching END. Preserve complete original mini in import inputs. The wrapper heading may differ; original core must not. Import note is metadata, never a new forecast timestamp.

Dated additions use `<!-- BEGIN RESEARCH ADDENDUM P-NNN <date>-<sequence> -->` and matching END, enclosing the entire original addendum/settlement block. Maintain a source-to-destination map, with explicit revisions; skip identical existing blocks. A canonical reference repeated in carryover is not a new card.

Rollover appends a closure to the old part and creates one dated opening snapshot for the next, continuity links, unchanged next ID and queue pointers. No copied forecasts, no new event and no back-edit of opening snapshots. Current values live in CURRENT_STATE and the current status section, reconciled to canonical entries.

**Cross-part revisions (R21).** A later settlement revision or addendum for a card whose original sits in a closed part is appended to the **active** part. Its wrapper is `<!-- BEGIN RESEARCH ADDENDUM P-NNN <date>-<sequence> -->`, and it opens with a pointer line `Original: <closed part path>, canonical block P-NNN; prior revision: <part and revision key>`. The closed part is never edited. The effective revision chain is resolved across parts by revision key (CURRENT_RULES §8). Neither a rollover nor a later settlement creates a new ID or duplicates the original card.

**Marker integrity (R19).** Before import, every block must satisfy:
- `BEGIN`/`END` markers balanced, one END per BEGIN, with no nesting across different IDs;
- the END names the same ID, and revision key where present, as its BEGIN;
- no duplicate revision key for an ID.

Legacy settlement markers without revision keys (mini-settlement-2 to -5) are accepted under their declared format. The import wrapper records the legacy format; legacy bytes are never rewritten to add keys.

## 9. Settlement self-audit

| Check | Required evidence |
|---|---|
| S1 | Every source block inventoried once; IDs and canonical/local status preserved |
| S2 | Exact frozen prefix/byte comparison, line endings and original footer unchanged |
| S3 | Every proposition/rank/p/baseline/expected value copied literally or missing as originally issued |
| S4 | Exact field/endpoint/contract arithmetic; missing/conflicting data not VOID |
| S5 | Evidence source/field/times; bound only graded if invariant; operator status separate |
| S6 | Counts, coverage, conditional probabilities and cohort definitions agree |
| S7 | R1 is this card; terminal R1–R12 complete with honest N/A |
| S8 | Every Rank-1 LOSS has eight-part review; wins checked equally; no invented causal shares |
| S9 | Original versus shadow/reforecast results and baseline coverage separate |
| S10 | Pending-event and terminal-evidence queues complete; SLA uses actual final or marked unknown |
| S11 | Expected errors/z and proper scores recompute; no historical baseline reconstruction |
| S12 | Output files read back, allowed writes only, mapping/manifest and rerun revisions reconcile |
| S13 | Revision keys unique per ID; every revision names its parent and affected keys; the effective grade per contract key follows the single parent chain; conflicting branches marked REVISION_CONFLICT and counted UNRESOLVED |
| S14 | FROZEN_SOURCE receipt (path, raw bytes, SHA-256, block inventory) written before settlement; source growth checked at package time and any later block routed, not silently covered |
| S15 | Every open queue item has actor, next source and field, due time with timezone, final-time basis, last attempt and scheduled-automation status; evidence strata shown in the proper-score lines |

## 10. Acceptance examples

Active and settled structural examples (mini-log-7 / mini-settlement-6): [active](research/prompts/examples/EXAMPLE_ACTIVE_MINI.md), [settled](research/prompts/examples/EXAMPLE_SETTLED_MINI.md); the v10 pair is in [legacy_mini_log_6/](research/prompts/examples/legacy_mini_log_6/EXAMPLE_ACTIVE_MINI.md). Worked checks and negative fixtures: [v11 fixtures F01–F32](research/verification/framework_change_2026-10-12-1/FIXTURES.md), [v10 verification](research/verification/framework_change_2026-10-11-1/VERIFICATION_REPORT.md). They are synthetic documentation tests, not sports forecasts or prospective evidence.

## 11. Timing semantics for new v12 work

Use [TIMING_RESEARCH_PROTOCOL](TIMING_RESEARCH_PROTOCOL.md) in the existing Timing/Known-at/Lineup-state/A1/A3/A8/A9 fields. No added mandatory schema field or mini-format migration. Retain actual late issue time even with CLEAN_PRE_START_INPUTS; report that cohort separately. All old mini formats and issued timing/rank/p/baseline/grade bytes remain unchanged. S9/S10 additionally keep clean-input late-issued research apart from pre-start-issued prospective/shadow scores; a settlement cannot create missing pre-start proof.

## 12. Primary ML/RL receipt and feedback

[PRIMARY_PREDICTION_PROTOCOL](PRIMARY_PREDICTION_PROTOCOL.md) controls new model-assisted cards in existing A4/A5/A9 metadata. Existing mini-log-7 and older formats retain their format; the declared policy/version changes, never an issued core. Settlement retains the original bundle, grades original keys first, then creates a new source-backed feedback row and reconciles the effective revision inventory before future learning. The market/decision lab remains excluded.
