# Card and log templates, with the self-audit

**Opened 2026-09-28 (md-only operation).** Copy these templates. Fill every field, or write its missingness label; never delete a field. The self-audit in §5 is the current Markdown check. The field codes in [brackets] preserve the historical audit IDs.

**Core and annex (2026-09-28(e); `CURRENT_RULES.md` §B, "Timing").** The card is written in two blocks:
- **Core** (Fields 1–6 below, as marked): everything that sets a probability or a rank. It is frozen and appended to Part 6 **before the start**.
- **Annex** (§1A): disclosures computed from the frozen numbers. It is appended under the core afterwards, and may be written after the start. It never changes a frozen number.

---

## 1. The forecast card

```markdown
## <ID> — <Home> v <Away> (<competition>), <venue-local date>

### Field 1 — Identity and contract (core) [1]
- **ID:** <P-### or TMP-YYYYMMDD-LEAGUE-HOME-AWAY> · **Event IDs:** <feed name: id> (e.g. ESPN 401875252; MLB gamePk 822678)
- **Competition / stage / season type:** <…>
- **Venue:** <name, city, country> · **Start:** <venue-local time> (<IANA zone>) = <UTC> = **<AEST/AEDT time>** (<date rollover: yes/no>). User time <as given>: <verified / corrected>.
- **State at freeze:** <PREGAME / LIVE_ISSUED> (source, time)
- **Contracts (quarantined lines):** 1. <row as supplied> · 2. … · Period, overtime, extra time, tie, push and void terms: <…>
- **Method:** MDS-2026.09.28-v5.1 · <control revision named in METHOD.md> · manifest <CONTROL_MANIFEST_… .md>, SHA-256 <copied from the Current freeze receipt line at the top of GAME_LOG_STATUS_CURRENT.md>
- **UNIVERSE:** <mini-log universe table, date / event id> or OUT_OF_UNIVERSE [UV]

### Field 2 — Evidence and exposure, decisive rows (core) [7, 7r, 8]
| Fact | Value | Source (owner) | Retrieved (AEST) | Status |
|---|---|---|---|---|
| Home lineup / starters / goalie / pitcher | <names> | <official page> | <time> | CONFIRMED_OFFICIAL / PROJECTED_BEAT_VERIFIED (receipt below) / LINEUPS_NOT_YET_PUBLISHED / RETRIEVAL_MISS |
| Away lineup … | | | | |
| Bench / rotation / coach | | | | |
| Injuries, suspensions, rest | | | | |
| Weather (outdoor): match-window hourly | <temp, wind, rain %> | <Open-Meteo / BOM / NWS / MLB gamefeed> | | |
| Season rates (team, opponent) | | | | |

- **Participants per side:** <side A: lineup / bench / coach; side B: …>
- **S-1 Rev 2 receipt** (only where PROJECTED_BEAT_VERIFIED is claimed): outlet · reporter · timestamp · verbatim quote · second source.
- **Decision-driving players,** with quantified lines (minutes, usage, rate). A bare name is `AGGREGATE_ONLY`; list any sampling-noise flags.
- **Lineages for identity and state (three):** 1. … 2. … 3. …
- **Retrieval attempts** (required whenever a route failed; `SOURCES.md` §1.7, §3.12): `ROUTE <n> | <source> | <url/endpoint> | <time> | <OPENED / BLOCKED / JS_ONLY / STALE / WRONG_EVENT / NOT_PUBLISHED / RETRIEVAL_MISS> | <field or none> | <lineage>`, one per route, in the order tried.
- **Official social post used** (if any; `SOURCES.md` §1.8): platform · account · how authenticated (the organisation's site link, or its domain handle) · post URL/ID · published (exact, or a relative bound) · retrieved · verbatim text · field claimed · counted with lineage <n>.

### Field 3 — Joint distribution (core) [2, 3, BR, WB, T13, CVW]
- **Prior:** <source and number>. **Reference row:** <`BASE_RATES_REGISTER.md` §… row, n> or REFERENCE_BASE_RATE: NOT_YET_DERIVED.
- **TB-1-MD:** Oh … Dh … Oa … Da … → T = … , M = … (`PROBABILITY_TOOLKIT.md` §4; k, HE, widths from §4.3).
- **Named adjustments (signed, each with its mechanism):** 1. … 2. …
- **Centre / median / width:** total μ = …, median …, width σ = …; margin m = …, σ = … · **Reference width:** … (card/reference = …; below 0.85 names what the card knows).
- **Outcome-family table (masses sum to 1):**

| Family | Mass |
|---|---:|
| <e.g. home by 8+> | 0.xxx |
| <…> | 0.xxx |
| **Sum** | **1.000** |

- **Phase and team marginals:** <if phase or team rows exist>
- **Representative Rank-1 outcome:** <score>
- **Derivation of each row's p** (show the arithmetic, e.g. z = (188.5 − 182.5)/18.7 = 0.32 → Φ = 0.6255 → P(Over) = 0.374).
- **Tennis only:** dated Elo benchmark (Tennis Abstract, <date>, A <elo> v B <elo> → P = …) [T13].
- **Cricket only:** venue window by innings order, or INSUFFICIENT_VENUE_HISTORY [CVW]; TOSS STATUS; STRIP STATUS; conditions.

### Field 4 — Contract queries and ranks (core) [BP, TB, RM, 5b]
| Rank | Contract | p (UNVALIDATED_SUBJECTIVE) | BASELINE_P | TEAM_BASELINE_P | RM-1 q (or RM1_OUT_OF_DOMAIN) | Tier | Flags | Pair |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | | | | | | | | FORCED_PAIR / FREE / COVERING_PAIR |
| 2 | | | | | | | | |
| 3 | | | | | | | | |
| 4 | | | | | | | | |

- **TOP2_QUALITY:** <TOP2_STRONG / TOP2_SUPPORTED / TOP1_ONLY / TOP2_COIN_FLIP> (R1 q …, R2 q …; joint hit/failure probability: not estimated from q). Out of RM-1's domain: from p, labelled `(p tiers)`.
- **SIDE_FLIP in the top two:** <none> or "Rank <n>: the card's own probability for this row is <p>, below 0.5. It ranks here only through RM-1's historical recalibration" (+ the cushion-evidence sentence, `PROBABILITY_TOOLKIT.md` §5.3).
- **Preferred side of each over/under pair:** …; **push mass:** … (derived).
- **Predictability row:** <league: share of 0.70+ favourites, won %> (`BASE_RATES_REGISTER.md` §7.8).
- **Projected winner:** <team>, P = … (from the same distribution).

### Field 5 — Dependence (core) [5, 5a]
- **P(R1 ∧ R2)** = … (coupling: positive / negative / independent), read off the family table.
- **P(¬R1 ∧ ¬R2)** = … (the state that kills both: …); **P(all fail)** = … where three or more rows share a driver.
- **Checks:** complements sum to 1; nested lines monotone; P(−L) ≤ P(win) ≤ P(+L); family sum 1.000.

### Field 6 — Freeze (core)
- **Frozen at:** <AEST time> after the final refresh of <lineups / injuries / weather / state> at <time>. **Freeze − start:** −<minutes> min. **Supersedes:** <earlier pregame freeze time, or none>.
- **Self-audit (§5): all blocking items pass; core items listed.**
- **SHADOW:** NO_LANE (md-only)
```

