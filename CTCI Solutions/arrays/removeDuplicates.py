'''
PROBLEM STATEMENT:
1) Remove the duplicate elements in an unsorted n-array,
return the new array!

2) Remove the duplicate elements in a sorted n-array in-place,
return the new length!
'''

'''
ANS:
1)

a)
Without sorting,
- count the number of occurences for each element using a dict
- key idea: number of (k, v) pairs == length of new array
With sorting,
- implement an efficient sorting algo like quick or merge sort
- now, we can solve the original problem by implementing question 2)
=> remove repeated elements in-place, as per question 2)

2)

'''

'''
2) Sorted array as input, legnth of new array as output
Time: O(n), n is the 
Space: O(n)
'''
def removeDups4(arr):
    if (len(arr) <= 1):
        return len(arr)
    i, j = 1, 0
    while(i < len(arr)):
        if (arr[i] != arr[j]):
            j += 1
            arr[j] = arr[i]
        i += 1
    return j + 1


'''
1 a) Unsorted array as input
Time: O(n), n is the 
Space: O(n)
'''
def removeDups3(arr):
    arr.sort()                  # call to an efficient sort function
    if (len(arr) <= 1):
        return arr
    i, j = 0, 1
    while(i < len(arr) - 1 and j < len(arr)):
        if (arr[i] == arr[j]):
            arr.pop(j)
            continue
        else:
            i += 1
    return arr

'''
1 a) Unsorted array as input
Time: O(n) where n is the number of elements in the n-array
Space: O(n)
'''
def removeDups2(arr):
    _dict = {}
    for i in range(len(arr)):
        if (arr[i] not in _dict):
            _dict[arr[i]] = 1
        else:
            _dict[arr[i]] += 1

    arr = []
    for key in _dict: arr.append(key)

    return arr

'''
1 a) Unsorted array as input, variant.
Time: O(n) where n is the number of elements in the n-array
Space: O(n)
'''
def removeDups1(arr): 
    # values set to zero, all keys have a unique value, by default
    mp = {x : None for x in arr}
    
    _arr = []

    for key in mp: _arr.append(key)

    # obvious assertion
    # print(len(_arr) == len(mp))

    return _arr

print(removeDups1([1, 2, 5, 1, 7213,23,323, 2]))
print(removeDups2([1, 2, 5, 1, 7213,23,323, 2]))
print(removeDups4([1, 2, 5, 1, 7213,23,323, 2]))