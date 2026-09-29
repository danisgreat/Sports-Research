# Serie del Caribe (Caribbean Series) & Winter Leagues — Rules, Code & Analytical Framework

**Sport Discipline:** `Baseball`  
**Competition / League Subfolder:** `Caribbean Series and Winter Leagues`  
**Governing Body:** Confederación de Béisbol Profesional del Caribe (CBPC)  
**Inaugural Era / Foundation:** 1949  
**Status:** Canonical Reference Framework & Operating Protocol

---

## 1. Annual Rules & Competition Audit Protocol (Mandatory Reminder)

> [!IMPORTANT]
> ### 🚨 ANNUAL PRE-SEASON AUDIT REMINDER
> **Target Audit Date:** **`January 2 (Annually, one month prior to Serie del Caribe / Winter League Finals)`**  
> **Standard Season Kickoff Window:** **`Winter leagues run October-January; Serie del Caribe takes place first week of February`**  
>
> Exactly **one month prior to the commencement of every new season**, a full operational audit must be executed to determine whether the analytical parameters, league rules, or tournament structures require updating.

### Pre-Season Audit Checklist
Before issuing any forecast or recording historical results for an upcoming season:
1. **Rulebook Amendments:** Audit newly ratified rule changes by Confederación de Béisbol Profesional del Caribe (CBPC) (e.g. playing duration, clock rules, overtime procedures, substitution mechanics, penalty enforcement).
2. **Mini-Competitions & In-Season Tournaments:** Check for newly introduced mini-competitions, in-season cups, showcase rounds, or altered playoff brackets (e.g., Dominican LIDOM Finals, Venezuelan LVBP Finals, Mexican LMP Finals, Puerto Rican LBPRC Finals.).
3. **Franchise & Conference Realignment:** Verify team expansion, relocation, division restructuring, or conference realignment.
4. **Roster & Player Availability Governance:** Inspect changes to active roster limits, injury replacement protocols, concussion management bylaws, and substitute eligibility rules.
5. **Officiating & Review Technology:** Review updates to video review systems, automated officiating (VAR, ARC, ABS, Hawk-Eye), and coaches' challenge allowances.
6. **Model Baseline Recalibration:** Recompute league-wide scoring baselines, margin standard deviations, key-number masses, and team priors.

---

## 2. Core Playing Rules & Scoring Framework

### Match Duration & Clock Governance
- **Regulation Playing Time:** 9 innings.
- **Scoring Architecture:** Standard baseball scoring.
- **Overtime & Tie Resolution:** Extra innings: Automatic runner on second base from 10th inning.

---

## 3. Competition Structure & Tournament Framework

### Regular Season & Format
- **Format:** Tournament of winter champions from Dominican Republic (LIDOM), Puerto Rico (LBPRC), Mexico (LMP), Venezuela (LVBP), plus guest nations (e.g. Panama, Curacao, Colombia).
- **Standings & Tie-Breaking Criteria:**
  - Standard standings calculated by championship points or winning percentage.
  - Head-to-head records, differential percentages (e.g. percentage in AFL, run differential in baseball, point differential in football).
- **Post-Season / Finals System:** Round-robin group play followed by semi-finals and single-game championship final.

---

## 4. Roster, Squad & Officiating Governance

### Squad Management & Substitutions
- **Squad Size & Active Roster:** Championship teams reinforce rosters by drafting top players from eliminated domestic winter league teams.
- **Player Eligibility & Availability:** Team sheets and inactive lists must be re-verified against official feeds within 60 minutes of scheduled start time.

### Officiating & Video Review Framework
- **Officiating Crew:** CBPC international umpiring crew.
- **Review Protocols:** Standardized review triggers for goal-line / boundary line disputes, scoring plays, turnovers, or challenged decisions.

---

## 5. Analytical Modeling & Settlement Protocol

### Mathematical Modeling Methodology
- **Distributional Architecture:** High-intensity short tournament; elite MLB and AAA talent bolstered by domestic winter veterans.
- **Key Constraints:**
  - Model must anchor on official league population base rates.
  - Cushion lines (+k.5) and derivative handicap markets must be derived from the joint score/run distribution object, never estimated independently.
  - Weather vectors (wind, temperature, precipitation, altitude) must be mapped to ground orientation and venue geometry.

### Official Settlement Protocol
- **Data Lineage:** CBPC official box scores.
- **Official Game Threshold:** Matches must meet the governing body's minimum completion threshold to be deemed official for full-game settlements.
- **Postponements & Rescheduled Matches:** If a match is delayed, suspended, or moved, settlement follows official league completion rules; uncompleted events void under standard market rules.

---

## 6. Machine-Readable Configuration Schema (JSON)

```json
{
  "competition_name": "Serie del Caribe (Caribbean Series) & Winter Leagues",
  "sport_category": "Baseball",
  "subfolder_directory": "Caribbean Series and Winter Leagues",
  "governing_body": "Confederación de Béisbol Profesional del Caribe (CBPC)",
  "season_kickoff_window": "Winter leagues run October-January; Serie del Caribe takes place first week of February",
  "annual_audit_reminder_date": "January 2 (Annually, one month prior to Serie del Caribe / Winter League Finals)",
  "audit_interval_days_prior": 30,
  "match_duration": "9 innings.",
  "scoring_rules": "Standard baseball scoring.",
  "overtime_protocol": "Extra innings: Automatic runner on second base from 10th inning.",
  "roster_rules": "Championship teams reinforce rosters by drafting top players from eliminated domestic winter league teams.",
  "officiating": "CBPC international umpiring crew.",
  "settlement_source": "CBPC official box scores."
}
```
