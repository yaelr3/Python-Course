"""
find the number of valid passphrases
"""

import re
vlaidpassphrases = 0
with open(r'C:\regexp.txt') as file:
    for line in file:
        m = re.search(r'(\b\w+\b)(?=.*?\b\1\b)', (re.sub(r'(\b\w+\b)',lambda m: "".join(sorted(m.group(0))),line)))
        if not m:
            vlaidpassphrases += 1

    print(vlaidpassphrases)
