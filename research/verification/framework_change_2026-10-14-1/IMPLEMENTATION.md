# Framework change 2026-10-14-1: basketball archive quarantine and observed-only rebuild

[Data rebuild receipt](DATA_REBUILD_RECEIPT.md) · [Verification report](VERIFICATION_REPORT.md) · [Capture manifest](CAPTURE_MANIFEST.csv) · [Audit of 2026-10-12](../framework_change_2026-10-12-1/AUDIT_RECOMMENDATIONS_2026-10-12.txt)

**Class:** data repair (archive) and source documentation. No rule, prompt, template, log, card, grade, P-ID, profile or threshold changed.

## Why

Commit `e73c9c24e` (2026-10-14, "Rebuild B League, EuroCup, KBL and Liga ACB basketball archives; add G League and 2026 seasons") staged the whole working tree, as the user asked to push everything pending. It reintroduced on main what the 2026-10-12 change had contained, and so undid three of that audit's items:

- **R07:** 63 Python files, 4 SQLite databases, 32 JSON files and one saved HTML page went into `research/`. The repository holds Markdown, CSV and text only (CONTRIBUTING; CURRENT_RULES §0).
- **R01/R02:** the five basketball archives carried builder defaults:
  - NBA G League: 19:00 start on 49.8% and attendance 2,500 on 52.6% of rows.
  - B League: "… Official Crew" as the referee on 98.8% of rows, attendance 4,200, and hand-typed pre-2016 tables.
  - EuroCup: start time `1` on 81% of rows, and invented dates for every 1975–2001 row.
  - Liga ACB: UTC times labelled local, home arenas from a lookup table, and "No" overtime everywhere.
  - KBL: start times guessed from the weekday, and D-League games mixed in.
- **R04/R06:** an unscoped "verified" SOURCES §3.33 was added, along with the duplicate folder `Basketball/G League/`. The 2026-10-12 phase-D commit had already found the G League build and left it unpublished.

The same commit also added five unsourced research reports (three stored as escaped JSON strings, one a duplicate) and 16 new roster, venue, coach and officials Markdown files, and rewrote 10 existing roster and venue files. Like the 2026-10-12 roster files, they were treated as unsourced generated prose. The new files are quarantined, and the 10 rewritten files are back to their earlier content.

## What was done

| Step | Change | Audit items | Status |
|---|---|---|---|
| 1. Preserve | Everything above was copied byte-for-byte to `C:\Users\danie\Desktop\Sports Research LOCAL_QUARANTINE_2026-10-14\` (2,089 files checked with `cmp`, 0 mismatches), with `git status` and the full binary patch of `e73c9c24e`. Its README lists the contents | R07 | DONE |
| 2. Remove | The 179 files that `e73c9c24e` added in those groups were removed from the repository. The 266 basketball files it modified, and SOURCES.md, were restored to their `65f780cef` versions before the rebuild. The commit's other two changes stay: `MODEL_PROBABILITY_ML_RECOMMENDATIONS_2026-10-12.md` (another writer's document, Markdown) and the user's one-line prompt-1 edit | R04, R06, R07 | DONE |
| 3. Rebuild | KBL, B League, Liga ACB, EuroCup and NBA G League were rebuilt from each league's own record (KBL from the earlier session's API captures; the other four captured fresh on 2026-10-14). Observed fields only, blanks with reasons, stable native IDs, placeholder values blanked with flags, nothing balanced | R01, R02, R03, R05, R06, R26, R27 | DONE |
| 4. Document | One `DATA_PROVENANCE.md` per folder (field classes, exclusions, schema, checks, flags, per-season counts); SOURCES §3.33 with scoped claims; ACTIVE_FILE_INDEX §2; ARCHIVE_USE_GUIDE §8; CHANGELOG. Originals archived in `archive/superseded_2026-10-14/` | R04, R05, R37 | DONE |
| 5. Check | CSV-aware counts, duplicate IDs, weekday agreement, games per team, season-date alignment, a scan for leftover defaults, finals spot checks against Wikipedia, and 12 B.League carried dates against their game pages ([report](VERIFICATION_REPORT.md)) | R04 | DONE |

**Helpers.** The capture, rebuild and check scripts ran from the session's scratch area, outside the repository (CONTRIBUTING). Their rules are written out in each DATA_PROVENANCE §2. Raw captures stay in the quarantine folder's `captures/` with SHA-256 values in [CAPTURE_MANIFEST.csv](CAPTURE_MANIFEST.csv).

## Not done (open)

- **History rewrite (owner decision).** The quarantined files stay reachable in Git history at `e73c9c24e`. Removing them from history needs a force-push, which CONTRIBUTING forbids without the owner's decision.
- **Seasons not rebuilt (still header-only):**
  - B League before 2016-17 (JBL, bj-league, NBL Japan): no per-row source was available.
  - EuroCup before 2002-03 (different tier-two FIBA cups).
  - NBA G League 2001-02 to 2003-04: not in the league's statistics API.
  - NBA G League 2026-27: no game played at capture.
- **Coverage gaps by source:**
  - B League: quarter scores, attendance and referees are on per-game pages that were not captured.
  - Liga ACB: the source has no venue, attendance, referee, overtime or quarter fields.
  - NBA G League: before 2018 there are no quarters, venues or attendance.
- **Roster and venue Markdown files** (`HISTORICAL_PLAYERS_AND_ROSTERS.md`, `VENUES_AND_LOCATIONS.md`) in these folders are back to their pre-`e73c9c24e` content. They were not audited here.
