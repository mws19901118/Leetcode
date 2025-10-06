class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)                                                          #Get the dimension.
        heap = [(grid[0][0], 0, 0)]                                            #Initialize the min heap with time to reach grid[0][0] and the cell coordinate.
        visited = set()                                                        #Store visited cells.
        while heap:                                                            #Iterate while heap is not empty.
            t, x, y = heapq.heappop(heap)                                      #Pop the top of heap.
            if x == n - 1 and y == n - 1:                                      #If reaches destination, return current time t.
                return t
            if (x, y) in visited:                                              #If the cell is visited, skip.
                continue
            visited.add((x, y))                                                #Mark current cell as visited.
            for u, v in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]:      #Traverse 4 neighbors.
                if u < 0 or u >= n or v < 0 or v >= n or (u, v) in visited:    #If neighbor is invalid or visited, skip.
                    continue
                heapq.heappush(heap, (t + max(0, grid[u][v] - t), u, v))       #Add the time to reach neighbor from current cell and neighbor cell coordinate to heap.
