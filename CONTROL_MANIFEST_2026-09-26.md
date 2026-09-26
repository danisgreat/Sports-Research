# Control manifest — 2026-09-26 (review implementation: evidence before rules)

Method: **MDS-2026.09.19-v4.3**
Control revision: **CR-2026.09.21-3** (label unchanged; content receipt under the same label)
Status: **CURRENT post-write content receipt**, generated 2026-09-26 15:03 AEST by `tools/make_manifest.py` from `CONTROL_MANIFEST_2026-09-25-6.md`.

**Purpose.** This is the byte-level SHA-256 receipt that every new card freezes (`METHOD.md` header; PF-7). Implements the 2026-09-26 repository review (RULES_GENERAL.md §"2026-09-26"): C-RULE-FREEZE, C-READING-GATE and the sport files' §0 live pages, C-EVENT-UNIVERSE, C-MARKET-BENCHMARK (post-settlement scoring only), C-MLB-SHADOW, the evidence-status tool, LEARNINGS_INDEX.md, the closed candidate backlog and the repository clean-up. No card was issued under CONTROL_MANIFEST_2026-09-25-6.

**It does not change any forecasting coefficient, probability cap or ranking override.**

**Category (C-RULE-FREEZE):** MEASUREMENT.

This manifest is excluded from its own hash table. The living logs (`PREDICTION_LOG_COMBINED_5.md`, `GAME_LOG_STATUS_CURRENT.md`) are a write-time snapshot and change with every card. Hashes are taken in CRLF form (`tools/manifest_lib.py`); verify with `python tools/verify_manifest.py`.

**Changed since CONTROL_MANIFEST_2026-09-25-6.md (by bytes):** `README.md`, `METHOD.md`, `CONTROLS.md`, `RULES_GENERAL.md`, `UPCOMING_GAME_RESEARCH_GUIDE.md`, `SCORING_AND_VALIDATION.md`, `LEARNING_REGISTER.md`, `RULES_BASEBALL.md`, `RULES_CRICKET.md`, `RULES_SOCCER.md`, `RULES_BASKETBALL.md`, `RULES_AFL.md`, `RULES_NRL_RUGBY.md`, `RULES_RUGBY_UNION.md`, `RULES_AMERICAN_FOOTBALL.md`, `RULES_ICE_HOCKEY.md`, `RULES_TENNIS.md`, `audit_card_controls.py`, `test_audit_card_controls.py`, `NUMERICAL_PROGRAM.md`, `NUMERICAL_MODEL_REGISTER.md`, `CURRENT_RULES.md`, `CHANGELOG.md`, `CONTRIBUTING.md`, `SKILL_BASELINE_LEDGER.md`, `.gitignore`, `.github/workflows/checks.yml`, `tools/make_manifest.py`, `tools/repo_hygiene.py`, `tools/skill_baseline.py`, `tools/test_repo_tools.py`, `tools/test_skill_baseline.py`, `research/settled_rows_2026-09-25/README.md`, `research/rank_model_2026-09-25e/README.md`.

**New in the receipt:** `LEARNINGS_INDEX.md`, `MARKET_BENCHMARK_LEDGER.md`, `tools/slate_universe.py`, `tools/test_slate_universe.py`, `tools/market_benchmark.py`, `tools/test_market_benchmark.py`, `tools/evidence_status.py`, `tools/test_evidence_status.py`, `tools/mlb_model.py`, `tools/test_mlb_model.py`, `research/mlb_shadow/README.md`.

**Dropped:** none.

**Unchanged:** 69 files.

## SHA-256 file receipt

