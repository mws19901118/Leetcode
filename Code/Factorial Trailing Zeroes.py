class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        zeros=0
        while n!=0:                             #The number of trailing zeros is actually the number of factor 5.
            zeros+=n/5                          #Thus, calculate how many numbers smaller than n have factor 5.
            n=n/5                               #Notice the power of 5.
        return zeros
