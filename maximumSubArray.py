class maximumSubArraySum:
	def __init__(self, arr):
		self.arr = arr

	def bubbleSort(self):
		for a in range(len(self.arr)):
			for b in range(a, len(self.arr)):
				if (self.arr[a] > self.arr[b]):
					self.arr[b], self.arr[a] = self.arr[a], self.arr[b]
		print(self.arr)

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
	
	def quadraticSolution(self):
		bestSum = 0
		for a in range(len(self.arr)):
			curSum = 0
			for b in range(a, len(self.arr)):
				curSum += self.arr[b]
				bestSum = max(curSum, bestSum)
		print(self.arr)
		print("best sum: " + str(bestSum))
	
	def linearSolution(self):
		bestSum = 0 ; curSum = 0
		for a in range(len(self.arr)):
			curSum = max(self.arr[a], curSum+self.arr[a])
			bestSum = max(curSum, bestSum)
		print(self.arr)
		print("best sum: " + str(bestSum))

if __name__ == '__main__':
	obj = maximumSubArraySum([-1,2,4,-3,5,2,-5,2])
	obj.quadraticSolution()