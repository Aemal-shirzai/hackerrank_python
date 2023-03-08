from itertools import combinations

N = int(input())
data = input().split()
M = int(input())

combinations = list(combinations(data, M))
combinations_with_a = list(filter(lambda pair: 'a' in pair, combinations))
print("%.4f"%(len(combinations_with_a)/len(combinations)))