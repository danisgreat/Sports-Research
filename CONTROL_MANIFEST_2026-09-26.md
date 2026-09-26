# Control manifest — 2026-09-26 (review implementation: evidence before rules; a numerical model for every sport)

Method: **MDS-2026.09.19-v4.3**
Control revision: **CR-2026.09.21-3** (label unchanged; content receipt under the same label)
Status: **CURRENT post-write content receipt**, generated 2026-09-26 19:58 AEST by `tools/make_manifest.py` from `CONTROL_MANIFEST_2026-09-25-6.md`.

**Purpose.** This is the byte-level SHA-256 receipt that every new card freezes (`METHOD.md` header; PF-7). Implements the 2026-09-26 repository review (RULES_GENERAL.md §"2026-09-26" (a)–(j)): C-RULE-FREEZE, C-READING-GATE and the sport files' §0 live pages, C-EVENT-UNIVERSE, C-MARKET-BENCHMARK (post-settlement scoring only), C-MLB-SHADOW, the evidence-status tool, LEARNINGS_INDEX.md, the closed candidate backlog and the repository clean-up; (k) C-SPORT-SHADOW: reduced-feature A0/A1 models for every other sport (tools/sport_models.py, tools/sport_data.py) with their public-data validation (research/sport_models_2026-09-26/); and (l) blind shadow lanes for every sport including tennis and cricket, with the settlement record SHADOW: (audit 10s). Shadow models are never a card input. Regenerated in place before merge (2026-09-26(d), after an independent review); no card was issued under any earlier version of this file or under CONTROL_MANIFEST_2026-09-25-6.

**It does not change any forecasting coefficient, probability cap or ranking override.**

**Category (C-RULE-FREEZE):** MEASUREMENT.

This manifest is excluded from its own hash table. The living logs (`PREDICTION_LOG_COMBINED_5.md`, `GAME_LOG_STATUS_CURRENT.md`) are a write-time snapshot and change with every card. Hashes are taken in CRLF form (`tools/manifest_lib.py`); verify with `python tools/verify_manifest.py`.

**Changed since CONTROL_MANIFEST_2026-09-25-6.md (by bytes):** `README.md`, `METHOD.md`, `CONTROLS.md`, `RULES_GENERAL.md`, `UPCOMING_GAME_RESEARCH_GUIDE.md`, `SCORING_AND_VALIDATION.md`, `LEARNING_REGISTER.md`, `RULES_BASEBALL.md`, `RULES_CRICKET.md`, `RULES_SOCCER.md`, `RULES_BASKETBALL.md`, `RULES_AFL.md`, `RULES_NRL_RUGBY.md`, `RULES_RUGBY_UNION.md`, `RULES_AMERICAN_FOOTBALL.md`, `RULES_ICE_HOCKEY.md`, `RULES_TENNIS.md`, `audit_card_controls.py`, `test_audit_card_controls.py`, `NUMERICAL_PROGRAM.md`, `NUMERICAL_MODEL_REGISTER.md`, `MODEL_IMPLEMENTATION_RECIPES.md`, `CURRENT_RULES.md`, `CHANGELOG.md`, `CONTRIBUTING.md`, `SKILL_BASELINE_LEDGER.md`, `.gitignore`, `.github/workflows/checks.yml`, `tools/make_manifest.py`, `tools/repo_hygiene.py`, `tools/skill_baseline.py`, `tools/test_repo_tools.py`, `tools/test_skill_baseline.py`, `research/settled_rows_2026-09-25/README.md`, `research/rank_model_2026-09-25e/README.md`.

**New in the receipt:** `LEARNINGS_INDEX.md`, `MARKET_BENCHMARK_LEDGER.md`, `tools/slate_universe.py`, `tools/test_slate_universe.py`, `tools/market_benchmark.py`, `tools/test_market_benchmark.py`, `tools/evidence_status.py`, `tools/test_evidence_status.py`, `tools/mlb_model.py`, `tools/test_mlb_model.py`, `research/mlb_shadow/README.md`, `tools/sport_models.py`, `tools/sport_data.py`, `tools/test_sport_models.py`, `research/sport_shadow/README.md`, `research/sport_models_2026-09-26/README.md`, `research/sport_models_2026-09-26/validation_results.json`.

**Dropped:** none.

**Unchanged:** 68 files.

## SHA-256 file receipt

