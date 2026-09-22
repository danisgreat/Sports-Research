# Base-rates register

**Opened 2026-09-17(b).** Single home for **published base rates used as identity inputs** to a card's arithmetic.

## What belongs here, and what does not

Historical field-owner frequencies belong here with numerator/denominator, exact population, endpoint, retrieval date, query, missingness and uncertainty. They are empirical estimates, even when calculated without a fitted regression. They can inform an explicitly weighted prior or baseline; they are not mathematical identity inputs that every matchup must share. Numbers below are preserved from the prior retrieval and were not independently re-fetched in this correction. No universal run-line ceiling, push cap, variance floor or automatic rank bar follows from them. See SCORING_AND_VALIDATION and RULES_GENERAL G-L24.

## Why it exists

Before this register, base rates lived inside whichever sport file happened to derive one. The `P-438`–`P-451` audit derived eight new MLB figures at once and immediately exposed the problem: the same number was needed by `RULES_BASEBALL.md` controls 34, 35 and 37, by `RULES_GENERAL.md` `G-L24`, and by the scorecard's push-mass coherence rule in `METHOD.md` §5. Three copies of a number with three refresh dates is how a stale base rate becomes an invisible error. There is one copy, here.

It also makes the honest gaps visible. Most sports in this repository have **no derived margin band at all**, and the table below says so in the same place it publishes the one that exists, rather than leaving the absence implicit.

---

## 1. Handicap / margin bands — consumed by `G-L24` (`RULES_GENERAL.md` §16.13(e))

G-L24 queries the specified team’s signed-margin distribution, not the realised winner’s pooled margin. See RULES_GENERAL section 16.13(e) for exact integer, half-line and draw treatment.

| Sport / competition | Line | `b_L` | Conditioning | `n` | Source and query | Derived | Refresh |
|---|---|---|---|---:|---|---|---|
| **MLB** | 1.5 | **0.278** overall | by winner-minus-loser season W%: −0.2 **0.284** · −0.1 **0.301** · 0.0 **0.282** · +0.1 **0.268** · **+0.2 0.229** | 2,286 | `statsapi.mlb.com/api/v1/schedule?sportId=1&startDate=2026-03-25&endDate=2026-09-16&gameType=R&hydrate=linescore`; margin = \|away−home\| on `Final`/`Completed Early` games | 2026-09-17(b) | each season, and mid-season if cited after 1 Aug |
| MLB (9-inning games only) | 1.5 | 0.239 | excludes extras | 2,086 | same | 2026-09-17(b) | with the row above |
| NFL | 3 / 7 | key-number masses **`NOT_YET_DERIVED`** | — | — | `G-L12` already fixes a historical residual SD benchmark of about 13.9 points (Stern 1991), not a conditional width floor in `RULES_AMERICAN_FOOTBALL.md`; the key-number *masses* at 3 and 7 have never been computed here | — | derive before the next NFL handicap card |
| Soccer | 1.5 | `NOT_YET_DERIVED` | one-goal band; compute separately for the favourite and the draw state, because a draw is a third terminal state (`G-L19`) | — | ESPN `soccer/<slug>/scoreboard?dates=` over a full completed season, one date per call (ranges are unsupported) | — | derive before the next soccer handicap ranked #1 |
| Basketball | varies | `NOT_YET_DERIVED` | margin is integer-valued; `b_L` must be computed per line, not per sport | — | — | — | derive per competition before use |
| NHL / ice hockey | 1.5 | `NOT_YET_DERIVED` | empty-net goals make the 2-goal band structurally unlike other sports — derive it, do not assume it | — | `api-web.nhle.com` public schedule/score endpoints | — | derive before the next NHL handicap card |
| AFL, NRL, rugby union, cricket, tennis | varies | `NOT_YET_DERIVED` | — | — | — | — | derive per competition before use |

**Missing band:** mark the reference NOT_YET_DERIVED. A complete conditional model may still supply a transparent subjective or fitted margin distribution. Missing pooled data does not automatically demote a row; missing conditional evidence is disclosed. The previous 0.53/0.54 ceiling and fixed extras contribution are withdrawn. For example w=.85 and r=.23 imply P(−1.5)=.6545 without violating probability laws. No historical card is re-ranked.

## 2. Endpoint / overtime mixtures — consumed by `RULES_BASEBALL.md` control 37 and `G-L19`

| Sport | Quantity | Value | `n` | Source | Derived | Refresh |
|---|---|---:|---:|---|---|---|
| **MLB** | P(tie after 9 → extras) | **0.0875** | 2,286 | `statsapi`, `currentInning > scheduledInnings` | 2026-09-17(b) | each season |
| MLB | P(final margin = 1 \| extras) | **0.685** | 200 | same (2-run 0.205; 3+ 0.110) | 2026-09-17(b) | each season |
| MLB | runs added by extras | mean **2.88**; P(≥2) **0.605**; P(≥4) ≈ 0.24 | 200 | same; final total minus 9-inning total | 2026-09-17(b) | each season |
| MLB | regulation total in games that reach extras | mean **6.81**, median 6 | 200 | same | 2026-09-17(b) | each season |
| MLB | innings played in extras games | 10: 149 · 11: 34 · 12: 13 · 13: 4 | 200 | same | 2026-09-17(b) | each season |
| KBO / NPB | terminal-tie rate after the innings cap | `NOT_YET_DERIVED` | — | `G-L19` requires the cap itself as a `G0`/`G2` identity field (baseball control 32, origin `P-432`) | — | derive before the next KBO/NPB winner label |
| Soccer (knockout) | extra-time / shoot-out reach rate | `NOT_YET_DERIVED` | — | — | — | derive before the next knockout winner label |

