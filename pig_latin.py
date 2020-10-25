'''
PROBLEM STATEMENT:
Design a program to take a word as an input, and then encode it into a Pig Latin.
'''

'''
DESIGN: UNFINISHED
'''

def toPigLatin(_str: str) -> str:
    vowels = ['a', 'e', 'i', 'o', 'u']
    firstLetter = _str[0]
    if (firstLetter in vowels):
        return f"{_str}way"
    return _str

print(toPigLatin("amina"))


