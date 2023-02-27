n, m = input().split()
all_integers = input().split()
N = set(input().split())
M = set(input().split())
happiness = 0

for num in all_integers:
    if num in N:
        happiness += 1
    elif num in M:
        happiness -= 1
        
print(happiness)