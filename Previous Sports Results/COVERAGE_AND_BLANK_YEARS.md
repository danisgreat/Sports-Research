# Previous Sports Results — coverage, blank years and why

**Written 2026-09-30 (AEST).** This explains which folders should stay blank and why, which fields cannot be recovered for which eras, and where the current `COACHES.md`/`OFFICIATING.md` statuses disagree with the historical record. Sources for filling the active years are in the [implementation guide](DATA_SOURCES_IMPLEMENTATION.md).

**Evidence.** Competition histories were checked against each competition's champions/editions list on Wikipedia (read through the Wikipedia API on 2026-09-30; used as a discovery source), AFL Tables season pages, WAFL FootyFacts and general knowledge. Each competition's evidence basis is printed. Items marked **VERIFY** are not settled: check them against the governing body's own list before changing a folder.

## 1. How to mark a year that cannot be populated

Leave the CSV with its header only, and write the reason in `COACHES.md` and `OFFICIATING.md` using one of these statuses:

| Status | Use when | Example |
|---|---|---|
| `NOT_YET_FOUNDED` | The competition did not exist yet | NBA before 1946 |
| `NOT_HELD` | The competition existed but was not staged that year (war, pandemic, lockout, dispute, date change) | Wimbledon 2020; NHL 2004-05 |
| `NOT_SCHEDULED` | Periodic event with no edition that year | FIFA World Cup 2021 |
| `CURTAILED` | Season started but was stopped; games that were played exist and should be logged | EuroLeague 2019-20 |
| `HELD_DATA_UNAVAILABLE` | The event was held but a field cannot be sourced (for example officials in 1920) | NBA referees before 1989-90 |
| `SCOPE_EXCLUDED` | Held, but outside what this folder is meant to cover | Women's Wimbledon before 1973 if the WTA folder is kept Open-era only |

Today the folders use a single `INACTIVE` status with a generic reason ('war interruptions, labor strikes, pandemic restrictions, or league suspension'). That hides the real cause and treats curtailed seasons as if no games were played.

## 2. Which year a season is filed under

The folders are 1900–2025. The existing files are **not consistent**: the NBA roster file says the 2025 folder holds 2025-26 (start year), but the cancelled 2004-05 NHL season is marked in the 2005 folder (end year), and the 2019-20 EuroLeague is marked in 2020. Recommended rule:

1. **Calendar-year competitions** (MLB, AFL, NRL, MLS, IPL, Grand Slams): the year played.
2. **Split seasons** (NBA, NHL, European football and basketball, Sheffield Shield): the year the season **starts** (2024-25 → 2024). This matches most existing first-season years (NBA 1946, NHL 1917, UEFA Champions League 1955, La Liga 1929).
   Exceptions already in the folders: EuroLeague and LNB Élite start at the END year of their first season (EuroLeague 1958 = 1957-58). Either convert them or document the exception in the competition's README.
3. **Tournaments and one-off games**: the year the event was played. Postponed events are filed in the year played and cross-referenced from the named year:
   Tokyo 2020 Olympics → 2021; UEFA EURO 2020 → 2021; Rugby League World Cup 2021 and Women's Rugby World Cup 2021 → 2022; AFCON 2021 → 2022 and AFCON 2023 → 2024; AFC Asian Cup 2023 → 2024; FIFA Club World Cup 2020 → 2021 and 2021 → 2022.
   The folders already do this for the Olympics, EURO 2020 and both 2021 rugby World Cups (2020 inactive, 2021/2022 active). AFCON and the AFC Asian Cup are filed by edition name instead: align them.
4. **Bowl games** by game date; **College Football Playoff** by season year (the folder already does this). Bowls that moved between 31 December and 1 January create calendar years with no game or two games: record that explicitly.
5. **Two seasons in one year** (AFLW 2022, NRLW 2022, NBL 1998, first La Liga season 1929): keep both in the same folder with a `Season` value in the Game Type column.

## 3. Fields that cannot be recovered for some eras

| Field | Where it runs out | Why |
|---|---|---|
| Game officials, basketball (NBA) | Before 1989-90 | Basketball-Reference referee registers start in 1989-90; no verified source lists earlier crews per game. |
| Game officials, NFL | Before 2015 in open data | nflverse officials start in 2015; earlier crews are on Pro-Football-Reference (browser only) and in newspapers. |
| Game officials, NHL | Before the modern game-centre era | NHL right-rail data covers modern games; Hockey-Reference box scores list none; a 1949-50 game-centre request returned 404. |
| Umpires, VFL/AFL and state leagues | Whole history in open structured data | AFL Tables and the AFL API carry no umpire fields. Trove newspapers name umpires to 1954. |
| Umpires, MLB | Partial before full-crew records | Retrosheet game logs always carry the plate umpire field; full crews depend on the season. |
| Coaches, cricket and early rugby union | Most of the 20th century | Teams were led by captains; coaching staffs are a modern role. Log the captain in the notes and leave the coach field blank with `HELD_DATA_UNAVAILABLE`. |
| Coaches and chair umpires, tennis | Almost all of history | Players' coaches were not recorded; chair umpires are published only for recent finals. Leave blank. |
| Officials, college football, Canadian football, U SPORTS | Whole history in open data | No structured source was found; only newspapers and game books. |
| Game-level data, pre-2005 minor-league baseball, pre-2000 NBL/WNBL, pre-1990 European basketball, early women's leagues | Varies | Not published in a verified database; newspapers only. |

## 4. Competition-by-competition coverage

Columns: first season; the year convention this spec uses for the folder; years 1900–2025 with **no competition** and the reason; years that were **held but curtailed or unusual**; items to verify; notes. Pre-founding years are summarised by the first season.

### AFL

#### AFL

- **First season:** 1897. **Folder year convention:** calendar year. **Evidence:** AT.
- **Blank before founding:** none (existed before 1900).
- **No competition after founding:** none — contested every year to 2025.
- **Held but curtailed or unusual:** 2020: Shortened season (16-minute quarters, 17 rounds).
- **Notes:** VFL 1897-1989, AFL from 1990. Played every season incl. both world wars (only 4 clubs in 1916).

#### AFL Grand Final

- **First season:** 1898. **Folder year convention:** year the event was played. **Evidence:** AT.
- **Blank before founding:** none (existed before 1900).
- **No competition after founding:** 1924: No Grand Final: 1924 finals were a round-robin; Essendon premiers on the round-robin.
- **Held but curtailed or unusual:** 1948: Drawn Grand Final replayed (two matches); 1977: Drawn Grand Final replayed; 2010: Drawn Grand Final replayed; 2020: Played at the Gabba, Brisbane (first outside Victoria).
- **Notes:** AFL Tables season pages 1898-1931 all carry a Grand Final except 1897 (round-robin) and 1924. 1916 and 1917 Grand Finals were played.

#### AFLW

- **First season:** 2017. **Folder year convention:** calendar year. **Evidence:** K.
- **Blank before founding:** 1900–2016.
- **No competition after founding:** none — contested every year to 2025.
- **Held but curtailed or unusual:** 2020: Season abandoned before the Grand Final; no premiership awarded; 2022: TWO seasons in calendar 2022: Season 6 (Jan-Apr) and Season 7 (Aug-Nov).

### American Football

#### IFAF World Championship

- **First season:** 1999. **Folder year convention:** year the event was played. **Evidence:** K.
- **Blank before founding:** 1900–1998.
- **No competition after founding:** 2000–2002, 2004–2006, 2008–2010, 2012–2014, 2016–2018, 2020–2025: No edition scheduled (not an annual event); 2019: 2019 edition (Australia) cancelled; none held since.

#### NFL

- **First season:** 1920. **Folder year convention:** season START year (2024-25 → 2024). **Evidence:** K.
- **Blank before founding:** 1900–1919.
- **No competition after founding:** none — contested every year to 2025.
- **Notes:** APFA 1920-21, NFL from 1922. 1982 and 1987 strike-shortened but played.

#### Super Bowl

- **First season:** 1967. **Folder year convention:** year the event was played. **Evidence:** K.
- **Blank before founding:** 1900–1966.
- **No competition after founding:** none — contested every year to 2025.
- **Notes:** Folder = calendar year the game was played (Super Bowl I, 15 Jan 1967, closed the 1966 season).

#### UFL

- **First season:** 2024. **Folder year convention:** calendar year. **Evidence:** K.
- **Blank before founding:** 1900–2023.
- **No competition after founding:** none — contested every year to 2025.
- **Notes:** The 2024- UFL (XFL + USFL merger). Not the 2009-2012 United Football League, which is a different competition.

### Baseball

#### Australian Baseball League

- **First season:** 1989. **Folder year convention:** season START year (2024-25 → 2024). **Evidence:** K (VERIFY 1999-2001 IBLA seasons and 2020-21/2021-22 cancellations).
- **Blank before founding:** 1900–1988.
- **No competition after founding:** 1999–2009: Original ABL folded after 1998-99; 1999-2002 International Baseball League of Australia, then Claxton Shield (not the ABL); 2020: 2020-21 season cancelled (COVID-19); 2021: 2021-22 season cancelled (COVID-19).
- **VERIFY:** 1999–2001, 2020–2021 (status not settled by the evidence read).

#### CPBL

- **First season:** 1990. **Folder year convention:** calendar year. **Evidence:** K.
- **Blank before founding:** 1900–1989.
- **No competition after founding:** none — contested every year to 2025.

#### Caribbean Series and Winter Leagues

- **First season:** 1949. **Folder year convention:** year the event was played. **Evidence:** W.
- **Blank before founding:** 1900–1948.
- **No competition after founding:** 1961–1969: Series suspended after the Cuban Revolution (1961-1969); 1981: Not held: Venezuelan league players' strike.
- **Notes:** Folder name also says 'Winter Leagues': the national winter leagues (Cuba to 1961, Puerto Rico from 1938, Venezuela from 1946, Mexico Pacific from 1945, Dominican from 1951/1955) ran in years the Series did not. Decide whether this folder logs the Series only.

#### KBO

- **First season:** 1982. **Folder year convention:** calendar year. **Evidence:** K.
- **Blank before founding:** 1900–1981.
- **No competition after founding:** none — contested every year to 2025.

#### MLB

- **First season:** 1876. **Folder year convention:** calendar year. **Evidence:** K.
- **Blank before founding:** none (existed before 1900).
- **No competition after founding:** none — contested every year to 2025.
- **Held but curtailed or unusual:** 1994: Season ended 11 Aug 1994; no postseason or World Series; 2020: 60-game season.
- **Notes:** 1900: National League only (American League became major in 1901). 1981 and 1994-95 strikes; 1994 postseason cancelled; 2020 60-game season.

