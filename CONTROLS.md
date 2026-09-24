# Controls — current compact reference


Revision **CR-2026.09.21-3**, METHOD **MDS-2026.09.19-v4.3**. SCORING_AND_VALIDATION is the mathematical authority. The six-field METHOD object is the single mandatory output template. Historical controls and origins are preserved in LEARNING_REGISTER and the pre-revision control snapshot (`audit_2026-09-17_implementation/before/CONTROLS_with_margin_band_addition.md`, not present in this repository); their withdrawn statistical claims are not active rules.


| Control | Current requirement | Template field |
|---|---|---|
| G0–G6 | Freeze exact event, contract, period, activation, state and timestamps; blocked or already decided rows do not issue | 1 |
| G8–G10 / G-L13 | Field owner, exact raw source, availability/retrieval time; no synthetic/model-summary settlement | 2 |
| G13.1 | Retrieve L5/L10/L15/L20 and H2H continuity; descriptive overlapping windows, no pseudo-significance test | 2 |
| G14/G15 | Both starters/bench/coaches and role/workload; outdoor venue-hourly environment/current surface; explicit missingness | 2 |
| G-L7 | Open available disaggregated records before aggregate-driven direction; AGGREGATE_ONLY is an evidence grade, not a numerical probability cap | 2 |
| G-L11 | Unique denominators and appropriate uncertainty, no automatic two-SE direction rule | 2, 3 |
| G-L1/G-L9 | Disjoint exhaustive outcome states, coherent complements including push/action, representative scores | 3, 5 |
| G-L2/G-L12 | Declared priors and scenario weights; uncertainty can change mean and variance. No unsupported directional lean, universal zero-shrink prohibition or NFL width floor | 3 |
| G-L8 | Exact PMF/CDF queries at each endpoint; integer push; no universal absolute-normalised-distance ordering | 3, 4 |
| G-L18 | Team allocation and linked phase marginals from the same joint process | 3 |
| G-L19 | Competition-specific terminal states, ties/draws/OT/retirement/censoring | 1, 3 |
| G-L20 | Relevant current-regime comparables enter a declared uncertain model; one observed crossing alone imposes no 0.50 cap or minimum mass | 2, 3 |
| G-L10/G-L17/G-L21 | Joint top-two success/failure and shared-driver all-fail mass, or JOINT_UNQUANTIFIED with valid bounds; driver signs per row | 5 |
| G-L15/G-L22 | FORCED_PAIR/FREE; freeze preferred side; one target decision; event-level weights; correct push-conditioned scoring | 4, 6 |
| G-L14/G-L16 | Verified provider and exact period; a bounded grade requires settlement invariant across all admissible splits | 1, 6 |
| G-L23 | Raw process/disruption record at settlement; separate process, conversion and endpoint effects; inspect wins and losses | 6 |
| G-L24 | Signed-margin joint queries; specified-team conditioning, draw/push masses; no pooled-band substitution or BAND_NOT_DERIVED rank bar | 3, 4 |
| MLB 34/35/37 | No universal −1.5 ceiling, 12% push cap or fixed extras contributions. Tie exactly on L becomes Over conditional on completed action. No extras double-count | 3, 4 |
| Cricket 32 | Activation before outcome; a chase cannot settle an inactive batting-first contract | 1, 6 |
| Source admission | CANDIDATE source status is not numerical feature approval; field/cutoff tests and H0 are required | 2, 6 |
| Eligibility | All existing logs learning-only; no historical import becomes a prospective trial; no model promotion from a short streak | 6 |


<!-- THREE-SOURCE-TIME-GATE-2026-09-19-CR4 -->
## Universal three-source, timezone and final-state controls — CR-2026.09.19-4


These are **blocking cross-sport controls** for every new forecast, late refresh, live-state check and settlement.


