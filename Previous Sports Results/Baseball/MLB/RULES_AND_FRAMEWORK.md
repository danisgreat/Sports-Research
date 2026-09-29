# Major League Baseball (MLB) — Rules, Code & Analytical Framework

**Sport Discipline:** `Baseball`  
**Competition / League Subfolder:** `MLB`  
**Governing Body:** Office of the Commissioner of Baseball  
**Inaugural Era / Foundation:** 1876 (National League) & 1901 (American League); unified 2000  
**Status:** Canonical Reference Framework & Operating Protocol

---

## 1. Annual Rules & Competition Audit Protocol (Mandatory Reminder)

> [!IMPORTANT]
> ### 🚨 ANNUAL PRE-SEASON AUDIT REMINDER
> **Target Audit Date:** **`February 25 (Annually, exactly one month prior to Opening Day / Spring Training launch)`**  
> **Standard Season Kickoff Window:** **`Late March / Early April (Opening Day)`**  
>
> Exactly **one month prior to the commencement of every new season**, a full operational audit must be executed to determine whether the analytical parameters, league rules, or tournament structures require updating.

### Pre-Season Audit Checklist
Before issuing any forecast or recording historical results for an upcoming season:
1. **Rulebook Amendments:** Audit newly ratified rule changes by Office of the Commissioner of Baseball (e.g. playing duration, clock rules, overtime procedures, substitution mechanics, penalty enforcement).
2. **Mini-Competitions & In-Season Tournaments:** Check for newly introduced mini-competitions, in-season cups, showcase rounds, or altered playoff brackets (e.g., MLB All-Star Game, Home Run Derby, MLB Little League Classic, Field of Dreams Game, MLB London Series, Mexico City Series.).
3. **Franchise & Conference Realignment:** Verify team expansion, relocation, division restructuring, or conference realignment.
4. **Roster & Player Availability Governance:** Inspect changes to active roster limits, injury replacement protocols, concussion management bylaws, and substitute eligibility rules.
5. **Officiating & Review Technology:** Review updates to video review systems, automated officiating (VAR, ARC, ABS, Hawk-Eye), and coaches' challenge allowances.
6. **Model Baseline Recalibration:** Recompute league-wide scoring baselines, margin standard deviations, key-number masses, and team priors.

---

## 2. Core Playing Rules & Scoring Framework

### Match Duration & Clock Governance
- **Regulation Playing Time:** 9 innings (plus extra innings if tied).
- **Scoring Architecture:** Runs scored by runners advancing safely around all four bases to home plate.
- **Overtime & Tie Resolution:** Extra Innings: Automatic runner placed on second base to begin every half-inning from the 10th inning onward in the regular season (Ghost Runner rule; not used in postseason).

---

## 3. Competition Structure & Tournament Framework

### Regular Season & Format
- **Format:** 30 clubs (15 American League, 15 National League) playing 162 regular season games each (balanced schedule across all 29 opponents).
- **Standings & Tie-Breaking Criteria:**
  - Standard standings calculated by championship points or winning percentage.
  - Head-to-head records, differential percentages (e.g. percentage in AFL, run differential in baseball, point differential in football).
- **Post-Season / Finals System:** 12-team postseason: 6 teams per league (3 division champions seeded 1-3, 3 wild cards seeded 4-6). Best-of-3 Wild Card Series, Best-of-5 Division Series (ALDS/NLDS), Best-of-7 League Championship Series (ALCS/NLCS), Best-of-7 World Series.

---

## 4. Roster, Squad & Officiating Governance

### Squad Management & Substitutions
- **Squad Size & Active Roster:** 26-man active roster (expanding to 28 in September). Maximum 13 pitchers allowed on active roster. Pitch clock: 15 seconds with bases empty, 18 seconds with runners on base. Disengagement limit: 2 pickoff attempts/step-offs per plate appearance. Universal Designated Hitter (DH).
- **Player Eligibility & Availability:** Team sheets and inactive lists must be re-verified against official feeds within 60 minutes of scheduled start time.

### Officiating & Video Review Framework
- **Officiating Crew:** 4 on-field umpires (expanded to 6 in postseason). Replay review center in Chelsea, New York. Manager challenge protocol: 1 challenge per game (retained if call overturned); umpires can initiate reviews in 8th inning and later.
- **Review Protocols:** Standardized review triggers for goal-line / boundary line disputes, scoring plays, turnovers, or challenged decisions.

---

## 5. Analytical Modeling & Settlement Protocol

### Mathematical Modeling Methodology
- **Distributional Architecture:** Negative Binomial run distribution with park factors, weather (temperature, humidity, barometric pressure, wind vector), starter projection (IP, K%, BB%, GB%), and bullpen leverage index. Run line baseline: home -1.5 / away +1.5 with key number 1 (~28-30% of games decided by 1 run).
- **Key Constraints:**
  - Model must anchor on official league population base rates.
  - Cushion lines (+k.5) and derivative handicap markets must be derived from the joint score/run distribution object, never estimated independently.
  - Weather vectors (wind, temperature, precipitation, altitude) must be mapped to ground orientation and venue geometry.

### Official Settlement Protocol
- **Data Lineage:** Official game criteria: 5 full innings (or 4.5 if home team leads) required for moneyline settlement. Totals and run lines require 9 full innings (or 8.5 if home team leads) unless shortened game reaches official complete status under specific market rules.
- **Official Game Threshold:** Matches must meet the governing body's minimum completion threshold to be deemed official for full-game settlements.
- **Postponements & Rescheduled Matches:** If a match is delayed, suspended, or moved, settlement follows official league completion rules; uncompleted events void under standard market rules.

---

## 6. Machine-Readable Configuration Schema (JSON)

```json
{
  "competition_name": "Major League Baseball (MLB)",
  "sport_category": "Baseball",
  "subfolder_directory": "MLB",
  "governing_body": "Office of the Commissioner of Baseball",
  "season_kickoff_window": "Late March / Early April (Opening Day)",
  "annual_audit_reminder_date": "February 25 (Annually, exactly one month prior to Opening Day / Spring Training launch)",
  "audit_interval_days_prior": 30,
  "match_duration": "9 innings (plus extra innings if tied).",
  "scoring_rules": "Runs scored by runners advancing safely around all four bases to home plate.",
  "overtime_protocol": "Extra Innings: Automatic runner placed on second base to begin every half-inning from the 10th inning onward in the regular season (Ghost Runner rule; not used in postseason).",
  "roster_rules": "26-man active roster (expanding to 28 in September). Maximum 13 pitchers allowed on active roster. Pitch clock: 15 seconds with bases empty, 18 seconds with runners on base. Disengagement limit: 2 pickoff attempts/step-offs per plate appearance. Universal Designated Hitter (DH).",
  "officiating": "4 on-field umpires (expanded to 6 in postseason). Replay review center in Chelsea, New York. Manager challenge protocol: 1 challenge per game (retained if call overturned); umpires can initiate reviews in 8th inning and later.",
  "settlement_source": "Official game criteria: 5 full innings (or 4.5 if home team leads) required for moneyline settlement. Totals and run lines require 9 full innings (or 8.5 if home team leads) unless shortened game reaches official complete status under specific market rules."
}
```
