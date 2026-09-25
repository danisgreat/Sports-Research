# METHOD — operational forecast and settlement procedure


Status: **ACTIVE — primary operational authority**
Method version: **MDS-2026.09.19-v4.3**
Control revision: **CR-2026.09.21-3** — preserves CR-2026.09.21-2 and removes residual live-rule/version/queue drift found by post-reconciliation read-back. Freeze the SHA-256 file receipt from [CONTROL_MANIFEST_2026-09-25-6.md](CONTROL_MANIFEST_2026-09-25-6.md) with every new card. It re-hashes [CONTROL_MANIFEST_2026-09-25-5.md](CONTROL_MANIFEST_2026-09-25-5.md), the Rank-1/Rank-2 content receipt (2026-09-25(e)) under the same control revision, after the 2026-09-26(a) canonical-ID assignment (P-516, P-517; README, CHANGELOG and the settled-row extractor). No card was issued under -5. It adds `C-RANK-MODEL` (RM-1, `tools/rank_model.py`), `C-TOP2-QUALITY`, `C-TEAM-BASELINE` (TB-1, `tools/team_baseline.py`), the amended `C-PLUS-CUSHION`, `C-SETTLEMENT-FROM-FEED` and the NFL/AFL/NRL references to everything in [CONTROL_MANIFEST_2026-09-25-4.md](CONTROL_MANIFEST_2026-09-25-4.md). That manifest was the post-settled-row-review receipt and remains the receipt for P-510–P-515. It added the 2026-09-25(d) calibration controls and construction tools (`C-PLUS-CUSHION`, `C-DEPARTURE-LEDGER`, `C-TRACK-RECORD`, `C-LOW-RESOLUTION-BAND`, `tools/card_math.py`, `tools/calibration_report.py`) to the 2026-09-25(c) baseline-skill, current-rules and repository controls, and the earlier 2026-09-24(f)/2026-09-25 controls. Verify it with `python tools/verify_manifest.py`. [CONTROL_MANIFEST_2026-09-25-3.md](CONTROL_MANIFEST_2026-09-25-3.md), [CONTROL_MANIFEST_2026-09-25-2.md](CONTROL_MANIFEST_2026-09-25-2.md) and [CONTROL_MANIFEST_2026-09-25.md](CONTROL_MANIFEST_2026-09-25.md) were the receipts of the repository review, the research pass and the audit closure (no card was issued under any of them); [CONTROL_MANIFEST_2026-09-23.md](CONTROL_MANIFEST_2026-09-23.md) remains the receipt for P-495–P-509; [CONTROL_MANIFEST_2026-09-21-3.md](CONTROL_MANIFEST_2026-09-21-3.md) for cards issued before 2026-09-23 about 22:00 AEST.
Effective: 21 September 2026 for forecasts issued after this control revision; earlier cards retain their issued method/control versions.


This revision implements [the model audit](archive/audit_documents_implemented_2026-09-25/MODEL_REVIEW_2026-09-17.md). The complete previous method is preserved in the before snapshot (`audit_2026-09-17_implementation/before/METHOD.md`, not present in this repository). Detailed gate IDs in RULES_GENERAL and sport files remain traceable; this document is the single workflow and compact output authority. [SCORING_AND_VALIDATION.md](SCORING_AND_VALIDATION.md) is the single mathematical/evaluation authority. Older dated addenda describe historical decisions and cannot reinstate withdrawn rules.


<!-- THREE-SOURCE-TIME-GATE-2026-09-19-CR4 -->
## Universal three-source, event-time and terminal-state hard gate — 2026-09-19


Every new event requires at least **three distinct reliable upstream source lineages**. Mirrors, syndicated copies, reposts, search snippets, generated summaries and multiple pages from one feed do not create additional independent sources. Where available, use a field-owner exact-event source, an official team/club/participant or second primary source, and an independent high-quality secondary source.


