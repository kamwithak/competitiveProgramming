'''
PROBLEM STATEMENT:
Write a method to replace all spaces in a string with '%20'. You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string.
'''

'''
ANS:
Split the string using whitespace, resutling array.
Iterate over array and check if the element is NOT an empty string left from trailing spaces,
If that is the case, then append what we need to our resulting string, Clean up before returning.
'''

'''
Time: O(n), where n is len(arr)
Space: O(n)
'''
def URLify(str1: str, trueLength: int) -> str:
    ans = ''
    arr = str1.split(' ')
    for i in range(len(arr)):
        if (arr[i] != ''): 
            ans += arr[i] + '%20'
    return ans[:-3]

print(URLify("hello hey   ", 7))