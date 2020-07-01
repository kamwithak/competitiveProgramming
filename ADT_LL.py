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
		while cur:										# O(n) - iterative implementation
			_str += str(cur.value) + ' -> '
			cur = cur.next
		_str += 'None'
		print(_str)

	def addToFront(self, newNode):						# O(1) - constant time	
		newNode.next = self.head
		self.head = newNode								# readjusting the head ptr
		self.curNumberOfNodes += 1

	def getHead(self):
		return self.head

	def getTail(self):
		return self.tail

	def getCurrentSizeOfLinkedList(self):
		return self.curNumberOfNodes

if __name__ == '__main__':
	obj = LinkedList(10)
	#obj.loadLinkedList(100)
	obj.printIteratively()
	print(obj.getHead().value)
	print(obj.getTail().value)