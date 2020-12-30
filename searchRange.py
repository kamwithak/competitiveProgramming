from typing import List

class Solution:
    """
    Problem Statement:
    Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
    If target is not found in the array, return [-1, -1].
    """
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res, targetFound = [], False
        for i in range(len(nums)):
            if (nums[i] == target and not targetFound):
                res.append(i)
                targetFound = True
            elif (nums[i] != target and targetFound):
                res.append(i-1)
                targetFound = False
            elif (i == len(nums)-1 and targetFound):
                res.append(i)
                targetFound = False
        if (not res): res.append(-1) ; res.append(-1)
        elif (len(res) == 1): res.append(res[0])
        return res

obj = Solution()
print(obj.searchRange([1,2,4,4,4,5,5,9,9,11,11,11,11,12,12], 11))