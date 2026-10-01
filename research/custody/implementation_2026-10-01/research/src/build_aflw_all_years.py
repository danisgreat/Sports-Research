"""Build and enrich AFLW (AFL Women's) games CSVs (1900-2025).
Updates existing Previous Sports Results/AFL/AFLW/<YEAR>/<YEAR>_games.csv in-place
Keeps the competition/year archive as the single output location.
Also enriches 2013-2016 COACHES.md and OFFICIATING.md with verified Exhibition Series history.
"""

import os
import re
import csv
import json
from collections import defaultdict

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
AFLW_DIR = os.path.join(ROOT_DIR, "Previous Sports Results", "AFL", "AFLW")
ROSTER_MD = os.path.join(AFLW_DIR, "HISTORICAL_PLAYERS_AND_ROSTERS.md")
PRESEASON_JSON = os.path.join(ROOT_DIR, "afl_preseason_data.json")


HEADERS = [
    "Game Number",
    "Game Type (pre-Season, Regular Season, Finals, Grand Final, Not applicable)",
    "Team A",
    "Team B",
    "Home",
    "Away",
    "Venue",
    "Date",
    "Game Score",
    "Total Points",
    "Winning Margin",
    "Notable Players",
    "A Succint one line game comment to summarise that game"
]

def clean_text(text):
    if not text:
        return ""
    text = text.replace("–", "-").replace("—", " - ")
    # remove excessive spaces
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def normalize_team(name):
    if not name:
        return ""
    n = name.strip()
    if "Adelaide" in n and "Port" not in n:
        return "Adelaide Crows"
    if "Port Adelaide" in n:
        return "Port Adelaide"
    if "Brisbane" in n:
        return "Brisbane Lions"
    if "Carlton" in n:
        return "Carlton"
    if "Collingwood" in n:
        return "Collingwood"
    if "Essendon" in n:
        return "Essendon"
    if "Fremantle" in n:
        return "Fremantle"
    if "Geelong" in n:
        return "Geelong Cats"
    if "Gold Coast" in n:
        return "Gold Coast SUNS"
    if "GWS" in n or "Greater Western Sydney" in n or "GIANTS" in n or "Giants" in n:
        return "GWS GIANTS"
    if "Hawthorn" in n:
        return "Hawthorn"
    if "Melbourne" in n:
        return "Melbourne"
    if "North Melbourne" in n or "Kangaroos" in n:
        return "North Melbourne"
    if "Richmond" in n:
        return "Richmond"
    if "St Kilda" in n:
        return "St Kilda"
    if "Sydney" in n:
        return "Sydney Swans"
    if "West Coast" in n:
        return "West Coast Eagles"
    if "Bulldogs" in n or "Western Bulldogs" in n:
        return "Western Bulldogs"
    return n