Before issue or refresh, verify venue/host city and country, official venue-local date/time, IANA venue timezone and exact-date UTC offset, and the timezone-aware conversion to `Australia/Melbourne`, including the correct **AEST/AEDT** label and calendar-date rollover. User-supplied times are estimates until independently verified; print any correction explicitly.


Immediately before issue/refresh, verify event state across the qualifying source set. A scheduled time does not prove the event has started, and elapsed expected duration does not prove it is final. Material source conflict produces `EVENT_STATE_CONFLICT` and fails closed.


No event may be settled until at least **three distinct reliable lineages** agree on the exact event/date, explicit terminal status and final result. A score without an explicit final marker is insufficient; any credible current live/in-progress source blocks settlement. Search-result summaries never count as settlement evidence. Re-check immediately before a Drive status transition and read back the file afterward.


Use fail-closed labels as applicable: `SOURCE_COUNT_LT_3`, `SOURCE_LINEAGE_NOT_INDEPENDENT`, `EVENT_DATE_NOT_VERIFIED`, `EVENT_LOCAL_TIME_NOT_VERIFIED`, `EVENT_TIMEZONE_NOT_VERIFIED`, `MELBOURNE_TIME_CONVERSION_NOT_VERIFIED`, `EVENT_STATE_CONFLICT`, `FINAL_STATE_NOT_VERIFIED_BY_3_SOURCES`, `DERIVATIVE_SETTLEMENT_FIELD_NOT_VERIFIED_BY_3_SOURCES`.


P-469 is the reference failure case: a misleading search summary conflicted with opened live sources, so settlement should have remained blocked.




<!-- CRICKET-SOURCE-PATCH-2026-09-21-CR1 -->
## Cricket source-control patch — CR-2026.09.21-1


This control revision does **not** change the forecasting objective, model family, calibration state or any predictive coefficient. It repairs cricket evidence retrieval and classification after a fresh source audit.


For cricket only:


1. `TOSS STATUS` and `STRIP STATUS` are separate fields and use separate search ladders in `RULES_CRICKET.md` §2 / `DATA_SOURCE_REGISTER.md` §6A.
2. The toss fact is searched through the field owner first, then official/rights-holder video, official team/competition updates, admitted structured endpoints, specialist exact-match records and independent reporting.
3. An exact-match strip can be `OBSERVED` only from a named current-match observer/source class defined in the cricket rules. Previous same-venue matches, venue averages and ICC pitch ratings are context, not today's strip.
4. Official board/competition video and sanctioned NV Play/board-branded Match Centre are explicit late-information lanes. A specialist transcript of the same broadcast is the **same upstream lineage**, not independent confirmation.
5. Identical or near-identical unusual pitch metadata across front ends is `AUTOMATED_PITCH_METADATA` and a suspected shared feed until provenance proves otherwise. It cannot masquerade as multiple independent observed strip reports.
6. A same-format venue baseline may legitimately be unavailable. Record `INSUFFICIENT_VENUE_HISTORY`, use a labelled broader comparable prior if appropriate, and widen uncertainty; never fabricate a sample.
7. An official page can be stale for a specific field. Mark the affected field `STALE`, preserve any still-valid identity fields, and use another official/static/sanctioned route plus independent corroboration.
8. The toss-window refresh and final pre-issue refresh are mandatory research steps. Failure to find an exact strip after the full shown search is an evidence limitation, not permission to invent it.


The executable preflight companion is advanced to this control revision and checks the new cricket source-state object. These controls are integrity/retrieval controls only; no forecast-improvement claim follows.




## 1. Role and objective


<!-- DEEP-RESEARCH-IMPLEMENTATION-2026-09-19-V42 -->
### 1.1 Mandatory independent-forecast pipeline


The requested line/total may be parsed for contract identity, but it is **quarantined** from forecasting. The required sequence is:


`identity/contract parse -> quarantine threshold -> valid sports evidence -> canonical facts -> features -> independent joint outcome distribution -> freeze/hash distribution -> query supplied line(s) -> rank/output`.


