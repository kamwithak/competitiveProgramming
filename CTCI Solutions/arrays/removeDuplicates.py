'''
PROBLEM STATEMENT:
1) Remove the duplicate elements in an unsorted n-array!

2) Remove the duplicate elements in a sorted n-array!
'''

'''
ANS:
1)

a) count the number of occurences for each element using a dict
b) if the # of occurences == 1: then add that particular element to the array we want to return

2)

a)
b)
'''

'''
1)
Time: O(n) where n is the number of elements in the n-array
Space: O(n)
'''
def removeDups2(arr):
    pass

'''
1)
Time: O(n) where n is the number of elements in the n-array
Space: O(n)
'''
def removeDups1(arr): 
    mp = {x : None for x in arr}               # values set to zero, all keys are unique by default

    _arr = []

    for key in mp: _arr.append(key)

    return _arr

print(removeDups1([1, 2, 5, 1, 7, 2, 4, 2, 4, 5, 1, -21]))

  