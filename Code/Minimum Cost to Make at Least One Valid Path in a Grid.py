class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])                                                              #Get the dimensions.
        cost = 0                                                                                    #Initialize cost.
        directions = {1: (0, 1), 2: (0, -1), 3: (1, 0), 4: (-1, 0)}                                 #Map the directions based on cell value.
        dq, visited = deque([(0, 0)]), set([(0, 0)])                                                #Initialize deque and visited set.
        while True:                                                                                 #Iterate until reach destination.
            neighbors = set()                                                                       #Initialize neighbors set.
            while dq:                                                                               #Iterate while dq is not empty.
                x, y = dq.popleft()                                                                 #Popleft current cell from dq.
                if (x, y) == (m - 1, n - 1):                                                        #If reaches the destination, return cost.
                    return cost
                next_x, next_y = x + directions[grid[x][y]][0], y + directions[grid[x][y]][1]       #Get the next call based on direction.
                if 0 <= next_x < m and 0 <= next_y < n and (next_x, next_y) not in visited:         #If next cell is valid and not visited, process the followings.
                    dq.append((next_x, next_y))                                                     #Append it to dq.
                    visited.add((next_x, next_y))                                                   #Add it to visited.
                    neighbors.discard((next_x, next_y))                                             #Discard it from neighbors,
                for u, v in [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]:                       #Traverse the neighbors of current cell.
                    if u < 0 or u >= m or v < 0 or v >= n or (u, v) in visited:                     #If neighbors is invalid or visited, continue.
                        continue
                    neighbors.add((u, v))                                                           #Add it to neighbors.
            dq = deque(neighbors)                                                                   #Convert neighbors to dq,
            cost += 1                                                                               #Increase cost.
