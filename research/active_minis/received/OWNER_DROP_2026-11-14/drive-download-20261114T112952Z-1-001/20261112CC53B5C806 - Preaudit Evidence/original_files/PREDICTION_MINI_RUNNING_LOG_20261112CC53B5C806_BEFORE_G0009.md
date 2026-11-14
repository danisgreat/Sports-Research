<!-- MINI-LOG-FORMAT: mini-log-10 -->
# Prediction Mini Running Log — 20261112CC53B5C806

## A. Authority snapshot

| Field | Value |
|---|---|
| Authority mode | `PUBLISHED_MAIN_PINNED` for repository controls; `CHAT_LOCAL_OWNER_OVERRIDE` for local-only delivery. **Not** `LOCAL_WORKING_TREE` or a repository-issued mini |
| Repository / branch / read HEAD | `danisgreat/Sports-Research` / `main` / `008cedc4ff469e7a808292aa3667a7bffe22e273` (GitHub connector, read-only) |
| Relevant working differences | `NOT_INSPECTED`: no access to the user's computer working tree; no GitHub mutations performed |
| Method / control / scoring / selection | `MDS-2026.11.11-v24.16` / `CR-2026.11.11-R4` / `SCV-2026.11.11-v13` / `SEL-2026.10.22-v4` |
| Subsequent records change | `CR-2026.11.12-R1`: no shared repository active mini; each research chat keeps its own distinct mini; forecast rules unchanged |
| Prompt suite / mini format | `P-2026.11.11-v24.14` / `mini-log-10` |
| Active Combined Log | `prediction logs/PREDICTION_LOG_COMBINED_9.md` (GitHub reference, not a local output) |
| Highest committed / next canonical ID | `P-638` / `P-639` (reference snapshot only, **neither allocated nor reserved**) |
| Outstanding local minis and keys | GitHub `research/active_minis/`: NONE (directory absent at pinned commit); external research-chat MINI_KEY inventory NOT_VERIFIED; this chat: this mini only |
| MINI_KEY / first local event key | `20261112CC53B5C806` / `LOCAL-20261112CC53B5C806-G0001` |
| New canonical ID / assignment stage | `NOT_ASSIGNED` / `PROMPT_4_IMPORT` |
| Issuing writer | This specific ChatGPT conversation. Writer restriction is local to this chat; **no enforceable GitHub lease acquired** |
| Lease start / lease expiry | Original chat-local initialization `2026-11-12T21:47:25+11:00` / `NOT_ESTABLISHED` (previous assumed 30-day expiry withdrawn) |
| Lease hand-overs | NONE; transfers require an explicit documented hand-over and exact latest mini snapshot |
| Frozen for settlement | NO; eight chat-local research draft cards; no repository issue/freeze |
| Reading receipt / opened at | See auditable reading receipt below; original initialization `2026-11-12T21:47:25+11:00`, reviewed `2026-11-12T22:49:11+11:00` |
| Mode | `LOCAL_MINI_STAGING` / `CHAT_LOCAL_ONLY` / `DRAFT_NOT_APPLIED` |
| Owner instruction | Keep all research, cards, revisions and mini snapshots in this conversation. GitHub is **strictly read-only**. Do not push, commit, create, edit or trigger workflows. |
| Repository file status | `NOT_CREATED` / `NOT_ISSUED` / `NO_REMOTE_FREEZE` |

**SPORTS_ONLY / MARKET_BLIND · RESEARCH_ONLY_NOT_CERTIFIED · CANONICAL_IMPORT_STATUS: PENDING**

**Authority exception:** Repository `WORKFLOW.md` and Prompt 2 normally require the repository agent to update `CURRENT_STATE.md`, commit and push a local working-tree mini. The owner's explicit chat-local/no-push instruction overrides those publication actions. Accordingly, this is an **audited chat-local draft**, not a repository-authorized issued mini. No commit time, model freeze, canonical import or prospective publication evidence is claimed.

### Reading receipt — verified GitHub `main`

- Repository: `danisgreat/Sports-Research`, default branch `main`.
- Pinned full commit: `008cedc4ff469e7a808292aa3667a7bffe22e273` (verified using GitHub branch metadata).
- Read through GitHub connector: `README.md`, `CORE.md`, `CURRENT_STATE.md`, `RULES_REFERENCE.md`, `WORKFLOW.md`, `CARD_AND_LOG_TEMPLATES.md`, `research/prompts/README.md`, `research/prompts/COMMON_OPERATING_PROTOCOL.md`, `research/prompts/2_START_LOCAL_MINI.md`, and `GAME_LOG_STATUS_CURRENT.md`.
- Sections applied: `CURRENT_STATE` 12 November R1 records change and current release; `WORKFLOW` Parts A/B; `CORE` sections 1–2 and associated model/source rules; `RULES_REFERENCE` Part A authority/mini/identity; `CARD_AND_LOG_TEMPLATES` §2; Prompt 2 read, reconcile, create, verify; Prompt index/common protocol.
- GitHub `research/active_minis/` returned NOT_FOUND (404); `CURRENT_STATE` explains the removal to `archive/retired_active_minis_2026-11-12/`. This does not prove any unseen external chat lacks a mini with the same identity.
- No owner local clone / local uncommitted controls were accessible; no comparison with local working tree claimed.
- Current state: method v24.16; current control R4; latest records change 12-Nov R1; prompt v24.14; mini-log-10; next canonical P-639 (unallocated).
- Mini initialization audit time: `2026-11-12T22:49:11+11:00` (Australia/Melbourne, AEDT).

## B. Local ID rules

The immutable local mini namespace is `20261112CC53B5C806`. The first distinct accepted event will be `LOCAL-20261112CC53B5C806-G0001`; subsequent new events advance sequentially (`G0002`, `G0003`, ...) **only after the corresponding complete card has actually been appended and read back**. Duplicate fixture requests, addenda, corrections, carryovers and model-shadow rows consume no new ordinal. Search native event IDs, competition, stage, date, reschedules, participants and archived/canonical aliases to avoid duplicates.

Canonical ID is `NOT_ASSIGNED` until an independently authorized settlement and prompt-4 import. The GitHub snapshot's next canonical ID is context only. Do not create a proposed `P-` identifier. Each event's model/shadow native IDs remain separate from local and canonical IDs.

Each new research event must retain the exact request, event identity, period/contract definitions, source URLs and field-level known-at times, verified lineups/benches/availability for both teams, historical L5/L10/L15/L20 where applicable, source alternatives/corroboration, reference calculation, adjustment ledger, sensitivity, distribution/masses, ranked contracts, explicit missingness and append-only revisions. An unsupported numerical assertion is labelled `NOT_ESTIMATED`, not filled. All per-game forecasts here are **chat-local and not GitHub-frozen**.

## C. Carryover and evidence queue

| ID | Event key | Queue | Original card / frozen pick table | Latest revision | Open field | Responsible actor | Next source + exact field | Due (ISO, tz) | Final-time basis | Last attempt | Scheduled automation |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Q-0001 | `LOCAL-20261112CC53B5C806-G0001` | PENDING_EVENT | Card G0001 (local draft, no frozen issue) | NONE | Verified completed score, actual start, retirement/WO terms | This chat, on next explicit result/settlement request | Official ATP results: complete set scores and status; corroborate second scoreboard | 2026-11-14T12:00:00+11:00 (triage target, not a scheduled action) | UNKNOWN; no verified first-ball or final time | 2026-11-12T23:55:32+11:00, schedule/state and R1 checked; no actual outcome verified | NO |

| Q-0002 | `LOCAL-20261112CC53B5C806-G0002` | PENDING_EVENT | Card G0002 (chat-local draft; unissued) | NONE | Actual puck time, verified final/regulation/OT score, starting goalies, operator full-game definition | This chat only on explicit follow-up | Pro Hokei match 131 protocol: official final and periods; corroborate Shaiba.kz; user operator terms if available | 2026-11-15T00:30:00+11:00 (triage only; no automated check) | UNKNOWN | 2026-11-13T00:29:59+11:00, official schedule and source check | NO |
| Q-0003 | `LOCAL-20261112CC53B5C806-G0003` | PENDING_EVENT | Card G0003 (chat-local draft, no official freeze) | NONE | Actual first ball, final set scores, retirement or match suspension status, contract operator settlement | This chat only on explicit result/settlement request | Stockholm official results and ATP match centre: final sets + completion status; second independent score feed | 2026-11-15T01:00:00+11:00 (triage only; no automated check) | UNKNOWN | 2026-11-13T01:10:58+11:00, draw, ranking, service/return and score-state checked; no outcome retrieved | NO |

| Q-0004 | `LOCAL-20261112CC53B5C806-G0004` | PENDING_EVENT | Card G0004 (chat-local draft, no prospective GitHub freeze) | NONE | Official final/OT box score, actual tip, late starters and injuries, native ID | This chat only on explicit settlement follow-up | Official WNBL Game Centre: final quarter and OT scores; confirm independent scoreboard | 2026-11-15T19:00:00+11:00 (triage only; no automatic action) | UNKNOWN | 2026-11-13T18:59:21+11:00, official Nov13 schedule/rosters, last five/four results, independent shadow executed | NO |

| Q-0005 | `LOCAL-20261112CC53B5C806-G0005` | PENDING_EVENT | Card G0005 (chat-local read-only research draft) | NONE | Official final, OT/quarters, real start, starting fives and Ellenson actual availability | This chat only on explicit user settlement follow-up | KBL official box/quarter scoring and active list; corroborate independent provider | 2026-11-15T21:00:00+11:00 (triage only, no scheduled task) | UNKNOWN | 2026-11-13T21:03:22+11:00, scheduled official fixture and pre-event reporting; no target result used | NO |

| Q-0006 | `LOCAL-20261112CC53B5C806-G0006` | PENDING_EVENT | Card G0006 (local shadow research, NOT issued) | NONE | Verified actual tip, official final and OT/quarters, active starters and bench | This chat on explicit result/settlement follow-up | Official B.League ScheduleKey 506581: final and all quarters, game status, lineup; corroborate both clubs | 2026-11-15T21:05:00+11:00 (triage only, not scheduled action) | UNKNOWN | 2026-11-13 ~21:08 AEDT: pretarget sources and injury notices; no target-game live score consulted | NO |

| Q-0007 | `LOCAL-20261112CC53B5C806-G0007` | PENDING_EVENT | Card G0007 (chat-local unissued qualitative research with executed exploratory shadow) | NONE | Actual puck-drop, full official match periods, starting goalies/skaters, exact operator OT/SO settlement terms | This chat only if user explicitly requests settlement | Czech federation game `3156` `https://czehockey.cz/game/detail/178203`: full-match final/periods/goalie TOI and actual start; corroborate official club page | 2026-11-15T22:00:00+11:00 (manual triage target only) | UNKNOWN | 2026-11-13 ~21:57 AEDT: pre-match 0:0 placeholder and official standings checked; further research after official scheduled clock without target result | NO |

| Q-0008 | `LOCAL-20261112CC53B5C806-G0008` | PENDING_EVENT | G0008 chat-local research draft (no remote issue/freeze) | NONE | Verified actual first serve/final sets/retirement; 13:00 CET order vs provisional clocks; initial fitness medical | This chat on explicit result/settlement request | ATP Challenger Orléans 2026 official quarterfinal Piros–Altmaier final sets, start/status; corroborate tournament match centre | 2026-11-15T23:00:00+11:00 (manual triage only; not automation) | UNKNOWN | 2026-11-13T22:58:23+11:00: draw, form, serve/return and no target score researched; no actual first serve verified | NO |

## D. Request intake

*Initial administrative review consumed no event ordinal. The first sporting request is recorded below; no canonical identifier is assigned.*

| Request key | Received (ISO, tz) | Event / alias as requested | Disposition | Card or addendum pointer, or no-card reason |
|---|---|---|---|---|
| INTAKE-0001 | 2026-11-12T23:44+11:00 (minute precision, user request received) | Dalibor Svrcina vs Otto Virtanen, Challenger Orleans, Round 2, 13-Nov 00:00 AEDT; Svrcina +0.5, Virtanen −0.5, O/U23.5 full-match games | READ_ONLY_DRAFT (new complete research card; non-repo, qualitative) | `LOCAL-20261112CC53B5C806-G0001`; `# NEW LOCAL EVENT CARDS`; no official forecast issue/freeze |

| INTAKE-0002 | 2026-11-13T00:29:59+11:00 (actual local research receipt, not message-arrival time) | Torpedo Ust-Kamenogrosk vs Arlan Kokshetau, Kazakhstan Open Champs, estimated 13-Nov-2026 00:30 AEDT; Torpedo −1.5 / Arlan +1.5 / total O/U6.5 | READ_ONLY_DRAFT (research and shadow; no certified p_card) | `LOCAL-20261112CC53B5C806-G0002`; local complete A1–A9 card, first of two 12/13-Nov games only |
| INTAKE-0003 | 2026-11-13T00:59+11:00 (message-receipt minute, not issue) | Thiago Agustin (Tirante) vs Alexander Shevchenko, ATP Stockholm QF, 13-Nov-2026 01:00 AEDT (not-before); Tirante +0.5, Shevchenko −0.5, total O/U23.5 games | READ_ONLY_DRAFT (qualitative; exact-game shadow diagnostics only; scheduled start threshold reached) | `LOCAL-20261112CC53B5C806-G0003`, complete A1–A9; no certified p_card/issue/freeze |

| INTAKE-0004 | 2026-11-13T18:49+11:00 (request minute; not actual issue) | Geelong Venom(W) vs Perth Lynx(W), Australia WNBL, estimated 13-Nov-2026 19:00 AEDT; Geelong +6.5, Perth −6.5, combined O/U163.5 points incl OT | READ_ONLY_DRAFT (complete A1–A9 research, qualitative; separate 1.2m-run shadow) | `LOCAL-20261112CC53B5C806-G0004`, no certified p_card, repository issue or freeze |

| INTAKE-0005 | 2026-11-13T20:54+11:00 (request-time minute; user-provided context) | Wonju Promy vs Suwon Sonicboom, Korea KBL, 13-Nov-2026 21:00 AEDT; Promy −5.5, Sonicboom +5.5, total Over/Under 179.5 points incl OT | READ_ONLY_DRAFT (complete A1–A9 research, 1.2m shadow, no certified p_card) | `LOCAL-20261112CC53B5C806-G0005`; explicit research/issue and timing caveats |

| INTAKE-0006 | 2026-11-13T21:04+11:00 (request received near estimated start; minute precision from system time) | Kawasaki Brave Thunders vs Saga Ballooners, Japan B.PREMIER, 13 Nov 2026 21:05 AEDT; Thunders −9.5, Saga +9.5, full-game O/U169.5 incl OT | READ_ONLY_DRAFT (new complete A1–A9 card; actual tip unverified; 1.2m conditional shadow, no certified p_card) | `LOCAL-20261112CC53B5C806-G0006`; chat-local research and timing qualification |

| INTAKE-0007 | 2026-11-13T21:56+11:00 (user request minute, not issue time) | HC Motor České Budějovice U20 vs Liberec U20, Czech KB Extraliga juniorů, estimated 13-Nov-2026 00:30 AEDT (actual published 13-Nov 12:00 CET with conflicting cached club timing); Motor −1.5, Liberec +1.5, total O/U5.5 goals | READ_ONLY_DRAFT (A1–A9 research, post-scheduled-time; 1.2m shadow only; non-repo, no certified p_card) | `LOCAL-20261112CC53B5C806-G0007`, complete card in same local mini; no publication, canonical import, outcome view or formal freeze |

## Initialization audit — non-issued metadata correction

| Item | Audit result |
|---|---|
| Original snapshot | `PREDICTION_MINI_RUNNING_LOG_20261112CC53B5C806_INITIAL_SNAPSHOT.md`, 4871 bytes; SHA-256 `d53368a7bb6318646d023f24f034398f61a5d3d12e8e2c810016cdbf92493ae6` |
| Change made | Clarified current forecast control vs 12 November records revision; withdrew unsupported 30-day lease expiry; expanded reading, scope and custody receipt |
| New event / count change | NONE / zero events |
| Prior issued card text affected | NONE; zero cards existed |
| Model/reference computation | NOT_PERFORMED |
| Settlement / canonical import | NOT_PERFORMED |
| GitHub write / push | NONE |
| Audit timestamp | `2026-11-12T22:49:11+11:00` |
| Verification | File readback, single format/footer markers, zero-card counts, stable MINI_KEY / local key, unchanged initial snapshot — see creation receipt |

**Execution-manifest compatibility:** Template §2 retains an obsolete example manifest section, but current Prompt 2 and the common protocol explicitly say **no execution-manifest companion for a new mini-log-10**. None has been generated. Model receipts are event-specific when actual runs occur.

| INTAKE-0008 | 2026-11-13 evening AEDT (message time not independently recorded to seconds) | Zsombor Piros vs Daniel Altmaier, Challenger Orleans QF, est. 13-Nov 23:00 AEDT; Piros +2.5 games, Altmaier −2.5, combined Over/Under 22.5 games | READ_ONLY_DRAFT: new full research card, uncalibrated exact-chain shadow only; no formal primary p or GitHub issue | `LOCAL-20261112CC53B5C806-G0008`: A1–A9 complete with stated missingness; intake and footer updated |

# NEW LOCAL EVENT CARDS

*Cards are chat-local research drafts, not GitHub-issued. Preserve this card's original core in all later updates; corrections are dated addenda. No repository forecast freeze or canonical ID has been issued.*

<!-- BEGIN CARD LOCAL-20261112CC53B5C806-G0001 -->
## Card · LOCAL-20261112CC53B5C806-G0001 · Tennis / ATP Challenger Orléans · Svrčina vs Virtanen · 2026-11-12 CET

- **Local event key:** `LOCAL-20261112CC53B5C806-G0001` — `LOCAL_UNIMPORTED_EVENT`.
- **Canonical ID / assignment stage:** `NOT_ASSIGNED` / `PROMPT_4_IMPORT`.
- **Event / native ID / aliases:** 2026 Challenger Orléans 125 men's singles, second round (round of 16), Dalibor Svrčina (CZE) vs Otto Virtanen (FIN); Sofascore match `tJQbsxcec`; ATP tournament posting ID `2273` (draw reference); native event ID NOT_UNIQUELY_VERIFIED.
- **Authority:** `PUBLISHED_MAIN_PINNED` at `008cedc4ff469e7a808292aa3667a7bffe22e273`; `MDS v24.16` / forecast control `CR-2026.11.11-R4` / record update `CR-2026.11.12-R1` / prompt `P-2026.11.11-v24.14` / scoring `SCV-2026.11.11-v13` / selection `SEL-2026.10.22-v4`; CHAT-LOCAL owner override (no repository working-tree access, no GitHub writes).
- **Probability method / eligibility:** `UNCALIBRATED_QUALITATIVE` card with a separately executed `EXPLORATORY_SHADOW_NOT_PRIMARY` 750,000-match simulation. This shadow is **not** an executed GitHub `ml reference`/`pregame` run and is not the declared/frozen primary `ANALYST_PRIMARY_V1` probability. No validated numeric p_card is issued.
- **Learning record:** `LEARN_RECORD_INCOMPLETE`: dated recent-results evidence and relevant service data retained; no canonical LEARN-v2 feature/label pack or frozen repository WARM_START/FEEDBACK_LOSSES artifacts.
- **Future learning:** `PENDING_SETTLEMENT`, local sporting-result capture only; full acceptance depends on future independent evidence/timing/custody review.
- **Analysis status:** `UNCALIBRATED_QUALITATIVE`; supporting shadow numeric diagnostics are distinct and marked NOT_PRIMARY.
- **Timing:** owner requested estimated `2026-11-13T00:00:00+11:00` = `2026-11-12T13:00:00Z` = `2026-11-12T14:00:00+01:00`. Provider disagreement: Sofascore/TennisTemple `12:30Z` (23:30 AEDT), tournament-search listing `13:00Z` (midnight AEDT), Tennis Tonic `13:30 CET` (23:30 AEDT), another listing `18:30Z`. Official same-day signed OOP not verified. **Verified first-ball time: UNKNOWN; issue phase TIMING_UNVERIFIED; no representation of a pre-start repository-frozen forecast.**
- **Scheduled lead/band:** N/A: inconsistent times; no first-serve event confirmation. Last research/issue recorded `2026-11-12T23:55:32+11:00` (AEDT) in the file; run after some provider-advertised starts but before other provider-advertised starts.
- **Endpoint / definition:** best-of-three singles; total games across all completed sets, counting tie-break set as 7–6 (13 games), not tiebreak points; signed margin = Virtanen games minus Svrčina games. Svrčina +0.5 covers if Svrčina total games ≥ Virtanen total games; Virtanen −0.5 covers if Virtanen total games > Svrčina games. O23.5 = at least 24 games; U23.5 = no more than 23. No spread pushes for integer game totals; retirement/operator void terms NOT_VERIFIED and **must not be inferred** from sporting totals.
- **Distribution object:** `EXPLORATORY_SHADOW_NOT_PRIMARY`; game-by-game server-hold Monte Carlo with 7-point win-by-2 tiebreak at 6–6 in every set; three input scenarios of 250,000 independent best-of-three match paths, mixture weights 0.25/0.5/0.25. No model release, reference receipt, calibration or freeze.
- **Shadow expected score/moments:** mean completed games 25.46, SD approx 5.91 (scenario-SD weighted, not full-mixture total SD), signed Svrčina game margin -0.70; player-specific match game mean NOT_COMPUTED. No official p_card expected score or distribution.
- **Baseline:** `BASELINE_UNAVAILABLE`: no audited identical-line Challenger Orléans event-level cohort/reference distribution, no local released tennis model access and no certified league-only comparator generated.
- **Regime/context:** indoor hard, Challenger 125, no weather exposure (covered venue), both right-handed; Svrčina stronger recent W/L and return; Virtanen larger serve, higher indoor Elo per one source, more indoor-hard history. No first-meeting H2H adjustment. Player medical status/retirement/medical-timeout NEGATIVE_REPORT_NOT_VERIFIED.
- **Settlement capture plan:** later capture ATP/Orléans final set scores and event status independently from a second provider, determine game sum and margin, cross-check retirement/operator policy, retain final-time/source timestamps; no automation created.
- **Rules read/archive check:** GitHub `CURRENT_STATE.md`, `CORE.md`, `RULES_REFERENCE.md`, `RULES_TENNIS.md` §0 and §1, `CARD_AND_LOG_TEMPLATES.md` §2/§3, `research/prompts/1_GAME_CARD.md`, `research/prompts/2_START_LOCAL_MINI.md`, `GAME_REQUEST_TEMPLATE.md` §1b, `PROBABILITY_TOOLKIT.md` §6, `RESEARCH_PROTOCOL.md` and current sport sources; repository archive pack/source-audit execution NOT_AVAILABLE and not claimed.
- **Known-at:** all web source observations retrieved in this response around 2026-11-12 AEDT; sources sometimes use mutable live pages, so exact original publication/freeze of all stats is NOT_VERIFIED. Qualitative card not designated `CLEAN_PRE_START_INPUTS` because first-play timing uncertain; no known live score used in modelling.
- **Lineup state / issue step:** `CONFIRMED_DRAW_PARTICIPANTS` by 2026 tournament draw and first-round result; tennis singles has no lineup/bench equivalent. Availability `MEDICAL_STATUS_UNVERIFIED` for both; no fresh same-day official fitness certification.
- **Pricing basis:** `SHADOW_ONLY` scenario mixture not formal pricing. No frozen league reference / validated adjustment ledger, so card qualitative despite exploratory numbers.
- **Form windows:** research snapshots (completed **played matches** including retirement in win/loss as noted): Svrčina L5 4–1; L10 8–2; L15 10–5; L20 14–6 (10/06 Nishioka retirement counted W, not a full-game total). Virtanen L5 3–2; L10 6–4; L15 8–7; L20 10–10 (US Open qualifying Dimitrov walkover excluded from played n). L15/L20 reconstructed from TennisTemple match paths, NOT a dedicated independently audited data package. Surface-only history: Svrčina 2026 indoor-hard 5–1; Virtanen 12–6, from current Tennis Tonic preview (not L20 indoor-specific).

### Decision block

**Decision:** No high-confidence edge. Directional Rank 1 = Virtanen −0.5 **total games** on indoor-serve strength, but extremely scenario-sensitive; directional Rank 2 = Over 23.5 **total games** due to plausible deciding-set frequency and Svrčina's recent tendency to reach three sets. Both are `LOW_CONFIDENCE`, not calibrated probability picks; abstaining is justified.

| Rank | Role | Tag | Contract key / exact proposition | p_card | p_base | BASELINE_P | Line distance (units / z) | Probability basis | Main failure route |
|---|---|---|---|---|---|---|---|---|---|
| 1 | PICK (directional only) | SUPPLIED | `VIRT_GAMES_MINUS_0_5`: Virtanen games − Svrčina games ≥ 1 | NOT_ESTIMATED | NOT_COMPUTED | BASELINE_UNAVAILABLE | signed Svr margin mean −0.70 vs line −0.5; z NOT_VALIDATED | QUALITATIVE; exploratory shadow ~55.0% | Svrčina's return neutralises serve and Svrčina holds equal/more games |
| 2 | PICK (directional only) | SUPPLIED | `TOTAL_OVER_23_5`: completed total ≥ 24 | NOT_ESTIMATED | NOT_COMPUTED | BASELINE_UNAVAILABLE | exploratory mean 25.46 vs 23.5; z NOT_VALIDATED | QUALITATIVE; exploratory shadow ~53.5% | Virtanen controls two relatively short sets |
| – | INFORMATIONAL | SUPPLIED | `SVR_GAMES_PLUS_0_5`: Svrčina games − Virtanen games ≥ 0 | NOT_ESTIMATED | NOT_COMPUTED | BASELINE_UNAVAILABLE | NOT_VALIDATED | shadow ~45.0% | Virtanen's indoor first-strike patterns |
| – | INFORMATIONAL | SUPPLIED | `TOTAL_UNDER_23_5`: completed total ≤ 23 | NOT_ESTIMATED | NOT_COMPUTED | BASELINE_UNAVAILABLE | NOT_VALIDATED | shadow ~46.5% | deciding third set; long 7–5 or 7–6 sets |

**Baseline coverage:** 0/0 numeric primary rows (all primary p_card NOT_ESTIMATED). **Rank-1 gate:** NOT_ASSESSABLE, no compliant reference/league baseline. **Rank-2 floor:** NOT_ASSESSABLE. **Joint failure:** exploratory shadow `P(Virtanen−0.5 AND Over23.5)` NOT_COMPUTED; no issued joint metric. **Shadow RANK_DELTA / BASE_ONLY:** NOT_AVAILABLE. **Adjustment dependence:** UNTESTED for official card; exploratory serve-scenario sensitivity is MATERIAL. **Potential winner:** qualitative lean Virtanen; shadow P(Virtanen match wins) 57.3%, Svrčina 42.7% **NOT PRIMARY** (tennis games handicap != necessarily match win). **Supplied rows not selected:** Svrčina +0.5 and Under 23.5 retained as informational. **Model shadow (MLSCOPE-v3):** `NOT_RUN_NO_LOCAL_REPOSITORY_MODEL`; independent exploratory sim executed, with file/hash receipt below; no GitHub model shadow issued.

### Appendix

#### A1. Identity, timing and state

- Competition: ATP Challenger 125, Co'met Orléans Open 2026, Orléans France, indoor hard, singles best of 3, second round/round of 16 (synonymous here). ATP draw and tournament listing corroborate exact players.
- Original user request (preserved verbatim):

```text
Upcoming Tennis Match: Dalibor Svrcina vs Otto Virtanen, Challenger Orleans, Round 2,
Estimated Game Time Start: 13 November 2026, 12:00 AM AEDT (can be delayed so continue the process as normal)
Svrcina Handicap Games Spread: +0.5
Virtanen Handicap Games Spread: -0.5
Combined Total: Over/Under 23.5 Games
```

- Owner provided 13-Nov 00:00 AEDT, but at least two conflicting source start times exist. The latest exact same-day official OOP and verified first ball are missing. Issue-state `TIMING_UNVERIFIED`, `KNOWN_AT_UNVERIFIED`, and NO_REMOTE_FREEZE; cannot claim prospective eligible issuance. Web results did not provide an authenticated point-by-point current-state check.
- Home/away side NOT_APPLICABLE tennis singles; no venue home advantage, neither player French. Central Arena vs Court 1 labelling is conflicted among providers; both refer to Orléans event, court not verified.

#### A2. Exact supplied contracts

| Key | Exact expression | Sporting outcome convention | Operator/retirement status |
|---|---|---|---|
| `SVR_GAMES_PLUS_0_5` | Svrčina total games +0.5 > Virtanen total games | Games win-or-tie, NOT automatically match win | NOT_VERIFIED |
| `VIRT_GAMES_MINUS_0_5` | Virtanen total games −0.5 > Svrčina total games | Virtanen wins aggregate games by ≥1 | NOT_VERIFIED |
| `TOTAL_OVER_23_5` | sum of games >23.5 | ≥24 played games | NOT_VERIFIED |
| `TOTAL_UNDER_23_5` | sum of games <23.5 | ≤23 played games | NOT_VERIFIED |

No substitution of −1.5/+1.5 lines published by unrelated sources. No odds, vig, market prices or bookmaker-dependent numbers entered.

#### A3. Evidence and historical inputs

