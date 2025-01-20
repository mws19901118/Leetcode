class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])                                                                                    #Get dimensions.
        heap = [(heightMap[i][j], i, j) for i, j in product(range(m), range(n)) if i == 0 or j == 0 or i == m - 1 or j == n - 1]    #Find all the edge cells.
        heapq.heapify(heap)                                                                                                         #Store them in a min heap by the height.
        visited = set()                                                                                                             #Store visited cells in a set.
        count = 0                                                                                                                   #Initialize count.
        while heap:                                                                                                                 #Iterate while heap is not empty.
            h, x, y = heapq.heappop(heap)                                                                                           #Pop top of heap.
            if (x, y) in visited:                                                                                                   #If current cell is visited, skip.
                continue
            count += max(0, h - heightMap[x][y])                                                                                    #Add the difference between watermark and current cell height to count if it is greater than 0.
            for u, v in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]:                                                           #Traverse 4 neighbors.
                if u < 0 or u >= m or v < 0 or v >= n or (u, v) in visited:                                                         #If neighbor is invalid or visited, skip.
                    continue
                heapq.heappush(heap, (max(h, heightMap[u][v]), u, v))                                                               #Push neighbor and new watermark(higher of current watermark and height of neighbor) to heap.
            visited.add((x, y))                                                                                                     #Mark current cell as visited.
        return count
