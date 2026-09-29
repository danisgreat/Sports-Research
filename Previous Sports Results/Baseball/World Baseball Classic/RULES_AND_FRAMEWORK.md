# World Baseball Classic (WBC) — Rules, Code & Analytical Framework

**Sport Discipline:** `Baseball`  
**Competition / League Subfolder:** `World Baseball Classic`  
**Governing Body:** World Baseball Softball Confederation (WBSC) & MLB / MLBPA  
**Inaugural Era / Foundation:** 2006  
**Status:** Canonical Reference Framework & Operating Protocol

---

## 1. Annual Rules & Competition Audit Protocol (Mandatory Reminder)

> [!IMPORTANT]
> ### 🚨 ANNUAL PRE-SEASON AUDIT REMINDER
> **Target Audit Date:** **`February 5 (Annually / one month prior to tournament launch)`**  
> **Standard Season Kickoff Window:** **`March (Quadrennial spring tournament)`**  
>
> Exactly **one month prior to the commencement of every new season**, a full operational audit must be executed to determine whether the analytical parameters, league rules, or tournament structures require updating.

### Pre-Season Audit Checklist
Before issuing any forecast or recording historical results for an upcoming season:
1. **Rulebook Amendments:** Audit newly ratified rule changes by World Baseball Softball Confederation (WBSC) & MLB / MLBPA (e.g. playing duration, clock rules, overtime procedures, substitution mechanics, penalty enforcement).
2. **Mini-Competitions & In-Season Tournaments:** Check for newly introduced mini-competitions, in-season cups, showcase rounds, or altered playoff brackets (e.g., Pool A, Pool B, Pool C, Pool D.).
3. **Franchise & Conference Realignment:** Verify team expansion, relocation, division restructuring, or conference realignment.
4. **Roster & Player Availability Governance:** Inspect changes to active roster limits, injury replacement protocols, concussion management bylaws, and substitute eligibility rules.
5. **Officiating & Review Technology:** Review updates to video review systems, automated officiating (VAR, ARC, ABS, Hawk-Eye), and coaches' challenge allowances.
6. **Model Baseline Recalibration:** Recompute league-wide scoring baselines, margin standard deviations, key-number masses, and team priors.

---

## 2. Core Playing Rules & Scoring Framework

### Match Duration & Clock Governance
- **Regulation Playing Time:** 9 innings.
- **Scoring Architecture:** Standard baseball scoring.
- **Overtime & Tie Resolution:** Tie-breaker rule: Runners on 1st and 2nd base with nobody out starting in the 10th inning.

---

## 3. Competition Structure & Tournament Framework

### Regular Season & Format
- **Format:** 20 national teams divided into 4 round-robin pools (Tokyo, Taichung/San Juan, Miami, Phoenix). Top 2 per pool advance to quarterfinals.
- **Standings & Tie-Breaking Criteria:**
  - Standard standings calculated by championship points or winning percentage.
  - Head-to-head records, differential percentages (e.g. percentage in AFL, run differential in baseball, point differential in football).
- **Post-Season / Finals System:** Single-elimination Championship Round held at a primary MLB venue (e.g. loanDepot park, Miami).

---

## 4. Roster, Squad & Officiating Governance

### Squad Management & Substitutions
- **Squad Size & Active Roster:** Strict pitch counts: First Round max 65 pitches; Quarterfinals max 80 pitches; Championship Round max 95 pitches. Mandatory rest days (4+ days for 50+ pitches, 1 day for 30+ pitches, consecutive days cap). Universal DH.
- **Player Eligibility & Availability:** Team sheets and inactive lists must be re-verified against official feeds within 60 minutes of scheduled start time.

### Officiating & Video Review Framework
- **Officiating Crew:** Mixed crew of MLB and international umpires.
- **Review Protocols:** Standardized review triggers for goal-line / boundary line disputes, scoring plays, turnovers, or challenged decisions.

---

## 5. Analytical Modeling & Settlement Protocol

### Mathematical Modeling Methodology
- **Distributional Architecture:** Pitch counts severely limit starting pitcher length; bullpen depth and relief deployment are decisive. Run differential matters in pool tiebreakers.
- **Key Constraints:**
  - Model must anchor on official league population base rates.
  - Cushion lines (+k.5) and derivative handicap markets must be derived from the joint score/run distribution object, never estimated independently.
  - Weather vectors (wind, temperature, precipitation, altitude) must be mapped to ground orientation and venue geometry.

### Official Settlement Protocol
- **Data Lineage:** MLB / World Baseball Classic official box scores.
- **Official Game Threshold:** Matches must meet the governing body's minimum completion threshold to be deemed official for full-game settlements.
- **Postponements & Rescheduled Matches:** If a match is delayed, suspended, or moved, settlement follows official league completion rules; uncompleted events void under standard market rules.

---

## 6. Machine-Readable Configuration Schema (JSON)

```json
{
  "competition_name": "World Baseball Classic (WBC)",
  "sport_category": "Baseball",
  "subfolder_directory": "World Baseball Classic",
  "governing_body": "World Baseball Softball Confederation (WBSC) & MLB / MLBPA",
  "season_kickoff_window": "March (Quadrennial spring tournament)",
  "annual_audit_reminder_date": "February 5 (Annually / one month prior to tournament launch)",
  "audit_interval_days_prior": 30,
  "match_duration": "9 innings.",
  "scoring_rules": "Standard baseball scoring.",
  "overtime_protocol": "Tie-breaker rule: Runners on 1st and 2nd base with nobody out starting in the 10th inning.",
  "roster_rules": "Strict pitch counts: First Round max 65 pitches; Quarterfinals max 80 pitches; Championship Round max 95 pitches. Mandatory rest days (4+ days for 50+ pitches, 1 day for 30+ pitches, consecutive days cap). Universal DH.",
  "officiating": "Mixed crew of MLB and international umpires.",
  "settlement_source": "MLB / World Baseball Classic official box scores."
}
```
