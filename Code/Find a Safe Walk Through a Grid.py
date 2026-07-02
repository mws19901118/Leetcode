class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])                                                  #Get the dimensions.
        maxHealth = [[0 for _ in range(n)] for _ in range(m)]                           #Initialize max health at each cell tp be 0.
        maxHealth[0][0] = health - grid[0][0]                                           #Update the max health of the starting cell.
        dq = deque([(0, 0, maxHealth[0][0])])                                           #Initialize deque.
        while dq:                                                                       #BFS.
            x, y, h = dq.popleft()                                                      #Popleft the deque.
            if (x, y) == (m - 1, n - 1):                                                #If reaches the destination, return true.
                return True
            for u, v in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]:               #Traverse the neighbors.
                if 0 <= u < m and 0 <= v < n and h - grid[u][v] > maxHealth[u][v]:      #If it is valid and the health reaching the neighbor from the current cell is higher than previous health, we should go to the neighbor.
                    maxHealth[u][v] = h - grid[u][v]                                    #Update max health of the neighbor.
                    dq.append((u, v, maxHealth[u][v]))                                  #Append the neighbor and its health to the deque.
        return False                                                                    #Return false at the end.
