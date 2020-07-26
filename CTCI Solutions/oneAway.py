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
    ctr = 0
    for i in range(len(str1)):
        if (str1[i] != str2[i]):
            ctr += 1
    return ctr <= 1

def oneEditInsert(str1: str, str2: str) -> bool:
    pass
