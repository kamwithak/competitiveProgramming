class Solution():

    def __init__(self, needle, haystack):
        self.needle = needle
        self.haystack = haystack

    def needleInHaystackPythonic(self):
        idx = self.haystack.find(self.needle)
        return idx, idx + len(self.needle) - 1
    
    def needleInHaystackCustom(self):
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
                if (self.haystack[newH] != self.needle[newN]):
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
