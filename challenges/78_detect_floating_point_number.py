import re
N = int(input())
for _ in range(N):
    print(re.search(r'^([-\+])?\d*\.\d+$', input()) is not None)