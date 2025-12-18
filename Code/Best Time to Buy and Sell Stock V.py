class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        dp = [[0] * 3 for _ in range(k + 1)]                                                    #Initialize dp; dp[i][j] means the max profit after at most i operations with state j(0 means don't hold any stock; 1 means hold a normal transaction; 2 means hold a short sell transaction).
        for j in range(1, k + 1):                                                               #On first day, we can only perform a stock buy.
            dp[j][1] = -prices[0]                                                               #Buy for normal transaction.
            dp[j][2] = prices[0]                                                                #Buy for short sell transaction.

        for i in range(1, len(prices)):                                                         #Traverse the rest days.
            for j in reversed(range(1, k + 1)):                                                 #Traverse from k to 1 backwards, because we are using a rolling 2D dp array for each day, so update the dp[j] of current day based on the dp[j - 1] of previous day.
                dp[j][0] = max(dp[j][0], max(dp[j][1] + prices[i], dp[j][2] - prices[i]))       #Update dp[j][0] to either finish a nomarl transaction or a short sell transaction.
                dp[j][1] = max(dp[j][1], dp[j - 1][0] - prices[i])                              #Update dp[j][1] to buy for a normal transaction.
                dp[j][2] = max(dp[j][2], dp[j - 1][0] + prices[i])                              #Update dp[j][2] to buy for a short sell transaction.

        return dp[k][0]                                                                         #Return dp[k][0].
