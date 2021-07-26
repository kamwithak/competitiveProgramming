class maximumSubArraySum:
	def __init__(self, arr):
		self.arr = arr
	
	def sort(self):
		for a in range(len(self.arr)-1):
			for b in range(a+1, len(self.arr)):
				if (self.arr[a] > self.arr[b]):
					self.arr[b], self.arr[a] = self.arr[a], self.arr[b]
		print(self.arr)

	"""
		[-2, 1, -3, 4, -1, 2, 1, -5, 4]
		Look at all possible triplets: i, j, k
		Compute sum for each, identify the max_sum using max()
	"""
	def cubicSolution(self):
		bestSum = 0
		for a in range(len(self.arr)):
			for b in range(a, len(self.arr)):
				curSum = 0
				for c in range(a, b+1):
					curSum += self.arr[c]
				bestSum = max(curSum, bestSum)
		print(self.arr)
		print("best sum: " + str(bestSum))
	
	"""
		[-2, 1, -3, 4, -1, 2, 1, -5, 4]
		Look at all possible tuples i, j
		Compute running sum for each pair i and j, identify the max_sum using max()
	"""
	def quadraticSolution(self):
		bestSum = 0
		for a in range(len(self.arr)):
			curSum = 0
			for b in range(a, len(self.arr)):
				curSum += self.arr[b]
				bestSum = max(curSum, bestSum)
		print(self.arr)
		print("best sum: " + str(bestSum))
	
	"""
	Kadanes Algorithm:
		[-2, 1, -3, 4, -1, 2, 1, -5, 4]
	"""
	def linearSolution(self):
		bestSum = 0 ; curSum = 0
		for a in range(len(self.arr)):
			curSum = max(self.arr[a], curSum+self.arr[a])
			bestSum = max(curSum, bestSum)
		print(self.arr)
		print("best sum: " + str(bestSum))

if __name__ == '__main__':
	obj = maximumSubArraySum([-1,2,4,-3,5,2,-5,2])
	# obj.linearSolution()
	obj.sort()