# Current state

**Current release ? MDS-2026.11.16-v27.0 / CR-2026.11.16-R4 / P-2026.11.16-v27.0 / SCV-2026.11.16-v18: ONE-CHAT-v3.** Original-request contracts and exact published blobs govern admission; GitHub push activity is independently re-verified; data seals use `forecast-seals`; complete request coverage is required. The confidence sequence targets the changing average conditional advantage, and reports a frozen assessed prefix separately from current performance. [Runbook](research/one_chat/RUNBOOK.md), [plan](research/external/EVALUATION_PLAN_v27.0.md), [implementation](research/verification/framework_change_2026-11-16-4/IMPLEMENTATION.md).

**Historical logs are used.** All 685 cards, 3,150 contract rows: 3,082 admitted (1,291 stated probabilities, 1,791 outcome-only), 68 excluded with reasons. Positive historical study comparisons remain reported. [Per-card audit and historical scores](research/verification/framework_change_2026-11-16-4/historical_evidence/REPORT.md). Running new checks after settlement does not backdate a request, probability or publication time. Current prospective status remains `NOT_YET_DEMONSTRATED` because no actual request/card has yet been sealed under this registration. This is not a statement that no historical learning occurred.

**Previous release - MDS-2026.11.16-v25.0 / CR-2026.11.16-R2 / P-2026.11.16-v25.0 / SCV-2026.11.16-v16: ONE-CHAT-v1.** Owner order 16 November 2026: the card one research chat writes for one game is the measured forecast. Each card ends with an `ONECHAT_V1` block (a probability for both sides of every supplied line, timing header, FACTS table); `ml one-chat intake` reads it, `ml one-chat score` measures it against 0.5 on supplied lines; the first 100 eligible games are the registered cohort and FREEZE-v1 holds until they are assessed. Also: STATS-ONLY-v2 (price-carrying sources may be used with the prices stripped), one version file (`VERSIONS.csv`), the deep loss register and card-game review clocks. [Brief](research/external/ONE_CHAT_BRIEF_v25.0.md), [plan](research/external/EVALUATION_PLAN_v25.0.md), [implementation](research/verification/framework_change_2026-11-16-2/IMPLEMENTATION.md).

**Records and repairs - CR-2026.11.16-R1 (16 November 2026).** On-request comprehensive audit of P-001 to P-685 ([report](research/verification/retrospective_2026-11-16-1/RETROSPECTIVE_REPORT.md)) and four defect repairs that change no forecast or recorded score ([implementation](research/verification/framework_change_2026-11-16-1/IMPLEMENTATION.md)). Method, prompt suite and scoring versions are unchanged. The improvement plan is a proposal awaiting owner decisions ([CHANGE_PROPOSAL](research/verification/framework_change_2026-11-16-1/CHANGE_PROPOSAL.md)).

**Earlier releases (v24.20 and before), dated notes and import sections:** [research/history/CURRENT_STATE_RELEASES.md](research/history/CURRENT_STATE_RELEASES.md); the full record is [CHANGELOG](CHANGELOG.md).

## Authority

