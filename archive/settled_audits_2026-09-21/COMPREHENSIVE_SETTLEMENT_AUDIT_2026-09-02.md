# Comprehensive settlement, retrospective, queue, source and learning audit — 2026-09-02

Status: **CORRECTIVE CONSOLIDATION — frozen issued forecasts remain unchanged**  
Audit access window: **2026-09-02 Australia/Sydney**  
Queue authority: top controlling snapshot of `PREDICTION_LOG_COMBINED.md`; historical component snapshots were used only for reconciliation.  
Probability/value state: **NOT_GENERATED / NOT PUBLISHED; NO VALUE DETERMINABLE**.

## 1. Executive settlement summary

- Canonical coverage is P-001 through P-238. No event remains live. P-192 was cancelled before first pitch and had no actionable V01.
- P-216 is now officially final and fully settled: Zimbabwe 195/6, 64/1 after six; P-162 is closed by an official ITF draw result.
- P-217 is final but not fully settleable: C01/C02 depend on the unnamed operator's reduced-overs/DLS/action rule. Directional endpoints are known, but formal grades remain UNRESOLVED.
- The current audit cohort P-215–P-238 contains 99 ranked rows: **42 definite WIN, 40 definite LOSS, 10 PROVISIONAL WIN, 5 PROVISIONAL LOSS, 2 UNRESOLVED**. Rank #1 is **11 definite WIN, 9 definite LOSS, 2 provisional WIN, 1 provisional LOSS, 1 unresolved**. Winner aliases are **15 definite WIN, 6 definite LOSS, 1 provisional WIN, 2 provisional LOSS**.
- By sport: basketball 2-2; cricket 9-9-2 unresolved; tennis 4-4; baseball 27-25; Chinese FA Cup soccer 10 provisional wins / 5 provisional losses.
- By market: basketball spreads 1-1 and totals 1-1; cricket innings totals 4-4-2 unresolved and phase totals 5-5; tennis handicaps 2-2 and totals 2-2; baseball sides 14-12 and totals 13-13; provisional soccer team totals 3-0, first-half goals 2-1, match totals 2-1, BTTS 0-3, corners 3-0.
- P-215/P-216 and the supplied P-217–P-238 artifact are performance-ineligible late imports. The latter first became locally demonstrable at 2026-09-02 08:55:54 Australia/Sydney (pre-edit SHA-256 `4F51DBF1036E3BF0685ED4BA71538A99DE5B115E195E50961ED5649A020D8DF5`), after the covered events.
- The earlier running-log draft is superseded where it called P-218–P-238 all fully settled, transposed P-217 contract IDs, named P-225's opponent Zhizhen Zhang, and described single-batch learnings as promoted.

## 2. Complete chronological master status list

