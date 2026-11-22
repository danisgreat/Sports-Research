# Canonical import · 22 November 2026 · P-686 to P-696 (20261118DA6D9F6251746B979F5895FA)

Prompt 3→4 (P-2026.11.18-v29.1 · CANONICAL_IMPORT · LOCAL_WORKING_TREE) on GitHub mini `20261118DA6D9F6251746B979F5895FA` pulled from `origin/forecast-seals` and `origin/card-drops`. Import time `2026-11-22T06:40:00+00:00` (`2026-11-22T17:40:00+11:00`). Archived byte-exact at `archive/settled_minis_2026-11-22/20261118DA6D9F6251746B979F5895FA/`.

## Assigned IDs (P-686 to P-696)

| ID | Scheduled start (UTC) | Card key | Seal | Final | Rank 1 | Rank 2 | Card d |
|---|---|---|---|---|---|---|---:|
| **P-686** | 2026-11-18 01:00 | `20261118DA6D9F6251746B979F5895FA-G0001` | UNSEALED | Minnesota Timberwolves 106-105 Portland Trail Blazers | L1 AWAY 4.5 (WIN) | L2 UNDER 225.5 (WIN) | +0.0350 |
| **P-687** | 2026-11-18 02:00 | `20261118DA6D9F6251746B979F5895FA-G0002` | SEALED | Tennessee 61-46 Michigan State | L1 AWAY -2.5 (LOSS) | L2 OVER 149.5 (LOSS) | -0.0345 |
| **P-688** | 2026-11-18 10:05 | `20261118DA6D9F6251746B979F5895FA-G0003` | SEALED | Chiba Jets 89-84 Akita Northern Happinets | L1 AWAY 8.5 (WIN) | L2 OVER 180.5 (LOSS) | +0.0159 |
| **P-689** | 2026-11-19 00:00 | `20261118DA6D9F6251746B979F5895FA-G0005` | SEALED | Rochester Americans 2-1 Syracuse Crunch (Regulation) | L1 AWAY -0.5 (WIN) | L2 AWAY 0.5 (WIN) | +0.0372 |
| **P-690** | 2026-11-19 00:00 | `20261118DA6D9F6251746B979F5895FA-G0006` | SEALED | Houston Rockets 119-104 Indiana Pacers | L1 HOME 8.5 (LOSS) | L2 OVER 224.5 (LOSS) | -0.1136 |
| **P-691** | 2026-11-19 01:00 | `20261118DA6D9F6251746B979F5895FA-G0008` | SEALED | Atlanta Hawks 117-112 Oklahoma City Thunder | L1 AWAY 6.5 (WIN) | L2 OVER 228.5 (WIN) | +0.0550 |
| **P-692** | 2026-11-19 01:00 | `20261118DA6D9F6251746B979F5895FA-G0009` | SEALED | Detroit Pistons 122-109 New Orleans Pelicans | L1 AWAY 3.5 (WIN) | L2 OVER 224.5 (WIN) | +0.1818 |
| **P-693** | 2026-11-19 01:30 | `20261118DA6D9F6251746B979F5895FA-G0010` | SEALED | Samford 74-64 USC Upstate | L1 HOME 8.5 (LOSS) | L2 OVER 150.5 (LOSS) | -0.1685 |
| **P-694** | 2026-11-19 03:00 | `20261118DA6D9F6251746B979F5895FA-G0011` | SEALED | Utah Jazz 109-97 Los Angeles Lakers | L1 AWAY 11.5 (WIN) | L2 OVER 229.5 (LOSS) | +0.0220 |
| **P-695** | 2026-11-19 08:30 | `20261118DA6D9F6251746B979F5895FA-G0012` | SEALED | Illawarra Hawks 103-97 Adelaide 36ers | L2 OVER 196.5 (WIN) | L1 HOME 4.5 (WIN) | +0.0295 |
| **P-696** | 2026-11-20 08:10 | `20261118DA6D9F6251746B979F5895FA-G0013` | SEALED | Melbourne Renegades W 165/4 (20 ov; 32/1 after 6 ov); Adelaide Strikers W 168/5 (19.5 ov) | L2 UNDER 42.5 (WIN) | L1 UNDER 157.5 (LOSS) | +0.0261 |

- **Non-card keys accounted for (0 IDs consumed):** `20261118DA6D9F6251746B979F5895FA-G0004` (unregistered AHL draft replaced by G0005) and `20261118DA6D9F6251746B979F5895FA-G0007` (`NBA:0022600258`, registered request with no card dropped — `NO_FORECAST`).
- **Canonical continuity:** Highest ID before **P-685**; after **P-696**; next **P-697**. Reserved **P-518–P-522** untouched.

## Custody and readback

- `prediction logs/PREDICTION_LOG_COMBINED_11.md` before: **22,101 B**, SHA-256 `b0ea1474d58d8bfd7027380f2562c39eb4f383dd0c4fc6dca67d7335d2ca2d1f`.
- Appended: **188,066 B** (11 canonical wrappers + 11 settlement addenda).
- `prediction logs/PREDICTION_LOG_COMBINED_11.md` after: **210,167 B**, SHA-256 `708eccd576ca77053c1a3124c412d1ba1e819bc57cea770263d1c2108c84df34`. Prefix byte-identical.
- [CANONICAL_READBACK.csv](CANONICAL_READBACK.csv): **22/22** blocks verified byte-exact after the prefix.
- **Deep loss register:** 10 new reviews (`DLR-2026-11-22-001`..`DLR-2026-11-22-010`) appended to `research/deep_loss/DEEP_LOSS_REGISTER.csv`.

## Training handoff (`CARD-TRAIN-v1`) & Track P (`ONE-CHAT-v3`)

- `python -m ml card-training run --out research/card_training/2026-11-22-1` ingests the updated effective history (`P-001`–`P-696`) as an exploratory study (`ML-SEP-v1`).
- Official `ONE-CHAT-v3` intake saved to `research/one_chat/intake/2026-11-22-1` and captured outcomes to `research/one_chat/outcomes/2026-11-22-1/OUTCOMES.csv`. No predictive advantage is certified.
