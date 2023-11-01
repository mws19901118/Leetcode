class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        heaps = [[] for _ in range(len(workers))]                              #For each worker, store the distance to each bike and index of bike in a min heap.
        for i, (x, y) in enumerate(workers):                                   #Traverse workers.
            for j, (u, v) in enumerate(bikes):                                 #Traverse bikes.
                heapq.heappush(heaps[i], (abs(x - u) + abs(y - v), j))         #Populate heaps[i].
        heap = []                                                              #For all unused worker, store the nearest bike distance and index of worker and index of bike.
        for i, h in enumerate(heaps):                                          #Traverse heaps.
            d, j = heapq.heappop(h)                                            #Pop current heap.
            heapq.heappush(heap, (d, i, j))                                    #Populate heap.
        visitedWorker, usedBike = set(), set()                                 #Use set to store used workers and used bikes.
        result = [-1] * len(workers)                                           #Initialize result array.
        while len(visitedWorker) < len(workers):                               #Iterate while not all workers are visited.                       
            d, i, j = heapq.heappop(heap)                                      #Pop heap.
            if j not in usedBike:                                              #If bike j is not used, assign bike j to worker i then update visitedWorker and usedBike.
                result[i] = j
                visitedWorker.add(i)
                usedBike.add(j)
            elif heaps[i]:                                                     #Otherwise, pop the next pair in heaps[i] and push it to heap with i.
                next_d, next_j = heapq.heappop(heaps[i])
                heapq.heappush(heap, (next_d, i, next_j))
        return result
