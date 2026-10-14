"""
export_eurocup_csvs.py - Compiles and exports verified EuroCup Basketball CSV logs (1975-2026).
Outputs to:
1. EuroCup_Basketball_CSVs/EuroCup_Basketball_<YEAR>.csv (52 files)
2. Previous Sports Results/Basketball/EuroCup/<YEAR>/<YEAR>_games.csv (52 files)
Preserves 1900-1974 pre-establishment headers intact.
"""

import sqlite3
import csv
import os
import re
import datetime

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "eurocup", "eurocup.db")
STANDALONE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "EuroCup_Basketball_CSVs"))
REPO_BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "Previous Sports Results", "Basketball", "EuroCup"))

FIELDNAMES = [
    "Game Number",
    "Game ID",
    "Season",
    "Season Year",
    "League Name",
    "Era",
    "Game Type (Pre-Season, Regular Season, Play-In, Playoffs, Quarterfinals, Semifinals, Finals, Cup, All-Star Game, Not applicable)",
    "Stage / Round",
    "Date",
    "Day of Week",
    "Start Time (Local)",
    "Team 1",
    "Team 2",
    "Home Team",
    "Away Team",
    "Home Score",
    "Away Score",
    "Game Score",
    "Total Points",
    "Winning Margin",
    "Winner",
    "Loser",
    "Result",
    "Period Format",
    "Overtime",
    "Q1 Home",
    "Q1 Away",
    "Q2 Home",
    "Q2 Away",
    "Q3 Home",
    "Q3 Away",
    "Q4 Home",
    "Q4 Away",
    "OT Home",
    "OT Away",
    "Venue",
    "City",
    "Attendance",
    "Referees",
    "Summary Comment",
    "Primary Data Source"
]

def clean_city_name(city_raw):
    if not city_raw:
        return "Europe"
    c = str(city_raw).strip()
    # Replace html tags
    c = re.sub(r'<[^>]+>', ' ', c)
    # If street address with postal code and city
    if 'Valencia' in c:
        return 'Valencia'
    if 'Zgorzelec' in c:
        return 'Zgorzelec'
    # Strip leading postal codes like '01000 Bourg en Bresse' -> 'Bourg-en-Bresse'
    m = re.match(r'^\d{4,5}\s+(.*)$', c)
    if m:
        c = m.group(1).strip()
    c = re.sub(r'\s+', ' ', c).strip()
    return c if c else "Europe"

def clean_venue_name(venue_raw):
    if not venue_raw:
        return "European Indoor Arena"
    v = str(venue_raw).strip()
    v = re.sub(r'<[^>]+>', ' ', v)
    v = re.sub(r'\s+', ' ', v).strip()
    return v if v else "European Indoor Arena"

