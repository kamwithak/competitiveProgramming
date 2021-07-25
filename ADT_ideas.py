class Node(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'Node with data={self.val}'

import random

def createRandomLinkedList(numberOfNodes=10):
    
    head = None

    for i in range(numberOfNodes):
        randomValue = random.randint(0, 10)
        newNode = Node(val=randomValue)
        newNode.next = head
        head = newNode

    return head


def reverseLinkedList(head):
    prevNode = None
    curNode = head

    while (curNode):
        nextNode = curNode.next
        curNode.next = prevNode
        prevNode = curNode
        curNode = nextNode

    head = prevNode

    return head
    

def printLinkedList(head):
    curNode = head

    traversal = []
    while (curNode):
        # print(curNode.val)
        traversal.append(curNode.val)
        print(repr(curNode))
        curNode = curNode.next

    return traversal

if __name__ == '__main__':
    # print(Node(val=10, next=None).val)
    # print(Node(val=10, next=None).next)

    head = createRandomLinkedList(10)
    print(printLinkedList(head))
    print('reversing')
    newHead = reverseLinkedList(head)
    print(printLinkedList(newHead))

