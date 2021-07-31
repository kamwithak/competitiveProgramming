"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
"""
def iterative(x, n):
  res = 1
  for i in range(abs(n)):
      res *= x
      
  if (n < 0):
      return 1 / res
  
  return res


def recursive(x, n):
  if (n == 0): return 1
  elif (n == 1): return x
  else:
    res = recursive(x, n//2)
    if (n % 2 == 0):
      return res * res
    else:
      return res * res * x

print(iterative(2.000, 10))
print(recursive(2.000, 10))