# Bulk results history: provenance and rules (BULK-v1, 11 November 2026)

Built by `python -m ml bulk-history` (code in `ml/bulk_history.py`) through the repository's one checked fetcher (`ml.source_access`, the SCRIPT reader: every one of the eight AI agent names must be permitted by the site's robots rules). Raw downloads stay in a cache outside the repository; only the sporting columns below are committed, with each body's URL, retrieval time and SHA-256 in the folder's `RECEIPTS.csv`. No odds, lines or prices are read: none of these datasets carries them.

**Captured today means known today.** These rows were captured on 10–11 November 2026. They are history for future cards, studies and parameter rows. They are never point-in-time evidence that any fact was known before a past card.

## soccer/MATCHES.csv

- **Source:** openfootball/football.json, read file by file from `raw.githubusercontent.com` (robots: no rules file). Public domain ("dedicated to the public domain. Use as you please with no restrictions whatsoever").
- **Scope:** 32 competitions, season folders 2021-22 to 2026-27 and calendar years 2025–2026, where the dataset holds them; 25,143 matches with a full-time score. Matches without a score (unplayed, or not yet entered) are counted and left out. Half-time scores are present for about 93% of matches.
- **Transformation:** each match's date, round, team1 (home) and team2 (away), half-time and full-time scores are copied as written. A score written as a bare pair is read as the full-time score. Team names are openfootball's own and are not merged across competitions.
- **Limits:** coverage of the current season lags the real fixtures (the Premier League runs to 20 September 2026 on 11 November 2026); some leagues hold one season only; no corners, cards, line-ups or extra-time detail; neutral venues are not marked. Not a field-owner record: `FIELD_OWNER_ADMISSION_UNVERIFIED`.

## cricket/INNINGS.csv and cricket/PHASE_RATES.csv

- **Source:** Cricsheet ball-by-ball CSV archives (`cricsheet.org/downloads/<name>_csv2.zip`; robots allows them for every reader), under the Open Data Commons Attribution licence. Attribution: data from Cricsheet (cricsheet.org).
- **Scope:** matches from 1 January 2019 in men's and women's T20 internationals, men's and women's ODIs, IPL, BBL, WBBL, PSL, CPL, T20 Blast, SA20, ILT20, BPL, LPL, MLC and WPL: 19,899 innings. The Hundred and multi-day formats are excluded (the owner's cricket request is a 20- or 50-over first innings).
- **INNINGS:** one row per first or second innings: runs (off the bat plus extras), wickets (retired hurt and retired not out are not wickets), legal balls (wides and no-balls are not), runs and wickets at the end of overs 5, 6 and 10 (an innings that ended earlier keeps its final score there, as the settlement rule does), whether the match used a reduced-overs method, toss winner and decision.
- **PHASE_RATES:** per competition, year, innings and over: counts of legal balls by runs off the bat (0, 1, 2, 3, 4, 6, other), wickets, wides, no-balls and extras runs. Byes and leg-byes on a legal ball count as a dot for the bat; their runs are in `extras_runs`.
- **Limits:** a scorecard error in Cricsheet is carried as is; venue names are Cricsheet's; no pitch or weather detail.

## What is deliberately not here

- **MLB:** the MLB Stats API passes the robots check, but its copyright notice permits only "individual, non-commercial, non-bulk use", so no bulk MLB history is downloaded. Baseball checks use the learning store's verified finals.
- **Tennis:** Jeff Sackmann's ATP and WTA repositories were withdrawn (HTTP 404 since early November 2026); mirrors of withdrawn data are not used. TennisMyLife's ATP files allow non-commercial research but not redistribution of the raw database, so only tour-level aggregates derived from them are committed (`research/competition_parameters/TENNIS_TOUR_RATES.csv`). There is no permitted bulk WTA source.
- **Soccer corners:** the main open corners source (football-data.co.uk) refuses AI agents; its mirrors are not used. Corners stay priced per game from a permitted provider (RULES_SOCCER), with no kit row.
- **Rugby union:** no permitted bulk results source was found in this round; the kit marks union NOT_COVERED.