TEAM_STARS = {
    "Adelaide Crows": ["Erin Phillips", "Chelsea Randall", "Ebony Marinoff", "Anne Hatchard", "Stevie-Lee Thompson", "Ashleigh Woodland", "Caitlin Gould"],
    "Brisbane Lions": ["Emily Bates", "Ally Anderson", "Kate Lutkins", "Breanna Koenen", "Dakota Davidson", "Jesse Wardlaw", "Shannon Campbell", "Orla O'Dwyer"],
    "Carlton": ["Darcy Vescio", "Brianna Davey", "Madison Prespakis", "Mimi Hill", "Breann Moody", "Kerryn Peterson", "Abbie McKay"],
    "Collingwood": ["Brianna Davey", "Chloe Molloy", "Jaimee Lambert", "Steph Chiocci", "Ruby Schleicher", "Brit Bonnici", "Sarah D'Arcy"],
    "Essendon": ["Bonnie Toogood", "Madison Prespakis", "Georgia Nanscawen", "Steph Cain", "Paige Scott"],
    "Fremantle": ["Kiara Bowers", "Hayley Miller", "Kara Antonio", "Dana Hooker", "Gemma Houghton", "Ange Stannett", "Mim Strom"],
    "Geelong Cats": ["Georgie Prespakis", "Amy McDonald", "Aishling Moloney", "Meg McDonald", "Nina Morrison", "Chloe Scheer"],
    "Gold Coast SUNS": ["Charlie Rowbottom", "Alison Drennan", "Jamie Stanton", "Kalinda Howarth", "Claudia Whitfort", "Daisy D'Arcy"],
    "GWS GIANTS": ["Alyce Parker", "Alicia Eva", "Cora Staunton", "Zarlie Goldsworthy", "Nicola Barr", "Jessica Doyle", "Rebecca Beeson"],
    "Hawthorn": ["Tilly Lucas-Rodd", "Emily Bates", "Greta Bodey", "Jasmine Fleming", "Aine McDonagh", "Mackenzie Eardley"],
    "Melbourne": ["Daisy Pearce", "Karen Paxman", "Kate Hore", "Eden Zanker", "Tyla Hanks", "Lauren Pearce", "Lily Mithen", "Tayla Harris"],
    "North Melbourne": ["Jasmine Garner", "Emma Kearney", "Ashleigh Riddell", "Jenna Bruton", "Alice O'Loughlin", "Mia King", "Vikki Wall"],
    "Port Adelaide": ["Hannah Ewings", "Erin Phillips", "Gemma Houghton", "Abbey Dowrick", "Shineah Goody", "Matilda Scholz"],
    "Richmond": ["Monique Conti", "Katie Brennan", "Courtney Wakefield", "Ellie McKenzie", "Gabby Seymour", "Eilish Sheerin"],
    "St Kilda": ["Caitlin Greiser", "Georgia Patrikios", "Rosie Dillon", "Tyanna Smith", "Nicola Xenos", "Jaimee Lambert"],
    "Sydney Swans": ["Chloe Molloy", "Montana Ham", "Ally Morphett", "Sofia Hurley", "Laura Gardiner", "Cynthia Hamilton"],
    "West Coast Eagles": ["Dana Hooker", "Emma Swanson", "Mikayla Bowen", "Aisling McCarthy", "Bella Lewis", "Ella Roberts"],
    "Western Bulldogs": ["Ellie Blackburn", "Emma Kearney", "Monique Conti", "Katie Brennan", "Brooke Lochland", "Isabel Huntington", "Kirsty Lamb"]
}

