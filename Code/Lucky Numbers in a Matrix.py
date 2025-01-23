class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])                                                                          #Get the dimensions.
        rowMin = [min(x) for x in matrix]                                                                           #Get the min value of each row.
        colMax = [max(matrix[j][i] for j in range(m)) for i in range(n)]                                            #Get the max value of each column.
        return [matrix[i][j] for i, j in product(range(m), range(n)) if matrix[i][j] == rowMin[i] == colMax[j]]     #Traverse matrix and return all lucky numbers.
