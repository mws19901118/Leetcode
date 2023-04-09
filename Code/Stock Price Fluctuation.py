class StockPrice:

    def __init__(self):
        self.latestTime = -1                                                            #Store the latest timestamp.
        self.prices = {}                                                                #Store prices at each timestamp.
        self.minHeap = []                                                               #Store the prices in a min heap.
        self.maxHeap = []                                                               #Store the prices in a max heap.

    def update(self, timestamp: int, price: int) -> None:
        self.latestTime = max(timestamp, self.latestTime)                               #Update lastest timestamp.
        self.prices[timestamp] = price                                                  #Upsert prices at given timestamp.
        heapq.heappush(self.minHeap, (price, timestamp))                                #Push price and timestamp in min heap.
        heapq.heappush(self.maxHeap, (-price, timestamp))                               #Push price and timestamp in max heap.

    def current(self) -> int:
        return self.prices[self.latestTime]                                             #Return the price at latest timestamp.

    def maximum(self) -> int:
        while -self.maxHeap[0][0] != self.prices[self.maxHeap[0][1]]:                   #While the price at top of max heap does not match the current price at that timestamp, pop max heap.
            heapq.heappop(self.maxHeap)
        return -self.maxHeap[0][0]                                                      #Return the price at top of max heap.

    def minimum(self) -> int:
        while self.minHeap[0][0] != self.prices[self.minHeap[0][1]]:                    #While the price at top of min heap does not match the current price at that timestamp, pop min heap.
            heapq.heappop(self.minHeap)
        return self.minHeap[0][0]                                                       #Return the price at top of min heap.

# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