**Research retention before model availability (RETAIN-v2).** Defined in [RESEARCH_RETENTION_PROTOCOL](RESEARCH_PROTOCOL.md#part-c-research_retention_protocol); summarised in [CORE](CORE.md) §2.

**Required repository fallback (REF-v2).** Defined in [WORKFLOW](WORKFLOW.md#part-a-execution_environment_protocol) Part A §2 (GitHub `main` at a printed SHA when a local file is unreadable).

**ML/RL scope (MLSCOPE-v3).** Defined in [FORECAST_CYCLE_PROTOCOL](REFERENCE_MODEL_PROTOCOL.md#merged-forecast_cycle_protocol); summarised in [CORE](CORE.md) §7.

**Execution environment (ENV-v2).** Defined in [EXECUTION_ENVIRONMENT_PROTOCOL](WORKFLOW.md#part-a-execution_environment_protocol); summarised in [CORE](CORE.md) §1.

<!-- BEGIN GENERATED STATE (python -m ml state --write) -->

*Generated from the records; do not edit by hand. A test fails if this block differs from `python -m ml state`.*

| Item | Value |
|---|---|
| Versions (from `VERSIONS.csv`) | MDS-2026.11.16-v27.0 · CR-2026.11.16-R4 · P-2026.11.16-v27.0 · SCV-2026.11.16-v18 · SEL-2026.10.22-v4 |
| Highest canonical ID / next | P-685 / **P-686** (from the import mappings) |
| Historical cards used for training | 685 cards; 3082 admitted contract rows, 1291 with stated p; historical study, not prospective issuance |
| Active local mini | `NONE`; last / next local key `NONE` / `NONE` (footer) |
| Open cards in the active mini | 0 of 0: none |
| Frozen league-day events without settlement | 0: none |
| Learning store | view 15; 5402 events, 5402 results, 8 team-statistic rows, 0 player-availability rows |
| Adjustment ledger | 0 contract rows on 0 cards; 0 adjustment rows |
| Prospective shadow ledger | 12 frozen rows on 2 events (`research/prospective/CYCLE_SHADOW_LEDGER.csv`) |
| Effective settlements (imported local-key rows) | 829 rows, 69 revised by settlement imports, 0 UNRESOLVED |
| Permanently closed unattainable contracts | 9 exact rows; DO_NOT_RETRY; excluded from sporting scores |
| Active releases | none |

<!-- END GENERATED STATE -->

**Versions and pointers (hand-maintained):**

| Item | Value |
|---|---|
| Status | ACTIVE |
| Method | MDS-2026.11.16-v26.0 (ONE-CHAT-v2: sealed cards, committed inputs, anytime-valid demonstration); previous MDS-2026.11.16-v25.0 (ONE-CHAT-v1: the chat's card is the measured forecast; STATS-ONLY-v2); earlier versions: [history](research/history/CURRENT_STATE_RELEASES.md) |
| Control revision | CR-2026.11.16-R3 (ONE-CHAT-v2 release); previous CR-2026.11.16-R2 (ONE-CHAT-v1 release); earlier versions: [history](research/history/CURRENT_STATE_RELEASES.md) |
| Scoring version | SCV-2026.11.16-v17 (section 16: the anytime-valid demonstration); previous SCV-2026.11.16-v16 (section 15: the measured-card assessment); earlier versions: [history](research/history/CURRENT_STATE_RELEASES.md) |
| Selection version | SEL-2026.10.22-v4 for cards with a `PICKS_V2` block (a probability for every contract, most-likely list, information list, abstain flag); SEL-2026.10.12-v3 / P_ORDER_V2 retained for earlier cards, whose Rank-1 gate and Rank-2 floor stay as written for them; historical manual mixtures remain in their own cohort |
| Prompt suite | P-2026.11.16-v26.0 (prompts 3, 4 and 6: sealing, committed inputs, the anytime verdict); previous P-2026.11.16-v25.0 (prompts 3, 4 and 6 run the ONE-CHAT-v1 intake, scoring and deep loss register); earlier versions: [history](research/history/CURRENT_STATE_RELEASES.md) |
| Learning pipeline | MLSCOPE-v3 with ML-SEP-v1 (no promoted model) and LEARNLOG-v1; store, ledger and release values are in the generated block above. No active release: MLB-CYCLE-4, NHL-CYCLE-6 and NBA-CYCLE-4 were retired on 16 November 2026 (stale, zero frozen games); the declared card references are unchanged. One-chat intakes and scores: [research/one_chat/](research/one_chat/README.md). |
| Active local mini | NONE (owner instruction 12 November 2026, CR-2026.11.12-R1). The repository holds no active mini. Each research chat starts and keeps its own mini under its own distinct MINI_KEY (WORKFLOW prompt 2: parallel minis use distinct namespaces). The former files, all settled or empty, are in [archive/retired_active_minis_2026-11-12/](archive/retired_active_minis_2026-11-12/README.md) |
| Mini-log format | `mini-log-10` (in-progress `mini-log-2` through `mini-log-9` retain their format and issued cores) |
| Settlement format | `mini-settlement-10` with source discovery, attempts and closure / S1-S19 (settlement-9 and earlier retain original formats) |
| Freeze | None. Custody is the git history of `main` (CURRENT_RULES §9). Cards record the HEAD SHA they read. The last control manifest, `CONTROL_MANIFEST_2026-10-09-3.md`, is in [archive/controls/](archive/controls/). |
| Highest committed canonical ID | **P-685** |
| Next canonical ID | **P-686** (equal to the line in GAME_LOG_STATUS_CURRENT.md) |
| Reserved IDs | P-518 to P-522 |
| Active Combined Log | [prediction logs/PREDICTION_LOG_COMBINED_11.md](prediction%20logs/PREDICTION_LOG_COMBINED_11.md) |
| Previous parts | Parts 1 to 8, immutable; Part 6 keeps its original P-518 to P-522 source block; Part 7 closed with 51 originals P-550 to P-600; Part 8 closed with 22 originals P-601 to P-622; Part 9 closed 14 November 2026 with 37 originals P-623 to P-659; Part 10 closed 16 November 2026 with 26 originals P-660 to P-685 |
| Final settlement register | 153 retained records through P-637 (previous138 plus15 originals P-623–P-637), plus the separately imported historical P-638; P-584 is terminal. All new event finals established; the 2 Be1–Neptunas corner directions (P-630 R1/R6) are permanently closed UNATTAINABLE. Old rows, cohorts and later revisions remain in their original reports; the R3 report and globalqueue describe current limits. |

## Selection rules (provisional until the prospective window completes)

- Only Rank 1 and Rank 2 count as wins (Rule T2). A Rank-1 loss gets a deep retrospection (Rule R1). Supplied contracts are reference only (Rule P4).
- `p_card` selection ceiling 90%, never a probability clip. Original Rank-1 gate: at least 62% and a 4-point lead over the best eligible non-complementary alternative. Primary order is decreasing p_card; Rank-2 floor 58% is disclosed. Joint failure is diagnostic; RET03 gate, RET04 different-quantity Rank 2 and XCARD6 diversification are separate frozen shadows. Up to four supported candidates; qualitative/NO_FORECAST research is retained.
- Source: [SELECTION_RULES.md](RULES_REFERENCE.md#part-b-selection_rules) (status PROVISIONAL).

## Scoreboard

- **Summary from the records (CARD-TRAIN-v1 run [2026-11-16-1](research/card_training/2026-11-16-1/REPORT.md), all settled cards P-001 to P-685).** 3,082 decisive rows on 656 cards. Rank 1: 381 W / 228 L, 62.6% (58.7% to 66.3%). Rank 2: 331 W / 249 L, 57.1% (53.0% to 61.0%). Ranks 3 and 4: 618 W / 494 L, 55.6%. Rows with a stated probability: 1,291 on 280 cards, Brier 0.2311, card-mean difference against a constant 0.5 of -0.0204 [-0.0312, -0.0096]; November chat-research rows -0.0017 [-0.0292, +0.0259] on 32 cards. 1,791 rows (58%) carry no number. Outcome-exposed and descriptive; no frozen same-row baseline exists for any of these cards.
- **Predictive advantage (ONE-CHAT-v2):** NOT_YET_DEMONSTRATED with 0 games: the sequence starts with the first card sealed before play. The verdict, e-value and lower bound are printed by `python -m ml one-chat score`. Historical context only (unsealed, not confirmatory): [historical evidence](research/verification/framework_change_2026-11-16-3/historical_evidence/HISTORICAL_EVIDENCE.csv).
- **Audit and its findings:** [on-request audit of 16 November 2026](research/verification/retrospective_2026-11-16-1/RETROSPECTIVE_REPORT.md).
- Earlier scoreboard notes (13 October to 10 November) and the 11 October retrospective summary: [history](research/history/CURRENT_STATE_RELEASES.md).
Full tables: [research/scoreboard/SCOREBOARD.md](research/scoreboard/SCOREBOARD.md).

- Nothing here is performance-certified.

**Implementation notes of 11–14 October 2026:** [research/history/CURRENT_STATE_IMPLEMENTATION_NOTES.md](research/history/CURRENT_STATE_IMPLEMENTATION_NOTES.md).

## Sources

- Register: [SOURCES.md](SOURCES.md) (rules, source register, adapter statuses, exclusions, reachability matrix). The source adapters and parsers were removed; the routes are used by hand.
- No lineage audit has established independent collection for any source. Treat independence as unknown.

## Models

- **New cards:** ANALYST_PRIMARY_V1 / UNCALIBRATED_ANALYST_PRIMARY, the frozen reference plus logged adjustments (ADJUSTMENTS_V1); code does the reference, the linter, the ledger and the freeze (MLSCOPE-v3). Historical MODEL_ASSISTED cards keep their labels. Rows that cannot be supported are bounded, qualitative or NO_FORECAST, never fabricated. The ML/RL workshop is used only in prompts 6 and 8.
- **Model workshop (2026-10-14):** fitted development models exist in [`ml/`](ml/README.md), with outputs and statuses in [research/model_shadow/STATUS.md](research/model_shadow/STATUS.md). All are `HISTORICAL_DEVELOPMENT`; no prospective lane has started, and these old historical outputs remain unadmitted. New primary cards use a separate freshly fitted per-event bundle, not these cached predictions.
- The 2026-10-09 numerical runtime and its model register are archived design notes ([NUMERICAL_MODEL_REGISTER.md](archive/root_documents_2026-10-14/NUMERICAL_MODEL_REGISTER.md)).

## Where things are

| Need | Document |
|---|---|
| Rules | [CURRENT_RULES.md](RULES_REFERENCE.md#part-a-current_rules), [METHOD.md](CORE.md#merged-method), [SELECTION_RULES.md](RULES_REFERENCE.md#part-b-selection_rules) |
| Operator prompts | [research/prompts/](research/prompts/README.md), [PROMPTS.md](PROMPTS.md) |
| Card, mini and log formats; self-audit checklists | [CARD_AND_LOG_TEMPLATES.md](CARD_AND_LOG_TEMPLATES.md) |
| Probability tables | [PROBABILITY_TOOLKIT.md](PROBABILITY_TOOLKIT.md) |
| League scoring levels | [LEAGUE_PROFILES.md](PARAMETERS.md#part-d-league_profiles) |
| Base rates and regimes | [BASE_RATES_REGISTER.md](PARAMETERS.md#part-c-base_rates_register) |
| Sources and reachability | [SOURCES.md](SOURCES.md) |
| Previous results | [ARCHIVE_USE_GUIDE.md](ARCHIVE_USE_GUIDE.md), [Previous Sports Results/README.md](https://github.com/danisgreat/Sports-Research/blob/2ea94f6f718d1f43c7af9e567008495114ef9cef/Previous%20Sports%20Results/README.md) |
| Scoring | [SCORING_AND_VALIDATION.md](SCORING_AND_VALIDATION.md) |
| Verification | [VERIFICATION_PROTOCOL.md](VERIFICATION_PROTOCOL.md) |
| Proposed improvements | [HYPOTHESIS_REGISTER.md](HYPOTHESIS_REGISTER.md) |
| Retrospective and recommendation status | [FRAMEWORK_RETROSPECTIVE_2026-10-09.md](archive/root_documents_2026-10-14/FRAMEWORK_RETROSPECTIVE_2026-10-09.md); latest audit [retrospective_2026-11-16-1](research/verification/retrospective_2026-11-16-1/RETROSPECTIVE_REPORT.md) (on request, P-001 to P-685) with its [improvement plan](research/verification/framework_change_2026-11-16-1/CHANGE_PROPOSAL.md); earlier cohort retrospectives of 11, 16 and 21 October under research/verification/ |
| Historical root documents archived 2026-10-14 | [Archive index](archive/root_documents_2026-10-14/README.md); [old-path recovery](HISTORICAL_LINK_INDEX.md#root-document-archive-2026-10-14). Navigation change only; all IDs, grades and versions unchanged. |
| Superseded documents | [archive/superseded_2026-10-09/](archive/superseded_2026-10-09/README.md), `archive/controls/` |

**Local research record and updated-document delivery (owner update, 16 October 2026).** Defined in [MINI_LOG_IDENTITY_PROTOCOL](WORKFLOW.md#part-b-mini_log_identity_protocol); summarised in [CORE](CORE.md) §2.

## Combined Log rollover — 2026-11-16T19:19:56+11:00

Active destination: [Part 11](prediction%20logs/PREDICTION_LOG_COMBINED_11.md); Part 10 closed after 1,530,426 bytes / 26 originals P-660–P-685 (1.5 MB threshold exceeded; owner order of 16 November). Highest P-685 / next P-686 and reserved P-518–P-522 unchanged by the rollover; zero IDs consumed. [Rollover receipt](research/verification/combined_rollover_2026-11-16-1/README.md), [queue continuity](research/verification/combined_rollover_2026-11-16-1/QUEUE_CONTINUITY.md).

## Settlement revisions import — 2026-11-16T19:22:52+11:00

Prompts 3→4 under the owner order of 16 November (S-1). The 53 rows left UNRESOLVED by the 14 and 15 November imports (P-647, P-661, P-662, P-664, P-678, P-683) are settled as revision-2 from the captures the owner's source recovery saved: 26 WIN, 27 LOSS; the effective view now holds 0 UNRESOLVED rows. The two WBBL six-over grades rest on a one-run threshold bound; three second-lineage checks stay open with grades settled. One deep loss review (P-662, first lean). Six addendum blocks appended to Part 11 with exact readback. [Report](research/verification/settlement_import_2026-11-16-1/CANONICAL_IMPORT_REPORT.md). CARD-TRAIN-v1 rerun: [research/card_training/2026-11-16-1](research/card_training/2026-11-16-1/REPORT.md) (3,082 rows admitted, 2,858 scored; conclusions unchanged).
