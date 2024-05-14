class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m, n = len(maze), len(maze[0])                                                            #Get the dimensions.
        q = [(start[0], start[1], 0)]                                                             #Initialize queue to be the starting cell and 0 distance.
        result = float('inf')                                                                     #Initialize result to be positive infinity.
        visited = {}                                                                              #Store the min distance visiting cell (x, y) with direction (u, v).
        while q:                                                                                  #BFS.
            newq = []                                                                             #Initialize new queue.
            for x, y, d in q:                                                                     #Traverse q.
                if d >= result:                                                                   #If d is already not smaller than result, skip.
                    continue
                for u, v in [(-1, 0), (0, 1), (1, 0), (0, -1)]:                                   #Traverse 4 directions.
                    if (x, y, u, v) in visited and visited[(x, y, u, v)] <= d :                   #If current cell and direction is already visited and the distance is smaller than or equal to current than current distance, skip as no need to traverse it again.
                        continue
                    i, j, k = x, y, 0                                                             #Initialize i, j, k to move the ball.
                    while 0 <= i + u < m and 0 <= j + v < n and maze[i + u][j + v] == 0:          #Move the ball in direction (u, v) while the ball is in empty cells.
                        i += u
                        j += v
                        k += 1
                    if [i, j] == destination:                                                     #If the ball stops at destination, update result.
                        result = min(result, d + k)
                    newq.append((i, j, d + k))                                                    #Append stop cell and new distance to newq.
                    visited[(x, y, u, v)] = d                                                     #Update visited[(x, y, u, v)].
            q = newq                                                                              #Replace q with newq.
        return result if result < float('inf') else -1                                            #If result is not positive infinity, return result; otherwise return -1 as the ball cannot stop at destination.
