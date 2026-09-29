# Chinese Professional Baseball League (CPBL) — Rules, Code & Analytical Framework

**Sport Discipline:** `Baseball`  
**Competition / League Subfolder:** `CPBL`  
**Governing Body:** CPBL Commission (Taiwan)  
**Inaugural Era / Foundation:** 1989  
**Status:** Canonical Reference Framework & Operating Protocol

---

## 1. Annual Rules & Competition Audit Protocol (Mandatory Reminder)

> [!IMPORTANT]
> ### 🚨 ANNUAL PRE-SEASON AUDIT REMINDER
> **Target Audit Date:** **`February 28 (Annually, one month prior to opening day)`**  
> **Standard Season Kickoff Window:** **`Late March / Early April`**  
>
> Exactly **one month prior to the commencement of every new season**, a full operational audit must be executed to determine whether the analytical parameters, league rules, or tournament structures require updating.

### Pre-Season Audit Checklist
Before issuing any forecast or recording historical results for an upcoming season:
1. **Rulebook Amendments:** Audit newly ratified rule changes by CPBL Commission (Taiwan) (e.g. playing duration, clock rules, overtime procedures, substitution mechanics, penalty enforcement).
2. **Mini-Competitions & In-Season Tournaments:** Check for newly introduced mini-competitions, in-season cups, showcase rounds, or altered playoff brackets (e.g., CPBL All-Star Game.).
3. **Franchise & Conference Realignment:** Verify team expansion, relocation, division restructuring, or conference realignment.
4. **Roster & Player Availability Governance:** Inspect changes to active roster limits, injury replacement protocols, concussion management bylaws, and substitute eligibility rules.
5. **Officiating & Review Technology:** Review updates to video review systems, automated officiating (VAR, ARC, ABS, Hawk-Eye), and coaches' challenge allowances.
6. **Model Baseline Recalibration:** Recompute league-wide scoring baselines, margin standard deviations, key-number masses, and team priors.

---

## 2. Core Playing Rules & Scoring Framework

### Match Duration & Clock Governance
- **Regulation Playing Time:** 9 innings.
- **Scoring Architecture:** Standard baseball scoring.
- **Overtime & Tie Resolution:** 12-inning tie limit in regular season.

---

## 3. Competition Structure & Tournament Framework

### Regular Season & Format
- **Format:** 6 clubs playing a split-season format (60 games Spring, 60 games Autumn; 120 total games per team).
- **Standings & Tie-Breaking Criteria:**
  - Standard standings calculated by championship points or winning percentage.
  - Head-to-head records, differential percentages (e.g. percentage in AFL, run differential in baseball, point differential in football).
- **Post-Season / Finals System:** Playoff Series leading to the Taiwan Series (best-of-7 championship).

---

## 4. Roster, Squad & Officiating Governance

### Squad Management & Substitutions
- **Squad Size & Active Roster:** Foreign player quota (max 4 on roster, 3 active). Universal DH.
- **Player Eligibility & Availability:** Team sheets and inactive lists must be re-verified against official feeds within 60 minutes of scheduled start time.

### Officiating & Video Review Framework
- **Officiating Crew:** CPBL umpiring crew with video review challenge system.
- **Review Protocols:** Standardized review triggers for goal-line / boundary line disputes, scoring plays, turnovers, or challenged decisions.

---

## 5. Analytical Modeling & Settlement Protocol

### Mathematical Modeling Methodology
- **Distributional Architecture:** Warm subtropical climate, high offensive variance, foreign starter reliance.
- **Key Constraints:**
  - Model must anchor on official league population base rates.
  - Cushion lines (+k.5) and derivative handicap markets must be derived from the joint score/run distribution object, never estimated independently.
  - Weather vectors (wind, temperature, precipitation, altitude) must be mapped to ground orientation and venue geometry.

### Official Settlement Protocol
- **Data Lineage:** CPBL.com.tw official match records.
- **Official Game Threshold:** Matches must meet the governing body's minimum completion threshold to be deemed official for full-game settlements.
- **Postponements & Rescheduled Matches:** If a match is delayed, suspended, or moved, settlement follows official league completion rules; uncompleted events void under standard market rules.

---

## 6. Machine-Readable Configuration Schema (JSON)

```json
{
  "competition_name": "Chinese Professional Baseball League (CPBL)",
  "sport_category": "Baseball",
  "subfolder_directory": "CPBL",
  "governing_body": "CPBL Commission (Taiwan)",
  "season_kickoff_window": "Late March / Early April",
  "annual_audit_reminder_date": "February 28 (Annually, one month prior to opening day)",
  "audit_interval_days_prior": 30,
  "match_duration": "9 innings.",
  "scoring_rules": "Standard baseball scoring.",
  "overtime_protocol": "12-inning tie limit in regular season.",
  "roster_rules": "Foreign player quota (max 4 on roster, 3 active). Universal DH.",
  "officiating": "CPBL umpiring crew with video review challenge system.",
  "settlement_source": "CPBL.com.tw official match records."
}
```
