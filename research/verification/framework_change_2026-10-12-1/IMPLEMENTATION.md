# Implementation map — framework change 2026-10-12-1

[Change proposal](CHANGE_PROPOSAL.md) · [Data rebuild receipt](DATA_REBUILD_RECEIPT.md) · [Verification report](VERIFICATION_REPORT.md) · [Audit input](AUDIT_RECOMMENDATIONS_2026-10-12.txt)

**Status vocabulary:**
- **DONE:** document or data change made and checked.
- **DONE_PARTIAL:** made for a stated scope, with the remainder named.
- **SHADOW_READY:** recording instruction exists; no outcome collected.
- **REGISTERED:** experiment frozen in HYPOTHESIS_REGISTER; 0 events.
- **DATA_PENDING:** work attempted or scoped and not finished, with the reason.
- **NO_CHANGE:** already satisfied, with evidence.
- **PLANNED:** in this change, not yet done at the time of writing; updated before publication.

No status here means a predictive improvement.

Order of work: phase A (R01–R07), then B (R08–R14, R26–R27, PR-01–PR-10), C (R15–R23, R33–R38), D (R24–R25, R28–R32), following the audit's §4.

## Phase A — containment and repair of unpublished data (R01–R07)

| ID | Decision | Change and files | Acceptance evidence | Status |
|---|---|---|---|---|
| R01 | Adopt | Fabricated Czech build quarantined outside the repository (byte copies + patch). 51 seasons rebuilt from the captured hockeyarchives pages, observed fields only: no default date/time/attendance/referee, no estimated or balanced periods. `Previous Sports Results/Ice Hockey/Czech Extraliga/<YEAR>/<YEAR>_games.csv`, `…/DATA_PROVENANCE.md` | 18,752 rows; 0 start-time/attendance/referee values; dates only from source (16,909); 55 period-sum typos flagged, not balanced; 8/8 external sample. [Receipt](DATA_REBUILD_RECEIPT.md) §3 | DONE |
| R02 | Adopt | Football rebuilt from england.csv and football-data observed fields only. HT only where printed (1995-96+), kick-off only 2019-20+, referee and statistics only 2000-01+, attendance only where printed, no matchweek approximation, odds never read. `Previous Sports Results/Soccer/Premier League/…` | 20,740 rows; 0 default values; 11,943/11,944 two-compiler agreement; 9/9 ESPN sample | DONE |
| R03 | Adopt | Hand-typed Community Shield table quarantined and **excluded**. The Shield is not a league match. It may be added later only with per-row official receipts | 0 Shield rows in every active copy (the alias copies are out of the repository) | DONE |
| R04 | Adopt | Unpublished SOURCES §3.34/§3.35 withdrawn. New SOURCES §3.31/§3.32 name only the sources read, per field, with checks and limits. Field matrices in both DATA_PROVENANCE files. ARCHIVE_USE_GUIDE §9 rule 7 limits "verified" claims | Claims reviewed against what was actually read | DONE |
| R05 | Adopt | Schema migration recorded: old 13-column placeholder names kept, new columns listed, 56 (hockey) and 54 (football) columns. The 36-versus-38 miscount noted | DATA_PROVENANCE §3 in each folder | DONE |
| R06 | Adopt | One canonical path per competition (aliases and root copies quarantined). Stable surrogate IDs from date and teams, never row numbers. ARCHIVE_USE_GUIDE §9 rules 1–2 | 0 duplicate IDs; alias folders absent from the repository | DONE |
| R07 | Adopt | 16 .py files, caches and 51 .htm moved out of the repository into the quarantine folder (preserved). CONTRIBUTING states that helpers and raw captures stay outside the repository, with their SHA-256 recorded in receipts | `git status` shows no code or HTML; CONTRIBUTING rule added | DONE |

## Phase B — instruction conflicts, mathematics and prediction (R08–R14, R26–R27, PR-01–PR-10)

