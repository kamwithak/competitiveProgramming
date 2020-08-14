'''
PROBLEM STATEMENT:
Remove the duplicate elements in an unsorted n-array!
'''

'''
ANS:

'''

'''
Time: O(n) where n is the number of elements in the n-array
Space: O(n)
'''

def removeDups(arr): 
    mp = {x : None for x in arr}               # values set to zero, all keys are unique by default

    _arr = []

    for key in mp: _arr.append(key)

    return _arr

print(removeDups([1, 2, 5, 1, 7, 2, 4, 2, 4, 5, 1, -21]))

  