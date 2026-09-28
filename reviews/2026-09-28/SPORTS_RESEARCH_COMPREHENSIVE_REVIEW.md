# Sports Research: comprehensive review

**Reviewed:** 28 September 2026, Australia/Sydney. **Overall rating: 6.0 / 10.**

**Assessment: Needs revision.** The framework is substantially stronger than its current execution. Its written safeguards are thoughtful, its software is useful, and it is unusually candid about unproven models. However, current settlement records contain demonstrable factual and transcription errors, the scoring pipeline does not preserve essential eligibility and probability fields, and prospective evidence has barely started. More written rules will not resolve those problems by themselves.

**Verification completeness: Partial.** All major document families were covered; historical records and external sources were sampled. The requested review and repair-plan artifacts are complete within that stated scope.

This is a reviewer judgement about the documents and working research system, **not a 60% forecast success rate, an estimate of profitability, or a statistically measured quality score**.

The companion [repair plan](SPORTS_RESEARCH_REPAIR_PLAN.md) specifies the order of work, affected files, required evidence and acceptance checks. This review creates new review artifacts only. It does not change issued cards, settlements, governing rules, model coefficients, IDs or the user's staged changes.

## 1. Scope and evidence

The review inventoried **71 documents**: 61 root Markdown files, nine research-folder READMEs and the current P-518-onward mini log. Together they contain approximately 1.50 million whitespace-delimited words, largely historical logs. The inventory and SHA-256 fingerprints are in [audit_evidence.json](audit_evidence.json).

Coverage is **comprehensive across the major document families, with sampled historical verification**. It is not a claim that every historical sentence, forecast, source URL or sporting rule was independently reverified. Work included:

- Operational authority, scoring and eligibility rules; source policy; numerical-model stages; research validation summaries; all ten sport modules' live-rule introductions and selected gates.
- The five combined logs through their custody/status summaries, the full settled-row extract, and targeted historical examples, including P-443 and P-491.
- All five current mini-log cards' issued and settlement tables, their state labels, source receipts and selected retrospective claims.
- Independent arithmetic over the committed 1,264-row dataset and the 20 ranked settlement rows in P-518–P-522.
- The root and tools test suites, repository hygiene, current control manifest, evidence-status report and strict mini-log completeness audit.
- Fresh field-owner checks of MLB event 822678 and AFLW event 8942. These are targeted verification, not complete three-lineage re-settlement of the cohort.

The reviewed checkout was `main`, HEAD `39edc5e8cb787169723bce929e0dbab4d3be8a08`. The P-518 mini log already had both staged and unstaged changes. Findings about it refer to the **working-tree version**, not an assertion that these changes have been committed or approved. Earlier context helped locate the authority files; current findings come from the files and checks performed in this review.

**Limits:** Google Drive copies were not audited. The historical model experiments were inspected through their code/design and retained results; all season-scale experiments were not rerun. GitHub branch protection was not verified. ESPN's cited MLB summary endpoint returned access denied, and some pages did not render through the web reader. Such access failures are not evidence that their underlying claims are false.

## 2. Rating and rationale

The weights sum to 100%; the weighted score is exactly 6.0/10. The marks are deliberately more demanding for evidence and record integrity than for the number of documents or sophistication of terminology.

