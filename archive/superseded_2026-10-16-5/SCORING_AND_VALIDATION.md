# Scoring and validation

**Persistent research and corroboration (EXH-v1).** Apply [RESEARCH_EXHAUSTIVENESS_PROTOCOL](RESEARCH_EXHAUSTIVENESS_PROTOCOL.md) to every required field in research, logging, settlement and verification. If a source is incomplete, open alternatives and verify material facts with another independent source; track every remaining field and attempt. Unresolved facts/corroboration never qualify as complete information. New settlements use mini-settlement-9 with a visible source-discovery/reuse section, three source/attempt/closure CSVs and S17; older originals retain their rules and bytes. Consult [RESEARCH_SOURCE_REGISTER](RESEARCH_SOURCE_REGISTER.md) and prior package registers, recheck actual coverage, and continue discovery beyond them.

**SCV-2026.10.16-v11.** New views use these definitions; historical published scores remain unchanged and labelled by their original version ([v6](archive/superseded_2026-10-12/SCORING_AND_VALIDATION.md)). [CURRENT_RULES](CURRENT_RULES.md) controls claims. Fitted experimental primary models are available through PRIMARY_PREDICTION_PROTOCOL; no model is predictive-performance certified. v8 separates pre-start input quality from actual issue phase with no fixed lead deadline; prior v7 added request coverage (§1), evidence-stratified views (§2a), shadow scoring for SHADOW_RANK_DELTA and SHADOW_BASE_ONLY (§6), and deterministic revision resolution in the scoreboard (§7).

## 1. Units, probability and coverage

**Research retention before model availability (RETAIN-v1).** [RESEARCH_RETENTION_PROTOCOL](RESEARCH_RETENTION_PROTOCOL.md) supersedes EXEC-v1's model prerequisite for recording/import. Write every identified researched event under its reconciled working P-ID and canonically retain it through verified import even if the model/adapter/runtime/module/baseline/calibration/receipt is absent or failed. Use RESEARCH_ONLY_NO_MODEL, explicit execution reason and blank nonexistent artifact paths; keep model p_card NOT_ESTIMATED and supported analyst_p NOT_PRIMARY. Missing ML never by itself blocks the ID or a source-backed settlement. Retain verified settled labels for future model development with source/known-at/revision/feature status; only actual frozen experts can supply Hedge losses. Never invent probabilities, execution, final scores or pregame timing. Identity/custody/write conflicts remain real blockers.

SCV-v11 adds explicit research-only retention and future-label coverage, without changing score formulas. Count RESEARCH_ONLY_NO_MODEL in retained research records; exclude its analyst_p/absent model probabilities from model T2, Brier, calibration and prospective cohorts. Preserve historical manual cohorts under their actual original policies. A settled event can provide a future training target even when no original forecast exists.

An event is the basic unit; propositions within it are dependent. Freeze original p_card, baseline p, rank, line, contract, method and issue/cutoff before result. Keep zero distinct from missing. q is never an event probability.

Unconditional W+P+L+V=1; p_card=W/(W+L) scores only decisive W/L outcomes on the identical convention. It does not evaluate push/void probability. Where all masses were issued and action is well-defined, separately report a categorical score over the full outcome space. Do not mix it with binary scores.

For every view report event and row inventory, W/L/PUSH/VOID/UNRESOLVED, exclusions with reasons, numeric probability coverage, paired-baseline coverage and evidence mix. NO_FORECAST and qualitative cards remain in research coverage.

**Request coverage (R22).** Count from each mini's intake table (mini-log-7 onward). Report, and reconcile so that they sum:
- requests received and unique events requested;
- retained cards: numeric, qualitative, NO_FORECAST;
- requests that never became a card: BLOCKED, DUPLICATE_OF_EXISTING_ID, OUT_OF_SCOPE or READ_ONLY_DRAFT, each with its count;
- pending.

