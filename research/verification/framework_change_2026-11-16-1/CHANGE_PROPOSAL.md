# Change proposal · 16 November 2026 · how to improve the framework

Written for the owner. Prompt 8 at P-2026.11.15-v24.18, from the [on-request comprehensive audit](../retrospective_2026-11-16-1/RETROSPECTIVE_REPORT.md) of P-001 to P-685 and a review of every operating document, prompt, register and `ml/` module. Base HEAD `4e60611bc`.

**Instruction (owner, 16 November 2026):** review all files, apply the framework's improvement rules and say how to improve it fully.

**What was done under that instruction:** four defect repairs and two stale pointers ([IMPLEMENTATION](IMPLEMENTATION.md)), classed as bug fixes that change no forecast or recorded score, which FREEZE-v1 allows. **Everything else below is a proposal.** Items marked OWNER DECISION change what is measured or how a card is made; FREEZE-v1 reserves those for an owner order, so none was implemented.

## The problem in one paragraph

The rules describe cards made in this repository from a frozen reference, with a ledger, a linter and three model lanes, plus a five-lane external comparison. The work actually done is one chat per game writing its own card, settled here later. Because the two do not meet, the ledger has 0 rows, the model lanes have 0 frozen games, the learning-log dataset has 0 games and the 100-game assessment has 0 eligible games. Meanwhile 45 framework changes in 37 days have left 2 MB of operating text and 111 named controls. The improvement is to measure the card the chat really writes, feed the learning from it, and stop changing rules until 100 such games are in.

## Priority 1 — make the chat's card the measured object (OWNER DECISION)

| ID | Change | Disposition | Acceptance |
|---|---|---|---|
| **M-1** | Replace the unstarted FIVE_LANES against SINGLE_RESEARCH experiment with one registered cohort, **ONE-CHAT-v1**: one chat per game, one card, the first 100 games in order of settlement. Keep EXT-EVAL-v2's counting rules (games not picks, no calendar minimum, cohort frozen, on-request audits never promote). | ADOPT, needs owner order | A new evaluation plan naming the forecast identity, the comparator and the metric before the first game |
| **M-2** | Every supplied line gets a number for both sides. A lean without a number stays allowed but is recorded UNPRICED and never ranked. Today 58% of rows have no number and cannot be scored. | ADOPT with M-1 | Share of supplied lines with a number, reported per drop; target 100% |
| **M-3** | Each card ends with one fixed block the import can read without interpretation: one CSV row per supplied line (contract, side, line, p), the request time, the research start time and one not-started observation (page and time). It is the PICKS_V2 idea cut down to what a chat can fill. | ADOPT with M-1 | `ml` parses the block for every card of a drop with no hand transcription |
| **M-4** | The comparator is computed here at import, never by the chat: the constant 0.5 for a supplied two-way line, and the league base rate where a parameter row exists. This is the same-row baseline every past cohort lacked. | ADOPT with M-1 | Paired table printed by the import for every drop |
| **M-5** | Custody before the result: the owner saves each card file as soon as the chat finishes. The import compares the file's saved time with the official start and labels the card pre-start, post-start or unknown. Today 22 of 75 cards were last written after the start and 12 had no clock. | ADOPT with M-1 | Pre-start share reported per drop |
| **M-6** | Primary metric: card-mean Brier minus 0.25 on supplied lines, with its 95% interval over games; success is -0.01 or better with the interval below zero, plus the calibration table. Rank 1 and Rank 2 win rates are reported beside it, not instead of it. | ADOPT with M-1 | Written into the M-1 plan |

Until M-1 is ordered, the existing plan stays registered and stays empty.

## Priority 2 — hold the rules still (already the owner's rule; keep it)

| ID | Change | Disposition | Acceptance |
|---|---|---|---|
| **G-1** | Apply FREEZE-v1 as written: no rule, format or selection change until the 100-game cohort is assessed. Bug fixes, source refreshes and records continue. | ADOPT (no new text needed) | Zero method or prompt version changes between M-1's start and its assessment |
| **G-2** | One version file. Today a rule change restamps about 27 prompt and index files by hand and archives 5 to 40 originals. Keep versions in one CSV and have `ml state --write` print them wherever they appear. | ADOPT at the next permitted release | A release touches the changed rule, the version file and the changelog only |
| **G-3** | Cut the standing text. CURRENT_STATE (52 KB) keeps its generated block and pointers; its dated paragraphs move to research/history. The 30 banner paragraphs repeated in eight or more files are stated once in CORE and linked. CORE returns to the 16 KB it was designed to be. | ADOPT at the next permitted release; editorial, no rule changes | CORE ≤ 16 KB; prompt 1 plus one sport file ≤ 30 KB; test_prompt_consistency still passes |
| **G-4** | Retire text for routes no longer used: the five-lane profile, lane briefs and L1–L6 audit supplement become history when M-1 starts; one chat brief of at most two pages replaces them. | ADOPT with M-1 | A chat needs one brief, the kit, the sport's source list and the do-not-open list |

## Priority 3 — give the learning something to learn from

