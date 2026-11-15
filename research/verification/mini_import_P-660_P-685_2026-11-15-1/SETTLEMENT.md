<!-- MINI-SETTLEMENT-FORMAT: mini-settlement-10 -->
# Settlement · owner drop OWNER_DROP_2026-11-15 · seven chat-local minis, 26 games, 75 cards

**Prompt 3 (P-2026.11.15-v24.18 · LOCAL_MINI_SETTLEMENT), LOCAL_WORKING_TREE** `C:\Users\danie\Projects\Sports-Research`, branch `main`, base HEAD `9934e37cef4ca179a7437a33e265de46cc9b5763`. Settlement effective 2026-11-15T12:09:48+00:00. Writer: repository agent (Claude Code) at the owner's request of 15 November 2026. Method MDS-2026.11.15-v24.20, scoring SCV-2026.11.15-v15, AUDIT-v1. Canonical IDs are **not** assigned in this document: every record's mapping is `NOT_ASSIGNED / PENDING_PROMPT_4_IMPORT`; the prompt-4 import report carries the final mapping.

**What this settles.** Every card in the drop, graded on its own frozen text against verified finals. All 75 cards are chat-local: none was issued, frozen, linted, reference-run or committed in the repository, so **every row is diagnostic (ANALYST_NOT_PRIMARY) and the primary denominator is zero.** Original orders, probabilities, leans and wording are copied literally; nothing is re-priced. The framework audit is in [AUDIT_REPORT.md](AUDIT_REPORT.md).

## FROZEN_SOURCE

Frozen at 2026-11-15T12:09:48+00:00 before any settlement text was written. The drop is copied byte-identically at `research/active_minis/received/OWNER_DROP_2026-11-15/` (53 files; SHA-256 comparison with the OneDrive folder: identical). Final minis used as sources are under `inputs/chat_minis/`. Per-card offsets, bytes and SHA-256 are in [FROZEN_SOURCE.csv](FROZEN_SOURCE.csv).

| Source mini | Bytes | SHA-256 | Cards | Notes |
|---|---:|---|---:|---|
| `20261114B4496A3F` | 285266 | `fce23543cbeccc73eb53575bd642ccb860bb5d3ce9944d2750304352480edf6a` | 10 | marker-bounded mini-log-10 cards; identical copy inside MINI_EXPORT_BUNDLE_20261114B4496A3F.zip; associated reference-input and model-result files retained in received/ |
| `202611148A011BE83FCC` | 90948 | `88bd3046a6ced194ead2e66505a56d228331e9ba5c63639768ea14c714e6db14` | 10 | heading-bounded (`## Event Gnnnn`) |
| `202611148C6C0822` | 88325 | `ffea26efa2a951693d6d599ff2c22eab9cac606a3af25979ae81850801d608ad` | 10 | heading-bounded; `_G0009_STAGED` byte-consistent earlier state; per-game evidence-queue appends retained inside each card span |
| `20261114CHAT2988664A` | 97758 | `c4595095a400bdf88eac3de3ce1146aa50bb0b0dc483c8c0838ad93b165944a3` | 10 | heading-bounded (`## CARD Gnnnn`) |
| `20261114EA6B2758F0` | 99938 | `9a77696fda3c25630d6db90105a548c85ad9843b68ffac666e7da5dbbd608c9a` | 9 | heading-bounded; earlier states `_G0004_preserved` and `_G0005_staged` are byte-consistent prefixes; no Hobart card |
| `CHAT20261114DDA525E495` | 170956 | `2e3919afcdb935b38d5e10d500496544c96fdfc2ef63781f37f9d53a0179f19e` | 10 | heading-bounded; `_G0006_SNAPSHOT`, `_G0007/8/9_UPDATED` are byte-consistent earlier states |
| `20261115CHAT48A8D395742B` | 419585 | `ce47d1f13a2e81a76a95b66dd2699fcfbf1ecc02df768f0b7f4e18e9138e842d` | 16 | complete export with marker-bounded cards; per-card extracts and SHA256SUMS retained in received/ |

Each 14 November mini's footer reserves a next key `G0010`/`G0011` that was never used; it is not a card. Footers are not settled.

## LOCAL_ID_MAPPING (pre-import; unchanged by the import)

| Record key | Event | Canonical ID | Status |
|---|---|---|---|
| `LOCAL-20261114B4496A3F-G0001` | Chicago State Cougars @ San Diego Toreros · 2026-11-13 PT | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-202611148A011BE83FCC-G0001` | Chicago State Cougars @ San Diego Toreros · 2026-11-13 PT | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-202611148C6C0822-G0001` | Chicago State Cougars @ San Diego Toreros · 2026-11-13 PT | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261114CHAT2988664A-G0001` | Chicago State Cougars @ San Diego Toreros · 2026-11-13 PT | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261114EA6B2758F0-G0001` | Chicago State Cougars @ San Diego Toreros · 2026-11-13 PT | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-CHAT20261114DDA525E495-G0001` | Chicago State Cougars @ San Diego Toreros · 2026-11-13 PT | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261114B4496A3F-G0002` | Hobart Hurricanes Women v Brisbane Heat Women · 2026-11-14 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-202611148A011BE83FCC-G0002` | Hobart Hurricanes Women v Brisbane Heat Women · 2026-11-14 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-202611148C6C0822-G0002` | Hobart Hurricanes Women v Brisbane Heat Women · 2026-11-14 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261114CHAT2988664A-G0002` | Hobart Hurricanes Women v Brisbane Heat Women · 2026-11-14 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-CHAT20261114DDA525E495-G0002` | Hobart Hurricanes Women v Brisbane Heat Women · 2026-11-14 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261114B4496A3F-G0003` | Perth Scorchers Women v Adelaide Strikers Women · 2026-11-14 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-202611148A011BE83FCC-G0003` | Perth Scorchers Women v Adelaide Strikers Women · 2026-11-14 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-202611148C6C0822-G0003` | Perth Scorchers Women v Adelaide Strikers Women · 2026-11-14 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261114CHAT2988664A-G0003` | Perth Scorchers Women v Adelaide Strikers Women · 2026-11-14 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261114EA6B2758F0-G0002` | Perth Scorchers Women v Adelaide Strikers Women · 2026-11-14 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-CHAT20261114DDA525E495-G0003` | Perth Scorchers Women v Adelaide Strikers Women · 2026-11-14 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261114B4496A3F-G0005` | Jonas Forejtek v Marvin Moeller · 2026-11-14 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-202611148A011BE83FCC-G0005` | Jonas Forejtek v Marvin Moeller · 2026-11-14 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-202611148C6C0822-G0005` | Jonas Forejtek v Marvin Moeller · 2026-11-14 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261114CHAT2988664A-G0005` | Jonas Forejtek v Marvin Moeller · 2026-11-14 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261114EA6B2758F0-G0004` | Jonas Forejtek v Marvin Moeller · 2026-11-14 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-CHAT20261114DDA525E495-G0005` | Jonas Forejtek v Marvin Moeller · 2026-11-14 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261114B4496A3F-G0004` | Tappara U20 v HPK U20 · 2026-11-14 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-202611148A011BE83FCC-G0004` | Tappara U20 v HPK U20 · 2026-11-14 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-202611148C6C0822-G0004` | Tappara U20 v HPK U20 · 2026-11-14 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261114CHAT2988664A-G0004` | Tappara U20 v HPK U20 · 2026-11-14 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261114EA6B2758F0-G0003` | Tappara U20 v HPK U20 · 2026-11-14 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-CHAT20261114DDA525E495-G0004` | Tappara U20 v HPK U20 · 2026-11-14 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261114B4496A3F-G0006` | Mountfield HK U20 v HC RT TORAX Poruba 2011 U20 · 2026-11-14 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-202611148A011BE83FCC-G0006` | Mountfield HK U20 v HC RT TORAX Poruba 2011 U20 · 2026-11-14 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-202611148C6C0822-G0006` | Mountfield HK U20 v HC RT TORAX Poruba 2011 U20 · 2026-11-14 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261114CHAT2988664A-G0006` | Mountfield HK U20 v HC RT TORAX Poruba 2011 U20 · 2026-11-14 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261114EA6B2758F0-G0005` | Mountfield HK U20 v HC RT TORAX Poruba 2011 U20 · 2026-11-14 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-CHAT20261114DDA525E495-G0006` | Mountfield HK U20 v HC RT TORAX Poruba 2011 U20 · 2026-11-14 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261114B4496A3F-G0007` | Alytaus Patriotai v Mažeikių M Basket · 2026-11-14 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-202611148A011BE83FCC-G0007` | Alytaus Patriotai v Mažeikių M Basket · 2026-11-14 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-202611148C6C0822-G0007` | Alytaus Patriotai v Mažeikių M Basket · 2026-11-14 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261114CHAT2988664A-G0007` | Alytaus Patriotai v Mažeikių M Basket · 2026-11-14 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261114EA6B2758F0-G0006` | Alytaus Patriotai v Mažeikių M Basket · 2026-11-14 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-CHAT20261114DDA525E495-G0007` | Alytaus Patriotai v Mažeikių M Basket · 2026-11-14 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261114B4496A3F-G0008` | Vimmerby HC v Nybro Vikings IF · 2026-11-14 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-202611148A011BE83FCC-G0008` | Vimmerby HC v Nybro Vikings IF · 2026-11-14 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-202611148C6C0822-G0008` | Vimmerby HC v Nybro Vikings IF · 2026-11-14 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261114CHAT2988664A-G0008` | Vimmerby HC v Nybro Vikings IF · 2026-11-14 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261114EA6B2758F0-G0007` | Vimmerby HC v Nybro Vikings IF · 2026-11-14 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-CHAT20261114DDA525E495-G0008` | Vimmerby HC v Nybro Vikings IF · 2026-11-14 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261114B4496A3F-G0009` | IF Malmö Redhawks v Växjö Lakers HC · 2026-11-14 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-202611148A011BE83FCC-G0009` | IF Malmö Redhawks v Växjö Lakers HC · 2026-11-14 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-202611148C6C0822-G0009` | IF Malmö Redhawks v Växjö Lakers HC · 2026-11-14 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261114CHAT2988664A-G0009` | IF Malmö Redhawks v Växjö Lakers HC · 2026-11-14 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261114EA6B2758F0-G0008` | IF Malmö Redhawks v Växjö Lakers HC · 2026-11-14 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-CHAT20261114DDA525E495-G0009` | IF Malmö Redhawks v Växjö Lakers HC · 2026-11-14 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261114B4496A3F-G0010` | AEK Athens v Doxa Lefkadas ELABET · 2026-11-14 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-202611148A011BE83FCC-G0010` | AEK Athens v Doxa Lefkadas ELABET · 2026-11-14 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-202611148C6C0822-G0010` | AEK Athens v Doxa Lefkadas ELABET · 2026-11-14 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261114CHAT2988664A-G0010` | AEK Athens v Doxa Lefkadas ELABET · 2026-11-14 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261114EA6B2758F0-G0009` | AEK Athens v Doxa Lefkadas ELABET · 2026-11-14 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-CHAT20261114DDA525E495-G0010` | AEK Athens v Doxa Lefkadas ELABET · 2026-11-14 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261115CHAT48A8D395742B-G0001` | Norway v Wales · 2026-11-14 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261115CHAT48A8D395742B-G0002` | Georgia Tech @ Clemson · 2026-11-14 ET | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261115CHAT48A8D395742B-G0003` | Alabama @ Vanderbilt · 2026-11-14 CT | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261115CHAT48A8D395742B-G0004` | Laval Rocket @ Rochester Americans · 2026-11-14 ET | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261115CHAT48A8D395742B-G0005` | Dallas Mavericks @ Cleveland Cavaliers · 2026-11-14 ET | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261115CHAT48A8D395742B-G0006` | Buffalo Sabres @ Dallas Stars · 2026-11-14 CT | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261115CHAT48A8D395742B-G0007` | Brooklyn Nets @ Memphis Grizzlies · 2026-11-14 CT | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261115CHAT48A8D395742B-G0008` | Chicago Bulls @ Minnesota Timberwolves · 2026-11-14 CT | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261115CHAT48A8D395742B-G0009` | Australia v England · 2026-11-15 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261115CHAT48A8D395742B-G0011` | Brisbane Bullets v Tasmania JackJumpers · 2026-11-15 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261115CHAT48A8D395742B-G0010` | Niigata Albirex BB v Gifu Swoops · 2026-11-15 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261115CHAT48A8D395742B-G0012` | Changwon LG Sakers v Suwon KT Sonicboom · 2026-11-15 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261115CHAT48A8D395742B-G0013` | Busan KCC Egis v Daegu KOGAS Pegasus · 2026-11-15 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261115CHAT48A8D395742B-G0014` | Kashiwa Reysol v Kawasaki Frontale · 2026-11-15 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261115CHAT48A8D395742B-G0015` | Australia v New Zealand · 2026-11-15 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261115CHAT48A8D395742B-G0016` | Dubai Basketball v Spartak Office Shoes Subotica · 2026-11-15 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |

## Event finals and sources

Every source below passed `python -m ml source-audit --reader CLAUDE_AGENT` (ALLOWED or NO_RULES_FILE) before it was opened. Search-engine summaries guided discovery only and are never cited as evidence. Two search leads were wrong games and are excluded (Malmö–Växjö 22 Sep, Vimmerby–Nybro 18 Sep).