- **C-SRC3:** require at least **3 distinct reliable upstream source lineages** for each event. Mirrors, syndication, reposts, search snippets and generated summaries do not create independent lineages.
- **C-SRCMIX:** where available, include a field-owner exact-event source, another official team/club/participant or second primary source, and an independent high-quality secondary source.
- **C-TIME1:** verify venue/host city and country, official venue-local calendar date and time, IANA timezone, exact-date UTC offset, `Australia/Melbourne` converted date/time, correct **AEST/AEDT** label, and calendar-date rollover.
- **C-TIME2:** user-supplied time is estimated metadata until independently verified. Any discrepancy must be printed explicitly before analysis.
- **C-STATE3:** immediately before issue/refresh, verify `SCHEDULED/PREGAME`, `LIVE`, `POSTPONED/CANCELLED`, or terminal state across the qualifying source set. Credible conflict = `EVENT_STATE_CONFLICT` and fail closed.
- **C-FINAL3:** settlement requires at least **3 distinct reliable lineages** agreeing on exact event/date, explicit terminal state and final result. A score without a terminal marker is insufficient. Any credible live/in-progress source blocks settlement. **Receipt requirement (added 2026-09-25; 2026-09-23 read-only audit item 6):** each settlement lineage is recorded with its exact URL or endpoint and event ID, field owner, upstream lineage (data vendor where exposed, e.g. `sportradar_timestamp`), known-at or retrieved-at time, and admissibility (field owner, independent, or discovery-only). **Three hostnames do not certify C-FINAL3.** Syndicated copies, mirrors of one feed and pages built on one data vendor count as one lineage. A lineage whose printed record ID cannot be reproduced does not count (2026-09-24(f): four MLB gamePks and one NHL game ID printed in a settlement were not the real records).
- **C-SNIP:** search-result snippets, generated summaries and headlines are discovery only and cannot establish finality.
- **C-DERIV3:** derivative fields used for grading require three independent providers where three genuinely independent providers exist; otherwise record the source limitation and do not claim three-source verification.
- **C-WRITECHK:** re-check event state immediately before a Drive status transition and read back the written log afterward.
- **Failure labels:** `SOURCE_COUNT_LT_3`, `SOURCE_LINEAGE_NOT_INDEPENDENT`, `EVENT_DATE_NOT_VERIFIED`, `EVENT_LOCAL_TIME_NOT_VERIFIED`, `EVENT_TIMEZONE_NOT_VERIFIED`, `MELBOURNE_TIME_CONVERSION_NOT_VERIFIED`, `EVENT_STATE_CONFLICT`, `FINAL_STATE_NOT_VERIFIED_BY_3_SOURCES`, `DERIVATIVE_SETTLEMENT_FIELD_NOT_VERIFIED_BY_3_SOURCES`.


P-469 is the reference false-final incident demonstrating why these controls are blocking.




<!-- CRICKET-SOURCE-PATCH-2026-09-21-CR1 -->
## Cricket toss/strip source controls — CR-2026.09.21-1


These controls preserve the CR-4 cross-sport gates and add **cricket-specific retrieval/integrity requirements**. They do not create a forecast coefficient or claim predictive lift.


| Control | Class | Requirement / consequence |
|---|---|---|
| **C-CR-TOSS** | `MECHANISM_REQUIRED` | Record `TOSS STATUS` separately from strip/weather. Search the field owner → official/rights-holder video → official team/competition update → admitted structured endpoint → specialist exact-match record → independent reporting. Unknown toss may remain a branch only when the contract/activation logic is valid. |
| **C-CR-STRIP** | `MECHANISM_REQUIRED` | `STRIP STATUS` is `OBSERVED`, `NOT_FOUND_AFTER_SEARCH`, `CONFLICTING`, or `STALE_ONLY`. `OBSERVED` requires a named exact-match current-strip source class from `RULES_CRICKET.md` §2. Previous matches, venue averages and post-match ICC ratings cannot create today's strip. |
| **C-CR-VIDEO/NVPLAY** | `CONTEXT_MATERIALITY` | Query verified board/competition video, rights-holder toss/pitch coverage and sanctioned NV Play/board-branded Match Centre where applicable during the toss window. |
| **C-CR-LINEAGE-FP** | `BLOCKING_INTEGRITY` for independence claims | Identical/near-identical unusual structured pitch blocks across front ends are one suspected upstream lineage until provenance proves otherwise. A transcript and the broadcast it transcribes are one lineage. |
| **C-CR-AUTO-PITCH** | `BLOCKING_INTEGRITY` for strip-observation claims | Unattributed automated pitch metadata is never relabelled as a human current-strip observation and cannot satisfy the exact-strip gate by itself. |
| **C-CR-VENUE-MISS** | `CONTEXT_MATERIALITY` | Same-format venue history may be `INSUFFICIENT_VENUE_HISTORY`. Use a broader labelled prior and wider uncertainty; never fabricate rung/sample completion. |
| **C-CR-STALE-OFFICIAL** | `BLOCKING_INTEGRITY` for the affected volatile field | Official is not synonymous with current. If an official dynamic page is demonstrably stale for state/toss/XI/score, mark that field `STALE` and route to a fresh official/static/sanctioned source plus independent corroboration. |
| **C-CR-REFRESH** | `MECHANISM_REQUIRED` | Re-run toss, XI, strip, radar/weather and event state during the actual toss window and immediately before issue. Start crossing requires state reclassification before delivery. |


`NOT_FOUND_AFTER_SEARCH` is a valid cricket strip outcome only when the required search is shown. Missing strip evidence lowers the evidence grade / widens the distribution; it does not block every forecast and it never licenses an invented surface description.




## Candidate status


C-OU-GEOMETRY: **DESIGN REVISION / ZERO VERIFIED PROSPECTIVE CARDS**. Match sport, endpoint, horizon, baseline difficulty and frozen preferred selection, with full manifest/issue/result-time/version joins. Historical cohort counts remain developmental. Fifty cards/two sports/0.02 Brier are review markers only, not a sufficient promotion rule.


C-RUN-CENTRE-BIAS: **DEVELOPMENT ONLY / NO BIAS COEFFICIENT**. Separate actual predictive means, medians and informal corridor midpoints; split MLB/NPB/KBO/CPBL and endpoint before analysing residuals. Later MLB residuals changed direction, so no universal Under adjustment follows.


