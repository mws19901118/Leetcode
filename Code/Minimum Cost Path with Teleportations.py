class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])                                                                                                                        #Get the dimensions.
        dp = [[inf for _ in range(n)] for _ in range(m)]                                                                                                      #Initialize dp.
        for _ in range(k + 1):                                                                                                                                #Iterate k + 1 times.
            sortedCells = sorted([(i, j) for i, j in product(range(m), range(n))], key = lambda x: (grid[x[0]][x[1]], dp[x[0]][x[1]]))                        #Sort each cell in by its grid value in asending order then its dp value in asending order.
            minCost = inf                                                                                                                                     #Initialize the min cost at teleportation destination.
            for i, j in sortedCells:                                                                                                                          #Traverse sorted cells.
                dp[i][j] = min(dp[i][j], minCost)                                                                                                             #Update dp[i][j] if the min cost is smaller. 
                minCost = min(minCost, dp[i][j])                                                                                                              #Update min cost.
            for i, j in product(reversed(range(m)), reversed(range(n))):                                                                                      #Traverse the grid backwards.
                if i == m - 1 and j == n - 1:                                                                                                                 #If it is the bottom right cell, its cost is always 0.
                    dp[i][j] = 0
                    continue
                dp[i][j] = min(dp[i][j], (dp[i + 1][j] + grid[i + 1][j] if i < m - 1 else inf), (dp[i][j + 1] + grid[i][j + 1] if j < n - 1 else inf))        #Update dp[i][j] from normal move.
        return dp[0][0]                                                                                                                                       #Return dp[0][0].
