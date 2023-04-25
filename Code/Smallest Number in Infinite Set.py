class SmallestInfiniteSet:

    def __init__(self):
        self.heap = []                                                                      #Use heap to maintain the order of added back numbers.
        self.poppedAtLeastOnce = set()                                                      #Also store them in a set.
        self.smallestUnpopped = 1                                                           #Store the smallest unpopped number.

    def popSmallest(self) -> int:
        if self.heap:                                                                       #If heap is not empty, pop the top of heap.
            x = heapq.heappop(self.heap)
            self.poppedAtLeastOnce.remove(x)                                                #Also remove x from set.
            return x                                                                        #Return x.
        self.smallestUnpopped += 1                                                          #Otherwise, increase smallest unpopped number and return prevous value.
        return self.smallestUnpopped - 1

    def addBack(self, num: int) -> None:
        if num not in self.poppedAtLeastOnce and num < self.smallestUnpopped:               #If num is not in set and is smaller than smallest unpopped number, it has been popped before, so push it to heap and add it to set.
            heapq.heappush(self.heap, num)
            self.poppedAtLeastOnce.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
