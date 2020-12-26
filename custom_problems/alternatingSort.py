def alternatingSort(a):
    b = []
    i = 0 ; j = len(a)-1
    j_turn = True
    while (i <= j):
        if (j_turn):
            b.append(a[i])
            i += 1
            j_turn = False
        else:
            b.append(a[j])
            j -= 1
            j_turn = True

    
    print(b)

alternatingSort([1,2,3,4,5,6,7,8])