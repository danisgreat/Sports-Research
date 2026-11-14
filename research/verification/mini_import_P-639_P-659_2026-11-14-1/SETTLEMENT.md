<!-- MINI-SETTLEMENT-FORMAT: mini-settlement-10 -->
# Settlement · owner drop OWNER_DROP_2026-11-14 · seven chat-local minis, 21 games, 90 records

**Prompt 3 (P-2026.11.11-v24.14 · LOCAL_MINI_SETTLEMENT), LOCAL_WORKING_TREE** `C:\Users\danie\Projects\Sports-Research`, branch `main`, base HEAD `008cedc4ff469e7a808292aa3667a7bffe22e273`. Settlement effective 2026-11-14T12:15:21+00:00. Writer: repository agent (Claude Code) at the owner's request of 14 November 2026. Method MDS-2026.11.11-v24.16, scoring SCV-2026.11.11-v13, selection SEL-2026.10.22-v4. Canonical IDs are **not** assigned in this document: every record's mapping below is `NOT_ASSIGNED / PENDING_PROMPT_4_IMPORT`; the prompt-4 import report carries the final mapping.

**What this settles.** Every card or research record in the owner drop, graded on its own frozen text against verified finals. All 90 records are chat-local: none was issued, frozen, linted, reference-run or committed in the repository, so **every row is diagnostic (ANALYST_NOT_PRIMARY) and the primary denominator is zero.** Original ranks, probabilities, leans and wording are copied literally; nothing is re-priced. The audit of each mini against the framework is in [AUDIT_REPORT.md](AUDIT_REPORT.md).

## FROZEN_SOURCE

Frozen at 2026-11-14T12:15:21+00:00 before any settlement text was written. Byte copies of the owner drop are at `research/active_minis/received/OWNER_DROP_2026-11-14/` (178 files, byte-identical to the OneDrive folder). Extracted members used as sources are under `inputs/`. Per-record core offsets, bytes and SHA-256 are in [FROZEN_SOURCE.csv](FROZEN_SOURCE.csv).

| Source mini / bundle | File used | Bytes | SHA-256 | Records | Notes |
|---|---|---:|---|---:|---|
| `20261112EE4AFA68` | `inputs/chat_minis/20261112EE4AFA68.md` | 314991 | `83c6296e3c22df3a3a979c21bc1b42cd40d3a03d1994ccaf0ebaeae4e52d3b43` | 11 | as dropped |
| `20261112CHAT9538BF5E` | `inputs/chat_minis/20261112CHAT9538BF5E.md` | 241223 | `261f9a46042453040f986825cbbdeb1b928d220cd48b213212c374381bd5b562` | 10 | as dropped |
| `202611128358B025` | `inputs/chat_minis/202611128358B025.md` | 225984 | `a87c1cec9a5fcdea84ea22973864863f8fca4336ea8ea10ce974821be4c82498` | 11 | member research/active_minis/202611128358B025.md of drive-download.../202611128358B025_associated_files/Sports_Research_Mini_202611128358B025_Pre_Audit_2026-11-14.zip |
| `20261112CHAT17C8C881` | `inputs/chat_minis/20261112CHAT17C8C881.md` | 222301 | `6011036b8988e3bf5093b12dae0a88f088c216871e876794fc1bfd8d93cf01d6` | 9 | member mini/20261112CHAT17C8C881.md of drive-download.../PRE_AUDIT_BUNDLE_20261112CHAT17C8C881.zip |
| `20261112CC53B5C806` | `inputs/chat_minis/20261112CC53B5C806.md` | 246441 | `9da07f291fe663b9a5c41792613c0419fa0820081a6912c6564b9de7ae4ac5b5` | 9 | as dropped |
| `20261112D3C239297F` | `inputs/chat_minis/20261112D3C239297F.md` | 226276 | `a96275285e5de5cd7ab7241a14f6fbecbdf18b15e085283b38b84e414b177431` | 8 | PREDICTION_MINI_PRE_G0009_READBACK.md (latest available readback; the final 300,547-byte mini SHA fc276d27... is NOT in the drop) |
| `20261109R3NEXT` R3NEXT-A | `inputs/r3next/...` | – | per record | 11 | Strand A: v24.15/16 research drafts embedded in `20261109R3NEXT.md` (174,171 B) and its FULL bundle; each original verified against its declared SHA |
| `20261109R3NEXT` R3NEXT-B | `inputs/r3next/...` | – | per record | 11 | Strand B: DRAFT-001..011 research notes in the DRAFT011 package (`COMPLETE_MINI_LOG_AND_ALL_ASSOCIATED_TEXT.md`); each verified against its declared SHA |
| `20261109R3NEXT` R3NEXT-C | `inputs/r3next/...` | – | per record | 10 | Strand C: v4.12 model cards G1-G010 in `20261109R3NEXT_v412_GAMES_1_TO_10_LOCAL_DRAFT.md` (two byte-identical copies in the drop); G1-G009 verified against declared card SHA, G010 has no declared hash |

**Not settled as forecasts (documentary only, retained in received/):** six v24.15 retrospective conversions per R3NEXT package (RV24-15-01..06, RETRO_v24.15_DRAFT_001..006; each says it is not a forecast), process/review notes, the 30,820-byte `20261109R3NEXT.READ_ONLY_DRAFT.md` (an earlier snapshot of the strand-A container), pre-append snapshots and readbacks of every chat mini, the pasted `mini running log 14112026_1.md` (a rendered copy of the CHAT9538BF5E mini: 99.78% word-identical, URLs stripped), scenario scripts/JSON and integrity receipts. **Missing:** the final `20261112D3C239297F` mini (300,547 B, SHA `fc276d2766f3e0dbff35af58aed2c2957baced5e4ee5b0a7fbf7f90d71b837ae`); its G0009-G0011 card text is therefore MISSING_ORIGINAL (owner decision 14 Nov 2026: proceed without it). Its scripts/JSON outputs exist but no card is reconstructed from them.

## LOCAL_ID_MAPPING (pre-import; unchanged by the import)

| Record key | Event | Native identity | Canonical ID | Status |
|---|---|---|---|---|
| `R3NEXT-B/DRAFT-001` | Polona Hercog v Varvara Lepchenko · 2026-11-09 | WTA 125 Sopó (DIRECTV Open), R32 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `R3NEXT-C/V412-CHAT-G1` | Polona Hercog v Varvara Lepchenko · 2026-11-09 | WTA 125 Sopó (DIRECTV Open), R32 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `R3NEXT-A/Hercog_Lepchenko_Sopo_2026_READ_ONLY_RESEARCH_DRAFT.md` | Polona Hercog v Varvara Lepchenko · 2026-11-09 | WTA 125 Sopó (DIRECTV Open), R32 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `R3NEXT-A/Perth_Lynx_Bendigo_Spirit_2026_READ_ONLY_RESEARCH_DRAFT.md` | Perth Lynx (W) v Bendigo Spirit (W) · 2026-11-10 | WNBL 2026-27 Round 4 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `R3NEXT-B/DRAFT-002` | Perth Lynx (W) v Bendigo Spirit (W) · 2026-11-10 | WNBL 2026-27 Round 4 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `R3NEXT-C/V412-CHAT-G2` | Perth Lynx (W) v Bendigo Spirit (W) · 2026-11-10 | WNBL 2026-27 Round 4 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `R3NEXT-A/Mobis_Phoebus_Goyang_Skygunners_KBL_2026_Read_Only_Research_Draft.md` | Ulsan Hyundai Mobis Phoebus v Goyang Sono Skygunners · 2026-11-10 | KBL 2026-27 Round 2 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `R3NEXT-B/DRAFT-003` | Ulsan Hyundai Mobis Phoebus v Goyang Sono Skygunners · 2026-11-10 | KBL 2026-27 Round 2 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `R3NEXT-C/V412-CHAT-G3` | Ulsan Hyundai Mobis Phoebus v Goyang Sono Skygunners · 2026-11-10 | KBL 2026-27 Round 2 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `R3NEXT-A/Colorado_Avalanche_Toronto_Maple_Leafs_2026_Read_Only_Research_Draft.md` | Colorado Avalanche @ Toronto Maple Leafs · 2026-11-10 ET | NHL 2026-27 regular season | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `R3NEXT-B/DRAFT-004` | Colorado Avalanche @ Toronto Maple Leafs · 2026-11-10 ET | NHL 2026-27 regular season | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `R3NEXT-C/V412-CHAT-G004` | Colorado Avalanche @ Toronto Maple Leafs · 2026-11-10 ET | NHL 2026-27 regular season | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `R3NEXT-A/Creighton_Kansas_State_NCAAB_2026_READ_ONLY_RESEARCH_DRAFT.md` | Creighton Bluejays @ Kansas State Wildcats · 2026-11-10 CT | NCAA Division I men 2026-27 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `R3NEXT-B/DRAFT-006` | Creighton Bluejays @ Kansas State Wildcats · 2026-11-10 CT | NCAA Division I men 2026-27 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `R3NEXT-C/V412-CHAT-G006` | Creighton Bluejays @ Kansas State Wildcats · 2026-11-10 CT | NCAA Division I men 2026-27 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `R3NEXT-A/Colorado_Eagles_Abbotsford_Canucks_AHL_2026_READ_ONLY_RESEARCH_DRAFT.md` | Colorado Eagles @ Abbotsford Canucks · 2026-11-10 PT | AHL 2026-27, native game 1029282 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `R3NEXT-B/DRAFT-005` | Colorado Eagles @ Abbotsford Canucks · 2026-11-10 PT | AHL 2026-27, native game 1029282 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `R3NEXT-C/V412-CHAT-G005` | Colorado Eagles @ Abbotsford Canucks · 2026-11-10 PT | AHL 2026-27, native game 1029282 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `R3NEXT-A/Akita_Ibaraki_BPremier_2026_v24.15_READ_ONLY_RESEARCH_DRAFT.md` | Akita Northern Happinets v Ibaraki Robots · 2026-11-11 | B.LEAGUE PREMIER 2026-27, ScheduleKey 506570 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `R3NEXT-B/DRAFT-007` | Akita Northern Happinets v Ibaraki Robots · 2026-11-11 | B.LEAGUE PREMIER 2026-27, ScheduleKey 506570 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `R3NEXT-C/V412-CHAT-G007` | Akita Northern Happinets v Ibaraki Robots · 2026-11-11 | B.LEAGUE PREMIER 2026-27, ScheduleKey 506570 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `R3NEXT-A/Hiroshima_Dragonflies_Sendai_89ers_BPremier_2026_v24.15_READ_ONLY_RESEARCH_DRAFT.md` | Hiroshima Dragonflies v Sendai 89ers · 2026-11-11 | B.LEAGUE PREMIER 2026-27, ScheduleKey 506574 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `R3NEXT-B/DRAFT-008` | Hiroshima Dragonflies v Sendai 89ers · 2026-11-11 | B.LEAGUE PREMIER 2026-27, ScheduleKey 506574 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `R3NEXT-C/V412-CHAT-G008` | Hiroshima Dragonflies v Sendai 89ers · 2026-11-11 | B.LEAGUE PREMIER 2026-27, ScheduleKey 506574 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `R3NEXT-A/Urawa_Reds_Cerezo_Osaka_LevainCup_2026_v24.15_RESEARCH_DRAFT.md` | Urawa Red Diamonds v Cerezo Osaka · 2026-11-11 | J.League YBC Levain Cup 2026/27 QF first leg (match 111102) | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `R3NEXT-B/DRAFT-010` | Urawa Red Diamonds v Cerezo Osaka · 2026-11-11 | J.League YBC Levain Cup 2026/27 QF first leg (match 111102) | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `R3NEXT-C/V412-CHAT-G009` | Urawa Red Diamonds v Cerezo Osaka · 2026-11-11 | J.League YBC Levain Cup 2026/27 QF first leg (match 111102) | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `R3NEXT-A/Urawa_Kashima_2026_11_11_FIXTURE_IDENTITY_CONFLICT_v24.15.md` | Urawa Red Diamonds v Cerezo Osaka · 2026-11-11 | J.League YBC Levain Cup 2026/27 QF first leg (match 111102) | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `R3NEXT-B/DRAFT-009` | Urawa Red Diamonds v Cerezo Osaka · 2026-11-11 | J.League YBC Levain Cup 2026/27 QF first leg (match 111102) | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `R3NEXT-A/Tasmania_Jewels_Southside_Flyers_WNBL_2026_v24.16_READ_ONLY_RESEARCH_DRAFT.md` | Tasmania Jewels (W) v Southside Melbourne Flyers (W) · 2026-11-12 | WNBL 2026-27 Round 5 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `R3NEXT-B/DRAFT-011` | Tasmania Jewels (W) v Southside Melbourne Flyers (W) · 2026-11-12 | WNBL 2026-27 Round 5 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `R3NEXT-C/V412-CHAT-G010` | Tasmania Jewels (W) v Southside Melbourne Flyers (W) · 2026-11-12 | WNBL 2026-27 Round 5 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261112EE4AFA68-G0001` | Dalibor Svrčina v Otto Virtanen · 2026-11-12 | ATP Challenger 125 Orléans, R16 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261112CHAT9538BF5E-G0001` | Dalibor Svrčina v Otto Virtanen · 2026-11-12 | ATP Challenger 125 Orléans, R16 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-202611128358B025-G0001` | Dalibor Svrčina v Otto Virtanen · 2026-11-12 | ATP Challenger 125 Orléans, R16 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261112CHAT17C8C881-G0001` | Dalibor Svrčina v Otto Virtanen · 2026-11-12 | ATP Challenger 125 Orléans, R16 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261112CC53B5C806-G0001` | Dalibor Svrčina v Otto Virtanen · 2026-11-12 | ATP Challenger 125 Orléans, R16 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261112D3C239297F-G0001` | Dalibor Svrčina v Otto Virtanen · 2026-11-12 | ATP Challenger 125 Orléans, R16 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261112EE4AFA68-G0002` | Torpedo Ust-Kamenogorsk v Arlan Kokshetau · 2026-11-12 | Kazakhstan Pro Hokei Ligasy 2026-27, schedule row 131 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261112CHAT9538BF5E-G0002` | Torpedo Ust-Kamenogorsk v Arlan Kokshetau · 2026-11-12 | Kazakhstan Pro Hokei Ligasy 2026-27, schedule row 131 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-202611128358B025-G0002` | Torpedo Ust-Kamenogorsk v Arlan Kokshetau · 2026-11-12 | Kazakhstan Pro Hokei Ligasy 2026-27, schedule row 131 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261112CHAT17C8C881-G0002` | Torpedo Ust-Kamenogorsk v Arlan Kokshetau · 2026-11-12 | Kazakhstan Pro Hokei Ligasy 2026-27, schedule row 131 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261112CC53B5C806-G0002` | Torpedo Ust-Kamenogorsk v Arlan Kokshetau · 2026-11-12 | Kazakhstan Pro Hokei Ligasy 2026-27, schedule row 131 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261112D3C239297F-G0002` | Torpedo Ust-Kamenogorsk v Arlan Kokshetau · 2026-11-12 | Kazakhstan Pro Hokei Ligasy 2026-27, schedule row 131 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261112EE4AFA68-G0003` | Thiago Agustín Tirante v Aleksandr Shevchenko · 2026-11-12 | ATP 250 Stockholm Open, QF | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261112CHAT9538BF5E-G0003` | Thiago Agustín Tirante v Aleksandr Shevchenko · 2026-11-12 | ATP 250 Stockholm Open, QF | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-202611128358B025-G0003` | Thiago Agustín Tirante v Aleksandr Shevchenko · 2026-11-12 | ATP 250 Stockholm Open, QF | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261112CHAT17C8C881-G0003` | Thiago Agustín Tirante v Aleksandr Shevchenko · 2026-11-12 | ATP 250 Stockholm Open, QF | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261112CC53B5C806-G0003` | Thiago Agustín Tirante v Aleksandr Shevchenko · 2026-11-12 | ATP 250 Stockholm Open, QF | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261112D3C239297F-G0003` | Thiago Agustín Tirante v Aleksandr Shevchenko · 2026-11-12 | ATP 250 Stockholm Open, QF | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261112EE4AFA68-G0004` | Geelong Venom (W) v Perth Lynx (W) · 2026-11-13 | WNBL 2026-27 Round 5 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261112CHAT9538BF5E-G0004` | Geelong Venom (W) v Perth Lynx (W) · 2026-11-13 | WNBL 2026-27 Round 5 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-202611128358B025-G0004` | Geelong Venom (W) v Perth Lynx (W) · 2026-11-13 | WNBL 2026-27 Round 5 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261112CHAT17C8C881-G0004` | Geelong Venom (W) v Perth Lynx (W) · 2026-11-13 | WNBL 2026-27 Round 5 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261112CC53B5C806-G0004` | Geelong Venom (W) v Perth Lynx (W) · 2026-11-13 | WNBL 2026-27 Round 5 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261112D3C239297F-G0004` | Geelong Venom (W) v Perth Lynx (W) · 2026-11-13 | WNBL 2026-27 Round 5 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261112EE4AFA68-G0005` | Wonju DB Promy v Suwon KT Sonicboom · 2026-11-13 | KBL 2026-27 Round 2 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261112CHAT9538BF5E-G0005` | Wonju DB Promy v Suwon KT Sonicboom · 2026-11-13 | KBL 2026-27 Round 2 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-202611128358B025-G0005` | Wonju DB Promy v Suwon KT Sonicboom · 2026-11-13 | KBL 2026-27 Round 2 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261112CHAT17C8C881-G0005` | Wonju DB Promy v Suwon KT Sonicboom · 2026-11-13 | KBL 2026-27 Round 2 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261112CC53B5C806-G0005` | Wonju DB Promy v Suwon KT Sonicboom · 2026-11-13 | KBL 2026-27 Round 2 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261112D3C239297F-G0005` | Wonju DB Promy v Suwon KT Sonicboom · 2026-11-13 | KBL 2026-27 Round 2 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261112EE4AFA68-G0006` | Kawasaki Brave Thunders v Saga Ballooners · 2026-11-13 | B.LEAGUE PREMIER 2026-27, ScheduleKey 506581 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261112CHAT9538BF5E-G0006` | Kawasaki Brave Thunders v Saga Ballooners · 2026-11-13 | B.LEAGUE PREMIER 2026-27, ScheduleKey 506581 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-202611128358B025-G0006` | Kawasaki Brave Thunders v Saga Ballooners · 2026-11-13 | B.LEAGUE PREMIER 2026-27, ScheduleKey 506581 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261112CHAT17C8C881-G0006` | Kawasaki Brave Thunders v Saga Ballooners · 2026-11-13 | B.LEAGUE PREMIER 2026-27, ScheduleKey 506581 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261112CC53B5C806-G0006` | Kawasaki Brave Thunders v Saga Ballooners · 2026-11-13 | B.LEAGUE PREMIER 2026-27, ScheduleKey 506581 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261112D3C239297F-G0006` | Kawasaki Brave Thunders v Saga Ballooners · 2026-11-13 | B.LEAGUE PREMIER 2026-27, ScheduleKey 506581 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261112EE4AFA68-G0007` | BANES Motor České Budějovice U20 v Bílí Tygři Liberec U20 · 2026-11-13 | Czech KB Extraliga juniorů (U20) 2026-27, round 20, federation match 3156 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261112CHAT9538BF5E-G0007` | BANES Motor České Budějovice U20 v Bílí Tygři Liberec U20 · 2026-11-13 | Czech KB Extraliga juniorů (U20) 2026-27, round 20, federation match 3156 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-202611128358B025-G0007` | BANES Motor České Budějovice U20 v Bílí Tygři Liberec U20 · 2026-11-13 | Czech KB Extraliga juniorů (U20) 2026-27, round 20, federation match 3156 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261112CHAT17C8C881-G0007` | BANES Motor České Budějovice U20 v Bílí Tygři Liberec U20 · 2026-11-13 | Czech KB Extraliga juniorů (U20) 2026-27, round 20, federation match 3156 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261112CC53B5C806-G0007` | BANES Motor České Budějovice U20 v Bílí Tygři Liberec U20 · 2026-11-13 | Czech KB Extraliga juniorů (U20) 2026-27, round 20, federation match 3156 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261112D3C239297F-G0007` | BANES Motor České Budějovice U20 v Bílí Tygři Liberec U20 · 2026-11-13 | Czech KB Extraliga juniorů (U20) 2026-27, round 20, federation match 3156 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261112EE4AFA68-G0008` | Zsombor Piros v Daniel Altmaier · 2026-11-13 | ATP Challenger 125 Orléans, QF | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261112CHAT9538BF5E-G0008` | Zsombor Piros v Daniel Altmaier · 2026-11-13 | ATP Challenger 125 Orléans, QF | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-202611128358B025-G0008` | Zsombor Piros v Daniel Altmaier · 2026-11-13 | ATP Challenger 125 Orléans, QF | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261112CHAT17C8C881-G0008` | Zsombor Piros v Daniel Altmaier · 2026-11-13 | ATP Challenger 125 Orléans, QF | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261112CC53B5C806-G0008` | Zsombor Piros v Daniel Altmaier · 2026-11-13 | ATP Challenger 125 Orléans, QF | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261112D3C239297F-G0008` | Zsombor Piros v Daniel Altmaier · 2026-11-13 | ATP Challenger 125 Orléans, QF | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261112EE4AFA68-G0009` | Alejandro Tabilo v Thiago Agustín Tirante · 2026-11-13 | ATP 250 Stockholm Open, SF | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261112CHAT9538BF5E-G0009` | Alejandro Tabilo v Thiago Agustín Tirante · 2026-11-13 | ATP 250 Stockholm Open, SF | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-202611128358B025-G0009` | Alejandro Tabilo v Thiago Agustín Tirante · 2026-11-13 | ATP 250 Stockholm Open, SF | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261112CHAT17C8C881-G0009` | Alejandro Tabilo v Thiago Agustín Tirante · 2026-11-13 | ATP 250 Stockholm Open, SF | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261112CC53B5C806-G0009` | Alejandro Tabilo v Thiago Agustín Tirante · 2026-11-13 | ATP 250 Stockholm Open, SF | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261112EE4AFA68-G0010` | Bryant Bulldogs @ Rutgers Scarlet Knights · 2026-11-13 ET | NCAA Division I men 2026-27 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261112CHAT9538BF5E-G0010` | Bryant Bulldogs @ Rutgers Scarlet Knights · 2026-11-13 ET | NCAA Division I men 2026-27 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-202611128358B025-G0010` | Bryant Bulldogs @ Rutgers Scarlet Knights · 2026-11-13 ET | NCAA Division I men 2026-27 | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261112EE4AFA68-G0011` | New York Knicks @ Indiana Pacers · 2026-11-13 ET | NBA 2026-27, Emirates NBA Cup East Group B (game 0022600034) | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-202611128358B025-G0011` | New York Knicks @ Indiana Pacers · 2026-11-13 ET | NBA 2026-27, Emirates NBA Cup East Group B (game 0022600034) | NOT_ASSIGNED | PENDING_PROMPT_4_IMPORT |
| `LOCAL-20261112D3C239297F-G0009`..`G0011` | Tabilo–Tirante, Bryant–Rutgers, Knicks–Pacers | – | NOT_ASSIGNED | MISSING_ORIGINAL (no card text in drop) |

## Event finals and sources

Every source below passed `python -m ml source-audit --reader CLAUDE_AGENT` (ALLOWED or NO_RULES_FILE) and was opened. **Disclosure:** the first delegated fetch (Torpedo/Motor) ran before the audit; it opened sports.kz, shaiba.kz and hctorpedo.pro (later ALLOWED) and hcmotor.cz, which the audit returned as BLOCKED_FOR_AI. The hcmotor.cz content is excluded and not cited. Search-engine summaries guided discovery only and are never treated as opened sources.

| Event | Final | Periods | Evidence | Final time |
|---|---|---|---|---|
| Polona Hercog v Varvara Lepchenko · 2026-11-09 | Hercog d. Lepchenko 6-2 7-6(3) | Sets 6-2, 7-6(3); games Hercog 13, Lepchenko 8; total 21 | C | NOT_VERIFIED (listing 16:40, zone unstated) |
| Perth Lynx (W) v Bendigo Spirit (W) · 2026-11-10 | Perth 94-84 Bendigo | Breaks 33-31, 53-51, 80-70 (Perth first); quarters 33-31, 20-20, 27-19, 14-14; no OT | B | NOT_VERIFIED |
| Ulsan Hyundai Mobis Phoebus v Goyang Sono Skygunners · 2026-11-10 | Sono 86-79 Mobis (at Ulsan) | Mobis-Sono Q1 22-20 (stated), half 34-47 (stated), after Q3 57-65 (stated); derived Q2 12-27, Q3 23-18, Q4 22-21; no OT | B | NOT_VERIFIED |
| Colorado Avalanche @ Toronto Maple Leafs · 2026-11-10 ET | Colorado 6-3 Toronto (regulation) | COL-TOR 2-1, 1-1, 3-1; 3-3 at 4:11 of 3rd; Landeskog 5:02 (4-3), Lehkonen 17:15 (5-3), Necas empty net 17:30 (6-3) | B | NOT_VERIFIED |
| Creighton Bluejays @ Kansas State Wildcats · 2026-11-10 CT | Kansas State 89-82 Creighton | Halftime 40-40 per a search summary only (ESPN, BLOCKED_FOR_AI, not opened): NOT_VERIFIED; OT not indicated | C | NOT_VERIFIED |
| Colorado Eagles @ Abbotsford Canucks · 2026-11-10 PT | Colorado 4-3 Abbotsford (shootout); 3-3 after regulation and overtime | COL-ABB 2-1, 0-1, 1-1, OT 0-0, SO 1-0 (Wise); Fix-Wolansky tied it 3-3 at 18:05 of 3rd | B | NOT_VERIFIED |
| Akita Northern Happinets v Ibaraki Robots · 2026-11-11 | Ibaraki 95-83 Akita (at Akita) | Akita-Ibaraki 22-22, 28-22, 10-19, 23-32; half 50-44 Akita; no OT | B | NOT_VERIFIED |
| Hiroshima Dragonflies v Sendai 89ers · 2026-11-11 | Sendai 106-91 Hiroshima (at Hiroshima) | Quarter table not rendered; club report: Hiroshima conceded 60 in the first half (narrative); no OT indicated | B | NOT_VERIFIED |
| Urawa Red Diamonds v Cerezo Osaka · 2026-11-11 | Urawa 2-0 Cerezo Osaka (HT 0-0) | Goals Ueki 74', Komori 90+4'; first half 0-0; corner kicks NOT FOUND | A | NOT_VERIFIED |
| Tasmania Jewels (W) v Southside Melbourne Flyers (W) · 2026-11-12 | Tasmania 99-79 Southside | Tas-SS 15-25, 27-15, 30-23, 27-16; half 42-40 Tas (derived; coach 'down by two'); no OT | B | NOT_VERIFIED |
| Dalibor Svrčina v Otto Virtanen · 2026-11-12 | Virtanen d. Svrčina 6-3 7-5 | Games Virtanen 13, Svrčina 8; total 21; ATP match time 01:10:11 | B | NOT_VERIFIED (duration 1:10:11; start not published) |
| Torpedo Ust-Kamenogorsk v Arlan Kokshetau · 2026-11-12 | Torpedo 4-1 Arlan (regulation) | 0:0, 3:1, 1:0; Torpedo 22:49, 24:05, 38:40, 59:33 (empty net); Arlan 24:18 | B | NOT_VERIFIED |
| Thiago Agustín Tirante v Aleksandr Shevchenko · 2026-11-12 | Tirante d. Shevchenko 7-6(5) 6-7(5) 6-3 | Games Tirante 19, Shevchenko 16; total 35; ATP 02:49:27; TennisExplorer start 15:20 (zone not stated) | B | NOT_VERIFIED (duration 2:49:27) |
| Geelong Venom (W) v Perth Lynx (W) · 2026-11-13 | Perth 95-76 Geelong (at Geelong) | Perth-Geelong 21-19, 24-20, 29-17, 21-20; no OT | C | NOT_VERIFIED |
| Wonju DB Promy v Suwon KT Sonicboom · 2026-11-13 | Wonju DB 94-83 Suwon KT | Q1 23-17, half 51-41, after Q3 69-66 (stated); derived Q2 28-24, Q3 18-25, Q4 25-17; no OT | B | NOT_VERIFIED |
| Kawasaki Brave Thunders v Saga Ballooners · 2026-11-13 | Kawasaki 90-72 Saga | Quarter scores shown only as an image on permitted pages: NOT_VERIFIED; no OT indicated | B | NOT_VERIFIED |
| BANES Motor České Budějovice U20 v Bílí Tygři Liberec U20 · 2026-11-13 | Motor 6-1 Liberec (regulation) | 0:0, 1:0, 5:1; official start 13.11.2026 12:00 CET | B | NOT_VERIFIED |
| Zsombor Piros v Daniel Altmaier · 2026-11-13 | Altmaier d. Piros 7-5 6-4 | Games Altmaier 13, Piros 9; total 22; ATP 01:34:40 | C | NOT_VERIFIED (duration 1:34:40) |
| Alejandro Tabilo v Thiago Agustín Tirante · 2026-11-13 | Tirante d. Tabilo 7-5 7-6(1) | Games Tirante 14, Tabilo 11; total 25; ATP 01:46:11; TennisExplorer start 14:10 (zone not stated) | B | NOT_VERIFIED (duration 1:46:11) |
| Bryant Bulldogs @ Rutgers Scarlet Knights · 2026-11-13 ET | Rutgers 72-51 Bryant | Half 35-31 Rutgers; second half 37-20 (derived); no OT indicated | B | NOT_VERIFIED |
| New York Knicks @ Indiana Pacers · 2026-11-13 ET | Indiana 106-104 New York | Quarter line not in permitted text; Knicks scored 20 in Q4 and topped 27 only in Q3 (SI); no OT indicated | C | NOT_VERIFIED |

<!-- BEGIN SETTLEMENT EVENT R01 revision-1 -->
## Event · Polona Hercog v Varvara Lepchenko · 2026-11-09 · WTA 125 Sopó (DIRECTV Open), R32

**Final:** Hercog d. Lepchenko 6-2 7-6(3). **Periods:** Sets 6-2, 7-6(3); games Hercog 13, Lepchenko 8; total 21. **Evidence C.** Scheduled 2026-11-09T15:00:00+00:00.

| Opened source | Audit | Field read |
|---|---|---|
| https://www.tennisexplorer.com/sopo-wta/2026/wta-women/ | ALLOWED | R32 line 6-2, 7-6(3); row 09.11. 16:40 (zone not stated) |
| https://www.wtatennis.com/tournaments/1181/sopo-125/2026/scores | ALLOWED | Loaded; score list did not render (no value read) |

<!-- BEGIN SETTLEMENT R3NEXT-B/DRAFT-001 revision-1 -->
### Settlement · `R3NEXT-B/DRAFT-001` · Polona Hercog v Varvara Lepchenko · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `078507c6f0a36e2f4525240c4149192763cedb64b20a8615f494734cd557a82c`, 15489 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/r3next/COMPLETE/research_notes/DRAFT_001/Hercog_Lepchenko_Sopo_2026-11-10_READ_ONLY_DRAFT.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `TIMING_UNVERIFIED` (recorded `NOT_RECORDED`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| LEAN_SIDE | Hercog to win | NOT_ESTIMATED (QUALITATIVE) | **WIN** | team margin +5 |  |
| LEAN_TOTAL | Under 21.5 games | NOT_ESTIMATED (QUALITATIVE) | **WIN** | total 21 vs 21.5: -0.5 |  |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Hercog to win (NOT_ESTIMATED) WIN; TOP_TOTAL Under 21.5 games (NOT_ESTIMATED) WIN; RANK1 Hercog to win (NOT_ESTIMATED) WIN. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Hercog d. Lepchenko 6-2 7-6(3); Sets 6-2, 7-6(3); games Hercog 13, Lepchenko 8; total 21. Identity matched on teams/players, date and competition (WTA 125 Sopó (DIRECTV Open), R32).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Tennis rows count every game of the completed match; no retirement.
**R4. Rank diagnostics.** 2W/0L/0U over 2 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Hercog games minus Lepchenko games = +5; total 21. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Hercog took the first set 6-2 and won a 7-6(3) second-set tiebreak. The 21-game total sits one game under 21.5; the tiebreak was the only path to the 22nd game.
**R9. Source/timing review.** Settlement sources: https://www.tennisexplorer.com/sopo-wta/2026/wta-women/ (ALLOWED); https://www.wtatennis.com/tournaments/1181/sopo-125/2026/scores (ALLOWED). Card timing `TIMING_UNVERIFIED`; self-declared phase labels: n/a. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT R3NEXT-B/DRAFT-001 revision-1 -->

<!-- BEGIN SETTLEMENT R3NEXT-C/V412-CHAT-G1 revision-1 -->
### Settlement · `R3NEXT-C/V412-CHAT-G1` · Polona Hercog v Varvara Lepchenko · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `36c2f91cedd80adf8fc3335bfb3d5733da8bcea9ad9f0a8c54507a46a02936ab`, 4666 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/r3next/V412/V412-CHAT-G1.block.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `WRITE_TIME_NOT_RECORDED` (recorded `NOT_STATED`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| V412 | Hercog to win | 0.487 (V412_MODEL) | **WIN** | team margin +5 | 0.263169 |
| V412 | Lepchenko to win | 0.513 (V412_MODEL) | **LOSS** | team margin -5 | 0.263169 |
| V412 | Over 21.5 games | 0.603 (V412_MODEL) | **LOSS** | total 21 vs 21.5: -0.5 | 0.363609 |
| V412 | Under 21.5 games | 0.397 (V412_MODEL) | **WIN** | total 21 vs 21.5: -0.5 | 0.363609 |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Lepchenko to win (0.513) LOSS; TOP_TOTAL Over 21.5 games (0.603) LOSS. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Hercog d. Lepchenko 6-2 7-6(3); Sets 6-2, 7-6(3); games Hercog 13, Lepchenko 8; total 21. Identity matched on teams/players, date and competition (WTA 125 Sopó (DIRECTV Open), R32).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Tennis rows count every game of the completed match; no retirement.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Hercog games minus Lepchenko games = +5; total 21. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Hercog took the first set 6-2 and won a 7-6(3) second-set tiebreak. The 21-game total sits one game under 21.5; the tiebreak was the only path to the 22nd game.
**R9. Source/timing review.** Settlement sources: https://www.tennisexplorer.com/sopo-wta/2026/wta-women/ (ALLOWED); https://www.wtatennis.com/tournaments/1181/sopo-125/2026/scores (ALLOWED). Card timing `WRITE_TIME_NOT_RECORDED`; self-declared phase labels: n/a. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT R3NEXT-C/V412-CHAT-G1 revision-1 -->

<!-- BEGIN SETTLEMENT R3NEXT-A/Hercog_Lepchenko_Sopo_2026_READ_ONLY_RESEARCH_DRAFT.md revision-1 -->
### Settlement · `R3NEXT-A/Hercog_Lepchenko_Sopo_2026_READ_ONLY_RESEARCH_DRAFT.md` · Polona Hercog v Varvara Lepchenko · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `369ba0e02363ed78a3e1e9dc9cf69c2843ac6583113d922fefa8edb1e6c25b45`, 12961 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/r3next/FULL/original_research/Hercog_Lepchenko_Sopo_2026_READ_ONLY_RESEARCH_DRAFT.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `TIMING_UNVERIFIED` (recorded `NOT_RECORDED`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| NONE | No direction (NO_RANKED_ROWS / ABSTAIN) | NOT_ESTIMATED (QUALITATIVE) | **NOT_GRADED_NO_DIRECTION** | no direction |  |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: none (no direction). No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Hercog d. Lepchenko 6-2 7-6(3); Sets 6-2, 7-6(3); games Hercog 13, Lepchenko 8; total 21. Identity matched on teams/players, date and competition (WTA 125 Sopó (DIRECTV Open), R32).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Tennis rows count every game of the completed match; no retirement.
**R4. Rank diagnostics.** 0W/0L/0U over 1 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Hercog games minus Lepchenko games = +5; total 21. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Hercog took the first set 6-2 and won a 7-6(3) second-set tiebreak. The 21-game total sits one game under 21.5; the tiebreak was the only path to the 22nd game.
**R9. Source/timing review.** Settlement sources: https://www.tennisexplorer.com/sopo-wta/2026/wta-women/ (ALLOWED); https://www.wtatennis.com/tournaments/1181/sopo-125/2026/scores (ALLOWED). Card timing `TIMING_UNVERIFIED`; self-declared phase labels: n/a. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT R3NEXT-A/Hercog_Lepchenko_Sopo_2026_READ_ONLY_RESEARCH_DRAFT.md revision-1 -->

### Deep loss reviews (DEEPLOSS-v1)

#### Deep loss review · Polona Hercog v Varvara Lepchenko · Lepchenko to win

**1. Exact frozen claim.** `Lepchenko to win`, full-game endpoint as each record defined it. Triggered in 1 record(s):

| Record | Trigger role(s) | Original p (basis) | Brier | Log loss |
|---|---|---|---:|---:|
| `R3NEXT-C/V412-CHAT-G1` | TOP_SIDE | 0.513 (V412_MODEL) | 0.263169 | 0.719491 |

No record carried a primary p_card, frozen reference or same-row baseline; BASELINE_P comparison NOT_COMPUTABLE.

**2. Verified outcome.** Hercog d. Lepchenko 6-2 7-6(3) (Sets 6-2, 7-6(3); games Hercog 13, Lepchenko 8; total 21). team margin -5. Sources in R9; evidence C; final wall-clock NOT_VERIFIED (listing 16:40, zone unstated).
**3. Distribution check.** Numeric records priced this row at 0.513-0.513 (mean 0.513); a loss at those prices is a 49%-49% event under each record's own uncalibrated object. Percentile placement inside each record's printed score object is not reconstructed; the printed objects stay in the cores.
**4. Error decomposition.** Realised line distance: team margin -5. No record had a calibrated centre or a measured effect-table row, so the miss cannot be split into reference error and adjustment error; no blame shares are invented.
**5. Research audit.** v4.12 card built from Elo/ranking/last-5 with 59% data coverage, all rows marked WAIT. Facts not re-opened here remain UNVERIFIED_AT_CUTOFF; no source in any card carries a captured retrieval receipt (chat-local research).
**6. What decided the game.** Hercog took the first set 6-2 and won a 7-6(3) second-set tiebreak. The 21-game total sits one game under 21.5; the tiebreak was the only path to the 22nd game.
**7. Knowable at cutoff?** Hercog's clay history was cited by the research drafts. The final score and its timing were not knowable.
**8. Process audit.** Chat-local record; no repository reference stage, no source-audit receipts, no lineup confirmation, no freeze. Timing per record in CARD_TIMING.csv (several written after the scheduled start). Endpoint and contract definitions were correct.
**9. Verdict.** 51.3% coin flip; the v4.12 tool itself said WAIT. No pick should be inferred.
**10. Cutoff-only counterfactual.** NOT_ESTIMATED: no knowable fact has a measured effect-table row, so no corrected probability is priced after the result.
**11. Failure class and recurrence.** Shared across 1 record(s) on one game: the parallel chats used overlapping public inputs, so their losses are one dependent observation, not 1 independent ones.
**12. Correction.** NO_CHANGE to any rule from one result. Procedure proposals are in AUDIT_REPORT §6 (PROPOSED_NOT_TESTED).
**13. Matched wins.** None among the triggering records.
**14. Honesty.** Original numbers and labels preserved; no luck claim without the arithmetic above; no invented percentages, operator terms or publication times. Preservation PASS; information closure INCOMPLETE.

#### Deep loss review · Polona Hercog v Varvara Lepchenko · Over 21.5 games

**1. Exact frozen claim.** `Over 21.5 games`, full-game endpoint as each record defined it. Triggered in 1 record(s):

| Record | Trigger role(s) | Original p (basis) | Brier | Log loss |
|---|---|---|---:|---:|
| `R3NEXT-C/V412-CHAT-G1` | TOP_TOTAL | 0.603 (V412_MODEL) | 0.363609 | 0.923819 |

No record carried a primary p_card, frozen reference or same-row baseline; BASELINE_P comparison NOT_COMPUTABLE.

**2. Verified outcome.** Hercog d. Lepchenko 6-2 7-6(3) (Sets 6-2, 7-6(3); games Hercog 13, Lepchenko 8; total 21). total 21 vs 21.5: -0.5. Sources in R9; evidence C; final wall-clock NOT_VERIFIED (listing 16:40, zone unstated).
**3. Distribution check.** Numeric records priced this row at 0.603-0.603 (mean 0.603); a loss at those prices is a 40%-40% event under each record's own uncalibrated object. Percentile placement inside each record's printed score object is not reconstructed; the printed objects stay in the cores.
**4. Error decomposition.** Realised line distance: total 21 vs 21.5: -0.5. No record had a calibrated centre or a measured effect-table row, so the miss cannot be split into reference error and adjustment error; no blame shares are invented.
**5. Research audit.** v4.12 total 60.3% with interval 53-67%, no surface adjustment. Facts not re-opened here remain UNVERIFIED_AT_CUTOFF; no source in any card carries a captured retrieval receipt (chat-local research).
**6. What decided the game.** Hercog took the first set 6-2 and won a 7-6(3) second-set tiebreak. The 21-game total sits one game under 21.5; the tiebreak was the only path to the 22nd game.
**7. Knowable at cutoff?** Strand B's qualitative Under lean existed in the same folder. The final score and its timing were not knowable.
**8. Process audit.** Chat-local record; no repository reference stage, no source-audit receipts, no lineup confirmation, no freeze. Timing per record in CARD_TIMING.csv (several written after the scheduled start). Endpoint and contract definitions were correct.
**9. Verdict.** Lost by one game on a 7-6 second set; a priced 60% total with no validation.
**10. Cutoff-only counterfactual.** NOT_ESTIMATED: no knowable fact has a measured effect-table row, so no corrected probability is priced after the result.
**11. Failure class and recurrence.** Shared across 1 record(s) on one game: the parallel chats used overlapping public inputs, so their losses are one dependent observation, not 1 independent ones.
**12. Correction.** NO_CHANGE to any rule from one result. Procedure proposals are in AUDIT_REPORT §6 (PROPOSED_NOT_TESTED).
**13. Matched wins.** None among the triggering records.
**14. Honesty.** Original numbers and labels preserved; no luck claim without the arithmetic above; no invented percentages, operator terms or publication times. Preservation PASS; information closure INCOMPLETE.

#### Joint section · top side and top total both lost · Polona Hercog v Varvara Lepchenko

Records: `R3NEXT-C/V412-CHAT-G1`: Lepchenko to win and Over 21.5 games. Both legs failed on the same game state (Hercog d. Lepchenko 6-2 7-6(3)). The cards' own joint-failure figures, where printed, are retained in the cores; none was calibrated, and treating the two leans as independent picks would double-count one wrong read of the game.

<!-- END SETTLEMENT EVENT R01 revision-1 -->

<!-- BEGIN SETTLEMENT EVENT R02 revision-1 -->
## Event · Perth Lynx (W) v Bendigo Spirit (W) · 2026-11-10 · WNBL 2026-27 Round 4

**Final:** Perth 94-84 Bendigo. **Periods:** Breaks 33-31, 53-51, 80-70 (Perth first); quarters 33-31, 20-20, 27-19, 14-14; no OT. **Evidence B.** Scheduled 2026-11-10T10:00:00+00:00. Same scheduled start as R03 (10:00Z); owner's request order (DRAFT-002 / V412 G2 before G3) breaks the tie.

| Opened source | Audit | Field read |
|---|---|---|
| https://www.basketball.com.au/news/wnbl27-round-4-perth-lynx-bendigo-spirit-match-report | ALLOWED | 'beat the Bendigo Spirit 94-84'; 'Perth led at every break, 33-31, 53-51 and 80-70'; published 11/11/2026 6:19 AM |
| https://www.wnbl.com.au/news/lynx-hold-strong-to-overcome-spirit | ALLOWED | '94-84 victory'; 33-31 quarter-time, 53-51 half, 80-70 three-quarter |

<!-- BEGIN SETTLEMENT R3NEXT-A/Perth_Lynx_Bendigo_Spirit_2026_READ_ONLY_RESEARCH_DRAFT.md revision-1 -->
### Settlement · `R3NEXT-A/Perth_Lynx_Bendigo_Spirit_2026_READ_ONLY_RESEARCH_DRAFT.md` · Perth Lynx (W) v Bendigo Spirit (W) · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `abf15c595405bed9d9ae392d6538994bee8e0c972ae79770ff85c165d27d05d8`, 20705 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/r3next/FULL/original_research/Perth_Lynx_Bendigo_Spirit_2026_READ_ONLY_RESEARCH_DRAFT.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `TIMING_UNVERIFIED` (recorded `NOT_RECORDED`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| LEAN_SIDE | Bendigo +10.5 | 0.616 (SHRUNK_SCORE_DIAGNOSTIC) | **WIN** | team margin -10 with handicap +10.5: cover by +0.5 | 0.147456 |
| INFO | Over 167.5 | 0.552 (SHRUNK_SCORE_DIAGNOSTIC) | **WIN** | total 178 vs 167.5: +10.5 | 0.200704 |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Bendigo +10.5 (0.616) WIN; TOP_TOTAL Over 167.5 (0.552) WIN; RANK1 Bendigo +10.5 (0.616) WIN. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Perth 94-84 Bendigo; Breaks 33-31, 53-51, 80-70 (Perth first); quarters 33-31, 20-20, 27-19, 14-14; no OT. Identity matched on teams/players, date and competition (WNBL 2026-27 Round 4).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Basketball rows include overtime (BK-OT-1); none occurred.
**R4. Rank diagnostics.** 2W/0L/0U over 2 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Perth minus Bendigo = +10; total 178. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Perth won the third quarter 27-19 to lead by ten and the fourth finished 14-14, so the margin closed at exactly 10, half a point short of Perth -10.5. Amoore 27 points and six threes; total 178 cleared 167.5 by 10.5.
**R9. Source/timing review.** Settlement sources: https://www.basketball.com.au/news/wnbl27-round-4-perth-lynx-bendigo-spirit-match-report (ALLOWED); https://www.wnbl.com.au/news/lynx-hold-strong-to-overcome-spirit (ALLOWED). Card timing `TIMING_UNVERIFIED`; self-declared phase labels: n/a. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT R3NEXT-A/Perth_Lynx_Bendigo_Spirit_2026_READ_ONLY_RESEARCH_DRAFT.md revision-1 -->

<!-- BEGIN SETTLEMENT R3NEXT-B/DRAFT-002 revision-1 -->
### Settlement · `R3NEXT-B/DRAFT-002` · Perth Lynx (W) v Bendigo Spirit (W) · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `b622817ec9c565ecc44b54e25699ba1b5ec9f7f242ec9cd723f8734fb7ca2e69`, 16592 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/r3next/COMPLETE/research_notes/DRAFT_002/Perth_Lynx_Bendigo_Spirit_WNBL_2026-11-10_READ_ONLY_DRAFT.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `TIMING_UNVERIFIED` (recorded `NOT_RECORDED`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| LEAN_SIDE | Perth -10.5 | NOT_ESTIMATED (QUALITATIVE) | **LOSS** | team margin +10 with handicap -10.5: cover by -0.5 |  |
| LEAN_TOTAL | Over 167.5 | NOT_ESTIMATED (QUALITATIVE) | **WIN** | total 178 vs 167.5: +10.5 |  |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Perth -10.5 (NOT_ESTIMATED) LOSS; TOP_TOTAL Over 167.5 (NOT_ESTIMATED) WIN; RANK1 Perth -10.5 (NOT_ESTIMATED) LOSS. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Perth 94-84 Bendigo; Breaks 33-31, 53-51, 80-70 (Perth first); quarters 33-31, 20-20, 27-19, 14-14; no OT. Identity matched on teams/players, date and competition (WNBL 2026-27 Round 4).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Basketball rows include overtime (BK-OT-1); none occurred.
**R4. Rank diagnostics.** 1W/1L/0U over 2 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Perth minus Bendigo = +10; total 178. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Perth won the third quarter 27-19 to lead by ten and the fourth finished 14-14, so the margin closed at exactly 10, half a point short of Perth -10.5. Amoore 27 points and six threes; total 178 cleared 167.5 by 10.5.
**R9. Source/timing review.** Settlement sources: https://www.basketball.com.au/news/wnbl27-round-4-perth-lynx-bendigo-spirit-match-report (ALLOWED); https://www.wnbl.com.au/news/lynx-hold-strong-to-overcome-spirit (ALLOWED). Card timing `TIMING_UNVERIFIED`; self-declared phase labels: n/a. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT R3NEXT-B/DRAFT-002 revision-1 -->

<!-- BEGIN SETTLEMENT R3NEXT-C/V412-CHAT-G2 revision-1 -->
### Settlement · `R3NEXT-C/V412-CHAT-G2` · Perth Lynx (W) v Bendigo Spirit (W) · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `4845678cb22924ea619a0688c97f22dd8ebbc3ae9c758376fc54145f522a8211`, 5780 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/r3next/V412/V412-CHAT-G2.block.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `WRITE_TIME_NOT_RECORDED` (recorded `NOT_STATED`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| V412 | Perth -10.5 | 0.421 (V412_MODEL) | **LOSS** | team margin +10 with handicap -10.5: cover by -0.5 | 0.177241 |
| V412 | Bendigo +10.5 | 0.579 (V412_MODEL) | **WIN** | team margin -10 with handicap +10.5: cover by +0.5 | 0.177241 |
| V412 | Over 167.5 | 0.382 (V412_MODEL) | **WIN** | total 178 vs 167.5: +10.5 | 0.381924 |
| V412 | Under 167.5 | 0.618 (V412_MODEL) | **LOSS** | total 178 vs 167.5: +10.5 | 0.381924 |
| V412 | Perth to win | 0.700 (V412_MODEL) | **WIN** | team margin +10 | 0.090000 |
| V412 | Bendigo to win | 0.300 (V412_MODEL) | **LOSS** | team margin -10 | 0.090000 |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Perth to win (0.700) WIN; TOP_TOTAL Under 167.5 (0.618) LOSS. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Perth 94-84 Bendigo; Breaks 33-31, 53-51, 80-70 (Perth first); quarters 33-31, 20-20, 27-19, 14-14; no OT. Identity matched on teams/players, date and competition (WNBL 2026-27 Round 4).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Basketball rows include overtime (BK-OT-1); none occurred.
**R4. Rank diagnostics.** 3W/3L/0U over 6 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Perth minus Bendigo = +10; total 178. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Perth won the third quarter 27-19 to lead by ten and the fourth finished 14-14, so the margin closed at exactly 10, half a point short of Perth -10.5. Amoore 27 points and six threes; total 178 cleared 167.5 by 10.5.
**R9. Source/timing review.** Settlement sources: https://www.basketball.com.au/news/wnbl27-round-4-perth-lynx-bendigo-spirit-match-report (ALLOWED); https://www.wnbl.com.au/news/lynx-hold-strong-to-overcome-spirit (ALLOWED). Card timing `WRITE_TIME_NOT_RECORDED`; self-declared phase labels: n/a. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT R3NEXT-C/V412-CHAT-G2 revision-1 -->

### Deep loss reviews (DEEPLOSS-v1)

#### Deep loss review · Perth Lynx (W) v Bendigo Spirit (W) · Perth -10.5

**1. Exact frozen claim.** `Perth -10.5`, full-game endpoint as each record defined it. Triggered in 1 record(s):

| Record | Trigger role(s) | Original p (basis) | Brier | Log loss |
|---|---|---|---:|---:|
| `R3NEXT-B/DRAFT-002` | TOP_SIDE, RANK1 | NOT_ESTIMATED (QUALITATIVE) |  |  |

No record carried a primary p_card, frozen reference or same-row baseline; BASELINE_P comparison NOT_COMPUTABLE.

**2. Verified outcome.** Perth 94-84 Bendigo (Breaks 33-31, 53-51, 80-70 (Perth first); quarters 33-31, 20-20, 27-19, 14-14; no OT). team margin +10 with handicap -10.5: cover by -0.5. Sources in R9; evidence B; final wall-clock NOT_VERIFIED.
**3. Distribution check.** Every triggering record was qualitative (NOT_ESTIMATED), so there is no frozen distribution to place the result in. Percentile placement inside each record's printed score object is not reconstructed; the printed objects stay in the cores.
**4. Error decomposition.** Realised line distance: team margin +10 with handicap -10.5: cover by -0.5. No record had a calibrated centre or a measured effect-table row, so the miss cannot be split into reference error and adjustment error; no blame shares are invented.
**5. Research audit.** Strand B qualitative only. Facts not re-opened here remain UNVERIFIED_AT_CUTOFF; no source in any card carries a captured retrieval receipt (chat-local research).
**6. What decided the game.** Perth won the third quarter 27-19 to lead by ten and the fourth finished 14-14, so the margin closed at exactly 10, half a point short of Perth -10.5. Amoore 27 points and six threes; total 178 cleared 167.5 by 10.5.
**7. Knowable at cutoff?** Strand A's shrunk-score diagnostic had Bendigo +10.5 at 61.6%; v4.12 had it at 57.9%. The final score and its timing were not knowable.
**8. Process audit.** Chat-local record; no repository reference stage, no source-audit receipts, no lineup confirmation, no freeze. Timing per record in CARD_TIMING.csv (several written after the scheduled start). Endpoint and contract definitions were correct.
**9. Verdict.** Lost by half a point (margin exactly 10). The numeric sources pointed the other way.
**10. Cutoff-only counterfactual.** NOT_ESTIMATED: no knowable fact has a measured effect-table row, so no corrected probability is priced after the result.
**11. Failure class and recurrence.** Shared across 1 record(s) on one game: the parallel chats used overlapping public inputs, so their losses are one dependent observation, not 1 independent ones.
**12. Correction.** NO_CHANGE to any rule from one result. Procedure proposals are in AUDIT_REPORT §6 (PROPOSED_NOT_TESTED).
**13. Matched wins.** `R3NEXT-B/DRAFT-002` TOP_TOTAL Over 167.5 WIN. These rest on the same unvalidated construction and do not show the process worked.
**14. Honesty.** Original numbers and labels preserved; no luck claim without the arithmetic above; no invented percentages, operator terms or publication times. Preservation PASS; information closure INCOMPLETE.

#### Deep loss review · Perth Lynx (W) v Bendigo Spirit (W) · Under 167.5

**1. Exact frozen claim.** `Under 167.5`, full-game endpoint as each record defined it. Triggered in 1 record(s):

| Record | Trigger role(s) | Original p (basis) | Brier | Log loss |
|---|---|---|---:|---:|
| `R3NEXT-C/V412-CHAT-G2` | TOP_TOTAL | 0.618 (V412_MODEL) | 0.381924 | 0.962335 |

No record carried a primary p_card, frozen reference or same-row baseline; BASELINE_P comparison NOT_COMPUTABLE.

**2. Verified outcome.** Perth 94-84 Bendigo (Breaks 33-31, 53-51, 80-70 (Perth first); quarters 33-31, 20-20, 27-19, 14-14; no OT). total 178 vs 167.5: +10.5. Sources in R9; evidence B; final wall-clock NOT_VERIFIED.
**3. Distribution check.** Numeric records priced this row at 0.618-0.618 (mean 0.618); a loss at those prices is a 38%-38% event under each record's own uncalibrated object. Percentile placement inside each record's printed score object is not reconstructed; the printed objects stay in the cores.
**4. Error decomposition.** Realised line distance: total 178 vs 167.5: +10.5. No record had a calibrated centre or a measured effect-table row, so the miss cannot be split into reference error and adjustment error; no blame shares are invented.
**5. Research audit.** v4.12 'built from only the two teams' own results (weaker)'. Facts not re-opened here remain UNVERIFIED_AT_CUTOFF; no source in any card carries a captured retrieval receipt (chat-local research).
**6. What decided the game.** Perth won the third quarter 27-19 to lead by ten and the fourth finished 14-14, so the margin closed at exactly 10, half a point short of Perth -10.5. Amoore 27 points and six threes; total 178 cleared 167.5 by 10.5.
**7. Knowable at cutoff?** Six older H2Hs under; current-season rates pointed Over (strand A 55.2%). The final score and its timing were not knowable.
**8. Process audit.** Chat-local record; no repository reference stage, no source-audit receipts, no lineup confirmation, no freeze. Timing per record in CARD_TIMING.csv (several written after the scheduled start). Endpoint and contract definitions were correct.
**9. Verdict.** v4.12's 61.8% Under ignored current-season scoring; total 178.
**10. Cutoff-only counterfactual.** NOT_ESTIMATED: no knowable fact has a measured effect-table row, so no corrected probability is priced after the result.
**11. Failure class and recurrence.** Shared across 1 record(s) on one game: the parallel chats used overlapping public inputs, so their losses are one dependent observation, not 1 independent ones.
**12. Correction.** NO_CHANGE to any rule from one result. Procedure proposals are in AUDIT_REPORT §6 (PROPOSED_NOT_TESTED).
**13. Matched wins.** `R3NEXT-C/V412-CHAT-G2` TOP_SIDE Perth to win WIN. These rest on the same unvalidated construction and do not show the process worked.
**14. Honesty.** Original numbers and labels preserved; no luck claim without the arithmetic above; no invented percentages, operator terms or publication times. Preservation PASS; information closure INCOMPLETE.

<!-- END SETTLEMENT EVENT R02 revision-1 -->

<!-- BEGIN SETTLEMENT EVENT R03 revision-1 -->
## Event · Ulsan Hyundai Mobis Phoebus v Goyang Sono Skygunners · 2026-11-10 · KBL 2026-27 Round 2

**Final:** Sono 86-79 Mobis (at Ulsan). **Periods:** Mobis-Sono Q1 22-20 (stated), half 34-47 (stated), after Q3 57-65 (stated); derived Q2 12-27, Q3 23-18, Q4 22-21; no OT. **Evidence B.** Scheduled 2026-11-10T10:00:00+00:00.

| Opened source | Audit | Field read |
|---|---|---|
| https://www.newspim.com/news/view/20261110001526 | ALLOWED | '86-79로 승리'; Q1 22-20 Mobis; half 47-34 Sono; published 2026-11-10 21:23 |
| https://news.jkn.co.kr/post/1084944 | ALLOWED | 86-79; end Q3 65-57 Sono; Mobis held to 12 in Q2 |

<!-- BEGIN SETTLEMENT R3NEXT-A/Mobis_Phoebus_Goyang_Skygunners_KBL_2026_Read_Only_Research_Draft.md revision-1 -->
### Settlement · `R3NEXT-A/Mobis_Phoebus_Goyang_Skygunners_KBL_2026_Read_Only_Research_Draft.md` · Ulsan Hyundai Mobis Phoebus v Goyang Sono Skygunners · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `2891f73b53c43569c19a81a0bf31ced26581e08913735781041948d30c94edfb`, 20845 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/r3next/FULL/original_research/Mobis_Phoebus_Goyang_Skygunners_KBL_2026_Read_Only_Research_Draft.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `TIMING_UNVERIFIED` (recorded `NOT_RECORDED`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| LEAN_SIDE | Mobis +3.0 | NOT_ESTIMATED (QUALITATIVE) | **LOSS** | team margin -7 with handicap +3: cover by -4 |  |
| LEAN_TOTAL | Under 175.5 | NOT_ESTIMATED (QUALITATIVE) | **WIN** | total 165 vs 175.5: -10.5 |  |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Mobis +3.0 (NOT_ESTIMATED) LOSS; TOP_TOTAL Under 175.5 (NOT_ESTIMATED) WIN; RANK1 Mobis +3.0 (NOT_ESTIMATED) LOSS. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Sono 86-79 Mobis (at Ulsan); Mobis-Sono Q1 22-20 (stated), half 34-47 (stated), after Q3 57-65 (stated); derived Q2 12-27, Q3 23-18, Q4 22-21; no OT. Identity matched on teams/players, date and competition (KBL 2026-27 Round 2).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Basketball rows include overtime (BK-OT-1); none occurred.
**R4. Rank diagnostics.** 1W/1L/0U over 2 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Mobis minus Sono = -7; total 165. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Mobis scored 12 in the second quarter (27 conceded) and trailed by 13 at half; Mobis shot 8/31 from three (26%). Lee Jung-hyun 26 and O'Bryant 29/12 for Sono. A 7-point home loss beats Mobis +3.0 by 4 points.
**R9. Source/timing review.** Settlement sources: https://www.newspim.com/news/view/20261110001526 (ALLOWED); https://news.jkn.co.kr/post/1084944 (ALLOWED). Card timing `TIMING_UNVERIFIED`; self-declared phase labels: n/a. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT R3NEXT-A/Mobis_Phoebus_Goyang_Skygunners_KBL_2026_Read_Only_Research_Draft.md revision-1 -->

<!-- BEGIN SETTLEMENT R3NEXT-B/DRAFT-003 revision-1 -->
### Settlement · `R3NEXT-B/DRAFT-003` · Ulsan Hyundai Mobis Phoebus v Goyang Sono Skygunners · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `b59062d1079e7abdd2de4c2a9eb2cca10314b2a12b07e6f82eb9aa33d652496a`, 14149 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/r3next/COMPLETE/research_notes/DRAFT_003/Mobis_Phoebus_Goyang_Sono_KBL_2026-11-10_READ_ONLY_DRAFT.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `TIMING_UNVERIFIED` (recorded `NOT_RECORDED`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| LEAN_SIDE | Mobis +3.0 | NOT_ESTIMATED (QUALITATIVE) | **LOSS** | team margin -7 with handicap +3: cover by -4 |  |
| LEAN_TOTAL | Under 175.5 | NOT_ESTIMATED (QUALITATIVE) | **WIN** | total 165 vs 175.5: -10.5 |  |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Mobis +3.0 (NOT_ESTIMATED) LOSS; TOP_TOTAL Under 175.5 (NOT_ESTIMATED) WIN; RANK1 Mobis +3.0 (NOT_ESTIMATED) LOSS. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Sono 86-79 Mobis (at Ulsan); Mobis-Sono Q1 22-20 (stated), half 34-47 (stated), after Q3 57-65 (stated); derived Q2 12-27, Q3 23-18, Q4 22-21; no OT. Identity matched on teams/players, date and competition (KBL 2026-27 Round 2).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Basketball rows include overtime (BK-OT-1); none occurred.
**R4. Rank diagnostics.** 1W/1L/0U over 2 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Mobis minus Sono = -7; total 165. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Mobis scored 12 in the second quarter (27 conceded) and trailed by 13 at half; Mobis shot 8/31 from three (26%). Lee Jung-hyun 26 and O'Bryant 29/12 for Sono. A 7-point home loss beats Mobis +3.0 by 4 points.
**R9. Source/timing review.** Settlement sources: https://www.newspim.com/news/view/20261110001526 (ALLOWED); https://news.jkn.co.kr/post/1084944 (ALLOWED). Card timing `TIMING_UNVERIFIED`; self-declared phase labels: n/a. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT R3NEXT-B/DRAFT-003 revision-1 -->

<!-- BEGIN SETTLEMENT R3NEXT-C/V412-CHAT-G3 revision-1 -->
### Settlement · `R3NEXT-C/V412-CHAT-G3` · Ulsan Hyundai Mobis Phoebus v Goyang Sono Skygunners · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `699f9992a5be9c721cd59e4d8a40c47a285f8c1716237ec27d78d2d9059ffa19`, 6441 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/r3next/V412/V412-CHAT-G3.block.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `WRITE_TIME_NOT_RECORDED` (recorded `NOT_STATED`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| V412 | Mobis +3.0 | 0.484 (V412_MODEL) | **LOSS** | team margin -7 with handicap +3: cover by -4 | 0.234256 |
| V412 | Goyang -3.0 | 0.516 (V412_MODEL) | **WIN** | team margin +7 with handicap -3: cover by +4 | 0.234256 |
| V412 | Over 175.5 | 0.372 (V412_MODEL) | **LOSS** | total 165 vs 175.5: -10.5 | 0.138384 |
| V412 | Under 175.5 | 0.628 (V412_MODEL) | **WIN** | total 165 vs 175.5: -10.5 | 0.138384 |
| V412 | Mobis to win | 0.403 (V412_MODEL) | **LOSS** | team margin -7 | 0.162409 |
| V412 | Goyang to win | 0.597 (V412_MODEL) | **WIN** | team margin +7 | 0.162409 |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Goyang to win (0.597) WIN; TOP_TOTAL Under 175.5 (0.628) WIN. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Sono 86-79 Mobis (at Ulsan); Mobis-Sono Q1 22-20 (stated), half 34-47 (stated), after Q3 57-65 (stated); derived Q2 12-27, Q3 23-18, Q4 22-21; no OT. Identity matched on teams/players, date and competition (KBL 2026-27 Round 2).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Basketball rows include overtime (BK-OT-1); none occurred.
**R4. Rank diagnostics.** 3W/3L/0U over 6 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Mobis minus Sono = -7; total 165. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Mobis scored 12 in the second quarter (27 conceded) and trailed by 13 at half; Mobis shot 8/31 from three (26%). Lee Jung-hyun 26 and O'Bryant 29/12 for Sono. A 7-point home loss beats Mobis +3.0 by 4 points.
**R9. Source/timing review.** Settlement sources: https://www.newspim.com/news/view/20261110001526 (ALLOWED); https://news.jkn.co.kr/post/1084944 (ALLOWED). Card timing `WRITE_TIME_NOT_RECORDED`; self-declared phase labels: n/a. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT R3NEXT-C/V412-CHAT-G3 revision-1 -->

### Deep loss reviews (DEEPLOSS-v1)

#### Deep loss review · Ulsan Hyundai Mobis Phoebus v Goyang Sono Skygunners · Mobis +3.0

**1. Exact frozen claim.** `Mobis +3.0`, full-game endpoint as each record defined it. Triggered in 2 record(s):

| Record | Trigger role(s) | Original p (basis) | Brier | Log loss |
|---|---|---|---:|---:|
| `R3NEXT-A/Mobis_Phoebus_Goyang_Skygunners_KBL_2026_Read_Only_Research_Draft.md` | TOP_SIDE, RANK1 | NOT_ESTIMATED (QUALITATIVE) |  |  |
| `R3NEXT-B/DRAFT-003` | TOP_SIDE, RANK1 | NOT_ESTIMATED (QUALITATIVE) |  |  |

No record carried a primary p_card, frozen reference or same-row baseline; BASELINE_P comparison NOT_COMPUTABLE.

**2. Verified outcome.** Sono 86-79 Mobis (at Ulsan) (Mobis-Sono Q1 22-20 (stated), half 34-47 (stated), after Q3 57-65 (stated); derived Q2 12-27, Q3 23-18, Q4 22-21; no OT). team margin -7 with handicap +3: cover by -4. Sources in R9; evidence B; final wall-clock NOT_VERIFIED.
**3. Distribution check.** Every triggering record was qualitative (NOT_ESTIMATED), so there is no frozen distribution to place the result in. Percentile placement inside each record's printed score object is not reconstructed; the printed objects stay in the cores.
**4. Error decomposition.** Realised line distance: team margin -7 with handicap +3: cover by -4. No record had a calibrated centre or a measured effect-table row, so the miss cannot be split into reference error and adjustment error; no blame shares are invented.
**5. Research audit.** Mobis injuries to import group and home court: cited by strand A/B. Facts not re-opened here remain UNVERIFIED_AT_CUTOFF; no source in any card carries a captured retrieval receipt (chat-local research).
**6. What decided the game.** Mobis scored 12 in the second quarter (27 conceded) and trailed by 13 at half; Mobis shot 8/31 from three (26%). Lee Jung-hyun 26 and O'Bryant 29/12 for Sono. A 7-point home loss beats Mobis +3.0 by 4 points.
**7. Knowable at cutoff?** Goyang's 40 3PA/game and O'Bryant/Lee scoring were printed as risks. The final score and its timing were not knowable.
**8. Process audit.** Chat-local record; no repository reference stage, no source-audit receipts, no lineup confirmation, no freeze. Timing per record in CARD_TIMING.csv (several written after the scheduled start). Endpoint and contract definitions were correct.
**9. Verdict.** Lost by 4 points beyond the line after a 12-point Mobis second quarter; v4.12 also had the side under 50%.
**10. Cutoff-only counterfactual.** NOT_ESTIMATED: no knowable fact has a measured effect-table row, so no corrected probability is priced after the result.
**11. Failure class and recurrence.** Shared across 2 record(s) on one game: the parallel chats used overlapping public inputs, so their losses are one dependent observation, not 2 independent ones.
**12. Correction.** NO_CHANGE to any rule from one result. Procedure proposals are in AUDIT_REPORT §6 (PROPOSED_NOT_TESTED).
**13. Matched wins.** `R3NEXT-A/Mobis_Phoebus_Goyang_Skygunners_KBL_2026_Read_Only_Research_Draft.md` TOP_TOTAL Under 175.5 WIN; `R3NEXT-B/DRAFT-003` TOP_TOTAL Under 175.5 WIN. These rest on the same unvalidated construction and do not show the process worked.
**14. Honesty.** Original numbers and labels preserved; no luck claim without the arithmetic above; no invented percentages, operator terms or publication times. Preservation PASS; information closure INCOMPLETE.

<!-- END SETTLEMENT EVENT R03 revision-1 -->

<!-- BEGIN SETTLEMENT EVENT R04 revision-1 -->
## Event · Colorado Avalanche @ Toronto Maple Leafs · 2026-11-10 ET · NHL 2026-27 regular season

**Final:** Colorado 6-3 Toronto (regulation). **Periods:** COL-TOR 2-1, 1-1, 3-1; 3-3 at 4:11 of 3rd; Landeskog 5:02 (4-3), Lehkonen 17:15 (5-3), Necas empty net 17:30 (6-3). **Evidence B.** Scheduled 2026-11-11T00:00:00+00:00.

| Opened source | Audit | Field read |
|---|---|---|
| https://www.nhl.com/news/colorado-avalanche-toronto-maple-leafs-game-recap-november-10-2026 | ALLOWED | '6-3 win'; empty net at 17:30 for the 6-3 final |
| https://www.thesportsleader.com/2026/11/10/avalanche-use-late-surge-to-streak-past-maple-leafs/ | ALLOWED | 6-3; Lehkonen 'in regulation'; Necas empty net 15 s later |

<!-- BEGIN SETTLEMENT R3NEXT-A/Colorado_Avalanche_Toronto_Maple_Leafs_2026_Read_Only_Research_Draft.md revision-1 -->
### Settlement · `R3NEXT-A/Colorado_Avalanche_Toronto_Maple_Leafs_2026_Read_Only_Research_Draft.md` · Colorado Avalanche @ Toronto Maple Leafs · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `6b57db95964ca7c66c853349c53794d8155092167f21f79e79b16e299d23436b`, 20115 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/r3next/FULL/original_research/Colorado_Avalanche_Toronto_Maple_Leafs_2026_Read_Only_Research_Draft.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `TIMING_UNVERIFIED` (recorded `NOT_RECORDED`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| LEAN_SIDE | Toronto +1.5 | 0.713790 (LOCAL_MODEL) | **LOSS** | team margin -3 with handicap +1.5: cover by -1.5 | 0.509496 |
| LEAN_TOTAL | Over 6.5 | 0.530312 (LOCAL_MODEL) | **WIN** | total 9 vs 6.5: +2.5 | 0.220607 |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Toronto +1.5 (0.713790) LOSS; TOP_TOTAL Over 6.5 (0.530312) WIN; RANK1 Toronto +1.5 (0.713790) LOSS. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Colorado 6-3 Toronto (regulation); COL-TOR 2-1, 1-1, 3-1; 3-3 at 4:11 of 3rd; Landeskog 5:02 (4-3), Lehkonen 17:15 (5-3), Necas empty net 17:30 (6-3). Identity matched on teams/players, date and competition (NHL 2026-27 regular season).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Hockey rows: the result is identical under 60-minute, full-game and shootout-credited conventions, so no endpoint ambiguity changes a grade.
**R4. Rank diagnostics.** 1W/1L/0U over 2 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Colorado minus Toronto = +3; total 9. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Tied 3-3 midway through the third, Colorado scored at 5:02 and 17:15, then an empty-netter at 17:30 turned a one-goal game into a three-goal margin. Toronto +1.5 was alive until 17:15 of the third.
**R9. Source/timing review.** Settlement sources: https://www.nhl.com/news/colorado-avalanche-toronto-maple-leafs-game-recap-november-10-2026 (ALLOWED); https://www.thesportsleader.com/2026/11/10/avalanche-use-late-surge-to-streak-past-maple-leafs/ (ALLOWED). Card timing `TIMING_UNVERIFIED`; self-declared phase labels: n/a. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT R3NEXT-A/Colorado_Avalanche_Toronto_Maple_Leafs_2026_Read_Only_Research_Draft.md revision-1 -->

<!-- BEGIN SETTLEMENT R3NEXT-B/DRAFT-004 revision-1 -->
### Settlement · `R3NEXT-B/DRAFT-004` · Colorado Avalanche @ Toronto Maple Leafs · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `8449187469b4ba551801144a7078d8344fbd2d9b5d38d5da428b36748303af36`, 15777 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/r3next/COMPLETE/research_notes/DRAFT_004/Colorado_Avalanche_Toronto_Maple_Leafs_NHL_2026-11-11_READ_ONLY_DRAFT.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `TIMING_UNVERIFIED` (recorded `NOT_RECORDED`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| LEAN_SIDE | Avalanche to win | NOT_ESTIMATED (QUALITATIVE) | **WIN** | team margin +3 |  |
| LEAN_TOTAL | Over 6.5 | NOT_ESTIMATED (QUALITATIVE) | **WIN** | total 9 vs 6.5: +2.5 |  |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Avalanche to win (NOT_ESTIMATED) WIN; TOP_TOTAL Over 6.5 (NOT_ESTIMATED) WIN; RANK1 Avalanche to win (NOT_ESTIMATED) WIN. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Colorado 6-3 Toronto (regulation); COL-TOR 2-1, 1-1, 3-1; 3-3 at 4:11 of 3rd; Landeskog 5:02 (4-3), Lehkonen 17:15 (5-3), Necas empty net 17:30 (6-3). Identity matched on teams/players, date and competition (NHL 2026-27 regular season).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Hockey rows: the result is identical under 60-minute, full-game and shootout-credited conventions, so no endpoint ambiguity changes a grade.
**R4. Rank diagnostics.** 2W/0L/0U over 2 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Colorado minus Toronto = +3; total 9. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Tied 3-3 midway through the third, Colorado scored at 5:02 and 17:15, then an empty-netter at 17:30 turned a one-goal game into a three-goal margin. Toronto +1.5 was alive until 17:15 of the third.
**R9. Source/timing review.** Settlement sources: https://www.nhl.com/news/colorado-avalanche-toronto-maple-leafs-game-recap-november-10-2026 (ALLOWED); https://www.thesportsleader.com/2026/11/10/avalanche-use-late-surge-to-streak-past-maple-leafs/ (ALLOWED). Card timing `TIMING_UNVERIFIED`; self-declared phase labels: n/a. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT R3NEXT-B/DRAFT-004 revision-1 -->

<!-- BEGIN SETTLEMENT R3NEXT-C/V412-CHAT-G004 revision-1 -->
### Settlement · `R3NEXT-C/V412-CHAT-G004` · Colorado Avalanche @ Toronto Maple Leafs · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `1789cc065b4be10dad2e237e1fd040b7f8e3c3c7db83123bca418db1ac339945`, 6414 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/r3next/V412/V412-CHAT-G004.block.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `POST_SCHEDULED_START_WRITE` (recorded `2026-11-11T00:11:09Z (11 min AFTER scheduled start, per its own intake row)`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| V412 | Avalanche to win | 0.561 (V412_MODEL) | **WIN** | team margin +3 | 0.192721 |
| V412 | Toronto +1.5 | 0.615 (V412_MODEL) | **LOSS** | team margin -3 with handicap +1.5: cover by -1.5 | 0.378225 |
| V412 | Over 6.5 | 0.536 (V412_MODEL) | **WIN** | total 9 vs 6.5: +2.5 | 0.215296 |
| V412 | Under 6.5 | 0.464 (V412_MODEL) | **LOSS** | total 9 vs 6.5: +2.5 | 0.215296 |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Toronto +1.5 (0.615) LOSS; TOP_TOTAL Over 6.5 (0.536) WIN. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Colorado 6-3 Toronto (regulation); COL-TOR 2-1, 1-1, 3-1; 3-3 at 4:11 of 3rd; Landeskog 5:02 (4-3), Lehkonen 17:15 (5-3), Necas empty net 17:30 (6-3). Identity matched on teams/players, date and competition (NHL 2026-27 regular season).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Hockey rows: the result is identical under 60-minute, full-game and shootout-credited conventions, so no endpoint ambiguity changes a grade.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Colorado minus Toronto = +3; total 9. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Tied 3-3 midway through the third, Colorado scored at 5:02 and 17:15, then an empty-netter at 17:30 turned a one-goal game into a three-goal margin. Toronto +1.5 was alive until 17:15 of the third.
**R9. Source/timing review.** Settlement sources: https://www.nhl.com/news/colorado-avalanche-toronto-maple-leafs-game-recap-november-10-2026 (ALLOWED); https://www.thesportsleader.com/2026/11/10/avalanche-use-late-surge-to-streak-past-maple-leafs/ (ALLOWED). Card timing `POST_SCHEDULED_START_WRITE`; self-declared phase labels: n/a. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT R3NEXT-C/V412-CHAT-G004 revision-1 -->

### Deep loss reviews (DEEPLOSS-v1)

#### Deep loss review · Colorado Avalanche @ Toronto Maple Leafs · Toronto +1.5

**1. Exact frozen claim.** `Toronto +1.5`, full-game endpoint as each record defined it. Triggered in 2 record(s):

| Record | Trigger role(s) | Original p (basis) | Brier | Log loss |
|---|---|---|---:|---:|
| `R3NEXT-A/Colorado_Avalanche_Toronto_Maple_Leafs_2026_Read_Only_Research_Draft.md` | TOP_SIDE, RANK1 | 0.713790 (LOCAL_MODEL) | 0.509496 | 1.251029 |
| `R3NEXT-C/V412-CHAT-G004` | TOP_SIDE | 0.615 (V412_MODEL) | 0.378225 | 0.954512 |

No record carried a primary p_card, frozen reference or same-row baseline; BASELINE_P comparison NOT_COMPUTABLE.

**2. Verified outcome.** Colorado 6-3 Toronto (regulation) (COL-TOR 2-1, 1-1, 3-1; 3-3 at 4:11 of 3rd; Landeskog 5:02 (4-3), Lehkonen 17:15 (5-3), Necas empty net 17:30 (6-3)). team margin -3 with handicap +1.5: cover by -1.5. Sources in R9; evidence B; final wall-clock NOT_VERIFIED.
**3. Distribution check.** Numeric records priced this row at 0.615-0.714 (mean 0.664); a loss at those prices is a 29%-38% event under each record's own uncalibrated object. Percentile placement inside each record's printed score object is not reconstructed; the printed objects stay in the cores.
**4. Error decomposition.** Realised line distance: team margin -3 with handicap +1.5: cover by -1.5. No record had a calibrated centre or a measured effect-table row, so the miss cannot be split into reference error and adjustment error; no blame shares are invented.
**5. Research audit.** Strand A local model 71.4% with 'sensitive to goalie/empty-net and shrink choices' disclosed; v4.12 61.5%. Facts not re-opened here remain UNVERIFIED_AT_CUTOFF; no source in any card carries a captured retrieval receipt (chat-local research).
**6. What decided the game.** Tied 3-3 midway through the third, Colorado scored at 5:02 and 17:15, then an empty-netter at 17:30 turned a one-goal game into a three-goal margin. Toronto +1.5 was alive until 17:15 of the third.
**7. Knowable at cutoff?** Colorado's five recent wins by 3+ were printed (strand B). The final score and its timing were not knowable.
**8. Process audit.** Chat-local record; no repository reference stage, no source-audit receipts, no lineup confirmation, no freeze. Timing per record in CARD_TIMING.csv (several written after the scheduled start). Endpoint and contract definitions were correct.
**9. Verdict.** Alive until 17:15 of the third, then two goals including an empty-netter. A 71% price on a +1.5 puck line against a deeper team was too high; the empty-net tail was named but not priced.
**10. Cutoff-only counterfactual.** NOT_ESTIMATED: no knowable fact has a measured effect-table row, so no corrected probability is priced after the result.
**11. Failure class and recurrence.** Shared across 2 record(s) on one game: the parallel chats used overlapping public inputs, so their losses are one dependent observation, not 2 independent ones.
**12. Correction.** NO_CHANGE to any rule from one result. Procedure proposals are in AUDIT_REPORT §6 (PROPOSED_NOT_TESTED).
**13. Matched wins.** `R3NEXT-A/Colorado_Avalanche_Toronto_Maple_Leafs_2026_Read_Only_Research_Draft.md` TOP_TOTAL Over 6.5 WIN; `R3NEXT-C/V412-CHAT-G004` TOP_TOTAL Over 6.5 WIN. These rest on the same unvalidated construction and do not show the process worked.
**14. Honesty.** Original numbers and labels preserved; no luck claim without the arithmetic above; no invented percentages, operator terms or publication times. Preservation PASS; information closure INCOMPLETE.

<!-- END SETTLEMENT EVENT R04 revision-1 -->

<!-- BEGIN SETTLEMENT EVENT R06 revision-1 -->
## Event · Creighton Bluejays @ Kansas State Wildcats · 2026-11-10 CT · NCAA Division I men 2026-27

**Final:** Kansas State 89-82 Creighton. **Periods:** Halftime 40-40 per a search summary only (ESPN, BLOCKED_FOR_AI, not opened): NOT_VERIFIED; OT not indicated. **Evidence C.** Scheduled 2026-11-11T02:10:00+00:00.

| Opened source | Audit | Field read |
|---|---|---|
| https://www.kstatesports.com/news/2026/11/11/mens-basketball-rechsteiners-26-carries-k-state-past-creighton-89-82 | ALLOWED | Title only: 'Rechsteiner's 26 Carries K-State Past Creighton, 89-82' |
| https://gocreighton.com/news/2026/11/10/mens-basketball-at-kansas-state | ALLOWED | Title only: 'Men's Basketball Drops Road Opener at Kansas State' (confirms loss, no score) |

<!-- BEGIN SETTLEMENT R3NEXT-A/Creighton_Kansas_State_NCAAB_2026_READ_ONLY_RESEARCH_DRAFT.md revision-1 -->
### Settlement · `R3NEXT-A/Creighton_Kansas_State_NCAAB_2026_READ_ONLY_RESEARCH_DRAFT.md` · Creighton Bluejays @ Kansas State Wildcats · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `a6c650f58c36b756e9bb0067da4840b918bef5f8b330d89a5450540cb2f3ce9b`, 23749 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/r3next/FULL/original_research/Creighton_Kansas_State_NCAAB_2026_READ_ONLY_RESEARCH_DRAFT.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `TIMING_UNVERIFIED` (recorded `NOT_RECORDED`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| LEAN_TOTAL | Under 159.5 | 0.6796 (LOCAL_MODEL) | **LOSS** | total 171 vs 159.5: +11.5 | 0.461856 |
| LEAN_SIDE | Kansas State +3.5 | 0.5775 (LOCAL_MODEL) | **WIN** | team margin +7 with handicap +3.5: cover by +10.5 | 0.178506 |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Kansas State +3.5 (0.5775) WIN; TOP_TOTAL Under 159.5 (0.6796) LOSS; RANK1 Under 159.5 (0.6796) LOSS. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Kansas State 89-82 Creighton; Halftime 40-40 per a search summary only (ESPN, BLOCKED_FOR_AI, not opened): NOT_VERIFIED; OT not indicated. Identity matched on teams/players, date and competition (NCAA Division I men 2026-27).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Basketball rows include overtime (BK-OT-1); none occurred.
**R4. Rank diagnostics.** 1W/1L/0U over 2 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Kansas State minus Creighton = +7; total 171. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Kansas State won by seven at home behind Rechsteiner's 26 (six threes). The 171-point total was 11.5 over 159.5; Creighton's loss beat Creighton -3.5 by 10.5.
**R9. Source/timing review.** Settlement sources: https://www.kstatesports.com/news/2026/11/11/mens-basketball-rechsteiners-26-carries-k-state-past-creighton-89-82 (ALLOWED); https://gocreighton.com/news/2026/11/10/mens-basketball-at-kansas-state (ALLOWED). Card timing `TIMING_UNVERIFIED`; self-declared phase labels: n/a. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT R3NEXT-A/Creighton_Kansas_State_NCAAB_2026_READ_ONLY_RESEARCH_DRAFT.md revision-1 -->

<!-- BEGIN SETTLEMENT R3NEXT-B/DRAFT-006 revision-1 -->
### Settlement · `R3NEXT-B/DRAFT-006` · Creighton Bluejays @ Kansas State Wildcats · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `9beabe590c7841df0cb6a026778680505cede35ecd2ed3eaab165f21e5b1d37c`, 15415 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/r3next/COMPLETE/research_notes/DRAFT_006/Creighton_Kansas_State_NCAAB_2026-11-11_READ_ONLY_DRAFT.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `TIMING_UNVERIFIED` (recorded `NOT_RECORDED`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| LEAN_TOTAL | Under 159.5 | NOT_ESTIMATED (QUALITATIVE) | **LOSS** | total 171 vs 159.5: +11.5 |  |
| LEAN_SIDE | Creighton -3.5 | NOT_ESTIMATED (QUALITATIVE) | **LOSS** | team margin -7 with handicap -3.5: cover by -10.5 |  |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Creighton -3.5 (NOT_ESTIMATED) LOSS; TOP_TOTAL Under 159.5 (NOT_ESTIMATED) LOSS; RANK1 Under 159.5 (NOT_ESTIMATED) LOSS. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Kansas State 89-82 Creighton; Halftime 40-40 per a search summary only (ESPN, BLOCKED_FOR_AI, not opened): NOT_VERIFIED; OT not indicated. Identity matched on teams/players, date and competition (NCAA Division I men 2026-27).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Basketball rows include overtime (BK-OT-1); none occurred.
**R4. Rank diagnostics.** 0W/2L/0U over 2 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Kansas State minus Creighton = +7; total 171. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Kansas State won by seven at home behind Rechsteiner's 26 (six threes). The 171-point total was 11.5 over 159.5; Creighton's loss beat Creighton -3.5 by 10.5.
**R9. Source/timing review.** Settlement sources: https://www.kstatesports.com/news/2026/11/11/mens-basketball-rechsteiners-26-carries-k-state-past-creighton-89-82 (ALLOWED); https://gocreighton.com/news/2026/11/10/mens-basketball-at-kansas-state (ALLOWED). Card timing `TIMING_UNVERIFIED`; self-declared phase labels: n/a. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT R3NEXT-B/DRAFT-006 revision-1 -->

<!-- BEGIN SETTLEMENT R3NEXT-C/V412-CHAT-G006 revision-1 -->
### Settlement · `R3NEXT-C/V412-CHAT-G006` · Creighton Bluejays @ Kansas State Wildcats · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `fc8c15ab38777d26b36a769c3b705eceb5a7f185999ed4a9f5f149d819011028`, 6518 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/r3next/V412/V412-CHAT-G006.block.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `PRE_SCHEDULED_START_WRITE` (recorded `2026-11-11T02:01Z (before 02:10Z start)`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| V412 | Creighton -3.5 | 0.531 (V412_MODEL) | **LOSS** | team margin -7 with handicap -3.5: cover by -10.5 | 0.281961 |
| V412 | Kansas State +3.5 | 0.469 (V412_MODEL) | **WIN** | team margin +7 with handicap +3.5: cover by +10.5 | 0.281961 |
| V412 | Over 159.5 | 0.355 (V412_MODEL) | **WIN** | total 171 vs 159.5: +11.5 | 0.416025 |
| V412 | Under 159.5 | 0.645 (V412_MODEL) | **LOSS** | total 171 vs 159.5: +11.5 | 0.416025 |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Creighton -3.5 (0.531) LOSS; TOP_TOTAL Under 159.5 (0.645) LOSS. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Kansas State 89-82 Creighton; Halftime 40-40 per a search summary only (ESPN, BLOCKED_FOR_AI, not opened): NOT_VERIFIED; OT not indicated. Identity matched on teams/players, date and competition (NCAA Division I men 2026-27).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Basketball rows include overtime (BK-OT-1); none occurred.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Kansas State minus Creighton = +7; total 171. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Kansas State won by seven at home behind Rechsteiner's 26 (six threes). The 171-point total was 11.5 over 159.5; Creighton's loss beat Creighton -3.5 by 10.5.
**R9. Source/timing review.** Settlement sources: https://www.kstatesports.com/news/2026/11/11/mens-basketball-rechsteiners-26-carries-k-state-past-creighton-89-82 (ALLOWED); https://gocreighton.com/news/2026/11/10/mens-basketball-at-kansas-state (ALLOWED). Card timing `PRE_SCHEDULED_START_WRITE`; self-declared phase labels: n/a. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT R3NEXT-C/V412-CHAT-G006 revision-1 -->

### Deep loss reviews (DEEPLOSS-v1)

#### Deep loss review · Creighton Bluejays @ Kansas State Wildcats · Under 159.5

**1. Exact frozen claim.** `Under 159.5`, full-game endpoint as each record defined it. Triggered in 3 record(s):

| Record | Trigger role(s) | Original p (basis) | Brier | Log loss |
|---|---|---|---:|---:|
| `R3NEXT-A/Creighton_Kansas_State_NCAAB_2026_READ_ONLY_RESEARCH_DRAFT.md` | TOP_TOTAL, RANK1 | 0.6796 (LOCAL_MODEL) | 0.461856 | 1.138185 |
| `R3NEXT-B/DRAFT-006` | TOP_TOTAL, RANK1 | NOT_ESTIMATED (QUALITATIVE) |  |  |
| `R3NEXT-C/V412-CHAT-G006` | TOP_TOTAL | 0.645 (V412_MODEL) | 0.416025 | 1.035637 |

No record carried a primary p_card, frozen reference or same-row baseline; BASELINE_P comparison NOT_COMPUTABLE.

**2. Verified outcome.** Kansas State 89-82 Creighton (Halftime 40-40 per a search summary only (ESPN, BLOCKED_FOR_AI, not opened): NOT_VERIFIED; OT not indicated). total 171 vs 159.5: +11.5. Sources in R9; evidence C; final wall-clock NOT_VERIFIED.
**3. Distribution check.** Numeric records priced this row at 0.645-0.680 (mean 0.662); a loss at those prices is a 32%-36% event under each record's own uncalibrated object. Percentile placement inside each record's printed score object is not reconstructed; the printed objects stay in the cores.
**4. Error decomposition.** Realised line distance: total 171 vs 159.5: +11.5. No record had a calibrated centre or a measured effect-table row, so the miss cannot be split into reference error and adjustment error; no blame shares are invented.
**5. Research audit.** Strand A 'raw completed totals 137, 138, 134 and 173' from two-game samples: TRUE but tiny n. Facts not re-opened here remain UNVERIFIED_AT_CUTOFF; no source in any card carries a captured retrieval receipt (chat-local research).
**6. What decided the game.** Kansas State won by seven at home behind Rechsteiner's 26 (six threes). The 171-point total was 11.5 over 159.5; Creighton's loss beat Creighton -3.5 by 10.5.
**7. Knowable at cutoff?** K-State's three-point volume was named as the kill path; Rechsteiner made six. The final score and its timing were not knowable.
**8. Process audit.** Chat-local record; no repository reference stage, no source-audit receipts, no lineup confirmation, no freeze. Timing per record in CARD_TIMING.csv (several written after the scheduled start). Endpoint and contract definitions were correct.
**9. Verdict.** Highest-priced row in strand A (68.0%) and v4.12 (64.5%) on 2-4 games of current data; lost by 11.5. Should not have carried that confidence.
**10. Cutoff-only counterfactual.** NOT_ESTIMATED: no knowable fact has a measured effect-table row, so no corrected probability is priced after the result.
**11. Failure class and recurrence.** Shared across 3 record(s) on one game: the parallel chats used overlapping public inputs, so their losses are one dependent observation, not 3 independent ones.
**12. Correction.** NO_CHANGE to any rule from one result. Procedure proposals are in AUDIT_REPORT §6 (PROPOSED_NOT_TESTED).
**13. Matched wins.** `R3NEXT-A/Creighton_Kansas_State_NCAAB_2026_READ_ONLY_RESEARCH_DRAFT.md` TOP_SIDE Kansas State +3.5 WIN. These rest on the same unvalidated construction and do not show the process worked.
**14. Honesty.** Original numbers and labels preserved; no luck claim without the arithmetic above; no invented percentages, operator terms or publication times. Preservation PASS; information closure INCOMPLETE.

#### Deep loss review · Creighton Bluejays @ Kansas State Wildcats · Creighton -3.5

**1. Exact frozen claim.** `Creighton -3.5`, full-game endpoint as each record defined it. Triggered in 2 record(s):

| Record | Trigger role(s) | Original p (basis) | Brier | Log loss |
|---|---|---|---:|---:|
| `R3NEXT-B/DRAFT-006` | TOP_SIDE | NOT_ESTIMATED (QUALITATIVE) |  |  |
| `R3NEXT-C/V412-CHAT-G006` | TOP_SIDE | 0.531 (V412_MODEL) | 0.281961 | 0.757153 |

No record carried a primary p_card, frozen reference or same-row baseline; BASELINE_P comparison NOT_COMPUTABLE.

**2. Verified outcome.** Kansas State 89-82 Creighton (Halftime 40-40 per a search summary only (ESPN, BLOCKED_FOR_AI, not opened): NOT_VERIFIED; OT not indicated). team margin -7 with handicap -3.5: cover by -10.5. Sources in R9; evidence C; final wall-clock NOT_VERIFIED.
**3. Distribution check.** Numeric records priced this row at 0.531-0.531 (mean 0.531); a loss at those prices is a 47%-47% event under each record's own uncalibrated object. Percentile placement inside each record's printed score object is not reconstructed; the printed objects stay in the cores.
**4. Error decomposition.** Realised line distance: team margin -7 with handicap -3.5: cover by -10.5. No record had a calibrated centre or a measured effect-table row, so the miss cannot be split into reference error and adjustment error; no blame shares are invented.
**5. Research audit.** v4.12 'Creighton by 4.6'; strand B qualitative. Facts not re-opened here remain UNVERIFIED_AT_CUTOFF; no source in any card carries a captured retrieval receipt (chat-local research).
**6. What decided the game.** Kansas State won by seven at home behind Rechsteiner's 26 (six threes). The 171-point total was 11.5 over 159.5; Creighton's loss beat Creighton -3.5 by 10.5.
**7. Knowable at cutoff?** K-State home court and Creighton's first road game were cited. The final score and its timing were not knowable.
**8. Process audit.** Chat-local record; no repository reference stage, no source-audit receipts, no lineup confirmation, no freeze. Timing per record in CARD_TIMING.csv (several written after the scheduled start). Endpoint and contract definitions were correct.
**9. Verdict.** Creighton lost outright by 7.
**10. Cutoff-only counterfactual.** NOT_ESTIMATED: no knowable fact has a measured effect-table row, so no corrected probability is priced after the result.
**11. Failure class and recurrence.** Shared across 2 record(s) on one game: the parallel chats used overlapping public inputs, so their losses are one dependent observation, not 2 independent ones.
**12. Correction.** NO_CHANGE to any rule from one result. Procedure proposals are in AUDIT_REPORT §6 (PROPOSED_NOT_TESTED).
**13. Matched wins.** None among the triggering records.
**14. Honesty.** Original numbers and labels preserved; no luck claim without the arithmetic above; no invented percentages, operator terms or publication times. Preservation PASS; information closure INCOMPLETE.

#### Joint section · top side and top total both lost · Creighton Bluejays @ Kansas State Wildcats

Records: `R3NEXT-B/DRAFT-006`: Creighton -3.5 and Under 159.5; `R3NEXT-C/V412-CHAT-G006`: Creighton -3.5 and Under 159.5. Both legs failed on the same game state (Kansas State 89-82 Creighton). The cards' own joint-failure figures, where printed, are retained in the cores; none was calibrated, and treating the two leans as independent picks would double-count one wrong read of the game.

<!-- END SETTLEMENT EVENT R06 revision-1 -->

<!-- BEGIN SETTLEMENT EVENT R05 revision-1 -->
## Event · Colorado Eagles @ Abbotsford Canucks · 2026-11-10 PT · AHL 2026-27, native game 1029282

**Final:** Colorado 4-3 Abbotsford (shootout); 3-3 after regulation and overtime. **Periods:** COL-ABB 2-1, 0-1, 1-1, OT 0-0, SO 1-0 (Wise); Fix-Wolansky tied it 3-3 at 18:05 of 3rd. **Evidence B.** Scheduled 2026-11-11T03:00:00+00:00. Note: Both club pages are the same collector (Colorado Eagles); the earlier OurSportsCentral pages were 9/10 Oct games and are excluded. The Wednesday 11 Nov rematch (Abbotsford 4-3) is a different game.

| Opened source | Audit | Field read |
|---|---|---|
| https://www.coloradoeagles.com/news/detail/colorado-kicks-off-road-trip-with-4-3-shootout-win-over-canucks | ALLOWED | Nov 10 recap: 1-0 at 3:10, 2-0, 2-1, 2-2 at 12:59 2nd, 3-2, 3-3 at 18:05 3rd, no OT goal, Wise lone shootout goal |
| https://www.coloradoeagles.com/games | ALLOWED | Tue Nov 10 at Abbotsford 'Win 3-4 SO'; box COL 2/0/1/0/SO1, ABB 1/1/1/0/0 |

<!-- BEGIN SETTLEMENT R3NEXT-A/Colorado_Eagles_Abbotsford_Canucks_AHL_2026_READ_ONLY_RESEARCH_DRAFT.md revision-1 -->
### Settlement · `R3NEXT-A/Colorado_Eagles_Abbotsford_Canucks_AHL_2026_READ_ONLY_RESEARCH_DRAFT.md` · Colorado Eagles @ Abbotsford Canucks · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `e4a30f7e14b96f5aa32fd60f94365fde04304dea288317093d08007ca18e2199`, 23196 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/r3next/FULL/original_research/Colorado_Eagles_Abbotsford_Canucks_AHL_2026_READ_ONLY_RESEARCH_DRAFT.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `TIMING_UNVERIFIED` (recorded `NOT_RECORDED`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| LEAN_SIDE | Abbotsford to win | 0.557987 (POISSON_EXACT) | **LOSS** | team margin -1 | 0.311349 |
| INFO | Colorado Eagles to win | 0.442013 (POISSON_EXACT) | **WIN** | team margin +1 | 0.311349 |
| INFO | Over 5.5 | 0.521015 (POISSON_EXACT) | **WIN** | total 6 vs 5.5: +0.5 | 0.229427 |
| INFO | Under 5.5 | 0.478985 (POISSON_EXACT) | **LOSS** | total 6 vs 5.5: +0.5 | 0.229427 |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Abbotsford to win (0.557987) LOSS; TOP_TOTAL Over 5.5 (0.521015) WIN; RANK1 Abbotsford to win (0.557987) LOSS. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Colorado 4-3 Abbotsford (shootout); 3-3 after regulation and overtime; COL-ABB 2-1, 0-1, 1-1, OT 0-0, SO 1-0 (Wise); Fix-Wolansky tied it 3-3 at 18:05 of 3rd. Identity matched on teams/players, date and competition (AHL 2026-27, native game 1029282).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Hockey rows: the result is identical under 60-minute, full-game and shootout-credited conventions, so no endpoint ambiguity changes a grade.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Colorado minus Abbotsford (full game incl. SO) = +1; total 6. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Regulation and overtime finished 3-3 (Abbotsford tied it at 18:05 of the third); Colorado won the shootout 1-0. Goals were 6 before the shootout and 7 with the shootout credit, so Over 5.5 wins under either convention.
**R9. Source/timing review.** Settlement sources: https://www.coloradoeagles.com/news/detail/colorado-kicks-off-road-trip-with-4-3-shootout-win-over-canucks (ALLOWED); https://www.coloradoeagles.com/games (ALLOWED). Card timing `TIMING_UNVERIFIED`; self-declared phase labels: n/a. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT R3NEXT-A/Colorado_Eagles_Abbotsford_Canucks_AHL_2026_READ_ONLY_RESEARCH_DRAFT.md revision-1 -->

<!-- BEGIN SETTLEMENT R3NEXT-B/DRAFT-005 revision-1 -->
### Settlement · `R3NEXT-B/DRAFT-005` · Colorado Eagles @ Abbotsford Canucks · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `ea940e71f0bbe3bfcf38a5d04ce47aef7d81c39c3bd530b84604610cb03b698c`, 20312 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/r3next/COMPLETE/research_notes/DRAFT_005/Colorado_Eagles_Abbotsford_Canucks_AHL_2026-11-11_READ_ONLY_DRAFT.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `TIMING_UNVERIFIED` (recorded `NOT_RECORDED`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| LEAN_SIDE | Abbotsford to win | NOT_ESTIMATED (QUALITATIVE) | **LOSS** | team margin -1 |  |
| LEAN_TOTAL | Under 5.5 | NOT_ESTIMATED (QUALITATIVE) | **LOSS** | total 6 vs 5.5: +0.5 |  |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Abbotsford to win (NOT_ESTIMATED) LOSS; TOP_TOTAL Under 5.5 (NOT_ESTIMATED) LOSS; RANK1 Abbotsford to win (NOT_ESTIMATED) LOSS. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Colorado 4-3 Abbotsford (shootout); 3-3 after regulation and overtime; COL-ABB 2-1, 0-1, 1-1, OT 0-0, SO 1-0 (Wise); Fix-Wolansky tied it 3-3 at 18:05 of 3rd. Identity matched on teams/players, date and competition (AHL 2026-27, native game 1029282).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Hockey rows: the result is identical under 60-minute, full-game and shootout-credited conventions, so no endpoint ambiguity changes a grade.
**R4. Rank diagnostics.** 0W/2L/0U over 2 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Colorado minus Abbotsford (full game incl. SO) = +1; total 6. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Regulation and overtime finished 3-3 (Abbotsford tied it at 18:05 of the third); Colorado won the shootout 1-0. Goals were 6 before the shootout and 7 with the shootout credit, so Over 5.5 wins under either convention.
**R9. Source/timing review.** Settlement sources: https://www.coloradoeagles.com/news/detail/colorado-kicks-off-road-trip-with-4-3-shootout-win-over-canucks (ALLOWED); https://www.coloradoeagles.com/games (ALLOWED). Card timing `TIMING_UNVERIFIED`; self-declared phase labels: n/a. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT R3NEXT-B/DRAFT-005 revision-1 -->

<!-- BEGIN SETTLEMENT R3NEXT-C/V412-CHAT-G005 revision-1 -->
### Settlement · `R3NEXT-C/V412-CHAT-G005` · Colorado Eagles @ Abbotsford Canucks · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `42a1c46925e274c9d61eed647b049e14ba7978da5e0166b3d905379a7c5ac787`, 4861 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/r3next/V412/V412-CHAT-G005.block.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `PRE_SCHEDULED_START_WRITE` (recorded `2026-11-11T01:46:00Z (before 03:00Z start)`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| V412 | Colorado Eagles to win | 0.475 (V412_MODEL) | **WIN** | team margin +1 | 0.275625 |
| V412 | Abbotsford to win | 0.525 (V412_MODEL) | **LOSS** | team margin -1 | 0.275625 |
| V412 | Over 5.5 | 0.476 (V412_MODEL) | **WIN** | total 6 vs 5.5: +0.5 | 0.274576 |
| V412 | Under 5.5 | 0.524 (V412_MODEL) | **LOSS** | total 6 vs 5.5: +0.5 | 0.274576 |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Abbotsford to win (0.525) LOSS; TOP_TOTAL Under 5.5 (0.524) LOSS. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Colorado 4-3 Abbotsford (shootout); 3-3 after regulation and overtime; COL-ABB 2-1, 0-1, 1-1, OT 0-0, SO 1-0 (Wise); Fix-Wolansky tied it 3-3 at 18:05 of 3rd. Identity matched on teams/players, date and competition (AHL 2026-27, native game 1029282).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Hockey rows: the result is identical under 60-minute, full-game and shootout-credited conventions, so no endpoint ambiguity changes a grade.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Colorado minus Abbotsford (full game incl. SO) = +1; total 6. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Regulation and overtime finished 3-3 (Abbotsford tied it at 18:05 of the third); Colorado won the shootout 1-0. Goals were 6 before the shootout and 7 with the shootout credit, so Over 5.5 wins under either convention.
**R9. Source/timing review.** Settlement sources: https://www.coloradoeagles.com/news/detail/colorado-kicks-off-road-trip-with-4-3-shootout-win-over-canucks (ALLOWED); https://www.coloradoeagles.com/games (ALLOWED). Card timing `PRE_SCHEDULED_START_WRITE`; self-declared phase labels: n/a. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT R3NEXT-C/V412-CHAT-G005 revision-1 -->

### Deep loss reviews (DEEPLOSS-v1)

#### Deep loss review · Colorado Eagles @ Abbotsford Canucks · Abbotsford to win

**1. Exact frozen claim.** `Abbotsford to win`, full-game endpoint as each record defined it. Triggered in 3 record(s):

| Record | Trigger role(s) | Original p (basis) | Brier | Log loss |
|---|---|---|---:|---:|
| `R3NEXT-A/Colorado_Eagles_Abbotsford_Canucks_AHL_2026_READ_ONLY_RESEARCH_DRAFT.md` | TOP_SIDE, RANK1 | 0.557987 (POISSON_EXACT) | 0.311349 | 0.816416 |
| `R3NEXT-B/DRAFT-005` | TOP_SIDE, RANK1 | NOT_ESTIMATED (QUALITATIVE) |  |  |
| `R3NEXT-C/V412-CHAT-G005` | TOP_SIDE | 0.525 (V412_MODEL) | 0.275625 | 0.744440 |

No record carried a primary p_card, frozen reference or same-row baseline; BASELINE_P comparison NOT_COMPUTABLE.

**2. Verified outcome.** Colorado 4-3 Abbotsford (shootout); 3-3 after regulation and overtime (COL-ABB 2-1, 0-1, 1-1, OT 0-0, SO 1-0 (Wise); Fix-Wolansky tied it 3-3 at 18:05 of 3rd). team margin -1. Sources in R9; evidence B; final wall-clock NOT_VERIFIED.
**3. Distribution check.** Numeric records priced this row at 0.525-0.558 (mean 0.541); a loss at those prices is a 44%-48% event under each record's own uncalibrated object. Percentile placement inside each record's printed score object is not reconstructed; the printed objects stay in the cores.
**4. Error decomposition.** Realised line distance: team margin -1. No record had a calibrated centre or a measured effect-table row, so the miss cannot be split into reference error and adjustment error; no blame shares are invented.
**5. Research audit.** Abbotsford 8-3-1 and home venue: TRUE per strand A sources. Facts not re-opened here remain UNVERIFIED_AT_CUTOFF; no source in any card carries a captured retrieval receipt (chat-local research).
**6. What decided the game.** Regulation and overtime finished 3-3 (Abbotsford tied it at 18:05 of the third); Colorado won the shootout 1-0. Goals were 6 before the shootout and 7 with the shootout credit, so Over 5.5 wins under either convention.
**7. Knowable at cutoff?** The shootout coin flip is structural; strand A had 50/50 OT assignment. The final score and its timing were not knowable.
**8. Process audit.** Chat-local record; no repository reference stage, no source-audit receipts, no lineup confirmation, no freeze. Timing per record in CARD_TIMING.csv (several written after the scheduled start). Endpoint and contract definitions were correct.
**9. Verdict.** Regulation 3-3; lost in a one-round shootout. This is the one loss in the folder that is close to pure variance (55.8% vs a 3-3 game decided by one shootout goal).
**10. Cutoff-only counterfactual.** NOT_ESTIMATED: no knowable fact has a measured effect-table row, so no corrected probability is priced after the result.
**11. Failure class and recurrence.** Shared across 3 record(s) on one game: the parallel chats used overlapping public inputs, so their losses are one dependent observation, not 3 independent ones.
**12. Correction.** NO_CHANGE to any rule from one result. Procedure proposals are in AUDIT_REPORT §6 (PROPOSED_NOT_TESTED).
**13. Matched wins.** `R3NEXT-A/Colorado_Eagles_Abbotsford_Canucks_AHL_2026_READ_ONLY_RESEARCH_DRAFT.md` TOP_TOTAL Over 5.5 WIN. These rest on the same unvalidated construction and do not show the process worked.
**14. Honesty.** Original numbers and labels preserved; no luck claim without the arithmetic above; no invented percentages, operator terms or publication times. Preservation PASS; information closure INCOMPLETE.

#### Deep loss review · Colorado Eagles @ Abbotsford Canucks · Under 5.5

**1. Exact frozen claim.** `Under 5.5`, full-game endpoint as each record defined it. Triggered in 2 record(s):

| Record | Trigger role(s) | Original p (basis) | Brier | Log loss |
|---|---|---|---:|---:|
| `R3NEXT-B/DRAFT-005` | TOP_TOTAL | NOT_ESTIMATED (QUALITATIVE) |  |  |
| `R3NEXT-C/V412-CHAT-G005` | TOP_TOTAL | 0.524 (V412_MODEL) | 0.274576 | 0.742337 |

No record carried a primary p_card, frozen reference or same-row baseline; BASELINE_P comparison NOT_COMPUTABLE.

**2. Verified outcome.** Colorado 4-3 Abbotsford (shootout); 3-3 after regulation and overtime (COL-ABB 2-1, 0-1, 1-1, OT 0-0, SO 1-0 (Wise); Fix-Wolansky tied it 3-3 at 18:05 of 3rd). total 6 vs 5.5: +0.5. Sources in R9; evidence B; final wall-clock NOT_VERIFIED.
**3. Distribution check.** Numeric records priced this row at 0.524-0.524 (mean 0.524); a loss at those prices is a 48%-48% event under each record's own uncalibrated object. Percentile placement inside each record's printed score object is not reconstructed; the printed objects stay in the cores.
**4. Error decomposition.** Realised line distance: total 6 vs 5.5: +0.5. No record had a calibrated centre or a measured effect-table row, so the miss cannot be split into reference error and adjustment error; no blame shares are invented.
**5. Research audit.** Colorado L5 4.8 combined goals: as cited. Facts not re-opened here remain UNVERIFIED_AT_CUTOFF; no source in any card carries a captured retrieval receipt (chat-local research).
**6. What decided the game.** Regulation and overtime finished 3-3 (Abbotsford tied it at 18:05 of the third); Colorado won the shootout 1-0. Goals were 6 before the shootout and 7 with the shootout credit, so Over 5.5 wins under either convention.
**7. Knowable at cutoff?** Two current-season H2H totals were 7 (strand A). The final score and its timing were not knowable.
**8. Process audit.** Chat-local record; no repository reference stage, no source-audit receipts, no lineup confirmation, no freeze. Timing per record in CARD_TIMING.csv (several written after the scheduled start). Endpoint and contract definitions were correct.
**9. Verdict.** Six goals before the shootout; Over under every convention.
**10. Cutoff-only counterfactual.** NOT_ESTIMATED: no knowable fact has a measured effect-table row, so no corrected probability is priced after the result.
**11. Failure class and recurrence.** Shared across 2 record(s) on one game: the parallel chats used overlapping public inputs, so their losses are one dependent observation, not 2 independent ones.
**12. Correction.** NO_CHANGE to any rule from one result. Procedure proposals are in AUDIT_REPORT §6 (PROPOSED_NOT_TESTED).
**13. Matched wins.** None among the triggering records.
**14. Honesty.** Original numbers and labels preserved; no luck claim without the arithmetic above; no invented percentages, operator terms or publication times. Preservation PASS; information closure INCOMPLETE.

#### Joint section · top side and top total both lost · Colorado Eagles @ Abbotsford Canucks

Records: `R3NEXT-B/DRAFT-005`: Abbotsford to win and Under 5.5; `R3NEXT-C/V412-CHAT-G005`: Abbotsford to win and Under 5.5. Both legs failed on the same game state (Colorado 4-3 Abbotsford (shootout); 3-3 after regulation and overtime). The cards' own joint-failure figures, where printed, are retained in the cores; none was calibrated, and treating the two leans as independent picks would double-count one wrong read of the game.

<!-- END SETTLEMENT EVENT R05 revision-1 -->

<!-- BEGIN SETTLEMENT EVENT R07 revision-1 -->
## Event · Akita Northern Happinets v Ibaraki Robots · 2026-11-11 · B.LEAGUE PREMIER 2026-27, ScheduleKey 506570

**Final:** Ibaraki 95-83 Akita (at Akita). **Periods:** Akita-Ibaraki 22-22, 28-22, 10-19, 23-32; half 50-44 Akita; no OT. **Evidence B.** Scheduled 2026-11-11T10:05:00+00:00. Same scheduled start as R08 (10:05Z); owner's request order (DRAFT-007 / V412 G007 before G008) breaks the tie.

| Opened source | Audit | Field read |
|---|---|---|
| https://northern-happinets.com/news/detail/id=23107 | ALLOWED | '83 - 95'; quarters 22-22, 28-22, 10-19, 23-32; '19:05 試合開始' |
| https://www.ibarakirobots.win/topics_detail42/id=25726 | ALLOWED | Post-game comments confirm Ibaraki win; no score in text |

<!-- BEGIN SETTLEMENT R3NEXT-A/Akita_Ibaraki_BPremier_2026_v24.15_READ_ONLY_RESEARCH_DRAFT.md revision-1 -->
### Settlement · `R3NEXT-A/Akita_Ibaraki_BPremier_2026_v24.15_READ_ONLY_RESEARCH_DRAFT.md` · Akita Northern Happinets v Ibaraki Robots · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `7286f72d2aafdbcfe55b297150151e5acb1e9339a1f9249c76680c46befa67ce`, 17541 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/r3next/FULL/original_research/Akita_Ibaraki_BPremier_2026_v24.15_READ_ONLY_RESEARCH_DRAFT.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `TIMING_UNVERIFIED` (recorded `NOT_RECORDED`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| LEAN_SIDE | Ibaraki +1.5 | 0.700 (LOCAL_DIAGNOSTIC) | **WIN** | team margin +12 with handicap +1.5: cover by +13.5 | 0.090000 |
| INFO | Akita -1.5 | 0.300 (LOCAL_DIAGNOSTIC) | **LOSS** | team margin -12 with handicap -1.5: cover by -13.5 | 0.090000 |
| INFO | Over 167.5 | 0.531 (LOCAL_DIAGNOSTIC) | **WIN** | total 178 vs 167.5: +10.5 | 0.219961 |
| INFO | Under 167.5 | 0.469 (LOCAL_DIAGNOSTIC) | **LOSS** | total 178 vs 167.5: +10.5 | 0.219961 |
| INFO | Ibaraki to win | 0.664 (LOCAL_DIAGNOSTIC) | **WIN** | team margin +12 | 0.112896 |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Ibaraki +1.5 (0.700) WIN; TOP_TOTAL Over 167.5 (0.531) WIN; RANK1 Ibaraki +1.5 (0.700) WIN. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Ibaraki 95-83 Akita (at Akita); Akita-Ibaraki 22-22, 28-22, 10-19, 23-32; half 50-44 Akita; no OT. Identity matched on teams/players, date and competition (B.LEAGUE PREMIER 2026-27, ScheduleKey 506570).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Basketball rows include overtime (BK-OT-1); none occurred.
**R4. Rank diagnostics.** 3W/2L/0U over 5 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Akita minus Ibaraki = -12; total 178. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Akita led 50-44 at half, then scored 10 in the third quarter (Ibaraki 19) and lost the fourth 23-32. The 178-point total cleared 167.5 by 10.5; the second-half 51-33 Ibaraki run made the +1.5 side comfortable.
**R9. Source/timing review.** Settlement sources: https://northern-happinets.com/news/detail/id=23107 (ALLOWED); https://www.ibarakirobots.win/topics_detail42/id=25726 (ALLOWED). Card timing `TIMING_UNVERIFIED`; self-declared phase labels: n/a. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT R3NEXT-A/Akita_Ibaraki_BPremier_2026_v24.15_READ_ONLY_RESEARCH_DRAFT.md revision-1 -->

<!-- BEGIN SETTLEMENT R3NEXT-B/DRAFT-007 revision-1 -->
### Settlement · `R3NEXT-B/DRAFT-007` · Akita Northern Happinets v Ibaraki Robots · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `3fadf3f89a1b5540adffbca2526fe21c968c4471d6120d0da53c93e5412bc147`, 15136 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/r3next/COMPLETE/research_notes/DRAFT_007/Akita_Happinets_Ibaraki_Robots_BPREMIER_2026-11-11_v24.15_READ_ONLY_DRAFT.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `TIMING_UNVERIFIED` (recorded `NOT_RECORDED`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| LEAN_SIDE | Ibaraki +1.5 | NOT_ESTIMATED (QUALITATIVE) | **WIN** | team margin +12 with handicap +1.5: cover by +13.5 |  |
| LEAN_TOTAL | Under 167.5 | NOT_ESTIMATED (QUALITATIVE) | **LOSS** | total 178 vs 167.5: +10.5 |  |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Ibaraki +1.5 (NOT_ESTIMATED) WIN; TOP_TOTAL Under 167.5 (NOT_ESTIMATED) LOSS; RANK1 Ibaraki +1.5 (NOT_ESTIMATED) WIN. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Ibaraki 95-83 Akita (at Akita); Akita-Ibaraki 22-22, 28-22, 10-19, 23-32; half 50-44 Akita; no OT. Identity matched on teams/players, date and competition (B.LEAGUE PREMIER 2026-27, ScheduleKey 506570).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Basketball rows include overtime (BK-OT-1); none occurred.
**R4. Rank diagnostics.** 1W/1L/0U over 2 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Akita minus Ibaraki = -12; total 178. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Akita led 50-44 at half, then scored 10 in the third quarter (Ibaraki 19) and lost the fourth 23-32. The 178-point total cleared 167.5 by 10.5; the second-half 51-33 Ibaraki run made the +1.5 side comfortable.
**R9. Source/timing review.** Settlement sources: https://northern-happinets.com/news/detail/id=23107 (ALLOWED); https://www.ibarakirobots.win/topics_detail42/id=25726 (ALLOWED). Card timing `TIMING_UNVERIFIED`; self-declared phase labels: n/a. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT R3NEXT-B/DRAFT-007 revision-1 -->

<!-- BEGIN SETTLEMENT R3NEXT-C/V412-CHAT-G007 revision-1 -->
### Settlement · `R3NEXT-C/V412-CHAT-G007` · Akita Northern Happinets v Ibaraki Robots · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `58eebbf1074e74a0fa8b846fc4112e67d30f811cc4dc451b02b881c4460d81c8`, 5304 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/r3next/V412/V412-CHAT-G007.block.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `PRE_SCHEDULED_START_WRITE` (recorded `2026-11-11T09:54:59Z (before 10:05Z start)`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| V412 | Akita -1.5 | 0.208 (V412_MODEL) | **LOSS** | team margin -12 with handicap -1.5: cover by -13.5 | 0.043264 |
| V412 | Ibaraki +1.5 | 0.792 (V412_MODEL) | **WIN** | team margin +12 with handicap +1.5: cover by +13.5 | 0.043264 |
| V412 | Over 167.5 | 0.456 (V412_MODEL) | **WIN** | total 178 vs 167.5: +10.5 | 0.295936 |
| V412 | Under 167.5 | 0.544 (V412_MODEL) | **LOSS** | total 178 vs 167.5: +10.5 | 0.295936 |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Ibaraki +1.5 (0.792) WIN; TOP_TOTAL Under 167.5 (0.544) LOSS. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Ibaraki 95-83 Akita (at Akita); Akita-Ibaraki 22-22, 28-22, 10-19, 23-32; half 50-44 Akita; no OT. Identity matched on teams/players, date and competition (B.LEAGUE PREMIER 2026-27, ScheduleKey 506570).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Basketball rows include overtime (BK-OT-1); none occurred.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Akita minus Ibaraki = -12; total 178. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Akita led 50-44 at half, then scored 10 in the third quarter (Ibaraki 19) and lost the fourth 23-32. The 178-point total cleared 167.5 by 10.5; the second-half 51-33 Ibaraki run made the +1.5 side comfortable.
**R9. Source/timing review.** Settlement sources: https://northern-happinets.com/news/detail/id=23107 (ALLOWED); https://www.ibarakirobots.win/topics_detail42/id=25726 (ALLOWED). Card timing `PRE_SCHEDULED_START_WRITE`; self-declared phase labels: n/a. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT R3NEXT-C/V412-CHAT-G007 revision-1 -->

### Deep loss reviews (DEEPLOSS-v1)

#### Deep loss review · Akita Northern Happinets v Ibaraki Robots · Under 167.5

**1. Exact frozen claim.** `Under 167.5`, full-game endpoint as each record defined it. Triggered in 2 record(s):

| Record | Trigger role(s) | Original p (basis) | Brier | Log loss |
|---|---|---|---:|---:|
| `R3NEXT-B/DRAFT-007` | TOP_TOTAL | NOT_ESTIMATED (QUALITATIVE) |  |  |
| `R3NEXT-C/V412-CHAT-G007` | TOP_TOTAL | 0.544 (V412_MODEL) | 0.295936 | 0.785262 |

No record carried a primary p_card, frozen reference or same-row baseline; BASELINE_P comparison NOT_COMPUTABLE.

**2. Verified outcome.** Ibaraki 95-83 Akita (at Akita) (Akita-Ibaraki 22-22, 28-22, 10-19, 23-32; half 50-44 Akita; no OT). total 178 vs 167.5: +10.5. Sources in R9; evidence B; final wall-clock NOT_VERIFIED.
**3. Distribution check.** Numeric records priced this row at 0.544-0.544 (mean 0.544); a loss at those prices is a 46%-46% event under each record's own uncalibrated object. Percentile placement inside each record's printed score object is not reconstructed; the printed objects stay in the cores.
**4. Error decomposition.** Realised line distance: total 178 vs 167.5: +10.5. No record had a calibrated centre or a measured effect-table row, so the miss cannot be split into reference error and adjustment error; no blame shares are invented.
**5. Research audit.** Strand B qualitative; v4.12 54.4%. Facts not re-opened here remain UNVERIFIED_AT_CUTOFF; no source in any card carries a captured retrieval receipt (chat-local research).
**6. What decided the game.** Akita led 50-44 at half, then scored 10 in the third quarter (Ibaraki 19) and lost the fourth 23-32. The 178-point total cleared 167.5 by 10.5; the second-half 51-33 Ibaraki run made the +1.5 side comfortable.
**7. Knowable at cutoff?** Akita's last five averaged 189.4 combined (printed). The final score and its timing were not knowable.
**8. Process audit.** Chat-local record; no repository reference stage, no source-audit receipts, no lineup confirmation, no freeze. Timing per record in CARD_TIMING.csv (several written after the scheduled start). Endpoint and contract definitions were correct.
**9. Verdict.** Lost by 10.5 points; the printed L5 evidence contradicted the lean.
**10. Cutoff-only counterfactual.** NOT_ESTIMATED: no knowable fact has a measured effect-table row, so no corrected probability is priced after the result.
**11. Failure class and recurrence.** Shared across 2 record(s) on one game: the parallel chats used overlapping public inputs, so their losses are one dependent observation, not 2 independent ones.
**12. Correction.** NO_CHANGE to any rule from one result. Procedure proposals are in AUDIT_REPORT §6 (PROPOSED_NOT_TESTED).
**13. Matched wins.** `R3NEXT-B/DRAFT-007` RANK1 Ibaraki +1.5 WIN; `R3NEXT-B/DRAFT-007` TOP_SIDE Ibaraki +1.5 WIN; `R3NEXT-C/V412-CHAT-G007` TOP_SIDE Ibaraki +1.5 WIN. These rest on the same unvalidated construction and do not show the process worked.
**14. Honesty.** Original numbers and labels preserved; no luck claim without the arithmetic above; no invented percentages, operator terms or publication times. Preservation PASS; information closure INCOMPLETE.

<!-- END SETTLEMENT EVENT R07 revision-1 -->

<!-- BEGIN SETTLEMENT EVENT R08 revision-1 -->
## Event · Hiroshima Dragonflies v Sendai 89ers · 2026-11-11 · B.LEAGUE PREMIER 2026-27, ScheduleKey 506574

**Final:** Sendai 106-91 Hiroshima (at Hiroshima). **Periods:** Quarter table not rendered; club report: Hiroshima conceded 60 in the first half (narrative); no OT indicated. **Evidence B.** Scheduled 2026-11-11T10:05:00+00:00.

| Opened source | Audit | Field read |
|---|---|---|
| https://www.bleague.jp/game_detail/?ScheduleKey=506574&tab=1 | ALLOWED | FINAL 91 (HOME 広島) 106 (AWAY 仙台); 19:05 TIP OFF |
| https://hiroshimadragonflies.com/topics_detail39/id=25018 | ALLOWED | Club report: '前半だけで60失点'; no score line |

<!-- BEGIN SETTLEMENT R3NEXT-A/Hiroshima_Dragonflies_Sendai_89ers_BPremier_2026_v24.15_READ_ONLY_RESEARCH_DRAFT.md revision-1 -->
### Settlement · `R3NEXT-A/Hiroshima_Dragonflies_Sendai_89ers_BPremier_2026_v24.15_READ_ONLY_RESEARCH_DRAFT.md` · Hiroshima Dragonflies v Sendai 89ers · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `b5d473fb821b24b2e8a9f0d05c1f49152cfe3b1b860adff0bb75ac9d00f4edf3`, 14077 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/r3next/FULL/original_research/Hiroshima_Dragonflies_Sendai_89ers_BPremier_2026_v24.15_READ_ONLY_RESEARCH_DRAFT.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `TIMING_UNVERIFIED` (recorded `NOT_RECORDED`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| LEAN_TOTAL | Under 170.5 | 0.54621 (LOCAL_DIAGNOSTIC) | **LOSS** | total 197 vs 170.5: +26.5 | 0.298345 |
| INFO | Sendai +2.5 | 0.50374 (LOCAL_DIAGNOSTIC) | **WIN** | team margin +15 with handicap +2.5: cover by +17.5 | 0.246274 |
| INFO | Hiroshima -2.5 | 0.49626 (LOCAL_DIAGNOSTIC) | **LOSS** | team margin -15 with handicap -2.5: cover by -17.5 | 0.246274 |
| INFO | Over 170.5 | 0.45379 (LOCAL_DIAGNOSTIC) | **WIN** | total 197 vs 170.5: +26.5 | 0.298345 |
| INFO | Hiroshima to win | 0.56276 (LOCAL_DIAGNOSTIC) | **LOSS** | team margin -15 | 0.316699 |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Hiroshima to win (0.56276) LOSS; TOP_TOTAL Under 170.5 (0.54621) LOSS; RANK1 Under 170.5 (0.54621) LOSS. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Sendai 106-91 Hiroshima (at Hiroshima); Quarter table not rendered; club report: Hiroshima conceded 60 in the first half (narrative); no OT indicated. Identity matched on teams/players, date and competition (B.LEAGUE PREMIER 2026-27, ScheduleKey 506574).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Basketball rows include overtime (BK-OT-1); none occurred.
**R4. Rank diagnostics.** 2W/3L/0U over 5 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Hiroshima minus Sendai = -15; total 197. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Sendai scored 60 in the first half alone and 106 in total; the 197-point total beat 170.5 by 26.5. Sendai won by 15 as the road side.
**R9. Source/timing review.** Settlement sources: https://www.bleague.jp/game_detail/?ScheduleKey=506574&tab=1 (ALLOWED); https://hiroshimadragonflies.com/topics_detail39/id=25018 (ALLOWED). Card timing `TIMING_UNVERIFIED`; self-declared phase labels: n/a. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT R3NEXT-A/Hiroshima_Dragonflies_Sendai_89ers_BPremier_2026_v24.15_READ_ONLY_RESEARCH_DRAFT.md revision-1 -->

<!-- BEGIN SETTLEMENT R3NEXT-B/DRAFT-008 revision-1 -->
### Settlement · `R3NEXT-B/DRAFT-008` · Hiroshima Dragonflies v Sendai 89ers · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `17120c1744c9939851ecf4ea3f0205c7ea43917cb824ba0d41ddc290a62a022c`, 12466 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/r3next/COMPLETE/research_notes/DRAFT_008/Hiroshima_Dragonflies_Sendai_89ers_BPREMIER_2026-11-11_v24.15_READ_ONLY_DRAFT.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `TIMING_UNVERIFIED` (recorded `NOT_RECORDED`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| LEAN_TOTAL | Under 170.5 | NOT_ESTIMATED (QUALITATIVE) | **LOSS** | total 197 vs 170.5: +26.5 |  |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_TOTAL Under 170.5 (NOT_ESTIMATED) LOSS; RANK1 Under 170.5 (NOT_ESTIMATED) LOSS. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Sendai 106-91 Hiroshima (at Hiroshima); Quarter table not rendered; club report: Hiroshima conceded 60 in the first half (narrative); no OT indicated. Identity matched on teams/players, date and competition (B.LEAGUE PREMIER 2026-27, ScheduleKey 506574).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Basketball rows include overtime (BK-OT-1); none occurred.
**R4. Rank diagnostics.** 0W/1L/0U over 1 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Hiroshima minus Sendai = -15; total 197. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Sendai scored 60 in the first half alone and 106 in total; the 197-point total beat 170.5 by 26.5. Sendai won by 15 as the road side.
**R9. Source/timing review.** Settlement sources: https://www.bleague.jp/game_detail/?ScheduleKey=506574&tab=1 (ALLOWED); https://hiroshimadragonflies.com/topics_detail39/id=25018 (ALLOWED). Card timing `TIMING_UNVERIFIED`; self-declared phase labels: n/a. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT R3NEXT-B/DRAFT-008 revision-1 -->

<!-- BEGIN SETTLEMENT R3NEXT-C/V412-CHAT-G008 revision-1 -->
### Settlement · `R3NEXT-C/V412-CHAT-G008` · Hiroshima Dragonflies v Sendai 89ers · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `49b6cc6290154d1c5c8271ad90343aa2116fa44232b6d2e09f0c4d205c17846c`, 5847 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/r3next/V412/V412-CHAT-G008.block.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `POST_SCHEDULED_START_WRITE` (recorded `2026-11-11T10:07:36Z (2.6 min AFTER scheduled start)`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| V412 | Hiroshima -2.5 | 0.395 (V412_MODEL) | **LOSS** | team margin -15 with handicap -2.5: cover by -17.5 | 0.156025 |
| V412 | Sendai +2.5 | 0.605 (V412_MODEL) | **WIN** | team margin +15 with handicap +2.5: cover by +17.5 | 0.156025 |
| V412 | Over 170.5 | 0.470 (V412_MODEL) | **WIN** | total 197 vs 170.5: +26.5 | 0.280900 |
| V412 | Under 170.5 | 0.530 (V412_MODEL) | **LOSS** | total 197 vs 170.5: +26.5 | 0.280900 |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Sendai +2.5 (0.605) WIN; TOP_TOTAL Under 170.5 (0.530) LOSS. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Sendai 106-91 Hiroshima (at Hiroshima); Quarter table not rendered; club report: Hiroshima conceded 60 in the first half (narrative); no OT indicated. Identity matched on teams/players, date and competition (B.LEAGUE PREMIER 2026-27, ScheduleKey 506574).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Basketball rows include overtime (BK-OT-1); none occurred.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Hiroshima minus Sendai = -15; total 197. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Sendai scored 60 in the first half alone and 106 in total; the 197-point total beat 170.5 by 26.5. Sendai won by 15 as the road side.
**R9. Source/timing review.** Settlement sources: https://www.bleague.jp/game_detail/?ScheduleKey=506574&tab=1 (ALLOWED); https://hiroshimadragonflies.com/topics_detail39/id=25018 (ALLOWED). Card timing `POST_SCHEDULED_START_WRITE`; self-declared phase labels: n/a. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT R3NEXT-C/V412-CHAT-G008 revision-1 -->

### Deep loss reviews (DEEPLOSS-v1)

#### Deep loss review · Hiroshima Dragonflies v Sendai 89ers · Hiroshima to win

**1. Exact frozen claim.** `Hiroshima to win`, full-game endpoint as each record defined it. Triggered in 1 record(s):

| Record | Trigger role(s) | Original p (basis) | Brier | Log loss |
|---|---|---|---:|---:|
| `R3NEXT-A/Hiroshima_Dragonflies_Sendai_89ers_BPremier_2026_v24.15_READ_ONLY_RESEARCH_DRAFT.md` | TOP_SIDE | 0.56276 (LOCAL_DIAGNOSTIC) | 0.316699 | 0.827273 |

No record carried a primary p_card, frozen reference or same-row baseline; BASELINE_P comparison NOT_COMPUTABLE.

**2. Verified outcome.** Sendai 106-91 Hiroshima (at Hiroshima) (Quarter table not rendered; club report: Hiroshima conceded 60 in the first half (narrative); no OT indicated). team margin -15. Sources in R9; evidence B; final wall-clock NOT_VERIFIED.
**3. Distribution check.** Numeric records priced this row at 0.563-0.563 (mean 0.563); a loss at those prices is a 44%-44% event under each record's own uncalibrated object. Percentile placement inside each record's printed score object is not reconstructed; the printed objects stay in the cores.
**4. Error decomposition.** Realised line distance: team margin -15. No record had a calibrated centre or a measured effect-table row, so the miss cannot be split into reference error and adjustment error; no blame shares are invented.
**5. Research audit.** Hiroshima 13-1 vs Sendai 12-4: TRUE per strand A official stats (10 Nov 22:46 JST). Facts not re-opened here remain UNVERIFIED_AT_CUTOFF; no source in any card carries a captured retrieval receipt (chat-local research).
**6. What decided the game.** Sendai scored 60 in the first half alone and 106 in total; the 197-point total beat 170.5 by 26.5. Sendai won by 15 as the road side.
**7. Knowable at cutoff?** Sendai's 107-point previous game and 3PT volume were printed. The final score and its timing were not knowable.
**8. Process audit.** Chat-local record; no repository reference stage, no source-audit receipts, no lineup confirmation, no freeze. Timing per record in CARD_TIMING.csv (several written after the scheduled start). Endpoint and contract definitions were correct.
**9. Verdict.** Informational 56% row; Sendai won by 15 on the road.
**10. Cutoff-only counterfactual.** NOT_ESTIMATED: no knowable fact has a measured effect-table row, so no corrected probability is priced after the result.
**11. Failure class and recurrence.** Shared across 1 record(s) on one game: the parallel chats used overlapping public inputs, so their losses are one dependent observation, not 1 independent ones.
**12. Correction.** NO_CHANGE to any rule from one result. Procedure proposals are in AUDIT_REPORT §6 (PROPOSED_NOT_TESTED).
**13. Matched wins.** None among the triggering records.
**14. Honesty.** Original numbers and labels preserved; no luck claim without the arithmetic above; no invented percentages, operator terms or publication times. Preservation PASS; information closure INCOMPLETE.

#### Deep loss review · Hiroshima Dragonflies v Sendai 89ers · Under 170.5

**1. Exact frozen claim.** `Under 170.5`, full-game endpoint as each record defined it. Triggered in 3 record(s):

| Record | Trigger role(s) | Original p (basis) | Brier | Log loss |
|---|---|---|---:|---:|
| `R3NEXT-A/Hiroshima_Dragonflies_Sendai_89ers_BPremier_2026_v24.15_READ_ONLY_RESEARCH_DRAFT.md` | TOP_TOTAL, RANK1 | 0.54621 (LOCAL_DIAGNOSTIC) | 0.298345 | 0.790121 |
| `R3NEXT-B/DRAFT-008` | TOP_TOTAL, RANK1 | NOT_ESTIMATED (QUALITATIVE) |  |  |
| `R3NEXT-C/V412-CHAT-G008` | TOP_TOTAL | 0.530 (V412_MODEL) | 0.280900 | 0.755023 |

No record carried a primary p_card, frozen reference or same-row baseline; BASELINE_P comparison NOT_COMPUTABLE.

**2. Verified outcome.** Sendai 106-91 Hiroshima (at Hiroshima) (Quarter table not rendered; club report: Hiroshima conceded 60 in the first half (narrative); no OT indicated). total 197 vs 170.5: +26.5. Sources in R9; evidence B; final wall-clock NOT_VERIFIED.
**3. Distribution check.** Numeric records priced this row at 0.530-0.546 (mean 0.538); a loss at those prices is a 45%-47% event under each record's own uncalibrated object. Percentile placement inside each record's printed score object is not reconstructed; the printed objects stay in the cores.
**4. Error decomposition.** Realised line distance: total 197 vs 170.5: +26.5. No record had a calibrated centre or a measured effect-table row, so the miss cannot be split into reference error and adjustment error; no blame shares are invented.
**5. Research audit.** Season cross-match 168.45: arithmetic TRUE; Sendai's last game 107 points printed. Facts not re-opened here remain UNVERIFIED_AT_CUTOFF; no source in any card carries a captured retrieval receipt (chat-local research).
**6. What decided the game.** Sendai scored 60 in the first half alone and 106 in total; the 197-point total beat 170.5 by 26.5. Sendai won by 15 as the road side.
**7. Knowable at cutoff?** Offence-only scoring summed to 178.0 (printed as the contrary case). The final score and its timing were not knowable.
**8. Process audit.** Chat-local record; no repository reference stage, no source-audit receipts, no lineup confirmation, no freeze. Timing per record in CARD_TIMING.csv (several written after the scheduled start). Endpoint and contract definitions were correct.
**9. Verdict.** Lost by 26.5 points; the 60-point first half was outside every printed scenario (sensitivity range 164-172).
**10. Cutoff-only counterfactual.** NOT_ESTIMATED: no knowable fact has a measured effect-table row, so no corrected probability is priced after the result.
**11. Failure class and recurrence.** Shared across 3 record(s) on one game: the parallel chats used overlapping public inputs, so their losses are one dependent observation, not 3 independent ones.
**12. Correction.** NO_CHANGE to any rule from one result. Procedure proposals are in AUDIT_REPORT §6 (PROPOSED_NOT_TESTED).
**13. Matched wins.** `R3NEXT-C/V412-CHAT-G008` TOP_SIDE Sendai +2.5 WIN. These rest on the same unvalidated construction and do not show the process worked.
**14. Honesty.** Original numbers and labels preserved; no luck claim without the arithmetic above; no invented percentages, operator terms or publication times. Preservation PASS; information closure INCOMPLETE.

#### Joint section · top side and top total both lost · Hiroshima Dragonflies v Sendai 89ers

Records: `R3NEXT-A/Hiroshima_Dragonflies_Sendai_89ers_BPremier_2026_v24.15_READ_ONLY_RESEARCH_DRAFT.md`: Hiroshima to win and Under 170.5. Both legs failed on the same game state (Sendai 106-91 Hiroshima (at Hiroshima)). The cards' own joint-failure figures, where printed, are retained in the cores; none was calibrated, and treating the two leans as independent picks would double-count one wrong read of the game.

<!-- END SETTLEMENT EVENT R08 revision-1 -->

<!-- BEGIN SETTLEMENT EVENT R09 revision-1 -->
## Event · Urawa Red Diamonds v Cerezo Osaka · 2026-11-11 · J.League YBC Levain Cup 2026/27 QF first leg (match 111102)

**Final:** Urawa 2-0 Cerezo Osaka (HT 0-0). **Periods:** Goals Ueki 74', Komori 90+4'; first half 0-0; corner kicks NOT FOUND. **Evidence A.** Scheduled 2026-11-11T10:30:00+00:00.

| Opened source | Audit | Field read |
|---|---|---|
| https://www.jleague.jp/match/leaguecup/2026/111102/ | ALLOWED | Score 2-0; 前半 'ゴールはありません'; 19:30 KO; stats section not in text |
| https://web.gekisaka.jp/news/jleaguecup/detail/?462996-462996-fl= | ALLOWED | '浦和 2-0(前半0-0)C大阪'; 74分, 90分+4; published 26/11/11 21:30 |

<!-- BEGIN SETTLEMENT R3NEXT-A/Urawa_Reds_Cerezo_Osaka_LevainCup_2026_v24.15_RESEARCH_DRAFT.md revision-1 -->
### Settlement · `R3NEXT-A/Urawa_Reds_Cerezo_Osaka_LevainCup_2026_v24.15_RESEARCH_DRAFT.md` · Urawa Red Diamonds v Cerezo Osaka · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `8b35023a88ee98cbb51fa1805500a6dc96e86737fb8d4c11beb8427009560fac`, 16554 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/r3next/FULL/original_research/Urawa_Reds_Cerezo_Osaka_LevainCup_2026_v24.15_RESEARCH_DRAFT.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `TIMING_UNVERIFIED` (recorded `NOT_RECORDED`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| LEAN_TOTAL | First half Over 0.5 goals | NOT_ESTIMATED (QUALITATIVE) | **LOSS** | total 0 vs 0.5: -0.5 |  |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_TOTAL First half Over 0.5 goals (NOT_ESTIMATED) LOSS; RANK1 First half Over 0.5 goals (NOT_ESTIMATED) LOSS. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Urawa 2-0 Cerezo Osaka (HT 0-0); Goals Ueki 74', Komori 90+4'; first half 0-0; corner kicks NOT FOUND. Identity matched on teams/players, date and competition (J.League YBC Levain Cup 2026/27 QF first leg (match 111102)).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Soccer rows: 90 minutes plus stoppage; corners unresolved.
**R4. Rank diagnostics.** 0W/1L/0U over 1 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Urawa minus Cerezo = +2; total 2. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** No goal in the first half; Urawa scored at 74' and 90+4'. Two goals in total; the corner count was not found on any permitted page, so both corner rows stay UNRESOLVED.
**R9. Source/timing review.** Settlement sources: https://www.jleague.jp/match/leaguecup/2026/111102/ (ALLOWED); https://web.gekisaka.jp/news/jleaguecup/detail/?462996-462996-fl= (ALLOWED). Card timing `TIMING_UNVERIFIED`; self-declared phase labels: n/a. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT R3NEXT-A/Urawa_Reds_Cerezo_Osaka_LevainCup_2026_v24.15_RESEARCH_DRAFT.md revision-1 -->

<!-- BEGIN SETTLEMENT R3NEXT-B/DRAFT-010 revision-1 -->
### Settlement · `R3NEXT-B/DRAFT-010` · Urawa Red Diamonds v Cerezo Osaka · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `75a27d4a5df1d6a21224311c62eac2e9e5b044acafa194819fa0b44c71317600`, 12562 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/r3next/COMPLETE/research_notes/DRAFT_010/Urawa_Reds_Cerezo_Osaka_2026-11-11_v24.15_READ_ONLY_DRAFT.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `TIMING_UNVERIFIED` (recorded `NOT_RECORDED`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| LEAN_TOTAL | First half Over 0.5 goals | NOT_ESTIMATED (QUALITATIVE) | **LOSS** | total 0 vs 0.5: -0.5 |  |
| SECOND | Full-time Over 2.5 goals | NOT_ESTIMATED (QUALITATIVE) | **LOSS** | total 2 vs 2.5: -0.5 |  |
| EXPLORATORY | Under 10.5 corners | NOT_ESTIMATED (QUALITATIVE) | **UNRESOLVED** | corner count not found |  |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_TOTAL First half Over 0.5 goals (NOT_ESTIMATED) LOSS; RANK1 First half Over 0.5 goals (NOT_ESTIMATED) LOSS. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Urawa 2-0 Cerezo Osaka (HT 0-0); Goals Ueki 74', Komori 90+4'; first half 0-0; corner kicks NOT FOUND. Identity matched on teams/players, date and competition (J.League YBC Levain Cup 2026/27 QF first leg (match 111102)).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Soccer rows: 90 minutes plus stoppage; corners unresolved.
**R4. Rank diagnostics.** 0W/2L/1U over 3 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Urawa minus Cerezo = +2; total 2. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** No goal in the first half; Urawa scored at 74' and 90+4'. Two goals in total; the corner count was not found on any permitted page, so both corner rows stay UNRESOLVED.
**R9. Source/timing review.** Settlement sources: https://www.jleague.jp/match/leaguecup/2026/111102/ (ALLOWED); https://web.gekisaka.jp/news/jleaguecup/detail/?462996-462996-fl= (ALLOWED). Card timing `TIMING_UNVERIFIED`; self-declared phase labels: n/a. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT R3NEXT-B/DRAFT-010 revision-1 -->

<!-- BEGIN SETTLEMENT R3NEXT-C/V412-CHAT-G009 revision-1 -->
### Settlement · `R3NEXT-C/V412-CHAT-G009` · Urawa Red Diamonds v Cerezo Osaka · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `084f26f8a6aa0829365d92922a9d6555aeca1d08961b373823749d400dba8971`, 5390 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/r3next/V412/V412-CHAT-G009.block.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `POST_SCHEDULED_START_WRITE` (recorded `2026-11-11T10:30:28Z (28 s AFTER scheduled kick-off)`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| V412 | First half Over 0.5 goals | 0.795 (V412_MODEL) | **LOSS** | total 0 vs 0.5: -0.5 | 0.632025 |
| V412 | First half Under 0.5 goals | 0.205 (V412_MODEL) | **WIN** | total 0 vs 0.5: -0.5 | 0.632025 |
| V412 | Full-time Over 2.5 goals | 0.680 (V412_MODEL) | **LOSS** | total 2 vs 2.5: -0.5 | 0.462400 |
| V412 | Full-time Under 2.5 goals | 0.320 (V412_MODEL) | **WIN** | total 2 vs 2.5: -0.5 | 0.462400 |
| V412 | Over 10.5 corners | 0.374 (V412_MODEL) | **UNRESOLVED** | corner count not found |  |
| V412 | Under 10.5 corners | 0.626 (V412_MODEL) | **UNRESOLVED** | corner count not found |  |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_TOTAL First half Over 0.5 goals (0.795) LOSS. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Urawa 2-0 Cerezo Osaka (HT 0-0); Goals Ueki 74', Komori 90+4'; first half 0-0; corner kicks NOT FOUND. Identity matched on teams/players, date and competition (J.League YBC Levain Cup 2026/27 QF first leg (match 111102)).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Soccer rows: 90 minutes plus stoppage; corners unresolved.
**R4. Rank diagnostics.** 2W/2L/2U over 6 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Urawa minus Cerezo = +2; total 2. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** No goal in the first half; Urawa scored at 74' and 90+4'. Two goals in total; the corner count was not found on any permitted page, so both corner rows stay UNRESOLVED.
**R9. Source/timing review.** Settlement sources: https://www.jleague.jp/match/leaguecup/2026/111102/ (ALLOWED); https://web.gekisaka.jp/news/jleaguecup/detail/?462996-462996-fl= (ALLOWED). Card timing `POST_SCHEDULED_START_WRITE`; self-declared phase labels: n/a. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT R3NEXT-C/V412-CHAT-G009 revision-1 -->

<!-- BEGIN SETTLEMENT R3NEXT-A/Urawa_Kashima_2026_11_11_FIXTURE_IDENTITY_CONFLICT_v24.15.md revision-1 -->
### Settlement · `R3NEXT-A/Urawa_Kashima_2026_11_11_FIXTURE_IDENTITY_CONFLICT_v24.15.md` · Urawa Red Diamonds v Cerezo Osaka · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `614a393ced0451eba90938a08f0969c8ab448ce770e67282426b33f84b311af9`, 4909 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/r3next/FULL/original_research/Urawa_Kashima_2026_11_11_FIXTURE_IDENTITY_CONFLICT_v24.15.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `TIMING_UNVERIFIED` (recorded `NOT_RECORDED`).

**NO_FORECAST identity-conflict note.** The request named Urawa v Kashima at the Urawa–Cerezo kick-off; the record correctly refused to forecast. No contract row exists, nothing is graded. Retained as documentary research under the Urawa–Cerezo event because the owner's corrected request followed it.

<!-- END SETTLEMENT R3NEXT-A/Urawa_Kashima_2026_11_11_FIXTURE_IDENTITY_CONFLICT_v24.15.md revision-1 -->

<!-- BEGIN SETTLEMENT R3NEXT-B/DRAFT-009 revision-1 -->
### Settlement · `R3NEXT-B/DRAFT-009` · Urawa Red Diamonds v Cerezo Osaka · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `27bc11402fb39a6d82352cfe907c3b53e038dcccfd24f485c4af5657e7b0efa9`, 7371 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/r3next/COMPLETE/research_notes/DRAFT_009/Urawa_Reds_Kashima_Antlers_2026-11-11_FIXTURE_MISMATCH_v24.15_NO_FORECAST.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `TIMING_UNVERIFIED` (recorded `NOT_RECORDED`).

**NO_FORECAST identity-conflict note.** The request named Urawa v Kashima at the Urawa–Cerezo kick-off; the record correctly refused to forecast. No contract row exists, nothing is graded. Retained as documentary research under the Urawa–Cerezo event because the owner's corrected request followed it.

<!-- END SETTLEMENT R3NEXT-B/DRAFT-009 revision-1 -->

### Deep loss reviews (DEEPLOSS-v1)

#### Deep loss review · Urawa Red Diamonds v Cerezo Osaka · First half Over 0.5 goals

**1. Exact frozen claim.** `First half Over 0.5 goals`, full-game endpoint as each record defined it. Triggered in 3 record(s):

| Record | Trigger role(s) | Original p (basis) | Brier | Log loss |
|---|---|---|---:|---:|
| `R3NEXT-A/Urawa_Reds_Cerezo_Osaka_LevainCup_2026_v24.15_RESEARCH_DRAFT.md` | TOP_TOTAL, RANK1 | NOT_ESTIMATED (QUALITATIVE) |  |  |
| `R3NEXT-B/DRAFT-010` | TOP_TOTAL, RANK1 | NOT_ESTIMATED (QUALITATIVE) |  |  |
| `R3NEXT-C/V412-CHAT-G009` | TOP_TOTAL | 0.795 (V412_MODEL) | 0.632025 | 1.584745 |

No record carried a primary p_card, frozen reference or same-row baseline; BASELINE_P comparison NOT_COMPUTABLE.

**2. Verified outcome.** Urawa 2-0 Cerezo Osaka (HT 0-0) (Goals Ueki 74', Komori 90+4'; first half 0-0; corner kicks NOT FOUND). total 0 vs 0.5: -0.5. Sources in R9; evidence A; final wall-clock NOT_VERIFIED.
**3. Distribution check.** Numeric records priced this row at 0.795-0.795 (mean 0.795); a loss at those prices is a 20%-20% event under each record's own uncalibrated object. Percentile placement inside each record's printed score object is not reconstructed; the printed objects stay in the cores.
**4. Error decomposition.** Realised line distance: total 0 vs 0.5: -0.5. No record had a calibrated centre or a measured effect-table row, so the miss cannot be split into reference error and adjustment error; no blame shares are invented.
**5. Research audit.** Strand A/B: first-half proportion was a J1 proxy, rotations noted (Urawa reserve goalkeeper). Facts not re-opened here remain UNVERIFIED_AT_CUTOFF; no source in any card carries a captured retrieval receipt (chat-local research).
**6. What decided the game.** No goal in the first half; Urawa scored at 74' and 90+4'. Two goals in total; the corner count was not found on any permitted page, so both corner rows stay UNRESOLVED.
**7. Knowable at cutoff?** First-leg caution and heavy rotation were printed as reasons for a 0-0 half. The final score and its timing were not knowable.
**8. Process audit.** Chat-local record; no repository reference stage, no source-audit receipts, no lineup confirmation, no freeze. Timing per record in CARD_TIMING.csv (several written after the scheduled start). Endpoint and contract definitions were correct.
**9. Verdict.** v4.12 priced it at 79.5% with 32% data coverage; the research drafts called it LOW confidence. A cup first leg with rotated XIs should not carry 79.5%.
**10. Cutoff-only counterfactual.** NOT_ESTIMATED: no knowable fact has a measured effect-table row, so no corrected probability is priced after the result.
**11. Failure class and recurrence.** Shared across 3 record(s) on one game: the parallel chats used overlapping public inputs, so their losses are one dependent observation, not 3 independent ones.
**12. Correction.** NO_CHANGE to any rule from one result. Procedure proposals are in AUDIT_REPORT §6 (PROPOSED_NOT_TESTED).
**13. Matched wins.** None among the triggering records.
**14. Honesty.** Original numbers and labels preserved; no luck claim without the arithmetic above; no invented percentages, operator terms or publication times. Preservation PASS; information closure INCOMPLETE.

<!-- END SETTLEMENT EVENT R09 revision-1 -->

<!-- BEGIN SETTLEMENT EVENT R10 revision-1 -->
## Event · Tasmania Jewels (W) v Southside Melbourne Flyers (W) · 2026-11-12 · WNBL 2026-27 Round 5

**Final:** Tasmania 99-79 Southside. **Periods:** Tas-SS 15-25, 27-15, 30-23, 27-16; half 42-40 Tas (derived; coach 'down by two'); no OT. **Evidence B.** Scheduled 2026-11-12T08:00:00+00:00.

| Opened source | Audit | Field read |
|---|---|---|
| https://www.basketball.com.au/news/wnbl27-round-5-tasmania-jewels-southside-melbourne-flyers-match-report | ALLOWED | '99-79'; 'Southside led 25-15 after the first quarter'; 'won the last three quarters 27-15, 30-23 and 27-16' |
| https://aapnews.aap.com.au/news/jewels-show-plenty-of-polish-to-bring-down-wnbl-flyers | ALLOWED | Same final; halftime 'down by two' |

<!-- BEGIN SETTLEMENT R3NEXT-A/Tasmania_Jewels_Southside_Flyers_WNBL_2026_v24.16_READ_ONLY_RESEARCH_DRAFT.md revision-1 -->
### Settlement · `R3NEXT-A/Tasmania_Jewels_Southside_Flyers_WNBL_2026_v24.16_READ_ONLY_RESEARCH_DRAFT.md` · Tasmania Jewels (W) v Southside Melbourne Flyers (W) · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `99b3e6539a59f0934990cb9382305c8a3cd5224ab78bb757756f6cbd5b863412`, 9715 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/r3next/FULL/original_research/Tasmania_Jewels_Southside_Flyers_WNBL_2026_v24.16_READ_ONLY_RESEARCH_DRAFT.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `TIMING_UNVERIFIED` (recorded `NOT_RECORDED`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| LEAN_SIDE | Southside +8.5 | NOT_ESTIMATED (QUALITATIVE) | **LOSS** | team margin -20 with handicap +8.5: cover by -11.5 |  |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Southside +8.5 (NOT_ESTIMATED) LOSS; RANK1 Southside +8.5 (NOT_ESTIMATED) LOSS. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Tasmania 99-79 Southside; Tas-SS 15-25, 27-15, 30-23, 27-16; half 42-40 Tas (derived; coach 'down by two'); no OT. Identity matched on teams/players, date and competition (WNBL 2026-27 Round 5).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Basketball rows include overtime (BK-OT-1); none occurred.
**R4. Rank diagnostics.** 0W/1L/0U over 1 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Tasmania minus Southside = +20; total 178. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Southside led 25-15 after one quarter, then lost the last three quarters by 30 combined. Basham 20 and five Tasmanians in double figures. A 20-point loss beat Southside +8.5 by 11.5.
**R9. Source/timing review.** Settlement sources: https://www.basketball.com.au/news/wnbl27-round-5-tasmania-jewels-southside-melbourne-flyers-match-report (ALLOWED); https://aapnews.aap.com.au/news/jewels-show-plenty-of-polish-to-bring-down-wnbl-flyers (ALLOWED). Card timing `TIMING_UNVERIFIED`; self-declared phase labels: n/a. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT R3NEXT-A/Tasmania_Jewels_Southside_Flyers_WNBL_2026_v24.16_READ_ONLY_RESEARCH_DRAFT.md revision-1 -->

<!-- BEGIN SETTLEMENT R3NEXT-B/DRAFT-011 revision-1 -->
### Settlement · `R3NEXT-B/DRAFT-011` · Tasmania Jewels (W) v Southside Melbourne Flyers (W) · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `fe9478fc4d8a8b30898ff20e0a6e446c87f03379800597392626d93819ea2ed0`, 11166 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/r3next/COMPLETE/research_notes/DRAFT_011/Tasmania_Jewels_Southside_Flyers_WNBL_2026-11-12_v24.16_READ_ONLY_DRAFT.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `TIMING_UNVERIFIED` (recorded `NOT_RECORDED`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| LEAN_SIDE | Southside +8.5 | NOT_ESTIMATED (QUALITATIVE) | **LOSS** | team margin -20 with handicap +8.5: cover by -11.5 |  |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Southside +8.5 (NOT_ESTIMATED) LOSS; RANK1 Southside +8.5 (NOT_ESTIMATED) LOSS. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Tasmania 99-79 Southside; Tas-SS 15-25, 27-15, 30-23, 27-16; half 42-40 Tas (derived; coach 'down by two'); no OT. Identity matched on teams/players, date and competition (WNBL 2026-27 Round 5).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Basketball rows include overtime (BK-OT-1); none occurred.
**R4. Rank diagnostics.** 0W/1L/0U over 1 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Tasmania minus Southside = +20; total 178. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Southside led 25-15 after one quarter, then lost the last three quarters by 30 combined. Basham 20 and five Tasmanians in double figures. A 20-point loss beat Southside +8.5 by 11.5.
**R9. Source/timing review.** Settlement sources: https://www.basketball.com.au/news/wnbl27-round-5-tasmania-jewels-southside-melbourne-flyers-match-report (ALLOWED); https://aapnews.aap.com.au/news/jewels-show-plenty-of-polish-to-bring-down-wnbl-flyers (ALLOWED). Card timing `TIMING_UNVERIFIED`; self-declared phase labels: n/a. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT R3NEXT-B/DRAFT-011 revision-1 -->

<!-- BEGIN SETTLEMENT R3NEXT-C/V412-CHAT-G010 revision-1 -->
### Settlement · `R3NEXT-C/V412-CHAT-G010` · Tasmania Jewels (W) v Southside Melbourne Flyers (W) · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `9fb70432ea869d37aacd5b2eab88c80a050d696f1d9a88e1dc64524a00643263`, 6292 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/r3next/V412/V412-CHAT-G010.block.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `POST_SCHEDULED_START_WRITE` (recorded `after scheduled start (own statement; time not printed)`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| V412 | Tasmania -8.5 | 0.249 (V412_MODEL) | **WIN** | team margin +20 with handicap -8.5: cover by +11.5 | 0.564001 |
| V412 | Southside +8.5 | 0.751 (V412_MODEL) | **LOSS** | team margin -20 with handicap +8.5: cover by -11.5 | 0.564001 |
| V412 | Over 165.5 | 0.487 (V412_MODEL) | **WIN** | total 178 vs 165.5: +12.5 | 0.263169 |
| V412 | Under 165.5 | 0.513 (V412_MODEL) | **LOSS** | total 178 vs 165.5: +12.5 | 0.263169 |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Southside +8.5 (0.751) LOSS; TOP_TOTAL Under 165.5 (0.513) LOSS. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Tasmania 99-79 Southside; Tas-SS 15-25, 27-15, 30-23, 27-16; half 42-40 Tas (derived; coach 'down by two'); no OT. Identity matched on teams/players, date and competition (WNBL 2026-27 Round 5).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Basketball rows include overtime (BK-OT-1); none occurred.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Tasmania minus Southside = +20; total 178. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Southside led 25-15 after one quarter, then lost the last three quarters by 30 combined. Basham 20 and five Tasmanians in double figures. A 20-point loss beat Southside +8.5 by 11.5.
**R9. Source/timing review.** Settlement sources: https://www.basketball.com.au/news/wnbl27-round-5-tasmania-jewels-southside-melbourne-flyers-match-report (ALLOWED); https://aapnews.aap.com.au/news/jewels-show-plenty-of-polish-to-bring-down-wnbl-flyers (ALLOWED). Card timing `POST_SCHEDULED_START_WRITE`; self-declared phase labels: n/a. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT R3NEXT-C/V412-CHAT-G010 revision-1 -->

### Deep loss reviews (DEEPLOSS-v1)

#### Deep loss review · Tasmania Jewels (W) v Southside Melbourne Flyers (W) · Southside +8.5

**1. Exact frozen claim.** `Southside +8.5`, full-game endpoint as each record defined it. Triggered in 3 record(s):

| Record | Trigger role(s) | Original p (basis) | Brier | Log loss |
|---|---|---|---:|---:|
| `R3NEXT-A/Tasmania_Jewels_Southside_Flyers_WNBL_2026_v24.16_READ_ONLY_RESEARCH_DRAFT.md` | TOP_SIDE, RANK1 | NOT_ESTIMATED (QUALITATIVE) |  |  |
| `R3NEXT-B/DRAFT-011` | TOP_SIDE, RANK1 | NOT_ESTIMATED (QUALITATIVE) |  |  |
| `R3NEXT-C/V412-CHAT-G010` | TOP_SIDE | 0.751 (V412_MODEL) | 0.564001 | 1.390302 |

No record carried a primary p_card, frozen reference or same-row baseline; BASELINE_P comparison NOT_COMPUTABLE.

**2. Verified outcome.** Tasmania 99-79 Southside (Tas-SS 15-25, 27-15, 30-23, 27-16; half 42-40 Tas (derived; coach 'down by two'); no OT). team margin -20 with handicap +8.5: cover by -11.5. Sources in R9; evidence B; final wall-clock NOT_VERIFIED.
**3. Distribution check.** Numeric records priced this row at 0.751-0.751 (mean 0.751); a loss at those prices is a 25%-25% event under each record's own uncalibrated object. Percentile placement inside each record's printed score object is not reconstructed; the printed objects stay in the cores.
**4. Error decomposition.** Realised line distance: team margin -20 with handicap +8.5: cover by -11.5. No record had a calibrated centre or a measured effect-table row, so the miss cannot be split into reference error and adjustment error; no blame shares are invented.
**5. Research audit.** Southside's 91-77 Round 2 win: TRUE; Froling cleared to return and Okot's debut: TRUE per WNBL 12 Nov articles cited by v4.12. Facts not re-opened here remain UNVERIFIED_AT_CUTOFF; no source in any card carries a captured retrieval receipt (chat-local research).
**6. What decided the game.** Southside led 25-15 after one quarter, then lost the last three quarters by 30 combined. Basham 20 and five Tasmanians in double figures. A 20-point loss beat Southside +8.5 by 11.5.
**7. Knowable at cutoff?** Tasmania's frontcourt additions were KNOWABLE and printed as signed findings favouring Tasmania. The final score and its timing were not knowable.
**8. Process audit.** Chat-local record; no repository reference stage, no source-audit receipts, no lineup confirmation, no freeze. Timing per record in CARD_TIMING.csv (several written after the scheduled start). Endpoint and contract definitions were correct.
**9. Verdict.** Should not have been the lean: two availability changes (Froling return, Okot debut) favoured Tasmania and were unpriced. v4.12's 75.1% on a 4-game Tasmania sample was unjustified.
**10. Cutoff-only counterfactual.** NOT_ESTIMATED: no knowable fact has a measured effect-table row, so no corrected probability is priced after the result.
**11. Failure class and recurrence.** Shared across 3 record(s) on one game: the parallel chats used overlapping public inputs, so their losses are one dependent observation, not 3 independent ones.
**12. Correction.** NO_CHANGE to any rule from one result. Procedure proposals are in AUDIT_REPORT §6 (PROPOSED_NOT_TESTED).
**13. Matched wins.** None among the triggering records.
**14. Honesty.** Original numbers and labels preserved; no luck claim without the arithmetic above; no invented percentages, operator terms or publication times. Preservation PASS; information closure INCOMPLETE.

#### Deep loss review · Tasmania Jewels (W) v Southside Melbourne Flyers (W) · Under 165.5

**1. Exact frozen claim.** `Under 165.5`, full-game endpoint as each record defined it. Triggered in 1 record(s):

| Record | Trigger role(s) | Original p (basis) | Brier | Log loss |
|---|---|---|---:|---:|
| `R3NEXT-C/V412-CHAT-G010` | TOP_TOTAL | 0.513 (V412_MODEL) | 0.263169 | 0.719491 |

No record carried a primary p_card, frozen reference or same-row baseline; BASELINE_P comparison NOT_COMPUTABLE.

**2. Verified outcome.** Tasmania 99-79 Southside (Tas-SS 15-25, 27-15, 30-23, 27-16; half 42-40 Tas (derived; coach 'down by two'); no OT). total 178 vs 165.5: +12.5. Sources in R9; evidence B; final wall-clock NOT_VERIFIED.
**3. Distribution check.** Numeric records priced this row at 0.513-0.513 (mean 0.513); a loss at those prices is a 49%-49% event under each record's own uncalibrated object. Percentile placement inside each record's printed score object is not reconstructed; the printed objects stay in the cores.
**4. Error decomposition.** Realised line distance: total 178 vs 165.5: +12.5. No record had a calibrated centre or a measured effect-table row, so the miss cannot be split into reference error and adjustment error; no blame shares are invented.
**5. Research audit.** v4.12 51.3%. Facts not re-opened here remain UNVERIFIED_AT_CUTOFF; no source in any card carries a captured retrieval receipt (chat-local research).
**6. What decided the game.** Southside led 25-15 after one quarter, then lost the last three quarters by 30 combined. Basham 20 and five Tasmanians in double figures. A 20-point loss beat Southside +8.5 by 11.5.
**7. Knowable at cutoff?** Tasmania's 103-90 and 93-85 home games were printed. The final score and its timing were not knowable.
**8. Process audit.** Chat-local record; no repository reference stage, no source-audit receipts, no lineup confirmation, no freeze. Timing per record in CARD_TIMING.csv (several written after the scheduled start). Endpoint and contract definitions were correct.
**9. Verdict.** Coin-flip row; total 178.
**10. Cutoff-only counterfactual.** NOT_ESTIMATED: no knowable fact has a measured effect-table row, so no corrected probability is priced after the result.
**11. Failure class and recurrence.** Shared across 1 record(s) on one game: the parallel chats used overlapping public inputs, so their losses are one dependent observation, not 1 independent ones.
**12. Correction.** NO_CHANGE to any rule from one result. Procedure proposals are in AUDIT_REPORT §6 (PROPOSED_NOT_TESTED).
**13. Matched wins.** None among the triggering records.
**14. Honesty.** Original numbers and labels preserved; no luck claim without the arithmetic above; no invented percentages, operator terms or publication times. Preservation PASS; information closure INCOMPLETE.

#### Joint section · top side and top total both lost · Tasmania Jewels (W) v Southside Melbourne Flyers (W)

Records: `R3NEXT-C/V412-CHAT-G010`: Southside +8.5 and Under 165.5. Both legs failed on the same game state (Tasmania 99-79 Southside). The cards' own joint-failure figures, where printed, are retained in the cores; none was calibrated, and treating the two leans as independent picks would double-count one wrong read of the game.

<!-- END SETTLEMENT EVENT R10 revision-1 -->

<!-- BEGIN SETTLEMENT EVENT E11 revision-1 -->
## Event · Dalibor Svrčina v Otto Virtanen · 2026-11-12 · ATP Challenger 125 Orléans, R16

**Final:** Virtanen d. Svrčina 6-3 7-5. **Periods:** Games Virtanen 13, Svrčina 8; total 21; ATP match time 01:10:11. **Evidence B.** Scheduled 2026-11-12T12:30:00+00:00.

| Opened source | Audit | Field read |
|---|---|---|
| https://www.atptour.com/en/scores/current-challenger/orleans/2273/results | ALLOWED | 'Otto Virtanen wins the match 6-3 7-5'; Central Arena; 01:10:11 |
| https://www.tennisexplorer.com/player/virtanen-7d161/ | ALLOWED | '12.11. ... R16 6-3, 7-5' |

<!-- BEGIN SETTLEMENT LOCAL-20261112EE4AFA68-G0001 revision-1 -->
### Settlement · `LOCAL-20261112EE4AFA68-G0001` · Dalibor Svrčina v Otto Virtanen · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `3136ed19cc4e55a03791ce07b5c522f2a35c21d005f70055921eedc732cab205`, 22500 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/chat_minis/20261112EE4AFA68.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `HEURISTIC_ARTIFACT_SEE_LABELS` (recorded `2026-11-13T00:00:00+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| T1 | Svrcina +0.5 games | NOT_ESTIMATED (QUALITATIVE) | **LOSS** | team margin -5 with handicap +0.5: cover by -4.5 |  |
| T2 | Over 23.5 games | NOT_ESTIMATED (QUALITATIVE) | **LOSS** | total 21 vs 23.5: -2.5 |  |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Svrcina +0.5 games (NOT_ESTIMATED) LOSS; TOP_TOTAL Over 23.5 games (NOT_ESTIMATED) LOSS; RANK1 Svrcina +0.5 games (NOT_ESTIMATED) LOSS. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Virtanen d. Svrčina 6-3 7-5; Games Virtanen 13, Svrčina 8; total 21; ATP match time 01:10:11. Identity matched on teams/players, date and competition (ATP Challenger 125 Orléans, R16).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Tennis rows count every game of the completed match; no retirement.
**R4. Rank diagnostics.** 0W/2L/0U over 2 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Svrčina games minus Virtanen games = -5; total 21. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** A straight-sets Virtanen win in 70 minutes: 21 games, so Over 23.5 lost by 2.5 games, and Svrčina won 8 games to 13, so Svrčina +0.5 lost by 4.5 games. No set went beyond 7-5.
**R9. Source/timing review.** Settlement sources: https://www.atptour.com/en/scores/current-challenger/orleans/2273/results (ALLOWED); https://www.tennisexplorer.com/player/virtanen-7d161/ (ALLOWED). Card timing `HEURISTIC_ARTIFACT_SEE_LABELS`; self-declared phase labels: TIMING_UNVERIFIED. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT LOCAL-20261112EE4AFA68-G0001 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-20261112CHAT9538BF5E-G0001 revision-1 -->
### Settlement · `LOCAL-20261112CHAT9538BF5E-G0001` · Dalibor Svrčina v Otto Virtanen · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `64d29b0cf49cf892f6410a6d44d07fd65211260195ae444dd73d6b2cedaff452`, 25782 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/chat_minis/20261112CHAT9538BF5E.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `HEURISTIC_ARTIFACT_SEE_LABELS` (recorded `2026-11-13T00:00:00+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| LEAN_SIDE | Svrcina +0.5 games | NOT_ESTIMATED (QUALITATIVE_UNRANKED) | **LOSS** | team margin -5 with handicap +0.5: cover by -4.5 |  |
| LEAN_TOTAL | Over 23.5 games | NOT_ESTIMATED (QUALITATIVE_UNRANKED) | **LOSS** | total 21 vs 23.5: -2.5 |  |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Svrcina +0.5 games (NOT_ESTIMATED) LOSS; TOP_TOTAL Over 23.5 games (NOT_ESTIMATED) LOSS; RANK1 Svrcina +0.5 games (NOT_ESTIMATED) LOSS. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Virtanen d. Svrčina 6-3 7-5; Games Virtanen 13, Svrčina 8; total 21; ATP match time 01:10:11. Identity matched on teams/players, date and competition (ATP Challenger 125 Orléans, R16).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Tennis rows count every game of the completed match; no retirement.
**R4. Rank diagnostics.** 0W/2L/0U over 2 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Svrčina games minus Virtanen games = -5; total 21. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** A straight-sets Virtanen win in 70 minutes: 21 games, so Over 23.5 lost by 2.5 games, and Svrčina won 8 games to 13, so Svrčina +0.5 lost by 4.5 games. No set went beyond 7-5.
**R9. Source/timing review.** Settlement sources: https://www.atptour.com/en/scores/current-challenger/orleans/2273/results (ALLOWED); https://www.tennisexplorer.com/player/virtanen-7d161/ (ALLOWED). Card timing `HEURISTIC_ARTIFACT_SEE_LABELS`; self-declared phase labels: POST_START_POSSIBLE;TIMING_UNVERIFIED. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT LOCAL-20261112CHAT9538BF5E-G0001 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-202611128358B025-G0001 revision-1 -->
### Settlement · `LOCAL-202611128358B025-G0001` · Dalibor Svrčina v Otto Virtanen · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `1e215dea9cc41b22032841c8dbb1b1b2d9d6d7f54ad6cabdaff2d2e241d5c243`, 21329 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/chat_minis/202611128358B025.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `POST_SCHEDULED_START_WRITE` (recorded `2026-11-12T23:57:37+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| D1 | Svrcina +0.5 games | 0.554476 (DIAGNOSTIC_RECURSION) | **LOSS** | team margin -5 with handicap +0.5: cover by -4.5 | 0.307444 |
| D2 | Over 23.5 games | 0.536635 (DIAGNOSTIC_RECURSION) | **LOSS** | total 21 vs 23.5: -2.5 | 0.287977 |
| D3 | Under 23.5 games | 0.463365 (DIAGNOSTIC_RECURSION) | **WIN** | total 21 vs 23.5: -2.5 | 0.287977 |
| D4 | Virtanen -0.5 games | 0.445524 (DIAGNOSTIC_RECURSION) | **WIN** | team margin +5 with handicap -0.5: cover by +4.5 | 0.307444 |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Svrcina +0.5 games (0.554476) LOSS; TOP_TOTAL Over 23.5 games (0.536635) LOSS; RANK1 Svrcina +0.5 games (0.554476) LOSS. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Virtanen d. Svrčina 6-3 7-5; Games Virtanen 13, Svrčina 8; total 21; ATP match time 01:10:11. Identity matched on teams/players, date and competition (ATP Challenger 125 Orléans, R16).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Tennis rows count every game of the completed match; no retirement.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Svrčina games minus Virtanen games = -5; total 21. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** A straight-sets Virtanen win in 70 minutes: 21 games, so Over 23.5 lost by 2.5 games, and Svrčina won 8 games to 13, so Svrčina +0.5 lost by 4.5 games. No set went beyond 7-5.
**R9. Source/timing review.** Settlement sources: https://www.atptour.com/en/scores/current-challenger/orleans/2273/results (ALLOWED); https://www.tennisexplorer.com/player/virtanen-7d161/ (ALLOWED). Card timing `POST_SCHEDULED_START_WRITE`; self-declared phase labels: TIMING_UNVERIFIED. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT LOCAL-202611128358B025-G0001 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-20261112CHAT17C8C881-G0001 revision-1 -->
### Settlement · `LOCAL-20261112CHAT17C8C881-G0001` · Dalibor Svrčina v Otto Virtanen · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `3fb8b769d4208b5a68b7f5f7fdb936298949cdc829afabe1133e44424331630f`, 20409 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/chat_minis/20261112CHAT17C8C881.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `POST_SCHEDULED_START_WRITE` (recorded `2026-11-12T23:59:17+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| D1 | Over 23.5 games | 0.53906 (DIAGNOSTIC_TREE) | **LOSS** | total 21 vs 23.5: -2.5 | 0.290586 |
| D2 | Svrcina +0.5 games | 0.52987 (DIAGNOSTIC_TREE) | **LOSS** | team margin -5 with handicap +0.5: cover by -4.5 | 0.280762 |
| D3 | Virtanen -0.5 games | 0.47013 (DIAGNOSTIC_TREE) | **WIN** | team margin +5 with handicap -0.5: cover by +4.5 | 0.280762 |
| D4 | Under 23.5 games | 0.46094 (DIAGNOSTIC_TREE) | **WIN** | total 21 vs 23.5: -2.5 | 0.290586 |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Svrcina +0.5 games (0.52987) LOSS; TOP_TOTAL Over 23.5 games (0.53906) LOSS; RANK1 Over 23.5 games (0.53906) LOSS. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Virtanen d. Svrčina 6-3 7-5; Games Virtanen 13, Svrčina 8; total 21; ATP match time 01:10:11. Identity matched on teams/players, date and competition (ATP Challenger 125 Orléans, R16).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Tennis rows count every game of the completed match; no retirement.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Svrčina games minus Virtanen games = -5; total 21. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** A straight-sets Virtanen win in 70 minutes: 21 games, so Over 23.5 lost by 2.5 games, and Svrčina won 8 games to 13, so Svrčina +0.5 lost by 4.5 games. No set went beyond 7-5.
**R9. Source/timing review.** Settlement sources: https://www.atptour.com/en/scores/current-challenger/orleans/2273/results (ALLOWED); https://www.tennisexplorer.com/player/virtanen-7d161/ (ALLOWED). Card timing `POST_SCHEDULED_START_WRITE`; self-declared phase labels: NONE_FOUND. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT LOCAL-20261112CHAT17C8C881-G0001 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-20261112CC53B5C806-G0001 revision-1 -->
### Settlement · `LOCAL-20261112CC53B5C806-G0001` · Dalibor Svrčina v Otto Virtanen · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `600d26f2888e9457bab56038ed212df657affd3b47f985edf2497afd2f1f72d6`, 23725 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/chat_minis/20261112CC53B5C806.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `HEURISTIC_ARTIFACT_SEE_LABELS` (recorded `2026-11-13T00:00:00+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| 1 | Virtanen -0.5 games | 0.550 (SHADOW_APPROX) | **WIN** | team margin +5 with handicap -0.5: cover by +4.5 | 0.202500 |
| 2 | Over 23.5 games | 0.535 (SHADOW_APPROX) | **LOSS** | total 21 vs 23.5: -2.5 | 0.286225 |
| INFO | Under 23.5 games | 0.465 (SHADOW_APPROX) | **WIN** | total 21 vs 23.5: -2.5 | 0.286225 |
| INFO | Svrcina +0.5 games | 0.450 (SHADOW_APPROX) | **LOSS** | team margin -5 with handicap +0.5: cover by -4.5 | 0.202500 |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Virtanen -0.5 games (0.550) WIN; TOP_TOTAL Over 23.5 games (0.535) LOSS; RANK1 Virtanen -0.5 games (0.550) WIN. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Virtanen d. Svrčina 6-3 7-5; Games Virtanen 13, Svrčina 8; total 21; ATP match time 01:10:11. Identity matched on teams/players, date and competition (ATP Challenger 125 Orléans, R16).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Tennis rows count every game of the completed match; no retirement.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Svrčina games minus Virtanen games = -5; total 21. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** A straight-sets Virtanen win in 70 minutes: 21 games, so Over 23.5 lost by 2.5 games, and Svrčina won 8 games to 13, so Svrčina +0.5 lost by 4.5 games. No set went beyond 7-5.
**R9. Source/timing review.** Settlement sources: https://www.atptour.com/en/scores/current-challenger/orleans/2273/results (ALLOWED); https://www.tennisexplorer.com/player/virtanen-7d161/ (ALLOWED). Card timing `HEURISTIC_ARTIFACT_SEE_LABELS`; self-declared phase labels: TIMING_UNVERIFIED. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT LOCAL-20261112CC53B5C806-G0001 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-20261112D3C239297F-G0001 revision-1 -->
### Settlement · `LOCAL-20261112D3C239297F-G0001` · Dalibor Svrčina v Otto Virtanen · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `5f747b1e60bda6b2cedcc12eb82e1654bb00458afeeb66f9705ae139072e8c5a`, 26961 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/chat_minis/20261112D3C239297F.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `HEURISTIC_ARTIFACT_SEE_LABELS` (recorded `2026-11-13T00:00:00+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| D1 | Virtanen -0.5 games | 0.570 (SCENARIO_MC) | **WIN** | team margin +5 with handicap -0.5: cover by +4.5 | 0.184900 |
| D2 | Over 23.5 games | 0.527 (SCENARIO_MC) | **LOSS** | total 21 vs 23.5: -2.5 | 0.277729 |
| D3 | Under 23.5 games | 0.473 (SCENARIO_MC) | **WIN** | total 21 vs 23.5: -2.5 | 0.277729 |
| D4 | Svrcina +0.5 games | 0.430 (SCENARIO_MC) | **LOSS** | team margin -5 with handicap +0.5: cover by -4.5 | 0.184900 |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Virtanen -0.5 games (0.570) WIN; TOP_TOTAL Over 23.5 games (0.527) LOSS; RANK1 Virtanen -0.5 games (0.570) WIN. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Virtanen d. Svrčina 6-3 7-5; Games Virtanen 13, Svrčina 8; total 21; ATP match time 01:10:11. Identity matched on teams/players, date and competition (ATP Challenger 125 Orléans, R16).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Tennis rows count every game of the completed match; no retirement.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Svrčina games minus Virtanen games = -5; total 21. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** A straight-sets Virtanen win in 70 minutes: 21 games, so Over 23.5 lost by 2.5 games, and Svrčina won 8 games to 13, so Svrčina +0.5 lost by 4.5 games. No set went beyond 7-5.
**R9. Source/timing review.** Settlement sources: https://www.atptour.com/en/scores/current-challenger/orleans/2273/results (ALLOWED); https://www.tennisexplorer.com/player/virtanen-7d161/ (ALLOWED). Card timing `HEURISTIC_ARTIFACT_SEE_LABELS`; self-declared phase labels: TIMING_UNVERIFIED. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT LOCAL-20261112D3C239297F-G0001 revision-1 -->

### Deep loss reviews (DEEPLOSS-v1)

#### Deep loss review · Dalibor Svrčina v Otto Virtanen · Svrcina +0.5 games

**1. Exact frozen claim.** `Svrcina +0.5 games`, full-game endpoint as each record defined it. Triggered in 4 record(s):

| Record | Trigger role(s) | Original p (basis) | Brier | Log loss |
|---|---|---|---:|---:|
| `LOCAL-202611128358B025-G0001` | TOP_SIDE, RANK1 | 0.554476 (DIAGNOSTIC_RECURSION) | 0.307444 | 0.808504 |
| `LOCAL-20261112CHAT17C8C881-G0001` | TOP_SIDE | 0.52987 (DIAGNOSTIC_TREE) | 0.280762 | 0.754746 |
| `LOCAL-20261112CHAT9538BF5E-G0001` | TOP_SIDE, RANK1 | NOT_ESTIMATED (QUALITATIVE_UNRANKED) |  |  |
| `LOCAL-20261112EE4AFA68-G0001` | TOP_SIDE, RANK1 | NOT_ESTIMATED (QUALITATIVE) |  |  |

No record carried a primary p_card, frozen reference or same-row baseline; BASELINE_P comparison NOT_COMPUTABLE.

**2. Verified outcome.** Virtanen d. Svrčina 6-3 7-5 (Games Virtanen 13, Svrčina 8; total 21; ATP match time 01:10:11). team margin -5 with handicap +0.5: cover by -4.5. Sources in R9; evidence B; final wall-clock NOT_VERIFIED (duration 1:10:11; start not published).
**3. Distribution check.** Numeric records priced this row at 0.530-0.554 (mean 0.542); a loss at those prices is a 45%-47% event under each record's own uncalibrated object. Percentile placement inside each record's printed score object is not reconstructed; the printed objects stay in the cores.
**4. Error decomposition.** Realised line distance: team margin -5 with handicap +0.5: cover by -4.5. No record had a calibrated centre or a measured effect-table row, so the miss cannot be split into reference error and adjustment error; no blame shares are invented.
**5. Research audit.** Elo edge for Svrčina came from a Tennis Abstract snapshot that the card itself flagged as conflicting with an older 3 Aug version; serve/return inputs were all-surface 52-week aggregates, not indoor-specific. The 4-1 L5 for Svrčina is TRUE on the cited result lists. Facts not re-opened here remain UNVERIFIED_AT_CUTOFF; no source in any card carries a captured retrieval receipt (chat-local research).
**6. What decided the game.** A straight-sets Virtanen win in 70 minutes: 21 games, so Over 23.5 lost by 2.5 games, and Svrčina won 8 games to 13, so Svrčina +0.5 lost by 4.5 games. No set went beyond 7-5.
**7. Knowable at cutoff?** Virtanen's indoor serve profile (62.6%/77.3% first-serve figures in CC53's card) was knowable and two chats leaned Virtanen on it. The final score and its timing were not knowable.
**8. Process audit.** Chat-local record; no repository reference stage, no source-audit receipts, no lineup confirmation, no freeze. Timing per record in CARD_TIMING.csv (several written after the scheduled start). Endpoint and contract definitions were correct.
**9. Verdict.** SHOULD NOT have been the lean for four of six chats: the inputs were split and the two chats that weighted indoor serve got the side right. Loss is a model-input choice, not bad luck: 8 games to 13 is far outside a coin-flip margin.
**10. Cutoff-only counterfactual.** NOT_ESTIMATED: no knowable fact has a measured effect-table row, so no corrected probability is priced after the result.
**11. Failure class and recurrence.** Shared across 4 record(s) on one game: the parallel chats used overlapping public inputs, so their losses are one dependent observation, not 4 independent ones.
**12. Correction.** NO_CHANGE to any rule from one result. Procedure proposals are in AUDIT_REPORT §6 (PROPOSED_NOT_TESTED).
**13. Matched wins.** None among the triggering records.
**14. Honesty.** Original numbers and labels preserved; no luck claim without the arithmetic above; no invented percentages, operator terms or publication times. Preservation PASS; information closure INCOMPLETE.

#### Deep loss review · Dalibor Svrčina v Otto Virtanen · Over 23.5 games

**1. Exact frozen claim.** `Over 23.5 games`, full-game endpoint as each record defined it. Triggered in 6 record(s):

| Record | Trigger role(s) | Original p (basis) | Brier | Log loss |
|---|---|---|---:|---:|
| `LOCAL-202611128358B025-G0001` | TOP_TOTAL | 0.536635 (DIAGNOSTIC_RECURSION) | 0.287977 | 0.769240 |
| `LOCAL-20261112CC53B5C806-G0001` | TOP_TOTAL | 0.535 (SHADOW_APPROX) | 0.286225 | 0.765718 |
| `LOCAL-20261112CHAT17C8C881-G0001` | TOP_TOTAL, RANK1 | 0.53906 (DIAGNOSTIC_TREE) | 0.290586 | 0.774487 |
| `LOCAL-20261112CHAT9538BF5E-G0001` | TOP_TOTAL | NOT_ESTIMATED (QUALITATIVE_UNRANKED) |  |  |
| `LOCAL-20261112D3C239297F-G0001` | TOP_TOTAL | 0.527 (SCENARIO_MC) | 0.277729 | 0.748660 |
| `LOCAL-20261112EE4AFA68-G0001` | TOP_TOTAL | NOT_ESTIMATED (QUALITATIVE) |  |  |

No record carried a primary p_card, frozen reference or same-row baseline; BASELINE_P comparison NOT_COMPUTABLE.

**2. Verified outcome.** Virtanen d. Svrčina 6-3 7-5 (Games Virtanen 13, Svrčina 8; total 21; ATP match time 01:10:11). total 21 vs 23.5: -2.5. Sources in R9; evidence B; final wall-clock NOT_VERIFIED (duration 1:10:11; start not published).
**3. Distribution check.** Numeric records priced this row at 0.527-0.539 (mean 0.534); a loss at those prices is a 46%-47% event under each record's own uncalibrated object. Percentile placement inside each record's printed score object is not reconstructed; the printed objects stay in the cores.
**4. Error decomposition.** Realised line distance: total 21 vs 23.5: -2.5. No record had a calibrated centre or a measured effect-table row, so the miss cannot be split into reference error and adjustment error; no blame shares are invented.
**5. Research audit.** Over rested on both players' recent deciding-set frequency; true for the L5 cited, not opponent-adjusted. Facts not re-opened here remain UNVERIFIED_AT_CUTOFF; no source in any card carries a captured retrieval receipt (chat-local research).
**6. What decided the game.** A straight-sets Virtanen win in 70 minutes: 21 games, so Over 23.5 lost by 2.5 games, and Svrčina won 8 games to 13, so Svrčina +0.5 lost by 4.5 games. No set went beyond 7-5.
**7. Knowable at cutoff?** Straight-set routes were priced at 46-47% by the chats themselves. The final score and its timing were not knowable.
**8. Process audit.** Chat-local record; no repository reference stage, no source-audit receipts, no lineup confirmation, no freeze. Timing per record in CARD_TIMING.csv (several written after the scheduled start). Endpoint and contract definitions were correct.
**9. Verdict.** A near coin-flip lean that lost to a 21-game straight-sets match; defensible as a lean, not as a pick. Every chat had it at 52.7-53.9%.
**10. Cutoff-only counterfactual.** NOT_ESTIMATED: no knowable fact has a measured effect-table row, so no corrected probability is priced after the result.
**11. Failure class and recurrence.** Shared across 6 record(s) on one game: the parallel chats used overlapping public inputs, so their losses are one dependent observation, not 6 independent ones.
**12. Correction.** NO_CHANGE to any rule from one result. Procedure proposals are in AUDIT_REPORT §6 (PROPOSED_NOT_TESTED).
**13. Matched wins.** `LOCAL-20261112CC53B5C806-G0001` RANK1 Virtanen -0.5 games WIN; `LOCAL-20261112CC53B5C806-G0001` TOP_SIDE Virtanen -0.5 games WIN; `LOCAL-20261112D3C239297F-G0001` RANK1 Virtanen -0.5 games WIN; `LOCAL-20261112D3C239297F-G0001` TOP_SIDE Virtanen -0.5 games WIN. These rest on the same unvalidated construction and do not show the process worked.
**14. Honesty.** Original numbers and labels preserved; no luck claim without the arithmetic above; no invented percentages, operator terms or publication times. Preservation PASS; information closure INCOMPLETE.

#### Joint section · top side and top total both lost · Dalibor Svrčina v Otto Virtanen

Records: `LOCAL-20261112EE4AFA68-G0001`: Svrcina +0.5 games and Over 23.5 games; `LOCAL-20261112CHAT9538BF5E-G0001`: Svrcina +0.5 games and Over 23.5 games; `LOCAL-202611128358B025-G0001`: Svrcina +0.5 games and Over 23.5 games; `LOCAL-20261112CHAT17C8C881-G0001`: Svrcina +0.5 games and Over 23.5 games. Both legs failed on the same game state (Virtanen d. Svrčina 6-3 7-5). The cards' own joint-failure figures, where printed, are retained in the cores; none was calibrated, and treating the two leans as independent picks would double-count one wrong read of the game.

<!-- END SETTLEMENT EVENT E11 revision-1 -->

<!-- BEGIN SETTLEMENT EVENT E12 revision-1 -->
## Event · Torpedo Ust-Kamenogorsk v Arlan Kokshetau · 2026-11-12 · Kazakhstan Pro Hokei Ligasy 2026-27, schedule row 131

**Final:** Torpedo 4-1 Arlan (regulation). **Periods:** 0:0, 3:1, 1:0; Torpedo 22:49, 24:05, 38:40, 59:33 (empty net); Arlan 24:18. **Evidence B.** Scheduled 2026-11-12T13:30:00+00:00. Note: The 13 Nov rematch (row 133, Torpedo 3-2) is a different event and is not graded. hctorpedo.pro article 6771 (4:1) is a 5 Dec 2025 game and is excluded.

| Opened source | Audit | Field read |
|---|---|---|
| https://sportarena.kz/hockey/1065877-chrk-po-khokkeyu-torpedo-pobedilo-arlan.html | ALLOWED | '4:1 (0:0, 3:1, 1:0)'; published 13 Nov 02:46 |
| https://shaiba.kz/news/811753 | ALLOWED | '4:1 (0:0, 3:1, 1:0)'; published 12 Nov 20:50 |
| https://www.sports.kz/news/uverennoy-pobedoy-zavershilsya-match-torpedo-arlan | ALLOWED | 4:1; '12.11.2026 18:30'; its period narrative conflicts and is not used |

<!-- BEGIN SETTLEMENT LOCAL-20261112EE4AFA68-G0002 revision-1 -->
### Settlement · `LOCAL-20261112EE4AFA68-G0002` · Torpedo Ust-Kamenogorsk v Arlan Kokshetau · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `5abf5a899248abf132cbab5b35274d2525c0e66c2f459cb5c97cff3fef70c1dc`, 25723 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/chat_minis/20261112EE4AFA68.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `PRE_SCHEDULED_START_WRITE` (recorded `2026-11-13T00:29:04+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| T1 | Arlan +1.5 goals | NOT_ESTIMATED (QUALITATIVE) | **LOSS** | team margin -3 with handicap +1.5: cover by -1.5 |  |
| T2 | Under 6.5 goals | NOT_ESTIMATED (QUALITATIVE) | **WIN** | total 5 vs 6.5: -1.5 |  |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Arlan +1.5 goals (NOT_ESTIMATED) LOSS; TOP_TOTAL Under 6.5 goals (NOT_ESTIMATED) WIN; RANK1 Arlan +1.5 goals (NOT_ESTIMATED) LOSS. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Torpedo 4-1 Arlan (regulation); 0:0, 3:1, 1:0; Torpedo 22:49, 24:05, 38:40, 59:33 (empty net); Arlan 24:18. Identity matched on teams/players, date and competition (Kazakhstan Pro Hokei Ligasy 2026-27, schedule row 131).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Hockey rows: the result is identical under 60-minute, full-game and shootout-credited conventions, so no endpoint ambiguity changes a grade.
**R4. Rank diagnostics.** 1W/1L/0U over 2 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Torpedo minus Arlan = +3; total 5. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Torpedo scored at 22:49 and 24:05, Arlan replied at 24:18, and Torpedo made it 3-1 at 38:40; the 4-1 came from an empty-net goal at 59:33. Before the empty-netter Arlan +1.5 was losing by exactly 2 goals, so the empty net did not decide it.
**R9. Source/timing review.** Settlement sources: https://sportarena.kz/hockey/1065877-chrk-po-khokkeyu-torpedo-pobedilo-arlan.html (ALLOWED); https://shaiba.kz/news/811753 (ALLOWED); https://www.sports.kz/news/uverennoy-pobedoy-zavershilsya-match-torpedo-arlan (ALLOWED). Card timing `PRE_SCHEDULED_START_WRITE`; self-declared phase labels: TIMING_UNVERIFIED. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT LOCAL-20261112EE4AFA68-G0002 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-20261112CHAT9538BF5E-G0002 revision-1 -->
### Settlement · `LOCAL-20261112CHAT9538BF5E-G0002` · Torpedo Ust-Kamenogorsk v Arlan Kokshetau · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `be3dfc235e296256f3fbe66d861308bac2b2f91f84411e2ec3cbc21473c52742`, 25325 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/chat_minis/20261112CHAT9538BF5E.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `PRE_SCHEDULED_START_WRITE` (recorded `2026-11-13T00:28:41+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| LEAN_SIDE | Arlan +1.5 goals | NOT_ESTIMATED (QUALITATIVE_UNRANKED) | **LOSS** | team margin -3 with handicap +1.5: cover by -1.5 |  |
| LEAN_TOTAL | Under 6.5 goals | NOT_ESTIMATED (QUALITATIVE_UNRANKED) | **WIN** | total 5 vs 6.5: -1.5 |  |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Arlan +1.5 goals (NOT_ESTIMATED) LOSS; TOP_TOTAL Under 6.5 goals (NOT_ESTIMATED) WIN; RANK1 Arlan +1.5 goals (NOT_ESTIMATED) LOSS. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Torpedo 4-1 Arlan (regulation); 0:0, 3:1, 1:0; Torpedo 22:49, 24:05, 38:40, 59:33 (empty net); Arlan 24:18. Identity matched on teams/players, date and competition (Kazakhstan Pro Hokei Ligasy 2026-27, schedule row 131).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Hockey rows: the result is identical under 60-minute, full-game and shootout-credited conventions, so no endpoint ambiguity changes a grade.
**R4. Rank diagnostics.** 1W/1L/0U over 2 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Torpedo minus Arlan = +3; total 5. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Torpedo scored at 22:49 and 24:05, Arlan replied at 24:18, and Torpedo made it 3-1 at 38:40; the 4-1 came from an empty-net goal at 59:33. Before the empty-netter Arlan +1.5 was losing by exactly 2 goals, so the empty net did not decide it.
**R9. Source/timing review.** Settlement sources: https://sportarena.kz/hockey/1065877-chrk-po-khokkeyu-torpedo-pobedilo-arlan.html (ALLOWED); https://shaiba.kz/news/811753 (ALLOWED); https://www.sports.kz/news/uverennoy-pobedoy-zavershilsya-match-torpedo-arlan (ALLOWED). Card timing `PRE_SCHEDULED_START_WRITE`; self-declared phase labels: BEFORE_OFFICIAL_SCHEDULE. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT LOCAL-20261112CHAT9538BF5E-G0002 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-202611128358B025-G0002 revision-1 -->
### Settlement · `LOCAL-202611128358B025-G0002` · Torpedo Ust-Kamenogorsk v Arlan Kokshetau · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `140f0b59939c088e952a6808ff3305e01ebf12029e68abd2fefb17c91b85b63d`, 20721 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/chat_minis/202611128358B025.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `PRE_SCHEDULED_START_WRITE` (recorded `2026-11-13T00:28:42+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| D1 | Under 6.5 goals | 0.6444 (DIAGNOSTIC_POISSON_FULLGAME) | **WIN** | total 5 vs 6.5: -1.5 | 0.126451 |
| D2 | Torpedo -1.5 goals | 0.5262 (DIAGNOSTIC_POISSON_FULLGAME) | **WIN** | team margin +3 with handicap -1.5: cover by +1.5 | 0.224486 |
| D3 | Arlan +1.5 goals | 0.4738 (DIAGNOSTIC_POISSON_FULLGAME) | **LOSS** | team margin -3 with handicap +1.5: cover by -1.5 | 0.224486 |
| D4 | Over 6.5 goals | 0.3556 (DIAGNOSTIC_POISSON_FULLGAME) | **LOSS** | total 5 vs 6.5: -1.5 | 0.126451 |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Torpedo -1.5 goals (0.5262) WIN; TOP_TOTAL Under 6.5 goals (0.6444) WIN; RANK1 Under 6.5 goals (0.6444) WIN. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Torpedo 4-1 Arlan (regulation); 0:0, 3:1, 1:0; Torpedo 22:49, 24:05, 38:40, 59:33 (empty net); Arlan 24:18. Identity matched on teams/players, date and competition (Kazakhstan Pro Hokei Ligasy 2026-27, schedule row 131).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Hockey rows: the result is identical under 60-minute, full-game and shootout-credited conventions, so no endpoint ambiguity changes a grade.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Torpedo minus Arlan = +3; total 5. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Torpedo scored at 22:49 and 24:05, Arlan replied at 24:18, and Torpedo made it 3-1 at 38:40; the 4-1 came from an empty-net goal at 59:33. Before the empty-netter Arlan +1.5 was losing by exactly 2 goals, so the empty net did not decide it.
**R9. Source/timing review.** Settlement sources: https://sportarena.kz/hockey/1065877-chrk-po-khokkeyu-torpedo-pobedilo-arlan.html (ALLOWED); https://shaiba.kz/news/811753 (ALLOWED); https://www.sports.kz/news/uverennoy-pobedoy-zavershilsya-match-torpedo-arlan (ALLOWED). Card timing `PRE_SCHEDULED_START_WRITE`; self-declared phase labels: PRE_SCHEDULED_START_RESEARCH. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT LOCAL-202611128358B025-G0002 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-20261112CHAT17C8C881-G0002 revision-1 -->
### Settlement · `LOCAL-20261112CHAT17C8C881-G0002` · Torpedo Ust-Kamenogorsk v Arlan Kokshetau · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `1b2f9c555f78c0476f5a41c30b34781dc86391592e7ab2a4376a3e8a9d5dfeae`, 23601 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/chat_minis/20261112CHAT17C8C881.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `PRE_SCHEDULED_START_WRITE` (recorded `2026-11-13T00:23:37+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| R1 | Arlan +1.5 goals | 0.6139 (DIAGNOSTIC_POISSON_60M) | **LOSS** | team margin -3 with handicap +1.5: cover by -1.5 | 0.376873 |
| R2 | Under 6.5 goals | 0.6180 (DIAGNOSTIC_POISSON_FULLGAME) | **WIN** | total 5 vs 6.5: -1.5 | 0.145924 |
| INFO | Torpedo -1.5 goals | 0.3861 (DIAGNOSTIC_POISSON_60M) | **WIN** | team margin +3 with handicap -1.5: cover by +1.5 | 0.376873 |
| INFO | Over 6.5 goals | 0.3820 (DIAGNOSTIC_POISSON_FULLGAME) | **LOSS** | total 5 vs 6.5: -1.5 | 0.145924 |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Arlan +1.5 goals (0.6139) LOSS; TOP_TOTAL Under 6.5 goals (0.6180) WIN; RANK1 Arlan +1.5 goals (0.6139) LOSS. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Torpedo 4-1 Arlan (regulation); 0:0, 3:1, 1:0; Torpedo 22:49, 24:05, 38:40, 59:33 (empty net); Arlan 24:18. Identity matched on teams/players, date and competition (Kazakhstan Pro Hokei Ligasy 2026-27, schedule row 131).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Hockey rows: the result is identical under 60-minute, full-game and shootout-credited conventions, so no endpoint ambiguity changes a grade.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Torpedo minus Arlan = +3; total 5. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Torpedo scored at 22:49 and 24:05, Arlan replied at 24:18, and Torpedo made it 3-1 at 38:40; the 4-1 came from an empty-net goal at 59:33. Before the empty-netter Arlan +1.5 was losing by exactly 2 goals, so the empty net did not decide it.
**R9. Source/timing review.** Settlement sources: https://sportarena.kz/hockey/1065877-chrk-po-khokkeyu-torpedo-pobedilo-arlan.html (ALLOWED); https://shaiba.kz/news/811753 (ALLOWED); https://www.sports.kz/news/uverennoy-pobedoy-zavershilsya-match-torpedo-arlan (ALLOWED). Card timing `PRE_SCHEDULED_START_WRITE`; self-declared phase labels: NONE_FOUND. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT LOCAL-20261112CHAT17C8C881-G0002 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-20261112CC53B5C806-G0002 revision-1 -->
### Settlement · `LOCAL-20261112CC53B5C806-G0002` · Torpedo Ust-Kamenogorsk v Arlan Kokshetau · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `16e9a1ec354d9c80b0037b2509d3f98203c1a1a24c1c75ebc6d0ca02f3112a0c`, 26259 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/chat_minis/20261112CC53B5C806.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `WRITE_TIME_NOT_RECORDED` (recorded `NOT_RECORDED`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| DIR | Under 6.5 goals | 0.623 (SHADOW_MC) | **WIN** | total 5 vs 6.5: -1.5 | 0.142129 |
| DIR_LOW | Arlan +1.5 goals | 0.529 (SHADOW_MC) | **LOSS** | team margin -3 with handicap +1.5: cover by -1.5 | 0.279841 |
| INFO | Torpedo -1.5 goals | 0.471 (SHADOW_MC) | **WIN** | team margin +3 with handicap -1.5: cover by +1.5 | 0.279841 |
| INFO | Over 6.5 goals | 0.377 (SHADOW_MC) | **LOSS** | total 5 vs 6.5: -1.5 | 0.142129 |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Arlan +1.5 goals (0.529) LOSS; TOP_TOTAL Under 6.5 goals (0.623) WIN; RANK1 Under 6.5 goals (0.623) WIN. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Torpedo 4-1 Arlan (regulation); 0:0, 3:1, 1:0; Torpedo 22:49, 24:05, 38:40, 59:33 (empty net); Arlan 24:18. Identity matched on teams/players, date and competition (Kazakhstan Pro Hokei Ligasy 2026-27, schedule row 131).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Hockey rows: the result is identical under 60-minute, full-game and shootout-credited conventions, so no endpoint ambiguity changes a grade.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Torpedo minus Arlan = +3; total 5. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Torpedo scored at 22:49 and 24:05, Arlan replied at 24:18, and Torpedo made it 3-1 at 38:40; the 4-1 came from an empty-net goal at 59:33. Before the empty-netter Arlan +1.5 was losing by exactly 2 goals, so the empty net did not decide it.
**R9. Source/timing review.** Settlement sources: https://sportarena.kz/hockey/1065877-chrk-po-khokkeyu-torpedo-pobedilo-arlan.html (ALLOWED); https://shaiba.kz/news/811753 (ALLOWED); https://www.sports.kz/news/uverennoy-pobedoy-zavershilsya-match-torpedo-arlan (ALLOWED). Card timing `WRITE_TIME_NOT_RECORDED`; self-declared phase labels: TIMING_UNVERIFIED. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT LOCAL-20261112CC53B5C806-G0002 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-20261112D3C239297F-G0002 revision-1 -->
### Settlement · `LOCAL-20261112D3C239297F-G0002` · Torpedo Ust-Kamenogorsk v Arlan Kokshetau · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `9e80bc58efc8327982aa57406398c7a8d9c8e5fb1e3d0efe20f46c454e43fa3f`, 28355 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/chat_minis/20261112D3C239297F.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `POST_SCHEDULED_START_WRITE` (recorded `2026-11-13T00:31:34+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| D1 | Under 6.5 goals | 0.623 (SCENARIO_FULLGAME) | **WIN** | total 5 vs 6.5: -1.5 | 0.142129 |
| D2 | Torpedo -1.5 goals | 0.507 (SCENARIO_FULLGAME) | **WIN** | team margin +3 with handicap -1.5: cover by +1.5 | 0.243049 |
| D3 | Arlan +1.5 goals | 0.493 (SCENARIO_FULLGAME) | **LOSS** | team margin -3 with handicap +1.5: cover by -1.5 | 0.243049 |
| D4 | Over 6.5 goals | 0.377 (SCENARIO_FULLGAME) | **LOSS** | total 5 vs 6.5: -1.5 | 0.142129 |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Torpedo -1.5 goals (0.507) WIN; TOP_TOTAL Under 6.5 goals (0.623) WIN; RANK1 Under 6.5 goals (0.623) WIN. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Torpedo 4-1 Arlan (regulation); 0:0, 3:1, 1:0; Torpedo 22:49, 24:05, 38:40, 59:33 (empty net); Arlan 24:18. Identity matched on teams/players, date and competition (Kazakhstan Pro Hokei Ligasy 2026-27, schedule row 131).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Hockey rows: the result is identical under 60-minute, full-game and shootout-credited conventions, so no endpoint ambiguity changes a grade.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Torpedo minus Arlan = +3; total 5. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Torpedo scored at 22:49 and 24:05, Arlan replied at 24:18, and Torpedo made it 3-1 at 38:40; the 4-1 came from an empty-net goal at 59:33. Before the empty-netter Arlan +1.5 was losing by exactly 2 goals, so the empty net did not decide it.
**R9. Source/timing review.** Settlement sources: https://sportarena.kz/hockey/1065877-chrk-po-khokkeyu-torpedo-pobedilo-arlan.html (ALLOWED); https://shaiba.kz/news/811753 (ALLOWED); https://www.sports.kz/news/uverennoy-pobedoy-zavershilsya-match-torpedo-arlan (ALLOWED). Card timing `POST_SCHEDULED_START_WRITE`; self-declared phase labels: POST_SCHEDULED_START_DRAFT;TIMING_UNVERIFIED. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT LOCAL-20261112D3C239297F-G0002 revision-1 -->

### Deep loss reviews (DEEPLOSS-v1)

#### Deep loss review · Torpedo Ust-Kamenogorsk v Arlan Kokshetau · Arlan +1.5 goals

**1. Exact frozen claim.** `Arlan +1.5 goals`, full-game endpoint as each record defined it. Triggered in 4 record(s):

| Record | Trigger role(s) | Original p (basis) | Brier | Log loss |
|---|---|---|---:|---:|
| `LOCAL-20261112CC53B5C806-G0002` | TOP_SIDE | 0.529 (SHADOW_MC) | 0.279841 | 0.752897 |
| `LOCAL-20261112CHAT17C8C881-G0002` | TOP_SIDE, RANK1 | 0.6139 (DIAGNOSTIC_POISSON_60M) | 0.376873 | 0.951659 |
| `LOCAL-20261112CHAT9538BF5E-G0002` | TOP_SIDE, RANK1 | NOT_ESTIMATED (QUALITATIVE_UNRANKED) |  |  |
| `LOCAL-20261112EE4AFA68-G0002` | TOP_SIDE, RANK1 | NOT_ESTIMATED (QUALITATIVE) |  |  |

No record carried a primary p_card, frozen reference or same-row baseline; BASELINE_P comparison NOT_COMPUTABLE.

**2. Verified outcome.** Torpedo 4-1 Arlan (regulation) (0:0, 3:1, 1:0; Torpedo 22:49, 24:05, 38:40, 59:33 (empty net); Arlan 24:18). team margin -3 with handicap +1.5: cover by -1.5. Sources in R9; evidence B; final wall-clock NOT_VERIFIED.
**3. Distribution check.** Numeric records priced this row at 0.529-0.614 (mean 0.571); a loss at those prices is a 39%-47% event under each record's own uncalibrated object. Percentile placement inside each record's printed score object is not reconstructed; the printed objects stay in the cores.
**4. Error decomposition.** Realised line distance: team margin -3 with handicap +1.5: cover by -1.5. No record had a calibrated centre or a measured effect-table row, so the miss cannot be split into reference error and adjustment error; no blame shares are invented.
**5. Research audit.** Torpedo 26 GP 138-46 and Arlan 92-58 standings: TRUE (official table quoted in cards). H2H 'within one goal' claims: early-season 6-7 Sep games, TRUE per cards' sources but not re-opened here. Facts not re-opened here remain UNVERIFIED_AT_CUTOFF; no source in any card carries a captured retrieval receipt (chat-local research).
**6. What decided the game.** Torpedo scored at 22:49 and 24:05, Arlan replied at 24:18, and Torpedo made it 3-1 at 38:40; the 4-1 came from an empty-net goal at 59:33. Before the empty-netter Arlan +1.5 was losing by exactly 2 goals, so the empty net did not decide it.
**7. Knowable at cutoff?** Torpedo's home dominance (5/5 recent wins by 2+) was printed in the cards as the counter-case. The final score and its timing were not knowable.
**8. Process audit.** Chat-local record; no repository reference stage, no source-audit receipts, no lineup confirmation, no freeze. Timing per record in CARD_TIMING.csv (several written after the scheduled start). Endpoint and contract definitions were correct.
**9. Verdict.** Fragile lean, honestly labelled LOW. Torpedo led 3-1 from the second period and the empty-netter was not needed for the cover, so this was not an empty-net accident.
**10. Cutoff-only counterfactual.** NOT_ESTIMATED: no knowable fact has a measured effect-table row, so no corrected probability is priced after the result.
**11. Failure class and recurrence.** Shared across 4 record(s) on one game: the parallel chats used overlapping public inputs, so their losses are one dependent observation, not 4 independent ones.
**12. Correction.** NO_CHANGE to any rule from one result. Procedure proposals are in AUDIT_REPORT §6 (PROPOSED_NOT_TESTED).
**13. Matched wins.** `LOCAL-20261112CC53B5C806-G0002` RANK1 Under 6.5 goals WIN; `LOCAL-20261112CC53B5C806-G0002` TOP_TOTAL Under 6.5 goals WIN; `LOCAL-20261112CHAT17C8C881-G0002` TOP_TOTAL Under 6.5 goals WIN; `LOCAL-20261112CHAT9538BF5E-G0002` TOP_TOTAL Under 6.5 goals WIN; `LOCAL-20261112EE4AFA68-G0002` TOP_TOTAL Under 6.5 goals WIN. These rest on the same unvalidated construction and do not show the process worked.
**14. Honesty.** Original numbers and labels preserved; no luck claim without the arithmetic above; no invented percentages, operator terms or publication times. Preservation PASS; information closure INCOMPLETE.

<!-- END SETTLEMENT EVENT E12 revision-1 -->

<!-- BEGIN SETTLEMENT EVENT E13 revision-1 -->
## Event · Thiago Agustín Tirante v Aleksandr Shevchenko · 2026-11-12 · ATP 250 Stockholm Open, QF

**Final:** Tirante d. Shevchenko 7-6(5) 6-7(5) 6-3. **Periods:** Games Tirante 19, Shevchenko 16; total 35; ATP 02:49:27; TennisExplorer start 15:20 (zone not stated). **Evidence B.** Scheduled 2026-11-12T14:00:00+00:00.

| Opened source | Audit | Field read |
|---|---|---|
| https://www.atptour.com/en/scores/current/stockholm/429/results | ALLOWED | 'Thiago Agustin Tirante wins the match 7-6(5) 6-7(5) 6-3'; 02:49:27 |
| https://www.tennisexplorer.com/stockholm/2026/atp-men/ | ALLOWED | Same sets; start 15:20 |

<!-- BEGIN SETTLEMENT LOCAL-20261112EE4AFA68-G0003 revision-1 -->
### Settlement · `LOCAL-20261112EE4AFA68-G0003` · Thiago Agustín Tirante v Aleksandr Shevchenko · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `c6709d39a1057b6a207f0a284a7eeead04d3c8e556f02101a954e41c229def48`, 30499 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/chat_minis/20261112EE4AFA68.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `POST_SCHEDULED_START_WRITE` (recorded `2026-11-13T01:10:52+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| T1 | Tirante +0.5 games | NOT_ESTIMATED (QUALITATIVE) | **WIN** | team margin +3 with handicap +0.5: cover by +3.5 |  |
| T2 | Under 23.5 games | NOT_ESTIMATED (QUALITATIVE) | **LOSS** | total 35 vs 23.5: +11.5 |  |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Tirante +0.5 games (NOT_ESTIMATED) WIN; TOP_TOTAL Under 23.5 games (NOT_ESTIMATED) LOSS; RANK1 Tirante +0.5 games (NOT_ESTIMATED) WIN. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Tirante d. Shevchenko 7-6(5) 6-7(5) 6-3; Games Tirante 19, Shevchenko 16; total 35; ATP 02:49:27; TennisExplorer start 15:20 (zone not stated). Identity matched on teams/players, date and competition (ATP 250 Stockholm Open, QF).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Tennis rows count every game of the completed match; no retirement.
**R4. Rank diagnostics.** 1W/1L/0U over 2 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Tirante games minus Shevchenko games = +3; total 35. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Two tiebreak sets and a deciding set produced 35 games, 11.5 over 23.5. Tirante won 19 games to 16.
**R9. Source/timing review.** Settlement sources: https://www.atptour.com/en/scores/current/stockholm/429/results (ALLOWED); https://www.tennisexplorer.com/stockholm/2026/atp-men/ (ALLOWED). Card timing `POST_SCHEDULED_START_WRITE`; self-declared phase labels: TIMING_UNVERIFIED. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT LOCAL-20261112EE4AFA68-G0003 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-20261112CHAT9538BF5E-G0003 revision-1 -->
### Settlement · `LOCAL-20261112CHAT9538BF5E-G0003` · Thiago Agustín Tirante v Aleksandr Shevchenko · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `905d1a00a1b5be569ee4bf933cc6d154a3fca677b9d9b5d5cd0122c7997d0f91`, 19431 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/chat_minis/20261112CHAT9538BF5E.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `POST_SCHEDULED_START_WRITE` (recorded `2026-11-13T01:05:59+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| LEAN_TOTAL | Under 23.5 games | NOT_ESTIMATED (QUALITATIVE_UNRANKED) | **LOSS** | total 35 vs 23.5: +11.5 |  |
| LEAN_SIDE | Shevchenko -0.5 games | NOT_ESTIMATED (QUALITATIVE_UNRANKED) | **LOSS** | team margin -3 with handicap -0.5: cover by -3.5 |  |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Shevchenko -0.5 games (NOT_ESTIMATED) LOSS; TOP_TOTAL Under 23.5 games (NOT_ESTIMATED) LOSS; RANK1 Under 23.5 games (NOT_ESTIMATED) LOSS. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Tirante d. Shevchenko 7-6(5) 6-7(5) 6-3; Games Tirante 19, Shevchenko 16; total 35; ATP 02:49:27; TennisExplorer start 15:20 (zone not stated). Identity matched on teams/players, date and competition (ATP 250 Stockholm Open, QF).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Tennis rows count every game of the completed match; no retirement.
**R4. Rank diagnostics.** 0W/2L/0U over 2 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Tirante games minus Shevchenko games = +3; total 35. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Two tiebreak sets and a deciding set produced 35 games, 11.5 over 23.5. Tirante won 19 games to 16.
**R9. Source/timing review.** Settlement sources: https://www.atptour.com/en/scores/current/stockholm/429/results (ALLOWED); https://www.tennisexplorer.com/stockholm/2026/atp-men/ (ALLOWED). Card timing `POST_SCHEDULED_START_WRITE`; self-declared phase labels: TIMING_UNVERIFIED. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT LOCAL-20261112CHAT9538BF5E-G0003 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-202611128358B025-G0003 revision-1 -->
### Settlement · `LOCAL-202611128358B025-G0003` · Thiago Agustín Tirante v Aleksandr Shevchenko · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `26854b982edd2d063845ceb6398500b74ef8d8d1e9ad0261f53476b8a540fbaa`, 18370 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/chat_minis/202611128358B025.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `POST_SCHEDULED_START_WRITE` (recorded `2026-11-13T01:08:35+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| D1 | Over 23.5 games | 0.54602 (SCENARIO_MIXTURE) | **WIN** | total 35 vs 23.5: +11.5 | 0.206098 |
| D2 | Tirante +0.5 games | 0.50591 (SCENARIO_MIXTURE) | **WIN** | team margin +3 with handicap +0.5: cover by +3.5 | 0.244125 |
| D3 | Shevchenko -0.5 games | 0.49409 (SCENARIO_MIXTURE) | **LOSS** | team margin -3 with handicap -0.5: cover by -3.5 | 0.244125 |
| D4 | Under 23.5 games | 0.45398 (SCENARIO_MIXTURE) | **LOSS** | total 35 vs 23.5: +11.5 | 0.206098 |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Tirante +0.5 games (0.50591) WIN; TOP_TOTAL Over 23.5 games (0.54602) WIN; RANK1 Over 23.5 games (0.54602) WIN. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Tirante d. Shevchenko 7-6(5) 6-7(5) 6-3; Games Tirante 19, Shevchenko 16; total 35; ATP 02:49:27; TennisExplorer start 15:20 (zone not stated). Identity matched on teams/players, date and competition (ATP 250 Stockholm Open, QF).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Tennis rows count every game of the completed match; no retirement.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Tirante games minus Shevchenko games = +3; total 35. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Two tiebreak sets and a deciding set produced 35 games, 11.5 over 23.5. Tirante won 19 games to 16.
**R9. Source/timing review.** Settlement sources: https://www.atptour.com/en/scores/current/stockholm/429/results (ALLOWED); https://www.tennisexplorer.com/stockholm/2026/atp-men/ (ALLOWED). Card timing `POST_SCHEDULED_START_WRITE`; self-declared phase labels: POST_SCHEDULED_START_ISSUE. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT LOCAL-202611128358B025-G0003 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-20261112CHAT17C8C881-G0003 revision-1 -->
### Settlement · `LOCAL-20261112CHAT17C8C881-G0003` · Thiago Agustín Tirante v Aleksandr Shevchenko · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `91e3d377b51a4d8f6cc853400ad2274ebf2238d83ab0a94c8b6c75b2c59cddb3`, 22810 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/chat_minis/20261112CHAT17C8C881.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `POST_SCHEDULED_START_WRITE` (recorded `2026-11-13T01:08:14+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| D1 | Tirante +0.5 games | 0.6875 (DIAGNOSTIC_MARKOV) | **WIN** | team margin +3 with handicap +0.5: cover by +3.5 | 0.097656 |
| D2 | Over 23.5 games | 0.5268 (DIAGNOSTIC_MARKOV) | **WIN** | total 35 vs 23.5: +11.5 | 0.223918 |
| D3 | Under 23.5 games | 0.4732 (DIAGNOSTIC_MARKOV) | **LOSS** | total 35 vs 23.5: +11.5 | 0.223918 |
| D4 | Shevchenko -0.5 games | 0.3125 (DIAGNOSTIC_MARKOV) | **LOSS** | team margin -3 with handicap -0.5: cover by -3.5 | 0.097656 |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Tirante +0.5 games (0.6875) WIN; TOP_TOTAL Over 23.5 games (0.5268) WIN; RANK1 Tirante +0.5 games (0.6875) WIN. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Tirante d. Shevchenko 7-6(5) 6-7(5) 6-3; Games Tirante 19, Shevchenko 16; total 35; ATP 02:49:27; TennisExplorer start 15:20 (zone not stated). Identity matched on teams/players, date and competition (ATP 250 Stockholm Open, QF).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Tennis rows count every game of the completed match; no retirement.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Tirante games minus Shevchenko games = +3; total 35. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Two tiebreak sets and a deciding set produced 35 games, 11.5 over 23.5. Tirante won 19 games to 16.
**R9. Source/timing review.** Settlement sources: https://www.atptour.com/en/scores/current/stockholm/429/results (ALLOWED); https://www.tennisexplorer.com/stockholm/2026/atp-men/ (ALLOWED). Card timing `POST_SCHEDULED_START_WRITE`; self-declared phase labels: POST_SCHEDULED_START_ISSUE. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT LOCAL-20261112CHAT17C8C881-G0003 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-20261112CC53B5C806-G0003 revision-1 -->
### Settlement · `LOCAL-20261112CC53B5C806-G0003` · Thiago Agustín Tirante v Aleksandr Shevchenko · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `f7311307b59bc6300d58cbdde635c7284626868febb2a1058e1258535570a1eb`, 25137 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/chat_minis/20261112CC53B5C806.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `POST_SCHEDULED_START_WRITE` (recorded `2026-11-13T01:10:58+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| 1 | Over 23.5 games | 0.553 (SHADOW_RANGE_MID(54.8-55.9)) | **WIN** | total 35 vs 23.5: +11.5 | 0.199809 |
| 2 | Tirante +0.5 games | NOT_POINT(41.7-61.0) (SHADOW_RANGE) | **WIN** | team margin +3 with handicap +0.5: cover by +3.5 |  |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Tirante +0.5 games (NOT_POINT(41.7-61.0)) WIN; TOP_TOTAL Over 23.5 games (0.553) WIN; RANK1 Over 23.5 games (0.553) WIN. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Tirante d. Shevchenko 7-6(5) 6-7(5) 6-3; Games Tirante 19, Shevchenko 16; total 35; ATP 02:49:27; TennisExplorer start 15:20 (zone not stated). Identity matched on teams/players, date and competition (ATP 250 Stockholm Open, QF).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Tennis rows count every game of the completed match; no retirement.
**R4. Rank diagnostics.** 2W/0L/0U over 2 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Tirante games minus Shevchenko games = +3; total 35. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Two tiebreak sets and a deciding set produced 35 games, 11.5 over 23.5. Tirante won 19 games to 16.
**R9. Source/timing review.** Settlement sources: https://www.atptour.com/en/scores/current/stockholm/429/results (ALLOWED); https://www.tennisexplorer.com/stockholm/2026/atp-men/ (ALLOWED). Card timing `POST_SCHEDULED_START_WRITE`; self-declared phase labels: NONE_FOUND. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT LOCAL-20261112CC53B5C806-G0003 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-20261112D3C239297F-G0003 revision-1 -->
### Settlement · `LOCAL-20261112D3C239297F-G0003` · Thiago Agustín Tirante v Aleksandr Shevchenko · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `661d7cd250941212b078c5b4707fbd0e04f66df6d1b85a8e8f571d21477e43d2`, 30058 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/chat_minis/20261112D3C239297F.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `POST_SCHEDULED_START_WRITE` (recorded `2026-11-13T01:11:16+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| D1 | Tirante +0.5 games | 0.5942 (SCENARIO_MIXTURE) | **WIN** | team margin +3 with handicap +0.5: cover by +3.5 | 0.164674 |
| D2 | Over 23.5 games | 0.5803 (SCENARIO_MIXTURE) | **WIN** | total 35 vs 23.5: +11.5 | 0.176148 |
| D3 | Under 23.5 games | 0.4197 (SCENARIO_MIXTURE) | **LOSS** | total 35 vs 23.5: +11.5 | 0.176148 |
| D4 | Shevchenko -0.5 games | 0.4058 (SCENARIO_MIXTURE) | **LOSS** | team margin -3 with handicap -0.5: cover by -3.5 | 0.164674 |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Tirante +0.5 games (0.5942) WIN; TOP_TOTAL Over 23.5 games (0.5803) WIN; RANK1 Tirante +0.5 games (0.5942) WIN. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Tirante d. Shevchenko 7-6(5) 6-7(5) 6-3; Games Tirante 19, Shevchenko 16; total 35; ATP 02:49:27; TennisExplorer start 15:20 (zone not stated). Identity matched on teams/players, date and competition (ATP 250 Stockholm Open, QF).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Tennis rows count every game of the completed match; no retirement.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Tirante games minus Shevchenko games = +3; total 35. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Two tiebreak sets and a deciding set produced 35 games, 11.5 over 23.5. Tirante won 19 games to 16.
**R9. Source/timing review.** Settlement sources: https://www.atptour.com/en/scores/current/stockholm/429/results (ALLOWED); https://www.tennisexplorer.com/stockholm/2026/atp-men/ (ALLOWED). Card timing `POST_SCHEDULED_START_WRITE`; self-declared phase labels: POST_SCHEDULED_START;TIMING_UNVERIFIED. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT LOCAL-20261112D3C239297F-G0003 revision-1 -->

### Deep loss reviews (DEEPLOSS-v1)

#### Deep loss review · Thiago Agustín Tirante v Aleksandr Shevchenko · Under 23.5 games

**1. Exact frozen claim.** `Under 23.5 games`, full-game endpoint as each record defined it. Triggered in 2 record(s):

| Record | Trigger role(s) | Original p (basis) | Brier | Log loss |
|---|---|---|---:|---:|
| `LOCAL-20261112CHAT9538BF5E-G0003` | TOP_TOTAL, RANK1 | NOT_ESTIMATED (QUALITATIVE_UNRANKED) |  |  |
| `LOCAL-20261112EE4AFA68-G0003` | TOP_TOTAL | NOT_ESTIMATED (QUALITATIVE) |  |  |

No record carried a primary p_card, frozen reference or same-row baseline; BASELINE_P comparison NOT_COMPUTABLE.

**2. Verified outcome.** Tirante d. Shevchenko 7-6(5) 6-7(5) 6-3 (Games Tirante 19, Shevchenko 16; total 35; ATP 02:49:27; TennisExplorer start 15:20 (zone not stated)). total 35 vs 23.5: +11.5. Sources in R9; evidence B; final wall-clock NOT_VERIFIED (duration 2:49:27).
**3. Distribution check.** Every triggering record was qualitative (NOT_ESTIMATED), so there is no frozen distribution to place the result in. Percentile placement inside each record's printed score object is not reconstructed; the printed objects stay in the cores.
**4. Error decomposition.** Realised line distance: total 35 vs 23.5: +11.5. No record had a calibrated centre or a measured effect-table row, so the miss cannot be split into reference error and adjustment error; no blame shares are invented.
**5. Research audit.** Recent-match game totals cited (6/10 and 7/10 under 24) are descriptive only; no opponent adjustment. Facts not re-opened here remain UNVERIFIED_AT_CUTOFF; no source in any card carries a captured retrieval receipt (chat-local research).
**6. What decided the game.** Two tiebreak sets and a deciding set produced 35 games, 11.5 over 23.5. Tirante won 19 games to 16.
**7. Knowable at cutoff?** Two evenly matched indoor servers made tiebreak sets plausible; most numeric chats priced Over at 53-58%. The final score and its timing were not knowable.
**8. Process audit.** Chat-local record; no repository reference stage, no source-audit receipts, no lineup confirmation, no freeze. Timing per record in CARD_TIMING.csv (several written after the scheduled start). Endpoint and contract definitions were correct.
**9. Verdict.** Should not have been preferred over Over: the only numeric models in the cohort all favoured Over; the qualitative chats overrode that without a stated reason.
**10. Cutoff-only counterfactual.** NOT_ESTIMATED: no knowable fact has a measured effect-table row, so no corrected probability is priced after the result.
**11. Failure class and recurrence.** Shared across 2 record(s) on one game: the parallel chats used overlapping public inputs, so their losses are one dependent observation, not 2 independent ones.
**12. Correction.** NO_CHANGE to any rule from one result. Procedure proposals are in AUDIT_REPORT §6 (PROPOSED_NOT_TESTED).
**13. Matched wins.** `LOCAL-20261112EE4AFA68-G0003` RANK1 Tirante +0.5 games WIN; `LOCAL-20261112EE4AFA68-G0003` TOP_SIDE Tirante +0.5 games WIN. These rest on the same unvalidated construction and do not show the process worked.
**14. Honesty.** Original numbers and labels preserved; no luck claim without the arithmetic above; no invented percentages, operator terms or publication times. Preservation PASS; information closure INCOMPLETE.

#### Deep loss review · Thiago Agustín Tirante v Aleksandr Shevchenko · Shevchenko -0.5 games

**1. Exact frozen claim.** `Shevchenko -0.5 games`, full-game endpoint as each record defined it. Triggered in 1 record(s):

| Record | Trigger role(s) | Original p (basis) | Brier | Log loss |
|---|---|---|---:|---:|
| `LOCAL-20261112CHAT9538BF5E-G0003` | TOP_SIDE | NOT_ESTIMATED (QUALITATIVE_UNRANKED) |  |  |

No record carried a primary p_card, frozen reference or same-row baseline; BASELINE_P comparison NOT_COMPUTABLE.

**2. Verified outcome.** Tirante d. Shevchenko 7-6(5) 6-7(5) 6-3 (Games Tirante 19, Shevchenko 16; total 35; ATP 02:49:27; TennisExplorer start 15:20 (zone not stated)). team margin -3 with handicap -0.5: cover by -3.5. Sources in R9; evidence B; final wall-clock NOT_VERIFIED (duration 2:49:27).
**3. Distribution check.** Every triggering record was qualitative (NOT_ESTIMATED), so there is no frozen distribution to place the result in. Percentile placement inside each record's printed score object is not reconstructed; the printed objects stay in the cores.
**4. Error decomposition.** Realised line distance: team margin -3 with handicap -0.5: cover by -3.5. No record had a calibrated centre or a measured effect-table row, so the miss cannot be split into reference error and adjustment error; no blame shares are invented.
**5. Research audit.** Shevchenko's 'four straight indoor wins' and qualifier run: consistent with the draw path; not opponent adjusted. Facts not re-opened here remain UNVERIFIED_AT_CUTOFF; no source in any card carries a captured retrieval receipt (chat-local research).
**6. What decided the game.** Two tiebreak sets and a deciding set produced 35 games, 11.5 over 23.5. Tirante won 19 games to 16.
**7. Knowable at cutoff?** Tirante's rest advantage (walkover in R16) was known and noted. The final score and its timing were not knowable.
**8. Process audit.** Chat-local record; no repository reference stage, no source-audit receipts, no lineup confirmation, no freeze. Timing per record in CARD_TIMING.csv (several written after the scheduled start). Endpoint and contract definitions were correct.
**9. Verdict.** Weak lean that the card itself rated below its total lean; the game margin was only 3, a narrow loss.
**10. Cutoff-only counterfactual.** NOT_ESTIMATED: no knowable fact has a measured effect-table row, so no corrected probability is priced after the result.
**11. Failure class and recurrence.** Shared across 1 record(s) on one game: the parallel chats used overlapping public inputs, so their losses are one dependent observation, not 1 independent ones.
**12. Correction.** NO_CHANGE to any rule from one result. Procedure proposals are in AUDIT_REPORT §6 (PROPOSED_NOT_TESTED).
**13. Matched wins.** None among the triggering records.
**14. Honesty.** Original numbers and labels preserved; no luck claim without the arithmetic above; no invented percentages, operator terms or publication times. Preservation PASS; information closure INCOMPLETE.

#### Joint section · top side and top total both lost · Thiago Agustín Tirante v Aleksandr Shevchenko

Records: `LOCAL-20261112CHAT9538BF5E-G0003`: Shevchenko -0.5 games and Under 23.5 games. Both legs failed on the same game state (Tirante d. Shevchenko 7-6(5) 6-7(5) 6-3). The cards' own joint-failure figures, where printed, are retained in the cores; none was calibrated, and treating the two leans as independent picks would double-count one wrong read of the game.

<!-- END SETTLEMENT EVENT E13 revision-1 -->

<!-- BEGIN SETTLEMENT EVENT E14 revision-1 -->
## Event · Geelong Venom (W) v Perth Lynx (W) · 2026-11-13 · WNBL 2026-27 Round 5

**Final:** Perth 95-76 Geelong (at Geelong). **Periods:** Perth-Geelong 21-19, 24-20, 29-17, 21-20; no OT. **Evidence C.** Scheduled 2026-11-13T08:00:00+00:00. Note: Only one opened source carries the score; evidence C.

| Opened source | Audit | Field read |
|---|---|---|
| https://www.basketball.com.au/news/wnbl27-round-5-geelong-venom-perth-lynx-match-report | ALLOWED | 'Perth won all four quarters, 21-19, 24-20, 29-17 and 21-20'; 95-76; published 14/11/2026 7:10 AM |
| https://www.wnbl.com.au/news/perth-lynx-dig-their-claws-into-geelong-venom | ALLOWED | WRONG GAME (28 Dec 2025, 106-78); excluded |

<!-- BEGIN SETTLEMENT LOCAL-20261112EE4AFA68-G0004 revision-1 -->
### Settlement · `LOCAL-20261112EE4AFA68-G0004` · Geelong Venom (W) v Perth Lynx (W) · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `17c94cd167170663bfaa8e18646e27b0ec609a4fec25a2c14c52d152245bbf6f`, 27755 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/chat_minis/20261112EE4AFA68.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `PRE_SCHEDULED_START_WRITE` (recorded `2026-11-13T18:56:31+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| T1 | Geelong +6.5 | NOT_ESTIMATED (QUALITATIVE) | **LOSS** | team margin -19 with handicap +6.5: cover by -12.5 |  |
| T2 | Under 163.5 | NOT_ESTIMATED (QUALITATIVE) | **LOSS** | total 171 vs 163.5: +7.5 |  |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Geelong +6.5 (NOT_ESTIMATED) LOSS; TOP_TOTAL Under 163.5 (NOT_ESTIMATED) LOSS; RANK1 Geelong +6.5 (NOT_ESTIMATED) LOSS. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Perth 95-76 Geelong (at Geelong); Perth-Geelong 21-19, 24-20, 29-17, 21-20; no OT. Identity matched on teams/players, date and competition (WNBL 2026-27 Round 5).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Basketball rows include overtime (BK-OT-1); none occurred.
**R4. Rank diagnostics.** 0W/2L/0U over 2 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Geelong minus Perth = -19; total 171. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Perth won every quarter and broke the game open in the third (29-17) to lead by 18; Amoore 21 points, six assists, four steals. Perth's 95 alone took the total to 171.
**R9. Source/timing review.** Settlement sources: https://www.basketball.com.au/news/wnbl27-round-5-geelong-venom-perth-lynx-match-report (ALLOWED); https://www.wnbl.com.au/news/perth-lynx-dig-their-claws-into-geelong-venom (ALLOWED). Card timing `PRE_SCHEDULED_START_WRITE`; self-declared phase labels: TIMING_UNVERIFIED. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT LOCAL-20261112EE4AFA68-G0004 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-20261112CHAT9538BF5E-G0004 revision-1 -->
### Settlement · `LOCAL-20261112CHAT9538BF5E-G0004` · Geelong Venom (W) v Perth Lynx (W) · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `fa6143e68aa25bc71fde3f88cc7ab318fe95a1453b277dcb008c9f529d3c7c63`, 23058 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/chat_minis/20261112CHAT9538BF5E.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `PRE_SCHEDULED_START_WRITE` (recorded `2026-11-13T18:55:17+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| LEAN_SIDE | Geelong +6.5 | NOT_ESTIMATED (QUALITATIVE_UNRANKED) | **LOSS** | team margin -19 with handicap +6.5: cover by -12.5 |  |
| LEAN_TOTAL | Under 163.5 | NOT_ESTIMATED (QUALITATIVE_UNRANKED) | **LOSS** | total 171 vs 163.5: +7.5 |  |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Geelong +6.5 (NOT_ESTIMATED) LOSS; TOP_TOTAL Under 163.5 (NOT_ESTIMATED) LOSS; RANK1 Geelong +6.5 (NOT_ESTIMATED) LOSS. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Perth 95-76 Geelong (at Geelong); Perth-Geelong 21-19, 24-20, 29-17, 21-20; no OT. Identity matched on teams/players, date and competition (WNBL 2026-27 Round 5).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Basketball rows include overtime (BK-OT-1); none occurred.
**R4. Rank diagnostics.** 0W/2L/0U over 2 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Geelong minus Perth = -19; total 171. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Perth won every quarter and broke the game open in the third (29-17) to lead by 18; Amoore 21 points, six assists, four steals. Perth's 95 alone took the total to 171.
**R9. Source/timing review.** Settlement sources: https://www.basketball.com.au/news/wnbl27-round-5-geelong-venom-perth-lynx-match-report (ALLOWED); https://www.wnbl.com.au/news/perth-lynx-dig-their-claws-into-geelong-venom (ALLOWED). Card timing `PRE_SCHEDULED_START_WRITE`; self-declared phase labels: TIMING_UNVERIFIED. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT LOCAL-20261112CHAT9538BF5E-G0004 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-202611128358B025-G0004 revision-1 -->
### Settlement · `LOCAL-202611128358B025-G0004` · Geelong Venom (W) v Perth Lynx (W) · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `80d6aef574cc688c5be4854d0e1ea3ac93aeefa6a7f9a4ec22654ed4a88e22f8`, 19553 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/chat_minis/202611128358B025.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `PRE_SCHEDULED_START_WRITE` (recorded `2026-11-13T18:56:18+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| D1 | Geelong +6.5 | 0.6081 (DIAGNOSTIC_LOCAL_MODEL) | **LOSS** | team margin -19 with handicap +6.5: cover by -12.5 | 0.369786 |
| D2 | Over 163.5 | 0.5088 (DIAGNOSTIC_LOCAL_MODEL) | **WIN** | total 171 vs 163.5: +7.5 | 0.241277 |
| D3 | Under 163.5 | 0.4912 (DIAGNOSTIC_LOCAL_MODEL) | **LOSS** | total 171 vs 163.5: +7.5 | 0.241277 |
| D4 | Perth -6.5 | 0.3919 (DIAGNOSTIC_LOCAL_MODEL) | **WIN** | team margin +19 with handicap -6.5: cover by +12.5 | 0.369786 |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Geelong +6.5 (0.6081) LOSS; TOP_TOTAL Over 163.5 (0.5088) WIN; RANK1 Geelong +6.5 (0.6081) LOSS. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Perth 95-76 Geelong (at Geelong); Perth-Geelong 21-19, 24-20, 29-17, 21-20; no OT. Identity matched on teams/players, date and competition (WNBL 2026-27 Round 5).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Basketball rows include overtime (BK-OT-1); none occurred.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Geelong minus Perth = -19; total 171. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Perth won every quarter and broke the game open in the third (29-17) to lead by 18; Amoore 21 points, six assists, four steals. Perth's 95 alone took the total to 171.
**R9. Source/timing review.** Settlement sources: https://www.basketball.com.au/news/wnbl27-round-5-geelong-venom-perth-lynx-match-report (ALLOWED); https://www.wnbl.com.au/news/perth-lynx-dig-their-claws-into-geelong-venom (ALLOWED). Card timing `PRE_SCHEDULED_START_WRITE`; self-declared phase labels: NONE_FOUND. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT LOCAL-202611128358B025-G0004 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-20261112CHAT17C8C881-G0004 revision-1 -->
### Settlement · `LOCAL-20261112CHAT17C8C881-G0004` · Geelong Venom (W) v Perth Lynx (W) · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `93e44d5875330b0e08703d91e7899a102e4c21ac31a0b93ab787551dc970a425`, 20895 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/chat_minis/20261112CHAT17C8C881.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `PRE_SCHEDULED_START_WRITE` (recorded `2026-11-13T18:49:00+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| LEAN_SIDE | Geelong +6.5 | NOT_STATED (ILLUSTRATIVE_GRID) | **LOSS** | team margin -19 with handicap +6.5: cover by -12.5 |  |
| LEAN_TOTAL | Under 163.5 | NOT_STATED (ILLUSTRATIVE_GRID) | **LOSS** | total 171 vs 163.5: +7.5 |  |
| WINNER | Perth outright | 0.599 (ILLUSTRATIVE_GRID) | **WIN** | team margin +19 | 0.160801 |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Perth outright (0.599) WIN; TOP_TOTAL Under 163.5 (NOT_STATED) LOSS; RANK1 Geelong +6.5 (NOT_STATED) LOSS. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Perth 95-76 Geelong (at Geelong); Perth-Geelong 21-19, 24-20, 29-17, 21-20; no OT. Identity matched on teams/players, date and competition (WNBL 2026-27 Round 5).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Basketball rows include overtime (BK-OT-1); none occurred.
**R4. Rank diagnostics.** 1W/2L/0U over 3 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Geelong minus Perth = -19; total 171. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Perth won every quarter and broke the game open in the third (29-17) to lead by 18; Amoore 21 points, six assists, four steals. Perth's 95 alone took the total to 171.
**R9. Source/timing review.** Settlement sources: https://www.basketball.com.au/news/wnbl27-round-5-geelong-venom-perth-lynx-match-report (ALLOWED); https://www.wnbl.com.au/news/perth-lynx-dig-their-claws-into-geelong-venom (ALLOWED). Card timing `PRE_SCHEDULED_START_WRITE`; self-declared phase labels: PRE_SCHEDULED_START. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT LOCAL-20261112CHAT17C8C881-G0004 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-20261112CC53B5C806-G0004 revision-1 -->
### Settlement · `LOCAL-20261112CC53B5C806-G0004` · Geelong Venom (W) v Perth Lynx (W) · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `48cadd98f4ca5765d28f284633f7b90d464c7c74229773bf26ba5045a2b61269`, 29466 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/chat_minis/20261112CC53B5C806.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `WRITE_TIME_NOT_RECORDED` (recorded `NOT_RECORDED`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| 1 | Geelong +6.5 | 0.6054 (SHADOW_SCENARIO) | **LOSS** | team margin -19 with handicap +6.5: cover by -12.5 | 0.366509 |
| 2 | Over 163.5 | 0.5358 (SHADOW_SCENARIO) | **WIN** | total 171 vs 163.5: +7.5 | 0.215482 |
| INFO | Under 163.5 | 0.4642 (SHADOW_SCENARIO) | **LOSS** | total 171 vs 163.5: +7.5 | 0.215482 |
| INFO | Perth -6.5 | 0.3946 (SHADOW_SCENARIO) | **WIN** | team margin +19 with handicap -6.5: cover by +12.5 | 0.366509 |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Geelong +6.5 (0.6054) LOSS; TOP_TOTAL Over 163.5 (0.5358) WIN; RANK1 Geelong +6.5 (0.6054) LOSS. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Perth 95-76 Geelong (at Geelong); Perth-Geelong 21-19, 24-20, 29-17, 21-20; no OT. Identity matched on teams/players, date and competition (WNBL 2026-27 Round 5).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Basketball rows include overtime (BK-OT-1); none occurred.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Geelong minus Perth = -19; total 171. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Perth won every quarter and broke the game open in the third (29-17) to lead by 18; Amoore 21 points, six assists, four steals. Perth's 95 alone took the total to 171.
**R9. Source/timing review.** Settlement sources: https://www.basketball.com.au/news/wnbl27-round-5-geelong-venom-perth-lynx-match-report (ALLOWED); https://www.wnbl.com.au/news/perth-lynx-dig-their-claws-into-geelong-venom (ALLOWED). Card timing `WRITE_TIME_NOT_RECORDED`; self-declared phase labels: NONE_FOUND. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT LOCAL-20261112CC53B5C806-G0004 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-20261112D3C239297F-G0004 revision-1 -->
### Settlement · `LOCAL-20261112D3C239297F-G0004` · Geelong Venom (W) v Perth Lynx (W) · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `4b751a56828f9e52efe225def2f1f6ee008bf0da5ef7f1e6671c3d8bc44b008a`, 27129 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/chat_minis/20261112D3C239297F.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `PRE_SCHEDULED_START_WRITE` (recorded `2026-11-13T18:59:43+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| D1 | Geelong +6.5 | 0.5577 (SCENARIO_MC) | **LOSS** | team margin -19 with handicap +6.5: cover by -12.5 | 0.311029 |
| D2 | Over 163.5 | 0.5261 (SCENARIO_MC) | **WIN** | total 171 vs 163.5: +7.5 | 0.224581 |
| D3 | Under 163.5 | 0.4739 (SCENARIO_MC) | **LOSS** | total 171 vs 163.5: +7.5 | 0.224581 |
| D4 | Perth -6.5 | 0.4423 (SCENARIO_MC) | **WIN** | team margin +19 with handicap -6.5: cover by +12.5 | 0.311029 |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Geelong +6.5 (0.5577) LOSS; TOP_TOTAL Over 163.5 (0.5261) WIN; RANK1 Geelong +6.5 (0.5577) LOSS. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Perth 95-76 Geelong (at Geelong); Perth-Geelong 21-19, 24-20, 29-17, 21-20; no OT. Identity matched on teams/players, date and competition (WNBL 2026-27 Round 5).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Basketball rows include overtime (BK-OT-1); none occurred.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Geelong minus Perth = -19; total 171. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Perth won every quarter and broke the game open in the third (29-17) to lead by 18; Amoore 21 points, six assists, four steals. Perth's 95 alone took the total to 171.
**R9. Source/timing review.** Settlement sources: https://www.basketball.com.au/news/wnbl27-round-5-geelong-venom-perth-lynx-match-report (ALLOWED); https://www.wnbl.com.au/news/perth-lynx-dig-their-claws-into-geelong-venom (ALLOWED). Card timing `PRE_SCHEDULED_START_WRITE`; self-declared phase labels: PRE_SCHEDULED_START_RESEARCH;TIMING_UNVERIFIED. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT LOCAL-20261112D3C239297F-G0004 revision-1 -->

### Deep loss reviews (DEEPLOSS-v1)

#### Deep loss review · Geelong Venom (W) v Perth Lynx (W) · Geelong +6.5

**1. Exact frozen claim.** `Geelong +6.5`, full-game endpoint as each record defined it. Triggered in 6 record(s):

| Record | Trigger role(s) | Original p (basis) | Brier | Log loss |
|---|---|---|---:|---:|
| `LOCAL-202611128358B025-G0004` | TOP_SIDE, RANK1 | 0.6081 (DIAGNOSTIC_LOCAL_MODEL) | 0.369786 | 0.936749 |
| `LOCAL-20261112CC53B5C806-G0004` | TOP_SIDE, RANK1 | 0.6054 (SHADOW_SCENARIO) | 0.366509 | 0.929883 |
| `LOCAL-20261112CHAT17C8C881-G0004` | RANK1 | NOT_STATED (ILLUSTRATIVE_GRID) |  |  |
| `LOCAL-20261112CHAT9538BF5E-G0004` | TOP_SIDE, RANK1 | NOT_ESTIMATED (QUALITATIVE_UNRANKED) |  |  |
| `LOCAL-20261112D3C239297F-G0004` | TOP_SIDE, RANK1 | 0.5577 (SCENARIO_MC) | 0.311029 | 0.815767 |
| `LOCAL-20261112EE4AFA68-G0004` | TOP_SIDE, RANK1 | NOT_ESTIMATED (QUALITATIVE) |  |  |

No record carried a primary p_card, frozen reference or same-row baseline; BASELINE_P comparison NOT_COMPUTABLE.

**2. Verified outcome.** Perth 95-76 Geelong (at Geelong) (Perth-Geelong 21-19, 24-20, 29-17, 21-20; no OT). team margin -19 with handicap +6.5: cover by -12.5. Sources in R9; evidence C; final wall-clock NOT_VERIFIED.
**3. Distribution check.** Numeric records priced this row at 0.558-0.608 (mean 0.590); a loss at those prices is a 39%-44% event under each record's own uncalibrated object. Percentile placement inside each record's printed score object is not reconstructed; the printed objects stay in the cores.
**4. Error decomposition.** Realised line distance: team margin -19 with handicap +6.5: cover by -12.5. No record had a calibrated centre or a measured effect-table row, so the miss cannot be split into reference error and adjustment error; no blame shares are invented.
**5. Research audit.** Bec Cole OUT and Perth 'no new injuries' were from the WNBL 13 Nov preview (published before tip, minute not captured). Geelong's 143-147 post-debut totals and Perth's 169-185 totals are TRUE per the cited schedule rows. No card had possession or efficiency data. Facts not re-opened here remain UNVERIFIED_AT_CUTOFF; no source in any card carries a captured retrieval receipt (chat-local research).
**6. What decided the game.** Perth won every quarter and broke the game open in the third (29-17) to lead by 18; Amoore 21 points, six assists, four steals. Perth's 95 alone took the total to 171.
**7. Knowable at cutoff?** Perth's 89.0 PPG and 3-1 record, and Geelong's three home losses by 9+ to good teams, were all printed as counter-evidence. The final score and its timing were not knowable.
**8. Process audit.** Chat-local record; no repository reference stage, no source-audit receipts, no lineup confirmation, no freeze. Timing per record in CARD_TIMING.csv (several written after the scheduled start). Endpoint and contract definitions were correct.
**9. Verdict.** Should not have been treated as the side lean by all six chats: the 'simple paired margin -2 to -3.3' ignored that Geelong lost to every above-.500 opponent by 9+. Perth won every quarter; this is a model failure (no opponent-quality adjustment), not variance.
**10. Cutoff-only counterfactual.** NOT_ESTIMATED: no knowable fact has a measured effect-table row, so no corrected probability is priced after the result.
**11. Failure class and recurrence.** Shared across 6 record(s) on one game: the parallel chats used overlapping public inputs, so their losses are one dependent observation, not 6 independent ones.
**12. Correction.** NO_CHANGE to any rule from one result. Procedure proposals are in AUDIT_REPORT §6 (PROPOSED_NOT_TESTED).
**13. Matched wins.** `LOCAL-202611128358B025-G0004` TOP_TOTAL Over 163.5 WIN; `LOCAL-20261112CC53B5C806-G0004` TOP_TOTAL Over 163.5 WIN; `LOCAL-20261112CHAT17C8C881-G0004` TOP_SIDE Perth outright WIN; `LOCAL-20261112D3C239297F-G0004` TOP_TOTAL Over 163.5 WIN. These rest on the same unvalidated construction and do not show the process worked.
**14. Honesty.** Original numbers and labels preserved; no luck claim without the arithmetic above; no invented percentages, operator terms or publication times. Preservation PASS; information closure INCOMPLETE.

#### Deep loss review · Geelong Venom (W) v Perth Lynx (W) · Under 163.5

**1. Exact frozen claim.** `Under 163.5`, full-game endpoint as each record defined it. Triggered in 3 record(s):

| Record | Trigger role(s) | Original p (basis) | Brier | Log loss |
|---|---|---|---:|---:|
| `LOCAL-20261112CHAT17C8C881-G0004` | TOP_TOTAL | NOT_STATED (ILLUSTRATIVE_GRID) |  |  |
| `LOCAL-20261112CHAT9538BF5E-G0004` | TOP_TOTAL | NOT_ESTIMATED (QUALITATIVE_UNRANKED) |  |  |
| `LOCAL-20261112EE4AFA68-G0004` | TOP_TOTAL | NOT_ESTIMATED (QUALITATIVE) |  |  |

No record carried a primary p_card, frozen reference or same-row baseline; BASELINE_P comparison NOT_COMPUTABLE.

**2. Verified outcome.** Perth 95-76 Geelong (at Geelong) (Perth-Geelong 21-19, 24-20, 29-17, 21-20; no OT). total 171 vs 163.5: +7.5. Sources in R9; evidence C; final wall-clock NOT_VERIFIED.
**3. Distribution check.** Every triggering record was qualitative (NOT_ESTIMATED), so there is no frozen distribution to place the result in. Percentile placement inside each record's printed score object is not reconstructed; the printed objects stay in the cores.
**4. Error decomposition.** Realised line distance: total 171 vs 163.5: +7.5. No record had a calibrated centre or a measured effect-table row, so the miss cannot be split into reference error and adjustment error; no blame shares are invented.
**5. Research audit.** Geelong home totals 143-147 TRUE; Perth's four totals all 169+ TRUE. Facts not re-opened here remain UNVERIFIED_AT_CUTOFF; no source in any card carries a captured retrieval receipt (chat-local research).
**6. What decided the game.** Perth won every quarter and broke the game open in the third (29-17) to lead by 18; Amoore 21 points, six assists, four steals. Perth's 95 alone took the total to 171.
**7. Knowable at cutoff?** The chats' own numbers put the total centre at 160.75-165.5 with SD ~17-21, i.e. a coin flip. The final score and its timing were not knowable.
**8. Process audit.** Chat-local record; no repository reference stage, no source-audit receipts, no lineup confirmation, no freeze. Timing per record in CARD_TIMING.csv (several written after the scheduled start). Endpoint and contract definitions were correct.
**9. Verdict.** A coin-flip total that two qualitative chats picked over the numeric chats' slight Over; Perth's 95 alone made it Over.
**10. Cutoff-only counterfactual.** NOT_ESTIMATED: no knowable fact has a measured effect-table row, so no corrected probability is priced after the result.
**11. Failure class and recurrence.** Shared across 3 record(s) on one game: the parallel chats used overlapping public inputs, so their losses are one dependent observation, not 3 independent ones.
**12. Correction.** NO_CHANGE to any rule from one result. Procedure proposals are in AUDIT_REPORT §6 (PROPOSED_NOT_TESTED).
**13. Matched wins.** `LOCAL-20261112CHAT17C8C881-G0004` TOP_SIDE Perth outright WIN. These rest on the same unvalidated construction and do not show the process worked.
**14. Honesty.** Original numbers and labels preserved; no luck claim without the arithmetic above; no invented percentages, operator terms or publication times. Preservation PASS; information closure INCOMPLETE.

#### Joint section · top side and top total both lost · Geelong Venom (W) v Perth Lynx (W)

Records: `LOCAL-20261112EE4AFA68-G0004`: Geelong +6.5 and Under 163.5; `LOCAL-20261112CHAT9538BF5E-G0004`: Geelong +6.5 and Under 163.5. Both legs failed on the same game state (Perth 95-76 Geelong (at Geelong)). The cards' own joint-failure figures, where printed, are retained in the cores; none was calibrated, and treating the two leans as independent picks would double-count one wrong read of the game.

<!-- END SETTLEMENT EVENT E14 revision-1 -->

<!-- BEGIN SETTLEMENT EVENT E15 revision-1 -->
## Event · Wonju DB Promy v Suwon KT Sonicboom · 2026-11-13 · KBL 2026-27 Round 2

**Final:** Wonju DB 94-83 Suwon KT. **Periods:** Q1 23-17, half 51-41, after Q3 69-66 (stated); derived Q2 28-24, Q3 18-25, Q4 25-17; no OT. **Evidence B.** Scheduled 2026-11-13T10:00:00+00:00.

| Opened source | Audit | Field read |
|---|---|---|
| http://www.rookie.co.kr/news/articleView.html?idxno=130306 | ALLOWED | '94-83으로 승리'; Q1 23-17; half 51-41; Q4 began 69-66; entered 2026.11.13 20:54 |
| https://star.ohmynews.com/NWS_Web/OhmyStar/at_pg.aspx?CNTN_CD=A0003284916&PAGE_CD=N0002&BLCK_NO=&CMPT_CD=M0147 | ALLOWED | 94-83; half 51-41; 26.11.14 10:59 |

<!-- BEGIN SETTLEMENT LOCAL-20261112EE4AFA68-G0005 revision-1 -->
### Settlement · `LOCAL-20261112EE4AFA68-G0005` · Wonju DB Promy v Suwon KT Sonicboom · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `b2d7cf7339ef7c47eb28fc69696fee896b75f3150f0f8bb3121410510be078ee`, 29796 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/chat_minis/20261112EE4AFA68.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `POST_SCHEDULED_START_WRITE` (recorded `2026-11-13T21:04:59+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| T1 | Under 179.5 | NOT_ESTIMATED (QUALITATIVE) | **WIN** | total 177 vs 179.5: -2.5 |  |
| T2 | Suwon KT +5.5 | NOT_ESTIMATED (QUALITATIVE) | **LOSS** | team margin -11 with handicap +5.5: cover by -5.5 |  |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Suwon KT +5.5 (NOT_ESTIMATED) LOSS; TOP_TOTAL Under 179.5 (NOT_ESTIMATED) WIN; RANK1 Under 179.5 (NOT_ESTIMATED) WIN. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Wonju DB 94-83 Suwon KT; Q1 23-17, half 51-41, after Q3 69-66 (stated); derived Q2 28-24, Q3 18-25, Q4 25-17; no OT. Identity matched on teams/players, date and competition (KBL 2026-27 Round 2).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Basketball rows include overtime (BK-OT-1); none occurred.
**R4. Rank diagnostics.** 1W/1L/0U over 2 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Wonju minus Suwon = +11; total 177. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Henry Ellenson returned from a seven-game absence with 28 points and 10 rebounds; Alvano 20 and 9 assists. KT closed to 69-66 after three quarters, then DB won the fourth 25-17. Margin 11 (Wonju -5.5 by 5.5); total 177 (Under 179.5 by 2.5).
**R9. Source/timing review.** Settlement sources: http://www.rookie.co.kr/news/articleView.html?idxno=130306 (ALLOWED); https://star.ohmynews.com/NWS_Web/OhmyStar/at_pg.aspx?CNTN_CD=A0003284916&PAGE_CD=N0002&BLCK_NO=&CMPT_CD=M0147 (ALLOWED). Card timing `POST_SCHEDULED_START_WRITE`; self-declared phase labels: TIMING_UNVERIFIED. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT LOCAL-20261112EE4AFA68-G0005 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-20261112CHAT9538BF5E-G0005 revision-1 -->
### Settlement · `LOCAL-20261112CHAT9538BF5E-G0005` · Wonju DB Promy v Suwon KT Sonicboom · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `bab6c3a528a3fb2b96b6d0b144a893ebe814455422d5a48fad88421881f4366f`, 22653 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/chat_minis/20261112CHAT9538BF5E.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `POST_SCHEDULED_START_WRITE` (recorded `2026-11-13T21:01:37+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| LEAN_TOTAL | Under 179.5 | NOT_ESTIMATED (QUALITATIVE_UNRANKED) | **WIN** | total 177 vs 179.5: -2.5 |  |
| LEAN_SIDE | Wonju DB -5.5 | NOT_ESTIMATED (QUALITATIVE_UNRANKED) | **WIN** | team margin +11 with handicap -5.5: cover by +5.5 |  |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Wonju DB -5.5 (NOT_ESTIMATED) WIN; TOP_TOTAL Under 179.5 (NOT_ESTIMATED) WIN; RANK1 Under 179.5 (NOT_ESTIMATED) WIN. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Wonju DB 94-83 Suwon KT; Q1 23-17, half 51-41, after Q3 69-66 (stated); derived Q2 28-24, Q3 18-25, Q4 25-17; no OT. Identity matched on teams/players, date and competition (KBL 2026-27 Round 2).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Basketball rows include overtime (BK-OT-1); none occurred.
**R4. Rank diagnostics.** 2W/0L/0U over 2 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Wonju minus Suwon = +11; total 177. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Henry Ellenson returned from a seven-game absence with 28 points and 10 rebounds; Alvano 20 and 9 assists. KT closed to 69-66 after three quarters, then DB won the fourth 25-17. Margin 11 (Wonju -5.5 by 5.5); total 177 (Under 179.5 by 2.5).
**R9. Source/timing review.** Settlement sources: http://www.rookie.co.kr/news/articleView.html?idxno=130306 (ALLOWED); https://star.ohmynews.com/NWS_Web/OhmyStar/at_pg.aspx?CNTN_CD=A0003284916&PAGE_CD=N0002&BLCK_NO=&CMPT_CD=M0147 (ALLOWED). Card timing `POST_SCHEDULED_START_WRITE`; self-declared phase labels: NONE_FOUND. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT LOCAL-20261112CHAT9538BF5E-G0005 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-202611128358B025-G0005 revision-1 -->
### Settlement · `LOCAL-202611128358B025-G0005` · Wonju DB Promy v Suwon KT Sonicboom · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `2a7ead867c0199d9c992a8ddba5526090f056a7cfe0f90dbda7237b7ce3253f4`, 19336 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/chat_minis/202611128358B025.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `POST_SCHEDULED_START_WRITE` (recorded `2026-11-13T21:02:36+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| D1 | Under 179.5 | 0.56037 (LOCAL_GAUSSIAN) | **WIN** | total 177 vs 179.5: -2.5 | 0.193275 |
| D2 | Suwon KT +5.5 | 0.53497 (LOCAL_GAUSSIAN) | **LOSS** | team margin -11 with handicap +5.5: cover by -5.5 | 0.286193 |
| D3 | Wonju DB -5.5 | 0.46503 (LOCAL_GAUSSIAN) | **WIN** | team margin +11 with handicap -5.5: cover by +5.5 | 0.286193 |
| D4 | Over 179.5 | 0.43963 (LOCAL_GAUSSIAN) | **LOSS** | total 177 vs 179.5: -2.5 | 0.193275 |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Suwon KT +5.5 (0.53497) LOSS; TOP_TOTAL Under 179.5 (0.56037) WIN; RANK1 Under 179.5 (0.56037) WIN. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Wonju DB 94-83 Suwon KT; Q1 23-17, half 51-41, after Q3 69-66 (stated); derived Q2 28-24, Q3 18-25, Q4 25-17; no OT. Identity matched on teams/players, date and competition (KBL 2026-27 Round 2).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Basketball rows include overtime (BK-OT-1); none occurred.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Wonju minus Suwon = +11; total 177. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Henry Ellenson returned from a seven-game absence with 28 points and 10 rebounds; Alvano 20 and 9 assists. KT closed to 69-66 after three quarters, then DB won the fourth 25-17. Margin 11 (Wonju -5.5 by 5.5); total 177 (Under 179.5 by 2.5).
**R9. Source/timing review.** Settlement sources: http://www.rookie.co.kr/news/articleView.html?idxno=130306 (ALLOWED); https://star.ohmynews.com/NWS_Web/OhmyStar/at_pg.aspx?CNTN_CD=A0003284916&PAGE_CD=N0002&BLCK_NO=&CMPT_CD=M0147 (ALLOWED). Card timing `POST_SCHEDULED_START_WRITE`; self-declared phase labels: NONE_FOUND. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT LOCAL-202611128358B025-G0005 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-20261112CHAT17C8C881-G0005 revision-1 -->
### Settlement · `LOCAL-20261112CHAT17C8C881-G0005` · Wonju DB Promy v Suwon KT Sonicboom · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `8cae71751f683680f4ab337bdbbc62772642f02b68ff9311605e3d7f6c4e19fa`, 19514 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/chat_minis/20261112CHAT17C8C881.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `POST_SCHEDULED_START_WRITE` (recorded `2026-11-13T21:03:02+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| D1 | Under 179.5 | 0.5573 (HYPOTHETICAL_GRID) | **WIN** | total 177 vs 179.5: -2.5 | 0.195983 |
| D2 | Suwon KT +5.5 | 0.5125 (HYPOTHETICAL_GRID) | **LOSS** | team margin -11 with handicap +5.5: cover by -5.5 | 0.262656 |
| D3 | Wonju DB -5.5 | 0.4875 (HYPOTHETICAL_GRID) | **WIN** | team margin +11 with handicap -5.5: cover by +5.5 | 0.262656 |
| D4 | Over 179.5 | 0.4427 (HYPOTHETICAL_GRID) | **LOSS** | total 177 vs 179.5: -2.5 | 0.195983 |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Suwon KT +5.5 (0.5125) LOSS; TOP_TOTAL Under 179.5 (0.5573) WIN; RANK1 Under 179.5 (0.5573) WIN. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Wonju DB 94-83 Suwon KT; Q1 23-17, half 51-41, after Q3 69-66 (stated); derived Q2 28-24, Q3 18-25, Q4 25-17; no OT. Identity matched on teams/players, date and competition (KBL 2026-27 Round 2).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Basketball rows include overtime (BK-OT-1); none occurred.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Wonju minus Suwon = +11; total 177. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Henry Ellenson returned from a seven-game absence with 28 points and 10 rebounds; Alvano 20 and 9 assists. KT closed to 69-66 after three quarters, then DB won the fourth 25-17. Margin 11 (Wonju -5.5 by 5.5); total 177 (Under 179.5 by 2.5).
**R9. Source/timing review.** Settlement sources: http://www.rookie.co.kr/news/articleView.html?idxno=130306 (ALLOWED); https://star.ohmynews.com/NWS_Web/OhmyStar/at_pg.aspx?CNTN_CD=A0003284916&PAGE_CD=N0002&BLCK_NO=&CMPT_CD=M0147 (ALLOWED). Card timing `POST_SCHEDULED_START_WRITE`; self-declared phase labels: NONE_FOUND. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT LOCAL-20261112CHAT17C8C881-G0005 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-20261112CC53B5C806-G0005 revision-1 -->
### Settlement · `LOCAL-20261112CC53B5C806-G0005` · Wonju DB Promy v Suwon KT Sonicboom · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `7b5579bb9416c5571a4f9ab9df359246207a5d38e7ece98dbeccadeeb95f3904`, 22630 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/chat_minis/20261112CC53B5C806.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `WRITE_TIME_NOT_RECORDED` (recorded `NOT_RECORDED`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| 1 | Under 179.5 | 0.5588 (SHADOW_MC) | **WIN** | total 177 vs 179.5: -2.5 | 0.194657 |
| 2 | Wonju DB -5.5 | 0.5157 (SHADOW_MC) | **WIN** | team margin +11 with handicap -5.5: cover by +5.5 | 0.234546 |
| INFO | Suwon KT +5.5 | 0.4843 (SHADOW_MC) | **LOSS** | team margin -11 with handicap +5.5: cover by -5.5 | 0.234546 |
| INFO | Over 179.5 | 0.4412 (SHADOW_MC) | **LOSS** | total 177 vs 179.5: -2.5 | 0.194657 |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Wonju DB -5.5 (0.5157) WIN; TOP_TOTAL Under 179.5 (0.5588) WIN; RANK1 Under 179.5 (0.5588) WIN. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Wonju DB 94-83 Suwon KT; Q1 23-17, half 51-41, after Q3 69-66 (stated); derived Q2 28-24, Q3 18-25, Q4 25-17; no OT. Identity matched on teams/players, date and competition (KBL 2026-27 Round 2).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Basketball rows include overtime (BK-OT-1); none occurred.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Wonju minus Suwon = +11; total 177. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Henry Ellenson returned from a seven-game absence with 28 points and 10 rebounds; Alvano 20 and 9 assists. KT closed to 69-66 after three quarters, then DB won the fourth 25-17. Margin 11 (Wonju -5.5 by 5.5); total 177 (Under 179.5 by 2.5).
**R9. Source/timing review.** Settlement sources: http://www.rookie.co.kr/news/articleView.html?idxno=130306 (ALLOWED); https://star.ohmynews.com/NWS_Web/OhmyStar/at_pg.aspx?CNTN_CD=A0003284916&PAGE_CD=N0002&BLCK_NO=&CMPT_CD=M0147 (ALLOWED). Card timing `WRITE_TIME_NOT_RECORDED`; self-declared phase labels: NONE_FOUND. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT LOCAL-20261112CC53B5C806-G0005 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-20261112D3C239297F-G0005 revision-1 -->
### Settlement · `LOCAL-20261112D3C239297F-G0005` · Wonju DB Promy v Suwon KT Sonicboom · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `50cfef0a9d6731e596fe97582b168895a3dddfbb3acce3dc6911e503741d8a36`, 22751 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/chat_minis/20261112D3C239297F.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `POST_SCHEDULED_START_WRITE` (recorded `2026-11-13T21:03:22+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| D1 | Under 179.5 | 0.5565 (SCENARIO_MC) | **WIN** | total 177 vs 179.5: -2.5 | 0.196692 |
| D2 | Suwon KT +5.5 | 0.5064 (SCENARIO_MC) | **LOSS** | team margin -11 with handicap +5.5: cover by -5.5 | 0.256441 |
| D3 | Wonju DB -5.5 | 0.4936 (SCENARIO_MC) | **WIN** | team margin +11 with handicap -5.5: cover by +5.5 | 0.256441 |
| D4 | Over 179.5 | 0.4435 (SCENARIO_MC) | **LOSS** | total 177 vs 179.5: -2.5 | 0.196692 |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Suwon KT +5.5 (0.5064) LOSS; TOP_TOTAL Under 179.5 (0.5565) WIN; RANK1 Under 179.5 (0.5565) WIN. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Wonju DB 94-83 Suwon KT; Q1 23-17, half 51-41, after Q3 69-66 (stated); derived Q2 28-24, Q3 18-25, Q4 25-17; no OT. Identity matched on teams/players, date and competition (KBL 2026-27 Round 2).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Basketball rows include overtime (BK-OT-1); none occurred.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Wonju minus Suwon = +11; total 177. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Henry Ellenson returned from a seven-game absence with 28 points and 10 rebounds; Alvano 20 and 9 assists. KT closed to 69-66 after three quarters, then DB won the fourth 25-17. Margin 11 (Wonju -5.5 by 5.5); total 177 (Under 179.5 by 2.5).
**R9. Source/timing review.** Settlement sources: http://www.rookie.co.kr/news/articleView.html?idxno=130306 (ALLOWED); https://star.ohmynews.com/NWS_Web/OhmyStar/at_pg.aspx?CNTN_CD=A0003284916&PAGE_CD=N0002&BLCK_NO=&CMPT_CD=M0147 (ALLOWED). Card timing `POST_SCHEDULED_START_WRITE`; self-declared phase labels: TIMING_UNVERIFIED. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT LOCAL-20261112D3C239297F-G0005 revision-1 -->

### Deep loss reviews (DEEPLOSS-v1)

#### Deep loss review · Wonju DB Promy v Suwon KT Sonicboom · Suwon KT +5.5

**1. Exact frozen claim.** `Suwon KT +5.5`, full-game endpoint as each record defined it. Triggered in 4 record(s):

| Record | Trigger role(s) | Original p (basis) | Brier | Log loss |
|---|---|---|---:|---:|
| `LOCAL-202611128358B025-G0005` | TOP_SIDE | 0.53497 (LOCAL_GAUSSIAN) | 0.286193 | 0.765653 |
| `LOCAL-20261112CHAT17C8C881-G0005` | TOP_SIDE | 0.5125 (HYPOTHETICAL_GRID) | 0.262656 | 0.718465 |
| `LOCAL-20261112D3C239297F-G0005` | TOP_SIDE | 0.5064 (SCENARIO_MC) | 0.256441 | 0.706030 |
| `LOCAL-20261112EE4AFA68-G0005` | TOP_SIDE | NOT_ESTIMATED (QUALITATIVE) |  |  |

No record carried a primary p_card, frozen reference or same-row baseline; BASELINE_P comparison NOT_COMPUTABLE.

**2. Verified outcome.** Wonju DB 94-83 Suwon KT (Q1 23-17, half 51-41, after Q3 69-66 (stated); derived Q2 28-24, Q3 18-25, Q4 25-17; no OT). team margin -11 with handicap +5.5: cover by -5.5. Sources in R9; evidence B; final wall-clock NOT_VERIFIED.
**3. Distribution check.** Numeric records priced this row at 0.506-0.535 (mean 0.518); a loss at those prices is a 47%-49% event under each record's own uncalibrated object. Percentile placement inside each record's printed score object is not reconstructed; the printed objects stay in the cores.
**4. Error decomposition.** Realised line distance: team margin -11 with handicap +5.5: cover by -5.5. No record had a calibrated centre or a measured effect-table row, so the miss cannot be split into reference error and adjustment error; no blame shares are invented.
**5. Research audit.** Ellenson's expected return was in the 13 Nov Jumpball preview (10:45 KST) cited by D3C; he played and scored 28/10, so the availability fact was TRUE and decisive. KT's three absences: consistent with KT's thin rotation. Facts not re-opened here remain UNVERIFIED_AT_CUTOFF; no source in any card carries a captured retrieval receipt (chat-local research).
**6. What decided the game.** Henry Ellenson returned from a seven-game absence with 28 points and 10 rebounds; Alvano 20 and 9 assists. KT closed to 69-66 after three quarters, then DB won the fourth 25-17. Margin 11 (Wonju -5.5 by 5.5); total 177 (Under 179.5 by 2.5).
**7. Knowable at cutoff?** Ellenson's return was KNOWABLE before tip and the cards named it as the main risk; 8358's own sensitivity showed KT +5.5 falling to 43.9% with a +6 Ellenson effect. The final score and its timing were not knowable.
**8. Process audit.** Chat-local record; no repository reference stage, no source-audit receipts, no lineup confirmation, no freeze. Timing per record in CARD_TIMING.csv (several written after the scheduled start). Endpoint and contract definitions were correct.
**9. Verdict.** Should not have been preferred: the chats identified the decisive input and still kept the pre-return margin centre. That is an unpriced availability effect, the exact failure the AVAIL protocol targets.
**10. Cutoff-only counterfactual.** NOT_ESTIMATED: no knowable fact has a measured effect-table row, so no corrected probability is priced after the result.
**11. Failure class and recurrence.** Shared across 4 record(s) on one game: the parallel chats used overlapping public inputs, so their losses are one dependent observation, not 4 independent ones.
**12. Correction.** NO_CHANGE to any rule from one result. Procedure proposals are in AUDIT_REPORT §6 (PROPOSED_NOT_TESTED).
**13. Matched wins.** `LOCAL-202611128358B025-G0005` RANK1 Under 179.5 WIN; `LOCAL-202611128358B025-G0005` TOP_TOTAL Under 179.5 WIN; `LOCAL-20261112CHAT17C8C881-G0005` RANK1 Under 179.5 WIN; `LOCAL-20261112CHAT17C8C881-G0005` TOP_TOTAL Under 179.5 WIN; `LOCAL-20261112D3C239297F-G0005` RANK1 Under 179.5 WIN; `LOCAL-20261112D3C239297F-G0005` TOP_TOTAL Under 179.5 WIN; `LOCAL-20261112EE4AFA68-G0005` RANK1 Under 179.5 WIN; `LOCAL-20261112EE4AFA68-G0005` TOP_TOTAL Under 179.5 WIN. These rest on the same unvalidated construction and do not show the process worked.
**14. Honesty.** Original numbers and labels preserved; no luck claim without the arithmetic above; no invented percentages, operator terms or publication times. Preservation PASS; information closure INCOMPLETE.

<!-- END SETTLEMENT EVENT E15 revision-1 -->

<!-- BEGIN SETTLEMENT EVENT E16 revision-1 -->
## Event · Kawasaki Brave Thunders v Saga Ballooners · 2026-11-13 · B.LEAGUE PREMIER 2026-27, ScheduleKey 506581

**Final:** Kawasaki 90-72 Saga. **Periods:** Quarter scores shown only as an image on permitted pages: NOT_VERIFIED; no OT indicated. **Evidence B.** Scheduled 2026-11-13T10:05:00+00:00.

| Opened source | Audit | Field read |
|---|---|---|
| https://www.bleague.jp/game_detail/?ScheduleKey=506581&tab=1 | ALLOWED | Final 90-72; '19:05 TIP OFF' |
| https://kawasaki-bravethunders.com/topics_detail43/id=25910 | ALLOWED | '11/13 ○川崎 90-72 佐賀●' |

<!-- BEGIN SETTLEMENT LOCAL-20261112EE4AFA68-G0006 revision-1 -->
### Settlement · `LOCAL-20261112EE4AFA68-G0006` · Kawasaki Brave Thunders v Saga Ballooners · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `8095952ecb087fb39b8dae0fa9189116c585b7d80917ab6962b3bcaa81ccf772`, 31715 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/chat_minis/20261112EE4AFA68.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `POST_SCHEDULED_START_WRITE` (recorded `2026-11-13T21:17:35+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| T1 | Saga +9.5 | NOT_ESTIMATED (QUALITATIVE) | **LOSS** | team margin -18 with handicap +9.5: cover by -8.5 |  |
| T2 | Under 169.5 | NOT_ESTIMATED (QUALITATIVE) | **WIN** | total 162 vs 169.5: -7.5 |  |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Saga +9.5 (NOT_ESTIMATED) LOSS; TOP_TOTAL Under 169.5 (NOT_ESTIMATED) WIN; RANK1 Saga +9.5 (NOT_ESTIMATED) LOSS. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Kawasaki 90-72 Saga; Quarter scores shown only as an image on permitted pages: NOT_VERIFIED; no OT indicated. Identity matched on teams/players, date and competition (B.LEAGUE PREMIER 2026-27, ScheduleKey 506581).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Basketball rows include overtime (BK-OT-1); none occurred.
**R4. Rank diagnostics.** 1W/1L/0U over 2 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Kawasaki minus Saga = +18; total 162. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Kawasaki ended a five-game losing run with an 18-point home win; Saga fell to 1-14 (ninth straight loss). Half-time and third-quarter splits came only from blocked pages (saga-s.co.jp, basketballking.jp) and are not used. Margin 18 beat Saga +9.5 by 8.5; total 162 under 169.5.
**R9. Source/timing review.** Settlement sources: https://www.bleague.jp/game_detail/?ScheduleKey=506581&tab=1 (ALLOWED); https://kawasaki-bravethunders.com/topics_detail43/id=25910 (ALLOWED). Card timing `POST_SCHEDULED_START_WRITE`; self-declared phase labels: RESEARCH_POST_SCHEDULED;TIMING_UNVERIFIED. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT LOCAL-20261112EE4AFA68-G0006 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-20261112CHAT9538BF5E-G0006 revision-1 -->
### Settlement · `LOCAL-20261112CHAT9538BF5E-G0006` · Kawasaki Brave Thunders v Saga Ballooners · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `b2aa640b39c08fad28fe4a607b47f73f35a618793a40ea60f2a90842a3962b8a`, 22414 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/chat_minis/20261112CHAT9538BF5E.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `PRE_SCHEDULED_START_WRITE` (recorded `2026-11-13T21:04:12+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| LEAN_SIDE | Saga +9.5 | NOT_ESTIMATED (QUALITATIVE_UNRANKED) | **LOSS** | team margin -18 with handicap +9.5: cover by -8.5 |  |
| LEAN_TOTAL | Under 169.5 | NOT_ESTIMATED (QUALITATIVE_UNRANKED) | **WIN** | total 162 vs 169.5: -7.5 |  |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Saga +9.5 (NOT_ESTIMATED) LOSS; TOP_TOTAL Under 169.5 (NOT_ESTIMATED) WIN; RANK1 Saga +9.5 (NOT_ESTIMATED) LOSS. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Kawasaki 90-72 Saga; Quarter scores shown only as an image on permitted pages: NOT_VERIFIED; no OT indicated. Identity matched on teams/players, date and competition (B.LEAGUE PREMIER 2026-27, ScheduleKey 506581).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Basketball rows include overtime (BK-OT-1); none occurred.
**R4. Rank diagnostics.** 1W/1L/0U over 2 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Kawasaki minus Saga = +18; total 162. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Kawasaki ended a five-game losing run with an 18-point home win; Saga fell to 1-14 (ninth straight loss). Half-time and third-quarter splits came only from blocked pages (saga-s.co.jp, basketballking.jp) and are not used. Margin 18 beat Saga +9.5 by 8.5; total 162 under 169.5.
**R9. Source/timing review.** Settlement sources: https://www.bleague.jp/game_detail/?ScheduleKey=506581&tab=1 (ALLOWED); https://kawasaki-bravethunders.com/topics_detail43/id=25910 (ALLOWED). Card timing `PRE_SCHEDULED_START_WRITE`; self-declared phase labels: POST_SCHEDULED_START;TIMING_UNVERIFIED. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT LOCAL-20261112CHAT9538BF5E-G0006 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-202611128358B025-G0006 revision-1 -->
### Settlement · `LOCAL-202611128358B025-G0006` · Kawasaki Brave Thunders v Saga Ballooners · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `49e89e725770c7a7a7c4c46b352f2bacc849f2d6124b6eadc54b7e62da506a69`, 21821 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/chat_minis/202611128358B025.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `POST_SCHEDULED_START_WRITE` (recorded `2026-11-13T21:10:33+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| D1 | Saga +9.5 | 0.621585 (CONDITIONAL_MC) | **LOSS** | team margin -18 with handicap +9.5: cover by -8.5 | 0.386368 |
| D2 | Under 169.5 | 0.527995 (CONDITIONAL_MC) | **WIN** | total 162 vs 169.5: -7.5 | 0.222789 |
| D3 | Over 169.5 | 0.472005 (CONDITIONAL_MC) | **LOSS** | total 162 vs 169.5: -7.5 | 0.222789 |
| D4 | Kawasaki -9.5 | 0.378415 (CONDITIONAL_MC) | **WIN** | team margin +18 with handicap -9.5: cover by +8.5 | 0.386368 |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Saga +9.5 (0.621585) LOSS; TOP_TOTAL Under 169.5 (0.527995) WIN; RANK1 Saga +9.5 (0.621585) LOSS. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Kawasaki 90-72 Saga; Quarter scores shown only as an image on permitted pages: NOT_VERIFIED; no OT indicated. Identity matched on teams/players, date and competition (B.LEAGUE PREMIER 2026-27, ScheduleKey 506581).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Basketball rows include overtime (BK-OT-1); none occurred.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Kawasaki minus Saga = +18; total 162. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Kawasaki ended a five-game losing run with an 18-point home win; Saga fell to 1-14 (ninth straight loss). Half-time and third-quarter splits came only from blocked pages (saga-s.co.jp, basketballking.jp) and are not used. Margin 18 beat Saga +9.5 by 8.5; total 162 under 169.5.
**R9. Source/timing review.** Settlement sources: https://www.bleague.jp/game_detail/?ScheduleKey=506581&tab=1 (ALLOWED); https://kawasaki-bravethunders.com/topics_detail43/id=25910 (ALLOWED). Card timing `POST_SCHEDULED_START_WRITE`; self-declared phase labels: POST_SCHEDULED_START_ISSUE. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT LOCAL-202611128358B025-G0006 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-20261112CHAT17C8C881-G0006 revision-1 -->
### Settlement · `LOCAL-20261112CHAT17C8C881-G0006` · Kawasaki Brave Thunders v Saga Ballooners · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `77ccdce0b42d1d554667c5ad2128c020beca7faf96ad901606b745ab2c758d2f`, 18709 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/chat_minis/20261112CHAT17C8C881.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `WRITE_TIME_NOT_RECORDED` (recorded `NOT_RECORDED`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| R1 | Saga +9.5 | 0.5771 (HYPOTHETICAL_GRID) | **LOSS** | team margin -18 with handicap +9.5: cover by -8.5 | 0.333044 |
| R2 | Under 169.5 | 0.5115 (HYPOTHETICAL_GRID) | **WIN** | total 162 vs 169.5: -7.5 | 0.238632 |
| INFO | Over 169.5 | 0.4885 (HYPOTHETICAL_GRID) | **LOSS** | total 162 vs 169.5: -7.5 | 0.238632 |
| INFO | Kawasaki -9.5 | 0.4229 (HYPOTHETICAL_GRID) | **WIN** | team margin +18 with handicap -9.5: cover by +8.5 | 0.333044 |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Saga +9.5 (0.5771) LOSS; TOP_TOTAL Under 169.5 (0.5115) WIN; RANK1 Saga +9.5 (0.5771) LOSS. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Kawasaki 90-72 Saga; Quarter scores shown only as an image on permitted pages: NOT_VERIFIED; no OT indicated. Identity matched on teams/players, date and competition (B.LEAGUE PREMIER 2026-27, ScheduleKey 506581).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Basketball rows include overtime (BK-OT-1); none occurred.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Kawasaki minus Saga = +18; total 162. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Kawasaki ended a five-game losing run with an 18-point home win; Saga fell to 1-14 (ninth straight loss). Half-time and third-quarter splits came only from blocked pages (saga-s.co.jp, basketballking.jp) and are not used. Margin 18 beat Saga +9.5 by 8.5; total 162 under 169.5.
**R9. Source/timing review.** Settlement sources: https://www.bleague.jp/game_detail/?ScheduleKey=506581&tab=1 (ALLOWED); https://kawasaki-bravethunders.com/topics_detail43/id=25910 (ALLOWED). Card timing `WRITE_TIME_NOT_RECORDED`; self-declared phase labels: POST_SCHEDULED_START_WRITE. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT LOCAL-20261112CHAT17C8C881-G0006 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-20261112CC53B5C806-G0006 revision-1 -->
### Settlement · `LOCAL-20261112CC53B5C806-G0006` · Kawasaki Brave Thunders v Saga Ballooners · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `77df675bced409c9820529a84715ac96183b6e2831e1d742bc355b488b02a209`, 24351 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/chat_minis/20261112CC53B5C806.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `WRITE_TIME_NOT_RECORDED` (recorded `NOT_RECORDED`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| 1 | Saga +9.5 | 0.618484 (SHADOW_MC) | **LOSS** | team margin -18 with handicap +9.5: cover by -8.5 | 0.382522 |
| 2 | Under 169.5 | 0.575317 (SHADOW_MC) | **WIN** | total 162 vs 169.5: -7.5 | 0.180356 |
| INFO | Over 169.5 | 0.424683 (SHADOW_MC) | **LOSS** | total 162 vs 169.5: -7.5 | 0.180356 |
| INFO | Kawasaki -9.5 | 0.381516 (SHADOW_MC) | **WIN** | team margin +18 with handicap -9.5: cover by +8.5 | 0.382522 |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Saga +9.5 (0.618484) LOSS; TOP_TOTAL Under 169.5 (0.575317) WIN; RANK1 Saga +9.5 (0.618484) LOSS. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Kawasaki 90-72 Saga; Quarter scores shown only as an image on permitted pages: NOT_VERIFIED; no OT indicated. Identity matched on teams/players, date and competition (B.LEAGUE PREMIER 2026-27, ScheduleKey 506581).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Basketball rows include overtime (BK-OT-1); none occurred.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Kawasaki minus Saga = +18; total 162. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Kawasaki ended a five-game losing run with an 18-point home win; Saga fell to 1-14 (ninth straight loss). Half-time and third-quarter splits came only from blocked pages (saga-s.co.jp, basketballking.jp) and are not used. Margin 18 beat Saga +9.5 by 8.5; total 162 under 169.5.
**R9. Source/timing review.** Settlement sources: https://www.bleague.jp/game_detail/?ScheduleKey=506581&tab=1 (ALLOWED); https://kawasaki-bravethunders.com/topics_detail43/id=25910 (ALLOWED). Card timing `WRITE_TIME_NOT_RECORDED`; self-declared phase labels: POST_SCHEDULED_START;POST_SCHEDULED_START_NOT_CERTIFIED_PREGAME;RESEARCH_POST_SCHEDULED_START. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT LOCAL-20261112CC53B5C806-G0006 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-20261112D3C239297F-G0006 revision-1 -->
### Settlement · `LOCAL-20261112D3C239297F-G0006` · Kawasaki Brave Thunders v Saga Ballooners · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `8a6fcaeca18f68a7159ee3e2553e25982e6155da3b9298f23cf0607ee7094716`, 28241 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/chat_minis/20261112D3C239297F.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `POST_SCHEDULED_START_WRITE` (recorded `2026-11-13T21:21:35+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| D1 | Saga +9.5 | 0.600872 (SCENARIO_MIXTURE) | **LOSS** | team margin -18 with handicap +9.5: cover by -8.5 | 0.361047 |
| D2 | Over 169.5 | 0.503487 (SCENARIO_MIXTURE) | **LOSS** | total 162 vs 169.5: -7.5 | 0.253499 |
| D3 | Under 169.5 | 0.496513 (SCENARIO_MIXTURE) | **WIN** | total 162 vs 169.5: -7.5 | 0.253499 |
| D4 | Kawasaki -9.5 | 0.399128 (SCENARIO_MIXTURE) | **WIN** | team margin +18 with handicap -9.5: cover by +8.5 | 0.361047 |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Saga +9.5 (0.600872) LOSS; TOP_TOTAL Over 169.5 (0.503487) LOSS; RANK1 Saga +9.5 (0.600872) LOSS. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Kawasaki 90-72 Saga; Quarter scores shown only as an image on permitted pages: NOT_VERIFIED; no OT indicated. Identity matched on teams/players, date and competition (B.LEAGUE PREMIER 2026-27, ScheduleKey 506581).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Basketball rows include overtime (BK-OT-1); none occurred.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Kawasaki minus Saga = +18; total 162. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Kawasaki ended a five-game losing run with an 18-point home win; Saga fell to 1-14 (ninth straight loss). Half-time and third-quarter splits came only from blocked pages (saga-s.co.jp, basketballking.jp) and are not used. Margin 18 beat Saga +9.5 by 8.5; total 162 under 169.5.
**R9. Source/timing review.** Settlement sources: https://www.bleague.jp/game_detail/?ScheduleKey=506581&tab=1 (ALLOWED); https://kawasaki-bravethunders.com/topics_detail43/id=25910 (ALLOWED). Card timing `POST_SCHEDULED_START_WRITE`; self-declared phase labels: TIMING_UNVERIFIED. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT LOCAL-20261112D3C239297F-G0006 revision-1 -->

### Deep loss reviews (DEEPLOSS-v1)

#### Deep loss review · Kawasaki Brave Thunders v Saga Ballooners · Saga +9.5

**1. Exact frozen claim.** `Saga +9.5`, full-game endpoint as each record defined it. Triggered in 6 record(s):

| Record | Trigger role(s) | Original p (basis) | Brier | Log loss |
|---|---|---|---:|---:|
| `LOCAL-202611128358B025-G0006` | TOP_SIDE, RANK1 | 0.621585 (CONDITIONAL_MC) | 0.386368 | 0.971764 |
| `LOCAL-20261112CC53B5C806-G0006` | TOP_SIDE, RANK1 | 0.618484 (SHADOW_MC) | 0.382522 | 0.963602 |
| `LOCAL-20261112CHAT17C8C881-G0006` | TOP_SIDE, RANK1 | 0.5771 (HYPOTHETICAL_GRID) | 0.333044 | 0.860620 |
| `LOCAL-20261112CHAT9538BF5E-G0006` | TOP_SIDE, RANK1 | NOT_ESTIMATED (QUALITATIVE_UNRANKED) |  |  |
| `LOCAL-20261112D3C239297F-G0006` | TOP_SIDE, RANK1 | 0.600872 (SCENARIO_MIXTURE) | 0.361047 | 0.918473 |
| `LOCAL-20261112EE4AFA68-G0006` | TOP_SIDE, RANK1 | NOT_ESTIMATED (QUALITATIVE) |  |  |

No record carried a primary p_card, frozen reference or same-row baseline; BASELINE_P comparison NOT_COMPUTABLE.

**2. Verified outcome.** Kawasaki 90-72 Saga (Quarter scores shown only as an image on permitted pages: NOT_VERIFIED; no OT indicated). team margin -18 with handicap +9.5: cover by -8.5. Sources in R9; evidence B; final wall-clock NOT_VERIFIED.
**3. Distribution check.** Numeric records priced this row at 0.577-0.622 (mean 0.605); a loss at those prices is a 38%-42% event under each record's own uncalibrated object. Percentile placement inside each record's printed score object is not reconstructed; the printed objects stay in the cores.
**4. Error decomposition.** Realised line distance: team margin -18 with handicap +9.5: cover by -8.5. No record had a calibrated centre or a measured effect-table row, so the miss cannot be split into reference error and adjustment error; no blame shares are invented.
**5. Research audit.** Saga 1-13 and 95.2 opponent PPG: TRUE per cards' sources. Kawasaki 0-5 L5 and 1-9 home: TRUE per cited schedules. Facts not re-opened here remain UNVERIFIED_AT_CUTOFF; no source in any card carries a captured retrieval receipt (chat-local research).
**6. What decided the game.** Kawasaki ended a five-game losing run with an 18-point home win; Saga fell to 1-14 (ninth straight loss). Half-time and third-quarter splits came only from blocked pages (saga-s.co.jp, basketballking.jp) and are not used. Margin 18 beat Saga +9.5 by 8.5; total 162 under 169.5.
**7. Knowable at cutoff?** Saga's defensive collapse rate was printed in every card as the main failure route. The final score and its timing were not knowable.
**8. Process audit.** Chat-local record; no repository reference stage, no source-audit receipts, no lineup confirmation, no freeze. Timing per record in CARD_TIMING.csv (several written after the scheduled start). Endpoint and contract definitions were correct.
**9. Verdict.** Losing all six times on one line is a shared-input failure: every chat discounted Kawasaki's home win probability because of its losing run and underweighted Saga's 9-game slide. Margin 18 vs line 9.5 is not a near miss.
**10. Cutoff-only counterfactual.** NOT_ESTIMATED: no knowable fact has a measured effect-table row, so no corrected probability is priced after the result.
**11. Failure class and recurrence.** Shared across 6 record(s) on one game: the parallel chats used overlapping public inputs, so their losses are one dependent observation, not 6 independent ones.
**12. Correction.** NO_CHANGE to any rule from one result. Procedure proposals are in AUDIT_REPORT §6 (PROPOSED_NOT_TESTED).
**13. Matched wins.** `LOCAL-202611128358B025-G0006` TOP_TOTAL Under 169.5 WIN; `LOCAL-20261112CC53B5C806-G0006` TOP_TOTAL Under 169.5 WIN; `LOCAL-20261112CHAT17C8C881-G0006` TOP_TOTAL Under 169.5 WIN; `LOCAL-20261112CHAT9538BF5E-G0006` TOP_TOTAL Under 169.5 WIN; `LOCAL-20261112EE4AFA68-G0006` TOP_TOTAL Under 169.5 WIN. These rest on the same unvalidated construction and do not show the process worked.
**14. Honesty.** Original numbers and labels preserved; no luck claim without the arithmetic above; no invented percentages, operator terms or publication times. Preservation PASS; information closure INCOMPLETE.

#### Deep loss review · Kawasaki Brave Thunders v Saga Ballooners · Over 169.5

**1. Exact frozen claim.** `Over 169.5`, full-game endpoint as each record defined it. Triggered in 1 record(s):

| Record | Trigger role(s) | Original p (basis) | Brier | Log loss |
|---|---|---|---:|---:|
| `LOCAL-20261112D3C239297F-G0006` | TOP_TOTAL | 0.503487 (SCENARIO_MIXTURE) | 0.253499 | 0.700146 |

No record carried a primary p_card, frozen reference or same-row baseline; BASELINE_P comparison NOT_COMPUTABLE.

**2. Verified outcome.** Kawasaki 90-72 Saga (Quarter scores shown only as an image on permitted pages: NOT_VERIFIED; no OT indicated). total 162 vs 169.5: -7.5. Sources in R9; evidence B; final wall-clock NOT_VERIFIED.
**3. Distribution check.** Numeric records priced this row at 0.503-0.503 (mean 0.503); a loss at those prices is a 50%-50% event under each record's own uncalibrated object. Percentile placement inside each record's printed score object is not reconstructed; the printed objects stay in the cores.
**4. Error decomposition.** Realised line distance: total 162 vs 169.5: -7.5. No record had a calibrated centre or a measured effect-table row, so the miss cannot be split into reference error and adjustment error; no blame shares are invented.
**5. Research audit.** Same inputs as the side. Facts not re-opened here remain UNVERIFIED_AT_CUTOFF; no source in any card carries a captured retrieval receipt (chat-local research).
**6. What decided the game.** Kawasaki ended a five-game losing run with an 18-point home win; Saga fell to 1-14 (ninth straight loss). Half-time and third-quarter splits came only from blocked pages (saga-s.co.jp, basketballking.jp) and are not used. Margin 18 beat Saga +9.5 by 8.5; total 162 under 169.5.
**7. Knowable at cutoff?** Kawasaki's slow, low-scoring recent games (L5 all below 169.5) were printed. The final score and its timing were not knowable.
**8. Process audit.** Chat-local record; no repository reference stage, no source-audit receipts, no lineup confirmation, no freeze. Timing per record in CARD_TIMING.csv (several written after the scheduled start). Endpoint and contract definitions were correct.
**9. Verdict.** D3C's 50.35% 'second' row was a coin flip ranked by a 0.7-point edge; it should not have been ranked as a direction at all.
**10. Cutoff-only counterfactual.** NOT_ESTIMATED: no knowable fact has a measured effect-table row, so no corrected probability is priced after the result.
**11. Failure class and recurrence.** Shared across 1 record(s) on one game: the parallel chats used overlapping public inputs, so their losses are one dependent observation, not 1 independent ones.
**12. Correction.** NO_CHANGE to any rule from one result. Procedure proposals are in AUDIT_REPORT §6 (PROPOSED_NOT_TESTED).
**13. Matched wins.** None among the triggering records.
**14. Honesty.** Original numbers and labels preserved; no luck claim without the arithmetic above; no invented percentages, operator terms or publication times. Preservation PASS; information closure INCOMPLETE.

#### Joint section · top side and top total both lost · Kawasaki Brave Thunders v Saga Ballooners

Records: `LOCAL-20261112D3C239297F-G0006`: Saga +9.5 and Over 169.5. Both legs failed on the same game state (Kawasaki 90-72 Saga). The cards' own joint-failure figures, where printed, are retained in the cores; none was calibrated, and treating the two leans as independent picks would double-count one wrong read of the game.

<!-- END SETTLEMENT EVENT E16 revision-1 -->

<!-- BEGIN SETTLEMENT EVENT E17 revision-1 -->
## Event · BANES Motor České Budějovice U20 v Bílí Tygři Liberec U20 · 2026-11-13 · Czech KB Extraliga juniorů (U20) 2026-27, round 20, federation match 3156

**Final:** Motor 6-1 Liberec (regulation). **Periods:** 0:0, 1:0, 5:1; official start 13.11.2026 12:00 CET. **Evidence B.** Scheduled 2026-11-13T11:00:00+00:00. Note: SRC-ALT breach disclosed: a delegated fetch opened hcmotor.cz (BLOCKED_FOR_AI for Claude-User) before the audit was run; that evidence (goal scorers/minutes) is excluded and is not cited.

| Opened source | Audit | Field read |
|---|---|---|
| https://czehockey.cz/game/detail/178203 | ALLOWED | '13. 11. 2026, 12:00'; period line '0:0, 1:0, 5:1' |
| https://www.hcbilitygri.cz/matches/JUN | NO_RULES_FILE | 'pátek 13.11.2026 12:00', 6-1 |

<!-- BEGIN SETTLEMENT LOCAL-20261112EE4AFA68-G0007 revision-1 -->
### Settlement · `LOCAL-20261112EE4AFA68-G0007` · BANES Motor České Budějovice U20 v Bílí Tygři Liberec U20 · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `26fb28f6681ca139fdd6ccc56a607bb34856a35680db1fde1bbed05c57ec9f0e`, 24371 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/chat_minis/20261112EE4AFA68.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `POST_SCHEDULED_START_WRITE` (recorded `2026-11-13T22:09:04+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| PREF | Over 5.5 goals | NOT_ESTIMATED (QUALITATIVE) | **WIN** | total 7 vs 5.5: +1.5 |  |
| SECOND | Liberec U20 +1.5 goals | NOT_ESTIMATED (QUALITATIVE) | **LOSS** | team margin -5 with handicap +1.5: cover by -3.5 |  |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Liberec U20 +1.5 goals (NOT_ESTIMATED) LOSS; TOP_TOTAL Over 5.5 goals (NOT_ESTIMATED) WIN; RANK1 Over 5.5 goals (NOT_ESTIMATED) WIN. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Motor 6-1 Liberec (regulation); 0:0, 1:0, 5:1; official start 13.11.2026 12:00 CET. Identity matched on teams/players, date and competition (Czech KB Extraliga juniorů (U20) 2026-27, round 20, federation match 3156).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Hockey rows: the result is identical under 60-minute, full-game and shootout-credited conventions, so no endpoint ambiguity changes a grade.
**R4. Rank diagnostics.** 1W/1L/0U over 2 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Motor minus Liberec = +5; total 7. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Goalless first period, 1-0 after two, then Motor scored five times in the third (Liberec one). At 2-1 midway through the third Liberec +1.5 was still alive; four Motor goals in about ten minutes ended it.
**R9. Source/timing review.** Settlement sources: https://czehockey.cz/game/detail/178203 (ALLOWED); https://www.hcbilitygri.cz/matches/JUN (NO_RULES_FILE). Card timing `POST_SCHEDULED_START_WRITE`; self-declared phase labels: TIMING_UNVERIFIED. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT LOCAL-20261112EE4AFA68-G0007 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-20261112CHAT9538BF5E-G0007 revision-1 -->
### Settlement · `LOCAL-20261112CHAT9538BF5E-G0007` · BANES Motor České Budějovice U20 v Bílí Tygři Liberec U20 · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `a7a8e55daff2e289a994dc9ff246ff83451f7f3e5b76a679c4a83330625f66b8`, 15612 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/chat_minis/20261112CHAT9538BF5E.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `POST_SCHEDULED_START_WRITE` (recorded `2026-11-13T22:02:03+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| LEAN_TOTAL | Over 5.5 goals | NOT_ESTIMATED (QUALITATIVE_UNRANKED) | **WIN** | total 7 vs 5.5: +1.5 |  |
| LEAN_SIDE | Motor U20 -1.5 goals | NOT_ESTIMATED (QUALITATIVE_UNRANKED) | **WIN** | team margin +5 with handicap -1.5: cover by +3.5 |  |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Motor U20 -1.5 goals (NOT_ESTIMATED) WIN; TOP_TOTAL Over 5.5 goals (NOT_ESTIMATED) WIN; RANK1 Over 5.5 goals (NOT_ESTIMATED) WIN. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Motor 6-1 Liberec (regulation); 0:0, 1:0, 5:1; official start 13.11.2026 12:00 CET. Identity matched on teams/players, date and competition (Czech KB Extraliga juniorů (U20) 2026-27, round 20, federation match 3156).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Hockey rows: the result is identical under 60-minute, full-game and shootout-credited conventions, so no endpoint ambiguity changes a grade.
**R4. Rank diagnostics.** 2W/0L/0U over 2 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Motor minus Liberec = +5; total 7. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Goalless first period, 1-0 after two, then Motor scored five times in the third (Liberec one). At 2-1 midway through the third Liberec +1.5 was still alive; four Motor goals in about ten minutes ended it.
**R9. Source/timing review.** Settlement sources: https://czehockey.cz/game/detail/178203 (ALLOWED); https://www.hcbilitygri.cz/matches/JUN (NO_RULES_FILE). Card timing `POST_SCHEDULED_START_WRITE`; self-declared phase labels: POST_SCHEDULED_START_WRITE. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT LOCAL-20261112CHAT9538BF5E-G0007 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-202611128358B025-G0007 revision-1 -->
### Settlement · `LOCAL-202611128358B025-G0007` · BANES Motor České Budějovice U20 v Bílí Tygři Liberec U20 · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `b99806db080a38169c40d7e3f66edd12762ee5df27493685a7dbeca44dffaa99`, 14559 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/chat_minis/202611128358B025.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `POST_SCHEDULED_START_WRITE` (recorded `2026-11-13T22:03:45+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| D1 | Liberec U20 +1.5 goals | 0.614297 (POISSON_GRID) | **LOSS** | team margin -5 with handicap +1.5: cover by -3.5 | 0.377361 |
| D2 | Over 5.5 goals | 0.554320 (POISSON_GRID) | **WIN** | total 7 vs 5.5: +1.5 | 0.198631 |
| D3 | Under 5.5 goals | 0.445680 (POISSON_GRID) | **LOSS** | total 7 vs 5.5: +1.5 | 0.198631 |
| D4 | Motor U20 -1.5 goals | 0.385703 (POISSON_GRID) | **WIN** | team margin +5 with handicap -1.5: cover by +3.5 | 0.377361 |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Liberec U20 +1.5 goals (0.614297) LOSS; TOP_TOTAL Over 5.5 goals (0.554320) WIN; RANK1 Liberec U20 +1.5 goals (0.614297) LOSS. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Motor 6-1 Liberec (regulation); 0:0, 1:0, 5:1; official start 13.11.2026 12:00 CET. Identity matched on teams/players, date and competition (Czech KB Extraliga juniorů (U20) 2026-27, round 20, federation match 3156).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Hockey rows: the result is identical under 60-minute, full-game and shootout-credited conventions, so no endpoint ambiguity changes a grade.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Motor minus Liberec = +5; total 7. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Goalless first period, 1-0 after two, then Motor scored five times in the third (Liberec one). At 2-1 midway through the third Liberec +1.5 was still alive; four Motor goals in about ten minutes ended it.
**R9. Source/timing review.** Settlement sources: https://czehockey.cz/game/detail/178203 (ALLOWED); https://www.hcbilitygri.cz/matches/JUN (NO_RULES_FILE). Card timing `POST_SCHEDULED_START_WRITE`; self-declared phase labels: POST_SCHEDULED_START;POST_SCHEDULED_START_ISSUE. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT LOCAL-202611128358B025-G0007 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-20261112CHAT17C8C881-G0007 revision-1 -->
### Settlement · `LOCAL-20261112CHAT17C8C881-G0007` · BANES Motor České Budějovice U20 v Bílí Tygři Liberec U20 · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `e7bc16887b5848738505be54060f7eea2f7db6f47352e0a2b2cfe541cd94428b`, 18237 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/chat_minis/20261112CHAT17C8C881.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `WRITE_TIME_NOT_RECORDED` (recorded `NOT_RECORDED`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| D1 | Over 5.5 goals | 0.565 (ILLUSTRATIVE_GRID) | **WIN** | total 7 vs 5.5: +1.5 | 0.189225 |
| D2 | Liberec U20 +1.5 goals | 0.519 (ILLUSTRATIVE_GRID) | **LOSS** | team margin -5 with handicap +1.5: cover by -3.5 | 0.269361 |
| D3 | Motor U20 -1.5 goals | 0.481 (ILLUSTRATIVE_GRID) | **WIN** | team margin +5 with handicap -1.5: cover by +3.5 | 0.269361 |
| D4 | Under 5.5 goals | 0.435 (ILLUSTRATIVE_GRID) | **LOSS** | total 7 vs 5.5: +1.5 | 0.189225 |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Liberec U20 +1.5 goals (0.519) LOSS; TOP_TOTAL Over 5.5 goals (0.565) WIN; RANK1 Over 5.5 goals (0.565) WIN. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Motor 6-1 Liberec (regulation); 0:0, 1:0, 5:1; official start 13.11.2026 12:00 CET. Identity matched on teams/players, date and competition (Czech KB Extraliga juniorů (U20) 2026-27, round 20, federation match 3156).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Hockey rows: the result is identical under 60-minute, full-game and shootout-credited conventions, so no endpoint ambiguity changes a grade.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Motor minus Liberec = +5; total 7. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Goalless first period, 1-0 after two, then Motor scored five times in the third (Liberec one). At 2-1 midway through the third Liberec +1.5 was still alive; four Motor goals in about ten minutes ended it.
**R9. Source/timing review.** Settlement sources: https://czehockey.cz/game/detail/178203 (ALLOWED); https://www.hcbilitygri.cz/matches/JUN (NO_RULES_FILE). Card timing `WRITE_TIME_NOT_RECORDED`; self-declared phase labels: POST_OFFICIAL_SCHEDULED_START_WRITE;POST_SCHEDULED_START_RESEARCH_DRAFT. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT LOCAL-20261112CHAT17C8C881-G0007 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-20261112CC53B5C806-G0007 revision-1 -->
### Settlement · `LOCAL-20261112CC53B5C806-G0007` · BANES Motor České Budějovice U20 v Bílí Tygři Liberec U20 · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `a616fbe5626a152580976615432318534f525956777e70c1e277821f747dd881`, 30293 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/chat_minis/20261112CC53B5C806.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `WRITE_TIME_NOT_RECORDED` (recorded `NOT_RECORDED`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| 1 | Over 5.5 goals | 0.6044 (SHADOW_MC) | **WIN** | total 7 vs 5.5: +1.5 | 0.156499 |
| 2 | Liberec U20 +1.5 goals | 0.5255 (SHADOW_MC) | **LOSS** | team margin -5 with handicap +1.5: cover by -3.5 | 0.276150 |
| INFO | Motor U20 -1.5 goals | 0.4745 (SHADOW_MC) | **WIN** | team margin +5 with handicap -1.5: cover by +3.5 | 0.276150 |
| INFO | Under 5.5 goals | 0.3956 (SHADOW_MC) | **LOSS** | total 7 vs 5.5: +1.5 | 0.156499 |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Liberec U20 +1.5 goals (0.5255) LOSS; TOP_TOTAL Over 5.5 goals (0.6044) WIN; RANK1 Over 5.5 goals (0.6044) WIN. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Motor 6-1 Liberec (regulation); 0:0, 1:0, 5:1; official start 13.11.2026 12:00 CET. Identity matched on teams/players, date and competition (Czech KB Extraliga juniorů (U20) 2026-27, round 20, federation match 3156).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Hockey rows: the result is identical under 60-minute, full-game and shootout-credited conventions, so no endpoint ambiguity changes a grade.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Motor minus Liberec = +5; total 7. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Goalless first period, 1-0 after two, then Motor scored five times in the third (Liberec one). At 2-1 midway through the third Liberec +1.5 was still alive; four Motor goals in about ten minutes ended it.
**R9. Source/timing review.** Settlement sources: https://czehockey.cz/game/detail/178203 (ALLOWED); https://www.hcbilitygri.cz/matches/JUN (NO_RULES_FILE). Card timing `WRITE_TIME_NOT_RECORDED`; self-declared phase labels: POST_OFFICIAL_SCHEDULE_CLOCK;POST_OFFICIAL_SCHEDULE_TIME;POST_SCHEDULED_START;TIMING_UNVERIFIED. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT LOCAL-20261112CC53B5C806-G0007 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-20261112D3C239297F-G0007 revision-1 -->
### Settlement · `LOCAL-20261112D3C239297F-G0007` · BANES Motor České Budějovice U20 v Bílí Tygři Liberec U20 · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `bdceca1f5e4a8447c277d401f75919d8b9ba68e8c4ac4e986e288caca4a94688`, 21971 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/chat_minis/20261112D3C239297F.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `HEURISTIC_ARTIFACT_SEE_LABELS` (recorded `2026-11-14T01:30:00+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| D1 | Over 5.5 goals | 0.56581 (SCENARIO_GRID) | **WIN** | total 7 vs 5.5: +1.5 | 0.188521 |
| D2 | Liberec U20 +1.5 goals | 0.54351 (SCENARIO_GRID) | **LOSS** | team margin -5 with handicap +1.5: cover by -3.5 | 0.295403 |
| D3 | Motor U20 -1.5 goals | 0.45649 (SCENARIO_GRID) | **WIN** | team margin +5 with handicap -1.5: cover by +3.5 | 0.295403 |
| D4 | Under 5.5 goals | 0.43419 (SCENARIO_GRID) | **LOSS** | total 7 vs 5.5: +1.5 | 0.188521 |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Liberec U20 +1.5 goals (0.54351) LOSS; TOP_TOTAL Over 5.5 goals (0.56581) WIN; RANK1 Over 5.5 goals (0.56581) WIN. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Motor 6-1 Liberec (regulation); 0:0, 1:0, 5:1; official start 13.11.2026 12:00 CET. Identity matched on teams/players, date and competition (Czech KB Extraliga juniorů (U20) 2026-27, round 20, federation match 3156).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Hockey rows: the result is identical under 60-minute, full-game and shootout-credited conventions, so no endpoint ambiguity changes a grade.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Motor minus Liberec = +5; total 7. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Goalless first period, 1-0 after two, then Motor scored five times in the third (Liberec one). At 2-1 midway through the third Liberec +1.5 was still alive; four Motor goals in about ten minutes ended it.
**R9. Source/timing review.** Settlement sources: https://czehockey.cz/game/detail/178203 (ALLOWED); https://www.hcbilitygri.cz/matches/JUN (NO_RULES_FILE). Card timing `HEURISTIC_ARTIFACT_SEE_LABELS`; self-declared phase labels: TIMING_UNVERIFIED. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT LOCAL-20261112D3C239297F-G0007 revision-1 -->

### Deep loss reviews (DEEPLOSS-v1)

#### Deep loss review · BANES Motor České Budějovice U20 v Bílí Tygři Liberec U20 · Liberec U20 +1.5 goals

**1. Exact frozen claim.** `Liberec U20 +1.5 goals`, full-game endpoint as each record defined it. Triggered in 5 record(s):

| Record | Trigger role(s) | Original p (basis) | Brier | Log loss |
|---|---|---|---:|---:|
| `LOCAL-202611128358B025-G0007` | TOP_SIDE, RANK1 | 0.614297 (POISSON_GRID) | 0.377361 | 0.952688 |
| `LOCAL-20261112CC53B5C806-G0007` | TOP_SIDE | 0.5255 (SHADOW_MC) | 0.276150 | 0.745494 |
| `LOCAL-20261112CHAT17C8C881-G0007` | TOP_SIDE | 0.519 (ILLUSTRATIVE_GRID) | 0.269361 | 0.731888 |
| `LOCAL-20261112D3C239297F-G0007` | TOP_SIDE | 0.54351 (SCENARIO_GRID) | 0.295403 | 0.784188 |
| `LOCAL-20261112EE4AFA68-G0007` | TOP_SIDE | NOT_ESTIMATED (QUALITATIVE) |  |  |

No record carried a primary p_card, frozen reference or same-row baseline; BASELINE_P comparison NOT_COMPUTABLE.

**2. Verified outcome.** Motor 6-1 Liberec (regulation) (0:0, 1:0, 5:1; official start 13.11.2026 12:00 CET). team margin -5 with handicap +1.5: cover by -3.5. Sources in R9; evidence B; final wall-clock NOT_VERIFIED.
**3. Distribution check.** Numeric records priced this row at 0.519-0.614 (mean 0.551); a loss at those prices is a 39%-48% event under each record's own uncalibrated object. Percentile placement inside each record's printed score object is not reconstructed; the printed objects stay in the cores.
**4. Error decomposition.** Realised line distance: team margin -5 with handicap +1.5: cover by -3.5. No record had a calibrated centre or a measured effect-table row, so the miss cannot be split into reference error and adjustment error; no blame shares are invented.
**5. Research audit.** Season goals (Liberec conceded 71 in 17) TRUE per federation standings cited. Prior 19 Sep junior H2H 4-3 OT: TRUE per cited match page. Facts not re-opened here remain UNVERIFIED_AT_CUTOFF; no source in any card carries a captured retrieval receipt (chat-local research).
**6. What decided the game.** Goalless first period, 1-0 after two, then Motor scored five times in the third (Liberec one). At 2-1 midway through the third Liberec +1.5 was still alive; four Motor goals in about ten minutes ended it.
**7. Knowable at cutoff?** Motor's superior season differential was printed; the chats' own 'stronger Motor' scenarios showed the side flipping. The final score and its timing were not knowable.
**8. Process audit.** Chat-local record; no repository reference stage, no source-audit receipts, no lineup confirmation, no freeze. Timing per record in CARD_TIMING.csv (several written after the scheduled start). Endpoint and contract definitions were correct.
**9. Verdict.** Handicap lean on a youth league with unconfirmed goalies; the cards correctly refused a certified pick. Five third-period goals is an outlier collapse, but the loss margin (5) is not close.
**10. Cutoff-only counterfactual.** NOT_ESTIMATED: no knowable fact has a measured effect-table row, so no corrected probability is priced after the result.
**11. Failure class and recurrence.** Shared across 5 record(s) on one game: the parallel chats used overlapping public inputs, so their losses are one dependent observation, not 5 independent ones.
**12. Correction.** NO_CHANGE to any rule from one result. Procedure proposals are in AUDIT_REPORT §6 (PROPOSED_NOT_TESTED).
**13. Matched wins.** `LOCAL-202611128358B025-G0007` TOP_TOTAL Over 5.5 goals WIN; `LOCAL-20261112CC53B5C806-G0007` RANK1 Over 5.5 goals WIN; `LOCAL-20261112CC53B5C806-G0007` TOP_TOTAL Over 5.5 goals WIN; `LOCAL-20261112CHAT17C8C881-G0007` RANK1 Over 5.5 goals WIN; `LOCAL-20261112CHAT17C8C881-G0007` TOP_TOTAL Over 5.5 goals WIN; `LOCAL-20261112D3C239297F-G0007` RANK1 Over 5.5 goals WIN; `LOCAL-20261112D3C239297F-G0007` TOP_TOTAL Over 5.5 goals WIN; `LOCAL-20261112EE4AFA68-G0007` RANK1 Over 5.5 goals WIN; `LOCAL-20261112EE4AFA68-G0007` TOP_TOTAL Over 5.5 goals WIN. These rest on the same unvalidated construction and do not show the process worked.
**14. Honesty.** Original numbers and labels preserved; no luck claim without the arithmetic above; no invented percentages, operator terms or publication times. Preservation PASS; information closure INCOMPLETE.

<!-- END SETTLEMENT EVENT E17 revision-1 -->

<!-- BEGIN SETTLEMENT EVENT E18 revision-1 -->
## Event · Zsombor Piros v Daniel Altmaier · 2026-11-13 · ATP Challenger 125 Orléans, QF

**Final:** Altmaier d. Piros 7-5 6-4. **Periods:** Games Altmaier 13, Piros 9; total 22; ATP 01:34:40. **Evidence C.** Scheduled 2026-11-13T12:00:00+00:00. Note: Single opened lineage (ATP); TennisExplorer Orléans URLs returned 'Tournament does not exist'; tennis.com BLOCKED_FOR_AI.

| Opened source | Audit | Field read |
|---|---|---|
| https://www.atptour.com/en/scores/current-challenger/orleans/2273/results | ALLOWED | 'Daniel Altmaier wins the match 7-5 6-4'; 01:34:40 |
| https://www.atptour.com/en/scores/current-challenger/orleans/2273/daily-schedule | ALLOWED | Only Day 7 rendered; no 13 Nov order of play |

<!-- BEGIN SETTLEMENT LOCAL-20261112EE4AFA68-G0008 revision-1 -->
### Settlement · `LOCAL-20261112EE4AFA68-G0008` · Zsombor Piros v Daniel Altmaier · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `2138135ed90160c4ff38e8854b86d063c0251ab0aa1d7c2b0e4a0e8443409f56`, 30514 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/chat_minis/20261112EE4AFA68.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `POST_SCHEDULED_START_WRITE` (recorded `2026-11-13T23:01:03+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| PREF | Piros +2.5 games | NOT_ESTIMATED (QUALITATIVE) | **LOSS** | team margin -4 with handicap +2.5: cover by -1.5 |  |
| SECOND | Over 22.5 games | NOT_ESTIMATED (QUALITATIVE) | **LOSS** | total 22 vs 22.5: -0.5 |  |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Piros +2.5 games (NOT_ESTIMATED) LOSS; TOP_TOTAL Over 22.5 games (NOT_ESTIMATED) LOSS; RANK1 Piros +2.5 games (NOT_ESTIMATED) LOSS. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Altmaier d. Piros 7-5 6-4; Games Altmaier 13, Piros 9; total 22; ATP 01:34:40. Identity matched on teams/players, date and competition (ATP Challenger 125 Orléans, QF).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Tennis rows count every game of the completed match; no retirement.
**R4. Rank diagnostics.** 0W/2L/0U over 2 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Piros games minus Altmaier games = -4; total 22. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Straight sets 7-5 6-4: 22 games, half a game under 22.5, and a four-game Altmaier margin, 1.5 games beyond Piros +2.5. One break in each set decided both rows; there was no tiebreak.
**R9. Source/timing review.** Settlement sources: https://www.atptour.com/en/scores/current-challenger/orleans/2273/results (ALLOWED); https://www.atptour.com/en/scores/current-challenger/orleans/2273/daily-schedule (ALLOWED). Card timing `POST_SCHEDULED_START_WRITE`; self-declared phase labels: TIMING_UNVERIFIED. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT LOCAL-20261112EE4AFA68-G0008 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-20261112CHAT9538BF5E-G0008 revision-1 -->
### Settlement · `LOCAL-20261112CHAT9538BF5E-G0008` · Zsombor Piros v Daniel Altmaier · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `3af0341a1bae4a0ee2d8e96a2a79fa1bb7e15743bfdce735828cf4448d1df8d8`, 20350 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/chat_minis/20261112CHAT9538BF5E.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `PRE_SCHEDULED_START_WRITE` (recorded `2026-11-13T22:58:14+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| LEAN_TOTAL | Over 22.5 games | NOT_ESTIMATED (QUALITATIVE_UNRANKED) | **LOSS** | total 22 vs 22.5: -0.5 |  |
| LEAN_SIDE | Piros +2.5 games | NOT_ESTIMATED (QUALITATIVE_UNRANKED) | **LOSS** | team margin -4 with handicap +2.5: cover by -1.5 |  |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Piros +2.5 games (NOT_ESTIMATED) LOSS; TOP_TOTAL Over 22.5 games (NOT_ESTIMATED) LOSS; RANK1 Over 22.5 games (NOT_ESTIMATED) LOSS. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Altmaier d. Piros 7-5 6-4; Games Altmaier 13, Piros 9; total 22; ATP 01:34:40. Identity matched on teams/players, date and competition (ATP Challenger 125 Orléans, QF).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Tennis rows count every game of the completed match; no retirement.
**R4. Rank diagnostics.** 0W/2L/0U over 2 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Piros games minus Altmaier games = -4; total 22. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Straight sets 7-5 6-4: 22 games, half a game under 22.5, and a four-game Altmaier margin, 1.5 games beyond Piros +2.5. One break in each set decided both rows; there was no tiebreak.
**R9. Source/timing review.** Settlement sources: https://www.atptour.com/en/scores/current-challenger/orleans/2273/results (ALLOWED); https://www.atptour.com/en/scores/current-challenger/orleans/2273/daily-schedule (ALLOWED). Card timing `PRE_SCHEDULED_START_WRITE`; self-declared phase labels: TIMING_UNVERIFIED. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT LOCAL-20261112CHAT9538BF5E-G0008 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-202611128358B025-G0008 revision-1 -->
### Settlement · `LOCAL-202611128358B025-G0008` · Zsombor Piros v Daniel Altmaier · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `4b062e46938b6d0b7ba2209c015516ad010de29b2ac390f8b16af092040c884f`, 18076 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/chat_minis/202611128358B025.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `PRE_SCHEDULED_START_WRITE` (recorded `2026-11-13T22:59:17+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| DIR | Over 22.5 games | 0.610 (SCORE_GRID_CENTRAL) | **LOSS** | total 22 vs 22.5: -0.5 | 0.372100 |
| D1_RAW | Piros +2.5 games | 0.629 (SCORE_GRID_CENTRAL) | **LOSS** | team margin -4 with handicap +2.5: cover by -1.5 | 0.395641 |
| D3 | Under 22.5 games | 0.390 (SCORE_GRID_CENTRAL) | **WIN** | total 22 vs 22.5: -0.5 | 0.372100 |
| D4 | Altmaier -2.5 games | 0.371 (SCORE_GRID_CENTRAL) | **WIN** | team margin +4 with handicap -2.5: cover by +1.5 | 0.395641 |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Piros +2.5 games (0.629) LOSS; TOP_TOTAL Over 22.5 games (0.610) LOSS; RANK1 Over 22.5 games (0.610) LOSS. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Altmaier d. Piros 7-5 6-4; Games Altmaier 13, Piros 9; total 22; ATP 01:34:40. Identity matched on teams/players, date and competition (ATP Challenger 125 Orléans, QF).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Tennis rows count every game of the completed match; no retirement.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Piros games minus Altmaier games = -4; total 22. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Straight sets 7-5 6-4: 22 games, half a game under 22.5, and a four-game Altmaier margin, 1.5 games beyond Piros +2.5. One break in each set decided both rows; there was no tiebreak.
**R9. Source/timing review.** Settlement sources: https://www.atptour.com/en/scores/current-challenger/orleans/2273/results (ALLOWED); https://www.atptour.com/en/scores/current-challenger/orleans/2273/daily-schedule (ALLOWED). Card timing `PRE_SCHEDULED_START_WRITE`; self-declared phase labels: POST_SCHEDULED_START;TIMING_UNVERIFIED. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT LOCAL-202611128358B025-G0008 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-20261112CHAT17C8C881-G0008 revision-1 -->
### Settlement · `LOCAL-20261112CHAT17C8C881-G0008` · Zsombor Piros v Daniel Altmaier · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `3053f679b8702a8a19bef753c762cc6e5cdc74f805c8e3b57893bae40839d604`, 19698 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/chat_minis/20261112CHAT17C8C881.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `PRE_SCHEDULED_START_WRITE` (recorded `2026-11-13T22:59:48+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| D1 | Over 22.5 games | 0.62307 (MIXTURE_TREE) | **LOSS** | total 22 vs 22.5: -0.5 | 0.388216 |
| D2 | Piros +2.5 games | 0.61532 (MIXTURE_TREE) | **LOSS** | team margin -4 with handicap +2.5: cover by -1.5 | 0.378619 |
| D3 | Altmaier -2.5 games | 0.38468 (MIXTURE_TREE) | **WIN** | team margin +4 with handicap -2.5: cover by +1.5 | 0.378619 |
| D4 | Under 22.5 games | 0.37693 (MIXTURE_TREE) | **WIN** | total 22 vs 22.5: -0.5 | 0.388216 |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Piros +2.5 games (0.61532) LOSS; TOP_TOTAL Over 22.5 games (0.62307) LOSS; RANK1 Over 22.5 games (0.62307) LOSS. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Altmaier d. Piros 7-5 6-4; Games Altmaier 13, Piros 9; total 22; ATP 01:34:40. Identity matched on teams/players, date and competition (ATP Challenger 125 Orléans, QF).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Tennis rows count every game of the completed match; no retirement.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Piros games minus Altmaier games = -4; total 22. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Straight sets 7-5 6-4: 22 games, half a game under 22.5, and a four-game Altmaier margin, 1.5 games beyond Piros +2.5. One break in each set decided both rows; there was no tiebreak.
**R9. Source/timing review.** Settlement sources: https://www.atptour.com/en/scores/current-challenger/orleans/2273/results (ALLOWED); https://www.atptour.com/en/scores/current-challenger/orleans/2273/daily-schedule (ALLOWED). Card timing `PRE_SCHEDULED_START_WRITE`; self-declared phase labels: NONE_FOUND. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT LOCAL-20261112CHAT17C8C881-G0008 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-20261112CC53B5C806-G0008 revision-1 -->
### Settlement · `LOCAL-20261112CC53B5C806-G0008` · Zsombor Piros v Daniel Altmaier · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `cddf4862f379089865cda227ee66062a8bb589527d00c560c940c8bdaef3255c`, 23457 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/chat_minis/20261112CC53B5C806.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `PRE_SCHEDULED_START_WRITE` (recorded `2026-11-13T22:58:23+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| 1 | Over 22.5 games | 0.61151 (SHADOW_INDOOR_SHRINK20) | **LOSS** | total 22 vs 22.5: -0.5 | 0.373944 |
| 2 | Piros +2.5 games | 0.71777 (SHADOW_INDOOR_SHRINK20) | **LOSS** | team margin -4 with handicap +2.5: cover by -1.5 | 0.515194 |
| INFO | Under 22.5 games | 0.38849 (SHADOW_INDOOR_SHRINK20) | **WIN** | total 22 vs 22.5: -0.5 | 0.373944 |
| INFO | Altmaier -2.5 games | 0.28223 (SHADOW_INDOOR_SHRINK20) | **WIN** | team margin +4 with handicap -2.5: cover by +1.5 | 0.515194 |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Piros +2.5 games (0.71777) LOSS; TOP_TOTAL Over 22.5 games (0.61151) LOSS; RANK1 Over 22.5 games (0.61151) LOSS. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Altmaier d. Piros 7-5 6-4; Games Altmaier 13, Piros 9; total 22; ATP 01:34:40. Identity matched on teams/players, date and competition (ATP Challenger 125 Orléans, QF).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Tennis rows count every game of the completed match; no retirement.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Piros games minus Altmaier games = -4; total 22. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Straight sets 7-5 6-4: 22 games, half a game under 22.5, and a four-game Altmaier margin, 1.5 games beyond Piros +2.5. One break in each set decided both rows; there was no tiebreak.
**R9. Source/timing review.** Settlement sources: https://www.atptour.com/en/scores/current-challenger/orleans/2273/results (ALLOWED); https://www.atptour.com/en/scores/current-challenger/orleans/2273/daily-schedule (ALLOWED). Card timing `PRE_SCHEDULED_START_WRITE`; self-declared phase labels: TIMING_UNVERIFIED. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT LOCAL-20261112CC53B5C806-G0008 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-20261112D3C239297F-G0008 revision-1 -->
### Settlement · `LOCAL-20261112D3C239297F-G0008` · Zsombor Piros v Daniel Altmaier · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `ac44d030e9a40fc49bd0c0e9bd8a36feced3f9760b2abfc7cf4ab6dcd6d92c12`, 22904 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/chat_minis/20261112D3C239297F.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `POST_SCHEDULED_START_WRITE` (recorded `2026-11-13T23:01:03+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| D1 | Over 22.5 games | 0.61164 (SCENARIO_MIXTURE) | **LOSS** | total 22 vs 22.5: -0.5 | 0.374103 |
| D2 | Piros +2.5 games | 0.55786 (SCENARIO_MIXTURE) | **LOSS** | team margin -4 with handicap +2.5: cover by -1.5 | 0.311208 |
| D3 | Altmaier -2.5 games | 0.44214 (SCENARIO_MIXTURE) | **WIN** | team margin +4 with handicap -2.5: cover by +1.5 | 0.311208 |
| D4 | Under 22.5 games | 0.38836 (SCENARIO_MIXTURE) | **WIN** | total 22 vs 22.5: -0.5 | 0.374103 |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Piros +2.5 games (0.55786) LOSS; TOP_TOTAL Over 22.5 games (0.61164) LOSS; RANK1 Over 22.5 games (0.61164) LOSS. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Altmaier d. Piros 7-5 6-4; Games Altmaier 13, Piros 9; total 22; ATP 01:34:40. Identity matched on teams/players, date and competition (ATP Challenger 125 Orléans, QF).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Tennis rows count every game of the completed match; no retirement.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Piros games minus Altmaier games = -4; total 22. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Straight sets 7-5 6-4: 22 games, half a game under 22.5, and a four-game Altmaier margin, 1.5 games beyond Piros +2.5. One break in each set decided both rows; there was no tiebreak.
**R9. Source/timing review.** Settlement sources: https://www.atptour.com/en/scores/current-challenger/orleans/2273/results (ALLOWED); https://www.atptour.com/en/scores/current-challenger/orleans/2273/daily-schedule (ALLOWED). Card timing `POST_SCHEDULED_START_WRITE`; self-declared phase labels: TIMING_UNVERIFIED. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT LOCAL-20261112D3C239297F-G0008 revision-1 -->

### Deep loss reviews (DEEPLOSS-v1)

#### Deep loss review · Zsombor Piros v Daniel Altmaier · Piros +2.5 games

**1. Exact frozen claim.** `Piros +2.5 games`, full-game endpoint as each record defined it. Triggered in 6 record(s):

| Record | Trigger role(s) | Original p (basis) | Brier | Log loss |
|---|---|---|---:|---:|
| `LOCAL-202611128358B025-G0008` | TOP_SIDE | 0.629 (SCORE_GRID_CENTRAL) | 0.395641 | 0.991553 |
| `LOCAL-20261112CC53B5C806-G0008` | TOP_SIDE | 0.71777 (SHADOW_INDOOR_SHRINK20) | 0.515194 | 1.265033 |
| `LOCAL-20261112CHAT17C8C881-G0008` | TOP_SIDE | 0.61532 (MIXTURE_TREE) | 0.378619 | 0.955343 |
| `LOCAL-20261112CHAT9538BF5E-G0008` | TOP_SIDE | NOT_ESTIMATED (QUALITATIVE_UNRANKED) |  |  |
| `LOCAL-20261112D3C239297F-G0008` | TOP_SIDE | 0.55786 (SCENARIO_MIXTURE) | 0.311208 | 0.816129 |
| `LOCAL-20261112EE4AFA68-G0008` | TOP_SIDE, RANK1 | NOT_ESTIMATED (QUALITATIVE) |  |  |

No record carried a primary p_card, frozen reference or same-row baseline; BASELINE_P comparison NOT_COMPUTABLE.

**2. Verified outcome.** Altmaier d. Piros 7-5 6-4 (Games Altmaier 13, Piros 9; total 22; ATP 01:34:40). team margin -4 with handicap +2.5: cover by -1.5. Sources in R9; evidence C; final wall-clock NOT_VERIFIED (duration 1:34:40).
**3. Distribution check.** Numeric records priced this row at 0.558-0.718 (mean 0.630); a loss at those prices is a 28%-44% event under each record's own uncalibrated object. Percentile placement inside each record's printed score object is not reconstructed; the printed objects stay in the cores.
**4. Error decomposition.** Realised line distance: team margin -4 with handicap +2.5: cover by -1.5. No record had a calibrated centre or a measured effect-table row, so the miss cannot be split into reference error and adjustment error; no blame shares are invented.
**5. Research audit.** Piros 13-3 indoor season and near-equal hard Elo: TRUE per cited Tennis Abstract snapshot; Altmaier's tour-level schedule strength was not adjusted for. Facts not re-opened here remain UNVERIFIED_AT_CUTOFF; no source in any card carries a captured retrieval receipt (chat-local research).
**6. What decided the game.** Straight sets 7-5 6-4: 22 games, half a game under 22.5, and a four-game Altmaier margin, 1.5 games beyond Piros +2.5. One break in each set decided both rows; there was no tiebreak.
**7. Knowable at cutoff?** Altmaier's serve ceiling (10 aces to 1 in the match) and tour-level competition were named as the counter-case. The final score and its timing were not knowable.
**8. Process audit.** Chat-local record; no repository reference stage, no source-audit receipts, no lineup confirmation, no freeze. Timing per record in CARD_TIMING.csv (several written after the scheduled start). Endpoint and contract definitions were correct.
**9. Verdict.** Over-reliance on Challenger-level form against a tour-level opponent; CC53's own stress case had Piros +2.5 at 35%. Should have been an abstention.
**10. Cutoff-only counterfactual.** NOT_ESTIMATED: no knowable fact has a measured effect-table row, so no corrected probability is priced after the result.
**11. Failure class and recurrence.** Shared across 6 record(s) on one game: the parallel chats used overlapping public inputs, so their losses are one dependent observation, not 6 independent ones.
**12. Correction.** NO_CHANGE to any rule from one result. Procedure proposals are in AUDIT_REPORT §6 (PROPOSED_NOT_TESTED).
**13. Matched wins.** None among the triggering records.
**14. Honesty.** Original numbers and labels preserved; no luck claim without the arithmetic above; no invented percentages, operator terms or publication times. Preservation PASS; information closure INCOMPLETE.

#### Deep loss review · Zsombor Piros v Daniel Altmaier · Over 22.5 games

**1. Exact frozen claim.** `Over 22.5 games`, full-game endpoint as each record defined it. Triggered in 6 record(s):

| Record | Trigger role(s) | Original p (basis) | Brier | Log loss |
|---|---|---|---:|---:|
| `LOCAL-202611128358B025-G0008` | TOP_TOTAL, RANK1 | 0.610 (SCORE_GRID_CENTRAL) | 0.372100 | 0.941609 |
| `LOCAL-20261112CC53B5C806-G0008` | TOP_TOTAL, RANK1 | 0.61151 (SHADOW_INDOOR_SHRINK20) | 0.373944 | 0.945488 |
| `LOCAL-20261112CHAT17C8C881-G0008` | TOP_TOTAL, RANK1 | 0.62307 (MIXTURE_TREE) | 0.388216 | 0.975696 |
| `LOCAL-20261112CHAT9538BF5E-G0008` | TOP_TOTAL, RANK1 | NOT_ESTIMATED (QUALITATIVE_UNRANKED) |  |  |
| `LOCAL-20261112D3C239297F-G0008` | TOP_TOTAL, RANK1 | 0.61164 (SCENARIO_MIXTURE) | 0.374103 | 0.945823 |
| `LOCAL-20261112EE4AFA68-G0008` | TOP_TOTAL | NOT_ESTIMATED (QUALITATIVE) |  |  |

No record carried a primary p_card, frozen reference or same-row baseline; BASELINE_P comparison NOT_COMPUTABLE.

**2. Verified outcome.** Altmaier d. Piros 7-5 6-4 (Games Altmaier 13, Piros 9; total 22; ATP 01:34:40). total 22 vs 22.5: -0.5. Sources in R9; evidence C; final wall-clock NOT_VERIFIED (duration 1:34:40).
**3. Distribution check.** Numeric records priced this row at 0.610-0.623 (mean 0.614); a loss at those prices is a 38%-39% event under each record's own uncalibrated object. Percentile placement inside each record's printed score object is not reconstructed; the printed objects stay in the cores.
**4. Error decomposition.** Realised line distance: total 22 vs 22.5: -0.5. No record had a calibrated centre or a measured effect-table row, so the miss cannot be split into reference error and adjustment error; no blame shares are invented.
**5. Research audit.** Both players 2/2 three-set wins in Orléans: TRUE per draw results. Hold-rate inputs (82-85%) were assumed, as the cards disclosed. Facts not re-opened here remain UNVERIFIED_AT_CUTOFF; no source in any card carries a captured retrieval receipt (chat-local research).
**6. What decided the game.** Straight sets 7-5 6-4: 22 games, half a game under 22.5, and a four-game Altmaier margin, 1.5 games beyond Piros +2.5. One break in each set decided both rows; there was no tiebreak.
**7. Knowable at cutoff?** A routine two-set match was the named kill path in every card. The final score and its timing were not knowable.
**8. Process audit.** Chat-local record; no repository reference stage, no source-audit receipts, no lineup confirmation, no freeze. Timing per record in CARD_TIMING.csv (several written after the scheduled start). Endpoint and contract definitions were correct.
**9. Verdict.** Lost by half a game on a 7-5 6-4 scoreline. Close loss on the line, but every chat paired it with Piros +2.5, so both legs died on the same Altmaier straight-sets path.
**10. Cutoff-only counterfactual.** NOT_ESTIMATED: no knowable fact has a measured effect-table row, so no corrected probability is priced after the result.
**11. Failure class and recurrence.** Shared across 6 record(s) on one game: the parallel chats used overlapping public inputs, so their losses are one dependent observation, not 6 independent ones.
**12. Correction.** NO_CHANGE to any rule from one result. Procedure proposals are in AUDIT_REPORT §6 (PROPOSED_NOT_TESTED).
**13. Matched wins.** None among the triggering records.
**14. Honesty.** Original numbers and labels preserved; no luck claim without the arithmetic above; no invented percentages, operator terms or publication times. Preservation PASS; information closure INCOMPLETE.

#### Joint section · top side and top total both lost · Zsombor Piros v Daniel Altmaier

Records: `LOCAL-20261112EE4AFA68-G0008`: Piros +2.5 games and Over 22.5 games; `LOCAL-20261112CHAT9538BF5E-G0008`: Piros +2.5 games and Over 22.5 games; `LOCAL-202611128358B025-G0008`: Piros +2.5 games and Over 22.5 games; `LOCAL-20261112CHAT17C8C881-G0008`: Piros +2.5 games and Over 22.5 games; `LOCAL-20261112CC53B5C806-G0008`: Piros +2.5 games and Over 22.5 games; `LOCAL-20261112D3C239297F-G0008`: Piros +2.5 games and Over 22.5 games. Both legs failed on the same game state (Altmaier d. Piros 7-5 6-4). The cards' own joint-failure figures, where printed, are retained in the cores; none was calibrated, and treating the two leans as independent picks would double-count one wrong read of the game.

<!-- END SETTLEMENT EVENT E18 revision-1 -->

<!-- BEGIN SETTLEMENT EVENT E19 revision-1 -->
## Event · Alejandro Tabilo v Thiago Agustín Tirante · 2026-11-13 · ATP 250 Stockholm Open, SF

**Final:** Tirante d. Tabilo 7-5 7-6(1). **Periods:** Games Tirante 14, Tabilo 11; total 25; ATP 01:46:11; TennisExplorer start 14:10 (zone not stated). **Evidence B.** Scheduled 2026-11-13T13:00:00+00:00.

| Opened source | Audit | Field read |
|---|---|---|
| https://www.atptour.com/en/scores/current/stockholm/429/results | ALLOWED | 'Thiago Agustin Tirante wins the match 7-5 7-6(1)'; 01:46:11 |
| https://www.tennismajors.com/matches/atp/stockholm-open/alejandro-tabilo-vs-thiago-agustin-tirante-4 | ALLOWED | Same score; 'Duration : 1h46' |
| https://www.tennisexplorer.com/stockholm/2026/atp-men/ | ALLOWED | Same score; start 14:10 |

<!-- BEGIN SETTLEMENT LOCAL-20261112EE4AFA68-G0009 revision-1 -->
### Settlement · `LOCAL-20261112EE4AFA68-G0009` · Alejandro Tabilo v Thiago Agustín Tirante · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `413c121deb873250df31dcc8bb070fcfd789d4d3fc91d2c45b3d1aa5f2e05f80`, 27602 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/chat_minis/20261112EE4AFA68.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `POST_SCHEDULED_START_WRITE` (recorded `2026-11-14T00:08:42+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| 1 | Over 24.5 games | NOT_ESTIMATED (QUALITATIVE) | **WIN** | total 25 vs 24.5: +0.5 |  |
| 2 | Tabilo -1.5 games | NOT_ESTIMATED (QUALITATIVE) | **LOSS** | team margin -3 with handicap -1.5: cover by -4.5 |  |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Tabilo -1.5 games (NOT_ESTIMATED) LOSS; TOP_TOTAL Over 24.5 games (NOT_ESTIMATED) WIN; RANK1 Over 24.5 games (NOT_ESTIMATED) WIN. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Tirante d. Tabilo 7-5 7-6(1); Games Tirante 14, Tabilo 11; total 25; ATP 01:46:11; TennisExplorer start 14:10 (zone not stated). Identity matched on teams/players, date and competition (ATP 250 Stockholm Open, SF).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Tennis rows count every game of the completed match; no retirement.
**R4. Rank diagnostics.** 1W/1L/0U over 2 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Tabilo games minus Tirante games = -3; total 25. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Tirante won 7-5 and a 7-6(1) tiebreak: 25 games (Over 24.5 by half a game, carried by the tiebreak) and a three-game Tirante margin, so Tabilo -1.5 lost by 4.5.
**R9. Source/timing review.** Settlement sources: https://www.atptour.com/en/scores/current/stockholm/429/results (ALLOWED); https://www.tennismajors.com/matches/atp/stockholm-open/alejandro-tabilo-vs-thiago-agustin-tirante-4 (ALLOWED); https://www.tennisexplorer.com/stockholm/2026/atp-men/ (ALLOWED). Card timing `POST_SCHEDULED_START_WRITE`; self-declared phase labels: TIMING_UNVERIFIED. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT LOCAL-20261112EE4AFA68-G0009 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-20261112CHAT9538BF5E-G0009 revision-1 -->
### Settlement · `LOCAL-20261112CHAT9538BF5E-G0009` · Alejandro Tabilo v Thiago Agustín Tirante · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `d6e28b747aaf81aac641c5af1e3eaefd567e5f13a092c4093b6c01cf4538d76c`, 20256 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/chat_minis/20261112CHAT9538BF5E.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `POST_SCHEDULED_START_WRITE` (recorded `2026-11-14T00:08:30+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| PROV1 | Tabilo -1.5 games | NOT_ESTIMATED (QUALITATIVE_UNRANKED) | **LOSS** | team margin -3 with handicap -1.5: cover by -4.5 |  |
| PROV2 | Over 24.5 games | NOT_ESTIMATED (QUALITATIVE_UNRANKED) | **WIN** | total 25 vs 24.5: +0.5 |  |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Tabilo -1.5 games (NOT_ESTIMATED) LOSS; TOP_TOTAL Over 24.5 games (NOT_ESTIMATED) WIN; RANK1 Tabilo -1.5 games (NOT_ESTIMATED) LOSS. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Tirante d. Tabilo 7-5 7-6(1); Games Tirante 14, Tabilo 11; total 25; ATP 01:46:11; TennisExplorer start 14:10 (zone not stated). Identity matched on teams/players, date and competition (ATP 250 Stockholm Open, SF).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Tennis rows count every game of the completed match; no retirement.
**R4. Rank diagnostics.** 1W/1L/0U over 2 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Tabilo games minus Tirante games = -3; total 25. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Tirante won 7-5 and a 7-6(1) tiebreak: 25 games (Over 24.5 by half a game, carried by the tiebreak) and a three-game Tirante margin, so Tabilo -1.5 lost by 4.5.
**R9. Source/timing review.** Settlement sources: https://www.atptour.com/en/scores/current/stockholm/429/results (ALLOWED); https://www.tennismajors.com/matches/atp/stockholm-open/alejandro-tabilo-vs-thiago-agustin-tirante-4 (ALLOWED); https://www.tennisexplorer.com/stockholm/2026/atp-men/ (ALLOWED). Card timing `POST_SCHEDULED_START_WRITE`; self-declared phase labels: POST_START_POSSIBLE;TIMING_UNVERIFIED. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT LOCAL-20261112CHAT9538BF5E-G0009 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-202611128358B025-G0009 revision-1 -->
### Settlement · `LOCAL-202611128358B025-G0009` · Alejandro Tabilo v Thiago Agustín Tirante · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `0acc73e096d6dff8e8cc188053a37d648ee70c69ffb6017ebb9f250c3726fcdb`, 18170 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/chat_minis/202611128358B025.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `POST_SCHEDULED_START_WRITE` (recorded `2026-11-14T00:08:46+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| D1 | Over 24.5 games | 0.5621 (CENTRAL_GRID) | **WIN** | total 25 vs 24.5: +0.5 | 0.191756 |
| D2 | Tirante +1.5 games | 0.5301 (CENTRAL_GRID) | **WIN** | team margin +3 with handicap +1.5: cover by +4.5 | 0.220806 |
| D3 | Tabilo -1.5 games | 0.4699 (CENTRAL_GRID) | **LOSS** | team margin -3 with handicap -1.5: cover by -4.5 | 0.220806 |
| D4 | Under 24.5 games | 0.4379 (CENTRAL_GRID) | **LOSS** | total 25 vs 24.5: +0.5 | 0.191756 |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Tirante +1.5 games (0.5301) WIN; TOP_TOTAL Over 24.5 games (0.5621) WIN; RANK1 Over 24.5 games (0.5621) WIN. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Tirante d. Tabilo 7-5 7-6(1); Games Tirante 14, Tabilo 11; total 25; ATP 01:46:11; TennisExplorer start 14:10 (zone not stated). Identity matched on teams/players, date and competition (ATP 250 Stockholm Open, SF).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Tennis rows count every game of the completed match; no retirement.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Tabilo games minus Tirante games = -3; total 25. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Tirante won 7-5 and a 7-6(1) tiebreak: 25 games (Over 24.5 by half a game, carried by the tiebreak) and a three-game Tirante margin, so Tabilo -1.5 lost by 4.5.
**R9. Source/timing review.** Settlement sources: https://www.atptour.com/en/scores/current/stockholm/429/results (ALLOWED); https://www.tennismajors.com/matches/atp/stockholm-open/alejandro-tabilo-vs-thiago-agustin-tirante-4 (ALLOWED); https://www.tennisexplorer.com/stockholm/2026/atp-men/ (ALLOWED). Card timing `POST_SCHEDULED_START_WRITE`; self-declared phase labels: POST_SCHEDULED_START_ISSUE;TIMING_UNVERIFIED. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT LOCAL-202611128358B025-G0009 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-20261112CHAT17C8C881-G0009 revision-1 -->
### Settlement · `LOCAL-20261112CHAT17C8C881-G0009` · Alejandro Tabilo v Thiago Agustín Tirante · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `b1977ea7ff995eb32a128021c2b26b7fe2ad12460f1be30751d05cd0cfb176b7`, 23385 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/chat_minis/20261112CHAT17C8C881.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `POST_SCHEDULED_START_WRITE` (recorded `2026-11-14T00:01:00+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| D1 | Over 24.5 games | 0.559927 (MIXTURE_TREE) | **WIN** | total 25 vs 24.5: +0.5 | 0.193664 |
| D2 | Tirante +1.5 games | 0.551066 (MIXTURE_TREE) | **WIN** | team margin +3 with handicap +1.5: cover by +4.5 | 0.201542 |
| D3 | Tabilo -1.5 games | 0.448934 (MIXTURE_TREE) | **LOSS** | team margin -3 with handicap -1.5: cover by -4.5 | 0.201542 |
| D4 | Under 24.5 games | 0.440073 (MIXTURE_TREE) | **LOSS** | total 25 vs 24.5: +0.5 | 0.193664 |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Tirante +1.5 games (0.551066) WIN; TOP_TOTAL Over 24.5 games (0.559927) WIN; RANK1 Over 24.5 games (0.559927) WIN. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Tirante d. Tabilo 7-5 7-6(1); Games Tirante 14, Tabilo 11; total 25; ATP 01:46:11; TennisExplorer start 14:10 (zone not stated). Identity matched on teams/players, date and competition (ATP 250 Stockholm Open, SF).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Tennis rows count every game of the completed match; no retirement.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Tabilo games minus Tirante games = -3; total 25. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Tirante won 7-5 and a 7-6(1) tiebreak: 25 games (Over 24.5 by half a game, carried by the tiebreak) and a three-game Tirante margin, so Tabilo -1.5 lost by 4.5.
**R9. Source/timing review.** Settlement sources: https://www.atptour.com/en/scores/current/stockholm/429/results (ALLOWED); https://www.tennismajors.com/matches/atp/stockholm-open/alejandro-tabilo-vs-thiago-agustin-tirante-4 (ALLOWED); https://www.tennisexplorer.com/stockholm/2026/atp-men/ (ALLOWED). Card timing `POST_SCHEDULED_START_WRITE`; self-declared phase labels: POST_SCHEDULED_START_RESEARCH. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT LOCAL-20261112CHAT17C8C881-G0009 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-20261112CC53B5C806-G0009 revision-1 -->
### Settlement · `LOCAL-20261112CC53B5C806-G0009` · Alejandro Tabilo v Thiago Agustín Tirante · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `089ec58118edc6c6bd6c47087c2f154b3d5b554aea7f1087d01db522900fe3cc`, 22795 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/chat_minis/20261112CC53B5C806.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `POST_SCHEDULED_START_WRITE` (recorded `2026-11-14T00:08:53+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| 1 | Tirante +1.5 games | 0.598 (SHADOW_INDOOR_SHRINK20) | **WIN** | team margin +3 with handicap +1.5: cover by +4.5 | 0.161604 |
| 2 | Over 24.5 games | 0.551 (SHADOW_INDOOR_SHRINK20) | **WIN** | total 25 vs 24.5: +0.5 | 0.201601 |
| INFO | Under 24.5 games | 0.449 (SHADOW_INDOOR_SHRINK20) | **LOSS** | total 25 vs 24.5: +0.5 | 0.201601 |
| INFO | Tabilo -1.5 games | 0.402 (SHADOW_INDOOR_SHRINK20) | **LOSS** | team margin -3 with handicap -1.5: cover by -4.5 | 0.161604 |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Tirante +1.5 games (0.598) WIN; TOP_TOTAL Over 24.5 games (0.551) WIN; RANK1 Tirante +1.5 games (0.598) WIN. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Tirante d. Tabilo 7-5 7-6(1); Games Tirante 14, Tabilo 11; total 25; ATP 01:46:11; TennisExplorer start 14:10 (zone not stated). Identity matched on teams/players, date and competition (ATP 250 Stockholm Open, SF).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Tennis rows count every game of the completed match; no retirement.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Tabilo games minus Tirante games = -3; total 25. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Tirante won 7-5 and a 7-6(1) tiebreak: 25 games (Over 24.5 by half a game, carried by the tiebreak) and a three-game Tirante margin, so Tabilo -1.5 lost by 4.5.
**R9. Source/timing review.** Settlement sources: https://www.atptour.com/en/scores/current/stockholm/429/results (ALLOWED); https://www.tennismajors.com/matches/atp/stockholm-open/alejandro-tabilo-vs-thiago-agustin-tirante-4 (ALLOWED); https://www.tennisexplorer.com/stockholm/2026/atp-men/ (ALLOWED). Card timing `POST_SCHEDULED_START_WRITE`; self-declared phase labels: TIMING_UNVERIFIED. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT LOCAL-20261112CC53B5C806-G0009 revision-1 -->

`LOCAL-20261112D3C239297F-G0009`: MISSING_ORIGINAL; only its scenario script and JSON exist (`tennis_stockholm_tabilo_tirante_scenario_20261114.*`). Not graded.

### Deep loss reviews (DEEPLOSS-v1)

#### Deep loss review · Alejandro Tabilo v Thiago Agustín Tirante · Tabilo -1.5 games

**1. Exact frozen claim.** `Tabilo -1.5 games`, full-game endpoint as each record defined it. Triggered in 2 record(s):

| Record | Trigger role(s) | Original p (basis) | Brier | Log loss |
|---|---|---|---:|---:|
| `LOCAL-20261112CHAT9538BF5E-G0009` | TOP_SIDE, RANK1 | NOT_ESTIMATED (QUALITATIVE_UNRANKED) |  |  |
| `LOCAL-20261112EE4AFA68-G0009` | TOP_SIDE | NOT_ESTIMATED (QUALITATIVE) |  |  |

No record carried a primary p_card, frozen reference or same-row baseline; BASELINE_P comparison NOT_COMPUTABLE.

**2. Verified outcome.** Tirante d. Tabilo 7-5 7-6(1) (Games Tirante 14, Tabilo 11; total 25; ATP 01:46:11; TennisExplorer start 14:10 (zone not stated)). team margin -3 with handicap -1.5: cover by -4.5. Sources in R9; evidence B; final wall-clock NOT_VERIFIED (duration 1:46:11).
**3. Distribution check.** Every triggering record was qualitative (NOT_ESTIMATED), so there is no frozen distribution to place the result in. Percentile placement inside each record's printed score object is not reconstructed; the printed objects stay in the cores.
**4. Error decomposition.** Realised line distance: team margin -3 with handicap -1.5: cover by -4.5. No record had a calibrated centre or a measured effect-table row, so the miss cannot be split into reference error and adjustment error; no blame shares are invented.
**5. Research audit.** Tabilo's ranking/Elo and the Cancún H2H were TRUE; Tirante's 17/17 service-hold run was also TRUE and printed. Facts not re-opened here remain UNVERIFIED_AT_CUTOFF; no source in any card carries a captured retrieval receipt (chat-local research).
**6. What decided the game.** Tirante won 7-5 and a 7-6(1) tiebreak: 25 games (Over 24.5 by half a game, carried by the tiebreak) and a three-game Tirante margin, so Tabilo -1.5 lost by 4.5.
**7. Knowable at cutoff?** Tirante's serve form and Tabilo's heavier match load (2h53 + 1h54) were known. The final score and its timing were not knowable.
**8. Process audit.** Chat-local record; no repository reference stage, no source-audit receipts, no lineup confirmation, no freeze. Timing per record in CARD_TIMING.csv (several written after the scheduled start). Endpoint and contract definitions were correct.
**9. Verdict.** The numeric chats all had Tirante +1.5 above 53%; the two qualitative chats that leaned Tabilo -1.5 went against their own evidence. Loss margin 4.5 games.
**10. Cutoff-only counterfactual.** NOT_ESTIMATED: no knowable fact has a measured effect-table row, so no corrected probability is priced after the result.
**11. Failure class and recurrence.** Shared across 2 record(s) on one game: the parallel chats used overlapping public inputs, so their losses are one dependent observation, not 2 independent ones.
**12. Correction.** NO_CHANGE to any rule from one result. Procedure proposals are in AUDIT_REPORT §6 (PROPOSED_NOT_TESTED).
**13. Matched wins.** `LOCAL-20261112CHAT9538BF5E-G0009` TOP_TOTAL Over 24.5 games WIN; `LOCAL-20261112EE4AFA68-G0009` RANK1 Over 24.5 games WIN; `LOCAL-20261112EE4AFA68-G0009` TOP_TOTAL Over 24.5 games WIN. These rest on the same unvalidated construction and do not show the process worked.
**14. Honesty.** Original numbers and labels preserved; no luck claim without the arithmetic above; no invented percentages, operator terms or publication times. Preservation PASS; information closure INCOMPLETE.

<!-- END SETTLEMENT EVENT E19 revision-1 -->

<!-- BEGIN SETTLEMENT EVENT E20 revision-1 -->
## Event · Bryant Bulldogs @ Rutgers Scarlet Knights · 2026-11-13 ET · NCAA Division I men 2026-27

**Final:** Rutgers 72-51 Bryant. **Periods:** Half 35-31 Rutgers; second half 37-20 (derived); no OT indicated. **Evidence B.** Scheduled 2026-11-13T23:00:00+00:00.

| Opened source | Audit | Field read |
|---|---|---|
| https://bryantbulldogs.com/news/2026/11/13/mens-basketball-behar-scores-19-bulldogs-fall-at-rutgers-on-friday.aspx | ALLOWED | 'Rutgers 72, Bryant 51'; 'take a 35-31 lead to the break' |
| https://scarletknights.com/news/2026/11/13/mens-basketball-gurdak-dominates-inside-as-rutgers-pulls-away-from-bryant-72-51 | ALLOWED | Headline only: '... Past Bryant, 72-51' |

<!-- BEGIN SETTLEMENT LOCAL-20261112EE4AFA68-G0010 revision-1 -->
### Settlement · `LOCAL-20261112EE4AFA68-G0010` · Bryant Bulldogs @ Rutgers Scarlet Knights · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `6767f01509576c7ce93c01512f6acc6658f1218e2f09958ddf021096617cf499`, 25193 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/chat_minis/20261112EE4AFA68.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `PRE_SCHEDULED_START_WRITE` (recorded `2026-11-14T09:59:54+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| PREF | Under 148.5 | NOT_ESTIMATED (QUALITATIVE) | **WIN** | total 123 vs 148.5: -25.5 |  |
| SECOND | Bryant +21.5 | NOT_ESTIMATED (QUALITATIVE) | **WIN** | team margin -21 with handicap +21.5: cover by +0.5 |  |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Bryant +21.5 (NOT_ESTIMATED) WIN; TOP_TOTAL Under 148.5 (NOT_ESTIMATED) WIN; RANK1 Under 148.5 (NOT_ESTIMATED) WIN. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Rutgers 72-51 Bryant; Half 35-31 Rutgers; second half 37-20 (derived); no OT indicated. Identity matched on teams/players, date and competition (NCAA Division I men 2026-27).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Basketball rows include overtime (BK-OT-1); none occurred.
**R4. Rank diagnostics.** 2W/0L/0U over 2 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Rutgers minus Bryant = +21; total 123. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Bryant trailed only 35-31 at half; Rutgers won the second half 37-20 (Gurdak 20/14, Davis 18). The margin landed on exactly 21, so Rutgers -21.5 lost and Bryant +21.5 won by half a point; the 123-point total was 25.5 under 148.5.
**R9. Source/timing review.** Settlement sources: https://bryantbulldogs.com/news/2026/11/13/mens-basketball-behar-scores-19-bulldogs-fall-at-rutgers-on-friday.aspx (ALLOWED); https://scarletknights.com/news/2026/11/13/mens-basketball-gurdak-dominates-inside-as-rutgers-pulls-away-from-bryant-72-51 (ALLOWED). Card timing `PRE_SCHEDULED_START_WRITE`; self-declared phase labels: TIMING_UNVERIFIED. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT LOCAL-20261112EE4AFA68-G0010 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-20261112CHAT9538BF5E-G0010 revision-1 -->
### Settlement · `LOCAL-20261112CHAT9538BF5E-G0010` · Bryant Bulldogs @ Rutgers Scarlet Knights · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `a6e9d47e4c00b6d20b354145a030515d69900c5f66606c86645dc62b992de396`, 20926 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/chat_minis/20261112CHAT9538BF5E.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `PRE_SCHEDULED_START_WRITE` (recorded `2026-11-14T09:58:38+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| LEAN_TOTAL | Under 148.5 | NOT_ESTIMATED (QUALITATIVE_UNRANKED) | **WIN** | total 123 vs 148.5: -25.5 |  |
| LEAN_SIDE | Rutgers -21.5 | NOT_ESTIMATED (QUALITATIVE_UNRANKED) | **LOSS** | team margin +21 with handicap -21.5: cover by -0.5 |  |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Rutgers -21.5 (NOT_ESTIMATED) LOSS; TOP_TOTAL Under 148.5 (NOT_ESTIMATED) WIN; RANK1 Under 148.5 (NOT_ESTIMATED) WIN. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Rutgers 72-51 Bryant; Half 35-31 Rutgers; second half 37-20 (derived); no OT indicated. Identity matched on teams/players, date and competition (NCAA Division I men 2026-27).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Basketball rows include overtime (BK-OT-1); none occurred.
**R4. Rank diagnostics.** 1W/1L/0U over 2 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Rutgers minus Bryant = +21; total 123. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Bryant trailed only 35-31 at half; Rutgers won the second half 37-20 (Gurdak 20/14, Davis 18). The margin landed on exactly 21, so Rutgers -21.5 lost and Bryant +21.5 won by half a point; the 123-point total was 25.5 under 148.5.
**R9. Source/timing review.** Settlement sources: https://bryantbulldogs.com/news/2026/11/13/mens-basketball-behar-scores-19-bulldogs-fall-at-rutgers-on-friday.aspx (ALLOWED); https://scarletknights.com/news/2026/11/13/mens-basketball-gurdak-dominates-inside-as-rutgers-pulls-away-from-bryant-72-51 (ALLOWED). Card timing `PRE_SCHEDULED_START_WRITE`; self-declared phase labels: TIMING_UNVERIFIED. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT LOCAL-20261112CHAT9538BF5E-G0010 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-202611128358B025-G0010 revision-1 -->
### Settlement · `LOCAL-202611128358B025-G0010` · Bryant Bulldogs @ Rutgers Scarlet Knights · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `dd49c83b2a296e70378bd781290a40f3b2336cb8bbcac2d1dc9fd840271680e8`, 19062 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/chat_minis/202611128358B025.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `POST_SCHEDULED_START_WRITE` (recorded `2026-11-14T10:00:23+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| D1 | Under 148.5 | 0.632110 (SCENARIO_CENTRAL) | **WIN** | total 123 vs 148.5: -25.5 | 0.135343 |
| D2 | Bryant +21.5 | 0.518715 (SCENARIO_CENTRAL) | **WIN** | team margin -21 with handicap +21.5: cover by +0.5 | 0.231635 |
| D3 | Rutgers -21.5 | 0.481285 (SCENARIO_CENTRAL) | **LOSS** | team margin +21 with handicap -21.5: cover by -0.5 | 0.231635 |
| D4 | Over 148.5 | 0.367890 (SCENARIO_CENTRAL) | **LOSS** | total 123 vs 148.5: -25.5 | 0.135343 |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Bryant +21.5 (0.518715) WIN; TOP_TOTAL Under 148.5 (0.632110) WIN; RANK1 Under 148.5 (0.632110) WIN. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Rutgers 72-51 Bryant; Half 35-31 Rutgers; second half 37-20 (derived); no OT indicated. Identity matched on teams/players, date and competition (NCAA Division I men 2026-27).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Basketball rows include overtime (BK-OT-1); none occurred.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Rutgers minus Bryant = +21; total 123. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Bryant trailed only 35-31 at half; Rutgers won the second half 37-20 (Gurdak 20/14, Davis 18). The margin landed on exactly 21, so Rutgers -21.5 lost and Bryant +21.5 won by half a point; the 123-point total was 25.5 under 148.5.
**R9. Source/timing review.** Settlement sources: https://bryantbulldogs.com/news/2026/11/13/mens-basketball-behar-scores-19-bulldogs-fall-at-rutgers-on-friday.aspx (ALLOWED); https://scarletknights.com/news/2026/11/13/mens-basketball-gurdak-dominates-inside-as-rutgers-pulls-away-from-bryant-72-51 (ALLOWED). Card timing `POST_SCHEDULED_START_WRITE`; self-declared phase labels: NONE_FOUND. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT LOCAL-202611128358B025-G0010 revision-1 -->

`LOCAL-20261112D3C239297F-G0010`: MISSING_ORIGINAL (script/JSON `ncaab_bryant_rutgers_scenario_20261114.*` only). Not graded.

### Deep loss reviews (DEEPLOSS-v1)

#### Deep loss review · Bryant Bulldogs @ Rutgers Scarlet Knights · Rutgers -21.5

**1. Exact frozen claim.** `Rutgers -21.5`, full-game endpoint as each record defined it. Triggered in 1 record(s):

| Record | Trigger role(s) | Original p (basis) | Brier | Log loss |
|---|---|---|---:|---:|
| `LOCAL-20261112CHAT9538BF5E-G0010` | TOP_SIDE | NOT_ESTIMATED (QUALITATIVE_UNRANKED) |  |  |

No record carried a primary p_card, frozen reference or same-row baseline; BASELINE_P comparison NOT_COMPUTABLE.

**2. Verified outcome.** Rutgers 72-51 Bryant (Half 35-31 Rutgers; second half 37-20 (derived); no OT indicated). team margin +21 with handicap -21.5: cover by -0.5. Sources in R9; evidence B; final wall-clock NOT_VERIFIED.
**3. Distribution check.** Every triggering record was qualitative (NOT_ESTIMATED), so there is no frozen distribution to place the result in. Percentile placement inside each record's printed score object is not reconstructed; the printed objects stay in the cores.
**4. Error decomposition.** Realised line distance: team margin +21 with handicap -21.5: cover by -0.5. No record had a calibrated centre or a measured effect-table row, so the miss cannot be split into reference error and adjustment error; no blame shares are invented.
**5. Research audit.** Rutgers wins by 27 and 37 over weak openers: TRUE; Bryant's 25 turnovers at Providence: TRUE per cited preview. Facts not re-opened here remain UNVERIFIED_AT_CUTOFF; no source in any card carries a captured retrieval receipt (chat-local research).
**6. What decided the game.** Bryant trailed only 35-31 at half; Rutgers won the second half 37-20 (Gurdak 20/14, Davis 18). The margin landed on exactly 21, so Rutgers -21.5 lost and Bryant +21.5 won by half a point; the 123-point total was 25.5 under 148.5.
**7. Knowable at cutoff?** The descriptive margin centre (20.6) was printed below the line. The final score and its timing were not knowable.
**8. Process audit.** Chat-local record; no repository reference stage, no source-audit receipts, no lineup confirmation, no freeze. Timing per record in CARD_TIMING.csv (several written after the scheduled start). Endpoint and contract definitions were correct.
**9. Verdict.** Lost by half a point at exactly 21. The card's own centre was below the line, so leaning the favourite was not supported by its numbers.
**10. Cutoff-only counterfactual.** NOT_ESTIMATED: no knowable fact has a measured effect-table row, so no corrected probability is priced after the result.
**11. Failure class and recurrence.** Shared across 1 record(s) on one game: the parallel chats used overlapping public inputs, so their losses are one dependent observation, not 1 independent ones.
**12. Correction.** NO_CHANGE to any rule from one result. Procedure proposals are in AUDIT_REPORT §6 (PROPOSED_NOT_TESTED).
**13. Matched wins.** `LOCAL-20261112CHAT9538BF5E-G0010` RANK1 Under 148.5 WIN; `LOCAL-20261112CHAT9538BF5E-G0010` TOP_TOTAL Under 148.5 WIN. These rest on the same unvalidated construction and do not show the process worked.
**14. Honesty.** Original numbers and labels preserved; no luck claim without the arithmetic above; no invented percentages, operator terms or publication times. Preservation PASS; information closure INCOMPLETE.

<!-- END SETTLEMENT EVENT E20 revision-1 -->

<!-- BEGIN SETTLEMENT EVENT E21 revision-1 -->
## Event · New York Knicks @ Indiana Pacers · 2026-11-13 ET · NBA 2026-27, Emirates NBA Cup East Group B (game 0022600034)

**Final:** Indiana 106-104 New York. **Periods:** Quarter line not in permitted text; Knicks scored 20 in Q4 and topped 27 only in Q3 (SI); no OT indicated. **Evidence C.** Scheduled 2026-11-14T00:00:00+00:00. Note: Single opened lineage (SI); evidence C.

| Opened source | Audit | Field read |
|---|---|---|
| https://www.si.com/nba/pacers/onsi/pacers-defeat-knicks-in-nba-cup-thriller-01m7bmcnjg37 | ALLOWED | 'by a final score of 106-104' |
| https://www.talkbasket.net/228011-pacers-survive-defending-champions-knicks-106-104 | ALLOWED | HTTP 403 at open: no value read |

<!-- BEGIN SETTLEMENT LOCAL-20261112EE4AFA68-G0011 revision-1 -->
### Settlement · `LOCAL-20261112EE4AFA68-G0011` · New York Knicks @ Indiana Pacers · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `9a5887eeb7810d3dfcb3022dbc92be99eb560e3cf41b79ce0593529da6948ac0`, 19826 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/chat_minis/20261112EE4AFA68.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `POST_SCHEDULED_START_WRITE` (recorded `2026-11-14T11:08:55+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| PREF | Under 219.5 | NOT_ESTIMATED (QUALITATIVE) | **WIN** | total 210 vs 219.5: -9.5 |  |
| SECOND | Knicks -7.5 | NOT_ESTIMATED (QUALITATIVE) | **LOSS** | team margin -2 with handicap -7.5: cover by -9.5 |  |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Knicks -7.5 (NOT_ESTIMATED) LOSS; TOP_TOTAL Under 219.5 (NOT_ESTIMATED) WIN; RANK1 Under 219.5 (NOT_ESTIMATED) WIN. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Indiana 106-104 New York; Quarter line not in permitted text; Knicks scored 20 in Q4 and topped 27 only in Q3 (SI); no OT indicated. Identity matched on teams/players, date and competition (NBA 2026-27, Emirates NBA Cup East Group B (game 0022600034)).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Basketball rows include overtime (BK-OT-1); none occurred.
**R4. Rank diagnostics.** 1W/1L/0U over 2 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Knicks minus Pacers = -2; total 210. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Indiana, without Haliburton, won 106-104; Towns missed a tying jumper at the buzzer (search summary, not an opened page). Knicks -7.5 lost by 9.5 points; the 210 total was 9.5 under 219.5.
**R9. Source/timing review.** Settlement sources: https://www.si.com/nba/pacers/onsi/pacers-defeat-knicks-in-nba-cup-thriller-01m7bmcnjg37 (ALLOWED); https://www.talkbasket.net/228011-pacers-survive-defending-champions-knicks-106-104 (ALLOWED). Card timing `POST_SCHEDULED_START_WRITE`; self-declared phase labels: POST_OFFICIAL_SCHEDULE;TIMING_UNVERIFIED. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT LOCAL-20261112EE4AFA68-G0011 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-202611128358B025-G0011 revision-1 -->
### Settlement · `LOCAL-202611128358B025-G0011` · New York Knicks @ Indiana Pacers · revision-1

Parent: ORIGINAL_RECORD (frozen core SHA `5027fb15b08bd70aa93e723d3a06abc0af42df905923ec6bdc830586caff3f72`, 17712 B, source `research/verification/mini_import_P-639_P-659_2026-11-14-1/inputs/chat_minis/202611128358B025.md`). Effective 2026-11-14T12:15:21+00:00; affected keys: every row below. Issue status NOT_ISSUED (chat-local); timing `POST_SCHEDULED_START_WRITE` (recorded `2026-11-14T11:09:22+11:00`).

| Original order/role | Exact proposition (literal) | Original p (basis) | Grade | Arithmetic | Diagnostic Brier |
|---|---|---|---|---|---:|
| D1 | Pacers +7.5 | 0.635445 (SCENARIO_CENTRAL) | **WIN** | team margin +2 with handicap +7.5: cover by +9.5 | 0.132900 |
| D2 | Over 219.5 | 0.512970 (SCENARIO_CENTRAL) | **LOSS** | total 210 vs 219.5: -9.5 | 0.263138 |
| D3 | Under 219.5 | 0.487030 (SCENARIO_CENTRAL) | **WIN** | total 210 vs 219.5: -9.5 | 0.263138 |
| D4 | Knicks -7.5 | 0.364555 (SCENARIO_CENTRAL) | **LOSS** | team margin -2 with handicap -7.5: cover by -9.5 | 0.132900 |

**R1. Original prediction.** Literal rows above; the record's own trigger rows: TOP_SIDE Pacers +7.5 (0.635445) WIN; TOP_TOTAL Over 219.5 (0.512970) LOSS; RANK1 Pacers +7.5 (0.635445) WIN. No primary p_card was issued (chat-local, no repository reference or freeze).
**R2. Final event.** Indiana 106-104 New York; Quarter line not in permitted text; Knicks scored 20 in Q4 and topped 27 only in Q3 (SI); no OT indicated. Identity matched on teams/players, date and competition (NBA 2026-27, Emirates NBA Cup East Group B (game 0022600034)).
**R3. Contract settlement.** Arithmetic per row above; half-point lines cannot push. Basketball rows include overtime (BK-OT-1); none occurred.
**R4. Rank diagnostics.** 2W/2L/0U over 4 literal rows; zero primary rows; zero prospective rows.
**R5. Winner call.** Any winner statement in the core is retained unchanged; graded only where it is a literal row above.
**R6. Line assessment.** Final Knicks minus Pacers = -2; total 210. Signed distances in the arithmetic column; no prices or odds used.
**R7. Expected versus realised.** Where the record printed a centre or distribution it is retained in the core; no new distribution is constructed. Calibrated PIT NOT_ASSESSABLE (uncalibrated chat scenario outputs).
**R8. What decided it.** Indiana, without Haliburton, won 106-104; Towns missed a tying jumper at the buzzer (search summary, not an opened page). Knicks -7.5 lost by 9.5 points; the 210 total was 9.5 under 219.5.
**R9. Source/timing review.** Settlement sources: https://www.si.com/nba/pacers/onsi/pacers-defeat-knicks-in-nba-cup-thriller-01m7bmcnjg37 (ALLOWED); https://www.talkbasket.net/228011-pacers-survive-defending-champions-knicks-106-104 (ALLOWED). Card timing `POST_SCHEDULED_START_WRITE`; self-declared phase labels: POST_SCHEDULED_START;TIMING_UNVERIFIED. No pre-start freeze exists, so no clean-prospective claim is possible.
**R10. Classification.** RESEARCH_ONLY / NOT_ISSUED / ANALYST_NOT_PRIMARY; INFORMATION_INCOMPLETE (no reference stage, source-audit receipts, confirmed lineups or learning log).
**R11. Hypothesis.** PROPOSED_NOT_TESTED, see AUDIT_REPORT §6; one result changes no rule.
**R12. Disposition.** Diagnostic grades retained for prompt 6; no model bundle, so expert feedback NOT_APPLICABLE_NO_MODEL; no learning log was initialised pregame, so none is built after the result (LEARNLOG-v1). Terminal target in TERMINAL_TARGETS.csv.
<!-- END SETTLEMENT LOCAL-202611128358B025-G0011 revision-1 -->

`LOCAL-20261112D3C239297F-G0011`: MISSING_ORIGINAL (script/JSON `nba_knicks_pacers_scenario_20261114.*` only). Not graded.

### Deep loss reviews (DEEPLOSS-v1)

#### Deep loss review · New York Knicks @ Indiana Pacers · Knicks -7.5

**1. Exact frozen claim.** `Knicks -7.5`, full-game endpoint as each record defined it. Triggered in 1 record(s):

| Record | Trigger role(s) | Original p (basis) | Brier | Log loss |
|---|---|---|---:|---:|
| `LOCAL-20261112EE4AFA68-G0011` | TOP_SIDE | NOT_ESTIMATED (QUALITATIVE) |  |  |

No record carried a primary p_card, frozen reference or same-row baseline; BASELINE_P comparison NOT_COMPUTABLE.

**2. Verified outcome.** Indiana 106-104 New York (Quarter line not in permitted text; Knicks scored 20 in Q4 and topped 27 only in Q3 (SI); no OT indicated). team margin -2 with handicap -7.5: cover by -9.5. Sources in R9; evidence C; final wall-clock NOT_VERIFIED.
**3. Distribution check.** Every triggering record was qualitative (NOT_ESTIMATED), so there is no frozen distribution to place the result in. Percentile placement inside each record's printed score object is not reconstructed; the printed objects stay in the cores.
**4. Error decomposition.** Realised line distance: team margin -2 with handicap -7.5: cover by -9.5. No record had a calibrated centre or a measured effect-table row, so the miss cannot be split into reference error and adjustment error; no blame shares are invented.
**5. Research audit.** Haliburton OUT: TRUE (game reports confirm). Knicks three games in four nights: TRUE per schedule. Facts not re-opened here remain UNVERIFIED_AT_CUTOFF; no source in any card carries a captured retrieval receipt (chat-local research).
**6. What decided the game.** Indiana, without Haliburton, won 106-104; Towns missed a tying jumper at the buzzer (search summary, not an opened page). Knicks -7.5 lost by 9.5 points; the 210 total was 9.5 under 219.5.
**7. Knowable at cutoff?** The fatigue and road factors were printed as kill paths. The final score and its timing were not knowable.
**8. Process audit.** Chat-local record; no repository reference stage, no source-audit receipts, no lineup confirmation, no freeze. Timing per record in CARD_TIMING.csv (several written after the scheduled start). Endpoint and contract definitions were correct.
**9. Verdict.** The card ranked it secondary and not 'safer'; Indiana won outright. 8358's 63.5% Pacers +7.5 was the better-supported side.
**10. Cutoff-only counterfactual.** NOT_ESTIMATED: no knowable fact has a measured effect-table row, so no corrected probability is priced after the result.
**11. Failure class and recurrence.** Shared across 1 record(s) on one game: the parallel chats used overlapping public inputs, so their losses are one dependent observation, not 1 independent ones.
**12. Correction.** NO_CHANGE to any rule from one result. Procedure proposals are in AUDIT_REPORT §6 (PROPOSED_NOT_TESTED).
**13. Matched wins.** `LOCAL-20261112EE4AFA68-G0011` RANK1 Under 219.5 WIN; `LOCAL-20261112EE4AFA68-G0011` TOP_TOTAL Under 219.5 WIN. These rest on the same unvalidated construction and do not show the process worked.
**14. Honesty.** Original numbers and labels preserved; no luck claim without the arithmetic above; no invented percentages, operator terms or publication times. Preservation PASS; information closure INCOMPLETE.

#### Deep loss review · New York Knicks @ Indiana Pacers · Over 219.5

**1. Exact frozen claim.** `Over 219.5`, full-game endpoint as each record defined it. Triggered in 1 record(s):

| Record | Trigger role(s) | Original p (basis) | Brier | Log loss |
|---|---|---|---:|---:|
| `LOCAL-202611128358B025-G0011` | TOP_TOTAL | 0.512970 (SCENARIO_CENTRAL) | 0.263138 | 0.719430 |

No record carried a primary p_card, frozen reference or same-row baseline; BASELINE_P comparison NOT_COMPUTABLE.

**2. Verified outcome.** Indiana 106-104 New York (Quarter line not in permitted text; Knicks scored 20 in Q4 and topped 27 only in Q3 (SI); no OT indicated). total 210 vs 219.5: -9.5. Sources in R9; evidence C; final wall-clock NOT_VERIFIED.
**3. Distribution check.** Numeric records priced this row at 0.513-0.513 (mean 0.513); a loss at those prices is a 49%-49% event under each record's own uncalibrated object. Percentile placement inside each record's printed score object is not reconstructed; the printed objects stay in the cores.
**4. Error decomposition.** Realised line distance: total 210 vs 219.5: -9.5. No record had a calibrated centre or a measured effect-table row, so the miss cannot be split into reference error and adjustment error; no blame shares are invented.
**5. Research audit.** Pacers 225.6 season combined: as cited. Facts not re-opened here remain UNVERIFIED_AT_CUTOFF; no source in any card carries a captured retrieval receipt (chat-local research).
**6. What decided the game.** Indiana, without Haliburton, won 106-104; Towns missed a tying jumper at the buzzer (search summary, not an opened page). Knicks -7.5 lost by 9.5 points; the 210 total was 9.5 under 219.5.
**7. Knowable at cutoff?** Knicks' 214.5 L10 combined was printed. The final score and its timing were not knowable.
**8. Process audit.** Chat-local record; no repository reference stage, no source-audit receipts, no lineup confirmation, no freeze. Timing per record in CARD_TIMING.csv (several written after the scheduled start). Endpoint and contract definitions were correct.
**9. Verdict.** A 51.3% coin flip ranked second by 8358; lost by 9.5 points. Should not be presented as a direction.
**10. Cutoff-only counterfactual.** NOT_ESTIMATED: no knowable fact has a measured effect-table row, so no corrected probability is priced after the result.
**11. Failure class and recurrence.** Shared across 1 record(s) on one game: the parallel chats used overlapping public inputs, so their losses are one dependent observation, not 1 independent ones.
**12. Correction.** NO_CHANGE to any rule from one result. Procedure proposals are in AUDIT_REPORT §6 (PROPOSED_NOT_TESTED).
**13. Matched wins.** `LOCAL-202611128358B025-G0011` RANK1 Pacers +7.5 WIN; `LOCAL-202611128358B025-G0011` TOP_SIDE Pacers +7.5 WIN. These rest on the same unvalidated construction and do not show the process worked.
**14. Honesty.** Original numbers and labels preserved; no luck claim without the arithmetic above; no invented percentages, operator terms or publication times. Preservation PASS; information closure INCOMPLETE.

<!-- END SETTLEMENT EVENT E21 revision-1 -->

## Diagnostics (MINI_SETTLEMENT review level; descriptive only)

- Literal rows: 277: 131 WIN, 142 LOSS, 3 UNRESOLVED (Urawa–Cerezo corners), 1 no-direction record. **Primary rows: 0.**
- Numeric diagnostic rows: 206; mean Brier 0.2594 (a constant 0.5 forecast scores 0.2500 on any row). Rows within a record are complementary pairs and records on one game share inputs, so these are dependent and descriptive only.
- Rank-1 / stated first lean by source (W-L): 202611128358B025 6-5; 20261112CC53B5C806 6-3; 20261112CHAT17C8C881 4-5; 20261112CHAT9538BF5E 3-7; 20261112D3C239297F 5-3; 20261112EE4AFA68 6-5; R3NEXT-A 2-7; R3NEXT-B 3-7.
- Paired experiment eligibility (ASSESS-100): **0 eligible fully settled paired games** from this drop; no record has a frozen SINGLE/FIVE comparator or manifest (EXT-v3 not used).

**MINI_SETTLEMENT review row (for prompt 6):** `2026-11-14,MINI_SETTLEMENT,OWNER_DROP_2026-11-14,DATA_REPAIR_REQUIRED,90 chat-local records on 21 games; zero primary; timing/freeze/source-audit gaps; see AUDIT_REPORT.md`

## UNRESOLVED_CARRYOVER

| Key | Item | Next source / action | Responsible | Status |
|---|---|---|---|---|
| Urawa–Cerezo corners (3 rows) | Combined corner kicks | J.League match stats page (stats table not in fetched text); a second permitted provider | owner / repository agent on request | UNRESOLVED, NOT_SCHEDULED |
| D3C239297F G0009-G0011 | Missing card text | Owner to supply the 300,547-byte final mini | owner | MISSING_ORIGINAL |
| All 21 events | Final wall-clock time; actual first play | Official play-by-play / match centres | – | NOT_VERIFIED, retained |
| E14, E18, E21, R01, R06 | Second permitted lineage | Field-owner box score from a permitted host | – | Evidence C, grades unaffected |

## SETTLEMENT_MANIFEST

Records settled: 90 (58 chat cards, 30 R3NEXT strand records, 2 identity-conflict notes). Events: 21, all terminal. Missing originals: 3. Deep loss review groups: 33. Sidecars: FROZEN_SOURCE.csv, MASTER_GRADES.csv, EFFECTIVE_SETTLEMENT_ROWS.csv, CARD_TIMING.csv, EVENT_FINALS.csv, TERMINAL_TARGETS.csv, SOURCE_DISCOVERY_REGISTER.csv, SOURCE_SEARCH_ATTEMPTS.csv, REQUIREMENT_CLOSURE.csv, SOURCE_ACCESS_AUDIT_*.csv, SETTLEMENT_CHECKS.csv.
