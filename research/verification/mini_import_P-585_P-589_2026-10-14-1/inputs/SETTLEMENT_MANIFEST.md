# SETTLEMENT_MANIFEST — P-585 to P-589

## Reading receipt and controlled source
- Authority: **PUBLISHED_MAIN_PINNED**; GitHub repository `https://github.com/danisgreat/Sports-Research`, `main` read-only; full verified SHA `3ab6d27fedb177add7cca5b41b14346107688ce3`.
- Current method/control/scoring/selection: `MDS-2026.10.12-v11.0`, `CR-2026.10.12-R2`, `SCV-2026.10.12-v7`, `SEL-2026.10.12-v3` / published `P_ORDER_V2`; source card local policy `SUPPLIED_FIRST_V1` preserved, not retroactively converted. Mini format `mini-log-7`, settlement `mini-settlement-6`.
- Read on published SHA: `research/prompts/3_SETTLE_LOCAL_MINI.md`, `CURRENT_STATE.md`, `CURRENT_RULES.md`, `METHOD.md`, `SELECTION_RULES.md`, `CARD_AND_LOG_TEMPLATES.md` §§6,9, `SCORING_AND_VALIDATION.md`, `VERIFICATION_PROTOCOL.md`, `SOURCES.md` registered NHL/ATP/EuroCup/NBA routes, `ARCHIVE_USE_GUIDE.md`, `BASE_RATES_REGISTER.md`, sport rules by frozen original cards and current control route. Full original local mini and P-587/588/589 standalone card copies also inspected. GitHub canonical originals of P-581…P-584 not supplied as immutable card blocks in source mini; no regrading.
- Frozen source: `/mnt/data/Mini Prediction Log - P-585 onward - 2026-10-13/PREDICTION_MINI_RUNNING_LOG_P-585_ONWARD.md`
- Freeze timestamp: `2026-10-14T18:39:18+11:00`; current settlement effective 2026-10-14T18:50:59+11:00.
- FROZEN_SOURCE raw bytes: **208588**, SHA-256 `5a57bd78e79c6cd9b8eec8e6b52ab96bc4743ddbf656f442e659ad13c987fdae`; **1200 lines**, LF=1200, CRLF=0.
- Original footer retained unmodified: highest P-589 / next P-590; 5 new numeric cards; 6 prior pending and 3 prior evidence queues; repo next snapshot P-585; actual completed results now change only appended settlement section, **not** the original footer.
- Original block inventory: P-585, P-586, P-587, P-588, P-589 (5 BEGIN/END balanced); separate P-587 `2026-10-14-SHADOW-01` addendum (1); inherited canonical queues P-581…P-584 (4). No new ID. No prior local settlement-revision file found in this supplied destination; `revision-1` for all five.
- Writer lease handover: **NONE**. This package freezes this source snapshot, but does not create or authorise a new mini or silently modify the original mutable status. No subsequent append should use the frozen snapshot.
- Source growth check at package time: **PASS — raw SHA and byte count unchanged**; original copy byte equality: **PASS**; settled file exact source byte prefix: **PASS**. Source and original mini line endings identical; entire original header, five forecast blocks, P-587 research addendum and original footer remain a byte-identical prefix.

## Counts and sporting results
- Source requests/new cards: **5/5** numeric cards, zero new qualitative or NO_FORECAST, and no duplicate intake requests. Existing canonical references **4** (not fresh predictions).
- Terminal local events: **5**; terminal sporting grades all four rows: **9 WIN, 9 LOSS, 2 PUSH, 0 VOID, 0 UNRESOLVED** (**20 rows**). A/B headline = A/B+C/E sensitivity for currently settled fields. Operator-grade outcomes remain UNKNOWN separately.
- Formal Ranks 1–2: **5 WIN, 5 LOSS, 0 PUSH, 0 VOID, 0 UNRESOLVED**, 10/10 decisive, **50.00%** decisive hit; Rank1 4W/1L, Rank2 1W/4L; card classes ALL_WON=1, ALL_LOST=1, SPLIT=3; Hit@2=4/5=80%, mechanically protected card P-587 included only as construction context; without it 3/4=75% (tiny and late/non-certified).
- Frozen model winner calls: correct 3/5 (P-586/P-588/P-589), incorrect 2/5 (P-585/P-587), entirely not certified.
- Baseline: exact-line same-row baseline coverage primary **4/10** (P-587 and P-589), full supplied **8/20**; no historical fill.
- Timing: original P-586/P-587/P-588/P-589 explicitly `LATE_START_UNVERIFIED`; P-585 actual first serve unknown/source displayed Upcoming at issue. **0 verified prospective clean-pre-game cards**. No prospective backtest claim.
- Mandatory Rank1 deep reviews: **1** (P-585). All five terminal cards have R1–R12 and winner/expected/error reviews.
- Pending evidence: canonical P-584 owner confirmation, P-581 corners; canonical correction follow-up P-583 score, P-582 corners, operator terms / actual-final timestamps for 5 new cards. No sporting rows in new cards unresolved.

