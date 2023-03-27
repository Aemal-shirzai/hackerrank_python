N, X = map(int, input().split())
SCORES = [map(float, input().split()) for i in range(X)]
for i in zip(*SCORES):
    print( sum(i) / X )