| ID | Decision | Change and files | Status |
|---|---|---|---|
| R08 | Adopt | Correct prompt-1 SOURCES sections per sport, using anchored links; both rugby routes; non-NHL hockey routes | PLANNED |
| R09 | Adopt | One authority mode per run, printed with SHA and differences: CURRENT_RULES §0, prompts README, prompts 1–3 | PLANNED |
| R10 | Adopt | Status-register line 4 clarified (local staging → prompt 4 import) | PLANNED |
| R11 | Adopt | PROBABILITY_TOOLKIT retired procedures (q-ranking, old anchors) marked non-operative in place, with a compact active section | PLANNED |
| R12 | Adopt | Tennis bound removed; games handicap from complete set-score states | PLANNED |
| R13 | Adopt | Tie and moneyline treatment competition- and contract-specific; profile maxima labelled computational support limits | PLANNED |
| R14 | Adopt | Precision rule at gates and close orders; key-number adjustments applied to a normalised distribution | PLANNED |
| R26 | Adopt | Prompt 7: SUSPECTED_DEFAULT diagnostic instead of automatic missingness | PLANNED |
| R27 | Adopt | Prompt 7: endpoint-specific reconciliation equations; never balance | PLANNED |
| PR-01 | Adopt (retrieval) / register (use) | Form-window block L5/L10/L15/L20 + season + league in template A3, prompt 1 every sport, recipe R2 rewrite, C17 audit check; blended shrunk rate; experiment FC11-FORM-v1 | PLANNED |
| PR-02 | Adopt | Restore `RECENCY_AND_REBOUND.md` from history as an archived reference; link recovery mapping | PLANNED |
| PR-03 | Adopt (user-authorised) / register | Price from the declared sensitivity mixture when an input is labelled unfitted or uncertain; base-only p kept as shadow; FC11-MIX-v1 | PLANNED |
| PR-04 | Adopt | Two-step issue window (research by T−60, freeze after lineup check, no later than T−5) | PLANNED |
| PR-05 | Shadow | SHADOW_RANK_DELTA (rank by p_card − BASELINE_P); FC11-DELTA-v1 | PLANNED |
| PR-06 | Adopt | Baseline coverage line on every card; enumerated missing reasons | PLANNED |
| PR-07 | Merge into R33 | Line-distance column | PLANNED |
| PR-08 | Adopt via PR-01 | Archive read becomes a fixed step | PLANNED |
| PR-09 | Register | FC11-BIAS-v1 per-sport expected-score bias design; no correction before its sample | PLANNED |
| PR-10 | No change | NBL profile already refreshed in run 2 (LP-2026.10.11-v2) | NO_CHANGE |

## Phase C — lifecycle, custody, coverage and maintenance (R15–R23, R33–R38)

| ID | Decision | Change and files | Status |
|---|---|---|---|
| R15 | Adopt | Writer lease in the mini authority table; prompts 1–2 check it | PLANNED |
| R16 | Adopt | Frozen-source receipt and growth check in prompt 3; prompt 1 refuses appends to a frozen mini | PLANNED |
| R17 | Adopt | Revision keys, parent pointers, affected keys and deterministic effective-grade resolution: templates §6, SCORING §7 | PLANNED |
| R18 | Adopt | Pre-mutation recheck (HEAD, path, destination tail) before each mutation batch: VERIFICATION §3–4, prompts 4–5 | PLANNED |
| R19 | Adopt | Balanced-marker and legacy-format check before import | PLANNED |
| R20 | Adopt | Four named identities (raw source, imported core, destination prefix, committed blob) and `git ls-files --eol` checks | PLANNED |
| R21 | Adopt | Measurable rollover trigger; cross-part revision routing | PLANNED |
| R22 | Adopt | Request-intake table in the mini; coverage NOT_COMPUTABLE historically | PLANNED |
| R23 | Adopt | Evidence-stratified scoring views (A/B headline, +C/E sensitivity, unresolved bounds) | PLANNED |
| R33 | Adopt | Decision-table line-distance column | PLANNED |
| R34 | Adopt | Prompt revision policy and classes; suite P-2026.10.12-v11.0; dated clarification of the earlier "wording-only" entry | PLANNED |
| R35 | Adopt | Manual negative and edge fixtures for each new check | PLANNED |
| R36 | Adopt | Live navigation repointed; historical broken paths mapped in HISTORICAL_LINK_INDEX | PLANNED |
| R37 | Adopt | ACTIVE_FILE_INDEX.md with populated-season and row counts per competition | PLANNED |
| R38 | Adopt | Executable follow-up fields for every queue item; current P-577–P-579 queue given actor, route and due time | PLANNED |

## Phase D — claims, designs and data readiness (R24–R25, R28–R32)

| ID | Decision | Change and files | Status |
|---|---|---|---|
| R24 | Adopt | CURRENT_STATE wording "does not establish incremental skill" plus a dated clarification | PLANNED |
| R25 | Adopt | Two-stage internal-pilot design with all design inputs fixed now, for FC10 and FC11 experiments | PLANNED |
| R28 | Adopt | Known-at rule in CURRENT_RULES §5 and prompt 1 (archive rule already in ARCHIVE_USE_GUIDE §9.6) | PLANNED |
| R29 | Adopt (scoped) | Field-lineage matrix for leagues in current use, with live route probes | PLANNED |
| R30 | Adopt | NBL 2025 dates, stage and quarter-flag repair from the prepared sidecar; 2026 snapshot denominator and corroboration | PLANNED |
| R31 | Attempt | KBO/NPB observed innings recovery for a declared scope, or DATA_PENDING with the routes tried | PLANNED |
| R32 | Adopt | Profile freshness table (as-of, window, coverage, permitted endpoints); new rows only where the archive supports them | PLANNED |
| NEW-01 | Adopt | Scan the other builder-era archive folders (SOURCES §3.14–§3.30) for the R01/R02 default fingerprints | PLANNED |
