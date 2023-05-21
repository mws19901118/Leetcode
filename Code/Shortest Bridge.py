class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)                                                                           #Get n.
        boundary = set()                                                                        #Store coordinates of boundary cells of first island.
        for i, j in product(range(n), range(n)):                                                #Traverse grid to find the first island using BFS.
            if grid[i][j] == 1:
                q = [(i, j)]
                grid[i][j] = 3
                while q:
                    newq = []
                    for x, y in q:
                        for u, v in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]:
                            if 0 <= u < n and 0 <= v < n and grid[u][v] == 0:                   #Add coordinates of boundary cells to set.
                                boundary.add((x, y))
                            if 0 <= u < n and 0 <= v < n and grid[u][v] == 1:
                                newq.append((u, v))
                                grid[u][v] = 3
                    q = newq
                break
        length = 1
        q = list(boundary)
        while q:                                                                                #BFS from boundary cells to second island.
            newq = []
            for x, y in q:
                for u, v in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]:
                    if 0 <= u < n and 0 <= v < n and grid[u][v] == 1:                           #Return length once reaching second island. 
                        return length
                    if 0 <= u < n and 0 <= v < n and grid[u][v] == 0:
                        newq.append((u, v))
                        grid[u][v] = 2
            q = newq
            length += 1
