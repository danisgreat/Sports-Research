# Current state

**Historical verification added 17 November 2026 (HPPV-v1, Track H).**
[Registration and operator guide](research/verification/historical_pre_event_v1/README.md)
and [reproducible initial report](research/verification/historical_pre_event_v1/HISTORICAL_PROSPECTIVE_VALIDATION_REPORT.md).
All 685 cards / 3,150 rows are retained, including 280 cards with stated p. No
independent original-custody evidence is inferred: initially 0 Tier-A qualified
cards and **HISTORICAL_EVIDENCE_INSUFFICIENT**. Existing training use and historical
scores remain intact. Track P stays ONE-CHAT-v3 / v29.2, **0 qualifying games /
600-game horizon**, **NOT_YET_DEMONSTRATED** at this snapshot. Counts and verdicts
are separate; no historical rows enter its registry or sequential test.

**Current release — MDS-2026.11.22-v29.2 / CR-2026.11.22-R1 / P-2026.11.22-v29.2 / SCV-2026.11.18-v20: a request that registers can always be carded.** Owner order 22 November 2026, after six `seal-drops` refusals (18–22 November). Registering a new request now runs the card's own line rules (every label carries all its sides; a winner line is empty, so `ML` gets a reason instead of a crash) and refuses one contract registered twice: where no draw is possible, a moneyline and either side's ±0.5 are one winner contract (P-689 counted one AHL result twice). `prepare` reads half-point spreads in no-draw sports as that winner contract. Refusal reasons say how to fix FACTS sources and `not_started_source`; run summaries keep the full reasons. [ONE_CHAT_BRIEF_v29.2](research/external/ONE_CHAT_BRIEF_v29.2.md) adds a checklist before a card is handed over and the rules for a request written by hand. Requests registered earlier, sealed cards, scoring and [EVALUATION_PLAN_v29.0.md](research/external/EVALUATION_PLAN_v29.0.md) are unchanged. [Implementation](research/verification/framework_change_2026-11-22-1/IMPLEMENTATION.md).

**Previous release — MDS-2026.11.18-v29.1 / CR-2026.11.18-R2 / P-2026.11.18-v29.1 / SCV-2026.11.18-v20: read the owner's request text as written.** `ml one-chat prepare` parses shortened team names, colon-optional handicap lines, `Away @ Home` headers, mixed ML+spread requests, and `research/one_chat/SCHEDULE_SOURCES.csv` prefix matching while refusing template placeholders. Statistical constants and [EVALUATION_PLAN_v29.0.md](research/external/EVALUATION_PLAN_v29.0.md) are unchanged. [Runbook §7a](research/one_chat/RUNBOOK.md#7a-writing-the-requests-v291).

**Previous release — MDS-2026.11.18-v29.0 / CR-2026.11.18-R1 / P-2026.11.18-v29.0 / SCV-2026.11.18-v20: several chats a day.** Owner order 18 November 2026 (four chats, up to ten games each). `ml one-chat prepare` drafts each game's request, contracts and card skeleton from the owner's REQ-v5 messages; `register-requests` publishes a whole mini at once; `seal --watch` seals each finished card card by card (an unfinished or changed card no longer blocks the rest) and retries when chats publish at the same time; `intake --from-seals` scores the first sealed copies; a row unsettled 14 days after its scheduled start is dropped by rule with a worst-case sensitivity; a game without a verified first play is excluded instead of stopping the run; per-sport templates are on main. Statistical constants unchanged. [Plan](research/external/EVALUATION_PLAN_v29.0.md), [runbook §7](research/one_chat/RUNBOOK.md), [implementation](research/verification/framework_change_2026-11-18-1/IMPLEMENTATION.md).

**Previous release — MDS-2026.11.17-v28.0 / CR-2026.11.17-R1 / P-2026.11.17-v28.0 / SCV-2026.11.17-v19: review fixes.** Owner order 17 November 2026. The historical evidence command works on Windows (one portable lock, also used by timing corrections) and a Windows CI job guards it; local rehearsal staging is kept apart from the registered seal branch; GitHub activity is fetched only when a server time is needed and a failed fetch is explicit; the confidence sequence uses lambdas (0.5, 0.7, 0.9) and a 600-game horizon, registered with a published power study before any real game; stale pointers and rule contradictions corrected. The initial historical run is unchanged and verifies at its implementation commit; the current verified run is [hppv_runs/2026-11-17-1](research/verification/hppv_runs/2026-11-17-1/README.md) (outputs byte-identical). [Plan](research/external/EVALUATION_PLAN_v29.0.md), [implementation](research/verification/framework_change_2026-11-17-1/IMPLEMENTATION.md).

