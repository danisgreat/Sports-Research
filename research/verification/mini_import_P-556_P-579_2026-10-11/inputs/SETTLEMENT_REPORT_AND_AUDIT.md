# Settlement report and self-audit — P-572 to P-579

**Reading receipt:** Repository `danisgreat/Sports-Research` main HEAD `33d0ea0c1c70056db7c7fb0a07dec77a633e573f` read 2026-10-11 AEDT; METHOD; CURRENT_RULES §§2,3,5,8; SELECTION_RULES §§7-8; SCORING_AND_VALIDATION §2,6; CARD_AND_LOG_TEMPLATES §§6,9 and §3a; EXAMPLE_SETTLED_MINI; CURRENT_STATE; GAME_LOG_STATUS_CURRENT; RULES_BASEBALL §0; RULES_BASKETBALL §0; SOURCES §§3.1,3.2; ARCHIVE_USE_GUIDE §6; frozen master and P-578 A8 read fully from local artifacts.

- Created: 2026-10-11T21:58:06+11:00; frozen original `PREDICTION_MASTER_RUNNING_LOG_P-556_TO_P-579.md` size 593775 bytes, 3988 lines, SHA256 `3a406f539b43c982d1bfa8274d18be0d0670e73a59b10944ab6d90c5d48cc875`.
- Original master contains 24 unique event IDs P-556–P-579, including original P-578 A8, and 15 local settlements P-557–P-571; P-556 is already canonical/settled. New appendix covers P-572–P-579.
- Terminal **settled** P-572–P-576 (5); **PENDING_EVENT** P-577–P-579 (3); no renumbering; next working P-580.
- New batch grades: WIN 17; LOSS 3; PUSH 0; VOID 0. Evidence A 8, B 4, C 8, E 0, OP 0, X 0. (P-572/573 MyKBO each C; P-574/576 B.LEAGUE each A; P-575 RealGM/NBL B.)
- Top-two only: 9/10 = 90.0% (Rank1 4/5; Rank2 5/5); cards TOP2_ALL_WON 4; TOP2_SPLIT 1; ALL_LOST 0; Hit@2 5/5; mean NDCG@2 0.8774; winner calls 2/5.
- Deep retrospection: P-576 Rank1 LOSS, `OVERCONFIDENT_PROBABILITY`.
- Archive agreement: 0 current-year matched archive rows; 5 unverified in archive (2026 league files absent/header-only).
- SLA: five games settled within 72h of their Oct11 event. Active carryover 3 ≤5.
- Forecast process: all five deficient in lineup/bench confirmation and/or calibration. These are retrospective deficiencies under the prospective rule, not changes to issued card.
- **New lineup gate** forward-looking only; GitHub/Combined Log/canonical ledger not changed.

## Five-settlement outcome table

| ID | Terminal result | Rank1 | Rank2 | Rank3 | Rank4 | Winner call | Evidence |
|---|---|---|---|---|---|---|---|
| P-572 | KT Wiz 12–3 Samsung Lions | WIN | WIN | LOSS | WIN | CORRECT | C |
| P-573 | Lotte Giants 4–1 KIA Tigers | WIN | WIN | LOSS | WIN | INCORRECT | C |
| P-574 | Kyoto Hannaryz 81–89 SeaHorses Mikawa | WIN | WIN | WIN | WIN | CORRECT | A |
| P-575 | Illawarra Hawks 100–110 Cairns Taipans | WIN | WIN | WIN | WIN | INCORRECT | B |
| P-576 | Tokyo Sunrockers 68–70 Sendai 89ers | LOSS | WIN | WIN | WIN | INCORRECT | A |

## S1–S14 self-audit

| Check | Result | Evidence |
|---|---|---|
| S1 | PASS | Cards P-557–P-579 one occurrence each; P-556 standalone canonical reference; exactly one settlement per P-557–P-579 incl pending |
| S2 | PASS | Output begins with frozen input exact byte-for-byte; SHA256 and size recorded |
| S3 | PASS | Four issued literal propositions and original p_card copied from card for all new five settlements, script asserts equality |
| S4 | PASS | 17 wins 3 losses; Rank1 4 W 1 L; Rank2 5 W; only ranks1/2 counted |
| S5 | PASS with evidence limit | KBO single structured MyKBO Final evidence C; B.LEAGUE exact-owner Final A; RealGM structured NBL Final + NBL owner match B; timestamps and URLs included in every Basis |
| S6 | PASS | R1–R12 present for each newly settled event; R1 sourced from its own original card |
| S7 | PASS | Only P-576 Rank1 lost; exactly eight deep-retrospective parts and valid failure class |
| S8 | PASS | Full sporting endpoints used; no cancellation/retirement found; no operator terms invented; no OP needed |
| S9 | PASS | P-577–P-579 unverified as terminal; only those kept PENDING_EVENT, matching carryover list |
| S10 | PASS | Open carryover 3; final dates all 2026-10-11, settled within 72h |
| S11 | PASS | Process: DEFICIENT explicitly in R9/R10, lineup/bench gates/timing/calibration reviewed separately from grades |
| S12 | PASS with archive limitations | Required repo authority read; prior/2026 archives for these leagues absent/header-only, no fabricated comparison |
| S13 | PASS | No GitHub, Combined Prediction Log or canonical ledger write |
| S14 | PASS | Per-card expected-score means and SDs copied from original and error/z computed from actual outcomes; none changed |

**Important limitation:** P-577–P-579 have not been settled solely because a verified terminal result was not established at the above check, not because the scheduled start is in the future. They should be rechecked on the next live update; do not recast them as permanently unsettled.
