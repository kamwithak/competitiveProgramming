"""
PROBLEM STATEMENT:

Given an array (arr) as an argument complete the function countSmiley
that should return the total number of smiling faces.

Rules for a smiling face:

Each smiley face must contain a valid pair of eyes.

Eyes can be marked as : or ;

A smiley face can have a nose but it does not have to.
Valid characters for a nose are - or ~

Every smiling face must have a smiling mouth that 
should be marked with either ) or D but not both
"""

"""
ANS:

1) Trivial bruteforce

2) Custom strategy

2) Use Regular expressions!

https://stackoverflow.com/questions/43513509/count-the-smiley-faces-in-an-array

"""

"""
Time: O(len(arr) * len(possibleOptions))
Space: linear time
"""
def countSmiley1(arr):
    possibleOptions = [":)",";)",":-)",";-)",";~)",":~)",":D",";D",":-D",":~D",";-D",";~D"]
    ctr = 0
    for option in arr:
        if (option in possibleOptions):
            ctr += 1
    return ctr

"""
Time: O(len(arr))
Space: linear time
"""
def countSmiley2(arr):
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def validSmileWithThreeCharacters(eyes, noseOrMouth, mouth):
        x = (eyes == ':' or eyes == ';')
        y = (noseOrMouth == '-' or noseOrMouth == '~')
        z = (mouth == ')' or mouth == 'D')
        return x and y and z

    def validSmileWithTwoCharacters(eyes, noseOrMouth):
        x = (eyes == ':' or eyes == ';')
        y = (noseOrMouth == ')' or noseOrMouth == 'D')
        return x and y
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ctr = 0
    for smile in arr:
        eyes = smile[0]
        noseOrMouth = smile[1]
        if (len(smile) == 3):
            mouth = smile[2]
            if (validSmileWithThreeCharacters(eyes, noseOrMouth, mouth)):
                ctr += 1
        elif (len(smile) == 2):
            if (validSmileWithTwoCharacters(eyes, noseOrMouth)):
                ctr += 1
    return ctr

"""
REGEX!
"""
import re
def countSmiley3(arr):
    text = ''
    for elem in arr:
        text+=elem
    return len(re.findall('[:;][-~]?[)D]', text))

print(countSmiley2([":)",";)",";~D"]))
