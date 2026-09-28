# Sports Research: evidence-based repair plan

**Date:** 28 September 2026, Australia/Sydney. **Companion assessment:** [comprehensive review — 6.0/10](SPORTS_RESEARCH_COMPREHENSIVE_REVIEW.md).

**Status: implementation record updated 28 September 2026.** The reproducible extraction, fail-closed record/scoring gates, document corrections, archived-rule deletion and control receipt have been implemented. The remaining source-backed settlement, canonical import, and prospective-evidence phases are explicitly open because their evidence gates have not passed. No model coefficient or forecast probability was refit, no issued card was rewritten, and no new canonical ID was allocated. Current records remain `LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE`. See [implementation report](IMPLEMENTATION_REPORT.md) for exact changes, checks and open gates.

The work should proceed in dependency order: **preserve evidence → repair records → repair schema/scoring → strengthen checks → reconcile documentation → collect prospective evidence → evaluate model changes**. Avoid rebuilding the production dataset before correcting its admission and identity logic.

## 1. First work session: protect the evidence and stop propagation

**Owner:** repository maintainer, assisted by the research agent. **Addresses:** F1–F4 and F8.

1. Record the current branch, HEAD and both staged/unstaged changes. The reviewed P-518-onward mini log is already dirty; do not overwrite it, restore it wholesale or commit another session's work accidentally.
2. Archive the exact reviewed mini-log bytes and hash them before any correction. Save the original issued sections separately from settlement revisions, retaining their existing timestamps and aliases. A newly made archive proves content preservation, not an earlier issue time.
3. Mark the affected settlement/process blocks as pending reconciliation in an appended audit receipt. Keep outcome verification separate from process verification: a wrong pitching narrative does not automatically make the 7–1 final wrong.
4. Hold the current mini-log learnings out of active rule promotion and model fitting until their supporting facts pass verification. In particular, do not activate the +15% basketball-width change, the new losing-streak coefficient threshold, or an ACB-specific RM-1 exemption from this cohort.
5. Open a reconciliation register for P-518–P-522 with one row per issued event: canonical ID, exact official event ID, competition, date, horizon, source-file hash, import state, outcome state and process state. Preserve the current ID assignments pending reconciliation; do not reuse P-518 because a stale summary calls it available.

**Acceptance:** source bytes are archived; original issued p, q, ranks and source statements match the archive; each disputed claim has an explicit status; no disputed row or learning is silently promoted. Check an issued-section hash before and after the repair.

## 2. Reverify the five settlements and generate corrected tables

**Owner:** settlement reviewer. **Files:** active mini log, Part 5, status register; later any dependent research summaries. **Addresses:** F1, F2, F3, F8.

### Exact event and source checks

| Card | Required verification | Known issue to resolve |
|---|---|---|
| P-518 | MLB gamePk 822678; exact date; official final, pitching and line score; independent terminal corroboration | Correct final but wrong hits/errors, starter statistics, duration and attendance; summary date mismatch |
| P-519 | Issued AFLW match 8942; season, round, teams, official result and injury record | Settlement cites 7412; no-disruption claim conflicts with official injury reporting |
| P-520 | Exact KBO competition/team/date/game identifier and inning/pitcher record | Summary and issued start times differ; settlement sources require exact-event verification; current baseline uses need competition-specific provenance |
| P-521 | ACB 105378; final score, active sheet, quarter and player statistics | Official ACB page and live stats are one upstream lineage unless evidence establishes otherwise |
| P-522 | Issued ACB 105380 versus settlement 105379; coach, roster, final and process record | Different event ID and coach narratives; retrospective contradicts the card's named kill paths |

For each source, retain `source_url`, `retrieved_at_utc`, exact event identity, terminal state, relevant extracted fields, upstream lineage and a source-response hash or permitted snapshot. An outlet name alone is insufficient. If fewer than the required independent lineages can be established, retain an honest verification-limit label under the governing policy; do not duplicate the same feed to meet a count.

### Correct settlement without rewriting forecasts

1. Copy issued p, q, ranks, baseline values and missingness from the frozen record using exact decision IDs. Do not type replacement 0.500 baselines.
2. Recompute the result from the verified event outcome and the exact contract, including period, draw, push, void, retirement and overtime terms.
3. Recompute Brier cells from the appropriate score definition. Preserve research grades separately from any unavailable operator settlement.
4. Append a correction with old value, new value, source, reason and affected downstream artifacts. An unresolved field stays unresolved.
5. Rebuild the retrospective only from verified facts. Use a table distinguishing observation, interpretation and testable hypothesis. For P-522, record the named low-total and low-margin kill paths as having occurred if the recorded final is verified; do not invent a new family-state label absent from the issued joint table.
6. Import reconciled issued records and corrections to Part 5; update its top snapshot, the current status register and the mini-log pointer as one coordinated change. Archive the mini log only after readback confirms complete custody.

