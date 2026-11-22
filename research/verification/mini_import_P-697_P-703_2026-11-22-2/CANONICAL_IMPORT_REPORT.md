# Canonical import · 23 November 2026 · P-697 to P-703 (20261120-495CEEB69E9540938CF6A7DAA7B546B4)

Prompt 3→4 (P-2026.11.22-v29.2 · CANONICAL_IMPORT · LOCAL_WORKING_TREE) on GitHub mini `20261120-495CEEB69E9540938CF6A7DAA7B546B4`, pulled from `origin/forecast-seals` and `origin/card-drops`. Import time `2026-11-22T20:00:00+00:00` (`2026-11-23T07:00:00+11:00`). Archived byte-exact at [archive/settled_minis_2026-11-22/20261120-495CEEB69E9540938CF6A7DAA7B546B4/](../../../archive/settled_minis_2026-11-22/20261120-495CEEB69E9540938CF6A7DAA7B546B4/README.md).

## Assigned IDs (P-697 to P-703)

| ID | Scheduled start (UTC) | Card key | Seal | Final | Rank 1 | Rank 2 | Card d |
|---|---|---|---|---|---|---|---:|
| **P-697** | 2026-11-20 11:10 | `…-G0001` | SEALED | Beer Sheva/Dimona 90-80 Ness Ziona | Ness Ziona −7.5 (LOSS) | Over 169.5 (WIN) | −0.0068 |
| **P-698** | 2026-11-20 11:35 | `…-G0002` | UNSEALED | Beijing Guoan 0-2 Shanghai Port | 1H Over 0.5 (WIN) | Over 2.5 (LOSS) | +0.0501 |
| **P-699** | 2026-11-21 00:30 | `…-G0003` | SEALED | Cavaliers 128-119 Pacers | Under 234.5 (LOSS) | Pacers +5.5 (LOSS) | −0.0606 |
| **P-700** | 2026-11-22 00:00 | `…-G0004` | UNSEALED | Blue Jackets 4-3 Maple Leafs | Under 6.5 (LOSS) | Maple Leafs +0.5 (LOSS) | −0.0502 |
| **P-701** | 2026-11-22 06:00 | `…-G0005` | UNSEALED | Bullets 115-104 Kings | Bullets +4.5 (WIN) | Under 189.5 (LOSS) | +0.0114 |
| **P-702** | 2026-11-22 08:00 | `…-G0006` | UNSEALED | Aktobe U20 6-3 Torpedo U20 | Aktobe +4.5 (WIN) | Over 7.5 (WIN) | +0.1006 |
| **P-703** | 2026-11-22 08:10 | `…-G0007` | SEALED | Stars 159/7 (57/0 after 6) | Stars 6-over Under 41.5 (LOSS) | Stars 20-over Under 148.5 (LOSS) | −0.0431 |

Card keys are `20261120-495CEEB69E9540938CF6A7DAA7B546B4-G000n`. Ranks for refused cards are the registered rule computed on the card.

- **Canonical continuity:** highest ID before **P-696**; after **P-703**; next **P-704**. Reserved **P-518–P-522** untouched. No key in the mini is left without an ID.

## Custody and readback

- `prediction logs/PREDICTION_LOG_COMBINED_11.md` before: **210,167 B**, SHA-256 `708eccd576ca77053c1a3124c412d1ba1e819bc57cea770263d1c2108c84df34`, equal to the after-state recorded by the P-686–P-696 import.
- Appended: **135,432 B** (7 canonical wrappers holding the original card bytes, and 7 settlement addenda).
- After: **345,599 B**, SHA-256 `8e65cc64d0ab82dec8b5c88645450609cd3378af92694991e9beb8cac79cb5a3`. The prefix is byte-identical.
- [CANONICAL_READBACK.csv](CANONICAL_READBACK.csv): **14/14** blocks found byte-exact after the prefix.
- **Deep loss register:** 9 reviews (`DLR-2026-11-22-011` to `019`) appended to `research/deep_loss/DEEP_LOSS_REGISTER.csv`; `ml deep-loss` reports no register problems.

## Training handoff (CARD-TRAIN-v1) and Track P (ONE-CHAT-v3)

- `python -m ml card-training run --out research/card_training/2026-11-23-1` ingests the effective history P-001 to P-703 as an exploratory study (ML-SEP-v1). It is not applied to any card.
- Intake `research/one_chat/intake/2026-11-22-2` is built from every sealed card (13). It supersedes `2026-11-22-1` as the complete census, so score with it alone. Outcomes for the three sealed cards of this mini are in `research/one_chat/outcomes/2026-11-22-2/OUTCOMES.csv`. No game here is Track P-eligible: first play is unverified on all three sealed cards. No predictive advantage is certified.
