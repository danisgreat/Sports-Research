# WAFL Women's (WAFLW) — Rules, Code & Analytical Framework

**Sport Discipline:** `State Level AFL`  
**Competition / League Subfolder:** `WAFLW`  
**Governing Body:** WAFC  
**Inaugural Era / Foundation:** 2019  
**Status:** Canonical Reference Framework & Operating Protocol

---

## 1. Annual Rules & Competition Audit Protocol (Mandatory Reminder)

> [!IMPORTANT]
> ### 🚨 ANNUAL PRE-SEASON AUDIT REMINDER
> **Target Audit Date:** **`February 10 (Annually, one month prior to kickoff)`**  
> **Standard Season Kickoff Window:** **`March`**  
>
> Exactly **one month prior to the commencement of every new season**, a full operational audit must be executed to determine whether the analytical parameters, league rules, or tournament structures require updating.

### Pre-Season Audit Checklist
Before issuing any forecast or recording historical results for an upcoming season:
1. **Rulebook Amendments:** Audit newly ratified rule changes by WAFC (e.g. playing duration, clock rules, overtime procedures, substitution mechanics, penalty enforcement).
2. **Mini-Competitions & In-Season Tournaments:** Check for newly introduced mini-competitions, in-season cups, showcase rounds, or altered playoff brackets (e.g., None.).
3. **Franchise & Conference Realignment:** Verify team expansion, relocation, division restructuring, or conference realignment.
4. **Roster & Player Availability Governance:** Inspect changes to active roster limits, injury replacement protocols, concussion management bylaws, and substitute eligibility rules.
5. **Officiating & Review Technology:** Review updates to video review systems, automated officiating (VAR, ARC, ABS, Hawk-Eye), and coaches' challenge allowances.
6. **Model Baseline Recalibration:** Recompute league-wide scoring baselines, margin standard deviations, key-number masses, and team priors.

---

## 2. Core Playing Rules & Scoring Framework

### Match Duration & Clock Governance
- **Regulation Playing Time:** 4 quarters x 15 minutes plus time-on.
- **Scoring Architecture:** Goal = 6 points, Behind = 1 point.
- **Overtime & Tie Resolution:** Finals extra time: 2 x 3-minute periods.

---

## 3. Competition Structure & Tournament Framework

### Regular Season & Format
- **Format:** 8 clubs playing 14 rounds followed by top-4 finals.
- **Standings & Tie-Breaking Criteria:**
  - Standard standings calculated by championship points or winning percentage.
  - Head-to-head records, differential percentages (e.g. percentage in AFL, run differential in baseball, point differential in football).
- **Post-Season / Finals System:** Top 4 finals series.

---

## 4. Roster, Squad & Officiating Governance

### Squad Management & Substitutions
- **Squad Size & Active Roster:** Western Australian development pathway.
- **Player Eligibility & Availability:** Team sheets and inactive lists must be re-verified against official feeds within 60 minutes of scheduled start time.

### Officiating & Video Review Framework
- **Officiating Crew:** WAFC panel.
- **Review Protocols:** Standardized review triggers for goal-line / boundary line disputes, scoring plays, turnovers, or challenged decisions.

---

## 5. Analytical Modeling & Settlement Protocol

### Mathematical Modeling Methodology
- **Distributional Architecture:** Fast surface baseline, suburban Perth conditions.
- **Key Constraints:**
  - Model must anchor on official league population base rates.
  - Cushion lines (+k.5) and derivative handicap markets must be derived from the joint score/run distribution object, never estimated independently.
  - Weather vectors (wind, temperature, precipitation, altitude) must be mapped to ground orientation and venue geometry.

### Official Settlement Protocol
- **Data Lineage:** WAFL.com.au official match centre.
- **Official Game Threshold:** Matches must meet the governing body's minimum completion threshold to be deemed official for full-game settlements.
- **Postponements & Rescheduled Matches:** If a match is delayed, suspended, or moved, settlement follows official league completion rules; uncompleted events void under standard market rules.

---

## 6. Machine-Readable Configuration Schema (JSON)

```json
{
  "competition_name": "WAFL Women's (WAFLW)",
  "sport_category": "State Level AFL",
  "subfolder_directory": "WAFLW",
  "governing_body": "WAFC",
  "season_kickoff_window": "March",
  "annual_audit_reminder_date": "February 10 (Annually, one month prior to kickoff)",
  "audit_interval_days_prior": 30,
  "match_duration": "4 quarters x 15 minutes plus time-on.",
  "scoring_rules": "Goal = 6 points, Behind = 1 point.",
  "overtime_protocol": "Finals extra time: 2 x 3-minute periods.",
  "roster_rules": "Western Australian development pathway.",
  "officiating": "WAFC panel.",
  "settlement_source": "WAFL.com.au official match centre."
}
```