**Acceptance:** 20/20 ranked rows preserve issued baseline semantics; every result has a deterministic contract calculation; verified process fields agree with their source; source count is by upstream lineage; the three canonical queue surfaces agree; the issued-card hash is unchanged.

## 3. Give Markdown a dependable machine-readable record

**Owner:** data/tool maintainer. **Addresses:** F4, F5 and F9.

Markdown can remain the human-readable authority. Add a structured JSON block or rigorously specified table to each new card, then generate CSV views from it. A database migration is not required to solve the present problem.

Use distinct identities for the sporting event, the forecast issued at a particular time, the target, the selection and the settlement revision. `(card, rank)` is not a unique target identity: ranks can change across views and revisions, while different lines on the same game are different contracts.

| Group | Required fields |
|---|---|
| Identity | `event_id`, `event_cluster_id`, `forecast_id`, `card_id`, `decision_id`, `target_id`, `competition`, `season`, participant IDs |
| Contract | target quantity, period, line, side, units, overtime/draw/push/void/action terms, contract version |
| Timing | input cutoff, actual issue time, independently evidenced event-start/state receipt, input availability time, horizon |
| Frozen model | distribution type/object/hash, p-win/p-push/p-loss/p-void or explicit conditioning, q and its declared interpretation, issued rank, method/control/code/parameter hashes |
| Evaluation selection | `preferred_at_issue`, complementary-pair ID, covering-pair ID, target weight, selection-policy version |
| Baselines | baseline probability/vector, baseline status, exact competition/endpoint, training cutoff, baseline version; team baseline separately |
| Settlement | observed value, result, verification state, source receipt IDs, revision ID, supersedes/reason fields |
| Eligibility | pregame/live, learning/performance status, prospective-cohort ID, exclusion reason, eligibility-policy version |

Represent missing values as null plus a status/reason. Do not store `NOT_YET_DERIVED` and 0.500 as though they were one measurement. Distinguish “not covered by model,” “model has no demonstrated resolution,” “retrieval failed,” and “value genuinely estimated near 0.5.”

**Migration sequence:** new cards first; P-518–P-522 next after verification; then probability-era historical cards with surviving evidence. Keep ordinal-era and unrecoverable rows in an explicitly limited historical view. Do not manufacture p, q, push masses, issue times or baselines to fill the schema.

**Acceptance:** exact event and target uniqueness; conflicts fail closed; two opposite rows share a target and do not create duplicate trials; nested lines stay distinct but share an event cluster; live rows remain in the archive but are excluded from pregame views; every migrated value links to its original location.

## 4. Make scoring follow the existing mathematical specification

**Owner:** scoring maintainer. **Files:** `tools/calibration_report.py`, `tools/skill_baseline.py`, `tools/evidence_status.py`, extractor, ranking data loader and relevant tests. **Addresses:** F4–F5.

### Correct the unit and probability first

1. Select the frozen preferred decision by its explicit flag, not `p >= 0.5` and not which side won.
2. For genuinely binary, action-valid targets, use `(p - y)^2`.
3. For push-capable targets, retain the whole W/P/L vector. Under the current half-scaled categorical convention use `0.5 × Σ(p_k - 1[y=k])²` across the declared categories. If void is separately modelled, declare the category space and scale explicitly.
4. Report decisive-only binary scoring separately using `p_win / (p_win + p_loss)` on decisive observations. Never silently use unconditional win p after removing pushes. Preserve historical mixed scores as `LEGACY_MIXED_DIAGNOSTIC` where the vector is missing.
5. Compare each forecast against a baseline on the same event, target, contract, conditioning and information cutoff. Missing baseline means no paired comparison for that row, with the exclusion counted.
6. Average prespecified target scores within each event, then weight events equally for the principal event-level result. If a decision-weighted diagnostic is useful, label it separately. Resampling events does not, by itself, change a decision-weighted point estimate into an event-weighted one.
7. Use paired event-cluster bootstrap differences, with date/week-block sensitivity when schedule dependence matters. Repeated analyses, leagues and slices require a declared primary metric and multiplicity policy; do not select the most favourable result after looking.
8. Derive prospective progress only from an eligibility join: valid issue before start, frozen p/q/baseline, valid terminal evidence, matching control version, unique decision/event and declared cohort. Report missing-field reasons, not just a count.

### Regression cases that must pass

