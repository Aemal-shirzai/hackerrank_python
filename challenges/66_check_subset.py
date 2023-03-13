N = int(input())

for num in range(N):
    a_set_count = int(input())
    a_set = set(map(int, input().split()))

    b_set_count = int(input())
    b_set = set(map(int, input().split()))

    print(True if a_set.issubset(b_set) else False)