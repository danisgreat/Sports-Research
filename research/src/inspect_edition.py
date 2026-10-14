import urllib.request
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

url = "https://acb.com/es/liga/calendario?temporada=88"
req = urllib.request.Request(url, headers=headers)
html = urllib.request.urlopen(req, timeout=15).read().decode('utf-8', errors='ignore')

# Unescape Next.js RSC chunks
chunks = re.findall(r'self\.__next_f\.push\(\[1,"(.*?)"\]\)', html, re.DOTALL)
full_text = ''.join(c.encode().decode('unicode_escape', errors='ignore') for c in chunks)

print("Edition 88 unescaped RSC text len:", len(full_text))

# Search for any occurrence of 6-digit number or matches or rounds
round_matches = re.findall(r'round[A-Za-z0-9_]*["\s:]+([0-9]+)', full_text, re.I)
print("Round matches:", set(round_matches))

# Look for match links or IDs
links = re.findall(r'href=[\'"]([^\'"]*partido[^\'"]*)[\'"]', full_text)
print("Match links in full_text:", len(links), links[:5])

# Find scores
scores = re.findall(r'(\b\d{2,3}\s*[-–]\s*\d{2,3}\b)', full_text)
print("Score strings in full_text:", len(scores), scores[:10])
