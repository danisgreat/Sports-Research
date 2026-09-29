# South Australian National Football League (SANFL) — Rules, Code & Analytical Framework

**Sport Discipline:** `State Level AFL`  
**Competition / League Subfolder:** `SANFL`  
**Governing Body:** South Australian National Football League Commission  
**Inaugural Era / Foundation:** 1877 (the oldest surviving Australian rules football league)  
**Status:** Canonical Reference Framework & Operating Protocol

---

## 1. Annual Rules & Competition Audit Protocol (Mandatory Reminder)

> [!IMPORTANT]
> ### 🚨 ANNUAL PRE-SEASON AUDIT REMINDER
> **Target Audit Date:** **`February 25 (Annually, one month prior to season kickoff)`**  
> **Standard Season Kickoff Window:** **`Late March / Early April`**  
>
> Exactly **one month prior to the commencement of every new season**, a full operational audit must be executed to determine whether the analytical parameters, league rules, or tournament structures require updating.

### Pre-Season Audit Checklist
Before issuing any forecast or recording historical results for an upcoming season:
1. **Rulebook Amendments:** Audit newly ratified rule changes by South Australian National Football League Commission (e.g. playing duration, clock rules, overtime procedures, substitution mechanics, penalty enforcement).
2. **Mini-Competitions & In-Season Tournaments:** Check for newly introduced mini-competitions, in-season cups, showcase rounds, or altered playoff brackets (e.g., ANZAC Round, Indigenous Round, Thomas Seymour Hill Cup.).
3. **Franchise & Conference Realignment:** Verify team expansion, relocation, division restructuring, or conference realignment.
4. **Roster & Player Availability Governance:** Inspect changes to active roster limits, injury replacement protocols, concussion management bylaws, and substitute eligibility rules.
5. **Officiating & Review Technology:** Review updates to video review systems, automated officiating (VAR, ARC, ABS, Hawk-Eye), and coaches' challenge allowances.
6. **Model Baseline Recalibration:** Recompute league-wide scoring baselines, margin standard deviations, key-number masses, and team priors.

---

## 2. Core Playing Rules & Scoring Framework

### Match Duration & Clock Governance
- **Regulation Playing Time:** 4 quarters x 20 minutes plus time-on.
- **Scoring Architecture:** Goal = 6 points, Behind = 1 point.
- **Overtime & Tie Resolution:** Regular season: Draws stand. Finals: 2 x 5-minute extra time periods.

---

## 3. Competition Structure & Tournament Framework

### Regular Season & Format
- **Format:** 10 clubs (8 traditional SANFL clubs plus Adelaide Crows and Port Adelaide Magpies reserves). 18-round home-and-away season.
- **Standings & Tie-Breaking Criteria:**
  - Standard standings calculated by championship points or winning percentage.
  - Head-to-head records, differential percentages (e.g. percentage in AFL, run differential in baseball, point differential in football).
- **Post-Season / Finals System:** SANFL Page-McIntyre Final Five system concluding with the SANFL Grand Final at Adelaide Oval.

---

## 4. Roster, Squad & Officiating Governance

### Squad Management & Substitutions
- **Squad Size & Active Roster:** Salary cap and player retention rules. Strict AFL alignment rules for AFL club reserves.
- **Player Eligibility & Availability:** Team sheets and inactive lists must be re-verified against official feeds within 60 minutes of scheduled start time.

### Officiating & Video Review Framework
- **Officiating Crew:** SANFL Umpires Department; boundary, field, and goal umpires.
- **Review Protocols:** Standardized review triggers for goal-line / boundary line disputes, scoring plays, turnovers, or challenged decisions.

---

## 5. Analytical Modeling & Settlement Protocol

### Mathematical Modeling Methodology
- **Distributional Architecture:** Strong home-ground advantage at traditional suburban grounds (Alberton, Unley, Prospect, Glenelg, Elizabeth).
- **Key Constraints:**
  - Model must anchor on official league population base rates.
  - Cushion lines (+k.5) and derivative handicap markets must be derived from the joint score/run distribution object, never estimated independently.
  - Weather vectors (wind, temperature, precipitation, altitude) must be mapped to ground orientation and venue geometry.

### Official Settlement Protocol
- **Data Lineage:** SANFL official match statistics / PlayHQ.
- **Official Game Threshold:** Matches must meet the governing body's minimum completion threshold to be deemed official for full-game settlements.
- **Postponements & Rescheduled Matches:** If a match is delayed, suspended, or moved, settlement follows official league completion rules; uncompleted events void under standard market rules.

---

## 6. Machine-Readable Configuration Schema (JSON)

```json
{
  "competition_name": "South Australian National Football League (SANFL)",
  "sport_category": "State Level AFL",
  "subfolder_directory": "SANFL",
  "governing_body": "South Australian National Football League Commission",
  "season_kickoff_window": "Late March / Early April",
  "annual_audit_reminder_date": "February 25 (Annually, one month prior to season kickoff)",
  "audit_interval_days_prior": 30,
  "match_duration": "4 quarters x 20 minutes plus time-on.",
  "scoring_rules": "Goal = 6 points, Behind = 1 point.",
  "overtime_protocol": "Regular season: Draws stand. Finals: 2 x 5-minute extra time periods.",
  "roster_rules": "Salary cap and player retention rules. Strict AFL alignment rules for AFL club reserves.",
  "officiating": "SANFL Umpires Department; boundary, field, and goal umpires.",
  "settlement_source": "SANFL official match statistics / PlayHQ."
}
```
