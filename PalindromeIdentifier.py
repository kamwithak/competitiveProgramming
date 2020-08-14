class PalindromeIdentifier:
    def __init__(self, str):
        self.str = str

    def isPalindromeResursive(self, _str):
        index = len(_str)
        if (index == 0 or index == 1):
            return True
        
        if (_str[0] == _str[index - 1]):
            return self.isPalindromeResursive(_str[1:])
        
        return False

    def isPalindromeIterative(self):
        n = len(self.str)
        for i in range(int(n/2)):
            if (self.str[i] != self.str[n-i-1]):
                return False
        return True
;
if __name__ == "__main__":
    _str = "racecar"
    obj = PalindromeIdentifier(_str)
    print(obj.isPalindromeIterative())
    print(obj.isPalindromeResursive(_str))
