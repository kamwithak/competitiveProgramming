'''
PROBLEM STATEMENT:

Write code to remove duplicates from an unsorted linked list.

3 -> 243 -> 23 -> 123 -> 2 -> 1 -> None

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
  while (node.next != None):
    if node.data in nodes.keys():
      node.data = node.next.data
      node.next = node.next.next
    else:
      nodes[node.data] = True
      node = node.next
  return head

def printNodes(head):
  node = head
  while (node != None):
    print(node.data)
    node = node.next

if __name__ == "__main__":
  head = Node(1,Node(2,Node(4,Node(4,Node(5,Node(4,Node(4)))))))
  print("before:")
  printNodes(head)
  removeDups(head)
  print("after:")
  printNodes(head)