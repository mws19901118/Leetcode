class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        sold, hold = 0, -prices[0]                      #Initialize the max cash we have sold stock or we currently hold stock for the first day.
        for i in range(1, len(prices)):                 #Traverse prices[1:].
            sold = max(sold, hold + prices[i] - fee)    #If we have sold stock, take the max of cash in 2 situations: we sell today or we sold before.
            hold = max(hold, sold - prices[i])          #If we hold stock, take the max of cash in 2 situations: we buy stock or we bought before.
        return sold                                     #At the end, we mush hold no stocks, so return sold.
