class Solution:
    def numSteps(self, s: str) -> int:
        x = int(s, 2)        #Convert s to int from binary string.
        count = 0
        while x != 1:        #Iterate while x is not 1.
            if x & 1:        #If x is odd, increase 1.
                x += 1
            else:            #If x is even, shift right 1 bit.
                x >>= 1
            count += 1       #Increase count.
        return count
