class Solution:
    def sumRemoteness(self, grid: List[List[int]]) -> int:
        def BFS(i: int, j: int) -> int:                                                                                    #BFS to calculate the remoteness of current component.
            count, value = 0, 0                                                                                            #Initialize cell count and cell sum.
            q = deque([(i, j)])                                                                                            #Initialize q with current cell.
            visited.add((i, j))                                                                                            #Mark current cell as visited.
            while q:                                                                                                       #BFS to calculate count and value.
                x, y = q.popleft()
                count += 1
                value += grid[x][y]
                for u, v in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]:
                    if u < 0 or u >= m or v < 0 or v >= n or (u, v) in visited or grid[u][v] == -1:
                        continue
                    q.append((u, v))
                    visited.add((u, v))
            return (total_sum - value) * count                                                                              #For every cell in current component, its remoteness is total_sum - value.
     
        m, n = len(grid), len(grid[0])                                                                                      #Get the dimensions.
        visited = set()                                                                                                     #Store visited cells.
        total_sum = sum(max(0, grid[i][j]) for i, j in product(range(m), range(n)))                                         #Calculate total sum of non-blocked cells.
        return sum(BFS(i, j) for i, j in product(range(m), range(n)) if grid[i][j] > 0 and (i, j) not in visited)           #Sum up the BFS result of all non-blocked components and return.
