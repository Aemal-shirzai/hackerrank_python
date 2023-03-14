N = input()
ROOMS = input().split()
UNIQUE_ROOMS = set(ROOMS)

for room in list(UNIQUE_ROOMS):
    ROOMS.remove(room)

print(UNIQUE_ROOMS.difference(set(ROOMS)).pop())