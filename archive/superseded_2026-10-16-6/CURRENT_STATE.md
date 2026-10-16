# Current state

**Local keys until import; updated mini after every game (MINI-v1).** Apply [MINI_LOG_IDENTITY_PROTOCOL](MINI_LOG_IDENTITY_PROTOCOL.md). Prompts 1–3 use stable local event keys and never assign/reserve canonical P-IDs; prompt 4 alone assigns them during verified import. After each prompt-1 game request, append the research/addendum, update and read back the mini, and return its complete updated .md document. Preserve every owner-entered Upcoming game block and all earlier issued bytes. New formats: mini-log-10 / mini-settlement-10; earlier records retain their original formats.

**Current release — MDS/P v19.0 / CR-R4 / MINI-v1 / RETAIN-v2:** FORMAT + PROCEDURE: local-key research/settlement, canonical P-ID assignment only in prompt 4, and complete updated mini .md delivery after every game request. New mini-log-10 / mini-settlement-10, C22/S18; EXH-v1 persists. Highest P-600 / next P-601 and all existing records/numerical policies unchanged. [Implementation](research/verification/framework_change_2026-10-16-5/IMPLEMENTATION.md).

**Persistent research and corroboration (EXH-v1).** Apply [RESEARCH_EXHAUSTIVENESS_PROTOCOL](RESEARCH_EXHAUSTIVENESS_PROTOCOL.md) to every required field in research, logging, settlement and verification. If a source is incomplete, open alternatives and verify material facts with another independent source; track every remaining field and attempt. Unresolved facts/corroboration never qualify as complete information. New settlements use mini-settlement-10 with a visible source-discovery/reuse section, three source/attempt/closure CSVs and S17; older originals retain their rules and bytes. Consult [RESEARCH_SOURCE_REGISTER](RESEARCH_SOURCE_REGISTER.md) and prior package registers, recheck actual coverage, and continue discovery beyond them.

**Historical procedural release, 16 October 2026:** MDS/P v17.1 / CR-R2; mandatory online prior-game research and confirmed-player searches, results-store/profile retirement. [Implementation](research/verification/framework_change_2026-10-16-3/IMPLEMENTATION.md). No ID, score, numerical policy or mini-format changes. Earlier release paragraphs retain their historical scope.


**Online history and confirmed players (HIST-2026.10.16-v3 / AVAIL-2026.10.16-v4).** For every game, research both sides' L5/L10/L15/L20 online under [HISTORICAL_SOURCE_PROTOCOL](HISTORICAL_SOURCE_PROTOCOL.md), with opened sources, dated game rows and true n. Seek exact-game confirmed players, starting roles, bench/replacements and absences under [ROSTER_AVAILABILITY_PROTOCOL](ROSTER_AVAILABILITY_PROTOCOL.md); projected players remain unconfirmed. The retired local results store and its derived profiles are not required inputs or fallbacks. Earlier archive-first directions are superseded.

> Maintained by hand. Import, rollover, retrospective and framework changes update this page with the corresponding work. Reconcile current values with the current section of [GAME_LOG_STATUS_CURRENT.md](GAME_LOG_STATUS_CURRENT.md), canonical entries and dated state addenda. A Combined Log opening header is a historical snapshot, not a current allocation record. A genuine current-record disagreement blocks allocation; do not guess or run retired tools named in old headers.

## Authority

**Research retention before model availability (RETAIN-v2).** Retain every identified researched event under its stable local event key regardless of ML/runtime/baseline/calibration availability; use RESEARCH_ONLY_NO_MODEL and an honest execution disposition when needed. Prompts 1–3 neither assign nor reserve canonical P-IDs. Prompt 1 appends the full research card to the mini, updates its intake/footer, reads back the result and returns the complete updated Markdown document after every game request. Prompt 4 alone reconciles duplicates and assigns canonical P-IDs at import, preserving local originals and a local-to-canonical map. Verified labels remain future-development candidates; only real frozen bundles supply expert feedback. See RESEARCH_RETENTION_PROTOCOL and MINI_LOG_IDENTITY_PROTOCOL. Identity/custody/write conflicts remain real blockers; missing ML does not discard research.

Historical retention release: MDS-v17.0 / CR-2026.10.16-R1 / P-v17.0 / SCV-v11; mini-log-9 / mini-settlement-8. The later v18 source-persistence release and current v19 local-key/delivery release supersede these procedure/format defaults. [Retention implementation](research/verification/framework_change_2026-10-16-1/IMPLEMENTATION.md).

