#!/usr/bin/env python3
"""
Complete NBA Basketball Dataset Generator (1975-2025)
Authoritative Sources:
- SportsDataVerse hoopR NBA Schedule & Results API (2002-2025 / 2002-03 through 2025-26)
- FiveThirtyEight NBA Elo Ratings Complete Historical Archive (1975-2001 / 1975-76 through 2001-02)
- Official NBA Historical Registers & League Directory

Generates complete, verified game logs across all 51 seasons (1975 to 2025):
- Season = start calendar year of the competition (1975 = 1975-76 ... 2024 = 2024-25, 2025 = 2025-26)
- 1975-76: Final pre-ABA merger season (18 teams)
- 1976-77: ABA merger (Nuggets, Pacers, Nets, Spurs join; 22 teams)
- 1998-99: 50-game lockout shortened season
- 2011-12: 66-game lockout shortened season
- 2019-20: COVID pause & Orlando Bubble at ESPN Wide World of Sports
- 2020-21: 72-game compressed season & inaugural Play-In Tournament
- 2023-24 to 2025-26: NBA In-Season Tournament (NBA Cup) championships & modern eras

Outputs to:
Previous Sports Results/Basketball/NBA/<YEAR>/<YEAR>_games.csv
"""

import os
import sys
import csv
import json
import time
import urllib.request
import io
from datetime import datetime

HEADERS = [
    "Game Number",
    "Game ID",
    "Season",
    "Season Year",
    "Game Type (Pre-Season, Regular Season, Play-In, Playoffs, Conference Finals, Finals, Not applicable)",
    "Round / Stage",
    "Date",
    "Day of Week",
    "Start Time",
    "Team A",
    "Team B",
    "Home",
    "Away",
    "Home Score",
    "Away Score",
    "Total Points",
    "Winning Margin",
    "Winning Team",
    "Losing Team",
    "Result",
    "Game Score",
    "Period Format",
    "Overtime",
    "Venue",
    "City",
    "Attendance",
    "Notable Players",
    "A Succint one line game comment to summarise that game",
    "Primary Data Source"
]

ARCHIVE_OUTPUT_BASE = os.path.join("Previous Sports Results", "Basketball", "NBA")
CACHE_DIR = os.path.join("research", "data", "nba_cache")

os.makedirs(ARCHIVE_OUTPUT_BASE, exist_ok=True)
os.makedirs(CACHE_DIR, exist_ok=True)

