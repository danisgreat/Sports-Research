# PROMPT 7 — Repair or extend the historical results archive

**Mode:** ARCHIVE_EXPANSION. Markdown/CSV/text only; no scripts/builders in the repository. A helper run outside it is disclosed, with its rules written out in prose (CONTRIBUTING). Inputs: `<league, seasons, fields or documented priority>`. Writes: declared target CSVs, source/provenance/coverage notes, audited profile updates if supported, and a new verification folder. No issued log/card changes and no implicit model promotion.

## 1. Read and scope

Print the [reading receipt](README.md) after common controls, ARCHIVE_USE_GUIDE, archive README/coverage/source implementation notes, relevant SOURCES/profile/base-rate definitions, target schema and existing files, this prompt and latest relevant retrospective. Inventory branch/HEAD/dirty files; preserve originals of repaired data in the report scope.

Choose explicit league/season range and event grain before collection. Prioritise current forecast leagues and required endpoint fields over bulk historic volume. Declare season naming, competition stage, official schedule denominator, timezone, postponement/doubleheader identity, missing columns and exclusion rules. The target can be any sport and league. Pick it from the request, from the leagues in current use (CURRENT_STATE, the active log, the profiles that [LEAGUE_PROFILES](../../LEAGUE_PROFILES.md) marks stale or missing) and from the `Archive check` lines of recent cards that reported a missing or partial file. Before estimating any rate, audit each source column the rate depends on: count populated against blank, and test whether a flag or count is a measurement or a default (see §3).

## 2. Collect with field provenance

Use exact official/registered structured sources and record URL, native IDs, source field, publication/retrieval times, snapshot/as-of date and collector lineage. Write the dataset's `DATA_PROVENANCE.md`: a per-column class (observed, derived, missing, conflicting, independently checked), schema and migration, canonical path, ID scheme, defects and use rules (ARCHIVE_USE_GUIDE §9). A transformation helper, if one is used, runs outside the repository and its rules are written out in prose there (CONTRIBUTING). Record availability evidence separately from the game date: a later correction is known only from its correction time (R28). Preserve existing header/order/types; proposed schema changes need an explicit migration decision rather than ad hoc columns. Keep unrepresentable source fields in a Markdown sidecar until approved.

Do not guess names, start times, regulation scores, overtime, phase counts or missing outcomes. Zero is valid; blank is unknown.

**Default-looking values are a diagnostic, not a verdict (R26).** A column that holds one constant on every row, or a flag that is never set while other fields contradict it, is labelled `SUSPECTED_DEFAULT` (for example ties recorded with no extra period marked). It stays so until the field definition, the source and the season's rules have been checked. Record the outcome as one of:
- `MEASURED` (a legitimate constant or a real all-zero column stays);
- `NOT_APPLICABLE`;
- `UNOBSERVED` (blank);
- `CONFIRMED_PLACEHOLDER`, proven by reading the builder or the source. These values are removed from measurement, and the raw values are kept in the quarantine record.

Keep the raw value and its interpretation in separate places. Never fill an unknown with a default, a mid-season date, a fixed time or attendance, "half of the final score", or a row-number round. Cancelled/suspended games stay classified. Final totals that include shootout/OT must be distinguished from regulation. Postgame narratives remain postgame and cannot populate point-in-time features. Same-team/date is not sufficient deduplication for doubleheaders.

Repairs record old value, new value, official evidence and reason; preserve source copies where allowed in text. A source conflict is quarantined or unresolved, not silently won by the easiest scrape. Preserve raw source values alongside documented normalization.

## 3. Validate actual coverage

Print schema/header/type checks, logical record count, duplicate/native-ID and alias checks, date/season/status/endpoint checks, zero-versus-missing counts and field missingness. CSV can contain quoted commas/newlines: physical line count minus one is valid only after proving no embedded newlines. Use permitted CSV-aware file facilities or documented manual reconciliation, not a false complete count.

Check total=home+away, signed/absolute margin and winner/tie consistency wherever fields are available. Check that date and start time are populated (a row without a date cannot feed form, rest or point-in-time recipes).

**Endpoint-specific reconciliation (R27).** State, per league, era and endpoint, the equation the period fields should satisfy and which fields are measured. For example:
- modern Czech hockey: P1+P2+P3+OT+SO pair = printed final, the deciding shootout goal included;
- 1980s Czech hockey: periods sum to the printed tie, with the shootout tally printed separately;
- soccer half-time: HT ≤ FT per side;
- extra innings, extra time and golden point: listed explicitly.

A row that breaks its equation is flagged and kept as printed. **Never invent a balancing value.** Mark it usable for final-score work and unusable for period work. Classify shortened, cancelled, suspended, replayed, awarded and forfeited games, and the stage scope, before comparing with the official schedule denominator. Check that the stage field matches the competition's own stage vocabulary (post-season, cup, play-in or friendly games must not be typed as regular season). Reconcile a reproduced profile to the existing row first, so that a method difference is not mistaken for a data change. Validate the full changed set where feasible; otherwise state total versus actually checked and avoid a full-validation claim. Independently check a predeclared spread across early/middle/late season, zeros, ties, OT/extras and doubleheaders; at least ten or all if fewer. List exact sampled IDs and source agreement/disagreement.

Reconcile event count to the official season schedule including postponed/cancelled/replayed games and exact stage scope. A header-only or partially collected file is not complete. Plausibility/profile differences are findings to investigate, not reasons to force scores toward an expected average.

## 4. Profile and availability

Update coverage/source notes with actual rows/fields, gaps, dates, sources and checks. Recompute a profile only from a defined vetted population with adequate coverage, explicit seasons/stage/endpoint, n, missingness, means/SD/covariance and arithmetic. Compare old/new windows before pooling; avoid double-counting current games or league-rule transitions. Archive the prior row and state effective date. If data is inadequate, mark DATA_PENDING and keep the stale prior explicitly labelled; never add a retrospective residual as a universal offset.

Whole-season historical data are not automatically known before every game. Record availability limitations and exclude post-cutoff fields when used for replay/forecast. A refreshed profile is a data update, not demonstrated predictive improvement. It needs its own prospective paired comparison against the retained prior, registered in HYPOTHESIS_REGISTER (use the existing profile entry for that league if there is one, otherwise add a dated entry). Write the same audit for every league you touch: coverage, defects found, windows compared, decision and what stayed unrepaired.

## 5. Verify, publish and report

Read back changed CSVs and notes, reconcile rows added/repaired/unchanged, review diff and exact write scope. Commit only intended data/source/coverage/profile/report paths; do not add large local canonical exports or unrelated files. Push without force when invoked, fetch and verify remote SHA/artifact.

Return target/grain/season scope, official versus collected counts, field coverage, source lineage limits, complete versus sampled checks, unresolved conflicts, profile readiness, file links and publication status. Stop dependent computations when their data fails checks while retaining completed independent work.