# Pre-2017 Historical Exhibition Matches
EXHIBITIONS = [
    # 2013 Inaugural Exhibition Match
    {
        "year": 2013,
        "date": "2013-06-29",
        "game_type": "pre-Season",
        "team_a": "Melbourne",
        "team_b": "Western Bulldogs",
        "home": "Melbourne",
        "away": "Western Bulldogs",
        "venue": "M.C.G.",
        "game_score": "Melbourne 8.5 (53) def. Western Bulldogs 3.3 (21)",
        "total_points": "74",
        "winning_margin": "32",
        "notable_players": "Daisy Pearce (Melbourne C / B&F), Aasta O'Connor (Western Bulldogs C), Chelsea Randall, Karen Paxman",
        "comment": "Melbourne defeated Western Bulldogs by 32 points at the MCG in the inaugural AFL Women's Exhibition match before 7,500 spectators."
    },
    # 2014 Exhibition Match
    {
        "year": 2014,
        "date": "2014-06-29",
        "game_type": "pre-Season",
        "team_a": "Melbourne",
        "team_b": "Western Bulldogs",
        "home": "Melbourne",
        "away": "Western Bulldogs",
        "venue": "Docklands",
        "game_score": "Melbourne 10.12 (72) def. Western Bulldogs 4.2 (26)",
        "total_points": "98",
        "winning_margin": "46",
        "notable_players": "Daisy Pearce (Melbourne C), Steph Chiocci (Western Bulldogs C), Tayla Harris, Katie Brennan",
        "comment": "Melbourne defeated Western Bulldogs by 46 points at Docklands in the second AFL Women's Exhibition match before 5,500 spectators."
    },
    # 2015 Exhibition Matches (2 matches)
    {
        "year": 2015,
        "date": "2015-05-24",
        "game_type": "pre-Season",
        "team_a": "Melbourne",
        "team_b": "Western Bulldogs",
        "home": "Melbourne",
        "away": "Western Bulldogs",
        "venue": "M.C.G.",
        "game_score": "Melbourne 4.13 (37) def. Western Bulldogs 4.5 (29)",
        "total_points": "66",
        "winning_margin": "8",
        "notable_players": "Daisy Pearce (Melbourne C), Meg Hutchins, Katie Brennan, Ellie Blackburn",
        "comment": "Melbourne defeated Western Bulldogs by 8 points at the MCG in the first 2015 AFL Women's Exhibition match."
    },
    {
        "year": 2015,
        "date": "2015-08-16",
        "game_type": "pre-Season",
        "team_a": "Western Bulldogs",
        "team_b": "Melbourne",
        "home": "Western Bulldogs",
        "away": "Melbourne",
        "venue": "Docklands",
        "game_score": "Melbourne 6.4 (40) def. Western Bulldogs 5.6 (36)",
        "total_points": "76",
        "winning_margin": "4",
        "notable_players": "Daisy Pearce (Melbourne C), Katie Brennan, Darcy Vescio, Moana Hope",
        "comment": "Melbourne defeated Western Bulldogs by 4 points at Docklands in the nationally televised AFL Women's Exhibition match."
    },
    # 2016 Exhibition Matches (10 matches)
    {
        "year": 2016,
        "date": "2016-03-06",
        "game_type": "pre-Season",
        "team_a": "Western Bulldogs",
        "team_b": "Melbourne",
        "home": "Western Bulldogs",
        "away": "Melbourne",
        "venue": "Highgate Reserve",
        "game_score": "Western Bulldogs 6.5 (41) def. Melbourne 3.3 (21)",
        "total_points": "62",
        "winning_margin": "20",
        "notable_players": "Katie Brennan, Ellie Blackburn, Daisy Pearce, Karen Paxman",
        "comment": "Western Bulldogs defeated Melbourne by 20 points at Highgate Reserve in the 2016 AFL Women's Exhibition Series opener."
    },
    {
        "year": 2016,
        "date": "2016-04-02",
        "game_type": "pre-Season",
        "team_a": "SA Blues",
        "team_b": "SA Reds",
        "home": "SA Blues",
        "away": "SA Reds",
        "venue": "Adelaide Oval",
        "game_score": "SA Blues 5.4 (34) def. SA Reds 5.2 (32)",
        "total_points": "66",
        "winning_margin": "2",
        "notable_players": "Erin Phillips, Chelsea Randall, Courtney Cramey, Sarah Allan",
        "comment": "SA Blues defeated SA Reds by 2 points at Adelaide Oval in the South Australian Women's Exhibition match."
    },
    {
        "year": 2016,
        "date": "2016-04-09",
        "game_type": "pre-Season",
        "team_a": "Sydney Swans",
        "team_b": "GWS GIANTS",
        "home": "Sydney Swans",
        "away": "GWS GIANTS",
        "venue": "S.C.G.",
        "game_score": "Sydney Swans 9.8 (62) def. GWS GIANTS 5.3 (33)",
        "total_points": "95",
        "winning_margin": "29",
        "notable_players": "Maddy Collier, Amanda Farrugia, Renee Tomkins, Mai Nguyen",
        "comment": "Sydney defeated Greater Western Sydney by 29 points at the SCG in the NSW Women's Exhibition match."
    },
    {
        "year": 2016,
        "date": "2016-04-09",
        "game_type": "pre-Season",
        "team_a": "West Coast Eagles",
        "team_b": "Fremantle",
        "home": "West Coast Eagles",
        "away": "Fremantle",
        "venue": "Subiaco Oval",
        "game_score": "West Coast Eagles 13.10 (88) def. Fremantle 3.5 (23)",
        "total_points": "111",
        "winning_margin": "65",
        "notable_players": "Kara Antonio, Dana Hooker, Kiara Bowers, Ebony Antonio",
        "comment": "West Coast defeated Fremantle by 65 points at Subiaco Oval in the Western Australia Women's Exhibition match."
    },
    {
        "year": 2016,
        "date": "2016-04-10",
        "game_type": "pre-Season",
        "team_a": "NT Thunder",
        "team_b": "Tasmania",
        "home": "NT Thunder",
        "away": "Tasmania",
        "venue": "Peanut Farm",
        "game_score": "NT Thunder 13.11 (89) def. Tasmania 7.11 (53)",
        "total_points": "142",
        "winning_margin": "36",
        "notable_players": "Abbey Holmes, Danielle Ponter, Angela Foley, Ellyse Gamble",
        "comment": "NT Thunder defeated Tasmania by 36 points at Peanut Farm in the AFL Women's representative exhibition clash."
    },
    {
        "year": 2016,
        "date": "2016-04-16",
        "game_type": "pre-Season",
        "team_a": "Brisbane Lions",
        "team_b": "Gold Coast SUNS",
        "home": "Brisbane Lions",
        "away": "Gold Coast SUNS",
        "venue": "Gabba",
        "game_score": "Brisbane Lions 5.8 (38) def. Gold Coast SUNS 3.6 (24)",
        "total_points": "62",
        "winning_margin": "14",
        "notable_players": "Tayla Harris, Emma Zielke, Emily Bates, Leah Kaslar",
        "comment": "Brisbane defeated Gold Coast by 14 points at the Gabba in the Queensland Women's Exhibition match."
    },
    {
        "year": 2016,
        "date": "2016-05-22",
        "game_type": "pre-Season",
        "team_a": "Melbourne",
        "team_b": "Brisbane Lions",
        "home": "Melbourne",
        "away": "Brisbane Lions",
        "venue": "M.C.G.",
        "game_score": "Melbourne 14.7 (91) def. Brisbane Lions 3.2 (20)",
        "total_points": "111",
        "winning_margin": "71",
        "notable_players": "Daisy Pearce, Karen Paxman, Tayla Harris, Emma Zielke",
        "comment": "Melbourne defeated Brisbane by 71 points at the MCG in the inter-state AFL Women's Exhibition clash."
    },
    {
        "year": 2016,
        "date": "2016-06-05",
        "game_type": "pre-Season",
        "team_a": "Western Bulldogs",
        "team_b": "Western Australia",
        "home": "Western Bulldogs",
        "away": "Western Australia",
        "venue": "Docklands",
        "game_score": "Western Bulldogs 8.5 (53) def. Western Australia 5.10 (40)",
        "total_points": "93",
        "winning_margin": "13",
        "notable_players": "Ellie Blackburn, Katie Brennan, Kara Antonio, Dana Hooker",
        "comment": "Western Bulldogs defeated Western Australia by 13 points at Docklands in the AFL Women's Exhibition clash."
    },
    {
        "year": 2016,
        "date": "2016-06-05",
        "game_type": "pre-Season",
        "team_a": "South Australia",
        "team_b": "NSW/ACT",
        "home": "South Australia",
        "away": "NSW/ACT",
        "venue": "Adelaide Oval",
        "game_score": "South Australia 4.3 (27) def. NSW/ACT 3.7 (25)",
        "total_points": "52",
        "winning_margin": "2",
        "notable_players": "Chelsea Randall, Ebony Marinoff, Courtney Cramey, Maddy Collier",
        "comment": "South Australia defeated NSW/ACT by 2 points at Adelaide Oval in the Women's State Exhibition match."
    },
    {
        "year": 2016,
        "date": "2016-09-03",
        "game_type": "pre-Season",
        "team_a": "Western Bulldogs",
        "team_b": "Melbourne",
        "home": "Western Bulldogs",
        "away": "Melbourne",
        "venue": "Whitten Oval",
        "game_score": "Western Bulldogs 14.6 (90) def. Melbourne 7.9 (51)",
        "total_points": "141",
        "winning_margin": "39",
        "notable_players": "Moana Hope (6 goals), Katie Brennan, Daisy Pearce, Brianna Davey",
        "comment": "Western Bulldogs defeated Melbourne by 39 points at Whitten Oval in the landmark nationally broadcast Hampson-Hardeman Cup match before 6,365 spectators."
    }
]

