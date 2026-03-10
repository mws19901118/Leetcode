class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        division = 10 ** 9 + 7                                                                               #Initialize division.
        dp = [[[0, 0] for _ in range(one + 1)] for _ in range(zero + 1)]                                     #Initialize dp; dp[i][j][k] means the number of possible stable binary arrays with i 0 and j 1 and ending with k(k is 0 or 1).
        for i in range(min(zero, limit) + 1):                                                                #Traverse from 0 to min(zero, limit) and set dp[i][0][0] to 1; this is the case of the stable binary string only contains 0.
            dp[i][0][0] = 1
        for j in range(min(one, limit) + 1):                                                                 #Traverse from 0 to min(one, limit) and set dp[0][j][1] to 1; this is the case of the stable binary string only contains 1.
            dp[0][j][1] = 1
        for i, j in product(range(1, zero + 1), range(1, one + 1)):                                          #Traverse each combination of 0 and 1 from small to large.
            dp[i][j][0] = (sum(dp[i - 1][j]) - (0 if i <= limit else dp[i - limit - 1][j][1])) % division    #dp[i][j][0] can be derived by appending 0 after any stable binary string in dp[i - 1][j]. But if i > limit, dp[i][j][0] has to deduct dp[i - limit - 1][j][1] because we cannot have limit + 1 consecutive 0. 
            dp[i][j][1] = (sum(dp[i][j - 1]) - (0 if j <= limit else dp[i][j - limit - 1][0])) % division    #dp[i][j][1] can be derived by appending 0 after any stable binary string in dp[i][j - 1]. But if j > limit, dp[i][j][1] has to deduct dp[i][j - limit - 1][0] because we cannot have limit + 1 consecutive 1.
        return sum(dp[zero][one]) % division                                                                 #Sum up dp[zero][one] then take modulo and return.
