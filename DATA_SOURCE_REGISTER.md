# Data Source Register (H0 & Runtime Ingestion)

**Authority:** MDS-2026.10.01-v8.0 / CR-2026.10.06-NUMERICAL-1.
**Scope:** Authoritative register of all primary, secondary, and benchmark data sources for the numerical machine learning system across all eight supported sports.

---

## 1. Governance and Ingestion Principles

1. **Immutable Raw Snapshots**: All external ingestion must write raw responses verbatim to `runtime/data/raw/<sport>/<provider>/<YYYY-MM-DD>/` accompanied by SHA-256 hash, retrieval timestamp (UTC), request payload/endpoint, and source version.
2. **Point-in-Time Provenance**: Every feature derived from external sources must record `known_at` (the earliest time the underlying fact was publicly authoritative). A feature is strictly **missing** if `known_at > cutoff_at`.
3. **No Direct Python R-Dependencies**: R-based ingestion wrappers (`fitzRoy`, `nrlR`) execute as isolated batch CLI scripts outputting normalized Parquet tables. No `rpy2` bindings are permitted in core prediction runtimes.
4. **Market Blindness**: Model fitting, feature engineering, and core probability generation are strictly independent of betting odds or market sentiment. Market snapshot prices are quarantined to `runtime/data/market/` for post-calibration value analysis only.

---

## 2. Sport-by-Sport Source Register

### 2.1 Cricket
- **Primary Event & Ball-by-Ball Source**: Cricsheet (`cricsheet.org`)
  - **Format**: JSON (Primary authoritative format; experimental CSVs excluded for feature builds).
  - **Coverage**: 22,700+ matches across Tests, ODIs, T20Is, and major domestic T20 leagues.
  - **Regime Boundary**: Test matches back to 2006 for ball-by-ball; series-level records back to 1975.
  - **Known Limitations**: Excludes withheld Afghanistan/APL domestic fixtures. Toss, innings sequence, and playing conditions confirmed against official board scorecards.
- **Official Field-Owner Sources**: ICC Match Centre (`icc-cricket.com`), ESPNcricinfo match notes (for mandatory powerplay over-ranges and DLS stoppage timing).
- **Point-in-Time Ingestion**: Match lineups and toss decisions strictly recorded at official release (~30 mins prior to match start).

### 2.2 Basketball (NBA & International)
- **Primary Box Score & Event Source**: Official Competition Data & Approved Licensed APIs.
  - **NBA Official Stats**: Box scores 1946+, advanced tracking 1996+, play-by-play 1996+, lineup data 2008+.
  - **BALLDONTLIE API**: Fallback provider. Free tier rate-limited to 5 requests/min. Production pipelines require authenticated commercial endpoints.
- **FIBA / NBL / EuroLeague**: Official competition feeds (e.g. `nbl.com.au`, `euroleaguebasketball.net`).
- **Feature Regime**: Lineup-level possession and net-rating features valid only 2008+. Prior eras use team-level pace and efficiency baselines.

### 2.3 American Football (NFL & College)
- **Primary Play-by-Play Source**: `nflverse` / `nflreadr` / `nflfastR`
  - **Coverage**: Full play-by-play and drive-level data back to 1999.
  - **Features**: Expected Points (EP), Win Probability (WP), drive outcomes, completion probability over expected (CPOE), snap counts, and pressure metrics.
  - **Regime Controls**: Modern rules on defenseless receivers, overtime format, and kickoff placement partitioned by rule changes (2011, 2018, 2024).

### 2.4 Baseball (MLB & International)
- **Primary Pitch & Statcast Source**: `pybaseball` / MLB Baseball Savant / MLB Gameday API
  - **Pre-Statcast Regime (2008–2014)**: Pitch f/x pitch-level tracking (velocity, movement, pitch type). Launch speed and angle unavailable.
  - **Modern Statcast Regime (2015–Present)**: Exit velocity, launch angle, barrel rate, expected batting average (xBA), catcher framing, defensive run value.
  - **Critical Rule**: Never mix 2008–2014 tracking features with 2015+ Statcast features without explicit regime indicators.
- **KBO / NPB**: Official league scorecards (KBO: `koreabaseball.com`, NPB: `npb.jp`) with daily bullpen usage logs.