#### Mexican League

- **First season:** 1925. **Folder year convention:** calendar year. **Evidence:** K.
- **Blank before founding:** 1900–1924.
- **No competition after founding:** 2020: 2020 season cancelled (COVID-19).

#### Minor Leagues

- **First season:** 1877. **Folder year convention:** calendar year. **Evidence:** K.
- **Blank before founding:** none (existed before 1900).
- **No competition after founding:** 2020: 2020 minor-league season cancelled (COVID-19).
- **Notes:** Minor leagues existed in 1900 (the folder starts at 1901, the founding of the NAPBL). The 1900 American League was itself a minor league.

#### NPB

- **First season:** 1936. **Folder year convention:** calendar year. **Evidence:** K.
- **Blank before founding:** 1900–1935.
- **No competition after founding:** 1945: No season (end of World War II).
- **Notes:** Japanese Baseball League 1936-1949 (1936 and 1937 had spring and autumn seasons); NPB two-league system from 1950.

#### Summer Olympics

- **First season:** 1992. **Folder year convention:** year the event was played. **Evidence:** K.
- **Blank before founding:** 1900–1991.
- **No competition after founding:** 1993–1995, 1997–1999, 2001–2003, 2005–2007, 2009–2019, 2022–2025: No edition scheduled (not an annual event); 2020: Tokyo 2020 postponed; played in 2021 (filed under 2021).
- **Notes:** Official medal sport 1992-2008 and at Tokyo 2020, which was PLAYED IN 2021 (folder must choose 2020 or 2021: see the convention section). Demonstration events 1912, 1936, 1956, 1964, 1984, 1988 are not medal events.

#### WBSC Premier12

- **First season:** 2015. **Folder year convention:** year the event was played. **Evidence:** K.
- **Blank before founding:** 1900–2014.
- **No competition after founding:** 2016–2018, 2020–2023, 2025: No edition scheduled (not an annual event).

#### World Baseball Classic

- **First season:** 2006. **Folder year convention:** year the event was played. **Evidence:** K.
- **Blank before founding:** 1900–2005.
- **No competition after founding:** 2007–2008, 2010–2012, 2014–2016, 2018–2020, 2022, 2024–2025: No edition scheduled (not an annual event); 2021: 2021 edition cancelled (COVID-19).

### Basketball

#### ABA League

- **First season:** 2001. **Folder year convention:** season START year (2024-25 → 2024). **Evidence:** K.
- **Blank before founding:** 1900–2000.
- **No competition after founding:** none — contested every year to 2025.
- **Held but curtailed or unusual:** 2019: 2019-20 season halted March 2020 (COVID-19); games before the stoppage exist; no champion.

#### B League

- **First season:** 2016. **Folder year convention:** season START year (2024-25 → 2024). **Evidence:** K.
- **Blank before founding:** 1900–2015.
- **No competition after founding:** none — contested every year to 2025.
- **Held but curtailed or unusual:** 2019: 2019-20 season halted March 2020 (COVID-19); games before the stoppage exist; no champion.

#### BSL

- **First season:** 1966. **Folder year convention:** season START year (2024-25 → 2024). **Evidence:** K.
- **Blank before founding:** 1900–1965.
- **No competition after founding:** none — contested every year to 2025.
- **Held but curtailed or unusual:** 2019: 2019-20 season halted March 2020 (COVID-19); games before the stoppage exist; no champion.

#### Basketball Bundesliga

- **First season:** 1966. **Folder year convention:** season START year (2024-25 → 2024). **Evidence:** K.
- **Blank before founding:** 1900–1965.
- **No competition after founding:** none — contested every year to 2025.
- **Held but curtailed or unusual:** 2019: Completed as a 10-team tournament in Munich, June 2020.

#### CBA

- **First season:** 1995. **Folder year convention:** season START year (2024-25 → 2024). **Evidence:** K.
- **Blank before founding:** 1900–1994.
- **No competition after founding:** none — contested every year to 2025.
- **Held but curtailed or unusual:** 2019: Resumed in a bubble June 2020 and completed.

#### EuroBasket

- **First season:** 1935. **Folder year convention:** year the event was played. **Evidence:** K.
- **Blank before founding:** 1900–1934.
- **No competition after founding:** 1936, 1938, 1940–1945, 1948, 1950, 1952, 1954, 1956, 1958, 1960, 1962, 1964, 1966, 1968, 1970, 1972, 1974, 1976, 1978, 1980, 1982, 1984, 1986, 1988, 1990, 1992, 1994, 1996, 1998, 2000, 2002, 2004, 2006, 2008, 2010, 2012, 2014, 2016, 2018–2021, 2023–2024: No edition scheduled (not an annual event).
- **Notes:** The 2021 edition was postponed and played in 2022.

#### EuroCup

- **First season:** 2002. **Folder year convention:** season START year (2024-25 → 2024). **Evidence:** K.
- **Blank before founding:** 1900–2001.
- **No competition after founding:** none — contested every year to 2025.
- **Held but curtailed or unusual:** 2019: 2019-20 season halted March 2020 (COVID-19); games before the stoppage exist; cancelled with no champion.

#### EuroLeague

- **First season:** 1958. **Folder year convention:** season END year (2024-25 → 2025). **Evidence:** K.
- **Blank before founding:** 1900–1957.
- **No competition after founding:** none — contested every year to 2025.
- **Held but curtailed or unusual:** 2020: 2019-20 season cancelled after the March 2020 stoppage; no champion (games Oct 2019-Mar 2020 exist).
- **Notes:** First season 1957-58 (folder uses the END year: 1958).

#### EuroLeague Women

- **First season:** 1958. **Folder year convention:** season START year (2024-25 → 2024). **Evidence:** K.
- **Blank before founding:** 1900–1957.
- **No competition after founding:** none — contested every year to 2025.
- **Held but curtailed or unusual:** 2019: 2019-20 season halted March 2020 (COVID-19); games before the stoppage exist; cancelled with no champion.
- **Notes:** First season 1958-59 (folder uses the START year: 1958).

#### FIBA AmeriCup

- **First season:** 1980. **Folder year convention:** year the event was played. **Evidence:** K.
- **Blank before founding:** 1900–1979.
- **No competition after founding:** 1981–1983, 1985–1987, 1990–1991, 1994, 1996, 1998, 2000, 2002, 2004, 2006, 2008, 2010, 2012, 2014, 2016, 2018–2021, 2023–2024: No edition scheduled (not an annual event).

#### FIBA Asia Cup

- **First season:** 1960. **Folder year convention:** year the event was played. **Evidence:** K.
- **Blank before founding:** 1900–1959.
- **No competition after founding:** 1961–1962, 1964, 1966, 1968, 1970, 1972, 1974, 1976, 1978, 1980, 1982, 1984, 1986, 1988, 1990, 1992, 1994, 1996, 1998, 2000, 2002, 2004, 2006, 2008, 2010, 2012, 2014, 2016, 2018–2021, 2023–2024: No edition scheduled (not an annual event).

#### Greek Basket League

- **First season:** 1927. **Folder year convention:** season START year (2024-25 → 2024). **Evidence:** W (VERIFY season-to-year mapping).
- **Blank before founding:** 1900–1926.
- **No competition after founding:** 1930–1933: Not held (Wikipedia: '1930-34 not held'); 1937: 1937-38 not held; 1940–1944: Not held (World War II / occupation); 1947: 1947-48 not held; 1951: 1951-52 not held; 1955: 1955-56 not held.
- **Held but curtailed or unusual:** 2019: 2019-20 halted (COVID-19); Panathinaikos declared champion on regular-season standings.
- **VERIFY:** 1945 (status not settled by the evidence read).
- **Notes:** First championship 1927-28. Seasons 1928-29 and 1929-30 need checking against the Hellenic Basketball Federation list (VERIFY).

#### KBL

- **First season:** 1997. **Folder year convention:** calendar year. **Evidence:** K.
- **Blank before founding:** 1900–1996.
- **No competition after founding:** none — contested every year to 2025.
- **Held but curtailed or unusual:** 2019: 2019-20 season halted March 2020 (COVID-19); games before the stoppage exist; no champion.
- **Notes:** First season 1997 (calendar); later split seasons from 1997-98.

#### LNB Elite

- **First season:** 1921. **Folder year convention:** season END year (2024-25 → 2025). **Evidence:** W (VERIFY whether '1939-41' means seasons ending 1939-41).
- **Blank before founding:** 1900–1920.
- **No competition after founding:** 1939–1941: Not held (World War II).
- **Held but curtailed or unusual:** 2020: 2019-20 cancelled (COVID-19); 2021: Final was a single match.
- **VERIFY:** 1939–1945 (status not settled by the evidence read).

#### Liga ACB

- **First season:** 1957. **Folder year convention:** season START year (2024-25 → 2024). **Evidence:** K.
- **Blank before founding:** 1900–1956.
- **No competition after founding:** none — contested every year to 2025.
- **Held but curtailed or unusual:** 2019: Completed as a 12-team final phase in Valencia, June 2020.
- **Notes:** Liga Nacional 1957-1983 (1957 calendar season), Liga ACB from 1983-84.

#### Men's FIBA World Cup

- **First season:** 1950. **Folder year convention:** year the event was played. **Evidence:** K.
- **Blank before founding:** 1900–1949.
- **No competition after founding:** 1951–1953, 1955–1958, 1960–1962, 1964–1966, 1968–1969, 1971–1973, 1975–1977, 1979–1981, 1983–1985, 1987–1989, 1991–1993, 1995–1997, 1999–2001, 2003–2005, 2007–2009, 2011–2013, 2015–2018, 2020–2022, 2024–2025: No edition scheduled (not an annual event).

#### NBA

- **First season:** 1946. **Folder year convention:** season START year (2024-25 → 2024). **Evidence:** K.
- **Blank before founding:** 1900–1945.
- **No competition after founding:** none — contested every year to 2025.
- **Held but curtailed or unusual:** 2019: Suspended March 2020; finished in the Orlando bubble (Jul-Oct 2020).
- **Notes:** BAA 1946-49, NBA from 1949-50. 1998-99 and 2011-12 lockout-shortened.

#### NBA G League

- **First season:** 2001. **Folder year convention:** season START year (2024-25 → 2024). **Evidence:** K.
- **Blank before founding:** 1900–2000.
- **No competition after founding:** none — contested every year to 2025.
- **Held but curtailed or unusual:** 2019: 2019-20 season halted March 2020 (COVID-19); games before the stoppage exist; no champion; 2020: 2020-21 played in a single-site bubble (18 teams).

#### NBL

