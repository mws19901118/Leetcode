class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        startingPoints = [(x[0], i) for i, x in enumerate(intervals)]                                       #Put the starting point and index of each interval in a list and then sort in ascending order.
        startingPoints.sort()
        result = []
        for x in intervals:                                                                                 #For each interval, binary search the first starting point in the list which is eqaul to or larger than the interval's ending point.
            start, end = 0, len(intervals) - 1
            while start <= end:
                mid = (start + end) // 2
                if startingPoints[mid][0] >= x[1] and (mid == 0 or startingPoints[mid - 1][0] < x[1]):
                    result.append(startingPoints[mid][1])                                                   #If found, append the index to result.
                    break
                elif startingPoints[mid][0] < x[1]:
                    if mid == len(intervals) - 1:
                        result.append(-1)                                                                   #If not found, append -1.
                    start = mid + 1
                else:
                    end = mid - 1
        return result
