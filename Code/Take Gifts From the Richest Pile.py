class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = [-x for x in gifts]        #Store gifts in a max heap.
        heapq.heapify(heap)
        for i in range(k):                #Iterate k times.
            x = -heapq.heappop(heap)      #Pop the top of heap.
            r = floor(sqrt(x))            #Calculate the floor of square root.
            heapq.heappush(heap, -r)      #Add it back to heap.
        return -sum(heap)                 #Return the sum of heap.
