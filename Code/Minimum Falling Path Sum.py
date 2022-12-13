class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        if len(matrix) == 1:                                                                                                                                                            #If matrix only has 1 element, just return it.
            return matrix[0][0]
        dp = copy.deepcopy(matrix[0])                                                                                                                                                   #Instensiate dp list with the first row in matrix.
        for i in range(1, len(matrix)):                                                                                                                                                 #Traverse each row downward.
            dp = [min(dp[0], dp[1]) + matrix[i][0]] + [min(dp[j - 1], dp[j], dp[j + 1]) + matrix[i][j] for j in range(1, len(matrix) - 1)] + [min(dp[-2], dp[-1]) + matrix[i][-1]]      #The new dp[i] is the min of (dp[i - 1], dp[i], dp[i + 1]) + matrix[i][j]; except for the cell on first and last column, which should removing the invalid dp[i - 1] or dp[i + 1].
        return min(dp)                                                                                                                                                                  #Return min(dp).
