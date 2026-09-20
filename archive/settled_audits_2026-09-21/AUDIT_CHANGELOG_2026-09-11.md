# Audit changelog — 2026-09-11

**Pass type:** settlement + deep retrospective + control-execution audit + cross-sport algorithm improvement + ledger completion. **No forecast was issued.** Method: `MDS-2026.09.06-v4.0` (unchanged). Google Drive not touched; local repository only. Pass run 2026-09-11 ~23:30 AEST, completed early 2026-09-12 AEST.

**Scope.** Reconcile the external running logs covering `P-345`–`P-371` into the active canonical log `PREDICTION_LOG_COMBINED_3.md`; check live state first; independently re-verify finals; settle every finished row to its frozen standard; complete the table-format settlement block, the three-question retrospective and — for every Rank-#1 loss — the deep retrospective; answer the user's three standing validation questions for every card; extract cross-sport learnings into the sport algorithms; research the over/under directive; audit sources; make every unsettled row individually trackable; archive the components.

---

## 1. Live-state check — the first required step

| Event | State | Action |
|---|---|---|
| `P-364` England v Pakistan, 3rd Test | **LIVE** — Day 3 (Pakistan 206/3, trailing by 114; ESPNcricinfo via `r.jina.ai`); scheduled to 2026-09-13 BST | Four ranked rows already settled from the completed England innings; **winner label open** → `TMP-OPEN-20260911-03` |
| `P-366` Rotterdam v Glasgow, ETPL M19 | FINAL (rain-reduced to 19 overs) — ETPL first-party page now COMPLETED | 6-over rows graded; 20-over rows terminal censored |
| All other events | FINAL | settled |

## 2. Components, provenance and ledger

- **Five components archived byte-exact in `prediction logs/`** with SHA-256 (the `P-357` settled log; the `P-358`–`P-371` pre-settlement, settled and refreshed logs; and the byte-exact original `P-344` component, which the 2026-09-09 pass had reconstructed because it did not find the file on disk).
- **Immutability check:** 1,638 of 1,638 issued lines of `P-358`–`P-371` appear verbatim in the settled version. No pre-settlement copy of `P-345`–`P-357` exists → `IMMUTABILITY_UNVERIFIABLE`.
- **ID reconciliation:** local `P-345`–`P-371` map one-to-one onto canonical IDs. A local label collision at "P-358" (an unsupplied external Fenerbahçe–Roma no-forecast record) takes **`TMP-SETTLED-20260911-01`** — the first use of that namespace; the mini-log's alias `TMP-CANON-20260911-01` is retired onto canonical `P-358` (Puerto Rico–China). Fenerbahçe 1–1 Roma verified at UEFA's feed.
- **`METHOD.md` §10 breach recorded:** `P-345`–`P-357` were reconciled ~30 h after becoming available (outside the 24-hour window), and a 2026-09-10 edit had left a dangling reference in the canonical log — corrected.
- **Control currency:** `P-345`–`P-351` were issued before the 2026-09-09 controls existed and are not graded against them; `P-358`–`P-371` are.

## 3. Settlement

| | |
|---|---|
| Issued cards | **26** (`P-345`–`P-369`, `P-371`); 4 `MLB PRIMARY_SCORED`, 22 `EXPLORATORY` |
| Administrative closures | `P-370` (`CR-P3` fail-closed — correct); `TMP-SETTLED-20260911-01` (non-scorable) |
| Finals independently re-verified | **17 of 26**, all agreeing (UEFA feed, MLB statsapi, KBO English scoreboard, FIBA, CricketArchive, ESPNcricinfo, FotMob) |
| Derivative rows settled this pass at frozen owners | `P-345-C03` (UEFA: Brugge 4 corners) **W**; `P-346-C05` (UEFA: 10) **W**; `P-355-C05` (FotMob: 9) **W** |
| Provisional (no provider frozen) | `P-368-C02` provisional W (9); `P-369-C01` provisional L (11) |
| Terminal censored | `P-366-C02/C03` (20-over endpoint not reached) |
| Graded ranked rows | **61 W / 44 L**, mean Brier **0.2434** (`P-345`–`P-357` 0.2264; `P-358`–`P-371` **0.2621, worse than baseline**) |
| Rank #1 | **16 W / 9 L** + 1 provisional L — losses `P-345`, `P-350`, `P-352`, `P-356`, `P-357`, `P-358`, `P-364`, `P-365`, `P-371` (+`P-369`), all deep-retrospected |
| Top two both won | **6 / 25** decidable |
| Potential-winner labels | **13 / 25** (expected 16.0 from their own probabilities); soccer three-way 1 / 5; `P-364` pending |
| Running scorecard | mixed **177 rows, 0.2435**; `PRIMARY_SCORED` **34 rows, 0.2373** (MLB 24 rows, 0.2252); card count **8 / 25** |
| Reliability | rows stated at `p ≥ 0.70` won **13 / 21** (mean stated 0.74) |

