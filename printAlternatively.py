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

"""

Given two arrays, print each element alternatively

For example)

arr1 = [a,b,c,d]

arr2 = [e,f,g,h,i,j,k]

=> a e b f c g d h i j k

"""

class Solution():
  def __init__(self, arr1, arr2):
    self.arr1 = arr1
    self.arr2 = arr2
    self.n = len(self.arr1)
    self.m = len(self.arr2)

  def print_lists(self):
    i, j = 0, 0
    config = True
    while(i < self.n and j < self.m):
      if (config):
        print(self.arr1[i])
        i += 1
        config = False
      else:
        print(self.arr2[j])
        j += 1
        config = True

    while (i < self.n):
      print(self.arr1[i])
      i += 1

    while (j < self.m):
      print(self.arr2[j])
      j += 1

obj = Solution(['a', 'b', 'c', 'd'], ['e','f','g','h','i','j','k'])
obj.print_lists()

