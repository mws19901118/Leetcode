class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit, lowprice = 0, 0x80000000
        for p in prices:
            lowprice = min(lowprice, p)                             #Maintain the lowest price till now.
            maxprofit = max(p - lowprice, maxprofit)                #Calculate current profit(buy at lowest price and sell now), if current profit > maxprofit, update maxprofit.
        return maxprofit
