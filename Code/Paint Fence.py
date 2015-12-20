class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0:
            return 0
        result = [k, k*k]                                       #The first 2 number are k and k^2.
        for i in range(2, n):
            result.append((result[-1] + result[-2]) * (k - 1))  #Current color should be different from either the previous color or the color before the previous color.
        return result[n - 1]