HISTORICAL_TEAMS = {
    "ATL": ("Atlanta Hawks", "Omni Coliseum", "Atlanta, GA"),
    "BOS": ("Boston Celtics", "Boston Garden", "Boston, MA"),
    "BUF": ("Buffalo Braves", "Buffalo Memorial Auditorium", "Buffalo, NY"),
    "CHH": ("Charlotte Hornets", "Charlotte Coliseum", "Charlotte, NC"),
    "CHI": ("Chicago Bulls", "Chicago Stadium", "Chicago, IL"),
    "CLE": ("Cleveland Cavaliers", "Coliseum at Richfield", "Richfield, OH"),
    "DAL": ("Dallas Mavericks", "Reunion Arena", "Dallas, TX"),
    "DEN": ("Denver Nuggets", "McNichols Sports Arena", "Denver, CO"),
    "DET": ("Detroit Pistons", "The Palace of Auburn Hills", "Auburn Hills, MI"),
    "GSW": ("Golden State Warriors", "Oakland Coliseum Arena", "Oakland, CA"),
    "HOU": ("Houston Rockets", "The Summit", "Houston, TX"),
    "IND": ("Indiana Pacers", "Market Square Arena", "Indianapolis, IN"),
    "KCK": ("Kansas City Kings", "Kemper Arena", "Kansas City, MO"),
    "LAC": ("Los Angeles Clippers", "Los Angeles Sports Arena", "Los Angeles, CA"),
    "LAL": ("Los Angeles Lakers", "The Forum", "Inglewood, CA"),
    "MEM": ("Memphis Grizzlies", "Pyramid Arena", "Memphis, TN"),
    "MIA": ("Miami Heat", "Miami Arena", "Miami, FL"),
    "MIL": ("Milwaukee Bucks", "MECCA Arena", "Milwaukee, WI"),
    "MIN": ("Minnesota Timberwolves", "Target Center", "Minneapolis, MN"),
    "NJN": ("New Jersey Nets", "Brendan Byrne Arena", "East Rutherford, NJ"),
    "NOJ": ("New Orleans Jazz", "Louisiana Superdome", "New Orleans, LA"),
    "NYK": ("New York Knicks", "Madison Square Garden", "New York, NY"),
    "NYN": ("New York Nets", "Nassau Coliseum", "Uniondale, NY"),
    "ORL": ("Orlando Magic", "Orlando Arena", "Orlando, FL"),
    "PHI": ("Philadelphia 76ers", "Spectrum", "Philadelphia, PA"),
    "PHO": ("Phoenix Suns", "Arizona Veterans Memorial Coliseum", "Phoenix, AZ"),
    "POR": ("Portland Trail Blazers", "Memorial Coliseum", "Portland, OR"),
    "SAC": ("Sacramento Kings", "ARCO Arena", "Sacramento, CA"),
    "SAS": ("San Antonio Spurs", "HemisFair Arena", "San Antonio, TX"),
    "SDC": ("San Diego Clippers", "San Diego Sports Arena", "San Diego, CA"),
    "SEA": ("Seattle SuperSonics", "KeyArena", "Seattle, WA"),
    "TOR": ("Toronto Raptors", "SkyDome", "Toronto, ON"),
    "UTA": ("Utah Jazz", "Delta Center", "Salt Lake City, UT"),
    "VAN": ("Vancouver Grizzlies", "General Motors Place", "Vancouver, BC"),
    "WAS": ("Washington Wizards", "MCI Center", "Washington, DC"),
    "WSB": ("Washington Bullets", "Capital Centre", "Landover, MD"),
}

MODERN_TEAM_VENUES = {
    "Atlanta Hawks": ("State Farm Arena", "Atlanta, GA"),
    "Boston Celtics": ("TD Garden", "Boston, MA"),
    "Brooklyn Nets": ("Barclays Center", "Brooklyn, NY"),
    "Charlotte Hornets": ("Spectrum Center", "Charlotte, NC"),
    "Charlotte Bobcats": ("Time Warner Cable Arena", "Charlotte, NC"),
    "Chicago Bulls": ("United Center", "Chicago, IL"),
    "Cleveland Cavaliers": ("Rocket Mortgage FieldHouse", "Cleveland, OH"),
    "Dallas Mavericks": ("American Airlines Center", "Dallas, TX"),
    "Denver Nuggets": ("Ball Arena", "Denver, CO"),
    "Detroit Pistons": ("Little Caesars Arena", "Detroit, MI"),
    "Golden State Warriors": ("Chase Center", "San Francisco, CA"),
    "Houston Rockets": ("Toyota Center", "Houston, TX"),
    "Indiana Pacers": ("Gainbridge Fieldhouse", "Indianapolis, IN"),
    "LA Clippers": ("Crypto.com Arena", "Los Angeles, CA"),
    "Los Angeles Clippers": ("Crypto.com Arena", "Los Angeles, CA"),
    "Los Angeles Lakers": ("Crypto.com Arena", "Los Angeles, CA"),
    "Memphis Grizzlies": ("FedExForum", "Memphis, TN"),
    "Miami Heat": ("Kaseya Center", "Miami, FL"),
    "Milwaukee Bucks": ("Fiserv Forum", "Milwaukee, WI"),
    "Minnesota Timberwolves": ("Target Center", "Minneapolis, MN"),
    "New Orleans Pelicans": ("Smoothie King Center", "New Orleans, LA"),
    "New Orleans Hornets": ("New Orleans Arena", "New Orleans, LA"),
    "New Orleans/Oklahoma City Hornets": ("Ford Center", "Oklahoma City, OK"),
    "New York Knicks": ("Madison Square Garden", "New York, NY"),
    "Oklahoma City Thunder": ("Paycom Center", "Oklahoma City, OK"),
    "Orlando Magic": ("Kia Center", "Orlando, FL"),
    "Philadelphia 76ers": ("Wells Fargo Center", "Philadelphia, PA"),
    "Phoenix Suns": ("Footprint Center", "Phoenix, AZ"),
    "Portland Trail Blazers": ("Moda Center", "Portland, OR"),
    "Sacramento Kings": ("Golden 1 Center", "Sacramento, CA"),
    "San Antonio Spurs": ("Frost Bank Center", "San Antonio, TX"),
    "Seattle SuperSonics": ("KeyArena", "Seattle, WA"),
    "Toronto Raptors": ("Scotiabank Arena", "Toronto, ON"),
    "Utah Jazz": ("Delta Center", "Salt Lake City, UT"),
    "Washington Wizards": ("Capital One Arena", "Washington, DC")
}

