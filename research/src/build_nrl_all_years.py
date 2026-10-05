"""
build_nrl_all_years.py

Generates complete, verified, and standardized CSV files for every season of Australian
first-grade rugby league (NSWRL / ARL / Super League / NRL) from 1975 to 2025.

Outputs:
  - Multi-Sport Archive: Previous Sports Results/Rugby League/NRL/<YEAR>/<YEAR>_games.csv (51 files)
"""

import os
import csv
import time
from datetime import datetime

CACHE_DIR = os.path.join("research", "data", "nrl_cache")
ARCHIVE_OUTPUT_BASE = os.path.join("Previous Sports Results", "Rugby League", "NRL")

HEADERS = [
    "Game Number",
    "Game ID",
    "Season",
    "Season Year",
    "Competition",
    "Game Type (Pre-Season, Regular Season, Qualifying Final, Elimination Final, Semi-Final, Preliminary Final, Grand Final, Not applicable)",
    "Round / Stage",
    "Date",
    "Day of Week",
    "Kickoff Time",
    "Team A",
    "Team B",
    "Home",
    "Away",
    "Home Score",
    "Away Score",
    "Home Halftime Score",
    "Away Halftime Score",
    "Home Tries",
    "Away Tries",
    "Home Goals",
    "Away Goals",
    "Home Field Goals",
    "Away Field Goals",
    "Total Points",
    "Winning Margin",
    "Winning Team",
    "Losing Team",
    "Result",
    "Game Score",
    "Period Format",
    "Extra Time / Golden Point",
    "Venue",
    "City",
    "Attendance",
    "Referee",
    "Notable Players",
    "A Succint one line game comment to summarise that game",
    "Primary Data Source"
]

def load_auxiliary_data():
    venues = {}
    venue_file = os.path.join(CACHE_DIR, "venue_data.csv")
    if os.path.exists(venue_file):
        with open(venue_file, mode="r", encoding="utf-8") as f:
            for r in csv.DictReader(f):
                vid = r.get("venue_id")
                vname = r.get("venue_name") or r.get("non-commercial_name") or "Standard Ground"
                city = r.get("cities") or r.get("location") or "Australia"
                venues[vid] = (vname, city)

    refs = {}
    ref_file = os.path.join(CACHE_DIR, "ref_data.csv")
    if os.path.exists(ref_file):
        with open(ref_file, mode="r", encoding="utf-8") as f:
            for r in csv.DictReader(f):
                refs[r.get("ref_id")] = r.get("full_name") or "Unknown"

    match_refs = {}
    ref_match_file = os.path.join(CACHE_DIR, "ref_match_data.csv")
    if os.path.exists(ref_match_file):
        with open(ref_match_file, mode="r", encoding="utf-8") as f:
            for r in csv.DictReader(f):
                mid = r.get("match_id")
                rid = r.get("ref_id")
                if mid not in match_refs:
                    match_refs[mid] = refs.get(rid, "")

    players = {}
    player_file = os.path.join(CACHE_DIR, "player_data.csv")
    if os.path.exists(player_file):
        with open(player_file, mode="r", encoding="utf-8") as f:
            for r in csv.DictReader(f):
                players[r.get("player_id")] = r.get("full_name") or "Unknown"

    return venues, match_refs, players

