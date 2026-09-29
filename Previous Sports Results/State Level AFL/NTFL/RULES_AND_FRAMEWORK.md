# Northern Territory Football League (NTFL) — Rules, Code & Analytical Framework

**Sport Discipline:** `State Level AFL`  
**Competition / League Subfolder:** `NTFL`  
**Governing Body:** AFL Northern Territory (AFLNT)  
**Inaugural Era / Foundation:** 1916  
**Status:** Canonical Reference Framework & Operating Protocol

---

## 1. Annual Rules & Competition Audit Protocol (Mandatory Reminder)

> [!IMPORTANT]
> ### 🚨 ANNUAL PRE-SEASON AUDIT REMINDER
> **Target Audit Date:** **`September 5 (Annually, exactly one month prior to wet season launch)`**  
> **Standard Season Kickoff Window:** **`October (Summer Wet Season Competition: October to March)`**  
>
> Exactly **one month prior to the commencement of every new season**, a full operational audit must be executed to determine whether the analytical parameters, league rules, or tournament structures require updating.

### Pre-Season Audit Checklist
Before issuing any forecast or recording historical results for an upcoming season:
1. **Rulebook Amendments:** Audit newly ratified rule changes by AFL Northern Territory (AFLNT) (e.g. playing duration, clock rules, overtime procedures, substitution mechanics, penalty enforcement).
2. **Mini-Competitions & In-Season Tournaments:** Check for newly introduced mini-competitions, in-season cups, showcase rounds, or altered playoff brackets (e.g., Australia Day clash, Tiwi Islands match.).
3. **Franchise & Conference Realignment:** Verify team expansion, relocation, division restructuring, or conference realignment.
4. **Roster & Player Availability Governance:** Inspect changes to active roster limits, injury replacement protocols, concussion management bylaws, and substitute eligibility rules.
5. **Officiating & Review Technology:** Review updates to video review systems, automated officiating (VAR, ARC, ABS, Hawk-Eye), and coaches' challenge allowances.
6. **Model Baseline Recalibration:** Recompute league-wide scoring baselines, margin standard deviations, key-number masses, and team priors.

---

## 2. Core Playing Rules & Scoring Framework

### Match Duration & Clock Governance
- **Regulation Playing Time:** 4 quarters x 20 minutes plus time-on.
- **Scoring Architecture:** Goal = 6 points, Behind = 1 point.
- **Overtime & Tie Resolution:** Extra time in finals only.

---

## 3. Competition Structure & Tournament Framework

### Regular Season & Format
- **Format:** 8 premier league clubs (St Mary's, Darwin Buffaloes, Nightcliff, Tiwi Bombers, Wanderers, Southern Districts, Palmerston, Waratah).
- **Standings & Tie-Breaking Criteria:**
  - Standard standings calculated by championship points or winning percentage.
  - Head-to-head records, differential percentages (e.g. percentage in AFL, run differential in baseball, point differential in football).
- **Post-Season / Finals System:** Page-McIntyre top 5 finals concluding with the NTFL Grand Final at TIO Stadium (Marrara Oval) in March.

---

## 4. Roster, Squad & Officiating Governance

### Squad Management & Substitutions
- **Squad Size & Active Roster:** Player point system accommodating fly-in players from AFL, VFL, SANFL, and WAFL during southern off-season.
- **Player Eligibility & Availability:** Team sheets and inactive lists must be re-verified against official feeds within 60 minutes of scheduled start time.

### Officiating & Video Review Framework
- **Officiating Crew:** AFLNT umpiring panel.
- **Review Protocols:** Standardized review triggers for goal-line / boundary line disputes, scoring plays, turnovers, or challenged decisions.

---

## 5. Analytical Modeling & Settlement Protocol

### Mathematical Modeling Methodology
- **Distributional Architecture:** High heat, extreme tropical humidity, monsoon rain events; high-pace, high-skill indigenous playing style.
- **Key Constraints:**
  - Model must anchor on official league population base rates.
  - Cushion lines (+k.5) and derivative handicap markets must be derived from the joint score/run distribution object, never estimated independently.
  - Weather vectors (wind, temperature, precipitation, altitude) must be mapped to ground orientation and venue geometry.

### Official Settlement Protocol
- **Data Lineage:** AFLNT Match Centre / PlayHQ.
- **Official Game Threshold:** Matches must meet the governing body's minimum completion threshold to be deemed official for full-game settlements.
- **Postponements & Rescheduled Matches:** If a match is delayed, suspended, or moved, settlement follows official league completion rules; uncompleted events void under standard market rules.

---

## 6. Machine-Readable Configuration Schema (JSON)

```json
{
  "competition_name": "Northern Territory Football League (NTFL)",
  "sport_category": "State Level AFL",
  "subfolder_directory": "NTFL",
  "governing_body": "AFL Northern Territory (AFLNT)",
  "season_kickoff_window": "October (Summer Wet Season Competition: October to March)",
  "annual_audit_reminder_date": "September 5 (Annually, exactly one month prior to wet season launch)",
  "audit_interval_days_prior": 30,
  "match_duration": "4 quarters x 20 minutes plus time-on.",
  "scoring_rules": "Goal = 6 points, Behind = 1 point.",
  "overtime_protocol": "Extra time in finals only.",
  "roster_rules": "Player point system accommodating fly-in players from AFL, VFL, SANFL, and WAFL during southern off-season.",
  "officiating": "AFLNT umpiring panel.",
  "settlement_source": "AFLNT Match Centre / PlayHQ."
}
```
