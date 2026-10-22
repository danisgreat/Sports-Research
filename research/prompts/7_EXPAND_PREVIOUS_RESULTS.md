# PROMPT 7 — Build reviewed online history in a declared scope

**Local keys until settlement; updated mini after every game (MINI-v2).** Defined in [MINI_LOG_IDENTITY_PROTOCOL](../../MINI_LOG_IDENTITY_PROTOCOL.md); summarised in [CORE](../../CORE.md) §2.

**Persistent research and corroboration (EXH-v1).** Defined in [RESEARCH_EXHAUSTIVENESS_PROTOCOL](../../RESEARCH_EXHAUSTIVENESS_PROTOCOL.md); summarised in [CORE](../../CORE.md) §5.

**P-2026.10.22-v24.0 · PROCEDURE · LOCAL_WORKING_TREE.** Read COMMON_OPERATING_PROTOCOL, CURRENT_RULES, REFERENCE_MODEL_PROTOCOL, COMPETITION_PARAMETERS, EFFECT_TABLES, HISTORICAL_SOURCE_PROTOCOL, ROSTER_AVAILABILITY_PROTOCOL, RESULTS_REBUILD_PLAN, SOURCES and actual target schemas. Writes: explicitly named market-free CSV/provenance/coverage/profile paths and a new verification folder. Raw captures/helpers stay externally; code stays under ml/. Original cards/logs/reports remain immutable.

**ML/RL scope (MLSCOPE-v3).** Defined in [FORECAST_CYCLE_PROTOCOL](../../FORECAST_CYCLE_PROTOCOL.md); summarised in [CORE](../../CORE.md) §7.

**Execution environment (ENV-v2).** Defined in [EXECUTION_ENVIRONMENT_PROTOCOL](../../EXECUTION_ENVIRONMENT_PROTOCOL.md); summarised in [CORE](../../CORE.md) §1.

## 1. Declare the target

Resolve sport/competition/season/era, event grain/endpoint, stable IDs/aliases, timezone, known-at/corrections, online source plan, official fixture denominator and exact output paths. The old results store is retired. Do not restore it from Git, recreate its directory tree by default or generate placeholder seasons. A rebuild needs explicit scope/destination, separate from game research. Preserve affected operating originals.

## 2. Collect observed online fields

Apply HISTORICAL_SOURCE_PROTOCOL to actual organizer/federation/league scorecards and both teams' dated results. Escalate to permitted providers and original-language sources; compare where needed. Game-sized work seeks both sides' L5/L10/L15/L20 with true n; season work reconciles its declared fixture population. Record URL, event/field/value, publication/available/retrieved times, capture hash and lineage. Seek exact-game confirmed players/roles/replacements under ROSTER_AVAILABILITY_PROTOCOL where in scope. Historical participation is not pregame publication proof.

## 3. Normalize, validate and admit

Use canonical event IDs and alias mappings; separate events/results/periods/lineups/source observations/corrections as needed. Classify OBSERVED/DERIVED/MISSING/CONFLICTING. No guessed times, fabricated periods, zero defaults or balancing scores. Check IDs, duplicates/reschedules/doubleheaders, season naming, types, final status, score equations, endpoints and official fixture completeness. Verify all changed rows where feasible; otherwise list exact checked IDs, sample method and unchecked remainder. Preserve conflicting evidence and field-specific use restrictions.

Separate event date and source availability/correction time. Date-only labels do not establish point-in-time features. Publish actual expected/collected/eligible/excluded counts, missingness and conflicts. New profiles need an independently verified population; retired profiles/models are never promoted implicitly. Game research may already use its own fresh reviewed inputs without waiting for this work.

## 4. Read back and publish exact scope

Verify every changed file/row/source map, preserved originals and relevant negative/valid cases. Inspect staged scope and publish only with task authorization. No raw captures/caches or unrelated edits. Fetch and compare remote commit/artifacts. Return actual coverage, admitted fields, true n, unresolved gaps, known-at limits and publication status. A plan or passing test is not a completed/certified rebuild.

## Data for the reference lane (REV-07 / REV-17, v24.0)

Prompt 7 builds what the reference lane runs on, in this order of value: (1) verified finals for the competitions the owner requests most, through a two-lineage backfill (`python -m ml backfill-basketball` for basketball; the same pattern with the competition's field owner and an independent second collector for other sports), then `python -m ml release-gate --competition C` must pass; (2) line-up and availability snapshots with publication times at every freeze (they are the only route to availability effects: EFFECT_TABLES §4); (3) a rebuilt `research/competition_parameters/COMPETITION_PARAMETERS.csv` after each season; (4) re-estimated rows for `research/effect_tables/EFFECT_TABLES.csv` (append, never overwrite) with their out-of-sample test; (5) the structured sources the checklists name (MoneyPuck, Understat, Cricsheet, nflverse, Squiggle, ClubElo). Raw bodies stay outside the repository with hashes in the receipts; a newly captured historical fact is known now, never on its game date. Record the competition's tier before and after.

## Persistent sourcing and information closure (EXH-v1)

Consult and freshly check shared/prior source observations, then pursue missing fields across owner, structured and local-language routes with independent corroboration. Record all actual discoveries and partial/failed attempts using the source-register templates; map every declared collection requirement and exception. Append dated shared route observations only in authorized scope. A source list, header-only export, single collector or exhausted attempt does not establish complete data.

**Connected cycle handoff (CYCLE-v1).** Defined in [FORECAST_CYCLE_PROTOCOL](../../FORECAST_CYCLE_PROTOCOL.md); summarised in [CORE](../../CORE.md) §7.
