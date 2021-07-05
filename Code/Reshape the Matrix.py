class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])                            #Get dimensions.
        if m * n != r * c:                                      #If total number of elements do not match, cannot reshape so return mat.
            return mat
        reshape = [[0 for _ in range(c)] for _ in range(r)]     #Initialize the reshape matrix.
        row, col = 0, 0                                         #Initialize the pointer to current row and column of pointer traversing reshape matrix.
        for i in range(m):                                      #Traverse mat.
            for j in range(n):
                reshape[row][col] = mat[i][j]                   #Set the current element of reshape to current element of mat.
                row += (col + 1) // c                           #Update row.
                col = (col + 1) % c                             #Update col.
        return reshape
