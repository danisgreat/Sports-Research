# Two external reviews of 22 November 2026: findings, checks and decisions (v29.2)

The owner passed on two read-only external reviews of the repository. **Review A** was an empirical diagnosis of top-two
picks, the kit and the missing inputs. **Review B** was a review of "improving the top two picks", built on reproduced
defects. Neither edited files. This page records what each found, what was checked here, and what v29.2 did. Local
absolute paths in the reviews are omitted.

## Checked here before acting

| Claim | Source | Check | Result |
|---|---|---|---|
| No settled one-chat card ran the kit | A | grep of the 11 archived P-686–P-696 cards for kit calls or receipts | **Confirmed**: 0 of 11 |
| `dc_rho` is 0 for every soccer row; corner parameters blank | A | `KIT_PARAMETERS_v24.15.csv` | **Confirmed**: 33 of 33 rows set 0.0; `corners_mean` empty in all 91 |
| Shrinkage `k` is 2 almost everywhere | A | same file | **Confirmed**: 67 of 68 rows set it to 2 |
| No player-availability rows in the learning store | A, B | `research/learning_store/PLAYER_AVAILABILITY.csv` | **Confirmed**: header only |
| Every sealed line was priced with an unmeasured absence | B | shadow selection run on intake `2026-11-22-1` | **Confirmed**: all 12 cards; a strict abstention rule issued nothing |
| `PlayerX Games -0.5` read as the tennis match winner | B | `prepare` on that text | **Confirmed**: a v29.2 defect in this branch, fixed |
| Over 149.5 at 0.70 and Over 154.5 at 0.80 both pass | B | card check | **Confirmed**, now flagged |
| Competition naming changes the kit row | B | `sr_kit.row` on real names | **Confirmed**: "Australia NBL" and "NBL Regular Season" fall to a family prior; "NBA Cup group stage" falls to the 40-minute FIBA prior |
| A replay `as_of` can use a later settlement; a seal at first play counts as pre-start | B | `one_chat.score` / `timing_label` | **Confirmed**, fixed |
| README still links the v29.0 brief | A | README | Out of date: fixed earlier in this branch |
| Scoreboard presents a v27.0, 400-game snapshot as current | B | `SCOREBOARD.md` §B | **Confirmed**, now dated and pointed at the score command |
| Learning-store link to a retired protocol | B | `research/learning_store/README.md` | **Confirmed**, repointed to its archived copy |

## Implemented in v29.2 (no change to the registered evaluation)

- **Contract semantics.** Winner equivalence (moneyline = ±0.5) now needs the handicap to be on the score that decides
  the match: basketball points, ice hockey goals including the shootout goal, baseball runs. A tennis games or sets
  spread stays its own contract, both in `prepare` and in the duplicate check (`forecast_integrity.winner_by_margin`).
- **Coherence across lines.** `INCOHERENT_ACROSS_LINES` flags a card whose prices break one score distribution: a
  higher Over more likely than a lower one, or a harder home handicap more likely than an easier one. It is a flag and
  a check-drop warning, never a refusal, because the plan freezes the card protocol. The score reports how flagged
  lines perform.
- **Kit row named in the chat packet.** `prepare` writes the kit row each game reaches. Near rows are listed by name
  ("Australia NBL" → `Basketball/NBL`), and any family-prior fallback is stated. The kit itself is unchanged: its
  code identity is part of the frozen v24.15 forecast identity.
- **Replay clocks.** A replay at `as_of` ignores seals published and settlements made after it. A clock equal to first
  play is not before it (`>=`), so a seal inside a minute-precision first-play time is never taken as pre-start.
- **Top two as a separately registered shadow.**
  [SELECTION_SHADOW_PLAN_v1](../../external/SELECTION_SHADOW_PLAN_v1.md) and `ml/selection_shadow.py` define a
  recommendation list with permission to issue one pick or none. It drops coin flips, contradictions, incoherent lines
  and duplicate contracts, marks dependent pairs, and has a strict variant that also abstains on unmeasured absences.
  It is compared with the frozen ranker on the same future games at a pre-stated checkpoint, with coverage and
  denominators shown.
- **Operations.** The runbook asks for requests 30 to 60 minutes before start. Check drops and full refusal reasons
  were added earlier in this release.

## Not implemented, and why

These change forecasts, the card protocol or the selection policy, so they need an owner decision and a new
registration (v30.0) under FREEZE-v1. They are listed in the order the reviews' evidence supports:

1. **A replayable kit receipt on every card.** One call from structured inputs to centre, width and tie-resolved p.
   Both reviews' first recommendation.
2. **Kit model upgrades**: possessions × opponent-adjusted efficiency for basketball totals; empirical-Bayes shrinkage
   with sample-size width inflation in place of `k = 2`; fitted recency weights in place of overlapping L5/L10/L20
   blends; estimated `dc_rho` and corner parameters; NFL key numbers; tennis form shock; coupled cricket phases;
   competition-specific rows for AHL, NCAAB, WTA and others.
3. **Measured availability effects** (player value with replacement, goalie, pitcher, quarterback), with scenario
   mixtures for questionable starters. The learning store has no player rows today.
4. **Central pre-computation in `prepare`**: the kit row's parameters, opponent-adjusted ratings, rest, travel, a frozen
   league baseline. All 80 registered contract rows have no frozen sporting baseline.
5. **Hard gates on the registered rank** (refusing `CONTRADICTS_OWN_CENTRE`, unranking `NO_DIRECTION`). The shadow
   policy tests these first. Adoption waits for its result.
6. **Pausing sports.** Review A's sport table mixes methods and very small samples (ice hockey n = 10). It is reported,
   not acted on.

## Cautions recorded

- **Thresholds read off settled results** (Review A: "62.5% at p ≥ 0.58, 76.9% at p ≥ 0.62" on n = 24 and 13) are
  selected after the outcome and would overstate a forward result. The shadow plan uses the existing 0.55 boundary and
  registers any other threshold before testing it.
- **`research/verified_history/`** (Review A suggests deleting it) is verified sporting history used by training and
  backtests, not dead weight. It is kept. The v24.15 five-lane profile, lane briefs and audit brief stay because code
  reads them. Sixteen superseded `research/external/` files were archived instead (`archive/superseded_2026-11-22/`).
- **Consolidating the legacy PICKS_V2 documentation** out of CORE, RULES_REFERENCE and the sport prompts is
  worthwhile, but it touches documents the tests read and the frozen card protocol cites. It is left for its own
  reviewed change.
- **Historical hit rates** (Rank 1 about 62–63%, Rank 2 about 57%) span several methods, and older cards had
  analyst-chosen lines. They are descriptive. The 60–65% band's under-performance (51.7% over 147 rows) is the clearest
  signal that printed confidence should not be taken at face value.
