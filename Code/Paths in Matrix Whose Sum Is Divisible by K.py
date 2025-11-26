class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])                                                    #Get the dimensions.
        division = 10 ** 9 + 7                                                            #Initialize division.
        dp = [[[0 for _ in range(k)] for _ in range(n)] for _ in range(m)]                #Initialize dp, dp[i][j][x] means the number of paths ending at grid[i][j] with remainder eqauls r when sum divided by x.
        for i, j in product(range(m), range(n)):                                          #Traverse grid.
            r = grid[i][j] % k                                                            #Calculate current remainder by k.
            if not i and not j:                                                           #For grid[0][0], set the number of path to 1 for remainder r.
                dp[i][j][r] = 1
            if i:                                                                         #If i is not 0, traverse dp[i - 1][j].
                for x, v in enumerate(dp[i - 1][j]):
                    dp[i][j][(x + r) % k] = (dp[i][j][(x + r) % k] + v) % division        #Update dp[i][j][(x + r) % k] based on dp[i - 1][j][x] and take the remainder after divided by 10 ** 9 + 7.
            if j:                                                                         #If j is not 0, traverse dp[i][j - 1].
                for x, v in enumerate(dp[i][j - 1]):
                    dp[i][j][(x + r) % k] = (dp[i][j][(x + r) % k] + v) % division        #Update dp[i][j][(x + r) % k] based on dp[i][j - 1][x] and take the remainder after divided by 10 ** 9 + 7.
        return dp[-1][-1][0]                                                              #Return p[-1][-1][0].
