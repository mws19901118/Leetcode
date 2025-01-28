class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])                                                  #Get the dimensions.
        result = 0
        for i, j in product(range(m), range(n)):                                        #Traverse grid.
            if grid[i][j] > 0:                                                          #If current cell is water, BFS to sum up the number of fishes in all connected water cells.
                count = 0
                q = deque([(i, j)])
                grid[i][j] *= -1                                                        #Mark grid[i][j] as visited.
                while q:
                    x, y = q.popleft()
                    count -= grid[x][y] 
                    for u, v in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]:
                        if u < 0 or u >= m or v < 0 or v >= n or grid[u][v] <= 0:
                            continue
                        q.append((u, v))
                        grid[u][v] *= -1                                                #Mark grid[u][v] as visited.
                result = max(result, count)                                             #Update result if count is greater.
        return result
