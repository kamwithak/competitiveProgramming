class TwoSum:
	"""
	Given an array of integers arr and an integer target,
	return indices of the two numbers such that they add up to target.

	You may assume that each input would have exactly one solution,
	and you may not use the same element twice.
	"""
	def __init__(self, arr, k):
		self.arr = arr
		self.k = k

	"""
	Compute all pairs i and j for an n-element arr where i => [0, n-2] and j => [1, n-1]
	"""
	def bruteForce(self):
		for i in range(len(self.arr)-1):
			for j in range(i+1, len(self.arr)):
				if (self.arr[i] + self.arr[j] == self.k):
					return [i, j]
		return False


	"""
	Use dictionary: iterate over arr, populate dictionay with each element we come across
	if (arr[i] - k in _dict):
		return [i, j]
	"""
	def linear(self):
		_dict = {}
		for i in range(len(self.arr)):
			if (self.k-self.arr[i] in _dict):
				return [self.arr[self.k-self.arr[i]], i]
			_dict[self.arr[i]] = i
		return []