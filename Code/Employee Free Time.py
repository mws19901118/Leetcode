"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        allIntervals = []                                                                                        #Put all inervals as tuple in one list.
        for employee in schedule:
            allIntervals.extend([(x.start, x.end) for x in employee])
        allIntervals.sort()                                                                                      #Sort the list.
        index = 0
        occupiedTime = []                                                                                        #Store the union of occupied time intervals.
        while index < len(allIntervals):                                                                         #Traverse all intervals.
            end = allIntervals[index][1]                                                                         #Get the end of current interval.
            i = index + 1
            while i < len(allIntervals) and allIntervals[i][0] <= end:                                           #Traverse from index + 1 until its start is greater than current end.
                end = max(end, allIntervals[i][1])                                                               #Update end.
                i += 1
            occupiedTime.append((allIntervals[index][0], end))                                                   #Append current occupied time interval.
            index = i
        return [Interval(occupiedTime[i][1], occupiedTime[i + 1][0]) for i in range(len(occupiedTime) - 1)]      #The gap between the end and next start of each pair of adjacent occupied time intervals is the free time.
