class Solution():

    def __init__(self, haystack, needle):
        self.haystack = haystack
        self.needle = needle

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
        if (not self.needle or self.needle==self.haystack):
            return 0
        
        res = [] ; matchFound = False
        
        if (len(self.needle)>len(self.haystack)): return res

        for h in range(len(self.haystack)-len(self.needle)+1):
            new_h = h
            new_n = 0
            while (not matchFound):
                if (self.haystack[new_h] != self.needle[new_n]):
                    break
                new_h += 1
                new_n += 1
                if (new_n == len(self.needle)):
                    res.append(h)
                    res.append(h+new_n-1)
                    matchFound = True

        return res
      
obj = Solution('mississippi','issippi')
print(obj.needleInHaystackCustom())
