class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row, col = [sum(x) for x in mat], [sum(x) for x in zip(*mat)]                                                                  #Count the 1 of each row and column.
        return sum(int(mat[i][j] == 1 and row[i] == 1 and col[j] == 1) for i, j in product(range(len(row)), range(len(col))))          #Traverse each cell, return the number of cells which is 1 and whose row and column both only has one 1.