| Claim | Observed pre-event field | Source / publication / limits |
|---|---|---|
| Exact draw / round | Svrčina and Virtanen in round of 16, Orléans 2026 | ATP draw `https://www.protennislive.com/posting/2026/2273/mds.pdf` search extraction; document direct-open/visual audit unavailable; also `https://tennispadelscore.com/tournaments/orleans-challenger-2026/` independently lists R2 |
| Orléans surface, best-of-3 | Indoor hard / Challenger 125 | `https://pythiatennis.com/dalibor-svrcina-vs-otto-virtanen-prediction-and-stats/?d=2026-11-11`; `https://www.sofascore.com/tennis/match/dalibor-svrcina-otto-virtanen/tJQbsxcec` |
| Time variant A | 12:30 UTC (2026-11-12) | Sofascore and TennisTemple; ≡ 23:30 AEDT 12-Nov |
| Time variant B | 13:00 UTC (2026-11-12) | TennisPadelScore (cached update 12-Nov 00:17 UTC); ≡ 00:00 AEDT 13-Nov |
| Time variant C | 13:30 French local time (12:30 UTC) | Tennis Tonic 11/12 Nov preview; uncertainty remains |
| Rank | Svrčina 112, Virtanen 127 (ATP 2026 12 Nov preview) | `https://tennistonic.com/tennis-news/1080686/h2h-prediction-of-dalibor-svrcina-vs-otto-virtanen-in-orleans-challenger-with-odds-preview-pick-12th-november-2026/`; other real-time widget ranks disagree, no independent official same-day certification |
| Recent L5/L10 | Svrčina 4–1 / 8–2, Virtanen 3–2 / 6–4 | `https://tennical.com/h2h/svrcina-dalibor-vs-virtanen-otto/`; `https://en.tennistemple.com/player/dalibor-svrcina/results`; `https://en.tennistemple.com/player/otto-virtanen/results` |
| L15/L20 | Svrčina 10–5 / 14–6; Virtanen 8–7 / 10–10 | Independently counted game entries on above TennisTemple 2026 results lists, exclude Virtanen Dimitrov WO; count Svrčina Nishioka retirement as win for W/L but not completed total; all-surface, mixed level, no opponent adjustment |
| Indoor-hard 2026 | Svrčina 5–1 (6 played), Virtanen 12–6 (18 played) | Tennis Tonic match preview (different source reports 4–1/9–5; discrepancy likely as-of/source coverage) |
| 52-week indoor serving | Svrčina first serve in 56.0%, 1st serve pts won 75.2%, 2nd serve pts won 48.9%, SPW 63.7%, RPW 42.0%, n=5 with stats; Virtanen 62.6%, 77.3%, 54.3%, SPW 68.7%, RPW 35.7%, n=15 | `https://pythiatennis.com/dalibor-svrcina-vs-otto-virtanen-prediction-and-stats/?d=2026-11-11`; subject to small n; stats feed denominator points NOT independently retained |
| R1 results | Svrčina bt Vitaliy Sachko 2–6, 6–3, 7–6(6); Virtanen bt Dino Prižmić 6–1, 2–6, 7–6(2) on 10 Nov | Tennis Tonic match preview; `https://www.365scores.com/en-us/tennis/league/orleans-6931/brackets`; both played 3 sets, Svr 30 total games, Virt 28 |
| R1 serve/return | Svrčina: 4 aces, 7 DF, 55% first in, 5 breaks conceded, 4 breaks; Virtanen 11 aces, 6 DF, 55% first in, 2 breaks conceded, 3 breaks | Tennis Tonic R1 recap; sample one match each; both recorded more service pressure for Svrčina |
| Travel/workload | Svrčina Bratislava 3–7 Nov SF + Orléans 10 Nov R1; Virtanen Brest late Oct SF, Bratislava early Nov R2 + Orléans 10 Nov R1 | TennisTemple result paths; exact travel mode/distance not sourced, same 48h recovery from R1 |
| H2H | 0–0; no previous meeting returned | tennis tonic, Tennical, GameSetPredict match records |
| Injury/MTO/withdrawal | Both in R2 draw; no confirmed player-specific current injury/medical-timeout fact found in targeted queries | Availability UNKNOWN, not inferred healthy; exact check from player/tournament medical source not available |

**Match-specific mechanism:** Svrčina's 42.0% indoor RPW vs Virtanen's 68.7% indoor SPW implies Virtanen SPW may be depressed by Svrčina's return; Svrčina's 63.7% SPW vs Virtanen's 35.7% RPW gives more symmetric point matchup than raw season serve advantage alone suggests. A service point and match score are not interchangeable. H2H is zero, cannot extrapolate.

**Data conflict preserved:** Pythia reports 2026 indoor 5 scored matches vs 15 for 52wk; Tennis Tonic 2026 5–1 vs 12–6 and TennisExplorer older 4–1 vs 9–5. Different capture windows; no silent reconciliation or fabricated weighted evidence. ATP rank Pythia/Tennis Tonic 112/127 differs from Sofascore dynamic 119/116.

#### A4. Distribution and sensitivity — executed non-primary simulation

- Actual self-contained executable: `tennis_shadow_svrcina_virtanen_20261112.py`; SHA-256 `cfe13547f6ba81cc1b55f27ccccb08c50ec34715266d7337a41c4e40abe8fc36`.
- Actual JSON output: `TENNIS_SHADOW_DIAGNOSTIC_20261112CC53B5C806-G0001.json`; SHA-256 `c23673d09eef9fbd9f1a0061efb9af0084aa3abdf5a612eab119d2cb82d62ec4`.
- Sample: 250,000 independent complete matches per each of three input cases = 750,000; RNG seeds 41276/41277/41278; NumPy `random` + Numba JIT, executed locally on 12-Nov 2026, not GitHub source.
- Code computes service hold from Bernoulli service-point probability `p` using tennis game deuce formula, then simulates alternate service games/tiebreak-point service order across best of 3 full sets. Match-point point independence, no retirements, no dependence/correlation across games, no fatigue or skill variation across sets. This is **conditional** and incomplete, not an independently trained/validated tennis forecasting system.
- Raw matchup SPW starting point: Svrčina `(0.637 + (1−0.357))/2 = 0.6400`; Virtanen `(0.687 + (1−0.420))/2 = 0.6335`. These are crude arithmetic blends, not fitted or opponent-adjusted formal estimates. Indoor Elo favors Virtanen and 5-match Svrčina sample is exceptionally small. Scenarios below bracket plausible shifts but are not statistically estimated posterior bounds.

| Scenario (25% / 50% / 25%) | Point-win Svr serve | Point-win Virt serve | Hold Svr | Hold Virt | P(Virt −0.5) shadow | P(Over23.5) shadow | P(three sets) shadow |
|---|---:|---:|---:|---:|---:|---:|---:|
| Svrčina-return favorable (low Virt) | 0.645 | 0.631 | 0.821 | 0.797 | 0.405 | 0.544 | 0.495 |
| Base, indoor Virtanen advantage | 0.632 | 0.647 | 0.798 | 0.825 | 0.553 | 0.543 | 0.493 |
| Larger Virtanen indoor advantage | 0.620 | 0.663 | 0.776 | 0.850 | 0.686 | 0.511 | 0.462 |
| **Mixture — SHADOW ONLY** | — | — | — | — | **0.550** | **0.535** | **0.486** |

- Under 23.5 complement 0.465; Svrčina +0.5 complement 0.450. Shadow Virtanen match winner 0.573; Svrčina match winner 0.427. Games can tie even when one player wins sets: mixture ~0.048 of paths.
- **Cross-family sensitivity failure:** an external Pythia model (not card input) puts Under 23.5 at 58.2%, not consistent with this exploratory over lean, and other external tennis models disagree on favorite. These are *not* baseline p, calibrations or grounds to assert primary issuance. This reduces confidence; transparent model disagreement retained.
- Formal PRIMARY_PREDICTION_PROTOCOL reference/grid/feedback file runs: `NOT_RUN`; no valid WARM_START/model frozen reference receipt; no numeric primary probabilities.

#### A5. Contract universe, sporting W/P/L/V

| Contract | Shadow probability only | Current sporting grade | Decision |
|---|---:|---|---|
| Svrčina +0.5 total games | 0.450 | PENDING_RESULT | Alternative |
| Virtanen −0.5 total games | 0.550 | PENDING_RESULT | Directional Rank 1, unstable |
| Over 23.5 combined total games | 0.535 | PENDING_RESULT | Directional Rank 2, contested |
| Under 23.5 combined total games | 0.465 | PENDING_RESULT | Alternative |

- All four have 0 PUSH probability if match completed with integer total games; retirement/withdrawal may produce VOID depending on operator, whose terms are unknown. No observed outcome used, and no W/P/L/V final grade issued.

#### A6. Departure/adjustment ledger

| Mechanism | Evidence | Direction | Formal effect-table value | Primary shift |
|---|---|---|---|---|
| Virtanen indoor serve | 68.7% indoor SPW; 12–6 indoor; 11 R1 aces | Virtanen games/win positive | NONE (not frozen) | NONE — only scenario shadow |
| Svrčina return + current form | 42.0% indoor RPW; 8–2 L10; R1 4 breaks | Svrčina games, longer sets | NONE (not frozen) | NONE — only scenario shadow |
| Fatigue | Svrčina Bratislava SF 7 Nov, both R1 10 Nov in three sets | width, either direction | NONE (not frozen) | NONE |
| H2H | no previous meetings | no adjustment | N/A | NONE |
| Injury availability | current official medical status not established | mixed scenario uncertainty | NONE | NONE |

No released reference, formal effect size/ledger or unadjusted primary p to claim; do not double count the source components in an official primary distribution.

#### A7. Family checks / independent shadows

- Arithmetic: all shadow complement probabilities sum to 1 per simulation; a tennis game handicap is a game-margin outcome and is **not identical to match winner**. Tie-game margin occurs ~4.8% in the mixture and can decide the +0.5 side.
- Tennis format: best-of-three, tiebreak at 6–6, each tiebreak set contributes 13 games, not points; no match super-tiebreak expected in singles.
- Total 23.5 may depend strongly on set-count mixture. Independent men best-of-three population 3-set reference 35.8% per `RULES_TENNIS.md`; shadow ~48.6% for close rating/serve matchup, hence strong uncertainty and no calibrated issuance.
- Observed seasonal split has mixed small samples; no opposing injury certainty, no complete opponent-adjusted histories; `NO_DEMONSTRATED_SKILL` for tennis is expressly noted in GitHub `RULES_TENNIS.md` §0. Numeric rank-1 gate NOT_ASSESSABLE.

#### A8. Sources / failure / refresh plan

- Tournament match draw / R2: `https://www.protennislive.com/posting/2026/2273/mds.pdf`; `https://tennispadelscore.com/tournaments/orleans-challenger-2026/`.
- R1 match/game/serve statistics: `https://tennistonic.com/tennis-news/1080686/h2h-prediction-of-dalibor-svrcina-vs-otto-virtanen-in-orleans-challenger-with-odds-preview-pick-12th-november-2026/`.
- 52wk indoor service returns (n and shares): `https://pythiatennis.com/dalibor-svrcina-vs-otto-virtanen-prediction-and-stats/?d=2026-11-11`.
- Season form and scoreline paths: `https://en.tennistemple.com/player/dalibor-svrcina/results`; `https://en.tennistemple.com/player/otto-virtanen/results`.
- H2H/form third-party: `https://tennical.com/h2h/svrcina-dalibor-vs-virtanen-otto/`.
- Timing variants, no verified actual first serve: `https://www.sofascore.com/tennis/match/dalibor-svrcina-otto-virtanen/tJQbsxcec`; Tennis Tonic and tournament listing above.
- Source limitations: direct open of certain web cached pages reported technical failures (search summaries still available); same-day signed OOP URL inaccessible; ATP PDF extracted match listing not visually audited; no live authorized primary-score exposure used; no specific doctor/injury report; exact server-point numerator/denominator and individual opponent adjustment absent; no repository `source-audit` command run; GitHub commits are read-only.
- Refresh plan: actual start/score/status from official ATP match record and independently second scoreboard; match medical updates if documented; operator retirement rules if owner supplies them; preserve any changed source with a dated revision rather than rewriting this card.

#### A9. Integrity / completion / readback receipt

- Card type: local unissued, `UNCALIBRATED_QUALITATIVE`; the 750,000-match numerical experiment is `EXPLORATORY_SHADOW_NOT_PRIMARY`, so numeric primary count is zero.
- Form windows: L5/L10 independently corroborated at named sources; L15/L20 counted from TennisTemple paths but not independently audited; seasonal indoor records disagree in n across providers. `INFORMATION_INCOMPLETE` not a claim of source closure.
- Model: self-authored shadow actually run with retained Python/JSON + SHA; official repo `ml.reference`, `ml.pregame`/`ml card lint`, league baseline, event kit and reference freeze not run.
- Status: current score/result `NOT_OBSERVED`; first-ball time `NOT_VERIFIED`; known-at `NOT_VERIFIED`; this is NOT a documented pre-event frozen issue.
- Completion matrix (actual): identity/draw **VERIFIED**, full player histories **PARTIAL**, serve-return matchup **PARTIAL**, availability/medical **MISSING**, H2H **VERIFIED NONE**, venue/surface **VERIFIED**, schedule/actual start **CONFLICT**, specified four contracts **COVERED**, model experiment **EXECUTED SHADOW ONLY**, released model/reference/baseline **NOT_RUN**, sensitivity **DONE SHADOW**, primary price/rank gate **NOT_ASSESSABLE**, settlement **NOT_PERFORMED**, canonical import **NOT_PERFORMED**, repository writes **NONE**, readback **LOCAL FILE VALIDATED**.
- **Sufficiency:** directional conclusions only; not performance-eligible and no calibrated primary p. Owner has explicitly prohibited GitHub writes and pushing.

**SPORTS_ONLY_MARKET_BLIND:** YES (no betting-odds input) · **OUTCOME_EXPOSURE:** NONE_KNOWN_BUT_LIVE_STATUS_UNVERIFIED · **SETTLEMENT:** NOT_PERFORMED · **CANONICAL_IMPORT:** PENDING / NOT_PERFORMED
<!-- END CARD LOCAL-20261112CC53B5C806-G0001 -->

<!-- BEGIN CARD LOCAL-20261112CC53B5C806-G0002 -->
## Card · LOCAL-20261112CC53B5C806-G0002 · Ice Hockey / Kazakhstan Pro Hokei Ligasy · Torpedo Ust-Kamenogorsk vs Arlan Kokshetau · 2026-11-12 (KZT)

- **Local event key:** `LOCAL-20261112CC53B5C806-G0002` — `LOCAL_UNIMPORTED_EVENT`.
- **Canonical ID / assignment stage:** `NOT_ASSIGNED` / `PROMPT_4_IMPORT`.
- **Event key / native ID / aliases:** Official league schedule fixture **131**, 2026–27 regular season, **Torpedo** (Ust-Kamenogorsk, home) vs **Arlan** (Kokshetau, away). Separate fixture 133 on 13 Nov Kazakhstan time is NOT this match. Secondary match record `shaiba.kz/match/39380/torpedo-arlan/12-11-2026`. Native league record 131 supported by schedule row; exact API GUID NOT_VERIFIED.
- **Authority:** `PUBLISHED_MAIN_PINNED` GitHub read-only SHA `008cedc4ff469e7a808292aa3667a7bffe22e273`; MDS v24.16, current control `CR-2026.11.11-R4`, records update `CR-2026.11.12-R1`, prompt `P-2026.11.11-v24.14`, scoring `SCV-2026.11.11-v13`, selection `SEL-2026.10.22-v4`; owner override CHAT_LOCAL_ONLY, no GitHub writes.
- **Probability method:** `UNCALIBRATED_QUALITATIVE`; a physically coherent but **unvalidated exploratory shadow** independent-Poisson regulation simulation with tie→one-goal OT/SO, 1,200,000 draws across three explicitly subjective scoring scenarios. Not a released/frozen `ANALYST_PRIMARY_V1` probability or valid source-backed league-adjusted distribution; no numeric `p_card` issued due unverified goalies, opponent-adjusted xG and operator contract endpoint.
- **Learning record:** `LEARN_RECORD_INCOMPLETE`: official league dates/opponents/scoreline rows for 26 Torpedo and 26 Arlan fixtures transcribed, including technical-win exception; not full LEARN-v2 player/goalie/line snapshots or true regulation score/known-at for each archived game. Supporting form JSON and script retained.
- **Future learning:** `PENDING_SETTLEMENT`, local result capture only. No automatic settlement or archive import.
- **Analysis status:** `UNCALIBRATED_QUALITATIVE`, no certified numeric primary forecast, sensitivity-only shadow figures marked NOT_PRIMARY.
- **Timing:** user requested `2026-11-13T00:30:00+11:00` AEDT, matching official `2026-11-12T18:30:00+05:00` (Kazakhstan) = `2026-11-12T13:30:00Z`. Research output/append timestamp `2026-11-13T00:29:59+11:00` AEDT. At web check, the official league fixture had no reported score and a secondary result page said NOT_STARTED; both dynamic pages may be stale. Verified first puck / actual delay **NOT_VERIFIED**, so status `TIMING_UNVERIFIED` and not a certified clean prestart issued card.
- **Scheduled lead / band:** the actual append is descriptive, not a commitment/freeze; timing is relative to scheduled 00:30 AEDT but actual first puck remains unverified; `KNOWN_AT_UNVERIFIED`, `NO_REMOTE_FREEZE`.
- **Endpoint / contract:** Hockey full-game puck line and total **ASSUMED** to include OT/SO with +1 on regulation tie; user did not specify operator terms or regulation-only versus full-match settlement. **UNKNOWN_DEFINITION** for formal selection, both markets; half-goal lines cannot push under a resolved single full-match goal count. Shootout score convention and postponement/abandonment rules NOT_VERIFIED.
- **Distribution:** `EXPLORATORY_SHADOW_NOT_PRIMARY`; independent Poisson for regulation goals + separate one-goal tie-break OT/SO, no fitted shot process, late empty-net or goalie mixture. 3 cases × 400,000 samples = 1,200,000; fixed seed 2026111202; scenario weights .25/.50/.25 are analyst stress-test assumptions, not learned weights or probability calibration. Code and JSON are attached locally.
- **Shadow expected score:** mixture Torpedo 3.60, Arlan 2.19, total 5.79 (including simplified tie extra goal); these are diagnostics, NOT validated central estimates. Full-match OT/shootout branch exposes regulation-tie mass ~14.7% and means are not from a fitted current-goalie ensemble.
- **Reference/baseline:** no executable GitHub `ml.reference tier`, no league-specific validated regression or snapshot and no formal `BASELINE_P`; official ladder's 10 teams yield 831 GF across 254 team-games (league goals/team-game ~3.27), but a Poisson league-only benchmark gives exploratory Under6.5 ~52.0% and omits true league total distribution and OT geometry. `BASELINE_UNAVAILABLE` for formal gates.
- **Regime/context:** home indoor rink (Boris Alexandrov Sports Palace, Ust-Kamenogorsk); Torpedo league #1 44 points and Arlan #3 41 points; 13 calendar days since each played 30 Oct; two-game consecutive-day series starting tonight, but this is the first game (NOT an actual second-night back-to-back); weather `N/A_INDOOR`. Ertis fixtures are an enormous unrepresentative influence: Torpedo 42 GF in four versus Ertis (13,8,9,12), Arlan 30 GF in four versus Ertis (11,5,5,9). Both are highly rated defensively; no justified goalie, special-teams, line-combination, coach or injury adjustments.
- **Settlement/capture:** obtain official match 131 period score (regulation, OT, SO), final and start/final timestamps and independent scoreboard, prove operator terms for supplied contracts before grading; no schedule automation made.
- **Rules read:** pinned `CURRENT_STATE.md`, `CORE.md`, `RULES_REFERENCE.md` Parts A/B, `RULES_ICE_HOCKEY.md` §§0,1–8, `PROBABILITY_TOOLKIT.md` §2.3, `RESEARCH_PROTOCOL.md` Parts A/B/D/E, `CARD_AND_LOG_TEMPLATES.md` §§2–3, `research/prompts/1_GAME_CARD.md`, `GAME_REQUEST_TEMPLATE.md` and official league source rows. No local repository model, source-audit CLI, freeze, linter or release executed.
- **Evidence receipt / known-at:** official league schedule/standings/team result pages retrieved using web search near `2026-11-13T00:29:59+11:00`; many season results can be amended on mutable sources; individual original source publication/availability times are unavailable. Secondary Shaiba.kz head-to-head corroborates two 2026 meetings; exact lineup/starting goalie unavailable. No live score used to produce the diagnostic.
- **Lineup state / issue:** `LINEUP_UNCONFIRMED` both teams; starting goalies `NOT_VERIFIED`, backup quality `NOT_VERIFIED`, skater lines/pairs/scratches `NOT_VERIFIED`, injuries/illness/suspensions `NOT_VERIFIED`, special-teams rates and xG/shots unavailable. A result-page tab labelled "Составы" (lineups) is not itself evidence of confirmed participants.
- **Pricing basis:** `SHADOW_STRESS_TEST_ONLY` (three numerical scenarios; never promoted to p_card). No named released model, no formal effect-table adjustment ledger, no valid numeric rank gate.
- **Form windows:** both clubs L5/L10/L15/L20 reconstructed from official dated Pro Hokei league records; latest 30 October. Season team rates official (Torpedo 138–46, 26 fixtures; Arlan 92–58, 26 administrative fixtures, of which **one 5–0 technical award** excluded for played-match windows). See A3 for true n; all numeric form windows are descriptive, overlapping, and not four independent signals.

### Decision block

**Decision:** Torpedo is favored to win the game, but **Arlan +1.5 vs Torpedo −1.5 is effectively balanced** by the current unvalidated goal-state model. The largest conditional signal is **Under 6.5**, from elite defensive numbers and reduction of Ertis-inflated scoring; however unconfirmed starting goalies and unknown official operator endpoint **block a qualifying Rank-1 pick** under `IH-P1/P2/P3` and `IH-B14`. Overall: **NO STRONG/CERTIFIED PICK**. The Over tail is substantial under aggressive scoring assumptions and late empty-net exposure.

| Rank | Role | Tag | Contract key / exact proposition | p_card | p_base | BASELINE_P | Distance / z | Probability basis | Main failure route |
|---|---|---|---|---|---|---|---|---|---|
| – | DIRECTIONAL, BLOCKED_RANK1 | SUPPLIED | `UNDER_6_5_FULL_ASSUMED`: final total ≤6 incl assumed OT/SO | NOT_ESTIMATED | NOT_COMPUTED | BASELINE_UNAVAILABLE | shadow mixture total mean 5.79 vs line 6.5; z not calibrated | exploratory NOT_PRIMARY 62.3% (scenario 49.2–73.7%) | goalie variance, Torpedo offensive output and empty-net seventh goal; endpoint unverified |
| – | INFORMATIONAL | SUPPLIED | `OVER_6_5_FULL_ASSUMED`: final total ≥7 | NOT_ESTIMATED | NOT_COMPUTED | BASELINE_UNAVAILABLE | as above | exploratory NOT_PRIMARY 37.7% (scenario 26.3–50.8%) | top-three defensive matchup and close-control pace |
| – | DIRECTIONAL_LOW_CONFIDENCE | SUPPLIED | `ARLAN_PLUS_1_5_FULL_ASSUMED`: Arlan loses by ≤1 or wins | NOT_ESTIMATED | NOT_COMPUTED | BASELINE_UNAVAILABLE | Torpedo shadow goal margin +1.41 vs 1.5; z not calibrated | exploratory NOT_PRIMARY 52.9% (50.9–56.9%) | Torpedo by 2+; empty-net goal |
| – | INFORMATIONAL | SUPPLIED | `TORPEDO_MINUS_1_5_FULL_ASSUMED`: Torpedo wins by ≥2 | NOT_ESTIMATED | NOT_COMPUTED | BASELINE_UNAVAILABLE | as above | exploratory NOT_PRIMARY 47.1% (43.1–49.1%) | one-goal victory / OT / Arlan defensive resistance |

**Rank-1 gate:** `NOT_ASSESSABLE` / `BLOCKED_ICE_HOCKEY_GOALIE_AND_OPERATOR_ENDPOINT`. No eligible numeric rank, no certified percentage or confidence score. **Rank-2 floor:** NOT_ASSESSABLE. **Baseline coverage:** 0 numeric primary rows; four supplied contract directions explicitly retained. **Joint failure:** no ranked primary pair; exploratory P(Under6.5 AND Arlan+1.5)=33.9%, but NOT a published joint grade. **Shadow delta/baseline:** NOT_PRIMARY. **Adjustment dependence:** no formal adjustments; scoring-regime sensitivity material. **Potential winner:** Torpedo favored qualitatively, shadow Torpedo ~73.4% and Arlan ~26.6% full-match including OT/SO, not certified. **No other user-requested lines**. **Model shadow (MLSCOPE-v3):** `NOT_RUN_NO_LOCAL_REPOSITORY_MODEL`; independent Monte Carlo is explicitly not the league release.

### Appendix

#### A1. Event identity, timing, rules and status

- User's request as supplied:

```text
Upcoming Ice Hockey Game: Torpedo Ust-Kamenogrosk vs Arlan Kokshetau, Kazakhstan Open Champs,
Estimated Game Time Start: 13 November 2026, 12:30 AM AEDT (can be delayed so continue the process as normal)

Ust-Kamenogrosk -1.5
Kokshetau +1.5
Combined Total: Over/Under 6.5 Goals
```
- Team-name alias `Ust-Kamenogrosk` resolves to official Torpedo (Ust-Kamenogorsk/Oskemen), and "Kazakhstan Open Champs" to Pro Hokei Ligasy 2026–27. Official venue, home team and fixture 131 distinguish from fixture 133 on 13 Nov at the same local time.
- Official schedule/second scoreboard say scheduled; no authenticated first-puck timestamp. At time of search, scoreboard reported "не начался" (not started), which may lag. No live/end score used. No pregame frozen issue/published timestamp claimed.
- 60-minute regulation, extra-time and shootout outcomes differ. Model's OT/SO tie-branch is a stress-test assumption, not proof of bookmaker rules. Without named settlement terms, actual action classification is UNKNOWN_DEFINITION; operator may settle 60-min totals or full match differently.

#### A2. Exact requested contracts and definitions

| Key | Sporting proposition under explicit **hypothetical full-match** convention | Failure/settlement gap |
|---|---|---|
| `TORPEDO_MINUS_1_5` | Torpedo final goals − Arlan final goals ≥2 | operator full-match/OT and empty-net rules unknown |
| `ARLAN_PLUS_1_5` | Torpedo margin ≤1 | if match ends one-goal OT, Arlan covers; actual operator rules unknown |
| `TOTAL_OVER_6_5` | sum of final goals ≥7 | shootout/OT scoring and void rules unknown |
| `TOTAL_UNDER_6_5` | sum of final goals ≤6 | shootout/OT scoring and void rules unknown |

For each row, no push under an unambiguous completed half-goal game, but operator-specific void and abandonment terms remain unverified. Each pair is complementary only on the same endpoint: hypothetical full-match pairs sum to one in each simulation state. No odds/predictor input enters calculations.

#### A3. Sources, history, form windows, availability snapshots

Official history routes:
- Torpedo `https://pro.ligasy.kz/ru/team/12-torpedo` — 26 dated, complete regular-season scoreboard rows from 2 Sep–30 Oct; 138 goals for/46 against, arithmetic verified against standings.
- Arlan `https://pro.ligasy.kz/ru/team/2-arlan` — 26 administrative rows 2 Sep–30 Oct, including 22 Sep Saryarqa–Arlan 0–5 TECHNICAL. This awarded result is *not a played game*, excluded from all Lx sample windows. Remaining **25 genuinely played games sum 92 for, 58 against**, matching official goals columns; using 97 GF from including the award would inflate attack.
- Standings `https://phl.ligasy.kz/ru/standings` — 10 clubs, 254 team-games and aggregate 831 GF/831 GA; 1st Torpedo 44 points and 3rd Arlan 41; 10th Ertis 31 GF/187 GA in 24 games.
- Competition schedule `https://pro.ligasy.kz/ru/schedule` — fixture 131 12 Nov local, 18:30; fixture 133 13 Nov 18:30 local is the rematch.
- H2H independent route `https://shaiba.kz/match/39380/torpedo-arlan/12-11-2026` — 6 Sep 2026 Arlan 3–2 Torpedo; 7 Sep Arlan 3–4 Torpedo OT. Three recent meetings including 14 Aug cup Torpedo 3–2; each decided by one goal. Exact last-10 mixed-competition H2H has 6 unders of 6.5 and 4 overs, including 9–0 aberration. Do not equate old H2H to current scoring process.
- Secondary form `https://arbatsport.kz/match/torpedo-ust-kamenogorsk-vs-arlan-2026-11-12` corroborates current form, but match-page publication dates and some fields not independently versioned.

| Window | Torpedo GF/GP | Torpedo GA/GP | Torpedo total/GP | Arlan GF/GP | Arlan GA/GP | Arlan total/GP | True n per side |
|---|---:|---:|---:|---:|---:|---:|---|
| Last 5 | 4.00 | 1.20 | 5.20 | 4.60 | 1.40 | 6.00 | 5 / 5 |
| Last 10 | 7.10 | 1.00 | 8.10 | 3.80 | 2.10 | 5.90 | 10 / 10 |
| Last 15 | 6.27 | 1.53 | 7.80 | 3.67 | 2.27 | 5.93 | 15 / 15 |
| Last 20 | 5.85 | 1.70 | 7.55 | 3.85 | 2.30 | 6.15 | 20 / 20 |
| Played season | 5.31 | 1.77 | 7.08 | 3.68 | 2.32 | 6.00 | 26 / 25 |
| Played excluding Ertis | 4.36 | 1.95 | 6.32 | 2.95 | 2.38 | 5.33 | 22 / 21 |

