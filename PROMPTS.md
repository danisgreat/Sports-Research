# Prompts — paste these into the chat that runs the forecasts

**2026-09-29 pipeline instruction for P-523+:** Apply [the pipeline gate register](PIPELINE_IMPLEMENTATION_2026-09-29.md) before the historical prompts below. A numerical card derives every contract from one versioned distribution, prints same-contract baselines and exact settlement endpoints, and ranks by issued p. Tier C and unsupported competitions take `NO_MODEL / NO_FORECAST_ISSUED`. Closing odds are allowed only after terminal settlement as a separate benchmark and never enter a forecast.

**Opened 2026-09-28.** These are historical standard prompts; for P-523+ apply the pipeline amendment above. The chat can use the linked Drive, root Markdown rules and the user-authorized `research/` code/data workspace. Fill in the angle brackets.

Notes for the operator:
- **The supplied rows are usually complementary pairs.** Bullets −1.5 with Hawks +1.5, or Over with Under the same line, always settle 2 W / 2 L. Tigers ML with Bay Stars +1.5 is a covering pair: at least one always wins. The prompts ask for the labels, so the arithmetic is never read as skill.
- **"Take as long as needed" and "pregame" are compatible.** The model freezes the card's **core** (everything that sets a probability or rank) by about 5 minutes before the start, and writes the **annex** (disclosures) afterwards (`CURRENT_RULES.md` §B, "Timing"). Send requests at least 90 minutes before the start where you can. A core frozen after the start is `LIVE_ISSUED` and kept out of pregame scoring.
- **Never paste passwords, codes or keys into a prompt.**

---

## 1. Continue the six-part combined log

```text
Continue the sports prediction framework in prediction logs/PREDICTION_LOG_COMBINED_6.md. Do not create another running or mini log.

Read CURRENT_RULES.md, CARD_AND_LOG_TEMPLATES.md, PROBABILITY_TOOLKIT.md, SOURCES.md, the Part 5 top snapshot and the Part 6 controlling custody note. Record the read time and the freeze receipt SHA in a new Part 6 working section after the original-source end marker. Never change the embedded P-518 to P-522 source block.

Before each prediction, read the relevant sport file and source section. Reconcile event identity and the current queue. P-518 to P-522 stay reserved under audit; the next new prediction ID is P-523 by explicit user instruction, then increment in issue order. Use TMP-YYYYMMDD-LEAGUE-HOME-AWAY only for a collision or unresolved identity; do not infer that the earlier five records have been certified.

For each game, append the frozen core before the start, then its annex and sources. Use the universe, unsettled, conflict, settled, learnings and document-mapping headings in CARD_AND_LOG_TEMPLATES.md section 3. If you cannot write to Part 6, paste the complete new entry and state clearly that it was not logged.

Keep SPORTS_ONLY / MARKET_BLIND. Never guess a fact, silently change a contract, count a copied source twice, or treat the original block's fully-settled claims as verified. The current P-523 instruction comes from the user, independent of that block.
```

---

## 2. One game (the template, then paste the sport add-on)

