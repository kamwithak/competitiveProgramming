class Node:
	def __init__(self, value, next=None):
		self.value = str(value)
		self.next = next

class LinkedList:
	def __init__(self, size=1, head=Node(1)):
		self.head = head	
		self.tail = self.head
		self.curNumberOfNodes = 1
		self.loadLinkedList(size)

	def loadLinkedList(self, tailValue):
		if tailValue == 0: return
		for num in range(2, tailValue+1):
			self.addToFront(Node(num))
	
	def printIteratively(self):
		cur = self.head
		_str = ''
		while cur:								 # O(n) - iterative
			_str += str(cur.value) + ' -> '
			cur = cur.next
		if cur is None: _str += 'None'
		print('LinkedList: ' + _str)

	def reverse(self):
		cur = self.head
		prev = None
		while cur:
			next_node = cur.next
			cur.next = prev
			prev = cur
			cur = next_node
		self.tail = self.head
		self.head = prev

	def addToFront(self, new_node):				# O(1) - constant time	
		new_node.next = self.head
		self.head = new_node
		self.curNumberOfNodes += 1

	def getHead(self):
		return self.head

	def getTail(self):
		return self.tail

	def getCurrentSizeOfLinkedList(self):
		return self.curNumberOfNodes

if __name__ == '__main__':
	obj = LinkedList(10)

	obj.printIteratively()
	print("Head: " + obj.getHead().value)
	print("Tail: " + obj.getTail().value)

	print("Reverse operation...")
	obj.reverse()

	obj.printIteratively()
	print("Head: " + obj.getHead().value)
	print("Tail: " + obj.getTail().value)