| Event | Final | Periods | Evidence |
|---|---|---|---|
| Chicago State Cougars @ San Diego Toreros · 2026-11-13 PT | San Diego 87-67 Chicago State | Halves CSU 29-38, USD 46-41 (half 46-29 USD); no OT column | C |
| Hobart Hurricanes Women v Brisbane Heat Women · 2026-11-14 | Brisbane Heat won by 10 wickets: Hobart 86 all out (17.5 ov, batted first); Brisbane 0-88 (5.4 ov) | Hobart score after 6 completed overs NOT_VERIFIED (wicket marks '3-11' and '6-42' given without over numbers) | B |
| Perth Scorchers Women v Adelaide Strikers Women · 2026-11-14 | Adelaide Strikers 4-202 (20 ov, batted first) beat Perth Scorchers 9-150 by 52 runs | Adelaide 3-106 after 14 overs; 96 off the last six; six-over score NOT_VERIFIED | B |
| Jonas Forejtek v Marvin Moeller · 2026-11-14 | Moeller d. Forejtek 7-6(1) 6-1 (96 min) | Sets 7-6(1), 6-1; games Moeller 13, Forejtek 7; total 20 | B |
| Tappara U20 v HPK U20 · 2026-11-14 | NOT_VERIFIED (played as scheduled per fixture listings; no permitted page read showed the final) | NOT_VERIFIED | NONE |
| Mountfield HK U20 v HC RT TORAX Poruba 2011 U20 · 2026-11-14 | Mountfield HK 3-2 Poruba (regulation) | 1:0, 0:2, 2:0; goals 13' Černý, 32' Vaculík, 38' Latvens, 45' Vyvial, 59' D. Pavlík; 'konec (60')' | C |
| Alytaus Patriotai v Mažeikių M Basket · 2026-11-14 | Alytus 85-81 Mažeikiai | 29-19, 19-25, 16-16, 21-21 (half 48-44, after three 64-60); no OT | B |
| Vimmerby HC v Nybro Vikings IF · 2026-11-14 | Vimmerby 5-2 Nybro (regulation) | 1-0, 2-2, 2-0; 1,047 spectators, VBO Arena | B |
| IF Malmö Redhawks v Växjö Lakers HC · 2026-11-14 | Växjö 2-1 Malmö (at Malmö) | Nadeau scored both Växjö goals; period scores and regulation/OT NOT_VERIFIED | C |
| AEK Athens v Doxa Lefkadas ELABET · 2026-11-14 | Doxa Lefkadas 77-73 AEK (at SUNEL Arena) | Cumulative 13-27, 37-45, 59-60, 73-77 (AEK first); quarters AEK 13/24/22/14, Doxa 27/18/15/17; no OT | B |
| Norway v Wales · 2026-11-14 | Norway 3-1 Wales | HT 0-0 (derived: goals 59' Nusa, about 68' Schjelderup, 79' Brooks, 88' Haaland pen); corners Norway 8, Wales 2 (10) | B |
| Georgia Tech @ Clemson · 2026-11-14 ET | Georgia Tech 20-6 Clemson | Derived from narrative: GT 7-6-7-0, CLE 0-3-3-0; half 13-3; no OT | B |
| Alabama @ Vanderbilt · 2026-11-14 CT | Alabama 21-6 Vanderbilt | Quarter scoring NOT_VERIFIED from an opened page; no OT indicated | C |
| Laval Rocket @ Rochester Americans · 2026-11-14 ET | Rochester 5-4 Laval (OT); 4-4 after regulation | ROC 1-2-1-1, LAV 1-1-2-0; Kuntar 2:13 of OT; no shootout | C |
| Dallas Mavericks @ Cleveland Cavaliers · 2026-11-14 ET | Cleveland 127-117 Dallas | DAL 33-20-38-26, CLE 33-38-34-22; no OT | B |
| Buffalo Sabres @ Dallas Stars · 2026-11-14 CT | Dallas 2-0 Buffalo (regulation) | Benn 16:23 of 2nd; Johnston power play 19:18 of 3rd; no OT | B |
| Brooklyn Nets @ Memphis Grizzlies · 2026-11-14 CT | Memphis 129-110 Brooklyn | Half 71-54 Memphis; no OT | C |
| Chicago Bulls @ Minnesota Timberwolves · 2026-11-14 CT | Chicago 117-106 Minnesota | Quarter scores NOT_VERIFIED; no OT indicated | C |
| Australia v England · 2026-11-15 | England 355/6 (50 ov, batted first); result NOT read on an opened page | England after 5 completed overs NOT_VERIFIED; Duckett out for 9 'early' | C |
| Brisbane Bullets v Tasmania JackJumpers · 2026-11-15 | Tasmania 104-92 Brisbane (at Brisbane Entertainment Centre) | Q1 26-21 Brisbane; half 52-50 Brisbane; Q3 29-14 Tasmania (79-66); no OT | B |
| Niigata Albirex BB v Gifu Swoops · 2026-11-15 | Niigata 73-70 Gifu | 20-10, 19-30, 13-13, 21-17 (half 39-40 Gifu); no OT | B |
| Changwon LG Sakers v Suwon KT Sonicboom · 2026-11-15 | LG 83-81 KT | 64-64 after three quarters; winner with 0.6 s left; no OT indicated | C |
| Busan KCC Egis v Daegu KOGAS Pegasus · 2026-11-15 | KCC 80-77 KOGAS | Q1 16-27, half 34-47, after three 59-58 (KCC first); no OT indicated | C |
| Kashiwa Reysol v Kawasaki Frontale · 2026-11-15 | Kashiwa 5-4 Kawasaki (aggregate 7-5) | HT 1-3; Kawasaki 9', 25', 30', 81'; Kashiwa 45+2', 54', 60', 64', 72'; corners NOT_VERIFIED | B |
| Australia v New Zealand · 2026-11-15 | Australia 32-12 New Zealand | Half-time NOT_VERIFIED from an opened page; no golden point indicated | C |
| Dubai Basketball v Spartak Office Shoes Subotica · 2026-11-15 | Dubai 93-75 Spartak | Quarter scores NOT_VERIFIED; no OT indicated | C |

<!-- BEGIN SETTLEMENT EVENT E01 revision-1 -->
## Event · Chicago State Cougars @ San Diego Toreros · 2026-11-13 PT · NCAA Division I men 2026-27

**Final:** San Diego 87-67 Chicago State. **Periods:** Halves CSU 29-38, USD 46-41 (half 46-29 USD); no OT column. **Evidence C.** Scheduled 2026-11-14T02:30:00+00:00.

| Opened source | Audit | Field read |
|---|---|---|
| https://usdtoreros.com/news/2026/11/13/mens-basketball-san-diego-stays-undefeated-at-home-in-87-67-win-over-chicago-state.aspx | ALLOWED | 87-67; 'led 46-29 at the break'; period table 29/38/67 and 46/41/87 |

<!-- BEGIN SETTLEMENT LOCAL-20261114B4496A3F-G0001 revision-1 -->
### Settlement · `LOCAL-20261114B4496A3F-G0001` · Chicago State Cougars @ San Diego Toreros · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `f77d826f861e9aa9eef3b9e372f25f58cfa80d3df59efee754260e0c3aa31e53`, 25134 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/20261114B4496A3F.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `POST_SCHEDULED_START_WRITE` (last recorded `2026-11-14T13:39:34+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| R1 | Chicago State +16.5 | 0.6726 (chat-local uncalibrated scenario) | **LOSS** | side margin -20, handicap +16.5: -3.5 | 0.452391 |
| R2 | Over 140.5 | 0.6652 (chat-local uncalibrated scenario) | **WIN** | total 154 vs 140.5: +13.5 | 0.112091 |
| INFO | Under 140.5 | 0.3348 (chat-local uncalibrated scenario) | **LOSS** | total 154 vs 140.5: +13.5 | 0.112091 |
| INFO | San Diego -16.5 | 0.3274 (chat-local uncalibrated scenario) | **WIN** | side margin +20, handicap -16.5: +3.5 | 0.452391 |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_SIDE Chicago State +16.5 (0.6726) LOSS; TOP_TOTAL Over 140.5 (0.6652) WIN; RANK1 Chicago State +16.5 (0.6726) LOSS. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** San Diego 87-67 Chicago State; Halves CSU 29-38, USD 46-41 (half 46-29 USD); no OT column. Identity matched on participants, date and competition (NCAA Division I men 2026-27).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Basketball rows include overtime (BK-OT-1); none occurred.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final San Diego minus Chicago State = 20; total 154. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** San Diego led 46-29 at half and won the second half 41-38; the 20-point margin beat Chicago State +16.5 by 3.5. Total 154 cleared 140.5 by 13.5.
**R9. Source/timing review.** Settlement sources: https://usdtoreros.com/news/2026/11/13/mens-basketball-san-diego-stays-undefeated-at-home-in-87-67-win-over-chicago-state.aspx (ALLOWED). Card timing `POST_SCHEDULED_START_WRITE`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-20261114B4496A3F-G0001 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-202611148A011BE83FCC-G0001 revision-1 -->
### Settlement · `LOCAL-202611148A011BE83FCC-G0001` · Chicago State Cougars @ San Diego Toreros · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `fb59d8de2b560799fc7f0af026b57bfe21d3e4f48303ab486e36470171524a21`, 2684 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/202611148A011BE83FCC.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `PRE_SCHEDULED_START_WRITE` (last recorded `2026-11-14T13:28:16+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| LEAN_SIDE | Chicago State +16.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | side margin -20, handicap +16.5: -3.5 |  |
| NOT_PREF | San Diego -16.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | side margin +20, handicap -16.5: +3.5 |  |
| LEAN_TOTAL | Over 140.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | total 154 vs 140.5: +13.5 |  |
| NOT_PREF | Under 140.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | total 154 vs 140.5: +13.5 |  |
| LEAN_WINNER | San Diego to win | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | side margin +20 |  |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_SIDE Chicago State +16.5 (NOT_ESTIMATED) LOSS; TOP_TOTAL Over 140.5 (NOT_ESTIMATED) WIN; RANK1 Chicago State +16.5 (NOT_ESTIMATED) LOSS. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** San Diego 87-67 Chicago State; Halves CSU 29-38, USD 46-41 (half 46-29 USD); no OT column. Identity matched on participants, date and competition (NCAA Division I men 2026-27).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Basketball rows include overtime (BK-OT-1); none occurred.
**R4. Rank diagnostics.** 3W/2L/0U over 5 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final San Diego minus Chicago State = 20; total 154. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** San Diego led 46-29 at half and won the second half 41-38; the 20-point margin beat Chicago State +16.5 by 3.5. Total 154 cleared 140.5 by 13.5.
**R9. Source/timing review.** Settlement sources: https://usdtoreros.com/news/2026/11/13/mens-basketball-san-diego-stays-undefeated-at-home-in-87-67-win-over-chicago-state.aspx (ALLOWED). Card timing `PRE_SCHEDULED_START_WRITE`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-202611148A011BE83FCC-G0001 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-202611148C6C0822-G0001 revision-1 -->
### Settlement · `LOCAL-202611148C6C0822-G0001` · Chicago State Cougars @ San Diego Toreros · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `4f0ce4005bc0c35f37704a0c2d0e096f953971b050cb378c1d94ceb995c5c26d`, 4125 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/202611148C6C0822.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `PRE_SCHEDULED_START_WRITE` (last recorded `2026-11-14T13:28:20+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| LEAN_SIDE | Chicago State +16.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | side margin -20, handicap +16.5: -3.5 |  |
| NOT_PREF | San Diego -16.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | side margin +20, handicap -16.5: +3.5 |  |
| LEAN_TOTAL | Over 140.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | total 154 vs 140.5: +13.5 |  |
| NOT_PREF | Under 140.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | total 154 vs 140.5: +13.5 |  |
| LEAN_WINNER | San Diego to win | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | side margin +20 |  |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_SIDE Chicago State +16.5 (NOT_ESTIMATED) LOSS; TOP_TOTAL Over 140.5 (NOT_ESTIMATED) WIN; RANK1 Chicago State +16.5 (NOT_ESTIMATED) LOSS. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** San Diego 87-67 Chicago State; Halves CSU 29-38, USD 46-41 (half 46-29 USD); no OT column. Identity matched on participants, date and competition (NCAA Division I men 2026-27).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Basketball rows include overtime (BK-OT-1); none occurred.
**R4. Rank diagnostics.** 3W/2L/0U over 5 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final San Diego minus Chicago State = 20; total 154. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** San Diego led 46-29 at half and won the second half 41-38; the 20-point margin beat Chicago State +16.5 by 3.5. Total 154 cleared 140.5 by 13.5.
**R9. Source/timing review.** Settlement sources: https://usdtoreros.com/news/2026/11/13/mens-basketball-san-diego-stays-undefeated-at-home-in-87-67-win-over-chicago-state.aspx (ALLOWED). Card timing `PRE_SCHEDULED_START_WRITE`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-202611148C6C0822-G0001 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-20261114CHAT2988664A-G0001 revision-1 -->
### Settlement · `LOCAL-20261114CHAT2988664A-G0001` · Chicago State Cougars @ San Diego Toreros · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `41469464e814088ce9c5b0a570437f26e3338384125db0db21bc0d7d33698c5f`, 5240 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/20261114CHAT2988664A.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `WRITE_TIME_NOT_RECORDED` (last recorded `NOT_RECORDED`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| R2 | Chicago State +16.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | side margin -20, handicap +16.5: -3.5 |  |
| NOT_PREF | San Diego -16.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | side margin +20, handicap -16.5: +3.5 |  |
| R1 | Over 140.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | total 154 vs 140.5: +13.5 |  |
| NOT_PREF | Under 140.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | total 154 vs 140.5: +13.5 |  |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_SIDE Chicago State +16.5 (NOT_ESTIMATED) LOSS; TOP_TOTAL Over 140.5 (NOT_ESTIMATED) WIN; RANK1 Over 140.5 (NOT_ESTIMATED) WIN. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** San Diego 87-67 Chicago State; Halves CSU 29-38, USD 46-41 (half 46-29 USD); no OT column. Identity matched on participants, date and competition (NCAA Division I men 2026-27).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Basketball rows include overtime (BK-OT-1); none occurred.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final San Diego minus Chicago State = 20; total 154. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** San Diego led 46-29 at half and won the second half 41-38; the 20-point margin beat Chicago State +16.5 by 3.5. Total 154 cleared 140.5 by 13.5.
**R9. Source/timing review.** Settlement sources: https://usdtoreros.com/news/2026/11/13/mens-basketball-san-diego-stays-undefeated-at-home-in-87-67-win-over-chicago-state.aspx (ALLOWED). Card timing `WRITE_TIME_NOT_RECORDED`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-20261114CHAT2988664A-G0001 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-20261114EA6B2758F0-G0001 revision-1 -->
### Settlement · `LOCAL-20261114EA6B2758F0-G0001` · Chicago State Cougars @ San Diego Toreros · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `fc4e135aed500bc99434c31f31ce2a09c7ffecbe57e05f222b013a18d721bc44`, 3266 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/20261114EA6B2758F0.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `PRE_SCHEDULED_START_WRITE` (last recorded `2026-11-14T13:25:22+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| LEAN_SIDE | Chicago State +16.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | side margin -20, handicap +16.5: -3.5 |  |
| NOT_PREF | San Diego -16.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | side margin +20, handicap -16.5: +3.5 |  |
| LEAN_TOTAL | Over 140.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | total 154 vs 140.5: +13.5 |  |
| NOT_PREF | Under 140.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | total 154 vs 140.5: +13.5 |  |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_SIDE Chicago State +16.5 (NOT_ESTIMATED) LOSS; TOP_TOTAL Over 140.5 (NOT_ESTIMATED) WIN; RANK1 Chicago State +16.5 (NOT_ESTIMATED) LOSS. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** San Diego 87-67 Chicago State; Halves CSU 29-38, USD 46-41 (half 46-29 USD); no OT column. Identity matched on participants, date and competition (NCAA Division I men 2026-27).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Basketball rows include overtime (BK-OT-1); none occurred.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final San Diego minus Chicago State = 20; total 154. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** San Diego led 46-29 at half and won the second half 41-38; the 20-point margin beat Chicago State +16.5 by 3.5. Total 154 cleared 140.5 by 13.5.
**R9. Source/timing review.** Settlement sources: https://usdtoreros.com/news/2026/11/13/mens-basketball-san-diego-stays-undefeated-at-home-in-87-67-win-over-chicago-state.aspx (ALLOWED). Card timing `PRE_SCHEDULED_START_WRITE`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-20261114EA6B2758F0-G0001 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-CHAT20261114DDA525E495-G0001 revision-1 -->
### Settlement · `LOCAL-CHAT20261114DDA525E495-G0001` · Chicago State Cougars @ San Diego Toreros · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `3ea3e175a664de342a01422ffa742b2ffc737ac39147e809e97e6d56efab5644`, 13536 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/CHAT20261114DDA525E495.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `PRE_SCHEDULED_START_WRITE` (last recorded `2026-11-14T13:25:19+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| R1 | Over 140.5 | 0.63197 (chat-local uncalibrated scenario) | **WIN** | total 154 vs 140.5: +13.5 | 0.135446 |
| R2 | Chicago State +16.5 | 0.60443 (chat-local uncalibrated scenario) | **LOSS** | side margin -20, handicap +16.5: -3.5 | 0.365336 |
| NOT_RANKED | San Diego -16.5 | 0.39557 (chat-local uncalibrated scenario) | **WIN** | side margin +20, handicap -16.5: +3.5 | 0.365336 |
| NOT_RANKED | Under 140.5 | 0.36803 (chat-local uncalibrated scenario) | **LOSS** | total 154 vs 140.5: +13.5 | 0.135446 |
| INFO | San Diego to win | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | side margin +20 |  |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_SIDE Chicago State +16.5 (0.60443) LOSS; TOP_TOTAL Over 140.5 (0.63197) WIN; RANK1 Over 140.5 (0.63197) WIN. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** San Diego 87-67 Chicago State; Halves CSU 29-38, USD 46-41 (half 46-29 USD); no OT column. Identity matched on participants, date and competition (NCAA Division I men 2026-27).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Basketball rows include overtime (BK-OT-1); none occurred.
**R4. Rank diagnostics.** 3W/2L/0U over 5 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final San Diego minus Chicago State = 20; total 154. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** San Diego led 46-29 at half and won the second half 41-38; the 20-point margin beat Chicago State +16.5 by 3.5. Total 154 cleared 140.5 by 13.5.
**R9. Source/timing review.** Settlement sources: https://usdtoreros.com/news/2026/11/13/mens-basketball-san-diego-stays-undefeated-at-home-in-87-67-win-over-chicago-state.aspx (ALLOWED). Card timing `PRE_SCHEDULED_START_WRITE`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-CHAT20261114DDA525E495-G0001 revision-1 -->

### Deep loss reviews (DEEPLOSS-v1)

#### Deep loss review · Chicago State Cougars @ San Diego Toreros · Chicago State +16.5

**1. Exact frozen claim.** `Chicago State +16.5`, full-game endpoint as each card defined it. Triggered in 6 card(s):

| Card | Trigger role(s) | Original p (basis) | Brier | Log loss |
|---|---|---|---:|---:|
| `LOCAL-202611148A011BE83FCC-G0001` | TOP_SIDE, RANK1 | NOT_ESTIMATED (qualitative (no numeric p)) |  |  |
| `LOCAL-202611148C6C0822-G0001` | TOP_SIDE, RANK1 | NOT_ESTIMATED (qualitative (no numeric p)) |  |  |
| `LOCAL-20261114B4496A3F-G0001` | TOP_SIDE, RANK1 | 0.6726 (chat-local uncalibrated scenario) | 0.452391 | 1.116573 |
| `LOCAL-20261114CHAT2988664A-G0001` | TOP_SIDE | NOT_ESTIMATED (qualitative (no numeric p)) |  |  |
| `LOCAL-20261114EA6B2758F0-G0001` | TOP_SIDE, RANK1 | NOT_ESTIMATED (qualitative (no numeric p)) |  |  |
| `LOCAL-CHAT20261114DDA525E495-G0001` | TOP_SIDE | 0.60443 (chat-local uncalibrated scenario) | 0.365336 | 0.927428 |

No card carried a primary p_card, frozen reference or same-row baseline; BASELINE_P comparison NOT_COMPUTABLE.

**2. Verified outcome.** San Diego 87-67 Chicago State (Halves CSU 29-38, USD 46-41 (half 46-29 USD); no OT column). side margin -20, handicap +16.5: -3.5. Sources in R9; evidence C; final wall-clock NOT_VERIFIED.
**3. Distribution check.** Numeric cards priced this row at 0.604-0.673; a loss at those prices is a 33%-40% event under each card's own uncalibrated object.
**4. Error decomposition.** Realised distance: side margin -20, handicap +16.5: -3.5. No card had a calibrated centre or a measured effect row, so the miss is not split into reference and adjustment error; no blame shares are invented.
**5. Research audit.** Six cards on the same public inputs: Chicago State's 81-62 road win at Cal Baptist and Price's scoring were treated as cushion evidence, while the 59-109 loss at Texas (the only strong opponent CSU had met) and CSU's 15 newcomers were noted but not weighed. No card measured opponent strength; the 2-2 and 2-1 records came against mostly weak schedules. DDA's 0.604 and B44's 0.673 came from analyst-chosen margin centres (+12 and +8.45) with no fitted reference.
**6. What decided the game.** San Diego led 46-29 at half and won the second half 41-38; the 20-point margin beat Chicago State +16.5 by 3.5. Total 154 cleared 140.5 by 13.5.
**7. Knowable at cutoff?** Knowable: CSU's 50-point loss to the one high-major opponent, USD's 83.3 points per game, and that a 16.5 line already implied a lopsided game. Not knowable: San Diego's 46-29 first half.
**8. Process audit.** Chat-local record; no repository reference stage, no source-audit receipts, no lineup confirmation, no freeze. Timing per card in CARD_TIMING.csv.
**9. Verdict.** ERROR (plus-handicap without an opponent-strength check). The cushion rested on one win over a weak team. Under AUDIT-v1 this row would now need a CHECKED opponent review or stay UNPRICED; it should not have been a lean. The matched Over 140.5 win came from the same unvalidated scoring centres.
**10. Cutoff-only counterfactual.** NOT_ESTIMATED: no knowable fact has a measured effect-table row, so no corrected probability is priced after the result.
**11. Failure class and recurrence.** Shared across 6 cards on one game: overlapping public inputs make these one dependent observation, not 6.
**12. Correction.** NO_CHANGE to any rule from one result. Pattern-level proposals are in AUDIT_REPORT (PROPOSED_NOT_TESTED).
**13. Matched wins.** `LOCAL-202611148A011BE83FCC-G0001` TOP_TOTAL Over 140.5 WIN; `LOCAL-202611148C6C0822-G0001` TOP_TOTAL Over 140.5 WIN; `LOCAL-20261114B4496A3F-G0001` TOP_TOTAL Over 140.5 WIN; `LOCAL-20261114CHAT2988664A-G0001` RANK1 Over 140.5 WIN; `LOCAL-20261114CHAT2988664A-G0001` TOP_TOTAL Over 140.5 WIN; `LOCAL-20261114EA6B2758F0-G0001` TOP_TOTAL Over 140.5 WIN; `LOCAL-CHAT20261114DDA525E495-G0001` RANK1 Over 140.5 WIN; `LOCAL-CHAT20261114DDA525E495-G0001` TOP_TOTAL Over 140.5 WIN. These rest on the same unvalidated construction and do not show the process worked.
**14. Honesty.** Original numbers and labels preserved; no luck claim without the arithmetic above; no invented percentages, operator terms or publication times.

<!-- END SETTLEMENT EVENT E01 revision-1 -->

<!-- BEGIN SETTLEMENT EVENT E02 revision-1 -->
## Event · Hobart Hurricanes Women v Brisbane Heat Women · 2026-11-14 · WBBL|12 Match 21, Bellerive Oval / Ninja Stadium, Hobart

**Final:** Brisbane Heat won by 10 wickets: Hobart 86 all out (17.5 ov, batted first); Brisbane 0-88 (5.4 ov). **Periods:** Hobart score after 6 completed overs NOT_VERIFIED (wicket marks '3-11' and '6-42' given without over numbers). **Evidence B.** Scheduled 2026-11-14T04:40:00+00:00. Note: Six-over rows UNRESOLVED (ESPNcricinfo RULES_UNKNOWN, crex BLOCKED_FOR_AI; cricket.com.au scorecard script-loaded).

| Opened source | Audit | Field read |
|---|---|---|
| https://www.brisbaneheat.com.au/news/4608979/white-hot-heat-records-tumble-in-hobart | ALLOWED | 'the Hurricanes batted first'; 'bundling Hobart out for 86'; chase 'in just 5.4 overs' |
| https://aapnews.aap.com.au/news/heat-hammer-hurricanes-in-wbbl-scorchers-finally-lose | ALLOWED | 'for 86 in 17.5 overs'; '3-11' and '6-42' inside the powerplay, no over numbers |
| https://cricket.com.au/matches/CA:40641?tab=scorecard | ALLOWED | Match identity confirmed; scorecard rows script-loaded, not read |

<!-- BEGIN SETTLEMENT LOCAL-20261114B4496A3F-G0002 revision-1 -->
### Settlement · `LOCAL-20261114B4496A3F-G0002` · Hobart Hurricanes Women v Brisbane Heat Women · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `3ef92b3c4059a0144f2b675503985938ff95c641b03cf9b2894c59f7d1505e1c`, 27112 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/20261114B4496A3F.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `PRE_SCHEDULED_START_WRITE` (last recorded `2026-11-14T15:35:35+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| R1 | Hobart 6 overs Under 41.5 | 0.6305 (chat-local uncalibrated scenario) | **UNRESOLVED** | phase score NOT_VERIFIED |  |
| R2 | Hobart innings Under 152.5 | 0.6284 (chat-local uncalibrated scenario) | **WIN** | innings runs 86 vs 152.5: -66.5 | 0.138087 |
| INFO | Hobart innings Over 152.5 | 0.3716 (chat-local uncalibrated scenario) | **LOSS** | innings runs 86 vs 152.5: -66.5 | 0.138087 |
| INFO | Hobart 6 overs Over 41.5 | 0.3695 (chat-local uncalibrated scenario) | **UNRESOLVED** | phase score NOT_VERIFIED |  |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_TOTAL Hobart innings Under 152.5 (0.6284) WIN; RANK1 Hobart 6 overs Under 41.5 (0.6305) UNRESOLVED. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** Brisbane Heat won by 10 wickets: Hobart 86 all out (17.5 ov, batted first); Brisbane 0-88 (5.4 ov); Hobart score after 6 completed overs NOT_VERIFIED (wicket marks '3-11' and '6-42' given without over numbers). Identity matched on participants, date and competition (WBBL|12 Match 21, Bellerive Oval / Ninja Stadium, Hobart).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Cricket rows: innings totals at completion (all out counts as completion); phase rows need the score at the stated completed over.
**R4. Rank diagnostics.** 1W/1L/2U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final Hobart innings runs = 86; total 86. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** Hobart were 3-11 and then 6-42 and were all out for 86 in 17.5 overs, 66.5 runs under 152.5. Their six-over score was not published on any permitted page read.
**R9. Source/timing review.** Settlement sources: https://www.brisbaneheat.com.au/news/4608979/white-hot-heat-records-tumble-in-hobart (ALLOWED); https://aapnews.aap.com.au/news/heat-hammer-hurricanes-in-wbbl-scorchers-finally-lose (ALLOWED); https://cricket.com.au/matches/CA:40641?tab=scorecard (ALLOWED). Card timing `PRE_SCHEDULED_START_WRITE`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-20261114B4496A3F-G0002 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-202611148A011BE83FCC-G0002 revision-1 -->
### Settlement · `LOCAL-202611148A011BE83FCC-G0002` · Hobart Hurricanes Women v Brisbane Heat Women · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `371f92e65db3d96e7870175f2040a8d4d864d152b0430af2491cb9b076409731`, 3187 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/202611148A011BE83FCC.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `PRE_SCHEDULED_START_WRITE` (last recorded `2026-11-14T15:30:00+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| NOT_PREF | Hobart 6 overs Over 41.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **UNRESOLVED** | phase score NOT_VERIFIED |  |
| R2 | Hobart 6 overs Under 41.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **UNRESOLVED** | phase score NOT_VERIFIED |  |
| NOT_PREF | Hobart innings Over 152.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | innings runs 86 vs 152.5: -66.5 |  |
| R1 | Hobart innings Under 152.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | innings runs 86 vs 152.5: -66.5 |  |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_TOTAL Hobart innings Under 152.5 (NOT_ESTIMATED) WIN; RANK1 Hobart innings Under 152.5 (NOT_ESTIMATED) WIN. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** Brisbane Heat won by 10 wickets: Hobart 86 all out (17.5 ov, batted first); Brisbane 0-88 (5.4 ov); Hobart score after 6 completed overs NOT_VERIFIED (wicket marks '3-11' and '6-42' given without over numbers). Identity matched on participants, date and competition (WBBL|12 Match 21, Bellerive Oval / Ninja Stadium, Hobart).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Cricket rows: innings totals at completion (all out counts as completion); phase rows need the score at the stated completed over.
**R4. Rank diagnostics.** 1W/1L/2U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final Hobart innings runs = 86; total 86. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** Hobart were 3-11 and then 6-42 and were all out for 86 in 17.5 overs, 66.5 runs under 152.5. Their six-over score was not published on any permitted page read.
**R9. Source/timing review.** Settlement sources: https://www.brisbaneheat.com.au/news/4608979/white-hot-heat-records-tumble-in-hobart (ALLOWED); https://aapnews.aap.com.au/news/heat-hammer-hurricanes-in-wbbl-scorchers-finally-lose (ALLOWED); https://cricket.com.au/matches/CA:40641?tab=scorecard (ALLOWED). Card timing `PRE_SCHEDULED_START_WRITE`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-202611148A011BE83FCC-G0002 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-202611148C6C0822-G0002 revision-1 -->
### Settlement · `LOCAL-202611148C6C0822-G0002` · Hobart Hurricanes Women v Brisbane Heat Women · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `5b2f6d08466502fe742dbb4fd22a78c9d34580c787ed69c3df59eeefdcf48c15`, 3979 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/202611148C6C0822.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `WRITE_TIME_NOT_RECORDED` (last recorded `NOT_RECORDED`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| R2 | Hobart 6 overs Under 41.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **UNRESOLVED** | phase score NOT_VERIFIED |  |
| NOT_PREF | Hobart 6 overs Over 41.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **UNRESOLVED** | phase score NOT_VERIFIED |  |
| R1 | Hobart innings Under 152.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | innings runs 86 vs 152.5: -66.5 |  |
| NOT_PREF | Hobart innings Over 152.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | innings runs 86 vs 152.5: -66.5 |  |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_TOTAL Hobart innings Under 152.5 (NOT_ESTIMATED) WIN; RANK1 Hobart innings Under 152.5 (NOT_ESTIMATED) WIN. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** Brisbane Heat won by 10 wickets: Hobart 86 all out (17.5 ov, batted first); Brisbane 0-88 (5.4 ov); Hobart score after 6 completed overs NOT_VERIFIED (wicket marks '3-11' and '6-42' given without over numbers). Identity matched on participants, date and competition (WBBL|12 Match 21, Bellerive Oval / Ninja Stadium, Hobart).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Cricket rows: innings totals at completion (all out counts as completion); phase rows need the score at the stated completed over.
**R4. Rank diagnostics.** 1W/1L/2U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final Hobart innings runs = 86; total 86. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** Hobart were 3-11 and then 6-42 and were all out for 86 in 17.5 overs, 66.5 runs under 152.5. Their six-over score was not published on any permitted page read.
**R9. Source/timing review.** Settlement sources: https://www.brisbaneheat.com.au/news/4608979/white-hot-heat-records-tumble-in-hobart (ALLOWED); https://aapnews.aap.com.au/news/heat-hammer-hurricanes-in-wbbl-scorchers-finally-lose (ALLOWED); https://cricket.com.au/matches/CA:40641?tab=scorecard (ALLOWED). Card timing `WRITE_TIME_NOT_RECORDED`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-202611148C6C0822-G0002 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-20261114CHAT2988664A-G0002 revision-1 -->
### Settlement · `LOCAL-20261114CHAT2988664A-G0002` · Hobart Hurricanes Women v Brisbane Heat Women · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `82ec9b307d177758d30c068d4c12348a2d7e0f2eeaf9dab75735978868b32e85`, 4137 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/20261114CHAT2988664A.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `WRITE_TIME_NOT_RECORDED` (last recorded `NOT_RECORDED`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| R2 | Hobart 6 overs Under 41.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **UNRESOLVED** | phase score NOT_VERIFIED |  |
| NOT_PREF | Hobart 6 overs Over 41.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **UNRESOLVED** | phase score NOT_VERIFIED |  |
| R1 | Hobart innings Under 152.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | innings runs 86 vs 152.5: -66.5 |  |
| NOT_PREF | Hobart innings Over 152.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | innings runs 86 vs 152.5: -66.5 |  |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_TOTAL Hobart innings Under 152.5 (NOT_ESTIMATED) WIN; RANK1 Hobart innings Under 152.5 (NOT_ESTIMATED) WIN. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** Brisbane Heat won by 10 wickets: Hobart 86 all out (17.5 ov, batted first); Brisbane 0-88 (5.4 ov); Hobart score after 6 completed overs NOT_VERIFIED (wicket marks '3-11' and '6-42' given without over numbers). Identity matched on participants, date and competition (WBBL|12 Match 21, Bellerive Oval / Ninja Stadium, Hobart).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Cricket rows: innings totals at completion (all out counts as completion); phase rows need the score at the stated completed over.
**R4. Rank diagnostics.** 1W/1L/2U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final Hobart innings runs = 86; total 86. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** Hobart were 3-11 and then 6-42 and were all out for 86 in 17.5 overs, 66.5 runs under 152.5. Their six-over score was not published on any permitted page read.
**R9. Source/timing review.** Settlement sources: https://www.brisbaneheat.com.au/news/4608979/white-hot-heat-records-tumble-in-hobart (ALLOWED); https://aapnews.aap.com.au/news/heat-hammer-hurricanes-in-wbbl-scorchers-finally-lose (ALLOWED); https://cricket.com.au/matches/CA:40641?tab=scorecard (ALLOWED). Card timing `WRITE_TIME_NOT_RECORDED`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-20261114CHAT2988664A-G0002 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-CHAT20261114DDA525E495-G0002 revision-1 -->
### Settlement · `LOCAL-CHAT20261114DDA525E495-G0002` · Hobart Hurricanes Women v Brisbane Heat Women · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `0feac596acb90058e3c0e91537299cc533fc80e4b308427e2923f20d96eb2e1c`, 17538 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/CHAT20261114DDA525E495.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `PRE_SCHEDULED_START_WRITE` (last recorded `2026-11-14T15:38:19+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| R1 | Hobart innings Under 152.5 | 0.65348 (chat-local uncalibrated scenario) | **WIN** | innings runs 86 vs 152.5: -66.5 | 0.120076 |
| NOT_RANKED | Hobart innings Over 152.5 | 0.34652 (chat-local uncalibrated scenario) | **LOSS** | innings runs 86 vs 152.5: -66.5 | 0.120076 |
| R2 | Hobart 6 overs Under 41.5 | 0.63121 (chat-local uncalibrated scenario) | **UNRESOLVED** | phase score NOT_VERIFIED |  |
| NOT_RANKED | Hobart 6 overs Over 41.5 | 0.36879 (chat-local uncalibrated scenario) | **UNRESOLVED** | phase score NOT_VERIFIED |  |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_TOTAL Hobart innings Under 152.5 (0.65348) WIN; RANK1 Hobart innings Under 152.5 (0.65348) WIN. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** Brisbane Heat won by 10 wickets: Hobart 86 all out (17.5 ov, batted first); Brisbane 0-88 (5.4 ov); Hobart score after 6 completed overs NOT_VERIFIED (wicket marks '3-11' and '6-42' given without over numbers). Identity matched on participants, date and competition (WBBL|12 Match 21, Bellerive Oval / Ninja Stadium, Hobart).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Cricket rows: innings totals at completion (all out counts as completion); phase rows need the score at the stated completed over.
**R4. Rank diagnostics.** 1W/1L/2U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final Hobart innings runs = 86; total 86. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** Hobart were 3-11 and then 6-42 and were all out for 86 in 17.5 overs, 66.5 runs under 152.5. Their six-over score was not published on any permitted page read.
**R9. Source/timing review.** Settlement sources: https://www.brisbaneheat.com.au/news/4608979/white-hot-heat-records-tumble-in-hobart (ALLOWED); https://aapnews.aap.com.au/news/heat-hammer-hurricanes-in-wbbl-scorchers-finally-lose (ALLOWED); https://cricket.com.au/matches/CA:40641?tab=scorecard (ALLOWED). Card timing `PRE_SCHEDULED_START_WRITE`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-CHAT20261114DDA525E495-G0002 revision-1 -->

<!-- END SETTLEMENT EVENT E02 revision-1 -->

<!-- BEGIN SETTLEMENT EVENT E03 revision-1 -->
## Event · Perth Scorchers Women v Adelaide Strikers Women · 2026-11-14 · WBBL|12 Match 22, WACA Ground, Perth

**Final:** Adelaide Strikers 4-202 (20 ov, batted first) beat Perth Scorchers 9-150 by 52 runs. **Periods:** Adelaide 3-106 after 14 overs; 96 off the last six; six-over score NOT_VERIFIED. **Evidence B.** Scheduled 2026-11-14T08:10:00+00:00. Note: Six-over rows UNRESOLVED (no permitted page gave the 6-over score). AAP's 51-run margin is inconsistent with 202-150; 52 used.

| Opened source | Audit | Field read |
|---|---|---|
| https://aapnews.aap.com.au/news/heat-hammer-hurricanes-in-wbbl-scorchers-finally-lose | ALLOWED | '4-202'; '9-150 in reply'; '3-106 after 14'; says 'by 51 runs' (inconsistent with its own scores) |
| https://www.crictracker.com/cricket-news/mushangwes-5-11-ends-perth-scorchers-unbeaten-run-as-strikers-post-record-total-9270/ | ALLOWED | '4-202', '9-150', 'by 52 runs'; '3-106 after 14 overs' |
| https://www.cricket.com.au/news/4609036/perth-scorchers-adelaide-strikers-wbbl12-match-report-highlights-waca-wolvaardt-mushangwe-de-broughe-penna-devine-mooney-king | ALLOWED | '4-202'; '9-150 in reply'; '96 off the last six' |

<!-- BEGIN SETTLEMENT LOCAL-20261114B4496A3F-G0003 revision-1 -->
### Settlement · `LOCAL-20261114B4496A3F-G0003` · Perth Scorchers Women v Adelaide Strikers Women · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `f2dc2d7c67b8e3adc43fd19013e9cb5207a3182d4ed19a924e5af5cb7cd24c06`, 30929 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/20261114B4496A3F.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `POST_SCHEDULED_START_WRITE` (last recorded `2026-11-14T19:13:38+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| R1 | Adelaide innings Over 150.5 | 0.5596 (chat-local uncalibrated scenario) | **WIN** | innings runs 202 vs 150.5: +51.5 | 0.193952 |
| R2 | Adelaide 6 overs Over 41.5 | 0.5356 (chat-local uncalibrated scenario) | **UNRESOLVED** | phase score NOT_VERIFIED |  |
| INFO | Adelaide 6 overs Under 41.5 | 0.4644 (chat-local uncalibrated scenario) | **UNRESOLVED** | phase score NOT_VERIFIED |  |
| INFO | Adelaide innings Under 150.5 | 0.4404 (chat-local uncalibrated scenario) | **LOSS** | innings runs 202 vs 150.5: +51.5 | 0.193952 |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_TOTAL Adelaide innings Over 150.5 (0.5596) WIN; RANK1 Adelaide innings Over 150.5 (0.5596) WIN. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** Adelaide Strikers 4-202 (20 ov, batted first) beat Perth Scorchers 9-150 by 52 runs; Adelaide 3-106 after 14 overs; 96 off the last six; six-over score NOT_VERIFIED. Identity matched on participants, date and competition (WBBL|12 Match 22, WACA Ground, Perth).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Cricket rows: innings totals at completion (all out counts as completion); phase rows need the score at the stated completed over.
**R4. Rank diagnostics.** 1W/1L/2U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final Adelaide innings runs = 202; total 202. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** Adelaide batted first and made a franchise-record 4-202: 3-106 after 14 overs, then 96 off the last six (a WBBL-record 40-run Power Surge). 202 beat 150.5 by 51.5.
**R9. Source/timing review.** Settlement sources: https://aapnews.aap.com.au/news/heat-hammer-hurricanes-in-wbbl-scorchers-finally-lose (ALLOWED); https://www.crictracker.com/cricket-news/mushangwes-5-11-ends-perth-scorchers-unbeaten-run-as-strikers-post-record-total-9270/ (ALLOWED); https://www.cricket.com.au/news/4609036/perth-scorchers-adelaide-strikers-wbbl12-match-report-highlights-waca-wolvaardt-mushangwe-de-broughe-penna-devine-mooney-king (ALLOWED). Card timing `POST_SCHEDULED_START_WRITE`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-20261114B4496A3F-G0003 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-202611148A011BE83FCC-G0003 revision-1 -->
### Settlement · `LOCAL-202611148A011BE83FCC-G0003` · Perth Scorchers Women v Adelaide Strikers Women · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `4c696554870ffd247a827ff04a816d329b3d6c96c5c9f3614ddf667a8817fe21`, 3353 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/202611148A011BE83FCC.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `PRE_SCHEDULED_START_WRITE` (last recorded `2026-11-14T18:59:00+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| NOT_PREF | Adelaide 6 overs Over 41.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **UNRESOLVED** | phase score NOT_VERIFIED |  |
| R2 | Adelaide 6 overs Under 41.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **UNRESOLVED** | phase score NOT_VERIFIED |  |
| R1 | Adelaide innings Over 150.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | innings runs 202 vs 150.5: +51.5 |  |
| NOT_PREF | Adelaide innings Under 150.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | innings runs 202 vs 150.5: +51.5 |  |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_TOTAL Adelaide innings Over 150.5 (NOT_ESTIMATED) WIN; RANK1 Adelaide innings Over 150.5 (NOT_ESTIMATED) WIN. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** Adelaide Strikers 4-202 (20 ov, batted first) beat Perth Scorchers 9-150 by 52 runs; Adelaide 3-106 after 14 overs; 96 off the last six; six-over score NOT_VERIFIED. Identity matched on participants, date and competition (WBBL|12 Match 22, WACA Ground, Perth).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Cricket rows: innings totals at completion (all out counts as completion); phase rows need the score at the stated completed over.
**R4. Rank diagnostics.** 1W/1L/2U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final Adelaide innings runs = 202; total 202. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** Adelaide batted first and made a franchise-record 4-202: 3-106 after 14 overs, then 96 off the last six (a WBBL-record 40-run Power Surge). 202 beat 150.5 by 51.5.
**R9. Source/timing review.** Settlement sources: https://aapnews.aap.com.au/news/heat-hammer-hurricanes-in-wbbl-scorchers-finally-lose (ALLOWED); https://www.crictracker.com/cricket-news/mushangwes-5-11-ends-perth-scorchers-unbeaten-run-as-strikers-post-record-total-9270/ (ALLOWED); https://www.cricket.com.au/news/4609036/perth-scorchers-adelaide-strikers-wbbl12-match-report-highlights-waca-wolvaardt-mushangwe-de-broughe-penna-devine-mooney-king (ALLOWED). Card timing `PRE_SCHEDULED_START_WRITE`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-202611148A011BE83FCC-G0003 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-202611148C6C0822-G0003 revision-1 -->
### Settlement · `LOCAL-202611148C6C0822-G0003` · Perth Scorchers Women v Adelaide Strikers Women · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `1e6d7da3710be3cbe3401bfd8c241d21cc1b7757fdb225f151ec78be7db79c0a`, 4295 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/202611148C6C0822.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `WRITE_TIME_NOT_RECORDED` (last recorded `NOT_RECORDED`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| NOT_PREF | Adelaide 6 overs Over 41.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **UNRESOLVED** | phase score NOT_VERIFIED |  |
| R2 | Adelaide 6 overs Under 41.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **UNRESOLVED** | phase score NOT_VERIFIED |  |
| R1 | Adelaide innings Over 150.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | innings runs 202 vs 150.5: +51.5 |  |
| NOT_PREF | Adelaide innings Under 150.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | innings runs 202 vs 150.5: +51.5 |  |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_TOTAL Adelaide innings Over 150.5 (NOT_ESTIMATED) WIN; RANK1 Adelaide innings Over 150.5 (NOT_ESTIMATED) WIN. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** Adelaide Strikers 4-202 (20 ov, batted first) beat Perth Scorchers 9-150 by 52 runs; Adelaide 3-106 after 14 overs; 96 off the last six; six-over score NOT_VERIFIED. Identity matched on participants, date and competition (WBBL|12 Match 22, WACA Ground, Perth).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Cricket rows: innings totals at completion (all out counts as completion); phase rows need the score at the stated completed over.
**R4. Rank diagnostics.** 1W/1L/2U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final Adelaide innings runs = 202; total 202. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** Adelaide batted first and made a franchise-record 4-202: 3-106 after 14 overs, then 96 off the last six (a WBBL-record 40-run Power Surge). 202 beat 150.5 by 51.5.
**R9. Source/timing review.** Settlement sources: https://aapnews.aap.com.au/news/heat-hammer-hurricanes-in-wbbl-scorchers-finally-lose (ALLOWED); https://www.crictracker.com/cricket-news/mushangwes-5-11-ends-perth-scorchers-unbeaten-run-as-strikers-post-record-total-9270/ (ALLOWED); https://www.cricket.com.au/news/4609036/perth-scorchers-adelaide-strikers-wbbl12-match-report-highlights-waca-wolvaardt-mushangwe-de-broughe-penna-devine-mooney-king (ALLOWED). Card timing `WRITE_TIME_NOT_RECORDED`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-202611148C6C0822-G0003 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-20261114CHAT2988664A-G0003 revision-1 -->
### Settlement · `LOCAL-20261114CHAT2988664A-G0003` · Perth Scorchers Women v Adelaide Strikers Women · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `efb721655816176dffbe763f9befe131c55aff947c1a06ba66d08178fd7b0a01`, 4374 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/20261114CHAT2988664A.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `WRITE_TIME_NOT_RECORDED` (last recorded `NOT_RECORDED`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| R2 | Adelaide 6 overs Over 41.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **UNRESOLVED** | phase score NOT_VERIFIED |  |
| NOT_PREF | Adelaide 6 overs Under 41.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **UNRESOLVED** | phase score NOT_VERIFIED |  |
| R1 | Adelaide innings Over 150.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | innings runs 202 vs 150.5: +51.5 |  |
| NOT_PREF | Adelaide innings Under 150.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | innings runs 202 vs 150.5: +51.5 |  |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_TOTAL Adelaide innings Over 150.5 (NOT_ESTIMATED) WIN; RANK1 Adelaide innings Over 150.5 (NOT_ESTIMATED) WIN. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** Adelaide Strikers 4-202 (20 ov, batted first) beat Perth Scorchers 9-150 by 52 runs; Adelaide 3-106 after 14 overs; 96 off the last six; six-over score NOT_VERIFIED. Identity matched on participants, date and competition (WBBL|12 Match 22, WACA Ground, Perth).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Cricket rows: innings totals at completion (all out counts as completion); phase rows need the score at the stated completed over.
**R4. Rank diagnostics.** 1W/1L/2U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final Adelaide innings runs = 202; total 202. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** Adelaide batted first and made a franchise-record 4-202: 3-106 after 14 overs, then 96 off the last six (a WBBL-record 40-run Power Surge). 202 beat 150.5 by 51.5.
**R9. Source/timing review.** Settlement sources: https://aapnews.aap.com.au/news/heat-hammer-hurricanes-in-wbbl-scorchers-finally-lose (ALLOWED); https://www.crictracker.com/cricket-news/mushangwes-5-11-ends-perth-scorchers-unbeaten-run-as-strikers-post-record-total-9270/ (ALLOWED); https://www.cricket.com.au/news/4609036/perth-scorchers-adelaide-strikers-wbbl12-match-report-highlights-waca-wolvaardt-mushangwe-de-broughe-penna-devine-mooney-king (ALLOWED). Card timing `WRITE_TIME_NOT_RECORDED`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-20261114CHAT2988664A-G0003 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-20261114EA6B2758F0-G0002 revision-1 -->
### Settlement · `LOCAL-20261114EA6B2758F0-G0002` · Perth Scorchers Women v Adelaide Strikers Women · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `78372b4f3f6bd287c819d79414302bacf19b76745de90faa27d6f3b9fcb600dc`, 3022 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/20261114EA6B2758F0.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `PRE_SCHEDULED_START_WRITE` (last recorded `2026-11-14T19:00:30+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| R1 | Adelaide 6 overs Under 41.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **UNRESOLVED** | phase score NOT_VERIFIED |  |
| NOT_PREF | Adelaide 6 overs Over 41.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **UNRESOLVED** | phase score NOT_VERIFIED |  |
| R2 | Adelaide innings Under 150.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | innings runs 202 vs 150.5: +51.5 |  |
| NOT_PREF | Adelaide innings Over 150.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | innings runs 202 vs 150.5: +51.5 |  |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_TOTAL Adelaide innings Under 150.5 (NOT_ESTIMATED) LOSS; RANK1 Adelaide 6 overs Under 41.5 (NOT_ESTIMATED) UNRESOLVED. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** Adelaide Strikers 4-202 (20 ov, batted first) beat Perth Scorchers 9-150 by 52 runs; Adelaide 3-106 after 14 overs; 96 off the last six; six-over score NOT_VERIFIED. Identity matched on participants, date and competition (WBBL|12 Match 22, WACA Ground, Perth).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Cricket rows: innings totals at completion (all out counts as completion); phase rows need the score at the stated completed over.
**R4. Rank diagnostics.** 1W/1L/2U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final Adelaide innings runs = 202; total 202. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** Adelaide batted first and made a franchise-record 4-202: 3-106 after 14 overs, then 96 off the last six (a WBBL-record 40-run Power Surge). 202 beat 150.5 by 51.5.
**R9. Source/timing review.** Settlement sources: https://aapnews.aap.com.au/news/heat-hammer-hurricanes-in-wbbl-scorchers-finally-lose (ALLOWED); https://www.crictracker.com/cricket-news/mushangwes-5-11-ends-perth-scorchers-unbeaten-run-as-strikers-post-record-total-9270/ (ALLOWED); https://www.cricket.com.au/news/4609036/perth-scorchers-adelaide-strikers-wbbl12-match-report-highlights-waca-wolvaardt-mushangwe-de-broughe-penna-devine-mooney-king (ALLOWED). Card timing `PRE_SCHEDULED_START_WRITE`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-20261114EA6B2758F0-G0002 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-CHAT20261114DDA525E495-G0003 revision-1 -->
### Settlement · `LOCAL-CHAT20261114DDA525E495-G0003` · Perth Scorchers Women v Adelaide Strikers Women · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `c4b98bd1cf6f534e5baea18cf3759462065d7d761b749839dbf42e074d65edd9`, 18804 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/CHAT20261114DDA525E495.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `PRE_SCHEDULED_START_WRITE` (last recorded `2026-11-14T19:07:36+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| R1 | Adelaide 6 overs Over 41.5 | 0.648317 (chat-local uncalibrated scenario) | **UNRESOLVED** | phase score NOT_VERIFIED |  |
| R2 | Adelaide innings Over 150.5 | 0.5133 (chat-local uncalibrated scenario) | **WIN** | innings runs 202 vs 150.5: +51.5 | 0.236877 |
| NOT_RANKED | Adelaide innings Under 150.5 | 0.4867 (chat-local uncalibrated scenario) | **LOSS** | innings runs 202 vs 150.5: +51.5 | 0.236877 |
| NOT_RANKED | Adelaide 6 overs Under 41.5 | 0.351683 (chat-local uncalibrated scenario) | **UNRESOLVED** | phase score NOT_VERIFIED |  |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_TOTAL Adelaide innings Over 150.5 (0.5133) WIN; RANK1 Adelaide 6 overs Over 41.5 (0.648317) UNRESOLVED. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** Adelaide Strikers 4-202 (20 ov, batted first) beat Perth Scorchers 9-150 by 52 runs; Adelaide 3-106 after 14 overs; 96 off the last six; six-over score NOT_VERIFIED. Identity matched on participants, date and competition (WBBL|12 Match 22, WACA Ground, Perth).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Cricket rows: innings totals at completion (all out counts as completion); phase rows need the score at the stated completed over.
**R4. Rank diagnostics.** 1W/1L/2U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final Adelaide innings runs = 202; total 202. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** Adelaide batted first and made a franchise-record 4-202: 3-106 after 14 overs, then 96 off the last six (a WBBL-record 40-run Power Surge). 202 beat 150.5 by 51.5.
**R9. Source/timing review.** Settlement sources: https://aapnews.aap.com.au/news/heat-hammer-hurricanes-in-wbbl-scorchers-finally-lose (ALLOWED); https://www.crictracker.com/cricket-news/mushangwes-5-11-ends-perth-scorchers-unbeaten-run-as-strikers-post-record-total-9270/ (ALLOWED); https://www.cricket.com.au/news/4609036/perth-scorchers-adelaide-strikers-wbbl12-match-report-highlights-waca-wolvaardt-mushangwe-de-broughe-penna-devine-mooney-king (ALLOWED). Card timing `PRE_SCHEDULED_START_WRITE`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-CHAT20261114DDA525E495-G0003 revision-1 -->

### Deep loss reviews (DEEPLOSS-v1)

#### Deep loss review · Perth Scorchers Women v Adelaide Strikers Women · Adelaide innings Under 150.5

**1. Exact frozen claim.** `Adelaide innings Under 150.5`, full-game endpoint as each card defined it. Triggered in 1 card(s):

| Card | Trigger role(s) | Original p (basis) | Brier | Log loss |
|---|---|---|---:|---:|
| `LOCAL-20261114EA6B2758F0-G0002` | TOP_TOTAL | NOT_ESTIMATED (qualitative (no numeric p)) |  |  |

No card carried a primary p_card, frozen reference or same-row baseline; BASELINE_P comparison NOT_COMPUTABLE.

**2. Verified outcome.** Adelaide Strikers 4-202 (20 ov, batted first) beat Perth Scorchers 9-150 by 52 runs (Adelaide 3-106 after 14 overs; 96 off the last six; six-over score NOT_VERIFIED). innings runs 202 vs 150.5: +51.5. Sources in R9; evidence B; final wall-clock NOT_VERIFIED.
**3. Distribution check.** Every triggering card was qualitative, so there is no frozen distribution to place the result in.
**4. Error decomposition.** Realised distance: innings runs 202 vs 150.5: +51.5. No card had a calibrated centre or a measured effect row, so the miss is not split into reference and adjustment error; no blame shares are invented.
**5. Research audit.** EA6 leaned Under on Perth's bowling (opponents averaged about 141) but its own data showed Adelaide at 185, 170, 152 and 139 (three of four over 150.5, the 139 a chase). It did not separate batting first from chasing.
**6. What decided the game.** Adelaide batted first and made a franchise-record 4-202: 3-106 after 14 overs, then 96 off the last six (a WBBL-record 40-run Power Surge). 202 beat 150.5 by 51.5.
**7. Knowable at cutoff?** Knowable: Adelaide's recent ceiling and that this was a batting-first innings. Not knowable: a record 40-run Power Surge and 96 off the last six.
**8. Process audit.** Chat-local record; no repository reference stage, no source-audit receipts, no lineup confirmation, no freeze. Timing per card in CARD_TIMING.csv.
**9. Verdict.** ERROR (lean against the card's own scoring evidence). Low conviction was stated, but the lean should have been no pick; the other five cards leaned Over and were right.
**10. Cutoff-only counterfactual.** NOT_ESTIMATED: no knowable fact has a measured effect-table row, so no corrected probability is priced after the result.
**11. Failure class and recurrence.** Single card.
**12. Correction.** NO_CHANGE to any rule from one result. Pattern-level proposals are in AUDIT_REPORT (PROPOSED_NOT_TESTED).
**13. Matched wins.** None among the triggering cards.
**14. Honesty.** Original numbers and labels preserved; no luck claim without the arithmetic above; no invented percentages, operator terms or publication times.

<!-- END SETTLEMENT EVENT E03 revision-1 -->

<!-- BEGIN SETTLEMENT EVENT E04 revision-1 -->
## Event · Jonas Forejtek v Marvin Moeller · 2026-11-14 · ATP Challenger 50 Monastir 1, semifinal (Centre Court)

**Final:** Moeller d. Forejtek 7-6(1) 6-1 (96 min). **Periods:** Sets 7-6(1), 6-1; games Moeller 13, Forejtek 7; total 20. **Evidence B.** Scheduled 2026-11-14T10:00:00+00:00. Note: Scheduled start conflicts across feeds (10:00Z / 11:00Z; one feed showed 'Postponed Suspended'); the 10:00Z listing is used for ordering.

| Opened source | Audit | Field read |
|---|---|---|
| https://www.atptour.com/en/scores/current-challenger/monastir/3159/results | ALLOWED | 'Sat, 14 November, 2026 Day (7)', 'Semifinals - Centre Court': 'Marvin Moeller wins the match 7-6(1) 6-1' |
| https://www.tennisnet.com/news/atp-challenger-monastir-marvin-moeller-bucht-mit-finaleinzug-aussie-ticket | ALLOWED | '7:6 (1), 6:1-Erfolg nach 96 Minuten'; stamped Samstag 14.11.2026, 14:57 |

<!-- BEGIN SETTLEMENT LOCAL-20261114B4496A3F-G0005 revision-1 -->
### Settlement · `LOCAL-20261114B4496A3F-G0005` · Jonas Forejtek v Marvin Moeller · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `7b75116d5cddd47579b6008c1d7223bc784d1f29781c16569025ec37b9e5c1ef`, 29384 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/20261114B4496A3F.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `POST_SCHEDULED_START_WRITE` (last recorded `2026-11-14T22:20:39+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| R1 | Moeller +3.5 games | 0.7582 (chat-local uncalibrated scenario) | **WIN** | side margin +6, handicap +3.5: +9.5 | 0.058467 |
| R2 | Over 22.5 games | 0.6050 (chat-local uncalibrated scenario) | **LOSS** | games 20 vs 22.5: -2.5 | 0.366025 |
| INFO | Forejtek -3.5 games | 0.2418 (chat-local uncalibrated scenario) | **LOSS** | side margin -6, handicap -3.5: -9.5 | 0.058467 |
| INFO | Under 22.5 games | 0.3950 (chat-local uncalibrated scenario) | **WIN** | games 20 vs 22.5: -2.5 | 0.366025 |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_SIDE Moeller +3.5 games (0.7582) WIN; TOP_TOTAL Over 22.5 games (0.6050) LOSS; RANK1 Moeller +3.5 games (0.7582) WIN. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** Moeller d. Forejtek 7-6(1) 6-1 (96 min); Sets 7-6(1), 6-1; games Moeller 13, Forejtek 7; total 20. Identity matched on participants, date and competition (ATP Challenger 50 Monastir 1, semifinal (Centre Court)).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Tennis rows count every game of the completed match; no retirement.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final Forejtek games minus Moeller games = -6; total 20. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** Moeller won a first-set tiebreak 7-1 and the second set 6-1. Twenty games is 2.5 under 22.5; Moeller's +6 game margin covered both +3.5 and +4.5.
**R9. Source/timing review.** Settlement sources: https://www.atptour.com/en/scores/current-challenger/monastir/3159/results (ALLOWED); https://www.tennisnet.com/news/atp-challenger-monastir-marvin-moeller-bucht-mit-finaleinzug-aussie-ticket (ALLOWED). Card timing `POST_SCHEDULED_START_WRITE`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-20261114B4496A3F-G0005 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-202611148A011BE83FCC-G0005 revision-1 -->
### Settlement · `LOCAL-202611148A011BE83FCC-G0005` · Jonas Forejtek v Marvin Moeller · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `a67f9317006cc2247cba94e4dc76070e786a745dd65fd039b3413dfbfeadd3f1`, 8020 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/202611148A011BE83FCC.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `POST_SCHEDULED_START_WRITE` (last recorded `2026-11-14T22:09:55+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| NOT_PREF | Forejtek -3.5 games | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | side margin -6, handicap -3.5: -9.5 |  |
| R2 | Moeller +4.5 games | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | side margin +6, handicap +4.5: +10.5 |  |
| R1 | Over 22.5 games | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | games 20 vs 22.5: -2.5 |  |
| NOT_PREF | Under 22.5 games | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | games 20 vs 22.5: -2.5 |  |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_SIDE Moeller +4.5 games (NOT_ESTIMATED) WIN; TOP_TOTAL Over 22.5 games (NOT_ESTIMATED) LOSS; RANK1 Over 22.5 games (NOT_ESTIMATED) LOSS. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** Moeller d. Forejtek 7-6(1) 6-1 (96 min); Sets 7-6(1), 6-1; games Moeller 13, Forejtek 7; total 20. Identity matched on participants, date and competition (ATP Challenger 50 Monastir 1, semifinal (Centre Court)).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Tennis rows count every game of the completed match; no retirement.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final Forejtek games minus Moeller games = -6; total 20. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** Moeller won a first-set tiebreak 7-1 and the second set 6-1. Twenty games is 2.5 under 22.5; Moeller's +6 game margin covered both +3.5 and +4.5.
**R9. Source/timing review.** Settlement sources: https://www.atptour.com/en/scores/current-challenger/monastir/3159/results (ALLOWED); https://www.tennisnet.com/news/atp-challenger-monastir-marvin-moeller-bucht-mit-finaleinzug-aussie-ticket (ALLOWED). Card timing `POST_SCHEDULED_START_WRITE`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-202611148A011BE83FCC-G0005 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-202611148C6C0822-G0005 revision-1 -->
### Settlement · `LOCAL-202611148C6C0822-G0005` · Jonas Forejtek v Marvin Moeller · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `cbcf5fadc92388a5518216be9e9473b6a86fabba87485ddc4018e33275b8a57e`, 7824 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/202611148C6C0822.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `POST_SCHEDULED_START_WRITE` (last recorded `2026-11-14T22:11:49+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| NOT_PREF | Forejtek -3.5 games | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | side margin -6, handicap -3.5: -9.5 |  |
| R1 | Moeller +4.5 games | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | side margin +6, handicap +4.5: +10.5 |  |
| R2 | Over 22.5 games | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | games 20 vs 22.5: -2.5 |  |
| NOT_PREF | Under 22.5 games | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | games 20 vs 22.5: -2.5 |  |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_SIDE Moeller +4.5 games (NOT_ESTIMATED) WIN; TOP_TOTAL Over 22.5 games (NOT_ESTIMATED) LOSS; RANK1 Moeller +4.5 games (NOT_ESTIMATED) WIN. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** Moeller d. Forejtek 7-6(1) 6-1 (96 min); Sets 7-6(1), 6-1; games Moeller 13, Forejtek 7; total 20. Identity matched on participants, date and competition (ATP Challenger 50 Monastir 1, semifinal (Centre Court)).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Tennis rows count every game of the completed match; no retirement.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final Forejtek games minus Moeller games = -6; total 20. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** Moeller won a first-set tiebreak 7-1 and the second set 6-1. Twenty games is 2.5 under 22.5; Moeller's +6 game margin covered both +3.5 and +4.5.
**R9. Source/timing review.** Settlement sources: https://www.atptour.com/en/scores/current-challenger/monastir/3159/results (ALLOWED); https://www.tennisnet.com/news/atp-challenger-monastir-marvin-moeller-bucht-mit-finaleinzug-aussie-ticket (ALLOWED). Card timing `POST_SCHEDULED_START_WRITE`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-202611148C6C0822-G0005 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-20261114CHAT2988664A-G0005 revision-1 -->
### Settlement · `LOCAL-20261114CHAT2988664A-G0005` · Jonas Forejtek v Marvin Moeller · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `9f880c43e63675117492294f6c2b3f213c7f2fa3f6135c7d9537be5fff0e1b6e`, 8680 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/20261114CHAT2988664A.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `POST_SCHEDULED_START_WRITE` (last recorded `2026-11-14T22:05:50+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| NOT_PREF | Forejtek -3.5 games | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | side margin -6, handicap -3.5: -9.5 |  |
| R1 | Moeller +4.5 games | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | side margin +6, handicap +4.5: +10.5 |  |
| R2 | Over 22.5 games | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | games 20 vs 22.5: -2.5 |  |
| NOT_PREF | Under 22.5 games | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | games 20 vs 22.5: -2.5 |  |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_SIDE Moeller +4.5 games (NOT_ESTIMATED) WIN; TOP_TOTAL Over 22.5 games (NOT_ESTIMATED) LOSS; RANK1 Moeller +4.5 games (NOT_ESTIMATED) WIN. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** Moeller d. Forejtek 7-6(1) 6-1 (96 min); Sets 7-6(1), 6-1; games Moeller 13, Forejtek 7; total 20. Identity matched on participants, date and competition (ATP Challenger 50 Monastir 1, semifinal (Centre Court)).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Tennis rows count every game of the completed match; no retirement.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final Forejtek games minus Moeller games = -6; total 20. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** Moeller won a first-set tiebreak 7-1 and the second set 6-1. Twenty games is 2.5 under 22.5; Moeller's +6 game margin covered both +3.5 and +4.5.
**R9. Source/timing review.** Settlement sources: https://www.atptour.com/en/scores/current-challenger/monastir/3159/results (ALLOWED); https://www.tennisnet.com/news/atp-challenger-monastir-marvin-moeller-bucht-mit-finaleinzug-aussie-ticket (ALLOWED). Card timing `POST_SCHEDULED_START_WRITE`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-20261114CHAT2988664A-G0005 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-20261114EA6B2758F0-G0004 revision-1 -->
### Settlement · `LOCAL-20261114EA6B2758F0-G0004` · Jonas Forejtek v Marvin Moeller · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `78e97d7b68eead56c1501499574b6a28c4c4f958c346af4722f34eb283bd519d`, 9965 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/20261114EA6B2758F0.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `POST_SCHEDULED_START_WRITE` (last recorded `2026-11-14T22:10:59+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| NOT_PREF | Forejtek -3.5 games | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | side margin -6, handicap -3.5: -9.5 |  |
| R1 | Moeller +4.5 games | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | side margin +6, handicap +4.5: +10.5 |  |
| R2 | Over 22.5 games | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | games 20 vs 22.5: -2.5 |  |
| NOT_PREF | Under 22.5 games | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | games 20 vs 22.5: -2.5 |  |
| LEAN_WINNER | Forejtek to win | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | side margin -6 |  |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_SIDE Moeller +4.5 games (NOT_ESTIMATED) WIN; TOP_TOTAL Over 22.5 games (NOT_ESTIMATED) LOSS; RANK1 Moeller +4.5 games (NOT_ESTIMATED) WIN. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** Moeller d. Forejtek 7-6(1) 6-1 (96 min); Sets 7-6(1), 6-1; games Moeller 13, Forejtek 7; total 20. Identity matched on participants, date and competition (ATP Challenger 50 Monastir 1, semifinal (Centre Court)).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Tennis rows count every game of the completed match; no retirement.
**R4. Rank diagnostics.** 2W/3L/0U over 5 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final Forejtek games minus Moeller games = -6; total 20. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** Moeller won a first-set tiebreak 7-1 and the second set 6-1. Twenty games is 2.5 under 22.5; Moeller's +6 game margin covered both +3.5 and +4.5.
**R9. Source/timing review.** Settlement sources: https://www.atptour.com/en/scores/current-challenger/monastir/3159/results (ALLOWED); https://www.tennisnet.com/news/atp-challenger-monastir-marvin-moeller-bucht-mit-finaleinzug-aussie-ticket (ALLOWED). Card timing `POST_SCHEDULED_START_WRITE`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-20261114EA6B2758F0-G0004 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-CHAT20261114DDA525E495-G0005 revision-1 -->
### Settlement · `LOCAL-CHAT20261114DDA525E495-G0005` · Jonas Forejtek v Marvin Moeller · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `83252d2f128c1a74758c75b0110cf2e5a88a607ae6731efdbfd927969839bf35`, 17608 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/CHAT20261114DDA525E495.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `POST_SCHEDULED_START_WRITE` (last recorded `2026-11-14T22:15:14+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| R1 | Moeller +3.5 games | 0.7833 (chat-local uncalibrated scenario) | **WIN** | side margin +6, handicap +3.5: +9.5 | 0.046959 |
| R2 | Over 22.5 games | 0.5943 (chat-local uncalibrated scenario) | **LOSS** | games 20 vs 22.5: -2.5 | 0.353192 |
| NOT_RANKED | Forejtek -3.5 games | 0.2167 (chat-local uncalibrated scenario) | **LOSS** | side margin -6, handicap -3.5: -9.5 | 0.046959 |
| NOT_RANKED | Under 22.5 games | 0.4057 (chat-local uncalibrated scenario) | **WIN** | games 20 vs 22.5: -2.5 | 0.353192 |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_SIDE Moeller +3.5 games (0.7833) WIN; TOP_TOTAL Over 22.5 games (0.5943) LOSS; RANK1 Moeller +3.5 games (0.7833) WIN. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** Moeller d. Forejtek 7-6(1) 6-1 (96 min); Sets 7-6(1), 6-1; games Moeller 13, Forejtek 7; total 20. Identity matched on participants, date and competition (ATP Challenger 50 Monastir 1, semifinal (Centre Court)).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Tennis rows count every game of the completed match; no retirement.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final Forejtek games minus Moeller games = -6; total 20. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** Moeller won a first-set tiebreak 7-1 and the second set 6-1. Twenty games is 2.5 under 22.5; Moeller's +6 game margin covered both +3.5 and +4.5.
**R9. Source/timing review.** Settlement sources: https://www.atptour.com/en/scores/current-challenger/monastir/3159/results (ALLOWED); https://www.tennisnet.com/news/atp-challenger-monastir-marvin-moeller-bucht-mit-finaleinzug-aussie-ticket (ALLOWED). Card timing `POST_SCHEDULED_START_WRITE`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-CHAT20261114DDA525E495-G0005 revision-1 -->

### Deep loss reviews (DEEPLOSS-v1)

#### Deep loss review · Jonas Forejtek v Marvin Moeller · Over 22.5 games

**1. Exact frozen claim.** `Over 22.5 games`, full-game endpoint as each card defined it. Triggered in 6 card(s):

| Card | Trigger role(s) | Original p (basis) | Brier | Log loss |
|---|---|---|---:|---:|
| `LOCAL-202611148A011BE83FCC-G0005` | TOP_TOTAL, RANK1 | NOT_ESTIMATED (qualitative (no numeric p)) |  |  |
| `LOCAL-202611148C6C0822-G0005` | TOP_TOTAL | NOT_ESTIMATED (qualitative (no numeric p)) |  |  |
| `LOCAL-20261114B4496A3F-G0005` | TOP_TOTAL | 0.6050 (chat-local uncalibrated scenario) | 0.366025 | 0.928870 |
| `LOCAL-20261114CHAT2988664A-G0005` | TOP_TOTAL | NOT_ESTIMATED (qualitative (no numeric p)) |  |  |
| `LOCAL-20261114EA6B2758F0-G0004` | TOP_TOTAL | NOT_ESTIMATED (qualitative (no numeric p)) |  |  |
| `LOCAL-CHAT20261114DDA525E495-G0005` | TOP_TOTAL | 0.5943 (chat-local uncalibrated scenario) | 0.353192 | 0.902141 |

No card carried a primary p_card, frozen reference or same-row baseline; BASELINE_P comparison NOT_COMPUTABLE.

**2. Verified outcome.** Moeller d. Forejtek 7-6(1) 6-1 (96 min) (Sets 7-6(1), 6-1; games Moeller 13, Forejtek 7; total 20). games 20 vs 22.5: -2.5. Sources in R9; evidence B; final wall-clock NOT_VERIFIED.
**3. Distribution check.** Numeric cards priced this row at 0.594-0.605; a loss at those prices is a 40%-41% event under each card's own uncalibrated object.
**4. Error decomposition.** Realised distance: games 20 vs 22.5: -2.5. No card had a calibrated centre or a measured effect row, so the miss is not split into reference and adjustment error; no blame shares are invented.
**5. Research audit.** All six cards leaned on five of six Monastir matches clearing 22.5 and Moeller's three three-set wins; these are selection-biased tournament samples. B44's tree gave a mean of 25.4 games and P(Over) 0.605; DDA 0.594; deciding-set probability about 0.50.
**6. What decided the game.** Moeller won a first-set tiebreak 7-1 and the second set 6-1. Twenty games is 2.5 under 22.5; Moeller's +6 game margin covered both +3.5 and +4.5.
**7. Knowable at cutoff?** Knowable: Moeller's higher rank (229 v 303) and Elo edge, which the same cards used for Moeller +3.5/+4.5 (those rows won). Not knowable: a 7-1 first-set tiebreak and a 6-1 second set.
**8. Process audit.** Chat-local record; no repository reference stage, no source-audit receipts, no lineup confirmation, no freeze. Timing per card in CARD_TIMING.csv.
**9. Verdict.** VARIANCE with MODEL_LIMIT. The cards' read that Moeller was the stronger player was right; his dominance is what produced a short match. A 40% event under the cards' own numbers, but the total lean added little beyond the handicap and the two are correlated.
**10. Cutoff-only counterfactual.** NOT_ESTIMATED: no knowable fact has a measured effect-table row, so no corrected probability is priced after the result.
**11. Failure class and recurrence.** Shared across 6 cards on one game: overlapping public inputs make these one dependent observation, not 6.
**12. Correction.** NO_CHANGE to any rule from one result. Pattern-level proposals are in AUDIT_REPORT (PROPOSED_NOT_TESTED).
**13. Matched wins.** `LOCAL-202611148A011BE83FCC-G0005` TOP_SIDE Moeller +4.5 games WIN; `LOCAL-202611148C6C0822-G0005` RANK1 Moeller +4.5 games WIN; `LOCAL-202611148C6C0822-G0005` TOP_SIDE Moeller +4.5 games WIN; `LOCAL-20261114B4496A3F-G0005` RANK1 Moeller +3.5 games WIN; `LOCAL-20261114B4496A3F-G0005` TOP_SIDE Moeller +3.5 games WIN; `LOCAL-20261114CHAT2988664A-G0005` RANK1 Moeller +4.5 games WIN; `LOCAL-20261114CHAT2988664A-G0005` TOP_SIDE Moeller +4.5 games WIN; `LOCAL-20261114EA6B2758F0-G0004` RANK1 Moeller +4.5 games WIN; `LOCAL-20261114EA6B2758F0-G0004` TOP_SIDE Moeller +4.5 games WIN; `LOCAL-CHAT20261114DDA525E495-G0005` RANK1 Moeller +3.5 games WIN; `LOCAL-CHAT20261114DDA525E495-G0005` TOP_SIDE Moeller +3.5 games WIN. These rest on the same unvalidated construction and do not show the process worked.
**14. Honesty.** Original numbers and labels preserved; no luck claim without the arithmetic above; no invented percentages, operator terms or publication times.

<!-- END SETTLEMENT EVENT E04 revision-1 -->

<!-- BEGIN SETTLEMENT EVENT E05 revision-1 -->
## Event · Tappara U20 v HPK U20 · 2026-11-14 · Finland U20 SM-sarja 2026-27

**Final:** NOT_VERIFIED (played as scheduled per fixture listings; no permitted page read showed the final). **Periods:** NOT_VERIFIED. **Evidence NONE.** Scheduled 2026-11-14T11:00:00+00:00. Note: Elite Prospects returned HTTP 403; Sofascore RULES_UNKNOWN; Leijonat and Ilkka-Pohjalainen BLOCKED_FOR_AI. Queued in UNRESOLVED_POST_IMPORT.

| Opened source | Audit | Field read |
|---|---|---|
| https://hpk.fi/joukkue/hpk-u20/otteluohjelma-u20/ | ALLOWED | Fixture 'LA 14.11. 13:00 Tappara-HPK'; no score shown |
| https://www.tappara.fi/fi-fi/article/a-nuoret/u20-ottelut/12/?filter_view=1&results=1 | NO_RULES_FILE | Results list script-loaded; no match rows |
| https://www.flashscore.co.uk/match/ice-hockey/hpk-8nboRSAG/tappara-4pQ2VSJs/ | ALLOWED | 'Loading...' placeholder; no match data |

<!-- BEGIN SETTLEMENT LOCAL-20261114B4496A3F-G0004 revision-1 -->
### Settlement · `LOCAL-20261114B4496A3F-G0004` · Tappara U20 v HPK U20 · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `d9c60ffd6e938597eb6d6fc5ad51e0093e4762bb963e32e8e496b5e86f2817c7`, 28357 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/20261114B4496A3F.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `PRE_SCHEDULED_START_WRITE` (last recorded `2026-11-14T21:51:56+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| UNRANKED_GOALIE_GATE | Over 5.5 goals | 0.6163 (chat-local uncalibrated scenario) | **UNRESOLVED** | final NOT_VERIFIED |  |
| R1 | HPK ML | 0.5538 (chat-local uncalibrated scenario) | **UNRESOLVED** | final NOT_VERIFIED |  |
| INFO | Tappara ML | 0.4462 (chat-local uncalibrated scenario) | **UNRESOLVED** | final NOT_VERIFIED |  |
| INFO | Under 5.5 goals | 0.3837 (chat-local uncalibrated scenario) | **UNRESOLVED** | final NOT_VERIFIED |  |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_SIDE HPK ML (0.5538) UNRESOLVED; RANK1 HPK ML (0.5538) UNRESOLVED. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** NOT_VERIFIED (played as scheduled per fixture listings; no permitted page read showed the final); NOT_VERIFIED. Identity matched on participants, date and competition (Finland U20 SM-sarja 2026-27).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Hockey rows: every grade is the same under 60-minute, full-game and shootout-credited conventions, except where marked.
**R4. Rank diagnostics.** 0W/0L/4U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final Tappara minus HPK = NOT_VERIFIED; total NOT_VERIFIED. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** Result not established from any permitted source; every row is UNRESOLVED.
**R9. Source/timing review.** Settlement sources: https://hpk.fi/joukkue/hpk-u20/otteluohjelma-u20/ (ALLOWED); https://www.tappara.fi/fi-fi/article/a-nuoret/u20-ottelut/12/?filter_view=1&results=1 (NO_RULES_FILE); https://www.flashscore.co.uk/match/ice-hockey/hpk-8nboRSAG/tappara-4pQ2VSJs/ (ALLOWED). Card timing `PRE_SCHEDULED_START_WRITE`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-20261114B4496A3F-G0004 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-202611148A011BE83FCC-G0004 revision-1 -->
### Settlement · `LOCAL-202611148A011BE83FCC-G0004` · Tappara U20 v HPK U20 · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `800783c103d0c779275401a1ab02456be4a7caddb8e787711e566bcbc469933c`, 3358 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/202611148A011BE83FCC.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `PRE_SCHEDULED_START_WRITE` (last recorded `2026-11-14T21:42:00+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| NOT_PREF | Tappara ML | NOT_ESTIMATED (qualitative (no numeric p)) | **UNRESOLVED** | final NOT_VERIFIED |  |
| R2 | HPK ML | NOT_ESTIMATED (qualitative (no numeric p)) | **UNRESOLVED** | final NOT_VERIFIED |  |
| R1 | Over 5.5 goals | NOT_ESTIMATED (qualitative (no numeric p)) | **UNRESOLVED** | final NOT_VERIFIED |  |
| NOT_PREF | Under 5.5 goals | NOT_ESTIMATED (qualitative (no numeric p)) | **UNRESOLVED** | final NOT_VERIFIED |  |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_SIDE HPK ML (NOT_ESTIMATED) UNRESOLVED; TOP_TOTAL Over 5.5 goals (NOT_ESTIMATED) UNRESOLVED; RANK1 Over 5.5 goals (NOT_ESTIMATED) UNRESOLVED. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** NOT_VERIFIED (played as scheduled per fixture listings; no permitted page read showed the final); NOT_VERIFIED. Identity matched on participants, date and competition (Finland U20 SM-sarja 2026-27).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Hockey rows: every grade is the same under 60-minute, full-game and shootout-credited conventions, except where marked.
**R4. Rank diagnostics.** 0W/0L/4U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final Tappara minus HPK = NOT_VERIFIED; total NOT_VERIFIED. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** Result not established from any permitted source; every row is UNRESOLVED.
**R9. Source/timing review.** Settlement sources: https://hpk.fi/joukkue/hpk-u20/otteluohjelma-u20/ (ALLOWED); https://www.tappara.fi/fi-fi/article/a-nuoret/u20-ottelut/12/?filter_view=1&results=1 (NO_RULES_FILE); https://www.flashscore.co.uk/match/ice-hockey/hpk-8nboRSAG/tappara-4pQ2VSJs/ (ALLOWED). Card timing `PRE_SCHEDULED_START_WRITE`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-202611148A011BE83FCC-G0004 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-202611148C6C0822-G0004 revision-1 -->
### Settlement · `LOCAL-202611148C6C0822-G0004` · Tappara U20 v HPK U20 · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `ed2837952b585a61c4d9174adf8a022ae07397d1f410f0b0ef0c1f840bfcec92`, 3654 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/202611148C6C0822.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `PRE_SCHEDULED_START_WRITE` (last recorded `2026-11-14T21:42:00+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| R2 | HPK ML | NOT_ESTIMATED (qualitative (no numeric p)) | **UNRESOLVED** | final NOT_VERIFIED |  |
| NOT_PREF | Tappara ML | NOT_ESTIMATED (qualitative (no numeric p)) | **UNRESOLVED** | final NOT_VERIFIED |  |
| R1 | Over 5.5 goals | NOT_ESTIMATED (qualitative (no numeric p)) | **UNRESOLVED** | final NOT_VERIFIED |  |
| NOT_PREF | Under 5.5 goals | NOT_ESTIMATED (qualitative (no numeric p)) | **UNRESOLVED** | final NOT_VERIFIED |  |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_SIDE HPK ML (NOT_ESTIMATED) UNRESOLVED; TOP_TOTAL Over 5.5 goals (NOT_ESTIMATED) UNRESOLVED; RANK1 Over 5.5 goals (NOT_ESTIMATED) UNRESOLVED. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** NOT_VERIFIED (played as scheduled per fixture listings; no permitted page read showed the final); NOT_VERIFIED. Identity matched on participants, date and competition (Finland U20 SM-sarja 2026-27).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Hockey rows: every grade is the same under 60-minute, full-game and shootout-credited conventions, except where marked.
**R4. Rank diagnostics.** 0W/0L/4U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final Tappara minus HPK = NOT_VERIFIED; total NOT_VERIFIED. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** Result not established from any permitted source; every row is UNRESOLVED.
**R9. Source/timing review.** Settlement sources: https://hpk.fi/joukkue/hpk-u20/otteluohjelma-u20/ (ALLOWED); https://www.tappara.fi/fi-fi/article/a-nuoret/u20-ottelut/12/?filter_view=1&results=1 (NO_RULES_FILE); https://www.flashscore.co.uk/match/ice-hockey/hpk-8nboRSAG/tappara-4pQ2VSJs/ (ALLOWED). Card timing `PRE_SCHEDULED_START_WRITE`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-202611148C6C0822-G0004 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-20261114CHAT2988664A-G0004 revision-1 -->
### Settlement · `LOCAL-20261114CHAT2988664A-G0004` · Tappara U20 v HPK U20 · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `c62a9b46ee74c9dd4e5911143bf2310d3099d7d428dbd594fb64b4128402770d`, 3612 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/20261114CHAT2988664A.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `WRITE_TIME_NOT_RECORDED` (last recorded `NOT_RECORDED`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| NOT_PREF | Tappara ML | NOT_ESTIMATED (qualitative (no numeric p)) | **UNRESOLVED** | final NOT_VERIFIED |  |
| R2 | HPK ML | NOT_ESTIMATED (qualitative (no numeric p)) | **UNRESOLVED** | final NOT_VERIFIED |  |
| R1 | Over 5.5 goals | NOT_ESTIMATED (qualitative (no numeric p)) | **UNRESOLVED** | final NOT_VERIFIED |  |
| NOT_PREF | Under 5.5 goals | NOT_ESTIMATED (qualitative (no numeric p)) | **UNRESOLVED** | final NOT_VERIFIED |  |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_SIDE HPK ML (NOT_ESTIMATED) UNRESOLVED; TOP_TOTAL Over 5.5 goals (NOT_ESTIMATED) UNRESOLVED; RANK1 Over 5.5 goals (NOT_ESTIMATED) UNRESOLVED. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** NOT_VERIFIED (played as scheduled per fixture listings; no permitted page read showed the final); NOT_VERIFIED. Identity matched on participants, date and competition (Finland U20 SM-sarja 2026-27).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Hockey rows: every grade is the same under 60-minute, full-game and shootout-credited conventions, except where marked.
**R4. Rank diagnostics.** 0W/0L/4U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final Tappara minus HPK = NOT_VERIFIED; total NOT_VERIFIED. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** Result not established from any permitted source; every row is UNRESOLVED.
**R9. Source/timing review.** Settlement sources: https://hpk.fi/joukkue/hpk-u20/otteluohjelma-u20/ (ALLOWED); https://www.tappara.fi/fi-fi/article/a-nuoret/u20-ottelut/12/?filter_view=1&results=1 (NO_RULES_FILE); https://www.flashscore.co.uk/match/ice-hockey/hpk-8nboRSAG/tappara-4pQ2VSJs/ (ALLOWED). Card timing `WRITE_TIME_NOT_RECORDED`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-20261114CHAT2988664A-G0004 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-20261114EA6B2758F0-G0003 revision-1 -->
### Settlement · `LOCAL-20261114EA6B2758F0-G0003` · Tappara U20 v HPK U20 · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `a3a1f674d6455ff43a151c059c405d5b70d870eb324a2bd3d4e7fb7e3957c1da`, 2917 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/20261114EA6B2758F0.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `PRE_SCHEDULED_START_WRITE` (last recorded `2026-11-14T21:42:00+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| R1 | HPK ML | NOT_ESTIMATED (qualitative (no numeric p)) | **UNRESOLVED** | final NOT_VERIFIED |  |
| NOT_PREF | Tappara ML | NOT_ESTIMATED (qualitative (no numeric p)) | **UNRESOLVED** | final NOT_VERIFIED |  |
| R2 | Over 5.5 goals | NOT_ESTIMATED (qualitative (no numeric p)) | **UNRESOLVED** | final NOT_VERIFIED |  |
| NOT_PREF | Under 5.5 goals | NOT_ESTIMATED (qualitative (no numeric p)) | **UNRESOLVED** | final NOT_VERIFIED |  |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_SIDE HPK ML (NOT_ESTIMATED) UNRESOLVED; TOP_TOTAL Over 5.5 goals (NOT_ESTIMATED) UNRESOLVED; RANK1 HPK ML (NOT_ESTIMATED) UNRESOLVED. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** NOT_VERIFIED (played as scheduled per fixture listings; no permitted page read showed the final); NOT_VERIFIED. Identity matched on participants, date and competition (Finland U20 SM-sarja 2026-27).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Hockey rows: every grade is the same under 60-minute, full-game and shootout-credited conventions, except where marked.
**R4. Rank diagnostics.** 0W/0L/4U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final Tappara minus HPK = NOT_VERIFIED; total NOT_VERIFIED. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** Result not established from any permitted source; every row is UNRESOLVED.
**R9. Source/timing review.** Settlement sources: https://hpk.fi/joukkue/hpk-u20/otteluohjelma-u20/ (ALLOWED); https://www.tappara.fi/fi-fi/article/a-nuoret/u20-ottelut/12/?filter_view=1&results=1 (NO_RULES_FILE); https://www.flashscore.co.uk/match/ice-hockey/hpk-8nboRSAG/tappara-4pQ2VSJs/ (ALLOWED). Card timing `PRE_SCHEDULED_START_WRITE`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-20261114EA6B2758F0-G0003 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-CHAT20261114DDA525E495-G0004 revision-1 -->
### Settlement · `LOCAL-CHAT20261114DDA525E495-G0004` · Tappara U20 v HPK U20 · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `51c041fd4231ced7065a7d999c4a9507c26671e6eb0c5933249ab8d876e24ad1`, 16076 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/CHAT20261114DDA525E495.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `PRE_SCHEDULED_START_WRITE` (last recorded `2026-11-14T21:50:13+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| D1 | Over 5.5 goals | 0.614186 (chat-local uncalibrated scenario) | **UNRESOLVED** | final NOT_VERIFIED |  |
| D2 | HPK ML | 0.5858 (chat-local uncalibrated scenario) | **UNRESOLVED** | final NOT_VERIFIED |  |
| NOT_RANKED | Tappara ML | 0.4142 (chat-local uncalibrated scenario) | **UNRESOLVED** | final NOT_VERIFIED |  |
| NOT_RANKED | Under 5.5 goals | 0.3858 (chat-local uncalibrated scenario) | **UNRESOLVED** | final NOT_VERIFIED |  |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_SIDE HPK ML (0.5858) UNRESOLVED; TOP_TOTAL Over 5.5 goals (0.614186) UNRESOLVED; RANK1 Over 5.5 goals (0.614186) UNRESOLVED. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** NOT_VERIFIED (played as scheduled per fixture listings; no permitted page read showed the final); NOT_VERIFIED. Identity matched on participants, date and competition (Finland U20 SM-sarja 2026-27).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Hockey rows: every grade is the same under 60-minute, full-game and shootout-credited conventions, except where marked.
**R4. Rank diagnostics.** 0W/0L/4U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final Tappara minus HPK = NOT_VERIFIED; total NOT_VERIFIED. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** Result not established from any permitted source; every row is UNRESOLVED.
**R9. Source/timing review.** Settlement sources: https://hpk.fi/joukkue/hpk-u20/otteluohjelma-u20/ (ALLOWED); https://www.tappara.fi/fi-fi/article/a-nuoret/u20-ottelut/12/?filter_view=1&results=1 (NO_RULES_FILE); https://www.flashscore.co.uk/match/ice-hockey/hpk-8nboRSAG/tappara-4pQ2VSJs/ (ALLOWED). Card timing `PRE_SCHEDULED_START_WRITE`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-CHAT20261114DDA525E495-G0004 revision-1 -->

<!-- END SETTLEMENT EVENT E05 revision-1 -->

<!-- BEGIN SETTLEMENT EVENT E06 revision-1 -->
## Event · Mountfield HK U20 v HC RT TORAX Poruba 2011 U20 · 2026-11-14 · Czech U20 Extraliga juniorů 2026-27, round 21

**Final:** Mountfield HK 3-2 Poruba (regulation). **Periods:** 1:0, 0:2, 2:0; goals 13' Černý, 32' Vaculík, 38' Latvens, 45' Vyvial, 59' D. Pavlík; 'konec (60')'. **Evidence C.** Scheduled 2026-11-14T11:30:00+00:00.

| Opened source | Audit | Field read |
|---|---|---|
| https://www.onlajny.com/match/index/id/540513 | ALLOWED | 'Sobota 14.11.2026, 12:30', 21. kolo, 3:2 (1:0, 0:2, 2:0), konec (60') |

<!-- BEGIN SETTLEMENT LOCAL-20261114B4496A3F-G0006 revision-1 -->
### Settlement · `LOCAL-20261114B4496A3F-G0006` · Mountfield HK U20 v HC RT TORAX Poruba 2011 U20 · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `2ca48bb4fc07b3f55d4ec0a6447ef784df58006b24b8489a25080c89e7017cba`, 25293 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/20261114B4496A3F.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `POST_SCHEDULED_START_WRITE` (last recorded `2026-11-14T22:32:55+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| R1 | Poruba +1.5 | 0.6269 (chat-local uncalibrated scenario) | **WIN** | side margin -1, handicap +1.5: +0.5 | 0.139204 |
| R2 | Under 5.5 goals | 0.5119 (chat-local uncalibrated scenario) | **WIN** | total 5 vs 5.5: -0.5 | 0.238242 |
| INFO | Over 5.5 goals | 0.4881 (chat-local uncalibrated scenario) | **LOSS** | total 5 vs 5.5: -0.5 | 0.238242 |
| INFO | Hradec Kralove -1.5 | 0.3731 (chat-local uncalibrated scenario) | **LOSS** | side margin +1, handicap -1.5: -0.5 | 0.139204 |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_SIDE Poruba +1.5 (0.6269) WIN; TOP_TOTAL Under 5.5 goals (0.5119) WIN; RANK1 Poruba +1.5 (0.6269) WIN. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** Mountfield HK 3-2 Poruba (regulation); 1:0, 0:2, 2:0; goals 13' Černý, 32' Vaculík, 38' Latvens, 45' Vyvial, 59' D. Pavlík; 'konec (60')'. Identity matched on participants, date and competition (Czech U20 Extraliga juniorů 2026-27, round 21).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Hockey rows: every grade is the same under 60-minute, full-game and shootout-credited conventions, except where marked.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final Hradec minus Poruba = 1; total 5. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** Poruba led 2-1 after two periods; Hradec scored at 45' and the winner at 59'. A one-goal home win in regulation covered Poruba +1.5, and five goals stayed under 5.5.
**R9. Source/timing review.** Settlement sources: https://www.onlajny.com/match/index/id/540513 (ALLOWED). Card timing `POST_SCHEDULED_START_WRITE`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-20261114B4496A3F-G0006 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-202611148A011BE83FCC-G0006 revision-1 -->
### Settlement · `LOCAL-202611148A011BE83FCC-G0006` · Mountfield HK U20 v HC RT TORAX Poruba 2011 U20 · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `fa4977a1aa8d1a28d50c0cc05a8e6397d279d9178656f9ad7c9b5254e53a936f`, 9139 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/202611148A011BE83FCC.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `PRE_SCHEDULED_START_WRITE` (last recorded `2026-11-14T22:27:33+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| R1 | Poruba +1.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | side margin -1, handicap +1.5: +0.5 |  |
| NOT_PREF | Hradec Kralove -1.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | side margin +1, handicap -1.5: -0.5 |  |
| R2 | Under 5.5 goals | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | total 5 vs 5.5: -0.5 |  |
| NOT_PREF | Over 5.5 goals | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | total 5 vs 5.5: -0.5 |  |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_SIDE Poruba +1.5 (NOT_ESTIMATED) WIN; TOP_TOTAL Under 5.5 goals (NOT_ESTIMATED) WIN; RANK1 Poruba +1.5 (NOT_ESTIMATED) WIN. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** Mountfield HK 3-2 Poruba (regulation); 1:0, 0:2, 2:0; goals 13' Černý, 32' Vaculík, 38' Latvens, 45' Vyvial, 59' D. Pavlík; 'konec (60')'. Identity matched on participants, date and competition (Czech U20 Extraliga juniorů 2026-27, round 21).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Hockey rows: every grade is the same under 60-minute, full-game and shootout-credited conventions, except where marked.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final Hradec minus Poruba = 1; total 5. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** Poruba led 2-1 after two periods; Hradec scored at 45' and the winner at 59'. A one-goal home win in regulation covered Poruba +1.5, and five goals stayed under 5.5.
**R9. Source/timing review.** Settlement sources: https://www.onlajny.com/match/index/id/540513 (ALLOWED). Card timing `PRE_SCHEDULED_START_WRITE`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-202611148A011BE83FCC-G0006 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-202611148C6C0822-G0006 revision-1 -->
### Settlement · `LOCAL-202611148C6C0822-G0006` · Mountfield HK U20 v HC RT TORAX Poruba 2011 U20 · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `5551454a55a9240a1138708063aa634c7ac3c27a1c334190d96afba6cca95a83`, 8626 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/202611148C6C0822.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `PRE_SCHEDULED_START_WRITE` (last recorded `2026-11-14T22:26:52+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| R2 | Poruba +1.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | side margin -1, handicap +1.5: +0.5 |  |
| NOT_PREF | Hradec Kralove -1.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | side margin +1, handicap -1.5: -0.5 |  |
| R1 | Under 5.5 goals | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | total 5 vs 5.5: -0.5 |  |
| NOT_PREF | Over 5.5 goals | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | total 5 vs 5.5: -0.5 |  |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_SIDE Poruba +1.5 (NOT_ESTIMATED) WIN; TOP_TOTAL Under 5.5 goals (NOT_ESTIMATED) WIN; RANK1 Under 5.5 goals (NOT_ESTIMATED) WIN. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** Mountfield HK 3-2 Poruba (regulation); 1:0, 0:2, 2:0; goals 13' Černý, 32' Vaculík, 38' Latvens, 45' Vyvial, 59' D. Pavlík; 'konec (60')'. Identity matched on participants, date and competition (Czech U20 Extraliga juniorů 2026-27, round 21).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Hockey rows: every grade is the same under 60-minute, full-game and shootout-credited conventions, except where marked.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final Hradec minus Poruba = 1; total 5. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** Poruba led 2-1 after two periods; Hradec scored at 45' and the winner at 59'. A one-goal home win in regulation covered Poruba +1.5, and five goals stayed under 5.5.
**R9. Source/timing review.** Settlement sources: https://www.onlajny.com/match/index/id/540513 (ALLOWED). Card timing `PRE_SCHEDULED_START_WRITE`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-202611148C6C0822-G0006 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-20261114CHAT2988664A-G0006 revision-1 -->
### Settlement · `LOCAL-20261114CHAT2988664A-G0006` · Mountfield HK U20 v HC RT TORAX Poruba 2011 U20 · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `129cb3e8470cc97f58ed65fae99bb8b28152118cb843357a7d786e35d52a7da6`, 9568 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/20261114CHAT2988664A.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `PRE_SCHEDULED_START_WRITE` (last recorded `2026-11-14T22:26:36+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| NOT_PREF | Hradec Kralove -1.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | side margin +1, handicap -1.5: -0.5 |  |
| R1 | Poruba +1.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | side margin -1, handicap +1.5: +0.5 |  |
| NOT_PREF | Over 5.5 goals | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | total 5 vs 5.5: -0.5 |  |
| R2 | Under 5.5 goals | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | total 5 vs 5.5: -0.5 |  |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_SIDE Poruba +1.5 (NOT_ESTIMATED) WIN; TOP_TOTAL Under 5.5 goals (NOT_ESTIMATED) WIN; RANK1 Poruba +1.5 (NOT_ESTIMATED) WIN. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** Mountfield HK 3-2 Poruba (regulation); 1:0, 0:2, 2:0; goals 13' Černý, 32' Vaculík, 38' Latvens, 45' Vyvial, 59' D. Pavlík; 'konec (60')'. Identity matched on participants, date and competition (Czech U20 Extraliga juniorů 2026-27, round 21).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Hockey rows: every grade is the same under 60-minute, full-game and shootout-credited conventions, except where marked.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final Hradec minus Poruba = 1; total 5. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** Poruba led 2-1 after two periods; Hradec scored at 45' and the winner at 59'. A one-goal home win in regulation covered Poruba +1.5, and five goals stayed under 5.5.
**R9. Source/timing review.** Settlement sources: https://www.onlajny.com/match/index/id/540513 (ALLOWED). Card timing `PRE_SCHEDULED_START_WRITE`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-20261114CHAT2988664A-G0006 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-20261114EA6B2758F0-G0005 revision-1 -->
### Settlement · `LOCAL-20261114EA6B2758F0-G0005` · Mountfield HK U20 v HC RT TORAX Poruba 2011 U20 · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `3207ee354719235c22b117be268bf176e6f59689f1dd2e32bf354b73a0fce677`, 13474 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/20261114EA6B2758F0.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `WRITE_TIME_NOT_RECORDED` (last recorded `NOT_RECORDED`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| R1 | Poruba +1.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | side margin -1, handicap +1.5: +0.5 |  |
| NOT_PREF | Hradec Kralove -1.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | side margin +1, handicap -1.5: -0.5 |  |
| R2 | Under 5.5 goals | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | total 5 vs 5.5: -0.5 |  |
| NOT_PREF | Over 5.5 goals | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | total 5 vs 5.5: -0.5 |  |
| LEAN_WINNER | Hradec Kralove to win | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | side margin +1 |  |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_SIDE Poruba +1.5 (NOT_ESTIMATED) WIN; TOP_TOTAL Under 5.5 goals (NOT_ESTIMATED) WIN; RANK1 Poruba +1.5 (NOT_ESTIMATED) WIN. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** Mountfield HK 3-2 Poruba (regulation); 1:0, 0:2, 2:0; goals 13' Černý, 32' Vaculík, 38' Latvens, 45' Vyvial, 59' D. Pavlík; 'konec (60')'. Identity matched on participants, date and competition (Czech U20 Extraliga juniorů 2026-27, round 21).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Hockey rows: every grade is the same under 60-minute, full-game and shootout-credited conventions, except where marked.
**R4. Rank diagnostics.** 3W/2L/0U over 5 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final Hradec minus Poruba = 1; total 5. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** Poruba led 2-1 after two periods; Hradec scored at 45' and the winner at 59'. A one-goal home win in regulation covered Poruba +1.5, and five goals stayed under 5.5.
**R9. Source/timing review.** Settlement sources: https://www.onlajny.com/match/index/id/540513 (ALLOWED). Card timing `WRITE_TIME_NOT_RECORDED`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-20261114EA6B2758F0-G0005 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-CHAT20261114DDA525E495-G0006 revision-1 -->
### Settlement · `LOCAL-CHAT20261114DDA525E495-G0006` · Mountfield HK U20 v HC RT TORAX Poruba 2011 U20 · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `c8e2bbea19d9fbc60a1dd2b4cbea5b7470cf7f8140267048f1bdb67fd40f7344`, 12722 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/CHAT20261114DDA525E495.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `PRE_SCHEDULED_START_WRITE` (last recorded `2026-11-14T22:28:08+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| D1 | Poruba +1.5 | 0.6427 (chat-local uncalibrated scenario) | **WIN** | side margin -1, handicap +1.5: +0.5 | 0.127663 |
| NOT_RANKED | Hradec Kralove -1.5 | 0.3573 (chat-local uncalibrated scenario) | **LOSS** | side margin +1, handicap -1.5: -0.5 | 0.127663 |
| D2 | Under 5.5 goals | 0.5119 (chat-local uncalibrated scenario) | **WIN** | total 5 vs 5.5: -0.5 | 0.238242 |
| NOT_RANKED | Over 5.5 goals | 0.4881 (chat-local uncalibrated scenario) | **LOSS** | total 5 vs 5.5: -0.5 | 0.238242 |
| INFO | Hradec Kralove to win | 0.6107 (chat-local uncalibrated scenario) | **WIN** | side margin +1 | 0.151554 |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_SIDE Poruba +1.5 (0.6427) WIN; TOP_TOTAL Under 5.5 goals (0.5119) WIN; RANK1 Poruba +1.5 (0.6427) WIN. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** Mountfield HK 3-2 Poruba (regulation); 1:0, 0:2, 2:0; goals 13' Černý, 32' Vaculík, 38' Latvens, 45' Vyvial, 59' D. Pavlík; 'konec (60')'. Identity matched on participants, date and competition (Czech U20 Extraliga juniorů 2026-27, round 21).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Hockey rows: every grade is the same under 60-minute, full-game and shootout-credited conventions, except where marked.
**R4. Rank diagnostics.** 3W/2L/0U over 5 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final Hradec minus Poruba = 1; total 5. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** Poruba led 2-1 after two periods; Hradec scored at 45' and the winner at 59'. A one-goal home win in regulation covered Poruba +1.5, and five goals stayed under 5.5.
**R9. Source/timing review.** Settlement sources: https://www.onlajny.com/match/index/id/540513 (ALLOWED). Card timing `PRE_SCHEDULED_START_WRITE`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-CHAT20261114DDA525E495-G0006 revision-1 -->

<!-- END SETTLEMENT EVENT E06 revision-1 -->

<!-- BEGIN SETTLEMENT EVENT E07 revision-1 -->
## Event · Alytaus Patriotai v Mažeikių M Basket · 2026-11-14 · Lithuania URBO-NKL 2026-27

**Final:** Alytus 85-81 Mažeikiai. **Periods:** 29-19, 19-25, 16-16, 21-21 (half 48-44, after three 64-60); no OT. **Evidence B.** Scheduled 2026-11-14T12:10:00+00:00.

| Opened source | Audit | Field read |
|---|---|---|
| https://www.tv3.lt/naujiena/sportas/uzupis-pelne-21-taska-o-patriotai-iveike-m-basket-n1568471 | ALLOWED | 85:81 (29:19, 19:25, 16:16, 21:21); published 2026-11-14 16:42 |
| https://nkl.lt/komandos/alytaus-patriotai/ | ALLOWED | Row 2026-11-14 14:10:00 Alytaus Patriotai v Mažeikių M Basket 85-81 |

<!-- BEGIN SETTLEMENT LOCAL-20261114B4496A3F-G0007 revision-1 -->
### Settlement · `LOCAL-20261114B4496A3F-G0007` · Alytaus Patriotai v Mažeikių M Basket · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `07d2151d86c471e850b75857419cfaa00c6587d7e3dbf075bfd4839dce274c88`, 26588 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/20261114B4496A3F.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `PRE_SCHEDULED_START_WRITE` (last recorded `2026-11-14T23:05:37+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| R1 | Mazeikiai +12.5 | 0.6470 (chat-local uncalibrated scenario) | **WIN** | side margin -4, handicap +12.5: +8.5 | 0.124609 |
| R2 | Over 166.5 | 0.5353 (chat-local uncalibrated scenario) | **LOSS** | total 166 vs 166.5: -0.5 | 0.286546 |
| INFO | Under 166.5 | 0.4647 (chat-local uncalibrated scenario) | **WIN** | total 166 vs 166.5: -0.5 | 0.286546 |
| INFO | Alytus -12.5 | 0.3530 (chat-local uncalibrated scenario) | **LOSS** | side margin +4, handicap -12.5: -8.5 | 0.124609 |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_SIDE Mazeikiai +12.5 (0.6470) WIN; TOP_TOTAL Over 166.5 (0.5353) LOSS; RANK1 Mazeikiai +12.5 (0.6470) WIN. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** Alytus 85-81 Mažeikiai; 29-19, 19-25, 16-16, 21-21 (half 48-44, after three 64-60); no OT. Identity matched on participants, date and competition (Lithuania URBO-NKL 2026-27).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Basketball rows include overtime (BK-OT-1); none occurred.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final Alytus minus Mažeikiai = 4; total 166. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** Alytus won the first quarter by ten and the last two quarters were level, so a four-point win covered Mažeikiai +12.5 easily. The total of 166 missed Over 166.5 by half a point.
**R9. Source/timing review.** Settlement sources: https://www.tv3.lt/naujiena/sportas/uzupis-pelne-21-taska-o-patriotai-iveike-m-basket-n1568471 (ALLOWED); https://nkl.lt/komandos/alytaus-patriotai/ (ALLOWED). Card timing `PRE_SCHEDULED_START_WRITE`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-20261114B4496A3F-G0007 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-202611148A011BE83FCC-G0007 revision-1 -->
### Settlement · `LOCAL-202611148A011BE83FCC-G0007` · Alytaus Patriotai v Mažeikių M Basket · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `57b4f76cd187dca8194c3e064382388ba6a68481fbf81a9837b095b93f949907`, 14455 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/202611148A011BE83FCC.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `PRE_SCHEDULED_START_WRITE` (last recorded `2026-11-14T23:01:04+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| R1 | Mazeikiai +12.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | side margin -4, handicap +12.5: +8.5 |  |
| NOT_PREF | Alytus -12.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | side margin +4, handicap -12.5: -8.5 |  |
| R2 | Over 166.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | total 166 vs 166.5: -0.5 |  |
| ALT | Under 166.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | total 166 vs 166.5: -0.5 |  |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_SIDE Mazeikiai +12.5 (NOT_ESTIMATED) WIN; TOP_TOTAL Over 166.5 (NOT_ESTIMATED) LOSS; RANK1 Mazeikiai +12.5 (NOT_ESTIMATED) WIN. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** Alytus 85-81 Mažeikiai; 29-19, 19-25, 16-16, 21-21 (half 48-44, after three 64-60); no OT. Identity matched on participants, date and competition (Lithuania URBO-NKL 2026-27).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Basketball rows include overtime (BK-OT-1); none occurred.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final Alytus minus Mažeikiai = 4; total 166. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** Alytus won the first quarter by ten and the last two quarters were level, so a four-point win covered Mažeikiai +12.5 easily. The total of 166 missed Over 166.5 by half a point.
**R9. Source/timing review.** Settlement sources: https://www.tv3.lt/naujiena/sportas/uzupis-pelne-21-taska-o-patriotai-iveike-m-basket-n1568471 (ALLOWED); https://nkl.lt/komandos/alytaus-patriotai/ (ALLOWED). Card timing `PRE_SCHEDULED_START_WRITE`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-202611148A011BE83FCC-G0007 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-202611148C6C0822-G0007 revision-1 -->
### Settlement · `LOCAL-202611148C6C0822-G0007` · Alytaus Patriotai v Mažeikių M Basket · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `be96161c6a3c1ef4cd6209682a25915a3a11ebaf99099ce5864ba3a270077eb3`, 7860 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/202611148C6C0822.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `PRE_SCHEDULED_START_WRITE` (last recorded `2026-11-14T23:00:50+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| R1 | Mazeikiai +12.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | side margin -4, handicap +12.5: +8.5 |  |
| NOT_PREF | Alytus -12.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | side margin +4, handicap -12.5: -8.5 |  |
| R2 | Over 166.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | total 166 vs 166.5: -0.5 |  |
| NOT_PREF | Under 166.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | total 166 vs 166.5: -0.5 |  |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_SIDE Mazeikiai +12.5 (NOT_ESTIMATED) WIN; TOP_TOTAL Over 166.5 (NOT_ESTIMATED) LOSS; RANK1 Mazeikiai +12.5 (NOT_ESTIMATED) WIN. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** Alytus 85-81 Mažeikiai; 29-19, 19-25, 16-16, 21-21 (half 48-44, after three 64-60); no OT. Identity matched on participants, date and competition (Lithuania URBO-NKL 2026-27).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Basketball rows include overtime (BK-OT-1); none occurred.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final Alytus minus Mažeikiai = 4; total 166. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** Alytus won the first quarter by ten and the last two quarters were level, so a four-point win covered Mažeikiai +12.5 easily. The total of 166 missed Over 166.5 by half a point.
**R9. Source/timing review.** Settlement sources: https://www.tv3.lt/naujiena/sportas/uzupis-pelne-21-taska-o-patriotai-iveike-m-basket-n1568471 (ALLOWED); https://nkl.lt/komandos/alytaus-patriotai/ (ALLOWED). Card timing `PRE_SCHEDULED_START_WRITE`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-202611148C6C0822-G0007 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-20261114CHAT2988664A-G0007 revision-1 -->
### Settlement · `LOCAL-20261114CHAT2988664A-G0007` · Alytaus Patriotai v Mažeikių M Basket · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `38af6cbfb91ef9c3df759f6a80832b1930cc4e8d892bd240825645e8b8a07c18`, 13965 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/20261114CHAT2988664A.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `PRE_SCHEDULED_START_WRITE` (last recorded `2026-11-14T23:02:57+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| NOT_PREF | Alytus -12.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | side margin +4, handicap -12.5: -8.5 |  |
| R1 | Mazeikiai +12.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | side margin -4, handicap +12.5: +8.5 |  |
| NO_PICK | Over 166.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | total 166 vs 166.5: -0.5 |  |
| NO_PICK | Under 166.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | total 166 vs 166.5: -0.5 |  |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_SIDE Mazeikiai +12.5 (NOT_ESTIMATED) WIN; RANK1 Mazeikiai +12.5 (NOT_ESTIMATED) WIN. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** Alytus 85-81 Mažeikiai; 29-19, 19-25, 16-16, 21-21 (half 48-44, after three 64-60); no OT. Identity matched on participants, date and competition (Lithuania URBO-NKL 2026-27).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Basketball rows include overtime (BK-OT-1); none occurred.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final Alytus minus Mažeikiai = 4; total 166. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** Alytus won the first quarter by ten and the last two quarters were level, so a four-point win covered Mažeikiai +12.5 easily. The total of 166 missed Over 166.5 by half a point.
**R9. Source/timing review.** Settlement sources: https://www.tv3.lt/naujiena/sportas/uzupis-pelne-21-taska-o-patriotai-iveike-m-basket-n1568471 (ALLOWED); https://nkl.lt/komandos/alytaus-patriotai/ (ALLOWED). Card timing `PRE_SCHEDULED_START_WRITE`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-20261114CHAT2988664A-G0007 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-20261114EA6B2758F0-G0006 revision-1 -->
### Settlement · `LOCAL-20261114EA6B2758F0-G0006` · Alytaus Patriotai v Mažeikių M Basket · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `b6d92df3181445bd22e86673f165ed953ff2dbc8962cd9135d545173d45dd7e0`, 16435 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/20261114EA6B2758F0.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `PRE_SCHEDULED_START_WRITE` (last recorded `2026-11-14T23:05:09+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| R1 | Mazeikiai +12.5 | 0.5434 (chat-local uncalibrated scenario) | **WIN** | side margin -4, handicap +12.5: +8.5 | 0.208484 |
| NOT_PREF | Alytus -12.5 | 0.4566 (chat-local uncalibrated scenario) | **LOSS** | side margin +4, handicap -12.5: -8.5 | 0.208484 |
| R2 | Over 166.5 | 0.5220 (chat-local uncalibrated scenario) | **LOSS** | total 166 vs 166.5: -0.5 | 0.272484 |
| NOT_PREF | Under 166.5 | 0.4780 (chat-local uncalibrated scenario) | **WIN** | total 166 vs 166.5: -0.5 | 0.272484 |
| INFO | Alytus to win | 0.7448 (chat-local uncalibrated scenario) | **WIN** | side margin +4 | 0.065127 |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_SIDE Mazeikiai +12.5 (0.5434) WIN; TOP_TOTAL Over 166.5 (0.5220) LOSS; RANK1 Mazeikiai +12.5 (0.5434) WIN. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** Alytus 85-81 Mažeikiai; 29-19, 19-25, 16-16, 21-21 (half 48-44, after three 64-60); no OT. Identity matched on participants, date and competition (Lithuania URBO-NKL 2026-27).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Basketball rows include overtime (BK-OT-1); none occurred.
**R4. Rank diagnostics.** 3W/2L/0U over 5 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final Alytus minus Mažeikiai = 4; total 166. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** Alytus won the first quarter by ten and the last two quarters were level, so a four-point win covered Mažeikiai +12.5 easily. The total of 166 missed Over 166.5 by half a point.
**R9. Source/timing review.** Settlement sources: https://www.tv3.lt/naujiena/sportas/uzupis-pelne-21-taska-o-patriotai-iveike-m-basket-n1568471 (ALLOWED); https://nkl.lt/komandos/alytaus-patriotai/ (ALLOWED). Card timing `PRE_SCHEDULED_START_WRITE`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-20261114EA6B2758F0-G0006 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-CHAT20261114DDA525E495-G0007 revision-1 -->
### Settlement · `LOCAL-CHAT20261114DDA525E495-G0007` · Alytaus Patriotai v Mažeikių M Basket · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `cee3908c041835082ffbf4b746971c01d67972d6eabfc71667744099e125b1f2`, 15645 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/CHAT20261114DDA525E495.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `PRE_SCHEDULED_START_WRITE` (last recorded `2026-11-14T23:04:00+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| D1 | Mazeikiai +12.5 | 0.6252 (chat-local uncalibrated scenario) | **WIN** | side margin -4, handicap +12.5: +8.5 | 0.140475 |
| NOT_RANKED | Alytus -12.5 | 0.3748 (chat-local uncalibrated scenario) | **LOSS** | side margin +4, handicap -12.5: -8.5 | 0.140475 |
| D2 | Over 166.5 | 0.5324 (chat-local uncalibrated scenario) | **LOSS** | total 166 vs 166.5: -0.5 | 0.283450 |
| NOT_RANKED | Under 166.5 | 0.4676 (chat-local uncalibrated scenario) | **WIN** | total 166 vs 166.5: -0.5 | 0.283450 |
| INFO | Alytus to win | 0.6684 (chat-local uncalibrated scenario) | **WIN** | side margin +4 | 0.109959 |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_SIDE Mazeikiai +12.5 (0.6252) WIN; TOP_TOTAL Over 166.5 (0.5324) LOSS; RANK1 Mazeikiai +12.5 (0.6252) WIN. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** Alytus 85-81 Mažeikiai; 29-19, 19-25, 16-16, 21-21 (half 48-44, after three 64-60); no OT. Identity matched on participants, date and competition (Lithuania URBO-NKL 2026-27).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Basketball rows include overtime (BK-OT-1); none occurred.
**R4. Rank diagnostics.** 3W/2L/0U over 5 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final Alytus minus Mažeikiai = 4; total 166. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** Alytus won the first quarter by ten and the last two quarters were level, so a four-point win covered Mažeikiai +12.5 easily. The total of 166 missed Over 166.5 by half a point.
**R9. Source/timing review.** Settlement sources: https://www.tv3.lt/naujiena/sportas/uzupis-pelne-21-taska-o-patriotai-iveike-m-basket-n1568471 (ALLOWED); https://nkl.lt/komandos/alytaus-patriotai/ (ALLOWED). Card timing `PRE_SCHEDULED_START_WRITE`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-CHAT20261114DDA525E495-G0007 revision-1 -->

### Deep loss reviews (DEEPLOSS-v1)

#### Deep loss review · Alytaus Patriotai v Mažeikių M Basket · Over 166.5

**1. Exact frozen claim.** `Over 166.5`, full-game endpoint as each card defined it. Triggered in 5 card(s):

| Card | Trigger role(s) | Original p (basis) | Brier | Log loss |
|---|---|---|---:|---:|
| `LOCAL-202611148A011BE83FCC-G0007` | TOP_TOTAL | NOT_ESTIMATED (qualitative (no numeric p)) |  |  |
| `LOCAL-202611148C6C0822-G0007` | TOP_TOTAL | NOT_ESTIMATED (qualitative (no numeric p)) |  |  |
| `LOCAL-20261114B4496A3F-G0007` | TOP_TOTAL | 0.5353 (chat-local uncalibrated scenario) | 0.286546 | 0.766363 |
| `LOCAL-20261114EA6B2758F0-G0006` | TOP_TOTAL | 0.5220 (chat-local uncalibrated scenario) | 0.272484 | 0.738145 |
| `LOCAL-CHAT20261114DDA525E495-G0007` | TOP_TOTAL | 0.5324 (chat-local uncalibrated scenario) | 0.283450 | 0.760142 |

No card carried a primary p_card, frozen reference or same-row baseline; BASELINE_P comparison NOT_COMPUTABLE.

**2. Verified outcome.** Alytus 85-81 Mažeikiai (29-19, 19-25, 16-16, 21-21 (half 48-44, after three 64-60); no OT). total 166 vs 166.5: -0.5. Sources in R9; evidence B; final wall-clock NOT_VERIFIED.
**3. Distribution check.** Numeric cards priced this row at 0.522-0.535; a loss at those prices is a 46%-48% event under each card's own uncalibrated object.
**4. Error decomposition.** Realised distance: total 166 vs 166.5: -0.5. No card had a calibrated centre or a measured effect row, so the miss is not split into reference and adjustment error; no blame shares are invented.
**5. Research audit.** Five cards had scoring centres of 167.75 to 168.3, within two points of the line; three called it 'very slight', 'near coin flip' or 'marginal'.
**6. What decided the game.** Alytus won the first quarter by ten and the last two quarters were level, so a four-point win covered Mažeikiai +12.5 easily. The total of 166 missed Over 166.5 by half a point.
**7. Knowable at cutoff?** Knowable: that the line sat on the centre. Not knowable: a 16-16 third quarter and a 21-21 fourth.
**8. Process audit.** Chat-local record; no repository reference stage, no source-audit receipts, no lineup confirmation, no freeze. Timing per card in CARD_TIMING.csv.
**9. Verdict.** VARIANCE. The total finished at 166, half a point short. A centre this close to the line is no lean; it should have been recorded as no direction, which one card (CHAT2988664A) did.
**10. Cutoff-only counterfactual.** NOT_ESTIMATED: no knowable fact has a measured effect-table row, so no corrected probability is priced after the result.
**11. Failure class and recurrence.** Shared across 5 cards on one game: overlapping public inputs make these one dependent observation, not 5.
**12. Correction.** NO_CHANGE to any rule from one result. Pattern-level proposals are in AUDIT_REPORT (PROPOSED_NOT_TESTED).
**13. Matched wins.** `LOCAL-202611148A011BE83FCC-G0007` RANK1 Mazeikiai +12.5 WIN; `LOCAL-202611148A011BE83FCC-G0007` TOP_SIDE Mazeikiai +12.5 WIN; `LOCAL-202611148C6C0822-G0007` RANK1 Mazeikiai +12.5 WIN; `LOCAL-202611148C6C0822-G0007` TOP_SIDE Mazeikiai +12.5 WIN; `LOCAL-20261114B4496A3F-G0007` RANK1 Mazeikiai +12.5 WIN; `LOCAL-20261114B4496A3F-G0007` TOP_SIDE Mazeikiai +12.5 WIN; `LOCAL-20261114EA6B2758F0-G0006` RANK1 Mazeikiai +12.5 WIN; `LOCAL-20261114EA6B2758F0-G0006` TOP_SIDE Mazeikiai +12.5 WIN; `LOCAL-CHAT20261114DDA525E495-G0007` RANK1 Mazeikiai +12.5 WIN; `LOCAL-CHAT20261114DDA525E495-G0007` TOP_SIDE Mazeikiai +12.5 WIN. These rest on the same unvalidated construction and do not show the process worked.
**14. Honesty.** Original numbers and labels preserved; no luck claim without the arithmetic above; no invented percentages, operator terms or publication times.

<!-- END SETTLEMENT EVENT E07 revision-1 -->

<!-- BEGIN SETTLEMENT EVENT E08 revision-1 -->
## Event · Vimmerby HC v Nybro Vikings IF · 2026-11-14 · Sweden HockeyAllsvenskan 2026-27

**Final:** Vimmerby 5-2 Nybro (regulation). **Periods:** 1-0, 2-2, 2-0; 1,047 spectators, VBO Arena. **Evidence B.** Scheduled 2026-11-14T14:00:00+00:00. Note: An earlier hockeysverige page (18 Sep 2026, Nybro 7-6 SO) is a different game and is excluded.

| Opened source | Audit | Field read |
|---|---|---|
| https://stats.swehockey.se/ScheduleAndResults/Schedule/20962 | NO_RULES_FILE | '2026-11-14 15:00 Vimmerby HC - Nybro Vikings IF 5 - 2 (1-0, 2-2, 2-0)' |
| https://www.tvmatchen.nu/sport/ishockey/hockeyallsvenskan-resultat-14-november-2026/ | ALLOWED | 'Vimmerby–Nybro 5-2'; scorer narrative; published 14 November 22:04 |

<!-- BEGIN SETTLEMENT LOCAL-20261114B4496A3F-G0008 revision-1 -->
### Settlement · `LOCAL-20261114B4496A3F-G0008` · Vimmerby HC v Nybro Vikings IF · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `297049ffdbb568203ffbafa2c8a359a5facb24645087f55837fdff6f2296e446`, 31750 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/20261114B4496A3F.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `WRITE_TIME_NOT_RECORDED` (last recorded `NOT_RECORDED`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| R1 | Under 5.5 goals | 0.579 (chat-local uncalibrated scenario) | **LOSS** | total 7 vs 5.5: +1.5 | 0.335241 |
| R2 | Vimmerby ML | 0.525 (chat-local uncalibrated scenario) | **WIN** | side margin +3 | 0.225625 |
| INFO | Nybro ML | 0.475 (chat-local uncalibrated scenario) | **LOSS** | side margin -3 | 0.225625 |
| INFO | Over 5.5 goals | 0.421 (chat-local uncalibrated scenario) | **WIN** | total 7 vs 5.5: +1.5 | 0.335241 |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_SIDE Vimmerby ML (0.525) WIN; TOP_TOTAL Under 5.5 goals (0.579) LOSS; RANK1 Under 5.5 goals (0.579) LOSS. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** Vimmerby 5-2 Nybro (regulation); 1-0, 2-2, 2-0; 1,047 spectators, VBO Arena. Identity matched on participants, date and competition (Sweden HockeyAllsvenskan 2026-27).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Hockey rows: every grade is the same under 60-minute, full-game and shootout-credited conventions, except where marked.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final Vimmerby minus Nybro = 3; total 7. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** Orrsten opened in the first; after Krämer's equaliser Vimmerby scored twice in quick succession (Lejon, Andersson) for 3-1, Lindfors made it 3-2, and Vimmerby scored twice in the third (Karlsson on the power play, Lejon). A three-goal home win; seven goals.
**R9. Source/timing review.** Settlement sources: https://stats.swehockey.se/ScheduleAndResults/Schedule/20962 (NO_RULES_FILE); https://www.tvmatchen.nu/sport/ishockey/hockeyallsvenskan-resultat-14-november-2026/ (ALLOWED). Card timing `WRITE_TIME_NOT_RECORDED`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-20261114B4496A3F-G0008 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-202611148A011BE83FCC-G0008 revision-1 -->
### Settlement · `LOCAL-202611148A011BE83FCC-G0008` · Vimmerby HC v Nybro Vikings IF · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `a54c814f44d75cbb9d46475d1565338979d9d02b7f065c7a4db9a096d333bd38`, 12882 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/202611148A011BE83FCC.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `PRE_SCHEDULED_START_WRITE` (last recorded `2026-11-15T00:49:20+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| R1 | Nybro ML | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | side margin -3 |  |
| NOT_PREF | Vimmerby ML | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | side margin +3 |  |
| R2 | Over 5.5 goals | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | total 7 vs 5.5: +1.5 |  |
| NOT_PREF | Under 5.5 goals | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | total 7 vs 5.5: +1.5 |  |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_SIDE Nybro ML (NOT_ESTIMATED) LOSS; TOP_TOTAL Over 5.5 goals (NOT_ESTIMATED) WIN; RANK1 Nybro ML (NOT_ESTIMATED) LOSS. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** Vimmerby 5-2 Nybro (regulation); 1-0, 2-2, 2-0; 1,047 spectators, VBO Arena. Identity matched on participants, date and competition (Sweden HockeyAllsvenskan 2026-27).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Hockey rows: every grade is the same under 60-minute, full-game and shootout-credited conventions, except where marked.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final Vimmerby minus Nybro = 3; total 7. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** Orrsten opened in the first; after Krämer's equaliser Vimmerby scored twice in quick succession (Lejon, Andersson) for 3-1, Lindfors made it 3-2, and Vimmerby scored twice in the third (Karlsson on the power play, Lejon). A three-goal home win; seven goals.
**R9. Source/timing review.** Settlement sources: https://stats.swehockey.se/ScheduleAndResults/Schedule/20962 (NO_RULES_FILE); https://www.tvmatchen.nu/sport/ishockey/hockeyallsvenskan-resultat-14-november-2026/ (ALLOWED). Card timing `PRE_SCHEDULED_START_WRITE`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-202611148A011BE83FCC-G0008 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-202611148C6C0822-G0008 revision-1 -->
### Settlement · `LOCAL-202611148C6C0822-G0008` · Vimmerby HC v Nybro Vikings IF · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `1e953af0c8356581a9ec68ae78802fdbb31a0792e7f82af0309dd3b6c010ae16`, 12215 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/202611148C6C0822.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `PRE_SCHEDULED_START_WRITE` (last recorded `2026-11-15T00:49:32+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| R1 | Nybro ML | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | side margin -3 |  |
| NOT_PREF | Vimmerby ML | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | side margin +3 |  |
| R2 | Under 5.5 goals | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | total 7 vs 5.5: +1.5 |  |
| NOT_PREF | Over 5.5 goals | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | total 7 vs 5.5: +1.5 |  |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_SIDE Nybro ML (NOT_ESTIMATED) LOSS; TOP_TOTAL Under 5.5 goals (NOT_ESTIMATED) LOSS; RANK1 Nybro ML (NOT_ESTIMATED) LOSS. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** Vimmerby 5-2 Nybro (regulation); 1-0, 2-2, 2-0; 1,047 spectators, VBO Arena. Identity matched on participants, date and competition (Sweden HockeyAllsvenskan 2026-27).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Hockey rows: every grade is the same under 60-minute, full-game and shootout-credited conventions, except where marked.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final Vimmerby minus Nybro = 3; total 7. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** Orrsten opened in the first; after Krämer's equaliser Vimmerby scored twice in quick succession (Lejon, Andersson) for 3-1, Lindfors made it 3-2, and Vimmerby scored twice in the third (Karlsson on the power play, Lejon). A three-goal home win; seven goals.
**R9. Source/timing review.** Settlement sources: https://stats.swehockey.se/ScheduleAndResults/Schedule/20962 (NO_RULES_FILE); https://www.tvmatchen.nu/sport/ishockey/hockeyallsvenskan-resultat-14-november-2026/ (ALLOWED). Card timing `PRE_SCHEDULED_START_WRITE`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-202611148C6C0822-G0008 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-20261114CHAT2988664A-G0008 revision-1 -->
### Settlement · `LOCAL-20261114CHAT2988664A-G0008` · Vimmerby HC v Nybro Vikings IF · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `6c03bf533c14c09255dc6e9caaeeb56e7f224b5e9784f29c036fd8dbb4a150f5`, 12009 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/20261114CHAT2988664A.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `PRE_SCHEDULED_START_WRITE` (last recorded `2026-11-15T00:43:00+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| NOT_PREF | Vimmerby ML | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | side margin +3 |  |
| R1 | Nybro ML | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | side margin -3 |  |
| WEAK_LEAN | Over 5.5 goals | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | total 7 vs 5.5: +1.5 |  |
| NOT_PREF | Under 5.5 goals | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | total 7 vs 5.5: +1.5 |  |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_SIDE Nybro ML (NOT_ESTIMATED) LOSS; TOP_TOTAL Over 5.5 goals (NOT_ESTIMATED) WIN; RANK1 Nybro ML (NOT_ESTIMATED) LOSS. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** Vimmerby 5-2 Nybro (regulation); 1-0, 2-2, 2-0; 1,047 spectators, VBO Arena. Identity matched on participants, date and competition (Sweden HockeyAllsvenskan 2026-27).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Hockey rows: every grade is the same under 60-minute, full-game and shootout-credited conventions, except where marked.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final Vimmerby minus Nybro = 3; total 7. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** Orrsten opened in the first; after Krämer's equaliser Vimmerby scored twice in quick succession (Lejon, Andersson) for 3-1, Lindfors made it 3-2, and Vimmerby scored twice in the third (Karlsson on the power play, Lejon). A three-goal home win; seven goals.
**R9. Source/timing review.** Settlement sources: https://stats.swehockey.se/ScheduleAndResults/Schedule/20962 (NO_RULES_FILE); https://www.tvmatchen.nu/sport/ishockey/hockeyallsvenskan-resultat-14-november-2026/ (ALLOWED). Card timing `PRE_SCHEDULED_START_WRITE`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-20261114CHAT2988664A-G0008 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-20261114EA6B2758F0-G0007 revision-1 -->
### Settlement · `LOCAL-20261114EA6B2758F0-G0007` · Vimmerby HC v Nybro Vikings IF · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `de53c2a6cf5fa3a07343d1657c766283e1f5efb3153e3483d18058972b8a8760`, 13139 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/20261114EA6B2758F0.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `PRE_SCHEDULED_START_WRITE` (last recorded `2026-11-15T00:52:11+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| R1 | Nybro ML | 0.526 (chat-local uncalibrated scenario) | **LOSS** | side margin -3 | 0.276676 |
| R2 | Over 5.5 goals | 0.517 (chat-local uncalibrated scenario) | **WIN** | total 7 vs 5.5: +1.5 | 0.233289 |
| NOT_PREF | Under 5.5 goals | 0.483 (chat-local uncalibrated scenario) | **LOSS** | total 7 vs 5.5: +1.5 | 0.233289 |
| NOT_PREF | Vimmerby ML | 0.474 (chat-local uncalibrated scenario) | **WIN** | side margin +3 | 0.276676 |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_SIDE Nybro ML (0.526) LOSS; TOP_TOTAL Over 5.5 goals (0.517) WIN; RANK1 Nybro ML (0.526) LOSS. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** Vimmerby 5-2 Nybro (regulation); 1-0, 2-2, 2-0; 1,047 spectators, VBO Arena. Identity matched on participants, date and competition (Sweden HockeyAllsvenskan 2026-27).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Hockey rows: every grade is the same under 60-minute, full-game and shootout-credited conventions, except where marked.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final Vimmerby minus Nybro = 3; total 7. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** Orrsten opened in the first; after Krämer's equaliser Vimmerby scored twice in quick succession (Lejon, Andersson) for 3-1, Lindfors made it 3-2, and Vimmerby scored twice in the third (Karlsson on the power play, Lejon). A three-goal home win; seven goals.
**R9. Source/timing review.** Settlement sources: https://stats.swehockey.se/ScheduleAndResults/Schedule/20962 (NO_RULES_FILE); https://www.tvmatchen.nu/sport/ishockey/hockeyallsvenskan-resultat-14-november-2026/ (ALLOWED). Card timing `PRE_SCHEDULED_START_WRITE`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-20261114EA6B2758F0-G0007 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-CHAT20261114DDA525E495-G0008 revision-1 -->
### Settlement · `LOCAL-CHAT20261114DDA525E495-G0008` · Vimmerby HC v Nybro Vikings IF · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `1eecf92210dbc98a4f78765972d251961883620654bd74bde0f909102e581c5c`, 14928 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/CHAT20261114DDA525E495.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `PRE_SCHEDULED_START_WRITE` (last recorded `2026-11-15T00:54:04+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| D1 | Nybro ML | 0.5279 (chat-local uncalibrated scenario) | **LOSS** | side margin -3 | 0.278678 |
| NOT_RANKED | Vimmerby ML | 0.4721 (chat-local uncalibrated scenario) | **WIN** | side margin +3 | 0.278678 |
| NO_DIRECTION | Under 5.5 goals | 0.5003 (chat-local uncalibrated scenario) | **LOSS** | total 7 vs 5.5: +1.5 | 0.250300 |
| NO_DIRECTION | Over 5.5 goals | 0.4997 (chat-local uncalibrated scenario) | **WIN** | total 7 vs 5.5: +1.5 | 0.250300 |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_SIDE Nybro ML (0.5279) LOSS; RANK1 Nybro ML (0.5279) LOSS. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** Vimmerby 5-2 Nybro (regulation); 1-0, 2-2, 2-0; 1,047 spectators, VBO Arena. Identity matched on participants, date and competition (Sweden HockeyAllsvenskan 2026-27).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Hockey rows: every grade is the same under 60-minute, full-game and shootout-credited conventions, except where marked.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final Vimmerby minus Nybro = 3; total 7. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** Orrsten opened in the first; after Krämer's equaliser Vimmerby scored twice in quick succession (Lejon, Andersson) for 3-1, Lindfors made it 3-2, and Vimmerby scored twice in the third (Karlsson on the power play, Lejon). A three-goal home win; seven goals.
**R9. Source/timing review.** Settlement sources: https://stats.swehockey.se/ScheduleAndResults/Schedule/20962 (NO_RULES_FILE); https://www.tvmatchen.nu/sport/ishockey/hockeyallsvenskan-resultat-14-november-2026/ (ALLOWED). Card timing `PRE_SCHEDULED_START_WRITE`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-CHAT20261114DDA525E495-G0008 revision-1 -->

### Deep loss reviews (DEEPLOSS-v1)

#### Deep loss review · Vimmerby HC v Nybro Vikings IF · Nybro ML

**1. Exact frozen claim.** `Nybro ML`, full-game endpoint as each card defined it. Triggered in 5 card(s):

| Card | Trigger role(s) | Original p (basis) | Brier | Log loss |
|---|---|---|---:|---:|
| `LOCAL-202611148A011BE83FCC-G0008` | TOP_SIDE, RANK1 | NOT_ESTIMATED (qualitative (no numeric p)) |  |  |
| `LOCAL-202611148C6C0822-G0008` | TOP_SIDE, RANK1 | NOT_ESTIMATED (qualitative (no numeric p)) |  |  |
| `LOCAL-20261114CHAT2988664A-G0008` | TOP_SIDE, RANK1 | NOT_ESTIMATED (qualitative (no numeric p)) |  |  |
| `LOCAL-20261114EA6B2758F0-G0007` | TOP_SIDE, RANK1 | 0.526 (chat-local uncalibrated scenario) | 0.276676 | 0.746548 |
| `LOCAL-CHAT20261114DDA525E495-G0008` | TOP_SIDE, RANK1 | 0.5279 (chat-local uncalibrated scenario) | 0.278678 | 0.750564 |

No card carried a primary p_card, frozen reference or same-row baseline; BASELINE_P comparison NOT_COMPUTABLE.

**2. Verified outcome.** Vimmerby 5-2 Nybro (regulation) (1-0, 2-2, 2-0; 1,047 spectators, VBO Arena). side margin -3. Sources in R9; evidence B; final wall-clock NOT_VERIFIED.
**3. Distribution check.** Numeric cards priced this row at 0.526-0.528; a loss at those prices is a 47%-47% event under each card's own uncalibrated object.
**4. Error decomposition.** Realised distance: side margin -3. No card had a calibrated centre or a measured effect row, so the miss is not split into reference and adjustment error; no blame shares are invented.
**5. Research audit.** Five cards read Nybro's 19 v 15 table points, stronger defence and two recent wins; the numeric cards gave 0.526 and 0.528. B44's later goalie addendum moved its own lean to Under and Vimmerby. Vimmerby's home ice and its 4-3 shootout win the night before were noted.
**6. What decided the game.** Orrsten opened in the first; after Krämer's equaliser Vimmerby scored twice in quick succession (Lejon, Andersson) for 3-1, Lindfors made it 3-2, and Vimmerby scored twice in the third (Karlsson on the power play, Lejon). A three-goal home win; seven goals.
**7. Knowable at cutoff?** Knowable: the near-even numbers. Not knowable: Vimmerby's two quick second-period goals and two third-period goals, one on the power play.
**8. Process audit.** Chat-local record; no repository reference stage, no source-audit receipts, no lineup confirmation, no freeze. Timing per card in CARD_TIMING.csv.
**9. Verdict.** VARIANCE / no edge. Every card's own estimate was a coin flip; a 'lean' at 0.53 is not a pick. Recording it as rank 1 overstated it.
**10. Cutoff-only counterfactual.** NOT_ESTIMATED: no knowable fact has a measured effect-table row, so no corrected probability is priced after the result.
**11. Failure class and recurrence.** Shared across 5 cards on one game: overlapping public inputs make these one dependent observation, not 5.
**12. Correction.** NO_CHANGE to any rule from one result. Pattern-level proposals are in AUDIT_REPORT (PROPOSED_NOT_TESTED).
**13. Matched wins.** `LOCAL-202611148A011BE83FCC-G0008` TOP_TOTAL Over 5.5 goals WIN; `LOCAL-20261114CHAT2988664A-G0008` TOP_TOTAL Over 5.5 goals WIN; `LOCAL-20261114EA6B2758F0-G0007` TOP_TOTAL Over 5.5 goals WIN. These rest on the same unvalidated construction and do not show the process worked.
**14. Honesty.** Original numbers and labels preserved; no luck claim without the arithmetic above; no invented percentages, operator terms or publication times.

#### Deep loss review · Vimmerby HC v Nybro Vikings IF · Under 5.5 goals

**1. Exact frozen claim.** `Under 5.5 goals`, full-game endpoint as each card defined it. Triggered in 2 card(s):

| Card | Trigger role(s) | Original p (basis) | Brier | Log loss |
|---|---|---|---:|---:|
| `LOCAL-202611148C6C0822-G0008` | TOP_TOTAL | NOT_ESTIMATED (qualitative (no numeric p)) |  |  |
| `LOCAL-20261114B4496A3F-G0008` | TOP_TOTAL, RANK1 | 0.579 (chat-local uncalibrated scenario) | 0.335241 | 0.865122 |

No card carried a primary p_card, frozen reference or same-row baseline; BASELINE_P comparison NOT_COMPUTABLE.

**2. Verified outcome.** Vimmerby 5-2 Nybro (regulation) (1-0, 2-2, 2-0; 1,047 spectators, VBO Arena). total 7 vs 5.5: +1.5. Sources in R9; evidence B; final wall-clock NOT_VERIFIED.
**3. Distribution check.** Numeric cards priced this row at 0.579-0.579; a loss at those prices is a 42%-42% event under each card's own uncalibrated object.
**4. Error decomposition.** Realised distance: total 7 vs 5.5: +1.5. No card had a calibrated centre or a measured effect row, so the miss is not split into reference and adjustment error; no blame shares are invented.
**5. Research audit.** 8C6 (qualitative) and B44 (0.579) leaned Under on both sides' recent 3/5 totals of five or fewer. B44's own sensitivity put Under between 47.7% and 68.4% for ±0.3 goals per side.
**6. What decided the game.** Orrsten opened in the first; after Krämer's equaliser Vimmerby scored twice in quick succession (Lejon, Andersson) for 3-1, Lindfors made it 3-2, and Vimmerby scored twice in the third (Karlsson on the power play, Lejon). A three-goal home win; seven goals.
**7. Knowable at cutoff?** Knowable: Vimmerby's weak penalty kill and 3.72 goals against per game. Not knowable: two third-period Vimmerby goals, one on the power play.
**8. Process audit.** Chat-local record; no repository reference stage, no source-audit receipts, no lineup confirmation, no freeze. Timing per card in CARD_TIMING.csv.
**9. Verdict.** VARIANCE with MODEL_LIMIT: the model's range spanned both sides of 50%. Seven goals came from in-game events, not an unseen pre-game fact.
**10. Cutoff-only counterfactual.** NOT_ESTIMATED: no knowable fact has a measured effect-table row, so no corrected probability is priced after the result.
**11. Failure class and recurrence.** Shared across 2 cards on one game: overlapping public inputs make these one dependent observation, not 2.
**12. Correction.** NO_CHANGE to any rule from one result. Pattern-level proposals are in AUDIT_REPORT (PROPOSED_NOT_TESTED).
**13. Matched wins.** `LOCAL-20261114B4496A3F-G0008` TOP_SIDE Vimmerby ML WIN. These rest on the same unvalidated construction and do not show the process worked.
**14. Honesty.** Original numbers and labels preserved; no luck claim without the arithmetic above; no invented percentages, operator terms or publication times.

#### Joint section · top side and top total both lost · Vimmerby HC v Nybro Vikings IF

Cards: `LOCAL-202611148C6C0822-G0008`: Nybro ML and Under 5.5 goals. Both legs failed on one game state (Vimmerby 5-2 Nybro (regulation)); the leans shared one premise, so treating them as two independent picks would double-count one wrong read.

<!-- END SETTLEMENT EVENT E08 revision-1 -->

<!-- BEGIN SETTLEMENT EVENT E09 revision-1 -->
## Event · IF Malmö Redhawks v Växjö Lakers HC · 2026-11-14 · SHL 2026-27

**Final:** Växjö 2-1 Malmö (at Malmö). **Periods:** Nadeau scored both Växjö goals; period scores and regulation/OT NOT_VERIFIED. **Evidence C.** Scheduled 2026-11-14T14:15:00+00:00. Note: The hockeysverige page first found (Växjö 4-3 OT) was published 22 Sep 2026 and is a different game; excluded.

| Opened source | Audit | Field read |
|---|---|---|
| https://www.tvmatchen.nu/sport/ishockey/shl-resultat-14-november-2026/ | ALLOWED | 'Malmö–Växjö | 1-2'; 'Smålandslaget vann med 2-1 borta mot Malmö ... Olivier Nadeau ... båda målen'; published 14 november 21:51 |

<!-- BEGIN SETTLEMENT LOCAL-20261114B4496A3F-G0009 revision-1 -->
### Settlement · `LOCAL-20261114B4496A3F-G0009` · IF Malmö Redhawks v Växjö Lakers HC · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `f6c0b7280a7ebef53e3f54317b0253401b1f5799f201dfcb428ddfadcaaf2f1d`, 25296 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/20261114B4496A3F.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `POST_SCHEDULED_START_WRITE` (last recorded `2026-11-15T01:20:27+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| R1 | Malmo ML | 0.6695 (chat-local uncalibrated scenario) | **LOSS** | side margin -1 | 0.448230 |
| R2 | Vaxjo +1.5 | 0.5868 (chat-local uncalibrated scenario) | **WIN** | side margin +1, handicap +1.5: +2.5 | 0.170734 |
| R3 | Under 5.5 goals | 0.5461 (chat-local uncalibrated scenario) | **WIN** | total 3 vs 5.5: -2.5 | 0.206025 |
| R4 | Over 5.5 goals | 0.4539 (chat-local uncalibrated scenario) | **LOSS** | total 3 vs 5.5: -2.5 | 0.206025 |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_SIDE Malmo ML (0.6695) LOSS; TOP_TOTAL Under 5.5 goals (0.5461) WIN; RANK1 Malmo ML (0.6695) LOSS. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** Växjö 2-1 Malmö (at Malmö); Nadeau scored both Växjö goals; period scores and regulation/OT NOT_VERIFIED. Identity matched on participants, date and competition (SHL 2026-27).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Hockey rows: every grade is the same under 60-minute, full-game and shootout-credited conventions, except where marked.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final Malmö minus Växjö = -1; total 3. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** Växjö won 2-1 away with Nadeau scoring twice. Malmö ML lost and Växjö +1.5 won under any OT/SO convention; three goals stayed under 5.5 under any convention.
**R9. Source/timing review.** Settlement sources: https://www.tvmatchen.nu/sport/ishockey/shl-resultat-14-november-2026/ (ALLOWED). Card timing `POST_SCHEDULED_START_WRITE`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-20261114B4496A3F-G0009 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-202611148A011BE83FCC-G0009 revision-1 -->
### Settlement · `LOCAL-202611148A011BE83FCC-G0009` · IF Malmö Redhawks v Växjö Lakers HC · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `bc1196b313431f8e30f46a86f87b4e896790b0369e7738a04e1c9c978ad89e06`, 13203 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/202611148A011BE83FCC.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `POST_SCHEDULED_START_WRITE` (last recorded `2026-11-15T01:16:16+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| R1 | Under 5.5 goals | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | total 3 vs 5.5: -2.5 |  |
| R2 | Vaxjo +1.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | side margin +1, handicap +1.5: +2.5 |  |
| R3 | Malmo ML | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | side margin -1 |  |
| NOT_PREF | Over 5.5 goals | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | total 3 vs 5.5: -2.5 |  |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_SIDE Vaxjo +1.5 (NOT_ESTIMATED) WIN; TOP_TOTAL Under 5.5 goals (NOT_ESTIMATED) WIN; RANK1 Under 5.5 goals (NOT_ESTIMATED) WIN. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** Växjö 2-1 Malmö (at Malmö); Nadeau scored both Växjö goals; period scores and regulation/OT NOT_VERIFIED. Identity matched on participants, date and competition (SHL 2026-27).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Hockey rows: every grade is the same under 60-minute, full-game and shootout-credited conventions, except where marked.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final Malmö minus Växjö = -1; total 3. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** Växjö won 2-1 away with Nadeau scoring twice. Malmö ML lost and Växjö +1.5 won under any OT/SO convention; three goals stayed under 5.5 under any convention.
**R9. Source/timing review.** Settlement sources: https://www.tvmatchen.nu/sport/ishockey/shl-resultat-14-november-2026/ (ALLOWED). Card timing `POST_SCHEDULED_START_WRITE`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-202611148A011BE83FCC-G0009 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-202611148C6C0822-G0009 revision-1 -->
### Settlement · `LOCAL-202611148C6C0822-G0009` · IF Malmö Redhawks v Växjö Lakers HC · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `f7cc65355ca17df0ee76fce4452e9277a03e75ddf4dbb5e2ee7bbf752e84f944`, 11588 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/202611148C6C0822.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `POST_SCHEDULED_START_WRITE` (last recorded `2026-11-15T01:16:19+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| R1 | Malmo ML | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | side margin -1 |  |
| R2 | Under 5.5 goals | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | total 3 vs 5.5: -2.5 |  |
| R3 | Vaxjo +1.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | side margin +1, handicap +1.5: +2.5 |  |
| R4 | Over 5.5 goals | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | total 3 vs 5.5: -2.5 |  |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_SIDE Malmo ML (NOT_ESTIMATED) LOSS; TOP_TOTAL Under 5.5 goals (NOT_ESTIMATED) WIN; RANK1 Malmo ML (NOT_ESTIMATED) LOSS. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** Växjö 2-1 Malmö (at Malmö); Nadeau scored both Växjö goals; period scores and regulation/OT NOT_VERIFIED. Identity matched on participants, date and competition (SHL 2026-27).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Hockey rows: every grade is the same under 60-minute, full-game and shootout-credited conventions, except where marked.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final Malmö minus Växjö = -1; total 3. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** Växjö won 2-1 away with Nadeau scoring twice. Malmö ML lost and Växjö +1.5 won under any OT/SO convention; three goals stayed under 5.5 under any convention.
**R9. Source/timing review.** Settlement sources: https://www.tvmatchen.nu/sport/ishockey/shl-resultat-14-november-2026/ (ALLOWED). Card timing `POST_SCHEDULED_START_WRITE`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-202611148C6C0822-G0009 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-20261114CHAT2988664A-G0009 revision-1 -->
### Settlement · `LOCAL-20261114CHAT2988664A-G0009` · IF Malmö Redhawks v Växjö Lakers HC · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `d2f182cdcd0777e7260dbf646c2f516be6fd08e0e83e14898d24e7c83b96bf2a`, 11998 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/20261114CHAT2988664A.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `POST_SCHEDULED_START_WRITE` (last recorded `2026-11-15T01:16:03+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| R1 | Vaxjo +1.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | side margin +1, handicap +1.5: +2.5 |  |
| R2 | Malmo ML | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | side margin -1 |  |
| R3 | Under 5.5 goals | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | total 3 vs 5.5: -2.5 |  |
| NOT_PREF | Over 5.5 goals | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | total 3 vs 5.5: -2.5 |  |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_SIDE Vaxjo +1.5 (NOT_ESTIMATED) WIN; TOP_TOTAL Under 5.5 goals (NOT_ESTIMATED) WIN; RANK1 Vaxjo +1.5 (NOT_ESTIMATED) WIN. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** Växjö 2-1 Malmö (at Malmö); Nadeau scored both Växjö goals; period scores and regulation/OT NOT_VERIFIED. Identity matched on participants, date and competition (SHL 2026-27).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Hockey rows: every grade is the same under 60-minute, full-game and shootout-credited conventions, except where marked.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final Malmö minus Växjö = -1; total 3. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** Växjö won 2-1 away with Nadeau scoring twice. Malmö ML lost and Växjö +1.5 won under any OT/SO convention; three goals stayed under 5.5 under any convention.
**R9. Source/timing review.** Settlement sources: https://www.tvmatchen.nu/sport/ishockey/shl-resultat-14-november-2026/ (ALLOWED). Card timing `POST_SCHEDULED_START_WRITE`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-20261114CHAT2988664A-G0009 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-20261114EA6B2758F0-G0008 revision-1 -->
### Settlement · `LOCAL-20261114EA6B2758F0-G0008` · IF Malmö Redhawks v Växjö Lakers HC · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `567b703336fa9674050135fed4bdd72fabdc3b18adb26e8cdcf2d7a0ddcbd122`, 13187 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/20261114EA6B2758F0.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `POST_SCHEDULED_START_WRITE` (last recorded `2026-11-15T01:21:50+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| R1 | Vaxjo +1.5 | 0.65517 (chat-local uncalibrated scenario) | **WIN** | side margin +1, handicap +1.5: +2.5 | 0.118908 |
| R2 | Malmo ML | 0.59793 (chat-local uncalibrated scenario) | **LOSS** | side margin -1 | 0.357520 |
| R3 | Under 5.5 goals | 0.51186 (chat-local uncalibrated scenario) | **WIN** | total 3 vs 5.5: -2.5 | 0.238281 |
| R4 | Over 5.5 goals | 0.48814 (chat-local uncalibrated scenario) | **LOSS** | total 3 vs 5.5: -2.5 | 0.238281 |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_SIDE Vaxjo +1.5 (0.65517) WIN; TOP_TOTAL Under 5.5 goals (0.51186) WIN; RANK1 Vaxjo +1.5 (0.65517) WIN. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** Växjö 2-1 Malmö (at Malmö); Nadeau scored both Växjö goals; period scores and regulation/OT NOT_VERIFIED. Identity matched on participants, date and competition (SHL 2026-27).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Hockey rows: every grade is the same under 60-minute, full-game and shootout-credited conventions, except where marked.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final Malmö minus Växjö = -1; total 3. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** Växjö won 2-1 away with Nadeau scoring twice. Malmö ML lost and Växjö +1.5 won under any OT/SO convention; three goals stayed under 5.5 under any convention.
**R9. Source/timing review.** Settlement sources: https://www.tvmatchen.nu/sport/ishockey/shl-resultat-14-november-2026/ (ALLOWED). Card timing `POST_SCHEDULED_START_WRITE`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-20261114EA6B2758F0-G0008 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-CHAT20261114DDA525E495-G0009 revision-1 -->
### Settlement · `LOCAL-CHAT20261114DDA525E495-G0009` · IF Malmö Redhawks v Växjö Lakers HC · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `238f443ce7f5360749839a6fa3ee3327f7f0ecbbeafa0361ab61bb464efb1af0`, 13440 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/CHAT20261114DDA525E495.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `POST_SCHEDULED_START_WRITE` (last recorded `2026-11-15T01:16:49+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| D1 | Malmo ML | 0.6295 (chat-local uncalibrated scenario) | **LOSS** | side margin -1 | 0.396270 |
| D2 | Vaxjo +1.5 | 0.6242 (chat-local uncalibrated scenario) | **WIN** | side margin +1, handicap +1.5: +2.5 | 0.141226 |
| NO_DIRECTION | Under 5.5 goals | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | total 3 vs 5.5: -2.5 |  |
| NO_DIRECTION | Over 5.5 goals | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | total 3 vs 5.5: -2.5 |  |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_SIDE Malmo ML (0.6295) LOSS; RANK1 Malmo ML (0.6295) LOSS. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** Växjö 2-1 Malmö (at Malmö); Nadeau scored both Växjö goals; period scores and regulation/OT NOT_VERIFIED. Identity matched on participants, date and competition (SHL 2026-27).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Hockey rows: every grade is the same under 60-minute, full-game and shootout-credited conventions, except where marked.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final Malmö minus Växjö = -1; total 3. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** Växjö won 2-1 away with Nadeau scoring twice. Malmö ML lost and Växjö +1.5 won under any OT/SO convention; three goals stayed under 5.5 under any convention.
**R9. Source/timing review.** Settlement sources: https://www.tvmatchen.nu/sport/ishockey/shl-resultat-14-november-2026/ (ALLOWED). Card timing `POST_SCHEDULED_START_WRITE`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-CHAT20261114DDA525E495-G0009 revision-1 -->

### Deep loss reviews (DEEPLOSS-v1)

#### Deep loss review · IF Malmö Redhawks v Växjö Lakers HC · Malmo ML

**1. Exact frozen claim.** `Malmo ML`, full-game endpoint as each card defined it. Triggered in 3 card(s):

| Card | Trigger role(s) | Original p (basis) | Brier | Log loss |
|---|---|---|---:|---:|
| `LOCAL-202611148C6C0822-G0009` | TOP_SIDE, RANK1 | NOT_ESTIMATED (qualitative (no numeric p)) |  |  |
| `LOCAL-20261114B4496A3F-G0009` | TOP_SIDE, RANK1 | 0.6695 (chat-local uncalibrated scenario) | 0.448230 | 1.107149 |
| `LOCAL-CHAT20261114DDA525E495-G0009` | TOP_SIDE, RANK1 | 0.6295 (chat-local uncalibrated scenario) | 0.396270 | 0.992902 |

No card carried a primary p_card, frozen reference or same-row baseline; BASELINE_P comparison NOT_COMPUTABLE.

**2. Verified outcome.** Växjö 2-1 Malmö (at Malmö) (Nadeau scored both Växjö goals; period scores and regulation/OT NOT_VERIFIED). side margin -1. Sources in R9; evidence C; final wall-clock NOT_VERIFIED.
**3. Distribution check.** Numeric cards priced this row at 0.629-0.669; a loss at those prices is a 33%-37% event under each card's own uncalibrated object.
**4. Error decomposition.** Realised distance: side margin -1. No card had a calibrated centre or a measured effect row, so the miss is not split into reference and adjustment error; no blame shares are invented.
**5. Research audit.** Three cards (B44 0.670, DDA 0.630, 8C6 qualitative) used Malmö's 4th v 11th standing, +9 v −9 goal difference and home ice. Växjö's 5-0 win two nights earlier and its 4-3 OT win in September were noted. Starting goalies were unconfirmed in every card.
**6. What decided the game.** Växjö won 2-1 away with Nadeau scoring twice. Malmö ML lost and Växjö +1.5 won under any OT/SO convention; three goals stayed under 5.5 under any convention.
**7. Knowable at cutoff?** Knowable: the standings gap and the unconfirmed goalies. Not knowable: Nadeau's two goals and a 2-1 road win.
**8. Process audit.** Chat-local record; no repository reference stage, no source-audit receipts, no lineup confirmation, no freeze. Timing per card in CARD_TIMING.csv.
**9. Verdict.** MODEL_LIMIT. A 60-67% favourite losing is a one-in-three event; the cards' covering pair (Växjö +1.5) won. No pre-game error identified, but certainty above 0.65 was not supported without goalie confirmation.
**10. Cutoff-only counterfactual.** NOT_ESTIMATED: no knowable fact has a measured effect-table row, so no corrected probability is priced after the result.
**11. Failure class and recurrence.** Shared across 3 cards on one game: overlapping public inputs make these one dependent observation, not 3.
**12. Correction.** NO_CHANGE to any rule from one result. Pattern-level proposals are in AUDIT_REPORT (PROPOSED_NOT_TESTED).
**13. Matched wins.** `LOCAL-202611148C6C0822-G0009` TOP_TOTAL Under 5.5 goals WIN; `LOCAL-20261114B4496A3F-G0009` TOP_TOTAL Under 5.5 goals WIN. These rest on the same unvalidated construction and do not show the process worked.
**14. Honesty.** Original numbers and labels preserved; no luck claim without the arithmetic above; no invented percentages, operator terms or publication times.

<!-- END SETTLEMENT EVENT E09 revision-1 -->

<!-- BEGIN SETTLEMENT EVENT E10 revision-1 -->
## Event · AEK Athens v Doxa Lefkadas ELABET · 2026-11-14 · Greece Stoiximan GBL 2026-27, round 7

**Final:** Doxa Lefkadas 77-73 AEK (at SUNEL Arena). **Periods:** Cumulative 13-27, 37-45, 59-60, 73-77 (AEK first); quarters AEK 13/24/22/14, Doxa 27/18/15/17; no OT. **Evidence B.** Scheduled 2026-11-14T15:00:00+00:00.

| Opened source | Audit | Field read |
|---|---|---|
| https://www.novasports.gr/sport/mpasket/event/basket-league/article/15230837/aek-doksa-leykadas-73-77-istoriki-niki-me-iroa-xarmon/ | ALLOWED | '73-77'; 'Δεκάλεπτα: 13-27, 37-45, 59-60, 73-77'; 14/11/2026 19:11 |
| https://www.enikos.gr/sports/gbl-itta-tis-aek-apo-ti-doxa-lefkadas-aittitos-o-paok-diplo-tou-irakli-stin-patra/2676763/ | ALLOWED | 77-73 Doxa; same quarter line; published 20:32 Saturday 14 November 2026 |

<!-- BEGIN SETTLEMENT LOCAL-20261114B4496A3F-G0010 revision-1 -->
### Settlement · `LOCAL-20261114B4496A3F-G0010` · AEK Athens v Doxa Lefkadas ELABET · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `6d55ace438d3813e7759ff282c03ba4567d70ac72824b414e65c2cf6930c630c`, 22793 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/20261114B4496A3F.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `POST_SCHEDULED_START_WRITE` (last recorded `2026-11-15T02:02:27+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| R1 | Doxa +7.5 | 0.6904 (chat-local uncalibrated scenario) | **WIN** | side margin +4, handicap +7.5: +11.5 | 0.095852 |
| R2 | Under 160.5 | 0.5507 (chat-local uncalibrated scenario) | **WIN** | total 150 vs 160.5: -10.5 | 0.201870 |
| INFO | Over 160.5 | 0.4493 (chat-local uncalibrated scenario) | **LOSS** | total 150 vs 160.5: -10.5 | 0.201870 |
| INFO | AEK -7.5 | 0.3096 (chat-local uncalibrated scenario) | **LOSS** | side margin -4, handicap -7.5: -11.5 | 0.095852 |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_SIDE Doxa +7.5 (0.6904) WIN; TOP_TOTAL Under 160.5 (0.5507) WIN; RANK1 Doxa +7.5 (0.6904) WIN. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** Doxa Lefkadas 77-73 AEK (at SUNEL Arena); Cumulative 13-27, 37-45, 59-60, 73-77 (AEK first); quarters AEK 13/24/22/14, Doxa 27/18/15/17; no OT. Identity matched on participants, date and competition (Greece Stoiximan GBL 2026-27, round 7).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Basketball rows include overtime (BK-OT-1); none occurred.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final AEK minus Doxa = -4; total 150. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** Doxa led 27-13 after one quarter and won 77-73 outright; Doxa +7.5 covered by 11.5. The total of 150 was 10.5 under 160.5.
**R9. Source/timing review.** Settlement sources: https://www.novasports.gr/sport/mpasket/event/basket-league/article/15230837/aek-doksa-leykadas-73-77-istoriki-niki-me-iroa-xarmon/ (ALLOWED); https://www.enikos.gr/sports/gbl-itta-tis-aek-apo-ti-doxa-lefkadas-aittitos-o-paok-diplo-tou-irakli-stin-patra/2676763/ (ALLOWED). Card timing `POST_SCHEDULED_START_WRITE`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-20261114B4496A3F-G0010 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-202611148A011BE83FCC-G0010 revision-1 -->
### Settlement · `LOCAL-202611148A011BE83FCC-G0010` · AEK Athens v Doxa Lefkadas ELABET · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `969c4186ffbb36d47cd360b13f171e309cccbde6bef33babf4faab447eb35e07`, 12844 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/202611148A011BE83FCC.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `PRE_SCHEDULED_START_WRITE` (last recorded `2026-11-15T01:58:27+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| NOT_PREF | AEK -7.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | side margin -4, handicap -7.5: -11.5 |  |
| R1 | Doxa +7.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | side margin +4, handicap +7.5: +11.5 |  |
| NOT_PREF | Over 160.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | total 150 vs 160.5: -10.5 |  |
| R2 | Under 160.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | total 150 vs 160.5: -10.5 |  |
| LEAN_WINNER | AEK to win | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | side margin -4 |  |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_SIDE Doxa +7.5 (NOT_ESTIMATED) WIN; TOP_TOTAL Under 160.5 (NOT_ESTIMATED) WIN; RANK1 Doxa +7.5 (NOT_ESTIMATED) WIN. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** Doxa Lefkadas 77-73 AEK (at SUNEL Arena); Cumulative 13-27, 37-45, 59-60, 73-77 (AEK first); quarters AEK 13/24/22/14, Doxa 27/18/15/17; no OT. Identity matched on participants, date and competition (Greece Stoiximan GBL 2026-27, round 7).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Basketball rows include overtime (BK-OT-1); none occurred.
**R4. Rank diagnostics.** 2W/3L/0U over 5 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final AEK minus Doxa = -4; total 150. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** Doxa led 27-13 after one quarter and won 77-73 outright; Doxa +7.5 covered by 11.5. The total of 150 was 10.5 under 160.5.
**R9. Source/timing review.** Settlement sources: https://www.novasports.gr/sport/mpasket/event/basket-league/article/15230837/aek-doksa-leykadas-73-77-istoriki-niki-me-iroa-xarmon/ (ALLOWED); https://www.enikos.gr/sports/gbl-itta-tis-aek-apo-ti-doxa-lefkadas-aittitos-o-paok-diplo-tou-irakli-stin-patra/2676763/ (ALLOWED). Card timing `PRE_SCHEDULED_START_WRITE`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-202611148A011BE83FCC-G0010 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-202611148C6C0822-G0010 revision-1 -->
### Settlement · `LOCAL-202611148C6C0822-G0010` · AEK Athens v Doxa Lefkadas ELABET · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `aebff917583fa6086360ae115bd791567b0b813938e1ddc4b22d1e1295942d14`, 8881 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/202611148C6C0822.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `PRE_SCHEDULED_START_WRITE` (last recorded `2026-11-15T01:57:24+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| R1 | Doxa +7.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | side margin +4, handicap +7.5: +11.5 |  |
| R2 | Under 160.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | total 150 vs 160.5: -10.5 |  |
| R3 | Over 160.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | total 150 vs 160.5: -10.5 |  |
| NOT_PREF | AEK -7.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | side margin -4, handicap -7.5: -11.5 |  |
| LEAN_WINNER | AEK to win | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | side margin -4 |  |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_SIDE Doxa +7.5 (NOT_ESTIMATED) WIN; TOP_TOTAL Under 160.5 (NOT_ESTIMATED) WIN; RANK1 Doxa +7.5 (NOT_ESTIMATED) WIN. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** Doxa Lefkadas 77-73 AEK (at SUNEL Arena); Cumulative 13-27, 37-45, 59-60, 73-77 (AEK first); quarters AEK 13/24/22/14, Doxa 27/18/15/17; no OT. Identity matched on participants, date and competition (Greece Stoiximan GBL 2026-27, round 7).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Basketball rows include overtime (BK-OT-1); none occurred.
**R4. Rank diagnostics.** 2W/3L/0U over 5 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final AEK minus Doxa = -4; total 150. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** Doxa led 27-13 after one quarter and won 77-73 outright; Doxa +7.5 covered by 11.5. The total of 150 was 10.5 under 160.5.
**R9. Source/timing review.** Settlement sources: https://www.novasports.gr/sport/mpasket/event/basket-league/article/15230837/aek-doksa-leykadas-73-77-istoriki-niki-me-iroa-xarmon/ (ALLOWED); https://www.enikos.gr/sports/gbl-itta-tis-aek-apo-ti-doxa-lefkadas-aittitos-o-paok-diplo-tou-irakli-stin-patra/2676763/ (ALLOWED). Card timing `PRE_SCHEDULED_START_WRITE`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-202611148C6C0822-G0010 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-20261114CHAT2988664A-G0010 revision-1 -->
### Settlement · `LOCAL-20261114CHAT2988664A-G0010` · AEK Athens v Doxa Lefkadas ELABET · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `3c97c74472e1d23d012bbbc571f89bddbe441b50d48b1ee27a1479a8348b2287`, 11888 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/20261114CHAT2988664A.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `PRE_SCHEDULED_START_WRITE` (last recorded `2026-11-15T01:58:28+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| NOT_PREF | AEK -7.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | side margin -4, handicap -7.5: -11.5 |  |
| R1 | Doxa +7.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | side margin +4, handicap +7.5: +11.5 |  |
| NOT_PREF | Over 160.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | total 150 vs 160.5: -10.5 |  |
| R2 | Under 160.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | total 150 vs 160.5: -10.5 |  |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_SIDE Doxa +7.5 (NOT_ESTIMATED) WIN; TOP_TOTAL Under 160.5 (NOT_ESTIMATED) WIN; RANK1 Doxa +7.5 (NOT_ESTIMATED) WIN. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** Doxa Lefkadas 77-73 AEK (at SUNEL Arena); Cumulative 13-27, 37-45, 59-60, 73-77 (AEK first); quarters AEK 13/24/22/14, Doxa 27/18/15/17; no OT. Identity matched on participants, date and competition (Greece Stoiximan GBL 2026-27, round 7).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Basketball rows include overtime (BK-OT-1); none occurred.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final AEK minus Doxa = -4; total 150. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** Doxa led 27-13 after one quarter and won 77-73 outright; Doxa +7.5 covered by 11.5. The total of 150 was 10.5 under 160.5.
**R9. Source/timing review.** Settlement sources: https://www.novasports.gr/sport/mpasket/event/basket-league/article/15230837/aek-doksa-leykadas-73-77-istoriki-niki-me-iroa-xarmon/ (ALLOWED); https://www.enikos.gr/sports/gbl-itta-tis-aek-apo-ti-doxa-lefkadas-aittitos-o-paok-diplo-tou-irakli-stin-patra/2676763/ (ALLOWED). Card timing `PRE_SCHEDULED_START_WRITE`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-20261114CHAT2988664A-G0010 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-20261114EA6B2758F0-G0009 revision-1 -->
### Settlement · `LOCAL-20261114EA6B2758F0-G0009` · AEK Athens v Doxa Lefkadas ELABET · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `3b2f566f91351cc8f0c4d81d3e4963a300bee962fc66cf492952892118f29a4a`, 12604 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/20261114EA6B2758F0.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `WRITE_TIME_NOT_RECORDED` (last recorded `NOT_RECORDED`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| R1 | Doxa +7.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | side margin +4, handicap +7.5: +11.5 |  |
| NOT_PREF | AEK -7.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | side margin -4, handicap -7.5: -11.5 |  |
| R2 | Under 160.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | total 150 vs 160.5: -10.5 |  |
| ALT | Over 160.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | total 150 vs 160.5: -10.5 |  |
| LEAN_WINNER | AEK to win | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | side margin -4 |  |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_SIDE Doxa +7.5 (NOT_ESTIMATED) WIN; TOP_TOTAL Under 160.5 (NOT_ESTIMATED) WIN; RANK1 Doxa +7.5 (NOT_ESTIMATED) WIN. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** Doxa Lefkadas 77-73 AEK (at SUNEL Arena); Cumulative 13-27, 37-45, 59-60, 73-77 (AEK first); quarters AEK 13/24/22/14, Doxa 27/18/15/17; no OT. Identity matched on participants, date and competition (Greece Stoiximan GBL 2026-27, round 7).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Basketball rows include overtime (BK-OT-1); none occurred.
**R4. Rank diagnostics.** 2W/3L/0U over 5 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final AEK minus Doxa = -4; total 150. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** Doxa led 27-13 after one quarter and won 77-73 outright; Doxa +7.5 covered by 11.5. The total of 150 was 10.5 under 160.5.
**R9. Source/timing review.** Settlement sources: https://www.novasports.gr/sport/mpasket/event/basket-league/article/15230837/aek-doksa-leykadas-73-77-istoriki-niki-me-iroa-xarmon/ (ALLOWED); https://www.enikos.gr/sports/gbl-itta-tis-aek-apo-ti-doxa-lefkadas-aittitos-o-paok-diplo-tou-irakli-stin-patra/2676763/ (ALLOWED). Card timing `WRITE_TIME_NOT_RECORDED`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-20261114EA6B2758F0-G0009 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-CHAT20261114DDA525E495-G0010 revision-1 -->
### Settlement · `LOCAL-CHAT20261114DDA525E495-G0010` · AEK Athens v Doxa Lefkadas ELABET · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `e6d7cf07c21931f1561de264bb8c352880b05966292e9bb3e79885730d875c10`, 14262 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/CHAT20261114DDA525E495.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `POST_SCHEDULED_START_WRITE` (last recorded `2026-11-15T02:01:17+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| D1 | Doxa +7.5 | 0.6758 (chat-local uncalibrated scenario) | **WIN** | side margin +4, handicap +7.5: +11.5 | 0.105106 |
| NOT_RANKED | AEK -7.5 | 0.3242 (chat-local uncalibrated scenario) | **LOSS** | side margin -4, handicap -7.5: -11.5 | 0.105106 |
| D2 | Under 160.5 | 0.5866 (chat-local uncalibrated scenario) | **WIN** | total 150 vs 160.5: -10.5 | 0.170900 |
| NOT_RANKED | Over 160.5 | 0.4134 (chat-local uncalibrated scenario) | **LOSS** | total 150 vs 160.5: -10.5 | 0.170900 |
| INFO | AEK to win | 0.5096 (chat-local uncalibrated scenario) | **LOSS** | side margin -4 | 0.259692 |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_SIDE Doxa +7.5 (0.6758) WIN; TOP_TOTAL Under 160.5 (0.5866) WIN; RANK1 Doxa +7.5 (0.6758) WIN. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** Doxa Lefkadas 77-73 AEK (at SUNEL Arena); Cumulative 13-27, 37-45, 59-60, 73-77 (AEK first); quarters AEK 13/24/22/14, Doxa 27/18/15/17; no OT. Identity matched on participants, date and competition (Greece Stoiximan GBL 2026-27, round 7).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Basketball rows include overtime (BK-OT-1); none occurred.
**R4. Rank diagnostics.** 2W/3L/0U over 5 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final AEK minus Doxa = -4; total 150. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** Doxa led 27-13 after one quarter and won 77-73 outright; Doxa +7.5 covered by 11.5. The total of 150 was 10.5 under 160.5.
**R9. Source/timing review.** Settlement sources: https://www.novasports.gr/sport/mpasket/event/basket-league/article/15230837/aek-doksa-leykadas-73-77-istoriki-niki-me-iroa-xarmon/ (ALLOWED); https://www.enikos.gr/sports/gbl-itta-tis-aek-apo-ti-doxa-lefkadas-aittitos-o-paok-diplo-tou-irakli-stin-patra/2676763/ (ALLOWED). Card timing `POST_SCHEDULED_START_WRITE`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-CHAT20261114DDA525E495-G0010 revision-1 -->

<!-- END SETTLEMENT EVENT E10 revision-1 -->

<!-- BEGIN SETTLEMENT EVENT E11 revision-1 -->
## Event · Norway v Wales · 2026-11-14 · UEFA Nations League 2026-27 League A Group A4

**Final:** Norway 3-1 Wales. **Periods:** HT 0-0 (derived: goals 59' Nusa, about 68' Schjelderup, 79' Brooks, 88' Haaland pen); corners Norway 8, Wales 2 (10). **Evidence B.** Scheduled 2026-11-14T17:00:00+00:00. Note: Corner count single-lineage (hoofoot); Sofascore and FootyStats RULES_UNKNOWN, VAVEL and Sky BLOCKED_FOR_AI.

| Opened source | Audit | Field read |
|---|---|---|
| https://www.beinsports.com/en-us/soccer/uefa-nations-league/articles/norway-3-1-wales-haaland-keeps-quarter-final-hopes-alive-2026-11-14 | ALLOWED | '3-1 victory'; Nusa 59th, Schjelderup 'nine minutes later', Brooks '79 minutes in', Haaland penalty 88th |
| https://hoofoot.net/full-matches/uefa-nations-league/norway-vs-wales-highlights-november-14-2026/ | ALLOWED | 'Full Time' 3:1; 'Corners: Norway 8, Wales 2.' |

<!-- BEGIN SETTLEMENT LOCAL-20261115CHAT48A8D395742B-G0001 revision-1 -->
### Settlement · `LOCAL-20261115CHAT48A8D395742B-G0001` · Norway v Wales · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `1b2c319afe4dc00b219e0ab84d42e7bc50529f696c39685ebc50a291f057c921`, 23590 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/20261115CHAT48A8D395742B.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `PRE_SCHEDULED_START_WRITE` (last recorded `2026-11-15T03:56:04+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| R1 | First half Over 0.5 goals | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | first-half goals 0 vs 0.5: -0.5 |  |
| DISFAVOURED | First half Under 0.5 goals | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | first-half goals 0 vs 0.5: -0.5 |  |
| MIXED | Over 2.5 goals | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | total 4 vs 2.5: +1.5 |  |
| MIXED | Under 2.5 goals | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | total 4 vs 2.5: +1.5 |  |
| R2 | Corners Under 10.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | corners 10 vs 10.5: -0.5 |  |
| DISFAVOURED | Corners Over 10.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | corners 10 vs 10.5: -0.5 |  |
| LEAN_WINNER | Norway to win | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | side margin +2 |  |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_SIDE Norway to win (NOT_ESTIMATED) WIN; TOP_TOTAL Corners Under 10.5 (NOT_ESTIMATED) WIN; RANK1 First half Over 0.5 goals (NOT_ESTIMATED) LOSS. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** Norway 3-1 Wales; HT 0-0 (derived: goals 59' Nusa, about 68' Schjelderup, 79' Brooks, 88' Haaland pen); corners Norway 8, Wales 2 (10). Identity matched on participants, date and competition (UEFA Nations League 2026-27 League A Group A4).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Soccer rows: 90 minutes plus stoppage; first half 45 plus stoppage.
**R4. Rank diagnostics.** 4W/3L/0U over 7 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final Norway minus Wales = 2; total 4. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** Wales had the better first half and it ended 0-0; Norway scored three times after the hour. Four goals beat 2.5; ten corners stayed under 10.5 (corners rest on one permitted page).
**R9. Source/timing review.** Settlement sources: https://www.beinsports.com/en-us/soccer/uefa-nations-league/articles/norway-3-1-wales-haaland-keeps-quarter-final-hopes-alive-2026-11-14 (ALLOWED); https://hoofoot.net/full-matches/uefa-nations-league/norway-vs-wales-highlights-november-14-2026/ (ALLOWED). Card timing `PRE_SCHEDULED_START_WRITE`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-20261115CHAT48A8D395742B-G0001 revision-1 -->

### Deep loss reviews (DEEPLOSS-v1)

#### Deep loss review · Norway v Wales · First half Over 0.5 goals

**1. Exact frozen claim.** `First half Over 0.5 goals`, full-game endpoint as each card defined it. Triggered in 1 card(s):

| Card | Trigger role(s) | Original p (basis) | Brier | Log loss |
|---|---|---|---:|---:|
| `LOCAL-20261115CHAT48A8D395742B-G0001` | RANK1 | NOT_ESTIMATED (qualitative (no numeric p)) |  |  |

No card carried a primary p_card, frozen reference or same-row baseline; BASELINE_P comparison NOT_COMPUTABLE.

**2. Verified outcome.** Norway 3-1 Wales (HT 0-0 (derived: goals 59' Nusa, about 68' Schjelderup, 79' Brooks, 88' Haaland pen); corners Norway 8, Wales 2 (10)). first-half goals 0 vs 0.5: -0.5. Sources in R9; evidence B; final wall-clock NOT_VERIFIED.
**3. Distribution check.** Every triggering card was qualitative, so there is no frozen distribution to place the result in.
**4. Error decomposition.** Realised distance: first-half goals 0 vs 0.5: -0.5. No card had a calibrated centre or a measured effect row, so the miss is not split into reference and adjustment error; no blame shares are invented.
**5. Research audit.** The card used Norway's 4/4 Nations League first halves with a goal and 5/7 unique fixtures; it flagged Wales' two goalless first halves against Denmark.
**6. What decided the game.** Wales had the better first half and it ended 0-0; Norway scored three times after the hour. Four goals beat 2.5; ten corners stayed under 10.5 (corners rest on one permitted page).
**7. Knowable at cutoff?** Knowable: the small sample. Not knowable: Wales having the better first half and all four goals coming after 59 minutes.
**8. Process audit.** Chat-local record; no repository reference stage, no source-audit receipts, no lineup confirmation, no freeze. Timing per card in CARD_TIMING.csv.
**9. Verdict.** VARIANCE on thin evidence. Seven fixtures are too few to support a first-half lean; the card's own label was 'qualitative'. The full-time Over 2.5 and corners Under 10.5 rows won.
**10. Cutoff-only counterfactual.** NOT_ESTIMATED: no knowable fact has a measured effect-table row, so no corrected probability is priced after the result.
**11. Failure class and recurrence.** Single card.
**12. Correction.** NO_CHANGE to any rule from one result. Pattern-level proposals are in AUDIT_REPORT (PROPOSED_NOT_TESTED).
**13. Matched wins.** `LOCAL-20261115CHAT48A8D395742B-G0001` TOP_SIDE Norway to win WIN; `LOCAL-20261115CHAT48A8D395742B-G0001` TOP_TOTAL Corners Under 10.5 WIN. These rest on the same unvalidated construction and do not show the process worked.
**14. Honesty.** Original numbers and labels preserved; no luck claim without the arithmetic above; no invented percentages, operator terms or publication times.

<!-- END SETTLEMENT EVENT E11 revision-1 -->

<!-- BEGIN SETTLEMENT EVENT E12 revision-1 -->
## Event · Georgia Tech @ Clemson · 2026-11-14 ET · NCAA FBS 2026, ACC

**Final:** Georgia Tech 20-6 Clemson. **Periods:** Derived from narrative: GT 7-6-7-0, CLE 0-3-3-0; half 13-3; no OT. **Evidence B.** Scheduled 2026-11-14T17:30:00+00:00.

| Opened source | Audit | Field read |
|---|---|---|
| https://ramblinwreck.com/news/2026/11/14/fb-recap-clemson-26 | ALLOWED | 'defeating Clemson, 20-6' |
| https://clemsontigers.com/news/2026/11/14/georgia-tech-defeats-clemson-20-6 | ALLOWED | 'defeated Clemson (6-4, 4-3 ACC), 20-6'; 13-3 at half; scoreless fourth quarter |

<!-- BEGIN SETTLEMENT LOCAL-20261115CHAT48A8D395742B-G0002 revision-1 -->
### Settlement · `LOCAL-20261115CHAT48A8D395742B-G0002` · Georgia Tech @ Clemson · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `62be623a6cd4fd5752f065948ef87832e42b0fa9b346a0ba6ffb98fd56b967a6`, 24943 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/20261115CHAT48A8D395742B.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `POST_SCHEDULED_START_WRITE` (last recorded `2026-11-15T04:31:23+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| R1 | Clemson +15.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | side margin -14, handicap +15.5: +1.5 |  |
| OPPOSED | Georgia Tech -15.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | side margin +14, handicap -15.5: -1.5 |  |
| R2 | Over 47.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | total 26 vs 47.5: -21.5 |  |
| ALT | Under 47.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | total 26 vs 47.5: -21.5 |  |
| LEAN_WINNER | Clemson to win | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | side margin -14 |  |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_SIDE Clemson +15.5 (NOT_ESTIMATED) WIN; TOP_TOTAL Over 47.5 (NOT_ESTIMATED) LOSS; RANK1 Clemson +15.5 (NOT_ESTIMATED) WIN. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** Georgia Tech 20-6 Clemson; Derived from narrative: GT 7-6-7-0, CLE 0-3-3-0; half 13-3; no OT. Identity matched on participants, date and competition (NCAA FBS 2026, ACC).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Football rows include any overtime; none occurred.
**R4. Rank diagnostics.** 2W/3L/0U over 5 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final Georgia Tech minus Clemson = 14; total 26. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** Georgia Tech led 13-3 at half and 20-3 early in the third; a scoreless fourth left 26 points, 21.5 under 47.5. A 14-point win failed the literal Georgia Tech -15.5 and kept Clemson +15.5 alive by 1.5.
**R9. Source/timing review.** Settlement sources: https://ramblinwreck.com/news/2026/11/14/fb-recap-clemson-26 (ALLOWED); https://clemsontigers.com/news/2026/11/14/georgia-tech-defeats-clemson-20-6 (ALLOWED). Card timing `POST_SCHEDULED_START_WRITE`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-20261115CHAT48A8D395742B-G0002 revision-1 -->

### Deep loss reviews (DEEPLOSS-v1)

#### Deep loss review · Georgia Tech @ Clemson · Over 47.5

**1. Exact frozen claim.** `Over 47.5`, full-game endpoint as each card defined it. Triggered in 1 card(s):

| Card | Trigger role(s) | Original p (basis) | Brier | Log loss |
|---|---|---|---:|---:|
| `LOCAL-20261115CHAT48A8D395742B-G0002` | TOP_TOTAL | NOT_ESTIMATED (qualitative (no numeric p)) |  |  |

No card carried a primary p_card, frozen reference or same-row baseline; BASELINE_P comparison NOT_COMPUTABLE.

**2. Verified outcome.** Georgia Tech 20-6 Clemson (Derived from narrative: GT 7-6-7-0, CLE 0-3-3-0; half 13-3; no OT). total 26 vs 47.5: -21.5. Sources in R9; evidence B; final wall-clock NOT_VERIFIED.
**3. Distribution check.** Every triggering card was qualitative, so there is no frozen distribution to place the result in.
**4. Error decomposition.** Realised distance: total 26 vs 47.5: -21.5. No card had a calibrated centre or a measured effect row, so the miss is not split into reference and adjustment error; no blame shares are invented.
**5. Research audit.** The card leaned Over on Georgia Tech's 7/9 season overs, while noting Clemson's 22.7 points per game and 'significant skill/OL absences' and an 18-13 game the week before.
**6. What decided the game.** Georgia Tech led 13-3 at half and 20-3 early in the third; a scoreless fourth left 26 points, 21.5 under 47.5. A 14-point win failed the literal Georgia Tech -15.5 and kept Clemson +15.5 alive by 1.5.
**7. Knowable at cutoff?** Knowable: Clemson's offensive absences, which the card itself listed. Not knowable: the in-game course (a 13-3 half and a scoreless fourth).
**8. Process audit.** Chat-local record; no repository reference stage, no source-audit receipts, no lineup confirmation, no freeze. Timing per card in CARD_TIMING.csv.
**9. Verdict.** ERROR (lean against the card's own absence evidence). The card called it 'slight/low-confidence'; it should have been no direction. Its rank-1 Clemson +15.5 won.
**10. Cutoff-only counterfactual.** NOT_ESTIMATED: no knowable fact has a measured effect-table row, so no corrected probability is priced after the result.
**11. Failure class and recurrence.** Single card.
**12. Correction.** NO_CHANGE to any rule from one result. Pattern-level proposals are in AUDIT_REPORT (PROPOSED_NOT_TESTED).
**13. Matched wins.** `LOCAL-20261115CHAT48A8D395742B-G0002` RANK1 Clemson +15.5 WIN; `LOCAL-20261115CHAT48A8D395742B-G0002` TOP_SIDE Clemson +15.5 WIN. These rest on the same unvalidated construction and do not show the process worked.
**14. Honesty.** Original numbers and labels preserved; no luck claim without the arithmetic above; no invented percentages, operator terms or publication times.

<!-- END SETTLEMENT EVENT E12 revision-1 -->

<!-- BEGIN SETTLEMENT EVENT E13 revision-1 -->
## Event · Alabama @ Vanderbilt · 2026-11-14 CT · NCAA FBS 2026, SEC

**Final:** Alabama 21-6 Vanderbilt. **Periods:** Quarter scoring NOT_VERIFIED from an opened page; no OT indicated. **Evidence C.** Scheduled 2026-11-14T17:45:00+00:00. Note: Only the page title was returned; ESPN and Yahoo BLOCKED_FOR_AI. Who started at quarterback for Alabama is NOT_VERIFIED from an opened page.

| Opened source | Audit | Field read |
|---|---|---|
| https://rolltide.com/news/2026/11/14/football-no-3-7-7-alabama-takes-down-vanderbilt-21-6 | ALLOWED | Title only returned: 'No. 3/7/7 Alabama Takes Down Vanderbilt, 21-6' |

<!-- BEGIN SETTLEMENT LOCAL-20261115CHAT48A8D395742B-G0003 revision-1 -->
### Settlement · `LOCAL-20261115CHAT48A8D395742B-G0003` · Alabama @ Vanderbilt · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `58b0311b3ae1aa18ff1fb81408de00b1393f9788de9e125d3c176507cb9a0564`, 21691 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/20261115CHAT48A8D395742B.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `PRE_SCHEDULED_START_WRITE` (last recorded `2026-11-15T04:43:58+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| NOT_PREF | Alabama -14.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | side margin +15, handicap -14.5: +0.5 |  |
| R1 | Vanderbilt +14.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | side margin -15, handicap +14.5: -0.5 |  |
| ALT | Over 48.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | total 27 vs 48.5: -21.5 |  |
| R2 | Under 48.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | total 27 vs 48.5: -21.5 |  |
| LEAN_WINNER | Alabama to win | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | side margin +15 |  |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_SIDE Vanderbilt +14.5 (NOT_ESTIMATED) LOSS; TOP_TOTAL Under 48.5 (NOT_ESTIMATED) WIN; RANK1 Vanderbilt +14.5 (NOT_ESTIMATED) LOSS. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** Alabama 21-6 Vanderbilt; Quarter scoring NOT_VERIFIED from an opened page; no OT indicated. Identity matched on participants, date and competition (NCAA FBS 2026, SEC).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Football rows include any overtime; none occurred.
**R4. Rank diagnostics.** 3W/2L/0U over 5 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final Alabama minus Vanderbilt = 15; total 27. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** A 15-point Alabama win beat Alabama -14.5 by half a point and failed Vanderbilt +14.5 by half a point; 27 points stayed 21.5 under 48.5.
**R9. Source/timing review.** Settlement sources: https://rolltide.com/news/2026/11/14/football-no-3-7-7-alabama-takes-down-vanderbilt-21-6 (ALLOWED). Card timing `PRE_SCHEDULED_START_WRITE`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-20261115CHAT48A8D395742B-G0003 revision-1 -->

### Deep loss reviews (DEEPLOSS-v1)

#### Deep loss review · Alabama @ Vanderbilt · Vanderbilt +14.5

**1. Exact frozen claim.** `Vanderbilt +14.5`, full-game endpoint as each card defined it. Triggered in 1 card(s):

| Card | Trigger role(s) | Original p (basis) | Brier | Log loss |
|---|---|---|---:|---:|
| `LOCAL-20261115CHAT48A8D395742B-G0003` | TOP_SIDE, RANK1 | NOT_ESTIMATED (qualitative (no numeric p)) |  |  |

No card carried a primary p_card, frozen reference or same-row baseline; BASELINE_P comparison NOT_COMPUTABLE.

**2. Verified outcome.** Alabama 21-6 Vanderbilt (Quarter scoring NOT_VERIFIED from an opened page; no OT indicated). side margin -15, handicap +14.5: -0.5. Sources in R9; evidence C; final wall-clock NOT_VERIFIED.
**3. Distribution check.** Every triggering card was qualitative, so there is no frozen distribution to place the result in.
**4. Error decomposition.** Realised distance: side margin -15, handicap +14.5: -0.5. No card had a calibrated centre or a measured effect row, so the miss is not split into reference and adjustment error; no blame shares are invented.
**5. Research audit.** The card's thesis was Alabama switching from Russell to backup Mack, taken from a Friday secondary report (Yahoo, BLOCKED_FOR_AI under this audit, opened by the chat). Who actually started is NOT_VERIFIED from an opened page here.
**6. What decided the game.** A 15-point Alabama win beat Alabama -14.5 by half a point and failed Vanderbilt +14.5 by half a point; 27 points stayed 21.5 under 48.5.
**7. Knowable at cutoff?** Knowable at cutoff: only the secondary injury report; no official depth chart was cited. Not knowable: the final 15-point margin.
**8. Process audit.** Chat-local record; no repository reference stage, no source-audit receipts, no lineup confirmation, no freeze. Timing per card in CARD_TIMING.csv.
**9. Verdict.** MIXED. Lost by half a point; the key premise came from a single unofficial report and was not confirmed, which is an unmeasured availability effect the card priced qualitatively. Under AUDIT-v1 it should have been UNPRICED with the QB scenario kept as a sensitivity.
**10. Cutoff-only counterfactual.** NOT_ESTIMATED: no knowable fact has a measured effect-table row, so no corrected probability is priced after the result.
**11. Failure class and recurrence.** Single card.
**12. Correction.** NO_CHANGE to any rule from one result. Pattern-level proposals are in AUDIT_REPORT (PROPOSED_NOT_TESTED).
**13. Matched wins.** `LOCAL-20261115CHAT48A8D395742B-G0003` TOP_TOTAL Under 48.5 WIN. These rest on the same unvalidated construction and do not show the process worked.
**14. Honesty.** Original numbers and labels preserved; no luck claim without the arithmetic above; no invented percentages, operator terms or publication times.

<!-- END SETTLEMENT EVENT E13 revision-1 -->

<!-- BEGIN SETTLEMENT EVENT E14 revision-1 -->
## Event · Laval Rocket @ Rochester Americans · 2026-11-14 ET · AHL 2026-27

**Final:** Rochester 5-4 Laval (OT); 4-4 after regulation. **Periods:** ROC 1-2-1-1, LAV 1-1-2-0; Kuntar 2:13 of OT; no shootout. **Evidence C.** Scheduled 2026-11-14T22:05:00+00:00. Note: Both pages are the same collector (Rochester club); Elite Prospects returned 403.

| Opened source | Audit | Field read |
|---|---|---|
| https://www.amerks.com/ | ALLOWED | Game Center: ROC 1,2,1,1 = 5 'F OT'; LAV 1,1,2,0 = 4 |
| https://www.amerks.com/news/detail/amerks-rally-in-third-top-rocket-in-overtime-thriller | ALLOWED | 'game-winner from Trevor Kuntar 2:13 into overtime' |

<!-- BEGIN SETTLEMENT LOCAL-20261115CHAT48A8D395742B-G0004 revision-1 -->
### Settlement · `LOCAL-20261115CHAT48A8D395742B-G0004` · Laval Rocket @ Rochester Americans · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `511fa0799ed0c3de6d90062e7991d2e057fad979226dca10f515e68fccb0ce67`, 24125 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/20261115CHAT48A8D395742B.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `POST_SCHEDULED_START_WRITE` (last recorded `2026-11-15T09:06:45+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| R1 | Laval ML | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | side margin -1 |  |
| ALT | Rochester ML | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | side margin +1 |  |
| MARGINAL | Over 5.5 goals | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | total 9 vs 5.5: +3.5 |  |
| ALT | Under 5.5 goals | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | total 9 vs 5.5: +3.5 |  |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_SIDE Laval ML (NOT_ESTIMATED) LOSS; TOP_TOTAL Over 5.5 goals (NOT_ESTIMATED) WIN; RANK1 Laval ML (NOT_ESTIMATED) LOSS. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** Rochester 5-4 Laval (OT); 4-4 after regulation; ROC 1-2-1-1, LAV 1-1-2-0; Kuntar 2:13 of OT; no shootout. Identity matched on participants, date and competition (AHL 2026-27).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Hockey rows: every grade is the same under 60-minute, full-game and shootout-credited conventions, except where marked.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final Laval minus Rochester (incl. OT) = -1; total 9. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** Tied 4-4 after regulation, Rochester won 2:13 into overtime. Laval ML lost; eight regulation goals (nine with OT) beat 5.5 under either convention.
**R9. Source/timing review.** Settlement sources: https://www.amerks.com/ (ALLOWED); https://www.amerks.com/news/detail/amerks-rally-in-third-top-rocket-in-overtime-thriller (ALLOWED). Card timing `POST_SCHEDULED_START_WRITE`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-20261115CHAT48A8D395742B-G0004 revision-1 -->

### Deep loss reviews (DEEPLOSS-v1)

#### Deep loss review · Laval Rocket @ Rochester Americans · Laval ML

**1. Exact frozen claim.** `Laval ML`, full-game endpoint as each card defined it. Triggered in 1 card(s):

| Card | Trigger role(s) | Original p (basis) | Brier | Log loss |
|---|---|---|---:|---:|
| `LOCAL-20261115CHAT48A8D395742B-G0004` | TOP_SIDE, RANK1 | NOT_ESTIMATED (qualitative (no numeric p)) |  |  |

No card carried a primary p_card, frozen reference or same-row baseline; BASELINE_P comparison NOT_COMPUTABLE.

**2. Verified outcome.** Rochester 5-4 Laval (OT); 4-4 after regulation (ROC 1-2-1-1, LAV 1-1-2-0; Kuntar 2:13 of OT; no shootout). side margin -1. Sources in R9; evidence C; final wall-clock NOT_VERIFIED.
**3. Distribution check.** Every triggering card was qualitative, so there is no frozen distribution to place the result in.
**4. Error decomposition.** Realised distance: side margin -1. No card had a calibrated centre or a measured effect row, so the miss is not split into reference and adjustment error; no blame shares are invented.
**5. Research audit.** The card used Laval's 12-4 record, 18-5 goals over four games and the 3-1 win the night before. Rochester's home rebound and goalie rotation were named as the risk.
**6. What decided the game.** Tied 4-4 after regulation, Rochester won 2:13 into overtime. Laval ML lost; eight regulation goals (nine with OT) beat 5.5 under either convention.
**7. Knowable at cutoff?** Knowable: Laval's form and the back-to-back. Not knowable: Rochester's third-period rally to 4-4 and the 2:13 OT winner.
**8. Process audit.** Chat-local record; no repository reference stage, no source-audit receipts, no lineup confirmation, no freeze. Timing per card in CARD_TIMING.csv.
**9. Verdict.** VARIANCE. A favourite losing in overtime is close to a coin flip; no pre-game fact the card missed explains it.
**10. Cutoff-only counterfactual.** NOT_ESTIMATED: no knowable fact has a measured effect-table row, so no corrected probability is priced after the result.
**11. Failure class and recurrence.** Single card.
**12. Correction.** NO_CHANGE to any rule from one result. Pattern-level proposals are in AUDIT_REPORT (PROPOSED_NOT_TESTED).
**13. Matched wins.** `LOCAL-20261115CHAT48A8D395742B-G0004` TOP_TOTAL Over 5.5 goals WIN. These rest on the same unvalidated construction and do not show the process worked.
**14. Honesty.** Original numbers and labels preserved; no luck claim without the arithmetic above; no invented percentages, operator terms or publication times.

<!-- END SETTLEMENT EVENT E14 revision-1 -->

<!-- BEGIN SETTLEMENT EVENT E15 revision-1 -->
## Event · Dallas Mavericks @ Cleveland Cavaliers · 2026-11-14 ET · NBA 2026-27 regular season (game 0022600232)

**Final:** Cleveland 127-117 Dallas. **Periods:** DAL 33-20-38-26, CLE 33-38-34-22; no OT. **Evidence B.** Scheduled 2026-11-15T00:30:00+00:00. Note: Scheduled tip not printed in the card (game 0022600232); ordering uses the card's pre-tip clock (11:25 AEDT) and request order within the 00:30-01:00Z window.

| Opened source | Audit | Field read |
|---|---|---|
| https://www.foxsports.com/nba/dallas-mavericks-vs-cleveland-cavaliers-nov-14-2026-game-boxscore-106716 | ALLOWED | Line score DAL 33,20,38,26 = 117; CLE 33,38,34,22 = 127; heading dated Nov 15 (UTC) |
| https://www.si.com/nba/scoreboard/mavericks-vs-cavaliers-11-14-2026-1675 | ALLOWED | 'Final Score — November 14, 2026'; same line score |

<!-- BEGIN SETTLEMENT LOCAL-20261115CHAT48A8D395742B-G0005 revision-1 -->
### Settlement · `LOCAL-20261115CHAT48A8D395742B-G0005` · Dallas Mavericks @ Cleveland Cavaliers · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `3395101135cb881bd1e006c50f55ffaae9fd501a1bd6964d764db1c7f505c27f`, 19174 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/20261115CHAT48A8D395742B.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `WRITE_TIME_NOT_RECORDED` (last recorded `NOT_RECORDED`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| R1 | Dallas -8.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | side margin -10, handicap -8.5: -18.5 |  |
| ALT | Cleveland +8.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | side margin +10, handicap +8.5: +18.5 |  |
| R2 | Under 227.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | total 244 vs 227.5: +16.5 |  |
| ALT | Over 227.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | total 244 vs 227.5: +16.5 |  |
| LEAN_WINNER | Dallas to win | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | side margin -10 |  |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_SIDE Dallas -8.5 (NOT_ESTIMATED) LOSS; TOP_TOTAL Under 227.5 (NOT_ESTIMATED) LOSS; RANK1 Dallas -8.5 (NOT_ESTIMATED) LOSS. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** Cleveland 127-117 Dallas; DAL 33-20-38-26, CLE 33-38-34-22; no OT. Identity matched on participants, date and competition (NBA 2026-27 regular season (game 0022600232)).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Basketball rows include overtime (BK-OT-1); none occurred.
**R4. Rank diagnostics.** 2W/3L/0U over 5 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final Dallas minus Cleveland = -10; total 244. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** Cleveland won the second quarter 38-20 and led most of the night; a 10-point home win failed Dallas -8.5 by 18.5. 244 points beat 227.5 by 16.5.
**R9. Source/timing review.** Settlement sources: https://www.foxsports.com/nba/dallas-mavericks-vs-cleveland-cavaliers-nov-14-2026-game-boxscore-106716 (ALLOWED); https://www.si.com/nba/scoreboard/mavericks-vs-cavaliers-11-14-2026-1675 (ALLOWED). Card timing `WRITE_TIME_NOT_RECORDED`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-20261115CHAT48A8D395742B-G0005 revision-1 -->

### Deep loss reviews (DEEPLOSS-v1)

#### Deep loss review · Dallas Mavericks @ Cleveland Cavaliers · Dallas -8.5

**1. Exact frozen claim.** `Dallas -8.5`, full-game endpoint as each card defined it. Triggered in 1 card(s):

| Card | Trigger role(s) | Original p (basis) | Brier | Log loss |
|---|---|---|---:|---:|
| `LOCAL-20261115CHAT48A8D395742B-G0005` | TOP_SIDE, RANK1 | NOT_ESTIMATED (qualitative (no numeric p)) |  |  |

No card carried a primary p_card, frozen reference or same-row baseline; BASELINE_P comparison NOT_COMPUTABLE.

**2. Verified outcome.** Cleveland 127-117 Dallas (DAL 33-20-38-26, CLE 33-38-34-22; no OT). side margin -10, handicap -8.5: -18.5. Sources in R9; evidence B; final wall-clock NOT_VERIFIED.
**3. Distribution check.** Every triggering card was qualitative, so there is no frozen distribution to place the result in.
**4. Error decomposition.** Realised distance: side margin -10, handicap -8.5: -18.5. No card had a calibrated centre or a measured effect row, so the miss is not split into reference and adjustment error; no blame shares are invented.
**5. Research audit.** The card's whole case was Cleveland's reported absences (Mitchell, Harden, Allen, Watson; Mobley and Merrill already out) after a delayed trip, against Dallas' near-neutral 12-game net rating and a 94-133 last loss.
**6. What decided the game.** Cleveland won the second quarter 38-20 and led most of the night; a 10-point home win failed Dallas -8.5 by 18.5. 244 points beat 227.5 by 16.5.
**7. Knowable at cutoff?** Knowable: the absences (reported game day, before the card). Not knowable: Proctor's 24-11-10 triple-double and Cleveland's 38-20 second quarter.
**8. Process audit.** Chat-local record; no repository reference stage, no source-audit receipts, no lineup confirmation, no freeze. Timing per card in CARD_TIMING.csv.
**9. Verdict.** ERROR (unmeasured availability priced as an edge). AUDIT-v1 now requires a measured effect or UNPRICED for exactly this; NBA reserve units routinely outperform depleted expectations. The lean should have been withheld.
**10. Cutoff-only counterfactual.** NOT_ESTIMATED: no knowable fact has a measured effect-table row, so no corrected probability is priced after the result.
**11. Failure class and recurrence.** Single card.
**12. Correction.** NO_CHANGE to any rule from one result. Pattern-level proposals are in AUDIT_REPORT (PROPOSED_NOT_TESTED).
**13. Matched wins.** None among the triggering cards.
**14. Honesty.** Original numbers and labels preserved; no luck claim without the arithmetic above; no invented percentages, operator terms or publication times.

#### Deep loss review · Dallas Mavericks @ Cleveland Cavaliers · Under 227.5

**1. Exact frozen claim.** `Under 227.5`, full-game endpoint as each card defined it. Triggered in 1 card(s):

| Card | Trigger role(s) | Original p (basis) | Brier | Log loss |
|---|---|---|---:|---:|
| `LOCAL-20261115CHAT48A8D395742B-G0005` | TOP_TOTAL | NOT_ESTIMATED (qualitative (no numeric p)) |  |  |

No card carried a primary p_card, frozen reference or same-row baseline; BASELINE_P comparison NOT_COMPUTABLE.

**2. Verified outcome.** Cleveland 127-117 Dallas (DAL 33-20-38-26, CLE 33-38-34-22; no OT). total 244 vs 227.5: +16.5. Sources in R9; evidence B; final wall-clock NOT_VERIFIED.
**3. Distribution check.** Every triggering card was qualitative, so there is no frozen distribution to place the result in.
**4. Error decomposition.** Realised distance: total 244 vs 227.5: +16.5. No card had a calibrated centre or a measured effect row, so the miss is not split into reference and adjustment error; no blame shares are invented.
**5. Research audit.** Same absence thesis: fewer Cleveland creators means fewer points. The card called it 'cautious, not strong' and noted both teams' season games often cleared 227.5.
**6. What decided the game.** Cleveland won the second quarter 38-20 and led most of the night; a 10-point home win failed Dallas -8.5 by 18.5. 244 points beat 227.5 by 16.5.
**7. Knowable at cutoff?** Knowable: both teams' high-scoring season profile. Not knowable: 244 points.
**8. Process audit.** Chat-local record; no repository reference stage, no source-audit receipts, no lineup confirmation, no freeze. Timing per card in CARD_TIMING.csv.
**9. Verdict.** ERROR (same unmeasured availability effect, applied to the total). Should have been no direction.
**10. Cutoff-only counterfactual.** NOT_ESTIMATED: no knowable fact has a measured effect-table row, so no corrected probability is priced after the result.
**11. Failure class and recurrence.** Single card.
**12. Correction.** NO_CHANGE to any rule from one result. Pattern-level proposals are in AUDIT_REPORT (PROPOSED_NOT_TESTED).
**13. Matched wins.** None among the triggering cards.
**14. Honesty.** Original numbers and labels preserved; no luck claim without the arithmetic above; no invented percentages, operator terms or publication times.

#### Joint section · top side and top total both lost · Dallas Mavericks @ Cleveland Cavaliers

Cards: `LOCAL-20261115CHAT48A8D395742B-G0005`: Dallas -8.5 and Under 227.5. Both legs failed on one game state (Cleveland 127-117 Dallas); the leans shared one premise, so treating them as two independent picks would double-count one wrong read.

<!-- END SETTLEMENT EVENT E15 revision-1 -->

<!-- BEGIN SETTLEMENT EVENT E16 revision-1 -->
## Event · Buffalo Sabres @ Dallas Stars · 2026-11-14 CT · NHL 2026-27 regular season (game 2026020322)

**Final:** Dallas 2-0 Buffalo (regulation). **Periods:** Benn 16:23 of 2nd; Johnston power play 19:18 of 3rd; no OT. **Evidence B.** Scheduled 2026-11-15T01:00:00+00:00. Tie: tie at 01:00Z with P-676 and P-677, broken by request order (card keys G0006, G0007, G0008). Note: Single league source (NHL.com is the field owner; evidence B).

| Opened source | Audit | Field read |
|---|---|---|
| https://www.nhl.com/news/buffalo-sabres-dallas-stars-game-recap-november-14-2026 | ALLOWED | 'defeated the Buffalo Sabres 2-0'; Benn '16:23 of the second period'; Johnston 'power play at 19:18 of the third period for the 2-0 final' |

<!-- BEGIN SETTLEMENT LOCAL-20261115CHAT48A8D395742B-G0006 revision-1 -->
### Settlement · `LOCAL-20261115CHAT48A8D395742B-G0006` · Buffalo Sabres @ Dallas Stars · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `c4d7acf54a3e538976af1331aa61d171e396011c52b768328961ade29586822c`, 27653 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/20261115CHAT48A8D395742B.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `PRE_SCHEDULED_START_WRITE` (last recorded `2026-11-15T11:50:26+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| R1 | Buffalo +1.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | side margin -2, handicap +1.5: -0.5 |  |
| R2 | Dallas ML | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | side margin +2 |  |
| R3 | Under 6.5 goals | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | total 2 vs 6.5: -4.5 |  |
| R4 | Over 6.5 goals | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | total 2 vs 6.5: -4.5 |  |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_SIDE Buffalo +1.5 (NOT_ESTIMATED) LOSS; TOP_TOTAL Under 6.5 goals (NOT_ESTIMATED) WIN; RANK1 Buffalo +1.5 (NOT_ESTIMATED) LOSS. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** Dallas 2-0 Buffalo (regulation); Benn 16:23 of 2nd; Johnston power play 19:18 of 3rd; no OT. Identity matched on participants, date and competition (NHL 2026-27 regular season (game 2026020322)).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Hockey rows: every grade is the same under 60-minute, full-game and shootout-credited conventions, except where marked.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final Buffalo minus Dallas = -2; total 2. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** A 1-0 game until 19:18 of the third, when Dallas scored on the power play; a two-goal loss failed Buffalo +1.5 by 0.5. Two goals were 4.5 under 6.5.
**R9. Source/timing review.** Settlement sources: https://www.nhl.com/news/buffalo-sabres-dallas-stars-game-recap-november-14-2026 (ALLOWED). Card timing `PRE_SCHEDULED_START_WRITE`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-20261115CHAT48A8D395742B-G0006 revision-1 -->

### Deep loss reviews (DEEPLOSS-v1)

#### Deep loss review · Buffalo Sabres @ Dallas Stars · Buffalo +1.5

**1. Exact frozen claim.** `Buffalo +1.5`, full-game endpoint as each card defined it. Triggered in 1 card(s):

| Card | Trigger role(s) | Original p (basis) | Brier | Log loss |
|---|---|---|---:|---:|
| `LOCAL-20261115CHAT48A8D395742B-G0006` | TOP_SIDE, RANK1 | NOT_ESTIMATED (qualitative (no numeric p)) |  |  |

No card carried a primary p_card, frozen reference or same-row baseline; BASELINE_P comparison NOT_COMPUTABLE.

**2. Verified outcome.** Dallas 2-0 Buffalo (regulation) (Benn 16:23 of 2nd; Johnston power play 19:18 of 3rd; no OT). side margin -2, handicap +1.5: -0.5. Sources in R9; evidence B; final wall-clock NOT_VERIFIED.
**3. Distribution check.** Every triggering card was qualitative, so there is no frozen distribution to place the result in.
**4. Error decomposition.** Realised distance: side margin -2, handicap +1.5: -0.5. No card had a calibrated centre or a measured effect row, so the miss is not split into reference and adjustment error; no blame shares are invented.
**5. Research audit.** The card used Buffalo's 8/9 road covers and late competitiveness, and Dallas' missing defencemen; it named Dallas' power play against Buffalo's 69.7% penalty kill as the main kill path.
**6. What decided the game.** A 1-0 game until 19:18 of the third, when Dallas scored on the power play; a two-goal loss failed Buffalo +1.5 by 0.5. Two goals were 4.5 under 6.5.
**7. Knowable at cutoff?** Knowable: the special-teams mismatch the card named. Not knowable: a 1-0 game until a power-play goal at 19:18 of the third.
**8. Process audit.** Chat-local record; no repository reference stage, no source-audit receipts, no lineup confirmation, no freeze. Timing per card in CARD_TIMING.csv.
**9. Verdict.** VARIANCE, with the failure coming through exactly the kill path the card named. Lost by half a goal.
**10. Cutoff-only counterfactual.** NOT_ESTIMATED: no knowable fact has a measured effect-table row, so no corrected probability is priced after the result.
**11. Failure class and recurrence.** Single card.
**12. Correction.** NO_CHANGE to any rule from one result. Pattern-level proposals are in AUDIT_REPORT (PROPOSED_NOT_TESTED).
**13. Matched wins.** `LOCAL-20261115CHAT48A8D395742B-G0006` TOP_TOTAL Under 6.5 goals WIN. These rest on the same unvalidated construction and do not show the process worked.
**14. Honesty.** Original numbers and labels preserved; no luck claim without the arithmetic above; no invented percentages, operator terms or publication times.

<!-- END SETTLEMENT EVENT E16 revision-1 -->

<!-- BEGIN SETTLEMENT EVENT E17 revision-1 -->
## Event · Brooklyn Nets @ Memphis Grizzlies · 2026-11-14 CT · NBA 2026-27 regular season (game 0022600234)

**Final:** Memphis 129-110 Brooklyn. **Periods:** Half 71-54 Memphis; no OT. **Evidence C.** Scheduled 2026-11-15T01:00:00+00:00. Tie: tie at 01:00Z, request order. Note: talkbasket returned 403; NBA.com, ESPN, Yahoo and WRAL BLOCKED_FOR_AI.

| Opened source | Audit | Field read |
|---|---|---|
| https://fieldlevelmedia.com/nba/grizzlies-snap-4-game-home-skid-with-win-over-nets/ | ALLOWED | '129-110 win over the visiting Brooklyn Nets'; 'a 71-54 advantage into the break' |

<!-- BEGIN SETTLEMENT LOCAL-20261115CHAT48A8D395742B-G0007 revision-1 -->
### Settlement · `LOCAL-20261115CHAT48A8D395742B-G0007` · Brooklyn Nets @ Memphis Grizzlies · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `02e212107cbab3afc4d891c3476ad2865fafad69ffd2ffd17d7d01bae1817523`, 24920 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/20261115CHAT48A8D395742B.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `WRITE_TIME_NOT_RECORDED` (last recorded `NOT_RECORDED`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| R1 | Nets +4.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | side margin -19, handicap +4.5: -14.5 |  |
| R3 | Grizzlies -4.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | side margin +19, handicap -4.5: +14.5 |  |
| R4 | Over 224.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | total 239 vs 224.5: +14.5 |  |
| R2 | Under 224.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | total 239 vs 224.5: +14.5 |  |
| LEAN_WINNER | Memphis to win | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | side margin +19 |  |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_SIDE Nets +4.5 (NOT_ESTIMATED) LOSS; TOP_TOTAL Under 224.5 (NOT_ESTIMATED) LOSS; RANK1 Nets +4.5 (NOT_ESTIMATED) LOSS. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** Memphis 129-110 Brooklyn; Half 71-54 Memphis; no OT. Identity matched on participants, date and competition (NBA 2026-27 regular season (game 0022600234)).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Basketball rows include overtime (BK-OT-1); none occurred.
**R4. Rank diagnostics.** 3W/2L/0U over 5 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final Brooklyn minus Memphis = -19; total 239. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** Memphis scored 71 in the first half and won by 19; Nets +4.5 failed by 14.5. 239 points beat 224.5 by 14.5.
**R9. Source/timing review.** Settlement sources: https://fieldlevelmedia.com/nba/grizzlies-snap-4-game-home-skid-with-win-over-nets/ (ALLOWED). Card timing `WRITE_TIME_NOT_RECORDED`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-20261115CHAT48A8D395742B-G0007 revision-1 -->

### Deep loss reviews (DEEPLOSS-v1)

#### Deep loss review · Brooklyn Nets @ Memphis Grizzlies · Nets +4.5

**1. Exact frozen claim.** `Nets +4.5`, full-game endpoint as each card defined it. Triggered in 1 card(s):

| Card | Trigger role(s) | Original p (basis) | Brier | Log loss |
|---|---|---|---:|---:|
| `LOCAL-20261115CHAT48A8D395742B-G0007` | TOP_SIDE, RANK1 | NOT_ESTIMATED (qualitative (no numeric p)) |  |  |

No card carried a primary p_card, frozen reference or same-row baseline; BASELINE_P comparison NOT_COMPUTABLE.

**2. Verified outcome.** Memphis 129-110 Brooklyn (Half 71-54 Memphis; no OT). side margin -19, handicap +4.5: -14.5. Sources in R9; evidence C; final wall-clock NOT_VERIFIED.
**3. Distribution check.** Every triggering card was qualitative, so there is no frozen distribution to place the result in.
**4. Error decomposition.** Realised distance: side margin -19, handicap +4.5: -14.5. No card had a calibrated centre or a measured effect row, so the miss is not split into reference and adjustment error; no blame shares are invented.
**5. Research audit.** The card leaned on Memphis missing Jerome and Pippen on a back-to-back, against Memphis' +8 net-rating edge and home court; Edey and Grant were uncertain.
**6. What decided the game.** Memphis scored 71 in the first half and won by 19; Nets +4.5 failed by 14.5. 239 points beat 224.5 by 14.5.
**7. Knowable at cutoff?** Knowable: Memphis' net-rating edge and home court. Not knowable: a 71-54 half.
**8. Process audit.** Chat-local record; no repository reference stage, no source-audit receipts, no lineup confirmation, no freeze. Timing per card in CARD_TIMING.csv.
**9. Verdict.** ERROR (unmeasured availability against a large measured strength gap). Memphis' remaining players produced 129 points; the absences were not worth the cushion the card gave them.
**10. Cutoff-only counterfactual.** NOT_ESTIMATED: no knowable fact has a measured effect-table row, so no corrected probability is priced after the result.
**11. Failure class and recurrence.** Single card.
**12. Correction.** NO_CHANGE to any rule from one result. Pattern-level proposals are in AUDIT_REPORT (PROPOSED_NOT_TESTED).
**13. Matched wins.** None among the triggering cards.
**14. Honesty.** Original numbers and labels preserved; no luck claim without the arithmetic above; no invented percentages, operator terms or publication times.

#### Deep loss review · Brooklyn Nets @ Memphis Grizzlies · Under 224.5

**1. Exact frozen claim.** `Under 224.5`, full-game endpoint as each card defined it. Triggered in 1 card(s):

| Card | Trigger role(s) | Original p (basis) | Brier | Log loss |
|---|---|---|---:|---:|
| `LOCAL-20261115CHAT48A8D395742B-G0007` | TOP_TOTAL | NOT_ESTIMATED (qualitative (no numeric p)) |  |  |

No card carried a primary p_card, frozen reference or same-row baseline; BASELINE_P comparison NOT_COMPUTABLE.

**2. Verified outcome.** Memphis 129-110 Brooklyn (Half 71-54 Memphis; no OT). total 239 vs 224.5: +14.5. Sources in R9; evidence C; final wall-clock NOT_VERIFIED.
**3. Distribution check.** Every triggering card was qualitative, so there is no frozen distribution to place the result in.
**4. Error decomposition.** Realised distance: total 239 vs 224.5: +14.5. No card had a calibrated centre or a measured effect row, so the miss is not split into reference and adjustment error; no blame shares are invented.
**5. Research audit.** Same availability thesis applied to the total, labelled 'very fragile'; both teams' last games were over 250.
**6. What decided the game.** Memphis scored 71 in the first half and won by 19; Nets +4.5 failed by 14.5. 239 points beat 224.5 by 14.5.
**7. Knowable at cutoff?** Knowable: both teams' recent high totals. Not knowable: 239 points.
**8. Process audit.** Chat-local record; no repository reference stage, no source-audit receipts, no lineup confirmation, no freeze. Timing per card in CARD_TIMING.csv.
**9. Verdict.** ERROR (same unmeasured availability effect). Should have been no direction.
**10. Cutoff-only counterfactual.** NOT_ESTIMATED: no knowable fact has a measured effect-table row, so no corrected probability is priced after the result.
**11. Failure class and recurrence.** Single card.
**12. Correction.** NO_CHANGE to any rule from one result. Pattern-level proposals are in AUDIT_REPORT (PROPOSED_NOT_TESTED).
**13. Matched wins.** None among the triggering cards.
**14. Honesty.** Original numbers and labels preserved; no luck claim without the arithmetic above; no invented percentages, operator terms or publication times.

#### Joint section · top side and top total both lost · Brooklyn Nets @ Memphis Grizzlies

Cards: `LOCAL-20261115CHAT48A8D395742B-G0007`: Nets +4.5 and Under 224.5. Both legs failed on one game state (Memphis 129-110 Brooklyn); the leans shared one premise, so treating them as two independent picks would double-count one wrong read.

<!-- END SETTLEMENT EVENT E17 revision-1 -->

<!-- BEGIN SETTLEMENT EVENT E18 revision-1 -->
## Event · Chicago Bulls @ Minnesota Timberwolves · 2026-11-14 CT · NBA 2026-27 regular season

**Final:** Chicago 117-106 Minnesota. **Periods:** Quarter scores NOT_VERIFIED; no OT indicated. **Evidence C.** Scheduled 2026-11-15T01:00:00+00:00. Tie: tie at 01:00Z, request order. Note: bleachernation returned 403; ABC News, NBA.com and Ontap BLOCKED_FOR_AI.

| Opened source | Audit | Field read |
|---|---|---|
| https://www.thesportsanimal.com/2026/11/14/bulls-win-second-straight-halt-timberwolves-five-game-streak/ | ALLOWED | 'held on for a 117-106 win over the Minnesota Timberwolves on Saturday night in Minneapolis' |
| https://fieldlevelmedia.com/nba/grizzlies-snap-4-game-home-skid-with-win-over-nets/ | ALLOWED | Teaser on the same page: Bulls 117-106 (same agency lineage risk) |

<!-- BEGIN SETTLEMENT LOCAL-20261115CHAT48A8D395742B-G0008 revision-1 -->
### Settlement · `LOCAL-20261115CHAT48A8D395742B-G0008` · Chicago Bulls @ Minnesota Timberwolves · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `29788447d6590d7d6aa1949125e7cef3480c59310d8da1711c415d693df6689e`, 26595 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/20261115CHAT48A8D395742B.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `POST_SCHEDULED_START_WRITE` (last recorded `2026-11-15T12:05:25+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| R1 | Under 237.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | total 223 vs 237.5: -14.5 |  |
| R2 | Chicago +15.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | side margin +11, handicap +15.5: +26.5 |  |
| ALT | Minnesota -15.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | side margin -11, handicap -15.5: -26.5 |  |
| ALT | Over 237.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | total 223 vs 237.5: -14.5 |  |
| LEAN_WINNER | Minnesota to win | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | side margin -11 |  |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_SIDE Chicago +15.5 (NOT_ESTIMATED) WIN; TOP_TOTAL Under 237.5 (NOT_ESTIMATED) WIN; RANK1 Under 237.5 (NOT_ESTIMATED) WIN. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** Chicago 117-106 Minnesota; Quarter scores NOT_VERIFIED; no OT indicated. Identity matched on participants, date and competition (NBA 2026-27 regular season).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Basketball rows include overtime (BK-OT-1); none occurred.
**R4. Rank diagnostics.** 2W/3L/0U over 5 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final Chicago minus Minnesota = 11; total 223. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** Chicago won outright by 11, so Chicago +15.5 covered by 26.5; 223 points stayed 14.5 under 237.5.
**R9. Source/timing review.** Settlement sources: https://www.thesportsanimal.com/2026/11/14/bulls-win-second-straight-halt-timberwolves-five-game-streak/ (ALLOWED); https://fieldlevelmedia.com/nba/grizzlies-snap-4-game-home-skid-with-win-over-nets/ (ALLOWED). Card timing `POST_SCHEDULED_START_WRITE`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-20261115CHAT48A8D395742B-G0008 revision-1 -->

<!-- END SETTLEMENT EVENT E18 revision-1 -->

<!-- BEGIN SETTLEMENT EVENT E19 revision-1 -->
## Event · Australia v England · 2026-11-15 · England in Australia 2026-27, 2nd ODI (day-night), Adelaide Oval

**Final:** England 355/6 (50 ov, batted first); result NOT read on an opened page. **Periods:** England after 5 completed overs NOT_VERIFIED; Duckett out for 9 'early'. **Evidence C.** Scheduled 2026-11-15T03:30:00+00:00. Note: Five-over rows UNRESOLVED: ESPNcricinfo RULES_UNKNOWN, TNT Sports RULES_UNKNOWN, ABC and France24 BLOCKED_FOR_AI.

| Opened source | Audit | Field read |
|---|---|---|
| https://www.tribuneindia.com/news/australia-england/aus-vs-eng-2nd-odi-bantons-ton-fifties-from-root-jacks-cox-power-england-to-355-6 | ALLOWED | 'After Australia opted to bowl first'; England 355/6 in 50 overs; 'Bartlett packed Ben Duckett (9) early' |

<!-- BEGIN SETTLEMENT LOCAL-20261115CHAT48A8D395742B-G0009 revision-1 -->
### Settlement · `LOCAL-20261115CHAT48A8D395742B-G0009` · Australia v England · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `a99b9e7d7f791fe20626b593abc466577b9346e81b613e20bbc880082b35999c`, 27971 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/20261115CHAT48A8D395742B.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `PRE_SCHEDULED_START_WRITE` (last recorded `2026-11-15T14:26:36+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| ALT | England innings Over 282.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | innings runs 355 vs 282.5: +72.5 |  |
| R1 | England innings Under 282.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | innings runs 355 vs 282.5: +72.5 |  |
| R2 | England 5 overs Over 26.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **UNRESOLVED** | phase score NOT_VERIFIED |  |
| ALT | England 5 overs Under 26.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **UNRESOLVED** | phase score NOT_VERIFIED |  |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_TOTAL England innings Under 282.5 (NOT_ESTIMATED) LOSS; RANK1 England innings Under 282.5 (NOT_ESTIMATED) LOSS. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** England 355/6 (50 ov, batted first); result NOT read on an opened page; England after 5 completed overs NOT_VERIFIED; Duckett out for 9 'early'. Identity matched on participants, date and competition (England in Australia 2026-27, 2nd ODI (day-night), Adelaide Oval).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Cricket rows: innings totals at completion (all out counts as completion); phase rows need the score at the stated completed over.
**R4. Rank diagnostics.** 1W/1L/2U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final England innings runs = 355; total 355. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** England made 355/6 batting first (Banton century), 72.5 over 282.5. The contracts concern England's innings only; the match result is not needed and is not cited.
**R9. Source/timing review.** Settlement sources: https://www.tribuneindia.com/news/australia-england/aus-vs-eng-2nd-odi-bantons-ton-fifties-from-root-jacks-cox-power-england-to-355-6 (ALLOWED). Card timing `PRE_SCHEDULED_START_WRITE`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-20261115CHAT48A8D395742B-G0009 revision-1 -->

### Deep loss reviews (DEEPLOSS-v1)

#### Deep loss review · Australia v England · England innings Under 282.5

**1. Exact frozen claim.** `England innings Under 282.5`, full-game endpoint as each card defined it. Triggered in 1 card(s):

| Card | Trigger role(s) | Original p (basis) | Brier | Log loss |
|---|---|---|---:|---:|
| `LOCAL-20261115CHAT48A8D395742B-G0009` | TOP_TOTAL, RANK1 | NOT_ESTIMATED (qualitative (no numeric p)) |  |  |

No card carried a primary p_card, frozen reference or same-row baseline; BASELINE_P comparison NOT_COMPUTABLE.

**2. Verified outcome.** England 355/6 (50 ov, batted first); result NOT read on an opened page (England after 5 completed overs NOT_VERIFIED; Duckett out for 9 'early'). innings runs 355 vs 282.5: +72.5. Sources in R9; evidence C; final wall-clock NOT_VERIFIED.
**3. Distribution check.** Every triggering card was qualitative, so there is no frozen distribution to place the result in.
**4. Error decomposition.** Realised distance: innings runs 355 vs 282.5: +72.5. No card had a calibrated centre or a measured effect row, so the miss is not split into reference and adjustment error; no blame shares are invented.
**5. Research audit.** The card's 'very slight' Under rested on England's 131 collapse in Perth and Adelaide's older par; its own table showed 3/5 bat-first innings above 282.5 and 350+ in five of eight bat-first innings.
**6. What decided the game.** England made 355/6 batting first (Banton century), 72.5 over 282.5. The contracts concern England's innings only; the match result is not needed and is not cited.
**7. Knowable at cutoff?** Knowable: England's bat-first ceiling and that they were batting first (toss known before the card). Not knowable: Banton's century.
**8. Process audit.** Chat-local record; no repository reference stage, no source-audit receipts, no lineup confirmation, no freeze. Timing per card in CARD_TIMING.csv.
**9. Verdict.** ERROR (lean against the card's own batting-first evidence). 355/6 cleared by 72.5; it should have been no direction.
**10. Cutoff-only counterfactual.** NOT_ESTIMATED: no knowable fact has a measured effect-table row, so no corrected probability is priced after the result.
**11. Failure class and recurrence.** Single card.
**12. Correction.** NO_CHANGE to any rule from one result. Pattern-level proposals are in AUDIT_REPORT (PROPOSED_NOT_TESTED).
**13. Matched wins.** None among the triggering cards.
**14. Honesty.** Original numbers and labels preserved; no luck claim without the arithmetic above; no invented percentages, operator terms or publication times.

<!-- END SETTLEMENT EVENT E19 revision-1 -->

<!-- BEGIN SETTLEMENT EVENT E20 revision-1 -->
## Event · Brisbane Bullets v Tasmania JackJumpers · 2026-11-15 · NBL 2026-27 Round 9

**Final:** Tasmania 104-92 Brisbane (at Brisbane Entertainment Centre). **Periods:** Q1 26-21 Brisbane; half 52-50 Brisbane; Q3 29-14 Tasmania (79-66); no OT. **Evidence B.** Scheduled 2026-11-15T06:00:00+00:00.

| Opened source | Audit | Field read |
|---|---|---|
| https://www.nbl.com.au/news/stattmann-fires-as-jackjumpers-beat-bullets | ALLOWED | 'BRISBANE BULLETS 92 – TASMANIA JACKJUMPERS 104'; 26-21 quarter-time; 52-50 half; Q3 29-14 |
| https://aapnews.aap.com.au/news/jackjumpers-outgun-bullets-in-nbl-showdown | ALLOWED | 'defeat Brisbane 104-92'; '79-66 at three-quarter time' |

<!-- BEGIN SETTLEMENT LOCAL-20261115CHAT48A8D395742B-G0011 revision-1 -->
### Settlement · `LOCAL-20261115CHAT48A8D395742B-G0011` · Brisbane Bullets v Tasmania JackJumpers · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `28a467e35ed165ad2e6d9f145081aa18bf47f880a2dd76427dbe0c671bce047f`, 26935 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/20261115CHAT48A8D395742B.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `POST_SCHEDULED_START_WRITE` (last recorded `2026-11-15T17:07:48+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| R1 | Tasmania -1.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | side margin +12, handicap -1.5: +10.5 |  |
| ALT | Brisbane +1.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | side margin -12, handicap +1.5: -10.5 |  |
| R2 | Over 185.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | total 196 vs 185.5: +10.5 |  |
| ALT | Under 185.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | total 196 vs 185.5: +10.5 |  |
| LEAN_WINNER | Tasmania to win | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | side margin +12 |  |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_SIDE Tasmania -1.5 (NOT_ESTIMATED) WIN; TOP_TOTAL Over 185.5 (NOT_ESTIMATED) WIN; RANK1 Tasmania -1.5 (NOT_ESTIMATED) WIN. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** Tasmania 104-92 Brisbane (at Brisbane Entertainment Centre); Q1 26-21 Brisbane; half 52-50 Brisbane; Q3 29-14 Tasmania (79-66); no OT. Identity matched on participants, date and competition (NBL 2026-27 Round 9).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Basketball rows include overtime (BK-OT-1); none occurred.
**R4. Rank diagnostics.** 3W/2L/0U over 5 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final Brisbane minus Tasmania = -12; total 196. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** Brisbane led 52-50 at half; Tasmania won the third quarter 29-14 and the game by 12. Tasmania -1.5 covered by 10.5; 196 beat 185.5 by 10.5.
**R9. Source/timing review.** Settlement sources: https://www.nbl.com.au/news/stattmann-fires-as-jackjumpers-beat-bullets (ALLOWED); https://aapnews.aap.com.au/news/jackjumpers-outgun-bullets-in-nbl-showdown (ALLOWED). Card timing `POST_SCHEDULED_START_WRITE`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-20261115CHAT48A8D395742B-G0011 revision-1 -->

<!-- END SETTLEMENT EVENT E20 revision-1 -->

<!-- BEGIN SETTLEMENT EVENT E21 revision-1 -->
## Event · Niigata Albirex BB v Gifu Swoops · 2026-11-15 · B.LEAGUE ONE 2026-27 matchday 10 game 2 (ScheduleKey 507356)

**Final:** Niigata 73-70 Gifu. **Periods:** 20-10, 19-30, 13-13, 21-17 (half 39-40 Gifu); no OT. **Evidence B.** Scheduled 2026-11-15T06:05:00+00:00.

| Opened source | Audit | Field read |
|---|---|---|
| https://www.albirex.com/news/detail/id=25136 | ALLOWED | 73-70; quarters 20-10, 19-30, 13-13, 21-17 |
| https://www.bleague.jp/game_detail/?ScheduleKey=507356 | ALLOWED | '2026/11/15 新潟 VS 岐阜', tip 15:05, final 73-70 |

<!-- BEGIN SETTLEMENT LOCAL-20261115CHAT48A8D395742B-G0010 revision-1 -->
### Settlement · `LOCAL-20261115CHAT48A8D395742B-G0010` · Niigata Albirex BB v Gifu Swoops · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `0c07067e923b61d36f0818a08c01e1864183ba8d2e83e26ce8e90cd5752218ac`, 22740 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/20261115CHAT48A8D395742B.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `PRE_SCHEDULED_START_WRITE` (last recorded `2026-11-15T16:55:06+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| R1 | Niigata -6.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | side margin +3, handicap -6.5: -3.5 |  |
| ALT | Gifu +6.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | side margin -3, handicap +6.5: +3.5 |  |
| R2 | Over 158.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | total 143 vs 158.5: -15.5 |  |
| ALT | Under 158.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | total 143 vs 158.5: -15.5 |  |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_SIDE Niigata -6.5 (NOT_ESTIMATED) LOSS; TOP_TOTAL Over 158.5 (NOT_ESTIMATED) LOSS; RANK1 Niigata -6.5 (NOT_ESTIMATED) LOSS. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** Niigata 73-70 Gifu; 20-10, 19-30, 13-13, 21-17 (half 39-40 Gifu); no OT. Identity matched on participants, date and competition (B.LEAGUE ONE 2026-27 matchday 10 game 2 (ScheduleKey 507356)).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Basketball rows include overtime (BK-OT-1); none occurred.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final Niigata minus Gifu = 3; total 143. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** Gifu won the second quarter 30-19 to lead at half; Niigata won the fourth 21-17 for a three-point win. Niigata -6.5 failed by 3.5; 143 points stayed 15.5 under 158.5.
**R9. Source/timing review.** Settlement sources: https://www.albirex.com/news/detail/id=25136 (ALLOWED); https://www.bleague.jp/game_detail/?ScheduleKey=507356 (ALLOWED). Card timing `PRE_SCHEDULED_START_WRITE`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-20261115CHAT48A8D395742B-G0010 revision-1 -->

### Deep loss reviews (DEEPLOSS-v1)

#### Deep loss review · Niigata Albirex BB v Gifu Swoops · Niigata -6.5

**1. Exact frozen claim.** `Niigata -6.5`, full-game endpoint as each card defined it. Triggered in 1 card(s):

| Card | Trigger role(s) | Original p (basis) | Brier | Log loss |
|---|---|---|---:|---:|
| `LOCAL-20261115CHAT48A8D395742B-G0010` | TOP_SIDE, RANK1 | NOT_ESTIMATED (qualitative (no numeric p)) |  |  |

No card carried a primary p_card, frozen reference or same-row baseline; BASELINE_P comparison NOT_COMPUTABLE.

**2. Verified outcome.** Niigata 73-70 Gifu (20-10, 19-30, 13-13, 21-17 (half 39-40 Gifu); no OT). side margin +3, handicap -6.5: -3.5. Sources in R9; evidence B; final wall-clock NOT_VERIFIED.
**3. Distribution check.** Every triggering card was qualitative, so there is no frozen distribution to place the result in.
**4. Error decomposition.** Realised distance: side margin +3, handicap -6.5: -3.5. No card had a calibrated centre or a measured effect row, so the miss is not split into reference and adjustment error; no blame shares are invented.
**5. Research audit.** The card used Niigata's 9-6 v 3-13 record, the 92-75 win the night before, two of three H2H covers and Gifu's scorer McCree out.
**6. What decided the game.** Gifu won the second quarter 30-19 to lead at half; Niigata won the fourth 21-17 for a three-point win. Niigata -6.5 failed by 3.5; 143 points stayed 15.5 under 158.5.
**7. Knowable at cutoff?** Knowable: that this was game two of a back-to-back and the card's own note of second-day regression risk. Not knowable: Gifu's 30-19 second quarter.
**8. Process audit.** Chat-local record; no repository reference stage, no source-audit receipts, no lineup confirmation, no freeze. Timing per card in CARD_TIMING.csv.
**9. Verdict.** MODEL_LIMIT. A three-point win on day two; the card had no measured back-to-back or rematch effect and the cushion was not justified by evidence beyond the previous night.
**10. Cutoff-only counterfactual.** NOT_ESTIMATED: no knowable fact has a measured effect-table row, so no corrected probability is priced after the result.
**11. Failure class and recurrence.** Single card.
**12. Correction.** NO_CHANGE to any rule from one result. Pattern-level proposals are in AUDIT_REPORT (PROPOSED_NOT_TESTED).
**13. Matched wins.** None among the triggering cards.
**14. Honesty.** Original numbers and labels preserved; no luck claim without the arithmetic above; no invented percentages, operator terms or publication times.

#### Deep loss review · Niigata Albirex BB v Gifu Swoops · Over 158.5

**1. Exact frozen claim.** `Over 158.5`, full-game endpoint as each card defined it. Triggered in 1 card(s):

| Card | Trigger role(s) | Original p (basis) | Brier | Log loss |
|---|---|---|---:|---:|
| `LOCAL-20261115CHAT48A8D395742B-G0010` | TOP_TOTAL | NOT_ESTIMATED (qualitative (no numeric p)) |  |  |

No card carried a primary p_card, frozen reference or same-row baseline; BASELINE_P comparison NOT_COMPUTABLE.

**2. Verified outcome.** Niigata 73-70 Gifu (20-10, 19-30, 13-13, 21-17 (half 39-40 Gifu); no OT). total 143 vs 158.5: -15.5. Sources in R9; evidence B; final wall-clock NOT_VERIFIED.
**3. Distribution check.** Every triggering card was qualitative, so there is no frozen distribution to place the result in.
**4. Error decomposition.** Realised distance: total 143 vs 158.5: -15.5. No card had a calibrated centre or a measured effect row, so the miss is not split into reference and adjustment error; no blame shares are invented.
**5. Research audit.** The card's slight Over came from three H2H totals of 163+ and Gifu's 165.8 season mean, while noting Gifu's L5 mean of 153.8 and the missing scorer.
**6. What decided the game.** Gifu won the second quarter 30-19 to lead at half; Niigata won the fourth 21-17 for a three-point win. Niigata -6.5 failed by 3.5; 143 points stayed 15.5 under 158.5.
**7. Knowable at cutoff?** Knowable: Gifu's lower recent totals and the missing scorer. Not knowable: 143 points.
**8. Process audit.** Chat-local record; no repository reference stage, no source-audit receipts, no lineup confirmation, no freeze. Timing per card in CARD_TIMING.csv.
**9. Verdict.** ERROR (lean against the card's own recent-form and availability evidence). Should have been no direction.
**10. Cutoff-only counterfactual.** NOT_ESTIMATED: no knowable fact has a measured effect-table row, so no corrected probability is priced after the result.
**11. Failure class and recurrence.** Single card.
**12. Correction.** NO_CHANGE to any rule from one result. Pattern-level proposals are in AUDIT_REPORT (PROPOSED_NOT_TESTED).
**13. Matched wins.** None among the triggering cards.
**14. Honesty.** Original numbers and labels preserved; no luck claim without the arithmetic above; no invented percentages, operator terms or publication times.

#### Joint section · top side and top total both lost · Niigata Albirex BB v Gifu Swoops

Cards: `LOCAL-20261115CHAT48A8D395742B-G0010`: Niigata -6.5 and Over 158.5. Both legs failed on one game state (Niigata 73-70 Gifu); the leans shared one premise, so treating them as two independent picks would double-count one wrong read.

<!-- END SETTLEMENT EVENT E21 revision-1 -->

<!-- BEGIN SETTLEMENT EVENT E22 revision-1 -->
## Event · Changwon LG Sakers v Suwon KT Sonicboom · 2026-11-15 · KBL 2026-27 round 2

**Final:** LG 83-81 KT. **Periods:** 64-64 after three quarters; winner with 0.6 s left; no OT indicated. **Evidence C.** Scheduled 2026-11-15T07:30:00+00:00. Tie: tie at 07:30Z with P-682, broken by request order (G0012 before G0013). Note: Jumpball and Basket Korea BLOCKED_FOR_AI; single permitted lineage.

| Opened source | Audit | Field read |
|---|---|---|
| https://www.newspim.com/news/view/20261115000138 | ALLOWED | LG 83-81 KT; 64-64 after the third; Marei winner with 0.6 s left |

<!-- BEGIN SETTLEMENT LOCAL-20261115CHAT48A8D395742B-G0012 revision-1 -->
### Settlement · `LOCAL-20261115CHAT48A8D395742B-G0012` · Changwon LG Sakers v Suwon KT Sonicboom · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `7c1c7c610e1417d6779fe1faeb78c592f62153fc2bd43468f770887e691ce782`, 25608 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/20261115CHAT48A8D395742B.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `PRE_SCHEDULED_START_WRITE` (last recorded `2026-11-15T18:23:03+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| R1 | Suwon KT +3.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | side margin -2, handicap +3.5: +1.5 |  |
| ALT | Changwon LG -3.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | side margin +2, handicap -3.5: -1.5 |  |
| NO_PICK | Over 170.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | total 164 vs 170.5: -6.5 |  |
| NO_PICK | Under 170.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | total 164 vs 170.5: -6.5 |  |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_SIDE Suwon KT +3.5 (NOT_ESTIMATED) WIN; RANK1 Suwon KT +3.5 (NOT_ESTIMATED) WIN. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** LG 83-81 KT; 64-64 after three quarters; winner with 0.6 s left; no OT indicated. Identity matched on participants, date and competition (KBL 2026-27 round 2).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Basketball rows include overtime (BK-OT-1); none occurred.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final LG minus KT = 2; total 164. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** Level 64-64 after three quarters, LG won on Marei's shot with 0.6 seconds left. A two-point loss covered KT +3.5; 164 stayed under 170.5.
**R9. Source/timing review.** Settlement sources: https://www.newspim.com/news/view/20261115000138 (ALLOWED). Card timing `PRE_SCHEDULED_START_WRITE`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-20261115CHAT48A8D395742B-G0012 revision-1 -->

<!-- END SETTLEMENT EVENT E22 revision-1 -->

<!-- BEGIN SETTLEMENT EVENT E23 revision-1 -->
## Event · Busan KCC Egis v Daegu KOGAS Pegasus · 2026-11-15 · KBL 2026-27 round 2

**Final:** KCC 80-77 KOGAS. **Periods:** Q1 16-27, half 34-47, after three 59-58 (KCC first); no OT indicated. **Evidence C.** Scheduled 2026-11-15T07:30:00+00:00. Tie: tie at 07:30Z, request order. Note: Same single permitted article as P-681.

| Opened source | Audit | Field read |
|---|---|---|
| https://www.newspim.com/news/view/20261115000138 | ALLOWED | KCC 80-77; 1Q 16-27; half 34-47; after 3Q 59-58; Heo Hoon decisive play with 3 s left |

<!-- BEGIN SETTLEMENT LOCAL-20261115CHAT48A8D395742B-G0013 revision-1 -->
### Settlement · `LOCAL-20261115CHAT48A8D395742B-G0013` · Busan KCC Egis v Daegu KOGAS Pegasus · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `d3f365930a46693c5ce18c84abf4c4e50f4d1f002e08976777f2d8deb3af17f8`, 21626 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/20261115CHAT48A8D395742B.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `PRE_SCHEDULED_START_WRITE` (last recorded `2026-11-15T18:25:16+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| R1 | Busan KCC -2.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | side margin +3, handicap -2.5: +0.5 |  |
| ALT | Daegu KOGAS +2.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | side margin -3, handicap +2.5: -0.5 |  |
| ALT | Over 167.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | total 157 vs 167.5: -10.5 |  |
| R2 | Under 167.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | total 157 vs 167.5: -10.5 |  |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_SIDE Busan KCC -2.5 (NOT_ESTIMATED) WIN; TOP_TOTAL Under 167.5 (NOT_ESTIMATED) WIN; RANK1 Busan KCC -2.5 (NOT_ESTIMATED) WIN. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** KCC 80-77 KOGAS; Q1 16-27, half 34-47, after three 59-58 (KCC first); no OT indicated. Identity matched on participants, date and competition (KBL 2026-27 round 2).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Basketball rows include overtime (BK-OT-1); none occurred.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final KCC minus KOGAS = 3; total 157. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** KCC trailed by 21 in the second quarter and won 80-77 on a late Heo Hoon play; a three-point win covered KCC -2.5 by 0.5. 157 stayed under 167.5.
**R9. Source/timing review.** Settlement sources: https://www.newspim.com/news/view/20261115000138 (ALLOWED). Card timing `PRE_SCHEDULED_START_WRITE`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-20261115CHAT48A8D395742B-G0013 revision-1 -->

<!-- END SETTLEMENT EVENT E23 revision-1 -->

<!-- BEGIN SETTLEMENT EVENT E24 revision-1 -->
## Event · Kashiwa Reysol v Kawasaki Frontale · 2026-11-15 · J.League YBC Levain Cup 2026 QF 2nd leg (match 111504)

**Final:** Kashiwa 5-4 Kawasaki (aggregate 7-5). **Periods:** HT 1-3; Kawasaki 9', 25', 30', 81'; Kashiwa 45+2', 54', 60', 64', 72'; corners NOT_VERIFIED. **Evidence B.** Scheduled 2026-11-15T08:00:00+00:00. Note: Corner rows UNRESOLVED: the J.League stats tab did not render in fetched text.

| Opened source | Audit | Field read |
|---|---|---|
| https://www.jleague.jp/match/leaguecup/2026/111504/ | ALLOWED | 5-4; kick-off 17:03; goal list with minutes; 45+2' 'GOAL! 1-3'; stats table not in readable text |
| https://soccermagazine.jp/levaincup/17876228 | ALLOWED | 柏 5-4 川崎F; goal minutes 9, 25, 30, 45+2, 54, 60, 64, 72 |

<!-- BEGIN SETTLEMENT LOCAL-20261115CHAT48A8D395742B-G0014 revision-1 -->
### Settlement · `LOCAL-20261115CHAT48A8D395742B-G0014` · Kashiwa Reysol v Kawasaki Frontale · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `c3ff824eb3d0694fd67754030ecefc16765f8dcdede6a4701fef0f668ea33b8d`, 20351 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/20261115CHAT48A8D395742B.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `POST_SCHEDULED_START_WRITE` (last recorded `2026-11-15T19:12:47+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| LEAN | First half Over 0.5 goals | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | first-half goals 4 vs 0.5: +3.5 |  |
| ALT | First half Under 0.5 goals | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | first-half goals 4 vs 0.5: +3.5 |  |
| R1 | Over 2.5 goals | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | total 9 vs 2.5: +6.5 |  |
| ALT | Under 2.5 goals | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | total 9 vs 2.5: +6.5 |  |
| R2 | Corners Under 10.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **UNRESOLVED** | corner count NOT_VERIFIED |  |
| ALT | Corners Over 10.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **UNRESOLVED** | corner count NOT_VERIFIED |  |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_TOTAL Over 2.5 goals (NOT_ESTIMATED) WIN; RANK1 Over 2.5 goals (NOT_ESTIMATED) WIN. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** Kashiwa 5-4 Kawasaki (aggregate 7-5); HT 1-3; Kawasaki 9', 25', 30', 81'; Kashiwa 45+2', 54', 60', 64', 72'; corners NOT_VERIFIED. Identity matched on participants, date and competition (J.League YBC Levain Cup 2026 QF 2nd leg (match 111504)).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Soccer rows: 90 minutes plus stoppage; first half 45 plus stoppage.
**R4. Rank diagnostics.** 2W/2L/2U over 6 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final Kashiwa minus Kawasaki = 1; total 9. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** Kawasaki led 3-0 after half an hour and 3-1 at half; Kashiwa scored four times between 54' and 72'. Nine goals in normal time; four first-half goals.
**R9. Source/timing review.** Settlement sources: https://www.jleague.jp/match/leaguecup/2026/111504/ (ALLOWED); https://soccermagazine.jp/levaincup/17876228 (ALLOWED). Card timing `POST_SCHEDULED_START_WRITE`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-20261115CHAT48A8D395742B-G0014 revision-1 -->

<!-- END SETTLEMENT EVENT E24 revision-1 -->

<!-- BEGIN SETTLEMENT EVENT E25 revision-1 -->
## Event · Australia v New Zealand · 2026-11-15 · IRL Men's Rugby League World Cup 2026 Final, Suncorp Stadium, Brisbane

**Final:** Australia 32-12 New Zealand. **Periods:** Half-time NOT_VERIFIED from an opened page; no golden point indicated. **Evidence C.** Scheduled 2026-11-15T08:35:00+00:00. Note: SBS, RNZ and NZ Herald BLOCKED_FOR_AI; nrl.com redirected to sign-in. The score rests on one permitted AAP line; evidence C.

| Opened source | Audit | Field read |
|---|---|---|
| https://aapnews.aap.com.au/news/jackjumpers-outgun-bullets-in-nbl-showdown | ALLOWED | Sidebar headline 'Kangaroos bounce Kiwis for fourth-straight Cup title', 'toppling New Zealand 32-12 in Brisbane' |
| https://www.rlwc2026.com/ | ALLOWED | Match-report headline 'Kangaroos make it a World Cup four-peat' (15 NOV 2026); score widget placeholder 0-0 |

<!-- BEGIN SETTLEMENT LOCAL-20261115CHAT48A8D395742B-G0015 revision-1 -->
### Settlement · `LOCAL-20261115CHAT48A8D395742B-G0015` · Australia v New Zealand · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `f4f19542a1697118e8f0cd8c2d34d3ade53a73f0cab00056f1419fe153fc575c`, 20635 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/20261115CHAT48A8D395742B.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `PRE_SCHEDULED_START_WRITE` (last recorded `2026-11-15T19:23:44+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| ALT | Australia -3.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | side margin +20, handicap -3.5: +16.5 |  |
| R2 | New Zealand +3.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | side margin -20, handicap +3.5: -16.5 |  |
| R1 | Over 41.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | total 44 vs 41.5: +2.5 |  |
| ALT | Under 41.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | total 44 vs 41.5: +2.5 |  |
| LEAN_WINNER | Australia to win | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | side margin +20 |  |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_SIDE New Zealand +3.5 (NOT_ESTIMATED) LOSS; TOP_TOTAL Over 41.5 (NOT_ESTIMATED) WIN; RANK1 Over 41.5 (NOT_ESTIMATED) WIN. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** Australia 32-12 New Zealand; Half-time NOT_VERIFIED from an opened page; no golden point indicated. Identity matched on participants, date and competition (IRL Men's Rugby League World Cup 2026 Final, Suncorp Stadium, Brisbane).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Rugby league rows full game including golden point; none occurred.
**R4. Rank diagnostics.** 3W/2L/0U over 5 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final Australia minus New Zealand = 20; total 44. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** Australia won by 20, so New Zealand +3.5 failed by 16.5 and Australia -3.5 covered; 44 points beat 41.5 by 2.5.
**R9. Source/timing review.** Settlement sources: https://aapnews.aap.com.au/news/jackjumpers-outgun-bullets-in-nbl-showdown (ALLOWED); https://www.rlwc2026.com/ (ALLOWED). Card timing `PRE_SCHEDULED_START_WRITE`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-20261115CHAT48A8D395742B-G0015 revision-1 -->

### Deep loss reviews (DEEPLOSS-v1)

#### Deep loss review · Australia v New Zealand · New Zealand +3.5

**1. Exact frozen claim.** `New Zealand +3.5`, full-game endpoint as each card defined it. Triggered in 1 card(s):

| Card | Trigger role(s) | Original p (basis) | Brier | Log loss |
|---|---|---|---:|---:|
| `LOCAL-20261115CHAT48A8D395742B-G0015` | TOP_SIDE | NOT_ESTIMATED (qualitative (no numeric p)) |  |  |

No card carried a primary p_card, frozen reference or same-row baseline; BASELINE_P comparison NOT_COMPUTABLE.

**2. Verified outcome.** Australia 32-12 New Zealand (Half-time NOT_VERIFIED from an opened page; no golden point indicated). side margin -20, handicap +3.5: -16.5. Sources in R9; evidence C; final wall-clock NOT_VERIFIED.
**3. Distribution check.** Every triggering card was qualitative, so there is no frozen distribution to place the result in.
**4. Error decomposition.** Realised distance: side margin -20, handicap +3.5: -16.5. No card had a calibrated centre or a measured effect row, so the miss is not split into reference and adjustment error; no blame shares are invented.
**5. Research audit.** The card leaned on the previous 24-22 head-to-head; its own opponent-strength note said Australia's other margins were +14, +60 and +32.
**6. What decided the game.** Australia won by 20, so New Zealand +3.5 failed by 16.5 and Australia -3.5 covered; 44 points beat 41.5 by 2.5.
**7. Knowable at cutoff?** Knowable: Australia's tournament margins and the small 3.5 cushion. Not knowable: a 20-point final.
**8. Process audit.** Chat-local record; no repository reference stage, no source-audit receipts, no lineup confirmation, no freeze. Timing per card in CARD_TIMING.csv.
**9. Verdict.** MODEL_LIMIT. One close head-to-head outweighed four games of evidence; the card labelled it low confidence. Its rank-1 Over 41.5 won.
**10. Cutoff-only counterfactual.** NOT_ESTIMATED: no knowable fact has a measured effect-table row, so no corrected probability is priced after the result.
**11. Failure class and recurrence.** Single card.
**12. Correction.** NO_CHANGE to any rule from one result. Pattern-level proposals are in AUDIT_REPORT (PROPOSED_NOT_TESTED).
**13. Matched wins.** `LOCAL-20261115CHAT48A8D395742B-G0015` RANK1 Over 41.5 WIN; `LOCAL-20261115CHAT48A8D395742B-G0015` TOP_TOTAL Over 41.5 WIN. These rest on the same unvalidated construction and do not show the process worked.
**14. Honesty.** Original numbers and labels preserved; no luck claim without the arithmetic above; no invented percentages, operator terms or publication times.

<!-- END SETTLEMENT EVENT E25 revision-1 -->

<!-- BEGIN SETTLEMENT EVENT E26 revision-1 -->
## Event · Dubai Basketball v Spartak Office Shoes Subotica · 2026-11-15 · ABA League 2026-27 Round 8 Group B (match 77/26/1)

**Final:** Dubai 93-75 Spartak. **Periods:** Quarter scores NOT_VERIFIED; no OT indicated. **Evidence C.** Scheduled 2026-11-15T09:00:00+00:00. Note: League listing only (field owner); highlight titles carry '(14.11.2026)', which conflicts with the 15.11 listing; the card's own pre-tip official page check was 20:00 AEDT 15 Nov.

| Opened source | Audit | Field read |
|---|---|---|
| https://www.aba-liga.com/ | ALLOWED | 'Sun 15.11. 10:00 CET FINISHED' match/77 DUB 93 SPA 75; news 'Dubai Basketball gets the Sunday afternoon win against Spartak Office Shoes' |

<!-- BEGIN SETTLEMENT LOCAL-20261115CHAT48A8D395742B-G0016 revision-1 -->
### Settlement · `LOCAL-20261115CHAT48A8D395742B-G0016` · Dubai Basketball v Spartak Office Shoes Subotica · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `68db999adcc7b5e3ad5ee4d87ae9f6f8a4225347e3415d5facced982345b17eb`, 17200 B, source `research/verification/mini_import_P-660_P-685_2026-11-15-1/inputs/chat_minis/20261115CHAT48A8D395742B.md`). Effective 2026-11-15T12:09:48+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `WRITE_TIME_NOT_RECORDED` (last recorded `NOT_RECORDED`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| ALT | Dubai -12.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | side margin +18, handicap -12.5: +5.5 |  |
| R1 | Spartak +12.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | side margin -18, handicap +12.5: -5.5 |  |
| ALT | Over 170.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **LOSS** | total 168 vs 170.5: -2.5 |  |
| R2 | Under 170.5 | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | total 168 vs 170.5: -2.5 |  |
| LEAN_WINNER | Dubai to win | NOT_ESTIMATED (qualitative (no numeric p)) | **WIN** | side margin +18 |  |

**R1. Original prediction.** Literal rows above; trigger rows: TOP_SIDE Spartak +12.5 (NOT_ESTIMATED) LOSS; TOP_TOTAL Under 170.5 (NOT_ESTIMATED) WIN; RANK1 Spartak +12.5 (NOT_ESTIMATED) LOSS. No primary p_card (chat-local, no repository reference or freeze).
**R2. Final event.** Dubai 93-75 Spartak; Quarter scores NOT_VERIFIED; no OT indicated. Identity matched on participants, date and competition (ABA League 2026-27 Round 8 Group B (match 77/26/1)).
**R3. Contract settlement.** Arithmetic per row; half-point lines cannot push. Basketball rows include overtime (BK-OT-1); none occurred.
**R4. Rank diagnostics.** 3W/2L/0U over 5 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement is retained and graded only where it is a literal row above.
**R6. Line assessment.** Final Dubai minus Spartak = 18; total 168. No prices or odds used.
**R7. Expected versus realised.** Printed centres stay in the core; no new distribution is built. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat outputs).
**R8. What decided it.** Dubai won by 18; Spartak +12.5 failed by 5.5 and Dubai -12.5 covered. 168 points stayed 2.5 under 170.5.
**R9. Source/timing review.** Settlement sources: https://www.aba-liga.com/ (ALLOWED). Card timing `WRITE_TIME_NOT_RECORDED`. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6 and CARD-TRAIN-v1; no model bundle (expert feedback NOT_APPLICABLE_NO_MODEL); no pregame learning log, so none is built after the result (LEARNLOG-v1).
<!-- END SETTLEMENT LOCAL-20261115CHAT48A8D395742B-G0016 revision-1 -->

### Deep loss reviews (DEEPLOSS-v1)

#### Deep loss review · Dubai Basketball v Spartak Office Shoes Subotica · Spartak +12.5

**1. Exact frozen claim.** `Spartak +12.5`, full-game endpoint as each card defined it. Triggered in 1 card(s):

| Card | Trigger role(s) | Original p (basis) | Brier | Log loss |
|---|---|---|---:|---:|
| `LOCAL-20261115CHAT48A8D395742B-G0016` | TOP_SIDE, RANK1 | NOT_ESTIMATED (qualitative (no numeric p)) |  |  |

No card carried a primary p_card, frozen reference or same-row baseline; BASELINE_P comparison NOT_COMPUTABLE.

**2. Verified outcome.** Dubai 93-75 Spartak (Quarter scores NOT_VERIFIED; no OT indicated). side margin -18, handicap +12.5: -5.5. Sources in R9; evidence C; final wall-clock NOT_VERIFIED.
**3. Distribution check.** Every triggering card was qualitative, so there is no frozen distribution to place the result in.
**4. Error decomposition.** Realised distance: side margin -18, handicap +12.5: -5.5. No card had a calibrated centre or a measured effect row, so the miss is not split into reference and adjustment error; no blame shares are invented.
**5. Research audit.** The card's own opponent-strength audit said Dubai were 'objectively strong' (6-0, +12.5 mean margin); the Spartak lean rested on three of four old H2H games within twelve.
**6. What decided the game.** Dubai won by 18; Spartak +12.5 failed by 5.5 and Dubai -12.5 covered. 168 points stayed 2.5 under 170.5.
**7. Knowable at cutoff?** Knowable: Dubai's unbeaten record and margin, which the card wrote down. Not knowable: an 18-point win.
**8. Process audit.** Chat-local record; no repository reference stage, no source-audit receipts, no lineup confirmation, no freeze. Timing per card in CARD_TIMING.csv.
**9. Verdict.** ERROR (plus-handicap against the card's own opponent-strength finding). This is the underdog-cushion pattern from the 14 Nov audit; the lean should have been withheld.
**10. Cutoff-only counterfactual.** NOT_ESTIMATED: no knowable fact has a measured effect-table row, so no corrected probability is priced after the result.
**11. Failure class and recurrence.** Single card.
**12. Correction.** NO_CHANGE to any rule from one result. Pattern-level proposals are in AUDIT_REPORT (PROPOSED_NOT_TESTED).
**13. Matched wins.** `LOCAL-20261115CHAT48A8D395742B-G0016` TOP_TOTAL Under 170.5 WIN. These rest on the same unvalidated construction and do not show the process worked.
**14. Honesty.** Original numbers and labels preserved; no luck claim without the arithmetic above; no invented percentages, operator terms or publication times.

<!-- END SETTLEMENT EVENT E26 revision-1 -->

## Diagnostics (MINI_SETTLEMENT review level; descriptive only)

- Literal rows: 325: 140 WIN, 135 LOSS, 50 UNRESOLVED. **Primary rows: 0.**
- Numeric diagnostic rows: 78; mean Brier 0.2145 (a constant 0.5 scores 0.2500). Rows within a card are complementary pairs and cards on one game share inputs; dependent and descriptive only.
- Rank-1 / first lean by mini (W-L): 202611148A011BE83FCC 6-3; 202611148C6C0822 6-3; 20261114B4496A3F 5-3; 20261114CHAT2988664A 8-1; 20261114EA6B2758F0 5-2; 20261115CHAT48A8D395742B 7-9; CHAT20261114DDA525E495 6-2.
- TOP_SIDE: 34W-22L-6U.
- TOP_TOTAL: 46W-19L-5U.
- ASSESS-100: **0 eligible fully settled paired games** (no EXT-v3 manifest or frozen comparator).

**MINI_SETTLEMENT review row (for prompt 6):** `2026-11-15,MINI_SETTLEMENT,OWNER_DROP_2026-11-15,DATA_REPAIR_REQUIRED,75 chat-local cards on 26 games; zero primary; timing/freeze/source-audit gaps; one game final unverified; see AUDIT_REPORT.md`

## UNRESOLVED_CARRYOVER

| Key | Item | Next source / action | Status |
|---|---|---|---|
| P-664 Tappara U20 v HPK U20 | Final score (all 24 rows) | A permitted page with the result (Tappara/HPK match report, Leijonat is BLOCKED_FOR_AI) | UNRESOLVED, NOT_SCHEDULED |
| P-661, P-662 | Hobart and Adelaide six-over scores (22 rows) | Permitted ball-by-ball (cricket.com.au scorecard rendered without data) | UNRESOLVED |
| P-678 | England after 5 overs (2 rows) | Permitted ball-by-ball | UNRESOLVED |
| P-683 | Kashiwa–Kawasaki corners (2 rows) | J.League stats tab | UNRESOLVED |
| All events | Final wall-clock; actual first play | Official play-by-play / match centres | NOT_VERIFIED |
| Evidence-C events | Second permitted lineage | Field-owner box score from a permitted host | grades unaffected |

## SETTLEMENT_MANIFEST

Cards settled: 75. Events: 26 (25 with verified finals, 1 with all rows UNRESOLVED). Deep loss review groups: 21. Sidecars: FROZEN_SOURCE.csv, MASTER_GRADES.csv, CARD_TIMING.csv, EVENT_FINALS.csv, TERMINAL_TARGETS.csv, SOURCE_DISCOVERY_REGISTER.csv, SOURCE_SEARCH_ATTEMPTS.csv, REQUIREMENT_CLOSURE.csv, SOURCE_ACCESS_AUDIT.csv, SETTLEMENT_CHECKS.csv.
