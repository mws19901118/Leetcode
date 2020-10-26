class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)                                                      #Initialize DP list from 0 to n, indicating if given number is must win or must lose.
        for i in range(1, n + 1):
            dp[i] = not all(dp[i - j * j] for j in range(1, int(sqrt(i)) + 1))      #For each number i, it's must win only if not all dp[i - j * j] is must win, for j from 1 to int(sqrt(i)).
        return dp[n]                                                                #Return dp[n]
