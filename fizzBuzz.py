class fizzBuzz():
    def __init__(self, n):
        self.n = n
    
    def solutionA(self):
        ans = []
        for i in range(self.n):
            if (i % 3 == 0 and i % 5 == 0):
                ans.append('fizzbuzz')
            elif (i % 3 == 0):
                ans.append('fizz')
            elif (i % 5 == 0):
                ans.append('buzz')
            else:
                ans.append(i)
        return ans

    def solutionB(self):
        ans = []
        for i in range(self.n):
            if (i % 3 == 0):
                if (i % 5 == 0):
                    ans.append('fizzbuzz')
                else:
                    ans.append('fizz')
            elif (i % 5 == 0):
                ans.append('buzz')
            else:
                ans.append(i)
        return ans

obj = fizzBuzz(4)
resA = obj.solutionA()
resB = obj.solutionB()

for i in range(len(resA)):
    if (resA[i] != resB[i]):
        print("discrepency")

print("both solutions are admissable and equivalent")