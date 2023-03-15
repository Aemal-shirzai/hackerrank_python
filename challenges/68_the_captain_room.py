N = input()
ROOMS = input().split()

all_rooms = set()
captain_rooms = set()

for room in ROOMS:
    if room not in all_rooms:
        all_rooms.add(room)
        captain_rooms.add(room)
    else:
        captain_rooms.discard(room)
        
print(captain_rooms.pop())