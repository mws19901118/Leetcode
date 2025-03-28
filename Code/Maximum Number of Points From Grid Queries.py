class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])                                                #Get the dimensions.
        point = 0                                                                     #Initialize point.
        sorted_queries = sorted([(x, i) for i, x in enumerate(queries)])              #Sort queryies and keep original index.
        heap = [(grid[0][0], 0, 0)]                                                   #Store starting cells in a min heap order by the value.
        visited = set([(0, 0)])                                                       #Store visited cells.
        result = [0] * len(queries)                                                   #Initialize result.
        for query, index in sorted_queries:                                           #Traverse sorted queries.
            dq = deque()                                                              #Initialize a deque for current BFS.
            while heap and heap[0][0] < query:                                        #While the heap is not empty and the top of the heap has a smaller value than query, pop the heap and append the cell to the deque.
                _, x, y = heapq.heappop(heap)
                dq.append((x, y))
            while dq:                                                                 #BFS.
                x, y = dq.popleft()                                                   #Popleft the deque to get current cell.
                point += 1                                                            #Increase point because this is the first time visiting current cell.
                for u, v in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]:         #Traverse neighbors.
                    if u < 0 or u >= m or v < 0 or v >= n or (u, v) in visited:       #If the neighbor is invalid or visited, skip.
                        continue
                    if grid[u][v] >= query:                                           #If the neighbor has a value greater than or equal to query, push it to the heap for future queries.
                        heapq.heappush(heap, (grid[u][v], u, v))
                    else:                                                             #Otherwise, append neighbor to the deque.
                        dq.append((u, v))
                    visited.add((u, v))                                               #Mark the neighbor as visited.
            result[index] = point                                                     #After BFS, update result[index].
        return result
