import os
import csv
import glob

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
    "Primary Data Source",
]

def validate_directory(dir_path, is_repo=False):
    print(f"\n--- Checking Directory: {dir_path} ---")
    files_checked = 0
    total_games = 0
    errors = []
    
    for y in range(1975, 2027):
        if is_repo:
            fpath = os.path.join(dir_path, str(y), f"{y}_games.csv")
        else:
            fpath = os.path.join(dir_path, f"KBL_Basketball_{y}.csv")
            
        if not os.path.exists(fpath):
            errors.append(f"Missing file for season {y}: {fpath}")
            continue
            
        files_checked += 1
        with open(fpath, "r", encoding="utf-8") as fp:
            reader = csv.reader(fp)
            header = next(reader, None)
            if header != EXPECTED_COLUMNS:
                errors.append(f"{fpath}: Header mismatch. Found {len(header)} cols, expected {len(EXPECTED_COLUMNS)} cols.")
                continue
                
            game_num = 0
            for row_idx, row in enumerate(reader, 1):
                total_games += 1
                game_num += 1
                
                # Check column count
                if len(row) != len(EXPECTED_COLUMNS):
                    errors.append(f"{fpath} Row {row_idx}: Column count mismatch ({len(row)} != {len(EXPECTED_COLUMNS)})")
                    continue
                    
                g_num = row[0]
                g_id = row[1]
                season = row[2]
                season_year = row[3]
                league = row[4]
                era = row[5]
                game_type = row[6]
                stage = row[7]
                date = row[8]
                home = row[13]
                away = row[14]
                h_score_str = row[15]
                a_score_str = row[16]
                tot_str = row[18]
                margin_str = row[19]
                winner = row[20]
                loser = row[21]
                result = row[22]
                
                # Math checks if scores present
                if h_score_str and a_score_str:
                    try:
                        h_score = int(h_score_str)
                        a_score = int(a_score_str)
                        tot = int(tot_str)
                        margin = int(margin_str)
                        
                        if tot != h_score + a_score:
                            errors.append(f"{fpath} Row {row_idx}: Total mismatch ({tot} != {h_score}+{a_score})")
                        if margin != abs(h_score - a_score):
                            errors.append(f"{fpath} Row {row_idx}: Margin mismatch ({margin} != |{h_score}-{a_score}|)")
                            
                        if h_score > a_score and result != "Home Win":
                            errors.append(f"{fpath} Row {row_idx}: Result mismatch for home win ({result})")
                        elif a_score > h_score and result != "Away Win":
                            errors.append(f"{fpath} Row {row_idx}: Result mismatch for away win ({result})")
                            
                        # Linescores check if all 4 quarters present
                        q1_h, q2_h, q3_h, q4_h = row[25], row[27], row[29], row[31]
                        ot_h = row[33]
                        if q1_h and q2_h and q3_h and q4_h:
                            q_sum = int(q1_h) + int(q2_h) + int(q3_h) + int(q4_h) + (int(ot_h) if ot_h else 0)
                            if q_sum != h_score:
                                errors.append(f"{fpath} Row {row_idx}: Home quarters sum mismatch ({q_sum} != {h_score})")
                                
                        q1_a, q2_a, q3_a, q4_a = row[26], row[28], row[30], row[32]
                        ot_a = row[34]
                        if q1_a and q2_a and q3_a and q4_a:
                            q_sum_a = int(q1_a) + int(q2_a) + int(q3_a) + int(q4_a) + (int(ot_a) if ot_a else 0)
                            if q_sum_a != a_score:
                                errors.append(f"{fpath} Row {row_idx}: Away quarters sum mismatch ({q_sum_a} != {a_score})")
                    except ValueError as ve:
                        errors.append(f"{fpath} Row {row_idx}: Score parse error: {ve}")

    print(f"Directory {dir_path}: {files_checked} files verified, {total_games} games, {len(errors)} errors.")
    if errors:
        for err in errors[:10]:
            print("  ERROR:", err)
    return files_checked, total_games, errors

def main():
    print("=" * 70)
    print("RUNNING KBL COMPLETE VALIDATION SUITE (1975-2026)")
    print("=" * 70)
    
    fc1, tg1, err1 = validate_directory("KBL_Basketball_CSVs", is_repo=False)
    fc2, tg2, err2 = validate_directory("Previous Sports Results/Basketball/KBL", is_repo=True)
    
    total_files = fc1 + fc2
    total_games = tg1 + tg2
    total_errors = len(err1) + len(err2)
    
    print("\n" + "=" * 70)
    print("VALIDATION SUMMARY:")
    print(f"  Total Files Checked: {total_files} (Target: 104 across 52 seasons)")
    print(f"  Total Game Rows Verified: {total_games}")
    print(f"  Total Validation Errors: {total_errors}")
    print("=" * 70)
    
    if total_errors == 0:
        print("ALL 104 FILES PASSED 100% VALIDATION WITH ZERO ERRORS!")
    else:
        print(f"FAILED with {total_errors} errors.")

if __name__ == "__main__":
    main()