| Dimension | Weight | Score / 10 | Assessment |
|---|---:|---:|---|
| Research design and governance | 15% | 8.5 | Strong separation of forecasts, outcomes, revisions, sources, horizons and model promotion. |
| Source policy and provenance | 10% | 7.0 | Good field-owner and lineage rules; current receipts do not consistently substantiate the claims attached to them. |
| Probability and model design | 15% | 6.5 | Distribution-first design is sound; row-level calibration and some manual distributions break consistency. |
| Validation and demonstrated skill | 20% | 4.0 | Useful historical experiments, but selection/reuse limits and no qualifying prospective baseline record. |
| Ledger and settlement integrity | 15% | 4.5 | Preserved issued records and correction history are strengths; current baselines, process facts and queue summaries drift. |
| Reproducibility and engineering | 10% | 7.5 | Standard-library tools, tests, hashes and fixtures; semantic validation and complete data schemas remain missing. |
| Clarity and maintainability | 10% | 5.5 | Clear entry points exist, but layered overrides, stale headers and long summaries make correct operation difficult. |
| Learning and change discipline | 5% | 5.5 | Rule freeze and candidate statuses are good; recent retrospectives still turn isolated outcomes into confident causal stories. |
| **Overall** | **100%** | **6.0** | **A serious research framework that needs evidence and execution repairs before its conclusions can be trusted consistently.** |

The score would rise through accurate records, reproducible semantic checks and clean prospective evaluation. Adding further sport-specific rules or increasingly precise subjective probabilities would not, by itself, improve the rating.

## 3. What is already good

**The mathematical policy is substantially right.** `SCORING_AND_VALIDATION.md` distinguishes binary, conditional decisive and categorical push-aware scores; treats complementary rows as one target; recognises covering-pair hit rates as mechanical; and calls for event-level weighting and clustered uncertainty. It also separates observed results from operator action terms. These are essential protections against misleading success rates.

**The evidence boundary is honest at the top level.** The README, method and eligibility policy say the historical logs remain learning-only. H0 is explicitly not approved. Numerical implementations are separated from promoted forecasting models. The failed MLB starter experiment, weak cricket results and NHL totals deterioration are retained rather than hidden.

**Source controls are detailed and sport-aware.** Cricket toss and strip evidence are separated; basketball distinguishes actual tip from scheduled start; baseball accounts for starters and home-team termination; soccer distinguishes regulation from qualification; hockey treats overtime and shootouts separately; tennis recognises retirement and format differences. These modules deserve preservation, with freshness checks for the specific competition being analysed.

**There is real engineering work.** The current manifest matched all **124 entries**. Repository hygiene reported no problems among **688 tracked files**. All **79 root tests and 126 tools tests passed**. The tools calculate probabilities and scores, expose missing evidence and maintain a reproducible research trail.

**Recent methodological restraint is valuable.** `C-RULE-FREEZE`, a declared event universe, shadow lanes and the prospective baseline ledger are the right direction. The predictability research correctly retained the existing approach when an alternative did not show a convincing advantage. That is stronger practice than changing coefficients after every loss.

## 4. Prioritized findings

Severity here describes impact: **P0** can invalidate a central result or its evidence; **P1** materially affects interpretation, measurement or operation; **P2** affects clarity or maintenance. Findings below are proposed repairs, not changes already applied to the research system.

### F1 — P0: A correct final score is being used to support an incorrect process record

**Location:** current mini log, P-518 settlement, approximately lines 227–261.

The official MLB feed confirms Mets 7–1 Nationals, so this review is not claiming the final score is wrong. It contradicts several details used to explain that result:

| Field | Mini-log settlement | Fresh official feed |
|---|---|---|
| Mets runs–hits–errors | 7–11–1 | **7–9–1** |
| Nationals runs–hits–errors | 1–5–0 | **1–3–1** |
| Jonah Tong | 4.2 IP, 6 K, 4 BB | **5.0 IP, 9 K, 1 BB** |
| Connelly Early | 3.0 IP, 2 H, 2 BB, 4 K, 54 pitches | **3.0 IP, 1 H, 0 BB, 1 K, 34 pitches** |
| Game duration | 2:58 | **2:43** |
| Attendance | 26,452 | **27,284** |

