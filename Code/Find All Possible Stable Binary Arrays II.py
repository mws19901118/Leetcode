class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:                                      #Same as Find All Possible Stable Binary Arrays I.py
        division = 10 ** 9 + 7
        dp = [[[0, 0] for _ in range(one + 1)] for _ in range(zero + 1)]
        for i in range(min(zero, limit) + 1):
            dp[i][0][0] = 1
        for j in range(min(one, limit) + 1):
            dp[0][j][1] = 1
        for i, j in product(range(1, zero + 1), range(1, one + 1)):
            dp[i][j][0] = (sum(dp[i - 1][j]) - (0 if i <= limit else dp[i - limit - 1][j][1])) % division
            dp[i][j][1] = (sum(dp[i][j - 1]) - (0 if j <= limit else dp[i][j - limit - 1][0])) % division
        return sum(dp[zero][one]) % division
