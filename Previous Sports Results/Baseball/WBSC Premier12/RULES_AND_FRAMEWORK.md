# WBSC Premier12 — Rules, Code & Analytical Framework

**Sport Discipline:** `Baseball`  
**Competition / League Subfolder:** `WBSC Premier12`  
**Governing Body:** World Baseball Softball Confederation (WBSC)  
**Inaugural Era / Foundation:** 2015  
**Status:** Canonical Reference Framework & Operating Protocol

---

## 1. Annual Rules & Competition Audit Protocol (Mandatory Reminder)

> [!IMPORTANT]
> ### 🚨 ANNUAL PRE-SEASON AUDIT REMINDER
> **Target Audit Date:** **`October 10 (One month prior to tournament kickoff)`**  
> **Standard Season Kickoff Window:** **`November (Every 4 years)`**  
>
> Exactly **one month prior to the commencement of every new season**, a full operational audit must be executed to determine whether the analytical parameters, league rules, or tournament structures require updating.

### Pre-Season Audit Checklist
Before issuing any forecast or recording historical results for an upcoming season:
1. **Rulebook Amendments:** Audit newly ratified rule changes by World Baseball Softball Confederation (WBSC) (e.g. playing duration, clock rules, overtime procedures, substitution mechanics, penalty enforcement).
2. **Mini-Competitions & In-Season Tournaments:** Check for newly introduced mini-competitions, in-season cups, showcase rounds, or altered playoff brackets (e.g., Opening Round Groups.).
3. **Franchise & Conference Realignment:** Verify team expansion, relocation, division restructuring, or conference realignment.
4. **Roster & Player Availability Governance:** Inspect changes to active roster limits, injury replacement protocols, concussion management bylaws, and substitute eligibility rules.
5. **Officiating & Review Technology:** Review updates to video review systems, automated officiating (VAR, ARC, ABS, Hawk-Eye), and coaches' challenge allowances.
6. **Model Baseline Recalibration:** Recompute league-wide scoring baselines, margin standard deviations, key-number masses, and team priors.

---

## 2. Core Playing Rules & Scoring Framework

### Match Duration & Clock Governance
- **Regulation Playing Time:** 9 innings.
- **Scoring Architecture:** Standard baseball scoring.
- **Overtime & Tie Resolution:** WBSC tie-breaker from the 10th inning (runners on 1st and 2nd base, no outs).

---

## 3. Competition Structure & Tournament Framework

### Regular Season & Format
- **Format:** Top 12 nations in the WBSC World Rankings. Group stage followed by Super Round and Medal Games at Tokyo Dome.
- **Standings & Tie-Breaking Criteria:**
  - Standard standings calculated by championship points or winning percentage.
  - Head-to-head records, differential percentages (e.g. percentage in AFL, run differential in baseball, point differential in football).
- **Post-Season / Finals System:** Super Round top 2 play in Gold Medal Game; 3rd and 4th play in Bronze Medal Game.

---

## 4. Roster, Squad & Officiating Governance

### Squad Management & Substitutions
- **Squad Size & Active Roster:** 28-man national rosters. Active MLB 40-man roster players generally restricted, giving dominance to NPB, KBO, CPBL, and minor league stars.
- **Player Eligibility & Availability:** Team sheets and inactive lists must be re-verified against official feeds within 60 minutes of scheduled start time.

### Officiating & Video Review Framework
- **Officiating Crew:** WBSC international umpires.
- **Review Protocols:** Standardized review triggers for goal-line / boundary line disputes, scoring plays, turnovers, or challenged decisions.

---

## 5. Analytical Modeling & Settlement Protocol

### Mathematical Modeling Methodology
- **Distributional Architecture:** Dominance of Asian professional stars (NPB/KBO) with tournament-style starting rotations.
- **Key Constraints:**
  - Model must anchor on official league population base rates.
  - Cushion lines (+k.5) and derivative handicap markets must be derived from the joint score/run distribution object, never estimated independently.
  - Weather vectors (wind, temperature, precipitation, altitude) must be mapped to ground orientation and venue geometry.

### Official Settlement Protocol
- **Data Lineage:** WBSC official match sheets.
- **Official Game Threshold:** Matches must meet the governing body's minimum completion threshold to be deemed official for full-game settlements.
- **Postponements & Rescheduled Matches:** If a match is delayed, suspended, or moved, settlement follows official league completion rules; uncompleted events void under standard market rules.

---

## 6. Machine-Readable Configuration Schema (JSON)

```json
{
  "competition_name": "WBSC Premier12",
  "sport_category": "Baseball",
  "subfolder_directory": "WBSC Premier12",
  "governing_body": "World Baseball Softball Confederation (WBSC)",
  "season_kickoff_window": "November (Every 4 years)",
  "annual_audit_reminder_date": "October 10 (One month prior to tournament kickoff)",
  "audit_interval_days_prior": 30,
  "match_duration": "9 innings.",
  "scoring_rules": "Standard baseball scoring.",
  "overtime_protocol": "WBSC tie-breaker from the 10th inning (runners on 1st and 2nd base, no outs).",
  "roster_rules": "28-man national rosters. Active MLB 40-man roster players generally restricted, giving dominance to NPB, KBO, CPBL, and minor league stars.",
  "officiating": "WBSC international umpires.",
  "settlement_source": "WBSC official match sheets."
}
```
