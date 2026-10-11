# Current operating rules

**MDS-2026.10.11-v10.0 · CR-2026.10.11-R1 · SCV-2026.10.11-v6.** Effective for new work after this revision is read. Current IDs and destination: [CURRENT_STATE.md](CURRENT_STATE.md). [Previous rules](archive/superseded_2026-10-11/prompt_v10/CURRENT_RULES.md) remain historical evidence.

## 0. Authority, scope and honest execution

The framework remains Markdown, CSV and text. Read files, browse permitted sporting sources, use transparent arithmetic and plain file/git tools. Do not add scripts, code, JSON, notebooks or workflows. Do not claim an exact grid, simulation, model fit, calculation, file write, readback or scheduled capture unless actually performed.

Latest user instructions control task scope. In the local repository, current working files govern, with branch/HEAD and relevant uncommitted differences disclosed; GitHub main is the publication surface. An external agent reads one pinned current-main revision. Neither silently changes branches, pulls over dirty work, nor assumes a stale download is current.

Precedence: user instruction; these operating rules and current state for their respective domains; selection/scoring/templates; sport and league rules; historical examples/learning notes. Sport-specific physical rules and actual competition conditions must be verified, not overridden by a generic no-draw assumption. Report substantive contradictions. Continue independent research when a conflict blocks only issuance/import. Never resolve an identity or ID collision by guessing.

## 1. Reading gate

Every task opens CURRENT_STATE, METHOD, CURRENT_RULES, SELECTION_RULES, CARD_AND_LOG_TEMPLATES and its own prompt. Print the receipt in [the prompt index](research/prompts/README.md): exact paths/sections read, revision, time with offset, missing required files and source of authority. Claim full reading only when full text was read.

Cards also read the applicable sport/league rules, ARCHIVE_USE_GUIDE, relevant SOURCES routes, PROBABILITY_TOOLKIT sections, profile/base-rate rows, active mini, status register and relevant canonical records. Settlement adds scoring and original card/contract evidence. Import, rollover and retrospective add VERIFICATION_PROTOCOL; retrospective adds current hypotheses and latest completed retrospective. Prompt 7 adds coverage/schema/source notes; prompt 8 adds contribution rules, changelog and affected dependencies.

Unavailable required control files block the dependent mutation; missing sporting data is recorded and does not justify inventing it. Cite the rule or source next to any value it shaped. Every card prints its archive coverage, actual files/rows/date range inspected, cutoff filter, findings and gaps. Inspect current files: an old claim that a league is header-only is not a live check.

## 2. Rule T2: frozen top two and transparent denominators

Only the original Rank 1 and Rank 2 can count as primary wins. At most four supported candidates are retained; ranks 3–4 and shadow selections stay informational. A missing second pick is not manufactured. Never replace a losing primary with a winning alternate or reforecast.

Report W/L/PUSH/VOID/UNRESOLVED separately, number of requested events, retained cards, numeric/qualitative/NO_FORECAST cards and scoring coverage. WIN/(WIN+LOSS) is conditional on resolved decisive outcomes and must not hide unresolved cases. Missing evidence is not VOID. Dependent rows do not become independent trials. Mechanically protected pairs require an explicit label; Hit@2 is then a construction diagnostic, not predictive skill. Exact definitions: [SCORING_AND_VALIDATION.md](SCORING_AND_VALIDATION.md).

## 3. Rule R1: outcome review without hindsight

Every settled Rank-1 LOSS receives eight parts: exact claim; verified outcome; original-distribution check; cutoff knowability; process/model/variance assessment; cutoff-only counterfactual; failure class; testable correction. Keep R1–R12 for every terminal card, including wins and partial settlements, with unavailable sections marked and explained.

Do not invent numeric blame percentages. A single tail loss neither proves miscalibration nor vindicates a distribution. Process is SOUND, DEFICIENT or NOT_ASSESSABLE with evidence; uncalibrated status is reported separately. Review matched wins for the same defects. Counterfactuals are diagnostic and never replace frozen ranks or join prospective cohorts.

## 4. Rule P4: event first, reproducible selection

Supplied contracts are reference propositions, not privileged selections. Freeze the candidate-generation recipe, endpoints, standard ladder and exclusions before inspecting their probabilities. Price all supported supplied rows and the declared derived slate from one coherent event model. Keep every supplied row's disposition; do not erase a difficult line or keep moving lines until a gate passes.

