import math
class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(math.sqrt(n))  #From 1 to n, only the bulbs whose index is a square number will be toggled an odd times, thus they are on at last.
