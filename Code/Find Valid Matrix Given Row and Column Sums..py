class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m, n = len(rowSum), len(colSum)                              #Get the dimensions.
        matrix = [[0 for _ in range(n)] for _ in range(m)]           #Initialize matrix.
        i, j = 0, 0                                                  #Initialize current row and column, starting from 0 and 0.
        while i < m and j < n:                                       #Traverse while row and column from top left to bottom right until either there is row or column un set.
            matrix[i][j] = min(rowSum[i], colSum[j])                 #Assign matrix[i][j] to the smaller of rowSum[i] and colSum[j].
            rowSum[i] -= matrix[i][j]                                #Subtract matrix[i][j] from rowSum[i].
            colSum[j] -= matrix[i][j]                                #Subtract matrix[i][j] from colSum[j].
            if rowSum[i] == 0:                                       #If rowSum[i] is 0, we cannot assign more numbers on this row, so move to next row.
                i += 1
            else:                                                    #Otherwise, we cannot assign more numbers on this column, so move to next column.
                j += 1
        return matrix
