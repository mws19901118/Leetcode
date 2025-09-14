class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [inf] * amount                                #Initialize dp, starting with 0 at 0 and inf for the rest.
        for x in coins:                                          #Traverse coins.
            for i in range(amount + 1 - x):                      #Then traverse the value from 0 to amount + 1 - x.
                dp[i + x] = min(dp[i + x], dp[i] + 1)            #Update dp[i + x] to take the minimum of dp[i + x] and dp[i] + 1.
        return dp[amount] if dp[amount] < inf else -1            #Return dp[amount] if it is not inf; otherwise, return -1.
