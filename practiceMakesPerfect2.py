from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        _master = []

        for i in range(numRows):
            aList = [1]
            for j in range(i):

                if (j == i - 1):
                    aList.append(1)

            _master.append(aList)    
        return _master

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        back, front = 0, 0
        
        for c in s:
            if (c == '('):
                back += 1
            elif (c == ')'):
                back -= 1
            
            if (back < 0):
                back = 0
                front += 1
                
        return back + front