| Case | Expected behaviour |
|---|---|
| P-443 Over 8, W/P/L 0.45/0.13/0.42 | Preferred target retained; decisive p = 0.5172413793; categorical and decisive scores kept separate |
| Exact 0.50/0.50 forced pair | One target decision under the frozen preference/tie policy, not two independent trials |
| Two covering handicap rows | Both may be retained as distinct contracts; mechanical Hit@2 is excluded from reliability claims |
| A card with many lines versus one with few | Equal-event principal metric gives both events equal total weight |
| P-518/P-519/P-521/P-522 | Archived as live-issued; cannot advance a pregame prospective checkpoint |
| Missing q or method hash on a P-518+ row | Not counted as a qualifying RM-1 prospective observation |
| Missing baseline | Remains missing; no automatic 0.5 substitution |
| P-036 rank conflict | Quarantine or explicitly reconcile identities; no last-occurrence winner by default |
| Revised settlement | Original forecast untouched; changed label creates a traceable new score revision |

**Acceptance:** the 639-row all-row Brier reproduces as 0.226835 on the old dataset under its legacy label; proxy diagnostic values reproduce as documented in the review; the new eligible view has an independently reconciled count and exact exclusions. No claim that the new number is “better” merely because the denominator changed.

## 5. Make probability coherence and validation semantic

**Owner:** model/tool maintainer. **Addresses:** F6–F8.

Keep the existing completeness checker, but label its result **fields present**. Add a second validator for relationships and evidence. The checker already admits that it does not establish truth; the missing step is treating semantic verification as a required outcome of the workflow.

**Distribution checks:** nonnegative masses; declared total mass; valid support; exact complement/push identities; nested-event monotonicity; covering-pair union bounds; joint probabilities within Fréchet bounds; endpoint compatibility; CDF queries reproducing every row. For discrete team-score models also check valid score pairs, total/margin relationships and declared no-tie treatment. When a continuous approximation is used, label its support limitations.

**Specific reproductions:** P-518's Normal margin must not be certified as the same object as its different hand-built margin table. P-522's q values 0.535 and 0.342 must fail a probability interpretation for the covering pair. P-519's capped second-row tier must prevent an unqualified `TOP2_STRONG` statement. P-520's near-tied-flip exception must be named in the ordering rule.

**RM-1 treatment:** preserve historical q and the existing user-authorised model during the audit. Add an explicit statement that its independently calibrated rows may not form one joint probability distribution. Do not use q products as a joint-success estimate without a coherent joint model. A candidate repair could calibrate the distribution, or fit row probabilities under event-geometry constraints; either requires fresh evaluation. Do not silently project q onto constraints and describe that as a validated improvement.

**Evidence checks:** exact event IDs agree across issue/settlement; source receipts contain the claimed field; lineages are deduplicated; cutoff precedes issue and issue precedes actual start for pregame; frozen baseline and model fields are unchanged; settlement process names and quantities match the source, not merely any text on the card.

**Acceptance:** tests reject each demonstrated defect, not just missing headings. Correct fixtures pass. Historical records receive appended diagnostics rather than rewritten predictions. New invalid cards fail closed or are delivered in a clearly limited non-probabilistic state under the governing policy.

## 6. Reconcile the documents after the data and tools

**Owner:** documentation maintainer. **Addresses:** F3, F5 and F10.

1. Generate one current capability table by competition and target: implemented, source-supported, historically evaluated, prospectively evaluated, approved for issue. Point README, numerical program/register and sport headers to it.
2. Replace the wrong “decision Brier 0.2268” label. Print metric version, population, denominator and weighting wherever the value is repeated. Keep the original research findings under a clearly dated historical heading.
3. Replace broad calibration/skill language with what the comparison supports. For example: “The historical mixed-row diagnostic has Brier 0.2268; no prospective advantage over a matched baseline has yet been demonstrated.”
4. Reduce the mandatory entry document to the actual sequence and stop conditions. Put formulas, evidence origins and superseded policies behind stable links. A shorter entry point must not delete the audit trail.
5. Generate queue summaries from the reconciliation register. Distinguish reserved IDs, issued cards, administrative no-forecasts, live-issued records, unresolved fields and fully verified settlements.
6. Keep observations and hypotheses separate in learning entries. Each predictive candidate needs a population, mechanism, comparison, parameter source, frozen test and decision criterion. The proposed +15% width is a hypothesis, not an estimated effect.
7. Repair stale local references and clearly mark unavailable historical snapshots. Two missing relative links were detected in `PREGAME_ELIGIBILITY_REGISTER_2026-09-05.md`; do not silently replace an unavailable original with an unrelated later document.
8. Regenerate the current control manifest only for the final coherent governance change, with the correct category. Repoint the relevant method/mini-log references and verify readback. Integrity and documentation repairs do not establish forecasting gains.

**Acceptance:** one current answer to model status and queue state; one correct label per metric; no active summary reinstates a withdrawn rule; historical snapshots remain traceable; links and manifest verify.

