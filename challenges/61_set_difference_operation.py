N = int(input())
english_list = set(input().split())

M = int(input())
french_list = set(input().split())


print(len(english_list.difference(french_list)))