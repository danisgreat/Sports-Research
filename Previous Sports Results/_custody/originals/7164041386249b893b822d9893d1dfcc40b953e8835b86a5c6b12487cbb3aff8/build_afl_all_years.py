"""Build and enrich AFL games CSVs (1900-2025).
Updates existing Previous Sports Results/AFL/AFL/<YEAR>/<YEAR>_games.csv
Keeps the competition/year archive as the single output location.
"""

import os
import re
import csv
import json
from collections import defaultdict

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
AFL_DIR = os.path.join(ROOT_DIR, "Previous Sports Results", "AFL", "AFL")
GF_DIR = os.path.join(ROOT_DIR, "Previous Sports Results", "AFL", "AFL Grand Final")
ROSTER_MD = os.path.join(AFL_DIR, "HISTORICAL_PLAYERS_AND_ROSTERS.md")
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

def normalize_team(name):
    n = name.strip()
    if "South Melbourne" in n or "Sydney" in n:
        return "Sydney"
    if "Footscray" in n or "Western Bulldogs" in n:
        return "Western Bulldogs"
    if "North Melbourne" in n or "Kangaroos" in n:
        return "North Melbourne"
    if "Brisbane Bears" in n or "Brisbane Lions" in n or "Brisbane" in n:
        return "Brisbane"
    if "Greater Western Sydney" in n or "GWS" in n:
        return "Greater Western Sydney"
    if "Port Adelaide" in n:
        return "Port Adelaide"
    if "Gold Coast" in n:
        return "Gold Coast"
    if "West Coast" in n:
        return "West Coast"
    return n

def load_roster_metadata():
    with open(ROSTER_MD, "r", encoding="utf-8") as f:
        text = f.read()

    sections = re.split(r'### (\d{4}) Season', text)
    metadata = {}
    for i in range(1, len(sections), 2):
        y = int(sections[i])
        body = sections[i+1]
        
        premiers_m = re.search(r'- \*\*Premiers:\*\* ([^\n\r]+)', body)
        brownlow_m = re.search(r'- \*\*Brownlow Medal:\*\* ([^\n\r]+)', body)
        coleman_m = re.search(r'- \*\*Leading Goalkicker / Coleman Medal:\*\* ([^\n\r]+)', body)
        norm_smith_m = re.search(r'- \*\*Norm Smith Medal \(GF Best on Ground\):\*\* ([^\n\r]+)', body)
        marquee_m = re.search(r'- \*\*Key Marquee Players[^:]*:\*\* ([^\n\r]+)', body)
        
        metadata[y] = {
            'premiers': premiers_m.group(1).strip() if premiers_m else '',
            'brownlow': brownlow_m.group(1).strip() if brownlow_m else '',
            'coleman': coleman_m.group(1).strip() if coleman_m else '',
            'norm_smith': norm_smith_m.group(1).strip() if norm_smith_m else '',
            'marquee': marquee_m.group(1).strip() if marquee_m else ''
        }
    return metadata

def load_coaches():
    coaches = {}
    for y in range(1900, 2026):
        p = os.path.join(AFL_DIR, str(y), "COACHES.md")
        team_coaches = {}
        if os.path.exists(p):
            with open(p, "r", encoding="utf-8") as f:
                text = f.read()
            for m in re.finditer(r'\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|', text):
                t = m.group(1).strip()
                c = m.group(2).strip()
                role = m.group(3).strip()
                if t not in ['Club', '---', '']:
                    team_coaches[normalize_team(t)] = (c, role)
        coaches[y] = team_coaches
    return coaches

def load_grand_finals():
    gf_data = {}
    for y in range(1900, 2026):
        path = os.path.join(GF_DIR, str(y), f"{y}_games.csv")
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                reader = list(csv.DictReader(f))
                if reader:
                    gf_data[y] = reader
    return gf_data

