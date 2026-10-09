# Card and log templates

**Retrospective-only carryover packets:** retain the supplied artifacts and original source prefix; reconcile selected IDs and reserved references; append a dated exhibit to the configured active log without issuing new cards or recounting historical grades. Keep any excluded local card in source custody and show its pending reservation separately from the canonical next ID. The [October 8 packet review](research/verification/carryover_review_2026-10-08/REPORT.md) preserves 65 reviews and 780 sections. Run `py -3.14 -B -m research.operations.verify_carryover_review` for published custody, adding `--local-body-custody` only when local publisher captures are available.

**Local authority and all-log reconciliation (October 5):** Local working files govern; GitHub main publishes them. The latest user instruction supersedes earlier GitHub-only prompts. Current [all-log evidence](research/verification/all_log_resolution_2026-10-05/REPORT.md) accounts for all 537 slots and temporary aliases, ten repaired documentary mappings, four new sporting reviews and 53 precise carryovers. Existing IDs and frozen forecast/source bytes remain unchanged.

Current authority: [CURRENT_RULES.md](CURRENT_RULES.md), MDS-2026.10.09-v8.3 / CR-2026.10.09-R3. Requested cards normally arrive through the [local-mini lifecycle](#local-mini-format-mini-log-3) and the operator prompts in [research/prompts/](research/prompts/README.md). Requested research uses the following template and receives a canonical ID regardless of calibration. Later sections describe the separate frozen certified-issuer protocol; its gates do not block requested research.

## Requested research card — default workflow

Prepare JSON with `event_key`, `native_event_id` (unknown if not verified), `league`, `title`, `tracking_handle`, `analysis_status`, `source_path` and full Markdown `body`. Body: exact fixture/time/state and source update time; supplied contracts and sporting/operator semantics (reference only, Rule P4); posted participants; season/recent/exposure/bullpen/environment evidence; **the event distribution** (sport engine/score matrix/simulation or an explicit reproducible analyst scenario) with its parameters; **four candidates** priced from that one distribution, each tagged `SUPPLIED` or `ANALYST_DERIVED` with exact proposition, line, period and endpoint; **ranked by p_card, Rank 1 and Rank 2 as the picks** and ranks 3–4 marked informational (Rule T2); the joint top-two failure probability; potential winner; rationale and failure routes; calibration/assumption/missingness labels; full sources and retained receipts. Use `UNCALIBRATED_QUALITATIVE` and `NOT_ESTIMATED` for unsupported percentages. Analyst scenarios may contain explicit uncalibrated reproducible estimates.

Run `py -3.14 -m research.operations.log_card commit card.json`, then `verify`. Retain actual log time, original source bytes and exact projection. Import original cards literally beneath a dated canonical correction; do not retroactively rewrite probabilities, claim times or fabricate missing ranks. The configured active combined log is the destination; existing events retain their ID for dated additions. No retrospective until requested.

### Top-two pick table (from P-557)

| Rank | Role | Tag | Proposition | p_card | Probability status | Evidence | Failure route |
|---|---|---|---|---|---|---|---|
| 1 | PICK | SUPPLIED / ANALYST_DERIVED (replaces …) | … | … | … | … | … |
| 2 | PICK | … | … | … | … | … | … |
| 3 | INFORMATIONAL | … | … | … | … | … | … |
| 4 | INFORMATIONAL | … | … | … | … | … | … |

The Proposition cell holds the exact proposition, line, period and endpoint. Below the table print: P(Rank 1 and Rank 2 both lose) from the same distribution; the Rank 1 − Rank 2 gap; and the supplied rows that were not selected, with their p_card from the same distribution.

### Settlement with top-two counting and Rank-1 retrospection (from 2026-10-09)

Grade every row W/L/PUSH/VOID on its sporting endpoint with an evidence grade (A owner, B structured provider, C best-available, E estimated bound, OP default rule, X no data → VOID). Count wins only for ranks 1–2 and print the card class (`TOP2_ALL_WON`/`TOP2_SPLIT`/`TOP2_ALL_LOST`/`VOID`). If Rank 1 lost, append the deep retrospection with all eight parts of Rule R1 (claim, what happened, distribution check, knowability, verdict, own-top-two counterfactual, failure class, proposed correction). The [2026-10-09 final settlement](research/verification/final_settlement_2026-10-09/REPORT.md) is the worked reference.

## Local mini format `mini-log-3`

`mini-log-3` is `mini-log-2` plus the fields and checks below. Everything in the [`mini-log-2` section](#local-mini-format-mini-log-2) (file layout, IDs, blocks, addenda, settlement, settlement folder) applies unchanged. The first line is `<!-- MINI-LOG-FORMAT: mini-log-3 -->`; `mini-log-2` minis already in progress remain valid and are finished in their own format (`mini_log.detect_version` reads the tag, and the [legacy examples](research/prompts/examples/legacy_mini_log_2/) are tested). The [golden mini](research/prompts/examples/EXAMPLE_ACTIVE_MINI.md) and its [settled copy](research/prompts/examples/EXAMPLE_SETTLED_MINI.md) are the reference; `research.operations.mini_log verify` and `research.operations.card_validator` enforce this section, and prompt 4 re-runs them on import.

**Extra card metadata** (all required; `N/A`, `NONE` or `FRAMEWORK_DEFAULT:` are explicit values, never blanks):

| Bullet | Value |
|---|---|
| `Distribution object` | `<family>_<method>_v<n> — <one-line parameters>`. One grid prices every row; the first token is the object's id. |
| `Regime flags` | `NONE`, or comma-separated `FINALS_COMPRESSION`, `EARLY_SEASON`, `CUP_ROTATION`, `RULE_CHANGE:<name>`, taken from the measured table in `BASE_RATES_REGISTER.md` |
| `Retirement rule`, `Listed-pitcher rule`, `Abandonment rule` | `N/A`, `FRAMEWORK_DEFAULT: <rule>` or `OPERATOR: <name>: <rule>` (GOV-04). Settlement applies the stated rule and grades such rows `OP`; it never invents one |
| `Settlement fields` | The exact field each pick settles on, with `(provider: <name>)`. Corners, half-time, period and player rows require a named provider (SRC-02) |
| `Capture due` | ISO 8601 with a UTC offset, after the scheduled start; a warning above 36 h. `capture_schedule` lists captures due and overdue |
| `Evidence snapshots` | `sha256:<64 hex>@<ISO time with offset>` items separated by `; `, or `NONE` (warns). `evidence_snapshot verify-card` resolves each token to a stored receipt (SRC-03) |

**Decision block and appendix.** The card body is `### Decision block` (at most 4096 bytes, target 2560) followed by `### Appendix` (sections `A1.`–`A9.`: identity, supplied contracts, evidence, distribution, priced ladder, adjustments, family checks, sources, integrity receipt). The decision block holds the `**Distribution:**` line, the pick table, and the bold lines `**P(Rank 1 and Rank 2 both lose):**`, `**Rank 1 − Rank 2 gap:**`, `**Rank-1 gate:**`, `**Adjustment dependence:**`, `**Supplied rows not selected:**` and `**Potential winner:**`.

**One distribution.** Every pick row's `Probability status` reads `FROM_DISTRIBUTION:<distribution id>`; there is no `q` column; ranks are non-increasing in p_card; no `TO_FILL` placeholder survives.

**Rank-1 gate** (provisional values from `runtime/config/selection_rules.json`): `**Rank-1 gate:** PASS|RANK1_UNSTABLE — p_card x%; best non-complementary alternative y%; margin z points`. It passes when p_card is at least 62% and the margin is at least 4 points; the validator recomputes the verdict from the stated numbers. A failing gate is allowed and routes the card to its own scoreboard cohort. Rank 2 is the remaining row with p_card of at least 58% that minimises the joint top-two failure probability; the validator warns above 35%.

**Adjustments.** `**Adjustments:** NONE`, or the table `| Name | Target | Size | SD units | Prior basis |` with a basis of `fitted`, `archive_estimate` or `analyst_judgement`. If any adjustment exceeds 0.25 SD, print `**Unadjusted top two:** <rank 1>; <rank 2>` and set `**Adjustment dependence:**` to `ADJUSTMENT_DEPENDENT` exactly when that pair differs from the picks (the validator checks both directions).

**Family rules** (from `selection_rules.json`, checked on the pick table): a first-half Over 0.5 is not Rank 1 below 72%; a baseball +1.5 is not Rank 1 below 65%; tennis games rows need the exact-tree distribution with a form shock; corners rows need a provider and a negative-binomial count distribution.

**Re-forecast addendum.** A confirmed starter, goalie or quarterback change after the research time writes a dated `ADDENDUM` whose re-priced table is headed `| Rank | Proposition | p_reforecast |` (never the pick-table header). The card stays unchanged and is graded.

**Settlement additions.** R1 of each settlement copies that card's own Rank 1 and Rank 2 (`settlement_lint` fails an R1 that describes another card's ranking). Settle within 72 hours of the final (`settlement_sla`); open carryover stays at or below 5.

## Local mini format `mini-log-2`

A local mini is the working file in which an external chat agent (GitHub read-only) writes cards between canonical imports. The lifecycle and the six operator prompts are in [research/prompts/](research/prompts/README.md); the [golden active mini](research/prompts/examples/EXAMPLE_ACTIVE_MINI.md) and its [settled copy](research/prompts/examples/EXAMPLE_SETTLED_MINI.md) are validated by the test suite and are the reference for every detail below. `research.operations.mini_log` validates this format (`verify`, `verify-settled`) and `research.operations.import_mini` imports it.

**File.** `Mini Prediction Log - <FIRST> onward - <date>/PREDICTION_MINI_RUNNING_LOG_<FIRST>_ONWARD.md`. First line `<!-- MINI-LOG-FORMAT: mini-log-2 -->`; then `## A. Authority snapshot` (two-column table including `First working P-ID for this mini`), `## B. Local ID rules`, `## C. Active carryover`, `# NEW LOCAL EVENT CARDS`, and `# RUNNING FOOTER` with its table between `<!-- BEGIN FOOTER -->` and `<!-- END FOOTER -->`.

**IDs.** The first working ID is max(repository next canonical ID, previous mini's highest working ID + 1). One sporting event = one ID, issued in increasing order; IDs never change. Creating a mini, an addendum, a carryover or a settlement consumes no ID. The importer keeps every working ID or stops on a collision; it never renumbers.

**Blocks.** Every unit sits between exact markers, and no heading inside a block may start with a P-ID (`## P-…`), which the allocator would read as a new card.

| Block | Markers | First line | Where |
|---|---|---|---|
| Card | `<!-- BEGIN CARD P-NNN -->` … `<!-- END CARD P-NNN -->` | `## Card · P-NNN · SPORT / LEAGUE · Event · YYYY-MM-DD` | After `# NEW LOCAL EVENT CARDS`, before the footer, increasing ID |
| Carryover | `<!-- BEGIN CARRYOVER P-NNN -->` … | `### Carryover · P-NNN · …` | Section C; ID below every new card |
| Addendum | `<!-- BEGIN ADDENDUM P-NNN -->` … | `### Addendum · P-NNN · <ISO 8601 with offset>` | After the card it amends, before the footer |
| Settlement | `<!-- BEGIN SETTLEMENT P-NNN -->` … | `### Settlement · P-NNN · Event` | Only in the appended settlement section |

**Card.** Metadata bullets `- **Working ID:**` (`P-NNN — LOCAL_WORKING_ID — PENDING_CANONICAL_IMPORT`), `Event key` (ending `:YYYY-MM-DD`), `Native event ID`, `Sport`, `League`, `Tracking alias`, `Analysis status`, `Timing state` (`PREGAME`, `LATE_START_UNVERIFIED` or `LIVE_OBSERVED`), `Research completed`, `Scheduled start`, `Endpoint`; sections 1–8 (identity and state; supplied contracts, reference only; evidence; event distribution; candidates and picks; family checks; sources; integrity receipt). The pick table uses the header above with exactly four rows, roles `PICK, PICK, INFORMATIONAL, INFORMATIONAL`, a `SUPPLIED` or `ANALYST_DERIVED` tag, a percentage `p_card` in (0%, 90%] for every row and non-increasing p_card. Below it, the exact lines `**P(Rank 1 and Rank 2 both lose):** x%`, `**Rank 1 − Rank 2 gap:**`, `**Supplied rows not selected:**` and `**Potential winner:** name — p% (endpoint)`. Warnings (not errors): Rank 1 below 60% without `RANK1_UNSTABLE`; joint top-two failure above 35%.

**Addendum.** Corrections and late news under an existing ID (the card's own, or an earlier canonical ID found by the duplicate check). It contains no pick table, leaves the footer unchanged, and is imported as a dated canonical addendum before the settlement. Settlement grades the original card only.

**Settlement.** The settled mini is the frozen mini's exact bytes followed by `# SETTLEMENT AND RETROSPECTIVES`, the tag `<!-- SETTLEMENT-FORMAT: mini-settlement-2 -->`, a header table recording `Frozen original SHA-256` (or `NOT_COMPUTED`), and one settlement block per card and carryover. A block states `**Card state:** SETTLED` or `PENDING_EVENT` (non-terminal events only). A settled block gives `**Final event:**`, `**Settlement sources:**`, the table `| Rank | Proposition | p_card | Grade | Counts toward wins | Evidence | Basis |` with propositions and p_card copied exactly, grades WIN/LOSS/PUSH/VOID, evidence A/B/C/E/OP/X (X must be VOID) and `Counts toward wins` = `YES` only for a Rank 1 or 2 WIN; then `**Top-two result:**`, `**Winner call:**`, R1.–R12., and — when Rank 1 lost — the eight-part deep retrospection with a failure class from the taxonomy in `research/operations/top_two.py`.

**Settlement folder.** `Mini Settlement - <FIRST> to <LAST> - <date>/` holds `ORIGINAL_MINI/<frozen>.md`, `PREDICTION_MINI_SETTLED_<FIRST>_<LAST>.md`, `LOCAL_ID_MAPPING.md`, `UNRESOLVED_CARRYOVER.md` and `SETTLEMENT_MANIFEST.json`; `mini_log join` builds the settled file byte-exactly from a separately written settlement section.

## Complete universe

A retained `event-universe-1` JSON has `captured_utc`, nonempty hashed `source_refs`, and every relevant event: lane, league, season, durable event_id, home/away, scheduled_start_utc, endpoint and period. Capture and registration precede issuance. Register all fixtures before selecting successful candidates. Append an evidence-backed abstention for every omitted fixture. A model-only provider surrogate belongs to daily research coverage, not a live official-ID universe.

## Evidence bundle

The version is `forecast-evidence-1`. Required identity includes lane, league, season, event_id, exact home/away, model_version, endpoint, scheduled_start_utc, data_cutoff_utc and issued_utc. Registries are pinned by hash. Every input artifact has path, SHA-256 and available_utc no later than cutoff. Model/card/baseline distributions have exact event, endpoint, cutoff and input checksum plus retained score states. Contracts specify market, side, line, period, endpoint and void rule. No missing field is filled by narrative.

Attach three agreeing pregame body receipts with exact source/parser, league scope, official owner, retained content hash, independent upstream audits and event-specific lineage audits. Unknown collector independence blocks issuance. Source states must be fresh within the registered cap of at most five minutes. Actual-start evidence is added only after the event.

An adjustment requires an approved method version, reason, frozen parameters and pre-cutoff hashed evidence. `NONE` leaves the distribution unchanged. Do not supply subjective percentages or counterfeit source URLs to make a template pass.

## Issued core

The issuer's Markdown includes permanent P-ID, exact event/endpoint, issue/cutoff/start times, model version, model/input/registry hashes, source lineages, contract rows with coherent win/push/loss masses and separate p_model/p_card/p_baseline, adjustment status and transaction ID. Rendered ordering follows p_card. The machine bundle is immutable; the ledger-selected projection and canonical ledger bind its bytes.

A preparation is **PREPARED_DRAFT_NOT_ISSUED** and consumes no ID. A committed pregame card is **ISSUED_PENDING_TERMINAL_ADMISSION**. Existing issued forecasts retain their own original format and ranking arithmetic.

## Research diagnostic addendum and mini closure

Bind the existing canonical ID/event, immutable original source/projection hashes, actual observation/review time, exact endpoint and each original source version. Retain conditional grade, operator definition status, actual-start admission, audited terminal-lineage status and performance eligibility separately. UNKNOWN_DEFINITION, UNRESOLVED_PERIOD, UNRESOLVED_PROVIDER_FIELD and missing p/baseline remain literal missingness; NO_FORECAST and late/live classifications remain unchanged. List every unresolved requirement in carryover. A diagnostic addendum does not create an ISSUE or certified settlement record.

An archive receipt binds original length/hash, archive path/hash, preserved-body offset, canonical entry mappings, overlap/addendum disposition, carryover and actual next-ID readback. Closure allocates no ID for an already represented event. Remove redundant working copies only after exact archive/readback checks.

## Settlement revision

Add exact final native body receipts, three independent agreeing terminal collectors, actual-start receipt and supporting field semantics. `append_settlement_revision` derives W/L/P from the fixed contracts and final scores. Each revision records reason, revision number, previous revision hash and unchanged issue-core hash. A disputed score, unknown actual start, wrong period or incomplete source quorum stays unresolved and outside performance scoring.

## Retrospective

A failed Rank 1 always requires the Rule R1 deep retrospection (CURRENT_RULES.md). For each event record: observed endpoint/outcome; issued probability and baseline literal; diagnostic surprise without claiming certainty; source, timing and contract validity; predeclared mechanism that occurred; mechanism that did not occur; adjustment vs model effect; and the next testable hypothesis. Review wins under the same evidence criteria as losses. Postgame awards, season-end knowledge and narrative explanation are postgame information.

## Model-only research

Daily shadows contain no P-number, no issued card, no researched lineup claim and no performance-eligible row. Include their family/version, probability vector, input/body/build hashes, forecast/cutoff times, fixture state and provisional source quality. Report all frozen and abstained fixtures in coverage. A diagnostic grade remains a diagnostic grade until separate live admission gates pass.

## Experiment forecasts and canonical cards

The [experiment protocol](research/experiments/NEXT_STEPS.md) defines separate development artifacts and actual-timestamp forecast journals. Creating a draft, power plan, experiment lock or measured result never allocates a P-ID or backfills a historical card. Requested game cards still use the canonical workflow to the active combined log independently of calibration. Retain original `p`, ranking `q`, targets and issued versions; experiment probabilities are PMFs, and `q` is not scored as an event probability.
