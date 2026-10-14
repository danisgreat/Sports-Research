import sys
import re
import json

sys.stdout.reconfigure(encoding='utf-8')

with open('research/sample_game_501311.html', 'r', encoding='utf-8') as f:
    html = f.read()

m = re.search(r'_contexts_s3id\.data\s*=\s*(\{.*?\});', html, re.DOTALL)
if m:
    data = json.loads(m.group(1))
    game = data.get('Game', {})
    for k in sorted(game.keys()):
        print(f"{k}: {game[k]}")
