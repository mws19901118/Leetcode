class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        division = 10 ** 9 + 7                                                    #Initialize division.
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]                    #Initiali dp list; dp[i][j] represents the number of ways to express j with the x-power of first i number.
        dp[0][0] = 1                                                              #Set dp[0][0] to 1 
        for i in range(1, n + 1):                                                 #Traverse from 1 to n(inclusive).
            power = i ** x                                                        #Calculate i ** x.
            for j in range(n + 1):                                                #Traverse from 0 to n.
                dp[i][j] = dp[i - 1][j]                                           #Set dp[i][j] to dp[i - 1][j].
                if j >= power:                                                    #If j is greater than power, add dp[i - 1][j - power] to dp[i][j] and take modulo.
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - power]) % division
        return dp[n][n]                                                           #Return dp[n][n].
