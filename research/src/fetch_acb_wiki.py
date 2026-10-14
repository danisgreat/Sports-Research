"""
fetch_acb_wiki.py - Extract game results from Spanish Wikipedia for Liga ACB & Liga Nacional.
"""

import urllib.request
import urllib.parse
import json
import re
import time
from acb_teams import resolve_acb_team

HEADERS = {
    'User-Agent': 'SportsResearchBot/1.0 (contact@sportsresearch.org)'
}

def get_wikitext(page_title):
    url = f"https://es.wikipedia.org/w/api.php?action=parse&page={urllib.parse.quote(page_title)}&format=json&prop=wikitext"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        time.sleep(0.4)
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            return data.get('parse', {}).get('wikitext', {}).get('*', '')
    except Exception as e:
        print(f"Error fetching {page_title}: {e}")
        return ""

def parse_sports_results(wikitext, season_year):
    # Finds {{#invoke:Sports results|main ... }}
    # and extracts team codes and match_XXX_YYY = ScoreH - ScoreA
    games = []
    sr_match = re.search(r'\{\{#invoke:Sports results\|main(.*?)\}\}', wikitext, re.DOTALL)
    if not sr_match:
        return games
    sr_content = sr_match.group(1)
    
    # Extract team names: name_XXX = [[Link|Name]]
    team_names = {}
    for line in sr_content.splitlines():
        m = re.search(r'name_([A-Za-z0-9]+)\s*=\s*(?:\[\[(?:[^\|\]]+\|)?([^\]]+)\]\]|([^|\n]+))', line)
        if m:
            code = m.group(1).strip()
            name = (m.group(2) or m.group(3)).strip()
            team_names[code] = name
            
    # Extract matches: match_XXX_YYY = 82-62
    match_lines = re.findall(r'match_([A-Za-z0-9]+)_([A-Za-z0-9]+)\s*=\s*([0-9]{1,3})\s*[-–]\s*([0-9]{1,3})', sr_content)
    game_idx = 1
    for h_code, a_code, h_s, a_s in match_lines:
        h_raw = team_names.get(h_code, h_code)
        a_raw = team_names.get(a_code, a_code)
        h_canon, venue, city, region = resolve_acb_team(h_raw)
        a_canon, _, _, _ = resolve_acb_team(a_raw)
        
        # Approximate round / date based on index if not explicitly parsed
        games.append({
            'game_id': f"ACB_{season_year}_RS_{game_idx:04d}",
            'season': f"{season_year}-{str((season_year+1)%100).zfill(2)}",
            'season_year': season_year,
            'league_name': "Liga ACB",
            'era': "Modern Liga ACB Era",
            'game_type': "Regular Season",
            'stage_round': f"Regular Season Round {((game_idx-1)//9)+1}",
            'date': f"{season_year}-10-15", # Placeholder will be refined
            'home_team': h_canon,
            'away_team': a_canon,
            'home_score': int(h_s),
            'away_score': int(a_s),
            'venue': venue,
            'city': city,
            'attendance': "",
            'referees': "",
            'notes': "",
            'source': "Wikipedia Spanish ACB Results Table"
        })
        game_idx += 1
    return games

if __name__ == '__main__':
    for y in [2020, 2021, 2022, 2023, 2024]:
        y2 = str((y + 1) % 100).zfill(2)
        wt = get_wikitext(f"Liga_ACB_{y}-{y2}")
        g = parse_sports_results(wt, y)
        print(f"Season {y}-{y+1}: extracted {len(g)} regular season games")
