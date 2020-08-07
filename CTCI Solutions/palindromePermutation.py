'''
PROBLEM STATEMENT:
Given a n-char string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards. A permutation
is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words. ie) spaces and numbers
'''

'''
ANS:
Clever algorithm here, we use a hash table to count how many times each char appears in a string.
Then, we iterate over the keys of the hashtable and ensure that no more than one char has an odd count.
This is how we determine if a palindrome exists:
WELL, we need an even number of almost all chars, s.t that half can be on one 'side', and the other half on the other 'side'
=> There must be no more than one char with an odd number of occurences => zero odd (all even) or one odd (n-1 even), but not more than that
Ex) R A C E  C A R, T A C O  O C A T 
'''

'''
Time: O(n)
Space: O(n)
'''
def palindromePermutation(str: str) -> bool:
    _dict = {}
    for i in range(len(str)):                               # count the number of occurences of each char in str                       
        if (str[i] != " "):
            if (str[i] not in _dict):
                _dict[str[i]] = 1
            else:
                _dict[str[i]] += 1
    # ~
    _numOdd = 0                                             # count the number of occurences with odd parity
    for key in _dict:    
        if (_dict[key] % 2 != 0):
            _numOdd += 1
    # ~

    return not _numOdd > 1                                  # true if number of occurences with odd parity <= 1

print(palindromePermutation("taco cat"))