test_cases = int(input())

results = []

for _ in range(test_cases):
    size = int(input())
    initial_list = list(map(int, input().split()))

    for _ in range(size-1):
        inserted = initial_list[0]
        if initial_list[0] >= initial_list[-1]:
            initial_list.pop(0)
        else:
            inserted = initial_list[-1]
            initial_list.pop(-1)

        if len(initial_list) == 1:
            results.append('Yes')

        if initial_list[0] > inserted or initial_list[-1] > inserted:
            results.append('No')
            break
    
for a in results:
    print(a)