| ID | Event | Current canonical status |
|---|---|---|
| P-001 | Welsh Fire Women v Trent Rockets Women, The Hundred Women's 11th Match (carried over from legacy V6-022) | FINAL / SETTLED |
| P-002 | Philadelphia Phillies @ Miami Marlins (MLB regular season) | FINAL / SETTLED |
| P-003 | FC København v Polissya Zhytomyr (UEFA Conference League, Q2, 2nd leg) | FINAL / CLOSED — one corners row terminal UNSETTLEABLE |
| P-004 | MI London (Men) v London Spirit (Men), The Hundred Men's Competition 2026 | FINAL / SETTLED |
| P-005 | Texas Rangers @ Tampa Bay Rays (MLB regular season) | FINAL / SETTLED |
| P-006 | Southern Brave (Men) v Birmingham Phoenix (Men), The Hundred Men's Competition 2026 | FINAL / SETTLED |
| P-007 | Manchester Super Giants (Men) v Trent Rockets (Men), The Hundred Men's Competition 2026 | FINAL / SETTLED |
| P-008 | New York Yankees @ Chicago Cubs, MLB regular season | FINAL / SETTLED |
| P-009 | Indiana Fever @ Portland Fire, WNBA regular season — FORECAST | FINAL / SETTLED |
| P-010 | Carlton v Brisbane Lions, AFL Round 21 — FORECAST (locked 2026-08-01T08:56:26Z / 18:56:26 AEST) | FINAL / SETTLED |
| P-011 | Arizona Diamondbacks @ Cleveland Guardians — PREGAME CARD | FINAL / SETTLED |
| P-012 | Welsh Fire Women v Southern Brave Women, The Hundred Women's Competition 2026, Match 19 | FINAL / SETTLED |
| P-013 | Welsh Fire Men v Southern Brave Men, The Hundred Men's Competition 2026, Match 19 | FINAL / SETTLED |
| P-014 | San Diego Padres (Michael King) at Arizona Diamondbacks (Brandon Pfaadt) | FINAL / SETTLED |
| P-015 | Sri Lanka Women vs Pakistan Women, 3rd T20I | FINAL / SETTLED |
| P-016 | Kiwoom Heroes at Lotte Giants, KBO regular season | FINAL / SETTLED |
| P-017 | Sunrisers Leeds Women v London Spirit Women, The Hundred 2026 | FINAL / SETTLED |
| P-018 | Sunrisers Leeds Men vs London Spirit Men, The Hundred 2026 Match 20 (2026-08-04) | FINAL / SETTLED |
| P-019 | Manchester Super Giants Women v Welsh Fire Women, The Hundred Women's Competition 2026, Match 21 | FINAL / SETTLED |
| P-020 | Trent Rockets Women v Birmingham Phoenix Women, The Hundred Women's Competition 2026, Match 22 | FINAL / SETTLED |
| P-021 | Los Angeles Angels (Reid Detmers) at Baltimore Orioles (Trevor Rogers), MLB | FINAL / CLOSED — no forecast issued |
| P-022 | Los Angeles Angels (Ryan Johnson) at Baltimore Orioles (Brandon Young), MLB | FINAL / SETTLED |
| P-023 | Benfica v Heart of Midlothian, UEFA Europa League qualifying | FINAL / SETTLED |
| P-024 | Toronto Tempo @ Portland Fire, WNBA regular season - LIVE FORECAST (appended 2026-08-07 AEST) | FINAL / SETTLED |
| P-025 | Brisbane Lions v Hawthorn, AFL Round 22 - LIVE FORECAST (appended 2026-08-07 AEST) | FINAL / SETTLED |
| P-026 | Birmingham Phoenix Women v Sunrisers Leeds Women, The Hundred 2026 - START-CROSSED/PRE-DELIVERY FORECAST (appended 2026-08-08 AEST) | FINAL / SETTLED |
| P-027 | Melbourne v Fremantle, AFL Round 22 - LIVE FORECAST (appended 2026-08-08 AEST) | FINAL / SETTLED |
| P-028 | West Coast v Collingwood, AFL Round 22 - LIVE FORECAST (appended 2026-08-09 AEST) | FINAL / SETTLED |
| P-029 | St Kilda v Carlton, AFL Round 22 - PREGAME FORECAST (appended 2026-08-09 AEST) | FINAL / SETTLED |
| P-030 | Sunrisers Leeds Women v Welsh Fire Women, The Hundred 2026 Match 27 - PREGAME FORECAST (appended 2026-08-09 AEST) | FINAL / SETTLED |
| P-031 | Manchester City v Atletico Madrid, 2026 Coupang Play Series - LIVE FORECAST (appended 2026-08-09 AEST) | FINAL / SETTLED |
| P-032 | London Spirit Women v Birmingham Phoenix Women, The Hundred 2026 Match 28 - START-CROSSED/PRE-DELIVERY FORECAST (appended 2026-08-09 AEST) | FINAL / SETTLED |
| P-033 | Cincinnati Reds at Washington Nationals - PREGAME FORECAST (appended 2026-08-10 AEST) | FINAL / SETTLED |
| P-034 | Baltimore Orioles at Minnesota Twins - PREGAME FORECAST (appended 2026-08-11 AEST) | FINAL / SETTLED |
| P-035 | Atlanta Dream @ Connecticut Sun, WNBA regular season - LIVE FORECAST | FINAL / SETTLED |
| P-036 | Philadelphia Phillies at Minnesota Twins — MLB Field of Dreams | FINAL / SETTLED |
| P-037 | Jamaica Kingsmen vs Guyana Amazon Warriors — CPL | FINAL / SETTLED |
| P-038 | Australia vs Bangladesh — 1st Test | FINAL / SETTLED |
| P-039 | Manly-Warringah Sea Eagles vs Dolphins — NRL | FINAL / SETTLED |
| P-040 | Fremantle vs Adelaide Crows — AFL | FINAL / SETTLED |
| P-041 | Wolverhampton Wanderers v Blackburn Rovers, EFL Championship Round 1 — PREGAME FORECAST (appended 2026-08-15T02:07:19+10:00) | FINAL / SETTLED |
| P-042 | Manchester Super Giants Men v Sunrisers Leeds Men, The Hundred Eliminator — LIVE FORECAST (appended 2026-08-15T03:01:20+10:00) | FINAL / SETTLED |
| P-043 | St. Louis Cardinals at Chicago Cubs, MLB — PREGAME FORECAST (appended 2026-08-15T04:16:53+10:00) | FINAL / SETTLED |
| P-044 | Richmond v Collingwood, AFLW — PREGAME FORECAST (appended 2026-08-15T16:58:00+10:00) | FINAL / SETTLED |
| P-045 | Hawthorn v Collingwood, AFL — PREGAME FORECAST (appended 2026-08-15T19:35:00+10:00) | FINAL / SETTLED |
| P-046 | Chelsea v Real Sociedad, soccer — PREGAME FORECAST (appended 2026-08-15T22:49:00+10:00) | FINAL / SETTLED |
| P-047 | Bayern Munich v RB Leipzig, soccer — PREGAME FORECAST (appended 2026-08-15T22:59:00+10:00) | FINAL / SETTLED |
| P-048 | Essendon v Sydney Swans, AFL Round 23 — ZERO-SCORE LIVE-START FORECAST | FINAL / SETTLED |
| P-049 | Doosan Bears at KIA Tigers, KBO regular season — PREGAME FORECAST | FINAL / SETTLED |
| P-050 | Trent Rockets Women v Sunrisers Leeds Women, The Hundred 2026 Final — LIVE ORIGINAL-LINE ASSESSMENT | FINAL / SETTLED |
| P-051 | FC Basel v FC Barcelona, senior men's club friendly — PREGAME FORECAST | FINAL / SETTLED |
| P-052 | Athletics at Kansas City Royals, MLB regular season — PREGAME FORECAST | FINAL / SETTLED |
| P-053 | Yomiuri Giants at Yokohama DeNA BayStars, NPB Central League — PREGAME FORECAST | FINAL / SETTLED |
| P-054 | Kiwoom Heroes at Lotte Giants, KBO — PREGAME FORECAST | FINAL / SETTLED |
| P-055 | Detroit Tigers at Pittsburgh Pirates, MLB — PREGAME FORECAST | FINAL / SETTLED |
| P-056 | Arizona Diamondbacks at Boston Red Sox, MLB — PREGAME FORECAST | FINAL / SETTLED |
| P-057 | Minnesota Lynx @ Golden State Valkyries, WNBA — LATE ADMINISTRATIVE IMPORT OF ISSUED CHAT FORECAST | FINAL / SETTLED |
| P-058 | St Kilda v Gold Coast SUNS, AFL Round 24 — ZERO-SCORE WARMUP / ORIGINAL-LINE FORECAST | FINAL / SETTLED |
| P-059 | St. Louis Cardinals (Michael McGreevy) at Cincinnati Reds (Brady Singer), MLB — ZERO-SCORE WARMUP / ORIGINAL-LINE FORECAST | FINAL / SETTLED |
| P-060 | New York Yankees (Gerrit Cole) at Baltimore Orioles (Kyle Bradish), MLB — INCLEMENT-WEATHER START DELAY / ORIGINAL-LINE FORECAST | FINAL / SETTLED |
| P-061 | Hokkaido Nippon-Ham Fighters at Chiba Lotte Marines | FINAL / SETTLED |
| P-062 | West Coast Eagles v Hawthorn (late import) | FINAL / SETTLED |
| P-063 | Newcastle United v Liverpool (late import) | FINAL / SETTLED |
| P-064 | Texas Rangers (Kumar Rocker) at Chicago White Sox (José Urquidy), MLB — PRE-FIRST-PITCH FORECAST | FINAL / SETTLED |
| P-065 | Golden State Valkyries at Minnesota Lynx, WNBA regular season — PRE-TIP FORECAST | FINAL / SETTLED |
| P-066 | Atlanta Dream at Los Angeles Sparks, WNBA regular season — PRE-TIP FORECAST | FINAL / SETTLED |
| P-067 | Doosan Bears at KT Wiz, KBO regular season — PRE-FIRST-PITCH FORECAST | FINAL / SETTLED |
| P-068 | Hanwha Eagles at SSG Landers, KBO regular season — PRE-FIRST-PITCH FORECAST | FINAL / SETTLED |
| P-069 | Lotte Giants at KIA Tigers, KBO regular season — PRE-FIRST-PITCH FORECAST | FINAL / SETTLED |
| P-070 | Central Ballester Reserves vs El Porvenir Reserves — START PASSED / LIVE STATE NOT VERIFIED | FINAL / SETTLED |
| P-071 | Alejandro Juan Mano vs Alejandro Turriziani Alvarez, ITF M25 Oviedo — DELAYED / NOT STARTED FORECAST | FINAL / SETTLED |
| P-072 | Jelle Sels vs Stijn Paardekooper — DELAYED / NOT STARTED FORECAST | FINAL / SETTLED |
| P-073 | Tobol Kostanay vs Kaisar Kyzylorda — PREGAME FORECAST | FINAL / SETTLED |
| P-074 | Maccabi Herzliya U19 vs Hapoel Rishon LeZion U19 — PREGAME FORECAST | FINAL / SETTLED |
| P-075 | OKS vs Middelfart — PREGAME FORECAST | FINAL / SETTLED |
| P-076 | FK Horní Ředice vs FK Dukla Praha — PREGAME FORECAST | FINAL / SETTLED |
| P-077 | Vincent Weaver vs Aryan Jit Singh — PREGAME FORECAST | FINAL / SETTLED |
| P-078 | SK Brann (W) vs FK Austria Wien (W) — PREGAME FORECAST | FINAL / SETTLED |
| P-079 | Abha vs Al Khaleej Saihat — PREGAME | FINAL / SETTLED |
| P-080 | Al Taawoun Buraidah vs Al Fayha — PREGAME | FINAL / SETTLED |
| P-081 | Independiente del Valle vs Deportes Tolima — PREGAME | FINAL / SETTLED |
| P-082 | CF Monterrey vs Chicago Fire FC — PREGAME | FINAL / SETTLED |
| P-083 | Cleveland Guardians at Los Angeles Angels, MLB regular season — PREGAME FORECAST | FINAL / SETTLED |
| P-084 | Washington Mystics at Phoenix Mercury, WNBA regular season — PREGAME FORECAST | FINAL / SETTLED |
| P-085 | Lobos Puebla vs Fuerza Regia, LNBP regular season — LIVE START-CROSSING FORECAST | FINAL / SETTLED |
| P-086 | Club León vs Real Salt Lake — Leagues Cup quarterfinal — START PASSED / LIVE STATE NOT VERIFIED | FINAL / SETTLED |
| P-087 | India vs Sri Lanka, 2nd Test, Day 4 — PRE-START DAY-4 LIVE-STATE RESEARCH CARD | FINAL / SETTLED |
| P-088 | Howlers Sporting Singtam vs Sikkim Boys Football Club — SFA A Division S-League — PREGAME FORECAST | FINAL / SETTLED |
| P-089 | Hanshin Tigers @ Chunichi Dragons — PREGAME | FINAL / SETTLED |
| P-090 | Hokkaido Nippon-Ham Fighters @ Saitama Seibu Lions — PREGAME | FINAL / SETTLED |
| P-091 | Tohoku Rakuten Golden Eagles @ Orix Buffaloes — PREGAME | FINAL / SETTLED |
| P-092 | Doosan Bears @ KT Wiz — PREGAME | FINAL / SETTLED |
| P-093 | NC Dinos @ LG Twins, KBO regular season — PREGAME FORECAST | FINAL / SETTLED |
| P-094 | Yorkshire Women vs Surrey Women, Metro Bank One Day Cup Women — TOSS COMPLETE / PRE-FIRST-BALL FORECAST | FINAL / SETTLED |
| P-095 | TSG Hawks @ Fubon Guardians, CPBL regular season — PREGAME FORECAST | FINAL / SETTLED |
| P-096 | Rakuten Monkeys @ CTBC Brothers, CPBL regular season — PREGAME FORECAST | FINAL / SETTLED |
| P-097 | Wei-Chuan Dragons @ Uni-President 7-ELEVEn Lions, CPBL regular season — PREGAME FORECAST | FINAL / SETTLED |
| P-098 | Vietnam vs Thailand, ASEAN Hyundai Cup 2026 Final Leg 2 — PRE-KICKOFF-DATA VIEW | FINAL / SETTLED |
| P-099 | Rotterdam Dockers vs Amsterdam Flames, European T20 Premier League 2026 — TOSS COMPLETE / PRE-FIRST-BALL VIEW | FINAL / SETTLED |
| P-100 | Apollon Limassol Women vs FH Hafnarfjordur Women, UEFA Women's Europa Cup 2026/27 — PREGAME FORECAST | FINAL / SETTLED |
| P-101 | Germany Women vs Türkiye Women, international friendly — PREGAME FORECAST | FINAL / SETTLED |
| P-102 | VfL Wolfsburg Women vs Inter Women, UEFA Women's Champions League 2026/27 — PREGAME FORECAST | FINAL / SETTLED |
| P-103 | Tampa Bay Rays at Detroit Tigers | FINAL / SETTLED |
| P-104 | Ajax Women vs Real Madrid Women — UEFA Women's Champions League third qualifying round, first leg — PREGAME | FINAL / SETTLED |
| P-105 | Al Ahli Saudi FC vs Auckland FC — FIFA Intercontinental Cup 2026, African-Asian-Pacific Cup Playoff — PREGAME | FINAL / SETTLED |
| P-106 | Newcastle United vs West Bromwich Albion — Carabao Cup Second Round — PREGAME | FINAL / SETTLED |
| P-107 | Bradford City vs Burnley — Carabao Cup Round 2 — PREGAME | FINAL / SETTLED |
| P-108 | Tottenham Hotspur vs Charlton Athletic — Carabao Cup Round 2 — PREGAME | FINAL / SETTLED |
| P-109 | Chicago Cubs @ Arizona Diamondbacks — MLB regular season — PREGAME | FINAL / SETTLED |
| P-110 | Kei Nishikori vs Michael Antonius — US Open Men's Qualifying Q2 — DELAYED / NOT STARTED | FINAL / SETTLED |
| P-111 | Boston Red Sox @ Miami Marlins — MLB regular season — PREGAME | FINAL / SETTLED |
| P-112 | Minnesota Twins @ Athletics — MLB regular season — PREGAME | FINAL / SETTLED |
| P-113 | Club América vs Columbus Crew — Leagues Cup 2026 Quarterfinal | FINAL / SETTLED |
| P-114 | India vs Sri Lanka, 2nd Test, Day 5 — PRE-DAY-5 LIVE-STATE FORECAST | FINAL / SETTLED |
| P-115 | Belfast Wolves vs Dublin Guardians, European T20 Premier League 2026 — START-CROSSED / NOT STARTED | FINAL / SETTLED |
| P-116 | Brisbane Broncos vs Melbourne Storm — PREGAME | FINAL / SETTLED |
| P-117 | ISI Dangkor Senchey FC vs Life FC Sihanoukville — PREGAME | FINAL / SETTLED |
| P-118 | Sandro Kopp vs Martin Krumich — PREGAME | FINAL / SETTLED |
| P-119 | Noah Karma vs Alessandro Hunziker — PREGAME | FINAL / SETTLED |
| P-120 | Guinea vs South Sudan — PREGAME | FINAL / SETTLED |
| P-121 | Sardarapat FC vs FC Syunik — Armenian Cup | FINAL / SETTLED |
| P-122 | Bahrain vs Oman — PREGAME | FINAL / SETTLED |
| P-123 | BuxDU vs Metallurg Bekabad — SCHEDULE-CONFLICT / NO VERIFIED LIVE SCORE | FINAL / SETTLED |
| P-124 | Chase Ferguson vs Fumin Jiang — M15 Maanshan 8 Quarterfinal | FINAL / SETTLED |
| P-125 | Canberra Brave vs Sydney Bears — 2026 AIHL Goodall Cup Preliminary Final | FINAL / SETTLED |
| P-126 | Sikkim Aakraman FC vs Sikkim Boys Club — SFA A Division S-League | FINAL-FOLLOW-UP / UNRESOLVED-CONFLICTED — field-owner result/phase and C06 corners |
| P-127 | Iran vs New Zealand — FIBA Basketball World Cup 2027 Asian Qualifiers | FINAL / SETTLED |
| P-128 | Auckland vs Bay of Plenty — Hilux NPC Round 5 | FINAL / SETTLED |
| P-129 | Manly Warringah Sea Eagles vs St George Illawarra Dragons — NRL Round 26 | FINAL / SETTLED |
| P-130 | Beitar Haifa Yakov vs Hapoel Bnei Arrara Ara — Israel State Cup 2026/27 | FINAL / SETTLED |
| P-131 | Penrith Panthers vs Canterbury-Bankstown Bulldogs — NRL Round 26 | FINAL / SETTLED |
| P-132 | RC Vannes Sevens vs LOU Rugby Sevens — In Extenso SuperSevens, Pau | FINAL / SETTLED |
| P-133 | Arthur Géa vs Nishesh Basavareddy — US Open 2026 Men's Qualifying Final | FINAL / SETTLED |
| P-134 | Cape Verde vs Guinea — FIBA Basketball World Cup 2027 African Qualifiers | FINAL / SETTLED |
| P-135 | Unión de Santa Fe vs Sarmiento — Torneo Clausura 2026 | FINAL / SETTLED |
| P-136 | James Duckworth vs Arthur Fery — ATP Winston-Salem Open 2026 Semifinal | FINAL / SETTLED |
| P-137 | Los Angeles Dodgers (Tarik Skubal) @ Detroit Tigers (Drew Anderson) — MLB | FINAL / SETTLED |
| P-138 | Miami Marlins (Eury Pérez) @ Washington Nationals (Jackson Kent) — MLB | FINAL / SETTLED |
| P-139 | Falcons @ Dolphins preseason | FINAL / SETTLED |
| P-140 | Astros @ Mets | FINAL / SETTLED |
| P-141 | Red Sox @ Yankees | FINAL / SETTLED |
| P-142 | Rockies @ Braves | FINAL / SETTLED |
| P-143 | Giants @ Jets preseason | FINAL / SETTLED |
| P-144 | Buccaneers @ Jaguars preseason | FINAL / SETTLED |
| P-145 | Rangers @ Brewers | FINAL / SETTLED |
| P-146 | Sun @ Fever | FINAL / SETTLED |
| P-147 | Gotham v Portland | FINAL / SETTLED |
| P-148 | Toluca Femenil v León Femenil | FINAL / PARTIAL — C02 corners PROVISIONAL LOSS |
| P-149 | Colorado Rapids 2 v Ventura County | FINAL / PARTIAL — C02 corners PROVISIONAL WIN |
| P-150 | Montreal @ Winnipeg, CFL | FINAL / SETTLED |
| P-151 | Boca Juniors v Lanús | FINAL / PARTIAL — C02 corners STRONG PROVISIONAL WIN |
| P-152 | Atlante v León | FINAL / SETTLED |
| P-153 | Necaxa v Cruz Azul | FINAL / SETTLED |
| P-154 | Vikings @ Broncos preseason | FINAL / SETTLED |
| P-155 | Phillies @ Angels | FINAL / SETTLED |
| P-156 | Orioles @ Athletics | FINAL / SETTLED |
| P-157 | Sacramento @ Reno | FINAL / CLOSED — no actionable forecast |
| P-158 | Tempo @ Aces | FINAL / SETTLED |
| P-159 | Mystics @ Sparks | FINAL / SETTLED |
| P-160 | Diamondbacks @ Giants | FINAL / SETTLED |
| P-161 | Sultanes @ Toros | FINAL / SETTLED |
| P-162 | Te v Ferguson | FINAL / SETTLED — ITF field-owner confirmation recovered |
| P-163 | Adelaide v West Coast AFLW | FINAL / SETTLED |
| P-164 | Lotte @ Nippon-Ham, live | FINAL / SETTLED |
| P-165 | Tohoku Rakuten Golden Eagles @ Saitama Seibu Lions — NPB Pacific League | FINAL / SETTLED |
| P-166 | Melbourne Mustangs vs Canberra Brave — AIHL Goodall Cup Semifinal | FINAL / RESEARCH SETTLED — operator OT/action terms unresolved |
| P-167 | Kiwoom Heroes @ Doosan Bears — KBO | FINAL / SETTLED |
| P-168 | LG Twins @ Lotte Giants — KBO | FINAL / SETTLED |
| P-169 | Melbourne vs Carlton — AFL Wildcard Final | FINAL / SETTLED |
| P-170 | North Queensland Cowboys vs Wests Tigers — NRL | FINAL / SETTLED |
| P-171 | Glasgow Cosmic vs Dublin Guardians — European T20 Premier League | FINAL / SETTLED |
| P-172 | Liverpool vs Nottingham Forest — English Premier League | FINAL / SETTLED |
| P-173 | Chengdu Rongcheng vs Liaoning Tieren (Ironman) — Chinese Super League | FINAL / SETTLED |
| P-174 | Henan vs Chongqing Tonglianglong — Chinese Super League | FINAL / SETTLED |
| P-175 | South Africa vs Zimbabwe — Namibia T20I Tri-Series | FINAL / SETTLED |
| P-176 | Amiens SC vs FC Versailles — France Ligue 3 | FINAL / PARTIAL — C05 corners PROVISIONAL WIN |
| P-177 | SC Aubagne Air Bel vs Bourg-en-Bresse Péronnas — France Ligue 3 | FINAL / SETTLED |
| P-178 | AS Cannes vs Le Puy-en-Velay — France Ligue 3 | FINAL / PARTIAL — C05 corners UNRESOLVED |
| P-179 | Thionville Lusitanos vs Paris 13 Atletico — France Ligue 3 | FINAL / PARTIAL — C05 corners PROVISIONAL WIN |
| P-180 | 1. FC Köln vs TSG Hoffenheim — Germany Bundesliga | FINAL / SETTLED |
| P-181 | Coventry City vs Hull City — English Premier League | FINAL / SETTLED |
| P-182 | Excelsior Rotterdam vs Sparta Rotterdam — Netherlands Eredivisie | FINAL / SETTLED |
| P-183 | Levante UD vs Real Betis — La Liga | FINAL / SETTLED |
| P-184 | North Carolina vs TCU — NCAA Football | FINAL / SETTLED |
| P-185 | Robert Morris @ Wagner — NCAA FCS / NEC | FINAL / SETTLED |
| P-186 | Los Angeles Dodgers @ Detroit Tigers — MLB | FINAL / SETTLED |
| P-187 | Trinbago Knight Riders vs Jamaica Kingsmen — Republic Bank CPL 2026 | FINAL / SETTLED |
| P-188 | Boston Red Sox @ New York Yankees — MLB | FINAL / SETTLED |
| P-189 | Alabama A&M Bulldogs vs Howard Bison — Cricket MEAC/SWAC Challenge | FINAL / SETTLED |
| P-190 | New Zealand Warriors (W) vs St George Illawarra Dragons (W) — NRLW Round 9 | FINAL / SETTLED |
| P-191 | Walyalup (Fremantle W) vs Carlton W — AFLW Round 3 | FINAL / SETTLED |
| P-192 | SSG Landers @ KIA Tigers — KBO | CANCELLED BEFORE FIRST PITCH / CLOSED NO ACTION |
| P-193 | Essendon (W) vs Richmond (W) — AFLW Round 3 | FINAL / SETTLED |
| P-194 | FC St. Pauli vs 1. FC Kaiserslautern — Germany 2. Bundesliga | FINAL / SETTLED |
| P-195 | KAA Gent vs Club Brugge — Belgium First Division A | FINAL / SETTLED |
| P-196 | Egypt vs Congo DR — FIBA Basketball World Cup 2027 African Qualifiers | FINAL / SETTLED |
| P-197 | Feyenoord vs ADO Den Haag — Netherlands Eredivisie | FINAL / SETTLED |
| P-198 | Poland vs Germany — FIBA Basketball World Cup 2027 European Qualifiers | FINAL / SETTLED |
| P-199 | Frederikshavn White Hawks vs Sønderjyske — Danish Metal Ligaen | FINAL / SETTLED |
| P-200 | Herning Blue Fox vs Rungsted Seier Capital — Danish Metal Ligaen | FINAL / RESEARCH SETTLED — operator OT/SO/action terms unresolved |
| P-201 | SC Freiburg vs Werder Bremen — Germany Bundesliga | FINAL / SETTLED |
| P-202 | Randers FC vs AGF Aarhus — Denmark 3F Superliga | FINAL / SETTLED |
| P-203 | RC Deportivo de A Coruña vs Valencia CF — LaLiga | FINAL / SETTLED |
| P-204 | Boston Red Sox @ New York Yankees — MLB | FINAL / SETTLED |
| P-205 | Chicago White Sox @ Minnesota Twins — MLB | FINAL / SETTLED |
| P-206 | Los Angeles Dodgers @ Detroit Tigers — MLB | FINAL / SETTLED |
| P-207 | Cagliari vs Inter Milan — Italy Serie A | FINAL / SETTLED |
| P-208 | Lazio vs Genoa — Italy Serie A | FINAL / SETTLED |
| P-209 | Corinthians vs Santos — Brazil Série A | FINAL / SETTLED |
| P-210 | Flamengo vs Botafogo — Brazil Série A | FINAL / SETTLED |
| P-211 | Jaime Faria vs Jenson Brooksby — US Open Men's Singles R1 | FINAL / SETTLED |
| P-212 | McCartney Kessler vs Ekaterina Alexandrova — US Open Women R1 | FINAL / SETTLED |
| P-213 | Toby Samuel vs Tomas Machac — US Open Men's Singles R1 | FINAL / SETTLED |
| P-214 | Baltimore Orioles @ Athletics — MLB | FINAL / SETTLED |
| P-215 | Japan vs Qatar — FIBA Basketball World Cup 2027 Asian Qualifiers | FINAL / SETTLED |
| P-216 | Namibia vs Zimbabwe — Namibia T20I Tri-Series 2026 | FINAL / SETTLED |
| P-217 | Trinbago Knight Riders vs Guyana Amazon Warriors — Caribbean Premier League 2026 | FINAL / PARTIAL — C01/C02 operator shortening rules unresolved |
| P-218 | Ann Li vs Antonia Ruzic — US Open Women 2026 | FINAL / SETTLED |
| P-219 | New York Mets (Robert Stock) @ Tampa Bay Rays (Ian Seymour) — MLB 2026 | FINAL / SETTLED |
| P-220 | San Diego Padres (Michael King) @ Cincinnati Reds (Brady Singer) — MLB 2026 | FINAL / SETTLED |
| P-221 | Miami Marlins (Ryan Gusto) @ Washington Nationals (Will Dion) — MLB 2026 | FINAL / SETTLED |
| P-222 | Seattle Mariners (George Kirby) @ Boston Red Sox (Payton Tolle) — MLB 2026 | FINAL / SETTLED |
| P-223 | New York Yankees at Los Angeles Angels | FINAL / SETTLED |
| P-224 | Philadelphia Phillies (Aaron Nola) @ Arizona Diamondbacks (Brandon Pfaadt) — MLB 2026 | FINAL / SETTLED |
| P-225 | Chun-Hsin Tseng vs Tianhui Zhang — ATP Challenger Zhangjiagang 2026 | FINAL / SETTLED |
| P-226 | Hanshin Tigers @ Tokyo Yakult Swallows — NPB 2026 | FINAL / SETTLED |
| P-227 | Hiroshima Toyo Carp @ Chunichi Dragons — NPB 2026 | FINAL / SETTLED |
| P-228 | Orix Buffaloes @ Tohoku Rakuten Golden Eagles — NPB 2026 | FINAL / SETTLED |
| P-229 | Hanwha Eagles @ KT Wiz — KBO 2026 | FINAL / SETTLED |
| P-230 | KIA Tigers @ NC Dinos — KBO 2026 | FINAL / SETTLED |
| P-231 | LG Twins @ Doosan Bears — KBO 2026 | FINAL / SETTLED |
| P-232 | Lotte Giants @ Samsung Lions — KBO 2026 | FINAL / SETTLED |
| P-233 | Beijing Guoan vs Lanzhou Longyuan Athletic — China FA Cup 2026 | FINAL / PROVISIONAL — no current CFA/club final recovered |
| P-234 | Dalian Yingbo vs Shanghai Shenhua — China FA Cup 2026 | FINAL / PROVISIONAL — no current CFA/club final recovered |
| P-235 | Shandong Taishan vs Shanghai Port — China FA Cup 2026 | FINAL / PROVISIONAL — no current CFA/club final recovered |
| P-236 | England Women vs Ireland Women — 1st ODI, 2026 | FINAL / SETTLED |
| P-237 | Zimbabwe vs South Africa — Namibia T20I Tri-Series 2026 | FINAL / SETTLED |
| P-238 | Glasgow Cosmic vs Rotterdam Dockers — European T20 Premier League 2026 | FINAL / SETTLED |


