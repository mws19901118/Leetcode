class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        sold, hold = 0, float('-inf')                                        #Initialize the max cash we have sold stock or we currently hold stock before traversing.
        for x in prices:                                                     #Traverse prices.
            sold, hold = max(sold, hold + x - fee), max(hold, sold - x)      #If we have sold stock, take the max of cash in 2 situations: we sell today or we sold before. If we hold stock, take the max of cash in 2 situations: we buy stock or we bought before.
        return sold                                                          #At the end, we mush hold no stocks, so return sold.
