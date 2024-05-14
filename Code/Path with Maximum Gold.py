class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(x: int, y: int, visited: set[tuple]) -> int:                                  #DFS to calculate the total gold starting from current cell.
            visited.add((x, y))                                                               #Mark current cell as visited.
            result = 0                                                                        #Initialize result.
            for u, v in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]:                     #Traverse 4 neighbors.
                if 0 <= u < m and 0 <= v < n and (u, v) not in visited and grid[u][v]:        #If neighbor is valid, unvisited and gold, keep dfs and update result.
                    result = max(result, dfs(u, v, visited))
            visited.remove((x, y))                                                            #Unmark current cell as visited.
            return result + grid[x][y]                                                        #Return result plus gold in current cell.

        result = 0
        m, n = len(grid), len(grid[0])                                                        #Get the dimensions.
        for i, j in product(range(m), range(n)):                                              #Traverse grid.
            if grid[i][j]:                                                                    #If current cell is gold, start dfs and update result.
                result = max(result, dfs(i, j, set()))
        return result
