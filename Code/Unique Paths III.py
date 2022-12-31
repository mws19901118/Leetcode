class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])                                                      #Get the demensions.
        squares, start = 1, (-1, -1)                                                        #Intialize total unvisted empty square count and starting square.                                                    
        for i, j in product(range(m), range(n)):
            if grid[i][j] == 1:                                                             #Find start position.
                start = (i, j)
            elif grid[i][j] == 0:                                                           #Count empty squares.
                squares += 1

        def DFS(x: int, y: int, squares: int) -> int:
            if grid[x][y] == 2:                                                             #If reaches the ending square, only when there is no unvisited squares, there is a way to walk over all non-obstacle square once. 
                return int(squares == 0)
            count = 0                                                                       #Initialzie the count of ways from current square.                                                        
            grid[x][y] = -1                                                                 #Since cannot visit current square twice, mark it as -1 to work as obstacle.
            for nx, ny in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]:                 #Traverse all neighbors.
                if nx >= 0 and nx < m and ny >= 0 and ny < n and grid[nx][ny] != -1:        #If neighbor is valid and not obstacle, keep DFS.
                    count += DFS(nx, ny, squares - 1)
            grid[x][y] = 0                                                                  #Restore current square to empty.
            return count                                                                    #Return count.

        return DFS(start[0], start[1], squares)                                             #Return the result of DFS.
