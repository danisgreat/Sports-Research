# PROMPT 7 — Repair or extend the historical results archive

**Mode:** ARCHIVE_EXPANSION. Markdown/CSV/text only; no scripts/builders. Inputs: `<league, seasons, fields or documented priority>`. Writes: declared target CSVs, source/provenance/coverage notes, audited profile updates if supported, and a new verification folder. No issued log/card changes and no implicit model promotion.

## 1. Read and scope

Print the [reading receipt](README.md) after common controls, ARCHIVE_USE_GUIDE, archive README/coverage/source implementation notes, relevant SOURCES/profile/base-rate definitions, target schema and existing files, this prompt and latest relevant retrospective. Inventory branch/HEAD/dirty files; preserve originals of repaired data in the report scope.

Choose explicit league/season range and event grain before collection. Prioritise current forecast leagues and required endpoint fields over bulk historic volume. Declare season naming, competition stage, official schedule denominator, timezone, postponement/doubleheader identity, missing columns and exclusion rules. For RET-01 inspect NBL 2025-26 and 2026-27 regular-season coverage; for KBO extras audit missing flags versus genuine zeros before estimating rates.

## 2. Collect with field provenance

Use exact official/registered structured sources and record URL, native IDs, source field, publication/retrieval times, snapshot/as-of date and collector lineage. Preserve existing header/order/types; proposed schema changes need an explicit migration decision rather than ad hoc columns. Keep unrepresentable source fields in a Markdown sidecar until approved.

Do not guess names, start times, regulation scores, overtime, phase counts or missing outcomes. Zero is valid; blank is unknown. Cancelled/suspended games stay classified. Final totals that include shootout/OT must be distinguished from regulation. Postgame narratives remain postgame and cannot populate point-in-time features. Same-team/date is not sufficient deduplication for doubleheaders.

Repairs record old value, new value, official evidence and reason; preserve source copies where allowed in text. A source conflict is quarantined or unresolved, not silently won by the easiest scrape. Preserve raw source values alongside documented normalization.

## 3. Validate actual coverage

Print schema/header/type checks, logical record count, duplicate/native-ID and alias checks, date/season/status/endpoint checks, zero-versus-missing counts and field missingness. CSV can contain quoted commas/newlines: physical line count minus one is valid only after proving no embedded newlines. Use permitted CSV-aware file facilities or documented manual reconciliation, not a false complete count.

Check total=home+away, signed/absolute margin and winner/tie consistency wherever fields are available. Validate the full changed set where feasible; otherwise state total versus actually checked and avoid a full-validation claim. Independently check a predeclared spread across early/middle/late season, zeros, ties, OT/extras and doubleheaders; at least ten or all if fewer. List exact sampled IDs and source agreement/disagreement.

Reconcile event count to the official season schedule including postponed/cancelled/replayed games and exact stage scope. A header-only or partially collected file is not complete. Plausibility/profile differences are findings to investigate, not reasons to force scores toward an expected average.

## 4. Profile and availability

Update coverage/source notes with actual rows/fields, gaps, dates, sources and checks. Recompute a profile only from a defined vetted population with adequate coverage, explicit seasons/stage/endpoint, n, missingness, means/SD/covariance and arithmetic. Compare old/new windows before pooling; avoid double-counting current games or league-rule transitions. Archive the prior row and state effective date. If data is inadequate, mark DATA_PENDING and keep the stale prior explicitly labelled; never add a retrospective residual as a universal offset.

Whole-season historical data are not automatically known before every game. Record availability limitations and exclude post-cutoff fields when used for replay/forecast. A refreshed profile is a data update, not demonstrated predictive improvement; RET-01 requires separate prospective paired evaluation.

## 5. Verify, publish and report

Read back changed CSVs and notes, reconcile rows added/repaired/unchanged, review diff and exact write scope. Commit only intended data/source/coverage/profile/report paths; do not add large local canonical exports or unrelated files. Push without force when invoked, fetch and verify remote SHA/artifact.

Return target/grain/season scope, official versus collected counts, field coverage, source lineage limits, complete versus sampled checks, unresolved conflicts, profile readiness, file links and publication status. Stop dependent computations when their data fails checks while retaining completed independent work.
