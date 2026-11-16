with open(r"D:\lia-rizki-new\index.html", "r", encoding="utf-8") as f:
    html = f.read()

import re

# Find cover container (id="cover" or data-id="7ecf3c0b")
pos = html.find('id="cover"')
if pos == -1:
    pos = html.find('cover')

print("Snippet of cover (4000 chars):")
print(html[pos:pos+4000])
