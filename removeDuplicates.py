"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
"""

def removeDuplicatesInefficient1(nums):
  arr = []
  for elem in nums:
    if (elem not in arr):
      arr.append(elem)
  return arr

def removeDuplicatesInefficient2(nums):
  return list(set(nums))

def removeDuplicatesInefficient(nums):
  i = 0
  while i < len(nums)-1:
    if (nums[i] == nums[i+1]):
      del nums[i]
    else:
      i += 1
  return len(nums)

def removeDuplicates1(nums):
  n = len(nums)
  i = 0
  for j in range(1, n):
    if (nums[j] != nums[i]):
      i += 1
      nums[i] = nums[j]
  
  return nums

def removeDuplicates2(nums):
  size = len(nums)
  e = 0
  for i in range(1, size):
    if (nums[i-1-e] == nums[i-e]):
      nums.pop(i-1-e)
      e += 1
  return nums

print(removeDuplicates2([0,0,1,1,1,2,2,3,3,4]))

