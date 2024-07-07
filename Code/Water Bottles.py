class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        count, empty = 0, 0                                                    #Initialize total count and empty bottles after each exchange.
        while numBottles > 0:                                                  #Iterate while there are full bottles left.
            count += numBottles                                                #Drink all full bottles.
            numBottles, empty = divmod(numBottles + empty, numExchange)        #Now exchange all empty bottles to full bottles.
        return count
