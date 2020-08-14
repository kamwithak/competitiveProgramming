'''
PROBLEM STATEMENT:
Remove the duplicate elements in an unsorted array!
'''

'''
ANS:

'''

'''
Time:
Space:
'''

def removeDups(arr): 
    # mp = {}
    # for x in arr:
    #     mp[x] = 0
    mp = {x : 0 for x in arr}               # values set to zero, by default, in map

    for key in arr:                         # for each key in arr
        if mp[key] == 0:                    # check if associatd value is equiv. to zero
            print(key, end = " ") 
            mp[key] = 1                     # if it is, then set the associatd value to one

removeDups([ 1, 2, 5, 1, 7, 2, 4, 2 ]) 

  