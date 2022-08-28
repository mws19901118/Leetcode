class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])                                                #Get the dimensions of mat.
        diagonals = [(0, x) for x in range(n)] + [(x, 0) for x in range(1, m)]      #Enumerate starting positions.
        for x, y in diagonals:                                                      #Traverse starting posisionts.
            values, i = [], 0                                                       #Store the values in this diagonal and length of diagonal.
            while x + i < m and y + i < n:                                          #Traverse the diagonal until reaches the bound.
                values.append(mat[x + i][y + i])                                    #Add current number to values.
                i += 1
            values.sort()                                                           #Sort values.
            for i, v in enumerate(values):                                          #Update the values in diagonal.
                mat[x + i][y + i] = v
        return mat                                                                  #Return matrix.
    