## 3. Contract-level settlement table — P-215 through P-238

This table covers every newly or previously remaining ranked row in the active continuation. Administrative IDs added where a card omitted them preserve the frozen candidate order and rank; they do not rewrite the issued forecast. `RR/PR` = result right/process right; `RR/PD` = result right/process different; `RW/PBR` = result wrong/process broadly right; `RW/PW` = result wrong/process wrong.

| Contract ID | Rank | Exact frozen endpoint | Official/retrieved endpoint | Settlement | Four-way verdict | Process grade / defect | Source |
|---|---:|---|---|---|---|---|---|
| P-215-C01 | 3 | Qatar +34.5 | Qatar lost by 53 | LOSS | RW/PW | PROCESS_DEFECT — STATE_FRESHNESS / CALIBRATION | S215 |
| P-215-C02 | 2 | Japan -34.5 | Japan won by 53 | WIN | RR/PR | PROCESS_DEFECT — STATE_FRESHNESS / CALIBRATION | S215 |
| P-215-C03 | 4 | Combined Over 169.5 | 193 points | WIN | RR/PD | PROCESS_DEFECT — STATE_FRESHNESS / CALIBRATION | S215 |
| P-215-C04 | 1 | Combined Under 169.5 | 193 points | LOSS | RW/PW | PROCESS_DEFECT — STATE_FRESHNESS / CALIBRATION | S215 |
| P-216-C01 | 4 | Zimbabwe 20-over Over 165.5 | 195/6 after 20 | WIN | RR/PD | PROCESS_DEFECT — STATE_FRESHNESS / DEPENDENCE_TAIL | S216 |
| P-216-C02 | 1 | Zimbabwe 20-over Under 165.5 | 195/6 after 20 | LOSS | RW/PBR | PROCESS_DEFECT — STATE_FRESHNESS / DEPENDENCE_TAIL | S216 |
| P-216-C03 | 2 | Zimbabwe after 6 Over 47.5 | 64/1 after 6 | WIN | RR/PR | PROCESS_DEFECT — STATE_FRESHNESS / DEPENDENCE_TAIL | S216 |
| P-216-C04 | 3 | Zimbabwe after 6 Under 47.5 | 64/1 after 6 | LOSS | RW/PBR | PROCESS_DEFECT — STATE_FRESHNESS / DEPENDENCE_TAIL | S216 |
| P-217-C01 | 4 | GAW 20-over Over 174.5 | 185/5 in 16 overs | UNRESOLVED — directional WIN | N/A — operator unresolved | INCONCLUSIVE — IDENTITY_CONTRACT / UNKNOWN_DEFINITION | S217 |
| P-217-C02 | 1 | GAW 20-over Under 174.5 | 185/5 in 16 overs | UNRESOLVED — directional LOSS | N/A — operator unresolved | INCONCLUSIVE — IDENTITY_CONTRACT / UNKNOWN_DEFINITION | S217 |
| P-217-C03 | 2 | GAW after 6 Over 46.5 | 31/2 after 6 | LOSS | RW/PBR | PROCESS_DEFECT — DEPENDENCE_TAIL | S217 |
| P-217-C04 | 3 | GAW after 6 Under 46.5 | 31/2 after 6 | WIN | RR/PD | PROCESS_DEFECT — DEPENDENCE_TAIL | S217 |
| P-218-C01 | 4 | Ruzic +4.5 games | Ruzic lost by 7 games | LOSS | RW/PBR | COMPLIANT — RANDOM_REALIZATION | S218 |
| P-218-C02 | 1 | Li -4.5 games | Li won by 7 games | WIN | RR/PR | COMPLIANT — NONE | S218 |
| P-218-C03 | 3 | Over 20.5 games | 19 games | LOSS | RW/PBR | COMPLIANT — RANDOM_REALIZATION | S218 |
| P-218-C04 | 2 | Under 20.5 games | 19 games | WIN | RR/PR | COMPLIANT — NONE | S218 |
| P-219-C01 | 1 | Mets +1.5 | Mets won 3-2 | WIN | RR/PR | COMPLIANT — NONE | S219 |
| P-219-C02 | 3 | Rays -1.5 | Rays lost 2-3 | LOSS | RW/PBR | COMPLIANT — RANDOM_REALIZATION | S219 |
| P-219-C03 | 2 | Over 7.5 | 5 runs | LOSS | RW/PBR | COMPLIANT — RANDOM_REALIZATION | S219 |
| P-219-C04 | 4 | Under 7.5 | 5 runs | WIN | RR/PD | COMPLIANT — RANDOM_REALIZATION | S219 |
| P-220-C01 | 3 | Padres -1.5 | Padres won by 5 | WIN | RR/PD | PROCESS_DEFECT — MATCHUP_CONTEXT / CALIBRATION | S220 |
| P-220-C02 | 1 | Reds +1.5 | Reds lost by 5 | LOSS | RW/PW | PROCESS_DEFECT — MATCHUP_CONTEXT / CALIBRATION | S220 |
| P-220-C03 | 2 | Over 9.0 | 5 runs | LOSS | RW/PW | PROCESS_DEFECT — MATCHUP_CONTEXT / CALIBRATION | S220 |
| P-220-C04 | 4 | Under 9.0 | 5 runs | WIN | RR/PD | PROCESS_DEFECT — MATCHUP_CONTEXT / CALIBRATION | S220 |
| P-221-C01 | 4 | Marlins -1.5 | Marlins lost by 3 | LOSS | RW/PBR | PROCESS_DEFECT — MATCHUP_CONTEXT | S221 |
| P-221-C02 | 1 | Nationals +1.5 | Nationals won 6-3 | WIN | RR/PR | PROCESS_DEFECT — MATCHUP_CONTEXT | S221 |
| P-221-C03 | 2 | Over 8.5 | 9 runs | WIN | RR/PR | PROCESS_DEFECT — MATCHUP_CONTEXT | S221 |
| P-221-C04 | 3 | Under 8.5 | 9 runs | LOSS | RW/PBR | PROCESS_DEFECT — MATCHUP_CONTEXT | S221 |
| P-222-C01 | 1 | Mariners +1.5 | Boston won by 1 in 10 innings | WIN | RR/PR | COMPLIANT — NONE | S222 |
| P-222-C02 | 4 | Red Sox -1.5 | Boston won by 1 | LOSS | RW/PBR | COMPLIANT — RANDOM_REALIZATION | S222 |
| P-222-C03 | 2 | Over 7.5 | 17 runs | WIN | RR/PR | COMPLIANT — NONE | S222 |
| P-222-C04 | 3 | Under 7.5 | 17 runs | LOSS | RW/PBR | COMPLIANT — RANDOM_REALIZATION | S222 |
| P-223-C01 | 2 | Yankees ML | Yankees lost 1-10 | LOSS | RW/PW | PROCESS_DEFECT — MATCHUP_CONTEXT | S223 |
| P-223-C02 | 1 | Angels +1.5 | Angels won 10-1 | WIN | RR/PR | PROCESS_DEFECT — MATCHUP_CONTEXT | S223 |
| P-223-C03 | 4 | Over 8.0 | 11 runs | WIN | RR/PD | PROCESS_DEFECT — MATCHUP_CONTEXT | S223 |
| P-223-C04 | 3 | Under 8.0 | 11 runs | LOSS | RW/PW | PROCESS_DEFECT — MATCHUP_CONTEXT | S223 |
| P-224-C01 | 1 | Phillies +1.5 | Phillies won 2-1 | WIN | RR/PR | COMPLIANT — NONE | S224 |
| P-224-C02 | 2 | Diamondbacks +1.5 | Diamondbacks lost by 1 | WIN | RR/PR | COMPLIANT — NONE | S224 |
| P-224-C03 | 4 | Over 8.5 | 3 runs | LOSS | RW/PBR | COMPLIANT — RANDOM_REALIZATION | S224 |
| P-224-C04 | 3 | Under 8.5 | 3 runs | WIN | RR/PR | COMPLIANT — NONE | S224 |
| P-225-C01 | 3 | Tianhui Zhang +4.5 games | Zhang lost by 8 games | LOSS | RW/PBR | COMPLIANT — settlement identity corrected | S225 |
| P-225-C02 | 2 | Tseng -4.5 games | Tseng won by 8 games | WIN | RR/PR | COMPLIANT — NONE | S225 |
| P-225-C03 | 4 | Over 20.5 games | 16 games | LOSS | RW/PBR | COMPLIANT — RANDOM_REALIZATION | S225 |
| P-225-C04 | 1 | Under 20.5 games | 16 games | WIN | RR/PR | COMPLIANT — NONE | S225 |
| P-226-C01 | 3 | Hanshin -2.5 | Hanshin won by 4 | WIN | RR/PD | PROCESS_DEFECT — RATE_PROCESS / CALIBRATION | S226 |
| P-226-C02 | 2 | Yakult +2.5 | Yakult lost by 4 | LOSS | RW/PW | PROCESS_DEFECT — RATE_PROCESS / CALIBRATION | S226 |
| P-226-C03 | 4 | Over 7.5 | 8 runs | WIN | RR/PD | PROCESS_DEFECT — RATE_PROCESS / CALIBRATION | S226 |
| P-226-C04 | 1 | Under 7.5 | 8 runs | LOSS | RW/PW | PROCESS_DEFECT — RATE_PROCESS / CALIBRATION | S226 |
| P-227-C01 | 1 | Hiroshima +1.5 | Hiroshima won 5-1 | WIN | RR/PR | COMPLIANT — NONE | S227 |
| P-227-C02 | 3 | Chunichi +0.5 | Chunichi lost 1-5 | LOSS | RW/PBR | COMPLIANT — RANDOM_REALIZATION | S227 |
| P-227-C03 | 4 | Over 6.5 | 6 runs | LOSS | RW/PBR | COMPLIANT — RANDOM_REALIZATION | S227 |
| P-227-C04 | 2 | Under 6.5 | 6 runs | WIN | RR/PR | COMPLIANT — NONE | S227 |
| P-228-C01 | 3 | Orix +0.5 | Orix lost 1-5 | LOSS | RW/PBR | PROCESS_DEFECT — MATCHUP_CONTEXT | S228 |
| P-228-C02 | 1 | Rakuten +0.5 | Rakuten won 5-1 | WIN | RR/PR | PROCESS_DEFECT — MATCHUP_CONTEXT | S228 |
| P-228-C03 | 2 | Over 6.5 | 6 runs | LOSS | RW/PW | PROCESS_DEFECT — MATCHUP_CONTEXT | S228 |
| P-228-C04 | 4 | Under 6.5 | 6 runs | WIN | RR/PD | PROCESS_DEFECT — MATCHUP_CONTEXT | S228 |
| P-229-C01 | 1 | Hanwha +1.5 | Hanwha lost by 5 | LOSS | RW/PW | PROCESS_DEFECT — MATCHUP_CONTEXT / CALIBRATION | S229 |
| P-229-C02 | 4 | KT -1.5 | KT won by 5 | WIN | RR/PD | PROCESS_DEFECT — MATCHUP_CONTEXT / CALIBRATION | S229 |
| P-229-C03 | 2 | Over 9.5 | 7 runs | LOSS | RW/PW | PROCESS_DEFECT — MATCHUP_CONTEXT / CALIBRATION | S229 |
| P-229-C04 | 3 | Under 9.5 | 7 runs | WIN | RR/PD | PROCESS_DEFECT — MATCHUP_CONTEXT / CALIBRATION | S229 |
| P-230-C01 | 2 | KIA ML | KIA lost 2-7 | LOSS | RW/PW | PROCESS_DEFECT — MATCHUP_CONTEXT | S230 |
| P-230-C02 | 1 | NC +1.5 | NC won 7-2 | WIN | RR/PR | PROCESS_DEFECT — MATCHUP_CONTEXT | S230 |
| P-230-C03 | 3 | Over 9.5 | 9 runs | LOSS | RW/PBR | PROCESS_DEFECT — MATCHUP_CONTEXT | S230 |
| P-230-C04 | 4 | Under 9.5 | 9 runs | WIN | RR/PD | PROCESS_DEFECT — MATCHUP_CONTEXT | S230 |
| P-231-C01 | 3 | LG +0.5 | LG won 3-1 | WIN | RR/PR | PROCESS_DEFECT — CALIBRATION | S231 |
| P-231-C02 | 1 | Doosan +1.5 | Doosan lost by 2 | LOSS | RW/PW | PROCESS_DEFECT — CALIBRATION | S231 |
| P-231-C03 | 4 | Over 8.5 | 4 runs | LOSS | RW/PBR | PROCESS_DEFECT — CALIBRATION | S231 |
| P-231-C04 | 2 | Under 8.5 | 4 runs | WIN | RR/PR | PROCESS_DEFECT — CALIBRATION | S231 |
| P-232-C01 | 1 | Lotte +1.5 | Lotte lost by 3 | LOSS | RW/PW | PROCESS_DEFECT — RATE_PROCESS / MATCHUP_CONTEXT | S232 |
| P-232-C02 | 3 | Samsung -1.5 | Samsung won by 3 | WIN | RR/PD | PROCESS_DEFECT — RATE_PROCESS / MATCHUP_CONTEXT | S232 |
| P-232-C03 | 4 | Over 10.5 | 3 runs | LOSS | RW/PBR | PROCESS_DEFECT — RATE_PROCESS / MATCHUP_CONTEXT | S232 |
| P-232-C04 | 2 | Under 10.5 | 3 runs | WIN | RR/PR | PROCESS_DEFECT — RATE_PROCESS / MATCHUP_CONTEXT | S232 |
| P-233-C01 | 1 | Beijing team goals Over 1.5 | Beijing scored 3 | PROVISIONAL WIN | RR/PR | PROCESS_DEFECT — MATCHUP_CONTEXT | S233 |
| P-233-C02 | 2 | 1H Over 0.5 goals | HT 1-0 | PROVISIONAL WIN | RR/PR | PROCESS_DEFECT — MATCHUP_CONTEXT | S233 |
| P-233-C03 | 3 | Over 2.5 goals | 4 goals | PROVISIONAL WIN | RR/PR | PROCESS_DEFECT — MATCHUP_CONTEXT | S233 |
| P-233-C04 | 4 | BTTS — No | Final 3-1 | PROVISIONAL LOSS | RW/PW | PROCESS_DEFECT — MATCHUP_CONTEXT | S233 |
| P-233-C05 | 5 | Corners Over 8.5 | 13 reported corners | PROVISIONAL WIN | RR/PR | PROCESS_DEFECT — SOURCE_TRANSFORMATION | S233 |
| P-234-C01 | 1 | 1H Over 0.5 goals | HT 0-0 | PROVISIONAL LOSS | RW/PW | PROCESS_DEFECT — MATCHUP_CONTEXT / CALIBRATION | S234 |
| P-234-C02 | 2 | Dalian team goals Over 0.5 | Dalian scored 1 | PROVISIONAL WIN | RR/PR | PROCESS_DEFECT — MATCHUP_CONTEXT / CALIBRATION | S234 |
| P-234-C03 | 3 | Corners Over 8.5 | 10 reported corners | PROVISIONAL WIN | RR/PR | PROCESS_DEFECT — SOURCE_TRANSFORMATION | S234 |
| P-234-C04 | 4 | BTTS — Yes | Final 1-0 | PROVISIONAL LOSS | RW/PW | PROCESS_DEFECT — MATCHUP_CONTEXT / CALIBRATION | S234 |
| P-234-C05 | 5 | Over 2.5 goals | 1 goal | PROVISIONAL LOSS | RW/PW | PROCESS_DEFECT — MATCHUP_CONTEXT / CALIBRATION | S234 |
| P-235-C01 | 1 | 1H Over 0.5 goals | HT 0-2 | PROVISIONAL WIN | RR/PR | PROCESS_DEFECT — MATCHUP_CONTEXT | S235 |
| P-235-C02 | 2 | Shanghai Port team goals Over 0.5 | Port scored 3 | PROVISIONAL WIN | RR/PR | PROCESS_DEFECT — MATCHUP_CONTEXT | S235 |
| P-235-C03 | 3 | BTTS — Yes | Final 0-3 | PROVISIONAL LOSS | RW/PW | PROCESS_DEFECT — MATCHUP_CONTEXT | S235 |
| P-235-C04 | 4 | Over 2.5 goals | 3 goals | PROVISIONAL WIN | RR/PR | PROCESS_DEFECT — MATCHUP_CONTEXT | S235 |
| P-235-C05 | 5 | Corners Over 8.5 | 14 reported corners | PROVISIONAL WIN | RR/PR | PROCESS_DEFECT — SOURCE_TRANSFORMATION | S235 |
| P-236-C01 | 2 | Ireland innings Over 218.5 | 281/5 after 50 | WIN | RR/PR | PROCESS_DEFECT — CALIBRATION / RATE_PROCESS | S236 |
| P-236-C02 | 3 | Ireland innings Under 218.5 | 281/5 after 50 | LOSS | RW/PBR | PROCESS_DEFECT — CALIBRATION / RATE_PROCESS | S236 |
| P-236-C03 | 4 | Ireland after 5 Over 20.5 | 23/1 after 5 | WIN | RR/PD | PROCESS_DEFECT — CALIBRATION / RATE_PROCESS | S236 |
| P-236-C04 | 1 | Ireland after 5 Under 20.5 | 23/1 after 5 | LOSS | RW/PW | PROCESS_DEFECT — CALIBRATION / RATE_PROCESS | S236 |
| P-237-C01 | 4 | South Africa innings Over 184.5 | 185/7 after 20 | WIN | RR/PD | PROCESS_DEFECT — STATE_FRESHNESS / MATCHUP_CONTEXT | S237 |
| P-237-C02 | 1 | South Africa innings Under 184.5 | 185/7 after 20 | LOSS | RW/PW | PROCESS_DEFECT — STATE_FRESHNESS / MATCHUP_CONTEXT | S237 |
| P-237-C03 | 3 | South Africa after 6 Over 54.5 | 59/0 after 6 | WIN | RR/PD | PROCESS_DEFECT — STATE_FRESHNESS / MATCHUP_CONTEXT | S237 |
| P-237-C04 | 2 | South Africa after 6 Under 54.5 | 59/0 after 6 | LOSS | RW/PW | PROCESS_DEFECT — STATE_FRESHNESS / MATCHUP_CONTEXT | S237 |
| P-238-C01 | 4 | Glasgow innings Over 161.5 | 140/9 after 20 | LOSS | RW/PBR | COMPLIANT — RANDOM_REALIZATION | S238 |
| P-238-C02 | 1 | Glasgow innings Under 161.5 | 140/9 after 20 | WIN | RR/PR | COMPLIANT — NONE | S238 |
| P-238-C03 | 3 | Glasgow after 6 Over 46.5 | 39/2 after 6 | LOSS | RW/PBR | COMPLIANT — RANDOM_REALIZATION | S238 |
| P-238-C04 | 2 | Glasgow after 6 Under 46.5 | 39/2 after 6 | WIN | RR/PR | COMPLIANT — NONE | S238 |

