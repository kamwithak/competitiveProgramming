'''
PROBLEM STATEMENT:

Implement an algorithm to delete a node in the middle (i.e., any node but
the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
that node
'''

'''
ANS:

IDEA: remove curNode by doing two things,
i) Set the curNode.data field to the nextNode.data field
ii) Set the curNode.next ptr to the nextNode.next ptr
'''

class Node():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
'''
Time: O(n)
Space: O(n)
'''
def removeNode(aNode: Node):
    aNode.data = aNode.next.data
    aNode.next = aNode.next.next
    return True                                                                    

def printNodes(head: Node):
    node = head
    while (node!=None):
        print(node.data)
        node = node.next

if __name__ == "__main__":
    head = Node(1,Node(2,Node(3,Node(4,Node(5,Node(6,Node(7)))))))
    removeNode(head.next.next)
    printNodes(head)