**Learning-only per user direction** — no accuracy, calibration or improvement verdict is drawn from these numbers.

## 4. The finding that reorganised the pass — controls listed, not executed

The external session declared `G-L7`, `G-L8`, `G-L2` and `G14.2` "incorporated as active process constraints" for `P-358`–`P-371`. The new audit script (`audit_card_controls.py`) confirms that **none of the thirteen issued cards printed an outcome-family table, a numeric total width, a normalised edge or a representative Rank-#1 outcome**; `G-L1` was missing from the session's carried list; `P-362` and `P-365` broke `G14.2`. Read card by card, **almost every Rank-#1 loss turned on a mechanism already printed on its own card** — Miller's hook branch (`P-347`), Ohtani's absence (`P-351`), the wicket-light-start branch and the Windhoek T20I totals (`P-352`), Tokoda's and Ko's long-start branches (`P-354`, `P-356`), a post-toss XI (`P-357`), a set batter and an old ball (`P-364`), the 4–1/5–1 separation state (`P-365`), Germany's four listed mechanisms (`P-371`). The research found the facts; the arithmetic did not carry them into the probabilities. The one clear exception is `P-350`: an independent Elo benchmark puts Alcaraz at ≈71–77% best-of-five against the card's 76%, so that loss is most plausibly variance.

## 5. Rule changes — disclosure, retrieval and format only (no fitted weight, no ordinal bar — `L-087`)

| ID | Rule | Home |
|---|---|---|
| **`G-L9`** | Complement decomposition — itemise `1 − p` across the row's named kill paths | `RULES_GENERAL.md` §16.5(e) |
| **`G-L10`** | Joint top-two probability with coupling label (`TOP-TWO HEDGE`) — informs, never reorders | §16.5(f) |
| **`G-L11`** | Sampling-noise check on small-sample rates, both directions | §16.5(g) |
| `G-L8` clarification | Median-based `P(total ≤ line)` for right-skewed run/goal totals | §16.5(d) addendum |
| **§16.8** | Card completeness block (nine fields) + settlement audit script; `RETRIEVAL_MISS` for line-ups published before the freeze | `RULES_GENERAL.md` §16.8; `METHOD.md` §4 item 7 |
| Candidates | `C-RUN-CENTRE-BIAS`, `C-PROB-EXTREMITY`, `C-UNDERDOG-SEPARATION` (prospective manifests) | `LEARNING_REGISTER.md` §3 |

## 6. Sport-file changes

