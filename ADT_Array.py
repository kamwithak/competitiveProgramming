class Array:								# ADT ~ Array of {key, value} arrays
	def __init__(self):
		self.array = []

	# O(n) ~ linear time, inefficient, we can do better ;)

	def printRelation(self):
		for pair in self.array:					# print each (key, value) pair
			print(pair)

	def alreadyExists(self, key):
		for pair in self.array:
			if pair[0] == key:
				return True
		return False

	def insert(self, key, value):
		if not self.alreadyExists(key):				# check to see if key isn't already in array
			return self.array.append((key, value))		# if true, add (key, value) pair to end of array

	def remove(self, key):
		for pair in self.array:					# iterate linearly
			if pair[0] == key:				# find arg key at some index, call that index i
				return self.array.remove(pair)		# remove (key, value) pair @ index i
		return 'Pair does not exist'

	def update(self, key, value):
		for pair in self.array:
			if pair[0] == key:
				self.array.remove(pair)
				return self.array.append((key, value))
		return 'Key does not exist'

arr = Array()
arr.insert(0,'a')
arr.insert(1,'b')
arr.insert(2,'c')
arr.insert(3,'d')
arr.remove(3)
arr.printRelation()

