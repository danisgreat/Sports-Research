# Scope and data inventory — retrospective 2026-10-21 (P-601–P-622)

Written before the analysis tables in [COHORT_TABLES.md](COHORT_TABLES.md). Prompt 6, `P-2026.10.17-v22.2 · COHORT_RETROSPECTIVE · LOCAL_WORKING_TREE`, MLSCOPE-v1 ML/RL review, LEARN-v1 §§6–8. Trigger: **user request**. No learning-status clock was due (below).

## Repository and timing receipt

| Item | Value |
|---|---|
| HEAD at start | `06f9538d6c21273e21d9cc8f1900cd1ad3231579` (= `origin/main` by `git ls-remote`, 2026-10-21 ≈01:37 AEDT; `git fetch` fails on Drive `desktop.ini` files inside `.git/refs`, a known local defect) |
| Dirty inventory at start | untracked `BASKETBALL.txt` and `MINI LOGS TO BE SETTLED/` (owner/peer, not touched or staged) |
| Snapshot | 2026-10-21T01:19:51+11:00 (scope frozen); report written 01:37–02:10 AEDT |
| Outcome exposure | **Retrospective / outcome-exposed.** Every outcome was seen during prompt 3 (20–21 Oct) and prompt 4 (21 Oct) in this same session before this review. |
| Prior exposure of the reviewer | This session wrote the prompt-3 settlement documents for MELILL01, Q7N4T9B2, K9V4R2M7F6, X7Q4M9R2 and 79B3 revision-2, and the prompt-4 import. The review is therefore not independent of the settlement. |

## Reading receipt (actually read in this task)