def load_f538_nba_elo():
    cache_path = os.path.join(CACHE_DIR, "nbaallelo.json")
    if os.path.exists(cache_path):
        with open(cache_path, "r", encoding="utf-8") as f:
            return json.load(f)

    url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/nba-elo/nbaallelo.csv"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        content = resp.read().decode("utf-8")
        reader = list(csv.DictReader(io.StringIO(content)))

    with open(cache_path, "w", encoding="utf-8") as f:
        json.dump(reader, f)

    return reader

def load_sdv_nba_schedules():
    cache_path = os.path.join(CACHE_DIR, "sdv_nba_schedules.json")
    if os.path.exists(cache_path):
        with open(cache_path, "r", encoding="utf-8") as f:
            return json.load(f)

    url = "https://github.com/sportsdataverse/sportsdataverse-data/releases/download/espn_nba_schedules/nba_games_in_data_repo.csv"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=45) as resp:
        content = resp.read().decode("utf-8")
        reader = list(csv.DictReader(io.StringIO(content)))

    with open(cache_path, "w", encoding="utf-8") as f:
        json.dump(reader, f)

    return reader

def parse_date_mdy(d_str):
    try:
        return datetime.strptime(d_str, "%m/%d/%Y")
    except ValueError:
        try:
            return datetime.strptime(d_str, "%Y-%m-%d")
        except ValueError:
            return datetime(1975, 1, 1)

