# Unresolved after import — 2026-10-11

Open sporting carryover: **3** (cap 5). Each is now a canonical card in Combined Log 7 with no settlement. The next mini carries each one as a `CARRYOVER` block under its canonical ID and settles it within 72 hours of its final (CURRENT_RULES §8; CARD_AND_LOG_TEMPLATES §2). The P-578 A8 addendum is already canonical under P-578; the original card is what gets graded.

| ID | Event | Event key | Why not settled (from UNRESOLVED_CARRYOVER.md) |
|---|---|---|---|
| P-577 | TENNIS / ATP Shanghai Masters — Alexander Bublik vs Brandon Nakashima — 2026-10-11 | `ATP-SHANGHAI:2026:GRANDSTAND2-BUBLIK-NAKASHIMA-R32:2026-10-11` | Estimated 19:30 AEDT, fourth match on court; no verified terminal set score at the 21:58 AEDT check |
| P-578 | BASKETBALL / NBA Preseason — Dallas Mavericks @ Houston Rockets — 2026-10-11 | `NBA_PRESEASON:2026-27:0012600016:2026-10-11` | Scheduled 21:00 AEDT, start reported delayed; no terminal NBA box score at the check |
| P-579 | BASKETBALL / Liga ACB — La Laguna Tenerife @ UCAM Murcia — 2026-10-11 | `ACB:2026-27:UCAM-LLT-20261011:2026-10-11` | Scheduled 21:30 AEDT; official ACB schedule showed no terminal result at the check |

Other open items (process, not sporting):

- Part 7 header line 10 (P-549 / P-550) disagrees with CURRENT_STATE (P-579 / P-580). Pre-existing; needs a decision on the header convention (prompt 8) or a rollover whose new header states the current IDs (prompt 5).
- `SPORTS_RESEARCH_PRESTART_LINEUP_AND_BENCH_RULE.md` (`PRESTART-XI-BENCH-2026-10-11`) is a proposed rule stored in `inputs/` only. It is not adopted; adopting it is a rule change under CURRENT_RULES §11.
