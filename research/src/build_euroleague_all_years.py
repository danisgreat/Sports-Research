#!/usr/bin/env python3
"""
Complete EuroLeague Basketball Dataset Generator (2000-2025)
Authoritative Source: EuroLeague Official API (api-live.euroleague.net / live.euroleague.net)

Fetches all games from the inaugural modern season (2000-01 / E2000) through 2025-26 (E2025).
Parses game details, phases (Regular Season, Top 16, Top 24, Play-In, Playoffs, Final Four),
quarter partial scores (Q1-Q4, OT), venue, attendance, referees, winning margins, and comments.

Populates:
Previous Sports Results/Basketball/EuroLeague/<YEAR>/<YEAR>_games.csv
"""

import os
import sys
import csv
import json
import time
import urllib.request
from datetime import datetime

HEADERS = [
    "Game Number",
    "Game ID",
    "Season",
    "Season Year",
    "Season Code",
    "Season Phase",
    "Game Type",
    "Round / Stage",
    "Date",
    "Day of Week",
    "Start Time (CET/CEST)",
    "UTC Date",
    "Team A",
    "Team B",
    "Home",
    "Away",
    "Home Team Code",
    "Away Team Code",
    "Venue",
    "City / Address",
    "Capacity",
    "Attendance",
    "Home Score",
    "Away Score",
    "Total Points",
    "Winning Margin",
    "Winning Team",
    "Losing Team",
    "Result",
    "Game Score",
    "Overtime",
    "Home Q1",
    "Away Q1",
    "Home Q2",
    "Away Q2",
    "Home Q3",
    "Away Q3",
    "Home Q4",
    "Away Q4",
    "Home OT",
    "Away OT",
    "Game Status",
    "Cancellation Reason",
    "Lead Referee",
    "Referee 2",
    "Referee 3",
    "Notable Players",
    "A Succint one line game comment to summarise that game",
    "Primary Data Source"
]

def fetch_season_games(season_code, retries=3):
    url = f"https://api-live.euroleague.net/v2/competitions/E/seasons/{season_code}/games"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
    for attempt in range(1, retries + 1):
        try:
            with urllib.request.urlopen(req, timeout=20) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                return data.get("data", [])
        except Exception as e:
            print(f"  Attempt {attempt} failed for {season_code}: {e}")
            if attempt < retries:
                time.sleep(2 * attempt)
            else:
                raise

def determine_game_type(phase_name, phase_code, group_name):
    gn_upper = (group_name or "").upper().strip()
    pn_upper = (phase_name or "").upper().strip()
    
    if "CHAMPIONSHIP" in gn_upper or gn_upper == "FINAL" or gn_upper.startswith("FINAL "):
        return "Championship Game"
    elif "THIRD" in gn_upper or "3RD" in gn_upper:
        return "Third Place Game"
    elif "SEMIFINAL" in gn_upper:
        return "Final Four Semifinal"
    elif "PLAYOFF" in gn_upper or "QUARTERFINAL" in gn_upper:
        return "Quarter-Finals / Playoffs"
    elif "EIGHTH" in gn_upper or "FIRST ROUND" in gn_upper and phase_code == "PO":
        return "Eighth-Finals / Playoffs"
    elif phase_code == "PI" or "PLAY-IN" in pn_upper:
        return "Play-In"
    elif phase_code == "TS" or "TOP 16" in pn_upper:
        return "Top 16"
    elif phase_code == "FF" or "FINAL FOUR" in pn_upper:
        return "Final Four"
    elif phase_code == "QR" or "QUALIFYING" in pn_upper:
        return "Qualifying Round"
    elif phase_code == "PO" or "PLAYOFF" in pn_upper:
        return "Quarter-Finals / Playoffs"
    elif phase_code == "RS" or "REGULAR" in pn_upper:
        return "Regular Season"
    return phase_name or "Regular Season"

