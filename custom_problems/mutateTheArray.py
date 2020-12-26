def mutateTheArray(n, a):
    newList = []
    first = third = 0
    for i in range(0, n):
        if (i == 0):
            first = 0
        else:
            first = a[i-1]
        if (i+1 == n):
            third = 0
        else:
            third = a[i+1]
        newList.append(first+a[i]+third)

    print(newList)

mutateTheArray(5,[4,0,1,-2,3])