class Solution:
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        return (n>0) and (n&n-1)==0     #If n is power of 2, in binary form, the most significant bit is 1, the others are 0.
                                        #However, in binary form, all the bits are 1 ans the length is 1 bit smaller than that of n. So n%n-1 is 0.
                                        #Be sure that n is greater than 0.
