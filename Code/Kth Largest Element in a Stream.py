class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k                                #Store k.
        self.heap = []                            #Initialize a min heap.
        for x in nums:                            #Push all value in nums to heap.
            self.push(x)

    def add(self, val: int) -> int:
        self.push(val)                            #Push value to heap.
        return self.heap[0]                       #Return heap top.
    
    def push(self, val: int):                     #Insert value into heap and maintain heap length.
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