```text
Upcoming <SPORT> event: <Team A> vs <Team B>, <Competition>
Estimated start: <date>, <time> AEST (verify it; it can move)

Supplied contracts:
<row 1>
<row 2>
<row 3>
<row 4>

Research and card this event under the framework in the linked Drive, using its Markdown documents only (no Python, no non-Markdown files).
- Pass the reading gate first: CURRENT_RULES.md §0.
- Follow the workflow in CURRENT_RULES.md §B.
- Use the card template in CARD_AND_LOG_TEMPLATES.md §1, and do all arithmetic with PROBABILITY_TOOLKIT.md.

1. Identity and state.
   - Confirm the teams, competition, venue and venue-local start; convert to AEST.
   - Classify the state from the official feed.
   - Flag any contract that looks wrong.
2. Participants.
   - Get the latest official lineups, starters, bench or rotation, injuries, suspensions, rest decisions and coaching news, each with its fetch time.
   - An official lineup beats a projected one.
   - Mark anything unconfirmed.
3. Environment. For an outdoor event, get the hourly forecast at the venue for the match window.
4. Evidence.
   - Use game logs before aggregates; the season rate plus the opponent.
   - Use the SOURCES.md lanes for this sport, and more than one lineage for every decisive fact.
   - For each missing field, record the failed route and time as an attempt-ledger line, then immediately open the next route in the failed source's row in SOURCES.md §3.12, then §1.7 and §3.11. Distinguish not yet published from inaccessible, stale and wrong-event pages; recheck the field owner at the final refresh.
   - Official social lanes are the accounts listed in SOURCES.md §3.12, read through the §1.8 routes: X timeline or oembed, Bluesky author feed, YouTube watch page, Threads through the proxy. Never use an account that is not authenticated from the organisation's own site or domain.
   - An original official social post may establish only the announcing organisation's own field if its account, exact post, contents and pre-issue time are verified (SOURCES.md §1.8). Count it with that organisation's website as one lineage; otherwise treat it as discovery only.
   - Stay market-blind.
5. Baselines and distribution.
   - Print BASELINE_P and TEAM_BASELINE_P: TB-1-MD by hand from the standings (PROBABILITY_TOOLKIT.md §4).
   - Build one joint distribution, and print the reference row and width.
   - Show the arithmetic from the distribution to each row's probability.
6. Rank.
   - RM-1 q for each row (PROBABILITY_TOOLKIT.md §5); rank by q, with #1 the most likely. If the sport is outside RM-1's eight sport groups (§5.0), print RM1_OUT_OF_DOMAIN and rank by p.
   - Print the tier, the flags and TOP2_QUALITY. If a SIDE_FLIP row is in the top two, say plainly that the card's own probability for it is below 0.5.
   - Label FORCED_PAIR / COVERING_PAIR, and give P(R1 and R2) and P(both fail) from the probabilities p.
   - Print the league's predictability row. Say plainly when the slate cannot produce a STRONG Rank 1, or when the supplied rows are complementary pairs.
   - You may add rows of your own. Price them from the same distribution and label them as additions.
7. Give the projected winner with its probability. List more-likely alternative contracts separately, priced from the same distribution and unranked.
8. Timing (CURRENT_RULES.md §B, "Timing").
   - Build the core first: everything in steps 1–7 that sets a probability or a rank.
   - Refresh lineups and news 30–5 minutes before the start, and freeze the core by 5 minutes before. You may re-freeze before the start if the official lineup lands; the last pregame freeze is the issue.
   - After the freeze, write the annex (CARD_AND_LOG_TEMPLATES.md §1A): departure ledger, kill paths, windows, alternatives, settlement routes, the full source table. The annex never changes a frozen number and uses no in-game information.
   - If the core cannot pass the blocking audit before the start, label the card LIVE_ISSUED.
9. Run the self-audit's core items (CARD_AND_LOG_TEMPLATES.md §5). Append the core after the original-source end marker in Part 6 before delivering it; then append the annex and give the new entry.

Never fabricate or guess. Say what you could not confirm. No retrospective yet.
```

**Sport add-ons:**

