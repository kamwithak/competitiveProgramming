class PairSum:
    '''
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    '''
    def __init__(self, arr, k):
        self.arr = arr
        self.k = k
    '''
    n^2 - algo 
    '''
    def solutionQuadraticTime(self):
        for i in range(len(self.arr)-1):
            for j in range(i+1, len(self.arr)):
                if (self.arr[i] + self.arr[j] == self.k):
                    return [i, j]
        return False
    
    '''
    n - algo
    '''
    def solutionLinearTime(self):
        _dict = {}
        for i in range(len(self.arr)):
            comp = self.k - self.arr[i]
            if (comp in _dict):
                return [_dict[comp], i]
            else:
                _dict[self.arr[i]] = i
        return False
        
if __name__ == "__main__":
    obj = PairSum([2, 7, 11, 15], 14+8)
    #print(obj.solutionQuadraticTime())
    print(obj.solutionLinearTime())
