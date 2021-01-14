def reverse(aString):
    aList = [c for c in aString]
    i = 0
    j = len(aString)-1

    while (i <= j):
        aList[i], aList[j] = aList[j], aList[i]

        i+=1
        j-=1

    return ''.join(aList)
# print(reverse('asd'))

def findMissing(aList, aListMissingOne):
    """
    Ex)
    Given aList := [4,12,9,5,6] and aListMissingOne := [4,9,12,6]
    Find the missing element
    Return 5
    
    IDEA: 
    Brute force! Examine all tuples.
    Time: O(n*m) and Space: O(1)

    Smarter: Use a hashMap, instead!
    Time: O(n+m) and Space: O(m)
    """

    assert len(aList)-len(aListMissingOne) == 1

    # n = len(aList)
    # m = len(aListMissingOne)

    # for i in range(n):
    #     for j in range(m):
    #         if (aList[i] == aListMissingOne[j]): break
    #         if (j == m-1): return aList[i]

    _dict = {}
    for i in range(len(aListMissingOne)):                       # O(len(aListMissingOne) + len(aList))
        _dict[aListMissingOne[i]] = aListMissingOne[i]
    for j in range(len(aList)):
        if (aList[j] not in _dict): return aList[j]

    return 'lists are permutations of each other'

print(findMissing([4,12,9,6],[4,9,12]))
