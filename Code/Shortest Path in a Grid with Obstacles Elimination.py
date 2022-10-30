class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])                                                                                                                                      #Get dimensions.
        q = [(0, 0, k)]                                                                                                                                                     #Initialize q with upper left cell and number of obstacles I can remove now.
        visited = {(x, y): (m * n + 1, -1) for x, y in product(range(m), range(n))}                                                                                         #Store the step and remaining move can for visiting each cell, initially m * n + 1 and -1 respectively.
        step = 0                                                                                                                                                            #Initialize step.
        while q:                                                                                                                                                            #Begin BFS.
            newq = []                                                                                                                                                       #Initialize newq.
            for x, y, r in q:                                                                                                                                               #Traverse q.
                if x == m - 1 and y == n - 1:                                                                                                                               #If reaches lower right cell, return current step.
                    return step
                for nx, ny in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]:                                                                                             #Traverse 4 neighbors of current cell.
                    if nx < 0 or nx >= m or ny < 0 or ny >= n or r < grid[nx][ny] or (visited[(nx, ny)][0] <= step and visited[(nx, ny)][1] >= r - grid[nx][ny]):           #If next cell is not valid or it's an obstacle and we don't have move remaining or it's visited with lesser step and more moves remaining, we should skip it. 
                        continue
                    visited[(nx, ny)] = (step, r - grid[nx][ny])                                                                                                            #Update the step and remaining move for visiting this cell.
                    newq.append((nx, ny, r - grid[nx][ny]))                                                                                                                 #Append (nx, ny, r - grid[nx][ny]) to newq.
            q = newq                                                                                                                                                        #Replace q with newq.
            step += 1                                                                                                                                                       #Increase step.
        return -1          
