class NumMatrix(object):                                                                        #2D Binary indexed tree.
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        self.row = len(matrix)
        if self.row == 0:
            return
        self.col = len(matrix[0])
        if self.col == 0:
            return
        self.tree = [[0 for j in range(self.col + 1)] for i in range(self.row + 1)]
        self.matrix = [[0 for j in range(self.col)] for i in range(self.row)]
        for i in range(self.row):
            for j in range(self.col):
                self.update(i, j, matrix[i][j])

    def update(self, row, col, val):
        """
        update the element at matrix[row,col] to val.
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        origin = self.matrix[row][col]
        self.matrix[row][col] = val
        i = row + 1
        while i < self.row + 1:
            j = col + 1
            while j < self.col + 1:
                self.tree[i][j] += val - origin
                j += j & -j
            i += i & -i

    def sumRegion(self, row1, col1, row2, col2):                                              #Sum a region, like Range Sum Query 2D - Immutable.
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.getSum(row2 + 1, col2 + 1) - self.getSum(row1, col2 + 1) - self.getSum(row2 + 1, col1) + self.getSum(row1, col1)
    
    def getSum(self, row, col):                                                               #Get the sum from the up left corner to certain row and column.
        result = 0
        i = row
        while i > 0:
            j = col
            while j > 0:
                result += self.tree[i][j]
                j -= j & -j
            i -= i & -i
        return result
# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.update(1, 1, 10)
# numMatrix.sumRegion(1, 2, 3, 4)
