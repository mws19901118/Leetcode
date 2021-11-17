class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        last = [1] * n                                      #Record the unique paths of each grid in last row. It's all 1 for first row.
        for i, j in product(range(m - 1), range(n - 1)):    #For each row, current paths eqauls the sum of paths from left grid and upper grid.
            last[j + 1] += last[j]
        return last[n - 1]
