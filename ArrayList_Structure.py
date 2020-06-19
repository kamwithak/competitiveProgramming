class ArrayList:
	def __init__(self, arr):
		self.arr = arr
		self.size = len(arr)

	# print array at any given instant
	def printArr(self):
		print(self.arr)

	# return length of input array
	def getSize(self):
		return self.size

	# append to the end of the array
	def appendToArray(self, e):
		self.arr.append(e)
		self.size += 1

	# get array value at index i
	def getAtIndex(self, i):
		try:
			return self.arr[i]
		except IndexError:
			raise Exception("index out of bounds")

	# array[i] <- e // print
	def setAtIndex(self, i, e):
		try:
			self.arr[i] = e
		except IndexError:
			raise Exception("index out of bounds")
		
	# array[i] <- e where the values at indicies [i,size(array)-1] are shifted to the next index
	def addAtIndex(self, i, e):
		try:
			q = self.getSize() - 1
			while q > i:
				self.arr[q] = self.arr[q-1]
				q -= 1
			self.arr[i] = e
		except IndexError:
			raise Exception("index out of bounds")
			
	# array[i] <- NULL where the values at indicies [i,size(array)-1] are shifted to the previous index
	def removeAtIndex(self, i):
		try:
			self.arr[i] = None
			q = self.getSize() - 1
			while q > i:
				self.arr[q-1] = self.arr[q]
				q -= 1
		except IndexError:
			raise Exception("index out of bounds")

if __name__ == '__main__':

	arr = ArrayList(['a','b','c','d','e','f','g','h','i','j','k'])
	arr.printArr()
	print('size of array is ' + str(arr.getSize()))

	#print(arr.getAtIndex(1))

	arr.setAtIndex(1, 'kamran')
	#arr.printArr()

	arr.addAtIndex(0, 'abc')
	#arr.appendToArray('kam')

	arr.printArr()






