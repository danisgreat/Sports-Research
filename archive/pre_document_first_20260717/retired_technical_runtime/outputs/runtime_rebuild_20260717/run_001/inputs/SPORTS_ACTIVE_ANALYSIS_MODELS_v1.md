# Active analysis-only sports models

Effective: 2026-07-17 (Australia/Sydney)

Capability status: **ACTIVE_ANALYSIS_ONLY — FIVE LIVE-STATE MODELS**

Quantitative operational status: **SUSPENDED — NO ACTIVE NUMERIC FORECAST MODELS**

Owner: Sports research governance

## 1. Permission boundary

`ACTIVE_ANALYSIS_ONLY` authorizes a deterministic qualitative live lean from a fresh, hashed, registered official-source snapshot. It does not authorize a probability, confidence percentage, fair price, betting edge, expected value, stake, profitability claim, calibration claim or prediction-ledger entry.

This tier is deliberately separate from `ACTIVE` in `SPORTS_MODEL_COVERAGE_REGISTRY_v3.csv`. Numeric `ACTIVE` still requires the full activation contract, including fitted artifacts, a preregistered untouched test and a later prospective shadow. The analysis tier must never be cited as satisfying those requirements.

The machine registry is `SPORTS_ANALYSIS_MODEL_REGISTRY_v1.json`. Requests and outputs are closed by `schema/analysis_request.schema.json` and `schema/analysis_output.schema.json`. Runtime code is `src/analysis.mjs`.

The separate matrix `schema/analysis_acceptance_traceability_v1.csv` contains 16 analysis-tier requirements, all backed by executable tests. It does not alter or waive the incomplete quantitative acceptance matrix.

## 2. Active scopes

| Sport | Model | Exact usable scope | State inputs | Important exclusions |
| --- | --- | --- | --- | --- |
| Baseball | `ANALYSIS_BASEBALL_LIVE_STATE_V1` | MLB, NPB or KBO live winner lean | score, inning/half, outs, occupied bases | no pitchers, lineup quality, park, weather, team rating or probability |
| Cricket | `ANALYSIS_CRICKET_CHASE_STATE_V1` | ODI/T20I/T20/WT20I/MLC second-innings standard-target live chase | target, score, wickets, legal balls, first-innings rate | no Test cricket, first innings, DLS/revised targets, player quality or probability |
| Soccer | `ANALYSIS_SOCCER_LIVE_SCORE_V1` | FIFA, EPL, Bundesliga, UEFA Champions League or A-League Men live winner lean | score, elapsed time, regulation time, red cards | no xG, lineup, competition-strength, extra-time contract or probability |
| AFL | `ANALYSIS_AFL_LIVE_MARGIN_V1` | AFL live winner lean | points, quarter, nominal time remaining | no AFLW, time-on model, venue/team/player strength or probability |
| NRL | `ANALYSIS_NRL_LIVE_MARGIN_V1` | NRL live winner lean | points and elapsed regulation time | no NRLW, field position, possession, sin bins, team/player strength or probability |

Unsupported competitions or states fail closed. A model does not inherit a new competition merely because its scoring system looks similar.

## 3. Deterministic rules

The rules are intentionally modest and inspectable:

- Baseball scales the observed run margin by innings progress, with a small late-bottom-inning base-occupancy adjustment.
- Limited-overs cricket compares the required scoring rate with the observed first-innings rate and adjusts for wickets remaining relative to balls remaining.
- Soccer scales the current goal margin by elapsed time and uses red-card imbalance only as a bounded player-count adjustment.
- AFL and NRL compare the current margin with a declining sport-specific live-variance threshold as time expires.
- A tied or near-balanced state returns `TOSSUP`; the runtime does not force a side.

Outputs use only `TOSSUP` or a named side with `SLIGHT`, `MODERATE` or `STRONG` qualitative strength. These labels are ordinal descriptions of the rule result, not calibrated probability bands.

## 4. Source and integrity requirements

Every run requires at least one source observation that:

1. names a source approved for that exact analysis model;
2. matches the registered official publisher host;
3. records observed, fetched and analysis timestamps in strict UTC order;
4. is no older than the model-specific 120–300 second freshness limit;
5. includes a SHA-256 hash of the retained source snapshot; and
6. contains no duplicate source ID.

Stale, unofficial, wrong-host, unregistered, conflicting or unhashed inputs fail closed. Dynamic public match centres are evidence sources, not licensed bulk training feeds.

## 5. Use

Fill a sport-specific template, retaining the exact official source snapshot used to populate it, then run:

```powershell
node scripts/sportsctl.mjs analyse-live --input templates/live_analysis_cricket.template.json --output runtime/latest_analysis.json
```

The shipped templates contain sentinels and are not valid evidence until every value and hash is replaced. The CLI prints and optionally writes a deterministic, hashed analysis output.

## 6. Road to numeric models

The research audit recommends separate pregame candidates rather than promoting these heuristics:

- baseball: an MLB dynamic Bradley–Terry regular-season winner model;
- cricket: a format-specific men’s ODI dynamic Bradley–Terry pregame model and a separately fitted live ODI model;
- soccer: a competition-specific Dixon–Coles score model;
- AFL and NRL: separate dynamic Davidson win/draw/loss models.

Those candidates remain development or future shadow work. Historical backtests can diagnose them but cannot be relabeled as a preregistered untouched test. Numeric activation therefore remains blocked until future disjoint test and shadow cohorts genuinely exist.
