# Comprehensive sports research audit and rebuild - 2026-07-16

Status: completed specification rebuild; operational forecasting **SUSPENDED — NO ACTIVE MODELS**  
Supersedes: `AUDIT_AND_CHANGES_2026-06-12.md`  
Evidence directory: `outputs/comprehensive_audit_20260716/`

## Executive verdict

The criticism that the prediction process produced too many wrong and misleading calls is justified. The failure was not simply bad luck or occasional non-compliance. The prior system had structural defects that could make a weak process look better than it was:

- it scored multiple alternatives from the same market, including exact complements, as though they were independent predictions;
- it optimized a custom top/bottom penalty system rather than a proper forecasting or expected-value objective;
- it mixed pregame, live, revised, and post-settlement information in mutable records;
- it generated many probabilities from nested recent-form counts and narrative adjustments without a reproducible fitted model;
- it treated simulation repeatability as confidence while often leaving parameter and model uncertainty unmeasured;
- it pooled incompatible sports, competitions, market families, and forecast states;
- it used source rituals and rule accumulation as substitutes for point-in-time evidence and forward validation;
- it had no prices, stakes, or payouts capable of supporting a profitability claim.

No honest rebuild can promise that no future prediction will be wrong. The repair is to make every issued forecast timestamped, reproducible, uncertainty-aware, separately settled, and eligible for proper out-of-sample evaluation - and to `PASS` when those conditions are not met.

## Audit scope

The sweep covered:

- the 9,494-line v2 operating document and its archived predecessor;
- the v2 source registry and the standalone Poisson/simulation framework;
- both historical results logs;
- the v2 CSV ledger, settled workbook, raw JSON files, and audit outputs;
- recorded decisions across Australian football, baseball, basketball, cricket, and soccer;
- source and rules chains for those sports plus rugby league, ice hockey, American football, tennis, and golf;
- performance reconciliation, rank behaviour, sport segmentation, complements, duplicates, schema quality, leakage risk, calibration, simulation design, and source freshness.

The quantitative results below are diagnostics of the files as found. They are not certified prospective results.

## 1. There was no single source of truth

Three active-looking sources disagree:

| Source | Real structured selections | Recorded result | End state |
| --- | ---: | --- | --- |
| `SPORTS_CALIBRATION_LEDGER_v2.csv` | 437, plus one embedded template row | 246-185-2, plus two `UNGRADED` and two unresolved `U` rows | Stale |
| Settled v2 workbook | 449, plus one embedded template row | 253-190-2, plus two `UNGRADED` and two unresolved `U` rows | Newest structured file, ending 2026-07-13 |
| `PREDICTION_RESULTS_LOG_v3.md` | Narrative rows and addenda | Later settlements and a 2026-07-16 live/provisional case | Not synchronized to either ledger |

The workbook has 12 records not in the CSV: three four-selection cards dated 2026-07-13. The narrative log then continues later. One logged LA-Minnesota row was simultaneously described as settled elsewhere and still marked pending in the card table. That is enough to reject every unqualified “current record” claim.

New rule: prediction and settlement tables are separate, append-only, and keyed by stable IDs. Summaries must be generated from one declared snapshot, not assembled by hand from whichever file is newest.

## 2. Headline legacy metrics were not trustworthy KPIs

Using the settled workbook only, the gross legacy result is 253 wins, 190 losses, and two pushes: 57.1% over 443 decisions. Mean stated probability is 54.3%, with an apparent Brier score of 0.219 and log loss of 0.626.

Those figures are labelled `RETROSPECTIVE_UNVERIFIED_LOCK`, not model performance, because the records do not preserve:

- an immutable prediction timestamp and event start;
- a data cutoff proving every feature was known at issue time;
- pregame/live state in a controlled field;
- a model, feature, data, code, and calibrator version;
- a source-packet ID and snapshot hash;
- direct source URLs for the decisive facts and settlement;
- a separate append-only settlement record.

No CSV `settlement_source` cell contains a direct HTTP URL; the field contains prose source names. Probability, outcome, error classification, and retrospective narrative sit together in mutable rows. At least dozens of prediction-base fields contain post-event settlement language. Consequently, the audit cannot prove that the stated probabilities were frozen before the outcomes were known.