Source: [MLB official event 822678](https://statsapi.mlb.com/api/v1.1/game/822678/feed/live), freshly retrieved at the time recorded in [the extracted verification receipt](mlb_822678_verification.json). This verifies one upstream source; it does not certify the log's three-lineage claim.

P-518's summary row also says 28 September 03:05 AEST, while the issued card and official feed identify 26 September 16:35 UTC, or **27 September 02:35 AEST**. The Baseball-Reference settlement link uses a different date from that event. Those discrepancies need reconciliation, not an assumed new fixture.

**Fix proposed:** append a sourced correction, retain the original issued card and superseded settlement, and quarantine the affected causal learning. Recheck the whole process record against the exact event. Do not assume that corrected scorekeeping requires changing the issued forecast or its outcome grade.

### F2 — P0: Settlement tables change the baselines that were supposedly frozen

**Location:** all five current cards' settlement tables; 20 ranked rows.

Every settlement `BASELINE_P` cell is 0.500, although the corresponding issued values or missingness states differ. Examples:

- P-518 Mets +1.5: issued **0.638**, settlement **0.500**; its printed team reference **0.6249** is replaced by a status label.
- P-520 Giants ML: issued **0.536**, settlement **0.500**.
- P-521 Joventut −5.5: issued **0.5445 card diagnostic; ACB register NOT_YET_DERIVED**, settlement **0.500**.
- P-522: issued **NOT_YET_DERIVED:acb**, settlement **0.500**.
- P-519: the issued text itself already mixes `NOT_YET_DERIVED` with a parenthetical 0.500; settlement removes that distinction entirely.

The evidence script found **20/20 baseline-field mismatches**, plus 20 team-baseline text/value mismatches. Some team-baseline mismatches discard qualifiers rather than numbers; they are not all numerical errors. Missing baselines are not measured 50% probabilities. A coin-flip comparator can exist, but it needs its own name and must not replace the frozen comparison.

**Fix proposed:** join settlement rows to immutable issued rows by exact decision identity, copy every frozen field verbatim and retain missingness. Add a separate `coin_flip_reference` only if requested by the scoring specification. Invalidate downstream comparisons that used substituted baselines until recalculated.

### F3 — P1: The current queue has competing answers

**Location:** Part 5 top snapshot, `GAME_LOG_STATUS_CURRENT.md`, README current-state table and current mini-log header.

The canonical summaries still point to the P-516-onward mini log and next ID P-518. The actual P-518-onward mini log contains P-518–P-522, claims the cohort is closed and gives P-523 next. The status file's opening paragraph also says P-509 was settled and, later in the same paragraph, that it is still live without cleanly isolating the historical assertion.

This is more than an old filename: a session trusting the documented next-ID source could reuse an already-issued ID. The mini log is not automatically authoritative merely because it is newer, particularly while its settlement evidence has defects.

**Fix proposed:** reconcile issue identity separately from settlement quality. Reserve all issued IDs immediately in the reconciliation plan, archive/hash the relevant variants, and update the canonical snapshot, status register and mini-log pointer together once identities are established. P-523 is the mini log's claimed next ID, not an ID reassigned by this review.

### F4 — P0: The extraction schema cannot enforce the scoring policy

**Location:** `research/settled_rows_2026-09-25/extract_settled_rows.py`, its CSV, `tools/calibration_report.py`, `tools/rank_model.py`, and `tools/evidence_status.py:rm1_gate`.

The CSV has 12 columns, but lacks event horizon, exact decision/target identity, push mass, issue-time preferred-side flag, q, baseline status, eligibility, control hash and source-availability times. Consequences are observable:

1. The calibration and RM-1 loaders use **p ≥ 0.5** as a proxy for selecting decisions. P-443's preferred Over 8 has W/P/L = **0.45/0.13/0.42**. It is a valid preferred target despite p(win) below 0.5, and this proxy drops it. Integer totals and three-way markets defeat the shortcut.
2. The calibration loader retains W/L rows and scores the unconditioned p, while discarding pushes. For P-443, the decisive probability should be **0.45/0.87 = 0.517241…**, as the scoring document already explains. The current aggregate therefore needs the existing **LEGACY_MIXED_DIAGNOSTIC** qualification; it is not the corrected decisive score.
3. A review-only extraction preview added **20 rows from all five new cards**, including **16 rows from four explicitly live-issued cards**: P-518, P-519, P-521 and P-522. The schema loses their horizon labels. Keeping live rows in a historical archive is fine; silently allowing them into a prospective pregame counter is not.
4. `rm1_gate` counts distinct card numbers at least 518 with p present. It does not establish pregame issue, valid settlement, frozen q or compatible controls. A rebuilt CSV can therefore advance the apparent prospective checkpoint without the required evidence.
5. The extractor uses last occurrence by `(card, rank)`. The retained conflict file shows P-036 rank 1 associated with both Twins ML and Phillies ML. These are not interchangeable records merely because they share a rank. The coverage file also records **72 unattributable dropped occurrences**; that is a parser count, not 72 proven unique lost decisions.

**Fix proposed:** use explicit event and decision keys, immutable issue fields, separate settlement revisions, eligibility flags and complete outcome vectors. Fail closed on conflicting identities. Build every diagnostic and checkpoint from a declared eligible view; do not repair missing historical values by guessing.

The [extraction preview](extraction_preview/README.md) is deliberately **not approved data for scoring or model fitting**.

### F5 — P1: Headline metrics mix denominators and overstate what calibration establishes

**Locations:** README current-state table; `CURRENT_RULES.md` around line 180; `LEARNINGS_INDEX.md:15`; calibration report.

Independent arithmetic on the unchanged committed CSV gives:

| Measurement | Denominator | Brier |
|---|---:|---:|
| All W/L rows with a probability | 639 rows / 155 cards | **0.226835** |
| Current p ≥ 0.5 decision proxy | 411 rows / 155 cards | **0.213098** |
| Same proxy, averaged within card then equally across cards | 155 cards | **0.227546** |

`LEARNINGS_INDEX.md` explicitly labels 0.2268 “Decision Brier.” The README places that number beside 411 decisions. The number is reproducible, but that denominator label is wrong. The latter two figures above are **diagnostic reconciliations of the existing proxy**, not recommended replacement performance estimates: F4 still applies.

The +6.6% figure is also reproducible against **the same sample's overall outcome frequency**, not against a frozen, competition/contract-matched baseline. The separate seed comparison is card Brier **0.2461** versus baseline **0.2360**, with a card-cluster interval spanning zero. It does not demonstrate that the card process is better or worse.

A slope near one is insufficient to conclude “calibration is good” across leagues, horizons, lines and probability bands. The report's Wilson band intervals and logistic slope standard error are not event-clustered, even though its slice-gap bootstrap is. The binned Murphy terms should also be labelled an approximation to the raw-score decomposition when distinct probabilities are grouped.

**Fix proposed:** give every metric an explicit population, unit, horizon, score version, weighting and comparator. Report paired event-level differences and suitable clustered uncertainty. Reserve “demonstrated skill” for the relevant prespecified comparison, not a favourable in-sample summary.

### F6 — P0: RM-1 values are not always a coherent set of event probabilities

**Location:** P-522 issued rows; `tools/rank_model.py` calibration and top-two statement.

Tenerife −3.5 and Zaragoza +9.5 cover every possible final margin. Therefore their win probabilities must satisfy:

`P(Tenerife −3.5 wins) + P(Zaragoza +9.5 wins) ≥ 1`.

The raw card probabilities do: **0.553 + 0.605 = 1.158**, compatible with the overlap. RM-1 produces **0.535 + 0.342 = 0.877**, which violates the lower bound. The CLI reproduces those numbers. They cannot simultaneously describe the same event distribution, even if each is a fitted row score.

This does **not** prove RM-1 is always a worse ranker, or justify removing it because two ACB picks lost. It establishes a mathematical limitation in describing q as the probability of each exact event. P-522 appropriately uses raw model p for its joint table; that distinction should be enforced everywhere.

There are two further presentation issues. P-519 receives `TOP2_STRONG` even though its flipped second row is explicitly capped at `SUPPORTED`: `top_two_statement` tests numeric q and ignores the cap. The CLI also prints independent products without knowing the pair's event geometry. Finally, P-520 reproduces the code's near-tied-flip ordering, so its non-descending numeric q order is **not a transcription error**; the documentation's “strict q order” description fails to explain the exception.

**Fix proposed:** distinguish experimental ranking scores from coherent joint probabilities, block impossible q probability claims, honour tier caps and derive dependence from the joint distribution or report bounds. Any change to the fitted ranking method must follow the existing freeze and validation process, not this cohort's results.

### F7 — P1: Some printed distributions do not reproduce their contract probabilities

**Location:** P-518 distribution parameters and outcome-family table.

P-518 declares a no-tie Normal margin with mean WSH +0.10 and SD 4.50, alongside a hand-written margin-family table giving Mets +1.5 = 0.640 and Nationals +1.5 = 0.635. Running the card's stated normal/no-zero queries gives approximately **0.5855 and 0.6039**, respectively. Those differences are too large to be rounding.

The family table is internally sum-consistent, but it is not the declared Normal marginal. The total query discrepancy is much smaller: negative binomial mean 10, SD 4.5 gives Over 8.5 about **0.5915**, versus 0.590 printed. The larger margin inconsistency is the substantive issue.

**Fix proposed:** choose one explicit authoritative distribution object and generate every marginal, family mass, probability, representative score and joint calculation from it. If a subjective mixture replaces a Normal model, describe that replacement rather than presenting both as the same calculation. Preserve historical issued values and append the discrepancy.

### F8 — P1: Source-count and retrospective claims exceed the evidence shown

**Location:** current mini-log settlements and general learnings.

- P-519's issued source uses AFLW event **8942**, while settlement cites **7412**. The freshly opened [official match centre](https://www.afl.com.au/aflw/matches/8942) confirms 69–39 for event 8942. The [official match report](https://www.afl.com.au/aflw/news/1623735/young-gold-coast-suns-turn-up-the-heat-against-winless-st-kilda-saints-despite-guns-return-to-form) confirms the quarter scores and lists injuries; the settlement says “Disruption facts: None.” The effect of those injuries on the forecast is not established.
- P-522 issues against ACB ID **105380**, then cites **105379** at settlement. Its issued narrative names Jaka Lakovic as Tenerife coach; the retrospective attributes the result to Txus Vidorreta. These are unresolved identity/process contradictions, not a basis for choosing whichever narrative sounds plausible.
- P-521 and P-522 count the ACB official site and ACB live statistics as separate lineages. They have not demonstrated three independent upstream lineages. Multiple presentations of the same official data count once under the repository's own rule.
- P-522 says none of its pre-event kill paths fired, even though the card explicitly named T≤169 and Tenerife margin≤3; its recorded total 161 and margin −1 satisfy both. This contradiction exists even before external re-verification of that final.
- The ACB retrospective describes winning raw probabilities as “completely accurate,” declares a systemic model pathology from two results, and recommends specific basketball widths (+15%), total centres and spread exemptions. A binary outcome does not reveal a forecast's true probability. Two games do not establish bimodality or estimate a universal width increase. A `TESTING` label does not neutralise nearby imperative wording saying the change “must” be applied.

**Fix proposed:** recheck exact event IDs, retain source extracts and field ownership, distinguish observed facts from hypotheses, and turn proposed predictive changes into genuine frozen tests. Do not import the current causal narratives or coefficients into active rules.

### F9 — P1: Prospective measurement exists mostly as infrastructure

The live evidence-status tool reports:

| Gate | Recorded progress at review |
|---|---|
| Baseline comparison | **0 decisions / 0 cards**, against the 100-decision / 30-card checkpoint |
| RM-1 prospective | **0 cards in the currently committed dataset**; the counter has F4's eligibility weakness |
| Post-settlement market benchmark | **0 decisions / 0 cards** |
| Event universe | **1 declaration, 12 events, 0 carded, 0 skipped** |
| MLB shadow | **0 frozen / 0 settled** |
| Other-sport shadow | **0 frozen rows** |
| Predictive rule freeze | **In force** |

This is an operational bottleneck, not evidence of a losing model. Four of the five newest cards explicitly missed pregame issuance. Several selected leagues have no automated shadow or registered baseline route. Consequently, substantial research effort can produce detailed records without advancing the actual evaluation.

**Fix proposed:** start with a manageable, declared population in a supported lane; prepare static research before the late lineup window; freeze, publish and record the shadow before actual start; account for every selected or skipped event. Preserve live cards as live. Never backdate the universe, baseline or forecast to manufacture prospective progress.

### F10 — P1/P2: Document history and current authority remain too entangled

`CURRENT_RULES.md` has **401 lines / about 6,665 words**, despite being described as a one-page entry point. `RULES_GENERAL.md` has about **41,480 words**, `LEARNING_REGISTER.md` about **47,045**, and the full source register about **22,525**. Length is not inherently a defect; repeatedly rediscovering precedence is.

Examples of current-state drift include the README's early claim that no forecasting model has been fitted and validated, followed later by historical A0/A1 model results; sport headers saying no model is fitted despite reduced-feature shadow builds; and numerical-register/program sections that still say NBL was not validated although later predictability work contains an NBL comparison. These can be reconciled by distinguishing **implemented**, **historically evaluated**, **prospectively evaluated** and **approved for forecasting**.

The historical settled-row README also retains “clear skill” and an independence recommendation based on aggregate top-two failure frequency, while later caveats narrow those conclusions. Population-average agreement with independence does not establish independence for a particular card.

**Fix proposed:** maintain one current status table and one compact live workflow, with explicit links to historical rationale. Generate repeated metrics and state summaries. Preserve dated evidence, but visually separate superseded claims so they cannot be mistaken for live instructions.

## 5. Review by document family

| Family | Main assessment | Required next action |
|---|---|---|
| METHOD, CONTROLS, CURRENT_RULES, agent role, preflight, research/logging guides | Strong lifecycle; duplicated obligations and rules that are incompletely enforced | One executable issue/settlement contract and a genuinely compact current workflow |
| SCORING_AND_VALIDATION, eligibility policy, baseline/market ledgers | Good mathematical authority; implementations and headline labels diverge | Implement explicit target identity, push conditioning, event weights and eligible cohorts |
| Five combined logs, status files, active mini log | Valuable immutable history; current custody and process errors are material | Reconcile IDs and exact events, append sourced corrections, regenerate views |
| SOURCES and DATA_SOURCE_REGISTER | Thoughtful per-field policy; printed source lists are weaker than actual receipts | Store exact-event evidence and upstream lineage mappings |
| Ten RULES sport modules and cricket/soccer league supplements | Necessary endpoint/format safeguards; historical calibration claims are often too broad | Verify competition/era when used; separate live gates from historical observations |
| BASE_RATES and RECENCY_AND_REBOUND | Useful empirical anchors and resistance to streak narratives | Require exact competition/endpoint/time validity; preserve null baselines and uncertainty |
| Model/data specification, training spec, implementation recipes, H0, numerical program/register, algorithm portfolio | Extensive and useful design; research builds have outgrown some status prose | One capability/status register, exact data admission and reproducible chronological evaluation |
| LEARNING_REGISTER, LEARNINGS_INDEX, research READMEs, CHANGELOG | Good failure retention and candidate closure; some hindsight narrative survives | Evidence-linked dispositions, controlled wording and preregistered tests |

Sport-specific priorities are also different. Baseball needs starter/process receipts and coherent margin modelling; basketball needs rule/roster freshness and honest RM-1 scope; AFLW must retain its own population; cricket needs innings/phase and chase-censoring distinctions; tennis needs format/retirement and reliable chronology. Sparse hockey/rugby and unvalidated competitions should not inherit stronger claims from better-covered leagues. These are priorities for implementing existing safeguards, not newly fitted predictive rules.

## 6. Verification scorecards

Counts below are scoped inventory counts, not universal accuracy percentages. Categories overlap and must not be added. “0/N” means no defect observed in that specific check; it does not verify the underlying sporting outcomes. Where a full denominator is not established it is stated as unknown.

### Document usefulness and quality

| Category | Observed defects | Assessment |
|---|---|---|
| Usefulness and completeness | Total unknown | All eight major families mapped; prospective evidence and reliable machine-readable records are the principal missing capabilities. |
| Analytical clarity | 3 / 3 headline summaries checked | README, CURRENT_RULES and LEARNINGS_INDEX associate the all-row Brier with the decision cohort; see F5. |
| Visual and interaction consistency | N/A | Markdown document review, not an interactive dashboard. Historical prose and navigation were sampled; no full rendered audit of every source document. |

### Analytical correctness and robustness

| Category | Observed defects | Assessment |
|---|---|---|
| Source authority and confidence | 4 / 5 current settlement blocks | P-518 process contradiction; P-519 wrong event reference; P-521 duplicated lineage; P-522 identity/lineage conflicts. P-520 not independently re-settled. |
| Calculation accuracy | 0 / 40 ranked-row Brier cells | Arithmetic matches printed p/q and claimed W/L outcomes within printed precision. This does not approve outcomes, eligibility or the probability model. |
| Distribution/probability agreement | 3 / 5 current cards | P-518 margin mismatch; P-519 top-two label ignores a tier cap; P-522 covering-pair q violates probability geometry. These are distinct failures, not three identical defects. |
| Complete source details | Total unknown | Exact-event URLs and timestamps exist in places, but generic portal references and unverified independence remain. |
| Cross-artifact consistency | 3 / 4 queue surfaces | Part 5, status register and README lag the issued-card inventory; the mini log itself still requires evidence reconciliation. |
| Data-quality controls | 20 / 20 current baseline cells | Settlement comparison changes a frozen value or missingness label in every ranked row. |
| Conclusion support | Total unknown | Historical model claims have useful caveats; current ACB causal and probability-certainty claims are unsupported. |

## 7. Correct path forward

The immediate task is to make the existing system tell the truth consistently: correct source-backed process records, preserve frozen fields, reconcile custody, implement the scoring specification and block impossible probability claims. Then accumulate a clean prospective cohort with declared selection and frozen comparators.

Use [the repair plan](SPORTS_RESEARCH_REPAIR_PLAN.md) as the implementation checklist. A later review should award higher marks for completed acceptance checks and reproducible evidence, rather than further revisions of prose. Passing a checkpoint permits an evaluation; it does not guarantee a positive result.

## 8. Reproduction and methodological references

Run `python reviews/2026-09-28/audit_evidence.py` from the repository root to reproduce the inventory, CSV arithmetic, active-table joins and Brier-cell checks. It writes only the review's derived JSON. The separate extraction preview was generated by importing the existing extractor and redirecting its output directory; it does not replace the committed dataset.

The statistical recommendations use proper probability scoring and chronological evaluation. Proper scores assess probability distributions rather than whether a single selected outcome happened to win; see [Gneiting and Raftery, 2007](https://sites.stat.washington.edu/people/raftery/Research/PDF/Gneiting2007jasa.pdf). Model selection must be separated from evaluation, and ordinary random folds are inappropriate substitutes for temporal tests when data are time-dependent; see the official [nested cross-validation guide](https://scikit-learn.org/stable/auto_examples/model_selection/plot_nested_cross_validation_iris.html) and [cross-validation documentation](https://scikit-learn.org/stable/modules/cross_validation.html). These references support the evaluation principles, not any claim that a particular sports model will improve.
