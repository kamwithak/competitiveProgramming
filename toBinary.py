class toBinary:
    def __init__(self, binaryArr=[]):
        self.binaryArr = binaryArr

    def conversion(self, n):
        if (n > 0):
            self.conversion(int(n / 2))
            self.binaryArr.append(n % 2)
    
    def getBinaryArr(self):
        return self.binaryArr

obj = toBinary()
obj.conversion(3343)
print(obj.getBinaryArr())