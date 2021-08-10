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


    def solutionB(self):
        _dict = {}

        for char in self.aString:
            if (char not in _dict):
                _dict[char] = 1
            else:
                _dict[char] += 1

        """
            {a:3,b:1,c:2,d:1,e:3,f:1}
        """  

        for char in self.aString
            if (_dict[char] == 1):
                return char
        
        return None
          

if __name__ == '__main__':

    for word in ['aaabccdeeef', 'abcbad', 'asdfghasdfgh']:
        obj = FirstNonRepeatingCharacter(word)
        print(obj.solutionA() == obj.solutionB())
