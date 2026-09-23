# Controls — current compact reference


Revision **CR-2026.09.21-3**, METHOD **MDS-2026.09.19-v4.3**. SCORING_AND_VALIDATION is the mathematical authority. The six-field METHOD object is the single mandatory output template. Historical controls and origins are preserved in LEARNING_REGISTER and the [pre-revision control snapshot](audit_2026-09-17_implementation/before/CONTROLS_with_margin_band_addition.md); their withdrawn statistical claims are not active rules.


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
- **C-FINAL3:** settlement requires at least **3 distinct reliable lineages** agreeing on exact event/date, explicit terminal state and final result. A score without a terminal marker is insufficient. Any credible live/in-progress source blocks settlement.
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
| **`S-1`** social identity | A social post needs durable-identifier identity, a checked timestamp, field-owner corroboration before it changes anything, and verbatim quotation. A plausible handle is not identity | `SOURCES.md` §"2026-09-19" |
| **`S-2`** press conferences | Admissible for availability, workload and role intent (`SECONDARY_ONLY`); **never** a signed adjustment to pace, efficiency or scoring rate | same |
| **`NOT_YET_PUBLISHED`** | A structured line-up query returning empty is a verified availability state, not a `RETRIEVAL_MISS` process defect. Record the query time | `SOURCES.md` §"2026-09-19"; §16.8 field 7 |
| **Debutant gates** | MLB `mlbDebutDate` → `LOW_SERVICE_SAMPLE`; ESPN cricket `debuts[]` → `NO_PRIOR_FORMAT_RECORD`; soccer `NO_COMPETITION_SAMPLE`. A debutant contributes width, never an assumed contribution | `RULES_BASEBALL.md`, `RULES_CRICKET.md`, `RULES_SOCCER.md` |


**Evidence base for `R-1`** (MLB 2026, 4,594 team-games / 108 starters / 2,244 out-of-sample predictions): rebound after a 0-run game **−0.102** runs [−0.456, +0.251]; top-10 offences after ≤2 runs **−0.126**; starter next-start ER after ≥6 ER **−0.017**, strikeouts **−0.070**; lag-1 autocorrelation +0.019 (team) and −0.037 (starter); recency RMSE last-1 **2.7677** > last-3 **2.2433** > last-5 **2.1324** > season **2.0177** > league constant **1.9844**. Empirical estimates on one season of one competition — not identities, not universal bounds, not fitted coefficients (`L-087`).


## 2026-09-19(b) — active-control classification (resolves the `L-095` deferral) and control revision CR-2026.09.19-1


**Why this exists.** `L-095` (2026-09-06) created a three-class control taxonomy and deferred tagging the ~86 lesson rows that predated it. That backlog has sat open ever since, and `L-096` — the control-effectiveness review — cannot run without it. The deferral is resolved here by **correcting the unit**: `L-096` needs *controls* classified by consequence-of-failure, not historical *lesson rows* tagged. `METHOD.md` §9 is explicit that dated retrospectives and archived text are evidence, not active instructions, and `METHOD.md` §4 has since superseded the taxonomy's forward function. Retro-tagging the 86 historical rows is therefore **closed as not-to-be-done**, with the reasoning recorded, rather than carried indefinitely. Full disposition: [`AUDIT_IMPLEMENTATION_2026-09-19.md`](AUDIT_IMPLEMENTATION_2026-09-19.md) §4.


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
| **`S-1`** social identity gate | `MECHANISM_REQUIRED` | social claim stays `SECONDARY_ONLY`, cannot lift a participant field |
| **`S-2`** press-conference material | `CONTEXT_MATERIALITY` | admissible for availability/role only; never a signed rate adjustment |
| `G15.1` environment / venue-coordinate forecast | `CONTEXT_MATERIALITY` | evidence cap (outdoor events) |
| `G13.1` descriptive recency windows, `G17.1` streak audit | `CONTEXT_MATERIALITY` | descriptive display only — **not** a trend test (withdrawn 2026-09-17) |
| `G-L20` direct current-regime comparable | `CONTEXT_MATERIALITY` | mass must be sized to its `n`; a single comparable is the weakest predictor measured (`R-1` §4) |
| Debutant gates (`LOW_SERVICE_SAMPLE`, `NO_PRIOR_FORMAT_RECORD`, `NO_COMPETITION_SAMPLE`) | `CONTEXT_MATERIALITY` | contributes width; no assumed contribution |
| `TOP_OU_REVIEW` trigger | *retrospective duty* | not a forecast-time control; it governs settlement scrutiny only |


`L-096` is now executable: for any `BLOCKING_INTEGRITY` or `MECHANISM_REQUIRED` control, compare the recurrence rate of its target defect before and after its effective date. A control whose target defect recurs at a similar rate post-adoption indicates an **execution** problem, not a wording problem — and per `L-096` the response is compliance discipline, not a fourth restatement of the rule.


### Control revision CR-2026.09.19-1


The control set changed on 2026-09-19 (`METHOD.md` §7, `SCORING_AND_VALIDATION.md` §3, this file, `SOURCES.md`, `DATA_SOURCE_REGISTER.md`, all ten `RULES_*.md`, and the new `RECENCY_AND_REBOUND.md`). The revision ID therefore advances from `CR-2026.09.17-1`.


**Manifest: 24 files** — the 23 in the previous manifest plus `RECENCY_AND_REBOUND.md`, which is control-class and must be covered. `audit_2026-09-17_implementation/VALIDATION.md` was corrected in the same pass so its manifest includes that file and its emitted revision label is **read live from `METHOD.md`** rather than hardcoded. **The authoritative revision ID is the one in `METHOD.md`.** **The hash value itself is deliberately NOT recorded in this file.** `CONTROLS.md` is inside the manifest, so writing the hash here would change the bytes being hashed and invalidate the value as it is written — a self-reference loop. The authoritative value lives in [`AUDIT_IMPLEMENTATION_2026-09-19.md`](AUDIT_IMPLEMENTATION_2026-09-19.md) §7 and in `audit_2026-09-17_implementation/RESULTS.md`, **both of which are outside the manifest**. Never record a manifest hash inside a manifest file.


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


If the bytes have changed since the value recorded in [`AUDIT_IMPLEMENTATION_2026-09-19.md`](AUDIT_IMPLEMENTATION_2026-09-19.md), **open a new revision ID** rather than reusing this one. A hash is a byte receipt, not timestamp evidence.


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


`A-REC-1` is a blocking governance check before an historical audit finding changes current analysis. Resolve the finding through `AUDIT_RECONCILIATION_ALL_SPORTS_2026-09-21.md`.


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