- **`RULES_BASEBALL.md`** — controls **26** (mechanism-overlap audit), **27** (PA-weighted lineup exposure), **28** (opponent long-start branch); the 12-card run-centre precision table (mean −1.58 runs); kill paths; checklist; `G14.2` breach note (`P-362`, `P-365`).
- **`RULES_BASKETBALL.md`** — controls **22** (shooting shrink with SE, both directions), **23** (spread family template incl. "underdog by 7+"), **24** (competitive game ↔ total coupling); six-card precision table.
- **`RULES_SOCCER.md`** — controls **30** (UEFA FAME settlement source), **31** (cross-competition translation); control 20's third instance with its arithmetic specified; controls 3, 5, 23 reinforced; ten-card centre-precision table.
- **`RULES_CRICKET.md`** — controls **25** (same-week cross-format surface evidence), **26** (post-toss XI retrieval), **27** (Test-restart tempo prior; restart is width).
- **`RULES_TENNIS.md`** — controls **13** (Tennis Abstract Elo benchmark, with the best-of-five conversion), **14** (long-layoff width).
- **`RULES_NRL_RUGBY.md`** — `P-363` positive model; instantiation of `G-L9`–`G-L11`.
- **`RULES_AFL.md`, `RULES_AMERICAN_FOOTBALL.md`, `RULES_ICE_HOCKEY.md`, `RULES_RUGBY_UNION.md`** — sport-native instantiation of `G-L9`–`G-L11` and §16.8.

## 7. Sources

New field-owner lane: **UEFA `matchstats` FAME feed** (keyless; parse raw JSON). Structured secondary: **FotMob via `r.jina.ai`**. Reconfirmed: KBO English scoreboard, FIBA game pages, Cricket Ireland-branded CricketArchive. Benchmark only: **Tennis Abstract Elo**. Re-graded to cross-check only: Guardian and VI corner counts (each wrong by one). Status only: the ETPL first-party page (stale >24 h). Access failed from this environment: ClubElo. Route notes: MLB statsapi needs `curl` (WebFetch 406); ESPNcricinfo via proxy can be cached. Full detail: `SOURCES.md` and `DATA_SOURCE_REGISTER.md` §"2026-09-11".

## 8. The over/under directive — researched answer

Ranking both sides of one line guarantees one O/U win; the meaningful measure is the favoured side. Four cohorts: **phase totals** hold (this import 7 W / 2 L); **far-from-centre alternate lines** 3 / 3; **baseball team-total Unders on the stronger starter** 6 / 2; **supplied main-line full totals** remain a coin flip (13 / 13; Over-favoured cards 1 / 5). The main line cannot be picked much better because centre errors (soccer 1.42 goals, baseball 3.35 runs, basketball 8.4 points mean absolute) dwarf the distance from centre to line. What changes: probabilities must say "coin flip" when the normalised edge is small; measured biases are addressed through mechanism (baseball control 26, basketball controls 22 and 24); own-pick selection is guided toward the families that have held (guidance, not an ordinal bar); `P(R1 ∧ R2)` is printed.

## 9. Honest limits of this pass

- Nine finals (`P-350`, `P-353`, `P-354`, `P-359`, `P-360`, `P-361`, `P-363`, `P-364` first innings, `P-365`) rely on the external pass's field-owner citations; not re-fetched.
- `P-345`–`P-357` issued text cannot be checked for immutability (no pre-settlement copy).
- The nine inherited Part-2 open rows were not independently re-researched (the external session reported 0 upgrades); only the named ESPN `uga.1` trigger for `P-341-C03` was re-probed.
- The `G-L11` worked example assumes ~25 three-point attempts per game (the card printed none); the Elo best-of-five conversion is an approximate constant-set-probability model; three baseball centres are corridor midpoints because those cards printed no numeric centre.
- The statsapi `battingOrder` lineup route is proposed, not yet demonstrated pre-game. ClubElo could not be reached.
- The keyword audit is heuristic; its misses were checked by eye for the claims made here.

## 10. Files changed

`PREDICTION_LOG_COMBINED_3.md` (snapshot, candidate list, §"2026-09-11" section with 27 settlement blocks, current and historical queues, full status, next slot) · `GAME_LOG_STATUS_INDEX_2026-09-05.md` · `RULES_GENERAL.md` · all ten `RULES_<SPORT>.md` · `CONTROLS.md` · `LEARNING_REGISTER.md` · `SOURCES.md` · `DATA_SOURCE_REGISTER.md` · `METHOD.md` · `EXTERNAL_LOGGING_WORKFLOW.md` · `PERFORMANCE_ELIGIBILITY_POLICY.md` · `README.md` · new `audit_card_controls.py` · new `AUDIT_CHANGELOG_2026-09-11.md` · five components added to `prediction logs/`.