```text
BASKETBALL (NBL / NBA / WNBA / EuroLeague / ACB / FIBA):
- Get the official starters and injury report with fetch times.
- The NBL tip is the first jumpBall event.
- TB-1-MD from the ESPN standings (NBL k 5; NBA/WNBA k 2).
- The weaker team's +1.5 to +3.5 covers only 0.32–0.45: give the C-PLUS-CUSHION decomposition.
- For a total within about 12 points of the line, keep overtime (about 5% of games, +25 points) as explicit mass.
```
```text
CRICKET (T20 / CPL / IPL / BBL):
- Get the toss and the confirmed XIs after the toss.
- "1st innings" means the team batting first; say what happens to the contract if the named team bats second.
- Toss, strip and conditions are separate fields with their own ladders (SOURCES.md §3.3).
- Get the pitch report from P1–P5 sources, and the dew and weather in the match window.
- Before the toss, phase totals are a bat-first/chase mixture. The chasing side's total is capped near the target.
```
```text
BASEBALL (MLB / NPB / KBO / CPBL):
- Get the probable starters and official batting orders, with fetch times, and the bullpen usage over the last 3 days.
- MLB weather comes from the statsapi gamefeed (field-relative wind), never a city forecast.
- Totals come from the negative binomial tables; run lines from the home/away shares (PROBABILITY_TOOLKIT.md §3).
- NPB and KBO games can end tied: state P(tie), and how each row settles on a tie.
- MLB has no STRONG favourites: say so.
```
```text
AFL / AFLW:
- Get the official team lineups (ins, outs, emergencies; final changes about an hour before the bounce) and the venue weather.
- Men's AFL sides anchor on TB-1-MD (k 2, home edge +6.6, margin width 36.8). AFLW is a separate population: its widths are NOT_YET_DERIVED, and it anchors on the population.
```
```text
NRL / RUGBY:
- Get the official team lists (Tuesday, then the final 1–17 about an hour before kick-off) and the venue weather.
- NRL sides and totals anchor on the population; print TB-1-MD as a reference only.
- Favourites stated at 0.70–0.80 have been over-confident.
```
```text
SOCCER:
- The club's official XI (about 60 minutes before kick-off) beats predicted lineups.
- Say whether each row settles on 90 minutes or includes extra time.
- Use the Poisson tables for results, handicaps and totals.
- Results anchor on TB-1-MD in the EPL, La Liga, the Bundesliga, Serie A and Ligue 1. Totals anchor on it in La Liga and the Bundesliga, and on the population elsewhere.
- Three-way results rarely reach 0.70.
```
```text
ICE HOCKEY (NHL):
- Get the confirmed starting goalie (preseason goalies stay projected).
- State whether each row includes overtime and the shoot-out.
- Totals use the Poisson table with the odd-total overtime structure.
- The puck line −1.5 = P(win) × 0.568.
- Preseason totals are 5.3–5.7.
```
```text
TENNIS:
- Get withdrawals, retirements, workload and the surface.
- Print the dated Tennis Abstract Elo (overall and surface) and the Elo probability. Explain any gap above 10 points.
- Give P(deciding set) against the 0.340 reference, and the handicap coherence check.
- State the retirement settlement rule for every row.
```
```text
NFL:
- Get the official inactives (about 90 minutes before kickoff), QB status and the weather.
- Sides anchor on TB-1-MD; totals on the population.
- Account for the key-number mass at 3 and 7.
- A model favourite at 0.70–0.80 has won about 2 in 3.
```

---

## 3. Settle current Part 6 entries

```text
Settle every eligible entry in Part 6 that is no longer live, following CURRENT_RULES.md §D8 and CARD_AND_LOG_TEMPLATES.md §2 in the linked Drive, using its Markdown documents only. Append only to Part 6; preserve its embedded original source block.

1. State: classify each entry from the official feed. Settle only FINAL events where every row can be settled; everything else stays in Incomplete / Unsettled, with its state and the time checked.
2. Settlement:
   - three terminal lineages with an explicit final marker (SOURCES.md settlement lineages). Never settle from match reports or AI-written recaps;
   - settle each row on its exact contract; settle the projected winner separately;
   - read the process record from a named endpoint;
   - the lineup diff uses names that are on the card;
   - z-scores;
   - copy p, q, BASELINE_P and TEAM_BASELINE_P from the issued card exactly. Never write 0.500 for a missing baseline;
   - never edit the issued card.
3. Retrospective for each settled event:
   - why each pick won or lost;
   - the enhanced review for a Rank-1 loss or a top over/under loss or push;
   - top-two review (mechanical results labelled);
   - totals review;
   - what went right;
   - blind spots, and whether each was knowable before the start;
   - the eight validation questions;
   - the three questions;
   - which kill paths occurred.
4. Link each finding to LEARNINGS_INDEX.md and the recurring mistakes (M1–M35). Classify it as one-off, sport-specific or cross-sport. The rule inventory is closed until the checkpoints report: a proposed rule or test is parked as one line for LEARNINGS_INDEX.md §10, and no single game creates a rule.
5. Sources: assess accuracy and timeliness, and record new reliable sources with their route and role.
6. IDs: check the Part 5 snapshot for conflicts. Give any conflicting entry a TMP ID in the conflict section, fully settled.
7. Append a SKILL_BASELINE_LEDGER-format row for each settled decision (CARD_AND_LOG_TEMPLATES.md §6) in Part 6's learnings section.

Return the new Part 6 entries in their section order, then two lists:
- settled entries, first to last;
- entries still awaiting settlement, first to last, each with its reason.

Status stays LEARNING_ONLY. Accuracy and honesty come before favourable-looking results.
```

---

## 4. Reconcile Part 6 working entries, then audit (repository session)

