# Verification report: framework change 2026-10-14-1

Format: `Check | PASS/FAIL/NOT_VERIFIED | evidence | limitation` (VERIFICATION_PROTOCOL). Run by this session on 2026-10-14 with plain git/file commands and CSV-aware reading from a scratch area outside the repository. **A green check proves only what it checks.** None of these is a predictive validation.

| Check | Result | Evidence | Limitation |
|---|---|---|---|
| Pre-change inventory recorded | PASS | Quarantine `git_status_before.txt`; HEAD = origin/main = `e73c9c24e` | — |
| Quarantined work preserved before removal | PASS | 2,089 files copied; `cmp` against the repository: 0 mismatches; full binary patch of `e73c9c24e` saved | Outside Git; the owner decides retention |
| No code, JSON, database or HTML added | PASS | Staged additions/modifications by extension: 0 `.py`, `.json`, `.db`, `.html`. Those types appear only as deletions | — |
| Unrelated work preserved | PASS | `PROMPT_1_SUPPLIED_FIRST_EXTENDED_2026-10-14.md` (untracked, another writer) not staged; `MODEL_PROBABILITY_ML_RECOMMENDATIONS_2026-10-12.md` and the prompt-1 edit kept | — |
| Issued logs, cards, P-IDs, earlier change folders unchanged | PASS | No staged path under `prediction logs/`, `research/issued_research/` or `framework_change_2026-10-1[12]*` | — |
| Rows, CSV-aware | PASS | KBL 8,285; B League 6,350; Liga ACB 15,881; EuroCup 4,851; NBA G League 10,947 (total 46,314) | — |
| Duplicate Game IDs | PASS | 0 in every league | — |
| Date ↔ weekday | PASS | 0 disagreements; KBL and B League printed weekdays also agree (0 `SOURCE_WEEKDAY_CONFLICT`) | — |
| Season ↔ date alignment | PASS | Every file's dates fall in its season (this also confirms the ACB edition mapping) | — |
| Regular-season games per team | PASS with documented exceptions | Equal per team in every completed season, except COVID-stopped seasons and the shortfalls named in each DATA_PROVENANCE §4 | Shortfalls not checked game by game |
| Leftover-default scan | PASS | Most common value per field: start times ≤ 25.6% (G League 00:00 UTC = 19:00 US Eastern), attendance ≤ 6.2% (COVID zeros), referees ≤ 0.2%, venues ≤ 10.9%. The `e73c9c24e` fingerprints (19:00 / 2,500 / "Official Crew" / `1` / "European Indoor Arena" / "Pabellón Polideportivo") are absent | Diagnostic, not proof of truth |
| Reconciliation (quarters + OT = final) | PASS | KBL 1 mismatch flagged; EuroCup 0; G League 0 (ESPN rows); nothing balanced | B League and ACB have no quarter fields |
| External finals samples | PASS | KBL 2024-25 (7) and 2025-26 (5) vs ko.wikipedia result sequence; B League 2024-25 (3) vs ja.wikipedia bracket; Liga ACB 2024-25 (3) vs en.wikipedia; EuroCup 2024-25 (2) and NBA G League 2024-25 (3) vs en.wikipedia | 23 games; samples only |
| B League carried dates | PASS | 12 of 12 random header-dated games (seed 20261014) match their bleague.jp game page | Same publisher |
| ESPN join safety (G League) | PASS | Join requires a unique score-date match and both team ids mapped; 339 id disagreements and 41 ambiguous matches not used | Evidence B |
| Archived originals | PASS | `archive/superseded_2026-10-14/`: SOURCES (from `65f780cef`), ACTIVE_FILE_INDEX, ARCHIVE_USE_GUIDE, CHANGELOG (from `e73c9c24e`) equal the pre-edit working text | — |
| Relative links in new and edited documents | PASS | 136 checked, 0 missing once this report exists | Anchors not checked |
| `git diff --cached --check` | PASS | No whitespace errors | — |
| Line endings | PASS | New CSVs and documents are LF, like the placeholders they replace (core.autocrlf=true converts on checkout) | — |
| Remote publication | Recorded in the commit | Push to origin/main after this report | Verified after push by `git rev-parse` |
