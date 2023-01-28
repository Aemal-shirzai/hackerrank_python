"""
The included code stub will read an integer, n, from STDIN.
Without using any string methods, try to print the following:
123....n
"""
if __name__ == '__main__':
    n = int(input())
    print(''.join(list(map(lambda val: str(val), range(1, n + 1)))))
