class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])                                                                                            #Get dimensions.
        q = [(0, 0, k)]                                                                                                           #Initialize q with upper left cell and number of obstacles I can remove now.
        visited = {}                                                                                                              #Store the max number of obstacles can remove at each visited cell.
        step = 0                                                                                                                  #Initialize step.
        while q:                                                                                                                  #Begin BFS.
            newq = []                                                                                                             #Initialize newq.
            for x, y, c in q:                                                                                                     #Traverse q.
                if x == m - 1 and y == n - 1:                                                                                     #If reaches lower right cell, return current step.
                    return step
                for nx, ny in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]:                                                   #Traverse 4 neighbors of current cell.
                    if nx >= 0 and nx < m and ny >= 0 and ny < n and ((nx, ny) not in visited or visited[(nx, ny)] < c):          #Next cell has to be valid and either is not visited or is visited with a smaller number of obstacles can remove.
                        if grid[nx][ny] == 0:                                                                                     #If next cell is not obstacle, append its coordinate with same number of obstacles to remove to newq and add in visit.
                            visited[(nx, ny)] = c
                            newq.append((nx, ny, c))
                        elif grid[nx][ny] == 1 and c > 0:                                                                         #Else if next cell is obstacle and we can remove it, append its coordinate with number of obstacles minus 1 to remove to newq and add in visit.
                            visited[(nx, ny)] = c - 1
                            newq.append((nx, ny, c - 1))
            q = newq                                                                                                              #Replace q with newq.
            step += 1                                                                                                             #Increase step.
        return -1                                                                                                                 #Return -1 if cannot reach lower right cell.