```text
Reconcile Part 6 working entries under CARD_AND_LOG_TEMPLATES.md §7, then audit entries eligible for canonical custody. The forecasting rules are Markdown-only. Do all record and rule work in the .md files. Maintainer tooling (the CI checks and the control manifest) runs last, and only in a repository session that can run it.

1. Integrity check before any edit: inventory, identity on four fields, duplicates, existing entries, and the state of every event. Unresolved events stay pending and tracked.
2. Keep original entries in Part 6. Append custody and settlement corrections there, never overwrite issue text. Assign canonical IDs from the snapshot, with the timestamped card taking the lower number; keep TMP IDs as aliases.
3. Audit each event:
   - why each pick won or lost (expected against actual game script, lineups, roles, pace, tactics, availability and conditions);
   - the enhanced Rank-1 review; top-two reliability; totals;
   - the lineup and coaching audit; the source audit and new sources;
   - blind spots, with whether each was available pre-game; links to earlier lessons; what went right.
4. Across the batch, compute from the logs (show the arithmetic):
   - Rank-1 and top-two records by q tier;
   - Brier for p and BASELINE_P on the same decisions (SKILL_BASELINE_LEDGER.md), and separately Brier(q) against Brier(p) as the T-RM1-PROSPECTIVE diagnostic (SCORING_AND_VALIDATION.md §15 admission rules);
   - results by league against its predictability row;
   - covering and forced pairs reported separately.
   Every figure carries its n.
5. Turn findings into documents under the rule freeze:
   - validity repairs may be applied;
   - the rule inventory is closed until the checkpoints report (CURRENT_RULES.md §D9): any new control, test, flag or predictive idea is parked as one line in LEARNINGS_INDEX.md §10, with its evidence pointer;
   - a MODEL_CHANGE happens only if I instruct it after seeing the evidence, and only if it passes a preregistered held-out test.
   - Put sport findings in the sport file's §0, cross-sport findings in CURRENT_RULES.md, and new sources in SOURCES.md.
   - Execute or disposition every document-mapping row.
6. Custody:
   - update the Part 5 and Part 6 top custody notes and GAME_LOG_STATUS_CURRENT.md;
   - preserve the original P-518 to P-522 source block in Part 6 and track pending events;
   - add a CHANGELOG entry.
7. Maintainer step (a repository session only): update and verify the Markdown control manifest and review the changed files (`CONTRIBUTING.md`). Push `main` when the user has authorized publication.

Validate every item in CARD_AND_LOG_TEMPLATES.md §5 (settlement block) for each event. Then report under these headings: settled and appended · still unsettled (why) · temporary IDs · files updated · changes (with category) · tests opened · new sources · major learnings · outstanding issues. Don't hide pre-game mistakes, force explanations to fit results, or invent anything.
```

---

## 5. Look for model improvements in the settled record

```text
Review all completed and settled logs, and find what could genuinely improve the probabilities, rankings, baselines or research procedure. Use the Markdown records and documents only.

1. From the settled cards, compute by hand (show the arithmetic, with n and a rough interval):
   - calibration by probability band (0.50–0.60, 0.60–0.70, 0.70+);
   - Rank-1 and top-two rates by RM-1 q tier;
   - card against BASELINE_P and TEAM_BASELINE_P on the same decisions;
   - results by sport and contract family;
   - forced and covering pairs separately.
2. List each candidate improvement: the problem, the evidence, and the exact change.
3. The bar for any change that moves a probability, rank, width or centre (the user's standing instruction):
   - preregister the hypothesis and decision rule first;
   - test on held-out games that did not suggest it;
   - the improvement needs a 95% interval entirely below 0 in every independent window.
   Tests that need code are run by a maintainer session and reported back as Markdown. While the rule inventory is closed (CURRENT_RULES.md §D9), a candidate is parked in LEARNINGS_INDEX.md §10 unless I explicitly instruct otherwise.
4. Apply only what qualifies:
   - validity repairs and disclosure or measurement controls may be applied now;
   - anything else is reported to me with its evidence, and waits for my explicit instruction.
5. Record everything:
   - LEARNING_REGISTER.md and LEARNINGS_INDEX.md;
   - the sport §0 pages; CURRENT_RULES.md for cross-sport items;
   - BASE_RATES_REGISTER.md for new reference rows;
   - CHANGELOG.md.
   Create a new Markdown document only where no existing one fits.

Report what qualified, what failed and why, and what I need to decide.
```
