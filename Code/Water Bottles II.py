class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        count, empty = 0, 0                                        #Initialize count and empty bottles.
        while True:                                                #Iterate.
            count += numBottles                                    #Drink all bottles currently available.
            empty += numBottles                                    #Update empty bottles.
            numBottles = 0                                         #Reset numBottles.
            while empty >= numExchange:                            #Try to exchange bottles as mamy as possible.
                empty -= numExchange                               #Exchange numExchange bottles.
                numBottles += 1                                    #Get 1 new bottle.
                numExchange += 1                                   #Increase numExchange.
            if not numBottles and empty < numExchange:             #If no bottles and not able to exchange for new bottles, break.  
                break
        return count
