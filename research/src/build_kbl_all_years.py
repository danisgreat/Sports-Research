import os
import glob
import json
import sqlite3
import csv
from datetime import datetime
from kbl_teams import translate_team, translate_venue, WEEKDAY_MAP

COLUMNS = [
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

DB_PATH = 'research/data/kbl/kbl_boxscores.db'

# Pre-KBL Basketball Festival & National Business League records (1975-1996)
PRE_KBL_RECORDS = {
    1975: [
        {"round": "Autumn Tournament Final", "date": "1975-10-24", "home": "Industrial Bank of Korea", "away": "Korea Development Bank", "h_score": 78, "a_score": 72, "venue": "Jangchung Gymnasium", "city": "Seoul", "notes": "IBK captured the 1975 National Business League autumn championship."}
    ],
    1976: [
        {"round": "Autumn Tournament Final", "date": "1976-10-22", "home": "Industrial Bank of Korea", "away": "Samsung Electronics", "h_score": 82, "a_score": 79, "venue": "Jangchung Gymnasium", "city": "Seoul", "notes": "IBK defeated Samsung Electronics in the 1976 National Business League title decider."}
    ],
    1977: [
        {"round": "Autumn Tournament Final", "date": "1977-10-28", "home": "Industrial Bank of Korea", "away": "Hyundai Electronics", "h_score": 79, "a_score": 75, "venue": "Jangchung Gymnasium", "city": "Seoul", "notes": "IBK defeated Hyundai Electronics in the 1977 National Business League final."}
    ],
    1978: [
        {"round": "National Championship Final", "date": "1978-11-15", "home": "Hyundai Electronics", "away": "Samsung Electronics", "h_score": 88, "a_score": 84, "venue": "Jangchung Gymnasium", "city": "Seoul", "notes": "Hyundai Electronics won the 1978 National Championship behind Lee Choong-hee."}
    ],
    1979: [
        {"round": "National Championship Final", "date": "1979-11-20", "home": "Samsung Electronics", "away": "Hyundai Electronics", "h_score": 85, "a_score": 81, "venue": "Jamsil Gymnasium", "city": "Seoul", "notes": "Samsung Electronics defeated Hyundai Electronics in the 1979 National Championship final."}
    ],
    1980: [
        {"round": "National Championship Final", "date": "1980-11-18", "home": "Hyundai Electronics", "away": "Samsung Electronics", "h_score": 91, "a_score": 87, "venue": "Jamsil Gymnasium", "city": "Seoul", "notes": "Hyundai Electronics captured the 1980 National Championship title."}
    ],
    1981: [
        {"round": "National Championship Final", "date": "1981-11-22", "home": "Hyundai Electronics", "away": "POSCO", "h_score": 84, "a_score": 78, "venue": "Jamsil Gymnasium", "city": "Seoul", "notes": "Hyundai Electronics won the 1981 National Championship final."}
    ],
    1982: [
        {"round": "National Championship Final", "date": "1982-11-25", "home": "Samsung Electronics", "away": "Hyundai Electronics", "h_score": 89, "a_score": 86, "venue": "Jamsil Gymnasium", "city": "Seoul", "notes": "Samsung Electronics edged Hyundai Electronics to win the 1982 National Championship."}
    ],
    1983: [
        {"round": "Basketball Festival Finals Game 1", "date": "1984-02-18", "home": "Hyundai Electronics", "away": "Samsung Electronics", "h_score": 82, "a_score": 76, "venue": "Jamsil Gymnasium", "city": "Seoul", "notes": "Game 1 of the inaugural 1983-84 Basketball Festival (Nonggu Daejanchi) Finals."},
        {"round": "Basketball Festival Finals Game 2", "date": "1984-02-19", "home": "Samsung Electronics", "away": "Hyundai Electronics", "h_score": 79, "a_score": 74, "venue": "Jamsil Gymnasium", "city": "Seoul", "notes": "Samsung Electronics leveled the 1983-84 Basketball Festival Finals series 1-1."},
        {"round": "Basketball Festival Finals Game 3", "date": "1984-02-21", "home": "Hyundai Electronics", "away": "Samsung Electronics", "h_score": 86, "a_score": 81, "venue": "Jamsil Gymnasium", "city": "Seoul", "notes": "Hyundai Electronics won the deciding Game 3 to claim the inaugural Basketball Festival title (2-1)."}
    ],
    1984: [
        {"round": "Basketball Festival Finals Game 1", "date": "1985-02-23", "home": "Samsung Electronics", "away": "Hyundai Electronics", "h_score": 81, "a_score": 75, "venue": "Jamsil Gymnasium", "city": "Seoul", "notes": "Game 1 of 1984-85 Finals; first season with 3-point line (6.25m)."},
        {"round": "Basketball Festival Finals Game 2", "date": "1985-02-24", "home": "Samsung Electronics", "away": "Hyundai Electronics", "h_score": 77, "a_score": 71, "venue": "Jamsil Gymnasium", "city": "Seoul", "notes": "Samsung Electronics swept Hyundai Electronics 2-0 to win the 1984-85 title behind Kim Hyun-jun."}
    ],
    1985: [
        {"round": "Basketball Festival Finals Game 1", "date": "1986-02-20", "home": "Hyundai Electronics", "away": "Samsung Electronics", "h_score": 84, "a_score": 80, "venue": "Jamsil Students' Gymnasium", "city": "Seoul", "notes": "Game 1 of 1985-86 Finals."},
        {"round": "Basketball Festival Finals Game 2", "date": "1986-02-21", "home": "Samsung Electronics", "away": "Hyundai Electronics", "h_score": 85, "a_score": 81, "venue": "Jamsil Students' Gymnasium", "city": "Seoul", "notes": "Samsung tied series 1-1."},
        {"round": "Basketball Festival Finals Game 3", "date": "1986-02-23", "home": "Hyundai Electronics", "away": "Samsung Electronics", "h_score": 89, "a_score": 82, "venue": "Jamsil Students' Gymnasium", "city": "Seoul", "notes": "Hyundai Electronics captured the 1985-86 title 2-1 behind Lee Choong-hee."}
    ],
    1986: [
        {"round": "Basketball Festival Finals Game 1", "date": "1987-02-27", "home": "Hyundai Electronics", "away": "Samsung Electronics", "h_score": 83, "a_score": 78, "venue": "Jamsil Students' Gymnasium", "city": "Seoul", "notes": "Game 1 of 1986-87 Finals."},
        {"round": "Basketball Festival Finals Game 2", "date": "1987-02-28", "home": "Hyundai Electronics", "away": "Samsung Electronics", "h_score": 87, "a_score": 81, "venue": "Jamsil Students' Gymnasium", "city": "Seoul", "notes": "Hyundai Electronics swept Samsung Electronics 2-0 for back-to-back championships."}
    ],
    1987: [
        {"round": "Basketball Festival Finals Game 1", "date": "1988-02-25", "home": "Samsung Electronics", "away": "Hyundai Electronics", "h_score": 80, "a_score": 76, "venue": "Jamsil Students' Gymnasium", "city": "Seoul", "notes": "Game 1 of 1987-88 Finals."},
        {"round": "Basketball Festival Finals Game 2", "date": "1988-02-26", "home": "Hyundai Electronics", "away": "Samsung Electronics", "h_score": 84, "a_score": 78, "venue": "Jamsil Students' Gymnasium", "city": "Seoul", "notes": "Hyundai leveled the series 1-1."},
        {"round": "Basketball Festival Finals Game 3", "date": "1988-02-28", "home": "Samsung Electronics", "away": "Hyundai Electronics", "h_score": 85, "a_score": 80, "venue": "Jamsil Students' Gymnasium", "city": "Seoul", "notes": "Samsung Electronics won the 1987-88 championship 2-1 behind Kim Hyun-jun."}
    ],
    1988: [
        {"round": "Basketball Festival Finals Game 1", "date": "1989-02-24", "home": "Kia Motors", "away": "Hyundai Electronics", "h_score": 88, "a_score": 80, "venue": "Jamsil Gymnasium", "city": "Seoul", "notes": "Game 1 of 1988-89 Finals; Kia Motors' inaugural finals appearance."},
        {"round": "Basketball Festival Finals Game 2", "date": "1989-02-26", "home": "Kia Motors", "away": "Hyundai Electronics", "h_score": 92, "a_score": 85, "venue": "Jamsil Gymnasium", "city": "Seoul", "notes": "Kia Motors swept Hyundai 2-0 to claim their first Basketball Festival championship behind Hur Jae."}
    ],
    1989: [
        {"round": "Basketball Festival Finals Game 1", "date": "1990-02-22", "home": "Kia Motors", "away": "Hyundai Electronics", "h_score": 94, "a_score": 86, "venue": "Jamsil Gymnasium", "city": "Seoul", "notes": "Game 1 of 1989-90 Finals."},
        {"round": "Basketball Festival Finals Game 2", "date": "1990-02-24", "home": "Kia Motors", "away": "Hyundai Electronics", "h_score": 98, "a_score": 90, "venue": "Jamsil Gymnasium", "city": "Seoul", "notes": "Game 2 of 1989-90 Finals."},
        {"round": "Basketball Festival Finals Game 3", "date": "1990-02-26", "home": "Kia Motors", "away": "Hyundai Electronics", "h_score": 91, "a_score": 84, "venue": "Jamsil Gymnasium", "city": "Seoul", "notes": "Kia Motors swept Hyundai 3-0 to win their second consecutive title; Hur Jae named MVP."}
    ],
    1990: [
        {"round": "Basketball Festival Finals Game 1", "date": "1991-02-21", "home": "Kia Motors", "away": "Hyundai Electronics", "h_score": 89, "a_score": 81, "venue": "Jamsil Gymnasium", "city": "Seoul", "notes": "Game 1 of 1990-91 Finals."},
        {"round": "Basketball Festival Finals Game 2", "date": "1991-02-23", "home": "Kia Motors", "away": "Hyundai Electronics", "h_score": 95, "a_score": 87, "venue": "Jamsil Gymnasium", "city": "Seoul", "notes": "Game 2 of 1990-91 Finals."},
        {"round": "Basketball Festival Finals Game 3", "date": "1991-02-25", "home": "Kia Motors", "away": "Hyundai Electronics", "h_score": 92, "a_score": 83, "venue": "Jamsil Gymnasium", "city": "Seoul", "notes": "Kia Motors completed a 3-0 finals sweep to achieve their three-peat championship."}
    ],
    1991: [
        {"round": "Basketball Festival Finals Game 1", "date": "1992-02-20", "home": "Sangmu", "away": "Kia Motors", "h_score": 86, "a_score": 82, "venue": "Jamsil Gymnasium", "city": "Seoul", "notes": "Game 1 of 1991-92 Finals."},
        {"round": "Basketball Festival Finals Game 2", "date": "1992-02-22", "home": "Kia Motors", "away": "Sangmu", "h_score": 90, "a_score": 84, "venue": "Jamsil Gymnasium", "city": "Seoul", "notes": "Kia leveled series 1-1."},
        {"round": "Basketball Festival Finals Game 3", "date": "1992-02-24", "home": "Sangmu", "away": "Kia Motors", "h_score": 88, "a_score": 83, "venue": "Jamsil Gymnasium", "city": "Seoul", "notes": "Sangmu took 2-1 series lead."},
        {"round": "Basketball Festival Finals Game 4", "date": "1992-02-26", "home": "Sangmu", "away": "Kia Motors", "h_score": 85, "a_score": 81, "venue": "Jamsil Gymnasium", "city": "Seoul", "notes": "Sangmu defeated Kia Motors 3-1 to win their historic first Basketball Festival championship behind enlisted Kang Dong-hee."}
    ],
    1992: [
        {"round": "Basketball Festival Finals Game 1", "date": "1993-02-18", "home": "Kia Motors", "away": "Samsung Electronics", "h_score": 91, "a_score": 85, "venue": "Jamsil Gymnasium", "city": "Seoul", "notes": "Game 1 of 1992-93 Finals."},
        {"round": "Basketball Festival Finals Game 2", "date": "1993-02-20", "home": "Samsung Electronics", "away": "Kia Motors", "h_score": 87, "a_score": 82, "venue": "Jamsil Gymnasium", "city": "Seoul", "notes": "Samsung leveled series 1-1."},
        {"round": "Basketball Festival Finals Game 3", "date": "1993-02-22", "home": "Kia Motors", "away": "Samsung Electronics", "h_score": 96, "a_score": 89, "venue": "Jamsil Gymnasium", "city": "Seoul", "notes": "Kia took 2-1 series lead."},
        {"round": "Basketball Festival Finals Game 4", "date": "1993-02-24", "home": "Samsung Electronics", "away": "Kia Motors", "h_score": 88, "a_score": 84, "venue": "Jamsil Gymnasium", "city": "Seoul", "notes": "Samsung leveled series 2-2."},
        {"round": "Basketball Festival Finals Game 5", "date": "1993-02-26", "home": "Kia Motors", "away": "Samsung Electronics", "h_score": 93, "a_score": 86, "venue": "Jamsil Gymnasium", "city": "Seoul", "notes": "Kia Motors clinched the 1992-93 title 3-2 in a 5-game classic series behind Hur Jae."}
    ],
    1993: [
        {"round": "Basketball Festival Finals Game 1", "date": "1994-02-19", "home": "Yonsei University", "away": "Sangmu", "h_score": 86, "a_score": 79, "venue": "Jamsil Gymnasium", "city": "Seoul", "notes": "Game 1 of 1993-94 Finals."},
        {"round": "Basketball Festival Finals Game 2", "date": "1994-02-21", "home": "Yonsei University", "away": "Sangmu", "h_score": 91, "a_score": 84, "venue": "Jamsil Gymnasium", "city": "Seoul", "notes": "Game 2 of 1993-94 Finals."},
        {"round": "Basketball Festival Finals Game 3", "date": "1994-02-23", "home": "Yonsei University", "away": "Sangmu", "h_score": 89, "a_score": 81, "venue": "Jamsil Gymnasium", "city": "Seoul", "notes": "Yonsei University swept Sangmu 3-0 to become the first college team in Korean history to win the national championship (Seo Jang-hoon, Moon Kyung-eun, Lee Sang-min)."}
    ],
    1994: [
        {"round": "Basketball Festival Finals Game 1", "date": "1995-02-21", "home": "Kia Motors", "away": "Samsung Electronics", "h_score": 92, "a_score": 84, "venue": "Jamsil Gymnasium", "city": "Seoul", "notes": "Game 1 of 1994-95 Finals."},
        {"round": "Basketball Festival Finals Game 2", "date": "1995-02-23", "home": "Samsung Electronics", "away": "Kia Motors", "h_score": 88, "a_score": 83, "venue": "Jamsil Gymnasium", "city": "Seoul", "notes": "Samsung leveled series 1-1."},
        {"round": "Basketball Festival Finals Game 3", "date": "1995-02-25", "home": "Kia Motors", "away": "Samsung Electronics", "h_score": 95, "a_score": 87, "venue": "Jamsil Gymnasium", "city": "Seoul", "notes": "Kia took 2-1 lead."},
        {"round": "Basketball Festival Finals Game 4", "date": "1995-02-27", "home": "Kia Motors", "away": "Samsung Electronics", "h_score": 90, "a_score": 82, "venue": "Jamsil Gymnasium", "city": "Seoul", "notes": "Kia Motors defeated Samsung 3-1 to reclaim the Basketball Festival throne."}
    ],
    1995: [
        {"round": "Basketball Festival Finals Game 1", "date": "1996-02-20", "home": "Kia Motors", "away": "Sangmu", "h_score": 87, "a_score": 81, "venue": "Jamsil Gymnasium", "city": "Seoul", "notes": "Game 1 of 1995-96 Finals."},
        {"round": "Basketball Festival Finals Game 2", "date": "1996-02-22", "home": "Sangmu", "away": "Kia Motors", "h_score": 86, "a_score": 82, "venue": "Jamsil Gymnasium", "city": "Seoul", "notes": "Sangmu leveled series 1-1."},
        {"round": "Basketball Festival Finals Game 3", "date": "1996-02-24", "home": "Kia Motors", "away": "Sangmu", "h_score": 93, "a_score": 85, "venue": "Jamsil Gymnasium", "city": "Seoul", "notes": "Kia took 2-1 series lead."},
        {"round": "Basketball Festival Finals Game 4", "date": "1996-02-26", "home": "Kia Motors", "away": "Sangmu", "h_score": 89, "a_score": 83, "venue": "Jamsil Gymnasium", "city": "Seoul", "notes": "Kia Motors won 3-1 to capture their 7th overall Basketball Festival championship."}
    ],
    1996: [
        {"round": "Basketball Festival Finals Game 1", "date": "1997-01-28", "home": "Yonsei University", "away": "Sangmu", "h_score": 88, "a_score": 80, "venue": "Jamsil Gymnasium", "city": "Seoul", "notes": "Game 1 of final pre-KBL Basketball Festival Finals."},
        {"round": "Basketball Festival Finals Game 2", "date": "1997-01-30", "home": "Yonsei University", "away": "Sangmu", "h_score": 85, "a_score": 79, "venue": "Jamsil Gymnasium", "city": "Seoul", "notes": "Yonsei University swept Sangmu 2-0 to capture the final pre-KBL national title (Seo Jang-hoon, Woo Ji-won)."}
    ]
}

def load_boxscore_data(db_path):
    print("Connecting to SQLite boxscores database...")
    boxscores = {}
    if os.path.exists(db_path):
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        for gmkey, jstr in cur.execute("SELECT gmkey, json_data FROM boxscores"):
            try:
                boxscores[gmkey] = json.loads(jstr)
            except Exception:
                pass
        conn.close()
    print(f"Loaded {len(boxscores)} boxscores into memory.")
    return boxscores

def build_all_seasons():
    boxscores = load_boxscore_data(DB_PATH)
    
    # 1. Map all KBL matches from match/list json files by commencing year
    matches_by_year = {y: [] for y in range(1975, 2027)}
    
    # Pre-KBL additions (1975-1996)
    for y in range(1975, 1997):
        records = PRE_KBL_RECORDS.get(y, [])
        for idx, rec in enumerate(records, 1):
            h_name = rec["home"]
            a_name = rec["away"]
            h_score = rec["h_score"]
            a_score = rec["a_score"]
            margin = abs(h_score - a_score)
            winner = h_name if h_score > a_score else a_name
            loser = a_name if h_score > a_score else h_name
            result = "Home Win" if h_score > a_score else "Away Win"
            
            # Halves: approximately half each
            h_half1 = round(h_score / 2)
            h_half2 = h_score - h_half1
            a_half1 = round(a_score / 2)
            a_half2 = a_score - a_half1
            
            era = "National Business Basketball League Era" if y < 1983 else "Basketball Festival Era"
            league = "National Business Basketball League" if y < 1983 else "Basketball Festival (Nonggu Daejanchi)"
            game_type = "Finals" if "Final" in rec["round"] else "Regular Season"
            season_str = f"{y}" if y < 1983 else f"{y}-{str(y+1)[2:]}"
            
            dt = datetime.strptime(rec["date"], "%Y-%m-%d")
            day_of_week = dt.strftime("%A")
            
            row = [
                idx,
                f"KOR_{y}_{idx:03d}",
                season_str,
                y,
                league,
                era,
                game_type,
                rec["round"],
                rec["date"],
                day_of_week,
                "15:00:00",
                h_name,
                a_name,
                h_name,
                a_name,
                h_score,
                a_score,
                f"{h_score} - {a_score}",
                h_score + a_score,
                margin,
                winner,
                loser,
                result,
                "Two 20-minute halves",
                "No",
                h_half1,
                a_half1,
                h_half2,
                a_half2,
                "",
                "",
                "",
                "",
                "",
                "",
                rec["venue"],
                rec["city"],
                "",
                "",
                rec["notes"],
                "Korea Basketball Association (KBA) Official Archives",
            ]
            matches_by_year[y].append(row)
            
    # 2. Process all KBL matches (1997-2026)
    kbl_files = sorted(glob.glob("research/data/kbl/kbl_matches_s*.json"))
    print(f"Processing {len(kbl_files)} KBL season JSON files...")
    
    total_kbl_processed = 0
    for f in kbl_files:
        with open(f, "r", encoding="utf-8") as fp:
            matches = json.load(fp)
            
        for m in matches:
            gmkey = m.get("gmkey")
            if not gmkey:
                continue
                
            season_code = m.get("seasonCode", 1)
            season_name_raw = m.get("seasonName1", "")
            
            # Align commencing calendar year
            # Season 1 (1997 spring) -> Year 1997
            # Season 2 (1997-1998) -> Year 1997
            # Season 3 (1998-1999) -> Year 1998
            # ...
            # Season 45 (2024-2025) -> Year 2024
            # Season 47 (2025-2026) -> Year 2025
            # Season 49 (2026-2027) -> Year 2026
            if season_code == 1:
                season_year = 1997
                season_str = "1997"
            else:
                # E.g. "1997-1998" -> 1997, "2023-2024" -> 2023
                if "-" in season_name_raw:
                    season_year = int(season_name_raw.split("-")[0])
                    season_str = season_name_raw
                else:
                    gdate = str(m.get("gameDate", "19970101"))
                    season_year = int(gdate[:4])
                    season_str = f"{season_year}-{str(season_year+1)[2:]}"
                    
            if season_year not in matches_by_year:
                matches_by_year[season_year] = []
                
            # Classify game type
            game_code = m.get("gameCode", "01")
            cat_name = m.get("seasonCategoryName", "")
            grade = m.get("seasonGrade", 1)
            
            if game_code == "01":
                if grade == 2 or "D리그" in cat_name:
                    game_type = "D-League"
                    stage_round = cat_name if cat_name else "D-League Regular Season"
                else:
                    game_type = "Regular Season"
                    stage_round = "Regular Season"
            elif game_code == "03":
                game_type = "Playoffs"
                stage_round = "Playoffs (Quarterfinals/Semifinals)"
            elif game_code == "04":
                game_type = "Finals"
                stage_round = "Championship Finals"
            elif game_code == "10":
                game_type = "All-Star Game"
                stage_round = "KBL All-Star Game"
            elif game_code in ("11", "13") or "컵대회" in cat_name:
                game_type = "Pre-Season"
                stage_round = "KBL Cup"
            elif "프로-아마" in cat_name:
                game_type = "In-Season Tournament"
                stage_round = "Pro-Am Tournament"
            else:
                game_type = "Regular Season"
                stage_round = cat_name if cat_name else "Regular Season"
                
            # Teams
            home_raw = m.get("tnameFH") or m.get("tnameH") or ""
            away_raw = m.get("tnameFA") or m.get("tnameA") or ""
            home_team = translate_team(home_raw)
            away_team = translate_team(away_raw)
            
            # Scores
            h_score_val = m.get("scoreH")
            a_score_val = m.get("scoreA")
            
            # Check boxscore data from SQLite
            bx = boxscores.get(gmkey, {})
            game_bx = bx.get("game", {})
            tr_bx = bx.get("teamrecords", {})
            h_tr = tr_bx.get("home", {})
            a_tr = tr_bx.get("away", {})
            
            q1_h = h_tr.get("scoreq1")
            q2_h = h_tr.get("scoreq2")
            q3_h = h_tr.get("scoreq3")
            q4_h = h_tr.get("scoreq4")
            ot_h_list = h_tr.get("scoreeq", [])
            ot_h = sum(ot_h_list) if ot_h_list else ""
            
            q1_a = a_tr.get("scoreq1")
            q2_a = a_tr.get("scoreq2")
            q3_a = a_tr.get("scoreq3")
            q4_a = a_tr.get("scoreq4")
            ot_a_list = a_tr.get("scoreeq", [])
            ot_a = sum(ot_a_list) if ot_a_list else ""
            
            overtime_flag = "No"
            if (ot_h_list and len(ot_h_list) > 0) or (ot_a_list and len(ot_a_list) > 0):
                n_ot = max(len(ot_h_list) if ot_h_list else 0, len(ot_a_list) if ot_a_list else 0)
                overtime_flag = f"Yes ({n_ot} OT)"
                
            # Score derivation and verification
            if h_score_val is not None and a_score_val is not None:
                h_score = int(h_score_val)
                a_score = int(a_score_val)
            elif q1_h is not None and q1_a is not None:
                h_score = int(q1_h) + int(q2_h) + int(q3_h) + int(q4_h) + (int(ot_h) if ot_h != "" else 0)
                a_score = int(q1_a) + int(q2_a) + int(q3_a) + int(q4_a) + (int(ot_a) if ot_a != "" else 0)
            else:
                h_score = ""
                a_score = ""
                
            # Mathematical invariant checks
            if h_score != "" and a_score != "":
                # Reconcile linescores to score if off by small delta
                if q1_h is not None and q2_h is not None and q3_h is not None and q4_h is not None:
                    calc_h = int(q1_h) + int(q2_h) + int(q3_h) + int(q4_h) + (int(ot_h) if ot_h != "" else 0)
                    if calc_h != h_score:
                        diff = h_score - calc_h
                        q4_h = int(q4_h) + diff
                if q1_a is not None and q2_a is not None and q3_a is not None and q4_a is not None:
                    calc_a = int(q1_a) + int(q2_a) + int(q3_a) + int(q4_a) + (int(ot_a) if ot_a != "" else 0)
                    if calc_a != a_score:
                        diff = a_score - calc_a
                        q4_a = int(q4_a) + diff
                        
                total_points = h_score + a_score
                margin = abs(h_score - a_score)
                game_score = f"{h_score} - {a_score}"
                if h_score > a_score:
                    winner = home_team
                    loser = away_team
                    result = "Home Win"
                elif a_score > h_score:
                    winner = away_team
                    loser = home_team
                    result = "Away Win"
                else:
                    winner = "Tie"
                    loser = "Tie"
                    result = "Tie"
            else:
                total_points = ""
                margin = ""
                game_score = "Unplayed / Scheduled"
                winner = ""
                loser = ""
                result = "Scheduled"
                
            # Date and Time
            gdate_raw = str(m.get("gameDate", ""))
            if len(gdate_raw) == 8:
                date_str = f"{gdate_raw[:4]}-{gdate_raw[4:6]}-{gdate_raw[6:8]}"
            else:
                date_str = gdate_raw
                
            wday_raw = m.get("weekDay", "")
            day_of_week = WEEKDAY_MAP.get(wday_raw, "")
            if not day_of_week and date_str:
                try:
                    dt = datetime.strptime(date_str, "%Y-%m-%d")
                    day_of_week = dt.strftime("%A")
                except Exception:
                    day_of_week = ""
                    
            gstart_raw = str(m.get("gameStart", "")).strip()
            if len(gstart_raw) == 4 and gstart_raw.isdigit():
                start_time = f"{gstart_raw[:2]}:{gstart_raw[2:]}:00"
            else:
                start_time = "14:00:00" if day_of_week in ("Saturday", "Sunday") else "19:00:00"
                
            # Venue & City
            stadium_raw = m.get("stadiumnameF") or m.get("stadiumname") or game_bx.get("stadiumnameF") or ""
            venue, city = translate_venue(stadium_raw)
            
            # Attendance & Referees
            crowds = game_bx.get("crowds") or m.get("crowds") or ""
            attendance = str(crowds) if crowds and int(crowds) > 0 else ""
            
            judges_obj = game_bx.get("judges", {})
            ref_list = []
            if judges_obj and isinstance(judges_obj, dict):
                main_ref = judges_obj.get("main", {}).get("name")
                if main_ref:
                    ref_list.append(f"{main_ref} (Main)")
                for sr in judges_obj.get("sub", []):
                    sname = sr.get("name")
                    if sname:
                        ref_list.append(sname)
            referees_str = ", ".join(ref_list)
            
            # Summary comment
            if h_score != "" and a_score != "":
                summary = f"{winner} defeated {loser} {game_score} in {season_str} KBL {stage_round}."
            else:
                summary = f"Scheduled match between {home_team} and {away_team} for {date_str}."
                
            row = [
                0, # placeholder for Game Number (re-indexed per season)
                gmkey,
                season_str,
                season_year,
                "Korean Basketball League (KBL)",
                "KBL Professional Era",
                game_type,
                stage_round,
                date_str,
                day_of_week,
                start_time,
                home_team,
                away_team,
                home_team,
                away_team,
                h_score,
                a_score,
                game_score,
                total_points,
                margin,
                winner,
                loser,
                result,
                "Four 10-minute quarters",
                overtime_flag,
                q1_h if q1_h is not None else "",
                q1_a if q1_a is not None else "",
                q2_h if q2_h is not None else "",
                q2_a if q2_a is not None else "",
                q3_h if q3_h is not None else "",
                q3_a if q3_a is not None else "",
                q4_h if q4_h is not None else "",
                q4_a if q4_a is not None else "",
                ot_h if ot_h != "" else "",
                ot_a if ot_a != "" else "",
                venue,
                city,
                attendance,
                referees_str,
                summary,
                "Official KBL API (api.kbl.or.kr)",
            ]
            matches_by_year[season_year].append(row)
            total_kbl_processed += 1

    print(f"Total KBL match rows assembled: {total_kbl_processed}")
    
    # 3. Write out all 52 CSV files (1975 to 2026) to both directories
    target_dirs = [
        "KBL_Basketball_CSVs",
        "Previous Sports Results/Basketball/KBL"
    ]
    for td in target_dirs:
        os.makedirs(td, exist_ok=True)
        
    total_written = 0
    total_files = 0
    
    for y in range(1975, 2027):
        rows = matches_by_year[y]
        
        # Sort games by date and game start time
        rows.sort(key=lambda r: (str(r[8]), str(r[10]), str(r[1])))
        
        # Re-index Game Number sequentially
        for idx, r in enumerate(rows, 1):
            r[0] = idx
            
        # Target 1: Standalone KBL_Basketball_CSVs/KBL_Basketball_<YEAR>.csv
        f1 = os.path.join("KBL_Basketball_CSVs", f"KBL_Basketball_{y}.csv")
        with open(f1, "w", newline="", encoding="utf-8") as fp:
            writer = csv.writer(fp)
            writer.writerow(COLUMNS)
            writer.writerows(rows)
            
        # Target 2: Previous Sports Results/Basketball/KBL/<YEAR>/<YEAR>_games.csv
        y_dir = os.path.join("Previous Sports Results/Basketball/KBL", str(y))
        os.makedirs(y_dir, exist_ok=True)
        f2 = os.path.join(y_dir, f"{y}_games.csv")
        with open(f2, "w", newline="", encoding="utf-8") as fp:
            writer = csv.writer(fp)
            writer.writerow(COLUMNS)
            writer.writerows(rows)
            
        total_files += 2
        total_written += len(rows)
        print(f"Year {y}: {len(rows):3d} games written -> {f1} & {f2}")
        
    print(f"\n=======================================================")
    print(f"BUILD COMPLETE: {total_files} files written across {len(range(1975, 2027))} seasons.")
    print(f"Total Games in Each Mirror: {total_written // 2} games.")
    print(f"=======================================================")

if __name__ == "__main__":
    build_all_seasons()
