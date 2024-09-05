class Solution:
    def numWays(self, n: int, k: int) -> int:
        result = [k, k * k]                                     #The first 2 number are k and k ** 2.
        for i in range(2, n):
            result.append((result[-1] + result[-2]) * (k - 1))  #Current color should be different from either the previous color: (k - 1) * result[-1] or same with previous color but different with the color before the previous color (k - 1) * result[-2].
        return result[n - 1]
