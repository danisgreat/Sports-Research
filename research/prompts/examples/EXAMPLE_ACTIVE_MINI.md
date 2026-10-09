<!-- MINI-LOG-FORMAT: mini-log-4 -->
# Prediction Mini Running Log — P-900 onward

> **FORMAT EXAMPLE ONLY.** Fictional league, teams, numbers and sources. Not a forecast and never imported. Real minis start at the repository's next canonical ID.

## A. Authority snapshot

| Field | Value |
|---|---|
| Repository | https://github.com/danisgreat/Sports-Research |
| Branch | main |
| GitHub HEAD SHA | `0000000000000000000000000000000000000000` |
| Method | MDS-2026.10.09-v9.0 |
| Control revision | CR-2026.10.09-R5 |
| Scoring version | SCV-2026.10.09-v5 |
| Active Combined Log | `prediction logs/PREDICTION_LOG_COMBINED_7.md` |
| Highest committed repository P-ID | P-899 |
| Repository next-ID snapshot | P-900 |
| Highest local working P-ID before creation | NONE |
| First working P-ID for this mini | P-900 |
| Reading receipt | CURRENT_STATE, METHOD, CURRENT_RULES, SELECTION_RULES, CARD_AND_LOG_TEMPLATES and the EXAMPLE_ACTIVE_MINI structure read in full at the HEAD SHA above, 2026-10-10T07:55:00+11:00 (example) |
| Mini opened | 2026-10-10T08:00:00+11:00 |
| Mode | LOCAL_MINI_STAGING |

SPORTS_ONLY / MARKET_BLIND · PERFORMANCE_ELIGIBILITY: NOT_CERTIFIED · CANONICAL_IMPORT_STATUS: PENDING

## B. Local ID rules

- Creating this mini consumes no P-ID. One unique sporting event = one working P-ID.
- A working ID advances only after a complete new card is written and verified locally.
- Addenda, corrections, duplicates and aliases keep the original ID and consume none.
- Working IDs never change once issued; GitHub being behind does not invalidate them.
- Canonical import (prompt 4) is separate; the import step retains these IDs or stops on a collision.

## C. Active carryover

None.

# NEW LOCAL EVENT CARDS

<!-- BEGIN CARD P-900 -->
## Card · P-900 · ICE HOCKEY / EXAMPLE LEAGUE · Northfield Owls @ Southport Bears · 2026-10-10

> FORMAT EXAMPLE — fictional teams and numbers; not a forecast.

- **Working ID:** `P-900 — LOCAL_WORKING_ID — PENDING_CANONICAL_IMPORT`
- **Event key:** `EXAMPLE:2026-27:EX-0001:2026-10-10`
- **Native event ID:** `EX-0001`
- **Sport:** `Ice hockey`
- **League:** `EXAMPLE LEAGUE`
- **Tracking alias:** `LOCAL-20261010-P-900-EX-NOR-SOU`
- **Analysis status:** `UNCALIBRATED_ANALYST_SCENARIO`
- **Timing state:** `PREGAME`
- **Research completed:** `2026-10-10T09:15:00+11:00`
- **Scheduled start:** `2026-10-10T11:00:00+11:00`
- **Endpoint:** `Full game including OT/SO; a shootout adds one goal to the winner`
- **Distribution object:** `hockey_poisson_ot_v1` — independent Poisson regulation goals (λ 3.10 home, 2.70 away) with OT/SO resolution (home 52%, one goal added); one score grid prices every row below.
- **Regime flags:** `NONE`
- **Retirement rule:** `N/A`
- **Listed-pitcher rule:** `N/A`
- **Abandonment rule:** `FRAMEWORK_DEFAULT: an abandoned game is VOID unless the league publishes a result`
- **Settlement fields:** `Final score including OT/SO (provider: league game page)`
- **Capture due:** `2026-10-11T11:00:00+11:00`
- **Rules read:** `RULES_ICE_HOCKEY §0 §3; PROBABILITY_TOOLKIT §2.3; SELECTION_RULES §2 §3 §5; SOURCES §3.9 (example); BASE_RATES_REGISTER §7.2`
- **Archive check:** `ARCHIVE_UNAVAILABLE: fictional league, format example only (a real NHL card would name Previous Sports Results/Ice Hockey/NHL/2025/2025_games.csv, rows read, date range and recipes R1, R2, R5, R8)`
- **Evidence quotes:** `League game page (example) @ 2026-10-10T09:10:00+11:00 — "Scheduled · 11:00 AM · Southport Arena"; Team announcement (example) @ 2026-10-10T08:41:00+11:00 — "Starting in goal tonight: Alvarez (NOR), Brandt (SOU)"`