### Queue-row contract corrections outside P-215–P-238

These rows changed status in this audit and are not added to the 99-row continuation count.

| Contract ID | Rank | Exact frozen endpoint | Official/retrieved endpoint | Settlement | Four-way verdict | Process grade / defect | Source |
|---|---:|---|---|---|---|---|---|
| P-148-C02 | 2 | Toluca team corners Over 4.5 | Specialist reports Toluca 2 (match corners 2-6) | PROVISIONAL LOSS | RW/PBR | PROCESS_DEFECT — MATCHUP_CONTEXT / CALIBRATION | Q148 |
| P-162-C01 | 1 | Rigele Te -2.5 games | Te won 6-1, 6-4; +7 game margin | WIN | RR/PR | COMPLIANT — NONE | Q162 |
| P-162-C02 | 3 | Chase Ferguson +2.5 games | Ferguson lost by 7 games | LOSS | RW/PBR | COMPLIANT — RANDOM_REALIZATION | Q162 |
| P-162-C03 | 4 | Over 22.5 games | 17 games | LOSS | RW/PBR | COMPLIANT — RANDOM_REALIZATION | Q162 |
| P-162-C04 | 2 | Under 22.5 games | 17 games | WIN | RR/PR | COMPLIANT — NONE | Q162 |
| P-176-C05 | 5 | Total match corners Under 10.5 | Timeline records Amiens 5, Versailles 3; 8 total | PROVISIONAL WIN | RR/PD | PROCESS_DEFECT — MATCHUP_CONTEXT | Q176 |