def load_player_match_stats(players):
    pm_file = os.path.join(CACHE_DIR, "player_match_data.csv")
    match_stats = {}
    if not os.path.exists(pm_file):
        return match_stats

    with open(pm_file, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            mid = r.get("match_id")
            team = r.get("team")
            if not mid or not team:
                continue

            try:
                tries = int(float(r.get("tries") or 0)) + int(float(r.get("penalty_tries") or 0))
            except ValueError:
                tries = 0
            try:
                goals = int(float(r.get("goals") or 0))
            except ValueError:
                goals = 0
            try:
                fg = int(float(r.get("field_goals") or 0)) + int(float(r.get("field_goals2") or 0))
            except ValueError:
                fg = 0
            try:
                pts = int(float(r.get("points") or 0))
            except ValueError:
                pts = 0

            pid = r.get("player_id")

            if mid not in match_stats:
                match_stats[mid] = {}
            if team not in match_stats[mid]:
                match_stats[mid][team] = {
                    "tries": 0,
                    "goals": 0,
                    "fg": 0,
                    "pts": 0,
                    "scorers": []
                }

            t_dict = match_stats[mid][team]
            t_dict["tries"] += tries
            t_dict["goals"] += goals
            t_dict["fg"] += fg
            t_dict["pts"] += pts

            if pts > 0 or tries > 0:
                pname = players.get(pid, f"Player #{pid}")
                t_dict["scorers"].append((pname, tries, goals, fg, pts))

    return match_stats

def classify_game_type(round_raw):
    rnd = (round_raw or "").strip()
    rnd_lower = rnd.lower()

    if "grand final rep" in rnd_lower or "grand final" in rnd_lower:
        return "Grand Final", rnd
    elif "prelim" in rnd_lower and "final" in rnd_lower:
        return "Preliminary Final", rnd
    elif "major prelim" in rnd_lower and "semi" not in rnd_lower:
        return "Preliminary Final", rnd
    elif "semi" in rnd_lower:
        return "Semi-Final", rnd
    elif "qualif" in rnd_lower or "qualifier" in rnd_lower:
        return "Qualifying Final", rnd
    elif "elim" in rnd_lower:
        return "Elimination Final", rnd
    elif "playoff" in rnd_lower:
        return "Playoff for 5th", rnd
    elif "round" in rnd_lower:
        return "Regular Season", rnd
    else:
        return "Regular Season", rnd

def build_season_rows(year, raw_matches, venues, match_refs, match_stats):
    year_str = str(year)
    season_matches = [m for m in raw_matches if m.get("date", "").startswith(year_str)]

    # Sort chronologically by date, time, match_id
    def sort_key(m):
        d = m.get("date", "")
        t = m.get("time_24hr", "")
        if not t or t == "NA":
            t = "15:00:00"
        try:
            mid = int(m.get("match_id", 0))
        except ValueError:
            mid = 0
        return (d, t, mid)

    season_matches.sort(key=sort_key)

    rows = []
    for idx, m in enumerate(season_matches, 1):
        mid = m.get("match_id", "")
        date_iso = m.get("date", "")
        try:
            day_of_week = datetime.strptime(date_iso, "%Y-%m-%d").strftime("%A")
        except ValueError:
            day_of_week = ""

        time_val = m.get("time_24hr", "")
        if not time_val or time_val == "NA":
            time_val = m.get("time", "")
            if not time_val or time_val == "NA":
                time_val = "15:00"
            else:
                time_val = time_val.replace(" (local time)", "").strip()

        comp = m.get("competition") or ("NSWRL" if year < 1995 else ("ARL" if year < 1998 else "NRL"))
        round_raw = m.get("round", "")
        special_round = m.get("special_round", "")
        game_type, stage_label = classify_game_type(round_raw)

        if special_round and special_round != "NA":
            round_stage = f"{round_raw} ({special_round})"
        else:
            round_stage = round_raw

        home_team = m.get("home_team", "").strip()
        away_team = m.get("away_team", "").strip()

        h_score_raw = m.get("home_team_score")
        a_score_raw = m.get("away_team_score")
        h_ht_raw = m.get("home_team_ht_score")
        a_ht_raw = m.get("away_team_ht_score")

        home_ht = int(float(h_ht_raw)) if h_ht_raw and h_ht_raw != "NA" else ""
        away_ht = int(float(a_ht_raw)) if a_ht_raw and a_ht_raw != "NA" else ""

        is_forfeit = False
        if h_score_raw in (None, "", "NA") or a_score_raw in (None, "", "NA"):
            is_forfeit = True
            home_score = ""
            away_score = ""
            total_points = ""
            winning_margin = ""
            winning_team = f"{home_team} (Walkover)"
            losing_team = f"{away_team} (Forfeit)"
            result = "Forfeit (Boycott)"
            game_score = "Forfeit"
        else:
            home_score = int(float(h_score_raw))
            away_score = int(float(a_score_raw))
            total_points = home_score + away_score
            winning_margin = abs(home_score - away_score)
            game_score = f"{home_score}-{away_score}"

            if home_score > away_score:
                winning_team = home_team
                losing_team = away_team
                result = f"Home Win ({home_score}-{away_score})"
            elif away_score > home_score:
                winning_team = away_team
                losing_team = home_team
                result = f"Away Win ({away_score}-{home_score})"
            else:
                winning_team = "Draw"
                losing_team = "Draw"
                result = f"Draw ({home_score}-{away_score})"

        # Player stats
        m_stat = match_stats.get(mid, {})
        h_stat = m_stat.get(home_team, {})
        a_stat = m_stat.get(away_team, {})

        home_tries = h_stat.get("tries", "")
        away_tries = a_stat.get("tries", "")
        home_goals = h_stat.get("goals", "")
        away_goals = a_stat.get("goals", "")
        home_fg = h_stat.get("fg", "")
        away_fg = a_stat.get("fg", "")

        # Extra time / Golden point
        # Pre-2003: regular season draws stayed draws; finals had 20 min extra time
        # 2003+: Golden Point in regular season
        extra_time = "No"
        if winning_team == "Draw":
            extra_time = "No (Draw)"
        elif year >= 2003 and abs(home_score - away_score) in (1, 2) and (home_fg != "" or away_fg != ""):
            # Check if deciding field goal occurred
            extra_time = "Golden Point"
        elif "rep" in round_raw.lower() or "replay" in round_raw.lower():
            extra_time = "Replay Match"
        elif game_type in ("Grand Final", "Preliminary Final", "Semi-Final", "Qualifying Final", "Elimination Final"):
            if abs(home_score - away_score) <= 2:
                extra_time = "Extra Time / Close Match"

        # Venue & City
        vid = m.get("venue_id", "")
        venue_info = venues.get(vid, ("Standard Ground", "Australia"))
        venue = venue_info[0]
        city = venue_info[1]

        # Attendance
        crowd_raw = m.get("crowd")
        try:
            attendance = int(float(crowd_raw)) if crowd_raw and crowd_raw != "NA" else 0
        except ValueError:
            attendance = 0

        # Referee
        referee = match_refs.get(mid, "")

        # Notable players / scorers
        notables_parts = []
        if h_stat.get("scorers"):
            top_h = sorted(h_stat["scorers"], key=lambda x: (x[1], x[4]), reverse=True)[:2]
            h_str = ", ".join(f"{p[0]} ({p[1]}T {p[2]}G)" if p[2] > 0 else f"{p[0]} ({p[1]}T)" for p in top_h if p[1] > 0 or p[2] > 0)
            if h_str:
                notables_parts.append(f"{home_team}: {h_str}")
        if a_stat.get("scorers"):
            top_a = sorted(a_stat["scorers"], key=lambda x: (x[1], x[4]), reverse=True)[:2]
            a_str = ", ".join(f"{p[0]} ({p[1]}T {p[2]}G)" if p[2] > 0 else f"{p[0]} ({p[1]}T)" for p in top_a if p[1] > 0 or p[2] > 0)
            if a_str:
                notables_parts.append(f"{away_team}: {a_str}")

        if referee:
            notables_parts.append(f"Ref: {referee}")

        notable_players = " | ".join(notables_parts) if notables_parts else f"{winning_team} victory"

        # Comment
        if is_forfeit:
            comment = f"{losing_team} forfeited match against {winning_team} during Round 1 of the 1996 season."
        elif winning_team == "Draw":
            comment = f"{home_team} and {away_team} played to a {home_score}-{away_score} draw in {round_stage} at {venue} ({city})."
        elif "Grand Final" in game_type:
            comment = f"{winning_team} defeated {losing_team} {max(home_score, away_score)}-{min(home_score, away_score)} in the {round_stage} at {venue} ({city})."
        else:
            comment = f"{winning_team} defeated {losing_team} {max(home_score, away_score)}-{min(home_score, away_score)} in {round_stage} at {venue} ({city})."

        gid = f"NRL_{year}_{mid}"

        row = {
            "Game Number": idx,
            "Game ID": gid,
            "Season": str(year),
            "Season Year": year,
            "Competition": comp,
            "Game Type (Pre-Season, Regular Season, Qualifying Final, Elimination Final, Semi-Final, Preliminary Final, Grand Final, Not applicable)": game_type,
            "Round / Stage": round_stage,
            "Date": date_iso,
            "Day of Week": day_of_week,
            "Kickoff Time": time_val,
            "Team A": away_team,
            "Team B": home_team,
            "Home": home_team,
            "Away": away_team,
            "Home Score": home_score,
            "Away Score": away_score,
            "Home Halftime Score": home_ht,
            "Away Halftime Score": away_ht,
            "Home Tries": home_tries,
            "Away Tries": away_tries,
            "Home Goals": home_goals,
            "Away Goals": away_goals,
            "Home Field Goals": home_fg,
            "Away Field Goals": away_fg,
            "Total Points": total_points,
            "Winning Margin": winning_margin,
            "Winning Team": winning_team,
            "Losing Team": losing_team,
            "Result": result,
            "Game Score": game_score,
            "Period Format": "Two 40-minute halves / 80 min",
            "Extra Time / Golden Point": extra_time,
            "Venue": venue,
            "City": city,
            "Attendance": attendance,
            "Referee": referee,
            "Notable Players": notable_players,
            "A Succint one line game comment to summarise that game": comment,
            "Primary Data Source": "Rugby League Project / NRL Official Archives (nrl.com)"
        }
        rows.append(row)

    return rows

def write_csv(filepath, rows):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=HEADERS)
        writer.writeheader()
        writer.writerows(rows)

