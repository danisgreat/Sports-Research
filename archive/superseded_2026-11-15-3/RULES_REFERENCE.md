# Operating rules reference

**Current owner-authorized audit controls:** [AUDIT_REVIEW_PROTOCOL](AUDIT_REVIEW_PROTOCOL.md), AUDIT-v1 / SCV-v14. Apply it to new cards and handovers alongside the current CORE. Preserve missingness and the original historical method; neither unsupported scenarios nor retired v4.12 may supply new primary probabilities.

**Consolidated 2026-11-07, CR-2026.11.07-R3.** Part A (formerly CURRENT_RULES) and Part B (formerly SELECTION_RULES) were joined verbatim on 2026-11-07 (R2) and then rewritten (R3): contradictions are resolved by the framework's own precedence (owner instruction, then [CORE](CORE.md), whose v24 text governs any pre-v24 sentence, then the v24 protocols), repeated text is stated once, and rules that apply only to cards issued before P-2026.10.22-v24.0 are kept by reference to their archived text. Section numbers are unchanged, so references such as "CURRENT_RULES section 7" or "SELECTION_RULES §9" still point to the right place. What changed and why: [consolidation report](research/verification/framework_change_2026-11-07-3/CONTRADICTIONS.md). Verbatim originals: [CURRENT_RULES](archive/consolidation_2026-11-07/merged_sources/CURRENT_RULES.md), [SELECTION_RULES](archive/consolidation_2026-11-07/merged_sources/SELECTION_RULES.md).

**Versions in force:** see [CURRENT_STATE](CURRENT_STATE.md) (method, control, scoring, selection and prompt suite). Rule IDs cited below (MINI-v2, EXH-v1, HIST-v3, AVAIL-v4, RETAIN-v3, MLSCOPE-v3, ENV-v2, REF-v2, REQ-v3) are defined where [CORE](CORE.md) §9 lists them.

---

# Part A: CURRENT_RULES

*Formerly `CURRENT_RULES.md`. Previous control revisions are archived under `archive/superseded_*/CURRENT_RULES.md` (pre-v24 text: [archive/superseded_2026-10-22-2/CURRENT_RULES.md](archive/superseded_2026-10-22-2/CURRENT_RULES.md)).*

## 0. Authority, scope and honest execution

The framework is Markdown, CSV and text. Code, its tests and `requirements.txt` live only under `ml/` (owner instruction 2026-10-14); no JSON, notebooks, pickles, workflows or binaries anywhere. A helper run outside `ml/` is disclosed and its rules are written out in prose (CONTRIBUTING). Never claim a grid, simulation, fit, calculation, file write, readback, commit, push or scheduled capture that did not happen; report the exact error when one fails.

**What `ml/` is used for.** Prompt 1 runs the reference stage, the card freeze, the picks linter, the ledger and the simulators that [SIMULATION_PROTOCOL](SIMULATION_PROTOCOL.md) allows; prompt 3 runs the settlement commands; prompts 6 and 8 and maintainer workshop runs do the rest; prompts 2, 4 and 5 run no model. Code writes only Markdown and market-free CSV, under the research folders its command names (for example `research/model_shadow/`, `research/pregame/`, `research/adjustment_ledger/`, `research/competition_parameters/`, `research/effect_tables/`, `research/training_candidates/`), each output with a receipt: code SHA-256, input SHA-256, repository HEAD and run time. An output claims only what the code computed; a model is `EXPERIMENTAL_NOT_QUALIFIED` ([research/model_shadow/README.md](research/model_shadow/README.md)).

