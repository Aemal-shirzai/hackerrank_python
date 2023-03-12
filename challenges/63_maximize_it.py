from itertools import product

N, M = map(int, input().split())
all_lists = []
for list_n in range(N):
    list_values = list(map(int, input().split()))[1:]
    all_lists.append(list_values)

result = map(lambda combination: sum(i*i for i in combination)%M, list(product(*all_lists)))
print(max(result))