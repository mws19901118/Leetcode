class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        maxprofit=0
        lowprice=0x80000000
        p1 = [0]*len(prices)
        for i in range(len(prices)):
            lowprice=min(lowprice,prices[i])      
            maxprofit=max(prices[i]-lowprice,maxprofit)                 
            p1[i] = maxprofit                                   #Calculate the maxprofit for 1 transition from beginning to prices[i].
            
        maxprofit=0
        maxprice=-1
        p2 = [0]*len(prices)
        for i in range(len(prices) - 1, -1, -1):
            maxprice=max(maxprice,prices[i])      
            maxprofit=max(maxprice-prices[i],maxprofit)                 
            p2[i] = maxprofit                                   #Calculate the maxprofit for 1 transition from prices[i] to end.
        
        maxp=0
        for i in range(len(prices)):
            maxp = max(p1[i] + p2[i], maxp)                     #Calculate the maxprofit for 2 transitions, seperated at prices[i].
        return maxp