**One authority mode per run (R09).** Each run prints one mode in its reading receipt:
- `LOCAL_WORKING_TREE`: every prompt, 1 to 8, run by the repository agent in this repository (ENV-v2, owner instruction 22 October 2026). Print branch, HEAD and every uncommitted difference to a control file; those working files govern this run and the receipt names them.
- `PUBLISHED_MAIN_PINNED`: for reading legacy minis made outside the repository under ENV-v1, and for the owner's external research chats (EXT-v2, [EXTERNAL_RESEARCH_PROTOCOL](EXTERNAL_RESEARCH_PROTOCOL.md)), which read every control at the one full SHA the owner's request names and repeat it in their return. Cards are still made only here ([WORKFLOW](WORKFLOW.md#part-a-execution_environment_protocol) §1). All controls come from the one printed full SHA of `origin/main`.

Where the published and local versions of a control differ, the receipt lists the difference and which one was applied. Never change branches, pull over dirty work or assume a stale download is current.

**Precedence (PREC-v1, the single definition; other pages point here).** Owner instruction; then CORE for cards under P-2026.10.22-v24.0 and later (a pre-v24 sentence anywhere yields to it); then these operating rules and CURRENT_STATE in their domains; then selection, scoring and templates; then sport and league rules; then historical examples and lessons. Verify each sport's physical rules and the actual competition conditions; never override them with a generic default. Report a substantive contradiction; continue independent research when a conflict blocks only issuance or import; never resolve an identity or ID collision by guessing.

## 1. Reading gate

**Basketball endpoint (BK-OT-1, CR-2026.11.07-R1, owner convention 7 November 2026).** Every basketball line includes overtime: full-game totals, spreads and handicaps, team totals and winner lines settle on the final score after all overtime, in every competition. Only a contract whose own text names regulation, a quarter or a half settles on that segment. The endpoint is `FROZEN_FRAMEWORK_CONVENTION` and needs no operator term. Price overtime as explicit mass (the regulation-tie branch) and report whether a threshold was already crossed in regulation. Full text: [RULES_BASKETBALL](RULES_BASKETBALL.md) §0.5.

**Australian rules finals endpoint (AFL-ET-1, CR-2026.11.10-R2, owner convention 10 November 2026).** Every Australian rules finals line includes extra time: full-game totals, spreads and handicaps, team totals and winner lines settle on the final score after all extra time. Only a contract whose own text names regulation, the end of the fourth quarter, a quarter or a half settles on that segment. The endpoint is `FROZEN_FRAMEWORK_CONVENTION` and needs no operator term. Home-and-away games have no extra time. Full text: [RULES_AFL](RULES_AFL.md) §0.

**Prompt lifecycle.** Every task reads [COMMON_OPERATING_PROTOCOL](research/prompts/COMMON_OPERATING_PROTOCOL.md) and its complete selected prompt. Prompt 1 is a core file plus eleven sport files (`research/prompts/1_sports/`), each with its own steps and Upcoming game block. New cards are ANALYST_PRIMARY_V1 built as in section 7.

**Reading gate (GOV-v2).** A game card reads [CORE](CORE.md), the prompt 1 core and its one sport file in full, and the named sections of anything else it opens (the sport's RULES file, SOURCES routes, PROBABILITY_TOOLKIT tables, the competition's parameter rows, the active mini, the status register and the relevant canonical records). Every other task reads CURRENT_STATE, CORE, this document, CARD_AND_LOG_TEMPLATES and its own prompt. Settlement adds scoring and the original card and contract evidence; import, rollover and retrospective add VERIFICATION_PROTOCOL; a retrospective adds the hypothesis register and the latest retrospective; prompt 7 adds coverage, schema and source notes; prompt 8 adds CONTRIBUTING, CHANGELOG and the affected dependencies. Print the receipt in [the prompt index](research/prompts/README.md): exact paths and sections read, revision, time with offset, missing required files and source of authority. Claim full reading only of text read in full.

**Model reading gate (MLSCOPE-v3).** Prompt 1 reads model output only through the reference stage it ran itself (the printed Reference block and its receipt) and, after the card is written and read back, the pregame freeze block. It reads no other model, shadow, cycle or decision-lab output and no benchmark. A frozen reference is never rewritten by the card, and the card never rewrites an issued reference or receipt. Prompt 3 settles shadows, prompt 6 evaluates, prompt 8 releases.

A required control file still unreadable after the GitHub fallback (REF-v2) blocks the dependent mutation only; missing sporting data is recorded, never invented. Cite the rule or source next to any value it shaped. Every card prints its online source URLs, rows and date range inspected, horizon filter, findings and gaps. No deleted archive path is a required input.

## 2. Rule T2: frozen top two and transparent denominators

**Cards before v24.0:** only the original Rank 1 and Rank 2 count as primary wins; ranks 3–4 and shadow selections stay informational; a missing second pick is never manufactured; a losing primary is never replaced by a winning alternate or reforecast.

**Cards from v24.0:** rank 1 and rank 2 of the most-likely list are a descriptive count, and the headline is the paired proper score of the final probability against its references ([ADJUSTMENT_LEDGER_PROTOCOL](ADJUSTMENT_LEDGER_PROTOCOL.md) section 5). A pair that covers itself counts as one pick.

For every cohort, report WIN, LOSS, PUSH, VOID and UNRESOLVED separately, with requested events, retained cards, numeric, qualitative and NO_FORECAST cards and scoring coverage. WIN/(WIN+LOSS) is conditional on resolved decisive outcomes and never hides unresolved cases. Missing evidence is not VOID. Dependent rows are not independent trials. A mechanically protected pair is labelled, and Hit@2 on it is a construction diagnostic, not skill. Definitions: [SCORING_AND_VALIDATION](SCORING_AND_VALIDATION.md).

## 3. Rule R1: outcome review without hindsight

**Deep loss review (DEEPLOSS-v1, owner instruction 2026-11-08).** Every card settled from 8 November 2026 is checked for three rows, each judged on its own:

- **Top side:** the highest final-p row of the side families on the full game, that is winner or moneyline (two-way, three-way or draw-no-bet) and handicap or spread (point spread, run line, puck line, Asian handicap). If the card has no full-game side row, use its highest-p side row on any period.
- **Top total:** the highest final-p over/under row on a full-game total of any quantity the request supplies: points, goals, runs, games or corners, and for cricket the full-innings team total ([GAME_REQUEST_TEMPLATE](GAME_REQUEST_TEMPLATE.md) §1b). If there is none, use the highest-p over/under row on any quantity, such as a period or a checkpoint.
- **Rank 1:** the first row of the most-likely list (for cards before v24, the original Rank 1), when it is neither of the above.

Use the issued final p to find each row. For a card issued without probabilities, use the highest-ranked row of the family. **Each of these rows that is graded LOSS gets its own deep review.** When the top side and the top total both lose, a joint section says whether one cause (pace, a missing player, weather, an early red card) sank both, and whether the card should have priced them as dependent. A PUSH or VOID is not a loss. An UNRESOLVED row waits, and its review is due in the settlement revision that resolves it. A review that is missing, or that skips a section, fails settlement check S8.

**What the review must be.** Deep, comprehensive, brutally honest and accurate. It is written to find what was wrong, not to defend the card. Every claim cites its source and time. It uses the template in [CARD_AND_LOG_TEMPLATES](CARD_AND_LOG_TEMPLATES.md) §6 ("Deep loss review"), whose sections are:

1. the exact frozen claim;
2. the verified outcome and settlement arithmetic;
3. where the outcome fell in the frozen distribution, and the card against its reference and baseline on the row;
4. the error decomposed into reference, adjustments and width;
5. a fact-by-fact research audit;
6. what decided the game, from the box score;
7. what was knowable at the cutoff;
8. a process audit;
9. a verdict in plain words;
10. a counterfactual using only pre-cutoff information;
11. the failure class, and its recurrence across earlier reviews;
12. a testable correction, routed to a lane;
13. the same defects searched for in the card's winning rows;
14. an honesty checklist.

**Honesty rules.**

- "Variance" or "bad luck" is a verdict only with numbers that show it. Acceptable evidence:
  - the outcome's percentile in the frozen distribution;
  - a measured shooting, conversion or BABIP outlier against the teams' season rates;
  - a verified in-game event that no pre-game input could carry, such as an injury, an ejection, a red card or rain.
  Without such evidence, the verdict is ERROR, MODEL_LIMIT or NOT_ASSESSABLE, never luck.
- Say plainly when the pick should not have been made: for example, a near coin flip below the abstain line, a fact that was not verified, or an adjustment without an effect-table row.
- No numeric blame percentages: they would be invented, not measured.
- One tail loss neither proves miscalibration nor vindicates a distribution. Process is SOUND, DEFICIENT or NOT_ASSESSABLE, with evidence; calibration is reported separately, from prompt 6's cohorts.
- Counterfactuals are diagnostic only: they never replace frozen rows, ranks or grades, and never join prospective cohorts.
- Every terminal card, wins and partial settlements included, still keeps R1–R12, with unavailable sections marked and explained.

Settled records written before 8 November 2026 are not reopened; their reviews followed the eight-part rule then in force.

## 4. Rule P4: event first, reproducible selection

Supplied contracts are reference propositions, not privileged selections. Freeze the candidate recipe, endpoints, standard ladder and exclusions before inspecting probabilities. Price every supported supplied row and the declared derived slate from one coherent event distribution. Keep every supplied row's disposition; never drop a difficult line or keep moving lines until a threshold is met.

Ranking follows [Part B](#part-b-selection_rules): decreasing unrounded final p, ties by contract key, at most four rows, family eligibility filters applied, joint dependence disclosed rather than used to reorder. Record each candidate's quantity, family, line and endpoint so that an easier proposition is never presented as a better prediction.

<a id="5-sources-event-state-and-time"></a>

## 5. Sources, event state and time

**Sources that block AI agents (SRC-ALT-v1, owner instruction 2026-11-09).** Check every source with `python -m ml source-audit --url <url>` before opening it. Open only `ALLOWED` or `NO_RULES_FILE`; a blocked or unreadable-rules source is never reached through a proxy, cache, mirror or other user agent. Find a permitted alternate for the same fields (field owner's other outlets, then a reputable statistics site, then reputable media), record the substitution, and leave a field `NOT_VERIFIED` when none exists. Alternates by sport: [SOURCES](SOURCES.md) SRC-ALT-v1.

**Online history (HIST-v3).** Apply [HISTORICAL_SOURCE_PROTOCOL](HISTORICAL_SOURCE_PROTOCOL.md) to every sport and competition, even when local data exist: both sides' L5/L10/L15/L20 verified online with sources, true n, comparisons and unresolved fields. No retired store or profile is a fallback.

**SPORTS_ONLY / MARKET_BLIND.** No odds, line movement, tips, betting previews, prediction markets or fantasy inputs anywhere in research, references, adjustments or cards. A supplied threshold is contract metadata. No value, edge or staking claim.

**§5a. Decision lab: a separate contributor behind a firewall (DECISION-LAB-v2; owner instructions 2026-10-14 and 2026-11-08).** The owner keeps the decision lab as a separate contributor that never adds to the main prediction. `ml/decision/` may run a paper-only, historical study of staking policies on prices held in a local, git-excluded capture. It commits aggregate tables only, under `research/model_shadow/DECISION_LAB/`, never a price or a price-derived row. Its results are reported only in their own place (that folder, or a separately headed section of a report), never beside a card's probability. Nothing it produces enters the reference, an adjustment or effect-table row, p_card, the picks block, a rank, a width, a grade, the learning data or any release; and no forecast, reference, ledger, picks, learning or release module may import `ml.decision` or read its output folder (enforced by `ml/tests/test_decision_firewall.py`). No live or in-play automation is built (online in-play betting is prohibited in Australia under the Interactive Gambling Act 2001). The settlement benchmarks of [BENCHMARK_PROTOCOL](BENCHMARK_PROTOCOL.md) (the line-implied 0.5 and owner-entered post-settlement probabilities) are scoring references only: never read before settlement and never cited by a rule, rank, width, adjustment or learning disposition. *Decided 2026-11-08: kept as a separate contributor; the firewall above is permanent.*

**Identity.** Confirm competition, season, stage, participants, venue, native event ID or a labelled stable surrogate, scheduled time, timezone and official observed state. A reschedule is an alias update under the original identity. A doubleheader needs its game number or native ID. Search every mini and Combined Log, not just headers.

**Sources.** Official field owners first, then structured providers and quality corroboration. Record URL, exact field and value, source publication or update time when available, retrieval time, a short lawful quotation or faithful extract, fallbacks and failures, and collector lineage (UNKNOWN if unknown). Domain count is not independent-source count. A quotation or a git commit does not by itself prove pregame availability.

**Timing.** [TIMING_RESEARCH_PROTOCOL](RESEARCH_PROTOCOL.md#part-e-timing_research_protocol) governs research completion and timing, and the owner's standing rule applies: research is never rushed for the start time. Research continues until complete, after the scheduled or actual start if needed; no lead time forces freezing, issue or abandonment. The evidence horizon is the game-log scheduled start (earlier only for an earlier actual issue or a verified earlier first play); there is no separate cutoff, and lineups, starters, bench and news are researched up to it. Only field-level values demonstrably published by the horizon and before the actual start are admitted; a later page, lineup release, live participation or final game book does not prove its own pre-start value. When research is complete: a final availability and source-state recheck, one re-price of permitted changed inputs, then freeze, write and read back. Later evidence is a dated addendum, never an edit. Labels: `PREGAME` (verified not-started issue, at any lead), `POST_START_ISSUE`, `TIMING_UNVERIFIED` / `KNOWN_AT_UNVERIFIED`, `CLEAN_PRE_START_INPUTS` (only with independent proof and no live or final outcome exposure), `LIVE_OBSERVED` / `HISTORICAL_DIAGNOSTIC`. A late request may be issued as a fast card first ([REFERENCE_MODEL_PROTOCOL](REFERENCE_MODEL_PROTOCOL.md) §7) while the full research continues. Never backdate or relabel old cards. A stale 0–0 does not prove an event has not started.

**§5b. Availability (AVAIL-v4).** Every card applies [ROSTER_AVAILABILITY_PROTOCOL](ROSTER_AVAILABILITY_PROTOCOL.md) §§1–6 and [SOURCES §3.11](SOURCES.md#311-field-fallback-and-official-social-use-by-sport): both sides' exact starters and roles, selected bench or replacements, and current injury, illness, suspension and absence evidence, from the official match record or team sheet, both clubs, medical, eligibility and discipline sources, permitted structured fallbacks and local-language discovery; an obscure competition needs its own organiser and both teams, never a major-league substitute. A roster, probable pitcher, predicted XI, depth chart or projected goalie is not confirmation. "No injuries found" is not "no injuries"; a full starting side does not establish the bench or minutes; a failed fetch is not non-publication. Record attempts and decisive evidence with times in the card's evidence receipt (A3, A8) and lineup metadata (C20). Recheck at the release window and before freeze, and re-price changed inputs. A genuine gap stays explicit: a declared mixture labelled `LINEUP_UNCONFIRMED`, or qualitative or NO_FORECAST handling when states or weights are unsupported. An owner's only-confirmed constraint is honoured without dropping the research.

**Known-at (R28).** An input enters a card only if it was available by the horizon. A historical row's game date is not its availability time; archive rows are retrospective compilations, so print their capture date, and treat a late correction or late statistic as known from its correction time. An input whose availability cannot be shown is `KNOWN_AT_UNVERIFIED` and may not decide a ranked row. Full-season aggregates and corrected datasets are separate snapshots from what was known on the day.

## 6. Requested research and missingness

**No early exit (RC-2026.10.16-v2).** Execute [RESEARCH_COMPLETION_PROTOCOL](RESEARCH_PROTOCOL.md#part-a-research_completion_protocol) for every requested sport and competition. Deliver the complete sporting analysis and every applicable procedure regardless of calibration, model support, lineup or history gaps, kickoff, or mini, ID or write blockers; these restrict only the dependent calculation, clean-input claim or mutation. A thin research supplement or a blanket NO_FORECAST table is not completion. A numeric card uses ANALYST_PRIMARY_V1 (section 7). When numerical assumptions cannot be supported, use UNCALIBRATED_QUALITATIVE with p_card `NOT_ESTIMATED` and a reasoned qualitative ordering per contract, or NO_FORECAST when identity or evidence cannot support a direction, with the missing inputs and next action. Never fabricate rows, a probability, an SD, a baseline or a source to fill a template.

Missing baseline, calibration or fitted model never prevents research logging. Unsupported numeric fields are `NOT_COMPUTED`, unavailable facts `NOT_VERIFIED`, undefined terms `UNKNOWN_DEFINITION`, irrelevant fields `N/A`. Numeric zero is data. A qualitative rank gets no numeric proper score.

## 7. Distribution, baseline and uncertainty

Print model family, endpoint, parameters, input provenance, arithmetic and approximation limits. Marginals come from compatible joint or conditional constructions. Auxiliary counts (corners, players) are separate; without a joint model, report bounds, not an exact cross-family joint. Never label an unexecuted enumeration exact.

Keep unconditional win, push, loss and void masses; p_card = W/(W+L) where W+L > 0; masses sum to one within declared rounding. Preserve allowed draws and ties; resolve OT, ET, SO and extras only as the competition and contract do (basketball: BK-OT-1; Australian rules finals: AFL-ET-1). Never clip a probability: a value above the 0.90 selection ceiling stays outside the ranked list with its actual value. Tail truncation, covariance and score means and SDs are reproducible.

Every numeric row attempts a frozen `BASELINE_P` on the identical proposition, line and endpoint with the league-only recipe of Part B §9. A missing comparator stays missing; nothing is backfilled after results.

**Analyst primary pricing (ANALYST_PRIMARY_V1, v24).** The card's one coherent distribution supplies every p_card, rank and expected value. It is built from the frozen reference (centre and widths) plus one adjustment-ledger row per confirmed fact, with its effect-table row and entry size ([ADJUSTMENT_LEDGER_PROTOCOL](ADJUSTMENT_LEDGER_PROTOCOL.md) section 1), converted with PROBABILITY_TOOLKIT tables or the exact grid in `ml.reference`, every input, formula and intermediate value printed. Code may do the arithmetic and run the simulators that SIMULATION_PROTOCOL allows. Never count an effect already in the reference's rating or form inputs. Print the reference pair and the adjusted pair whenever an adjustment changes the most-likely list or an information row; flag `ADJUSTMENT_DEPENDENT` for such a change and `LARGE_ADJUSTMENT` above 0.25 SD. The width is never below the competition's floor without a written `width_floor_exception`. Sensitivity: run low, base and high values of the most uncertain inputs and show the p changes (ranges, not confidence intervals). A competition with no reference (tier C, no row or prior) prices its own distribution and prints `NONE` in the reference column. Pre-v24 hand-built and MODEL_ASSISTED cards keep their labels and methods.

**Price the uncertainty you disclose (PR-03).** When the card labels an input unfitted, stale, early-season, unconfirmed or `LINEUP_UNCONFIRMED` and runs low, base and high cases on it, the priced distribution is the declared mixture of those cases (default weights 0.25/0.50/0.25; other weights need a basis frozen before pricing). In the ledger, the fact is a `SCENARIO` row. A mixture widens the tails honestly; never then move a line to recover a higher p (section 4). *Pre-v24 cards also printed `p_base` as the SHADOW_BASE_ONLY shadow; v24 cards do not.*

**Recent form: four windows, one piece of evidence (PR-01).** Every numeric team-sport card prints each side's L5, L10, L15 and L20, season and league level (dated games before the horizon, verified online, true n). The windows overlap: never separate confirmations, and a short-window move is width, not a lean, unless a named current mechanism explains it. **Where the reference already uses form** (TB-2-MD, a tier A release), form is not adjusted again: there is no form row in the effect tables, and adding one would double count. **Where there is no reference** (tier C), the shrunk form blend of [ARCHIVE_USE_GUIDE](ARCHIVE_USE_GUIDE.md) recipe R2 enters the card's own centre and is printed with the unadjusted pair. Tennis and other individual sports print the player's last 5/10/15/20 on the relevant surface or format where a route exists.

## 8. Mini lifecycle and settlement

Formats: mini-log-10 and mini-settlement-10; minis already in an older format (mini-log-2 to -9, settlement-2 to -9) finish unchanged. Sequence: start (prompt 2), append card (1), freeze and settle (3), import (4), rollover if needed (5), retrospective (6), repair archive (7), change framework (8). Creating a mini or a rollover consumes no ID. Prompts 1–3 keep cards under stable local keys; prompt 4 alone assigns canonical P-IDs during a verified import with an explicit local-to-canonical map (MINI-v2). Never reserve a number during research. Existing issued P labels stay literal source aliases or verified canonical references. P-518–P-522 are never reused; originals are never renumbered.

**Lifecycle controls (R15, R16, R22).**
- **One issuing writer per mini.** A mini names its issuing writer and lease time; only that writer appends; distinct minis use distinct MINI_KEY namespaces; hand-over and expiry are recorded.
- **Freezing.** Prompt 3 freezes a mini with a `FROZEN_SOURCE` receipt (name, block inventory, freeze time, byte count, SHA-256), verified by prompt 4 at intake. New events then go to the next mini. A card found after the snapshot is reported as source growth.
- **Request intake.** Every request, including one that never becomes a card, is logged in the mini's intake table with a disposition.

Queues: PENDING_EVENT and terminal UNRESOLVED_EVIDENCE separately, with original IDs. Every queue item names its actor, exact next source and field, due time with timezone, final-time basis (or UNKNOWN), last attempt and whether any automation exists (R38). The five-event open cap and the 72-hour final-to-review target are alerts, never reasons to discard work or force grades. Use the verified final time; if absent, the clock is UNKNOWN and a scheduled-duration estimate is for triage only. Capture fragile fields promptly, normally within 36 hours of the scheduled start, adjusted for delays and multi-day formats. A due time is not a capture.

Settle the frozen contract. WIN, LOSS and PUSH need sufficient evidence; VOID needs the frozen void condition; a missing or conflicting field or definition is UNRESOLVED. Evidence C may support a provisional sporting grade with its limits visible. A bounded value grades only if every feasible value gives that grade. A frozen framework convention and an operator's settlement are different things: a sporting result under a convention does not prove an unknown operator result. For KBO, try the official box score promptly; if stale, keep the available result and retry after about 12 hours. A promised retry is not a completed fetch. Source corrections append a dated revision; they never silently replace a grade.

**Settlement revisions (R17).** Each settlement block has a unique key `revision-<n>` per original local key or canonical reference, its parent (NONE for the first), effective time, source, affected contract keys, and old and new values with the reason. A partial revision changes only its listed keys; other keys keep the grade from the parent chain. The effective grade of a key is the one in the latest revision of its single unbroken chain. Two revisions with the same parent are a `REVISION_CONFLICT`, and the affected keys are UNRESOLVED until a revision names both as parents. Never pick by position in the file or by timestamp. Every prior revision stays readable; no grade is counted twice.

## 9. Custody, current state and publication

Issued card cores, previous log parts, settled minis and dated reports are immutable. Corrections are appended with reason, timestamp, parent and superseded-revision pointer. Freeze an exact copy before settlement and compare actual bytes and prefixes, not line counts. Preserve line endings. Zero deleted lines in a numstat does not prove an append: compare the full original prefix and the hunk locations.

**Four identities, never conflated (R20).**
1. **Raw source snapshot:** the working file's exact bytes, with SHA-256 and byte count, before any change.
2. **Imported literal core:** the original card text copied byte for byte into its wrapper.
3. **Destination prefix:** the destination's exact bytes before the append, compared byte for byte afterwards.
4. **Committed representation:** the git blob; check with `git ls-files --eol`.

A claim of byte identity names which one it means. Line counts, zero deleted lines and a git SHA prove none of the first three. A normalised comparison declares its transformation (for example CRLF→LF) and keeps the raw source.

**Line endings (finding updated 2026-11-07).** The committed [.gitattributes](.gitattributes) marks the forensic and append-only paths `-text`. A Windows clone with the system default `core.autocrlf=true` still converts every other file to CRLF on checkout, so working bytes stop matching the committed hashes (seen on 2026-11-07). Work with `core.autocrlf=false` and `core.eol=lf` (set per clone: `git config core.autocrlf false`), check `git check-attr text <path>` and the raw bytes before claiming byte identity, and edit `-text` files at byte level; a text editor can silently convert a mixed-ending file. Changing the attributes file needs its own scoped review.

**Recheck before every mutation batch (R18).** Immediately before each append, rollover or status update, re-read HEAD, the active-log path and the destination's byte count and tail, and compare them with the plan. On any change, stop, rebuild the plan and preserve both writers' work.

The active log's opening header is a snapshot and may keep old IDs or method text; current state comes from CURRENT_STATE, the current status-register section, canonical entries and dated addenda. A stale opening snapshot is not a custody conflict; a disagreement between current records is a blocker. Never run retired tools named in historical headers.

Imports reconcile every card, carryover, addendum and settlement, including already-imported cards with new addenda, with full readback of every imported core. A partial import resumes by exact block comparison; a mismatch stops further mutation. A source is closed only when every block has a verified destination or an explicit retained disposition. Never delete originals automatically.

**Publication.** Every run that changes files ends with a commit and push of the exact intended paths, never the whole tree and never a force push, then a check that `HEAD` equals `origin/main` and that the committed artifacts are on the remote. A HEAD SHA records repository contents, not a card's pregame timestamp.

## 10. Learning and claims

Every record is RESEARCH_ONLY_NOT_CERTIFIED. Model quality, numerical coherence, calibration, predictive skill, operational readiness and custody are separate questions. **Absence of evidence is not evidence of absence (R24):** a cohort without frozen same-row pregame baselines does not establish incremental skill, and does not prove there is none. Line construction drives hit rates; a single high-probability loss does not establish overconfidence. Measure proper scores against frozen same-row baselines and references, coverage and expected-score errors; never optimise a headline win rate by line choice or by excluding unresolved losses. Historical climatology is descriptive, not a prospective baseline.

Fitted work keeps chronological development, tuning, calibration and untouched test or prospective windows apart. The `ml/` workshop is new code with its own tests; nothing from the removed 2026-10-09 runtime is restored wholesale. Thresholds are untested until registered and tested ([HYPOTHESIS_REGISTER](HYPOTHESIS_REGISTER.md)); a minimum duration or sample is not proof of power.

**Learning pipeline (LEARN-v1, R35).** [ML_PIPELINE](ML_PIPELINE.md#part-c-learning_pipeline_protocol) Part C governs. Prompt 1 records research rows as Markdown tables; only prompt 6 (or an authorised prompt 8 change) ingests them into the append-only `research/learning_store/`. Training releases are immutable and reproducible from a recorded store view. Challengers, Hedge schedules and calibrators are studied chronologically and reach cards only through a preregistered prospective shadow, a PROMOTION_ELIGIBLE disposition, an owner decision and a registry entry. Review levels (mini ≈40–50, interim ≈100, comprehensive ≈300, per-sport and per-competition clocks) are workflow triggers, never automatic promotion.

**Runtime receipt and comparator (R36, MLSCOPE-v3).** A card records its pregame freeze disposition and receipt path (EXECUTED, NOT_RUN_NO_RELEASE, NOT_RUN_STALE_RELEASE, NOT_RUN_INPUT_REFUSED or FAILED), never a bare ML_NOT_RUN, and the same-line BASELINE_LEAGUE_V1 comparator whenever league history allows.

**Browser-chat execution (CHAT-EXEC-v1) is retired for game research.** `ml/chat.py` remains maintainer tooling for prompt 8 experiments; no card copies its output.

## 11. Change control

Prompt 8 records the instruction or finding, the class, the archived originals, the dependencies, the version changes, the verification and the publication. **Classes and versions (R34).** The prompt suite carries `P-<date>-v<major>.<minor>`: the major bumps for a FORMAT or STATISTICAL change (a new field; a new rule for p, ranks or scoring), the minor for a PROCEDURE change (different steps, same outputs); an EDITORIAL change (wording only, identical behaviour) keeps the version and says so in CHANGELOG. Method and control tags (MDS, CR) follow the same classes. Every change states its class and, unless editorial, the before and after behaviour; a change to what an operator must do is never wording-only. Behavioural hypotheses need frozen tests; registrations are amended by versioned additions, never rewritten. Rules, prompts, templates, examples, scoring and receipts change together. Historical values are never revised under a new convention without a separate labelled diagnostic view.

**Statistical freeze and replaced rules (STATFREEZE-v1 / GOV-v2).**
- A change to a probability method, width, selection constant, reference or release is STATISTICAL. It takes effect at a season boundary or as a new, separately scored lane, never mid-season on a small sample. A bug fix that changes no output may be made at any time; PROCEDURE changes are batched into at most one release a month unless the owner orders otherwise; EDITORIAL changes may be made at any time.
- Every new rule names the rule it replaces, the document that held it and the archive path of the replaced text. A rule that cannot be checked by code or by a registered test is wording and does not enter the reading gate.
- A rule is stated once; other documents link to it. The `ml` test suite checks that the prompt suite, the dependency map and CURRENT_STATE agree.

## 12. Navigation

[Prompts](research/prompts/README.md) · [Templates](CARD_AND_LOG_TEMPLATES.md) · [Selection](#part-b-selection_rules) · [Scoring](SCORING_AND_VALIDATION.md) · [Verification](VERIFICATION_PROTOCOL.md) · [Sources](SOURCES.md) · [Archive guide](ARCHIVE_USE_GUIDE.md) · [Learning pipeline](ML_PIPELINE.md#part-c-learning_pipeline_protocol).

---

# Part B: SELECTION_RULES

*Formerly `SELECTION_RULES.md`. **SEL-2026.10.22-v4** applies to cards under P-2026.10.22-v24.0 and later; numerical thresholds are PROVISIONAL, not accuracy guarantees. Cards before v24.0 were selected under SEL-2026.10.12-v3, whose full text (Rank-1 gate, Rank-2 floor, the five shadows) is archived at [archive/superseded_2026-10-22-2/SELECTION_RULES.md](archive/superseded_2026-10-22-2/SELECTION_RULES.md) and is used only to read those cards' recorded labels. Part A controls; timing is [TIMING_RESEARCH_PROTOCOL](RESEARCH_PROTOCOL.md#part-e-timing_research_protocol).*

## 0. What changes under SEL v4 (v24.0 cards)

SEL v4 replaced SEL v3 sections 2 and 3: the Rank-1 gate (p at least 0.62 with a lead of at least 0.04), the Rank-2 floor (0.58) and the five shadow selections (RET03 gate, RET04, XCARD6, RANK_DELTA, BASE_ONLY). In their place ([ADJUSTMENT_LEDGER_PROTOCOL](ADJUSTMENT_LEDGER_PROTOCOL.md) sections 3–4) the card prints a probability for every supplied contract, the winner, a **most-likely list** (section 2), an **information list** (rows that moved at least 0.03 from the reference) and the **abstain flag** (`no strong pick` unless a ranked row reaches 0.65 or a row moved). The questions the shadows asked are answered by the information list and the ledger comparisons (against the reference, the baseline and the line-implied 0.5). Sections 4 to 9 apply unchanged.

## 1. Constants and scope

| Item | Rule |
|---|---|
| Most-likely list | At most four supported rows; never padded |
| Selection ceiling | Ranked p ≤ 0.90; a higher true value is kept outside the list, never clipped |
| Abstain floor | `no strong pick` when no ranked row reaches 0.65 and no row is an information row |
| Information row | \|final − reference\| ≥ 0.03 |
| Joint failure of the first two rows | Printed (exact, or Fréchet bounds); 0.30 target / 0.35 warning are historical diagnostics, never a reordering rule |
| Large adjustment | Above 0.25 SD; any size that changes the list is ADJUSTMENT_DEPENDENT |
| Decision block | About 650 words at most; full evidence in the appendix |
| Review target | Within 72 h of the verified final; an unknown final time is disclosed |
| Open-event alert | More than five pending events; evidence backlog counted separately |
| Fragile-field capture | Normally within 36 h of the scheduled start; delays and multi-day events state a revised due time |

## 2. Primary order and Rank-1 gate

*v24: the most-likely list. Cards before v24.0 used the Rank-1 gate of SEL v3 (archived).*

Freeze the candidate recipe and eligibility rules before pricing. A contract key comprises quantity, participant orientation, line, direction, period, endpoint and action or void convention; identical keys are deduplicated. Order eligible numeric rows by unrounded final p, highest first, ties by ascending contract key, and keep the first four or fewer. A qualitative slate uses an explained qualitative order, with no numeric score.

Family rules (section 4) decide eligibility: an inadmissible would-be first row is removed from the list with its reason and kept in the diagnostic ladder, and the process repeats on the rest. Never quietly demote a row below a lower-p row in a table claimed to be probability-sorted. Unsupported rows are excluded whether or not they would win.

**Precision at thresholds (R14).** Compute p and gaps at the precision of the calculation actually performed (a Φ table read to 2 dp, an interpolation, a truncated grid) and print the approximation error ε it implies (default 0.002 per probability for a 2-dp Φ table with linear interpolation). Compare unrounded values and round only for display. Two ranked rows within 2ε are a `PRECISION_TIE`, broken by contract key and disclosed. `ml card lint` checks the 0.65 abstain floor and the 0.03 information threshold against the probabilities printed in the picks block. Rounding never creates a rank, a pass or an information row. A key-number, push or tie adjustment is applied to the normalised common distribution and every row is re-derived from it; mass is never added to one row alone.

<a id="3-rank-2-and-the-joint-failure-probability"></a>

## 3. Rank 2, dependence and shadows

*v24: the second row of the most-likely list is simply the second-highest p. No floor and no shadow selection apply. Cards before v24.0 kept the Rank-2 floor and five shadows of SEL v3 (archived).*

Quantity keys identify the random variable and endpoint: the full-match total; the signed full margin (winner and either team's handicap share it); each named team total; each phase total; each player's count. Reversing a margin sign or renaming a family does not create a different quantity. Different quantities can still be structurally dependent; evaluate actual losing sets.

**Joint failure of the first two rows.** For unconditional losing masses l1 and l2: the exact joint is the sum of their common losing states in the shared distribution; nested loss sets give min(l1, l2); disjoint sets give 0, labelled MECHANICALLY_PROTECTED (and a covering pair counts as one pick). Otherwise show Fréchet bounds `[max(0, l1+l2−1), min(l1, l2)]`, never a product without justified conditional independence. Use the W, P, L, V masses, not 1 − p, when pushes or voids exist, and record P(both decisive) where a conditional comparison is needed. Exact, bounded and unavailable joints stay separate in retrospective tables.

## 4. Family checks

| Family | Required support |
|---|---|
| Soccer first-half Over 0.5 as the first row | A half-specific rate or model, p ≥ 0.72 and a 5-point lead over the best eligible alternative; full-time intensity alone is insufficient |
| Baseball +1.5 as the first row | p ≥ 0.65 from a signed team-specific P(win) + P(lose by exactly one), with ties and actions explicit |
| Tennis games | Reproducible point, set and match construction with a supported match-form mixture; approximation and deciding-set sensitivity disclosed; no invented exact enumeration. Game handicaps and totals come from the complete set-score states, **including match-losing states**. Covering −k.5 games does not imply winning the match, and set handicaps are a different quantity (R12) |
| Ties and moneylines | Draw or tie possibility is set by the exact competition and season, and moneyline action on a tie by the frozen contract (two-way void or push, three-way, or loss), never by a sport-wide default (R13); basketball winner lines include overtime (BK-OT-1), and Australian rules finals winner lines include extra time (AFL-ET-1) |
| Corners | A named provider, a supported count distribution and the field definition; a cross-score joint needs a joint model |
| Period and player rows | Exact phase or player definition, source field and capture plan; never a period score inferred from the final |
| Unknown league or format | Explicit local evidence or prior and its limits; never a silent transfer of another competition's rules |

League-wide absolute-margin or one-run rates are sanity checks, never a team's directional probability or a universal ceiling. A sport-file instruction that conflicts with this table is historical.

## 5. Candidate universe

Default recipe: the supported supplied lines; winner, draw and double chance as appropriate; and the supported handicap, total, team-total and period families on the sport's declared ladder. State each quantity's line range and step before pricing (legacy default ±2.5 SD, cricket ±2 SD; half lines, with integer lines only where pushes are defined). Record the set actually enumerated; if only part could be computed, label it `PARTIAL_UNIVERSE`.

Never claim an exhaustive search from four hand-picked rows. Keep unselected supplied rows and the relevant neighbouring lines. Analyst-derived lines can be easy by construction; report each one's p, its distance from the centre and its baseline p. Neither a high hit rate nor zero joint failure proves a useful prediction. Baseline and card are scored on the same frozen lines.

**Line difficulty on every ranked row (R33).** Each row prints its line and direction, its signed distance from the centre for that quantity (in units, and as z = (line − centre)/SD where the SD is supported, otherwise `N/A`), and whether it is SUPPLIED or ANALYST_DERIVED. A row 1.2 SD from the centre is an easier proposition than one at 0.3 SD; comparisons across cohorts use identical rows or disclose the difference.

## 6. Regimes and sensitivities

Regime flags: NONE, FINALS_COMPRESSION, EARLY_SEASON, CUP_ROTATION or RULE_CHANGE:<verified name>; other context is prose. A flag labels the context; it does not move a number by itself. A regime effect enters a card only as an [effect-table](PARAMETERS.md#part-b-effect_tables) row, at the entry size its status gives, or as a declared `SCENARIO` row. **Regime rows (REGIME-v3, 2026-11-08, measured on verified finals against the reference's own walk-forward forecasts and confirmed only by a CHRONOLOGICAL test that fits each season on earlier seasons):**

- NBA playoffs total −4.5% (`E-NBA-PLAYOFF-TOTAL-R2`, FULL; 5 of 5 later seasons better);
- MLB postseason total −10.9% (`E-MLB-POSTSEASON-TOTAL-R2`, HALF: confirmed only on a proxy, not on MLB-CYCLE-4);
- NRL first 28 days −2.5% (`E-NRL-EARLY-TOTAL-R2`, HALF: chronological intervals cross zero);
- AFL finals −3.2% (`E-AFL-FINALS-TOTAL-R2`, HALF).

The R1 rows are superseded (`research/effect_tables/SUPERSEDED.csv`). Each regime adjustment is also tested prospectively, adjusted against unadjusted, through its ADJUSTMENTS_V1 counterfactual. NBA, MLB and AFL early season and NRL finals are `MEASURED_NULL` (no adjustment); NHL and NFL are `NOT_ESTIMATED` (scenario only); NRL six-again is retired (every season since 2020 already contains it). Apply a regime row once, to the total centre, before reading the contracts, and never together with another row that measures the same thing (for MLB early season, a temperature row). The 2026-10-09 archive multipliers in [PARAMETERS](PARAMETERS.md#part-c-base_rates_register) Part C are historical and are never inputs (pre-v24 cards applied them as their own rules said). Study: [regime_study](research/verification/framework_change_2026-11-08-1/regime_study/). An unmeasured effect is a scenario with its basis, never an invented multiplier. Some finals regimes raise scoring; do not assume compression.

Every adjustment logs its target, before and after values, units and SD basis, source, basis (measured or analyst) and overlap with other terms (for v24 cards, as ledger rows). A change to the most-likely list is ADJUSTMENT_DEPENDENT; print the unadjusted pair, the sensitivity probabilities and which assumptions drive the result. A missing SD prevents an SD-size claim but never hides a rank change.

## 7. Grades, evidence and queues

Grades: WIN, LOSS, PUSH, VOID, UNRESOLVED. VOID is a verified frozen void rule, never "no data". Card states: SETTLED, PARTIALLY_SETTLED, PENDING_EVENT, UNRESOLVED_EVIDENCE, NO_FORECAST. A cancelled event may be terminal with VOID rows under a frozen rule; an unknown state stays pending.

| Evidence | Meaning |
|---|---|
| A | Official field-owner terminal record for the exact target |
| B | Structured provider or supported agreement, with provenance and lineage disclosed |
| C | Single secondary or provisional evidence; limits and conflicts kept |
| E | A valid bound on a partly observed value; grades only if the whole feasible set agrees |
| X | No sufficient evidence; UNRESOLVED |

Definition status is a separate column: OPERATOR_VERIFIED, FROZEN_FRAMEWORK_CONVENTION, UNKNOWN_DEFINITION or N/A (legacy OP stays a historical label). Never apply a newly invented default after the result; an owner convention applies from its own date and is recorded as a revision for earlier records (as BK-OT-1 was for P-616). Conflicting material sources are never adopted just to close a record. Corrections carry the original grade, new grade, source and reason.

## 8. Failure classes

FIRST_HALF_GOAL_OVERSELECTION, RUNLINE_CUSHION_CEILING, BASKETBALL_TOTAL_WITHOUT_PACE_MODEL, TENNIS_IID_UNDERDISPERSION, RANK_BY_Q_NOT_P, SHARED_DRIVER_TOP_TWO, HANDICAP_TAIL_OVERREACH, SMALL_SAMPLE_STRENGTH_OVERREACH, PHASE_INCOHERENCE, CORNER_ROW_WITHOUT_PROVIDER_OR_NB_MODEL, OVERCONFIDENT_PROBABILITY, WEAK_SLATE_FORCED_RANK, QUALITATIVE_RANKS_WITHOUT_DISTRIBUTION, REGIME_IGNORED, UNFITTED_ANALYST_ADJUSTMENT, LATE_INFORMATION, ENDPOINT_OR_CONTRACT, SOURCE_OR_IDENTITY, VARIANCE and OTHER.

Use an alias only with a printed mapping. A suspected failure is not an established error. Honest qualitative research is not misconduct: QUALITATIVE_RANKS_WITHOUT_DISTRIBUTION means numeric confidence claimed without a distribution. OVERCONFIDENT_PROBABILITY is never inferred from one high-p loss. OTHER and NOT_ASSESSABLE need an explanation. Several process faults may be kept, without invented causal percentages.

## 9. Frozen league-only baseline (RET-02)

`BASELINE_LEAGUE_V1` uses the same league, season regime, endpoint, orientation and line, with no team, lineup, form or event-result inputs. Freeze the recipe and source window before the forecast: a vetted league distribution with every parameter supported, or a declared prior-only empirical cohort with literal W/P/L/V counts on that exact line. Never switch recipes after seeing which comparator is easier to beat.

Document the distribution family, means, SDs, dispersion and covariance or the empirical counts, seasons, exclusions, orientation, sample size, data last-known time and source. Match the card's push and void conditioning. Empirical p = W/(W+L); a zero denominator is `NOT_COMPUTED`. A mean and SD alone do not determine a discrete, extras, tennis or phase distribution: those families stay `BASELINE_UNAVAILABLE` without support. Compute the baseline from its own league-only inputs, never from team-adjusted parameters. Print BASELINE_P and its ID on every numeric row, or a precise missing reason. A stale profile is labelled and tested, never refreshed with post-horizon games; no backfilled baseline enters prospective paired evaluation.

**Baseline coverage (PR-06).** Every numeric card prints `Baseline coverage: <rows with BASELINE_P>/<numeric ranked rows>`. A missing baseline uses exactly one reason: `NO_LEAGUE_PROFILE`, `PROFILE_LACKS_ENDPOINT`, `DISCRETE_FAMILY_UNSUPPORTED`, `NEW_FORMAT_NO_PRIOR`, `SOURCE_UNREACHABLE` (with attempt and time) or `OTHER:<explanation>`. A reason that names a missing profile row is listed for prompt 7. TB-1-MD and TB-2-MD use team inputs, so they are references, never `BASELINE_LEAGUE_V1`.

## 10. Primary probability source

The probability source is Part A section 7 (ANALYST_PRIMARY_V1 from the frozen reference plus the adjustment ledger). A workshop model reaches a card only as the frozen reference; it never overwrites p_card. Historical MODEL_ASSISTED_PRIMARY_V3 cards keep their original [model source](ML_PIPELINE.md#part-a-primary_prediction_protocol) and cohort.


## v24.15 operational and parameter amendment

For v24.15 manifest-bound external work, EXT-v3 governs reduced/six-role scope, explicit numeric-or-unpriced coverage, official no-play delay amendments and independent source snapshot versions. The owner authorizes this statistical/admission correction before a v24.14 scored card. Subsequent source-only audits may update access snapshots without changing method identity; other statistical changes keep the freeze and owner-authority rules. See [EXT-v3](EXTERNAL_RESEARCH_PROTOCOL_V3.md).


## Owner-directed ASSESS-100 amendment (CR-2026.11.11-R4)

Current EXT-EVAL-v2 assessment happens at the first 100 eligible fully settled paired games with no minimum weeks or end-of-week wait. It uses event-equal scoring with explicit uncertainty/dependence diagnostics. This assessment-only release preserves forecast/profile/kit v24.15 and earlier separately registered model experiments. Read [the current plan](research/external/EVALUATION_PLAN_v24.16.md); old calendar language yields to this owner instruction for the current assessment.
