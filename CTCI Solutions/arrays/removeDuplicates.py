'''
PROBLEM STATEMENT:
Remove the duplicate elements in an unsorted n-array!
'''

'''
ANS:
1) count the number of occurences for each element using a dict
2) if the # of occurences == 1: then add that particular element to the array we want to return
'''

'''
Time: O(n) where n is the number of elements in the n-array
Space: O(n)
'''

def removeDups1(arr): 
    mp = {x : None for x in arr}               # values set to zero, all keys are unique by default

    _arr = []

    for key in mp: _arr.append(key)

    return _arr

print(removeDups1([1, 2, 5, 1, 7, 2, 4, 2, 4, 5, 1, -21]))

  