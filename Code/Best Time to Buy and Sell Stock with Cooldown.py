class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = len(prices)
        if l == 0:
            return 0
        sell = [0, 0]                                 #Store the max profit when sell the stock on the ith day.
        hold = [0, -prices[0]]                        #Store the max profit when hold the stock on the ith day.
        wait = [0, 0]                                 #Store the max profit when cooldown on the ith day.
        for i in range(1, l):
            s = hold[-1] + prices[i]                  #Sell on current day.
            h = max(wait[-1] - prices[i], hold[-1])   #Hold on current day, either buy on current day or hold the stock bought before.
            w = max(sell[-1], wait[-1])               #Cooldown on current day.
            sell.append(s)
            hold.append(h)
            wait.append(w)
        return max(sell[-1], hold[-1], wait[-1])      #Return the max profit after the last day.