The primary slate follows [SELECTION_RULES](SELECTION_RULES.md): decreasing p_card, deterministic ties, at most four rows. Family constraints are declared eligibility filters. Joint dependence is disclosed, not used to silently reorder primary ranks. Different-quantity and diversification alternatives are explicitly frozen shadow selections. Rank-1 gate constants remain provisional; the alternative-quantity gate is a shadow, not a replacement. Record candidate quantity, family, line and endpoint so comparisons cannot disguise easier propositions as better predictions.

## 5. Sources, event state and time

SPORTS_ONLY / MARKET_BLIND: exclude odds, line movement, tips, betting previews, prediction markets and fantasy inputs. User-supplied thresholds are contract metadata. Do not claim value, edge or staking advice from this framework.

Confirm competition, season, stage, participants, venue, native event ID or labelled stable surrogate, scheduled time, timezone and official observed state. An event key includes competition/season/native ID or surrogate/date; a reschedule is an alias update under the original identity, not automatically a new event. Doubleheaders require game number or native ID. Search all relevant minis and Combined Logs, not just headers.

Use official field owners then structured providers and quality corroboration. Record URL, exact field/value, source update/publication time when available, retrieval time, short lawful quotation or faithful extract, fallback/failure and collector lineage (UNKNOWN if unknown). Domain count is not independent-source count. Retain decisive evidence as Markdown/text within allowed scope. A quotation and git commit do not prove pregame availability by themselves.

Record cutoff, research completion, actual write/issue time and final state recheck separately. Inputs must be demonstrably available by cutoff. Recheck just before issue; crossing the start changes the timing label. PREGAME requires explicit not-started evidence; stale 0–0 is insufficient. LIVE_OBSERVED, LATE_START_UNVERIFIED and HISTORICAL_DIAGNOSTIC stay separate. Outcome exposure is disclosed; a historical reconstruction cannot regain pregame status. Current event information may establish identity/state but observed in-game outcomes never enter a purported pregame forecast.

Also record scheduled lead time at issue. Within five minutes of scheduled start or later is the LATE_START monitoring band, even if an official delay confirms PREGAME. This band does not suppress requested research. Actual-start evidence is a separate field and may remain NOT_VERIFIED. Provider/capture plans are not scheduled jobs: state who will capture and whether automation actually exists.

## 6. Requested research and missingness

Deliver and retain requested research independently of certification. If a distribution can be honestly computed, use UNCALIBRATED_ANALYST_SCENARIO. Otherwise use UNCALIBRATED_QUALITATIVE with p_card NOT_ESTIMATED and a supported qualitative ordering, or NO_FORECAST when identity/evidence cannot support a direction. Explain the missing inputs and next action. Never fabricate four rows, a probability, SD, baseline or source to satisfy a template.

Missing baseline, calibration or fitted model does not prevent research logging. Unsupported numeric fields stay NOT_COMPUTED, unavailable facts NOT_VERIFIED, undefined contract terms UNKNOWN_DEFINITION, and structurally irrelevant fields N/A. Numeric zero is data, not missingness. Qualitative ranks receive no numerical gate PASS or proper score.

## 7. Distribution, baseline and uncertainty

Print model family, endpoint, parameters, input provenance, arithmetic and approximation limits. Marginals must come from compatible joint/conditional constructions. Separate supported auxiliary counts (corners, players) explicitly; without a joint model, report bounds rather than an exact cross-family joint. Do not label an unexecuted point/drive/ball enumeration exact.

Retain unconditional win/push/loss/void masses and p_card = W/(W+L) where W+L > 0. Preserve allowed draws/ties; resolve OT/ET/SO/extras only when the exact competition/contract does. Full result masses sum to one within declared rounding tolerance. Do not clip a probability to the 90% selection ceiling; exclude it from the ranked slate and retain its actual value diagnostically. Tail truncation, covariance and score means/SDs must be reproducible.

Every numeric candidate attempts a frozen BASELINE_P on the identical proposition/line/endpoint, using the league-only recipe in SELECTION_RULES §9. Missing comparator remains missing. Baseline provenance and cutoff are retained; no backfill after results. No fitted model currently exists.

List every analyst adjustment and avoid double-counting effects already in data. Print adjusted and unadjusted top two whenever any adjustment changes them, regardless of size. Flag ADJUSTMENT_DEPENDENT for any such change, and LARGE_ADJUSTMENT separately above 0.25 SD. Test plausible low/base/high assumptions for the most uncertain inputs and show p/rank/gate changes. These are sensitivity ranges, not confidence intervals unless an interval method was actually applied. Uncertain lineups need explicit scenarios/weights or an honest nonnumeric assessment; uncertainty does not always mean widening a distribution without moving its centre.

