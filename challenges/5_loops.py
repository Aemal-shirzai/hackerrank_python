"""
The provided code stub reads and integer, n , from STDIN.
 For all non-negative integers n < i, print square of i.
"""

if __name__ == '__main__':
    n = int(input())
    
    for num in range(n):
        print(num ** 2)