class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])                                                #Get the dimensions.
        dp = [[defaultdict(int) for _ in range(n)] for _ in range(m)]                 #For each cell, store the max score for every possible cost.
        for i, j in product(range(m), range(n)):                                      #Traverse the grid.
            cost = int(grid[i][j] > 0)                                                #Calculate cost for current cell.
            if not i and not j:                                                       #Initial process for the top left cell.
                if cost > k:                                                          #If the cost is greater than k, return -1.
                    return -1
                dp[i][j][cost] = grid[i][j]                                           #Set the score to cost.
                continue                                                              #Skip the rest of processing.
            if j:                                                                     #Process the move down scenario.
                for x, y in dp[i][j - 1].items():                                     #Traverse dp[i][j - 1].
                    if x + cost <= k:                                                 #If it is possible to move down to current cell, update the dp[i][j][x + cost].
                        dp[i][j][x + cost] = max(dp[i][j][x + cost], y + grid[i][j])
            if i:                                                                     #Process the move right scenario.
                for x, y in dp[i - 1][j].items():                                     #Traverse dp[i - 1][j].
                    if x + cost <= k:                                                 #If it is possible to move down to current cell, update the dp[i][j][x + cost].
                        dp[i][j][x + cost] = max(dp[i][j][x + cost], y + grid[i][j])
        return max(dp[-1][-1].values()) if len(dp[-1][-1]) else -1                    #If dp[-1][-1] is empty, return -1; otherwise, return the max value in it.
