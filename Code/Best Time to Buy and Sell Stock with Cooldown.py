class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell, wait, hold = [0], [0], [float('-inf')]    #Initialize the list to store max profit to sell, wait or hold on the ith day.
        for p in prices:                                #Traverse prices.
            s, w, h = sell[-1], wait[-1], hold[-1]      #Get the max profit from selling, waiting or holding on previous day.
            sell.append(h + p)                          #If sell today, the max profit now is h + p.
            wait.append(max(s, w))                      #If wait today, the max profit now is max(s, w).
            hold.append(max(h, w - p))                  #If hold today, the max profit now is max(h, w - p).
        return max(sell[-1], wait[-1], hold[-1])        #Return the max profit after the last day.
