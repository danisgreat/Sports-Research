# P-272 — Geelong Cats vs Carlton — 2026 AFL Finals Elimination Final

## 1. Frozen identity, state and contracts

- **Canonical ID:** `P-272`
- **Sport:** Australian rules football
- **Competition:** 2026 Toyota AFL Premiership, Elimination Final
- **Event:** Geelong Cats vs Carlton
- **Venue:** Melbourne Cricket Ground, Melbourne
- **Scheduled bounce:** Friday 4 September 2026, 7:40 pm AEST
- **Information/state cutoff:** **2026-09-04 19:33:09 AEST**
- **Cutoff invariant:** PASS — approximately 6 minutes 51 seconds before scheduled bounce
- **Game state:** `PREGAME`
- **AFL current-state evidence:** official AFL live article headline stated final teams were in; no game score had begun in the frozen source state
- **Operator:** not supplied
- **Draw / extra-time / settlement terms:** `UNKNOWN_DEFINITION`; operator-specific terms were not supplied
- **Retrospective:** **NO**

### User-supplied exact slate

| Contract ID | Contract | Ordinary full-game geometry |
|---|---|---|
| `P-272-C01` | **Geelong +11.5** | Wins if Geelong wins/draws or loses by 1–11 |
| `P-272-C02` | **Carlton -11.5** | Wins if Carlton wins by 12+ |
| `P-272-C03` | **Combined Over 165.5** | Wins at 166+ total points |
| `P-272-C04` | **Combined Under 165.5** | Wins at 165 or fewer total points |

---

## 2. Governing AFL process applied

The active AFL framework requires the forecast to be built from the current scoring chain rather than from raw points averages or head-to-head alone:

`clearance / turnover / intercept -> inside-50 -> scoring-shot creation and quality -> conversion`

Key controls applied:
- current shot-chain and territory evidence outranks old scoring/H2H;
- winner and handicap are separate thresholds;
- conversion is less stable than territory/shot creation;
- low/close, low/separation, high/close and high/separation branches are all tested;
- a streak is used only after assessing whether its mechanism persists;
- the latest meeting is reconciled rather than copied forward automatically;
- weather does not create an automatic Under;
- every contract is derived from one coherent game corridor.

---

## 3. Current selection and availability

### Geelong
Official club selection named:
- **IN:** Max Holmes, Mark Blicavs, Oli Wiltshire
- **OUT:** Jack Martin, Sam De Koning, Jhye Clark, all omitted
- Holmes was named for his first AFL game since Round 19.
- Blicavs returns after being managed in Round 24.

**Mechanism impact:** Holmes restores high-end run and transition speed, while Blicavs adds structural flexibility around stoppage, wing and defensive coverage. Holmes' layoff also adds uncertainty because his full-match workload and sharpness cannot simply be assumed.

### Carlton
Official club selection named:
- **IN:** Wade Derksen
- **OUT:** Nick Haynes, injured
- **Will Hayward:** unavailable after failing to get through main training

**Mechanism impact:** losing Haynes removes an experienced defensive option against a Geelong forward group with multiple tall/medium scoring threats. Hayward's absence removes another forward option. Carlton otherwise retained a settled side.

### Final-team limitation
The official AFL live article confirmed that final teams were in, but its static text did not expose a complete readable late-change/interchange table in the frozen capture. Therefore **no additional late change is asserted** beyond the official club selections above.

---

## 4. Form and regime audit

### Geelong
- Entered finals on **six consecutive wins by an average margin of 35 points**.
- Important qualification: the AFL's own preview notes those six wins came against teams now out of contention.
- In the second half of the season, Geelong had **three losses from three against top-six opponents**, plus the loss to Carlton.
- Geelong's current process profile is elite: **1st in forward-half intercepts, inside-50 differential and points from the forward half**.
- Jeremy Cameron returned in Round 24 after missing five consecutive wins through a shoulder injury and had 22 disposals. Shannon Neale had 47 goals for the season and Ollie Henry 42.

**Interpretation:** the six-win streak is real but cannot be carried forward as a simple "hot team" coefficient. Its competition-quality limitation is material. The stronger reusable signal is Geelong's persistent ability to win territory and lock the ball in its front half.

### Carlton
- After a 1–8 start, the Blues produced an **11–1–2 record across the next 14 matches** during their revival.
- In the wildcard win over Melbourne, Carlton kicked **nine goals to three after quarter-time**.
- Since Josh Fraser took charge, Carlton had been the **second-stingiest side**, conceding about **75 points per game across 15 matches**.
- During that revival period, Carlton ranked **4th for defensive-50-to-inside-50 against** and **3rd for scores per inside-50 against**.
- Sam Walsh produced 39 disposals, seven clearances, seven score involvements and five inside-50s against Melbourne; his five-final career disposal average was 32.4.

