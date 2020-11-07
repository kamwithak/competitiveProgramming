"""
Problem Statement:
Given two sorted arrays, of size m and n respectively, merge them into the same array while maintaining order.
BONUS: solve the problem in-place (nums1) where len(nums1) = m + n
"""

def mergeSortedArray(nums1: list, m: int, nums2: list, n: int):
    i = 0
    j = 0
    master_index = 0
    nums3 = [None] * (m + n) 

    while (i < m and j < n):
        if (nums1[i] < nums2[j]):
            nums3[master_index] = nums1[i]
            i += 1
        else:
            nums3[master_index] = nums2[j]
            j += 1
        master_index += 1
    
    while (i < m and master_index < m + n):
        nums3[master_index] = nums1[i]
        master_index += 1
        i += 1 

    while (j < n and master_index < m + n):
        nums3[master_index] = nums2[j]
        master_index += 1
        j += 1

    return nums3

def mergeSortedArrayInPlace(nums1: list, m: int, nums2: list, n: int):
    i = m - 1
    j = n - 1
    master_index = len(nums1) - 1

    while (master_index >= 0):
        if (i < 0):
            j -= 1
            nums1[master_index] = nums2[j]
        elif (j < 0):
            i -= 1
            nums1[master_index] = nums2[i]
        else:
            if (nums1[i] > nums2[j]):
                j -= 1
                nums1[master_index] = nums2[j]
            else:
                i -= 1
                nums1[master_index] = nums2[i]
        master_index -= 1

    return nums1

print(mergeSortedArray(nums1=[1,2,3], m=3, nums2=[1,2,5], n=3))