# Card, mini, settlement and canonical formats

**mini-log-6 · mini-settlement-5 · canonical-md-1.** Authority: MDS-2026.10.11-v10.0 / CR-2026.10.11-R1 / SCV-2026.10.11-v6. [Rules](CURRENT_RULES.md) and [selection definitions](SELECTION_RULES.md) control semantics.

<a id="local-mini-format-mini-log-2"></a>

## 1. Compatibility

Old minis finish in their original format. Never insert baselines, gates, expected scores or missing cutoffs into an old card. New dated addenda may carry unresolved status or diagnostic fields without changing its original selection/scoring version. Old numeric self-audits are interpreted against the original format, with gaps documented rather than repaired by fabrication. For v10 new minis, use the structures below. Example IDs beginning EXAMPLE are not P-IDs and must never be imported.

## 2. Mini

Create `Mini Prediction Log - <FIRST> onward - <date>/PREDICTION_MINI_RUNNING_LOG_<FIRST>_ONWARD.md`:

```markdown
<!-- MINI-LOG-FORMAT: mini-log-6 -->
# Prediction Mini Running Log — <FIRST> onward

## A. Authority snapshot
| Field | Value |
|---|---|
| Repository / branch / read HEAD | <actual local or published authority> |
| Relevant working differences | <paths or NONE> |
| Method / control / scoring / selection | <versions> |
| Active Combined Log | <resolved path> |
| Highest committed / next canonical ID | <current values> |
| Outstanding local minis and IDs | <contiguous inventory or NONE> |
| First working ID | <reconciled next local ID> |
| Reading receipt / opened at | <paths and ISO time with offset> |
| Mode | LOCAL_MINI_STAGING |

SPORTS_ONLY / MARKET_BLIND · RESEARCH_ONLY_NOT_CERTIFIED · CANONICAL_IMPORT_STATUS: PENDING

## B. Local ID rules
Creating this mini consumes no ID. One retained event receives one permanent working ID; canonical status requires import. Addenda/carryovers consume none. No silent skipping, reuse or renumbering. Only a complete written/read-back card advances the footer.

## C. Carryover and evidence queue
<one reference per unresolved event/field with ID, event key, original card path, exact frozen pick table, endpoint/definition pointer, latest revision, reason, next action and due time; or NONE>

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
- **Analysis status:** UNCALIBRATED_ANALYST_SCENARIO | UNCALIBRATED_QUALITATIVE | NO_FORECAST
- **Timing:** <state; cutoff; research completion; actual issue time; source state/recheck time; source publication time; actual start or NOT_VERIFIED>
- **Scheduled start:** <venue timezone, UTC and Australia/Sydney with offsets; source>
- **Scheduled lead / band:** <minutes at issue; BUFFERED or LATE_START or UNKNOWN>
- **Endpoint / definition:** <regulation/extras; tie/push/void/retirement/listed pitcher/abandonment convention; operator status>
- **Distribution object:** <id/family/parameters/approximation or NOT_COMPUTED>
- **Expected score:** <sport units; team means/SDs, total and signed margin, endpoint; N/A/NOT_COMPUTED as appropriate>
- **Baseline:** <BASELINE_LEAGUE_V1 recipe, cohort dates/n, parameters, cutoff/provenance or BASELINE_UNAVAILABLE reason>
- **Regime flags / context:** <approved flags; other context separately>
- **Settlement fields / capture plan:** <row-to-provider/field mapping; due time; responsible action; scheduled job YES/NO>
- **Rules read / archive check:** <paths/sections; actual files/rows/date window/filters/findings/gaps>
- **Evidence receipt:** <decisive claim/source/field/extract/source time/retrieval time/lineage; detail in A3>

### Decision block
<One-sentence assessment and principal uncertainty; mean score is not exact-score mode.>

| Rank | Role | Tag | Contract key / exact proposition | p_card | BASELINE_P | Probability basis | Main failure route |
|---|---|---|---|---|---|---|---|
| 1 | PICK | SUPPLIED or ANALYST_DERIVED | <line/period/endpoint/action> | <p or NOT_ESTIMATED> | <p or missing reason> | <distribution id or QUALITATIVE> | <mechanism> |
<up to four actual supported rows; roles PICK for ranks 1–2, INFORMATIONAL thereafter>

**Rank-1 gate:** <label; p; alternative key/p; gap; floor/family checks; scope>
**Rank-2 floor:** <PASS/BELOW_FLOOR/NOT_ASSESSABLE>
**Joint failure:** <exact unconditional value, bounds or NOT_COMPUTED; losing sets; P(both decisive) if relevant; MECHANICALLY_PROTECTED when applicable>
**Shadow gate / Rank 2:** <RET03 alternative/result; RET04 and XCARD6 contract/p/baseline/joint or NONE; NOT_PRIMARY>
**Adjustment dependence:** <NONE/ADJUSTMENT_DEPENDENT; LARGE_ADJUSTMENT separately; unadjusted pair when changed>
**Potential winner:** <result probabilities including allowed draw/tie, or NOT_ESTIMATED>
**Supplied rows not selected:** <each exact line/p or missing reason and disposition>

### Appendix
#### A1. Identity, timing and state
#### A2. Frozen supplied contracts and candidate recipe
#### A3. Evidence and archive inputs
#### A4. Distribution, baseline, expected-score arithmetic and sensitivity
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

For team scores X,Y: E(T)=E(X)+E(Y), E(M)=E(X)−E(Y); Var(T)=Var(X)+Var(Y)+2Cov(X,Y); Var(M)=Var(X)+Var(Y)−2Cov(X,Y). If using total/margin parameters, Var(X)=(Var(T)+Var(M)+2Cov(T,M))/4 and Var(Y)=(Var(T)+Var(M)−2Cov(T,M))/4. Missing covariance is not automatically zero. Preserve unsupported SD as NOT_COMPUTED.

## 4. Addenda

Use `<!-- BEGIN ADDENDUM P-NNN <timestamp-key> -->` and matching END; heading `### Addendum · P-NNN · <ISO timestamp>`. Record parent ID, original version, what changed, source/time, reason and current implications. No new P-ID, no edits to original ranks. A pregame reforecast table uses p_reforecast and is NOT_PRIMARY; it cannot replace original settlement. Post-event material is explicitly diagnostic. A mini's footer changes only for actual new cards or queue updates, never to pretend addenda allocate IDs.

