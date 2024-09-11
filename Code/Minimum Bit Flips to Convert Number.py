class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        return "{0:b}".format(start ^ goal).count("1")      #Convert start ^ goal to binary and count the 1 digit.
