class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return "{0:b}".format(x ^ y).count("1")       #Return the count of 1 in x ^ y.
