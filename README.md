# Sports Research

A disciplined, **market-blind** framework for researching sports events, issuing probability forecasts before the start, and settling them against the official record. It covers MLB, NPB/KBO, basketball (NBA, WNBA, NBL and more), the NHL, soccer, tennis, cricket, AFL, NRL, rugby union and the NFL. Everything is recorded in Markdown: every forecast, the evidence behind it, its settlement and every lesson learned.

> **Status.** Method **MDS-2026.09.19-v4.3** · control revision **CR-2026.09.21-3** · every record is **LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE**. This is research, not betting advice. Odds and betting sources are excluded by design. No numerical model has been fitted yet. The first card-versus-baseline check (`SKILL_BASELINE_LEDGER.md`) shows **no demonstrated skill yet over a naive population baseline**.

## Start here

1. **[`CURRENT_RULES.md`](CURRENT_RULES.md)**: the live rules on one page, with the workflow, the card format, sport quick cards, the recurring-mistake list and the tools. This is step 0 of the reading gate.
2. **[`METHOD.md`](METHOD.md)**: the operational authority (workflow, six-field card, precedence).
3. The sport's `RULES_<SPORT>.md`, in full. The standing reading gate is in `RULES_GENERAL.md` §1.
4. The active log's top snapshot, [`PREDICTION_LOG_COMBINED_5.md`](PREDICTION_LOG_COMBINED_5.md), for the next ID and open items.

## How it works

```text
identity + state ─► contract (lines quarantined) ─► official participants, weather, evidence
   ─► one joint outcome distribution (centre, width, family masses, reference row, BASELINE_P)
   ─► derive every row's probability ─► rank by probability ─► freeze (manifest SHA) ─► log before delivery
   ─► settle from 3 independent lineages ─► receipts, lineup diff, z-scores ─► retrospective ─► tested lessons
```

The framework's working principles:
- evidence comes from field owners, never from markets;
- a stated probability must come from a printed distribution;
- a single game never creates a rule;
- every claim about skill has to beat a baseline.

## Repository map

