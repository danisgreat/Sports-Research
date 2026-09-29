# Nippon Professional Baseball (NPB) — Rules, Code & Analytical Framework

**Sport Discipline:** `Baseball`  
**Competition / League Subfolder:** `NPB`  
**Governing Body:** Nippon Professional Baseball Organization  
**Inaugural Era / Foundation:** 1950 (roots in Japanese Baseball League, 1936)  
**Status:** Canonical Reference Framework & Operating Protocol

---

## 1. Annual Rules & Competition Audit Protocol (Mandatory Reminder)

> [!IMPORTANT]
> ### 🚨 ANNUAL PRE-SEASON AUDIT REMINDER
> **Target Audit Date:** **`February 25 (Annually, one month prior to Opening Day)`**  
> **Standard Season Kickoff Window:** **`Late March`**  
>
> Exactly **one month prior to the commencement of every new season**, a full operational audit must be executed to determine whether the analytical parameters, league rules, or tournament structures require updating.

### Pre-Season Audit Checklist
Before issuing any forecast or recording historical results for an upcoming season:
1. **Rulebook Amendments:** Audit newly ratified rule changes by Nippon Professional Baseball Organization (e.g. playing duration, clock rules, overtime procedures, substitution mechanics, penalty enforcement).
2. **Mini-Competitions & In-Season Tournaments:** Check for newly introduced mini-competitions, in-season cups, showcase rounds, or altered playoff brackets (e.g., NPB All-Star Series (2-3 games), Interleague Tournament.).
3. **Franchise & Conference Realignment:** Verify team expansion, relocation, division restructuring, or conference realignment.
4. **Roster & Player Availability Governance:** Inspect changes to active roster limits, injury replacement protocols, concussion management bylaws, and substitute eligibility rules.
5. **Officiating & Review Technology:** Review updates to video review systems, automated officiating (VAR, ARC, ABS, Hawk-Eye), and coaches' challenge allowances.
6. **Model Baseline Recalibration:** Recompute league-wide scoring baselines, margin standard deviations, key-number masses, and team priors.

---

## 2. Core Playing Rules & Scoring Framework

### Match Duration & Clock Governance
- **Regulation Playing Time:** 9 innings.
- **Scoring Architecture:** Standard baseball scoring.
- **Overtime & Tie Resolution:** Regular season: Matches tied after 12 innings are declared official draws (ties count in standings). No automatic ghost runner. Postseason: 12-inning tie limit in Climax Series; 12-inning limit in Games 1-7 of Japan Series (Games 8+ played to completion if necessary).

---

## 3. Competition Structure & Tournament Framework

### Regular Season & Format
- **Format:** 12 teams: Central League (6 teams, no DH; pitchers bat) and Pacific League (6 teams, uses DH). 143 regular season games + Interleague play (Koryusen).
- **Standings & Tie-Breaking Criteria:**
  - Standard standings calculated by championship points or winning percentage.
  - Head-to-head records, differential percentages (e.g. percentage in AFL, run differential in baseball, point differential in football).
- **Post-Season / Finals System:** Climax Series: First Stage (2v3, best-of-3), Final Stage (1v First Stage winner, best-of-6 with #1 seed starting with 1-0 advantage). Winners meet in the best-of-7 Japan Series.

---

## 4. Roster, Squad & Officiating Governance

### Squad Management & Substitutions
- **Squad Size & Active Roster:** 31-man registered roster, 26 active per game. Maximum 4-5 foreign players on active roster (cannot be all pitchers or all position players).
- **Player Eligibility & Availability:** Team sheets and inactive lists must be re-verified against official feeds within 60 minutes of scheduled start time.

### Officiating & Video Review Framework
- **Officiating Crew:** NPB professional umpiring crew. Replay review (Request system): 2 requests per 9 innings, retained if successful.
- **Review Protocols:** Standardized review triggers for goal-line / boundary line disputes, scoring plays, turnovers, or challenged decisions.

---

## 5. Analytical Modeling & Settlement Protocol

### Mathematical Modeling Methodology
- **Distributional Architecture:** Three-way outcome model required (Home Win, Away Win, Tie ~4-6% probability). Pitcher-dominated baseline; Central League has lower run environments due to batting pitchers.
- **Key Constraints:**
  - Model must anchor on official league population base rates.
  - Cushion lines (+k.5) and derivative handicap markets must be derived from the joint score/run distribution object, never estimated independently.
  - Weather vectors (wind, temperature, precipitation, altitude) must be mapped to ground orientation and venue geometry.

### Official Settlement Protocol
- **Data Lineage:** NPB.jp official box scores.
- **Official Game Threshold:** Matches must meet the governing body's minimum completion threshold to be deemed official for full-game settlements.
- **Postponements & Rescheduled Matches:** If a match is delayed, suspended, or moved, settlement follows official league completion rules; uncompleted events void under standard market rules.

---

## 6. Machine-Readable Configuration Schema (JSON)

```json
{
  "competition_name": "Nippon Professional Baseball (NPB)",
  "sport_category": "Baseball",
  "subfolder_directory": "NPB",
  "governing_body": "Nippon Professional Baseball Organization",
  "season_kickoff_window": "Late March",
  "annual_audit_reminder_date": "February 25 (Annually, one month prior to Opening Day)",
  "audit_interval_days_prior": 30,
  "match_duration": "9 innings.",
  "scoring_rules": "Standard baseball scoring.",
  "overtime_protocol": "Regular season: Matches tied after 12 innings are declared official draws (ties count in standings). No automatic ghost runner. Postseason: 12-inning tie limit in Climax Series; 12-inning limit in Games 1-7 of Japan Series (Games 8+ played to completion if necessary).",
  "roster_rules": "31-man registered roster, 26 active per game. Maximum 4-5 foreign players on active roster (cannot be all pitchers or all position players).",
  "officiating": "NPB professional umpiring crew. Replay review (Request system): 2 requests per 9 innings, retained if successful.",
  "settlement_source": "NPB.jp official box scores."
}
```
