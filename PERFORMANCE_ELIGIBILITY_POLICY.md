# Performance eligibility and user-confirmed freeze policy
> **Current revision — CR-2026.09.21-3:** METHOD **MDS-2026.09.19-v4.3** is the workflow/template authority; **SCORING_AND_VALIDATION.md** controls conditioning, exact scoring, event-level evaluation and prospective evidence. **All current combined-log material remains LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE.** Older settlement-only eligibility text below is retained as policy history and is non-operative for current performance claims unless a later controlling user instruction explicitly reactivates it.




> **2026-09-12 controlling correction:** All current combined-log material is LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE under the current user request. Settlement preserves outcome evidence; it does not authorize a performance claim. The [2026-09-12 audit](COMPREHENSIVE_SETTLEMENT_AUDIT_2026-09-12.md) and [probability/research corrections](audit_2026-09-12/rule_corrections.md) supersede conflicting older operational statements. Original issued records remain unchanged.




> **Current operative rule:** `METHOD.md` §7 states that settlement alone does **not** confer performance eligibility. The older settlement-only rule below is retained for provenance and historical interpretation, not as current authority.


Policy: **EP-2026.09.06-v2**
Current method: **MDS-2026.09.19-v4.3 / CR-2026.09.21-3**


<!-- CURRENT-ELIGIBILITY-OVERRIDE-2026-09-21-CR3 -->
## Current eligibility override — 2026-09-21 / CR-2026.09.21-3


For current reporting, the 2026-09-12+ controlling state is **LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE**. Settlement remains necessary to know an outcome, but settlement by itself is not authorization to present the historical pool as validated predictive performance. The 2026-09-06 settlement-only policy below is retained as historical policy and must not be used to override this current state.


## 2026-09-06 user directive — settlement is the sole performance-eligibility gate *(historical; superseded for current claims)*


The user directed: **any log that has been settled counts for performance eligibility.** Effective 2026-09-06, this replaces every narrower eligibility test previously used in this repository — pre-game-versus-live-issued horizon, local-import timing, git-history presence, hash/timestamp provenance, and the `E1-Q` / `E1-Q-LATE_IMPORT` qualitative-only labelling — as the gate for whether a settled contract/rank counts in the historical **performance** scorecard. The single test is now: **has the row reached a final, graded result?** If yes, it is performance-eligible. This supersedes the 2026-09-05 `USER_CONFIRMED_PREGAME_FREEZE` correction below only on the scope question (which cards count); that correction's underlying reasoning (provenance ≠ forecast validity, a late import does not retroactively disqualify a genuinely pre-issued pick) is superseded by a broader rule that no longer needs it to reach the same practical result for live-issued cards too.


Concretely, this means:


- **`LIVE_ISSUED` cards are no longer a separate excluded cohort.** Every row in `PREGAME_ELIGIBILITY_REGISTER_2026-09-05.md` currently marked `SEPARATE LIVE COHORT — excluded from pre-game metrics` is, from this date, performance-eligible on the same basis as a `PREGAME` row, provided it reached `FINAL / SETTLED` (or an identifiable settled sub-row within a `FINAL / PARTIAL` card). A live-issued forecast still ranks and settles under its own issued text and its own issued cutoff/state — this directive does not retroactively convert a live-issued rank into a pregame one, or edit what was issued. It only removes live-issued status as a reason to exclude an otherwise-settled row from the performance count.
- **Import timing, `E1-Q-LATE_IMPORT`, and git/local-timestamp provenance stop functioning as performance-eligibility gates.** A card imported after its event's scheduled start, with no independently verifiable pre-result timestamp, is still performance-eligible once settled — the same practical outcome the 2026-09-05 correction already reached for non-live cards, now extended without needing a separate provenance argument, and now covering live-issued cards as well.
- **What is unaffected by this directive:**
  - No-forecast / no-action / administrative-closure records still contribute nothing — there is no issued row to grade.
  - A row still unresolved, void, partial or `EVIDENCE GAP` stays outside the count until it too reaches a graded final; it does not count as a win, a loss, or a push by default.
  - Process grade and outcome grade remain separately tracked (L-013). A process-defective win still counts as a win in the performance scorecard; it is separately flagged as process-defective. This directive changes *which* settled rows count, not the existing rule that a bad process can still win and a good process can still lose.
  - Issued forecasts, ranks and settlement text remain immutable; corrections are appended, never rewritten (no hindsight rewriting).
  - This remains a **descriptive, retrospective performance/accuracy record.** It is not a claim of calibration, statistical significance, betting edge, ROI, or validation of any numerical model. The numerical program (`NTS-2026.09.02-v0.3`, Stage 0, no fitted model) and its own `E1-P` shadow-probability test cohort are governed separately by `ALGORITHM_PORTFOLIO_AND_EVALUATION.md` and `NUMERICAL_TRAINING_SPEC.md` and are **not** affected by this directive — settlement alone does not make a card usable as model training/calibration/test data; that still requires the numerical program's own frozen manifest process.