**Interpretation:** Carlton's turnaround has a tangible mechanism: stronger possession control, transition and defensive efficiency rather than a bare win streak. That makes the Blues a genuine winner/separation threat.

---

## 5. Most-recent-meeting reconciliation

**Round 12, 2026 at the MCG: Carlton 12.16 (88) defeated Geelong 12.12 (84). Total: 172.**

The relevant mechanism was not merely the four-point final margin:
- Geelong led by 20 points midway through the second quarter.
- Carlton changed the shape of the game by moving the ball with more speed and changing angles.
- In the decisive late sequence Carlton won the clearance, went deep inside 50 and Patrick Cripps converted the response.

### What persists
Carlton's possession/transition identity and ability to escape a high press are still live and are directly relevant against Geelong's forward-half pressure.

### What changed
- Geelong now has Holmes and Blicavs back in the selected side.
- Carlton is without Haynes and Hayward.
- Geelong has had the week off; Carlton comes in on a six-day break after the wildcard final.
- Geelong's current forward-half territory profile remains competition-leading.

**Conclusion:** the May result is a real Carlton matchup warning, but it is not sufficient to project Carlton to a 12+ win automatically.

---

## 6. Weather and surface gate

- Current Melbourne conditions at the freeze were cloudy and cool.
- BOM's Melbourne/Olympic Park observation at 5:40 pm recorded approximately **15.2°C, northerly wind 24 km/h with gusts to 35 km/h, and 0 mm rain since 9 am**.
- The broader Melbourne forecast was mostly cloudy and breezy.
- A severe-wind warning existed for parts of Victoria, but the warning text's damaging-wind timing/locations did **not** justify treating the MCG game itself as a damaging-wind event at the pre-game cutoff.
- **Current MCG turf/surface condition:** `NOT independently verified from an official current surface report`.

**Forecast implication:** some breeze increases kicking/ball-use variance, but the evidence does **not** support a weather-driven automatic Under.

---

## 7. Qualitative game corridor

Because no fitted or validated numerical model exists, this is a qualitative scenario corridor rather than a published probability distribution.

### Lower-scoring / control branch
**Approximate total family: 145–160**
- Carlton's improved defensive-50 control reduces clean Geelong shots.
- Finals pressure and possession control slow repeat scoring chains.
- Geelong still wins enough territory to prevent a large Carlton separation.

### Central branch
**Approximate total family: 158–174**
- Geelong wins more forward-half territory.
- Carlton still generates transition exits and periods of possession control.
- The margin remains mostly within about 10 points either way, with a slight Geelong game-winner lean.

### High-scoring branch
**Approximate total family: 176–190+**
- Geelong pressure creates repeated short-field shots and Carlton also breaks the press into open transition.
- Carlton's loss of Haynes is exposed by Geelong's Cameron/Neale/Henry forward mix.
- Conversion runs above ordinary expectation.

### Carlton separation / kill path
Carlton -11.5 becomes the leading outcome if Carlton repeatedly beats Geelong's first pressure layer, wins the important centre-clearance moments and forces the Cats into inefficient chase/transition defence, while Geelong's weaker record against high-end opposition proves more representative than its six-win close to the season.

### Geelong separation branch
Geelong can also create a 12+ margin if its league-leading forward-half intercept and inside-50 profile overwhelms Carlton's exits and Carlton's depleted defensive personnel cannot absorb the repeat-entry load.

---

## 8. Ranked forecast — exact supplied contracts

| Rank | Contract | Forecast status | Why it ranks here |
|---:|---|---|---|
| **1** | **Geelong +11.5** | **BEST / strongest relative lean** | The most robust contract across the central game tree. It survives a Geelong win, a draw, and Carlton wins by up to 11. Carlton's current regime and same-venue H2H make a Blues win plausible, but they do not make a 12+ separation the central requirement. Geelong's territory profile, week off and returning Holmes/Blicavs provide several independent paths to staying inside the cushion. |
| **2** | **Under 165.5** | **LEAN — lower confidence than Rank #1** | Carlton's defensive revival and elimination-final pressure support a lower-scoring path. However 165.5 sits inside the central corridor, the most recent H2H totalled 172, Geelong's forward-half scoring engine is strong and Carlton is missing Haynes. This is therefore only a modest directional edge, not a high-confidence Under. |
| **3** | **Over 165.5** | **LIVE ALTERNATIVE / slightly below Under** | The Over has a credible route through Geelong repeat entries, Carlton transition scoring and the weakened Carlton defensive matchup. It ranks just below the Under because Carlton's recent defensive control and finals context modestly favour a more compressed scoring environment. The total threshold remains central and uncertain. |
| **4** | **Carlton -11.5** | **LEAST LIKELY of supplied rows** | Carlton can absolutely win, but this contract specifically needs 12+ points. The strongest Carlton evidence supports matchup competitiveness and a viable winner branch more clearly than it supports sustained separation. Geelong +11.5 and Carlton -11.5 are not equivalent to the winner call. |

