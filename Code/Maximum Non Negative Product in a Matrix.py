class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])                                            #Get the dimensions.
        dp = [[[0, 0] for _ in range(n)] for _ in range(m)]                       #Store the min and max path product at each cell.
        for i, j in product(range(m), range(n)):                                  #Traverse the grid and update the min and max path product at each cell using DP.
            if not i and not j:
                dp[i][j] = [grid[i][j], grid[i][j]]
            elif not i:
                dp[i][j] = [min(grid[i][j] * dp[i][j - 1][0], grid[i][j] * dp[i][j - 1][1]), max(grid[i][j] * dp[i][j - 1][0], grid[i][j] * dp[i][j - 1][1])]
            elif not j:
                dp[i][j] = [min(grid[i][j] * dp[i - 1][j][0], grid[i][j] * dp[i - 1][j][1]), max(grid[i][j] * dp[i - 1][j][0], grid[i][j] * dp[i - 1][j][1])]
            else:
                dp[i][j] = [min(grid[i][j] * dp[i][j - 1][0], grid[i][j] * dp[i][j - 1][1], grid[i][j] * dp[i - 1][j][0], grid[i][j] * dp[i - 1][j][1]), max(grid[i][j] * dp[i][j - 1][0], grid[i][j] * dp[i][j - 1][1], grid[i][j] * dp[i - 1][j][0], grid[i][j] * dp[i - 1][j][1])]
        return dp[-1][-1][1] % (10 ** 9 + 7) if dp[-1][-1][1] >= 0 else -1        #If the max path product at the destination cell is not smaller than 0, take modulo and return; otherwise, return -1.
