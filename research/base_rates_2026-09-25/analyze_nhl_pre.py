import json
from analyze_nhl import summarize
P = json.load(open('nhl_pre.json', encoding='utf-8'))
for season in (20252026, 20262027):
    gs = [g for g in P.values() if g['season'] == season and g['gameType'] == 1 and g['gameState'] in ('OFF', 'FINAL')]
    print(json.dumps(summarize(gs, f'preseason {season}')))
