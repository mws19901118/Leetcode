class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])                                                                                                                                #Get the dimensions.
        result = [[0 for _ in range(n - k + 1)] for _ in range(m - k + 1)]                                                                                            #Initialize result.
        for i, j in product(range(m - k + 1), range(n - k + 1)):                                                                                                      #Traverse the first m - k + 1 rows and n - k + 1 columns.
            values = sorted(grid[x][y] for x, y in product(range(i, i + k), range(j, j + k)))                                                                         #Store the k x k submatrix starting at grid[i][j] in a list and sort it.
            result[i][j] = 0 if values[0] == values[-1] else min(values[j] - values[j - 1] if values[j] != values[j - 1] else inf for j in range(1, len(values)))     #Calculate the minimum absolute difference.
        return result
