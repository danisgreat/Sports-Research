import urllib.request
import urllib.parse
import json
import re
import time
import os

HEADERS = {
    'User-Agent': 'SportsResearchBot/1.0 (https://github.com/sports-research; contact@sportsresearch.org) Python/3.10'
}

def fetch_wiki_parse(page_title):
    url = f"https://es.wikipedia.org/w/api.php?action=parse&page={urllib.parse.quote(page_title)}&format=json&prop=wikitext|sections"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        time.sleep(0.5) # Polite rate limiting to avoid 429
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            if 'parse' in data:
                return data['parse']['wikitext']['*']
            elif 'error' in data:
                print(f"Error for {page_title}: {data['error'].get('info')}")
                return None
    except Exception as e:
        print(f"Exception fetching {page_title}: {e}")
        return None

def test_wiki_season(year):
    y2 = str((year + 1) % 100).zfill(2)
    title = f"Liga_ACB_{year}-{y2}" if year >= 1983 else f"Liga_Nacional_de_Baloncesto_{year}-{y2}"
    print(f"\n--- Checking {year} ({title}) ---")
    wikitext = fetch_wiki_parse(title)
    if not wikitext:
        return
    print(f"Length: {len(wikitext)}")
    
    # Check for match results
    # 1. Sports results module: match_XXX_YYY = 82-62
    matches_sr = re.findall(r'match_([A-Za-z0-9]+)_([A-Za-z0-9]+)\s*=\s*([0-9]{1,3}\s*[-–]\s*[0-9]{1,3})', wikitext)
    print(f"Sports results module matches: {len(matches_sr)}")
    
    # 2. General score patterns: ScoreHome - ScoreAway
    scores = re.findall(r'([0-9]{2,3})\s*[-–]\s*([0-9]{2,3})', wikitext)
    print(f"Total score pairs in wikitext: {len(scores)}")
    
    # 3. Check for playoffs
    has_playoffs = 'playoff' in wikitext.lower()
    print(f"Has playoff section: {has_playoffs}")

for y in [1976, 1983, 1988, 1995, 2005, 2015, 2020, 2023]:
    test_wiki_season(y)
