class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        self.row = len(matrix)
        if self.row == 0:
            return
        self.column = len(matrix[0])
        if self.column == 0:
            return
        self.sumfromstart = [[0 for j in range(self.column + 1)] for i in range(self.row + 1)]          #Store the sum of matrix whose top left corner is the top left corner of origin matrix and bottom right corner is every element of original matrix.
        for i in range(self.row):
            for j in range(self.column):
                self.sumfromstart[i + 1][j + 1] = matrix[i][j] + self.sumfromstart[i][j + 1] + self.sumfromstart[i + 1][j] - self.sumfromstart[i][j]

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.sumfromstart[row2 + 1][col2 + 1] - self.sumfromstart[row1][col2  + 1] - self.sumfromstart[row2 + 1][col1] + self.sumfromstart[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.sumRegion(1, 2, 3, 4)
