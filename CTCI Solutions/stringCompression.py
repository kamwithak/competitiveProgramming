'''
PROBLEM STATEMENT:
String Compression: Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).
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