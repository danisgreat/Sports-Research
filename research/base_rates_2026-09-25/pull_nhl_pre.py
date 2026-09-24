import json
from pull_nhl_tennis import nhl_season
a = nhl_season('2025-09-18', '2025-10-06')
b = nhl_season('2026-09-18', '2026-09-24')
a.update(b)
json.dump(a, open('nhl_pre.json', 'w', encoding='utf-8'))
from collections import Counter
print(Counter((g['season'], g['gameType'], g['gameState']) for g in a.values()))
