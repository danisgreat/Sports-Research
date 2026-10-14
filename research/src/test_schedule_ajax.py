import sys
import requests
import re
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

url = "https://www.bleague.jp/schedule/?tab=1&year=2023&mon=10"
resp = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(resp.text, 'html.parser')

scripts = soup.find_all('script')
for idx, s in enumerate(scripts):
    txt = s.get_text()
    if '_contexts' in txt:
        print(f"Script {idx} has _contexts! Length: {len(txt)}")
        m = re.search(r'_contexts_s3id\.data\s*=\s*(\{.*?\});', txt, re.DOTALL)
        if m:
            print("  Found _contexts_s3id.data in schedule!")
            import json
            data = json.loads(m.group(1))
            print("  Schedule data keys:", list(data.keys())[:15])
            if 'list' in data:
                print("  list length:", len(data['list']))
                if data['list']:
                    print("  list[0] keys:", list(data['list'][0].keys()))
            for k in data:
                if isinstance(data[k], list) and len(data[k]) > 0:
                    print(f"  key {k} is list with length {len(data[k])}")
