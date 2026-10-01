import csv
import json
import os
import re
from datetime import datetime

# Load data files
RESULTS_CSV = "research/data/nbl_results_wide.csv"
BOX_TEAM_CSV = "research/data/nbl_box_team.csv"
PRESEASON_JSON = "research/data/nbl_rosetta_preseason.json"

ROOT_OUTPUT_DIR = "NBL_CSVs"
ARCHIVE_OUTPUT_BASE = os.path.join("Previous Sports Results", "Basketball", "NBL")

os.makedirs(ROOT_OUTPUT_DIR, exist_ok=True)
os.makedirs(ARCHIVE_OUTPUT_BASE, exist_ok=True)

CSV_HEADERS = [
    "Game Number",
    "Game ID",
    "Season",
    "Season Year",
    "Game Type (Pre-Season, Regular Season, Play-In, Playoffs, Conference Finals, Finals, Not applicable)",
    "Round / Stage",
    "Date",
    "Day of Week",
    "Start Time (Local)",
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
    "Home Q1 / Half 1",
    "Away Q1 / Half 1",
    "Home Q2 / Half 2",
    "Away Q2 / Half 2",
    "Home Q3",
    "Away Q3",
    "Home Q4",
    "Away Q4",
    "Home OT",
    "Away OT",
    "Venue",
    "City / State",
    "Attendance",
    "Notable Players",
    "A Succint one line game comment to summarise that game",
    "Primary Data Source"
]

def get_period_format(season_str):
    try:
        yr = int(season_str[:4])
    except:
        return "Four 10-minute quarters (40 min)"
    if yr < 1979:
        return "N/A"
    elif yr <= 1983:
        return "Two 20-minute halves (40 min)"
    elif yr <= 2008:
        return "Four 12-minute quarters (48 min)"
    else:
        return "Four 10-minute quarters (40 min)"

def get_day_of_week(date_str):
    try:
        d = datetime.strptime(date_str, "%Y-%m-%d")
        return d.strftime("%A")
    except:
        return ""

def load_box_team():
    box_by_match = {}
    if not os.path.exists(BOX_TEAM_CSV):
        return box_by_match
    with open(BOX_TEAM_CSV, "r", encoding="utf-8", errors="ignore") as f:
        reader = csv.DictReader(f)
        for row in reader:
            mid = row.get("match_id", "")
            if not mid:
                continue
            if mid not in box_by_match:
                box_by_match[mid] = {}
            ha = row.get("home_away", "").lower()
            box_by_match[mid][ha] = row
    return box_by_match

def load_preseason_matches():
    preseason_matches_by_year = {}
    if not os.path.exists(PRESEASON_JSON):
        return preseason_matches_by_year
    with open(PRESEASON_JSON, "r", encoding="utf-8", errors="ignore") as f:
        data = json.load(f)
    for sid, sinfo in data.items():
        syear = str(sinfo.get("year", ""))
        sname = sinfo.get("name", "Pre-Season")
        for m in sinfo.get("matches", []):
            if m.get("match_status") != "complete":
                continue
            h_score = m.get("home_score")
            a_score = m.get("away_score")
            if h_score is None or a_score is None:
                continue
            if syear not in preseason_matches_by_year:
                preseason_matches_by_year[syear] = []
            
            # Extract date
            st = m.get("start_time_datetime") or m.get("start_time") or ""
            date_val = st[:10] if len(st) >= 10 else ""
            time_val = st[11:16] if len(st) >= 16 else ""

            home_team = m.get("home_team", {}).get("name", "Home Team")
            away_team = m.get("away_team", {}).get("name", "Away Team")
            venue_obj = m.get("venue") or {}
            venue_name = venue_obj.get("name") or "Various Venues"
            city = venue_obj.get("state") or venue_obj.get("suburb") or "Australia"

            preseason_matches_by_year[syear].append({
                "source": "rosetta_preseason",
                "match_id": m.get("id") or m.get("external_id") or "",
                "season": sname,
                "season_year": syear,
                "game_type": "Pre-Season / NBL Blitz" if "blitz" in sname.lower() else "Pre-Season",
                "round": sname,
                "date": date_val,
                "time": time_val,
                "home_team": home_team,
                "away_team": away_team,
                "home_score": int(h_score),
                "away_score": int(a_score),
                "venue": venue_name,
                "city": city,
                "attendance": m.get("attendance") or ""
            })
    return preseason_matches_by_year

