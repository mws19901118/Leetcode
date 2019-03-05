# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
import heapq
class Solution:
    def employeeFreeTime(self, schedule: List[List[Interval]]) -> List[Interval]:
        heap = []
        for s in schedule:                                              #Put each interval in a list as list.
            for i in s:
                heap.append([i.start, i.end])
        
        heapq.heapify(heap)                                             #Heapify list to build a min heap so it's ordered by start time.
        periods = []                                                    #Store merged intervals as list. 
        period = [-1, -1]                                               #Initialize a dummy starter.
        while len(heap):                                                #While there is elements in min heap.
            x = heapq.heappop(heap)                                     #Pop the heap top.
            if x[0] <= period[1]:                                       #If it's overlapping with current interval, merge it with current interval.
                period[1] = max(period[1], x[1])
            else:                                                       #Otherwise, append the current interval to periods and use it as new current interval.
                periods.append(period)
                period = x
        periods.append(period)                                          #Append the last current interval to periods.
        
        result = []
        for i in range(1, len(periods) - 1):                            #Traverse periods from 1, because of the dummy starter.
            result.append(Interval(periods[i][1], periods[i + 1][0]))   #The gap between each interval is free time, convert them to interval.
        return result
