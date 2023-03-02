from itertools import combinations_with_replacement

user_input = input().split(' ')

for i in combinations_with_replacement(sorted(user_input[0]), int(user_input[1])):
    print(''.join(i))