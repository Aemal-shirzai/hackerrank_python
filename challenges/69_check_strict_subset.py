set_a = set(input().split())
N = int(input())

print(all(  set_a > set(input().split()) for _ in range(N) ))