**Previous release — MDS-2026.11.16-v27.0 / CR-2026.11.16-R4 / P-2026.11.16-v27.0 / SCV-2026.11.16-v18: ONE-CHAT-v3.** Original-request contracts and exact published blobs govern admission; GitHub push activity is independently re-verified; data seals use `forecast-seals`; complete request coverage is required. The confidence sequence targets the changing average conditional advantage, and reports a frozen assessed prefix separately from current performance. [Runbook](research/one_chat/RUNBOOK.md), [plan](research/external/EVALUATION_PLAN_v27.0.md), [implementation](research/verification/framework_change_2026-11-16-4/IMPLEMENTATION.md).

**Historical logs are used.** All 685 cards, 3,150 contract rows: 3,082 admitted (1,291 stated probabilities, 1,791 outcome-only), 68 excluded with reasons. Positive historical study comparisons remain reported. [Per-card audit and historical scores](research/verification/framework_change_2026-11-16-4/historical_evidence/REPORT.md). Running new checks after settlement does not backdate a request, probability or publication time. Current prospective status remains `NOT_YET_DEMONSTRATED` because no actual request/card has yet been sealed under this registration. This is not a statement that no historical learning occurred.

**Previous release - MDS-2026.11.16-v25.0 / CR-2026.11.16-R2 / P-2026.11.16-v25.0 / SCV-2026.11.16-v16: ONE-CHAT-v1.** Owner order 16 November 2026: the card one research chat writes for one game is the measured forecast. Each card ends with an `ONECHAT_V1` block (a probability for both sides of every supplied line, timing header, FACTS table); `ml one-chat intake` reads it, `ml one-chat score` measures it against 0.5 on supplied lines; the first 100 eligible games are the registered cohort and FREEZE-v1 holds until they are assessed. Also: STATS-ONLY-v2 (price-carrying sources may be used with the prices stripped), one version file (`VERSIONS.csv`), the deep loss register and card-game review clocks. [Brief](research/external/ONE_CHAT_BRIEF_v25.0.md), [plan](research/external/EVALUATION_PLAN_v25.0.md), [implementation](research/verification/framework_change_2026-11-16-2/IMPLEMENTATION.md).

**Records and repairs - CR-2026.11.16-R1 (16 November 2026).** On-request comprehensive audit of P-001 to P-685 ([report](research/verification/retrospective_2026-11-16-1/RETROSPECTIVE_REPORT.md)) and four defect repairs that change no forecast or recorded score ([implementation](research/verification/framework_change_2026-11-16-1/IMPLEMENTATION.md)). Method, prompt suite and scoring versions are unchanged. The improvement plan is a proposal awaiting owner decisions ([CHANGE_PROPOSAL](research/verification/framework_change_2026-11-16-1/CHANGE_PROPOSAL.md)).

**Earlier releases (v24.20 and before), dated notes and import sections:** [research/history/CURRENT_STATE_RELEASES.md](research/history/CURRENT_STATE_RELEASES.md); the full record is [CHANGELOG](CHANGELOG.md).

## Authority

Standing protocols (`ENV-v2`, `REF-v2`, `RETAIN-v2`, `MLSCOPE-v3`, `ML-SEP-v1`, `FREEZE-v1`) are summarised in [CORE.md](CORE.md) and linked from [ACTIVE_FILE_INDEX.md](ACTIVE_FILE_INDEX.md).

<!-- BEGIN GENERATED STATE (python -m ml state --write) -->

*Generated from the records; do not edit by hand. A test fails if this block differs from `python -m ml state`.*

| Item | Value |
|---|---|
| Versions (from `VERSIONS.csv`) | MDS-2026.11.22-v29.2 · CR-2026.11.22-R1 · P-2026.11.22-v29.2 · SCV-2026.11.18-v20 · SEL-2026.10.22-v4 |
| Highest canonical ID / next | P-696 / **P-697** (from the import mappings) |
| Historical cards used for training | 696 cards; 3128 admitted contract rows, 1337 with stated p; historical study, not prospective issuance |
| Active local mini | `NONE`; last / next local key `NONE` / `NONE` (footer) |
| Open cards in the active mini | 0 of 0: none |
| Frozen league-day events without settlement | 0: none |
| Learning store | view 15; 5402 events, 5402 results, 8 team-statistic rows, 0 player-availability rows |
| Adjustment ledger | 0 contract rows on 0 cards; 0 adjustment rows |
| Prospective shadow ledger | 12 frozen rows on 2 events (`research/prospective/CYCLE_SHADOW_LEDGER.csv`) |
| Effective settlements (imported local-key rows) | 875 rows, 69 revised by settlement imports, 0 UNRESOLVED |
| Permanently closed unattainable contracts | 9 exact rows; DO_NOT_RETRY; excluded from sporting scores |
| Active releases | none |

<!-- END GENERATED STATE -->

**Versions and pointers (hand-maintained):**

