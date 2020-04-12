import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-stone for stone in stones]            #Use the negative value of each stone to form a max heap.
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:                           #While there are more than 1 stone in heap, simulate the process.
            y = -heapq.heappop(maxHeap)                   #Find the heaviest stone y.
            x = -heapq.heappop(maxHeap)                   #Find the second heaviest stone x.
            if x < y:                                     #If x < y, push x - y(weight y - x) to max heap.
                heapq.heappush(maxHeap, x - y)
        if len(maxHeap) == 1:                             #If only 1 stone left, return its weight.
            return -maxHeap[0]
        else:                                             #Otherwise return 0.
            return 0
