class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(max(0, prices[i + 1] - prices[i]) for i in range(len(prices) - 1))   #On each day(except the first day), the max profit is current price minus previous price, so return the sum of max profit each day.
