'''
PROBLEM STATEMENT:
Write code to remove duplicates from an unsorted linked list.

3 -> 243 -> 23 -> 123 -> 2 -> 1 -> None

'''

'''
ANS:

'''

class Node():
  def __init__(self, data=None, next=None):
    self.data = data
    self.next = next

'''
Time: O(n), n is the number of nodes in the Linked List
Space: O(n)
'''
def removeDups(head) -> Node:
  nodes = {}
  node = head
  while (node != None):
    if node.data in nodes.keys():
      node.data = node.next.data
      node.next = node.next.next
    else:
      nodes[node.data] = 1
      node = node.next
  return head

def printNodes(head):
  node = head
  while (node != None):
    print(node.data)
    node = node.next

if __name__ == "__main__":
  head = Node(1,Node(3,Node(3,Node(1,Node(5)))))
  print("before:")
  printNodes(head)
  removeDups(head)
  print("after:")
  printNodes(head)