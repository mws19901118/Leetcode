class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])                                                                                                                                                                                #Get the dimensions.
        dp = [[[0 for _ in range(3)] for _ in range(n)] for _ in range(m)]                                                                                                                                              #Initialize dp; dp[i][j][k] means the max coins at coordinate (i, j) with k abilities left.
        for i, j in product(range(m), range(n)):                                                                                                                                                                        #Traverse the grid.
            if not i and not j:                                                                                                                                                                                         #Handle the initial cell; use ability if there is a robber.
                dp[0][0] = [coins[0][0] if coins[0][0] >= 0 else 0, coins[0][0] if coins[0][0] >= 0 else 0, coins[0][0]]
                continue
            for k in range(3):                                                                                                                                                                                          #Populate dp[k].
                if not i:                                                                                                                                                                                               #Handle first row; use ability if there is a robber and the robot has ability left; the robot can also choose not to use ability.
                    dp[i][j][k] = max(dp[i][j - 1][k] + coins[i][j], dp[i][j - 1][k + 1] if k < 2 and coins[i][j] < 0 else -inf)
                elif not j:                                                                                                                                                                                             #Handle first column; use ability if there is a robber and the robot has ability left; the robot can also choose not to use ability.
                    dp[i][j][k] = max(dp[i - 1][j][k] + coins[i][j], dp[i - 1][j][k + 1] if k < 2 and coins[i][j] < 0 else -inf)
                else:                                                                                                                                                                                                   #Handle other cells; use ability if there is a robber and the robot has ability left; the robot can also choose not to use ability.
                    dp[i][j][k] = max(max(dp[i][j - 1][k], dp[i - 1][j][k]) + coins[i][j], dp[i][j - 1][k + 1] if k < 2 and coins[i][j] < 0 else -inf, dp[i - 1][j][k + 1] if k < 2 and coins[i][j] < 0 else -inf)
        return max(dp[-1][-1])
