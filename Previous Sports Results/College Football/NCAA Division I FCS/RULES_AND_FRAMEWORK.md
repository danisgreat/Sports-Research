# NCAA Division I Football Championship Subdivision (FCS) — Rules, Code & Analytical Framework

**Sport Discipline:** `College Football`  
**Competition / League Subfolder:** `NCAA Division I FCS`  
**Governing Body:** NCAA FCS Committee  
**Inaugural Era / Foundation:** 1978 (formerly Division I-AA)  
**Status:** Canonical Reference Framework & Operating Protocol

---

## 1. Annual Rules & Competition Audit Protocol (Mandatory Reminder)

> [!IMPORTANT]
> ### 🚨 ANNUAL PRE-SEASON AUDIT REMINDER
> **Target Audit Date:** **`July 25 (Annually, one month prior to opening weekend)`**  
> **Standard Season Kickoff Window:** **`Late August / September`**  
>
> Exactly **one month prior to the commencement of every new season**, a full operational audit must be executed to determine whether the analytical parameters, league rules, or tournament structures require updating.

### Pre-Season Audit Checklist
Before issuing any forecast or recording historical results for an upcoming season:
1. **Rulebook Amendments:** Audit newly ratified rule changes by NCAA FCS Committee (e.g. playing duration, clock rules, overtime procedures, substitution mechanics, penalty enforcement).
2. **Mini-Competitions & In-Season Tournaments:** Check for newly introduced mini-competitions, in-season cups, showcase rounds, or altered playoff brackets (e.g., None.).
3. **Franchise & Conference Realignment:** Verify team expansion, relocation, division restructuring, or conference realignment.
4. **Roster & Player Availability Governance:** Inspect changes to active roster limits, injury replacement protocols, concussion management bylaws, and substitute eligibility rules.
5. **Officiating & Review Technology:** Review updates to video review systems, automated officiating (VAR, ARC, ABS, Hawk-Eye), and coaches' challenge allowances.
6. **Model Baseline Recalibration:** Recompute league-wide scoring baselines, margin standard deviations, key-number masses, and team priors.

---

## 2. Core Playing Rules & Scoring Framework

### Match Duration & Clock Governance
- **Regulation Playing Time:** 4 quarters x 15 minutes.
- **Scoring Architecture:** Standard NCAA rules.
- **Overtime & Tie Resolution:** NCAA overtime rules.

---

## 3. Competition Structure & Tournament Framework

### Regular Season & Format
- **Format:** 128 programs across 13 conferences. 24-team single-elimination championship playoff (11 automatic conference bids, 13 at-large).
- **Standings & Tie-Breaking Criteria:**
  - Standard standings calculated by championship points or winning percentage.
  - Head-to-head records, differential percentages (e.g. percentage in AFL, run differential in baseball, point differential in football).
- **Post-Season / Finals System:** NCAA Division I Football Championship Game held in Frisco, Texas at Toyota Stadium.

---

## 4. Roster, Squad & Officiating Governance

### Squad Management & Substitutions
- **Squad Size & Active Roster:** 63-scholarship equivalency limit.
- **Player Eligibility & Availability:** Team sheets and inactive lists must be re-verified against official feeds within 60 minutes of scheduled start time.

### Officiating & Video Review Framework
- **Officiating Crew:** NCAA FCS certified officiating crews.
- **Review Protocols:** Standardized review triggers for goal-line / boundary line disputes, scoring plays, turnovers, or challenged decisions.

---

## 5. Analytical Modeling & Settlement Protocol

### Mathematical Modeling Methodology
- **Distributional Architecture:** Cold-weather regional playoff games (Dakota schools, Montana schools).
- **Key Constraints:**
  - Model must anchor on official league population base rates.
  - Cushion lines (+k.5) and derivative handicap markets must be derived from the joint score/run distribution object, never estimated independently.
  - Weather vectors (wind, temperature, precipitation, altitude) must be mapped to ground orientation and venue geometry.

### Official Settlement Protocol
- **Data Lineage:** NCAA official match statistics.
- **Official Game Threshold:** Matches must meet the governing body's minimum completion threshold to be deemed official for full-game settlements.
- **Postponements & Rescheduled Matches:** If a match is delayed, suspended, or moved, settlement follows official league completion rules; uncompleted events void under standard market rules.

---

## 6. Machine-Readable Configuration Schema (JSON)

```json
{
  "competition_name": "NCAA Division I Football Championship Subdivision (FCS)",
  "sport_category": "College Football",
  "subfolder_directory": "NCAA Division I FCS",
  "governing_body": "NCAA FCS Committee",
  "season_kickoff_window": "Late August / September",
  "annual_audit_reminder_date": "July 25 (Annually, one month prior to opening weekend)",
  "audit_interval_days_prior": 30,
  "match_duration": "4 quarters x 15 minutes.",
  "scoring_rules": "Standard NCAA rules.",
  "overtime_protocol": "NCAA overtime rules.",
  "roster_rules": "63-scholarship equivalency limit.",
  "officiating": "NCAA FCS certified officiating crews.",
  "settlement_source": "NCAA official match statistics."
}
```
