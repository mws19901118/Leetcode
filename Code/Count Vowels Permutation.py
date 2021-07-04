class Solution:
    def countVowelPermutation(self, n: int) -> int:
        division = 10 ** 9 + 7
        dp = [1, 1, 1, 1, 1]                                                                                                                  #Initialize dp for the case when n == 1.
        for _ in range(1, n):                                                                                                                 #Iterate from n - 1 times.
            dp = [dp[1], (dp[0] + dp[2]) % division, (dp[0] + dp[1] + dp[3] + dp[4]) % division, (dp[2] + dp[4]) % division, dp[0]]           #Update dp for a, e, i, o, u.
        return sum(dp) % division                                                                                                             #Sum up dp and then return modulo.
