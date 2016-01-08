import math
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:                                         #Power of 3 should be larger than or equal to 1.
            return False
        t = math.log(n) / math.log(3)                     #Calculate log3(n).
        return abs(t - round(t)) < 0.00000001             #If it's an integer, n is power of 3.
