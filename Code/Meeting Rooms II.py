# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
import heapq
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        def cmpInterval(a, b):
            return a.start - b.start
        intervals.sort(cmp = cmpInterval)                     #Sort the list according to the start time.
        rooms = 0                                             #Record the rooms needed at current time.
        result = 0                                            #Record the max rooms needed.
        endtimes = []                                         #Use a heap to store the end times.
        for x in intervals:
            while endtimes != [] and endtimes[0] <= x.start:  #When comes to a interval, remove all the meeting finished before current meeting starts from heap and release correspoding rooms.
                heapq.heappop(endtimes)
                rooms -= 1
            heapq.heappush(endtimes, x.end)                   #Push the end time of current meeting to the heap.
            rooms += 1                                        #Current meeting occupies a room.
            result = max(rooms, result)                       #Update result.
        return result
