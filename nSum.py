"""
You are given an array of n integers and a number k. Determine whether there is a pair
of elements in the array that sums to exactly k. For example, given the array [1, 3, 7] and
k = 8, the answer is “yes,” but given k = 6 the answer is “no.”

Ex)
---------------------------------------------------------------------------------------------
arr = [1, 3, 7] ; k = 8
=> 1 + 7 == 8 => return [0, 2] => return "yes"

arr = [1, 3, 7] ; k = 6
=> return "no"
---------------------------------------------------------------------------------------------
Time: O(n^2) where n is len(arr)
Space: O(1)
- bruteforce look at all pairs

Time: O(n) - one pass
Space: O(n) - hashmap (take advantage of the constant time look up that dict gives us)
- hashmap

Extended: consider threeSum variant....
Time: O(n^3) where n is len(arr)
Space: O(1)
- bruteforce look at all pairs

Time: O(n^2) - quadratic
Space: O(n) - hashmap (take advantage of the constant time look up that dict gives us)
- hashmap

"""

from typing import List

class Solution:
	
	def slowTwoSum(self, nums: List[int], target: int) -> List[int]:
		for i in range(0, len(nums)-1):
			for j in range(i+1, len(nums)):
				if (target == nums[i] + nums[j]):
					return [i, j]
		return []
	
	def fastTwoSumUnordered(self, nums: List[int], target: int) -> List[int]:		# assumes unordered input
		_dict = {}																	# init dict
		for i in range(0, len(nums)):												# iterate over array and add num[i] to map
			comp = target - nums[i]													# compute complement
			if (comp in _dict):														# if complement has been cached, return it
				return [_dict[comp], i]
			_dict[nums[i]] = i
		return False

	def fastTwoSumOrdered(self, nums: List[int], target: int) -> List[int]:		# assumes ordered input
		l, r = 0, len(nums)-1
		while (l<r):
			curSum = nums[l] + nums[r]
			if (curSum > target):												# we desire a smaller sum
				r -= 1
			elif (curSum < target):												# we desire a larger sum
				l += 1
			else:
				return [l, r] 

	def slowThreeSum(self, nums: List[int], target: int) -> List[int]:
		for i in range(0, len(nums)-2):
			for j in range(i+1, len(nums)-1):
				for k in range(j+1, len(nums)):
					if (target == nums[i] + nums[j] + nums[k]):
						return [i, j, k]
		return []

	def fastThreeSumUnsorted(self, nums: List[int], target: int) -> List[int]:
		# We can reduce 3SUM to 2SUM: a + b + c = k => a + b = k - c = l
		arr = []
		nums.sort()																		# efficient sort
		for c in range(1, len(nums)-2):
			if (c == 0 or (c > 0 and nums[c] != nums[c-1])):
				l, r = c+1, len(nums)-1
				while (l<r):
					curSum = nums[l] + nums[r] + nums[c]
					if (curSum < target):												# we desire a smaller sum
						l += 1
					elif (curSum > target):												# we desire a larger sum
						r -= 1
					else:
						arr.append([nums[c], nums[l], nums[r]])
						while (l < r and nums[l] == nums[l+1]): l+=1
						while (l < r and nums[r] == nums[r-1]): r-=1
						l+=1
						r-=1
		return arr


obj = Solution()
print(obj.fastThreeSumUnsorted([-1,0,1,2,-1,-4], 0))