**Required repository fallback (REF-v1).** Always keep [https://github.com/danisgreat/Sports-Research/tree/main](https://github.com/danisgreat/Sports-Research/tree/main) as the standing reference. If required local files are not fully accessible (missing, unreadable, truncated or incomplete), retrieve the actual required contents from this repository before declaring them unavailable. Apply [GITHUB_REFERENCE_PROTOCOL](GITHUB_REFERENCE_PROTOCOL.md): resolve one main commit SHA, record exact files/read time and fallback results in the existing reading receipt, and preserve the declared authority mode. Never substitute an unpublished local mini, claim unread content or treat viewing code as executing it. If authorized remote access also fails, record the real gap and continue independent work.

PROCEDURE: MDS-v16.1 / CR-R8 / P-v16.1. [Reference recovery implementation](research/verification/framework_change_2026-10-15-8/IMPLEMENTATION.md). Numerical primary V3, scoring/selection, formats and all allocation/settlement values are unchanged.

FORMAT + PROCEDURE: MDS-v16.0 / CR-R7 / P-v16.0 / PRIMARY-v3.2; SCV-v10 and SEL-v3 unchanged. [Audit and implementation](research/verification/framework_change_2026-10-15-7/IMPLEMENTATION.md). Allocation and existing event/settlement values below are unchanged.

**Strict research completion (15 October 2026):** [RC-2026.10.16-v2](RESEARCH_COMPLETION_PROTOCOL.md) requires full sport-specific research and every contract assessment despite calibration/runtime/lineup/timing/mini blockers, with supported automatic analyst comparisons in a separate NOT_PRIMARY lane and an evidenced A9 completion matrix. P-v15.0 adds this receipt within existing mini-log-7 appendices; no numerical ML/selection/scoring policy, issued record or allocation changes. [Implementation](research/verification/framework_change_2026-10-15-6/IMPLEMENTATION.md).

**Preferred web history recovery (15 October 2026):** [HISTORICAL_SOURCE_PROTOCOL](HISTORICAL_SOURCE_PROTOCOL.md) requires online source research first when exact local history is absent, incomplete or incorrect, across all sports and competitions. Fresh reviewed inputs and exact competition metadata can support the existing primary model without waiting for shared archive repair. Known-at, evidence and unsupported-model checks remain; no dataset refresh or predictive qualification is claimed. [Implementation](research/verification/framework_change_2026-10-15-5/IMPLEMENTATION.md).

**Primary integrity review (15 October 2026):** [PRIMARY-2026.10.15-v3](PRIMARY_PREDICTION_PROTOCOL.md) retains the deterministic mixture and fixes warm-refit known-at leakage, duplicate history/feedback contributions, parameter admission and receipt integrity. Online expert aggregation, not a trained environment-control RL policy. The old replay is proxy evidence with pooling and policy mismatch limits, not validation of the corrected runtime. [Review and implementation](research/verification/framework_change_2026-10-15-4/REVIEW.md). Existing IDs/grades remain unchanged.

**Primary mixture and scheduled-start horizon (15 October 2026):** [PRIMARY-2026.10.15-v2](PRIMARY_PREDICTION_PROTOCOL.md) replaces random Exp3 expert selection with the full-information mixture PRIMARY_HEDGE_MIX_V2 (the earlier proxy replay reported lower Brier; its runtime/parameter/pooling limits are documented in the new integrity review). There is no separate cutoff: the evidence horizon is the game-log scheduled start, and lineups, confirmed starters, bench and news are researched up until then ([TIMING-2026.10.15-v2](TIMING_RESEARCH_PROTOCOL.md)). [Implementation](research/verification/framework_change_2026-10-15-3/IMPLEMENTATION.md). No bundle had been issued under v1.

**Primary ML/RL integration (15 October 2026):** PRIMARY-2026.10.15-v1 authorised model-assisted experimental primary cards from actual receipt-bound per-event runs, with a sporting bandit selecting the distribution and learning only from resolved available feedback (superseded by v2 above). No old DATA_HOLD model is qualified by this change. Unsupported/missing runs remain explicit NO_FORECAST. [Implementation](research/verification/framework_change_2026-10-15-2/IMPLEMENTATION.md).

**Timing update (15 October 2026):** TIMING-2026.10.15-v1 removes all fixed manual research/freeze deadlines and permits research to finish after start. CLEAN_PRE_START_INPUTS describes verified pre-start evidence and no outcome exposure independently of actual issue time. Post-start issuance remains visible and separately scored; it is not a pre-start-issued prospective forecast. [Implementation](research/verification/framework_change_2026-10-15-1/IMPLEMENTATION.md). Existing issued cards, IDs, grades, statistics and model qualification unchanged.

**Availability procedure update (14 October 2026):** [AVAIL-2026.10.14-v1](ROSTER_AVAILABILITY_PROTOCOL.md) and [change receipt](research/verification/framework_change_2026-10-14-4/IMPLEMENTATION.md) require comprehensive starter, bench and absence research for both sides, including obscure competitions. PROCEDURE only; truthful missingness, prediction/selection/scoring rules, formats and model-workshop firewall remain in force. Prompt v11.3 retains this procedure and adds the complete lifecycle/integrity controls.

| Item | Value |
|---|---|
| Status | ACTIVE |
| Method | MDS-2026.10.16-v19.0 (Markdown/CSV/text controls; primary runtime in ml/) |
| Control revision | CR-2026.10.16-R4 ([research retention](research/verification/framework_change_2026-10-16-1/IMPLEMENTATION.md); [GitHub fallback](research/verification/framework_change_2026-10-15-8/IMPLEMENTATION.md); [mandatory ML execution](research/verification/framework_change_2026-10-15-7/IMPLEMENTATION.md); [strict research completion](research/verification/framework_change_2026-10-15-6/IMPLEMENTATION.md); [historical web recovery](research/verification/framework_change_2026-10-15-5/IMPLEMENTATION.md); [mixture integrity review](research/verification/framework_change_2026-10-15-4/REVIEW.md); [primary mixture and scheduled-start horizon](research/verification/framework_change_2026-10-15-3/IMPLEMENTATION.md); [primary ML/RL release](research/verification/framework_change_2026-10-15-2/IMPLEMENTATION.md); [completion-based timing release](research/verification/framework_change_2026-10-15-1/IMPLEMENTATION.md); retains [integrity and lifecycle release](research/verification/framework_change_2026-10-14-5/IMPLEMENTATION.md); [availability procedure](research/verification/framework_change_2026-10-14-4/IMPLEMENTATION.md); retains [workshop/reading-gate/firewall](research/verification/framework_change_2026-10-14-3/IMPLEMENTATION.md)) |
| Scoring version | SCV-2026.10.16-v11 (historical v5-v7 views retained) |
| Selection version | SEL-2026.10.12-v3 / P_ORDER_V2 priced from the actual selected primary ML grid; historical manual mixtures remain in their own cohort; alternatives recorded as shadows |
| Prompt suite | P-2026.10.16-v19.0 (FORMAT + PROCEDURE: local keys, canonical assignment only in prompt 4, complete cumulative .md after each game; MINI-v1 / RETAIN-v2; C22/S18) |
| Mini-log format | `mini-log-10` (in-progress `mini-log-2` through `mini-log-9` retain their format and issued cores) |
| Settlement format | `mini-settlement-10` with source discovery, attempts and closure / S1-S18 (settlement-9 and earlier retain original formats) |
| Freeze | None. Custody is the git history of `main` (CURRENT_RULES §9). Cards record the HEAD SHA they read. The last control manifest, `CONTROL_MANIFEST_2026-10-09-3.md`, is in [archive/controls/](archive/controls/). |
| Highest committed canonical ID | **P-600** |
| Next canonical ID | **P-601** (equal to the line in GAME_LOG_STATUS_CURRENT.md) |
| Reserved IDs | P-518 to P-522 |
| Active Combined Log | [prediction logs/PREDICTION_LOG_COMBINED_7.md](prediction%20logs/PREDICTION_LOG_COMBINED_7.md) |
| Previous parts | Parts 1 to 6, immutable; Part 6 keeps its original P-518 to P-522 source block |
| Final settlement register | **116 retained records: 115 terminal sporting-result reviews + 1 legacy pending P-584**. P-590-P-600 source cohort: 23W/21L/2 definition-unresolved rows, conditional sporting grades only; no operator/model certification. [Current import](research/verification/mini_import_P-590_P-600_2026-10-16-1/CANONICAL_IMPORT_REPORT.md). Earlier dated scoreboards retain their original figures. |

## Selection rules (provisional until the prospective window completes)

- Only Rank 1 and Rank 2 count as wins (Rule T2). A Rank-1 loss gets a deep retrospection (Rule R1). Supplied contracts are reference only (Rule P4).
- `p_card` selection ceiling 90%, never a probability clip. Original Rank-1 gate: at least 62% and a 4-point lead over the best eligible non-complementary alternative. Primary order is decreasing p_card; Rank-2 floor 58% is disclosed. Joint failure is diagnostic; RET03 gate, RET04 different-quantity Rank 2 and XCARD6 diversification are separate frozen shadows. Up to four supported candidates; qualitative/NO_FORECAST research is retained.
- Source: [SELECTION_RULES.md](SELECTION_RULES.md) (status PROVISIONAL).

## Scoreboard

- **Current import (14 October):** P-585-P-589 retain SUPPLIED_FIRST_V1/SF-2 as a separate cohort: 5 numeric research cards, primary 5W/5L (Rank 1 4W/1L, Rank 2 1W/4L), sporting 9W/9L/2PUSH over 20 rows. Frozen paired coverage 4/10 primary rows on 2 events in 1 ISO week; paired Brier 0.251668318 versus baseline 0.229513269, difference +0.022155049, INSUFFICIENT_EVIDENCE. Current P_ORDER_V2 remains unchanged; no clean prospective certification. Prior policy/historical tables below retained. [October 14 report](research/verification/mini_import_P-585_P-589_2026-10-14-1/CANONICAL_IMPORT_REPORT.md).

- **Current v10/v11 import measurement (13 October):** v10 P-580–P-583 = 4 retained events (3 numeric primary, 1 NO_FORECAST), primary 5W/1L, baseline coverage 4/6 rows on 2 events in 1 ISO week; paired Brier card 0.187418187 vs baseline 0.188131225 (difference -0.000713038), INSUFFICIENT_EVIDENCE. V11 P-584 = 1 pending diagnostic-only event, zero eligible primary rows. Historical pre-v10 P-577–P-579 add 5W/1L; current historical inventory 94 forecast cards, 118W/62L plus 8 legacy VOID slots, 65.6% decisive rate; historical Rank 1 58W/33L/3V, Rank 2 60W/29L/5V. The 0-card v10/v11 release snapshot was dated to the framework release and is superseded for current counts by this import; no old card is relabelled or baseline backfilled. Full scoring/queue provenance: [import](research/verification/mini_import_P-577_P-584_2026-10-13-1/CANONICAL_IMPORT_REPORT.md). Clean prospective predictive skill remains unestablished; nothing is performance-certified.
- **Historical v5 snapshot follows:** original cohorts and figures remain unchanged; these are descriptive, not prospective v10 evidence.

Full tables: [research/scoreboard/SCOREBOARD.md](research/scoreboard/SCOREBOARD.md).

- Forecast cards scored: 91 (P-126 to P-576). Gated counted cohort: 0 cards (no card yet carries a recorded Rank-1 gate PASS). RANK1_UNSTABLE cohort: 20 cards (P-557 to P-576), 34 counted wins in 40 live top-two rows = 85.0% (95% interval 70.9% to 92.9%). All forecast cards (historical, ungated): 113 counted wins in 174 live top-two rows = 64.9% (95% interval 57.6% to 71.6%). Rank 1 56-32, Rank 2 57-29, ranks 3-4 106-67 (informational).
- Last cohort retrospective: [2026-10-11](research/verification/retrospective_2026-10-11/RETROSPECTIVE_REPORT.md), new cohort P-557 to P-576 against P-126 to P-556. Rank 1 80.0% (58.4% to 91.9%) does not beat Rank 2 90.0% (69.9% to 97.2%) or ranks 3-4 77.5%. Top-two Brier 0.131 against climatology 0.128 (skill -0.03). Every RANK1_UNSTABLE top-two pair covers itself (stated joint failure 0.0%, realised all-lost 0 of 20). So the counted rate is driven by line construction, and the cohort **does not establish** incremental predictive skill: there were no frozen same-row pregame baselines, and the skill figure uses an in-sample climatology reference, which is descriptive only. *(Wording corrected 2026-10-12, audit R24. The earlier summary said "not skill", which overstated what 20 cards without paired baselines can show. The dated retrospective is unchanged.)* 0 of 20 cards passed the Rank-1 gate; experiment SEL-1 has 1 of 8 week-blocks and no PASS card, so the gate stays provisional. Seven proposals (RET-01 to RET-07) are `PROPOSED_NOT_TESTED` in [HYPOTHESIS_REGISTER.md](HYPOTHESIS_REGISTER.md).
- Nothing here is performance-certified.

## October 14 implementation and integrity status (framework changes 3–5)

The workshop is partly implemented development research, not a qualified predictor. The [current review](research/verification/framework_change_2026-10-14-5/ML_WORKSHOP_REVIEW.md) reconciles actual code and artifacts: 172 discovered competition folders; 29 completed historical models, 1 interrupted/incomplete model, and 142 NOT_MODELLED routes. Four numerical development passes remain DATA_HOLD for source/admission; no prospective lane or model promotion. The [artifact admission record](research/model_shadow/ARTIFACT_PROVENANCE.md) overrides unsupported label/candidate interpretations in old generated cards.

All eight prompts are updated to v11.3; prompt 1 keeps eleven standalone sport/general sections and each section's Upcoming game block. Availability research remains comprehensive, with truthful missingness. Targeted source/receipt/timing/settlement/propensity repairs pass 60 workshop tests. The corrected paper decision replay does not demonstrate RL benefits. [Implementation and release verification](research/verification/framework_change_2026-10-14-5/VERIFICATION_REPORT.md). Canonical IDs, forecasts, grades, scoring/selection and archive datasets are unchanged.

## October 12 implementation status

Framework change [2026-10-12-1](research/verification/framework_change_2026-10-12-1/IMPLEMENTATION.md) implements the 38 audit recommendations of `AUDIT_RECOMMENDATIONS_2026-10-12.txt` and the 10 prediction recommendations, in the audit's order. Item-by-item status and evidence are in its implementation map. Headlines:
- **Archive:** fabricated, unpublished Czech and English builds quarantined outside the repository; both leagues rebuilt from observed fields.
- **Controls:** single authority mode; writer lease, freeze receipt and request intake; settlement revision chains; pre-mutation rechecks; four named byte identities.
- **Toolkit:** corrected tennis, tie and key-number mathematics; retired procedures marked non-operative.
- **Cards:** form windows L5–L20; mixture pricing; line difficulty and baseline coverage; shadows RANK_DELTA and BASE_ONLY; completed two-stage experiment designs.

No log, grade, P-ID or issued card changed. All predictive effects remain untested.

## October 11 implementation status

Prompts 1–8 and their supporting rules/templates/examples are replaced under the user-authorized v10 release. RET-02/05/06/07 are implemented as document/measurement/source-process controls; RET-03/04 are shadow recording protocols, not validated replacements. **Run 2 (same day):** the NBL profile was refreshed to the 2023-25 window (`LP-2026.10.11-v2`; the 2022-24 row is retained as the comparator), the KBO and NPB extra-innings shares were withdrawn as `NOT_ESTIMABLE` after the audit showed placeholder columns, a 29-game 2026-27 NBL snapshot was added to the archive, and the local-machine reachability column of the SOURCES matrix was probed by hand ([implementation](research/verification/framework_change_2026-10-11-2/IMPLEMENTATION.md)). Source lineage audits (SRC-04) and the repair of the archive defects found remain DATA_PENDING. All predictive effects remain untested; FC10-PROFILE-v1 predictive acceptance is BLOCKED_DESIGN. Original RET registrations and the dated retrospective remain unchanged; versioned amendments are in HYPOTHESIS_REGISTER. No log, grade, historical forecast, existing raw CSV or P-ID changed in either release; run 2 added one new partial CSV (`Basketball/NBL/2026`).

## Sources

- Register: [SOURCES.md](SOURCES.md) (rules, source register, adapter statuses, exclusions, reachability matrix). The source adapters and parsers were removed; the routes are used by hand.
- No lineage audit has established independent collection for any source. Treat independence as unknown.

## Models

- **New cards:** MODEL_ASSISTED_PRIMARY_V3 / EXPERIMENTAL_PRIMARY_NOT_CERTIFIED uses the primary runtime and its real receipts. Original historical manual cards remain unchanged. Missing exact-scope data/runtime support means NO_FORECAST, not a fabricated model output. [Primary policy](PRIMARY_PREDICTION_PROTOCOL.md).
- **Model workshop (2026-10-14):** fitted development models exist in [`ml/`](ml/README.md), with outputs and statuses in [research/model_shadow/STATUS.md](research/model_shadow/STATUS.md). All are `HISTORICAL_DEVELOPMENT`; no prospective lane has started, and these old historical outputs remain unadmitted. New primary cards use a separate freshly fitted per-event bundle, not these cached predictions.
- The 2026-10-09 numerical runtime and its model register are archived design notes ([NUMERICAL_MODEL_REGISTER.md](archive/root_documents_2026-10-14/NUMERICAL_MODEL_REGISTER.md)).

## Where things are

| Need | Document |
|---|---|
| Rules | [CURRENT_RULES.md](CURRENT_RULES.md), [METHOD.md](METHOD.md), [SELECTION_RULES.md](SELECTION_RULES.md) |
| Operator prompts | [research/prompts/](research/prompts/README.md), [PROMPTS.md](PROMPTS.md) |
| Card, mini and log formats; self-audit checklists | [CARD_AND_LOG_TEMPLATES.md](CARD_AND_LOG_TEMPLATES.md) |
| Probability tables | [PROBABILITY_TOOLKIT.md](PROBABILITY_TOOLKIT.md) |
| League scoring levels | [LEAGUE_PROFILES.md](LEAGUE_PROFILES.md) |
| Base rates and regimes | [BASE_RATES_REGISTER.md](BASE_RATES_REGISTER.md) |
| Sources and reachability | [SOURCES.md](SOURCES.md) |
| Previous results | [ARCHIVE_USE_GUIDE.md](ARCHIVE_USE_GUIDE.md), [Previous Sports Results/README.md](https://github.com/danisgreat/Sports-Research/blob/2ea94f6f718d1f43c7af9e567008495114ef9cef/Previous%20Sports%20Results/README.md) |
| Scoring | [SCORING_AND_VALIDATION.md](SCORING_AND_VALIDATION.md) |
| Verification | [VERIFICATION_PROTOCOL.md](VERIFICATION_PROTOCOL.md) |
| Proposed improvements | [HYPOTHESIS_REGISTER.md](HYPOTHESIS_REGISTER.md) |
| Retrospective and recommendation status | [FRAMEWORK_RETROSPECTIVE_2026-10-09.md](archive/root_documents_2026-10-14/FRAMEWORK_RETROSPECTIVE_2026-10-09.md); latest cohort retrospective [retrospective_2026-10-11](research/verification/retrospective_2026-10-11/RETROSPECTIVE_REPORT.md) (register status in its §6) |
| Historical root documents archived 2026-10-14 | [Archive index](archive/root_documents_2026-10-14/README.md); [old-path recovery](HISTORICAL_LINK_INDEX.md#root-document-archive-2026-10-14). Navigation change only; all IDs, grades and versions unchanged. |
| Superseded documents | [archive/superseded_2026-10-09/](archive/superseded_2026-10-09/README.md), `archive/controls/` |


**Local research record and updated-document delivery (owner update, 16 October 2026).** Use a stable local event key during research and local settlement; do not assign, reserve or advance any canonical P-ID. Append the researched card regardless of model availability, update intake and the local footer, verify the full mini and return its complete updated .md file after each game request. Prompt 4 alone assigns canonical IDs after duplicate/identity reconciliation and records the immutable local-to-canonical mapping. An already assigned canonical ID remains a reference, never a new pregame allocation. Preserve issued originals and actual timing. See MINI_LOG_IDENTITY_PROTOCOL.

See [RETAIN-v2](RESEARCH_RETENTION_PROTOCOL.md). This owner update changes local identity and delivery procedures; numerical model, selection and scoring formulas are unchanged.


## Current legacy settlement import — 2026-10-16T15:18:45+11:00

Highest canonical **P-600**; next **P-601**; active Combined Log remains Part 7. Inventory **116 retained research records = 115 terminal sporting-result reviews + 1 legacy pending P-584** (104 prior terminal + eleven P-590-P-600 result reviews). Four originals P-597-P-600 added; seven existing originals P-590-P-596 skipped; one P-590 reconciliation addendum and eleven revision-1 settlements retained. [Complete import/readback](research/verification/mini_import_P-590_P-600_2026-10-16-1/CANONICAL_IMPORT_REPORT.md).

The supplied package reports **23 conditional sporting WIN / 21 LOSS / 2 UNRESOLVED** across 46 dependent supplied-contract rows; all eleven events still lack complete operator-action terms and exact final-at/SLA evidence. P-596 Saryarka ML and P-598 Huima −8.5 ML remain UNKNOWN_DEFINITION. These grades retain original rules and analyst roles; no current online-history/lineup compliance, fitted primary model, certified performance or pregame availability is backfilled. Model primary/baseline paired scores remain NOT_COMPUTABLE for this cohort; 37 descriptive analyst rows remain NOT_PRIMARY. Prior score cohorts retain their original figures. Raw carryover: 17 items, 2 closed by canonical-core/owner-result capture, 15 open; older P-581-P-584 and prior operator/time/custody queues remain. No automation scheduled.
