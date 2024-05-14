class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n, count = len(grid), len(grid[0]), 0                                                #Get the dimensions and initialize count.
        for i, j in product(range(m), range(n)):                                                #Traverse each cell in grid.
            if grid[i][j] == "1":                                                               #If gird[i][j] is '1', we found an island.
                q = deque([(i, j)])                                                             #Put (i, j) in a deque.
                grid[i][j] = "2"                                                                #Set grid[i][j] to '2' to mark it as visited.
                while q:                                                                        #BFS while q is not empty.
                    x, y = q.popleft()                                                          #Popleft q.
                    for u, v in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]:               #Traverse all 4 neighbors.
                        if 0 <= u < m and 0 <= v < n and grid[u][v] == "1":                     #If the neighbor is '1', it is part of the island.
                            grid[u][v] = "2"                                                    #Mark neighbor as visited.
                            q.append((u, v))                                                    #Append it to q.
                count += 1                                                                      #Increase count.
        return count
