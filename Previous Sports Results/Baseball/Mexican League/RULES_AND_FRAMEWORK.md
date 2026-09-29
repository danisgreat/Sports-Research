# Liga Mexicana de Béisbol (LMB) — Rules, Code & Analytical Framework

**Sport Discipline:** `Baseball`  
**Competition / League Subfolder:** `Mexican League`  
**Governing Body:** LMB Board of Directors  
**Inaugural Era / Foundation:** 1925  
**Status:** Canonical Reference Framework & Operating Protocol

---

## 1. Annual Rules & Competition Audit Protocol (Mandatory Reminder)

> [!IMPORTANT]
> ### 🚨 ANNUAL PRE-SEASON AUDIT REMINDER
> **Target Audit Date:** **`March 15 (Annually, one month prior to opening day)`**  
> **Standard Season Kickoff Window:** **`Mid-April`**  
>
> Exactly **one month prior to the commencement of every new season**, a full operational audit must be executed to determine whether the analytical parameters, league rules, or tournament structures require updating.

### Pre-Season Audit Checklist
Before issuing any forecast or recording historical results for an upcoming season:
1. **Rulebook Amendments:** Audit newly ratified rule changes by LMB Board of Directors (e.g. playing duration, clock rules, overtime procedures, substitution mechanics, penalty enforcement).
2. **Mini-Competitions & In-Season Tournaments:** Check for newly introduced mini-competitions, in-season cups, showcase rounds, or altered playoff brackets (e.g., Juego de Estrellas (All-Star Game).).
3. **Franchise & Conference Realignment:** Verify team expansion, relocation, division restructuring, or conference realignment.
4. **Roster & Player Availability Governance:** Inspect changes to active roster limits, injury replacement protocols, concussion management bylaws, and substitute eligibility rules.
5. **Officiating & Review Technology:** Review updates to video review systems, automated officiating (VAR, ARC, ABS, Hawk-Eye), and coaches' challenge allowances.
6. **Model Baseline Recalibration:** Recompute league-wide scoring baselines, margin standard deviations, key-number masses, and team priors.

---

## 2. Core Playing Rules & Scoring Framework

### Match Duration & Clock Governance
- **Regulation Playing Time:** 9 innings (7 innings for scheduled doubleheaders).
- **Scoring Architecture:** Standard baseball scoring.
- **Overtime & Tie Resolution:** Extra innings played to completion.

---

## 3. Competition Structure & Tournament Framework

### Regular Season & Format
- **Format:** 20 teams split into Zona Norte and Zona Sur. 93-game regular season.
- **Standings & Tie-Breaking Criteria:**
  - Standard standings calculated by championship points or winning percentage.
  - Head-to-head records, differential percentages (e.g. percentage in AFL, run differential in baseball, point differential in football).
- **Post-Season / Finals System:** 4-round playoff bracket concluding in the Serie del Rey (King's Series, best-of-7).

---

## 4. Roster, Squad & Officiating Governance

### Squad Management & Substitutions
- **Squad Size & Active Roster:** Expanded foreign/import player regulations. Universal DH.
- **Player Eligibility & Availability:** Team sheets and inactive lists must be re-verified against official feeds within 60 minutes of scheduled start time.

### Officiating & Video Review Framework
- **Officiating Crew:** LMB umpiring panel with central review.
- **Review Protocols:** Standardized review triggers for goal-line / boundary line disputes, scoring plays, turnovers, or challenged decisions.

---

## 5. Analytical Modeling & Settlement Protocol

### Mathematical Modeling Methodology
- **Distributional Architecture:** Extreme elevation adjustments required (e.g. Mexico City elevation 2,240m creates massive run-environment inflation; northern desert venues have extreme heat).
- **Key Constraints:**
  - Model must anchor on official league population base rates.
  - Cushion lines (+k.5) and derivative handicap markets must be derived from the joint score/run distribution object, never estimated independently.
  - Weather vectors (wind, temperature, precipitation, altitude) must be mapped to ground orientation and venue geometry.

### Official Settlement Protocol
- **Data Lineage:** Milb.com/mexican / LMB official feeds.
- **Official Game Threshold:** Matches must meet the governing body's minimum completion threshold to be deemed official for full-game settlements.
- **Postponements & Rescheduled Matches:** If a match is delayed, suspended, or moved, settlement follows official league completion rules; uncompleted events void under standard market rules.

---

## 6. Machine-Readable Configuration Schema (JSON)

```json
{
  "competition_name": "Liga Mexicana de Béisbol (LMB)",
  "sport_category": "Baseball",
  "subfolder_directory": "Mexican League",
  "governing_body": "LMB Board of Directors",
  "season_kickoff_window": "Mid-April",
  "annual_audit_reminder_date": "March 15 (Annually, one month prior to opening day)",
  "audit_interval_days_prior": 30,
  "match_duration": "9 innings (7 innings for scheduled doubleheaders).",
  "scoring_rules": "Standard baseball scoring.",
  "overtime_protocol": "Extra innings played to completion.",
  "roster_rules": "Expanded foreign/import player regulations. Universal DH.",
  "officiating": "LMB umpiring panel with central review.",
  "settlement_source": "Milb.com/mexican / LMB official feeds."
}
```
