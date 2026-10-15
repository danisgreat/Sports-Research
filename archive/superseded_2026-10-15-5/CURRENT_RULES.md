# Current operating rules

**MDS-2026.10.15-v15.0 · CR-2026.10.15-R4 · SCV-2026.10.15-v10 · SEL-2026.10.12-v3.** Effective for new work after this revision is read. Current IDs and destination: [CURRENT_STATE.md](CURRENT_STATE.md). Previous rules remain historical evidence: [CR-2026.10.15-R3](archive/superseded_2026-10-15-4/CURRENT_RULES.md), [CR-2026.10.15-R2](archive/superseded_2026-10-15-3/CURRENT_RULES.md), [CR-2026.10.14-R2](archive/superseded_2026-10-14-5/CURRENT_RULES.md), [CR-2026.10.14-R1](archive/superseded_2026-10-14-4/CURRENT_RULES.md), [CR-2026.10.12-R2](archive/superseded_2026-10-14-3/CURRENT_RULES.md), [v11.0 CR-R1](archive/superseded_2026-10-12/CURRENT_RULES_v11.0_CR-R1.md), [v10.0](archive/superseded_2026-10-12/CURRENT_RULES.md), [pre-v10](archive/superseded_2026-10-11/prompt_v10/CURRENT_RULES.md).

## 0. Authority, scope and honest execution

The framework remains Markdown, CSV and text. Read files, browse permitted sporting sources, use transparent arithmetic and plain file/git tools. Do not add scripts, code, JSON, notebooks or workflows to the repository, except inside the model workshop below. A helper used outside it is disclosed, and its rules are written out in prose (CONTRIBUTING). Do not claim an exact grid, simulation, model fit, calculation, file write, readback or scheduled capture unless actually performed.

**Model workshop exception (owner instruction 2026-10-14; [framework change 2026-10-14-3](research/verification/framework_change_2026-10-14-3/IMPLEMENTATION.md)).**
- **Where code may live.** Python source, its tests and its `requirements.txt` may exist only under `ml/`. No JSON, notebooks, pickles, workflows or binaries anywhere, `ml/` included.
- **Who uses it.** Under the owner-authorised [PRIMARY_PREDICTION_PROTOCOL](PRIMARY_PREDICTION_PROTOCOL.md), prompts 1–3 may run/read the named market-free primary model/receipt/feedback lane. Primary probabilities use its actual fitted expert distributions, combined by the full-information sporting mixture (PRIMARY_HEDGE_MIX_V3). Other development artifacts and the market decision lab remain excluded; unsupported runs never produce invented numeric primaries.
- **What it may write.** Markdown and market-free CSV under the named `research/primary_predictions/` event bundle/input folder and `research/model_shadow/`; explicitly declared parameter admission Markdown/CSV under `research/primary_policy/`, each carrying a receipt: code SHA-256, archive snapshot SHA-256, repository HEAD and run time.
- **Honesty.** A file there claims only what the code actually computed. A model's status is set by the rules in `research/model_shadow/README.md`; this owner instruction authorises EXPERIMENTAL_PRIMARY_NOT_CERTIFIED, not qualification of old artifacts or production performance.

**One authority mode per run (R09).** Latest user instructions control task scope. Each run prints exactly one mode in its reading receipt and never mixes revisions silently:
- `PUBLISHED_MAIN_PINNED` is the default for prompts 1–3 and for any agent outside the repository. Read every control from one commit of `origin/main`, print its full SHA, and use only that commit's files. Local edits do not apply.
- `LOCAL_WORKING_TREE` applies only to a run inside the repository whose user asks for local controls, or to prompts 4–8, which mutate the repository. Print branch, HEAD and every uncommitted difference to a control file. Those working files govern this run only, and the receipt names them.

Where the published and local versions of a control differ, the receipt lists the difference and says which one was applied. Neither mode silently changes branches, pulls over dirty work, or assumes a stale download is current.

Precedence: user instruction; these operating rules and current state for their respective domains; selection/scoring/templates; sport and league rules; historical examples/learning notes. Sport-specific physical rules and actual competition conditions must be verified, not overridden by a generic no-draw assumption. Report substantive contradictions. Continue independent research when a conflict blocks only issuance/import. Never resolve an identity or ID collision by guessing.

