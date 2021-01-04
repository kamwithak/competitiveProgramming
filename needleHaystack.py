class Solution():

    def __init__(self, needle, haystack):
        self.needle = needle
        self.haystack = haystack

    def needleInHaystack(self):
        """
        Given two strings, needle and haystack:
        Find the starting and ending index of needle in haystack
        Ex) 'hello' & 'abchellodef' => [3, 7]
        
        Analysis:
        Time: O(mn) where m is H_SIZE and n is N_SIZE
        Space: O(1)

        """
        res, matchFound = [], False
        H_SIZE, N_SIZE = len(self.haystack), len(self.needle)
        
        for ptrH in range(H_SIZE):
            newH = ptrH
            newN = 0
            while (not matchFound):
                if (self.needle[newN] != self.haystack[newH]):
                    break

                newH += 1
                newN += 1

                if (newN == N_SIZE):
                    res.append(ptrH)
                    res.append(newH-1)
                    matchFound = True

        return res



obj = Solution('hello','abchellodef')
print(obj.needleInHaystack())