from collections import defaultdict

n, m = map(int, input().split(' '))
D = defaultdict(list)
for a_index in range(1, n+1):
    D[input().rstrip()].append(a_index)

for b_index in range(1, m+1):
    b_item = input().rstrip()
    if not b_item in D:
        print('-1')
        continue
    
    print(' '.join(map(str, D[b_item])))

# OR

# A = [input() for i in range(n)]
# B = [input() for i in range(m)]

# for b_item in B:
#     if not b_item in A:
#         print('-1')
#         continue
    
#     print(' '.join([str(i+1) for i, x in enumerate(A) if x == b_item]))
