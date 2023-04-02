import re
m = re.search(r'([a-z0-9])\1+', input())
print(m and m.group(1) or -1)
