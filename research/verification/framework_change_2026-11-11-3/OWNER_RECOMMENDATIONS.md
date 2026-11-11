**Verdict:** the checks are now strict and sound, but the framework has never been run on a real game, and as built it would refuse most of your own requests. No card has been issued since 21 October and none under v24.13 or v24.14. I'd add a real-game trial and a short list of fixes before the first v24.14 card, because the freeze makes them costly afterwards.

One correction to my last message: I said the new soccer league numbers were in the chats' kit files. They are not; only cricket and tennis are.

I changed nothing in the repo. I tested each claim below marked "confirmed" by running it.

## What would stop it working in practice

1. **A lane is refused if any fact lacks a publication time (confirmed).** Results pages, standings and roster pages rarely show one. A form-window lane with one `UNKNOWN` publication time was refused outright. That pressures a chat to invent a time. A fact read before the start was public before the start, so the retrieval time is enough.

2. **All five lanes are required (confirmed).** With three accepted lanes, admission failed. There is no reduced mode for a late request, and no slot for a sixth chat.

3. **Nothing can be admitted after the scheduled start, even if play is delayed (confirmed).** Your requests say "can be delayed so continue the process as normal". Here a delay means a new event package, which voids all five returns.

4. **Your own request formats cannot be fully priced (confirmed).**
   - Soccer: the kit has no corners numbers, and every supplied line must be priced, so a soccer game with the corners line cannot be admitted.
   - Cricket: both lines need the simulator, which is barred from supplying a card's probability.
   - Both sports can only be kept as research with no forecast.

5. **The source lists expire on 18 November, 10:31 am AEDT.** After that every evidence row is refused. The refresh rule says a changed file takes a new version number, while the experiment needs 100 games under one unchanged version.

6. **The workload per game is heavy.** By my count: about 20 commands, two pushes, a dozen copy-pastes, a written source-lineage note for every web address, and a second forecast made before the chats report. Past requests often arrived at or after the start.

7. **Chats have no reliable clock.** The timing checks rest on times the chat types. The profile asks for an "actual clock" but does not say to read it from the code sandbox.

## What limits accuracy

8. **Every soccer league except the Premier League is priced on Premier League numbers (confirmed).** For Algeria Ligue 1 the league baseline gives Over 2.5 goals 56.1%; the actual rate in your data is 32.5%.

   | League | Goals per game | Actual Over 2.5 | Baseline used |
   |---|---|---|---|
   | Premier League | 2.92 | 56.5% | 56.1% |
   | Algeria Ligue 1 | 1.87 | 32.5% | 56.1% |
   | Argentina | 2.00 | 32.1% | 56.1% |
   | J1 League | 2.20 | 38.2% | 56.1% |

   The measured rows for 32 leagues already sit unused in the 11 November study folder. A baseline this wrong also makes "card beats baseline" meaningless for those leagues.

9. **For most leagues the starting number still knows nothing about the two teams.** The history packs produce form windows, but nothing turns them into a number.

10. **Research still cannot move a probability.** 13 effect rows, including player absences, pitcher, goalie and weather, are still not estimated. Lineup capture has begun but needs about 200 cards per sport.

11. **Cricket and hockey simulators still fail their checks.**

## What limits measurement

12. **The five-chats-versus-one test needs a pre-research forecast per game, but no prompt tells the agent to make one.** It also needs 100 pairs frozen before the start.
13. **Nothing scores the lanes' facts after the game.** Checking "was the player it called out actually out" needs only 20–30 games and would show which chats and sources to trust.
14. **Your benchmark protocol is unused.** It allows a hand-entered comparison after settlement that never touches a forecast; that is your call.

## Housekeeping

- The repo sits inside OneDrive; I hit a "permission denied" on a git folder, and the new lock files and atomic writes are exposed to sync clashes.
- The v24.13 profile and lane briefs still sit beside the v24.14 ones, and the kit's own header still names v24.13 files.

## What I would add, in order

1. **Run one real game end to end and time it**, before anything else.
2. **Load the measured soccer league rows** into the main table and the kit.
3. **Loosen three intake rules:** accept an unknown publication time when retrieval was before the start; allow a labelled reduced mode; handle a delay as an amendment.
4. **Allow partial pricing**, so unpriceable lines are marked rather than blocking the game.
5. **Separate the weekly source-list refresh from the method version.**
6. **Add a per-lane fact scorecard** at settlement.
7. **Build one team-strength starting number per sport** from each side's recent games, tested on held-out leagues.
8. **Tell chats to read the time from the sandbox.**
9. **Move the repo out of OneDrive.**

Items 2, 3, 4 and 7 change numbers or admission, so the freeze forbids them once the first card is issued.