For minis before mini-log-7, request coverage is `NOT_COMPUTABLE`. Never assume that every request became a card. Publish unresolved-case sensitivity: for W wins, L losses and U unresolved potentially decisive rows, bounds W/(W+L+U) to (W+U)/(W+L+U), explicitly conditional on those U later proving decisive. If no denominator, report N/A rather than 0%.

## 2. Counting and cohorts

Only original Ranks 1–2 enter primary wins. Rate = W/(W+L); PUSH/VOID excluded with counts, UNRESOLVED visible. Report each rank separately. Ranks 3–4, shadow gate/pairs, reforecasts and historical reconstructions have separate tables and never offset primary losses.

Card class over top-two slots: ALL_WON, SPLIT or ALL_LOST only when both slots are decisive; ONE_DECISIVE when only one is W/L and the other is PUSH/VOID or no second pick; NO_DECISIVE for no W/L and no unresolved; PARTIAL_UNRESOLVED whenever either issued primary row remains unresolved. Preserve old TOP2 labels as historical, not silently recoded grades.

Hit@2 = at least one primary WIN among cards with at least one decisive row and no unresolved primary row, divided by that fully resolved eligible-card count. Report excluded unresolved/no-decisive cards. Both-loss frequency uses only cards with two decisive primary rows. If joint masses are unconditional and pushes/voids can occur, compare like-for-like unconditional joint outcomes on fully resolved cards or use a computed conditional joint given both decisive. Never compare unlike denominators. MECHANICALLY_PROTECTED pairs are reported separately.

Cohorts cross-classify policy/version, league/format/endpoint/family, numeric versus qualitative, actual issue phase, input evidence quality, original gate PASS/RANK1_UNSTABLE/UNKNOWN_GATE/legacy recorded rule, evidence and supplied/derived status. Under [TIMING_RESEARCH_PROTOCOL](TIMING_RESEARCH_PROTOCOL.md), verified PREGAME issuance has no minimum scheduled lead: even an issue immediately before actual start qualifies if not-started evidence is valid. CLEAN_PRE_START_INPUTS / POST_START_ISSUE may contribute to its own research T2/proper-score cohort after comprehensive research, but is never pooled with clean pre-start-issued prospective cards or used to meet an old experiment timing criterion. Lead minutes remain descriptive, not a freeze deadline or quality gate. TIMING_UNVERIFIED/KNOWN_AT_UNVERIFIED and LIVE_OBSERVED/HISTORICAL_DIAGNOSTIC remain separate. Do not infer old timing, gate PASS or model admission; preserve all historical labels and experiment definitions.

## 2a. Evidence-stratified views (R23)

- **Headline view:** only rows graded on evidence A or B, with definition status OPERATOR_VERIFIED or FROZEN_FRAMEWORK_CONVENTION.
- **Sensitivity view:** adds rows graded on C (provisional single-source) and on E (an invariant bound). Report both views side by side, with the count of rows that each added class contributes.
- **Excluded:** rows graded on X are UNRESOLVED and appear only in the §1 unresolved-case bounds.

A provisional C grade never silently becomes A or B. An upgrade is a new settlement revision with the new evidence. Sporting evidence grade, operator definition status and performance eligibility are three separate columns in every row inventory. When the evidence mix changes between two cohorts, print it beside any comparison of them.

## 3. Proper scores and expected score

Binary Brier=(p−y)^2; log loss=−ln(p) if y=1, otherwise −ln(1−p). Wrong literal 0/1 gives infinite log loss; no hidden clipping. Half-sum multiclass Brier=0.5×sum((p_k−y_k)^2), labelled with this scaling. Missing original p means NOT_COMPUTABLE.

For same-row baseline: d_Brier=Brier(card)−Brier(baseline); negative favours the card. Also retain paired log-loss difference when finite. Report paired counts and all exclusions. Brier skill=1−mean Brier(card)/mean Brier(baseline) only on identical rows, with positive baseline denominator. A zero denominator yields UNDEFINED, not perfect skill. A realised in-sample climatology b(1−b) is a retrospective descriptive reference, not an independent pregame baseline.

