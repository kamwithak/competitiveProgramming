'''
PROBLEM STATEMENT:

Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures? ...
'''

'''
ANS:

Depends on encoding method, ASCII (128 bit or 256 bit charcter mapping?), or Unicode (UTF-8/16/32)
We can assume Extended ASCII with 256 possible characters
=> str CANNOT have greater length than 256 characters, without having the same chars repeat
=> Create array of boolean flags, iterate over string, check the ascii encoding to map the associated number as an index with a bool
=> set value to True everytime we iterate over char, if we iterate again over same char, break loop, we know it isn't unique!
'''

'''
Time: O(n), where n is len(str)
Space: O(n), list
'''
def isUnique1(str: str) -> bool:
    if (len(str) > 256): return False
    flag_arr = [False] * 256
    for i in str:
        index = ord(i)
        if (flag_arr[index]): return False
        flag_arr[index] = True 
    return True

'''
Time: O(n), where n is len(str)
Space: O(n), dict
'''
def isUnique2(str: str) -> bool:
    _dict = {}
    for i in range(len(str)):
        if (str[i] not in _dict):
            _dict[str[i]] = 1
        else:
            _dict[str[i]] += 1
    for j in _dict:
        if (_dict[j] > 1): return False
    return True