C-PHASE-VS-FULL-TOTAL, C-MARGIN-TAIL-MASS, C-PROB-EXTREMITY and C-UNDERDOG-SEPARATION: retain as hypotheses with no ranking effect. Existing cohorts cannot validate changes devised after their outcomes. Apply the scoring and prospective admission rules before any future count is credited. Easier thresholds and multiple correlated rows are not evidence of improved prediction.


## Current evidence and changes


P-344 arithmetic corrected to 0.283425; current legacy aggregate 477 rows at 0.2265475891. P-255/P-256 period-bound WIN claims withdrawn; existing audit handles reopened. Primary queue 23, documentary/period queue 5, next P-452: the active Part-4 snapshot remains the sole state authority. No new coefficient, probability cap, model validation or market-value claim is promoted. See AUDIT_IMPLEMENTATION_2026-09-17 and the unchanged original review evidence.


## 2026-09-19 — `R-1`, `S-1`, `S-2` and the top-over/under review trigger


| Addition | Rule in one line | Home |
|---|---|---|
| **Top-O/U enhanced review** | A loss **or push** on the card's highest-ranked over/under (identified from issue-time ranks) triggers the same deep failure review as a Rank #1 loss; logged as `TOP_OU_REVIEW`. Retrospective scrutiny only — it licenses no hedging, no probability shading and no refusal to rank a total | `METHOD.md` §7; `SCORING_AND_VALIDATION.md` §3; research-guide Step 5 |
| **`R-1`** recency | Recent results are evidence about a **rate**, never a forecast of a **deviation**. No rebound lean, no hangover lean, no "high calibre will correct it". Moving a centre requires a **named mechanism** in the disaggregated record; otherwise recent form widens only | [`RECENCY_AND_REBOUND.md`](RECENCY_AND_REBOUND.md); sport files §"2026-09-19" |
| **`S-1 Rev 2`** accredited beat & media | Beat/team reporting needs accredited identity, explicit date/venue anchor, 2-source corroboration, and verbatim quotation. When official feeds lag, satisfies G14.2 as `PROJECTED_BEAT_VERIFIED` | `SOURCES.md` §"2026-09-24"; `DATA_SOURCE_REGISTER.md` |
| **`S-2`** press conferences | Admissible for availability, workload and role intent (`SECONDARY_ONLY`); **never** a signed adjustment to pace, efficiency or scoring rate | same |
| **`NOT_YET_PUBLISHED`** | A structured line-up query returning empty is a verified availability state, not a `RETRIEVAL_MISS` process defect. Record the query time | `SOURCES.md` §"2026-09-19"; §16.8 field 7 |
| **Debutant gates** | MLB `mlbDebutDate` → `LOW_SERVICE_SAMPLE`; ESPN cricket `debuts[]` → `NO_PRIOR_FORMAT_RECORD`; soccer `NO_COMPETITION_SAMPLE`. A debutant contributes width, never an assumed contribution | `RULES_BASEBALL.md`, `RULES_CRICKET.md`, `RULES_SOCCER.md` |


**Evidence base for `R-1`** (MLB 2026, 4,594 team-games / 108 starters / 2,244 out-of-sample predictions): rebound after a 0-run game **−0.102** runs [−0.456, +0.251]; top-10 offences after ≤2 runs **−0.126**; starter next-start ER after ≥6 ER **−0.017**, strikeouts **−0.070**; lag-1 autocorrelation +0.019 (team) and −0.037 (starter); recency RMSE last-1 **2.7677** > last-3 **2.2433** > last-5 **2.1324** > season **2.0177** > league constant **1.9844**. Empirical estimates on one season of one competition — not identities, not universal bounds, not fitted coefficients (`L-087`).


## 2026-09-19(b) — active-control classification (resolves the `L-095` deferral) and control revision CR-2026.09.19-1


**Why this exists.** `L-095` (2026-09-06) created a three-class control taxonomy and deferred tagging the ~86 lesson rows that predated it. That backlog has sat open ever since, and `L-096` — the control-effectiveness review — cannot run without it. The deferral is resolved here by **correcting the unit**: `L-096` needs *controls* classified by consequence-of-failure, not historical *lesson rows* tagged. `METHOD.md` §9 is explicit that dated retrospectives and archived text are evidence, not active instructions, and `METHOD.md` §4 has since superseded the taxonomy's forward function. Retro-tagging the 86 historical rows is therefore **closed as not-to-be-done**, with the reasoning recorded, rather than carried indefinitely. Full disposition: [`archive/audit_documents_implemented_2026-09-25/AUDIT_IMPLEMENTATION_2026-09-19.md`](archive/audit_documents_implemented_2026-09-25/AUDIT_IMPLEMENTATION_2026-09-19.md) §4.


**Classes**, aligned to `METHOD.md` §4's split:


