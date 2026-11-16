path = "D:/lia-rizki-new/wp-content/uploads/elementor/css/post-81430.css"
with open(path, "r", encoding="utf-8") as f:
    css = f.read()

import re

ids = ['395e316b', '1253c8d7', '1f86e674', '77cdd702', '2c81e3ef', 'a37a48f', '2990bd31', '311ad98d', '883444f']
for cid in ids:
    print(f"=== CSS for {cid} ===")
    for m in re.finditer(rf'[^{{}}]*{cid}[^{{}}]*\{{[^}}]*\}}', css):
        print(m.group(0))
