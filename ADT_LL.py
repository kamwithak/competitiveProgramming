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

	def loadLinkedList2(self, tailValue):
		if tailValue == 0: return
		for num in range(2, tailValue+1):
			self.addToFront(Node(num))
		#if tailValue % 2 == 0:
		#else:

	def __str__(self, cur):								# O(n) - recursive implementation								
		print("yeeee")
		if cur != None:									# iterates through linked list starting at node 'cur'
			print(cur.value)
			self.__str__(cur.next)

	
	#def printIteratively(self):
		#cur = self.head
		#while cur:										# O(n) - iterative implementation
			#print(cur.value)
			#cur = cur.next

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
	
	#def addToEnd(self, cur, value):						# O(n) - recursive implementation
	#	if cur != None:
	#		self.addToEnd(cur.next, value)				# buggy,
	#	else:											# from here
	#		newNode = Node(value) ; lastNode = self.getLastNode()
	#		lastNode.next = newNode
	#		self.tail = newNode

#obj = LinkedList(Node(1), Node(5)) 						# head and tail nodes defined as args
#obj.head.next = Node(2, Node(3, Node(4, Node(5))))		# cur.next until tail node
#obj.addToFront(0)
#obj.addToEnd(obj.head, 10)
#obj.__str__(obj.head)
#print(obj.tail.value)

if __name__ == '__main__':
	obj = LinkedList(100)
	#obj.loadLinkedList(100)
	obj.__str__(obj.getHead())
	print(obj.getHead().value)
	print(obj.getTail().value)