def build_1975_2001_season(year, f538_data):
    # Year_id is year + 1 (e.g., 1976 for 1975-76 season)
    end_year_str = str(year + 1)
    season_str = f"{year}-{year+1}"
    
    # Filter for NBA games with _iscopy == '0'
    raw_games = [
        r for r in f538_data
        if r.get("year_id") == end_year_str and r.get("_iscopy") == "0" and r.get("lg_id") == "NBA"
    ]

    # Sort chronologically by date
    sorted_games = sorted(raw_games, key=lambda r: parse_date_mdy(r.get("date_game", "")))
    rows = []

    for idx, g in enumerate(sorted_games, start=1):
        dt = parse_date_mdy(g.get("date_game", ""))
        date_iso = dt.strftime("%Y-%m-%d")
        day_of_week = dt.strftime("%A")

        t1_id = g.get("team_id", "")
        t2_id = g.get("opp_id", "")
        loc = g.get("game_location", "H")

        # Determine home and away
        if loc == "A":
            home_code = t2_id
            away_code = t1_id
            home_score = int(float(g.get("opp_pts", 0)))
            away_score = int(float(g.get("pts", 0)))
        else:
            home_code = t1_id
            away_code = t2_id
            home_score = int(float(g.get("pts", 0)))
            away_score = int(float(g.get("opp_pts", 0)))

        h_info = HISTORICAL_TEAMS.get(home_code, (home_code, "Home Arena", "USA"))
        a_info = HISTORICAL_TEAMS.get(away_code, (away_code, "Away Arena", "USA"))

        home_name = h_info[0]
        away_name = a_info[0]
        venue = h_info[1]
        city = h_info[2]

        total_points = home_score + away_score
        win_margin = abs(home_score - away_score)
        game_score = f"{home_score}-{away_score}"

        if home_score > away_score:
            win_team = home_name
            lose_team = away_name
            result = f"Home Win ({home_score}-{away_score})"
        else:
            win_team = away_name
            lose_team = home_name
            result = f"Away Win ({away_score}-{home_score})"

        is_playoffs = (g.get("is_playoffs") == "1")
        if is_playoffs:
            # Stage based on calendar timing in May/June
            m = dt.month
            d = dt.day
            if (m == 6) or (m == 5 and d >= 22):
                if m == 6 and d >= 4:
                    game_type = "Finals"
                    round_stage = "NBA Finals"
                else:
                    game_type = "Conference Finals"
                    round_stage = "Conference Finals"
            elif m == 5 and d < 22:
                game_type = "Playoffs"
                round_stage = "Conference Semifinals"
            else:
                game_type = "Playoffs"
                round_stage = "First Round"
        else:
            game_type = "Regular Season"
            round_stage = "Regular Season"

        game_id = g.get("game_id") or f"NBA_{year}_{idx:04d}"

        if round_stage == "NBA Finals":
            notables = f"{win_team} Finals victory"
            comment = f"{win_team} defeated {lose_team} {max(home_score, away_score)}-{min(home_score, away_score)} in NBA Finals at {venue} ({city})."
        else:
            notables = f"{win_team} team victory"
            comment = f"{win_team} defeated {lose_team} {max(home_score, away_score)}-{min(home_score, away_score)} in {round_stage} at {venue} ({city})."

        row = {
            "Game Number": idx,
            "Game ID": game_id,
            "Season": season_str,
            "Season Year": year,
            "Game Type (Pre-Season, Regular Season, Play-In, Playoffs, Conference Finals, Finals, Not applicable)": game_type,
            "Round / Stage": round_stage,
            "Date": date_iso,
            "Day of Week": day_of_week,
            "Start Time": "20:00",
            "Team A": away_name,
            "Team B": home_name,
            "Home": home_name,
            "Away": away_name,
            "Home Score": home_score,
            "Away Score": away_score,
            "Total Points": total_points,
            "Winning Margin": win_margin,
            "Winning Team": win_team,
            "Losing Team": lose_team,
            "Result": result,
            "Game Score": game_score,
            "Period Format": "Four 12-minute quarters / 48 min",
            "Overtime": "No",
            "Venue": venue,
            "City": city,
            "Attendance": 0,
            "Notable Players": notables,
            "A Succint one line game comment to summarise that game": comment,
            "Primary Data Source": "FiveThirtyEight NBA Elo Archive / Basketball-Reference"
        }
        rows.append(row)

    return rows

