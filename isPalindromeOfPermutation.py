class isPalindromeOfPermutation():
    def __init__(self, inputString):
        self.inputString = inputString

    def solution(self):
        _set = set()

        for char in self.inputString:
            if (char not in _set):
                _set.add(char)
            else:
                _set.remove(char)

        _isPalindromeOfPermutation = len(_set) <= 1

        return _isPalindromeOfPermutation


        """
        inputString == 'racecar'            =>                {e}        
        inputString == 'dood'               =>                {}
        inputString == 'llllllllllll'       =>                {}
        """

obj = isPalindromeOfPermutation('llllllllllll')

print(obj.solution())