def parse_game(g, idx):
    played = g.get("played", False)
    status = g.get("gameStatus", "")
    
    local = g.get("local") or {}
    road = g.get("road") or {}
    local_club = local.get("club") or {}
    road_club = road.get("club") or {}
    
    home_team = local_club.get("name") or local_club.get("abbreviatedName") or "Unknown"
    away_team = road_club.get("name") or road_club.get("abbreviatedName") or "Unknown"
    home_code = local_club.get("code") or ""
    away_code = road_club.get("code") or ""
    
    home_score = local.get("score") if played else ""
    away_score = road.get("score") if played else ""
    
    total_pts = (home_score + away_score) if (played and home_score != "" and away_score != "") else ""
    diff = abs(home_score - away_score) if (played and home_score != "" and away_score != "") else ""
    
    winner_club = g.get("winner") or {}
    winner_name = winner_club.get("name") or ""
    loser_name = ""
    result_str = ""
    game_score_str = ""
    
    if played and home_score != "" and away_score != "":
        if home_score > away_score:
            winner_name = home_team
            loser_name = away_team
            result_str = f"Home Win ({home_score}-{away_score})"
        elif away_score > home_score:
            winner_name = away_team
            loser_name = home_team
            result_str = f"Away Win ({away_score}-{home_score})"
        else:
            result_str = f"Tie ({home_score}-{away_score})"
        game_score_str = f"{home_score}-{away_score}"
    elif not played:
        if status.lower() == "cancelled":
            result_str = "Cancelled"
        else:
            result_str = "Scheduled / Unplayed"
        game_score_str = "N/A"
        
    # Partials / Quarters
    local_part = local.get("partials") or {}
    road_part = road.get("partials") or {}
    q1_h = local_part.get("partials1", "") if played else ""
    q1_a = road_part.get("partials1", "") if played else ""
    q2_h = local_part.get("partials2", "") if played else ""
    q2_a = road_part.get("partials2", "") if played else ""
    q3_h = local_part.get("partials3", "") if played else ""
    q3_a = road_part.get("partials3", "") if played else ""
    q4_h = local_part.get("partials4", "") if played else ""
    q4_a = road_part.get("partials4", "") if played else ""
    
    ot_h_dict = local_part.get("extraPeriods") or {}
    ot_a_dict = road_part.get("extraPeriods") or {}
    ot_count = max(len(ot_h_dict), len(ot_a_dict))
    ot_str = f"Yes ({ot_count} OT)" if ot_count > 0 else "No"
    ot_h = sum(ot_h_dict.values()) if ot_h_dict else (0 if ot_count > 0 else "")
    ot_a = sum(ot_a_dict.values()) if ot_a_dict else (0 if ot_count > 0 else "")
    
    venue = g.get("venue") or {}
    venue_name = venue.get("name") or ""
    venue_address = venue.get("address") or ""
    capacity = venue.get("capacity") or ""
    attendance = g.get("audience") if (g.get("audienceConfirmed") or g.get("audience")) else ""
    
    dt_raw = g.get("date") or g.get("localDate") or ""
    date_str, time_str, dow_str = "", "", ""
    if dt_raw:
        try:
            clean_dt = dt_raw.replace("Z", "")
            if "." in clean_dt:
                clean_dt = clean_dt.split(".")[0]
            dt_obj = datetime.fromisoformat(clean_dt)
            date_str = dt_obj.strftime("%Y-%m-%d")
            time_str = dt_obj.strftime("%H:%M")
            dow_str = dt_obj.strftime("%A")
        except Exception:
            date_str = dt_raw[:10]
            
    phase_data = g.get("phaseType") or {}
    phase_code = phase_data.get("code") or ""
    phase_name = phase_data.get("name") or phase_data.get("alias") or "Regular Season"
    group_data = g.get("group") or {}
    group_name = group_data.get("rawName") or group_data.get("name") or ""
    
    game_type = determine_game_type(phase_name, phase_code, group_name)
    round_str = g.get("roundAlias") or g.get("roundName") or f"Round {g.get('round', '')}"
    
    season_data = g.get("season") or {}
    season_alias = season_data.get("alias") or f"{season_data.get('year')}"
    season_year = season_data.get("year")
    season_code = season_data.get("code")
    game_id = g.get("identifier") or f"{season_code}_{g.get('gameCode')}"
    
    ref1 = (g.get("referee1") or {}).get("name") or ""
    ref2 = (g.get("referee2") or {}).get("name") or ""
    ref3 = (g.get("referee3") or {}).get("name") or ""
    
    # Reason for cancellations if applicable
    cancellation_reason = ""
    if not played:
        if str(season_year) == "2019":
            cancellation_reason = "Cancelled due to COVID-19 pandemic shutdown"
        elif str(season_year) == "2021" and any(r in (home_team + away_team).upper() for r in ["ZENIT", "CSKA", "UNICS"]):
            cancellation_reason = "Cancelled due to suspension and annulment of Russian clubs"
        elif status.lower() == "cancelled":
            cancellation_reason = "Cancelled fixture"
            
    comment = ""
    if played:
        if game_type == "Championship Game":
            comment = f"{winner_name} crowned EuroLeague Champions after defeating {loser_name} {game_score_str} at {venue_name or 'the championship arena'}."
        elif "Final Four" in game_type:
            comment = f"{winner_name} defeated {loser_name} {game_score_str} in Final Four ({game_type}) at {venue_name}."
        elif "Playoff" in game_type:
            comment = f"{winner_name} beat {loser_name} {game_score_str} in {round_str} ({group_name or 'Playoffs'})."
        else:
            comment = f"{winner_name} defeated {loser_name} {game_score_str} in {round_str} ({game_type})."
    else:
        comment = f"Match between {away_team} and {home_team} in {round_str} was {status.lower() or 'not played'}."
        
    return [
        idx,
        game_id,
        season_alias,
        season_year,
        season_code,
        phase_name,
        game_type,
        round_str,
        date_str,
        dow_str,
        time_str,
        g.get("utcDate") or "",
        away_team,      # Team A (matches old header)
        home_team,      # Team B (matches old header)
        home_team,      # Home
        away_team,      # Away
        home_code,
        away_code,
        venue_name,
        venue_address,
        capacity,
        attendance,
        home_score,
        away_score,
        total_pts,
        diff,
        winner_name,
        loser_name,
        result_str,
        game_score_str,
        ot_str,
        q1_h,
        q1_a,
        q2_h,
        q2_a,
        q3_h,
        q3_a,
        q4_h,
        q4_a,
        ot_h,
        ot_a,
        "Played" if played else (status.capitalize() if status else "Unplayed"),
        cancellation_reason,
        ref1,
        ref2,
        ref3,
        f"{winner_name} team victory",
        comment,
        "Euroleague Basketball Official API (api-live.euroleague.net / live.euroleague.net)"
    ]

