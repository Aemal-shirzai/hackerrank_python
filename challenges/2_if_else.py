"""
Given an integer, , perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of  to , print Not Weird
If n is even and in the inclusive range of  to , print Weird
If n is even and greater than , print Not Weird
"""

def my_func(n):
    is_even = n % 2 == 0
    if not is_even or (is_even and n in range(6, 21)):
        print('Weird')
    elif n in range(2, 6) or n > 20:
        print('Not Weird')

if __name__ == '__main__':
    n = int(input().strip())
    my_func(n)
