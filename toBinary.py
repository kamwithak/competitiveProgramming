class toBinary:
    def __init__(self, binaryArr=[]):
        self.binaryArr = binaryArr

    def conversionRecursive(self, n):
        if (n > 0):
            self.conversionRecursive(int(n / 2))
            self.binaryArr.append(n % 2)
    
    def conversionIterative(self, n):
        while (n > 0):
            r = n % 2
            self.binaryArr.append(r)
            n = n // 2
        self.binaryArr = self.binaryArr[::-1]
    
    def getBinaryArr(self):
        return self.binaryArr

obj = toBinary()
obj.conversionRecursive(16)
print(obj.getBinaryArr())