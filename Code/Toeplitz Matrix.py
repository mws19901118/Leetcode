class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])                                                                                          #Get the dimensions of matrix.
        start = [(0, 0)] + [(i, 0) for i in range(1, m)] + [(0, i) for i in range(1, n)]                                            #Initialize the start points of each diagonal, basically the first column and first row.
        return all(all(matrix[x + i][y + i] == matrix[x][y] for i in range(min(m - x, n - y))) for x, y in start)                   #Each element in each diagonal should be same with its start.
