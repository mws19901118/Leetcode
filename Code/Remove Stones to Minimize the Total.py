class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        maxHeap = [-p for p in piles]                     #Initialize a max heap.
        heapq.heapify(maxHeap)
        for _ in range(k):                                #Iterate k times.
            x = heapq.heappop(maxHeap)                    #Pop the largest pile.
            heapq.heappush(maxHeap, x + (-x) // 2)        #Remove half of stones then push back to heap.
        return -sum(maxHeap)                              #Return count of remain stones.
