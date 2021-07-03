def staircase(n):
    fib = [0, 1]
    if (n==1):
        return fib[n-1]
    elif (n==2):
        return fib[n-1]
    for i in range(2,n):
        fib.append(fib[i-2] + fib[i-1])
    return fib[n-1]

for i in range(1, 10):
    print('i: ', i, end=" - ")
    print('f: ', staircase(i))