## Proper scores (original p only, completed decisive original picks)
| Cohort | W / L | n | Mean Brier | Mean log loss | Paired same-row baseline n |
|---|---|---:|---:|---:|---:|
| All original Rank1+Rank2, headline A/B | 5/5 | 10 | 0.236406 | 0.665504 | 4 |
| All original Rank1+Rank2, sensitivity A/B+C/E | 5/5 | 10 | 0.236406 | 0.665504 | 4 |
| Rank1 only | 4/1 | 5 | 0.180756 | 0.552424 | 2 |
| Rank2 only | 1/4 | 5 | 0.292055 | 0.778584 | 2 |
| All 18 decisive original supplied lines incl informational (descriptive only) | 9/9 | 18 | 0.233535 | 0.659650 | 6 |

Frozen paired rows (n=4): card mean Brier **0.251668**, baseline **0.229513**, delta **+0.022155**; card mean log loss **0.696473**, baseline **0.648153**, delta **+0.048321**. These numbers do NOT establish calibration or generalisable superiority.

## Shadow results — not primary
- `SHADOW_BASE_ONLY` over the same two selected keys in each of 5 cards: W=5 L=5, n=10, Brier=0.233933, logloss=0.660276; these are base-scenario probabilities, never part of original rank evaluation.
- P-587 **corrected** `SHADOW_RANK_DELTA` only: Ducks ML LOSS / Flames +1.5 WIN, n=2, Brier=0.262243; original P-587 shadow addendum governs order, originally issued primary unaffected. This comparison shares exact two underlying original candidates and cannot be interpreted as two new predictions.
- Other `SHADOW_RANK_DELTA`: not issued as two complete shadow picks; published `P_ORDER_V2` full ladder absent, `RET03/RET04/XCARD6` only frozen existing diagnostics. Zero shadow reforecasts promoted into original scoring.

## Sources and exact field receipts

**Timestamp fidelity:** `2026-10-14T18:50:59+11:00` is the package compilation timestamp, **not** a measured HTTP retrieval time for each URL. The precise per-URL observation instant was not recorded; do not interpret it as a source update, verified final time or a pre-issue source snapshot. Publication dates are recorded only at their exposed precision.

| Event | Source URL | Exact observed field(s) | Evidence | Update/last publication | Source observation timing |
|---|---|---|---|---|---|
| P-585 | https://en.rolexshanghaimasters.com/en/media/news/gea-mensik-shanghai-2026-tuesday | Géa 7–6(4), 6–4 Menšík; Completed best-of-three, two sets, no retirement reported; Géa 13 games, Menšík 10; total=23; Géa−Menšík=+3 games. | B / owner or club | ATP editorial publication 13 Oct 2026; time not stated | Checked in 14 Oct 2026 settlement run; exact per-URL retrieval instant not captured |
| P-586 | https://www.basquetmanresa.com/en/news/baxi-manresa/game-report/2026/defeat-of-kidsus-on-the-complicated-court-of-bahcesehir/ | Bahçeşehir 100–88 Manresa; Four regulation quarters 32–20, 21–24, 23–22, 24–22; no overtime; total=188, Bahçeşehir−Manresa=+12. | B / owner or club | Publisher displays 13 Oct 2026, 20:46; timezone not exposed | Checked in 14 Oct 2026 settlement run; exact per-URL retrieval instant not captured |
| P-587 | https://www.nhl.com/gamecenter/cgy-vs-ana/2026/10/13/2026020103/boxscore | Calgary 4–2 Anaheim; NHL 3-period regulation 1–2, 1–0, 2–0; no OT/SO; total=6. Calgary scored final empty-net goal; Anaheim−Calgary=−2. | A / owner or club | exact update time unknown; published 13–14 Oct | Checked in 14 Oct 2026 settlement run; exact per-URL retrieval instant not captured |
| P-588 | https://www.nba.com/watch/video/game-recap-warriors-101-lakers-89?plsrc=nba | Golden State 101–89 Los Angeles; NBA preseason four quarters Warriors 29/21/22/29, Lakers 29/34/13/13; no overtime; total=190, Golden State−Los Angeles=+12. | B / owner or club | NBA recap dated 14 Oct 2026; time not stated | Checked in 14 Oct 2026 settlement run; exact per-URL retrieval instant not captured |
| P-589 | https://www.nhl.com/news/boston-bruins-san-jose-sharks-game-recap-october-13-2026 | Boston 6–3 San Jose; NHL regulation three periods 2–1, 2–1, 2–1; no OT/SO; empty-net goal at 18:18 of third; total=9, Boston−San Jose=+3. | B / owner or club | exact update time unknown; published 13–14 Oct | Checked in 14 Oct 2026 settlement run; exact per-URL retrieval instant not captured |

