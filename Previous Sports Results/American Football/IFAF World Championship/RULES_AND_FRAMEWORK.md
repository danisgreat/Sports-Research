# IFAF World Championship of American Football — Rules, Code & Analytical Framework

**Sport Discipline:** `American Football`  
**Competition / League Subfolder:** `IFAF World Championship`  
**Governing Body:** International Federation of American Football (IFAF)  
**Inaugural Era / Foundation:** 1999 (Palermo, Italy)  
**Status:** Canonical Reference Framework & Operating Protocol

---

## 1. Annual Rules & Competition Audit Protocol (Mandatory Reminder)

> [!IMPORTANT]
> ### 🚨 ANNUAL PRE-SEASON AUDIT REMINDER
> **Target Audit Date:** **`May 1 (One month prior to tournament summer launch)`**  
> **Standard Season Kickoff Window:** **`Quadrennial tournament (summer months)`**  
>
> Exactly **one month prior to the commencement of every new season**, a full operational audit must be executed to determine whether the analytical parameters, league rules, or tournament structures require updating.

### Pre-Season Audit Checklist
Before issuing any forecast or recording historical results for an upcoming season:
1. **Rulebook Amendments:** Audit newly ratified rule changes by International Federation of American Football (IFAF) (e.g. playing duration, clock rules, overtime procedures, substitution mechanics, penalty enforcement).
2. **Mini-Competitions & In-Season Tournaments:** Check for newly introduced mini-competitions, in-season cups, showcase rounds, or altered playoff brackets (e.g., None.).
3. **Franchise & Conference Realignment:** Verify team expansion, relocation, division restructuring, or conference realignment.
4. **Roster & Player Availability Governance:** Inspect changes to active roster limits, injury replacement protocols, concussion management bylaws, and substitute eligibility rules.
5. **Officiating & Review Technology:** Review updates to video review systems, automated officiating (VAR, ARC, ABS, Hawk-Eye), and coaches' challenge allowances.
6. **Model Baseline Recalibration:** Recompute league-wide scoring baselines, margin standard deviations, key-number masses, and team priors.

---

## 2. Core Playing Rules & Scoring Framework

### Match Duration & Clock Governance
- **Regulation Playing Time:** 4 quarters x 12 minutes (IFAF international rules).
- **Scoring Architecture:** Standard gridiron scoring: TD = 6, FG = 3, Safety = 2, PAT = 1, 2-pt Conv = 2.
- **Overtime & Tie Resolution:** NCAA-style tie-breaker from the 25-yard line.

---

## 3. Competition Structure & Tournament Framework

### Regular Season & Format
- **Format:** National teams qualifying through continental confederations (IFAF Americas, IFAF Europe, IFAF Asia, IFAF Oceania, IFAF Africa).
- **Standings & Tie-Breaking Criteria:**
  - Standard standings calculated by championship points or winning percentage.
  - Head-to-head records, differential percentages (e.g. percentage in AFL, run differential in baseball, point differential in football).
- **Post-Season / Finals System:** Group pool play followed by medal rounds (Gold, Silver, Bronze matches).

---

## 4. Roster, Squad & Officiating Governance

### Squad Management & Substitutions
- **Squad Size & Active Roster:** 45-man national rosters; national eligibility and passport rules strictly enforced.
- **Player Eligibility & Availability:** Team sheets and inactive lists must be re-verified against official feeds within 60 minutes of scheduled start time.

### Officiating & Video Review Framework
- **Officiating Crew:** IFAF international certified officiating crews.
- **Review Protocols:** Standardized review triggers for goal-line / boundary line disputes, scoring plays, turnovers, or challenged decisions.

---

## 5. Analytical Modeling & Settlement Protocol

### Mathematical Modeling Methodology
- **Distributional Architecture:** High scoring variance across international tiers; USA and Japan historically dominant.
- **Key Constraints:**
  - Model must anchor on official league population base rates.
  - Cushion lines (+k.5) and derivative handicap markets must be derived from the joint score/run distribution object, never estimated independently.
  - Weather vectors (wind, temperature, precipitation, altitude) must be mapped to ground orientation and venue geometry.

### Official Settlement Protocol
- **Data Lineage:** IFAF official match sheets.
- **Official Game Threshold:** Matches must meet the governing body's minimum completion threshold to be deemed official for full-game settlements.
- **Postponements & Rescheduled Matches:** If a match is delayed, suspended, or moved, settlement follows official league completion rules; uncompleted events void under standard market rules.

---

## 6. Machine-Readable Configuration Schema (JSON)

```json
{
  "competition_name": "IFAF World Championship of American Football",
  "sport_category": "American Football",
  "subfolder_directory": "IFAF World Championship",
  "governing_body": "International Federation of American Football (IFAF)",
  "season_kickoff_window": "Quadrennial tournament (summer months)",
  "annual_audit_reminder_date": "May 1 (One month prior to tournament summer launch)",
  "audit_interval_days_prior": 30,
  "match_duration": "4 quarters x 12 minutes (IFAF international rules).",
  "scoring_rules": "Standard gridiron scoring: TD = 6, FG = 3, Safety = 2, PAT = 1, 2-pt Conv = 2.",
  "overtime_protocol": "NCAA-style tie-breaker from the 25-yard line.",
  "roster_rules": "45-man national rosters; national eligibility and passport rules strictly enforced.",
  "officiating": "IFAF international certified officiating crews.",
  "settlement_source": "IFAF official match sheets."
}
```
