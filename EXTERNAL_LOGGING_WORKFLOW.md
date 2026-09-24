## 2026-09-12 archival and reconciliation amendment
> **Current revision — CR-2026.09.21-3:** METHOD **MDS-2026.09.19-v4.3** is the workflow/template authority; **SCORING_AND_VALIDATION.md** controls conditioning, exact scoring, event-level evaluation and prospective evidence. All existing logs remain LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE. NUMERICAL_PROGRAM controls authorized implementation scope and actual build state; MODEL_IMPLEMENTATION_RECIPES contains the executable Markdown reference. Older dated policy blocks are historical where inconsistent. No source, dataset or model is approved/fitted by this banner.




Current authority: **PREDICTION_LOG_COMBINED_5.md**. Part 4 is closed at P-481; Part 5 is the active queue / next-ID authority, with P-482 next at the rollover snapshot. Determine the next ID from the current Part-5 snapshot and `GAME_LOG_STATUS_CURRENT.md`, not from an older hard-coded queue statement. GAME_LOG_STATUS_CURRENT.md enumerates canonical/local/temporary records. Before assigning IDs, compare mini variants with canonical issued rows. Preserve source text and hashes; append missing content and dated corrections, never duplicate a known event because its mini filename differs. Archive imported raw minis in archive/mini_logs. Archive filenames may retain old pending labels; only the current register controls state.


Record live items with source and UTC retrieval time and move to the next event. Track unresolved result/field tasks as TMP-OPEN and missing historical adjudication documents as TMP-AUDIT. Retire each only on its own evidenced completion, retaining alias history. All current material is LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE. New learns belong in the relevant event table and sport rule, with cross-sport process corrections also in RULES_GENERAL and LEARNING_REGISTER.


# External logging workflow — generate, settle, promote


Status: **ACTIVE — operational**
Created: **2026-09-04**
Owner process: this sits under [AGENT_ROLE_AND_TASK.md](AGENT_ROLE_AND_TASK.md) and [RULES_GENERAL.md](RULES_GENERAL.md); [UPCOMING_GAME_RESEARCH_GUIDE.md](UPCOMING_GAME_RESEARCH_GUIDE.md) is the per-event procedure. Where any of them conflict with this file, they control.


This file holds the three prompts for the operator's chosen working cycle:


1. **Generate** — an external chatbot session produces pre-result forecast cards into a running mini-log.
2. **Settle & retrospect** — a repository session settles every finished event and runs the retrospective.
3. **Promote & archive** — a repository session folds the audited lessons into the rule/reference docs, appends the mini-log to the combined log, and archives the raw file.


---


<!-- THREE-SOURCE-TIME-GATE-2026-09-19-CR4 -->
## Universal source/time/status workflow — CR-2026.09.19-4


Before creating, refreshing, moving or settling any game-log entry:


1. obtain **at least three independent reliable upstream source lineages** for the exact event; duplicates/mirrors/syndication do not count separately and search snippets/generated summaries do not count;
2. verify official venue-local date/time and IANA timezone, then convert timezone-aware to `Australia/Melbourne`, recording AEST/AEDT and any calendar-date rollover;
3. compare the verified time with the user-supplied estimate and print any correction;
4. re-check event state across the qualifying sources immediately before issue/refresh;
5. for settlement, require three independent sources to agree on exact event/date, explicit terminal state and final result; any credible live state or material conflict keeps the event unresolved;
6. immediately before a Drive status write, re-check finality, then read the log back after writing.


Use fail-closed labels from CONTROLS when any requirement fails. P-469 is the reference false-final incident.


## 0. Constraints that make or break the cycle — read before using the prompts


1. **Record the freeze basis.** The user confirms all existing non-live cards were frozen pre-game; apply PERFORMANCE_ELIGIBILITY_POLICY.md and retain their original ranks. Preserve source hash, import time and issue horizon separately. An earlier local git commit is not required for this confirmed history. Future snapshots are recommended, and live-issued views remain separate.
2. **Self-generated slates are `SYSTEMATIC_UNIVERSE`, not `USER_SUPPLIED`** (UPCOMING_GAME_RESEARCH_GUIDE.md §6). The operator pre-declares, once and in writing: the book/source, the market families carded per sport, any fixed alternate-line grid, and the universe freeze rule — then applies the **same grid to every event**. Choosing lines per game by how they look is selection bias and voids performance eligibility for the whole log.
3. **Market-blind.** The book's odds are recorded as metadata with a capture time and **never enter the forecast or the rank** (RULES_GENERAL.md §4 bookmaker-independence hard gate).
4. **Outcome targets are not process instructions.** "At least one over/under should win" and "the top two should win" are goals for the *method*, not steps a forecaster may follow — following them means narrative-fitting and hedging, which the framework forbids (AGENT_ROLE_AND_TASK.md §7; RULES_GENERAL.md §5 outcome-conditioned audit). The cycle channels that intent the only honest way: the settle-and-retrospect step gives **deep scrutiny to every Rank-1 loss, every Rank-2 loss, and every event where both total rows were mis-ranked** (now a standing instruction in RULES_GENERAL.md §9), and checks whether the component budget and corridor were honestly built — it never tells the forecaster to favour a total or a particular side.
5. **One event is a candidate, never a weight** (RULES_GENERAL.md §9; `G40`). The promote step may edit **reference material** directly (actual sport/competition rules; source cards) and may add **`TESTING`-status candidate rows** to LEARNING_REGISTER.md. It may **not** change any `SFA-<SPORT>` control, scenario weight or ordering rule from a single cohort — that needs the LEARNING_REGISTER.md §5 promotion procedure and the full test manifest.
6. **Volume vs. standard.** A framework-compliant card is 20–45 minutes of genuine work, and the **bottleneck is settlement + retrospective, not generation** — every card produces settlement work plus a grade, and at a ~45–55% contract loss rate roughly half of them spawn a deep retrospective (Rank-1, Rank-2, or a mis-ranked total). Guidance:
   - **Target ~10 events per day, deliberately rotated across sports** so the ~30-per-priority-slice requirement fills. At that rate: 60 clean units in ~6–8 weeks, ~150 balanced in ~4–5 months.
   - 5–10/day is comfortable and sustainable. 15–20/day is doable in bursts but settlement quality slips — keep it occasional. **Above ~20/day is counterproductive:** shallow cards settle `PROCESS_DEFECT`/`INCONCLUSIVE` and are quarantined from every performance measure (`G39`), and rubber-stamp retrospectives teach nothing.
   - **Coverage beats count.** Eight low-correlation cross-sport events are worth more than 20 games from one league's slate — both for effective sample size and for slice coverage.
   - A single day's 100 events are heavily correlated (one weather system, one news cycle), so their effective sample size is a fraction of 100. If the operator wants genuinely higher volume, that requires a separately documented "fast card" method with its own lower eligibility tier — a deliberate decision, not just working faster.
7. **Simultaneous events are fine — card them together, do not serialise.** Two (or more) events kicking off at the same time are all pregame when carded, so the "settle finals before the next card" gate (`RULES_GENERAL.md` §2) is not triggered; card them all, commit before their shared start, settle them all afterward. Waiting for the first to finish forfeits the clean card on the rest. Two constraints: (a) same-league same-day cards are **not independent data points** — shared weather, news cycle, officiating pool and fatigue patterns mean a systematic misread on one usually repeats on the other, so the eventual process review treats closely-correlated same-day same-league cards as partially dependent (`G9` lineage principle), and a shared source counts once across both; (b) if a cluster of simultaneous starts is larger than what can be taken through the full standard before first pitch, card what you can and put the rest in the eligible-but-unselected list with reason "insufficient time before start" — never rush a half-card.
8. **Historical ranking eligibility is active for user-confirmed non-live cards.** Score identifiable settled picks under their issued method, including failed process. Numeric probabilities, fitted-weight improvement, calibration and edge require their own evidence.
9. **Governing-doc currency.** Every session — generating or repository — must read the **current** governing documents fresh at the start (RULES_GENERAL.md §1, `G0`). An external session with no repository access must be handed the current files (from the synced Google Drive or pasted in), never a remembered or months-old copy. The P-268/P-270/P-271 stale-method finding is the evidenced reason this is a gate, not advice.