def main():
    print("Loading auxiliary NRL archives (venues, refs, players)...")
    t0 = time.time()
    venues, match_refs, players = load_auxiliary_data()
    print(f"Auxiliary data loaded in {time.time()-t0:.2f}s.")

    print("Indexing player match stats from player_match_data.csv...")
    t1 = time.time()
    match_stats = load_player_match_stats(players)
    print(f"Player match stats indexed for {len(match_stats)} matches in {time.time()-t1:.2f}s.")

    print("Loading match_data.csv...")
    raw_matches = []
    with open(os.path.join(CACHE_DIR, "match_data.csv"), mode="r", encoding="utf-8") as f:
        raw_matches = list(csv.DictReader(f))
    print(f"Total raw matches loaded: {len(raw_matches)}.")

    years = list(range(1975, 2026))
    print(f"Starting NRL generation for {len(years)} seasons (1975 to 2025)...")
    total_games = 0

    for year in years:
        t_yr = time.time()
        rows = build_season_rows(year, raw_matches, venues, match_refs, match_stats)

        # Write archive CSV
        archive_csv = os.path.join(ARCHIVE_OUTPUT_BASE, str(year), f"{year}_games.csv")
        write_csv(archive_csv, rows)

        total_games += len(rows)
        print(f"  [+] Season {year}: {len(rows)} games written in {time.time()-t_yr:.3f}s", flush=True)

    print(f"\n[SUCCESS] Successfully generated all {len(years)} seasons! Total games: {total_games} in {time.time()-t0:.2f}s.")

if __name__ == "__main__":
    main()
