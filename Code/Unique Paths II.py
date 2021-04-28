class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = [0] * (len(obstacleGrid[0]) + 1)                       #Initialize dp array with dp[1] = 1 and others 0.
        dp[1] = 1
        for row in obstacleGrid:                                    #Traverse rows in obstacleGrid.
            for i, x in enumerate(row):                             #Traverse each row.
                dp[i + 1] = 0 if x else dp[i + 1] + dp[i]           #If current cell is 0, set dp[i + 1] to 0; otherwise, set it to dp[i + 1] + dp[i] as the sum of paths from up and left.
        return dp[-1]                                               #Return the last element in dp.