Full: `research/prompts/6_COMBINED_LOG_RETROSPECTIVE.md`; `LEARNING_PIPELINE_PROTOCOL.md` (read in full earlier this session). Sections: `research/prompts/COMMON_OPERATING_PROTOCOL.md` lines 9–32 (scope, LEARN-v2, prompt table); `VERIFICATION_PROTOCOL.md` §5 and the LEARN-v1 section; `RESEARCH_RETENTION_PROTOCOL.md` §§3–5; `HYPOTHESIS_REGISTER.md` headings and the two 2026-10-16 retrospective sections; `CHANGELOG.md` top entries; `research/scoreboard/SCOREBOARD.md` first 60 lines; `research/learning_status/REVIEW_LOG.csv`; the import package `research/verification/mini_import_P-601_P-622_2026-10-21-1/` (README, CANONICAL_IMPORT_REPORT §§ Reconciliation–end, VERIFICATION, UNRESOLVED_POST_IMPORT, LOCAL_ID_MAPPING, EFFECTIVE_SETTLEMENT_ROWS, the settlement documents' Learning record / SETTLEMENT_MANIFEST / MINI_SETTLEMENT sections); Part 8 settlement wrappers (expected-versus-final and Rank-1 loss review lines for P-612–P-622, P-606 revision-1). Code read: `ml/evaluation/card_history.py` (inputs), `ml/research_ingest.py`, `ml/research_learning.py`, `ml/learning_status.py` (review reading), `ml/primary.py` (`settle`, CLI), `ml/endpoint.py`.

`SCORING_AND_VALIDATION.md` and the remaining VERIFICATION_PROTOCOL sections were read during prompts 3–4 of this session, not re-read here. No GitHub fallback was needed (all local files readable).

## Scope

| Field | Value |
|---|---|
| Cohort | P-601–P-622 (22 canonical events, imported 2026-10-21, commit `06f9538`) |
| Event dates (local) | 16 Oct (P-601–P-608), 17 Oct (P-609–P-611), 18 Oct (P-612–P-617, P-619–P-622), 20 Oct (P-618) — ISO weeks 2026-W42 (21 events) and 2026-W43 (P-618) |
| Formats | mini-log-10 cards; mini-settlement-10 settlements; 79B3 R1 package (legacy mini-settlement-10 from an external chat) |
| Policy cohorts | **RESEARCH_ONLY_NO_MODEL** P-601–P-611 (analyst values NOT_PRIMARY; p_card NOT_ESTIMATED) · **ANALYST_PRIMARY_V1 / UNCALIBRATED** P-612–P-622 |
| Issuance strata | P-612–P-618 owner-saved `READ_ONLY_DRAFT / NOT_ISSUED`; P-619–P-622 issue phase UNVERIFIED; no card has a verified pre-start issue |
| Timing strata | verified POST_START: P-610, P-613, P-615, P-618, P-622; others UNVERIFIED; no CLEAN_PRE_START_INPUTS card |
| Evidence strata | A, B, C, E, X per row (EFFECTIVE_SETTLEMENT_ROWS) |
| Baselines | frozen same-row BASELINE_P on P-612 (4 rows) and P-621 (4 rows) only; none reconstructed |
| Pending / unresolved | P-620 winner call pending (contracts terminal); P-604 corners UNRESOLVED (2 rows); P-616 OT definition UNRESOLVED (grade-changing) |
| Excluded | Legacy pending P-584 (no new settlement); held `LOCAL-20261018MELILL01-G0004` (no canonical ID); unimported `SETTLEMENT_20261016A691119714D1_REV1_COMPLETE.zip` (8 events, never imported); empty mini `2026101710538263F6ED` (0 cards) except its frozen model shadow, which is audited separately in §3 of the report |
| NO_FORECAST / qualitative / duplicate requests | none in the cohort; P-601 analyst values NOT_ESTIMATED (research-only) |
| Comparisons | card v frozen BASELINE_P (same rows only); card-history full-history context; frozen model shadow (unpaired) |

## Inventory by ID

| ID | Local key | Sport / competition | Cohort | Rows (W/L/P/U) | Effective revision | Learning-store result | Label candidate |
|---|---|---|---|---|---|---|---|
| P-601 | 79B3-G0001 | Soccer / CSL | RESEARCH_ONLY | 6 (3/3/0/0) | revision-1 | 0–1, 2 sources (corroborating); corners 5–4 | revision-1, 8 labels |
| P-602 | 79B3-G0002 | Soccer / UAE Pro League | RESEARCH_ONLY | 6 (3/3/0/0) | revision-1 | 5–1, 1 source | revision-1, 8 |
| P-603 | 79B3-G0003 | Soccer / ISL | RESEARCH_ONLY | 6 (3/3/0/0) | rev-1 (4) + rev-2 corners (2) | 1–2, 2 sources; corners 1–5 | revision-1 (6) + revision-2 (2) |
| P-604 | 79B3-G0004 | Soccer / Algeria Ligue 1 | RESEARCH_ONLY | 6 (2/2/0/2) | rev-1 (4) + rev-2 corners UNRESOLVED (2) | 2–1, 1 source; corners 8–5 (new single source, grades unchanged) | revision-1 (6); revision-2 none (UNRESOLVED) |
| P-605 | 79B3-G0005 | Ice Hockey / Liiga | RESEARCH_ONLY | 4 (2/2/0/0) | revision-1 | 3–1 regulation, end 17:48:47Z | revision-1, 6 |
| P-606 | 79B3-G0006 | Basketball / NBA preseason | RESEARCH_ONLY | 4 (2/2/0/0) | revision-1 | **116–98** (2 sources; settlement says 117–98 — finding F-01) | revision-1, 6 |
| P-607 | 79B3-G0007 | Ice Hockey / NHL | RESEARCH_ONLY | 4 (2/2/0/0) | revision-1 | COL 5–2 PIT | revision-1, 6 |
| P-608 | 79B3-G0008 | Basketball / NBA preseason | RESEARCH_ONLY | 4 (2/2/0/0) | revision-1 | GSW 128–118 POR | revision-1, 6 |
| P-609 | 79B3-G0009 | Rugby union / Test | RESEARCH_ONLY | 4 (2/2/0/0) | revision-1 | AUS 21–43 NZ | revision-1, 6 |
| P-610 | 79B3-G0010 | Basketball / B.League Premier | RESEARCH_ONLY | 4 (2/2/0/0) | revision-2 | 71–89, last PBP 07:15:35Z | revision-2, 6 |
| P-611 | 79B3-G0011 | Basketball / NBL | RESEARCH_ONLY | 4 (2/2/0/0) | revision-2 | 115–83 | revision-2, 6 |
| P-612 | MELILL01-G0001 | Basketball / NBL | ANALYST_PRIMARY_V1 | 4 (2/2/0/0) | revision-1 | 89–91 | revision-1, 6 |
| P-613 | MELILL01-G0002 | Cricket ODI | ANALYST_PRIMARY_V1 | 4 (2/2/0/0) | revision-1 | PAK 305 – SL 268 | revision-1, 6 |
| P-614 | MELILL01-G0003 | Basketball / Czech women | ANALYST_PRIMARY_V1 | 4 (2/2/0/0) | revision-1 | 82–51, 2 sources | revision-1, 6 |
| P-615 | Q7N4-G0001 | Basketball / B.League One | ANALYST_PRIMARY_V1 | 4 (2/2/0/0) | revision-1 | 82–89, last PBP 08:49:16Z | revision-1, 6 |
| P-616 | Q7N4-G0002 | Basketball / PBA | ANALYST_PRIMARY_V1 | 4 (1/1/2/0) | revision-1 | 112–114 OT (reg 106–106) | revision-1, 4 score labels only (contract grades definition-unresolved) |
| P-617 | Q7N4-G0003 | Soccer / LaLiga | ANALYST_PRIMARY_V1 | 6 (3/3/0/0) | revision-1 | 2–0; corners 7–4 | revision-1, 8 |
| P-618 | Q7N4-G0004 | Baseball / KBO | ANALYST_PRIMARY_V1 | 4 (2/2/0/0) | revision-1 | LG 1–13 KIA, end 21:58 KST | revision-1, 6 |
| P-619 | K9V4-G0001 | Soccer / J1 | ANALYST_PRIMARY_V1 | 8 (5/3/0/0) | revision-1 | 3–0; corners not ingested (providers disagree 6 v 7) | revision-1, 10 |
| P-620 | X7Q4-G0001 | Cricket / Test | ANALYST_PRIMARY_V1 | 4 (2/2/0/0) | revision-1 | not ingested — match pending at freeze | none (pending) |
| P-621 | X7Q4-G0002 | Basketball / LBA | ANALYST_PRIMARY_V1 | 4 (2/2/0/0) | revision-1 | 82–98 | revision-1, 6 |
| P-622 | X7Q4-G0003 | Cricket / Women's T20I | ANALYST_PRIMARY_V1 | 4 (2/2/0/0) | revision-1 | IND-W 104 – ZIM-W 102 | revision-1, 6 |

Totals: 102 contract rows = 52 research-only (25W/25L/0P/2U) + 50 primary-cohort (25W/23L/2P/0U); 21 events ingested; 22 label candidates (136 labels). No conflicting revision branches (R17 chains single-parent, import VERIFICATION check 11). Original p values are taken only from the import's EFFECTIVE_SETTLEMENT_ROWS, which copies the frozen cores; none was recovered from summaries.

## Source blocks

Cards and settlements are the canonical wrappers in [Part 8](../../../prediction%20logs/PREDICTION_LOG_COMBINED_8.md) (post-import SHA-256 `2d799865…79d2`, unchanged by this task). Preserved inputs: `../mini_import_P-601_P-622_2026-10-21-1/inputs/`. Result captures for the learning store are outside the repository in `C:\Users\danie\Documents\SportsResearch-captures\retrospective-2026-10-21\` (24 files, hashes in [LEARN_EXPORT/CAPTURE_INVENTORY.csv](LEARN_EXPORT/CAPTURE_INVENTORY.csv)).
