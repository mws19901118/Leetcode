class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])                  #Get dimensions.
        firstRow, firstColumn = False, False                #Indicate if first row has 0 and first column has 0.
        for i, j in product(range(m), range(n)):            #Traverse matrix.
            if matrix[i][j] != 0:                           #If current cell is not 0, continue.
                continue
            if i == 0:                                      #If i == 0, update firstRow.
                firstRow = True
            if j == 0:                                      #If j == 0, update firstColumn.
                firstColumn = True
            matrix[i][0], matrix[0][j] = 0, 0               #Set the first cell in current row and column to 0 to indicate that this row or column should be set to 0.

        for i in range(1, m):                               #Traverse rows except first row.
            if matrix[i][0] == 0:                           #If the first cell is 0, set the entire row to 0.
                for j in range(n):
                    matrix[i][j] = 0
        for j in range(1, n):                               #Traverse columns except first column.
            if matrix[0][j] == 0:                           #If the first cell is 0, set the entire column to 0.
                for i in range(m):
                    matrix[i][j] = 0
        if firstRow:                                        #If first row should be set to 0, set first row to 0.
            for j in range(n):
                matrix[0][j] = 0
        if firstColumn:                                     #If first column should be set to 0, set first column to 0.
            for i in range(m):
                matrix[i][0] = 0
