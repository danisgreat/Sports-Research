import urllib.request
import re
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def test_match_id(mid):
    # Try fetching with dummy slug
    url = f'https://live.acb.com/es/partidos/game-{mid}/resumen'
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=5) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            m = re.search(r'"initialMatchHeader":\{"matchId":(\d+),"competitionId":(\d+),"start":"([^"]+)".*?"teams":\{"home":\{[^}]*?"fullName":"([^"]+)".*?"away":\{[^}]*?"fullName":"([^"]+)"', html)
            if m:
                print(f"Match {mid}: {m.group(3)} | {m.group(4)} vs {m.group(5)}")
                return True
            else:
                print(f"Match {mid}: HTML returned, no header found. Len: {len(html)}")
                return False
    except urllib.error.HTTPError as e:
        print(f"Match {mid}: HTTP {e.code}")
        return False
    except Exception as e:
        print(f"Match {mid}: Error {e}")
        return False

print("Testing match IDs:")
for mid in [105400, 105300, 104000, 103000, 102000, 101000, 100000, 95000, 90000]:
    test_match_id(mid)
