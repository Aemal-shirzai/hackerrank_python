from collections import Counter

total_sheos_count = int(input())
all_size_availible = Counter(map(int, input().split()))
total_customers = int(input())

total_sale = 0
print(all_size_availible)

for customer in range(total_customers):
    size, price = map(int, input().split())
    if all_size_availible[size]:
        total_sale += price
        all_size_availible[size] -= 1