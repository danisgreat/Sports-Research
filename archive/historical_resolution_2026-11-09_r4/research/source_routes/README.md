# Agent-accessible source routes ·9 November 2026

209 explicit competition/scope rows covering all ten named sports and the OTHER_SPORTS onboarding lane, plus venue weather. [COMPETITION_ROUTES.csv](COMPETITION_ROUTES.csv) gives checked exact URLs, alternates, field tests and limits. [SOURCE_ACCESS_AUDIT.csv](SOURCE_ACCESS_AUDIT.csv) contains 486 exact URL checks of five Anthropic and three OpenAI agent tokens. [CAPTURE_TESTS.csv](CAPTURE_TESTS.csv) records actual retrievals, failures, external raw paths and hashes. Access is a dated observation, not a guarantee of future availability, permission for every URL, or proof of accuracy.

## Other-sport onboarding

For an unlisted sport or competition, follow research/prompts/1_sports/OTHER_SPORTS.md: discover and audit its actual federation, competition owner and structured statistics source. No existing major-league sample certifies that scope; unresolved rules/fields remain explicit.

## Admission and use

1. Find the exact competition row; use the sample as a route to its actual event. Re-audit that exact URL with `python -B -m ml source-audit --url <url>` immediately before opening it. Only ALLOWED/NO_RULES_FILE proceeds. Redirects are checked before following. A missing robots file means no rules file found, not a legal licence or evidence that no technical filter exists.
2. Separate access, extraction, coverage and accuracy. An index proves a route, never a final score, corner count, confirmed lineup or historical feature. EVENT_SPECIFIC_CHECK_REQUIRED applies even to a tested feed: verify target identity, endpoint, date/zone and completion status.
3. Prefer field-owner structured boxes, official PDF gamebooks and public feeds; prove score by periods/innings/sets. Cross-check disputed fields with a genuinely independent collector; different domains and a copied feed do not establish independence. Conditional C is a sensitivity stratum, never A/B certification.
4. Preserve publication, known-at, capture/retrieval and snapshot times separately. If publication/final clock is unknown, disclose an observed-final upper bound; never backdate it to forecast time. Preserve exact raw captures outside the repo; commit sporting-only extracts, path/hash and source lineage.
5. If a permitted raw page returns403 but an ordinary supported renderer returns the same public page, record both. No user-agent spoofing, proxy, cached mirror, CAPTCHA workaround or bypass. RULES_UNKNOWN403 for robots is refusal, not that renderer case. Never use a search snippet alone for a grade.
6. Keep odds, tips, model estimates and predictions out of the research inputs. Read structured sporting statistics separately on mixed pages. If all permitted alternatives fail, mark the specific field UNAVAILABLE/NOT_VERIFIED, with attempts, rather than treating extraction failure as absence.

## Working examples and limits

NBA: official statsdmz PDF + period sums; Fox standings is a permitted fallback with **rounded PPG totals proxy**, explicitly labelled (max rounding .05 per team per game), never exact scored/conceded totals. NBA injury report is a separate field-owner route. WNBA is not certified from NBA samples.

NBL: official match page and club schedule fetched for Melbourne–Illawarra18October; blocked schedule host avoided. EuroLeague: actual official XML result feed fetched, with `played` flag. EuroCup and domestic FIBA competitions require their own metadata; a public LiveStats example is not all-league coverage.

AHL: actual HockeyTech game-summary feed verified1–4 and period totals. NHL public HTML was a shell; an actual DK Pittsburgh box supplied P607 corroboration. Smaller hockey leagues have their own explicit rows; no NHLproxy assertion.

MLB: official native849817 feed identifies Game5,3–1, distinct from Game4 native849816,7–3. KBO: official English date query failed to select the requested Octoberdate; MyKBO game/innings supplied the result, with same-provider limit. NPB: official season-stat table works; match boxes still need event checks.

Soccer: official LFF final/goal times, Footlive FT/secondhalf derivation, Promedios corner table and ScoreMondo exact statistics were tested. Minor-competition scoreboards do not imply corners or XIs. Old LigaPremier-FMF affiliate route is retired. Tennis: ATP archive is blocked even though its root is allowed; two permitted set-score pages were tested instead.

AFL season table, NRL draw, WorldRugby tournaments, NFL scores and Cricsheet download index were fetched. They provide starting routes, not a claim that all requested event fields are already verified. Some minor competitions have only a discovery route; the catalogue deliberately retains that gap instead of claiming universal filter-free accurate coverage.