- **`BLOCKING_INTEGRITY`** — identity, contract, event state, source admissibility, arithmetic coherence. Failure means **no issuance**.
- **`MECHANISM_REQUIRED`** — a required analytical step. Omission is a process defect and caps the evidence grade at `FORCED RANK / LOW`; it is **not** a numerical cap on a derived probability.
- **`CONTEXT_MATERIALITY`** — a contextual factor that must be considered; absence lowers evidence grade only.


| Control | Class | Failure consequence |
|---|---|---|
| `G0`–`G6` identity, contract, target, endpoint, activation, terminal states | `BLOCKING_INTEGRITY` | no issuance |
| Synthetic/simulated-source exclusion (`L-079`) | `BLOCKING_INTEGRITY` | no issuance |
| Event-state / start-crossing gate | `BLOCKING_INTEGRITY` | no issuance; fail closed |
| Sport onboarding gates (`BK-P1`, `AF-P1`, competition-rules packet) | `BLOCKING_INTEGRITY` | no issuance |
| `G-L13` raw-record verification | `BLOCKING_INTEGRITY` | claim is `SUMMARY_ONLY`, unusable as a settled field |
| `G-L16` period-scope match | `BLOCKING_INTEGRITY` | settlement invalid |
| `G-L19` terminal end-state family | `BLOCKING_INTEGRITY` | winner label structurally invalid |
| `G-L1` outcome-state families with mass | `MECHANISM_REQUIRED` | process defect; evidence grade capped |
| `G-L8` distribution → exact contract masses | `MECHANISM_REQUIRED` | same |
| `G-L9` complement decomposition | `MECHANISM_REQUIRED` | same |
| `G-L10` / `G-L17` / `G-L21` joint win, joint failure, card-level failure mass and sign check | `MECHANISM_REQUIRED` | same; `JOINT_UNQUANTIFIED` with valid bounds is honest completion |
| `G-L12` / `G-L24` margin width and handicap queries from the joint model | `MECHANISM_REQUIRED` | same; no universal bound follows |
| `G-L18` allocation marginals | `MECHANISM_REQUIRED` | same |
| `G-L22` forced-pair labelling and one-decision counting | `MECHANISM_REQUIRED` | measurement defect |
| `G-L7` disaggregated record before an aggregate carries direction | `MECHANISM_REQUIRED` | same |
| `G-L11` real numerators before a small-sample rate takes a signed adjustment | `MECHANISM_REQUIRED` | same |
| **`R-1`** recency: rate-revision via named mechanism, never deviation-forecast | `MECHANISM_REQUIRED` | unsupported signed adjustment; centre must revert to the longer-window rate |
| `G-L14` settlement route printed and verified | `MECHANISM_REQUIRED` | row may become unsettleable |
| `G-L23` process record and disruption facts before amending a control | `MECHANISM_REQUIRED` | control may not be amended |
| `G14.2` participants: starters, bench, coaches | `MECHANISM_REQUIRED` | evidence cap; `BENCH_NOT_RETRIEVED` blocks a margin/full-game total from Rank #1 |
| **`S-1 Rev 2`** beat & team media gate | `MECHANISM_REQUIRED` | uncorroborated claim stays `SECONDARY_ONLY`; accredited 2-source beat report lifts to `PROJECTED_BEAT_VERIFIED` . **2026-09-24(f):** the printed receipt is mandatory, and an official lineup published before the freeze outranks it |
| **`S-2`** press-conference material | `CONTEXT_MATERIALITY` | admissible for availability/role only; never a signed rate adjustment |
| `G15.1` environment / venue-coordinate forecast | `CONTEXT_MATERIALITY` | evidence cap (outdoor events) |
| `G13.1` descriptive recency windows, `G17.1` streak audit | `CONTEXT_MATERIALITY` | descriptive display only — **not** a trend test (withdrawn 2026-09-17) |
| `G-L20` direct current-regime comparable | `CONTEXT_MATERIALITY` | mass must be sized to its `n`; a single comparable is the weakest predictor measured (`R-1` §4) |
| Debutant gates (`LOW_SERVICE_SAMPLE`, `NO_PRIOR_FORMAT_RECORD`, `NO_COMPETITION_SAMPLE`) | `CONTEXT_MATERIALITY` | contributes width; no assumed contribution |
| `TOP_OU_REVIEW` trigger | *retrospective duty* | not a forecast-time control; it governs settlement scrutiny only |


`L-096` is now executable: for any `BLOCKING_INTEGRITY` or `MECHANISM_REQUIRED` control, compare the recurrence rate of its target defect before and after its effective date. A control whose target defect recurs at a similar rate post-adoption indicates an **execution** problem, not a wording problem — and per `L-096` the response is compliance discipline, not a fourth restatement of the rule.


### Control revision CR-2026.09.19-1


The control set changed on 2026-09-19 (`METHOD.md` §7, `SCORING_AND_VALIDATION.md` §3, this file, `SOURCES.md`, `DATA_SOURCE_REGISTER.md`, all ten `RULES_*.md`, and the new `RECENCY_AND_REBOUND.md`). The revision ID therefore advances from `CR-2026.09.17-1`.


