class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        m, n = len(maze), len(maze[0])                                                        #Get the dimensions.
        directions = [(-1, 0, 'u'), (0, 1, 'r'), (1, 0, 'd'), (0, -1, 'l')]                   #List all the directions and corresponding instruction.
        visited = set()                                                                       #Store all visited coordinates.
        heap = [(0, "", ball[0], ball[1])]                                                    #Use a min heap to store all coordinates pending visiting, maintaining the order by the total distance so far and instruction.
        while heap:                                                                           #Iterate while heap is not empty.
            d, path, x, y = heapq.heappop(heap)                                               #Pop heap.
            if (x, y) in visited:                                                             #If current coordinate is visited, skip it.
                continue
            if [x, y] == hole:                                                                #If the ball reaches the hole, directly return path as it this is the first shortest distance with lexicographically smallest instruction.
                return path
            visited.add((x, y))                                                               #Mark current coordinate as visited.
            for u, v, p in directions:                                                        #Traverse 4 directions.
                i, j, k = x, y, 0
                while 0 <= i + u < m and 0 <= j + v < n and not maze[i + u][j + v]:           #Ball move towards current direction until it hits border or wall.
                    i += u
                    j += v
                    k += 1
                    if [i, j] == hole:                                                        #If current coordinate is hole, also stop.
                        break
                heapq.heappush(heap, (d + k, path + p, i, j))                                 #Push the new coordinate with update distance and instruction to heap.
        return "impossible"                                                                   #Return "impossible" if cannot reach hole.
