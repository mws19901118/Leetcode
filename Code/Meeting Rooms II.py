class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        points = sorted([(x, 1) for x, y in intervals] + [(y, -1) for x, y in intervals])           #Break intervals to points, 1 for start point and -1 for end point.
        count, result = 0, 0                                                                        #Initialize meeting room count and result.
        for x, y in points:                                                                         #Traverse points.
            count += y                                                                              #Increase or decrease count depending on if it's start or end.
            result = max(result, count)                                                             #Update result if necessary.
        return result
