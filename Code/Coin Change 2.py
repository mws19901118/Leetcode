class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)               #Store DP result for each amount.
        dp[0] = 1                             #If amount is 0, dp[0] is 1.
        for i in coins:                       #The outer for loop should be traversing coins. Otherwise, there are duplicates.
            for j in range(1, amount + 1):
                if j >= i:
                    dp[j] += dp[j - i]        #For each coin value i, dp[j] += dp[j - i]. In this caes, each coin value will only be passed once.
        return dp[amount]                     #Return dp[amount]