### Decision block

**Distribution:** `hockey_poisson_ot_v1` — λ_home 3.10, λ_away 2.70; tied regulation (16.8%) to OT/SO, home 52%, one goal added. Ladder priced from this grid: totals 4.5–8.5, handicaps ±0.5 to ±2.5, moneyline, team totals (appendix A5).

| Rank | Role | Tag | Proposition | p_card | Probability status | Evidence | Failure route |
|---|---|---|---|---|---|---|---|
| 1 | PICK | ANALYST_DERIVED (replaces supplied Under 6.5) | Total goals Under 7.5 — full game incl. OT/SO | 77.1% | FROM_DISTRIBUTION:hockey_poisson_ot_v1 | Combined λ 5.8; both starters confirmed | A high-event game or empty-net goals push the total to 8+ |
| 2 | PICK | SUPPLIED | Northfield Owls +1.5 — full game incl. OT/SO | 68.2% | FROM_DISTRIBUTION:hockey_poisson_ot_v1 | Close chance quality; OT losses cover | Southport wins by 2+, usually via a late empty-net goal |
| 3 | INFORMATIONAL | SUPPLIED | Southport Bears moneyline — full game incl. OT/SO | 56.8% | FROM_DISTRIBUTION:hockey_poisson_ot_v1 | Small home edge | Northfield finishing variance |
| 4 | INFORMATIONAL | ANALYST_DERIVED (replaces supplied Over 6.5) | Total goals Over 5.5 — full game incl. OT/SO | 52.2% | FROM_DISTRIBUTION:hockey_poisson_ot_v1 | Combined λ 5.8 sits at the line | Both goalies hold the game to 5 or fewer |

**P(Rank 1 and Rank 2 both lose):** 9.3%
**Rank 1 − Rank 2 gap:** 8.9 points
**Rank-1 gate:** PASS — p_card 77.1%; best non-complementary alternative 68.2%; margin 8.9 points
**Adjustment dependence:** NONE
**Supplied rows not selected:** Over 6.5 41.1%; Under 6.5 58.9% (same distribution).
**Potential winner:** Southport Bears — 56.8% (full game including OT/SO)

### Appendix

#### A1. Identity, timing and state

Native event `EX-0001` on the league schedule; fixture state `Scheduled` at research completion (source update 09:10 +11:00). No in-game information was used.

#### A2. Supplied contracts (reference only, Rule P4)

1. Southport Bears moneyline (full game)
2. Northfield Owls +1.5 (full game)
3. Total goals Over 6.5 (full game)
4. Total goals Under 6.5 (full game)

#### A3. Evidence summary

Confirmed starting goalies for both teams (team announcements 08:40 +11:00); both teams on two days' rest; no new injuries. Five-on-five chance quality is close, with a small home edge.

#### A4. Event distribution

Regulation goals are independent Poisson with λ_home 3.10 and λ_away 2.70 (analyst scenario from season scoring and goalie quality; not a fitted model). A tied regulation (16.8% of mass) goes to OT/SO, and the home side wins it 52% of the time with one goal added.

#### A5. Priced ladder (excerpt)

| Proposition | p_card |
|---|---:|
| Total goals Under 7.5 | 77.1% |
| Northfield Owls +1.5 | 68.2% |
| Southport Bears moneyline | 56.8% |
| Total goals Over 5.5 | 52.2% |