**Manifest: 24 files** — the 23 in the previous manifest plus `RECENCY_AND_REBOUND.md`, which is control-class and must be covered. `audit_2026-09-17_implementation/VALIDATION.md` was corrected in the same pass so its manifest includes that file and its emitted revision label is **read live from `METHOD.md`** rather than hardcoded. **The authoritative revision ID is the one in `METHOD.md`.** **The hash value itself is deliberately NOT recorded in this file.** `CONTROLS.md` is inside the manifest, so writing the hash here would change the bytes being hashed and invalidate the value as it is written — a self-reference loop. The authoritative value lives in [`archive/audit_documents_implemented_2026-09-25/AUDIT_IMPLEMENTATION_2026-09-19.md`](archive/audit_documents_implemented_2026-09-25/AUDIT_IMPLEMENTATION_2026-09-19.md) §7 and in `audit_2026-09-17_implementation/RESULTS.md`, **both of which are outside the manifest**. Never record a manifest hash inside a manifest file.


Recompute before freezing onto a card:


```python
import hashlib, json
from pathlib import Path
root = Path('.')
names = ['METHOD.md','SCORING_AND_VALIDATION.md','CONTROLS.md','RULES_GENERAL.md',
         'RECENCY_AND_REBOUND.md','MODEL_IMPLEMENTATION_RECIPES.md','NUMERICAL_PROGRAM.md',
         'NUMERICAL_TRAINING_SPEC.md','NUMERICAL_MODEL_REGISTER.md','MODEL_AND_DATA_SPEC.md',
         'H0_DATASET_CARD.md','SOURCES.md','DATA_SOURCE_REGISTER.md','BASE_RATES_REGISTER.md'] \
        + sorted(p.name for p in root.glob('RULES_*.md') if p.name != 'RULES_GENERAL.md')
h = {n: hashlib.sha256((root/n).read_bytes()).hexdigest() for n in names}
print(len(h), hashlib.sha256(json.dumps(h, sort_keys=True, separators=(',',':')).encode()).hexdigest())
```


If the bytes have changed since the value recorded in [`archive/audit_documents_implemented_2026-09-25/AUDIT_IMPLEMENTATION_2026-09-19.md`](archive/audit_documents_implemented_2026-09-25/AUDIT_IMPLEMENTATION_2026-09-19.md), **open a new revision ID** rather than reusing this one. A hash is a byte receipt, not timestamp evidence.


<!-- DEEP-RESEARCH-IMPLEMENTATION-2026-09-19-V42 -->
## 2026-09-19(c) — deep-research hard gates


| Control | Class | Requirement / failure consequence |
|---|---|---|
| **PF-1 SOURCE-FIREWALL** | `BLOCKING_INTEGRITY` | Reject sportsbook/bookmaker/odds/tipster/picks/prediction-market/fantasy/DFS evidence and any secondary analysis derived from it. Explicitly reject RotoWire, RotoGrinders and FPTrack. Discovery-only use must terminate at a valid upstream source before the fact enters evidence. |
| **PF-2 LINE-QUARANTINE** | `BLOCKING_INTEGRITY` | Supplied totals/spreads/alternate lines are contract metadata only and cannot enter features, priors, model inputs, scenario weights, calibration or narrative direction before the independent distribution is frozen. |
| **PF-3 KNOWN-AT** | `BLOCKING_INTEGRITY` | Every predictive fact must satisfy `first_known_at <= cutoff_at`. Revised box scores, final labels and postgame reporting cannot backfill issue-time features. |
| **PF-4 FRESHNESS** | `BLOCKING_INTEGRITY` for critical dynamic state | Lineups/starting participants/availability/surface/weather and other dynamic critical state must be current to the source's update cadence and refreshed before issue; stale or superseded state blocks normal issuance. |
| **PF-5 LINEAGE** | `BLOCKING_INTEGRITY` | Each material source needs an upstream lineage. Multiple branded mirrors of one feed count once. Unknown lineage is not independent corroboration. |
| **PF-6 CRITICAL-SOURCE DIVERSITY** | `BLOCKING_INTEGRITY` | A critical fact is satisfied by its direct field owner, or (when no field-owner route exists) by at least two genuinely independent valid lineages. Otherwise mark unresolved; do not manufacture certainty. |
| **PF-7 VERSION-MANIFEST** | `BLOCKING_INTEGRITY` | Card method/control versions must equal the live authority; mismatch fails closed. Historical cards keep their original version. |
| **PF-8 RAW/FEATURE/FORECAST SEPARATION** | `MECHANISM_REQUIRED` | Preserve separate raw facts, feature transforms, model/scenario parameters, predictive distribution and post-forecast contract query. No blended prose-only arithmetic. |
| **PF-9 NO-AD-HOC-CENTRE** | `MECHANISM_REQUIRED` | Signed centre adjustments require an estimated/frozen coefficient or an explicit sourced scenario mixture. Arbitrary +/− run/point/goal adjustments are prohibited. |
| **PF-10 DISTRIBUTION-FIRST** | `MECHANISM_REQUIRED` | Totals and lines are queries against one coherent event distribution. Separate independently invented probabilities for adjacent lines or opposite sides are invalid. |
| **PF-11 TEST-INTEGRITY** | `BLOCKING_INTEGRITY` for model promotion | TRAIN/TUNE/CAL/TEST are chronological and event-grouped; transforms are fit inside the training fold; TEST is opened once; OOF-only ensemble/calibration inputs. |
| **PF-12 PERFORMANCE-CLAIM** | `BLOCKING_INTEGRITY` | Documentation, synthetic tests or a short hit-rate streak cannot be described as predictive improvement. Promotion requires frozen out-of-sample evidence and then prospective shadow evidence for the exact scope. |


