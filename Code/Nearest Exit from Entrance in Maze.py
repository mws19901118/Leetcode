class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])                                                                                #Get dimensions.
        q = [(entrance[0], entrance[1])]                                                                              #Initialize queue.
        maze[entrance[0]][entrance[1]] = '-'                                                                          #Mark entrance as visited.
        step = 0                                                                                                      #Initialize step to exit.
        while q:                                                                                                      #BFS.
            newq = []                                                                                                 #Initialize newq.
            for x, y in q:                                                                                            #Traverse each position in q.
                if (x == 0 or x == m - 1 or y == 0 or y == n - 1) and (x, y) != (entrance[0], entrance[1]):           #If current position is on the border and not the entrance, return step.
                    return step
                for nx, ny in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]:                                       #Traverse 4 neighbors.
                    if 0 <= nx < m and 0 <= ny < n and maze[nx][ny] == '.':                                           #If neighbor is valid and empty cell, append it to newq and mark it as visited.
                        newq.append((nx, ny))
                        maze[nx][ny] = '-'
            q = newq                                                                                                  #Replace q with newq.
            step += 1                                                                                                 #Increase step.
        return -1                                                                                                     #Return -1 if cannot find exit.
