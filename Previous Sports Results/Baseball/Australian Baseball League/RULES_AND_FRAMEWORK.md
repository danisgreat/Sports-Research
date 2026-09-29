# Australian Baseball League (ABL) — Rules, Code & Analytical Framework

**Sport Discipline:** `Baseball`  
**Competition / League Subfolder:** `Australian Baseball League`  
**Governing Body:** Baseball Australia  
**Inaugural Era / Foundation:** 2010 (modern era; historic roots from 1989)  
**Status:** Canonical Reference Framework & Operating Protocol

---

## 1. Annual Rules & Competition Audit Protocol (Mandatory Reminder)

> [!IMPORTANT]
> ### 🚨 ANNUAL PRE-SEASON AUDIT REMINDER
> **Target Audit Date:** **`October 15 (Annually, exactly one month prior to season kickoff)`**  
> **Standard Season Kickoff Window:** **`Mid-November (Southern Hemisphere Summer)`**  
>
> Exactly **one month prior to the commencement of every new season**, a full operational audit must be executed to determine whether the analytical parameters, league rules, or tournament structures require updating.

### Pre-Season Audit Checklist
Before issuing any forecast or recording historical results for an upcoming season:
1. **Rulebook Amendments:** Audit newly ratified rule changes by Baseball Australia (e.g. playing duration, clock rules, overtime procedures, substitution mechanics, penalty enforcement).
2. **Mini-Competitions & In-Season Tournaments:** Check for newly introduced mini-competitions, in-season cups, showcase rounds, or altered playoff brackets (e.g., None.).
3. **Franchise & Conference Realignment:** Verify team expansion, relocation, division restructuring, or conference realignment.
4. **Roster & Player Availability Governance:** Inspect changes to active roster limits, injury replacement protocols, concussion management bylaws, and substitute eligibility rules.
5. **Officiating & Review Technology:** Review updates to video review systems, automated officiating (VAR, ARC, ABS, Hawk-Eye), and coaches' challenge allowances.
6. **Model Baseline Recalibration:** Recompute league-wide scoring baselines, margin standard deviations, key-number masses, and team priors.

---

## 2. Core Playing Rules & Scoring Framework

### Match Duration & Clock Governance
- **Regulation Playing Time:** 9 innings (often 7 innings in doubleheaders).
- **Scoring Architecture:** Standard baseball scoring.
- **Overtime & Tie Resolution:** Extra innings: WBSC tie-breaker runner on 2nd base from 10th inning.

---

## 3. Competition Structure & Tournament Framework

### Regular Season & Format
- **Format:** 6 franchises (Adelaide Giants, Brisbane Bandits, Canberra Cavalry, Melbourne Aces, Perth Heat, Sydney Blue Sox). 40-game season across 10 round weekends.
- **Standings & Tie-Breaking Criteria:**
  - Standard standings calculated by championship points or winning percentage.
  - Head-to-head records, differential percentages (e.g. percentage in AFL, run differential in baseball, point differential in football).
- **Post-Season / Finals System:** Top 4 playoffs concluding in best-of-3 Championship Series for the Claxton Shield.

---

## 4. Roster, Squad & Officiating Governance

### Squad Management & Substitutions
- **Squad Size & Active Roster:** Player point system balancing Australian players, foreign imports, and MLB affiliated loan prospects.
- **Player Eligibility & Availability:** Team sheets and inactive lists must be re-verified against official feeds within 60 minutes of scheduled start time.

### Officiating & Video Review Framework
- **Officiating Crew:** Baseball Australia certified umpires.
- **Review Protocols:** Standardized review triggers for goal-line / boundary line disputes, scoring plays, turnovers, or challenged decisions.

---

## 5. Analytical Modeling & Settlement Protocol

### Mathematical Modeling Methodology
- **Distributional Architecture:** Summer conditions, high travel fatigue across trans-continental flights (Perth to Brisbane/Sydney), roster volatility due to MLB winter release dates.
- **Key Constraints:**
  - Model must anchor on official league population base rates.
  - Cushion lines (+k.5) and derivative handicap markets must be derived from the joint score/run distribution object, never estimated independently.
  - Weather vectors (wind, temperature, precipitation, altitude) must be mapped to ground orientation and venue geometry.

### Official Settlement Protocol
- **Data Lineage:** TheABL.com.au official stats.
- **Official Game Threshold:** Matches must meet the governing body's minimum completion threshold to be deemed official for full-game settlements.
- **Postponements & Rescheduled Matches:** If a match is delayed, suspended, or moved, settlement follows official league completion rules; uncompleted events void under standard market rules.

---

## 6. Machine-Readable Configuration Schema (JSON)

```json
{
  "competition_name": "Australian Baseball League (ABL)",
  "sport_category": "Baseball",
  "subfolder_directory": "Australian Baseball League",
  "governing_body": "Baseball Australia",
  "season_kickoff_window": "Mid-November (Southern Hemisphere Summer)",
  "annual_audit_reminder_date": "October 15 (Annually, exactly one month prior to season kickoff)",
  "audit_interval_days_prior": 30,
  "match_duration": "9 innings (often 7 innings in doubleheaders).",
  "scoring_rules": "Standard baseball scoring.",
  "overtime_protocol": "Extra innings: WBSC tie-breaker runner on 2nd base from 10th inning.",
  "roster_rules": "Player point system balancing Australian players, foreign imports, and MLB affiliated loan prospects.",
  "officiating": "Baseball Australia certified umpires.",
  "settlement_source": "TheABL.com.au official stats."
}
```