`prediction_preflight.py` is the executable implementation of PF-1 through PF-7 plus core provenance/coherence checks. `audit_card_controls.py` remains the printed-card completeness audit; the two scripts serve different purposes.


## 2026-09-19(d) — CR-2026.09.19-3 implementation/read-back closure


CR-3 synchronizes active headers and executable controls to the already-governing **MDS-2026.09.19-v4.2 / NTS-2026.09.19-v0.5** state, removes stale hard-coded queue/ID text, and regenerates the control receipt after read-back. It does not introduce a new predictive feature, distribution family, probability adjustment or performance claim. The PF-1–PF-12 gates and the CR-2 forecasting semantics remain unchanged.


<!-- ALL-SPORTS-AUDIT-RECONCILIATION-2026-09-21-CR2 -->
## Audit-precedence control — CR-2026.09.21-2


`A-REC-1` is a blocking governance check before an historical audit finding changes current analysis. Resolve the finding through `archive/audit_documents_implemented_2026-09-25/AUDIT_RECONCILIATION_ALL_SPORTS_2026-09-21.md`.


| State | Required action |
|---|---|
| `ACTIVE_RETAINED` | Apply the current controlling formulation once. |
| `DUPLICATE_ALREADY_IMPLEMENTED` | Do not add another copy or second weight. |
| `SUPERSEDED_NARROWED` | Apply only the documented successor. |
| `REJECTED_INCORRECT` | Exclude from current analysis; retain only as provenance. |
| `EMPIRICAL_WORK_REQUIRED` | Leave pending until the stated dataset/test is completed; never promote by documentation. |


The canonical cross-audit survivors are: event/time/state verification; source-lineage independence; point-in-time `known_at`; betting/fantasy source firewall; supplied-line quarantine; current participants/roles; disaggregated evidence; one sport-native joint distribution; exact push/void/censoring arithmetic; no automatic rebound/hangover/due effect; one-result anti-overfit; enhanced Rank-1/top-O/U failure review; and three-lineage terminal settlement.




<!-- ALL-SPORTS-LIVE-RULE-CONTROLS-2026-09-21-CR3 -->
## CR-2026.09.21-3 live-rule drift closure


| Control | Class | Current requirement |
|---|---|---|
| **A-REC-2 LIVE-RULE READ-BACK** | `BLOCKING_INTEGRITY` | After audit reconciliation, search active rule files for superseded formulations. A prose supersession ledger is not sufficient if stale live gate text still contradicts it. |
| **PF-13 DISTRIBUTIONAL-TAIL** | `MECHANISM_REQUIRED` | Tail stress comes from the same frozen sport-native joint distribution/branch mixture. Historical second-highest+median / second-lowest+median pseudo-tail sums are non-operative. |
| **PF-14 NO UNIVERSAL SEPARATION FLOOR** | `MECHANISM_REQUIRED` | No 40–60% or other pooled band mechanically blocks Rank #1. Reference rates and rank-gap labels are descriptive; exact marginal likelihood and robustness govern ordering. |
| **PF-15 DISJOINT NUANCE** | `MECHANISM_REQUIRED` | `DISJOINT` forces repair only when it exposes an impossible/incoherent construction. Mutually exclusive but coherent high-probability marginals may still rank highly. |
| **PF-16 OBSOLETE-CANDIDATE CLOSURE** | `BLOCKING_INTEGRITY` | `C-TAIL-BUDGET-v1`, `C-PATH-GEOMETRY-v1` and the old `C-SEPARATION-FLOOR` definition are CLOSED/SUPERSEDED. Any future test needs a new ID/version and a distribution-first preregistration. |
| **LEDGER-5** | `BLOCKING_INTEGRITY` | Part 4 is closed at P-481. `PREDICTION_LOG_COMBINED_5.md` / `GAME_LOG_STATUS_CURRENT.md` controls the active queue and next ID (P-482 at rollover). |


These controls correct implementation drift only. They add no fitted coefficient, probability cap, rank bonus/penalty or performance claim.


<!-- AUDIT-2026-09-24F -->
## 2026-09-24(f) — settlement-integrity controls (from the audit of the P-495–P-508 import)

