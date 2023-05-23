class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k                                #Store k.
        self.heap = []                            #Initialize a min heap.
        for x in nums:                            #Add all value in nums to heap.
            self.add(x)
    
    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)            #Return heap top.
        if len(self.heap) > self.k:               #Insert value into heap and maintain heap length.
            heapq.heappop(self.heap)
        return self.heap[0]                       #Return heap top.

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
