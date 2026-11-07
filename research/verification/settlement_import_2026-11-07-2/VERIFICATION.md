# Verification — P-616 BK-OT-1 import 2026-11-07

| Check | Result | Evidence |
|---|---|---|
| Frozen source unchanged | PASS | Q7N4 `ORIGINAL_MINI.md` 172,799 bytes `89146dbb…c85d` = 2026-10-21 receipt |
| Identity | PASS | 0 IDs consumed; one revision of existing P-616; unique key `P-616 2026-11-07-settlement-revision-2`; parent revision-1; no branch |
| Pre-mutation recheck | PASS | Part 9 15,961 bytes `502ac808…e591` = committed blob at `ef9eb9c74` |
| Append-only and readback | PASS | Prefix unchanged; core 3,101 bytes `701053e2…df3e` re-hashed at destination 16885–19986 ([IMPORT_READBACK.csv](IMPORT_READBACK.csv)); Part 8 untouched |
| Retained copy | PASS | `inputs/` copy = `research/active_minis/` document, 9,936 bytes `73c6a2f2…c03e` ([SOURCE_FILE_INVENTORY.csv](SOURCE_FILE_INVENTORY.csv)) |
| Grades | PASS | No grade changed; only P-616's definition status moved to `FROZEN_FRAMEWORK_CONVENTION` |
| Rule text consistent | PASS | BK-OT-1 wording appears in RULES_BASKETBALL (BK-P4 ×2, §0.5, §6, §8.3 BK-B8, controls 6 and 13), CORE, CURRENT_RULES and both basketball prompt files; no "operator endpoint" deferral is left in the live basketball rules |
| Hard rule (no prices) | PASS | No price, line or odds source used |
| Line endings | PASS | New files LF only |
