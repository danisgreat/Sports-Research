# Canonical import P-601–P-622 — 21 October 2026

Authority LOCAL_WORKING_TREE; branch `main`, base HEAD `3e29a58693e2ed02ff862e9bf0f751af2feadee1` (= last fetched `origin/main`; `git fetch` failed on the known `refs/agents/desktop.ini` ref). Owner-invoked prompt 4 (P-2026.10.17-v22.2). Import applied **2026-10-21T01:07:13+11:00** (clock read). MLSCOPE-v1: no model, runtime, shadow or learning command was run; the only repository code executed was the structural checker `python -m ml primary verify-log --mini`, which prompt 4 names for that purpose. Helper scripts for hashing, planning and readback stayed outside the repository.

## Owner decisions taken during this import (2026-10-21)

1. **Q7N4T9B2 G0004 (KIA @ LG, semi-PO Game 3):** its source footer called the ordinal "not consumed … do not automatically consume". The owner chose to import it now. It keeps its literal `READ_ONLY_DRAFT / NOT_ISSUED / POST_SCHEDULED_START` status.
2. **MELILL01 intake defect:** `<!-- END CARD LOCAL-20261018MELILL01-G0004 -->` at source byte 140,884 has no BEGIN marker, while the footer declares four cards (`verify-log`: "mini card markers orphaned/unbalanced"). The owner chose to import G0001–G0003 and **hold G0004** (Beijing Guoan v Qingdao West Coast). Nothing was repaired; the held section and its settlement block are preserved and receive no ID.

## Sources, freeze and step-0 intake

Every source was copied byte-for-byte into [inputs/](inputs/) and re-hashed after writing ([SOURCE_FILE_INVENTORY.csv](SOURCE_FILE_INVENTORY.csv)). Prompt-3 FROZEN_SOURCE fields marked PENDING_PROMPT_4 are completed in [FROZEN_SOURCE_RECEIPTS.csv](FROZEN_SOURCE_RECEIPTS.csv). Each `PREDICTION_MINI_SETTLED.md` is the frozen mini followed by its settlement document, and starts with the exact frozen prefix (checked for all six).

| Mini | Frozen source (bytes · SHA-256) | Card markers | Settlement input | Disposition |
|---|---|---|---|---|
| 2026101679B3FBCC8D | 313,155 · `b7478342…ad7e` = the declared revision-1 FROZEN_SOURCE, verified as the exact prefix of the R1 settled file (387,500 · `6cfea59c…0ee6`) | G0001–G0011 + 2 G0001 addenda | R1 package (revision-1 ×11) + revision-2 document (G0010, G0011, G0003/G0004 corner keys) | 11 new events P-601–P-611 |
| 20261018MELILL01 | 142,555 · `f5163079…e245` (Downloads, saved 2026-10-21 00:21) | 3 balanced + 1 orphan END | prompt-3 revision-1 | P-612–P-614; G0004 HELD_INTAKE_DEFECT |
| 20261018Q7N4T9B2 | 172,799 · `89146dbb…c85d` (Downloads, 00:21) | G0001–G0004 | prompt-3 revision-1 | P-615–P-618 |
| 20261018K9V4R2M7F6 | 47,340 · `2324baf0…98d2` (Downloads, 00:22) | G0001 | prompt-3 revision-1 | P-619 |
| 20261018X7Q4M9R2 | 150,699 · `8bca9a3e…2748` (Downloads, 00:22) | G0001–G0003 | prompt-3 revision-1 | P-620–P-622 |
| 2026101710538263F6ED | 12,311 · `f8c680b5…aba6a` | none (empty mini) | prompt-3 document (no cards) | 0 IDs (empty mini consumes none) |

