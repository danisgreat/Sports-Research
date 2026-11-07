# October 1 canonical logging repair and requested baseball research

Completed October 1, 2026. This report records the repair and verification; it is not a retrospective or settlement of the new game cards.

## Canonical entries and next ID

| Canonical ID | Event | Treatment |
|---|---|---|
| P-523 | Oriente Petrolero vs The Strongest | Retained original mini card, with dated import notes; historical source timing is preserved. |
| P-524 | KT Wiz @ Kia Tigers | Retained original mini card, including its uncalibrated numerical assessment; dated correction distinguishes the official eleven-inning regular-season rule from the original twelve-inning language. |
| P-525 | Chunichi Dragons @ Hiroshima Toyo Carp, game 25 | Retained the pasted intake literally, including its original NO_FORECAST state, and added a separately dated live qualitative assessment. Original research is not backdated or silently replaced. |
| P-526 | Hanwha Eagles @ Samsung Lions, native KBO event 20261001HHSS0 | Completed sports-only, market-blind live qualitative analysis and four ranked propositions. |

All four are in [Part 6](../../../prediction%20logs/PREDICTION_LOG_COMBINED_6.md). The common ledger allocator and [current status register](../../../GAME_LOG_STATUS_CURRENT.md) both report **P-527 next**. The four canonical research entries are separate from certified prospective ISSUE records; that distinction does not prevent analysis or running-log storage.

The retained cards were committed at approximately **10:35 UTC / 20:35 AEST**. Exact per-card records, input paths and commitment hashes are in [COMMIT_RECEIPTS.json](COMMIT_RECEIPTS.json). The former mini log now directs readers to the canonical log. Its entire retirement-time original is preserved in [originals/mini_at_retirement.md](originals/mini_at_retirement.md), SHA-256 `cb49d28a6c30216f3ec078ff676ed1ab5bb9cb6b3f0cdff10d1e8a360aab5c01`.

## Durable workflow repair

`research.operations.log_card` retains original source bytes, allocates under the existing common ledger lock, journals preparation, appends the complete canonical card, verifies the resulting bytes, and journals commitment. Recovery handles a prepared transaction and an interrupted exact-prefix append; unrelated changes cause refusal rather than an unsafe overwrite. Exact repeat imports return the existing ID. Changed content requires a dated addendum. The workflow updates the current queue automatically after commitment, recovery and duplicate readback.

Current rules, templates and prompts now permit requested research for every sport without requiring a registered model, calibrated probabilities, an approved baseline, a fixed fixture universe, an independence quorum or an early pregame cutoff. Late/live research records its real observation and logging times. Qualitative ranks and transparent, reproducible uncalibrated scenarios are permitted. Missing values and uncertain availability remain explicit. Existing performance-certification requirements remain separate and are not presented as analysis blockers.

CI uses the current control-selection verifier and includes the logging tests. Synthetic issuer fixtures now use the original Part 6 source block rather than treating later production cards as their test starting state. Current research queue IDs are displayed in bold so the preserved historical legacy reader continues to read its original historical rows; current ledger readers still include the new research cards. Repeated status refreshes preserve the original status bytes and generate one current queue and one administrative-history heading.

The four cards retain issuance receipt **CONTROL_MANIFEST_2026-10-01-3.md** and its hash. Subsequent integration corrections are recorded by immutable receipts 4 and 5. The current selected control is **CONTROL_MANIFEST_2026-10-01-5.md**, method MDS-2026.10.01-v7.1 / control CR-2026.10.01-I2. Earlier receipts and committed card cores were not rewritten to claim issuance under a later receipt.

## Hanwha–Samsung assessment

The official scheduled start is **18:30 KST / 19:30 AEST**, rather than the supplied 19:00 AEST. Actual first-pitch time was not verified. The final owner observation retained before logging was **2026-10-01T10:31:20.441891+00:00 / 20:31 AEST**: Hanwha 0–0 Samsung, top third, zero outs, first-base occupancy marker; Won pitching and Jung Eun-won batting. Two completed innings were scoreless. This is a conditional live assessment at its real research time, not a pregame issuance or a claim about later unobserved play.

1. **Combined Under 11.5 runs.** Modest preferred total: the threshold exceeds the retained league scoring mean; Hanwha's shorter recent scoring windows are weak; posted orders omit usual contributors; two innings were scoreless. Hwang's walks, a short start, Won's contact risk and later bullpen innings are credible failure routes.
2. **Samsung Lions -0.5.** Preferred side and potential winner: stronger season run prevention, Won's better command, home record and recent form. Won's latest nine-earned-run outing materially limits conviction.
3. **Hanwha Eagles +2.5.** The two-run cushion and retained power provide a route despite Samsung's side advantage. Hwang's command/short-outing risk and Hanwha's recent heavier defeats expose a three-run-loss branch.
4. **Combined Over 11.5 runs.** The less likely requested total, with an explicit opposing run-cluster route. It cannot succeed with the Under on a complete integer final score.

**Potential winner: Samsung.** Ranks 1 and 2 are close. No calibrated probability or baseline is estimated. Samsung winning and Samsung -0.5 are the same sporting proposition. Hanwha +2.5 and Samsung -0.5 can both succeed on a one- or two-run Samsung win; they are not independent picks. A sporting tie fails Samsung -0.5 and satisfies Hanwha +2.5. Operator-specific void and shortened-game definitions were not supplied and are not invented.

The [full analysis](KBO_HANWHA_SAMSUNG_ANALYSIS.md) contains the posted batting orders, both starters' season and recent records, named two-day bullpen workloads, recent team windows, season and head-to-head context, weather interpretation, rules, uncertainties and failure routes. The [source receipts](SOURCE_RECEIPTS.md) retain exact native request parameters, retrieval timestamps, body paths and hashes. Three retrieved Google Drive reference texts are preserved locally; no Drive writes were made. No bookmaker odds, fantasy or tipster material was used in the assessment.

## Verification

- Full tests: `py -3.14 -X utf8 -B -m pytest -p no:cacheprovider research\tests research\operations\test_log_card.py -q` — **115 passed in 65.87 seconds**. This includes seven focused logging tests and the synthetic-production-tail regression test.
- Current control verification: `py -3.14 -X utf8 -B -m research.operations.control_freeze --verify` — **326 files, zero mismatches**.
- [FINAL_CHECKS.json](FINAL_CHECKS.json), observed at **10:48:17 UTC**, reports `valid: true`, with no issues: four canonical cards, eight hash-chained ledger records, zero pending transactions, P-527 next, exact readback, and one current status queue.
- Parts 1–5, the pre-repair Part 6 bytes, and its original **141,740-byte** source block are preserved. The original block SHA-256 is `c4d497bf339010eae2ff5df23a2d76290983585671666e74791618342565cf30`. The checks verified 89 original snapshots, 17 frozen research files, and all four frozen model builds.
- All **65 source bodies retained for this research** pass their hash checks. The separate repository-wide receipt check verifies **73 bodies**; these are different check scopes and are not summed as unique sources. Refreshed posted lineup names match the initial official response.
- Scoped policy, code, CI and test changes pass `git diff --check`. Literal imported Markdown retains original hard-break whitespace, so the Part 6 copy can produce formatting-only trailing-whitespace warnings; original card source text was not rewritten to remove these.

These checks establish storage, source-body integrity and workflow mechanics. They do not establish future predictive skill or calibrated probabilities. No new current-game retrospective, grade or settlement was added. No Git commit/push or Google Drive publication was performed.
