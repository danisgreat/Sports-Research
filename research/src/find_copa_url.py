import urllib.request
import re

headers = {'User-Agent': 'Mozilla/5.0'}
req = urllib.request.Request('https://acb.com', headers=headers)
html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8', errors='ignore')
copa_links = re.findall(r'href=[\"\']([^\"\']*copa[^\"\']*)[\"\']', html, re.IGNORECASE)
print('Copa links:', set(copa_links[:20]))
