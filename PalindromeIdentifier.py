class PalindromeIdentifier:
    def __init__(self, str):
        self.str = str

    def isPalindromeResursive(self, _str):
        return self.isPalindromeHelper(_str)

    def isPalindromeHelper(self, _str):
        index = len(_str)
        if (index == 0 or index == 1):
            return True
        
        if (_str[0] == _str[index - 1]):
            return self.isPalindromeHelper(_str[1:])
        
        return False

    def isPalindromeIterative(self):
        n = len(self.str)
        for i in range(int(n/2)):
            if (self.str[i] != self.str[n-i-1]):
                return False
        return True

if __name__ == "__main__":
    obj = PalindromeIdentifier("racecar")
    print(obj.isPalindromeResursive(obj.str))
