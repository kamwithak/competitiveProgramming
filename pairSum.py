class PairSum:
    '''
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice
    '''
    def __init__(self, arr, k):
        self.arr = arr
        self.k = k

    def solution(self):
        for i in range(len(self.arr)-1):
            for j in range(i+1, len(self.arr)):
                if (self.arr[i] + self.arr[j] == self.k):
                    return [i, j]
        return False

if __name__ == "__main__":
    obj = PairSum([2, 7, 11, 15], 7+15)
    print(obj.solution())