"""
These are example implementations, with varying complexities,
for returning the nth # in the fibonacci sequence.
Kam
"""


""" 

Time: O(N)
Space: O(1)

""" 
def iterativeFib2(n):
    if (n == 0 or n == 1): return n
    fib = 1
    fib_prev = 1
    for i in range(1, n-1):
        tmp = fib
        fib += fib_prev
        fib_prev = tmp
    return fib

""" 

Time: O(N)
Space: O(N)

""" 
def iterativeFib1(n):
    fib = []
    fib.append(0)
    fib.append(1)
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib[n]

""" 

Time: O(N)
Space: O(N)

""" 
def recursiveFib(n):
    if (n == 0 or n == 1): return n
    else: return recursiveFib(n-2) + recursiveFib(n-1)

if __name__ == "__main__":
    for i in range(0, 20):
        print(iterativeFib1(i) == iterativeFib2(i) == recursiveFib(i))
