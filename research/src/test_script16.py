import sys
import requests
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

url = 'https://www.bleague.jp/schedule/?tab=1&year=2023&mon=10'
resp = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(resp.text, 'html.parser')
scripts = soup.find_all('script')
print(scripts[16].get_text()[:1500])
