class Solution:
    def DFS(self, grid: List[List[int]], squares: int, path: List[tuple], position: tuple) -> int:    #DFS.
        m, n = len(grid), len(grid[0])                                                                #Get the dimentions of grid.
        count = 0                                                                                     #Count unique paths from this square.
        for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:                                               #Traverse all 4 direction.
            nx, ny = position[0] + x, position[1] + y                                                 #Calculate new position.
            if nx >= 0 and nx < m and ny >= 0 and ny < n and grid[nx][ny] in [0, 2]:                  #New position should be valid and is 0 or 2.
                if grid[nx][ny] == 2:                                                                 #If it's 2, DFS reaches the end.
                    count += len(path) == squares                                                     #Check if the length of path eqauls the count of non-obstacle squares. If so, add 1 to count.
                    continue                                                                          #Continue.
                grid[nx][ny] = -1                                                                     #If it's 0, update grid cell so it's already walked.
                path.append((nx, ny))                                                                 #Add it to path.
                count += self.DFS(grid, squares, path, (nx, ny))                                      #Keep DFS recursively.
                path.pop()                                                                            #Pop from path.
                grid[nx][ny] = 0                                                                      #Restore the grid cell.
        return count                                                                                  #Return count.
        
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        start = (-1, -1)
        squares = 1                                                                                   
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:                                                                   #Find start position.
                    start = (i, j)
                elif grid[i][j] == 0:                                                                 #Count non-obstacle squares(except end).
                    squares += 1
        return self.DFS(grid, squares, [(start)], start)                                              #Return the result of DFS.
