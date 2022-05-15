class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjacentList = [defaultdict(int) for _ in range(n + 1)]                             #Build graph.
        for u, v, w in times:
            adjacentList[u][v] = w
        time = [float('inf') for _ in range(n + 1)]                                         #Initialize time at each node to be infinity.
        time[k], heap = 0, (0, k)]                                                          #Set time[k] to 0 and add (0, k) to heap.
        while heap:                                                                         #Iterate while heap is not empty.
            currentTime, x = heapq.heappop(heap)                                            #Pop heap.
            for y in adjacentList[x]:                                                       #Traverse all neighbors of current node.
                newTime = time[x] + adjacentList[x][y]                                      #Calculate time of y to receive signal from k through x.
                if newTime < time[y]:                                                       #Update the min time of y to receive signal and push to heap if necessary.
                    time[y] = newTime
                    heapq.heappush(heap, (time[y], y))
        return max(time[1:]) if all(x < float('inf') for x in time[1:]) else -1             #If all nodes can receive signal, return max(time[1:]); otherwise, return -1.