The following are forbidden before the distribution freeze: implied probability from odds, line movement, consensus, sportsbook previews, betting picks/tips, fantasy/DFS projections, fantasy ownership/rankings, and any secondary article whose analysis is derived from those sources. The supplied threshold cannot be a prior, anchor, feature, target-centering device, calibration target, scenario weight, or sanity-check direction.


If only a prohibited source contains a material fact, record that fact as `UNAVAILABLE`; do not import it because it looks plausible. A valid upstream field owner or independent source must be recovered first.


Every material input carries `source_id`, `source_class`, `field_owner`, `upstream_lineage_id`, `published_at`, `first_known_at`, `retrieved_at`, `cutoff_at`, `freshness_status`, `validity_status` and `snapshot_hash` where available. Multiple sites on one feed are one lineage, not independent corroboration.


### 1.2 Quantitative discipline for centres, totals and margins


No analyst may add or subtract an arbitrary number of runs/points/goals because a narrative seems favourable. A signed effect on the predictive centre must be either:


1. an effect estimated inside chronological training data with shrinkage/regularisation and frozen before evaluation; or
2. an explicit scenario mixture based on independently sourced participant/environment states, labelled `UNVALIDATED_SUBJECTIVE`, with the uncertainty represented in the distribution rather than hidden in a point adjustment.


Short recent-result windows remain descriptive unless a named mechanism changes (for example participant availability, pitch velocity, role, lineup, possession/pace process or weather). Recent outcomes alone do not create a rebound/hangover/"due" adjustment.




Research the exact sporting event, build a coherent distribution or explicitly subjective scenario model, derive every supplied contract's probability, rank by probability of winning, log before delivery, and settle against the frozen endpoint. All forecasts are SPORTS_ONLY / MARKET_BLIND. Supplied lines and operator terms define contracts; odds, market movement, tipsters and previews are not predictive evidence. Prices, if explicitly requested later, are a segregated audit and cannot change the frozen forecast.


All existing combined logs remain **LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE**. PRIMARY_SCORED is a population label, not permission to claim performance. No model is fitted, calibrated or validated by editing this framework. Missing prices/terms or missing validated probabilities means NO VALUE DETERMINABLE; no EV, ROI or staking claim follows from a hit rate.


## 2. Population scoping


Maintain separate populations for MLB, EPL, NRL, AFL and AFLW; the latter are separate competitions even when grouped administratively. Other requested sports remain exploratory until independently scoped. Never pool their score scales, endpoint rules or model parameters merely to increase n. Log and settle every issued card regardless of population; primary versus exploratory labels control comparisons, not which losses survive.


## 3. Lifecycle


1. Start with `CURRENT_RULES.md` (step 0 of the reading gate, 2026-09-25(c)). Then fresh-read this method, scoring specification, active log's top snapshot, applicable sport/competition rules and source records. Read detailed gate text when needed. Record versions and control hash.
2. Inventory mini-log variants and temporary IDs. Check event state and retry-ready queues; settle verified finals in their issuing parts, leave live/unresolved items open, and preserve separate documentary/operator follow-ups. Current active log is Part 5 (`PREDICTION_LOG_COMBINED_5.md`); next ID is read from its top snapshot / `GAME_LOG_STATUS_CURRENT.md`, never from a copied historical summary.
3. Freeze identity, contract, activation, endpoint, horizon, participants and time. PREGAME requires issuance before start; already decided rows cannot issue. A failed blocking identity/action gate means NO FORECAST.
4. Retrieve field-owned evidence: volatile state/lineups/bench/coaches, rules and environment first, then process history and context. Open raw records rather than model-generated summaries. Check the venue-coordinate hourly forecast/current surface for outdoor events. Name missingness and the affected branch. Synthetic results never settle a contract.
5. Construct the six-field object in section 4 using one joint model. Retrieve L5/L10/L15/L20 and H2H windows with continuity and unique-event counts; use them descriptively. State exposure, opponent adjustment, starter/relief or analogous transitions and failure scenarios. Do not double-count overlapping causal adjustments.
6. Query exact probabilities and joint bounds, derive ranks, check support/complements/nesting/period relationships, and refresh volatile evidence immediately before issue.
7. Append the frozen card to the active log before delivery. Update its snapshot in the same edit. Reconcile an external log within 24 hours of availability; an overdue unregistered log blocks the next forecast.
8. Settle the exact research endpoint and operator action separately; append corrections rather than rewriting issued data. Run the retrospective and versioned scores below.


