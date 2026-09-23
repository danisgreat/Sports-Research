# Audit implementation ledger — 21 September 2026

**Prospective authority after this implementation:** **MDS-2026.09.19-v4.3 / CR-2026.09.21-1**  
**Scope:** source-integrity and cricket toss/pitch retrieval controls.  
**Predictive status:** **NO PREDICTIVE-LIFT CLAIM.** This pass changes retrieval, provenance, missingness, lineage and enforcement. It does not fit a model, change a validated coefficient, claim improved calibration, or retrofit prior cards.

Source audit: [`AUDIT_AND_CRICKET_SOURCE_UPDATE_2026-09-21.md`](AUDIT_AND_CRICKET_SOURCE_UPDATE_2026-09-21.md).

---

## 1. What was reconciled

The current root authority was compared against the prior audits and the 2026-09-21 cricket source audit. Findings were placed into three buckets before any edit:

1. **Retain:** already-correct controls remain active without being duplicated.
2. **Implement/repair:** correct findings that were absent, inconsistent or only partially implemented were made prospective controls.
3. **Reject/supersede:** earlier ideas contradicted by newer evidence or later controls remain inactive.

No historical issued prediction, rank, probability, result or settlement was rewritten by this pass.

---

## 2. Retained findings — still correct

The following controls remain active and were not weakened:

- supplied totals/spreads/alternate lines are contract metadata only until the independent sporting distribution is frozen;
- betting lines, odds movement, betting previews/picks/tips and fantasy/DFS material are prohibited predictive inputs;
- every material fact must satisfy point-in-time `known_at <= cutoff_at` and carry source provenance/lineage;
- multiple front ends on one upstream feed are one evidentiary lineage;
- search-result snippets and generated summaries are discovery only;
- every new event requires the CR-4 minimum of three distinct reliable upstream lineages, with timezone-aware event identity/state verification;
- terminal settlement still requires three independent reliable lineages explicitly agreeing on exact event/date, terminal state and final result;
- exact-match strip evidence is separate from weather and historical venue tendency;
- weather cannot create unreported grass, hardness, seam, pace, turn or deterioration claims;
- the toss decision is weak circumstantial context only and cannot itself establish a strip report or a signed total/winner lean;
- the immediately preceding match at the same venue is a different-strip comparator unless same-strip reuse is explicitly confirmed;
- debutants remain subject to `NO_PRIOR_FORMAT_RECORD`/sample-width controls;
- recent outcomes do not create rebound, hangover or “due” effects without a named mechanism;
- cricket totals/phases must arise from one coherent resource/phase process rather than additive double-counting shortcuts.

---

## 3. Implemented repairs — cricket toss and pitch source control

### 3.1 One ambiguous conditions ladder was replaced prospectively by two distinct ladders

The previous documentation mixed toss retrieval, exact-strip observation and historical context, and later amendments created a six-rung/eight-rung drift. New cricket cards now use:

- **TOSS FACT ladder T1–T6** for the factual toss winner, decision and XI state; and
- **STRIP/PITCH EVIDENCE ladder P1–P8** for today's strip versus historical/context evidence.

This also removes the duplicated “toss broadcast” concept. A broadcast can be T2 for the toss and P1 for a named exact-match pitch report, but those are different fields, not two independent corroborating lineages.

### 3.2 Toss status is explicit

Allowed statuses are:

- `VERIFIED`
- `NOT_VERIFIED_AFTER_SEARCH`
- `NOT_YET_PUBLISHED`
- `CONFLICTING`

The toss winner must not be inferred solely from which side appears to bat first.

### 3.3 Strip status is explicit

Allowed statuses are:

- `OBSERVED`
- `NOT_FOUND_AFTER_SEARCH`
- `CONFLICTING`
- `STALE_ONLY`

Only current-match P1–P5 evidence can establish today's strip. Rungs P6–P8 are context only unless a source explicitly establishes same-strip reuse.

### 3.4 New source lanes were added

The source register now explicitly supports, subject to field-specific limits:

- official board/competition verified video or a rights-holder toss/pitch broadcast;
- sanctioned NV Play / board-branded Match Centre routes when the competition officially uses them;
- specialist live commentary as a transcript/access route to a named broadcast pitch report;
- automated pitch metadata as a distinct weak evidence class, never silently relabelled as a human observed strip report.

### 3.5 Source-lineage fingerprinting is now a hard cricket control

Identical or near-identical unusual structured pitch labels across multiple websites are treated as a **suspected shared upstream feed** until independence is demonstrated.

Such records are classified as `AUTOMATED_PITCH_METADATA` when no named observer/source is established. They do not:

- set `STRIP_STATUS=OBSERVED`;
- create an additional independent pitch lineage merely because another front end shows the same fields; or
- satisfy the three-source event gate twice.

### 3.6 Venue-history missingness is now valid

The old implication that the venue-history rung is “always computable” is withdrawn prospectively. A new or sparse venue/format may honestly return:

`INSUFFICIENT_VENUE_HISTORY`

