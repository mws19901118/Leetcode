class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m, k, n = len(mat1), len(mat1[0]), len(mat2[0])                                                                 #Get m, k, n.
        result = [[0 for _ in range(n)] for _ in range(m)]                                                              #Initialize result.
        mat1Rows = [[(j, mat1[i][j]) for j in range(k) if mat1[i][j]] for i in range(m)]                                #Compress each row of mat1 into sparse vector.
        mat2Columns = [[(i, mat2[i][j]) for i in range(k) if mat2[i][j]] for j in range(n)]                             #Compress each column of mat2 into sparse vector.
        for i, j in product(range(m), range(n)):                                                                        #Calculate each value in result.
            x, y = 0, 0
            while x < len(mat1Rows[i]) and y < len(mat2Columns[j]):                                                     #Traverse the sparse vector of row i in mat1 and column j in mat2.
                if mat1Rows[i][x][0] == mat2Columns[j][y][0]:                                                           #Add the product to result[i][j] if the indexes are same.
                    result[i][j] += mat1Rows[i][x][1] * mat2Columns[j][y][1]
                    x += 1                                                                                              #Move forward x.
                    y += 1                                                                                              #Move forward y.
                elif mat1Rows[i][x][0] < mat2Columns[j][y][0]:                                                          #Move forward x if mat1Rows[i][x][0] < mat2Columns[j][y][0].
                    x += 1
                else:                                                                                                   #Move forward y if mat1Rows[i][x][0] > mat2Columns[j][y][0].
                    y += 1
        return result
