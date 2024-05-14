class Solution:
    def BFS(self, grid: List[List[int]], i: int, j: int) -> int:
        if grid[i][j] == 0:                                                                         #If current position is 0, return 0.
            return 0
        grid[i][j] = -1                                                                             #Set current position to -1 as it's visited.
        m, n = len(grid), len(grid[0])                                                              #Get the dimensions.
        area = 0                                                                                    #Initialize area.
        q = [(i, j)]                                                                                #Initialize queue with current position.
        while q:                                                                                    #BFS while q is not empty.
            newq = []
            for x, y in q:                                                                          #For each position in q, and 1 to area.
                area += 1
                for nx, ny in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:                     #Check 4 neighbors, if it's valid and unvisited island, add the position to newq and set it to -1.
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = -1
                        newq.append((nx, ny))
            q = newq                                                                                #Replace q with newq.
        return area                                                                                 #Return area of current island.
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        return max(self.BFS(grid, i, j) for i in range(len(grid)) for j in range(len(grid[i])))     #BFS at each position and return max value.
