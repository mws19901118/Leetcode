class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])                                                                  #Get dimensions.
        count = 0
        for i, j in product(range(m), range(n)):                                                        #Traverse grid.
            if grid[i][j] != 0:                                                                         #If grid[i][j] is not 0, continue.
                continue
            q = [(i, j)]
            grid[i][j] = -1
            reachEdge = False
            while q:                                                                                    #BFS.
                newq = []
                for x, y in q:
                    for nx, ny in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]:
                        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0:
                            newq.append((nx, ny))
                            grid[nx][ny] = -1
                        elif nx == -1 or nx == m or ny == -1 or ny == n:                                #Set reachEdge to true if reaches edge.
                            reachEdge = True
                q = newq
            count += int(not reachEdge)                                                                 #Increase cound only when not reaching edge.
        return count
