# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        def intervalCmp(a,b):                                                                 #Define new cmp function to sort intervals according to the 'start' value.
            return a.start-b.start
        
        if intervals==[]:
            return []
        intervals.sort(cmp=intervalCmp)                                                       #Sort the list.
        
        result=[]
        result.append(intervals[0])                                                           #Append the 1st element of intervals to result.
        l=len(intervals)
        for i in range(1,l):
            if intervals[i].end>=result[-1].start and intervals[i].start<=result[-1].end:     #If the intervals[i] overlaps result[-1], update the start value and end value of result[-1].
                result[-1].start=min(intervals[i].start,result[-1].start)
                result[-1].end=max(intervals[i].end,result[-1].end)
            if intervals[i].start>result[-1].end:                                             #If the intervals[i].start>result[-1].end, it doesn't overlap result[-1], so append it to the result.
                result.append(intervals[i])
        return result