Official terminal retries: EuroLeague media centre game19489 still displayed stale 0–0 during current search, while Manresa club final was verifiable; a renewed media-centre request is manual `NOT_SCHEDULED`, choose next-review within 24 hours (its publicly cached page lags). Official NHL Bruins gamecenter/JSON routes inaccessible to this browser at settlement; NHL owner detailed recap verified final and will be rechecked against structured game sheet manually. KBO owner scoreboard was accessible and resolves prior score discrepancy. For owner sources with no prescribed interval, use manual 24 hours due transient cache lag, not an invented automated check. No independent raw publication timestamp implies a verified final-time SLA.

## S1–S15 executed settlement audit
| Check | Result | Actual evidence / limitation |
|---|---|---|
| S1 | PASS | Five distinct issued card markers balanced, one P-587 addendum, four inherited canonical queues; no ID changes |
| S2 | PASS | Raw source and ORIGINAL_MINI hashes match; exact settled prefix compared byte-for-byte; original footer included intact |
| S3 | PASS | Full verbatim original decision-table rows echoed in each settlement, raw `p_card`, base, baseline and original expected score preserved; no reconstruction |
| S4 | PASS | Final score and literal four lines per card graded; P-587 integer 6.0 pushes both, tennis tiebreak games counted 13 |
| S5 | PARTIAL | Owner/club source reports available, clock publication/final-time and operator action terms unverified; actor/route retained |
| S6 | PASS | 20 supplied rows = 9W+9L+2P; primary 10=5W+5L, no unresolved sporting grade |
| S7 | PASS | Five event-specific R1–R12; no copied generic score or changed rank table |
| S8 | PASS | P-585 Rank1 loss receives eight explicit deep-review parts; win reviews run R1–R12 |
| S9 | PASS | P-587 corrected rank-delta and base-only shadows separated from primary and baseline counts |
| S10 | PARTIAL | New five events terminal; P-584 official unverified, P-581 owner corners outstanding; final wall times unknown |
| S11 | PASS/PARTIAL | Calculated exact Brier/log loss on 10 original decisive primary rows, four paired baseline rows; score/SD identities exact where source gave full-game SD; P-586 full-game SD not fitted |
| S12 | PASS | Original copy/settled/manifest/mapping/carryover/grade ledger written locally and read back; no GitHub/Combined changes |
| S13 | PASS | Five distinct `revision-1` keys, parent NONE, all four keys affected; no imported prior revision reused |
| S14 | PASS | FROZEN_SOURCE receipt written before grade work, source hash rechecked on completion, no growth observed |
| S15 | PARTIAL | Every open queue row includes actor, route, due, final basis and last attempted; no actual final wall time, automated retry not scheduled |

## Limitations, idempotence, next action
- The settlement concerns local cards P-585–P-589 only. The already canonical P-581–P-584 cannot be regraded without their original imported source blocks/revision graph; new evidence is a manual correction lead, not an effective revised grade.
- Results are sporting under `FROZEN_FRAMEWORK_CONVENTION`, not proven operator-specific settlement. A/B graded fields use official owner or participating-club source; all evidence times are current retrievals, not certified original final times.
- Original source mini remains intact and may still say ACTIVE. The settlement package is the explicit frozen receipt; next mini not auto-created, and issuer lease not silently transferred. Prevent any further append to this frozen source.
- Settlement output is **new-only**; on rerun create a new revision package (do not overwrite these files), retain parent-chain revisions and update only changed keys.
- **GitHub writes: NO; Combined Log writes: NO; canonical import: NOT_PERFORMED; canonical IDs consumed: 0; new working IDs assigned in settlement: 0.**
