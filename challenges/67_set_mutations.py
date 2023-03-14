N = int(input())
ListA = set(input().split())
operations = int(input())

for operation in range(operations):
    command, length = input().split()
    ListB = set(input().split())
    getattr(ListA, command)(ListB)

print(sum(map(int, ListA)))