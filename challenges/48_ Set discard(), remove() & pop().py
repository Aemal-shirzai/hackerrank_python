n = int(input())
s = set(map(int, input().split()))
N = int(input())

for _ in range(N):
    command = input()
    unpacked = command.split()
    if len(unpacked) > 1:
        operation_name, value = unpacked
        try:
            getattr(s, operation_name)(int(value))
        except:
            pass
    else:
        operation_name = command
        getattr(s, operation_name)()
print(sum(s))