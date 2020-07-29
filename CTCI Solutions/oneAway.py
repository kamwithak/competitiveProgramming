'''
PROBLEM STATEMENT:
There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character.
Given two strings, write a function to check if they are one edit (or zero edits) away.
'''

'''
ANS:
We can ignore bruteforcing the edits for all possible charcters, to see if we can 'create' str2.
Instead, the lengths of the strings will tell us
exactly which one of the three edits should be checked.
'''

'''
Time: O(n)
Space: O(n)
'''
def oneAway(str1: str, str2: str) -> bool:
    if (len(str1) == len(str2)):                        # replace a char in str1 to get str2
        return oneEditReplace(str1, str2)
    if (len(str1) < len(str2)):                         # insert a char in str1 to get str2
        return oneEditInsert(str1, str2)   
    if (len(str1) > len(str2)):                         # insert a char in str2 to get str1 
        return oneEditInsert(str2, str1)   
    return False

def oneEditReplace(str1: str, str2: str) -> bool:
    found = False
    for i in range(len(str1)):
        if (str1[i] != str2[i]):
            if (found):
                return False
            found = not found
    return True

def oneEditInsert(str1: str, str2: str) -> bool:
    edited = False
    i = 0
    j = 0
    while (i < len(str1) and j < len(str2)):
        if (str1[i] != str2[j]):
            if (edited):
                return False
            edited = True
            j += 1
        else:
            i += 1
            j += 1
    return True

#print(oneEditReplace("abc", "ade"))
#print(oneEditInsert("a", "abc"))

import unittest
class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False)
    ]

    def test_oneAway(self):
        for [test_s1, test_s2, expected] in self.data:
            actual = oneAway(test_s1, test_s2)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()