## 5. Capture and contract evidence

Map each row to quantity, unit, provider, exact field, period, action/void rule and current availability. Include source update and read time, fallback and UNKNOWN lineage. Distinguish field-owner result from operator definition. Evidence bounds name their feasible range and whether it crosses a threshold. Merely listing a URL or future capture time is not a receipt.

## 6. Settlement package

Folder `Mini Settlement - <FIRST> to <LAST> - <date>/`: ORIGINAL_MINI (exact copy), PREDICTION_MINI_SETTLED file, LOCAL_ID_MAPPING.md, UNRESOLVED_CARRYOVER.md, SETTLEMENT_MANIFEST.md. Settled file = frozen bytes followed by the section below; on later runs preserve the earlier settled file and append a versioned revision in a new output, never overwrite it.

```markdown
# SETTLEMENT AND RETROSPECTIVES
<!-- SETTLEMENT-FORMAT: mini-settlement-5 -->
Authority/read time: <actual receipt>
Frozen original: <path; byte/line counts if measured; exact-prefix comparison result>
Inventory: <cards/carryovers/addenda; pending and unresolved separately>

<!-- BEGIN SETTLEMENT P-NNN revision-1 -->
### Settlement · P-NNN · <event> · <actual review time>
**Card state:** SETTLED | PARTIALLY_SETTLED | PENDING_EVENT | UNRESOLVED_EVIDENCE | NO_FORECAST
**Original card / prior revision:** <source pointers>
**Final event / verified final time:** <facts, endpoint, sources; unknown explicit>
**Definition status:** <sporting convention; operator verified/unknown separately>
**Expected vs final:** <frozen expected, observed, error and z or precise missing reason>

| Rank | Exact original proposition | Original p_card | Original BASELINE_P | Grade | Evidence | Counts toward wins | Basis / definition / time |
|---|---|---|---|---|---|---|---|
<one row per issued candidate, including UNRESOLVED; no invented missing ranks>

**Top-two result:** <class; W/L/PUSH/VOID/UNRESOLVED; decisive denominator>
**Proper scores:** <paired Brier/log loss rows or NOT_COMPUTABLE reasons>
**Shadow results:** <separate frozen RET03/RET04/XCARD6 diagnostics or NOT_ISSUED>
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
| C11 | Cutoff/research/issue/recheck ordering; honest event/lead states and outcome exposure |
| C12 | Market blindness, supported evidence with times, lineage unknowns |
| C13 | Actual archive window/sample/coverage and point-in-time availability |
| C14 | Frozen same-row baseline and independent league-only parameters, or explicit unavailable reason |
| C15 | Expected-score arithmetic/units/covariance and missingness; decision block/appendix complete |
| C16 | Written card and footer read back; earlier blocks unchanged; audit has actual evidence, not just check names |

## 8. Canonical entry and rollover

Keep canonical-md-1: `<!-- BEGIN CANONICAL RESEARCH P-NNN -->`, heading `## P-NNN — <sport/league/event/date>`, actual import note, original card core unchanged from Working ID through integrity receipt, then matching END. Preserve complete original mini in import inputs. The wrapper heading may differ; original core must not. Import note is metadata, never a new forecast timestamp.

Dated additions use `<!-- BEGIN RESEARCH ADDENDUM P-NNN <date>-<sequence> -->` and matching END, enclosing the entire original addendum/settlement block. Maintain a source-to-destination map, with explicit revisions; skip identical existing blocks. A canonical reference repeated in carryover is not a new card.

Rollover appends a closure to the old part and creates one dated opening snapshot for the next, continuity links, unchanged next ID and queue pointers. No copied forecasts, no new event and no back-edit of opening snapshots. Current values live in CURRENT_STATE and the current status section, reconciled to canonical entries.

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

## 10. Acceptance examples

Active and settled structural examples: [active](research/prompts/examples/EXAMPLE_ACTIVE_MINI.md), [settled](research/prompts/examples/EXAMPLE_SETTLED_MINI.md). Worked checks and negative fixtures: [verification](research/verification/framework_change_2026-10-11-1/VERIFICATION_REPORT.md). They are synthetic documentation tests, not sports forecasts or prospective evidence.
