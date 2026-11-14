# Audit of the 14 November 2026 owner drop against the framework

Audit date 2026-11-14 (AEDT evening). Scope: every file in `Mini logs and stuff - to be settled/` including the `drive-download-20261114T112952Z-1-001/` subfolder and the members of its three zip files: 178 files, byte-copied unchanged to [`research/active_minis/received/OWNER_DROP_2026-11-14/`](../../active_minis/received/OWNER_DROP_2026-11-14/). Framework in force: MDS-2026.11.11-v24.16, prompts P-2026.11.11-v24.14, ENV-v2, MINI-v2, EXT-v3, SRC-ALT-v3, LEARNLOG-v1, ML-SEP-v1, records change CR-2026.11.12-R1.

**Bottom line.** The drop holds seven chat-local minis with 90 records on 21 games (9 to 14 November 2026). None of them is a repository-issued card: no writer lease, no reference stage, no `card lint`, no pregame freeze, no commit. All 21 games have verified finals and every record is settled, but **every graded row is diagnostic only and the primary denominator is zero**. The records are kept because RETAIN-v3 requires it, not because they qualify as forecasts. Six chats carded the same 11 games in parallel and three strands covered the other 10, so the 90 records are 21 dependent observations, not 90.

## 1. Inventory and custody

| Mini / strand | Container | Records | Games | Custody result |
|---|---|---:|---|---|
| `20261112EE4AFA68` | `PREAUDIT_20261112EE4AFA68/` mini, 314,991 B | 11 cards + 2 addenda | 12-14 Nov, all 11 | SHA matches its own SHA256SUMS; markers balanced |
| `20261112CHAT9538BF5E` | `PRE_AUDIT_PACKET_20261112CHAT9538BF5E/` mini, 241,223 B | 10 | 12-13 Nov (no Knicks–Pacers) | Matches manifest. The pasted `mini running log 14112026_1.md` (226,268 B) is a rendered copy of the same mini: 99.78% word-identical, link URLs stripped. Not used as a source |
| `202611128358B025` | zip member `research/active_minis/202611128358B025.md`, 225,984 B | 11 | all 11 | Matches the zip's SHA256SUMS |
| `20261112CHAT17C8C881` | zip member `mini/20261112CHAT17C8C881.md`, 222,301 B | 9 | 12-13 Nov | Matches SHA256SUMS. **No BEGIN/END card markers**: cores were cut at card headings (a mini-log-10 marker defect) |
| `20261112CC53B5C806` | `original_files/PREDICTION_MINI_RUNNING_LOG_20261112CC53B5C806.md`, 246,441 B | 9 | 12-13 Nov | Byte-identical to the copy inside its zip |
| `20261112D3C239297F` | `PREDICTION_MINI_PRE_G0009_READBACK.md`, 226,276 B | 8 | 12-13 Nov | **Final mini missing**: the handover names a 300,547 B file, SHA `fc276d27…`, that is not in the drop. G0009-G0011 are MISSING_ORIGINAL; only their scripts/JSON exist. Owner decision: proceed without |
| `20261109R3NEXT` strand A | v24.15/16 research drafts embedded in `20261109R3NEXT.md` (174,171 B) and the FULL bundle | 11 (incl. 1 identity-conflict note) | 9-12 Nov, 10 games | Every embedded original matches its declared SHA (25/25 in FULL) |
| `20261109R3NEXT` strand B | DRAFT-001..011 in `COMPLETE_MINI_LOG_AND_ALL_ASSOCIATED_TEXT.md` | 11 (incl. 1 identity-conflict note) | same 10 | 22/22 originals match declared SHA |
| `20261109R3NEXT` strand C | v4.12 model cards G1-G010 in `20261109R3NEXT_v412_GAMES_1_TO_10_LOCAL_DRAFT.md` (two identical copies) | 10 | same 10 | G1-G009 match declared card SHA; **G010 has no declared hash** |

Not forecasts and therefore not graded: twelve v24.15 retrospective conversions (each states it is not a forecast), process/review notes, pre-append snapshots and readbacks, scenario scripts, JSON outputs and integrity receipts. They stay in `received/`.

## 2. Framework compliance, finding by finding

