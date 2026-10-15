# Historical source recovery across every sport and competition

**HIST-2026.10.15-v1 · MDS-2026.10.15-v15.2 · CR-2026.10.15-R6 · P-2026.10.15-v15.0.** Owner instruction: when Previous Sports Results does not contain the needed history, is incomplete or is incorrect, **verified internet research is the preferred first recovery option**. This applies to every sport, league, tournament, cup, season, regional/lower division, women's/youth competition and obscure event. Healthy reviewed archive rows remain reusable. This is a source/research procedure, not a fitted-model or performance qualification.

## 1. Choose the source path before giving up on a field

1. Inspect the exact local competition/season/endpoint files and provenance briefly. Record actual row/field/date coverage, last usable result, known defects and aliases. Do not assume that an old header-only/coverage note is current. A populated file can still be incomplete or wrong.
2. For **any needed gap, stale window, suspicious default, missing endpoint or disagreement**, make online source discovery/research the first recovery action. Do not first borrow another league's history, estimate missing scores, wait for a bulk archive rebuild or issue a data-missing forecast without this attempt. Search enough prior events for both sides' L5/L10/L15/L20 plus needed season/league model history; a team form page alone does not establish a league training population.
3. Start with the actual competition/organizer/federation's results, original game sheets/scorecards and both teams' dated schedules/results. Then permitted structured sporting providers and trustworthy local historical sources. Use [SOURCES](SOURCES.md) as a starting map, not an exhaustive league allowlist. Public sporting routes discovered during research may be used with the same access, evidence and provenance rules; lack of a pre-registered familiar provider is not evidence of no data.
4. For obscure coverage, search original-language competition/team names, former names/transliterations, season/stage/date and native game IDs. Try organizer/federation sites, team archives, official PDFs and local match reports. Search result snippets/AI summaries locate evidence; open the underlying source to establish a value. Record concrete queries/routes, read times, failures and conflicts. Related mirrors sharing a collector are not independent confirmation.
5. Verify the exact event and field before merging. Prefer the responsible field owner for a contested sporting result, with compatible event identity/period/final state/era. Preserve both versions and an explicit resolving reason. A mutable page, latest timestamp, repeated secondary claim or unexplained mismatch is not automatic correction evidence. An unresolved field stays excluded/missing; do not average conflicting scores.
6. Only after actual applicable searches may a gap remain HISTORICAL_DATA_UNAVAILABLE / INCOMPLETE / CONFLICTING. State side/field, true usable n, routes attempted, impact and next action. A documented genuine gap is acceptable; an unperformed search is not completion. No guarantee every obscure competition publishes complete history.

## 2. Sport-specific evidence to look for

| Sport / family | Exact historical evidence and distinctions |
|---|---|
| Basketball | League/federation/team season results and box scores; regulation/OT, period format, local duration, selected competition and stage |
| Soccer | Competition/federation/club fixtures and match reports; regulation versus extra time/penalties, abandoned/awarded games, half/corner fields only from their owners |
| Cricket | Board/organizer scorecards; format, batting/bowling role, innings runs/wickets/legal balls, all-out versus shortened/declaration/chase, toss and method where relevant |
| Baseball | League/team scorebooks; native ID and doubleheader game number, home/away, innings/regulation/extras and tie/action rules |
| Ice hockey | League/federation game sheets; regulation periods, OT/shootout and official final-score convention, abandoned/awarded status |
| Tennis | Tour/federation/tournament draw and completed score records; player identity, surface, best-of, deciding-set/tiebreak, retirements/walkovers. Research still applies although primary adapter remains unsupported |
| Australian rules | National/state/local organizer and club scorecards; goals/behinds/points, competition-specific length, season/stage and draws/finals |
| Rugby league | Actual league/federation/club results; local scoring, regulation/golden-point/finals endpoint. Do not substitute union results |
| Rugby union | Actual union/competition/club results and match sheets; local scoring, draws/finals/extra time. Do not substitute league results |
| American / college / Canadian football | League, conference, institution/team gamebooks; local scoring/period/OT/tie rules, regulation and final fields, season/stage |
| Field hockey / other sports | Exact federation/organizer/team historical records and local format; distinguish shootout from match score. Research eligibility is independent of primary-adapter support |

The same discovery steps apply within each family to major and minor competitions. A generic sport's rules, a nearby league's stats or an unrelated gender/age/format are not local evidence.

## 3. Provenance, correction and time

