class DiagonalDifference():
    def __init__(self, squareMatrix):
        self.squareMatrix = squareMatrix
        self.sizeOfSquareMatrix = len(squareMatrix)
    
    def solution(self):
        leftToRight, rightToLeft = 0, 0
        leftIndex, rightIndex = 0, self.sizeOfSquareMatrix-1
        for arr in self.squareMatrix:
            leftToRight += arr[leftIndex]
            leftIndex += 1
            rightToLeft += arr[rightIndex]
            rightIndex -= 1
        return abs(leftToRight-rightToLeft)

obj = DiagonalDifference([[1,2,3],[4,5,6],[9,8,9]])

print(obj.solution())

