# Availability procedure fixtures

**Date:** 14 October 2026. **Execution:** manual rule walkthroughs against AVAIL-2026.10.14-v1, CURRENT_RULES §5b, prompt 1 and C20. No real lineup was researched or issued in these fixtures; there is no simulated predictive result.

Each row was assessed against the stated rule, with the expected decision recorded below. PASS means the documentation supports the correct process decision, not that player availability or predictive accuracy was measured.

| ID | Synthetic trigger | Negative case that must fail | Legitimate case that passes / required disposition | Walkthrough |
|---|---|---|---|---|
| AV01 | Both basketball teams have published selections | Operator checks home five only and calls both sides confirmed | Check both sides' exact starting releases, selected reserves and medical/absence updates independently; C20 has the final recheck | PASS |
| AV02 | Season roster available, game roster absent | Season membership is called today's starting five or bench | Retain membership context, complete final-team search, record unresolved starting/bench fields and supported uncertainty | PASS |
| AV03 | Official site is JavaScript-only | Operator labels the field NOT_PUBLISHED after a text-parser failure | Renderer/PDF/original official-team post or next permitted route is attempted; classify access failure separately | PASS |
| AV04 | Obscure Japanese basketball match missing from ESPN | Stop after the English search and reuse NBA injury assumptions | Resolve organizer and both clubs, search local names/date with 欠場/負傷/スタメン and record original evidence/failures | PASS |
| AV05 | Football XI published, substitutes omitted | Full lineup/availability is called complete | Confirm XI separately; inspect full team sheet/bench and medical/discipline routes; report the remaining field | PASS |
| AV06 | Cricket squad known before toss | Squad is called playing XI, likely impact substitute called certain | Keep squad context, recheck exact toss/XI/substitute categories and rules; missing XI retains its true state | PASS |
| AV07 | MLB/NPB starter report and active registration exist | Probable pitcher or active list is used as final batting order/bench | Check exact-game order and selected roster, distinguish announced role from probable label and injuries | PASS |
| AV08 | Hockey projected report names goalie | Morning-skate photograph or projected page becomes confirmation | Find explicit current confirmation or keep a supported goalie mixture; bench/scratches separate | PASS |
| AV09 | No fresh medical report found | Blank injury list is reported as everyone healthy | Complete club/league/absence searches; say disclosure is incomplete and preserve actual reported information | PASS |
| AV10 | Early league team list has a late change | Earlier list wins because it was the first official page | Record latest authoritative correction, check both teams immediately before freeze, re-price affected inputs once | PASS |
| AV11 | Two sites repeat one team post | Two URLs are counted as independent verification | Retain original release, one lineage; conflicting independently collected material is not discarded | PASS |
| AV12 | Team sheet image contains an unclear name | Fill unclear player from the last game's roster | Inspect legible original or another exact-game source; keep the unreadable field NOT_VERIFIED | PASS |
| AV13 | At T−5 league has genuinely not published a side | Operator skips escalation, or fabricates confirmation to avoid the label | Full ladder and release recheck documented; explicit gap with supported mixture or qualitative/NO_FORECAST; retained request | PASS |
| AV14 | User explicitly requires only-confirmed numeric issuance | Issue a numeric card while its required starting field remains absent | Keep research draft, recheck while pregame, honour constraint; no invented issue/automation | PASS |
| AV15 | Lineup becomes available after actual start | Rewrite the original cutoff or call post-start recovery pregame | Keep original status; dated addendum/reforecast with truthful timing and outcome exposure | PASS |
| AV16 | Tennis singles or synthetic toy sport | Demand an artificial bench, or exempt a real obscure team sport | N/A only for a structurally inapplicable field with reason; health/withdrawal search still applies to real tennis | PASS |
| AV17 | All relevant routes fail and no supported scenario weights exist | Invent equal probabilities or four ranked rows | Complete attempt ledger and use qualitative/NO_FORECAST under current rules; request coverage retained | PASS |
| AV18 | Source discovery finds a new organizer link | Prompt 1 edits SOURCES or reads workshop forecasts for assistance | Record route in named mini's evidence appendix; queue source-maintenance task; respect reading/write boundary | PASS |

Structural checks separately verify all ten prompt sections contain the protocol, operative sport-file references exist, current versions agree, archives match pre-edit working bytes, and protected workshop/log artifacts are unchanged. See [verification](VERIFICATION_REPORT.md).