### 2.5 Australian Rules Football (AFL)
- **Primary Data Source**: `fitzRoy` (R-based ingestion pipeline)
  - **Underlying Feeds**: AFL Tables (1897–Present; match totals and basic stats), Footywire (2010–Present; detailed player stats, marks inside 50, contested possessions), Squiggle API (modern ratings).
  - **Ingestion Mode**: Isolated R script exporting to `runtime/data/canonical/afl/`.
  - **Regime Boundary**: Rich player-level features, clearances, and inside-50 marks strictly limited to 2010+. Match scores and team baselines back to 1990.

### 2.6 Rugby League (NRL)
- **Primary Data Source**: `nrlR` / Rugby League Project / Official NRL API
  - **Coverage**: Historical match records back to 1998.
  - **Features**: Set completions, ruck speed, run metres, post-contact metres, line breaks, six-again counts, sin-bin logs.
  - **Regime Boundary**: Six-again rule (2020+) creates a distinct high-pace, high-fatigue regime; models must partition pre-2020 and post-2020 scoring environments.

### 2.7 Soccer
- **Primary Open Event Source**: StatsBomb Open Data (`github.com/statsbomb/open-data`)
  - **Coverage**: Free high-density event and 360-degree freeze-frame tracking for selected tournament packages (World Cups, Euros, FA Women's Super League, selected historical seasons).
- **League Match & Results Archive**: Football-Data.co.uk (`football-data.co.uk`)
  - **Coverage**: 1993–Present across European top leagues. Match results, halftime scores, match shots, shots on target, fouls, corners, cards.
- **Quarantine Note**: Football-Data odds columns are immediately stripped and moved to market quarantine.

### 2.8 Ice Hockey (NHL - Eighth Sport)
- **Primary Event & Shot Source**: MoneyPuck (`moneypuck.com`) & Official NHL API
  - **Coverage**: 2007–08 season to present.
  - **Features**: Shot-by-shot data with 124 attributes, expected goals (xG), shot distance/angle, rebound flags, manpower state (5v5, 5v4, 4v5, empty net).
  - **Known Limitations**: Blocked shots are excluded from MoneyPuck raw tables; shot-attempt and possession baselines derived from NHL play-by-play.

### 2.9 Tennis
- **Primary Match & Point-by-Point Source**: Tennis Abstract & Jeff Sackmann Match Charting Project (`github.com/JeffSackmann`)
  - **Coverage**: ATP, WTA, and Grand Slam matches 1968–Present; point-by-point charted matches 2011–Present.
  - **Features**: Opponent-adjusted serve/return points won, first-serve %, break points converted/saved, surface splits (Clay, Hard, Grass), Elo ratings.
  - **Regime Boundary**: Surface is a hard regime boundary; best-of-3 vs best-of-5 endpoint rules strictly separated.

---

## 3. Source Quality & Validation Matrix

| Sport | Provider | Format | Primary / Fallback | Update Latency | Point-in-Time Safe? |
|---|---|---|---|---|---|
| Cricket | Cricsheet | JSON | Primary | Post-match (~2h) | Yes (explicit innings/ball order) |
| Cricket | ESPNcricinfo | HTML/JSON | Fallback | Live | Yes (timestamped match notes) |
| Basketball | NBA Official / Balldontlie | JSON | Primary | 15m post-game | Yes (official box scores) |
| NFL | nflfastR | Parquet | Primary | Live / Post-game | Yes (timestamped play index) |
| Baseball | pybaseball / Savant | CSV/JSON | Primary | Live / Daily | Yes (pitch sequence index) |
| AFL | fitzRoy (AFL Tables/Footywire) | Parquet | Primary | Daily | Yes (regime-checked: 2010+) |
| NRL | nrlR / RLP | Parquet | Primary | Daily | Yes (regime-checked: 2020+) |
| Soccer | StatsBomb / Football-Data | JSON/CSV | Primary | Weekly / Daily | Yes (halftime/fulltime splits) |
| NHL | MoneyPuck / NHL API | CSV/JSON | Primary | Daily | Yes (shot timestamps / period) |
| Tennis | Tennis Abstract / Sackmann MCP | CSV | Primary | Daily / Post-tournament | Yes (point/match sequence) |

---

## 4. Maintenance and Deprecation Protocol

1. Any changes to third-party endpoints or schema breakages must be registered as a dated revision in this document.
2. In the event of source deprecation, fallback providers must be audited for feature equivalence before switching.
3. Automated regression tests in `runtime/tests/` verify that all parser pipelines conform to the schemas defined herein.