All files are LF-only, no BOM, one `MINI-LOG-FORMAT` marker each. **Structural check:** `verify-log` passed the empty mini (0 cards) and correctly failed MELILL01 on the orphan marker. It failed the other minis with "a no-code mini needs one hand-derived analysis status per card": their cards state the disposition with other wordings (`Probability method:`, `Analysis / information status:`, `Card class:`), and the 79B3 cards are pre-MLSCOPE `RESEARCH_ONLY_NO_MODEL`. Under prompt 4's retention rule the same check was done by hand: every card has exactly one honest probability-method disposition (11 × `RESEARCH_ONLY_NO_MODEL` with analyst diagnostics NOT_PRIMARY; 11 × `ANALYST_PRIMARY_V1 / UNCALIBRATED_ANALYST_PRIMARY`). `MODEL_ASSISTED_CYCLE_V1` appears in the 79B3 G0005/G0010 cores only as a description of the unavailable runtime. This is recorded as a format non-conformance, not repaired.

**Other source copies.** `inputs/2026101679B3FBCC8D/EARLIER_COPY_…md` (218,460 bytes) is an earlier cumulative copy (G0001–G0007, diverges from the frozen source at byte 13,950 in §D); retained as a historical copy only. Its seven card bodies are not the import source. The three prompt-3 evidence-only reviews of NOT_ISSUED drafts (four-, five- and seven-game) plus the DRAFT-E06 revision-2 are retained under [inputs/documentary_no_canonical_event/](inputs/documentary_no_canonical_event/): their original draft cards were never supplied and have no local keys, so they create no canonical event.

## Reconciliation and allocation

Current state before import: highest **P-600**, next **P-601**, reserved P-518–P-522, active Part 8 with zero originals (CURRENT_STATE, GAME_LOG_STATUS_CURRENT and Part 8 agree). Highest was also recomputed from every `BEGIN CANONICAL RESEARCH` marker in Parts 1–8. Duplicate search: all 22 events (teams, competition, 16–20 October dates) were searched across Parts 1–8 — no canonical block exists for any of them. The unimported Downloads package `SETTLEMENT_20261016A691119714D1_REV1_COMPLETE.zip` (8 different 16–17 Oct events, incl. KBO semi-PO **Game 1**) was checked for overlap: none. It was not supplied for this task and was not imported.

**Declared source order:** minis by the scheduled start of their earliest card — 79B3 (16 Oct 22:35 AEDT), MELILL01 (18 Oct 17:00), Q7N4 (17:35), K9V4 (18:00), X7Q4 (19:00) — then local ordinal. Result: **22 contiguous new IDs P-601–P-622**; zero reused, zero skipped, reserved range untouched; empty mini, held card, addenda and settlement revisions consumed none. Final mapping: [LOCAL_ID_MAPPING.csv](LOCAL_ID_MAPPING.csv). Prompt-3 NOT_ASSIGNED mappings inside the settlement documents are unchanged (frozen pre-import mapping).

| P-ID | Local key | Event |
|---|---|---|
| P-601 | LOCAL-2026101679B3FBCC8D-G0001 | CSL · Henan FC v Tianjin Jinmen Tiger · 16 Oct |
| P-602 | …-G0002 | UAE Pro League · Al Dhafra v Dubai United · 16 Oct |
| P-603 | …-G0003 | ISL · SC Delhi v Mohun Bagan SG · 16 Oct |
| P-604 | …-G0004 | Algeria Ligue 1 · Olympique Akbou v ES Ben Aknoun · 16 Oct |
| P-605 | …-G0005 | Liiga · HPK v Ilves · 16 Oct |
| P-606 | …-G0006 | NBA preseason · Hornets @ Grizzlies · 16 Oct (US) |
| P-607 | …-G0007 | NHL · Penguins @ Avalanche · 16 Oct (US) |
| P-608 | …-G0008 | NBA preseason · Trail Blazers @ Warriors · 16 Oct (US) |
| P-609 | …-G0009 | Bledisloe Cup · Australia v New Zealand · 17 Oct |
| P-610 | …-G0010 | B.PREMIER · Altiri Chiba v Hiroshima Dragonflies · 17 Oct |
| P-611 | …-G0011 | NBL · SE Melbourne Phoenix v Cairns Taipans · 17 Oct |
| P-612 | LOCAL-20261018MELILL01-G0001 | NBL · Melbourne United v Illawarra Hawks · 18 Oct |
| P-613 | …-G0002 | ODI Tri-Series · Pakistan v Sri Lanka · 18 Oct |
| P-614 | …-G0003 | Czech women's 1. liga · ŽBK KP Brno v Žabiny Brno B · 18 Oct |
| P-615 | LOCAL-20261018Q7N4T9B2-G0001 | B.ONE · FE Nagoya v Tryhoop Okayama · 18 Oct |
| P-616 | …-G0002 | PBA · TNT v Converge · 18 Oct |
| P-617 | …-G0003 | LaLiga · Osasuna v Racing Santander · 18 Oct |
| P-618 | …-G0004 | KBO semi-PO G3 · KIA @ LG · 20 Oct |
| P-619 | LOCAL-20261018K9V4R2M7F6-G0001 | J1 · Machida Zelvia v Avispa Fukuoka · 18 Oct |
| P-620 | LOCAL-20261018X7Q4M9R2-G0001 | Test · South Africa v Australia (2nd) · 18 Oct |
| P-621 | …-G0002 | LBA · Napoli v Olimpia Milano · 18 Oct |
| P-622 | …-G0003 | Women's T20I · India v Zimbabwe (2nd) · 18 Oct |

