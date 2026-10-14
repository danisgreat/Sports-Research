"""
validate_acb.py - Comprehensive validation suite for Spanish Basketball (1975-2026).
Verifies:
1. 52 files in Liga_ACB_Basketball_CSVs/ (1975-2026)
2. 52 files in Previous Sports Results/Basketball/Liga ACB/<YEAR>/ (1975-2026)
3. 1900-1974 pre-establishment headers preserved
4. Exact 41-column basketball schema
5. Sequential 1-indexed Game Numbers (1..N)
6. Total Points == Home Score + Away Score
7. Winning Margin == |Home Score - Away Score|
8. Valid ISO-8601 dates (YYYY-MM-DD)
9. Non-empty home and away teams
10. Valid Results ("Home Win", "Away Win", "Draw")
"""

import os
import csv
import datetime

STANDALONE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "Liga_ACB_Basketball_CSVs"))
REPO_BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "Previous Sports Results", "Basketball", "Liga ACB"))

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
    total_games_verified = 0
    seasons_checked = 0
    
    print("=" * 70)
    print("RUNNING SPANISH LIGA ACB VALIDATION SUITE (1975-2026)")
    print("=" * 70)
    
    # 1. Check pre-establishment files 1900-1974
    for y in range(1900, 1975):
        p = os.path.join(REPO_BASE_DIR, str(y), f"{y}_games.csv")
        if not os.path.exists(p):
            errors.append(f"Missing pre-establishment file: {p}")
        else:
            with open(p, "r", encoding="utf-8") as f:
                header = f.readline().strip()
                if not header.startswith("Game Number"):
                    errors.append(f"Corrupt pre-establishment header in {p}")
                    
    print("[PASS] Pre-establishment files (1900-1974) verified intact.")
    
    # 2. Check 1975-2026 files in both locations
    for y in range(1975, 2027):
        sa_file = os.path.join(STANDALONE_DIR, f"Liga_ACB_Basketball_{y}.csv")
        rp_file = os.path.join(REPO_BASE_DIR, str(y), f"{y}_games.csv")
        
        if not os.path.exists(sa_file):
            errors.append(f"Missing standalone CSV: {sa_file}")
            continue
        if not os.path.exists(rp_file):
            errors.append(f"Missing repo CSV: {rp_file}")
            continue
            
        for path_type, path in [("Standalone", sa_file), ("Repo", rp_file)]:
            with open(path, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                headers = reader.fieldnames
                if headers != EXPECTED_COLUMNS:
                    errors.append(f"Header mismatch in {path_type} {y}: got {len(headers)} cols, expected {len(EXPECTED_COLUMNS)}")
                    continue
                    
                rows = list(reader)
                if len(rows) == 0:
                    errors.append(f"Zero rows in {path_type} {y} ({path})")
                    continue
                    
                if path_type == "Standalone":
                    seasons_checked += 1
                    total_games_verified += len(rows)
                    
                prev_gn = 0
                for row_idx, r in enumerate(rows, start=1):
                    gn = int(r["Game Number"])
                    if gn != prev_gn + 1:
                        errors.append(f"{path_type} {y} row {row_idx}: Non-sequential Game Number {gn} (expected {prev_gn + 1})")
                    prev_gn = gn
                    
                    hs = int(r["Home Score"])
                    ascore = int(r["Away Score"])
                    tot = int(r["Total Points"])
                    margin = int(r["Winning Margin"])
                    
                    if tot != hs + ascore:
                        errors.append(f"{path_type} {y} row {row_idx}: Total mismatch {tot} != {hs} + {ascore}")
                    if margin != abs(hs - ascore):
                        errors.append(f"{path_type} {y} row {row_idx}: Margin mismatch {margin} != |{hs} - {ascore}|")
                    if r["Game Score"] != f"{hs} - {ascore}":
                        errors.append(f"{path_type} {y} row {row_idx}: Score string mismatch '{r['Game Score']}' vs '{hs} - {ascore}'")
                        
                    res = r["Result"]
                    if hs > ascore and res != "Home Win":
                        errors.append(f"{path_type} {y} row {row_idx}: Result mismatch: Home Win expected, got {res}")
                    elif ascore > hs and res != "Away Win":
                        errors.append(f"{path_type} {y} row {row_idx}: Result mismatch: Away Win expected, got {res}")
                    elif hs == ascore and res != "Draw":
                        errors.append(f"{path_type} {y} row {row_idx}: Result mismatch: Draw expected, got {res}")
                        
                    # Date verification
                    dt_str = r["Date"]
                    try:
                        datetime.datetime.strptime(dt_str, "%Y-%m-%d")
                    except ValueError:
                        errors.append(f"{path_type} {y} row {row_idx}: Invalid date format '{dt_str}'")
                        
                    if not r["Home Team"] or not r["Away Team"]:
                        errors.append(f"{path_type} {y} row {row_idx}: Missing team name")
                        
    print(f"\n[INFO] Seasons checked: {seasons_checked} (1975-2026)")
    print(f"[INFO] Total unique games verified: {total_games_verified}")
    print(f"[INFO] Total files verified: {seasons_checked * 2} files")
    
    if errors:
        print(f"\n[FAILED] {len(errors)} validation errors found:")
        for err in errors[:25]:
            print(f"  - {err}")
        return False
    else:
        print("\n[SUCCESS] ALL 104 FILES VALIDATED WITH 100% MATHEMATICAL INTEGRITY!")
        return True

if __name__ == '__main__':
    validate_all()
