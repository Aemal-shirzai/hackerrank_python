N = int(input())
english_list = set(input().split())

M = int(input())
french_list = set(input().split())


print(len(english_list.symmetric_difference(french_list)))