- Torpedo's October four Ertis results 13–0, 8–0, 9–2, 12–1 total 42 GF and 3 GA; these match the league's last-place record and should not be treated as direct evidence of production versus third-place Arlan. Arlan's four Ertis results 11–2, 5–3, 5–1, 9–2 sum 30 GF and 8 GA. Exclusions are a sensitivity diagnostic, not opponent-adjusted xG.
- Recent five: Torpedo 20–6 aggregate, Arlan 23–7; both finished 30 Oct 2026. Both have a long 13-day layoff before this game; travel and rest effects unknown, no claimed fatigue edge. Arlan technical 5–0 awarded match excluded from historical rates.
- **Official availability:** exact starting goalies, backups, skaters/lines, substitutions, illness, injuries, suspensions and final scratch list for both sides remain UNVERIFIED. Same-day official lineup/goalie source not returned in focused Kazakh/Russian/English searches; indexed match centre has a lineups tab but no reliably retrieved confirmed names or timestamps. A third-party preview discusses an uncorroborated potential absence; **not admitted as a confirmed injury input**. No false "all healthy" inference.
- **Process metrics:** no verified 2026–27 named-provider xG, SOG with blocked-shot definition, high-danger chances, PP/PK percentages, expected goaltender save differential, EN-goal frequency for this exact league. The NHL population constants in sport rules are only structural examples, **not calibrated Kazakhstan rate parameters**.

#### A4. Calculations, counterfactuals, sensitivity and missing reference

- League-only attack level from official table: `LM = 831 / 254 = 3.272` team goals/game, `LM_total ≈ 6.543`. An **illustrative** Poisson under 6.5 = `P(Pois(6.543) ≤6) ≈ 0.520`; not a formal competition `BASELINE_P` without exact goal-count distribution/OT adjustment.
- Raw additive scoring cross-average: Torpedo home expectation `(5.308 + 58/26)/2 ≈ 3.77`; Arlan away expectation `(92/26 + 46/26)/2 ≈ 2.65`; raw total ≈ 6.42. These denominators include Arlan administrative game; a 25-played sensitivity produces slightly different values. Raw averages confound opponent strength, technical award and regulation/full-match definition.
- Weak-opponent omission: Torpedo `96GF/43GA` in 22 non-Ertis games; Arlan `62GF/50GA` in 21 such games. Multiplicative attack/defence ratios around common LM yield approximately Torpedo 3.17 and Arlan 1.77 **regulation** means (not fitted).
- Scenario inputs were declared before Monte Carlo: LOW (3.17/1.77; weight .25), MID (3.55/2.05; weight .50), HIGH (3.77/2.66; weight .25); all in Torpedo/Arlan goals for regulation. High is raw additive average, LOW omits Ertis, MID interpolates. These stress-test weights are discretionary, not estimated from held-out outcomes. 400,000 independent simulations per scenario, PCG64 seed 2026111202; genuine execution file `hockey_shadow_torpedo_arlan_20261112.py`, JSON `HOCKEY_SHADOW_DIAGNOSTIC_20261112CC53B5C806-G0002.json`.
- Model: `X~Poisson(λ_T)`, `Y~Poisson(λ_A)` for regulation, independently. If tied, exactly one additional goal to one team, winner weight `λ_T/(λ_T+λ_A)`; else final equals regulation. This correctly prevents a 2-goal OT win and flags the difference between regulation total and full match, but it treats season finals as regulation-fit rates, **omits opponent-adjusted shots, goalie substitution, score effects, 6-on-5 empty net, and a genuine SHOOTOUT convention**. That omission can meaningfully change total and -1.5 results.

| Scenario | Reg λ Torpedo | Reg λ Arlan | Under 6.5 shadow | Arlan +1.5 shadow | Torpedo −1.5 shadow |
|---|---:|---:|---:|---:|---:|
| LOW | 3.17 | 1.77 | 73.7% | 52.8% | 47.2% |
| MID | 3.55 | 2.05 | 63.0% | 50.9% | 49.1% |
| HIGH | 3.77 | 2.66 | 49.2% | 56.9% | 43.1% |
| Weighted stress-test (NOT_PRIMARY) | – | – | **62.3%** | **52.9%** | **47.1%** |

- Over 6.5 is complementary to Under at 37.7% in the diagnostic; empty-net/goalie branches make this non-certifiable. Rounded MC sampling error is tiny relative to source and model uncertainty; avoid using MC precision as confidence.
- Stability: Under varies by 24.5 percentage points across reasonable mechanisms; Arlan +1.5 varies ~6 points but sits barely above a coin flip. Under is a descriptive lean, not robust to a high-score scenario. No stable ≥0.65 approved candidate.

#### A5. Full universe / W-P-L-V for each supplied direction

| Contract | Hypothetical WIN | LOSS | PUSH | VOID / UNKNOWN | Direction, disposition |
|---|---|---|---|---|---|
| Torpedo −1.5 | margin ≥2 | margin ≤1 | 0 with half-goal resolved endpoint | operator abandonment/OT terms UNKNOWN | marginal negative; ~47.1% SHADOW ONLY |
| Arlan +1.5 | margin ≤1 | margin ≥2 | 0 | same unknown | marginal positive; ~52.9% SHADOW ONLY |
| Over 6.5 | sum ≥7 | sum ≤6 | 0 | same unknown | negative; ~37.7% SHADOW ONLY |
| Under 6.5 | sum ≤6 | sum ≥7 | 0 | same unknown | positive but goalie-blocked; ~62.3% SHADOW ONLY |

Sporting result probabilities from shadow Torpedo full-match win ~73.4%, Arlan ~26.6%, regulation tie ~14.7% before OT/SO. This is not the same proposition as Torpedo -1.5. No formal rank; no contractual operator odds or market probabilities consulted.

#### A6. Adjustments and no-double-counting

| Mechanism | Evidence | Treatment | Assumed official primary effect |
|---|---|---|---|
| Ertis mismatch | 42 Torpedo GF against 24-game 31–187 Ertis; Arlan 30 | LOW scenario omits these fixtures; compared to unadjusted HIGH | NONE; model stress-test only |
| Defensive form | Official Torpedo GA 46, Arlan GA 58 with a technical match | descriptive under support; overlaps seasonal ratings | NONE; no double-count form shift |
| 13-day layoff | Both last played Oct 30, same rest window | adds unquantified goalie/line uncertainty | NONE |
| Home rink | Torpedo home, Arlan away | established location; no fit for Kazakhstan home effect | NONE |
| Recent H2H | 2 September league games decided by one goal | suppress overconfidence in -1.5 only; no fitted boost | NONE |
| Goalie/lines | two starts and benches unconfirmed | score and width uncertain; formal total ranked BLOCKED | NONE |
| OT/empty net | Hockey structural mechanism in RULES_ICE_HOCKEY | simulated simple OT; EN unresolved | NONE |

#### A7. Coherence / family / shadow gate

- In every simulated path Torpedo −1.5 and Arlan +1.5 are complements; Over 6.5/Under 6.5 are complements for **assumed** full-match scoring. OT game finishing one goal cannot cover favorite −1.5.
- Reg ties average 14.7%; a 3–3 tie is regulation total 6 but hypothetical 4–3/3–4 OT final has 7 and lands Over 6.5. Weighted regulation Under6.5 ~66.2%, hypothetical full-match Under6.5 ~62.3%; this gap demonstrates the endpoint sensitivity. No actual operator terms were supplied.
- `IH-P1`, `IH-P2`, `IH-P3`, `IH-B14` block a certified Rank 1. Kazakhstan-specific first-puck availability or independent process stats did not close the goalie gap. NHL historical baselines not used as Kazakhstan calibration; ignore betting/prediction websites for numerical evidence.
- No historical or live-score exposure admitted; no duplicate same-event card, different next-day fixture explicitly excluded. No claim of `ml card lint`, checksum source repository freeze, or prospective ledger publication.

#### A8. Source route and unresolved-evidence plan

- Priority official: `https://pro.ligasy.kz/ru/schedule`, `https://pro.ligasy.kz/ru/team/12-torpedo`, `https://pro.ligasy.kz/ru/team/2-arlan`, `https://phl.ligasy.kz/ru/standings`.
- Second independent: `https://shaiba.kz/match/39380/torpedo-arlan/12-11-2026`, and `https://arbatsport.kz/match/torpedo-ust-kamenogorsk-vs-arlan-2026-11-12`. Search result read of individual league pages succeeded although some direct web-open attempts reported cache/UnexpectedStatusCode; individual historical scorelines and official totals were arithmetic-checked.
- Failed/restricted needs: no actual confirmed game-specific goalie or scrapes found in Russian/Kazakh/English searches for "Торпедо Арлан 12 ноября 2026 вратари состав", team official lineups and absences; no independently sourced credible official 2026 Rysbekov status; no league-specific PP/PK xG, injury report, actual first puck or OT/total action policy. The next admissible source for those fields is official game 131 protocol once available, with its own publication timestamp. Not scheduled.
- Next capture: official final score plus regulation period breakdown and goalie participation, injury/line snapshots if preserved, first-puck timestamp and any technical/abandonment indicator. Independent cross-check from Shaiba.kz. Card cannot be settled until exact user contract's operator rules are established or state UNRESOLVED.

#### A9. Integrity and required research-completion matrix

| Required procedure | Actual work/evidence and result | Remaining gap / next field | Status |
|---|---|---|---|
| Authority, exact identity, duplicate, schedule | Main SHA pinned; official fixture 131 distinguished from 133; 00:30 AEDT conversion | actual puck drop unavailable; no remote freeze | DONE_PARTIAL_TIMING |
| Both-side starters/bench/absences | English/Russian/Kazakh queries + roster and same-game scoreboard routes | goalie starter, backups, skaters, scratches, confirmed medical; next official game-sheet | INFORMATION_INCOMPLETE |
| Online history/source correction/known-at | 26 official rows each, source comparison, technical award explicitly excluded | per-game original publication timestamps and every regulation period missing | INFORMATION_INCOMPLETE |
| Both sides L5/L10/L15/L20/season/league | computed 5/10/15/20 both, 26 Torpedo / 25 played Arlan; league 10 teams | no opponent-adjusted goal xG; full official historical regulation split | DONE_FOR_VISIBLE_FINAL_GOALS |
| Sport mechanisms and conditions | venue, rest, H2H, mismatch, OT, empty net, opponent strength stress | goalies, special teams, shot definition, fatigue personnel | INFORMATION_INCOMPLETE |
| Reference and primary/freeze receipts | league-only Poisson diagnostic attempt; no official run, no released competition model | repo ml.reference unavailable; operator and goalie gate unclosed | NOT_RUN_PRIMARY |
| Adjustments / equations | scenario formulas + stated subjective weights, no double count, 1.2M true simulation | no learned effect table/equivalent trained goalie mixture | SHADOW_ONLY |
| All four supplied rows / W-P-L-V | 4/4 covered with complement states and defined settlement uncertainty | actual operator definition UNKNOWN_DEFINITION | DONE_FOR_HYPOTHETICAL_ONLY |
| Expected goals/baseline/sensitivity/dependence | true executed shadow; LOW/MID/HIGH intervals & OT gap; league mean reconstructed | no league exact baseline / calibrated primary p | SHADOW_ONLY |
| Seven steps / append card, audit, custody | A1–A9 complete with gaps; prior card bytes preserved; scheduled local file append and readback; no repository mutation | official issue/freeze and GitHub linter **NOT_PERFORMED** | CHAT_LOCAL_DRAFT |

- **Information completeness:** `INFORMATION_INCOMPLETE`, notably both starting goalies, live event state and operator endpoint/settlement rules. Model procedure `EXPLORATORY_SHADOW_EXECUTED / PRIMARY_NOT_RUN`; issuance `DRAFT_NOT_REPOSITORY_ISSUED`.
- **Sporting disposition:** no safely certifiable most-likely pick. Directional only Under 6.5 if the supplied contract is full-match and goalie regime resembles the lower/mid scenarios; at aggressive scoring inputs Under is below 50%. Arlan +1.5 roughly balanced and not low-risk. NEVER claim a calibrated 62.3% forecast or hindsight revision.
- **Integrity:** all G0001 card bytes preserved; hash of original mini and resulting mini held in separate receipt; all IDs stable; no official GitHub commit/push, no canonical P-ID, no automated settlement. This record is a chat-local working draft.

**SPORTS_ONLY_MARKET_BLIND:** YES (no betting odds in inputs) · **OUTCOME_EXPOSURE:** NONE_USED_BUT_ACTUAL_START_UNVERIFIED · **SETTLEMENT:** NOT_PERFORMED · **CANONICAL_IMPORT:** PENDING / NOT_PERFORMED
<!-- END CARD LOCAL-20261112CC53B5C806-G0002 -->


<!-- BEGIN CARD LOCAL-20261112CC53B5C806-G0003 -->
## Card · LOCAL-20261112CC53B5C806-G0003 · Tennis / ATP Stockholm 250 · Thiago Agustín Tirante vs Aleksandr Shevchenko · 2026-11-12 CET

- **Local event key:** `LOCAL-20261112CC53B5C806-G0003` — `LOCAL_UNIMPORTED_EVENT`; **canonical ID:** `NOT_ASSIGNED / PROMPT_4_IMPORT`.
- **Event / aliases:** ATP Stockholm (BNP Paribas/Bybit Nordic Open) 2026, men's singles quarterfinal, Centre Court; Thiago Agustín Tirante (ARG, also listed as “Thiago Agustin”) against Aleksandr/Alexander Shevchenko (KAZ). No official native event ID extracted. Not a duplicate of G0001 (Orléans tennis) or G0002 (Kazakhstan ice hockey).
- **Authority:** `danisgreat/Sports-Research` main pinned `008cedc4ff469e7a808292aa3667a7bffe22e273`; MDS v24.16; forecast control CR-2026.11.11-R4; records change CR-2026.11.12-R1; prompt P-2026.11.11-v24.14; scoring SCV-2026.11.11-v13; selection SEL-2026.10.22-v4; owner's chat-local/no-GitHub-write override.
- **Analysis / issue status:** `UNCALIBRATED_QUALITATIVE` / `READ_ONLY_DRAFT / NOT_REPOSITORY_ISSUED`; **no validated primary probability**, no frozen reference or canonical issued score. Independent Markov model executed for *shadow-only conditional diagnostics*; does not populate `p_card`.
- **Learning:** `LEARN_RECORD_INCOMPLETE`; exact game history and dated medical/availability source snapshots incomplete. Future learning `PENDING_SETTLEMENT`, no shared learning-store ingestion.
- **Timing:** user request circa `2026-11-13T00:59+11:00` AEDT; official no-earlier-than scheduled start `2026-11-12T15:00:00+01:00` CET = `2026-11-12T14:00:00+00:00` UTC = `2026-11-13T01:00:00+11:00` AEDT. **Analysis and draft completion `2026-11-13T01:10:58+11:00` after scheduled threshold**; actual first ball `NOT_VERIFIED`, no result exposed in inputs. Phase `POST_SCHEDULED_TIME_ACTUAL_START_UNVERIFIED`, not certified pre-event. Source publication/known-at before first ball NOT independently proven.
- **Endpoint:** completed singles match best-of-three sets, tiebreak at 6–6 to 7 by two; full-match **games** not set spreads. Half-game contract has no push on a completed scored event. Bookmaker/operator retirement, walkover, suspension, disqualification and abandoned-match action definitions NOT_SUPPLIED; actual external settlement `UNKNOWN_DEFINITION` for those paths.
- **Venue / conditions:** Kungliga Tennishallen, Stockholm, indoor hard, no outdoor weather modifier. Player rest and qualifying load are material; ball speed/temperature, court speed and exact ball brand `NOT_VERIFIED`.
- **Full-game distribution object:** `EXPLORATORY_TENNIS_SET_MARKOV_20261113_G0003`; IID service-point probabilities by player, exact game-hold formula, 6–6 tiebreak point-state DP, exact completed-set kernels and best-of-three conditional sum, random first server 50/50. All case calculations read from attached executable code and JSON; *not* a fitted or prospective-calibrated primary model.
- **Expected games and winner:** primary `NOT_ESTIMATED`; exploratory total 25.72 / 25.99 / 26.17 (all-surface / shrunk indoor / indoor-only), with scenario-dependent Tirante match-win 58.4% / 51.4% / 39.2%; scenario results are non-certified and must not be conflated with a card forecast.
- **Baseline:** formal `BASELINE_LEAGUE_V1` **NOT_AVAILABLE** (no exact competition-cohort reference/forecast release verified or run locally); no proper `p_base`/`BASELINE_P`, competition-specific probabilities or certified ranks.
- **Pricing basis:** NO_CARD_PRICING; illustrative sensitivity uses (a) all-surface, (b) indoor return/serve adjusted toward an arbitrary 20-match prior, and (c) indoor-only. **No scenario weights or aggregation into p_card**.
- **Form:** Tirante recent five *played* matches 2–3; Shevchenko 4–1 (qualifying included), corroboration routes described A3. A pre-match provider lists L10 4–6 and 7–3 respectively, but the full L10 ledger is NOT independently reconstructed. L15 and L20 match-level true n/rates `NOT_VERIFIED`, not imputed. Tennis surface 2026 sources disagree on indoor W–L windows (Tirante 3–4; Shevchenko 6–4 versus 9–5), so both are retained as source-level definitions, no silent selection.
- **Availability / physical state:** both identified as entrants; neither's injury/illness/medical clearance independently verified. Tirante's previous-round **opponent** Etcheverry withdrew (not evidence that Tirante himself was injured). Shevchenko completed three sets against Ruud on 11 November. No official new absence or medical status asserted; tennis does not have a bench/starting lineup but player-specific walkover and MTO state need checking.
- **Evidence capture / reading receipt:** tournament schedule, recent official results, Tennis.com H2H, TennisDB and specialist tennis statistics, retrieved in this session 2026-11-13 approximately 00:59–01:05 AEDT; precise per-provider source publication times often unavailable. Sources and gaps in A3/A8. GitHub references verified earlier in this conversation; no local repository code checked out.

### Decision block

**Assessment:** **Over 23.5 total games** is the sole mildly consistent *directional* lean, but none of the lines reaches a defensible high-confidence threshold. The games handicap is unstable: stronger broad-form Tirante versus Shevchenko's higher recent indoor return/serve and qualifier momentum. In a sparse, source-disputed indoor sample, abstaining is a reasonable outcome.

| Rank | Role | Tag | Contract key / exact proposition | p_card | p_base | BASELINE_P | Distance / z | Probability basis | Main failure route |
|---|---|---|---|---|---|---|---|---|---|
| 1 | PICK_DIRECTIONAL_LOW_CONFIDENCE | SUPPLIED | `TOTAL_OVER_23_5`: match total games ≥24 | NOT_ESTIMATED | NOT_COMPUTED | BASELINE_UNAVAILABLE | model means 25.72–26.17, z UNVALIDATED | Qualitative; exploratory scenarios 54.8–55.9% | Two efficient straight sets or lower-than-estimated holds |
| 2 | INFORMATIONAL_NOT_STABLE | SUPPLIED | `TIRANTE_GAMES_PLUS_0_5`: Tirante games ≥ Shevchenko games (ties count as Tirante cover) | NOT_ESTIMATED | NOT_COMPUTED | BASELINE_UNAVAILABLE | signed game centre −0.96 to +0.78; z UNVALIDATED | Qualitative; exploratory scenarios 41.7–61.0% | Shevchenko's indoor advantage, long-match fatigue effects reversed |
| – | INFORMATIONAL_NOT_STABLE | SUPPLIED | `SHEVCHENKO_GAMES_MINUS_0_5`: Shevchenko games > Tirante games | NOT_ESTIMATED | NOT_COMPUTED | BASELINE_UNAVAILABLE | same margin, opposite contract | Qualitative; exploratory scenarios 39.0–58.3% | Tirante's superior wider-sample serve/return and better rest |
| – | INFORMATIONAL | SUPPLIED | `TOTAL_UNDER_23_5`: match total games ≤23 | NOT_ESTIMATED | NOT_COMPUTED | BASELINE_UNAVAILABLE | model means 25.72–26.17; z UNVALIDATED | Qualitative; exploratory scenarios 44.1–45.2% | Third set and multiple 7–5/7–6 sets |

**Baseline coverage:** 0/0 numerically priced primary rows; all 4/4 supplied contracts independently evaluated. **Rank-1 gate:** `NOT_ASSESSABLE`; conditional shadow below 0.65 and uncalibrated. **Rank-2 floor:** `NOT_ASSESSABLE`. **Most-likely list:** no numerical formal rank; directional only. **Rank scope:** supplied lines only. **Unstable handicap:** all-surface suggests Tirante +0.5; indoor-only suggests Shevchenko −0.5.

**Joint failure** of Over 23.5 plus Tirante +0.5 means Under 23.5 AND Shevchenko −0.5. Exploratory probabilities 17.4% / 21.2% / 28.7% across the three cases. NOT a certified combined-selection probability. **Model shadow:** independent code executed (not repo ML): JSON `TENNIS_SHADOW_DIAGNOSTIC_20261112CC53B5C806-G0003.json` SHA256 `249931437875a878cc64f343f24202ee4871b9fea80d13af750048db0747deec`, source `tennis_shadow_tirante_shevchenko_20261113.py` SHA256 `68ef67d4f6758d51197e82d3d5b0c31c9863356fe8ec058b9a5bcec570e037a1`. **Official MLSCOPE-v3 release execution:** `NOT_RUN_NO_LOCAL_REFERENCE_RELEASE` / pregame freeze `NOT_PERFORMED`. No rank, p_card or settled result from shadow.

### Appendix

#### A1. Exact identity, time, state

- Official Stockholm Open schedule: https://www.stockholmopen.se/en/tournament/spelschema?dayToDisplay=6 lists Tirante vs qualified Shevchenko QF “Not Before 15:00” CET on Thursday 12 November 2026, following Michelsen vs Tabilo. Stockholm 15:00 CET = UTC 14:00 = AEDT 01:00 Nov 13. Courts can run late. Centre Court at Kungliga Tennishallen, ATP 250, indoor hard, best of 3. Source cross-checked with https://www.tennis.com/tournaments/stockholm-open/matches/t-tirante-vs-a-shevchenko-2026-11-12 and https://tennistourcalendar.com/2026-stockholm-open-daily-schedule-order-of-play-and-results/.
- Latest pre-event schedule/listing pages still display this fixture as upcoming/0–0, not evidence of actual start. No verified play or outcome at `2026-11-13T01:10:58+11:00`; avoid presenting this as a frozen pre-start prediction because it is past the **scheduled earliest** start.
- Exact event official native ID and retirement-action operator unknown. H2H earlier 2025-03-18 Miami qualifying 6–3,6–3 Tirante (outdoor hard), not a same-surface indoor comparator.

#### A2. Supplied contracts and match-completion conventions

| Owner supplied | Formal completed-match W | Formal completed-match L | Push | Missing/void path |
|---|---|---|---|---|
| Tirante +0.5 games | T ≥ S games | T < S games | NONE on .5 | walkover/retirement rules unspecified |
| Shevchenko −0.5 games | S > T games | S ≤ T games | NONE on .5 | walkover/retirement rules unspecified |
| Over 23.5 combined games | G ≥24 | G ≤23 | NONE on .5 | walkover/retirement rules unspecified |
| Under 23.5 combined games | G ≤23 | G ≥24 | NONE on .5 | walkover/retirement rules unspecified |

The +0.5 and −0.5 handicaps are exact complements **including match states with equal games**; match winner and games spread are **not equivalent**. Endpoints include every game in all completed sets; tiebreak points do **not** add games (7–6 contributes 13). No operator terms provided; do not assert action for retirement or W/O.

#### A3. Historical data, level, playing style, availability and learning gaps

| Decisive observation | Evidence and status | Consequence |
|---|---|---|
| Official event draw/conditions | Official Stockholm schedule linked A1; ATP 250 indoor hard | CONFIRMED fixture/round/surface |
| Tirante ranking / Shevchenko | Tennis.com preview 51 / 107, https://www.tennis.com/tournaments/stockholm-open/matches/t-tirante-vs-a-shevchenko-2026-11-12 | Rankings used descriptively, not additive numeric factors |
| Tirante Stockholm matches | Official tournament result https://www.stockholmopen.se/en/tournament/resultat?resultDay=2: Munar 7–6(3),6–3; independent TennisDB records Etcheverry R16 W/O | One played Stockholm win only; W/O is **not** a scored fixture or serve-stat datapoint |
| Shevchenko Stockholm | https://www.flashscore.com/tennis/atp-singles/stockholm/results/ and https://tennistale.com/tournaments/atp/2026/stockholm: qualifying Durasovic 6–1,6–1; Fearnley 6–2,6–4; Mannarino 6–1,6–3; Ruud 6–7(5),6–4,6–3 | Four on-court wins, qualifying opponents must not be equated with Tour opposition |
| Recent five **played** | Tirante: Munar W; Struff L; Bellucci L; Svajda W; Mannarino L, true n=5. Shevchenko: Ruud W; Mannarino W; Fearnley W; Durasovic W; Sakellaridis L, true n=5. Source TennisDB and event records | 2–3 versus 4–1; 10-Nov Tirante W/O excluded |
| Recent ten | https://thetennistrader.com/match/thiago-agustin-tirante-vs-alexander-shevchenko-stockholm-2026.html reports Tirante 4–6 and Shevchenko 7–3. Its raw last-ten match list not independently captured/reconciled | n=10 provider summary, PROVISIONAL; no pretend complete audited ten-row ledger; no odds/market data used |
| Recent 15, 20 / surface-only L5/L10/L15/L20 | Full dated match rows/reconciliation NOT_CAPTURED; TennisDB cached search and direct-open versions disagreed on freshness (direct-open stale Aug 2026) | True n and opponent-adjusted match-scoring windows NOT_VERIFIED; leave missing |
| Indoor-season records | Tennis Explorer https://noproxy.tennisexplorer.com/match-detail/?id=3377329 reports Tirante 3–4 / Shevchenko 9–5; TheWorldOfTennis https://theworldoftennis.com/match/aleksandr-shevchenko-thiago-agustin-tirante/ reports 3–4 / 6–4 | Inconsistent source scope and qualifying inclusions. Do **not** reconcile by picking a preferred number; source-specific only |
| Serve/return numerators | 52-week PythiaTennis statistics https://pythiatennis.com/alexander-shevchenko-vs-thiago-agustin-tirante-prediction-and-stats/?d=2026-11-12; indoor serve-points won Tirante .663 (6 matches), Shevchenko .672 (11); return-points won Tirante .317, Shevchenko .353; all-surface service .666/.633 and return .358/.357 (57/66 matches) | Independent model uses only raw service/return observations, **not site's picks or odds**; source sample and as-of timestamps not independently verified |
| H2H | 18 March 2025 Miami Q: Tirante beat Shevchenko 6–3,6–3; Tennis.com and TennisLive corroborate | 1–0 historical, different venue/season; no deterministic matchup shift |
| Fatigue / travel | Tirante rested due Etcheverry W/O, recent Paris/Vienna; Shevchenko qualified at Stockholm and played three sets against Ruud 11 Nov. | Confirmed relative tournament workload, actual fatigue/body status UNKNOWN; scenario-sensitive mechanism only |
| Injuries / withdrawals / coach | Etcheverry withdrew; **not** Tirante. No official same-day player medical/MTO status, Shevchenko medical clearance, new coach or specific tactical unit verified. | `MEDICAL_STATUS_UNVERIFIED`, no “healthy” claim or numeric injury adjustment |

**LEARN-v2 partial row register:** for the two observed cohorts, dated Stockholm wins above and last five played listed. Complete L10/L15/L20, each opponent ranking-at-date, match durations and per-match serve/return numerators and publication time not captured; `LEARN_RECORD_INCOMPLETE`. The online match list is not a validated historical source package.

#### A4. Reference stage, exact tennis distribution, sensitivity and expected score

Official repository reference stage and `ml`/frozen league baseline unavailable in chat-local execution; no pregame model receipt and no official primary forecast. An independently executable analytical diagnostic **did run** as `tennis_shadow_tirante_shevchenko_20261113.py` SHA256 `68ef67d4f6758d51197e82d3d5b0c31c9863356fe8ec058b9a5bcec570e037a1`.

For source-backed **conditional scenarios**, estimate each player's point-win on serve as the average of (own service-points won) and (1 − opponent return-points won), with no fitted opponent adjustment. Inputs from A3:

- **All surfaces:** Tirante (0.666+1−0.357)/2 = 0.6545; Shevchenko (0.633+1−0.358)/2 = 0.6375.
- **Indoor only:** Tirante (0.663+1−0.353)/2 = 0.6550; Shevchenko (0.672+1−0.317)/2 = 0.6775. Indoor sample only 6 and 11 matches.
- **20-match illustrative shrink:** ((20×0.6545)+(6×0.6550))/(20+6) = 0.6546; ((20×0.6375)+(11×0.6775))/(20+11) = 0.6517. **20 is a sensitivity assumption, not an inferred or validated optimal prior.** No arbitrary scenario mixing weights.