`PREGAME_ELIGIBILITY_REGISTER_2026-09-05.md`, `GAME_LOG_STATUS_INDEX_2026-09-05.md` and the active combined log's snapshot are updated to reflect this rule; see each file's own 2026-09-06 addendum for the mechanical restatement rather than a full per-row rewrite.


## 2026-09-06 addendum — mandatory stratification (`L-090`, external blindspot audit `B-04`)


**Settlement remains the sole eligibility gate; this addendum governs how an eligible pool may be reported, not who is in it.** An externally supplied blindspot audit (`archive/EXTERNAL_BLINDSPOT_AUDIT_2026-09-06_RECEIVED.md`) correctly observed that `EP-2026.09.06-v2` makes settlement the sole test of whether a row *counts*, but says nothing about how the resulting pool should be *reported* — and pooling rows issued under different method versions, horizons, sports and target families into one headline percentage would be statistically uninterpretable even though every row in it is legitimately eligible.


**Requirement.** Any headline performance figure computed from the settlement-only eligible pool must be accompanied, at minimum, by a breakdown across:


1. **Issued method version** (`MDS-<date>-v<n>`) — a v2.5 card and a v3.8 card were produced under materially different process rigour and should not be silently averaged.
2. **Pregame-versus-live-issued horizon** — retained as a reporting dimension even though it is no longer an eligibility filter.
3. **Sport / competition** — a baseball-heavy period should not be presented as if it characterises cricket or tennis performance.
4. **Target family** — winner / handicap / total / phase / derivative-and-niche, since these have different structural win-rate properties (see `L-091` on complement-forced pairs).
5. **Event-versus-decision-set weighting** — a twelve-contract card must not out-vote a single-contract card in an event-level summary; report event-level Rank-#1 accuracy and exact-pair ordering ahead of, or alongside, any raw row tally, never in place of it.


A single undifferentiated pooled percentage may be *computed* for internal reference, but may never be presented as the primary or only performance claim without this breakdown alongside it. This addendum adds a reporting discipline; it does not reopen, narrow, or add a new test to `EP-2026.09.06-v2`'s eligibility question itself.


## 2026-09-05 user confirmation — pre-game freeze basis (retained context; scope superseded above)


The user confirmed: **all existing game logs except views explicitly labelled LIVE were strictly frozen pre-game**. Accept this as the provenance basis `USER_CONFIRMED_PREGAME_FREEZE`, effective September 5. Non-live issued cards are eligible for historical qualitative directional/ranking evaluation. A late local import alone no longer excludes them. This correction supersedes earlier blanket `E1-Q-LATE_IMPORT`, “all non-performance-eligible” and “zero eligible historical units” statements. It records user confirmation; it does not assert independent timestamp verification or change original file times.


Keep four distinct fields: **forecast horizon at issue**, **event state when checked for settlement**, **provenance basis**, and **endpoint settlement status**. An originally pre-game card found live during settlement stays pre-game and awaits a final; it does not become a live-issued forecast. A live source/page, a “live counter-branch”, or a post-issue status check is not an issuance label. Explicit live or live-state-unverified issued views stay outside pre-game metrics. Original pre-game and later live views of one event must retain their own ranks and share an event cluster.


