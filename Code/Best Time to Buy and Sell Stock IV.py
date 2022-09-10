class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not k or not len(prices):                                                        #If k == 0 or prices is empty, directly return 0.
            return 0
        cost, profit = [float('inf')] * k, [float('-inf')] * k                              #Initialize the min cost(buy stock but not sell yet) and max profit of performing total i + 1 transactions, 0 <= i < k. 
        for price in prices:                                                                #Traverse prices.
            for i in range(k):
                cost[i] = min(cost[i], price - (profit[i - 1] if i > 0 else 0))             #If buy at current price will decrease cost for transaction i + 1, then update cost[i].
                profit[i] = max(profit[i], price - cost[i])                                 #If sell at current price will increase profit for transaction i + 1, then update profit[i].
        return profit[-1]
