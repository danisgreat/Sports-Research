import urllib.request
import re

headers = {'User-Agent': 'Mozilla/5.0'}
url = 'https://www.acb.com/es/liga/calendario'
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req, timeout=15) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

# Extract all self.__next_f.push scripts
next_scripts = re.findall(r'self\.__next_f\.push\(\[1,"(.*?)"\]\)', html, re.DOTALL)
print("Total next_f chunks:", len(next_scripts))

combined = ""
for chunk in next_scripts:
    unescaped = chunk.encode().decode('unicode_escape', errors='ignore')
    combined += unescaped

print("Combined Next.js data length:", len(combined))

sample_teams = re.findall(r'("nombre":\s*"[^"]+"|Real Madrid|Barça|Baskonia|Unicaja)', combined)
print("Sample teams in Next.js data:", list(set(sample_teams))[:10])

sample_dates = re.findall(r'\b202[0-9]-[0-9]{2}-[0-9]{2}\b', combined)
print("Sample dates found:", len(sample_dates), list(set(sample_dates))[:10])

sample_jornadas = re.findall(r'jornada["\s:]+([0-9]+)', combined, re.I)
print("Sample jornadas:", len(sample_jornadas), list(set(sample_jornadas))[:10])
