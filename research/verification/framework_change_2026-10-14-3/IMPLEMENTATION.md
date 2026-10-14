# Implementation: framework change 2026-10-14-3

**Instruction and decisions:** [CHANGE_PROPOSAL.md](CHANGE_PROPOSAL.md). **Design:** [ML_RL_IMPLEMENTATION_FRAMEWORK_2026-10-14.md](../../../ML_RL_IMPLEMENTATION_FRAMEWORK_2026-10-14.md). **Fixtures:** [FIXTURES.md](FIXTURES.md). **Verification:** [VERIFICATION.md](VERIFICATION.md).

## 1. Work-package map

Status values:
- `IMPLEMENTED`: built, run, and its acceptance evidence printed.
- `PARTLY`: some of it is done, and the remainder is named.
- `NOT_DONE`: not done, with the reason.
- `DEFERRED`: needs a later owner decision or a sporting season.

| WP | Disposition | What was done | Evidence | Status |
|---|---|---|---|---|
| WP-00 owner decisions | adopt | D1 = `ml/` in this repository (owner's choice; a variant of option B). D2 = SHADOW only. D3 = the owner asked for RL, so a firewalled paper decision lab was built and the betting prohibition was kept. D4 = tiered labels (LABEL_B for development, labelled). D5 = every archive-backed league plus IPL. | CHANGE_PROPOSAL §1 | IMPLEMENTED |
| WP-01 shadow lane definition | adopt | CURRENT_RULES §0 workshop exception, §1 reading-gate exclusion, §5a firewall, §7/§10 wording; prompt index exclusion; prompt 8 header; CONTRIBUTING; VERIFICATION_PROTOCOL §6; `research/model_shadow/README.md` (statuses, commit-then-reveal, guards) | diffs; archive copies in `archive/superseded_2026-10-14-3/` | IMPLEMENTED |
| WP-02 source register corrections | adopt (Cricsheet only) | Cricsheet licence ODbL → ODC-By. The football-data location conflict (F13) is left for the owner; the files stay git-excluded and are read only by the lab. | SOURCES line 63 | PARTLY |
| WP-03 workshop and archive rebuild | adapt | Workshop built (`ml/`). The canonical export was **not** rebuilt; the workshop reads the raw yearly CSVs directly, dropping and counting unusable rows. | `ml/data/archive.py`; load reports in each MODEL_CARD | PARTLY |
| WP-04 label admission (receipts) | defer | Not done: needs field-owner receipts for each league. Models are trained on LABEL_B and say so. | MODEL_CARD "Label tier" | NOT_DONE |
| WP-05 Cricsheet capture | defer | Not done: needs a download outside the repository and a provenance document. The IPL ladder uses archive scorecards only (C0–C2). | IPL MODEL_CARD | NOT_DONE |
| WP-06 baselines in code | adopt | `BASELINE_LEAGUE_V1` and TB-1 coded. TB-1 replicates the toolkit's hand figure (NBA 2025-26 home-win Brier 0.2165 in code against the toolkit's 0.2159 hand / 0.2161 tool). | §2 below; `ml/models/baseline.py` | IMPLEMENTED |
| WP-07 development models | adopt, widened to every competition (owner instruction 3) | One generic process over every competition folder: discovery, column detection, sport rules, automatic tune/test seasons, comparators (validated or `UNVALIDATED` TB-1). Rolling-origin weekly refits, tune-only hyperparameters with a pre-declared boundary-extension rule. Folders that cannot be modelled are listed with a reason. | `python -m ml discover`; `research/model_shadow/STATUS.md`; each `DEVELOPMENT_RESULTS.md` | IMPLEMENTED |
| WP-08 prospective lanes | defer | Tooling built and tested (`ml/shadow/lane.py`: freeze, receipt, reveal, settle). **No lane started**: a lane needs (a) a `SHADOW_CANDIDATE` model, (b) a registered hypothesis, and (c) a current-season results feed (the archive lags the live season). | §2; HYPOTHESIS_REGISTER entry | PARTLY |
| WP-09 cricket C0–C2 | adopt, generalised | Any limited-overs competition (overs cap from the format): IPL and ODI internationals today. Multi-day cricket is listed `NOT_MODELLED` with its reason. | `research/model_shadow/CRT20-IPL-FI-r1/`, `CROD-ODI-INTERNATIONAL-FI-r1/` | IMPLEMENTED |
| WP-10 calibration layer | adopt | Coherent winner reweighting (tested on the October 12 example) plus the ML-CAL-WIN experiment per model; calibration diagnostics for every model and for the cards (report R4). | DEVELOPMENT_RESULTS; CARD_CALIBRATION/REPORT.md | IMPLEMENTED |
| WP-11 challengers (GBM, NGBoost) | defer | Not built: §8.6 says challengers come only after a lane's L3 model is frozen, and none is. | — | NOT_DONE |
| WP-12 stage-1 review and sizing | defer | Needs prospective data. | — | DEFERRED |
| WP-13 promotion decisions | defer | No model is beyond development. | — | DEFERRED |
| WP-14 market benchmark | adapt | Delivered as MKT-BENCH-r1 inside the decision lab: historical EPL, model against the no-vig Pinnacle close, aggregates only. The archived ledger itself was not restored. | DECISION_LAB/RESULTS.md §1 | PARTLY |
| WP-15 decision project (RL) | adapt (owner-requested) | Paper-only lab in this repository under the §5a firewall: de-vig method chosen on warm-up seasons; shrunk quarter Kelly; LinTS bandit with CLV reward and logged propensities; full-information learner; off-policy check; drawdown halt. | DECISION_LAB/RESULTS.md | IMPLEMENTED (paper only) |

## 2. Results (from the committed run; numbers are copied from the generated files)

<<RESULTS>>

## 3. What this change does not do

- It makes no card, rule or rank depend on a model; no model is REFERENCE or ANCHOR.
- It claims no prospective skill. Every model result is `HISTORICAL_DEVELOPMENT`.
- It gives no betting advice. The decision lab is a paper study, and its result is negative.
- It does not rebuild the canonical export, verify labels against field owners, capture Cricsheet, or start a live lane.
- It does not touch any issued card, mini, log, grade, P-ID, archive CSV or dated report.