## 7. Run a small, valid prospective programme

**Owner:** research operator. **Addresses:** F9 and the validation rating.

Start with a competition and target for which the whole chain is operational: a schedule universe, official state, available features, a registered baseline, exact contract scoring and a shadow implementation. Choose the scope before inspecting its outcomes. This is an operational pilot; it is not a recommendation that the league will be profitable or that a sport with more historical 70% favourites necessarily offers better decision value.

Before the first issue, freeze:

- Population, competitions, target families, exclusion rules and selection policy.
- Date boundaries and review checkpoints; do not label a previously explored interval untouched.
- Model, ranking and baseline versions; exact training data cutoff and feature availability policy.
- Primary paired event-level proper score, meaningful improvement tolerance, uncertainty method and critical slices.
- Handling of missing data, late starts, postponed games, pushes, voids and rule changes.
- Outcome-independent rules for when the programme continues, stops or opens a method review.

**Daily operation:** declare the universe before selecting events; prepare static records early; refresh only volatile inputs close to start; complete evidence checks; freeze and issue before actual start; freeze the blind shadow before start; record every skip or miss honestly. At settlement, generate the table from frozen values and verified outcomes, then update the baseline and shadow ledgers. If the window is missed, retain the live classification and do not count it toward pregame evidence.

The existing **100 decisions / 30 cards**, **25 RM-1 cards** and **150 shadow games/rows** are review checkpoints, not proof thresholds or substitutes for precision. A study may need more events for a narrow interval or rare slice. A positive pooled result does not automatically establish a benefit in each league, endpoint or probability band.

Keep any operator-entered closing-probability benchmark after settlement and separate from forecast construction, as current policy requires. It is an additional comparator, not a reason to fetch market inputs into the predictive lane.

**Acceptance:** all eligible events have an accounted disposition; every scored row has its frozen inputs and verified result; prospective counts reconcile to the event register; no live/backfilled row enters the pregame cohort; outcome-independent checkpoints are honoured.

## 8. Evaluate predictive changes only after the measurement repairs

**Owner:** model reviewer. **Addresses:** RM-1, subjective adjustments and the numerical research programme.

The current historical work justifies testing, not a blanket model replacement. RM-1's term selection used the record later used to evaluate it; the research README acknowledges that. Several reduced-feature v2 models were redesigned after earlier failures in the eventual test windows, also disclosed. Preserve those limits prominently.

For a proposed change:

1. State the exact defect or hypothesis and retain a simple comparator.
2. Freeze source admission, feature availability, split dates, candidate settings and primary metric before the new test.
3. Fit preprocessing, parameters and optional calibration only in the permitted earlier blocks. Use chronological, event-grouped evaluation. If trying several settings, select them inside training/tuning data, not on the final test.
4. Evaluate the same targets/events for both methods, with paired event-level differences, uncertainty, calibration, support and critical-slice checks.
5. Preserve failures and inconclusive results. Absence of a significant difference is not proof of equivalence or that the present model is best.
6. Require relevant prospective operation before promotion under the existing policy. Never optimise specifically to recover the outcome of one lost game.

**Acceptance:** no material data/chronology defect; the frozen decision rule is met; support and calibration checks pass; claims match the exact scope; otherwise keep the candidate experimental and collect more evidence.

## 9. Completion checklist and handoff

Do not close this repair programme merely because the files read better. Close individual phases when their evidence passes:

- [x] Reviewed source snapshot archived; original issued fields unchanged and the working mini-log hash rechecked.
- [x] P-518–P-522 exact-event spot checks registered with explicit source-lineage and process limitations; full canonical settlement reconciliation remains open.
- [x] No baseline value or missingness was replaced during settlement.
- [ ] Canonical log, status register and mini-log pointer agree.
- [x] Event/decision schema retains horizon, W/P/L, q, baselines and eligibility.
- [x] Parser conflicts and missing rows are retained separately or explicitly quarantined.
- [x] Metrics use the right denominator, conditioning, weighting and comparator in the revised gates.
- [x] Covering-pair, nested-target, joint-bound and distribution-query regression checks run.
- [x] Prospective counters reject live, unverified and incomplete records.
- [x] Current documentation and the regenerated control manifest agree with the tools.
- [ ] At least one complete prospective issue-to-settlement cycle has been verified.
- [x] Model improvement claims remain withheld until the declared evaluation supports them.

Run the existing test suites, hygiene check and manifest verification after implementation, plus the new semantic regression cases. Review the actual changed artifacts and representative source joins. Use a scoped branch/commit and the repository's review process; do not include unrelated worktree changes.

The near-term success criterion is **a trustworthy and reproducible research process**. Predictive improvement is a separate empirical question that the repaired process will finally be able to answer.
