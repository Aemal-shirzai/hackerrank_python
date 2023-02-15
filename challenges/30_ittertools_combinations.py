from itertools import combinations
str, counter = input().split(" ")

for num in range(1, int(counter) + 1):
    for new_combine in combinations(sorted(str), num):
        print (''.join(new_combine))