def load_preseason_json():
    with open(PRESEASON_JSON, "r", encoding="utf-8") as f:
        matches = json.load(f)["matches"]
    
    by_year = defaultdict(list)
    for m in matches:
        if "AFLW" in m.get("competition_name", ""):
            continue
        y = m["year"]
        by_year[y].append(m)
    return by_year

EXHIBITIONS = [
    {
        "year": 2020,
        "date": "2020-02-28",
        "game_type": "pre-Season",
        "team_a": "Victoria",
        "team_b": "All-Stars",
        "home": "Victoria",
        "away": "All-Stars",
        "venue": "Marvel Stadium",
        "game_score": "Victoria 24.10 (154) def. All-Stars 15.18 (108)",
        "total_points": "262",
        "winning_margin": "46",
        "notable_players": "Dustin Martin (Best on Ground), Trent Cotchin (Victoria C), Nat Fyfe (All-Stars C)",
        "comment": "Victoria defeated the All-Stars by 46 points in the AFL State of Origin for Bushfire Relief charity match."
    },
    {
        "year": 2008,
        "date": "2008-05-10",
        "game_type": "pre-Season",
        "team_a": "Victoria",
        "team_b": "Dream Team",
        "home": "Victoria",
        "away": "Dream Team",
        "venue": "M.C.G.",
        "game_score": "Victoria 21.11 (137) def. Dream Team 17.18 (120)",
        "total_points": "257",
        "winning_margin": "17",
        "notable_players": "Brendan Fevola (Allen Aylett Medal, 6 goals), Jonathan Brown (Victoria C), Andrew McLeod (Dream Team C)",
        "comment": "Victoria defeated the Dream Team by 17 points at the MCG in the AFL Hall of Fame Tribute Match celebrating 150 years of Australian football."
    },
    {
        "year": 2013,
        "date": "2013-02-08",
        "game_type": "pre-Season",
        "team_a": "Indigenous All-Stars",
        "team_b": "Richmond",
        "home": "Indigenous All-Stars",
        "away": "Richmond",
        "venue": "Traeger Park",
        "game_score": "Indigenous All-Stars 14.6 (90) def. Richmond 8.12 (60)",
        "total_points": "150",
        "winning_margin": "30",
        "notable_players": "Liam Jurrah, Patrick Ryder, Jack Riewoldt",
        "comment": "Indigenous All-Stars defeated Richmond by 30 points at Traeger Park in Alice Springs."
    },
    {
        "year": 2015,
        "date": "2015-02-20",
        "game_type": "pre-Season",
        "team_a": "West Coast",
        "team_b": "Indigenous All-Stars",
        "home": "West Coast",
        "away": "Indigenous All-Stars",
        "venue": "Medibank Stadium",
        "game_score": "West Coast 7.7 (49) def. Indigenous All-Stars 5.11 (41)",
        "total_points": "90",
        "winning_margin": "8",
        "notable_players": "Shaun Burgoyne (C), Luke Shuey",
        "comment": "West Coast defeated Indigenous All-Stars by 8 points at Medibank Stadium, Leederville."
    },
    {
        "year": 2009,
        "date": "2009-02-07",
        "game_type": "pre-Season",
        "team_a": "Indigenous All-Stars",
        "team_b": "Adelaide",
        "home": "Indigenous All-Stars",
        "away": "Adelaide",
        "venue": "Marrara Stadium",
        "game_score": "Indigenous All-Stars 12.11 (83) def. Adelaide 7.9 (51)",
        "total_points": "134",
        "winning_margin": "32",
        "notable_players": "Andrew McLeod (C), Matthew McLeod",
        "comment": "Indigenous All-Stars defeated Adelaide by 32 points at TIO Stadium, Darwin."
    }
]

