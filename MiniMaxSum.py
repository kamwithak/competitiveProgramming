class MiniMaxSum():
    def __init__(self, arr):
        self.arr = arr
        self.size = 5
    
    def solution(self):
        """
        Given five positive integers,
        find the minimum and maximum values
        that can be calculated by summing exactly
        four of the five integers.
        Then print the respective minimum and maximum
        values as a single line of two space-separated
        long integers.
        """
        ptr1, ptr2, ptr3, ptr4 = 0, 1, 2, 3
        sum1 = self.arr[ptr1]+self.arr[ptr2]+self.arr[ptr3]+self.arr[ptr4]
        sum2 = self.arr[ptr1]+self.arr[ptr2]+self.arr[ptr3]+self.arr[ptr4+1]
        sum3 = self.arr[ptr1]+self.arr[ptr2]+self.arr[ptr3+1]+self.arr[ptr4+1]
        sum4 = self.arr[ptr1]+self.arr[ptr2+1]+self.arr[ptr3+1]+self.arr[ptr4+1]
        sum5 = self.arr[ptr1+1]+self.arr[ptr2+1]+self.arr[ptr3+1]+self.arr[ptr4+1]
        return min(sum1,sum2,sum3,sum4, sum5), max(sum1,sum2,sum3,sum4, sum5)

obj = MiniMaxSum([1,3,5,7,9])

print(obj.solution())