1. **Authority and writer (ENV-v2, MINI-v2 §2): NOT MET.** Every chat ran under `PUBLISHED_MAIN_PINNED` read-only authority with the owner's "no GitHub writes" override. ENV-v2 makes prompt 1 a repository-agent task with a commit as the freeze; none exists. The 12 Nov records change (CR-2026.11.12-R1) lets chats keep their own minis, but it did not make chat cards issued cards, so all 90 records are NOT_ISSUED.
2. **External research protocol (EXT-v3): NOT USED.** No event manifest, no lanes, no packets, no SINGLE freeze, no L5 pricing. The parallel chats are the five-lane idea done without its controls: six independent cards per game instead of five role-bound lanes merged into one. None of these games counts toward ASSESS-100 (**0 eligible paired games**).
3. **Local identity (MINI-v2 §1): PARTLY MET.** The six 12-14 Nov minis use distinct MINI_KEYs and valid local keys. The DRAFT011 package (strand B) labels its drafts with "proposed" keys `LOCAL-20261109R3NEXT-G0001…G0006` even though that namespace belonged to the repository mini, whose lease the chat did not hold and which was archived with zero cards. Those keys are treated as aliases only; none was consumed.
4. **Duplicate events: NOT MET at chat level, resolved at import.** The same 11 games were carded up to six times. Per the owner's decision, each game has one canonical ID; parallel records are addenda that consume no ID.
5. **Timing and issue phase (TIMING-v2): NOT MET for prospective use.** No record has a pre-start freeze. Of the 58 chat cards, 20 call their own phase post-scheduled-start, and the latest timestamp recorded in each card is after the scheduled start for at least 30 of them ([CARD_TIMING.csv](CARD_TIMING.csv); heuristic, because chats log request, research and write times inconsistently). Strand C's own intake rows put four of seven timed runs after the scheduled start (G004 +11 min, G008 +2.6 min, G009 +28 s, G010 after). Most requests arrived within 15 minutes of the scheduled start, and some after it (Tabilo–Tirante, Knicks–Pacers). **No record can be scored as a clean pre-start forecast.**
6. **Probabilities (ML-SEP-v1, MLSCOPE-v3): diagnostic only.** No record issued a `p_card` or `PICKS_V2` block. Numbers come from ad-hoc chat scripts (tennis Markov recursions, Poisson grids, Gaussian score grids) and the retired local v4.12 tool (strand C, a different and older method). None was validated or calibrated.
7. **Source permission (SRC-ALT-v3): NOT MET.** The chats never ran `ml source-audit`. Of 514 distinct URLs cited across all records, **20 are BLOCKED for the ChatGPT reader that opened them** (nba.com ×8, jumpball.co.kr ×8, tennistonic.com ×2, sports.yahoo.com, basketkorea.com) and **35 return RULES_UNKNOWN** (hokej.cz, sofascore.com, kbl.or.kr, protennislive.com and others). These should not have been opened ([CITED_URL_ACCESS_AUDIT_CHATGPT.csv](CITED_URL_ACCESS_AUDIT_CHATGPT.csv)).
8. **Market firewall (hard rule): no violation found; exposure disclosed.** No odds or prices entered any calculation. Some cards opened prediction/odds-bearing pages for statistics only (pythiatennis "prediction-and-stats", tennistonic previews, abasketballreport "predictions" head-to-head, one covers.com page for an injury note marked UNVERIFIED and not priced). Each card states that only stats or schedule fields were read. That fits the owner's stats-only rule, but it cannot be independently verified that the prediction text did not influence the analyst.
9. **Availability research (AVAIL-v4): INCOMPLETE everywhere.** No card had confirmed starters or goalies. Two decisive availability facts were known and named but not priced: Ellenson's return (Wonju–Suwon) and Froling/Okot (Tasmania–Southside).
10. **Learning logs (LEARNLOG-v1): absent.** No record initialised a pregame learning log, so none is built after the result. Terminal targets are retained for future reviewed development only.
11. **Format (mini-log-10): mostly met.** Exceptions: CHAT17C8C881 has no card markers; 8358B025 uses `CHAT_LOCAL_DRAFT` markers instead of `CARD`; strand A/B are research notes, not cards.

## 3. Problems in this settlement itself (disclosed)

- **One SRC-ALT breach by this session.** A delegated fetch for the Torpedo and Motor results ran before the source audit and opened hcmotor.cz, which the audit then returned as BLOCKED_FOR_AI for Claude-User. That content is excluded and not cited; the Motor U20 result rests on czehockey.cz (ALLOWED) and hcbilitygri.cz (NO_RULES_FILE). Every other settlement source was audited before it was cited.
- **Single-lineage results (evidence C):** Hercog–Lepchenko, Creighton–Kansas State (page titles only), Geelong–Perth, Piros–Altmaier and Knicks–Pacers. The scores agree with every search summary seen, but only one permitted page was opened and read.
- **Unresolved:** Urawa–Cerezo corner kicks (3 rows). Final wall-clock and actual first-play times are unverified for all 21 games.
- **Two near-misses in identity:** Torpedo–Arlan and Eagles–Abbotsford both had back-to-back rematches the next day (13 Nov Torpedo 3-2; 11 Nov Abbotsford 4-3). The cards' games were confirmed by date and native schedule row/time: Torpedo 4-1 (12 Nov) and Eagles 4-3 SO (10 Nov).

## 4. Results

Literal rows: 277 (131 WIN, 142 LOSS, 3 UNRESOLVED, 1 no-direction record). Numeric diagnostic rows: 206, mean Brier **0.2594**; a constant 0.5 forecast scores 0.2500. These rows are dependent (complementary pairs, parallel records on one game), so the figure is descriptive, not a skill test.

