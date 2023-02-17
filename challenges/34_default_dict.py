from collections import defaultdict

n, m = map(int, input().split(' '))
A = [input() for i in range(n)]
B = [input() for i in range(m)]

for b_item in B:
    if not b_item in A:
        print('-1')
        continue
    
    print(' '.join([str(i+1) for i, x in enumerate(A) if x == b_item]))