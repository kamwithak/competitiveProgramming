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

obj = Solution()
print(obj.generate(3))

