class Solution:
    def coloredCells(self, n: int) -> int:
        return 2 * n * (n - 1) + 1          #Initial value is 1 and each minute later the area will expand 4 * (n - 1) cells, so overall is 4 * (1 + n - 1) * n // 2 + 1 = 2 * n * (n - 1) + 1.
