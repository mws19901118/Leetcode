from sortedcontainers import SortedDict                                       #Import SortedDict.
class MyCalendarThree:

    def __init__(self):
        self.endTimesByStartTime = SortedDict()                               #Use sorted dict to store the end time of each start time.
        self.maxBooking = 1                                                   #Intitialize maxBooking to be 1.

    def book(self, start: int, end: int) -> int:
        heap = []                                                             #Intitialize a heap.
        for x in self.endTimesByStartTime:                                    #Traverse endTimesByStartTime in ascending order.
            if x >= end:                                                      #If the start time is greater than current end time, stop.
                break
            while heap and heap[0] <= x:                                      #While heap is not empty and the heap top is not greater than current start time, pop heap.
                heapq.heappop(heap)
            for y in self.endTimesByStartTime[x]:                             #Traverse all the end times for x.
                if start <= x < end or x < start < y:                         #If xe is in [start, end) or start is in (x, y), current booking has intersection with booking [x, y].
                    heapq.heappush(heap, y)                                   #Add y to heap.
            self.maxBooking = max(self.maxBooking, len(heap) + 1)             #The length of heap plus 1 is the size of intersection, so update maxBooking if necessary.
        self.endTimesByStartTime.setdefault(start, [])                        #Set endTimesByStartTime[start] to empty list if start not already exist in endTimesByStartTime.
        self.endTimesByStartTime[start].append(end)                           #Append end to endTimesByStartTime[start].
        return self.maxBooking                                                #Return maxBooking.

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
