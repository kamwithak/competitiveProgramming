<<<<<<< HEAD
'''
PROBLEM STATEMENT:
~~~~~~~~~~~~~~~~~~
Design a program to take a word as an input, and then encode it into a Pig Latin.
'''

'''
DESIGN:
~~~~~~
if the first letter is a vowel:
    append 'way' to the end of the word and return that
otherwise:
    iterate over all chars that are not vowels, keep track on index
    slice where the first vowel is found, rearrange, and put back together
    append 'ay' to the end of the word and return that

'''

def toPigLatin(_str: str) -> str:
    vowels = ['a', 'e', 'i', 'o', 'u']
    firstLetter = _str[0]
    if (firstLetter in vowels):         # words that start with a vowel
        return f"{_str}yay"
    else:                               # words that start with a consonant
        index = 0
        for char in _str:
            if (char in vowels):
                break
            index += 1
        return f"{_str[index:]}{_str[:index]}ay"

print(toPigLatin("yello"))


=======
'''
PROBLEM STATEMENT:
~~~~~~~~~~~~~~~~~~
Design a program to take a word as an input, and then encode it into a Pig Latin.
'''

'''
DESIGN:
~~~~~~
if the first letter is a vowel:
    append 'way' to the end of the word and return that
otherwise:
    iterate over all chars that are not vowels, keep track on index
    slice where the first vowel is found, rearrange, and put back together
    append 'ay' to the end of the word and return that

'''

def toPigLatin(_str: str) -> str:
    vowels = ['a', 'e', 'i', 'o', 'u']
    firstLetter = _str[0]
    if (firstLetter in vowels):         # words that start with a vowel
        return f"{_str}yay"
    else:                               # words that start with a consonant
        index = 0
        for char in _str:
            if (char in vowels):
                break
            index += 1
        return f"{_str[index:]}{_str[:index]}ay"

print(toPigLatin("yello"))
>>>>>>> c87048f6d203a6448ef863b636a9fca7537a1dee
