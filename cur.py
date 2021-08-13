"""
Problem Statement:

A permutation can be specified by an array P,
where P[i] represents the location of the element at i in the permutation.

For example, [2, 1, 0] represents the permutation where elements at the index 0 and 2 are swapped.

Given an array and a permutation, apply the permutation to the array.

For example, given the array ["a", "b", "c"] and the permutation [2, 1, 0], return ["c", "b", "a"].
"""

def applyPermutationToArray(arr, perm):
    # NOT IN-PLACE:
    # masterArr = []
    # for i in perm:
    #     masterArr.append(arr[i])
    # return masterArr

    hashMapArr, hashMapPerm = {}, {}
    
    for i in range(len(arr)):
        hashMapArr[i] = arr[i]
    for key in hashMapArr:
        arr[key] = hashMapArr[perm[key]]

    return arr

print(applyPermutationToArray(['a', 'b', 'c'], [2,1,0]))