The apparent Brier and log-loss numbers are retained only to locate suspicious segments. They cannot promote a model or substantiate an accuracy claim. Proper scoring rules reward honest probabilities only when forecasts are genuinely prospective; the replacement standard follows [Gneiting and Raftery (2007)](https://doi.org/10.1198/016214506000001437) and chronological evaluation principles rather than random or retrospective re-ranking.

## 3. Complementary card construction distorted the record

The same-line over/under sweep found 73 of 102 legacy card IDs containing at least one exact over/under complement. Those affected cards account for 338 rows when every row on an affected card is flagged for correlation review. A pair-member detector that also includes opposite spreads found 150 exact pairs - 127 over/under and 23 opposite-spread pairs - occupying 300 individual rows across 75 card IDs. The counts differ because one measure flags whole cards and the other counts only exact pair members.

After the 12 workbook-only rows are included, the final migration workbook detects 306 exact complement-selection rows out of 449 (68.2%). The six-row increase comes from exact pairs in the later cards; it does not count every correlated or overlapping alternative, so it remains a lower bound on dependence.

This is not a minor presentation issue. On a non-push result, listing both `Over 183.5` and `Under 183.5` guarantees one win and one loss. Thirty-seven four-pick cards were composed entirely of two complementary pairs. Apart from unresolved/push branches, a 2-2 result was built into the card and provided no evidence of forecasting skill.

The log also repeated the same Collingwood-Richmond outcomes across multiple card IDs without a stable issue timestamp or `supersedes_prediction_id`. That multiplies one final outcome across undocumented revisions.

New rule: one selected market outcome is one prediction. The opposite side belongs in the candidate probability vector and is not independently scored. A later live reforecast receives a new immutable snapshot and an explicit parent; it never overwrites or silently duplicates the earlier call.

## 4. Ranking quality did not support the old narrative

The latest structured workbook produces the following descriptive rank results:

| Rank | W-L-P | Hit rate excluding pushes | Mean stated probability | Finding |
| ---: | ---: | ---: | ---: | --- |
| 1 | 69-34-0 | 67.0% | 65.5% | Far below the old self-imposed 80% target |
| 2 | 62-37-1 | 62.6% | 59.8% | Some separation, not independently validated |
| 3 | 54-43-1 | 55.7% | Weak separation |
| 4 | 46-52-0 | 46.9% | Not a <=30% “bottom” outcome |
| 5 | 3-12-0 | 20.0% | Small sample and overstatement |
| 6 | 10-5-0 | 66.7% | Rank inversion |
| 7 | 6-2-0 | 75.0% | Rank inversion; very small sample |
| 8 | 3-5-0 | 37.5% | Very small sample |

Since 2026-07-10, rank 1 was 13-5 while rank 4 was 10-3. A period in which the nominal bottom slot wins 76.9% of decisions is not evidence that ranking improved simply because the aggregate card record rises.

The old top-pick-loss and bottom-pick-win flags also mixed card-level and selection-level semantics. Some cards copied a flag across every row; others marked only the affected row. The resulting penalty totals are not reproducible and are retired.

New evaluation uses Brier/log loss and appropriate multiclass/distributional scores, baseline comparison, calibration diagnostics, and uncertainty on a locked cohort. Rank is a downstream decision display, not a scoring economy.

## 5. Sport results were uneven, correlated, and incomplete

Latest-workbook descriptive results are:

| Canonical group | Decisions | W-L-P | Hit rate | Audit interpretation |
| --- | ---: | ---: | ---: | --- |
| Australian football | 44 | 23-21-0 | 52.3% | Coin-flip level; no demonstrated edge |
| Baseball, other | 24 | 15-9-0 | 62.5% | Small mixed-league sample |
| Basketball, other | 115 | 60-55-0 | 52.2% | Near coin flip |
| Cricket | 97 decisions | 54-43-0 | 55.7% | Plus two void and two unresolved rows; heavily complement/phase driven |
| KBO | 12 | 7-5-0 | 58.3% | Too small to rely on |
| MLB | 42 decisions | 23-19-2 | 54.8% | Alternative lines and correlation limit meaning |
| NPB | 4 | 2-2-0 | 50.0% | No inference possible |
| Soccer | 81 | 56-25-0 | 69.1% | Inflated by broad safety outcomes and mixed taxonomy |
| WNBA | 24 | 13-11-0 | 54.2% | Poor probability quality despite near-even hit rate |

The soccer number is especially misleading: rows labelled simply `Soccer` and rows labelled `Soccer/FIFA World Cup` have materially different results and market construction. They should not have been pooled. The largest heuristic market family - phase and innings totals - was approximately coin-flip despite repeated confidence narratives.

The ledger has meaningful volume only in five broad families: Australian football, baseball, basketball, cricket, and soccer. There is no meaningful locked sample for NFL, NHL, NRL, tennis, golf, rugby union, motorsport, or combat sports. “All sports” is therefore a source/process coverage statement only. It is not evidence of predictive validity in every sport.

New rule: no all-sport calibration number. Cohorts are segmented by model version, sport, competition class, market family, forecast horizon, and pregame/live state. Unsupported segments remain `RESEARCH_ONLY` or `PASS`.

## 6. Forecast construction was not reproducible enough

The v2 process repeatedly used fixed L5/L10/L15/L20 windows, recent hit counts, hand-chosen round weights, narrative “haircuts,” and manually assigned confidence. Those inputs can be useful exploratory features, but they are not a probability model unless the feature definition, training set, target, fitting method, calibration, and out-of-sample result are frozen and reproducible.

The system also searched across many candidate markets and then presented a self-selected “best four.” That creates selection bias. Broad safety markets, exact complements, overlapping cushions, totals, player props, winner leans, pregame forecasts, and live forecasts were mixed in one results narrative.

One-off postmortems generated new hard rules after individual losses. This is rule accretion and outcome-fitting, not validated learning. A single 80% forecast can lose without proving the model wrong; a new universal rule should not be created from that one result. Conversely, repeated nominal 80% forecasts winning materially less than 80% is evidence that must be tested on a locked forward sample.

New model changes require a change ticket, training/calibration/test boundaries, declared baselines, chronological validation, a model card, promotion criteria, and rollback conditions. Feature-window and decay choices must be selected inside training folds. The validation framework uses expanding/rolling time splits and dependence-aware uncertainty; it does not randomly shuffle matches across roster, season, and rules regimes. See [Hyndman's time-series cross-validation reference](https://pkg.robjhyndman.com/forecast/reference/tsCV.html).

## 7. Simulation precision was overstated

The old Poisson framework often started from assumed means or narrative adjustments, simulated many draws, and reported stable-looking percentages. More Monte Carlo draws reduce simulation noise conditional on the chosen parameters; they do not repair biased parameters, wrong independence assumptions, omitted lineup effects, structural breaks, or the wrong distribution.

Raw Poisson assumptions are especially fragile under overdispersion, zero inflation, correlated scores, changing game state, weather/venue regimes, overtime, cricket wickets/balls/depth, and basketball/AFL possession dynamics. Count models remain useful transparent baselines in suitable settings - for example, the classic soccer work of [Dixon and Coles (1997)](https://doi.org/10.1111/1467-9876.00065) - but a named distribution is not validation.

New simulation outputs must report model and parameter provenance, seed, draw count, Monte Carlo standard error, predictive intervals, push/void branches, and challenger disagreement. Analytic probabilities are preferred when available. No simulated probability is issued until the underlying model beats declared baselines out of sample.

## 8. Source policy and rules needed factual corrections

The v2 registry contained a malformed rules table, stale access claims, mandatory StatMuse-first checks, mandatory social checks even when blocked, access proxies presented like sources, and undocumented/aggregator endpoints elevated beyond their authority.

The replacement registry makes authority fact-specific:

- official governing body, competition, event, team sheet, gamebook, or scorecard controls rules, identity, eligibility, state, and settlement;
- licensed or defined statistical providers may control their own measured data, with definition and freshness recorded;
- specialist secondary sites and aggregators are cross-checks, not silent substitutes for official facts;
- social media is optional discovery unless it is an authenticated first-party statement;
- an access proxy is never cited as the publisher;
- blocked, missing, intermittent, and JavaScript-only access states are recorded honestly.

The sweep also corrected time-sensitive rules claims. Examples include the 2026 NRL process of a final 19 at 90 minutes before kickoff followed by verification of the actual 17; FIBA's 2024 rules remaining the baseline until the 2026 rules take effect on 2026-10-01 unless exact competition regulations override; the MCC 2026 Laws taking effect on 2026-10-01; and NFL 2026 playing-rule proposals not being treated as a final 2026 rulebook.

The registry now records effective dates, observed/fetched dates, fact type, and fallback status. It removes the fiction that adding more mandatory websites automatically creates better evidence.

## 9. Prices, EV, ROI, and staking were unsupported

The v2 schema has no complete bookmaker/operator, decimal price, price timestamp, market status, stake, payout, commission/vig, or closing-price record. Many log entries explicitly say “research-only, no odds.” Raw JSON odds objects cannot fill the gap because they are not reliably mapped to prediction IDs or proven to have been available at the cutoff.

Therefore:

- ROI, yield, closing-line value, and profitability are unknown;
- a high event probability is not automatically a good bet;
- “micro-stake” language is retired unless a timestamped executable price, uncertainty policy, bankroll policy, correlation control, and settlement result exist.

When prices are authorized, the structured record must retain the exact operator/provider, jurisdiction/delay state, market ID and rules, side, line, price, available size when relevant, open/suspended/in-play status, observed time, and source hash. Expected value is calculated only from the calibrated probability and that recorded price.

## 10. Current case confirming the problem

At 11:55 AEST on 2026-07-16, `PREDICTION_RESULTS_LOG_v3.md` recorded a provisional MI New York-Washington Freedom MLC Eliminator watchlist:

1. MI powerplay Under 52.5 at about 62%;
2. MI 20-over Under 183.5 at about 59%;
3. MI 20-over Over 183.5 at about 41%;
4. MI powerplay Over 52.5 at about 38%;
5. Washington winner lean at about 61%.

The row correctly said it was **not a validated final card** because the match-specific pitch report was not verified, but it still published precise probabilities and both sides of each line. MI New York then scored 266/9 in 20 overs. The mandatory powerplay was 100 runs at six overs. The two favoured unders lost by extreme margins and the complementary overs won. The [official Washington Freedom match page](https://www.washingtonfreedom.com/schedule-fixtures-results/washington-freedom-vs-mi-new-york-wafmny07152026270186) records MI's 266/9; the [current Cricbuzz scorecard](https://www.cricbuzz.com/live-cricket-scorecard/150931/waf-vs-miny-eliminator-3v4-major-league-cricket-2026) shows the 100-run mandatory powerplay.

At the audit verification time, the chase had not finished on the opened current sources, so the Washington winner lean remains unresolved and is not graded. The entire case is legacy/provisional and excluded from v4 calibration.

This case does not, by itself, identify one certain causal parameter error because the original feature/model snapshot was not preserved. It does show the operational defects directly: a missing critical input did not result in a clean pass, a narrow recent-innings argument understated the upper tail, precise probabilities were issued without a validated model artifact, and complementary alternatives manufactured a 2-2-looking selection result from one badly missed directional view.

## Changes implemented

### Canonical policy and schema

- `SPORTS_RESEARCH_AUTHORITY_MANIFEST.md` establishes one precedence order and an explicit `SUSPENDED — NO ACTIVE MODELS` state.
- `SPORTS_MODEL_COVERAGE_REGISTRY_v3.csv` is the exact operational allowlist; it now contains 15 non-operative DEVELOPMENT architecture rows and one UNSUPPORTED catch-all, with zero ACTIVE rows.
- `combined_sports_doc_v3.md` replaces the 9,494-line accumulated rule stack with a concise operating manual.
- `SPORTS_SOURCE_REGISTRY_v3.md` replaces mandatory-site rituals with fact-specific authority, current official routes, effective dates, and honest fallback states.
- `SPORTS_DATA_DICTIONARY_v3.md` defines normalized request, snapshot, candidate-universe, prediction, source, feature, model, uncertainty, price, execution, settlement, and evaluation records.
- `SPORTS_MODEL_VALIDATION_AND_SIMULATION_FRAMEWORK_v3.md` defines chronological validation, baselines, proper scores, model cards, calibration, uncertainty, simulation requirements, promotion, monitoring, and rollback.
- `SPORTS_SCORING_SPECIFICATION_v3.md` is the single authority for eligibility, proper scores, branch reconciliation, EV, execution metrics, and test fixtures.
- `SPORTS_ACCEPTANCE_TESTS_v3.md`, the runtime under `src/`, and both validators provide fail-closed gates. Executable coverage is reported item-by-item and is not equivalent to model validation.
- At this audit cutoff, `PREDICTION_RESULTS_LOG_v4.md` was retained as pre-runtime prose evidence with zero eligible predictions and `PREDICTION_RESULTS_LOG_v5.md` was an empty journal-derived view contract. This sentence is historical; v5 is now a generated copy-friendly view of the current verified journal.
- `SPORTS_CALIBRATION_LEDGER_v3.csv` and `SPORTS_SETTLEMENTS_v3.csv` are initialized header-only structured transports; historical rows are not migrated into them.

### Controls retired

- top-pick-loss, bottom-pick-win, sweep exemptions, double penalties, and the adjusted penalty record;
- forced four-pick cards and independent scoring of complements;
- mandatory StatMuse-first and mandatory blocked social checks;
- universal L5/L10/L15/L20 requirements;
- all-sport pooled calibration;
- staking or ROI language without timestamped prices;
- simulation confidence based only on a high draw count;
- new hard rules derived from one miss.

### Controls added

- one market outcome per prediction and separate candidate probabilities;
- `PASS / MODEL_UNAVAILABLE` with null quantitative fields while no exact coverage row is ACTIVE;
- immutable request, publication snapshot, event start, cutoff, model/data/feature/code versions, source packet, and hash;
- independent analysis mode plus `PREGAME_PROJECTED`, `PREGAME_CONFIRMED`, or typed LIVE state, with new snapshot/prediction IDs for every update;
- append-only settlement versions with direct source URLs and correction history;
- controlled sport/competition/market/status enums;
- proper out-of-sample scores, simple baselines, calibration diagnostics, sharpness, and dependence-aware uncertainty;
- model cards, change tickets, promotion gates, monitoring triggers, and rollback;
- UNSUPPORTED status for every unvalidated sport/market/state/mode and no headline all-sport KPI.

## Data quarantine and preservation

Pre-audit copies are preserved under `archive/pre_audit_20260716/`. The old root documents and ledgers are deprecated even if retained for traceability.

The root JSON files are `QUARANTINED_UNPROVENANCED`. Several contain final or odds-related material, while filenames do not prove provider, request time, cutoff, or data-through state. They cannot enter training or backtesting until a source route, timestamps, event mapping, access status, hash, and point-in-time relationship are documented.

The legacy audit/migration table marks historical rows ineligible. That is deliberate: a missing pre-event lock cannot be reconstructed after the result merely by copying the row into a cleaner schema.

## What remains unknown

- The true prospective accuracy and calibration of the historical forecasts.
- Whether any historical segment beat a simple baseline after candidate-selection and correlation effects.
- Profitability, because executable prices, stakes, and payouts were not captured.
- Exact causal attribution for many misses, because feature/model snapshots were mutable or absent.
- Predictive quality for NFL, NHL, NRL, tennis, golf, and other unrepresented sports.
- Whether a future v3 model will improve results; that requires a new locked forward sample.

These are not small footnotes. They are why no legacy KPI is carried into v4.

## Release conditions for any future performance claim

A sport/model/market/state/mode cohort remains UNSUPPORTED or SHADOW-only until all of the following are true:

1. Every forecast is frozen before its target resolves, with a reproducible point-in-time source and feature snapshot.
2. The target, settlement convention, candidate universe, model, calibrator, and analysis plan are predeclared.
3. Evaluation is chronological and leakage-free, with dependencies clustered or blocked.
4. The model beats declared simple baselines on proper scores with uncertainty, not just hit rate.
5. Calibration and sharpness are acceptable on a forward holdout of sufficient effective size.
6. Model-search and multiple-testing history is retained.
7. EV uses a complete timestamped price/branch packet; ROI, yield, P&L and CLV use an actual execution and valid comparable close.
8. Monitoring and rollback thresholds are active.
9. A later prospective shadow meets its preregistered rule after the untouched test has been viewed and marked SPENT.
10. The reviewed model card, source map, parser tests, artifacts, approval, expiry, and exact coverage row are activated together.

Until those conditions are met, the correct label is `MODEL UNAVAILABLE / NO VERIFIED EDGE`.

## Audit evidence index

- `outputs/comprehensive_audit_20260716/performance_audit.md`: reconciliation, rank/sport metrics, complements, data integrity, and causal patterns.
- `outputs/comprehensive_audit_20260716/methodology_audit.md`: objective-function, validation, calibration, simulation, and sport-specific design review.
- `outputs/comprehensive_audit_20260716/source_research.md`: 2026 source and rules verification with direct official routes.
- `outputs/comprehensive_audit_20260716/performance_summary.json`: machine-readable counts and metrics.
- `outputs/comprehensive_audit_20260716/complement_pairs.csv`, `outputs/comprehensive_audit_20260716/ledger_issue_records.csv`, and `outputs/comprehensive_audit_20260716/csv_xlsx_diff.csv`: record-level evidence.
- `outputs/comprehensive_audit_20260716/SPORTS_RESEARCH_AUDIT_20260716.xlsx`: readable audit workbook and clean v3 templates.
- `outputs/comprehensive_audit_20260716/static_validation.txt`: final static specification-gate output; runtime/model validation is explicitly not implied.
- `outputs/comprehensive_audit_20260716/FILE_INTEGRITY_MANIFEST_20260716.csv`: final file sizes and SHA-256 hashes for the rebuilt deliverables and principal evidence files.

## Final accountability statement

The previous documentation was too long, too prescriptive in the wrong places, and too permissive about the central requirement: proving what was predicted, with what data and model, before the outcome. The June audit over-attributed failures to process compliance and under-recognized that the scoring and probability-construction design itself was flawed. That conclusion is withdrawn.

The rebuilt system does not erase the mistakes or convert legacy rows into validated evidence. It prevents those rows from supporting claims they cannot support, records the known failures plainly, and makes the next forecast earn its place in the results register.

## Development model construction update

Later on 2026-07-16, the previously generic sport requirements were instantiated in `SPORTS_DEVELOPMENT_MODEL_CATALOG_v1.md` as version 0.1.0 architecture cards. The catalog contains a shared point-in-time hierarchical generative framework and 15 sport-native modules: Australian football, rugby league, rugby union, cricket, soccer score, soccer counts/player events, basketball, baseball, ice hockey, American football, tennis, volleyball, golf, motorsport and combat.

The cards specify coherent primitive-event engines, baselines, participation/exposure scenarios, required features, live-state contracts, diagnostics, transfer restrictions and hard exclusions. Related markets must derive from one joint distribution; player props require a separately validated exposure model. A missing or materially unstable input forces abstention.

The corresponding broad coverage rows changed from `UNSUPPORTED` to `DEVELOPMENT` and now name their catalog model ID/version. No activation evidence was added: source-map, test, shadow, approval and expiry fields remain blank. `OTHER_SPORT_ALL` remains `UNSUPPORTED`. A new static test, `SPEC-DEVELOPMENT-MODELS-001`, verifies those invariants and prevents a design card from being mistaken for an active model.

This update improves implementation readiness, not forecast readiness. No eligible training data, fitted coefficients, calibration artifact, untouched test, prospective shadow or empirical accuracy result was created. Operational status therefore remains `SUSPENDED — NO ACTIVE MODELS` and all quantitative requests still return `PASS / MODEL_UNAVAILABLE`.