## 1. Reading gate

**Prompt lifecycle (P-2026.10.15-v14.0).** Every task reads [COMMON_OPERATING_PROTOCOL](research/prompts/COMMON_OPERATING_PROTOCOL.md) and its complete selected prompt. Prompt 1 retains eleven standalone sport/general workflows and their own inactive Upcoming game blocks. New primary cards are model-assisted under PRIMARY_PREDICTION_PROTOCOL; independent sporting shadows stay separately labelled; only verified receipts and matching settled endpoints support prospective comparisons in prompts 3/6. Prompt 8 requires tests, recoverable generating-code/data identities, actual runs and explicit qualification decisions. Tests/development results do not promote models, and the decision lab never enters card learning.

Every task opens CURRENT_STATE, METHOD, CURRENT_RULES, SELECTION_RULES, CARD_AND_LOG_TEMPLATES and its own prompt. Print the receipt in [the prompt index](research/prompts/README.md): exact paths/sections read, revision, time with offset, missing required files and source of authority. Claim full reading only when full text was read.

Cards also read the applicable sport/league rules, ARCHIVE_USE_GUIDE, relevant SOURCES routes, PROBABILITY_TOOLKIT sections, profile/base-rate rows, active mini, status register and relevant canonical records. Settlement adds scoring and original card/contract evidence. Import, rollover and retrospective add VERIFICATION_PROTOCOL; retrospective adds current hypotheses and latest completed retrospective. Prompt 7 adds coverage/schema/source notes; prompt 8 adds contribution rules, changelog and affected dependencies.

**Primary-model reading/execution gate (owner instruction 15 October 2026).** Read and use only the declared source-reviewed primary runtime/bundle and sporting feedback under PRIMARY_PREDICTION_PROTOCOL. The former blanket exclusion is superseded for this lane. Historical/generated DATA_HOLD outputs cannot substitute for a new per-event run; ordinary shadows remain separately admitted. The market/DECISION_LAB folder remains outside card reading/learning.

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

**§5a. Decision-lab firewall (owner instruction 2026-10-14).** `ml/decision/` may run a paper-only, historical study of staking policies (fractional Kelly, contextual bandits) on prices held in the local, git-excluded benchmark capture. It commits aggregate tables only, under `research/model_shadow/DECISION_LAB/`, never a price or a price-derived row. Nothing it produces is betting advice, a value claim or an input to any card, rule, rank, width or learning disposition, and the MARKET_BLIND rule above is unchanged for all research. Online in-play betting is prohibited in Australia under the Interactive Gambling Act 2001, so no live or in-play automation is built.

Confirm competition, season, stage, participants, venue, native event ID or labelled stable surrogate, scheduled time, timezone and official observed state. An event key includes competition/season/native ID or surrogate/date; a reschedule is an alias update under the original identity, not automatically a new event. Doubleheaders require game number or native ID. Search all relevant minis and Combined Logs, not just headers.

Use official field owners then structured providers and quality corroboration. Record URL, exact field/value, source update/publication time when available, retrieval time, short lawful quotation or faithful extract, fallback/failure and collector lineage (UNKNOWN if unknown). Domain count is not independent-source count. Retain decisive evidence as Markdown/text within allowed scope. A quotation and git commit do not prove pregame availability by themselves.

[TIMING_RESEARCH_PROTOCOL](TIMING_RESEARCH_PROTOCOL.md) governs manual research completion and timing. Continue comprehensive research until complete, even after scheduled or actual start; no fixed lead time forces freezing, issuance or abandonment. The evidence horizon is the game-log scheduled start: there is no separate cutoff, and lineups, confirmed starters, bench and news are researched up until then (it moves earlier only to an earlier actual issue or verified earlier first play). Record the horizon, retrieval, research completion, final availability check, actual issue and actual-event state separately. PREGAME describes verified not-started issuance, at any lead; a delayed start may allow PREGAME after the advertised time. CLEAN_PRE_START_INPUTS describes independently evidenced pre-start inputs and no live/final target-outcome exposure; it may accompany POST_START_ISSUE, which remains a separate descriptive cohort, never a claim of pre-start release. Unverified start/source timing stays TIMING_UNVERIFIED/KNOWN_AT_UNVERIFIED; observed live/final outcomes make the work LIVE_OBSERVED/HISTORICAL_DIAGNOSTIC. Do not backdate or revise old labels. A stale 0–0 does not prove the event has not started.

