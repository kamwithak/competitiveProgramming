import sys

class FirstNonRepeatingCharacter():

    def __init__(self, aString):
        self.aString = aString
        self.size = len(aString)

    """

    aaabccdeeef => b
    abcbad => c
    asdfghasdfgh => None

    """
    def solutionA(self):
        _dict = {}
        _banned = set()

        for index, char in enumerate(self.aString):
            if (char not in _dict and char not in _banned):
                _dict[char] = index
            elif (char in _dict):
                _dict.pop(char)
                _banned.add(char)
    
        if not _dict:
            return None
        
        return self.aString[min(_dict.values())]

if __name__ == '__main__':
    obj = FirstNonRepeatingCharacter('aaabccdeeef')
    print(obj.solutionA())