### Contract-level settlement controls

Each row below applies to every contract ID in its stated range. Direct result/source access occurred during the **2026-09-02 Australia/Sydney audit session**. Exact per-page wall-clock minutes were not captured, are immaterial to already-final endpoints, and are not invented.

| Contract IDs | State/source check | Operator-rule dependency | Threshold/provider invariance |
|---|---|---|---|
| P-215-C01–C04 | FINAL; S215 official FIBA | None outcome-changing for the completed score endpoints | Yes; half-point lines |
| P-216-C01–C04 | FINAL; S216 ICC final plus separate six-over scorecard field | No DLS/shortening realised; operator does not alter completed run endpoints | Yes; half-point lines |
| P-217-C01/C02 | FINAL event; S217 confirms 185/5 in 16 | **Material and missing**: actual reduced-overs/DLS/action/void rule | **No formal invariance** across possible operator rules; remain UNRESOLVED |
| P-217-C03/C04 | FINAL phase; S217 confirms 31/2 after six completed overs | No uncompleted-phase issue | Yes; half-point line and phase completed |
| P-218-C01–C04 | FINAL; S218 official USTA | No retirement/walkover occurred | Yes; normal-completion half-point lines |
| P-219-C01–C04 | FINAL; S219 official MLB | No extra inning or listed-pitcher condition affected the completed endpoints | Yes; half-point lines |
| P-220-C01–C04 | FINAL; S220 official MLB | No extra inning affected the endpoints; total price/action unavailable but not needed for directional grade | Yes; side lines are half points and five runs is below either side of the integer 9.0 total without push ambiguity |
| P-221-C01–C04 | FINAL; S221 official MLB | No extra inning affected the endpoints | Yes; half-point lines |
| P-222-C01–C04 | FINAL in 10 innings; S222 official MLB | Extra-inning treatment was not supplied, but the regulation tie and 9-8 final leave all four contracts on the same winning/losing side | **Yes across regulation-only and extra-inning-inclusive endpoints** |
| P-223-C01–C04 | FINAL; S223 official MLB | No extra inning affected the endpoints | Yes; ML/half-point sides and 11 is above integer 8.0 without push ambiguity |
| P-224-C01–C04 | FINAL; S224 official MLB | No extra inning affected the endpoints | Yes; half-point lines |
| P-225-C01–C04 | FINAL; S225 official ATP | No retirement/walkover occurred | Yes; normal-completion half-point lines |
| P-226-C01–C04 | FINAL; S226 official NPB | No draw/extra-inning treatment affected the completed endpoints | Yes; half-point lines |
| P-227-C01–C04 | FINAL; S227 official NPB | No draw/extra-inning treatment affected the completed endpoints | Yes; half-point lines |
| P-228-C01–C04 | FINAL; S228 official NPB | No draw/extra-inning treatment affected the completed endpoints | Yes; half-point lines |
| P-229-C01–C04 | FINAL; S229 official KBO plus specialist box | No action/extra-inning treatment affected the completed endpoints | Yes; half-point lines |
| P-230-C01–C04 | FINAL; S230 official KBO plus specialist box | No action/extra-inning treatment affected the completed endpoints | Yes; ML/half-point/half-run endpoints |
| P-231-C01–C04 | FINAL; S231 official KBO plus specialist box | No action/extra-inning treatment affected the completed endpoints | Yes; half-point lines |
| P-232-C01–C04 | FINAL; S232 official KBO plus specialist box | No action/extra-inning treatment affected the completed endpoints | Yes; half-point lines |
| P-233-C01–C05 | Specialist final only; S233 | Corners provider/operator definition unproved; official field owner absent | Reported values agree and are on the same side of each threshold, but source ownership is unproved; all rows PROVISIONAL |
| P-234-C01–C05 | Specialist final only; S234 | Corners provider/operator definition unproved; official field owner absent | Reported values agree and are on the same side of each threshold, but source ownership is unproved; all rows PROVISIONAL |
| P-235-C01–C05 | Specialist final only; S235 | Corners provider/operator definition unproved; official field owner absent | Reported values agree and are on the same side of each threshold, but source ownership is unproved; all rows PROVISIONAL |
| P-236-C01–C04 | FINAL; S236 ECB result narrative plus specialist five-over/innings fields | No DLS/shortening affected Ireland's completed 50-over innings | Yes; half-point lines |
| P-237-C01–C04 | FINAL; S237 specialist scorecards agree | No DLS/shortening affected the completed innings/phase endpoints | Yes; half-point lines |
| P-238-C01–C04 | FINAL; S238 official ETPL | No DLS/shortening affected Glasgow's completed innings/phase endpoints | Yes; half-point lines |
| P-148-C02 | FINAL event; Q148 official club score plus specialist corner field | Named sportsbook/provider corner definition remains missing | Endpoint is below 4.5 on the retrieved field, but ownership is unproved; PROVISIONAL LOSS |
| P-162-C01–C04 | FINAL; Q162 official ITF printable draw | No retirement/walkover occurred; missing retirement wording is not outcome-changing | Yes; normal completion and half-point lines |
| P-176-C05 | FINAL event; Q176 complete specialist timeline | Named sportsbook/provider corner definition remains missing | Eight is below 10.5 on the retrieved timeline, but ownership is unproved; PROVISIONAL WIN |

