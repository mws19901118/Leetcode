class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])                                                                                          #Get dimensions.
        dp = [1] * m                                                                                                            #Initialize dp to be the length of sequence with valid moves starting at current cell.
        for j in reversed(range(n - 1)):                                                                                        #Traverse columns backward starting from column n - 1.
            newdp = [0] * m                                                                                                     #Initialize new dp.
            for i in range(m):                                                                                                  #Traverse each row.
                newdp[i] = max(dp[k] if 0 <= k < m and grid[k][j + 1] > grid[i][j] else 0 for k in [i - 1, i, i + 1]) + 1       #Traverse each possible neighbor row, if next column at neighbor row is valid and greater than current cell, we can move to there from current cell. So, take the max of dp of neighbor row then plus 1.
            dp = newdp                                                                                                          #Replace dp with new dp.
        return max(dp) - 1                                                                                                      #Return max number of moves, which is the max length for first column minus 1.
