class Solution():

    def __init__(self, needle, haystack):
        self.needle = needle
        self.haystack = haystack

    def needleInHaystack(self):
        """
        Given two strings, needle and haystack:
        find the starting and ending index of needle in haystack
        Ex) 'hello' & 'abchellodef' => [3, 7]
        """
        res = []
        H_SIZE, N_SIZE = len(self.haystack), len(self.needle)
        ptrN, ptrH, matchFound = 0, 0, False
        
        while (ptrH < H_SIZE and not matchFound):
            newH = ptrH
            newN = ptrN
            while (not matchFound):
                if (self.needle[newN] != self.haystack[newH]):
                    break

                newH += 1
                newN += 1

                if (newN == N_SIZE):
                    res.append(ptrH)
                    res.append(newH-1)
                    matchFound = True

            ptrH += 1
        return res



obj = Solution('kam','iiikamksiii')
print(obj.needleInHaystack())