At service point p, probability of holding from deuce rules: `p^4(1+4q+10q²) + 20 p³q³ × p²/(p²+q²)`, q=1−p. Explicit point-level tiebreak sequence, full 6–0 through 7–6 set kernels, matched next-set server and two-or-three-set outcomes computed by deterministic Markov enumeration. Neither the code nor the source asserts calibrated OOD quality, injury response, court-speed effect, validated retirement handling or prospectively frozen model. The 50% initial server assumption is illustrative.

| Shadow scenario (no weights) | Tirante point serve / Shevchenko | Hold T / S | T +0.5 | S −0.5 | O23.5 | U23.5 | P(decider) | Mean total |
|---|---|---|---:|---:|---:|---:|---:|---:|
| All-surface | 0.6545 / 0.6375 | 83.7% / 80.8% | 61.0% | 39.0% | 54.8% | 45.2% | 49.4% | 25.72 |
| 20-match shrink | 0.6546 / 0.6517 | 83.7% / 83.2% | 54.1% | 45.9% | 55.9% | 44.1% | 50.0% | 25.99 |
| Indoor-only | 0.6550 / 0.6775 | 83.8% / 87.2% | 41.7% | 58.3% | 55.8% | 44.2% | 49.0% | 26.17 |

**Limitations:** the 20-match shrink and matchup-average are sensitivity devices; samples overlap across time/surface; service points IID assumption ignores return-style opponents, momentum, fatigue, injury and game-score dependence. Strong first serve can increase both tiebreaks and Over, but two controlled sets can still stay Under. No framework-validated competition variance/width-floor exception, no official `p_card` or `BASELINE_P`.

#### A5. All four propositions, W/P/L/V and two-sided evidence

All four exact user-supplied lines are covered in A2 and decision table. **Numerical shadow only**: range T +0.5 41.7–61.0%; S −0.5 39.0–58.3%; O23.5 54.8–55.9%; U23.5 44.1–45.2%. Values from one common match-score grid per scenario, never unrelated independent bets; over/under complementary; ±0.5 spread complementary including equal-games states.

- For **Over**, supporting mechanisms: indoor holds, chance of tiebreaks and deciding set. Opposing: Shevchenko's qualifying momentum or Tirante's rest may produce a dominant 2–0 with few games; plausible lower serve holds. Lean **mildly Over** without formal p.
- For **Under**, supporting: two-set finishes and some Shevchenko recent lopsided wins. Opposing: opponent quality changes, Ruud match went three, both can hold on indoor. Not primary choice.
- For **Tirante +0.5**, supporting: higher current ranking, outside-indoor serve/return, Miami H2H, rest. Opposing: 6-match indoor sample, Shevchenko's indoor return/service advantages and upsets. Unstable.
- For **Shevchenko −0.5**, supporting: four on-court victories including Ruud; stronger specific indoor percentages. Opposing: cumulative qualifying/three-set fatigue, Tirante's serve and indoor sample selection bias. Unstable.
- W/P/L/V: no push for completed .5 lines; void/retirement operator terms missing. No claim of a known settlement convention.

#### A6. Adjustment ledger / scenarios / unadjusted comparison

No formal source-qualified effect table or calibrated `REFMODEL-v1` is locally available; **zero priced formal adjustment rows**. Shadow scenario levers are observed indoor-versus-all-surface point-service composition, *not* independent official effect sizes. Ranking, H2H, rest and recent wins are qualitative mechanisms only to avoid double counting or manufacturing numerical effects. Tirante W/O is not added as a win performance in serve rates. The 20-match prior is labelled exploratory, with no calibrated best weight; all three conditional cases remain separately presented.

#### A7. Family checks, dependency and shadow hygiene

- The game-score and total distributions in each scenario sum to 1 (exact dynamic programming check); all complementary half-game events sum to 1. At equal total games, **Tirante +0.5 covers and Shevchenko −0.5 does not**. Exact complete-match model tie-in-games mass ~5% across cases; this is handled explicitly rather than losing it.
- A games-handicap winner is not identical to the match winner: in a 2–1 win with a heavily lost set the player may lose aggregate games; winner mass separately recorded.
- Over 23.5 + Tirante +0.5 dual-loss diagnostic from a common grid (Under AND Shevchenko −0.5) = 17.4% / 21.2% / 28.7% across scenarios; not a calibrated joint recommendation.
- Retirements, back-to-back/court speed, actual injury and special circumstances not modelled. Match score cannot be assessed as a clean pregame issue after verified first ball unless a genuinely pre-start frozen copy exists (none in this chat).

#### A8. Provenance, access/coverage, final recheck and queue

| Source | Specific field used | Limit / next verification |
|---|---|---|
| https://www.stockholmopen.se/en/tournament/spelschema | Original official match and no-earlier-than time, Centre Court, qualifying | Verify actual first-ball/official updated OOP if critical; publication not timestamped |
| https://www.stockholmopen.se/en/tournament/resultat?resultDay=2 | Tirante v Munar 7–6(3),6–3 | Round 1 only, not confirmation of today result |
| https://www.tennis.com/tournaments/stockholm-open/matches/t-tirante-vs-a-shevchenko-2026-11-12 | Players, rankings, H2H, scheduled quarterfinal | live status and match issue not verified |
| https://www.flashscore.com/tennis/atp-singles/stockholm/results/ | Stockholm completed qualifying, Mannarino and Ruud results | Direct-open returned stale cached page in one retrieval; current search result used for date-specific rows, as-of uncertainty |
| https://tennis-db.com/players/203/thiago-agustin-tirante/matches and https://tennis-db.com/players/206/aleksandr-shevchenko/matches | Recent match-level rows and W/O handling | direct-open cached outdated August view; search summaries newer, insufficient for true L15/L20 ledger |
| https://pythiatennis.com/alexander-shevchenko-vs-thiago-agustin-tirante-prediction-and-stats/?d=2026-11-12 | Raw recent indoor and all-surface serve/return rates, match n | site also has forecasts but those were NOT used; data published-at unverified; indoor small n |
| https://noproxy.tennisexplorer.com/match-detail/?id=3377329 and https://theworldoftennis.com/match/aleksandr-shevchenko-thiago-agustin-tirante/ | Independent surface record, match roles | Disagreement on Shevchenko indoor scope; not resolved |

**Open evidence:** both players' confirmed medical state and physical capacity; exact 15/20 match ledger; harmonised season indoor match n; reliable source publication times; match actual start/in-play status; operator retirement/W/O contract; prospective competition baseline/released reference; official archive native ID. **Next source/action:** official Stockholm match centre and ATP match stats/result once published, independently cross-check tournament results, capture completed set scores and retirement; build full L20 only from contemporaneously dated match records. No automation scheduled or background monitoring implied.

#### A9. Integrity readback, seven-step research completion, timing and issuance

| Required procedure | Actual work performed and result | Limitation / next field | Status |
|---|---|---|---|
| Authority, native identity, duplicate, timing | Official tournament QF confirmed; local G0003 distinct; main SHA pinned; user 01:00 scheduled not-before | actual first ball, operator event ID | DONE_WITH_TIMING_GAP |
| Both-side participants, current absences, medical | Two named players confirmed; queried draw, W/O, last match | player-specific medical/withdrawal and final in-play recheck unavailable | INFORMATION_INCOMPLETE |
| History source comparison and known-at | Tournament official + Tennis.com + TennisDB + specialist rates examined, conflicting season tallies flagged | complete 15/20 and origin timestamps | INFORMATION_INCOMPLETE |
| L5/L10/L15/L20, season/level | L5 five dated played matches both; L10 4–6 and 7–3 only provider provisional; surface records captured with conflict | L15/L20 and complete scored game rows not verified | INFORMATION_INCOMPLETE |
| Tennis mechanisms/conditions | Indoor hard, H2H, tiebreak, serve/return, rest, opponent calibre, qualification | balls, exact court speed, fatigue/fitness | DONE_WITH_GAPS |
| Formal reference / freeze | Repository reference and pregame freeze never executed | no local `ml` release, no source-qualified baseline, actual start unknown | NOT_RUN |
| Independent arithmetic / sensitivity | Markov exact completed-match grid run for three scenarios; code and JSON retained with SHA | uncalibrated and small sample; no official p | SHADOW_EXECUTED |
| Every supplied proposition | All four evaluated, game-margin equality fixed, W/P/L/V and full-match interpretation explained | retirement/operator action unknown | DONE_CONDITIONAL |
| Expected game / same-line baseline / dependence | 25.72–26.17 scenario means; no formal baseline, joint failure conditional calculation | baseline cannot pass numeric gate | SHADOW_ONLY |
| Append, original custody / delivery | G0001,G0002 cores remain byte-for-byte unchanged; revised mini file readback as separate receipt | GitHub linter, commit, push, remote issuance deliberately NOT_PERFORMED | CHAT_LOCAL_DRAFT |

**Overall research status:** `INFORMATION_INCOMPLETE`; numerical `EXPLORATORY_MARKOV_SHADOW_EXECUTED / PRIMARY_NOT_RUN`; publication `READ_ONLY_DRAFT_NOT_ISSUED`. **No market odds, sportsbook prices or line movement used in model.** No claim of official pre-match issuance, eventual result, settlement, calibration or canonical allocation. Research conducted after the scheduled not-before threshold, actual first ball unverified.

**SPORTS_ONLY_MARKET_BLIND:** YES (no odds inputs) · **OUTCOME_EXPOSURE:** NO_MATCH_OUTCOME_SEEN_AT_CARD_BUILD, ACTUAL_START_UNVERIFIED · **SETTLEMENT:** NOT_PERFORMED · **CANONICAL_IMPORT:** PENDING / NOT_PERFORMED
<!-- END CARD LOCAL-20261112CC53B5C806-G0003 -->

<!-- BEGIN CARD LOCAL-20261112CC53B5C806-G0004 -->
## Card · LOCAL-20261112CC53B5C806-G0004 · Basketball / WNBL · Geelong Venom (W) vs Perth Lynx (W) · 2026-11-13

- **Local event key:** `LOCAL-20261112CC53B5C806-G0004` — `LOCAL_UNIMPORTED_EVENT`; no canonical ID.
- **Canonical ID / stage:** `NOT_ASSIGNED` / `PROMPT_4_IMPORT` (NOT_RUN).
- **Event/native identity/aliases:** WNBL 2026/27 regular season Round 5, Geelong Venom home versus Perth Lynx, Microkeeper Arena, 2026-11-13 19:00 AEDT; native game-centre ID NOT_VERIFIED. Owner aliases `Geelong Venom(W)`, `Perth Lynx(W)`.
- **Authority:** GitHub `danisgreat/Sports-Research`, pinned public `main` snapshot `008cedc4ff469e7a808292aa3667a7bffe22e273`, `MDS/P v24.16`, forecast control `CR-2026.11.11-R4`, later records change `CR-2026.11.12-R1`, prompt `P-2026.11.11-v24.14`, scoring `SCV-2026.11.11-v13`, selection `SEL-2026.10.22-v4`; chat-local OWNER override = no repository write/commit/push.
- **Probability method:** `UNCALIBRATED_QUALITATIVE`. A separately executed `EXPLORATORY_JOINT_BASKETBALL_SHADOW` produces conditional probabilities, not `p_card` and not an issued GitHub `ml reference` or prospective pregame freeze. 1,200,000 actual RNG paths, seed `202611131849`, with documented regulation-score and overtime logic; evidence, code and JSON attached. No independently qualified WNBL model or actual GitHub `ml` run.
- **Learning record:** `LEARN_RECORD_INCOMPLETE`: both sides' available 2026/27 season matches recorded (5 and 4), coach/availability snapshots and published sources; FIBA-40 pace/four-factor denominators, historical L10/L15/L20 and native archive were not independently admitted; no committed LEARN-v2 feature/availability pack.
- **Future learning:** `PENDING_SETTLEMENT / BLOCKED_PENDING_ISSUANCE_CUSTODY`: result, scoring and exact event ID can later be recovered, but this chat-local card cannot become a retrospectively frozen original.
- **Analysis status:** `UNCALIBRATED_QUALITATIVE` with supporting shadow; `INFORMATION_INCOMPLETE` in formally required fields.
- **Timing:** User request ~2026-11-13 18:49 AEDT (minute precision); official scheduled 19:00 AEDT; research sources and independent simulation captured prior to scheduled start; actual first-play time NOT_VERIFIED. This local file has NO_REMOTE_FREEZE and no issued prospective reference. Actual append time documented in update receipt, not fabricated in this card.
- **Scheduled start:** 2026-11-13T19:00:00+11:00 Australia/Melbourne/Australia/Sydney = 2026-11-13T08:00:00Z. Microkeeper Arena, Geelong, Victoria, Australia. Official event page: https://www.wnbl.com.au/news/how-to-watch-geelong-v-perth ; official schedule https://schedule.nbl.com.au/wnbl .
- **Schedule state:** listed upcoming when checked; event may delay; exact live lineup/pregame release and true first-play state not independently verified. No target outcome used.
- **Endpoint/definition:** Full game including any five-minute overtime (`BK-OT-1` frozen framework convention); Geelong +6.5 covers if final Geelong points +6.5 > Perth points; Perth −6.5 covers if Perth wins by >=7; total Over163.5 requires >=164 combined; Under <=163. No push for .5 full-game lines; void/abandonment operator terms NOT_VERIFIED. Two-sided winner likewise full game incl OT.
- **Distribution object:** `EXPLORATORY_JOINT_BASKETBALL_SHADOW`, Gaussian regulation joint total and Perth-minus-Geelong margin, independent correlation assumption rho=0 (unfitted); integer team scores, when regulation tied simulate repeated Poisson(10.3) per side per 5-minute overtime until non-tie. FIBA-40 family prior SD 17.93 total /13.97 margin widened ×1.10 = 19.723/15.367, NOT WNBL-validated. Three input regimes low/base/high: mu_total 155/165.5/176, mu_Perth_margin 0/1.81/5.5, transparent weights 0.25/0.50/0.25. Regulation mean total offset by -0.55 to account for OT; any full-game forecast is an approximation. Program `wnbl_shadow_geelong_perth_20261113.py`, output `WNBL_SHADOW_DIAGNOSTIC_20261112CC53B5C806-G0004.json`.
- **Expected score:** exploratory mixture Geelong 81.62, Perth 83.92, total 165.54, signed Perth margin +2.29, SD_total input 19.723 and SD_margin input 15.367 (mixture SD actually wider owing to differing scenario centres; no falsely asserted modelled post-OT exact SD). `p_card` expected-score object NOT_COMPUTED.
- **Baseline:** `BASELINE_LEAGUE_V1_UNAVAILABLE` exact WNBL competition row not available in pinned `COMPETITION_PARAMETERS.csv`; the FIBA-40 family prior is an external-competition uncalibrated sensitivity comparator, not promoted to a frozen same-line `BASELINE_P`.
- **Regime/context:** WNBL regular season Round 5, FIBA-40 minutes (four 10-minute quarters), extra periods 5 minutes; early season team samples 5 vs 4; home venue Geelong; recent slower Geelong pace proxy / higher-scoring Perth pace proxy; Geelong key guard Bec Cole out lower leg through Round 7 per freshest official article; Maddy Rocci returned from foot injury as of Nov4; Han Xu 23 ppg as of Nov13; Perth Georgia Amoore scoring/assists, roster includes Maley, Peters, Key; Sami Whitcomb out season (knee) but absent from active day roster, WNBL preview shows no *additional game-day* absences. Opposite-team matchup for Han against former club is narrative, not a numeric effect.
- **Starter/bench state:** `LINEUP_UNCONFIRMED` for both sides. Official game preview gives expected depth charts, NOT a confirmed first five. Named rotation and out statuses in A3; no fabricated minute restriction or late scratch.
- **Pricing basis:** `SHADOW_ONLY`; the 0.25/0.50/0.25 regime mixture is a sensitivity device, not a frozen WNBL historical likelihood fit or primary distribution. No numeric gates achieved; formal row `p_card=NOT_ESTIMATED`.
- **Form windows:** 2026/27 available league games only: Geelong L5 2–3, PF 75.2, PA 79.8, combined155.0 (n=5); L10/L15/L20 each observed n=5 only and do NOT imply 10/15/20 independent 2026/27 games. Perth L5 observed 3–1, PF89.0 PA87.0, combined176.0 (n=4); L10/L15/L20 each observed n=4 only. Previous season matches deliberately not pooled without current-roster reconciliation. League-level verified mean and pace denominators unavailable.
- **Settlement capture:** later official WNBL game centre quarter-by-quarter/final after OT plus second provider, actual start/venue, substitutions and injuries. No scheduled task or background monitoring created.
- **Known-at:** official 13 Nov WNBL preview and 10 Nov injury/score features available before requested 19:00; exact individual source update timestamps sometimes missing, not proof of point-in-time archival retention. No outcome exposure at source capture; late injury change still possible.

### Decision block

**Directional choice:** Geelong Venom +6.5 full-game points is the least fragile of the four supplied rows in the executed sensitivity experiment (60.5% across the three declared hypothetical scoring environments; 52.4–66.1% in individual scenarios). The Lynx remain favoured to win outright (~55.9% exploratory); Geelong's cushion benefits from Han Xu interior production, home court and more rest, but Perth's high scoring and Geelong's Cole absence are live failure routes. No `PASS`/high-confidence label warranted.

| Rank | Role | Tag | Contract key / exact proposition | p_card | p_base | BASELINE_P | Line distance (units / z) | Probability basis | Main failure route |
|---|---|---|---|---|---|---|---|---|---|
| 1 | PICK (directional) | SUPPLIED | `GEE_PLUS_6_5`: Geelong +6.5 full-game spread | NOT_ESTIMATED | NOT_COMPUTED | BASELINE_UNAVAILABLE | line Perth margin +6.5 minus shadow centre +2.29 = +4.21 / z ≈ 0.27 (sensitivity only) | QUALITATIVE; shadow 60.54%, range 52.41–66.12% | Perth's shooters convert, second-chance deficit, late fouls / 7+ margin |
| 2 | PICK (directional) | SUPPLIED | `TOTAL_OVER_163_5`: combined full-game >=164 | NOT_ESTIMATED | NOT_COMPUTED | BASELINE_UNAVAILABLE | shadow centre 165.54 minus 163.5 = 2.04 / z ≈ +0.10 | QUALITATIVE; shadow 53.58%, range 33.48–73.35% | Geelong controls tempo; both teams face slower interior possessions |
| – | INFORMATIONAL | SUPPLIED | `TOTAL_UNDER_163_5`: combined full-game <=163 | NOT_ESTIMATED | NOT_COMPUTED | BASELINE_UNAVAILABLE | same full-game centre | QUALITATIVE; shadow 46.42%, range 26.65–66.52% | Perth raises possessions, hot shooting or OT |
| – | INFORMATIONAL | SUPPLIED | `PER_MINUS_6_5`: Perth final win margin >=7 | NOT_ESTIMATED | NOT_COMPUTED | BASELINE_UNAVAILABLE | same margin centre | QUALITATIVE; shadow 39.46%, range 33.88–47.59% | Geelong's size/rebounding and home cushion, late narrowing |

**Rank-1 gate:** `NOT_ASSESSABLE` (p_card absent, WNBL benchmark/eligibility and primary reference/freeze not executed); shadow mixture 0.6054 below indicative 0.65 strong threshold in any event. **Rank-2 floor:** NOT_ASSESSABLE. **BASELINE_P coverage:** 0/0 numeric primary rows. **Expected winner:** shadow Perth 55.87%, Geelong 44.13% (NOT_PRIMARY); no draw after OT. **Joint failure:** shadow P(Geelong +6.5 fails AND Over163.5 fails) = 17.90% (same simulation states); correlation is not 0 even though normal total and margin latent shocks are drawn independently, because threshold conditions and OT are linked through final scores. **Adjustment dependence:** SCENARIO_SENSITIVE; no formally priced effect-table rows; scenario weights are not fitted. **Shadow gates:** NOT_PRIMARY, no model release run. **Supplied unselected:** Perth -6.5 and Under163.5 retained as full evaluated opposing rows. **Abstain flag:** NO_STRONG_PICK.

### Appendix

#### A1. Identity, venue, format, timing and duplicate check

Owner request preserved exactly:

```text
Upcoming Basketball Game: Geelong Venom(W) vs Perth Lynx(W), Australia WNBL,
Estimated Game Time Start: 13 November 2026, 7:00 PM AEDT (can be delayed so continue the process as normal)

Venom(W) +6.5
Lynx(W) -6.5
Combined Total: Over/Under 163.5 Points
```

Official WNBL preview confirms the venue and 19:00 AEDT start, with matching league schedule. Round 5, 2026/27, Geelong home, Perth away. WNBL uses FIBA/40-minute four-quarter rules with 5-min OT; framework rule BK-OT-1 includes overtime in all full-game contracts. `G0001`, `G0002`, `G0003` are other sports/events; this is a fresh unique event `G0004`. The venue's recent naming has alternate alias Geelong Arena/Microkeeper Arena; official current sponsor name takes precedence. Native game-centre event ID and actual first possession unverified. No verified live score or result used.

#### A2. Exact supplied contract definitions and candidate recipe

Four propositions all for *full game incl OT*: `GEE_PLUS_6_5` Geelong final point margin >= -6, `PER_MINUS_6_5` Perth final margin >= +7, `TOTAL_OVER_163_5` combined >=164, `TOTAL_UNDER_163_5` combined <=163. Because points are integer and lines 0.5, none pushes; opposite rows are complementary conditional on a completed non-void game. Abandonment and named bookmaker void terms unknown and cannot be inferred; internal sport endpoint fixed by BK-OT-1.

Rank scope `SUPPLIED_ONLY`. Pairing Geelong cushion + Over is a shared-state pair not two independent evidence pieces. Separate winner probabilities are informational only.

#### A3. Current evidence: results, depth, availability, opponent context, historical source reliability

**Opened/verifiable schedule and score-source rows through 13 Nov 2026 before scheduled start:**

| 2026 date | Venue / side | Opponent | Geelong PF–PA (regular season) | Combined | Source |
|---|---|---|---|---:|---|
| 15 Oct | Away | Tasmania Jewels | 90–103 | 193 | https://schedule.nbl.com.au/wnbl |
| 24 Oct | Home | Southside Melbourne Flyers | 74–69 | 143 | https://schedule.nbl.com.au/wnbl |
| 31 Oct | Home | UC Capitals | 68–77 | 145 | https://schedule.nbl.com.au/wnbl |
| 2 Nov | Away | Bendigo Spirit | 77–70 | 147 | https://schedule.nbl.com.au/wnbl |
| 5 Nov | Home | Townsville Fire | 67–80 | 147 | https://schedule.nbl.com.au/wnbl |

| 2026 date | Venue / side | Opponent | Perth PF–PA (regular season) | Combined | Source |
|---|---|---|---|---:|---|
| 17 Oct | Home | Townsville Fire | 86–83 | 169 | https://schedule.nbl.com.au/wnbl |
| 24 Oct | Away | Adelaide Lightning | 90–82 | 172 | https://www.sofascore.com/basketball/match/perth-lynx-adelaide-lightning/RQYsiRY ; official schedule corroboration |
| 3 Nov | Away | Townsville Fire | 86–99 | 185 | https://schedule.nbl.com.au/wnbl |
| 10 Nov | Home | Bendigo Spirit | 94–84 | 178 | https://www.wnbl.com.au/news/lynx-hold-strong-to-overcome-spirit |

**Verified windows with true n:** 2026/27 Geelong L5 n5 2–3, last-three PF (68+77+67)/3=70.67, PA (77+70+80)/3=75.67, total 146.33. Perth L5 n4 3–1, last-three PF (90+86+94)/3=90.0, PA(82+99+84)/3=88.33, total178.33. L10/L15/L20 *present season* n5/n4 and not independently complete; previous-season L10/15/20 not admitted due player transfers. Geelong home n3 GF69.67 GA75.33 total145.0; Perth away n2 GF88 GA90.5 total178.5. Date/source of 2025/26 H2H: 28 Dec 2025 Perth 106–78 Geelong (basketball.com.au, superseded roster). Do not count H2H as an independent current-team forecast due Han Xu transferring from Perth to Geelong and other changes.

**Common opponent / matchup:** Townsville defeated both teams by 13 in their latest encounters (Geelong 67–80 at home; Perth 86–99 away). Perth defeated Bendigo by 10 at home while Geelong defeated Bendigo by 7 away; the Perth win came against an eight-player, injury-depleted Bendigo group, limiting margin inference (WNBL official November 10 feature). Opponent level matters more than raw PF/PA averages, but neither two-team common-opponent set is a fitted adjustment.

**Expected rotations from official WNBL Nov 13 preview, not confirmed five:**

- Geelong point guards Maddison Rocci / Lilly Rotunno / Millicent McCarthy; shooting guards Indiah Bowyer / Dakota Crichton / Jasmine King / Bec Cole (OUT); wings Wanglai Zhang / Aleks Connolly / Poppy Stevens; forwards Alex Sharp / Sara-Rose Smith; centres Han Xu / Mackenzie Clinch Hoycard. Role allocations from official *expected* chart, not per-match minutes.
- Perth point guards Georgia Amoore / Samantha Ashby; guards Alex Ciabattoni / Steph Gorman / Kyana Weir; wings Haley Peters / Chloe Hodges / Reece Anticevic; forwards Anneli Maley / Brooke Malone; centres Teonni Key / Teige Morrell. No confirmed starters or minutes restrictions.

**Injuries/availability:** Official Nov13 WNBL feature explicitly calls Bec Cole OUT, lower leg, Round 7 return estimate, replaced by Millicent McCarthy; a 10-Nov third-party mirror still suggested Round 5, superseded for this event. Official 4-Nov report cleared Rocci for return after a foot injury, but same-day minutes not confirmed. Perth official match-day article lists *no injuries*; Samantha Whitcomb (Sami Whitcomb) was ruled out for the season Aug27 with knee injury, remains an absent contracted player but not a new game-day scratch. No evidence of fresh medical restrictions for Han, Amoore, Maley, Peters or Key; *not listed injured* != confirmed fit. Coaches: Geelong Cheryl Chambers, Perth Ryan Petrik. Han Xu 23 ppg, ~56% FG per official 13-Nov preview, former Perth player; Georgia Amoore has >=6 assists all four games, 23.5 ppg in last two according to same preview. No documented starter confirmation.

**Rest/travel:** Geelong last played Nov5, eight calendar days prior; Perth last played Nov10, three calendar days prior; Perth crosses from WA to VIC for this away game. Physiological effect size not measured here. No back-to-back for either. Indoor arena makes outdoor weather not applicable. Referee crew and official last-minute scratched player list not verified. Early-season sample and opposing pace/total distributions warrant width inflation.

#### A4. Baseline, expected score, procedures, joint distribution and sensitivity

**Source arithmetic (not pace-adjusted):** Geelong PF=376/5=75.2, PA=399/5=79.8, avg total=155.0, margin=-4.6. Perth PF=356/4=89.0, PA=348/4=87.0, avg total=176.0, margin=+2.0. Equal-attack/defence matchup score from these tiny team samples = Geelong (75.2+87.0)/2=81.1, Perth (89.0+79.8)/2=84.4, aggregate165.5, Perth +3.3 before any venue correction. FIBA-40 family median home margin 1.49 from pinned GitHub `COMPETITION_PARAMETERS.csv` is a non-WNBL proxy, yielding indicative central Perth margin 3.3-1.49=+1.81. This is not opponent-adjusted ORtg/DRtg. Independent possessions, pace, offensive/defensive rating numerators, shot mix, 3PA%, turnover/rebound rates, FTA and verified lineup-minute inputs missing; cannot claim a fitted possession model.

**Family prior:** GitHub parameters row `FAMILY_PRIOR:BASKETBALL_FIBA40`: total mean166.65; raw total sd17.93, raw margin sd13.97; family prior is not a WNBL league-only baseline. Since no `Basketball/WNBL` exact league row exists at the pinned commit, exploratory sd(total)=17.93×1.10=19.723 and sd(margin)=13.97×1.10=15.367, with NO sanctioned numeric primary `BASELINE_P`/width-floor certification. Low/base/high total centres 155.0/165.5/176.0 reflect Geelong/attack-defence midpoint/Perth; signed Perth margin 0/1.81/5.5 is a sensitivity span with no fitted probabilities. Default 0.25/0.50/0.25 mixture weights are an *assumption*, not estimated odds. A formal WNBL future study must measure context, dispersion and covariances independently.

**Actually executed exploratory algorithm:** NumPy seeded RNG `202611131849`; 300,000/600,000/300,000 full-match paths; each draws regulation total Gaussian with mean target−0.55 and SD19.723 plus signed margin Gaussian with mean scenario (0/1.81/5.5) and SD15.367; rho assumed0 (unfitted). Score transformation rounds individual scores: Geelong=round((total−margin)/2), Perth=round((total+margin)/2). Any rounded 40-minute tie starts FIBA five-minute OT: each team Poisson mean10.3 points independently per extra period, iterate until a winner. Total OT incidence 2.56% in this exploratory sample. This is a simplified score-level challenger not a full possession/efficiency/stint simulator; 5-min overtime means reflect 40-min pace proxy but are not a measured WNBL OT dataset. No prices, bookmaker moves, live scores or outcome observations used.