| File | SHA-256 | Bytes |
|---|---|---:|
| `README.md` | `83b7ffbd2e5a6385772422e283669329539cf9c0669f9bcb77fe5f2a258437f6` | 13243 |
| `METHOD.md` | `d911a127877ba8a34087d978d6cc5d09862f2537553f808a1dcfb4e6e66890fd` | 30556 |
| `CONTROLS.md` | `9ead96e7e539c03bf258f49303d92ddd7dbf14ee8923d8334c1d6b40f1dc2ee9` | 41896 |
| `RULES_GENERAL.md` | `8cc714483f8e78e6b9398718399e70ee31fcdf24eb9a9548475d969b6ecd76fd` | 280008 |
| `SOURCES.md` | `6e172c9fecf767af75da09d0f745e1428910795aa1e4e674a364b4b3af71faac` | 76886 |
| `DATA_SOURCE_REGISTER.md` | `898affe43d3490b83a2c8a888d88dc2b09cbdfe71024294ae79df9d32d17efef` | 178952 |
| `UPCOMING_GAME_RESEARCH_GUIDE.md` | `6957e109a00ac7c83cb4f68cd90ed7fb801816fa1fa4941abe56bb8c67846bfd` | 75475 |
| `SCORING_AND_VALIDATION.md` | `5323963fba3c5f7e687718a6946055f9cde5e860a85342acbcd3b94e0db6caea` | 23613 |
| `PERFORMANCE_ELIGIBILITY_POLICY.md` | `a102c231debc12253accf5ade0ed3086c7b51dcf3959e570129ad8b6d96dd2fa` | 19422 |
| `LEARNING_REGISTER.md` | `34f276452156aee1152ce2556c8cdc71d84e50ffb988efb1420bc1d494062c4a` | 321945 |
| `AGENT_ROLE_AND_TASK.md` | `7ab4a2b52fa33a0cf9f9838926dda2acc6babc71fb1b99c3387873b0c15d52fb` | 25862 |
| `EXTERNAL_LOGGING_WORKFLOW.md` | `b724db948916f0bb4ae8847fcfd7fc278cf5db8fed8a2d04411507f5dcc1a6d8` | 68415 |
| `FORECAST_PREFLIGHT_MANIFEST.md` | `34718b2faca3276e7213bc622e01ff06998151390f5f7c3f12497082e7468678` | 9309 |
| `RULES_BASEBALL.md` | `cf500d7f30e6a3e5554c0c923ca3521a6b299045cfc1fabbc82e9ac2fd8685ec` | 138715 |
| `RULES_CRICKET.md` | `25bae3168155e1a62fbac2e8130d1aca3b5e40b160118552b45c994efaab1258` | 112020 |
| `RULES_SOCCER.md` | `2bdd6cd2922addd20305aa13d9a78d011a5a5107ece4253321f3b8d184a18d40` | 110870 |
| `RULES_BASKETBALL.md` | `e8b0dec70fa8ddb4eb88a85e07e7f3db8c6675856e8ec62e580058d42dae2c0b` | 106777 |
| `RULES_AFL.md` | `76f80fc9c44941a1bb8af979b13aa35391c523de8b3e95925e44538655dc8fb4` | 65081 |
| `RULES_NRL_RUGBY.md` | `de596c7bbfd96073560be50f3282ee036fa1677affb119fd2f77498241bafafb` | 63732 |
| `RULES_RUGBY_UNION.md` | `1f5de0f2b8e06ec3206cd27c88bfe9e8c2d291af1c0aae461109c5b677e950ec` | 53744 |
| `RULES_AMERICAN_FOOTBALL.md` | `2bc3eeed34ab556b7010ca2cb8e7b433c8c9357dd1a2e7c5a27a0fddf8a69aa5` | 69354 |
| `RULES_ICE_HOCKEY.md` | `6bbab247dbf5851c7d88411329f88e16f617a4588e7534f4e8d92bacbce633a0` | 61002 |
| `RULES_TENNIS.md` | `e5f5a86725cb66110eda5ac645c23e54c47f9aef5f4cc2941ca88d87e86e0dab` | 77105 |
| `LEAGUE_RULES_CRICKET.md` | `b6b13dfa72047b62fd9987e21daa0ec25510ab0853ebbac461b5725de5f99099` | 26252 |
| `LEAGUE_RULES_SOCCER.md` | `236463054f21792ad091fd3f326c7cb12aac767c933ffc4bd2e265acf55df06b` | 43865 |
| `prediction_preflight.py` | `b4d07fef54e71ef8478c5b2cec3af15c5f5accf50ba3e703348ab16609006d26` | 29319 |
| `test_prediction_preflight.py` | `c91ef73ac3faa420e3b67f8e5f345a851c4f9a69e43e75c21be6d3c7a53d5d60` | 11403 |
| `audit_card_controls.py` | `f22785c09a9b6156aeda757e7cccb05288761b64f3995553176e15b575ecd67c` | 34592 |
| `test_audit_card_controls.py` | `a81d8676530d399b2c5e87373506972a45d02c44235dae42f293217eb2e1bfb0` | 16880 |
| `receipts.py` | `33c906e5b6a0f67ffaf103347f058955401923a3cb57ee43158cd7f2d1b3de30` | 21886 |
| `test_receipts.py` | `c841b495300f0e7e7afec7f4b24b1780c6a879b0067ed5b648a800625cee3c08` | 6502 |
| `H0_DATASET_CARD.md` | `a2d44c60788d0506c1108e1629fb2a2e6ac23d6fc41ca87c2e27a6d138152278` | 19413 |
| `NUMERICAL_PROGRAM.md` | `9a77514bde3433b293b94a49494cb696273915b8f3453d78dc372518e5957e1f` | 11768 |
| `NUMERICAL_MODEL_REGISTER.md` | `58f521ba28abe4d4891414d9e3a00824bdeb823b1ab844297377a15176b4f280` | 22785 |
| `NUMERICAL_TRAINING_SPEC.md` | `888fa925485a64642443b7555d8a989aea955d0a7997e23a09edef7db93bbd37` | 31309 |
| `MODEL_AND_DATA_SPEC.md` | `c4d77b5036afbe531387886ee460d35a47ba6d824bf5a13077f20d7c9906b771` | 64024 |
| `ALGORITHM_PORTFOLIO_AND_EVALUATION.md` | `c0dbea56b78a51c5f6a075d7e0ace6e0d84a4fe97a1366cd699624e5783f49aa` | 51138 |
| `MODEL_IMPLEMENTATION_RECIPES.md` | `f016aa31c039dd95152f36a6df56d2758c2769b146b73bd8b8a43fa18e02021c` | 20837 |
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
| `CURRENT_RULES.md` | `dcfdc424103f1f684d2b650bf3db82712a031e72e46c5f63c038cfd666816070` | 42719 |
| `CHANGELOG.md` | `e7272ec1af3922b287f2d87f9eedccdbea5677934af06914313ac3009fcb2d07` | 35781 |
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
| `LEARNINGS_INDEX.md` | `bd858edd04ffe70e1d4f451ede960f98ce9cce5094ced5c2cd4201a15b169ee1` | 34798 |
| `MARKET_BENCHMARK_LEDGER.md` | `c17ac01e622fc07e020c28ac576fcd6f0478af06b0212610b2f37ac3591aa467` | 3349 |
| `tools/slate_universe.py` | `9331769ace5441d9d1c63f3ae5412b1c8960cd1e8c44cfb569236e5935141550` | 15186 |
| `tools/test_slate_universe.py` | `030a22aefb59d4df5da9b538bd89533eb82172baf3e709da1fdf3ef1f3bb3db4` | 4689 |
| `tools/market_benchmark.py` | `fdc541ceb97b784d9c2b0c0f82a27a9f4e422b4b05e18b55a072f11a9ecf4eba` | 11107 |
| `tools/test_market_benchmark.py` | `56cd7541090ed5180c7841d94d6cfdfd8371b7b332c582c2d05e3442c5d1e794` | 4559 |
| `tools/evidence_status.py` | `d6fef4da0196e5100f3190b844de4622a3c00999cd1c64706a2d8be70f9ab975` | 8439 |
| `tools/test_evidence_status.py` | `da66a9bb88a01f71143dc00746f896abfcfbc5398d4ced1bbd01336787851e65` | 4451 |
| `tools/mlb_model.py` | `572e45de8079fc3f4d7c16b6d6e5279970bce66aad243ef8b2cc5b13d35ff943` | 29211 |
| `tools/test_mlb_model.py` | `0fab2be5e9a2d632156b681578317d8bd3f6328d08c65d78f56dcc8ace24aad9` | 9720 |
| `research/mlb_shadow/README.md` | `9e6b1c294664dccddde0e01ef4c8ae4637dd2f4ee7c98d5834a1f21310f1b7c4` | 2866 |
