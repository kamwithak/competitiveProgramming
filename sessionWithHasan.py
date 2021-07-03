<<<<<<< HEAD
"""
Write a function that takes a list as an argument,
iterate over all the numbers in list:
take sum, return sum
"""
def _sum(_input):
  x = 0
  for i in range(len(_input)):
    x += _input[i]
  return x
  
# print(_sum([1,2,3,4,5]))

"""
Write a function nmaed 'isEven' that takes a int as input,
check if the int is even, then return True
if it is odd, then return False
"""
def isEven(n):
  if(n % 2 == 0):
    return True 
  return False

# print(isEven(12))

def isOdd(n):
  return not isEven(n)

"""
Take the sum of a list, but only where the indicies are even.
Call it evenSum([])
"""
def evenSum(_list):
  x = 0 
  for i in range(len(_list)):
    if isEven(i):
      x += _list[i]
  return x
  
# print(evenSum([1,2,3,4,5]))

"""
Given a string, count the number of chars in that string,
and put that into a dictionary.
"""
def countChars(aStr):
  _dict = {}
  for val in aStr:
    if (val in _dict):
      _dict[val] += 1
    else:
      _dict[val] = 1 
  return _dict  

# print(countChars('HASAAN'))
# print({'H':1, 'A':3, 'S':1, 'N':1})

def reverse(_list):
  return _list[::-1]

def flip(param, aMatrix):
  temp = aMatrix
  if (param == 'V'):
    for i in range(len(temp)):
      temp[i] = reverse(temp[i])
  elif (param == 'H'):
    temp = reverse(temp)
  return temp
  
def main(aSequence, aMatrix):
  curMatrix = aMatrix
  for subSequence in aSequence:
    curMatrix = flip(subSequence, curMatrix)
  return curMatrix

# print(main('VH', [[1,2],[3,4]]))


def reverse(arr):
  def swap(i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

  i = 0
  j = len(arr)-1

  while (i <= j):

    swap(i,j)

    i+=1
    j-=1

  return arr

print(reverse([1,2,3,4]))
=======
"""
Write a function that takes a list as an argument,
iterate over all the numbers in list:
take sum, return sum
"""
def _sum(_input):
  x = 0
  for i in range(len(_input)):
    x += _input[i]
  return x
  
# print(_sum([1,2,3,4,5]))

"""
Write a function nmaed 'isEven' that takes a int as input,
check if the int is even, then return True
if it is odd, then return False
"""
def isEven(n):
  if(n % 2 == 0):
    return True 
  return False

# print(isEven(12))

def isOdd(n):
  return not isEven(n)

"""
Take the sum of a list, but only where the indicies are even.
Call it evenSum([])
"""
def evenSum(_list):
  x = 0 
  for i in range(len(_list)):
    if isEven(i):
      x += _list[i]
  return x
  
# print(evenSum([1,2,3,4,5]))

"""
Given a string, count the number of chars in that string,
and put that into a dictionary.
"""
def countChars(aStr):
  _dict = {}
  for val in aStr:
    if (val in _dict):
      _dict[val] += 1
    else:
      _dict[val] = 1 
  return _dict  

# print(countChars('HASAAN'))
# print({'H':1, 'A':3, 'S':1, 'N':1})

def reverse(_list):
  return _list[::-1]

def flip(param, aMatrix):
  temp = aMatrix
  if (param == 'V'):
    for i in range(len(temp)):
      temp[i] = reverse(temp[i])
  elif (param == 'H'):
    temp = reverse(temp)
  return temp
  
def main(aSequence, aMatrix):
  curMatrix = aMatrix
  for subSequence in aSequence:
    curMatrix = flip(subSequence, curMatrix)
  return curMatrix

# print(main('VH', [[1,2],[3,4]]))


def reverse(arr):
  def swap(i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

  i = 0
  j = len(arr)-1

  while (i <= j):

    swap(i,j)

    i+=1
    j-=1

  return arr


reversed = []
def reverse2(arr):
  for elem in arr:
    reversed.insert(0, elem)
  return reversed


print(reverse2([1,2,3,4]))
>>>>>>> c87048f6d203a6448ef863b636a9fca7537a1dee
