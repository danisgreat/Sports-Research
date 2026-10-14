import sys
import requests
import json
import re
from bs4 import BeautifulSoup
import time

sys.stdout.reconfigure(encoding='utf-8')

def fetch_events_for_season(year):
    events = [
        (2, "B1 Regular Season", "Regular Season"),
        (3, "B1 Championship Playoffs", "Playoffs"),
        (4, "B1 Relegation Playoff", "Relegation"),
        (5, "B.League All-Star Game", "All-Star Game"),
        (7, "B2 Regular Season", "Regular Season"),
        (8, "B2 Playoffs", "Playoffs"),
        (11, "B1/B2 Promotion/Relegation Series", "Promotion/Relegation"),
        (20, "B.League Early Cup", "Early Cup"),
    ]
    
    all_games = []
    t0 = time.time()
    for ev_id, comp_name, game_type in events:
        index = 0
        current_date = None
        ev_games = 0
        while True:
            url = f"https://www.bleague.jp/schedule/?data_format=json&year={year}&event={ev_id}&mon=all&index={index}"
            try:
                r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=12)
                d = r.json()
            except Exception as e:
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
                
                h_team_el = soup.select_one('.team.home .team-name')
                a_team_el = soup.select_one('.team.away .team-name')
                h_name = h_team_el.get_text(strip=True) if h_team_el else ''
                a_name = a_team_el.get_text(strip=True) if a_team_el else ''
                
                h_score_el = soup.select_one('.home-score span')
                a_score_el = soup.select_one('.away-score span')
                h_score = h_score_el.get_text(strip=True) if h_score_el else ''
                a_score = a_score_el.get_text(strip=True) if a_score_el else ''
                
                info_arena = soup.find(class_='info-arena')
                spans = [s.get_text(strip=True) for s in info_arena.find_all('span')] if info_arena else []
                stage = spans[0] if len(spans) > 0 else comp_name
                venue = spans[1] if len(spans) > 1 else ''
                start_time = spans[2] if len(spans) > 2 else ''
                
                all_games.append({
                    'gid': gid,
                    'comp': comp_name,
                    'game_type': game_type,
                    'stage': stage,
                    'date': current_date,
                    'time': start_time,
                    'home': h_name,
                    'away': a_name,
                    'h_score': h_score,
                    'a_score': a_score,
                    'venue': venue,
                })
                ev_games += 1
                
            next_idx = d.get('index')
            if not next_idx or next_idx <= index:
                break
            index = next_idx
        if ev_games > 0:
            print(f"  {comp_name}: {ev_games} games")
    t1 = time.time()
    print(f"Total games for {year}: {len(all_games)} (fetched in {t1-t0:.2f}s)")
    return all_games

print("Testing 2016 (2016-17 inaugural B.League season):")
g16 = fetch_events_for_season(2016)
if g16:
    print("Sample game:", g16[0])
