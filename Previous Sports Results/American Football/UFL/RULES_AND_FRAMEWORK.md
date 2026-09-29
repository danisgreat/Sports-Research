# United Football League (UFL) — Rules, Code & Analytical Framework

**Sport Discipline:** `American Football`  
**Competition / League Subfolder:** `UFL`  
**Governing Body:** UFL Board of Directors / Football Operations  
**Inaugural Era / Foundation:** 2024 (merger of modern USFL and XFL)  
**Status:** Canonical Reference Framework & Operating Protocol

---

## 1. Annual Rules & Competition Audit Protocol (Mandatory Reminder)

> [!IMPORTANT]
> ### 🚨 ANNUAL PRE-SEASON AUDIT REMINDER
> **Target Audit Date:** **`February 28 (Annually, one month prior to opening weekend)`**  
> **Standard Season Kickoff Window:** **`Late March / Early April`**  
>
> Exactly **one month prior to the commencement of every new season**, a full operational audit must be executed to determine whether the analytical parameters, league rules, or tournament structures require updating.

### Pre-Season Audit Checklist
Before issuing any forecast or recording historical results for an upcoming season:
1. **Rulebook Amendments:** Audit newly ratified rule changes by UFL Board of Directors / Football Operations (e.g. playing duration, clock rules, overtime procedures, substitution mechanics, penalty enforcement).
2. **Mini-Competitions & In-Season Tournaments:** Check for newly introduced mini-competitions, in-season cups, showcase rounds, or altered playoff brackets (e.g., None.).
3. **Franchise & Conference Realignment:** Verify team expansion, relocation, division restructuring, or conference realignment.
4. **Roster & Player Availability Governance:** Inspect changes to active roster limits, injury replacement protocols, concussion management bylaws, and substitute eligibility rules.
5. **Officiating & Review Technology:** Review updates to video review systems, automated officiating (VAR, ARC, ABS, Hawk-Eye), and coaches' challenge allowances.
6. **Model Baseline Recalibration:** Recompute league-wide scoring baselines, margin standard deviations, key-number masses, and team priors.

---

## 2. Core Playing Rules & Scoring Framework

### Match Duration & Clock Governance
- **Regulation Playing Time:** 4 quarters x 15 minutes. Running clock on incompletions outside 2 minutes of halves.
- **Scoring Architecture:** Touchdown = 6 points. No kicked PATs: Tiered scrimmage conversions (1 point from 2-yd line, 2 points from 5-yd line, 3 points from 10-yd line). Field Goal = 3 points. Safety = 2 points.
- **Overtime & Tie Resolution:** College/shootout hybrid: Best-of-3 single-play attempts from the 5-yard line for 2 points each. Sudden death if tied after 3 rounds.

---

## 3. Competition Structure & Tournament Framework

### Regular Season & Format
- **Format:** 8 franchises split into USFL Conference (Birmingham Stallions, Houston Roughnecks, Memphis Showboats, Michigan Panthers) and XFL Conference (Arlington Renegades, DC Defenders, San Antonio Brahmas, St. Louis Battlehawks). 10-week season.
- **Standings & Tie-Breaking Criteria:**
  - Standard standings calculated by championship points or winning percentage.
  - Head-to-head records, differential percentages (e.g. percentage in AFL, run differential in baseball, point differential in football).
- **Post-Season / Finals System:** Conference Championship games followed by UFL Championship Game.

---

## 4. Roster, Squad & Officiating Governance

### Squad Management & Substitutions
- **Squad Size & Active Roster:** 50-man rosters (42 active, 8 inactive on game day). 4th-and-12 alternative onside kick option in fourth quarter.
- **Player Eligibility & Availability:** Team sheets and inactive lists must be re-verified against official feeds within 60 minutes of scheduled start time.

### Officiating & Video Review Framework
- **Officiating Crew:** Transparent replay review with live broadcast audio from head of officiating (Dean Blandino / Mike Pereira framework).
- **Review Protocols:** Standardized review triggers for goal-line / boundary line disputes, scoring plays, turnovers, or challenged decisions.

---

## 5. Analytical Modeling & Settlement Protocol

### Mathematical Modeling Methodology
- **Distributional Architecture:** Conversion points distribution differs radically from NFL due to tiered conversion system. Key number 3 remains, but 7 is replaced by 6, 8, and 9.
- **Key Constraints:**
  - Model must anchor on official league population base rates.
  - Cushion lines (+k.5) and derivative handicap markets must be derived from the joint score/run distribution object, never estimated independently.
  - Weather vectors (wind, temperature, precipitation, altitude) must be mapped to ground orientation and venue geometry.

### Official Settlement Protocol
- **Data Lineage:** TheUFL.com official stats and Fox/ESPN verified box scores.
- **Official Game Threshold:** Matches must meet the governing body's minimum completion threshold to be deemed official for full-game settlements.
- **Postponements & Rescheduled Matches:** If a match is delayed, suspended, or moved, settlement follows official league completion rules; uncompleted events void under standard market rules.

---

## 6. Machine-Readable Configuration Schema (JSON)

```json
{
  "competition_name": "United Football League (UFL)",
  "sport_category": "American Football",
  "subfolder_directory": "UFL",
  "governing_body": "UFL Board of Directors / Football Operations",
  "season_kickoff_window": "Late March / Early April",
  "annual_audit_reminder_date": "February 28 (Annually, one month prior to opening weekend)",
  "audit_interval_days_prior": 30,
  "match_duration": "4 quarters x 15 minutes. Running clock on incompletions outside 2 minutes of halves.",
  "scoring_rules": "Touchdown = 6 points. No kicked PATs: Tiered scrimmage conversions (1 point from 2-yd line, 2 points from 5-yd line, 3 points from 10-yd line). Field Goal = 3 points. Safety = 2 points.",
  "overtime_protocol": "College/shootout hybrid: Best-of-3 single-play attempts from the 5-yard line for 2 points each. Sudden death if tied after 3 rounds.",
  "roster_rules": "50-man rosters (42 active, 8 inactive on game day). 4th-and-12 alternative onside kick option in fourth quarter.",
  "officiating": "Transparent replay review with live broadcast audio from head of officiating (Dean Blandino / Mike Pereira framework).",
  "settlement_source": "TheUFL.com official stats and Fox/ESPN verified box scores."
}
```
