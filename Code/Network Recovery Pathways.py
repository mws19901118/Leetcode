class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        adjacentList = defaultdict(list)                            #Build the adjacent list skipping offline nodes.
        for x, y, c in edges:
            if online[x] and online[y]:
                adjacentList[x].append((y, c))

        @cache                                                      #Cache result.
        def canReach(limit: int) -> bool:                           #Check if can reach from node 0 to node n - 1 with min cost limit using Dijkstra.
            heap = [(-k, 0)]                                        #Initialize max heap.
            best = defaultdict(lambda: -1)                          #Store the max left cost available at each node.
            best[0] = k
            while heap:                                             #Iterate while the heap is not empty.
                r, x = heapq.heappop(heap)                          #Pop the max heap.
                r = -r
                if r < best[x]:                                     #If r < best[x], the current node and remaining capacity is obsolete, so skip it.
                    continue
                for y, c in adjacentList[x]:                        #Traverse neighbors.
                    if c > r or c < limit or best[y] >= r - c:      #If the cost of edge is greater than remaining or smaller than limit or the neighbor is visited with better remaning capacity, skip it. 
                        continue
                    if y == len(online) - 1:                        #If reaching node n - 1, return true.
                        return True
                    best[y] = r - c                                 #Update best[y].
                    heapq.heappush(heap, (-best[y], y))             #Push best[y] and y into the max heap.
            return False                                            #Return false at the end.

        start, end = 0, 1000000000
        while start <= end:                                         #Binary search for the result from 0 to 1000000000.
            mid = (start + end) // 2
            if canReach(mid) and not canReach(mid + 1):
                return mid
            elif not canReach(mid):
                end = mid - 1
            else:
                start = mid + 1
        return -1                                                   #Return -1 if cannot reach n - 1 from 0.