---


## 1. Prompt — GENERATE (run in the external chatbot session)


> **Start a new running forecast log.**
>
> **First, read — in full, this session — the current governing documents** (from the synced Google Drive copies; do not use a remembered or older version, and tell me the method version string you actually read):
> `AGENT_ROLE_AND_TASK.md`, `RULES_GENERAL.md` (especially §3 competition-rules currency, §4 sources/bookmaker-independence, §5–6, and §11 `GFA-2` steps `G0`–`G40` with the §11.9 mandatory card checklist), the relevant `RULES_<SPORT>.md` for each sport I ask about **including its "Sport and competition rules reference" section** (§9, or §10/§11; and `LEAGUE_RULES_CRICKET.md` / `LEAGUE_RULES_SOCCER.md` for those two), `MODEL_AND_DATA_SPEC.md`, `ALGORITHM_PORTFOLIO_AND_EVALUATION.md`, `NUMERICAL_TRAINING_SPEC.md`, `UPCOMING_GAME_RESEARCH_GUIDE.md`, `DATA_SOURCE_REGISTER.md`, and the `PROMOTED` plus relevant `TESTING` rows of `LEARNING_REGISTER.md`.
>
> **Slate policy — this is a `SYSTEMATIC_UNIVERSE` (self-generated) log.** Use exactly this pre-declared grid for every event, with no per-game additions or removals:
> - **Book / odds source:** [operator fills in — e.g. "TAB (Australia)"].
> - **Market families per event:** head-to-head / moneyline (both sides); the main handicap (both sides — run line ±1.5 for baseball, the main point spread for basketball/gridiron/AFL/NRL, the main Asian handicap for soccer, the main game/match handicap elsewhere); the main game/match total (Over and Under). [Add here any fixed alternate grid you want, e.g. "+ total ±1 unit"; otherwise state "main lines only".]
> - **Universe freeze:** record the freeze time; keep a short list of events that were eligible but not carded and why.
>
> **For each event, run `GFA-2` end to end** with the sport's `SFA-<SPORT>` content, and produce the full card in the canonical schema (`MODEL_AND_DATA_SPEC.md`, and the card structure used throughout `PREDICTION_LOG_COMBINED.md`). Every line of the §11.9 mandatory card checklist must be present, including **line 1a** (the reference section consulted with its review date; and, if this is the first card of a new season / pre-season / tournament edition for a competition, the field-owner rules-currency re-check with its source and date; and, if the competition has never been forecast before, its full rules written out first).
>
> **Market-blind.** Record the book's odds and the capture time for every row as metadata only. They must not influence the forecast or the rank in any way.
>
> **Sources.** For every decisive fact, record the exact source (URL or record), the owner, the observed/accessed time, and an `OPENED` / `SNIPPET` / `ASSUMED` tag (`RULES_GENERAL.md` §4). End each card with a "Sources" block listing every source used with its tag. Prefer field-owning official sources and the providers approved in `DATA_SOURCE_REGISTER.md`.
>
> **Rank every valid unresolved supplied row** by marginal win likelihood and robustness — unique ranks, no `PASS` to avoid ranking; use `FORCED RANK` with low evidence for weak rows. Name one **potential winner** with its exact endpoint (regulation / eventual winner incl. overtime-extra-time-extra-innings / advance).
>
> **Do not settle results and do not write retrospectives** — those are done later in the repository. Your output is pre-result cards only.
>
> **IDs.** Use local running IDs `RL-<YYYYMMDD>-NN`. Canonical `P-###` numbers are assigned on import.
>
> **Pending section.** Keep a section titled `## PENDING SETTLEMENT` at the **top** of the running log listing every event that has not started, is live, or is awaiting an official final. An event stays there until it has an official final; it is then moved into its ID-ordered place in the body (with the settlement fields left blank for the repository step).
>
> **After every batch, output the COMPLETE updated running log as full text**, and state the UTC time of that output, so I can save it and commit it to git before the events start.
>
> **Volume and balance.** Card [operator sets a number — recommended 8–15] events this session, spread across sports/markets/horizons. Do not exceed what you can take through the full process; a shallow card is worse than no card.
>
> **End of session,** restate: the complete running log; the `PENDING SETTLEMENT` list; the method version you read; and a one-line flag for any competition that is at a season/edition boundary or is being carded for the first time (so the repository session verifies its rules).


---


## 2. Prompt — SETTLE & RETROSPECT (run in the repository)


> Here is a running forecast mini-log generated in an external session. **Do not change any card's forecast text.** Settle it and run the full retrospective.
>
> **First, read the current governing documents fresh** (the §1 list in `RULES_GENERAL.md`), then read `PREDICTION_LOG_COMBINED_2.md`'s top controlling snapshot and note the next canonical `P-###`.
>
> **Fingerprint the supplied file:** filename, byte size, SHA-256 and first local observation time. Separately record issue horizon and provenance basis. Apply USER_CONFIRMED_PREGAME_FREEZE to the existing non-live history. Do not infer late forecasting from late importing.
>
> **Produce, first, a numbered list of every event in the log from the first**, with: local ID, proposed canonical ID, sport, competition, event, scheduled start (with timezone), and current state — `PENDING (not started)` / `LIVE` / `FINAL`.
>
> **Then, for each event in ID order:**
> 1. Verify the current state from field-owning / high-quality current sources. If it is **not final** (pending or live), leave it in the `PENDING SETTLEMENT` section, do not grade it, record its state and the check time, and move to the next event.
> 2. If it is **final**, run the complete settlement protocol in `UPCOMING_GAME_RESEARCH_GUIDE.md` §16: settle every contract field by field from the official final and the named statistic provider, preserving any conflicting provider values and their lineages. Record the settlement in the log's table format.
> 3. Grade **outcome and process separately** using the four honest verdicts (`G37`): result-right/process-right, result-right/process-different, result-wrong/process-broadly-right, result-wrong/process-wrong. Do not fit a story to the result.
>
> **Deep retrospective — mandatory for:** every **Rank-1 loss**; every **Rank-2 loss**; every event where **both total (over/under) rows were ranked on the wrong side of the result**; and every card graded `PROCESS_DEFECT`. For each, use the retrospective table from `RULES_GENERAL.md` §5 / `MODEL_AND_DATA_SPEC.md` (`Preissue expectation | Actual driver | Difference | Knowability | Process grade | Defect class | Lesson/test | Method change`). For the total-row cases specifically, check whether the component budget (`G20`) was honestly solved at the opponent floor / centre / high, whether the corridor was too narrow, and whether an Under was ranked above its Over without discharging the sport-file burden.
>
> **What went right.** For every audited event — wins included — record what went right and the **mechanism** behind it, so a working read is reinforced, not only failures examined.
>
> **Address pre-game errors head-on.** If a card's analysis contains a mistake (identity, a stale source, a mis-solved budget, a missed branch, a wrong rules assumption), name it explicitly and research the fix comprehensively. Do not paper over it.
>
> **Sources review.** For every decisive fact, was the source field-owning / high quality? Flag any source that proved stale or wrong. Search for a better source where one is plausibly available, and list any new high-quality source that meets the `DATA_SOURCE_REGISTER.md` §4 bar (access/use terms, coverage, definitions, known-at provenance) as a candidate addition.
>
> **Link to prior lessons.** For every finding, state whether it confirms, extends, or contradicts an existing `LEARNING_REGISTER.md` entry (`L-###`), a recurring-mistake-registry item (`M1`–`M9`), or a prior retrospective — cite the ID.
>
> **Output:**
> a. the settled log in the table format, plus the updated `PENDING SETTLEMENT` list;
> b. a detailed **"why each pick went right or wrong"** section, linked to prior lessons;
> c. a **candidate-learnings list** — each with a proposed disposition: `REFERENCE-DOC EDIT` (an actual sport/competition rule), `SOURCE-REGISTER EDIT` (a new/changed source), `LEARNING_REGISTER TESTING CANDIDATE` (a process/algorithm hypothesis, with its preregistered test), or `NO CHANGE`.
>
> Implement substantiated identity, source, arithmetic, role, phase-budget and reasoning-completeness repairs in the relevant sport rules and learning register. Keep original forecasts intact. Test proposed coefficients/weights on later cases; do not claim that an observed historical outcome validates a newly designed rule.


