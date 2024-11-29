class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])                                              #Get the dimensions.
        if grid[1][0] > 1 and grid[0][1] > 1:                                       #If the top left corner is surrounded by cells it cannot reach directly, return -1 as it is impossible to proceed.
            return -1
        heap = [(0, 0, 0)]                                                          #Initialize heap.
        visited_time = {(0, 0): 0}                                                  #Store the earliest visited time for each cell.
        while heap:                                                                 #Iterate while heap is not empty.
            t, x, y = heapq.heappop(heap)                                           #Pop heap top.
            if x == m - 1 and y == n - 1:                                           #If reaches the bottom right corner, return current time.
                return t
            for u, v in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]:           #Traverse 4 neighbors.
                if u < 0 or u >= m or v < 0 or v >= n:                              #If neighbor is invalid, skip.
                    continue
                next_t = (max(grid[u][v] - t, 0) | 1) + t                           #Calculate the time to visit neighbor: if can direct visit, time is t + 1; otherwise, take some steps back and forth in already visited area and return to current location, so the steps taken is always an even number, then an extra step to reach neighbor.
                if (u, v) in visited_time and visited_time[(u, v)] <= next_t:       #If neighbord is already visited in a not later time, skip.
                    continue
                visited_time[(u, v)] = next_t                                       #Set the visited time for neighbor.
                heapq.heappush(heap, (next_t, u, v))                                #Push visited time and cell location to heap.
