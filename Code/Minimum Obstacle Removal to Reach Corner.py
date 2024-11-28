class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])                                            #Get the dimensions.
        start, visited = set([(0, 0)]), set([(0, 0)])                             #Initialize start and visited set.
        count = 0                                                                 #Initialize count.
        while True:                                                               #Iterate while not reaching the lower right corner.
            q = deque(start)                                                      #Put all cells in start in a deque.
            start.clear()                                                         #Clear start set.
            while q:                                                              #BFS until no more empty cells.
                x, y = q.popleft()
                if x == m - 1 and y == n - 1:                                     #If reaches the lower right corner, return count.
                    return count
                for u, v in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]:     #Traverse 4 neighbors of current cell.
                    if u < 0 or u >= m or v < 0 or v >= n or (u, v) in visited:
                        continue
                    if grid[u][v]:                                                #If the neighbor is obastacle, add it to start for next iteration if necessary.
                        start.add((u, v))
                    else:                                                         #Otherwise, append it to q.
                        q.append((u, v))
                    visited.add((u, v))                                           #Mark it as visited.
            count += 1                                                            #Start next iteration by virtually remove all obastacles in start, so increase count.
