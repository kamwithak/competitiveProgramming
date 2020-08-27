'''
PROBLEM STATEMENT:

Check Permutation:
Given two strings, write a method to decide if one is a permutation of the other.
'''

'''
ANS:

We can either sort the strings individually, and compare if the resulting strings are equivalent
Although not optimal, it is clean and easy to understand.
Or, we can count the number of occurences for each character, and check if that is equivalent
'''

'''
Time: O(n*log(n)), depending on sorting implementation. For ex) BubbleSort would be O(n^2)
Space: O(n), array
'''
def checkPermutation1(str1: str, str2: str) -> bool:
    if (len(str1) != len(str2)):
        return False
    # ~
    if (sorted(str1) == sorted(str2)):
        return True
    return False

#print(checkPermutation1("cba", "abc"))

'''
Time: O(n), using a hashtable for constant time look up
Space: O(n), atmost n key-value pairs
'''
def checkPermutation2(str1: str, str2: str) -> bool:
    if (len(str1) != len(str2)):
        return False
    # ~
    _dict1 = {} ; _dict2 = {}
    for char in str1: 
        if (char not in _dict1):
            _dict1[char] = 1
        else:
            _dict1[char] += 1
    for char in str2: 
        if (char not in _dict2):
            _dict2[char] = 1
        else:
            _dict2[char] += 1
    return _dict1 == _dict2
    
#print(checkPermutation2("cba", "cba"))
