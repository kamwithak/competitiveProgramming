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

class Solution:
    
    def addBinary(self, a: str, b: str) -> str:
        
        if (a == b == '0'):
            return '0'
        
        def toBinary(num):
            arr = []
            while (num > 0):
                arr.append(num % 2)
                num = num // 2
            return "".join([str(elem) for elem in arr[::-1]])            
            
        base10 = int(a, 2) + int(b, 2)
        
        return toBinary(base10)
        