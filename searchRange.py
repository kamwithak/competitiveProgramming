from typing import List

class Solution:
    """
    Problem Statement:
    Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
    If target is not found in the array, return [-1, -1].
    """

    def searchRangeFaster(self, nums: List[int], target: int) -> List[int]:
        pass

    def searchRangeLinear(self, nums: List[int], target: int) -> List[int]:
        """
        Args:
            nums (List[int]): sorted list of int-type numbers
            target (int): target int we are looking for in nums

        Returns:
            List[int]: pair for starting and ending index
        
        Time: O(n)
        Space: O(n)
        """
        res, n, targetFound = [], len(nums), False
        for i in range(n):
            if (nums[i] == target and not targetFound):
                res.append(i)
                targetFound = True
            elif (nums[i] != target and targetFound):
                res.append(i-1)
                targetFound = False
            elif (i == n-1 and targetFound):
                res.append(i)
                targetFound = False
        if (not res): res.append(-1) ; res.append(-1)
        elif (len(res) == 1): res.append(res[0])
        return res

obj = Solution()
print(obj.searchRangeLinear([1,2,4,4,4,5,5,9,9,11,11,11,11,12,12], 12))