class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])                                                                          #Get dimemsions.
        self.s = [[0 for j in range(n + 1)] for i in range(m + 1)]
        for i in range(m):                                                                                          #Store the sum of matrix whose top left corner is the top left corner of origin matrix and bottom right corner is every element of original matrix.
            for j in range(n):
                self.s[i + 1][j + 1] = matrix[i][j] + self.s[i][j + 1] + self.s[i + 1][j] - self.s[i][j]
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.s[row2 + 1][col2 + 1] - self.s[row2 + 1][col1] - self.s[row1][col2 + 1] + self.s[row1][col1]    #Calculate sum and return.


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
