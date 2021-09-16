class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])                              #Get the dimensions.
        result = []                                                     #Initialize result.
        rowLength, columnLength = n - 1, m - 1                          #Initialize the spiral row length and spiral column length.
        for i in range(min(m // 2, n // 2)):                            #Traverse from outer spiral to inner spiral; the number of full spiral is min(m // 2, n // 2).
            for j in range(i, i + rowLength):                           #Append top spiral row.
                result.append(matrix[i][j])
            for j in range(i, i + columnLength):                        #Append right spiral column.
                result.append(matrix[j][-(i + 1)])
            for j in reversed(range(i + 1, i + rowLength + 1)):         #Append bottom spiral row.
                result.append(matrix[-(i + 1)][j])
            for j in reversed(range(i + 1, i + columnLength + 1)):      #Append left spiral column.
                result.append(matrix[j][i])
            rowLength -= 2                                              #Decrease spiral row length by 2 for next spiral.
            columnLength -= 2                                           #Decrease spiral column length by 2 for next spiral.
        if rowLength > -1 and columnLength > -1:                        #If both spiral row length and spiral column length is greater than -1, there is still one innermost partial spiral unvisited.
            if rowLength >= columnLength:                               #If spiral row length is not smaller than spiral column length, append final row to result.
                for i in range(rowLength + 1):
                    result.append(matrix[m // 2][m // 2 + i])
            else:                                                       #Otherwise, append final column to result.
                for i in range(columnLength + 1):
                    result.append(matrix[n // 2 + i][n // 2])
        return result                                                   #Return result.
