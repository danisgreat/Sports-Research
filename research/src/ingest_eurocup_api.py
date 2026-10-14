"""
ingest_eurocup_api.py - Ingests official modern EuroCup & ULEB Cup data (2002-2026).
Queries official Euroleague Basketball API:
https://api-live.euroleague.net/v2/competitions/U/seasons/U{YYYY}/games
"""

import urllib.request
import json
import sqlite3
import datetime
import os
import time

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "eurocup", "eurocup.db")
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

def get_day_of_week(date_str):
    try:
        dt = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return dt.strftime("%A")
    except:
        return ""

def ingest_modern_seasons():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    
    total_games = 0
    print("Beginning modern EuroCup ingestion (2002-2026) from official Euroleague API...")
    
    for yr in range(2002, 2027):
        url = f"https://api-live.euroleague.net/v2/competitions/U/seasons/U{yr}/games"
        req = urllib.request.Request(url, headers=HEADERS)
        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                data = json.loads(resp.read().decode('utf-8'))
        except Exception as e:
            print(f"Error fetching season U{yr}: {e}")
            continue
            
        games = data.get('data', [])
        season_inserted = 0
        
        # League name and Era
        if yr <= 2007:
            league_name = "ULEB Cup"
            era = "ULEB Cup Era"
        elif yr <= 2015:
            league_name = "Eurocup Basketball"
            era = "Eurocup Era"
        elif yr <= 2022:
            league_name = "7DAYS EuroCup"
            era = "Modern EuroCup Era"
        else:
            league_name = "BKT EuroCup"
            era = "Modern EuroCup Era"
            
        for g in games:
            # Only record completed games with scores
            local = g.get('local') or {}
            road = g.get('road') or {}
            h_score = local.get('score')
            a_score = road.get('score')
            
            if h_score is None or a_score is None or not g.get('played', True):
                continue
                
            h_score = int(h_score)
            a_score = int(a_score)
            
            game_code = g.get('gameCode')
            m_id = g.get('id') or game_code
            game_id = f"EUROCUP_{yr}_{game_code}"
            
            # Team names
            h_club = local.get('club') or {}
            a_club = road.get('club') or {}
            h_name = h_club.get('name') or h_club.get('abbreviatedName') or "Home Team"
            a_name = a_club.get('name') or a_club.get('abbreviatedName') or "Away Team"
            
            # Dates & times
            dt_raw = g.get('date', '')
            date_str = dt_raw[:10] if dt_raw else f"{yr}-01-01"
            dow = get_day_of_week(date_str)
            start_time = g.get('confirmedHour') or (dt_raw[11:16] if len(dt_raw) >= 16 else "Not recorded")
            
            # Quarters & Overtime
            l_part = local.get('partials') or {}
            r_part = road.get('partials') or {}
            q1_h = str(l_part.get('partials1', ''))
            q1_a = str(r_part.get('partials1', ''))
            q2_h = str(l_part.get('partials2', ''))
            q2_a = str(r_part.get('partials2', ''))
            q3_h = str(l_part.get('partials3', ''))
            q3_a = str(r_part.get('partials3', ''))
            q4_h = str(l_part.get('partials4', ''))
            q4_a = str(r_part.get('partials4', ''))
            
            l_ot = l_part.get('extraPeriods') or {}
            r_ot = r_part.get('extraPeriods') or {}
            if l_ot or r_ot:
                ot_h_val = sum(int(v) for v in l_ot.values() if isinstance(v, (int, str)) and str(v).isdigit())
                ot_a_val = sum(int(v) for v in r_ot.values() if isinstance(v, (int, str)) and str(v).isdigit())
                ot_h = str(ot_h_val)
                ot_a = str(ot_a_val)
                num_ots = max(len(l_ot), len(r_ot))
                overtime = f"{num_ots} OT" if num_ots > 1 else "1 OT"
            else:
                ot_h = ""
                ot_a = ""
                overtime = "No"
                
            # Venue & Location
            v_info = g.get('venue') or {}
            venue = v_info.get('name', 'Indoor Arena')
            city = ""
            addr = v_info.get('address', '')
            if addr:
                parts = addr.split(',')
                city = parts[-2].strip() if len(parts) >= 2 else addr
            if not city:
                city = "Europe"
                
            # Referees
            refs = []
            for r_key in ['referee1', 'referee2', 'referee3', 'referee4']:
                r_val = g.get(r_key)
                if r_val and isinstance(r_val, str):
                    refs.append(r_val.strip())
                elif r_val and isinstance(r_val, dict):
                    refs.append(r_val.get('name', ''))
            referees = ", ".join(filter(None, refs))
            
            # Attendance
            att_raw = g.get('audience')
            attendance = str(att_raw) if att_raw is not None else ""
            
            # Game type and stage
            phase = g.get('phaseType') or {}
            phase_name = phase.get('name', '') if isinstance(phase, dict) else str(phase)
            round_name = g.get('roundName') or f"Round {g.get('round', 1)}"
            
            if 'Final' in phase_name or 'Final' in round_name:
                game_type = "Finals"
            elif 'Semifinal' in phase_name or 'Semifinal' in round_name:
                game_type = "Semifinals"
            elif 'Quarterfinal' in phase_name or 'Quarterfinal' in round_name:
                game_type = "Quarterfinals"
            elif 'Playoff' in phase_name or 'Eighth' in phase_name or 'Round of 16' in round_name or 'Eighthfinals' in phase_name:
                game_type = "Playoffs"
            elif 'Top 16' in phase_name or 'Last 16' in phase_name or 'Last 32' in phase_name:
                game_type = "Regular Season"
            else:
                game_type = "Regular Season"
                
            stage_round = f"{phase_name} - {round_name}" if phase_name and phase_name != round_name else round_name
            
            # Invariants
            tot = h_score + a_score
            margin = abs(h_score - a_score)
            winner = h_name if h_score > a_score else a_name
            loser = a_name if h_score > a_score else h_name
            result = "Home Win" if h_score > a_score else "Away Win"
            game_score = f"{h_score} - {a_score}"
            
            notes = f"Official EuroCup game code {game_code}. {winner} defeated {loser} by {margin} pts."
            
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
                'game_id': game_id,
                'season': f"{yr}-{str((yr+1)%100).zfill(2)}",
                'season_year': yr,
                'league_name': league_name,
                'era': era,
                'game_type': game_type,
                'stage_round': stage_round,
                'date': date_str,
                'day_of_week': dow,
                'start_time': start_time,
                'team_1': h_name,
                'team_2': a_name,
                'home_team': h_name,
                'away_team': a_name,
                'home_score': h_score,
                'away_score': a_score,
                'game_score': game_score,
                'total_points': tot,
                'winning_margin': margin,
                'winner': winner,
                'loser': loser,
                'result': result,
                'period_format': "Four 10-minute quarters",
                'overtime': overtime,
                'q1_home': q1_h, 'q1_away': q1_a,
                'q2_home': q2_h, 'q2_away': q2_a,
                'q3_home': q3_h, 'q3_away': q3_a,
                'q4_home': q4_h, 'q4_away': q4_a,
                'ot_home': ot_h, 'ot_away': ot_a,
                'venue': venue,
                'city': city,
                'attendance': attendance,
                'referees': referees,
                'notes': notes,
                'source': f"Official Euroleague Basketball API (api-live.euroleague.net, season U{yr})"
            })
            season_inserted += 1
            
        conn.commit()
        total_games += season_inserted
        print(f"Season {yr}-{str((yr+1)%100).zfill(2)}: inserted {season_inserted} matches into eurocup.db")
        time.sleep(0.2)
        
    conn.close()
    print(f"\nModern EuroCup ingestion complete! Total matches: {total_games}")

if __name__ == '__main__':
    ingest_modern_seasons()
