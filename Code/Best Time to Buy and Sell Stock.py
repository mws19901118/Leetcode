class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        length=len(prices)
        if length==0 or length==1:
            return 0
        maxprofit=0
        lowprice=prices[0]
        for i in range(length):
            lowprice=min(lowprice,prices[i])                    #maintain the lowest price
            maxprofit=max(prices[i]-lowprice,maxprofit)         #if current profit>maxprofit, set maxprofit to current profit
        return maxprofit