P-233–P-235 remain PROVISIONAL because no current CFA/club final was recovered; agreeing specialist values may share an upstream lineage. This table records endpoint invariance separately from source authority—agreement does not turn a provisional source into a field owner.


## 4. Detailed event-by-event retrospective

| Event | Forecast expectation | Actual driver | What was right | What was wrong/omitted | Mechanism / knowability | Process grade |
|---|---|---|---|---|---|---|
| P-148 | Early goal/Toluca pressure and corner Over | Toluca won 1-0 but the specialist field reports only two Toluca corners | Winner/control view | Territory-to-corner transfer and lead-state suppression | Early Toluca lead was a named, knowable corner-suppression path; settlement remains provisional | PROCESS_DEFECT — MATCHUP_CONTEXT / CALIBRATION |
| P-162 | Te serve/return control, straight-set separation and Under | Te won 6-1, 6-4 in 17 games | Winner, handicap and Under joint tree | Nothing material; later source status was incomplete | Predicted mechanism; official result now closes the prior provisional final | COMPLIANT |
| P-176 | Low Amiens attack and low corners | Amiens won 3-0, but the complete timeline records only eight corners | Corner Under endpoint | Team/side/goal mechanism was wrong | Corner result arrived through a different allocation than forecast; provider ownership still missing | PROCESS_DEFECT — MATCHUP_CONTEXT; settlement PROVISIONAL |
| P-215 | Under 169.5 / Japan dominance | Japan 123-70; transition shooting and bench scoring sustained 193 | Winner and spread | Total centre and start-state gate | Total mechanism differed; start crossing and upper branch were knowable | PROCESS_DEFECT — STATE_FRESHNESS / CALIBRATION |
| P-216 | Zimbabwe Under 165.5 with PP Over | 64/1 PP, 101/6 at 12, then a 94-run seventh-wicket stand | Fast PP and middle collapse | Death-resource tail and final toss refresh | Early/middle path aligned; finisher tail was knowable, exact stand was not | PROCESS_DEFECT — STATE_FRESHNESS / DEPENDENCE_TAIL |
| P-217 | Full-innings Under with PP Over | 31/2 PP, then Hetmyer 111* drove 185/5 in 16 | Winner and low early branch | Shortening resource reset and operator terms | PP used a named kill path; operator missing was known | INCONCLUSIVE/PARTIAL — IDENTITY_CONTRACT; phase PROCESS_DEFECT |
| P-218 | Li straight-set separation | Li 7-5, 6-1 | Spread/Under joint tree | Nothing material | Predicted lopsided-set mechanism | COMPLIANT |
| P-219 | Mets cushion; high Stock-failure tail | Mets 3-2; Stock 5.1 scoreless | Cushion/close branch | Winner and Over weighting | Close path aligned; starter driver differed within ordinary uncertainty | COMPLIANT |
| P-220 | Reds cushion and Over | Padres 5-0; King scoreless, Singer failed | Padres winner and separation branch | Ranking ignored aligned starter/bullpen edges | Named branch occurred and was knowably underweighted | PROCESS_DEFECT — MATCHUP_CONTEXT / CALIBRATION |
| P-221 | Nationals cushion and Over; Miami winner | Washington won 6-3 | Top two contracts | Winner coherence | Top rows aligned; inconsistency was knowable | PROCESS_DEFECT — MATCHUP_CONTEXT |
| P-222 | Seattle cushion, Boston winner, Over | Boston 9-8 in 10 | Winner/margin separation and volatility | Nothing material | Predicted mechanism | COMPLIANT |
| P-223 | Angels cushion but Yankees winner/Under | Angels won 10-1; Ureña dominated | Best-starter cushion | Winner/total coherence | Cushion mechanism aligned; winner defect was knowable | PROCESS_DEFECT — MATCHUP_CONTEXT |
| P-224 | Close game, both +1.5, Under | Phillies 2-1 | All central contracts | Nothing material | Predicted mechanism | COMPLIANT |
| P-225 | Tseng separation and Under | Tseng beat Tianhui Zhang 6-4, 6-0 | Joint score tree | Settlement writer used “Zhizhen” | Forecast mechanism aligned; post-settlement identity error was knowable | COMPLIANT forecast; administrative IDENTITY_CONTRACT correction |
| P-226 | Hanshin winner but Under/Yakult cushion | Hanshin 6-2 | Favourite quality | One-sided low-total separation | Named separation branch was knowably underweighted | PROCESS_DEFECT — RATE_PROCESS / CALIBRATION |
| P-227 | Hiroshima cushion and Under | Hiroshima 5-1 after five-run seventh | Side and Under | Winner alias missed relief transition | Core target aligned; exact cluster was an ordinary tail | COMPLIANT |
| P-228 | Rakuten side and Over | Rakuten 5-1 | Side | Direct starter-pair 5-1 comparator underweighted for total | Side aligned; total error was knowable | PROCESS_DEFECT — MATCHUP_CONTEXT |
| P-229 | Hanwha cushion and Over despite KT evidence | KT 6-1 | Research found KT separation | Ranking contradicted its evidence | Named 6-2 branch essentially occurred; knowable | PROCESS_DEFECT — MATCHUP_CONTEXT / CALIBRATION |
| P-230 | NC cushion but KIA winner | NC 7-2; four-run seventh | Top cushion | Winner coherence/relief transition | Cushion aligned; internal inconsistency was knowable | PROCESS_DEFECT — MATCHUP_CONTEXT |
| P-231 | Doosan cushion and Under; LG winner | LG 3-1 | Under/winner | Exactly-two margin risk | Low-score family aligned; boundary allocation was knowable | PROCESS_DEFECT — CALIBRATION |
| P-232 | Lotte cushion and Under; Samsung winner | Samsung 3-0 | Under/winner | Favourite suppression/separation | Under aligned; cushion error knowable from team/bullpen/form | PROCESS_DEFECT — RATE_PROCESS / MATCHUP_CONTEXT |
| P-233 | Beijing scoring/early/Over/corners | Beijing 3-1, HT 1-0, 13 reported corners | Four rows | BTTS No conflated dominance with clean sheet | Main attack path aligned; cross-market distinction knowable | PROCESS_DEFECT; settlement PROVISIONAL |
| P-234 | Early/high-event knockout view | Dalian 1-0, HT 0-0, 10 reported corners | Dalian goal/corners | Knockout caution and regulation winner distinction | Only target-specific rows aligned; kill path knowable | PROCESS_DEFECT — MATCHUP_CONTEXT / CALIBRATION; PROVISIONAL |
| P-235 | Port scoring/high-event but Shandong winner | Port won 3-0, HT 0-2, 14 reported corners | Port goal/early/Over/corners | Winner and BTTS coherence | Attack path aligned; inconsistency knowable | PROCESS_DEFECT — MATCHUP_CONTEXT; PROVISIONAL |
| P-236 | Ireland innings Over but 5-over Under first | 23/1 after 5; 281/5 | Innings Over/winner | Sparse phase sample, line-crossing corridor, extras | Innings aligned; evidence-width defect knowable | PROCESS_DEFECT — CALIBRATION / RATE_PROCESS |
| P-237 | SA Under 184.5 and PP Under | 59/0; 185/7 | Winner and upper branches | Toss refresh, direct opponent/venue evidence, width | Upper branch occurred; 0.5 margin random but rank defect knowable | PROCESS_DEFECT — STATE_FRESHNESS / MATCHUP_CONTEXT |
| P-238 | Glasgow phase/innings Unders | 39/2; 140/9; Rotterdam chased | Both Unders and winner | Nothing material | Predicted mechanism | COMPLIANT |

