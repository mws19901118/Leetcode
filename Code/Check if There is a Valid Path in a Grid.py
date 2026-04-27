class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])                                                                                                                            #Get the dimensions.
        neighbors = {1: [(0, -1), (0, 1)], 2: [(-1, 0), (1, 0)], 3: [(0, -1), (1, 0)], 4: [(0, 1), (1, 0)], 5: [(0, -1), (-1, 0)], 6: [(0, 1), (-1, 0)]}          #For each type of road, store its neighbor directions.
        connectors = {(0, -1): [1, 4, 6], (0, 1): [1, 3, 5], (-1, 0): [2, 3, 4], (1, 0): [2, 5, 6]}                                                               #For each direction, store its valid connectoring roads.
        dq = deque([(0, 0)])                                                                                                                                      #Initialize deque with the top left cell.
        visited = set()                                                                                                                                           #Store visited cells.
        while dq:                                                                                                                                                 #BFS.
            x, y = dq.popleft()
            if (x, y) == (m - 1, n - 1):                                                                                                                          #If reaches bottom right cell, return true.
                return True
            for i, j in neighbors[grid[x][y]]:                                                                                                                    #Traverse the neighbor directions based on current road.
                u, v = x + i, y + j                                                                                                                               #Get the neighbor cell coordinate.
                if 0 <= u < m and 0 <= v < n and grid[u][v] in connectors[(i, j)] and (u, v) not in visited:                                                      #Process neighbor cell only if is not out of bound, its road can conenct with current cell and it is not visited.
                    visited.add((u, v))                                                                                                                           #Mark the neighbor as visited.
                    dq.append((u, v))                                                                                                                             #Append the neighbor to deque.
        return False                                                                                                                                              #Return false at the end.
