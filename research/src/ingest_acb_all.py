"""
ingest_acb_all.py - Complete ingestion engine for Spanish Basketball (1975-2026).
Fetches all official games across Liga Nacional, Liga ACB, Copa del Rey, and Supercopa de España
directly from official acb.com Next.js hydration endpoints, and inserts them into acb.db.
"""

import urllib.request
import re
import json
import sqlite3
import datetime
import os
import sys
import time

from acb_teams import resolve_acb_team
from build_acb_database import DB_PATH, init_db

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
}

def fetch_edition_calendar(comp, edition_id, max_retries=3):
    url = f"https://acb.com/es/{comp}/calendario?temporada={edition_id}"
    req = urllib.request.Request(url, headers=HEADERS)
    for attempt in range(max_retries):
        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                html = resp.read().decode('utf-8', errors='ignore')
            chunks = re.findall(r'self\.__next_f\.push\(\[1,"(.*?)"\]\)', html, re.DOTALL)
            full_text = ''.join(c.encode().decode('unicode_escape', errors='ignore') for c in chunks)
            return full_text
        except Exception as e:
            if attempt == max_retries - 1:
                return None
            time.sleep(1.0)
    return None

def parse_full_text(full_text, comp, season_year, edition_id):
    if not full_text:
        return []
        
    # Extract teams
    teams_matches = list(re.finditer(r'"teams":\s*(\[\{"id":\d+.*?"displayTextColor":"#[0-9a-fA-F]+"[^\}]*\}\])', full_text))
    if not teams_matches:
        t_pos = full_text.rfind('"teams":[{"id":')
        if t_pos == -1:
            return []
        end_t = full_text.find('],"rounds"', t_pos)
        teams_raw = full_text[t_pos+8:end_t+1]
    else:
        teams_raw = teams_matches[-1].group(1)
        
    teams_json = teams_raw.replace('"$undefined"', 'null')
    try:
        teams = json.loads(teams_json)
    except Exception as e:
        # Fallback teams parsing
        teams = []
        team_objs = re.findall(r'\{"id":(\d+),"fullName":"([^"]+)"', teams_raw)
        for t_id, f_name in team_objs:
            teams.append({'id': int(t_id), 'fullName': f_name})
            
    # Extract rounds
    r_pos = full_text.find('"rounds":[{"id":')
    if r_pos == -1:
        return []
    start_bracket = r_pos + 9
    depth = 0
    end_bracket = -1
    for i in range(start_bracket, len(full_text)):
        if full_text[i] == '[':
            depth += 1
        elif full_text[i] == ']':
            depth -= 1
            if depth == 0:
                end_bracket = i
                break
    if end_bracket == -1:
        return []
        
    rounds_raw = full_text[start_bracket:end_bracket+1]
    rounds_clean = re.sub(r'"\$[^\"]+:teams:(\d+)"', r'\1', rounds_raw).replace('"$undefined"', 'null')
    try:
        rounds = json.loads(rounds_clean)
    except Exception as e:
        return []
        
    # Determine League Name & Era
    if season_year <= 1982:
        default_league = "Liga Nacional"
        era = "Liga Nacional Era"
    elif season_year <= 1993:
        default_league = "Liga ACB"
        era = "ACB Founding Era"
    else:
        default_league = "Liga ACB"
        era = "Modern Liga ACB Era"
        
    games = []
    for r in rounds:
        r_num = r.get('roundNumber', 1)
        sp = r.get('subphase')
        sp_id = sp.get('id') if isinstance(sp, dict) else (sp if isinstance(sp, int) else None)
        sp_num = sp.get('subphaseNumber', 1) if isinstance(sp, dict) else 1
        
        for m in r.get('matches', []):
            h_score = m.get('homeTeamScore')
            a_score = m.get('awayTeamScore')
            
            # In historical data or completed games, scores must exist
            if h_score is None or a_score is None:
                continue
                
            m_id = m.get('id')
            h_idx = m.get('homeTeam')
            a_idx = m.get('awayTeam')
            start_dt = m.get('startDateTime', '')
            status = m.get('matchStatus', 'FINALIZADO')
            
            # Resolve team names
            h_name = "Home Team"
            a_name = "Away Team"
            if isinstance(h_idx, int) and h_idx < len(teams):
                h_name = teams[h_idx].get('fullName', teams[h_idx].get('name', 'Home Team'))
            if isinstance(a_idx, int) and a_idx < len(teams):
                a_name = teams[a_idx].get('fullName', teams[a_idx].get('name', 'Away Team'))
                
            h_canon, venue, city, region = resolve_acb_team(h_name)
            a_canon, _, _, _ = resolve_acb_team(a_name)
            
            # Stage & Game Type
            if comp == 'liga':
                league_name = default_league
                if sp_id == 291:
                    game_type = "Playoffs"
                    stage_round = f"Playoffs - Finals Game {sp_num}"
                elif sp_id == 292:
                    game_type = "Playoffs"
                    stage_round = f"Playoffs - Semifinals Game {sp_num}"
                elif sp_id == 293:
                    game_type = "Playoffs"
                    stage_round = f"Playoffs - Quarterfinals Game {sp_num}"
                elif sp_id == 294:
                    game_type = "Playoffs"
                    stage_round = f"Playoffs - Round of 16 Game {sp_num}"
                elif sp_id == 280:
                    game_type = "Relegation / Play-down"
                    stage_round = f"Relegation Series Game {sp_num}"
                elif sp_id == 221:
                    game_type = "Playoffs"
                    stage_round = f"Valencia Bubble - Group Round {sp_num}"
                else:
                    if r_num <= (34 if season_year >= 1994 else 44):
                        game_type = "Regular Season"
                        stage_round = f"Regular Season Round {r_num}"
                    else:
                        game_type = "Playoffs"
                        stage_round = f"Playoffs Round {r_num}"
            elif comp == 'copa-del-rey':
                league_name = "Copa del Rey"
                game_type = "Copa del Rey"
                if sp_id == 291:
                    stage_round = "Copa del Rey - Final"
                elif sp_id == 292:
                    stage_round = "Copa del Rey - Semifinales"
                elif sp_id == 293:
                    stage_round = "Copa del Rey - Cuartos de final"
                else:
                    stage_round = f"Copa del Rey - Round {r_num}"
            elif comp == 'supercopa':
                league_name = "Supercopa de España"
                game_type = "Supercopa de España"
                if sp_id == 291:
                    stage_round = "Supercopa - Final"
                elif sp_id == 292:
                    stage_round = "Supercopa - Semifinales"
                else:
                    stage_round = f"Supercopa - Round {r_num}"
            else:
                league_name = default_league
                game_type = "Regular Season"
                stage_round = f"Round {r_num}"
                
            date_str = start_dt[:10] if start_dt else f"{season_year}-01-01"
            start_time = start_dt[11:16] if len(start_dt) >= 16 else "Not recorded"
            
            # Period format & OT
            period_format = "Four 10-minute quarters" if season_year >= 2000 else "Two 20-minute halves"
            q_final = m.get('currentQuarter', 4)
            overtime = "No" if q_final <= 4 else f"{q_final - 4} OT"
            
            h_int = int(h_score)
            a_int = int(a_score)
            tot = h_int + a_int
            margin = abs(h_int - a_int)
            winner = h_canon if h_int > a_int else (a_canon if a_int > h_int else "Draw")
            loser = a_canon if h_int > a_int else (h_canon if a_int > h_int else "Draw")
            result = "Home Win" if h_int > a_int else ("Away Win" if a_int > h_int else "Draw")
            
            try:
                dt_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
                dow = dt_obj.strftime("%A")
            except:
                dow = "Not recorded"
                
            comp_code = "LIGA" if comp == 'liga' else ("COPA" if comp == 'copa-del-rey' else "SC")
            game_id = f"ACB_{season_year}_{comp_code}_{m_id}"
            
            # Succinct one line comment
            notes = f"Official {league_name} match ID {m_id}. {winner} defeated {loser} by {margin} pts." if winner != "Draw" else f"Official {league_name} match ID {m_id}. Match ended in a draw."
            
            games.append({
                'game_id': game_id,
                'season': f"{season_year}-{str((season_year+1)%100).zfill(2)}",
                'season_year': season_year,
                'league_name': league_name,
                'era': era,
                'game_type': game_type,
                'stage_round': stage_round,
                'date': date_str,
                'day_of_week': dow,
                'start_time': start_time,
                'team_1': h_canon,
                'team_2': a_canon,
                'home_team': h_canon,
                'away_team': a_canon,
                'home_score': h_int,
                'away_score': a_int,
                'game_score': f"{h_int} - {a_int}",
                'total_points': tot,
                'winning_margin': margin,
                'winner': winner,
                'loser': loser,
                'result': result,
                'period_format': period_format,
                'overtime': overtime,
                'q1_home': '', 'q1_away': '',
                'q2_home': '', 'q2_away': '',
                'q3_home': '', 'q3_away': '',
                'q4_home': '', 'q4_away': '',
                'ot_home': '', 'ot_away': '',
                'venue': venue,
                'city': city,
                'attendance': '',
                'referees': '',
                'notes': notes,
                'source': f"Official ACB Next.js API (acb.com, {comp}, edition {edition_id})"
            })
            
    return games

