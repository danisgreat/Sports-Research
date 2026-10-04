#!/usr/bin/env python3
"""
Comprehensive Validation Script for Austria Bundesliga Basketball Datasets (1975-2025)
Checks all 51 seasons across:
1. Austria_Bundesliga_Basketball_CSVs/Austria_Bundesliga_Basketball_<YEAR>.csv
2. Previous Sports Results/Basketball/BSL/<YEAR>/<YEAR>_games.csv
3. Previous Sports Results/Basketball/Austria Basketball Bundesliga/<YEAR>/<YEAR>_games.csv
"""

import os
import csv
import sys
from datetime import datetime

ROOT_DIR = "Austria_Bundesliga_Basketball_CSVs"
BSL_DIR = os.path.join("Previous Sports Results", "Basketball", "BSL")
AUT_DIR = os.path.join("Previous Sports Results", "Basketball", "Austria Basketball Bundesliga")

REQUIRED_HEADERS = [
    "Game Number",
    "Game ID",
    "Season",
    "Season Year",
    "Game Type (Pre-Season, Austrian Supercup, Regular Season, Top 6 / Platzierungsrunde, Qualifizierungsrunde, Quarter-Finals, Semi-Finals, Finals, All-Star Game, Not applicable)",
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

def validate():
    print("=" * 80)
    print("Starting Comprehensive Validation of Austria Bundesliga Basketball Records...")
    print("=" * 80)

    total_root_games = 0
    total_bsl_games = 0
    total_aut_games = 0

    errors = []

    for yr in range(1975, 2026):
        # 1. Root CSV
        root_path = os.path.join(ROOT_DIR, f"Austria_Bundesliga_Basketball_{yr}.csv")
        if not os.path.exists(root_path):
            errors.append(f"Missing root file: {root_path}")
            continue

        # 2. BSL CSV
        bsl_path = os.path.join(BSL_DIR, str(yr), f"{yr}_games.csv")
        if not os.path.exists(bsl_path):
            errors.append(f"Missing BSL file: {bsl_path}")
            continue

        # 3. AUT CSV
        aut_path = os.path.join(AUT_DIR, str(yr), f"{yr}_games.csv")
        if not os.path.exists(aut_path):
            errors.append(f"Missing AUT file: {aut_path}")
            continue

        # Validate Root CSV content
        with open(root_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            headers = reader.fieldnames
            if headers != REQUIRED_HEADERS:
                errors.append(f"Header mismatch in {root_path}")

            rows = list(reader)
            count = len(rows)
            total_root_games += count

            if count == 0:
                errors.append(f"Empty game file: {root_path}")

            game_nums = set()
            game_ids = set()
            prev_date = datetime(yr, 1, 1)

            for idx, r in enumerate(rows):
                gn = int(r["Game Number"])
                gid = r["Game ID"]
                dt_str = r["Date"]
                h_score = int(r["Home Score"])
                a_score = int(r["Away Score"])
                tot = int(r["Total Points"])
                m = int(r["Winning Margin"])
                p_format = r["Period Format"]

                if gn in game_nums:
                    errors.append(f"Duplicate Game Number {gn} in {root_path}")
                game_nums.add(gn)

                if gid in game_ids:
                    errors.append(f"Duplicate Game ID {gid} in {root_path}")
                game_ids.add(gid)

                # Validate date
                try:
                    dt = datetime.strptime(dt_str, "%Y-%m-%d")
                except ValueError:
                    errors.append(f"Invalid date format {dt_str} in {root_path}")

                # Math check
                if h_score + a_score != tot:
                    errors.append(f"Total points mismatch: {h_score}+{a_score}!={tot} in {gid}")
                if abs(h_score - a_score) != m:
                    errors.append(f"Margin mismatch: |{h_score}-{a_score}|!={m} in {gid}")

                # Period format
                if yr < 2000 and "20-minute halves" not in p_format:
                    errors.append(f"Expected halves before 2000, got {p_format} in {gid}")
                elif yr >= 2000 and "10-minute quarters" not in p_format:
                    errors.append(f"Expected quarters from 2000, got {p_format} in {gid}")

                # Non-empty strings
                for col in ["Home", "Away", "Winning Team", "Losing Team", "Venue", "City", "Notable Players", "A Succint one line game comment to summarise that game"]:
                    if not r[col] or len(r[col].strip()) == 0:
                        errors.append(f"Empty column {col} in {gid}")

        # Check BSL CSV matches count
        with open(bsl_path, "r", encoding="utf-8") as f:
            bsl_count = sum(1 for line in f) - 1
            total_bsl_games += bsl_count
            if bsl_count != count:
                errors.append(f"Row count mismatch: root={count}, bsl={bsl_count} for {yr}")

        # Check AUT CSV matches count
        with open(aut_path, "r", encoding="utf-8") as f:
            aut_count = sum(1 for line in f) - 1
            total_aut_games += aut_count
            if aut_count != count:
                errors.append(f"Row count mismatch: root={count}, aut={aut_count} for {yr}")

    print("=" * 80)
    print("VALIDATION RESULTS SUMMARY:")
    print(f"Total Seasons Checked: 51 (1975 to 2025)")
    print(f"Root CSV Directory ({ROOT_DIR}): 51 files, {total_root_games:,} total games")
    print(f"BSL Directory ({BSL_DIR}): 51 files, {total_bsl_games:,} total games")
    print(f"AUT Directory ({AUT_DIR}): 51 files, {total_aut_games:,} total games")
    print(f"Total Errors Found: {len(errors)}")

    if errors:
        print("\nFIRST 10 ERRORS:")
        for err in errors[:10]:
            print(" -", err)
        sys.exit(1)
    else:
        print("\nSUCCESS! 100% OF VALIDATION CHECKS PASSED PERFECTLY!")
        print("=" * 80)

if __name__ == "__main__":
    validate()
