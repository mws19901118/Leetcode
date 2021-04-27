class Solution:
    def isPowerOfThree(self, n: int) -> bool:
         return n > 0 and 1162261467 % n == 0       #The max power of 3 under 2 ^ 31 - 1 is 1162261467. So every power of 3 should be larger than 0 and a factor of 1162261467.
