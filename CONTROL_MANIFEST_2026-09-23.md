# Control manifest — 2026-09-23 (post-import content receipt)

Method: **MDS-2026.09.19-v4.3**  
Control revision: **CR-2026.09.21-3** (unchanged)  
Status: **CURRENT post-write content receipt** (regenerated 22:03 AEST after the §"2026-09-23(d)" P-487 follow-up appended to `LEARNING_REGISTER.md`, `RULES_BASKETBALL.md` and the two living logs; no card had frozen the earlier version — the P-495-onward mini log had issued nothing), first written 2026-09-23 21:51 AEST  
Purpose: this is the byte-level SHA-256 receipt after the 2026-09-23 consolidated mini-log import (`PREDICTION_LOG_COMBINED_5.md` §"2026-09-23(c)"). That import appended dated learning, source and custody addenda to the files listed below. **It did not change any forecasting rule, coefficient, gate or control revision.** The two promoted items (`O-ID-DATE-STARTER-MATCH`, `O-EXTERNAL-ID-CLAIM-SWEEP`) are import/custody integrity controls.

This manifest is excluded from its own hash table. `CONTROL_MANIFEST_2026-09-21-3.md` remains the receipt for cards issued before this import. The two living logs (`PREDICTION_LOG_COMBINED_5.md`, `GAME_LOG_STATUS_CURRENT.md`) are hashed as a write-time snapshot and are expected to change with every card.

Files changed by the import: `README.md`, `METHOD.md`, `RULES_GENERAL.md`, `SOURCES.md`, `DATA_SOURCE_REGISTER.md`, `LEARNING_REGISTER.md`, `EXTERNAL_LOGGING_WORKFLOW.md`, `RULES_BASEBALL.md`, `RULES_BASKETBALL.md`, `PREDICTION_LOG_COMBINED_5.md`, `GAME_LOG_STATUS_CURRENT.md`. All other hashes are unchanged from 2026-09-21-3 **by content**. Five files (`LEAGUE_RULES_CRICKET.md`, `LEAGUE_RULES_SOCCER.md`, `MODEL_IMPLEMENTATION_RECIPES.md`, `RECENCY_AND_REBOUND.md`, `AUDIT_RECONCILIATION_ALL_SPORTS_2026-09-21.md`) and `audit_card_controls.py` had already drifted in line endings only (LF v CRLF) since 2026-09-21-3. Their raw hashes below reflect the current bytes.

## SHA-256 file receipt