| Scenario | n | P(Geelong +6.5) | P(Perth −6.5) | P(Over163.5) | P(Under163.5) |
|---|---:|---:|---:|---:|---:|
| Lower-scoring Geelong control | 300,000 | 66.12% | 33.88% | 33.48% | 66.52% |
| Matchup-centred | 600,000 | 61.81% | 38.19% | 53.75% | 46.25% |
| Higher-scoring Perth tempo | 300,000 | 52.41% | 47.59% | 73.35% | 26.65% |
| **Scenario-weighted** | **1,200,000** | **60.54%** | **39.46%** | **53.58%** | **46.42%** |

**Shadow expected outcome:** Geelong81.62–Perth83.92, combined165.54, Perth margin2.29; P(Perth winner)=55.87%, P(Geelong winner)=44.13%. Normal tail, scenario-centre mixture and overtime make SD of complete distribution greater/different from simple single-scenario inputs. All percentages are conditional, not empirically validated event probabilities or `p_card`.

**Team-score budget at O/U163.5:** if Geelong scores 70, Perth needs >=94 for Over; Geelong 80 -> Perth >=84; Geelong 90 -> Perth >=74. Thus Geelong suppressed scoring alone does not force Under if Perth converts 90+, and a tight Geelong 75–80 score may keep match close with either total. Perth −6.5 requires a 7+-point final gap; winning outright by <=6 does not cover. Overtime can lift Over but narrow/widen the handicap depending on who scores; late foul and bench effects are not separately fitted.

**Sensitivity / width:** low/base/high case shows Geelong +6.5 retains majority *conditional* support (52.4–66.1%) but Over163.5 flips drastically (33.5–73.3%). Observed season scoring ranges overlap, correlated with opponent strength, lineup regime, shot quality; cannot infer safe total from season-average 165.5. Formal exact WNBL reference and adjustment effect table unavailable to execute. League-only numeric baseline attempt = FAIL_NO_COMPETITION_ROW; source first-team scores available but not valid independent historical league cohort. No claim of running `python -m ml reference` or `ml pregame` from the GitHub repo.

#### A5. All supplied lines, W/P/L/V, winner, risk and joint dependence

`GEE_PLUS_6_5`: strongest across low/base/high, because Geelong can lose by 1–6 and still cover; failure if Perth offensive bursts create 7+ gap, late fouling widens. Win/lose (completed, non-void) = 60.54%/39.46% CONDITIONAL EXPLORATORY SHADOW; push=0, void unknown.

`PER_MINUS_6_5`: can win outright yet fail by ≤6, including late narrowing or overtime one-possession win. Shadow 39.46%/60.54%, push=0, void unknown. Raw 3-1 Perth record not proof of covering 7+.

`TOTAL_OVER_163_5`: slight base-case lean; requires >=164 including OT, 80+84 or 70+94 type budgets; vulnerable to Geelong's three consecutive slow home totals. Shadow 53.58%/46.42%, push=0, void unknown.

`TOTAL_UNDER_163_5`: supported by Geelong's home 143/145/147, stronger defensive interior with Han; can fail if Perth's 90+ pace/shotmaking or overtime. Shadow 46.42%/53.58%, push=0, void unknown.

**Joint probability:** P(Geelong +6.5 fails AND Over 163.5 fails) = P(Perth≥7 margin AND total<=163)=17.90% in the same shared scoring paths, no factorised multiplier. Geelong-cushion + Over does not qualify as 2 independent picks. Loss for both Geelong+6.5 and Under163.5 = 21.56%, distinct event, from same grid. Source cards remain non-repository, not officially issued.

#### A6. Adjustment ledger / venue, absences and comparator

Formal v24 `LEDGER-v1` **not executed**: no WNBL-matched frozen `REFMODEL-v1` reference receipt, no permitted WNBL-specific effect entries with source-qualified durations. No numeric subtraction for Cole, Whitcomb, Han-v-former-team, Rocci clearance, Perth travel or coaching; they inform *scenario width and direction* only. The FIBA40 proxy home margin 1.49 is explicitly labelled from median family prior, not an official WNBL measured effect. Unlike previous seasons, Geelong now fields Han Xu (formerly Perth), so prior H2H roster identities should not be silently imported as current skill.

#### A7. Family checks and alternate state branches

All paired half-point contracts complement exactly in the executed paths, and all matches finish with a winner after OT. Input score object is common to total/spread/winner markets; it does not conflate a Perth win with Perth −6.5. Complete-state model excludes explicit possession-based shooting/turnover/special teams equivalents, minute restrictions, foul counts, transition bursts, bench scoring, late intentional fouls and blowout-garbage-time mechanisms; these are material limitations. Scenario low/base/high brackets part of that risk. The framework labels `no strong pick` unless calibrated primary risk gates pass; neither did. Primary model shadow disposition: `NOT_RUN_NO_LOCAL_REPOSITORY_EXECUTION` (custom independent research diagnostic is separate, source and output hashes in appendix/receipt). No formal numeric `BASELINE_P`, stable rank-1 pass or published p.

#### A8. Source register, missingness, evidence freshness and settlement capture

| Source URL | Field covered | Limit and follow-up |
|---|---|---|
| https://www.wnbl.com.au/news/how-to-watch-geelong-v-perth | Official Nov13 tip, arena, roster depth, Cole OUT, Perth no *new* absences, Han/Amoore current profile | Live starters/bench and publication-at exact minute not established |
| https://schedule.nbl.com.au/wnbl | Official fixture and both sides' five/four completed WNBL27 matches | Some rendered cached schedule team filters inconsistent: use date scores, exclude preseason |
| https://www.wnbl.com.au/news/lynx-hold-strong-to-overcome-spirit | Perth Nov10 94-84, Amoore 27pts/6 threes/6ast, Maley14pts/13reb, Bendigo 8-player depleted | Game specific, not a pace/ORTG population estimate |
| https://www.wnbl.com.au/news/geelong-venom-receive-massive-injury-boost-maddy-rocci | Nov4 Rocci cleared from foot injury | Not minute allocation or guaranteed starting status |
| https://www.wnbl.com.au/news/injury-strikes-down-geelong-venom-guard-bec-cole | Oct23 Cole injured lower leg, replacement | Return revised in Nov13 preview to Round7; prefer freshest official |
| https://www.basketball.com.au/news/wnbl-injury-report | Nov10 league injury tracker, Whitcomb season long knee issue | Third-party update predates Nov13 official Cole timetable; not a confirmed player healthy list |
| https://www.sofascore.com/basketball/match/perth-lynx-adelaide-lightning/RQYsiRY | Perth away Adelaide 90-82 Oct24 | Independent live page can update, known-at exact not frozen |
| https://www.basketball.com.au/news/complete-2025-26-wnbl-season-schedule-and-fixture-list-of-all-92-regular-season-games | H2H prior Dec28 Perth106-78 Geelong | Historical 2025/26 different rosters; no direct numeric carryover |
| https://github.com/danisgreat/Sports-Research/blob/008cedc4ff469e7a808292aa3667a7bffe22e273/research/competition_parameters/COMPETITION_PARAMETERS.csv | FIBA-40 family variance/home-margin prior, WNBL row absent | Repo read-only, no `ml reference` execution or committed frozen baseline |

Research access was web search with indexed official previews and league schedule; direct open of one WNBL preview returned cache-miss (alternative indexed official extract used), not represented as a full page open. No claim of source-audit CLI run or publication-time capture beyond observed listing. Sources used strictly sports results/news/rosters and repo, **no sportsbook, market odds or tip-site projections** fed analysis.

**Unresolved:** same-day official starting lineups, late scratches/medical minutes and bench availability; exact current possession counts and opponent-adjusted ORtg/DRtg; actual local first-tip; precise 2026/27 WNBL league pace/variance/OT rate; extended true dated L10/L15/L20 across roster changes; official native game-centre ID; opening of full boxscore and source timestamps; competition-specific published baseline, execution receipt, and remote freeze. A user may ask for settlement later. To settle: fetch final WNBL Game Centre exact quarter/final/OT breakdown and independent cross-check, record true final and actual start if evidence, apply BK-OT-1. No automation set and no future background action implied.

#### A9. Integrity, custody, seven steps, and research-completion matrix

| Required procedure | Actual findings/actions | Gap / next field | Status |
|---|---|---|---|
| Authority / identity / duplicates / schedule | Pinned main SHA/rules, official WNBL Nov13 Round5 home Geelong, distinct G0004 | exact native game ID, actual first-play minute | DONE_WITH_GAPS |
| Both-side availability / starters / bench / recheck | Official Nov13 expected rotations; Cole out, Whitcomb season out, Rocci cleared; no new Perth day-out on official preview | No confirmed fives, final late scratch/minutes/fit | INFORMATION_INCOMPLETE |
| Online historical facts and source comparison | Official schedule 5+4 league results; third-party Adelaide cross-check, Bendigo official write-up | Some source publication-at precision and dated complete history | INFORMATION_INCOMPLETE |
| L5/L10/L15/L20 + league | Geelong n5 and Perth n4 current; computed PF/PA/home/away and latest 3; last year H2H contextual only | n10/n15/n20 true extended samples and measured league-level data | INFORMATION_INCOMPLETE |
| Basketball mechanisms and playing conditions | WNBL FIBA40, five-minute OT, rest/travel, mismatch, underdog cushion, pace contrast, late-foul budgets | Verified possessions/shot quality/rotation minutes | DONE_WITH_GAPS |
| Reference/official pregame freeze | Pinned FIBA40 prior row inspected; no WNBL row | No official frozen WNBL reference or GitHub pregame run; owner explicitly no Git changes | NOT_RUN |
| Model/arithmetic and scenario dependence | 1.2m actual Monte Carlo joint-score paths, three regimes, overtime loop, complete four rows | Uncalibrated prior/covariance, no independent skill qualification | SHADOW_EXECUTED |
| Exact four contracts and winner | Both handicap, both total, market blind, winning/losing sets and joint failure | Operator-specific abandonment/void terms | DONE_CONDITIONAL |
| Expected score/baseline/sensitivity | Score budget, mix mean, team estimates, 10% prior SD inflation, n/sensitivity, baseline failure explicit | True WNBL league baseline and full post-OT SD | SHADOW_ONLY |
| A1-A9, card readback/delivery, custody | Cumulative original mini and three existing card bodies must be byte preserved; append/readback receipts generated outside GitHub | No repository linter/freeze/commit/push, intentionally | CHAT_LOCAL_DRAFT |

**Overall:** `INFORMATION_INCOMPLETE / RESEARCH_COMPLETED_WITH_EXPLICIT_GAPS`; numerical disposition `EXPLORATORY_SHADOW_EXECUTED / PRIMARY_NOT_RUN`; selection `UNCALIBRATED_QUALITATIVE / NO_STRONG_PICK`; delivery `CHAT_LOCAL_READ_ONLY_DRAFT_NOT_ISSUED`; ranked directions not retrospectively certified if tipped before local append completes. No canonical allocation, GitHub publication, settlement, or scheduled future check.

**SPORTS_ONLY_MARKET_BLIND:** YES · **OUTCOME_EXPOSURE:** NO_MATCH_OUTCOME_SEEN; actual game-state not verified · **SETTLEMENT:** NOT_PERFORMED · **CANONICAL_IMPORT:** NOT_PERFORMED
<!-- END CARD LOCAL-20261112CC53B5C806-G0004 -->

<!-- BEGIN CARD LOCAL-20261112CC53B5C806-G0005 -->
## Card · LOCAL-20261112CC53B5C806-G0005 · Basketball / Korea KBL · Wonju DB Promy vs Suwon KT Sonicboom · 2026-11-13 KST

- **Local event key:** `LOCAL-20261112CC53B5C806-G0005` — `LOCAL_UNIMPORTED_EVENT`.
- **Canonical ID / assignment stage:** `NOT_ASSIGNED` / `PROMPT_4_IMPORT`.
- **Authority:** `PUBLISHED_MAIN_PINNED` GitHub `main` SHA `008cedc4ff469e7a808292aa3667a7bffe22e273`; MDS v24.16, control CR-2026.11.11-R4, records CR-2026.11.12-R1, scoring SCV-2026.11.11-v13, selection SEL-2026.10.22-v4, prompt P-2026.11.11-v24.14. Owner's chat-local read-only override; no working tree or published freeze.
- **Game identity / aliases:** 2026–27 Korean Basketball League regular season, Wonju DB Promy/Dongbu Promy (home) vs Suwon KT Sonicboom/KT (away), exact matching StatGG game `S49G01N66`; official KBL schedule November 13, 19:00 Korea Standard Time, Wonju DB Promy Arena, Wonju, Republic of Korea. Native KBL game identifier not separately confirmed.
- **User-requested start:** 2026-11-13 21:00 AEDT (UTC+11) = 19:00 KST (UTC+09) = 10:00 UTC. User request arrived about 20:54 AEDT, estimated from supplied conversation context. Scheduled start verified; **actual first possession NOT_VERIFIED**, no GitHub pregame freeze. Do not treat work performed after scheduled tip as an issued pregame forecast.
- **Competition / regulation:** Korean KBL 2026–27, FIBA-derived 4×10-minute regulation, 5-minute overtime as needed; every full-game spread and total **includes overtime** under framework BK-OT-1 (`FROZEN_FRAMEWORK_CONVENTION`). No half or quarter contracts.
- **Issue status:** `UNCALIBRATED_QUALITATIVE / READ_ONLY_DRAFT / NOT_ISSUED_IN_REPOSITORY`. Any numeric figures are `EXPLORATORY_SHADOW_NOT_PRIMARY` and **not official p_card**, not a released predictive model, not independently qualified and not suitable for formal Rank-1 numerical gate. Original source publication times for some mutable pregame pages are unknown (`KNOWN_AT_UNVERIFIED`).
- **Model/source disposition:** GitHub `ml reference`, `ml pregame`, `ml card lint`, `ml learning-log` and freeze NOT_RUN (working repository/runtime unavailable; owner no-Git-change instruction). Separately executed **1,200,000-match** source-disclosed normal/scoreboard+OT shadow in `/mnt/data/kbl_shadow_wonju_suwon_20261113.py`, diagnostic `/mnt/data/KBL_SHADOW_DIAGNOSTIC_20261112CC53B5C806-G0005.json`; no fictitious model receipt.
- **Baseline:** `BASELINE_LEAGUE_V1 NOT_FORMALLY_FROZEN`. Main-branch historical KBL competition parameter: `Basketball/KBL`, development 1,080 rows, mean combined 159.39, raw total SD 17.93, raw margin SD 13.97, residual total 16.82, residual margin 12.61; `HISTORICAL_DEVELOPMENT_UNADMITTED` (not current season and not predictive qualification). Current 2026–27 13-game team records and external league scoring reference around 171.4 indicate scoring-regime shift; exact current-league cohort/row dates not audited. Shadow uses historical family widths inflated 10%, not a formal league baseline. Do not promote old KBL 159.39 mean to current expected total.
- **Learning record:** `LEARN_RECORD_INCOMPLETE`: precise dated L5 results and standings retained below; independently audited L10 dated row set, all current-season games, lineups, and feature source-time fields not fully acquired. Future learning PENDING_SETTLEMENT and independently verified known-at gate.
- **Expected result (shadow only):** Wonju ~91.30, Suwon ~85.28, combined ~176.58, signed home margin ~+6.02; total SD ~20.69, margin SD ~15.46. Descriptive means, not exact score picks.
- **Cutoff and outcome exposure:** Calculations use only historical results through 2026-11-09, official 13-Nov pregame news and no 13-Nov live game states; checked source pages showed `upcoming` without target score. Actual first possession not independently timestamped. Research/append timestamps are recorded in local append receipt; no prospective freeze claimed.

### Decision block

**Decision:** Under 179.5 total points is the **least fragile directional lean**, but remains LOW confidence and fails the framework's 0.65 strong-pick convention. Wonju has a plausible home advantage, especially with Henry Ellenson expected back and several Suwon absences, but **Wonju −5.5 sits almost on the estimated margin** and has no robust support. No high-confidence single or multi-leg position is justified.

| Rank | Role | Tag | Contract / exact proposition | Primary p_card | Primary p_base | BASELINE_P | Shadow diagnostic only | Principal failure route |
|---|---|---|---|---|---|---|---|---|
| 1 | PICK (conditional direction) | SUPPLIED | `TOTAL_UNDER_179_5`: combined final including OT ≤179 | NOT_ESTIMATED | NOT_COMPUTED | NOT_FROZEN | **55.88%**, sensitivity 40.38–68.40% | Ellenson return and Bass/KT perimeter shooting produce 180+; late fouls/OT |
| 2 | PICK (weak directional only) | SUPPLIED | `WONJU_MINUS_5_5`: Wonju final margin ≥6 | NOT_ESTIMATED | NOT_COMPUTED | NOT_FROZEN | **51.57%**, sensitivity 48.44–58.01% | KT stays within 5, or wins, via rebounding/Paris Bass scoring |
| – | INFORMATIONAL | SUPPLIED | `SUWON_PLUS_5_5`: Suwon loses by ≤5 or wins | NOT_ESTIMATED | NOT_COMPUTED | NOT_FROZEN | **48.43%**, sensitivity 41.99–51.56% | Wonju transition and paint advantage becomes 6+ |
| – | INFORMATIONAL | SUPPLIED | `TOTAL_OVER_179_5`: combined final including OT ≥180 | NOT_ESTIMATED | NOT_COMPUTED | NOT_FROZEN | **44.12%**, sensitivity 31.60–59.62% | Short rotation and offensive suppression limit scoring |

**Winner (shadow only):** Wonju 65.15%, Suwon 34.85%. **Strong-pick gate:** `NOT_ASSESSABLE`; no calibrated/formally frozen primary probability and the exploratory leading direction <0.65. **Rank-2 floor:** NOT_ASSESSABLE. **Primary baseline coverage:** 0/0 numeric ranked rows. **Model shadow:** independently executed conditional Monte Carlo, **not an MLSCOPE-v3 GitHub shadow release**. **Adjustment dependence:** scenario-dependent; ranked Under flips in high-scoring scenario. **Joint failure:** for chosen directional Under and Wonju−5.5, both lose when `total≥180 AND Wonju margin≤5`; approximate complement joint must be read from shared simulation array (not reported as exact without calculation). **Exact supplied contracts:** all four mutually complementary propositions accounted for; no push at half-point lines; no void assumed outside applicable abandonment/operator terms.

### Appendix

#### A1. Identity, event state and exact user contracts

Owner request: `Upcoming Basketball Game: Wonju Promy vs Suwon Sonicboom, Korea KBL; Estimated Game Time Start: 13 November 2026, 9:00 PM AEDT; Promy -5.5; Sonicboom +5.5; Combined Total: Over/Under 179.5 Points`. Both clubs' unambiguous official names resolved; 13-Nov KBL game, not the earlier 23-Oct meeting. 19:00 KST venue Wonju DB Promy Arena confirmed by KBL schedule (`https://www.kbl.or.kr/match/schedule`) and independent StatGG game `S49G01N66` (`https://statgg.com/en/kbl/matches/S49G01N66`). Actual start, official active list and contemporaneous live/event state NOT_VERIFIED at append; the existence of a planned 19:00 start does not certify pre-start issuance. MARKET_BLIND: no prices used.

#### A2. Frozen supplied contracts, endpoints and action

| Key | Proposition | W/L/P/V mechanism | Source of status |
|---|---|---|---|
| WONJU_MINUS_5_5 | `DB − KT ≥ 6` | WIN if ≥6, LOSS if ≤5; PUSH impossible on half point | exact owner line; final incl OT |
| SUWON_PLUS_5_5 | `DB − KT ≤ 5` | complement of Wonju −5.5, not a second independent signal | exact owner line; final incl OT |
| TOTAL_OVER_179_5 | `DB + KT ≥ 180` | WIN if ≥180, LOSS if ≤179 | exact owner line; final incl OT |
| TOTAL_UNDER_179_5 | `DB + KT ≤ 179` | complement of Over 179.5 | exact owner line; final incl OT |

Both line pairs use full-match basket scoring and five-minute overtime under BK-OT-1. Exact operator cancellation/abandonment convention is not supplied; no VOID assessment can be made.

#### A3. Sources, actual dated form, personnel and known-at

**Pre-event standings / pace.** StatGG 13-Nov matchup snapshot: DB 7–6, 90.1 PF/89.3 PA, home 3–2; KT 6–7, 85.0 PF/86.5 PA, away 3–4; records through 13 games each. StatGG source reports pace 77.2 DB and 72.7 KT, ORtg 113.8 vs 111.8, DRtg 113.1 vs 116.7; provider's pace/efficiency scale is unverified against raw totals, so used directionally only. `https://statgg.com/en/kbl/matches/S49G01N66`. Separate primary pregame schedules on `https://www.kbl.or.kr/match/schedule` and `https://promy.kbl.or.kr/match/schedule`.

**Last five official-season results before target** (score shown in team's perspective, W/L from that team's side; AiScore dated list corroborated against another pregame results source):

| Wonju date (KST) | Opponent | Wonju–opponent | Result | Combined |
|---|---|---|---|---|
| 2026-11-08 | Seoul SK | 65–81 | L | 146 |
| 2026-11-07 | Seoul Samsung | 84–76 | W | 160 |
| 2026-11-01 | Changwon LG | 104–98 | W | 202 |
| 2026-10-31 | Busan KCC | 74–90 | L | 164 |
| 2026-10-28 | Daegu KOGAS | 90–95 (OT) | L | 185 |

| Suwon date (KST) | Opponent | Suwon–opponent | Result | Combined |
|---|---|---|---|---|
| 2026-11-09 | Seoul Samsung | 78–85 | L | 163 |
| 2026-11-07 | Daegu KOGAS | 92–81 | W | 173 |
| 2026-11-01 | Goyang Sono | 103–96 | W | 199 |
| 2026-10-31 | Anyang Red Boosters | 92–90 | W | 182 |
| 2026-10-25 | Seoul SK | 79–90 | L | 169 |

Rows: `https://www.aiscore.com/en/head-to-head/basketball/busan-ktf-sonicboom-vs-wonju-dongbu-promy`, corroborating `https://abasketballreport.com/predictions/head-to-head/2026-11-13/south-korea/kbl/wonju-db-promy/suwon-kt-sonicboom/NzAyNjMtNzAyNjI%3D` and 2026 season fixture/standings. **Overlapping form windows are not independent features.** Wonju L5 (n=5) PF83.4, PA88.0, total171.4; Suwon L5 (n=5) PF88.8, PA88.4, total177.2. Wonju L10 and Suwon L10 exact per-game dated rows not independently reconciled (n effective 0 verified complete). Current-season 13 games are a usable season summary only, not rebranded as individually verified L15/L20: season n=13, L15 and L20 **insufficient current-season 15/20**; full prior-season extension NOT_RECONSTRUCTED. One available aggregate provider lists last-10 numbers but not a full dated-rows audit, so it is withheld from quantitative fitting. KBL league scoring average around 171.4 on pregame schedule reference, cohort provenance incomplete; treat as context not exact audited league baseline.

**Head-to-head.** On 2026-10-23 Wonju won at Suwon 102–95 (197 combined), confirmed by StatGG and 13-Nov fixture source. Older 2025–26 H2H games had mostly closer margins; roster/season regime differs and they are not independently fitted. One H2H is descriptive, not a numerical adjustment.

**Availability / roles.** News published 2026-11-09 from Sports Chosun quotes DB club plans for Henry Ellenson (F/C) to return 13-Nov after concussion/headache protocol, first appearance since October 19; 13-Nov 10:45 KST Jumpball preview also calls it his return. **RETURN_EXPECTED, not a confirmed dressed/starting role**, with playing minutes restriction unknown; foreign lineup combinations with Ration Hammonds / Alan Williams unknown. DB leading on-ball guard E'Twaun/Lee Sean Alvano (name rendered differently by providers), scoring forward Ration Hammonds, Kang Sang-jae (reported unavailable), Jung Ho-young (reported ACL injury); DB starting five, selected bench and final scratches NOT_CONFIRMED.

KT: Kim Sun-hyung (G, surgical recovery), Ha Yun-gi (C, bone bruise/rehab), Miguel Oczon (G, appendicitis surgery Nov 6) reported **OUT** by 13-Nov Korean injury briefing; Jeong Chang-young (F) questionable after 9-Nov injury. Paris Bass (high-usage primary scorer, 39 points/15 rebounds in prior game) and backup foreign big are expected contributors, but their exact roles/starting status NOT_CONFIRMED. Sources: `https://www.dailyil.com/ko/briefing/2026-11-13_KBL/`, `https://www.dailyil.com/ko/games/kbl-2026-11-13-kt-db/`, `https://www.chosun.com/english/sports-en/2026/11/09/ZPWYKNMKAZH7BPW7KMZPUJGLKI/`, `https://www.jumpball.co.kr/news/newsview.php?ncode=1065577530368244`. This is secondary journalism/injury tracking; no official same-minute lineup or club medical bulletin retrieved. **KT availability is a major scoring and margin regime uncertainty.**

#### A4. Reference, score grid and sensitivity

`ANALYST_PRIMARY_V1` formal reference stage NOT_RUN: KBL not covered by current released NBA/WNBA/NBL TB-2 model; historical KBL competition row has inadmissible stale development evidence. No primary p_card reported. Standalone shadow calculation (script, JSON) uses one coherent synthetic joint scoreboard and the identical event paths for all four propositions. Inputs: DB season PF90.08, PA89.31, Suwon PF85.00, PA86.46; neutral matchup arithmetic centres (90.08+86.46)/2=88.27 DB, (85.00+89.31)/2=87.16 Suwon; modest home/rest and player-availability uncertainty in declared three scenarios. Independent regulation total/margin Gaussian innovations with standard deviations 17.93×1.10=19.723 and 13.97×1.10=15.367 from FIBA historical family-width sensitivity, rho=0.0 before scoreboard transform. Team scores = rounded clipped integers (T±M)/2; tied regulation scores add an approximate five-minute OT basket total (~21.5±7 points). This does **not** reproduce KBL exact possession/shot/foul and OT state rules and its weights are illustrative, not fitted. Explicit 25/50/25 scenario mixture is for sensitivity exploration only; formal primary mixture weights require stronger evidence.

| Predeclared sensitivity scenario | Weight | Regulation expected score DB–KT | Shadow P(Under179.5) | Shadow P(DB−5.5) |
|---|---:|---|---:|---:|
| KT injury-short-rotation / slower | 0.25 | 89.0–80.5 | 68.40% | 58.01% |
| Central, mixed recovery | 0.50 | 90.1–85.3 | 57.36% | 48.44% |
| Both offenses efficient, Bass high | 0.25 | 95.0–89.0 | 40.38% | 51.39% |
| **Mixture, N=1,200,000** | 1.00 | simulated full-game ~91.30–85.28 | **55.88%** | **51.57%** |

Shadow output mean total ~176.58, SD20.69; margin +6.02, SD15.46; ~2.4% regulation ties trigger synthetic OT. **The input scenarios are not confidence bands or an independently calibrated forecast.** Simple 2026 raw-data total midpoint ~175.4; with Ellenson return, PT impact of KT absences and opponent-adjusted pace unknown, the central budget is unstable. League-only baseline attempt: historical KBL table mean159.39 belongs older regime and cannot be used as same-event current exact-line BASELINE_P; fresh league total ~171.4 with unverified cohort has no frozen, independently reproducible same-line comparator. BASELINE_UNAVAILABLE.

**Score budget:** with KT scoring 78/85/92, Under179.5 needs DB ≤101/94/87 respectively; Over needs DB ≥102/95/88. Opposite: if DB scores 84/91/98, Under needs KT ≤95/88/81; Over requires KT ≥96/89/82. A healthy Ellenson/high shooting line or high Bass support can defeat the Under even with a DB win. At −5.5, DB 91 needs KT ≤85 to cover; KT scoring 86+ defeats that line. High late-foul shooting/OT can alter both, without automatic Under or handicap benefit.

#### A5. Full priced universe (exact supplied rows only)

Four full-game owner-supplied contracts retained in the decision table, two complete 0.5-line complement pairs, no unrequested alternate lines ranked. Every half-point contract is decisive in a completed game; no exact push; void/abandonment outside current data. `p_card NOT_ESTIMATED`, shadow rows are CONDITIONAL_DIAGNOSTICS with explicit complement checks (Under+Over=1, DB−5.5+KT+5.5=1). Ranking scope `SUPPLIED_ONLY`; winner directional shadow shown. A rank is only a research ordering, not a numerically gated/published primary pick.

#### A6. Adjustments, availability regimes and dependence

Admitted historical facts: DB home (3–2), KT away (3–4), five days since 8-Nov last DB game, four days since 9-Nov last KT game (local dates; no back-to-back on 13-Nov); KT shot fewer threes at lower accuracy 31.3% vs DB 34.6% from pregame StatGG; DB Ellenson expected, KT three outs + one questionable. No official sourced effect-table magnitudes for KBL 2026 cohort; **no claim of formally measured +X possession/margin shift**. Avoid double-counting injuries already captured in the 13-match season sample. Strongest changes: Ellenson minutes availability (DB offense), KT guard creation (tempo, Bass help) and live three-point conversion (widens both directions). These are evaluated in the named scenario tree rather than asserted as proven shifts. Fast and slow alternatives reverse the total direction, invalidating high confidence. Margin-total outcomes from the *same* synthetic joint scores; no independence assumption for combined legs. Joint formal primary failure NOT_COMPUTED.

#### A7. Family checks / shadow / uncertainty and calibration

