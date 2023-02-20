from collections import OrderedDict

N = int(input())
recs = OrderedDict()
for _ in range(N):
    name, price = input().rsplit(' ', 1)
    if not name in recs:
        recs[name] = 0
    recs[name] += int(price)

for name, price in recs.items():
    print(f"{name} {price}")