| Source | Rank-1 / first lean W-L | Top side W-L | Top total W-L | Numeric rows | Brier |
|---|---|---|---|---:|---:|
| EE4AFA68 | 6-5 | 2-9 | 7-4 | 0 | – |
| CHAT9538BF5E | 3-7 | 2-8 | 6-4 | 0 | – |
| 8358B025 | 6-5 | 5-6 | 8-3 | 44 | 0.2553 |
| CHAT17C8C881 | 4-5 | 3-6 | 6-3 | 33 | 0.2513 |
| CC53B5C806 | 6-3 | 4-5 | 7-2 | 33 | 0.2588 |
| D3C239297F (8 games) | 5-3 | 3-5 | 5-3 | 32 | 0.2476 |
| R3NEXT A (drafts) | 2-7 | 3-5 | 5-3 | 20 | 0.2469 |
| R3NEXT B (drafts) | 3-7 | 3-5 | 4-5 | 0 | – |
| R3NEXT C (v4.12) | – | 4-5 | 2-8 | 44 | 0.2844 |
| **All** | **35-42** | **29-54** | **50-35** | 206 | 0.2594 |

What the numbers say, without over-reading them:

- **Side leans failed badly (29-54); total leans did better (50-35).** The side losses cluster on underdog handicaps the chats liked for "cushion" reasons: Geelong +6.5 (lost by 19), Saga +9.5 (lost by 18), Svrčina +0.5, Piros +2.5, Liberec +1.5, Arlan +1.5, Southside +8.5 (lost by 20), Mobis +3.0, Toronto +1.5. The same pattern appeared in every chat, so it is one recurring judgement, repeated, not many independent errors.
- **The parallel chats mostly agreed with each other**, so carding a game six times did not add independent evidence. Where they disagreed on a side: in Tirante–Shevchenko and Tabilo–Tirante every numeric chat was right and the qualitative leans against them lost; in Svrčina–Virtanen the numeric chats split 2-2.
- **v4.12 totals went 2-8.** It priced unders at 54-64% on two-team-only samples with 32-75% data coverage.
- Nothing here can tune a parameter or certify skill: 21 games, no pre-start freeze, no calibrated reference.

## 5. Deep loss reviews

DEEPLOSS-v1 triggers: 131 losing rows across the records' top side, top total and rank-1 rows, grouped into **33 reviews** (one per game and losing contract, each with all 14 sections and a table of every record it covers) plus **10 joint sections** where a record's top side and top total both lost. They are in [SETTLEMENT.md](SETTLEMENT.md) and in Part 9 under each canonical ID. Main verdicts:

- **Should not have been made:** Geelong +6.5 (every opponent above .500 had beaten Geelong by 9+); Suwon KT +5.5 (Ellenson's return was known, named and left unpriced; he scored 28); Southside +8.5 (two Tasmanian frontcourt additions were known and unpriced); Piros +2.5 (Challenger form against a tour-level opponent; one chat's own stress case gave 35%); Under 159.5 for Creighton–Kansas State at 64-68% on two to four games of data; v4.12's 79.5% first-half Over in a rotated cup first leg.
- **Close or near-variance losses:** Abbotsford ML (3-3 game decided by one shootout goal); Perth -10.5 (margin exactly 10); Rutgers -21.5 (margin exactly 21); Over 22.5 in Piros–Altmaier (22 games).

## 6. Proposals (PROPOSED_NOT_TESTED; no rule changes)

1. **Run parallel chats as EXT-v3 lanes**, not as six complete cards: one manifest, five roles, one merged card. That is the only route to ASSESS-100 eligibility.
2. **Request games at least 30 minutes before the start.** Most requests in this drop arrived within 15 minutes of the scheduled start, which left the chats writing after it.
3. **Chat minis should record request, research-end and write times as three separate fields**; the current mix makes timing audits heuristic.
4. **Name-and-price rule for availability:** when a card names a returning or missing player as its main risk, it must show the line probability with and without that player (8358B025's Ellenson sensitivity is the model to follow).
5. **Underdog-cushion check:** before leaning a plus handicap, compare the favourite's record against opponents of similar strength, not only raw season margins. Test this on settled history before adopting it.
6. **Chats should run or import the source access lists** (`research/external/access/`) so blocked and rules-unknown hosts are not opened.
7. **Retire v4.12 numbers from the chats** or label them as a separate, older method; they are not comparable with v24 records.

## 7. What was done

Prompts 3 and 4 were run on all 90 records: settlement in [SETTLEMENT.md](SETTLEMENT.md), canonical IDs **P-639 to P-659** assigned in chronological order of scheduled start (one per game), all cores appended byte-exact to Part 9 with 113/113 readback blocks verified ([CANONICAL_IMPORT_REPORT.md](CANONICAL_IMPORT_REPORT.md)). Prompt 5 then closed Part 9 and opened Part 10.
