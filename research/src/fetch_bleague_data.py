import os
import sys
import requests
import json
import re
import sqlite3
import time
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

DB_PATH = "research/data/bleague/bleague.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS games (
            gid TEXT PRIMARY KEY,
            year INTEGER,
            season TEXT,
            tab INTEGER,
            event_id INTEGER,
            comp_name TEXT,
            game_type TEXT,
            stage TEXT,
            game_date TEXT,
            start_time TEXT,
            home_team_raw TEXT,
            away_team_raw TEXT,
            home_score INTEGER,
            away_score INTEGER,
            venue_raw TEXT,
            status TEXT
        )
    """)
    conn.commit()
    conn.close()

def fetch_season_games(year):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    
    season_str = f"{year}-{year+1-2000:02d}"
    
    # Event configs: (tab, event_id, comp_name, game_type)
    configs = [
        (1, 2, "B.League B1", "Regular Season"),
        (1, 3, "B.League B1 Championship", "Playoffs"),
        (1, 4, "B.League B1 Relegation Playoff", "Relegation"),
        (1, 5, "B.League All-Star Game", "All-Star Game"),
        (1, 11, "B.League B1/B2 Promotion/Relegation", "Promotion/Relegation"),
        (1, 20, "B.League Early Cup", "Early Cup"),
        (2, 7, "B.League B2", "Regular Season"),
        (2, 8, "B.League B2 Playoffs", "Playoffs"),
        (2, 9, "B.League B2 Relegation Playoff", "Relegation"),
    ]
    
    total_added = 0
    t0 = time.time()
    for tab, ev_id, comp, gtype in configs:
        index = 0
        current_date = None
        ev_count = 0
        while True:
            url = f"https://www.bleague.jp/schedule/?data_format=json&year={year}&tab={tab}&event={ev_id}&mon=all&index={index}"
            try:
                r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=12)
                d = r.json()
            except Exception as e:
                # Retry once
                try:
                    time.sleep(0.5)
                    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=15)
                    d = r.json()
                except Exception:
                    break
                    
            topics = d.get('topics', [])
            if not topics:
                break
                
            for card in topics:
                soup = BeautifulSoup(card, 'html.parser')
                date_box = soup.find(class_='champion-box') or soup.find(class_='title')
                if date_box:
                    d_txt = date_box.get_text(strip=True)
                    m = re.search(r'(\d{4}\.\d{2}\.\d{2})', d_txt)
                    if m:
                        current_date = m.group(1).replace('.', '-')
                        
                li = soup.find('li', class_='list-item')
                if not li:
                    continue
                gid = li.get('id')
                if not gid:
                    continue
                    
                h_team_el = soup.select_one('.team.home .team-name')
                a_team_el = soup.select_one('.team.away .team-name')
                h_name = h_team_el.get_text(strip=True) if h_team_el else ''
                a_name = a_team_el.get_text(strip=True) if a_team_el else ''
                
                h_score_el = soup.select_one('.home-score span')
                a_score_el = soup.select_one('.away-score span')
                h_score_str = h_score_el.get_text(strip=True) if h_score_el else ''
                a_score_str = a_score_el.get_text(strip=True) if a_score_el else ''
                
                h_score = int(h_score_str) if h_score_str.isdigit() else None
                away_score = int(a_score_str) if a_score_str.isdigit() else None
                
                info_arena = soup.find(class_='info-arena')
                spans = [s.get_text(strip=True) for s in info_arena.find_all('span')] if info_arena else []
                stage = spans[0] if len(spans) > 0 else comp
                venue = spans[1] if len(spans) > 1 else ''
                start_time = spans[2] if len(spans) > 2 else ''
                
                status_el = soup.find(class_='info-scorestate')
                status = status_el.get_text(strip=True) if status_el else 'FINAL'
                
                cur.execute("""
                    INSERT OR REPLACE INTO games (
                        gid, year, season, tab, event_id, comp_name, game_type,
                        stage, game_date, start_time, home_team_raw, away_team_raw,
                        home_score, away_score, venue_raw, status
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    gid, year, season_str, tab, ev_id, comp, gtype,
                    stage, current_date, start_time, h_name, a_name,
                    h_score, away_score, venue, status
                ))
                ev_count += 1
                total_added += 1
                
            next_idx = d.get('index')
            if not next_idx or next_idx <= index:
                break
            index = next_idx
            
    conn.commit()
    conn.close()
    t1 = time.time()
    print(f"Season {season_str} (Year {year}): {total_added} games saved in {t1-t0:.2f}s")
    return total_added

def main():
    init_db()
    print("=" * 60)
    print("FETCHING B.LEAGUE SEASONS (2016-2025)")
    print("=" * 60)
    grand_total = 0
    for y in range(2016, 2026):
        cnt = fetch_season_games(y)
        grand_total += cnt
    print(f"\nGRAND TOTAL B.LEAGUE GAMES INGESTED: {grand_total}")

if __name__ == "__main__":
    main()
