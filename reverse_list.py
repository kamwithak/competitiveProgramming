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

if __name__ == '__main__':
    obj = ComplexListDataStructure(arr=[1,2,3,4,5,6,7,8,9,10])
    print(obj.reverse1())


