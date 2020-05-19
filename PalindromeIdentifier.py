class PalindromeIdentifier:
    def __init__(self, str):
        self.str = str

    def isPalindrome(self):
        n = len(self.str)
        for i in range(int(n/2)):
            if (self.str[i] != self.str[n-i-1]):
                return False
        return True

if __name__ == "__main__":
    obj = PalindromeIdentifier("racecar")
    print(obj.isPalindrome())
