# Australian Football League (AFL) Premiership — Rules, Code & Analytical Framework

**Sport Discipline:** `AFL`  
**Competition / League Subfolder:** `AFL`  
**Governing Body:** AFL Commission  
**Inaugural Era / Foundation:** 1897 (as VFL; national AFL era from 1990)  
**Status:** Canonical Reference Framework & Operating Protocol

---

## 1. Annual Rules & Competition Audit Protocol (Mandatory Reminder)

> [!IMPORTANT]
> ### 🚨 ANNUAL PRE-SEASON AUDIT REMINDER
> **Target Audit Date:** **`February 15 (Annually, exactly one month prior to season kickoff)`**  
> **Standard Season Kickoff Window:** **`Mid-March (Round 1 / Opening Round)`**  
>
> Exactly **one month prior to the commencement of every new season**, a full operational audit must be executed to determine whether the analytical parameters, league rules, or tournament structures require updating.

### Pre-Season Audit Checklist
Before issuing any forecast or recording historical results for an upcoming season:
1. **Rulebook Amendments:** Audit newly ratified rule changes by AFL Commission (e.g. playing duration, clock rules, overtime procedures, substitution mechanics, penalty enforcement).
2. **Mini-Competitions & In-Season Tournaments:** Check for newly introduced mini-competitions, in-season cups, showcase rounds, or altered playoff brackets (e.g., Gather Round (all matches played in South Australia), Opening Round (northern states marquee fixtures).).
3. **Franchise & Conference Realignment:** Verify team expansion, relocation, division restructuring, or conference realignment.
4. **Roster & Player Availability Governance:** Inspect changes to active roster limits, injury replacement protocols, concussion management bylaws, and substitute eligibility rules.
5. **Officiating & Review Technology:** Review updates to video review systems, automated officiating (VAR, ARC, ABS, Hawk-Eye), and coaches' challenge allowances.
6. **Model Baseline Recalibration:** Recompute league-wide scoring baselines, margin standard deviations, key-number masses, and team priors.

---

## 2. Core Playing Rules & Scoring Framework

### Match Duration & Clock Governance
- **Regulation Playing Time:** 4 quarters x 20 minutes plus time-on (stoppages, goals, ball out of bounds; ~30-33 mins actual per quarter)
- **Scoring Architecture:** Goal = 6 points (kicked between middle tall posts without being touched); Behind = 1 point (kicked between tall and outer short post, hit post, or touched over line).
- **Overtime & Tie Resolution:** Home-and-away season: Draws stand (2 points awarded to each team). Finals: Two 3-minute halves of extra time, repeated if still tied until a result is determined.

---

## 3. Competition Structure & Tournament Framework

### Regular Season & Format
- **Format:** 18 clubs playing 23 regular season matches plus Gather Round and Opening Round. Top 8 clubs qualify for the 4-week AFL Finals Series.
- **Standings & Tie-Breaking Criteria:**
  - Standard standings calculated by championship points or winning percentage.
  - Head-to-head records, differential percentages (e.g. percentage in AFL, run differential in baseball, point differential in football).
- **Post-Season / Finals System:** AFL Final Eight System: Week 1 features Qualifying Finals (1v4, 2v3; double chance) and Elimination Finals (5v8, 6v7; knockout). Week 2 features Semi-Finals. Week 3 features Preliminary Finals. Week 4 features the AFL Grand Final at the MCG.

---

## 4. Roster, Squad & Officiating Governance

### Squad Management & Substitutions
- **Squad Size & Active Roster:** Matchday squad: 22 on field/bench + 1 tactical substitute (introduced 2023 as 5-man bench with tactical sub). 75 interchange rotations cap per match.
- **Player Eligibility & Availability:** Team sheets and inactive lists must be re-verified against official feeds within 60 minutes of scheduled start time.

### Officiating & Video Review Framework
- **Officiating Crew:** 4 field umpires, 2 boundary umpires, 2 goal umpires, plus the AFL Review Centre (ARC) for ball-tracking and goal-line edge detection review.
- **Review Protocols:** Standardized review triggers for goal-line / boundary line disputes, scoring plays, turnovers, or challenged decisions.

---

## 5. Analytical Modeling & Settlement Protocol

### Mathematical Modeling Methodology
- **Distributional Architecture:** Scoring shots (goals + behinds) decomposed into territory, inside-50 efficiency, marks inside 50, and conversion probability (p = goals/shots). Points modeled as S * (1 + 5p).
- **Key Constraints:**
  - Model must anchor on official league population base rates.
  - Cushion lines (+k.5) and derivative handicap markets must be derived from the joint score/run distribution object, never estimated independently.
  - Weather vectors (wind, temperature, precipitation, altitude) must be mapped to ground orientation and venue geometry.

### Official Settlement Protocol
- **Data Lineage:** Settled from AFL Official Match Centre / Champion Data feeds. Official completion requires 4 completed quarters. Push/draw terms follow contract rules.
- **Official Game Threshold:** Matches must meet the governing body's minimum completion threshold to be deemed official for full-game settlements.
- **Postponements & Rescheduled Matches:** If a match is delayed, suspended, or moved, settlement follows official league completion rules; uncompleted events void under standard market rules.

---

## 6. Machine-Readable Configuration Schema (JSON)

```json
{
  "competition_name": "Australian Football League (AFL) Premiership",
  "sport_category": "AFL",
  "subfolder_directory": "AFL",
  "governing_body": "AFL Commission",
  "season_kickoff_window": "Mid-March (Round 1 / Opening Round)",
  "annual_audit_reminder_date": "February 15 (Annually, exactly one month prior to season kickoff)",
  "audit_interval_days_prior": 30,
  "match_duration": "4 quarters x 20 minutes plus time-on (stoppages, goals, ball out of bounds; ~30-33 mins actual per quarter)",
  "scoring_rules": "Goal = 6 points (kicked between middle tall posts without being touched); Behind = 1 point (kicked between tall and outer short post, hit post, or touched over line).",
  "overtime_protocol": "Home-and-away season: Draws stand (2 points awarded to each team). Finals: Two 3-minute halves of extra time, repeated if still tied until a result is determined.",
  "roster_rules": "Matchday squad: 22 on field/bench + 1 tactical substitute (introduced 2023 as 5-man bench with tactical sub). 75 interchange rotations cap per match.",
  "officiating": "4 field umpires, 2 boundary umpires, 2 goal umpires, plus the AFL Review Centre (ARC) for ball-tracking and goal-line edge detection review.",
  "settlement_source": "Settled from AFL Official Match Centre / Champion Data feeds. Official completion requires 4 completed quarters. Push/draw terms follow contract rules."
}
```
