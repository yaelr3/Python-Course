import re
from functools import reduce

line = "baby abby yabb"

print(re.sub(r'(\b\w+\b)',lambda m: "".join(sorted(m.group(0))),line))