## 4. Compact mandatory forecast object


Each field is printed once; detailed gate references do not require duplicate prose. This replaces repeated lifecycle/checklist overlays and the old nine-field completeness block as the active presentation template, while preserving their substantive checks.


| Field | Required contents and traceability |
|---|---|
| **1 Identity and contract** | Canonical/event-cluster IDs, participants, competition, start/cutoff/issue times, pregame/live horizon, exact target/unit/period, supplied line/direction, activation, action/void/censoring terms, complete terminal states, research/operator distinction, method/control hash. G0–G6, G-L16, G-L19. |
| **2 Evidence and exposure** | Exact source, field owner, publication/availability and retrieval time; both sides' starters/bench/coaches; injury/workload/role state; environment/surface; descriptive windows/H2H continuity/unique n; disaggregated record for every aggregate-driven claim; verified settlement route and missingness. G8–G17, G-L7, G-L11, G-L13, G-L14. |
| **3 Joint distribution** | Prior with provenance and target; model family/support; all disjoint scenario weights; explicit exposure/rate and signed adjustment arithmetic; mean/median distinguished; variance or interval with definition/coverage; team and linked phase marginals; endpoint/termination transitions; representative scores. Uncertainty is integrated through declared priors/scenarios and may alter mean and variance. G-L1, G-L2, G-L8, G-L12, G-L18, G-L20. **From 2026-09-25(b):** print the competition's reference row and reference width (`BASE_RATES_REGISTER.md` §7, or `NOT_YET_DERIVED`) beside the prior, centre and width (`C-WIDTH-BENCHMARK`); a single-game comparator never outweighs the season rate (`R-1` corollary). |
| **4 Contract queries and ranks** | Exact W/P/L and any action conditioning; q(non-push) separately if defined; distribution reference; rank derived from stated objective; FORCED_PAIR/FREE, frozen preferred side, all considered alternate lines; component/separation budgets and sign checks; no numerical row cap disconnected from the distribution. **From 2026-09-25(c):** print `BASELINE_P` beside each ranked row: the naive, leak-free population probability of the same contract, or `NOT_YET_DERIVED` (`C-BASELINE-SKILL`; `SKILL_BASELINE_LEDGER.md`). **From 2026-09-25(d):** derive each row from the printed distribution with `tools/card_math.py` (M14). Print the **departure ledger** from `BASELINE_P`, attributed to named mechanisms (`C-DEPARTURE-LEDGER`). Print the sport's **track-record row** (`C-TRACK-RECORD`). Label rows at 0.50–0.65 `LOW_RESOLUTION`. A non-baseball +k.5 row carries the `C-PLUS-CUSHION` decomposition. **From 2026-09-25(e):**
- print RM-1's q, tier and flags beside each stated p (`python tools/rank_model.py rank`), rank by q, and print the `TOP2_QUALITY` line (`C-RANK-MODEL`, `C-TOP2-QUALITY`);
- in covered leagues, print `TEAM_BASELINE_P` beside `BASELINE_P` and anchor the departure ledger on it where TB-1 has resolution (`C-TEAM-BASELINE`);
- a non-baseball, non-hockey, non-soccer cushion takes its baseline from the population cover rate (`BASE_RATES_REGISTER.md` §7.7(c)). |
| **5 Dependence and checks** | Joint top-two win/failure and all-fail probabilities from the joint states, or JOINT_UNQUANTIFIED with valid Frechet bounds; shared-driver sign for each row; exhaustive complement decomposition including pushes/voids where relevant; key-margin masses, coherence/normalization/nesting checks; evidence grade/missingness and kill paths. G-L9, G-L10, G-L17, G-L21, G-L22. Never invent a joint probability to fill the field. **When the joint states are explicit (a family table or branch tree with masses), the joint numbers are read off that table and printed as numbers.** `JOINT_UNQUANTIFIED` with bounds is reserved for dependence the model does not represent (R-5 of the 2026-09-22 audit; P-483). Label covering pairs `COVERING_PAIR` (SCORING_AND_VALIDATION §3). |
| **6 Freeze and follow-up** | Final volatile-refresh receipt, immutable version/hash, settlement provider/period/action route and retry trigger; at settlement add raw process/disruption record, exact outcome, scoring version and three-question retrospective. G-L23. **From 2026-09-25(b):** in covered lanes the freeze and settlement receipts come from `receipts.py` (`C-RECEIPT-TOOL`); at settlement print z = (actual − centre)/width for total and margin (`C-WIDTH-Z`). **From 2026-09-25(e):** settlement facts are read from the feed, never typed (`C-SETTLEMENT-FROM-FEED`, audit `10n`), and both p and q are scored. |


