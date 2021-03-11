class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount + 1)                                                                    #Store the least coins needed to get this value(from 0 to amount), initially -1.
        dp[0] = 0                                                                                   #To get 0, you don't need any coins.
        for c in coins:                                                                             #Traverse the coins list.
            for i in range(c, amount + 1):                                                          #Then traverse the value from c to amount.
                if dp[i - c] != -1:                                                                 #If dp[i - c] == -1, current value cannot be formed from i - c, so continue.
                    dp[i] = dp[i - c] + 1 if dp[i] == -1 else min(dp[i], dp[i - c] + 1)             #Update dp[i] tp take the minimum of dp[i] and dp[i - c] + 1 if dp[i] != -1; otherwise directly set dp[i] to dp[i - c] + 1.
        return dp[amount]                                                                           #Return the number of coins of amount.
