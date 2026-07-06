class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[0], -x[1]))                                               #Sort intervals by start in ascending order then by end in descending order.
        last, count = 0, len(intervals)                                                             #Store the index of last uncovered interval, initially 0. Intialize count as the length of intervals.
        for i in range(1, len(intervals)):                                                          #Traverse starting from 1.
            if intervals[i][0] >= intervals[last][0] and intervals[i][1] <= intervals[last][1]:     #If current interval is covered by last uncovered interval, subtract count by 1.
                count -= 1
            else:                                                                                   #Otherwise, update the index of last uncovered interval.
                last = i
        return count                                                                                #Return count.