| Area | Files |
|---|---|
| Live rules | [`CURRENT_RULES.md`](CURRENT_RULES.md) (summary) → [`METHOD.md`](METHOD.md), [`RULES_GENERAL.md`](RULES_GENERAL.md), `RULES_<SPORT>.md`, [`LEAGUE_RULES_CRICKET.md`](LEAGUE_RULES_CRICKET.md), [`LEAGUE_RULES_SOCCER.md`](LEAGUE_RULES_SOCCER.md), [`CONTROLS.md`](CONTROLS.md) |
| Scoring and evidence of skill | [`SCORING_AND_VALIDATION.md`](SCORING_AND_VALIDATION.md), [`SKILL_BASELINE_LEDGER.md`](SKILL_BASELINE_LEDGER.md), [`PERFORMANCE_ELIGIBILITY_POLICY.md`](PERFORMANCE_ELIGIBILITY_POLICY.md) |
| Reference data | [`BASE_RATES_REGISTER.md`](BASE_RATES_REGISTER.md) (§7: cross-sport rates and width benchmarks), [`RECENCY_AND_REBOUND.md`](RECENCY_AND_REBOUND.md), [`research/`](research/base_rates_2026-09-25/README.md) (re-runnable queries) |
| Sources | [`SOURCES.md`](SOURCES.md) (quick), [`DATA_SOURCE_REGISTER.md`](DATA_SOURCE_REGISTER.md) (full) |
| Procedures | [`UPCOMING_GAME_RESEARCH_GUIDE.md`](UPCOMING_GAME_RESEARCH_GUIDE.md) (pregame), [`EXTERNAL_LOGGING_WORKFLOW.md`](EXTERNAL_LOGGING_WORKFLOW.md) (mini logs, settlement), [`AGENT_ROLE_AND_TASK.md`](AGENT_ROLE_AND_TASK.md) |
| Learning | [`LEARNING_REGISTER.md`](LEARNING_REGISTER.md) (lessons, prospective tests, recurring mistakes M1–M31) |
| Logs | Parts 1–4 (closed) and [Part 5](PREDICTION_LOG_COMBINED_5.md) (active); [`GAME_LOG_STATUS_CURRENT.md`](GAME_LOG_STATUS_CURRENT.md) (state register); `Mini logs (to be sent to actual log later)/` (active mini log) |
| Numerical program (design only, not built) | [`NUMERICAL_PROGRAM.md`](NUMERICAL_PROGRAM.md), [`H0_DATASET_CARD.md`](H0_DATASET_CARD.md), [`NUMERICAL_MODEL_REGISTER.md`](NUMERICAL_MODEL_REGISTER.md), [`NUMERICAL_TRAINING_SPEC.md`](NUMERICAL_TRAINING_SPEC.md), [`MODEL_AND_DATA_SPEC.md`](MODEL_AND_DATA_SPEC.md), [`ALGORITHM_PORTFOLIO_AND_EVALUATION.md`](ALGORITHM_PORTFOLIO_AND_EVALUATION.md), [`MODEL_IMPLEMENTATION_RECIPES.md`](MODEL_IMPLEMENTATION_RECIPES.md) |
| Freeze receipts | `CONTROL_MANIFEST_*.md` (the current one is named in `METHOD.md`'s header) |
| History | [`CHANGELOG.md`](CHANGELOG.md) (dated changes, including the former README body), `archive/` (implemented audits, archived mini logs, historical snapshots) |

## Quickstart

All tools are standard-library Python 3.10 or later. There is nothing to install.

**Before issuing a card**

```bash
python tools/verify_manifest.py               # governance files match the current freeze receipt
python receipts.py pregame mlb 824703         # MLB: probables, official lineups, gamefeed weather, state
python receipts.py pregame espn basketball/nbl 401875254   # ESPN leagues: state, injury list
```

Print the reference row, reference width and `BASELINE_P` from [`BASE_RATES_REGISTER.md`](BASE_RATES_REGISTER.md) §7. Build the six-field card ([`METHOD.md`](METHOD.md) §4) and append it to the active mini log before delivery.

**At settlement**

```bash
python receipts.py settle mlb 824223 --card-home "Name A;Name B" --card-sp-home "Pitcher"
python receipts.py settle nhl 2026010034 --card-goalie-home "Goalie"
python receipts.py settle espn basketball/wnba 401857213 --card-away "A;B;C"
python audit_card_controls.py "<mini log>.md" --settlement --strict
python tools/skill_baseline.py                # after appending rows to SKILL_BASELINE_LEDGER.md
```

**Before committing** (CI runs the same checks: [`.github/workflows/checks.yml`](.github/workflows/checks.yml))

```bash
python -m unittest discover -s . -p "test_*.py"
python -m unittest discover -s tools -p "test_*.py"
python tools/repo_hygiene.py
python tools/verify_manifest.py
```

If you edited a governance file, regenerate the freeze receipt with `python tools/make_manifest.py --out CONTROL_MANIFEST_<date>-<n>.md --title "…" --note "…"`. Then repoint `METHOD.md` and the active mini log. See [`CONTRIBUTING.md`](CONTRIBUTING.md) for the branch and pull-request workflow.

## Current state

*The active log's top snapshot is the only authority for queue state and the next ID; this table is a convenience.*

| Item | State |
|---|---|
| Active canonical log | [Part 5](PREDICTION_LOG_COMBINED_5.md) (P-482 onward). Parts 1–4 are closed |
| Active mini log | `Mini logs (to be sent to actual log later)/Mini Prediction Log - P-510 onward - 2026-09-25/` |
| Next canonical ID | See Part 5's snapshot (P-510 as of 2026-09-25(c)) |
| Awaiting operator decision | Canonical numbers for `TMP-20260923-NBL-CNS-TAS` and `TMP-20260923-NPB-CHU-DB-G25` (both settled) |
| Freeze receipt | The manifest named in [`METHOD.md`](METHOD.md)'s header |
| Skill v baseline | Seed: card Brier 0.2461 v naive baseline 0.2360 (n = 29, 9 cards; interval spans 0). Prospective count 0 of 100 |
| Numerical model | Not built ([`H0_DATASET_CARD.md`](H0_DATASET_CARD.md)) |

## Canonical custody

| Part | Coverage | Custody |
|---|---|---|
| [Part 1](PREDICTION_LOG_COMBINED.md) | P-001–P-271 | Closed; settlement corrections only, including the reopened P-255/P-256 period questions |
| [Part 2](PREDICTION_LOG_COMBINED_2.md) | P-272–P-332 | Closed; nine inherited primary follow-up handles |
| [Part 3](PREDICTION_LOG_COMBINED_3.md) | P-333–P-423; P-372 reserved | Closed; 13 primary follow-up handles |
| [Part 4](PREDICTION_LOG_COMBINED_4.md) | P-424–P-481 | Closed at P-481; unresolved follow-up handles are tracked in the status register |
| [Part 5](PREDICTION_LOG_COMBINED_5.md) | P-482 onward | **Active queue / next-ID authority** |

Older component logs, archived mini variants and dated audits are evidence; they are not instructions. Preserve canonical IDs and temporary aliases. [`EXTERNAL_LOGGING_WORKFLOW.md`](EXTERNAL_LOGGING_WORKFLOW.md) covers variant discovery, reconciliation and archiving.

## Honesty boundary

- Issued forecasts, ranks and probabilities are never rewritten; corrections are appended.
- Missing lineups, timestamps, probabilities or records are recorded as missing, never invented.
- Every stated probability is an `UNVALIDATED_SUBJECTIVE` output of the card's own printed distribution.
- No record in this repository supports a performance, calibration, ROI or value claim. The first honest yardstick is the baseline ledger, and it has not been beaten yet.

## Licence

All rights reserved; see [`LICENSE`](LICENSE). Sports data remains subject to its providers' terms. The repository stores only derived statistics and small trimmed test fixtures.