#### A6. Adjustments

**Adjustments:** NONE

#### A7. Family checks

Full-game endpoint: OT/SO is resolved, not left as a draw. Empty-net tail: named as the Rank-2 failure route. Goalies: both confirmed.

#### A8. Sources

1. League schedule and game page (example) — identity, state, start time.
2. Team announcements (example) — starting goalies.

#### A9. Integrity receipt

`SPORTS_ONLY_MARKET_BLIND: PASS` · `OBSERVED_IN_GAME_OUTCOME_USED: NO` · `SETTLEMENT: NOT_PERFORMED`
<!-- END CARD P-900 -->

<!-- BEGIN ADDENDUM P-900 -->
### Addendum · P-900 · 2026-10-10T10:20:00+11:00

Late news before the start: a Northfield third-pair defender is a late scratch (team update 10:12 +11:00). Re-pricing with λ_away 2.68 moves Rank 1 to 77.4% and Rank 2 to 68.0%; the ranking is unchanged. The original card above stays unchanged and is what gets graded.
<!-- END ADDENDUM P-900 -->

<!-- BEGIN CARD P-901 -->
## Card · P-901 · BASKETBALL / EXAMPLE LEAGUE · Westbay Gulls vs Eastvale Pines · 2026-10-10

> FORMAT EXAMPLE — fictional teams and numbers; not a forecast.

- **Working ID:** `P-901 — LOCAL_WORKING_ID — PENDING_CANONICAL_IMPORT`
- **Event key:** `EXAMPLE:2026-27:EX-0002:2026-10-10`
- **Native event ID:** `EX-0002`
- **Sport:** `Basketball`
- **League:** `EXAMPLE LEAGUE`
- **Tracking alias:** `LOCAL-20261010-P-901-EX-WES-EAS`
- **Analysis status:** `UNCALIBRATED_ANALYST_SCENARIO`
- **Timing state:** `PREGAME`
- **Research completed:** `2026-10-10T18:40:00+11:00`
- **Scheduled start:** `2026-10-10T19:30:00+11:00`
- **Endpoint:** `Full game including overtime`
- **Distribution object:** `basketball_pace_normal_v1` — total ~ Normal(161.0, 18.0), home margin ~ Normal(+4.0, 12.0), overtime folded into the full-game grid; one grid prices every row below.
- **Regime flags:** `EARLY_SEASON`
- **Retirement rule:** `N/A`
- **Listed-pitcher rule:** `N/A`
- **Abandonment rule:** `FRAMEWORK_DEFAULT: an abandoned game is VOID unless the league publishes a result`
- **Settlement fields:** `Final score including overtime (provider: league game page)`
- **Capture due:** `2026-10-11T12:00:00+11:00`
- **Rules read:** `RULES_BASKETBALL §3; PROBABILITY_TOOLKIT §1.2 §1.3; SELECTION_RULES §2 §3 §6; SOURCES §3.2 (example); BASE_RATES_REGISTER regime table (EARLY_SEASON)`
- **Archive check:** `ARCHIVE_UNAVAILABLE: fictional league, format example only (a real card would name the league row in LEAGUE_PROFILES.md and the Previous Sports Results file, rows read and recipes R1, R2, R5)`
- **Evidence quotes:** `League game page (example) @ 2026-10-10T18:35:00+11:00 — "Scheduled · 7:30 PM · Westbay Arena"`

### Decision block

**Distribution:** `basketball_pace_normal_v1` — total ~ Normal(161.0, 18.0), margin ~ Normal(+4.0, 12.0), full game incl. OT. Ladder priced from this grid: totals 148.5–173.5, handicaps ±0.5 to ±14.5, moneyline (appendix A5).

