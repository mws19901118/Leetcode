class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])                                              #Get the dimensions of grid.
        dp = [0]                                                                    #Build the path sum for first row.
        for x in grid[0]:
            dp.append(dp[-1] + x)
        dp[0] = float('inf')                                                        #Set dp[0] to a real large number.
        for i, j in product(range(1, m), range(n)):                                 #Traverse the rest of matrix.
            dp[j + 1] = min(dp[j], dp[j + 1]) + grid[i][j]                          #Calculate the min path sum at each cell, which is the min from left(dp[j]) and from top(dp[j + 1]) plus value at current cell.
        return dp[-1]                                                               #Return dp[-1].
