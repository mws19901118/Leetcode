class Solution:
    def BFS(self, grid: List[List[str]], i: int, j:int):
        grid[i][j] == '2'                                                                                               #Set current coordinate as visited.
        q = [(i, j)]                                                                                                    #Initialize queue.
        while q:                                                                                                        #BFS while q is not empty.
            nextq = []                                                                                                  #Initialize nextq.
            for x, y in q:                                                                                              #Traverse each coordinate in queue.
                for nx, ny in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]:                                         #Traverse each neighbor.
                    if nx >= 0 and nx < len(grid) and ny >= 0 and ny < len(grid[0]) and grid[nx][ny] == '1':            #If the neighbor is valid and unvisited land.
                        grid[nx][ny] = '2'                                                                              #Mark neighbor as visited.
                        nextq.append((nx, ny))                                                                          #Append the coordinate of neighbor to nextq.
            q = nextq                                                                                                   #Replace q with nextq.
            
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0                                                                                                       #Initialize count.
        m, n = len(grid), len(grid[0])                                                                                  #Get the dimensions.
        for i, j in product(range(m), range(n)):                                                                        #Traverse grid.
            if grid[i][j] == '1':                                                                                       #If grid is '1', increase count and do BFS to mark the island as visited.
                count += 1
                self.BFS(grid, i, j)
        return count
