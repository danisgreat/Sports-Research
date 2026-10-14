import sys
import requests
import json
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')
headers = {'User-Agent': 'SportsResearchBot/1.0 (contact@sportsresearch.org)'}

def inspect_page(title):
    url = f"https://ja.wikipedia.org/w/api.php?action=parse&page={title}&format=json&prop=text"
    try:
        r = requests.get(url, headers=headers).json()
        if 'parse' not in r:
            print(f"[{title}] Not found")
            return
        html = r['parse']['text']['*']
        soup = BeautifulSoup(html, 'html.parser')
        tables = soup.find_all('table')
        print(f"[{title}] {len(html)} chars, {len(tables)} tables")
        for i, tbl in enumerate(tables[:4]):
            cls = tbl.get('class', [])
            rows = tbl.find_all('tr')
            headers_txt = [th.get_text(strip=True) for th in tbl.find_all('th')]
            print(f"  Table {i} ({' '.join(cls)}): {len(rows)} rows, th={headers_txt[:6]}")
    except Exception as e:
        print(f"[{title}] Error: {e}")

test_titles = [
    "Bjリーグ 2005-06",
    "Bjリーグ 2010-11",
    "Bjリーグ 2015-16",
    "JBLスーパーリーグ 2001-02",
    "JBL 2007-08",
    "JBL 2010-11",
    "NBL 2013-14",
    "NBL 2015-16",
    "バスケットボール日本リーグ",
    "第9回バスケットボール日本リーグ",
]

for t in test_titles:
    inspect_page(t)
