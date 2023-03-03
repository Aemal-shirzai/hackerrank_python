import numpy
N = int(input())
a = numpy.array([input().split() for _ in range(N)], int)
b = numpy.array([input().split() for _ in range(N)], int)
print(numpy.dot(a, b))
