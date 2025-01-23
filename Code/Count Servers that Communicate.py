class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])                                                                                        #Get the dimensions.
        rowCount, columnCount = [sum(r) for r in grid], [sum(grid[i][j] for i in range(m)) for j in range(n)]                 #Count servers in each row and column.
        return sum(int(grid[i][j] and (rowCount[i] != 1 or columnCount[j] != 1)) for i, j in product(range(m), range(n)))     #Count servers that are not the only server in both its row and its column.
