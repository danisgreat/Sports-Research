# Local mini settlement — findings and operator handoff

**Mode:** LOCAL_MINI_SETTLEMENT · **Review:** 13 October 2026, Australia/Melbourne · **GitHub:** `main` READ ONLY, pinned SHA `adb8560a597e5ff1a5ad21bfc76b3148bd58c719` (MDS-v11; the original forecast rules stay frozen to their issue versions).

## Executive reconciliation

- Active input `/mnt/data/CHAT_ACTIVE_MINI_P580_ONWARD_2026-10-12.md`: **172,050 raw bytes**, SHA-256 `364dc74e30520df5711743ecbc9efd5122a9024627f1bba4f4bb7cb9c49adba0`; `ORIGINAL_MINI.md` is byte-exact, and the same raw bytes are an exact prefix of `PREDICTION_MINI_SETTLED.md`.
- **8 distinct records:** three already canonical carryovers (P-577–P-579), five new local-unimported cards (P-580–P-584). **Four dated original addenda** stay intact. The original highest/next working IDs remain **P-584 / P-585**, but the mini is now **frozen for settlement** under this local receipt. Neither original P-ID nor original forecast text changed.
- **7 terminal sporting results**, **1 pending event** (P-584). Six original numerical top-two slates P-577–P-582 = **12 decisive primary rows: 10 W, 2 L, 0 PUSH, 0 VOID, 0 unresolved primary grades.** P-583 was NO_FORECAST (zero numeric primary ranks); P-584's late model output is NOT_PRIMARY. Evidence A: 10 rows (9 W, 1 L); evidence B: 2 rows (1 W, 1 L). These row counts are not independent forecasting trials.
- Original Rank 1 **4W–2L**, original Rank 2 **6W–0L**. Rank 1 losses **P-577 and P-581** have separate eight-part deep reviews, with R1–R12 on each terminal record. No original Rank-1 gate PASS inferred from outcomes; most are `RANK1_UNSTABLE`. Mechanical Hit@2 and easy line selection do not demonstrate superior prediction.
- Original primary rows' **descriptive** mean Brier **0.136674**, log loss **0.442658**. Frozen independent same-row `BASELINE_P` is populated on only four primary rows (P-581 and P-582): candidate Brier **0.187418** vs baseline **0.188131** (difference **−0.000713**). This sample of four dependent, heterogeneous rows is not significant/validated. No historical missing baseline backfilled.
- **Next action:** Do not append to the frozen source. Carry P-584 into the next authorised mini as its **existing pending ID** with a pointer to its first card, not as a newly issued forecast. Future genuine events begin from working P-585 only after issuing-writer hand-over and conflict recheck. Canonical import is separate, not performed.

## Literal sporting results against original ranks

| ID | Event final | R1 original | R2 original | Counted W/L | Outcome grade | Original winner lean |
|---|---|---|---|---|---|---|
| P-577 | Bublik 6–7, 6–3, 7–6 Nakashima (35 games) | Under 33.5 **L** | Nakashima +5.5 **W** | 1–1 | B · completed-set source | Nakashima **L** |
| P-578 | Dallas 132–115 Houston (247 points) | Under 258.5 **W** | Over 198.5 **W** | 2–0 | A · NBA owner | Houston **L** |
| P-579 | Murcia 77–90 Tenerife (167 points) | Under 197.5 **W** | Over 147.5 **W** | 2–0 | A · ACB owner | Murcia **L** |
| P-580 | Motor 4–3 Liberec (7 goals) | Liberec +2.5 **W** | Under 8.5 **W** | 2–0 | A · Czech federation | Liberec **L** |
| P-581 | Brøndby 5–2 Lyngby (7 goals, HT 3–0) | Under 4.5 **L** | Over 1.5 **W** | 1–1 | A · DBU owner | Brøndby **W** |
| P-582 | Liverpool 0–3 Manchester City (HT 0–0) | Under 5.5 **W** | 1H Under 2.5 **W** | 2–0 | A · Liverpool FC | City **W** |
| P-583 | KT Wiz 4–2 Samsung (6 runs) | No issued primary | No issued primary | excluded | B · KT result + Yonhap, conflicting stale box | Qualitative KT **right direction** |
| P-584 | Dragones–Guerreros: final not verified | No issued primary | No issued primary | pending | Pending · club fixture page only | Unresolved; diagnostic excluded |

**Supplementary target fields:** P-581 official DBU goals imply HT 3–0. Two secondary match-stat providers show **8+4=12 corners**, so Over 10.5 W/Under 10.5 L only as a B-grade *unranked* sporting diagnostic. P-582 TNTsports records **5+6=11 corners**, so Over 10.5 W/Under 10.5 L, also not original primary; the 0–0 halftime makes 1H Over 0.5 L and Under 0.5 W. P-583's frozen user input repeated Over 11.5 twice; deduplicated once; KT −1.5 W, Samsung +1.5 L, Over 11.5 L are **not scored numerical primary picks**.

