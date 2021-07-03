class LSWRC():
    def __init__(self, inputString):
        self.inputString = inputString
    
    def solution(self):
        """
            abcabcbb
        """
        _set = set()
        res = 0
        l = 0

        for r in range(len(self.inputString)):
            while self.inputString[r] in _set:
                _set.remove(self.inputString[l])
                l += 1 
            _set.add(self.inputString[r])
            res = max(res, r-l+1)
        return res

obj = LSWRC('abcabcbb')
print(obj.solution())