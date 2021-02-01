class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1          #Count n & 1.
            n >>= 1                 #Shift n one bit right.
        return count
