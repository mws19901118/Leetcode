class SeatManager:

    def __init__(self, n: int):
        self.heap = [i for i in range(1, n + 1)]          #Store all seats in a min heap.
        heapq.heapify(self.heap)

    def reserve(self) -> int:
        return heapq.heappop(self.heap)                   #Pop the top of heap.

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.heap, seatNumber)             #Push seatNumber to heap.


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