## Applied append and custody

Destination [Part 8](../../../prediction%20logs/PREDICTION_LOG_COMBINED_8.md) (`-text`, LF): pre-import **5,047 bytes**, SHA-256 `9b9484b7ad48c297996e2d55703ef908af7aa147d7ce1842fbda845c3e3f6303` (= committed blob); post-import **851,514 bytes**, SHA-256 `2d799865a2346731e10b2f37f625a7dee1c1c4317f9925e2d42299f73fa379d2`; appended suffix 846,467 bytes, SHA-256 `47c192ed44332d73c2558bf400d401db9b7b94280f44eeedd1af8d83626bbee4`. The pre-mutation recheck (HEAD, destination bytes/hash, planned suffix hash) passed immediately before the append.

Wrapper rule (MINI_LOG_IDENTITY §5): each `canonical-md-1` wrapper holds the **exact card core** — the bytes between the local `BEGIN CARD`/`END CARD` marker lines — after one metadata line (P-ID, local key, native identity, frozen-source and core hashes, offsets). The local markers and any heading outside them (e.g. P-611's `## GAME CARD` line, P-614's preceding heading) stay in the preserved source. This keeps R19 free of cross-ID nesting. Settlement and source-addendum wrappers (`RESEARCH ADDENDUM P-NNN 2026-10-21-settlement-revision-1|2`, `…-source-addendum-1|2`) hold the exact block contents in the same way, with `Original:`/`prior revision` pointers.

Units: 22 cores, 2 source addenda (P-601 research-recovery and analyst-probability-recovery), 26 settlement revisions (79B3 revision-1 ×11 and revision-2 ×4; the other minis revision-1 ×11). Every unit maps to a destination or an explicit retained disposition: [SOURCE_UNIT_DISPOSITIONS.csv](SOURCE_UNIT_DISPOSITIONS.csv). Shared settlement-document text outside per-event blocks (receipts, registers, queues, manifests, S-checks) and the minis' headers, intake tables, queues and footers are retained in the inputs only — they are not cards and are not re-interpreted.

## Effective settlements and scores

Row table: [EFFECTIVE_SETTLEMENT_ROWS.csv](EFFECTIVE_SETTLEMENT_ROWS.csv) (102 contract rows). Grades are conditional sporting grades; operator terms are unverified for every event.

| Cohort | Events | Rows W / L / PUSH / UNRESOLVED | Primary (ranks 1–2) |
|---|---|---|---|
| RESEARCH_ONLY_NO_MODEL, analyst diagnostics NOT_PRIMARY (P-601–P-611) | 11 | 52: **25 / 25 / 0 / 2** (P-604 corners) | none — p_card NOT_ESTIMATED; denominator 0 |
| ANALYST_PRIMARY_V1, uncalibrated (P-612–P-622) | 11 | 50: **25 / 23 / 2 / 0** (P-616 ±2.0 pushes) | 22 slots: **11 W / 10 L / 1 PUSH** — Rank 1 6W/5L; Rank 2 5W/5L/1P |