For each accepted event/field retain source URL, native/canonical identity and aliases, exact source value, publication/update/known-at time when evidenced, retrieval time, capture path/SHA256, endpoint/final-state definition and collector lineage (UNKNOWN when unknown). Raw bodies/helpers stay outside the repository. Preserve only permitted sporting extracts/normalized CSV in the named mini/model evidence scope. Record a reconciliation ledger with local row/field/value, web row/field/value, defect, resolving evidence, disposition and destination; do not edit an issued original or erase disputed evidence.

Use one row per stable event, reconcile reschedules/doubleheaders/aliases and deduplicate archive/web overlap. Admit compatible verified fields; quarantine unreliable fields/rows. Classify observed/derived/missing/conflicting values. No fabricated dates, period scores, OT flags or healthy-player assumptions. Market/odds/tips/fantasy fields never enter normalized model inputs; raw captures stay separate.

**Event date, source availability and retrieval are different.** A score searched today may train a future forecast if genuinely known by its horizon; it is not automatically available to an earlier historical refit. If original publication cannot be shown, use the first defensible observed/capture availability time, not a guessed historic timestamp. This can reduce warm-start coverage without preventing an honest current fit. A later-retrieved pre-start version needs independently recoverable publication evidence. Do not use target live/final outcomes, later corrections or future season aggregates to fill pre-start features. Existing same-day runtime conservatism, horizon and warm known-at checks remain.

## 4. Use the recovered data now; archive maintenance is separate

A game-card task may collect/reconcile source-reviewed normalized HISTORY.csv and evidence inside its named mini/primary bundle scope, and use it in the actual primary fit and form tables **without waiting for permanent archive repair**. Do not silently update shared Previous Sports Results, profile/base-rate rows or source registers during a read-only game-card task. Queue the exact scoped repair for prompt7, preserving original rows and provenance. Prompt7 may repair explicitly declared archive paths under its own authorized checks/publication.

HISTORY.csv uses the [primary input contract](PRIMARY_PREDICTION_PROTOCOL.md). Optional `source_kind` is ARCHIVE_REVIEWED, WEB_RECOVERED or WEB_CORRECTED; explicit source routing requires it on every row. The tags describe reviewed provenance, not automatic truth certification. A mixed dataset has separate source coverage and true form n; no double counting or silently imported bad local rows.

When archive discovery/configuration itself is missing or defective, provide a reviewed exact competition metadata CSV via:

```text
python -m ml primary predict --request REQUEST.csv --history HISTORY.csv --contracts CONTRACTS.csv --competition-source COMPETITION_SOURCE.csv --out research/primary_predictions/EVENT
```

COMPETITION_SOURCE.csv has exactly one row and columns `sport,competition,endpoint,tie_rule,extra_fraction,winner_bonus,overs_cap,source_url,available_at,review_status,evidence_path,evidence_sha256,archive_disposition,reason`. Sport is an implemented SPORT_RULES name; `sport/competition` must equal the request, with no major-league substitution. `review_status=RESEARCH_INPUT_REVIEWED`, actual archive_disposition MISSING/INCOMPLETE/INCORRECT, specific reason, HTTPS sporting source and matching evidence capture known by the horizon. Engine is chosen by the existing implementation; endpoint/tie/bonus/innings format must be supported and locally verified. Explicit extra_fraction is a reviewed format parameter for the existing approximation, not a fitted or default major-league constant. Non-cricket overs_cap is blank. No arbitrary extra/market columns.

This route does not promote old DATA_HOLD artifacts or remove their defects. It creates a fresh exact-scope configuration from reviewed sporting evidence; every historical row still needs source/time/score admission. MODEL_CONFIG and the full COMPETITION_SOURCE snapshot/hash are frozen and compared at readback. Receipt reports reviewed-source versus archive configuration and web/archive/unspecified row counts. Ordinary archive routing and its DATA_HOLD failures remain unchanged when no explicit source configuration is provided. Unsupported sports/period/player/format models remain NOT_IMPLEMENTED/NO_FORECAST even when historical facts can be researched online.

## 5. Verification and reporting

Before numeric issuance, verify archive triage, actual online searches for every material gap, field-level reconciliation, source coverage and all normalized rows used; preserve unsupported and unresolved dispositions. Report which values came from local versus web sources, corrected/excluded rows and original copies, usable dates/true n, baseline/model coverage, actual fit/receipts and known-at limits. An internet search, source tag, receipt or green test is not predictive qualification. [Implementation receipt](research/verification/framework_change_2026-10-15-5/IMPLEMENTATION.md).