def classify_game_type(season_str, round_num, match_type, is_last_round, is_penultimate_round, round_matches_count, match_num, total_matches):
    match_type_upper = (match_type or "").upper()
    if match_type_upper == "FINALS":
        # Determine specific finals stage
        try:
            r = int(round_num)
        except:
            r = 0
        if is_last_round:
            return "Finals (Grand Final)", "Grand Final"
        elif is_penultimate_round:
            return "Playoffs (Semi-Finals)", "Semi-Finals"
        else:
            return "Play-In / Qualifying Finals", f"Finals Round {round_num}"
    
    # Check for historical seasons (pre-2009) where match_type is 'REGULAR'
    try:
        yr = int(season_str[:4])
    except:
        yr = 2000
    
    if yr < 2009:
        if is_last_round:
            return "Finals (Grand Final)", "Grand Final"
        elif is_penultimate_round and round_matches_count <= 6:
            return "Playoffs (Semi-Finals)", "Semi-Finals"
        elif yr >= 1986 and round_num.isdigit() and int(round_num) >= 20 and round_matches_count <= 6:
            return "Playoffs (Elimination / Quarter-Finals)", f"Finals Round {round_num}"

    # Default to regular season
    return "Regular Season", f"Round {round_num}"

def build_all_seasons():
    box_data = load_box_team()
    preseason_data = load_preseason_matches()

    with open(RESULTS_CSV, "r", encoding="utf-8", errors="ignore") as f:
        all_results = list(csv.DictReader(f))

    # Group official matches by season key
    matches_by_season = {}
    for r in all_results:
        s = r.get("season", "").strip()
        if not s:
            continue
        if s not in matches_by_season:
            matches_by_season[s] = []
        matches_by_season[s].append(r)

    # Process each year from 1975 to 2025
    for year in range(1975, 2026):
        year_str = str(year)
        games = []

        if year < 1979:
            # Pre-NBL Era
            games.append({
                "Game Number": 1,
                "Game ID": f"NBL_{year_str}_PRE_NBL",
                "Season": year_str,
                "Season Year": year_str,
                "Game Type (Pre-Season, Regular Season, Play-In, Playoffs, Conference Finals, Finals, Not applicable)": "Not applicable",
                "Round / Stage": "Pre-Establishment Period",
                "Date": f"{year_str}-01-01",
                "Day of Week": get_day_of_week(f"{year_str}-01-01"),
                "Start Time (Local)": "",
                "Team A": "Pre-NBL Era (National Titles & Club Championships)",
                "Team B": "NBL Not Yet Established (Founded August 1978; Inaugural Season 1979)",
                "Home": "Pre-NBL Era",
                "Away": "NBL Not Yet Established",
                "Home Score": "",
                "Away Score": "",
                "Total Points": "",
                "Winning Margin": "",
                "Winning Team": "",
                "Losing Team": "",
                "Result": "No Official NBL Competition Held",
                "Game Score": "N/A",
                "Period Format": "N/A",
                "Overtime": "No",
                "Home Q1 / Half 1": "",
                "Away Q1 / Half 1": "",
                "Home Q2 / Half 2": "",
                "Away Q2 / Half 2": "",
                "Home Q3": "",
                "Away Q3": "",
                "Home Q4": "",
                "Away Q4": "",
                "Home OT": "",
                "Away OT": "",
                "Venue": "Australian Domestic Basketball Circuit",
                "City / State": "Australia",
                "Attendance": "",
                "Notable Players": "Pre-NBL Australian Basketball Era (Eddie Palubinskas, Ken Cole, Ray Tomlinson)",
                "A Succint one line game comment to summarise that game": f"The National Basketball League (NBL) was not yet founded in {year_str}; national basketball was contested via state leagues, National Titles, and the Australian Club Championships prior to the NBL's 1979 inaugural season.",
                "Primary Data Source": "National Basketball League (NBL) Historical Register & Basketball Australia Archives"
            })
        else:
            # Collect seasons that map to this year folder
            # For 1998, we have both '1998' (winter) and '1998-1999' (summer)
            # For 1979-1997, single year key '1979', etc.
            # For 1999-2024, summer season key e.g. '1999-2000' for 1999, '2024-2025' for 2024
            # For 2025, '2025-2026' for 2025
            seasons_to_include = []
            if year == 1998:
                seasons_to_include = ["1998", "1998-1999"]
            elif year < 1998:
                seasons_to_include = [year_str]
            elif year == 2025:
                seasons_to_include = ["2025-2026"]
            else:
                next_yr = str(year + 1)
                seasons_to_include = [f"{year}-{next_yr}"]

            # Add pre-season games for this year if available
            ps_matches = preseason_data.get(year_str, [])
            for pm in ps_matches:
                h_team = pm["home_team"]
                a_team = pm["away_team"]
                h_score = pm["home_score"]
                a_score = pm["away_score"]
                tot = h_score + a_score
                margin = abs(h_score - a_score)
                w_team = h_team if h_score > a_score else (a_team if a_score > h_score else "Tie")
                l_team = a_team if h_score > a_score else (h_team if a_score > h_score else "Tie")
                res_str = f"Home Win ({h_score}-{a_score})" if h_score > a_score else f"Away Win ({a_score}-{h_score})"

                games.append({
                    "Game Number": 0,  # will re-index
                    "Game ID": f"NBL_PRE_{pm['match_id']}",
                    "Season": pm["season"],
                    "Season Year": year_str,
                    "Game Type (Pre-Season, Regular Season, Play-In, Playoffs, Conference Finals, Finals, Not applicable)": pm["game_type"],
                    "Round / Stage": pm["round"],
                    "Date": pm["date"],
                    "Day of Week": get_day_of_week(pm["date"]),
                    "Start Time (Local)": pm["time"],
                    "Team A": h_team,
                    "Team B": a_team,
                    "Home": h_team,
                    "Away": a_team,
                    "Home Score": h_score,
                    "Away Score": a_score,
                    "Total Points": tot,
                    "Winning Margin": margin,
                    "Winning Team": w_team,
                    "Losing Team": l_team,
                    "Result": res_str,
                    "Game Score": f"{h_score}-{a_score}",
                    "Period Format": get_period_format(year_str),
                    "Overtime": "No",
                    "Home Q1 / Half 1": "",
                    "Away Q1 / Half 1": "",
                    "Home Q2 / Half 2": "",
                    "Away Q2 / Half 2": "",
                    "Home Q3": "",
                    "Away Q3": "",
                    "Home Q4": "",
                    "Away Q4": "",
                    "Home OT": "",
                    "Away OT": "",
                    "Venue": pm["venue"],
                    "City / State": pm["city"],
                    "Attendance": pm["attendance"],
                    "Notable Players": f"{w_team} team victory",
                    "A Succint one line game comment to summarise that game": f"{w_team} defeated {l_team} {max(h_score, a_score)}-{min(h_score, a_score)} in {pm['season']} at {pm['venue']}.",
                    "Primary Data Source": "NBL Official Rosetta API (prod.rosetta.nbl.com.au)"
                })

            # Process official league season matches
            for s_key in seasons_to_include:
                s_matches = matches_by_season.get(s_key, [])
                if not s_matches:
                    continue

                # Sort matches chronologically by match_time
                s_matches.sort(key=lambda m: (m.get("match_time") or "9999", int(m.get("match_number") or "0") if (m.get("match_number") or "").isdigit() else 0))

                # Identify max rounds for playoffs detection
                rounds_int = [int(m["round_number"]) for m in s_matches if (m.get("round_number") or "").isdigit()]
                max_r = max(rounds_int) if rounds_int else 1
                r_counts = {}
                for m in s_matches:
                    rn = m.get("round_number") or "1"
                    r_counts[rn] = r_counts.get(rn, 0) + 1

                for idx, m in enumerate(s_matches):
                    rn = m.get("round_number") or "1"
                    rn_int = int(rn) if rn.isdigit() else 0
                    is_last_round = (rn_int == max_r)
                    is_penultimate = (rn_int == max_r - 1)
                    m_count_in_round = r_counts.get(rn, 10)
                    m_type = m.get("match_type") or "REGULAR"

                    game_type, round_label = classify_game_type(
                        s_key, rn, m_type, is_last_round, is_penultimate, m_count_in_round, idx + 1, len(s_matches)
                    )

                    h_team = m.get("home_team_name") or "Home"
                    a_team = m.get("away_team_name") or "Away"
                    h_score_raw = m.get("home_score_string") or ""
                    a_score_raw = m.get("away_score_string") or ""

                    h_score = int(h_score_raw) if h_score_raw.isdigit() else 0
                    a_score = int(a_score_raw) if a_score_raw.isdigit() else 0
                    tot = h_score + a_score if (h_score_raw.isdigit() and a_score_raw.isdigit()) else ""
                    margin = abs(h_score - a_score) if (h_score_raw.isdigit() and a_score_raw.isdigit()) else ""

                    if h_score > a_score:
                        w_team, l_team = h_team, a_team
                        res_str = f"Home Win ({h_score}-{a_score})"
                    elif a_score > h_score:
                        w_team, l_team = a_team, h_team
                        res_str = f"Away Win ({a_score}-{h_score})"
                    else:
                        w_team, l_team = "Tie", "Tie"
                        res_str = f"Tie ({h_score}-{a_score})"

                    dt_raw = m.get("match_time") or ""
                    date_val = dt_raw[:10] if len(dt_raw) >= 10 else ""
                    time_val = dt_raw[11:16] if len(dt_raw) >= 16 else ""

                    # Quarter scores from box_data if available
                    mid = m.get("match_id", "")
                    box_info = box_data.get(mid, {})
                    h_box = box_info.get("home", {})
                    a_box = box_info.get("away", {})

                    h_q1 = h_box.get("p1_score", "")
                    a_q1 = a_box.get("p1_score", "")
                    h_q2 = h_box.get("p2_score", "")
                    a_q2 = a_box.get("p2_score", "")
                    h_q3 = h_box.get("p3_score", "")
                    a_q3 = a_box.get("p3_score", "")
                    h_q4 = h_box.get("p4_score", "")
                    a_q4 = a_box.get("p4_score", "")
                    h_ot = h_box.get("ot_score", "") if h_box.get("ot_score") not in ["NA", None] else ""
                    a_ot = a_box.get("ot_score", "") if a_box.get("ot_score") not in ["NA", None] else ""

                    extra_periods = m.get("extra_periods_used", "0")
                    is_ot = "Yes" if extra_periods in ["1", "2", "3"] or h_ot or a_ot else "No"

                    venue = m.get("venue_name") or "Various Arenas"
                    att = m.get("attendance") if m.get("attendance") not in ["0", "NA", None, ""] else ""

                    recap = f"{w_team} defeated {l_team} {max(h_score, a_score)}-{min(h_score, a_score)} in {round_label} ({s_key}) at {venue}."

                    games.append({
                        "Game Number": 0,
                        "Game ID": f"NBL_{s_key.replace('-', '_')}_{mid}",
                        "Season": s_key,
                        "Season Year": year_str,
                        "Game Type (Pre-Season, Regular Season, Play-In, Playoffs, Conference Finals, Finals, Not applicable)": game_type,
                        "Round / Stage": round_label,
                        "Date": date_val,
                        "Day of Week": get_day_of_week(date_val),
                        "Start Time (Local)": time_val,
                        "Team A": h_team,
                        "Team B": a_team,
                        "Home": h_team,
                        "Away": a_team,
                        "Home Score": h_score,
                        "Away Score": a_score,
                        "Total Points": tot,
                        "Winning Margin": margin,
                        "Winning Team": w_team,
                        "Losing Team": l_team,
                        "Result": res_str,
                        "Game Score": f"{h_score}-{a_score}",
                        "Period Format": get_period_format(s_key),
                        "Overtime": is_ot,
                        "Home Q1 / Half 1": h_q1,
                        "Away Q1 / Half 1": a_q1,
                        "Home Q2 / Half 2": h_q2,
                        "Away Q2 / Half 2": a_q2,
                        "Home Q3": h_q3,
                        "Away Q3": a_q3,
                        "Home Q4": h_q4,
                        "Away Q4": a_q4,
                        "Home OT": h_ot,
                        "Away OT": a_ot,
                        "Venue": venue,
                        "City / State": "Australia",
                        "Attendance": att,
                        "Notable Players": f"{w_team} victory",
                        "A Succint one line game comment to summarise that game": recap,
                        "Primary Data Source": "National Basketball League (NBL) Official Archive / nblR database"
                    })

        # Sort games chronologically and re-index Game Number
        games.sort(key=lambda g: (g["Date"] or "9999", g["Start Time (Local)"] or "00:00"))
        for g_idx, g in enumerate(games, 1):
            g["Game Number"] = g_idx

        # Write to both target paths
        root_path = os.path.join(ROOT_OUTPUT_DIR, f"NBL_{year_str}.csv")
        archive_year_dir = os.path.join(ARCHIVE_OUTPUT_BASE, year_str)
        os.makedirs(archive_year_dir, exist_ok=True)
        archive_path = os.path.join(archive_year_dir, f"{year_str}_games.csv")

        for out_file in [root_path, archive_path]:
            with open(out_file, "w", encoding="utf-8", newline="") as f_out:
                writer = csv.DictWriter(f_out, fieldnames=CSV_HEADERS)
                writer.writeheader()
                writer.writerows(games)

        print(f"[{year_str}] Written {len(games)} games -> {root_path} and {archive_path}")

if __name__ == "__main__":
    build_all_seasons()
    print("All 51 seasons from 1975 to 2025 built successfully!")