- **First season:** 1979. **Folder year convention:** calendar year. **Evidence:** K.
- **Blank before founding:** 1900–1978.
- **No competition after founding:** none — contested every year to 2025.
- **Notes:** Calendar seasons 1979-1998, then summer seasons from 1998-99 (folder 1998 holds BOTH the 1998 season and the start of 1998-99).

#### NBL1

- **First season:** 2019. **Folder year convention:** calendar year. **Evidence:** W.
- **Blank before founding:** 1900–2018.
- **No competition after founding:** 2020: 2020 season cancelled (COVID-19).

#### PBA

- **First season:** 1975. **Folder year convention:** calendar year. **Evidence:** K.
- **Blank before founding:** 1900–1974.
- **No competition after founding:** none — contested every year to 2025.
- **Held but curtailed or unusual:** 2020: Philippine Cup only, played in a bubble.

#### Serie A

- **First season:** 1920. **Folder year convention:** season END year (2024-25 → 2025). **Evidence:** W.
- **Blank before founding:** 1900–1919.
- **No competition after founding:** 1929: Not held; 1944: 1943-44 not held (World War II); 1945: 1944-45 not held (World War II).
- **Held but curtailed or unusual:** 2020: 2019-20 cancelled (COVID-19); no title awarded.
- **VERIFY:** 1944–1945 (status not settled by the evidence read).

#### Summer Olympics

- **First season:** 1936. **Folder year convention:** year the event was played. **Evidence:** K.
- **Blank before founding:** 1900–1935.
- **No competition after founding:** 1937–1939, 1941–1943, 1945–1947, 1949–1951, 1953–1955, 1957–1959, 1961–1963, 1965–1967, 1969–1971, 1973–1975, 1977–1979, 1981–1983, 1985–1987, 1989–1991, 1993–1995, 1997–1999, 2001–2003, 2005–2007, 2009–2011, 2013–2015, 2017–2019, 2022–2023, 2025: No edition scheduled (not an annual event); 1940, 1944: Olympic Games cancelled (World War II); 2020: Tokyo 2020 postponed; played in 2021 (filed under 2021).
- **Notes:** Women's tournament from 1976. Tokyo 2020 was PLAYED IN 2021.

#### VTB United League

- **First season:** 2008. **Folder year convention:** season START year (2024-25 → 2024). **Evidence:** K.
- **Blank before founding:** 1900–2007.
- **No competition after founding:** none — contested every year to 2025.
- **Held but curtailed or unusual:** 2019: 2019-20 season halted March 2020 (COVID-19); games before the stoppage exist; cancelled with no champion.

#### WNBA

- **First season:** 1997. **Folder year convention:** calendar year. **Evidence:** K.
- **Blank before founding:** 1900–1996.
- **No competition after founding:** none — contested every year to 2025.
- **Held but curtailed or unusual:** 2020: 22-game season in the Bradenton bubble.

#### WNBL

- **First season:** 1981. **Folder year convention:** calendar year. **Evidence:** K (VERIFY).
- **Blank before founding:** 1900–1980.
- **No competition after founding:** none — contested every year to 2025.
- **Notes:** Winter (calendar) seasons from 1981; moved to summer seasons around 2001-02 (VERIFY the switch year).

#### Women's FIBA World Cup

- **First season:** 1953. **Folder year convention:** year the event was played. **Evidence:** K.
- **Blank before founding:** 1900–1952.
- **No competition after founding:** 1954–1956, 1958, 1960–1963, 1965–1966, 1968–1970, 1972–1974, 1976–1978, 1980–1982, 1984–1985, 1987–1989, 1991–1993, 1995–1997, 1999–2001, 2003–2005, 2007–2009, 2011–2013, 2015–2017, 2019–2021, 2023–2025: No edition scheduled (not an annual event).

### Canadian Football

#### CFL

- **First season:** 1958. **Folder year convention:** calendar year. **Evidence:** K.
- **Blank before founding:** 1900–1957.
- **No competition after founding:** 2020: 2020 season cancelled (COVID-19).
- **Notes:** The CFL was formed in 1958; before that the IRFU ('Big Four') and WIFU played for the Grey Cup.

#### Grey Cup

- **First season:** 1909. **Folder year convention:** year the event was played. **Evidence:** W.
- **Blank before founding:** 1900–1908.
- **No competition after founding:** 1916–1918: Suspended (World War I); 1919: Not played (rules dispute); 2020: Cancelled (COVID-19).

#### Vanier Cup

- **First season:** 1965. **Folder year convention:** year the event was played. **Evidence:** K.
- **Blank before founding:** 1900–1964.
- **No competition after founding:** 2020: Cancelled (COVID-19).
- **Notes:** Canadian College Bowl 1965-1981; Vanier Cup name from 1982 (1967-? the Vanier Cup was the trophy; VERIFY naming).

### College Football

#### College Football Playoff

