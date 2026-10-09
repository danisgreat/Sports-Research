# Research workspace

**Markdown, CSV and text only.** Current state (next ID, active Combined Log) is in [../CURRENT_STATE.md](../CURRENT_STATE.md); the controlling rules are [../CURRENT_RULES.md](../CURRENT_RULES.md). The previous version of this page, which documented the Python workspace, is kept in [../archive/superseded_2026-10-09/research_readmes/research_README.md](../archive/superseded_2026-10-09/research_readmes/research_README.md). The code and JSON that lived under `research/` (source adapters, daily jobs, model builds, experiments, validators, receipts, registries) were removed on 2026-10-09; their last working state is commit `37203fc2b`.

## What is in this folder now

| Path | What it is |
|---|---|
| [prompts/](prompts/README.md) | The eight operator prompts and the golden examples |
| [scoreboard/SCOREBOARD.md](scoreboard/SCOREBOARD.md) | The top-two scoreboard, updated by hand after each import and retrospective |
| [issued_research/](issued_research/) | Preserved original texts of issued cards (`.txt`), byte for byte. Never edit |
| [verification/](verification/) | Dated evidence: reports, settlements, imports, reconciliations, retrospectives. Append-only; each folder is a record of that day |
| `data/processed/league_csv/` | `epl_results.csv` and `nbl_results.csv`, used by the archive check for sports whose yearly archive files are header-only |
| `data/raw/openfootball/` | English Premier League fixtures and results as text, one file per season (2020-21 to 2026-27) |
| `data/nbl_box_team.csv`, `data/nbl_results_wide.csv` | NBL team box scores and a wide results table |
| `data/processed/legacy_learning/` | `cards.csv` and `contracts.csv`: the literal, learning-only view of the historical rank log |
| `runs/` | CSV forecasts from the September and October EPL and NBL development runs (frozen historical evidence; their producing code is removed) |
| `custody/` | Markdown and CSV copies of the 2026-10-01 controls and run outputs (historical custody) |
| `EPL_PREREGISTRATION_2026-09-29.md`, `NBL_PREREGISTRATION_2026-09-29.md`, `baselines.csv`, `SETTLED_OUTCOMES_*.csv`, `PILOT_LEDGER_TEMPLATE.csv` | Historical pre-registrations and ledgers from the earlier model programme |
| `requirements*.txt` | Python dependency lists for the removed runtime (historical; nothing installs them) |
| `daily/`, `lineage_audits/`, `experiments/` | One-file remnants of the removed jobs |
| `src/`, `tests/`, `operations/`, `model_builds/`, `schemas/`, `shadow/`, `reachability/`, `baseline_definitions/` | Empty after the removal of code and JSON |

## The cycle in one paragraph

An external chat agent starts a mini (prompt 2), writes one card per event (prompt 1) and settles the mini within 72 hours of the finals (prompt 3). Claude Code imports the settled mini into the active Combined Log by hand edit (prompt 4), rolls the log over when it is full (prompt 5) and writes a cohort retrospective once about 30 cards have settled (prompt 6). Prompts 7 and 8 extend the archive and change the framework. All of it is documents: see [../PROMPTS.md](../PROMPTS.md).

## Rules for this folder

- Add nothing that is not Markdown, CSV or text. No scripts, JSON, notebooks or binary files.
- Never edit `issued_research/` or an existing `verification/` report. Add a new dated folder instead.
- A verification folder is named `<kind>_<date>` and holds a `REPORT.md` or the report files named by the prompt that created it.
