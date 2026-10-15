# Verification — preferred online historical recovery

| Check | Result | Evidence and limits |
|---|---|---|
| Required full workshop suite | PASS | `python -m pytest ml/tests -q --tb=short`: **251 passed in 58.61s**; 222 previous cases plus29 source-recovery cases |
| Cross-sport metadata | PASS | All16 registered sport-family configurations exercised:13 existing supported families route from exact reviewed metadata;3 unsupported engines explicitly reject. This is not source or model qualification of every real league |
| Missing archive CLI | PASS | CLI routing test forbids get_league and still creates/verifies a supported exact-scope source bundle; no local archive discovery required |
| Defective archive | PASS | Default DATA_HOLD still blocks; an explicit fresh reviewed route with reviewed corrected rows succeeds. Old archive/model admission is unchanged |
| Invalid source metadata | PASS | Future source time, wrong evidence hash, unsupported endpoint, wrong competition, missing review, market columns, missing defect reason, nonfinite extra fraction and unsupported bonus reject before output |
| History integrity | PASS | Web origin cannot admit future history; explicit source route requires every row's disposition. Existing duplicate/target/score/known-at/scope/market checks retained |
| Source readback | PASS | Source config hash and complete MODEL_CONFIG equality; self-consistent sidecar tamper still rejects if model config differs. False web-row coverage rejects against frozen history |
| Actual command-line flow | PASS | No-archive synthetic EXAMPLE_REMOTE_CUP predict --competition-source -> settle -> next predict --feedback, both complete bundles verified,120 recovered rows and1 available feedback event. [Summary](CLI_EXAMPLE.md). No actual online collection, sporting forecast/P-ID or pre-start publication claim |
| Prompt coverage | PASS | Eleven complete seven-step sport/general workflows, eleven direct historical-recovery instructions and eleven inactive public Upcoming blocks. Local filled values remain separate |
| Preserved controls/evidence | PASS | 24 prior committed control copies and765 protected working hashes checked. Current card/grade/canonical continuity unchanged; no shared archive rows rewritten |
| Links / local inputs | PASS | 84 added/changed local link targets exist; public/local prompt differs only in3 original input edit areas |
| Publication | VERIFY AFTER PUSH | Exact reviewed paths, raw archival blob identity, source scope and staged diffs checked before commit; non-force push/fetched main readback recorded in a new receipt |

Source priority and routing mechanics are implemented; tests do not certify source truth, historical known-at assertions, coverage for every competition, calibration or predictive gain. No new live source availability claims, automatic fetch schedule or bulk historical collection. Current same-day/known-at and unsupported-format limits remain. Required/changed link targets and local/public byte identities are checked in the custody/publication step.
