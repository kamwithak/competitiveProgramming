"""
Problem 1:
You are given a singly Linked List, return a deep copy of the list.
"""



# Definition for a Node.
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def addToList(newNode: Node):
    
    newNode.next

def makeDeepCopy(aList):
    prevNode = Node(aList.data)
    nextNode = aList.next
    while (nextNode != None):
        nextNextNode = nextNode.next
        nextNode.next = prevNode
        prevNode = nextNode
        nextNode = nextNextNode
    return prevNode
    

aList = Node(1,Node(2,Node(3,Node(4))))

curNode = aList
while (curNode != None):
    print(curNode.data)
    curNode = curNode.next

print("asda")
anotherList = makeDeepCopy(aList)

curNode = anotherList
while (curNode != None):
    print(curNode.data)
    curNode = curNode.next

