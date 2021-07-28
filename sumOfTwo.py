"""

A = []

B = []

find a number i in A and another number j in B s.t i + j = v. 


BruteForce: Inefficent - O(n^2)

    For elem_i in A:
        For elem_j in B:
            if (indicies are different and elem_i == elem_j):
                return True
    return False

Can we do better?

HashSet: Efficient - O(A.size + B.size)
    declare set

    iterate over each elem_i in A
        store v - elem_i in set
    
    iterate ove each elem_j in B:
        if (set.contains(elem_j)):
            return True
    
    return False 


=> v - A = B => v - B = A 
=> v = A + B

"""

def sumOfTwo(A, B, v):
    cache = set()

    for elem in A:
        cache.add(v-elem)
    
    for elem in B:
        if (elem in cache):
            return True

    return False


def _sumOfTwo(A, B, v):
    cache = set()

    for elem in B:
        cache.add(elem)

    for elem in A:
        if (v-elem in cache):
            return True
    
    return False

print(_sumOfTwo([1,2,3,4],[6,4,3,2], 11))