---


## 3. Prompt — PROMOTE & ARCHIVE (run in the repository, after step 2)


> Using the candidate-learnings list and the settled mini-log from the retrospective session:
>
> **First, read the current governing documents fresh.**
>
> **Apply each candidate learning to its correct home:**
> - **Actual sport/competition rule** (format, overtime, tiebreak, roster/import limit, promotion/relegation, a settlement quirk) → edit the relevant `RULES_<SPORT>.md` "Sport and competition rules reference" section, or `LEAGUE_RULES_CRICKET.md` / `LEAGUE_RULES_SOCCER.md`, directly; bump its "last reviewed" date.
> - **New or changed information source** → add or update its card in `DATA_SOURCE_REGISTER.md` with every §4 field.
> - **Process / algorithm hypothesis** → add a `TESTING`-status row to `LEARNING_REGISTER.md` with the hypothesis, the evidence case(s) from this cohort, the frozen comparator, and the preregistered chronological test. Implement justified completeness/validity controls now and mark PROMOTED_PROCESS. A predictive coefficient or scenario-weight change still needs the §5 chronological comparison; the same games that suggested it do not validate it.
> - **Cross-sport pattern** → only edit `RULES_GENERAL.md` / `GFA-2` if the pattern already clears the promotion bar from prior evidence; otherwise a single `TESTING` row that names every sport it may touch.
> - **General learning about the log itself** → a dated entry at the top of `PREDICTION_LOG_COMBINED_2.md`; a sport-specific one → the relevant sport section within it.
>
> **Append the mini-log to `PREDICTION_LOG_COMBINED_2.md`** as a new component section, in canonical-ID order:
> - assign the `P-###` numbers (reconcile against the snapshot's "Next canonical ID"; never reuse or renumber an issued ID);
> - add a provenance note: source filename, byte size, SHA-256, first-demonstrable git time, and the issue horizon, USER_CONFIRMED_PREGAME_FREEZE / other provenance basis, and settled-row eligibility per view;
> - append the raw cards, then the dated settlement/retrospective addendum from step 2;
> - in the **same edit**, update the combined log's component-order line and its **top controlling snapshot** (next canonical ID, open/pending queue, the descriptive ledgers, the clean-unit count toward the checkpoint).
>
> **Archive the raw file:** move the running-log file into `prediction logs/`, and add a row to the `README.md` document map describing it.
>
> **Update `MEMORY.md` / the memory files** only if a durable workflow or repo-structure fact changed.
>
> **Report:** list exactly which files changed and the one-line reason for each. Do not commit — that is the operator's step — unless explicitly told to. Re-state that the cohort carries no performance, edge or calibration claim and remains process-development evidence.


---


## 4. Running-log file — required shape


```
# Running forecast log <YYYY-MM-DD>


Method version read this session: <string from G0>
Slate policy: SYSTEMATIC_UNIVERSE — book <...>, market grid <...>, universe freeze <time>
Status: OPEN — pre-result cards only; settlement and retrospective done in the repository.


## PENDING SETTLEMENT
| Local ID | Event | Sport / competition | Scheduled start (tz) | State | Rank #1 | Potential winner |
|---|---|---|---|---|---|---|
| RL-YYYYMMDD-07 | ... | ... | ... | LIVE @ <time> | ... | ... |


## Settled-position body (ID order; settlement fields blank until the repo step)
### RL-YYYYMMDD-01 — <event>
<full GFA-2 card: identity + rules-currency (checklist 1a), frozen slate + geometry,
 reference base rates, baseline, regime mixture, recency block, environment block,
 exposure chain, joint object + scenarios, component & separation budgets,
 coherence, ranked rows, potential winner, final refresh, method version>
Sources: <every source, each tagged OPENED / SNIPPET / ASSUMED>
Odds captured (metadata only, not used): <rows @ decimal odds, capture time>
Settlement: <blank — repository step>
```


## 5. Cadence


- **Generate** as often as the operator can commit before events start (small batches, several times a day if the slate is spread through the day). Commit each batch to git immediately.
- **Settle & retrospect** at end of day, or per session — always settling every finished event before it goes stale, and carrying genuinely live events forward in the `PENDING SETTLEMENT` list.
- **Promote & archive** once a running log is fully settled (no events left pending), typically weekly, or when a log reaches a natural size.
- The framework's first process/ranking review is at **60 clean, demonstrably pre-result event units**; the sport-specific method-iteration review is at **~100–150 with roughly 30 per priority slice** (README "Path to performance-eligibility"). Count events, not cards or files.


## September 5 user confirmation — controlling eligibility correction


The user confirmed: **all existing game logs except views explicitly labelled LIVE were strictly frozen pre-game**. Accept this as the provenance basis `USER_CONFIRMED_PREGAME_FREEZE`, effective September 5. Non-live issued cards are eligible for historical qualitative directional/ranking evaluation. A late local import alone no longer excludes them. This correction supersedes earlier blanket `E1-Q-LATE_IMPORT`, “all non-performance-eligible” and “zero eligible historical units” statements. It records user confirmation; it does not assert independent timestamp verification or change original file times.


Keep four distinct fields: **forecast horizon at issue**, **event state when checked for settlement**, **provenance basis**, and **endpoint settlement status**. An originally pre-game card found live during settlement stays pre-game and awaits a final; it does not become a live-issued forecast. A live source/page, a “live counter-branch”, or a post-issue status check is not an issuance label. Explicit live or live-state-unverified issued views stay outside pre-game metrics. Original pre-game and later live views of one event must retain their own ranks and share an event cluster.


The headline historical scorecard includes all identifiable, genuinely issued, settled contracts/ranks in its stated cohort, including `FORCED RANK`, LOW evidence, and `PROCESS_DEFECT` outcomes. Do not remove a bad pick because its reasoning was poor. Process grade is a diagnostic column and a separately labelled compliance slice. No-forecast/no-action records are not trials; unresolved/void/push/partial rows have explicit denominators; materially unidentifiable contracts remain unscorable with the reason recorded. A row’s missing operator terms may limit ticket settlement without erasing a clearly defined research endpoint. Never use an issue-time row already decided as a predictive success.


Use the exact original pre-game order, including the latest genuinely pre-game refresh; never substitute a later live or retrospective order. Deduplicate aliases and group related targets/views by underlying event. Report historical performance by issued method, sport/competition, horizon and target. The ten newly settled cards are an evaluated v3.4 pre-game cohort. Earlier historical scorecards need those same row/view joins before a new all-history aggregate is reported; the complete status index is not itself a performance denominator.


Old games may measure their issued methods and supply development evidence for improvements. They cannot validate a v3.5/v3.6 change designed after their outcomes were seen. Keep the historical ranking count separate from each frozen challenger’s later test count. No probabilities, fitted coefficients, calibration or market-edge claims are created by this provenance correction. Future snapshots/hashes and externally timestamped revisions are useful provenance records; a local hash or editable git timestamp alone is not an independent timestamp authority, and no git-only approval gate is imposed on this user-confirmed history.


## Complete Markdown recording requirement


**Standing user instruction:** all audit changes, updates, learnings, rule changes, instructions and logs must be recorded in the Markdown documents. The `.md` set is the complete human-readable authority. Scripts, JSON and CSV are validation/data companions, not the only record of a decision.


For each future change, update the active prediction log, the specific sport rule document or RULES_GENERAL for cross-sport controls, LEARNING_REGISTER for disposition, and relevant method/source/workflow documents in the same pass. Append a dated, source-linked retrospective with original ranks, results, what went right/wrong, knowability, prior lessons and the exact adopted change. Record pending fields and live-at-first-check deferrals in the active queue. Preserve original issued cards and label superseding corrections. Document validation and link the changed Markdown files in the audit change log before delivery.


Current implementation: [September 5 audit change log](archive/audit_documents_implemented_2026-09-25/AUDIT_CHANGELOG_2026-09-05.md).


## Archival completeness — added 2026-09-06 (`G34.1` / `L-086`)


**A running-log component may not be archived, summarised or superseded while any card inside it is still unsettled, unless that card's complete frozen ranked slate — every row, not only Rank #1 — is reproduced verbatim in the archived artifact.**


This is not a tidiness rule. On 2026-09-05(b), `archive/mini_logs/PREDICTION_MINI_LOG_11_P294_P305.md` was archived carrying only the mini-log's twelve-row summary table, which records each card's Rank #1 and potential winner and nothing else. Two of those cards, `P-304` and `P-305`, were still unsettled at the time. When they were settled on 2026-09-06 both Rank #1 rows won and both potential-winner calls were correct — but their rows #2 through #5 exist in no file anywhere in this repository and can never be graded. **Eight ranked rows were lost to an archival convenience, not to a forecasting error.**


Operationally, at the promote-and-archive step:


1. Before writing the archive artifact, list every card in the component whose status is not `FINAL / SETTLED`.
2. For each of those, copy the **entire frozen ranked slate table** — every rank, contract, verdict, evidence grade and reason — into the archive, verbatim, alongside the summary row.
3. Where a row was genuinely never written down, record it explicitly as `UNGRADABLE / ARCHIVAL_OMISSION`. **Never reconstruct an unrecorded frozen row from memory or inference; that is fabrication, not recovery.**
4. State in the archive artifact that this check was performed, and for which cards.


The long-form per-card research prose may still be kept in the combined log's settlement addendum rather than duplicated in every archived component — that existing practice is unchanged. What may not be omitted is the frozen ranked slate of an unsettled card.


## 2026-09-06(f) — settlement and retrospective addendum


User-directed conflict handling: if a newly settled **distinct event** uses an already occupied canonical ID, preserve both originals and assign the new settlement a unique `TMP-SETTLED-<date>-<sequence>` reference in a separate bottom mini-log holding section. Record source Drive file/revision, event identity, conflicting ID and proposed later mapping; do not silently renumber the existing event or add the holding record to canonical aggregates before reconciliation. Same-event revisions and already documented component aliases do not require new IDs. This pass found no new conflict; P-318 remains next. [Holding section](archive/mini_logs/PREDICTION_MINI_LOG_SETTLEMENT_2026-09-06.md#newly-settled-logs-with-conflicting-canonical-ids--temporary-holding-section).


Frozen external source files may retain historical UNSETTLED labels. Keep their bytes, add a clearly linked dated settlement MD with per-game learnings, and update the canonical snapshot in the same pass. Drive was read only in this audit. Compare normalized text separately from byte hashes; a fresh local hash is not an independent pregame timestamp.


## 2026-09-09 — second temporary-ID namespace: `TMP-OPEN-<date>-<sequence>`


The `TMP-SETTLED-<date>-<sequence>` convention above solves exactly one problem: **an ID collision**, where a newly settled *distinct event* lands on an already-occupied canonical ID. That case has still never arisen (`P-318`–`P-332` and `P-333`–`P-344` both mapped one-to-one with no collision).


A different problem needed a handle, per user direction that *all* logs be trackable through to full settlement with full retrospectives: **an issued row whose settlement field has not been reached to standard.** Those rows are real, they accumulate, and until now they lived only as prose dispositions inside a queue table — recoverable, but not individually addressable. A second, deliberately distinct namespace is therefore opened:


> **`TMP-OPEN-<YYYYMMDD>-<seq>`** — a tracking handle for an **issued row that is not yet settled to standard**. It is **not** a canonical ID; it never enters the scorecard, never receives a W/L or a Brier score, and is **retired the moment the row settles or is declared terminal**, at which point the row is graded under its own canonical `P-###-C##` identifier. Its sole function is to guarantee that no unsettled row can be silently lost from the queue.


**Rules of use.**


1. **Never confuse the two.** `TMP-SETTLED-*` = an ID collision on a settled event. `TMP-OPEN-*` = an unsettled row on a correctly-numbered event. They solve opposite problems and must not share a sequence.
2. **A handle does not move custody.** A `TMP-OPEN-*` handle may be issued from the active log for a row whose canonical home is a closed archive — the handle is an index entry only. Custody, settlement and learnings stay with the row's own file. `TMP-OPEN-20260909-03` … `-11` index the nine still-open `PREDICTION_LOG_COMBINED_2.md` appendix rows; Part 2 remains the sole place they are settled.
3. **A handle is never a scorecard row.** It carries no probability and no result. A `PROVISIONAL` or `UNSETTLEABLE` disposition is unchanged by having a handle.
4. **Retrospective state is recorded alongside it.** For a partially-settled card, state which rows are fully retrospected and why the open row is not — an outcome retrospective is impossible where no outcome exists to standard, but the *process* retrospective (did the pre-registered settlement gate work?) is always completed. `P-341-C03` is the worked example: no outcome grade, but a complete and positive process retrospective.
5. **Every handle carries a concrete retry trigger where one exists.** A vague "retry later" is not sufficient; name the endpoint and the condition. `TMP-OPEN-20260909-01` names re-querying `soccer/uga.1` once ESPN rolls that feed to 2026-27 (verified 2026-09-09 as covered-but-stale at season 2025); `TMP-OPEN-20260909-02` records that no ESPN route exists for any Slovak competition after ten slug probes plus a core-directory check, so only an SFZ / Niké liga data-partner record can settle it.


**First issuance: 11 handles, 2026-09-09** — `-01` and `-02` for the two new `P-333`+ derivative corner rows, `-03` through `-11` indexing the inherited Part-2 appendix rows. Full table: `PREDICTION_LOG_COMBINED_3.md` §"Open queue — derivative rows awaiting a field-owning provider, with tracking IDs" and `GAME_LOG_STATUS_INDEX_2026-09-05.md` §"Every row still open across all three parts".


## 2026-09-11 — first collision handle; the carried-control list; the completeness block; a reconciliation-window breach


**1. First use of `TMP-SETTLED-<date>-<seq>`.** An external artifact issued the label "P-358" to an administrative no-forecast record (Fenerbahçe v Roma, start crossed); a later external log independently issued "P-358" to the Puerto Rico (W) v China (W) forecast. Only the latter was supplied. Resolution: canonical `P-358` = Puerto Rico–China (issued, documented, contiguous with `P-359`–`P-371`); the mini-log's own alias `TMP-CANON-20260911-01` is retired onto it; the unsupplied record takes **`TMP-SETTLED-20260911-01`** (final verified 1–1 at UEFA's feed; non-scorable; canonical ID deferred until its text is supplied). The external session invented a third namespace (`TMP-CANON-*`) instead of using this one — **external sessions must use `TMP-SETTLED-*` for label collisions and `TMP-OPEN-*` for unsettled rows, and nothing else.**


**2. The carried-control list must be complete and verbatim.** The `P-358` log's header listed `G-L7`, `G-L8`, `G-L2` and `G14.2` as carried constraints but **omitted `G-L1`**, and none of its thirteen cards executed the family table, width or normalised edge. From now on the GENERATE prompt (§1) requires the external session to paste **`RULES_GENERAL.md` §16.5(a)–(g) and §16.8 verbatim** at the top of its running log, and to end **every card** with the §16.8 completeness block.


**3. Settlement pass: run the audit.** The SETTLE & RETROSPECT step (§2) now runs `python audit_card_controls.py <running_log.md>` and records the result per card. A missing field is a process defect on that card (issued evidence stays immutable), and a cohort-wide pattern is itself a finding.


**4. Line-ups published before the freeze are retrievable.** `NOT_RETRIEVED` after a competition has published its line-up — a cricket XI once the toss is recorded, a baseball batting order, a soccer or rugby-league team sheet — is a `RETRIEVAL_MISS`, not an unavailability (`RULES_GENERAL.md` §16.8 item 7). `P-357` froze after the toss with "XI unresolved".


**5. The 24-hour window was missed.** The `P-345`–`P-357` log was on disk from 2026-09-10 17:37 AEST and reconciled at ~2026-09-11 23:50 AEST; a 2026-09-10 edit to the canonical log added only a dangling sentence. Practical remedy: when a settled external log is supplied, **reconcile it in the same session** before any new external forecasting continues; if a pass cannot complete, register the log's ID range and SHA-256 in the canonical snapshot immediately (the minimum §10 allows) rather than leaving a partial edit.


**6. Byte-preservation.** When a component is supplied as an attachment, check the user's Downloads folder for the same filename before reconstructing it. The 2026-09-09 pass reconstructed `P-344` although the original was on disk; it is now archived byte-exact.


## 2026-09-15 — three external running logs with user-directed ID starts; how they were reconciled


**What arrived.** Three external running logs (`P-373`–`P-389`, `P-390`–`P-406`, `P-407`–`P-423`), written on a read-only Drive by sessions that started at user-directed IDs, plus a byte-identical duplicate of the first. They reached this repository on 2026-09-15 and were reconciled the same session (inside `METHOD.md` §10's 24-hour window), although the first had been running since 2026-09-11.


**Rules applied (and now standing):**


1. **Fingerprint first; identical duplicates are one record.** SHA-256 each file; keep one copy of any byte-identical duplicate.
2. **User-directed ID starts are honoured; gaps are declared.** Issued labels become canonical when no collision exists. An ID skipped by every session (`P-372`) is recorded as **RESERVED / UNUSED** and never reused.
3. **Same event, two records.** When an external card and an existing handle refer to the same sporting event (`P-374` and `TMP-SETTLED-20260911-01`), the genuine pregame forecast is canonical and the other record is retired into it — never scored twice.
4. **Handles issued by an external session are adopted as issued** (`TMP-OPEN-20260912-01`, `TMP-OPEN-20260914-01`…`-06`); new ones continue the date sequence (`TMP-OPEN-20260915-01`…`-05`).
5. **Settle, then update the mini log itself, then append, then archive.** Each game's settlement and retrospective is written into that game's section of the mini log; the temporary-ID section and the general learnings/rule changes/sources section go at the bottom of the mini log; the relevant sections are appended to the active combined log; only then is the updated mini log archived (`archive/mini_logs/…_RETROSPECTIVE_SETTLED_<date>.md`), with the raw upload kept byte-exact alongside it. **No separate settlement document is created**, and no working files are kept outside the MD documents.
6. **Recompute before trusting.** Every Brier printed by the external session is recomputed (131 of 131 reproduced) and finals are re-verified at a field owner or structured feed.


**Workflow gap observed.** The external sessions kept Drive read-only and therefore could not see each other's IDs or this repository's P-364 settlement; log C still listed P-364 as live. Upload each running log to the Drive folder at the end of every session so the next session starts from the current queue.


## 2026-09-16 — a settlement variant of an already-imported log; handle-number collisions


**What happened.** Log C's raw upload (`…THROUGH_P423.md`, 218,707 bytes) was archived at 16:21 AEST on 2026-09-15. At 16:46 its external session wrote a settled variant to the Downloads folder: `PREDICTION_MINI_RUNNING_LOG_P407_P423_FULL_RETROSPECTIVE_2026-09-15.md`, 266,045 bytes, SHA-256 `f0c77cf8df3b9614422ceb5ad55b684835b3b0fdbe20c6be45fce5765214edc0`. The 2026-09-15(b) import never saw it. It was reconciled on 2026-09-16, inside `METHOD.md` §10's window (first available ~2026-09-15 16:46).


**Rules (standing):**
1. **Inventory every drop location each session** — Downloads, Desktop, the repository and a Drive `modifiedTime` search. Fingerprint every `PREDICTION_MINI*` file against `archive/mini_logs/` and all its subfolders. A size or hash with no archived match is an unimported variant, even when its ID range is already canonical.
2. **A variant never re-grades a canonical row by itself.** Compare its settlement fields row by row, and adopt only what is verified at a field owner. C′ agreed with every canonical final and W/L. Its one divergence — leaving P-408-C01 provisional — had already been booked at the Premier League record.
3. **Canonical handle numbers are never renumbered.** When an external session issues handles that collide with canonical ones (C′'s `TMP-OPEN-20260915-02`…`-06` point at different rows), record them as retired aliases in `GAME_LOG_STATUS_CURRENT.md`.
4. **External narrative facts are verified before entering a rule file.** C′'s claims were checked at ESPN, MLB statsapi and the NPB box. All were confirmed except P-421 ("tied 2–2 entering the eighth" — the Twins led 2–1) and slightly wrong P-408 possession and shot figures. C′ also correctly reported three things the canonical settlement had missed: P-408's red card, P-419's red cards, and RSSSF's 14 September Drukpa–RTC listing.
5. **Archive.** Keep the raw variant byte-exact in `archive/mini_logs/originals_2026-09-16/`, and the reconciled copy with its appended audit as `archive/mini_logs/PREDICTION_MINI_RUNNING_LOG_P407_P423_FULL_RETROSPECTIVE_RECONCILED_2026-09-16.md`.




## 2026-09-17 — a fully self-settled external mini log


**What arrived.** `PREDICTION_MINI_RUNNING_LOG_P424_P437_FULL_SETTLEMENT_RETROSPECTIVE_2026-09-17.md` (211,510 bytes, SHA-256 `b0b11de0d6eaba61a6f89f6a5e60e44f4de15804ba651859bbe41bc548092839`), covering `P-424`–`P-437` — the first external log to arrive already settled, with per-card retrospectives, a cohort audit and a document-update map.


**What the repository pass still had to do, and why it matters:**
1. **Integrity check before any write** — 14 IDs each used once, no collision with `P-001`–`P-423`, no duplicate events (`P-424` and `P-428` are distinct ETPL fixtures from `P-305` and `P-406`), one temporary handle.
2. **Independent verification of finals** — not delegated to the log. ESPN confirmed both ETPL scorecards (including the powerplay matchnotes) and all five ACLE finals with corner counts. The four KBO finals **could not** be verified and are recorded as carried, not confirmed.
3. **Recomputation of every printed Brier** — 52 of 52 reproduced, and every card mean reproduced.
4. **Settlement-rule enforcement over convenience** — the log left `P-430-C05` open although the evidence points to a loss; the repository kept it open for the same reason (§16.10(j)) rather than booking ESPN's count.
5. **Disposition of the log's own proposals** — its five candidate changes were checked against existing rules before promotion: two became cross-sport gates with recurrence evidence (`G-L17`, `G-L18`), one became an integrity gate on its own merits (`G-L19`), one was generalised from an existing basketball control (`G-L20`), and one (a probability cap) was **rejected** because the batch's own data did not support it.


**Standing rule confirmed:** a self-settled external log is still an untrusted narrative until its finals are re-verified and its arithmetic recomputed. It is a faster starting point, not a shortcut past `G-L13`.


## 2026-09-17(b) — a self-settled log whose own diagnosis was wrong, and what that changes


**What arrived.** `PREDICTION_MINI_RUNNING_LOG_P438_P451_FULL_SETTLEMENT_RETROSPECTIVE_2026-09-17.md` (171,419 bytes, SHA-256 `24e60bb35a068ea715b58fe5985239a7939334d80f6889fda16f23086bd14702`), covering `P-438`–`P-451`, already settled with per-card retrospectives and a document-update map — the second self-settled log, and the second in one day. Its pre-settlement raw upload, `PREDICTION_MINI_RUNNING_LOG_FROM_P438_UPDATED_P451.md` (116,470 bytes, SHA-256 `a1d98a39e2089bf68c10b00b0f4b5ec6fb82b3acc25bf80b9ee4336b213729bb`), is archived beside it. The two are not byte-identical and are not duplicates: the second is the settled variant of the first.


**The new finding, and it is the important one.** On 2026-09-17 the standing rule was *"a self-settled external log is an untrusted narrative until its finals are re-verified and its arithmetic recomputed."* That rule was satisfied by this log — **every final was correct and all 52 Brier values reproduced exactly**. And its central retrospective conclusion was still wrong.


`P-438` finished 3–2 against three ranked Unders. The log diagnosed "the card's early-phase centre was too low" and proposed carrying more early-goal mass. The structured feed, opened in this pass on the first call, says the opposite: **Kuwait SC took two shots in ninety minutes and scored two goals**; Al-Wahda took **41**; and **Kuwait's Marhoon was sent off in the 60th minute**, before the 87' and 90+7' goals that killed the remaining rows. The card's low-scoring process read was right; the loss was finishing variance on a two-shot base plus a disruption event. Acting on the log's diagnosis would have pushed the model to raise early-goal mass in exactly the low-process matches where it is least warranted.


**So the verification step is extended.** Re-verifying the *final* is necessary and not sufficient. An external retrospective's **causal claim** must be checked against the process record before any rule derived from it is promoted. This is now `G-L23` (`RULES_GENERAL.md` §16.13(c)) and the §16.8 block's new settlement field 10.


**What the repository pass did, in order:**


1. **Integrity check before any write** — 14 IDs each used once; no collision with `P-001`–`P-437` (the only prior `P-438` strings in the repository were four "next canonical ID" pointers); no duplicate events; no temporary prediction IDs; states classified (12 graded, 1 `NO ACTION`, 1 blocked).
2. **Independent verification of every final from a raw record** — `statsapi` for all eight MLB games **plus inning-by-inning regulation splits**; ESPN `afc.cup` and `uefa.europa` for the four soccer games with goal minutes, cards and shot counts; ESPN cricket series `1534175` for the CPL Eliminator including the innings order that determined whether the card had any active contract. First cohort in Part 4 with **zero** finals carried on narrative.
3. **Recomputation of every printed Brier** — 52 of 52 reproduced, all 12 card means reproduced, and the log's own 0.2097 cohort mean reproduced.
4. **Recovery of what the log left open** — the log recorded `P-451`'s result as unrecoverable. It was recovered by escalating to the rendering rung: `lnbp.mx/Dorados/team_results.html` is a JS-only field owner, not an unreachable one. Handle opened and retired in the same edit.
5. **Correction of the log's diagnosis where the evidence contradicted it** — `P-438`, above. The log's own proposed change was **not** adopted; three different rules were derived from the actual mechanism instead.
6. **Derivation of base rates the log asserted qualitatively.** The log wrote "print `P(tie after 9)` beside integer totals" and "the Coors upper tail was too low" without numbers. Six `statsapi` calls over the 2026 season (n = 2,286) turned both into printed identities, and surfaced a third defect the log did not see at all: **every favourite −1.5 row compressed the one-run band to 14–19% against a league 23–28%**. → baseball controls 34–37.
7. **Disposition of the log's five candidate changes** — three were reinforcements of rules that already existed and had not been executed (`G-L17`, `G-L18`, control 22); one (early-goal mass) was **rejected** on the process evidence; one (`P(tie after 9)`) was **promoted with a number** rather than as prose.


**Standing rule, revised.** A self-settled external log is a faster starting point, never a shortcut past `G-L13` — and now, never a shortcut past `G-L23` either. **Verify the final, recompute the arithmetic, and check the causal claim against the process record.** A log can be completely accurate about what happened and still be wrong about why, and it is the "why" that becomes a rule.


### Addendum, same pass — what the restored completeness audit revealed about mini-log *structure*


`audit_card_controls.py` did not exist at the repository root when this pass began, although §16.8 and this document both instruct running it. It was rebuilt and run over both of the day's mini logs. The per-card results are in `PREDICTION_LOG_COMBINED_4.md` §"2026-09-17(b)"; one structural finding belongs here, because it is a requirement on the **format** of an external log rather than on any card.


**An external mini log that carries only ranked picks plus settlement cannot be audited at all.**


| Log | Cards | Issue-time fields auditable? |
|---|---|---|
| `P-438`–`P-451` | 14 | **10 of 14** carried a full issued card body; `P-438`, `P-439`, `P-440` carried a *Ranked picks* table and nothing else |
| `P-424`–`P-437` | 14 | **0 of 14** — the log is settlement blocks only. Twelve cards register as missing every issue-time field, which is not a finding about those cards; it is the absence of their text |


The distinction matters because the two produce identical-looking audit output and mean opposite things. A card that printed no outcome-family table is a process defect. A card whose body was never transcribed into the mini log is an **unauditable record** — and silently scoring it as a defect would manufacture a finding, exactly the error `G-L23` guards against on the settlement side.


**Requirement, from this pass forward.** An external mini log submitted for import carries, per card, the **issued card body as issued** — the ranked table *and* the geometry, participant state, dependence and settlement-route fields that the §16.8 completeness block enumerates — not a picks summary. Where a card body genuinely cannot be reproduced, the log marks that card **`BODY_NOT_CARRIED`** so the audit records it as unauditable rather than as non-compliant. On import, run:


```
python audit_card_controls.py <mini_log.md> --settlement
python audit_card_controls.py <mini_log.md> --settlement --strict   # cards issued/settled after the 2026-09-25 manifest
```


and record the per-card table in the dated section, together with the count of `BODY_NOT_CARRIED` cards. A cohort whose completeness cannot be audited is still importable and still settles normally — but it may not be cited as evidence about the method's quality, because the method as written cannot be shown to be the method that was run (`PERFORMANCE_ELIGIBILITY_POLICY.md` §"2026-09-17(b)").




<!-- DEEP-RESEARCH-IMPLEMENTATION-2026-09-19-V42 -->


## 2026-09-19 version and source-policy reconciliation gate


External/mini logs may preserve the method/control version that governed an already-issued card, but the **next unissued card** must resolve the current root authority before issue. Under the current authority that is METHOD **MDS-2026.09.19-v4.3** and CONTROLS **CR-2026.09.21-2**. The CR-2026.09.19-4 event-verification gate remains an active component preserved inside the later revision.


- Do not rewrite a historical card from v4.0/v4.1 to v4.2; that would falsify the original information/control state.
- The active mini-log header must distinguish `historical_card_versions` from `governing_version_for_next_issue`.
- A version mismatch on the next issue is blocking (`PF-7`). Reconcile the header, manifest and current root documents before forecasting.
- Historical citations to now-prohibited betting/fantasy/DFS sources remain preserved as audit evidence, but their facts are not reusable prospectively unless independently recovered from a valid upstream source.
- External-log import must preserve forecast/distribution hashes and source-provenance receipts where available. Never infer missing timestamps or retroactively manufacture a preflight pass.




## 2026-09-21 all-sports audit-precedence note


For an unissued card, resolve audit conflicts through `archive/audit_documents_implemented_2026-09-25/AUDIT_RECONCILIATION_ALL_SPORTS_2026-09-21.md` before copying any older mini-log instruction. A later verified correction supersedes an incompatible older audit finding; a redundant finding is not re-added; and historical cards keep the method/control revision frozen at issue. This is a workflow/authority correction only and creates no predictive coefficient, probability cap or performance claim.


<!-- CONSOLIDATED-MINI-LOG-IMPORT-2026-09-23 -->
## 2026-09-23 — four mini-log files consolidated; two custody controls promoted

**What arrived.** The local `Mini logs (to be sent to actual log later)/` folder held four files:
- two receipt stubs (P-482-onward, P-484-onward);
- one WTA receipt stub (already merged by a peer session at about 21:10 AEST);
- the P-494-onward log (77,390 bytes, SHA-256 `aba5f510…87c7`).

The P-494 log in turn pointed at an external Codex attachment (the only full copy of the P-489 card) and at an out-of-repo Documents merged log (the only full copy of the P-484–P-488/P-492 settlements). Everything was archived byte-exact in `archive/mini_logs/originals_2026-09-23/`, then consolidated into `archive/mini_logs/Mini Prediction Log - P-487 to P-494 CONSOLIDATED - 2026-09-23/` and imported to Part 5 §"2026-09-23(c)". Live records were carried as-is to the new `Mini Prediction Log - P-495 onward - 2026-09-23/` (user direction).

**Two findings that change the import procedure.** Both are integrity controls with no forecast effect, promoted as PROMOTED_PROCESS (`LEARNING_REGISTER.md` L-20260923-01/02).

1. **`O-ID-DATE-STARTER-MATCH`.** Before labelling two records "the same event" (a reforecast, R1, a same-event view), print for both records:
   - date;
   - venue;
   - home/away;
   - starters, lineups or players.

   Any mismatch makes them separate events with separate IDs.
   - *Origin:* the P-489 card (22 Sep, Azuma v Muller) and its "R1" (23 Sep, Fukazawa v Nakachi) were merged. The merge created a false issue-horizon conflict, and it would have settled a 22 Sep card on a 23 Sep game.
2. **`O-EXTERNAL-ID-CLAIM-SWEEP`.** Every supplied transcript or attachment is scanned for embedded running-log ID tables.
   - Any ID/event pair not present in the repository is registered as `BODY_NOT_CARRIED` under a temporary ID.
   - It blocks promotion of any competing claimant to that ID until the operator resolves it.
   - *Origin:* P-487 = Dallas Wings @ Phoenix Mercury existed only in the P-488 and P-489 transcripts. A later NBL card claimed P-487, and the reconciliation recorded "no claimant".

**Two further checks added to the import checklist.**

3. **Pointer resolution.** Every "record location" pointer in a mini log must resolve to a file that actually contains the record.
   - *Origin:* the P-494 log said P-484–P-488/P-492 were "recorded in Part 5"; only custody rows were.
   - Out-of-repo files that hold the only copy of a record are archived in-repo at import.
4. **Concurrency.** Peer sessions wrote to Part 5, the status register and the mini log within minutes of one another on 2026-09-23.
   - Snapshot and hash the mini-log folder before an import.
   - Re-check modification times immediately before each write.
   - Never delete a file whose hash differs from its archived copy.

**Audit-script limitation (proposed tooling fix; not changed in this pass).** *— **Resolved 2026-09-25.** The segmentation now uses the `BEGIN/END VERBATIM ISSUED RECORD` markers, recognises `TMP-` IDs and level-5/6 headings, and ignores `## Entry N`. The real cause of P-494's false negatives was also fixed: the settlement-boundary regex treated the issue-time line "**Status:** UNSETTLED — LIVE-ISSUED VIEW" as the start of settlement text. Tests: `test_audit_card_controls.py`.*
- `audit_card_controls.py` opens a card at a `P-###` heading and closes it at the next `## ` heading.
- Cards whose fields sit under "## Entry 1 / ## Entry 2" (P-494), or in bold-label paragraphs (P-491), are reported as missing fields they visibly print.
- Record its output together with a manual field check (as in Part 5 §"2026-09-23(c)" F.1) until the segmentation is fixed.


<!-- AUDIT-2026-09-24F -->
## 2026-09-24(f) — a peer import whose finals were right and whose process record was invented

**What arrived.** At 22:47 AEST a peer repository session committed `cb95acd`. It:
- settled the P-495-onward mini log (TMP-G25 and P-493–P-508);
- archived the mini log;
- created the P-509-onward log;
- wrote six new rules into five RULES files.

The operator then asked for this pass, with the instruction not to settle live logs.

**What the verification found.**
1. **All 17 finals were right.** One grade pair was wrong: P-496 had its set scores reversed.
2. **The process record was largely invented.** In 14 or more of 17 blocks it is contradicted by the field owner: linescores, decisions, goal types, goalies, quarter lines, coaches, stat lines, game IDs, weather and a base rate.
3. **The rules were built on the invented narratives.** Six predictive rules were derived from those narratives and promoted from one game each.
4. **The summaries misstated the cards.** 13 of 17 status-register rows, and the learning-register and sport-file tables, misstated the issued ranks, lines or winners.
5. **Pointers and snapshot were broken.** The §"2026-09-24(e)" heading cited by every register row did not exist, and the Part 5 snapshot was not advanced.
6. **The cards were not appended.** The issued cards were never added to Part 5.

**The 2026-09-17(b) standing rule gets one more clause.**
> Verify the final, recompute the arithmetic, check the causal claim against the process record — **and read the process record from the feed instead of writing it.** A settlement can be right about every score and still invent the game.

**Import checklist additions (all now required).**
1. **`C-PROCESS-RECORD-PROVENANCE`.** Every process fact in a settlement block carries its endpoint and retrieval time. Unsourced causal facts make the block `PROCESS_RECORD_UNVERIFIED`, and no rule may cite it.
2. **`C-SUMMARY-FROM-CARD`.** Generate every register and summary row from the issued Field 4 table, then diff the summary against the card. A mismatch blocks the commit.
3. **`C-LINEUP-DIFF`.** At settlement, diff every card's named personnel against the official box.
4. **`C-PROMOTION-RECEIPT`.** No predictive rule enters a RULES file as `PROMOTED_PROCESS` from the games that suggested it. It enters as `TESTING`, with a prospective-test ID.
5. **Pointer resolution (2026-09-23 rule, re-applied).**
   - Every "§X" cited in a register row must exist as a heading.
   - The Part 5 snapshot's next ID must equal the status register's next ID.
   - Issued cards must be present in Part 5 (or explicitly `BODY_NOT_CARRIED`) before their settlement is summarised as "full records in Part 5".
6. **Leftover sweep.** Drive re-syncs can restore already-processed mini-log folders into `Mini logs (to be sent to actual log later)/`. On 2026-09-24 this happened with the P-482 and P-484 folders.
   - Hash each leftover against the archive.
   - If it is byte-identical, move it to `archive/mini_logs/originals_<date>/` with a receipt.
   - If it differs, verify that every event in it is already settled, then move it (never delete).

**Live-event handling (operator instruction, 2026-09-24).** P-509 was live throughout the pass. It is not settled and not retrospected, and it stays the only record in the active mini log. The audit added only a pre-settlement checklist (Part 5 §(f) part N), without touching the issued card text.


<!-- AUDIT-CLOSURE-2026-09-25 -->
## 2026-09-25 — audit closure: archive conditions and registration timing

These items were mapped by the 2026-09-22 cohort audit (§5 item 21) and the 2026-09-23 read-only audit (item 10) but never written here. Closure ledger: `archive/audit_documents_implemented_2026-09-25/AUDIT_CLOSURE_LEDGER_2026-09-25.md`.

1. **Archive a mini log only after canonical custody is verified.** Before a processed mini log moves to `archive/mini_logs/`, confirm each of these in the canonical files:
   - every issued card is preserved verbatim in Part 5, or explicitly `BODY_NOT_CARRIED`;
   - every row has its target-level settlement;
   - every required retrospective is written: Rank-1, `TOP_OU_REVIEW` and wins audited;
   - every unresolved handle is still tracked in the active mini log and the status register.

   On 2026-09-24 the P-495–P-508 log was archived while its cards were not yet in Part 5; they were appended by the §"2026-09-24(f)" audit (Appendix Z).
2. **Registration within 24 hours** (`METHOD.md` §3 step 7). This recurred on the P-482-onward log, registered about 35–39 hours after issue. It is an existing rule, so no new rule is added; this is recurrence evidence only.
3. **Commands for new cohorts:** `python audit_card_controls.py <log.md> --settlement --strict`, and for automated manifests `python prediction_preflight.py <manifest.json>`, which now accepts the optional `participants` object.

<!-- RESEARCH-2026-09-25 -->
## 2026-09-25(b) — settlement additions: receipts, z-scores and reference rows

Home: `RULES_GENERAL.md` §"2026-09-25(b)". These steps apply to every card settled after `CONTROL_MANIFEST_2026-09-25-2`.

1. **Process record from the receipt tool** (`C-RECEIPT-TOOL`, implementing `C-PROCESS-RECORD-PROVENANCE`). In lanes the tool covers, paste the output of one of these:
   - `python receipts.py settle mlb <gamePk> --card-away "…" --card-home "…" --card-sp-away X --card-sp-home Y`;
   - `… settle nhl <gameId> --card-goalie-away X --card-goalie-home Y`;
   - `… settle espn <sport/league> <eventId> --card-away "…" --card-home "…"`.

   The output carries the endpoints, the regulation score (for regulation-only contracts), and the `C-LINEUP-DIFF` lines. It is **one** terminal lineage; C-FINAL3's other two lineages are still fetched separately.
2. **z-scores** (`C-WIDTH-Z`). For each card that printed a centre and width, append `z_total = (actual − centre)/width` and `z_margin` to the settlement block. Add them to the `C-WIDTH-Z` manifest count for the card's family (`LEARNING_REGISTER.md` §"2026-09-25(b)" A).
3. **Reference rows at review.** A Rank-1 or `TOP_OU_REVIEW` retrospective states where the actual result fell against the §7 reference row. For example, "total 195: 0.89 card-SDs above the centre; the league 1H share was 0.51". This separates "unusual game" from "card far from population".
4. **Audit.** `python audit_card_controls.py <log.md> --settlement --strict` now also checks `WB`, `HC` and `10z`.

<!-- REPO-HYGIENE-CI-2026-09-25C -->
## 2026-09-25(c) — baseline ledger, branches and manifests at import and settlement

1. **Baseline ledger** (`C-BASELINE-SKILL`). For each settled card, append one row per decision to `SKILL_BASELINE_LEDGER.md` §"Prospective rows":
   - a forced pair once;
   - `Card p` copied from Field 4;
   - `Baseline p` exactly as the card printed `BASELINE_P` at issue;
   - the result W, L or P.

   Then run `python tools/skill_baseline.py` and paste its table into the settlement block. Cards that printed `BASELINE_P: NOT_YET_DERIVED` are listed as excluded, not scored.
2. **Branch per import or settlement pass** (`CONTRIBUTING.md`):
   - work on `session/<date>-<topic>`;
   - run the local checks;
   - open a pull request;
   - merge when the `checks` workflow is green.

   A direct commit to `main` is a process defect (`C-BRANCH-PR`). The `cb95acd` invented process record is the reason.
3. **Manifests.** If the pass edits any governance file, regenerate the receipt with `tools/make_manifest.py`, repoint `METHOD.md` and the active mini log, and confirm with `tools/verify_manifest.py`. The living logs (Part 5, the status register) are exempt from matching.
4. **Commands for new cohorts** (supersedes item 3 of §"2026-09-25"): `python audit_card_controls.py <log.md> --settlement --strict` (add `--allow-empty` for an empty active log), `python tools/skill_baseline.py` and `python tools/repo_hygiene.py`.

<!-- SETTLED-ROW-REVIEW-2026-09-25D -->
## 2026-09-25(d) — canonical settlement table and the 25-card review

1. **Canonical settlement table.** Every settlement block grades its rows in exactly this table, so the settled-row dataset rebuilds without heuristics:

   ```text
   | Rank | Contract | Family | p | BASELINE_P | Result | Brier |
   |---|---|---|---:|---:|---|---:|
   | 1 | Combined Total: Under 184.5 | total | 0.613 | 0.530 | LOSS | 0.3758 |
   ```

   - The card ID is in the heading or line directly above the table.
   - `Family` is one of: total, team-total, phase, handicap, moneyline, corners, prop, other.
   - `Result` is WIN, LOSS, PUSH or VOID.
   - `p` and `BASELINE_P` are copied from the issued card (`C-SUMMARY-FROM-CARD`).
2. **The 25-card review** (`SCORING_AND_VALIDATION.md` §14). Rebuild the dataset and report:
   ```bash
   python research/settled_rows_2026-09-25/extract_settled_rows.py
   python tools/calibration_report.py
   python tools/skill_baseline.py
   ```
   Paste the reliability table, Murphy decomposition, slope and the over-confident slices into the review. Update the `C-TRACK-RECORD` rows in `UPCOMING_GAME_RESEARCH_GUIDE.md` step 10 and `CURRENT_RULES.md`. Record the tests' progress (`T-PLUS-CUSHION`, `C-LOW-RESOLUTION-BAND`, `T-TOTAL-DIRECTION-LEAGUE`, `C-PROB-EXTREMITY`).
3. **No shrink, weight or cap** is ever derived from these reports (`L-087`). They drive labels, disclosures and tests only.
