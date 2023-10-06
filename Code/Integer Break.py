class Solution:
    def integerBreak(self, n: int) -> int:      #https://leetcode.com/problems/integer-break/solutions/80785/O(log(n))-Time-solution-with-explanation/
        if n <= 3:
            return n - 1
        elif n % 3 == 0:
            return 3 ** (n // 3)
        elif n % 3 == 1:
            return 3 ** (n // 3 - 1) * 4
        return 3 ** (n // 3) * 2
