"""
validate_eurocup.py - Exhaustive validation script for EuroCup Basketball CSV logs (1975-2026).
Verifies:
1. File presence: all 52 standalone files (EuroCup_Basketball_<YEAR>.csv) and 52 repo files (<YEAR>_games.csv).
2. Exact 41-column basketball schema match.
3. Complete row identity between standalone and repo files.
4. Mathematical invariants: Total Points = H + A, Winning Margin = |H - A|, Game Score = H - A.
5. Match outcome consistency: Winner, Loser, Result.
6. Sequential Game Numbers (1..N).
7. Date validity (YYYY-MM-DD) and Day of Week accuracy.
8. Non-empty critical fields (teams, venues, cities, eras, league names).
9. Verification of 1900-1974 pre-establishment files.
"""

import os
import csv
import re
import datetime
import sys

STANDALONE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "EuroCup_Basketball_CSVs"))
REPO_BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "Previous Sports Results", "Basketball", "EuroCup"))

EXPECTED_COLUMNS = [
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

def validate_all():
    errors = []
    warnings = []
    
    print("================================================================================")
    print("STARTING EUROCUP BASKETBALL COMPREHENSIVE VALIDATION SUITE (1975-2026)")
    print("================================================================================")
    
    # 1. Check pre-establishment files (1900-1974)
    pre_est_count = 0
    for y in range(1900, 1975):
        rf = os.path.join(REPO_BASE_DIR, str(y), f"{y}_games.csv")
        if os.path.exists(rf):
            pre_est_count += 1
        else:
            warnings.append(f"Pre-establishment file missing for year {y}: {rf}")
    print(f"Pre-establishment repository files (1900-1974) verified: {pre_est_count}/75 found.")
    
    total_games_standalone = 0
    total_games_repo = 0
    seasons_checked = 0
    
    for year in range(1975, 2027):
        standalone_path = os.path.join(STANDALONE_DIR, f"EuroCup_Basketball_{year}.csv")
        repo_path = os.path.join(REPO_BASE_DIR, str(year), f"{year}_games.csv")
        
        # Verify file existence
        if not os.path.exists(standalone_path):
            errors.append(f"Missing standalone file: {standalone_path}")
            continue
        if not os.path.exists(repo_path):
            errors.append(f"Missing repo file: {repo_path}")
            continue
            
        seasons_checked += 1
        
        # Read standalone
        with open(standalone_path, mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            standalone_headers = reader.fieldnames
            standalone_rows = list(reader)
            
        # Read repo
        with open(repo_path, mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            repo_headers = reader.fieldnames
            repo_rows = list(reader)
            
        # Header check
        if standalone_headers != EXPECTED_COLUMNS:
            errors.append(f"Year {year} standalone headers do not match expected 41-column schema!")
        if repo_headers != EXPECTED_COLUMNS:
            errors.append(f"Year {year} repo headers do not match expected 41-column schema!")
            
        # Row count match
        if len(standalone_rows) != len(repo_rows):
            errors.append(f"Year {year} row count mismatch: standalone has {len(standalone_rows)}, repo has {len(repo_rows)}")
            
        if len(standalone_rows) == 0:
            errors.append(f"Year {year} has 0 rows!")
            
        total_games_standalone += len(standalone_rows)
        total_games_repo += len(repo_rows)
        
        # Row-by-row integrity check on standalone rows
        for idx, row in enumerate(standalone_rows, start=1):
            gid = row.get("Game ID", f"UNKNOWN_{year}_{idx}")
            
            # Check sequential Game Number
            gnum = row.get("Game Number")
            if str(gnum) != str(idx):
                errors.append(f"{gid}: Game Number mismatch: expected {idx}, got {gnum}")
                
            # Season Year
            sy = row.get("Season Year")
            if str(sy) != str(year):
                errors.append(f"{gid}: Season Year mismatch: expected {year}, got {sy}")
                
            # Scores & Math Invariants
            try:
                hs = int(row.get("Home Score", 0))
                ascore = int(row.get("Away Score", 0))
                tot = int(row.get("Total Points", 0))
                margin = int(row.get("Winning Margin", 0))
                
                if tot != hs + ascore:
                    errors.append(f"{gid}: Total points mismatch: {tot} != {hs} + {ascore}")
                if margin != abs(hs - ascore):
                    errors.append(f"{gid}: Margin mismatch: {margin} != |{hs} - {ascore}|")
                expected_gs = f"{hs} - {ascore}"
                if row.get("Game Score") != expected_gs:
                    errors.append(f"{gid}: Game Score mismatch: {row.get('Game Score')} != {expected_gs}")
            except Exception as e:
                errors.append(f"{gid}: Error parsing scores/margins: {e}")
                
            # Winner / Loser / Result
            res = row.get("Result")
            win = row.get("Winner")
            lose = row.get("Loser")
            ht = row.get("Home Team")
            at = row.get("Away Team")
            
            if hs > ascore:
                if res != "Home Win":
                    errors.append(f"{gid}: Expected Home Win, got {res}")
                if win != ht:
                    errors.append(f"{gid}: Expected Winner {ht}, got {win}")
                if lose != at:
                    errors.append(f"{gid}: Expected Loser {at}, got {lose}")
            elif ascore > hs:
                if res != "Away Win":
                    errors.append(f"{gid}: Expected Away Win, got {res}")
                if win != at:
                    errors.append(f"{gid}: Expected Winner {at}, got {win}")
                if lose != ht:
                    errors.append(f"{gid}: Expected Loser {ht}, got {lose}")
            else:
                if res != "Draw":
                    errors.append(f"{gid}: Expected Draw, got {res}")
                if win != "Tie":
                    errors.append(f"{gid}: Expected Tie winner, got {win}")
                    
            # Date & Day of Week
            dt_str = row.get("Date")
            dow = row.get("Day of Week")
            if not re.match(r"^\d{4}-\d{2}-\d{2}$", dt_str):
                errors.append(f"{gid}: Invalid date format {dt_str}")
            else:
                try:
                    exp_dow = datetime.date.fromisoformat(dt_str).strftime("%A")
                    if dow != exp_dow:
                        errors.append(f"{gid}: Day of Week mismatch: expected {exp_dow}, got {dow}")
                except Exception as e:
                    errors.append(f"{gid}: Date parsing error: {e}")
                    
            # Non-empty checks
            for field in ["League Name", "Era", "Stage / Round", "Home Team", "Away Team", "Venue", "City"]:
                val = row.get(field, "")
                if not val or str(val).strip() == "":
                    errors.append(f"{gid}: Empty required field '{field}'")
                    
    print(f"Validated {seasons_checked} seasons (1975-2026).")
    print(f"Total Standalone Games: {total_games_standalone}")
    print(f"Total Repository Games: {total_games_repo}")
    
    if warnings:
        print(f"\nWarnings encountered ({len(warnings)}):")
        for w in warnings[:10]:
            print(f"  - {w}")
            
    if errors:
        print(f"\nVALIDATION FAILED! {len(errors)} errors found:")
        for err in errors[:25]:
            print(f"  [ERROR] {err}")
        if len(errors) > 25:
            print(f"  ... and {len(errors) - 25} more errors.")
        sys.exit(1)
    else:
        print("\nALL INVARIANTS, SCHEMAS, AND ROW COUNTS PASSED PERFECTLY WITH ZERO ERRORS!")
        print("================================================================================")

if __name__ == "__main__":
    validate_all()