def ingest_all():
    init_db()
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    
    total_inserted = 0
    start_year = 1975
    end_year = 2026
    
    print(f"Beginning complete ACB ingestion from {start_year} to {end_year}...")
    for year in range(start_year, end_year + 1):
        ed = year - 1935
        season_games = []
        
        # 1. Liga (Regular Season + Playoffs)
        t0 = time.time()
        txt_liga = fetch_edition_calendar('liga', ed)
        games_liga = parse_full_text(txt_liga, 'liga', year, ed)
        season_games.extend(games_liga)
        
        # 2. Copa del Rey
        txt_copa = fetch_edition_calendar('copa-del-rey', ed)
        games_copa = parse_full_text(txt_copa, 'copa-del-rey', year, ed)
        season_games.extend(games_copa)
        
        # 3. Supercopa
        txt_sc = fetch_edition_calendar('supercopa', ed)
        games_sc = parse_full_text(txt_sc, 'supercopa', year, ed)
        season_games.extend(games_sc)
        
        # Insert into DB
        for g in season_games:
            cur.execute("""
            INSERT OR REPLACE INTO games VALUES (
                :game_id, :season, :season_year, :league_name, :era, :game_type, :stage_round,
                :date, :day_of_week, :start_time, :team_1, :team_2, :home_team, :away_team,
                :home_score, :away_score, :game_score, :total_points, :winning_margin,
                :winner, :loser, :result, :period_format, :overtime,
                :q1_home, :q1_away, :q2_home, :q2_away, :q3_home, :q3_away, :q4_home, :q4_away,
                :ot_home, :ot_away, :venue, :city, :attendance, :referees, :notes, :source
            )
            """, g)
            
        conn.commit()
        total_inserted += len(season_games)
        elapsed = time.time() - t0
        print(f"Season {year}-{str((year+1)%100).zfill(2)} (Ed {ed}): {len(season_games)} games "
              f"(Liga: {len(games_liga)}, Copa: {len(games_copa)}, SC: {len(games_sc)}) in {elapsed:.1f}s", flush=True)
              
    conn.close()
    print(f"\nIngestion complete! Total games inserted into acb.db: {total_inserted}")

if __name__ == '__main__':
    ingest_all()
