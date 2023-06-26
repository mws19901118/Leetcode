class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        result, heap = 0, []                                                  #Initialize result and a min heap.
        for x in costs[:candidates]:                                          #Push the first candidates number from front to heap with a flag saying they are not from end.
            heapq.heappush(heap, (x, 0))
        pointerFront = candidates                                             #Set the next number to push to heap from front.
        for x in costs[max(candidates, len(costs) - candidates):]:            #Push numnbers from end to heap starting wieh max(candidates, len(costs) - candidates) so there is no overlapping, also with a flag saying they are from end.
            heapq.heappush(heap, (x, 1))
        pointerEnd = max(candidates, len(costs) - candidates) - 1             #Set the next number to push to heap from end.
        for _ in range(k):                                                    #Iterate k times.
            c, isFromBehind = heapq.heappop(heap)                             #Pop the heap top.
            result += c                                                       #Add the cost to result.
            if pointerFront <= pointerEnd:                                    #If pointerFront <= pointerEnd, there are still numbers not pushed to heap.
                if not isFromBehind:                                          #If current number is from front, push costs[pointerFront] to heap with a flag saying it is not from end.
                    heapq.heappush(heap, (costs[pointerFront], 0))
                    pointerFront += 1
                else:                                                         #Otherwise, push costs[pointerEnd] to heap with a flag saying it is from end.
                    heapq.heappush(heap, (costs[pointerEnd], 1))
                    pointerEnd -= 1
        return result                                                         #Return result.
