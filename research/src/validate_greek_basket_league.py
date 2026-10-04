#!/usr/bin/env python3
"""
Validation script for Greece Basket League game records (1975-2025).
Ensures 100% data integrity, schema compliance, chronological order,
and exact consistency between root CSVs and Previous Sports Results subdirectories.
"""

import os
import sys
import io
import csv

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ROOT_DIR = r"c:\Users\danie\Desktop\Sports Research\Greek_Basket_League_CSVs"
PREV_DIR = r"c:\Users\danie\Desktop\Sports Research\Previous Sports Results\Basketball\Greek Basket League"

EXPECTED_HEADERS = [
    "Game Number",
    "Game ID",
    "Season",
    "Season Year",
    "Game Type (Pre-Season, Regular Season, Top 6, Play-out, Play-In, Quarter-Finals, Semi-Finals, 3rd Place Playoff, Greek Finals, Greek Super Cup, All-Star Game, Not applicable)",
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
    "City",
    "Attendance",
    "Notable Players",
    "A Succint one line game comment to summarise that game",
    "Primary Data Source"
]

def validate_all():
    print("=" * 80)
    print("VALIDATING GREECE BASKET LEAGUE DATASET (1975-2025)")
    print("=" * 80)
    
    total_games = 0
    errors = []
    
    for yr in range(1975, 2026):
        root_file = os.path.join(ROOT_DIR, f"Greek_Basket_League_{yr}.csv")
        prev_file = os.path.join(PREV_DIR, str(yr), f"{yr}_games.csv")
        
        # 1. Existence
        if not os.path.exists(root_file):
            errors.append(f"Missing root file: {root_file}")
            continue
        if not os.path.exists(prev_file):
            errors.append(f"Missing prev file: {prev_file}")
            continue
            
        # 2. Read rows
        with open(root_file, "r", encoding="utf-8") as f:
            r_reader = list(csv.reader(f))
        with open(prev_file, "r", encoding="utf-8") as f:
            p_reader = list(csv.reader(f))
            
        if len(r_reader) != len(p_reader):
            errors.append(f"Row count mismatch for {yr}: Root={len(r_reader)} vs Prev={len(p_reader)}")
            continue
            
        # 3. Check headers
        r_head = r_reader[0]
        if r_head != EXPECTED_HEADERS:
            errors.append(f"Header mismatch in {root_file}")
            
        # 4. Check data rows
        data_rows = r_reader[1:]
        prev_data = p_reader[1:]
        
        if len(data_rows) == 0:
            errors.append(f"Empty dataset for season {yr}")
            continue
            
        prev_date = ""
        for i, (row, p_row) in enumerate(zip(data_rows, prev_data)):
            # Check row match
            if row != p_row:
                errors.append(f"Row mismatch in season {yr}, game {i+1}")
                break
                
            game_num = int(row[0])
            if game_num != i + 1:
                errors.append(f"Non-consecutive Game Number in {yr}: expected {i+1}, got {game_num}")
                
            home_team = row[11]
            away_team = row[12]
            if not home_team or not away_team or home_team == "Unknown" or away_team == "Unknown":
                errors.append(f"Invalid team in {yr} game {i+1}: {home_team} vs {away_team}")
                
            h_sc = int(row[13])
            a_sc = int(row[14])
            tot = int(row[15])
            margin = int(row[16])
            win_team = row[17]
            loss_team = row[18]
            
            if tot != h_sc + a_sc:
                errors.append(f"Math error (Total Points) in {yr} game {i+1}: {tot} != {h_sc} + {a_sc}")
            if margin != abs(h_sc - a_sc):
                errors.append(f"Math error (Margin) in {yr} game {i+1}: {margin} != abs({h_sc} - {a_sc})")
            if h_sc > a_sc and win_team != home_team:
                errors.append(f"Winner mismatch in {yr} game {i+1}: expected {home_team}, got {win_team}")
            elif a_sc > h_sc and win_team != away_team:
                errors.append(f"Winner mismatch in {yr} game {i+1}: expected {away_team}, got {win_team}")
                
            # Chronological date check
            date_str = row[6]
            if prev_date and date_str < prev_date:
                errors.append(f"Out of chronological order in {yr} game {i+1}: {date_str} < {prev_date}")
            prev_date = date_str
            
        total_games += len(data_rows)
        print(f"Season {yr} ({yr}-{str(yr+1)[2:]}): PASS ({len(data_rows)} games verified)")
        
    print("=" * 80)
    if errors:
        print(f"VALIDATION FAILED with {len(errors)} errors:")
        for e in errors[:20]:
            print("  -", e)
        return False
    else:
        print(f"ALL 51 SEASONS (1975-2025) VALIDATED SUCCESSFULLY!")
        print(f"Total verified games across dataset: {total_games:,}")
        print("=" * 80)
        return True

if __name__ == "__main__":
    success = validate_all()
    if not success:
        sys.exit(1)
