class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()                                                        #Sort intervals by start.
        result = []
        i = 0
        while i < len(intervals):                                               #Traverse through intervals.
            end = intervals[i][1]
            j = i + 1
            while j < len(intervals) and intervals[j][0] <= end:                #Find all intervals overlapping with current interval.
                end = max(end, intervals[j][1])                                 #Update the end of current interval.
                j += 1
            result.append([intervals[i][0], end])                               #Append the merged intervals.
            i = j                                                               #Go to next interval.
        return result