| File | SHA-256 | Bytes |
|---|---|---:|
| `README.md` | `9ce532df016c9d7de7cbe1fb18cbe5a3d34ec1d50ea87cb03a54573433e0e8c3` | 14292 |
| `METHOD.md` | `817e5e61aec60dd7788f0f26aa607986d3a464ff3fea1778075ab9cb34f8a7b6` | 31073 |
| `CONTROLS.md` | `50240aa1254b49141b864fe575f78d3ee5862074aa7c06fbfc6d89b8d2c6223c` | 42572 |
| `RULES_GENERAL.md` | `57f46ba309033bac8f286ef725499b8c8cabd636efbee2de9d2bc785d26313f2` | 285972 |
| `SOURCES.md` | `6e172c9fecf767af75da09d0f745e1428910795aa1e4e674a364b4b3af71faac` | 76886 |
| `DATA_SOURCE_REGISTER.md` | `898affe43d3490b83a2c8a888d88dc2b09cbdfe71024294ae79df9d32d17efef` | 178952 |
| `UPCOMING_GAME_RESEARCH_GUIDE.md` | `a3e7ed767257a7660c5c221cc23ffa6d4d3f3b332430c1ef5705427de445778f` | 76011 |
| `SCORING_AND_VALIDATION.md` | `64cb95cf3afcfd3f4d33f79bc34428aa82d095290810d64e9f62de929e806a22` | 23793 |
| `PERFORMANCE_ELIGIBILITY_POLICY.md` | `a102c231debc12253accf5ade0ed3086c7b51dcf3959e570129ad8b6d96dd2fa` | 19422 |
| `LEARNING_REGISTER.md` | `e08f6546394d9b87e2049e76b992e72e65d8de17cda2495e8afa860ad00bcf19` | 329664 |
| `AGENT_ROLE_AND_TASK.md` | `7ab4a2b52fa33a0cf9f9838926dda2acc6babc71fb1b99c3387873b0c15d52fb` | 25862 |
| `EXTERNAL_LOGGING_WORKFLOW.md` | `b724db948916f0bb4ae8847fcfd7fc278cf5db8fed8a2d04411507f5dcc1a6d8` | 68415 |
| `FORECAST_PREFLIGHT_MANIFEST.md` | `34718b2faca3276e7213bc622e01ff06998151390f5f7c3f12497082e7468678` | 9309 |
| `RULES_BASEBALL.md` | `cb9549d4bdb730a80f7141de7cf4a7d48bef0ed0f1402e73401de3f6b758762a` | 139544 |
| `RULES_CRICKET.md` | `82896597cfacaf04b2779ed3f2a5805dc8a65dd01f600d511c95ed3355066fe7` | 112985 |
| `RULES_SOCCER.md` | `c35fecedbd855f444d00d1c8a52f34893726b4ce800daaded0b73301c76d3a3b` | 111637 |
| `RULES_BASKETBALL.md` | `f86d5d456211ed4f1b2e88c874c2392e7fff6c06a7155934fd8bbd006b186c3d` | 107462 |
| `RULES_AFL.md` | `0f61b20d1c46ec8d34d5c083edeaa2b6cf39f2345651fe837032b1822a55ed8f` | 65706 |
| `RULES_NRL_RUGBY.md` | `02029fb588ec3e3c6c526b1048d6ffeaa225519a82831b42af8b8141166cc391` | 64224 |
| `RULES_RUGBY_UNION.md` | `24f3ed0bc16f720245fb7e94e95777a8171e7878dbbe1615c154d6a573faa833` | 54278 |
| `RULES_AMERICAN_FOOTBALL.md` | `5651e7330ed40c78fc686807bf9f600d81ece39f8ad00e4e6bfabcf0f71aabe1` | 69998 |
| `RULES_ICE_HOCKEY.md` | `ad728316a64c16b6a60c98a000e17251c95bb3ef1a9273146505cb888de1e8f2` | 61765 |
| `RULES_TENNIS.md` | `0fcf130aae5f04e7c7a1e612f99a6386bab9e53d7883fbfc7f27ba515075382d` | 77976 |
| `LEAGUE_RULES_CRICKET.md` | `b6b13dfa72047b62fd9987e21daa0ec25510ab0853ebbac461b5725de5f99099` | 26252 |
| `LEAGUE_RULES_SOCCER.md` | `236463054f21792ad091fd3f326c7cb12aac767c933ffc4bd2e265acf55df06b` | 43865 |
| `prediction_preflight.py` | `b4d07fef54e71ef8478c5b2cec3af15c5f5accf50ba3e703348ab16609006d26` | 29319 |
| `test_prediction_preflight.py` | `c91ef73ac3faa420e3b67f8e5f345a851c4f9a69e43e75c21be6d3c7a53d5d60` | 11403 |
| `audit_card_controls.py` | `c8f5b420e995c28dfbf1daaaf451801248c4f58182dbde2c1eebbb61d0ac9a69` | 35130 |
| `test_audit_card_controls.py` | `84da7061d82bc7cc063499c516298b0e3888356205b349ea26116bdfcba21693` | 17948 |
| `receipts.py` | `33c906e5b6a0f67ffaf103347f058955401923a3cb57ee43158cd7f2d1b3de30` | 21886 |
| `test_receipts.py` | `c841b495300f0e7e7afec7f4b24b1780c6a879b0067ed5b648a800625cee3c08` | 6502 |
| `H0_DATASET_CARD.md` | `a2d44c60788d0506c1108e1629fb2a2e6ac23d6fc41ca87c2e27a6d138152278` | 19413 |
| `NUMERICAL_PROGRAM.md` | `58b16f645172a3b94fae8ffe90af0e1d7f08606df6baa67745e6cc5a29429665` | 13037 |
| `NUMERICAL_MODEL_REGISTER.md` | `ae1c75d6a4c7d3f8a9f5639acf9813e2506c4aee07cbf14ee22353060dad7aa9` | 26413 |
| `NUMERICAL_TRAINING_SPEC.md` | `888fa925485a64642443b7555d8a989aea955d0a7997e23a09edef7db93bbd37` | 31309 |
| `MODEL_AND_DATA_SPEC.md` | `c4d77b5036afbe531387886ee460d35a47ba6d824bf5a13077f20d7c9906b771` | 64024 |
| `ALGORITHM_PORTFOLIO_AND_EVALUATION.md` | `c0dbea56b78a51c5f6a075d7e0ace6e0d84a4fe97a1366cd699624e5783f49aa` | 51138 |
| `MODEL_IMPLEMENTATION_RECIPES.md` | `7bb3ed44e2e51bf7361f57ddcfcbe22223637bc90d4932e6ba9081909ec5c42e` | 21136 |
| `RECENCY_AND_REBOUND.md` | `b35e9684ecb6d468b2570d6e429301cba567f8590e230bb3a46d42ffd4d93f37` | 18248 |
| `BASE_RATES_REGISTER.md` | `6789928df1e7bf55dd814c62d1b63fb50a19d52d60f728d16465608650b91c6b` | 31145 |
| `GAME_LOG_STATUS_CURRENT.md` | `7caff59e52c28eaa8326b1baaeaf85a45d970fa826346e817b051cbbcf9b8af7` | 139678 |
| `PREDICTION_LOG_COMBINED_5.md` | `127b0ca79a793860b47fc3a5a6a26f7a3bd95586ed62f439f228c9cfb56e8703` | 1057962 |
| `archive/audit_documents_implemented_2026-09-25/AUDIT_RECONCILIATION_ALL_SPORTS_2026-09-21.md` | `4cc9ca4c2da51dae05ea01ff864b86c99b273f2ec2cb3347613b776167ab2621` | 14968 |
| `archive/audit_documents_implemented_2026-09-25/AUDIT_IMPLEMENTATION_2026-09-21-CR3.md` | `3ce923f087fc42f5a42fc86ea6d23b2122f75b63be38c3bf2bd19cf66402b978` | 6320 |
| `archive/audit_documents_implemented_2026-09-25/AUDIT_CLOSURE_LEDGER_2026-09-25.md` | `22b5a8b01fda9b07d0062506e25d3d4992d4fc04c9742c70c3bf8157448a8272` | 17137 |
| `research/base_rates_2026-09-25/README.md` | `e62e32f84c0ceaf536acbfd26010e3b2845ef867e9b3fb2a73b4ceec93fbfebf` | 4297 |
| `research/base_rates_2026-09-25/analyze_extra.py` | `07b85846c3a3969662883a177e412ba3d428be58c36e0380f1f63d93f5b1441b` | 3952 |
| `research/base_rates_2026-09-25/analyze_leagues.py` | `c277fbea3457ab6cfcad9d654d6f108be5c630d75fb3d5bb2fa8f154bd146595` | 12818 |
| `research/base_rates_2026-09-25/analyze_mlb.py` | `37eeb60dd15dfec070e8a1220acc3d9c947481b724603f7e6bb5a12bb2eb92f7` | 3871 |
| `research/base_rates_2026-09-25/analyze_more.py` | `939e7e1cffb8c7951f1cc795ff331ef07ab80d3f4538c3ca80820a09b60990c7` | 4845 |
| `research/base_rates_2026-09-25/analyze_nhl.py` | `c889c185a596cc3191ecd794a3263419554d916bad3fcd763733575d88613e2b` | 3811 |
| `research/base_rates_2026-09-25/analyze_nhl_pre.py` | `e4b70d8615a73743d7897b86ec7de491ba57cf3c92d1484a4fa2767ac40bec55` | 322 |
| `research/base_rates_2026-09-25/analyze_tennis.py` | `4e508b00e77dd428a992e0428c3bb3acaddbb254ae72024a20cfe36e7a7be51b` | 4975 |
| `research/base_rates_2026-09-25/extra_results.json` | `b0712035363175342dc4dad16107c26f1ae4e3ce46ecf0e01b5d4d457737c2e8` | 3768 |
| `research/base_rates_2026-09-25/fetch.py` | `6ac05a3beaca1b9f1921e848f5119e5012efa185de5e6c59ca5e9b061aed5488` | 2705 |
| `research/base_rates_2026-09-25/league_results.json` | `5217d09ecbd55a63bbd3ad2330141ce428c47e22a8d78a7c681e081a3892386f` | 17454 |
| `research/base_rates_2026-09-25/mlb_results.json` | `6fc884ceab5f7aff2f5f0985c6b6a5efd05622b80fea00bfa92f544696689005` | 5807 |
| `research/base_rates_2026-09-25/more_results.json` | `86c76c3329108e1ffe44f34a8a82bbdeacb2224d21f9f65fc88c08b787bc7298` | 5300 |
| `research/base_rates_2026-09-25/nhl_results.json` | `0186286b32d3f373faeb8946aebee7cb195d85e0ec349377baac1fda76b99b00` | 2149 |
| `research/base_rates_2026-09-25/pooled_checks.py` | `a84d47f596dc3474bdc09b3344a8aceda82f9f319192ea81229f06c082b78c40` | 3282 |
| `research/base_rates_2026-09-25/pull_all.py` | `de3c068d4dd900fe48d16c11af47c98a46e7885a9c83119d18d3c3dbe0a397f2` | 591 |
| `research/base_rates_2026-09-25/pull_more.py` | `14c90f5481a6e4ddc04950918040d6d0b919dc99bee5db5cfd05439d9ec294de` | 2449 |
| `research/base_rates_2026-09-25/pull_nhl_pre.py` | `53a6ea9ece407426622606c1a7d97b08154d7721e12aa40aef75620357cb4fe8` | 328 |
| `research/base_rates_2026-09-25/pull_nhl_tennis.py` | `32d15bcb8efc7bb69d880883c0e6d91610758b676c58ed63d31fb6d9054517c6` | 3509 |
| `research/base_rates_2026-09-25/tennis_results.json` | `274650d4117e9b75bfaaaa028f43a7f6ae599a265a46a397ba94d326d886f34e` | 5574 |
| `CURRENT_RULES.md` | `412daf58757daf5aa444acc5109b1ac80b913eca69d64c3fc75fd213695b2750` | 44267 |
| `CHANGELOG.md` | `586adef8e7199721965c24a412239230fa5ad883486e37133b6a55309a74d655` | 40607 |
| `CONTRIBUTING.md` | `2a62e9f3910c01e474ad3f5bac3b5b493277b901a4f2caae82d35ab6cfe57ee6` | 4705 |
| `SKILL_BASELINE_LEDGER.md` | `63ab9bddaff8d5381224664aa929df759eebbdbc03a189688c0f8daed4458712` | 10145 |
| `LICENSE` | `1efb20731adc03fb046120ceeceb7f4e0ca0d73b2eb2d5fcf2093350863161b8` | 1211 |
| `.gitignore` | `3d36960f62f2ed189d59bfd55f1ea7e1609e8d7c953e86d15d19202adc46650c` | 1038 |
| `.gitattributes` | `8e7b10c0994c597d8d35111d065d6986c543f5a514d308ec74217885443e9dcc` | 513 |
| `.github/workflows/checks.yml` | `4f28e429fc6f69a1bce9f029572479235edeb468b14a0865e724457a00195743` | 1619 |
| `tools/manifest_lib.py` | `646b30705db92e03c0c83e135274aff6317c41a688d80dd6f4e6099d7bd395e6` | 2133 |
| `tools/make_manifest.py` | `247bfc65d265f643a8225a2dcf29feb86fc88b51a7d3ea31da4cdd360e705de6` | 8576 |
| `tools/verify_manifest.py` | `51fc35aedd098185c6a4e17b63d6bbe5a6c1ca74757be50b6b06dc3f561fa2b4` | 3551 |
| `tools/repo_hygiene.py` | `32f25a888190325ff8994180710571af7cbe6507883c3e386e9b6c5c6dad7981` | 5270 |
| `tools/skill_baseline.py` | `320f3a3aa35cada5cb1f5d31e427e8382d6d22ad276a876fadae1600e917f543` | 7616 |
| `tools/test_repo_tools.py` | `23691fbacce8bf207e5843a0a9e1dafd89fa803d8474c8dec1fcedac8f96c2f6` | 7934 |
| `tools/test_skill_baseline.py` | `5b9af14596de89231a56aed60a24c4d7c817ff6d9748b4d7203a9a6bf50fab18` | 3637 |
| `research/base_rates_2026-09-25/build_skill_baseline_seed.py` | `babaa48ef17feb22916bab7feabf04ff2a4b3d800393fcafaa5246d578d61ede` | 9714 |
| `research/base_rates_2026-09-25/.gitignore` | `03edf42376bb781d8497699bee737ae42badca878e1d27cf191d04e87e8d872c` | 161 |
| `tools/card_math.py` | `a14202a134b101a62950a96e52751a8b5d8236dfb513b8a4a37c091106082677` | 11330 |
| `tools/calibration_report.py` | `15964628f4a89325acff60d3bd07a1ca9c2ded0de0e76574cf1c6a88622cf042` | 8502 |
| `tools/test_card_math.py` | `f3c65d208b5bcbb4850b0ebfc531d192038cf5ee3bbc670fbf33b4b8cd0144c7` | 5601 |
| `research/settled_rows_2026-09-25/README.md` | `b30c19d31bfe21a70222cc76fe200846bc0da89083a86fac9b308f1112a17ee1` | 9792 |
| `research/settled_rows_2026-09-25/extract_settled_rows.py` | `5aa5a094855d1894e8cb29f9c9fd9cc96d33befbf515ce7aa79fb92552e54a17` | 19751 |
| `research/settled_rows_2026-09-25/analyze_settled.py` | `4eff0b3eb4b3d497a361dc450eca97cb86979ca543cfba33f09c1eabb1a82b32` | 8463 |
| `research/settled_rows_2026-09-25/analyze_supplement.py` | `148653ad9e111b5730cb1ce5267a7b3f07c1e4036dd12c802b4907f603b7491b` | 4868 |
| `research/settled_rows_2026-09-25/analysis_results.json` | `b1441e3e1c1f471286271e90738e2dcf3c8cd5036b4fc2773c304877da0b229f` | 17392 |
| `research/settled_rows_2026-09-25/supplement_results.json` | `78b9ed833e03bf85a43851f00434456a463a223cc16987eacc3be3e61dab0beb` | 5262 |
| `tools/rank_model.py` | `d6589f7f6a16fdf078446c75c3cd5c834a8cc3c341969bcf0daadb24357c38df` | 22683 |
| `tools/rank_model_coefficients.json` | `d8b6d12a7a48804a2e4ec366066bd66ead1b880d8c23dffd54c81d6483a62c68` | 341 |
| `tools/test_rank_model.py` | `e0c7960ea338fb9c68ac4e62099d1ee4e14836f4d6b038d84eb8c1f20ef0de9e` | 6736 |
| `tools/team_baseline.py` | `fd9adec4d863a8aff17c700ad6daeef2eb28b34abf08bd26bc591756d1221b28` | 26662 |
| `tools/test_team_baseline.py` | `eaed5279e273bef44da03b6fc63744ad076571b2a8ffd6bbbde713d3e1183d3b` | 4885 |
| `research/rank_model_2026-09-25e/README.md` | `d0eba618b172973f389ee79cbc5dbd686fa978d421da314b74fed2b05c94a4cb` | 11431 |
| `research/rank_model_2026-09-25e/validate_rank_model.py` | `8de3651281eeb547981b0471d63ec3293d3288b87b04bdd1d393423d665eb00d` | 13308 |
| `research/team_baseline_2026-09-25e/README.md` | `2cea0dc61b944733479804d1f7ac01c91f7d91df55aeb39ef5121424e9b30ee3` | 9237 |
| `research/team_baseline_2026-09-25e/validate_team_baseline.py` | `d926982f8b0a1acaf1bbe3a769fa9f37a6b163f7d57cd12b18930b78138b9da7` | 8691 |
| `research/team_baseline_2026-09-25e/oval_base_rates.py` | `62617d80a3eec1c8f077df04dfa03ae1d97f5144e33c1d95029b7dd6596ca7dd` | 5991 |
| `research/team_baseline_2026-09-25e/pull_oval.py` | `ebf68e78db6e555c0228f52327252b02918842c0b33e3ab9cc9b62643eae77a4` | 1114 |
| `research/base_rates_2026-09-25/pull_oval_specs.py` | `1b757907548ea1341eb5e3119c509dd2705aaa34f6dd79637896acc4144a7ea3` | 694 |
| `LEARNINGS_INDEX.md` | `d7abda94bf7f86953dcaa7ddf776ecc613a827b4cc0421016db02419bc62fb53` | 36399 |
| `MARKET_BENCHMARK_LEDGER.md` | `c17ac01e622fc07e020c28ac576fcd6f0478af06b0212610b2f37ac3591aa467` | 3349 |
| `tools/slate_universe.py` | `9331769ace5441d9d1c63f3ae5412b1c8960cd1e8c44cfb569236e5935141550` | 15186 |
| `tools/test_slate_universe.py` | `030a22aefb59d4df5da9b538bd89533eb82172baf3e709da1fdf3ef1f3bb3db4` | 4689 |
| `tools/market_benchmark.py` | `fdc541ceb97b784d9c2b0c0f82a27a9f4e422b4b05e18b55a072f11a9ecf4eba` | 11107 |
| `tools/test_market_benchmark.py` | `56cd7541090ed5180c7841d94d6cfdfd8371b7b332c582c2d05e3442c5d1e794` | 4559 |
| `tools/evidence_status.py` | `985f233ddfa96903679e3517d17b833595c066d4cfdfdd7d2e9da523298ee4b2` | 9596 |
| `tools/test_evidence_status.py` | `63db5f665c55102118eeb6eaf4326e9fa46c1db49b180143543ffdc6eb45da3b` | 4954 |
| `tools/mlb_model.py` | `cb0dc9093f10a04542fa9360f53a4771340b546cd9254e44df8cd4cce55ba0c2` | 29942 |
| `tools/test_mlb_model.py` | `e683dd68f913beaf8aecd938ce3b9616bf6e875860809bf2b70f69ad11406c7f` | 9939 |
| `research/mlb_shadow/README.md` | `d8cab21b78a75948795a00bc18a7e9b5a313567af517d4e9fc36d60710c424a2` | 3442 |
| `tools/sport_models.py` | `8439e379299a6c52ffca6b0565ddd8fd49d3b7b014dabc2b1d1b09ade04fc002` | 96649 |
| `tools/sport_data.py` | `60beb71298a396201db5f9dd99478a88e765ca873c145010c7ac34f2ddf40667` | 22430 |
| `tools/test_sport_models.py` | `927147b812bcf841f686c2696e3db137263e5c40a8af7538c8e599025ad4f9df` | 35079 |
| `research/sport_shadow/README.md` | `bcd0cc4b390f7d09992ea7cf5f50e3ab33087abe1508ad61e28b2a9d19942f0a` | 5578 |
| `research/sport_models_2026-09-26/README.md` | `6c6a0f63ade64284c6eeb3a8225d04a947e89561734020632a11cccda6f013c1` | 27775 |
| `research/sport_models_2026-09-26/validation_results.json` | `0967c988b8ca62be57d8bdfb789bb37ac0237d88959677c952fee0fa7d6f79ea` | 74704 |
