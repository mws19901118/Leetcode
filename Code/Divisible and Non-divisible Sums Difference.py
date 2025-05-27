class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        return (1 + n) * n // 2 - (m + (n // m) * m) * (n // m)      #Total sum from 1 to n minus sum of muliples of m in [1, n] then multiplied by 2.
