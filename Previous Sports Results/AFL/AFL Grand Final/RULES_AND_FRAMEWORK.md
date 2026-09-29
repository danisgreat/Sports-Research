# AFL Grand Final — Rules, Code & Analytical Framework

**Sport Discipline:** `AFL`  
**Competition / League Subfolder:** `AFL Grand Final`  
**Governing Body:** AFL Commission  
**Inaugural Era / Foundation:** 1898  
**Status:** Canonical Reference Framework & Operating Protocol

---

## 1. Annual Rules & Competition Audit Protocol (Mandatory Reminder)

> [!IMPORTANT]
> ### 🚨 ANNUAL PRE-SEASON AUDIT REMINDER
> **Target Audit Date:** **`August 25 (Annually, exactly one month prior to Grand Final week)`**  
> **Standard Season Kickoff Window:** **`Last Saturday in September (or first Saturday in October)`**  
>
> Exactly **one month prior to the commencement of every new season**, a full operational audit must be executed to determine whether the analytical parameters, league rules, or tournament structures require updating.

### Pre-Season Audit Checklist
Before issuing any forecast or recording historical results for an upcoming season:
1. **Rulebook Amendments:** Audit newly ratified rule changes by AFL Commission (e.g. playing duration, clock rules, overtime procedures, substitution mechanics, penalty enforcement).
2. **Mini-Competitions & In-Season Tournaments:** Check for newly introduced mini-competitions, in-season cups, showcase rounds, or altered playoff brackets (e.g., Grand Final Sprint, Longest Kick competition.).
3. **Franchise & Conference Realignment:** Verify team expansion, relocation, division restructuring, or conference realignment.
4. **Roster & Player Availability Governance:** Inspect changes to active roster limits, injury replacement protocols, concussion management bylaws, and substitute eligibility rules.
5. **Officiating & Review Technology:** Review updates to video review systems, automated officiating (VAR, ARC, ABS, Hawk-Eye), and coaches' challenge allowances.
6. **Model Baseline Recalibration:** Recompute league-wide scoring baselines, margin standard deviations, key-number masses, and team priors.

---

## 2. Core Playing Rules & Scoring Framework

### Match Duration & Clock Governance
- **Regulation Playing Time:** 4 quarters x 20 minutes plus time-on.
- **Scoring Architecture:** Goal = 6 points, Behind = 1 point.
- **Overtime & Tie Resolution:** Extra Time Protocol: If scores are tied at full time, two 3-minute halves (with time-on) are played. If still tied, the process repeats until a winner emerges. The historical Grand Final Replay rule was abolished post-2016.

---

## 3. Competition Structure & Tournament Framework

### Regular Season & Format
- **Format:** Single championship match contested between the winners of the two Preliminary Finals, traditionally staged at the Melbourne Cricket Ground (MCG).
- **Standings & Tie-Breaking Criteria:**
  - Standard standings calculated by championship points or winning percentage.
  - Head-to-head records, differential percentages (e.g. percentage in AFL, run differential in baseball, point differential in football).
- **Post-Season / Finals System:** Ultimate deciding fixture of the AFL season. Winner receives the AFL Premiership Cup, Premiership Medals, and the best-on-ground receives the Norm Smith Medal.

---

## 4. Roster, Squad & Officiating Governance

### Squad Management & Substitutions
- **Squad Size & Active Roster:** 22 named players + 1 tactical substitute selected from the final 26-man squads submitted Thursday night.
- **Player Eligibility & Availability:** Team sheets and inactive lists must be re-verified against official feeds within 60 minutes of scheduled start time.

### Officiating & Video Review Framework
- **Officiating Crew:** Senior senior panel: 4 field umpires, 4 boundary umpires, 2 goal umpires, full ARC review operations.
- **Review Protocols:** Standardized review triggers for goal-line / boundary line disputes, scoring plays, turnovers, or challenged decisions.

---

## 5. Analytical Modeling & Settlement Protocol

### Mathematical Modeling Methodology
- **Distributional Architecture:** Grand Final pricing applies venue prior (MCG ground dimensions 160m x 141m), neutral/home crowd distribution, and finals pressure metrics (clearance and contested possession differentials).
- **Key Constraints:**
  - Model must anchor on official league population base rates.
  - Cushion lines (+k.5) and derivative handicap markets must be derived from the joint score/run distribution object, never estimated independently.
  - Weather vectors (wind, temperature, precipitation, altitude) must be mapped to ground orientation and venue geometry.

### Official Settlement Protocol
- **Data Lineage:** Settled immediately upon final siren of regulation (or extra time if required). Official trophy presentation constitutes final record.
- **Official Game Threshold:** Matches must meet the governing body's minimum completion threshold to be deemed official for full-game settlements.
- **Postponements & Rescheduled Matches:** If a match is delayed, suspended, or moved, settlement follows official league completion rules; uncompleted events void under standard market rules.

---

## 6. Machine-Readable Configuration Schema (JSON)

```json
{
  "competition_name": "AFL Grand Final",
  "sport_category": "AFL",
  "subfolder_directory": "AFL Grand Final",
  "governing_body": "AFL Commission",
  "season_kickoff_window": "Last Saturday in September (or first Saturday in October)",
  "annual_audit_reminder_date": "August 25 (Annually, exactly one month prior to Grand Final week)",
  "audit_interval_days_prior": 30,
  "match_duration": "4 quarters x 20 minutes plus time-on.",
  "scoring_rules": "Goal = 6 points, Behind = 1 point.",
  "overtime_protocol": "Extra Time Protocol: If scores are tied at full time, two 3-minute halves (with time-on) are played. If still tied, the process repeats until a winner emerges. The historical Grand Final Replay rule was abolished post-2016.",
  "roster_rules": "22 named players + 1 tactical substitute selected from the final 26-man squads submitted Thursday night.",
  "officiating": "Senior senior panel: 4 field umpires, 4 boundary umpires, 2 goal umpires, full ARC review operations.",
  "settlement_source": "Settled immediately upon final siren of regulation (or extra time if required). Official trophy presentation constitutes final record."
}
```
