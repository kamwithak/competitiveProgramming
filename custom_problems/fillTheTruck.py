"""
A Warehouse manager needs to create a shipment to fill a truck.
All the products in the warehouse are in boxes of the same size.

Each product is packed in some number of units per box. (where each unit is equal)

Write an algorithm to determine the maximum number of units of any mix of products that can be shipped.

Input:
i)   num: an integer representing the number of products
ii)  boxes: a list of integers where the ith element represents the number of available boxes
iii) unitSize: an integer representing size of unitsPerBox
iv)  unitsPerBox: a list of integers where the ith element represents the number of units packed in the ith box
v)   truckSize: an integer representing the number of boxes the truck can carry

Output:
Return an integer representing the maximum units that can be carried by truck.

Idea:
Since we want to maximize the number of units in all boxes, we can simply sort the boxes descending by the number of units that each box can hold
Iterating over the result, we compute the sum, left-to-right, until the truck is full.

"""

from typing import List

def fillTheTruck(num: int, boxes: List[int], unitSize: int, unitsPerBox: List[int], truckSize: int) -> int:
    result = 0
    boxesAvailable = truckSize
    arr = sorted([(unit, i) for i, unit in enumerate(unitsPerBox)], reverse=True)
    for unit, i in arr:
        if (boxes[i] < boxesAvailable):
            result += boxes[i] * unit
            boxesAvailable -= boxes[i]
        else:
            result += boxesAvailable * unit
            break
    return result

print(fillTheTruck(num=3,boxes=[1,2,3],unitSize=3,unitsPerBox=[3,2,1],truckSize=3))