Other P-001–P-214 event retrospectives remain in the combined/component appendices; P-148, P-162 and P-176 are repeated here because their contract status changed in this audit. The chronological table above reclassifies current state without inserting later facts into frozen cards.

## 5. Dedicated Rank #1-loss audit

| Contract | Rank #1 thesis | Actual | Failure route | Defect class | Audit conclusion |
|---|---|---|---|---|---|
| P-215-C04 | Under 169.5 | 193 | Start crossed; transition/bench upper branch unweighted | STATE_FRESHNESS / CALIBRATION | Process wrong; quarantine |
| P-216-C02 | Zimbabwe Under 165.5 | 195 | 64 PP, middle collapse, 94-run seventh-wicket recovery | STATE_FRESHNESS / DEPENDENCE_TAIL | Broad thesis partly right; finisher tail underweighted |
| P-217-C02 | GAW Under 174.5 | 185 in 16 | Shortening changed intent; operator rule absent | IDENTITY_CONTRACT / UNKNOWN_DEFINITION | Directional loss only; formal grade unresolved |
| P-220-C02 | Reds +1.5 | 0-5 | Aligned starter/bullpen/favourite edges outweighed breadth | MATCHUP_CONTEXT / CALIBRATION | Knowable ranking error |
| P-226-C04 | Under 7.5 | 8 | One-sided 6-2 family ordinary at low total | RATE_PROCESS / CALIBRATION | Knowable geometry error |
| P-229-C01 | Hanwha +1.5 | 1-6 | Own H2H/current evidence favoured KT separation | MATCHUP_CONTEXT / CALIBRATION | Knowable ranking contradiction |
| P-231-C02 | Doosan +1.5 | 1-3 | Exactly-two favourite margin not separated from “close” | CALIBRATION | Boundary-sensitive but knowable |
| P-232-C01 | Lotte +1.5 | 0-3 | Samsung suppression/separation aligned across inputs | RATE_PROCESS / MATCHUP_CONTEXT | Knowable ranking error |
| P-234-C01 | 1H Over 0.5 | HT 0-0 | Knockout regulation caution underweighted | MATCHUP_CONTEXT / CALIBRATION | PROVISIONAL loss; single-case sport-native candidate |
| P-236-C04 | Ireland after 5 Under 20.5 | 23/1 | Corridor crossed line; sparse sample/extras risk | CALIBRATION / RATE_PROCESS | Knowable evidence-width error |
| P-237-C02 | SA Under 184.5 | 185 | Toss/exposure and exact opponent/venue 61 PP underweighted | STATE_FRESHNESS / MATCHUP_CONTEXT | 0.5 boundary, but rank defect knowable |

A Rank #1 loss is not itself calibration proof. P-231 and P-237 were boundary-sensitive, but both exposed preissue ranking/width defects. P-217 is a directional trigger only; the operator grade remains unresolved.

## 6. What went right across the batch

- Joint score trees worked best when they separated winner from margin (P-222), overlapping cushions (P-224), and phase from innings (P-218, P-238).
- Official league/tour result lanes closed MLB, NPB, KBO, ATP/WTA/US Open, FIBA and ETPL ordinary endpoints without inventing operator rules.
- Several cards contained the decisive counterbranch: Padres/Samsung/KT/Hanshin separation and Zimbabwe/GAW acceleration were rank-weight defects, not missing research.
- Complement geometry was preserved, so the 99-row ledger is not misrepresented as 99 independent trials.

## 7. Recurring failures and candidate improvements

- Cushion breadth repeatedly outranked aligned favourite starter/team/bullpen separation evidence (P-220, P-229, P-231, P-232).
- Low total repeatedly implied close margin; 5-0, 6-1, 3-1 and 3-0 are ordinary one-sided low-score families.
- Winner annotations contradicted the highest-ranked side or derivative mechanism (P-221, P-223, P-230, P-235).
- Cricket phase lines ranked first despite a line-crossing corridor or missing exact sample (P-236); toss/exposure and wicket resources were not refreshed strongly enough (P-216, P-237).
- Niche soccer fields were over-closed from specialist pages. Preserve operator/provider name or use PROVISIONAL/UNRESOLVED.
- Proposed candidates: sport-native knockout regulation adjustment (`C-PL10-SOC-KNOCKOUT-REG`) and cricket early-phase extras/legality term (`C-PL10-CR-PHASE-EXTRAS`). Both stay CANDIDATE with zero prospective completions.

## 8. Learning governance disposition

