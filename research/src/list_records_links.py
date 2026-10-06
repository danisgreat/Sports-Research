import urllib.request
import re

url = "https://stats.espncricinfo.com/ci/engine/records/index.html?category=9;class=2"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
html = urllib.request.urlopen(req).read().decode("utf-8", errors="replace")

for m in re.finditer(r'<a href="(/ci/engine/records/[^"]+)"[^>]*>(.*?)</a>', html):
    link = m.group(1)
    text = re.sub(r'<[^>]+>', '', m.group(2)).strip()
    if text:
        print(f"{text}: {link}")