ANALYST_PRIMARY_V1 primary decisive rows (n=21): mean binary Brier **0.2041** (by hand from the settlement documents; push rows scored separately as categorical half-sum 0.7207). Paired same-row BASELINE_P exists for 8 rows only (P-612 ×4, mean d_Brier +0.0602, baseline better; P-621 ×4, mean −0.0113): mean +0.0245, two events — descriptive, `INSUFFICIENT_EVIDENCE`. The research-only analyst values are not scored as primary probabilities (SCV-v11 §1).

**Timing cohorts (unchanged by import).** No card has a verified pre-start issue or clean-pre-start-input proof. Owner feed timestamps confirm post-start completion for P-610 (tip 16:10:24 v card 16:15:11 AEDT), P-615 (tip 17:40:16 v ≥17:41:02), P-613 (first ball 19:02:47 v card after 19:06), P-618 (first pitch 20:31 v card after) and P-622 (first ball 00:30:39 v card after). P-620's first ball was 21:00:43 AEDT, two hours after schedule; its delivery time is unrecorded, so its issue phase stays UNVERIFIED. P-612–P-618 are owner-supplied `READ_ONLY_DRAFT / NOT_ISSUED` records retained as research; they are reported in their own cohort and never pooled with issued cards.

**Pending/unresolved after import.** No new pending event. P-620's contracts are all terminal (SA first innings ≥324/7 is an invariant bound); only its qualitative Test-winner call awaits the 22 Oct result. Terminal unresolved fields: P-604 corners (2 rows); P-616 operator overtime definition (grade-changing); single-source corner counts for P-603 and P-619 (conflict 1 v 2 for Machida, invariant); operator terms and exact final times for all. Held: LOCAL-20261018MELILL01-G0004. Full queue: [UNRESOLVED_POST_IMPORT.md](UNRESOLVED_POST_IMPORT.md).

## Source-time correction (prompt-3 documents)

The prompt-3 settlement documents imported here were written by the same session and carry "prepared ≈…" and "effective" times that were **estimated, not read from the clock**, and several are later than the real write times. Actual file times (AEDT): X7Q4 00:40:05, K9V4 00:40:55, Q7N4 00:43:08, MELILL01 00:45:00, 79B3 revision-2 00:46:56 (document says ≈01:15), E06 revision-2 00:46:57 (says ≈01:20), empty-mini document 00:47:24 (says ≈01:25). The imported bytes stay literal; use these file times as the true revision times. Revision order and grades are unaffected.

## Research-source register and learning handoff

[RESEARCH_SOURCE_REGISTER](../../../RESEARCH_SOURCE_REGISTER.md) gains one dated, deduplicated section of the new routes observed in these settlements (declared scope: this import). The three package sidecars [SOURCE_DISCOVERY_REGISTER.csv](SOURCE_DISCOVERY_REGISTER.csv) (38 rows), [SOURCE_SEARCH_ATTEMPTS.csv](SOURCE_SEARCH_ATTEMPTS.csv) (11) and [REQUIREMENT_CLOSURE.csv](REQUIREMENT_CLOSURE.csv) (32) are verbatim table cells from the imported settlement documents. Information completion stays **INFORMATION_INCOMPLETE**; import closes no open field.

For prompt 6 (no ingest here): learning records are the "Learning record (LEARN-v2)" tables inside each settlement document, joined through LOCAL_ID_MAPPING.csv. Settled packages and hashes: 79B3 `inputs/2026101679B3FBCC8D/PREDICTION_MINI_SETTLED_…_R1.md` (`6cfea59c…0ee6`) + revision-2 document (`2026101679B3FBCC8D_SETTLEMENT_REVISION_2.md`); MELILL01 `0eb363bf…4c1e`; Q7N4 `b6d2213b…1177`; K9V4 `9636ef07…07a9`; X7Q4 `c16cf7c2…6d83` (all `inputs/<mini>/PREDICTION_MINI_SETTLED.md`). MINI_SETTLEMENT review rows are in each document for prompt 6 to append to `research/learning_status/REVIEW_LOG.csv`; this import did not write the learning store, training candidates or review log.

Verification and tests: [VERIFICATION.md](VERIFICATION.md). Readback ranges: [IMPORT_READBACK.csv](IMPORT_READBACK.csv).
