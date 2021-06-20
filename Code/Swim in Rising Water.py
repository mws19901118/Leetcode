class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visited = [[False for j in range(len(grid))] for i in range(len(grid))]                             #Indicate if current squre has been visited.
        heap = [(grid[0][0], (0, 0))]                                                                       #Use a min heap to store the unvisited squares(elevation and coordinate) surronding visited area, initially it's the top left square.
        while not visited[len(grid) - 1][len(grid) - 1]:                                                    #Iterate while the bottom right square is unvisited.
            time, start = heapq.heappop(heap)                                                               #Pop heap to get the time and coordinate of next squre to start BFS.
            q = [start]                                                                                     #Initailize queue for BFS.
            while q:                                                                                        #BFS.
                nextq = []
                for x, y in q:                                                                              #Traverse coordinates in queue.
                    visited[x][y] = True                                                                    #Set current squre to be visited.
                    for nx, ny in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]:                         #Traverse 4 neighbors.
                        if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid) or visited[nx][ny]:       #If neighbor is invalid or visited, continue.
                            continue
                        if grid[nx][ny] <= time:                                                            #If we can swim to neighbor, set it to visited and add it to nextq.
                            visited[nx][ny] = True
                            nextq.append((nx, ny))
                        else:                                                                               #Otherwise, push the elevation and coordinate to heap
                            heapq.heappush(heap, (grid[nx][ny], (nx, ny)))
                q = nextq                                                                                   #Replace q with nextq.
        return time                                                                                         #Return time at the end.
