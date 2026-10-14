"""
build_eurocup_database.py - Database initialization for Euro Cup Basketball (1975-2026).
Compiles games across:
- FIBA European Cup Winners' Cup (1975-1991)
- FIBA European Cup (1991-1996)
- FIBA EuroCup (1996-1998)
- FIBA Saporta Cup (1998-2002)
- ULEB Cup (2002-2008)
- Eurocup Basketball / 7DAYS EuroCup / BKT EuroCup (2008-2026)
"""

import sqlite3
import os
import datetime

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "eurocup", "eurocup.db")

def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS games (
        game_id TEXT PRIMARY KEY,
        season TEXT,
        season_year INTEGER,
        league_name TEXT,
        era TEXT,
        game_type TEXT,
        stage_round TEXT,
        date TEXT,
        day_of_week TEXT,
        start_time TEXT,
        team_1 TEXT,
        team_2 TEXT,
        home_team TEXT,
        away_team TEXT,
        home_score INTEGER,
        away_score INTEGER,
        game_score TEXT,
        total_points INTEGER,
        winning_margin INTEGER,
        winner TEXT,
        loser TEXT,
        result TEXT,
        period_format TEXT,
        overtime TEXT,
        q1_home TEXT,
        q1_away TEXT,
        q2_home TEXT,
        q2_away TEXT,
        q3_home TEXT,
        q3_away TEXT,
        q4_home TEXT,
        q4_away TEXT,
        ot_home TEXT,
        ot_away TEXT,
        venue TEXT,
        city TEXT,
        attendance TEXT,
        referees TEXT,
        notes TEXT,
        source TEXT
    )
    """)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
    print("EuroCup database initialized successfully at", DB_PATH)
