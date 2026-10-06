# National Hockey League (NHL) & Professional Ice Hockey Numerical Rules

**Authority:** MDS-2026.10.01-v8.0 / CR-2026.10.06-NUMERICAL-1.
**Companion Document:** [RULES_ICE_HOCKEY.md](RULES_ICE_HOCKEY.md) (Foundational Ice Hockey Governance).

---

## 1. Scope & Primary Numerical Pipeline

This document defines the numerical prediction pipeline for the **National Hockey League (NHL)** and North American professional ice hockey (including AHL).

The core generative process is modeled as:

$$\text{Shot Attempts (Corsi)} \longrightarrow \text{Unblocked Shots (Fenwick)} \longrightarrow \text{Shot Quality / Expected Goals (xG)} \longrightarrow \text{Goals}$$

```text
Team 5v5 Shot Pace × Shooting Efficiency (xG)
                     +
Special Teams Opportunities (PP/PK) × Conversion Rate
                     +
Score Effects & Trailing Aggression
                     +
Goalie Save Quality Above Expected (GSAx)
                     +
Late-Game Pulled Goalie & Empty-Net Tail
                     │
                     ▼
  Joint Regulation Score Matrix (Home Goals, Away Goals)
                     │
                     ├── Regulation 1X2 Probabilities (Home / Draw / Away)
                     ├── Puck Line (-1.5 / +1.5) Probabilities
                     ├── Over / Under Goals PMF
                     └── Overtime / Shootout Branch → Full Game Moneyline
```

---

## 2. Invariants & Mechanics

### 2.1 Starting Goaltender Gate (Strict Mandatory Prerequisite)
- Goalies represent the single highest-variance individual factor in ice hockey.
- **Unconfirmed Goalie Rule**: If a starting goaltender is not confirmed via official team announcement, beat reporter morning skate report, or starting warm-up handshake, the model must evaluate an explicit **mixture distribution**:
  $$P(\text{Goals}) = p_{\text{starter}} \cdot P(\text{Goals} \mid \text{Starter}) + (1 - p_{\text{starter}}) \cdot P(\text{Goals} \mid \text{Backup})$$
- Totals on games with unconfirmed starters are strictly barred from Rank #1.

### 2.2 Regulation vs. Overtime/Shootout (Contract Geometry)
- **Regulation 60-Minute Contract**: Settles on the exact score at the end of the third period. Ties settle as `DRAW` on 1X2, or against the regulation line.
- **Full Game (OT/Shootout Included)**:
  - Any game tied after 60 minutes proceeds to 3-on-3 sudden-death overtime (5 minutes) followed by a 3-round shootout.
  - The winner receives exactly **one additional goal**.
  - **Mathematical Consequence**: Every game decided in OT/SO adds exactly 1 goal to an even score, resulting in an **odd total**:
    - A 2–2 tie becomes 3–2 (Total = 5, strictly Under 5.5).
    - A 3–3 tie becomes 4–3 (Total = 7, strictly Over 6.5).
  - Models must account for this discrete odd-number mass when pricing 5.5 and 6.5 full-game totals.

### 2.3 Empty-Net Goals and the Puck Line (-1.5 / +1.5)
- Trailing teams pull their goaltender for a 6-on-5 extra attacker typically with 1:30–2:30 remaining when trailing by 1 or 2 goals.
- **Empirical Base Rate**: Over 70% of two-goal regulation victories in the modern NHL feature an empty-net goal.
- **Puck Line Requirement**: A candidate recommending a $-1.5$ handicap must explicitly compute the probability of an empty-net conversion; candidates backing $+1.5$ must account for the empty-net kill risk.

---

## 3. Data Sources & Regime Controls

1. **Shot-Level Tracking**: MoneyPuck (`moneypuck.com`) 2007–08 to present.
   - Note: MoneyPuck excludes blocked shots from its shot-level tables. Corsi (total shot attempts) must be supplemented via NHL API play-by-play.
2. **Official Verification**: NHL Web API (`api-web.nhle.com/v1/gamecenter/{gameId}/boxscore`) provides official time on ice, starting goalies, empty-net indicators, and period scoring.
3. **Preseason Separation**: Preseason hockey displays 0.6–0.9 fewer goals per game due to split-squad rosters and conditioning. Never combine regular season and preseason training records without an explicit regime indicator.