| File | SHA-256 | Bytes |
|---|---|---:|
| `README.md` | `24f506f05d492ea8198da94fa5aee6affcb403417a90ea49707da954f42c5d39` | 17864 |
| `METHOD.md` | `73825b6f3dfaa26e0513a02d4663b95045e489f0bbe41da5db4d7456e5048f39` | 23756 |
| `CONTROLS.md` | `a6ba8b9c72572740dcca441efd39eda8977af19c6c4fb16569ae02fb6069cd1d` | 26765 |
| `RULES_GENERAL.md` | `32e9bf899875d70b5209699bbede7831fc013509463016e0b81a6c7e14fffaf7` | 221786 |
| `SOURCES.md` | `dc85e7c05f1339f061c1198b1769ac60cc32f561b94e5f9f468cdeb193a364e6` | 67465 |
| `DATA_SOURCE_REGISTER.md` | `1fd3530ab518c82a734778dc6fbfdc87518a547fb5bf231dae22f243ad316538` | 155693 |
| `UPCOMING_GAME_RESEARCH_GUIDE.md` | `708ff7449f76894dddee8de08abeab7147af5c3979454080e59ad93e2810b0ca` | 64399 |
| `SCORING_AND_VALIDATION.md` | `c40cf2a177ba63392fe46553cb48e5264b2d06d6601fa54542b8c15ed84a882f` | 14054 |
| `PERFORMANCE_ELIGIBILITY_POLICY.md` | `6bdaebdf2884dba01860a6148c78646ba887573bfca4eefdbc82b2c60716eec1` | 18799 |
| `LEARNING_REGISTER.md` | `68a9f5d4102215f6a5e2f80d36a5704eb59519e6035d623bfb3e52e027b5788d` | 264488 |
| `AGENT_ROLE_AND_TASK.md` | `60615e839dc00715ca4f23e86e2a0acc04fd10a5dbc1487d625cf22e6f673473` | 22003 |
| `EXTERNAL_LOGGING_WORKFLOW.md` | `681919a10b433f828e3a05e654a83c516ce6298d584199c25007a8928909b3ec` | 56156 |
| `FORECAST_PREFLIGHT_MANIFEST.md` | `5a46c3dbc6a7f8a494a4785a61d98ff4d73d3ac5586e9a3dc5fed8bc6db3eb4f` | 6651 |
| `RULES_BASEBALL.md` | `1bb9407ecf8b46b6cdc5464884e46f855bd4f5d217a8bc5a09f1009d88a4c1de` | 114314 |
| `RULES_CRICKET.md` | `52f487d6aca636cad91caf72c1952ae58fd3256869a4e5d109494f3f155dd4a4` | 97248 |
| `RULES_SOCCER.md` | `3e88677b9f8ea6b6cce0a605d940225c95d9f4ea6d1d15647dcc7dcab756c619` | 96139 |
| `RULES_BASKETBALL.md` | `2671721fdafa9542c7179aef9ffa0e3b14acf77c2a7fdeacd38a022dcd275bfa` | 83742 |
| `RULES_AFL.md` | `3f3809483892104c954772ea3c829a2187ad7fab19080845c95e8d35c83c2ed9` | 55484 |
| `RULES_NRL_RUGBY.md` | `ae76c443207759e245878d0f6a75d8b202eb2478785bbfe59b11a68393527fd6` | 54301 |
| `RULES_RUGBY_UNION.md` | `33d832954efa7ac05d9c7a3b2e458771c00eeb0909c7ef566ed3d2bfaed1c318` | 48927 |
| `RULES_AMERICAN_FOOTBALL.md` | `b265af696cff8d787f52ef05d963eea60664c1f8108ef3dd3fd37fc9ec881e5c` | 59418 |
| `RULES_ICE_HOCKEY.md` | `32016cc2b193f150407a82db37893a251f0f35d9d56d0149b81a7301a81e9d4a` | 49073 |
| `RULES_TENNIS.md` | `0994c197c71d0a43070788c4c8ae4d130e054ca10501035b27d8d74c1273dcd1` | 59582 |
| `LEAGUE_RULES_CRICKET.md` | `b6b13dfa72047b62fd9987e21daa0ec25510ab0853ebbac461b5725de5f99099` | 26252 |
| `LEAGUE_RULES_SOCCER.md` | `236463054f21792ad091fd3f326c7cb12aac767c933ffc4bd2e265acf55df06b` | 43865 |
| `prediction_preflight.py` | `f7526d309b776e0e7c583ad5c323e5bbc9c213a01998d56d305092b0323c2a51` | 25413 |
| `test_prediction_preflight.py` | `bd4bd8815e371be425b9c5b9801d8e2d305babf3a34f718544e41b1ee76f442a` | 8007 |
| `audit_card_controls.py` | `47cafe267d50024eb58d544b150fed9bb1aadb8617385dd4aca90e3dd76fa4f1` | 17463 |
| `H0_DATASET_CARD.md` | `a2d44c60788d0506c1108e1629fb2a2e6ac23d6fc41ca87c2e27a6d138152278` | 19413 |
| `NUMERICAL_PROGRAM.md` | `964168bbbdd3c21ab5956f7d2150cab14e6c13063441c6c3e7784426c3e305e0` | 9626 |
| `NUMERICAL_MODEL_REGISTER.md` | `7fe3f9ecfb51f0e0519ef8d91a857b0038393cdb2546fd2a1b3ee52966aef968` | 22540 |
| `NUMERICAL_TRAINING_SPEC.md` | `888fa925485a64642443b7555d8a989aea955d0a7997e23a09edef7db93bbd37` | 31309 |
| `MODEL_AND_DATA_SPEC.md` | `ac81a79812e3a5f1fa50002f9261732cb59fa12232e121fd78d9cf154292cd34` | 63977 |
| `ALGORITHM_PORTFOLIO_AND_EVALUATION.md` | `0c85f4b5efe57f8bc5e48ba186d79feaf7980d97edac6422212a9bd5f3f850ad` | 51091 |
| `MODEL_IMPLEMENTATION_RECIPES.md` | `f016aa31c039dd95152f36a6df56d2758c2769b146b73bd8b8a43fa18e02021c` | 20837 |
| `RECENCY_AND_REBOUND.md` | `58234fa4c0f3babe29f3c3ba94479ac91f441d1e097cf6750daa7c3316bba9bc` | 11914 |
| `BASE_RATES_REGISTER.md` | `44684c1843843316ae0732cd0da4934841b5ddf18315740e347b97de441b1412` | 9903 |
| `GAME_LOG_STATUS_CURRENT.md` | `b2d01a9c24d7836ade630c765c001b42b2f54c0edb49f7604020e14495128f9b` | 126624 |
| `PREDICTION_LOG_COMBINED_5.md` | `9302d6a8e9318e0faf6804b8f150a7297e6865d9177ec7cb93e177e8f4893612` | 290340 |
| `AUDIT_RECONCILIATION_ALL_SPORTS_2026-09-21.md` | `4cc9ca4c2da51dae05ea01ff864b86c99b273f2ec2cb3347613b776167ab2621` | 14968 |
| `AUDIT_IMPLEMENTATION_2026-09-21-CR3.md` | `3ce923f087fc42f5a42fc86ea6d23b2122f75b63be38c3bf2bd19cf66402b978` | 6320 |
