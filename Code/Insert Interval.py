# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        def intervalCmp(a,b):                                                                                   #Define new cmp function to sort intervals according to the 'start' value.
            return a.start-b.start
        
        result=[]
        if intervals==[]:                                                                                       #If the list is empty. append the new interval to result and return the result.
            result.append(newInterval)
            return result
        
        intervals.sort(cmp=intervalCmp)                                                                         #Sort the list.
        l=len(intervals)
        i=0
        while i<l:
            while i<l and intervals[i].end<newInterval.start:                                                   #If the intervals[i].end<newInterval.start, it doesn't overlap the new interval, so append it to the result.
                result.append(intervals[i])
                i+=1
            while i<l and intervals[i].end>=newInterval.start and intervals[i].start<=newInterval.end:          #If the intervals[i] overlaps the new interval, update the start value and end value of the new interval.
                newInterval.start=min(intervals[i].start,newInterval.start)
                newInterval.end=max(intervals[i].end,newInterval.end)
                i+=1
            result.append(newInterval)                                                                          #Append the new interval to the result.
            while i<l and intervals[i].start>newInterval.end:                                                   #If the intervals[i].start>newInterval.end, it doesn't overlap the new interval, so append it to the result.
                result.append(intervals[i])
                i+=1
        return result
