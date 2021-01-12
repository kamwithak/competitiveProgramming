class Two_Dimensional_Matrix:

    def isValidSize(self):
        for i in range(1, self.m):
            if (self.n != len(self.matrix[i])):
                return False
        return True 

    # def isValidType(self, expectedType=int):
    #     for i in range(len(self.matrix)):
    #         for j in range(len(matrix[0])):
    #             if (type(matrix[i][j]) != expectedType):
    #                 return False
    #     return True

    def __init__(self, matrix):

        self.matrix = matrix
        self.n = len([row for row in matrix])
        self.m = len([col for col in matrix[0]])

        if not self.isValidSize():
            raise Exception('~ MATRIX has invalid size ~')

        # if not self.isValidType():
        #     raise Exception('~ MATRIX has invalid type ~')
        
        
        # print(self.m)
        # print(self.n)


    def printMatrix(self):
        pass

if __name__ == "__main__":
    obj = Two_Dimensional_Matrix([[1,2,3,4],[1,2,4,6],[1,2,4,"s"],[2,5,6,3],[2,5,6,3],[2,5,6,7]])
