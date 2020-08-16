class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit, lowprice = 0, 0x80000000
        p1 = [0] * len(prices)
        for i in range(len(prices)):                                    #Calculate the maxprofit for 1 transition from beginning to prices[i].
            lowprice = min(lowprice, prices[i])      
            maxprofit = max(prices[i] - lowprice, maxprofit)                 
            p1[i] = maxprofit
            
        maxprofit, maxprice = 0, -1                                     #Calculate the maxprofit for 1 transition from prices[i] to end.
        p2 = [0] * len(prices)
        for i in range(len(prices) - 1, -1, -1):
            maxprice = max(maxprice, prices[i])      
            maxprofit = max(maxprice - prices[i], maxprofit)                 
            p2[i] = maxprofit
        
        maxp = 0
        for i in range(len(prices)):                                    #Calculate the maxprofit for 2 transitions, seperated at prices[i].
            maxp = max(p1[i] + p2[i], maxp)
        return maxp
    
