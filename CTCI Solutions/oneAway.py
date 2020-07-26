'''
PROBLEM STATEMENT:
There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character.
Given two strings, write a function to check if they are one edit (or zero edits) away.
'''

'''
ANS:
We can ignore directly checking the strings for one of the three edits. Instead, the lengths of the strings will tell us
exactly which one of the three edits should be checked.
'''

'''
Time: O(n)
Space: O(n)
'''
def oneAway(str1: str, str2: str) -> bool:
    if (len(str1) == len(str2)):        # replace a char in str1 to get str2
        pass
    if (len(str1) < len(str2)):         # insert a char in str1 to get str2
        pass    
    if (len(str1) > len(str2)):         # insert a char in str2 to get str1 
        pass
    return False