BLOCKING failures in identity, contract, event state, synthetic-source exclusion and applicable mandatory source gates prevent issuance. Other required-analysis gaps are explicit process defects and cap the evidence grade at FORCED RANK/LOW; that is not a numerical cap on a derived probability. Unsupported numerical/joint values remain unknown. No incomplete model is labelled calibrated.


## 5. Probability and scoring


Every well-formed ranked row carries UNVALIDATED_SUBJECTIVE probability unless an actually promoted numerical build governs that scope. It must be reproducible from the declared subjective distribution; no retrospective probability is added to old ordinal cards. PUBLISHED numerical probabilities require all gates in NUMERICAL_PROGRAM.


Apply [SCORING_AND_VALIDATION.md](SCORING_AND_VALIDATION.md) exactly: half-scaled W/P/L Brier and categorical log loss for push-capable action-settled contracts; decisive binary scores use q=p_win/(1-p_push) and exclude pushes only from that labelled diagnostic. Exact half-line complements sum to one conditional on action. No arbitrary residual for generic uncertainty. Do not silently discard pushes while scoring unconditional win probabilities.


Keep legacy mixed-row Brier separately. The corrected historical total is 477 rows, 273 W/204 L, 0.2265475891; PRIMARY_SCORED is 136 rows/33 cards, 0.246825. These are descriptive legacy diagnostics, not prospective validation. Derive aggregates from row sums, never rounded cohort means. Report rows, decisions and event clusters; forced complements count once per target in decision metrics. Compare with the same-event frozen empirical baseline and fixed threshold grid, not solely p=0.5.


## 6. Honesty boundary


Preserve issued probabilities, ranks, targets, identity and source facts. Append a sourced settlement correction when an earlier settlement is wrong; immutable history does not require perpetuating a wrong current label. Do not manufacture missing features, probabilities, source access, test timestamps or outcomes. Separate verified fact, transformation, model assumption, inference and unknown. A model family or mathematical test is not a fitted or validated model. No guaranteed result, calibration, independence or market-edge claim is justified by this framework revision.


## 7. Settlement, retrospectives and eligibility


Settle each period and definition separately from its field owner, recording disruption timing and final status. Evaluate activation first. A whole-match count cannot prove a regulation Over without a valid lower bound. P-255-C05 and P-256-C05 are now UNRESOLVED_PERIOD; their existing audit handles are reopened, separately from the 23 primary queue handles.


For every settled card answer: (1) what the outcome turned on; (2) whether it was knowable before issue, with evidence; (3) the smallest justified research/model change. Inspect wins as well as losses. A realised tail is not evidence by itself that the tail probability was wrong. Preserve source contradictions and distinguish retrieval/process errors from conversion, endpoint and disruption effects.