---

## 9. Potential game winner

### **Geelong Cats — narrow lean**

The winner call is deliberately weaker than Rank #1 Geelong +11.5.

The deciding factors are:
1. Geelong's league-leading forward-half intercept, inside-50 differential and forward-half scoring structure.
2. A week off versus Carlton's six-day turnaround.
3. Holmes and Blicavs returning.
4. Carlton's Haynes/Hayward absences.
5. Carlton's transition and defensive revival remains a strong adverse branch, which is why the winner call is **narrow rather than strong**.

**Representative central score shape only, not a model projection:** Geelong by roughly one to two goals, with the total clustering near the 165.5 threshold.

---

## 10. Evidence quality and limitations

- **Identity / venue / start:** HIGH — official AFL.
- **Selected-team changes:** HIGH — official club sources.
- **Final-team status:** HIGH for "final teams in"; MEDIUM for exact late-change detail because the static live article did not render the full final team table.
- **Current tactical/form profile:** HIGH/MEDIUM-HIGH — official AFL analytical preview and official match centre.
- **Weather:** HIGH for observed Melbourne/Olympic Park conditions; current MCG turf condition not independently verified.
- **Full L5/L10/L15/L20 exact threshold hit-rate reconstruction:** **NOT COMPLETED from an official stat feed before the pre-bounce cutoff.** No hit rates are invented. Current-regime summaries and the most recent meeting are used descriptively instead.
- **Operator settlement rules:** UNKNOWN.
- **Validated probabilities / edge / ROI / staking:** NOT AVAILABLE / NOT AUTHORISED.

---

# SOURCE REGISTER — P-272

## A. Google Drive governing framework, read-only
1. `PREDICTION_LOG_COMBINED_2.md` — active canonical log; P-272 next ID at opening; probability/value gates and append rules.
2. `README.md` — active workflow, source order, pre-game cutoff, corridor and settlement workflow.
3. `LEARNING_REGISTER.md` — current v3.4 method state and promoted controls, including AFL scoring-chain/coherence/streak/most-recent-meeting controls.
4. `RULES_AFL.md` — AFL identity, participant, territory, scoring-chain, context, branch and source rules.
5. `MODEL_AND_DATA_SPEC.md` — method-version history through MDS-2026.09.04-v3.4 and numerical publication boundary.

**Drive modification:** NONE.

## B. Official AFL / club sources
1. AFL — Finals week-two fixture:  
   https://www.afl.com.au/news/1597385/finals-fixture-ticket-details-schedule-confirmed-for-week-two-of-the-2026-finals-series

2. AFL — Elimination Final mega-preview, current form, tactical rankings, H2H, player context:  
   https://www.afl.com.au/news/1600128/mega-preview-cats-v-blues-stats-that-matter-who-wins-and-why

3. AFL — Current live pre-game article confirming final-team state:  
   https://www.afl.com.au/news/1601434/live-cats-take-on-hot-blues-in-elimination-final-blockbuster-at-the-g

4. AFL — Round 12 Carlton v Geelong official match centre and match report:  
   https://www.afl.com.au/afl/matches/8140

5. Geelong Cats — official elimination-final team selection:  
   https://www.geelongcats.com.au/news/2119044/afl-team-selection-cats-make-three-changes-for-elimination-final

6. Carlton — official elimination-final team news:  
   https://www.carltonfc.com.au/news/2119507/afl-team-news-one-change-for-cats-elimination-final

## C. Weather
1. Australian Bureau of Meteorology — Melbourne (Olympic Park) observations / current observation feed:  
   https://www.bom.gov.au/products/IDV60801/IDV60801.95936.shtml

2. Current Melbourne forecast card retrieved in-session at 19:31 AEST, including current cloudy conditions and the contemporaneous BOM severe-weather warning text.

---

# NEXT-QUERY OPERATING RULE

1. Keep every incomplete/unsettled card in the **UNSETTLED / INCOMPLETE QUEUE** at the top.
2. On the next query, state-check P-272 first.
3. If P-272 is final, perform settlement only unless the user explicitly asks for retrospective analysis; the user explicitly said **do not do a retrospective yet** for this card.
4. Once settled, move P-272 from the top unsettled queue into the normal settled chronology.
5. Preserve the frozen forecast unchanged.
6. Record every source used for settlement or any future analysis.
7. Re-read the current Drive method/version before issuing the next canonical local card.
8. Next local forecast ID: **P-273**, subject to reconciliation with the current Drive canonical snapshot.

---

