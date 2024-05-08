class Solution:
    def minCost(self, n: int, roads: List[List[int]], appleCost: List[int], k: int) -> List[int]:
        adjacentList = defaultdict(list)                                                #Build adjacent list.
        for a, b, c in roads:
            adjacentList[a].append((b, c))
            adjacentList[b].append((a, c))
        result = deepcopy(appleCost)                                                    #Initialize result for each city to buy apple at itself.
        heap = [(x, i + 1) for i, x in enumerate(appleCost)]                            #Initialize min heap for the cost for each city to buy apple through certain path.
        heapq.heapify(heap)
        while heap:                                                                     #Iterate while heap is not empty.
            cost, city = heapq.heappop(heap)                                            #Pop the cost and city at heap top.
            if result[city - 1] < cost:                                                 #If the result of current city is already smaller than current cost, skip.
                continue
            for neighbor, cost in adjacentList[city]:                                   #Traverses neighbor of current city
                if result[neighbor - 1] > result[city - 1] + (k + 1) * cost:            #If it costs less for neighbor to come to current city and follow how current city buy apple, update the result of neighbor.
                    result[neighbor - 1] = result[city - 1] + (k + 1) * cost
                    heapq.heappush(heap, (result[neighbor - 1], neighbor))              #Also push neighbor and its new cost to heap.
        return result