## Sources: event-specific decisive terminal fields

- P-577 Tennis.com, completed sets `6-7,6-3,7-6`: https://www.tennis.com/tournaments/rolex-shanghai-masters/matches/a-bublik-vs-b-nakashima-2026-10-11 . Field-owning ATP terminal result NOT independently fetched; evidence **B**.
- P-578 NBA official 0012600016, DAL 132/HOU 115, four quarter sums: https://www.nba.com/game/dal-vs-hou-0012600016?lid=i7ats91sny0x . Evidence **A**.
- P-579 ACB official UCAM 77/Tenerife 90, final of fourth quarter: https://live.acb.com/en/partidos/ucam-murcia-vs-la-laguna-tenerife-105398/jugadas . Evidence **A**.
- P-580 Czech federation Tipsport Extraliga fixture, Motor 4/Liberec 3, periods 2-2/1-0/1-1: https://ceskyhokej.cz/en/competition/games/14?do=gameCalendarWidget-changeDate&gameCalendarWidget-date=2026-10-11&gameListWidget-filter%5Bclub%5D=11 . Evidence **A**.
- P-581 DBU match 556151, finished 5–2 and three goals before 45-minute whistle: https://www.dbujylland.dk/resultater/kamp/556151_506118/kampinfo . Evidence **A**; separate corner-field B https://www.zerozero.com.ar/partido/2026-10-11-brondby-if-lyngby-bk/12244389 .
- P-582 Liverpool official match centre 0–3/second-half 0–3: https://www.liverpoolfc.com/matches/mens-team/liverpool-v-manchester-city-english-premier-league-20261011 . Evidence **A**; secondary corner field https://www.tntsports.co.uk/football/premier-league/2026-2027/live-liverpool-manchester-city_mtc21883285/live-stats.shtml .
- P-583 KT club fixture/results listing 4–2: https://www.ktwiz.co.kr/game/regular/schedule/202509 ; Yonhap published 12 Oct 2026 21:39 KST confirms 4–2: https://www.yna.co.kr/amp/view/AKR20261012178800007 . **Source conflict:** owner detailed box https://www.ktwiz.co.kr/game/regular/boxscore/20261012/20261012KTSS0 is stale/inconsistent (4–1). Record this openly and recheck exact box before any future operator-grade assertion.
- P-584 Dragones official fixture date/time but **no terminal final**: https://www.dragonesfc.mx/equipos/premier-a/calendario . Secondary BeSoccer event still displayed no result: https://www.besoccer.com/match/dragones-oaxaca/guerreros-del-pacifico/2027176995 . Do not infer a score from a stale/live partial screen.

All pages were researched on 13 October 2026. Exact per-URL retrieval timestamps and actual **final whistle** timestamps were not independently preserved; package-assembly time is not misrepresented as source-update time. This prevents exact 72-hour compliance claims. Market data, odds and prediction sources were not used in grading.

## Critical verification limits

1. P-577–P-579 are original **canonical references**, not new local predictions. Earlier *local* full original card cores were recovered from an accessible, preserved Library master and copied into the package. Direct GitHub Combined Log 7 content fetch returned empty; thus their **canonical block exact-byte comparison was NOT_VERIFIED**. Do not treat the source-reference package as proof of canonical byte equality.
2. The in-progress source is `mini-log-6` and stays in its original format. The settlement suffix follows its legacy compatibility and includes current v11 revision/queue/check rules. It is not retroactively converted into a mini-log-7 card.
3. Issuing-writer lease hand-over cannot be enforced on external agents. This run's **freeze receipt** exists in the separate manifest; the original frozen bytes retain the old `ACTIVE` footer as historical source text. Future authors must respect the freeze and use the next authorised mini.
4. Sporting scores are verified at a defined endpoint; where user-specific operator refund/void/settlement rules are unknown, **actual operator outcomes remain UNKNOWN_DEFINITION**. No source conflict is silently resolved and no missing line is called a zero.
5. All originally issued prognostic probabilities are uncalibrated. Later live/late supplements, RANK_DELTA and BASE_ONLY shadows are not allowed into the original prospective performance cohort.

## File inventory and readback

`ORIGINAL_MINI.md` is an exact immutable copy; `PREDICTION_MINI_SETTLED.md` is the entire exact original prefix plus eight unique `revision-1` settlement blocks with R1–R12; `CARRIED_ORIGINAL_CARD_REFERENCES_P577_P579.md` contains full earlier local originals; `LOCAL_ID_MAPPING.md` inventories original and addendum blocks; `UNRESOLVED_CARRYOVER.md` preserves pending-event and evidence queues; `SETTLEMENT_MANIFEST.md` contains freeze/growth/audit S1–S15; `PRIMARY_PROPER_SCORES.csv` contains the twelve reproducible original top-two scoring rows; `READBACK_VERIFICATION.md` contains container-backed byte/count checks.

**No GitHub or Combined Log writes. No new canonical IDs. No settlement/result edit to any issued original.**
