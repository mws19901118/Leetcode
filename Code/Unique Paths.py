class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        last = [1 for i in range(n)]                    #Record the unique paths of each grid in last row. It's all 1 for first row.
        for i in range(1, m):
            for j in range(1, n):                       #For each row, current paths eqauls the sum of paths from left grid and upper grid.
                last[j] += last[j - 1]
        return last[n - 1]
