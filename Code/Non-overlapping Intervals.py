class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()                                          #Sort intervals by beginnings.
        count, i, j = 0, 0, 1                                     #Initalize count and 2 pointers.
        while j < len(intervals):                                 #Traverse intervals until interval j reaches the end.
            if intervals[j][1] <= intervals[i][1]:                #If interval j is fully covered by interval i, remove interval i and move interval i to interval j. 
                count += 1
                i = j
            elif intervals[j][0] < intervals[i][1]:               #Else if interval j's beginning is smaller than interval i's end, remove interval j.
                count += 1
            else:                                                 #Otherwise, move interval i to interval j.
                i = j
            j += 1                                                #Interval j goes to the next.
        return count                                              #Return count.
