# Rebuilding a trustworthy results store

**Proposal, 16 October 2026. Not executed.** A different file format alone will not fix unsupported or fabricated observations. Rebuild from opened online sources, one competition/season at a time, with explicit identities, provenance and acceptance checks. Old counts/profiles are not a certified starting dataset.

| Previous design observed in current controls | Proposed design |
|---|---|
| Deep sport/competition/year trees with empty/header-only placeholders | Create exports only after collecting actual rows; coverage register distinguishes not collected, partial and complete |
| Copied aliases and special-event subsets | One canonical event identity; aliases/parent links and views rather than duplicated games |
| Broad CSVs mixing results, periods, players and prose | Separate event/result/period/lineup/source/correction tables joined by stable IDs |
| Default-looking times, zero attendance, incomplete periods and stale profiles | Unknown stays null/blank with reason; derivations name observed inputs; reject unsupported defaults and arithmetic inconsistencies |
| Event date mistaken for data availability | Separate scheduled/actual event, publication, first observed, retrieval and correction times |
| File existence treated as readiness | Field-specific admission, exact checked IDs, fixture-denominator checks and immutable input releases |

## Storage recommendation

Within current repository rules, keep Git for schemas, source register, transformation specifications, coverage/quality reports, manifests and small market-free normalized CSV exports. Store raw HTML/PDF/API captures outside Git with URL, retrieval time, SHA-256 and access/use notes. Do not commit binary databases, JSON dumps or caches.

A separately approved external SQLite store would suit canonical IDs, relational constraints, transactions and revisions. For larger analytical snapshots, Parquet queried with DuckDB is an alternative. Both need a separately scoped implementation/storage location under current rules; neither is created here. See [SQLite application format](https://www.sqlite.org/appfileformat.html), [DuckDB Parquet](https://duckdb.org/docs/current/data/parquet/overview) and [W3C provenance primer](https://www.w3.org/TR/prov-primer/). These support design concepts, not sports-result truth.

## Minimal records

- Competitions: canonical ID, sport/format/gender/age, organizer, era/season naming, endpoint rules and aliases.
- Events: canonical/native IDs and source namespace, competition/season/stage, participants, home/away/neutral, scheduled/actual start/timezone, status, reschedule/doubleheader identity.
- Results and periods/innings: event ID, exact segment/endpoint, observed values, status, source-observation ID and effective revision. Final scores never create missing periods.
- Players and lineup observations: stable names/IDs/aliases, event/team, selected starter/bench/reserve/inactive role, confirmation status and publication/known-at. Historical participation remains separate.
- Source observations: URL/provider/native ID, exact field/raw value, OBSERVED/DERIVED/MISSING/CONFLICTING class, publication/available/retrieved times, capture path/hash and collector lineage.
- Corrections: parent revision, replaced fields, reason, evidence and effective time; original observations remain recoverable.
- Releases/coverage: expected/collected/eligible/excluded counts, per-field missingness, checked sample/all IDs, conflicts, source/data/schema/code hashes, acceptance status and unresolved limits.

## Incremental rebuild sequence

1. Pilot one completed season with accessible official results and a checkable fixture denominator. Define scope, sources and endpoint before collection. Do not generate decades of folders.
2. Capture permitted source bodies externally, normalize observed fields and record provenance. Compare independent sources when identity/coverage/conflicts warrant it; state unknown independence.
3. Validate IDs/aliases, schedules/final states, home/away, score/period equations, timezones, hashes and blank versus zero. Reconcile every fixture disposition, including cancelled/awarded/abandoned events.
4. Inspect early/middle/late records and every detected exception against original sources. Publish exact checked IDs and unchecked remainder; a sample is not full verification. Resolve or quarantine conflicts by field.
5. Freeze a versioned release with actual coverage, source snapshots and checksums. Derive profiles only from admitted rows; model development reads that immutable snapshot with known-at limits.
6. Demonstrate idempotent re-import, append-only correction revisions, duplicate/malformed-input rejection and backup restoration to matching hashes. Then expand one competition/season at a time.

Completion applies only to the declared verified scope. Current games continue online independently. Tests/checksums alone never promote a new store or establish predictive skill.
