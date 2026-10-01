# KBO League — Rules, Code & Analytical Framework

**Sport Discipline:** `Baseball`  
**Competition / League Subfolder:** `KBO`  
**Governing Body:** Korea Baseball Organization (KBO)  
**Inaugural Era / Foundation:** 1982  
**Status:** Canonical Reference Framework & Operating Protocol

---

## 1. Annual Rules & Competition Audit Protocol (Mandatory Reminder)

> [!IMPORTANT]
> ### 🚨 ANNUAL PRE-SEASON AUDIT REMINDER
> **Target Audit Date:** **`February 25 (Annually, one month prior to Opening Day)`**  
> **Standard Season Kickoff Window:** **`Late March / Early April`**  
>
> Exactly **one month prior to the commencement of every new season**, a full operational audit must be executed to determine whether the analytical parameters, league rules, or tournament structures require updating.

### Pre-Season Audit Checklist
Before issuing any forecast or recording historical results for an upcoming season:
1. **Rulebook Amendments:** Audit newly ratified rule changes by Korea Baseball Organization (KBO) (e.g. playing duration, clock rules, overtime procedures, substitution mechanics, penalty enforcement).
2. **Mini-Competitions & In-Season Tournaments:** Check for newly introduced mini-competitions, in-season cups, showcase rounds, or altered playoff brackets (e.g., KBO All-Star Game.).
3. **Franchise & Conference Realignment:** Verify team expansion, relocation, division restructuring, or conference realignment.
4. **Roster & Player Availability Governance:** Inspect changes to active roster limits, injury replacement protocols, concussion management bylaws, and substitute eligibility rules.
5. **Officiating & Review Technology:** Review updates to video review systems, automated officiating (VAR, ARC, ABS, Hawk-Eye), and coaches' challenge allowances.
6. **Model Baseline Recalibration:** Recompute league-wide scoring baselines, margin standard deviations, key-number masses, and team priors.

---

## 2. Core Playing Rules & Scoring Framework

### Match Duration & Clock Governance
- **Regulation Playing Time:** 9 innings.
- **Scoring Architecture:** Standard baseball scoring.
- **Overtime & Tie Resolution:** From the 2025 rule change, regular-season games end after at most **11 innings**, with an official tie if still level. The previous 12-inning limit must be applied only to historical seasons where it governed. [Official KBO 2025 changes](https://www.koreabaseball.com/Kbo/League/GameManage2025.aspx), section 연장전 이닝 축소; [current 2026 changes](https://www.koreabaseball.com/Kbo/League/GameManage2026.aspx). October 1, 2026 source bodies retained in `research/verification/log_repair_2026-10-01/`. Postseason and other tie-break procedures require their separate season/stage audit; do not infer them from the regular-season limit.

---

## 3. Competition Structure & Tournament Framework

### Regular Season & Format
- **Format:** 10 clubs playing 144 regular season games. Universal Designated Hitter.
- **Standings & Tie-Breaking Criteria:**
  - Standard standings calculated by championship points or winning percentage.
  - Head-to-head records, differential percentages (e.g. percentage in AFL, run differential in baseball, point differential in football).
- **Post-Season / Finals System:** Stepladder Postseason System: Wild Card game (4th vs 5th; 4th seed starts with 1-0 lead), Semi-Playoff (3rd vs WC winner, best-of-5), Playoff (2nd vs Semi-Playoff winner, best-of-5), Korean Series (1st seed vs Playoff winner, best-of-7).

---

## 4. Roster, Squad & Officiating Governance

### Squad Management & Substitutions
- **Squad Size & Active Roster:** 28-man active roster. Max 3 foreign players per club (max 2 pitchers). First major top-flight league to implement full Automated Ball-Strike System (ABS / robot umpires) in 2024.
- **Player Eligibility & Availability:** Team sheets and inactive lists must be re-verified against official feeds within 60 minutes of scheduled start time.

### Officiating & Video Review Framework
- **Officiating Crew:** KBO umpires with ABS in-ear automated ball-strike relay.
- **Review Protocols:** Standardized review triggers for goal-line / boundary line disputes, scoring plays, turnovers, or challenged decisions.

---

## 5. Analytical Modeling & Settlement Protocol

### Mathematical Modeling Methodology
- **Distributional Architecture:** High offensive baseline (~10.0-10.8 runs per game combined). Three-way probability model required due to 12-inning tie cap.
- **Key Constraints:**
  - Model must anchor on official league population base rates.
  - Cushion lines (+k.5) and derivative handicap markets must be derived from the joint score/run distribution object, never estimated independently.
  - Weather vectors (wind, temperature, precipitation, altitude) must be mapped to ground orientation and venue geometry.

### Official Settlement Protocol
- **Data Lineage:** KBO official game records (koreabaseball.com).
- **Official Game Threshold:** Matches must meet the governing body's minimum completion threshold to be deemed official for full-game settlements.
- **Postponements & Rescheduled Matches:** If a match is delayed, suspended, or moved, settlement follows official league completion rules; uncompleted events void under standard market rules.

---

## 6. Machine-Readable Configuration Schema (JSON)

```json
{
  "competition_name": "KBO League",
  "sport_category": "Baseball",
  "subfolder_directory": "KBO",
  "governing_body": "Korea Baseball Organization (KBO)",
  "season_kickoff_window": "Late March / Early April",
  "annual_audit_reminder_date": "February 25 (Annually, one month prior to Opening Day)",
  "audit_interval_days_prior": 30,
  "match_duration": "9 innings.",
  "scoring_rules": "Standard baseball scoring.",
  "overtime_protocol": "Regular season: 12-inning tie limit (games declared official ties; no ghost runner). Postseason: 15-inning tie limit.",
  "roster_rules": "28-man active roster. Max 3 foreign players per club (max 2 pitchers). First major top-flight league to implement full Automated Ball-Strike System (ABS / robot umpires) in 2024.",
  "officiating": "KBO umpires with ABS in-ear automated ball-strike relay.",
  "settlement_source": "KBO official game records (koreabaseball.com)."
}
```