| Item | Value |
|---|---|
| Status | ACTIVE |
| Method | MDS-2026.11.22-v29.2 (generated from VERSIONS.csv) |
| Control revision | CR-2026.11.22-R1 (generated from VERSIONS.csv) |
| Scoring version | SCV-2026.11.18-v20 (generated from VERSIONS.csv) |
| Selection version | SEL-2026.10.22-v4 (generated from VERSIONS.csv) |
| Prompt suite | P-2026.11.22-v29.2 (generated from VERSIONS.csv) |
| Learning pipeline | MLSCOPE-v3 with ML-SEP-v1 (no promoted model) and LEARNLOG-v1; store, ledger and release values are in the generated block above. No active release: MLB-CYCLE-4, NHL-CYCLE-6 and NBA-CYCLE-4 were retired on 16 November 2026 (stale, zero frozen games); the declared card references are unchanged. One-chat intakes and scores: [research/one_chat/](research/one_chat/README.md). |
| Active local mini | NONE (owner instruction 12 November 2026, CR-2026.11.12-R1). The repository holds no active mini. Each research chat starts and keeps its own mini under its own distinct MINI_KEY (WORKFLOW prompt 2: parallel minis use distinct namespaces). The former files, all settled or empty, are in [archive/retired_active_minis_2026-11-12/](archive/retired_active_minis_2026-11-12/README.md) |
| Mini-log format | `mini-log-10` (in-progress `mini-log-2` through `mini-log-9` retain their format and issued cores) |
| Settlement format | `mini-settlement-10` with source discovery, attempts and closure / S1-S19 (settlement-9 and earlier retain original formats) |
| Freeze | None. Custody is the git history of `main` (CURRENT_RULES §9). Cards record the HEAD SHA they read. The last control manifest, `CONTROL_MANIFEST_2026-10-09-3.md`, is in [archive/controls/](archive/controls/). |
| Highest committed canonical ID | **P-696** |
| Next canonical ID | **P-697** (equal to the line in GAME_LOG_STATUS_CURRENT.md) |
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
- **Predictive advantage (ONE-CHAT-v3, v29.2):** NOT_YET_DEMONSTRATED. Cards are being sealed on `forecast-seals` (12 by 22 November 2026, from minis `20261118DA6D9F6251746B979F5895FA` and `20261120-495CEEB69E9540938CF6A7DAA7B546B4`); P-689 is the first with a verified pre-start server seal. The verdict, current mean, lower bound and assessed prefix are printed by `python -m ml one-chat score`. [Plan](research/external/EVALUATION_PLAN_v29.0.md).
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
| Scoring | SCV-2026.11.18-v20 (generated from VERSIONS.csv) |
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

## Settlement, audit, canonical import and archive — 2026-11-22T17:40:00+11:00 (P-686–P-696)

Prompts 3→4 on GitHub mini `20261118DA6D9F6251746B979F5895FA` pulled from `origin/forecast-seals` (10 sealed cards, 12 registered requests) and `origin/card-drops` (`G0001` unsealed card + `G0004` superseded draft). Archived byte-exact at [archive/settled_minis_2026-11-22/20261118DA6D9F6251746B979F5895FA/](archive/settled_minis_2026-11-22/20261118DA6D9F6251746B979F5895FA/README.md). All 11 carded games imported to [Part 11](prediction%20logs/PREDICTION_LOG_COMBINED_11.md) as **P-686–P-696** (46 rows: 23 WIN, 23 LOSS, **0 UNRESOLVED**; Rank 1 8W/3L, Rank 2 5W/6L; card-mean Brier 0.2422, `d = +0.0078` all 11 / `+0.0051` 10 sealed; 22/22 blocks verified byte-exact). Non-card keys `G0004` and `G0007` (`NO_FORECAST`) consumed 0 IDs. 10 deep loss reviews (`DLR-2026-11-22-001`–`010`) appended to `research/deep_loss/DEEP_LOSS_REGISTER.csv`. Track P (`ONE-CHAT-v3`): `P-689` (`G0005`, AHL) is the first game with verified pre-start server seal and official first-play capture; intake saved at `research/one_chat/intake/2026-11-22-1` and captured outcomes at `research/one_chat/outcomes/2026-11-22-1/OUTCOMES.csv`. No predictive advantage is certified; `FREEZE-v1` holds. [Settlement](research/verification/mini_import_P-686_P-696_2026-11-22-1/SETTLEMENT.md), [Audit](research/verification/mini_import_P-686_P-696_2026-11-22-1/AUDIT_REPORT.md), [Import report](research/verification/mini_import_P-686_P-696_2026-11-22-1/CANONICAL_IMPORT_REPORT.md). CARD-TRAIN-v1 rerun: [research/card_training/2026-11-22-1](research/card_training/2026-11-22-1/REPORT.md) (696 cards, 3,128 admitted rows, 1,337 with stated p, 2,904 scored walk-forward; conclusions unchanged).