Reference `NOT_RUN_UNAVAILABLE_LOCAL_GIT_CODE`; no release, no certified skill, no published primary. Shadow `EXECUTED` n=1,200,000 with deterministic seed 13112026 and actual program/JSON. All four complementary probabilities sum to one within rounding. Widths above historical KBL residual floors, but older season evidence unadmitted for 2026 KBL. OT is explicitly drawn when regulation tied; do not label approx simulation a KBL-realistic possession engine. True KBL late-foul timing, lineups, substitution constraints, score/period correlation and eligibility are not fully modelled. Median of mixture not necessarily a safe pick. No sportsbook, prices, analyst-tip sentiment or externally supplied projected scores enter calculation.

#### A8. Source/failure register and settlement capture

1. KBL official `https://www.kbl.or.kr/match/schedule` + DB club `https://promy.kbl.or.kr/match/schedule`: exact 13-Nov schedule and venue, no reliable confirmed starting five or signed 13-Nov pregame play-by-play retrieved.
2. StatGG `https://statgg.com/en/kbl/matches/S49G01N66`: pregame 13-game team totals, ranks, home/away, 23-Oct H2H, shooting and estimated pace; page mutable and source publication timestamp absent.
3. AiScore `https://www.aiscore.com/en/head-to-head/basketball/busan-ktf-sonicboom-vs-wonju-dongbu-promy`: both team L5 dated game rows and quarter scoreboard; source is a live page, query time in local research receipt.
4. Sports Chosun dated Nov9 `https://www.chosun.com/english/sports-en/2026/11/09/ZPWYKNMKAZH7BPW7KMZPUJGLKI/`: club quote on Ellenson return; corroborated Jumpball 13-Nov 10:45 KST `https://www.jumpball.co.kr/news/newsview.php?ncode=1065577530368244`.
5. Daily IL 13-Nov `https://www.dailyil.com/ko/briefing/2026-11-13_KBL/`: named KT absences and Jeong Chang-young doubtful; status is secondary source and club record unverified.
6. Current source state as seen during web research: preview/schedule; no 13-Nov match outcome used. Several `web.open` routes returned cached fetch errors; equivalent `web.search` indexed full source snippets provided evidence; exact page capture/publish time not always known. Unresolved: actual tipoff; both confirmed starting fives; full selected benches; Ellenson actual minutes/scratch status; official KT active squad; dated pregame L10/L15/L20; KBL 2026–27 exact same-line league baseline; possession/shot-quality features; operator cancellation terms.

For an explicit later settlement request, obtain field-owner official KBL final quarter scoring, OT segments and final score; confirm second scoreboard and native event ID. Grade spread from `DB − KT` and total from sum **including overtime**; source and final time required; no scheduled follow-up or autonomous monitoring created. Suggested review due `2026-11-15T21:00:00+11:00` is a triage target, not an automation or actual action.

#### A9. Integrity, completion matrix, issue and readback

| Required procedure | Actual work and finding | Remaining gap | Status |
|---|---|---|---|
| Authority / identity / duplicate / timing | Pinned repo SHA; official 13-Nov 19 KST fixture; G0001–G0004 unrelated | Actual first play, native KBL event ID | DONE_WITH_GAPS |
| Starters / bench / absences / recheck | Team-level previews, Ellenson return, KT 3 out + 1 questionable, DB named unavailable | Official dressed squad, fives, bench, Ellenson restriction | INFORMATION_INCOMPLETE |
| Online history / independent comparison / known-at | KBL official schedule, StatGG, AiScore, news, dated L5 games | Publication timestamps on mutable statistics, full dates L10+ | INFORMATION_INCOMPLETE |
| L5 / L10 / L15 / L20 / season / league | Recomputed both L5 from 10 dated scores; season n=13 each; KBL league context | Complete L10 dates, current-season n<15 and prior-season changes, exact league sample | INFORMATION_INCOMPLETE |
| KBL mechanisms, rules, venue, fatigue | FIBA40+OT, home court, 4/5-day rest, roster regime and budget, pace/special shooting | Exact shot creation, official minutes / active players | DONE_WITH_GAPS |
| Reference / frozen primary | Historical KBL row inspected; separate source-based approximation | No official `ml reference`/freeze/lint or calibrated baseline | NOT_RUN |
| Scenario arithmetic and dependence | 1.2m executed coherent score-grid paths, OT approximation, exact four row counters | Model release, fit, calibration, detailed overtime quality | SHADOW_ONLY |
| Every supplied contract | Two spread and two total directions computed; complement tests, definitions | Operator-specific void terms | DONE_CONDITIONAL |
| Expected score, W/P/L/V, baseline and sensitivity | Separate numerical shadows, score budget and branch thresholds | No valid primary p_card or same-line league comparator | SHADOW_ONLY |
| Complete A1–A9, append and custody | Draft card/source list/readback planned; preserving originals and updating local footer | No GitHub repository linter, freeze, ledger issue, commit or push by owner instruction | CHAT_LOCAL_DRAFT |

**Overall:** `INFORMATION_INCOMPLETE`; `RESEARCH_ONLY_NOT_CERTIFIED`; `NO_STRONG_PICK`; `EXPLORATORY_SHADOW_EXECUTED / PRIMARY_NOT_RUN`; `CHAT_LOCAL_READ_ONLY_DRAFT_NOT_REPO_ISSUED`; actual pre-start status must be decided from the recorded append time against **verified** first-possession time, not the user-supplied estimate. No canonical allocation or settlement.

**SPORTS_ONLY_MARKET_BLIND:** YES · **OUTCOME_EXPOSURE:** NO_TARGET_RESULT_SEEN_DURING_RESEARCH · **SETTLEMENT:** NOT_PERFORMED · **CANONICAL_IMPORT:** NOT_PERFORMED
<!-- END CARD LOCAL-20261112CC53B5C806-G0005 -->


<!-- BEGIN CARD LOCAL-20261112CC53B5C806-G0006 -->
## Card · LOCAL-20261112CC53B5C806-G0006 · Basketball / Japan B.LEAGUE PREMIER · Kawasaki Brave Thunders vs Saga Ballooners · 2026-11-13

- **Local event key:** `LOCAL-20261112CC53B5C806-G0006` — `LOCAL_UNIMPORTED_EVENT`, `CHAT_LOCAL_READ_ONLY_DRAFT`; no canonical P-ID reserved or assigned.
- **Native ID / aliases:** Official B.League ScheduleKey `506581`; Kawasaki Brave Thunders / 川崎ブレイブサンダース vs Saga Ballooners / 佐賀バルーナーズ. No prior G0001–G0005 identity collision detected in the accessible chat-local mini.
- **Authority / versions:** GitHub read-only pinned `008cedc4ff469e7a808292aa3667a7bffe22e273`, MDS v24.16, CR-2026.11.11-R4 forecast controls, CR-2026.11.12-R1 records revision, prompt v24.14, SCV-v13, SEL-v4. User override: no GitHub changes.
- **Method:** `UNCALIBRATED_QUALITATIVE` primary, with separate **executed 1,200,000-match shadow diagnostic** based on published regular-season data, scenario conditions and unvalidated normal/OT approximations. No released reference, no frozen primary distribution, no certified `p_card`, no audited league baseline; analysis-only.
- **Learning record:** `LEARN_RECORD_INCOMPLETE`, current league official L5 date/opponent/scores included below; pregame availability exact starters/minutes and L10–20 source rows unverified.
- **Timing:** Official scheduled `2026-11-13 19:05 JST (+09:00)` = `2026-11-13 10:05 UTC` = `2026-11-13 21:05 AEDT (+11:00)`; report/source collection and local append occur **after scheduled tip**; actual first possession `NOT_VERIFIED`; `POST_SCHEDULED_START / ACTUAL_START_UNVERIFIED / NOT_CERTIFIED_PREGAME`. User requested prior to scheduled tip, but this numerical analysis is not claimed to have been frozen before play. **No target-game live score or final consulted.**
- **Home/venue:** Kawasaki home, Tokyu Dresse Todoroki Arena, Kawasaki, Japan. Indoor arena: outdoor weather not applicable; current temperature does not affect basketball venue.
- **Endpoint:** Final score including *all overtime* under repository basketball control `BK-OT-1`, half-point spread/total with no possible push on a normally completed basketball game. Operator-specific abandonment/void terms not provided; sports research convention distinct from operator settlement.
- **Distribution:** Shadow `BPREMIER-KAW-SAG-20261113-NORMAL-OT-SENS-v1`, file `BPREMIER_SHADOW_DIAGNOSTIC_20261112CC53B5C806-G0006.json`; 3 scenario joint score grids (25% low, 50% base, 25% high), regulation independent normal total/margin, integer score formation, explicit tied-regulation overtime, `n=1,200,000`, RNG seed `20261113506`. The chosen parameters are subjective sensitivity assumptions, **not estimated fitting results**; no demonstrated prospective calibration.
- **Expected score (SHADOW_DIAGNOSTIC_ONLY):** Kawasaki 85.4211, Saga 80.5249, total 165.9460, Kawasaki margin +4.8962. Source cross-team raw means before shrink: Kawasaki 86.857, Saga 81.451, total 168.308, margin +5.406. Joint-margin/total volatility, 3-point distribution and possessions not fitted. NO PRIMARY EXPECTED SCORE ISSUED.
- **Baseline:** `BASELINE_P: BASELINE_UNAVAILABLE`, because the available historical `Basketball/B League` (2022–25, 2,937 development rows; mean total 159.19, raw total σ17.66, raw margin σ14.94; residual total 16.28) is an **unadmitted development sample for the pre-2026 B.League restructuring**, not a verified current 2026–27 B.PREMIER same-contract baseline. FIBA40 family prior 166.65 is a diagnostic sensitivity anchor only.
- **Availability:** Official Kawasaki report dated 13 Nov: Hirohide Araya (荒谷裕秀) suffered left ACL tear on 11 Nov vs Shimane, expected surgery; season 5.8 PPG (secondary outlet). Official Saga report dated 11 Nov: Sori Uchio (内尾聡理) dislocated left elbow on 8 Nov, recovery approximately 4 months. Not confirmed active tonight. Exact starting five/bench for both sides `LINEUP_UNCONFIRMED`, player-minute restrictions unknown. Do not infer full health for any remaining player.
- **Regime / context:** Kawasaki 4–12, Saga 1–13 entering event; recent L5 both 0–5, Kawasaki rest since 11 Nov (2 days) vs Saga since 8 Nov (5 days); home court Kawasaki, travel Saga. Strength comparison should recognize **both teams weak** rather than classifying Kawasaki as a strong favorite. Kawasaki's late home schedule 9/11/13 November; Araya/Uchio injury scenarios can affect usage, pace and width, with no fitted point shifts applied.
- **Settlement action:** `NOT_PERFORMED`, source to verify B.League official ScheduleKey=506581 final quarter scores incl OT, actual tip, lineups and status; corroborate official club recap/independent score provider; inspect operator abandonment rules if future settlement requested. No automatic scheduled job.
- **Known-at / integrity:** Official B.League fixture and club result pages pre-event historical data (latest previous matches 11 Nov / 8 Nov). Kawasaki injury official post dated 13 Nov, exact publication hour UNKNOWN; Saga report 11 Nov, pre-target. Retrieval approximately 21:04–21:08 AEDT on 13 Nov; **do not assert all sources were available before first possession**. No target game's live state exposed in computation.

### Decision block

**Research judgement:** `Saga +9.5` is the strongest *conditional* lean (low confidence), followed by `Under 169.5` (low confidence). Kawasaki may win outright yet fail to cover 10 points. The two teams' opposing recent total environments, roster absences and uncertain exact starters materially reduce confidence. Neither is a formally issued Rank-1 probability; no high-confidence selection.

| Priority (qualitative) | Role | Source tag | Exact supplied proposition | PRIMARY p_card | Conditional shadow share | Shadow scenario range | Main failure route |
|---|---|---|---|---|---:|---:|---|
| 1 | LEAN | SUPPLIED | Saga Ballooners **+9.5 points** (full game incl OT) | NOT_ESTIMATED | **61.8484%** | 55.54–67.87% | Saga's weak 1–13 profile and perimeter/paint defense allow a double-digit Kawasaki win |
| 2 | LEAN | SUPPLIED | **Under 169.5 total points** (full game incl OT) | NOT_ESTIMATED | **57.5317%** | 39.70–68.68% | Saga's opponents average ~95 PPG; high-scoring scenario and fouling/OT push over |
| 3 | INFORMATIONAL | SUPPLIED | **Over 169.5 total points** (full game incl OT) | NOT_ESTIMATED | 42.4683% | 31.32–60.30% | Kawasaki's poor recent attack and slow home outcomes |
| 4 | INFORMATIONAL | SUPPLIED | Kawasaki Brave Thunders **−9.5 points** (full game incl OT) | NOT_ESTIMATED | 38.1516% | 32.13–44.46% | Five straight Kawasaki defeats and lost wing rotation; need >=10-point victory |

**Supplied rows:** ALL FOUR priced in one separate scenario model and assessed qualitatively; no primary p_card issued. Shadow winner: Kawasaki 62.5343%, Saga 37.4657%, no draw after OT. **Rank-1 gate:** NOT_ASSESSABLE (no released primary, no suitable same-line population baseline or certified precision). **Rank-2 floor:** NOT_ASSESSABLE. **Baseline coverage:** 0/4 (formal). **Joint failure of Saga +9.5 and Under 169.5** in diagnostic: 16.3603% of simulations (Kawasaki wins by ≥10 AND ≥170 combined); joint both-wins 35.7403%. This is a conditional simulation dependency, not validated forecast reliability. **Abstention:** NO_STRONG_PICK. **Shadow gate:** no qualified release; `NOT_RUN_NO_RELEASE`. **No model improvement certification.**

### Appendix

#### A1. Identity, timing, venue, duplicate and match state

- `ScheduleKey=506581`, official Japanese B.PREMIER round; distinct from previous chat requests; Kawasaki listed HOME; Saga AWAY. Official schedule 19:05 JST (21:05 AEDT), 13 Nov 2026. Available source still showed pregame at retrieval, but this does NOT prove the game had not tipped.
- `RESEARCH_POST_SCHEDULED_START`; actual first ball `NOT_VERIFIED`; no live target outcome used. Issue/freeze/settlement `NOT_ISSUED`, `NOT_FROZEN`, `NOT_SETTLED`. Keep this outside prospective prestart scoring.
- Distinct team aliases: `川崎 / Kawasaki Brave Thunders`, `佐賀 / Saga Ballooners`. B.PREMIER 2026–27, not automatically comparable with 2025–26 B1 development series.

#### A2. Exact frozen requests, eligibility, score budget

| Key | Owner supplied line | Full-game final incl OT proposition | Action convention | Directional evidence |
|---|---|---|---|---|
| KAW−9.5 | Thunders −9.5 | Kawasaki wins by 10 or more | half line, no push | Poor opponent 1–13 and high Saga points allowed, but Kawasaki 0–5 in recent five |
| SAG+9.5 | Ballooners +9.5 | Saga loses by 9 or fewer, or wins | half line, no push | Kawasaki low recent offense, higher spread cushion, though Saga fragile defensively |
| O169.5 | Total Over 169.5 | Both teams combine for ≥170 | half line, no push | Saga last-five totals 181.8; offensive-strength and late-foul ceiling |
| U169.5 | Total Under 169.5 | Both combine for ≤169 | half line, no push | Kawasaki last-five totals 153.8; weak Kawasaki scoring and shot efficiency |

- **Budget:** At a target 170 points, if Saga scores 75, Kawasaki needs 95; if Saga 80, Kawasaki needs 90; if Saga 85, Kawasaki needs 85. Alternatively, if Kawasaki scores 80, Saga needs 90; if Kawasaki 85, Saga needs 85; if Kawasaki 90, Saga needs 80.
- Spread threshold: If Saga reaches 80, Kawasaki must reach at least 90 to cover −9.5; if Saga 85, Kawasaki ≥95; if Saga 75, Kawasaki ≥85. Losing outcome of +9.5 is ≥10-point Kawasaki margin regardless of total.
- `rank_scope=SUPPLIED_ONLY` by user's supplied contracts. Both sides of each supplied symmetric line are complementary probabilities in the diagnostic, never independent evidence.

#### A3. Evidence, form windows, sources, lineup and medical

**Official pre-target standings and season production:** B.League page `https://www.bleague.jp/game_detail/?ScheduleKey=506581` before this event shows Kawasaki 4–12, Saga 1–13, PF 78.5 vs 78.2 PPG; Kawasaki 43.5% FG, 29.9% 3P, 41.3 RPG; Saga 41.1% FG, 31.3% 3P, 32.4 RPG. Official club result pages, compiled over the already played games, give Kawasaki 1,256–1,355 over 16, Saga 1,095–1,333 over 14. **Calculations:** Kawasaki PF78.500 PA84.688; Saga PF78.214 PA95.214.

**Verified latest five, all pre-target and complete:**

| Date | Kawasaki opponent / venue | Kawasaki score | Total | Source |
|---|---|---|---:|---|
| 2026-11-11 | Shimane, home | 74–95 L | 169 | Official Kawasaki club results `https://www.bleague.jp/en/club_detail/?TeamID=727&tab=2` |
| 2026-11-09 | Altiri Chiba, home | 76–85 L | 161 | Same |
| 2026-11-06 | Shiga, away | 75–81 L | 156 | Same |
| 2026-11-01 | Yokohama BC, home | 66–77 L | 143 | Same |
| 2026-10-31 | Yokohama BC, home | 65–75 L | 140 | Same |

**Kawasaki L5 actual 5:** 0–5; PF 356/5=71.2, PA 413/5=82.6, sum 153.8. Earlier game 2026-10-26 vs Utsunomiya 92–89 W recovered, but full L10/15/20 dated event rows not completely opened; do not invent windows.

| Date | Saga opponent / venue | Saga score | Total | Source |
|---|---|---|---:|---|
| 2026-11-08 | Chiba Jets, home | 103–111 L | 214 | Official Saga club results `https://www.bleague.jp/club_detail/?TeamID=1638` |
| 2026-11-01 | Mikawa, away | 78–84 L | 162 | Same |
| 2026-10-31 | Mikawa, away | 83–100 L | 183 | Same |
| 2026-10-26 | Alvark Tokyo, home | 88–112 L | 200 | Same |
| 2026-10-21 | Nagasaki, home | 66–84 L | 150 | Same |

**Saga L5 actual 5:** 0–5; PF 418/5=83.6, PA 491/5=98.2, sum 181.8. Earlier 2026-10-18 at Kyoto 70–115 L recovered, but full L10/15/20 dataset not verified.

**Window inventory, no fabricated rows:**
| Window | Kawasaki W–L | PF/G | PA/G | n | Saga W–L | PF/G | PA/G | n |
|---|---|---:|---:|---:|---|---:|---:|---:|
| L5 | 0–5 | 71.20 | 82.60 | 5 | 0–5 | 83.60 | 98.20 | 5 |
| L10 | NOT_VERIFIED | — | — | 0 verified complete L10 | NOT_VERIFIED | — | — | 0 verified complete L10 |
| L15 | NOT_VERIFIED | — | — | 0 verified complete L15 | NOT_AVAILABLE: only 14 season matches | — | — | 0 |
| L20 | NOT_VERIFIED | — | — | only 16 season matches | NOT_AVAILABLE: only 14 season matches | — | — | 0 |
| Season to date | 4–12 | 78.50 | 84.69 | 16 | 1–13 | 78.21 | 95.21 | 14 |

**Medical primary sources:**
- Kawasaki `https://kawasaki-bravethunders.com/news/detail/id=25908` (13 November): Hirohide Araya, torn left ACL during 11 November first quarter, surgery planned, return UNKNOWN. Basketball King corroborates his prior 16 games and 5.8 PPG (`https://basketballking.jp/news/japan/20261113/643190.html`).
- Saga `https://ballooners.jp/news/detail/id=52402` (11 November; also path `id=48255` returns matching article): Sori Uchio, left elbow dislocation on 8 November, estimated four months recovery and planned surgery.
- Saga official player page `https://www.bleague.jp/club_detail/?TeamID=1638` identifies Nassir Little as 25.1 PPG club leader, David Dudzinski 7.0 RPG, and Taiki Sumida 5.6 APG. Such roster/leadership values are **not** confirmed game starters; do not use them as minute or active-status confirmations.
- Kawasaki pregame club preview `https://kawasaki-bravethunders.com/lp/game_20261109_20261111_20261113/` previews Saga's Nassir Little and Damyean Dotson as major perimeter/wing threats; coach Kawasaki Dai Oketani noted in team material. These are preview descriptions, not tonight's actual box score.
- **Both sides starter five, bench, scratches and minute restrictions:** NOT_VERIFIED for exact fixture; current team roster ≠ actual starting/available list. No medical status asserted for other players. Last-source recheck after scheduled start cannot establish pre-first-play lineups. Injury announcement publication hour may be unknown.

**Source provenance:** Official organizer/club pages and medical releases, + second independent report on Kawasaki Araya injury; retrieved 2026-11-13 about 21:04–21:08 AEDT (source timestamp for some articles date-only; exact hour unknown). Event's actual tip and state not confirmed. Prior games not duplicated in calculations. **No web odds used.**

#### A4. Baseline, formulas, shadow arithmetic, sensitivity

- Official season raw scored/allowed cross: `K=(78.50+95.214)/2=86.857`, `S=(78.214+84.688)/2=81.451`, total `168.308`, margin `+5.406`; this is a crude opponent-mixing projection, not opponent-adjusted possession/ORtg/DRtg.
- The 2026–27 B.PREMIER tier has no verified active calibrated reference release. Historical B League `USABLE_DEVELOPMENT` input is a population **diagnostic**, with unadmitted development cohort and changed competition identity; it is **not** promoted to a primary probability or same-line `BASELINE_P`.
- **Exact executed shadow:** `python /mnt/data/bpremier_shadow_kawasaki_saga_20261113.py`; completed 1,200,000 trials with RNG seed 20261113506. Scenarios fixed BEFORE simulation: low 300,000 at regulation μtotal160.0/μmargin+2.5, base 600,000 at 164.0/+4.9, high 300,000 at 174.0/+7.4; each σtotal18.5, σmargin15.2. Draw independent total and margin normal values, derive integer team points, resolve tied-regulation with 5-minute OT scoring (discrete assumed 4–12 points per side, additional periods if still tied), derive all rows from common score states. This **does not** represent actual possession/usage/fouls/lineup covariance; assumed overtime generation is illustrative.
- **Shadow expected:** K85.421, S80.525, total165.946, margin+4.896. OT simulated rate 2.481%. Numerics are normalized shares of actual executed trials but **not validated event probabilities**. W/P/L/V on each half line: W=share, P=0, L=1−share, V=0 under completed-game convention.
- **Low/base/high shadow:** Saga +9.5 = 67.868%, 61.991%, 55.543%; Under 169.5 = 68.677%, 60.873%, 39.703%. These wide outcome intervals are *epistemic sensitivity*, not Monte Carlo confidence intervals.
- **Independent constraints and dependence:** half-point complementary lines exactly sum to one; no draw after overtime; one coherent score grid per scenario. Winner K 62.534%, S 37.466%. Joint failure if top two both selected: 16.3603%; shared risks of superior Kawasaki scoring and Saga defense breakdown; not an independence calculation. Precision of 1m simulation is much smaller than structural uncertainty; numerical display precision is diagnostic only.
- **Reference/gates not executed:** official repository `ml reference`, `ml card lint`, pregame freeze, ledgers, RELEASE model and same-line league baseline were NOT_RUN because no writable local repository environment / release was used. No printed `p_card`, no Grade/eligible prospective model claims.

#### A5. Four supplied contracts — coherent W/P/L/V shadow only

| Contract | Shadow WIN | PUSH | LOSS | VOID | Basis / scope |
|---|---:|---:|---:|---:|---|
| Kawasaki −9.5 | 0.381516 | 0 | 0.618484 | 0 | full incl OT; margin ≥10 |
| Saga +9.5 | 0.618484 | 0 | 0.381516 | 0 | full incl OT; margin ≤9 |
| Over 169.5 | 0.424683 | 0 | 0.575317 | 0 | full incl OT; total ≥170 |
| Under 169.5 | 0.575317 | 0 | 0.424683 | 0 | full incl OT; total ≤169 |

Primary probabilities for **all four** are `NOT_ESTIMATED`; do not replace `p_card` with shadow WIN values. Qualitative direction remains Saga +9.5 then Under 169.5. Total source dispersion is high; stronger high-state gives a 60.3% shadow OVER, so Under cannot be called safe.

#### A6. Adjustment ledger, regime, rest, injuries, double-count

| Fact / mechanic | Verified source | Mechanism and potential direction | Applied primary effect |
|---|---|---|---|
| Kawasaki home court / Saga travel | Official B.League home/away, venue | helps Kawasaki margin, Saga travel impacts recovery | UNFITTED; covered by scenario margin only, no separate fixed points |
| Kawasaki Araya injury | Official 13 Nov ACL release | scorer/wing depth, perimeter assignment; replacement minutes unknown | SCENARIO/width, NOT calibrated |
| Saga Uchio injury | Official 11 Nov elbow release | limited reserve guard depth; half-court execution/defense unknown | SCENARIO/width, NOT calibrated |
| Kawasaki two-day rest; Saga five days | Official dated L5 | rest differs, but FIBA40 effect not measured | WIDTH ONLY; no automatic scalar |
| Kawasaki L5 low vs Saga L5 high | Official previous results | conflicting tempo; do not cherry-pick last result | scenario low/base/high, not separate 5+ repeated adjustments |
| Foreign players Little/Dotson | Official Kawasaki preview | Saga high-upside scoring branch despite 1–13 record | SCENARIO high, not a certain availability claim |

No researched hard numeric effects existed to move a certified reference ledger. Large-adjustment/Rank delta `NOT_ASSESSABLE`; no team/player impact double-counting introduced.

#### A7. Checks, odds firewall, model output and prior context

- `MARKET_BLIND` yes. No bookmaker/odds/consensus forecasts referenced or used.
- Current historical B.League prior does NOT prove new B.PREMIER scoring distribution (league structural change); league-only exact-contract baseline and official possession indicators missing.
- Baseline, primary reference and pregame freeze `NOT_RUN`. Shadow separate from primary, not a model release; no Brier/skill qualification. No opponent-adjusted ORtg/DRtg/pace, crew, active minutes or shot-quality model fitted.
- Five-game samples overlap season-to-date; they are not separate independent confirmations. No H2H adjustment applied because verified same-regime recent H2H could not be established. Team records and pre-target box rows used only as descriptive inputs.
- Distinct margin versus total risks: Saga cushion fails on Kawasaki double-digit victory; Under fails on high combined scoring. Both can fail simultaneously as observed in simulation.

#### A8. Evidence and settlement capture plan

| Field / source route | Found / attempted | Remaining required action |
|---|---|---|
| Event identity and venue — official `bleague.jp/game_detail/?ScheduleKey=506581` + club schedule | CONFIRMED scheduled 19:05 JST, home Kawasaki | actual opening jump/OT/revisions not verified |
| Season PPG and records — official organizer | CONFIRMED Kawasaki 4–12 / Saga 1–13 and scored rates | final 2026–27 pace/shot denominator archive, league aggregate prior |
| L5 results — official B.League club pages | 5 dated complete final scores per side extracted | more L10/L15/L20 dated rows (use organizer full results, alternate provider) |
| Injuries — both official clubs, secondary Kawasaki journalist | 2 major injury releases verified | actual starters/bench, replacements, minutes, further medical updates |
| Current previous H2H — official matches | Not verified for current-roster regime | research prior meetings if needed for future retrospective, no unsupported numeric effect |
| Current match result — B.League official box/quarter page and club recap | NOT CONSULTED; no outcome exposure | after event, explicit user request for settlement; capture final/OT by target ID |
| Operator settlement | Not supplied | clarify if future settlement conflicts with BK-OT-1 sports convention |

**Open event queue (Q-0006):** actor = same chat on explicit follow-up; field = official final/quarters/actual first tip/rotations; source `https://www.bleague.jp/game_detail/?ScheduleKey=506581`, corroborate `kawasaki-bravethunders.com` and `ballooners.jp`; due `2026-11-15T21:05:00+11:00` *triage target only*, final-time basis `UNKNOWN`, last source attempt `2026-11-13 ~21:08 AEDT`, scheduled automation `NO`. Nothing has been graded.

#### A9. Integrity receipt and research-completion matrix

| Requirement | Actual completed work | Gap / impact | Status |
|---|---|---|---|
| Authority + fixture/native ID + duplicate + timing | GitHub pinned control, official 506581, home/venue, both aliases, new G0006 without collision | actual first possession not verified; issue post scheduled | DONE_WITH_GAP |
| Both starters, bench, absences and recheck | Official both-club injuries, roster previews, secondary report Kawasaki | exact starting five/bench late confirmations missing for both | INFORMATION_INCOMPLETE |
| Online history and comparison | B.League official both club previous-game results, 5 actual rows each, dated and deduped | recent H2H, full opponent/pace data and second independent score confirmation missing | INFORMATION_INCOMPLETE |
| L5/L10/L15/L20/season/league | actual L5 and season verified with n; prior B League parameter row | verified complete L10–20 and modern B.PREMIER league averages missing | INFORMATION_INCOMPLETE |
| Venue/rules/rest/special situations | FIBA40 with 5-minute overtime, 2-day vs 5-day, injury branches and double-digit handicap kill paths | exact clock/foul distributions missing | DONE_WITH_GAPS |
| Reference + formal baseline + pregame freeze | Historical parameter row and crude scoring cross calculation | repository `ml reference`, source-freeze and same-line baseline unavailable/unexecuted | NOT_RUN |
| Distribution and uncertainty arithmetic | reproducible 1.2m separate shadow script/JSON, three explicitly assumed cases, score/OT and joint controls | not calibrated, no exact injury impact or pace/shot variance fit | SHADOW_EXECUTED_ONLY |
| All supplied contract analysis | full-game ±9.5, Over/Under169.5, complementary simulation masses, mechanisms | primary certified p_card unavailable | DONE_SHADOW/QUALITATIVE |
| Score budget, winner/joint, sensitivity | budget with 3 Saga scores, winner, joint failure, scenario ranges | no official primary reference; no valid gate | DONE_SHADOW_ONLY |
| A1–A9, intake, queue, local append and custody | All nine sections, source URLs and local text/readback receipt; previous 5 cards preserved | no repository verification/lint/commit/push by user override | CHAT_LOCAL_ONLY |