## 8. Mini lifecycle and settlement

New formats: mini-log-6 and mini-settlement-5; existing formats finish unchanged. Start (2), append card (1), freeze and settle (3), import (4), rollover if needed (5), retrospective (6), repair archive (7), change framework (8). Creating a mini or rollover consumes no ID. Local working P-IDs are permanent references but not canonical until verified import; a contiguous outstanding mini sequence must be accounted for before further allocation. Never reuse P-518–P-522 or silently skip/renumber.

Carry both PENDING_EVENT and terminal UNRESOLVED_EVIDENCE cases in separate queues with original IDs. The five-event open cap and 72-hour final-to-review target are alerts, never instructions to discard work or force grades. Use verified final time; if absent, mark clock UNKNOWN and use scheduled-duration estimate only for triage. Capture fragile fields promptly, normally within 36 hours after scheduled start, adjusted explicitly for delays and multi-day formats. Do not claim capture took place when only a due time exists.

Settle the frozen contract. WIN/LOSS/PUSH require sufficient evidence; VOID requires the frozen void condition; missing/conflicting field or definition yields UNRESOLVED. Evidence C may support a provisional sporting assessment but unresolved conflicts remain visible. A bounded value yields a definite grade only if every feasible value gives that grade. Frozen framework convention and operator settlement are distinct: a sporting result under a convention does not prove an unknown operator result.

For KBO, try the official terminal box score promptly. If stale, retain the available result and arrange/report a retry after about 12 hours, within the review SLA where possible. A promised retry is not a completed fetch. Source corrections append a dated revision; they never silently replace earlier grades.

## 9. Custody, current state and publication

Issued card cores, previous log parts, existing settled minis and dated reports are immutable. Append corrections with reason, timestamp, parent ID and superseded revision pointer. Freeze an exact file copy before settlement; compare actual bytes/prefix, not just line counts. Preserve line endings. Zero deleted lines in numstat alone does not prove append-only: compare the complete original prefix and inspect hunk locations.

The active log's opening header is an opening snapshot and may retain old IDs/method text. Resolve current state from CURRENT_STATE, the current status-register section and canonical entries plus dated state/rollover addenda. A stale opening snapshot is not itself a custody conflict. A disagreement in current records is a blocker. Do not run retired tools named in historical log headers.

Imports reconcile every card, carryover, addendum and settlement, including already-imported cards with missing new addenda. All imported cores receive full readback; no three-card spot check substitutes for completeness. Partial imports resume by exact block comparison; mismatch stops before further mutations. Closed-source status requires a verified destination or explicit retained disposition for every source block. Never delete originals automatically.

Stage exact intended paths, preserve unrelated work, commit/push only when authorized by the invoked task, never force. Fetch and verify the remote ref and committed artifacts before claiming publication. A HEAD SHA records repository contents, not proof of a local card's pregame timestamp.

## 10. Learning and claims

Every record remains RESEARCH_ONLY_NOT_CERTIFIED. Model quality, numerical coherence, calibration, predictive skill, operational readiness and record custody are separate questions. Measure proper scores against frozen same-row baselines, coverage and expected-score errors; do not optimize headline win rate by line choice or excluding unresolved losses. Historical climatology is descriptive, not a prospective baseline.

Use chronological development, tuning, calibration and untouched test/future shadow separation when designing fitted work. Current Markdown controls do not restore the removed runtime. Thresholds and new shadows are untested; eight weeks or a small sample minimum is not proof of power or promotion. See [HYPOTHESIS_REGISTER](HYPOTHESIS_REGISTER.md) and the [implementation roadmap](research/verification/framework_change_2026-10-11-1/IMPLEMENTATION.md).

## 11. Change control

Prompt 8 records the user instruction or finding, class, archived originals, dependencies, version changes, verification and publication. A user-authorized process repair can be implemented without pretending a statistical experiment passed. Behavioral selection/model hypotheses need separate frozen tests; preserve the original registration and append versioned amendments. Update rules, prompts, templates, examples, scoring and receipt definitions together. Do not revise historical values under a new scoring convention without a separate labelled diagnostic view.

## 12. Navigation

[Prompts](research/prompts/README.md) · [Templates](CARD_AND_LOG_TEMPLATES.md) · [Selection](SELECTION_RULES.md) · [Scoring](SCORING_AND_VALIDATION.md) · [Verification](VERIFICATION_PROTOCOL.md) · [Sources](SOURCES.md) · [Archive guide](ARCHIVE_USE_GUIDE.md).
