class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [[int(matrix[i][j]) for j in range(len(matrix[i]))] for i in range(len(matrix))]               #Record the max side length of squares.
        maxLength = 0                                                                                       #Record current side length of square whose bottom right corner is matrix[i-1][j-1].
        for i in range(len(dp)):
            for j in range(len(dp[i])):
                if dp[i][j] == 1 and i > 0 and j > 0:                                                       #If dp[i][j] is '1', current side length equals 1 plus the min side length of squares whose bottom right corner is dp[i-1][j-1], dp[i][j-1], dp[i-1][j] respectively.
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1
                maxLength = max(maxLength, dp[i][j])                                                        #Update the max side length.
        return maxLength * maxLength                                                                        #Return the square of max side length.