### 1A. The annex (appended under the core after the freeze)

```markdown
### ANNEX (post-freeze, <AEST time>) — <ID>
No frozen p, q, rank, centre, width or mass is changed below. No in-game information is used.
- **Departure ledger** (anchor = TEAM_BASELINE_P where TB-1 has resolution, otherwise BASELINE_P): row 1 logit departure … = mechanism A (share …) + mechanism B (share …); unexplained share … [DL].
- **Track-record row:** <the sport's record from its §0 page>.
- **LOW_RESOLUTION:** <rows at 0.50–0.65>.
- **C-PLUS-CUSHION** (non-baseball +k.5): population cover rate …; P(underdog wins) … + P(loses by ≤ k) …; the named reason the margin stays inside k [PC].
- **Tennis games handicap:** P(win) …; implied P(margin ≥ k+1 | win) …; population conditional … [HC].
- **Complement decomposition** of R1 and R2 across the kill paths: … [4]
- **Kill paths, as weighted branches** (masses from the frozen family table): 1. <state> (mass …) → kills <rows>. 2. … [6]
- **Windows:** L5/L10/L15/L20 for both sides (descriptive), and head-to-head with a continuity note and unique-event count.
- **Alternatives (not ranked, not scored):** <contract, p from the frozen distribution>.
- **SLATE_ADVISORY (optional):** up to two same-event contracts at q ≥ 0.70.
- **Settlement route for every row:** <field owner + two independent lineages> [9]. **Retry trigger:** <if not final by …>.
- **Full source table:** every source consulted, with owner, time and OPENED / SNIPPET / ASSUMED.
- **CORE_DEFECT:** <none> or <what is wrong in the core; the core is still scored as issued>.
```

