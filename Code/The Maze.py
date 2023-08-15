class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m, n = len(maze), len(maze[0])                                                        #Get dimensions.
        q = [start]                                                                           #Push start to queue.
        maze[start[0]][start[1]] = -1                                                         #Mark start position as visited.
        while q:                                                                              #BFS.
            newq = []
            for x, y in q:                                                                    #Traverse q.
                for u, v in [(-1, 0), (0, 1), (1, 0), (0, -1)]:                               #Traverse 4 directions.
                    i, j, k = x, y, 0
                    while 0 <= i + u < m and 0 <= j + v < n and maze[i + u][j + v] < 1:       #Find while the ball will stop.
                        i += u
                        j += v
                        k += 1
                    if [i, j] == destination:                                                 #If the ball stops at the destination, return True.
                        return True
                    if maze[i][j] == 0:                                                       #If the stop is not visited, append it to newq.
                        newq.append((i, j))                                                   #Note that if the stop is a passing cell of another move, there is also no need to keep BFS. Since the ball reachs wall and cannot go back and the vertial direction is already visited.
                    while k >= 1:                                                             #Mark all the passing cells as visited.
                        maze[i][j] = -1
                        k -= 1
                        i -= u
                        j -= v
            q = newq                                                                          #Replace q with newq.
        return False                                                                          #Return false if cannot reach.
