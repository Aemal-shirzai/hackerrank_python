cube = lambda x: pow(x, 3)

def fibonacci(N):
    fab_lis = [0,1]

    for i in range(2, N):
        fab_lis.append(fab_lis[i-2] + fab_lis[i-1])
    
    return(fab_lis[0:N])

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))