from collections import deque

my_que = deque()
N = int(input())

for _ in range(N):
    command = input()
    unpacked = command.split()
    if len(unpacked) > 1:
        operation_name, value = unpacked
        getattr(my_que, operation_name)(value)
    else:
        operation_name = command
        getattr(my_que, operation_name)()

print(" ".join(val for val in my_que))