def format_json_match(m):
    comp = m.get("competition_name", "Night Series")
    venue = m.get("venue", "")
    hp = int(m.get("home_points", 0))
    ap = int(m.get("away_points", 0))
    margin = abs(hp - ap)
    total = hp + ap
    ht = m.get("home_team", "")
    at = m.get("away_team", "")
    date = m.get("date", "")
    
    raw_score = m.get("score_text", "")
    if hp > ap:
        winner, loser = ht, at
        comment = f"{winner} defeated {loser} by {margin} points in the {comp} at {venue}."
    elif ap > hp:
        winner, loser = at, ht
        comment = f"{winner} defeated {loser} by {margin} points in the {comp} at {venue}."
    else:
        comment = f"{ht} drew with {at} ({hp} points each) in the {comp} at {venue}."
    
    notable = f"{comp} fixture: {ht} vs {at}"

    return {
        "Game Number": "",
        "Game Type (pre-Season, Regular Season, Finals, Grand Final, Not applicable)": "pre-Season",
        "Team A": ht,
        "Team B": at,
        "Home": ht,
        "Away": at,
        "Venue": venue,
        "Date": date,
        "Game Score": raw_score,
        "Total Points": str(total),
        "Winning Margin": str(margin),
        "Notable Players": notable,
        "A Succint one line game comment to summarise that game": comment
    }