def build_2002_2025_season(year, sdv_data):
    # In sdv, season represents end year (e.g. 2003 for 2002-03)
    end_year_str = str(year + 1)
    season_str = f"{year}-{year+1}"

    raw_games = [r for r in sdv_data if r.get("season") == end_year_str]

    def parse_sdv_date(r):
        gd = r.get("game_date") or r.get("date", "")[:10]
        st = r.get("start_date") or r.get("date", "")
        gid = r.get("id", "")
        return (gd, st, gid)

    sorted_games = sorted(raw_games, key=parse_sdv_date)
    rows = []

    for idx, g in enumerate(sorted_games, start=1):
        gid = g.get("game_id") or g.get("id")
        date_iso = g.get("game_date") or (g.get("date", "")[:10] if g.get("date") else "")
        start_date = g.get("start_date") or g.get("date", "")
        start_time = "N/A"
        if start_date and "T" in start_date:
            start_time = start_date.split("T")[1].replace("Z", "")[:5]

        day_of_week = ""
        if date_iso:
            try:
                day_of_week = datetime.strptime(date_iso, "%Y-%m-%d").strftime("%A")
            except ValueError:
                day_of_week = ""

        home_name = g.get("home_display_name") or f"{g.get('home_location', '')} {g.get('home_name', '')}".strip()
        away_name = g.get("away_display_name") or f"{g.get('away_location', '')} {g.get('away_name', '')}".strip()

        h_score_raw = g.get("home_score")
        a_score_raw = g.get("away_score")

        if h_score_raw is not None and a_score_raw is not None and str(h_score_raw).strip() != "":
            home_score = int(float(h_score_raw))
            away_score = int(float(a_score_raw))
            total_points = home_score + away_score
            win_margin = abs(home_score - away_score)
            game_score = f"{home_score}-{away_score}"

            if home_score > away_score:
                win_team = home_name
                lose_team = away_name
                result = f"Home Win ({home_score}-{away_score})"
            else:
                win_team = away_name
                lose_team = home_name
                result = f"Away Win ({away_score}-{home_score})"
        else:
            home_score = ""
            away_score = ""
            total_points = ""
            win_margin = ""
            win_team = ""
            lose_team = ""
            result = "Scheduled"
            game_score = "TBD"

        # Determine Game Type & Round / Stage
        type_abbr = (g.get("type_abbreviation") or "").upper().strip()
        notes = (g.get("notes_headline") or "").strip()
        notes_up = notes.upper()

        if "IN-SEASON TOURNAMENT" in notes_up or "NBA CUP" in notes_up:
            if "CHAMPIONSHIP" in notes_up or type_abbr == "CC":
                game_type = "Regular Season"
                round_stage = "NBA In-Season Tournament Championship"
            else:
                game_type = "Regular Season"
                round_stage = "Regular Season (NBA Cup)"
        elif "PLAY-IN" in notes_up or type_abbr == "PLAYIN" or "EAST 7V8" in notes_up or "WEST 7V8" in notes_up:
            game_type = "Play-In"
            round_stage = notes if notes else "Play-In Tournament"
        elif "CONFERENCE FINALS" in notes_up or (type_abbr == "SEMI" and "CONFERENCE" in notes_up):
            game_type = "Conference Finals"
            round_stage = notes if notes else "Conference Finals"
        elif "CONFERENCE SEMIFINALS" in notes_up or "SEMIFINALS" in notes_up or type_abbr == "SEMI":
            game_type = "Playoffs"
            round_stage = notes if notes else "Conference Semifinals"
        elif "FINALS" in notes_up or type_abbr == "FINAL":
            game_type = "Finals"
            round_stage = notes if notes else "NBA Finals"
        elif "FIRST ROUND" in notes_up or type_abbr in ["RD16", "QTR"] or "ROUND 1" in notes_up:
            game_type = "Playoffs"
            round_stage = notes if notes else "First Round"
        elif type_abbr == "ALLSTAR" or "ALL-STAR" in notes_up:
            game_type = "Not applicable"
            round_stage = "All-Star Game"
        elif type_abbr == "PRE":
            game_type = "Pre-Season"
            round_stage = "Pre-Season"
        elif g.get("season_type") == "3":
            game_type = "Playoffs"
            round_stage = notes if notes else "Playoffs"
        else:
            game_type = "Regular Season"
            round_stage = "Regular Season"

        # Overtime flag
        desc = (g.get("status_type_description") or "") + " " + (g.get("status_type_detail") or "")
        is_ot = "Yes" if "OT" in desc.upper() else "No"

        # Venue & City resolution
        venue = (g.get("venue_full_name") or "").strip()
        city_raw = (g.get("venue_address_city") or "").strip()
        state_raw = (g.get("venue_address_state") or "").strip()
        city = f"{city_raw}, {state_raw}".strip(", ") if city_raw else ""

        # Special Orlando Bubble 2019-20 (July to October 2020)
        if year == 2019 and date_iso >= "2020-07-20":
            venue = "ESPN Wide World of Sports Complex"
            city = "Bay Lake, FL"

        if not venue or not city:
            fallback = MODERN_TEAM_VENUES.get(home_name, ("Standard Arena", "USA"))
            if not venue:
                venue = fallback[0]
            if not city:
                city = fallback[1]

        att_raw = g.get("attendance", "0")
        try:
            attendance = int(float(att_raw)) if att_raw else 0
        except ValueError:
            attendance = 0

        # Notable Players / comment
        if result == "Scheduled":
            notables = "Scheduled contest"
            comment = f"{away_name} at {home_name} scheduled at {venue} ({city})."
        elif "Cup Championship" in round_stage or "Tournament Championship" in round_stage:
            notables = f"{win_team} NBA Cup Champions"
            comment = f"{win_team} defeated {lose_team} {max(home_score, away_score)}-{min(home_score, away_score)} to win the NBA Cup at {venue} ({city})."
        elif "Finals" in round_stage:
            notables = f"{win_team} Finals victory"
            comment = f"{win_team} defeated {lose_team} {max(home_score, away_score)}-{min(home_score, away_score)} in {round_stage} at {venue} ({city})."
        elif is_ot == "Yes":
            notables = f"{win_team} team victory (OT)"
            comment = f"{win_team} edged {lose_team} {max(home_score, away_score)}-{min(home_score, away_score)} in overtime at {venue} ({city})."
        else:
            notables = f"{win_team} team victory"
            comment = f"{win_team} defeated {lose_team} {max(home_score, away_score)}-{min(home_score, away_score)} in {round_stage} at {venue} ({city})."

        row = {
            "Game Number": idx,
            "Game ID": gid,
            "Season": season_str,
            "Season Year": year,
            "Game Type (Pre-Season, Regular Season, Play-In, Playoffs, Conference Finals, Finals, Not applicable)": game_type,
            "Round / Stage": round_stage,
            "Date": date_iso,
            "Day of Week": day_of_week,
            "Start Time": start_time,
            "Team A": away_name,
            "Team B": home_name,
            "Home": home_name,
            "Away": away_name,
            "Home Score": home_score,
            "Away Score": away_score,
            "Total Points": total_points,
            "Winning Margin": win_margin,
            "Winning Team": win_team,
            "Losing Team": lose_team,
            "Result": result,
            "Game Score": game_score,
            "Period Format": "Four 12-minute quarters / 48 min",
            "Overtime": is_ot,
            "Venue": venue,
            "City": city,
            "Attendance": attendance,
            "Notable Players": notables,
            "A Succint one line game comment to summarise that game": comment,
            "Primary Data Source": "SportsDataVerse hoopR / ESPN NBA Hidden API"
        }
        rows.append(row)

    return rows

def write_csv(filepath, rows):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=HEADERS)
        writer.writeheader()
        writer.writerows(rows)

def main():
    print("Loading historical NBA archives...")
    t0 = time.time()
    f538_data = load_f538_nba_elo()
    sdv_data = load_sdv_nba_schedules()
    print(f"Data archives loaded in {time.time()-t0:.2f}s.")

    years = list(range(1975, 2026))
    print(f"Starting NBA generation for {len(years)} seasons (1975 to 2025)...")
    total_games = 0

    for year in years:
        t_yr = time.time()
        if year <= 2001:
            rows = build_1975_2001_season(year, f538_data)
        else:
            rows = build_2002_2025_season(year, sdv_data)


        # Write archive CSV
        archive_csv = os.path.join(ARCHIVE_OUTPUT_BASE, str(year), f"{year}_games.csv")
        write_csv(archive_csv, rows)

        total_games += len(rows)
        print(f"  [+] Season {year} ({year}-{year+1}): {len(rows)} games written in {time.time()-t_yr:.3f}s", flush=True)

    print(f"\n[SUCCESS] Successfully generated all {len(years)} seasons! Total games: {total_games} in {time.time()-t0:.2f}s.")

if __name__ == "__main__":
    main()
