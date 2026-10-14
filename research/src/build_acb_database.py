"""
build_acb_database.py - Database builder and compiler for Spanish Basketball (1975-2026).
Compiles verified games across Liga Nacional (1975-1983), Liga ACB (1983-2026),
Copa del Rey de Baloncesto, Supercopa de España, and ACB Playoffs.
"""

import sqlite3
import os
import datetime
from acb_teams import resolve_acb_team

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "acb", "acb.db")

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

def insert_game(game_dict):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    
    # Calculate invariants
    h_score = int(game_dict['home_score'])
    a_score = int(game_dict['away_score'])
    tot = h_score + a_score
    margin = abs(h_score - a_score)
    winner = game_dict['home_team'] if h_score > a_score else game_dict['away_team']
    loser = game_dict['away_team'] if h_score > a_score else game_dict['home_team']
    result = "Home Win" if h_score > a_score else "Away Win"
    game_score = f"{h_score} - {a_score}"
    
    # Resolve day of week
    date_str = game_dict['date']
    try:
        dt = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        dow = dt.strftime("%A")
    except:
        dow = ""
        
    cur.execute("""
    INSERT OR REPLACE INTO games VALUES (
        :game_id, :season, :season_year, :league_name, :era, :game_type, :stage_round,
        :date, :day_of_week, :start_time, :team_1, :team_2, :home_team, :away_team,
        :home_score, :away_score, :game_score, :total_points, :winning_margin,
        :winner, :loser, :result, :period_format, :overtime,
        :q1_home, :q1_away, :q2_home, :q2_away, :q3_home, :q3_away, :q4_home, :q4_away,
        :ot_home, :ot_away, :venue, :city, :attendance, :referees, :notes, :source
    )
    """, {
        'game_id': game_dict['game_id'],
        'season': game_dict['season'],
        'season_year': game_dict['season_year'],
        'league_name': game_dict.get('league_name', 'Liga ACB'),
        'era': game_dict['era'],
        'game_type': game_dict['game_type'],
        'stage_round': game_dict['stage_round'],
        'date': date_str,
        'day_of_week': dow,
        'start_time': game_dict.get('start_time', ''),
        'team_1': game_dict['home_team'],
        'team_2': game_dict['away_team'],
        'home_team': game_dict['home_team'],
        'away_team': game_dict['away_team'],
        'home_score': h_score,
        'away_score': a_score,
        'game_score': game_score,
        'total_points': tot,
        'winning_margin': margin,
        'winner': winner,
        'loser': loser,
        'result': result,
        'period_format': game_dict.get('period_format', 'Four 10-minute quarters' if game_dict['season_year'] >= 2000 else 'Two 20-minute halves'),
        'overtime': game_dict.get('overtime', 'No'),
        'q1_home': game_dict.get('q1_home', ''),
        'q1_away': game_dict.get('q1_away', ''),
        'q2_home': game_dict.get('q2_home', ''),
        'q2_away': game_dict.get('q2_away', ''),
        'q3_home': game_dict.get('q3_home', ''),
        'q3_away': game_dict.get('q3_away', ''),
        'q4_home': game_dict.get('q4_home', ''),
        'q4_away': game_dict.get('q4_away', ''),
        'ot_home': game_dict.get('ot_home', ''),
        'ot_away': game_dict.get('ot_away', ''),
        'venue': game_dict.get('venue', ''),
        'city': game_dict.get('city', ''),
        'attendance': game_dict.get('attendance', ''),
        'referees': game_dict.get('referees', ''),
        'notes': game_dict.get('notes', ''),
        'source': game_dict.get('source', 'Official ACB / FEB / Historical Archives')
    })
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
    print("ACB database initialized successfully at", DB_PATH)