**Correct endpoint identity:** if regulation ends tied with total exactly L and an action-valid full game completes, at least one run is added, so the total exceeds L with probability 1 conditional on that state and completion. The historical 0.605 is P(at least two added), a different event. Compute tie probability from joint team scores; do not add extras to an already final-score model.

---

## 3. Total-runs / total-points geometry — consumed by `RULES_BASEBALL.md` control 35 and `METHOD.md` §5

| Quantity | 2026 value | `n` | Note |
|---|---:|---:|---|
| MLB mean / median total runs | **8.98 / 8** | 2,286 | sd **4.53**, variance 20.49 |
| MLB push mass by integer line | 6 → 7.0% · **7 → 11.5%** · 8 → 8.1% · 9 → 9.1% · 10 → 6.7% · 11 → 7.3% · 12 → 4.2% | 2,286 | **11.5% is the maximum at any integer** |
| Share of MLB total-runs variance explained by park identity | **4.3%** | 30 parks, n ≥ 60 each | between-park variance of means 0.885 against a total variance of 20.49 |

**Push cap withdrawn:** Var(T)=E[Var(T|X)]+Var(E[T|X]). The park-only 4.3% figure does not constrain every conditional variance or PMF cell. The 11.5% maximum is a realised cohort frequency, not a universal matchup ceiling. Derive push mass from a coherent conditional model and check it on held-out games. No independent row cap or automatic ranking correction follows.

### Venue reference distributions (2026, through 16 Sep)

Consumed by control 35's "print the venue base rate beside the line" requirement. `n` ≈ 74–78 per park, so the standard error on each proportion is ≈ 5.7 points — **these anchor a disclosure, they do not settle a close call.**

| Venue | mean | median | P(≥12) | modal total |
|---|---:|---:|---:|---|
| Coors Field | 11.38 | 11 | **47.3%** | 10 (12.2%) |
| Wrigley Field | 9.85 | 9 | 41.0% | 3 (11.5%) |
| Target Field | 9.18 | 9 | 27.3% | 5 (10.4%) |
| Daikin Park | 8.94 | 9 | 27.3% | 9 (10.4%) |
| Chase Field | 8.76 | 8 | 22.4% | 9 (13.2%) |
| Progressive Field | 8.45 | 8 | 24.4% | 5 (12.8%) |
| Busch Stadium | 8.36 | 8 | 21.8% | 5 (14.1%) |
| Globe Life Field | 8.18 | 8 | 20.3% | 6 (17.6%) |

Remaining 22 parks: **`NOT_YET_DERIVED`** — the query is the same one-liner; derive the venue in play before the card, not the whole league.

---

## 4. Round / competition reference rates — evidence only, not identity inputs

These are too small to be identities. They are recorded because a card that departs far from its own round's realised rate should say why.

| Competition | Quantity | Value | `n` | Derived |
|---|---|---:|---:|---|
| ACL2 + UEL matchday 1, 16 Sep 2026 | first-half goals 0/1/2/3/4 | 8 / 3 / 4 / 1 / 1 | 17 | 2026-09-17(b) |
| same | P(1H ≥ 2) → a 1H Under 1.5 wins | **35.3%** → 64.7% | 17 | SE ≈ 12 points |
| same | P(1H ≥ 3) → a 1H Under 2.5 wins | **11.8%** → 88.2% | 17 | SE ≈ 8 points |
| same | P(FT ≥ 3) / P(FT ≥ 5) | 35.3% / 17.6% | 17 | — |

**How this was used, and the limit.** The three cards that priced a 1H Under 2.5 at 87–92% sat on the round's own 88.2% and went 3/0. `P-438` priced a 1H Under **1.5** at 84% against a round rate of 64.7% and lost. At `n = 17` that gap is ~1.6 SE — suggestive, not conclusive — so it supports **soccer control 40's disclosure requirement** (derive sibling phase lines from one printed distribution) and supports **no coefficient at all**.

---

## Maintenance

- **Cite, never copy.** A sport file, `METHOD.md` or a card points at the row here. If a figure must be restated in place for readability, restate it with its `n` and derivation date attached so a stale copy is self-evident.
- **Staleness.** A season-cadence figure cited more than one completed season after its derivation date is `STALE` and must be recomputed before it is used as a reference prior.
- **Provenance.** Every row carries the query that produced it. A row whose query cannot be re-run is downgraded to §4 (evidence only) and loses its reference-use status.
- **`n` travels with the number, always** — in the sport file, on the card, and in any report (`METHOD.md` §5).

**Related:** `RULES_GENERAL.md` §16.13(e) (`G-L24`) · `RULES_BASEBALL.md` controls 34–37 · `RULES_AMERICAN_FOOTBALL.md` (G-L12 residual benchmark) · `DATA_SOURCE_REGISTER.md` §"2026-09-17(b)" (`SRC-MLB-STATSAPI-SEASON`) · `CONTROLS.md`.
