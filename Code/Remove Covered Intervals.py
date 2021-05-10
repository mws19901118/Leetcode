class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        def cmp(a: List[int], b: List[int]) -> int:                                                 #Sort intervals by start asendingly then by end desendingly.
            if a[0] != b[0]:
                return a[0] - b[0]
            else:
                return b[1] - a[1]

        intervals.sort(key = cmp_to_key(cmp))
        last, count = 0, len(intervals)                                                             #Store the index of last uncovered interval, initially 0. Intialize count as the length of intervals.
        for i in range(1, len(intervals)):                                                          #Traverse starting from 1.
            if intervals[i][0] >= intervals[last][0] and intervals[i][1] <= intervals[last][1]:     #If current interval is covered by last uncovered interval, subtract count by 1.
                count -= 1
            else:                                                                                   #Otherwise, update the index of last uncovered interval.
                last = i
        return count                                                                                #Return count.
