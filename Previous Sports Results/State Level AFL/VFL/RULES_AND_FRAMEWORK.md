# Victorian Football League (VFL) — Rules, Code & Analytical Framework

**Sport Discipline:** `State Level AFL`  
**Competition / League Subfolder:** `VFL`  
**Governing Body:** AFL Victoria  
**Inaugural Era / Foundation:** 1877 (as VFA; reorganized as VFL in 1996)  
**Status:** Canonical Reference Framework & Operating Protocol

---

## 1. Annual Rules & Competition Audit Protocol (Mandatory Reminder)

> [!IMPORTANT]
> ### 🚨 ANNUAL PRE-SEASON AUDIT REMINDER
> **Target Audit Date:** **`February 25 (Annually, exactly one month prior to opening round)`**  
> **Standard Season Kickoff Window:** **`Late March / Early April`**  
>
> Exactly **one month prior to the commencement of every new season**, a full operational audit must be executed to determine whether the analytical parameters, league rules, or tournament structures require updating.

### Pre-Season Audit Checklist
Before issuing any forecast or recording historical results for an upcoming season:
1. **Rulebook Amendments:** Audit newly ratified rule changes by AFL Victoria (e.g. playing duration, clock rules, overtime procedures, substitution mechanics, penalty enforcement).
2. **Mini-Competitions & In-Season Tournaments:** Check for newly introduced mini-competitions, in-season cups, showcase rounds, or altered playoff brackets (e.g., Wildcard Round.).
3. **Franchise & Conference Realignment:** Verify team expansion, relocation, division restructuring, or conference realignment.
4. **Roster & Player Availability Governance:** Inspect changes to active roster limits, injury replacement protocols, concussion management bylaws, and substitute eligibility rules.
5. **Officiating & Review Technology:** Review updates to video review systems, automated officiating (VAR, ARC, ABS, Hawk-Eye), and coaches' challenge allowances.
6. **Model Baseline Recalibration:** Recompute league-wide scoring baselines, margin standard deviations, key-number masses, and team priors.

---

## 2. Core Playing Rules & Scoring Framework

### Match Duration & Clock Governance
- **Regulation Playing Time:** 4 quarters x 20 minutes plus time-on.
- **Scoring Architecture:** Goal = 6 points, Behind = 1 point.
- **Overtime & Tie Resolution:** Home-and-away: Draws stand. Finals: 2 x 5-minute periods of extra time.

---

## 3. Competition Structure & Tournament Framework

### Regular Season & Format
- **Format:** State league featuring standalone Victorian clubs alongside AFL reserves teams from Victoria, NSW, and Queensland (21 teams).
- **Standings & Tie-Breaking Criteria:**
  - Standard standings calculated by championship points or winning percentage.
  - Head-to-head records, differential percentages (e.g. percentage in AFL, run differential in baseball, point differential in football).
- **Post-Season / Finals System:** Top 10 finals system (including Wildcard Round for 7th-10th), concluding in the VFL Grand Final at IKON Park.

---

## 4. Roster, Squad & Officiating Governance

### Squad Management & Substitutions
- **Squad Size & Active Roster:** Strict player point system (23-man matchday squad) balancing AFL-listed players with local development players.
- **Player Eligibility & Availability:** Team sheets and inactive lists must be re-verified against official feeds within 60 minutes of scheduled start time.

### Officiating & Video Review Framework
- **Officiating Crew:** State panel umpires accredited by AFL Victoria.
- **Review Protocols:** Standardized review triggers for goal-line / boundary line disputes, scoring plays, turnovers, or challenged decisions.

---

## 5. Analytical Modeling & Settlement Protocol

### Mathematical Modeling Methodology
- **Distributional Architecture:** Heavily influenced by AFL senior side selection; late changes in senior AFL teams directly impact VFL team sheets.
- **Key Constraints:**
  - Model must anchor on official league population base rates.
  - Cushion lines (+k.5) and derivative handicap markets must be derived from the joint score/run distribution object, never estimated independently.
  - Weather vectors (wind, temperature, precipitation, altitude) must be mapped to ground orientation and venue geometry.

### Official Settlement Protocol
- **Data Lineage:** AFL.com.au VFL Match Centre.
- **Official Game Threshold:** Matches must meet the governing body's minimum completion threshold to be deemed official for full-game settlements.
- **Postponements & Rescheduled Matches:** If a match is delayed, suspended, or moved, settlement follows official league completion rules; uncompleted events void under standard market rules.

---

## 6. Machine-Readable Configuration Schema (JSON)

```json
{
  "competition_name": "Victorian Football League (VFL)",
  "sport_category": "State Level AFL",
  "subfolder_directory": "VFL",
  "governing_body": "AFL Victoria",
  "season_kickoff_window": "Late March / Early April",
  "annual_audit_reminder_date": "February 25 (Annually, exactly one month prior to opening round)",
  "audit_interval_days_prior": 30,
  "match_duration": "4 quarters x 20 minutes plus time-on.",
  "scoring_rules": "Goal = 6 points, Behind = 1 point.",
  "overtime_protocol": "Home-and-away: Draws stand. Finals: 2 x 5-minute periods of extra time.",
  "roster_rules": "Strict player point system (23-man matchday squad) balancing AFL-listed players with local development players.",
  "officiating": "State panel umpires accredited by AFL Victoria.",
  "settlement_source": "AFL.com.au VFL Match Centre."
}
```
