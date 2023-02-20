from collections import OrderedDict

words = OrderedDict()
N = int(input())
for _ in range(N):
    word = input()
    if not word in words:
        words[word] = 0
    words[word] += 1

print(len(words))
print(' '.join([str(count) for count in words.values()]))