**What the user sees.** Deliver as soon as the core is frozen:
- the four ranked picks (with p, q and tier);
- any top-two `SIDE_FLIP` sentence;
- the projected winner;
- the decisive sources;
- one honest line on predictability. For example: "MLB slates have no STRONG favourites; these are coin flips", or "the supplied rows are two complementary pairs, so they will settle 2 W / 2 L whatever happens".

The annex follows in a second message.

---

## 2. The settlement block (appended under the card; the card is never edited)

```markdown
### Settlement — <ID> (settled <AEST time>)
**Terminal state:** FINAL, confirmed by 1. <field owner, URL, time> 2. <…> 3. <…>. Final score <…>; regulation score <…> where a contract is regulation-only.

**Process record (read from <endpoint>, retrieved <time>) [10, 10p]:** line score / quarter scores / innings / sets; disruption facts (injuries, red cards, sin bins, stoppages) with the minute and score. Classification: process failure / conversion / endpoint / disruption / variance.

**Lineup diff [10l, 10n]:** home k of n named starters started (<names on the card>); away …; any Rank-1 driver who did not play = PROCESS_DEFECT: LINEUP_CLAIM_FALSE.

**z [10z]:** z_total = (actual − centre)/width = …; z_margin = …

| Rank | Contract | Family | p | q | BASELINE_P | TEAM_BASELINE_P | Result | Brier(p) | Brier(q) |
|---:|---|---|---:|---:|---:|---:|---|---:|---:|
(p, q, BASELINE_P and TEAM_BASELINE_P are **copied from Field 4**, missingness labels included; never 0.500 in place of a missing value. Brier(q) is `T-RM1-PROSPECTIVE`'s row diagnostic only: write `EXCLUDED_PUSH` for a push-capable row, `—` for `RM1_OUT_OF_DOMAIN`, and `LIVE_ISSUED` for a card not issued pregame (`PROBABILITY_TOOLKIT.md` §10).)

**Projected winner:** <correct / wrong>. **Rank-1:** W/L. **Hit@2:** … (mechanical if it is a COVERING_PAIR). **Top over/under preferred side:** W/L/P → TOP_OU_REVIEW if L or P.

**Enhanced review** (Rank-1 loss, or top O/U loss or push): why it was ranked there; whether the pre-game evidence supported it; whether another row should have outranked it; which variable failed; whether an existing control applied and was executed; variance or rule change.

**Why each pick won or lost:** <row by row: what happened, which assumptions held, what the outcome turned on>.

**Validation questions:** 1. confirmed starting lineups obtained? 2. bench/rotation? 3. coaching info? 4. injuries, rest, late withdrawals? 5. were the sources accurate and current? 6. better sources available? 7. blind spots? 8. how to handle them next time? (Hindsight-only facts are not pre-game failures.)

**The three questions:** turned on … · knowable before issue? … (evidence) · smallest justified change … (TESTING only while the freeze holds).

**Kill paths:** which named states occurred, even if the row won.

**SHADOW [10s]:** NO_LANE (md-only)
```

---

## 3. Part 6 working continuation

**Append this session block after the original-source end marker** in `prediction logs/PREDICTION_LOG_COMBINED_6.md`. Keep its six section headings for new entries. Do not create a separate running file or alter the embedded P-518–P-522 source bytes.

