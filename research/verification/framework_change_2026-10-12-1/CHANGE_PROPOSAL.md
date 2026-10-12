# Change proposal — framework change 2026-10-12-1

## 1. Instruction and authority

**User instructions (verbatim, 2026-10-12, Australia/Sydney):**
1. "provide all of the recommendations to improve the prediction part of the framework, and is there a way to get the last 10,15,20 games as well into the stats, and not just account for the last 5 games ?"
2. "implement all of the recommendations and push to the main brnach on git"
3. (on the selected `AUDIT_RECOMMENDATIONS_2026-10-12.txt`) "thoughts on the selected audit recommendations"
4. "implement all of the recommendations in order, carefully and methodically"

Instruction 2 authorises publication to `main`. Instruction 4 covers both recommendation sets: the 38 audit items R01–R38 in the audit's own priority order, and the 10 prediction recommendations given in reply to instruction 1, labelled PR-01 to PR-10 here. The audit text is preserved verbatim beside this file ([AUDIT_RECOMMENDATIONS_2026-10-12.txt](AUDIT_RECOMMENDATIONS_2026-10-12.txt), SHA-256 `f8aad004…5b23e6`).

**Reading receipt.**

| Item | Value |
|---|---|
| Authority mode | Local working tree inside the repository. Prompt 8 runs locally; `main` is the publication target |
| Repository / branch / base | `C:\Users\danie\Desktop\Sports Research`, `main`, `eb1acf58bb7b8c794a2f6a473f737d921f2d5fae`. Local HEAD equalled freshly fetched `origin/main` (0 ahead, 0 behind) at 12:50 AEDT |
| Working differences at start | 107 modified tracked files: 102 Czech Extraliga / Premier League yearly CSVs, 4 roster/venue .md and SOURCES.md, all from an unpublished local build of 02:05–02:34 AEDT. 12 untracked entries (that build's copies, code and caches, plus the audit text). None was by this session |
| Read in full | CURRENT_STATE, METHOD, CURRENT_RULES, SELECTION_RULES, CARD_AND_LOG_TEMPLATES, SCORING_AND_VALIDATION, VERIFICATION_PROTOCOL, CONTRIBUTING, research/prompts/README and prompts 2–8, prompt 1 (common structure and the basketball section; the other sport sections by their source/reading lines), the latest completed retrospective (retrospective_2026-10-11: §2, §3.13, §4, §5, §7), the run-1 implementation map, the HYPOTHESIS_REGISTER v10 amendments and run-2 update, the three latest CHANGELOG entries, ARCHIVE_USE_GUIDE in full, both builders and fetch helpers of the local build |
| Sections read | SOURCES §2.3, §3.13–§3.30 headings and §3.30; LEARNING_REGISTER L-052, L-20260919-01/04, L-20260925-08; LEARNINGS_INDEX L-052; RULES_BASKETBALL §8.8; RULES_AFL §8.8 |
| Versions at start | MDS-2026.10.11-v10.0 · CR-2026.10.11-R1 · SCV-2026.10.11-v6 · SEL-2026.10.11-v2 · mini-log-6 / mini-settlement-5 · prompts P-2026.10.11-v10 |
| Contradictions found at start | Prompt 1 source sections (R08). Status register line 4 against prompts 1–3 (R10). PROBABILITY_TOOLKIT §5 q-ranking against P_ORDER_V2 (R11). Tennis bound (R12). The L5/L10/L15/L20 retrieval rule in RULES_<SPORT> §8.8 has no field in the v10 template or prompt 1 (PR-01). LEARNING_REGISTER links a missing `RECENCY_AND_REBOUND.md` (PR-02) |

## 2. Defects in scope

| Group | Defect (evidence) | Class |
|---|---|---|
| R01–R03 | Local hockey and football builders invented fields: Czech dates defaulted to 15 September (16,242 rows), fixed start times/attendances/referees, balanced period scores. Football half-time scores were set to full-time ÷ 2, with fixed kick-offs/attendances, approximate matchweeks and a hand-typed Community Shield table (2025 row false) | Data repair |
| R04–R06 | "Verified" claims for fabricated fields; 36- vs 38-column schema claim; three byte-identical copies per season; row-number IDs | Data repair / integrity |
| R07 | 16 Python files and 51 HTML caches in a Markdown/CSV/text repository | Integrity (scope) |
| R08–R14, R26–R27 | Wrong prompt-1 source sections; authority-mode ambiguity; status register contradiction; retired q-ranking text still operative-looking; invalid tennis bound; universal tie claims; rounding at gates; overbroad constant-column rule; non-endpoint-specific reconciliation | Administrative correction / process repair / scoring definition |
| R15–R23, R33–R38 | Writer ownership, freeze lifecycle, settlement revision resolution, pre-mutation rechecks, marker checks, byte identity under `core.autocrlf=true`, rollover trigger, request intake, evidence-stratified scoring, line-difficulty field, prompt versioning, regression fixtures, broken navigation, active-file index, executable queue follow-ups | Process repair / format definition |
| R24–R25, R28–R32 | Causal "not skill" wording; incomplete acceptance designs; known-at time; lineage; NBL date/stage repair; KBO/NPB innings; profile freshness | Claim correction / experiment design / data repair |
| PR-01 | L10/L15/L20 never reach the card (1 of the last 8 cards quoted a last-10 figure; 0 quoted L15/L20) | Process repair (retrieval) + registered experiment (use in the centre) |
| PR-02 | `RECENCY_AND_REBOUND.md` (window RMSE evidence) missing from the tree | Administrative (navigation) |
| PR-03 | The sensitivity case is computed but the pick ignores it. All 4 Rank-1 losses of the last cohort were ~1.2–1.3 SD lines priced from widths the card called unfitted | Selection/model change (user-authorised) + registered comparison |
| PR-04 | 12 of 20 cards completed after the scheduled start; 3 of 4 losses had unverified lineups | Process repair |
| PR-05 | No ranking diagnostic for information beyond the league baseline | Shadow experiment |
| PR-06 | BASELINE_P is defined, but 0 paired rows exist | Process repair (coverage reporting) |
| PR-07 | Line difficulty not shown (= R33) | Format definition |
| PR-08 | Archive read on 4 of 16 cards | Process repair (via PR-01 recipe) |
| PR-09 | No registered bias-correction design | Experiment design |
| PR-10 | NBL profile staleness | Already done in run 2 (LP-2026.10.11-v2); no change |

Change classes follow prompt 8 §2. A user instruction authorises the process and format changes. It does **not** make any predictive effect true: every model or selection effect is registered and stays untested.

## 3. Intended behaviour after the change

- **Archive.**
  - The Czech top flight and English top flight hold 51 seasons each of observed-only rows, each with a per-field provenance document, schema record, canonical path and stable IDs.
  - The fabricated local build and its code and caches are preserved outside the repository.
  - Archive integrity rules (one canonical path, stable IDs, no defaults, SUSPECTED_DEFAULT diagnostic, endpoint-specific reconciliation, known-at time, scoped "verified" claims) are written into ARCHIVE_USE_GUIDE §9 and prompt 7.
- **Cards** (mini-log-7):
  - **Form-window table:** L5/L10/L15/L20, season and league, from dated rows only, one shrunk blended rate with the windows not counted as separate confirmations, opponent context, and a season-boundary flag.
  - **Decision table:** gains a line-distance column.
  - **Pricing:** cards price from the declared sensitivity mixture when an input is labelled unfitted or uncertain, with the base-only p kept as a shadow.
  - **Timing:** a two-step issue window (research by about 60 minutes before start, freeze after the lineup check) with a request-intake table.
  - **Writer:** a writer lease.
  - **Audit:** a C17 audit check for the form windows.
- **Settlements** (mini-settlement-6): unique revision keys with parent pointers, deterministic effective-grade resolution, evidence-stratified scoring views, and executable queue follow-ups.
- **Imports and rollovers:** pre-mutation rechecks, a balanced-marker check, explicit raw-versus-normalised byte identity, and a measurable rollover trigger.
- **Rules:** a single authority mode per run; corrected source sections; non-operative labels on retired toolkit procedures; the tennis bound replaced; competition-specific ties; a precision rule at the gate.
- **Claims:** CURRENT_STATE says the cohort "does not establish" skill. Acceptance designs are completed with a two-stage internal-pilot plan (design inputs fixed now; variance from stage 1 only; stage-2 confirmatory cohort held out).

## 4. Versions

Bumped only where behaviour or format changes:
- MDS-2026.10.12-v11.0
- CR-2026.10.12-R1
- SCV-2026.10.12-v7 (revision resolution, evidence strata, new shadows)
- SEL-2026.10.12-v3 (precision rule, sensitivity mixture, two new shadows)
- formats mini-log-7 / mini-settlement-6
- prompts P-2026.10.12-v11.0 (class: PROCEDURE + FORMAT)

HYP gets a dated v3 amendment. canonical-md-1 is unchanged. In-progress minis in older formats finish unchanged; the new fields apply from the first mini-log-7 mini.

## 5. Verification plan

VERIFICATION_PROTOCOL §6 checks:
- every archived original against the base revision
- every changed relative link (file and anchor) resolved
- version strings consistent across METHOD / CURRENT_RULES / CURRENT_STATE / templates / examples / prompts
- old-format preservation
- `git diff --check`
- no code, JSON or HTML added
- issued logs, cards and dated reports byte-unchanged
- examples versus templates
- manual negative fixtures for each new check (R35)

Data checks:
- CSV-aware counts and ID uniqueness
- weekday consistency and absence of the quarantined default values
- two-compiler and external spot checks with receipts

Publication: commit by exact paths only (never the 102-file fabricated working state, never the quarantine), push without force, then fetch and compare the remote SHA and artifacts.

## 6. Rollback

Forward revision only. Data rollback restores the header-only placeholders from `eb1acf58b` (the archive copies and git history hold them). Rule rollback reinstates the archived originals under a new dated version. No issued forecast, grade, log byte, P-ID or dated report is changed by this proposal. Anything that cannot be finished honestly (for example a live source that cannot be reached) is left `DATA_PENDING` or `BLOCKED` with the attempt recorded, not reported as done.
