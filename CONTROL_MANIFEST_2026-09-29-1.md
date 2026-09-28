# Control manifest - 2026-09-29-1

Method: **MDS-2026.09.28-v5.1 (md-only)**
Control revision: **CR-2026.09.29-MD7**
Category: **USER_INSTRUCTED_CUSTODY plus RETRIEVAL** (log consolidation close-out; source, fallback and official-social lanes)
Status: **CURRENT, as selected by METHOD.md**

This supersedes the active pointer to manifest `2026-09-28-9`. That manifest no longer verifies, because nine files were edited after it was written during the P-523 correction; it is kept, and hashed below, as history. Cards frozen under an earlier manifest keep it.
- No issued probability, rank, contract, scoring rule or game result changed.
- `prediction logs/` contains exactly six combined logs. Parts 1-5 hold canonical history through P-517. Part 6 is the active part: P-518 to P-522 are reserved (their original source block is quarantined), and new cards run from P-523 in issue order until the user directs a new part.
- This manifest excludes itself, the living status register `GAME_LOG_STATUS_CURRENT.md`, active Part 6 and the living execution note `VERIFICATION_RECEIPT_2026-09-28.md`. The original source block in Part 6 has its own raw-byte SHA check.

**Normalization.** For each listed file:
1. decode UTF-8, with an optional BOM;
2. convert CRLF and CR to LF;
3. encode UTF-8 with every LF converted to CRLF;
4. hash those normalized bytes with SHA-256.