Expected-score error=observed−issued mean; z=error/issued SD only if SD>0 and endpoint/unit match. Report n, mean error, MAE, RMSE, interval coverage when predictive intervals were issued, and z summaries by sport/term. No SD or no issued mean stays missing. A mean score is not a modal exact-score prediction; absence of large z values does not establish calibrated tails.

## 4. Calibration diagnostics

Use predeclared complete bins covering [0,1], e.g. [0,.1), …, [.9,1], and retain empty bins. Report each bin's rows, distinct events, mean p, realised rate and descriptive uncertainty. Keep ranks, policy and endpoints distinguishable. A wide interval containing the stated probability or calibration slope 1 does not prove calibration; equivalence needs predeclared tolerances and sufficient precision. Do not fit and assess a calibrator on the same outcomes.

Calibration, discrimination and incremental predictive skill are different. A constant 85% on easy propositions can be well calibrated without useful event-specific information. Evaluate baseline-relative scores on identical lines as well as selection coverage.

## 5. Comparisons and uncertainty

Freeze cohort dates/inclusion, candidate and baseline versions, primary endpoint, minimum meaningful effect, analysis unit, missingness, sample-size justification and stopping rule before collecting future results. Original RET/XCARD registrations remain readable; amendments get new IDs and prospective start times.

Average paired row differences within each event first (predeclared rank weighting; default equal across available paired primary rows, report partial pairs), then within ISO week. Report event-weighted descriptive mean and equal-week mean separately. For k week means with sample SD s, an approximate interval is mean ± t_(k−1,.975)×s/sqrt(k), with the t value/source or arithmetic shown. k<8 is INSUFFICIENT_EVIDENCE under this framework; eight weeks is only a minimum, not a power guarantee. Strong serial/team dependence or heterogeneity limits this approximation and blocks a strong claim without a justified block analysis. Do not invent a bootstrap or power calculation that was not performed.

Wilson intervals may be shown for single-slot/card proportions with n and formula: centre=(p+z²/(2n))/(1+z²/n); half-width=z*sqrt(p(1−p)/n+z²/(4n²))/(1+z²/n), z=1.96. Pooled-row intervals ignore within-event dependence and are labelled descriptive; they do not establish promotion. No claim that their direction of error is always the same.

Acceptance requires the pre-registered meaningful improvement and precision, no material calibration/coverage degradation, and all evidence controls. Multiple sports/families/tests are exploratory unless multiplicity and selection were planned. No sample-size-needed number without stated effect, variance/dependence, alpha, power and method. Otherwise SAMPLE_SIZE_NOT_ESTIMATED. No acceptance merely because a CI contains zero/one or because mean |z| sits in an arbitrary band.

## 6. Ranking and joint diagnostics

Wins@2 counts original primary wins. NDCG@2 is optional and descriptive: for fully decisive four-row slates, DCG=rel1+rel2/log2(3); IDCG is 1 for one winner among all four, 1+1/log2(3) for two or more; no winners gives N/A. Partial/push/void/unresolved/fewer-row slates stay unscored for this legacy metric. Never count alternate or shadow wins as primary.

Compare exact predicted joints to matching observed events; bounds stay bounds. Zero joint failure from disjoint losses is a mathematical property, not measured forecasting success. Quantity labels alone do not prove independence. Ranking separation needs paired event-level evidence; a reversed empirical slot rate on 20 cards is a diagnostic, not conclusive failure.

**Shadows added in v7.** Each is scored on its own frozen rows, with the same proper scores and against the same frozen BASELINE_P, and is never mixed into primary counts.
- `SHADOW_RANK_DELTA`: its top two, scored like primary rows. Report the paired difference against the primary top two on the same events.
- `SHADOW_BASE_ONLY`: each row's `p_base` against the outcome, paired with the mixture p_card on the same row (experiment FC11-MIX-v1).

The form-window blend is an adjustment, not a shadow. Its effect is read from the card's adjusted and unadjusted expected scores (experiment FC11-FORM-v1).

