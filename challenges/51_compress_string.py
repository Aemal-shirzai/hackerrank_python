from itertools import groupby
for k, c in groupby('1222311'):
    print("(%d, %d)" % (len(list(c)), int(k)), end=' ')