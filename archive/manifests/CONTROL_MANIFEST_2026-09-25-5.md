# Control manifest — 2026-09-25-5 (Rank-1/Rank-2 pass: RM-1 ranking model, TB-1 team baseline, oval references, settlement from the feed)

Method: **MDS-2026.09.19-v4.3**
Control revision: **CR-2026.09.21-3** (label unchanged; content receipt under the same label)
Status: **CURRENT post-write content receipt**, generated 2026-09-25 23:51 AEST by `tools/make_manifest.py` from `CONTROL_MANIFEST_2026-09-25-4.md`.

**Purpose.** This is the byte-level SHA-256 receipt that every new card freezes (`METHOD.md` header; PF-7). Adds C-RANK-MODEL (RM-1, tools/rank_model.py), C-TOP2-QUALITY, C-TEAM-BASELINE (TB-1, tools/team_baseline.py), the amended C-PLUS-CUSHION with population cover rates (BASE_RATES_REGISTER.md 7.7), C-SETTLEMENT-FROM-FEED with audit fields RM, TB and 10n, the NFL/AFL/NRL references, the rebuilt settled-row dataset (17 mis-graded rows corrected) and the P-510-P-515 import.

**Model change:** YES. RM-1 (tools/rank_model_coefficients.json: a -0.187, b 1.543, cushion -1.127; fitted 2026-09-25 on 409 decision rows) is a user-authorised exception to L-087. It sets the issued rank order (C-RANK-MODEL) and never changes a stated probability. Safeguards: RULES_GENERAL.md 2026-09-25(e)(h). TB-1 constants are population-fitted (no log results).

This manifest is excluded from its own hash table. The living logs (`PREDICTION_LOG_COMBINED_5.md`, `GAME_LOG_STATUS_CURRENT.md`) are a write-time snapshot and change with every card. Hashes are taken in CRLF form (`tools/manifest_lib.py`); verify with `python tools/verify_manifest.py`.

**Changed since CONTROL_MANIFEST_2026-09-25-4.md (by bytes):** `README.md`, `METHOD.md`, `CONTROLS.md`, `RULES_GENERAL.md`, `SOURCES.md`, `DATA_SOURCE_REGISTER.md`, `UPCOMING_GAME_RESEARCH_GUIDE.md`, `SCORING_AND_VALIDATION.md`, `LEARNING_REGISTER.md`, `AGENT_ROLE_AND_TASK.md`, `EXTERNAL_LOGGING_WORKFLOW.md`, `RULES_BASEBALL.md`, `RULES_CRICKET.md`, `RULES_SOCCER.md`, `RULES_BASKETBALL.md`, `RULES_AFL.md`, `RULES_NRL_RUGBY.md`, `RULES_RUGBY_UNION.md`, `RULES_AMERICAN_FOOTBALL.md`, `RULES_ICE_HOCKEY.md`, `RULES_TENNIS.md`, `audit_card_controls.py`, `test_audit_card_controls.py`, `BASE_RATES_REGISTER.md`, `GAME_LOG_STATUS_CURRENT.md`, `PREDICTION_LOG_COMBINED_5.md`, `CURRENT_RULES.md`, `CHANGELOG.md`, `.gitignore`, `tools/make_manifest.py`, `research/settled_rows_2026-09-25/README.md`, `research/settled_rows_2026-09-25/extract_settled_rows.py`.

**New in the receipt:** `tools/rank_model.py`, `tools/rank_model_coefficients.json`, `tools/test_rank_model.py`, `tools/team_baseline.py`, `tools/test_team_baseline.py`, `research/rank_model_2026-09-25e/README.md`, `research/rank_model_2026-09-25e/validate_rank_model.py`, `research/team_baseline_2026-09-25e/README.md`, `research/team_baseline_2026-09-25e/validate_team_baseline.py`, `research/team_baseline_2026-09-25e/oval_base_rates.py`, `research/team_baseline_2026-09-25e/pull_oval.py`, `research/base_rates_2026-09-25/pull_oval_specs.py`.

**Dropped:** none.

**Unchanged:** 59 files.

## SHA-256 file receipt

