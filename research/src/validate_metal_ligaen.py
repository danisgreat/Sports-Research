import os
import csv
import re
from datetime import datetime

ROOT_DIR = r"c:\Users\danie\Desktop\Sports Research"
CSV_DIR = os.path.join(ROOT_DIR, "Danish_Metal_Ligaen_Ice_Hockey_CSVs")
MULTI_SPORT_1 = os.path.join(ROOT_DIR, "Previous Sports Results", "Ice Hockey", "Metal Ligaen")
MULTI_SPORT_2 = os.path.join(ROOT_DIR, "Previous Sports Results", "Ice Hockey", "Danish Metal Ligaen")

EXPECTED_HEADERS = [
    'Game Number',
    'Game ID',
    'Season',
    'Season Year',
    'Game Type (Pre-Season, Metal Cup / DIU Pokalen, Regular Season, Quarter-Finals, Semi-Finals, Bronze Medal Game, Finals, All-Star Game, Not applicable)',
    'Round / Stage',
    'Date',
    'Day of Week',
    'Start Time (Local)',
    'Team A',
    'Team B',
    'Home',
    'Away',
    'Home Score',
    'Away Score',
    'Period 1 Home',
    'Period 1 Away',
    'Period 2 Home',
    'Period 2 Away',
    'Period 3 Home',
    'Period 3 Away',
    'OT Home',
    'OT Away',
    'SO Home',
    'SO Away',
    'Total Goals',
    'Winning Margin',
    'Winning Team',
    'Losing Team',
    'Result',
    'Game Score',
    'Period Format',
    'Decision Type',
    'Overtime',
    'Shootout',
    'Venue',
    'City',
    'Attendance',
    'Notable Players',
    'A Succint one line game comment to summarise that game',
    'Primary Data Source'
]

GAME_TYPE_KEY = EXPECTED_HEADERS[4]

def validate_all():
    print("=" * 80)
    print("VALIDATING DANISH METAL LIGAEN ICE HOCKEY DATASET (1975-2025)")
    print("=" * 80)

    total_games = 0
    total_files = 0
    errors = []

    for year in range(1975, 2026):
        fname = f"Danish_Metal_Ligaen_Ice_Hockey_{year}.csv"
        fpath = os.path.join(CSV_DIR, fname)
        mpath1 = os.path.join(MULTI_SPORT_1, str(year), f"{year}_games.csv")
        mpath2 = os.path.join(MULTI_SPORT_2, str(year), f"{year}_games.csv")

        # Check archive file paths exist
        if not os.path.exists(mpath1):
            errors.append(f"Missing Metal Ligaen multi-sport CSV for year {year}: {mpath1}")
            continue
        if not os.path.exists(mpath2):
            errors.append(f"Missing Danish Metal Ligaen multi-sport CSV for year {year}: {mpath2}")
            continue

        total_files += 1

        with open(mpath1, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            headers = reader.fieldnames

            if headers != EXPECTED_HEADERS:
                diff = set(EXPECTED_HEADERS) ^ set(headers)
                errors.append(f"{year}: Headers mismatch! Diff: {diff}")

            game_count = 0
            for idx, row in enumerate(reader, start=1):
                game_count += 1
                total_games += 1

                # Validate data types and logic
                home_score = int(row["Home Score"])
                away_score = int(row["Away Score"])
                tot_goals = int(row["Total Goals"])
                margin = int(row["Winning Margin"])
                winner = row["Winning Team"]
                loser = row["Losing Team"]
                result = row["Result"]

                p1_h = int(row["Period 1 Home"])
                p1_a = int(row["Period 1 Away"])
                p2_h = int(row["Period 2 Home"])
                p2_a = int(row["Period 2 Away"])
                p3_h = int(row["Period 3 Home"])
                p3_a = int(row["Period 3 Away"])
                
                ot_h = int(row["OT Home"]) if row["OT Home"] else 0
                ot_a = int(row["OT Away"]) if row["OT Away"] else 0
                so_h = int(row["SO Home"]) if row["SO Home"] else 0
                so_a = int(row["SO Away"]) if row["SO Away"] else 0

                # Check period sum
                calc_h = p1_h + p2_h + p3_h + ot_h + so_h
                calc_a = p1_a + p2_a + p3_a + ot_a + so_a
                if calc_h != home_score or calc_a != away_score:
                    errors.append(f"{year} Game {row['Game ID']}: Period sum ({calc_h}-{calc_a}) != Final ({home_score}-{away_score})")

                # Math check
                if home_score + away_score != tot_goals:
                    errors.append(f"{year} Game {row['Game ID']}: Total Goals mismatch ({tot_goals} != {home_score + away_score})")
                if abs(home_score - away_score) != margin:
                    errors.append(f"{year} Game {row['Game ID']}: Margin mismatch ({margin} != {abs(home_score - away_score)})")

                # Ties vs Wins
                if winner == "Tie":
                    if year >= 1998 and row[GAME_TYPE_KEY] == "Regular Season":
                        errors.append(f"{year} Game {row['Game ID']}: Tie encountered in post-1998 season!")
                    if home_score != away_score:
                        errors.append(f"{year} Game {row['Game ID']}: Winner is Tie but scores differ ({home_score}-{away_score})")
                    if margin != 0:
                        errors.append(f"{year} Game {row['Game ID']}: Margin should be 0 for tie")
                else:
                    if home_score == away_score:
                        errors.append(f"{year} Game {row['Game ID']}: Scores tied ({home_score}-{away_score}) but winner is {winner}")
                    if winner == row["Home"]:
                        if home_score <= away_score or loser != row["Away"]:
                            errors.append(f"{year} Game {row['Game ID']}: Inconsistent home win")
                    elif winner == row["Away"]:
                        if away_score <= home_score or loser != row["Home"]:
                            errors.append(f"{year} Game {row['Game ID']}: Inconsistent away win")
                    else:
                        errors.append(f"{year} Game {row['Game ID']}: Unknown winner {winner}")

                # Date format
                try:
                    datetime.strptime(row["Date"], "%Y-%m-%d")
                except ValueError:
                    errors.append(f"{year} Game {row['Game ID']}: Invalid date {row['Date']}")

                # Empty field check (except OT and SO which are empty during regulation)
                for col in EXPECTED_HEADERS:
                    if col in ["OT Home", "OT Away", "SO Home", "SO Away"]:
                        continue
                    if not row[col] and row[col] != 0:
                        errors.append(f"{year} Game {row['Game ID']}: Column {col} is empty")

                # 2019 season check: No finals games
                if year == 2019 and row[GAME_TYPE_KEY] in ["Finals", "Bronze Medal Game"]:
                    errors.append(f"2019 season should not have Finals or Bronze Medal games due to COVID cancellation!")

    print(f"Total seasons validated: {total_files}/51")
    print(f"Total games validated: {total_games:,}")
    if errors:
        print(f"FAILED with {len(errors)} errors:")
        for err in errors[:20]:
            print("  -", err)
    else:
        print("ALL AUDITS PASSED WITH ZERO ERRORS!")
    print("=" * 80)

if __name__ == "__main__":
    validate_all()
