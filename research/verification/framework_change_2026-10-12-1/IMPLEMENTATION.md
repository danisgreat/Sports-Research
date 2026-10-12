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

| ID | Decision | Change made (files) | Acceptance evidence | Status |
|---|---|---|---|---|
| R08 | Adopt | Prompt 1: cricket §3.3, tennis §3.10, AFL §3.5, American football §3.8, rugby §3.6 + §3.7, basketball §3.2 + §3.13, baseball §3.1, soccer §3.4 (+§3.32). Hockey: §3.9 for the NHL only, with named non-NHL routes; "other sports" gets the fallback rules. All as anchored links | Link check of prompt 1: 23 links, 0 problems, anchors included (fixtures F01–F02) | DONE |
| R09 | Adopt | `PUBLISHED_MAIN_PINNED` / `LOCAL_WORKING_TREE`, one per run, with SHA and differences printed: CURRENT_RULES §0, prompts README receipt and text, prompts 1–3, prompt 4, mini authority table, VERIFICATION §1 | Fixtures F03–F04 | DONE |
| R10 | Adopt | GAME_LOG_STATUS_CURRENT line 4 rewritten (local staging, then prompt-4 import), with a dated note. Edited at byte level (the file is `-text` with mixed endings) | `git diff`: 1 line; 80 CRLF retained | DONE |
| R11 | Adopt | PROBABILITY_TOOLKIT operative-status table and per-section banners (§4 anchoring, §5 RM-1, §8 shares, §10 Brier(q) non-operative; §11 checks rewritten). All 11 RULES_<SPORT> files get a v11 precedence banner. Nine inline "Rank by RM-1 q" lines and two cricket chase-cap lines marked; cricket §7 of the toolkit corrected | Base copies archived; scan finds no unmarked "Rank by RM-1 q" | DONE |
| R12 | Adopt | Toolkit §6 rewritten: games handicap over all match states, including deciding-set losses; the false bound removed; set vs game handicap distinguished. §11 check 3 restricted. SELECTION_RULES §4 tennis row; prompt 1 tennis section | Counterexample computed: 6-0 4-6 4-6 → match LOSS, −1.5 games WIN (F09) | DONE |
| R13 | Adopt | Toolkit §3.1 moneyline-on-tie made contract-specific; SELECTION_RULES §4 ties row; LEAGUE_PROFILES sport constants (support limit relabelled; baseball draws competition-specific); prompt 1 baseball | Fixture F10 | DONE |
| R14 | Adopt | SELECTION_RULES §2 precision rule (ε, `GATE_UNRESOLVED_PRECISION`, `PRECISION_TIE`, adjustments only through the normalised distribution); toolkit rounding paragraph and §1.3 key numbers; prompt 1 | Fixtures F11–F12 | DONE |
| R26 | Adopt | Prompt 7 §2 SUSPECTED_DEFAULT → MEASURED / NOT_APPLICABLE / UNOBSERVED / CONFIRMED_PLACEHOLDER; ARCHIVE_USE_GUIDE §9 rule 4 | Fixtures F05–F06 | DONE |
| R27 | Adopt | Prompt 7 §3 endpoint-specific equations, never balance, usable-for-final-score versus period; ARCHIVE_USE_GUIDE §9 rule 5 | Fixture F08; the rebuilt hockey archive flags 55 rows and balances 0 | DONE |
| PR-01 | Adopt (retrieval) / register (use) | CURRENT_RULES §7; ARCHIVE_USE_GUIDE recipe R2 (seven steps; equal-weight L20 shrunk with toolkit k; four-window recency blend printed as a comparison; opponent context; season boundary; no lean without mechanism); template §3b and card line; prompt 1 (all 10 sports); C17; FC11-FORM-v1 | Example card shows the arithmetic (A 1.209 / blend 1.240); fixtures F24–F25 | DONE (experiment: 0 events) |
| PR-02 | Adopt | `archive/historical_restored/RECENCY_AND_REBOUND.md`, byte-exact from `a3c39d2f4^`, with README; link recovery in HISTORICAL_LINK_INDEX | `cmp` identical. The study's team-points table now cited correctly in recipe R2 (the MLB figures are starters' earned runs, not team scoring) | DONE |
| PR-03 | Adopt (user-authorised) / register | CURRENT_RULES §7 mixture pricing (0.25/0.50/0.25 default, frozen before pricing); `p_base` column; `SHADOW_BASE_ONLY`; C19; FC11-MIX-v1 | Example card: symmetric cases, so mixture = base (F27); fixture F26 | DONE (experiment: 0 events) |
| PR-04 | Adopt | CURRENT_RULES §5 two-step issue window and `LINEUP_UNCONFIRMED`; prompt 1 §2; card "lineup state / issue step" line; C20 | — | DONE (monitoring: RET-05) |
| PR-05 | Shadow | SELECTION_RULES §3(c) `SHADOW_RANK_DELTA`; template line; prompt 1 §5; SCORING §6; FC11-DELTA-v1 | Example: c_away and d_winner (Δ .10), joint loss .30 | SHADOW_READY |
| PR-06 | Adopt | SELECTION_RULES §9 coverage line and enumerated reasons; template; C18 | Fixture F29 | DONE |
| PR-07 | Merged into R33 | — | — | DONE (see R33) |
| PR-08 | Adopt via PR-01 | Archive read built into recipe R2 and C17 | — | DONE |
| PR-09 | Register | FC11-BIAS-v1 (shadow only; per-league start when the sample is reached) | HYPOTHESIS_REGISTER v3 | REGISTERED |
| PR-10 | No change | NBL profile already refreshed in run 2 (LP-2026.10.11-v2) | LEAGUE_PROFILES | NO_CHANGE |