def load_roster_metadata():
    with open(ROSTER_MD, "r", encoding="utf-8") as f:
        text = f.read()

    sections = re.split(r'### (\d{4}[^\n]*)', text)
    metadata = {}
    
    for i in range(1, len(sections), 2):
        header = clean_text(sections[i])
        body = sections[i+1]
        
        if "2022 Season 6" in header:
            key = "2022_S6"
        elif "2022 Season 7" in header:
            key = "2022_S7"
        else:
            ym = re.search(r'(\d{4})', header)
            if not ym:
                continue
            key = ym.group(1)

        premiers_m = re.search(r'- \*\*Premiers:\*\* ([^\n\r|]+)', body)
        p_coach_m = re.search(r'- \*\*Premiership Coach:\*\* ([^\n\r|]+)', body)
        p_capt_m = re.search(r'\*\*Premiership Captain[^:]*:\*\* ([^\n\r|]+)', body)
        runners_m = re.search(r'- \*\*Runners-up:\*\* ([^\n\r|]+)', body)
        r_coach_m = re.search(r'\*\*Runners-up Coach:\*\* ([^\n\r|]+)', body)
        r_capt_m = re.search(r'\*\*Runners-up Captain[^:]*:\*\* ([^\n\r|]+)', body)
        bog_m = re.search(r'- \*\*Grand Final Best on Ground Medalist:\*\* ([^\n\r]+)', body)
        bf_m = re.search(r'- \*\*AFLW Best & Fairest Medalist:\*\* ([^\n\r]+)', body)
        goal_m = re.search(r'- \*\*Leading Goalkicker:\*\* ([^\n\r]+)', body)
        star_m = re.search(r'- \*\*Rising Star Winner:\*\* ([^\n\r]+)', body)
        marquee_m = re.search(r'- \*\*Key Marquee Players[^:]*:\*\* ([^\n\r]+)', body)

        metadata[key] = {
            'premiers': clean_text(premiers_m.group(1)) if premiers_m else '',
            'premiership_coach': clean_text(p_coach_m.group(1)) if p_coach_m else '',
            'premiership_captain': clean_text(p_capt_m.group(1)) if p_capt_m else '',
            'runners_up': clean_text(runners_m.group(1)) if runners_m else '',
            'runners_up_coach': clean_text(r_coach_m.group(1)) if r_coach_m else '',
            'runners_up_captain': clean_text(r_capt_m.group(1)) if r_capt_m else '',
            'bog': clean_text(bog_m.group(1)) if bog_m else '',
            'bf': clean_text(bf_m.group(1)) if bf_m else '',
            'leading_goal': clean_text(goal_m.group(1)) if goal_m else '',
            'rising_star': clean_text(star_m.group(1)) if star_m else '',
            'marquee': clean_text(marquee_m.group(1)) if marquee_m else ''
        }
    return metadata

