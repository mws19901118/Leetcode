class Solution:
    def isPossible(self, target: List[int]) -> bool:
        total = sum(target)                       #Sum up the total number.
        heap = [-x for x in target]               #Use max heap to store elements.
        heapq.heapify(heap)
        while heap[0] != -1:                      #While the heap top is not 1.
            x = -heapq.heappop(heap)              #Pop heap.
            total -= x                            #Substract x from total, which is the previous sum.
            if x <= total or total < 1:           #If x <= total or total < 1, x cannot be set, return false.
                return False
            x %= total
            total += x
            heapq.heappush(heap, -x or -total)    #Push updated x back to heap.
        return True
