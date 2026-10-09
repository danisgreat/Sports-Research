# PROMPT 7 — EXPAND OR REPAIR THE PREVIOUS RESULTS

**Run by:** Claude Code in a local checkout of the repository · **GitHub:** write (archive CSVs and coverage notes) · **Mode:** `ARCHIVE_EXPANSION`

The archive in [Previous Sports Results/](../../Previous%20Sports%20Results/README.md) feeds every card's archive check ([ARCHIVE_USE_GUIDE.md](../../ARCHIVE_USE_GUIDE.md)). This prompt adds or repairs yearly game files. It produces **CSV and Markdown only**: you gather rows from the source routes by hand, write them in the folder's existing column layout, and prove them with printed arithmetic. The archive builders were removed on 2026-10-09 (last working state at commit `37203fc2b`); do not rebuild them as scripts.

---

## 0. Reading gate

Print the **reading receipt** ([research/prompts/README.md](README.md)) after opening: [CURRENT_RULES.md](../../CURRENT_RULES.md) (§5, §9), [ARCHIVE_USE_GUIDE.md](../../ARCHIVE_USE_GUIDE.md), [Previous Sports Results/README.md](../../Previous%20Sports%20Results/README.md), [COVERAGE_AND_BLANK_YEARS.md](../../Previous%20Sports%20Results/COVERAGE_AND_BLANK_YEARS.md), [DATA_SOURCES_IMPLEMENTATION.md](../../Previous%20Sports%20Results/DATA_SOURCES_IMPLEMENTATION.md), the league's source section in [SOURCES.md](../../SOURCES.md) (§3.14 to §3.30 describe how existing league histories were gathered; §3.1 to §3.10 give the live routes), [LEAGUE_PROFILES.md](../../LEAGUE_PROFILES.md), and the target folder's existing yearly file (header and a sample of rows).

## 1. Choose the target

Prioritise, in this order: (1) missing or stale seasons of a league that cards are being written for (check the league's last `Date` in its newest file); (2) official event-level labels and the columns a card needs (scores, overtime flag, starting pitchers, line scores); (3) older seasons. State the league, the season(s), the expected game count from the official schedule and why this target.

## 2. Collect

1. Use the source routes in SOURCES for that league (official first; independent corroboration for a sample). Keep the source's own identifiers (game ID, event ID) in the identifier column.
2. Write rows in the **existing header and column order** of the folder's other yearly files. Never invent a column. Leave unknown fields blank rather than guessed (unknown names, times and officials stay blank).
3. Postgame prose columns (`Notable Players`, one-line comment, `Game Summary`) stay postgame; fill them only from the source and never as pregame evidence.
4. Awards and whole-season narratives stay out of game rows.
5. Record each source used (URL, what it supplied, date read) in a short `<Year>_SOURCES.md` beside the CSV or in the coverage document; there are no stored response bodies.
6. Do not edit an existing row of a verified file to "fix" it unless you can cite the official record; if you do, list the change in the coverage document.

## 3. Prove it (print every result)

| Check | How |
|---|---|
| Header | The first line equals the header of a sibling year file (compare with `head -1`). |
| Row count | Data rows (`wc -l` minus 1) equal the official game count for the season, or the gap is listed. |
| Duplicates | No duplicated game ID, and no duplicated (date, home, away) except true doubleheaders (check `Doubleheader`/game number). |
| Score arithmetic | For ten random rows: total = home + away; winning margin = |home − away|; winner matches the scores. |
| Date range | All dates fall inside the season; the first and last dates match the official calendar. |
| Spot check | Compare at least ten random rows with a second source; report agreements and disagreements. |
| Plausibility | League mean score, home-win share and overtime share are within the league's [LEAGUE_PROFILES.md](../../LEAGUE_PROFILES.md) range (a large gap is a finding, not an error to hide). |

## 4. Record coverage

Update `COVERAGE_AND_BLANK_YEARS.md` (and the sport's README) with the season, the row count, the sources, the checks, and any seasons that are inactive, future or unexplained. A header-only folder is never "complete". If the new season changes a league's profile by more than one season of data, add a dated note in [LEAGUE_PROFILES.md](../../LEAGUE_PROFILES.md) and recompute the affected row by hand (ARCHIVE_USE_GUIDE recipe R1), keeping the old row in the note.

## 5. Publish

Commit only the CSV, source and coverage files you touched, by path. Large exports (`_canonical/*.csv`) are not committed. Push to `main` without force and re-read the remote HEAD.

## 6. Report

```text
READING RECEIPT: <as printed>
Target: <league · seasons> · reason:
Rows added / repaired: <n> · official count: <n> · gap:
Sources: <list with dates read>
Checks: header <…> · row count <…> · duplicates <…> · score arithmetic <…> · dates <…> · spot check <n agree / n disagree> · plausibility <…>
Coverage documents updated: <list>
Profile row affected: <yes/no; what changed>
Commit SHA / publication status:
```
