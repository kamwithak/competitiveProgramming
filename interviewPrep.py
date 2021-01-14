def reverse(aString):
    aList = [c for c in aString]
    i = 0
    j = len(aString)-1

    while (i <= j):
        aList[i], aList[j] = aList[j], aList[i]

        i+=1
        j-=1

    return ''.join(aList)
# print(reverse('kamran'))


def findMissing(aList, aListMissingOne):
    """
    Ex)
    Given aList := [4,12,9,5,6] and aListMissingOne := [4,9,12,6]
    Find the missing element
    Return 5
    
    IDEA: 

    """
    n = len(aList)
    m = len(aListMissingOne)

    for i in range(n):
        for j in range(m):
            if (aList[i] == aListMissingOne[j]): break
            if (j == m-1): return aList[i]

    return 'lists are permutations of each other'

print(findMissing([4,5,12,9,6],[4,9,12,6]))