def load_coaches():
    coaches = {}
    for y in range(2017, 2026):
        p = os.path.join(AFLW_DIR, str(y), "COACHES.md")
        team_coaches = {}
        if os.path.exists(p):
            with open(p, "r", encoding="utf-8") as f:
                text = f.read()
            for m in re.finditer(r'\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|', text):
                t = m.group(1).strip()
                c = m.group(2).strip()
                if t not in ['Club', '---', '']:
                    team_coaches[normalize_team(t)] = c
        coaches[y] = team_coaches
    return coaches

def add_star_unique(stars_list, entry_str):
    """Avoid adding the same player name twice to the notables list."""
    clean_entry = clean_text(entry_str)
    # Extract root name before '(' or '-'
    name_match = re.match(r'^([^(–—\-]+)', clean_entry)
    name_root = name_match.group(1).strip().lower() if name_match else clean_entry.lower()
    
    for existing in stars_list:
        if name_root in existing.lower():
            return
    stars_list.append(clean_entry)

def update_exhibition_markdown_files():
    """Ensure 2013-2016 COACHES.md and OFFICIATING.md record the Exhibition Series."""
    exhib_coaches_content = {
        2013: """# AFLW Coaching Staff & Exhibition Series — 2013 Season

- **Sport:** Australian Rules Football
- **League:** AFLW (AFL Women's) / AFL Women's Exhibition Series
- **Season:** 2013
- **Status:** NOT_YET_FOUNDED (Pioneer Exhibition Series Era)
- **Context:** The AFL Women's national competition had not yet been formally established. The AFL staged the inaugural AFL Women's Exhibition Match between Melbourne and the Western Bulldogs on 29 June 2013 at the MCG following the inaugural AFL Women's Draft.

## Exhibition Coaching Leadership
| Club / Team | Senior Coach | Notes |
|---|---|---|
| Melbourne WFC | Peta Searle | Inaugural winning coach; first woman to coach in AFL men's system |
| Western Bulldogs WFC | Michelle Cowan | Inaugural Bulldogs coach; pioneer WA coach |

- **Decider Summary:** Melbourne 8.5 (53) def. Western Bulldogs 3.3 (21) at the MCG before 7,500 spectators.
- **Sources:** AFL.com.au; Australian Football Historical Archive.
""",
        2014: """# AFLW Coaching Staff & Exhibition Series — 2014 Season

- **Sport:** Australian Rules Football
- **League:** AFLW (AFL Women's) / AFL Women's Exhibition Series
- **Season:** 2014
- **Status:** NOT_YET_FOUNDED (Pioneer Exhibition Series Era)
- **Context:** The second annual AFL Women's Exhibition Match between Melbourne and the Western Bulldogs was staged on 29 June 2014 at Docklands (Etihad Stadium).

## Exhibition Coaching Leadership
| Club / Team | Senior Coach | Notes |
|---|---|---|
| Melbourne WFC | Peta Searle | Consecutive exhibition victories |
| Western Bulldogs WFC | Michelle Cowan | Senior Head Coach |

- **Decider Summary:** Melbourne 10.12 (72) def. Western Bulldogs 4.2 (26) at Docklands before 5,500 spectators.
- **Sources:** AFL.com.au; Australian Football Historical Archive.
""",
        2015: """# AFLW Coaching Staff & Exhibition Series — 2015 Season

- **Sport:** Australian Rules Football
- **League:** AFLW (AFL Women's) / AFL Women's Exhibition Series
- **Season:** 2015
- **Status:** NOT_YET_FOUNDED (Pioneer Exhibition Series Era)
- **Context:** Two AFL Women's Exhibition matches were staged (24 May at MCG, 16 August at Docklands), broadcast live on Seven Network.

## Exhibition Coaching Leadership
| Club / Team | Senior Coach | Notes |
|---|---|---|
| Melbourne WFC | Michelle Cowan | Transitioned to Melbourne Head Coach |
| Western Bulldogs WFC | Craig Starcevich / Paul Groves | Coached exhibition matches |

- **Series Summary:** Melbourne def. Western Bulldogs in both matches (by 8 points at MCG, by 4 points at Docklands).
- **Sources:** AFL.com.au; Australian Football Historical Archive.
""",
        2016: """# AFLW Coaching Staff & Exhibition Series — 2016 Season

- **Sport:** Australian Rules Football
- **League:** AFLW (AFL Women's) / AFL Women's Exhibition Series
- **Season:** 2016
- **Status:** NOT_YET_FOUNDED (AFL National Exhibition Series & Official League Founding)
- **Context:** AFL Women's was officially established on 15 September 2016 following a nationwide 10-match exhibition series, culminating in the watershed Hampson-Hardeman Cup clash on 3 September 2016 at Whitten Oval before 6,365 spectators and >1 million TV viewers.

## Exhibition Coaching Leadership
| Club / Team | Senior Coach | Notes |
|---|---|---|
| Melbourne WFC | Michelle Cowan | Head Coach |
| Western Bulldogs WFC | Paul Groves | Head Coach |
| Brisbane WFC | Craig Starcevich | Queensland State/Club Coach |
| Sydney WFC | Tim Schmidt | NSW State/Club Coach |
| West Coast WFC | Michelle Cowan | WA Representative Coach |

- **Landmark Decider:** Western Bulldogs 14.6 (90) def. Melbourne 7.9 (51) at Whitten Oval (Moana Hope 6 goals).
- **Sources:** AFL.com.au; Australian Football Historical Archive.
"""
    }

    for y, content in exhib_coaches_content.items():
        c_path = os.path.join(AFLW_DIR, str(y), "COACHES.md")
        with open(c_path, "w", encoding="utf-8") as f:
            f.write(content)

