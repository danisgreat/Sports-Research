import sys
import requests
from bs4 import BeautifulSoup
import re

sys.stdout.reconfigure(encoding='utf-8')

url = 'https://www.bleague.jp/schedule/?data_format=json&year=2023&tab=1&event=2&mon=all&index=0'
resp = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}).json()

for card_html in resp['topics'][:3]:
    soup = BeautifulSoup(card_html, 'html.parser')
    date_el = soup.find(class_='title')
    game_li = soup.find('li', class_='list-item')
    game_id = game_li.get('id') if game_li else None
    home_name = soup.find(class_='team home').find(class_='team-name').get_text(strip=True) if soup.find(class_='team home') else None
    away_name = soup.find(class_='team away').find(class_='team-name').get_text(strip=True) if soup.find(class_='team away') else None
    home_score = soup.find(class_='number home-score').get_text(strip=True) if soup.find(class_='number home-score') else None
    away_score = soup.find(class_='number away-score').get_text(strip=True) if soup.find(class_='number away-score') else None
    info_arena = soup.find(class_='info-arena')
    spans = [s.get_text(strip=True) for s in info_arena.find_all('span')] if info_arena else []
    
    print(f"Date: {date_el.get_text(strip=True) if date_el else None} | ID: {game_id} | {home_name} ({home_score}) vs {away_name} ({away_score}) | Info: {spans}")
