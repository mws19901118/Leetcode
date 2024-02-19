class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n and not n & (n - 1)        #If n is power of 2, in binary form, the most significant bit is 1, the others are 0.
                                            #And for n - 1, in binary form, all the bits are 1 and the length is 1 bit smaller than that of n. So n & (n - 1) == 0.
                                            #Be sure that n is greater than 0.