Home: `RULES_GENERAL.md` §"2026-09-24(f)". Evidence: `PREDICTION_LOG_COMBINED_5.md` §"2026-09-24(f)". The control revision label is unchanged (`CR-2026.09.21-3`); these are additive integrity, measurement and retrieval controls with no forecasting effect.

| Control | Rule in one line | Class | Failure consequence |
|---|---|---|---|
| **`C-PROCESS-RECORD-PROVENANCE`** | Every settlement process fact carries the endpoint or URL and the retrieval time it was read from, or is marked `UNSOURCED`. A causal narrative on unsourced facts is `PROCESS_RECORD_UNVERIFIED` | `BLOCKING_INTEGRITY` (settlement) | No rule, weight or disposition may cite the block |
| **`C-LINEUP-DIFF`** | At settlement, print the card's named starters, starting pitcher or goalie against the official box, as "k of n started" per side. A Rank-1 driver who did not play means `PROCESS_DEFECT: LINEUP_CLAIM_FALSE` | `MECHANISM_REQUIRED` (settlement) | The defect is recorded whatever the result |
| **`S-1 Rev 2` receipt enforcement** | `PROJECTED_BEAT_VERIFIED` counts only with a printed receipt: outlet, reporter, timestamp, verbatim quote, two sources. An official lineup published before the freeze outranks it: `CONFIRMED_OFFICIAL` or `RETRIEVAL_MISS` | `MECHANISM_REQUIRED` (issue) | Without the receipt: `NOT_RETRIEVED`, and G14.2's Rank-1 block applies |
| **`G-L22(c) COVERING_PAIR`** | Two rows whose union covers every outcome (opposite +1.5 in MLB; ML plus the opponent's +1.5) are labelled. Hit@2 is mechanical and is excluded from top-two summaries | measurement | Measurement defect |
| **`C-SUMMARY-FROM-CARD`** | Every summary row is copied from the issued Field 4 table and cross-checked | `BLOCKING_INTEGRITY` (import) | The import commit is blocked |
| **`C-PROMOTION-RECEIPT`** | Every RULES-file rule carries its status, evidence count and, if predictive, a prospective-test ID. A predictive rule from one or two events is `TESTING` | governance | The rule is non-operative until it is receipted |
| **MLB gamefeed weather at freeze** | A baseball total at #1 or as the top O/U prints the statsapi `weather` block (field-relative wind), or `WEATHER_NOT_RETRIEVED` | `CONTEXT_MATERIALITY` → retrieval | Evidence cap on the total row |

**Rules withdrawn in the same pass** (all were promoted from a single game in `cb95acd`): `MLB-DOUBLEHEADER-G1-TOTAL-DEFLATION`, `BASKETBALL-DERBY-TOTAL-SUPPRESSION`, "dual run-line arbitrage", `FIBA-CLUB-QUALIFIER-PACE-ADJUSTMENT` (→ TESTING `T-BKB-SEASON-OPENER-WIDTH`) and `TENNIS-CHALLENGER-CLAY-HANDICAP-CAP` (→ TESTING `T-TEN-LOWTIER-HCP`). `NHL-PRESEASON-ROSTER-ASYMMETRY` is demoted to a non-ranking disclosure item.

<!-- RESEARCH-2026-09-25 -->
## 2026-09-25(b) — research-derived reference checks and retrieval tooling

Home: `RULES_GENERAL.md` §"2026-09-25(b)". Evidence: `BASE_RATES_REGISTER.md` §7, `RECENCY_AND_REBOUND.md` §7 and `research/base_rates_2026-09-25/`. Freeze receipt: `CONTROL_MANIFEST_2026-09-25-2.md`. The control revision label is unchanged (`CR-2026.09.21-3`), following the 2026-09-23 and 2026-09-25 precedent. These are additive disclosure, measurement and retrieval controls: none moves a probability, centre, width or rank.

| Control | Rule in one line | Class | Failure consequence |
|---|---|---|---|
| **`C-WIDTH-BENCHMARK`** | A printed total or margin width is printed beside the competition's reference width from `BASE_RATES_REGISTER.md` §7, or `REFERENCE_WIDTH_NOT_YET_DERIVED`. A width below 0.85 × the reference names the information that justifies it | disclosure (issue) | `WIDTH_BELOW_REFERENCE_UNEXPLAINED`; audit field `WB` (blocks under `--strict`) |
| **`C-WIDTH-Z`** | At settlement, print z = (actual − centre)/width for the total and the margin. It accrues to the `C-WIDTH-Z` manifest | measurement (settlement) | Measurement defect; audit field `10z` (blocks under `--strict`) |
| **`C-RECEIPT-TOOL`** | In lanes it covers, `receipts.py pregame` (at freeze) and `receipts.py settle` (at settlement) are the preferred receipts. A hand-written record must carry the same fields and endpoints | retrieval | A hand record without endpoints is `PROCESS_RECORD_UNVERIFIED` (2026-09-24(f)(b)). The tool is one lineage; C-FINAL3 is unchanged |
| **`C-HCP-COHERENCE`** (tennis) | A −k.5 games-handicap row prints P(win), c_s and c_d, beside the population conditionals. Hard identity: P(−k.5) ≤ P(win) | disclosure (issue); the identity fails closed | `HCP_CONDITIONAL_ABOVE_REFERENCE`; audit field `HC` (blocks under `--strict`) |
| **Early-season and regime references** | NBL and WNBA early-season windows (opposite signs); WNBA 2026 regime shift; NHL preseason. Print the reference beside the centre | disclosure (field BR) | Process defect |
| **`R-1` corollary** | A one-game comparator never carries more numeric weight than the season rate (worst predictor in 6 of 6 competitions) | reference | Process defect; G-L20 and M17 apply |

<!-- REPO-HYGIENE-CI-2026-09-25C -->
## 2026-09-25(c) — baseline skill, current-rules summary and repository controls

Home: `RULES_GENERAL.md` §"2026-09-25(c)". Freeze receipt: `CONTROL_MANIFEST_2026-09-25-3.md`. The control revision label is unchanged. None of these moves a forecast number.

| Control | Rule in one line | Class | Failure consequence |
|---|---|---|---|
| **`C-BASELINE-SKILL`** | Every ranked row prints `BASELINE_P`, the naive leak-free population probability of the same contract (or `NOT_YET_DERIVED`). Settled decisions go to `SKILL_BASELINE_LEDGER.md`; `tools/skill_baseline.py` reports card − baseline | measurement (issue and settlement) | Audit field `BP` (blocks under `--strict`). No skill statement without the preregistered 100-decision check |
| **`CURRENT_RULES.md`** | Step 0 of the reading gate. A derived live summary; the cited section governs on conflict, and the summary is updated in the same pass as any rule change | documentation | Documentation defect, fixed in the same pass |
| **`C-REPO-CI`** | CI runs every test, the hygiene check, manifest verification and the strict mini-log audit on every push and pull request | repository integrity | A red check blocks the merge (once branch protection is enabled) |
| **`C-BRANCH-PR`** | Sessions work on `session/<date>-<topic>` branches and merge by pull request after green checks. Commit messages follow `type(scope): what changed` (`CONTRIBUTING.md`) | repository integrity | A direct unreviewed commit to `main` is a process defect |
| **Manifest tooling** | Manifests are generated by `tools/make_manifest.py` and verified by `tools/verify_manifest.py`, with CRLF-form hashes and `.gitattributes` enforcing CRLF checkout | integrity | Stale manifest: CI fails |
| **Repository hygiene** | No tracked dependency trees, build output, local settings, raw API pulls, control characters or literal backslash-n artefacts (`tools/repo_hygiene.py`) | repository integrity | CI fails |

<!-- SETTLED-ROW-REVIEW-2026-09-25D -->
## 2026-09-25(d) — settled-row review controls

Home: `RULES_GENERAL.md` §"2026-09-25(d)". Evidence: `research/settled_rows_2026-09-25/README.md`. Freeze receipt: `CONTROL_MANIFEST_2026-09-25-4.md`. None changes a stated probability or rank (`L-087`).

| Control | Rule in one line | Class | Failure consequence |
|---|---|---|---|
| **`C-PLUS-CUSHION`** | A non-baseball +k.5 row prints the population margin band, `BASELINE_P`, P(underdog wins) + P(loses by ≤ k) from the card's margin distribution, and the named reason it stays close | CANDIDATE control (disclosure; recurrence ×3; record 17/40 at 0.642) | `PLUS_CUSHION_UNSUPPORTED`; evidence grade capped at LOW; audit field `PC` (blocks under `--strict`) |
| **`C-DEPARTURE-LEDGER`** | Each ranked row's log-odds departure from `BASELINE_P` is attributed to named mechanisms (`tools/card_math.py departure`) | construction discipline | `UNEXPLAINED_DEPARTURE` above 10% unattributed; grade capped at LOW; audit field `DL` (blocks under `--strict`) |
| **`C-TRACK-RECORD`** | The card prints its sport's (and family's) own calibration row from `tools/calibration_report.py`. An over-confident record, or Brier ≥ 0.25 on n ≥ 10, labels the card `NO_DEMONSTRATED_SKILL` | disclosure | Grade capped at LOW; departure ledger required |
| **`C-LOW-RESOLUTION-BAND`** | Rows stated 0.50–0.65 are labelled `LOW_RESOLUTION` and described as near-coin-flips | disclosure | Process defect |
| **Calibration review standard** | Every 25-card review runs `tools/calibration_report.py`: reliability, Murphy decomposition, logistic slope, card-cluster slices, baseline difference. No rank-slot claims below #1 | measurement | Review incomplete |
| **`tools/card_math.py`** | The reference distribution-to-contract implementation (M14/G-L8): normal, negative binomial, Poisson, Skellam, `no_zero`, push mass, exact joints | tool | A row not reproducible from the card's own distribution is invented precision (METHOD §12) |