| Rank | Role | Tag | Proposition | p_card | Probability status | Evidence | Failure route |
|---|---|---|---|---|---|---|---|
| 1 | PICK | ANALYST_DERIVED (replaces supplied Over 160.5) | Combined total Over 152.5 — full game incl. OT | 68.2% | FROM_DISTRIBUTION:basketball_pace_normal_v1 | Both teams' pace above league mean | A slow, foul-light game finishes at 152 or fewer |
| 2 | PICK | ANALYST_DERIVED (replaces supplied Under 160.5) | Combined total Under 168.5 — full game incl. OT | 66.2% | FROM_DISTRIBUTION:basketball_pace_normal_v1 | Both defences rate above average | Hot three-point shooting or overtime lifts the total to 169+ |
| 3 | INFORMATIONAL | ANALYST_DERIVED (replaces supplied Westbay −6.5) | Westbay Gulls moneyline — full game incl. OT | 63.1% | FROM_DISTRIBUTION:basketball_pace_normal_v1 | Home margin centre +4 | Eastvale's perimeter run |
| 4 | INFORMATIONAL | SUPPLIED | Eastvale Pines +6.5 — full game incl. OT | 58.3% | FROM_DISTRIBUTION:basketball_pace_normal_v1 | Margin SD 12 around +4 | Westbay wins by 7+ |

**P(Rank 1 and Rank 2 both lose):** 0.0% (a total cannot be both 152 or fewer and 169 or more)
**Rank 1 − Rank 2 gap:** 2.0 points
**Rank-1 gate:** RANK1_UNSTABLE — p_card 68.2%; best non-complementary alternative 66.2%; margin 2.0 points
**Adjustment dependence:** NONE
**Supplied rows not selected:** Westbay −6.5 41.7%; Over 160.5 51.1%; Under 160.5 48.9% (same distribution).
**Potential winner:** Westbay Gulls — 63.1% (full game including OT)

### Appendix

#### A1. Identity, timing and state

Native event `EX-0002`; state `Scheduled` at research completion. Westbay is at home.

#### A2. Supplied contracts (reference only, Rule P4)

1. Westbay Gulls −6.5
2. Eastvale Pines +6.5
3. Combined total Over 160.5
4. Combined total Under 160.5

#### A4. Event distribution

Possessions × efficiency scenario: total ~ Normal(161.0, 18.0); home margin ~ Normal(+4.0, 12.0), treated as independent of the total. Overtime is folded into the full-game distribution. Uncalibrated analyst scenario.

#### A5. Priced ladder (excerpt)

| Proposition | p_card |
|---|---:|
| Combined total Over 152.5 | 68.2% |
| Combined total Under 168.5 | 66.2% |
| Westbay Gulls moneyline | 63.1% |
| Eastvale Pines +6.5 | 58.3% |

#### A6. Adjustments

**Adjustments:**

| Name | Target | Size | SD units | Prior basis |
|---|---|---|---|---|
| early_season_pace | total | +1.5 | 0.08 | archive_estimate |

#### A7. Family checks

Totals use a pace × efficiency centre, not a raw points average. Overtime is resolved. Rank 1 and Rank 2 are a bracketing pair, so their joint failure is zero by construction. The gate fails because the lead over Rank 2 is only 2.0 points: the card is scored in the RANK1_UNSTABLE cohort.

#### A8. Sources

1. League game page (example).

#### A9. Integrity receipt

`SPORTS_ONLY_MARKET_BLIND: PASS` · `OBSERVED_IN_GAME_OUTCOME_USED: NO` · `SETTLEMENT: NOT_PERFORMED`
<!-- END CARD P-901 -->

# RUNNING FOOTER

<!-- BEGIN FOOTER -->
| Field | Value |
|---|---|
| Highest local working P-ID actually used | P-901 |
| Next local working P-ID | P-902 |
| Repository next-ID snapshot when mini opened | P-900 |
| Active carryovers | 0 |
| New event cards | 2 |
| Local mini status | ACTIVE |
| Canonical import | PENDING |
| GitHub writes performed | NO |
<!-- END FOOTER -->
