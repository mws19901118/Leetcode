class Solution:
    def DFS(self, grid: List[List[int]], squares: int, visited: int, position: tuple) -> int:         #DFS.
        m, n = len(grid), len(grid[0])                                                                #Get the dimentions of grid.
        count = 0                                                                                     #Count unique paths from this square.
        for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:                                               #Traverse all 4 direction.
            nx, ny = position[0] + x, position[1] + y                                                 #Calculate new position.
            if nx >= 0 and nx < m and ny >= 0 and ny < n and grid[nx][ny] in [0, 2]:                  #New position should be valid and is 0 or 2.
                if grid[nx][ny] == 2:                                                                 #If it's 2, DFS reaches the end.
                    count += visited == squares                                                       #Check if visited squares eqauls the count of empty squares. If so, add 1 to count.
                    continue                                                                          #Continue.
                grid[nx][ny] = -1                                                                     #If it's 0, update grid cell so it's already walked.
                visited += 1                                                                          #Increase visited by 1.
                count += self.DFS(grid, squares, visited, (nx, ny))                                   #Keep DFS recursively.
                visited -= 1                                                                          #Decrease visited by 1.
                grid[nx][ny] = 0                                                                      #Restore the grid cell.
        return count                                                                                  #Return count.
        
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        start = (-1, -1)
        squares = 0                                                                                   
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:                                                                   #Find start position.
                    start = (i, j)
                elif grid[i][j] == 0:                                                                 #Count empty squares.
                    squares += 1
        return self.DFS(grid, squares, 0, start)                                                      #Return the result of DFS.