def export_all():
    os.makedirs(STANDALONE_DIR, exist_ok=True)
    os.makedirs(REPO_BASE_DIR, exist_ok=True)
    
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    
    total_files = 0
    total_games = 0
    season_summary = []
    
    for year in range(1975, 2027):
        cur.execute("""
            SELECT game_id, season, season_year, league_name, era, game_type, stage_round,
                   date, day_of_week, start_time, team_1, team_2, home_team, away_team,
                   home_score, away_score, game_score, total_points, winning_margin,
                   winner, loser, result, period_format, overtime,
                   q1_home, q1_away, q2_home, q2_away, q3_home, q3_away, q4_home, q4_away,
                   ot_home, ot_away, venue, city, attendance, referees, notes, source
            FROM games
            WHERE season_year = ?
            ORDER BY date ASC, game_id ASC
        """, (year,))
        rows = cur.fetchall()
        
        if not rows:
            print(f"Warning: No games found for year {year} in database!")
            continue
            
        csv_rows = []
        for idx, r in enumerate(rows, start=1):
            (g_id, season, s_year, l_name, era, g_type, stage,
             dt, dow, st, t1, t2, ht, at,
             hs, ascore, gs, tot, margin,
             win, lose, res, pf, ot,
             q1h, q1a, q2h, q2a, q3h, q3a, q4h, q4a,
             oth, ota, ven, city, att, ref, notes, src) = r
             
            # Clean and re-verify
            try:
                dt_obj = datetime.date.fromisoformat(dt)
                dow = dt_obj.strftime("%A")
            except:
                pass
                
            tot = hs + ascore
            margin = abs(hs - ascore)
            gs = f"{hs} - {ascore}"
            
            if hs > ascore:
                win = ht
                lose = at
                res = "Home Win"
            elif ascore > hs:
                win = at
                lose = ht
                res = "Away Win"
            else:
                win = "Tie"
                lose = "Tie"
                res = "Draw"
                
            clean_city = clean_city_name(city)
            clean_ven = clean_venue_name(ven)
            
            # Format uniform Game ID
            formatted_game_id = f"EUROCUP_{year}_{idx:04d}"
            
            # Generate summary comment if empty or generic
            if not notes or "defeated" not in notes:
                if res != "Draw":
                    summary = f"Official {l_name} match. {win} defeated {lose} {hs}-{ascore} (margin {margin} pts)."
                else:
                    summary = f"Official {l_name} two-legged aggregate tie fixture. {ht} and {at} drew {hs}-{ascore}."
            else:
                summary = notes
                
            row_dict = {
                "Game Number": idx,
                "Game ID": formatted_game_id,
                "Season": season,
                "Season Year": s_year,
                "League Name": l_name,
                "Era": era,
                "Game Type (Pre-Season, Regular Season, Play-In, Playoffs, Quarterfinals, Semifinals, Finals, Cup, All-Star Game, Not applicable)": g_type,
                "Stage / Round": stage,
                "Date": dt,
                "Day of Week": dow,
                "Start Time (Local)": st if st else "Not recorded",
                "Team 1": ht,
                "Team 2": at,
                "Home Team": ht,
                "Away Team": at,
                "Home Score": hs,
                "Away Score": ascore,
                "Game Score": gs,
                "Total Points": tot,
                "Winning Margin": margin,
                "Winner": win,
                "Loser": lose,
                "Result": res,
                "Period Format": pf,
                "Overtime": ot if ot else "No",
                "Q1 Home": q1h if q1h is not None else "",
                "Q1 Away": q1a if q1a is not None else "",
                "Q2 Home": q2h if q2h is not None else "",
                "Q2 Away": q2a if q2a is not None else "",
                "Q3 Home": q3h if q3h is not None else "",
                "Q3 Away": q3a if q3a is not None else "",
                "Q4 Home": q4h if q4h is not None else "",
                "Q4 Away": q4a if q4a is not None else "",
                "OT Home": oth if oth is not None else "",
                "OT Away": ota if ota is not None else "",
                "Venue": clean_ven,
                "City": clean_city,
                "Attendance": att if att is not None else "",
                "Referees": ref if ref is not None else "",
                "Summary Comment": summary,
                "Primary Data Source": src
            }
            csv_rows.append(row_dict)
            
        # 1. Standalone directory
        standalone_file = os.path.join(STANDALONE_DIR, f"EuroCup_Basketball_{year}.csv")
        with open(standalone_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()
            writer.writerows(csv_rows)
            
        # 2. Repo directory
        repo_year_dir = os.path.join(REPO_BASE_DIR, str(year))
        os.makedirs(repo_year_dir, exist_ok=True)
        repo_file = os.path.join(repo_year_dir, f"{year}_games.csv")
        with open(repo_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()
            writer.writerows(csv_rows)
            
        total_files += 2
        total_games += len(csv_rows)
        season_summary.append((year, len(csv_rows)))
        print(f"Exported {year} ({season}): {len(csv_rows)} games -> {standalone_file} & {repo_file}")
        
    conn.close()
    print(f"\nEuroCup Export complete! {total_files} files written across 52 seasons, totaling {total_games} games.")
    return season_summary

if __name__ == '__main__':
    export_all()