def main():
    roster_meta = load_roster_metadata()
    coaches_meta = load_coaches()
    gf_meta = load_grand_finals()
    ps_json = load_preseason_json()

    print(f"Loaded roster meta for {len(roster_meta)} years.")
    print(f"Loaded coaches meta for {len(coaches_meta)} years.")
    print(f"Loaded grand final meta for {len(gf_meta)} years.")
    print(f"Loaded pre-season json for {len(ps_json)} years.")

    total_games_updated = 0
    years_processed = 0

    for year in range(1900, 2026):
        csv_path = os.path.join(AFL_DIR, str(year), f"{year}_games.csv")
        existing_rows = []
        if os.path.exists(csv_path):
            with open(csv_path, "r", encoding="utf-8", errors="ignore") as f:
                reader = csv.DictReader(f)
                for r in reader:
                    existing_rows.append(r)
        
        # Determine if night series needs to be added (1956-1987)
        new_night_rows = []
        if 1956 <= year <= 1987:
            for m in ps_json.get(year, []):
                new_night_rows.append(format_json_match(m))

        # Check exhibitions
        new_exhib_rows = []
        for ex in EXHIBITIONS:
            if ex["year"] == year:
                new_exhib_rows.append({
                    "Game Number": "",
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

        all_rows = existing_rows + new_night_rows + new_exhib_rows
        
        def sort_key(row):
            d = row.get("Date", "1900-01-01")
            t = row.get("Game Type (pre-Season, Regular Season, Finals, Grand Final, Not applicable)", "")
            type_weight = 1 if "pre-season" in t.lower() else (2 if "regular" in t.lower() else (3 if "finals" in t.lower() else 4))
            return (d, type_weight)

        all_rows.sort(key=sort_key)

        meta = roster_meta.get(year, {})
        brownlow = meta.get("brownlow", "")
        coleman = meta.get("coleman", "")
        premiers = meta.get("premiers", "")
        norm_smith = meta.get("norm_smith", "")
        marquee_str = meta.get("marquee", "")
        year_coaches = coaches_meta.get(year, {})

        marquee_by_team = defaultdict(list)
        if marquee_str:
            parts = [p.strip() for p in marquee_str.split(",") if p.strip()]
            for p in parts:
                m_match = re.match(r'([^(]+)\s*\(([^,]+)', p)
                if m_match:
                    pname = m_match.group(1).strip()
                    pteam = normalize_team(m_match.group(2).strip())
                    marquee_by_team[pteam].append(pname)

        bl_player = ""
        bl_team = ""
        if brownlow and "Not instituted" not in brownlow and "No Brownlow" not in brownlow:
            bm = re.match(r'([^(]+)\s*\(([^,)]+)', brownlow)
            if bm:
                bl_player = bm.group(1).strip()
                bl_team = normalize_team(bm.group(2).strip())

        cl_player = ""
        cl_team = ""
        if coleman and "Not instituted" not in coleman:
            cm = re.match(r'([^(]+)\s*\(([^,)]+)', coleman)
            if cm:
                cl_player = cm.group(1).strip()
                cl_team = normalize_team(cm.group(2).strip())

        gf_idx = 0
        gf_list = gf_meta.get(year, [])

        final_rows = []
        for idx, row in enumerate(all_rows, 1):
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
            comment = row.get("A Succint one line game comment to summarise that game", "")
            existing_notable = row.get("Notable Players", "").strip()

            norm_a = normalize_team(team_a)
            norm_b = normalize_team(team_b)

            notable = existing_notable
            
            # 1. Grand Final handling
            if "grand final" in gtype.lower():
                if gf_list and gf_idx < len(gf_list):
                    gf_row = gf_list[gf_idx]
                    notable = gf_row.get("Notable Players", "").strip()
                    if gf_row.get("A Succint one line game comment to summarise that game", "").strip():
                        comment = gf_row.get("A Succint one line game comment to summarise that game", "").strip()
                    gf_idx += 1
                if not notable:
                    notable_parts = []
                    if norm_smith and "Not instituted" not in norm_smith:
                        notable_parts.append(f"{norm_smith} (Norm Smith Medal)")
                    if premiers:
                        notable_parts.append(f"{premiers}")
                    notable = ", ".join(notable_parts)

            # 2. Finals handling
            elif "finals" in gtype.lower() and not notable:
                stars = []
                for nt in [norm_a, norm_b]:
                    plist = marquee_by_team.get(nt, [])
                    for p in plist[:2]:
                        stars.append(f"{p} ({nt})")
                if bl_player and (bl_team == norm_a or bl_team == norm_b):
                    stars.insert(0, f"{bl_player} ({bl_team} - Brownlow)")
                if cl_player and (cl_team == norm_a or cl_team == norm_b):
                    stars.insert(0, f"{cl_player} ({cl_team} - Coleman)")
                
                # If still empty, add coaches
                if not stars:
                    coach_parts = []
                    if norm_a in year_coaches:
                        c_name, c_role = year_coaches[norm_a]
                        coach_parts.append(f"{c_name} ({team_a} Coach)")
                    if norm_b in year_coaches:
                        c_name, c_role = year_coaches[norm_b]
                        coach_parts.append(f"{c_name} ({team_b} Coach)")
                    stars = coach_parts

                if stars:
                    notable = ", ".join(stars[:3])
                else:
                    notable = f"{team_a} vs {team_b} Finals Match"

            # 3. Regular Season handling
            elif not notable:
                stars = []
                if bl_player and (bl_team == norm_a or bl_team == norm_b):
                    stars.append(f"{bl_player} ({bl_team} - Brownlow)")
                if cl_player and (cl_team == norm_a or cl_team == norm_b):
                    stars.append(f"{cl_player} ({cl_team} - Coleman)")
                for nt in [norm_a, norm_b]:
                    plist = marquee_by_team.get(nt, [])
                    for p in plist[:2]:
                        s_str = f"{p} ({nt})"
                        if s_str not in stars:
                            stars.append(s_str)
                if not stars:
                    coach_parts = []
                    if norm_a in year_coaches:
                        c_name, c_role = year_coaches[norm_a]
                        coach_parts.append(f"{c_name} ({team_a})")
                    if norm_b in year_coaches:
                        c_name, c_role = year_coaches[norm_b]
                        coach_parts.append(f"{c_name} ({team_b})")
                    stars = coach_parts

                if stars:
                    notable = ", ".join(stars[:3])
                else:
                    notable = f"{team_a} vs {team_b} Starters"

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

        with open(csv_path, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=HEADERS)
            writer.writeheader()
            writer.writerows(final_rows)

        total_games_updated += len(final_rows)
        years_processed += 1

    print(f"\nSuccessfully processed {years_processed} years (1900-2025)!")
    print(f"Total games across all files: {total_games_updated}")

if __name__ == "__main__":
    main()