| Disposition | Items | Decision |
|---|---|---|
| Proposed | C-PL10-SOC-KNOCKOUT-REG; C-PL10-CR-PHASE-EXTRAS | CANDIDATE only; single-case origins; no active weight/rule change |
| Reinforced | L-009, L-010, L-039, L-043, L-045, L-049, L-050, L-055, L-056 | Existing controls cover phase/resource separation, low/close vs separation, source atomicity, conflicts and slate geometry |
| Promoted | None | No PROMOTED_PROCESS or PROMOTED_FORECAST claim |
| Rejected | Draft phrase “General learnings promoted to the top” and any single-batch coefficient/weight shift | Violates prospective promotion procedure |
| Deferred | Baseball separation weighting; winner/derivative coherence weight | Existing gates reinforced; numerical change needs frozen prospective manifest |
| Performance eligibility | P-215–P-238 | Descriptive late-import evidence only; no calibration, hit-rate, model-selection or forecast-weight completion |

## 9. Source-quality findings and candidates

Every source below was accessed on 2026-09-02 Australia/Sydney. A successful retrieval creates a field-specific research candidate, not universal approval or H0 permission.

| ID | Direct source | Owner/role | Fields and limitations |
|---|---|---|---|
| S215 | [FIBA game 126960](https://www.fiba.basketball/en/events/fiba-basketball-world-cup-2027-asian-qualifiers/games/126960-JPN-QAT) | Official event owner | Final/team scores/box; dynamic correction history not audited for H0 |
| S216 | [ICC report](https://www.icc-cricket.com/news/zimbabwe-survive-namibia-fightback-in-windhoek-thriller) / [CricketWorld scorecard](https://www.cricketworld.com/cricket/namibia-vs-zimbabwe/match/scorecard/98363) | ICC report / specialist phase feed | Final/mechanism and 6-over field; separate lineages; neither owns operator rules |
| S217 | [CPL release](https://cplt20.prezly.com/hetmyer-hundred-bests-knight-riders) / [CricketWorld scorecard](https://www.cricketworld.com/cricket/trinbago-knight-riders-vs-guyana-amazon-warriors/match/scorecard/96829) | Competition report / specialist | Final, revised overs, phase; operator shortening rules absent |
| S218 | [US Open/USTA report](https://www.usopen.org/amp/en_US/news/articles/2026-09-01/ann_lis_decision_to_relocate_pays_dividends_at_2026_us_open.html) | Official event owner | Winner/set score; normal completion |
| S219 | [MLB Rays scoreboard](https://www.mlb.com/rays/scores/2026-08-31) | League/team official | Final and inning line |
| S220 | [MLB Padres recap](https://www.mlb.com/padres/video/machado-king-propel-padres-5-0-win-vs-reds) | League/team official | Final and pitcher mechanism; structured box preferable for reuse |
| S221 | [MLB story](https://www.mlb.com/stories/game/822689) | League official | Final/game flow |
| S222 | [MLB official game video/line score](https://www.mlb.com/video/game/824719) | League official | Final plus inning line; 8-8 after nine and 9-8 after ten |
| S223 | [MLB story 823982](https://www.mlb.com/stories/game/823982) | League official | Final/inning flow |
| S224 | [MLB story](https://www.mlb.com/stories/game/825040) | League official | Final/game flow |
| S225 | [ATP Zhangjiagang results](https://www.atptour.com/en/scores/current-challenger/zhangjiagang/7783/results) | Tour official | Identity and set score; confirms Tianhui Zhang |
| S226 | [NPB September 1 results](https://npb.jp/bis/eng/2026/games/) | League official | Final/inning score; exact page preferable |
| S227 | [NPB D-C-20](https://npb.jp/scores/2026/0901/d-c-20/) | League official | Final/inning score |
| S228 | [NPB September 1 results](https://npb.jp/bis/eng/2026/games/) | League official | Final/inning score; exact page preferable |
| S229 | [KBO daily](https://eng.koreabaseball.com/Schedule/DailySchedule.aspx) / [MyKBO 13892](https://mykbostats.com/games/13892-Hanwha-vs-KT-20260901) | League official / specialist | Official final plus detailed secondary box |
| S230 | [KBO daily](https://eng.koreabaseball.com/Schedule/DailySchedule.aspx) / [MyKBO 13893](https://mykbostats.com/games/13893-Kia-vs-NC-20260901) | League official / specialist | Same limitation |
| S231 | [KBO daily](https://eng.koreabaseball.com/Schedule/DailySchedule.aspx) / [MyKBO 13894](https://mykbostats.com/games/13894-LG-vs-Doosan-20260901) | League official / specialist | Same limitation |
| S232 | [KBO daily](https://eng.koreabaseball.com/Schedule/DailySchedule.aspx) / [MyKBO 13895](https://mykbostats.com/games/13895-Lotte-vs-Samsung-20260901) | League official / specialist | Same limitation |
| S233 | [Flashscore](https://www.flashscoreusa.com/game/soccer/beijing-guoan-WSLjVBLN/lanzhou-longyuan-athletic-vq7b83U1/) / [SoccerPunter](https://www.soccerpunter.com/match/19726928/Beijing-Guoan-vs-Lanzhou-Longyuan) | Specialist surfaces | No current CFA/club final recovered; PROVISIONAL; upstream independence unproved |
| S234 | [Sofascore](https://www.sofascore.com/football/match/dalian-yingbo-fc-shanghai-shenhua/yrbsRZOd) / [BeSoccer](https://www.besoccer.com/match/dalian-zhixing/shanghai-shenhua/2026345784) | Specialist surfaces | No current CFA/club final recovered; PROVISIONAL |
| S235 | [Sofascore](https://www.sofascore.com/football/match/shanghai-port-shandong-taishan/wrbsMFq) / [Scoremer](https://www.scoremer.com/match_live/1636436) | Specialist surfaces | No current CFA/club final recovered; PROVISIONAL |
| S236 | [ECB highlight](https://www.ecb.co.uk/video/4570463/highlights--bouchier-century-powers-three-lions-to-win--england-women-v-ireland--1st-metro-bank-odi) / [CricketWorld scorecard](https://www.cricketworld.com/cricket/england-women-vs-ireland-women/match/scorecard/95250) | Host board / specialist phase | Result narrative plus exact 5-over/innings field |
| S237 | [ESPNcricinfo](https://www.cricinfo.com/series/namibia-t20i-tri-series-aug-2026-2026-1549518/south-africa-vs-zimbabwe-4th-match-1549527/full-scorecard) / [CricketWorld](https://www.cricketworld.com/cricket/south-africa-vs-zimbabwe/match/scorecard/98364) | Specialist scorecards | Strong agreement; no indexed host-board exact report found |
| S238 | [ETPL official report](https://www.etplofficial.com/news/dockers-prevail-in-dramatic-finish-against-cosmic) | Competition owner | Static report controls final; dynamic match page was stale/upcoming |

Queue-source changes:

- `Q148` — P-148 moves to **PROVISIONAL LOSS**: [365Scores](https://www.365scores.com/es/football/match/liga-mx-femenil-7143/leon-%28w%29-toluca-%28w%29-53629-53634-7143) reports 2-6 corners; the [Toluca report](https://www.tolucafc.com/noticias/estan-invictas) owns only the 1-0 final.
- `Q176` — P-176 moves to **PROVISIONAL WIN**: the complete [Football365 timeline](https://www.football365.fr/direct-foot/359214/359496/amiens-sc-versailles.html) contains five Amiens and three Versailles corners (8 total), but is not the official stat owner.
- `Q162` — P-162 is closed by the [official ITF print draw](https://www.itftennis.com/en/tournament/draws-and-results/print/?eventClassificationCode=M&matchTypeCode=S&tourType=N&tournamentId=1100204161).
- New candidates are field-specific only: ITF printable draws, static ICC/ETPL reports when dynamic pages are stale, and complete event timelines for provisional corner reconstruction. None is universally approved.

## 10. Local documents changed

| Document | Purpose |
|---|---|
| `COMPREHENSIVE_SETTLEMENT_AUDIT_2026-09-02.md` | Consolidated chronological, contract, retrospective, Rank #1, source, learning and queue audit |
| `PREDICTION_LOG_COMBINED.md` | Top administrative queue/next-ID snapshot only |
| `C:/Users/danie/Downloads/PREDICTION_MINI_RUNNING_LOG_P238(1).md` | Superseding correction layer for P-217 IDs, P-225 identity, provenance, provisional status and counts |
| `LEARNING_REGISTER.md` | Two CANDIDATE rows plus reinforced/rejected/deferred disposition; no promotion |
| `DATA_SOURCE_REGISTER.md` | Field-specific source candidates and limitations; no approval |
| `README.md` | Active map and stale P-216 status |

No sport/general rule file changes: existing controls already govern the observed defects; duplicating them or claiming predictive improvement would breach learning governance.

## 11. Remaining queue

No event is live. The audit is **not fully closed** because these final-event fields remain unresolved, provisional, or operator-dependent:

| Item | Status | Exact missing field |
|---|---|---|
| P-126 result/phase and C06 | UNRESOLVED / CONFLICTED | SFA/event-owner final, phase chronology and provider-consistent corners |
| P-148-C02 | PROVISIONAL LOSS | Named operator/provider-owner corner definition; specialist reports Toluca 2 |
| P-149-C02 | PROVISIONAL WIN | Named operator/provider-owner Ventura corner count |
| P-151-C02 | STRONG PROVISIONAL WIN | Named operator/provider-owner Boca corner count; secondary 11-3 |
| P-166-C01–C04 | RESEARCH SETTLED / OPERATOR UNKNOWN | Actual sportsbook OT/action terms |
| P-176-C05 | PROVISIONAL WIN | Official/provider-owner total-corner field; timeline totals 8 |
| P-178-C05 | UNRESOLVED | Complete trusted total-corner count and provider definition |
| P-179-C05 | PROVISIONAL WIN | Named provider-owner confirmation of reported 8-1 corners |
| P-200-C01–C04 | RESEARCH SETTLED / OPERATOR UNKNOWN | Actual sportsbook regulation vs OT/SO endpoint |
| P-217-C01/C02 | UNRESOLVED | Actual operator reduced-overs/DLS/action/void rule |

Next distinct canonical ID: **P-239**.
