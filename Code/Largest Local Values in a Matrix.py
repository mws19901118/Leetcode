class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        result = [[0 for _ in range(len(grid) - 2)] for _ in range(len(grid)- 2)]                        #Initialize result.
        for i, j in product(range(len(grid) - 2), range(len(grid) - 2)):                                 #Enumerate each top left corner of sub-matrixes.
            result[i][j] = max(grid[x][y] for x, y in product(range(i, i + 3), range(j, j + 3)))         #Calculate the local max in sub-matricx.
        return result
