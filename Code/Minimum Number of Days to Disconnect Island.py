class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])                                                                  #Get the dimensions.
        islandCells = set([(i, j) for i, j in product(range(m), range(n)) if grid[i][j]])               #Get all island cells.
        def isConnected():                                                                              #Check if current grid is connected.
            if not islandCells:                                                                         #If no island cells, return false.
                return False
            q = [list(islandCells)[0]]                                                                  #Get an island cell to start BFS.
            visited = set(q)
            while q:                                                                                    #BFS.
                newq = []
                for x, y in q:
                    for u, v in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]:
                        if 0 <= u < m and 0 <= v < n and (u, v) not in visited and grid[u][v]:
                            visited.add((u, v))
                            newq.append((u, v))
                q = newq
            return len(visited) == len(islandCells)                                                     #If all island cells are visited, return true; otherwize, return false.
        if not isConnected():                                                                           #If grid is already disconnected, return 0.
            return 0
        for i, j in product(range(m), range(n)):                                                        #Traverse grid.
            if grid[i][j]:                                                                              #If current cell is island, set it to water and remove it from island cells.
                grid[i][j] = 0
                islandCells.remove((i, j))
                if not isConnected():                                                                   #If grid is disconnected now, return 1.
                    return 1
                islandCells.add((i, j))                                                                 #If not, restore grid and island cells.
                grid[i][j] = 1
        return 2                                                                                        #Return 2 as it will take at most 2 days to make a connected 2 x 2 or larger island disconnected. 