The headline historical scorecard includes all identifiable, genuinely issued, settled contracts/ranks in its stated cohort, including `FORCED RANK`, LOW evidence, and `PROCESS_DEFECT` outcomes. Do not remove a bad pick because its reasoning was poor. Process grade is a diagnostic column and a separately labelled compliance slice. No-forecast/no-action records are not trials; unresolved/void/push/partial rows have explicit denominators; materially unidentifiable contracts remain unscorable with the reason recorded. A row’s missing operator terms may limit ticket settlement without erasing a clearly defined research endpoint. Never use an issue-time row already decided as a predictive success.


Use the exact original pre-game order, including the latest genuinely pre-game refresh; never substitute a later live or retrospective order. Deduplicate aliases and group related targets/views by underlying event. Report historical performance by issued method, sport/competition, horizon and target. The ten newly settled cards are an evaluated v3.4 pre-game cohort. Earlier historical scorecards need those same row/view joins before a new all-history aggregate is reported; the complete status index is not itself a performance denominator.


Old games may measure their issued methods and supply development evidence for improvements. They cannot validate a v3.5/v3.6 change designed after their outcomes were seen. Keep the historical ranking count separate from each frozen challenger’s later test count. No probabilities, fitted coefficients, calibration or market-edge claims are created by this provenance correction. Future snapshots/hashes and externally timestamped revisions are useful provenance records; a local hash or editable git timestamp alone is not an independent timestamp authority, and no git-only approval gate is imposed on this user-confirmed history.


## 2026-09-09 — user-directed learning-only carve-out for the `P-333`–`P-344` cohort


**Standing policy `EP-2026.09.06-v2` is unchanged:** settlement remains the sole eligibility test, and any settled row counts in the descriptive scorecard regardless of horizon or import timing.


**Current user directive, which takes precedence for this cohort only** (`RULES_GENERAL.md` §0 / `METHOD.md` §9 precedence order — a current user directive outranks a standing policy): the user has stated that this log *"is still not performance-eligible, but continue to use it to learn and improve."* Accordingly, for `P-333`–`P-344`:


- the cohort's settled rows **are** folded into the running Brier scorecard in `PREDICTION_LOG_COMBINED_3.md`, for ledger continuity and so the numbers are not hidden;
- but **no accuracy, quality, calibration, discrimination or improvement verdict may be drawn from them**, and no statement anywhere may present this cohort as evidence that the method works or has improved;
- the cohort's role is **diagnostic and instructional only** — it exists to surface failure mechanisms (which it did: `G-L7`'s aggregate-to-disaggregate finding came entirely from it) and to feed the prospective test manifests.


This is a scope restriction on *interpretation*, not a change to any settled result, rank, probability or Brier value. It does not alter `EP-2026.09.06-v2` for any other cohort. Two honest figures that must travel with any citation of this cohort: its `EXPLORATORY` subset scored **0.2665 mean Brier against a 0.2500 trivial baseline — worse than the baseline**, and the `PRIMARY_SCORED` card count stands at **4 of the 25** required before the first pattern/calibration review means anything.


The same restriction is recorded in `PREDICTION_LOG_COMBINED_3.md`'s controlling snapshot (Performance-eligibility row) and `METHOD.md` §"2026-09-09". Where a future session finds this cohort cited as performance evidence, that citation is wrong and should be corrected to this carve-out.


## 2026-09-11 — learning-only carve-out extended to `P-345`–`P-371`


The user restated on 2026-09-11 that the log *"is still not performance-eligible, but continue to use it to learn."* The 2026-09-09 carve-out above therefore **extends to `P-345`–`P-371`** on identical terms: the cohort's settled rows are folded into the running Brier scorecard for ledger continuity, but **no accuracy, quality, calibration, discrimination or improvement verdict may be drawn from them**. The figures that must travel with any citation: this import's mean Brier **0.2434** over 105 rows, with its later half (`P-358`–`P-371`) at **0.2621 — worse than the 0.2500 trivial baseline**; rows stated at 70%+ won 62% of the time; `PRIMARY_SCORED` card count **8 of 25**. Standing policy `EP-2026.09.06-v2` is unchanged for every other cohort.


## 2026-09-17(b) — learning-only carve-out extended to `P-424`–`P-451`, and the first `PRIMARY_SCORED` material in Part 4


