#!/usr/bin/env python3
"""Update the merged open-source PR count in README.md (between OSS-COUNT markers)."""
import json, os, re, urllib.parse, urllib.request
EXCLUDE = ["user:farisbasha", "org:howincodes", "org:stuverse", "user:arshadMusliyarakath", "user:uvaise-mohd",
           "user:krishnaho", "user:Mohammed-Hafil", "user:fathimafida", "org:Wincept-Technologies"]
q = "is:pr author:farisbasha is:merged " + " ".join("-" + e for e in EXCLUDE)
req = urllib.request.Request("https://api.github.com/search/issues?per_page=1&q=" + urllib.parse.quote(q),
                             headers={"Authorization": "Bearer " + os.environ["GITHUB_TOKEN"], "Accept": "application/vnd.github+json"})
n = json.load(urllib.request.urlopen(req))["total_count"]
shown = f"{(n // 5) * 5}+" if n >= 10 else str(n)
badge = (f'<a href="https://github.com/pulls?q=is%3Apr+author%3Afarisbasha+is%3Amerged+-user%3Afarisbasha">'
         f'<img src="https://img.shields.io/badge/merged%20pull%20requests-{urllib.parse.quote(shown)}-2ea44f?style=for-the-badge&logo=github" alt="{shown} merged pull requests"/></a>')
s = open("README.md").read()
new = re.sub(r"<!--OSS-COUNT-->.*?<!--/OSS-COUNT-->", f"<!--OSS-COUNT-->{badge}<!--/OSS-COUNT-->", s, flags=re.S)
if new != s:
    open("README.md", "w").write(new)
    print("updated", shown)
else:
    print("unchanged", shown)