**Overall research status:** `INFORMATION_INCOMPLETE`, with actual source gaps above. **Forecast:** `UNCALIBRATED_QUALITATIVE / SHADOW_1_200_000_EXECUTED / PRIMARY_NOT_RUN`. **Issue status:** `POST_SCHEDULED_START_NOT_CERTIFIED_PREGAME / CHAT_LOCAL_DRAFT_NOT_REPOSITORY_ISSUED`. **Risk:** `NO_STRONG_PICK`.

**SPORTS_ONLY_MARKET_BLIND:** YES · **OUTCOME_EXPOSURE:** NO_TARGET_SCORE_SEEN · **SETTLEMENT:** NOT_PERFORMED · **CANONICAL_IMPORT:** NOT_PERFORMED
<!-- END CARD LOCAL-20261112CC53B5C806-G0006 -->


<!-- BEGIN CARD LOCAL-20261112CC53B5C806-G0007 -->
## Card · LOCAL-20261112CC53B5C806-G0007 · Ice hockey / Czech U20 Extraliga · Motor České Budějovice U20 vs Bílí Tygři Liberec U20 · 2026-11-13 CET

- **Local event key:** `LOCAL-20261112CC53B5C806-G0007` — `LOCAL_UNIMPORTED_EVENT`; first local record for this event in this chat.
- **Canonical ID / assignment stage:** `NOT_ASSIGNED / PROMPT_4_IMPORT`; no canonical ID reserved.
- **Event / native ID / aliases:** Czech Hockey Federation `match 3156`, game-detail internal URL `178203`, Komerční banka extraliga juniorů 2026/27 round 20; BANES Motor České Budějovice (Motor U20, České Budějovice U20) vs Bílí Tygři Liberec (Liberec U20). No relation to senior teams or U18 fixtures of similar names.
- **Authority:** GitHub `danisgreat/Sports-Research` `main` pinned `008cedc4ff469e7a808292aa3667a7bffe22e273` read-only. MDS v24.16; forecast control CR-2026.11.11-R4; records update CR-2026.11.12-R1; prompt v24.14; scoring SCV-v13; selection SEL-v4; user `CHAT_LOCAL_ONLY / NO_GITHUB_WRITE` override. No local clone, repo reference freeze, issued card or ledger execution.
- **Probability method:** `UNCALIBRATED_QUALITATIVE` as primary; independently **executed** `EXPLORATORY_SHADOW_NOT_PRIMARY` 1,200,000-run joint goal Monte Carlo with 3 source-anchored but *assumed* scoring/goalie/empty-net scenarios. Not an official primary `ANALYST_PRIMARY_V1` run; no released model or independently validated calibration. Source/JSON: `hockey_shadow_motor_liberec_20261113.py`, `HOCKEY_SHADOW_DIAGNOSTIC_20261112CC53B5C806-G0007.json`.
- **Learning record:** `LEARN_RECORD_INCOMPLETE`; official Liberec 17 results and Motor L5 retained with dates/score sources; Motor L10/L15/L20 dated rows, complete current goalkeeper and skater availability snapshots, shot/PP covariates and point-in-time league event-level baseline not assembled. No LEARNLOG or frozen repository feature pack executed.
- **Future learning:** `PENDING_SETTLEMENT / NOT_ADMITTED`: requires verified actual start/final/periods, goaltenders, source timestamps and unknown operator terms; this card's timing is not certified pregame.
- **Analysis status:** `UNCALIBRATED_QUALITATIVE` with shadow directional diagnostics; `INFORMATION_INCOMPLETE`; `NO_STRONG_PICK`; not performance-eligible.
- **Timing and exposure:** User estimated `2026-11-13T00:30+11:00`, equal to 12-Nov 13:30 UTC or 14:30 CET. **Official federation and current club match list** publish **13-Nov-2026 12:00 CET** = 13-Nov **22:00 AEDT** (11:00 UTC); a minority of club cached listings show **15:30 CET** (14-Nov **01:30 AEDT**). These conflict and the actual first puck-drop was never independently checked. Initial fixture/standings/goalie-empty match centre observed before 22:00 AEDT; further research and chat-local append are after the 22:00 scheduled clock. `POST_SCHEDULED_START / ACTUAL_START_UNVERIFIED / NOT_CLEAN_PREGAME_ISSUE`. No target-game live/final score consulted, and `0:0` on a pregame match page is not graded as a result.
- **Venue and conditions:** Budvar aréna, České Budějovice, Czechia. Indoor ice; outdoor weather `NOT_APPLICABLE`; ice quality, officials' penalty environment and rink differences not quantified.
- **Exact endpoint / actions:** User supplied full-game Motor `−1.5`, Liberec `+1.5` goals, combined `O/U 5.5`. Model assumes regulation + winner-takes-one-goal OT/SO if tied, one conditional empty-net scoring branch; half-point lines have no pushes when action stands. Under these simplified rules the exact supplied contracts are OT-goal-invariant if a regulation tie can add at most one goal, although named sportsbook/operator action rules, suspension, forfeits and shootout convention are `UNKNOWN_DEFINITION` and not presumed. Win/lose/void need operator confirmation in settlement.
- **Shadow distribution object:** `IND_POISSON_60MIN_PLUS_STYLIZED_OT_EN_SCENARIOS` with 0.25 low, 0.50 base, 0.25 high weights; three independent Monte Carlo batches of 300k / 600k / 300k. Home edge implicit in home team pairing, **not** separately fitted. Correlated scoring/true pulled-goalie likelihood and lineup states are not fit. Empty-net branch may double-count raw season scoring; simulation is sensitivity only.
- **Shadow expected score and uncertainty:** scenario-weighted Motor **3.779**, Liberec **2.652**, combined **6.431**, Motor signed lead **+1.127** goals; within-scenario weighted SD total **2.468** and margin **2.546** (NOT the full-mixture SD). These numbers are uncalibrated diagnostics, **not** certified primary expected scores.
- **Baseline:** Exact-line `BASELINE_LEAGUE_V1` **NOT_COMPUTED**: official league-wide pre-event standings allow empirical mean but no verified past same-line event-level distribution or Czech-junior goaltender/OT calibrated baseline. League prior 910 team goals / 296 team appearances = **3.0743 per team-game**, 6.1486 combined; this descriptive mean does not substitute for `BASELINE_P`.
- **Regime/context:** host 5th / 38 pts from 19 games vs visitor 15th / 12 pts from 17; youth-junior volatile goalie/depth exposure; last match on 19-Sep ended Liberec 3–4 Motor after extra-time process (exact SO/OT subtype needs re-verification). Motor more reliable recent defense; Liberec 3 wins in last 4 including extra-time, so weak season record not equivalent to guaranteed blowout.
- **Settlement capture plan:** after the event on explicit user follow-up, capture official Czech Hockey Federation `match 3156` final (score, period splits, OT/SO, goaltenders, exact start and status) and corroborate hokej.cz and both clubs; determine total and full-game margin; preserve operator rules/void condition separately. No scheduled automation; no settlement performed here. Triage due **2026-11-15T22:00+11:00** is a manual target only, final-time basis `UNKNOWN`.
- **Rules/source reading receipt:** `CORE.md`, `CURRENT_STATE.md`, `RULES_REFERENCE.md` §7–9, `RULES_ICE_HOCKEY.md` §§0–3,6–8, `PROBABILITY_TOOLKIT.md` §2, `CARD_AND_LOG_TEMPLATES.md` §§2–3, `RESEARCH_PROTOCOL.md` Parts A/B/E, `research/prompts/1_GAME_CARD.md` and ice-hockey sport-specific requirements by pinned main; 2026 Czech federation fixture/standings, official Liberec U20 results, Motor regional club match reports. Only read/search/fetch GitHub operations; repository's `ml reference`/`card lint`/pregame freeze were **not executed**.
- **Known-at and lineup state:** Federation fixture/standings and dated pre-event results captured prior to official 22:00 AEDT schedule and other same-game result exposure. Page publication timestamps for mutable roster/standings unknown. Exact-game official `SESTAVY` skater and goaltender tables contained `NO DATA AVAILABLE` in the pre-match inspection; **both starting goaltenders, defense pairs, offensive lines, scratches, call-ups and injuries unconfirmed**. A season roster at Motor lists goaltenders Štěpán Bogač and Vojtěch Jelínek, **not verified starters**. Do not label unreported injuries as none.
- **Pricing basis:** `SHADOW_ONLY` three illustrative cases with unfit 0.25/0.50/0.25 weights, not an independently frozen primary reference/adjustment ledger. Official `p_card` NOT_ESTIMATED. No uncalibrated shadow promoted to a calibrated probability.
- **Form windows:** Motor L5 from dated 17–31 Oct rows: GF16/5 3.20, GA10/5 2.00, total 5.20; L10/L15/L20 dated rows **NOT_COMPLETED**; regular-season full n19 69 GF/45 GA from official table. Liberec complete L5 GF14 GA16 total6.00, L10 GF28 GA40 total6.80, L15 GF38 GA64 total6.80, L20 available n17 GF41 GA71 total6.59 (cannot imply 20 games); season n17 same 41/71. League total 6.1486 goals/game from all 16 standings entries. Full source rows and gaps in A3.

### Decision block

**Assessment:** **Over 5.5 goals** is the strongest *exploratory* direction due to a 6.15-goal league environment and Liberec's season-high conceded rate; however its sensitivity range spans both sides of 50%. Motor is clearly the stronger outright side; its `−1.5` remains vulnerable to close games, and **no high-confidence pick can be issued** without confirmed goalies, exact endpoint custody and pregame timing.

| Rank | Role | Tag | Exact contract / proposition | p_card | p_base | BASELINE_P | Line distance | Basis / failure |
|---|---|---|---|---|---|---|---|---|
| 1 | PICK (directional only) | SUPPLIED | `TOTAL_OVER_5_5`: combined match goals ≥6 | NOT_ESTIMATED | NOT_COMPUTED | BASELINE_UNAVAILABLE | shadow centre 6.431 − 5.5 = +0.931 goals; no validated z | Qualitative; separate shadow ~0.6044. Goaltending, low-shot and low-conversion 5-goal branch kills |
| 2 | PICK (directional only) | SUPPLIED | `LIBEREC_PLUS_1_5`: Motor winning margin <2 | NOT_ESTIMATED | NOT_COMPUTED | BASELINE_UNAVAILABLE | shadow margin 1.127 vs +1.5, no validated z | Qualitative; separate shadow ~0.5255. Motor finishing and empty-net 2-goal outcome kills |
| — | INFORMATIONAL | SUPPLIED | `MOTOR_MINUS_1_5`: Motor winning margin ≥2 | NOT_ESTIMATED | NOT_COMPUTED | BASELINE_UNAVAILABLE | shadow margin 1.127 vs +1.5; no validated z | Shadow ~0.4745; vulnerable to 1-goal/OT finish |
| — | INFORMATIONAL | SUPPLIED | `TOTAL_UNDER_5_5`: combined match goals ≤5 | NOT_ESTIMATED | NOT_COMPUTED | BASELINE_UNAVAILABLE | shadow total centre 6.431 >5.5; no validated z | Shadow ~0.3956; killed by 6+ goal conversion/goalie weakness |

**Baseline coverage:** 0/0 numeric primary rows. **Rank-1 gate:** `NOT_ASSESSABLE`; no frozen exact-line baseline, certified p_card, goalie confirmation or prospective freeze. **Rank-2 floor:** `NOT_ASSESSABLE`. **Joint failure (shadow only):** P(Over5.5 loses AND Liberec+1.5 loses) = P(total ≤5 AND Motor margin ≥2) ≈ **0.1490**, unconditional across the assumed sample tree; no issued-card joint. **Family check:** `Motor−1.5` + `Liberec+1.5` =1.000 in shadow, `Over+Under5.5` =1.000; pushes excluded for half-lines in assumed action. **Adjustment dependence:** `SCENARIO_SENSITIVE`; Over crosses 50% between cases and handicap direction flips in high case. **Potential winner (shadow only):** Motor 0.6792; Liberec 0.3208 (OT winner branch included). **Abstain:** YES, `NO_STRONG_PICK`; all qualified primary probabilities unavailable. **Model shadow (MLSCOPE-v3):** `NOT_RUN_NO_RELEASE_OR_LOCAL_MODEL`; separate executable *illustrative* Monte Carlo is not the GitHub model shadow.

### Appendix

#### A1. Identity, timing and state

- Official game `3156` / page `https://czehockey.cz/game/detail/178203`; organizer's full pre-match fixture `https://www.czehockey.cz/competition/games/1?gameListWidget-page=13`. Club current schedule `https://www.hcbilitygri.cz/matches/JUN`. All identify same home and away U20 players and 13-Nov match.
- Official and most current published scheduling: **13-Nov 12:00 CET**, i.e. UTC11:00, AEDT22:00; user originally supplied **13-Nov AEDT00:30** (previous Czech local date, unrelated to actual match). Old filtered/cached club lists advertise **15:30 CET**. Retain both, source conflict; a post-scheduled issue is *not* a prestart issue unless first play actually verified later (not done).
- `STATUS_AT_ISSUE`: `TIMING_UNVERIFIED`, `POST_OFFICIAL_SCHEDULE_CLOCK`, no verified live/final target exposure, no access to actual first-play timestamp. Neither the federation pregame placeholder `0:0` nor any unrelated age-group/senior match is target evidence.
- Venue Budvar aréna, České Budějovice; youth regular season, three 20-minute regulation periods. Exact OT/SO & contract settlement only assumed for exploratory scoring, field-owner regulation and operator terms unavailable.

#### A2. Frozen owner-supplied contracts and candidate plan

| Exact row | Scored quantity | Win condition | Push/void | Support | Counterargument / primary status |
|---|---|---|---|---|---|
| Motor −1.5 | Full-game home-away goal margin | Motor wins by at least 2 | None on half-line if valid match, operator void UNKNOWN | Fifth place, 69–45 and Liberec defensive 71 conceded | One-goal H2H, OT games, scoring width; NOT_ESTIMATED primary |
| Liberec +1.5 | Full-game goal margin | Liberec wins or loses by ≤1 | None on half-line if valid, operator void UNKNOWN | 3/last4 wins for Liberec, Motor close losses in last2 | 15th-place defense, Motor attack & EN goals; NOT_ESTIMATED primary |
| Over 5.5 | Total official match goals | At least 6 | None on half-line if valid, operator void UNKNOWN | League 6.1486, Liberec GA 4.176, 19-Sep H2H total7 | Both teams' most recent L5 total means 5.2 / 6.0; goalie uncertainty; NOT_ESTIMATED primary |
| Under 5.5 | Total official match goals | At most 5 | None on half-line if valid, operator void UNKNOWN | Motor last five 5.2 total, 2.0 goals against | Liberec's porous defense + power play, empty-net tail; NOT_ESTIMATED primary |

Rank scope supplied lines only (no derived thresholds). One coherent three-scenario joint goal simulator provided all **shadow**, not primary, row values. No multiple user fixtures combined.

#### A3. Evidence and online historical rows

**Official league snapshot** `https://ceskyhokej.cz/competition/standings/1` (2026/27 before match): 16 teams, 296 team appearances / 148 games, GF sum 910, league average GF/team 3.0743 and full-game 6.1486; Motor 5th 19 GP GF69 GA45 38pts; Liberec 15th 17 GP GF41 GA71 12pts. Site shows season-to-date tabular figures; publication/correction time unknown.

**Motor U20 recent played matches**, official/regional reports and source corroboration; scores are Motor first. OT/SO match-score shorthand is explicitly not a regulation goals record:

| Date | Opponent / site | Final Motor–opponent | Source |
|---|---|---|---|
| 2026-10-17 | Litvínov away | 3–1 | competition result summaries; regional report index; full official original row not independently recovered |
| 2026-10-19 | Slavia Praha home | 3–1 | `https://hcmotor.cz/zapasy.asp?filtrTym=SLA&kde=vsechno&sezona=2027&stats=true` |
| 2026-10-23 | Plzeň home | 5–1 | `https://hcmotor.cz/zapasy.asp?filtrTym=PLZ&kde=doma&sezona=2027&stats=true` |
| 2026-10-30 | Mountfield HK away | 3–4 | `https://www.onlajny.com/match/index/date/2026-10-30/id/540494`; `https://www.jchokej.cz/archiv-kratkych-zprav?page=2` |
| 2026-10-31 | Pardubice away | 2–3 after shootout (reg 2–2) | `https://www.jchokej.cz/archiv-kratkych-zprav?page=2` and Motor club match archive |

Motor **L5** GF16 GA10, average scored 3.20 and conceded 2.00, total 5.20. **L10/L15/L20 dated opponent-specific records** NOT_COMPLETE because no verified intact 19-game source pack was retrieved (several search pages identified as 2025/26, explicitly rejected). Season n19 69/45 independently from organizer. Don't convert 19-game aggregates into 20 specific rows.

**Liberec U20 current-season results**, all from `https://www.hcbilitygri.cz/matches/JUN`, ordered by date; scores are Liberec first. Club match page lists 17 results. Extra-time subtypes for some matches require result-details recheck; final team-scoring totals match federation 41/71 exactly:

| Date | Opponent | Final LIB–opp |
|---|---|---|
| 2026-09-04 | Litvínov | 2–3 |
| 2026-09-05 | Karlovy Vary | 1–4 |
| 2026-09-11 | Vítkovice | 3–4 |
| 2026-09-12 | Třinec | 3–6 |
| 2026-09-18 | Jihlava | 0–2 |
| 2026-09-19 | Motor | 3–4 after extra time |
| 2026-09-25 | Mountfield HK | 1–8 |
| 2026-09-26 | Pardubice | 1–7 |
| 2026-09-28 | Mladá Boleslav | 3–5 |
| 2026-10-10 | Sparta Praha | 3–5 |
| 2026-10-16 | Plzeň | 5–6 after extra time |
| 2026-10-17 | Slavia Praha | 2–1 |
| 2026-10-23 | Karlovy Vary | 1–2 |
| 2026-10-24 | Litvínov | 4–3 OT (`https://www.hcverva.cz/match/6814`) |
| 2026-10-28 | Poruba | 3–2 |
| 2026-10-30 | Třinec | 1–5 |
| 2026-10-31 | Vítkovice | 5–4 after shootout |

Liberec form from dated results: **L5 GF14 GA16** (2.80/3.20, total6.00); **L10 GF28 GA40** (2.80/4.00, total6.80); **L15 GF38 GA64** (2.53/4.27, total6.80); **L20 only n17 GF41 GA71** (2.41/4.18, total6.59); season n17 same. Windows overlap and are ONE evidence stream, not independent signals. League-level benchmark 6.1486 combined, not an identical-line success-rate baseline.

**H2H:** one corroborated 2026/27 U20 match, 19 September at Liberec, final `3:4` after extra-time handling; Motor won by **1**, both teams scored ≥3 (7 total). No use of U18 matchup 11 Oct (4–3) or senior team results; no trusted current-regime older H2H changes to p.

**Both-side availability/roster:** exact-match federation page `SESTAVY` skaters/goalies empty pregame. Motor general season roster `https://hcmotor.cz/soupiska.asp?kategorie=U20&sezona=2027` shows potential goalkeeper names Štěpán Bogač and Vojtěch Jelínek, **not confirmed**. Club pre-match Onlajny top scorers: Motor Matyáš Humeník (30 points), Jakub Lev (29); Liberec Daniel Pekař (15), Vasyl Špilka (12). Liberec's possible goalie, both lines/bench, scratches, suspensions, illnesses, injury and return reports remain **MISSING / not independently confirmed**. No fabricated absence/health assertions.

#### A4. Distribution, official reference gap, arithmetic and sensitivity

- Source anchor: league μ goals/team =910/296=**3.074324**. Season Motor GF69 GA45 n19 and Liberec GF41 GA71 n17. Using an **illustrative** pseudogame shrinkage constant k=10, rating `O=(GF+k×μ)/(n+k)`, `D=(GA+k×μ)/(n+k)`. Base 60-minute goal centres `λMotor=(OM+DL)/2≈3.604`, `λLib=(OL+DM)/2≈2.635`; sum≈6.239. No league-certified reference or calibrated goal process executed.
- Assumed scenario rates, declared before simulation: low (Motor 3.10, Liberec 2.05, conditional empty net p=.15); base (3.604, 2.635, p=.30); high (4.25, 2.90, p=.45). Weighted **.25/.50/.25** for *illustrative sensitivity*, NOT source-fitted likelihoods. Independent Poisson 60-minute goals, one extra potential empty-net goal on an exactly-one-goal late lead, and a one-goal extra result in regulation draws with arbitrary win split `λMotor/(λMotor+λLib)`. This is **not** a fit to Czech U20 events. The explicit empty-net addition is possibly double-counted by full-game season rates and can bias expected totals and handicaps; quantify as shadow only.
- Runtime: Python 3, NumPy random generator deterministic seed `20261113`, `1_200_000` completed simulations (300k low / 600k base / 300k high), standard source script `hockey_shadow_motor_liberec_20261113.py`. NOT executed: repository `python -m ml reference`, reference freeze, pregame run, canonical ledger or model source admission. No training dataset or performance qualification.
- Shadow outcome probabilities (conditional estimates only): Motor −1.5 **0.474520**, Liberec +1.5 **0.525480**, Over5.5 **0.604422**, Under5.5 **0.395578**, outright Motor **0.679200**, Liberec **0.320800**. Complimentary rows sum to 1.00 by construction (no push under half-lines; no void simulated).
- Scenario outcome matrix:

| Scenario / weight | Motor −1.5 | Liberec +1.5 | Over5.5 | Under5.5 |
|---|---:|---:|---:|---:|
| Low conversion .25 | 0.4412 | 0.5589 | 0.4268 | 0.5732 |
| Base .50 | 0.4581 | 0.5419 | 0.6195 | 0.3805 |
| High pace/goalies .25 | 0.5407 | 0.4593 | 0.7519 | 0.2481 |

- **Sensitivity:** Over5.5 range **0.427–0.752** (crosses 50%), Motor−1.5 range **0.441–0.541** (crosses 50%). No family-level robust numeric advantage. `NO_STRONG_PICK`. Possession/game-width/shot-based fitted covariance and competition-specific goalie effects unavailable.
- **Goal-line budget:** At total 5.5, combinations 3–2 and 4–1 are Under; 3–3, 4–2, 5–1, 5–2 are Over. Motor −1.5 fails 3–2 and on any one-goal OT/SO win; succeeds 4–2 or 4–1. Extra-net risk may turn 3–2 into 4–2, hurting Lib+1.5 and helping Over.
- **Formal league baseline:** `BASELINE_LEAGUE_V1=NOT_COMPUTED`; only official league mean 6.1486 exists, not a certified same-threshold distribution/cohort. Official lineup effects not quantified; applying NHL distributions or 73% EN rule to Czech U20 would be invalid.

#### A5. All four contracts, hypothetical W/P/L/V and pair relations

| Supplied proposition | Qualitative preference | Shadow W/P/L/V (only under assumed operator) | Primary disposition |
|---|---|---|---|
| Motor −1.5 goals | lower-ranked side of spread pair | 0.4745 / 0 / 0.5255 / 0 | NOT_ESTIMATED, not qualified |
| Liberec +1.5 goals | secondary directional | 0.5255 / 0 / 0.4745 / 0 | NOT_ESTIMATED, not qualified |
| Total Over 5.5 goals | strongest directional | 0.6044 / 0 / 0.3956 / 0 | NOT_ESTIMATED, not qualified |
| Total Under 5.5 goals | less supported | 0.3956 / 0 / 0.6044 / 0 | NOT_ESTIMATED, not qualified |

All void values assumed zero **only in illustrative completed-game simulation**; real operator postponement, abandonment, shootout or settlement terms unknown. The first two proposed directional legs are **not independent**; the same Motor two-goal lead that defeats Lib+1.5 can coexist with an Over. Joint failure in simulated complete game states =0.1490, not calibrated. No numerical rank gate passed.

#### A6. Mechanisms, adjustments and counterfactuals

| Mechanism | Known evidence | Effect disposition | Unresolved response |
|---|---|---|---|
| Relative team strength | Motor +24 goals /19, Liberec −30/17; fifth vs fifteenth | Source-backed direction Motor outright, but no effect-table adjustment inferred | Elite goalies, lineup timing and variance may compress 2-goal spread |
| Motor recent defense | L5 allowed 10 goals, 2.0/game, stronger than full-season 2.37 | Widen defensive uncertainty; no automatic Under centre shift due overlapping form | If goalie substitution, this history may not transport |
| Liberec form rebound | Won 3/last 4, long-run defensive 4.18 against | Separate close-game and weak-goalie/large-tail scenarios | Small sample and opponent-strength mixture |
| H2H Sep19 | Motor 4–3 after extra time | One-goal caution for −1.5 and 7-goal path for Over, no direct rate bump | Personnel/regime continuity incomplete |
| Fatigue and travel | Both last played 31 October; youth international break; Liberec travels to České Budějovice and has 14-Nov Jihlava fixture | Potential future workload/context; not a quantified center effect | Travel distance, practices, goalie workload missing |
| Goalkeepers / skaters | Match-centre lineup blank before schedule; Motor season roster not game starters | Scenario widening only, no invented starting/backup grade | Exact starting goalies, lines, scratches, PP/PK details |
| Score state / empty net | Full-game −1.5 prone to late net-pull insurance goals | Model includes stylized EN scenarios for transparency | No measured Czech-junior EN frequency or validation; may double-count |
| Penalties / shot quality | Liberec scored 2 PP goals vs Litvínov on 24-Oct; game-specific units and shot-mix unknown | Mechanistic uncertainty, not a numeric adjustment | Current special teams, expected-goals shot data absent |

**Adjustment dependence:** synthetic scenario results vary with manually specified team λ and EN assumption; no official adjustment ledger, release or formal unadjusted ranking comparison. Independent-Poisson limitations dominate.

#### A7. Family consistency and non-primary comparison

- All shadow contract rows derived from the same simulated two-team score and time-state tree; complementary sums exactly 1 per scenario and mixture. One-goal OT branch never creates a two-goal winner; on 5.5 total, tie goals 0–0/1–1/2–2/3–3 plus one retain threshold classification versus 60 min; operator void still unknown.
- All applicable exact-row width/goaltender guards `NOT_ASSESSABLE` for a **primary** card. Model lacks release qualification, event-specific goalie variance, score covariance/overdispersion fit and official known-at baseline. Historical NHL one-goal percentages were NOT ported to Czech juniors.
- External betting-market odds, predictions and bookmaker probabilities were deliberately excluded. Published probability is **NOT_ESTIMATED** on every supplied row; the executed diagnostics are for sensitivity and not learning-eligible forecasts.

#### A8. Sources, failures, capture plan and no-outcome precautions

| Source or route | Pre-target field observed | Actual gap/limitation |
|---|---|---|
| `https://czehockey.cz/game/detail/178203` | Official U20 match 3156, venue, 12:00 CET fixture, empty game-day lineup tables before official start | Actual start/final/goaltenders NOT_VERIFIED; pregame 0:0 placeholder is not an actual score |
| `https://ceskyhokej.cz/competition/standings/1` | Official 2026/27 team table: full 16 teams, n, GF/GA, position, points | Snapshot modification times not exposed, event-level total history not exported |
| `https://www.hcbilitygri.cz/matches/JUN` | Official Liberec all 17 dated pregame fixtures and results, 12:00 CET current schedule | No exact current lineup, injury/return roster release; some older mirrored 15:30 pages conflict |
| `https://www.hcverva.cz/match/6814` | Liberec won Litvínov 4–3 OT, published 24-Oct and shots 34/26 | Not a pregame current-pace or goaltender estimate |
| `https://www.jchokej.cz/archiv-kratkych-zprav?page=2` | Motor lost 30 Oct HK 3–4, 31 Oct Pardubice 2–3 SO | Motor full L10–20 dated row pack incomplete |
| `https://hcmotor.cz/zapasy.asp?filtrTym=SLA&kde=vsechno&sezona=2027&stats=true` | Motor vs Slavia 3–1 on 19-Oct | Single indexed match, not entire seasonal game list |
| `https://hcmotor.cz/zapasy.asp?filtrTym=PLZ&kde=doma&sezona=2027&stats=true` | Motor vs Plzeň 5–1 on 23-Oct | Single indexed match, no full L15 history |
| `https://hcmotor.cz/soupiska.asp?kategorie=U20&sezona=2027` | Motor youth roster and potential named goalkeepers | Game starting status explicitly UNCONFIRMED |
| `https://m.onlajny.com/match/index/date/2026-11-13/id/540507` | Pre-match standings and scoring leaders, official 12:00 local listing | Live mutable feed deliberately NOT checked for outcome after start; independent organizer listing used |
| `https://hcmotor.cz/zapasy.asp?filtrTym=LIB&kde=vsechno&sezona=2027&stats=true` | Match U20 listed but an older mirror showed 15:30 CET | Time conflict retained, not silently treated as actual start |

