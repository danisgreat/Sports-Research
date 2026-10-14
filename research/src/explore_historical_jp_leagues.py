import sys
import requests
import json
import re

sys.stdout.reconfigure(encoding='utf-8')

headers = {'User-Agent': 'Mozilla/5.0'}

# 1. Test ja.wikipedia articles for bj-league, JBL, NBL, Japan League
test_articles = [
    "bjリーグ2005-06",
    "bjリーグ2015-16",
    "JBLスーパーリーグ 2001-02",
    "JBL 2007-08",
    "ナショナル・バスケットボール・リーグ (日本) 2013-14",
    "第9回バスケットボール日本リーグ", # 1975-76 is 9th Japan League
    "第10回バスケットボール日本リーグ",
]

for title in test_articles:
    url = f"https://ja.wikipedia.org/w/api.php?action=parse&page={title}&format=json&prop=sections|wikitext"
    r = requests.get(url, headers=headers).json()
    if 'parse' in r:
        sections = [s['line'] for s in r['parse'].get('sections', [])]
        print(f"Article '{title}' EXISTS! ({len(r['parse']['wikitext']['*'])} chars, {len(sections)} sections)")
        print(f"  Sample sections: {sections[:5]}")
    else:
        print(f"Article '{title}' NOT FOUND")
