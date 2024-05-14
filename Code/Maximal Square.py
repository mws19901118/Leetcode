class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])                                          #Get the dimensions.
        dp = [[0 for j in range(n + 1)] for i in range(m + 1)]                      #Record the max side length of squares.
        maxLength = 0                                                               #Record current side length of square whose bottom right corner is matrix[i-1][j-1].
        for i, j in product(range(m), range(n)):                                    #Traverse matrix.
            if matrix[i][j] == '1':                                                 #If matrix[i][j] is '1', current side length equals 1 plus the min side length of squares whose bottom right corner is dp[i][j], dp[i + 1][j], dp[i][j + 1] respectively.
                dp[i + 1][j + 1] = min(dp[i][j], dp[i + 1][j], dp[i][j + 1]) + 1
                maxLength = max(maxLength, dp[i + 1][j + 1])                        #Update the max side length.
        return maxLength * maxLength                                                #Return the square of max side length.
