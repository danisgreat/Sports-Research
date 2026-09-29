# National Football League (NFL) — Rules, Code & Analytical Framework

**Sport Discipline:** `American Football`  
**Competition / League Subfolder:** `NFL`  
**Governing Body:** NFL Management Council / Competition Committee  
**Inaugural Era / Foundation:** 1920 (as APFA; renamed NFL in 1922; merged with AFL in 1970)  
**Status:** Canonical Reference Framework & Operating Protocol

---

## 1. Annual Rules & Competition Audit Protocol (Mandatory Reminder)

> [!IMPORTANT]
> ### 🚨 ANNUAL PRE-SEASON AUDIT REMINDER
> **Target Audit Date:** **`August 5 (Annually, exactly one month prior to regular season kickoff / Hall of Fame game)`**  
> **Standard Season Kickoff Window:** **`Thursday following first Monday in September`**  
>
> Exactly **one month prior to the commencement of every new season**, a full operational audit must be executed to determine whether the analytical parameters, league rules, or tournament structures require updating.

### Pre-Season Audit Checklist
Before issuing any forecast or recording historical results for an upcoming season:
1. **Rulebook Amendments:** Audit newly ratified rule changes by NFL Management Council / Competition Committee (e.g. playing duration, clock rules, overtime procedures, substitution mechanics, penalty enforcement).
2. **Mini-Competitions & In-Season Tournaments:** Check for newly introduced mini-competitions, in-season cups, showcase rounds, or altered playoff brackets (e.g., NFL International Series (London, Munich, Frankfurt, São Paulo), Thanksgiving Tripleheader, Christmas Day games.).
3. **Franchise & Conference Realignment:** Verify team expansion, relocation, division restructuring, or conference realignment.
4. **Roster & Player Availability Governance:** Inspect changes to active roster limits, injury replacement protocols, concussion management bylaws, and substitute eligibility rules.
5. **Officiating & Review Technology:** Review updates to video review systems, automated officiating (VAR, ARC, ABS, Hawk-Eye), and coaches' challenge allowances.
6. **Model Baseline Recalibration:** Recompute league-wide scoring baselines, margin standard deviations, key-number masses, and team priors.

---

## 2. Core Playing Rules & Scoring Framework

### Match Duration & Clock Governance
- **Regulation Playing Time:** 4 quarters x 15 minutes (60 minutes regulation). 12-minute halftime.
- **Scoring Architecture:** Touchdown = 6 points; Field Goal = 3 points; Safety = 2 points; Try/PAT Kick = 1 point; 2-Point Conversion = 2 points.
- **Overtime & Tie Resolution:** Regular season: 10-minute period. Both teams get a possession unless first team scores a TD, or defensive safety. If tied after 10 mins, game is a tie. Postseason: 15-minute periods until a winner is determined; both teams guaranteed a possession regardless of first-possession TD.

---

## 3. Competition Structure & Tournament Framework

### Regular Season & Format
- **Format:** 32 franchises divided into AFC and NFC (4 divisions of 4 teams each). 18-week regular season (17 games + 1 bye week).
- **Standings & Tie-Breaking Criteria:**
  - Standard standings calculated by championship points or winning percentage.
  - Head-to-head records, differential percentages (e.g. percentage in AFL, run differential in baseball, point differential in football).
- **Post-Season / Finals System:** 14-team postseason (7 per conference: 4 division winners + 3 wild cards). #1 seeds receive first-round bye. Single-elimination: Wild Card Weekend, Divisional Round, Conference Championships, Super Bowl.

---

## 4. Roster, Squad & Officiating Governance

### Squad Management & Substitutions
- **Squad Size & Active Roster:** 53-man active roster (48 dressed on game day if 8 offensive linemen dressed), 16-man practice squad, emergency 3rd quarterback activation rule.
- **Player Eligibility & Availability:** Team sheets and inactive lists must be re-verified against official feeds within 60 minutes of scheduled start time.

### Officiating & Video Review Framework
- **Officiating Crew:** 7 on-field officials (Referee, Umpire, Down Judge, Line Judge, Field Judge, Side Judge, Back Judge) + NFL Officiating Replay Command Center in New York. 2 coach's challenges per game (3rd awarded if both successful). Automatic review of all scoring plays, turnovers, and plays within 2 minutes of each half.
- **Review Protocols:** Standardized review triggers for goal-line / boundary line disputes, scoring plays, turnovers, or challenged decisions.

---

## 5. Analytical Modeling & Settlement Protocol

### Mathematical Modeling Methodology
- **Distributional Architecture:** Key number anchoring on 3, 7, 6, 10, 4, 14. Margin residual width ~13.6 points. Weather (temperature, cross-winds >15 mph, precipitation) integrated into total and passing efficiency projections.
- **Key Constraints:**
  - Model must anchor on official league population base rates.
  - Cushion lines (+k.5) and derivative handicap markets must be derived from the joint score/run distribution object, never estimated independently.
  - Weather vectors (wind, temperature, precipitation, altitude) must be mapped to ground orientation and venue geometry.

### Official Settlement Protocol
- **Data Lineage:** Official settlement via NFL GSIS / Game Statistics and Information System. Minimum 55 completed minutes of play required for official game status.
- **Official Game Threshold:** Matches must meet the governing body's minimum completion threshold to be deemed official for full-game settlements.
- **Postponements & Rescheduled Matches:** If a match is delayed, suspended, or moved, settlement follows official league completion rules; uncompleted events void under standard market rules.

---

## 6. Machine-Readable Configuration Schema (JSON)

```json
{
  "competition_name": "National Football League (NFL)",
  "sport_category": "American Football",
  "subfolder_directory": "NFL",
  "governing_body": "NFL Management Council / Competition Committee",
  "season_kickoff_window": "Thursday following first Monday in September",
  "annual_audit_reminder_date": "August 5 (Annually, exactly one month prior to regular season kickoff / Hall of Fame game)",
  "audit_interval_days_prior": 30,
  "match_duration": "4 quarters x 15 minutes (60 minutes regulation). 12-minute halftime.",
  "scoring_rules": "Touchdown = 6 points; Field Goal = 3 points; Safety = 2 points; Try/PAT Kick = 1 point; 2-Point Conversion = 2 points.",
  "overtime_protocol": "Regular season: 10-minute period. Both teams get a possession unless first team scores a TD, or defensive safety. If tied after 10 mins, game is a tie. Postseason: 15-minute periods until a winner is determined; both teams guaranteed a possession regardless of first-possession TD.",
  "roster_rules": "53-man active roster (48 dressed on game day if 8 offensive linemen dressed), 16-man practice squad, emergency 3rd quarterback activation rule.",
  "officiating": "7 on-field officials (Referee, Umpire, Down Judge, Line Judge, Field Judge, Side Judge, Back Judge) + NFL Officiating Replay Command Center in New York. 2 coach's challenges per game (3rd awarded if both successful). Automatic review of all scoring plays, turnovers, and plays within 2 minutes of each half.",
  "settlement_source": "Official settlement via NFL GSIS / Game Statistics and Information System. Minimum 55 completed minutes of play required for official game status."
}
```
