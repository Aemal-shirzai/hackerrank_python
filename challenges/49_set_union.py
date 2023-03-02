n_count = int(input())
N = set(map(int, input().split()))

m_count = int(input())
M = set(map(int, input().split()))

result = N.union(M)
print(len(result))