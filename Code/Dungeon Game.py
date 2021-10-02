class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])                                                                    #Get the dimensions.
        dp = [200001] * n                                                                                       #Initialize dp list with size n. In current iteration of text1[:i + 1], dp[j] meams the min hp for dungeon[i][j] alive.
        dp[-1] = 1                                                                                              #Set dp[-1] to 1 while other other indexes to a really large number(larger than the max sum of a row).
        for i in reversed(range(m)):                                                                            #Traverse dungeon from bottom right corner to top left corner.
            for j in reversed(range(n)):
                dp[j] = max(1, (dp[j] if j == n - 1 else min(dp[j + 1], dp[j])) - dungeon[i][j])                #Since knight can only move rightward or downward, min hp for dungeon[i][j] will first take the smaller min hp dungeon[i + 1][j] and dungeon[i][j + 1](only dungeon[i + 1][j] if j is at the end and intialize dp[j] at a really lartge number will cover the case where i == m - 1). Then substract dungeon[i][j] from previous value. Also, dp[j] should be at least 1.
        return dp[0]                                                                                            #Return dp[0].
