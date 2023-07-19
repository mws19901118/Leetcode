class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()                                          #Sort intervals by beginnings.
        count, end = 0, float('-inf')                             #Initialize count and current interval end.
        for x, y in intervals:                                    #Traverse intervals.
            if x < end:                                           #If x < end, there is a overlap, so increase count.
                count += 1
                end = min(end, y)                                 #And always take the interval with smaller end to reduce the chance of overlapping in the future.
            else:                                                 #Otherwise just update end to y.
                end = y
        return count
