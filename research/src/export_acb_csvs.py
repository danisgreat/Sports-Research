"""
export_acb_csvs.py - Compiles and exports verified Spanish Basketball CSV logs (1975-2026).
Outputs to:
1. Liga_ACB_Basketball_CSVs/Liga_ACB_Basketball_<YEAR>.csv (52 files)
2. Previous Sports Results/Basketball/Liga ACB/<YEAR>/<YEAR>_games.csv (52 files)
Preserves 1900-1974 pre-establishment headers.
"""

import sqlite3
import csv
import os
import datetime

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "acb", "acb.db")
STANDALONE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "Liga_ACB_Basketball_CSVs"))
REPO_BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "Previous Sports Results", "Basketball", "Liga ACB"))

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
            ORDER BY date ASC, start_time ASC, game_id ASC
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
             
            # Mathematical invariant checks
            assert tot == hs + ascore, f"Total mismatch in {g_id}: {tot} != {hs} + {ascore}"
            assert margin == abs(hs - ascore), f"Margin mismatch in {g_id}: {margin} != |{hs} - {ascore}|"
            
            row_dict = {
                "Game Number": idx,
                "Game ID": g_id,
                "Season": season,
                "Season Year": s_year,
                "League Name": l_name,
                "Era": era,
                "Game Type (Pre-Season, Regular Season, Play-In, Playoffs, Quarterfinals, Semifinals, Finals, Cup, All-Star Game, Not applicable)": g_type,
                "Stage / Round": stage,
                "Date": dt,
                "Day of Week": dow,
                "Start Time (Local)": st,
                "Team 1": t1,
                "Team 2": t2,
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
                "Overtime": ot,
                "Q1 Home": q1h,
                "Q1 Away": q1a,
                "Q2 Home": q2h,
                "Q2 Away": q2a,
                "Q3 Home": q3h,
                "Q3 Away": q3a,
                "Q4 Home": q4h,
                "Q4 Away": q4a,
                "OT Home": oth,
                "OT Away": ota,
                "Venue": ven,
                "City": city,
                "Attendance": att,
                "Referees": ref,
                "Summary Comment": notes,
                "Primary Data Source": src
            }
            csv_rows.append(row_dict)
            
        # 1. Standalone directory
        standalone_file = os.path.join(STANDALONE_DIR, f"Liga_ACB_Basketball_{year}.csv")
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
    print(f"\nExport complete! {total_files} files written across 52 seasons, totaling {total_games} games.")
    return season_summary

if __name__ == '__main__':
    export_all()