def process_all_seasons():
    base_dir = os.path.abspath("Previous Sports Results/Basketball/EuroLeague")
    
    
    total_games_all = 0
    total_seasons = 0
    
    print("=" * 70)
    print("Starting EuroLeague Historical Dataset Build (2000 to 2025)")
    print("=" * 70)
    
    for year in range(2000, 2026):
        season_code = f"E{year}"
        print(f"\nProcessing {season_code} (Season {year}-{str(year+1)[-2:]})...")
        
        try:
            games_raw = fetch_season_games(season_code)
        except Exception as e:
            print(f"Error fetching {season_code}: {e}")
            continue
            
        # Deduplicate games by identifier / gameCode if any duplicates exist
        seen_ids = set()
        deduped_games = []
        for g in games_raw:
            gid = g.get("identifier") or g.get("gameCode")
            if gid not in seen_ids:
                seen_ids.add(gid)
                deduped_games.append(g)
                
        # Sort chronologically by date and gameCode
        deduped_games.sort(key=lambda x: (x.get("date") or "", x.get("gameCode") or 0))
        
        rows = []
        for idx, g in enumerate(deduped_games, 1):
            rows.append(parse_game(g, idx))
            
        # Write to paths
        year_folder = os.path.join(base_dir, str(year))
        os.makedirs(year_folder, exist_ok=True)
        
        target_path_previous = os.path.join(year_folder, f"{year}_games.csv")
        
        for p in [target_path_previous]:
            with open(p, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(HEADERS)
                writer.writerows(rows)
                
        played_count = sum(1 for r in rows if r[41] == "Played")
        print(f"  -> Generated {len(rows)} games ({played_count} played) written to:")
        print(f"     1. {target_path_previous}")
        
        total_games_all += len(rows)
        total_seasons += 1
        time.sleep(0.2)
        
    print("\n" + "=" * 70)
    print(f"COMPLETED: {total_seasons} seasons processed, {total_games_all} total games written across all target CSVs.")
    print("=" * 70)

if __name__ == "__main__":
    process_all_seasons()
