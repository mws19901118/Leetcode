class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and not n & (n - 1) and len(format(n, 'b')) & 1 == 1        #Check if n is power of 2 and its binary has odd bits.