A broader comparable may be used only with its true population stated. Missing same-venue history widens uncertainty; it is never invented.

### 3.7 Official-page staleness is field-specific

An official hostname does not override contradictory fresh state evidence simply because it is official. When a dynamic official event page is demonstrably stale for a field:

- mark that field `STALE`;
- preserve unaffected official identity/venue fields;
- retrieve another official/static/sanctioned scoring route where available; and
- reconcile against independent high-quality evidence.

### 3.8 Toss-window and final pre-issue refresh are mandatory

For cricket, the workflow now explicitly refreshes during the actual toss window and again immediately before issue:

- event state;
- toss and decision;
- confirmed XIs / late changes;
- exact-match strip evidence;
- local weather/radar/conditions;
- source conflicts, stale fields and duplicate lineages.

If scheduled start has passed, state must be reclassified before any pregame issuance.

---

## 4. Rejected/superseded ideas — not reintroduced

This pass explicitly keeps the following inactive:

- treating “one of the complementary Over/Under sides won” as meaningful forecasting performance when both sides were selected;
- treating second-highest/second-lowest scores as distribution “modes”;
- assuming same-venue history always exists;
- counting multiple websites using the same upstream feed as independent confirmation;
- treating a generic automated pitch-condition block as a named observed strip report;
- treating the toss decision as proof of a batting/bowling pitch;
- using generic fantasy/tipping/prediction pages as decision-driving pitch evidence;
- using market lines, betting picks or fantasy projections as sporting evidence;
- promoting a permanent predictive weight from one unusual match without a mechanism and prospective validation.

---

## 5. Files changed in this implementation

- `README.md`
- `METHOD.md`
- `CONTROLS.md`
- `RULES_CRICKET.md`
- `DATA_SOURCE_REGISTER.md`
- `SOURCES.md`
- `UPCOMING_GAME_RESEARCH_GUIDE.md`
- `LEARNING_REGISTER.md`
- `FORECAST_PREFLIGHT_MANIFEST.md`
- `prediction_preflight.py`
- `test_prediction_preflight.py`

New audit/control records:

- `AUDIT_AND_CRICKET_SOURCE_UPDATE_2026-09-21.md`
- `AUDIT_IMPLEMENTATION_2026-09-21.md`
- `CONTROL_MANIFEST_2026-09-21.md`

The method identifier remains **MDS-2026.09.19-v4.3** because this pass does not alter the forecasting objective or promoted modelling architecture. The control revision advances to **CR-2026.09.21-1** because enforceable source/missingness/preflight requirements changed.

---

## 6. Executable enforcement

`prediction_preflight.py` now requires a top-level `sport`. For `sport == "cricket"`, it additionally requires a `cricket_conditions` object and fails closed when the new source controls are violated.

It validates, among other things:

- legal toss and strip statuses;
- complete toss/strip search flags;
- `COMPUTED` versus `INSUFFICIENT_VENUE_HISTORY` handling;
- pre-toss/post-toss state;
- no automated pitch metadata used as an observed strip;
- no duplicate pitch lineage counted independently;
- no toss decision used as the strip report; and
- a final conditions refresh that occurs no later than distribution freeze.

### Regression result

Executed after the final text/code reconciliation on 2026-09-21:

- Python compilation: **PASS**
- `python -m unittest -v test_prediction_preflight.py`: **20/20 tests PASS**

The new tests include:

- missing sport blocked;
- cricket conditions object required;
- valid cricket conditions pass;
- automated pitch metadata masquerading as an observation blocked; and
- duplicate pitch lineage blocked.

This proves only that the coded controls behave as specified. It does **not** prove a better hit rate, Brier score, log loss, RMSE or calibration.

---

## 7. Prospective card requirement

Every new cricket card under **MDS-2026.09.19-v4.3 / CR-2026.09.21-1** must expose at minimum:

- `TOSS STATUS` and its source/lineage;
- `STRIP STATUS` and the exact-match source/speaker when found;
- `MATCH CONDITIONS STATUS` and weather/interruption evidence;
- the attempted TOSS and STRIP ladders;
- venue-history availability or `INSUFFICIENT_VENUE_HISTORY`;
- source-lineage de-duplication and suspected shared feeds;
- whether automated pitch metadata existed and how it was classified; and
- the final toss/XI/strip/weather refresh receipt.

`NOT_FOUND_AFTER_SEARCH` is an acceptable honest result only after the required search is actually performed. Missing strip evidence widens uncertainty and caps evidence quality; it never licenses invention.

---

## 8. Validation still required before any performance claim

This control patch does not close the broader empirical work already identified by prior audits. The project still needs, in the applicable validated scope:

- quality-approved H0 construction with point-in-time source snapshots;
- chronological training/tuning/calibration and untouched test evaluation;
- prospective shadow evidence;
- proper distributional scores and calibration checks; and
- promotion only where the frozen challenger actually beats the appropriate baseline.

Until those gates pass, the honest status remains **LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE** with `UNVALIDATED_SUBJECTIVE` probabilities where the current method permits them.
