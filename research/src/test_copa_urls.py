import urllib.request

headers = {'User-Agent': 'Mozilla/5.0'}
candidates = [
    'https://acb.com/es/copa-del-rey/calendario?temporada=88',
    'https://acb.com/copa-del-rey/calendario',
    'https://acb.com/es/copa-del-rey/calendario',
    'https://acb.com/es/copadelrey/calendario',
    'https://acb.com/es/liga/calendario?temporada=88',
    'https://acb.com/es/supercopa/calendario?temporada=88',
    'https://acb.com/es/minicopa/calendario?temporada=88'
]
for c in candidates:
    try:
        req = urllib.request.Request(c, headers=headers)
        with urllib.request.urlopen(req, timeout=5) as resp:
            print(f"OK: {c} (code {resp.status})")
    except Exception as e:
        print(f"FAIL: {c} ({e})")
