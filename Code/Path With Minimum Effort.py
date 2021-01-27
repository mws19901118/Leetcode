class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:                             #Dijkstra algorithm.
        m, n = len(heights), len(heights[0])                                                  #Get dimensions of heights.
        efforts = [[1000001] * n for _ in range(m)]                                           #Initialize min efforts at each cell with a value greater than max value of height.
        efforts[0][0] = 0                                                                     #Set the min effort at starting cell to be 0.
        heap = [(0, 0, 0)]                                                                    #Put all currently reachable cells into a heap, priority ordered by the corresponding current effort;
        while heap:
            effort, x, y = heapq.heappop(heap)                                                #Pop heap.
            if x == m - 1 and y == n - 1:                                                     #If reaches destination, return corresponding effort.
                return effort
            for nx, ny in [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]:                   #Traverse all neighbors of current cell.
                if m > nx >= 0 <= ny < n:
                    newEffort = max(effort, abs(heights[nx][ny] - heights[x][y]))             #Update the min effort of neightbor and push to heap if necessary.
                    if efforts[nx][ny] > newEffort:
                        efforts[nx][ny] = newEffort
                        heapq.heappush(heap, (newEffort, nx, ny))