- **First season:** 2014. **Folder year convention:** season START year (2024-25 → 2024). **Evidence:** K.
- **Blank before founding:** 1900–2013.
- **No competition after founding:** none — contested every year to 2025.
- **Notes:** Folder = SEASON year (the 2014 season's playoff was played 1-12 Jan 2015). This differs from the bowl folders, which use the game date.

#### Cotton Bowl

- **First season:** 1937. **Folder year convention:** year the event was played. **Evidence:** K (VERIFY per year).
- **Blank before founding:** 1900–1936.
- **No competition after founding:** none — contested every year to 2025.
- **Notes:** Some calendar years have 0 or 2 Cotton Bowls after the game moved around 31 Dec/1 Jan (CFP era). File by game date and check each year.

#### Fiesta Bowl

- **First season:** 1971. **Folder year convention:** year the event was played. **Evidence:** K (VERIFY).
- **Blank before founding:** 1900–1970.
- **No competition after founding:** none — contested every year to 2025.
- **Notes:** Played in December 1971-1980, then moved to 1 January from 1982, so calendar 1981 has no Fiesta Bowl (VERIFY). File by game date.

#### NCAA Division I FBS

- **First season:** 1869. **Folder year convention:** season START year (2024-25 → 2024). **Evidence:** K.
- **Blank before founding:** none (existed before 1900).
- **No competition after founding:** none — contested every year to 2025.
- **Notes:** 'FBS' exists from 2006 (Division I-A 1978-2005). Before 1978 this folder can only mean major college football; say which teams count.

#### NCAA Division I FCS

- **First season:** 1978. **Folder year convention:** season START year (2024-25 → 2024). **Evidence:** K.
- **Blank before founding:** 1900–1977.
- **No competition after founding:** none — contested every year to 2025.
- **Held but curtailed or unusual:** 2020: 2020 season largely moved to spring 2021; championship played May 2021.

#### Orange Bowl

- **First season:** 1935. **Folder year convention:** year the event was played. **Evidence:** K.
- **Blank before founding:** 1900–1934.
- **No competition after founding:** none — contested every year to 2025.

#### Peach Bowl

- **First season:** 1968. **Folder year convention:** year the event was played. **Evidence:** K (VERIFY).
- **Blank before founding:** 1900–1967.
- **No competition after founding:** none — contested every year to 2025.
- **Notes:** December game from 1968; some calendar years have 0 or 2 games after date moves (VERIFY per year). File by game date.

#### Rose Bowl

- **First season:** 1902. **Folder year convention:** year the event was played. **Evidence:** K.
- **Blank before founding:** 1900–1901.
- **No competition after founding:** 1903–1915: Not played 1903-1915 (Tournament of Roses held chariot races instead).
- **Held but curtailed or unusual:** 1942: Played in Durham, North Carolina (wartime); 2021: Played in Arlington, Texas (COVID-19).

#### Sugar Bowl

- **First season:** 1935. **Folder year convention:** year the event was played. **Evidence:** K.
- **Blank before founding:** 1900–1934.
- **No competition after founding:** none — contested every year to 2025.

### Cricket One-Day Format

#### Marsh One-Day Cup

- **First season:** 1969. **Folder year convention:** season START year (2024-25 → 2024). **Evidence:** K.
- **Blank before founding:** 1900–1968.
- **No competition after founding:** none — contested every year to 2025.
- **Notes:** Australian domestic one-day competition from 1969-70 under many sponsor names.

#### Men's Champions Trophy

- **First season:** 1998. **Folder year convention:** year the event was played. **Evidence:** K.
- **Blank before founding:** 1900–1997.
- **No competition after founding:** 1999, 2001, 2003, 2005, 2007–2008, 2010–2012, 2014–2016, 2018–2024: No edition scheduled (not an annual event).

#### Men's Cricket World Cup

- **First season:** 1975. **Folder year convention:** year the event was played. **Evidence:** K.
- **Blank before founding:** 1900–1974.
- **No competition after founding:** 1976–1978, 1980–1982, 1984–1986, 1988–1991, 1993–1995, 1997–1998, 2000–2002, 2004–2006, 2008–2010, 2012–2014, 2016–2018, 2020–2022, 2024–2025: No edition scheduled (not an annual event).

#### Metro Bank One Day Cup

- **First season:** 1963. **Folder year convention:** calendar year. **Evidence:** K.
- **Blank before founding:** 1900–1962.
- **No competition after founding:** 2020: No one-day cup in 2020 (Bob Willis Trophy and T20 Blast only).
- **Notes:** English domestic one-day lineage: Gillette Cup 1963-80, NatWest 1981-2000, C&G 2001-06, Friends Provident 2007-09, CB40 2010-13 (40 overs), Royal London 2014-22, Metro Bank from 2023.

#### Vijay Hazare Trophy

- **First season:** 2002. **Folder year convention:** season START year (2024-25 → 2024). **Evidence:** W.
- **Blank before founding:** 1900–2001.
- **No competition after founding:** none — contested every year to 2025.
- **Scope:** Folder starts 1993 with the zonal predecessor; the Vijay Hazare Trophy national competition starts 2002-03.
- **Notes:** National knockout from 2002-03 (Wikipedia). The folder's 1993 start follows the earlier zonal Ranji one-day competition, which is a predecessor, not the Vijay Hazare Trophy.

#### Women's Cricket World Cup

- **First season:** 1973. **Folder year convention:** year the event was played. **Evidence:** K.
- **Blank before founding:** 1900–1972.
- **No competition after founding:** 1974–1977, 1979–1981, 1983–1987, 1989–1992, 1994–1996, 1998–1999, 2001–2004, 2006–2008, 2010–2012, 2014–2016, 2018–2021, 2023–2024: No edition scheduled (not an annual event).

### Cricket T20

#### Big Bash

- **First season:** 2011. **Folder year convention:** season START year (2024-25 → 2024). **Evidence:** K.
- **Blank before founding:** 1900–2010.
- **No competition after founding:** none — contested every year to 2025.

#### CPL

- **First season:** 2013. **Folder year convention:** calendar year. **Evidence:** K.
- **Blank before founding:** 1900–2012.
- **No competition after founding:** none — contested every year to 2025.

#### ILT20

- **First season:** 2023. **Folder year convention:** calendar year. **Evidence:** K.
- **Blank before founding:** 1900–2022.
- **No competition after founding:** none — contested every year to 2025.

#### IPL

- **First season:** 2008. **Folder year convention:** calendar year. **Evidence:** K.
- **Blank before founding:** 1900–2007.
- **No competition after founding:** none — contested every year to 2025.
- **Held but curtailed or unusual:** 2020: Played in the UAE (Sep-Nov); 2021: Suspended in May, completed in the UAE (Sep-Oct).

#### MLC

- **First season:** 2023. **Folder year convention:** calendar year. **Evidence:** K.
- **Blank before founding:** 1900–2022.
- **No competition after founding:** none — contested every year to 2025.

#### Men's T20 World Cup

- **First season:** 2007. **Folder year convention:** year the event was played. **Evidence:** K.
- **Blank before founding:** 1900–2006.
- **No competition after founding:** 2008, 2011, 2013, 2015, 2017–2020, 2023, 2025: No edition scheduled (not an annual event).

#### PSL

- **First season:** 2016. **Folder year convention:** calendar year. **Evidence:** K.
- **Blank before founding:** 1900–2015.
- **No competition after founding:** none — contested every year to 2025.
- **Held but curtailed or unusual:** 2020: Playoffs postponed from March to November 2020; 2021: Suspended in March, completed in Abu Dhabi in June.

#### SA20

- **First season:** 2023. **Folder year convention:** calendar year. **Evidence:** K.
- **Blank before founding:** 1900–2022.
- **No competition after founding:** none — contested every year to 2025.

#### The Hundred

- **First season:** 2021. **Folder year convention:** calendar year. **Evidence:** W.
- **Blank before founding:** 1900–2020.
- **No competition after founding:** none — contested every year to 2025.

#### WBBL

- **First season:** 2015. **Folder year convention:** season START year (2024-25 → 2024). **Evidence:** K.
- **Blank before founding:** 1900–2014.
- **No competition after founding:** none — contested every year to 2025.

#### WPL

- **First season:** 2023. **Folder year convention:** calendar year. **Evidence:** K.
- **Blank before founding:** 1900–2022.
- **No competition after founding:** none — contested every year to 2025.

#### Women's T20 World Cup

- **First season:** 2009. **Folder year convention:** year the event was played. **Evidence:** K.
- **Blank before founding:** 1900–2008.
- **No competition after founding:** 2011, 2013, 2015, 2017, 2019, 2021–2022, 2025: No edition scheduled (not an annual event).

### Cricket Tests

#### County Championship

- **First season:** 1890. **Folder year convention:** calendar year. **Evidence:** W.
- **Blank before founding:** none (existed before 1900).
- **No competition after founding:** 1915–1918: Not held (World War I); 1940–1945: Not held (World War II); 2020: Not held; replaced by the Bob Willis Trophy (COVID-19).

#### ICC World Test Championship

- **First season:** 2019. **Folder year convention:** season START year (2024-25 → 2024). **Evidence:** K.
- **Blank before founding:** 1900–2018.
- **No competition after founding:** none — contested every year to 2025.
- **Notes:** Two-year cycles: 2019-21, 2021-23, 2023-25, 2025-27. Tests in every year from 2019 belong to a cycle.

#### Plunket Shield

- **First season:** 1906. **Folder year convention:** season START year (2024-25 → 2024). **Evidence:** W (VERIFY 1944/1945).
- **Blank before founding:** 1900–1905.
- **No competition after founding:** 1915–1918: No competition (World War I); 1940–1944: Not contested (World War II).
- **VERIFY:** 1940, 1944–1945 (status not settled by the evidence read).
- **Notes:** Wikipedia lists '1915-18' and '1940-45' as not contested; the exact season-to-year mapping (is 1945-46 played?) needs checking (VERIFY).

#### Ranji Trophy

- **First season:** 1934. **Folder year convention:** season START year (2024-25 → 2024). **Evidence:** K.
- **Blank before founding:** 1900–1933.
- **No competition after founding:** 2020: 2020-21 season cancelled (COVID-19).

#### Sheffield Shield

- **First season:** 1892. **Folder year convention:** season START year (2024-25 → 2024). **Evidence:** W.
- **Blank before founding:** none (existed before 1900).
- **No competition after founding:** 1915–1918: Not contested (World War I); 1940–1945: Not contested (World War II).
- **Held but curtailed or unusual:** 2019: 2019-20 curtailed after nine rounds; no final (COVID-19).

#### The Ashes

- **First season:** 1882. **Folder year convention:** season START year (2024-25 → 2024). **Evidence:** K (VERIFY against the 'List of Ashes series' page).
- **Blank before founding:** none (existed before 1900).
- **No competition after founding:** 1900, 1904, 1906, 1908, 1910, 1913–1914, 1922–1923, 1925, 1927, 1929, 1931, 1933, 1935, 1937, 1947, 1949, 1951–1952, 1955, 1957, 1959–1960, 1963, 1966–1967, 1969, 1971, 1973, 1976, 1979–1980, 1983–1984, 1987–1988, 1991–1992, 1995–1996, 1999–2000, 2003–2004, 2007–2008, 2011–2012, 2014, 2016, 2018, 2020, 2022, 2024: No edition scheduled (not an annual event); 1915–1919: No Test cricket between England and Australia (World War I); 1939: No series (next series 1946-47; World War II); 1940–1945: No Test cricket between England and Australia (World War II).
- **Notes:** Ashes series are not annual. Folder = year the series STARTS (e.g. 2025-26 in Australia -> 2025). 2013 holds two series (England 2013 and Australia 2013-14). 1900 had no series. The 1976-77 Centenary Test and 1979-80 series were not for the Ashes.

### Hockey

#### Euro Hockey League

- **First season:** 2007. **Folder year convention:** season START year (2024-25 → 2024). **Evidence:** W.
- **Blank before founding:** 1900–2006.
- **No competition after founding:** none — contested every year to 2025.
- **Held but curtailed or unusual:** 2019: 2019-20 knockout stages cancelled (COVID-19).
- **VERIFY:** 2020 (status not settled by the evidence read).

#### FIH Hockey Pro League

- **First season:** 2019. **Folder year convention:** season START year (2024-25 → 2024). **Evidence:** K.
- **Blank before founding:** 1900–2018.
- **No competition after founding:** none — contested every year to 2025.
- **Notes:** 2019 (Jan-Jun 2019) then split seasons 2020-21, 2021-22 ... The 2020-21 season ran Jan 2020 - Jun 2021.

#### Hockey India League

- **First season:** 2013. **Folder year convention:** calendar year. **Evidence:** K.
- **Blank before founding:** 1900–2012.
- **No competition after founding:** 2018–2023: League dormant 2018-2023; 2025: No edition scheduled (not an annual event).
- **VERIFY:** 2025 (status not settled by the evidence read).
- **Notes:** Revived for 2024-25 (Dec 2024 - Feb 2025), filed under 2024.

#### Hoofdklasse

- **First season:** 1898. **Folder year convention:** season START year (2024-25 → 2024). **Evidence:** W.
- **Blank before founding:** none (existed before 1900).
- **No competition after founding:** 1901: 1901-02 not held; 1914: 1914-15 not held; 1939: 1939-40 not held; 1944: 1944-45 not held; 1946: 1946-47 not held; 1962: 1962-63 not held.
- **Held but curtailed or unusual:** 2019: 2019-20 cancelled with no champion (COVID-19).
- **VERIFY:** 2020 (status not settled by the evidence read).
- **Scope:** Folder populated only from 1973; the Dutch men's national championship list runs from 1898-99.
- **Notes:** Wikipedia's Dutch men's champions list runs from 1898-99; the folder starts at 1973. Decide whether the folder covers the national champions list or only the modern Hoofdklasse.

#### Men's FIH Hockey World Cup

- **First season:** 1971. **Folder year convention:** year the event was played. **Evidence:** K.
- **Blank before founding:** 1900–1970.
- **No competition after founding:** 1972, 1974, 1976–1977, 1979–1981, 1983–1985, 1987–1989, 1991–1993, 1995–1997, 1999–2001, 2003–2005, 2007–2009, 2011–2013, 2015–2017, 2019–2022, 2024–2025: No edition scheduled (not an annual event).

#### Summer Olympics

- **First season:** 1908. **Folder year convention:** year the event was played. **Evidence:** K.
- **Blank before founding:** 1900–1907.
- **No competition after founding:** 1909–1911, 1913–1915, 1917–1919, 1921–1923, 1925–1927, 1929–1931, 1933–1935, 1937–1939, 1941–1943, 1945–1947, 1949–1951, 1953–1955, 1957–1959, 1961–1963, 1965–1967, 1969–1971, 1973–1975, 1977–1979, 1981–1983, 1985–1987, 1989–1991, 1993–1995, 1997–1999, 2001–2003, 2005–2007, 2009–2011, 2013–2015, 2017–2019, 2022–2023, 2025: No edition scheduled (not an annual event); 1912, 1924: Hockey not on the Olympic programme; 1916: Olympic Games cancelled (World War I); 1940, 1944: Olympic Games cancelled (World War II); 2020: Tokyo 2020 postponed; played in 2021 (filed under 2021).
- **Notes:** Not held 1912 or 1924. Women's tournament from 1980. Tokyo 2020 PLAYED IN 2021.

#### Women's FIH Hockey World Cup

- **First season:** 1974. **Folder year convention:** year the event was played. **Evidence:** K.
- **Blank before founding:** 1900–1973.
- **No competition after founding:** 1975, 1977, 1979–1980, 1982, 1984–1985, 1987–1989, 1991–1993, 1995–1997, 1999–2001, 2003–2005, 2007–2009, 2011–2013, 2015–2017, 2019–2021, 2023–2025: No edition scheduled (not an annual event).

### Ice Hockey

#### AHL

- **First season:** 1936. **Folder year convention:** season START year (2024-25 → 2024). **Evidence:** W.
- **Blank before founding:** 1900–1935.
- **No competition after founding:** none — contested every year to 2025.
- **Held but curtailed or unusual:** 2019: 2019-20 season halted March 2020 (COVID-19); games before the stoppage exist; no Calder Cup; 2020: 2020-21 regular season played; no playoffs, no Calder Cup.
- **Notes:** IAHL 1936-40, AHL from 1940.

#### AIHL

- **First season:** 2000. **Folder year convention:** calendar year. **Evidence:** K.
- **Blank before founding:** 1900–1999.
- **No competition after founding:** 2020–2021: Season cancelled (COVID-19).

#### Czech Extraliga

- **First season:** 1993. **Folder year convention:** season START year (2024-25 → 2024). **Evidence:** K.
- **Blank before founding:** 1900–1992.
- **No competition after founding:** none — contested every year to 2025.
- **Held but curtailed or unusual:** 2019: Playoffs cancelled (COVID-19).

#### DEL

- **First season:** 1994. **Folder year convention:** season START year (2024-25 → 2024). **Evidence:** K.
- **Blank before founding:** 1900–1993.
- **No competition after founding:** none — contested every year to 2025.
- **Held but curtailed or unusual:** 2019: Playoffs cancelled (COVID-19).

#### ECHL

- **First season:** 1988. **Folder year convention:** season START year (2024-25 → 2024). **Evidence:** K.
- **Blank before founding:** 1900–1987.
- **No competition after founding:** none — contested every year to 2025.
- **Held but curtailed or unusual:** 2019: 2019-20 season halted March 2020 (COVID-19); games before the stoppage exist; no Kelly Cup; 2020: 2020-21 played with 13 teams (others opted out).

#### KHL

- **First season:** 2008. **Folder year convention:** season START year (2024-25 → 2024). **Evidence:** K.
- **Blank before founding:** 1900–2007.
- **No competition after founding:** none — contested every year to 2025.
- **Held but curtailed or unusual:** 2019: Playoffs cancelled (COVID-19); no Gagarin Cup.

#### Liiga

- **First season:** 1975. **Folder year convention:** season START year (2024-25 → 2024). **Evidence:** K.
- **Blank before founding:** 1900–1974.
- **No competition after founding:** none — contested every year to 2025.
- **Held but curtailed or unusual:** 2019: Playoffs cancelled (COVID-19).
- **Notes:** SM-liiga from 1975-76; Finnish championship series ran before that.

#### Men's IIHF World Championship

- **First season:** 1920. **Folder year convention:** year the event was played. **Evidence:** W.
- **Blank before founding:** 1900–1919.
- **No competition after founding:** 1921–1923, 1925–1927, 1929: No edition scheduled (not an annual event); 1940–1946: Not held (World War II); 1980: Not held in Olympic years 1980, 1984, 1988; 1984, 1988: Not held (Olympic year); 2020: Cancelled (COVID-19).
- **Notes:** The IIHF counts the 1920, 1924 and 1928 Olympic tournaments as World Championships (the folder starts at 1930).

#### NHL

- **First season:** 1917. **Folder year convention:** season START year (2024-25 → 2024). **Evidence:** W.
- **Blank before founding:** 1900–1916.
- **No competition after founding:** 2004: 2004-05 season cancelled (lockout).
- **Held but curtailed or unusual:** 1918: 1918-19: Stanley Cup Final abandoned (influenza), Cup not awarded; 2012: 2012-13 lockout-shortened (48 games); 2019: Paused March 2020; finished in Edmonton/Toronto bubbles.
- **Notes:** Folder first season 1917 = 1917-18 (START year). The cancelled season is 2004-05, which is the 2004 folder under that convention.

#### PWHL

- **First season:** 2023. **Folder year convention:** season START year (2024-25 → 2024). **Evidence:** K.
- **Blank before founding:** 1900–2022.
- **No competition after founding:** none — contested every year to 2025.
- **Notes:** Inaugural 2023-24 season began 1 January 2024.

#### SHL

- **First season:** 1975. **Folder year convention:** season START year (2024-25 → 2024). **Evidence:** K.
- **Blank before founding:** 1900–1974.
- **No competition after founding:** none — contested every year to 2025.
- **Held but curtailed or unusual:** 2019: Playoffs cancelled (COVID-19).
- **Notes:** Elitserien 1975-2013, SHL from 2013.

#### Swiss National League

- **First season:** 1937. **Folder year convention:** season START year (2024-25 → 2024). **Evidence:** K.
- **Blank before founding:** 1900–1936.
- **No competition after founding:** none — contested every year to 2025.
- **Held but curtailed or unusual:** 2019: Playoffs cancelled (COVID-19).

#### Winter Olympics

- **First season:** 1920. **Folder year convention:** year the event was played. **Evidence:** K.
- **Blank before founding:** 1900–1919.
- **No competition after founding:** 1921–1923, 1925–1927, 1929–1931, 1933–1935, 1937–1939, 1941–1943, 1945–1947, 1949–1951, 1953–1955, 1957–1959, 1961–1963, 1965–1967, 1969–1971, 1973–1975, 1977–1979, 1981–1983, 1985–1987, 1989–1991, 1993, 1995–1997, 1999–2001, 2003–2005, 2007–2009, 2011–2013, 2015–2017, 2019–2021, 2023–2025: No edition scheduled (not an annual event); 1940, 1944: Olympic Games cancelled (World War II).
- **Notes:** 1920 tournament was part of the Antwerp Summer Games. Women's tournament from 1998.

#### Women's IIHF World Championship

- **First season:** 1990. **Folder year convention:** year the event was played. **Evidence:** W.
- **Blank before founding:** 1900–1989.
- **No competition after founding:** 1991, 1993, 1995–1996: No edition scheduled (not an annual event); 1998, 2002, 2006, 2010: Not held (Olympic year); 2003: Cancelled (SARS outbreak, Beijing); 2014, 2018: Top level not held (Olympic year); 2020: Cancelled (COVID-19).

### Rugby League

#### Men's Rugby League World Cup

- **First season:** 1954. **Folder year convention:** year the event was played. **Evidence:** K.
- **Blank before founding:** 1900–1953.
- **No competition after founding:** 1955–1956, 1958–1959, 1961–1967, 1969, 1971, 1973–1974, 1976, 1978–1984, 1993–1994, 1996–1999, 2001–2007, 2009–2012, 2014–2016, 2018–2021, 2023–2025: No edition scheduled (not an annual event).
- **Notes:** 1985-88 and 1989-92 editions were played over several years (finals 1988 and 1992). The 2021 edition was postponed and PLAYED IN 2022.

#### NRL

- **First season:** 1908. **Folder year convention:** calendar year. **Evidence:** K.
- **Blank before founding:** 1900–1907.
- **No competition after founding:** none — contested every year to 2025.
- **Held but curtailed or unusual:** 1997: Two competitions: ARL and Super League (Australia); 2020: Paused Mar-May 2020, completed.
- **Notes:** NSWRFL 1908-94, ARL 1995-96 (Super League war: separate SL competition in 1997), NRL from 1998.

#### NRLW

- **First season:** 2018. **Folder year convention:** calendar year. **Evidence:** K.
- **Blank before founding:** 1900–2017.
- **No competition after founding:** none — contested every year to 2025.
- **Held but curtailed or unusual:** 2022: TWO seasons in calendar 2022: the delayed 2021 season (Feb-Apr 2022) and the 2022 season (Aug-Oct).

#### RFL Championship

- **First season:** 1895. **Folder year convention:** season START year (2024-25 → 2024). **Evidence:** K.
- **Blank before founding:** none (existed before 1900).
- **No competition after founding:** not assessed until the folder's lineage is decided (see Scope).
- **Scope:** Scope undecided: second-tier Championship (2003-) or the top-flight Championship lineage (1895-1996). Statuses not compared until the scope is fixed.
- **Notes:** AMBIGUOUS FOLDER: the 'RFL Championship' is the second tier from 2003. The folder starts in 1900, which only fits the Northern Union / RFL top-flight Championship lineage (1895-1996). Decide which lineage this folder records before populating.

#### State of Origin

- **First season:** 1980. **Folder year convention:** calendar year. **Evidence:** K.
- **Blank before founding:** 1900–1979.
- **No competition after founding:** none — contested every year to 2025.
- **Held but curtailed or unusual:** 2020: Played in November 2020.
- **Notes:** 1980-81 single matches; three-game series from 1982.

#### Super League

- **First season:** 1996. **Folder year convention:** calendar year. **Evidence:** K.
- **Blank before founding:** 1900–1995.
- **No competition after founding:** none — contested every year to 2025.
- **Held but curtailed or unusual:** 2020: Disrupted by COVID-19; finished with a play-off, league table on win percentage.

#### Women's Rugby League World Cup

- **First season:** 2000. **Folder year convention:** year the event was played. **Evidence:** K.
- **Blank before founding:** 1900–1999.
- **No competition after founding:** 2001–2002, 2004–2007, 2009–2012, 2014–2016, 2018–2021, 2023–2025: No edition scheduled (not an annual event).
- **Notes:** The 2021 edition was postponed and PLAYED IN 2022.

#### Women's Super League

- **First season:** 2017. **Folder year convention:** calendar year. **Evidence:** K.
- **Blank before founding:** 1900–2016.
- **No competition after founding:** 2020: Season cancelled (COVID-19).

### Rugby Union

#### Champions Cup

- **First season:** 1995. **Folder year convention:** season START year (2024-25 → 2024). **Evidence:** K.
- **Blank before founding:** 1900–1994.
- **No competition after founding:** none — contested every year to 2025.
- **Held but curtailed or unusual:** 2019: Knockouts completed Sep-Oct 2020.
- **Notes:** Heineken Cup 1995-2014, Champions Cup from 2014-15.

#### EPCR Challenge Cup

- **First season:** 1996. **Folder year convention:** season START year (2024-25 → 2024). **Evidence:** K.
- **Blank before founding:** 1900–1995.
- **No competition after founding:** none — contested every year to 2025.
- **Held but curtailed or unusual:** 2019: Knockouts completed Sep-Oct 2020.

#### Farah Palmer Cup

- **First season:** 1999. **Folder year convention:** calendar year. **Evidence:** K (VERIFY).
- **Blank before founding:** 1900–1998.
- **No competition after founding:** none — contested every year to 2025.
- **Notes:** Women's provincial championship from 1999; named Farah Palmer Cup from 2016. Check for years with no competition before 2016 (VERIFY).

#### League One

- **First season:** 2003. **Folder year convention:** season START year (2024-25 → 2024). **Evidence:** K (VERIFY year mapping).
- **Blank before founding:** 1900–2002.
- **No competition after founding:** none — contested every year to 2025.
- **Held but curtailed or unusual:** 2020: Top League 2020 cancelled after six rounds (COVID-19).
- **Notes:** Top League 2003-04 to 2021, Japan Rugby League One from 2022. Season timing changed several times (autumn-winter to January-May); map each season to one folder explicitly.

#### Men's Rugby World Cup

- **First season:** 1987. **Folder year convention:** year the event was played. **Evidence:** K.
- **Blank before founding:** 1900–1986.
- **No competition after founding:** 1988–1990, 1992–1994, 1996–1998, 2000–2002, 2004–2006, 2008–2010, 2012–2014, 2016–2018, 2020–2022, 2024–2025: No edition scheduled (not an annual event).

#### Premiership

- **First season:** 1987. **Folder year convention:** season START year (2024-25 → 2024). **Evidence:** K.
- **Blank before founding:** 1900–1986.
- **No competition after founding:** none — contested every year to 2025.
- **Held but curtailed or unusual:** 2019: Resumed Aug 2020, final Oct 2020.

#### Premiership Women's Rugby

- **First season:** 2017. **Folder year convention:** season START year (2024-25 → 2024). **Evidence:** K.
- **Blank before founding:** 1900–2016.
- **No competition after founding:** none — contested every year to 2025.
- **Held but curtailed or unusual:** 2019: 2019-20 halted March 2020 and cancelled with no champion (COVID-19); games before the stoppage exist.

#### Six Nations

- **First season:** 1883. **Folder year convention:** calendar year. **Evidence:** K.
- **Blank before founding:** none (existed before 1900).
- **No competition after founding:** 1915–1919: Not held (World War I; 1919 had unofficial Victory internationals); 1940–1946: Not held (World War II; 1946 had unofficial Victory internationals).
- **Held but curtailed or unusual:** 1972: Incomplete (Scotland and Wales did not play in Ireland); 2020: Final round played October 2020.
- **Notes:** Home Nations 1883-1909, Five Nations 1910-1931 and 1947-1999, Home Nations 1932-1939, Six Nations from 2000.

#### Super Rugby Pacific

- **First season:** 1996. **Folder year convention:** calendar year. **Evidence:** K.
- **Blank before founding:** 1900–1995.
- **No competition after founding:** none — contested every year to 2025.
- **Held but curtailed or unusual:** 2020: Suspended after 7 rounds (March 2020); replaced by Super Rugby Aotearoa and Super Rugby AU; 2021: Super Rugby Aotearoa, AU and Trans-Tasman.

#### The Rugby Championship

- **First season:** 1996. **Folder year convention:** calendar year. **Evidence:** K.
- **Blank before founding:** 1900–1995.
- **No competition after founding:** none — contested every year to 2025.
- **Held but curtailed or unusual:** 2020: Tri Nations in Australia (Argentina, Australia, New Zealand).
- **Notes:** Tri Nations 1996-2011, Rugby Championship from 2012.

#### Top 14

- **First season:** 1892. **Folder year convention:** season END year (2024-25 → 2025). **Evidence:** W (VERIFY WWII seasons).
- **Blank before founding:** none (existed before 1900).
- **No competition after founding:** 1915–1919: Championship suspended (World War I); Coupe de l'Espérance played instead.
- **Held but curtailed or unusual:** 2020: 2019-20 halted March 2020 and cancelled without a champion (COVID-19); games before the stoppage exist.
- **Notes:** French championship from 1892. Wikipedia says the championship was also suspended in World War II; the exact seasons need checking (VERIFY).

#### United Rugby Championship

- **First season:** 2001. **Folder year convention:** season START year (2024-25 → 2024). **Evidence:** K.
- **Blank before founding:** 1900–2000.
- **No competition after founding:** none — contested every year to 2025.
- **Held but curtailed or unusual:** 2019: Resumed Aug 2020 with a truncated play-off.
- **Notes:** Celtic League 2001-2011, Pro12, Pro14, URC from 2021-22.

#### Women's Rugby World Cup

- **First season:** 1991. **Folder year convention:** year the event was played. **Evidence:** K.
- **Blank before founding:** 1900–1990.
- **No competition after founding:** 1992–1993, 1995–1997, 1999–2001, 2003–2005, 2007–2009, 2011–2013, 2015–2016, 2018–2021, 2023–2024: No edition scheduled (not an annual event).
- **Notes:** The 2021 edition was postponed and PLAYED IN 2022.

#### Women's Six Nations

- **First season:** 1996. **Folder year convention:** calendar year. **Evidence:** W.
- **Blank before founding:** 1900–1995.
- **No competition after founding:** none — contested every year to 2025.
- **Held but curtailed or unusual:** 2020: Not completed (three fixtures cancelled, COVID-19); 2021: One-off pool format; championship listed as not contested.

### Soccer

#### A-League Men

- **First season:** 2005. **Folder year convention:** season START year (2024-25 → 2024). **Evidence:** K.
- **Blank before founding:** 1900–2004.
- **No competition after founding:** none — contested every year to 2025.
- **Held but curtailed or unusual:** 2019: Suspended Mar 2020, completed Aug 2020.

#### A-League Women

- **First season:** 2008. **Folder year convention:** season START year (2024-25 → 2024). **Evidence:** K.
- **Blank before founding:** 1900–2007.
- **No competition after founding:** none — contested every year to 2025.

#### AFC Champions League

- **First season:** 1967. **Folder year convention:** year the event was played. **Evidence:** K (VERIFY).
- **Blank before founding:** 1900–1966.
- **No competition after founding:** 1968: No edition (VERIFY); 1972: 1972 edition cancelled; competition then suspended; 1973–1984: Competition suspended 1973-1984.
- **VERIFY:** 1968 (status not settled by the evidence read).
- **Notes:** Asian Champion Club Tournament 1967-1971, not held 1972-1984, Asian Club Championship 1985/86-2001/02, AFC Champions League from 2002-03 (calendar 2003-2022, split seasons again from 2023-24). Early-edition years need checking (VERIFY).

#### Bundesliga

- **First season:** 1963. **Folder year convention:** season START year (2024-25 → 2024). **Evidence:** K.
- **Blank before founding:** 1900–1962.
- **No competition after founding:** none — contested every year to 2025.

#### CAF Champions League

- **First season:** 1964. **Folder year convention:** calendar year. **Evidence:** K.
- **Blank before founding:** 1900–1963.
- **No competition after founding:** 1965: Not held.

#### CONCACAF Champions Cup

- **First season:** 1962. **Folder year convention:** calendar year. **Evidence:** W.
- **Blank before founding:** 1900–1961.
- **No competition after founding:** 1964–1966, 2001: Not held or not completed.
- **Notes:** CONCACAF Champions' Cup 1962-2008, CONCACAF Champions League 2008-09 to 2023, Champions Cup from 2024.

#### CONCACAF Gold Cup

- **First season:** 1991. **Folder year convention:** year the event was played. **Evidence:** K.
- **Blank before founding:** 1900–1990.
- **No competition after founding:** 1992, 1994–1995, 1997, 1999, 2001, 2004, 2006, 2008, 2010, 2012, 2014, 2016, 2018, 2020, 2022, 2024: No edition scheduled (not an annual event).
- **Notes:** The CONCACAF Championship (1963-1989) is the predecessor, not the Gold Cup.

#### CONMEBOL Libertadores

- **First season:** 1960. **Folder year convention:** calendar year. **Evidence:** K.
- **Blank before founding:** 1900–1959.
- **No competition after founding:** none — contested every year to 2025.

#### Copa America

- **First season:** 1916. **Folder year convention:** year the event was played. **Evidence:** K.
- **Blank before founding:** 1900–1915.
- **No competition after founding:** 1918: Postponed (influenza epidemic); 1928, 1930–1934, 1936, 1938, 1940, 1943–1944, 1948, 1950–1952, 1954, 1958, 1960–1962, 1964–1966, 1968–1974, 1976–1978, 1980–1982, 1984–1986, 1988, 1990, 1992, 1994, 1996, 1998, 2000, 2002–2003, 2005–2006, 2008–2010, 2012–2014, 2017–2018, 2020, 2022–2023, 2025: No edition scheduled (not an annual event).
- **Notes:** 1959 had two editions (Argentina and Ecuador).

#### FIFA Club World Cup

- **First season:** 2000. **Folder year convention:** year the event was played. **Evidence:** K.
- **Blank before founding:** 1900–1999.
- **No competition after founding:** 2001–2004, 2024: No edition scheduled (not an annual event).
- **Notes:** Not held 2001-2004 or 2024. The 2020 edition was played in Feb 2021 and the 2021 edition in Feb 2022: choose edition-name or played-year filing.

#### Frauen-Bundesliga

- **First season:** 1990. **Folder year convention:** season START year (2024-25 → 2024). **Evidence:** K.
- **Blank before founding:** 1900–1989.
- **No competition after founding:** none — contested every year to 2025.

#### La Liga

- **First season:** 1929. **Folder year convention:** season START year (2024-25 → 2024). **Evidence:** K.
- **Blank before founding:** 1900–1928.
- **No competition after founding:** 1936: 1936-37 not held (Spanish Civil War); 1937: 1937-38 not held (Spanish Civil War); 1938: 1938-39 not held (Spanish Civil War).
- **Notes:** 1929 = the first season (Feb-Jun 1929); 1929-30 is the 1929 folder too under the start-year rule, so decide how to file the two. La Liga resumed in 1939-40 (folder 1939).

#### Liga F

- **First season:** 1988. **Folder year convention:** season START year (2024-25 → 2024). **Evidence:** K.
- **Blank before founding:** 1900–1987.
- **No competition after founding:** none — contested every year to 2025.
- **Held but curtailed or unusual:** 2019: Curtailed; Barcelona awarded the title.

#### Ligue 1

- **First season:** 1932. **Folder year convention:** season START year (2024-25 → 2024). **Evidence:** K.
- **Blank before founding:** 1900–1931.
- **No competition after founding:** 1939–1944: Wartime championships 1939-40 to 1944-45 are not official.

#### Major League Soccer

- **First season:** 1996. **Folder year convention:** calendar year. **Evidence:** K.
- **Blank before founding:** 1900–1995.
- **No competition after founding:** none — contested every year to 2025.
- **Held but curtailed or unusual:** 2020: MLS is Back tournament plus a shortened season.

#### Men's AFC Asian Cup

- **First season:** 1956. **Folder year convention:** year the event was played. **Evidence:** K.
- **Blank before founding:** 1900–1955.
- **No competition after founding:** 1957–1959, 1961–1963, 1965–1967, 1969–1971, 1973–1975, 1977–1979, 1981–1983, 1985–1987, 1989–1991, 1993–1995, 1997–1999, 2001–2003, 2005–2006, 2008–2010, 2012–2014, 2016–2018, 2020–2023, 2025: No edition scheduled (not an annual event).
- **Scope:** Folder files by edition name (e.g. 2023); the 2023 edition was played in 2024.
- **Notes:** The '2023' Asian Cup was PLAYED IN January-February 2024 in Qatar.

#### Men's Africa Cup of Nations

- **First season:** 1957. **Folder year convention:** year the event was played. **Evidence:** K.
- **Blank before founding:** 1900–1956.
- **No competition after founding:** 1958, 1960–1961, 1964, 1966–1967, 1969, 1971, 1973, 1975, 1977, 1979, 1981, 1983, 1985, 1987, 1989, 1991, 1993, 1995, 1997, 1999, 2001, 2003, 2005, 2007, 2009, 2011, 2014, 2016, 2018, 2020–2021, 2023: No edition scheduled (not an annual event).
- **Scope:** Folder files by edition name; the 2021 and 2023 editions were played in 2022 and 2024.
- **Notes:** The 2021 edition was PLAYED IN Jan-Feb 2022, the 2023 edition in Jan-Feb 2024, and the 2025 edition from 21 Dec 2025 into Jan 2026.

#### Men's FIFA World Cup

- **First season:** 1930. **Folder year convention:** year the event was played. **Evidence:** K.
- **Blank before founding:** 1900–1929.
- **No competition after founding:** 1931–1933, 1935–1937, 1939–1941, 1943–1945, 1947–1949, 1951–1953, 1955–1957, 1959–1961, 1963–1965, 1967–1969, 1971–1973, 1975–1977, 1979–1981, 1983–1985, 1987–1989, 1991–1993, 1995–1997, 1999–2001, 2003–2005, 2007–2009, 2011–2013, 2015–2017, 2019–2021, 2023–2025: No edition scheduled (not an annual event); 1942, 1946: Not held (World War II).

#### Men's UEFA European Championship

- **First season:** 1960. **Folder year convention:** year the event was played. **Evidence:** K.
- **Blank before founding:** 1900–1959.
- **No competition after founding:** 1961–1963, 1965–1967, 1969–1971, 1973–1975, 1977–1979, 1981–1983, 1985–1987, 1989–1991, 1993–1995, 1997–1999, 2001–2003, 2005–2007, 2009–2011, 2013–2015, 2017–2020, 2022–2023, 2025: No edition scheduled (not an annual event).
- **Notes:** EURO 2020 was PLAYED IN 2021.

#### NWSL

- **First season:** 2013. **Folder year convention:** calendar year. **Evidence:** K.
- **Blank before founding:** 1900–2012.
- **No competition after founding:** none — contested every year to 2025.
- **Held but curtailed or unusual:** 2020: Regular season cancelled; Challenge Cup and Fall Series only.

#### Premier League

- **First season:** 1992. **Folder year convention:** season START year (2024-25 → 2024). **Evidence:** K.
- **Blank before founding:** 1900–1991.
- **No competition after founding:** none — contested every year to 2025.
- **Notes:** The Premier League begins 1992-93. worldfootball.net also labels the pre-1992 First Division 'Premier League' in its URLs; do not import those into this folder unless the folder is meant to cover the English top flight.

#### Premiere Ligue

- **First season:** 1974. **Folder year convention:** season START year (2024-25 → 2024). **Evidence:** K.
- **Blank before founding:** 1900–1973.
- **No competition after founding:** none — contested every year to 2025.
- **Held but curtailed or unusual:** 2019: Curtailed (COVID-19).

#### Serie A

- **First season:** 1898. **Folder year convention:** season START year (2024-25 → 2024). **Evidence:** W.
- **Blank before founding:** none (existed before 1900).
- **No competition after founding:** 1915–1918: Not held (World War I); 1943: 1943-44 Campionato Alta Italia is not an official championship; 1944: 1944-45 not held.
- **Notes:** Serie A single table from 1929-30; earlier Italian championships used regional groups. 1945-46 (folder 1945) was contested (Divisione Nazionale) and is official.

#### Serie A Femminile

- **First season:** 1968. **Folder year convention:** season START year (2024-25 → 2024). **Evidence:** K.
- **Blank before founding:** 1900–1967.
- **No competition after founding:** none — contested every year to 2025.
- **Held but curtailed or unusual:** 2019: Curtailed (COVID-19).

#### Summer Olympics

- **First season:** 1900. **Folder year convention:** year the event was played. **Evidence:** K.
- **Blank before founding:** none (existed before 1900).
- **No competition after founding:** 1901–1903, 1905–1907, 1909–1911, 1913–1915, 1917–1919, 1921–1923, 1925–1927, 1929–1931, 1933–1935, 1937–1939, 1941–1943, 1945–1947, 1949–1951, 1953–1955, 1957–1959, 1961–1963, 1965–1967, 1969–1971, 1973–1975, 1977–1979, 1981–1983, 1985–1987, 1989–1991, 1993–1995, 1997–1999, 2001–2003, 2005–2007, 2009–2011, 2013–2015, 2017–2019, 2022–2023, 2025: No edition scheduled (not an annual event); 1916: Olympic Games cancelled (World War I); 1932: Football not on the 1932 Olympic programme; 1940, 1944: Olympic Games cancelled (World War II); 2020: Tokyo 2020 postponed; played in 2021 (filed under 2021).
- **Notes:** The IOC counts the 1900 and 1904 tournaments. Not held 1932. Women's tournament from 1996. Tokyo 2020 PLAYED IN 2021.

#### UEFA Champions League

- **First season:** 1955. **Folder year convention:** season START year (2024-25 → 2024). **Evidence:** K.
- **Blank before founding:** 1900–1954.
- **No competition after founding:** none — contested every year to 2025.

#### UEFA Conference League

- **First season:** 2021. **Folder year convention:** season START year (2024-25 → 2024). **Evidence:** K.
- **Blank before founding:** 1900–2020.
- **No competition after founding:** none — contested every year to 2025.

#### UEFA Europa League

- **First season:** 1971. **Folder year convention:** season START year (2024-25 → 2024). **Evidence:** K.
- **Blank before founding:** 1900–1970.
- **No competition after founding:** none — contested every year to 2025.
- **Notes:** UEFA Cup from 1971-72 (the Inter-Cities Fairs Cup 1955-1971 is a predecessor).

#### WSL

- **First season:** 2011. **Folder year convention:** calendar year. **Evidence:** K.
- **Blank before founding:** 1900–2010.
- **No competition after founding:** none — contested every year to 2025.
- **Held but curtailed or unusual:** 2019: 2019-20 curtailed; decided on points per game.
- **Notes:** Calendar seasons 2011-2016, Spring Series 2017, then split seasons from 2017-18.

#### Women's FIFA World Cup

- **First season:** 1991. **Folder year convention:** year the event was played. **Evidence:** K.
- **Blank before founding:** 1900–1990.
- **No competition after founding:** 1992–1994, 1996–1998, 2000–2002, 2004–2006, 2008–2010, 2012–2014, 2016–2018, 2020–2022, 2024–2025: No edition scheduled (not an annual event).

#### Women's UEFA European Championship

- **First season:** 1984. **Folder year convention:** year the event was played. **Evidence:** K.
- **Blank before founding:** 1900–1983.
- **No competition after founding:** 1985–1986, 1988, 1990, 1992, 1994, 1996, 1998–2000, 2002–2004, 2006–2008, 2010–2012, 2014–2016, 2018–2021, 2023–2024: No edition scheduled (not an annual event).
- **Notes:** EURO 2021 was postponed and PLAYED IN 2022.

### State Level AFL

#### NTFL

- **First season:** 1916. **Folder year convention:** season START year (2024-25 → 2024). **Evidence:** W (VERIFY).
- **Blank before founding:** 1900–1915.
- **No competition after founding:** 1942–1945: Not held (World War II; Darwin evacuated); 1974: 1974-75 season abandoned (Cyclone Tracy).
- **Notes:** NTFL is a wet-season (Oct-Mar) competition; check the founding season and any other recesses (VERIFY).

#### QAFL

- **First season:** 1904. **Folder year convention:** calendar year. **Evidence:** W.
- **Blank before founding:** 1900–1903.
- **No competition after founding:** 1915–1918: No competition (World War I); 1919: No competition (influenza pandemic).
- **Notes:** First premiership listed is 1904 (shared). Premiers were decided in every season 1940-1949, so World War II was played. The competition changed names and structure several times (QFL, QANFL, QAFL, NEAFL era, QAFL).

#### SANFL

- **First season:** 1877. **Folder year convention:** calendar year. **Evidence:** K (VERIFY).
- **Blank before founding:** none (existed before 1900).
- **No competition after founding:** 1916–1918: Recess (World War I); an unofficial patriotic league was played.
- **Held but curtailed or unusual:** 1942: Wartime merged-club competition (premierships recognised); 1943: Wartime merged-club competition; 1944: Wartime merged-club competition.
- **Notes:** The folder marks 1942-1944 inactive, but the SANFL recognises the merged-club wartime premierships (VERIFY).

#### SANFLW

- **First season:** 2017. **Folder year convention:** calendar year. **Evidence:** K.
- **Blank before founding:** 1900–2016.
- **No competition after founding:** none — contested every year to 2025.

#### TSL

- **First season:** 1879. **Folder year convention:** calendar year. **Evidence:** W (VERIFY WWI).
- **Blank before founding:** none (existed before 1900).
- **No competition after founding:** 1942–1944: Recess (World War II).
- **VERIFY:** 1916–1918 (status not settled by the evidence read).
- **Notes:** AMBIGUOUS FOLDER: the Tasmanian State League existed 1986-2000 and from 2009; the Hobart-based TFL is the pre-1986 lineage. Wikipedia confirms the TFL recess 1942-1944; World War I recess years need checking (VERIFY).

#### VFL

- **First season:** 1877. **Folder year convention:** calendar year. **Evidence:** W.
- **Blank before founding:** none (existed before 1900).
- **No competition after founding:** 1916–1917: Season not contested (World War I); 1942–1944: Season not contested (World War II); 2020: Season not contested (COVID-19).
- **Held but curtailed or unusual:** 2021: Finals not contested; no premiership awarded (COVID-19).
- **Notes:** VFA 1877-1995, VFL from 1996.

#### VFLW

- **First season:** 2016. **Folder year convention:** calendar year. **Evidence:** K.
- **Blank before founding:** 1900–2015.
- **No competition after founding:** 2020: Season cancelled (COVID-19).

#### WAFL

- **First season:** 1885. **Folder year convention:** calendar year. **Evidence:** W; WAFL FootyFacts 1917 results page lists scored games (2026-09-30).
- **Blank before founding:** none (existed before 1900).
- **No competition after founding:** none — contested every year to 2025.
- **Held but curtailed or unusual:** 1942: Under-age competition; 1943: Under-age competition; 1944: Under-age competition.
- **Notes:** WAFA/WAFL played through World War I; 1942-1944 were under-age (under-18) competitions whose premierships have equal status in official records.

#### WAFLW

- **First season:** 2019. **Folder year convention:** calendar year. **Evidence:** K.
- **Blank before founding:** 1900–2018.
- **No competition after founding:** none — contested every year to 2025.

### Tennis

#### ATP/London

- **First season:** 1877. **Folder year convention:** calendar year. **Evidence:** W.
- **Blank before founding:** none (existed before 1900).
- **No competition after founding:** 1915–1918: No competition (World War I); 1940–1945: No competition (World War II); 2020: No competition (COVID-19).
- **Notes:** Folder labelled ATP, but pre-1968 events are the amateur Wimbledon Championships (the ATP was founded 1972).

#### ATP/Melbourne

- **First season:** 1905. **Folder year convention:** calendar year. **Evidence:** W.
- **Blank before founding:** 1900–1904.
- **No competition after founding:** 1916–1918: No competition (World War I); 1941–1945: No competition (World War II); 1986: No competition (moved from December to January).
- **Held but curtailed or unusual:** 1977: Two editions (January and December 1977).
- **Notes:** Not always in Melbourne before 1972 (Sydney, Adelaide, Brisbane, Perth, and New Zealand in 1906 and 1912).

#### ATP/New York

- **First season:** 1881. **Folder year convention:** calendar year. **Evidence:** W.
- **Blank before founding:** none (existed before 1900).
- **No competition after founding:** none — contested every year to 2025.
- **Held but curtailed or unusual:** 1917: Held as the National Patriotic Tournament.
- **Notes:** Played every year. Newport, Rhode Island 1881-1914; Forest Hills 1915-1920 and 1924-1977; Germantown, Philadelphia 1921-1923; Flushing Meadows from 1978.

#### ATP/Paris

- **First season:** 1925. **Folder year convention:** calendar year. **Evidence:** W.
- **Blank before founding:** 1900–1924.
- **No competition after founding:** 1940: No competition (World War II); 1941–1945: Tournoi de France 1941-1945 is not officially recognised.
- **Notes:** French Championships from 1891 but closed to members of French clubs until 1924; international from 1925. Not held 1915-1919.

#### WTA/London

- **First season:** 1884. **Folder year convention:** calendar year. **Evidence:** W.
- **Blank before founding:** none (existed before 1900).
- **No competition after founding:** 1915–1918: No competition (World War I); 1940–1945: No competition (World War II); 2020: No competition (COVID-19).
- **Scope:** Folder populated only from 1973 (WTA founding); the women's championship itself runs from 1884.
- **Notes:** Women's singles from 1884. The folder starts in 1973 (WTA founding) even though the championship existed.

#### WTA/Melbourne

- **First season:** 1922. **Folder year convention:** calendar year. **Evidence:** K (WTA list not read: 429).
- **Blank before founding:** 1900–1921.
- **No competition after founding:** 1941–1945: No competition (World War II); 1986: No competition (date change).
- **Held but curtailed or unusual:** 1977: Two editions (January and December 1977).
- **Scope:** Folder populated only from 1973; the women's championship runs from 1922.
- **Notes:** Women's singles from 1922.

#### WTA/New York

- **First season:** 1887. **Folder year convention:** calendar year. **Evidence:** K (WTA list not read: 429).
- **Blank before founding:** none (existed before 1900).
- **No competition after founding:** none — contested every year to 2025.
- **Scope:** Folder populated only from 1973; the women's championship runs from 1887.
- **Notes:** Women's singles from 1887; held every year (Philadelphia until 1920).

#### WTA/Paris

- **First season:** 1925. **Folder year convention:** calendar year. **Evidence:** W.
- **Blank before founding:** 1900–1924.
- **No competition after founding:** 1940: No competition (World War II); 1941–1945: Tournoi de France 1941-1945 not recognised.
- **Scope:** Folder populated only from 1973; the women's championship runs from 1897 (international from 1925).
- **Notes:** Women's singles from 1897 (closed to French club members until 1924).

## 5. Folder statuses that disagree with the record

Compared on 2026-09-30 against the `INACTIVE`/active status written in each `<Year>/COACHES.md`. Uncertain years and scope questions are excluded (listed in §4 as VERIFY/Scope). **These folders were not changed**: apply fixes deliberately.

| Competition | Marked INACTIVE but the competition was held | Marked INACTIVE but held in a curtailed or unusual form (games exist) | Marked active but no competition was held |
|---|---|---|---|
| AFL/AFL Grand Final | 1916–1917 | — | — |
| Baseball/Caribbean Series and Winter Leagues | — | — | 1981 |
| Baseball/Minor Leagues | 1900 | — | — |
| Basketball/EuroBasket | 2025 | — | — |
| Basketball/EuroLeague | — | 2020 | — |
| Basketball/EuroLeague Women | 2020 | — | — |
| Basketball/FIBA AmeriCup | 2025 | — | — |
| Basketball/FIBA Asia Cup | 2025 | — | — |
| Basketball/Greek Basket League | — | — | 1930–1933, 1937, 1940, 1947, 1951, 1955 |
| Basketball/Serie A | — | — | 1929 |
| Basketball/VTB United League | 2020 | — | — |
| Cricket One-Day Format/Men's Champions Trophy | 2025 | — | — |
| Cricket One-Day Format/Vijay Hazare Trophy | — | — | 1993–2001 |
| Cricket One-Day Format/Women's Cricket World Cup | 2025 | — | — |
| Cricket Tests/County Championship | — | — | 2020 |
| Cricket Tests/The Ashes | — | — | 1900, 1904, 1906, 1908, 1910, 1913–1914, 1922–1923, 1925, 1927, 1929, 1931, 1933, 1935, 1937, 1947, 1949, 1951–1952, 1955, 1957, 1959–1960, 1963, 1966–1967, 1969, 1971, 1973, 1976, 1979–1980, 1983–1984, 1987–1988, 1991–1992, 1995–1996, 1999–2000, 2003–2004, 2007–2008, 2011–2012, 2014, 2016, 2018, 2020, 2022, 2024 |
| Ice Hockey/AHL | — | 2020 | — |
| Ice Hockey/Czech Extraliga | 2020 | — | — |
| Ice Hockey/DEL | 2020 | — | — |
| Ice Hockey/ECHL | — | 2020 | — |
| Ice Hockey/KHL | 2020 | — | — |
| Ice Hockey/Liiga | 2020 | — | — |
| Ice Hockey/Men's IIHF World Championship | 1920, 1924, 1928 | — | 1980, 1984, 1988 |
| Ice Hockey/NHL | 2005 | — | 2004 |
| Ice Hockey/SHL | 2020 | — | — |
| Ice Hockey/Swiss National League | 2020 | — | — |
| Ice Hockey/Women's IIHF World Championship | 2005 | — | — |
| Rugby League/Men's Rugby League World Cup | 1985–1987, 1989–1991 | — | — |
| Rugby Union/League One | — | 2020 | — |
| Rugby Union/Premiership Women's Rugby | 2020 | — | — |
| Rugby Union/Super Rugby Pacific | — | 2020 | — |
| Rugby Union/Top 14 | — | 2020 | — |
| Rugby Union/Women's Rugby World Cup | 2025 | — | — |
| Soccer/CONCACAF Champions Cup | — | — | 1964–1966, 2001 |
| Soccer/La Liga | 1939 | — | — |
| Soccer/Men's AFC Asian Cup | 2024 | — | 2023 |
| Soccer/Men's Africa Cup of Nations | 2022, 2024–2025 | — | 2021, 2023 |
| Soccer/Serie A | 1945 | — | — |
| Soccer/Serie A Femminile | 2020 | — | — |
| Soccer/Summer Olympics | 1900, 1904 | — | — |
| Soccer/Women's UEFA European Championship | 2025 | — | — |
| State Level AFL/NTFL | — | — | 1974 |
| State Level AFL/QAFL | 1942–1944 | — | 1903, 1915, 1919 |
| State Level AFL/SANFL | — | 1942–1944 | — |
| State Level AFL/WAFL | 1916–1918 | — | — |
| Tennis/ATP/Melbourne | 1915, 1940 | — | 1986 |
| Tennis/ATP/New York | 1915–1916, 1918 | 1917 | — |
| Tennis/WTA/Melbourne | — | — | 1986 |

**48 of 172 competition folders** have at least one status that disagrees with the record. The main patterns:

- **2025 events marked inactive.** EuroBasket, FIBA AmeriCup, FIBA Asia Cup, the ICC Champions Trophy, the Women's Cricket World Cup, the Women's Rugby World Cup, Women's EURO and AFCON 2025 all took place in 2025.
- **Split seasons filed one year late.** Seasons cancelled in 2019-20 are marked in the 2020 folder, which under the start-year rule is the 2020-21 season that was played (ice hockey leagues, EuroLeague Women, VTB, Serie A Femminile, Premiership Women's Rugby). The NHL lockout season 2004-05 is marked in 2005 while 2004 is active.
- **Curtailed treated as not held.** EuroLeague 2019-20, Super Rugby 2020, Top League 2020, Top 14 2019-20, the AHL and ECHL 2020-21, SANFL 1942-44: games were played and should be logged.
- **War years wrong.** VFL Grand Finals 1916 and 1917, WAFL 1916-18 and QAFL 1942-44 were played; the Australian Championships were held in 1915 and 1940 but not in 1986; the US Championships ran through World War I.
- **Missing gaps.** 1981 Caribbean Series, 1980/1984/1988 men's ice hockey World Championships, 2020 County Championship (replaced by the Bob Willis Trophy), NTFL 1974-75 (Cyclone Tracy), CONCACAF 1964-66 and 2001, and non-Ashes years.

## 6. Placeholder content in the existing files

A scan on 2026-09-30 read every active-year `COACHES.md` and `OFFICIATING.md` (8,339 of each). 7,327 of each use one generic template; the other 1,012 (AFL, MLB, NFL and the tennis folders) use a second, sport-flavoured template. Spot checks found **no season-specific names in either template**.

The text is placeholder, and some of it is wrong for the year it describes:
- `Basketball/NBA/2024/COACHES.md` names Phil Jackson and Red Auerbach as 2024 senior leadership.
- `Baseball/MLB/1950/COACHES.md` mentions 'defensive shifts, and modern analytics'; `American Football/NFL/1980/COACHES.md` mentions the 'Shanahan wide-zone system'.
- `AFL/AFL/1900/COACHES.md` describes 'surge football' and line coaches for 1900; the other templates cite 'VAR / TMO / DRS / Video Review / Hawk-Eye' regardless of sport or era.

Treat all existing COACHES, OFFICIATING and HISTORICAL_PLAYERS_AND_ROSTERS text as placeholder until it is replaced with sourced facts. Nothing in those files should be cited.