**Enhanced-failure review — two triggers (user directive, 2026-09-19).** A deep failure review is mandatory whenever **either** of the following loses:


1. the card's **Rank #1** selection; or
2. the card's **highest-ranked over/under selection** — the preferred side of the top-ranked totals target, whether or not it is Rank #1 overall, and whether the target is a supplied `FORCED_PAIR` or a `FREE` alternate total.


Both reviews use the same enhanced form and the same standard of evidence: why it was ranked where it was; whether the pre-game evidence genuinely supported that placement; whether another row should have outranked it on frozen information; which variable was missing, mis-weighted or mis-sourced; whether an existing control should have prevented it and was executed; and whether a rule change is warranted or the result was variance. A push on the top over/under is **not** a win and triggers the review; the review records the push explicitly rather than treating the target as ungraded. Where the same row is both Rank #1 and the top over/under, one review covers both and says so. Log the trigger as `TOP_OU_REVIEW` so it is separately countable from the Rank-#1 flag (`SCORING_AND_VALIDATION.md` §3).


This raises the standard of scrutiny on totals to match sides. It does **not** change ranking, probability or selection: nothing here licenses hedging a totals pair, softening a stated probability to avoid a review, or declining to rank a total. Reviewing a loss more thoroughly is a retrospective duty, not a forecasting incentive (§6).


**Settlement-integrity controls (2026-09-24(f); RULES_GENERAL §"2026-09-24(f)").** Every settlement:
- reads its process facts from a named record, with the endpoint and retrieval time (`C-PROCESS-RECORD-PROVENANCE`); a block with unsourced causal facts is `PROCESS_RECORD_UNVERIFIED` and supports no rule;
- diffs the card's named starters, starting pitcher or goalie against the official box (`C-LINEUP-DIFF`); a Rank-1 driver who did not play is `PROCESS_DEFECT: LINEUP_CLAIM_FALSE`;
- copies every summary row from the issued Field 4 table (`C-SUMMARY-FROM-CARD`);
- promotes nothing predictive from the games that suggested it (`C-PROMOTION-RECEIPT`; §16.10 item 11).
Run `python audit_card_controls.py <log.md> --settlement --strict` and record the per-card table.

Pattern reviews at 25/50 cards are review schedules only. All current log material remains learning-only; settlement alone does not confer performance eligibility. Promotion of a changed model requires a frozen prospective comparison and complete timestamp/version joins. C-OU-GEOMETRY has zero verified prospective cards at this revision; old imports are development evidence. Do not use their outcomes to tune and then claim a prospective test.


## 8. Numerical program


[NUMERICAL_PROGRAM.md](NUMERICAL_PROGRAM.md) controls implementation scope and build status. The user's 17 September implementation request authorizes the audit changes; the later clarification prioritizes implementation within Markdown. Algorithms, input schemas and acceptance tests are therefore supplied in Markdown. No new approval is requested for these authorized changes. Real data fitting, empirical quality approval, calibration and prospective evidence are not fabricated as document-editing milestones.


## 9. Authority and precedence


Current user instructions take precedence. Within the documents: honesty/identity/anti-hindsight invariants; this method and SCORING_AND_VALIDATION; current detailed source/target gates and sport-specific rules; then promoted process controls. Predictions, dated retrospectives, audit snapshots and archived text are evidence, not active instructions. No historic paragraph can reinstate retired caps, the pseudo-trend test, market features or settlement-only eligibility. The active log's top snapshot alone controls queues and next ID. `CURRENT_RULES.md` (2026-09-25(c)) is a derived summary and map. Where it disagrees with the section it cites, the cited section governs and the summary is corrected. `CHANGELOG.md` is history, not instruction.


## 10. Ledger integrity


