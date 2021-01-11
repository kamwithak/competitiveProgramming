class Solution():

	def __init__(self, A, B):
		self.A = A
		self.B = B

	def printAlternativelySameSize(self):
		"""
		Assumes that len(self.A) == len(self.B) != 0
		Alternatively print each element in the two Lists
		"""
		if (len(self.A) != len(self.B)):
			raise Exception("the two lists must be of same length")
		if (len(self.A) == len(self.B) == 0):
			raise Exception("Empty lists")
		#	
		ptrA = 0 ; ptrB = 0 ; decisionPoint = False
		while (ptrA < len(self.A) or ptrB < len(self.B)):
			if (not decisionPoint):
				print(self.A[ptrA])
				ptrA+=1
				decisionPoint = True
			else:
				print(self.B[ptrB])
				ptrB+=1
				decisionPoint = False

	def printAlternativelyDifferentSize(self):
		"""
		Alternatively print each element in the two Lists, regardless of List size
		"""
		ptrA = 0 ; ptrB = 0 ; decisionPoint = False
		while (ptrA < len(self.A) and ptrB < len(self.B)):
    			if (not decisionPoint):
				print(self.A[ptrA])
				ptrA+=1
				decisionPoint = True
			else:
				print(self.B[ptrB])
				ptrB+=1
				decisionPoint = False

		while (ptrA < len(self.A)):
    			print(self.A[ptrA])
			ptrA += 1

		while (ptrB < len(self.B)):
			print(self.B[ptrB])
			ptrB += 1

obj = Solution(A=[3,2,1], B=[3,2,1])
obj.printAlternativelySameSize()