```markdown
# Part 6 working continuation — <date AEST>

| Item | Value |
|---|---|
| Governing method | <method, control revision and scoring version from METHOD.md at session read> |
| Freeze with every card | <manifest name and SHA-256, copied from the Current freeze receipt line at the top of GAME_LOG_STATUS_CURRENT.md> |
| Session read (reading gate) | CURRENT_RULES.md; CARD_AND_LOG_TEMPLATES.md §1, §5; SOURCES.md §1 — read <AEST time> under receipt SHA <first 12 characters>. Re-read when the receipt SHA changes |
| Per-card reads | RULES_<SPORT>.md §0 (+ league rules file); SOURCES.md §3.x; Part 6's unsettled section; the Part 5 canonical snapshot |
| Next new prediction ID | <from Part 6 top custody note: P-523 then sequential; use TMP only for collision or unresolved identity> |
| Status | LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE |

## 0. Universe declarations
## 1. Incomplete / Unsettled Logs
## 2. Temporary-ID / Canonical-ID Conflict Logs
## 3. Fully Settled Logs
## 4. General Learnings, Rule Changes, Observations and New Sources
## 5. Document Update Mapping
```

- **After every query,** append the new card and annex in Part 6. If the file cannot be written, paste the full new entry without claiming it was logged.
- **Section 5 rows** read `| Item | Target file and section (or proposed new file and purpose) | Status: TODO / DONE / DECLINED (reason) |`.

---

## 4. Universe declaration (`C-EVENT-UNIVERSE`)

Write this before the day's first card, and never edit it afterwards:

```markdown
### UNIVERSE <venue-local date> — <league(s)> (declared <AEST time>, before any card that day)
| Event id | Home | Away | Start (AEST) | Disposition |
|---|---|---|---|---|
| <feed id> | | | | CARDED <ID> / SKIP: <reason, time> |
```

- Every event gets a disposition by settlement time.
- Choose leagues by predictability if you like (`BASE_RATES_REGISTER.md` §7.8), but declare them **before** researching events. Never choose event by event after research.

---

## 5. Self-audit (run at the core freeze, when the annex is appended, and at settlement)

**Blocking at the core freeze.** If any item fails, fix it or do not deliver. If it cannot pass before the start, the card is `LIVE_ISSUED`.
- [ ] B1. Identity verified with three lineages; venue-local, UTC and AEST times printed; state is PREGAME, or the card is labelled LIVE_ISSUED.
- [ ] B2. Contracts parsed exactly, with overtime, tie and push terms stated.
- [ ] B3. The family table has masses summing to 1.000 [2].
- [ ] B4. Centre and width printed, and each row's p derived from them with the arithmetic shown [3].
- [ ] B5. P(¬R1 ∧ ¬R2) printed, and P(all fail) where three or more rows share a driver [5a].
- [ ] B6. Participants per side (lineup, bench, coach) with their states; any PROJECTED_BEAT_VERIFIED has its receipt [7, 7r].
- [ ] B7. No market, fantasy or synthetic source used; every decisive fact is OPENED, not SNIPPET or ASSUMED.
- [ ] B8. Outdoor event: a match-window weather row. MLB total: the gamefeed wind (or WEATHER_NOT_YET_PUBLISHED).

**Required in the core.** A missing item caps the grade at LOW and is recorded as a process defect.
- [ ] R1. Method version, control revision and manifest SHA [1].
- [ ] R2. BASELINE_P beside every ranked row [BP].
- [ ] R3. TEAM_BASELINE_P, or its status (TB1_NO_RESOLUTION / NOT_COVERED / UNVALIDATED) [TB].
- [ ] R4. RM-1 q (or `RM1_OUT_OF_DOMAIN`), tier and flags per row; ranks by q (or by p out of domain); the TOP2_QUALITY line; the top-two SIDE_FLIP sentence where it applies [RM].
- [ ] R5. Predictability row.
- [ ] R6. Reference row [BR] and reference width [WB].
- [ ] R7. FORCED_PAIR / FREE / COVERING_PAIR labels, the preferred side, and push mass [5b].
- [ ] R8. P(R1 ∧ R2) with its coupling [5]; one representative Rank-1 outcome [6].
- [ ] R9. AGGREGATE_ONLY flags where they apply [8].
- [ ] R10. The UNIVERSE line or OUT_OF_UNIVERSE [UV].
- [ ] R11. Sport-specific:
  - tennis: the Elo benchmark [T13];
  - cricket: toss and strip statuses and the venue window [CVW];
  - non-baseball +k.5: the population cover rate as its BASELINE_P [PC].
- [ ] R12. The arithmetic checks in `PROBABILITY_TOOLKIT.md` §11.
- [ ] R13. The core is appended to Part 6 before delivery, with `Freeze − start`.

