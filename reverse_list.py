import sys

class ComplexListDataStructure():
    
    def __init__(self, arr=[]):
        self.arr = arr
        self.size = len(arr)


    def swap(self, i, j):
        tmp = self.arr[i]
        self.arr[i] = self.arr[j]
        self.arr[j] = tmp

    def reverse1(self):
        """
            Time: O(n/2) == O(n) where n is self.size
            Space: O(1)
        """
        i = 0
        j = self.size-1
        while (i < j):
            self.swap(i, j)
            i += 1
            j -= 1
        return self.arr

    def reverse2(self):
        if (len(self.arr) == 1):
            return self.arr
        else:
            firstElement = self.arr.pop(0)
            self.reverse2()
            self.arr.append(firstElement)
    
    def removeMax(self):
        maxElement = -sys.maxsize
        maxIndex = -sys.maxsize
        for index, elem in enumerate(self.arr):
            if (elem > maxElement):
                maxElement = elem
                maxIndex = index
        self.arr.pop(maxIndex)
        return maxElement

    def removeMin(self):
        minElement = sys.maxsize
        minIndex = sys.maxsize
        for index, elem in enumerate(self.arr):
            if (elem < minElement):
                minElement = elem
                minIndex = index
        self.arr.pop(minIndex)
        return minElement
            
    def insertionSort(self, ascending=True):
        if (len(self.arr) == 1):
            return self.arr
        else:
            if (ascending):
                maxElement = self.removeMax()
                self.insertionSort(ascending)
                self.arr.append(maxElement)
            else:
                minElement = self.removeMin()
                self.insertionSort(ascending)
                self.arr.append(minElement)

    def getArr(self):
        return self.arr

if __name__ == '__main__':
    obj = ComplexListDataStructure(arr=[10,8,543,24,234,23,52,2])
    obj.insertionSort()
    print(obj.getArr())