| ID | Change | Disposition | Acceptance |
|---|---|---|---|
| **L-1** | Save the result page at settlement. Settlement already opens a permitted page for every final; keeping that capture with its hash lets every settled card game enter the learning store. Today 20 of 5,402 store events are card games. | ADOPT (procedure, no forecast change) | Each import reports store events added = games settled with a capture |
| **L-2** | A fixed FACTS block per card (per side: last 5, 10 and 20 results and scoring, rest days, home or away, named absences with status, competition average), filled by the chat from its research. This is the only way to learn which research facts predict; CARD-TRAIN-v1 has only sport, contract type, rank and p to work with and finds nothing beyond p. | ADOPT with M-3, OWNER DECISION (format) | `ml learning-log build` admits every card of a drop |
| **L-3** | One model per sport, tested on held-out competitions, for basketball, ice hockey and baseball as POOLED-v1 does for soccer, built from the store and the open bulk history. Retire the three stale per-league releases and move the 29 per-league workshop folders to the archive. | SHADOW; statistical, so build and test now, use only after the cohort (STATFREEZE-v1) | Held-out-competition Brier against the league base rate, interval below zero, before any use as a reference |
| **L-4** | Count review clocks on card games, not on backfilled store results (3,695 backfilled NBA games currently trip every clock). | ADOPT (small code change, reminders only) | `ml learning-status` DUE rows match settled card games |
| **L-5** | Once the FACTS block has 100 games, refit the size of the research move and any availability effect from them. Not before. | DEFER until L-2 has data | Registered study with tune and evaluation windows apart |

## Priority 4 — forecast-quality hypotheses from the audit (all PROPOSED_NOT_TESTED)

Each comes from outcome-exposed tables, so each needs the next cohort to test it. None may be applied to cards now.

| ID | Hypothesis | Evidence | Test on the M-1 cohort |
|---|---|---|---|
| **H-NODIR** | A number within 5 points of 0.5 is no direction and is never ranked. | 819 rows below 0.60 scored no better than 0.5; November chat numbers averaged 0.509 and won 0.510 | Rank 1 win rate with and without such rows; registered before the cohort |
| **H-BAND** | Stated 0.60 to 0.65 is overconfident by about 10 points. | 147 rows on 114 cards: stated 0.621, won 0.517, gap -0.10 [-0.19, -0.01] | Same band on new games; if it repeats, a shrink toward 0.5 is tested |
| **H-AVAIL-CHAT** | A lean that rests on an absence with no measured effect is recorded UNPRICED. | 4 of 4 such deep loss reviews were ERROR (P-674, P-676); AUDIT-v1 already forbids it for issued cards | Count and results of UNPRICED-for-absence rows against priced ones |
| **H-OWN-EVIDENCE** | A lean that contradicts a figure printed on the same card is refused at intake. | 4 reviews (P-662, P-671, P-678, P-680) | Needs M-3 so the check is mechanical |
| **H-SPORT** | Tennis, American football and Australian rules numbers are worse than 0.5. | +0.028 [-0.007, +0.063] on 20 cards; +0.038 [+0.014, +0.062] on 7; +0.099 on 4 | Same table per sport; the samples are small |
| **H-PERIOD** | Period and corner Overs win more than Unders at supplied lines. | Period Over 67.6% (102), Under 45.8% (96); corner Over 67.5% (83) | Same split on new games; difficulty of the lines is not controlled |

## Priority 5 — settlement and sources

| ID | Change | Disposition | Acceptance |
|---|---|---|---|
| **S-1** | Retry the unresolved queue (82 rows on 32 cards) with the eight routes added on 16 November: P-664 final, the WBBL six-over scores, the ODI five-over score and the Kashiwa corners first. | ADOPT (records only) | Rows moved from UNRESOLVED with a cited permitted source |
| **S-2** | At request time, flag any supplied line whose result field has no permitted settlement source for that competition (phase scores and corners in minor leagues), so the owner knows before the game. | ADOPT with G-4's brief | Unresolved share per drop falls from 15% |
| **S-3** | Two sources for a final where two permitted ones exist; 13 of the last 26 games had one. | ADOPT (procedure) | Share of games at evidence class A or B per drop |
| **S-4** | A deep loss register in CSV (ID, trigger, verdict, registered class). The pattern rule (three reviews of one class) could not be run because verdicts are prose; 30 of the last 51 reviews could not be tallied at all. | ADOPT at the next permitted release (format) | Prompt 6 prints the class tally from the file |
| **S-5** | The chat brief repeats the access rule that mattered: 80 of 451 cited URLs were not permitted for the chat's reader. | ADOPT with G-4's brief | Not-permitted share per drop |

## Priority 6 — housekeeping

| ID | Change | Disposition |
|---|---|---|
| **K-1** | Roll Part 10 over to Part 11 (it is 1.53 MB against the 1.5 MB trigger). | ADOPT on request (prompt 5) |
| **K-2** | Fix prompt 6's opening line, which still says "this 21-game batch". | ADOPT at the next permitted release (editorial) |
| **K-3** | Rebuild the CURRENT_STATE scoreboard from `ml card-history`; it still leads with imports of 13 and 14 October. | ADOPT with G-3 |
| **K-4** | Mirror: pull the OneDrive checkout so it matches `main`. | Owner action |

## Rejected or not recommended

- **More chats per game.** Six chats on one game agreed because they read the same pages; it counted one view six times. One chat per game, more games.
- **Recalibrating the stated numbers now.** CARD-TRAIN-v1 shows no gain (+0.0005 [-0.0016, +0.0026]).
- **Promoting any model.** No lane has a frozen game.
- **New controls to police the chats.** The chats ignored AUDIT-v1 because nothing checked them, not because a rule was missing. M-3 makes the checks mechanical at import instead.

## Order of work

1. Owner decides M-1 to M-6 (and L-2 with them). One release, then the freeze holds.
2. Here, before the first cohort game: the two-page chat brief, the block parser, the import's paired table, the capture at settlement (L-1), the review clock (L-4).
3. In parallel, with no effect on cards: S-1, K-1, L-3 in shadow.
4. At 100 games: assess, test H-NODIR to H-PERIOD, then one release with whatever passed, plus G-2, G-3, S-4.

## Rollback

The repairs implemented today are reverted by reverting their commit; no record, grade or forecast depends on them.