**Annex (§1A), before settlement.** A missing item is a process defect; it does not change the score.
- [ ] A1. Departure ledger [DL] and track-record row.
- [ ] A2. The complement decomposition [4] and kill paths with mass [6].
- [ ] A3. The settlement route for every row [9].
- [ ] A4. Narratives: the cushion decomposition [PC]; tennis handicap coherence [HC].
- [ ] A5. Windows, alternatives, the optional SLATE_ADVISORY, and the full source table.
- [ ] A6. `CORE_DEFECT` line (none, or the defect, with the core still scored as issued).

**At settlement.**
- [ ] S1. Three terminal lineages with an explicit final marker; no credible live source.
- [ ] S2. Process record read from a named endpoint with its time [10, 10p]; disruption facts; classification.
- [ ] S3. Lineup diff, "k of n", using names that are on the card [10l, 10n].
- [ ] S4. z_total and z_margin [10z].
- [ ] S5. Settlement table copied from Field 4 (p, q, baselines, missingness); Brier(p) on every row; Brier(q) only as the `T-RM1-PROSPECTIVE` diagnostic, with its exclusions.
- [ ] S6. Enhanced review for a Rank-1 loss or a top-O/U loss or push; the three questions; kill paths checked.
- [ ] S7. The SHADOW line [10s].
- [ ] S8. Ledger row appended (§6); universe dispositions complete; document-mapping rows added.
- [ ] S9. The annex is complete (A1–A6), or its absence is recorded as a process defect. Any lesson is parked (`LEARNINGS_INDEX.md` §10), not promoted, while the rule inventory is closed.

---

## 6. Ledger rows

**`SKILL_BASELINE_LEDGER.md`, "Prospective rows" section.** Append one row per issued decision, at settlement. A forced pair counts once, as the higher-ranked row. A covering pair counts as two rows.

```markdown
| Decision | Card | Rank | Contract (as issued) | Family | Card p | Baseline p | Baseline population (leak-free) | Result |
|---|---|---|---|---|---:|---:|---|---|
| <ID>-<short> | <ID> | 1 | <copied> | total / handicap / moneyline / phase | 0.xxx | 0.xxx or NOT_YET_DERIVED | <league season before the event, n> | W / L / P |
```

- Rows whose baseline is `NOT_YET_DERIVED` are listed but not scored.
- **Counting toward `C-BASELINE-SKILL`:** exactly the rows defined in `SKILL_BASELINE_LEDGER.md` rule 7 (prospective, verified pregame core freeze, numeric issue-time BASELINE_P, three terminal lineages).
- **`MARKET_BENCHMARK_LEDGER.md`** is written by the operator only, after settlement. The model never reads or writes it.

---

## 7. Promoting Part 6 working entries to canonical custody (maintainer session)

1. **Inventory.** List every working entry in Part 6 (and any supplied attachment or Drive copy): its ID, event, state and whether it is already in Parts 1–5. Fingerprint duplicates.
2. **Identity.** Check each event on four fields: date, venue, home/away and starters. Duplicates of one event are merged as views. Distinct events are never merged.
3. **IDs.**
   - New cards continue at P-523 in issue order by explicit user instruction. Resolve a collision by event identity and issue timestamp; keep P-518–P-522 under their separate audit until certified.
   - Keep TMP IDs as aliases. Never overwrite or renumber.
   - Conflicts go to the conflict section with full settlement.
4. **State.** Unresolved events stay pending, with the state and the time checked. Only finals are settled (§2).
5. **Preserve issue text.** The original entry stays in Part 6. Append custody or settlement corrections there with the old and new values, source and reason; never replace a frozen issue. Mark an entry canonical only after the identity, issue-time and source gates pass.
6. **Learnings.** While the rule inventory is closed (`CURRENT_RULES.md` §D9), a lesson is parked as one line in `LEARNINGS_INDEX.md` §10. Only validity repairs and user-instructed changes get a `LEARNING_REGISTER.md` disposition. Execute or disposition every document-mapping row.
7. **Custody and check.**
   - Preserve Part 6's embedded original-source block and track pending events in `GAME_LOG_STATUS_CURRENT.md`.
   - Update the Part 5/Part 6 top custody notes and status register: next ID and open follow-ups.
   - Maintainers then review the Markdown records and receipt (`CONTRIBUTING.md`).
