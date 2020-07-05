class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        d, count = x ^ y, 0       # Calculate x^y and count 1s in its binary.
        while d > 0:
            count += d & 1
            d >>= 1
        return count
