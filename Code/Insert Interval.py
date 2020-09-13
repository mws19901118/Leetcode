class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:                                             #Traverse through intervals until current interval's start is larger than new interval's end.
            if intervals[i][1] < newInterval[0]:                                                                    #If current interval's end is smaller than new interval's start, add current interval to result.
                result.append(intervals[i])
            else:                                                                                                   #Otherwise merge current interval with new interval.
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
            i += 1
        result.append(newInterval)                                                                                  #Add new interval to result.
        result.extend(intervals[i:])                                                                                #Add remaining intervals to result.
        return result