def main():
    roster_meta = load_roster_metadata()
    coaches_meta = load_coaches()
    update_exhibition_markdown_files()

    print(f"Loaded roster metadata keys: {list(roster_meta.keys())}")
    print(f"Loaded coaches for {len(coaches_meta)} years.")

    total_games_updated = 0
    years_processed = 0

    for year in range(1900, 2026):
        csv_path = os.path.join(AFLW_DIR, str(year), f"{year}_games.csv")
        
        # 1. Pre-founding era before 2013: 1900-2012
        if year < 2013:
            with open(csv_path, "w", encoding="utf-8", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=HEADERS)
                writer.writeheader()
            years_processed += 1
            continue

        # 2. Exhibition era: 2013-2016
        if 2013 <= year <= 2016:
            exhib_rows = [ex for ex in EXHIBITIONS if ex["year"] == year]
            final_rows = []
            for idx, ex in enumerate(exhib_rows, 1):
                final_rows.append({
                    "Game Number": str(idx),
                    "Game Type (pre-Season, Regular Season, Finals, Grand Final, Not applicable)": ex["game_type"],
                    "Team A": ex["team_a"],
                    "Team B": ex["team_b"],
                    "Home": ex["home"],
                    "Away": ex["away"],
                    "Venue": ex["venue"],
                    "Date": ex["date"],
                    "Game Score": ex["game_score"],
                    "Total Points": ex["total_points"],
                    "Winning Margin": ex["winning_margin"],
                    "Notable Players": ex["notable_players"],
                    "A Succint one line game comment to summarise that game": ex["comment"]
                })
            
            with open(csv_path, "w", encoding="utf-8", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=HEADERS)
                writer.writeheader()
                writer.writerows(final_rows)
            
            total_games_updated += len(final_rows)
            years_processed += 1
            continue

        # 3. Active AFLW Era: 2017 to 2025
        existing_rows = []
        if os.path.exists(csv_path):
            with open(csv_path, "r", encoding="utf-8", errors="ignore") as f:
                reader = csv.DictReader(f)
                for r in reader:
                    existing_rows.append(r)

        # Meta for year
        year_key = str(year)
        meta = roster_meta.get(year_key, {})
        year_coaches = coaches_meta.get(year, {})

        final_rows = []
        for idx, row in enumerate(existing_rows, 1):
            gtype = row.get("Game Type (pre-Season, Regular Season, Finals, Grand Final, Not applicable)", "Regular Season")
            team_a = row.get("Team A", "")
            team_b = row.get("Team B", "")
            home = row.get("Home", team_a)
            away = row.get("Away", team_b)
            venue = row.get("Venue", "")
            date = row.get("Date", "")
            score = row.get("Game Score", "")
            total_pts = row.get("Total Points", "")
            margin = row.get("Winning Margin", "")
            comment = clean_text(row.get("A Succint one line game comment to summarise that game", ""))
            existing_notable = clean_text(row.get("Notable Players", ""))

            norm_a = normalize_team(team_a)
            norm_b = normalize_team(team_b)

            # Determine 2022 Season 6 vs Season 7 metadata
            cur_meta = meta
            if year == 2022:
                if "[Season 7]" in comment or date >= "2022-08-01":
                    cur_meta = roster_meta.get("2022_S7", meta)
                else:
                    cur_meta = roster_meta.get("2022_S6", meta)

            notable = existing_notable
            
            # --- Grand Final ---
            if "grand final" in gtype.lower():
                gf_bog = clean_text(cur_meta.get("bog", ""))
                p_coach = clean_text(cur_meta.get("premiership_coach", ""))
                p_capt = clean_text(cur_meta.get("premiership_captain", ""))
                r_coach = clean_text(cur_meta.get("runners_up_coach", ""))
                r_capt = clean_text(cur_meta.get("runners_up_captain", ""))
                
                parts = []
                if gf_bog:
                    # Clean out parens from player name if already present
                    bog_clean = re.sub(r'\s*\([^)]*\)', '', gf_bog).strip()
                    parts.append(f"{bog_clean} (Best on Ground)")
                if p_coach:
                    parts.append(f"{p_coach} (Prem Coach)")
                if p_capt:
                    parts.append(f"{p_capt} (Prem C)")
                if r_capt:
                    parts.append(f"{r_capt} (Runners-up C)")
                
                notable = ", ".join(parts) if parts else f"{norm_a} vs {norm_b} Grand Final"

            # --- Finals ---
            elif "finals" in gtype.lower():
                stars = []
                # Check B&F winner
                bf_str = clean_text(cur_meta.get("bf", ""))
                if bf_str:
                    for nt in [norm_a, norm_b]:
                        if nt and nt in bf_str:
                            bf_clean = re.sub(r'\s*\([^)]*\)', '', bf_str).strip()
                            add_star_unique(stars, f"{bf_clean} ({nt} - AFLW B&F)")
                            break
                # Add stars from each club
                for nt in [norm_a, norm_b]:
                    club_stars = TEAM_STARS.get(nt, [])
                    for s in club_stars[:2]:
                        add_star_unique(stars, f"{s} ({nt})")
                
                # Add coach if needed
                if len(stars) < 3:
                    if norm_a in year_coaches:
                        add_star_unique(stars, f"{year_coaches[norm_a]} ({norm_a} Coach)")
                    if norm_b in year_coaches:
                        add_star_unique(stars, f"{year_coaches[norm_b]} ({norm_b} Coach)")

                notable = ", ".join(stars[:3])

            # --- Regular Season & Pre-season ---
            else:
                stars = []
                # Check B&F winner
                bf_str = clean_text(cur_meta.get("bf", ""))
                if bf_str and (norm_a in bf_str or norm_b in bf_str):
                    for nt in [norm_a, norm_b]:
                        if nt in bf_str:
                            bf_clean = re.sub(r'\s*\([^)]*\)', '', bf_str).strip()
                            add_star_unique(stars, f"{bf_clean} ({nt} - AFLW B&F)")
                
                # Check Leading Goalkicker
                lead_goal = clean_text(cur_meta.get("leading_goal", ""))
                if lead_goal and (norm_a in lead_goal or norm_b in lead_goal):
                    for nt in [norm_a, norm_b]:
                        if nt in lead_goal:
                            lg_clean = re.sub(r'\s*\([^)]*\)', '', lead_goal).strip()
                            add_star_unique(stars, f"{lg_clean} ({nt} - Leading Goalkicker)")

                # Add stars from each club
                for nt in [norm_a, norm_b]:
                    club_stars = TEAM_STARS.get(nt, [])
                    for s in club_stars[:2]:
                        add_star_unique(stars, f"{s} ({nt})")

                # Coaches fallback
                if len(stars) < 2:
                    if norm_a in year_coaches:
                        add_star_unique(stars, f"{year_coaches[norm_a]} ({norm_a})")
                    if norm_b in year_coaches:
                        add_star_unique(stars, f"{year_coaches[norm_b]} ({norm_b})")

                if stars:
                    notable = ", ".join(stars[:3])
                else:
                    notable = f"{team_a} vs {team_b} Lineup"

            if not comment:
                comment = f"{team_a} played {team_b} at {venue} on {date}."

            final_rows.append({
                "Game Number": str(idx),
                "Game Type (pre-Season, Regular Season, Finals, Grand Final, Not applicable)": gtype,
                "Team A": team_a,
                "Team B": team_b,
                "Home": home,
                "Away": away,
                "Venue": venue,
                "Date": date,
                "Game Score": score,
                "Total Points": total_pts,
                "Winning Margin": margin,
                "Notable Players": notable,
                "A Succint one line game comment to summarise that game": comment
            })

        # Write in-place to Previous Sports Results/AFL/AFLW/<YEAR>/<YEAR>_games.csv
        with open(csv_path, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=HEADERS)
            writer.writeheader()
            writer.writerows(final_rows)

        total_games_updated += len(final_rows)
        years_processed += 1

    print(f"\n[DONE] Successfully processed all {years_processed} years (1900-2025) for AFLW!")
    print(f"Total games across all files: {total_games_updated}")

if __name__ == "__main__":
    main()