**§5b. Comprehensive availability research (AVAIL-2026.10.15-v2).** Every game card applies [ROSTER_AVAILABILITY_PROTOCOL](ROSTER_AVAILABILITY_PROTOCOL.md) §§1–6 and [SOURCES §3.11](SOURCES.md#311-field-fallback-and-official-social-use-by-sport). Confirm both sides' exact starters/starting role and selected bench/replacements separately from current injury, illness, suspension and absence evidence. A roster, probable pitcher, predicted XI, depth chart or projected goalie is not confirmation. Complete official exact-match/team-sheet, both clubs, medical/eligibility/discipline, permitted structured fallback and local-language discovery for missing fields; obscure competitions require their actual organizer/federation and both teams, not a major-league substitute. Record actual attempts and decisive evidence/times in the existing Evidence receipt/A3/A8 and lineup-state metadata; C20 checks completion. Recheck the actual release window and immediately before freeze, then re-price changed inputs. No injuries found does not mean no injuries. A full starting side does not establish the bench or expected minutes/workload. A source failure is not proof of non-publication. After comprehensive research, genuine publication/access/conflict gaps remain explicit; unsupported material scenarios use qualitative/NO_FORECAST handling. An incomplete search cannot pass the process audit, and no rule guarantees publication by a universal deadline. A user's explicit only-confirmed issuance constraint is honoured without dropping the research request or inventing confirmation.

**Research completion workflow (PR-04 revision, owner instruction 15 October 2026).**
1. Complete identity, authority, every applicable availability route, sporting/archive inputs, coherent distribution, exact contracts/candidate recipe, baseline attempt, sensitivity and actual audit. There is no countdown deadline; continue after play starts if needed.
2. The pre-start evidence horizon is the game-log scheduled start (or an earlier actual issue / verified first play), never an earlier chosen cutoff. Retrieve later if necessary, but admit only field-level values demonstrably published by that horizon and before the actual start. A later current page, lineup release, live participation or final game book cannot prove its pre-start value by itself. Record any outcome exposure immediately.
3. When the research is complete, perform the final availability/source-state recheck, re-price permitted changed inputs once, freeze the completed issued card and write/read it back. Freeze protects that completed original; it is not an advance deadline. New evidence after issue is a dated addendum/reforecast, never an edit to original ranks/probabilities.

Complete the source escalation before calling a lineup unavailable. If genuine material gaps remain, record side/field, actual attempts and next manual check; retain a supported mixture labelled LINEUP_UNCONFIRMED, or qualitative/NO_FORECAST when states/weights are unsupported. A clean pre-start-input claim requires the proof in the timing protocol, not merely the analyst's intent or absence of an intentionally opened scoreboard. An explicit user time/only-confirmed constraint is honoured, with unmet constraints recorded truthfully.

**Known-at time (R28).** An input enters a pregame card only if it was available by the card's cutoff, which is the game-log scheduled start (TIMING_RESEARCH_PROTOCOL §1); there is no separate earlier cutoff. A historical row's game date is not its availability time. Archive rows are retrospective compilations: print the capture date, and treat a late correction or late-published statistic as known only from its correction time. If that is unknown, label the input `KNOWN_AT_UNVERIFIED` and keep it out of anything that decides Rank 1. Full-season aggregates and corrected datasets are separate snapshots from what was known on the day.

## 6. Requested research and missingness

Deliver and retain requested research independently of certification. New numeric primary cards use MODEL_ASSISTED_PRIMARY_V3 / EXPERIMENTAL_PRIMARY_NOT_CERTIFIED and an actual runtime bundle. UNCALIBRATED_ANALYST_SCENARIO describes historical/manual comparison work only, explicitly requested and separately labelled. Otherwise use UNCALIBRATED_QUALITATIVE with p_card NOT_ESTIMATED and a supported qualitative ordering, or NO_FORECAST when identity/evidence cannot support a direction. Explain the missing inputs and next action. Never fabricate four rows, a probability, SD, baseline or source to satisfy a template.

Missing baseline, calibration or fitted model does not prevent research logging. Unsupported numeric fields stay NOT_COMPUTED, unavailable facts NOT_VERIFIED, undefined contract terms UNKNOWN_DEFINITION, and structurally irrelevant fields N/A. Numeric zero is data, not missingness. Qualitative ranks receive no numerical gate PASS or proper score.

## 7. Distribution, baseline and uncertainty

Print model family, endpoint, parameters, input provenance, arithmetic and approximation limits. Marginals must come from compatible joint/conditional constructions. Separate supported auxiliary counts (corners, players) explicitly; without a joint model, report bounds rather than an exact cross-family joint. Do not label an unexecuted point/drive/ball enumeration exact.

Retain unconditional win/push/loss/void masses and p_card = W/(W+L) where W+L > 0. Preserve allowed draws/ties; resolve OT/ET/SO/extras only when the exact competition/contract does. Full result masses sum to one within declared rounding tolerance. Do not clip a probability to the 90% selection ceiling; exclude it from the ranked slate and retain its actual value diagnostically. Tail truncation, covariance and score means/SDs must be reproducible.

Every numeric candidate attempts a frozen BASELINE_P on the identical proposition/line/endpoint, using the league-only recipe in SELECTION_RULES §9. Missing comparator remains missing. Baseline provenance and cutoff are retained; no backfill after results. New primary cards use the actual fitted per-event ML/RL bundle under PRIMARY_PREDICTION_PROTOCOL; older workshop outputs retain their development/shadow status and cannot be substituted.

**New ML/RL primary pricing:** the selected retained score grid is the numerical source. No manual mixture, adjustment or form-rate overwrite may silently replace it. Unsupported material lineup/weather/regime effects mean qualitative/NO_FORECAST until a versioned scenario adapter actually runs. The following analyst mixture/adjustment procedure remains for explicitly requested manual comparisons and historical interpretation, not an alternative numerical primary. List every analyst adjustment and avoid double-counting effects already in data. Print adjusted and unadjusted top two whenever any adjustment changes them, regardless of size. Flag ADJUSTMENT_DEPENDENT for any such change, and LARGE_ADJUSTMENT separately above 0.25 SD. Test plausible low/base/high assumptions for the most uncertain inputs and show p/rank/gate changes. These are sensitivity ranges, not confidence intervals unless an interval method was actually applied. Uncertain lineups need explicit scenarios/weights or an honest nonnumeric assessment; uncertainty does not always mean widening a distribution without moving its centre.

**Price the uncertainty you disclose (PR-03; SEL-2026.10.12-v3).**
- **When it applies:** the card labels an input unfitted, stale, early-season, unconfirmed or `LINEUP_UNCONFIRMED`, and runs a low/base/high case on it.
- **Historical/manual scenario distribution:** the declared mixture of those cases, default weights 0.25/0.50/0.25. Different weights need a stated basis, frozen before pricing. Every row's p_card, the gate and the ranks come from the mixture.
- **Shadow:** the base-case-only p is printed beside each row as `p_base` (shadow `SHADOW_BASE_ONLY`). It never counts as a primary result.
- **Tails:** a mixture widens the tails honestly. Do not then move the line to recover a higher p: the candidate recipe is frozen first (§4).

**Recent form: four windows, one rate (PR-01).**
- **Windows:** every numeric team-sport card reads each side's L5, L10, L15 and L20, season-to-date and league level (ARCHIVE_USE_GUIDE recipe R2). Use dated games only, before the cutoff, from the archive or a registered source route. A window that does not exist is printed with its true n.
- **One piece of evidence:** the windows overlap. They are never counted as separate confirmations, and a short-window move is never a direction on its own (no bounce-back or streak lean without a named, current mechanism).
- **Use in the centre:** the rate that enters the centre is one shrunk blend, computed and printed as recipe R2 says. Using it is an analyst adjustment and goes in the adjustment table with the unadjusted pair.
- **Individual sports:** tennis and other individual sports print the player's last 5/10/15/20 matches on the relevant surface or format where a route exists, under the same rules.

## 8. Mini lifecycle and settlement

New formats: mini-log-7 and mini-settlement-6; existing formats (mini-log-2 to -6, settlement -2 to -5) finish unchanged. Start (2), append card (1), freeze and settle (3), import (4), rollover if needed (5), retrospective (6), repair archive (7), change framework (8). Creating a mini or rollover consumes no ID. Local working P-IDs are permanent references but not canonical until verified import; a contiguous outstanding mini sequence must be accounted for before further allocation. Never reuse P-518–P-522 or silently skip/renumber.

**Lifecycle controls (R15, R16, R22).**
- **One issuing writer per mini.** A mini names its issuing writer and lease time. Only that writer appends new cards. A second mini may not prepare the same next working ID while an unexpired lease or an unaccounted-for mini exists. Hand-over and expiry are recorded in the mini.
- **Freezing.** Settlement freezes a mini by writing a `FROZEN_SOURCE` receipt: path, byte count, SHA-256 and block inventory at freeze time. From then on, new events go to the next authorised mini. A card found after the snapshot is reported as source growth: neither omitted nor counted as covered by the earlier receipt.
- **Request intake.** Every request, including one that never becomes a card, is logged in the mini's intake table with a disposition.

Carry both PENDING_EVENT and terminal UNRESOLVED_EVIDENCE cases in separate queues with original IDs. Every queue item names its responsible actor, exact next source and field, due time with timezone, final-time basis (or UNKNOWN), last attempt, and whether any scheduled automation exists (R38). The five-event open cap and 72-hour final-to-review target are alerts, never instructions to discard work or force grades. Use verified final time; if absent, mark clock UNKNOWN and use scheduled-duration estimate only for triage. Capture fragile fields promptly, normally within 36 hours after scheduled start, adjusted explicitly for delays and multi-day formats. Do not claim capture took place when only a due time exists.

Settle the frozen contract. WIN/LOSS/PUSH require sufficient evidence; VOID requires the frozen void condition; missing/conflicting field or definition yields UNRESOLVED. Evidence C may support a provisional sporting assessment but unresolved conflicts remain visible. A bounded value yields a definite grade only if every feasible value gives that grade. Frozen framework convention and operator settlement are distinct: a sporting result under a convention does not prove an unknown operator result.

For KBO, try the official terminal box score promptly. If stale, retain the available result and arrange/report a retry after about 12 hours, within the review SLA where possible. A promised retry is not a completed fetch. Source corrections append a dated revision; they never silently replace earlier grades.

**Settlement revisions (R17).** Each settlement block has a unique key `revision-<n>` per P-ID, its parent revision (NONE for the first), effective time, source, affected contract keys, and old and new values with the reason. A partial revision changes only its listed keys. Every other key keeps the grade from its parent chain. The effective grade of a contract key is the one in the latest revision of the single unbroken parent chain. Two revisions with the same parent are a `REVISION_CONFLICT`: the affected keys are UNRESOLVED until a resolving revision names both as parents. Never pick by "last block in the file" or by the greatest timestamp. Every prior revision stays readable, and no grade is counted twice.

## 9. Custody, current state and publication

Issued card cores, previous log parts, existing settled minis and dated reports are immutable. Append corrections with reason, timestamp, parent ID and superseded revision pointer. Freeze an exact file copy before settlement; compare actual bytes/prefix, not just line counts. Preserve line endings. Zero deleted lines in numstat alone does not prove append-only: compare the complete original prefix and inspect hunk locations.

**Four identities, never conflated (R20).** This repository runs with `core.autocrlf=true`, so working bytes and committed blobs can differ in line endings.
1. **Raw source snapshot:** the working file's exact bytes, with SHA-256 and byte count, taken before any change.
2. **Imported literal core:** the original card text copied byte-for-byte into its wrapper.
3. **Destination prefix:** the destination working file's exact bytes before the append, compared byte-for-byte afterwards.
4. **Committed representation:** the git blob, normalised to LF. Check it with `git ls-files --eol`.

A claim of byte identity names which identity it means. Line counts, zero deleted lines and the git SHA prove none of the first three. Any normalised comparison declares its transformation (for example CRLF→LF) and keeps the raw source. Changing git attributes needs its own scoped review.

**Finding, 2026-10-12.** The byte-exact (`-text`) rules for Combined Log parts 6–8, `GAME_LOG_STATUS_CURRENT.md`, `research/verification/**`, `research/issued_research/**`, `archive/mini_logs/**` and the archive's `_canonical`/`_custody` folders exist only in this machine's local `.git/info/attributes` (the committed `.gitattributes` was deleted earlier). A fresh clone or another machine applies `core.autocrlf` conversion to those files. Until the owner decides whether to restore a committed attributes file, any agent working outside the original machine must check `git check-attr text <path>` and the raw bytes before claiming byte identity, and must edit `-text` files at byte level. A text editor can silently convert a whole mixed-ending file; this happened and was caught and repaired on 2026-10-12.

**Recheck before every mutation batch (R18).** Immediately before each append, rollover or status update, re-read HEAD, the active-log path and the destination file's current byte count and tail. Compare them with the plan. On any change, stop, rebuild the plan against the new state and preserve both writers' work. Never append from a stale plan.

The active log's opening header is an opening snapshot and may retain old IDs/method text. Resolve current state from CURRENT_STATE, the current status-register section and canonical entries plus dated state/rollover addenda. A stale opening snapshot is not itself a custody conflict. A disagreement in current records is a blocker. Do not run retired tools named in historical log headers.

Imports reconcile every card, carryover, addendum and settlement, including already-imported cards with missing new addenda. All imported cores receive full readback; no three-card spot check substitutes for completeness. Partial imports resume by exact block comparison; mismatch stops before further mutations. Closed-source status requires a verified destination or explicit retained disposition for every source block. Never delete originals automatically.

Stage exact intended paths, preserve unrelated work, commit/push only when authorized by the invoked task, never force. Fetch and verify the remote ref and committed artifacts before claiming publication. A HEAD SHA records repository contents, not proof of a local card's pregame timestamp.

## 10. Learning and claims

Every record remains RESEARCH_ONLY_NOT_CERTIFIED. Model quality, numerical coherence, calibration, predictive skill, operational readiness and record custody are separate questions. **Absence of evidence is not evidence of absence (R24):** a cohort without frozen same-row pregame baselines "does not establish" incremental skill. It does not prove there is none. Line construction affects a hit rate. A single high-probability loss does not establish overconfidence. Measure proper scores against frozen same-row baselines, coverage and expected-score errors; do not optimize headline win rate by line choice or excluding unresolved losses. Historical climatology is descriptive, not a prospective baseline.

Use chronological development, tuning, calibration and untouched test/future shadow separation when designing fitted work. The removed 2026-10-09 runtime is not restored wholesale; the `ml/` workshop is new code with its own tests, and modules ported from commit `37203fc2b` are re-tested. Thresholds and new shadows are untested; eight weeks or a small sample minimum is not proof of power or promotion. See [HYPOTHESIS_REGISTER](HYPOTHESIS_REGISTER.md) and the [implementation roadmap](research/verification/framework_change_2026-10-11-1/IMPLEMENTATION.md).

## 11. Change control

Prompt 8 records the user instruction or finding, class, archived originals, dependencies, version changes, verification and publication. **Prompt revisions (R34).** The prompt suite carries `P-<date>-v<major>.<minor>`.
- The **major** bumps for a FORMAT or STATISTICAL change: a new field, a new rule for p, ranks or scoring.
- The **minor** bumps for a PROCEDURE change: different steps, the same outputs.
- An EDITORIAL change (wording only, behaviour identical) keeps the version and says so in CHANGELOG.

Every change states its class, and the before/after behaviour if it is not editorial. A change that alters what an operator must do is never classed as wording-only. A user-authorized process repair can be implemented without pretending a statistical experiment passed. Behavioral selection/model hypotheses need separate frozen tests; preserve the original registration and append versioned amendments. Update rules, prompts, templates, examples, scoring and receipt definitions together. Do not revise historical values under a new scoring convention without a separate labelled diagnostic view.

## 12. Navigation

[Prompts](research/prompts/README.md) · [Templates](CARD_AND_LOG_TEMPLATES.md) · [Selection](SELECTION_RULES.md) · [Scoring](SCORING_AND_VALIDATION.md) · [Verification](VERIFICATION_PROTOCOL.md) · [Sources](SOURCES.md) · [Archive guide](ARCHIVE_USE_GUIDE.md).
