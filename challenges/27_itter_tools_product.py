from itertools import product

from itertools import product

a = list(map(int, input().split(' ')))
b = list(map(int, input().split(' ')))


print(*list(product(a, b)))

# OR

# new_list = ''
# for outer in a:
#     for inner in b:
#         new_list += str((outer, inner)) + ' '
# print(new_list)