## Phase C — lifecycle, custody, coverage and maintenance (R15–R23, R33–R38)

| ID | Decision | Change made (files) | Acceptance evidence | Status |
|---|---|---|---|---|
| R15 | Adopt | Writer and lease fields in the mini authority table; prompt 2 §2 single-issuing-writer rule; prompt 1 §2 check; CURRENT_RULES §8; C20 | Fixture F13 | DONE |
| R16 | Adopt | FROZEN_SOURCE receipt and growth check: prompt 3 §1, template §6, S14; prompt 1 refuses frozen minis | Fixture F14; example package receipt | DONE |
| R17 | Adopt | Revision keys, parent chain, affected keys, REVISION_CONFLICT: CURRENT_RULES §8, template §6, prompt 3 §4, SCORING §7, VERIFICATION §3.11, S13 | Fixture F15 | DONE |
| R18 | Adopt | Pre-mutation recheck: CURRENT_RULES §9, prompts 4 and 5, VERIFICATION §3.10 and §4 | — | DONE |
| R19 | Adopt | Marker integrity and legacy declaration: template §8, prompt 4 §2, VERIFICATION §3.9 | Fixtures F16–F17 | DONE |
| R20 | Adopt | Four identities: CURRENT_RULES §9, prompt 4, VERIFICATION §1. **Finding:** the byte-exact `-text` rules exist only in this machine's `.git/info/attributes`. Recorded as an owner decision; no attribute file was changed | Real incident caught and repaired (F18) | DONE (owner decision open) |
| R21 | Adopt | Prompt 5 trigger, calibrated to actual part sizes (1.5 MB / 50 entries; Part 7 was 1.26 MB with 30 entries); cross-part revisions to the active part: template §8, prompt 5 | Fixtures F19–F20 | DONE |
| R22 | Adopt | Intake table (template §2-D), prompt 1, SCORING §1 request coverage, prompt 6 | Fixture F21 | DONE |
| R23 | Adopt | SCORING §2a evidence-stratified views; prompts 3 and 6; settlement template | Fixture F22 | DONE |
| R33 | Adopt | SELECTION_RULES §5 line-difficulty rule; decision-table column (units / z); prompt 1; prompt 6 item 6; C18 | Fixture F28; example distances −1.249 / −0.978 | DONE |
| R34 | Adopt | CURRENT_RULES §11 revision classes; prompt 8 §4; suite P-2026.10.12-v11.0 (FORMAT + PROCEDURE). CHANGELOG clarification that the 2026-10-12 "generalise" entry changed behaviour | Fixture F32 | DONE |
| R35 | Adopt | [FIXTURES.md](FIXTURES.md) F01–F32 (manual walkthroughs, labelled as manual); prompt 8 §5 requires fixtures | Example prefix check executed | DONE |
| R36 | Adopt | HISTORICAL_LINK_INDEX "2026-10-12 recovery map" (38 targets plus the status register's historical links; every Git recovery checked). SOURCES and LEARNINGS_INDEX live links repointed; archive README link qualified. Dated CHANGELOG entries untouched | Link check of the live set: 0 problems outside dated sections | DONE |
| R37 | Adopt | [ACTIVE_FILE_INDEX.md](../../../ACTIVE_FILE_INDEX.md): operating files; 35 populated archive folders with seasons, logical rows, header width, provenance status; scan notes | 475,734 rows (454,014 without aliases) by CSV parser | DONE |
| R38 | Adopt | Queue fields in the template, prompts 2 and 3, CURRENT_RULES §8. The current queue (P-577 to P-579) gets actor, route, due time and scheduling status in GAME_LOG_STATUS_CURRENT (byte-level insert). P-579's capture due time had already passed: recorded as a breach | 8 lines added, CRLF style kept | DONE |
| NEW-01 | Adopt (non-destructive) | Fingerprint and duplicate scan of every archive folder. 4 byte-identical alias pairs on main (Austria/BSL, Danish/Metal Ligaen, ODI/Men's ODI, College Football pair) marked with `ALIAS_OF_CANONICAL.md` and in ARCHIVE_USE_GUIDE §8. `SUSPECTED_DEFAULT` start times (Austria, Greek, Danish), NBA/WNBA attendance 0, KBO/NPB/college patterns noted. **No published rows deleted**; emptying aliases and classifying the flagged columns are owner/prompt-7 decisions | ACTIVE_FILE_INDEX §2 | DONE_PARTIAL |

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
