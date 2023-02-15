from itertools import permutations
str, counter = input().split(" ")
permutated = list(permutations(str, int(counter)))
permutated.sort()
for perm in permutated:
    print(''.join(perm))