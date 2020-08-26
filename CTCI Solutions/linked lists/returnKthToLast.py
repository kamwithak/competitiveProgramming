'''
PROBLEM STATEMENT:
Implement an algorithm to find the kth to last element of a singly linked list
'''

'''
ANS:
1) Length of LL is known: N = LL.size()

=> the kth to last element is the (N-k)th element
=> simply iterate over LL and return the (N-k)th node (index: N-k-1)

2) Length of LL is unknown

=> Recursion over the LL. When the calls are returning, the method passes back a ctr.
Each parent function call adds 1 to this ctr.
When the counter equals k, we know we have reached the (N-k)th element (index: N-k-1))
=> return as needed.

'''
class Node():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

'''
1)
Time: O(n)
Space: O(n)
'''
def kthToLast(head: Node, n: int, k: int) -> Node:
    node = head
    if (k<0):                               # edge cases
        for i in range(0, n):
            if (i == n-1):
                return node
            node = node.next
    elif (k>=n):
        return node

    for i in range(0, n-k):
        if (i == n-k-1):                    # on the last iteration,
            return node                     # return node at n-k-1 index
        node = node.next
    return None

if __name__ == "__main__":
    head = Node(1,Node(2,Node(3,Node(4,Node(5,Node(6,Node(7)))))))
    print(kthToLast(head, 7, 0).data)
    print(kthToLast(head, 7, 6).data)