Exactly one active log accepts new forecasts: PREDICTION_LOG_COMBINED_5.md. Parts 1–4 are closed to new forecasts and accept only evidenced settlement/correction work. Preserve P-372 as reserved/unused and all existing temporary handles and aliases. Fingerprint all mini variants before import, distinguish duplicate storage from distinct views, verify canonical coverage and unchanged issued selections, then archive raw evidence unchanged. Every edit, new source, lesson disposition and validation result is recorded in Markdown. See [implementation ledger](archive/audit_documents_implemented_2026-09-25/AUDIT_IMPLEMENTATION_2026-09-17.md) for this revision's changes and limits.


<!-- ALL-SPORTS-AUDIT-RECONCILIATION-2026-09-21-CR2 -->
## 11. Historical-audit reconciliation gate — CR-2026.09.21-2


Before an older audit finding is used prospectively, classify it against [`archive/audit_documents_implemented_2026-09-25/AUDIT_RECONCILIATION_ALL_SPORTS_2026-09-21.md`](archive/audit_documents_implemented_2026-09-25/AUDIT_RECONCILIATION_ALL_SPORTS_2026-09-21.md) and, for findings from 2026-09-22 onward, the successor [`archive/audit_documents_implemented_2026-09-25/AUDIT_CLOSURE_LEDGER_2026-09-25.md`](archive/audit_documents_implemented_2026-09-25/AUDIT_CLOSURE_LEDGER_2026-09-25.md) as **ACTIVE/RETAINED**, **ALREADY IMPLEMENTED/DUPLICATE**, **SUPERSEDED/NARROWED**, **REJECTED/INCORRECT**, or **EMPIRICAL WORK REQUIRED**. The later document does not win merely because it is later; the recorded evidence and explicit supersession do.


Operational consequences:


- **REJECTED/INCORRECT** findings never enter a forecast, source rule, scorecard or retrospective adjustment.
- **SUPERSEDED/NARROWED** findings are read only for provenance; the later controlling formulation is used.
- **DUPLICATE** findings are not re-added as a second rule or double-counted as a second mechanism.
- **EMPIRICAL WORK REQUIRED** findings remain pending until the stated dataset/test exists; prose cannot mark them complete.
- Historical cards/audits are evidence, not active authority. They cannot reinstate withdrawn probability ceilings, normalized-edge ordering, `UNORDERED` escape hatches, rebound/hangover rules, market/fantasy evidence, guaranteed venue-history availability or any single-game coefficient.


This reconciliation changes control precedence, not the forecasting model; MDS remains **MDS-2026.09.19-v4.3**.




<!-- ALL-SPORTS-LIVE-RULE-CLEANUP-METHOD-2026-09-21-CR3 -->
## 12. CR-3 live-rule and queue synchronization


The CR-2 audit ledger remains the historical supersession map. CR-3 is a read-back implementation correction: it removes residual active uses of the old order-statistic tail budget, path-count/category ranking shortcuts, universal 40–60% separation floor and blanket `DISJOINT` top-half ban; closes their obsolete prospective-test definitions; synchronizes all ten sport modules; and aligns the executable preflight control revision.


Current forecasting construction is **distribution first, contract query second**. One coherent sport-native joint event distribution/branch mixture generates totals, phase totals, margins/cushions and winner queries. Descriptive base rates, rank-gap labels and dependence classifications do not mechanically force an ordinal. Without a fitted/calibrated numerical distribution, numerical probabilities are permitted **only** as `UNVALIDATED_SUBJECTIVE` outputs of a complete, reproducible, declared distribution (§5). A number that cannot be reproduced from the printed distribution is invented precision and is not permitted. No such number supports a performance, calibration or value claim. *(Corrected 2026-09-25: the previous sentence, "keep numerical probabilities unquantified", contradicted §5; this resolves item 5 of the 2026-09-23 read-only audit.)*


Ledger custody is also synchronized: Part 4 is closed at P-481; Part 5 is the active queue/next-ID authority, with P-482 the rollover next ID. Current log material remains **LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE**.