# NCAA Division I Football Bowl Subdivision (FBS) — Rules, Code & Analytical Framework

**Sport Discipline:** `College Football`  
**Competition / League Subfolder:** `NCAA Division I FBS`  
**Governing Body:** NCAA Football Rules Committee  
**Inaugural Era / Foundation:** 1869 (division split into I-A / FBS established 1978)  
**Status:** Canonical Reference Framework & Operating Protocol

---

## 1. Annual Rules & Competition Audit Protocol (Mandatory Reminder)

> [!IMPORTANT]
> ### 🚨 ANNUAL PRE-SEASON AUDIT REMINDER
> **Target Audit Date:** **`July 24 (Annually, exactly one month prior to Week 0 kickoff)`**  
> **Standard Season Kickoff Window:** **`Late August (Week 0) / Labor Day Weekend (Week 1)`**  
>
> Exactly **one month prior to the commencement of every new season**, a full operational audit must be executed to determine whether the analytical parameters, league rules, or tournament structures require updating.

### Pre-Season Audit Checklist
Before issuing any forecast or recording historical results for an upcoming season:
1. **Rulebook Amendments:** Audit newly ratified rule changes by NCAA Football Rules Committee (e.g. playing duration, clock rules, overtime procedures, substitution mechanics, penalty enforcement).
2. **Mini-Competitions & In-Season Tournaments:** Check for newly introduced mini-competitions, in-season cups, showcase rounds, or altered playoff brackets (e.g., Rivalry Week (Iron Bowl, The Game, Red River Rivalry, Army-Navy Game), Conference Championship Games.).
3. **Franchise & Conference Realignment:** Verify team expansion, relocation, division restructuring, or conference realignment.
4. **Roster & Player Availability Governance:** Inspect changes to active roster limits, injury replacement protocols, concussion management bylaws, and substitute eligibility rules.
5. **Officiating & Review Technology:** Review updates to video review systems, automated officiating (VAR, ARC, ABS, Hawk-Eye), and coaches' challenge allowances.
6. **Model Baseline Recalibration:** Recompute league-wide scoring baselines, margin standard deviations, key-number masses, and team priors.

---

## 2. Core Playing Rules & Scoring Framework

### Match Duration & Clock Governance
- **Regulation Playing Time:** 4 quarters x 15 minutes. Clock stops on first downs only inside the last 2 minutes of each half (rule update 2023).
- **Scoring Architecture:** TD = 6; FG = 3; Safety = 2; PAT = 1; 2-pt Conv = 2.
- **Overtime & Tie Resolution:** Possession-based overtime from the 25-yard line. Teams must attempt a 2-point conversion starting in the 2nd overtime. Beginning in 3rd overtime, teams alternate single 2-point conversion plays.

---

## 3. Competition Structure & Tournament Framework

### Regular Season & Format
- **Format:** 134 FBS programs across 10 conferences (Power Four: SEC, Big Ten, ACC, Big 12; Group of Five: AAC, MWC, Sun Belt, MAC, CUSA) and Independents (Notre Dame). 12 regular season games.
- **Standings & Tie-Breaking Criteria:**
  - Standard standings calculated by championship points or winning percentage.
  - Head-to-head records, differential percentages (e.g. percentage in AFL, run differential in baseball, point differential in football).
- **Post-Season / Finals System:** Conference championship games in early December, followed by College Football Playoff and bowl games.

---

## 4. Roster, Squad & Officiating Governance

### Squad Management & Substitutions
- **Squad Size & Active Roster:** 85-scholarship limit, 105-man roster cap (2024 settlement), NCAA Transfer Portal windows, NIL eligibility frameworks.
- **Player Eligibility & Availability:** Team sheets and inactive lists must be re-verified against official feeds within 60 minutes of scheduled start time.

### Officiating & Video Review Framework
- **Officiating Crew:** 8 on-field collegiate officials + in-stadium video review replay official with authority to stop play for targeting and line-to-gain calls.
- **Review Protocols:** Standardized review triggers for goal-line / boundary line disputes, scoring plays, turnovers, or challenged decisions.

---

## 5. Analytical Modeling & Settlement Protocol

### Mathematical Modeling Methodology
- **Distributional Architecture:** Greater spread variance than NFL (spreads range from -1.0 to -55.0). Explosive play metrics, Havoc rate, and SP+ / EPA baselines.
- **Key Constraints:**
  - Model must anchor on official league population base rates.
  - Cushion lines (+k.5) and derivative handicap markets must be derived from the joint score/run distribution object, never estimated independently.
  - Weather vectors (wind, temperature, precipitation, altitude) must be mapped to ground orientation and venue geometry.

### Official Settlement Protocol
- **Data Lineage:** Official NCAA Game Statistics, ESPN/StatBroadcast feeds. Minimum 55 minutes or official termination by referee.
- **Official Game Threshold:** Matches must meet the governing body's minimum completion threshold to be deemed official for full-game settlements.
- **Postponements & Rescheduled Matches:** If a match is delayed, suspended, or moved, settlement follows official league completion rules; uncompleted events void under standard market rules.

---

## 6. Machine-Readable Configuration Schema (JSON)

```json
{
  "competition_name": "NCAA Division I Football Bowl Subdivision (FBS)",
  "sport_category": "College Football",
  "subfolder_directory": "NCAA Division I FBS",
  "governing_body": "NCAA Football Rules Committee",
  "season_kickoff_window": "Late August (Week 0) / Labor Day Weekend (Week 1)",
  "annual_audit_reminder_date": "July 24 (Annually, exactly one month prior to Week 0 kickoff)",
  "audit_interval_days_prior": 30,
  "match_duration": "4 quarters x 15 minutes. Clock stops on first downs only inside the last 2 minutes of each half (rule update 2023).",
  "scoring_rules": "TD = 6; FG = 3; Safety = 2; PAT = 1; 2-pt Conv = 2.",
  "overtime_protocol": "Possession-based overtime from the 25-yard line. Teams must attempt a 2-point conversion starting in the 2nd overtime. Beginning in 3rd overtime, teams alternate single 2-point conversion plays.",
  "roster_rules": "85-scholarship limit, 105-man roster cap (2024 settlement), NCAA Transfer Portal windows, NIL eligibility frameworks.",
  "officiating": "8 on-field collegiate officials + in-stadium video review replay official with authority to stop play for targeting and line-to-gain calls.",
  "settlement_source": "Official NCAA Game Statistics, ESPN/StatBroadcast feeds. Minimum 55 minutes or official termination by referee."
}
```
