import urllib.request
import re

headers = {'User-Agent': 'Mozilla/5.0'}

def check_ed(comp, ed):
    url = f'https://acb.com/es/{comp}/calendario?temporada={ed}'
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=5) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            return '"rounds":[{"id":' in html
    except:
        return False

print("Probing Copa del Rey editions:")
copa_eds = []
for ed in [40, 45, 50, 55, 60, 65, 68, 69, 70, 75, 80, 85, 88, 89, 90, 91]:
    has = check_ed('copa-del-rey', ed)
    print(f"Copa ed {ed}: {has}")

print("\nProbing Supercopa editions:")
for ed in [65, 68, 69, 70, 75, 80, 85, 88, 89, 90, 91]:
    has = check_ed('supercopa', ed)
    print(f"Supercopa ed {ed}: {has}")
