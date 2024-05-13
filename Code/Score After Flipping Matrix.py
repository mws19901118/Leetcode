class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])                                    #Get dimensions.
        for i in range(m):                                                #Traverse each row.
            if not grid[i][0]:                                            #If the start of row is 0, flip the entire row. Because we want the first column of all rows to be 1 to maximize the score.
                for j in range(n):
                    grid[i][j] = 1 - grid[i][j]
        result = (1 << (n - 1)) * m                                       #Compute score for the most significant bit.
        for j in range(1, n):                                             #Traverse the rest columns.
            count = sum(grid[i][j] for i in range(m))                     #Count the ones in current column.
            result += (1 << (n - j - 1)) * max(count, m - count)          #Take the max of ones after flipping or not flipping, then add its contribution to score.
        return result