The standing user direction is unchanged: the log **is not performance-eligible**, and is used to learn. The carve-out above therefore extends to `P-424`–`P-451` on identical terms — rows fold into the running scorecard for ledger continuity, and **no accuracy, calibration, discrimination or improvement verdict may be drawn from them.**


Two things about this cohort change what must travel with any citation of it.


**1. It contains `PRIMARY_SCORED` cards for the first time since Part 4 opened.** Eight of the fourteen `P-438`–`P-451` records are MLB. The `PRIMARY_SCORED` card count moves **25 → 33** and the row count **104 → 136 at ≈ 0.2468 mean Brier**, against a 0.2500 trivial baseline. That is a **0.003 improvement on a coin flip over 33 cards**, which is indistinguishable from noise and must never be presented otherwise. The next pattern review is due at **50 cards**; until then the `PRIMARY_SCORED` record supports no verdict of any kind.


**2. Its headline row count is structurally inflated, and the honest figure is smaller.** All 32 MLB rows added here are `FORCED_PAIR` — the cards were issued on `{dog +1.5, fav −1.5, Over L, Under L}`, two complementary pairs, so **each card scored exactly 2 W / 2 L whatever happened**. The "16 W / 16 L" this contributes is arithmetic, not performance. Under the `G-L22` counting rule (`METHOD.md` §5) the same eight cards represent **16 decisions, 10 correct**. Any citation of this cohort's `PRIMARY_SCORED` numbers must carry that split, because pooling forced pairs with free rows biases the aggregate W/L toward 50% and makes the Brier a statement about the supplied line rather than the analysis.


**Figures that must travel with any citation of `P-424`–`P-451`:**


| Figure | Value |
|---|---|
| `P-438`–`P-451` cohort mean Brier | **0.2097** over 52 rows, vs 0.2500 trivial |
| — of which MLB (`PRIMARY_SCORED`) | 0.2293 over 32 rows, **all forced pairs = 16 decisions, 10 correct** |
| — of which soccer (`EXPLORATORY`) | 0.1783 over 20 free rows — **the gap is contract geometry, not skill**: the soccer cards had wide alternate lines available and the MLB cards did not |
| `PRIMARY_SCORED` running total | **136 rows / 33 cards / ≈ 0.2468** — 0.003 better than a coin flip |
| ≥ 0.80 probability band, this cohort | 11 W / 15 at a mean stated 86.4% — but **3 of the 4 losses are one card**, so the effective independent sample is ~2 events |
| Mechanical completeness audit | **13 of 14 cards missing at least one BLOCKING §16.8 field**; field 5a (shared-failure mass) missing on **13 of 13** cards that could be audited |


That last row is the one that most constrains interpretation. A cohort in which the mandatory completeness block was essentially never executed cannot be read as evidence about the method's quality, because **the method as written was not the method that was run**. The `P-424`–`P-437` mini log is worse in one specific respect: it carried no issued card bodies at all, only picks and settlement, so its issue-time compliance **cannot be audited even in principle** — see `EXTERNAL_LOGGING_WORKFLOW.md` §"2026-09-17(b)".


`EP-2026.09.06-v2` is unchanged for every other cohort. The same restriction is recorded in `PREDICTION_LOG_COMBINED_4.md`'s controlling snapshot and `METHOD.md` §"2026-09-17(b)".


<!-- DEEP-RESEARCH-IMPLEMENTATION-2026-09-19-V42 -->
## 2026-09-19(c) — added eligibility requirements


No model/version is performance-eligible unless its evidence chain proves all of the following for the exact evaluated population:


- no prohibited betting/market/fantasy source entered predictive features, priors, calibration or model selection;
- every feature has a point-in-time `known_at <= cutoff` lineage;
- all views of one event are grouped together in chronological validation;
- preprocessing and feature learning were fold-local;
- calibration/ensemble fitting used only declared CAL/OOF material;
- untouched TEST was opened once and unsuccessful results were retained;
- evaluation includes proper distribution/contract scores, calibration/coverage and uncertainty, not hit rate alone;
- prospective shadow forecasts carry source/model/control hashes and survive live missingness/source-latency conditions.


A software test pass demonstrates control correctness only. It does not make the forecasting model performance-eligible.