## 7. Scoreboard procedure

Build a row-level inventory from original cards joined to their **effective** settlement per contract key. That is the latest revision on the single unbroken parent chain (CURRENT_RULES §8), not the last block in a file. Keys in a `REVISION_CONFLICT` count as UNRESOLVED. Retain prior revisions and supersession reasons, and count each contract once. Reconcile every included ID and aggregate count, then independently recompute representative arithmetic. Do not backfill missing card p from a summary or q.

Headline: paired baseline-relative proper scores, number of paired events/weeks and uncertainty/status. If unavailable, say NOT_COMPUTABLE. Show hit rates, timing, gate, evidence mix, unresolved coverage and expected-score diagnostics alongside. Preserve historical snapshots; begin v10 at its first actual card, with zero events until one exists. Update CURRENT_STATE's current summary without changing log grades. Existing historical denominators require a separate labelled reconciliation if definitions differ.

## 8. Historical evidence and release

Historical learning logs, revised datasets and post-event counterfactuals cannot establish prospective skill. An omitted probability, cutoff or baseline is not restored by a later interpretation. Every recommendation is tracked as document implementation, data readiness, test registration, observed experiment result and release decision separately. Certification remains suspended.

## 9. Completion-based research policy (SCV-v8)

T2 retains every original primary result in its declared policy/timing cohort; a post-start issue is not excluded from research logging solely for lateness. CLEAN_PRE_START_INPUTS requires the timing protocol's independent field-known-at and outcome-exposure checks. Report pre-start-issued, clean-pre-start-input/post-start-issued, unverified and outcome-exposed counts separately, plus unchanged legacy cohorts. Record baseline construction/issue time too: an outcome-blind comparator made after start remains in the same late-issued lane, not a pre-start-frozen prospective baseline. No missing baseline, issue time, source receipt or historical probability is reconstructed. Existing preregistered prospective/model release gates remain unchanged; no predictive benefit is claimed for removing deadlines.

## 10. Historical V1 model-assisted primary cohort (SCV-v9)

[PRIMARY_PREDICTION_PROTOCOL](PRIMARY_PREDICTION_PROTOCOL.md) authorises MODEL_ASSISTED_PRIMARY_V1. Its actual issued top two count in their own T2 cohort; do not relabel historical manual cards, add comparator/shadow wins or pool assisted with independent manual evidence. Preserve selected model/action probability/context/recipe and whole-grid hashes. Sporting reward=1 minus mean original decisive-primary Brier; all-push/void/unknown gives no update. Feedback must follow final and available-at, with one effective original bundle/settlement chain per event. Primary use is explicitly experimental; no old DATA_HOLD or model/operational certification is silently upgraded. New prospective acceptance/design remains unregistered/BLOCKED_DESIGN until separately frozen; tests or synthetic demos prove no advantage.

## 11. Mixture integrity cohort (SCV-v10)

MODEL_ASSISTED_PRIMARY_V3 / PRIMARY_HEDGE_MIX_V3 retains original primary top-two scores in its own policy/timing cohort. Full-information learning scores every expert on frozen common questions: home-win and league-line total binary Brier, total only for cricket. Primary pushes leave top-two Brier NOT_COMPUTED; fully evidenced common questions can still train expert weights. Warm fits use only labels available at that simulated refit, and verified issued feedback replaces the overlapping warm event, never adds a second observation. Retain both learning ledgers and parameter admission/default status. This is online aggregation, not evidence of a trained RL agent. Historical V1/V2 cards retain their original policy; do not pool cohorts or count comparator wins. Legacy §10's selected-arm/top-two reward describes the old V1 policy only.

The old replay's pooled competition-week interval is not an accepted V3 performance result. Future pooled analyses namespace event IDs and cluster common calendar weeks across competitions; DATA_HOLD leagues remain diagnostic, outside the admitted pool. Even this correction does not establish independence across weeks, source truth, prospective skill or qualification.