**Failed/rejected histories:** broad `hcmotor.cz/zapasy.asp?sezona=2026U20` shows **2025/26** and would incorrectly join two seasons; excluded in favor of 2026/27 official federation and 2027 team-filtered match results. Some general club pages mix senior U18/U20 results; those are excluded. Exact injury/goalie evidence was not recovered and must not be assumed absent. No target live/final score searched after pre-event status check, so analysis avoids outcome-conditioned inputs; nevertheless the post-schedule output is NOT a pregame issue.

**Capture after explicit settlement request:** field owner full match report + match 3156 status and period scores/goalies/first puck; independent club Hokej.cz results; original score/goal sum; operator-defined void/OT as a separate term. No background monitoring was scheduled.

#### A9. Integrity receipt, completion matrix and limitations

| Procedure | Actual work performed | Gap / affected contract | Status |
|---|---|---|---|
| Exact event, source controls, duplicate and time | Czech federation match 3156, U20 aliases/venue, distinct from seniors/U18, current mini G0007 free; main SHA pinned | conflicting 12:00 vs archived 15:30 CET; actual first play unknown | DONE_WITH_GAP |
| Both teams' starters, bench, goaltenders, absences | Official blank game-day sheet checked; Motor season roster inspected; searched club/report pages | BOTH goalies, all starter/bench/medical and precise scratches remain unconfirmed | INFORMATION_INCOMPLETE |
| Verified prior games and independent search | Lib 17 dated club records; Motor five dated matches with club/regional corroboration; excluded stale previous-season page | Motor full L10/L15/L20, cross-field independent source per date incomplete | INFORMATION_INCOMPLETE |
| L5/L10/L15/L20, season, league | Exact Lib L5/10/15/17; Motor L5, season n19; league all 16 rows/148 games | Motor complete L10/L15; L20 has only n19 season aggregate not dated list | INFORMATION_INCOMPLETE |
| Sport mechanisms, venue, conditions, rules | Relative strengths, H2H, travel and break, shot/special-teams and empty-net risk, indoor applicability | field-owner youth OT/SO fine terms and goaltender performance | DONE_WITH_GAPS |
| Official reference, lineup mixtures, freeze, formal baseline | Read pinned rules and league mean; disclosed numerical model limitations | No repository model release/ref/freeze, no exact-row baseline cohort | NOT_RUN |
| Analytic distribution, assumptions, simulation | Deterministic 1.2m simulation script, output JSON, three rate/EN scenarios with actual model math | Unfitted youth league parameters, no measured goalie/score-state/shot model; shadow only | SHADOW_EXECUTED |
| Every owner line, complementary W/P/L/V | Four full-game contracts assessed with support, counterarguments and shadow exact masses | p_card formally NOT_ESTIMATED; operator void unresolved | DONE_QUALITATIVE |
| Expected scores, sensitivity, dependence, loss joint | Shadow 3.779–2.652, total6.431, scenario ranges; joint losing states 0.1490 | No fitted primary expected score or calibrated p | SHADOW_ONLY |
| A1–A9, local custody and readback | All appendices recorded and prior cards checked through local writer script | No GitHub commit, freeze, model receipt or C1–C27 repo lint by owner override | CHAT_LOCAL_ONLY |

**Overall research status:** `INFORMATION_INCOMPLETE`; missing fields explicitly held above. **Forecast:** `UNCALIBRATED_QUALITATIVE / EXECUTED_EXPLORATORY_1_200_000_SHADOW / PRIMARY_NOT_RUN`. **Issue:** `POST_OFFICIAL_SCHEDULE_TIME / ACTUAL_START_UNVERIFIED / CHAT_LOCAL_READ_ONLY_DRAFT / NOT_REPOSITORY_ISSUED`. **No strong/high-confidence pick.** **Model values are not published probabilities.** Local writer and footer/index readback receipt is separately saved after the append.

**SPORTS_ONLY_MARKET_BLIND:** YES · **OUTCOME_EXPOSURE:** NO_TARGET_LIVE_OR_FINAL_SCORE_USED · **SETTLEMENT:** NOT_PERFORMED · **CANONICAL_IMPORT:** NOT_PERFORMED
<!-- END CARD LOCAL-20261112CC53B5C806-G0007 -->

<!-- BEGIN CARD LOCAL-20261112CC53B5C806-G0008 -->
## Card · LOCAL-20261112CC53B5C806-G0008 · Tennis / Orléans Challenger 125 · Zsombor Piros vs Daniel Altmaier · 2026-11-13 CET

- **Local event key:** `LOCAL-20261112CC53B5C806-G0008` — `LOCAL_UNIMPORTED_EVENT`; canonical ID `NOT_ASSIGNED / PROMPT_4_IMPORT`.
- **Competition / format:** 2026 ATP Challenger Orléans (Co'met Orléans Open), men's singles quarterfinal; indoor hard court, best-of-three, ordinary 6–6 tiebreak assumed; final-set tiebreak detail not independently reverified.
- **Identity:** [7] Zsombor Piros (HUN) versus [2] Daniel Altmaier (GER), no verified historical H2H. Tournament official timetable confirms quarterfinals Friday 13 Nov; Tennis-France and contemporaneous order-of-play reporting list 13:00 CET; other providers list conflicting 10:00/11:00 UTC provisional times.
- **Scheduled time:** owner estimate `2026-11-13T23:00:00+11:00` = 2026-11-13 13:00 CET = 12:00 UTC, corroborated by published Court 1 order-of-play reporting; actual first service `NOT_VERIFIED`.
- **Research completion / record capture:** `2026-11-13T22:58:23+11:00` AEDT; time and phase are independent of actual first serve; do not certify prospective issue without a verified pre-start cutoff and immutable published freeze. The prior official listed time is the relevant cutoff; known-at of dynamic stats is partly unverified.
- **Authority:** GitHub `danisgreat/Sports-Research`, read-only pinned `008cedc4ff469e7a808292aa3667a7bffe22e273`; MDS/P v24.16 / CR-2026.11.11-R4 and 2026-11-12 records R1 / prompt P-2026.11.11-v24.14 / SCV-v13 / SEL-v4; user overrides publication in favor of chat-local drafts.
- **Research / primary status:** `INFORMATION_INCOMPLETE / UNCALIBRATED_QUALITATIVE / PRIMARY_P_NOT_ESTIMATED / READ_ONLY_DRAFT / NOT_REPOSITORY_ISSUED`.
- **Independent diagnostic:** exact completed-match scoring-tree enumeration, **not** Monte Carlo, with scenario source script `tennis_shadow_piros_altmaier_20261113.py` and JSON `TENNIS_SHADOW_DIAGNOSTIC_20261112CC53B5C806-G0008.json`; all displayed numbers are **shadow-only** and not framework p_card, official published odds or certification.
- **End points / action:** completed best-of-three total games and net games margin including tiebreak sets as 7–6; Piros +2.5 wins if Piros games minus Altmaier games ≥−2; Altmaier −2.5 wins if margin ≤−3; Over 22.5 wins when total ≥23, Under wins when ≤22. No push for half-lines if completed; withdrawal/retirement/void handling unknown without operator terms.
- **Learning:** `LEARN_RECORD_INCOMPLETE`; five dated recent matches for each player verified to descriptive level, but full L15/L20 match-score archive, publication timestamps, and point-level source-event provenance not independently reconstructed. `PENDING_SETTLEMENT`; no league learning write.
- **Lineup and health:** Individual tennis starters are the participants if play begins; both named participants confirmed in tournament draw; no confirmed fitness clearance, medical reports, or retirement status. Prior reported MTOs found in nonofficial preview, NOT independently admitted as a health fact.
- **Sources, known-at:** see A3/A8. Retrieval during current chat before/scheduled near start, original publication timestamps missing for some dynamic pages; do not designate CLEAN_PRE_START_INPUTS for an unverifiable original availability claim.
- **Model availability:** `ML_NOT_RUN` for repository formal reference, kit, card lint, freeze and learning log; chat-local exact-scoring diagnostic `EXECUTED_NOT_PRIMARY`; not a trained or calibrated Challenger model.

### Decision block

**Qualitative leading direction: Over 22.5 games (LOW confidence).** It survives all four exploratory score-strength scenarios, unlike either games-handicap side. A close straight-set match or dominant Altmaier service game is the principal failure mechanism. No safe/high-confidence certified selection.

| Rank | Role | Tag | Contract key and exact proposition | p_card | p_base | BASELINE_P | Line distance | Probability basis | Main failure route |
|---|---|---|---|---|---|---|---|---|---|
| 1 | QUALITATIVE_LEAN | SUPPLIED | T-OVER22.5: completed match total ≥23 | NOT_ESTIMATED | NOT_ESTIMATED | BASELINE_UNAVAILABLE: Challenger peer cohort not frozen | Not estimated for primary | QUALITATIVE; separate exact-chain shadow below | Quick two-set match without enough tiebreaks |
| 2 | SECONDARY_QUALITATIVE | SUPPLIED | P-PLUS2.5: Piros games margin ≥−2 | NOT_ESTIMATED | NOT_ESTIMATED | BASELINE_UNAVAILABLE | Not estimated for primary | QUALITATIVE; high opponent-sensitivity in shadow | Altmaier serves at current two-match rate and dominates breaks |

**All supplied propositions, independent exact-chain sensitivity (NOT p_card):**

| Contract | All-surface 52wk | Indoor shrink-20 match | Indoor 52wk alone | Two-match high-variance stress | Direction / action |
|---|---:|---:|---:|---:|---|
| **Piros +2.5 games** | 72.574% | 71.777% | 67.005% | 35.368% | Not stable across all samples; no certified p |
| **Altmaier −2.5 games** | 27.426% | 28.223% | 32.995% | 64.632% | Opposite to Piros +2.5; not independent evidence |
| **Over 22.5 games** | 59.644% | 61.151% | 64.288% | 52.886% | First qualitative direction; low confidence |
| **Under 22.5 games** | 40.356% | 38.849% | 35.712% | 47.114% | Complement of Over; quick straight-set win route |

**Baseline coverage:** 0 numeric primary rows; no trustworthy Challenger league-only comparator. **Rank-1 gate:** NOT_ASSESSABLE, no calibrated p_card or precision test. **Rank-2 floor:** NOT_ASSESSABLE. **Winner:** official winner probability NOT_ESTIMATED; shadow Piros matchwin 58.1% indoor-shrunk, across tested sources 21.8%–59.7%; not decision-ready. **Joint failure:** within indoor-shrink scenario, P(Piros +2.5 loses AND Over 22.5 loses) = 0.1480, computed as P(Under 22.5) − P(Piros +2.5 AND Under 22.5) = 0.3885 − 0.2405; this is not independent-leg probability. **No push** for completed half-lines; void terms unresolved. **Abstain** is reasonable, since no primary numeric contract meets qualification.

### Appendix

#### A1. Identity, scheduling, state

Exact participants/round/venue: [7] Piros vs [2] Altmaier; Orleans France, indoor hard, Challenger 125 quarterfinal, best of three. Tournament organizer programme lists QF Friday 13-Nov; independent scheduling lists 13:00 Paris and user estimates 23:00 Melbourne. Other schedule vendors conflict at UTC 10:00 or 11:00; do not silently discard conflicts. Original start/progression/withdrawal not verified at issue. No other mini key or prior card for this target. `TIMING_UNVERIFIED` until exact first ball; prior score/result not viewed and no outcome exposure claimed.

#### A2. Frozen supplied contracts and full universe

Only four user-supplied full-match propositions ranked qualitatively; no derived lines/market prices considered:
- `Piros handicap +2.5`: unconditional full completed match W if Piros net games margin ≥−2, L otherwise; P=0, V only if retirement/WO under missing operator contract.
- `Altmaier handicap −2.5`: W if Altmaier net games margin ≥3, L otherwise; complementary to first on fully completed matches.
- `Total Over 22.5`: W if ≥23 games played in completed match; L if ≤22; half-line, no push.
- `Total Under 22.5`: W if ≤22; L if ≥23, complementary to Over.
- Matchwinner for both sides is informational only, not an owner's additional line and has no primary p.

#### A3. Evidence, recent history and roster/medical

Sources with precise URLs and retrieved or examined in current chat around `2026-11-13T22:58:23+11:00` AEDT:
1. Tournament fixture and schedule: `https://opendorleans.com/programmation/` (organizer tournament stage, no exact match clock); `https://www.tennis-france.com/tournois/orleans-2026` (13:00 Paris); `https://tennistonic.com/tennis-news/1081224/prediction-preview-h2h-altmaier-piros-martinez-portero-and-basavareddy-to-play-on-court-1-on-friday-orleans-challenger/` (scheduling and factual match scores only, **none of its odds or predictions used**); `https://www.sofascore.com/tennis/match/zsombor-piros-daniel-altmaier/iUabsVpHb` (conflicting 10:00 UTC provisional schedule). Date of page publication often unknown; field-level original known-at remains unverified.
2. Tournament draw: `https://en.sportsand.me/tennis/challenger-orleans?tab=draw` (result dates, draw; page also contains odds, intentionally not used); `https://en.sportsand.me/tennis/team/zsombor-piros?tab=calendar` (Piros dated results).
3. Historical and opponent service facts: `https://www.tennisexplorer.com/match-detail/?id=3377369` (2026 indoors Piros 13–3, Altmaier 6–4, overall season scope Piros 55–25 and Altmaier 27–34, rank around 99/73); `https://www.stevegtennis.com/head-to-head/men/Daniel_Altmaier/Zsombor_Piros/` (two-round score and service game numerators); 52-week serve/return statistics table at `https://pythiatennis.com/daniel-altmaier-vs-zsombor-piros-prediction-and-stats/?d=2026-11-13` (**raw historical stat columns only; no output or market/pricing used**). These are not federation-certified underlying row snapshots; named profile definitions differ.
4. Head-to-head: first recorded tour meeting (`0–0`); no previous verified match record. Height/handedness from TennisExplorer; not entered as a numeric effect.

**Five most recent played matches (the overlapping L5 form window):**

| Player | Date | Event | Opponent | Match outcome, sets | Pre-cutoff evidence and caveat |
|---|---|---|---|---|---|
| Piros | 2026-11-11 | Orléans CH R16 | Clément Tabur | W 2–6, 7–6(6), 6–3 | Draw and matches; qualifying service stats not full raw point feed |
| Piros | 2026-11-10 | Orléans CH R32 | Luca Nardi | W 7–6(2), 1–6, 6–4 | Draw and matches |
| Piros | 2026-11-06 | Bratislava 2 CH QF | Dalibor Svrčina | L 6–4, 0–6, 4–6 | Piros scores from opponent-side display |
| Piros | 2026-11-04 | Bratislava 2 CH R16 | Sascha Gueymard Wayenburg | W 6–3, 6–7, 6–3 | Tiebreak points unavailable in one feed |
| Piros | 2026-11-02 | Bratislava 2 CH R32 | Matthew William Donald | W 6–3, 6–3 | No retirement reported, not proof of medical fitness |
| Altmaier | 2026-11-11 | Orléans CH R16 | Buvaysar Gadamauri | W 3–6, 7–5, 6–1 | Match results from draw; opponent qualified |
| Altmaier | 2026-11-10 | Orléans CH R32 | Adrien Gobat | W 6–2, 3–6, 6–3 | Qualifying opponent; two-set service split in stat provider |
| Altmaier | 2026-10-31 | Paris Masters qualifying | Alex Molčan | L 4–6, 6–7 | Official match date/time provider comparison needed |
| Altmaier | 2026-10-29 | Basel ATP R16 | Jiří Lehečka | L 5–7, 4–6 | ATP vs Challenger competition-level difference |
| Altmaier | 2026-10-26 | Basel ATP R32 | Juan Manuel Cerúndolo | W 6–7, 7–6, 6–4 | Tiebreak details in secondary provider |

**L5:** Piros 4–1, Altmaier 3–2. **L10:** Piros 7–3, Altmaier 6–4 based on secondary statistical digest, not independently reconstructable complete dated game rows here. **L15/L20:** `NOT_VERIFIED`, cannot print true n and opponent-adjusted rate. **2026 indoor:** Piros 13–3, Altmaier 6–4 in TennisExplorer view; other publishers show Piros 14–3/Altmaier 6–5 because of source scope/timing; do not merge as independent facts. **2026 season:** sources vary e.g. Piros 51–23 vs 55–25 and Altmaier 27–34, depending event/retirement/snapshot inclusion. `SEASON_SCOPE_CONFLICT` flagged rather than fabricated resolution. Specific level-adjusted opponent strength unavailable.

**Exact-match two-round serving evidence** (unfitted and very small): Altmaier 27 aces, 24/27 service games held (89%) and 109/155 service points (70.3%); Piros 15 aces, 23/30 holds (77%) and 135/224 service points (60.3%); their return-points-won ratio 38.2% vs 35.7%, respectively. Source SteveG, two matches. First opponent-quality problem: both Altmaier opponents were qualifiers; stronger numbers may not translate unchanged against Piros's return. Piros faced stronger prior opponents in mixed indoor Challenger fields. These last-two matches already sit inside 52-week indoor samples, no double-counted adjustment.

**Health/participants:** both listed in quarterfinal draw. No independently confirmed new injury, MTO, withdrawal, limited serving, medication, physiotherapy or coaching change; `INJURY_STATUS_UNVERIFIED`, not healthy confirmed. Bench/replacements `N/A` for individual tennis singles; travel is back-to-back European indoor weeks for Piros, Altmaier Paris/Basel to Orleans, but workload and recovery remain conditional.

#### A4. Distribution and sensitivity, arithmetic

**Model shadow (not primary):** exact recursion over point service probability → service hold → alternating server game states → 6–6 tiebreak → best-of-three set states and completed match total/margin. Each scenario sums all terminal match-score state masses to 1. P(game hold) = p⁴(1+4q+10q²) + 20p³q³ × p²/(p²+q²), q=1−p. Initial server 50:50. Tie-break server order is 1–2–2–2. No point-by-point actual model was run on the official repository. Shadow code under `/mnt/data/tennis_shadow_piros_altmaier_20261113.py` and JSON separately retained.

52-week sourced point win rates: Piros SPW 62.3% all / 63.7% indoor, RPW 39.0% all / 37.0% indoor, 72 all / 16 indoor matches; Altmaier SPW 62.9% all / 69.1% indoor, RPW 34.5% all / 31.1% indoor, 60 all / 10 indoor. Opponent match-up approximation **Piros serve p=½[Piros SPW+(1−Altmaier RPW)]**, vice versa for Altmaier; indoor shrink setting n₀=20 equivalent matches, explicitly *unfitted sensitivity* rather than optimized/validated coefficient.

| Scenario | Piros matchup SPW | Altmaier matchup SPW | Expected games | P(deciding set), shadow | Piros matchwinner, shadow |
|---|---:|---:|---:|---:|---:|
| All surface | 0.639 | 0.619 | 25.32 | 49.2% | 59.7% |
| Indoor shrink20 | 0.650 | 0.633 | 25.62 | 49.4% | 58.1% |
| Indoor only | 0.663 | 0.660 | 26.21 | 50.0% | 51.2% |
| Two-round stress | 0.611 | 0.673 | 24.50 | 42.1% | 21.8% |

All scenario numbers are **uncalibrated conditional forecasts, not confidence intervals**, likely overstate precision and do not have an independent skill certificate. Point-service independence, unweighted opponents, score-state/pressure, return/serve covariance, retirement terms and break-point volatility all cause error. The most adverse recent-two stress has a much larger Altmaier serving advantage; long-run indoor-only outcomes favor Piros's return enough to preserve the cushion. Because that short-run scenario already overlaps the long-run 52-week sample, it is a **stress test, not a fourth independent piece of evidence or mixture weight**. Formal reference stage, frozen baseline/adjustments, simulation release and ledger verification were not run; shadow does not fill them.

**Expected score:** formal primary NOT_COMPUTED. Indoor-shrink shadow only: approximate expected total and Piros minus Altmaier total-games margin in table above; shadow approximate player games (T+M)/2 and (T−M)/2. These are means across different set counts, not an achievable match score or prediction of a particular final. A 7–6, 6–4 straight-set match totals 23 and meets the Over; 6–4, 6–4 totals 20 and stays Under. Three full sets generally cross 22.5, but early retirement/short decider conventions differ and must be verified.

**League-only baseline:** `NOT_RUN / BASELINE_UNAVAILABLE`, no time-stamped Challenger cohort over identical best-of-three indoor 22.5 and handicap 2.5 was accessed. No retrospective 0.5 substitution. **Adjusted reference:** `NONE`, no official released model or coherent frozen input verified; independent shadow is not a replacement for the formal stage. **Sensitivity:** numeric four-case table above. **Calibration:** no validated scope, NO_DEMONSTRATED_SKILL by tennis rule. **Primary confidence:** low.

#### A5. All propositions and W/P/L/V

Propositions are complements within each line family, but not between families. All completed games half-lines have W+L=1, P=0, V=0 under assumptions. The uncalibrated shadow gives p(W) by scenario as in Decision table; p(L)=1−p(W). For unknown retirement and operator void, unconditioned V cannot be estimated. Cross-family joint at indoor-shrink: Piros cushion AND Under is printed in Decision block; P(Over AND Piros cushion) can be derived from shared match score object, never multiplication of marginals. No modeled edge over a user-supplied price, as none was used.

#### A6. Adjustments and playing context

| Mechanism | Factual basis | Numerical adjustment? | Uncertainty / direction |
|---|---|---|---|
| Indoor surface and form | Piros 13–3 2026 indoor; Altmaier 6–4, shorter Altmaier schedule | No primary; indoor vs all-surface scenarios only | Piros return can shorten Alt holds; indoor speed increases tiebreak frequency |
| Current serve | Altmaier 24/27 holds in first two vs Piros 23/30 | No primary; recent-two stress only | Can reverse handicap, while total retains modest Over in model |
| Return and opponent level | Piros returns a higher share of points all-surface; Altmaier faced two qualifiers | No scalar | Overweighting one-week service runs is a known failure route |
| Workload/rest | Both last played 11 November, two three-set Orléans wins each | Scenario width only | Fatigue may widen break-rate tails both directions |
| Venue/conditions | Indoor hard court, both right-handed; ball speed not verified | No scalar | No outdoor weather effect; court speed unquantified |
| Medical | No current injury clearance or MTO cross-verified | No scalar | Late withdrawal could void, constrain or shift service |

#### A7. Family, branch and coherence checks

- Both players can win 2–0 or 2–1; every terminal match state is derived from same joint score grid. Piros +2.5 and Altmaier −2.5 sum to 1 for fully completed event, as do Over/Under 22.5. No push. Winner and games handicap are **not** constrained to move together in tennis (a deciding-set loser may win more games overall), unlike standard points sports.
- Piros recent three-set matches support long-match branches, but Altmaier two matches also three-set; these are overlapping endpoint observations rather than independent model certifiers. The three-set branch in indoor shrink is roughly half of completed matches, unfitted and perhaps too high.
- `RANK1_UNSTABLE` numerically not assessable: no formal p_card/ε/league comparator; shadow direction for Over stable across scenario set but fails high-confidence qualification.
- No scenario demonstrated prospectively calibrated advantage over league reference; avoid assertions of a safe or near-certain bet.

#### A8. Source register, failures, timing and capture plan

| Source / URL | Decisive fields checked | Status / gaps |
|---|---|---|
| Tournament organizer https://opendorleans.com/programmation/ | Competition quarterfinal date, stage, publishing process | Organizer page may have old cached editions; Friday stage reverified by contemporaneous draw |
| Tennis-France https://www.tennis-france.com/tournois/orleans-2026 | Court 13:00 CET listing | Independent schedule, actual match start not confirmed |
| Tennis Tonic https://tennistonic.com/tennis-news/1081224/prediction-preview-h2h-altmaier-piros-martinez-portero-and-basavareddy-to-play-on-court-1-on-friday-orleans-challenger/ | First 2 results and Court 1 time; no odds or predictions admitted | Publication 13-Nov; timestamp to minute missing |
| TennisExplorer https://www.tennisexplorer.com/match-detail/?id=3377369 | Ranking, indoor records, player dimensions | Dynamic stats cache conflicts in exact season match n |
| SportsAnd https://en.sportsand.me/tennis/challenger-orleans?tab=draw | Progression and score lines | Betting content intentionally ignored; no official point-level match feeds |
| SteveGTennis https://www.stevegtennis.com/head-to-head/men/Daniel_Altmaier/Zsombor_Piros/ | Set/serve/return numerators at event | Two-match sample; competition/opponent confounding |
| PythiaTennis https://pythiatennis.com/daniel-altmaier-vs-zsombor-piros-prediction-and-stats/?d=2026-11-13 | Raw 52wk SPW/RPW counts only | Fitted predictions, odds, rankings, returns **NOT used**; underlying original match-level feed not audited |
| Sofascore https://www.sofascore.com/tennis/match/zsombor-piros-daniel-altmaier/iUabsVpHb | Competing 10:00 UTC schedule | Conflicts with 13:00 CET / 12:00 UTC order-of-play, source likely stale |

**Next evidence requirements:** verify first-serve and full official match result from ATP Challenger score centre; find original 13-Nov organizer order-of-play PDF and exact source release time; confirm official player fitness, any MTO/withdrawal, match rule (retirement treatment per operator) and full dated surface L15/L20 stats; only then consider a new dated source refresh. All due dates are triage targets, no automation scheduled, no future result-check promise. Avoid original outcome exposure in a pregame card.

#### A9. Completion and readback audit

| Procedure | Actual work / result | Remaining gap | State |
|---|---|---|---|
| Authority, native identity, duplicate | Read pinned GitHub rule-set and existing G0001–G0007, exact participants/draw | No repository lease or working tree issue | CHAT_LOCAL_ONLY |
| Event start/venue/state | Orléans QF, indoor; 13:00 CET order of play cross-checked | Actual first ball and competing provisional provider times | DONE_WITH_GAPS |
| Players, roster, injury and availability | Names/draw verified, no substitutes in singles | New injury clearance / medical release not found | INCOMPLETE_EVIDENCE |
| Online historical form and sources | Dated 5 matches each; 2026 indoor records and conflicting season totals | Complete sourced L15/L20 and per-point opponent-adjusted source archive | INCOMPLETE_EVIDENCE |
| Sport mechanisms | Serve/return, tiebreaks, best of three, rest, opponent level, retirement | Quantified court speed/fitness and tiebreak game rule confirmation | DONE_WITH_GAPS |
| Reference, model execution, calibration | Exact scoring diagnostic script executed; output file with scenarios | Formal primary reference/baseline, ledger, kit, model freeze not executed | SHADOW_ONLY |
| Contract and sensitivity | Four owner lines including W/P/L/V, four scenario comparisons | Operator retirement terms; no calibrated p_card | DONE_QUALITATIVE |
| Expected score/dependence | Shadow total/game margin, common-state probability, scenario ranges | No primary expected score or exact baseline | SHADOW_ONLY |
| A1–A9, mini append, custody | Whole card, prior-block identity check, intake/footer/queue update, SHA-256 receipt | No repository commit, pregame freeze or GitHub published issue | CHAT_LOCAL_DRAFT |

**Overall information status:** `INFORMATION_INCOMPLETE`; **forecast status:** `UNCALIBRATED_QUALITATIVE / PRIMARY_P_NOT_ESTIMATED / EXPLORATORY_EXACT_ENUMERATION_SHADOW`; **issue status:** `TIMING_UNVERIFIED / CHAT_LOCAL_NOT_ISSUED_IN_REPOSITORY`; **settlement:** NOT_PERFORMED; **canonical import:** NOT_PERFORMED. Any numeric scenario results are **not** validated primary probabilities.

**SPORTS_ONLY_MARKET_BLIND:** YES (no source odds/picks used) · **OUTCOME_EXPOSURE:** NO_MATCH_RESULT_USED · **GITHUB_WRITE:** NO
<!-- END CARD LOCAL-20261112CC53B5C806-G0008 -->

# RUNNING FOOTER
<!-- BEGIN FOOTER -->
| Field | Value |
|---|---|
| Last local event key / next local event key | `LOCAL-20261112CC53B5C806-G0008` / `LOCAL-20261112CC53B5C806-G0009` |
| New canonical IDs assigned | NONE; assignment only at `PROMPT_4_IMPORT` |
| Repository next-ID snapshot | `P-639` (read-only context; unallocated) |
| New cards / numeric / qualitative / NO_FORECAST | `8 / 0 / 8 / 0` (G0001–G0008, all qualitative primary with independently executed uncalibrated diagnostics; no numeric primary) |
| Pending events / unresolved evidence records | `8 / 0` (evidence gaps within pending cards; no independent terminal unresolved record) |
| Local mini status / import status | `ACTIVE_CHAT_LOCAL_DRAFT` / `NOT_PERFORMED` |
| Repository active-mini pointer | NONE (by `CR-2026.11.12-R1`; not modified) |
| GitHub writes performed | NO |
| GitHub push performed | NO |
| Repository issue/freeze | `NOT_ISSUED` / `NO_REMOTE_FREEZE` |
| Last update | `2026-11-13T22:58:23+11:00` (chat-local G0008 append/readback; 23:00 AEDT scheduled start, actual first-ball not verified) |
<!-- END FOOTER -->
