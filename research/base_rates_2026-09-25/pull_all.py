from fetch import espn_scoreboard
import json
SPEC = [('basketball/wnba','20260501','20260924'),('basketball/nba','20251021','20260620'),
        ('basketball/nbl','20250918','20260331'),('hockey/nhl','20251007','20260620'),
        ('soccer/eng.1','20250815','20260524')]
out = {}
for path,s,e in SPEC:
    d = espn_scoreboard(path,s,e)
    ev = d['events']
    fin = [x for x in ev if x['status']['type'].get('completed')]
    out[path] = {'n_days': d['n_days'], 'failed': len(d['failed_days']), 'events': len(ev), 'completed': len(fin)}
    print(path, out[path], flush=True)
