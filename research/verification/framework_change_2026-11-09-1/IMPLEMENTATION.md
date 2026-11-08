# Framework change 2026-11-09-1 — sources that block AI agents (v24.6 / CR-2026.11.09-R1)

**Owner instruction, 9 November 2026:** "if any source is blocking because of this AI filter, go search for alternate sources that provide the necessary information, apply this for all sports and leagues and competitions".

**Class.** PROCEDURE. No card, grade, ID, reference or release changes. The release code closure is untouched: NBA-CYCLE-2 is still current. Versions: method MDS-2026.11.09-v24.6, control CR-2026.11.09-R1, prompts P-2026.11.09-v24.4.

## 1. Rule (SRC-ALT-v1)

Before a source is opened, `python -m ml source-audit --url <url>` reads the site's robots.txt and returns one status for the exact path:

| Status | Meaning | Use |
|---|---|---|
| `ALLOWED` | The rules permit every Anthropic agent token: ClaudeBot, Claude-User, Claude-SearchBot, Claude-Web, anthropic-ai | May be opened |
| `NO_RULES_FILE` | robots.txt returned 404 or 410 | May be opened |
| `BLOCKED_FOR_AI` | At least one token is disallowed for the path, or `Content-Signal: ai-input=no` is declared | Not opened |
| `BLOCKED_FOR_ALL` | The path is disallowed for every agent | Not opened |
| `RULES_UNKNOWN` | 403, 429, 5xx, a timeout or an HTML challenge instead of rules | Not opened: not permission (the owner's standing access rule) |

**How a blocked source is handled.** A blocked or unknown source is never reached another way: no reader proxy (r.jina.ai), cache, mirror of the same pages or changed user agent. The research finds an alternate that publishes the same fields, in this order:
1. the field owner's other official outlets;
2. a reputable statistics site;
3. reputable media.

Each alternate is checked the same way. A site that also shows prices is used with its prices blocked. The substitution is recorded. If no permitted alternate gives a field, it stays `NOT_VERIFIED`, with the attempts recorded.

**Where the rule applies:**
- CORE (standing rules);
- RULES_REFERENCE Part A §5;
- WORKFLOW Part A §2;
- the common operating protocol;
- prompt 1, and prompt 3 (both lineages of a settlement must be permitted sources);
- prompt 7, which re-audits the register at each new season.

Tests: `ml/tests/test_source_audit.py` (13).

## 2. Audit of 9 November 2026

- **The register.** Every URL named in SOURCES.md: 245 URLs. 119 `ALLOWED`, 49 `NO_RULES_FILE`, 45 `BLOCKED_FOR_AI`, 32 `RULES_UNKNOWN` ([register/SOURCE_ACCESS_AUDIT.csv](register/SOURCE_ACCESS_AUDIT.csv)).
- **Candidates.** 130 candidate alternates across every sport and data need: 79 `ALLOWED`, 19 `NO_RULES_FILE`, 14 `BLOCKED_FOR_AI`, 18 `RULES_UNKNOWN` ([candidates/SOURCE_ACCESS_AUDIT.csv](candidates/SOURCE_ACCESS_AUDIT.csv)).
- **The result.** A permitted alternate was found for every data need in the register. The table by sport is in [SOURCES](../../../SOURCES.md) SRC-ALT-v1.

Notable results:

| Area | Blocked or unknown | Permitted instead |
|---|---|---|
| NBA | nba.com and ESPN | Basketball-Reference box scores, CBS Sports and Fox Sports; the NBA's own injury report on official.nba.com |
| NHL | The NHL APIs | nhl.com game centre pages, Hockey-Reference and CBS Sports. These can supply the second lineage that the NHL release gate needs for P-607 |
| KBO | koreabaseball.com and Naver | The field owner's English site (eng.koreabaseball.com) and MyKBOStats |
| Cricket | Cricbuzz, ESPNcricinfo and HowStat | ICC, the home boards and Cricsheet |
| Soccer | LaLiga's site, FotMob, worldfootball.net and FBref | Soccerway, Transfermarkt, Futbol24, the league sites, and Flashscore with its prices blocked |
| Weather | Open-Meteo, the US National Weather Service and the Bureau of Meteorology | MET Norway, Meteostat and the UK Met Office |
| News | Google News, X, BBC, Reuters, the Guardian, ABC and AP | Bing News, DuckDuckGo and Bluesky as pointers; the item itself is opened at a permitted source |

## 3. Consequences recorded

- **P-604 corners.** The 2026-11-07 revision read Futbol24 through r.jina.ai, a route that is now excluded. Futbol24 itself is `ALLOWED`. The next settlement run re-reads the corners there; the grade (evidence C) stands until then.
- **League-day settlement.** `league-day settle` reads ESPN, which is `RULES_UNKNOWN`. Until prompt 8 gives it a permitted lineage (Basketball-Reference plus CBS Sports), NBA league-day games are settled by hand from permitted sources.
- **Correction.** The 8 November note said Basketball-Reference blocks AI crawlers. Its robots rules permit every Anthropic token on box-score and season pages.