| File | Normalized SHA-256 | Normalized bytes |
|---|---|---:|
| `BASE_RATES_REGISTER.md` | `f9df00b888606a14e843342c5237e675247d3028411f94aeca4a4da852ef24ae` | 36415 |
| `CARD_AND_LOG_TEMPLATES.md` | `89c4ca8a8b4a79c3a1b500fd45c75fb301d3d38b2c9adf8dd0b1ed843beaccd6` | 19966 |
| `CHANGELOG.md` | `91f02310ce8b9ee17a62acdc119dd1d6fa261941996c0b656981f5446650b1d2` | 59454 |
| `CONTRIBUTING.md` | `bac7a3ba9e228762d3eff57b253b5191195bfe6eb2cab8bd06885cd7dbe4401a` | 2044 |
| `CONTROL_MANIFEST_2026-09-28-4.md` | `533af3b585c5a1d766d6adcee4cfc3f660abc3720a6d3727c8a5f6a5a6df3be7` | 20033 |
| `CONTROL_MANIFEST_2026-09-28-5.md` | `77eed529422a0d4ff3132ce256c934d22cc2ae13b9f448463d97fc27b097e40a` | 4692 |
| `CONTROL_MANIFEST_2026-09-28-6.md` | `f74d0369cd91770c54ee32a9c548467023ee19fa3cd2de26114795c6ef26b392` | 7381 |
| `CONTROL_MANIFEST_2026-09-28-7.md` | `a25f89fa04ef02d80e985f3f9f3a829a2a2780922923de9cfbabc339bb6df969` | 7943 |
| `CONTROL_MANIFEST_2026-09-28-8.md` | `6dc64b2d74178335b76dc8180983a8d51b104c1cbe50f463148927d675bf6a0f` | 7845 |
| `CONTROL_MANIFEST_2026-09-28-9.md` | `ee7a8ee9481eb6a8c8085bb4fcde9e55560f163f5ec78af11259a7cd55f0e7b0` | 6535 |
| `CURRENT_RULES.md` | `28397d5941338dc6e1334237df1e890a4a175feca60021fab07e959a1aba7c77` | 41353 |
| `HISTORICAL_LINK_INDEX.md` | `d88da53952d78ee205d7511e2be20f474ab83acc627bf1d8f3a6860738426ab9` | 68536 |
| `LEAGUE_RULES_CRICKET.md` | `4c73d2b33e460b0bca3bf992dd706531cc5e93238ea0b2be2fbdfc78ed28beec` | 26610 |
| `LEAGUE_RULES_SOCCER.md` | `2fb2db93e7a1369884ae74e8a71c633cb70f347c8142cc1a4b4306f5183a454c` | 44093 |
| `LEARNING_REGISTER.md` | `9a4917c69740f75e73529d2b9263301bf88140579237d0f1044e39d2ffd7d369` | 348190 |
| `LEARNINGS_INDEX.md` | `c953ee180e34c2f834446409d9faae5e0a415eaa68e70c93b4c83caeac515a50` | 43203 |
| `LICENSE.md` | `1efb20731adc03fb046120ceeceb7f4e0ca0d73b2eb2d5fcf2093350863161b8` | 1211 |
| `MARKET_BENCHMARK_LEDGER.md` | `d886b11c3fef4aec742749d4e41a4926a36345abab51240693d9b6482e1f9b1c` | 3883 |
| `METHOD.md` | `088407057270bd5c99bb4ff3318daeb86c7fa7a2f23035c8eda9984322a54399` | 5698 |
| `P518_P522_RECONCILIATION.md` | `f9df7b57af68958c64568f28b86b6f18bed793c81bb34863fb16fb68630b3912` | 7581 |
| `prediction logs/PREDICTION_LOG_COMBINED.md` | `9b6f07a5ccd5c10209e5c7701b9698ed71eaab6aecbf156af36d8fffe7efaf81` | 4139536 |
| `prediction logs/PREDICTION_LOG_COMBINED_2.md` | `b63569d6ff05b42f4cc9ef49f6e5f723e11eefdb554928b8ec2af98587f22c64` | 565262 |
| `prediction logs/PREDICTION_LOG_COMBINED_3.md` | `aabfc9f9c155f4752c92129611332a6f2cb8e747564d86c8835ad685157fbf6c` | 419639 |
| `prediction logs/PREDICTION_LOG_COMBINED_4.md` | `91216b87bdd8c0786240ffbb3fdc3fd338703598d0731fa2fc16a21b5a26b14e` | 854587 |
| `prediction logs/PREDICTION_LOG_COMBINED_5.md` | `29a627d17b5bea00f0bf65e038bf421c3353deae53834d870ab72531a548896d` | 1058646 |
| `PROBABILITY_TOOLKIT.md` | `c6fe84a9243251881b2468791d7d0c0d42612d4f799c64d19b826f22a97e834b` | 50453 |
| `PROMPTS.md` | `316b03a26abf7a17769f379f93d87824fee9a746d677b1e597db895b925dee7a` | 17899 |
| `README.md` | `3d7631e2833412ec7be033309669a5203bfbcd0fce154cabd50fd41aedd1f609` | 7614 |
| `RECORD_ELIGIBILITY_SCHEMA.md` | `79502cb1134fc47fc0a8e95d59b74a8a08a6fe6aa5e7118d1a0b10074e51a3b9` | 6090 |
| `RULES_AFL.md` | `0d484bd98f94931a5b943a7745c6986b4053d851e009295c21232eed17982193` | 37979 |
| `RULES_AMERICAN_FOOTBALL.md` | `ee4875832616051320043e0f5ca784f0962721eea66dcdaa8309921009e400f2` | 43972 |
| `RULES_BASEBALL.md` | `e055da0b26e65e2813ebfc46aed261449c80b3af7c401fbb64db7547d4ed87ef` | 63198 |
| `RULES_BASKETBALL.md` | `b3b40e51a9395fc9ec7a3e2792cb41d703caf5f2badc70777f37eb9de1d2a183` | 48564 |
| `RULES_CRICKET.md` | `e88fecaceb1f3ac1037de4d2e8920a8c050769429cfbbcc7d1d9e9b718b02844` | 57700 |
| `RULES_ICE_HOCKEY.md` | `dd98dbbea86b84f80b6a4a76ed128d14cb01f17723d40cb4692827d538921af3` | 36832 |
| `RULES_NRL_RUGBY.md` | `98384bcf5c343d1b17b30c3b01d7e24e59ccddb489660dcc7531869e48fd78fc` | 35430 |
| `RULES_RUGBY_UNION.md` | `bb98d55c354d69438ff9967e3d6061c1b8187f25be7bf09ebb580f9c7884378d` | 34655 |
| `RULES_SOCCER.md` | `88698b4e478a34677baddb7af6efae6881ab6d171839c14364362e36bbd96def` | 43023 |
| `RULES_TENNIS.md` | `8ce618e5ddc029a3743767aa77294cb0aff67d8a5cbbebf9daf7da010aa3e865` | 44073 |
| `SCORING_AND_VALIDATION.md` | `2402fff6be49de519db24a2a96db2f4b2d5c176a5a66abd7a30380b13dd34bab` | 28584 |
| `SKILL_BASELINE_LEDGER.md` | `fa12e9c8d1a0b7ab9814ff6905ab973121a8c3606aedffaabbda45fceb9c1636` | 12491 |
| `SOURCES.md` | `39a3e6c4ddbdc589195d5429a01239640a43902c51da26d1aa3fdceca799ec15` | 71101 |
| `VALIDATION_EVIDENCE.md` | `986f353d216aefd2221058c8aea927f3d9b2dc3c92dcc03cdbde41345cfe997a` | 50646 |
| `VERIFICATION_PROTOCOL.md` | `26c9b6041166ac56b9630a8f8f51511d61e633dfccb4085be24bd470d05ad013` | 6790 |

**Listed files:** 44. Verify every normalized hash and size above. `METHOD.md` points here, and this manifest's own normalized SHA-256 is in the first line of `GAME_LOG_STATUS_CURRENT.md`. The embedded original P-518 onward source block in Part 6 must remain exactly 141,740 bytes with raw SHA-256 `c4d497bf339010eae2ff5df23a2d76290983585671666e74791618342565cf30`.