| File | SHA-256 | Bytes |
|---|---|---:|
| `README.md` | `2e8c16daf9a5a5946d5f53f9fa5fed2a4b342bb040fcf4bdd257f5c87d1948ae` | 10556 |
| `METHOD.md` | `0428e5e78aeb23a59260501971ad02c68f0945c836e34cc2fcf9e2993cf1a526` | 28982 |
| `CONTROLS.md` | `809d2a9e5694944a19d518a2769306c7f91b18f3a78c96c7babed3046f0b9dbe` | 39650 |
| `RULES_GENERAL.md` | `8f0b83cdf80a34c544890d6304de78f77836aff9f78dad925c4bb7d1be55b80a` | 269316 |
| `SOURCES.md` | `6e172c9fecf767af75da09d0f745e1428910795aa1e4e674a364b4b3af71faac` | 76886 |
| `DATA_SOURCE_REGISTER.md` | `898affe43d3490b83a2c8a888d88dc2b09cbdfe71024294ae79df9d32d17efef` | 178952 |
| `UPCOMING_GAME_RESEARCH_GUIDE.md` | `2953159d8bb7da5d72324adb53870a660ed4d51d8d38c20543f91983c6138a77` | 74704 |
| `SCORING_AND_VALIDATION.md` | `bb68cbe78478a4803d15fdac22345975dffd7fbd8a30a91f6f59ccae33fb913c` | 21735 |
| `PERFORMANCE_ELIGIBILITY_POLICY.md` | `a102c231debc12253accf5ade0ed3086c7b51dcf3959e570129ad8b6d96dd2fa` | 19422 |
| `LEARNING_REGISTER.md` | `daf42692e23436d9805368778cd9dc8ac15c55979fe500c6223265364d080885` | 311573 |
| `AGENT_ROLE_AND_TASK.md` | `7ab4a2b52fa33a0cf9f9838926dda2acc6babc71fb1b99c3387873b0c15d52fb` | 25862 |
| `EXTERNAL_LOGGING_WORKFLOW.md` | `b724db948916f0bb4ae8847fcfd7fc278cf5db8fed8a2d04411507f5dcc1a6d8` | 68415 |
| `FORECAST_PREFLIGHT_MANIFEST.md` | `34718b2faca3276e7213bc622e01ff06998151390f5f7c3f12497082e7468678` | 9309 |
| `RULES_BASEBALL.md` | `19b333db29abc5d2ac3416506b6ee85f46636eea950620a921a52b7546ae8af7` | 128143 |
| `RULES_CRICKET.md` | `ccb69b131c1be6dd23b89a1903f63b23197193e4a5b16e4fdc6a8d95ec0a1e38` | 104057 |
| `RULES_SOCCER.md` | `e0adf82a4250399a65fcca086ff0049408f130240c9d8d07981734bba4104d96` | 101752 |
| `RULES_BASKETBALL.md` | `f6d1325869d6d44decafb3175aeb1d6c421f9dbe72bba53f1bae8305abc0e7ad` | 97933 |
| `RULES_AFL.md` | `1e443386b906ab88d5aadfd0727a11ad7b5cbdad8430dd969cdf98b8f6fc977c` | 59270 |
| `RULES_NRL_RUGBY.md` | `18328783a3941d1098cd1b6014b39632786416aa438cd0af0d8535f32c70d1a3` | 57802 |
| `RULES_RUGBY_UNION.md` | `2d5a2af4f1d033002f5a2e3947aca662a5b51b22e5268694347bf194fe918783` | 50118 |
| `RULES_AMERICAN_FOOTBALL.md` | `747cea7432b9d107db78b3f0313349f3c4bc1234dd2b313a0e528c8b94b8140f` | 63017 |
| `RULES_ICE_HOCKEY.md` | `f6c1907ecff15978d7c5f04758359c266ed836244d5a6e1c588f9ea25b9635a1` | 55432 |
| `RULES_TENNIS.md` | `b1c2a11b7e19739b919af350afc8ad8e06d411cf4a3a570b2a72bf0cd4397062` | 70935 |
| `LEAGUE_RULES_CRICKET.md` | `b6b13dfa72047b62fd9987e21daa0ec25510ab0853ebbac461b5725de5f99099` | 26252 |
| `LEAGUE_RULES_SOCCER.md` | `236463054f21792ad091fd3f326c7cb12aac767c933ffc4bd2e265acf55df06b` | 43865 |
| `prediction_preflight.py` | `b4d07fef54e71ef8478c5b2cec3af15c5f5accf50ba3e703348ab16609006d26` | 29319 |
| `test_prediction_preflight.py` | `c91ef73ac3faa420e3b67f8e5f345a851c4f9a69e43e75c21be6d3c7a53d5d60` | 11403 |
| `audit_card_controls.py` | `d824bed2f7d2aabd02511c1eaac60aa94adf0c2967043f21472f62b0c5eac94f` | 33911 |
| `test_audit_card_controls.py` | `ca3289169b54c9e456f5ba213b7a8333ed8d08948b399c1159032dfd7478eff5` | 15992 |
| `receipts.py` | `33c906e5b6a0f67ffaf103347f058955401923a3cb57ee43158cd7f2d1b3de30` | 21886 |
| `test_receipts.py` | `c841b495300f0e7e7afec7f4b24b1780c6a879b0067ed5b648a800625cee3c08` | 6502 |
| `H0_DATASET_CARD.md` | `a2d44c60788d0506c1108e1629fb2a2e6ac23d6fc41ca87c2e27a6d138152278` | 19413 |
| `NUMERICAL_PROGRAM.md` | `bd82f29e15cab12853a9a05cae71369219284cc639d8a9735b6b845c55682d99` | 11311 |
| `NUMERICAL_MODEL_REGISTER.md` | `7fe3f9ecfb51f0e0519ef8d91a857b0038393cdb2546fd2a1b3ee52966aef968` | 22540 |
| `NUMERICAL_TRAINING_SPEC.md` | `888fa925485a64642443b7555d8a989aea955d0a7997e23a09edef7db93bbd37` | 31309 |
| `MODEL_AND_DATA_SPEC.md` | `c4d77b5036afbe531387886ee460d35a47ba6d824bf5a13077f20d7c9906b771` | 64024 |
| `ALGORITHM_PORTFOLIO_AND_EVALUATION.md` | `c0dbea56b78a51c5f6a075d7e0ace6e0d84a4fe97a1366cd699624e5783f49aa` | 51138 |
| `MODEL_IMPLEMENTATION_RECIPES.md` | `f016aa31c039dd95152f36a6df56d2758c2769b146b73bd8b8a43fa18e02021c` | 20837 |
| `RECENCY_AND_REBOUND.md` | `b35e9684ecb6d468b2570d6e429301cba567f8590e230bb3a46d42ffd4d93f37` | 18248 |
| `BASE_RATES_REGISTER.md` | `6789928df1e7bf55dd814c62d1b63fb50a19d52d60f728d16465608650b91c6b` | 31145 |
| `GAME_LOG_STATUS_CURRENT.md` | `40ea7942ff1f50e9fc6392284f08533eaa372b68a364ef017f270d7aa5ef57a6` | 138402 |
| `PREDICTION_LOG_COMBINED_5.md` | `73bd052aedb0a7a2f9cf2197c9ed8a2ed7a330930c5649a2af2b7d8688aefafc` | 1055119 |
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
| `CURRENT_RULES.md` | `b702b35e0f89a5950ef0c1c2ee2aabff0d903003497010831b5fc724d8a2681f` | 36604 |
| `CHANGELOG.md` | `2a966dfdbc99324aabece58e3eb192681b43697543972c7af91023d24afbe6b0` | 32257 |
| `CONTRIBUTING.md` | `3f6613706d74371319720ec83bbc18fefa39dc98b6169e5bf4af1b0915aeb427` | 3801 |
| `SKILL_BASELINE_LEDGER.md` | `0d914665196efe3983da38970a98cfc97444d6d66360cc65ed425569010bd92d` | 9842 |
| `LICENSE` | `1efb20731adc03fb046120ceeceb7f4e0ca0d73b2eb2d5fcf2093350863161b8` | 1211 |
| `.gitignore` | `e104c452c53c0dc2bca85d91432af13282d289ca04876e83384357be0f493fc9` | 906 |
| `.gitattributes` | `8e7b10c0994c597d8d35111d065d6986c543f5a514d308ec74217885443e9dcc` | 513 |
| `.github/workflows/checks.yml` | `fedefe694e26c153292cddfc78b86837ee63766dc8fbce3a3e775cc891e1a0dc` | 1506 |
| `tools/manifest_lib.py` | `646b30705db92e03c0c83e135274aff6317c41a688d80dd6f4e6099d7bd395e6` | 2133 |
| `tools/make_manifest.py` | `1eb47935c679e8e2bc84a8ef2eace8c8d40f9090a0c9cfadacc29fe493065049` | 5715 |
| `tools/verify_manifest.py` | `51fc35aedd098185c6a4e17b63d6bbe5a6c1ca74757be50b6b06dc3f561fa2b4` | 3551 |
| `tools/repo_hygiene.py` | `fed26719c9b4e354f2a545a469f762527b6a92893b6ef124528f1f58693532cb` | 3846 |
| `tools/skill_baseline.py` | `ae5cb0be0328cabee235deff66db3dadf1f19da6884ad66c71ae0693f13146e7` | 5722 |
| `tools/test_repo_tools.py` | `48cd7ceb321d6948bf4f9d034492c4765f2cc23fa77e99e3705b8519c9d932a5` | 5574 |
| `tools/test_skill_baseline.py` | `17e395c1703dba96eec1f80949a064ddddd5e836a676e245d1329b25763f5413` | 2688 |
| `research/base_rates_2026-09-25/build_skill_baseline_seed.py` | `babaa48ef17feb22916bab7feabf04ff2a4b3d800393fcafaa5246d578d61ede` | 9714 |
| `research/base_rates_2026-09-25/.gitignore` | `03edf42376bb781d8497699bee737ae42badca878e1d27cf191d04e87e8d872c` | 161 |
| `tools/card_math.py` | `a14202a134b101a62950a96e52751a8b5d8236dfb513b8a4a37c091106082677` | 11330 |
| `tools/calibration_report.py` | `15964628f4a89325acff60d3bd07a1ca9c2ded0de0e76574cf1c6a88622cf042` | 8502 |
| `tools/test_card_math.py` | `f3c65d208b5bcbb4850b0ebfc531d192038cf5ee3bbc670fbf33b4b8cd0144c7` | 5601 |
| `research/settled_rows_2026-09-25/README.md` | `83703540c664e68477b582683223a659a6a3dc5f663c45b16fe44e8d2869639b` | 8825 |
| `research/settled_rows_2026-09-25/extract_settled_rows.py` | `8d10e91a04fe946c5136d0da0274110afea43836d6bb30dc3bbfb1b0c06af6e0` | 19385 |
| `research/settled_rows_2026-09-25/analyze_settled.py` | `4eff0b3eb4b3d497a361dc450eca97cb86979ca543cfba33f09c1eabb1a82b32` | 8463 |
| `research/settled_rows_2026-09-25/analyze_supplement.py` | `148653ad9e111b5730cb1ce5267a7b3f07c1e4036dd12c802b4907f603b7491b` | 4868 |
| `research/settled_rows_2026-09-25/analysis_results.json` | `b1441e3e1c1f471286271e90738e2dcf3c8cd5036b4fc2773c304877da0b229f` | 17392 |
| `research/settled_rows_2026-09-25/supplement_results.json` | `78b9ed833e03bf85a43851f00434456a463a223cc16987eacc3be3e61dab0beb` | 5262 |
| `tools/rank_model.py` | `d6589f7f6a16fdf078446c75c3cd5c834a8cc3c341969bcf0daadb24357c38df` | 22683 |
| `tools/rank_model_coefficients.json` | `d8b6d12a7a48804a2e4ec366066bd66ead1b880d8c23dffd54c81d6483a62c68` | 341 |
| `tools/test_rank_model.py` | `e0c7960ea338fb9c68ac4e62099d1ee4e14836f4d6b038d84eb8c1f20ef0de9e` | 6736 |
| `tools/team_baseline.py` | `fd9adec4d863a8aff17c700ad6daeef2eb28b34abf08bd26bc591756d1221b28` | 26662 |
| `tools/test_team_baseline.py` | `eaed5279e273bef44da03b6fc63744ad076571b2a8ffd6bbbde713d3e1183d3b` | 4885 |
| `research/rank_model_2026-09-25e/README.md` | `2c82d81b17e5a3caa1a64aafe7f7277993187daca9641cfecdcf680b0077b256` | 9555 |
| `research/rank_model_2026-09-25e/validate_rank_model.py` | `8de3651281eeb547981b0471d63ec3293d3288b87b04bdd1d393423d665eb00d` | 13308 |
| `research/team_baseline_2026-09-25e/README.md` | `2cea0dc61b944733479804d1f7ac01c91f7d91df55aeb39ef5121424e9b30ee3` | 9237 |
| `research/team_baseline_2026-09-25e/validate_team_baseline.py` | `d926982f8b0a1acaf1bbe3a769fa9f37a6b163f7d57cd12b18930b78138b9da7` | 8691 |
| `research/team_baseline_2026-09-25e/oval_base_rates.py` | `62617d80a3eec1c8f077df04dfa03ae1d97f5144e33c1d95029b7dd6596ca7dd` | 5991 |
| `research/team_baseline_2026-09-25e/pull_oval.py` | `ebf68e78db6e555c0228f52327252b02918842c0b33e3ab9cc9b62643eae77a4` | 1114 |
| `research/base_rates_2026-09-25/pull_oval_specs.py` | `1b757907548ea1341eb5e3119c509dd2705aaa34f6dd79637896acc4144a7ea3` | 694 |
