# Verification ? online historical research release

Checks performed 16 October 2026 in LOCAL_WORKING_TREE on main, base 2ea94f6f718d1f43c7af9e567008495114ef9cef.

| Check | Result | Evidence / limit |
|---|---|---|
| Full workshop suite | PASS | `python -m pytest ml/tests -q`: 284 passed in 99.05 s, including the new missing-history-root regression. Earlier run before that fixture: 283 passed. These are synthetic/mechanical tests, not real sports/source qualification. |
| Focused history/execution regressions | PASS | history_retirement, web_history, execution: 49 passed in 53.96 s; reviewed web routing remains usable without archive discovery; invalid scope/hash/timing/unsupported inputs retain existing rejection gates. |
| Default discovery without store | PASS | config.discover() returned []; missing root is not created and get_league raises controlled KeyError, not filesystem failure. |
| All sports and workflows | PASS | Ten sport rule files plus NHL alias carry mandatory online/history-player notice. All eleven standalone prompt-1 workflows carry both obligations; zero old archive-reuse instructions or retired folder paths remain in that prompt. |
| Online process wording | PASS | Opened original sources, both sides' L5/L10/L15/L20, true n/short populations, row identities, independent-source comparison when needed, unresolved conflicts, publication/known-at/retrieval and market exclusions required. No arbitrary source-count guarantee. |
| Player confirmation | PASS | Exact-event starters/roles, selected bench/replacements, absences, source/time evidence and release/final recheck required; projected, missing, conflicting and postgame-only evidence never become pregame confirmation. |
| Protected historical records | PASS | SHA-256 comparison of 926 existing logs, active minis, issued originals, verification/report and model-shadow files: zero changes. |
| Prior operating snapshots | PASS | Base Git blobs preserved in archive/superseded_2026-10-16-3; RULES_NHL body retained exactly inside explicit wrapper markers to preserve its prior EOF blank. README snapshot verified against base; archive receipt has a distinct name. |
| Existing local work | PASS | .gitignore bytes unchanged and unstaged. Nine pre-existing prompt diff groups retain identical content after aligning the AVAIL version string; user event inputs remain unstaged, committed template staged separately. Unrelated config/editor files excluded. |
| Changed live local links | PASS | 58 newly introduced/changed local destinations checked; zero missing. Archived snapshots retain original relative context. Pinned historical Git source links do not certify current facts. |
| Results-folder removal | PASS | Original workspace path absent; recovery folder exists at C:/Users/danie/Downloads/SportsResearch-retired-results-2026-10-16. Git staging removes the tracked tree; no Git-history purge. |
| Source/profile/model claims | PASS | Store-derived profiles retired; no new sporting rows, baseline estimates, actual forecasts, model artifacts, IDs, outcomes or performance qualification claimed. Rebuild is a proposal only. |

Final staged scope, whitespace check, commit and remote readback are verified during publication. Current missingness/timing, research retention and exact-competition input gates remain. This release checks software/procedure/custody, not independent sports-source truth.

Final pre-publication checks: staged scope contains exactly 66,082 deleted entries, all under the retired tree, 52 modified active files and 61 new files (operating evidence/snapshots/rebuild plan/regression fixture). Zero unexpected staged paths or executable Python outside ml/. Default `git diff --cached --no-renames --check` passed; no whitespace exceptions used. Only .gitignore and pre-existing prompt input edits remain unstaged. Fresh fetch found HEAD and origin/main equal before commit.
